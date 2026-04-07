---
id: port
type: knowledge
owner: OA_Triage
---
# port
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
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

### File: README.md
```md
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

### File: platforms\windows\README.md
```md
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

### File: CONTRIBUTING.md
```md
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

### File: STYLE_GUIDE.md
```md
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

### File: platforms\macos\scripts\build-app.sh
```sh
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

