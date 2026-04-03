---
id: port-killer-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:01.510250
---

# KNOWLEDGE EXTRACT: port-killer
> **Extracted on:** 2026-03-30 17:51:05
> **Source:** port-killer

---

## File: `.gitignore`
```
# Xcode
*.xcodeproj
*.xcworkspace
xcuserdata/
*.xcuserstate
*.xccheckout
*.xcscmblueprint
DerivedData/

# Swift Package Manager
.build/
.swiftpm/
Package.resolved

# macOS
.DS_Store
.AppleDouble
.LSOverride
._*

# Thumbnails
Thumbs.db

# Build outputs
*.app
*.dmg
*.ipa
*.dSYM.zip
*.dSYM

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# Temporary files
*.tmp
*.temp

# Sparkle tools (downloaded for signing)
sparkle_tools/
sparkle.tar.xz
sparkle_private_key
*.p12
*.cer
*.certSigningRequest

docs

# Node.js / Bun
node_modules/
bun.lockb

# .NET / Windows
**/bin/
**/obj/
*.user
*.suo
*.userprefs
.vs/
*.DotSettings.user

# Rust
**/target/
```

## File: `appcast.xml`
```xml
<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:sparkle="http://www.andymatuschak.org/xml-namespaces/sparkle" xmlns:dc="http://purl.org/dc/elements/1.1/">
  <channel>
    <title>PortKiller Updates</title>
    <link>https://github.com/productdevbook/port-killer</link>
    <description>Most recent updates to PortKiller</description>
    <language>en</language>
    <item>
      <title>Version 3.3.1</title>
      <pubDate>Mon, 16 Feb 2026 14:22:31 +0000</pubDate>
      <sparkle:version>194</sparkle:version>
      <sparkle:shortVersionString>3.3.1</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <enclosure
        url="https://github.com/productdevbook/port-killer/releases/download/v3.3.1/PortKiller-v3.3.1-macos.dmg"
        length="5525447"
        type="application/octet-stream"
        sparkle:edSignature="YOzI4CmdZmRitsF61LOQi/fQbefdkzEl5+xB/uIYvIMTyDAIZ9uJRf0K8+gHNywfLIZ7y3X2d49S0IzC0kc/CA==" />
    </item>
  </channel>
</rss>
```

## File: `bun.lock`
```
{
  "lockfileVersion": 1,
  "configVersion": 1,
  "workspaces": {
    "": {
      "name": "portkiller",
      "dependencies": {
        "bumpp": "^10.3.2",
      },
    },
  },
  "packages": {
    "ansis": ["ansis@4.2.0", "", {}, "sha512-HqZ5rWlFjGiV0tDm3UxxgNRqsOTniqoKZu0pIAfh7TZQMGuZK+hH0drySty0si0QXj1ieop4+SkSfPZBPPkHig=="],

    "args-tokenizer": ["args-tokenizer@0.3.0", "", {}, "sha512-xXAd7G2Mll5W8uo37GETpQ2VrE84M181Z7ugHFGQnJZ50M2mbOv0osSZ9VsSgPfJQ+LVG0prSi0th+ELMsno7Q=="],

    "bumpp": ["bumpp@10.3.2", "", { "dependencies": { "ansis": "^4.2.0", "args-tokenizer": "^0.3.0", "c12": "^3.3.2", "cac": "^6.7.14", "escalade": "^3.2.0", "jsonc-parser": "^3.3.1", "package-manager-detector": "^1.5.0", "semver": "^7.7.3", "tinyexec": "^1.0.2", "tinyglobby": "^0.2.15", "yaml": "^2.8.1" }, "bin": { "bumpp": "bin/bumpp.mjs" } }, "sha512-yUUkVx5zpTywLNX97MlrqtpanI7eMMwFwLntWR2EBVDw3/Pm3aRIzCoDEGHATLIiHK9PuJC7xWI4XNWqXItSPg=="],

    "c12": ["c12@3.3.2", "", { "dependencies": { "chokidar": "^4.0.3", "confbox": "^0.2.2", "defu": "^6.1.4", "dotenv": "^17.2.3", "exsolve": "^1.0.8", "giget": "^2.0.0", "jiti": "^2.6.1", "ohash": "^2.0.11", "pathe": "^2.0.3", "perfect-debounce": "^2.0.0", "pkg-types": "^2.3.0", "rc9": "^2.1.2" }, "peerDependencies": { "magicast": "*" }, "optionalPeers": ["magicast"] }, "sha512-QkikB2X5voO1okL3QsES0N690Sn/K9WokXqUsDQsWy5SnYb+psYQFGA10iy1bZHj3fjISKsI67Q90gruvWWM3A=="],

    "cac": ["cac@6.7.14", "", {}, "sha512-b6Ilus+c3RrdDk+JhLKUAQfzzgLEPy6wcXqS7f/xe1EETvsDP6GORG7SFuOs6cID5YkqchW/LXZbX5bc8j7ZcQ=="],

    "chokidar": ["chokidar@4.0.3", "", { "dependencies": { "readdirp": "^4.0.1" } }, "sha512-Qgzu8kfBvo+cA4962jnP1KkS6Dop5NS6g7R5LFYJr4b8Ub94PPQXUksCw9PvXoeXPRRddRNC5C1JQUR2SMGtnA=="],

    "citty": ["citty@0.1.6", "", { "dependencies": { "consola": "^3.2.3" } }, "sha512-tskPPKEs8D2KPafUypv2gxwJP8h/OaJmC82QQGGDQcHvXX43xF2VDACcJVmZ0EuSxkpO9Kc4MlrA3q0+FG58AQ=="],

    "confbox": ["confbox@0.2.2", "", {}, "sha512-1NB+BKqhtNipMsov4xI/NnhCKp9XG9NamYp5PVm9klAT0fsrNPjaFICsCFhNhwZJKNh7zB/3q8qXz0E9oaMNtQ=="],

    "consola": ["consola@3.4.2", "", {}, "sha512-5IKcdX0nnYavi6G7TtOhwkYzyjfJlatbjMjuLSfE2kYT5pMDOilZ4OvMhi637CcDICTmz3wARPoyhqyX1Y+XvA=="],

    "defu": ["defu@6.1.4", "", {}, "sha512-mEQCMmwJu317oSz8CwdIOdwf3xMif1ttiM8LTufzc3g6kR+9Pe236twL8j3IYT1F7GfRgGcW6MWxzZjLIkuHIg=="],

    "destr": ["destr@2.0.5", "", {}, "sha512-ugFTXCtDZunbzasqBxrK93Ik/DRYsO6S/fedkWEMKqt04xZ4csmnmwGDBAb07QWNaGMAmnTIemsYZCksjATwsA=="],

    "dotenv": ["dotenv@17.2.3", "", {}, "sha512-JVUnt+DUIzu87TABbhPmNfVdBDt18BLOWjMUFJMSi/Qqg7NTYtabbvSNJGOJ7afbRuv9D/lngizHtP7QyLQ+9w=="],

    "escalade": ["escalade@3.2.0", "", {}, "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA=="],

    "exsolve": ["exsolve@1.0.8", "", {}, "sha512-LmDxfWXwcTArk8fUEnOfSZpHOJ6zOMUJKOtFLFqJLoKJetuQG874Uc7/Kki7zFLzYybmZhp1M7+98pfMqeX8yA=="],

    "fdir": ["fdir@6.5.0", "", { "peerDependencies": { "picomatch": "^3 || ^4" }, "optionalPeers": ["picomatch"] }, "sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg=="],

    "giget": ["giget@2.0.0", "", { "dependencies": { "citty": "^0.1.6", "consola": "^3.4.0", "defu": "^6.1.4", "node-fetch-native": "^1.6.6", "nypm": "^0.6.0", "pathe": "^2.0.3" }, "bin": { "giget": "dist/cli.mjs" } }, "sha512-L5bGsVkxJbJgdnwyuheIunkGatUF/zssUoxxjACCseZYAVbaqdh9Tsmmlkl8vYan09H7sbvKt4pS8GqKLBrEzA=="],

    "jiti": ["jiti@2.6.1", "", { "bin": { "jiti": "lib/jiti-cli.mjs" } }, "sha512-ekilCSN1jwRvIbgeg/57YFh8qQDNbwDb9xT/qu2DAHbFFZUicIl4ygVaAvzveMhMVr3LnpSKTNnwt8PoOfmKhQ=="],

    "jsonc-parser": ["jsonc-parser@3.3.1", "", {}, "sha512-HUgH65KyejrUFPvHFPbqOY0rsFip3Bo5wb4ngvdi1EpCYWUQDC5V+Y7mZws+DLkr4M//zQJoanu1SP+87Dv1oQ=="],

    "node-fetch-native": ["node-fetch-native@1.6.7", "", {}, "sha512-g9yhqoedzIUm0nTnTqAQvueMPVOuIY16bqgAJJC8XOOubYFNwz6IER9qs0Gq2Xd0+CecCKFjtdDTMA4u4xG06Q=="],

    "nypm": ["nypm@0.6.2", "", { "dependencies": { "citty": "^0.1.6", "consola": "^3.4.2", "pathe": "^2.0.3", "pkg-types": "^2.3.0", "tinyexec": "^1.0.1" }, "bin": { "nypm": "dist/cli.mjs" } }, "sha512-7eM+hpOtrKrBDCh7Ypu2lJ9Z7PNZBdi/8AT3AX8xoCj43BBVHD0hPSTEvMtkMpfs8FCqBGhxB+uToIQimA111g=="],

    "ohash": ["ohash@2.0.11", "", {}, "sha512-RdR9FQrFwNBNXAr4GixM8YaRZRJ5PUWbKYbE5eOsrwAjJW0q2REGcf79oYPsLyskQCZG1PLN+S/K1V00joZAoQ=="],

    "package-manager-detector": ["package-manager-detector@1.6.0", "", {}, "sha512-61A5ThoTiDG/C8s8UMZwSorAGwMJ0ERVGj2OjoW5pAalsNOg15+iQiPzrLJ4jhZ1HJzmC2PIHT2oEiH3R5fzNA=="],

    "pathe": ["pathe@2.0.3", "", {}, "sha512-WUjGcAqP1gQacoQe+OBJsFA7Ld4DyXuUIjZ5cc75cLHvJ7dtNsTugphxIADwspS+AraAUePCKrSVtPLFj/F88w=="],

    "perfect-debounce": ["perfect-debounce@2.0.0", "", {}, "sha512-fkEH/OBiKrqqI/yIgjR92lMfs2K8105zt/VT6+7eTjNwisrsh47CeIED9z58zI7DfKdH3uHAn25ziRZn3kgAow=="],

    "picomatch": ["picomatch@4.0.3", "", {}, "sha512-5gTmgEY/sqK6gFXLIsQNH19lWb4ebPDLA4SdLP7dsWkIXHWlG66oPuVvXSGFPppYZz8ZDZq0dYYrbHfBCVUb1Q=="],

    "pkg-types": ["pkg-types@2.3.0", "", { "dependencies": { "confbox": "^0.2.2", "exsolve": "^1.0.7", "pathe": "^2.0.3" } }, "sha512-SIqCzDRg0s9npO5XQ3tNZioRY1uK06lA41ynBC1YmFTmnY6FjUjVt6s4LoADmwoig1qqD0oK8h1p/8mlMx8Oig=="],

    "rc9": ["rc9@2.1.2", "", { "dependencies": { "defu": "^6.1.4", "destr": "^2.0.3" } }, "sha512-btXCnMmRIBINM2LDZoEmOogIZU7Qe7zn4BpomSKZ/ykbLObuBdvG+mFq11DL6fjH1DRwHhrlgtYWG96bJiC7Cg=="],

    "readdirp": ["readdirp@4.1.2", "", {}, "sha512-GDhwkLfywWL2s6vEjyhri+eXmfH6j1L7JE27WhqLeYzoh/A3DBaYGEj2H/HFZCn/kMfim73FXxEJTw06WtxQwg=="],

    "semver": ["semver@7.7.3", "", { "bin": { "semver": "bin/semver.js" } }, "sha512-SdsKMrI9TdgjdweUSR9MweHA4EJ8YxHn8DFaDisvhVlUOe4BF1tLD7GAj0lIqWVl+dPb/rExr0Btby5loQm20Q=="],

    "tinyexec": ["tinyexec@1.0.2", "", {}, "sha512-W/KYk+NFhkmsYpuHq5JykngiOCnxeVL8v8dFnqxSD8qEEdRfXk1SDM6JzNqcERbcGYj9tMrDQBYV9cjgnunFIg=="],

    "tinyglobby": ["tinyglobby@0.2.15", "", { "dependencies": { "fdir": "^6.5.0", "picomatch": "^4.0.3" } }, "sha512-j2Zq4NyQYG5XMST4cbs02Ak8iJUdxRM0XI5QyxXuZOzKOINmWurp3smXu3y5wDcJrptwpSjgXHzIQxR0omXljQ=="],

    "yaml": ["yaml@2.8.2", "", { "bin": { "yaml": "bin.mjs" } }, "sha512-mplynKqc1C2hTVYxd0PU2xQAc22TI1vShAYGksCCfxbn/dFwnHTNi1bvYsBTkhdUNtGIf5xNOg938rrSSYvS9A=="],
  }
}
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing

## Requirements

- **macOS 15.0+** / **Windows 10+**
- **Xcode 16+** with Swift 6.0 (for macOS)
- **.NET 9 SDK** (for Windows)

## Setup

```bash
git clone https://github.com/productdevbook/port-killer.git
cd port-killer
```

## Running the App

### macOS

```bash
cd platforms/macos

# Option 1: Xcode (recommended)
open Package.swift
# Press ▶️ to run

# Option 2: Build script
./scripts/build-app.sh && open .build/apple/Products/Release/PortKiller.app
```

> ⚠️ `swift run` doesn't work for menu bar apps - use Xcode or the build script.

### Windows

```bash
cd platforms/windows/PortKiller
dotnet run
```

## Building

### macOS

```bash
cd platforms/macos
swift build              # Debug
swift build -c release   # Release
./scripts/build-app.sh   # App bundle
```

### Windows

```bash
cd platforms/windows/PortKiller
dotnet build             # Debug
dotnet publish -c Release -r win-x64  # Release
```

## Pull Requests

1. Fork the repo
2. Create a branch (`git checkout -b feature/my-feature`)
3. Make changes and test locally
4. Commit (`git commit -m "feat: add feature"`)
5. Push and create PR

## Code Style

### macOS
- Swift 6.0 with strict concurrency
- SwiftUI for UI
- `@Observable` for state management
- Keep files under 300 lines

### Windows
- C# with WPF
- MVVM pattern

## Project Structure

```
platforms/
├── macos/
│   ├── Sources/
│   │   ├── PortKillerApp.swift    # Entry point
│   │   ├── Managers/              # State & scanning
│   │   ├── Models/                # Data models
│   │   └── Views/                 # SwiftUI views
│   ├── Resources/                 # Assets, Info.plist
│   └── scripts/                   # Build scripts
└── windows/
    └── PortKiller/                # .NET WPF project
```
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 PortKiller Contributors

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

## File: `package.json`
```json
{
  "name": "portkiller",
  "version": "3.3.1",
  "private": true,
  "scripts": {
    "release": "bumpp"
  },
  "dependencies": {
    "bumpp": "^10.3.2"
  },
  "changelogithub": {
    "emoji": true,
    "contributors": true,
    "capitalize": true,
    "group": true
  }
}
```

## File: `README.md`
```markdown
# PortKiller

<p align="center">
  <img src="https://raw.githubusercontent.com/productdevbook/port-killer/refs/heads/main/platforms/macos/Resources/AppIcon.svg" alt="PortKiller Icon" width="128" height="128">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.apple.com/macos/"><img src="https://img.shields.io/badge/macOS-15.0%2B-brightgreen" alt="macOS"></a>
  <a href="https://www.microsoft.com/windows"><img src="https://img.shields.io/badge/Windows-10%2B-0078D6" alt="Windows"></a>
  <a href="https://github.com/productdevbook/port-killer/releases"><img src="https://img.shields.io/github/v/release/productdevbook/port-killer" alt="GitHub Release"></a>
</p>

<p align="center">
A powerful cross-platform port management tool for developers.<br>
Monitor ports, manage Kubernetes port forwards, integrate Cloudflare Tunnels, and kill processes with one click.
</p>

### macOS

<p align="center">
  <img src=".github/assets/macos.png" alt="PortKiller macOS" width="800">
</p>

### Windows

<p align="center">
  <img src=".github/assets/windows.jpeg" alt="PortKiller Windows" width="800">
</p>

## Installation

### macOS

**Homebrew:**
```bash
brew install --cask productdevbook/tap/portkiller
```

**Manual:** Download `.dmg` from [GitHub Releases](https://github.com/productdevbook/port-killer/releases).

### Windows

Download `.zip` from [GitHub Releases](https://github.com/productdevbook/port-killer/releases) and extract.

## Features

### Port Management
- 🔍 Auto-discovers all listening TCP ports
- ⚡ One-click process termination (graceful + force kill)
- 🔄 Auto-refresh with configurable interval
- 🔎 Search and filter by port number or process name
- ⭐ Favorites for quick access to important ports
- 👁️ Watched ports with notifications
- 📂 Smart categorization (Web Server, Database, Development, System)

### Kubernetes Port Forwarding
- 🔗 Create and manage kubectl port-forward sessions
- 🔌 Auto-reconnect on connection loss
- 📝 Connection logs and status monitoring
- 🔔 Notifications on connect/disconnect

### Cloudflare Tunnels
- ☁️ View and manage active Cloudflare Tunnel connections
- 🌐 Quick access to tunnel status

### Cross-Platform
- 📍 Menu bar integration (macOS)
- 🖥️ System tray app (Windows)
- 🎨 Native UI for each platform

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup.

## Sponsors

<p align="center">
  <a href="https://cdn.jsdelivr.net/gh/productdevbook/static/sponsors.svg">
    <img src='https://cdn.jsdelivr.net/gh/productdevbook/static/sponsors.svg'/>
  </a>
</p>

## License

MIT License - see [LICENSE](LICENSE).
```

## File: `STYLE_GUIDE.md`
```markdown
# PortKiller Style Guide

This document defines the coding standards and conventions for the PortKiller project.

## Table of Contents

- [Swift Language](#swift-language)
- [Naming Conventions](#naming-conventions)
- [SwiftUI Patterns](#swiftui-patterns)
- [Concurrency](#concurrency)
- [File Organization](#file-organization)
- [Documentation](#documentation)
- [Code Quality](#code-quality)

## Swift Language

### Version and Features

- **Swift 6.0** is required
- Use modern Swift features (async/await, actors, structured concurrency)
- Enable **strict concurrency checking**
- Avoid legacy Objective-C patterns unless interfacing with system APIs

### Type Inference

Use type inference where it improves readability:

```swift
// Good - type is clear from context
let ports = scanner.scanPorts()
let count = ports.count

// Avoid - unnecessary explicit type
let ports: [PortInfo] = scanner.scanPorts()

// Good - explicit type adds clarity
let timeout: TimeInterval = 5.0
```

### Optionals

Prefer optional chaining and nil coalescing:

```swift
// Good
let name = port.processName ?? "Unknown"
window?.makeKeyAndOrderFront(nil)

// Avoid
if let processName = port.processName {
    name = processName
} else {
    name = "Unknown"
}
```

Use `guard` for early returns:

```swift
// Good
guard let port = selectedPort else { return }
// Use port here...

// Avoid
if selectedPort != nil {
    let port = selectedPort!
    // Use port here...
}
```

### Error Handling

Use `try?` for non-critical operations:

```swift
// Good - we don't care if this fails
try? await Task.sleep(for: .milliseconds(500))

// Good - critical operation, handle errors
do {
    try process.run()
    process.waitUntilExit()
} catch {
    print("Failed to run process: \(error)")
    return false
}
```

## Naming Conventions

Follow [Apple's Swift API Design Guidelines](https://swift.org/documentation/api-design-guidelines/).

### Types

- Use `PascalCase` for types and protocols
- Use descriptive, self-documenting names
- Avoid abbreviations unless widely understood

```swift
// Good
struct PortInfo { }
class AppState { }
enum ProcessType { }
protocol PortScanning { }

// Avoid
struct PI { }
class AS { }
enum PT { }
```

### Variables and Functions

- Use `camelCase` for variables, functions, and parameters
- Boolean variables should read as assertions

```swift
// Good
var isScanning = false
var canCheckForUpdates = true
func killProcess(pid: Int) { }

// Avoid
var scanning = false  // Unclear type
var able_to_check = true  // Wrong case
func kill(p: Int) { }  // Unclear parameter
```

### Constants

- Use static properties in enums for constants
- Group related constants together

```swift
// Good
enum UIConstants {
    static let width: CGFloat = 340
    static let maxHeight: CGFloat = 400
}

// Avoid
let MENU_BAR_WIDTH = 340  // Wrong case
let menuBarWidth = 340  // Should be grouped with related constants
```

### Enums

- Use lowercase for enum cases
- Omit prefixes when context is clear

```swift
// Good
enum ProcessType {
    case webServer
    case database
    case development
}

let type: ProcessType = .webServer  // Context clear

// Avoid
enum ProcessType {
    case ProcessTypeWebServer  // Redundant prefix
    case process_type_database  // Wrong case
}
```

## SwiftUI Patterns

### State Management

Use `@Observable` macro for state objects (not `ObservableObject`):

```swift
// Good - Modern @Observable
@Observable
@MainActor
final class AppState {
    var ports: [PortInfo] = []
    var isScanning = false
}

// Avoid - Legacy ObservableObject
@MainActor
final class AppState: ObservableObject {
    @Published var ports: [PortInfo] = []
    @Published var isScanning = false
}
```

### View Structure

Keep views focused and under 200 lines:

```swift
// Good - Single responsibility
struct PortListView: View {
    let ports: [PortInfo]

    var body: some View {
        List(ports) { port in
            PortRowView(port: port)
        }
    }
}

// Avoid - Too many responsibilities
struct MainView: View {
    var body: some View {
        // 500 lines of nested views...
    }
}
```

Extract complex views into separate components:

```swift
// Good
struct PortDetailView: View {
    let port: PortInfo

    var body: some View {
        VStack {
            PortHeader(port: port)
            PortInfo(port: port)
            PortActions(port: port)
        }
    }
}

// Each component is focused and reusable
```

### View Modifiers

Use custom view modifiers for repeated styling:

```swift
// Good
struct CardStyle: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .background(Color.white)
            .cornerRadius(8)
    }
}

extension View {
    func cardStyle() -> some View {
        modifier(CardStyle())
    }
}

// Usage
Text("Hello").cardStyle()
```

## Concurrency

### MainActor Isolation

Mark UI-related types with `@MainActor`:

```swift
// Good
@Observable
@MainActor
final class AppState {
    var ports: [PortInfo] = []

    func refresh() async {
        // Runs on main thread automatically
        ports = await scanner.scanPorts()
    }
}

// Avoid
@Observable
final class AppState {
    var ports: [PortInfo] = []

    func refresh() async {
        // May run on background thread - UI updates will crash
        ports = await scanner.scanPorts()
    }
}
```

### Actors

Use actors for thread-safe state:

```swift
// Good
actor PortScanner {
    func scanPorts() async -> [PortInfo] {
        // Thread-safe by default
    }

    func killProcess(pid: Int) async -> Bool {
        // Thread-safe by default
    }
}
```

### Sendable

Mark types as `Sendable` when they cross concurrency boundaries:

```swift
// Good
struct PortInfo: Sendable {
    let port: Int
    let pid: Int
    let processName: String
}

// Model can be safely passed between actors
```

### Task Management

Store tasks that need cancellation:

```swift
// Good
@ObservationIgnored
private nonisolated(unsafe) var refreshTask: Task<Void, Never>?

func startAutoRefresh() {
    refreshTask = Task {
        while !Task.isCancelled {
            await refresh()
            try? await Task.sleep(for: .seconds(5))
        }
    }
}

deinit {
    refreshTask?.cancel()
}
```

## File Organization

### File Structure

Organize files by feature/responsibility:

```
Sources/
├── PortKillerApp.swift       # App entry point
├── AppState.swift             # Main app state
├── Constants.swift            # App constants
├── Models/                    # Data models
│   ├── Models.swift
│   └── PortFilter.swift
├── Managers/                  # Business logic
│   ├── UpdateManager.swift
│   └── SponsorManager.swift
├── Services/                  # External services
│   └── SponsorsService.swift
├── Views/                     # UI components
│   ├── MainWindowView.swift
│   ├── SettingsView.swift
│   └── Components/
│       ├── PortTableView.swift
│       └── AddPortPopover.swift
└── PortScanner.swift          # Port scanning logic
```

### File Header

Each file should start with imports, then content:

```swift
import Foundation
import SwiftUI
import Defaults

// MARK: - Model Definition

/**
 * PortInfo represents a process listening on a network port.
 */
struct PortInfo: Identifiable, Sendable {
    // ...
}
```

### MARK Comments

Use `// MARK:` to organize code within files:

```swift
class AppState {
    // MARK: - Properties
    var ports: [PortInfo] = []

    // MARK: - Initialization
    init() { }

    // MARK: - Port Operations
    func refresh() async { }
    func killPort(_ port: PortInfo) async { }

    // MARK: - Favorites
    func toggleFavorite(_ port: Int) { }

    // MARK: - Private Methods
    private func updatePorts(_ newPorts: [PortInfo]) { }
}
```

Standard sections (in order):
1. Properties
2. Initialization
3. Public Methods (grouped by feature)
4. Private Methods

## Documentation

### JSDoc-Style Comments

Document all public APIs with JSDoc-style comments:

```swift
/**
 * Scans all listening TCP ports using lsof.
 *
 * Executes: `lsof -iTCP -sTCP:LISTEN -P -n +c 0`
 *
 * @returns Array of PortInfo objects representing all listening ports
 */
func scanPorts() async -> [PortInfo] {
    // Implementation
}

/**
 * Kills a process by sending a termination signal.
 *
 * @param pid - The process ID to kill
 * @param force - If true, sends SIGKILL (-9) instead of SIGTERM (-15)
 * @returns True if the kill command executed successfully
 */
func killProcess(pid: Int, force: Bool = false) async -> Bool {
    // Implementation
}
```

### Inline Comments

Use inline comments for complex logic:

```swift
// CRITICAL: Read data BEFORE waitUntilExit to avoid deadlock
// If pipe buffer fills up, ps will block waiting to write more data.
let data = pipe.fileHandleForReading.readDataToEndOfFile()
process.waitUntilExit()
```

### Property Documentation

Document non-obvious properties:

```swift
/// Cached favorites set, synced with UserDefaults
private var _favorites: Set<Int> = Defaults[.favorites] {
    didSet { Defaults[.favorites] = _favorites }
}

/// Whether a port scan is currently in progress
var isScanning = false
```

## Code Quality

### Line Length

- Keep lines under 120 characters when possible
- Break long function calls into multiple lines

```swift
// Good
let controller = SPUStandardUpdaterController(
    startingUpdater: true,
    updaterDelegate: nil,
    userDriverDelegate: nil
)

// Avoid - too long
let controller = SPUStandardUpdaterController(startingUpdater: true, updaterDelegate: nil, userDriverDelegate: nil)
```

### Function Length

- Keep functions under 50 lines
- Extract complex logic into helper functions

```swift
// Good
func parseLsofOutput(_ output: String) -> [PortInfo] {
    let lines = output.components(separatedBy: .newlines)
    var ports: [PortInfo] = []

    for line in lines.dropFirst() {
        guard let port = parseLineToPort(line) else { continue }
        ports.append(port)
    }

    return ports
}

private func parseLineToPort(_ line: String) -> PortInfo? {
    // Focused parsing logic
}
```

### Complexity

Avoid deeply nested code:

```swift
// Good - Early returns
guard !line.isEmpty else { continue }
guard components.count >= 9 else { continue }
guard let pid = Int(components[1]) else { continue }

// Avoid - Nested ifs
if !line.isEmpty {
    if components.count >= 9 {
        if let pid = Int(components[1]) {
            // Deep nesting...
        }
    }
}
```

### Magic Numbers

Define constants instead of magic numbers:

```swift
// Good
enum AppConstants {
    static let defaultRefreshInterval: Int = 5
    static let maxCommandLength: Int = 200
}

let interval = AppConstants.defaultRefreshInterval

// Avoid
try? await Task.sleep(for: .seconds(5))  // Why 5?
let trimmed = command.prefix(200)  // Why 200?
```

### DRY (Don't Repeat Yourself)

Extract repeated code into functions:

```swift
// Good
func createPort(port: Int, processName: String) -> PortInfo {
    PortInfo.active(
        port: port,
        pid: 0,
        processName: processName,
        address: "127.0.0.1",
        user: "user",
        command: processName,
        fd: "19u"
    )
}

let nodePort = createPort(port: 3000, processName: "node")
let nginxPort = createPort(port: 8080, processName: "nginx")
```

## Testing

### Test Organization

Use descriptive test names:

```swift
@Test("Detects nginx as web server")
func detectNginx() {
    #expect(ProcessType.detect(from: "nginx") == .webServer)
}

@Test("Search matches process name case insensitively")
func searchMatchesProcessNameCaseInsensitive() {
    let filter = PortFilter(searchText: "NODE")
    let port = createPort(processName: "node")
    #expect(filter.matches(port, favorites: [], watched: []))
}
```

### Test Structure

Follow Arrange-Act-Assert pattern:

```swift
@Test("Port range filter excludes ports outside range")
func portRangeFilter() {
    // Arrange
    var filter = PortFilter()
    filter.minPort = 3000
    filter.maxPort = 5000

    // Act
    let portInRange = createPort(port: 4000)
    let portOutOfRange = createPort(port: 6000)

    // Assert
    #expect(filter.matches(portInRange, favorites: [], watched: []))
    #expect(!filter.matches(portOutOfRange, favorites: [], watched: []))
}
```

## Common Patterns

### Singleton-like Managers

For app-wide managers:

```swift
@Observable
@MainActor
final class AppState {
    // Shared state accessible throughout the app
}

// Usage in SwiftUI
@Environment(AppState.self) private var appState
```

### Defaults Integration

Use cached properties for UserDefaults:

```swift
// In Defaults.Keys extension
static let favorites = Key<Set<Int>>("favorites", default: [])

// In AppState
private var _favorites: Set<Int> = Defaults[.favorites] {
    didSet { Defaults[.favorites] = _favorites }
}

var favorites: Set<Int> {
    get { _favorites }
    set { _favorites = newValue }
}
```

### Command Execution

Pattern for running system commands:

```swift
func runCommand(path: String, args: [String]) async -> String? {
    let process = Process()
    process.executableURL = URL(fileURLWithPath: path)
    process.arguments = args

    let pipe = Pipe()
    process.standardOutput = pipe
    process.standardError = FileHandle.nullDevice

    do {
        try process.run()
        let data = pipe.fileHandleForReading.readDataToEndOfFile()
        process.waitUntilExit()
        return String(data: data, encoding: .utf8)
    } catch {
        return nil
    }
}
```

## Additional Resources

- [Swift.org - API Design Guidelines](https://swift.org/documentation/api-design-guidelines/)
- [Apple - The Swift Programming Language](https://docs.swift.org/swift-book/)
- [Swift Concurrency Documentation](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html)
- [SwiftUI Best Practices](https://developer.apple.com/documentation/swiftui)

---

**Remember:** These are guidelines, not absolute rules. Use your best judgment and prioritize code clarity and maintainability.
```

## File: `platforms/macos/Package.swift`
```
// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "PortKiller",
    platforms: [
        .macOS(.v15)
    ],
    products: [
        .executable(name: "PortKiller", targets: ["PortKiller"])
    ],
    dependencies: [
        .package(url: "https://github.com/sindresorhus/KeyboardShortcuts", from: "2.4.0"),
        .package(url: "https://github.com/sindresorhus/Defaults", from: "9.0.0"),
        .package(url: "https://github.com/sindresorhus/LaunchAtLogin-Modern", from: "1.1.0"),
        .package(url: "https://github.com/sparkle-project/Sparkle", from: "2.8.1")
    ],
    targets: [
        .executableTarget(
            name: "PortKiller",
            dependencies: [
                "KeyboardShortcuts",
                "Defaults",
                .product(name: "LaunchAtLogin", package: "LaunchAtLogin-Modern"),
                .product(name: "Sparkle", package: "Sparkle")
            ],
            path: "Sources",
            resources: [
                .process("Resources")
            ],
            swiftSettings: [
                // Swift 6.2 performance optimizations
                .enableExperimentalFeature("NonisolatedNonsendingByDefault"),
                .enableExperimentalFeature("InlineArrayTypeSugar"),
                // Default MainActor isolation - reduces boilerplate, prevents actor hops
                .enableUpcomingFeature("DefaultIsolationMainActor"),
                // Enable Span types for zero-copy memory access (Swift 6.2+)
                .enableExperimentalFeature("LifetimeDependence"),
                .enableExperimentalFeature("Span")
            ]
        ),
        .testTarget(
            name: "PortKillerTests",
            dependencies: ["PortKiller"],
            path: "Tests"
        )
    ]
)
```

## File: `platforms/macos/Resources/Info.plist`
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleIdentifier</key>
    <string>com.portkiller.app</string>
    <key>CFBundleName</key>
    <string>PortKiller</string>
    <key>CFBundleDisplayName</key>
    <string>PortKiller</string>
    <key>CFBundleExecutable</key>
    <string>PortKiller</string>
    <key>CFBundleIconFile</key>
    <string>AppIcon</string>
    <key>CFBundleIconName</key>
    <string>AppIcon</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>1.2.1</string>
    <key>CFBundleVersion</key>
    <string>13</string>
    <key>LSMinimumSystemVersion</key>
    <string>15.0</string>
    <key>LSUIElement</key>
    <true/>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>NSUserNotificationAlertStyle</key>
    <string>alert</string>
    <key>NSHumanReadableCopyright</key>
    <string>Copyright © 2025 PortKiller Contributors</string>
    <!-- Sparkle Configuration -->
    <key>SUFeedURL</key>
    <string>https://raw.githubusercontent.com/productdevbook/port-killer/main/appcast.xml</string>
    <key>SUPublicEDKey</key>
    <string>F/FTbv7ZnucHLHqUmAF0w3peyir2Jxsf1k3J5TU85U0=</string>
    <key>SUEnableAutomaticChecks</key>
    <true/>
    <key>SUAllowsAutomaticUpdates</key>
    <true/>
    <key>SUScheduledCheckInterval</key>
    <integer>86400</integer>
    <key>SUShowReleaseNotes</key>
    <true/>
</dict>
</plist>
```

## File: `platforms/macos/Resources/AppIcon.icon/icon.json`
```json
{
  "fill" : {
    "linear-gradient" : [
      "display-p3:1.00000,0.41961,0.41961,1.00000",
      "srgb:0.78824,0.16471,0.16471,1.00000"
    ],
    "orientation" : {
      "start" : {
        "x" : 0.5,
        "y" : 0
      },
      "stop" : {
        "x" : 0.5,
        "y" : 0.7
      }
    }
  },
  "groups" : [
    {
      "blur-material" : null,
      "layers" : [
        {
          "hidden" : false,
          "image-name" : "cross.svg",
          "name" : "cross"
        }
      ],
      "shadow" : {
        "kind" : "neutral",
        "opacity" : 0.5
      },
      "translucency" : {
        "enabled" : true,
        "value" : 0.5
      }
    },
    {
      "layers" : [
        {
          "fill-specializations" : [
            {
              "appearance" : "dark",
              "value" : "automatic"
            }
          ],
          "glass" : true,
          "hidden" : false,
          "image-name" : "plug.svg",
          "name" : "plug",
          "position" : {
            "scale" : 1,
            "translation-in-points" : [
              0,
              -2
            ]
          }
        }
      ],
      "shadow" : {
        "kind" : "neutral",
        "opacity" : 0.5
      },
      "translucency" : {
        "enabled" : true,
        "value" : 0.5
      }
    }
  ],
  "supported-platforms" : {
    "circles" : [
      "watchOS"
    ],
    "squares" : "shared"
  }
}
```

## File: `platforms/macos/scripts/build-app.sh`
```bash
#!/bin/bash

# Build script for PortKiller.app (Universal Binary)
set -e

APP_NAME="PortKiller"
BUNDLE_ID="com.portkiller.app"

# Swift PM Universal Build Output Directory
# When building for multiple architectures, SPM puts products in apple/Products/Release
BUILD_DIR=".build/apple/Products/Release"
APP_DIR="$BUILD_DIR/$APP_NAME.app"
CONTENTS_DIR="$APP_DIR/Contents"
MACOS_DIR="$CONTENTS_DIR/MacOS"
RESOURCES_DIR="$CONTENTS_DIR/Resources"

# Fetch dependencies (no need for full build)
echo "📦 Fetching dependencies..."
swift package resolve

# Patch the CHECKOUT source files directly (not DerivedSources which gets regenerated)
# This patches the actual library code before the final build
echo "🔧 Patching library source files for macOS app bundle compatibility..."

# Create a helper file that will be included to fix Bundle.module
BUNDLE_FIX_CODE='
// Patched Bundle.module accessor for macOS app bundles
// This extension takes precedence over SPM-generated one due to same-module compilation
private func findResourceBundle(named bundleName: String) -> Bundle? {
    // For macOS app bundles: check Contents/Resources first
    if let resourceURL = Bundle.main.resourceURL {
        let bundlePath = resourceURL.appendingPathComponent("\(bundleName).bundle").path
        if let bundle = Bundle(path: bundlePath) {
            return bundle
        }
    }

    // Fallback: check app root (Bundle.main.bundleURL)
    let mainPath = Bundle.main.bundleURL.appendingPathComponent("\(bundleName).bundle").path
    if let bundle = Bundle(path: mainPath) {
        return bundle
    }

    return nil
}
'

# Patch KeyboardShortcuts - add resourceURL check to its Utilities.swift
KS_UTILS=".build/checkouts/KeyboardShortcuts/Sources/KeyboardShortcuts/Utilities.swift"
if [ -f "$KS_UTILS" ] && ! grep -q "resourceURL" "$KS_UTILS"; then
    echo "  → Patching KeyboardShortcuts/Utilities.swift"
    # Make file writable
    chmod +w "$KS_UTILS"
    # Add the fix at the beginning of the file
    cat > /tmp/ks_patch.swift << 'PATCH_EOF'
import Foundation

// PATCHED: Fix Bundle.module for macOS app bundles
// SPM's generated accessor doesn't check Contents/Resources
extension Foundation.Bundle {
    static var modulePatched: Bundle {
        let bundleName = "KeyboardShortcuts_KeyboardShortcuts"

        // For macOS app bundles: check Contents/Resources first
        if let resourceURL = Bundle.main.resourceURL {
            let bundlePath = resourceURL.appendingPathComponent("\(bundleName).bundle").path
            if let bundle = Bundle(path: bundlePath) {
                return bundle
            }
        }

        // Fallback: check app root
        let mainPath = Bundle.main.bundleURL.appendingPathComponent("\(bundleName).bundle").path
        if let bundle = Bundle(path: mainPath) {
            return bundle
        }

        // Development: use SPM's generated accessor as last resort
        return module
    }
}

// Patch String.localized to use modulePatched
extension String {
    var localizedPatched: String {
        NSLocalizedString(self, bundle: .modulePatched, comment: self)
    }
}

PATCH_EOF
    # Prepend patch to the file
    cat /tmp/ks_patch.swift "$KS_UTILS" > /tmp/ks_utils_patched.swift
    cp /tmp/ks_utils_patched.swift "$KS_UTILS"

    # Replace ".localized" (as property, not part of localizedStringWithFormat) with .localizedPatched
    KS_RECORDER=".build/checkouts/KeyboardShortcuts/Sources/KeyboardShortcuts/RecorderCocoa.swift"
    if [ -f "$KS_RECORDER" ]; then
        echo "  → Patching KeyboardShortcuts/RecorderCocoa.swift"
        chmod +w "$KS_RECORDER"
        # Only replace .localized when followed by non-word char (not localizedStringWithFormat)
        sed -i '' 's/\.localized\([^A-Za-z]\)/.localizedPatched\1/g' "$KS_RECORDER"
        # Also handle .localized at end of line
        sed -i '' 's/\.localized$/.localizedPatched/g' "$KS_RECORDER"
    fi
fi

# Also patch any other files that use .localized in KeyboardShortcuts
for ks_file in .build/checkouts/KeyboardShortcuts/Sources/KeyboardShortcuts/*.swift; do
    if [ -f "$ks_file" ] && grep -q '".*"\.localized' "$ks_file" && ! grep -q 'localizedPatched' "$ks_file"; then
        echo "  → Patching $(basename "$ks_file")"
        chmod +w "$ks_file"
        sed -i '' 's/\.localized\([^A-Za-z]\)/.localizedPatched\1/g' "$ks_file"
        sed -i '' 's/\.localized$/.localizedPatched/g' "$ks_file"
    fi
done

# Touch patched files to ensure SPM sees them as modified
echo "🔄 Updating timestamps on patched files..."
touch .build/checkouts/KeyboardShortcuts/Sources/KeyboardShortcuts/*.swift 2>/dev/null || true

# Remove compiled KeyboardShortcuts objects and executable to force recompilation
echo "🧹 Forcing recompilation..."
rm -f .build/*/release/KeyboardShortcuts.build/*.o 2>/dev/null || true
rm -f .build/*/release/PortKiller
rm -rf .build/*/release/*.bundle

echo "🔨 Building release binary with patched sources..."
swift build -c release --arch arm64 --arch x86_64

echo "📦 Creating app bundle..."
rm -rf "$APP_DIR"
mkdir -p "$MACOS_DIR"
mkdir -p "$RESOURCES_DIR"
mkdir -p "$CONTENTS_DIR/Frameworks"

echo "📋 Copying files..."
cp "$BUILD_DIR/$APP_NAME" "$MACOS_DIR/"
cp "Resources/Info.plist" "$CONTENTS_DIR/"

# Debug: List contents of build directory
echo "📂 Contents of $BUILD_DIR:"
ls -la "$BUILD_DIR/" | grep -E "\.bundle$|^total" || echo "  (no bundles found)"

# Generate icons from AppIcon.icon using actool (Xcode 26+)
if [ -d "Resources/AppIcon.icon" ]; then
    echo "🎨 Compiling AppIcon.icon with actool..."

    # Use actool to compile .icon folder - generates both Assets.car and fallback .icns
    # Wrap in conditional to handle CI crashes (common with Xcode 26+ on some GHA runners)
    if xcrun actool "Resources/AppIcon.icon" \
        --compile "$RESOURCES_DIR" \
        --app-icon AppIcon \
        --target-device mac \
        --platform macosx \
        --minimum-deployment-target 15.0 \
        --include-all-app-icons \
        --output-partial-info-plist /tmp/icon-info.plist 2>/dev/null; then
        echo "  ✅ Generated AppIcon.icns and Assets.car"
    else
        echo "  ⚠️ Warning: actool failed (likely CI/Environment issue)."
        # Fallback: use pre-generated static .icns file
        if [ -f "Resources/AppIcon.icns" ]; then
            echo "  → Using static AppIcon.icns as fallback"
            cp "Resources/AppIcon.icns" "$RESOURCES_DIR/"
        else
            echo "  ❌ Error: No AppIcon.icns fallback available."
            exit 1
        fi
    fi
elif [ -f "Resources/AppIcon.icns" ]; then
    # Fallback: copy static .icns if .icon folder doesn't exist
    echo "  → Copying static AppIcon.icns (legacy fallback)"
    cp "Resources/AppIcon.icns" "$RESOURCES_DIR/"
fi

# Copy all SPM resource bundles to Contents/Resources (use ditto to preserve symlinks)
for bundle in "$BUILD_DIR"/*.bundle; do
    if [ -d "$bundle" ]; then
        bundle_name=$(basename "$bundle")
        echo "  → Copying $bundle_name"
        ditto "$bundle" "$RESOURCES_DIR/$bundle_name"
    fi
done

# Download and copy Sparkle framework from official release (preserves symlinks)
SPARKLE_VERSION="2.8.1"
SPARKLE_CACHE="/tmp/Sparkle-${SPARKLE_VERSION}"

if [ ! -d "$SPARKLE_CACHE/Sparkle.framework" ]; then
    echo "📥 Downloading Sparkle ${SPARKLE_VERSION}..."
    curl -L -o /tmp/Sparkle.tar.xz "https://github.com/sparkle-project/Sparkle/releases/download/${SPARKLE_VERSION}/Sparkle-${SPARKLE_VERSION}.tar.xz"
    mkdir -p "$SPARKLE_CACHE"
    tar -xf /tmp/Sparkle.tar.xz -C "$SPARKLE_CACHE"
    rm /tmp/Sparkle.tar.xz
fi

echo "📦 Copying Sparkle.framework..."
ditto "$SPARKLE_CACHE/Sparkle.framework" "$CONTENTS_DIR/Frameworks/Sparkle.framework"

# Remove XPC services (not needed for non-sandboxed apps, saves ~500KB)
echo "🗑️ Removing unnecessary XPC services..."
rm -rf "$CONTENTS_DIR/Frameworks/Sparkle.framework/Versions/B/XPCServices"
rm -f "$CONTENTS_DIR/Frameworks/Sparkle.framework/XPCServices"

# Add rpath so executable can find the framework
echo "🔗 Setting up framework path..."
install_name_tool -add_rpath "@executable_path/../Frameworks" "$MACOS_DIR/$APP_NAME" 2>/dev/null || true

# Verify bundles were copied
echo "📂 Contents of $RESOURCES_DIR:"
ls -la "$RESOURCES_DIR/"

# Verify patched accessor is in binary (checks for resourceURL which is only in patched version)
echo "🔍 Verifying patched accessor..."
if strings "$MACOS_DIR/$APP_NAME" | grep -q "resourceURL"; then
    echo "  ✅ Patched accessor verified in binary"
else
    echo "  ❌ ERROR: Accessor not patched correctly! Binary still uses original SPM accessor."
    echo "  The app will crash when trying to load resource bundles."
    exit 1
fi

# Verify required bundles exist
echo "🔍 Verifying resource bundles..."
MISSING_BUNDLES=0
for bundle in KeyboardShortcuts_KeyboardShortcuts Defaults_Defaults; do
    if [ -d "$RESOURCES_DIR/${bundle}.bundle" ]; then
        echo "  ✅ ${bundle}.bundle"
    else
        echo "  ❌ Missing: ${bundle}.bundle"
        MISSING_BUNDLES=1
    fi
done
if [ $MISSING_BUNDLES -eq 1 ]; then
    echo "  ERROR: Some resource bundles are missing!"
    exit 1
fi

echo "🔏 Signing app bundle..."
codesign --force --deep --sign - "$APP_DIR"

echo "✅ App bundle created at: $APP_DIR"
echo ""
echo "To install, run:"
echo "  cp -r $APP_DIR /Applications/"
echo ""
echo "Or open directly:"
echo "  open $APP_DIR"
```

## File: `platforms/macos/Sources/AppState+AutoKill.swift`
```
import Foundation
import Defaults

extension AppState {
    /// Tracks when ports were first seen (port-pid key → first seen date).
    /// Stored on AppState as a non-observed property.
    private static var portFirstSeen: [String: Date] = [:]

    /// Checks auto-kill rules against current ports and kills matches that exceed their timeout.
    func checkAutoKillRules() {
        let rules = Defaults[.autoKillRules]
        guard !rules.isEmpty else { return }

        let enabledRules = rules.filter(\.isEnabled)
        guard !enabledRules.isEmpty else { return }

        let now = Date()

        // Update first-seen tracking
        let currentKeys = Set(ports.map { "\($0.port)-\($0.pid)" })
        // Remove stale entries
        Self.portFirstSeen = Self.portFirstSeen.filter { currentKeys.contains($0.key) }
        // Add new entries
        for port in ports {
            let key = "\(port.port)-\(port.pid)"
            if Self.portFirstSeen[key] == nil {
                Self.portFirstSeen[key] = now
            }
        }

        // Check rules
        for port in ports {
            let key = "\(port.port)-\(port.pid)"
            guard let firstSeen = Self.portFirstSeen[key] else { continue }

            for rule in enabledRules {
                guard rule.matches(port) else { continue }

                let elapsed = now.timeIntervalSince(firstSeen) / 60.0
                guard elapsed >= Double(rule.timeoutMinutes) else { continue }

                // Notify and kill
                if rule.notifyBeforeKill {
                    NotificationService.shared.notify(
                        title: "Auto-Kill: \(port.processName)",
                        body: "Port \(port.port) killed after \(rule.timeoutMinutes) min (rule: \(rule.name))"
                    )
                }

                Task {
                    await killPort(port)
                }

                // Remove from tracking so we don't re-trigger
                Self.portFirstSeen.removeValue(forKey: key)
                break // Only apply first matching rule
            }
        }
    }
}
```

## File: `platforms/macos/Sources/AppState+AutoRefresh.swift`
```
import Foundation
import Defaults

extension AppState {
    /// Stops the auto-refresh task.
    func stopAutoRefresh() {
        refreshTask?.cancel()
        refreshTask = nil
    }

    /// Starts a background task that periodically refreshes the port list.
    func startAutoRefresh() {
        stopAutoRefresh()
        refreshTask = Task { @MainActor in
            var unchangedCycles = 0
            _ = await self.refresh()
            while !Task.isCancelled {
                let baseInterval = max(1, Defaults[.refreshInterval])
                let delaySeconds = adaptiveRefreshDelay(baseInterval: baseInterval, unchangedCycles: unchangedCycles)
                try? await Task.sleep(for: .seconds(delaySeconds))
                guard !Task.isCancelled else { break }

                let didChange = await self.refresh()
                unchangedCycles = didChange ? 0 : min(unchangedCycles + 1, 60)
            }
        }
    }

    /// Dynamically backs off polling when the port list stays stable.
    private func adaptiveRefreshDelay(baseInterval: Int, unchangedCycles: Int) -> Double {
        let base = Double(baseInterval)
        let multiplier: Double

        switch unchangedCycles {
        case 0..<6:
            multiplier = 1.0
        case 6..<12:
            multiplier = 1.5
        default:
            multiplier = 2.0
        }

        return min(base * multiplier, 30.0)
    }
}
```

## File: `platforms/macos/Sources/AppState+Favorites.swift`
```
import Foundation

extension AppState {
    /// Toggles favorite status for a port (delegates to FavoritesState)
    func toggleFavorite(_ port: Int) {
        favoritesState.toggle(port)
    }

    /// Checks if a port is marked as favorite (delegates to FavoritesState)
    func isFavorite(_ port: Int) -> Bool {
        favoritesState.isFavorite(port)
    }
}
```

## File: `platforms/macos/Sources/AppState+KeyboardShortcuts.swift`
```
import Foundation
import AppKit
import KeyboardShortcuts

extension AppState {
    /// Sets up global keyboard shortcuts.
    func setupKeyboardShortcuts() {
        KeyboardShortcuts.onKeyUp(for: .toggleMainWindow) { [weak self] in
            // KeyboardShortcuts callbacks run on the main thread, so we can use assumeIsolated
            // This avoids creating a detached Task that outlives the callback context
            MainActor.assumeIsolated {
                self?.toggleMainWindow()
            }
        }
    }

    /// Toggles the main window visibility.
    func toggleMainWindow() {
        if let window = NSApp.windows.first(where: { $0.title == "PortKiller" || $0.identifier?.rawValue == "main" }) {
            if window.isVisible {
                window.orderOut(nil)
            } else {
                NSApp.setActivationPolicy(.regular)
                NSApp.activate(ignoringOtherApps: true)
                window.makeKeyAndOrderFront(nil)
                window.orderFrontRegardless()
            }
        } else {
            NSApp.setActivationPolicy(.regular)
            NSApp.activate(ignoringOtherApps: true)
        }
    }
}
```

## File: `platforms/macos/Sources/AppState+PortLabels.swift`
```
import AppKit
import Defaults

extension AppState {
    /// Returns the custom label for a port, if any
    func portLabel(for port: Int) -> String? {
        let label = Defaults[.portLabels][String(port)]
        return (label?.isEmpty ?? true) ? nil : label
    }

    /// Sets a custom label for a port
    func setPortLabel(_ label: String, for port: Int) {
        if label.isEmpty {
            Defaults[.portLabels].removeValue(forKey: String(port))
        } else {
            Defaults[.portLabels][String(port)] = label
        }
    }

    /// Removes the custom label for a port
    func removePortLabel(for port: Int) {
        Defaults[.portLabels].removeValue(forKey: String(port))
    }

    /// Prompts user to set a port label using NSAlert
    func promptForPortLabel(port: Int) {
        let alert = NSAlert()
        alert.messageText = "Set Label for Port \(port)"
        alert.informativeText = "Enter a custom name to identify this port."
        alert.addButton(withTitle: "Save")
        alert.addButton(withTitle: "Cancel")

        let textField = NSTextField(frame: NSRect(x: 0, y: 0, width: 260, height: 24))
        textField.placeholderString = "e.g., Frontend Dev Server"
        textField.stringValue = portLabel(for: port) ?? ""
        alert.accessoryView = textField
        alert.window.initialFirstResponder = textField

        if alert.runModal() == .alertFirstButtonReturn {
            setPortLabel(textField.stringValue, for: port)
        }
    }
}
```

## File: `platforms/macos/Sources/AppState+PortOperations.swift`
```
import Foundation

extension AppState {
    /// Refreshes the port list by scanning for active ports.
    @discardableResult
    func refresh() async -> Bool {
        if isScanning {
            hasPendingRefreshRequest = true
            return false
        }

        var didChangeAny = false

        repeat {
            hasPendingRefreshRequest = false
            isScanning = true

            let scanned = await scanner.scanPorts()
            let previousPorts = ports
            let didChange = updatePorts(scanned)
            didChangeAny = didChangeAny || didChange

            // Check process type notifications for newly appeared ports
            if didChange {
                checkProcessTypeNotifications(oldPorts: previousPorts, newPorts: scanned)
            }

            // Always update watcher state to keep transition baseline accurate.
            checkWatchedPorts()

            // Check auto-kill rules
            checkAutoKillRules()

            isScanning = false
        } while hasPendingRefreshRequest

        return didChangeAny
    }

    /// Updates the internal port list only if there are changes.
    @discardableResult
    func updatePorts(_ newPorts: [PortInfo]) -> Bool {
        let newSet = Set(newPorts.map { "\($0.port)-\($0.pid)" })
        let oldSet = Set(ports.map { "\($0.port)-\($0.pid)" })
        guard newSet != oldSet else { return false }

        ports = newPorts.sorted { a, b in
            let aFav = favorites.contains(a.port)
            let bFav = favorites.contains(b.port)
            if aFav != bFav { return aFav }
            return a.port < b.port
        }
        return true
    }

    /// Kills the process using the specified port.
    func killPort(_ port: PortInfo) async {
        if await scanner.killProcessGracefully(pid: port.pid) {
            ports.removeAll { $0.id == port.id }
            await refresh()
        }
    }

    /// Kills the listening process and all processes with ESTABLISHED connections to the port.
    func killPortDeep(_ port: PortInfo) async {
        // 1. Kill the listener
        _ = await scanner.killProcessGracefully(pid: port.pid)

        // 2. Find and kill ESTABLISHED connections
        let establishedPids = await scanner.findEstablishedPids(for: port.port)
        for pid in establishedPids where pid != port.pid {
            _ = await scanner.killProcessGracefully(pid: pid)
        }

        ports.removeAll { $0.id == port.id }
        await refresh()
    }

    /// Kills all processes currently using ports.
    func killAll() async {
        for port in ports {
            _ = await scanner.killProcessGracefully(pid: port.pid)
        }
        ports.removeAll()
        await refresh()
    }
}
```

## File: `platforms/macos/Sources/AppState+ProcessTypeNotifications.swift`
```
import Foundation
import Defaults

extension AppState {
    /// Checks for new ports matching enabled process type notifications.
    /// Call after each scan to detect newly appeared ports.
    func checkProcessTypeNotifications(oldPorts: [PortInfo], newPorts: [PortInfo]) {
        let enabledTypes = Defaults[.notifyProcessTypes]
        guard !enabledTypes.isEmpty else { return }

        let oldPortPids = Set(oldPorts.map { "\($0.port)-\($0.pid)" })

        for port in newPorts {
            let key = "\(port.port)-\(port.pid)"
            guard !oldPortPids.contains(key) else { continue }
            guard enabledTypes.contains(port.processType.rawValue) else { continue }

            NotificationService.shared.notify(
                title: "New \(port.processType.rawValue) on Port \(port.port)",
                body: "\(port.processName) started listening."
            )
        }
    }
}
```

## File: `platforms/macos/Sources/AppState+ProcessTypeOverrides.swift`
```
import Foundation
import Defaults

extension AppState {
    /// Sets a process type override for a given process name
    func setProcessTypeOverride(processName: String, type: ProcessType) {
        Defaults[.processTypeOverrides][processName] = type.rawValue
    }

    /// Clears the process type override for a given process name
    func clearProcessTypeOverride(processName: String) {
        Defaults[.processTypeOverrides].removeValue(forKey: processName)
    }

    /// Returns the overridden process type for a process name, if any
    func processTypeOverride(for processName: String) -> ProcessType? {
        guard let rawValue = Defaults[.processTypeOverrides][processName] else { return nil }
        return ProcessType(rawValue: rawValue)
    }
}
```

## File: `platforms/macos/Sources/AppState+WatchedPorts.swift`
```
import Foundation

extension AppState {
    /// Toggles watch status for a port (delegates to WatchedPortsState)
    func toggleWatch(_ port: Int) {
        watchedPortsState.toggle(port)
    }

    /// Checks if a port is being watched (delegates to WatchedPortsState)
    func isWatching(_ port: Int) -> Bool {
        watchedPortsState.isWatching(port)
    }

    /// Updates notification preferences for a watched port (delegates to WatchedPortsState)
    func updateWatch(_ port: Int, onStart: Bool, onStop: Bool) {
        watchedPortsState.updateWatch(port, onStart: onStart, onStop: onStop)
    }

    /// Removes a watched port by its ID (delegates to WatchedPortsState)
    func removeWatch(_ id: UUID) {
        watchedPortsState.removeWatch(id)
    }

    /// Checks watched ports for state changes and triggers notifications
    func checkWatchedPorts() {
        watchedPortsState.checkForChanges(ports: ports)
    }
}
```

## File: `platforms/macos/Sources/AppState.swift`
```
import Foundation
import SwiftUI
import Defaults
import KeyboardShortcuts
import Sparkle

// MARK: - Defaults Keys

extension Defaults.Keys {
    static let favorites = Key<Set<Int>>("favorites", default: [])
    static let watchedPorts = Key<[WatchedPort]>("watchedPorts", default: [])
    static let useTreeView = Key<Bool>("useTreeView", default: false)
    static let hideSystemProcesses = Key<Bool>("hideSystemProcesses", default: false)
    static let skipKillConfirmation = Key<Bool>("skipKillConfirmation", default: false)
    static let refreshInterval = Key<Int>("refreshInterval", default: 5)
    static let cloudflaredProtocol = Key<CloudflaredProtocol>("cloudflaredProtocol", default: .http2)

    // Process type overrides (processName → ProcessType.rawValue)
    static let processTypeOverrides = Key<[String: String]>("processTypeOverrides", default: [:])

    // Port labels (port number string → custom name)
    static let portLabels = Key<[String: String]>("portLabels", default: [:])

    // Process type notification filters (rawValues of enabled types, empty = disabled)
    static let notifyProcessTypes = Key<Set<String>>("notifyProcessTypes", default: [])

    // Auto-kill rules
    static let autoKillRules = Key<[AutoKillRule]>("autoKillRules", default: [])

    // Kubernetes-related keys
    static let customNamespaces = Key<[String]>("customNamespaces", default: [])

    // Onboarding
    static let hasCompletedOnboarding = Key<Bool>("hasCompletedOnboarding", default: false)

    // Sponsor-related keys
    static let sponsorCache = Key<SponsorCache?>("sponsorCache", default: nil)
    static let lastSponsorWindowShown = Key<Date?>("lastSponsorWindowShown", default: nil)
    static let sponsorDisplayInterval = Key<SponsorDisplayInterval>("sponsorDisplayInterval", default: .bimonthly)
}

// MARK: - Keyboard Shortcuts

extension KeyboardShortcuts.Name {
    static let toggleMainWindow = Self("toggleMainWindow")
}

// MARK: - App State

/// AppState manages the core application state including ports, favorites,
/// watched ports, filters, keyboard shortcuts, and auto-refresh functionality.
@Observable
@MainActor
final class AppState {
    // MARK: - Decomposed State Objects

    /// Manages favorite ports (extracted state)
    let favoritesState: FavoritesState

    /// Manages watched ports (extracted state)
    let watchedPortsState: WatchedPortsState

    // MARK: - Port State

    /// All currently scanned ports
    var ports: [PortInfo] = []

    /// Whether a port scan is currently in progress
    var isScanning = false

    // MARK: - Filter State

    /// Current filter settings for the port list
    var filter = PortFilter()

    /// Currently selected sidebar item (affects which ports are shown)
    var selectedSidebarItem: SidebarItem = .allPorts

    /// ID of the currently selected port in the detail view
    var selectedPortID: String? = nil

    /// The currently selected port, if any
    var selectedPort: PortInfo? {
        guard let id = selectedPortID else { return nil }
        return ports.first { $0.id == id }
    }

    /// ID of the currently selected port-forward connection
    var selectedPortForwardConnectionId: UUID? = nil

    /// The currently selected port-forward connection, if any
    var selectedPortForwardConnection: PortForwardConnectionState? {
        guard let id = selectedPortForwardConnectionId else { return nil }
        return portForwardManager.connections.first { $0.id == id }
    }

    // MARK: - Cached Filtered Ports (Memory Optimization)

    /// Cache for filtered ports to avoid repeated allocations
    @ObservationIgnored private var _cachedFilteredPorts: [PortInfo] = []
    @ObservationIgnored private var _filterCacheKey: FilterCacheKey?

    /// Cache key to detect when recalculation is needed
    private struct FilterCacheKey: Equatable {
        let portsCount: Int
        let portsHash: Int
        let sidebarItem: SidebarItem
        let filterActive: Bool
        let filterText: String
        let hideSystem: Bool
        let favoritesCount: Int
        let watchedCount: Int
    }

    /// Returns filtered ports based on sidebar selection and active filters.
    /// Uses caching to avoid repeated array allocations on each access.
    var filteredPorts: [PortInfo] {
        let currentKey = FilterCacheKey(
            portsCount: ports.count,
            portsHash: ports.isEmpty ? 0 : ports[0].hashValue ^ ports.count,
            sidebarItem: selectedSidebarItem,
            filterActive: filter.isActive,
            filterText: filter.searchText,
            hideSystem: Defaults[.hideSystemProcesses],
            favoritesCount: favorites.count,
            watchedCount: watchedPorts.count
        )

        // Return cached value if nothing changed
        if currentKey == _filterCacheKey {
            return _cachedFilteredPorts
        }

        // Recompute and cache
        _cachedFilteredPorts = computeFilteredPorts()
        _filterCacheKey = currentKey
        return _cachedFilteredPorts
    }

    /// Computes filtered ports (called only when cache is invalidated)
    private func computeFilteredPorts() -> [PortInfo] {
        if case .settings = selectedSidebarItem { return [] }

        var result: [PortInfo]

        switch selectedSidebarItem {
        case .allPorts, .settings, .sponsors, .kubernetesPortForward, .cloudflareTunnels:
            result = ports
        case .favorites:
            var activePorts = Set<Int>()
            result = ports.compactMap { port -> PortInfo? in
                guard favorites.contains(port.port) else { return nil }
                activePorts.insert(port.port)
                return port
            }
            for favPort in favorites where !activePorts.contains(favPort) {
                result.append(PortInfo.inactive(port: favPort))
            }
        case .watched:
            let watchedPortNumbers = Set(watchedPorts.map { $0.port })
            var activePorts = Set<Int>()
            result = ports.compactMap { port -> PortInfo? in
                guard watchedPortNumbers.contains(port.port) else { return nil }
                activePorts.insert(port.port)
                return port
            }
            for watchedPort in watchedPortNumbers where !activePorts.contains(watchedPort) {
                result.append(PortInfo.inactive(port: watchedPort))
            }
        case .processType(let type):
            result = ports.filter { $0.processType == type }
        }

        if filter.isActive {
            result = result.filter { filter.matches($0, favorites: favorites, watched: watchedPorts) }
        }

        if Defaults[.hideSystemProcesses] {
            result = result.filter { $0.processType != .system }
        }

        return result
    }

    // MARK: - Backward Compatibility Accessors

    /// Port numbers marked as favorites by the user (delegates to FavoritesState)
    var favorites: Set<Int> {
        get { favoritesState.favorites }
        set { favoritesState.favorites = newValue }
    }

    /// Ports being watched for state changes (delegates to WatchedPortsState)
    var watchedPorts: [WatchedPort] {
        get { watchedPortsState.watchedPorts }
        set { watchedPortsState.watchedPorts = newValue }
    }

    /// Tracks previous port states for watch notifications (delegates to WatchedPortsState)
    var previousPortStates: [Int: Bool] {
        get { watchedPortsState.previousPortStates }
        set { watchedPortsState.previousPortStates = newValue }
    }

    // MARK: - Managers

    /// Manages Sparkle auto-update functionality
    let updateManager = UpdateManager()

    /// Manages Kubernetes port-forward connections
    let portForwardManager = PortForwardManager()

    /// Manages Cloudflare tunnel connections
    let tunnelManager = TunnelManager()

    // MARK: - Internal Properties (for extensions)

    /// Port scanning actor
    let scanner: PortScannerProtocol

    /// Background task for auto-refresh
    @ObservationIgnored var refreshTask: Task<Void, Never>?
    /// Coalesces concurrent refresh requests into a single follow-up scan.
    @ObservationIgnored var hasPendingRefreshRequest = false

    // MARK: - Initialization

    init(
        scanner: PortScannerProtocol = PortScanner(),
        favoritesState: FavoritesState? = nil,
        watchedPortsState: WatchedPortsState? = nil
    ) {
        self.scanner = scanner
        self.favoritesState = favoritesState ?? FavoritesState()
        self.watchedPortsState = watchedPortsState ?? WatchedPortsState()

        setupKeyboardShortcuts()
        startAutoRefresh()
    }

    deinit {
        refreshTask?.cancel()
    }
}
```

## File: `platforms/macos/Sources/Constants.swift`
```
import Foundation

// MARK: - App Information

/**
 * AppInfo provides application metadata and external links.
 */
enum AppInfo {
    /// Application version from bundle info (e.g., "1.3.0")
    static let version: String = {
        Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String ?? "1.3.0"
    }()

    /// Build number from bundle info (e.g., "42")
    static let build: String = {
        Bundle.main.infoDictionary?["CFBundleVersion"] as? String ?? "1"
    }()

    /// Formatted version string (e.g., "v1.3.0 (42)")
    static let versionString: String = {
        "v\(version) (\(build))"
    }()

    /// GitHub repository URL
    static let githubRepo = "https://github.com/productdevbook/port-killer"

    /// GitHub releases page URL
    static let githubReleases = "https://github.com/productdevbook/port-killer/releases"

    /// GitHub sponsors page URL
    static let githubSponsors = "https://github.com/sponsors/productdevbook"

    /// GitHub issues page URL
    static let githubIssues = "https://github.com/productdevbook/port-killer/issues"

    /// Twitter/X profile URL
    static let twitterURL = "https://x.com/productdevbook"
}

// MARK: - Application Constants

/**
 * AppConstants defines core application configuration values.
 */
enum AppConstants {
    /// Default refresh interval in seconds
    static let defaultRefreshInterval: Int = 5

    /// Grace period between SIGTERM and SIGKILL when killing processes
    static let killGracePeriod: Duration = .milliseconds(500)

    /// Maximum length for displayed command strings
    static let maxCommandLength: Int = 200

    /// How long to cache sponsor data before refreshing (1 day)
    static let sponsorCacheExpiry: TimeInterval = 86400
}

// MARK: - UI Constants

/**
 * UIConstants defines size and layout constants for UI components.
 */
enum UIConstants {
    /**
     * Menu bar view dimensions
     */
    enum MenuBar {
        /// Fixed width of menu bar popover
        static let width: CGFloat = 340

        /// Maximum height of menu bar popover
        static let maxHeight: CGFloat = 400

        /// Height of each port row
        static let rowHeight: CGFloat = 44
    }

    /**
     * Main window dimensions
     */
    enum MainWindow {
        /// Minimum window width
        static let minWidth: CGFloat = 800

        /// Minimum window height
        static let minHeight: CGFloat = 500
    }
}
```

## File: `platforms/macos/Sources/PortKillerApp.swift`
```
import SwiftUI
import Defaults

@MainActor
final class AppDelegate: NSObject, NSApplicationDelegate {
    var appState: AppState?

    func applicationDidFinishLaunching(_ notification: Notification) {
        // Start as accessory (menu bar only, no Dock icon)
        NSApp.setActivationPolicy(.accessory)

        // Initialize notification service for watched port alerts
        NotificationService.shared.setup()

        // Monitor window visibility to toggle Dock icon
        NotificationCenter.default.addObserver(
            self,
            selector: #selector(windowDidBecomeKey),
            name: NSWindow.didBecomeKeyNotification,
            object: nil
        )
        NotificationCenter.default.addObserver(
            self,
            selector: #selector(windowWillClose),
            name: NSWindow.willCloseNotification,
            object: nil
        )
    }

    @objc private func windowDidBecomeKey(_ notification: Notification) {
        guard let window = notification.object as? NSWindow,
              window.title == "PortKiller" else { return }
        // Show in Dock when main window is open
        NSApp.setActivationPolicy(.regular)
    }

    @objc private func windowWillClose(_ notification: Notification) {
        guard let window = notification.object as? NSWindow,
              window.title == "PortKiller" else { return }
        // Hide from Dock when main window closes
        NSApp.setActivationPolicy(.accessory)
    }

    func applicationShouldTerminate(_ sender: NSApplication) -> NSApplication.TerminateReply {
        guard let appState = appState else {
            return .terminateNow
        }

        // Kill all port-forward connections and tunnels before terminating
        Task {
            await appState.portForwardManager.killStuckProcesses()
            await appState.tunnelManager.stopAllTunnels()
            await MainActor.run {
                NSApp.reply(toApplicationShouldTerminate: true)
            }
        }

        return .terminateLater
    }
}

@main
struct PortKillerApp: App {
    @NSApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    @State private var state = AppState()
    @State private var sponsorManager = SponsorManager()
    @State private var showOnboarding = !Defaults[.hasCompletedOnboarding]
    @Environment(\.openWindow) private var openWindow

    init() {
        // Disable automatic window tabbing (prevents Chrome-like tabs)
        NSWindow.allowsAutomaticWindowTabbing = false
    }

    var body: some Scene {
        // Main Window - Single instance only
        Window("PortKiller", id: "main") {
            MainWindowView()
                .environment(state)
                .environment(sponsorManager)
                .sheet(isPresented: $showOnboarding) {
                    OnboardingView()
                }
                .task {
                    // Pass state to AppDelegate for termination handling
                    appDelegate.appState = state

                    // Auto-start port-forward connections if enabled
                    if Defaults[.portForwardAutoStart] {
                        try? await Task.sleep(for: .seconds(1))
                        state.portForwardManager.startAll()
                    }

                    try? await Task.sleep(for: .seconds(3))
                    sponsorManager.checkAndShowIfNeeded()
                }
                .onChange(of: sponsorManager.shouldShowWindow) { _, shouldShow in
                    if shouldShow {
                        state.selectedSidebarItem = .sponsors
                        NSApp.activate(ignoringOtherApps: true)
                        openWindow(id: "main")
                        sponsorManager.markWindowShown()
                    }
                }
        }
        .windowStyle(.automatic)
        .defaultSize(width: 1000, height: 600)
        .commands {
            CommandGroup(replacing: .newItem) {} // Disable Cmd+N

            CommandGroup(after: .appInfo) {
				Button("Check for Updates...", systemImage: "arrow.triangle.2.circlepath") {
					state.updateManager.checkForUpdates()
				}
				.disabled(!state.updateManager.canCheckForUpdates)
            }

            CommandGroup(after: .newItem) {
                Button("Open Port Forwarder Window") {
                    NSApp.activate(ignoringOtherApps: true)
                    openWindow(id: "port-forwarder")
                }
                .keyboardShortcut("k", modifiers: [.command, .shift])
            }
        }

        // Port Forwarder Window
        Window("Port Forwarder", id: "port-forwarder") {
            PortForwarderWindowView()
                .environment(state)
        }
        .windowStyle(.automatic)
        .defaultSize(width: 900, height: 650)

        // Menu Bar (quick access)
        MenuBarExtra {
            MenuBarView(state: state)
        } label: {
            Image(nsImage: menuBarIcon())
        }
        .menuBarExtraStyle(.window)
    }

    private func menuBarIcon() -> NSImage {
        // Try various bundle paths for icon
        let paths = [
            Bundle.main.resourceURL?.appendingPathComponent("PortKiller_PortKiller.bundle"),
            Bundle.main.bundleURL.appendingPathComponent("PortKiller_PortKiller.bundle"),
            Bundle.main.resourceURL,
            Bundle.main.bundleURL
        ]
        for p in paths {
            if let url = p?.appendingPathComponent("ToolbarIcon@2x.png"),
               FileManager.default.fileExists(atPath: url.path()),
               let img = NSImage(contentsOf: url) {
                img.size = NSSize(width: 18, height: 18)
                img.isTemplate = true  // Enable template mode for monochrome menu bar icon
                return img
            }
        }
        // Fallback to system icon
        return NSImage(systemSymbolName: "network", accessibilityDescription: "PortKiller") ?? NSImage()
    }
}
```

## File: `platforms/macos/Sources/PortScanner.swift`
```
import Foundation
import Darwin

/**
 * PortScanner is a Swift actor that safely scans system ports and manages process termination.
 *
 * This actor provides thread-safe port scanning and process killing operations.
 * It uses system commands (lsof, ps, kill) to interact with the operating system.
 *
 * Key responsibilities:
 * - Scan all listening TCP ports using lsof
 * - Retrieve full command information for processes using ps
 * - Kill processes gracefully (SIGTERM then SIGKILL)
 * - Parse lsof output into structured PortInfo objects
 *
 * Thread Safety:
 * This is an actor, so all methods are isolated and can be called safely from any context.
 */
actor PortScanner: PortScannerProtocol {

    /**
     * Scans all listening TCP ports using lsof.
     *
     * Executes: `lsof -iTCP -sTCP:LISTEN -P -n +c 0`
     *
     * Flags explained:
     * - -iTCP: Show only TCP connections
     * - -sTCP:LISTEN: Show only listening sockets
     * - -P: Show port numbers (don't resolve to service names)
     * - -n: Show IP addresses (don't resolve to hostnames)
     * - +c 0: Show full command name (unlimited length)
     *
     * @returns Array of PortInfo objects representing all listening ports
     */
    func scanPorts() async -> [PortInfo] {
        // Wrap entire Process/Pipe lifecycle in autoreleasepool to release Obj-C bridged
        // objects (Process, Pipe, FileHandle, URL, Data) immediately after each scan.
        // Without this, these objects accumulate across the long-lived scanning Task,
        // causing ~35KB per scan × 47,520 scans over 66 hours = ~1.7GB leak.
        let output: String = autoreleasepool {
            let process = Process()
            process.executableURL = URL(fileURLWithPath: "/usr/sbin/lsof")
            process.arguments = ["-iTCP", "-sTCP:LISTEN", "-P", "-n", "+c", "0"]

            let pipe = Pipe()
            process.standardOutput = pipe
            process.standardError = FileHandle.nullDevice

            do {
                try process.run()

                // CRITICAL: Read data BEFORE waitUntilExit to avoid deadlock.
                // If lsof output exceeds the pipe buffer (~64KB), lsof blocks waiting
                // to write. If we waitUntilExit first, we deadlock.
                let data = pipe.fileHandleForReading.readDataToEndOfFile()
                process.waitUntilExit()

                return String(data: data, encoding: .utf8) ?? ""
            } catch {
                print("[PortScanner] Failed to scan ports: \(error.localizedDescription)")
                return ""
            }
        }

        guard !output.isEmpty else { return [] }

        // Extract PIDs from lsof output, then get command lines via sysctl (no process spawn)
        let pids = extractPids(from: output)
        let commands = pids.isEmpty ? [:] : getProcessCommands(for: pids)
        return parseLsofOutput(output, commands: commands)
    }

    /// Extracts unique PIDs from raw lsof output (second column of each data line).
    nonisolated private func extractPids(from output: String) -> Set<Int> {
        var pids = Set<Int>()
        let lines = output.split(separator: "\n", omittingEmptySubsequences: false)
        for line in lines.dropFirst() {
            guard !line.isEmpty else { continue }
            let components = line.split(separator: " ", omittingEmptySubsequences: true)
            guard components.count >= 2, let pid = Int(components[1]) else { continue }
            pids.insert(pid)
        }
        return pids
    }

    /**
     * Retrieves full command lines for specific processes via sysctl.
     *
     * Uses `sysctl(KERN_PROCARGS2)` to read each process's argv directly from the kernel.
     * This eliminates the `ps` process spawn entirely — no fork/exec, no Pipe, no FileHandle,
     * no Obj-C bridged objects. Pure C syscalls with minimal memory allocation.
     *
     * Cost comparison per scan (typical system, ~30 listening ports):
     *   ps approach:  fork+exec + pipe I/O + ~500KB string + parse = ~5ms, ~500KB peak RAM
     *   sysctl:       ~30 syscalls × ~2KB each = ~0.3ms, ~4KB peak RAM
     *
     * @param pids - Set of process IDs to query
     * @returns Dictionary mapping PID to full command string
     */
    nonisolated private func getProcessCommands(for pids: Set<Int>) -> [Int: String] {
        var commands: [Int: String] = [:]
        commands.reserveCapacity(pids.count)

        for pid in pids {
            if let cmd = commandLine(for: pid) {
                commands[pid] = cmd
            }
        }

        return commands
    }

    /// Reads a process's full command line (argv) from the kernel via sysctl.
    ///
    /// KERN_PROCARGS2 returns: [argc: Int32][exec_path\0][\0 padding][argv[0]\0][argv[1]\0]...
    /// We parse argc arguments and join them with spaces to match `ps -o command` output.
    /// Falls back to nil for system processes that restrict access (parseLsofOutput
    /// handles this by using the process name from lsof instead).
    nonisolated private func commandLine(for pid: Int) -> String? {
        var mib: [Int32] = [CTL_KERN, KERN_PROCARGS2, Int32(pid)]
        var size: Int = 0

        // First call: get required buffer size
        guard sysctl(&mib, 3, nil, &size, nil, 0) == 0,
              size > MemoryLayout<Int32>.size else { return nil }

        // Second call: read the data
        var buffer = [UInt8](repeating: 0, count: size)
        guard sysctl(&mib, 3, &buffer, &size, nil, 0) == 0 else { return nil }

        // Read argc from the first 4 bytes
        let argc = buffer.withUnsafeBytes { $0.load(as: Int32.self) }
        guard argc > 0 else { return nil }

        var pos = MemoryLayout<Int32>.size

        // Skip the executable path
        while pos < size && buffer[pos] != 0 { pos += 1 }
        // Skip null padding between exec path and argv
        while pos < size && buffer[pos] == 0 { pos += 1 }

        // Collect up to argc arguments (cap at 64 for safety)
        let maxArgs = min(argc, 64)
        var args = [String]()
        args.reserveCapacity(Int(maxArgs))
        var collected: Int32 = 0

        while pos < size && collected < maxArgs {
            let start = pos
            while pos < size && buffer[pos] != 0 { pos += 1 }
            if pos > start {
                args.append(String(decoding: buffer[start..<pos], as: UTF8.self))
            }
            pos += 1
            collected += 1
        }

        return args.isEmpty ? nil : args.joined(separator: " ")
    }

    /**
     * Parses lsof command output into structured PortInfo objects.
     *
     * Expected lsof output format:
     * ```
     * COMMAND    PID  USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
     * node     34805  code   19u  IPv6 0x3d8015e195af1f3f      0t0  TCP [::1]:3000 (LISTEN)
     * ```
     *
     * This method:
     * 1. Skips the header line
     * 2. Parses each line to extract process and port information
     * 3. Handles escaped characters in process names (e.g., "Code\x20H" → "Code H")
     * 4. Merges with command information from ps
     * 5. Deduplicates entries (same port + PID)
     *
     * @param output - Raw string output from lsof command
     * @param commands - Dictionary of PID to full command string from ps
     * @returns Array of unique PortInfo objects, sorted by port number
     */
    nonisolated private func parseLsofOutput(_ output: String, commands: [Int: String]) -> [PortInfo] {
        var ports: [PortInfo] = []
        var seen: Set<String> = []
        // Use split for zero-copy Substring iteration (no allocation per line)
        let lines = output.split(separator: "\n", omittingEmptySubsequences: false)

        // Skip header line and process each data line
        for line in lines.dropFirst() {
            guard !line.isEmpty else { continue }

            // Parse lsof output columns:
            // COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
            // Example: node      34805 code   19u  IPv6 0x3d8015e195af1f3f      0t0  TCP [::1]:3000 (LISTEN)
            let components = line.split(separator: " ", omittingEmptySubsequences: true)
            guard components.count >= 9 else { continue }

            // Extract process name and decode all hex escape sequences from lsof
            // lsof escapes special/non-ASCII characters as \xHH sequences
            // e.g., "Code\x20Helper", "\xe4\xbc\x81\xe4\xb8\x9a" (企业)
            let processName = Self.decodeLsofEscapes(String(components[0]))

            guard let pid = Int(components[1]) else { continue }

            // User name - use Substring directly where possible
            let user = String(components[2])

            // File descriptor
            let fd = String(components[3])

            // Extract the NAME column (address:port)
            // It's usually the second-to-last column, before "(LISTEN)"
            // Format: "127.0.0.1:3000", "*:8080", or "[::1]:3000"
            // We search backwards to find a component with ":" that isn't a device ID
            var addressPart: Substring = ""
            for i in stride(from: components.count - 1, through: 8, by: -1) {
                let comp = components[i]
                // Skip device IDs (0x...) and sizes (0t...)
                if comp.contains(":") && !comp.hasPrefix("0x") && !comp.hasPrefix("0t") {
                    addressPart = comp
                    break
                }
            }

            guard !addressPart.isEmpty else { continue }

            // Get full command from ps output
            let command = commands[pid] ?? processName

            guard let portInfo = parseAddress(String(addressPart), processName: processName, pid: pid, user: user, command: command, fd: fd) else {
                continue
            }

            // Avoid duplicates (same port + pid) using O(1) Set lookup
            let key = "\(portInfo.port)-\(portInfo.pid)"
            if seen.insert(key).inserted {
                ports.append(portInfo)
            }
        }

        return ports.sorted { $0.port < $1.port }
    }

    /**
     * Parses an address:port string into a PortInfo object.
     *
     * Handles multiple address formats:
     * - IPv4: "127.0.0.1:3000" or "*:8080"
     * - IPv6: "[::1]:3000" or "[fe80::1]:8080"
     *
     * @param address - The address:port string to parse
     * @param processName - Name of the process using the port
     * @param pid - Process ID
     * @param user - User running the process
     * @param command - Full command line of the process
     * @param fd - File descriptor number
     * @returns PortInfo object or nil if parsing fails
     */
    nonisolated private func parseAddress(_ address: String, processName: String, pid: Int, user: String, command: String, fd: String) -> PortInfo? {
        let parts: [String]

        if address.hasPrefix("[") {
            // IPv6 format: [::1]:3000
            // Split on the closing bracket to separate address from port
            guard let bracketEnd = address.firstIndex(of: "]") else { return nil }
            let afterBracket = address.index(after: bracketEnd)
            guard afterBracket < address.endIndex, address[afterBracket] == ":" else { return nil }
            let portStart = address.index(after: afterBracket)
            let addr = String(address[address.startIndex...bracketEnd])
            let port = String(address[portStart...])
            parts = [addr, port]
        } else {
            // IPv4 format: 127.0.0.1:3000 or *:8080
            parts = address.components(separatedBy: ":")
        }

        guard parts.count >= 2,
              let port = Int(parts.last ?? "") else {
            return nil
        }

        let addr = parts.dropLast().joined(separator: ":")

        return PortInfo.active(
            port: port,
            pid: pid,
            processName: processName,
            address: addr.isEmpty ? "*" : addr,
            user: user,
            command: command,
            fd: fd
        )
    }

    /**
     * Decodes lsof hex escape sequences (\xHH) into proper characters.
     *
     * lsof escapes non-ASCII bytes and some special characters as \xHH sequences.
     * This method collects all escaped bytes and decodes them as UTF-8, which
     * correctly handles multi-byte characters like Chinese (e.g., \xe4\xbc\x81 → 企).
     */
    nonisolated static func decodeLsofEscapes(_ input: String) -> String {
        var result = ""
        var pendingBytes: [UInt8] = []
        var i = input.startIndex

        while i < input.endIndex {
            // Check for \xHH pattern
            if input[i] == "\\" {
                let next = input.index(after: i)
                if next < input.endIndex, input[next] == "x" {
                    let hexStart = input.index(after: next)
                    let hexEnd = input.index(hexStart, offsetBy: 2, limitedBy: input.endIndex)
                    if let hexEnd, let byte = UInt8(input[hexStart..<hexEnd], radix: 16) {
                        pendingBytes.append(byte)
                        i = hexEnd
                        continue
                    }
                }
            }

            // Flush any pending bytes as UTF-8 before appending a literal character
            if !pendingBytes.isEmpty {
                result += String(decoding: pendingBytes, as: UTF8.self)
                pendingBytes.removeAll()
            }
            result.append(input[i])
            i = input.index(after: i)
        }

        // Flush remaining bytes
        if !pendingBytes.isEmpty {
            result += String(decoding: pendingBytes, as: UTF8.self)
        }

        return result
    }

    /**
     * Kills a process by sending a termination signal.
     *
     * Executes: `kill -15 <PID>` (SIGTERM) or `kill -9 <PID>` (SIGKILL)
     *
     * @param pid - The process ID to kill
     * @param force - If true, sends SIGKILL (-9) instead of SIGTERM (-15)
     * @returns True if the kill command executed successfully (exit code 0)
     */
    func killProcess(pid: Int, force: Bool = false) async -> Bool {
        // Direct syscall — no Process/Pipe/FileHandle overhead
        Darwin.kill(Int32(pid), force ? SIGKILL : SIGTERM) == 0
    }

    /**
     * Attempts to kill a process gracefully, falling back to force kill if needed.
     *
     * Strategy:
     * 1. Send SIGTERM (graceful shutdown signal)
     * 2. Wait 500ms for process to clean up
     * 3. Send SIGKILL (immediate termination)
     *
     * This two-stage approach allows processes to:
     * - Close file handles properly
     * - Flush buffers to disk
     * - Send shutdown notifications
     * - Clean up temporary resources
     *
     * @param pid - The process ID to kill
     * @returns True if either kill command succeeded
     */
    func killProcessGracefully(pid: Int) async -> Bool {
        // Try SIGTERM first (allows graceful shutdown)
        let graceful = await killProcess(pid: pid, force: false)
        if graceful {
            // Give the process time to clean up (500ms grace period)
            try? await Task.sleep(for: .milliseconds(500))
        }

        // Force kill with SIGKILL (immediate termination)
        return await killProcess(pid: pid, force: true)
    }

    /**
     * Finds PIDs of processes with ESTABLISHED connections to a specific port.
     *
     * Executes: `lsof -iTCP:<port> -sTCP:ESTABLISHED -P -n +c 0`
     *
     * Used for "deep kill" to also terminate client connections that remain
     * after the listening process is killed.
     *
     * @param port - The port number to check for established connections
     * @returns Set of PIDs with established connections
     */
    func findEstablishedPids(for port: Int) async -> Set<Int> {
        let output: String = autoreleasepool {
            let process = Process()
            process.executableURL = URL(fileURLWithPath: "/usr/sbin/lsof")
            process.arguments = ["-iTCP:\(port)", "-sTCP:ESTABLISHED", "-P", "-n", "+c", "0"]

            let pipe = Pipe()
            process.standardOutput = pipe
            process.standardError = FileHandle.nullDevice

            do {
                try process.run()
                let data = pipe.fileHandleForReading.readDataToEndOfFile()
                process.waitUntilExit()
                return String(data: data, encoding: .utf8) ?? ""
            } catch {
                return ""
            }
        }

        guard !output.isEmpty else { return [] }

        var pids = Set<Int>()
        let lines = output.split(separator: "\n", omittingEmptySubsequences: false)
        for line in lines.dropFirst() {
            guard !line.isEmpty else { continue }
            let components = line.split(separator: " ", omittingEmptySubsequences: true)
            guard components.count >= 2, let pid = Int(components[1]) else { continue }
            pids.insert(pid)
        }
        return pids
    }
}
```

## File: `platforms/macos/Sources/Extensions/ProcessType+Color.swift`
```
/**
 * ProcessType+Color.swift
 * PortKiller
 *
 * Provides color representation for process types in the UI.
 */

import SwiftUI

extension ProcessType {
    /// Color associated with this process type for UI display
    var color: Color {
        switch self {
        case .webServer: return .blue
        case .database: return .purple
        case .development: return .orange
        case .system: return .gray
        case .other: return .secondary
        }
    }
}
```

## File: `platforms/macos/Sources/Managers/KubernetesDiscoveryManager.swift`
```
import Foundation
import Defaults

// MARK: - Discovery State

enum KubernetesDiscoveryState: Equatable, Sendable {
    case idle
    case loading
    case loaded
    case error(String)
}

// MARK: - Kubernetes Discovery Manager

@Observable
@MainActor
final class KubernetesDiscoveryManager: Identifiable {
    let id = UUID()

    var namespaces: [KubernetesNamespace] = []
    var services: [KubernetesService] = []
    var selectedNamespace: KubernetesNamespace?
    var selectedService: KubernetesService?
    var selectedPort: KubernetesService.ServicePort?
    var proxyEnabled = true

    var namespaceState: KubernetesDiscoveryState = .idle
    var serviceState: KubernetesDiscoveryState = .idle

    private let processManager: PortForwardProcessManager

    init(processManager: PortForwardProcessManager) {
        self.processManager = processManager
    }

    // MARK: - Actions

    func loadNamespaces() async {
        namespaceState = .loading
        namespaces = []
        services = []
        selectedNamespace = nil
        selectedService = nil
        selectedPort = nil

        do {
            let fetchedNamespaces = try await processManager.fetchNamespaces()
            // Merge with custom namespaces
            let customNamespaceNames = Defaults[.customNamespaces]
            let customNamespaces = customNamespaceNames.map { KubernetesNamespace(name: $0, isCustom: true) }

            // Combine and remove duplicates (prefer auto-fetched over custom)
            var combinedNamespaces = fetchedNamespaces
            for customNS in customNamespaces {
                if !combinedNamespaces.contains(where: { $0.name == customNS.name }) {
                    combinedNamespaces.append(customNS)
                }
            }

            namespaces = combinedNamespaces.sorted { $0.name < $1.name }
            namespaceState = .loaded
        } catch {
            // On error, fall back to custom namespaces only
            let customNamespaceNames = Defaults[.customNamespaces]
            if !customNamespaceNames.isEmpty {
                namespaces = customNamespaceNames.map { KubernetesNamespace(name: $0, isCustom: true) }
                    .sorted { $0.name < $1.name }
                namespaceState = .loaded
            } else {
                let message = (error as? KubectlError)?.errorDescription ?? error.localizedDescription
                namespaceState = .error(message)
            }
        }
    }

    func selectNamespace(_ namespace: KubernetesNamespace) async {
        selectedNamespace = namespace
        selectedService = nil
        selectedPort = nil
        services = []
        serviceState = .loading

        do {
            services = try await processManager.fetchServices(namespace: namespace.name)
            serviceState = .loaded
        } catch {
            let message = (error as? KubectlError)?.errorDescription ?? error.localizedDescription
            serviceState = .error(message)
        }
    }

    func selectService(_ service: KubernetesService) {
        selectedService = service
        selectedPort = service.ports.first
    }

    func selectPort(_ port: KubernetesService.ServicePort) {
        selectedPort = port
    }

    // MARK: - Connection Creation

    func createConnectionConfig() -> PortForwardConnectionConfig? {
        guard let namespace = selectedNamespace,
              let service = selectedService,
              let port = selectedPort else {
            return nil
        }

        let remotePort = port.port
        let localPort = suggestLocalPort(for: remotePort)
        let proxyPort = proxyEnabled ? suggestProxyPort(for: localPort) : nil

        return PortForwardConnectionConfig(
            name: service.name,
            namespace: namespace.name,
            service: service.name,
            localPort: localPort,
            remotePort: remotePort,
            proxyPort: proxyPort
        )
    }

    func suggestLocalPort(for remotePort: Int) -> Int {
        switch remotePort {
        case 80: return 8080
        case 443: return 8443
        default:
            return remotePort > 1024 ? remotePort : remotePort + 8000
        }
    }

    func suggestProxyPort(for localPort: Int) -> Int {
        return localPort - 1
    }

    func reset() {
        namespaces = []
        services = []
        selectedNamespace = nil
        selectedService = nil
        selectedPort = nil
        namespaceState = .idle
        serviceState = .idle
    }

    // MARK: - Custom Namespace Management

    func addCustomNamespace(_ namespaceName: String) {
        let trimmedName = namespaceName.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmedName.isEmpty else { return }

        var customNamespaces = Defaults[.customNamespaces]
        if !customNamespaces.contains(trimmedName) {
            customNamespaces.append(trimmedName)
            Defaults[.customNamespaces] = customNamespaces

            // Add to current namespace list if not already present
            if !namespaces.contains(where: { $0.name == trimmedName }) {
                let newNamespace = KubernetesNamespace(name: trimmedName, isCustom: true)
                namespaces.append(newNamespace)
                namespaces.sort { $0.name < $1.name }

                // Update state to loaded if it was in error
                if case .error = namespaceState {
                    namespaceState = .loaded
                }
            }
        }
    }

    func addCustomNamespaces(_ namespaceNames: [String]) {
        for name in namespaceNames {
            addCustomNamespace(name)
        }
    }

    func removeCustomNamespace(_ namespace: KubernetesNamespace) {
        guard namespace.isCustom else { return }

        var customNamespaces = Defaults[.customNamespaces]
        customNamespaces.removeAll { $0 == namespace.name }
        Defaults[.customNamespaces] = customNamespaces

        // Remove from current namespace list
        namespaces.removeAll { $0.name == namespace.name }

        // If no namespaces left, reset to idle state
        if namespaces.isEmpty {
            namespaceState = .idle
        }
    }
}
```

## File: `platforms/macos/Sources/Managers/PortForwardManager+Execution.swift`
```
import Foundation
import Defaults

extension PortForwardManager {
    /// Runs the port forward process for a connection.
    func runPortForward(for state: PortForwardConnectionState, config: PortForwardConnectionConfig) async {
        // Direct exec mode: don't use kubectl port-forward, start exec proxy directly
        if config.useDirectExec, config.proxyPort != nil {
            await runDirectExecProxy(for: state, config: config)
            return
        }

        do {
            let process = try await processManager.startPortForward(
                id: state.id,
                namespace: config.namespace,
                service: config.service,
                localPort: config.localPort,
                remotePort: config.remotePort
            )

            try await Task.sleep(for: .seconds(2))

            if process.isRunning {
                state.portForwardStatus = .connected

                if config.proxyPort != nil {
                    state.proxyStatus = .connecting
                    state.proxyTask = Task {
                        await self.runProxy(for: state, config: config)
                    }
                } else {
                    sendConnectNotificationIfEnabled(for: config)
                }
            } else {
                state.portForwardStatus = .error
                state.lastError = "Port forward failed to start"
            }
        } catch {
            state.portForwardStatus = .error
            state.lastError = error.localizedDescription
        }
    }

    /// Runs the direct exec proxy for multi-connection support.
    func runDirectExecProxy(for state: PortForwardConnectionState, config: PortForwardConnectionConfig) async {
        guard let proxyPort = config.proxyPort else { return }

        state.portForwardStatus = .connected
        state.proxyStatus = .connecting

        do {
            let process = try await processManager.startDirectExecProxy(
                id: state.id,
                namespace: config.namespace,
                service: config.service,
                externalPort: proxyPort,
                remotePort: config.remotePort
            )

            try await Task.sleep(for: .seconds(1))

            if process.isRunning {
                state.proxyStatus = .connected
                sendConnectNotificationIfEnabled(for: config)
            } else {
                state.proxyStatus = .error
                state.portForwardStatus = .error
                state.lastError = "Direct exec proxy failed to start"
            }
        } catch {
            state.proxyStatus = .error
            state.portForwardStatus = .error
            state.lastError = error.localizedDescription
        }
    }

    /// Runs the socat proxy process.
    func runProxy(for state: PortForwardConnectionState, config: PortForwardConnectionConfig) async {
        guard let proxyPort = config.proxyPort else { return }

        do {
            let process = try await processManager.startProxy(
                id: state.id,
                externalPort: proxyPort,
                internalPort: config.localPort
            )

            try await Task.sleep(for: .seconds(1))

            if process.isRunning {
                state.proxyStatus = .connected
                sendConnectNotificationIfEnabled(for: config)
            } else {
                state.proxyStatus = .error
                state.lastError = "Socat proxy failed to start"
            }
        } catch {
            state.proxyStatus = .error
            state.lastError = error.localizedDescription
        }
    }

    /// Sends a connect notification if enabled (global + per-connection).
    func sendConnectNotificationIfEnabled(for config: PortForwardConnectionConfig) {
        guard Defaults[.portForwardShowNotifications] else { return }
        guard config.notifyOnConnect else { return }
        NotificationService.shared.notify(
            title: "Connected",
            body: "\(config.name) is ready on port \(config.proxyPort ?? config.localPort)"
        )
    }

    /// Sends a disconnect notification if enabled (global + per-connection).
    func sendDisconnectNotificationIfEnabled(for config: PortForwardConnectionConfig, wasIntentional: Bool) {
        guard !wasIntentional else { return }
        guard Defaults[.portForwardShowNotifications] else { return }
        guard config.notifyOnDisconnect else { return }
        NotificationService.shared.notify(
            title: "Disconnected",
            body: "\(config.name) connection lost"
        )
    }
}
```

## File: `platforms/macos/Sources/Managers/PortForwardManager+Monitoring.swift`
```
import Foundation

extension PortForwardManager {
    /// Starts the connection monitoring task.
    func startMonitoring() {
        if isMonitoring, let monitorTask, !monitorTask.isCancelled {
            return
        }

        monitorTask?.cancel()
        isMonitoring = true
        monitorTask = Task {
            while !Task.isCancelled && isMonitoring {
                await checkConnections()
                try? await Task.sleep(for: .seconds(1))
            }
        }
    }

    /// Stops the connection monitoring task.
    func stopMonitoring() {
        isMonitoring = false
        monitorTask?.cancel()
        monitorTask = nil
    }

    /// Checks all connections and reconnects if needed.
    func checkConnections() async {
        guard !isKillingProcesses else { return }
        // Take a snapshot to avoid data race during iteration
        let snapshot = connections
        for state in snapshot {
            guard state.config.isEnabled && state.config.autoReconnect else { continue }

            if state.config.useDirectExec, state.config.proxyPort != nil {
                await checkDirectExecConnection(state)
                continue
            }

            let localPort = state.config.localPort
            let processRunning = await processManager.isProcessRunning(for: state.id, type: .portForward)
            let hasError = await processManager.hasRecentError(for: state.id)
            let pfWorking = await processManager.isPortOpen(port: localPort)

            // Reconnect if disconnected or error
            if state.portForwardStatus == .disconnected || state.portForwardStatus == .error {
                await processManager.clearError(for: state.id)
                startConnection(state.id)
                continue
            }

            // Reconnect on error
            if state.portForwardStatus == .connected && hasError {
                let wasConnected = state.isFullyConnected
                state.lastError = "kubectl port-forward error on port \(localPort)"
                state.portForwardStatus = .disconnected
                state.proxyStatus = .disconnected
                if wasConnected {
                    sendDisconnectNotificationIfEnabled(for: state.config, wasIntentional: state.isIntentionallyStopped)
                }
                await processManager.killProcesses(for: state.id)
                await processManager.clearError(for: state.id)
                startConnection(state.id)
                continue
            }

            // Reconnect if process died
            if state.portForwardStatus == .connected && !processRunning {
                let wasConnected = state.isFullyConnected
                state.lastError = "Process terminated"
                state.portForwardStatus = .disconnected
                state.proxyStatus = .disconnected
                if wasConnected {
                    sendDisconnectNotificationIfEnabled(for: state.config, wasIntentional: state.isIntentionallyStopped)
                }
                startConnection(state.id)
                continue
            }

            // Reconnect if port not responding
            if state.portForwardStatus == .connected && !pfWorking {
                let wasConnected = state.isFullyConnected
                state.lastError = "Connection lost"
                state.portForwardStatus = .disconnected
                state.proxyStatus = .disconnected
                if wasConnected {
                    sendDisconnectNotificationIfEnabled(for: state.config, wasIntentional: state.isIntentionallyStopped)
                }
                await processManager.killProcesses(for: state.id)
                startConnection(state.id)
                continue
            }

            // Check proxy if enabled
            if let proxyPort = state.config.proxyPort {
                if state.proxyStatus == .disconnected && state.portForwardStatus == .connected {
                    state.proxyStatus = .connecting
                    state.proxyTask = Task {
                        await runProxy(for: state, config: state.config)
                    }
                    continue
                }

                let proxyWorking = await processManager.isPortOpen(port: proxyPort)
                if state.proxyStatus == .connected && !proxyWorking {
                    state.proxyStatus = .error
                    state.lastError = "Proxy connection lost"
                    if state.portForwardStatus == .connected {
                        state.proxyStatus = .connecting
                        state.proxyTask = Task {
                            await runProxy(for: state, config: state.config)
                        }
                    }
                }
            }
        }
    }

    /// Checks a direct exec connection and reconnects if needed.
    func checkDirectExecConnection(_ state: PortForwardConnectionState) async {
        guard state.config.proxyPort != nil else { return }

        if state.proxyStatus == .connecting {
            return
        }

        let proxyRunning = await processManager.isProcessRunning(for: state.id, type: .proxy)
        let hasError = await processManager.hasRecentError(for: state.id)

        if state.proxyStatus == .disconnected || state.proxyStatus == .error {
            await processManager.clearError(for: state.id)
            startConnection(state.id)
            return
        }

        if state.proxyStatus == .connected && hasError {
            let wasConnected = state.isFullyConnected
            state.lastError = "Proxy error on port \(state.config.proxyPort ?? 0)"
            state.portForwardStatus = .disconnected
            state.proxyStatus = .disconnected
            if wasConnected {
                sendDisconnectNotificationIfEnabled(for: state.config, wasIntentional: state.isIntentionallyStopped)
            }
            await processManager.killProcesses(for: state.id)
            await processManager.clearError(for: state.id)
            startConnection(state.id)
            return
        }

        if state.proxyStatus == .connected && !proxyRunning {
            let wasConnected = state.isFullyConnected
            state.lastError = "Proxy terminated"
            state.portForwardStatus = .disconnected
            state.proxyStatus = .disconnected
            if wasConnected {
                sendDisconnectNotificationIfEnabled(for: state.config, wasIntentional: state.isIntentionallyStopped)
            }
            startConnection(state.id)
            return
        }
    }
}
```

## File: `platforms/macos/Sources/Managers/PortForwardManager.swift`
```
import Foundation
import Defaults

// MARK: - Defaults Keys for Port Forwarder

extension Defaults.Keys {
    static let portForwardConnections = Key<[PortForwardConnectionConfig]>("portForwardConnections", default: [])
    static let portForwardAutoStart = Key<Bool>("portForwardAutoStart", default: false)
    static let portForwardShowNotifications = Key<Bool>("portForwardShowNotifications", default: true)
    static let customKubectlPath = Key<String?>("customKubectlPath", default: nil)
    static let customSocatPath = Key<String?>("customSocatPath", default: nil)
    static let customCloudflaredPath = Key<String?>("customCloudflaredPath", default: nil)
}

// MARK: - Port Forward Manager

@Observable
@MainActor
final class PortForwardManager {
    var connections: [PortForwardConnectionState] = []
    var isMonitoring = false
    var isKillingProcesses = false

    var monitorTask: Task<Void, Never>?
    let processManager = PortForwardProcessManager()

    var allConnected: Bool {
        guard !connections.isEmpty else { return false }
        return connections.allSatisfy(\.isFullyConnected)
    }

    var connectedCount: Int {
        connections.filter(\.isFullyConnected).count
    }

    // MARK: - Helper Methods

    /// Finds a connection state by its ID
    /// - Parameter id: The UUID of the connection to find
    /// - Returns: The connection state if found, nil otherwise
    func connection(for id: UUID) -> PortForwardConnectionState? {
        connections.first { $0.id == id }
    }

    /// Finds the index of a connection by its ID
    /// - Parameter id: The UUID of the connection to find
    /// - Returns: The index if found, nil otherwise
    func connectionIndex(for id: UUID) -> Int? {
        connections.firstIndex { $0.id == id }
    }

    init() {
        loadConnections()
    }

    // MARK: - Persistence

    func loadConnections() {
        let configs = Defaults[.portForwardConnections]
        connections = configs.map { PortForwardConnectionState(config: $0) }
    }

    func saveConnections() {
        Defaults[.portForwardConnections] = connections.map(\.config)
    }

    // MARK: - Connection CRUD

    func addConnection(_ config: PortForwardConnectionConfig) {
        connections.append(PortForwardConnectionState(config: config))
        saveConnections()
    }

    func removeConnection(_ id: UUID) {
        guard let index = connectionIndex(for: id) else { return }
        stopConnection(id)
        connections.remove(at: index)
        saveConnections()
    }

    func updateConnection(_ config: PortForwardConnectionConfig) {
        guard let index = connectionIndex(for: config.id) else { return }
        let wasConnected = connections[index].isFullyConnected
        if wasConnected {
            stopConnection(config.id)
        }
        connections[index].config = config
        saveConnections()
        if wasConnected && config.isEnabled {
            startConnection(config.id)
        }
    }

    // MARK: - Bulk Operations

    func startAll() {
        for connection in connections where connection.config.isEnabled {
            startConnection(connection.id)
        }
        startMonitoring()
    }

    func stopAll() {
        stopMonitoring()
        for connection in connections {
            stopConnection(connection.id)
        }
    }

    func killStuckProcesses() async {
        isKillingProcesses = true
        stopMonitoring()

        for connection in connections {
            connection.portForwardTask?.cancel()
            connection.proxyTask?.cancel()
            connection.portForwardTask = nil
            connection.proxyTask = nil
        }

        try? await Task.sleep(for: .milliseconds(200))

        await processManager.killAllPortForwarderProcesses()

        for connection in connections {
            connection.portForwardStatus = .disconnected
            connection.proxyStatus = .disconnected
        }

        isKillingProcesses = false
    }

    // MARK: - Single Connection Operations

    func startConnection(_ id: UUID) {
        guard !isKillingProcesses else { return }
        guard let state = connection(for: id) else { return }
        guard state.portForwardTask == nil, state.proxyTask == nil else { return }
        guard state.portForwardStatus != .connecting, state.proxyStatus != .connecting else { return }
        guard !state.isFullyConnected else { return }
        let config = state.config

        // Reset intentional stop flag when starting
        state.isIntentionallyStopped = false

        state.portForwardStatus = .connecting

        // Set up handlers and start port forward in a single task to ensure proper ordering
        state.portForwardTask = Task { [weak self, weak state] in
            guard let self = self, let state = state else { return }

            // Set log handler with proper weak capture (including inner Task)
            let logHandler: LogHandler = { [weak state] message, type, isError in
                guard let state = state else { return }
                Task { @MainActor [weak state] in
                    guard let state = state else { return }
                    state.appendLog(message, type: type, isError: isError)
                }
            }
            await self.processManager.setLogHandler(for: id, handler: logHandler)

            // Set port conflict handler with proper weak capture (including inner Task)
            let conflictHandler: PortConflictHandler = { [weak self, weak state] port in
                guard let self = self, let state = state else { return }
                Task { @MainActor [weak self, weak state] in
                    guard let self = self, let state = state else { return }
                    state.appendLog("Port \(port) in use, auto-recovering...", type: .portForward, isError: false)

                    await self.processManager.killProcessOnPort(port)

                    try? await Task.sleep(for: .milliseconds(500))

                    state.appendLog("Retrying connection...", type: .portForward, isError: false)
                    self.restartConnection(id)
                }
            }
            await self.processManager.setPortConflictHandler(for: id, handler: conflictHandler)

            await self.runPortForward(for: state, config: config)
        }
    }

    func stopConnection(_ id: UUID) {
        guard let state = connection(for: id) else { return }

        // Mark as intentionally stopped to avoid disconnect notification
        state.isIntentionallyStopped = true

        state.proxyTask?.cancel()
        state.proxyTask = nil
        state.proxyStatus = .disconnected

        state.portForwardTask?.cancel()
        state.portForwardTask = nil
        state.portForwardStatus = .disconnected

        // Clear logs to free memory when connection is stopped
        state.clearLogs()

        Task {
            await processManager.killProcesses(for: id)
            await processManager.removeLogHandler(for: id)
            await processManager.removePortConflictHandler(for: id)
        }
    }

    func restartConnection(_ id: UUID) {
        stopConnection(id)
        Task {
            try? await Task.sleep(for: .milliseconds(500))
            startConnection(id)
        }
    }
}
```

## File: `platforms/macos/Sources/Managers/PortForwardProcessManager+ConflictResolution.swift`
```
import Foundation
import Darwin

extension PortForwardProcessManager {
    /// Kills any process using the specified port.
    func killProcessOnPort(_ port: Int) async {
        // Wrap Process/Pipe lifecycle in autoreleasepool to release Obj-C bridged objects.
        // Read pipe data BEFORE waitUntilExit to avoid deadlock if output exceeds pipe buffer.
        let output: String = autoreleasepool {
            let lsof = Process()
            lsof.executableURL = URL(fileURLWithPath: "/usr/sbin/lsof")
            lsof.arguments = ["-ti", "tcp:\(port)"]

            let pipe = Pipe()
            lsof.standardOutput = pipe
            lsof.standardError = FileHandle.nullDevice

            do {
                try lsof.run()
                let data = pipe.fileHandleForReading.readDataToEndOfFile()
                lsof.waitUntilExit()
                return String(data: data, encoding: .utf8)?.trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
            } catch {
                return ""
            }
        }

        // Kill logic uses Darwin.kill (pure C) and await, so stays outside the pool
        if !output.isEmpty {
            let pids = output.split(separator: "\n")
            for pidStr in pids {
                if let pid = Int32(pidStr.trimmingCharacters(in: .whitespaces)) {
                    kill(pid, SIGTERM)
                }
            }

            try? await Task.sleep(for: .milliseconds(300))

            for pidStr in pids {
                if let pid = Int32(pidStr.trimmingCharacters(in: .whitespaces)) {
                    if kill(pid, 0) == 0 {
                        kill(pid, SIGKILL)
                    }
                }
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Managers/PortForwardProcessManager+Execution.swift`
```
import Foundation

extension PortForwardProcessManager {
    /// Starts a kubectl port-forward process.
    func startPortForward(
        id: UUID,
        namespace: String,
        service: String,
        localPort: Int,
        remotePort: Int
    ) async throws -> Process {
        guard let kubectlPath = DependencyChecker.shared.kubectlPath else {
            throw KubectlError.kubectlNotFound
        }

        let process = Process()
        process.executableURL = URL(fileURLWithPath: kubectlPath)
        process.arguments = [
            "port-forward",
            "-n", namespace,
            "svc/\(service)",
            "\(localPort):\(remotePort)",
            "--address=127.0.0.1"
        ]

        let pipe = Pipe()
        process.standardOutput = pipe
        process.standardError = pipe

        outputTasks[id]?[.portForward]?.cancel()
        if let existing = processes[id]?[.portForward], existing.isRunning {
            existing.terminate()
        }

        try process.run()

        if processes[id] == nil {
            processes[id] = [:]
        }
        processes[id]?[.portForward] = process

        startReadingOutput(pipe: pipe, id: id, type: .portForward)

        return process
    }

    /// Starts a standard socat proxy process.
    func startProxy(
        id: UUID,
        externalPort: Int,
        internalPort: Int
    ) async throws -> Process {
        guard let socatPath = DependencyChecker.shared.socatPath else {
            throw KubectlError.executionFailed("socat not found")
        }

        let process = Process()
        process.executableURL = URL(fileURLWithPath: socatPath)
        process.arguments = [
            "TCP-LISTEN:\(externalPort),fork,reuseaddr",
            "TCP:127.0.0.1:\(internalPort)"
        ]

        let pipe = Pipe()
        process.standardOutput = pipe
        process.standardError = pipe

        outputTasks[id]?[.proxy]?.cancel()
        if let existing = processes[id]?[.proxy], existing.isRunning {
            existing.terminate()
        }

        try process.run()

        if processes[id] == nil {
            processes[id] = [:]
        }
        processes[id]?[.proxy] = process

        startReadingOutput(pipe: pipe, id: id, type: .proxy)

        return process
    }

    /// Starts a direct exec proxy for multi-connection support.
    func startDirectExecProxy(
        id: UUID,
        namespace: String,
        service: String,
        externalPort: Int,
        remotePort: Int
    ) async throws -> Process {
        guard let kubectlPath = DependencyChecker.shared.kubectlPath else {
            throw KubectlError.kubectlNotFound
        }

        guard let socatPath = DependencyChecker.shared.socatPath else {
            throw KubectlError.executionFailed("socat not found for multi-connection mode")
        }

        let wrapperScript = createWrapperScript(
            kubectlPath: kubectlPath,
            socatPath: socatPath,
            namespace: namespace,
            service: service,
            remotePort: remotePort
        )

        let scriptPath = "/tmp/pf-wrapper-\(id.uuidString).sh"
        try wrapperScript.write(toFile: scriptPath, atomically: true, encoding: .utf8)

        let chmod = Process()
        chmod.executableURL = URL(fileURLWithPath: "/bin/chmod")
        chmod.arguments = ["+x", scriptPath]
        try chmod.run()
        chmod.waitUntilExit()

        let process = Process()
        process.executableURL = URL(fileURLWithPath: socatPath)
        process.arguments = [
            "TCP-LISTEN:\(externalPort),fork,reuseaddr",
            "EXEC:\(scriptPath)"
        ]

        let pipe = Pipe()
        process.standardOutput = pipe
        process.standardError = pipe

        outputTasks[id]?[.proxy]?.cancel()
        if let existing = processes[id]?[.proxy], existing.isRunning {
            existing.terminate()
        }

        try process.run()

        if processes[id] == nil {
            processes[id] = [:]
        }
        processes[id]?[.proxy] = process

        startReadingOutput(pipe: pipe, id: id, type: .proxy)

        return process
    }

    /// Creates a bash wrapper script for multi-connection proxy.
    func createWrapperScript(
        kubectlPath: String,
        socatPath: String,
        namespace: String,
        service: String,
        remotePort: Int
    ) -> String {
        """
        #!/bin/bash
        PORT=$((30000 + ($$ % 30000)))
        while /usr/bin/nc -z 127.0.0.1 $PORT 2>/dev/null; do
            PORT=$((PORT + 1))
        done
        \(kubectlPath) port-forward -n \(namespace) svc/\(service) $PORT:\(remotePort) --address=127.0.0.1 >/dev/null 2>&1 &
        KPID=$!
        trap "kill $KPID 2>/dev/null" EXIT
        for i in 1 2 3 4 5 6 7 8 9 10; do
            if /usr/bin/nc -z 127.0.0.1 $PORT 2>/dev/null; then break; fi
            sleep 0.5
        done
        \(socatPath) - TCP:127.0.0.1:$PORT
        """
    }
}
```

## File: `platforms/macos/Sources/Managers/PortForwardProcessManager+Kubernetes.swift`
```
import Foundation

// MARK: - Thread-safe Data Accumulator

/// Thread-safe container for accumulating Data from concurrent sources
private final class DataAccumulator: @unchecked Sendable {
    private var data = Data()
    private let lock = NSLock()

    func append(_ newData: Data) {
        lock.lock()
        defer { lock.unlock() }
        data.append(newData)
    }

    var value: Data {
        lock.lock()
        defer { lock.unlock() }
        return data
    }
}

extension PortForwardProcessManager {
    /// Fetches all Kubernetes namespaces.
    func fetchNamespaces() async throws -> [KubernetesNamespace] {
        let output = try await executeKubectl(arguments: ["get", "namespaces", "-o", "json"])

        do {
            let response = try JSONDecoder().decode(
                KubernetesNamespace.ListResponse.self,
                from: Data(output.utf8)
            )
            let namespaces = KubernetesNamespace.from(response: response)
            return namespaces.sorted { $0.name < $1.name }
        } catch {
            throw KubectlError.parsingFailed(error.localizedDescription)
        }
    }

    /// Fetches services in a specific namespace.
    func fetchServices(namespace: String) async throws -> [KubernetesService] {
        let output = try await executeKubectl(arguments: ["get", "services", "-n", namespace, "-o", "json"])

        do {
            let response = try JSONDecoder().decode(
                KubernetesService.ListResponse.self,
                from: Data(output.utf8)
            )
            let services = KubernetesService.from(response: response)
            return services.sorted { $0.name < $1.name }
        } catch {
            throw KubectlError.parsingFailed(error.localizedDescription)
        }
    }

    /// Executes a kubectl command and returns the output.
    nonisolated func executeKubectl(arguments: [String]) async throws -> String {
        guard let kubectlPath = DependencyChecker.shared.kubectlPath else {
            throw KubectlError.kubectlNotFound
        }

        return try await withCheckedThrowingContinuation { continuation in
            DispatchQueue.global(qos: .userInitiated).async {
                let process = Process()
                process.executableURL = URL(fileURLWithPath: kubectlPath)
                process.arguments = arguments

                let outputPipe = Pipe()
                let errorPipe = Pipe()
                process.standardOutput = outputPipe
                process.standardError = errorPipe

                // Thread-safe accumulators for concurrent data collection
                let outputAccumulator = DataAccumulator()
                let errorAccumulator = DataAccumulator()

                // Use autoreleasepool in handlers - background queues don't auto-drain
                outputPipe.fileHandleForReading.readabilityHandler = { handle in
                    autoreleasepool {
                        let data = handle.availableData
                        if !data.isEmpty {
                            outputAccumulator.append(data)
                        }
                    }
                }

                errorPipe.fileHandleForReading.readabilityHandler = { handle in
                    autoreleasepool {
                        let data = handle.availableData
                        if !data.isEmpty {
                            errorAccumulator.append(data)
                        }
                    }
                }

                do {
                    try process.run()
                    process.waitUntilExit()

                    outputPipe.fileHandleForReading.readabilityHandler = nil
                    errorPipe.fileHandleForReading.readabilityHandler = nil

                    // Use autoreleasepool for final reads
                    autoreleasepool {
                        let remainingOutput = outputPipe.fileHandleForReading.readDataToEndOfFile()
                        let remainingError = errorPipe.fileHandleForReading.readDataToEndOfFile()
                        outputAccumulator.append(remainingOutput)
                        errorAccumulator.append(remainingError)
                    }

                    let output = String(data: outputAccumulator.value, encoding: .utf8) ?? ""
                    let errorOutput = String(data: errorAccumulator.value, encoding: .utf8) ?? ""

                    if process.terminationStatus != 0 {
                        if errorOutput.contains("Unable to connect") ||
                           errorOutput.contains("connection refused") ||
                           errorOutput.contains("no configuration") ||
                           errorOutput.contains("dial tcp") {
                            continuation.resume(throwing: KubectlError.clusterNotConnected)
                        } else {
                            continuation.resume(throwing: KubectlError.executionFailed(
                                errorOutput.isEmpty ? "Unknown error" : errorOutput.trimmingCharacters(in: .whitespacesAndNewlines)
                            ))
                        }
                    } else {
                        continuation.resume(returning: output)
                    }
                } catch {
                    outputPipe.fileHandleForReading.readabilityHandler = nil
                    errorPipe.fileHandleForReading.readabilityHandler = nil
                    continuation.resume(throwing: error)
                }
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Managers/PortForwardProcessManager.swift`
```
import Foundation
import Darwin

// MARK: - Process Manager Actor

actor PortForwardProcessManager {
    // MARK: - Internal Properties (for extensions)

    var processes: [UUID: [PortForwardProcessType: Process]] = [:]
    var outputTasks: [UUID: [PortForwardProcessType: Task<Void, Never>]] = [:]
    var connectionErrors: [UUID: Date] = [:]
    var logHandlers: [UUID: LogHandler] = [:]
    var portConflictHandlers: [UUID: PortConflictHandler] = [:]

    // MARK: - Handler Management

    func setLogHandler(for id: UUID, handler: @escaping LogHandler) {
        logHandlers[id] = handler
    }

    func removeLogHandler(for id: UUID) {
        logHandlers.removeValue(forKey: id)
    }

    func setPortConflictHandler(for id: UUID, handler: @escaping PortConflictHandler) {
        portConflictHandlers[id] = handler
    }

    func removePortConflictHandler(for id: UUID) {
        portConflictHandlers.removeValue(forKey: id)
    }

    // MARK: - Output Reading

    func startReadingOutput(pipe: Pipe, id: UUID, type: PortForwardProcessType) {
        outputTasks[id]?[type]?.cancel()

        let task = Task { [weak self] in
            let handle = pipe.fileHandleForReading

            // Use async bytes stream for non-blocking read
            // This avoids potential deadlock from blocking availableData calls
            do {
                for try await line in handle.bytes.lines {
                    guard !Task.isCancelled else { break }

                    let trimmedLine = line.trimmingCharacters(in: .whitespacesAndNewlines)
                    guard !trimmedLine.isEmpty else { continue }

                    let isError = PortForwardOutputParser.isErrorLine(trimmedLine)

                    if isError {
                        await self?.markConnectionError(id: id)
                    }

                    if let port = PortForwardOutputParser.detectPortConflict(in: trimmedLine) {
                        if let handler = await self?.portConflictHandlers[id] {
                            handler(port)
                        }
                    }

                    if let handler = await self?.logHandlers[id] {
                        handler(trimmedLine, type, isError)
                    }
                }
            } catch {
                // Stream ended or was cancelled - this is expected when process terminates
            }
        }

        if outputTasks[id] == nil {
            outputTasks[id] = [:]
        }
        outputTasks[id]?[type] = task
    }

    // MARK: - Error Tracking

    func markConnectionError(id: UUID) {
        connectionErrors[id] = Date()
    }

    func hasRecentError(for id: UUID, within seconds: TimeInterval = 10) -> Bool {
        guard let errorTime = connectionErrors[id] else { return false }
        return Date().timeIntervalSince(errorTime) < seconds
    }

    func clearError(for id: UUID) {
        connectionErrors.removeValue(forKey: id)
    }

    // MARK: - Process Lifecycle

    func killProcesses(for id: UUID) {
        if let tasks = outputTasks[id] {
            for (_, task) in tasks {
                task.cancel()
            }
        }
        outputTasks[id] = nil

        guard let procs = processes[id] else { return }

        for (_, process) in procs {
            if process.isRunning {
                process.terminate()
            }
        }
        processes[id] = nil
        connectionErrors.removeValue(forKey: id)

        let scriptPath = "/tmp/pf-wrapper-\(id.uuidString).sh"
        try? FileManager.default.removeItem(atPath: scriptPath)
    }

    func isProcessRunning(for id: UUID, type: PortForwardProcessType) -> Bool {
        processes[id]?[type]?.isRunning ?? false
    }

    func isPortOpen(port: Int) -> Bool {
        PortHealthChecker.isPortOpen(port: port)
    }

    func killAllPortForwarderProcesses() async {
        let pkillKubectl = Process()
        pkillKubectl.executableURL = URL(fileURLWithPath: "/usr/bin/pkill")
        pkillKubectl.arguments = ["-9", "-f", "kubectl.*port-forward"]
        try? pkillKubectl.run()
        pkillKubectl.waitUntilExit()

        let pkillSocat = Process()
        pkillSocat.executableURL = URL(fileURLWithPath: "/usr/bin/pkill")
        pkillSocat.arguments = ["-9", "-f", "socat.*TCP-LISTEN"]
        try? pkillSocat.run()
        pkillSocat.waitUntilExit()

        try? await Task.sleep(for: .milliseconds(500))

        processes.removeAll()
        for (_, tasks) in outputTasks {
            for (_, task) in tasks { task.cancel() }
        }
        outputTasks.removeAll()
        connectionErrors.removeAll()
        logHandlers.removeAll()
        portConflictHandlers.removeAll()
    }
}
```

## File: `platforms/macos/Sources/Managers/SponsorManager.swift`
```
import Foundation
import SwiftUI
import Defaults

@Observable
@MainActor
final class SponsorManager {
    // MARK: - State
    var sponsors: [Sponsor] = []
    var contributors: [Contributor] = []
    var isLoading = false
    var error: Error?
    var shouldShowWindow = false

    // MARK: - Private
    private let service = SponsorsService()
    private var hasCheckedOnLaunch = false

    // MARK: - Init
    init() {
        loadCachedSponsors()
    }

    // MARK: - Public Methods

    /// Check if sponsors window should be shown (called on app launch)
    func checkAndShowIfNeeded() {
        guard !hasCheckedOnLaunch else { return }
        hasCheckedOnLaunch = true

        let interval = Defaults[.sponsorDisplayInterval]
        guard let days = interval.days else { return }

        let lastShown = Defaults[.lastSponsorWindowShown]
        let shouldShow: Bool

        if let lastShown {
            let daysSinceLastShown = Calendar.current.dateComponents(
                [.day],
                from: lastShown,
                to: Date()
            ).day ?? 0
            shouldShow = daysSinceLastShown >= days
        } else {
            shouldShow = true
        }

        if shouldShow {
            shouldShowWindow = true
        }

        // Refresh sponsors in background if cache is stale
        if Defaults[.sponsorCache]?.isStale ?? true {
            Task { @MainActor in
                await self.refreshSponsors()
            }
        }
    }

    /// Mark that sponsors window was shown
    func markWindowShown() {
        Defaults[.lastSponsorWindowShown] = Date()
        shouldShowWindow = false
    }

    /// Force show sponsors window (e.g., from Settings)
    func showSponsorsWindow() {
        shouldShowWindow = true
    }

    /// Refresh sponsors from API
    func refreshSponsors() async {
        isLoading = true
        error = nil

        do {
            async let fetchedSponsors = service.fetchSponsors()
            async let fetchedContributors = service.fetchContributors()
            
            let (sponsors, contributors) = try await (fetchedSponsors, fetchedContributors)
            
            // Filter out bots
            let validContributors = contributors.filter { !$0.login.lowercased().contains("[bot]") }
            
            print("Fetched \(sponsors.count) sponsors and \(validContributors.count) contributors")
            
            self.sponsors = sponsors
            self.contributors = validContributors

            Defaults[.sponsorCache] = SponsorCache(
                sponsors: sponsors,
                contributors: validContributors,
                fetchedAt: Date()
            )
        } catch {
            print("Failed to fetch sponsors/contributors: \(error)")
            self.error = error
        }

        isLoading = false
    }

    // MARK: - Private Methods

    private func loadCachedSponsors() {
        if let cache = Defaults[.sponsorCache] {
            sponsors = cache.sponsors
            // Filter cached contributors too, just in case
            contributors = cache.contributors.filter { !$0.login.lowercased().contains("[bot]") }
        }
    }
}
```

## File: `platforms/macos/Sources/Managers/TunnelManager.swift`
```
import Foundation
import AppKit

// MARK: - Tunnel Manager

/// Manages Cloudflare Quick Tunnel connections
/// Coordinates between TunnelState (UI) and CloudflaredService (process management)
@Observable
@MainActor
final class TunnelManager {
    /// Observable state for UI (extracted)
    let state: TunnelState

    /// The cloudflared service actor
    let cloudflaredService: CloudflaredService

    /// Task for cleaning up orphaned tunnels from previous sessions
    @ObservationIgnored private var cleanupTask: Task<Void, Never>?

    // MARK: - Backward Compatibility Accessors

    /// Active tunnel states (delegates to state)
    var tunnels: [CloudflareTunnelState] {
        get { state.tunnels }
        set { state.tunnels = newValue }
    }

    /// Number of currently active tunnels
    var activeTunnelCount: Int {
        state.activeTunnelCount
    }

    /// Cached installation status
    var isCloudflaredInstalled: Bool {
        state.isCloudflaredInstalled
    }

    // MARK: - Initialization

    init(
        state: TunnelState = TunnelState(),
        cloudflaredService: CloudflaredService = CloudflaredService()
    ) {
        self.state = state
        self.cloudflaredService = cloudflaredService

        // Check initial installation status
        state.setInstalled(cloudflaredService.isInstalled)

        // Clean up any orphaned tunnel processes from previous crashed sessions
        cleanupTask = Task {
            await cleanupOrphanedTunnels()
        }
    }

    /// Re-check cloudflared installation status (call after user installs)
    func recheckInstallation() {
        state.setInstalled(cloudflaredService.isInstalled)
    }

    /// Kill any stray cloudflared tunnel processes from previous sessions
    private func cleanupOrphanedTunnels() async {
        let process = Process()
        process.executableURL = URL(fileURLWithPath: "/usr/bin/pkill")
        process.arguments = ["-9", "-f", "cloudflared.*tunnel.*--url"]
        process.standardOutput = FileHandle.nullDevice
        process.standardError = FileHandle.nullDevice

        do {
            try process.run()
            process.waitUntilExit()
        } catch {
            // Ignore errors - process may not exist
        }
    }

    // MARK: - Tunnel Operations

    /// Start a tunnel for the specified port
    func startTunnel(for port: Int, portInfoId: String? = nil) {
        Task {
            await cleanupTask?.value
            await _startTunnelImpl(for: port, portInfoId: portInfoId)
        }
    }

    /// Internal implementation of startTunnel after cleanup is complete
    private func _startTunnelImpl(for port: Int, portInfoId: String? = nil) async {
        // Check if tunnel already exists for this port
        if let existing = state.tunnel(for: port) {
            if existing.status != .error {
                if let url = existing.tunnelURL {
                    ClipboardService.copy(url)
                }
                return
            }
            // Prevent accumulating stale error entries for repeated retries.
            state.removeTunnel(id: existing.id)
        }

        let tunnelState = CloudflareTunnelState(port: port, portInfoId: portInfoId)
        state.addTunnel(tunnelState)
        tunnelState.status = .starting

        Task { [weak self, weak tunnelState] in
            guard let self = self, let tunnelState = tunnelState else { return }

            // Set URL handler with proper weak capture in inner Task
            let urlHandler: @Sendable (String) -> Void = { [weak self, weak tunnelState] url in
                guard let tunnelState = tunnelState else { return }
                Task { @MainActor [weak self, weak tunnelState] in
                    guard let tunnelState = tunnelState else { return }
                    tunnelState.tunnelURL = url
                    tunnelState.status = .active
                    tunnelState.startTime = Date()
                    ClipboardService.copy(url)
                    NotificationService.shared.notify(
                        title: "Tunnel Active",
                        body: "Port \(tunnelState.port) available at \(self?.shortenedURL(url) ?? url)"
                    )
                }
            }
            await self.cloudflaredService.setURLHandler(for: tunnelState.id, handler: urlHandler)

            // Set error handler with proper weak capture in inner Task
            let errorHandler: @Sendable (String) -> Void = { [weak tunnelState] error in
                guard let tunnelState = tunnelState else { return }
                Task { @MainActor [weak tunnelState] in
                    guard let tunnelState = tunnelState else { return }
                    tunnelState.lastError = error
                    if tunnelState.status != .active {
                        tunnelState.status = .error
                    }
                }
            }
            await self.cloudflaredService.setErrorHandler(for: tunnelState.id, handler: errorHandler)

            // Set log handler to capture all output lines
            let logHandler: @Sendable (String) -> Void = { [weak tunnelState] line in
                guard let tunnelState = tunnelState else { return }
                let entry = TunnelLogEntry.parse(line)
                Task { @MainActor [weak tunnelState] in
                    tunnelState?.addLogEntry(entry)
                }
            }
            await self.cloudflaredService.setLogHandler(for: tunnelState.id, handler: logHandler)

            do {
                let process = try await self.cloudflaredService.startTunnel(id: tunnelState.id, port: port)
                try? await Task.sleep(for: .seconds(3))

                if !process.isRunning && tunnelState.status != .active {
                    // Clean up handlers when process terminates unexpectedly
                    await self.cloudflaredService.removeHandlers(for: tunnelState.id)
                    await MainActor.run {
                        tunnelState.status = .error
                        tunnelState.lastError = "Process terminated unexpectedly"
                    }
                }
            } catch {
                // Clean up handlers on error
                await self.cloudflaredService.removeHandlers(for: tunnelState.id)
                await MainActor.run {
                    tunnelState.status = .error
                    tunnelState.lastError = error.localizedDescription
                }
            }
        }
    }

    /// Stop the tunnel for the specified port
    func stopTunnel(for port: Int) {
        guard let tunnel = state.tunnel(for: port) else { return }
        stopTunnel(id: tunnel.id)
    }

    /// Stop a tunnel by its ID
    func stopTunnel(id: UUID) {
        guard let tunnel = tunnels.first(where: { $0.id == id }) else { return }
        tunnel.status = .stopping

        Task {
            await cloudflaredService.stopTunnel(id: id)
            await MainActor.run {
                state.removeTunnel(id: id)
            }
        }
    }

    /// Stop all active tunnels
    func stopAllTunnels() async {
        for tunnel in tunnels {
            tunnel.status = .stopping
        }
        await cloudflaredService.stopAllTunnels()
        state.removeAllTunnels()
    }

    /// Get the tunnel state for a port
    func tunnelState(for port: Int) -> CloudflareTunnelState? {
        state.tunnel(for: port)
    }

    /// Check if a port has an active tunnel
    func hasTunnel(for port: Int) -> Bool {
        state.hasTunnel(for: port)
    }

    /// Copy the tunnel URL for a port to clipboard
    func copyURL(for port: Int) {
        guard let tunnel = state.tunnel(for: port),
              let url = tunnel.tunnelURL else { return }
        ClipboardService.copy(url)
    }

    /// Open the tunnel URL in browser
    func openURL(for port: Int) {
        guard let tunnel = state.tunnel(for: port),
              let urlString = tunnel.tunnelURL,
              let url = URL(string: urlString) else { return }
        NSWorkspace.shared.open(url)
    }

    // MARK: - Helpers

    private func shortenedURL(_ url: String) -> String {
        url.replacingOccurrences(of: "https://", with: "")
    }
}
```

## File: `platforms/macos/Sources/Managers/TunnelState.swift`
```
/**
 * TunnelState.swift
 * PortKiller
 *
 * Pure UI state for Cloudflare tunnels.
 * Extracted from TunnelManager for separation of concerns.
 */

import Foundation

/// Observable state for Cloudflare tunnels
@Observable
@MainActor
final class TunnelState {
    /// Active tunnel states
    var tunnels: [CloudflareTunnelState] = []

    /// Cached installation status
    private(set) var isCloudflaredInstalled: Bool = false

    /// Number of currently active tunnels
    var activeTunnelCount: Int {
        tunnels.filter { $0.status == .active }.count
    }

    /// Update installation status
    func setInstalled(_ installed: Bool) {
        isCloudflaredInstalled = installed
    }

    /// Add a new tunnel state
    func addTunnel(_ tunnel: CloudflareTunnelState) {
        tunnels.append(tunnel)
    }

    /// Remove tunnel by ID
    func removeTunnel(id: UUID) {
        tunnels.removeAll { $0.id == id }
    }

    /// Remove all tunnels
    func removeAllTunnels() {
        tunnels.removeAll()
    }

    /// Get tunnel for a specific port
    func tunnel(for port: Int) -> CloudflareTunnelState? {
        tunnels.first { $0.port == port }
    }

    /// Check if port has a non-error tunnel
    func hasTunnel(for port: Int) -> Bool {
        tunnels.contains { $0.port == port && $0.status != .error }
    }
}
```

## File: `platforms/macos/Sources/Managers/UpdateManager.swift`
```
import Foundation
import Sparkle
import AppKit
import Observation
import Combine

/**
 * UpdateManager handles automatic updates using the Sparkle framework.
 *
 * Key features:
 * - Demand-driven initialization (does not preload on launch)
 * - Only initializes when running from .app bundle (not during development)
 * - Activates app before showing update UI (important for menu bar apps)
 * - Tracks update availability and last check date
 *
 * This class uses the @Observable macro for SwiftUI reactivity and is
 * marked with @MainActor to ensure all UI updates happen on the main thread.
 */
@Observable
@MainActor
final class UpdateManager {
    // MARK: - Public Properties

    /// Whether the updater is ready to check for updates
    /// Default to true in app bundles so menu command stays enabled before initialization.
    var canCheckForUpdates = Bundle.main.bundlePath.hasSuffix(".app")

    /// Timestamp of the last update check
    var lastUpdateCheckDate: Date?

    // MARK: - Private Properties

    /// Sparkle updater controller instance
    private var updaterController: SPUStandardUpdaterController?

    /// Tracks whether Sparkle has been initialized
    private var isInitialized = false

    /// Check if running from a proper app bundle (not swift run)
    private static var isRunningFromBundle: Bool {
        Bundle.main.bundlePath.hasSuffix(".app")
    }

    // MARK: - Computed Properties

    /**
     * Whether to automatically check for updates on launch.
     * Setting this value will trigger Sparkle initialization if needed.
     */
    var automaticallyChecksForUpdates: Bool {
        get { updaterController?.updater.automaticallyChecksForUpdates ?? false }
        set {
            ensureInitialized()
            updaterController?.updater.automaticallyChecksForUpdates = newValue
        }
    }

    /**
     * Whether to automatically download updates in the background.
     * Setting this value will trigger Sparkle initialization if needed.
     */
    var automaticallyDownloadsUpdates: Bool {
        get { updaterController?.updater.automaticallyDownloadsUpdates ?? false }
        set {
            ensureInitialized()
            updaterController?.updater.automaticallyDownloadsUpdates = newValue
        }
    }

    // MARK: - Initialization

    /// Initializes the update manager in a cold state.
    /// Sparkle is initialized only when an update API is actually used.
    init() {}

    // MARK: - Private Methods

    /**
     * Ensures Sparkle is initialized before use.
     * This is called automatically when needed and is safe to call multiple times.
     * Skips initialization when not running from an .app bundle (development mode).
     */
    private func ensureInitialized() {
        guard !isInitialized else { return }
        isInitialized = true

        guard Self.isRunningFromBundle else {
            return
        }

        let controller = SPUStandardUpdaterController(
            startingUpdater: true,
            updaterDelegate: nil,
            userDriverDelegate: nil
        )
        updaterController = controller
        canCheckForUpdates = controller.updater.canCheckForUpdates
        lastUpdateCheckDate = controller.updater.lastUpdateCheckDate

        // Observe Sparkle properties and update our @Observable properties
        controller.updater.publisher(for: \.canCheckForUpdates)
            .sink { [weak self] value in
                self?.canCheckForUpdates = value
            }
            .store(in: &cancellables)

        controller.updater.publisher(for: \.lastUpdateCheckDate)
            .sink { [weak self] value in
                self?.lastUpdateCheckDate = value
            }
            .store(in: &cancellables)
    }

    /// Storage for Combine cancellables.
    /// Note: These subscriptions live for the app's lifetime alongside the UpdateManager,
    /// so cleanup in deinit is not necessary. The subscriptions are intentionally retained.
    @ObservationIgnored private var cancellables = Set<AnyCancellable>()

    // MARK: - Public Methods

    /**
     * Manually checks for updates.
     * Activates the app and brings the update window to the front.
     * This is important for menu bar apps that don't normally have visible windows.
     */
    func checkForUpdates() {
        ensureInitialized()
        guard let controller = updaterController else { return }
        // Activate app to ensure Sparkle window appears in front
        NSApp.activate(ignoringOtherApps: true)
        controller.checkForUpdates(nil)
    }
}
```

## File: `platforms/macos/Sources/Models/AutoKillRule.swift`
```
import Foundation
import Defaults

/// A rule that automatically kills processes matching certain criteria after a timeout.
struct AutoKillRule: Codable, Identifiable, Hashable, Sendable, Defaults.Serializable {
    var id: UUID
    /// Display name for the rule
    var name: String
    /// Process name pattern (supports * wildcard, e.g. "node*"). Empty means match any.
    var processPattern: String
    /// Specific port to match. 0 means match any port.
    var port: Int
    /// Minutes after which the process should be killed
    var timeoutMinutes: Int
    /// Whether to notify before killing
    var notifyBeforeKill: Bool
    /// Whether this rule is active
    var isEnabled: Bool

    init(
        id: UUID = UUID(),
        name: String = "",
        processPattern: String = "",
        port: Int = 0,
        timeoutMinutes: Int = 30,
        notifyBeforeKill: Bool = true,
        isEnabled: Bool = true
    ) {
        self.id = id
        self.name = name
        self.processPattern = processPattern
        self.port = port
        self.timeoutMinutes = timeoutMinutes
        self.notifyBeforeKill = notifyBeforeKill
        self.isEnabled = isEnabled
    }

    /// Checks if this rule matches a given port info.
    func matches(_ portInfo: PortInfo) -> Bool {
        // Check port match
        if port > 0 && portInfo.port != port { return false }

        // Check process pattern match
        if !processPattern.isEmpty {
            return matchesGlob(portInfo.processName, pattern: processPattern)
        }

        // At least one criterion must be specified
        return port > 0
    }

    /// Simple glob matching with * wildcard support.
    private func matchesGlob(_ string: String, pattern: String) -> Bool {
        let lowered = string.lowercased()
        let pat = pattern.lowercased()

        if !pat.contains("*") {
            return lowered == pat
        }

        let parts = pat.split(separator: "*", omittingEmptySubsequences: false).map(String.init)

        if parts.count == 1 { return lowered == pat }

        // Check prefix
        if let first = parts.first, !first.isEmpty, !lowered.hasPrefix(first) {
            return false
        }
        // Check suffix
        if let last = parts.last, !last.isEmpty, !lowered.hasSuffix(last) {
            return false
        }

        // Check all parts appear in order
        var searchStart = lowered.startIndex
        for part in parts where !part.isEmpty {
            guard let range = lowered.range(of: part, range: searchStart..<lowered.endIndex) else {
                return false
            }
            searchStart = range.upperBound
        }
        return true
    }
}
```

## File: `platforms/macos/Sources/Models/CloudflaredProtocol.swift`
```
import Defaults
import Foundation

/// Supported transport protocols for cloudflared quick tunnels.
enum CloudflaredProtocol: String, CaseIterable, Codable, Defaults.Serializable, Sendable {
    case http2 = "http2"
    case quic = "quic"

    var displayName: String {
        switch self {
        case .http2: return "HTTP/2"
        case .quic: return "QUIC"
        }
    }
}
```

## File: `platforms/macos/Sources/Models/CloudflareTunnel.swift`
```
import Foundation

// MARK: - Tunnel Status

/// Status of a Cloudflare tunnel
enum CloudflareTunnelStatus: String, Sendable {
    case idle = "Idle"
    case starting = "Starting..."
    case active = "Active"
    case stopping = "Stopping..."
    case error = "Error"

    var icon: String {
        switch self {
        case .idle: "circle"
        case .starting: "circle.dotted"
        case .active: "circle.fill"
        case .stopping: "circle.dotted"
        case .error: "exclamationmark.circle.fill"
        }
    }
}

// MARK: - Tunnel State

/// Runtime state for a Cloudflare Quick Tunnel (ephemeral - not persisted)
@Observable
@MainActor
final class CloudflareTunnelState: Identifiable, Sendable {
    let id: UUID
    let port: Int
    let portInfoId: String?
    var status: CloudflareTunnelStatus = .idle
    var tunnelURL: String?
    var lastError: String?
    var startTime: Date?
    var logs: [TunnelLogEntry] = []

    /// Maximum number of log entries to keep per tunnel
    private static let maxLogEntries = 500

    /// Adds a log entry, keeping the buffer bounded
    func addLogEntry(_ entry: TunnelLogEntry) {
        logs.append(entry)
        if logs.count > Self.maxLogEntries {
            logs.removeFirst(logs.count - Self.maxLogEntries)
        }
    }

    /// Clears all log entries
    func clearLogs() {
        logs.removeAll()
    }

    init(id: UUID = UUID(), port: Int, portInfoId: String? = nil) {
        self.id = id
        self.port = port
        self.portInfoId = portInfoId
    }
}

extension CloudflareTunnelState: Hashable {
    nonisolated func hash(into hasher: inout Hasher) {
        hasher.combine(id)
    }

    nonisolated static func == (lhs: CloudflareTunnelState, rhs: CloudflareTunnelState) -> Bool {
        lhs.id == rhs.id
    }
}
```

## File: `platforms/macos/Sources/Models/Errors.swift`
```
/**
 * Errors.swift
 * PortKiller
 *
 * Defines error types for the PortKiller application.
 * All errors conform to LocalizedError to provide user-friendly messages.
 */

import Foundation

/// Application-specific error types
///
/// PortKillerError defines all possible error conditions that can occur
/// during port scanning, process killing, and permission checks. Each error
/// provides localized, user-friendly descriptions suitable for display in alerts.
enum PortKillerError: Error, LocalizedError {
    /// Port scanning operation failed
    case scanFailed(String)

    /// Failed to kill a process
    case killFailed(pid: Int, reason: String)

    /// Required system permission is denied
    case permissionDenied

    /// Network or system operation error
    case networkError(String)

    /// User-friendly error description
    var errorDescription: String? {
        switch self {
        case .scanFailed(let reason):
            return "Failed to scan ports: \(reason)"
        case .killFailed(let pid, let reason):
            return "Failed to kill process \(pid): \(reason)"
        case .permissionDenied:
            return "Permission denied. PortKiller requires accessibility permissions to manage processes."
        case .networkError(let reason):
            return "Network error: \(reason)"
        }
    }

    /// Detailed failure reason
    var failureReason: String? {
        switch self {
        case .scanFailed:
            return "The port scanning operation could not complete successfully."
        case .killFailed:
            return "The process termination request was denied or failed."
        case .permissionDenied:
            return "PortKiller does not have the necessary system permissions."
        case .networkError:
            return "A network or system-level error occurred."
        }
    }

    /// Suggested recovery action
    var recoverySuggestion: String? {
        switch self {
        case .scanFailed:
            return "Try refreshing the port list or restarting PortKiller."
        case .killFailed:
            return "The process may require elevated privileges. Try running 'sudo kill -9 \(pid)' in Terminal."
        case .permissionDenied:
            return "Go to System Settings > Privacy & Security > Accessibility and enable PortKiller."
        case .networkError:
            return "Check your network connection and try again."
        }
    }

    /// PID involved in the error (if applicable)
    private var pid: Int {
        switch self {
        case .killFailed(let pid, _):
            return pid
        default:
            return 0
        }
    }
}
```

## File: `platforms/macos/Sources/Models/KubernetesModels.swift`
```
import Foundation

// MARK: - Namespace

struct KubernetesNamespace: Identifiable, Codable, Sendable, Hashable {
    let name: String
    let isCustom: Bool

    var id: String { name }

    init(name: String, isCustom: Bool = false) {
        self.name = name
        self.isCustom = isCustom
    }
}

// MARK: - Service

struct KubernetesService: Identifiable, Codable, Sendable, Hashable {
    let name: String
    let namespace: String
    let type: String
    let clusterIP: String?
    let ports: [ServicePort]

    var id: String { "\(namespace)/\(name)" }

    struct ServicePort: Codable, Sendable, Hashable, Identifiable {
        let name: String?
        let port: Int
        let targetPort: Int
        let `protocol`: String?

        var id: Int { port }

        var displayName: String {
            if let name = name, !name.isEmpty {
                return "\(String(port)) (\(name))"
            }
            return String(port)
        }
    }
}

// MARK: - kubectl JSON Response Parsing

extension KubernetesNamespace {
    struct ListResponse: Codable {
        let items: [Item]

        struct Item: Codable {
            let metadata: Metadata

            struct Metadata: Codable {
                let name: String
            }
        }
    }

    static func from(response: ListResponse) -> [KubernetesNamespace] {
        response.items.map { KubernetesNamespace(name: $0.metadata.name) }
    }
}

extension KubernetesService {
    struct ListResponse: Codable {
        let items: [Item]

        struct Item: Codable {
            let metadata: Metadata
            let spec: Spec

            struct Metadata: Codable {
                let name: String
                let namespace: String
            }

            struct Spec: Codable {
                let type: String?
                let clusterIP: String?
                let ports: [Port]?

                struct Port: Codable {
                    let name: String?
                    let port: Int
                    let targetPort: TargetPort?
                    let `protocol`: String?

                    // targetPort can be either Int or String in Kubernetes
                    enum TargetPort: Codable {
                        case int(Int)
                        case string(String)

                        init(from decoder: Decoder) throws {
                            let container = try decoder.singleValueContainer()
                            if let intValue = try? container.decode(Int.self) {
                                self = .int(intValue)
                            } else if let stringValue = try? container.decode(String.self) {
                                self = .string(stringValue)
                            } else {
                                throw DecodingError.dataCorruptedError(
                                    in: container,
                                    debugDescription: "Cannot decode targetPort"
                                )
                            }
                        }

                        func encode(to encoder: Encoder) throws {
                            var container = encoder.singleValueContainer()
                            switch self {
                            case .int(let value): try container.encode(value)
                            case .string(let value): try container.encode(value)
                            }
                        }

                        var intValue: Int? {
                            switch self {
                            case .int(let value): return value
                            case .string: return nil
                            }
                        }
                    }
                }
            }
        }
    }

    static func from(response: ListResponse) -> [KubernetesService] {
        response.items.map { item in
            KubernetesService(
                name: item.metadata.name,
                namespace: item.metadata.namespace,
                type: item.spec.type ?? "ClusterIP",
                clusterIP: item.spec.clusterIP,
                ports: item.spec.ports?.map { port in
                    ServicePort(
                        name: port.name,
                        port: port.port,
                        targetPort: port.targetPort?.intValue ?? port.port,
                        protocol: port.protocol
                    )
                } ?? []
            )
        }
    }
}
```

## File: `platforms/macos/Sources/Models/PortFilter.swift`
```
import Foundation

struct PortFilter: Equatable, Sendable {
    var searchText: String = ""
    var minPort: Int? = nil
    var maxPort: Int? = nil
    var processTypes: Set<ProcessType> = Set(ProcessType.allCases)
    var showOnlyFavorites: Bool = false
    var showOnlyWatched: Bool = false

    var isActive: Bool {
        !searchText.isEmpty ||
        minPort != nil ||
        maxPort != nil ||
        processTypes.count < ProcessType.allCases.count ||
        showOnlyFavorites ||
        showOnlyWatched
    }

    func matches(_ port: PortInfo, favorites: Set<Int>, watched: [WatchedPort]) -> Bool {
        // Search text filter
        if !searchText.isEmpty {
            let query = searchText.lowercased()
            let matches = port.processName.lowercased().contains(query) ||
                          String(port.port).contains(query) ||
                          String(port.pid).contains(query) ||
                          port.address.lowercased().contains(query) ||
                          port.user.lowercased().contains(query) ||
                          port.command.lowercased().contains(query)
            if !matches { return false }
        }

        // Port range filter
        if let min = minPort, port.port < min { return false }
        if let max = maxPort, port.port > max { return false }

        // Process type filter
        if !processTypes.contains(port.processType) { return false }

        // Favorites filter
        if showOnlyFavorites && !favorites.contains(port.port) { return false }

        // Watched filter
        if showOnlyWatched && !watched.contains(where: { $0.port == port.port }) { return false }

        return true
    }

    mutating func reset() {
        searchText = ""
        minPort = nil
        maxPort = nil
        processTypes = Set(ProcessType.allCases)
        showOnlyFavorites = false
        showOnlyWatched = false
    }
}

enum SidebarItem: Hashable, Identifiable, Sendable {
    case allPorts
    case favorites
    case watched
    case processType(ProcessType)
    case kubernetesPortForward
    case cloudflareTunnels
    case sponsors
    case settings

    var id: String {
        switch self {
        case .allPorts: return "all"
        case .favorites: return "favorites"
        case .watched: return "watched"
        case .processType(let type): return "type-\(type.rawValue)"
        case .kubernetesPortForward: return "k8s-port-forward"
        case .cloudflareTunnels: return "cloudflare-tunnels"
        case .sponsors: return "sponsors"
        case .settings: return "settings"
        }
    }

    var title: String {
        switch self {
        case .allPorts: return "All Ports"
        case .favorites: return "Favorites"
        case .watched: return "Watched"
        case .processType(let type): return type.rawValue
        case .kubernetesPortForward: return "K8s Port Forward"
        case .cloudflareTunnels: return "Cloudflare Tunnels"
        case .sponsors: return "Sponsors"
        case .settings: return "Settings"
        }
    }

    var icon: String {
        switch self {
        case .allPorts: return "list.bullet"
        case .favorites: return "star.fill"
        case .watched: return "eye.fill"
        case .processType(let type): return type.icon
        case .kubernetesPortForward: return "point.3.connected.trianglepath.dotted"
        case .cloudflareTunnels: return "cloud.fill"
        case .sponsors: return "heart.fill"
        case .settings: return "gear"
        }
    }
}
```

## File: `platforms/macos/Sources/Models/PortForwardConnection.swift`
```
import Foundation
import Defaults

// MARK: - Connection Configuration

/// Configuration for a Kubernetes port-forward connection
/// Persisted using Defaults library
struct PortForwardConnectionConfig: Identifiable, Codable, Equatable, Hashable, Sendable, Defaults.Serializable {
    let id: UUID
    var name: String
    var namespace: String
    var service: String
    var localPort: Int
    var remotePort: Int
    var proxyPort: Int?
    var isEnabled: Bool
    var autoReconnect: Bool
    /// Direct exec mode: Uses kubectl exec + socat for true multi-connection support
    var useDirectExec: Bool
    /// Notification settings
    var notifyOnConnect: Bool
    var notifyOnDisconnect: Bool

    init(
        id: UUID = UUID(),
        name: String,
        namespace: String,
        service: String,
        localPort: Int,
        remotePort: Int,
        proxyPort: Int? = nil,
        isEnabled: Bool = true,
        autoReconnect: Bool = true,
        useDirectExec: Bool = true,
        notifyOnConnect: Bool = true,
        notifyOnDisconnect: Bool = true
    ) {
        self.id = id
        self.name = name
        self.namespace = namespace
        self.service = service
        self.localPort = localPort
        self.remotePort = remotePort
        self.proxyPort = proxyPort
        self.isEnabled = isEnabled
        self.autoReconnect = autoReconnect
        self.useDirectExec = useDirectExec
        self.notifyOnConnect = notifyOnConnect
        self.notifyOnDisconnect = notifyOnDisconnect
    }

    // MARK: - Codable Migration
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)

        // Required fields
        id = try container.decode(UUID.self, forKey: .id)
        name = try container.decode(String.self, forKey: .name)
        namespace = try container.decode(String.self, forKey: .namespace)
        service = try container.decode(String.self, forKey: .service)
        localPort = try container.decode(Int.self, forKey: .localPort)
        remotePort = try container.decode(Int.self, forKey: .remotePort)
        proxyPort = try container.decodeIfPresent(Int.self, forKey: .proxyPort)
        isEnabled = try container.decode(Bool.self, forKey: .isEnabled)
        autoReconnect = try container.decode(Bool.self, forKey: .autoReconnect)
        useDirectExec = try container.decode(Bool.self, forKey: .useDirectExec)

        // New fields with defaults for migration
        notifyOnConnect = try container.decodeIfPresent(Bool.self, forKey: .notifyOnConnect) ?? true
        notifyOnDisconnect = try container.decodeIfPresent(Bool.self, forKey: .notifyOnDisconnect) ?? true
    }

    private enum CodingKeys: String, CodingKey {
        case id, name, namespace, service, localPort, remotePort, proxyPort
        case isEnabled, autoReconnect, useDirectExec
        case notifyOnConnect, notifyOnDisconnect
    }
}

// MARK: - Connection Status

enum PortForwardStatus: String, Sendable {
    case disconnected = "Disconnected"
    case connecting = "Connecting..."
    case connected = "Connected"
    case error = "Error"

    var icon: String {
        switch self {
        case .disconnected: "circle"
        case .connecting: "circle.dotted"
        case .connected: "circle.fill"
        case .error: "exclamationmark.circle.fill"
        }
    }

    var color: String {
        switch self {
        case .disconnected: "secondary"
        case .connecting: "yellow"
        case .connected: "green"
        case .error: "red"
        }
    }
}

// MARK: - Connection Runtime State

/// A single log entry for a port-forward connection
struct PortForwardLogEntry: Identifiable, Sendable {
    let id = UUID()
    let timestamp: Date
    let message: String
    let type: PortForwardProcessType
    let isError: Bool
}

/// Runtime state for a port-forward connection (not persisted)
@Observable
@MainActor
final class PortForwardConnectionState: Identifiable, Hashable {
    let id: UUID
    var config: PortForwardConnectionConfig
    var portForwardStatus: PortForwardStatus = .disconnected
    var proxyStatus: PortForwardStatus = .disconnected
    var portForwardTask: Task<Void, Never>?
    var proxyTask: Task<Void, Never>?
    var lastError: String?
    var logs: [PortForwardLogEntry] = []
    /// Tracks if the connection was stopped intentionally by the user (vs unexpected disconnect)
    var isIntentionallyStopped: Bool = false

    /// Maximum log entries to keep per connection (memory optimization)
    private static let maxLogEntries = 100

    func appendLog(_ message: String, type: PortForwardProcessType, isError: Bool = false) {
        let entry = PortForwardLogEntry(timestamp: Date(), message: message, type: type, isError: isError)
        logs.append(entry)
        // Keep only last N log entries to prevent memory accumulation
        if logs.count > Self.maxLogEntries {
            logs.removeFirst(logs.count - Self.maxLogEntries)
        }
    }

    func clearLogs() {
        logs.removeAll()
    }

    /// Whether the connection is fully established (port-forward + optional proxy)
    var isFullyConnected: Bool {
        if config.proxyPort != nil {
            return portForwardStatus == .connected && proxyStatus == .connected
        }
        return portForwardStatus == .connected
    }

    /// The effective port that clients should connect to
    var effectivePort: Int {
        config.proxyPort ?? config.localPort
    }

    init(id: UUID, config: PortForwardConnectionConfig) {
        self.id = id
        self.config = config
    }

    init(config: PortForwardConnectionConfig) {
        self.id = config.id
        self.config = config
    }

    nonisolated func hash(into hasher: inout Hasher) {
        hasher.combine(id)
    }

    nonisolated static func == (lhs: PortForwardConnectionState, rhs: PortForwardConnectionState) -> Bool {
        lhs.id == rhs.id
    }
}
```

## File: `platforms/macos/Sources/Models/PortForwardErrors.swift`
```
import Foundation

// MARK: - Process Types

enum PortForwardProcessType: String, Sendable {
    case portForward = "kubectl"
    case proxy = "socat"
}

// MARK: - Errors

enum KubectlError: Error, LocalizedError, Sendable {
    case kubectlNotFound
    case executionFailed(String)
    case parsingFailed(String)
    case clusterNotConnected

    var errorDescription: String? {
        switch self {
        case .kubectlNotFound:
            return "kubectl not found. Please install kubernetes-cli."
        case .executionFailed(let message):
            return "kubectl failed: \(message)"
        case .parsingFailed(let message):
            return "Failed to parse response: \(message)"
        case .clusterNotConnected:
            return "Cannot connect to Kubernetes cluster. Check your kubectl configuration."
        }
    }
}

// MARK: - Callback Types

/// Callback for log output from port-forward processes
typealias LogHandler = @Sendable (String, PortForwardProcessType, Bool) -> Void

/// Callback for port conflict errors (address already in use)
typealias PortConflictHandler = @Sendable (Int) -> Void
```

## File: `platforms/macos/Sources/Models/PortInfo.swift`
```
/**
 * PortInfo.swift
 * PortKiller
 *
 * Represents information about a network port and its associated process.
 * Each PortInfo instance contains details about a port's number, process ID,
 * process name, network address, and user ownership.
 */

import Foundation
import Defaults

/// Information about a network port and its associated process
///
/// PortInfo encapsulates all details about a listening network port, including
/// the process that owns it, the address it's bound to, and whether it's currently active.
struct PortInfo: Identifiable, Hashable, Sendable {
    /// Stable identifier for diffing in SwiftUI.
    /// Using a deterministic key prevents rebuilding every row when scans refresh.
    var id: String { "\(port):\(pid):\(fd):\(isActive)" }

    /// The port number (e.g., 3000, 8080)
    let port: Int

    /// Process ID of the process using this port
    let pid: Int

    /// Name of the process using this port
    let processName: String

    /// Network address the port is bound to (e.g., "*:3000", "127.0.0.1:8080")
    let address: String

    /// Username of the process owner
    let user: String

    /// Full command line that started the process
    let command: String

    /// File descriptor information from lsof
    let fd: String

    /// Whether this port is currently active/listening
    let isActive: Bool

    /// Detected process type (cached at construction time for performance)
    let processType: ProcessType

    /// Formatted port number for display (e.g., ":3000")
    var displayPort: String { ":\(port)" }

    /// Create an inactive placeholder for a favorited/watched port
    ///
    /// - Parameter port: The port number
    /// - Returns: An inactive PortInfo instance with placeholder values
    static func inactive(port: Int) -> PortInfo {
        PortInfo(
            port: port,
            pid: 0,
            processName: "Not running",
            address: "-",
            user: "-",
            command: "",
            fd: "",
            isActive: false,
            processType: .other
        )
    }

    /// Create an active port from scan results
    ///
    /// - Parameters:
    ///   - port: The port number
    ///   - pid: Process ID
    ///   - processName: Name of the process
    ///   - address: Network address
    ///   - user: Username of the process owner
    ///   - command: Full command line
    ///   - fd: File descriptor information
    /// - Returns: An active PortInfo instance
    static func active(port: Int, pid: Int, processName: String, address: String, user: String, command: String, fd: String) -> PortInfo {
        // Check for user-defined process type override first
        let processType: ProcessType
        if let overrideRaw = Defaults[.processTypeOverrides][processName],
           let overrideType = ProcessType(rawValue: overrideRaw) {
            processType = overrideType
        } else {
            processType = ProcessType.detect(from: processName)
        }

        return PortInfo(
            port: port,
            pid: pid,
            processName: processName,
            address: address,
            user: user,
            command: command,
            fd: fd,
            isActive: true,
            processType: processType
        )
    }
}
```

## File: `platforms/macos/Sources/Models/ProcessGroup.swift`
```
/**
 * ProcessGroup.swift
 * PortKiller
 *
 * Groups multiple ports owned by the same process together.
 * Used in tree view mode to display processes and their ports hierarchically.
 */

import Foundation

/// A collection of ports owned by the same process
///
/// ProcessGroup is used in tree view mode to organize multiple ports under
/// their owning process. This provides a hierarchical view where users can
/// expand/collapse processes to see all their associated ports.
struct ProcessGroup: Identifiable, Sendable {
    /// Process name - used as stable identifier for grouping
    let id: String

    /// Name of the process owning these ports
    let processName: String

    /// All PIDs in this group
    let pids: [Int]

    /// All ports owned by this process (across all PIDs)
    let ports: [PortInfo]
}
```

## File: `platforms/macos/Sources/Models/ProcessType.swift`
```
/**
 * ProcessType.swift
 * PortKiller
 *
 * Categorizes processes into different types based on their name and function.
 * Used to provide visual indicators and filtering capabilities in the UI.
 */

import Foundation

/// Category of process based on its function
///
/// ProcessType provides automatic detection of process categories based on
/// well-known process names, enabling better organization and visualization
/// in the UI through icons and color coding.
enum ProcessType: String, CaseIterable, Identifiable, Sendable {
    /// Web servers (nginx, apache, caddy, etc.)
    case webServer = "Web Server"

    /// Database servers (postgres, mysql, redis, etc.)
    case database = "Database"

    /// Development tools (node, python, vite, etc.)
    case development = "Development"

    /// System processes (launchd, kernel services, etc.)
    case system = "System"

    /// Other/unknown processes
    case other = "Other"

    /// Unique identifier for this process type
    var id: String { rawValue }

    /// SF Symbol icon name for this process type
    var icon: String {
        switch self {
        case .webServer: return "globe"
        case .database: return "cylinder"
        case .development: return "hammer"
        case .system: return "gearshape"
        case .other: return "powerplug"
        }
    }

    /// Detect the process type from a process name
    ///
    /// Analyzes the process name against known patterns to categorize it into
    /// one of the predefined process types. The detection is case-insensitive
    /// and looks for common process name patterns.
    ///
    /// - Parameter processName: The name of the process to analyze
    /// - Returns: The detected ProcessType category
    ///
    /// # Examples
    /// ```swift
    /// ProcessType.detect(from: "nginx") // .webServer
    /// ProcessType.detect(from: "postgres") // .database
    /// ProcessType.detect(from: "node") // .development
    /// ProcessType.detect(from: "launchd") // .system
    /// ProcessType.detect(from: "unknown") // .other
    /// ```
    static func detect(from processName: String) -> ProcessType {
        let name = processName.lowercased()

        // Web servers
        let webServers = ["nginx", "apache", "httpd", "caddy", "traefik", "lighttpd"]
        if webServers.contains(where: { name.contains($0) }) {
            return .webServer
        }

        // Databases
        let databases = ["postgres", "mysql", "mariadb", "redis", "mongo", "sqlite", "cockroach", "clickhouse"]
        if databases.contains(where: { name.contains($0) }) {
            return .database
        }

        // Development tools
        let devTools = ["node", "npm", "yarn", "python", "ruby", "php", "java", "go", "cargo", "swift", "vite", "webpack", "esbuild", "next", "nuxt", "remix"]
        if devTools.contains(where: { name.contains($0) }) {
            return .development
        }

        // System processes
        let systemProcs = ["launchd", "rapportd", "sharingd", "airplay", "control", "kernel", "mds", "spotlight"]
        if systemProcs.contains(where: { name.contains($0) }) {
            return .system
        }

        return .other
    }
}
```

## File: `platforms/macos/Sources/Models/Sponsor.swift`
```
import Foundation
import Defaults

/// Represents a sponsor from static JSON
struct Sponsor: Identifiable, Codable, Sendable, Hashable {
    let name: String?
    let login: String
    let avatar: String?
    let amount: Int
    let link: String?
    let org: Bool?

    var id: String { login }

    var displayName: String {
        guard let name, !name.isEmpty else { return login }
        return name
    }

    var avatarUrl: String { avatar ?? "" }
    var profileUrl: URL? {
        guard let link else { return nil }
        return URL(string: link)
    }
}

struct Contributor: Identifiable, Codable, Sendable, Hashable {
	let login: String
	let avatarUrl: String
	let htmlUrl: String
	let contributions: Int
	
	// Calculated property for ID
	var id: String { login }
	
	enum CodingKeys: String, CodingKey {
		case login
		case avatarUrl = "avatar_url"
		case htmlUrl = "html_url"
		case contributions
	}
}

/// Cached sponsor data with timestamp
struct SponsorCache: Codable, Defaults.Serializable {
    let sponsors: [Sponsor]
    let contributors: [Contributor]
    let fetchedAt: Date

    var isStale: Bool {
        // Cache is stale after 24 hours
        Date().timeIntervalSince(fetchedAt) > 86400
    }
}

/// Sponsor display interval options
enum SponsorDisplayInterval: String, CaseIterable, Codable, Defaults.Serializable {
    case monthly = "Monthly"
    case bimonthly = "Every 2 Months"
    case quarterly = "Every 3 Months"
    case never = "Never"

    var days: Int? {
        switch self {
        case .monthly: return 30
        case .bimonthly: return 60
        case .quarterly: return 90
        case .never: return nil
        }
    }

    var localizedName: String {
        switch self {
        case .monthly: return "Monthly"
        case .bimonthly: return "Every 2 Months"
        case .quarterly: return "Every 3 Months"
        case .never: return "Never"
        }
    }
}
```

## File: `platforms/macos/Sources/Models/TunnelLogEntry.swift`
```
import Foundation

/// A log entry from cloudflared tunnel output
@Observable
@MainActor
final class TunnelLogEntry: Identifiable, Sendable {
    let id = UUID()
    let timestamp: Date
    let message: String
    let level: LogLevel

    nonisolated init(timestamp: Date = Date(), message: String, level: LogLevel = .info) {
        self.timestamp = timestamp
        self.message = message
        self.level = level
    }

    enum LogLevel: Sendable {
        case info
        case warning
        case error
        case request

        var color: String {
            switch self {
            case .info: "secondary"
            case .warning: "orange"
            case .error: "red"
            case .request: "blue"
            }
        }
    }

    /// Parses a cloudflared log line to determine level and clean message.
    nonisolated static func parse(_ line: String) -> TunnelLogEntry {
        let lowered = line.lowercased()

        let level: LogLevel
        if lowered.contains("error") || lowered.contains("failed") || lowered.contains("unable to") {
            level = .error
        } else if lowered.contains("warn") {
            level = .warning
        } else if lowered.contains("request") || lowered.contains("200") || lowered.contains("404") ||
                    lowered.contains("get ") || lowered.contains("post ") || lowered.contains("put ") ||
                    lowered.contains("delete ") || lowered.contains("status") {
            level = .request
        } else {
            level = .info
        }

        return TunnelLogEntry(message: line, level: level)
    }
}
```

## File: `platforms/macos/Sources/Models/WatchedPort.swift`
```
/**
 * WatchedPort.swift
 * PortKiller
 *
 * Represents a port that is being monitored for status changes.
 * Users can configure notifications when a watched port starts or stops.
 */

import Foundation
import Defaults

/// A port being monitored for status changes
///
/// WatchedPort allows users to track specific ports and receive notifications
/// when they become active (a process starts using them) or inactive (the process
/// stops using them). Each watched port can be configured independently for
/// start and stop notifications.
struct WatchedPort: Identifiable, Codable, Defaults.Serializable, Sendable {
    /// Unique identifier for this watched port
    let id: UUID

    /// The port number being watched
    let port: Int

    /// Whether to send a notification when this port becomes active
    var notifyOnStart: Bool

    /// Whether to send a notification when this port becomes inactive
    var notifyOnStop: Bool

    /// Create a new watched port
    ///
    /// - Parameters:
    ///   - port: The port number to watch
    ///   - notifyOnStart: Send notification when port starts (default: true)
    ///   - notifyOnStop: Send notification when port stops (default: true)
    init(port: Int, notifyOnStart: Bool = true, notifyOnStop: Bool = true) {
        self.id = UUID()
        self.port = port
        self.notifyOnStart = notifyOnStart
        self.notifyOnStop = notifyOnStop
    }
}
```

## File: `platforms/macos/Sources/Protocols/ClipboardServiceProtocol.swift`
```
/**
 * ClipboardServiceProtocol.swift
 * PortKiller
 *
 * Protocol abstraction for clipboard operations.
 * Enables dependency injection and testing.
 */

import Foundation

/// Protocol for clipboard operations
protocol ClipboardServiceProtocol {
    /// Copies text to the system clipboard
    /// - Parameter text: Text to copy
    static func copy(_ text: String)
}
```

## File: `platforms/macos/Sources/Protocols/NotificationServiceProtocol.swift`
```
/**
 * NotificationServiceProtocol.swift
 * PortKiller
 *
 * Protocol abstraction for system notifications.
 * Enables dependency injection and testing.
 */

import Foundation

/// Protocol for system notification operations
@MainActor
protocol NotificationServiceProtocol {
    /// Sets up the notification service
    func setup()

    /// Sends a notification to the user
    /// - Parameters:
    ///   - title: Notification title
    ///   - body: Notification body text
    func notify(title: String, body: String)

    /// Requests notification permission from the user
    /// - Returns: True if permission was granted
    func requestPermission() async -> Bool
}
```

## File: `platforms/macos/Sources/Protocols/PortScannerProtocol.swift`
```
/**
 * PortScannerProtocol.swift
 * PortKiller
 *
 * Protocol abstraction for port scanning operations.
 * Enables dependency injection and testing.
 */

import Foundation

/// Protocol for port scanning and process management operations
protocol PortScannerProtocol: Sendable {
    /// Scans for all listening TCP ports on the system
    /// - Returns: Array of PortInfo representing active ports
    func scanPorts() async -> [PortInfo]

    /// Kills a process by PID
    /// - Parameters:
    ///   - pid: Process ID to kill
    ///   - force: If true, uses SIGKILL; otherwise uses SIGTERM
    /// - Returns: True if the process was successfully killed
    func killProcess(pid: Int, force: Bool) async -> Bool

    /// Kills a process gracefully with fallback to force kill
    /// - Parameter pid: Process ID to kill
    /// - Returns: True if the process was successfully killed
    func killProcessGracefully(pid: Int) async -> Bool

    /// Finds PIDs of processes with ESTABLISHED connections to a port
    /// - Parameter port: Port number to check
    /// - Returns: Set of PIDs with established connections (excludes the listener)
    func findEstablishedPids(for port: Int) async -> Set<Int>
}
```

## File: `platforms/macos/Sources/Protocols/StorageProtocols.swift`
```
/**
 * StorageProtocols.swift
 * PortKiller
 *
 * Protocol abstractions for persistent storage.
 * Enables dependency injection and testing.
 */

import Foundation

/// Protocol for favorites storage
protocol FavoritesStorageProtocol: Sendable {
    /// Loads favorites from storage
    /// - Returns: Set of favorite port numbers
    func load() -> Set<Int>

    /// Saves favorites to storage
    /// - Parameter favorites: Set of favorite port numbers to save
    func save(_ favorites: Set<Int>)
}

/// Protocol for watched ports storage
protocol WatchedPortsStorageProtocol: Sendable {
    /// Loads watched ports from storage
    /// - Returns: Array of watched port configurations
    func load() -> [WatchedPort]

    /// Saves watched ports to storage
    /// - Parameter watchedPorts: Array of watched port configurations to save
    func save(_ watchedPorts: [WatchedPort])
}

/// Protocol for port forward connections storage
protocol PortForwardStorageProtocol: Sendable {
    /// Loads port forward connection configs from storage
    /// - Returns: Array of port forward connection configurations
    func load() -> [PortForwardConnectionConfig]

    /// Saves port forward connection configs to storage
    /// - Parameter connections: Array of configurations to save
    func save(_ connections: [PortForwardConnectionConfig])
}
```

## File: `platforms/macos/Sources/Services/ClipboardService.swift`
```
import AppKit

/// Utility service for clipboard operations
enum ClipboardService: ClipboardServiceProtocol {
    /// Copy text to clipboard
    static func copy(_ text: String) {
        let pasteboard = NSPasteboard.general
        pasteboard.clearContents()
        pasteboard.setString(text, forType: .string)
    }

    /// Copy logs as markdown formatted text
    static func copyLogsAsMarkdown(_ logs: [PortForwardLogEntry], connectionName: String? = nil) {
        var markdown = ""

        if let name = connectionName {
            markdown += "# Logs: \(name)\n\n"
        }

        markdown += "```\n"
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "HH:mm:ss"

        for log in logs {
            let timestamp = dateFormatter.string(from: log.timestamp)
            let source = log.type == .portForward ? "kubectl" : "socat"
            let prefix = log.isError ? "[ERROR]" : ""
            markdown += "\(timestamp) [\(source)] \(prefix)\(log.message)\n"
        }
        markdown += "```\n"

        copy(markdown)
    }

    /// Copy any items as markdown list
    static func copyAsMarkdownList(_ items: [String], title: String? = nil) {
        var markdown = ""

        if let title = title {
            markdown += "# \(title)\n\n"
        }

        for item in items {
            markdown += "- \(item)\n"
        }

        copy(markdown)
    }

    /// Copy as markdown code block
    static func copyAsCodeBlock(_ text: String, language: String = "") {
        let markdown = "```\(language)\n\(text)\n```"
        copy(markdown)
    }

    /// Copy as markdown table
    static func copyAsMarkdownTable(headers: [String], rows: [[String]]) {
        var markdown = ""

        // Header row
        markdown += "| " + headers.joined(separator: " | ") + " |\n"

        // Separator row
        markdown += "| " + headers.map { _ in "---" }.joined(separator: " | ") + " |\n"

        // Data rows
        for row in rows {
            markdown += "| " + row.joined(separator: " | ") + " |\n"
        }

        copy(markdown)
    }
}
```

## File: `platforms/macos/Sources/Services/CloudflaredService.swift`
```
import Foundation
import Darwin
import Defaults

// MARK: - Cloudflared Service Actor

/// Manages cloudflared tunnel subprocesses
actor CloudflaredService {
    private var processes: [UUID: Process] = [:]
    private var outputTasks: [UUID: Task<Void, Never>] = [:]
    private var urlHandlers: [UUID: @Sendable (String) -> Void] = [:]
    private var errorHandlers: [UUID: @Sendable (String) -> Void] = [:]
    private var logHandlers: [UUID: @Sendable (String) -> Void] = [:]

    // MARK: - Dependency Check

    nonisolated var cloudflaredPath: String? {
        // Check custom path first
        if let custom = Defaults[.customCloudflaredPath],
           !custom.isEmpty,
           FileManager.default.fileExists(atPath: custom) {
            return custom
        }
        let paths = [
            "/opt/homebrew/bin/cloudflared",
            "/usr/local/bin/cloudflared"
        ]
        return paths.first { FileManager.default.fileExists(atPath: $0) }
    }

    nonisolated var isInstalled: Bool {
        cloudflaredPath != nil
    }

    nonisolated var isUsingCustomPath: Bool {
        if let custom = Defaults[.customCloudflaredPath],
           !custom.isEmpty,
           FileManager.default.fileExists(atPath: custom) {
            return true
        }
        return false
    }

    nonisolated var autoDetectedPath: String? {
        let paths = [
            "/opt/homebrew/bin/cloudflared",
            "/usr/local/bin/cloudflared"
        ]
        return paths.first { FileManager.default.fileExists(atPath: $0) }
    }

    // MARK: - Handler Management

    func setURLHandler(for id: UUID, handler: @escaping @Sendable (String) -> Void) {
        urlHandlers[id] = handler
    }

    func setErrorHandler(for id: UUID, handler: @escaping @Sendable (String) -> Void) {
        errorHandlers[id] = handler
    }

    func setLogHandler(for id: UUID, handler: @escaping @Sendable (String) -> Void) {
        logHandlers[id] = handler
    }

    func removeHandlers(for id: UUID) {
        urlHandlers.removeValue(forKey: id)
        errorHandlers.removeValue(forKey: id)
        logHandlers.removeValue(forKey: id)
    }

    // MARK: - Tunnel Management

    func startTunnel(id: UUID, port: Int) throws -> Process {
        guard let cloudflaredPath = cloudflaredPath else {
            throw CloudflaredError.notInstalled
        }

        let process = Process()
        process.executableURL = URL(fileURLWithPath: cloudflaredPath)
        let protocolValue = Defaults[.cloudflaredProtocol].rawValue
        process.arguments = ["tunnel", "--url", "localhost:\(port)", "--protocol", protocolValue]

        let pipe = Pipe()
        process.standardOutput = pipe
        process.standardError = pipe

        try process.run()
        processes[id] = process

        startReadingOutput(pipe: pipe, id: id)

        return process
    }

    func stopTunnel(id: UUID) async {
        // Cancel output reading task
        outputTasks[id]?.cancel()
        outputTasks.removeValue(forKey: id)

        // Terminate process gracefully
        guard let process = processes[id] else { return }

        if process.isRunning {
            let pid = process.processIdentifier
            process.terminate()  // SIGTERM

            // Wait 500ms then force kill if still running
            try? await Task.sleep(for: .milliseconds(500))
            if kill(pid, 0) == 0 {  // Process still exists
                kill(pid, SIGKILL)
            }
        }

        processes.removeValue(forKey: id)
        removeHandlers(for: id)
    }

    func stopAllTunnels() async {
        for id in Array(processes.keys) {
            await stopTunnel(id: id)
        }
    }

    func isRunning(for id: UUID) -> Bool {
        processes[id]?.isRunning ?? false
    }

    // MARK: - Output Parsing

    private func startReadingOutput(pipe: Pipe, id: UUID) {
        let task = Task { [weak self] in
            let handle = pipe.fileHandleForReading

            while !Task.isCancelled {
                // Use autoreleasepool to prevent memory accumulation from FileHandle reads
                var output: String = ""
                autoreleasepool {
                    let data = handle.availableData
                    if data.isEmpty {
                        output = ""
                    } else {
                        output = String(data: data, encoding: .utf8)?
                            .trimmingCharacters(in: .whitespacesAndNewlines) ?? ""
                    }
                }

                if output.isEmpty { break }

                // Use split for zero-copy iteration
                let lines = output.split(separator: "\n", omittingEmptySubsequences: true)
                for line in lines {
                    await self?.parseLine(String(line), for: id)
                }
            }
        }
        outputTasks[id] = task
    }

    private func parseLine(_ line: String, for id: UUID) {
        // Forward all lines to log handler
        logHandlers[id]?(line)

        // cloudflared outputs the URL like:
        // "Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):
        // https://something-random.trycloudflare.com"
        // OR in newer versions with table format:
        // "| https://something-random.trycloudflare.com |"

        if let url = extractTunnelURL(from: line) {
            urlHandlers[id]?(url)
        }

        // Check for errors
        let lowercased = line.lowercased()
        if lowercased.contains("error") || lowercased.contains("failed") || lowercased.contains("unable to") {
            errorHandlers[id]?(line)
        }
    }

    private func extractTunnelURL(from line: String) -> String? {
        // Pattern: https://xxx.trycloudflare.com
        let pattern = #"https://[a-z0-9-]+\.trycloudflare\.com"#
        if let range = line.range(of: pattern, options: .regularExpression) {
            return String(line[range])
        }
        return nil
    }
}

// MARK: - Errors

enum CloudflaredError: Error, LocalizedError, Sendable {
    case notInstalled
    case startFailed(String)
    case tunnelFailed(String)

    var errorDescription: String? {
        switch self {
        case .notInstalled:
            return "cloudflared is not installed"
        case .startFailed(let message):
            return "Failed to start tunnel: \(message)"
        case .tunnelFailed(let message):
            return "Tunnel error: \(message)"
        }
    }
}
```

## File: `platforms/macos/Sources/Services/DependencyChecker.swift`
```
import Foundation
import Defaults

// MARK: - Dependency

struct PortForwardDependency: Sendable {
    let name: String
    let possiblePaths: [String]
    let brewPackage: String
    let isRequired: Bool

    var isInstalled: Bool {
        possiblePaths.contains { FileManager.default.fileExists(atPath: $0) }
    }

    var installedPath: String? {
        possiblePaths.first { FileManager.default.fileExists(atPath: $0) }
    }
}

// MARK: - Dependency Checker

actor DependencyChecker {
    static let shared = DependencyChecker()

    nonisolated let dependencies: [PortForwardDependency] = [
        PortForwardDependency(
            name: "kubectl",
            possiblePaths: [
                "/opt/homebrew/bin/kubectl",
                "/usr/local/bin/kubectl",
                "/usr/bin/kubectl"
            ],
            brewPackage: "kubernetes-cli",
            isRequired: true
        ),
        PortForwardDependency(
            name: "socat",
            possiblePaths: [
                "/opt/homebrew/bin/socat",
                "/usr/local/bin/socat"
            ],
            brewPackage: "socat",
            isRequired: false
        )
    ]

    nonisolated var kubectl: PortForwardDependency {
        dependencies.first { $0.name == "kubectl" }!
    }

    nonisolated var socat: PortForwardDependency {
        dependencies.first { $0.name == "socat" }!
    }

    nonisolated var missingRequired: [PortForwardDependency] {
        dependencies.filter { $0.isRequired && !$0.isInstalled }
    }

    nonisolated var missingOptional: [PortForwardDependency] {
        dependencies.filter { !$0.isRequired && !$0.isInstalled }
    }

    nonisolated var allRequiredInstalled: Bool {
        missingRequired.isEmpty
    }

    nonisolated var kubectlPath: String? {
        // Check custom path first
        if let custom = Defaults[.customKubectlPath],
           !custom.isEmpty,
           FileManager.default.fileExists(atPath: custom) {
            return custom
        }
        return kubectl.installedPath
    }

    nonisolated var socatPath: String? {
        // Check custom path first
        if let custom = Defaults[.customSocatPath],
           !custom.isEmpty,
           FileManager.default.fileExists(atPath: custom) {
            return custom
        }
        return socat.installedPath
    }

    nonisolated var isUsingCustomKubectl: Bool {
        if let custom = Defaults[.customKubectlPath],
           !custom.isEmpty,
           FileManager.default.fileExists(atPath: custom) {
            return true
        }
        return false
    }

    nonisolated var isUsingCustomSocat: Bool {
        if let custom = Defaults[.customSocatPath],
           !custom.isEmpty,
           FileManager.default.fileExists(atPath: custom) {
            return true
        }
        return false
    }

    func checkAndInstallMissing() async -> (success: Bool, message: String) {
        let missing = dependencies.filter { !$0.isInstalled }

        guard !missing.isEmpty else {
            return (true, "All dependencies are installed")
        }

        let brewPath: String
        if FileManager.default.fileExists(atPath: "/opt/homebrew/bin/brew") {
            brewPath = "/opt/homebrew/bin/brew"
        } else if FileManager.default.fileExists(atPath: "/usr/local/bin/brew") {
            brewPath = "/usr/local/bin/brew"
        } else {
            return (false, "Homebrew is not installed. Please install it from https://brew.sh")
        }

        var results: [String] = []

        for dep in missing {
            let result = await installWithBrew(brewPath: brewPath, package: dep.brewPackage)
            results.append("\(dep.name): \(result.success ? "Installed" : "Failed - \(result.message)")")
        }

        let allSuccess = missing.allSatisfy(\.isInstalled)
        return (allSuccess, results.joined(separator: "\n"))
    }

    private func installWithBrew(brewPath: String, package: String) async -> (success: Bool, message: String) {
        let process = Process()
        process.executableURL = URL(fileURLWithPath: brewPath)
        process.arguments = ["install", package]

        let pipe = Pipe()
        process.standardOutput = pipe
        process.standardError = pipe

        do {
            try process.run()
            process.waitUntilExit()

            // Use autoreleasepool to prevent memory accumulation
            var output: String = ""
            autoreleasepool {
                let data = pipe.fileHandleForReading.readDataToEndOfFile()
                output = String(data: data, encoding: .utf8) ?? ""
            }

            return process.terminationStatus == 0 ? (true, "Installed") : (false, output)
        } catch {
            return (false, error.localizedDescription)
        }
    }
}
```

## File: `platforms/macos/Sources/Services/NotificationService.swift`
```
/**
 * NotificationService.swift
 * PortKiller
 *
 * Manages system notifications for watched port events.
 * Handles notification center setup, permissions, and message delivery.
 */

import Foundation
import SwiftUI
@preconcurrency import UserNotifications

/// Service for managing system notifications
///
/// NotificationService centralizes all notification-related functionality,
/// including permission requests, notification delivery, and delegate handling.
/// It ensures notifications only run when the app is built as a .app bundle.
@MainActor
final class NotificationService: NSObject, NotificationServiceProtocol {
    /// Singleton instance
    static let shared = NotificationService()

    /// Notification center instance (nil if not running as .app bundle)
    private var notificationCenter: UNUserNotificationCenter? {
        // UNUserNotificationCenter only works in .app bundle
        guard Bundle.main.bundleIdentifier != nil,
              Bundle.main.bundlePath.hasSuffix(".app") else { return nil }
        return UNUserNotificationCenter.current()
    }

    private override init() {
        super.init()
    }

    /// Set up the notification service and request initial permissions
    ///
    /// Call this once during app initialization. It configures the notification
    /// center delegate and requests authorization if not already determined.
    func setup() {
        guard let center = notificationCenter else { return }
        center.delegate = self

        Task {
            let settings = await center.notificationSettings()
            if settings.authorizationStatus == .notDetermined {
                _ = try? await center.requestAuthorization(options: [.alert, .sound])
            }
        }
    }

    /// Request notification permissions from the user
    ///
    /// Presents the system permission dialog if not already determined.
    ///
    /// - Returns: True if permission was granted, false otherwise
    func requestPermission() async -> Bool {
        guard let center = notificationCenter else { return false }

        do {
            return try await center.requestAuthorization(options: [.alert, .sound, .badge])
        } catch {
            return false
        }
    }

    /// Check current notification authorization status
    ///
    /// - Returns: The current authorization status
    func checkAuthorizationStatus() async -> UNAuthorizationStatus {
        guard let center = notificationCenter else { return .notDetermined }
        let settings = await center.notificationSettings()
        return settings.authorizationStatus
    }

    /// Send a notification
    ///
    /// Delivers a notification with the specified title and body.
    /// Notifications are only sent if the app is built as a .app bundle
    /// and has proper permissions.
    ///
    /// - Parameters:
    ///   - title: Notification title
    ///   - body: Notification body message
    ///
    /// # Example
    /// ```swift
    /// NotificationService.shared.notify(
    ///     title: "Port 3000 Available",
    ///     body: "Port is now free."
    /// )
    /// ```
    func notify(title: String, body: String) {
        guard let center = notificationCenter else { return }

        let content = UNMutableNotificationContent()
        content.title = title
        content.body = body
        content.sound = .default

        let request = UNNotificationRequest(
            identifier: UUID().uuidString,
            content: content,
            trigger: nil
        )

        center.add(request)
    }
}

// MARK: - UNUserNotificationCenterDelegate

extension NotificationService: UNUserNotificationCenterDelegate {
    /// Handle notifications while app is in foreground
    nonisolated func userNotificationCenter(
        _ center: UNUserNotificationCenter,
        willPresent notification: UNNotification,
        withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void
    ) {
        completionHandler([.banner, .sound])
    }
}
```

## File: `platforms/macos/Sources/Services/PermissionService.swift`
```
/**
 * PermissionService.swift
 * PortKiller
 *
 * Centralized service for managing system permissions.
 * Handles accessibility and notification permission checks and requests.
 */

import Foundation
import SwiftUI
import ApplicationServices
@preconcurrency import UserNotifications

/// Service for managing system permissions
///
/// PermissionService centralizes all permission-related logic, including
/// checking and requesting accessibility and notification permissions.
/// It provides reactive properties for observing permission state changes.
@MainActor
@Observable
final class PermissionService {
    /// Singleton instance
    static let shared = PermissionService()

    /// Whether accessibility permission is granted
    var hasAccessibilityPermission: Bool = false

    /// Current notification authorization status
    var notificationStatus: UNAuthorizationStatus = .notDetermined

    /// Timer for periodic permission checks
    @ObservationIgnored
    private var permissionCheckTimer: Timer?

    private init() {
        checkPermissions()
    }

    /// Whether notification permission is granted
    var hasNotificationPermission: Bool {
        notificationStatus == .authorized
    }

    // MARK: - Accessibility Permission

    /// Check if accessibility permission is granted
    ///
    /// - Returns: True if accessibility permission is granted
    func checkAccessibility() -> Bool {
        let hasPermission = AXIsProcessTrusted()
        hasAccessibilityPermission = hasPermission
        return hasPermission
    }

    /// Request accessibility permission
    ///
    /// Opens the system accessibility permission dialog.
    func requestAccessibility() {
        let options = ["AXTrustedCheckOptionPrompt": true] as CFDictionary
        AXIsProcessTrustedWithOptions(options)
    }

    // MARK: - Notification Permission

    /// Check current notification permission status
    ///
    /// - Returns: Current authorization status
    func checkNotificationPermission() async -> UNAuthorizationStatus {
        // Only check if running as .app bundle
        guard Bundle.main.bundleIdentifier != nil,
              Bundle.main.bundlePath.hasSuffix(".app") else {
            notificationStatus = .notDetermined
            return .notDetermined
        }

        let settings = await UNUserNotificationCenter.current().notificationSettings()
        notificationStatus = settings.authorizationStatus
        return settings.authorizationStatus
    }

    /// Request notification permission
    ///
    /// Presents the system notification permission dialog.
    ///
    /// - Returns: True if permission was granted
    func requestNotificationPermission() async -> Bool {
        guard Bundle.main.bundlePath.hasSuffix(".app") else {
            return false
        }

        do {
            let granted = try await UNUserNotificationCenter.current()
                .requestAuthorization(options: [.alert, .sound, .badge])
            _ = await checkNotificationPermission()
            return granted
        } catch {
            return false
        }
    }

    /// Open system notification settings for this app
    func openNotificationSettings() {
        guard let bundleId = Bundle.main.bundleIdentifier else { return }
        let urlString = "x-apple.systempreferences:com.apple.Notifications-Settings.extension?id=\(bundleId)"
        if let url = URL(string: urlString) {
            NSWorkspace.shared.open(url)
        }
    }

    // MARK: - Periodic Checks

    /// Check all permissions
    ///
    /// Updates both accessibility and notification permission status.
    func checkPermissions() {
        // Check accessibility
        hasAccessibilityPermission = AXIsProcessTrusted()

        // Check notification permission (only works in .app bundle)
        guard Bundle.main.bundleIdentifier != nil,
              Bundle.main.bundlePath.hasSuffix(".app") else {
            notificationStatus = .notDetermined
            return
        }

        Task {
            await checkNotificationPermission()
        }
    }

    /// Start periodic permission checks
    ///
    /// Checks permissions every 5 seconds to detect changes made in System Settings.
    func startPeriodicChecks() {
        guard permissionCheckTimer == nil else { return }
        permissionCheckTimer = Timer.scheduledTimer(withTimeInterval: 5.0, repeats: true) { [weak self] _ in
            Task { @MainActor in
                self?.checkPermissions()
            }
        }
    }

    /// Stop periodic permission checks
    func stopPeriodicChecks() {
        permissionCheckTimer?.invalidate()
        permissionCheckTimer = nil
    }

    // MARK: - UI Helpers

    /// Icon name for notification status
    var notificationStatusIcon: String {
        switch notificationStatus {
        case .authorized: return "checkmark.circle.fill"
        case .denied: return "xmark.circle.fill"
        case .notDetermined: return "questionmark.circle.fill"
        case .provisional, .ephemeral: return "checkmark.circle.fill"
        @unknown default: return "questionmark.circle.fill"
        }
    }

    /// Color for notification status
    var notificationStatusColor: Color {
        switch notificationStatus {
        case .authorized, .provisional, .ephemeral: return .green
        case .denied: return .red
        case .notDetermined: return .orange
        @unknown default: return .secondary
        }
    }

    /// Text description for notification status
    var notificationStatusText: String {
        switch notificationStatus {
        case .authorized: return "Alerts enabled for port watch"
        case .denied: return "Notifications disabled in System Settings"
        case .notDetermined: return "Required for port watch alerts"
        case .provisional: return "Provisional notifications enabled"
        case .ephemeral: return "Temporary notifications enabled"
        @unknown default: return "Unknown status"
        }
    }
}
```

## File: `platforms/macos/Sources/Services/PortForwardOutputParser.swift`
```
import Foundation

/// Parses output from kubectl and socat processes
enum PortForwardOutputParser {
    /// Checks if a log line indicates an error condition
    static func isErrorLine(_ line: String) -> Bool {
        let lowercased = line.lowercased()
        return lowercased.contains("error") ||
               lowercased.contains("failed") ||
               lowercased.contains("unable to") ||
               lowercased.contains("connection refused") ||
               lowercased.contains("lost connection") ||
               lowercased.contains("an error occurred")
    }

    /// Detects port conflict from log line and returns the conflicting port if found
    static func detectPortConflict(in line: String) -> Int? {
        let lowercased = line.lowercased()
        guard lowercased.contains("address already in use") else { return nil }

        // kubectl format: "listen tcp4 127.0.0.1:7700: bind: address already in use"
        if let portMatch = line.range(of: #"127\.0\.0\.1:(\d+)"#, options: .regularExpression) {
            let portStr = line[portMatch].split(separator: ":").last ?? ""
            return Int(portStr)
        }

        // socat format: "bind(5, {LEN=16 AF=2 0.0.0.0:7699}, 16): Address already in use"
        if let portMatch = line.range(of: #"0\.0\.0\.0:(\d+)"#, options: .regularExpression) {
            let portStr = line[portMatch].split(separator: ":").last ?? ""
            return Int(portStr)
        }

        return nil
    }
}
```

## File: `platforms/macos/Sources/Services/PortGroupingService.swift`
```
/**
 * PortGroupingService.swift
 * PortKiller
 *
 * Centralized service for grouping ports by process or type.
 * Extracts duplicate grouping logic from views into a reusable service.
 */

import Foundation

/// Service for grouping and organizing port information
///
/// PortGroupingService provides centralized logic for organizing ports
/// in different ways, such as grouping by process (PID) or by process type.
/// This eliminates duplicate grouping logic across multiple views.
actor PortGroupingService {
    /// Singleton instance
    static let shared = PortGroupingService()

    private init() {}

    /// Groups ports by their owning process
    ///
    /// Creates ProcessGroup instances containing all ports owned by the same process.
    /// Groups are sorted alphabetically by process name for consistent display.
    ///
    /// - Parameter ports: Array of ports to group
    /// - Returns: Array of ProcessGroup instances, sorted by process name
    ///
    /// # Example
    /// ```swift
    /// let groups = await PortGroupingService.shared.groupByProcess(ports)
    /// // groups[0] might contain: ProcessGroup(id: 1234, processName: "node", ports: [3000, 3001])
    /// ```
    func groupByProcess(_ ports: [PortInfo]) -> [ProcessGroup] {
        let grouped = Dictionary(grouping: ports) { $0.processName }
        return grouped.map { name, ports in
            ProcessGroup(
                id: name,
                processName: name,
                pids: Array(Set(ports.map(\.pid))).sorted(),
                ports: ports.sorted { $0.port < $1.port }
            )
        }.sorted { $0.processName.localizedCaseInsensitiveCompare($1.processName) == .orderedAscending }
    }

    /// Groups ports by their owning process with custom sorting
    ///
    /// Creates ProcessGroup instances with custom sort logic that prioritizes
    /// favorited and watched ports. This is used in the menu bar view.
    ///
    /// - Parameters:
    ///   - ports: Array of ports to group
    ///   - favorites: Set of favorited port numbers
    ///   - watched: Set of watched port numbers
    /// - Returns: Array of ProcessGroup instances, sorted by priority then name
    func groupByProcessWithPriority(_ ports: [PortInfo], favorites: Set<Int>, watched: Set<Int>) -> [ProcessGroup] {
        let grouped = Dictionary(grouping: ports) { $0.processName }
        return grouped.map { name, ports in
            ProcessGroup(
                id: name,
                processName: name,
                pids: Array(Set(ports.map(\.pid))).sorted(),
                ports: ports.sorted { $0.port < $1.port }
            )
        }.sorted { a, b in
            // Check if groups have favorite or watched ports
            let aHasFavorite = a.ports.contains(where: { favorites.contains($0.port) })
            let aHasWatched = a.ports.contains(where: { watched.contains($0.port) })
            let bHasFavorite = b.ports.contains(where: { favorites.contains($0.port) })
            let bHasWatched = b.ports.contains(where: { watched.contains($0.port) })

            // Priority: Favorite > Watched > Neither
            let aPriority = aHasFavorite ? 2 : (aHasWatched ? 1 : 0)
            let bPriority = bHasFavorite ? 2 : (bHasWatched ? 1 : 0)

            if aPriority != bPriority {
                return aPriority > bPriority
            } else {
                // Same priority, sort alphabetically by process name
                return a.processName.localizedCaseInsensitiveCompare(b.processName) == .orderedAscending
            }
        }
    }

    /// Groups ports by their process type
    ///
    /// Organizes ports into categories based on their detected process type
    /// (web server, database, development tool, system process, or other).
    ///
    /// - Parameter ports: Array of ports to group
    /// - Returns: Dictionary mapping ProcessType to arrays of ports
    ///
    /// # Example
    /// ```swift
    /// let grouped = await PortGroupingService.shared.groupByType(ports)
    /// let webServers = grouped[.webServer] // All ports for web servers
    /// let databases = grouped[.database]   // All ports for databases
    /// ```
    func groupByType(_ ports: [PortInfo]) -> [ProcessType: [PortInfo]] {
        Dictionary(grouping: ports) { $0.processType }
    }
}
```

## File: `platforms/macos/Sources/Services/PortHealthChecker.swift`
```
import Foundation
import Darwin

/// Utility for checking TCP port availability
enum PortHealthChecker {
    /// Check if a port is actually accepting connections (TCP health check)
    static func isPortOpen(port: Int) -> Bool {
        let sock = Darwin.socket(AF_INET, SOCK_STREAM, 0)
        guard sock >= 0 else { return false }
        defer { Darwin.close(sock) }

        var timeout = timeval(tv_sec: 1, tv_usec: 0)
        setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO, &timeout, socklen_t(MemoryLayout<timeval>.size))

        var addr = sockaddr_in()
        addr.sin_family = sa_family_t(AF_INET)
        addr.sin_port = in_port_t(port).bigEndian
        addr.sin_addr.s_addr = inet_addr("127.0.0.1")

        let result = withUnsafePointer(to: &addr) {
            $0.withMemoryRebound(to: sockaddr.self, capacity: 1) {
                Darwin.connect(sock, $0, socklen_t(MemoryLayout<sockaddr_in>.size))
            }
        }

        return result == 0
    }
}
```

## File: `platforms/macos/Sources/Services/SponsorsService.swift`
```
import Foundation

/// Service for fetching sponsors from static JSON
actor SponsorsService {
    private let sponsorsURL = URL(string: "https://raw.githubusercontent.com/productdevbook/static/main/sponsors.json")!
    private let contributorsURL = URL(string: "https://api.github.com/repos/productdevbook/port-killer/contributors")!

    enum SponsorsError: Error, LocalizedError, Sendable {
        case networkError(String)
        case invalidResponse
        case decodingError(String)

        var errorDescription: String? {
            switch self {
            case .networkError(let description):
                return "Network error: \(description)"
            case .invalidResponse:
                return "Invalid response from server"
            case .decodingError(let description):
                return "Failed to parse sponsors: \(description)"
            }
        }
    }

    /// Fetch sponsors from static JSON
    func fetchSponsors() async throws -> [Sponsor] {
        let (data, response) = try await URLSession.shared.data(from: sponsorsURL)

        guard let httpResponse = response as? HTTPURLResponse,
              (200...299).contains(httpResponse.statusCode) else {
            throw SponsorsError.invalidResponse
        }

        do {
            return try JSONDecoder().decode([Sponsor].self, from: data)
        } catch {
            throw SponsorsError.decodingError(error.localizedDescription)
        }
    }

    /// Fetch contributors from GitHub API
    func fetchContributors() async throws -> [Contributor] {
        var request = URLRequest(url: contributorsURL)
        request.setValue("application/vnd.github+json", forHTTPHeaderField: "Accept")
        request.setValue("2022-11-28", forHTTPHeaderField: "X-GitHub-Api-Version")
        
        let (data, response) = try await URLSession.shared.data(for: request)

        guard let httpResponse = response as? HTTPURLResponse,
              (200...299).contains(httpResponse.statusCode) else {
            throw SponsorsError.invalidResponse
        }

        do {
            return try JSONDecoder().decode([Contributor].self, from: data)
        } catch {
            throw SponsorsError.decodingError(error.localizedDescription)
        }
    }
}
```

## File: `platforms/macos/Sources/Services/Storage/DefaultsFavoritesStorage.swift`
```
/**
 * DefaultsFavoritesStorage.swift
 * PortKiller
 *
 * UserDefaults-backed storage for favorites.
 */

import Foundation
import Defaults

/// Default implementation of FavoritesStorageProtocol using UserDefaults
struct DefaultsFavoritesStorage: FavoritesStorageProtocol {
    func load() -> Set<Int> {
        Defaults[.favorites]
    }

    func save(_ favorites: Set<Int>) {
        Defaults[.favorites] = favorites
    }
}
```

## File: `platforms/macos/Sources/Services/Storage/DefaultsPortForwardStorage.swift`
```
/**
 * DefaultsPortForwardStorage.swift
 * PortKiller
 *
 * UserDefaults-backed storage for port forward connections.
 */

import Foundation
import Defaults

/// Default implementation of PortForwardStorageProtocol using UserDefaults
struct DefaultsPortForwardStorage: PortForwardStorageProtocol {
    func load() -> [PortForwardConnectionConfig] {
        Defaults[.portForwardConnections]
    }

    func save(_ connections: [PortForwardConnectionConfig]) {
        Defaults[.portForwardConnections] = connections
    }
}
```

## File: `platforms/macos/Sources/Services/Storage/DefaultsWatchedPortsStorage.swift`
```
/**
 * DefaultsWatchedPortsStorage.swift
 * PortKiller
 *
 * UserDefaults-backed storage for watched ports.
 */

import Foundation
import Defaults

/// Default implementation of WatchedPortsStorageProtocol using UserDefaults
struct DefaultsWatchedPortsStorage: WatchedPortsStorageProtocol {
    func load() -> [WatchedPort] {
        Defaults[.watchedPorts]
    }

    func save(_ watchedPorts: [WatchedPort]) {
        Defaults[.watchedPorts] = watchedPorts
    }
}
```

## File: `platforms/macos/Sources/State/FavoritesState.swift`
```
/**
 * FavoritesState.swift
 * PortKiller
 *
 * Manages favorite ports state with persistence.
 * Extracted from AppState for single responsibility.
 */

import Foundation

/// Manages favorite ports
@Observable
@MainActor
final class FavoritesState {
    /// Storage backend for persistence
    private let storage: FavoritesStorageProtocol

    /// Cached favorites, synced with storage on change
    private var _favorites: Set<Int> {
        didSet {
            storage.save(_favorites)
        }
    }

    /// Port numbers marked as favorites
    var favorites: Set<Int> {
        get { _favorites }
        set { _favorites = newValue }
    }

    /// Initialize with storage backend
    /// - Parameter storage: Storage implementation (defaults to UserDefaults)
    init(storage: FavoritesStorageProtocol = DefaultsFavoritesStorage()) {
        self.storage = storage
        self._favorites = storage.load()
    }

    /// Toggles favorite status for a port
    /// - Parameter port: Port number to toggle
    func toggle(_ port: Int) {
        if _favorites.contains(port) {
            _favorites.remove(port)
        } else {
            _favorites.insert(port)
        }
    }

    /// Checks if a port is marked as favorite
    /// - Parameter port: Port number to check
    /// - Returns: True if the port is a favorite
    func isFavorite(_ port: Int) -> Bool {
        _favorites.contains(port)
    }
}
```

## File: `platforms/macos/Sources/State/WatchedPortsState.swift`
```
/**
 * WatchedPortsState.swift
 * PortKiller
 *
 * Manages watched ports state with persistence and notifications.
 * Extracted from AppState for single responsibility.
 */

import Foundation

/// Manages watched ports and notifications
@Observable
@MainActor
final class WatchedPortsState {
    /// Storage backend for persistence
    private let storage: WatchedPortsStorageProtocol

    /// Notification service for alerts
    private let notificationService: NotificationServiceProtocol

    /// Cached watched ports, synced with storage on change
    private var _watchedPorts: [WatchedPort] {
        didSet {
            storage.save(_watchedPorts)
        }
    }

    /// Tracks previous port states for change detection
    var previousPortStates: [Int: Bool] = [:]

    /// Ports being watched for state changes
    var watchedPorts: [WatchedPort] {
        get { _watchedPorts }
        set { _watchedPorts = newValue }
    }

    /// Initialize with storage and notification backends
    init(
        storage: WatchedPortsStorageProtocol = DefaultsWatchedPortsStorage(),
        notificationService: NotificationServiceProtocol = NotificationService.shared
    ) {
        self.storage = storage
        self.notificationService = notificationService
        self._watchedPorts = storage.load()
    }

    /// Toggles watch status for a port
    /// - Parameter port: Port number to toggle
    func toggle(_ port: Int) {
        if let idx = _watchedPorts.firstIndex(where: { $0.port == port }) {
            previousPortStates.removeValue(forKey: port)
            _watchedPorts.remove(at: idx)
        } else {
            _watchedPorts.append(WatchedPort(port: port))
        }
    }

    /// Checks if a port is being watched
    /// - Parameter port: Port number to check
    /// - Returns: True if the port is being watched
    func isWatching(_ port: Int) -> Bool {
        _watchedPorts.contains { $0.port == port }
    }

    /// Updates notification preferences for a watched port
    func updateWatch(_ port: Int, onStart: Bool, onStop: Bool) {
        if let idx = _watchedPorts.firstIndex(where: { $0.port == port }) {
            _watchedPorts[idx].notifyOnStart = onStart
            _watchedPorts[idx].notifyOnStop = onStop
        }
    }

    /// Removes a watched port by its ID
    func removeWatch(_ id: UUID) {
        if let w = _watchedPorts.first(where: { $0.id == id }) {
            previousPortStates.removeValue(forKey: w.port)
        }
        _watchedPorts.removeAll { $0.id == id }
    }

    /// Checks watched ports for state changes and triggers notifications
    /// - Parameter ports: Current active ports to check against
    func checkForChanges(ports: [PortInfo]) {
        let activePorts = Set(ports.map { $0.port })

        for w in _watchedPorts {
            let isActive = activePorts.contains(w.port)

            if let wasActive = previousPortStates[w.port] {
                if wasActive && !isActive && w.notifyOnStop {
                    notificationService.notify(
                        title: "Port \(w.port) Available",
                        body: "Port is now free."
                    )
                } else if !wasActive && isActive && w.notifyOnStart {
                    let name = ports.first { $0.port == w.port }?.processName ?? "Unknown"
                    notificationService.notify(
                        title: "Port \(w.port) In Use",
                        body: "Used by \(name)."
                    )
                }
            }

            previousPortStates[w.port] = isActive
        }
    }
}
```

## File: `platforms/macos/Sources/Views/MainWindowView.swift`
```
import SwiftUI

struct MainWindowView: View {
    @Environment(AppState.self) private var appState
    @Environment(SponsorManager.self) private var sponsorManager
    @State private var columnVisibility = NavigationSplitViewVisibility.all
    @State private var showKillAllConfirmation = false

    var body: some View {
        @Bindable var state = appState

        NavigationSplitView(columnVisibility: $columnVisibility) {
            SidebarView()
                .navigationSplitViewColumnWidth(min: 180, ideal: 220, max: 280)
        } content: {
            contentView
                .searchable(text: $state.filter.searchText, prompt: "Search ports, processes...")
                .navigationSplitViewColumnWidth(min: 300, ideal: 400, max: .infinity)
        } detail: {
            detailView
                .navigationSplitViewColumnWidth(min: 400, ideal: 500, max: 600)
        }
        .navigationSplitViewStyle(.balanced)
        .toolbar {
            toolbarContent
        }
        .onAppear {
            // Ensure app is properly activated for keyboard input
            NSApp.setActivationPolicy(.regular)
            NSApp.activate(ignoringOtherApps: true)
        }
        .confirmationDialog(
            "Kill All Processes",
            isPresented: $showKillAllConfirmation
        ) {
            Button("Kill All (\(appState.filteredPorts.count) processes)", role: .destructive) {
                Task {
                    await appState.killAll()
                }
            }
            Button("Cancel", role: .cancel) {}
        } message: {
            Text("Are you sure you want to kill all \(appState.filteredPorts.count) processes? This action cannot be undone.")
        }
        .onKeyPress(.delete) {
            if let port = appState.selectedPort {
                Task {
                    await appState.killPort(port)
                }
                return .handled
            }
            return .ignored
        }
        .onKeyPress(.deleteForward) {
            if let port = appState.selectedPort {
                Task {
                    await appState.killPort(port)
                }
                return .handled
            }
            return .ignored
        }
    }

    @ViewBuilder
    private var contentView: some View {
        switch appState.selectedSidebarItem {
        case .settings:
            SettingsView(state: appState, updateManager: appState.updateManager)
                .id("settings")
                .frame(maxWidth: .infinity, maxHeight: .infinity)
                .navigationSplitViewColumnWidth(min: 400, ideal: 600, max: .infinity)
        case .sponsors:
            SponsorsPageView(sponsorManager: sponsorManager)
                .id("sponsors")
                .frame(maxWidth: .infinity, maxHeight: .infinity)
                .navigationSplitViewColumnWidth(min: 400, ideal: 600, max: .infinity)
        case .kubernetesPortForward:
            PortForwarderSidebarContent()
                .id("port-forwarder")
                .frame(maxWidth: .infinity, maxHeight: .infinity)
                .navigationSplitViewColumnWidth(min: 400, ideal: 600, max: .infinity)
        case .cloudflareTunnels:
            CloudflareTunnelsView()
                .id("cloudflare-tunnels")
                .frame(maxWidth: .infinity, maxHeight: .infinity)
                .navigationSplitViewColumnWidth(min: 400, ideal: 600, max: .infinity)
        default:
            VStack(spacing: 0) {
                PortTableView()

                // Status bar
                statusBar
            }
        }
    }

    @ViewBuilder
    private var detailView: some View {
        if appState.selectedSidebarItem == .settings || appState.selectedSidebarItem == .sponsors || appState.selectedSidebarItem == .cloudflareTunnels {
            EmptyView()
        } else if appState.selectedSidebarItem == .kubernetesPortForward {
            ConnectionLogPanel(connection: appState.selectedPortForwardConnection)
        } else if let selectedPort = appState.selectedPort {
            PortDetailView(port: selectedPort)
        } else {
            ContentUnavailableView {
                Label("No Port Selected", systemImage: "network.slash")
            } description: {
                Text("Select a port from the list to view details")
            }
        }
    }

    private var statusBar: some View {
        HStack {
            // Port count
            Group {
                if appState.filter.isActive || appState.selectedSidebarItem != .allPorts {
                    Text("\(appState.filteredPorts.count) of \(appState.ports.count) ports")
                } else {
                    Text("\(appState.ports.count) ports listening")
                }
            }
            .font(.caption)
            .foregroundStyle(.secondary)

            Spacer()

            // Scanning indicator
            if appState.isScanning {
                ProgressView()
                    .controlSize(.small)
                Text("Scanning...")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 8)
        .background(Color(nsColor: .windowBackgroundColor))
    }

    @ToolbarContentBuilder
    private var toolbarContent: some ToolbarContent {
        ToolbarItemGroup(placement: .primaryAction) {
            Button {
                Task {
                    await appState.refresh()
                }
            } label: {
                Label("Refresh", systemImage: "arrow.clockwise")
            }
            .keyboardShortcut("r", modifiers: .command)
            .disabled(appState.isScanning)
            .help("Refresh port list (Cmd+R)")

            Button {
                appState.selectedSidebarItem = .settings
            } label: {
                Label("Settings", systemImage: "gear")
            }
            .keyboardShortcut(",", modifiers: .command)
            .help("Open Settings (Cmd+,)")
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortDetailView.swift`
```
import SwiftUI

struct PortDetailView: View {
    let port: PortInfo
    @Environment(AppState.self) private var appState
    @State private var showKillConfirmation = false

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                // Header
                header

                Divider()

                // Details Grid
                detailsGrid

                Divider()

                // Command
                commandSection

                Divider()

                // Actions
                actionsSection
            }
            .padding()
        }
        .confirmationDialog(
            "Kill Process",
            isPresented: $showKillConfirmation
        ) {
            Button("Kill Process", role: .destructive) {
                Task {
                    await appState.killPort(port)
                }
            }
            Button("Force Kill (SIGKILL)", role: .destructive) {
                Task {
                    await appState.killPort(port)
                }
            }
            Button("Deep Kill (+ Connections)", role: .destructive) {
                Task {
                    await appState.killPortDeep(port)
                }
            }
            Button("Cancel", role: .cancel) {}
        } message: {
            Text("Are you sure you want to kill \(port.processName) on port \(String(port.port))?")
        }
    }

    private var header: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack(spacing: 12) {
                ZStack {
                    Circle()
                        .fill(port.processType.color.opacity(0.2))
                        .frame(width: 48, height: 48)
                    Image(systemName: port.processType.icon)
                        .font(.title2)
                        .foregroundStyle(port.processType.color)
                }

                VStack(alignment: .leading, spacing: 4) {
                    Text(port.processName)
                        .font(.title2)
                        .fontWeight(.semibold)
                        .lineLimit(1)

                    HStack(spacing: 4) {
                        Text("Port \(String(port.port))")
                            .font(.subheadline)
                            .foregroundStyle(.secondary)

                        if let label = appState.portLabel(for: port.port) {
                            Text("·")
                                .foregroundStyle(.secondary)
                            Text(label)
                                .font(.subheadline)
                                .foregroundStyle(.orange)
                        }
                    }
                }

                Spacer()
            }

            HStack(spacing: 8) {
                Text(port.processType.rawValue)
                    .font(.caption)
                    .padding(.horizontal, 8)
                    .padding(.vertical, 4)
                    .background(port.processType.color.opacity(0.2))
                    .foregroundStyle(port.processType.color)
                    .clipShape(Capsule())

                if appState.isFavorite(port.port) {
                    HStack(spacing: 4) {
                        Image(systemName: "star.fill")
                        Text("Favorite")
                    }
                    .font(.caption)
                    .padding(.horizontal, 8)
                    .padding(.vertical, 4)
                    .background(.yellow.opacity(0.2))
                    .foregroundStyle(.yellow)
                    .clipShape(Capsule())
                }

                if appState.isWatching(port.port) {
                    HStack(spacing: 4) {
                        Image(systemName: "eye.fill")
                        Text("Watching")
                    }
                    .font(.caption)
                    .padding(.horizontal, 8)
                    .padding(.vertical, 4)
                    .background(.blue.opacity(0.2))
                    .foregroundStyle(.blue)
                    .clipShape(Capsule())
                }

                Spacer()
            }
        }
    }

    private var detailsGrid: some View {
        LazyVGrid(columns: [
            GridItem(.flexible()),
            GridItem(.flexible())
        ], alignment: .leading, spacing: 16) {
            DetailRow(title: "Port", value: String(port.port))
            DetailRow(title: "Label", value: appState.portLabel(for: port.port) ?? "—")
            DetailRow(title: "PID", value: String(port.pid))
            DetailRow(title: "Address", value: port.address)
            DetailRow(title: "User", value: port.user)
            DetailRow(title: "File Descriptor", value: port.fd)
            DetailRow(title: "Type", value: port.processType.rawValue)
        }
    }

    private var commandSection: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Text("Command")
                    .font(.headline)
                Spacer()
                Button {
                    NSPasteboard.general.clearContents()
                    NSPasteboard.general.setString(port.command, forType: .string)
                } label: {
                    Label("Copy", systemImage: "doc.on.doc")
                        .font(.caption)
                }
                .buttonStyle(.bordered)
                .controlSize(.small)
            }

            Text(port.command.count > AppConstants.maxCommandLength
                ? String(port.command.prefix(AppConstants.maxCommandLength)) + "..."
                : port.command)
                .font(.system(.caption, design: .monospaced))
                .foregroundStyle(.secondary)
                .textSelection(.enabled)
                .padding(12)
                .frame(maxWidth: .infinity, alignment: .leading)
                .background(Color(nsColor: .textBackgroundColor))
                .clipShape(RoundedRectangle(cornerRadius: 8))
        }
    }

    private var actionsSection: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Actions")
                .font(.headline)

            VStack(spacing: 8) {
                FavoriteWatchButtons(portNumber: port.port, style: .labeled)

                // Tunnel section
                if port.isActive {
                    tunnelSection
                }

                Button(role: .destructive) {
                    showKillConfirmation = true
                } label: {
                    Text("Kill Process")
                        .frame(maxWidth: .infinity)
                }
                .buttonStyle(.borderedProminent)
                .tint(.red)
            }
        }
    }

    @ViewBuilder
    private var tunnelSection: some View {
        if !appState.tunnelManager.isCloudflaredInstalled {
            CloudflaredMissingBanner()
        } else if let tunnel = appState.tunnelManager.tunnelState(for: port.port) {
            TunnelStatusBadge(
                tunnel: tunnel,
                onCopyURL: {
                    appState.tunnelManager.copyURL(for: port.port)
                },
                onStop: {
                    appState.tunnelManager.stopTunnel(for: port.port)
                }
            )
        } else {
            Button {
                appState.tunnelManager.startTunnel(for: port.port, portInfoId: port.id)
            } label: {
                HStack {
                    Image(systemName: "cloud.fill")
                    Text("Share via Tunnel")
                }
                .frame(maxWidth: .infinity)
            }
            .buttonStyle(.bordered)
            .help("Create a public URL for this port via Cloudflare Tunnel")
        }
    }
}

struct DetailRow: View {
    let title: String
    let value: String

    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(title)
                .font(.caption)
                .foregroundStyle(.secondary)
            Text(value)
                .font(.body)
                .textSelection(.enabled)
        }
    }
}
```

## File: `platforms/macos/Sources/Views/SidebarView.swift`
```
import SwiftUI

struct SidebarView: View {
    @Environment(AppState.self) private var appState

    @State private var showAddFavoritePopover = false
    @State private var showAddWatchPopover = false

    var body: some View {
        @Bindable var state = appState

        List(selection: $state.selectedSidebarItem) {
            Section("Categories") {
                sidebarRow(.allPorts, count: appState.ports.count)

                // Favorites row with add button
                favoritesRow

                // Watched row with add button
                watchedRow
            }

            Section("Networking") {
                kubernetesPortForwardRow
                cloudflareTunnelsRow
            }

            Section("Process Types") {
                ForEach(ProcessType.allCases) { type in
                    sidebarRow(.processType(type), count: countForType(type))
                }
            }

            Section("Filters") {
                filterControls
            }

            Section {
                Label {
                    Text("Sponsors")
                } icon: {
                    Image(systemName: "heart.fill")
                        .foregroundStyle(.pink)
                }
                .tag(SidebarItem.sponsors)

                Label("Settings", systemImage: "gear")
                    .tag(SidebarItem.settings)
            }
        }
        .listStyle(.sidebar)
    }

    // MARK: - Favorites Row

    private var favoritesRow: some View {
        Label {
            HStack {
                Text("Favorites")
                Spacer()

                Button {
                    showAddFavoritePopover = true
                } label: {
                    Image(systemName: "plus.circle.fill")
                        .foregroundStyle(.secondary)
                }
                .buttonStyle(.plain)
                .help("Add Favorite Port")
                .popover(isPresented: $showAddFavoritePopover) {
                    AddPortPopover(mode: .favorite) { port, _, _ in
                        appState.favorites.insert(port)
                    }
                }

                Text("\(favoritesCount)")
                    .foregroundStyle(.secondary)
                    .font(.caption)
                    .frame(minWidth: 20)
            }
        } icon: {
            Image(systemName: "star.fill")
                .foregroundStyle(.yellow)
        }
        .tag(SidebarItem.favorites)
        .contextMenu {
            Button {
                showAddFavoritePopover = true
            } label: {
                Label("Add Port...", systemImage: "plus")
            }
        }
    }

    // MARK: - Watched Row

    private var watchedRow: some View {
        Label {
            HStack {
                Text("Watched")
                Spacer()

                Button {
                    showAddWatchPopover = true
                } label: {
                    Image(systemName: "plus.circle.fill")
                        .foregroundStyle(.secondary)
                }
                .buttonStyle(.plain)
                .help("Add Watched Port")
                .popover(isPresented: $showAddWatchPopover) {
                    AddPortPopover(mode: .watch) { port, onStart, onStop in
                        appState.watchedPorts.append(
                            WatchedPort(port: port, notifyOnStart: onStart, notifyOnStop: onStop)
                        )
                    }
                }

                Text("\(watchedCount)")
                    .foregroundStyle(.secondary)
                    .font(.caption)
                    .frame(minWidth: 20)
            }
        } icon: {
            Image(systemName: "eye.fill")
                .foregroundStyle(.blue)
        }
        .tag(SidebarItem.watched)
        .contextMenu {
            Button {
                showAddWatchPopover = true
            } label: {
                Label("Add Port...", systemImage: "plus")
            }
        }
    }

    // MARK: - Kubernetes Port Forward Row

    private var kubernetesPortForwardRow: some View {
        Label {
            HStack {
                Text("K8s Port Forward")
                Spacer()

                // Status indicator
                Circle()
                    .fill(appState.portForwardManager.allConnected && !appState.portForwardManager.connections.isEmpty ? Color.green : Color.secondary.opacity(0.3))
                    .frame(width: 8, height: 8)

                Text("\(appState.portForwardManager.connections.count)")
                    .foregroundStyle(.secondary)
                    .font(.caption)
                    .frame(minWidth: 20)
            }
        } icon: {
            Image(systemName: "point.3.connected.trianglepath.dotted")
                .foregroundStyle(.blue)
        }
        .tag(SidebarItem.kubernetesPortForward)
    }

    // MARK: - Cloudflare Tunnels Row

    private var cloudflareTunnelsRow: some View {
        Label {
            HStack {
                Text("Cloudflare Tunnels")
                Spacer()

                // Status indicator
                if appState.tunnelManager.activeTunnelCount > 0 {
                    Circle()
                        .fill(Color.green)
                        .frame(width: 8, height: 8)
                }

                Text("\(appState.tunnelManager.tunnels.count)")
                    .foregroundStyle(.secondary)
                    .font(.caption)
                    .frame(minWidth: 20)
            }
        } icon: {
            Image(systemName: "cloud.fill")
                .foregroundStyle(.orange)
        }
        .tag(SidebarItem.cloudflareTunnels)
    }

    // MARK: - Standard Row

    private func sidebarRow(_ item: SidebarItem, count: Int) -> some View {
        Label {
            HStack {
                Text(item.title)
                Spacer()
                Text("\(count)")
                    .foregroundStyle(.secondary)
                    .font(.caption)
            }
        } icon: {
            Image(systemName: item.icon)
        }
        .tag(item)
    }

    // MARK: - Filter Controls

    @ViewBuilder
    private var filterControls: some View {
        @Bindable var state = appState

        VStack(alignment: .leading, spacing: 12) {
            VStack(alignment: .leading, spacing: 4) {
                Text("Port Range")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                HStack(spacing: 8) {
                    TextField("Min", value: $state.filter.minPort, format: .number.grouping(.never))
                        .textFieldStyle(.roundedBorder)
                        .frame(width: 60)
                    Text("-")
                        .foregroundStyle(.secondary)
                    TextField("Max", value: $state.filter.maxPort, format: .number.grouping(.never))
                        .textFieldStyle(.roundedBorder)
                        .frame(width: 60)
                }
            }

            if appState.filter.isActive {
                Button("Reset Filters") {
                    appState.filter.reset()
                }
                .font(.caption)
            }
        }
        .padding(.vertical, 4)
    }

    // MARK: - Helpers

    private var favoritesCount: Int {
        appState.favorites.count
    }

    private var watchedCount: Int {
        appState.watchedPorts.count
    }

    private func countForType(_ type: ProcessType) -> Int {
        appState.ports.filter { $0.processType == type }.count
    }
}
```

## File: `platforms/macos/Sources/Views/SponsorsWindowView.swift`
```
import SwiftUI

// MARK: - Sponsors Page View (Full Page in Main Window)

struct SponsorsPageView: View {
    @Bindable var sponsorManager: SponsorManager

    private let columns = [
        GridItem(.adaptive(minimum: 80, maximum: 100), spacing: 16)
    ]

    private var activeSponsors: [Sponsor] {
        sponsorManager.sponsors.filter { $0.amount > 0 }
    }

    private var pastSponsors: [Sponsor] {
        sponsorManager.sponsors.filter { $0.amount <= 0 }
    }

    var body: some View {
        ScrollView {
            VStack(spacing: 24) {
                // Header
                HStack(spacing: 16) {
                    Image(systemName: "heart.fill")
                        .font(.system(size: 28))
                        .foregroundStyle(.pink)

                    VStack(alignment: .leading, spacing: 2) {
                        Text("Sponsors")
                            .font(.title2)
                            .fontWeight(.bold)

                        Text("Thank you for supporting PortKiller!")
                            .font(.subheadline)
                            .foregroundStyle(.secondary)
                    }

                    Spacer()

                    if let url = URL(string: AppInfo.githubSponsors) {
                        Link(destination: url) {
                            HStack(spacing: 6) {
                                Image(systemName: "heart.fill")
                                Text("Become a Sponsor")
                            }
                            .font(.callout)
                            .padding(.horizontal, 16)
                            .padding(.vertical, 8)
                        }
                        .buttonStyle(.borderedProminent)
                        .tint(.pink)
                    }
                }
                .padding(.horizontal, 24)
                .padding(.top, 20)

                // Sponsors Content
                if sponsorManager.sponsors.isEmpty && !sponsorManager.isLoading {
                    emptyState
                } else {
                    VStack(spacing: 24) {
                        // Active Sponsors
                        if !activeSponsors.isEmpty {
                            sponsorSection(
                                title: "Active Sponsors",
                                icon: "star.fill",
                                color: .yellow,
                                sponsors: activeSponsors
                            )
                        }
                        
                        // Contributors
                        if !sponsorManager.contributors.isEmpty {
                            contributorSection(
                                title: "Contributors",
                                icon: "hammer.fill",
                                color: .blue,
								contributors: sponsorManager.contributors
                            )
                        } else {
                            Text("No contributors found")
                        }
						
						// Past Sponsors
						if !pastSponsors.isEmpty {
							sponsorSection(
								title: "Past Sponsors",
								icon: "heart.fill",
								color: .secondary,
								sponsors: pastSponsors,
								dimmed: true
							)
						}
                    }
                }

            }
            .padding(.bottom, 24)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color(nsColor: .windowBackgroundColor))
        .task {
            if sponsorManager.sponsors.isEmpty {
                await sponsorManager.refreshSponsors()
            }
        }
    }

    private func sponsorSection(title: String, icon: String, color: Color, sponsors: [Sponsor], dimmed: Bool = false) -> some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack(spacing: 8) {
                Image(systemName: icon)
                    .foregroundStyle(color)
                Text(title)
                    .font(.headline)
                Text("(\(sponsors.count))")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
            .padding(.horizontal, 24)

            LazyVGrid(columns: columns, spacing: 16) {
                ForEach(sponsors) { sponsor in
                    SponsorCard(sponsor: sponsor, dimmed: dimmed)
                }
            }
            .padding(.horizontal, 24)
        }
    }
    
    private func contributorSection(title: String, icon: String, color: Color, contributors: [Contributor]) -> some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack(spacing: 8) {
                Image(systemName: icon)
                    .foregroundStyle(color)
                Text(title)
                    .font(.headline)
                Text("(\(contributors.count))")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
            .padding(.horizontal, 24)

            LazyVGrid(columns: columns, spacing: 16) {
                ForEach(contributors) { contributor in
                    ContributorCard(contributor: contributor)
                }
            }
            .padding(.horizontal, 24)
        }
    }

    private var emptyState: some View {
        VStack(spacing: 20) {
            if sponsorManager.error != nil {
                Image(systemName: "wifi.exclamationmark")
                    .font(.system(size: 50))
                    .foregroundStyle(.secondary)

                Text("Couldn't load sponsors")
                    .font(.title2)
                    .fontWeight(.medium)

                Button("Try Again") {
                    Task {
                        await sponsorManager.refreshSponsors()
                    }
                }
                .buttonStyle(.borderedProminent)
            } else {
                Image(systemName: "person.3.fill")
                    .font(.system(size: 50))
                    .foregroundStyle(.secondary)

                Text("Be the first sponsor!")
                    .font(.title2)
                    .fontWeight(.medium)

                if let url = URL(string: AppInfo.githubSponsors) {
                    Link("Become a Sponsor", destination: url)
                        .buttonStyle(.borderedProminent)
                        .tint(.pink)
                }
            }
        }
        .frame(maxWidth: .infinity)
        .padding(60)
    }
}

// MARK: - Sponsor Card

struct SponsorCard: View {
    let sponsor: Sponsor
    var dimmed: Bool = false
    @State private var isHovered = false
    @State private var hasSponsorPage = false

    var body: some View {
        VStack(spacing: 8) {
            AsyncImage(url: URL(string: sponsor.avatarUrl)) { phase in
                switch phase {
                case .success(let image):
                    image
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                case .failure:
                    Image(systemName: "person.circle.fill")
                        .resizable()
                        .foregroundStyle(.secondary)
                case .empty:
                    ProgressView()
                @unknown default:
                    EmptyView()
                }
            }
            .frame(width: 48, height: 48)
            .clipShape(Circle())
            .overlay(
                Circle()
                    .stroke(Color.secondary.opacity(0.2), lineWidth: 1)
            )
            .scaleEffect(isHovered ? 1.08 : 1.0)
            .opacity(dimmed ? 0.6 : 1.0)
            .grayscale(dimmed ? 0.5 : 0)

            Text(sponsor.displayName)
                .font(.caption)
                .fontWeight(.medium)
                .lineLimit(1)
                .truncationMode(.tail)
                .foregroundStyle(dimmed ? .secondary : .primary)
            
            Button {
                if hasSponsorPage {
                    if let url = URL(string: "https://github.com/sponsors/\(sponsor.login)") {
                        NSWorkspace.shared.open(url)
                    }
                } else {
                    if let url = sponsor.profileUrl {
                        NSWorkspace.shared.open(url)
                    }
                }
            } label: {
                HStack(spacing: 2) {
                    Image(systemName: hasSponsorPage ? "heart.fill" : "person.fill")
                        .font(.system(size: 8))
                    Text(hasSponsorPage ? "Sponsor" : "Visit")
                        .font(.system(size: 9, weight: .semibold))
                }
                .padding(.horizontal, 6)
                .padding(.vertical, 2)
            }
            .buttonStyle(.borderedProminent)
            .tint(hasSponsorPage ? .pink : .blue)
            .controlSize(.mini)
        }
        .frame(width: 80)
        .padding(10)
        .background(isHovered ? Color.primary.opacity(0.05) : Color.clear)
        .cornerRadius(8)
        .animation(.easeInOut(duration: 0.15), value: isHovered)
        .onHover { hovering in
            isHovered = hovering
        }
        .onTapGesture {
            if let url = sponsor.profileUrl {
                NSWorkspace.shared.open(url)
            }
        }
        .help("@\(sponsor.login)")
        .task {
            await checkSponsorPage()
        }
    }
    
    private func checkSponsorPage() async {
        guard let url = URL(string: "https://github.com/sponsors/\(sponsor.login)") else { return }
        var request = URLRequest(url: url)
        request.httpMethod = "HEAD"
        
        do {
            let (_, response) = try await URLSession.shared.data(for: request)
            if let httpResponse = response as? HTTPURLResponse {
                // GitHub returns 200 even for non-existent sponsor pages (redirects to profile)
                // We need to check if we got redirected
                if let url = httpResponse.url, url.absoluteString.contains("/sponsors/") {
                    hasSponsorPage = true
                } else {
                    hasSponsorPage = false
                }
            }
        } catch {
            // Ignore error, assume no sponsor page
        }
    }
}

// MARK: - Contributor Card

struct ContributorCard: View {
    let contributor: Contributor
    @State private var isHovered = false
    @State private var hasSponsorPage = false

    var body: some View {
        VStack(spacing: 8) {
            ZStack(alignment: .bottomTrailing) {
                AsyncImage(url: URL(string: contributor.avatarUrl)) { phase in
                    switch phase {
                    case .success(let image):
                        image
                            .resizable()
                            .aspectRatio(contentMode: .fill)
                    case .failure:
                        Image(systemName: "person.circle.fill")
                            .resizable()
                            .foregroundStyle(.secondary)
                    case .empty:
                        ProgressView()
                    @unknown default:
                        EmptyView()
                    }
                }
                .frame(width: 48, height: 48)
                .clipShape(Circle())
                .overlay(
                    Circle()
                        .stroke(Color.secondary.opacity(0.2), lineWidth: 1)
                )
                
                // Contributions badge
                if contributor.contributions > 0 {
                    Text("\(contributor.contributions)")
                        .font(.system(size: 10, weight: .bold))
                        .foregroundStyle(.white)
                        .padding(.horizontal, 4)
                        .padding(.vertical, 2)
                        .background(Color.blue)
                        .clipShape(Capsule())
                        .overlay(
                            Capsule()
                                .stroke(Color(nsColor: .windowBackgroundColor), lineWidth: 2)
                        )
                        .offset(x: 4, y: 4)
                }
            }
            .scaleEffect(isHovered ? 1.08 : 1.0)

            Text(contributor.login)
                .font(.caption)
                .fontWeight(.medium)
                .lineLimit(1)
                .truncationMode(.tail)
                
            Button {
                if hasSponsorPage {
                    if let url = URL(string: "https://github.com/sponsors/\(contributor.login)") {
                        NSWorkspace.shared.open(url)
                    }
                } else {
                    if let url = URL(string: contributor.htmlUrl) {
                        NSWorkspace.shared.open(url)
                    }
                }
            } label: {
                HStack(spacing: 2) {
                    Image(systemName: hasSponsorPage ? "heart.fill" : "person.fill")
                        .font(.system(size: 8))
                    Text(hasSponsorPage ? "Sponsor" : "Visit")
                        .font(.system(size: 9, weight: .semibold))
                }
                .padding(.horizontal, 6)
                .padding(.vertical, 2)
            }
            .buttonStyle(.borderedProminent)
            .tint(hasSponsorPage ? .pink : .blue)
            .controlSize(.mini)
        }
        .frame(width: 80)
        .padding(10)
        .background(isHovered ? Color.primary.opacity(0.05) : Color.clear)
        .cornerRadius(8)
        .animation(.easeInOut(duration: 0.15), value: isHovered)
        .onHover { hovering in
            isHovered = hovering
        }
        .onTapGesture {
            if let url = URL(string: contributor.htmlUrl) {
                NSWorkspace.shared.open(url)
            }
        }
        .help("@\(contributor.login)")
        .task {
            await checkSponsorPage()
        }
    }
    
    private func checkSponsorPage() async {
        guard let url = URL(string: "https://github.com/sponsors/\(contributor.login)") else { return }
        var request = URLRequest(url: url)
        request.httpMethod = "HEAD"
        
        do {
            let (_, response) = try await URLSession.shared.data(for: request)
            if let httpResponse = response as? HTTPURLResponse {
                // GitHub returns 200 even for non-existent sponsor pages (redirects to profile)
                // We need to check if we got redirected
                if let url = httpResponse.url, url.absoluteString.contains("/sponsors/") {
                    hasSponsorPage = true
                } else {
                    hasSponsorPage = false
                }
            }
        } catch {
            // Ignore error, assume no sponsor page
        }
    }
}

```

## File: `platforms/macos/Sources/Views/CloudflareTunnels/CloudflareTunnelsView.swift`
```
import SwiftUI

struct CloudflareTunnelsView: View {
    @Environment(AppState.self) private var appState

    var body: some View {
        VStack(spacing: 0) {
            // Header
            header

            Divider()

            // Dependency warning banner
            if !appState.tunnelManager.isCloudflaredInstalled {
                CloudflaredMissingBanner()
                Divider()
            }

            // Content
            if appState.tunnelManager.tunnels.isEmpty {
                emptyState
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
            } else {
                tunnelsList
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
            }

            Divider()

            // Status bar
            statusBar
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }

    // MARK: - Header

    private var header: some View {
        HStack {
            Text("Cloudflare Tunnels")
                .font(.headline)

            Spacer()

            if appState.tunnelManager.tunnels.count > 0 {
                Button {
                    Task {
                        await appState.tunnelManager.stopAllTunnels()
                    }
                } label: {
                    Label("Stop All", systemImage: "stop.fill")
                }
                .buttonStyle(.bordered)
                .controlSize(.small)
            }
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 8)
        .background(Color(nsColor: .windowBackgroundColor))
    }

    // MARK: - Empty State

    private var emptyState: some View {
        ContentUnavailableView {
            Label("No Active Tunnels", systemImage: "cloud")
        } description: {
            Text("Share a port via tunnel from the port list to create a public URL")
        }
    }

    // MARK: - Tunnels List

    private var tunnelsList: some View {
        ScrollView {
            LazyVStack(spacing: 0) {
                ForEach(appState.tunnelManager.tunnels) { tunnel in
                    CloudflareTunnelRow(tunnel: tunnel)
                    Divider()
                }
            }
        }
    }

    // MARK: - Status Bar

    private var statusBar: some View {
        HStack {
            if appState.tunnelManager.activeTunnelCount > 0 {
                Circle()
                    .fill(Color.green)
                    .frame(width: 8, height: 8)
                Text("\(appState.tunnelManager.activeTunnelCount) active tunnel(s)")
            } else {
                Text("No active tunnels")
            }

            Spacer()

            if appState.tunnelManager.isCloudflaredInstalled {
                Image(systemName: "checkmark.circle.fill")
                    .foregroundStyle(.green)
                Text("cloudflared installed")
            }
        }
        .font(.caption)
        .foregroundStyle(.secondary)
        .padding(.horizontal, 12)
        .padding(.vertical, 8)
        .background(Color(nsColor: .windowBackgroundColor))
    }
}

// MARK: - Tunnel Row

struct CloudflareTunnelRow: View {
    let tunnel: CloudflareTunnelState
    @Environment(AppState.self) private var appState
    @State private var isHovered = false
    @State private var isCopied = false
    @State private var showLogs = false

    var body: some View {
        VStack(spacing: 0) {
            HStack(spacing: 12) {
                // Status indicator
                statusIndicator

                // Port info
                VStack(alignment: .leading, spacing: 2) {
                    Text("Port " + String(tunnel.port))
                        .font(.headline)

                    if let url = tunnel.tunnelURL {
                        Text(url)
                            .font(.caption)
                            .foregroundStyle(.blue)
                            .lineLimit(1)
                    } else if tunnel.status == .starting {
                        Text("Starting tunnel...")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    } else if let error = tunnel.lastError {
                        Text(error)
                            .font(.caption)
                            .foregroundStyle(.red)
                            .lineLimit(1)
                    }
                }

                Spacer()

                // Actions
                if tunnel.status == .active, tunnel.tunnelURL != nil {
                    actionButtons
                } else if tunnel.status == .starting {
                    ProgressView()
                        .controlSize(.small)
                }

                // Log toggle
                Button {
                    showLogs.toggle()
                } label: {
                    Image(systemName: "doc.text")
                        .foregroundColor(showLogs ? .accentColor : .secondary)
                }
                .buttonStyle(.plain)
                .help(showLogs ? "Hide logs" : "Show logs")

                // Stop button
                Button {
                    appState.tunnelManager.stopTunnel(id: tunnel.id)
                } label: {
                    Image(systemName: "xmark.circle.fill")
                        .foregroundStyle(.red)
                }
                .buttonStyle(.plain)
                .help("Stop tunnel")
            }
            .padding(.horizontal, 12)
            .padding(.vertical, 10)

            if showLogs {
                Divider()
                TunnelLogView(tunnel: tunnel)
                    .frame(height: 200)
            }
        }
        .background(isHovered ? Color.primary.opacity(0.05) : Color.clear)
        .onHover { hovering in
            isHovered = hovering
        }
        .contextMenu {
            if tunnel.status == .active, let url = tunnel.tunnelURL {
                Button {
                    ClipboardService.copy(url)
                } label: {
                    Label("Copy URL", systemImage: "doc.on.doc")
                }

                Button {
                    if let tunnelURL = URL(string: url) {
                        NSWorkspace.shared.open(tunnelURL)
                    }
                } label: {
                    Label("Open in Browser", systemImage: "globe")
                }

                Divider()
            }

            Button {
                showLogs.toggle()
            } label: {
                Label(showLogs ? "Hide Logs" : "Show Logs", systemImage: "doc.text")
            }

            Divider()

            Button(role: .destructive) {
                appState.tunnelManager.stopTunnel(id: tunnel.id)
            } label: {
                Label("Stop Tunnel", systemImage: "stop.fill")
            }
        }
    }

    private var statusIndicator: some View {
        Circle()
            .fill(statusColor)
            .frame(width: 10, height: 10)
    }

    private var statusColor: Color {
        switch tunnel.status {
        case .idle: .secondary
        case .starting: .yellow
        case .active: .green
        case .stopping: .yellow
        case .error: .red
        }
    }

    private var actionButtons: some View {
        HStack(spacing: 8) {
            Button {
                if let url = tunnel.tunnelURL {
                    ClipboardService.copy(url)
                    isCopied = true
                    Task {
                        try? await Task.sleep(for: .seconds(1.5))
                        isCopied = false
                    }
                }
            } label: {
                Image(systemName: isCopied ? "checkmark" : "doc.on.doc")
            }
            .buttonStyle(.bordered)
            .controlSize(.small)
            .help("Copy URL")

            Button {
                if let url = tunnel.tunnelURL, let tunnelURL = URL(string: url) {
                    NSWorkspace.shared.open(tunnelURL)
                }
            } label: {
                Image(systemName: "globe")
            }
            .buttonStyle(.bordered)
            .controlSize(.small)
            .help("Open in Browser")
        }
    }
}
```

## File: `platforms/macos/Sources/Views/CloudflareTunnels/TunnelLogView.swift`
```
import SwiftUI

struct TunnelLogView: View {
    let tunnel: CloudflareTunnelState
    @State private var searchText = ""
    @State private var filterLevel: TunnelLogEntry.LogLevel?

    private var filteredLogs: [TunnelLogEntry] {
        var logs = tunnel.logs
        if let level = filterLevel {
            logs = logs.filter { $0.level == level }
        }
        if !searchText.isEmpty {
            logs = logs.filter { $0.message.localizedCaseInsensitiveContains(searchText) }
        }
        return logs
    }

    private static let timeFormatter: DateFormatter = {
        let f = DateFormatter()
        f.dateFormat = "HH:mm:ss.SSS"
        return f
    }()

    var body: some View {
        VStack(spacing: 0) {
            // Toolbar
            HStack(spacing: 8) {
                Image(systemName: "magnifyingglass")
                    .foregroundStyle(.secondary)
                TextField("Search logs...", text: $searchText)
                    .textFieldStyle(.plain)

                Spacer()

                // Level filter
                Picker("", selection: $filterLevel) {
                    Text("All").tag(nil as TunnelLogEntry.LogLevel?)
                    Text("Requests").tag(TunnelLogEntry.LogLevel.request as TunnelLogEntry.LogLevel?)
                    Text("Errors").tag(TunnelLogEntry.LogLevel.error as TunnelLogEntry.LogLevel?)
                    Text("Warnings").tag(TunnelLogEntry.LogLevel.warning as TunnelLogEntry.LogLevel?)
                }
                .pickerStyle(.segmented)
                .frame(width: 280)

                Text("\(filteredLogs.count) entries")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .frame(width: 70, alignment: .trailing)

                Button {
                    tunnel.clearLogs()
                } label: {
                    Image(systemName: "trash")
                }
                .buttonStyle(.plain)
                .foregroundStyle(.secondary)
                .help("Clear logs")
            }
            .padding(.horizontal, 12)
            .padding(.vertical, 6)
            .background(Color(nsColor: .controlBackgroundColor))

            Divider()

            // Log entries
            if filteredLogs.isEmpty {
                ContentUnavailableView {
                    Label("No Logs", systemImage: "doc.text")
                } description: {
                    Text(tunnel.logs.isEmpty ? "Logs will appear here as requests come in" : "No logs match the current filter")
                }
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            } else {
                ScrollViewReader { proxy in
                    ScrollView {
                        LazyVStack(alignment: .leading, spacing: 0) {
                            ForEach(filteredLogs) { entry in
                                logEntryRow(entry)
                                    .id(entry.id)
                            }
                        }
                    }
                    .onChange(of: tunnel.logs.count) { _, _ in
                        if let last = filteredLogs.last {
                            proxy.scrollTo(last.id, anchor: .bottom)
                        }
                    }
                }
            }
        }
    }

    private func logEntryRow(_ entry: TunnelLogEntry) -> some View {
        HStack(alignment: .top, spacing: 8) {
            // Timestamp
            Text(Self.timeFormatter.string(from: entry.timestamp))
                .font(.system(.caption2, design: .monospaced))
                .foregroundStyle(.tertiary)
                .frame(width: 80, alignment: .leading)

            // Level indicator
            Circle()
                .fill(levelColor(entry.level))
                .frame(width: 6, height: 6)
                .padding(.top, 4)

            // Message
            Text(entry.message)
                .font(.system(.caption, design: .monospaced))
                .foregroundStyle(entry.level == .error ? .red : .primary)
                .lineLimit(3)
                .textSelection(.enabled)
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 3)
    }

    private func levelColor(_ level: TunnelLogEntry.LogLevel) -> Color {
        switch level {
        case .info: .secondary
        case .warning: .orange
        case .error: .red
        case .request: .blue
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Components/AddPortPopover.swift`
```
import SwiftUI
import AppKit

struct AddPortPopover: View {
    enum Mode {
        case favorite
        case watch
    }

    let mode: Mode
    let onAdd: (Int, Bool, Bool) -> Void

    @State private var portText = ""
    @State private var notifyOnStart = true
    @State private var notifyOnStop = true
    @Environment(\.dismiss) private var dismiss
    @FocusState private var isTextFieldFocused: Bool

    private var isValidPort: Bool {
        guard let port = Int(portText) else { return false }
        return port > 0 && port <= 65535
    }

    private var title: String {
        mode == .favorite ? "Add Favorite Port" : "Add Watched Port"
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text(title)
                .font(.headline)

            TextField("Port (1-65535)", text: $portText)
                .textFieldStyle(.roundedBorder)
                .focused($isTextFieldFocused)
                .onSubmit {
                    if isValidPort {
                        handleAdd()
                    }
                }

            if mode == .watch {
                VStack(alignment: .leading, spacing: 8) {
                    Toggle("Notify when port starts", isOn: $notifyOnStart)
                        .toggleStyle(.checkbox)

                    Toggle("Notify when port stops", isOn: $notifyOnStop)
                        .toggleStyle(.checkbox)
                }
                .padding(.vertical, 4)
            }

            HStack {
                Button("Cancel") {
                    dismiss()
                }
                .keyboardShortcut(.escape, modifiers: [])

                Spacer()

                Button("Add") {
                    handleAdd()
                }
                .keyboardShortcut(.return, modifiers: [])
                .disabled(!isValidPort || (mode == .watch && !notifyOnStart && !notifyOnStop))
                .buttonStyle(.borderedProminent)
            }
        }
        .padding()
        .frame(width: 280)
        .onAppear {
            // Make popover window key so TextField can receive focus
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.05) {
                NSApp.activate(ignoringOtherApps: true)
                if let window = NSApp.keyWindow {
                    window.makeKey()
                }
                isTextFieldFocused = true
            }
        }
    }

    private func handleAdd() {
        guard let port = Int(portText), port > 0, port <= 65535 else { return }
        onAdd(port, notifyOnStart, notifyOnStop)
        dismiss()
    }
}
```

## File: `platforms/macos/Sources/Views/Components/CloudflaredMissingBanner.swift`
```
import SwiftUI

struct CloudflaredMissingBanner: View {
    @Environment(AppState.self) private var appState
    @State private var isCopied = false
    @State private var isInstalling = false
    @State private var installError: String?

    private let installCommand = "brew install cloudflared"

    /// Check if Homebrew is installed
    private var brewPath: String? {
        let paths = ["/opt/homebrew/bin/brew", "/usr/local/bin/brew"]
        return paths.first { FileManager.default.fileExists(atPath: $0) }
    }

    private var isBrewInstalled: Bool {
        brewPath != nil
    }

    var body: some View {
        VStack(spacing: 0) {
            HStack(spacing: 12) {
                Image(systemName: "cloud.fill")
                    .foregroundStyle(.blue)

                VStack(alignment: .leading, spacing: 2) {
                    Text("cloudflared Required")
                        .font(.headline)
                    if !isBrewInstalled {
                        Text("Homebrew is required. Visit brew.sh to install.")
                            .font(.caption)
                            .foregroundStyle(.orange)
                    } else {
                        Text("Install cloudflared to share ports via Cloudflare Tunnel")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }

                Spacer()

                // Refresh button to re-check installation
                Button {
                    appState.tunnelManager.recheckInstallation()
                } label: {
                    Image(systemName: "arrow.clockwise")
                }
                .buttonStyle(.plain)
                .help("Check if installed")

                if isBrewInstalled {
                    // Copy command button
                    Button {
                        ClipboardService.copy(installCommand)
                        isCopied = true
                        Task {
                            try? await Task.sleep(for: .seconds(2))
                            isCopied = false
                        }
                    } label: {
                        Image(systemName: isCopied ? "checkmark" : "doc.on.doc")
                    }
                    .buttonStyle(.bordered)
                    .help(isCopied ? "Copied!" : "Copy command")

                    // Install button
                    Button {
                        installCloudflared()
                    } label: {
                        if isInstalling {
                            ProgressView()
                                .scaleEffect(0.7)
                                .frame(width: 16, height: 16)
                            Text("Installing...")
                        } else {
                            Label("Install", systemImage: "arrow.down.circle")
                        }
                    }
                    .buttonStyle(.borderedProminent)
                    .disabled(isInstalling)
                } else {
                    // Open brew.sh button
                    Button {
                        if let url = URL(string: "https://brew.sh") {
                            NSWorkspace.shared.open(url)
                        }
                    } label: {
                        Label("Get Homebrew", systemImage: "safari")
                    }
                    .buttonStyle(.borderedProminent)
                }
            }
            .padding(12)

            // Error message
            if let error = installError {
                HStack {
                    Image(systemName: "exclamationmark.triangle.fill")
                        .foregroundStyle(.red)
                    Text(error)
                        .font(.caption)
                        .foregroundStyle(.red)
                    Spacer()
                    Button("Dismiss") {
                        installError = nil
                    }
                    .font(.caption)
                    .buttonStyle(.plain)
                }
                .padding(.horizontal, 12)
                .padding(.bottom, 8)
            }
        }
        .background(Color.blue.opacity(0.1))
        .overlay(
            Rectangle()
                .fill(Color.blue)
                .frame(height: 2),
            alignment: .top
        )
    }

    private func installCloudflared() {
        guard let brewPath = brewPath else { return }

        isInstalling = true
        installError = nil

        Task.detached(priority: .userInitiated) {
            let process = Process()
            process.executableURL = URL(fileURLWithPath: brewPath)
            process.arguments = ["install", "cloudflared"]

            let pipe = Pipe()
            process.standardOutput = pipe
            process.standardError = pipe

            do {
                try process.run()
                process.waitUntilExit()

                // Use autoreleasepool to prevent memory accumulation
                var errorOutput: String = ""
                if process.terminationStatus != 0 {
                    autoreleasepool {
                        let data = pipe.fileHandleForReading.readDataToEndOfFile()
                        errorOutput = String(data: data, encoding: .utf8) ?? "Unknown error"
                    }
                }

                await MainActor.run {
                    isInstalling = false
                    if process.terminationStatus == 0 {
                        appState.tunnelManager.recheckInstallation()
                    } else {
                        installError = "Installation failed: \(errorOutput.prefix(100))"
                    }
                }
            } catch {
                await MainActor.run {
                    isInstalling = false
                    installError = "Failed to run brew: \(error.localizedDescription)"
                }
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Components/DependencyWarningBanner.swift`
```
import SwiftUI

struct DependencyWarningBanner: View {
    @State private var isInstalling = false

    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: "exclamationmark.triangle.fill")
                .foregroundStyle(.orange)

            VStack(alignment: .leading, spacing: 2) {
                Text("Missing Dependencies")
                    .font(.headline)
                Text("kubectl is required for port forwarding")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }

            Spacer()

            if isInstalling {
                ProgressView()
                    .scaleEffect(0.8)
            } else {
                Button("Install") {
                    installDependencies()
                }
                .buttonStyle(.bordered)
            }
        }
        .padding(12)
        .background(Color.orange.opacity(0.1))
        .overlay(
            Rectangle()
                .fill(Color.orange)
                .frame(height: 2),
            alignment: .top
        )
    }

    private func installDependencies() {
        isInstalling = true
        Task {
            _ = await DependencyChecker.shared.checkAndInstallMissing()
            await MainActor.run { isInstalling = false }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Components/FavoriteWatchButtons.swift`
```
/**
 * FavoriteWatchButtons.swift
 * PortKiller
 *
 * Reusable favorite and watch toggle buttons for ports.
 * Supports icon-only and labeled button styles.
 */

import SwiftUI

/// Style for favorite/watch buttons
enum FavoriteWatchButtonStyle {
    /// Icon-only button with plain style (for rows)
    case iconOnly
    /// Labeled button with bordered style (for detail views)
    case labeled
}

/// Favorite toggle button for a port
struct FavoriteButton: View {
    let portNumber: Int
    let style: FavoriteWatchButtonStyle

    @Environment(AppState.self) private var appState

    init(portNumber: Int, style: FavoriteWatchButtonStyle = .iconOnly) {
        self.portNumber = portNumber
        self.style = style
    }

    private var isFavorite: Bool {
        appState.isFavorite(portNumber)
    }

    var body: some View {
        switch style {
        case .iconOnly:
            Button {
                appState.toggleFavorite(portNumber)
            } label: {
                Image(systemName: isFavorite ? "star.fill" : "star")
                    .foregroundStyle(isFavorite ? .yellow : .secondary)
            }
            .buttonStyle(.plain)
            .help("Toggle favorite")

        case .labeled:
            Button {
                appState.toggleFavorite(portNumber)
            } label: {
                Text(isFavorite ? "Remove Favorite" : "Add Favorite")
                    .frame(maxWidth: .infinity)
            }
            .buttonStyle(.bordered)
        }
    }
}

/// Watch toggle button for a port
struct WatchButton: View {
    let portNumber: Int
    let style: FavoriteWatchButtonStyle

    @Environment(AppState.self) private var appState

    init(portNumber: Int, style: FavoriteWatchButtonStyle = .iconOnly) {
        self.portNumber = portNumber
        self.style = style
    }

    private var isWatching: Bool {
        appState.isWatching(portNumber)
    }

    var body: some View {
        switch style {
        case .iconOnly:
            Button {
                appState.toggleWatch(portNumber)
            } label: {
                Image(systemName: isWatching ? "eye.fill" : "eye")
                    .foregroundStyle(isWatching ? .blue : .secondary)
            }
            .buttonStyle(.plain)
            .help("Toggle watch")

        case .labeled:
            Button {
                appState.toggleWatch(portNumber)
            } label: {
                Text(isWatching ? "Stop Watching" : "Watch")
                    .frame(maxWidth: .infinity)
            }
            .buttonStyle(.bordered)
        }
    }
}

/// Combined favorite and watch buttons in a horizontal stack
struct FavoriteWatchButtons: View {
    let portNumber: Int
    let style: FavoriteWatchButtonStyle
    let spacing: CGFloat

    @Environment(AppState.self) private var appState

    init(
        portNumber: Int,
        style: FavoriteWatchButtonStyle = .iconOnly,
        spacing: CGFloat = 8
    ) {
        self.portNumber = portNumber
        self.style = style
        self.spacing = spacing
    }

    var body: some View {
        HStack(spacing: spacing) {
            FavoriteButton(portNumber: portNumber, style: style)
            WatchButton(portNumber: portNumber, style: style)
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Components/LabeledField.swift`
```
import SwiftUI

struct LabeledField<Content: View>: View {
    let label: String
    let content: () -> Content

    init(_ label: String, @ViewBuilder content: @escaping () -> Content) {
        self.label = label
        self.content = content
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(label)
                .font(.caption)
                .foregroundStyle(.secondary)
            content()
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Components/NestedPortRow.swift`
```
/// NestedPortListRow - Individual port row within expanded process group
///
/// Thin wrapper around PortRowView with nested style.
/// Maintains backward compatibility with existing usage.

import SwiftUI

struct NestedPortListRow: View {
    let port: PortInfo

    var body: some View {
        PortRowView(port: port, style: .nested)
    }
}
```

## File: `platforms/macos/Sources/Views/Components/PortContextMenu.swift`
```
/**
 * PortContextMenu.swift
 * PortKiller
 *
 * Shared context menu for port rows across the app.
 * Provides consistent actions for favorites, watching, clipboard, browser, tunnels, and kill.
 */

import SwiftUI

/// Configuration for PortContextMenu to enable/disable specific sections
struct PortContextMenuOptions {
    var includeCopyPortNumber: Bool = true
    var includeCopyCommand: Bool = true
    var includeKillAction: Bool = true
    var includeTunnelActions: Bool = true
    var includeBrowserActions: Bool = true

    static let full = PortContextMenuOptions()
    static let minimal = PortContextMenuOptions(
        includeCopyPortNumber: false,
        includeCopyCommand: false,
        includeKillAction: false,
        includeTunnelActions: false
    )
    static let menuBar = PortContextMenuOptions(
        includeCopyPortNumber: false,
        includeCopyCommand: false,
        includeKillAction: false
    )
    static let nested = PortContextMenuOptions(
        includeCopyPortNumber: false,
        includeCopyCommand: false,
        includeKillAction: false
    )
}

/// Shared context menu component for port actions
struct PortContextMenu: View {
    let port: PortInfo
    let options: PortContextMenuOptions

    @Environment(AppState.self) private var appState

    init(port: PortInfo, options: PortContextMenuOptions = .full) {
        self.port = port
        self.options = options
    }

    var body: some View {
        Group {
            // Favorite & Watch Section
            favoriteWatchSection

            // Copy Section
            if options.includeCopyPortNumber || (options.includeCopyCommand && port.isActive) {
                Divider()
                copySection
            }

            // Process Type Override
            if port.isActive {
                Divider()
                processTypeSection
            }

            // Kill Action
            if options.includeKillAction && port.isActive {
                Divider()
                killSection
            }

            // Browser Section
            if options.includeBrowserActions {
                Divider()
                browserSection
            }

            // Tunnel Section
            if options.includeTunnelActions && port.isActive {
                Divider()
                tunnelSection
            }
        }
    }

    // MARK: - Sections

    @ViewBuilder
    private var favoriteWatchSection: some View {
        Button {
            appState.toggleFavorite(port.port)
        } label: {
            Label(
                appState.isFavorite(port.port) ? "Remove from Favorites" : "Add to Favorites",
                systemImage: appState.isFavorite(port.port) ? "star.slash" : "star"
            )
        }

        Button {
            appState.toggleWatch(port.port)
        } label: {
            Label(
                appState.isWatching(port.port) ? "Stop Watching" : "Watch Port",
                systemImage: appState.isWatching(port.port) ? "eye.slash" : "eye"
            )
        }

        Divider()

        Button {
            appState.promptForPortLabel(port: port.port)
        } label: {
            Label(
                appState.portLabel(for: port.port) != nil ? "Edit Label" : "Set Label",
                systemImage: "pencil"
            )
        }

        if appState.portLabel(for: port.port) != nil {
            Button {
                appState.removePortLabel(for: port.port)
            } label: {
                Label("Remove Label", systemImage: "pencil.slash")
            }
        }
    }

    @ViewBuilder
    private var processTypeSection: some View {
        Menu {
            ForEach(ProcessType.allCases) { type in
                Button {
                    appState.setProcessTypeOverride(processName: port.processName, type: type)
                } label: {
                    HStack {
                        Label(type.rawValue, systemImage: type.icon)
                        if port.processType == type {
                            Image(systemName: "checkmark")
                        }
                    }
                }
            }

            if appState.processTypeOverride(for: port.processName) != nil {
                Divider()
                Button {
                    appState.clearProcessTypeOverride(processName: port.processName)
                } label: {
                    Label("Reset to Auto", systemImage: "arrow.counterclockwise")
                }
            }
        } label: {
            Label("Set Process Type", systemImage: "tag")
        }
    }

    @ViewBuilder
    private var copySection: some View {
        if options.includeCopyPortNumber {
            Button {
                NSPasteboard.general.clearContents()
                NSPasteboard.general.setString(String(port.port), forType: .string)
            } label: {
                Label("Copy Port Number", systemImage: "doc.on.doc")
            }
        }

        if options.includeCopyCommand && port.isActive {
            Button {
                NSPasteboard.general.clearContents()
                NSPasteboard.general.setString(port.command, forType: .string)
            } label: {
                Label("Copy Command", systemImage: "doc.on.doc")
            }
        }
    }

    @ViewBuilder
    private var killSection: some View {
        Button(role: .destructive) {
            Task {
                await appState.killPort(port)
            }
        } label: {
            Label("Kill Process", systemImage: "xmark.circle")
        }
        .keyboardShortcut(.delete, modifiers: [])

        Button(role: .destructive) {
            Task {
                await appState.killPortDeep(port)
            }
        } label: {
            Label("Deep Kill (+ Connections)", systemImage: "xmark.circle.fill")
        }
    }

    @ViewBuilder
    private var browserSection: some View {
        Button {
            if let url = URL(string: "http://localhost:\(port.port)") {
                NSWorkspace.shared.open(url)
            }
        } label: {
            Label("Open in Browser", systemImage: "globe.fill")
        }
        .keyboardShortcut("o", modifiers: .command)

        Button {
            NSPasteboard.general.clearContents()
            NSPasteboard.general.setString("http://localhost:\(port.port)", forType: .string)
        } label: {
            Label("Copy URL", systemImage: "document.on.clipboard")
        }
    }

    @ViewBuilder
    private var tunnelSection: some View {
        if appState.tunnelManager.isCloudflaredInstalled {
            if let tunnel = appState.tunnelManager.tunnelState(for: port.port) {
                if tunnel.status == .active, let url = tunnel.tunnelURL {
                    Button {
                        ClipboardService.copy(url)
                    } label: {
                        Label("Copy Tunnel URL", systemImage: "doc.on.doc")
                    }

                    Button {
                        if let tunnelURL = URL(string: url) {
                            NSWorkspace.shared.open(tunnelURL)
                        }
                    } label: {
                        Label("Open Tunnel URL", systemImage: "globe")
                    }
                }

                Button {
                    appState.tunnelManager.stopTunnel(for: port.port)
                } label: {
                    Label("Stop Tunnel", systemImage: "icloud.slash")
                }
            } else {
                Button {
                    appState.tunnelManager.startTunnel(for: port.port, portInfoId: port.id)
                } label: {
                    Label("Share via Tunnel", systemImage: "cloud.fill")
                }
            }
        } else {
            Button {
                ClipboardService.copy("brew install cloudflared")
            } label: {
                Label("Copy: brew install cloudflared", systemImage: "doc.on.doc")
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Components/ProcessGroupRow.swift`
```
/// ProcessGroupRow - Collapsible process group row for tree view
///
/// Displays a process group header with:
/// - Expand/collapse chevron
/// - Status indicator (active/killing)
/// - Process name with PID
/// - Port count badge
/// - Kill all ports button
///
/// - Note: Used in tree view to group multiple ports under one process.
/// - Important: Handles killing all ports in the group.

import SwiftUI

struct ProcessGroupListRow: View {
    let group: ProcessGroup
    let isExpanded: Bool
    let onToggleExpand: () -> Void
    @Environment(AppState.self) private var appState
    @State private var isHovered = false
    @State private var showConfirm = false
    @State private var isKilling = false

    var body: some View {
        HStack(spacing: 0) {
            // Indent/Expand toggle (aligned with Port column of header)
            HStack(spacing: 0) {
                Image(systemName: isExpanded ? "chevron.down" : "chevron.right")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .frame(width: 20, height: 20)
            }
            .frame(width: 70, alignment: .leading)
            .padding(.leading, 24)

            // Process Name (aligned with Process column of header)
            HStack(spacing: 6) {
                // Status indicator
                Circle()
                    .fill(isKilling ? .orange : .green)
                    .frame(width: 8, height: 8)
                    .opacity(isKilling ? 0.3 : 1)
                    .animation(.easeInOut(duration: 0.4).repeatForever(autoreverses: true), value: isKilling)

                Text(group.processName)
                    .font(.system(.body, design: .rounded))
                    .fontWeight(.medium)
            }
            .frame(width: 150, alignment: .leading)

            // PID(s) (aligned with PID column of header)
            Text(group.pids.count == 1 ? "\(group.pids[0])" : "\(group.pids.count) PIDs")
                .font(.system(.body, design: .monospaced))
                .foregroundStyle(.secondary)
                .frame(width: 70, alignment: .leading)
                .help(group.pids.map(String.init).joined(separator: ", "))

            // Port Count Badge (aligned with Type column of header effectively)
            if !showConfirm {
                Text("\(group.ports.count) ports")
                    .font(.caption2)
                    .padding(.horizontal, 6)
                    .padding(.vertical, 2)
                    .background(Color.secondary.opacity(0.1))
                    .foregroundStyle(.secondary)
                    .clipShape(Capsule())
                    .frame(width: 100, alignment: .leading)
            } else {
                Spacer().frame(width: 100)
            }

            Spacer()

            // Actions
            if showConfirm {
                HStack(spacing: 4) {
                    Button {
                        showConfirm = false
                        isKilling = true
                        Task {
                            for port in group.ports {
                                await appState.killPort(port)
                            }
                        }
                    } label: {
                        Image(systemName: "checkmark.circle.fill")
                            .foregroundStyle(.green)
                    }
                    .buttonStyle(.plain)

                    Button {
                        showConfirm = false
                    } label: {
                        Image(systemName: "xmark.circle.fill")
                            .foregroundStyle(.secondary)
                    }
                    .buttonStyle(.plain)
                }
                .frame(width: 80)
                .padding(.trailing, 16)
            } else {
                Button {
                    showConfirm = true
                } label: {
                    Image(systemName: "xmark.circle.fill")
                        .foregroundStyle(.red)
                }
                .buttonStyle(.plain)
                .opacity(isHovered ? 1 : 0)
                .help("Kill Process Tree")
                .frame(width: 80)
                .padding(.trailing, 16)
            }
        }
        .padding(.vertical, 6)
        .background(isHovered ? Color.primary.opacity(0.05) : Color.clear)
        .contentShape(Rectangle())
        .onHover { hovering in
            isHovered = hovering
        }
        .onTapGesture {
            onToggleExpand()
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Components/TunnelStatusBadge.swift`
```
import SwiftUI

struct TunnelStatusBadge: View {
    let tunnel: CloudflareTunnelState
    let onCopyURL: () -> Void
    let onStop: () -> Void

    var body: some View {
        HStack(spacing: 8) {
            // Main content area
            HStack(spacing: 8) {
                // Status indicator
                Circle()
                    .fill(statusColor)
                    .frame(width: 8, height: 8)

                if tunnel.status == .active, let url = tunnel.tunnelURL {
                    Text(shortenedURL(url))
                        .font(.body)
                        .foregroundStyle(.primary)
                        .lineLimit(1)
                } else if tunnel.status == .starting || tunnel.status == .stopping {
                    ProgressView()
                        .controlSize(.small)
                    Text(tunnel.status == .starting ? "Starting tunnel..." : "Stopping...")
                        .font(.body)
                        .foregroundStyle(.secondary)
                } else if tunnel.status == .error {
                    Image(systemName: "exclamationmark.triangle.fill")
                        .foregroundStyle(.red)
                    Text(tunnel.lastError ?? "Tunnel error")
                        .font(.body)
                        .foregroundStyle(.red)
                        .lineLimit(1)
                }
            }
            .frame(maxWidth: .infinity, alignment: .leading)

            // Action buttons
            if tunnel.status == .active {
                Button {
                    onCopyURL()
                } label: {
                    Image(systemName: "doc.on.doc")
                }
                .buttonStyle(.borderless)
                .help("Copy tunnel URL")
            }

            Button {
                onStop()
            } label: {
                Image(systemName: "xmark.circle.fill")
                    .foregroundStyle(tunnel.status == .active ? .red : .secondary)
            }
            .buttonStyle(.borderless)
            .help(tunnel.status == .error ? "Dismiss" : "Stop tunnel")
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 8)
        .frame(maxWidth: .infinity)
        .background {
            RoundedRectangle(cornerRadius: 6)
                .fill(Color(nsColor: .controlBackgroundColor))
        }
        .overlay {
            RoundedRectangle(cornerRadius: 6)
                .strokeBorder(Color(nsColor: .separatorColor), lineWidth: 0.5)
        }
    }

    private var statusColor: Color {
        switch tunnel.status {
        case .idle: .secondary
        case .starting: .orange
        case .active: .green
        case .stopping: .orange
        case .error: .red
        }
    }

    private func shortenedURL(_ url: String) -> String {
        url.replacingOccurrences(of: "https://", with: "")
    }
}
```

## File: `platforms/macos/Sources/Views/Components/PortRow/PortRowComponents.swift`
```
/**
 * PortRowComponents.swift
 * PortKiller
 *
 * Composable building blocks for port row displays.
 * These components can be combined to create different row layouts.
 */

import SwiftUI

// MARK: - Status Indicator

/// Displays active/inactive status as a colored circle
struct PortStatusIndicator: View {
    let isActive: Bool
    var size: CGFloat = 8

    var body: some View {
        Circle()
            .fill(isActive ? Color.green : Color.gray)
            .frame(width: size, height: size)
    }
}

// MARK: - Port Number Display

/// Displays port number in monospaced font with optional custom label
struct PortNumberDisplay: View {
    let port: Int
    let isActive: Bool
    var font: Font = .system(.body, design: .monospaced)
    var fontWeight: Font.Weight = .medium
    var showLabel: Bool = true

    @Environment(AppState.self) private var appState

    var body: some View {
        HStack(spacing: 4) {
            Text(String(port))
                .font(font)
                .fontWeight(fontWeight)
                .opacity(isActive ? 1 : 0.6)

            if showLabel, let label = appState.portLabel(for: port) {
                Text(label)
                    .font(.caption)
                    .foregroundStyle(.orange)
                    .lineLimit(1)
            }
        }
    }
}

// MARK: - Favorite/Watch Indicators

/// Shows favorite and watch status as small icons (read-only indicators)
struct PortStatusBadges: View {
    let portNumber: Int
    var fontSize: Font = .caption2

    @Environment(AppState.self) private var appState

    var body: some View {
        HStack(spacing: 4) {
            if appState.isFavorite(portNumber) {
                Image(systemName: "star.fill")
                    .font(fontSize)
                    .foregroundStyle(.yellow)
            }
            if appState.isWatching(portNumber) {
                Image(systemName: "eye.fill")
                    .font(fontSize)
                    .foregroundStyle(.blue)
            }
        }
    }
}

// MARK: - Process Info

/// Displays process name with type icon
struct PortProcessInfo: View {
    let processName: String
    let processType: ProcessType
    let isActive: Bool
    var showIcon: Bool = true

    var body: some View {
        HStack(spacing: 6) {
            if showIcon {
                Image(systemName: processType.icon)
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
            Text(processName)
                .lineLimit(1)
                .foregroundStyle(isActive ? .primary : .secondary)
        }
    }
}

// MARK: - Type Badge

/// Displays process type as a colored capsule badge
struct PortTypeBadge: View {
    let processType: ProcessType
    let isActive: Bool
    var font: Font = .caption
    var horizontalPadding: CGFloat = 6
    var verticalPadding: CGFloat = 2

    var body: some View {
        if isActive {
            Text(processType.rawValue)
                .font(font)
                .padding(.horizontal, horizontalPadding)
                .padding(.vertical, verticalPadding)
                .background(processType.color.opacity(0.15))
                .foregroundStyle(processType.color)
                .clipShape(Capsule())
        } else {
            Text("Inactive")
                .font(font)
                .padding(.horizontal, horizontalPadding)
                .padding(.vertical, verticalPadding)
                .background(Color.gray.opacity(0.15))
                .foregroundStyle(.secondary)
                .clipShape(Capsule())
        }
    }
}

// MARK: - Kill Button

/// Kill/Remove button for ports
struct PortKillButton: View {
    let port: PortInfo
    var onRemove: (() -> Void)?

    @Environment(AppState.self) private var appState

    var body: some View {
        if port.isActive {
            Button {
                Task {
                    await appState.killPort(port)
                }
            } label: {
                Image(systemName: "xmark.circle.fill")
                    .foregroundStyle(.red)
            }
            .buttonStyle(.plain)
            .help("Kill process")
        } else if let onRemove {
            Button {
                onRemove()
            } label: {
                Image(systemName: "trash")
                    .foregroundStyle(.red)
            }
            .buttonStyle(.plain)
            .help("Remove from list")
        }
    }
}

// MARK: - Actions Group

/// Combined action buttons for port rows
struct PortRowActions: View {
    let port: PortInfo
    var showFavorite: Bool = true
    var showWatch: Bool = true
    var showKill: Bool = true
    var onRemove: (() -> Void)?

    @Environment(AppState.self) private var appState

    var body: some View {
        HStack(spacing: 8) {
            if showFavorite {
                FavoriteButton(portNumber: port.port)
            }
            if showWatch {
                WatchButton(portNumber: port.port)
            }
            if showKill {
                PortKillButton(port: port, onRemove: onRemove)
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Components/PortRow/PortRowView.swift`
```
/**
 * PortRowView.swift
 * PortKiller
 *
 * Unified port row component that supports multiple display styles.
 * Replaces PortListRow, NestedPortListRow, MenuBarPortRow, MenuBarNestedPortRow.
 */

import SwiftUI
import Defaults

/// Style configuration for PortRowView
enum PortRowStyle {
    /// Full table view row with all columns
    case table
    /// Nested row within a process group (indented)
    case nested
    /// Compact row for menu bar
    case menuBar
    /// Minimal nested row for menu bar
    case menuBarNested
}

/// Configuration for kill confirmation behavior
enum KillConfirmationMode {
    /// No confirmation, kill immediately
    case immediate
    /// Show inline confirmation UI
    case inline(confirmingKill: Binding<String?>)
}

/// Unified port row view supporting multiple display styles
struct PortRowView: View {
    let port: PortInfo
    let style: PortRowStyle
    var killMode: KillConfirmationMode = .immediate
    var contextMenuOptions: PortContextMenuOptions = .full

    @Environment(AppState.self) private var appState
    @State private var isHovered = false
    @State private var isKilling = false

    var body: some View {
        content
            .background(rowBackground)
            .contentShape(Rectangle())
            .onHover { isHovered = $0 }
            .contextMenu {
                PortContextMenu(port: port, options: contextMenuOptionsForStyle)
            }
    }

    // MARK: - Content by Style

    @ViewBuilder
    private var content: some View {
        switch style {
        case .table:
            tableRowContent
        case .nested:
            nestedRowContent
        case .menuBar:
            menuBarRowContent
        case .menuBarNested:
            menuBarNestedContent
        }
    }

    // MARK: - Table Row (Full)

    private var tableRowContent: some View {
        HStack(spacing: 0) {
            // Favorite
            FavoriteButton(portNumber: port.port)
                .frame(width: 40, alignment: .center)

            // Status indicator
            PortStatusIndicator(isActive: port.isActive)
                .padding(.trailing, 8)

            // Port
            PortNumberDisplay(port: port.port, isActive: port.isActive)
                .frame(width: 70, alignment: .leading)

            // Process
            PortProcessInfo(
                processName: port.processName,
                processType: port.processType,
                isActive: port.isActive
            )
            .frame(minWidth: 150, maxWidth: .infinity, alignment: .leading)

            // PID
            Text(port.isActive ? String(port.pid) : "-")
                .font(.system(.body, design: .monospaced))
                .foregroundStyle(.secondary)
                .frame(width: 70, alignment: .leading)

            // Type
            PortTypeBadge(processType: port.processType, isActive: port.isActive)
                .frame(width: 100, alignment: .leading)

            // Address
            Text(port.address)
                .font(.caption)
                .foregroundStyle(.secondary)
                .frame(width: 80, alignment: .leading)

            // User
            Text(port.user)
                .font(.caption)
                .foregroundStyle(.secondary)
                .frame(width: 70, alignment: .leading)

            Spacer()

            // Actions
            HStack(spacing: 8) {
                WatchButton(portNumber: port.port)
                PortKillButton(port: port, onRemove: removeFromList)
            }
            .frame(width: 80)
        }
        .padding(.leading, 16)
        .padding(.trailing, 16)
        .padding(.vertical, 8)
    }

    // MARK: - Nested Row

    private var nestedRowContent: some View {
        HStack(spacing: 0) {
            // Indent + Status + Port
            HStack(spacing: 4) {
                Color.clear.frame(width: 20)
                PortStatusIndicator(isActive: port.isActive, size: 6)
                PortNumberDisplay(port: port.port, isActive: port.isActive)
            }
            .frame(width: 90, alignment: .leading)
            .padding(.leading, 24)

            // Tree connector
            Text("└─")
                .foregroundStyle(.tertiary)
                .frame(width: 20, alignment: .trailing)

            // Indicators
            PortStatusBadges(portNumber: port.port)
                .frame(width: 130, alignment: .leading)

            // PID placeholder
            Text("-")
                .font(.system(.body, design: .monospaced))
                .foregroundStyle(.tertiary)
                .frame(width: 70, alignment: .leading)

            // Type
            if port.isActive {
                PortTypeBadge(
                    processType: port.processType,
                    isActive: port.isActive,
                    font: .caption2
                )
                .frame(width: 100, alignment: .leading)
            } else {
                Spacer().frame(width: 100)
            }

            // Address
            Text(port.address)
                .font(.caption)
                .foregroundStyle(.secondary)
                .frame(width: 80, alignment: .leading)

            // User
            Text(port.user)
                .font(.caption)
                .foregroundStyle(.secondary)
                .frame(width: 70, alignment: .leading)

            Spacer()

            // Actions
            PortRowActions(port: port, showFavorite: true, showWatch: true, showKill: true)
                .frame(width: 80)
                .opacity(isHovered ? 1 : 0)
                .padding(.trailing, 16)
        }
        .padding(.vertical, 4)
    }

    // MARK: - Menu Bar Row

    private var menuBarRowContent: some View {
        HStack(spacing: 10) {
            // Status with glow
            Circle()
                .fill(isKilling ? .orange : .green)
                .frame(width: 6, height: 6)
                .shadow(color: (isKilling ? Color.orange : Color.green).opacity(0.5), radius: 3)
                .opacity(isKilling ? 0.5 : 1)
                .animation(.easeInOut(duration: 0.3), value: isKilling)

            if case .inline(let confirmingKill) = killMode, confirmingKill.wrappedValue == port.id {
                menuBarConfirmContent(confirmingKill: confirmingKill)
            } else {
                menuBarNormalContent
            }
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 8)
    }

    @ViewBuilder
    private func menuBarConfirmContent(confirmingKill: Binding<String?>) -> some View {
        Text("Kill \(port.processName)?")
            .font(.callout)
            .lineLimit(1)
        Spacer()
        HStack(spacing: 4) {
            Button("Kill") {
                isKilling = true
                confirmingKill.wrappedValue = nil
                Task { await appState.killPort(port) }
            }
            .buttonStyle(.borderedProminent)
            .tint(.red)
            .controlSize(.small)

            Button("Cancel") {
                confirmingKill.wrappedValue = nil
            }
            .buttonStyle(.bordered)
            .controlSize(.small)
        }
    }

    private var menuBarNormalContent: some View {
        Group {
            // Port + indicators
            HStack(spacing: 3) {
                if appState.isFavorite(port.port) {
                    Image(systemName: "star.fill")
                        .font(.caption2)
                        .foregroundStyle(.yellow)
                }
                Text(port.displayPort)
                    .font(.system(.body, design: .monospaced))
                    .fontWeight(.medium)
                    .lineLimit(1)
                if appState.isWatching(port.port) {
                    Image(systemName: "eye.fill")
                        .font(.caption2)
                        .foregroundStyle(.blue)
                }
            }
            .frame(width: 100, alignment: .leading)
            .opacity(isKilling ? 0.5 : 1)

            // Process name + label
            HStack(spacing: 4) {
                Text(port.processName)
                    .font(.callout)
                    .lineLimit(1)
                if let label = appState.portLabel(for: port.port) {
                    Text("(\(label))")
                        .font(.caption)
                        .foregroundStyle(.orange)
                        .lineLimit(1)
                }
            }
            .opacity(isKilling ? 0.5 : 1)

            Spacer()

            // PID
            Text("PID \(String(port.pid))")
                .font(.caption)
                .foregroundStyle(.secondary)
                .opacity(isKilling ? 0.5 : 1)

            // Kill button or loading
            if isKilling {
                Image(systemName: "hourglass")
                    .foregroundStyle(.orange)
            } else if case .inline(let confirmingKill) = killMode {
                Button {
                    if Defaults[.skipKillConfirmation] {
                        isKilling = true
                        Task { await appState.killPort(port) }
                    } else {
                        confirmingKill.wrappedValue = port.id
                    }
                } label: {
                    Image(systemName: "xmark.circle.fill")
                        .foregroundStyle(.red)
                }
                .buttonStyle(.plain)
                .opacity(isHovered ? 1 : 0)
            }
        }
    }

    // MARK: - Menu Bar Nested

    private var menuBarNestedContent: some View {
        HStack(spacing: 10) {
            Rectangle().fill(.clear).frame(width: 32)
            Text(port.displayPort)
                .font(.system(.callout, design: .monospaced))
                .frame(width: 60, alignment: .leading)
            Text("\(port.address) • \(port.displayPort)")
                .font(.caption)
                .foregroundStyle(.secondary)
                .lineLimit(1)
            Spacer()
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 6)
    }

    // MARK: - Helpers

    private var rowBackground: some View {
        Group {
            switch style {
            case .table:
                isHovered ? Color.primary.opacity(0.05) : Color.clear
            case .nested:
                isHovered ? Color.primary.opacity(0.03) : Color.clear
            case .menuBar:
                (isHovered || isConfirming) ? Color.primary.opacity(0.05) : Color.clear
            case .menuBarNested:
                Color.clear
            }
        }
    }

    private var isConfirming: Bool {
        if case .inline(let confirmingKill) = killMode {
            return confirmingKill.wrappedValue == port.id
        }
        return false
    }

    private var contextMenuOptionsForStyle: PortContextMenuOptions {
        switch style {
        case .table:
            return .full
        case .nested:
            return .nested
        case .menuBar:
            return .menuBar
        case .menuBarNested:
            return .minimal
        }
    }

    private func removeFromList() {
        if appState.isFavorite(port.port) {
            appState.favorites.remove(port.port)
        }
        if appState.isWatching(port.port) {
            appState.toggleWatch(port.port)
        }
    }
}
```

## File: `platforms/macos/Sources/Views/MenuBar/MenuBarActions.swift`
```
/// MenuBarActions - Action buttons at bottom of menu bar
///
/// Provides menu items for:
/// - Opening main window
/// - Refresh, view toggle
/// - Kill all processes
/// - Settings and quit actions
///
/// - Note: Uses MenuItemButton for consistent styling.
/// - Important: Handles window activation for menu bar apps.

import SwiftUI

struct MenuBarActions: View {
    @Binding var confirmingKillAll: Bool
    @Binding var useTreeView: Bool
    @Bindable var state: AppState
    let openWindow: OpenWindowAction

    var body: some View {
        VStack(spacing: 0) {
            MenuItemButton(title: "Refresh", icon: "arrow.clockwise", shortcut: "R") {
                Task { await state.refresh() }
            }

            MenuItemButton(
                title: useTreeView ? "List View" : "Tree View",
                icon: useTreeView ? "list.bullet" : "list.bullet.indent",
                shortcut: "T"
            ) {
                useTreeView.toggle()
            }

            if confirmingKillAll {
                HStack {
                    Text("Kill all \(state.ports.count) processes?")
                        .font(.callout)
                    Spacer()
                    Button("Kill") {
                        Task { await state.killAll() }
                        confirmingKillAll = false
                    }
                    .buttonStyle(.borderedProminent)
                    .tint(.red)
                    .controlSize(.small)
                    Button("Cancel") { confirmingKillAll = false }
                        .buttonStyle(.bordered)
                        .controlSize(.small)
                }
                .padding(.horizontal, 12)
                .padding(.vertical, 6)
            } else {
                MenuItemButton(title: "Kill All", icon: "xmark.circle", shortcut: "K", isDestructive: true) {
                    confirmingKillAll = true
                }
                .disabled(state.ports.isEmpty)
            }

            Divider()
                .padding(.vertical, 4)

            MenuItemButton(title: "Open PortKiller", icon: "macwindow", shortcut: "O") {
                openWindow(id: "main")
                Task { @MainActor in
                    try? await Task.sleep(for: .milliseconds(100))
                    bringMainWindowToFront()
                }
            }

            MenuItemButton(title: "Settings...", icon: "gear", shortcut: ",") {
                state.selectedSidebarItem = .settings
                openWindow(id: "main")
                Task { @MainActor in
                    try? await Task.sleep(for: .milliseconds(100))
                    bringMainWindowToFront()
                }
            }

            MenuItemButton(title: "Quit PortKiller", icon: "power", shortcut: "Q") {
                NSApplication.shared.terminate(nil)
            }
        }
        .padding(.vertical, 4)
    }
}

// MARK: - Menu Item Button

/// Styled button component for menu bar actions
struct MenuItemButton: View {
    let title: String
    let icon: String
    var shortcut: String? = nil
    var isDestructive: Bool = false
    let action: () -> Void

    @State private var isHovered = false

    var body: some View {
        Button(action: action) {
            HStack(spacing: 8) {
                Image(systemName: icon)
                    .frame(width: 16)
                    .foregroundStyle(isDestructive ? .red : .primary)
                Text(title)
                    .foregroundStyle(isDestructive ? .red : .primary)
                Spacer()
                if let shortcut = shortcut {
                    Text("⌘\(shortcut)")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
            }
            .padding(.horizontal, 12)
            .padding(.vertical, 6)
            .contentShape(Rectangle())
            .background(isHovered ? Color.accentColor : Color.clear)
            .foregroundStyle(isHovered ? .white : .primary)
        }
        .buttonStyle(.plain)
        .onHover { hovering in
            isHovered = hovering
        }
    }
}

// MARK: - Helper Functions

/// Brings the main window to front for menu bar apps
@MainActor
private func bringMainWindowToFront() {
    // For menu bar apps, we need to set activation policy to regular temporarily
    NSApp.setActivationPolicy(.regular)
    NSApp.activate(ignoringOtherApps: true)

    // Find the main window (not menu bar extra)
    for window in NSApp.windows {
        // Skip menu bar extra windows
        if window.level == .popUpMenu || window.level == .statusBar {
            continue
        }
        if window.canBecomeMain {
            window.makeKeyAndOrderFront(nil)
            window.orderFrontRegardless()
            return
        }
    }
}
```

## File: `platforms/macos/Sources/Views/MenuBar/MenuBarHeader.swift`
```
/// MenuBarHeader - Search bar and port count indicator
///
/// Displays a search field for filtering ports and shows the current
/// count of visible ports as a badge.
///
/// - Note: Uses SwiftUI TextField with clear button support.

import SwiftUI

struct MenuBarHeader: View {
    @Binding var searchText: String
    let portCount: Int

    var body: some View {
        HStack(spacing: 8) {
            Image(systemName: "network")
                .foregroundStyle(.secondary)
            HStack(spacing: 4) {
                Image(systemName: "magnifyingglass")
                    .foregroundStyle(.tertiary)
                    .font(.caption)
                TextField("Search...", text: $searchText)
                    .textFieldStyle(.plain)
                    .font(.callout)
                if !searchText.isEmpty {
                    Button { searchText = "" } label: {
                        Image(systemName: "xmark.circle.fill")
                            .foregroundStyle(.tertiary)
                    }
                    .buttonStyle(.plain)
                }
            }
            .padding(.horizontal, 6)
            .padding(.vertical, 4)
            .background(.quaternary)
            .cornerRadius(6)
            Text("\(portCount)")
                .font(.caption2)
                .foregroundStyle(.secondary)
                .padding(.horizontal, 5)
                .padding(.vertical, 2)
                .background(.tertiary.opacity(0.3))
                .clipShape(Capsule())
        }
        .padding(.horizontal, 10)
        .padding(.vertical, 8)
    }
}
```

## File: `platforms/macos/Sources/Views/MenuBar/MenuBarNestedPortRow.swift`
```
/// MenuBarNestedPortRow - Minimal nested port row for menu bar
///
/// Thin wrapper around PortRowView with menuBarNested style.
/// Injects AppState into environment for PortRowView.

import SwiftUI

struct MenuBarNestedPortRow: View {
    let port: PortInfo
    @Bindable var state: AppState

    var body: some View {
        PortRowView(port: port, style: .menuBarNested)
            .environment(state)
    }
}
```

## File: `platforms/macos/Sources/Views/MenuBar/MenuBarPortForwardRow.swift`
```
import SwiftUI

struct MenuBarPortForwardRow: View {
    let connection: PortForwardConnectionState
    @Bindable var state: AppState
    @State private var isHovered = false

    private var statusColor: Color {
        if connection.portForwardStatus == .error || connection.proxyStatus == .error {
            return .red
        } else if connection.isFullyConnected {
            return .green
        } else if connection.portForwardStatus == .connecting || connection.proxyStatus == .connecting {
            return .orange
        }
        return .secondary.opacity(0.3)
    }

    var body: some View {
        HStack(spacing: 10) {
            Circle().fill(statusColor).frame(width: 6, height: 6)
                .shadow(color: connection.isFullyConnected ? .green.opacity(0.5) : .clear, radius: 3)
            Text(":" + String(connection.effectivePort))
                .font(.system(.callout, design: .monospaced)).fontWeight(.medium)
                .frame(width: 55, alignment: .leading)
            Text(connection.config.name).font(.callout).lineLimit(1)
            Spacer()
            Button {
                if connection.isFullyConnected {
                    state.portForwardManager.stopConnection(connection.id)
                } else if connection.portForwardStatus != .connecting && connection.proxyStatus != .connecting {
                    state.portForwardManager.startConnection(connection.id)
                }
            } label: {
                HStack(spacing: 3) {
                    if connection.portForwardStatus == .connecting || connection.proxyStatus == .connecting {
                        ProgressView().scaleEffect(0.5).frame(width: 12, height: 12)
                    } else {
                        Image(systemName: connection.isFullyConnected ? "stop.fill" : "play.fill")
                    }
                    Text(connection.isFullyConnected ? "Stop" : "Start")
                }
                .font(.caption)
                .foregroundStyle(connection.isFullyConnected ? .red : .green)
            }
            .buttonStyle(.bordered).controlSize(.small)
            .opacity(isHovered ? 1 : 0.6)
            .disabled(connection.portForwardStatus == .connecting || connection.proxyStatus == .connecting)
        }
        .padding(.horizontal, 12).padding(.vertical, 8)
        .background(isHovered ? Color.primary.opacity(0.05) : Color.clear)
        .contentShape(Rectangle())
        .onHover { isHovered = $0 }
        .contextMenu {
            Button { state.portForwardManager.restartConnection(connection.id) } label: { Label("Restart", systemImage: "arrow.clockwise") }
            Divider()
            Button { if let url = URL(string: "http://localhost:" + String(connection.effectivePort)) { NSWorkspace.shared.open(url) } } label: { Label("Open in Browser", systemImage: "globe.fill") }
            Button { NSPasteboard.general.clearContents(); NSPasteboard.general.setString("http://localhost:" + String(connection.effectivePort), forType: .string) } label: { Label("Copy URL", systemImage: "document.on.clipboard") }
            Divider()
            Button(role: .destructive) { state.portForwardManager.removeConnection(connection.id) } label: { Label("Remove", systemImage: "trash") }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/MenuBar/MenuBarPortList.swift`
```
/// MenuBarPortList - Scrollable port list container
///
/// Manages the display of ports in either list or tree view mode.
/// Shows an empty state when no ports are found.
/// Includes Kubernetes port-forward connections at the top.
///
/// - Note: Uses LazyVStack for performance with large port lists.
/// - Important: Tree view groups ports by process, list view shows flat list.

import SwiftUI

struct MenuBarPortList: View {
    let filteredPorts: [PortInfo]
    let filteredPortForwardConnections: [PortForwardConnectionState]
    let groupedByProcess: [ProcessGroup]
    let useTreeView: Bool
    @Binding var expandedProcesses: Set<String>
    @Binding var confirmingKillPort: String?
    @Bindable var state: AppState

    var body: some View {
        ScrollView {
            LazyVStack(spacing: 0) {
                // Active Cloudflare Tunnels
                if !state.tunnelManager.tunnels.isEmpty {
                    sectionHeader("Cloudflare Tunnels", icon: "cloud.fill", color: .orange)

                    ForEach(state.tunnelManager.tunnels) { tunnel in
                        MenuBarTunnelRow(tunnel: tunnel, state: state)
                    }
                }

                // Port Forward connections grouped by namespace
                if !filteredPortForwardConnections.isEmpty {
                    sectionHeader("K8s Port Forward", icon: "point.3.connected.trianglepath.dotted", color: .blue)

                    ForEach(connectionsByNamespace, id: \.namespace) { group in
                        namespaceHeader(group.namespace, count: group.connections.count)
                        ForEach(group.connections) { connection in
                            MenuBarPortForwardRow(connection: connection, state: state)
                        }
                    }
                }

                // Normal ports
                if filteredPorts.isEmpty && filteredPortForwardConnections.isEmpty && state.tunnelManager.tunnels.isEmpty {
                    emptyState
                } else if !filteredPorts.isEmpty {
                    sectionHeader("Local Ports", icon: "network", color: .green)

                    if useTreeView {
                        treeView
                    } else {
                        listView
                    }
                }
            }
        }
        .frame(height: 400)
    }

    private func sectionHeader(_ title: String, icon: String, color: Color) -> some View {
        HStack(spacing: 6) {
            Image(systemName: icon)
                .font(.caption2)
                .foregroundStyle(color)
            Text(title)
                .font(.caption)
                .fontWeight(.semibold)
                .foregroundStyle(.secondary)
            Spacer()
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 6)
        .background(Color.primary.opacity(0.03))
    }

    private var connectionsByNamespace: [(namespace: String, connections: [PortForwardConnectionState])] {
        let grouped = Dictionary(grouping: filteredPortForwardConnections) { $0.config.namespace }
        return grouped.map { (namespace: $0.key, connections: $0.value) }
            .sorted { $0.namespace < $1.namespace }
    }

    private func namespaceHeader(_ namespace: String, count: Int) -> some View {
        HStack(spacing: 4) {
            Image(systemName: "folder.fill")
                .font(.caption2)
                .foregroundStyle(.tertiary)
            Text(namespace)
                .font(.caption2)
                .foregroundStyle(.tertiary)
            Text("(\(count))")
                .font(.caption2)
                .foregroundStyle(.quaternary)
            Spacer()
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 4)
    }

    /// Empty state shown when no ports are found
    private var emptyState: some View {
        VStack(spacing: 8) {
            Image(systemName: "network.slash")
                .font(.largeTitle)
                .foregroundStyle(.secondary)
            Text("No open ports")
                .foregroundStyle(.secondary)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 40)
    }

    /// Tree view groups ports by process
    private var treeView: some View {
        ForEach(groupedByProcess) { group in
            MenuBarProcessGroupRow(
                group: group,
                isExpanded: expandedProcesses.contains(group.id),
                onToggleExpand: {
                    if expandedProcesses.contains(group.id) {
                        expandedProcesses.remove(group.id)
                    } else {
                        expandedProcesses.insert(group.id)
                    }
                },
                onKillProcess: {
                    for port in group.ports {
                        Task { await state.killPort(port) }
                    }
                },
                state: state
            )
        }
    }

    /// List view shows flat list of ports
    private var listView: some View {
        ForEach(filteredPorts) { port in
            MenuBarPortRow(port: port, state: state, confirmingKill: $confirmingKillPort)
        }
    }
}
```

## File: `platforms/macos/Sources/Views/MenuBar/MenuBarPortRow.swift`
```
/// MenuBarPortRow - Compact port row for menu bar
///
/// Thin wrapper around PortRowView with menuBar style.
/// Injects AppState into environment for PortRowView.

import SwiftUI

struct MenuBarPortRow: View {
    let port: PortInfo
    @Bindable var state: AppState
    @Binding var confirmingKill: String?

    var body: some View {
        PortRowView(
            port: port,
            style: .menuBar,
            killMode: .inline(confirmingKill: $confirmingKill)
        )
        .environment(state)
    }
}
```

## File: `platforms/macos/Sources/Views/MenuBar/MenuBarProcessGroupRow.swift`
```
import SwiftUI

struct MenuBarProcessGroupRow: View {
    let group: ProcessGroup
    let isExpanded: Bool
    let onToggleExpand: () -> Void
    let onKillProcess: () -> Void
    @Bindable var state: AppState
    @State private var showConfirm = false
    @State private var isHovered = false
    @State private var isKilling = false

    var body: some View {
        VStack(spacing: 0) {
            HStack(spacing: 10) {
                Image(systemName: isExpanded ? "chevron.down" : "chevron.right").font(.caption).foregroundStyle(.secondary)
                Circle().fill(isKilling ? .orange : .green).frame(width: 6, height: 6)
                    .shadow(color: (isKilling ? Color.orange : Color.green).opacity(0.5), radius: 3)
                    .opacity(isKilling ? 0.5 : 1).animation(.easeInOut(duration: 0.3), value: isKilling)
                HStack(spacing: 4) {
                    if group.ports.contains(where: { state.isFavorite($0.port) }) { Image(systemName: "star.fill").font(.caption2).foregroundStyle(.yellow) }
                    Text(group.processName).font(.callout).fontWeight(.medium).lineLimit(1)
                    if group.ports.contains(where: { state.isWatching($0.port) }) { Image(systemName: "eye.fill").font(.caption2).foregroundStyle(.blue) }
                }
                Spacer()
                Text(group.pids.count == 1 ? "PID \(group.pids[0])" : "\(group.pids.count) PIDs").font(.caption2).foregroundStyle(.secondary)
                if !(isHovered || showConfirm) {
                    Text("\(group.ports.count)").font(.caption2).foregroundStyle(.secondary).padding(.horizontal, 5).background(.tertiary.opacity(0.5)).clipShape(Capsule())
                } else if !showConfirm {
                    Button { showConfirm = true } label: { Image(systemName: "xmark.circle.fill").foregroundStyle(.red) }.buttonStyle(.plain)
                }
                if showConfirm {
                    HStack(spacing: 4) {
                        Button { showConfirm = false; isKilling = true; onKillProcess() } label: { Image(systemName: "checkmark.circle.fill").foregroundStyle(.green) }.buttonStyle(.plain)
                        Button { showConfirm = false } label: { Image(systemName: "xmark.circle.fill").foregroundStyle(.secondary) }.buttonStyle(.plain)
                    }
                }
            }
            .padding(.horizontal, 12).padding(.vertical, 8)
            .background(isHovered ? Color.primary.opacity(0.05) : Color.clear)
            .contentShape(Rectangle()).onHover { isHovered = $0 }.onTapGesture { onToggleExpand() }
            if isExpanded { ForEach(group.ports) { port in MenuBarNestedPortRow(port: port, state: state) } }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/MenuBar/MenuBarTunnelRow.swift`
```
import SwiftUI

struct MenuBarTunnelRow: View {
    let tunnel: CloudflareTunnelState
    @Bindable var state: AppState
    @State private var isHovered = false
    @State private var isCopied = false

    private var statusColor: Color {
        switch tunnel.status {
        case .idle: .secondary.opacity(0.3)
        case .starting: .orange
        case .active: .green
        case .stopping: .orange
        case .error: .red
        }
    }

    var body: some View {
        HStack(spacing: 10) {
            Circle().fill(statusColor).frame(width: 6, height: 6)
                .shadow(color: tunnel.status == .active ? .green.opacity(0.5) : .clear, radius: 3)
            Text(":" + String(tunnel.port))
                .font(.system(.callout, design: .monospaced)).fontWeight(.medium)
                .frame(width: 55, alignment: .leading)

            if let url = tunnel.tunnelURL {
                Text(shortenedURL(url))
                    .font(.caption)
                    .foregroundStyle(.blue)
                    .lineLimit(1)
            } else if tunnel.status == .starting {
                Text("Starting...")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            } else if tunnel.status == .error {
                Text("Error")
                    .font(.caption)
                    .foregroundStyle(.red)
            }

            Spacer()

            if tunnel.status == .active, tunnel.tunnelURL != nil {
                Button {
                    if let url = tunnel.tunnelURL {
                        ClipboardService.copy(url)
                        isCopied = true
                        Task {
                            try? await Task.sleep(for: .seconds(1))
                            isCopied = false
                        }
                    }
                } label: {
                    Image(systemName: isCopied ? "checkmark" : "doc.on.doc")
                        .font(.caption)
                }
                .buttonStyle(.bordered).controlSize(.small)
                .opacity(isHovered ? 1 : 0.6)
            } else if tunnel.status == .starting {
                ProgressView().scaleEffect(0.5).frame(width: 16, height: 16)
            }

            Button {
                state.tunnelManager.stopTunnel(id: tunnel.id)
            } label: {
                Image(systemName: "xmark.circle.fill")
                    .font(.caption)
                    .foregroundStyle(.red)
            }
            .buttonStyle(.plain)
            .opacity(isHovered ? 1 : 0.6)
        }
        .padding(.horizontal, 12).padding(.vertical, 8)
        .background(isHovered ? Color.primary.opacity(0.05) : Color.clear)
        .contentShape(Rectangle())
        .onHover { isHovered = $0 }
        .contextMenu {
            if tunnel.status == .active, let url = tunnel.tunnelURL {
                Button {
                    ClipboardService.copy(url)
                } label: {
                    Label("Copy URL", systemImage: "doc.on.doc")
                }
                Button {
                    if let tunnelURL = URL(string: url) {
                        NSWorkspace.shared.open(tunnelURL)
                    }
                } label: {
                    Label("Open in Browser", systemImage: "globe.fill")
                }
                Divider()
            }
            Button(role: .destructive) {
                state.tunnelManager.stopTunnel(id: tunnel.id)
            } label: {
                Label("Stop Tunnel", systemImage: "stop.fill")
            }
        }
    }

    private func shortenedURL(_ url: String) -> String {
        url.replacingOccurrences(of: "https://", with: "")
    }
}
```

## File: `platforms/macos/Sources/Views/MenuBar/MenuBarView.swift`
```
/// MenuBarView - Main menu bar dropdown interface
///
/// Displays the list of active ports in a compact menu bar dropdown.
/// Supports both list and tree view modes for port organization.
///
/// - Note: This view is shown when clicking the menu bar icon.
/// - Important: Uses `@Bindable var state: AppState` for state management.

import SwiftUI
import Defaults

struct MenuBarView: View {
    @Environment(\.openWindow) private var openWindow
    @Bindable var state: AppState
    @State private var searchText = ""
    @State private var confirmingKillAll = false
    @State private var confirmingKillPort: String?
    @State private var hoveredPort: String?
    @State private var expandedProcesses: Set<String> = []
    @Default(.useTreeView) private var useTreeView
    @Default(.hideSystemProcesses) private var hideSystemProcesses

    // MARK: - Cached Data (Memory Optimization)
    @State private var cachedFilteredPorts: [PortInfo] = []
    @State private var cachedGroups: [ProcessGroup] = []
    @State private var lastCacheKey: CacheKey?

    /// Cache key to detect when recalculation is needed
    private struct CacheKey: Equatable {
        let portsCount: Int
        let firstPortHash: Int
        let searchText: String
        let hideSystem: Bool
    }

    private var groupedByProcess: [ProcessGroup] { cachedGroups }

    /// Updates all cached data only when inputs change
    private func updateCachedData() {
        let currentKey = CacheKey(
            portsCount: state.ports.count,
            firstPortHash: state.ports.first?.hashValue ?? 0,
            searchText: searchText,
            hideSystem: hideSystemProcesses
        )

        // Skip if nothing changed
        guard currentKey != lastCacheKey else { return }
        lastCacheKey = currentKey

        // Compute filtered ports once
        var filtered: [PortInfo]
        if searchText.isEmpty {
            filtered = state.ports
        } else {
            filtered = state.ports.filter {
                String($0.port).contains(searchText) || $0.processName.localizedCaseInsensitiveContains(searchText)
            }
        }

        if hideSystemProcesses {
            filtered = filtered.filter { $0.processType != .system }
        }

        cachedFilteredPorts = filtered.sorted { a, b in
            let aFav = state.isFavorite(a.port)
            let bFav = state.isFavorite(b.port)
            if aFav != bFav { return aFav }
            return a.port < b.port
        }

        // Compute groups from cached filtered ports
        let grouped = Dictionary(grouping: cachedFilteredPorts) { $0.processName }
        cachedGroups = grouped.map { name, ports in
            ProcessGroup(
                id: name,
                processName: name,
                pids: Array(Set(ports.map(\.pid))).sorted(),
                ports: ports.sorted { $0.port < $1.port }
            )
        }.sorted { a, b in
            let aHasFavorite = a.ports.contains(where: { state.isFavorite($0.port) })
            let aHasWatched = a.ports.contains(where: { state.isWatching($0.port) })
            let bHasFavorite = b.ports.contains(where: { state.isFavorite($0.port) })
            let bHasWatched = b.ports.contains(where: { state.isWatching($0.port) })

            let aPriority = aHasFavorite ? 2 : (aHasWatched ? 1 : 0)
            let bPriority = bHasFavorite ? 2 : (bHasWatched ? 1 : 0)

            if aPriority != bPriority {
                return aPriority > bPriority
            } else {
                return a.processName.localizedCaseInsensitiveCompare(b.processName) == .orderedAscending
            }
        }

        // Keep expansion state bounded to currently visible process IDs.
        let visibleProcessIDs = Set(cachedGroups.map(\.id))
        expandedProcesses = expandedProcesses.intersection(visibleProcessIDs)
    }

    /// Cached filtered ports (no allocation on access)
    private var filteredPorts: [PortInfo] { cachedFilteredPorts }

    /// Filters port-forward connections based on search text
    private var filteredPortForwardConnections: [PortForwardConnectionState] {
        let connections = state.portForwardManager.connections
        if searchText.isEmpty { return connections }
        return connections.filter {
            String($0.effectivePort).contains(searchText) ||
            $0.config.name.localizedCaseInsensitiveContains(searchText) ||
            $0.config.namespace.localizedCaseInsensitiveContains(searchText) ||
            $0.config.service.localizedCaseInsensitiveContains(searchText)
        }
    }

    var body: some View {
        VStack(spacing: 0) {
            MenuBarHeader(searchText: $searchText, portCount: filteredPorts.count + filteredPortForwardConnections.count)

            Divider()

            MenuBarPortList(
                filteredPorts: filteredPorts,
                filteredPortForwardConnections: filteredPortForwardConnections,
                groupedByProcess: groupedByProcess,
                useTreeView: useTreeView,
                expandedProcesses: $expandedProcesses,
                confirmingKillPort: $confirmingKillPort,
                state: state
            )

            Divider()

            MenuBarActions(
                confirmingKillAll: $confirmingKillAll,
                useTreeView: $useTreeView,
                state: state,
                openWindow: openWindow
            )
        }
        .frame(width: 340)
        .onAppear { updateCachedData() }
        .onChange(of: state.ports) { _, _ in updateCachedData() }
        .onChange(of: searchText) { _, _ in updateCachedData() }
        .onChange(of: hideSystemProcesses) { _, _ in updateCachedData() }
    }
}
```

## File: `platforms/macos/Sources/Views/Onboarding/OnboardingFeaturesStep.swift`
```
import SwiftUI

struct OnboardingFeaturesStep: View {
    private let features: [(icon: String, title: String, description: String, color: Color)] = [
        ("magnifyingglass", "Port Scanning", "See all listening ports in one place", .blue),
        ("xmark.circle.fill", "Quick Kill", "Terminate processes with one click", .red),
        ("star.fill", "Favorites", "Pin frequently used ports for quick access", .yellow),
        ("eye.fill", "Watched Ports", "Get notifications when ports become active", .purple),
        ("globe", "Cloudflare Tunnels", "Share local ports publicly", .orange),
    ]

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("What you can do")
                .font(.title2)
                .fontWeight(.bold)
                .padding(.bottom, 4)

            ForEach(features, id: \.title) { feature in
                HStack(spacing: 14) {
                    Image(systemName: feature.icon)
                        .font(.title3)
                        .foregroundStyle(feature.color)
                        .frame(width: 28, alignment: .center)

                    VStack(alignment: .leading, spacing: 2) {
                        Text(feature.title)
                            .fontWeight(.medium)
                        Text(feature.description)
                            .font(.callout)
                            .foregroundStyle(.secondary)
                    }
                }
            }
        }
        .padding(32)
        .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topLeading)
    }
}
```

## File: `platforms/macos/Sources/Views/Onboarding/OnboardingReadyStep.swift`
```
import SwiftUI

struct OnboardingReadyStep: View {
    var body: some View {
        VStack(spacing: 20) {
            Spacer()

            Image(systemName: "checkmark.circle.fill")
                .font(.system(size: 56))
                .foregroundColor(.green)

            Text("You're All Set!")
                .font(.largeTitle)
                .fontWeight(.bold)

            Text("PortKiller is ready to use.\nLook for the icon in your menu bar.")
                .font(.title3)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
                .lineSpacing(4)

            HStack(spacing: 24) {
                tipView(icon: "menubar.arrow.up.rectangle", text: "Click the menu bar icon\nfor quick access")
                tipView(icon: "gearshape.fill", text: "Visit Settings to\ncustomize further")
            }
            .padding(.top, 8)

            Spacer()
        }
        .padding(32)
    }

    private func tipView(icon: String, text: String) -> some View {
        VStack(spacing: 8) {
            Image(systemName: icon)
                .font(.title2)
                .foregroundStyle(.secondary)
            Text(text)
                .font(.caption)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
        }
        .frame(width: 140)
    }
}
```

## File: `platforms/macos/Sources/Views/Onboarding/OnboardingSetupStep.swift`
```
import SwiftUI
import LaunchAtLogin
import KeyboardShortcuts
@preconcurrency import UserNotifications

struct OnboardingSetupStep: View {
    @State private var notificationStatus: UNAuthorizationStatus = .notDetermined

    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text("Quick Setup")
                .font(.title2)
                .fontWeight(.bold)
                .padding(.bottom, 4)

            // Launch at Login
            VStack(alignment: .leading, spacing: 8) {
                LaunchAtLogin.Toggle {
                    VStack(alignment: .leading, spacing: 2) {
                        Text("Launch at Login")
                            .fontWeight(.medium)
                        Text("Start PortKiller when you log in")
                            .font(.callout)
                            .foregroundStyle(.secondary)
                    }
                }
                .toggleStyle(.switch)
            }
            .padding(12)
            .background(Color(nsColor: .controlBackgroundColor))
            .clipShape(RoundedRectangle(cornerRadius: 8))

            // Notifications
            VStack(alignment: .leading, spacing: 8) {
                HStack {
                    VStack(alignment: .leading, spacing: 2) {
                        Text("Notifications")
                            .fontWeight(.medium)
                        Text("Get notified when watched ports change state")
                            .font(.callout)
                            .foregroundStyle(.secondary)
                    }

                    Spacer()

                    if notificationStatus == .authorized {
                        HStack(spacing: 4) {
                            Image(systemName: "checkmark.circle.fill")
                                .foregroundStyle(.green)
                            Text("Enabled")
                                .font(.callout)
                                .foregroundStyle(.green)
                        }
                    } else if notificationStatus == .denied {
                        Button("Open Settings") {
                            if let bundleId = Bundle.main.bundleIdentifier {
                                let url = URL(string: "x-apple.systempreferences:com.apple.Notifications-Settings.extension?id=\(bundleId)")!
                                NSWorkspace.shared.open(url)
                            }
                        }
                        .controlSize(.small)
                    } else {
                        Button("Enable") {
                            requestPermission()
                        }
                        .controlSize(.small)
                    }
                }
            }
            .padding(12)
            .background(Color(nsColor: .controlBackgroundColor))
            .clipShape(RoundedRectangle(cornerRadius: 8))

            // Keyboard Shortcut
            VStack(alignment: .leading, spacing: 8) {
                HStack {
                    VStack(alignment: .leading, spacing: 2) {
                        Text("Global Shortcut")
                            .fontWeight(.medium)
                        Text("Open PortKiller from anywhere")
                            .font(.callout)
                            .foregroundStyle(.secondary)
                    }

                    Spacer()

                    KeyboardShortcuts.Recorder(for: .toggleMainWindow)
                        .frame(width: 150)
                }
            }
            .padding(12)
            .background(Color(nsColor: .controlBackgroundColor))
            .clipShape(RoundedRectangle(cornerRadius: 8))

            Spacer()
        }
        .padding(32)
        .task {
            await checkNotificationStatus()
        }
    }

    private func requestPermission() {
        Task {
            _ = await NotificationService.shared.requestPermission()
            await checkNotificationStatus()
        }
    }

    private func checkNotificationStatus() async {
        guard Bundle.main.bundlePath.hasSuffix(".app") else { return }
        let settings = await UNUserNotificationCenter.current().notificationSettings()
        notificationStatus = settings.authorizationStatus
    }
}
```

## File: `platforms/macos/Sources/Views/Onboarding/OnboardingView.swift`
```
import SwiftUI
import Defaults

struct OnboardingView: View {
    @Environment(\.dismiss) private var dismiss
    @State private var currentStep = 0

    private let totalSteps = 4

    var body: some View {
        VStack(spacing: 0) {
            // Content
            Group {
                switch currentStep {
                case 0: OnboardingWelcomeStep()
                case 1: OnboardingFeaturesStep()
                case 2: OnboardingSetupStep()
                case 3: OnboardingReadyStep()
                default: EmptyView()
                }
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity)

            Divider()

            // Navigation
            HStack {
                // Step indicators
                HStack(spacing: 6) {
                    ForEach(0..<totalSteps, id: \.self) { step in
                        Circle()
                            .fill(step == currentStep ? Color.accentColor : Color.secondary.opacity(0.3))
                            .frame(width: 7, height: 7)
                    }
                }

                Spacer()

                HStack(spacing: 12) {
                    if currentStep > 0 {
                        Button("Back") {
                            withAnimation(.easeInOut(duration: 0.2)) {
                                currentStep -= 1
                            }
                        }
                        .controlSize(.large)
                    }

                    if currentStep < totalSteps - 1 {
                        Button("Skip") {
                            completeOnboarding()
                        }
                        .controlSize(.large)
                        .foregroundStyle(.secondary)

                        Button("Next") {
                            withAnimation(.easeInOut(duration: 0.2)) {
                                currentStep += 1
                            }
                        }
                        .controlSize(.large)
                        .buttonStyle(.borderedProminent)
                    } else {
                        Button("Get Started") {
                            completeOnboarding()
                        }
                        .controlSize(.large)
                        .buttonStyle(.borderedProminent)
                    }
                }
            }
            .padding(20)
        }
        .frame(width: 520, height: 420)
    }

    private func completeOnboarding() {
        Defaults[.hasCompletedOnboarding] = true
        dismiss()
    }
}
```

## File: `platforms/macos/Sources/Views/Onboarding/OnboardingWelcomeStep.swift`
```
import SwiftUI

struct OnboardingWelcomeStep: View {
    var body: some View {
        VStack(spacing: 20) {
            Spacer()

            Image(systemName: "network")
                .font(.system(size: 56))
                .foregroundColor(.accentColor)

            Text("Welcome to PortKiller")
                .font(.largeTitle)
                .fontWeight(.bold)

            Text("Find and kill processes on any port.\nManage your development servers with ease.")
                .font(.title3)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
                .lineSpacing(4)

            Spacer()
        }
        .padding(32)
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/PortForwardConnectionCard.swift`
```
import SwiftUI

struct PortForwardConnectionCard: View {
    let connection: PortForwardConnectionState
    var isSelected: Bool = false
    var onSelect: (() -> Void)?
    @Environment(AppState.self) private var appState
    @State private var isExpanded = false

    private var statusColor: Color {
        if connection.portForwardStatus == .error || connection.proxyStatus == .error {
            return .red
        } else if connection.isFullyConnected {
            return .green
        } else if connection.portForwardStatus == .connecting || connection.proxyStatus == .connecting {
            return .orange
        } else {
            return .gray.opacity(0.4)
        }
    }

    private var statusText: String {
        if connection.portForwardStatus == .error || connection.proxyStatus == .error {
            return "Error"
        } else if connection.isFullyConnected {
            return "Connected"
        } else if connection.portForwardStatus == .connecting || connection.proxyStatus == .connecting {
            return "Connecting..."
        } else {
            return "Disconnected"
        }
    }

    private var isConnecting: Bool {
        connection.portForwardStatus == .connecting || connection.proxyStatus == .connecting
    }

    @ViewBuilder
    private var inlineActionButton: some View {
        if isConnecting {
            Button {
                appState.portForwardManager.stopConnection(connection.id)
            } label: {
                ProgressView()
                    .scaleEffect(0.6)
                    .frame(width: 24, height: 24)
            }
            .buttonStyle(.plain)
            .help("Cancel")
        } else if connection.isFullyConnected {
            Button {
                appState.portForwardManager.stopConnection(connection.id)
            } label: {
                Image(systemName: "stop.fill")
                    .foregroundStyle(.red)
                    .frame(width: 24, height: 24)
            }
            .buttonStyle(.plain)
            .help("Stop")
        } else {
            Button {
                appState.portForwardManager.startConnection(connection.id)
            } label: {
                Image(systemName: "play.fill")
                    .foregroundStyle(.green)
                    .frame(width: 24, height: 24)
            }
            .buttonStyle(.plain)
            .help("Start")
        }
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            // Header
            HStack(spacing: 10) {
                Circle()
                    .fill(statusColor)
                    .frame(width: 10, height: 10)

                Text(connection.config.name)
                    .fontWeight(.medium)

                Text("\u{00B7}")
                    .foregroundStyle(.tertiary)

                Text("\(connection.config.namespace)/\(connection.config.service)")
                    .foregroundStyle(.secondary)
                    .font(.callout)
                    .lineLimit(1)

                Spacer()

                // Port info
                Text(":" + String(connection.effectivePort))
                    .font(.system(.caption, design: .monospaced))
                    .foregroundStyle(.secondary)

                // Status badge
                Text(statusText)
                    .font(.caption)
                    .padding(.horizontal, 8)
                    .padding(.vertical, 3)
                    .background(statusColor.opacity(0.15))
                    .foregroundStyle(statusColor)
                    .clipShape(Capsule())

                // Inline action button
                inlineActionButton

                Button {
                    withAnimation(.easeInOut(duration: 0.15)) {
                        isExpanded.toggle()
                    }
                } label: {
                    Image(systemName: "chevron.right")
                        .rotationEffect(.degrees(isExpanded ? 90 : 0))
                        .foregroundStyle(.secondary)
                        .frame(width: 20, height: 20)
                }
                .buttonStyle(.plain)

                Button {
                    appState.portForwardManager.removeConnection(connection.id)
                } label: {
                    Image(systemName: "xmark")
                        .foregroundStyle(.secondary)
                        .frame(width: 20, height: 20)
                }
                .buttonStyle(.plain)
            }
            .padding(12)
            .contentShape(Rectangle())
            .onTapGesture {
                onSelect?()
            }

            if isExpanded {
                Divider()
                    .padding(.horizontal, 12)

                PortForwardConnectionEditForm(connection: connection)
                    .padding(12)
            }
        }
        .background(isSelected ? Color.accentColor.opacity(0.1) : statusColor.opacity(0.05))
        .clipShape(RoundedRectangle(cornerRadius: 8))
        .overlay(
            RoundedRectangle(cornerRadius: 8)
                .stroke(isSelected ? Color.accentColor : statusColor.opacity(0.3), lineWidth: isSelected ? 2 : 1)
        )
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/PortForwardConnectionEditForm.swift`
```
import SwiftUI

struct PortForwardConnectionEditForm: View {
    let connection: PortForwardConnectionState
    @Environment(AppState.self) private var appState

    @State private var name: String
    @State private var namespace: String
    @State private var service: String
    @State private var localPort: Int
    @State private var remotePort: Int
    @State private var proxyEnabled: Bool
    @State private var proxyPort: Int
    @State private var isEnabled: Bool
    @State private var autoReconnect: Bool
    @State private var useDirectExec: Bool
    @State private var notifyOnConnect: Bool
    @State private var notifyOnDisconnect: Bool

    init(connection: PortForwardConnectionState) {
        self.connection = connection
        _name = State(initialValue: connection.config.name)
        _namespace = State(initialValue: connection.config.namespace)
        _service = State(initialValue: connection.config.service)
        _localPort = State(initialValue: connection.config.localPort)
        _remotePort = State(initialValue: connection.config.remotePort)
        _proxyEnabled = State(initialValue: connection.config.proxyPort != nil)
        _proxyPort = State(initialValue: connection.config.proxyPort ?? connection.config.localPort - 1)
        _isEnabled = State(initialValue: connection.config.isEnabled)
        _autoReconnect = State(initialValue: connection.config.autoReconnect)
        _useDirectExec = State(initialValue: connection.config.useDirectExec)
        _notifyOnConnect = State(initialValue: connection.config.notifyOnConnect)
        _notifyOnDisconnect = State(initialValue: connection.config.notifyOnDisconnect)
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            // Error message and Restart button
            HStack(spacing: 12) {
                if let error = connection.lastError {
                    Image(systemName: "exclamationmark.triangle.fill")
                        .foregroundStyle(.red)
                    Text(error)
                        .font(.caption)
                        .foregroundStyle(.red)
                        .lineLimit(2)
                }

                Spacer()

                Button {
                    appState.portForwardManager.restartConnection(connection.id)
                } label: {
                    Label("Restart", systemImage: "arrow.clockwise")
                }
                .buttonStyle(.bordered)
                .disabled(connection.portForwardStatus == .disconnected)
            }

            Divider()

            // Edit form
            Grid(alignment: .leading, horizontalSpacing: 12, verticalSpacing: 10) {
                GridRow {
                    Text("Name").foregroundStyle(.secondary).frame(width: 80, alignment: .trailing)
                    TextField("", text: $name)
                        .textFieldStyle(.roundedBorder)
                        .frame(maxWidth: 180)
                        .onChange(of: name) { save() }
                }

                GridRow {
                    Text("Namespace").foregroundStyle(.secondary).frame(width: 80, alignment: .trailing)
                    TextField("", text: $namespace)
                        .textFieldStyle(.roundedBorder)
                        .frame(maxWidth: 180)
                        .onChange(of: namespace) { save() }
                }

                GridRow {
                    Text("Service").foregroundStyle(.secondary).frame(width: 80, alignment: .trailing)
                    TextField("", text: $service)
                        .textFieldStyle(.roundedBorder)
                        .frame(maxWidth: 180)
                        .onChange(of: service) { save() }
                }

                GridRow {
                    Text("Ports").foregroundStyle(.secondary).frame(width: 80, alignment: .trailing)
                    HStack(spacing: 8) {
                        TextField("", value: $localPort, format: .number.grouping(.never))
                            .textFieldStyle(.roundedBorder)
                            .frame(width: 70)
                            .onChange(of: localPort) { save() }
                        Text("\u{2192}").foregroundStyle(.tertiary)
                        TextField("", value: $remotePort, format: .number.grouping(.never))
                            .textFieldStyle(.roundedBorder)
                            .frame(width: 70)
                            .onChange(of: remotePort) { save() }
                    }
                }

                GridRow {
                    Text("Proxy").foregroundStyle(.secondary).frame(width: 80, alignment: .trailing)
                    HStack(spacing: 12) {
                        Toggle("", isOn: $proxyEnabled)
                            .toggleStyle(.switch)
                            .labelsHidden()
                            .onChange(of: proxyEnabled) { save() }

                        if proxyEnabled {
                            TextField("", value: $proxyPort, format: .number.grouping(.never))
                                .textFieldStyle(.roundedBorder)
                                .frame(width: 70)
                                .onChange(of: proxyPort) { save() }

                            Toggle("Multi-conn", isOn: $useDirectExec)
                                .toggleStyle(.checkbox)
                                .onChange(of: useDirectExec) { save() }
                                .help("Multiple simultaneous connections")
                        }
                    }
                }

                GridRow {
                    Text("Options").foregroundStyle(.secondary).frame(width: 80, alignment: .trailing)
                    HStack(spacing: 16) {
                        Toggle("Enabled", isOn: $isEnabled)
                            .onChange(of: isEnabled) { save() }
                        Toggle("Auto Reconnect", isOn: $autoReconnect)
                            .onChange(of: autoReconnect) { save() }
                    }
                    .toggleStyle(.checkbox)
                }

                GridRow {
                    Text("Notifications").foregroundStyle(.secondary).frame(width: 80, alignment: .trailing)
                    HStack(spacing: 16) {
                        Toggle("On Connect", isOn: $notifyOnConnect)
                            .onChange(of: notifyOnConnect) { save() }
                        Toggle("On Disconnect", isOn: $notifyOnDisconnect)
                            .onChange(of: notifyOnDisconnect) { save() }
                    }
                    .toggleStyle(.checkbox)
                }
            }
        }
    }

    private func save() {
        var config = connection.config
        config.name = name
        config.namespace = namespace
        config.service = service
        config.localPort = localPort
        config.remotePort = remotePort
        config.proxyPort = proxyEnabled ? proxyPort : nil
        config.isEnabled = isEnabled
        config.autoReconnect = autoReconnect
        config.useDirectExec = useDirectExec
        config.notifyOnConnect = notifyOnConnect
        config.notifyOnDisconnect = notifyOnDisconnect
        appState.portForwardManager.updateConnection(config)
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/PortForwarderSidebarContent.swift`
```
import SwiftUI

struct PortForwarderSidebarContent: View {
    @Environment(AppState.self) private var appState
    @State private var discoveryManager: KubernetesDiscoveryManager?
    @State private var searchText = ""
    @State private var groupByNamespace = true

    var body: some View {
        VStack(spacing: 0) {
            // Toolbar
            PortForwarderToolbar(
                searchText: $searchText,
                groupByNamespace: $groupByNamespace,
                discoveryManager: $discoveryManager
            )

            Divider()

            // Dependency warning banner
            if !DependencyChecker.shared.allRequiredInstalled {
                DependencyWarningBanner()
            }

            // Table header
            PortForwarderTableHeader()

            Divider()

            // Main content - Table
            if filteredConnections.isEmpty {
                emptyState
            } else {
                ScrollView {
                    LazyVStack(spacing: 0) {
                        if groupByNamespace {
                            groupedView
                        } else {
                            flatView
                        }
                    }
                }
            }

            Divider()

            // Status bar
            PortForwarderStatusBar()
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .sheet(item: $discoveryManager) { dm in
            ServiceBrowserView(
                discoveryManager: dm,
                onServiceSelected: { config in
                    appState.portForwardManager.addConnection(config)
                    discoveryManager = nil
                },
                onCancel: {
                    discoveryManager = nil
                }
            )
        }
    }

    // MARK: - Filtered Connections

    private var filteredConnections: [PortForwardConnectionState] {
        let connections = appState.portForwardManager.connections
        guard !searchText.isEmpty else { return connections }
        return connections.filter { conn in
            conn.config.name.localizedCaseInsensitiveContains(searchText) ||
            conn.config.namespace.localizedCaseInsensitiveContains(searchText) ||
            conn.config.service.localizedCaseInsensitiveContains(searchText) ||
            String(conn.effectivePort).contains(searchText)
        }
    }

    private var connectionsByNamespace: [(namespace: String, connections: [PortForwardConnectionState])] {
        let grouped = Dictionary(grouping: filteredConnections) { $0.config.namespace }
        return grouped.map { (namespace: $0.key, connections: $0.value) }
            .sorted { $0.namespace < $1.namespace }
    }

    // MARK: - Views

    @ViewBuilder
    private var groupedView: some View {
        ForEach(connectionsByNamespace, id: \.namespace) { group in
            // Namespace header
            HStack {
                Image(systemName: "folder.fill")
                    .foregroundStyle(.secondary)
                Text(group.namespace)
                    .font(.caption.weight(.semibold))
                Text("(\(group.connections.count))")
                    .font(.caption)
                    .foregroundStyle(.tertiary)
                Spacer()
            }
            .padding(.horizontal, 12)
            .padding(.vertical, 6)
            .frame(maxWidth: .infinity)
            .background(Color(nsColor: .windowBackgroundColor))

            ForEach(group.connections) { connection in
                PortForwarderTableRow(
                    connection: connection,
                    isSelected: appState.selectedPortForwardConnectionId == connection.id,
                    onSelect: { appState.selectedPortForwardConnectionId = connection.id }
                )
            }
        }
    }

    @ViewBuilder
    private var flatView: some View {
        ForEach(filteredConnections) { connection in
            PortForwarderTableRow(
                connection: connection,
                isSelected: appState.selectedPortForwardConnectionId == connection.id,
                onSelect: { appState.selectedPortForwardConnectionId = connection.id }
            )
        }
    }

    private var emptyState: some View {
        ContentUnavailableView {
            Label("No Connections", systemImage: "point.3.connected.trianglepath.dotted")
        } description: {
            if searchText.isEmpty {
                Text("Add a connection or import from Kubernetes")
            } else {
                Text("No connections match '\(searchText)'")
            }
        }
        .frame(maxHeight: .infinity)
    }
}

// MARK: - Add Connection Buttons

struct AddConnectionButtons: View {
    @Environment(AppState.self) private var appState
    @Binding var discoveryManager: KubernetesDiscoveryManager?

    var body: some View {
        HStack(spacing: 16) {
            // Manual add button
            Button {
                let config = PortForwardConnectionConfig(
                    name: "New Connection",
                    namespace: "default",
                    service: "service-name",
                    localPort: 8080,
                    remotePort: 80
                )
                appState.portForwardManager.addConnection(config)
            } label: {
                HStack(spacing: 6) {
                    Image(systemName: "plus.circle.fill")
                    Text("Add Connection")
                }
                .foregroundStyle(.secondary)
            }
            .buttonStyle(.plain)

            // Import from Kubernetes button
            Button {
                let dm = KubernetesDiscoveryManager(processManager: appState.portForwardManager.processManager)
                Task { await dm.loadNamespaces() }
                discoveryManager = dm
            } label: {
                HStack(spacing: 6) {
                    Image(systemName: "square.and.arrow.down")
                    Text("Import from Kubernetes")
                }
                .foregroundStyle(.blue)
            }
            .buttonStyle(.plain)
            .disabled(!DependencyChecker.shared.allRequiredInstalled)
        }
        .padding(.top, 4)
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/PortForwarderStatusBar.swift`
```
import SwiftUI

struct PortForwarderStatusBar: View {
    @Environment(AppState.self) private var appState

    var body: some View {
        HStack {
            // Connection count
            let manager = appState.portForwardManager
            if manager.connections.isEmpty {
                Text("No connections configured")
            } else {
                Text("\(manager.connectedCount) of \(manager.connections.count) connected")
            }

            Spacer()
        }
        .font(.caption)
        .foregroundStyle(.secondary)
        .padding(.horizontal, 12)
        .padding(.vertical, 8)
        .background(Color(nsColor: .windowBackgroundColor))
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/PortForwarderToolbar.swift`
```
import SwiftUI

struct PortForwarderToolbar: View {
    @Environment(AppState.self) private var appState
    @Binding var searchText: String
    @Binding var groupByNamespace: Bool
    @Binding var discoveryManager: KubernetesDiscoveryManager?

    var body: some View {
        HStack(spacing: 12) {
            // Search field
            HStack {
                Image(systemName: "magnifyingglass")
                    .foregroundStyle(.secondary)
                TextField("Search...", text: $searchText)
                    .textFieldStyle(.plain)
                if !searchText.isEmpty {
                    Button {
                        searchText = ""
                    } label: {
                        Image(systemName: "xmark.circle.fill")
                            .foregroundStyle(.secondary)
                    }
                    .buttonStyle(.plain)
                }
            }
            .padding(6)
            .background(Color(nsColor: .textBackgroundColor))
            .cornerRadius(6)
            .frame(maxWidth: 200)

            // Group toggle
            Button {
                groupByNamespace.toggle()
            } label: {
                Image(systemName: groupByNamespace ? "folder.fill" : "list.bullet")
            }
            .buttonStyle(.bordered)
            .help(groupByNamespace ? "Show flat list" : "Group by namespace")

            Spacer()

            let manager = appState.portForwardManager

            if !manager.connections.isEmpty {
                Button {
                    manager.startAll()
                } label: {
                    Label("Start All", systemImage: "play.fill")
                }
                .buttonStyle(.bordered)
                .disabled(manager.allConnected)

                Button {
                    manager.stopAll()
                } label: {
                    Label("Stop All", systemImage: "stop.fill")
                }
                .buttonStyle(.bordered)
                .disabled(manager.connectedCount == 0)

                Button {
                    Task { await manager.killStuckProcesses() }
                } label: {
                    Label("Force Stop", systemImage: "xmark.octagon.fill")
                }
                .buttonStyle(.bordered)
                .help("Kill all stuck kubectl/socat processes")
            }

            Button {
                let config = PortForwardConnectionConfig(
                    name: "New Connection",
                    namespace: "default",
                    service: "service-name",
                    localPort: 8080,
                    remotePort: 80
                )
                appState.portForwardManager.addConnection(config)
            } label: {
                Label("Add", systemImage: "plus.circle.fill")
            }
            .buttonStyle(.bordered)

            Button {
                let dm = KubernetesDiscoveryManager(processManager: appState.portForwardManager.processManager)
                Task { await dm.loadNamespaces() }
                discoveryManager = dm
            } label: {
                Label("Import", systemImage: "square.and.arrow.down.fill")
            }
            .buttonStyle(.bordered)
            .disabled(!DependencyChecker.shared.allRequiredInstalled)
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 8)
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/PortForwarderWindowView.swift`
```
import SwiftUI
import AppKit

struct PortForwarderWindowView: View {
    @Environment(AppState.self) private var appState
    @State private var discoveryManager: KubernetesDiscoveryManager?

    var body: some View {
        TabView {
            ConnectionsTab(discoveryManager: $discoveryManager)
                .tabItem {
                    Label("Connections", systemImage: "point.3.connected.trianglepath.dotted")
                }

            ServiceBrowserTab()
                .tabItem {
                    Label("Browse", systemImage: "magnifyingglass")
                }

            PortForwarderSettingsTab()
                .tabItem {
                    Label("Settings", systemImage: "gear")
                }
        }
        .frame(minWidth: 850, idealWidth: 1000, minHeight: 600, idealHeight: 700)
        .sheet(item: $discoveryManager) { dm in
            ServiceBrowserView(
                discoveryManager: dm,
                onServiceSelected: { config in
                    appState.portForwardManager.addConnection(config)
                    discoveryManager = nil
                },
                onCancel: {
                    discoveryManager = nil
                }
            )
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/ServiceBrowserView.swift`
```
import SwiftUI

struct ServiceBrowserView: View {
    @Bindable var discoveryManager: KubernetesDiscoveryManager
    let onServiceSelected: (PortForwardConnectionConfig) -> Void
    let onCancel: () -> Void

    var body: some View {
        VStack(spacing: 0) {
            // Header
            HStack {
                Text("Import from Kubernetes")
                    .font(.headline)
                Spacer()
                Button {
                    onCancel()
                } label: {
                    Image(systemName: "xmark.circle.fill")
                        .foregroundStyle(.secondary)
                }
                .buttonStyle(.plain)
            }
            .padding()

            Divider()

            // Content - 3 panel layout
            HStack(spacing: 0) {
                // Namespace List (left panel)
                NamespaceListView(
                    namespaces: discoveryManager.namespaces,
                    selectedNamespace: discoveryManager.selectedNamespace,
                    state: discoveryManager.namespaceState,
                    onSelect: { namespace in
                        Task { await discoveryManager.selectNamespace(namespace) }
                    },
                    onRefresh: {
                        Task { await discoveryManager.loadNamespaces() }
                    },
                    onAddCustom: { namespaceNames in
                        discoveryManager.addCustomNamespaces(namespaceNames)
                    },
                    onRemoveCustom: { namespace in
                        discoveryManager.removeCustomNamespace(namespace)
                    }
                )
                .frame(width: 180)

                Divider()

                // Service List (middle panel)
                ServiceListView(
                    services: discoveryManager.services,
                    selectedService: discoveryManager.selectedService,
                    state: discoveryManager.serviceState,
                    onSelect: { service in
                        discoveryManager.selectService(service)
                    }
                )
                .frame(minWidth: 180)

                Divider()

                // Port Selection (right panel)
                if let service = discoveryManager.selectedService {
                    ServiceDetailView(
                        service: service,
                        selectedPort: discoveryManager.selectedPort,
                        proxyEnabled: $discoveryManager.proxyEnabled,
                        suggestedLocalPort: discoveryManager.suggestLocalPort(for: discoveryManager.selectedPort?.port ?? 0),
                        onPortSelect: { port in
                            discoveryManager.selectPort(port)
                        }
                    )
                    .frame(width: 200)
                } else {
                    EmptySelectionView()
                        .frame(width: 200)
                }
            }

            Divider()

            // Footer with action buttons
            HStack {
                if case .error(let message) = discoveryManager.namespaceState {
                    Image(systemName: "exclamationmark.triangle.fill")
                        .foregroundStyle(.orange)
                    Text(message)
                        .font(.caption)
                        .foregroundStyle(.secondary)
                        .lineLimit(1)
                }

                Spacer()

                Button("Cancel") {
                    onCancel()
                }
                .keyboardShortcut(.cancelAction)

                Button("Add") {
                    if let config = discoveryManager.createConnectionConfig() {
                        onServiceSelected(config)
                    }
                }
                .keyboardShortcut(.defaultAction)
                .disabled(discoveryManager.selectedPort == nil)
            }
            .padding()
        }
        .frame(width: 800, height: 500)
        .task {
            if discoveryManager.namespaceState == .idle {
                await discoveryManager.loadNamespaces()
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/Browser/AddCustomNamespaceSheet.swift`
```
import SwiftUI

struct AddCustomNamespaceSheet: View {
    @Environment(\.dismiss) private var dismiss
    @State private var namespaceInput: String = ""
    @FocusState private var isInputFocused: Bool

    let onAdd: ([String]) -> Void

    var body: some View {
        VStack(spacing: 16) {
            Text("Add Custom Namespace")
                .font(.headline)

            Text("Enter namespace names (comma-separated for multiple)")
                .font(.caption)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)

            TextField("e.g., production, staging, dev", text: $namespaceInput)
                .textFieldStyle(.roundedBorder)
                .focused($isInputFocused)
                .onSubmit {
                    addNamespaces()
                }

            HStack {
                Button("Cancel") {
                    dismiss()
                }
                .keyboardShortcut(.cancelAction)

                Spacer()

                Button("Add") {
                    addNamespaces()
                }
                .keyboardShortcut(.defaultAction)
                .disabled(namespaceInput.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty)
            }
        }
        .padding()
        .frame(width: 400)
        .onAppear {
            isInputFocused = true
        }
    }

    private func addNamespaces() {
        let names = namespaceInput
            .split(separator: ",")
            .map { $0.trimmingCharacters(in: .whitespacesAndNewlines) }
            .filter { !$0.isEmpty }

        guard !names.isEmpty else { return }

        onAdd(names)
        dismiss()
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/Browser/EmptySelectionView.swift`
```
import SwiftUI

struct EmptySelectionView: View {
    var body: some View {
        VStack(spacing: 0) {
            HStack {
                Text("Service Details")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                Spacer()
            }
            .padding(.horizontal, 10)
            .padding(.vertical, 8)

            Divider()

            VStack {
                Spacer()
                Image(systemName: "arrow.left")
                    .font(.title2)
                    .foregroundStyle(.tertiary)
                Text("Select a service")
                    .font(.caption)
                    .foregroundStyle(.tertiary)
                Spacer()
            }
        }
        .background(Color.primary.opacity(0.02))
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/Browser/NamespaceListView.swift`
```
import SwiftUI

struct NamespaceListView: View {
    let namespaces: [KubernetesNamespace]
    let selectedNamespace: KubernetesNamespace?
    let state: KubernetesDiscoveryState
    let onSelect: (KubernetesNamespace) -> Void
    let onRefresh: () -> Void
    let onAddCustom: ([String]) -> Void
    let onRemoveCustom: (KubernetesNamespace) -> Void

    @State private var showingAddSheet = false

    var body: some View {
        VStack(spacing: 0) {
            HStack {
                Text("Namespaces")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                Spacer()
                Button {
                    showingAddSheet = true
                } label: {
                    Image(systemName: "plus.circle")
                        .font(.caption)
                }
                .buttonStyle(.plain)
                .help("Add custom namespace")
                Button {
                    onRefresh()
                } label: {
                    Image(systemName: "arrow.clockwise")
                        .font(.caption)
                }
                .buttonStyle(.plain)
                .disabled(state == .loading)
                .help("Refresh namespaces")
            }
            .padding(.horizontal, 10)
            .padding(.vertical, 8)

            Divider()

            Group {
                switch state {
                case .loading:
                    VStack {
                        Spacer()
                        ProgressView()
                            .scaleEffect(0.8)
                        Text("Loading...")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                        Spacer()
                    }

                case .error(let message):
                    VStack(spacing: 8) {
                        Spacer()
                        Image(systemName: "exclamationmark.triangle")
                            .font(.title2)
                            .foregroundStyle(.orange)
                        Text(message)
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, 8)
                        HStack(spacing: 8) {
                            Button("Retry") {
                                onRefresh()
                            }
                            .buttonStyle(.bordered)
                            .controlSize(.small)

                            Button("Add Custom") {
                                showingAddSheet = true
                            }
                            .buttonStyle(.borderedProminent)
                            .controlSize(.small)
                        }
                        Spacer()
                    }

                case .idle, .loaded:
                    if namespaces.isEmpty && state == .loaded {
                        VStack {
                            Spacer()
                            Text("No namespaces")
                                .font(.caption)
                                .foregroundStyle(.tertiary)
                            Spacer()
                        }
                    } else {
                        ScrollView {
                            LazyVStack(spacing: 1) {
                                ForEach(namespaces) { namespace in
                                    NamespaceRow(
                                        namespace: namespace,
                                        isSelected: selectedNamespace?.id == namespace.id,
                                        onSelect: onSelect,
                                        onDelete: namespace.isCustom ? {
                                            onRemoveCustom(namespace)
                                        } : nil
                                    )
                                }
                            }
                            .padding(.vertical, 4)
                        }
                    }
                }
            }
        }
        .background(Color.primary.opacity(0.02))
        .sheet(isPresented: $showingAddSheet) {
            AddCustomNamespaceSheet(onAdd: onAddCustom)
        }
    }
}

struct NamespaceRow: View {
    let namespace: KubernetesNamespace
    let isSelected: Bool
    let onSelect: (KubernetesNamespace) -> Void
    let onDelete: (() -> Void)?

    var body: some View {
        Button {
            onSelect(namespace)
        } label: {
            HStack {
                Image(systemName: namespace.isCustom ? "pencil.and.list.clipboard" : "folder")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                Text(namespace.name)
                    .font(.system(.body, design: .monospaced))
                    .lineLimit(1)
                Spacer()
            }
            .padding(.horizontal, 10)
            .padding(.vertical, 6)
            .background(isSelected ? Color.accentColor.opacity(0.2) : Color.clear)
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
        .contextMenu {
            if onDelete != nil {
                Button("Remove", role: .destructive) {
                    onDelete?()
                }
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/Browser/NamespacePanel.swift`
```
import SwiftUI

struct NamespacePanel: View {
    let namespaces: [KubernetesNamespace]
    let selectedNamespace: KubernetesNamespace?
    let state: KubernetesDiscoveryState
    let onSelect: (KubernetesNamespace) -> Void
    let onRefresh: () -> Void
    let onAddCustom: ([String]) -> Void
    let onRemoveCustom: (KubernetesNamespace) -> Void

    @State private var showingAddSheet = false

    var body: some View {
        VStack(spacing: 0) {
            HStack {
                Text("Namespaces")
                    .font(.headline)
                Spacer()
                Button {
                    showingAddSheet = true
                } label: {
                    Image(systemName: "plus.circle")
                }
                .buttonStyle(.plain)
                .help("Add custom namespace")
                Button {
                    onRefresh()
                } label: {
                    Image(systemName: "arrow.clockwise")
                }
                .buttonStyle(.plain)
                .disabled(state == .loading)
                .help("Refresh namespaces")
            }
            .padding(12)

            Divider()

            if state == .loading {
                VStack {
                    Spacer()
                    ProgressView()
                    Text("Loading...")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    Spacer()
                }
            } else if case .error(let msg) = state {
                VStack(spacing: 8) {
                    Spacer()
                    Image(systemName: "exclamationmark.triangle")
                        .foregroundStyle(.orange)
                    Text(msg)
                        .font(.caption)
                        .foregroundStyle(.secondary)
                        .multilineTextAlignment(.center)
                    HStack(spacing: 8) {
                        Button("Retry", action: onRefresh)
                            .buttonStyle(.bordered)
                        Button("Add Custom") {
                            showingAddSheet = true
                        }
                        .buttonStyle(.borderedProminent)
                    }
                    Spacer()
                }
                .padding()
            } else {
                ScrollView {
                    LazyVStack(spacing: 1) {
                        ForEach(namespaces) { ns in
                            Button { onSelect(ns) } label: {
                                HStack {
                                    Image(systemName: ns.isCustom ? "pencil.and.list.clipboard" : "folder")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                    Text(ns.name)
                                        .font(.system(.body, design: .monospaced))
                                    Spacer()
                                }
                                .padding(.horizontal, 12)
                                .padding(.vertical, 8)
                                .background(selectedNamespace?.id == ns.id ? Color.accentColor.opacity(0.2) : Color.clear)
                            }
                            .buttonStyle(.plain)
                            .contextMenu {
                                if ns.isCustom {
                                    Button("Remove", role: .destructive) {
                                        onRemoveCustom(ns)
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        .sheet(isPresented: $showingAddSheet) {
            AddCustomNamespaceSheet(onAdd: onAddCustom)
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/Browser/PortPanel.swift`
```
import SwiftUI

struct PortPanel: View {
    let service: KubernetesService?
    let selectedPort: KubernetesService.ServicePort?
    @Binding var proxyEnabled: Bool
    let discoveryManager: KubernetesDiscoveryManager
    let onPortSelect: (KubernetesService.ServicePort) -> Void
    let onAdd: () -> Void

    var body: some View {
        VStack(spacing: 0) {
            HStack {
                Text("Port Configuration")
                    .font(.headline)
                Spacer()
            }
            .padding(12)

            Divider()

            if let service = service {
                ScrollView {
                    VStack(alignment: .leading, spacing: 16) {
                        // Port selection
                        ForEach(service.ports) { port in
                            Button {
                                onPortSelect(port)
                            } label: {
                                HStack {
                                    Image(systemName: selectedPort?.id == port.id ? "checkmark.circle.fill" : "circle")
                                        .foregroundStyle(selectedPort?.id == port.id ? .blue : .secondary)
                                    Text(port.displayName)
                                        .font(.system(.body, design: .monospaced))
                                    Spacer()
                                }
                            }
                            .buttonStyle(.plain)
                        }

                        if selectedPort != nil {
                            Divider()

                            Toggle("Enable Proxy (socat)", isOn: $proxyEnabled)

                            let localPort = discoveryManager.suggestLocalPort(for: selectedPort?.port ?? 0)
                            let proxyPort = discoveryManager.suggestProxyPort(for: localPort)

                            VStack(alignment: .leading, spacing: 4) {
                                Text("Local: \(localPort)")
                                    .font(.caption)
                                if proxyEnabled {
                                    Text("Proxy: \(proxyPort)")
                                        .font(.caption)
                                }
                                Text("Connect to: localhost:\(proxyEnabled ? proxyPort : localPort)")
                                    .font(.caption)
                                    .foregroundStyle(.green)
                            }

                            Button("Add Connection", action: onAdd)
                                .buttonStyle(.borderedProminent)
                        }
                    }
                    .padding(12)
                }
            } else {
                VStack {
                    Spacer()
                    Text("Select a service")
                        .foregroundStyle(.tertiary)
                    Spacer()
                }
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/Browser/ServiceDetailView.swift`
```
import SwiftUI

struct ServiceDetailView: View {
    let service: KubernetesService
    let selectedPort: KubernetesService.ServicePort?
    @Binding var proxyEnabled: Bool
    let suggestedLocalPort: Int
    let onPortSelect: (KubernetesService.ServicePort) -> Void

    private var suggestedProxyPort: Int {
        suggestedLocalPort - 1
    }

    var body: some View {
        VStack(spacing: 0) {
            HStack {
                Text("Service Details")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                Spacer()
            }
            .padding(.horizontal, 10)
            .padding(.vertical, 8)

            Divider()

            ScrollView {
                VStack(alignment: .leading, spacing: 12) {
                    // Service Info
                    VStack(alignment: .leading, spacing: 4) {
                        Text(service.name)
                            .font(.headline)
                        HStack(spacing: 6) {
                            Text(service.type)
                                .font(.caption)
                                .padding(.horizontal, 6)
                                .padding(.vertical, 2)
                                .background(Color.secondary.opacity(0.2))
                                .clipShape(RoundedRectangle(cornerRadius: 4))
                            if let ip = service.clusterIP, ip != "None" {
                                Text(ip)
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                            }
                        }
                    }

                    Divider()

                    // Port Selection
                    Text("Select Port")
                        .font(.caption)
                        .foregroundStyle(.secondary)

                    if service.ports.isEmpty {
                        Text("No ports defined")
                            .font(.caption)
                            .foregroundStyle(.tertiary)
                    } else {
                        ForEach(service.ports) { port in
                            PortSelectionRow(
                                port: port,
                                isSelected: selectedPort?.id == port.id,
                                onSelect: { onPortSelect(port) }
                            )
                        }
                    }

                    // Port Configuration
                    if selectedPort != nil {
                        Divider()

                        Text("Port Configuration")
                            .font(.caption)
                            .foregroundStyle(.secondary)

                        VStack(alignment: .leading, spacing: 6) {
                            HStack {
                                Text("Local port:")
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                                Text(String(suggestedLocalPort))
                                    .font(.system(.caption, design: .monospaced, weight: .medium))
                            }

                            Toggle("Enable Proxy (socat)", isOn: $proxyEnabled)
                                .toggleStyle(.checkbox)

                            if proxyEnabled {
                                HStack {
                                    Text("Proxy port:")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                    Text(String(suggestedProxyPort))
                                        .font(.system(.caption, design: .monospaced, weight: .medium))
                                }
                            }

                            Divider()

                            HStack {
                                Text("Connect to:")
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                                Text("localhost:" + String(proxyEnabled ? suggestedProxyPort : suggestedLocalPort))
                                    .font(.system(.caption, design: .monospaced, weight: .semibold))
                                    .foregroundStyle(.green)
                            }
                        }
                        .padding(8)
                        .background(Color.primary.opacity(0.03))
                        .clipShape(RoundedRectangle(cornerRadius: 6))
                    }

                    Spacer()
                }
                .padding(10)
            }
        }
        .background(Color.primary.opacity(0.02))
    }
}

struct PortSelectionRow: View {
    let port: KubernetesService.ServicePort
    let isSelected: Bool
    let onSelect: () -> Void

    var body: some View {
        Button(action: onSelect) {
            HStack {
                Image(systemName: isSelected ? "checkmark.circle.fill" : "circle")
                    .foregroundStyle(isSelected ? Color.accentColor : .secondary)

                VStack(alignment: .leading, spacing: 2) {
                    HStack(spacing: 4) {
                        Text(String(port.port))
                            .font(.system(.body, design: .monospaced, weight: .medium))
                        if let name = port.name, !name.isEmpty {
                            Text("(\(name))")
                                .font(.caption)
                                .foregroundStyle(.secondary)
                        }
                    }
                    if let proto = port.protocol {
                        Text(proto)
                            .font(.caption2)
                            .foregroundStyle(.tertiary)
                    }
                }

                Spacer()
            }
            .padding(8)
            .background(isSelected ? Color.accentColor.opacity(0.1) : Color.clear)
            .clipShape(RoundedRectangle(cornerRadius: 6))
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/Browser/ServiceListView.swift`
```
import SwiftUI

struct ServiceListView: View {
    let services: [KubernetesService]
    let selectedService: KubernetesService?
    let state: KubernetesDiscoveryState
    let onSelect: (KubernetesService) -> Void

    var body: some View {
        VStack(spacing: 0) {
            HStack {
                Text("Services")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                Spacer()
                if !services.isEmpty {
                    Text("\(services.count)")
                        .font(.caption)
                        .foregroundStyle(.tertiary)
                }
            }
            .padding(.horizontal, 10)
            .padding(.vertical, 8)

            Divider()

            Group {
                switch state {
                case .loading:
                    VStack {
                        Spacer()
                        ProgressView()
                            .scaleEffect(0.8)
                        Text("Loading services...")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                        Spacer()
                    }

                case .error(let message):
                    VStack(spacing: 8) {
                        Spacer()
                        Image(systemName: "exclamationmark.triangle")
                            .foregroundStyle(.orange)
                        Text(message)
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, 8)
                        Spacer()
                    }

                case .idle:
                    VStack {
                        Spacer()
                        Image(systemName: "arrow.left")
                            .foregroundStyle(.tertiary)
                        Text("Select a namespace")
                            .font(.caption)
                            .foregroundStyle(.tertiary)
                        Spacer()
                    }

                case .loaded:
                    if services.isEmpty {
                        VStack {
                            Spacer()
                            Text("No services found")
                                .font(.caption)
                                .foregroundStyle(.tertiary)
                            Spacer()
                        }
                    } else {
                        ScrollView {
                            LazyVStack(spacing: 1) {
                                ForEach(services) { service in
                                    ServiceRow(
                                        service: service,
                                        isSelected: selectedService?.id == service.id,
                                        onSelect: onSelect
                                    )
                                }
                            }
                            .padding(.vertical, 4)
                        }
                    }
                }
            }
        }
        .background(Color.primary.opacity(0.02))
    }
}

struct ServiceRow: View {
    let service: KubernetesService
    let isSelected: Bool
    let onSelect: (KubernetesService) -> Void

    var body: some View {
        Button {
            onSelect(service)
        } label: {
            HStack {
                Image(systemName: "server.rack")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                VStack(alignment: .leading, spacing: 2) {
                    Text(service.name)
                        .font(.system(.body, design: .monospaced))
                        .lineLimit(1)
                    HStack(spacing: 4) {
                        Text(service.type)
                            .font(.caption2)
                            .foregroundStyle(.tertiary)
                        Text("\u{00B7}")
                            .foregroundStyle(.tertiary)
                        Text("\(service.ports.count) port\(service.ports.count != 1 ? "s" : "")")
                            .font(.caption2)
                            .foregroundStyle(.tertiary)
                    }
                }
                Spacer()
            }
            .padding(.horizontal, 10)
            .padding(.vertical, 6)
            .background(isSelected ? Color.accentColor.opacity(0.2) : Color.clear)
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/Browser/ServicePanel.swift`
```
import SwiftUI

struct ServicePanel: View {
    let services: [KubernetesService]
    let selectedService: KubernetesService?
    let state: KubernetesDiscoveryState
    let onSelect: (KubernetesService) -> Void

    var body: some View {
        VStack(spacing: 0) {
            HStack {
                Text("Services")
                    .font(.headline)
                Spacer()
                Text("\(services.count)")
                    .foregroundStyle(.secondary)
            }
            .padding(12)

            Divider()

            if state == .loading {
                VStack {
                    Spacer()
                    ProgressView()
                    Text("Loading...")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    Spacer()
                }
            } else if state == .idle {
                VStack {
                    Spacer()
                    Text("Select a namespace")
                        .foregroundStyle(.tertiary)
                    Spacer()
                }
            } else {
                ScrollView {
                    LazyVStack(spacing: 1) {
                        ForEach(services) { svc in
                            Button { onSelect(svc) } label: {
                                HStack {
                                    VStack(alignment: .leading) {
                                        Text(svc.name)
                                            .font(.system(.body, design: .monospaced))
                                        Text("\(svc.type) \u{00B7} \(svc.ports.count) ports")
                                            .font(.caption)
                                            .foregroundStyle(.secondary)
                                    }
                                    Spacer()
                                }
                                .padding(.horizontal, 12)
                                .padding(.vertical, 8)
                                .background(selectedService?.id == svc.id ? Color.accentColor.opacity(0.2) : Color.clear)
                            }
                            .buttonStyle(.plain)
                        }
                    }
                }
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/DetailPanel/ConnectionEditSection.swift`
```
import SwiftUI
import Defaults

struct ConnectionEditSection: View {
    @Environment(AppState.self) private var appState
    let connection: PortForwardConnectionState
    @Binding var isExpanded: Bool

    @State private var name: String = ""
    @State private var namespace: String = ""
    @State private var service: String = ""
    @State private var localPort: String = ""
    @State private var remotePort: String = ""
    @State private var proxyPort: String = ""
    @State private var proxyEnabled: Bool = false
    @State private var autoReconnect: Bool = true
    @State private var isEnabled: Bool = true
    @State private var useDirectExec: Bool = true
    @State private var notifyOnConnect: Bool = true
    @State private var notifyOnDisconnect: Bool = true

    // Kubernetes discovery
    @State private var namespaces: [KubernetesNamespace] = []
    @State private var services: [KubernetesService] = []
    @State private var isLoadingNamespaces = false
    @State private var isLoadingServices = false
    @State private var showNamespacePicker = false
    @State private var showServicePicker = false

    var body: some View {
        VStack(spacing: 0) {
            header

            if isExpanded {
                VStack(spacing: 16) {
                    ConnectionInfoSection(
                        name: $name,
                        namespace: $namespace,
                        service: $service,
                        remotePort: $remotePort,
                        namespaces: namespaces,
                        services: services,
                        isLoadingNamespaces: isLoadingNamespaces,
                        isLoadingServices: isLoadingServices,
                        showNamespacePicker: $showNamespacePicker,
                        showServicePicker: $showServicePicker,
                        onLoadNamespaces: loadNamespaces,
                        onLoadServices: loadServices
                    )

                    Divider()

                    PortMappingSection(
                        localPort: $localPort,
                        remotePort: $remotePort,
                        proxyPort: $proxyPort,
                        proxyEnabled: proxyEnabled
                    )

                    Divider()

                    OptionsSection(
                        proxyEnabled: $proxyEnabled,
                        useDirectExec: $useDirectExec,
                        autoReconnect: $autoReconnect,
                        isEnabled: $isEnabled,
                        notifyOnConnect: $notifyOnConnect,
                        notifyOnDisconnect: $notifyOnDisconnect
                    )
                }
                .padding(16)
                .transition(.opacity.combined(with: .move(edge: .top)))
            }
        }
        .animation(.easeInOut(duration: 0.2), value: isExpanded)
        .onAppear {
            loadFromConnection()
            loadNamespaces()
            if !connection.config.namespace.isEmpty {
                loadServices(for: connection.config.namespace)
            }
        }
        .onChange(of: connection.id) { loadFromConnection() }
        .onChange(of: isExpanded) { _, expanded in
            if expanded && namespaces.isEmpty {
                loadNamespaces()
            }
        }
        .onChange(of: name) { saveToConnection() }
        .onChange(of: namespace) { saveToConnection() }
        .onChange(of: service) { saveToConnection() }
        .onChange(of: localPort) { saveToConnection() }
        .onChange(of: remotePort) { saveToConnection() }
        .onChange(of: proxyPort) { saveToConnection() }
        .onChange(of: proxyEnabled) { saveToConnection() }
        .onChange(of: autoReconnect) { saveToConnection() }
        .onChange(of: isEnabled) { saveToConnection() }
        .onChange(of: useDirectExec) { saveToConnection() }
        .onChange(of: notifyOnConnect) { saveToConnection() }
        .onChange(of: notifyOnDisconnect) { saveToConnection() }
    }

    // MARK: - Header

    private var header: some View {
        HStack {
            Button {
                withAnimation { isExpanded.toggle() }
            } label: {
                HStack(spacing: 6) {
                    Image(systemName: "chevron.right")
                        .rotationEffect(.degrees(isExpanded ? 90 : 0))
                        .font(.caption.weight(.semibold))
                        .foregroundStyle(.secondary)
                    Text("Configuration")
                        .font(.headline)
                }
            }
            .buttonStyle(.plain)

            Spacer()

            statusBadge
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 10)
    }

    private var statusBadge: some View {
        HStack(spacing: 5) {
            Circle()
                .fill(statusColor)
                .frame(width: 8, height: 8)
            Text(statusText)
                .font(.caption.weight(.medium))
        }
        .foregroundStyle(statusColor)
        .padding(.horizontal, 8)
        .padding(.vertical, 4)
        .background(statusColor.opacity(0.1), in: Capsule())
    }

    // MARK: - Kubernetes Loading

    private func loadNamespaces() {
        isLoadingNamespaces = true
        Task {
            do {
                let fetchedNamespaces = try await appState.portForwardManager.processManager.fetchNamespaces()
                await MainActor.run {
                    // Merge with manual namespaces
                    let customNamespaceNames = Defaults[.customNamespaces]
                    let customNamespaces = customNamespaceNames.map { KubernetesNamespace(name: $0, isCustom: true) }

                    // Combine and remove duplicates (prefer auto-fetched over manual)
                    var combinedNamespaces = fetchedNamespaces
                    for customNS in customNamespaces {
                        if !combinedNamespaces.contains(where: { $0.name == customNS.name }) {
                            combinedNamespaces.append(customNS)
                        }
                    }

                    namespaces = combinedNamespaces.sorted { $0.name < $1.name }
                    isLoadingNamespaces = false
                }
            } catch {
                await MainActor.run {
                    // On error, fall back to manual namespaces only
                    let customNamespaceNames = Defaults[.customNamespaces]
                    if !customNamespaceNames.isEmpty {
                        namespaces = customNamespaceNames.map { KubernetesNamespace(name: $0, isCustom: true) }
                            .sorted { $0.name < $1.name }
                    }
                    isLoadingNamespaces = false
                }
            }
        }
    }

    private func loadServices(for ns: String) {
        isLoadingServices = true
        services = []
        Task {
            do {
                let result = try await appState.portForwardManager.processManager.fetchServices(namespace: ns)
                await MainActor.run {
                    services = result
                    isLoadingServices = false
                }
            } catch {
                await MainActor.run {
                    isLoadingServices = false
                }
            }
        }
    }

    // MARK: - Status

    private var statusColor: Color {
        if connection.portForwardStatus == .error || connection.proxyStatus == .error {
            return .red
        } else if connection.isFullyConnected {
            return .green
        } else if connection.portForwardStatus == .connecting || connection.proxyStatus == .connecting {
            return .orange
        }
        return .gray
    }

    private var statusText: String {
        if connection.portForwardStatus == .error || connection.proxyStatus == .error {
            return "Error"
        } else if connection.isFullyConnected {
            return "Connected"
        } else if connection.portForwardStatus == .connecting || connection.proxyStatus == .connecting {
            return "Connecting"
        }
        return "Stopped"
    }

    // MARK: - Persistence

    private func loadFromConnection() {
        name = connection.config.name
        namespace = connection.config.namespace
        service = connection.config.service
        localPort = String(connection.config.localPort)
        remotePort = String(connection.config.remotePort)
        proxyEnabled = connection.config.proxyPort != nil
        proxyPort = connection.config.proxyPort.map { String($0) } ?? ""
        autoReconnect = connection.config.autoReconnect
        isEnabled = connection.config.isEnabled
        useDirectExec = connection.config.useDirectExec
        notifyOnConnect = connection.config.notifyOnConnect
        notifyOnDisconnect = connection.config.notifyOnDisconnect
    }

    private func saveToConnection() {
        let newConfig = PortForwardConnectionConfig(
            id: connection.id,
            name: name,
            namespace: namespace,
            service: service,
            localPort: Int(localPort) ?? connection.config.localPort,
            remotePort: Int(remotePort) ?? connection.config.remotePort,
            proxyPort: proxyEnabled ? Int(proxyPort) : nil,
            isEnabled: isEnabled,
            autoReconnect: autoReconnect,
            useDirectExec: useDirectExec,
            notifyOnConnect: notifyOnConnect,
            notifyOnDisconnect: notifyOnDisconnect
        )
        appState.portForwardManager.updateConnection(newConfig)
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/DetailPanel/ConnectionInfoSection.swift`
```
import SwiftUI

struct ConnectionInfoSection: View {
    @Binding var name: String
    @Binding var namespace: String
    @Binding var service: String
    @Binding var remotePort: String

    let namespaces: [KubernetesNamespace]
    let services: [KubernetesService]
    let isLoadingNamespaces: Bool
    let isLoadingServices: Bool
    @Binding var showNamespacePicker: Bool
    @Binding var showServicePicker: Bool

    let onLoadNamespaces: () -> Void
    let onLoadServices: (String) -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Label("Connection", systemImage: "link")
                .font(.subheadline.weight(.semibold))
                .foregroundStyle(.secondary)

            VStack(spacing: 10) {
                HStack(spacing: 10) {
                    Image(systemName: "tag")
                        .foregroundStyle(.tertiary)
                        .frame(width: 16, height: 22, alignment: .center)
                    TextField("Connection name", text: $name)
                        .textFieldStyle(.roundedBorder)
                }

                HStack(spacing: 10) {
                    Image(systemName: "folder")
                        .foregroundStyle(.tertiary)
                        .frame(width: 16, height: 22, alignment: .center)

                    // Namespace picker
                    Button {
                        showNamespacePicker.toggle()
                    } label: {
                        HStack {
                            Text(namespace.isEmpty ? "namespace" : namespace)
                                .foregroundStyle(namespace.isEmpty ? .tertiary : .primary)
                            Spacer()
                            if isLoadingNamespaces {
                                ProgressView()
                                    .controlSize(.small)
                            } else {
                                Image(systemName: "chevron.up.chevron.down")
                                    .foregroundStyle(.secondary)
                                    .font(.caption)
                            }
                        }
                        .padding(.horizontal, 8)
                        .padding(.vertical, 4)
                        .background(Color(nsColor: .controlBackgroundColor))
                        .cornerRadius(6)
                        .overlay(
                            RoundedRectangle(cornerRadius: 6)
                                .stroke(Color(nsColor: .separatorColor), lineWidth: 1)
                        )
                    }
                    .buttonStyle(.plain)
                    .frame(maxWidth: 140)
                    .popover(isPresented: $showNamespacePicker, arrowEdge: .bottom) {
                        SearchablePickerView(
                            items: namespaces.map(\.name),
                            selection: namespace,
                            isLoading: isLoadingNamespaces,
                            placeholder: "Search namespaces...",
                            onSelect: { selected in
                                namespace = selected
                                onLoadServices(selected)
                                showNamespacePicker = false
                            },
                            onRefresh: { onLoadNamespaces() }
                        )
                    }

                    Image(systemName: "server.rack")
                        .foregroundStyle(.tertiary)
                        .frame(width: 16, height: 22, alignment: .center)

                    // Service picker
                    Button {
                        showServicePicker.toggle()
                    } label: {
                        HStack {
                            Text(service.isEmpty ? "service" : service)
                                .foregroundStyle(service.isEmpty ? .tertiary : .primary)
                            Spacer()
                            if isLoadingServices {
                                ProgressView()
                                    .controlSize(.small)
                            } else {
                                Image(systemName: "chevron.up.chevron.down")
                                    .foregroundStyle(.secondary)
                                    .font(.caption)
                            }
                        }
                        .padding(.horizontal, 8)
                        .padding(.vertical, 4)
                        .background(Color(nsColor: .controlBackgroundColor))
                        .cornerRadius(6)
                        .overlay(
                            RoundedRectangle(cornerRadius: 6)
                                .stroke(Color(nsColor: .separatorColor), lineWidth: 1)
                        )
                    }
                    .buttonStyle(.plain)
                    .popover(isPresented: $showServicePicker, arrowEdge: .bottom) {
                        SearchablePickerView(
                            items: services.map(\.name),
                            selection: service,
                            isLoading: isLoadingServices,
                            placeholder: "Search services...",
                            onSelect: { selected in
                                service = selected
                                // Auto-fill remote port
                                if let svc = services.first(where: { $0.name == selected }),
                                   let firstPort = svc.ports.first {
                                    remotePort = String(firstPort.port)
                                }
                                showServicePicker = false
                            },
                            onRefresh: { onLoadServices(namespace) }
                        )
                    }
                }
            }
            .font(.system(.body, design: .monospaced))
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/DetailPanel/ConnectionLogPanel.swift`
```
import SwiftUI

struct ConnectionLogPanel: View {
    @Environment(AppState.self) private var appState
    let connection: PortForwardConnectionState?
    @State private var showDetails = true

    var body: some View {
        VStack(spacing: 0) {
            if let conn = connection {
                // Edit Form Section
                ConnectionEditSection(connection: conn, isExpanded: $showDetails)

                Divider()

                // Logs Section
                ConnectionLogsSection(connection: conn)
            } else {
                // Empty state
                VStack(spacing: 8) {
                    Spacer()
                    Image(systemName: "sidebar.right")
                        .font(.system(size: 32))
                        .foregroundStyle(.tertiary)
                    Text("Select a connection")
                        .foregroundStyle(.secondary)
                    Text("Click on a connection to view details and logs")
                        .font(.caption)
                        .foregroundStyle(.tertiary)
                    Spacer()
                }
            }
        }
        .background(Color(nsColor: .textBackgroundColor))
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/DetailPanel/ConnectionLogsSection.swift`
```
import SwiftUI

struct ConnectionLogsSection: View {
    let connection: PortForwardConnectionState

    private static let dateFormatter: DateFormatter = {
        let df = DateFormatter()
        df.dateFormat = "HH:mm:ss"
        return df
    }()

    var body: some View {
        VStack(spacing: 0) {
            // Logs header
            HStack {
                Text("Logs")
                    .font(.headline)

                if !connection.logs.isEmpty {
                    Text("(\(connection.logs.count))")
                        .font(.caption)
                        .foregroundStyle(.tertiary)
                }

                Spacer()

                if !connection.logs.isEmpty {
                    Button {
                        ClipboardService.copyLogsAsMarkdown(connection.logs, connectionName: connection.config.name)
                    } label: {
                        Image(systemName: "doc.on.doc")
                    }
                    .buttonStyle(.borderless)
                    .help("Copy All Logs (Markdown)")

                    Button {
                        connection.clearLogs()
                    } label: {
                        Image(systemName: "trash")
                    }
                    .buttonStyle(.borderless)
                    .help("Clear Logs")
                }
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 10)

            Divider()

            if connection.logs.isEmpty {
                VStack(spacing: 8) {
                    Spacer()
                    Image(systemName: "text.alignleft")
                        .font(.system(size: 24))
                        .foregroundStyle(.tertiary)
                    Text("No logs yet")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    Spacer()
                }
            } else {
                ScrollViewReader { proxy in
                    ScrollView {
                        LazyVStack(alignment: .leading, spacing: 2) {
                            ForEach(connection.logs) { log in
                                HStack(alignment: .top, spacing: 8) {
                                    Text(Self.dateFormatter.string(from: log.timestamp))
                                        .font(.system(.caption, design: .monospaced))
                                        .foregroundStyle(.tertiary)

                                    Text(log.type == .portForward ? "kubectl" : "socat")
                                        .font(.system(.caption, design: .monospaced))
                                        .foregroundStyle(log.type == .portForward ? .blue : .purple)
                                        .frame(width: 50, alignment: .leading)

                                    Text(log.message)
                                        .font(.system(.caption, design: .monospaced))
                                        .foregroundStyle(log.isError ? .red : .primary)
                                        .textSelection(.enabled)
                                        .frame(maxWidth: .infinity, alignment: .leading)
                                }
                                .id(log.id)
                            }
                        }
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .padding(12)
                    }
                    .onChange(of: connection.logs.count) {
                        if let lastLog = connection.logs.last {
                            withAnimation {
                                proxy.scrollTo(lastLog.id, anchor: .bottom)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/DetailPanel/OptionsSection.swift`
```
import SwiftUI

struct OptionsSection: View {
    @Binding var proxyEnabled: Bool
    @Binding var useDirectExec: Bool
    @Binding var autoReconnect: Bool
    @Binding var isEnabled: Bool
    @Binding var notifyOnConnect: Bool
    @Binding var notifyOnDisconnect: Bool

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Label("Options", systemImage: "gearshape")
                .font(.subheadline.weight(.semibold))
                .foregroundStyle(.secondary)

            HStack(spacing: 20) {
                Toggle(isOn: $proxyEnabled) {
                    Label("Proxy", systemImage: "network")
                }
                .toggleStyle(.switch)
                .controlSize(.small)

                if proxyEnabled {
                    Toggle(isOn: $useDirectExec) {
                        Label("Multi-conn", systemImage: "arrow.triangle.branch")
                    }
                    .toggleStyle(.switch)
                    .controlSize(.small)
                    .help("Enable multiple simultaneous connections")
                }

                Spacer()
            }

            HStack(spacing: 20) {
                Toggle(isOn: $autoReconnect) {
                    Label("Auto Reconnect", systemImage: "arrow.clockwise")
                }
                .toggleStyle(.checkbox)

                Toggle(isOn: $isEnabled) {
                    Label("Enabled", systemImage: "power")
                }
                .toggleStyle(.checkbox)

                Spacer()
            }
            .font(.callout)

            HStack(spacing: 20) {
                Toggle(isOn: $notifyOnConnect) {
                    Label("Notify on Connect", systemImage: "bell")
                }
                .toggleStyle(.checkbox)

                Toggle(isOn: $notifyOnDisconnect) {
                    Label("Notify on Disconnect", systemImage: "bell.slash")
                }
                .toggleStyle(.checkbox)

                Spacer()
            }
            .font(.callout)
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/DetailPanel/PortMappingSection.swift`
```
import SwiftUI

struct PortMappingSection: View {
    @Binding var localPort: String
    @Binding var remotePort: String
    @Binding var proxyPort: String
    let proxyEnabled: Bool

    var body: some View {
        VStack(spacing: 12) {
            HStack {
                Label("Port Mapping", systemImage: "arrow.left.arrow.right")
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(.secondary)
                Spacer()
            }

            // Port flow visualization - centered
            HStack(alignment: .bottom, spacing: 8) {
                // Proxy port (if enabled)
                if proxyEnabled {
                    VStack(spacing: 4) {
                        Text("Proxy")
                            .font(.caption2)
                            .foregroundStyle(.tertiary)
                        TextField("port", text: $proxyPort)
                            .textFieldStyle(.roundedBorder)
                            .frame(width: 70)
                            .multilineTextAlignment(.center)
                    }

                    Image(systemName: "arrow.right")
                        .foregroundStyle(.tertiary)
                        .frame(height: 22)
                }

                // Local port
                VStack(spacing: 4) {
                    Text("Local")
                        .font(.caption2)
                        .foregroundStyle(.tertiary)
                    TextField("port", text: $localPort)
                        .textFieldStyle(.roundedBorder)
                        .frame(width: 70)
                        .multilineTextAlignment(.center)
                }

                Image(systemName: "arrow.right")
                    .foregroundStyle(.blue)
                    .frame(height: 22)

                // Kubernetes icon
                Image(systemName: "cloud")
                    .foregroundStyle(.blue)
                    .font(.title3)
                    .frame(height: 22)

                Image(systemName: "arrow.right")
                    .foregroundStyle(.blue)
                    .frame(height: 22)

                // Remote port
                VStack(spacing: 4) {
                    Text("Remote")
                        .font(.caption2)
                        .foregroundStyle(.tertiary)
                    TextField("port", text: $remotePort)
                        .textFieldStyle(.roundedBorder)
                        .frame(width: 70)
                        .multilineTextAlignment(.center)
                }
            }
            .font(.system(.body, design: .monospaced))
            .frame(maxWidth: .infinity)
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/DetailPanel/SearchablePickerView.swift`
```
import SwiftUI

struct SearchablePickerView: View {
    let items: [String]
    let selection: String
    let isLoading: Bool
    let placeholder: String
    let onSelect: (String) -> Void
    let onRefresh: () -> Void

    @State private var searchText = ""
    @FocusState private var isSearchFocused: Bool

    private var filteredItems: [String] {
        if searchText.isEmpty {
            return items
        }
        return items.filter { $0.localizedCaseInsensitiveContains(searchText) }
    }

    var body: some View {
        VStack(spacing: 0) {
            // Search field
            HStack(spacing: 8) {
                Image(systemName: "magnifyingglass")
                    .foregroundStyle(.secondary)
                TextField(placeholder, text: $searchText)
                    .textFieldStyle(.plain)
                    .focused($isSearchFocused)
                if !searchText.isEmpty {
                    Button {
                        searchText = ""
                    } label: {
                        Image(systemName: "xmark.circle.fill")
                            .foregroundStyle(.secondary)
                    }
                    .buttonStyle(.plain)
                }
            }
            .padding(8)
            .background(Color(nsColor: .controlBackgroundColor))

            Divider()

            // List
            if isLoading {
                HStack {
                    Spacer()
                    ProgressView()
                        .controlSize(.small)
                    Text("Loading...")
                        .foregroundStyle(.secondary)
                    Spacer()
                }
                .padding()
            } else if filteredItems.isEmpty {
                VStack(spacing: 8) {
                    if items.isEmpty {
                        Text("No items")
                            .foregroundStyle(.secondary)
                        Button("Refresh") { onRefresh() }
                            .buttonStyle(.bordered)
                    } else {
                        Text("No matches")
                            .foregroundStyle(.secondary)
                    }
                }
                .padding()
            } else {
                ScrollView {
                    LazyVStack(spacing: 0) {
                        ForEach(filteredItems, id: \.self) { item in
                            Button {
                                onSelect(item)
                            } label: {
                                HStack {
                                    if item == selection {
                                        Image(systemName: "checkmark")
                                            .foregroundStyle(.blue)
                                            .frame(width: 16)
                                    } else {
                                        Color.clear.frame(width: 16)
                                    }
                                    Text(item)
                                        .font(.system(.body, design: .monospaced))
                                    Spacer()
                                }
                                .padding(.horizontal, 10)
                                .padding(.vertical, 6)
                                .contentShape(Rectangle())
                            }
                            .buttonStyle(.plain)
                            .background(item == selection ? Color.accentColor.opacity(0.1) : Color.clear)
                        }
                    }
                }
                .frame(maxHeight: 200)
            }

            Divider()

            // Refresh button
            Button {
                onRefresh()
            } label: {
                HStack {
                    Image(systemName: "arrow.clockwise")
                    Text("Refresh")
                }
                .frame(maxWidth: .infinity)
                .padding(.vertical, 6)
            }
            .buttonStyle(.plain)
            .background(Color(nsColor: .controlBackgroundColor))
        }
        .frame(width: 220)
        .onAppear {
            isSearchFocused = true
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/Settings/DependencyRow.swift`
```
import SwiftUI
import AppKit
import Defaults

struct DependencyRow: View {
    let name: String
    let dependency: PortForwardDependency
    let currentPath: String?
    let isCustom: Bool
    let customPathKey: Defaults.Key<String?>

    @State private var isInstalling = false

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            // Status row
            HStack {
                Text(name)
                    .font(.headline)

                Spacer()

                if currentPath != nil {
                    HStack(spacing: 4) {
                        Image(systemName: "checkmark.circle.fill")
                            .foregroundStyle(.green)
                        Text("Installed")
                            .foregroundStyle(.secondary)
                    }
                } else {
                    if isInstalling {
                        ProgressView()
                            .scaleEffect(0.7)
                    } else {
                        Button("Install") {
                            install()
                        }
                        .buttonStyle(.bordered)
                        .controlSize(.small)
                    }

                    if !dependency.isRequired {
                        Text("(optional)")
                            .font(.caption)
                            .foregroundStyle(.tertiary)
                    }
                }
            }

            // Path row
            if let path = currentPath {
                HStack(spacing: 8) {
                    Text(path)
                        .font(.system(.caption, design: .monospaced))
                        .foregroundStyle(.secondary)
                        .lineLimit(1)
                        .truncationMode(.middle)

                    if isCustom {
                        Text("(custom)")
                            .font(.caption2)
                            .foregroundStyle(.orange)
                    } else {
                        Text("(auto)")
                            .font(.caption2)
                            .foregroundStyle(.tertiary)
                    }

                    Spacer()

                    Button("Browse...") {
                        browseForPath()
                    }
                    .buttonStyle(.borderless)
                    .controlSize(.small)

                    if isCustom {
                        Button("Reset") {
                            Defaults[customPathKey] = nil
                        }
                        .buttonStyle(.borderless)
                        .controlSize(.small)
                        .foregroundStyle(.secondary)
                    }
                }
            }
        }
        .padding(.vertical, 4)
    }

    private func install() {
        isInstalling = true
        Task {
            _ = await DependencyChecker.shared.checkAndInstallMissing()
            await MainActor.run { isInstalling = false }
        }
    }

    private func browseForPath() {
        let panel = NSOpenPanel()
        panel.title = "Select \(name) executable"
        panel.allowsMultipleSelection = false
        panel.canChooseDirectories = false
        panel.canChooseFiles = true
        panel.directoryURL = URL(fileURLWithPath: "/usr/local/bin")

        if panel.runModal() == .OK, let url = panel.url {
            Defaults[customPathKey] = url.path
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/TableComponents/PortForwarderTableHeader.swift`
```
import SwiftUI

struct PortForwarderTableHeader: View {
    var body: some View {
        HStack(spacing: 0) {
            Text("Status")
                .frame(width: 80, alignment: .leading)
            Text("Name")
                .frame(maxWidth: .infinity, alignment: .leading)
            Text("Service")
                .frame(maxWidth: .infinity, alignment: .leading)
            Text("Port")
                .frame(width: 80, alignment: .leading)
            Text("Actions")
                .frame(width: 80, alignment: .center)
        }
        .font(.caption.weight(.medium))
        .foregroundStyle(.secondary)
        .padding(.horizontal, 12)
        .padding(.vertical, 6)
        .background(Color(nsColor: .windowBackgroundColor))
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/TableComponents/PortForwarderTableRow.swift`
```
import SwiftUI

struct PortForwarderTableRow: View {
    @Environment(AppState.self) private var appState
    let connection: PortForwardConnectionState
    let isSelected: Bool
    let onSelect: () -> Void

    private var statusColor: Color {
        if connection.portForwardStatus == .error || connection.proxyStatus == .error {
            return .red
        } else if connection.isFullyConnected {
            return .green
        } else if connection.portForwardStatus == .connecting || connection.proxyStatus == .connecting {
            return .orange
        }
        return .gray
    }

    private var statusText: String {
        if connection.portForwardStatus == .error || connection.proxyStatus == .error {
            return "Error"
        } else if connection.isFullyConnected {
            return "Connected"
        } else if connection.portForwardStatus == .connecting || connection.proxyStatus == .connecting {
            return "Connecting"
        }
        return "Stopped"
    }

    private var isConnecting: Bool {
        connection.portForwardStatus == .connecting || connection.proxyStatus == .connecting
    }

    var body: some View {
        HStack(spacing: 0) {
            // Status
            HStack(spacing: 4) {
                Circle()
                    .fill(statusColor)
                    .frame(width: 8, height: 8)
                Text(statusText)
                    .font(.caption)
                    .foregroundStyle(statusColor)
            }
            .frame(width: 80, alignment: .leading)

            // Name
            Text(connection.config.name)
                .font(.body)
                .lineLimit(1)
                .frame(maxWidth: .infinity, alignment: .leading)

            // Service
            Text(connection.config.service)
                .font(.caption)
                .foregroundStyle(.secondary)
                .lineLimit(1)
                .frame(maxWidth: .infinity, alignment: .leading)

            // Port
            Text(":" + String(connection.effectivePort))
                .font(.system(.caption, design: .monospaced))
                .frame(width: 80, alignment: .leading)

            // Actions
            HStack(spacing: 4) {
                if isConnecting {
                    Button {
                        appState.portForwardManager.stopConnection(connection.id)
                    } label: {
                        ProgressView()
                            .scaleEffect(0.5)
                    }
                    .buttonStyle(.plain)
                    .frame(width: 24, height: 24)
                } else if connection.isFullyConnected {
                    Button {
                        appState.portForwardManager.stopConnection(connection.id)
                    } label: {
                        Image(systemName: "stop.fill")
                            .foregroundStyle(.red)
                    }
                    .buttonStyle(.plain)
                    .help("Stop")
                } else {
                    Button {
                        appState.portForwardManager.startConnection(connection.id)
                    } label: {
                        Image(systemName: "play.fill")
                            .foregroundStyle(.green)
                    }
                    .buttonStyle(.plain)
                    .help("Start")
                }

                Button {
                    appState.portForwardManager.removeConnection(connection.id)
                } label: {
                    Image(systemName: "trash")
                        .foregroundStyle(.secondary)
                }
                .buttonStyle(.plain)
                .help("Delete")
            }
            .frame(width: 80, alignment: .center)
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 6)
        .frame(maxWidth: .infinity)
        .background(isSelected ? Color.accentColor.opacity(0.15) : Color.clear)
        .contentShape(Rectangle())
        .onTapGesture {
            onSelect()
        }
        .contextMenu {
            if connection.isFullyConnected {
                Button {
                    appState.portForwardManager.stopConnection(connection.id)
                } label: {
                    Label("Stop", systemImage: "stop.fill")
                }
            } else if isConnecting {
                Button {
                    appState.portForwardManager.stopConnection(connection.id)
                } label: {
                    Label("Cancel", systemImage: "xmark")
                }
            } else {
                Button {
                    appState.portForwardManager.startConnection(connection.id)
                } label: {
                    Label("Start", systemImage: "play.fill")
                }
            }

            Button {
                appState.portForwardManager.restartConnection(connection.id)
            } label: {
                Label("Restart", systemImage: "arrow.clockwise")
            }
            .disabled(!connection.isFullyConnected)

            Divider()

            Button(role: .destructive) {
                appState.portForwardManager.removeConnection(connection.id)
            } label: {
                Label("Delete", systemImage: "trash")
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/Tabs/ConnectionsTab.swift`
```
import SwiftUI

struct ConnectionsTab: View {
    @Environment(AppState.self) private var appState
    @Binding var discoveryManager: KubernetesDiscoveryManager?
    @State private var selectedConnectionId: UUID?

    private var selectedConnection: PortForwardConnectionState? {
        guard let id = selectedConnectionId else { return nil }
        return appState.portForwardManager.connections.first { $0.id == id }
    }

    var body: some View {
        HSplitView {
            // Left: Connection list
            VStack(spacing: 0) {
                // Header with action buttons
                HStack {
                    Text("Connections")
                        .font(.headline)

                    Spacer()

                    Button {
                        let config = PortForwardConnectionConfig(
                            name: "New Connection",
                            namespace: "default",
                            service: "service-name",
                            localPort: 8080,
                            remotePort: 80
                        )
                        appState.portForwardManager.addConnection(config)
                    } label: {
                        Label("Add", systemImage: "plus.circle.fill")
                    }
                    .buttonStyle(.bordered)
                    .help("Add Connection")

                    Button {
                        let dm = KubernetesDiscoveryManager(processManager: appState.portForwardManager.processManager)
                        Task { await dm.loadNamespaces() }
                        discoveryManager = dm
                    } label: {
                        Label("Import", systemImage: "square.and.arrow.down.fill")
                    }
                    .buttonStyle(.bordered)
                    .disabled(!DependencyChecker.shared.allRequiredInstalled)
                    .help("Import from Kubernetes")
                }
                .padding(.horizontal, 20)
                .padding(.vertical, 12)

                Divider()

                // Dependency warning
                if !DependencyChecker.shared.allRequiredInstalled {
                    DependencyWarningBanner()
                }

                ScrollView {
                    VStack(alignment: .leading, spacing: 8) {
                        ForEach(appState.portForwardManager.connections) { connection in
                            PortForwardConnectionCard(
                                connection: connection,
                                isSelected: selectedConnectionId == connection.id,
                                onSelect: { selectedConnectionId = connection.id }
                            )
                        }
                    }
                    .padding(16)
                }

                Divider()

                // Status bar
                HStack {
                    let manager = appState.portForwardManager
                    if manager.connections.isEmpty {
                        Text("No connections configured")
                    } else {
                        Text("\(manager.connectedCount) of \(manager.connections.count) connected")
                    }

                    Spacer()

                    if manager.isKillingProcesses {
                        ProgressView()
                            .scaleEffect(0.7)
                        Text("Killing processes...")
                            .foregroundStyle(.secondary)
                    } else if !manager.connections.isEmpty {
                        Button("Kill All Stuck") {
                            Task { await manager.killStuckProcesses() }
                        }
                        .buttonStyle(.bordered)
                        .controlSize(.small)

                        Button("Start All") {
                            manager.startAll()
                        }
                        .buttonStyle(.bordered)
                        .disabled(manager.allConnected)

                        Button("Stop All") {
                            manager.stopAll()
                        }
                        .buttonStyle(.bordered)
                        .disabled(manager.connectedCount == 0)
                    }
                }
                .font(.caption)
                .foregroundStyle(.secondary)
                .padding(.horizontal, 16)
                .padding(.vertical, 10)
                .background(Color(nsColor: .windowBackgroundColor))
            }
            .frame(minWidth: 400)

            // Right: Log viewer
            ConnectionLogPanel(connection: selectedConnection)
                .frame(minWidth: 450)
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/Tabs/PortForwarderSettingsTab.swift`
```
import SwiftUI

struct PortForwarderSettingsTab: View {
    @AppStorage("portForwardAutoStart") private var autoStart = false
    @AppStorage("portForwardShowNotifications") private var showNotifications = true

    var body: some View {
        Form {
            Section("Startup") {
                Toggle("Auto-start connections on app launch", isOn: $autoStart)
            }

            Section("Notifications") {
                Toggle("Show connection notifications", isOn: $showNotifications)
            }

            Section("Dependencies") {
                DependencyRow(
                    name: "kubectl",
                    dependency: DependencyChecker.shared.kubectl,
                    currentPath: DependencyChecker.shared.kubectlPath,
                    isCustom: DependencyChecker.shared.isUsingCustomKubectl,
                    customPathKey: .customKubectlPath
                )

                DependencyRow(
                    name: "socat",
                    dependency: DependencyChecker.shared.socat,
                    currentPath: DependencyChecker.shared.socatPath,
                    isCustom: DependencyChecker.shared.isUsingCustomSocat,
                    customPathKey: .customSocatPath
                )
            }
        }
        .formStyle(.grouped)
        .scrollContentBackground(.hidden)
    }
}
```

## File: `platforms/macos/Sources/Views/PortForwarder/Tabs/ServiceBrowserTab.swift`
```
import SwiftUI

struct ServiceBrowserTab: View {
    @Environment(AppState.self) private var appState
    @State private var discoveryManager: KubernetesDiscoveryManager?

    var body: some View {
        VStack {
            if let dm = discoveryManager {
                ServiceBrowserEmbedded(
                    discoveryManager: dm,
                    onServiceSelected: { config in
                        appState.portForwardManager.addConnection(config)
                    }
                )
            } else {
                VStack(spacing: 16) {
                    Image(systemName: "magnifyingglass")
                        .font(.system(size: 48))
                        .foregroundStyle(.tertiary)

                    Text("Kubernetes Service Browser")
                        .font(.title2)

                    Text("Browse your Kubernetes cluster to find services and create port-forward connections.")
                        .foregroundStyle(.secondary)
                        .multilineTextAlignment(.center)
                        .frame(maxWidth: 400)

                    Button("Start Browsing") {
                        let dm = KubernetesDiscoveryManager(processManager: appState.portForwardManager.processManager)
                        Task { await dm.loadNamespaces() }
                        discoveryManager = dm
                    }
                    .buttonStyle(.borderedProminent)
                    .disabled(!DependencyChecker.shared.allRequiredInstalled)

                    if !DependencyChecker.shared.allRequiredInstalled {
                        Text("kubectl is required")
                            .font(.caption)
                            .foregroundStyle(.orange)
                    }
                }
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            }
        }
    }
}

struct ServiceBrowserEmbedded: View {
    @Bindable var discoveryManager: KubernetesDiscoveryManager
    let onServiceSelected: (PortForwardConnectionConfig) -> Void

    var body: some View {
        VStack(spacing: 0) {
            // 3 panel layout
            HStack(spacing: 0) {
                // Namespace List
                NamespacePanel(
                    namespaces: discoveryManager.namespaces,
                    selectedNamespace: discoveryManager.selectedNamespace,
                    state: discoveryManager.namespaceState,
                    onSelect: { namespace in
                        Task { await discoveryManager.selectNamespace(namespace) }
                    },
                    onRefresh: {
                        Task { await discoveryManager.loadNamespaces() }
                    },
                    onAddCustom: { namespaceNames in
                        discoveryManager.addCustomNamespaces(namespaceNames)
                    },
                    onRemoveCustom: { namespace in
                        discoveryManager.removeCustomNamespace(namespace)
                    }
                )
                .frame(width: 200)

                Divider()

                // Service List
                ServicePanel(
                    services: discoveryManager.services,
                    selectedService: discoveryManager.selectedService,
                    state: discoveryManager.serviceState,
                    onSelect: { service in
                        discoveryManager.selectService(service)
                    }
                )
                .frame(minWidth: 250)

                Divider()

                // Port Selection
                PortPanel(
                    service: discoveryManager.selectedService,
                    selectedPort: discoveryManager.selectedPort,
                    proxyEnabled: $discoveryManager.proxyEnabled,
                    discoveryManager: discoveryManager,
                    onPortSelect: { port in
                        discoveryManager.selectPort(port)
                    },
                    onAdd: {
                        if let config = discoveryManager.createConnectionConfig() {
                            onServiceSelected(config)
                        }
                    }
                )
                .frame(width: 250)
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/PortTable/PortListRow.swift`
```
/// PortListRow - Individual port row component for table view
///
/// Thin wrapper around PortRowView with table style.
/// Maintains backward compatibility with existing usage.

import SwiftUI

struct PortListRow: View {
    let port: PortInfo

    var body: some View {
        PortRowView(port: port, style: .table)
    }
}
```

## File: `platforms/macos/Sources/Views/PortTable/PortSortOptions.swift`
```
/// PortSortOptions - Sorting configuration for port table
///
/// Defines available sort orders for the port table view:
/// - Port number
/// - Process name
/// - PID
/// - Type (process category)
/// - Address
/// - User
/// - Actions (favorite/watched status)
///
/// - Note: Each sort order can be ascending or descending.

import Foundation

/// Available sort orders for port table
enum SortOrder: String, CaseIterable {
    case port = "Port"
    case process = "Process"
    case pid = "PID"
    case type = "Type"
    case address = "Address"
    case user = "User"
    case actions = "Actions"
}
```

## File: `platforms/macos/Sources/Views/PortTable/PortTableView.swift`
```
/// PortTableView - Main port table display
///
/// Displays ports in a sortable table format with support for:
/// - List view (flat list of all ports)
/// - Tree view (grouped by process)
/// - Column sorting (port, process, PID, type, address, user, actions)
/// - Empty state when no ports are found
///
/// - Note: Uses LazyVStack for performance with large port lists.
/// - Important: Integrates with AppState for port management.

import SwiftUI
import Defaults

struct PortTableView: View {
    @Environment(AppState.self) private var appState
    @State private var sortOrder: SortOrder = .port
    @State private var sortAscending = true
    @Default(.useTreeView) private var useTreeView
    @State private var expandedProcesses: Set<String> = []

    var body: some View {
        VStack(spacing: 0) {
            // Header
            headerRow

            Divider()

            // Port List
            if appState.filteredPorts.isEmpty {
                emptyState
            } else {
                ScrollView {
                    LazyVStack(spacing: 0) {
                        if useTreeView {
                            treeView
                        } else {
                            listView
                        }
                    }
                }
            }
        }
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                Button {
                    useTreeView.toggle()
                } label: {
                    Label(useTreeView ? "List View" : "Tree View", systemImage: useTreeView ? "list.bullet" : "list.bullet.indent")
                }
                .help(useTreeView ? "Switch to List View" : "Switch to Tree View")
            }
        }
        .onChange(of: appState.ports) { _, _ in
            let visibleProcessIDs = Set(groupedPorts.map(\.id))
            expandedProcesses = expandedProcesses.intersection(visibleProcessIDs)
        }
    }

    // MARK: - Header Row

    private var headerRow: some View {
        HStack(spacing: 0) {
            // Favorite header (centered)
            Button {
                if sortOrder == .actions {
                    sortAscending.toggle()
                } else {
                    sortOrder = .actions
                    sortAscending = true
                }
            } label: {
                HStack(spacing: 4) {
                    Text("★")
                        .font(.caption.weight(.medium))
                    if sortOrder == .actions {
                        Image(systemName: sortAscending ? "chevron.up" : "chevron.down")
                            .font(.caption2)
                    }
                }
                .foregroundStyle(sortOrder == .actions ? .primary : .secondary)
            }
            .buttonStyle(.plain)
            .frame(width: 40, alignment: .center)

            // Account for status indicator circle space
            Spacer()
                .frame(width: 16)
            headerButton("Port", .port, width: 70)
            // Process column (flexible)
            Button {
                if sortOrder == .process {
                    sortAscending.toggle()
                } else {
                    sortOrder = .process
                    sortAscending = true
                }
            } label: {
                HStack(spacing: 4) {
                    Text("Process")
                        .font(.caption.weight(.medium))
                    if sortOrder == .process {
                        Image(systemName: sortAscending ? "chevron.up" : "chevron.down")
                            .font(.caption2)
                    }
                }
                .foregroundStyle(sortOrder == .process ? .primary : .secondary)
            }
            .buttonStyle(.plain)
            .frame(minWidth: 150, maxWidth: .infinity, alignment: .leading)

            headerButton("PID", .pid, width: 70)
            headerButton("Type", .type, width: 100)
            headerButton("Address", .address, width: 80)
            headerButton("User", .user, width: 70)
            Spacer()
            Text("Actions")
                .font(.caption.weight(.medium))
                .foregroundStyle(.secondary)
                .frame(width: 80)
        }
        .padding(.leading, 16)
        .padding(.trailing, 16)
        .padding(.vertical, 8)
        .background(Color(nsColor: .controlBackgroundColor))
    }

    /// Creates a sortable header button
    private func headerButton(_ title: String, _ order: SortOrder, width: CGFloat) -> some View {
        Button {
            if sortOrder == order {
                sortAscending.toggle()
            } else {
                sortOrder = order
                sortAscending = true
            }
        } label: {
            HStack(spacing: 4) {
                Text(title)
                    .font(.caption.weight(.medium))
                if sortOrder == order {
                    Image(systemName: sortAscending ? "chevron.up" : "chevron.down")
                        .font(.caption2)
                }
            }
            .foregroundStyle(sortOrder == order ? .primary : .secondary)
        }
        .buttonStyle(.plain)
        .frame(width: width, alignment: .leading)
    }

    // MARK: - Empty State

    private var emptyState: some View {
        ContentUnavailableView {
            Label("No Ports", systemImage: "network.slash")
        } description: {
            Text("No listening ports found")
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }

    // MARK: - View Modes

    /// Tree view groups ports by process
    private var treeView: some View {
        ForEach(groupedPorts) { group in
            ProcessGroupListRow(
                group: group,
                isExpanded: expandedProcesses.contains(group.id),
                onToggleExpand: {
                    if expandedProcesses.contains(group.id) {
                        expandedProcesses.remove(group.id)
                    } else {
                        expandedProcesses.insert(group.id)
                    }
                }
            )

            if expandedProcesses.contains(group.id) {
                ForEach(group.ports) { port in
                    NestedPortListRow(port: port)
                        .background(appState.selectedPortID == port.id ? Color.accentColor.opacity(0.2) : Color.clear)
                        .contentShape(Rectangle())
                        .onTapGesture {
                            appState.selectedPortID = port.id
                        }
                }
            }
        }
    }

    /// List view shows flat list of ports
    private var listView: some View {
        ForEach(sortedPorts) { port in
            PortListRow(port: port)
                .background(appState.selectedPortID == port.id ? Color.accentColor.opacity(0.2) : Color.clear)
                .contentShape(Rectangle())
                .onTapGesture {
                    appState.selectedPortID = port.id
                }
        }
    }

    // MARK: - Data Processing

    /// Groups ports by process for tree view
    private var groupedPorts: [ProcessGroup] {
        let grouped = Dictionary(grouping: appState.filteredPorts) { $0.processName }
        return grouped.map { name, ports in
            ProcessGroup(
                id: name,
                processName: name,
                pids: Array(Set(ports.map(\.pid))).sorted(),
                ports: ports.sorted { $0.port < $1.port }
            )
        }.sorted { $0.processName.localizedCaseInsensitiveCompare($1.processName) == .orderedAscending }
    }

    /// Sorts ports based on current sort order
    private var sortedPorts: [PortInfo] {
        let ports = appState.filteredPorts
        return ports.sorted { a, b in
            let result: Bool
            switch sortOrder {
            case .port:
                result = a.port < b.port
            case .process:
                result = a.processName.localizedCaseInsensitiveCompare(b.processName) == .orderedAscending
            case .pid:
                result = a.pid < b.pid
            case .type:
                result = a.processType.rawValue < b.processType.rawValue
            case .address:
                result = a.address.localizedCaseInsensitiveCompare(b.address) == .orderedAscending
            case .user:
                result = a.user.localizedCaseInsensitiveCompare(b.user) == .orderedAscending
            case .actions:
                // Sort by favorite/watched status
                let aIsFavorite = appState.isFavorite(a.port)
                let aIsWatching = appState.isWatching(a.port)
                let bIsFavorite = appState.isFavorite(b.port)
                let bIsWatching = appState.isWatching(b.port)

                // Priority: Favorite > Watching > Neither
                let aPriority = aIsFavorite ? 2 : (aIsWatching ? 1 : 0)
                let bPriority = bIsFavorite ? 2 : (bIsWatching ? 1 : 0)

                if aPriority != bPriority {
                    result = aPriority > bPriority
                } else {
                    // Same priority, sort by port number
                    result = a.port < b.port
                }
            }
            return sortAscending ? result : !result
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Settings/AutoKillSettingsSection.swift`
```
import SwiftUI
import Defaults

struct AutoKillSettingsSection: View {
    @Default(.autoKillRules) private var rules
    @State private var editingRule: AutoKillRule?
    @State private var isAddingRule = false

    var body: some View {
        SettingsGroup("Auto-Kill Rules", icon: "clock.badge.xmark") {
            VStack(spacing: 0) {
                SettingsRowContainer {
                    VStack(alignment: .leading, spacing: 2) {
                        Text("Automatically kill processes after a timeout")
                            .fontWeight(.medium)
                        Text("Rules are checked on each port scan cycle")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }

                SettingsDivider()

                if rules.isEmpty {
                    SettingsRowContainer {
                        HStack {
                            Text("No rules configured")
                                .foregroundStyle(.secondary)
                            Spacer()
                            Button("Add Rule") {
                                isAddingRule = true
                            }
                            .controlSize(.small)
                        }
                    }
                } else {
                    ForEach(rules) { rule in
                        ruleRow(rule)
                        if rule.id != rules.last?.id {
                            SettingsDivider()
                        }
                    }

                    SettingsDivider()

                    SettingsRowContainer {
                        HStack {
                            Spacer()
                            Button("Add Rule") {
                                isAddingRule = true
                            }
                            .controlSize(.small)
                        }
                    }
                }
            }
        }
        .sheet(isPresented: $isAddingRule) {
            AutoKillRuleEditor(rule: AutoKillRule(name: "New Rule")) { newRule in
                rules.append(newRule)
            }
        }
        .sheet(item: $editingRule) { rule in
            AutoKillRuleEditor(rule: rule) { updated in
                if let index = rules.firstIndex(where: { $0.id == updated.id }) {
                    rules[index] = updated
                }
            }
        }
    }

    private func ruleRow(_ rule: AutoKillRule) -> some View {
        SettingsRowContainer {
            HStack {
                VStack(alignment: .leading, spacing: 2) {
                    HStack(spacing: 6) {
                        Circle()
                            .fill(rule.isEnabled ? .green : .secondary)
                            .frame(width: 8, height: 8)
                        Text(rule.name.isEmpty ? "Unnamed Rule" : rule.name)
                            .fontWeight(.medium)
                    }
                    HStack(spacing: 8) {
                        if !rule.processPattern.isEmpty {
                            Text("Process: \(rule.processPattern)")
                        }
                        if rule.port > 0 {
                            Text("Port: \(rule.port)")
                        }
                        Text("Timeout: \(rule.timeoutMinutes) min")
                    }
                    .font(.caption)
                    .foregroundStyle(.secondary)
                }

                Spacer()

                HStack(spacing: 8) {
                    Button {
                        editingRule = rule
                    } label: {
                        Image(systemName: "pencil")
                    }
                    .buttonStyle(.plain)

                    Button {
                        rules.removeAll { $0.id == rule.id }
                    } label: {
                        Image(systemName: "trash")
                            .foregroundStyle(.red)
                    }
                    .buttonStyle(.plain)
                }
            }
        }
    }
}

// MARK: - Rule Editor

struct AutoKillRuleEditor: View {
    @Environment(\.dismiss) private var dismiss
    @State var rule: AutoKillRule
    let onSave: (AutoKillRule) -> Void

    var body: some View {
        VStack(spacing: 0) {
            // Header
            Text("Edit Auto-Kill Rule")
                .font(.headline)
                .padding(.top, 20)

            Form {
                TextField("Rule Name", text: $rule.name)

                Section("Match Criteria") {
                    TextField("Process Pattern (e.g. node*, python*)", text: $rule.processPattern)
                    TextField("Port (0 = any)", value: $rule.port, format: .number)
                }

                Section("Behavior") {
                    Stepper("Timeout: \(rule.timeoutMinutes) minutes", value: $rule.timeoutMinutes, in: 1...1440)
                    Toggle("Notify before killing", isOn: $rule.notifyBeforeKill)
                    Toggle("Enabled", isOn: $rule.isEnabled)
                }
            }
            .formStyle(.grouped)
            .frame(minHeight: 280)

            // Actions
            HStack {
                Button("Cancel") {
                    dismiss()
                }
                .keyboardShortcut(.cancelAction)

                Spacer()

                Button("Save") {
                    onSave(rule)
                    dismiss()
                }
                .keyboardShortcut(.defaultAction)
                .disabled(rule.processPattern.isEmpty && rule.port == 0)
            }
            .padding(20)
        }
        .frame(width: 420)
    }
}
```

## File: `platforms/macos/Sources/Views/Settings/CloudflaredSettingsSection.swift`
```
/// CloudflaredSettingsSection - Cloudflare tunnel preferences
///
/// Displays cloudflared settings including:
/// - Transport protocol selection (HTTP/2 or QUIC)

import SwiftUI
import Defaults

struct CloudflaredSettingsSection: View {
    @Default(.cloudflaredProtocol) private var protocolSelection
    @Default(.customCloudflaredPath) private var customPath
    @State private var pathInput = ""

    private let service = CloudflaredService()

    private var effectivePath: String? {
        if let custom = customPath, !custom.isEmpty, FileManager.default.fileExists(atPath: custom) {
            return custom
        }
        return service.autoDetectedPath
    }

    var body: some View {
        SettingsGroup("Cloudflare Tunnels", icon: "cloud.fill") {
            VStack(spacing: 0) {
                SettingsRowContainer {
                    HStack {
                        VStack(alignment: .leading, spacing: 2) {
                            Text("Tunnel protocol")
                                .fontWeight(.medium)
                            Text("Choose how cloudflared connects to Cloudflare (applies to new tunnels)")
                                .font(.caption)
                                .foregroundStyle(.secondary)
                        }

                        Spacer()

                        Picker("", selection: $protocolSelection) {
                            ForEach(CloudflaredProtocol.allCases, id: \.self) { option in
                                Text(option.displayName).tag(option)
                            }
                        }
                        .labelsHidden()
                        .pickerStyle(.segmented)
                        .frame(width: 160)
                    }
                }

                SettingsDivider()

                SettingsRowContainer {
                    VStack(alignment: .leading, spacing: 10) {
                        HStack {
                            Text("cloudflared path")
                                .fontWeight(.medium)

                            Spacer()

                            if effectivePath != nil {
                                HStack(spacing: 4) {
                                    Image(systemName: "checkmark.circle.fill")
                                        .foregroundStyle(.green)
                                    Text("Installed")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                }
                            } else {
                                HStack(spacing: 4) {
                                    Image(systemName: "xmark.circle.fill")
                                        .foregroundStyle(.red)
                                    Text("Not found")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                }
                            }
                        }

                        HStack(spacing: 8) {
                            TextField("Custom path (leave empty for auto)", text: $pathInput)
                                .textFieldStyle(.roundedBorder)
                                .font(.system(.caption, design: .monospaced))
                                .onAppear {
                                    pathInput = customPath ?? ""
                                }
                                .onChange(of: pathInput) { _, newValue in
                                    if newValue.isEmpty {
                                        Defaults[.customCloudflaredPath] = nil
                                    } else {
                                        Defaults[.customCloudflaredPath] = newValue
                                    }
                                }

                            if !pathInput.isEmpty {
                                Button("Clear") {
                                    pathInput = ""
                                    Defaults[.customCloudflaredPath] = nil
                                }
                                .buttonStyle(.bordered)
                                .controlSize(.small)
                            }
                        }

                        if let path = effectivePath {
                            HStack(spacing: 4) {
                                Text("Using:")
                                    .font(.caption)
                                    .foregroundStyle(.tertiary)
                                Text(path)
                                    .font(.system(.caption, design: .monospaced))
                                    .foregroundStyle(.secondary)
                                Text(service.isUsingCustomPath ? "(custom)" : "(auto)")
                                    .font(.caption2)
                                    .foregroundStyle(service.isUsingCustomPath ? Color.orange : Color.gray)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Settings/GeneralSettingsSection.swift`
```
/// GeneralSettingsSection - General app preferences
///
/// Displays general settings including:
/// - Launch at login toggle
///
/// - Note: Uses LaunchAtLogin package for login item management.

import SwiftUI
import LaunchAtLogin
import Defaults

struct GeneralSettingsSection: View {
    @Default(.hideSystemProcesses) private var hideSystemProcesses
    @Default(.skipKillConfirmation) private var skipKillConfirmation

    var body: some View {
        SettingsGroup("General", icon: "gearshape.fill") {
            SettingsRowContainer {
                LaunchAtLogin.Toggle {
                    VStack(alignment: .leading, spacing: 2) {
                        Text("Launch at Login")
                            .fontWeight(.medium)
                        Text("Start PortKiller when you log in")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }
                .toggleStyle(.switch)
            }

			SettingsToggleRow(
				title: "Hide System processes",
				subtitle: "Hide macOS processes from the process list",
				isOn: $hideSystemProcesses
			)

            SettingsDivider()

            SettingsToggleRow(
                title: "Skip kill confirmation",
                subtitle: "Kill processes immediately without confirmation prompt",
                isOn: $skipKillConfirmation
            )
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Settings/NotificationsSettingsSection.swift`
```
import SwiftUI
import Defaults

struct NotificationsSettingsSection: View {
    @Default(.notifyProcessTypes) private var enabledTypes

    var body: some View {
        SettingsGroup("Port Notifications", icon: "bell.fill") {
            VStack(spacing: 0) {
                SettingsRowContainer {
                    VStack(alignment: .leading, spacing: 2) {
                        Text("Notify on new ports by process type")
                            .fontWeight(.medium)
                        Text("Get notified when a port opens for selected process types")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }

                ForEach(ProcessType.allCases) { type in
                    SettingsDivider()
                    processTypeToggle(type)
                }
            }
        }
    }

    private func processTypeToggle(_ type: ProcessType) -> some View {
        SettingsRowContainer {
            Toggle(isOn: Binding(
                get: { enabledTypes.contains(type.rawValue) },
                set: { enabled in
                    if enabled {
                        Defaults[.notifyProcessTypes].insert(type.rawValue)
                    } else {
                        Defaults[.notifyProcessTypes].remove(type.rawValue)
                    }
                }
            )) {
                HStack(spacing: 8) {
                    Image(systemName: type.icon)
                        .foregroundStyle(type.color)
                        .frame(width: 20)
                    Text(type.rawValue)
                }
            }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Settings/PermissionsSection.swift`
```
/// PermissionsSection - Permission management UI
///
/// Manages accessibility and notification permissions:
/// - Shows current permission status with visual indicators
/// - Provides buttons to grant or configure permissions
/// - Displays helpful status messages
///
/// - Note: Accessibility is required for global keyboard shortcuts.
/// - Important: Notification permission only works in .app bundles.

import SwiftUI
import ApplicationServices
@preconcurrency import UserNotifications

struct PermissionsSection: View {
    @Binding var hasAccessibility: Bool
    @Binding var notificationStatus: UNAuthorizationStatus
    let onRequestNotification: () -> Void
    let onOpenNotificationSettings: () -> Void

    var body: some View {
        SettingsGroup("Permissions", icon: "lock.shield.fill") {
            VStack(spacing: 0) {
                // Accessibility Permission
                SettingsRowContainer {
                    HStack(spacing: 12) {
                        Image(systemName: hasAccessibility ? "checkmark.circle.fill" : "exclamationmark.circle.fill")
                            .font(.title2)
                            .foregroundStyle(hasAccessibility ? .green : .orange)

                        VStack(alignment: .leading, spacing: 2) {
                            Text("Accessibility")
                                .fontWeight(.medium)
                            Text(hasAccessibility ? "Permission granted" : "Required for global shortcuts")
                                .font(.caption)
                                .foregroundStyle(.secondary)
                        }

                        Spacer()

                        if hasAccessibility {
                            Text("Granted")
                                .font(.caption)
                                .foregroundStyle(.green)
                                .padding(.horizontal, 8)
                                .padding(.vertical, 4)
                                .background(.green.opacity(0.1))
                                .clipShape(Capsule())
                        } else {
                            Button("Grant Access") {
                                promptAccessibility()
                            }
                            .buttonStyle(.borderedProminent)
                            .controlSize(.small)
                        }
                    }
                }

                SettingsDivider()

                // Notification Permission
                SettingsRowContainer {
                    HStack(spacing: 12) {
                        Image(systemName: notificationStatusIcon)
                            .font(.title2)
                            .foregroundStyle(notificationStatusColor)

                        VStack(alignment: .leading, spacing: 2) {
                            Text("Notifications")
                                .fontWeight(.medium)
                            Text(notificationStatusText)
                                .font(.caption)
                                .foregroundStyle(.secondary)
                        }

                        Spacer()

                        if notificationStatus == .authorized {
                            Text("Enabled")
                                .font(.caption)
                                .foregroundStyle(.green)
                                .padding(.horizontal, 8)
                                .padding(.vertical, 4)
                                .background(.green.opacity(0.1))
                                .clipShape(Capsule())
                        } else if notificationStatus == .notDetermined {
                            Button("Enable") {
                                onRequestNotification()
                            }
                            .buttonStyle(.borderedProminent)
                            .controlSize(.small)
                        } else {
                            Button("Open Settings") {
                                onOpenNotificationSettings()
                            }
                            .controlSize(.small)
                        }
                    }
                }
            }
        }
    }

    // MARK: - Notification Status Helpers

    /// Returns appropriate icon for notification status
    private var notificationStatusIcon: String {
        switch notificationStatus {
        case .authorized: return "checkmark.circle.fill"
        case .denied: return "xmark.circle.fill"
        case .notDetermined: return "questionmark.circle.fill"
        case .provisional, .ephemeral: return "checkmark.circle.fill"
        @unknown default: return "questionmark.circle.fill"
        }
    }

    /// Returns color for notification status indicator
    private var notificationStatusColor: Color {
        switch notificationStatus {
        case .authorized, .provisional, .ephemeral: return .green
        case .denied: return .red
        case .notDetermined: return .orange
        @unknown default: return .secondary
        }
    }

    /// Returns descriptive text for notification status
    private var notificationStatusText: String {
        switch notificationStatus {
        case .authorized: return "Alerts enabled for port watch"
        case .denied: return "Notifications disabled in System Settings"
        case .notDetermined: return "Required for port watch alerts"
        case .provisional: return "Provisional notifications enabled"
        case .ephemeral: return "Temporary notifications enabled"
        @unknown default: return "Unknown status"
        }
    }
}

// MARK: - Accessibility Prompt

/// Prompts user to grant accessibility permission
private func promptAccessibility() {
    let options = ["AXTrustedCheckOptionPrompt": true] as CFDictionary
    AXIsProcessTrustedWithOptions(options)
}
```

## File: `platforms/macos/Sources/Views/Settings/PortForwardingSettingsSection.swift`
```
/// PortForwardingSettingsSection - Port forwarding dependencies settings
///
/// Displays port forwarding settings including:
/// - kubectl path and custom path input
/// - socat path and custom path input
/// - Auto-start toggle

import SwiftUI
import Defaults

struct PortForwardingSettingsSection: View {
    @AppStorage("portForwardAutoStart") private var autoStart = false

    var body: some View {
        SettingsGroup("Port Forwarding", icon: "point.3.connected.trianglepath.dotted") {
            VStack(spacing: 0) {
                // Auto-start toggle
                SettingsToggleRow(
                    title: "Auto-start connections",
                    subtitle: "Start all connections when app launches",
                    isOn: $autoStart
                )

                SettingsDivider()

                // kubectl dependency
                DependencySettingsRow(
                    name: "kubectl",
                    dependency: DependencyChecker.shared.kubectl,
                    autoPath: DependencyChecker.shared.kubectl.installedPath,
                    customPathKey: .customKubectlPath
                )

                SettingsDivider()

                // socat dependency
                DependencySettingsRow(
                    name: "socat",
                    dependency: DependencyChecker.shared.socat,
                    autoPath: DependencyChecker.shared.socat.installedPath,
                    customPathKey: .customSocatPath
                )
            }
        }
    }
}

// MARK: - Dependency Settings Row

private struct DependencySettingsRow: View {
    let name: String
    let dependency: PortForwardDependency
    let autoPath: String?
    let customPathKey: Defaults.Key<String?>

    @Default private var customPath: String?
    @State private var isInstalling = false
    @State private var pathInput = ""

    init(name: String, dependency: PortForwardDependency, autoPath: String?, customPathKey: Defaults.Key<String?>) {
        self.name = name
        self.dependency = dependency
        self.autoPath = autoPath
        self.customPathKey = customPathKey
        self._customPath = Default(customPathKey)
    }

    private var effectivePath: String? {
        if let custom = customPath, !custom.isEmpty, FileManager.default.fileExists(atPath: custom) {
            return custom
        }
        return autoPath
    }

    private var isUsingCustom: Bool {
        if let custom = customPath, !custom.isEmpty, FileManager.default.fileExists(atPath: custom) {
            return true
        }
        return false
    }

    var body: some View {
        SettingsRowContainer {
            VStack(alignment: .leading, spacing: 10) {
                // Title row
                HStack {
                    HStack(spacing: 6) {
                        Text(name)
                            .fontWeight(.medium)

                        if !dependency.isRequired {
                            Text("(optional)")
                                .font(.caption)
                                .foregroundStyle(.tertiary)
                        }
                    }

                    Spacer()

                    if effectivePath != nil {
                        HStack(spacing: 4) {
                            Image(systemName: "checkmark.circle.fill")
                                .foregroundStyle(.green)
                            Text("Installed")
                                .font(.caption)
                                .foregroundStyle(.secondary)
                        }
                    } else {
                        HStack(spacing: 8) {
                            Image(systemName: "xmark.circle.fill")
                                .foregroundStyle(.red)
                            Text("Not found")
                                .font(.caption)
                                .foregroundStyle(.secondary)

                            if isInstalling {
                                ProgressView()
                                    .scaleEffect(0.7)
                            } else {
                                Button("Install") {
                                    install()
                                }
                                .buttonStyle(.bordered)
                                .controlSize(.small)
                            }
                        }
                    }
                }

                // Path input
                HStack(spacing: 8) {
                    TextField("Custom path (leave empty for auto)", text: $pathInput)
                        .textFieldStyle(.roundedBorder)
                        .font(.system(.caption, design: .monospaced))
                        .onAppear {
                            pathInput = customPath ?? ""
                        }
                        .onChange(of: pathInput) { _, newValue in
                            if newValue.isEmpty {
                                Defaults[customPathKey] = nil
                            } else {
                                Defaults[customPathKey] = newValue
                            }
                        }

                    if !pathInput.isEmpty {
                        Button("Clear") {
                            pathInput = ""
                            Defaults[customPathKey] = nil
                        }
                        .buttonStyle(.bordered)
                        .controlSize(.small)
                    }
                }

                // Current path info
                if let path = effectivePath {
                    HStack(spacing: 4) {
                        Text("Using:")
                            .font(.caption)
                            .foregroundStyle(.tertiary)
                        Text(path)
                            .font(.system(.caption, design: .monospaced))
                            .foregroundStyle(.secondary)
                        Text(isUsingCustom ? "(custom)" : "(auto)")
                            .font(.caption2)
                            .foregroundStyle(isUsingCustom ? Color.orange : Color.gray)
                    }
                } else if let auto = autoPath {
                    HStack(spacing: 4) {
                        Text("Auto-detected:")
                            .font(.caption)
                            .foregroundStyle(.tertiary)
                        Text(auto)
                            .font(.system(.caption, design: .monospaced))
                            .foregroundStyle(.secondary)
                    }
                }
            }
        }
    }

    private func install() {
        isInstalling = true
        Task {
            _ = await DependencyChecker.shared.checkAndInstallMissing()
            await MainActor.run { isInstalling = false }
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Settings/SettingsComponents.swift`
```
/// SettingsComponents - Reusable UI components for settings
///
/// Provides consistent styling for settings sections:
/// - SettingsGroup: Container with icon and title
/// - SettingsRowContainer: Padding wrapper for rows
/// - SettingsToggleRow: Toggle with title and subtitle
/// - SettingsButtonRow: Button with icon and description
/// - SettingsLinkRow: External link with arrow indicator
/// - SettingsDivider: Indented divider line
///
/// - Note: All components follow macOS Big Sur+ design patterns.

import SwiftUI

// MARK: - Settings Group

/// Container for a section of related settings with icon and title
struct SettingsGroup<Content: View>: View {
    let title: String
    let icon: String
    let content: Content

    init(_ title: String, icon: String, @ViewBuilder content: () -> Content) {
        self.title = title
        self.icon = icon
        self.content = content()
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HStack(spacing: 8) {
                Image(systemName: icon)
                    .font(.body)
                    .foregroundStyle(.secondary)
                Text(title)
                    .font(.headline)
            }

            content
                .background(Color(nsColor: .controlBackgroundColor))
                .clipShape(RoundedRectangle(cornerRadius: 10, style: .continuous))
        }
    }
}

// MARK: - Row Container

/// Wrapper that adds consistent padding to settings rows
struct SettingsRowContainer<Content: View>: View {
    let content: Content

    init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }

    var body: some View {
        content
            .frame(maxWidth: .infinity, alignment: .leading)
            .padding(.horizontal, 14)
            .padding(.vertical, 12)
    }
}

// MARK: - Toggle Row

/// Toggle row with title and subtitle text
struct SettingsToggleRow: View {
    let title: String
    let subtitle: String
    @Binding var isOn: Bool

    var body: some View {
        SettingsRowContainer {
            Toggle(isOn: $isOn) {
                VStack(alignment: .leading, spacing: 2) {
                    Text(title)
                        .fontWeight(.medium)
                    Text(subtitle)
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
            }
            .toggleStyle(.switch)
        }
    }
}

// MARK: - Button Row

/// Button row with icon, title, subtitle, and action
struct SettingsButtonRow: View {
    let title: String
    let subtitle: String
    let icon: String
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            SettingsRowContainer {
                HStack(spacing: 12) {
                    Image(systemName: icon)
                        .font(.title3)
                        .foregroundStyle(.secondary)
                        .frame(width: 24)

                    VStack(alignment: .leading, spacing: 2) {
                        Text(title)
                            .fontWeight(.medium)
                        Text(subtitle)
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }

                    Spacer()

                    Image(systemName: "arrow.up.forward")
                        .font(.caption)
                        .foregroundStyle(.tertiary)
                }
            }
        }
        .buttonStyle(.plain)
    }
}

// MARK: - Link Row

/// External link row with icon, title, subtitle, and arrow indicator
struct SettingsLinkRow: View {
    let title: String
    let subtitle: String
    let icon: String
    let url: String

    var body: some View {
        Link(destination: URL(string: url)!) {
            SettingsRowContainer {
                HStack(spacing: 12) {
                    Image(systemName: icon)
                        .font(.title3)
                        .foregroundStyle(.secondary)
                        .frame(width: 24)

                    VStack(alignment: .leading, spacing: 2) {
                        Text(title)
                            .fontWeight(.medium)
                        Text(subtitle)
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }

                    Spacer()

                    Image(systemName: "arrow.up.forward")
                        .font(.caption)
                        .foregroundStyle(.tertiary)
                }
            }
        }
        .buttonStyle(.plain)
    }
}

// MARK: - Divider

/// Indented divider for separating settings rows
struct SettingsDivider: View {
    var body: some View {
        Divider()
            .padding(.leading, 50)
    }
}
```

## File: `platforms/macos/Sources/Views/Settings/SettingsView.swift`
```
/// SettingsView - Main settings interface
///
/// Displays app settings organized into sections:
/// - General preferences (launch at login)
/// - Keyboard shortcuts (global hotkeys)
/// - Permissions (accessibility, notifications)
/// - Software updates (Sparkle integration)
/// - Sponsors configuration
/// - About information
///
/// - Note: Automatically checks permissions every 5 seconds while visible.
/// - Important: Uses `@Bindable var state: AppState` for state management.

import SwiftUI
import ApplicationServices
@preconcurrency import UserNotifications
import Sparkle
import LaunchAtLogin
import Defaults

struct SettingsView: View {
    @Bindable var state: AppState
    var updateManager: UpdateManager
    @Environment(SponsorManager.self) var sponsorManager
    @Environment(\.openWindow) private var openWindow
    @State private var hasAccessibility = AXIsProcessTrusted()
    @State private var notificationStatus: UNAuthorizationStatus = .notDetermined
    @State private var sponsorDisplayInterval = Defaults[.sponsorDisplayInterval]

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 28) {
                // MARK: - General
                GeneralSettingsSection()

                // MARK: - Port Forwarding
                PortForwardingSettingsSection()

                // MARK: - Auto-Kill Rules
                AutoKillSettingsSection()

                // MARK: - Notifications
                NotificationsSettingsSection()

                // MARK: - Cloudflare Tunnels
                CloudflaredSettingsSection()

                // MARK: - Keyboard Shortcuts
                ShortcutsSection()

                // MARK: - Permissions
                PermissionsSection(
                    hasAccessibility: $hasAccessibility,
                    notificationStatus: $notificationStatus,
                    onRequestNotification: requestNotificationPermission,
                    onOpenNotificationSettings: openNotificationSettings
                )

                // MARK: - Updates
                SettingsGroup("Software Update", icon: "arrow.triangle.2.circlepath") {
                    VStack(spacing: 0) {
                        SettingsRowContainer {
                            HStack {
                                VStack(alignment: .leading, spacing: 2) {
                                    Text("PortKiller \(AppInfo.versionString)")
                                        .fontWeight(.medium)
                                    if let lastCheck = updateManager.lastUpdateCheckDate {
                                        Text("Last checked \(lastCheck.formatted(.relative(presentation: .named)))")
                                            .font(.caption)
                                            .foregroundStyle(.secondary)
                                    } else {
                                        Text("Never checked for updates")
                                            .font(.caption)
                                            .foregroundStyle(.secondary)
                                    }
                                }

                                Spacer()

                                Button("Check Now") {
                                    updateManager.checkForUpdates()
                                }
                                .disabled(!updateManager.canCheckForUpdates)
                            }
                        }

                        SettingsDivider()

                        SettingsToggleRow(
                            title: "Check automatically",
                            subtitle: "Look for updates in the background",
                            isOn: Binding(
                                get: { updateManager.automaticallyChecksForUpdates },
                                set: { updateManager.automaticallyChecksForUpdates = $0 }
                            )
                        )

                        SettingsDivider()

                        SettingsToggleRow(
                            title: "Download automatically",
                            subtitle: "Download updates when available",
                            isOn: Binding(
                                get: { updateManager.automaticallyDownloadsUpdates },
                                set: { updateManager.automaticallyDownloadsUpdates = $0 }
                            )
                        )
                    }
                }

                // MARK: - Sponsors
                SettingsGroup("Sponsors", icon: "heart.fill") {
                    VStack(spacing: 0) {
                        SettingsRowContainer {
                            HStack {
                                VStack(alignment: .leading, spacing: 2) {
                                    Text("Show Sponsors Window")
                                        .fontWeight(.medium)
                                    Text("How often to display the sponsors window")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                }

                                Spacer()

                                Picker("", selection: $sponsorDisplayInterval) {
                                    ForEach(SponsorDisplayInterval.allCases, id: \.self) { interval in
                                        Text(interval.localizedName).tag(interval)
                                    }
                                }
                                .frame(width: 130)
                                .onChange(of: sponsorDisplayInterval) { _, newValue in
                                    Defaults[.sponsorDisplayInterval] = newValue
                                }
                            }
                        }

                        SettingsDivider()

                        SettingsRowContainer {
                            HStack {
                                VStack(alignment: .leading, spacing: 2) {
                                    Text("View Sponsors")
                                        .fontWeight(.medium)
                                    Text("See all current supporters")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                }

                                Spacer()

                                Button("Show Window") {
                                    sponsorManager.showSponsorsWindow()
                                    openWindow(id: "sponsors")
                                }
                            }
                        }
                    }
                }

                // MARK: - About
                SettingsGroup("About", icon: "info.circle.fill") {
                    VStack(spacing: 0) {
                        SettingsRowContainer {
                            HStack {
                                VStack(alignment: .leading, spacing: 2) {
                                    Text("Developer")
                                        .fontWeight(.medium)
                                    Text("productdevbook")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                }
                                Spacer()
                            }
                        }

                        SettingsDivider()

                        SettingsLinkRow(title: "GitHub", subtitle: "Star the project", icon: "star.fill", url: AppInfo.githubRepo)
                        SettingsDivider()
                        SettingsLinkRow(title: "Sponsor", subtitle: "Support development", icon: "heart.fill", url: AppInfo.githubSponsors)
                        SettingsDivider()
                        SettingsLinkRow(title: "Report Issue", subtitle: "Found a bug?", icon: "ladybug.fill", url: AppInfo.githubIssues)
                        SettingsDivider()
                        SettingsLinkRow(title: "Twitter/X", subtitle: "@productdevbook", icon: "at", url: AppInfo.twitterURL)
                        SettingsDivider()
                        SettingsButtonRow(
                            title: "Show Welcome Screen",
                            subtitle: "Replay the onboarding wizard",
                            icon: "hand.wave.fill",
                            action: {
                                Defaults[.hasCompletedOnboarding] = false
                            }
                        )
                    }
                }
            }
            .padding(28)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color(nsColor: .windowBackgroundColor))
        .task {
            // Periodically check permissions while view is visible
            // Task automatically cancels when view disappears
            while !Task.isCancelled {
                checkPermissions()
                try? await Task.sleep(for: .seconds(5))
            }
        }
    }

    // MARK: - Permission Management

    /// Checks current permission states
    private func checkPermissions() {
        // Check accessibility
        hasAccessibility = AXIsProcessTrusted()

        // Check notification permission (only works in .app bundle)
        guard Bundle.main.bundleIdentifier != nil,
              Bundle.main.bundlePath.hasSuffix(".app") else {
            // Running from debug build, skip notification check
            notificationStatus = .notDetermined
            return
        }

        Task {
            let settings = await UNUserNotificationCenter.current().notificationSettings()
            await MainActor.run {
                notificationStatus = settings.authorizationStatus
            }
        }
    }

    /// Requests notification permission from user
    private func requestNotificationPermission() {
        guard Bundle.main.bundlePath.hasSuffix(".app") else { return }

        Task {
            do {
                _ = try await UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge])
                await MainActor.run {
                    checkPermissions()
                }
            } catch {
                // Permission denied or error
            }
        }
    }

    /// Opens system notification settings for this app
    private func openNotificationSettings() {
        // Open System Settings > Notifications for this app
        if let bundleId = Bundle.main.bundleIdentifier {
            let url = URL(string: "x-apple.systempreferences:com.apple.Notifications-Settings.extension?id=\(bundleId)")!
            NSWorkspace.shared.open(url)
        }
    }
}
```

## File: `platforms/macos/Sources/Views/Settings/ShortcutsSection.swift`
```
/**
 * ShortcutsSection.swift
 * PortKiller
 *
 * Keyboard shortcuts configuration section for settings.
 * Allows users to customize global keyboard shortcuts.
 */

import SwiftUI
import KeyboardShortcuts
import ApplicationServices

/// Keyboard shortcuts configuration section
///
/// Displays configurable keyboard shortcuts with:
/// - Inline recorder for setting shortcuts
/// - Reset to default button
/// - Accessibility permission warning when needed
struct ShortcutsSection: View {
    @State private var hasAccessibility = AXIsProcessTrusted()

    var body: some View {
        SettingsGroup("Keyboard Shortcuts", icon: "command.square.fill") {
            VStack(spacing: 0) {
                // Toggle Main Window Shortcut
                SettingsRowContainer {
                    HStack(spacing: 12) {
                        VStack(alignment: .leading, spacing: 2) {
                            Text("Toggle Main Window")
                                .fontWeight(.medium)
                            Text("Show or hide the PortKiller window")
                                .font(.caption)
                                .foregroundStyle(.secondary)
                        }

                        Spacer()

                        KeyboardShortcuts.Recorder(for: .toggleMainWindow)
                            .frame(width: 130)

                        Button {
                            KeyboardShortcuts.reset(.toggleMainWindow)
                        } label: {
                            Image(systemName: "arrow.counterclockwise")
                                .font(.caption)
                        }
                        .buttonStyle(.borderless)
                        .help("Reset to default (⌘⇧P)")
                    }
                }

                // Accessibility Permission Warning
                if !hasAccessibility {
                    SettingsDivider()

                    SettingsRowContainer {
                        HStack(spacing: 12) {
                            Image(systemName: "exclamationmark.triangle.fill")
                                .font(.title3)
                                .foregroundStyle(.orange)

                            VStack(alignment: .leading, spacing: 2) {
                                Text("Accessibility Required")
                                    .fontWeight(.medium)
                                Text("Global shortcuts need Accessibility permission")
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                            }

                            Spacer()

                            Button("Grant Access") {
                                promptAccessibility()
                            }
                            .controlSize(.small)
                        }
                    }
                }
            }
        }
        .onAppear {
            hasAccessibility = AXIsProcessTrusted()
        }
    }

    /// Prompts user to grant accessibility permission
    private func promptAccessibility() {
        let options = ["AXTrustedCheckOptionPrompt": true] as CFDictionary
        AXIsProcessTrustedWithOptions(options)
    }
}

#Preview {
    ShortcutsSection()
        .padding()
        .frame(width: 500)
}
```

## File: `platforms/macos/Tests/PortFilterTests.swift`
```
import Testing
@testable import PortKiller

/**
 * Tests for PortFilter matching logic.
 *
 * These tests verify that the PortFilter correctly filters ports
 * based on various criteria including search text, port ranges,
 * process types, favorites, and watched ports.
 */
struct PortFilterTests {

    // MARK: - Test Fixtures

    /// Creates a sample active port for testing
    func createPort(
        port: Int = 3000,
        pid: Int = 12345,
        processName: String = "node",
        address: String = "127.0.0.1",
        user: String = "testuser",
        command: String = "node server.js"
    ) -> PortInfo {
        PortInfo.active(
            port: port,
            pid: pid,
            processName: processName,
            address: address,
            user: user,
            command: command,
            fd: "19u"
        )
    }

    // MARK: - isActive Tests

    @Test("Empty filter is not active")
    func emptyFilterNotActive() {
        let filter = PortFilter()
        #expect(!filter.isActive)
    }

    @Test("Filter with search text is active")
    func searchTextMakesActive() {
        var filter = PortFilter()
        filter.searchText = "node"
        #expect(filter.isActive)
    }

    @Test("Filter with port range is active")
    func portRangeMakesActive() {
        var filter = PortFilter()
        filter.minPort = 3000
        #expect(filter.isActive)

        var filter2 = PortFilter()
        filter2.maxPort = 9000
        #expect(filter2.isActive)
    }

    @Test("Filter with process types is active")
    func processTypesMakesActive() {
        var filter = PortFilter()
        filter.processTypes = [.development]
        #expect(filter.isActive)
    }

    @Test("Filter with favorites flag is active")
    func favoritesFlagMakesActive() {
        var filter = PortFilter()
        filter.showOnlyFavorites = true
        #expect(filter.isActive)
    }

    @Test("Filter with watched flag is active")
    func watchedFlagMakesActive() {
        var filter = PortFilter()
        filter.showOnlyWatched = true
        #expect(filter.isActive)
    }

    // MARK: - Search Text Tests

    @Test("Search matches process name")
    func searchMatchesProcessName() {
        let filter = PortFilter(searchText: "node")
        let port = createPort(processName: "node")
        #expect(filter.matches(port, favorites: [], watched: []))
    }

    @Test("Search matches port number")
    func searchMatchesPortNumber() {
        let filter = PortFilter(searchText: "3000")
        let port = createPort(port: 3000)
        #expect(filter.matches(port, favorites: [], watched: []))
    }

    @Test("Search matches PID")
    func searchMatchesPID() {
        let filter = PortFilter(searchText: "12345")
        let port = createPort(pid: 12345)
        #expect(filter.matches(port, favorites: [], watched: []))
    }

    @Test("Search matches address")
    func searchMatchesAddress() {
        let filter = PortFilter(searchText: "127.0.0.1")
        let port = createPort(address: "127.0.0.1")
        #expect(filter.matches(port, favorites: [], watched: []))
    }

    @Test("Search matches user")
    func searchMatchesUser() {
        let filter = PortFilter(searchText: "testuser")
        let port = createPort(user: "testuser")
        #expect(filter.matches(port, favorites: [], watched: []))
    }

    @Test("Search matches command")
    func searchMatchesCommand() {
        let filter = PortFilter(searchText: "server.js")
        let port = createPort(command: "node server.js")
        #expect(filter.matches(port, favorites: [], watched: []))
    }

    @Test("Search is case insensitive")
    func searchCaseInsensitive() {
        let filter = PortFilter(searchText: "NODE")
        let port = createPort(processName: "node")
        #expect(filter.matches(port, favorites: [], watched: []))
    }

    @Test("Search with no match returns false")
    func searchNoMatch() {
        let filter = PortFilter(searchText: "python")
        let port = createPort(processName: "node")
        #expect(!filter.matches(port, favorites: [], watched: []))
    }

    // MARK: - Port Range Tests

    @Test("Min port filter")
    func minPortFilter() {
        var filter = PortFilter()
        filter.minPort = 5000

        let portBelow = createPort(port: 3000)
        let portEqual = createPort(port: 5000)
        let portAbove = createPort(port: 8000)

        #expect(!filter.matches(portBelow, favorites: [], watched: []))
        #expect(filter.matches(portEqual, favorites: [], watched: []))
        #expect(filter.matches(portAbove, favorites: [], watched: []))
    }

    @Test("Max port filter")
    func maxPortFilter() {
        var filter = PortFilter()
        filter.maxPort = 5000

        let portBelow = createPort(port: 3000)
        let portEqual = createPort(port: 5000)
        let portAbove = createPort(port: 8000)

        #expect(filter.matches(portBelow, favorites: [], watched: []))
        #expect(filter.matches(portEqual, favorites: [], watched: []))
        #expect(!filter.matches(portAbove, favorites: [], watched: []))
    }

    @Test("Port range filter")
    func portRangeFilter() {
        var filter = PortFilter()
        filter.minPort = 3000
        filter.maxPort = 5000

        let portBelow = createPort(port: 2000)
        let portInRange = createPort(port: 4000)
        let portAbove = createPort(port: 6000)

        #expect(!filter.matches(portBelow, favorites: [], watched: []))
        #expect(filter.matches(portInRange, favorites: [], watched: []))
        #expect(!filter.matches(portAbove, favorites: [], watched: []))
    }

    // MARK: - Process Type Tests

    @Test("Process type filter")
    func processTypeFilter() {
        var filter = PortFilter()
        filter.processTypes = [.development]

        let nodePort = createPort(processName: "node") // Development
        let nginxPort = createPort(processName: "nginx") // Web server

        #expect(filter.matches(nodePort, favorites: [], watched: []))
        #expect(!filter.matches(nginxPort, favorites: [], watched: []))
    }

    @Test("Multiple process types filter")
    func multipleProcessTypesFilter() {
        var filter = PortFilter()
        filter.processTypes = [.development, .webServer]

        let nodePort = createPort(processName: "node") // Development
        let nginxPort = createPort(processName: "nginx") // Web server
        let postgresPort = createPort(processName: "postgres") // Database

        #expect(filter.matches(nodePort, favorites: [], watched: []))
        #expect(filter.matches(nginxPort, favorites: [], watched: []))
        #expect(!filter.matches(postgresPort, favorites: [], watched: []))
    }

    // MARK: - Favorites Filter Tests

    @Test("Show only favorites filter")
    func showOnlyFavoritesFilter() {
        var filter = PortFilter()
        filter.showOnlyFavorites = true

        let port = createPort(port: 3000)
        let favorites: Set<Int> = [3000, 8080]

        #expect(filter.matches(port, favorites: favorites, watched: []))

        let nonFavoritePort = createPort(port: 5000)
        #expect(!filter.matches(nonFavoritePort, favorites: favorites, watched: []))
    }

    // MARK: - Watched Filter Tests

    @Test("Show only watched filter")
    func showOnlyWatchedFilter() {
        var filter = PortFilter()
        filter.showOnlyWatched = true

        let port = createPort(port: 3000)
        let watched = [WatchedPort(port: 3000), WatchedPort(port: 8080)]

        #expect(filter.matches(port, favorites: [], watched: watched))

        let nonWatchedPort = createPort(port: 5000)
        #expect(!filter.matches(nonWatchedPort, favorites: [], watched: watched))
    }

    // MARK: - Combined Filter Tests

    @Test("Multiple filters combine with AND logic")
    func combinedFilters() {
        var filter = PortFilter()
        filter.searchText = "node"
        filter.minPort = 3000
        filter.maxPort = 5000

        // Matches all criteria
        let matchingPort = createPort(port: 3000, processName: "node")
        #expect(filter.matches(matchingPort, favorites: [], watched: []))

        // Fails search (command also shouldn't contain "node")
        let failsSearch = createPort(port: 3000, processName: "python", command: "python app.py")
        #expect(!filter.matches(failsSearch, favorites: [], watched: []))

        // Fails range
        let failsRange = createPort(port: 8000, processName: "node")
        #expect(!filter.matches(failsRange, favorites: [], watched: []))
    }

    // MARK: - Reset Tests

    @Test("Reset clears all filters")
    func resetClearsFilters() {
        var filter = PortFilter()
        filter.searchText = "node"
        filter.minPort = 3000
        filter.maxPort = 5000
        filter.processTypes = [.development]
        filter.showOnlyFavorites = true
        filter.showOnlyWatched = true

        #expect(filter.isActive)

        filter.reset()

        #expect(!filter.isActive)
        #expect(filter.searchText.isEmpty)
        #expect(filter.minPort == nil)
        #expect(filter.maxPort == nil)
        #expect(filter.processTypes == Set(ProcessType.allCases))
        #expect(!filter.showOnlyFavorites)
        #expect(!filter.showOnlyWatched)
    }

    // MARK: - Edge Cases

    @Test("Empty search matches everything")
    func emptySearchMatchesAll() {
        let filter = PortFilter(searchText: "")
        let port = createPort()
        #expect(filter.matches(port, favorites: [], watched: []))
    }

    @Test("Partial matches work")
    func partialMatches() {
        let filter = PortFilter(searchText: "serv")
        let port = createPort(command: "node server.js")
        #expect(filter.matches(port, favorites: [], watched: []))
    }
}
```

## File: `platforms/macos/Tests/ProcessTypeTests.swift`
```
import Testing
@testable import PortKiller

/**
 * Tests for ProcessType.detect() functionality.
 *
 * These tests verify that process names are correctly categorized
 * into their appropriate ProcessType categories.
 */
struct ProcessTypeTests {

    // MARK: - Web Server Tests

    @Test("Detects nginx as web server")
    func detectNginx() {
        #expect(ProcessType.detect(from: "nginx") == .webServer)
    }

    @Test("Detects apache as web server")
    func detectApache() {
        #expect(ProcessType.detect(from: "apache2") == .webServer)
    }

    @Test("Detects httpd as web server")
    func detectHttpd() {
        #expect(ProcessType.detect(from: "httpd") == .webServer)
    }

    @Test("Detects caddy as web server")
    func detectCaddy() {
        #expect(ProcessType.detect(from: "caddy") == .webServer)
    }

    @Test("Detects traefik as web server")
    func detectTraefik() {
        #expect(ProcessType.detect(from: "traefik") == .webServer)
    }

    // MARK: - Database Tests

    @Test("Detects postgres as database")
    func detectPostgres() {
        #expect(ProcessType.detect(from: "postgres") == .database)
    }

    @Test("Detects mysql as database")
    func detectMySQL() {
        #expect(ProcessType.detect(from: "mysqld") == .database)
    }

    @Test("Detects mariadb as database")
    func detectMariaDB() {
        #expect(ProcessType.detect(from: "mariadbd") == .database)
    }

    @Test("Detects redis as database")
    func detectRedis() {
        #expect(ProcessType.detect(from: "redis-server") == .database)
    }

    @Test("Detects mongodb as database")
    func detectMongoDB() {
        #expect(ProcessType.detect(from: "mongod") == .database)
    }

    @Test("Detects cockroachdb as database")
    func detectCockroachDB() {
        #expect(ProcessType.detect(from: "cockroach") == .database)
    }

    // MARK: - Development Tests

    @Test("Detects node as development")
    func detectNode() {
        #expect(ProcessType.detect(from: "node") == .development)
    }

    @Test("Detects npm as development")
    func detectNpm() {
        #expect(ProcessType.detect(from: "npm") == .development)
    }

    @Test("Detects python as development")
    func detectPython() {
        #expect(ProcessType.detect(from: "python3") == .development)
    }

    @Test("Detects ruby as development")
    func detectRuby() {
        #expect(ProcessType.detect(from: "ruby") == .development)
    }

    @Test("Detects java as development")
    func detectJava() {
        #expect(ProcessType.detect(from: "java") == .development)
    }

    @Test("Detects go as development")
    func detectGo() {
        #expect(ProcessType.detect(from: "go") == .development)
    }

    @Test("Detects vite as development")
    func detectVite() {
        #expect(ProcessType.detect(from: "vite") == .development)
    }

    @Test("Detects webpack as development")
    func detectWebpack() {
        #expect(ProcessType.detect(from: "webpack-dev-server") == .development)
    }

    @Test("Detects next as development")
    func detectNext() {
        #expect(ProcessType.detect(from: "next-server") == .development)
    }

    // MARK: - System Tests

    @Test("Detects launchd as system")
    func detectLaunchd() {
        #expect(ProcessType.detect(from: "launchd") == .system)
    }

    @Test("Detects rapportd as system")
    func detectRapportd() {
        #expect(ProcessType.detect(from: "rapportd") == .system)
    }

    @Test("Detects sharingd as system")
    func detectSharingd() {
        #expect(ProcessType.detect(from: "sharingd") == .system)
    }

    @Test("Detects controlcenter as system")
    func detectControlCenter() {
        #expect(ProcessType.detect(from: "ControlCenter") == .system)
    }

    // MARK: - Case Insensitivity Tests

    @Test("Process detection is case insensitive")
    func detectCaseInsensitive() {
        #expect(ProcessType.detect(from: "NODE") == .development)
        #expect(ProcessType.detect(from: "Node") == .development)
        #expect(ProcessType.detect(from: "NGINX") == .webServer)
        #expect(ProcessType.detect(from: "Nginx") == .webServer)
    }

    // MARK: - Substring Matching Tests

    @Test("Detects process names containing keywords")
    func detectSubstring() {
        #expect(ProcessType.detect(from: "com.docker.backend") == .other)
        #expect(ProcessType.detect(from: "node_exporter") == .development)
        #expect(ProcessType.detect(from: "postgresql-12") == .database)
    }

    // MARK: - Other/Default Tests

    @Test("Unknown processes default to other")
    func detectUnknown() {
        #expect(ProcessType.detect(from: "unknown_process") == .other)
        #expect(ProcessType.detect(from: "custom-app") == .other)
        #expect(ProcessType.detect(from: "foobar") == .other)
    }

    @Test("Empty process name defaults to other")
    func detectEmpty() {
        #expect(ProcessType.detect(from: "") == .other)
    }

    // MARK: - Real World Examples

    @Test("Detects real world process names")
    func detectRealWorld() {
        // Development servers
        #expect(ProcessType.detect(from: "/usr/local/bin/node") == .development)
        #expect(ProcessType.detect(from: "/opt/homebrew/bin/python3.11") == .development)

        // Databases
        #expect(ProcessType.detect(from: "/usr/lib/postgresql/14/bin/postgres") == .database)
        #expect(ProcessType.detect(from: "/usr/local/mysql/bin/mysqld") == .database)

        // Web servers
        #expect(ProcessType.detect(from: "/usr/sbin/nginx") == .webServer)
        #expect(ProcessType.detect(from: "/usr/local/apache2/bin/httpd") == .webServer)
    }
}
```

## File: `platforms/windows/PortKiller.sln`
```

Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 17
VisualStudioVersion = 17.8.0.0
MinimumVisualStudioVersion = 10.0.40219.1
Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "PortKiller", "PortKiller\PortKiller.csproj", "{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|x64 = Debug|x64
		Debug|ARM64 = Debug|ARM64
		Release|x64 = Release|x64
		Release|ARM64 = Release|ARM64
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}.Debug|x64.ActiveCfg = Debug|x64
		{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}.Debug|x64.Build.0 = Debug|x64
		{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}.Debug|ARM64.ActiveCfg = Debug|ARM64
		{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}.Debug|ARM64.Build.0 = Debug|ARM64
		{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}.Release|x64.ActiveCfg = Release|x64
		{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}.Release|x64.Build.0 = Release|x64
		{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}.Release|ARM64.ActiveCfg = Release|ARM64
		{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}.Release|ARM64.Build.0 = Release|ARM64
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
EndGlobal
```

## File: `platforms/windows/README.md`
```markdown
# PortKiller for Windows

A native Windows app for finding and killing processes on open ports. Perfect for developers who need to quickly free up ports like 3000, 8080, 5173, etc.

## Features

- 🔍 Auto-discovers listening TCP ports
- ⚡ One-click process termination
- 🔄 Auto-refresh every 5 seconds
- 🔎 Search by port or process name
- ⭐ Favorite ports for quick access
- 👁️ Watch ports and get notifications
- 🎨 Modern Windows 11 design with WinUI 3
- 🔔 System tray integration

## Requirements

- Windows 10 version 1809 (build 17763) or later
- Windows 11 (recommended)
- .NET 9.0 Runtime
- Administrator privileges (required to kill processes)

## Installation

### Option 1: Download from GitHub Releases (Recommended)

1. Go to [GitHub Releases](https://github.com/productdevbook/port-killer/releases)
2. Download the latest `PortKiller-vX.X.X-windows-x64.zip` (or `arm64` for ARM devices)
3. Extract the ZIP to a folder of your choice
4. Run `PortKiller.exe`

> **Note:** Requires [.NET 9 Runtime](https://dotnet.microsoft.com/download/dotnet/9.0) to be installed.

### Option 2: Build from Source

1. Clone the repository:
```bash
git clone https://github.com/productdevbook/port-killer.git
cd port-killer/platforms/windows
```

2. Open in Visual Studio 2022 or later:
```bash
cd PortKiller
dotnet restore
dotnet build
```

3. Run the application:
```bash
dotnet run
```

### Option 3: Visual Studio

1. Open `PortKiller.csproj` in Visual Studio 2022
2. Build the solution (Ctrl+Shift+B)
3. Run (F5) or Debug

### Option 4: Package for Distribution

```bash
dotnet publish -c Release -r win-x64 --self-contained
```

## Usage

### Basic Operations

1. **View All Ports**: The app automatically scans and displays all listening TCP ports
2. **Kill a Process**: Click the kill button next to any port
3. **Search**: Use the search box to filter by port number or process name
4. **Refresh**: Click the refresh button or wait for auto-refresh

### Favorites

- Click on a port to view details
- Click "Add to Favorites" to mark important ports
- Access favorites from the sidebar

### Watched Ports

- Click on a port and select "Watch Port"
- Get notifications when the port starts or stops
- Manage watched ports from the sidebar

### Sidebar Navigation

- **All Ports**: View all listening ports
- **Favorites**: Quick access to favorite ports
- **Watched**: Monitored ports with notifications
- **Process Types**: Filter by Web Server, Database, Development, System, Other
- **Settings**: Configure refresh interval and notifications

### System Tray

- The app runs in the system tray
- Left-click the tray icon to show/hide the window
- Right-click for context menu

## Architecture

### Technology Stack

- **Language**: C# 12 with .NET 8
- **UI Framework**: WinUI 3 (Windows App SDK)
- **Architecture**: MVVM with CommunityToolkit.Mvvm
- **DI Container**: Microsoft.Extensions.DependencyInjection

### Project Structure

```
PortKiller/
├── Models/              # Data models (PortInfo, ProcessType, etc.)
├── Services/            # Business logic services
│   ├── PortScannerService.cs       # Scans ports using Win32 API
│   ├── ProcessKillerService.cs     # Terminates processes
│   ├── SettingsService.cs          # Persistent settings
│   └── NotificationService.cs      # Windows notifications
├── ViewModels/          # MVVM ViewModels
│   └── MainViewModel.cs
├── App.xaml             # Application entry point
└── MainWindow.xaml      # Main UI
```

### How It Works

#### Port Scanning

The app uses the Windows `GetExtendedTcpTable` API to get all TCP connections:

```csharp
// Get all listening TCP connections with process IDs
GetExtendedTcpTable(IntPtr, ref int, bool, AF_INET, TCP_TABLE_OWNER_PID_LISTENER, 0);
```

This is equivalent to macOS `lsof -iTCP -sTCP:LISTEN` but more efficient.

#### Process Information

Uses WMI (Windows Management Instrumentation) to get detailed process info:

```csharp
// Get command line
ManagementObjectSearcher("SELECT CommandLine FROM Win32_Process WHERE ProcessId = {pid}")

// Get process owner
OpenProcessToken() + WindowsIdentity
```

#### Process Termination

Two-stage approach:
1. Try graceful shutdown with `CloseMainWindow()`
2. Force kill with `Process.Kill(entireProcessTree: true)`

## Development

### Prerequisites

- Visual Studio 2022 17.8 or later
- Windows App SDK 1.5 or later
- .NET 8 SDK

### Build

```bash
dotnet build -c Debug
```

### Test

```bash
dotnet test
```

### Package for Distribution

```bash
dotnet publish -c Release -r win-x64 --self-contained -p:PublishSingleFile=true
```

## Known Limitations

- Requires administrator privileges to kill processes
- Cannot kill system processes (by design)
- IPv6 support is limited (IPv4 only currently)
- Some processes may require force kill

## Troubleshooting

### "Access Denied" when killing process

Run the app as Administrator. Right-click and select "Run as administrator".

### Port scan not showing all ports

Make sure you're running as Administrator. Some ports require elevated privileges to view.

### App doesn't start

1. Check Windows version (Windows 10 1809+ or Windows 11)
2. Install .NET 8 Runtime
3. Install Windows App SDK Runtime

## Comparison with macOS Version

| Feature | macOS | Windows |
|---------|-------|---------|
| Port Scanning | `lsof` | Win32 API |
| Process Killing | `kill -15/-9` | `Process.Kill()` |
| UI Framework | SwiftUI | WinUI 3 |
| System Tray | MenuBarExtra | TaskbarIcon |
| Notifications | UNNotification | AppNotification |
| Settings Storage | UserDefaults | ApplicationData |

## Contributing

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for development guidelines.

## License

MIT License - see [LICENSE](../../LICENSE).

## Credits

Windows port by the PortKiller team. Original macOS version available at [github.com/productdevbook/port-killer](https://github.com/productdevbook/port-killer).
```

## File: `platforms/windows/PortKiller/app.manifest`
```
<?xml version="1.0" encoding="utf-8"?>
<assembly manifestVersion="1.0" xmlns="urn:schemas-microsoft-com:asm.v1">
  <assemblyIdentity version="1.0.0.0" name="PortKiller.app"/>
  
  <compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1">
    <application>
      <!-- Windows 10 and Windows 11 -->
      <supportedOS Id="{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}" />
    </application>
  </compatibility>

  <application xmlns="urn:schemas-microsoft-com:asm.v3">
    <windowsSettings>
      <dpiAware xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">true</dpiAware>
      <dpiAwareness xmlns="http://schemas.microsoft.com/SMI/2016/WindowsSettings">PerMonitorV2</dpiAwareness>
    </windowsSettings>
  </application>

  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
    <security>
      <requestedPrivileges xmlns="urn:schemas-microsoft-com:asm.v3">
        <requestedExecutionLevel level="requireAdministrator" uiAccess="false" />
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>
```

## File: `platforms/windows/PortKiller/App.xaml`
```
<Application x:Class="PortKiller.App"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:local="using:PortKiller"
             StartupUri="MainWindow.xaml">
    <Application.Resources>
        <!-- Built-in converters -->
        <BooleanToVisibilityConverter x:Key="BoolToVisibilityConverter"/>
    </Application.Resources>
</Application>
```

## File: `platforms/windows/PortKiller/App.xaml.cs`
```csharp
using System.Windows;
using Microsoft.Extensions.DependencyInjection;
using PortKiller.Services;
using PortKiller.ViewModels;

namespace PortKiller;

public partial class App : Application
{
    public static IServiceProvider Services { get; private set; } = null!;

    public App()
    {
        // Add global exception handling
        this.DispatcherUnhandledException += (s, e) =>
        {
            System.Diagnostics.Debug.WriteLine($"Unhandled exception: {e.Exception.Message}");
            System.Diagnostics.Debug.WriteLine($"Stack trace: {e.Exception.StackTrace}");
            MessageBox.Show($"An error occurred: {e.Exception.Message}\n\nStack trace:\n{e.Exception.StackTrace}", 
                "Error", MessageBoxButton.OK, MessageBoxImage.Error);
            e.Handled = true;
        };

        // Setup dependency injection
        var services = new ServiceCollection();
        ConfigureServices(services);
        Services = services.BuildServiceProvider();
    }

    private void ConfigureServices(IServiceCollection services)
    {
        // Services
        services.AddSingleton<PortScannerService>();
        services.AddSingleton<ProcessKillerService>();
        services.AddSingleton<SettingsService>();
        services.AddSingleton<NotificationService>();
        services.AddSingleton<TunnelService>();

        // ViewModels
        services.AddSingleton<MainViewModel>(sp => new MainViewModel(
            sp.GetRequiredService<PortScannerService>(),
            sp.GetRequiredService<ProcessKillerService>(),
            sp.GetRequiredService<SettingsService>(),
            NotificationService.Instance,
            System.Windows.Threading.Dispatcher.CurrentDispatcher
        ));
        services.AddSingleton<TunnelViewModel>(sp => new TunnelViewModel(
            sp.GetRequiredService<TunnelService>(),
            NotificationService.Instance,
            sp.GetRequiredService<SettingsService>()
        ));
    }
}
```

## File: `platforms/windows/PortKiller/appsettings.json`
```json
{
  "appSettings": {
    "defaultRefreshInterval": 5,
    "showNotifications": true
  }
}
```

## File: `platforms/windows/PortKiller/CloudflareTunnelsView.xaml`
```
<Window x:Class="PortKiller.CloudflareTunnelsView"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:helpers="clr-namespace:PortKiller.Helpers"
        mc:Ignorable="d"
        Title="Cloudflare Tunnels" 
        Height="600" Width="900"
        WindowStartupLocation="CenterScreen"
        Background="#1A1A1A">

    <Window.Resources>
        <!-- Converters -->
        <BooleanToVisibilityConverter x:Key="BoolToVisibilityConverter"/>
        <helpers:BoolToColorConverter x:Key="BoolToColorConverter"/>
        <helpers:NullToVisibilityConverter x:Key="NullToVisibilityConverter"/>
        <helpers:CountToColorConverter x:Key="CountToColorConverter"/>
        <helpers:InverseBoolToVisibilityConverter x:Key="InverseBoolToVisibilityConverter"/>
        
        <!-- Card Style -->
        <Style x:Key="TunnelCard" TargetType="Border">
            <Setter Property="Background" Value="#2A2A2A"/>
            <Setter Property="BorderBrush" Value="#3A3A3A"/>
            <Setter Property="BorderThickness" Value="1"/>
            <Setter Property="CornerRadius" Value="10"/>
            <Setter Property="Padding" Value="16"/>
            <Setter Property="Margin" Value="0,0,0,12"/>
        </Style>

        <!-- Button Style -->
        <Style x:Key="ModernButton" TargetType="Button">
            <Setter Property="Background" Value="#3A3A3A"/>
            <Setter Property="Foreground" Value="#E0E0E0"/>
            <Setter Property="BorderThickness" Value="0"/>
            <Setter Property="Padding" Value="12,8"/>
            <Setter Property="FontSize" Value="13"/>
            <Setter Property="Cursor" Value="Hand"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="Button">
                        <Border Background="{TemplateBinding Background}" 
                                CornerRadius="6"
                                Padding="{TemplateBinding Padding}">
                            <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
                        </Border>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
            <Style.Triggers>
                <Trigger Property="IsMouseOver" Value="True">
                    <Setter Property="Background" Value="#4A4A4A"/>
                </Trigger>
                <Trigger Property="IsEnabled" Value="False">
                    <Setter Property="Opacity" Value="0.5"/>
                </Trigger>
            </Style.Triggers>
        </Style>

        <!-- Icon Button Style -->
        <Style x:Key="IconButton" TargetType="Button" BasedOn="{StaticResource ModernButton}">
            <Setter Property="Width" Value="36"/>
            <Setter Property="Height" Value="36"/>
            <Setter Property="Padding" Value="6"/>
        </Style>

        <!-- Danger Button Style -->
        <Style x:Key="DangerButton" TargetType="Button" BasedOn="{StaticResource ModernButton}">
            <Setter Property="Background" Value="#e74c3c"/>
            <Style.Triggers>
                <Trigger Property="IsMouseOver" Value="True">
                    <Setter Property="Background" Value="#c0392b"/>
                </Trigger>
            </Style.Triggers>
        </Style>
    </Window.Resources>

    <Grid>
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/> <!-- Header -->
            <RowDefinition Height="*"/>    <!-- Content -->
            <RowDefinition Height="Auto"/> <!-- Status Bar -->
        </Grid.RowDefinitions>

        <!-- Header -->
        <Border Grid.Row="0" Background="#252525" BorderThickness="0,0,0,1" BorderBrush="#353535" Padding="20,16">
            <Grid>
                <StackPanel Orientation="Horizontal" VerticalAlignment="Center">
                    <TextBlock Text="☁" FontSize="24" Margin="0,0,12,0" Foreground="#F4AB3A"/>
                    <TextBlock Text="Cloudflare Tunnels" FontSize="20" FontWeight="SemiBold" Foreground="#E0E0E0" VerticalAlignment="Center"/>
                </StackPanel>

                <StackPanel Orientation="Horizontal" HorizontalAlignment="Right">
                    <StackPanel Orientation="Horizontal" VerticalAlignment="Center" Margin="0,0,12,0">
                        <TextBlock Text="Protocol" FontSize="12" Foreground="#A0A0A0" VerticalAlignment="Center" Margin="0,0,8,0"/>
                        <ComboBox Width="90"
                                  ItemsSource="{Binding ProtocolOptions}"
                                  SelectedValuePath="Value"
                                  SelectedValue="{Binding CloudflaredProtocol, Mode=TwoWay}"
                                  DisplayMemberPath="Label"
                                  Background="#3A3A3A"
                                  Foreground="#E0E0E0"
                                  BorderThickness="0"
                                  Padding="6,2"/>
                    </StackPanel>
                    <Button Content="Stop All" 
                            Click="StopAllButton_Click"
                            Style="{StaticResource DangerButton}"
                            Visibility="{Binding Tunnels.Count, Converter={StaticResource BoolToVisibilityConverter}}"
                            Margin="0,0,8,0"/>
                    <Button Content="Refresh" 
                            Click="RefreshButton_Click"
                            Style="{StaticResource ModernButton}"/>
                </StackPanel>
            </Grid>
        </Border>

        <!-- Content -->
        <Grid Grid.Row="1">
            <!-- Warning Banner if cloudflared not installed -->
            <Border Background="#3d2918" 
                    BorderBrush="#8B4513" 
                    BorderThickness="1" 
                    CornerRadius="8" 
                    Padding="16"
                    Margin="20"
                    VerticalAlignment="Top"
                    Visibility="{Binding IsCloudflaredInstalled, Converter={StaticResource InverseBoolToVisibilityConverter}}">
                <StackPanel>
                    <StackPanel Orientation="Horizontal" Margin="0,0,0,8">
                        <TextBlock Text="⚠" FontSize="20" Margin="0,0,12,0" Foreground="#f39c12"/>
                        <TextBlock Text="cloudflared Not Installed" FontSize="16" FontWeight="Bold" Foreground="#f39c12" VerticalAlignment="Center"/>
                    </StackPanel>
                    <TextBlock TextWrapping="Wrap" Foreground="#E0E0E0" Margin="32,0,0,8">
                        To use Cloudflare Tunnels, you need to install cloudflared:
                    </TextBlock>
                    <TextBlock TextWrapping="Wrap" Foreground="#B0B0B0" Margin="32,0,0,0" FontFamily="Consolas" FontSize="11">
                        • Download from: https://github.com/cloudflare/cloudflared/releases<LineBreak/>
                        • Or use Chocolatey: choco install cloudflared
                    </TextBlock>
                </StackPanel>
            </Border>

            <!-- Tunnel List -->
            <ScrollViewer VerticalScrollBarVisibility="Auto" Padding="20" Margin="0,20,0,0">
                <ItemsControl x:Name="TunnelsListView" ItemsSource="{Binding Tunnels}">
                    <ItemsControl.ItemTemplate>
                        <DataTemplate>
                            <Border Style="{StaticResource TunnelCard}">
                                <Grid>
                                    <Grid.RowDefinitions>
                                        <RowDefinition Height="Auto"/>
                                        <RowDefinition Height="Auto"/>
                                    </Grid.RowDefinitions>

                                    <!-- Main Info Row -->
                                    <Grid Grid.Row="0">
                                        <Grid.ColumnDefinitions>
                                            <ColumnDefinition Width="Auto"/>
                                            <ColumnDefinition Width="*"/>
                                            <ColumnDefinition Width="Auto"/>
                                        </Grid.ColumnDefinitions>

                                        <!-- Status Indicator -->
                                        <StackPanel Grid.Column="0" Margin="0,0,16,0">
                                            <Ellipse Width="12" Height="12" 
                                                     Fill="{Binding StatusColor}"
                                                     VerticalAlignment="Center"
                                                     Margin="0,0,0,4"/>
                                            <TextBlock Text="{Binding StatusText}" 
                                                       FontSize="10" 
                                                       Foreground="#A0A0A0"
                                                       HorizontalAlignment="Center"/>
                                        </StackPanel>

                                        <!-- Port and URL Info -->
                                        <StackPanel Grid.Column="1" VerticalAlignment="Center">
                                            <TextBlock FontSize="18" FontWeight="Bold" Foreground="#E0E0E0" Margin="0,0,0,4">
                                                <Run Text="Port"/>
                                                <Run Text="{Binding Port}" Foreground="#3498db"/>
                                            </TextBlock>
                                            
                                            <TextBlock Text="{Binding DisplayUrl}" 
                                                       FontSize="13" 
                                                       Foreground="{Binding IsActive, Converter={StaticResource BoolToColorConverter}}"
                                                       FontFamily="Consolas"
                                                       Margin="0,2,0,0"/>
                                            
                                            <TextBlock Text="{Binding LastError}" 
                                                       FontSize="11" 
                                                       Foreground="#e74c3c"
                                                       TextWrapping="Wrap"
                                                       Margin="0,4,0,0"
                                                       Visibility="{Binding LastError, Converter={StaticResource NullToVisibilityConverter}}"/>
                                        </StackPanel>

                                        <!-- Actions -->
                                        <StackPanel Grid.Column="2" Orientation="Horizontal" VerticalAlignment="Center">
                                            <!-- Uptime (if active) -->
                                            <Border Background="#3A3A3A" 
                                                    CornerRadius="4" 
                                                    Padding="8,4" 
                                                    Margin="0,0,8,0"
                                                    Visibility="{Binding IsActive, Converter={StaticResource BoolToVisibilityConverter}}">
                                                <StackPanel Orientation="Horizontal">
                                                    <TextBlock Text="⏱" FontSize="12" Margin="0,0,4,0"/>
                                                    <TextBlock Text="{Binding Uptime}" FontSize="12" Foreground="#A0A0A0"/>
                                                </StackPanel>
                                            </Border>

                                            <!-- Loading Spinner (if starting) -->
                                            <Grid Width="36" Height="36" Margin="0,0,4,0"
                                                  Visibility="{Binding IsStarting, Converter={StaticResource BoolToVisibilityConverter}}">
                                                <Ellipse Width="20" Height="20" 
                                                         Stroke="#f39c12" 
                                                         StrokeThickness="2"
                                                         StrokeDashArray="12,6"/>
                                                <Ellipse Width="20" Height="20" 
                                                         Stroke="#f39c12" 
                                                         StrokeThickness="2"
                                                         StrokeDashArray="12,6"
                                                         RenderTransformOrigin="0.5,0.5">
                                                    <Ellipse.RenderTransform>
                                                        <RotateTransform x:Name="SpinnerRotation" Angle="0"/>
                                                    </Ellipse.RenderTransform>
                                                    <Ellipse.Triggers>
                                                        <EventTrigger RoutedEvent="Loaded">
                                                            <BeginStoryboard>
                                                                <Storyboard RepeatBehavior="Forever">
                                                                    <DoubleAnimation Storyboard.TargetName="SpinnerRotation"
                                                                                   Storyboard.TargetProperty="Angle"
                                                                                   From="0" To="360" Duration="0:0:1"/>
                                                                </Storyboard>
                                                            </BeginStoryboard>
                                                        </EventTrigger>
                                                    </Ellipse.Triggers>
                                                </Ellipse>
                                            </Grid>

                                            <!-- Copy Button -->
                                            <Button ToolTip="Copy URL"
                                                    Click="CopyButton_Click"
                                                    Tag="{Binding}"
                                                    Style="{StaticResource IconButton}"
                                                    IsEnabled="{Binding CanCopyUrl}"
                                                    Margin="0,0,4,0">
                                                <TextBlock Text="📋" FontSize="16"/>
                                            </Button>

                                            <!-- Open in Browser Button -->
                                            <Button ToolTip="Open in Browser"
                                                    Click="OpenButton_Click"
                                                    Tag="{Binding}"
                                                    Style="{StaticResource IconButton}"
                                                    IsEnabled="{Binding CanOpenUrl}"
                                                    Margin="0,0,4,0">
                                                <TextBlock Text="🌐" FontSize="16"/>
                                            </Button>

                                            <!-- Stop Button -->
                                            <Button ToolTip="Stop Tunnel"
                                                    Click="StopButton_Click"
                                                    Tag="{Binding}"
                                                    Style="{StaticResource IconButton}"
                                                    Background="#e74c3c">
                                                <TextBlock Text="✕" FontSize="16"/>
                                            </Button>
                                        </StackPanel>
                                    </Grid>
                                </Grid>
                            </Border>
                        </DataTemplate>
                    </ItemsControl.ItemTemplate>
                </ItemsControl>
            </ScrollViewer>

            <!-- Empty State -->
            <StackPanel x:Name="EmptyState" 
                        HorizontalAlignment="Center" 
                        VerticalAlignment="Center"
                        Visibility="Collapsed">
                <TextBlock Text="☁" FontSize="64" HorizontalAlignment="Center" Margin="0,0,0,16" Opacity="0.3" Foreground="#F4AB3A"/>
                <TextBlock Text="No Active Tunnels" FontSize="20" Foreground="#A0A0A0" HorizontalAlignment="Center" FontWeight="SemiBold"/>
                <TextBlock Text="Start a tunnel from the port list to create a public URL" 
                           FontSize="13" 
                           Foreground="#808080" 
                           HorizontalAlignment="Center" 
                           Margin="0,8,0,16"
                           TextAlignment="Center"/>
                <TextBlock TextWrapping="Wrap" 
                           FontSize="12" 
                           Foreground="#606060" 
                           HorizontalAlignment="Center" 
                           TextAlignment="Center"
                           MaxWidth="400">
                    💡 Tip: Cloudflare Tunnels make your localhost ports accessible from anywhere on the internet with automatic HTTPS
                </TextBlock>
            </StackPanel>
        </Grid>

        <!-- Status Bar -->
        <Border Grid.Row="2" Background="#252525" BorderThickness="0,1,0,0" BorderBrush="#353535" Padding="20,12">
            <Grid>
                <StackPanel Orientation="Horizontal">
                    <Ellipse Width="8" Height="8" 
                             Fill="{Binding ActiveTunnelCount, Converter={StaticResource CountToColorConverter}}"
                             VerticalAlignment="Center" 
                             Margin="0,0,8,0"/>
                    <TextBlock FontSize="12" Foreground="#A0A0A0" VerticalAlignment="Center">
                        <Run Text="{Binding ActiveTunnelCount, Mode=OneWay}"/>
                        <Run Text="active tunnel(s)"/>
                    </TextBlock>
                </StackPanel>

                <StackPanel Orientation="Horizontal" HorizontalAlignment="Right" 
                            Visibility="{Binding IsCloudflaredInstalled, Converter={StaticResource BoolToVisibilityConverter}}">
                    <TextBlock Text="✓" FontSize="14" Foreground="#2ecc71" Margin="0,0,6,0" VerticalAlignment="Center"/>
                    <TextBlock Text="cloudflared installed" FontSize="12" Foreground="#A0A0A0" VerticalAlignment="Center"/>
                </StackPanel>
            </Grid>
        </Border>
    </Grid>
</Window>
```

## File: `platforms/windows/PortKiller/CloudflareTunnelsView.xaml.cs`
```csharp
using System.Windows;
using System.Windows.Controls;
using Microsoft.Extensions.DependencyInjection;
using PortKiller.Models;
using PortKiller.ViewModels;

namespace PortKiller;

/// <summary>
/// Cloudflare Tunnels management window
/// </summary>
public partial class CloudflareTunnelsView : Window
{
    private readonly TunnelViewModel _viewModel;
    private StackPanel? _emptyState;

    public CloudflareTunnelsView()
    {
        InitializeComponent();
        
        _viewModel = App.Services.GetRequiredService<TunnelViewModel>();
        DataContext = _viewModel;

        // Get reference to empty state
        _emptyState = this.FindName("EmptyState") as StackPanel;

        // Update empty state visibility
        UpdateEmptyState();
        _viewModel.Tunnels.CollectionChanged += (s, e) => UpdateEmptyState();
    }

    private void UpdateEmptyState()
    {
        if (_emptyState != null)
        {
            _emptyState.Visibility = _viewModel.Tunnels.Count == 0 ? Visibility.Visible : Visibility.Collapsed;
        }
    }

    private async void StopButton_Click(object sender, RoutedEventArgs e)
    {
        if (sender is not FrameworkElement { Tag: CloudflareTunnel tunnel })
            return;

        await _viewModel.StopTunnelAsync(tunnel);
    }

    private async void StopAllButton_Click(object sender, RoutedEventArgs e)
    {
        var dialog = new ConfirmDialog(
            $"Are you sure you want to stop all {_viewModel.Tunnels.Count} tunnel(s)?",
            "All public URLs will be terminated immediately.\n\nThis action cannot be undone.",
            "Stop All Tunnels")
        {
            Owner = this
        };
        
        dialog.ShowDialog();

        if (dialog.Result)
        {
            await _viewModel.StopAllTunnelsAsync();
        }
    }

    private void CopyButton_Click(object sender, RoutedEventArgs e)
    {
        if (sender is not FrameworkElement { Tag: CloudflareTunnel tunnel })
            return;

        if (!string.IsNullOrEmpty(tunnel.TunnelUrl))
        {
            _viewModel.CopyUrlToClipboard(tunnel.TunnelUrl);
        }
    }

    private void OpenButton_Click(object sender, RoutedEventArgs e)
    {
        if (sender is not FrameworkElement { Tag: CloudflareTunnel tunnel })
            return;

        if (!string.IsNullOrEmpty(tunnel.TunnelUrl))
        {
            _viewModel.OpenUrlInBrowser(tunnel.TunnelUrl);
        }
    }

    private void RefreshButton_Click(object sender, RoutedEventArgs e)
    {
        _viewModel.RecheckInstallation();
    }

    protected override void OnClosed(EventArgs e)
    {
        // Clean up: stop all tunnels when window closes
        _ = _viewModel.StopAllTunnelsAsync();
        base.OnClosed(e);
    }

    // Public method to start a tunnel from external source (e.g., main window)
    public async Task StartTunnelForPort(int port)
    {
        await _viewModel.StartTunnelAsync(port);
    }
}
```

## File: `platforms/windows/PortKiller/ConfirmDialog.xaml`
```
<Window x:Class="PortKiller.ConfirmDialog"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="Confirm"
        Width="360" Height="200"
        WindowStyle="None"
        AllowsTransparency="True"
        Background="Transparent"
        ResizeMode="NoResize"
        ShowInTaskbar="False"
        Topmost="True"
        WindowStartupLocation="CenterOwner">

    <Window.Resources>
        <SolidColorBrush x:Key="WindowBackground" Color="#F21E1E1E"/>
        <SolidColorBrush x:Key="BorderBrush" Color="#33FFFFFF"/>
        <SolidColorBrush x:Key="TextPrimary" Color="#FFFFFF"/>
        <SolidColorBrush x:Key="TextSecondary" Color="#B0B0B0"/>
        <SolidColorBrush x:Key="DangerColor" Color="#FF453A"/>
        <SolidColorBrush x:Key="AccentColor" Color="#5B9DD9"/>

        <!-- Button Style -->
        <Style x:Key="DialogButton" TargetType="Button">
            <Setter Property="Height" Value="32"/>
            <Setter Property="FontSize" Value="12"/>
            <Setter Property="FontWeight" Value="SemiBold"/>
            <Setter Property="BorderThickness" Value="0"/>
            <Setter Property="Cursor" Value="Hand"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="Button">
                        <Border Background="{TemplateBinding Background}" 
                                CornerRadius="6"
                                Padding="{TemplateBinding Padding}">
                            <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
                        </Border>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
        </Style>
    </Window.Resources>

    <Border Background="{StaticResource WindowBackground}" 
            CornerRadius="12" 
            BorderBrush="{StaticResource BorderBrush}" 
            BorderThickness="1">
        <Border.Effect>
            <DropShadowEffect Color="#80000000" BlurRadius="30" ShadowDepth="8" Direction="270" Opacity="0.5"/>
        </Border.Effect>

        <Grid Margin="20">
            <Grid.RowDefinitions>
                <RowDefinition Height="Auto"/>
                <RowDefinition Height="*"/>
                <RowDefinition Height="Auto"/>
            </Grid.RowDefinitions>

            <!-- Title -->
            <TextBlock x:Name="TitleText" Grid.Row="0" Text="Confirm Action" 
                       FontSize="16" FontWeight="Bold" 
                       Foreground="{StaticResource TextPrimary}" 
                       Margin="0,0,0,12"/>

            <!-- Message -->
            <StackPanel Grid.Row="1" VerticalAlignment="Center">
                <TextBlock x:Name="MessageText" 
                           Text="Kill process on port 3000?" 
                           FontSize="13" 
                           Foreground="{StaticResource TextPrimary}" 
                           TextWrapping="Wrap"
                           Margin="0,0,0,8"/>
                <TextBlock x:Name="DetailsText" 
                           Text="Process: node&#x0a;PID: 25944" 
                           FontSize="11" 
                           Foreground="{StaticResource TextSecondary}" 
                           TextWrapping="Wrap"/>
            </StackPanel>

            <!-- Buttons -->
            <Grid Grid.Row="2" Margin="0,12,0,0">
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="*"/>
                    <ColumnDefinition Width="12"/>
                    <ColumnDefinition Width="*"/>
                </Grid.ColumnDefinitions>

                <Button Grid.Column="0" 
                        Content="No" 
                        Click="NoButton_Click"
                        Style="{StaticResource DialogButton}"
                        Foreground="{StaticResource TextPrimary}"
                        Background="#30FFFFFF"/>

                <Button Grid.Column="2" 
                        Content="Yes" 
                        Click="YesButton_Click"
                        Style="{StaticResource DialogButton}"
                        Foreground="White"
                        Background="{StaticResource DangerColor}"/>
            </Grid>
        </Grid>
    </Border>
</Window>
```

## File: `platforms/windows/PortKiller/ConfirmDialog.xaml.cs`
```csharp
using System.Windows;

namespace PortKiller;

public partial class ConfirmDialog : Window
{
    public bool Result { get; private set; }

    public ConfirmDialog(string message, string details, string title = "Confirm Action")
    {
        InitializeComponent();
        TitleText.Text = title;
        MessageText.Text = message;
        DetailsText.Text = details;
    }

    private void YesButton_Click(object sender, RoutedEventArgs e)
    {
        Result = true;
        Close();
    }

    private void NoButton_Click(object sender, RoutedEventArgs e)
    {
        Result = false;
        Close();
    }
}
```

## File: `platforms/windows/PortKiller/MainWindow.xaml`
```
<Window x:Class="PortKiller.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:tb="http://www.hardcodet.net/taskbar"
        xmlns:helpers="clr-namespace:PortKiller.Helpers"
        mc:Ignorable="d"
        Title="PortKiller" 
        Height="700" Width="1200"
        WindowStartupLocation="CenterScreen"
        Background="Transparent"
        AllowsTransparency="True"
        WindowStyle="None"
        ResizeMode="CanResize"
        ShowInTaskbar="True"
        Visibility="Visible"
        Loaded="Window_Loaded">

    <Window.Resources>
        <!-- Boolean to Visibility Converter -->
        <BooleanToVisibilityConverter x:Key="BoolToVisibilityConverter"/>
        <helpers:InverseBoolToVisibilityConverter x:Key="InverseBoolToVisibilityConverter"/>

        <!-- Modern Card Style -->
        <Style x:Key="Card" TargetType="Border">
            <Setter Property="Background" Value="#2B2B2B"/>
            <Setter Property="BorderBrush" Value="#1FFFFFFF"/>
            <Setter Property="BorderThickness" Value="1"/>
            <Setter Property="CornerRadius" Value="12"/>
            <Setter Property="Padding" Value="16"/>
            <Setter Property="Margin" Value="0,0,0,12"/>
            <Setter Property="Effect">
                <Setter.Value>
                    <DropShadowEffect Color="Black" BlurRadius="15" ShadowDepth="4" Opacity="0.15"/>
                </Setter.Value>
            </Setter>
            <Style.Triggers>
                <Trigger Property="IsMouseOver" Value="True">
                    <Setter Property="Background" Value="#323232"/>
                    <Setter Property="BorderBrush" Value="#3FFFFFFF"/>
                </Trigger>
            </Style.Triggers>
        </Style>

        <!-- Window Control Button Style -->
        <Style x:Key="WindowControlButton" TargetType="Button">
            <Setter Property="Background" Value="Transparent"/>
            <Setter Property="Foreground" Value="#A0A0A0"/>
            <Setter Property="BorderThickness" Value="0"/>
            <Setter Property="Width" Value="46"/>
            <Setter Property="Height" Value="32"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="Button">
                        <Border Background="{TemplateBinding Background}">
                            <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
                        </Border>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
            <Style.Triggers>
                <Trigger Property="IsMouseOver" Value="True">
                    <Setter Property="Background" Value="#1FFFFFFF"/>
                    <Setter Property="Foreground" Value="#FFFFFF"/>
                </Trigger>
            </Style.Triggers>
        </Style>

        <!-- Close Button Style -->
        <Style x:Key="CloseButtonStyle" TargetType="Button" BasedOn="{StaticResource WindowControlButton}">
            <Style.Triggers>
                <Trigger Property="IsMouseOver" Value="True">
                    <Setter Property="Background" Value="#E81123"/>
                    <Setter Property="Foreground" Value="#FFFFFF"/>
                </Trigger>
            </Style.Triggers>
        </Style>

        <!-- Modern Button Style -->
        <Style x:Key="ModernButton" TargetType="Button">
            <Setter Property="Background" Value="Transparent"/>
            <Setter Property="Foreground" Value="#E0E0E0"/>
            <Setter Property="BorderThickness" Value="0"/>
            <Setter Property="Padding" Value="8,6"/>
            <Setter Property="FontSize" Value="13"/>
            <Setter Property="Cursor" Value="Hand"/>
            <Setter Property="FocusVisualStyle" Value="{x:Null}"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="Button">
                        <Border Background="{TemplateBinding Background}" 
                                CornerRadius="6"
                                Padding="{TemplateBinding Padding}">
                            <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
                        </Border>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
            <Style.Triggers>
                <Trigger Property="IsMouseOver" Value="True">
                    <Setter Property="Background" Value="#20FFFFFF"/>
                </Trigger>
            </Style.Triggers>
        </Style>

        <!-- Dark Sidebar Button Style -->
        <Style x:Key="SidebarButton" TargetType="Button">
            <Setter Property="Background" Value="Transparent"/>
            <Setter Property="Foreground" Value="#909090"/>
            <Setter Property="BorderThickness" Value="0"/>
            <Setter Property="Padding" Value="16,10"/>
            <Setter Property="HorizontalContentAlignment" Value="Left"/>
            <Setter Property="FontSize" Value="13"/>
            <Setter Property="Cursor" Value="Hand"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="Button">
                        <Border Background="{TemplateBinding Background}" 
                                CornerRadius="8"
                                Padding="{TemplateBinding Padding}"
                                Margin="8,2">
                            <ContentPresenter HorizontalAlignment="Left" VerticalAlignment="Center"/>
                        </Border>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
            <Style.Triggers>
                <Trigger Property="IsMouseOver" Value="True">
                    <Setter Property="Background" Value="#15FFFFFF"/>
                    <Setter Property="Foreground" Value="#FFFFFF"/>
                </Trigger>
            </Style.Triggers>
        </Style>
        
        <!-- Outline Button Style -->
        <Style x:Key="OutlineButton" TargetType="Button">
            <Setter Property="Background" Value="Transparent"/>
            <Setter Property="BorderBrush" Value="#30FFFFFF"/>
            <Setter Property="BorderThickness" Value="1"/>
            <Setter Property="Foreground" Value="#E0E0E0"/>
            <Setter Property="Padding" Value="16,10"/>
            <Setter Property="FontSize" Value="13"/>
            <Setter Property="FontWeight" Value="SemiBold"/>
            <Setter Property="Cursor" Value="Hand"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="Button">
                        <Border Background="{TemplateBinding Background}" 
                                BorderBrush="{TemplateBinding BorderBrush}"
                                BorderThickness="{TemplateBinding BorderThickness}"
                                CornerRadius="8"
                                Padding="{TemplateBinding Padding}">
                            <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
                        </Border>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
            <Style.Triggers>
                <Trigger Property="IsMouseOver" Value="True">
                    <Setter Property="Background" Value="#10FFFFFF"/>
                    <Setter Property="BorderBrush" Value="#50FFFFFF"/>
                </Trigger>
            </Style.Triggers>
        </Style>

        <!-- Modern Search TextBox Style -->
        <Style x:Key="ModernTextBox" TargetType="TextBox">
            <Setter Property="Background" Value="#15FFFFFF"/>
            <Setter Property="BorderBrush" Value="Transparent"/>
            <Setter Property="BorderThickness" Value="1"/>
            <Setter Property="Padding" Value="12,8"/>
            <Setter Property="FontSize" Value="13"/>
            <Setter Property="Foreground" Value="#FFFFFF"/>
            <Setter Property="CaretBrush" Value="#FFFFFF"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="TextBox">
                        <Border Background="{TemplateBinding Background}" 
                                BorderBrush="{TemplateBinding BorderBrush}"
                                BorderThickness="{TemplateBinding BorderThickness}"
                                CornerRadius="8">
                            <ScrollViewer x:Name="PART_ContentHost" Padding="{TemplateBinding Padding}"/>
                        </Border>
                        <ControlTemplate.Triggers>
                            <Trigger Property="IsFocused" Value="True">
                                <Setter Property="Background" Value="#20FFFFFF"/>
                                <Setter Property="BorderBrush" Value="#30FFFFFF"/>
                            </Trigger>
                            <Trigger Property="IsMouseOver" Value="True">
                                <Setter Property="Background" Value="#20FFFFFF"/>
                            </Trigger>
                        </ControlTemplate.Triggers>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
        </Style>

        <!-- Invisible ScrollViewer Style (hides scrollbar but keeps scroll functionality) -->
        <Style x:Key="InvisibleScrollViewer" TargetType="ScrollViewer">
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="ScrollViewer">
                        <Grid>
                            <ScrollContentPresenter />
                        </Grid>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
        </Style>
        
        <!-- System Tray Icon (created in code-behind) -->
    </Window.Resources>

    <!-- Main Container with Transparent Area for Blur -->
    <Border Background="Transparent" CornerRadius="16">
        <Border.Effect>
            <DropShadowEffect Color="#50000000" BlurRadius="40" ShadowDepth="10" Direction="270" Opacity="0.3"/>
        </Border.Effect>

        <Grid>
            <!-- Background layer: Solid for right side, transparent for sidebar -->
            <Grid>
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="240"/>
                    <ColumnDefinition Width="*"/>
                </Grid.ColumnDefinitions>
                <!-- Left sidebar area: Transparent for blur -->
                <Border Grid.Column="0" Background="Transparent"/>
                <!-- Right content area: Solid background -->
                <Border Grid.Column="1" Background="#1A1A1A" CornerRadius="0,16,16,0"/>
            </Grid>
            
            <!-- Content on top of background -->
            <Grid>
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="240"/>
                    <ColumnDefinition Width="*"/>
                </Grid.ColumnDefinitions>

                <!-- Left Sidebar (Transparent Blur) -->
                <Grid Grid.Column="0">
                    <Grid.RowDefinitions>
                        <RowDefinition Height="50"/>
                        <RowDefinition Height="*"/>
                    </Grid.RowDefinitions>

                    <!-- App Title (Draggable) -->
                    <Border Grid.Row="0" Background="Transparent" MouseLeftButtonDown="TitleBar_MouseLeftButtonDown">
                        <StackPanel Orientation="Horizontal" Margin="20,0,0,0" VerticalAlignment="Center">
                            <TextBlock Text="PortKiller" FontSize="15" FontWeight="SemiBold" Foreground="#E0E0E0" VerticalAlignment="Center"/>
                        </StackPanel>
                    </Border>

                    <!-- Sidebar Links -->
                    <Border Grid.Row="1" BorderThickness="0,0,1,0" CornerRadius="0,0,0,16" x:Name="SidebarBorder">
                        <Border.Background>
                            <SolidColorBrush Color="#20000000" Opacity="0.5"/>
                        </Border.Background>
                        <Border.BorderBrush>
                            <SolidColorBrush Color="#40FFFFFF" Opacity="0.15"/>
                        </Border.BorderBrush>
                        <ScrollViewer VerticalScrollBarVisibility="Hidden" Margin="12">
                            <StackPanel>
                                <!-- Categories Section -->
                                <TextBlock Text="CATEGORIES" FontSize="11" FontWeight="Bold" Foreground="#707070" Margin="12,12,0,8"/>
                                <Button Content="📋  All Ports" Click="SidebarButton_Click" Tag="AllPorts" Style="{StaticResource SidebarButton}"/>
                                <Button Content="⭐  Favorites" Click="SidebarButton_Click" Tag="Favorites" Style="{StaticResource SidebarButton}"/>
                                <Button Content="👁  Watched" Click="SidebarButton_Click" Tag="Watched" Style="{StaticResource SidebarButton}"/>

                                <!-- Process Types Section -->
                                <TextBlock Text="PROCESS TYPES" FontSize="11" FontWeight="Bold" Foreground="#707070" Margin="12,24,0,8"/>
                                <Button Content="🌐  Web Server" Click="SidebarButton_Click" Tag="WebServer" Style="{StaticResource SidebarButton}"/>
                                <Button Content="💾  Database" Click="SidebarButton_Click" Tag="Database" Style="{StaticResource SidebarButton}"/>
                                <Button Content="⚙  Development" Click="SidebarButton_Click" Tag="Development" Style="{StaticResource SidebarButton}"/>
                                <Button Content="🖥  System" Click="SidebarButton_Click" Tag="System" Style="{StaticResource SidebarButton}"/>
                                <Button Content="📦  Other" Click="SidebarButton_Click" Tag="Other" Style="{StaticResource SidebarButton}"/>

                                <!-- Cloudflare Tunnels Section -->
                                <TextBlock Text="SERVICES" FontSize="11" FontWeight="Bold" Foreground="#707070" Margin="12,24,0,8"/>
                                <Button Click="SidebarButton_Click" Tag="CloudflareTunnels" Style="{StaticResource SidebarButton}">
                                    <StackPanel Orientation="Horizontal">
                                        <TextBlock Text="☁" Foreground="#F4AB3A" Margin="0,0,6,0"/>
                                        <TextBlock Text="Cloudflare Tunnels"/>
                                    </StackPanel>
                                </Button>

                                <!-- Settings Section -->
                                <TextBlock Text="SETTINGS" FontSize="11" FontWeight="Bold" Foreground="#707070" Margin="12,24,0,8"/>
                                <Button Content="⚙  Settings" Click="SidebarButton_Click" Tag="Settings" Style="{StaticResource SidebarButton}"/>
                            </StackPanel>
                        </ScrollViewer>
                    </Border>
                </Grid>

                <!-- Right Content Area (Solid) -->
                <Grid Grid.Column="1">
                    <Grid.RowDefinitions>
                        <RowDefinition Height="Auto"/>
                        <RowDefinition Height="*"/>
                    </Grid.RowDefinitions>

                    <!-- Top Bar with Search and Controls -->
                    <Border Grid.Row="0" CornerRadius="0,16,0,0" MouseLeftButtonDown="TitleBar_MouseLeftButtonDown" Background="#2A2A2A" Height="50">
                        <Grid>
                            <Grid.ColumnDefinitions>
                                <ColumnDefinition Width="*"/>
                                <ColumnDefinition Width="Auto"/>
                            </Grid.ColumnDefinitions>

                            <!-- Search and Actions - Centered (No Icon) -->
                            <StackPanel Grid.Column="0" Orientation="Horizontal" HorizontalAlignment="Center" VerticalAlignment="Center">
                                <Border BorderThickness="0" CornerRadius="20" Padding="0" Background="#1E1E1E">
                                    <Grid Width="400" Height="36">
                                        <TextBox x:Name="SearchBox" 
                                                 Background="Transparent"
                                                 BorderThickness="0"
                                                 Padding="16,8,16,8"
                                                 FontSize="13"
                                                 Foreground="#E0E0E0"
                                                 CaretBrush="#E0E0E0"
                                                 VerticalContentAlignment="Center"
                                                 TextChanged="SearchBox_TextChanged"/>
                                        <TextBlock Text="Search ports, processes..." 
                                                   FontSize="13" 
                                                   Foreground="#606060" 
                                                   VerticalAlignment="Center" 
                                                   Margin="16,0,0,0" 
                                                   IsHitTestVisible="False"
                                                   Visibility="{Binding Text.IsEmpty, ElementName=SearchBox, Converter={StaticResource BoolToVisibilityConverter}}"/>
                                    </Grid>
                                </Border>
                            </StackPanel>

                            <!-- Window Controls -->
                            <StackPanel Grid.Column="1" Orientation="Horizontal" Margin="0,0,10,0">
                                <Button Click="RefreshButton_Click" Style="{StaticResource ModernButton}" Width="40" Height="40" ToolTip="Refresh (Ctrl+R)" Margin="0,0,8,0">
                                    <TextBlock Text="↻" FontSize="16" FontWeight="Bold" Margin="0,2,0,0"/>
                                </Button>
                                <Button Click="MinimizeButton_Click" Style="{StaticResource ModernButton}" Width="40" Height="40">
                                     <TextBlock Text="—" FontSize="12" FontWeight="Bold" Margin="0,4,0,0"/>
                                </Button>
                                <Button Click="MaximizeButton_Click" Style="{StaticResource ModernButton}" Width="40" Height="40">
                                     <Rectangle Width="10" Height="10" Stroke="{Binding Foreground, RelativeSource={RelativeSource AncestorType=Button}}" StrokeThickness="1.5"/>
                                </Button>
                                <Button Click="CloseButton_Click" Style="{StaticResource ModernButton}" Width="40" Height="40" Margin="8,0,0,0">
                                    <TextBlock Text="✕" FontSize="14"/>
                                </Button>
                            </StackPanel>
                        </Grid>
                    </Border>

                    <!-- Main Content Grid -->
                    <Grid Grid.Row="1">
                        <Grid.ColumnDefinitions>
                            <ColumnDefinition Width="*"/>
                            <ColumnDefinition Width="320"/>
                        </Grid.ColumnDefinitions>

                        <!-- Port List with Solid Grey Background -->
                        <Grid Grid.Column="0" x:Name="PortsPanel" Background="#1E1E1E">
                            <Grid.RowDefinitions>
                                <RowDefinition Height="Auto"/>
                                <RowDefinition Height="*"/>
                                <RowDefinition Height="Auto"/>
                            </Grid.RowDefinitions>

                            <!-- Solid Grey Header -->
                            <Border Grid.Row="0" BorderThickness="0,0,0,1" Padding="24,16" Background="#252525" BorderBrush="#353535">
                                <TextBlock x:Name="HeaderText" Text="All Ports" FontSize="20" FontWeight="SemiBold" Foreground="#E0E0E0"/>
                            </Border>

                            <!-- Ports ListView -->
                            <ScrollViewer Grid.Row="1" VerticalScrollBarVisibility="Hidden" Padding="16">
                                <ItemsControl x:Name="PortsListView">
                                    <ItemsControl.ItemTemplate>
                                        <DataTemplate>
                                            <Border Style="{StaticResource Card}" Margin="0,0,0,12" MouseLeftButtonDown="PortItem_Click" Tag="{Binding}" Cursor="Hand">
                                                <Grid>
                                                    <Grid.ColumnDefinitions>
                                                        <ColumnDefinition Width="80"/>
                                                        <ColumnDefinition Width="*"/>
                                                        <ColumnDefinition Width="Auto"/>
                                                    </Grid.ColumnDefinitions>

                                                    <!-- Port Number with Status (Minimal Design) -->
                                                    <StackPanel Grid.Column="0" VerticalAlignment="Center">
                                                        <TextBlock Text="{Binding DisplayPort}" FontSize="20" FontWeight="Bold" Foreground="#E0E0E0" HorizontalAlignment="Center"/>
                                                        <Ellipse Width="6" Height="6" Fill="#2ecc71" HorizontalAlignment="Center" Margin="0,4,0,0" 
                                                                 Visibility="{Binding IsActive, Converter={StaticResource BoolToVisibilityConverter}}"/>
                                                    </StackPanel>

                                                    <!-- Process Info -->
                                                    <StackPanel Grid.Column="1" VerticalAlignment="Center" Margin="16,0">
                                                        <TextBlock Text="{Binding ProcessName}" FontSize="15" FontWeight="SemiBold" Foreground="#E0E0E0"/>
                                                        <TextBlock FontSize="12" Foreground="#A0A0A0" Margin="0,4,0,0">
                                                            <Run Text="Address:"/>
                                                            <Run Text="{Binding Address}" FontWeight="SemiBold"/>
                                                        </TextBlock>
                                                        <TextBlock FontSize="11" Foreground="#808080" Margin="0,2,0,0">
                                                            <Run Text="PID:"/>
                                                            <Run Text="{Binding Pid}"/>
                                                            <Run Text=" • User:"/>
                                                            <Run Text="{Binding User}"/>
                                                        </TextBlock>
                                                    </StackPanel>

                                                    <!-- Actions (Kill Button and Spinner) -->
                                                    <StackPanel Grid.Column="2" Orientation="Horizontal" VerticalAlignment="Center">
                                                        <!-- Loading Spinner (visible when killing) -->
                                                        <Border Padding="10,6"
                                                                Visibility="{Binding IsKilling, Converter={StaticResource BoolToVisibilityConverter}}">
                                                            <Grid Width="16" Height="16" RenderTransformOrigin="0.5,0.5">
                                                                <Grid.RenderTransform>
                                                                    <RotateTransform/>
                                                                </Grid.RenderTransform>
                                                                <Ellipse Width="14" Height="14"
                                                                         Stroke="#e74c3c"
                                                                         StrokeThickness="2"
                                                                         Opacity="0.3"/>
                                                                <Path Data="M 7,0 A 7,7 0 0 1 14,7"
                                                                      Stroke="#e74c3c"
                                                                      StrokeThickness="2"
                                                                      StrokeStartLineCap="Round"
                                                                      StrokeEndLineCap="Round"
                                                                      Margin="1"/>
                                                                <Grid.Style>
                                                                    <Style TargetType="Grid">
                                                                        <Style.Triggers>
                                                                            <DataTrigger Binding="{Binding IsKilling}" Value="True">
                                                                                <DataTrigger.EnterActions>
                                                                                    <BeginStoryboard>
                                                                                        <Storyboard RepeatBehavior="Forever">
                                                                                            <DoubleAnimation
                                                                                                Storyboard.TargetProperty="(Grid.RenderTransform).(RotateTransform.Angle)"
                                                                                                From="0" To="360" Duration="0:0:0.8"/>
                                                                                        </Storyboard>
                                                                                    </BeginStoryboard>
                                                                                </DataTrigger.EnterActions>
                                                                            </DataTrigger>
                                                                        </Style.Triggers>
                                                                    </Style>
                                                                </Grid.Style>
                                                            </Grid>
                                                        </Border>

                                                        <!-- Kill Button (hidden when killing) -->
                                                        <Button Content="✕"
                                                                Click="KillButton_Click"
                                                                Tag="{Binding}"
                                                                Padding="10,6"
                                                                FontSize="16"
                                                                FontWeight="Normal"
                                                                Cursor="Hand"
                                                                ToolTip="Kill Process"
                                                                Visibility="{Binding IsKilling, Converter={StaticResource InverseBoolToVisibilityConverter}}">
                                                            <Button.Style>
                                                                <Style TargetType="Button">
                                                                    <Setter Property="Background" Value="Transparent"/>
                                                                    <Setter Property="Foreground" Value="#808080"/>
                                                                    <Setter Property="BorderThickness" Value="0"/>
                                                                    <Setter Property="Template">
                                                                        <Setter.Value>
                                                                            <ControlTemplate TargetType="Button">
                                                                                <Border Background="{TemplateBinding Background}"
                                                                                        CornerRadius="6"
                                                                                        Padding="{TemplateBinding Padding}">
                                                                                    <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
                                                                                </Border>
                                                                            </ControlTemplate>
                                                                        </Setter.Value>
                                                                    </Setter>
                                                                    <Style.Triggers>
                                                                        <Trigger Property="IsMouseOver" Value="True">
                                                                            <Setter Property="Background">
                                                                                <Setter.Value>
                                                                                    <SolidColorBrush Color="#40FFFFFF" Opacity="0.1"/>
                                                                                </Setter.Value>
                                                                            </Setter>
                                                                            <Setter Property="Foreground" Value="#e74c3c"/>
                                                                        </Trigger>
                                                                    </Style.Triggers>
                                                                </Style>
                                                            </Button.Style>
                                                        </Button>
                                                    </StackPanel>
                                                </Grid>
                                            </Border>
                                        </DataTemplate>
                                    </ItemsControl.ItemTemplate>
                                </ItemsControl>
                            </ScrollViewer>

                            <!-- Empty State -->
                            <StackPanel Grid.Row="1" x:Name="EmptyState" HorizontalAlignment="Center" VerticalAlignment="Center" Visibility="Collapsed">
                                <TextBlock Text="📊" FontSize="64" HorizontalAlignment="Center" Margin="0,0,0,16" Opacity="0.2"/>
                                <TextBlock Text="No ports found" FontSize="18" Foreground="#A0A0A0" HorizontalAlignment="Center" FontWeight="SemiBold"/>
                                <TextBlock Text="Start some services to see them here" FontSize="13" Foreground="#808080" HorizontalAlignment="Center" Margin="0,8,0,0"/>
                            </StackPanel>

                            <!-- Status Bar - Solid Grey -->
                            <Border Grid.Row="2" BorderThickness="0,1,0,0" Padding="24,10" Background="#252525" BorderBrush="#353535">
                                <Grid>
                                    <TextBlock x:Name="StatusText" Text="Ready" FontSize="11" Foreground="#808080" VerticalAlignment="Center"/>
                                    <StackPanel Orientation="Horizontal" HorizontalAlignment="Right">
                                        <Ellipse Width="6" Height="6" Fill="#2ecc71" VerticalAlignment="Center" Margin="0,0,6,0"/>
                                        <TextBlock Text="Auto-refresh" FontSize="11" Foreground="#808080" VerticalAlignment="Center"/>
                                    </StackPanel>
                                </Grid>
                            </Border>
                        </Grid>

                        <!-- Detail Panel - Solid Grey -->
                        <Border Grid.Column="1" x:Name="DetailPanel" BorderThickness="1,0,0,0" Padding="24" Visibility="Collapsed" CornerRadius="0,0,16,0" Background="#1E1E1E" BorderBrush="#353535">
                            <ScrollViewer VerticalScrollBarVisibility="Hidden">
                                <StackPanel>
                                    <TextBlock Text="Port Details" FontSize="18" FontWeight="Bold" Foreground="#E0E0E0" Margin="0,0,0,20"/>

                                    <!-- Detail Items - Solid Grey -->
                                    <StackPanel Margin="0,0,0,16">
                                        <TextBlock Text="PORT" FontSize="10" FontWeight="Bold" Foreground="#808080" Margin="0,0,0,4"/>
                                        <Border CornerRadius="8" Padding="12,8" Background="#2A2A2A">
                                            <TextBlock x:Name="DetailPort" Text="-" FontSize="14" Foreground="#E0E0E0" FontWeight="SemiBold"/>
                                        </Border>
                                    </StackPanel>

                                    <StackPanel Margin="0,0,0,16">
                                        <TextBlock Text="PROCESS" FontSize="10" FontWeight="Bold" Foreground="#808080" Margin="0,0,0,4"/>
                                        <Border CornerRadius="8" Padding="12,8" Background="#2A2A2A">
                                            <TextBlock x:Name="DetailProcess" Text="-" TextWrapping="Wrap" FontSize="14" Foreground="#E0E0E0"/>
                                        </Border>
                                    </StackPanel>

                                    <Grid Margin="0,0,0,16">
                                        <Grid.ColumnDefinitions>
                                            <ColumnDefinition Width="*"/>
                                            <ColumnDefinition Width="*"/>
                                        </Grid.ColumnDefinitions>

                                        <StackPanel Grid.Column="0" Margin="0,0,8,0">
                                            <TextBlock Text="PID" FontSize="10" FontWeight="Bold" Foreground="#808080" Margin="0,0,0,4"/>
                                            <Border CornerRadius="8" Padding="12,8" Background="#2A2A2A">
                                                <TextBlock x:Name="DetailPid" Text="-" FontSize="14" Foreground="#E0E0E0"/>
                                            </Border>
                                        </StackPanel>

                                        <StackPanel Grid.Column="1" Margin="8,0,0,0">
                                            <TextBlock Text="USER" FontSize="10" FontWeight="Bold" Foreground="#808080" Margin="0,0,0,4"/>
                                            <Border CornerRadius="8" Padding="12,8" Background="#2A2A2A">
                                                <TextBlock x:Name="DetailUser" Text="-" FontSize="14" Foreground="#E0E0E0"/>
                                            </Border>
                                        </StackPanel>
                                    </Grid>

                                    <StackPanel Margin="0,0,0,16">
                                        <TextBlock Text="ADDRESS" FontSize="10" FontWeight="Bold" Foreground="#808080" Margin="0,0,0,4"/>
                                        <Border CornerRadius="8" Padding="12,8" Background="#2A2A2A">
                                            <TextBlock x:Name="DetailAddress" Text="-" FontSize="14" Foreground="#E0E0E0"/>
                                        </Border>
                                    </StackPanel>

                                    <StackPanel Margin="0,0,0,20">
                                        <TextBlock Text="COMMAND" FontSize="10" FontWeight="Bold" Foreground="#808080" Margin="0,0,0,4"/>
                                        <Border CornerRadius="8" Padding="12,8" Background="#2A2A2A">
                                            <TextBlock x:Name="DetailCommand" Text="-" TextWrapping="Wrap" FontSize="12" Foreground="#E0E0E0"/>
                                        </Border>
                                    </StackPanel>

                                    <!-- Action Buttons - Clean Minimal Outline Style -->
                                    <StackPanel Margin="0,10,0,0">
                                        <Button x:Name="ShareTunnelButton" 
                                                Click="ShareTunnelButton_Click"
                                                Style="{StaticResource OutlineButton}"
                                                Margin="0,0,0,10"
                                                HorizontalAlignment="Stretch">
                                            <StackPanel Orientation="Horizontal">
                                                <TextBlock Text="☁" Foreground="#F4AB3A" Margin="0,0,6,0"/>
                                                <TextBlock Text="Share via Tunnel"/>
                                            </StackPanel>
                                        </Button>

                                        <Button x:Name="FavoriteButton" 
                                                Content="⭐  Add to Favorites" 
                                                Click="FavoriteButton_Click"
                                                Style="{StaticResource OutlineButton}"
                                                Margin="0,0,0,10"
                                                HorizontalAlignment="Stretch"/>

                                        <Button x:Name="WatchButton" 
                                                Content="👁  Watch Port" 
                                                Click="WatchButton_Click"
                                                Style="{StaticResource OutlineButton}"
                                                HorizontalAlignment="Stretch"/>
                                    </StackPanel>
                                </StackPanel>
                            </ScrollViewer>
                        </Border>
                    </Grid>

                    <!-- Cloudflare Tunnels Panel (Hidden by Default) -->
                    <Grid Grid.Column="0" Grid.ColumnSpan="2" x:Name="TunnelsPanel" Background="#1E1E1E" Visibility="Collapsed">
                        <Grid.RowDefinitions>
                            <RowDefinition Height="Auto"/>
                            <RowDefinition Height="*"/>
                            <RowDefinition Height="Auto"/>
                        </Grid.RowDefinitions>

                        <!-- Tunnels Header -->
                        <Border Grid.Row="0" BorderThickness="0,0,0,1" Padding="24,16" Background="#252525" BorderBrush="#353535">
                            <Grid>
                                <StackPanel Orientation="Horizontal" VerticalAlignment="Center">
                                    <TextBlock Text="☁" FontSize="20" Margin="0,0,10,0" Foreground="#F4AB3A"/>
                                    <TextBlock Text="Cloudflare Tunnels" FontSize="20" FontWeight="SemiBold" Foreground="#E0E0E0"/>
                                </StackPanel>
                                <StackPanel Orientation="Horizontal" HorizontalAlignment="Right">
                                    <StackPanel Orientation="Horizontal" VerticalAlignment="Center" Margin="0,0,12,0">
                                        <TextBlock Text="Protocol" FontSize="12" Foreground="#A0A0A0" VerticalAlignment="Center" Margin="0,0,8,0"/>
                                        <ComboBox x:Name="TunnelProtocolCombo"
                                                  Width="90"
                                                  ItemsSource="{Binding ProtocolOptions}"
                                                  SelectedValuePath="Value"
                                                  SelectedValue="{Binding CloudflaredProtocol, Mode=TwoWay}"
                                                  DisplayMemberPath="Label"
                                                  Background="#3A3A3A"
                                                  Foreground="#E0E0E0"
                                                  BorderThickness="0"
                                                  Padding="6,2"/>
                                    </StackPanel>
                                    <Button x:Name="StopAllTunnelsButton" 
                                            Content="Stop All" 
                                            Click="StopAllTunnels_Click"
                                            Visibility="Collapsed"
                                            Margin="0,0,8,0">
                                        <Button.Style>
                                            <Style TargetType="Button">
                                                <Setter Property="Background" Value="#e74c3c"/>
                                                <Setter Property="Foreground" Value="#FFFFFF"/>
                                                <Setter Property="BorderThickness" Value="0"/>
                                                <Setter Property="Padding" Value="12,6"/>
                                                <Setter Property="FontSize" Value="12"/>
                                                <Setter Property="Cursor" Value="Hand"/>
                                                <Setter Property="Template">
                                                    <Setter.Value>
                                                        <ControlTemplate TargetType="Button">
                                                            <Border Background="{TemplateBinding Background}" CornerRadius="6" Padding="{TemplateBinding Padding}">
                                                                <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
                                                            </Border>
                                                        </ControlTemplate>
                                                    </Setter.Value>
                                                </Setter>
                                                <Style.Triggers>
                                                    <Trigger Property="IsMouseOver" Value="True">
                                                        <Setter Property="Background" Value="#c0392b"/>
                                                    </Trigger>
                                                </Style.Triggers>
                                            </Style>
                                        </Button.Style>
                                    </Button>
                                    <Button Content="↻ Refresh" Click="RefreshTunnels_Click" Style="{StaticResource ModernButton}"/>
                                </StackPanel>
                            </Grid>
                        </Border>

                        <!-- Cloudflared Not Installed Warning -->
                        <Border Grid.Row="1" 
                                x:Name="CloudflaredWarning"
                                Background="#3d2918" 
                                BorderBrush="#8B4513" 
                                BorderThickness="1" 
                                CornerRadius="8" 
                                Padding="16"
                                Margin="24,16"
                                VerticalAlignment="Top"
                                Visibility="Collapsed">
                            <StackPanel>
                                <StackPanel Orientation="Horizontal" Margin="0,0,0,8">
                                    <TextBlock Text="⚠" FontSize="20" Margin="0,0,12,0" Foreground="#f39c12"/>
                                    <TextBlock Text="cloudflared Not Installed" FontSize="16" FontWeight="Bold" Foreground="#f39c12" VerticalAlignment="Center"/>
                                </StackPanel>
                                <TextBlock TextWrapping="Wrap" Foreground="#E0E0E0" Margin="32,0,0,8">
                                    To use Cloudflare Tunnels, you need to install cloudflared:
                                </TextBlock>
                                <TextBlock TextWrapping="Wrap" Foreground="#B0B0B0" Margin="32,0,0,0" FontFamily="Consolas" FontSize="11">
                                    • Download from: https://github.com/cloudflare/cloudflared/releases
                                    • Or use Chocolatey: choco install cloudflared
                                </TextBlock>
                            </StackPanel>
                        </Border>

                        <!-- Tunnels List -->
                        <ScrollViewer Grid.Row="1" VerticalScrollBarVisibility="Hidden" Padding="16">
                            <ItemsControl x:Name="TunnelsListView">
                                <ItemsControl.ItemTemplate>
                                    <DataTemplate>
                                        <Border Style="{StaticResource Card}" Margin="0,0,0,12" Cursor="Hand">
                                            <Grid>
                                                <Grid.ColumnDefinitions>
                                                    <ColumnDefinition Width="Auto"/>
                                                    <ColumnDefinition Width="*"/>
                                                    <ColumnDefinition Width="Auto"/>
                                                </Grid.ColumnDefinitions>

                                                <!-- Status Indicator -->
                                                <StackPanel Grid.Column="0" Margin="0,0,16,0" VerticalAlignment="Center">
                                                    <Ellipse Width="12" Height="12" 
                                                             Fill="{Binding StatusColor}"
                                                             HorizontalAlignment="Center"
                                                             Margin="0,0,0,4"/>
                                                    <TextBlock Text="{Binding StatusText}" 
                                                               FontSize="10" 
                                                               Foreground="#A0A0A0"
                                                               HorizontalAlignment="Center"/>
                                                </StackPanel>

                                                <!-- Port and URL Info -->
                                                <StackPanel Grid.Column="1" VerticalAlignment="Center">
                                                    <TextBlock FontSize="18" FontWeight="Bold" Foreground="#E0E0E0" Margin="0,0,0,4">
                                                        <Run Text="Port"/>
                                                        <Run Text="{Binding Port}" Foreground="#3498db"/>
                                                    </TextBlock>
                                                    <TextBlock Text="{Binding DisplayUrl}" 
                                                               FontSize="13" 
                                                               Foreground="#2ecc71"
                                                               FontFamily="Consolas"
                                                               Margin="0,2,0,0"/>
                                                    <TextBlock Text="{Binding LastError}" 
                                                               FontSize="11" 
                                                               Foreground="#e74c3c"
                                                               TextWrapping="Wrap"
                                                               Margin="0,4,0,0"/>
                                                </StackPanel>

                                                <!-- Actions -->
                                                <StackPanel Grid.Column="2" Orientation="Horizontal" VerticalAlignment="Center">
                                                    <!-- Uptime -->
                                                    <Border Background="#3A3A3A" 
                                                            CornerRadius="6" 
                                                            Padding="10,6" 
                                                            Margin="0,0,8,0"
                                                            VerticalAlignment="Center"
                                                            Visibility="{Binding IsActive, Converter={StaticResource BoolToVisibilityConverter}}">
                                                        <StackPanel Orientation="Horizontal" VerticalAlignment="Center">
                                                            <TextBlock Text="⏱" FontSize="16" Margin="0,0,6,0" VerticalAlignment="Center"/>
                                                            <TextBlock Text="{Binding Uptime}" FontSize="14" Foreground="#E0E0E0" VerticalAlignment="Center" FontWeight="SemiBold"/>
                                                        </StackPanel>
                                                    </Border>

                                                    <!-- Copy Button -->
                                                    <Button ToolTip="Copy URL"
                                                            Click="TunnelCopy_Click"
                                                            Tag="{Binding}"
                                                            Style="{StaticResource ModernButton}"
                                                            Width="36" Height="36"
                                                            Padding="6"
                                                            Margin="0,0,4,0">
                                                        <TextBlock Text="📋" FontSize="16"/>
                                                    </Button>

                                                    <!-- Open in Browser Button -->
                                                    <Button ToolTip="Open in Browser"
                                                            Click="TunnelOpen_Click"
                                                            Tag="{Binding}"
                                                            Style="{StaticResource ModernButton}"
                                                            Width="36" Height="36"
                                                            Padding="6"
                                                            Margin="0,0,4,0">
                                                        <TextBlock Text="🌐" FontSize="16"/>
                                                    </Button>

                                                    <!-- Stop Button -->
                                                    <Button ToolTip="Stop Tunnel"
                                                            Click="TunnelStop_Click"
                                                            Tag="{Binding}"
                                                            Width="36" Height="36"
                                                            Padding="6">
                                                        <Button.Style>
                                                            <Style TargetType="Button">
                                                                <Setter Property="Background" Value="#e74c3c"/>
                                                                <Setter Property="Foreground" Value="#FFFFFF"/>
                                                                <Setter Property="BorderThickness" Value="0"/>
                                                                <Setter Property="Cursor" Value="Hand"/>
                                                                <Setter Property="Template">
                                                                    <Setter.Value>
                                                                        <ControlTemplate TargetType="Button">
                                                                            <Border Background="{TemplateBinding Background}" CornerRadius="6" Padding="6">
                                                                                <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
                                                                            </Border>
                                                                        </ControlTemplate>
                                                                    </Setter.Value>
                                                                </Setter>
                                                                <Style.Triggers>
                                                                    <Trigger Property="IsMouseOver" Value="True">
                                                                        <Setter Property="Background" Value="#c0392b"/>
                                                                    </Trigger>
                                                                </Style.Triggers>
                                                            </Style>
                                                        </Button.Style>
                                                        <TextBlock Text="✕" FontSize="14"/>
                                                    </Button>
                                                </StackPanel>
                                            </Grid>
                                        </Border>
                                    </DataTemplate>
                                </ItemsControl.ItemTemplate>
                            </ItemsControl>
                        </ScrollViewer>

                        <!-- Tunnels Empty State -->
                        <StackPanel Grid.Row="1" x:Name="TunnelsEmptyState" HorizontalAlignment="Center" VerticalAlignment="Center" Visibility="Visible">
                            <TextBlock Text="☁" FontSize="64" HorizontalAlignment="Center" Margin="0,0,0,16" Opacity="0.3" Foreground="#F4AB3A"/>
                            <TextBlock Text="No Active Tunnels" FontSize="20" Foreground="#A0A0A0" HorizontalAlignment="Center" FontWeight="SemiBold"/>
                            <TextBlock Text="Start a tunnel from the port list to create a public URL" 
                                       FontSize="13" 
                                       Foreground="#808080" 
                                       HorizontalAlignment="Center" 
                                       Margin="0,8,0,16"
                                       TextAlignment="Center"/>
                            <TextBlock TextWrapping="Wrap" 
                                       FontSize="12" 
                                       Foreground="#606060" 
                                       HorizontalAlignment="Center" 
                                       TextAlignment="Center"
                                       MaxWidth="400">
                                💡 Tip: Cloudflare Tunnels make your localhost ports accessible from anywhere on the internet with automatic HTTPS
                            </TextBlock>
                        </StackPanel>

                        <!-- Tunnels Status Bar -->
                        <Border Grid.Row="2" BorderThickness="0,1,0,0" Padding="24,10" Background="#252525" BorderBrush="#353535" CornerRadius="0,0,16,0">
                            <Grid>
                                <StackPanel Orientation="Horizontal">
                                    <Ellipse x:Name="TunnelStatusDot" Width="6" Height="6" Fill="#808080" VerticalAlignment="Center" Margin="0,0,6,0"/>
                                    <TextBlock x:Name="TunnelStatusText" Text="0 active tunnel(s)" FontSize="11" Foreground="#808080" VerticalAlignment="Center"/>
                                </StackPanel>
                                <StackPanel x:Name="CloudflaredInstalledIndicator" Orientation="Horizontal" HorizontalAlignment="Right" Visibility="Collapsed">
                                    <TextBlock Text="✓" FontSize="14" Foreground="#2ecc71" Margin="0,0,6,0" VerticalAlignment="Center"/>
                                    <TextBlock Text="cloudflared installed" FontSize="11" Foreground="#808080" VerticalAlignment="Center"/>
                                </StackPanel>
                            </Grid>
                        </Border>
                    </Grid>
                </Grid>
            </Grid>
        </Grid>
    </Border>
</Window>
```

## File: `platforms/windows/PortKiller/MainWindow.xaml.cs`
```csharp
using System;
using System.Linq;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using Microsoft.Extensions.DependencyInjection;
using PortKiller.Models;
using PortKiller.ViewModels;
using PortKiller.Helpers;

namespace PortKiller;

public partial class MainWindow : Window
{
    private readonly MainViewModel _viewModel;
    private readonly TunnelViewModel _tunnelViewModel;
    private Hardcodet.Wpf.TaskbarNotification.TaskbarIcon? _trayIcon;
    private bool _isShuttingDown = false;

    public MainWindow()
    {
        InitializeComponent();

        _viewModel = App.Services.GetRequiredService<MainViewModel>();
        _tunnelViewModel = App.Services.GetRequiredService<TunnelViewModel>();
        TunnelProtocolCombo.DataContext = _tunnelViewModel;
        InitializeAsync();
        
        // Setup keyboard shortcuts
        SetupKeyboardShortcuts();
        
        // Initialize system tray icon
        InitializeTrayIcon();
        
        // Ensure window is visible and activated on startup
        Loaded += (s, e) =>
        {
            Show();
            Activate();
            WindowState = WindowState.Normal;
        };
    }

    private void InitializeTrayIcon()
    {
        _trayIcon = new Hardcodet.Wpf.TaskbarNotification.TaskbarIcon
        {
            ToolTipText = "PortKiller",
            Visibility = Visibility.Visible
        };

        // Create icon from text (simple fallback)
        _trayIcon.Icon = CreateTrayIcon();

        // Setup context menu
        var contextMenu = new ContextMenu
        {
            Background = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(42, 42, 42)),
            Foreground = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(224, 224, 224))
        };

        var openItem = new MenuItem { Header = "🪟  Open Main Window", FontWeight = FontWeights.SemiBold };
        openItem.Click += TrayOpenMain_Click;
        contextMenu.Items.Add(openItem);
        
        contextMenu.Items.Add(new Separator());

        var refreshItem = new MenuItem { Header = "○  Refresh", InputGestureText = "Ctrl+R" };
        refreshItem.Click += TrayRefresh_Click;
        contextMenu.Items.Add(refreshItem);

        var killAllItem = new MenuItem { Header = "✕  Kill All", InputGestureText = "Ctrl+K" };
        killAllItem.Click += TrayKillAll_Click;
        contextMenu.Items.Add(killAllItem);

        contextMenu.Items.Add(new Separator());

        var settingsItem = new MenuItem { Header = "⚙  Settings" };
        settingsItem.Click += TraySettings_Click;
        contextMenu.Items.Add(settingsItem);

        var quitItem = new MenuItem { Header = "×  Quit", InputGestureText = "Ctrl+Q" };
        quitItem.Click += TrayQuit_Click;
        contextMenu.Items.Add(quitItem);

        _trayIcon.ContextMenu = contextMenu;
        _trayIcon.TrayLeftMouseDown += TrayIcon_Click;
    }

    private System.Drawing.Icon CreateTrayIcon()
    {
        // Create a simple icon with a network symbol
        var bitmap = new System.Drawing.Bitmap(16, 16);
        using (var g = System.Drawing.Graphics.FromImage(bitmap))
        {
            g.Clear(System.Drawing.Color.Transparent);
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            
            // Draw a simple network/port icon (circle with dot)
            using (var pen = new System.Drawing.Pen(System.Drawing.Color.White, 2))
            {
                g.DrawEllipse(pen, 3, 3, 10, 10);
                g.FillEllipse(System.Drawing.Brushes.White, 6, 6, 4, 4);
            }
        }
        
        return System.Drawing.Icon.FromHandle(bitmap.GetHicon());
    }

    private async void InitializeAsync()
    {
        await _viewModel.InitializeAsync();
        UpdateUI();

        // Subscribe to property changes
        _viewModel.PropertyChanged += (s, e) =>
        {
            if (e.PropertyName == nameof(_viewModel.FilteredPorts) ||
                e.PropertyName == nameof(_viewModel.IsScanning))
            {
                Dispatcher.Invoke(UpdateUI);
            }
            
            if (e.PropertyName == nameof(_viewModel.Ports))
            {
                Dispatcher.Invoke(UpdateTrayMenu);
            }
        };
    }

    private void UpdateUI()
    {
        // Update ports list
        PortsListView.ItemsSource = _viewModel.FilteredPorts;

        // Update empty state
        EmptyState.Visibility = _viewModel.FilteredPorts.Count == 0 ? Visibility.Visible : Visibility.Collapsed;

        // Update status
        StatusText.Text = _viewModel.IsScanning
            ? "Scanning ports..."
            : $"{_viewModel.FilteredPorts.Count} port(s) listening";
    }

    // Window Controls
    private void TitleBar_MouseLeftButtonDown(object sender, MouseButtonEventArgs e)
    {
        if (e.ClickCount == 2)
        {
            WindowState = WindowState == WindowState.Maximized ? WindowState.Normal : WindowState.Maximized;
        }
        else
        {
            DragMove();
        }
    }

    private void MinimizeButton_Click(object sender, RoutedEventArgs e)
    {
        WindowState = WindowState.Minimized;
    }

    private void MaximizeButton_Click(object sender, RoutedEventArgs e)
    {
        WindowState = WindowState == WindowState.Maximized ? WindowState.Normal : WindowState.Maximized;
    }

    private void CloseButton_Click(object sender, RoutedEventArgs e)
    {
        Close();
    }

    private async void RefreshButton_Click(object sender, RoutedEventArgs e)
    {
        await _viewModel.RefreshPortsCommand.ExecuteAsync(null);
    }

    private void SearchBox_TextChanged(object sender, TextChangedEventArgs e)
    {
        _viewModel.Search(SearchBox.Text);
    }

    private void SidebarButton_Click(object sender, RoutedEventArgs e)
    {
        if (sender is Button button && button.Tag is string tag)
        {
            if (Enum.TryParse<SidebarItem>(tag, out var sidebarItem))
            {
                _viewModel.SelectedSidebarItem = sidebarItem;
                HeaderText.Text = sidebarItem.GetTitle();
                
                // Toggle between ports view and tunnels view
                if (sidebarItem == SidebarItem.CloudflareTunnels)
                {
                    PortsPanel.Visibility = Visibility.Collapsed;
                    DetailPanel.Visibility = Visibility.Collapsed;
                    TunnelsPanel.Visibility = Visibility.Visible;
                    UpdateTunnelsUI();
                }
                else
                {
                    TunnelsPanel.Visibility = Visibility.Collapsed;
                    PortsPanel.Visibility = Visibility.Visible;
                }
                
                // Highlight selected button (optional enhancement)
                foreach (var child in ((button.Parent as Panel)?.Children ?? new UIElementCollection(null, null)))
                {
                    if (child is Button btn)
                    {
                        btn.Background = System.Windows.Media.Brushes.Transparent;
                    }
                }
                button.Background = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromArgb(25, 52, 152, 219));
            }
        }
    }

    private void PortItem_Click(object sender, MouseButtonEventArgs e)
    {
        if (sender is Border border && border.Tag is PortInfo port)
        {
            _viewModel.SelectedPort = port;
            ShowPortDetails(port);
        }
    }

    private void ShowPortDetails(PortInfo port)
    {
        DetailPanel.Visibility = Visibility.Visible;

        DetailPort.Text = port.DisplayPort;
        DetailProcess.Text = port.ProcessName;
        DetailPid.Text = port.Pid.ToString();
        DetailAddress.Text = port.Address;
        DetailUser.Text = port.User;
        DetailCommand.Text = port.Command;

        // Update favorite button
        FavoriteButton.Content = _viewModel.IsFavorite(port.Port)
            ? "⭐ Remove from Favorites"
            : "⭐ Add to Favorites";

        // Update watch button
        WatchButton.Content = _viewModel.IsWatched(port.Port)
            ? "👁 Unwatch Port"
            : "👁 Watch Port";
    }

    private async void KillButton_Click(object sender, RoutedEventArgs e)
    {
        if (sender is Button button && button.Tag is PortInfo port)
        {
            var dialog = new ConfirmDialog(
                $"Are you sure you want to kill the process on port {port.Port}?",
                $"Process: {port.ProcessName}\nPID: {port.Pid}\n\nThis action cannot be undone.",
                "Kill Process")
            {
                Owner = this
            };
            
            dialog.ShowDialog();

            if (dialog.Result)
            {
                await _viewModel.KillProcessCommand.ExecuteAsync(port);
            }
        }
    }

    private void FavoriteButton_Click(object sender, RoutedEventArgs e)
    {
        if (_viewModel.SelectedPort != null)
        {
            _viewModel.ToggleFavoriteCommand.Execute(_viewModel.SelectedPort.Port);
            ShowPortDetails(_viewModel.SelectedPort);
        }
    }

    private void WatchButton_Click(object sender, RoutedEventArgs e)
    {
        if (_viewModel.SelectedPort != null)
        {
            var port = _viewModel.SelectedPort.Port;

            if (_viewModel.IsWatched(port))
            {
                _viewModel.RemoveWatchedPortCommand.Execute(port);
            }
            else
            {
                _viewModel.AddWatchedPortCommand.Execute(port);
            }

            ShowPortDetails(_viewModel.SelectedPort);
        }
    }

    private async void ShareTunnelButton_Click(object sender, RoutedEventArgs e)
    {
        if (_viewModel.SelectedPort == null)
            return;

        var port = _viewModel.SelectedPort.Port;

        // Navigate to Cloudflare Tunnels panel in sidebar
        _viewModel.SelectedSidebarItem = SidebarItem.CloudflareTunnels;
        HeaderText.Text = SidebarItem.CloudflareTunnels.GetTitle();
        
        // Toggle to tunnels view
        PortsPanel.Visibility = Visibility.Collapsed;
        DetailPanel.Visibility = Visibility.Collapsed;
        TunnelsPanel.Visibility = Visibility.Visible;
        UpdateTunnelsUI();

        // Start tunnel for the selected port
        await _tunnelViewModel.StartTunnelAsync(port);
    }

    // Window loaded event - enable blur for sidebar only
    private void Window_Loaded(object sender, RoutedEventArgs e)
    {
        try
        {
            // Enable acrylic blur effect for the entire window (sidebar will show blur through transparency)
            WindowBlurHelper.EnableAcrylicBlur(this, blurOpacity: 180, blurColor: 0x1A1A1A);
        }
        catch (Exception ex)
        {
            // Blur not supported on this system
            System.Diagnostics.Debug.WriteLine($"Blur effect not supported: {ex.Message}");
        }
    }

    // Keyboard shortcuts
    private void SetupKeyboardShortcuts()
    {
        var refreshGesture = new KeyGesture(Key.R, ModifierKeys.Control);
        var killAllGesture = new KeyGesture(Key.K, ModifierKeys.Control);
        var quitGesture = new KeyGesture(Key.Q, ModifierKeys.Control);

        InputBindings.Add(new KeyBinding(_viewModel.RefreshPortsCommand, refreshGesture));
        InputBindings.Add(new KeyBinding(ApplicationCommands.Close, quitGesture));
        
        CommandBindings.Add(new CommandBinding(ApplicationCommands.Close, (s, e) => Close()));
    }

    // System tray icon handlers
    private void TrayIcon_Click(object sender, RoutedEventArgs e)
    {
        // Show mini popup window near tray
        var miniWindow = new MiniPortKillerWindow();
        miniWindow.ShowNearTray();
    }

    private async void TrayRefresh_Click(object sender, RoutedEventArgs e)
    {
        await _viewModel.RefreshPortsCommand.ExecuteAsync(null);
    }

    private async void TrayKillAll_Click(object sender, RoutedEventArgs e)
    {
        var dialog = new ConfirmDialog(
            "Are you sure you want to kill ALL processes on listening ports?",
            $"This will terminate {_viewModel.Ports.Count} process(es).\n\nThis action cannot be undone.",
            "Kill All Processes")
        {
            Owner = this
        };
        
        dialog.ShowDialog();

        if (dialog.Result)
        {
            foreach (var port in _viewModel.Ports.ToList())
            {
                try
                {
                    await _viewModel.KillProcessCommand.ExecuteAsync(port);
                }
                catch (Exception ex)
                {
                    System.Diagnostics.Debug.WriteLine($"Failed to kill process on port {port.Port}: {ex.Message}");
                }
            }
        }
    }

    // Cloudflare Tunnels Methods
    private void UpdateTunnelsUI()
    {
        // Bind tunnels list to view model
        TunnelsListView.ItemsSource = _tunnelViewModel.Tunnels;
        
        // Update empty state
        TunnelsEmptyState.Visibility = _tunnelViewModel.Tunnels.Count == 0 ? Visibility.Visible : Visibility.Collapsed;
        
        // Update status bar
        var count = _tunnelViewModel.ActiveTunnelCount;
        TunnelStatusText.Text = $"{count} active tunnel(s)";
        TunnelStatusDot.Fill = count > 0 
            ? new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(46, 204, 113))
            : new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(128, 128, 128));
        
        // Update Stop All button visibility
        StopAllTunnelsButton.Visibility = _tunnelViewModel.Tunnels.Count > 0 ? Visibility.Visible : Visibility.Collapsed;
        
        // Update cloudflared installed indicator
        CloudflaredWarning.Visibility = _tunnelViewModel.IsCloudflaredInstalled ? Visibility.Collapsed : Visibility.Visible;
        CloudflaredInstalledIndicator.Visibility = _tunnelViewModel.IsCloudflaredInstalled ? Visibility.Visible : Visibility.Collapsed;
        
        // Subscribe to collection changes if not already
        _tunnelViewModel.Tunnels.CollectionChanged -= OnTunnelsCollectionChanged;
        _tunnelViewModel.Tunnels.CollectionChanged += OnTunnelsCollectionChanged;
    }

    private void OnTunnelsCollectionChanged(object? sender, System.Collections.Specialized.NotifyCollectionChangedEventArgs e)
    {
        Dispatcher.Invoke(() =>
        {
            TunnelsEmptyState.Visibility = _tunnelViewModel.Tunnels.Count == 0 ? Visibility.Visible : Visibility.Collapsed;
            
            var count = _tunnelViewModel.ActiveTunnelCount;
            TunnelStatusText.Text = $"{count} active tunnel(s)";
            TunnelStatusDot.Fill = count > 0 
                ? new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(46, 204, 113))
                : new System.Windows.Media.SolidColorBrush(System.Windows.Media.Color.FromRgb(128, 128, 128));
            
            StopAllTunnelsButton.Visibility = _tunnelViewModel.Tunnels.Count > 0 ? Visibility.Visible : Visibility.Collapsed;
        });
    }

    private void RefreshTunnels_Click(object sender, RoutedEventArgs e)
    {
        _tunnelViewModel.RecheckInstallation();
        UpdateTunnelsUI();
    }

    private async void StopAllTunnels_Click(object sender, RoutedEventArgs e)
    {
        var dialog = new ConfirmDialog(
            $"Are you sure you want to stop all {_tunnelViewModel.Tunnels.Count} tunnel(s)?",
            "All public URLs will be terminated immediately.\n\nThis action cannot be undone.",
            "Stop All Tunnels")
        {
            Owner = this
        };
        
        dialog.ShowDialog();

        if (dialog.Result)
        {
            await _tunnelViewModel.StopAllTunnelsAsync();
            UpdateTunnelsUI();
        }
    }

    private async void TunnelStop_Click(object sender, RoutedEventArgs e)
    {
        if (sender is not FrameworkElement { Tag: CloudflareTunnel tunnel })
            return;

        await _tunnelViewModel.StopTunnelAsync(tunnel);
    }

    private void TunnelCopy_Click(object sender, RoutedEventArgs e)
    {
        if (sender is not FrameworkElement { Tag: CloudflareTunnel tunnel })
            return;

        if (!string.IsNullOrEmpty(tunnel.TunnelUrl))
        {
            _tunnelViewModel.CopyUrlToClipboard(tunnel.TunnelUrl);
        }
    }

    private void TunnelOpen_Click(object sender, RoutedEventArgs e)
    {
        if (sender is not FrameworkElement { Tag: CloudflareTunnel tunnel })
            return;

        if (!string.IsNullOrEmpty(tunnel.TunnelUrl))
        {
            _tunnelViewModel.OpenUrlInBrowser(tunnel.TunnelUrl);
        }
    }

    private void TrayOpenMain_Click(object sender, RoutedEventArgs e)
    {
        Show();
        WindowState = WindowState.Normal;
        Activate();
    }

    private void TraySettings_Click(object sender, RoutedEventArgs e)
    {
        _viewModel.SelectedSidebarItem = SidebarItem.Settings;
        HeaderText.Text = "Settings";
        Show();
        WindowState = WindowState.Normal;
        Activate();
    }

    private void TrayQuit_Click(object sender, RoutedEventArgs e)
    {
        _isShuttingDown = true;
        Application.Current.Shutdown();
    }

    // Override close button to minimize to tray instead
    protected override void OnClosing(System.ComponentModel.CancelEventArgs e)
    {
        if (!_isShuttingDown)
        {
            e.Cancel = true;
            Hide();
        }
        base.OnClosing(e);
    }

    protected override void OnClosed(EventArgs e)
    {
        _trayIcon?.Dispose();
        base.OnClosed(e);
    }

    // Update tray menu with active ports
    private void UpdateTrayMenu()
    {
        if (_trayIcon == null || _trayIcon.ContextMenu == null) return;

        var contextMenu = _trayIcon.ContextMenu;
        
        // Remove old port menu items (everything before first separator)
        var firstSeparatorIndex = contextMenu.Items.Cast<object>()
            .TakeWhile(item => item is not Separator)
            .Count();
        
        // Remove old port items
        for (int i = contextMenu.Items.Count - 1; i >= 0; i--)
        {
            if (contextMenu.Items[i] is MenuItem menuItem && menuItem.Tag is PortInfo)
            {
                contextMenu.Items.RemoveAt(i);
            }
        }

        // Add header if there are ports
        var ports = _viewModel.Ports.Take(10).ToList(); // Limit to 10 ports
        
        if (ports.Any())
        {
            // Find the first separator and insert ports before it
            var separatorIndex = -1;
            for (int i = 0; i < contextMenu.Items.Count; i++)
            {
                if (contextMenu.Items[i] is Separator)
                {
                    separatorIndex = i;
                    break;
                }
            }

            if (separatorIndex > 0)
            {
                // Insert ports after "Active Ports" header
                int insertIndex = 1;
                foreach (var port in ports)
                {
                    var portMenuItem = new MenuItem
                    {
                        Header = $"● :{port.Port}  {port.ProcessName} (PID: {port.Pid})",
                        Tag = port
                    };
                    portMenuItem.Click += async (s, e) =>
                    {
                        var menuItem = s as MenuItem;
                        if (menuItem?.Tag is PortInfo portInfo)
                        {
                            var dialog = new ConfirmDialog(
                                $"Kill process on port {portInfo.Port}?",
                                $"Process: {portInfo.ProcessName}\nPID: {portInfo.Pid}",
                                "Kill Process")
                            {
                                Owner = this
                            };
                            
                            dialog.ShowDialog();

                            if (dialog.Result)
                            {
                                await _viewModel.KillProcessCommand.ExecuteAsync(portInfo);
                            }
                        }
                    };
                    contextMenu.Items.Insert(insertIndex++, portMenuItem);
                }
            }
        }
    }
}
```

## File: `platforms/windows/PortKiller/MiniPortKillerWindow.xaml`
```
<Window x:Class="PortKiller.MiniPortKillerWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:models="clr-namespace:PortKiller.Models"
        mc:Ignorable="d"
        Title="PortKiller Mini"
        Width="320" Height="500"
        WindowStyle="None"
        AllowsTransparency="True"
        Background="Transparent"
        ResizeMode="NoResize"
        ShowInTaskbar="False"
        Topmost="True"
        Deactivated="Window_Deactivated">

    <Window.Resources>
        <!-- Colors -->
        <SolidColorBrush x:Key="WindowBackground" Color="#C8282828"/> <!-- 78% opacity lighter grey for transparency -->
        <SolidColorBrush x:Key="BorderBrush" Color="#40FFFFFF"/>
        <SolidColorBrush x:Key="TextPrimary" Color="#FFFFFF"/>
        <SolidColorBrush x:Key="TextSecondary" Color="#B0FFFFFF"/>
        <SolidColorBrush x:Key="TextTertiary" Color="#60FFFFFF"/>
        <SolidColorBrush x:Key="AccentColor" Color="#5B9DD9"/>
        <SolidColorBrush x:Key="DangerColor" Color="#FF453A"/>
        <SolidColorBrush x:Key="HoverBackground" Color="#20FFFFFF"/>

        <!-- Menu Button Style -->
        <Style x:Key="MenuButtonStyle" TargetType="Button">
            <Setter Property="Background" Value="Transparent"/>
            <Setter Property="BorderThickness" Value="0"/>
            <Setter Property="Foreground" Value="{StaticResource TextPrimary}"/>
            <Setter Property="Padding" Value="12,8"/>
            <Setter Property="HorizontalContentAlignment" Value="Stretch"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="Button">
                        <Border Background="{TemplateBinding Background}" 
                                Padding="{TemplateBinding Padding}" 
                                CornerRadius="10" 
                                Margin="2,2">
                            <ContentPresenter/>
                        </Border>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
            <Style.Triggers>
                <Trigger Property="IsMouseOver" Value="True">
                    <Setter Property="Background" Value="#30FFFFFF"/> <!-- Subtle White tint on hover -->
                </Trigger>
            </Style.Triggers>
        </Style>

        <!-- ListBox Item Style -->
        <Style x:Key="PortListBoxItemStyle" TargetType="ListBoxItem">
            <Setter Property="Background" Value="Transparent"/>
            <Setter Property="BorderThickness" Value="0"/>
            <Setter Property="Padding" Value="12,6"/>
            <Setter Property="HorizontalContentAlignment" Value="Stretch"/>
            <Setter Property="Margin" Value="2,1"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="ListBoxItem">
                        <Border Background="{TemplateBinding Background}" 
                                Padding="{TemplateBinding Padding}" 
                                CornerRadius="10">
                            <ContentPresenter/>
                        </Border>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
            <Style.Triggers>
                <Trigger Property="IsMouseOver" Value="True">
                    <Setter Property="Background" Value="#30FFFFFF"/>
                </Trigger>
                <Trigger Property="IsSelected" Value="True">
                    <Setter Property="Background" Value="#40FFFFFF"/>
                </Trigger>
            </Style.Triggers>
        </Style>

        <!-- Context Menu Style -->
        <Style x:Key="ModernContextMenu" TargetType="ContextMenu">
            <Setter Property="Background" Value="#D8282828"/>
            <Setter Property="BorderBrush" Value="#40FFFFFF"/>
            <Setter Property="BorderThickness" Value="1"/>
            <Setter Property="Padding" Value="2"/>
            <Setter Property="HasDropShadow" Value="True"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="ContextMenu">
                        <Border Background="{TemplateBinding Background}"
                                BorderBrush="{TemplateBinding BorderBrush}"
                                BorderThickness="{TemplateBinding BorderThickness}"
                                CornerRadius="8"
                                Padding="{TemplateBinding Padding}">
                            <Border.Effect>
                                <DropShadowEffect Color="Black" Opacity="0.5" ShadowDepth="6" BlurRadius="15"/>
                            </Border.Effect>
                            <ItemsPresenter/>
                        </Border>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
        </Style>

        <!-- Context Menu Item Style -->
        <Style x:Key="ModernMenuItem" TargetType="MenuItem">
            <Setter Property="Foreground" Value="#E0E0E0"/>
            <Setter Property="Padding" Value="8,5"/>
            <Setter Property="FontSize" Value="12"/>
            <Setter Property="Template">
                <Setter.Value>
                    <ControlTemplate TargetType="MenuItem">
                        <Border x:Name="Border" Background="Transparent" Padding="{TemplateBinding Padding}" CornerRadius="4" Margin="1">
                            <Grid>
                                <Grid.ColumnDefinitions>
                                    <ColumnDefinition Width="Auto"/>
                                    <ColumnDefinition Width="*"/>
                                    <ColumnDefinition Width="Auto"/>
                                </Grid.ColumnDefinitions>
                                
                                <!-- Icon -->
                                <ContentPresenter Grid.Column="0" 
                                                Content="{TemplateBinding Icon}" 
                                                Margin="0,0,8,0"
                                                VerticalAlignment="Center"/>
                                
                                <!-- Header -->
                                <ContentPresenter Grid.Column="1" 
                                                ContentSource="Header"
                                                VerticalAlignment="Center"/>
                                
                                <!-- InputGestureText (Shortcut) -->
                                <TextBlock Grid.Column="2" 
                                         Text="{TemplateBinding InputGestureText}"
                                         Foreground="#999999"
                                         Margin="12,0,0,0"
                                         VerticalAlignment="Center"
                                         FontSize="11"/>
                            </Grid>
                        </Border>
                        <ControlTemplate.Triggers>
                            <Trigger Property="IsHighlighted" Value="True">
                                <Setter TargetName="Border" Property="Background" Value="#30FFFFFF"/>
                            </Trigger>
                            <Trigger Property="IsEnabled" Value="False">
                                <Setter Property="Foreground" Value="#707070"/>
                            </Trigger>
                        </ControlTemplate.Triggers>
                    </ControlTemplate>
                </Setter.Value>
            </Setter>
        </Style>

    </Window.Resources>

    <Border Background="{StaticResource WindowBackground}" 
            CornerRadius="10" 
            BorderBrush="{StaticResource BorderBrush}" 
            BorderThickness="1">
        
        <Grid>
            <Grid.RowDefinitions>
                <RowDefinition Height="Auto"/> <!-- Header -->
                <RowDefinition Height="Auto"/> <!-- Search -->
                <RowDefinition Height="Auto"/> <!-- Cloudflare Tunnels Section -->
                <RowDefinition Height="*"/>    <!-- List -->
                <RowDefinition Height="Auto"/> <!-- Footer -->
            </Grid.RowDefinitions>

            <!-- 1. Header: Open PortKiller -->
            <Button Grid.Row="0" Click="OpenApp_Click" Style="{StaticResource MenuButtonStyle}" Padding="12,10">
                <Grid>
                    <Grid.ColumnDefinitions>
                        <ColumnDefinition Width="*"/>
                        <ColumnDefinition Width="Auto"/>
                    </Grid.ColumnDefinitions>
                    <TextBlock Text="Open PortKiller" FontSize="13" FontWeight="SemiBold"/>
                    <TextBlock Grid.Column="1" Text="Ctrl+O" FontSize="12" Foreground="{StaticResource TextSecondary}"/>
                </Grid>
            </Button>

            <Rectangle Grid.Row="0" VerticalAlignment="Bottom" Height="1" Fill="{StaticResource BorderBrush}" Opacity="0.5"/>

            <!-- 2. Search Bar and Count -->
            <Grid Grid.Row="1" Margin="12,12,12,8">
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="*"/>
                    <ColumnDefinition Width="Auto"/>
                </Grid.ColumnDefinitions>

                <!-- Search Bar -->
                <Border Grid.Column="0" Background="#20FFFFFF" CornerRadius="6" BorderBrush="#30FFFFFF" BorderThickness="1" Height="28">
                    <Grid>
                        <Grid.ColumnDefinitions>
                            <ColumnDefinition Width="Auto"/>
                            <ColumnDefinition Width="*"/>
                        </Grid.ColumnDefinitions>
                        
                        <!-- Search Icon (Globe/Network) -->
                        <TextBlock Grid.Column="0" Text="🌐" Margin="8,0,4,0" VerticalAlignment="Center" FontSize="12" Opacity="0.7"/>
                        
                        <!-- Input -->
                        <TextBox x:Name="SearchBox" Grid.Column="1" 
                                 Background="Transparent" BorderThickness="0" 
                                 Foreground="{StaticResource TextPrimary}"
                                 CaretBrush="{StaticResource TextPrimary}"
                                 VerticalContentAlignment="Center"
                                 FontSize="13"
                                 TextChanged="SearchBox_TextChanged"/>
                        
                        <!-- Placeholder -->
                        <TextBlock Grid.Column="1" Text="Search..." IsHitTestVisible="False"
                                   Foreground="{StaticResource TextSecondary}"
                                   VerticalAlignment="Center" Margin="2,0,0,0">
                            <TextBlock.Style>
                                <Style TargetType="TextBlock">
                                    <Setter Property="Visibility" Value="Collapsed"/>
                                    <Style.Triggers>
                                        <DataTrigger Binding="{Binding Text, ElementName=SearchBox}" Value="">
                                            <Setter Property="Visibility" Value="Visible"/>
                                        </DataTrigger>
                                    </Style.Triggers>
                                </Style>
                            </TextBlock.Style>
                        </TextBlock>
                    </Grid>
                </Border>

                <!-- Count Badge (Outside Search Bar) -->
                <Border Grid.Column="1" Background="#40FFFFFF" CornerRadius="9" Margin="8,0,0,0" Padding="0" Height="18" Width="30">
                    <TextBlock x:Name="PortCountText" Text="0" FontSize="11" FontWeight="Bold" VerticalAlignment="Center" HorizontalAlignment="Center" Foreground="{StaticResource TextPrimary}"/>
                </Border>
            </Grid>

            <!-- 3. Cloudflare Tunnels Section -->
            <StackPanel Grid.Row="2" x:Name="TunnelsSection" Visibility="Collapsed" Margin="0,8,0,8">
                <!-- Section Header -->
                <Grid Margin="12,0,12,8">
                    <Grid.ColumnDefinitions>
                        <ColumnDefinition Width="Auto"/>
                        <ColumnDefinition Width="*"/>
                    </Grid.ColumnDefinitions>
                    
                    <StackPanel Orientation="Horizontal" Grid.Column="0">
                        <TextBlock Text="☁" FontSize="12" Margin="0,0,6,0" VerticalAlignment="Center" Foreground="#F4AB3A"/>
                        <TextBlock Text="Cloudflare Tunnels" 
                                   FontSize="11" 
                                   FontWeight="SemiBold" 
                                   Foreground="{StaticResource TextSecondary}"
                                   VerticalAlignment="Center"/>
                    </StackPanel>
                </Grid>

                <!-- Tunnels List -->
                <ItemsControl x:Name="TunnelsList" Margin="0,0,0,0">
                    <ItemsControl.ItemTemplate>
                        <DataTemplate>
                            <Border Background="Transparent" Padding="12,6" Margin="0,0,0,2">
                                <Border.Style>
                                    <Style TargetType="Border">
                                        <Style.Triggers>
                                            <Trigger Property="IsMouseOver" Value="True">
                                                <Setter Property="Background" Value="#30FFFFFF"/>
                                            </Trigger>
                                        </Style.Triggers>
                                    </Style>
                                </Border.Style>
                                
                                <Grid>
                                    <Grid.ColumnDefinitions>
                                        <ColumnDefinition Width="Auto"/> <!-- Dot -->
                                        <ColumnDefinition Width="Auto"/> <!-- Port -->
                                        <ColumnDefinition Width="*"/>    <!-- URL -->
                                        <ColumnDefinition Width="Auto"/> <!-- Copy Button -->
                                        <ColumnDefinition Width="Auto"/> <!-- Close Button -->
                                    </Grid.ColumnDefinitions>

                                    <!-- Green Dot (Active) -->
                                    <Ellipse Grid.Column="0" 
                                             Width="6" 
                                             Height="6" 
                                             Fill="#2ecc71" 
                                             VerticalAlignment="Center" 
                                             Margin="0,2,8,0"/>

                                    <!-- Port Number -->
                                    <TextBlock Grid.Column="1" 
                                               FontWeight="Bold" 
                                               Foreground="{StaticResource TextPrimary}" 
                                               VerticalAlignment="Center" 
                                               Margin="0,0,8,0">
                                        <Run Text=":"/>
                                        <Run Text="{Binding Port}"/>
                                    </TextBlock>

                                    <!-- Shortened URL -->
                                    <TextBlock Grid.Column="2" 
                                               Text="{Binding DisplayUrl}" 
                                               Foreground="#5B9DD9"
                                               TextTrimming="CharacterEllipsis" 
                                               VerticalAlignment="Center"
                                               FontFamily="Consolas"
                                               FontSize="11"
                                               ToolTip="{Binding TunnelUrl}"/>

                                    <!-- Copy Button -->
                                    <Button Grid.Column="3" 
                                            Content="📋" 
                                            Width="24" 
                                            Height="24"
                                            FontSize="12"
                                            Margin="4,0,0,0"
                                            Background="Transparent"
                                            BorderThickness="0"
                                            Foreground="{StaticResource TextSecondary}"
                                            Cursor="Hand"
                                            Click="CopyTunnelUrl_Click"
                                            Tag="{Binding}"
                                            ToolTip="Copy URL">
                                        <Button.Style>
                                            <Style TargetType="Button">
                                                <Setter Property="Background" Value="Transparent"/>
                                                <Setter Property="Template">
                                                    <Setter.Value>
                                                        <ControlTemplate TargetType="Button">
                                                            <Border Background="{TemplateBinding Background}" 
                                                                    CornerRadius="4"
                                                                    Padding="4">
                                                                <ContentPresenter HorizontalAlignment="Center" 
                                                                                VerticalAlignment="Center"/>
                                                            </Border>
                                                        </ControlTemplate>
                                                    </Setter.Value>
                                                </Setter>
                                                <Style.Triggers>
                                                    <Trigger Property="IsMouseOver" Value="True">
                                                        <Setter Property="Background" Value="#20FFFFFF"/>
                                                    </Trigger>
                                                </Style.Triggers>
                                            </Style>
                                        </Button.Style>
                                    </Button>

                                    <!-- Close/Stop Tunnel Button -->
                                    <Button Grid.Column="4" 
                                            Width="20" 
                                            Height="20"
                                            Margin="4,0,0,0"
                                            Background="{StaticResource DangerColor}"
                                            BorderThickness="0"
                                            Cursor="Hand"
                                            Click="StopTunnel_Click"
                                            Tag="{Binding}"
                                            ToolTip="Stop Tunnel">
                                        <Button.Template>
                                            <ControlTemplate TargetType="Button">
                                                <Border Background="{TemplateBinding Background}" 
                                                        CornerRadius="10">
                                                    <TextBlock Text="✕" 
                                                               FontSize="10" 
                                                               FontWeight="Normal"
                                                               Foreground="White"
                                                               HorizontalAlignment="Center" 
                                                               VerticalAlignment="Center"
                                                               Margin="0,-1,0,0"/>
                                                </Border>
                                            </ControlTemplate>
                                        </Button.Template>
                                    </Button>
                                </Grid>
                            </Border>
                        </DataTemplate>
                    </ItemsControl.ItemTemplate>
                </ItemsControl>

                <!-- Divider after tunnels -->
                <Rectangle Height="1" Fill="{StaticResource BorderBrush}" Opacity="0.3" Margin="12,8"/>
            </StackPanel>

            <!-- 4. Port List - Updated Grid.Row -->
            <ListBox Grid.Row="3" x:Name="PortsList" 
                     Background="Transparent" 
                     BorderThickness="0"
                     Margin="0,0,0,8"
                     ScrollViewer.HorizontalScrollBarVisibility="Disabled"
                     ScrollViewer.VerticalScrollBarVisibility="Hidden"
                     ItemContainerStyle="{StaticResource PortListBoxItemStyle}">
                <ListBox.ItemTemplate>
                    <DataTemplate DataType="{x:Type models:PortInfo}">
                        <Grid x:Name="ItemGrid">
                            <Grid.ContextMenu>
                                <ContextMenu Style="{StaticResource ModernContextMenu}" Opened="ContextMenu_Opened">
                                     <!-- Add to Favorites -->
                                    <MenuItem x:Name="FavoriteMenuItem"
                                              Header="Add to Favorites" 
                                              Style="{StaticResource ModernMenuItem}"
                                              Click="ContextMenu_AddToFavorites"
                                              Tag="{Binding}">
                                        <MenuItem.Icon>
                                            <TextBlock Text="⭐" FontSize="14" Margin="0"/>
                                        </MenuItem.Icon>
                                    </MenuItem>

                                    <!-- Watch Port -->
                                    <MenuItem x:Name="WatchMenuItem"
                                              Header="Watch Port" 
                                              Style="{StaticResource ModernMenuItem}"
                                              Click="ContextMenu_WatchPort"
                                              Tag="{Binding}">
                                        <MenuItem.Icon>
                                            <TextBlock Text="👁" FontSize="14" Margin="0"/>
                                        </MenuItem.Icon>
                                    </MenuItem>

                                    <!-- Separator -->
                                    <Separator Background="#40FFFFFF" Margin="2,2"/>

                                    <!-- Open in Browser -->
                                    <MenuItem Header="Open in Browser" 
                                              Style="{StaticResource ModernMenuItem}"
                                              Click="ContextMenu_OpenInBrowser"
                                              Tag="{Binding}"
                                              InputGestureText="⌘ O">
                                        <MenuItem.Icon>
                                            <TextBlock Text="🌐" FontSize="14" Margin="0"/>
                                        </MenuItem.Icon>
                                    </MenuItem>

                                    <!-- Copy URL -->
                                    <MenuItem Header="Copy URL" 
                                              Style="{StaticResource ModernMenuItem}"
                                              Click="ContextMenu_CopyUrl"
                                              Tag="{Binding}">
                                        <MenuItem.Icon>
                                            <TextBlock Text="📋" FontSize="14" Margin="0"/>
                                        </MenuItem.Icon>
                                    </MenuItem>

                                     <!-- Separator -->
                                    <Separator Background="#40FFFFFF" Margin="2,2"/>

                                    <!-- Share via Tunnel -->
                                    <MenuItem Header="Share via Tunnel" 
                                              Style="{StaticResource ModernMenuItem}"
                                              Click="ContextMenu_ShareViaTunnel"
                                              Tag="{Binding}">
                                        <MenuItem.Icon>
                                            <TextBlock Text="☁" FontSize="14" Margin="0" Foreground="#F4AB3A"/>
                                        </MenuItem.Icon>
                                    </MenuItem>
                                </ContextMenu>
                            </Grid.ContextMenu>

                            <Grid.ColumnDefinitions>
                                <ColumnDefinition Width="Auto"/> <!-- Dot -->
                                <ColumnDefinition Width="Auto"/> <!-- Port -->
                                <ColumnDefinition Width="*"/>    <!-- Process -->
                                <ColumnDefinition Width="Auto"/> <!-- PID or Action -->
                            </Grid.ColumnDefinitions>

                            <!-- Green Dot -->
                            <Ellipse x:Name="StatusDot" Grid.Column="0" Width="6" Height="6" Fill="#2ecc71" VerticalAlignment="Center" Margin="0,2,8,0"/>

                            <!-- Port Number -->
                            <TextBlock x:Name="PortText" Grid.Column="1" Text="{Binding DisplayPort}" FontWeight="Bold" Foreground="{StaticResource TextPrimary}" VerticalAlignment="Center" Margin="0,0,8,0"/>

                            <!-- Process Name -->
                            <TextBlock x:Name="ProcessText" Grid.Column="2" Text="{Binding ProcessName}" Foreground="{StaticResource TextSecondary}" TextTrimming="CharacterEllipsis" VerticalAlignment="Center"/>

                            <!-- PID (Default Visible) -->
                            <TextBlock x:Name="PidText" Grid.Column="3" Text="{Binding Pid}" Foreground="{StaticResource TextTertiary}" FontSize="12" VerticalAlignment="Center"/>

                            <!-- Processing State (Kill - Spinner) -->
                            <TextBlock x:Name="ProcessingText" Grid.Column="3" Text="⌛" FontSize="14" Foreground="#F4AB3A" Visibility="Collapsed" VerticalAlignment="Center"/>

                            <!-- Tunnel Processing State (Cloud with animation) -->
                            <StackPanel x:Name="TunnelProcessingPanel" Grid.Column="3" Orientation="Horizontal" Visibility="Collapsed" VerticalAlignment="Center">
                                <TextBlock Text="☁" FontSize="14" Foreground="#F4AB3A" VerticalAlignment="Center">
                                    <TextBlock.Style>
                                        <Style TargetType="TextBlock">
                                            <Style.Triggers>
                                                <EventTrigger RoutedEvent="Loaded">
                                                    <BeginStoryboard>
                                                        <Storyboard RepeatBehavior="Forever">
                                                            <DoubleAnimation Storyboard.TargetProperty="Opacity"
                                                                           From="1" To="0.3" Duration="0:0:0.5"
                                                                           AutoReverse="True"/>
                                                        </Storyboard>
                                                    </BeginStoryboard>
                                                </EventTrigger>
                                            </Style.Triggers>
                                        </Style>
                                    </TextBlock.Style>
                                </TextBlock>
                                <TextBlock Text=" Sharing..." FontSize="11" Foreground="#F4AB3A" VerticalAlignment="Center"/>
                            </StackPanel>

                            <!-- Kill Button (Hidden by default, shown on hover) -->
                            <Button x:Name="KillButton" Grid.Column="3" 
                                    Visibility="Hidden"
                                    Width="20" Height="20"
                                    Background="{StaticResource DangerColor}"
                                    BorderThickness="0"
                                    Cursor="Hand"
                                    PreviewMouseLeftButtonDown="KillSinglePort_Click"
                                    Tag="{Binding}">
                                <Button.Template>
                                    <ControlTemplate TargetType="Button">
                                        <Border Background="{TemplateBinding Background}" CornerRadius="10">
                                            <TextBlock Text="✕" 
                                                       FontSize="10" 
                                                       FontWeight="Normal"
                                                       Foreground="White"
                                                       HorizontalAlignment="Center" 
                                                       VerticalAlignment="Center"
                                                       Margin="0,-1,0,0"/>
                                        </Border>
                                    </ControlTemplate>
                                </Button.Template>
                            </Button>

                            <!-- Inline Confirmation (Overlay) -->
                            <Border Grid.Column="0" Grid.ColumnSpan="4" x:Name="ConfirmOverlay" Background="Transparent" Visibility="Collapsed">
                                <Grid>
                                    <Grid.ColumnDefinitions>
                                        <ColumnDefinition Width="Auto"/>
                                        <ColumnDefinition Width="*"/>
                                        <ColumnDefinition Width="Auto"/>
                                    </Grid.ColumnDefinitions>

                                    <StackPanel Grid.Column="0" Orientation="Horizontal" VerticalAlignment="Center" Margin="0,0" IsHitTestVisible="False">
                                        <Ellipse Width="6" Height="6" Fill="#2ecc71" VerticalAlignment="Center" Margin="0,0,8,0"/>
                                        <TextBlock Text="Kill " Foreground="{StaticResource TextPrimary}" FontWeight="SemiBold"/>
                                        <TextBlock Text="{Binding ProcessName}" Foreground="{StaticResource TextPrimary}" FontWeight="SemiBold"/>
                                        <TextBlock Text="?" Foreground="{StaticResource TextPrimary}" FontWeight="SemiBold"/>
                                    </StackPanel>

                                    <StackPanel Grid.Column="2" Orientation="Horizontal" VerticalAlignment="Center">
                                        <Button Content="Kill" 
                                                Click="ConfirmKill_Click" 
                                                Tag="{Binding}"
                                                Background="{StaticResource DangerColor}"
                                                Foreground="White"
                                                BorderThickness="0"
                                                Padding="12,5"
                                                Margin="0,0,8,0"
                                                Cursor="Hand">
                                            <Button.Template>
                                                <ControlTemplate TargetType="Button">
                                                    <Border Background="{TemplateBinding Background}" CornerRadius="4" Padding="{TemplateBinding Padding}">
                                                        <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
                                                    </Border>
                                                </ControlTemplate>
                                            </Button.Template>
                                        </Button>
                                        
                                        <Button Content="Cancel" 
                                                Click="CancelKill_Click" 
                                                Tag="{Binding}"
                                                Background="#3A3A3A"
                                                Foreground="{StaticResource TextPrimary}"
                                                BorderThickness="0"
                                                Padding="12,5"
                                                Cursor="Hand">
                                            <Button.Template>
                                                <ControlTemplate TargetType="Button">
                                                    <Border Background="{TemplateBinding Background}" CornerRadius="4" Padding="{TemplateBinding Padding}">
                                                        <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
                                                    </Border>
                                                </ControlTemplate>
                                            </Button.Template>
                                        </Button>
                                    </StackPanel>
                                </Grid>
                            </Border>
                        </Grid>
                        
                        <DataTemplate.Triggers>
                            <!-- Show Kill Button on Hover -->
                            <MultiDataTrigger>
                                <MultiDataTrigger.Conditions>
                                    <Condition Binding="{Binding IsMouseOver, RelativeSource={RelativeSource AncestorType=ListBoxItem}}" Value="True"/>
                                    <Condition Binding="{Binding IsConfirmingKill}" Value="False"/>
                                    <Condition Binding="{Binding IsKilling}" Value="False"/>
                                </MultiDataTrigger.Conditions>
                                <Setter TargetName="PidText" Property="Visibility" Value="Hidden"/>
                                <Setter TargetName="KillButton" Property="Visibility" Value="Visible"/>
                            </MultiDataTrigger>

                            <!-- Show Confirmation Overlay and Hide Content -->
                            <DataTrigger Binding="{Binding IsConfirmingKill}" Value="True">
                                <Setter TargetName="ConfirmOverlay" Property="Visibility" Value="Visible"/>
                                <Setter TargetName="StatusDot" Property="Visibility" Value="Collapsed"/>
                                <Setter TargetName="PortText" Property="Visibility" Value="Collapsed"/>
                                <Setter TargetName="ProcessText" Property="Visibility" Value="Collapsed"/>
                                <Setter TargetName="PidText" Property="Visibility" Value="Collapsed"/>
                                <Setter TargetName="KillButton" Property="Visibility" Value="Collapsed"/>
                            </DataTrigger>

                            <!-- Show Killing State -->
                            <DataTrigger Binding="{Binding IsKilling}" Value="True">
                                <Setter TargetName="PidText" Property="Visibility" Value="Collapsed"/>
                                <Setter TargetName="KillButton" Property="Visibility" Value="Collapsed"/>
                                <Setter TargetName="ProcessingText" Property="Visibility" Value="Visible"/>
                                <Setter TargetName="ConfirmOverlay" Property="Visibility" Value="Collapsed"/>
                            </DataTrigger>
                        </DataTemplate.Triggers>
                    </DataTemplate>
                </ListBox.ItemTemplate>
            </ListBox>

            <!-- Empty State Overlay -->
            <TextBlock Grid.Row="3" x:Name="EmptyStateText" Text="No active ports" 
                       HorizontalAlignment="Center" VerticalAlignment="Center" 
                       Foreground="{StaticResource TextSecondary}"
                       Visibility="Collapsed"/>

            <!-- 5. Footer Menu - Updated Grid.Row -->
            <StackPanel Grid.Row="4" Margin="0,4,0,0">
                <Rectangle Height="1" Fill="{StaticResource BorderBrush}" Opacity="0.5"/>
                
                <!-- Refresh Status Indicator (Raycast-style) -->
                <Button x:Name="RefreshButton" Click="RefreshButton_Click" Style="{StaticResource MenuButtonStyle}" Margin="0,2,0,0">
                    <Grid>
                        <Grid.ColumnDefinitions>
                            <ColumnDefinition Width="Auto"/>
                            <ColumnDefinition Width="*"/>
                            <ColumnDefinition Width="Auto"/>
                        </Grid.ColumnDefinitions>
                        
                        <!-- Status Indicator Container -->
                        <Grid Grid.Column="0" Width="16" Height="16" Margin="0,0,8,0">
                            <!-- Idle State: Refresh Icon -->
                            <TextBlock x:Name="RefreshIcon" Text="↻" FontSize="14" 
                                       VerticalAlignment="Center" HorizontalAlignment="Center"
                                       Visibility="Visible"/>
                            
                            <!-- Loading State: Spinning Circle -->
                            <Border x:Name="LoadingSpinner" Visibility="Collapsed"
                                    Width="14" Height="14" 
                                    CornerRadius="7"
                                    BorderThickness="2"
                                    BorderBrush="#60FFFFFF"
                                    RenderTransformOrigin="0.5,0.5">
                                <Border.RenderTransform>
                                    <RotateTransform x:Name="SpinnerRotation" Angle="0"/>
                                </Border.RenderTransform>
                                <!-- Accent arc for spinner effect -->
                                <Border Width="14" Height="14" CornerRadius="7" 
                                        BorderThickness="2,2,0,0" 
                                        BorderBrush="{StaticResource AccentColor}"
                                        Margin="-2"/>
                            </Border>
                            
                            <!-- Success State: Green Dot -->
                            <Ellipse x:Name="SuccessDot" Visibility="Collapsed"
                                     Width="8" Height="8" 
                                     Fill="#2ecc71"
                                     VerticalAlignment="Center" HorizontalAlignment="Center"/>
                        </Grid>
                        
                        <!-- Status Text -->
                        <TextBlock x:Name="RefreshStatusText" Grid.Column="1" 
                                   Text="Refresh" 
                                   VerticalAlignment="Center"/>
                        
                        <!-- Keyboard Shortcut -->
                        <TextBlock Grid.Column="2" Text="Ctrl+R" FontSize="12" 
                                   Foreground="{StaticResource TextSecondary}"/>
                    </Grid>
                </Button>

                <!-- Kill All -->
                <Button Click="KillAll_Click" Style="{StaticResource MenuButtonStyle}" Margin="0,2,0,0">
                    <Grid>
                        <Grid.ColumnDefinitions>
                            <ColumnDefinition Width="24"/>
                            <ColumnDefinition Width="*"/>
                            <ColumnDefinition Width="Auto"/>
                        </Grid.ColumnDefinitions>
                        <TextBlock Text="⚡" FontSize="12" Foreground="{StaticResource DangerColor}" VerticalAlignment="Center" HorizontalAlignment="Center"/>
                        <TextBlock Grid.Column="1" Text="Kill All Processes" Foreground="{StaticResource DangerColor}" VerticalAlignment="Center" Margin="4,0,0,0"/>
                        <TextBlock Grid.Column="2" Text="Ctrl+K" FontSize="12" Foreground="{StaticResource TextSecondary}"/>
                    </Grid>
                </Button>

                <Rectangle Height="1" Fill="{StaticResource BorderBrush}" Opacity="0.3" Margin="12,4"/>

                <!-- Quit -->
                <Button Click="Quit_Click" Style="{StaticResource MenuButtonStyle}" Margin="0,0,0,4">
                    <Grid>
                        <Grid.ColumnDefinitions>
                            <ColumnDefinition Width="24"/>
                            <ColumnDefinition Width="*"/>
                            <ColumnDefinition Width="Auto"/>
                        </Grid.ColumnDefinitions>
                        <TextBlock Text="✕" FontSize="12" VerticalAlignment="Center" HorizontalAlignment="Center"/>
                        <TextBlock Grid.Column="1" Text="Quit PortKiller" VerticalAlignment="Center" Margin="4,0,0,0"/>
                        <TextBlock Grid.Column="2" Text="Ctrl+Q" FontSize="12" Foreground="{StaticResource TextSecondary}"/>
                    </Grid>
                </Button>
            </StackPanel>
        </Grid>
    </Border>
</Window>
```

## File: `platforms/windows/PortKiller/MiniPortKillerWindow.xaml.cs`
```csharp
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using Microsoft.Extensions.DependencyInjection;
using PortKiller.Models;
using PortKiller.ViewModels;
using PortKiller.Services;

namespace PortKiller;

public partial class MiniPortKillerWindow : Window
{
    private readonly MainViewModel _viewModel;
    private readonly TunnelViewModel _tunnelViewModel;
    private bool _isProcessingAction = false;
    private System.Windows.Threading.DispatcherTimer? _tunnelUpdateTimer;
    private System.Windows.Threading.DispatcherTimer? _spinnerTimer;
    private System.Windows.Threading.DispatcherTimer? _successTimer;
    private double _spinnerAngle = 0;
    private bool _isManualRefresh = false; // Track manual refresh vs auto-refresh
    private bool _isClosing = false; // Track if window is closing to prevent UI updates

    public MiniPortKillerWindow()
    {
        InitializeComponent();
        
        _viewModel = App.Services.GetRequiredService<MainViewModel>();
        _tunnelViewModel = App.Services.GetRequiredService<TunnelViewModel>();
        
        System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Constructor - TunnelViewModel has {_tunnelViewModel.Tunnels.Count} tunnels");
        
        // Subscribe to the Ports collection changes directly
        _viewModel.Ports.CollectionChanged += (s, e) =>
        {
            Dispatcher.Invoke(UpdatePortList);
        };

        // Also subscribe to scanning state changes to update immediately
        _viewModel.PropertyChanged += (s, e) =>
        {
            if (e.PropertyName == nameof(_viewModel.IsScanning))
            {
                Dispatcher.Invoke(() =>
                {
                    // Only show refresh UI state for manual refresh, not auto-refresh
                    if (_isManualRefresh)
                    {
                        if (_viewModel.IsScanning)
                        {
                            ShowRefreshingState();
                        }
                        else
                        {
                            ShowRefreshedState();
                            _isManualRefresh = false; // Reset flag after manual refresh completes
                        }
                    }
                    
                    // Always update port list when scanning completes
                    if (!_viewModel.IsScanning)
                    {
                        UpdatePortList();
                    }
                });
            }
        };

        // Subscribe to tunnel changes
        _tunnelViewModel.Tunnels.CollectionChanged += (s, e) =>
        {
            System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Tunnels.CollectionChanged event fired - Action: {e.Action}");
            Dispatcher.Invoke(UpdateTunnelsList);
        };

        // Set up timer to periodically check for active tunnels
        _tunnelUpdateTimer = new System.Windows.Threading.DispatcherTimer
        {
            Interval = TimeSpan.FromSeconds(2)
        };
        _tunnelUpdateTimer.Tick += (s, e) => UpdateTunnelsList();
        _tunnelUpdateTimer.Start();

        // Initial refresh when window opens
        Loaded += async (s, e) => 
        {
            await _viewModel.RefreshPortsCommand.ExecuteAsync(null);
            UpdatePortList();
            UpdateTunnelsList();
        };
        
        UpdatePortList();
        UpdateTunnelsList();
    }

    private void UpdatePortList()
    {
        // Don't update UI if window is closing
        if (_isClosing) return;
        
        // Safety check if controls aren't initialized yet
        if (SearchBox == null || PortsList == null || PortCountText == null || EmptyStateText == null) return;

        var searchText = SearchBox.Text?.ToLower() ?? "";
        
        // Get fresh data from ViewModel - convert to list to avoid collection modification issues
        var allPorts = _viewModel.Ports.ToList();
        
        System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] UpdatePortList called - Total ports: {allPorts.Count}, Thread: {System.Threading.Thread.CurrentThread.ManagedThreadId}");
        
        var filteredPorts = allPorts
            .Where(p => string.IsNullOrEmpty(searchText) || 
                        p.DisplayPort.Contains(searchText) || 
                        (p.ProcessName != null && p.ProcessName.ToLower().Contains(searchText)) ||
                        p.Pid.ToString().Contains(searchText))
            .OrderBy(p => p.Port)
            .Take(15) // Limit for mini view
            .ToList();
        
        System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Filtered ports to display: {filteredPorts.Count}");
        
        // Update ItemsSource - WPF will handle the diff automatically
        PortsList.ItemsSource = filteredPorts;
        PortCountText.Text = allPorts.Count.ToString(); // Show total count, not filtered
        
        EmptyStateText.Visibility = filteredPorts.Any() ? Visibility.Collapsed : Visibility.Visible;
    }

    private void UpdateTunnelsList()
    {
        // Don't update UI if window is closing
        if (_isClosing) return;
        
        // Safety check if controls aren't initialized yet
        var tunnelsList = this.FindName("TunnelsList") as ItemsControl;
        var tunnelsSection = this.FindName("TunnelsSection") as StackPanel;
        
        if (tunnelsList == null || tunnelsSection == null)
        {
            System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] UpdateTunnelsList - Controls not found. TunnelsList: {(tunnelsList != null)}, TunnelsSection: {(tunnelsSection != null)}");
            return;
        }

        // Get active tunnels
        var activeTunnels = _tunnelViewModel.Tunnels
            .Where(t => t.Status == TunnelStatus.Active)
            .OrderBy(t => t.Port)
            .ToList();
        
        System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] UpdateTunnelsList called - Active tunnels: {activeTunnels.Count}");
        
        // Update ItemsSource
        tunnelsList.ItemsSource = activeTunnels;
        
        // Show/hide tunnels section based on whether there are active tunnels
        tunnelsSection.Visibility = activeTunnels.Any() ? Visibility.Visible : Visibility.Collapsed;
        
        System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] TunnelsSection visibility set to: {tunnelsSection.Visibility}");
    }

    private void SearchBox_TextChanged(object sender, TextChangedEventArgs e)
    {
        UpdatePortList();
    }

    private void KillSinglePort_Click(object sender, MouseButtonEventArgs e)
    {
        if (sender is Button btn && btn.Tag is PortInfo port)
        {
            // Stop event propagation
            e.Handled = true;
            port.IsConfirmingKill = true;
        }
    }

    private async void ConfirmKill_Click(object sender, RoutedEventArgs e)
    {
        if (sender is Button btn && btn.Tag is PortInfo port)
        {
            port.IsConfirmingKill = false;
            port.IsKilling = true;

            try
            {
                await _viewModel.KillProcessCommand.ExecuteAsync(port);
            }
            finally
            {
                // The port will be removed from the list by the ViewModel refresh
                // If it fails, we should reset the state
                if (_viewModel.Ports.Contains(port))
                {
                    port.IsKilling = false;
                }
            }
        }
    }

    private void CancelKill_Click(object sender, RoutedEventArgs e)
    {
        if (sender is Button btn && btn.Tag is PortInfo port)
        {
            port.IsConfirmingKill = false;
        }
    }

    private async void KillAll_Click(object sender, RoutedEventArgs e)
    {
        _isProcessingAction = true;
        
        try
        {
            if (!_viewModel.Ports.Any()) return;

            var dialog = new ConfirmDialog(
                $"Kill ALL {_viewModel.Ports.Count} active processes?",
                "This will terminate all processes currently using ports.")
            {
                Owner = this
            };
            
            dialog.ShowDialog();

            if (dialog.Result)
            {
                // Create a copy of the list to avoid collection modification errors
                var portsToKill = _viewModel.Ports.ToList();
                foreach (var port in portsToKill)
                {
                    await _viewModel.KillProcessCommand.ExecuteAsync(port);
                }
                
                // The auto-refresh in MainViewModel will update the UI automatically
                // via the CollectionChanged event subscription
            }
        }
        finally
        {
            _isProcessingAction = false;
        }
    }

    private async void RefreshButton_Click(object sender, RoutedEventArgs e)
    {
        System.Diagnostics.Debug.WriteLine("[MiniPortKiller] Refresh button clicked");
        _isManualRefresh = true; // Set flag to show refresh UI state
        await _viewModel.RefreshPortsCommand.ExecuteAsync(null);
        System.Diagnostics.Debug.WriteLine("[MiniPortKiller] Refresh command executed");
    }

    private void OpenApp_Click(object sender, RoutedEventArgs e)
    {
        Application.Current.MainWindow?.Show();
        Application.Current.MainWindow!.WindowState = WindowState.Normal;
        Application.Current.MainWindow?.Activate();
        Close();
    }

    private void Quit_Click(object sender, RoutedEventArgs e)
    {
        _isClosing = true;
        Application.Current.Shutdown();
    }

    private void Window_Deactivated(object sender, EventArgs e)
    {
        // Don't close if already closing
        if (_isClosing)
            return;
            
        // Don't close if we're showing a MessageBox or processing an action
        if (_isProcessingAction)
            return;
            
        // Close when clicking outside, behaving like a popup menu
        Close();
    }

    protected override void OnClosing(System.ComponentModel.CancelEventArgs e)
    {
        // Set closing flag to prevent UI updates
        _isClosing = true;
        
        // Stop and cleanup all timers
        try
        {
            _tunnelUpdateTimer?.Stop();
            _tunnelUpdateTimer = null;
            
            _spinnerTimer?.Stop();
            _spinnerTimer = null;
            
            _successTimer?.Stop();
            _successTimer = null;
        }
        catch (Exception ex)
        {
            System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Error cleaning up timers: {ex.Message}");
        }
        
        base.OnClosing(e);
    }

    public void ShowNearTray()
    {
        // Position near system tray (bottom-right)
        var workArea = SystemParameters.WorkArea;
        Left = workArea.Right - Width - 10;
        Top = workArea.Bottom - Height - 10;
        
        // Reset search
        if (SearchBox != null)
        {
            SearchBox.Text = "";
            SearchBox.Focus();
        }
        
        // Update the port list with current data
        UpdatePortList();
        
        Show();
        Activate();
        Focus();
    }

    private void CopyTunnelUrl_Click(object sender, RoutedEventArgs e)
    {
        if (sender is Button btn && btn.Tag is CloudflareTunnel tunnel)
        {
            if (!string.IsNullOrEmpty(tunnel.TunnelUrl))
            {
                try
                {
                    Clipboard.SetText(tunnel.TunnelUrl);
                    System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Copied tunnel URL: {tunnel.TunnelUrl}");
                }
                catch (Exception ex)
                {
                    System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Failed to copy URL: {ex.Message}");
                }
            }
        }
    }

    private async void StopTunnel_Click(object sender, RoutedEventArgs e)
    {
        if (sender is Button btn && btn.Tag is CloudflareTunnel tunnel)
        {
            _isProcessingAction = true;
            try
            {
                System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Stopping tunnel on port {tunnel.Port}");
                await _tunnelViewModel.StopTunnelAsync(tunnel);
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Failed to stop tunnel: {ex.Message}");
            }
            finally
            {
                _isProcessingAction = false;
            }
        }
    }

    // Refresh Status State Management (Raycast-style)
    private void ShowRefreshingState()
    {
        // Don't update UI if window is closing
        if (_isClosing) return;
        
        var refreshIcon = this.FindName("RefreshIcon") as System.Windows.Controls.TextBlock;
        var loadingSpinner = this.FindName("LoadingSpinner") as System.Windows.Controls.Border;
        var successDot = this.FindName("SuccessDot") as System.Windows.Shapes.Ellipse;
        var refreshStatusText = this.FindName("RefreshStatusText") as System.Windows.Controls.TextBlock;
        
        if (refreshIcon == null || loadingSpinner == null || successDot == null || refreshStatusText == null)
            return;

        // Stop any existing success timer
        _successTimer?.Stop();
        
        // Hide idle and success states
        refreshIcon.Visibility = Visibility.Collapsed;
        successDot.Visibility = Visibility.Collapsed;
        
        // Show loading spinner
        loadingSpinner.Visibility = Visibility.Visible;
        refreshStatusText.Text = "Refreshing...";
        
        // Start spinner animation
        StartSpinnerAnimation();
    }

    private void ShowRefreshedState()
    {
        // Don't update UI if window is closing
        if (_isClosing) return;
        
        var refreshIcon = this.FindName("RefreshIcon") as System.Windows.Controls.TextBlock;
        var loadingSpinner = this.FindName("LoadingSpinner") as System.Windows.Controls.Border;
        var successDot = this.FindName("SuccessDot") as System.Windows.Shapes.Ellipse;
        var refreshStatusText = this.FindName("RefreshStatusText") as System.Windows.Controls.TextBlock;
        
        if (refreshIcon == null || loadingSpinner == null || successDot == null || refreshStatusText == null)
            return;

        // Stop spinner animation
        StopSpinnerAnimation();
        
        // Hide loading spinner and idle state
        loadingSpinner.Visibility = Visibility.Collapsed;
        refreshIcon.Visibility = Visibility.Collapsed;
        
        // Show success state
        successDot.Visibility = Visibility.Visible;
        refreshStatusText.Text = "Refreshed";
        
        // Reset to idle state after 2 seconds
        _successTimer = new System.Windows.Threading.DispatcherTimer
        {
            Interval = TimeSpan.FromSeconds(2)
        };
        _successTimer.Tick += (s, e) =>
        {
            _successTimer?.Stop();
            ShowIdleState();
        };
        _successTimer.Start();
    }

    private void ShowIdleState()
    {
        // Don't update UI if window is closing
        if (_isClosing) return;
        
        var refreshIcon = this.FindName("RefreshIcon") as System.Windows.Controls.TextBlock;
        var loadingSpinner = this.FindName("LoadingSpinner") as System.Windows.Controls.Border;
        var successDot = this.FindName("SuccessDot") as System.Windows.Shapes.Ellipse;
        var refreshStatusText = this.FindName("RefreshStatusText") as System.Windows.Controls.TextBlock;
        
        if (refreshIcon == null || loadingSpinner == null || successDot == null || refreshStatusText == null)
            return;

        // Hide loading and success states
        loadingSpinner.Visibility = Visibility.Collapsed;
        successDot.Visibility = Visibility.Collapsed;
        
        // Show idle state
        refreshIcon.Visibility = Visibility.Visible;
        refreshStatusText.Text = "Refresh";
    }

    private void StartSpinnerAnimation()
    {
        var loadingSpinner = this.FindName("LoadingSpinner") as System.Windows.Controls.Border;
        
        _spinnerAngle = 0;
        _spinnerTimer = new System.Windows.Threading.DispatcherTimer
        {
            Interval = TimeSpan.FromMilliseconds(16) // ~60fps
        };
        _spinnerTimer.Tick += (s, e) =>
        {
            _spinnerAngle = (_spinnerAngle + 6) % 360;
            if (loadingSpinner?.RenderTransform is System.Windows.Media.RotateTransform rotation)
            {
                rotation.Angle = _spinnerAngle;
            }
        };
        _spinnerTimer.Start();
    }

    private void StopSpinnerAnimation()
    {
        _spinnerTimer?.Stop();
        _spinnerTimer = null;
    }

    // Context Menu Handlers
    private void ContextMenu_Opened(object sender, RoutedEventArgs e)
    {
        if (sender is ContextMenu contextMenu && contextMenu.PlacementTarget is Grid grid && grid.DataContext is PortInfo port)
        {
            // Update "Add to Favorites" / "Remove from Favorites"
            var favoriteMenuItem = contextMenu.Items.OfType<MenuItem>().FirstOrDefault(m => m.Name == "FavoriteMenuItem");
            if (favoriteMenuItem != null)
            {
                bool isFavorite = _viewModel.IsFavorite(port.Port);
                favoriteMenuItem.Header = isFavorite ? "Remove from Favorites" : "Add to Favorites";
            }

            // Update "Watch Port" / "Unwatch Port"
            var watchMenuItem = contextMenu.Items.OfType<MenuItem>().FirstOrDefault(m => m.Name == "WatchMenuItem");
            if (watchMenuItem != null)
            {
                bool isWatched = _viewModel.WatchedPorts.Any(w => w.Port == port.Port);
                watchMenuItem.Header = isWatched ? "Unwatch Port" : "Watch Port";
            }
        }
    }

    private void ContextMenu_AddToFavorites(object sender, RoutedEventArgs e)
    {
        if (sender is MenuItem menuItem && menuItem.Tag is PortInfo port)
        {
            _isProcessingAction = true;
            try
            {
                _viewModel.ToggleFavorite(port.Port);
                System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Toggled favorite for port {port.Port}");
            }
            finally
            {
                _isProcessingAction = false;
            }
        }
    }

    private void ContextMenu_WatchPort(object sender, RoutedEventArgs e)
    {
        if (sender is MenuItem menuItem && menuItem.Tag is PortInfo port)
        {
            _isProcessingAction = true;
            try
            {
                if (_viewModel.WatchedPorts.Any(w => w.Port == port.Port))
                {
                    _viewModel.RemoveWatchedPort(port.Port);
                    System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Removed watch for port {port.Port}");
                }
                else
                {
                    _viewModel.AddWatchedPort(port.Port);
                    System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Added watch for port {port.Port}");
                }
            }
            finally
            {
                _isProcessingAction = false;
            }
        }
    }

    private void ContextMenu_OpenInBrowser(object sender, RoutedEventArgs e)
    {
        if (sender is MenuItem menuItem && menuItem.Tag is PortInfo port)
        {
            _isProcessingAction = true;
            try
            {
                var url = $"http://localhost:{port.Port}";
                System.Diagnostics.Process.Start(new System.Diagnostics.ProcessStartInfo
                {
                    FileName = url,
                    UseShellExecute = true
                });
                System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Opened browser for port {port.Port}");
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Failed to open browser: {ex.Message}");
                MessageBox.Show($"Failed to open browser: {ex.Message}", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
            }
            finally
            {
                _isProcessingAction = false;
            }
        }
    }

    private void ContextMenu_CopyUrl(object sender, RoutedEventArgs e)
    {
        if (sender is MenuItem menuItem && menuItem.Tag is PortInfo port)
        {
            _isProcessingAction = true;
            try
            {
                var url = $"http://localhost:{port.Port}";
                Clipboard.SetText(url);
                System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Copied URL for port {port.Port}: {url}");
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Failed to copy URL: {ex.Message}");
            }
            finally
            {
                _isProcessingAction = false;
            }
        }
    }

    private async void ContextMenu_ShareViaTunnel(object sender, RoutedEventArgs e)
    {
        if (sender is MenuItem menuItem && menuItem.Tag is PortInfo port)
        {
            _isProcessingAction = true;
            
            // Find the row and show tunnel processing state
            StackPanel? tunnelProcessingPanel = null;
            TextBlock? pidText = null;
            Button? killButton = null;
            
            // Navigate up from MenuItem to find the parent Grid (port row)
            if (menuItem.Parent is ContextMenu contextMenu && 
                contextMenu.PlacementTarget is Grid portRowGrid)
            {
                // Find elements in the row
                tunnelProcessingPanel = FindChildByName<StackPanel>(portRowGrid, "TunnelProcessingPanel");
                pidText = FindChildByName<TextBlock>(portRowGrid, "PidText");
                killButton = FindChildByName<Button>(portRowGrid, "KillButton");
                
                // Show tunnel processing state and hide other elements
                if (tunnelProcessingPanel != null)
                {
                    tunnelProcessingPanel.Visibility = Visibility.Visible;
                }
                if (pidText != null)
                {
                    pidText.Visibility = Visibility.Collapsed;
                }
                if (killButton != null)
                {
                    killButton.Visibility = Visibility.Collapsed;
                }
            }
            
            try
            {
                System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Starting tunnel for port {port.Port}");
                await _tunnelViewModel.StartTunnelAsync(port.Port);
                System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Tunnel started for port {port.Port}");
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"[MiniPortKiller] Failed to start tunnel: {ex.Message}");
                MessageBox.Show($"Failed to start tunnel: {ex.Message}", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
            }
            finally
            {
                // Hide tunnel processing state and restore elements
                if (tunnelProcessingPanel != null)
                {
                    tunnelProcessingPanel.Visibility = Visibility.Collapsed;
                }
                if (pidText != null)
                {
                    pidText.Visibility = Visibility.Visible;
                }
                if (killButton != null)
                {
                    killButton.Visibility = Visibility.Hidden;
                }
                _isProcessingAction = false;
            }
        }
    }

    // Helper method to find a child element by name in a visual tree
    private static T? FindChildByName<T>(DependencyObject parent, string name) where T : FrameworkElement
    {
        int childCount = System.Windows.Media.VisualTreeHelper.GetChildrenCount(parent);
        for (int i = 0; i < childCount; i++)
        {
            var child = System.Windows.Media.VisualTreeHelper.GetChild(parent, i);
            
            if (child is T typedChild && typedChild.Name == name)
            {
                return typedChild;
            }
            
            var result = FindChildByName<T>(child, name);
            if (result != null)
            {
                return result;
            }
        }
        return null;
    }
}
```

## File: `platforms/windows/PortKiller/PortKiller.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <RuntimeIdentifiers>win-x64;win-arm64</RuntimeIdentifiers>
    <UseWPF>true</UseWPF>
    <RootNamespace>PortKiller</RootNamespace>
    <ApplicationManifest>app.manifest</ApplicationManifest>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <Version>1.0.0</Version>
    <Authors>PortKiller</Authors>
    <Product>PortKiller</Product>
    <Description>A native Windows app for finding and killing processes on open ports</Description>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="CommunityToolkit.Mvvm" Version="8.2.2" />
    <PackageReference Include="System.Management" Version="8.0.0" />
    <PackageReference Include="Hardcodet.NotifyIcon.Wpf" Version="1.1.0" />
    <PackageReference Include="Microsoft.Extensions.DependencyInjection" Version="8.0.0" />
    <PackageReference Include="Microsoft.Xaml.Behaviors.Wpf" Version="1.1.122" />
  </ItemGroup>

  <ItemGroup>
    <None Update="appsettings.json">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
  </ItemGroup>
</Project>
```

## File: `platforms/windows/PortKiller/Helpers/ValueConverters.cs`
```csharp
using System.Globalization;
using System.Windows;
using System.Windows.Data;
using System.Windows.Media;

namespace PortKiller.Helpers;

/// <summary>
/// Converts boolean to color (for active status)
/// </summary>
public class BoolToColorConverter : IValueConverter
{
    public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
    {
        if (value is bool isActive && isActive)
            return new SolidColorBrush((Color)ColorConverter.ConvertFromString("#3498db"));
        
        return new SolidColorBrush((Color)ColorConverter.ConvertFromString("#A0A0A0"));
    }

    public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
    {
        throw new NotImplementedException();
    }
}

/// <summary>
/// Converts null to collapsed visibility
/// </summary>
public class NullToVisibilityConverter : IValueConverter
{
    public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
    {
        return value != null ? Visibility.Visible : Visibility.Collapsed;
    }

    public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
    {
        throw new NotImplementedException();
    }
}

/// <summary>
/// Converts count to color (green if > 0, gray otherwise)
/// </summary>
public class CountToColorConverter : IValueConverter
{
    public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
    {
        if (value is int count && count > 0)
            return new SolidColorBrush((Color)ColorConverter.ConvertFromString("#2ecc71"));
        
        return new SolidColorBrush((Color)ColorConverter.ConvertFromString("#808080"));
    }

    public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
    {
        throw new NotImplementedException();
    }
}

/// <summary>
/// Inverts boolean for visibility binding
/// </summary>
public class InverseBoolToVisibilityConverter : IValueConverter
{
    public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
    {
        if (value is bool boolValue)
            return boolValue ? Visibility.Collapsed : Visibility.Visible;
        
        return Visibility.Collapsed;
    }

    public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
    {
        throw new NotImplementedException();
    }
}
```

## File: `platforms/windows/PortKiller/Helpers/WindowBlurHelper.cs`
```csharp
using System;
using System.Runtime.InteropServices;
using System.Windows;
using System.Windows.Interop;

namespace PortKiller.Helpers;

/// <summary>
/// Enables Windows 10/11 Acrylic blur effect on WPF windows using SetWindowCompositionAttribute
/// </summary>
public static class WindowBlurHelper
{
    [DllImport("user32.dll")]
    internal static extern int SetWindowCompositionAttribute(IntPtr hwnd, ref WindowCompositionAttributeData data);

    internal enum AccentState
    {
        ACCENT_DISABLED = 0,
        ACCENT_ENABLE_GRADIENT = 1,
        ACCENT_ENABLE_TRANSPARENTGRADIENT = 2,
        ACCENT_ENABLE_BLURBEHIND = 3,
        ACCENT_ENABLE_ACRYLICBLURBEHIND = 4, // Real acrylic blur (Windows 10 RS4+)
        ACCENT_INVALID_STATE = 5
    }

    [StructLayout(LayoutKind.Sequential)]
    internal struct AccentPolicy
    {
        public AccentState AccentState;
        public uint AccentFlags;
        public uint GradientColor; // Format: 0xAABBGGRR (Alpha, Blue, Green, Red)
        public uint AnimationId;
    }

    [StructLayout(LayoutKind.Sequential)]
    internal struct WindowCompositionAttributeData
    {
        public WindowCompositionAttribute Attribute;
        public IntPtr Data;
        public int SizeOfData;
    }

    internal enum WindowCompositionAttribute
    {
        WCA_ACCENT_POLICY = 19
    }

    /// <summary>
    /// Enables Acrylic blur effect on the window
    /// </summary>
    /// <param name="window">The WPF window</param>
    /// <param name="blurOpacity">Opacity of the blur (0-255). Default is 180 for good translucency</param>
    /// <param name="blurColor">Background tint color in BGR format (0xBBGGRR). Default is white (0xFFFFFF)</param>
    public static void EnableAcrylicBlur(Window window, byte blurOpacity = 180, uint blurColor = 0xFFFFFF)
    {
        try
        {
            var windowHelper = new WindowInteropHelper(window);
            
            if (windowHelper.Handle == IntPtr.Zero)
            {
                // Window not yet loaded, attach to SourceInitialized event
                window.SourceInitialized += (s, e) =>
                {
                    ApplyAcrylicBlur(window, blurOpacity, blurColor);
                };
            }
            else
            {
                ApplyAcrylicBlur(window, blurOpacity, blurColor);
            }
        }
        catch (Exception ex)
        {
            System.Diagnostics.Debug.WriteLine($"Failed to enable acrylic blur: {ex.Message}");
        }
    }

    private static void ApplyAcrylicBlur(Window window, byte blurOpacity, uint blurColor)
    {
        var windowHelper = new WindowInteropHelper(window);
        
        var accent = new AccentPolicy
        {
            AccentState = AccentState.ACCENT_ENABLE_ACRYLICBLURBEHIND,
            // Combine opacity and color: 0xAABBGGRR format
            GradientColor = ((uint)blurOpacity << 24) | (blurColor & 0xFFFFFF)
        };

        var accentStructSize = Marshal.SizeOf(accent);
        var accentPtr = Marshal.AllocHGlobal(accentStructSize);
        
        try
        {
            Marshal.StructureToPtr(accent, accentPtr, false);

            var data = new WindowCompositionAttributeData
            {
                Attribute = WindowCompositionAttribute.WCA_ACCENT_POLICY,
                SizeOfData = accentStructSize,
                Data = accentPtr
            };

            SetWindowCompositionAttribute(windowHelper.Handle, ref data);
        }
        finally
        {
            Marshal.FreeHGlobal(accentPtr);
        }
    }

    /// <summary>
    /// Enables blur with custom settings for a glass-like effect
    /// </summary>
    public static void EnableGlassBlur(Window window)
    {
        // Light opacity for maximum translucency, white tint
        EnableAcrylicBlur(window, blurOpacity: 100, blurColor: 0xFFFFFF);
    }

    /// <summary>
    /// Disables the blur effect
    /// </summary>
    public static void DisableBlur(Window window)
    {
        try
        {
            var windowHelper = new WindowInteropHelper(window);
            
            var accent = new AccentPolicy
            {
                AccentState = AccentState.ACCENT_DISABLED
            };

            var accentStructSize = Marshal.SizeOf(accent);
            var accentPtr = Marshal.AllocHGlobal(accentStructSize);
            
            try
            {
                Marshal.StructureToPtr(accent, accentPtr, false);

                var data = new WindowCompositionAttributeData
                {
                    Attribute = WindowCompositionAttribute.WCA_ACCENT_POLICY,
                    SizeOfData = accentStructSize,
                    Data = accentPtr
                };

                SetWindowCompositionAttribute(windowHelper.Handle, ref data);
            }
            finally
            {
                Marshal.FreeHGlobal(accentPtr);
            }
        }
        catch (Exception ex)
        {
            System.Diagnostics.Debug.WriteLine($"Failed to disable blur: {ex.Message}");
        }
    }
}
```

## File: `platforms/windows/PortKiller/Models/CloudflaredProtocol.cs`
```csharp
namespace PortKiller.Models;

public enum CloudflaredProtocol
{
    Http2,
    Quic
}

public static class CloudflaredProtocolExtensions
{
    public static string ToArgument(this CloudflaredProtocol protocol)
    {
        return protocol == CloudflaredProtocol.Quic ? "quic" : "http2";
    }

    public static string ToDisplayName(this CloudflaredProtocol protocol)
    {
        return protocol == CloudflaredProtocol.Quic ? "QUIC" : "HTTP/2";
    }

    public static CloudflaredProtocol FromString(string? value)
    {
        return string.Equals(value, "quic", System.StringComparison.OrdinalIgnoreCase)
            ? CloudflaredProtocol.Quic
            : CloudflaredProtocol.Http2;
    }
}
```

## File: `platforms/windows/PortKiller/Models/CloudflareTunnel.cs`
```csharp
using System;
using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace PortKiller.Models;

/// <summary>
/// Status of a Cloudflare tunnel
/// </summary>
public enum TunnelStatus
{
    Idle,
    Starting,
    Active,
    Stopping,
    Error
}

/// <summary>
/// Represents a Cloudflare Quick Tunnel instance
/// </summary>
public class CloudflareTunnel : INotifyPropertyChanged
{
    private Guid _id;
    private int _port;
    private TunnelStatus _status;
    private string? _tunnelUrl;
    private string? _lastError;
    private DateTime? _startTime;
    private int? _processId;

    public Guid Id
    {
        get => _id;
        set => SetField(ref _id, value);
    }

    public int Port
    {
        get => _port;
        set => SetField(ref _port, value);
    }

    public TunnelStatus Status
    {
        get => _status;
        set
        {
            if (SetField(ref _status, value))
            {
                OnPropertyChanged(nameof(StatusText));
                OnPropertyChanged(nameof(StatusColor));
                OnPropertyChanged(nameof(IsActive));
                OnPropertyChanged(nameof(IsStarting));
                OnPropertyChanged(nameof(CanCopyUrl));
                OnPropertyChanged(nameof(CanOpenUrl));
            }
        }
    }

    public string? TunnelUrl
    {
        get => _tunnelUrl;
        set
        {
            if (SetField(ref _tunnelUrl, value))
            {
                OnPropertyChanged(nameof(DisplayUrl));
                OnPropertyChanged(nameof(CanCopyUrl));
                OnPropertyChanged(nameof(CanOpenUrl));
            }
        }
    }

    public string? LastError
    {
        get => _lastError;
        set => SetField(ref _lastError, value);
    }

    public DateTime? StartTime
    {
        get => _startTime;
        set
        {
            if (SetField(ref _startTime, value))
            {
                OnPropertyChanged(nameof(Uptime));
            }
        }
    }

    public int? ProcessId
    {
        get => _processId;
        set => SetField(ref _processId, value);
    }

    // Computed properties for UI binding
    public string StatusText => Status switch
    {
        TunnelStatus.Idle => "Idle",
        TunnelStatus.Starting => "Starting...",
        TunnelStatus.Active => "Active",
        TunnelStatus.Stopping => "Stopping...",
        TunnelStatus.Error => "Error",
        _ => "Unknown"
    };

    public string StatusColor => Status switch
    {
        TunnelStatus.Idle => "#808080",
        TunnelStatus.Starting => "#f39c12",
        TunnelStatus.Active => "#2ecc71",
        TunnelStatus.Stopping => "#f39c12",
        TunnelStatus.Error => "#e74c3c",
        _ => "#808080"
    };

    public bool IsActive => Status == TunnelStatus.Active;
    public bool IsStarting => Status == TunnelStatus.Starting;
    public bool CanCopyUrl => IsActive && !string.IsNullOrEmpty(TunnelUrl);
    public bool CanOpenUrl => IsActive && !string.IsNullOrEmpty(TunnelUrl);

    public string DisplayUrl => string.IsNullOrEmpty(TunnelUrl) 
        ? (Status == TunnelStatus.Starting ? "Generating URL..." : "No URL available")
        : TunnelUrl.Replace("https://", "");

    public string Uptime
    {
        get
        {
            if (StartTime == null || Status != TunnelStatus.Active)
                return "-";

            var elapsed = DateTime.Now - StartTime.Value;
            if (elapsed.TotalMinutes < 1)
                return $"{elapsed.Seconds}s";
            if (elapsed.TotalHours < 1)
                return $"{elapsed.Minutes}m {elapsed.Seconds}s";
            return $"{(int)elapsed.TotalHours}h {elapsed.Minutes}m";
        }
    }

    public CloudflareTunnel(int port)
    {
        Id = Guid.NewGuid();
        Port = port;
        Status = TunnelStatus.Idle;
    }

    // INotifyPropertyChanged implementation
    public event PropertyChangedEventHandler? PropertyChanged;

    public virtual void OnPropertyChanged([CallerMemberName] string? propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }

    protected bool SetField<T>(ref T field, T value, [CallerMemberName] string? propertyName = null)
    {
        if (EqualityComparer<T>.Default.Equals(field, value)) return false;
        field = value;
        OnPropertyChanged(propertyName);
        return true;
    }
}
```

## File: `platforms/windows/PortKiller/Models/PortFilter.cs`
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace PortKiller.Models;

/// <summary>
/// Filter settings for the port list
/// </summary>
public class PortFilter
{
    public string SearchText { get; set; } = string.Empty;
    public int? MinPort { get; set; }
    public int? MaxPort { get; set; }
    public HashSet<ProcessType> ProcessTypes { get; set; } = new(Enum.GetValues<ProcessType>());
    public bool ShowOnlyFavorites { get; set; }
    public bool ShowOnlyWatched { get; set; }

    public bool IsActive =>
        !string.IsNullOrEmpty(SearchText) ||
        MinPort.HasValue ||
        MaxPort.HasValue ||
        ProcessTypes.Count < Enum.GetValues<ProcessType>().Length ||
        ShowOnlyFavorites ||
        ShowOnlyWatched;

    public bool Matches(PortInfo port, HashSet<int> favorites, List<WatchedPort> watched)
    {
        // Search text filter
        if (!string.IsNullOrEmpty(SearchText))
        {
            var query = SearchText.ToLowerInvariant();
            var matches = port.ProcessName.ToLowerInvariant().Contains(query) ||
                         port.Port.ToString().Contains(query) ||
                         port.Pid.ToString().Contains(query) ||
                         port.Address.ToLowerInvariant().Contains(query) ||
                         port.User.ToLowerInvariant().Contains(query) ||
                         port.Command.ToLowerInvariant().Contains(query);
            if (!matches) return false;
        }

        // Port range filter
        if (MinPort.HasValue && port.Port < MinPort.Value) return false;
        if (MaxPort.HasValue && port.Port > MaxPort.Value) return false;

        // Process type filter
        if (!ProcessTypes.Contains(port.ProcessType)) return false;

        // Favorites filter
        if (ShowOnlyFavorites && !favorites.Contains(port.Port)) return false;

        // Watched filter
        if (ShowOnlyWatched && !watched.Any(w => w.Port == port.Port)) return false;

        return true;
    }

    public void Reset()
    {
        SearchText = string.Empty;
        MinPort = null;
        MaxPort = null;
        ProcessTypes = new(Enum.GetValues<ProcessType>());
        ShowOnlyFavorites = false;
        ShowOnlyWatched = false;
    }
}

/// <summary>
/// Sidebar navigation items
/// </summary>
public enum SidebarItem
{
    AllPorts,
    Favorites,
    Watched,
    WebServer,
    Database,
    Development,
    System,
    Other,
    KubernetesPortForward,
    CloudflareTunnels,
    Settings
}

public static class SidebarItemExtensions
{
    public static string GetTitle(this SidebarItem item) => item switch
    {
        SidebarItem.AllPorts => "All Ports",
        SidebarItem.Favorites => "Favorites",
        SidebarItem.Watched => "Watched",
        SidebarItem.WebServer => "Web Server",
        SidebarItem.Database => "Database",
        SidebarItem.Development => "Development",
        SidebarItem.System => "System",
        SidebarItem.Other => "Other",
        SidebarItem.KubernetesPortForward => "K8s Port Forward",
        SidebarItem.CloudflareTunnels => "Cloudflare Tunnels",
        SidebarItem.Settings => "Settings",
        _ => "Unknown"
    };

    public static string GetIcon(this SidebarItem item) => item switch
    {
        SidebarItem.AllPorts => "\uE8FD", // List
        SidebarItem.Favorites => "\uE734", // Favorite
        SidebarItem.Watched => "\uE890", // View
        SidebarItem.WebServer => "\uE774", // Globe
        SidebarItem.Database => "\uF1AA", // Database
        SidebarItem.Development => "\uE90F", // Code
        SidebarItem.System => "\uE713", // Settings
        SidebarItem.Other => "\uE7E8", // Plug
        SidebarItem.KubernetesPortForward => "\uE968", // Connect
        SidebarItem.CloudflareTunnels => "\uE753", // Cloud
        SidebarItem.Settings => "\uE713", // Settings
        _ => "\uE7E8"
    };

    public static ProcessType? GetProcessType(this SidebarItem item) => item switch
    {
        SidebarItem.WebServer => ProcessType.WebServer,
        SidebarItem.Database => ProcessType.Database,
        SidebarItem.Development => ProcessType.Development,
        SidebarItem.System => ProcessType.System,
        SidebarItem.Other => ProcessType.Other,
        _ => null
    };
}
```

## File: `platforms/windows/PortKiller/Models/PortInfo.cs`
```csharp
using System;
using System.ComponentModel;
using System.Runtime.CompilerServices;

namespace PortKiller.Models;

/// <summary>
/// Information about a network port and its associated process.
/// Represents a listening TCP port with details about the process that owns it.
/// </summary>
public class PortInfo : INotifyPropertyChanged
{
    private bool _isConfirmingKill;
    private bool _isKilling;

    public event PropertyChangedEventHandler? PropertyChanged;

    /// <summary>
    /// Unique identifier for this port info instance
    /// </summary>
    public Guid Id { get; init; } = Guid.NewGuid();

    /// <summary>
    /// The port number (e.g., 3000, 8080)
    /// </summary>
    public int Port { get; init; }

    /// <summary>
    /// Process ID of the process using this port
    /// </summary>
    public int Pid { get; init; }

    /// <summary>
    /// Name of the process using this port
    /// </summary>
    public string ProcessName { get; init; } = string.Empty;

    /// <summary>
    /// Network address the port is bound to (e.g., "0.0.0.0", "127.0.0.1")
    /// </summary>
    public string Address { get; init; } = string.Empty;

    /// <summary>
    /// Username of the process owner
    /// </summary>
    public string User { get; init; } = string.Empty;

    /// <summary>
    /// Full command line that started the process
    /// </summary>
    public string Command { get; init; } = string.Empty;

    /// <summary>
    /// Whether this port is currently active/listening
    /// </summary>
    public bool IsActive { get; init; }

    /// <summary>
    /// UI State: Showing confirmation buttons
    /// </summary>
    public bool IsConfirmingKill
    {
        get => _isConfirmingKill;
        set
        {
            if (_isConfirmingKill != value)
            {
                _isConfirmingKill = value;
                OnPropertyChanged();
            }
        }
    }

    /// <summary>
    /// UI State: Process is being killed (spinner)
    /// </summary>
    public bool IsKilling
    {
        get => _isKilling;
        set
        {
            if (_isKilling != value)
            {
                _isKilling = value;
                OnPropertyChanged();
            }
        }
    }

    /// <summary>
    /// Formatted port number for display (e.g., ":3000")
    /// </summary>
    public string DisplayPort => $":{Port}";

    /// <summary>
    /// Detected process type based on the process name
    /// </summary>
    public ProcessType ProcessType => ProcessTypeExtensions.Detect(ProcessName);

    /// <summary>
    /// Create an inactive placeholder for a favorited/watched port
    /// </summary>
    public static PortInfo Inactive(int port) => new()
    {
        Port = port,
        Pid = 0,
        ProcessName = "Not running",
        Address = "-",
        User = "-",
        Command = string.Empty,
        IsActive = false
    };

    /// <summary>
    /// Create an active port from scan results
    /// </summary>
    public static PortInfo Active(
        int port,
        int pid,
        string processName,
        string address,
        string user,
        string command) => new()
    {
        Port = port,
        Pid = pid,
        ProcessName = processName,
        Address = address,
        User = user,
        Command = command,
        IsActive = true
    };

    protected virtual void OnPropertyChanged([CallerMemberName] string? propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}
```

## File: `platforms/windows/PortKiller/Models/ProcessType.cs`
```csharp
using System;
using System.Linq;

namespace PortKiller.Models;

/// <summary>
/// Category of process based on its function.
/// Provides automatic detection of process categories based on well-known process names.
/// </summary>
public enum ProcessType
{
    WebServer,
    Database,
    Development,
    System,
    Other
}

public static class ProcessTypeExtensions
{
    /// <summary>
    /// Gets the display name for the process type
    /// </summary>
    public static string GetDisplayName(this ProcessType type) => type switch
    {
        ProcessType.WebServer => "Web Server",
        ProcessType.Database => "Database",
        ProcessType.Development => "Development",
        ProcessType.System => "System",
        ProcessType.Other => "Other",
        _ => "Other"
    };

    /// <summary>
    /// Gets the icon glyph (Segoe Fluent Icons) for the process type
    /// </summary>
    public static string GetIcon(this ProcessType type) => type switch
    {
        ProcessType.WebServer => "\uE774", // Globe
        ProcessType.Database => "\uF1AA", // Database
        ProcessType.Development => "\uE90F", // Code
        ProcessType.System => "\uE713", // Settings
        ProcessType.Other => "\uE7E8", // Plug
        _ => "\uE7E8"
    };

    /// <summary>
    /// Detect the process type from a process name
    /// </summary>
    public static ProcessType Detect(string processName)
    {
        if (string.IsNullOrEmpty(processName))
            return ProcessType.Other;

        var name = processName.ToLowerInvariant();

        // Web servers
        string[] webServers = ["nginx", "apache", "httpd", "caddy", "traefik", "lighttpd", "iis", "iisexpress"];
        if (webServers.Any(name.Contains))
            return ProcessType.WebServer;

        // Databases
        string[] databases = ["postgres", "mysql", "mariadb", "redis", "mongo", "sqlite", "cockroach", "clickhouse", "sqlservr", "mssql"];
        if (databases.Any(name.Contains))
            return ProcessType.Database;

        // Development tools
        string[] devTools = ["node", "npm", "yarn", "python", "ruby", "php", "java", "go", "cargo", "dotnet", "vite", "webpack", "esbuild", "next", "nuxt", "remix", "bun", "deno"];
        if (devTools.Any(name.Contains))
            return ProcessType.Development;

        // System processes
        string[] systemProcs = ["svchost", "csrss", "lsass", "winlogon", "services", "system", "smss", "dwm"];
        if (systemProcs.Any(name.Contains))
            return ProcessType.System;

        return ProcessType.Other;
    }
}
```

## File: `platforms/windows/PortKiller/Models/WatchedPort.cs`
```csharp
using System;
using System.Text.Json.Serialization;

namespace PortKiller.Models;

/// <summary>
/// A port being monitored for status changes.
/// Users can configure notifications when a watched port starts or stops.
/// </summary>
public record WatchedPort
{
    /// <summary>
    /// Unique identifier for this watched port
    /// </summary>
    [JsonPropertyName("id")]
    public Guid Id { get; init; } = Guid.NewGuid();

    /// <summary>
    /// The port number being watched
    /// </summary>
    [JsonPropertyName("port")]
    public int Port { get; init; }

    /// <summary>
    /// Whether to send a notification when this port becomes active
    /// </summary>
    [JsonPropertyName("notifyOnStart")]
    public bool NotifyOnStart { get; init; } = true;

    /// <summary>
    /// Whether to send a notification when this port becomes inactive
    /// </summary>
    [JsonPropertyName("notifyOnStop")]
    public bool NotifyOnStop { get; init; } = true;
}
```

## File: `platforms/windows/PortKiller/Services/NotificationService.cs`
```csharp
using System;

namespace PortKiller.Services;

/// <summary>
/// Service for sending Windows notifications for watched port events.
/// Uses simple message boxes for now (can be enhanced with Windows 10/11 toast notifications later)
/// </summary>
public class NotificationService
{
    private static readonly Lazy<NotificationService> _instance = new(() => new NotificationService());
    public static NotificationService Instance => _instance.Value;

    private bool _isInitialized;

    private NotificationService()
    {
    }

    /// <summary>
    /// Initialize the notification service
    /// </summary>
    public void Initialize()
    {
        _isInitialized = true;
    }

    /// <summary>
    /// Send notification when a watched port starts
    /// </summary>
    public void NotifyPortStarted(int port, string processName)
    {
        if (!_isInitialized)
            return;

        try
        {
            // For now, we'll just write to debug output
            // You can enhance this with Windows.UI.Notifications or other notification libraries
            System.Diagnostics.Debug.WriteLine($"✅ Port {port} started - Process: {processName}");
        }
        catch
        {
            // Silently fail - notifications are not critical
        }
    }

    /// <summary>
    /// Send notification when a watched port stops
    /// </summary>
    public void NotifyPortStopped(int port)
    {
        if (!_isInitialized)
            return;

        try
        {
            System.Diagnostics.Debug.WriteLine($"❌ Port {port} stopped");
        }
        catch
        {
            // Silently fail
        }
    }

    /// <summary>
    /// Send a general notification
    /// </summary>
    public void Notify(string title, string message)
    {
        if (!_isInitialized)
            return;

        try
        {
            System.Diagnostics.Debug.WriteLine($"📢 {title}: {message}");
        }
        catch
        {
            // Silently fail
        }
    }

    public void Unregister()
    {
        _isInitialized = false;
    }
}
```

## File: `platforms/windows/PortKiller/Services/PortScannerService.cs`
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.NetworkInformation;
using System.Runtime.InteropServices;
using System.Runtime.Versioning;
using System.Security.Principal;
using System.Threading.Tasks;
using PortKiller.Models;

namespace PortKiller.Services;

/// <summary>
/// Service for scanning listening TCP ports on Windows.
/// Uses GetExtendedTcpTable Win32 API for best performance and accuracy.
/// </summary>
[SupportedOSPlatform("windows")]
public class PortScannerService
{
    // Win32 API imports for TCP table
    [DllImport("iphlpapi.dll", SetLastError = true)]
    private static extern uint GetExtendedTcpTable(
        IntPtr pTcpTable,
        ref int dwOutBufLen,
        bool sort,
        int ipVersion,
        TCP_TABLE_CLASS tblClass,
        int reserved);

    private enum TCP_TABLE_CLASS
    {
        TCP_TABLE_BASIC_LISTENER = 0,
        TCP_TABLE_BASIC_CONNECTIONS = 1,
        TCP_TABLE_BASIC_ALL = 2,
        TCP_TABLE_OWNER_PID_LISTENER = 3,
        TCP_TABLE_OWNER_PID_CONNECTIONS = 4,
        TCP_TABLE_OWNER_PID_ALL = 5,
        TCP_TABLE_OWNER_MODULE_LISTENER = 6,
        TCP_TABLE_OWNER_MODULE_CONNECTIONS = 7,
        TCP_TABLE_OWNER_MODULE_ALL = 8
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct MIB_TCPROW_OWNER_PID
    {
        public uint state;
        public uint localAddr;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public byte[] localPort;
        public uint remoteAddr;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public byte[] remotePort;
        public int owningPid;

        public ushort LocalPort => BitConverter.ToUInt16(new byte[2] { localPort[1], localPort[0] }, 0);
        public string LocalAddress => new System.Net.IPAddress(localAddr).ToString();
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct MIB_TCPTABLE_OWNER_PID
    {
        public uint dwNumEntries;
        [MarshalAs(UnmanagedType.ByValArray, ArraySubType = UnmanagedType.Struct, SizeConst = 1)]
        public MIB_TCPROW_OWNER_PID[] table;
    }

    // IPv6 structures
    [StructLayout(LayoutKind.Sequential)]
    private struct MIB_TCP6ROW_OWNER_PID
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 16)]
        public byte[] localAddr;
        public uint localScopeId;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public byte[] localPort;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 16)]
        public byte[] remoteAddr;
        public uint remoteScopeId;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public byte[] remotePort;
        public uint state;
        public int owningPid;

        public ushort LocalPort => BitConverter.ToUInt16(new byte[2] { localPort[1], localPort[0] }, 0);
        public string LocalAddress => new System.Net.IPAddress(localAddr).ToString();
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct MIB_TCP6TABLE_OWNER_PID
    {
        public uint dwNumEntries;
        [MarshalAs(UnmanagedType.ByValArray, ArraySubType = UnmanagedType.Struct, SizeConst = 1)]
        public MIB_TCP6ROW_OWNER_PID[] table;
    }

    private const int AF_INET = 2;  // IPv4
    private const int AF_INET6 = 23; // IPv6
    private const uint MIB_TCP_STATE_LISTEN = 2;

    /// <summary>
    /// Scans all listening TCP ports using Windows API.
    /// Equivalent to macOS lsof command.
    /// </summary>
    public async Task<List<PortInfo>> ScanPortsAsync()
    {
        return await Task.Run(() =>
        {
            try
            {
                var ports = new List<PortInfo>();
                var processCache = new Dictionary<int, (string name, string command, string user)>();

                // Scan IPv4 ports
                var tcpRows = GetAllTcpConnections();
                var listeningRows = tcpRows.Where(row => row.state == MIB_TCP_STATE_LISTEN).ToList();

                foreach (var row in listeningRows)
                {
                    try
                    {
                        var pid = row.owningPid;
                        var port = row.LocalPort;
                        var address = row.LocalAddress;

                        // Get process info (with caching)
                        if (!processCache.TryGetValue(pid, out var processInfo))
                        {
                            processInfo = GetProcessInfo(pid);
                            processCache[pid] = processInfo;
                        }

                        var portInfo = PortInfo.Active(
                            port: port,
                            pid: pid,
                            processName: processInfo.name,
                            address: address,
                            user: processInfo.user,
                            command: processInfo.command);
                        
                        // Explicitly set IsKilling to false when creating new Active ports
                        portInfo.IsKilling = false;
                        portInfo.IsConfirmingKill = false;

                        ports.Add(portInfo);
                    }
                    catch
                    {
                        // Skip ports we can't get info for
                        continue;
                    }
                }

                // Scan IPv6 ports
                var tcp6Rows = GetAllTcp6Connections();
                var listening6Rows = tcp6Rows.Where(row => row.state == MIB_TCP_STATE_LISTEN).ToList();

                foreach (var row in listening6Rows)
                {
                    try
                    {
                        var pid = row.owningPid;
                        var port = row.LocalPort;
                        var address = row.LocalAddress;

                        // Get process info (with caching)
                        if (!processCache.TryGetValue(pid, out var processInfo))
                        {
                            processInfo = GetProcessInfo(pid);
                            processCache[pid] = processInfo;
                        }

                        var portInfo = PortInfo.Active(
                            port: port,
                            pid: pid,
                            processName: processInfo.name,
                            address: address,
                            user: processInfo.user,
                            command: processInfo.command);
                        
                        portInfo.IsKilling = false;
                        portInfo.IsConfirmingKill = false;

                        ports.Add(portInfo);
                    }
                    catch
                    {
                        // Skip ports we can't get info for
                        continue;
                    }
                }

                // Remove duplicates (same port + pid)
                return ports
                    .GroupBy(p => new { p.Port, p.Pid })
                    .Select(g => g.First())
                    .OrderBy(p => p.Port)
                    .ToList();
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Error scanning ports: {ex.Message}");
                return new List<PortInfo>();
            }
        });
    }

    /// <summary>
    /// Gets all TCP connections using Win32 API
    /// </summary>
    private List<MIB_TCPROW_OWNER_PID> GetAllTcpConnections()
    {
        var tcpRows = new List<MIB_TCPROW_OWNER_PID>();
        int bufferSize = 0;

        // First call to get buffer size
        uint result = GetExtendedTcpTable(
            IntPtr.Zero,
            ref bufferSize,
            true,
            AF_INET,
            TCP_TABLE_CLASS.TCP_TABLE_OWNER_PID_ALL,
            0);

        IntPtr tcpTablePtr = Marshal.AllocHGlobal(bufferSize);

        try
        {
            // Second call to get actual data
            result = GetExtendedTcpTable(
                tcpTablePtr,
                ref bufferSize,
                true,
                AF_INET,
                TCP_TABLE_CLASS.TCP_TABLE_OWNER_PID_ALL,
                0);

            if (result != 0)
                return tcpRows;

            var table = Marshal.PtrToStructure<MIB_TCPTABLE_OWNER_PID>(tcpTablePtr);
            var rowPtr = (IntPtr)((long)tcpTablePtr + Marshal.SizeOf(table.dwNumEntries));

            for (int i = 0; i < table.dwNumEntries; i++)
            {
                var row = Marshal.PtrToStructure<MIB_TCPROW_OWNER_PID>(rowPtr);
                tcpRows.Add(row);
                rowPtr = (IntPtr)((long)rowPtr + Marshal.SizeOf<MIB_TCPROW_OWNER_PID>());
            }
        }
        finally
        {
            Marshal.FreeHGlobal(tcpTablePtr);
        }

        return tcpRows;
    }

    /// <summary>
    /// Gets all IPv6 TCP connections using Win32 API
    /// </summary>
    private List<MIB_TCP6ROW_OWNER_PID> GetAllTcp6Connections()
    {
        var tcpRows = new List<MIB_TCP6ROW_OWNER_PID>();
        int bufferSize = 0;

        // First call to get buffer size
        uint result = GetExtendedTcpTable(
            IntPtr.Zero,
            ref bufferSize,
            true,
            AF_INET6,
            TCP_TABLE_CLASS.TCP_TABLE_OWNER_PID_ALL,
            0);

        if (bufferSize == 0)
            return tcpRows;

        IntPtr tcpTablePtr = Marshal.AllocHGlobal(bufferSize);

        try
        {
            // Second call to get actual data
            result = GetExtendedTcpTable(
                tcpTablePtr,
                ref bufferSize,
                true,
                AF_INET6,
                TCP_TABLE_CLASS.TCP_TABLE_OWNER_PID_ALL,
                0);

            if (result != 0)
                return tcpRows;

            var numEntries = Marshal.ReadInt32(tcpTablePtr);
            var rowPtr = (IntPtr)((long)tcpTablePtr + sizeof(int));

            for (int i = 0; i < numEntries; i++)
            {
                var row = Marshal.PtrToStructure<MIB_TCP6ROW_OWNER_PID>(rowPtr);
                tcpRows.Add(row);
                rowPtr = (IntPtr)((long)rowPtr + Marshal.SizeOf<MIB_TCP6ROW_OWNER_PID>());
            }
        }
        finally
        {
            Marshal.FreeHGlobal(tcpTablePtr);
        }

        return tcpRows;
    }

    /// <summary>
    /// Gets detailed process information (name, command line, user)
    /// </summary>
    private (string name, string command, string user) GetProcessInfo(int pid)
    {
        try
        {
            using var process = Process.GetProcessById(pid);
            var name = process.ProcessName;
            
            // Try to get full command line
            string command;
            try
            {
                // Use WMI to get command line
                command = GetProcessCommandLine(pid) ?? process.MainModule?.FileName ?? name;
                
                // Truncate if too long
                if (command.Length > 200)
                    command = command.Substring(0, 200) + "...";
            }
            catch
            {
                command = name;
            }

            // Get process owner (user)
            string user;
            try
            {
                user = GetProcessOwner(process) ?? Environment.UserName;
            }
            catch
            {
                user = Environment.UserName;
            }

            return (name, command, user);
        }
        catch
        {
            return ("Unknown", "Unknown", "Unknown");
        }
    }

    /// <summary>
    /// Gets the command line of a process using WMI
    /// </summary>
    private string? GetProcessCommandLine(int pid)
    {
        try
        {
            using var searcher = new System.Management.ManagementObjectSearcher(
                $"SELECT CommandLine FROM Win32_Process WHERE ProcessId = {pid}");
            using var objects = searcher.Get();
            
            foreach (System.Management.ManagementObject obj in objects)
            {
                return obj["CommandLine"]?.ToString();
            }
        }
        catch
        {
            // Ignore - we'll fallback to process name
        }
        return null;
    }

    /// <summary>
    /// Gets the owner (username) of a process
    /// </summary>
    private string? GetProcessOwner(Process process)
    {
        try
        {
            var processHandle = process.Handle;
            if (OpenProcessToken(processHandle, 8, out IntPtr tokenHandle))
            {
                try
                {
                    using var identity = new WindowsIdentity(tokenHandle);
                    return identity.Name;
                }
                finally
                {
                    CloseHandle(tokenHandle);
                }
            }
        }
        catch
        {
            // Ignore - we'll fallback
        }
        return null;
    }

    [DllImport("advapi32.dll", SetLastError = true)]
    private static extern bool OpenProcessToken(IntPtr ProcessHandle, uint DesiredAccess, out IntPtr TokenHandle);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool CloseHandle(IntPtr hObject);
}
```

## File: `platforms/windows/PortKiller/Services/ProcessKillerService.cs`
```csharp
using System;
using System.Diagnostics;
using System.Runtime.Versioning;
using System.Threading.Tasks;

namespace PortKiller.Services;

/// <summary>
/// Service for terminating processes on Windows.
/// Equivalent to macOS kill command functionality.
/// </summary>
[SupportedOSPlatform("windows")]
public class ProcessKillerService
{
    /// <summary>
    /// Kills a process by PID.
    /// Windows doesn't have SIGTERM equivalent, so this terminates immediately.
    /// </summary>
    public async Task<bool> KillProcessAsync(int pid, bool force = false)
    {
        return await Task.Run(() =>
        {
            try
            {
                using var process = Process.GetProcessById(pid);
                
                if (!force)
                {
                    // Try graceful close first
                    if (process.CloseMainWindow())
                    {
                        // Give it time to close gracefully
                        process.WaitForExit(2000);
                        if (process.HasExited)
                            return true;
                    }
                }

                // Force kill
                process.Kill(entireProcessTree: true);
                return true;
            }
            catch (ArgumentException)
            {
                // Process doesn't exist
                return false;
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Error killing process {pid}: {ex.Message}");
                return false;
            }
        });
    }

    /// <summary>
    /// Attempts to kill a process gracefully with fallback to force kill.
    /// Strategy:
    /// 1. Try CloseMainWindow() for graceful shutdown
    /// 2. Wait 500ms
    /// 3. Force kill with Process.Kill()
    /// </summary>
    public async Task<bool> KillProcessGracefullyAsync(int pid)
    {
        try
        {
            using var process = Process.GetProcessById(pid);

            // Try graceful close first
            var closedGracefully = process.CloseMainWindow();
            if (closedGracefully)
            {
                // Give it time to clean up (500ms grace period)
                var exited = process.WaitForExit(500);
                if (exited)
                    return true;
            }

            // Force kill if still running
            if (!process.HasExited)
            {
                await Task.Delay(100); // Small delay before force kill
                process.Kill(entireProcessTree: true);
                return true;
            }

            return true;
        }
        catch (ArgumentException)
        {
            // Process doesn't exist anymore
            return false;
        }
        catch (Exception ex)
        {
            Debug.WriteLine($"Error killing process {pid} gracefully: {ex.Message}");
            return false;
        }
    }

    /// <summary>
    /// Kills all processes listening on a specific port
    /// </summary>
    public async Task<int> KillProcessesOnPortAsync(int port)
    {
        var scanner = new PortScannerService();
        var ports = await scanner.ScanPortsAsync();
        var processesOnPort = ports.Where(p => p.Port == port && p.IsActive).ToList();

        int killedCount = 0;
        foreach (var portInfo in processesOnPort)
        {
            var success = await KillProcessGracefullyAsync(portInfo.Pid);
            if (success)
                killedCount++;
        }

        return killedCount;
    }

    /// <summary>
    /// Check if process exists and is running
    /// </summary>
    public bool ProcessExists(int pid)
    {
        try
        {
            using var process = Process.GetProcessById(pid);
            return !process.HasExited;
        }
        catch
        {
            return false;
        }
    }
}
```

## File: `platforms/windows/PortKiller/Services/SettingsService.cs`
```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using PortKiller.Models;

namespace PortKiller.Services;

/// <summary>
/// Service for persisting and loading application settings.
/// Stores data in AppData\Local\PortKiller
/// </summary>
public class SettingsService
{
    private const string AppName = "PortKiller";
    private const string SettingsFileName = "settings.json";
    private readonly string _settingsPath;

    public SettingsService()
    {
        var appDataPath = Path.Combine(
            Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData),
            AppName);
        
        Directory.CreateDirectory(appDataPath);
        _settingsPath = Path.Combine(appDataPath, SettingsFileName);
    }

    private class SettingsData
    {
        public List<int>? Favorites { get; set; }
        public List<WatchedPort>? WatchedPorts { get; set; }
        public int RefreshInterval { get; set; } = 5;
        public bool AutoStart { get; set; }
        public bool ShowNotifications { get; set; } = true;
        public string CloudflaredProtocol { get; set; } = "http2";
    }

    private SettingsData LoadSettingsData()
    {
        try
        {
            if (File.Exists(_settingsPath))
            {
                var json = File.ReadAllText(_settingsPath);
                return JsonSerializer.Deserialize<SettingsData>(json) ?? new SettingsData();
            }
        }
        catch
        {
            // If load fails, return defaults
        }
        return new SettingsData();
    }

    private void SaveSettingsData(SettingsData data)
    {
        try
        {
            var json = JsonSerializer.Serialize(data, new JsonSerializerOptions { WriteIndented = true });
            File.WriteAllText(_settingsPath, json);
        }
        catch
        {
            // Silently fail - settings save is not critical
        }
    }

    // Favorites
    public HashSet<int> GetFavorites()
    {
        var data = LoadSettingsData();
        return data.Favorites != null ? new HashSet<int>(data.Favorites) : new HashSet<int>();
    }

    public void SaveFavorites(HashSet<int> favorites)
    {
        var data = LoadSettingsData();
        data.Favorites = favorites.ToList();
        SaveSettingsData(data);
    }

    // Watched Ports
    public List<WatchedPort> GetWatchedPorts()
    {
        var data = LoadSettingsData();
        return data.WatchedPorts ?? new List<WatchedPort>();
    }

    public void SaveWatchedPorts(List<WatchedPort> watchedPorts)
    {
        var data = LoadSettingsData();
        data.WatchedPorts = watchedPorts;
        SaveSettingsData(data);
    }

    // Refresh Interval
    public int GetRefreshInterval()
    {
        var data = LoadSettingsData();
        return data.RefreshInterval;
    }

    public void SaveRefreshInterval(int seconds)
    {
        var data = LoadSettingsData();
        data.RefreshInterval = seconds;
        SaveSettingsData(data);
    }

    // Auto Start
    public bool GetAutoStart()
    {
        var data = LoadSettingsData();
        return data.AutoStart;
    }

    public void SaveAutoStart(bool autoStart)
    {
        var data = LoadSettingsData();
        data.AutoStart = autoStart;
        SaveSettingsData(data);
    }

    // Show Notifications
    public bool GetShowNotifications()
    {
        var data = LoadSettingsData();
        return data.ShowNotifications;
    }

    public void SaveShowNotifications(bool show)
    {
        var data = LoadSettingsData();
        data.ShowNotifications = show;
        SaveSettingsData(data);
    }

    // Cloudflared Protocol
    public CloudflaredProtocol GetCloudflaredProtocol()
    {
        var data = LoadSettingsData();
        return CloudflaredProtocolExtensions.FromString(data.CloudflaredProtocol);
    }

    public void SaveCloudflaredProtocol(CloudflaredProtocol protocol)
    {
        var data = LoadSettingsData();
        data.CloudflaredProtocol = protocol.ToArgument();
        SaveSettingsData(data);
    }

    // Clear all settings
    public void ClearAllSettings()
    {
        try
        {
            if (File.Exists(_settingsPath))
            {
                File.Delete(_settingsPath);
            }
        }
        catch
        {
            // Ignore errors
        }
    }
}
```

## File: `platforms/windows/PortKiller/Services/TunnelService.cs`
```csharp
using System.Diagnostics;
using System.IO;
using System.Text.RegularExpressions;
using PortKiller.Models;

namespace PortKiller.Services;

/// <summary>
/// Service for managing Cloudflare tunnel processes
/// </summary>
public class TunnelService
{
    private readonly Dictionary<Guid, Process> _processes = new();
    private readonly Dictionary<Guid, Action<string>> _urlHandlers = new();
    private readonly Dictionary<Guid, Action<string>> _errorHandlers = new();

    // Possible cloudflared.exe installation paths
    private static readonly string[] CloudflaredPaths = {
        @"C:\Program Files\cloudflared\cloudflared.exe",
        @"C:\Program Files (x86)\cloudflared\cloudflared.exe",
        @"C:\ProgramData\chocolatey\bin\cloudflared.exe",
        Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), @"cloudflared\cloudflared.exe"),
        @"cloudflared.exe" // Try PATH
    };

    /// <summary>
    /// Checks if cloudflared is installed
    /// </summary>
    public bool IsCloudflaredInstalled => CloudflaredPath != null;

    /// <summary>
    /// Gets the path to cloudflared.exe if installed
    /// </summary>
    public string? CloudflaredPath
    {
        get
        {
            // Check explicit paths first
            var explicitPath = CloudflaredPaths.Take(CloudflaredPaths.Length - 1)
                .FirstOrDefault(File.Exists);
            
            if (explicitPath != null)
                return explicitPath;

            // Try to find in PATH
            try
            {
                var process = new Process
                {
                    StartInfo = new ProcessStartInfo
                    {
                        FileName = "where",
                        Arguments = "cloudflared",
                        RedirectStandardOutput = true,
                        UseShellExecute = false,
                        CreateNoWindow = true
                    }
                };
                
                process.Start();
                var output = process.StandardOutput.ReadToEnd();
                process.WaitForExit();

                if (process.ExitCode == 0 && !string.IsNullOrWhiteSpace(output))
                {
                    var firstPath = output.Split('\n')[0].Trim();
                    if (File.Exists(firstPath))
                        return firstPath;
                }
            }
            catch
            {
                // Ignore errors
            }

            return null;
        }
    }

    /// <summary>
    /// Starts a tunnel for the specified port
    /// </summary>
    public async Task<Process> StartTunnelAsync(CloudflareTunnel tunnel, CloudflaredProtocol protocol)
    {
        var cloudflaredPath = CloudflaredPath;
        if (cloudflaredPath == null)
            throw new InvalidOperationException("cloudflared is not installed");

        var protocolArg = protocol.ToArgument();
        var process = new Process
        {
            StartInfo = new ProcessStartInfo
            {
                FileName = cloudflaredPath,
                Arguments = $"tunnel --url localhost:{tunnel.Port} --protocol {protocolArg}",
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true
            }
        };

        // Set up output handlers
        process.OutputDataReceived += (sender, e) => 
        {
            if (!string.IsNullOrEmpty(e.Data))
                ParseOutput(tunnel.Id, e.Data);
        };

        process.ErrorDataReceived += (sender, e) => 
        {
            if (!string.IsNullOrEmpty(e.Data))
                ParseOutput(tunnel.Id, e.Data);
        };

        try
        {
            process.Start();
            process.BeginOutputReadLine();
            process.BeginErrorReadLine();

            _processes[tunnel.Id] = process;
            tunnel.ProcessId = process.Id;

            // Wait a moment to check if process started successfully
            await Task.Delay(1000);

            if (process.HasExited)
            {
                throw new InvalidOperationException($"Cloudflared process exited with code {process.ExitCode}");
            }

            return process;
        }
        catch (Exception ex)
        {
            _errorHandlers.TryGetValue(tunnel.Id, out var errorHandler);
            errorHandler?.Invoke($"Failed to start tunnel: {ex.Message}");
            throw;
        }
    }

    /// <summary>
    /// Stops a tunnel
    /// </summary>
    public async Task StopTunnelAsync(Guid tunnelId)
    {
        if (!_processes.TryGetValue(tunnelId, out var process))
            return;

        try
        {
            if (!process.HasExited)
            {
                // Try graceful shutdown first
                process.Kill(entireProcessTree: false);
                
                // Wait up to 2 seconds for graceful shutdown
                var exited = process.WaitForExit(2000);
                
                // Force kill if still running
                if (!exited && !process.HasExited)
                {
                    process.Kill(entireProcessTree: true);
                }
            }
        }
        catch (Exception ex)
        {
            Debug.WriteLine($"Error stopping tunnel {tunnelId}: {ex.Message}");
        }
        finally
        {
            process.Dispose();
            _processes.Remove(tunnelId);
            _urlHandlers.Remove(tunnelId);
            _errorHandlers.Remove(tunnelId);
        }

        await Task.CompletedTask;
    }

    /// <summary>
    /// Stops all active tunnels
    /// </summary>
    public async Task StopAllTunnelsAsync()
    {
        var tunnelIds = _processes.Keys.ToList();
        foreach (var id in tunnelIds)
        {
            await StopTunnelAsync(id);
        }
    }

    /// <summary>
    /// Registers a handler for when the tunnel URL is ready
    /// </summary>
    public void SetUrlHandler(Guid tunnelId, Action<string> handler)
    {
        _urlHandlers[tunnelId] = handler;
    }

    /// <summary>
    /// Registers a handler for errors
    /// </summary>
    public void SetErrorHandler(Guid tunnelId, Action<string> handler)
    {
        _errorHandlers[tunnelId] = handler;
    }

    /// <summary>
    /// Checks if a tunnel process is running
    /// </summary>
    public bool IsRunning(Guid tunnelId)
    {
        return _processes.TryGetValue(tunnelId, out var process) && !process.HasExited;
    }

    /// <summary>
    /// Parses cloudflared output to extract tunnel URL
    /// </summary>
    private void ParseOutput(Guid tunnelId, string line)
    {
        // cloudflared outputs URLs in format:
        // "https://something-random.trycloudflare.com"
        // Can appear in table format or plain text

        var urlPattern = @"https://[a-z0-9-]+\.trycloudflare\.com";
        var match = Regex.Match(line, urlPattern);

        if (match.Success)
        {
            var url = match.Value;
            _urlHandlers.TryGetValue(tunnelId, out var urlHandler);
            urlHandler?.Invoke(url);
        }

        // Check for errors
        var lowerLine = line.ToLower();
        if (lowerLine.Contains("error") || 
            lowerLine.Contains("failed") || 
            lowerLine.Contains("unable to") ||
            lowerLine.Contains("permission denied"))
        {
            _errorHandlers.TryGetValue(tunnelId, out var errorHandler);
            errorHandler?.Invoke(line);
        }
    }

    /// <summary>
    /// Cleans up any orphaned cloudflared processes from previous sessions
    /// </summary>
    public async Task CleanupOrphanedTunnelsAsync()
    {
        await Task.Run(() =>
        {
            try
            {
                var processes = Process.GetProcessesByName("cloudflared");
                foreach (var process in processes)
                {
                    try
                    {
                        // Check if it's a tunnel process
                        var commandLine = GetProcessCommandLine(process.Id);
                        if (commandLine != null && commandLine.Contains("tunnel") && commandLine.Contains("--url"))
                        {
                            process.Kill();
                            Debug.WriteLine($"Killed orphaned cloudflared process (PID: {process.Id})");
                        }
                    }
                    catch
                    {
                        // Process may have already exited
                    }
                    finally
                    {
                        process.Dispose();
                    }
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"Error cleaning up orphaned tunnels: {ex.Message}");
            }
        });
    }

    /// <summary>
    /// Gets the command line of a process (for cleanup verification)
    /// </summary>
    private string? GetProcessCommandLine(int processId)
    {
        try
        {
            using var searcher = new System.Management.ManagementObjectSearcher(
                $"SELECT CommandLine FROM Win32_Process WHERE ProcessId = {processId}");
            
            foreach (System.Management.ManagementObject obj in searcher.Get())
            {
                return obj["CommandLine"]?.ToString();
            }
        }
        catch
        {
            // Ignore
        }
        return null;
    }
}
```

## File: `platforms/windows/PortKiller/ViewModels/MainViewModel.cs`
```csharp
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using System.Windows.Threading;
using PortKiller.Models;
using PortKiller.Services;

namespace PortKiller.ViewModels;

/// <summary>
/// Main view model managing application state and port operations.
/// Equivalent to macOS AppState.swift
/// </summary>
public partial class MainViewModel : ObservableObject
{
    private readonly PortScannerService _scanner;
    private readonly ProcessKillerService _killer;
    private readonly SettingsService _settings;
    private readonly NotificationService _notifications;
    private readonly Dispatcher _dispatcher;
    
    private CancellationTokenSource? _refreshCancellation;
    private Dictionary<int, bool> _previousPortStates = new();

    // Observable Properties
    [ObservableProperty]
    private ObservableCollection<PortInfo> _ports = new();

    [ObservableProperty]
    private ObservableCollection<PortInfo> _filteredPorts = new();

    [ObservableProperty]
    private bool _isScanning;

    [ObservableProperty]
    private PortInfo? _selectedPort;

    [ObservableProperty]
    private SidebarItem _selectedSidebarItem = SidebarItem.AllPorts;

    [ObservableProperty]
    private PortFilter _filter = new();

    [ObservableProperty]
    private HashSet<int> _favorites = new();

    [ObservableProperty]
    private List<WatchedPort> _watchedPorts = new();

    [ObservableProperty]
    private int _refreshInterval = 5;

    [ObservableProperty]
    private bool _showNotifications = true;

    public MainViewModel(
        PortScannerService scanner,
        ProcessKillerService killer,
        SettingsService settings,
        NotificationService notifications,
        Dispatcher dispatcher)
    {
        _scanner = scanner;
        _killer = killer;
        _settings = settings;
        _notifications = notifications;
        _dispatcher = dispatcher;

        LoadSettings();
    }

    partial void OnSelectedSidebarItemChanged(SidebarItem value)
    {
        UpdateFilteredPorts();
    }

    partial void OnFilterChanged(PortFilter value)
    {
        UpdateFilteredPorts();
    }

    // Initialization
    public async Task InitializeAsync()
    {
        _notifications.Initialize();
        await RefreshPortsAsync();
        StartAutoRefresh();
    }

    // Settings Management
    private void LoadSettings()
    {
        Favorites = _settings.GetFavorites();
        WatchedPorts = _settings.GetWatchedPorts();
        RefreshInterval = _settings.GetRefreshInterval();
        ShowNotifications = _settings.GetShowNotifications();
    }

    private void SaveSettings()
    {
        _settings.SaveFavorites(Favorites);
        _settings.SaveWatchedPorts(WatchedPorts);
        _settings.SaveRefreshInterval(RefreshInterval);
        _settings.SaveShowNotifications(ShowNotifications);
    }

    // Port Scanning
    [RelayCommand]
    public async Task RefreshPortsAsync()
    {
        if (IsScanning)
            return;

        IsScanning = true;

        try
        {
            var scannedPorts = await _scanner.ScanPortsAsync();
            
            // Update on UI thread
            _dispatcher.Invoke(() =>
            {
                Ports.Clear();
                foreach (var port in scannedPorts)
                {
                    Ports.Add(port);
                }

                UpdateFilteredPorts();
                CheckWatchedPorts();
            });
        }
        catch (Exception ex)
        {
            Debug.WriteLine($"Error refreshing ports: {ex.Message}");
        }
        finally
        {
            IsScanning = false;
        }
    }

    // Auto-refresh
    private void StartAutoRefresh()
    {
        _refreshCancellation?.Cancel();
        _refreshCancellation = new CancellationTokenSource();
        var token = _refreshCancellation.Token;

        Task.Run(async () =>
        {
            while (!token.IsCancellationRequested)
            {
                try
                {
                    await Task.Delay(TimeSpan.FromSeconds(RefreshInterval), token);
                    if (!token.IsCancellationRequested)
                    {
                        await RefreshPortsAsync();
                    }
                }
                catch (TaskCanceledException)
                {
                    break;
                }
            }
        }, token);
    }

    public void StopAutoRefresh()
    {
        _refreshCancellation?.Cancel();
    }

    // Port Operations
    [RelayCommand]
    public async Task KillProcessAsync(PortInfo? port)
    {
        if (port == null || !port.IsActive)
            return;

        try
        {
            // Set UI state for spinner
            port.IsKilling = true;
            
            var success = await _killer.KillProcessGracefullyAsync(port.Pid);
            if (success)
            {
                // Refresh immediately to show change
                await Task.Delay(500);
                await RefreshPortsAsync();
            }
            else
            {
                // Reset state if failed (and still in list)
                port.IsKilling = false;
            }
        }
        catch (Exception ex)
        {
            Debug.WriteLine($"Error killing process: {ex.Message}");
            port.IsKilling = false;
        }
    }

    // Favorites Management
    [RelayCommand]
    public void ToggleFavorite(int port)
    {
        if (Favorites.Contains(port))
        {
            Favorites.Remove(port);
        }
        else
        {
            Favorites.Add(port);
        }

        // Trigger property change
        OnPropertyChanged(nameof(Favorites));
        SaveSettings();
        UpdateFilteredPorts();
    }

    public bool IsFavorite(int port) => Favorites.Contains(port);

    // Watched Ports Management
    [RelayCommand]
    public void AddWatchedPort(int port)
    {
        if (!WatchedPorts.Any(w => w.Port == port))
        {
            WatchedPorts.Add(new WatchedPort { Port = port });
            OnPropertyChanged(nameof(WatchedPorts));
            SaveSettings();
            UpdateFilteredPorts();
        }
    }

    [RelayCommand]
    public void RemoveWatchedPort(int port)
    {
        var watched = WatchedPorts.FirstOrDefault(w => w.Port == port);
        if (watched != null)
        {
            WatchedPorts.Remove(watched);
            OnPropertyChanged(nameof(WatchedPorts));
            SaveSettings();
            UpdateFilteredPorts();
        }
    }

    public bool IsWatched(int port) => WatchedPorts.Any(w => w.Port == port);

    // Watched Port Notifications
    private void CheckWatchedPorts()
    {
        if (!ShowNotifications)
            return;

        var activePorts = Ports.Where(p => p.IsActive).Select(p => p.Port).ToHashSet();

        foreach (var watched in WatchedPorts)
        {
            var isActive = activePorts.Contains(watched.Port);
            var wasActive = _previousPortStates.GetValueOrDefault(watched.Port, false);

            // Port just started
            if (isActive && !wasActive && watched.NotifyOnStart)
            {
                var portInfo = Ports.First(p => p.Port == watched.Port);
                _notifications.NotifyPortStarted(watched.Port, portInfo.ProcessName);
            }

            // Port just stopped
            if (!isActive && wasActive && watched.NotifyOnStop)
            {
                _notifications.NotifyPortStopped(watched.Port);
            }

            _previousPortStates[watched.Port] = isActive;
        }
    }

    // Filtering
    private void UpdateFilteredPorts()
    {
        var result = GetFilteredPorts();
        
        FilteredPorts.Clear();
        foreach (var port in result)
        {
            FilteredPorts.Add(port);
        }
    }

    private List<PortInfo> GetFilteredPorts()
    {
        // Start with all or filtered by sidebar
        var result = SelectedSidebarItem switch
        {
            SidebarItem.AllPorts => Ports.ToList(),
            SidebarItem.Favorites => GetFavoritePorts(),
            SidebarItem.Watched => GetWatchedPortInfos(),
            SidebarItem.Settings => new List<PortInfo>(),
            _ when SelectedSidebarItem.GetProcessType() is ProcessType type 
                => Ports.Where(p => p.ProcessType == type).ToList(),
            _ => Ports.ToList()
        };

        // Apply additional filters
        if (Filter.IsActive)
        {
            result = result.Where(p => Filter.Matches(p, Favorites, WatchedPorts)).ToList();
        }

        return result.OrderBy(p => p.Port).ToList();
    }

    private List<PortInfo> GetFavoritePorts()
    {
        var result = new List<PortInfo>();
        var activePorts = Ports.ToLookup(p => p.Port);

        foreach (var favPort in Favorites)
        {
            var activePort = activePorts[favPort].FirstOrDefault();
            if (activePort != null)
            {
                result.Add(activePort);
            }
            else
            {
                result.Add(PortInfo.Inactive(favPort));
            }
        }

        return result;
    }

    private List<PortInfo> GetWatchedPortInfos()
    {
        var result = new List<PortInfo>();
        var activePorts = Ports.ToLookup(p => p.Port);

        foreach (var watched in WatchedPorts)
        {
            var activePort = activePorts[watched.Port].FirstOrDefault();
            if (activePort != null)
            {
                result.Add(activePort);
            }
            else
            {
                result.Add(PortInfo.Inactive(watched.Port));
            }
        }

        return result;
    }

    // Search
    public void Search(string query)
    {
        Filter.SearchText = query;
        OnPropertyChanged(nameof(Filter));
        UpdateFilteredPorts();
    }

    public void ClearSearch()
    {
        Filter.SearchText = string.Empty;
        OnPropertyChanged(nameof(Filter));
        UpdateFilteredPorts();
    }
}
```

## File: `platforms/windows/PortKiller/ViewModels/TunnelViewModel.cs`
```csharp
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Diagnostics;
using System.Runtime.CompilerServices;
using System.Windows;
using System.Windows.Threading;
using PortKiller.Models;
using PortKiller.Services;

namespace PortKiller.ViewModels;

/// <summary>
/// ViewModel for managing Cloudflare tunnels
/// </summary>
public class TunnelViewModel : INotifyPropertyChanged
{
    private readonly TunnelService _tunnelService;
    private readonly NotificationService _notificationService;
    private readonly SettingsService _settings;
    private readonly DispatcherTimer _uptimeTimer;
    private bool _isCloudflaredInstalled;
    private CloudflaredProtocol _cloudflaredProtocol;

    public ObservableCollection<CloudflareTunnel> Tunnels { get; }
    public IReadOnlyList<CloudflaredProtocolOption> ProtocolOptions { get; }

    public bool IsCloudflaredInstalled
    {
        get => _isCloudflaredInstalled;
        set => SetField(ref _isCloudflaredInstalled, value);
    }

    public int ActiveTunnelCount => Tunnels.Count(t => t.Status == TunnelStatus.Active);

    public CloudflaredProtocol CloudflaredProtocol
    {
        get => _cloudflaredProtocol;
        set
        {
            if (SetField(ref _cloudflaredProtocol, value))
            {
                _settings.SaveCloudflaredProtocol(value);
            }
        }
    }

    public TunnelViewModel(TunnelService tunnelService, NotificationService notificationService, SettingsService settings)
    {
        _tunnelService = tunnelService;
        _notificationService = notificationService;
        _settings = settings;
        Tunnels = new ObservableCollection<CloudflareTunnel>();
        ProtocolOptions = new List<CloudflaredProtocolOption>
        {
            new(CloudflaredProtocol.Http2, "HTTP/2"),
            new(CloudflaredProtocol.Quic, "QUIC")
        };

        // Check if cloudflared is installed
        IsCloudflaredInstalled = _tunnelService.IsCloudflaredInstalled;
        CloudflaredProtocol = _settings.GetCloudflaredProtocol();

        // Set up timer to update uptime every second
        _uptimeTimer = new DispatcherTimer
        {
            Interval = TimeSpan.FromSeconds(1)
        };
        _uptimeTimer.Tick += (s, e) => UpdateUptimes();
        _uptimeTimer.Start();

        // Clean up orphaned tunnels from previous sessions
        Task.Run(async () => await _tunnelService.CleanupOrphanedTunnelsAsync());
    }

    /// <summary>
    /// Starts a new tunnel for the specified port
    /// </summary>
    public async Task StartTunnelAsync(int port)
    {
        if (!IsCloudflaredInstalled)
        {
            MessageBox.Show(
                "cloudflared is not installed. Please install it to use Cloudflare Tunnels.\n\n" +
                "Installation options:\n" +
                "1. Download from: https://github.com/cloudflare/cloudflared/releases\n" +
                "2. Or use Chocolatey: choco install cloudflared",
                "cloudflared Not Found",
                MessageBoxButton.OK,
                MessageBoxImage.Warning);
            return;
        }

        // Check if tunnel already exists for this port
        var existingTunnel = Tunnels.FirstOrDefault(t => t.Port == port && t.Status != TunnelStatus.Error);
        if (existingTunnel != null)
        {
            // Already tunneling this port - just copy the URL if available
            if (!string.IsNullOrEmpty(existingTunnel.TunnelUrl))
            {
                CopyUrlToClipboard(existingTunnel.TunnelUrl);
            }
            return;
        }

        var tunnel = new CloudflareTunnel(port)
        {
            Status = TunnelStatus.Starting
        };

        Application.Current.Dispatcher.Invoke(() => Tunnels.Add(tunnel));

        // Set up handlers
        _tunnelService.SetUrlHandler(tunnel.Id, url =>
        {
            Application.Current.Dispatcher.Invoke(() =>
            {
                tunnel.TunnelUrl = url;
                tunnel.Status = TunnelStatus.Active;
                tunnel.StartTime = DateTime.Now;

                // Auto-copy URL to clipboard
                CopyUrlToClipboard(url);

                // Send notification
                _notificationService.Notify(
                    "Tunnel Active",
                    $"Port {tunnel.Port} is now public at\n{ShortenUrl(url)}");

                OnPropertyChanged(nameof(ActiveTunnelCount));
            });
        });

        _tunnelService.SetErrorHandler(tunnel.Id, error =>
        {
            Application.Current.Dispatcher.Invoke(() =>
            {
                tunnel.LastError = error;
                if (tunnel.Status != TunnelStatus.Active)
                {
                    tunnel.Status = TunnelStatus.Error;
                }
                Debug.WriteLine($"Tunnel error: {error}");
            });
        });

        try
        {
            await _tunnelService.StartTunnelAsync(tunnel, CloudflaredProtocol);

            // Wait a bit to see if URL is detected
            await Task.Delay(3000);

            if (tunnel.Status == TunnelStatus.Starting)
            {
                // Still starting, URL should appear soon
                Debug.WriteLine($"Tunnel for port {port} is starting, waiting for URL...");
            }
        }
        catch (Exception ex)
        {
            Application.Current.Dispatcher.Invoke(() =>
            {
                tunnel.Status = TunnelStatus.Error;
                tunnel.LastError = ex.Message;
                
                MessageBox.Show(
                    $"Failed to start tunnel for port {port}:\n{ex.Message}",
                    "Tunnel Error",
                    MessageBoxButton.OK,
                    MessageBoxImage.Error);
            });
        }
    }

    /// <summary>
    /// Stops a tunnel
    /// </summary>
    public async Task StopTunnelAsync(CloudflareTunnel tunnel)
    {
        tunnel.Status = TunnelStatus.Stopping;

        try
        {
            await _tunnelService.StopTunnelAsync(tunnel.Id);
            
            Application.Current.Dispatcher.Invoke(() =>
            {
                Tunnels.Remove(tunnel);
                OnPropertyChanged(nameof(ActiveTunnelCount));
            });
        }
        catch (Exception ex)
        {
            Debug.WriteLine($"Error stopping tunnel: {ex.Message}");
            tunnel.Status = TunnelStatus.Error;
            tunnel.LastError = ex.Message;
        }
    }

    /// <summary>
    /// Stops all active tunnels
    /// </summary>
    public async Task StopAllTunnelsAsync()
    {
        var tunnelsToStop = Tunnels.ToList();
        
        foreach (var tunnel in tunnelsToStop)
        {
            tunnel.Status = TunnelStatus.Stopping;
        }

        await _tunnelService.StopAllTunnelsAsync();

        Application.Current.Dispatcher.Invoke(() =>
        {
            Tunnels.Clear();
            OnPropertyChanged(nameof(ActiveTunnelCount));
        });
    }

    /// <summary>
    /// Copies tunnel URL to clipboard
    /// </summary>
    public void CopyUrlToClipboard(string url)
    {
        try
        {
            Clipboard.SetText(url);
            _notificationService.Notify("Copied", "Tunnel URL copied to clipboard");
        }
        catch (Exception ex)
        {
            Debug.WriteLine($"Failed to copy to clipboard: {ex.Message}");
        }
    }

    /// <summary>
    /// Opens tunnel URL in default browser
    /// </summary>
    public void OpenUrlInBrowser(string url)
    {
        try
        {
            Process.Start(new ProcessStartInfo
            {
                FileName = url,
                UseShellExecute = true
            });
        }
        catch (Exception ex)
        {
            MessageBox.Show(
                $"Failed to open URL:\n{ex.Message}",
                "Error",
                MessageBoxButton.OK,
                MessageBoxImage.Error);
        }
    }

    /// <summary>
    /// Re-checks cloudflared installation status
    /// </summary>
    public void RecheckInstallation()
    {
        IsCloudflaredInstalled = _tunnelService.IsCloudflaredInstalled;
    }

    /// <summary>
    /// Updates uptime for all active tunnels
    /// </summary>
    private void UpdateUptimes()
    {
        foreach (var tunnel in Tunnels.Where(t => t.Status == TunnelStatus.Active))
        {
            // Trigger property change for uptime
            tunnel.OnPropertyChanged(nameof(tunnel.Uptime));
        }
    }

    /// <summary>
    /// Shortens a trycloudflare.com URL for display
    /// </summary>
    private string ShortenUrl(string url)
    {
        return url.Replace("https://", "");
    }

    // INotifyPropertyChanged implementation
    public event PropertyChangedEventHandler? PropertyChanged;

    protected virtual void OnPropertyChanged([CallerMemberName] string? propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }

    protected bool SetField<T>(ref T field, T value, [CallerMemberName] string? propertyName = null)
    {
        if (EqualityComparer<T>.Default.Equals(field, value)) return false;
        field = value;
        OnPropertyChanged(propertyName);
        return true;
    }
}

public sealed class CloudflaredProtocolOption
{
    public CloudflaredProtocolOption(CloudflaredProtocol value, string label)
    {
        Value = value;
        Label = label;
    }

    public CloudflaredProtocol Value { get; }
    public string Label { get; }
}
```

