---
id: chops-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:01.224728
---

# KNOWLEDGE EXTRACT: chops
> **Extracted on:** 2026-03-30 13:25:38
> **Source:** chops

---

## File: `.env.example`
```
APPLE_TEAM_ID=
APPLE_ID=
SIGNING_IDENTITY_NAME=
```

## File: `.gitignore`
```
# Xcode
*.xcodeproj/xcuserdata/
*.xcworkspace/xcuserdata/
DerivedData/
build/
*.pbxuser
*.mode1v3
*.mode2v3
*.perspectivev3
*.moved-aside
*.hmap
*.ipa
*.dSYM.zip
*.dSYM

# Swift Package Manager
.build/
.swiftpm/
Packages/

# Environment
.env

# macOS
.DS_Store
*.swp
*~

# Distribution
*.dmg
*.app
*.zip

# Site
site/node_modules/
site/dist/
site/.astro/
site/.wrangler/
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## [Unreleased]

## [1.11.0] - 2026-03-28

- Chat with AI agents directly inside Chops (ACP support)
- Cancel in-progress AI requests
- Floating AI button for quick access to the compose panel
- Improved compose panel layout and usability

## [1.10.0] - 2026-03-27

- Native markdown editor with syntax highlighting and formatting shortcuts (bold, italic, headings, links, lists)
- Select and copy text from the skill preview
- Find bar in the skill editor (Cmd+F)
- Auto-save skill files after 1 second of inactivity

## [1.9.0] - 2026-03-27

- Scan and display agents alongside skills

## [1.8.0] - 2026-03-25

- Add skills to collections via right-click context menu
- Drag and drop skills into sidebar collections
- Detect skills from Claude Desktop and CLI plugins
- Faster skill preview loading (eliminated ~2s delay)

## [1.7.0] - 2026-03-24

- Rich markdown theme in skill preview
- Support for Antigravity, OpenCode, Pi, Global Agents, and Copilot CLI as tool sources
- Sidebar hides tools that aren't installed
- Non-skill config files hidden from All Skills view
- Fixed Sparkle minimum macOS version requirement

## [1.6.0] - 2026-03-22

- Fix layout freeze when selecting a skill
- Press Enter to quickly create new collections
- Rename collections from the right-click menu

## [1.5.0] - 2026-03-21

- Connect to remote servers (such as OpenClaw) to discover, browse, and edit skills (@t2)

## [1.4.0] - 2026-03-21

- Delete skills directly from the context menu or toolbar
- Diagnostic logging and fixes for UI freezing

## [1.3.0] - 2026-03-21

- Markdown preview mode with syntax highlighting in the skill editor

## [1.2.0] - 2026-03-21

- Skills registry browser for discovering and installing community skills

## [1.1.0] - 2026-03-18

- Drag-to-Applications DMG installer with styled Finder window
- macOS Sequoia (15) support
- Credential management moved to `.env` file (no more hardcoded values)

## [1.0.1] - 2026-03-16

- About tab in settings with version info, update checks, and links
- Apple logo in download button, version and system requirements on site
- Download button links directly to DMG

## [1.0.0] - 2026-03-15

- Initial release — discover, organize, and edit AI agent skills
- Three-column layout with sidebar, skill list, and markdown editor
- Support for Claude Code, Cursor, Codex, Windsurf, Copilot, Aider, Amp
- Sparkle auto-updates with EdDSA signing
- Marketing site at chops.md
```

## File: `CLAUDE.md`
```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What is Chops

A native macOS app (SwiftUI + SwiftData) for discovering, organizing, and editing AI coding agent skills across tools (Claude Code, Cursor, Codex, Windsurf, Copilot, Aider, Amp). Fully open source (MIT), public repo at github.com/Shpigford/chops. No sandbox — requires full filesystem access to read user dotfiles.

## Build & Run

```bash
# Generate Xcode project (required after changing project.yml)
xcodegen generate

# Open in Xcode
open Chops.xcodeproj

# CLI build
xcodebuild -scheme Chops -configuration Release

# Local release-like build that launches cleanly from shell
xcodebuild -scheme Chops -configuration LocalRelease

# Release (needs APPLE_TEAM_ID, APPLE_ID, SIGNING_IDENTITY_NAME env vars)
./scripts/release.sh <version>
```

Requires: Xcode, `brew install xcodegen`, macOS 15+. Sparkle (>= 2.6.0) is the only external dependency (auto-updates via GitHub Releases).

No test suite exists. Validate manually by building and running.

## Development Rules

**Always manually test.** After every change, build the app (`xcodebuild`), launch it, and exercise the feature you changed. Seeing "build succeeded" is not enough — open the app and verify the actual behavior. If it's a UI change, look at it. If it's a data change, confirm the data. No exceptions.

**No fallbacks.** Do not write fallback logic, graceful degradation, or backwards-compatibility shims. The product should work correctly via the primary code path. If something fails, fix the root cause — don't paper over it with a fallback. We are early-stage; the code should be clean and direct, not defensive.

## Architecture

**Entry:** `Chops/App/ChopsApp.swift` → sets up SwiftData ModelContainer + Sparkle updater.

**State:** `AppState` is an `@Observable` singleton holding UI filters, search text, and selection state.

**Models (SwiftData):**
- `Skill` — a discovered skill file. Uniquely identified by resolved symlink path. Tracks which tools it's installed in.
- `SkillCollection` — user-created groupings of skills.

**Services:**
- `SkillScanner` — probes tool directories (~/.claude/skills/, ~/.cursor/rules/, etc.), parses frontmatter, upserts into SwiftData. Deduplicates via resolved symlink paths.
- `FileWatcher` — FSEvents via `DispatchSourceFileSystemObject`, triggers re-scan on changes.
- `SkillParser` → dispatches to `FrontmatterParser` (.md) or `MDCParser` (.mdc).
- **ACP agent hierarchy** — `BaseACPAgent` owns all transport/session logic. Vendor subclasses override three hooks:
  - `shouldFilter(JsonRpcMessage) → Bool` — drop messages before SDK decoding (e.g. Augment's `usage_update`)
  - `postProcess(String) → String` — strip vendor-specific XML tags before text is stored
  - `resolvePermission(title, options)` — present permission UI; hook for future session-wide allow-all
  - `ACPAgentFactory.make(for: ToolSource)` instantiates the right subclass; `ComposePanel` holds `BaseACPAgent?`.

**Views:** Three-column `NavigationSplitView` (Sidebar → List → Detail). Editor uses native `NSTextView` with markdown highlighting. Cmd+S save via `FocusedValues`. Agent responses render via `MarkdownMessageView` (MarkdownUI `.gitHub` theme + syntax highlighting).

**Tool sources** are defined in `ToolSource.swift` — each enum case knows its display name, icon, and filesystem paths to scan.

## Release Pipeline

`scripts/release.sh` does: xcodegen → archive → export with Developer ID → create DMG → notarize → staple → git tag → generate Sparkle appcast.xml → GitHub Release. Appcast served at chops.md/appcast.xml.

## Website

Marketing site lives in `site/` — Astro 6, built with `npm run build` from that directory. Appcast XML is in `site/public/appcast.xml`.
```

## File: `ExportOptions.plist`
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>method</key>
    <string>developer-id</string>
    <key>teamID</key>
    <string>${APPLE_TEAM_ID}</string>
</dict>
</plist>
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Josh Pigford

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

## File: `project.yml`
```yaml
name: Chops
options:
  bundleIdPrefix: com.joshpigford
  deploymentTarget:
    macOS: "15.0"
  createIntermediateGroups: true
  generateEmptyDirectories: true

configs:
  Debug: debug
  Release: release
  LocalRelease: release

packages:
  Sparkle:
    url: https://github.com/sparkle-project/Sparkle
    from: "2.6.0"
  ACP:
    url: https://github.com/wiedymi/swift-acp
    branch: main
  Highlightr:
    url: https://github.com/raspu/Highlightr
    from: "2.2.1"
  cmark-gfm:
    url: https://github.com/brokenhandsio/cmark-gfm.git
    from: "2.1.0"

targets:
  Chops:
    type: application
    platform: macOS
    sources:
      - path: Chops
        excludes:
          - "*.entitlements"
          - Info.plist
    dependencies:
      - package: Sparkle
      - package: Highlightr
      - package: cmark-gfm
        product: cmark
      - package: ACP
        product: ACP
      - package: ACP
        product: ACPModel
      - package: ACP
        product: ACPRegistry
    settings:
      base:
        PRODUCT_BUNDLE_IDENTIFIER: com.joshpigford.Chops
        MARKETING_VERSION: "1.0.0"
        CURRENT_PROJECT_VERSION: 1
        INFOPLIST_FILE: Chops/Info.plist
        CODE_SIGN_ENTITLEMENTS: Chops/Chops.entitlements
        MACOSX_DEPLOYMENT_TARGET: "15.0"
        GENERATE_INFOPLIST_FILE: NO
        SWIFT_STRICT_CONCURRENCY: minimal
        ASSETCATALOG_COMPILER_APPICON_NAME: ChopsIcon
        ENABLE_HARDENED_RUNTIME: YES
      configs:
        Release:
          CODE_SIGN_IDENTITY: "Developer ID Application"
        LocalRelease:
          CODE_SIGN_ENTITLEMENTS: Chops/ChopsLocalRelease.entitlements
```

## File: `README.md`
```markdown
<p align="center">
  <img src="site/public/favicon.png" width="128" height="128" alt="Chops icon" />
</p>

<h1 align="center">Chops</h1>

<p align="center">Your AI skills and agents, finally organized.</p>

<p align="center">
  <a href="https://github.com/Shpigford/chops/releases/latest/download/Chops.dmg">Download</a> &middot;
  <a href="https://chops.md">Website</a> &middot;
  <a href="https://x.com/Shpigford">@Shpigford</a>
</p>

<p align="center">
  <img src="site/public/screenshot.png" width="720" alt="Chops screenshot" />
</p>

One macOS app to discover, organize, and edit coding agent skills and agents across Claude Code, Cursor, Codex, Windsurf, and Amp. Stop digging through dotfiles.

## Features

- **Multi-tool support** — Claude Code, Cursor, Codex, Windsurf, Copilot, Aider, Amp
- **Skills + Agents** — Discovers both skills and agents from each tool's directories
- **Built-in editor** — Monospaced editor with Cmd+S save, frontmatter parsing
- **Collections** — Organize skills and agents without modifying source files
- **Real-time file watching** — FSEvents-based, instant updates on disk changes
- **Full-text search** — Search across name, description, and content
- **Create new skills & agents** — Generates correct boilerplate per tool
- **Remote servers** — Connect to servers like [OpenClaw](https://openclaw.ai) to discover, browse, and install skills

## Prerequisites

- **macOS 15** (Sequoia) or later
- **Xcode** with command-line tools (`xcode-select --install`)
- **Homebrew** ([brew.sh](https://brew.sh))
- **xcodegen** — `brew install xcodegen`

Sparkle (auto-update framework) is the only external dependency and is pulled automatically by Xcode via Swift Package Manager. No manual setup needed.

## Quick Start

```bash
git clone https://github.com/Shpigford/chops.git
cd chops
brew install xcodegen    # skip if already installed
xcodegen generate        # generates Chops.xcodeproj from project.yml
open Chops.xcodeproj     # opens in Xcode
```

Then hit **Cmd+R** to build and run.

> **Note:** The Xcode project is generated from `project.yml`. If you change `project.yml`, re-run `xcodegen generate`. Don't edit the `.xcodeproj` directly.

### CLI build (no Xcode GUI)

```bash
xcodebuild -scheme Chops -configuration Debug build
```

## Project Structure

```
Chops/
├── App/
│   ├── ChopsApp.swift        # @main entry — SwiftData ModelContainer + Sparkle
│   ├── AppState.swift         # @Observable singleton — filters, selection, search
│   └── ContentView.swift      # Three-column NavigationSplitView, kicks off scanning
├── Models/
│   ├── Skill.swift            # @Model — a discovered skill or agent file
│   ├── Collection.swift       # @Model — user-created skill groupings
│   └── ToolSource.swift       # Enum of supported tools, their paths and icons
├── Services/
│   ├── SkillScanner.swift     # Probes tool directories, upserts skills into SwiftData
│   ├── SkillParser.swift      # Dispatches to FrontmatterParser or MDCParser
│   ├── FileWatcher.swift      # FSEvents listener, triggers re-scan on changes
│   └── SearchService.swift    # In-memory full-text search
├── Utilities/
│   ├── FrontmatterParser.swift  # Extracts YAML frontmatter from .md files
│   └── MDCParser.swift          # Parses Cursor .mdc files
├── Views/
│   ├── Sidebar/               # Tool filters, skills/agents lists, collections
│   ├── Detail/                # Skill editor, metadata display
│   ├── Settings/              # Preferences & update UI
│   └── Shared/                # Reusable components (ToolBadge, NewSkillSheet)
├── Resources/                 # Asset catalog (tool icons, colors)
└── Chops.entitlements         # Disables sandbox (intentional)

project.yml          # xcodegen config — source of truth for Xcode project settings
scripts/             # Release pipeline (release.sh)
site/                # Marketing website (Astro 6)
```

## Architecture

**SwiftUI + SwiftData**, native macOS with zero web views.

### App lifecycle

1. `ChopsApp` initializes a SwiftData `ModelContainer` (persists `Skill` and `SkillCollection`)
2. Sparkle updater starts in the background
3. `AppState` is created and injected into the SwiftUI environment
4. `ContentView` renders and calls `startScanning()`
5. `SkillScanner` probes all tool directories and upserts discovered skills
6. `FileWatcher` attaches FSEvents listeners — on any change, the scanner re-runs automatically

### Key design decisions

- **No sandbox.** The app needs unrestricted filesystem access to read dotfiles across `~/`. This is intentional and required for core functionality. The entitlements file explicitly disables the app sandbox.
- **Dedup via symlinks.** Skills are uniquely identified by their resolved symlink path. If the same file is symlinked into multiple tool directories, it shows up as one skill with multiple tool badges.
- **No test suite.** Validate changes manually — build, run, trigger the feature you changed, observe the result.

### State management

`AppState` is an `@Observable` class that holds all UI state: selected tool filter, selected skill, search text, sidebar filter mode. It's injected via `@Environment` and accessible from any view.

### UI layout

Three-column `NavigationSplitView`:
- **Sidebar** — tool filters and collections
- **List** — filtered/searched skill list
- **Detail** — skill editor (wraps `NSTextView` for native text editing with Cmd+S save)

## Supported Tools

Chops scans these directories for skills and agents:

| Tool | Skills | Agents |
|------|--------|--------|
| Claude Code | `~/.claude/skills/` | `~/.claude/agents/` |
| Cursor | `~/.cursor/skills/`, `~/.cursor/rules` | `~/.cursor/agents/` |
| Windsurf | `~/.codeium/windsurf/memories/`, `~/.windsurf/rules` | — |
| Codex | `~/.codex/skills/` | `~/.codex/agents/` |
| Amp | `~/.config/amp/skills/` | — |
| Global | `~/.agents/skills/` | — |

Copilot and Aider are also supported but only detect project-level skills and agents (no global paths). Custom scan paths can be added for any tool.

Tool definitions live in `Chops/Models/ToolSource.swift` — each enum case knows its display name, icon, color, and filesystem paths.

## Common Dev Tasks

### Add support for a new tool

1. Add a new case to the `ToolSource` enum in `Chops/Models/ToolSource.swift`
2. Fill in `displayName`, `iconName`, `color`, and `globalPaths`
3. Optionally add a logo to the asset catalog and return it from `logoAssetName`
4. Update `SkillScanner` if the new tool uses a non-standard file layout

### Modify skill parsing

- **Frontmatter (`.md`)** — edit `Chops/Utilities/FrontmatterParser.swift`
- **Cursor `.mdc` files** — edit `Chops/Utilities/MDCParser.swift`
- **Dispatch logic** — edit `Chops/Services/SkillParser.swift` (decides which parser to use)

### Change the UI

Views are in `Chops/Views/`, organized by column (Sidebar, Detail) and shared components. The main layout is in `Chops/App/ContentView.swift`.

## Testing

No automated test suite. Validate manually:

1. Build and run the app (Cmd+R)
2. Trigger the exact feature you changed
3. Observe the result — check for correct behavior and error messages
4. Test edge cases (empty states, missing directories, malformed files)

## Website

The marketing site lives in `site/` and is built with [Astro](https://astro.build/).

```bash
cd site
npm install      # first time only
npm run dev      # local dev server
npm run build    # production build → site/dist/
```

## AI Agent Setup

This repo includes a Claude Code skill at `.claude/skills/setup.md` that gives AI coding agents full context on the project — architecture, key files, and common tasks. If you're using Claude Code, it'll pick this up automatically.

## License

MIT — see [LICENSE](LICENSE).
```

## File: `SECURITY.md`
```markdown
# Security Policy

If you discover a security vulnerability in Chops, please report it through
GitHub's [private vulnerability reporting](https://github.com/Shpigford/chops/security/advisories/new)
rather than opening a public issue.
```

## File: `Chops/Chops.entitlements`
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.app-sandbox</key>
	<false/>
</dict>
</plist>
```

## File: `Chops/ChopsLocalRelease.entitlements`
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.app-sandbox</key>
	<false/>
	<key>com.apple.security.cs.disable-library-validation</key>
	<true/>
</dict>
</plist>
```

## File: `Chops/Info.plist`
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleName</key>
	<string>Chops</string>
	<key>CFBundleDisplayName</key>
	<string>Chops</string>
	<key>CFBundleIdentifier</key>
	<string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
	<key>CFBundleVersion</key>
	<string>$(CURRENT_PROJECT_VERSION)</string>
	<key>CFBundleShortVersionString</key>
	<string>$(MARKETING_VERSION)</string>
	<key>CFBundlePackageType</key>
	<string>APPL</string>
	<key>CFBundleExecutable</key>
	<string>$(EXECUTABLE_NAME)</string>
	<key>LSMinimumSystemVersion</key>
	<string>$(MACOSX_DEPLOYMENT_TARGET)</string>
	<key>CFBundleIconFile</key>
	<string>ChopsIcon</string>
	<key>CFBundleIconName</key>
	<string>ChopsIcon</string>
	<key>NSHumanReadableCopyright</key>
	<string>Copyright © 2026 Josh Pigford. All rights reserved.</string>
	<key>SUFeedURL</key>
	<string>https://chops.md/appcast.xml</string>
	<key>SUPublicEDKey</key>
	<string>I1gi82QlV84mZZXMzxJyVMFKpDCmcatBYVSGcq1nJgE=</string>
</dict>
</plist>
```

## File: `Chops/App/AppState.swift`
```
import SwiftUI

@Observable
final class AppState {
    var selectedTool: ToolSource?
    var selectedSkill: Skill?
    var searchText: String = ""
    var showingNewSkillSheet: Bool = false
    var showingRegistrySheet: Bool = false
    var newItemKind: ItemKind = .skill
    var sidebarFilter: SidebarFilter = .allSkills
    /// Filter by item kind within a tool view (nil = show all)
    var toolKindFilter: ItemKind?
}

enum SidebarFilter: Hashable {
    case allSkills
    case allAgents
    case allRules
    case favorites
    case tool(ToolSource)
    case collection(String)
    case server(String)
}
```

## File: `Chops/App/ChopsApp.swift`
```
import SwiftUI
import SwiftData
import Sparkle

@main
struct ChopsApp: App {
    @State private var appState = AppState()
    @AppStorage("ACPDebugLogging") private var debugLoggingEnabled = false
    private let updaterController: SPUStandardUpdaterController

    init() {
        updaterController = SPUStandardUpdaterController(
            startingUpdater: true,
            updaterDelegate: nil,
            userDriverDelegate: nil
        )
    }

    var sharedModelContainer: ModelContainer = {
        let schema = Schema([Skill.self, SkillCollection.self, RemoteServer.self])
        let config = ModelConfiguration(schema: schema, isStoredInMemoryOnly: false)

        do {
            return try ModelContainer(for: schema, configurations: [config])
        } catch {
            fatalError("Could not create ModelContainer: \(error)")
        }
    }()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(appState)
        }
        .modelContainer(sharedModelContainer)
        .commands {
            TextEditingCommands()
            CommandGroup(replacing: .saveItem) {
                Button("Save") {
                    NotificationCenter.default.post(name: .saveCurrentSkill, object: nil)
                }
                .keyboardShortcut("s", modifiers: .command)
                .disabled(appState.selectedSkill == nil)
            }
            CommandGroup(after: .appInfo) {
                CheckForUpdatesView(updater: updaterController.updater)
            }
            CommandGroup(after: .help) {
                Toggle("Enable Debug Logging", isOn: $debugLoggingEnabled)
                Divider()
                Button("Export Diagnostic Log…") {
                    let context = sharedModelContainer.mainContext
                    DiagnosticExporter.export(modelContext: context)
                }
            }
        }

        Settings {
            SettingsView(updater: updaterController.updater)
                .environment(appState)
                .modelContainer(sharedModelContainer)
        }
    }
}

// MARK: - Sparkle Check for Updates menu item

struct CheckForUpdatesView: View {
    @ObservedObject private var checkForUpdatesViewModel: CheckForUpdatesViewModel
    let updater: SPUUpdater

    init(updater: SPUUpdater) {
        self.updater = updater
        self.checkForUpdatesViewModel = CheckForUpdatesViewModel(updater: updater)
    }

    var body: some View {
        Button("Check for Updates…") {
            updater.checkForUpdates()
        }
        .disabled(!checkForUpdatesViewModel.canCheckForUpdates)
    }
}

final class CheckForUpdatesViewModel: ObservableObject {
    @Published var canCheckForUpdates = false
    private var observation: Any?

    init(updater: SPUUpdater) {
        observation = updater.observe(\.canCheckForUpdates, options: [.initial, .new]) { [weak self] updater, change in
            DispatchQueue.main.async {
                self?.canCheckForUpdates = updater.canCheckForUpdates
            }
        }
    }
}
```

## File: `Chops/App/ContentView.swift`
```
import SwiftUI
import SwiftData

struct ContentView: View {
    @Environment(\.modelContext) private var modelContext
    @Environment(AppState.self) private var appState
    @Query(sort: \Skill.name) private var skills: [Skill]
    @State private var scanner: SkillScanner?
    @State private var fileWatcher: FileWatcher?
    @State private var columnVisibility: NavigationSplitViewVisibility = .all

    var body: some View {
        @Bindable var appState = appState

        NavigationSplitView(columnVisibility: $columnVisibility) {
            SidebarView()
        } content: {
            SkillListView()
        } detail: {
            if let skill = appState.selectedSkill {
                SkillDetailView(skill: skill)
            } else {
                ContentUnavailableView(
                    "Select a Skill",
                    systemImage: "doc.text",
                    description: Text("Choose a skill from the sidebar to view and edit it.")
                )
            }
        }
        .searchable(text: $appState.searchText, prompt: "Search skills...")
        .onAppear {
            startScanning()
        }
        .sheet(isPresented: $appState.showingNewSkillSheet) {
            NewSkillSheet()
        }
        .sheet(isPresented: $appState.showingRegistrySheet) {
            RegistrySheet()
        }
        .onChange(of: appState.sidebarFilter) {
            appState.toolKindFilter = nil
        }
        .frame(minWidth: 900, minHeight: 500)
        .onReceive(NotificationCenter.default.publisher(for: .customScanPathsChanged)) { _ in
            scanner?.scanAll()
        }
    }

    private func startScanning() {
        AppLogger.ui.notice("App started, beginning initial scan")
        let scanner = SkillScanner(modelContext: modelContext)
        self.scanner = scanner
        scanner.removeDeletedSkills()
        scanner.scanAll()

        var allPaths: [String] = []
        for tool in ToolSource.allCases {
            allPaths.append(contentsOf: tool.globalPaths)
            allPaths.append(contentsOf: tool.globalAgentPaths)
        }
        let fm = FileManager.default
        let home = fm.homeDirectoryForCurrentUser.path
        let claudePlugins = "\(home)/.claude/plugins"
        let claudePluginCache = "\(claudePlugins)/cache"
        let claudePluginManifest = "\(claudePlugins)/installed_plugins.json"
        for path in [claudePlugins, claudePluginCache, claudePluginManifest] where fm.fileExists(atPath: path) {
            allPaths.append(path)
        }
        let claudeDesktopSessions = "\(home)/Library/Application Support/Claude/local-agent-mode-sessions"
        if fm.fileExists(atPath: claudeDesktopSessions) {
            allPaths.append(claudeDesktopSessions)
        }
        allPaths = Array(Set(allPaths)).sorted()

        let watcher = FileWatcher { _ in
            scanner.scanAll()
            scanner.removeDeletedSkills()
        }
        watcher.watchDirectories(allPaths)
        self.fileWatcher = watcher
        AppLogger.ui.notice("File watchers active on \(allPaths.count) directories")

        // Sync remote servers in the background
        Task {
            await scanner.syncAllRemoteServers()
        }
    }
}
```

## File: `Chops/ChopsIcon.icon/icon.json`
```json
{
  "fill" : {
    "linear-gradient" : [
      "extended-srgb:0.20392,0.78039,0.34902,1.00000",
      "extended-srgb:0.00000,0.78431,0.70196,1.00000"
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
      "layers" : [
        {
          "blend-mode" : "normal",
          "fill" : {
            "solid" : "extended-gray:1.00000,1.00000"
          },
          "glass" : true,
          "hidden" : false,
          "image-name" : "blocks.svg",
          "name" : "blocks",
          "opacity" : 1,
          "position" : {
            "scale" : 30,
            "translation-in-points" : [
              0,
              0
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

## File: `Chops/Models/ACPConfiguration.swift`
```
import Foundation
import ACPRegistry

// MARK: - ACP Configuration Manager

/// Manages registry-based ACP agent discovery, selection, and installation.
@Observable
@MainActor
final class ACPConfiguration {
    static let shared = ACPConfiguration()

    private static let enabledIdsKey = "acpEnabledAgentIds"

    /// Allowlist of registry agent IDs surfaced in the UI.
    /// Extend this set to support additional agents.
    static let supportedAgentIds: Set<String> = [
        "claude-acp",
        "auggie",
        "codex-acp",
        "cursor"
    ]

    private let registryClient = RegistryClient()
    private let installer = AgentInstaller()

    // MARK: - Observable State

    /// Registry agents filtered to `supportedAgentIds`, in allowlist order.
    private(set) var registryAgents: [RegistryAgent] = []
    private(set) var isLoadingRegistry = false
    private(set) var registryError: String?

    private var enabledIds: Set<String> {
        didSet {
            UserDefaults.standard.set(Array(enabledIds), forKey: Self.enabledIdsKey)
        }
    }

    // MARK: - Derived

    var enabledAgents: [RegistryAgent] {
        registryAgents.filter { enabledIds.contains($0.id) }
    }

    var hasEnabledACP: Bool { !enabledAgents.isEmpty }

    // MARK: - Init

    private init() {
        let stored = UserDefaults.standard.stringArray(forKey: Self.enabledIdsKey) ?? []
        enabledIds = Set(stored)
    }

    // MARK: - Enable / Disable

    func isEnabled(_ agentId: String) -> Bool { enabledIds.contains(agentId) }

    func setEnabled(_ agentId: String, _ on: Bool) {
        if on { enabledIds.insert(agentId) } else { enabledIds.remove(agentId) }
    }

    // MARK: - Registry

    func loadRegistryIfNeeded() async {
        guard registryAgents.isEmpty, !isLoadingRegistry else { return }
        await refreshRegistry()
    }

    func refreshRegistry() async {
        isLoadingRegistry = true
        registryError = nil
        do {
            let registry = try await registryClient.fetch(forceRefresh: true)
            let allowed = Self.supportedAgentIds
            let order: [String] = ["claude-acp", "auggie", "codex-acp", "cursor"]
            registryAgents = order.compactMap { id in
                registry.agents.first { $0.id == id && allowed.contains($0.id) }
            }
        } catch {
            registryError = error.localizedDescription
        }
        isLoadingRegistry = false
    }

    // MARK: - Resolve

    /// Returns a ready-to-launch `InstalledAgent` for the given registry agent.
    /// For npx/uvx agents this is instant; for binary agents it downloads on first use.
    func resolve(_ agent: RegistryAgent) async throws -> InstalledAgent {
        if let existing = await installer.installedAgent(agent.id) {
            return existing
        }
        return try await installer.install(agent)
    }
}
```

## File: `Chops/Models/AgentTarget.swift`
```
import Foundation

struct AgentTarget: Identifiable, Hashable {
    let id: String
    let displayName: String
    let globalSkillsDir: String
    let skillFileName: String

    /// Paths to check — at least one must exist for the agent to be considered installed.
    /// These should be files/dirs that the actual tool creates, NOT dirs that `npx skills add` would create.
    let evidencePaths: [String]

    /// Optional: app bundle name to check in /Applications
    let appBundleName: String?

    /// Optional: CLI binary name to check in PATH
    let cliBinaryName: String?

    var isInstalled: Bool {
        let fm = FileManager.default
        let home = fm.homeDirectoryForCurrentUser.path

        // Check for app bundle
        if let app = appBundleName {
            let appPaths = [
                "/Applications/\(app).app",
                "\(home)/Applications/\(app).app",
            ]
            if appPaths.contains(where: { fm.fileExists(atPath: $0) }) {
                return true
            }
        }

        // Check for CLI binary
        if let cli = cliBinaryName {
            let searchPaths = [
                "/usr/local/bin/\(cli)",
                "/opt/homebrew/bin/\(cli)",
                "\(home)/.local/bin/\(cli)",
            ]
            // Also check nvm paths
            let nvmDir = "\(home)/.nvm/versions/node"
            if let nodeDirs = try? fm.contentsOfDirectory(atPath: nvmDir) {
                for nodeDir in nodeDirs {
                    let binPath = "\(nvmDir)/\(nodeDir)/bin/\(cli)"
                    if fm.fileExists(atPath: binPath) { return true }
                }
            }
            for path in searchPaths where fm.fileExists(atPath: path) {
                return true
            }
        }

        // Check evidence paths — tool-specific config files
        for path in evidencePaths where fm.fileExists(atPath: path) {
            return true
        }

        return false
    }

    var expandedSkillsDir: String {
        (globalSkillsDir as NSString).expandingTildeInPath
    }

    static var installed: [AgentTarget] {
        all.filter(\.isInstalled)
    }

    static let all: [AgentTarget] = {
        let home = FileManager.default.homeDirectoryForCurrentUser.path
        let configHome: String = {
            if let xdg = ProcessInfo.processInfo.environment["XDG_CONFIG_HOME"], !xdg.isEmpty {
                return xdg
            }
            return "\(home)/.config"
        }()

        return [
            // CLI tools — detect via binary or config files
            AgentTarget(
                id: "claude-code",
                displayName: "Claude Code",
                globalSkillsDir: "\(home)/.claude/skills",
                skillFileName: "SKILL.md",
                evidencePaths: [
                    "\(home)/.claude/settings.json",
                    "\(home)/.claude/CLAUDE.md",
                    "\(home)/.claude/cache",
                ],
                appBundleName: nil,
                cliBinaryName: "claude"
            ),
            AgentTarget(
                id: "codex",
                displayName: "Codex",
                globalSkillsDir: "\(home)/.codex/skills",
                skillFileName: "SKILL.md",
                evidencePaths: [
                    "\(home)/.codex/config.toml",
                    "\(home)/.codex/auth.json",
                ],
                appBundleName: nil,
                cliBinaryName: "codex"
            ),
            AgentTarget(
                id: "amp",
                displayName: "Amp",
                globalSkillsDir: "\(configHome)/amp/skills",
                skillFileName: "SKILL.md",
                evidencePaths: [
                    "\(configHome)/amp/config.json",
                    "\(configHome)/amp/settings.json",
                ],
                appBundleName: nil,
                cliBinaryName: "amp"
            ),
            AgentTarget(
                id: "opencode",
                displayName: "OpenCode",
                globalSkillsDir: "\(configHome)/opencode/skills",
                skillFileName: "SKILL.md",
                evidencePaths: [
                    "\(configHome)/opencode/opencode.json",
                    "\(configHome)/opencode/opencode.jsonc",
                    "\(home)/.local/share/opencode",
                ],
                appBundleName: "OpenCode",
                cliBinaryName: "opencode"
            ),
            AgentTarget(
                id: "goose",
                displayName: "Goose",
                globalSkillsDir: "\(configHome)/goose/skills",
                skillFileName: "SKILL.md",
                evidencePaths: [
                    "\(configHome)/goose/config.yaml",
                    "\(configHome)/goose/profiles",
                ],
                appBundleName: nil,
                cliBinaryName: "goose"
            ),

            // IDE/editor apps — detect via /Applications
            AgentTarget(
                id: "cursor",
                displayName: "Cursor",
                globalSkillsDir: "\(home)/.cursor/skills",
                skillFileName: "SKILL.md",
                evidencePaths: [
                    "\(home)/.cursor/argv.json",
                    "\(home)/.cursor/extensions",
                ],
                appBundleName: "Cursor",
                cliBinaryName: nil
            ),
            AgentTarget(
                id: "windsurf",
                displayName: "Windsurf",
                globalSkillsDir: "\(home)/.codeium/windsurf/skills",
                skillFileName: "SKILL.md",
                evidencePaths: [
                    "\(home)/.codeium/windsurf/argv.json",
                    "\(home)/.codeium/windsurf/extensions",
                ],
                appBundleName: "Windsurf",
                cliBinaryName: nil
            ),
            AgentTarget(
                id: "warp",
                displayName: "Warp",
                globalSkillsDir: "\(home)/.warp/skills",
                skillFileName: "SKILL.md",
                evidencePaths: [
                    "\(home)/.warp/launch_configurations",
                ],
                appBundleName: "Warp",
                cliBinaryName: nil
            ),
        ]
    }()
}
```

## File: `Chops/Models/ChopsSettings.swift`
```
import Foundation

/// User-configurable source-of-truth root directory.
/// Sub-directories for skills, agents, and rules are derived from the root.
struct ChopsSettings {
    private init() {}

    private static let home = FileManager.default.homeDirectoryForCurrentUser.path

    static var sotDir: String {
        get { UserDefaults.standard.string(forKey: "sotDir") ?? "\(home)/.chops" }
        set { UserDefaults.standard.set(newValue, forKey: "sotDir") }
    }

    static var sotSkillsDir: String { "\(sotDir)/skills" }
    static var sotAgentsDir: String { "\(sotDir)/agents" }
    static var sotRulesDir: String { "\(sotDir)/rules" }

    /// When false (default), skills installed by CLI and Desktop plugins are excluded from the library.
    static var includePluginSkills: Bool {
        get { UserDefaults.standard.bool(forKey: "includePluginSkills") }
        set { UserDefaults.standard.set(newValue, forKey: "includePluginSkills") }
    }
}
```

## File: `Chops/Models/Collection.swift`
```
import SwiftData
import Foundation

@Model
final class SkillCollection {
    @Attribute(.unique) var name: String
    var icon: String
    var sortOrder: Int

    @Relationship(inverse: \Skill.collections)
    var skills: [Skill]

    init(name: String, icon: String = "folder", skills: [Skill] = [], sortOrder: Int = 0) {
        self.name = name
        self.icon = icon
        self.skills = skills
        self.sortOrder = sortOrder
    }
}
```

## File: `Chops/Models/RemoteServer.swift`
```
import SwiftData
import Foundation

@Model
final class RemoteServer {
    @Attribute(.unique) var id: String
    var label: String
    var host: String
    var port: Int
    var username: String
    var skillsBasePath: String
    var sshKeyPath: String?
    var lastSyncDate: Date?
    var lastSyncError: String?

    @Relationship(deleteRule: .cascade, inverse: \Skill.remoteServer)
    var skills: [Skill]

    init(
        label: String,
        host: String,
        port: Int = 22,
        username: String,
        skillsBasePath: String
    ) {
        self.id = UUID().uuidString
        self.label = label
        self.host = host
        self.port = port
        self.username = username
        self.skillsBasePath = skillsBasePath
        self.skills = []
    }

    var sshDestination: String {
        "\(username)@\(host)"
    }

    var isOpenClaw: Bool {
        skillsBasePath.contains("openclaw")
    }
}
```

## File: `Chops/Models/SchemaVersions.swift`
```
import SwiftData
import Foundation

// No versioned schema needed — SwiftData handles additive changes
// (new optional properties + new entities) via automatic lightweight migration.
```

## File: `Chops/Models/Skill.swift`
```
import SwiftData
import Foundation

enum ItemKind: String, Codable, CaseIterable {
    case skill
    case agent
    case rule

    var displayName: String {
        switch self {
        case .skill: "Skills"
        case .agent: "Agents"
        case .rule: "Rules"
        }
    }

    var singularName: String {
        switch self {
        case .skill: "Skill"
        case .agent: "Agent"
        case .rule: "Rule"
        }
    }

    var icon: String {
        switch self {
        case .skill: "doc.text"
        case .agent: "person.crop.rectangle"
        case .rule: "list.bullet.rectangle"
        }
    }
}

@Model
final class Skill {
    @Attribute(.unique) var resolvedPath: String
    var filePath: String
    var isDirectory: Bool
    var name: String
    var skillDescription: String
    var content: String
    var frontmatterData: Data?

    var collections: [SkillCollection]
    var isFavorite: Bool
    var lastOpened: Date?
    var fileModifiedDate: Date
    var fileSize: Int
    var isGlobal: Bool

    var remoteServer: RemoteServer?
    var remotePath: String?

    var isRemote: Bool { remoteServer != nil }

    var isPlugin: Bool {
        filePath.contains("/.claude/plugins/") ||
        filePath.contains("/local-agent-mode-sessions/") ||
        toolSources.contains(.claudeDesktop)
    }

    var isReadOnly: Bool {
        isPlugin || isBundledOpenClawSkill
    }

    /// Comma-separated tool raw values (e.g. "claude,cursor,codex")
    var toolSourcesRaw: String

    /// All file paths where this skill is installed (JSON-encoded array)
    var installedPathsData: Data?

    /// Raw `ItemKind` value. Defaults to `"skill"` for lightweight migration compatibility.
    var kind: String = ItemKind.skill.rawValue

    // MARK: - Computed

    var itemKind: ItemKind {
        get { ItemKind(rawValue: kind) ?? .skill }
        set { kind = newValue.rawValue }
    }

    var displayTypeName: String {
        switch itemKind {
        case .agent: "Agent"
        case .rule: "Rule"
        case .skill: "Skill"
        }
    }

    var toolSources: [ToolSource] {
        get {
            toolSourcesRaw
                .split(separator: ",")
                .compactMap { ToolSource(rawValue: String($0)) }
        }
        set {
            let unique = Array(Set(newValue.map(\.rawValue))).sorted()
            toolSourcesRaw = unique.joined(separator: ",")
        }
    }

    /// Primary tool source (first one added)
    var toolSource: ToolSource {
        toolSources.first ?? .custom
    }

    var installedPaths: [String] {
        get {
            guard let data = installedPathsData else { return [filePath] }
            return (try? JSONDecoder().decode([String].self, from: data)) ?? [filePath]
        }
        set {
            do {
                installedPathsData = try JSONEncoder().encode(Array(Set(newValue)))
            } catch {
                AppLogger.fileIO.fault("Failed to encode installedPaths: \(error.localizedDescription)")
            }
        }
    }

    var frontmatter: [String: String] {
        get {
            guard let data = frontmatterData else { return [:] }
            return (try? JSONDecoder().decode([String: String].self, from: data)) ?? [:]
        }
        set {
            do {
                frontmatterData = try JSONEncoder().encode(newValue)
            } catch {
                AppLogger.fileIO.fault("Failed to encode frontmatter: \(error.localizedDescription)")
            }
        }
    }

    /// How many tools this skill is installed for
    var installCount: Int { toolSources.count }

    private var isBundledOpenClawSkill: Bool {
        filePath.hasPrefix("/opt/homebrew/lib/node_modules/openclaw/skills/")
            || filePath.hasPrefix("/usr/local/lib/node_modules/openclaw/skills/")
    }

    /// For project-level skills, extracts the project name from the path.
    /// e.g. ~/Development/every-expert/.claude/skills/foo/SKILL.md → "every-expert"
    var projectName: String? {
        guard !isGlobal else { return nil }
        let components = filePath.components(separatedBy: "/")
        // Find the component before a dotfile directory (.claude, .cursor, .codex, etc.)
        for (i, component) in components.enumerated() {
            if component.hasPrefix(".") && i > 0 {
                return components[i - 1]
            }
        }
        return nil
    }

    // MARK: - Init

    init(
        filePath: String,
        toolSource: ToolSource,
        isDirectory: Bool = false,
        name: String = "",
        skillDescription: String = "",
        content: String = "",
        frontmatter: [String: String] = [:],

        collections: [SkillCollection] = [],
        isFavorite: Bool = false,
        lastOpened: Date? = nil,
        fileModifiedDate: Date = .now,
        fileSize: Int = 0,
        isGlobal: Bool = true,
        resolvedPath: String = "",
        kind: ItemKind = .skill
    ) {
        self.resolvedPath = resolvedPath.isEmpty ? filePath : resolvedPath
        self.filePath = filePath
        self.toolSourcesRaw = toolSource.rawValue
        self.installedPathsData = try? JSONEncoder().encode([filePath]) // [String] encode never throws
        self.isDirectory = isDirectory
        self.name = name
        self.skillDescription = skillDescription
        self.content = content
        self.frontmatterData = try? JSONEncoder().encode(frontmatter) // [String: String] encode never throws

        self.collections = collections
        self.isFavorite = isFavorite
        self.lastOpened = lastOpened
        self.fileModifiedDate = fileModifiedDate
        self.fileSize = fileSize
        self.isGlobal = isGlobal
        self.kind = kind.rawValue
    }

    // MARK: - Merge

    /// Merge another location/tool into this skill
    func addInstallation(path: String, tool: ToolSource) {
        var paths = installedPaths
        if !paths.contains(path) {
            paths.append(path)
            installedPaths = paths
        }
        var tools = toolSources
        if !tools.contains(tool) {
            tools.append(tool)
            toolSources = tools
        }
    }

    var deletionTargets: [String] {
        Array(
            Set(
                ([filePath] + installedPaths).map { path in
                    if isDirectory {
                        return (path as NSString).deletingLastPathComponent
                    }
                    return path
                }
            )
        ).sorted()
    }

    func deleteFromDisk() throws {
        let fm = FileManager.default

        for path in deletionTargets where fm.fileExists(atPath: path) {
            guard fm.isDeletableFile(atPath: path) else {
                throw SkillDeletionError.notDeletable(path)
            }
        }

        for path in deletionTargets where fm.fileExists(atPath: path) {
            try fm.removeItem(atPath: path)
        }
    }
}

enum SkillDeletionError: LocalizedError {
    case notDeletable(String)

    var errorDescription: String? {
        switch self {
        case .notDeletable(let path):
            let home = FileManager.default.homeDirectoryForCurrentUser.path
            let displayPath = path.replacingOccurrences(of: home, with: "~")
            return "Couldn't delete \(displayPath). Check permissions and try again."
        }
    }
}
```

## File: `Chops/Models/ToolSource.swift`
```
import SwiftUI

enum ToolSource: String, Codable, CaseIterable, Identifiable {
    case agents
    case augment
    case claude
    case cursor
    case windsurf
    case codex
    case copilot
    case aider
    case amp
    case openclaw
    case opencode
    case pi
    case antigravity
    case claudeDesktop
    case custom

    var id: String { rawValue }

    /// Whether this tool should appear in the sidebar tools list.
    var listable: Bool {
        switch self {
        case .custom, .claudeDesktop, .agents, .aider:
            return false
        default:
            return true
        }
    }

    var displayName: String {
        switch self {
        case .augment: "Auggie"
        case .claude: "Claude Code"
        case .cursor: "Cursor"
        case .windsurf: "Windsurf"
        case .codex: "Codex"
        case .copilot: "Copilot"
        case .aider: "Aider"
        case .amp: "Amp"
        case .openclaw: "OpenClaw"
        case .opencode: "OpenCode"
        case .pi: "Pi"
        case .agents: "Global"
        case .antigravity: "Antigravity"
        case .claudeDesktop: "Claude Desktop"
        case .custom: "Custom"
        }
    }

    /// SF Symbol fallback icon name
    var iconName: String {
        switch self {
        case .augment: "wand.and.sparkles"
        case .claude: "brain.head.profile"
        case .cursor: "cursorarrow.rays"
        case .windsurf: "wind"
        case .codex: "book.closed"
        case .copilot: "airplane"
        case .aider: "wrench.and.screwdriver"
        case .amp: "bolt.fill"
        case .openclaw: "server.rack"
        case .opencode: "terminal"
        case .pi: "sparkles"
        case .agents: "globe"
        case .antigravity: "arrow.up.circle"
        case .claudeDesktop: "desktopcomputer"
        case .custom: "folder"
        }
    }

    /// Asset catalog image name, nil if no custom logo
    var logoAssetName: String? {
        switch self {
        case .augment: "tool-augment"
        case .claude: "tool-claude"
        case .cursor: "tool-cursor"
        case .codex: "tool-codex"
        case .windsurf: "tool-windsurf"
        case .copilot: "tool-copilot"
        case .amp: "tool-amp"
        case .antigravity: "tool-antigravity"
        case .claudeDesktop: "tool-claude"
        case .opencode: "tool-opencode"
        default: nil
        }
    }

    var color: Color {
        switch self {
        case .augment: .cyan
        case .claude: .orange
        case .cursor: .blue
        case .windsurf: .teal
        case .codex: .green
        case .copilot: .purple
        case .aider: .yellow
        case .amp: .pink
        case .openclaw: .indigo
        case .opencode: .red
        case .pi: .cyan
        case .agents: .mint
        case .antigravity: .red
        case .claudeDesktop: .orange
        case .custom: .gray
        }
    }

    var globalAgentPaths: [String] {
        let home = FileManager.default.homeDirectoryForCurrentUser.path
        switch self {
        case .claude: return ["\(home)/.claude/agents"]
        case .cursor: return ["\(home)/.cursor/agents"]
        case .codex: return ["\(home)/.codex/agents"]
        default: return []
        }
    }

    var globalPaths: [String] {
        let home = FileManager.default.homeDirectoryForCurrentUser.path
        let configHome: String = {
            if let xdg = ProcessInfo.processInfo.environment["XDG_CONFIG_HOME"], !xdg.isEmpty {
                return xdg
            }
            return "\(home)/.config"
        }()
        switch self {
        case .augment: return ["\(home)/.augment/skills"]
        case .claude: return ["\(home)/.claude/skills"]
        case .cursor: return ["\(home)/.cursor/skills"]
        case .windsurf: return []
        case .codex: return ["\(home)/.codex/skills"]
        case .copilot: return ["\(home)/.copilot/skills"]
        case .aider: return []
        case .amp: return ["\(configHome)/amp/skills"]
        case .openclaw:
            var paths: [String] = []
            // Main skills directory
            if FileManager.default.fileExists(atPath: "\(home)/.openclaw/skills") {
                paths.append("\(home)/.openclaw/skills")
            }
            // Workspace skills (search all workspace dirs)
            let openclawDir = URL(fileURLWithPath: "\(home)/.openclaw")
            if let workspaces = try? FileManager.default.contentsOfDirectory(
                at: openclawDir,
                includingPropertiesForKeys: [.isDirectoryKey],
                options: [.skipsHiddenFiles]
            ) {
                for workspace in workspaces {
                    let skillsPath = workspace.appendingPathComponent("skills")
                    if FileManager.default.fileExists(atPath: skillsPath.path) {
                        paths.append(skillsPath.path)
                    }
                }
            }
            // NPM global installation (ARM Mac)
            if FileManager.default.fileExists(atPath: "/opt/homebrew/lib/node_modules/openclaw/skills") {
                paths.append("/opt/homebrew/lib/node_modules/openclaw/skills")
            }
            // NPM global installation (Intel Mac)
            if FileManager.default.fileExists(atPath: "/usr/local/lib/node_modules/openclaw/skills") {
                paths.append("/usr/local/lib/node_modules/openclaw/skills")
            }
            return paths
        case .opencode: return ["\(configHome)/opencode/skills"]
        case .pi: return ["\(home)/.pi/agent/skills"]
        case .agents: return ["\(home)/.agents/skills"]
        case .antigravity: return ["\(home)/.gemini/antigravity/skills"]
        case .claudeDesktop: return []
        case .custom: return []
        }
    }

    var globalRulePaths: [String] {
        let home = FileManager.default.homeDirectoryForCurrentUser.path
        switch self {
        case .cursor: return ["\(home)/.cursor/rules"]
        case .windsurf: return ["\(home)/.codeium/windsurf/memories", "\(home)/.windsurf/rules"]
        default: return []
        }
    }

    /// Whether the tool is actually installed on this machine.
    /// Checks for app bundles, CLI binaries, tool-specific config files,
    /// or known global skill locations that imply a real setup is present.
    var isInstalled: Bool {
        let fm = FileManager.default
        let home = fm.homeDirectoryForCurrentUser.path

        switch self {
        case .claude:
            return fm.fileExists(atPath: "\(home)/.claude/settings.json")
                || fm.fileExists(atPath: "\(home)/.claude/CLAUDE.md")
                || fm.fileExists(atPath: "\(home)/.claude/plugins/installed_plugins.json")
                || Self.cliBinaryExists("claude")
                || globalPaths.contains { fm.fileExists(atPath: $0) }
        case .cursor:
            return fm.fileExists(atPath: "/Applications/Cursor.app")
                || fm.fileExists(atPath: "\(home)/.cursor/argv.json")
                || globalPaths.contains { fm.fileExists(atPath: $0) }
        case .windsurf:
            return fm.fileExists(atPath: "/Applications/Windsurf.app")
                || fm.fileExists(atPath: "\(home)/.codeium/windsurf/argv.json")
                || globalPaths.contains { fm.fileExists(atPath: $0) }
                || globalRulePaths.contains { fm.fileExists(atPath: $0) }
        case .codex:
            return fm.fileExists(atPath: "\(home)/.codex/config.toml")
                || fm.fileExists(atPath: "\(home)/.codex/auth.json")
                || Self.cliBinaryExists("codex")
                || globalPaths.contains { fm.fileExists(atPath: $0) }
        case .amp:
            let configHome = ProcessInfo.processInfo.environment["XDG_CONFIG_HOME"]
                .flatMap { $0.isEmpty ? nil : $0 } ?? "\(home)/.config"
            return fm.fileExists(atPath: "\(configHome)/amp/config.json")
                || fm.fileExists(atPath: "\(configHome)/amp/settings.json")
                || Self.cliBinaryExists("amp")
                || globalPaths.contains { fm.fileExists(atPath: $0) }
        case .pi:
            return Self.cliBinaryExists("pi")
                || globalPaths.contains { fm.fileExists(atPath: $0) }
        case .copilot:
            return fm.fileExists(atPath: "\(home)/.copilot")
                || Self.cliBinaryExists("copilot")
                || globalPaths.contains { fm.fileExists(atPath: $0) }
        case .agents:
            return fm.fileExists(atPath: "\(home)/.agents/skills")
        case .antigravity:
            return Self.appBundleExists("Antigravity")
                || fm.fileExists(atPath: "\(home)/.antigravity")
                || Self.cliBinaryExists("antigravity")
                || globalPaths.contains { fm.fileExists(atPath: $0) }
        case .opencode:
            let configHome = ProcessInfo.processInfo.environment["XDG_CONFIG_HOME"]
                .flatMap { $0.isEmpty ? nil : $0 } ?? "\(home)/.config"
            return Self.appBundleExists("OpenCode")
                || fm.fileExists(atPath: "\(configHome)/opencode/opencode.json")
                || fm.fileExists(atPath: "\(configHome)/opencode/opencode.jsonc")
                || fm.fileExists(atPath: "\(home)/.local/share/opencode")
                || Self.cliBinaryExists("opencode")
                || globalPaths.contains { fm.fileExists(atPath: $0) }
        case .augment:
            return fm.fileExists(atPath: "\(home)/.augment")
                || Self.cliBinaryExists("augment")
                || globalPaths.contains { fm.fileExists(atPath: $0) }
        case .claudeDesktop:
            return Self.appBundleExists("Claude")
        case .openclaw:
            return fm.fileExists(atPath: "\(home)/.openclaw")
                || Self.cliBinaryExists("openclaw")
                || fm.fileExists(atPath: "/opt/homebrew/lib/node_modules/openclaw")
                || fm.fileExists(atPath: "/usr/local/lib/node_modules/openclaw")
                || globalPaths.contains { fm.fileExists(atPath: $0) }
        case .aider, .custom:
            return true
        }
    }

    private static func appBundleExists(_ name: String) -> Bool {
        let fm = FileManager.default
        let home = fm.homeDirectoryForCurrentUser.path
        let paths = [
            "/Applications/\(name).app",
            "\(home)/Applications/\(name).app",
        ]
        return paths.contains { fm.fileExists(atPath: $0) }
    }

    private static func cliBinaryExists(_ name: String) -> Bool {
        let fm = FileManager.default
        let home = fm.homeDirectoryForCurrentUser.path
        let paths = [
            "/usr/local/bin/\(name)",
            "/opt/homebrew/bin/\(name)",
            "\(home)/.local/bin/\(name)",
        ]
        for path in paths where fm.fileExists(atPath: path) {
            return true
        }
        let nvmDir = "\(home)/.nvm/versions/node"
        if let nodeDirs = try? fm.contentsOfDirectory(atPath: nvmDir) {
            for nodeDir in nodeDirs {
                if fm.fileExists(atPath: "\(nvmDir)/\(nodeDir)/bin/\(name)") { return true }
            }
        }
        return false
    }
}
```

## File: `Chops/Models/WizardTemplate.swift`
```
import Foundation

// MARK: - Wizard Template Type

/// Types of wizard templates for AI-assisted composition
enum WizardTemplateType: String, CaseIterable, Codable, Identifiable {
    case skill = "skill"
    case agent = "agent"
    case rule = "rule"

    var id: String { rawValue }

    var displayName: String {
        switch self {
        case .skill: "Skills"
        case .agent: "Agents"
        case .rule: "Rules"
        }
    }

    var fileName: String {
        "\(rawValue)-composer.md"
    }

    var icon: String {
        switch self {
        case .skill: "doc.text"
        case .agent: "person.crop.rectangle"
        case .rule: "list.bullet.rectangle"
        }
    }
}

// MARK: - Wizard Template

/// A wizard template with content and metadata
struct WizardTemplate: Identifiable, Equatable {
    var id: String { type.rawValue }
    let type: WizardTemplateType
    var content: String
    var lastModified: Date

    /// Render template with placeholders replaced
    func render(fileContent: String, userInstructions: String) -> String {
        content
            .replacingOccurrences(of: "{{file_content}}", with: fileContent)
            .replacingOccurrences(of: "{{user_instructions}}", with: userInstructions)
    }
}
```

## File: `Chops/Resources/Assets.xcassets/Contents.json`
```json
{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `Chops/Resources/Assets.xcassets/AccentColor.colorset/Contents.json`
```json
{
  "colors" : [
    {
      "color" : {
        "color-space" : "srgb",
        "components" : {
          "alpha" : "1.000",
          "blue" : "0.380",
          "green" : "0.820",
          "red" : "1.000"
        }
      },
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `Chops/Resources/Assets.xcassets/tool-amp.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "logo.svg",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  },
  "properties" : {
    "preserves-vector-representation" : true,
    "template-rendering-intent" : "template"
  }
}
```

## File: `Chops/Resources/Assets.xcassets/tool-antigravity.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "logo.svg",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  },
  "properties" : {
    "preserves-vector-representation" : true,
    "template-rendering-intent" : "template"
  }
}
```

## File: `Chops/Resources/Assets.xcassets/tool-augment.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "logo.svg",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  },
  "properties" : {
    "preserves-vector-representation" : true,
    "template-rendering-intent" : "template"
  }
}
```

## File: `Chops/Resources/Assets.xcassets/tool-claude.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "logo.svg",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  },
  "properties" : {
    "preserves-vector-representation" : true,
    "template-rendering-intent" : "template"
  }
}
```

## File: `Chops/Resources/Assets.xcassets/tool-codex.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "logo.svg",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  },
  "properties" : {
    "preserves-vector-representation" : true,
    "template-rendering-intent" : "template"
  }
}
```

## File: `Chops/Resources/Assets.xcassets/tool-copilot.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "logo.svg",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  },
  "properties" : {
    "preserves-vector-representation" : true,
    "template-rendering-intent" : "template"
  }
}
```

## File: `Chops/Resources/Assets.xcassets/tool-cursor.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "logo.svg",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  },
  "properties" : {
    "preserves-vector-representation" : true,
    "template-rendering-intent" : "template"
  }
}
```

## File: `Chops/Resources/Assets.xcassets/tool-openclaw.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "logo.svg",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  },
  "properties" : {
    "preserves-vector-representation" : true,
    "template-rendering-intent" : "original"
  }
}
```

## File: `Chops/Resources/Assets.xcassets/tool-opencode.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "logo.svg",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  },
  "properties" : {
    "preserves-vector-representation" : true,
    "template-rendering-intent" : "template"
  }
}
```

## File: `Chops/Resources/Assets.xcassets/tool-windsurf.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "logo.svg",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  },
  "properties" : {
    "preserves-vector-representation" : true,
    "template-rendering-intent" : "template"
  }
}
```

## File: `Chops/Services/AppLogger.swift`
```
import Foundation
import os

enum AppLogger {
    private static let subsystem = Bundle.main.bundleIdentifier ?? "com.shpigford.Chops"

    static let scanning = Logger(subsystem: subsystem, category: "scanning")
    static let fileIO = Logger(subsystem: subsystem, category: "fileIO")
    static let ui = Logger(subsystem: subsystem, category: "ui")
    static let settings = Logger(subsystem: subsystem, category: "settings")
}
```

## File: `Chops/Services/FileWatcher.swift`
```
import Foundation
import os

final class FileWatcher {
    private var sources: [DispatchSourceFileSystemObject] = []
    private var fileDescriptors: [Int32] = []
    private let callback: (String) -> Void
    private let queue = DispatchQueue(label: "com.shpigford.Chops.filewatcher", qos: .utility)
    private var debounceWorkItem: DispatchWorkItem?

    init(callback: @escaping (String) -> Void) {
        self.callback = callback
    }

    func watchDirectories(_ paths: [String]) {
        stopAll()
        for path in paths {
            guard FileManager.default.fileExists(atPath: path) else { continue }
            watchDirectory(path)
        }
    }

    private func watchDirectory(_ path: String) {
        let fd = open(path, O_EVTONLY)
        guard fd >= 0 else {
            AppLogger.fileIO.warning("Failed to watch: \(path)")
            return
        }
        fileDescriptors.append(fd)

        let source = DispatchSource.makeFileSystemObjectSource(
            fileDescriptor: fd,
            eventMask: [.write, .rename, .delete, .extend],
            queue: queue
        )

        source.setEventHandler { [weak self] in
            guard let self else { return }
            AppLogger.fileIO.debug("File change detected: \(path)")
            self.debouncedCallback(path)
        }

        source.setCancelHandler {
            close(fd)
        }

        source.resume()
        sources.append(source)
    }

    private func debouncedCallback(_ path: String) {
        debounceWorkItem?.cancel()
        let work = DispatchWorkItem { [weak self] in
            AppLogger.fileIO.notice("Triggering rescan after debounce")
            DispatchQueue.main.async {
                self?.callback(path)
            }
        }
        debounceWorkItem = work
        queue.asyncAfter(deadline: .now() + 0.5, execute: work)
    }

    func stopAll() {
        debounceWorkItem?.cancel()
        for source in sources {
            source.cancel()
        }
        sources.removeAll()
        fileDescriptors.removeAll()
    }

    deinit {
        stopAll()
    }
}
```

## File: `Chops/Services/SearchService.swift`
```
import Foundation
import SwiftData

enum SearchService {
    static func search(query: String, in context: ModelContext) -> [Skill] {
        guard !query.isEmpty else { return [] }

        let descriptor = FetchDescriptor<Skill>()
        guard let allSkills = try? context.fetch(descriptor) else { return [] }

        return allSkills.filter { skill in
            skill.name.localizedCaseInsensitiveContains(query) ||
            skill.skillDescription.localizedCaseInsensitiveContains(query) ||
            skill.content.localizedCaseInsensitiveContains(query)
        }
    }
}
```

## File: `Chops/Services/SkillParser.swift`
```
import Foundation

enum SkillParser {
    static func parse(fileURL: URL, toolSource: ToolSource) -> ParsedSkill? {
        guard let content = try? String(contentsOf: fileURL, encoding: .utf8) else {
            return nil
        }

        switch toolSource {
        case .claude, .claudeDesktop, .cursor:
            if fileURL.pathExtension == "mdc" {
                return MDCParser.parse(content)
            }
            return FrontmatterParser.parse(content)
        case .codex, .amp, .windsurf, .copilot, .aider, .openclaw, .opencode, .pi, .agents, .augment, .antigravity, .custom:
            // Try frontmatter first, fall back to heading
            let parsed = FrontmatterParser.parse(content)
            if !parsed.name.isEmpty { return parsed }
            return parseHeadingFormat(content)
        }
    }

    private static func parseHeadingFormat(_ content: String) -> ParsedSkill {
        let lines = content.components(separatedBy: "\n")
        var name = ""

        for line in lines {
            if line.hasPrefix("# ") {
                name = String(line.dropFirst(2)).trimmingCharacters(in: .whitespaces)
                break
            }
        }

        return ParsedSkill(
            frontmatter: [:],
            content: content,
            name: name,
            description: ""
        )
    }
}
```

## File: `Chops/Services/SkillRegistry.swift`
```
import Foundation

@Observable
final class SkillRegistry {
    var isSearching = false
    var searchError: String?

    // Cache repo trees and default branches to avoid repeated API calls
    private var treeCache: [String: [String]] = [:] // source -> [SKILL.md paths]
    private var branchCache: [String: String] = [:] // source -> default branch

    // MARK: - Search

    struct SearchResponse: Codable {
        let skills: [RegistrySkill]
        let count: Int
    }

    struct RegistrySkill: Identifiable, Codable {
        let id: String
        let skillId: String
        let name: String
        let installs: Int
        let source: String

        var formattedInstalls: String {
            if installs >= 1_000_000 {
                return "\(String(format: "%.1f", Double(installs) / 1_000_000).replacingOccurrences(of: ".0", with: ""))M"
            } else if installs >= 1_000 {
                return "\(String(format: "%.1f", Double(installs) / 1_000).replacingOccurrences(of: ".0", with: ""))K"
            }
            return "\(installs)"
        }
    }

    func search(query: String) async throws -> [RegistrySkill] {
        guard query.count >= 2 else { return [] }

        let encoded = query.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? query
        let url = URL(string: "https://skills.sh/api/search?q=\(encoded)&limit=30")!

        let (data, response) = try await URLSession.shared.data(from: url)
        guard let http = response as? HTTPURLResponse, http.statusCode == 200 else {
            throw RegistryError.searchFailed
        }

        let decoded = try JSONDecoder().decode(SearchResponse.self, from: data)
        return decoded.skills
    }

    // MARK: - Content Resolution

    func fetchContent(skill: RegistrySkill) async throws -> String {
        let branch = try await getDefaultBranch(source: skill.source)
        let paths = try await getSkillPaths(source: skill.source, branch: branch)

        // Try each SKILL.md path until we find one whose frontmatter name matches
        for path in paths {
            let rawURL = URL(string: "https://raw.githubusercontent.com/\(skill.source)/\(branch)/\(path)")!
            guard let (data, response) = try? await URLSession.shared.data(from: rawURL),
                  let http = response as? HTTPURLResponse, http.statusCode == 200,
                  let content = String(data: data, encoding: .utf8) else {
                continue
            }

            // Check if this SKILL.md's frontmatter name matches the skillId
            let frontmatterName = parseFrontmatterName(from: content)
            if frontmatterName == skill.skillId || frontmatterName == skill.name {
                return content
            }
        }

        throw RegistryError.skillNotFound
    }

    private func getDefaultBranch(source: String) async throws -> String {
        if let cached = branchCache[source] {
            return cached
        }

        let url = URL(string: "https://api.github.com/repos/\(source)")!
        let (data, response) = try await URLSession.shared.data(from: url)
        guard let http = response as? HTTPURLResponse, http.statusCode == 200 else {
            // Fall back to "main" if we can't determine default branch
            return "main"
        }

        struct RepoResponse: Codable {
            let default_branch: String
        }

        let repo = try JSONDecoder().decode(RepoResponse.self, from: data)
        branchCache[source] = repo.default_branch
        return repo.default_branch
    }

    private func getSkillPaths(source: String, branch: String) async throws -> [String] {
        if let cached = treeCache[source] {
            return cached
        }

        let url = URL(string: "https://api.github.com/repos/\(source)/git/trees/\(branch)?recursive=1")!
        let (data, response) = try await URLSession.shared.data(from: url)
        guard let http = response as? HTTPURLResponse else {
            throw RegistryError.treeFetchFailed
        }
        if http.statusCode == 403 {
            throw RegistryError.rateLimited
        }
        guard http.statusCode == 200 else {
            throw RegistryError.treeFetchFailed
        }

        struct TreeResponse: Codable {
            struct TreeEntry: Codable {
                let path: String
                let type: String
            }
            let tree: [TreeEntry]
        }

        let tree = try JSONDecoder().decode(TreeResponse.self, from: data)
        let skillPaths = tree.tree
            .filter { $0.type == "blob" && $0.path.hasSuffix("/SKILL.md") }
            .map(\.path)

        treeCache[source] = skillPaths
        return skillPaths
    }

    private func parseFrontmatterName(from content: String) -> String? {
        let lines = content.components(separatedBy: .newlines)
        guard lines.first?.trimmingCharacters(in: .whitespaces) == "---" else { return nil }

        for line in lines.dropFirst() {
            let trimmed = line.trimmingCharacters(in: .whitespaces)
            if trimmed == "---" { break }
            if trimmed.hasPrefix("name:") {
                return trimmed
                    .dropFirst(5)
                    .trimmingCharacters(in: .whitespaces)
                    .trimmingCharacters(in: CharacterSet(charactersIn: "\"'"))
            }
        }
        return nil
    }

    // MARK: - Install

    func install(content: String, skillName: String, agents: [AgentTarget]) throws {
        let sanitized = skillName
            .lowercased()
            .replacingOccurrences(of: " ", with: "-")
            .filter { $0.isLetter || $0.isNumber || $0 == "-" || $0 == "." || $0 == "_" }
            .trimmingCharacters(in: CharacterSet(charactersIn: ".-"))

        guard !sanitized.isEmpty else {
            throw RegistryError.invalidSkillName
        }

        let fm = FileManager.default
        let home = fm.homeDirectoryForCurrentUser.path

        // Canonical location — matches the official skills CLI behavior
        let canonicalDir = "\(home)/.agents/skills/\(sanitized)"
        let canonicalFile = "\(canonicalDir)/SKILL.md"
        let canonicalAlreadyExisted = fm.fileExists(atPath: canonicalFile)

        // Write real file to canonical location if not already there
        if !canonicalAlreadyExisted {
            try fm.createDirectory(atPath: canonicalDir, withIntermediateDirectories: true)
            try content.write(toFile: canonicalFile, atomically: true, encoding: .utf8)
        }

        // Symlink from each agent's skills dir to the canonical location
        var newLinks = 0
        for agent in agents {
            let agentDir = "\(agent.expandedSkillsDir)/\(sanitized)"

            // Skip if already installed (real file or symlink)
            if fm.fileExists(atPath: agentDir) { continue }

            // Create parent dir if needed
            try fm.createDirectory(atPath: agent.expandedSkillsDir, withIntermediateDirectories: true)

            // Create symlink to canonical dir
            try fm.createSymbolicLink(atPath: agentDir, withDestinationPath: canonicalDir)
            newLinks += 1
        }

        if newLinks == 0 && canonicalAlreadyExisted {
            throw RegistryError.skillAlreadyExists
        }
    }

    // MARK: - Errors

    enum RegistryError: LocalizedError {
        case searchFailed
        case treeFetchFailed
        case rateLimited
        case skillNotFound
        case invalidSkillName
        case skillAlreadyExists

        var errorDescription: String? {
            switch self {
            case .searchFailed: "Search request failed"
            case .treeFetchFailed: "Could not fetch repository contents"
            case .rateLimited: "GitHub API rate limit reached — try again in a few minutes"
            case .skillNotFound: "File not found in repository"
            case .invalidSkillName: "Invalid name"
            case .skillAlreadyExists: "Already installed for all selected targets"
            }
        }
    }
}
```

## File: `Chops/Services/SkillScanner.swift`
```
import Foundation
import SwiftData
import os

/// Data collected from the filesystem for a single skill, before SwiftData persistence.
struct ScannedSkillData: Sendable {
    let fileURL: URL
    let resolvedPath: String
    let toolSource: ToolSource
    let isDirectory: Bool
    let isGlobal: Bool
    let name: String
    let skillDescription: String
    let content: String
    let frontmatter: [String: String]
    let modDate: Date
    let fileSize: Int
    let kind: ItemKind
}

@Observable
final class SkillScanner {
    private let modelContext: ModelContext
    private var scanTask: Task<Void, Never>?
    private var scanGeneration = 0

    /// Filenames that are tool config/meta files, not skills.
    private static let ignoredFileNames: Set<String> = [
        "README.md",
        "README",
        "CLAUDE.md",
        "AGENTS.md",
        "AGENTS.override.md",
        "global_rules.md",
        "SYSTEM.md",
        "APPEND_SYSTEM.md",
        "LICENSE.md",
        "LICENSE",
        "CHANGELOG.md",
    ]

    private static func shouldIgnoreLooseMarkdownFile(named fileName: String) -> Bool {
        return ignoredFileNames.contains(fileName)
    }

    init(modelContext: ModelContext) {
        self.modelContext = modelContext
    }

    /// Project-level paths to probe inside each project directory
    private static let projectProbes: [(subpath: String, tool: ToolSource, kind: ItemKind)] = [
        (".claude/skills", .claude, .skill),
        (".claude/agents", .claude, .agent),
        (".cursor/skills", .cursor, .skill),
        (".cursor/rules", .cursor, .rule),
        (".cursor/agents", .cursor, .agent),
        (".codex/skills", .codex, .skill),
        (".codex/agents", .codex, .agent),
        (".windsurf/rules", .windsurf, .rule),
        (".github", .copilot, .skill),
        (".github/agents", .copilot, .agent),
        (".config/amp/skills", .amp, .skill),
        (".opencode/skills", .opencode, .skill),
    ]

    func scanAll() {
        let start = CFAbsoluteTimeGetCurrent()
        AppLogger.scanning.notice("Scan started")

        scanTask?.cancel()
        scanGeneration += 1
        let generation = scanGeneration
        let customPaths = UserDefaults.standard.stringArray(forKey: "customScanPaths") ?? []
        let includePlugins = ChopsSettings.includePluginSkills
        scanTask = Task.detached { [weak self] in
            let results = Self.collectAllSkills(customPaths: customPaths, includePlugins: includePlugins)
            guard !Task.isCancelled else { return }
            let elapsed = CFAbsoluteTimeGetCurrent() - start
            AppLogger.scanning.notice("File collection done: \(results.count) skills in \(String(format: "%.2f", elapsed))s")

            await MainActor.run {
                guard let self, self.scanGeneration == generation else { return }
                self.applyResults(results)
                let total = CFAbsoluteTimeGetCurrent() - start
                AppLogger.scanning.notice("Scan complete: \(results.count) skills applied in \(String(format: "%.2f", total))s")
            }
        }
    }

    /// Pure filesystem I/O — safe to run off main thread.
    private static func collectAllSkills(customPaths: [String], includePlugins: Bool) -> [ScannedSkillData] {
        var results: [ScannedSkillData] = []

        for tool in ToolSource.allCases where tool != .custom {
            guard !Task.isCancelled else { return results }
            guard tool.isInstalled else {
                continue
            }
            for path in tool.globalPaths {
                let url = URL(fileURLWithPath: path)
                collectFromDirectory(url, toolSource: tool, isGlobal: true, kind: .skill, into: &results)
            }
            for path in tool.globalAgentPaths {
                let url = URL(fileURLWithPath: path)
                collectFromDirectory(url, toolSource: tool, isGlobal: true, kind: .agent, into: &results)
            }
            for path in tool.globalRulePaths {
                let url = URL(fileURLWithPath: path)
                collectFromDirectory(url, toolSource: tool, isGlobal: true, kind: .rule, into: &results)
            }
        }

        if includePlugins {
            // CLI plugins (installed_plugins.json)
            if ToolSource.claude.isInstalled {
                collectFromCLIPlugins(into: &results)
            }
            // Claude Desktop/Cowork plugin skills
            if ToolSource.claudeDesktop.isInstalled {
                collectClaudeDesktopSkills(into: &results)
            }
        }

        for path in customPaths {
            guard !Task.isCancelled else { return results }
            collectFromCustomDirectory(URL(fileURLWithPath: path), into: &results)
        }

        return results
    }

    private static func collectFromCustomDirectory(_ directory: URL, into results: inout [ScannedSkillData]) {
        let fm = FileManager.default
        guard let projects = try? fm.contentsOfDirectory(
            at: directory,
            includingPropertiesForKeys: [.isDirectoryKey],
            options: [.skipsHiddenFiles]
        ) else { return }

        for project in projects {
            guard !Task.isCancelled else { return }
            var isDir: ObjCBool = false
            fm.fileExists(atPath: project.path, isDirectory: &isDir)
            guard isDir.boolValue else { continue }

            for probe in projectProbes {
                let probePath = project.appendingPathComponent(probe.subpath)
                guard fm.fileExists(atPath: probePath.path) else { continue }

                if probe.tool == .copilot && probe.kind == .skill {
                    let file = probePath.appendingPathComponent("copilot-instructions.md")
                    if fm.fileExists(atPath: file.path) {
                        if let data = collectSkillData(at: file, toolSource: .copilot, isDirectory: false, isGlobal: false, kind: probe.kind) {
                            results.append(data)
                        }
                    }
                } else {
                    collectFromDirectory(probePath, toolSource: probe.tool, isGlobal: false, kind: probe.kind, into: &results)
                }
            }
        }
    }

    private static func collectFromDirectory(_ directory: URL, toolSource: ToolSource, isGlobal: Bool, kind: ItemKind = .skill, into results: inout [ScannedSkillData]) {
        let fm = FileManager.default

        var isDir: ObjCBool = false
        guard fm.fileExists(atPath: directory.path, isDirectory: &isDir) else { return }

        guard isDir.boolValue else { return }

        // Enumerate through the resolved directory so symlinked directories are traversed.
        let resolvedDirectory = directory.resolvingSymlinksInPath()

        guard let contents = try? fm.contentsOfDirectory(
            at: resolvedDirectory,
            includingPropertiesForKeys: [.isDirectoryKey, .isSymbolicLinkKey, .contentModificationDateKey, .fileSizeKey],
            options: [.skipsHiddenFiles]
        ) else { return }

        // Track both bases so each entry can be remapped back to the canonical path for storage.
        let originalBase = directory.path
        let resolvedBase = resolvedDirectory.path

        for rawItem in contents {
            guard !Task.isCancelled else { return }
            // Remap to canonical path for storage; use rawItem for filesystem operations.
            let item: URL
            if originalBase != resolvedBase, rawItem.path.hasPrefix(resolvedBase + "/") {
                let suffix = String(rawItem.path.dropFirst(resolvedBase.count))
                item = URL(fileURLWithPath: originalBase + suffix)
            } else {
                item = rawItem
            }
            var itemIsDir: ObjCBool = false
            fm.fileExists(atPath: rawItem.path, isDirectory: &itemIsDir)

            if itemIsDir.boolValue {
                let skillFile = item.appendingPathComponent("SKILL.md")
                let agentsFile = item.appendingPathComponent("AGENTS.md")
                let rawSkillFile = rawItem.appendingPathComponent("SKILL.md")
                let rawAgentsFile = rawItem.appendingPathComponent("AGENTS.md")

                if fm.fileExists(atPath: rawSkillFile.path) {
                    if let data = collectSkillData(at: skillFile, toolSource: toolSource, isDirectory: true, isGlobal: isGlobal, kind: kind) {
                        results.append(data)
                    }
                } else if fm.fileExists(atPath: rawAgentsFile.path) {
                    if let data = collectSkillData(at: agentsFile, toolSource: toolSource, isDirectory: true, isGlobal: isGlobal, kind: kind) {
                        results.append(data)
                    }
                } else if kind == .agent, let agentFile = preferredAgentFile(in: rawItem) {
                    let remappedAgentFile = item.appendingPathComponent(agentFile.lastPathComponent)
                    if let data = collectSkillData(at: remappedAgentFile, toolSource: toolSource, isDirectory: true, isGlobal: isGlobal, kind: kind) {
                        results.append(data)
                    }
                }
            } else if item.pathExtension == "md" || item.pathExtension == "mdc" || item.pathExtension == "toml" {
                guard !shouldIgnoreLooseMarkdownFile(named: item.lastPathComponent) else { continue }
                if let data = collectSkillData(at: item, toolSource: toolSource, isDirectory: false, isGlobal: isGlobal, kind: kind) {
                    results.append(data)
                }
            }
        }
    }

    private static func preferredAgentFile(in directory: URL) -> URL? {
        let fm = FileManager.default
        guard let contents = try? fm.contentsOfDirectory(
            at: directory,
            includingPropertiesForKeys: [.isDirectoryKey],
            options: [.skipsHiddenFiles]
        ) else { return nil }

        let candidates = contents.filter { item in
            var isDir: ObjCBool = false
            fm.fileExists(atPath: item.path, isDirectory: &isDir)
            guard !isDir.boolValue else { return false }
            guard ["md", "mdc", "toml"].contains(item.pathExtension) else { return false }
            return !shouldIgnoreLooseMarkdownFile(named: item.lastPathComponent)
        }

        let directoryName = directory.lastPathComponent.lowercased()
        if let matchingFile = candidates.first(where: { $0.deletingPathExtension().lastPathComponent.lowercased() == directoryName }) {
            return matchingFile
        }

        if candidates.count == 1 {
            return candidates[0]
        }

        return nil
    }

    /// For Claude Desktop plugin paths, produce a canonical identity that strips volatile
    /// components (session IDs, version numbers). For all other tools, returns the normal
    /// symlink-resolved path. Same pattern as remote skills using `remote://` prefixes.
    private static func canonicalResolvedPath(for fileURL: URL, toolSource: ToolSource) -> String {
        let resolved = fileURL.resolvingSymlinksInPath().path
        let path = fileURL.path

        // CLI plugins: .../.claude/plugins/cache/<publisher>/<plugin>/<version>/skills/<skill>/SKILL.md
        if toolSource == .claude, let range = path.range(of: ".claude/plugins/cache/") {
            let after = String(path[range.upperBound...])
            let parts = after.components(separatedBy: "/")
            // parts: [publisher, plugin, version, "skills", skill, "SKILL.md"]
            guard parts.count >= 6, parts[3] == "skills" else { return resolved }
            return "claude-plugin:\(parts[0])/\(parts[1])/\(parts[4])"
        }

        guard toolSource == .claudeDesktop else { return resolved }

        // Local plugins: .../cowork_plugins/cache/<marketplace>/<plugin>/<version>/skills/<skill>/SKILL.md
        if let range = path.range(of: "cowork_plugins/cache/") {
            let after = String(path[range.upperBound...])
            let parts = after.components(separatedBy: "/")
            // parts: [marketplace, plugin, version, "skills", skill, "SKILL.md"]
            guard parts.count >= 6, parts[3] == "skills" else { return resolved }
            return "claude-desktop:cowork_plugins/\(parts[0])/\(parts[1])/\(parts[4])"
        }

        // Remote plugins: .../remote_cowork_plugins/<plugin-id>/skills/<skill>/SKILL.md
        if let range = path.range(of: "remote_cowork_plugins/") {
            let after = String(path[range.upperBound...])
            let parts = after.components(separatedBy: "/")
            // parts: [plugin-id, "skills", skill, "SKILL.md"]
            guard parts.count >= 4, parts[1] == "skills" else { return resolved }
            return "claude-desktop:remote_cowork_plugins/\(parts[0])/\(parts[2])"
        }

        return resolved
    }

    private static func isSyntheticLocalResolvedPath(_ resolvedPath: String) -> Bool {
        resolvedPath.hasPrefix("claude-plugin:") || resolvedPath.hasPrefix("claude-desktop:")
    }

    /// Read and parse a single skill file. Pure I/O, no SwiftData.
    private static func collectSkillData(at fileURL: URL, toolSource: ToolSource, isDirectory: Bool, isGlobal: Bool, kind: ItemKind = .skill) -> ScannedSkillData? {
        let fm = FileManager.default
        let resolved = canonicalResolvedPath(for: fileURL, toolSource: toolSource)

        // Resolve symlinks for the actual read — fileURL may be a remapped canonical path
        // that does not physically exist when a parent directory is a symlink.
        let physicalURL = fileURL.resolvingSymlinksInPath()
        guard let parsed = SkillParser.parse(fileURL: physicalURL, toolSource: toolSource) else {
            AppLogger.scanning.warning("Failed to parse: \(fileURL.path)")
            return nil
        }

        let attrs = try? fm.attributesOfItem(atPath: physicalURL.path)
        let modDate  = (attrs?[.modificationDate] as? Date) ?? .now
        let fileSize = (attrs?[.size] as? Int) ?? 0

        let name: String
        if !parsed.name.isEmpty {
            name = parsed.name
        } else if isDirectory {
            name = fileURL.deletingLastPathComponent().lastPathComponent
        } else {
            name = fileURL.deletingPathExtension().lastPathComponent
        }

        return ScannedSkillData(
            fileURL: fileURL,
            resolvedPath: resolved,
            toolSource: toolSource,
            isDirectory: isDirectory,
            isGlobal: isGlobal,
            name: name,
            skillDescription: parsed.description,
            content: parsed.content,
            frontmatter: parsed.frontmatter,
            modDate: modDate,
            fileSize: fileSize,
            kind: kind
        )
    }

    // MARK: - Claude Plugin Scanning

    /// Scan CLI plugins from ~/.claude/plugins/installed_plugins.json
    private static func collectFromCLIPlugins(into results: inout [ScannedSkillData]) {
        let fm = FileManager.default
        let home = fm.homeDirectoryForCurrentUser.path
        let jsonPath = "\(home)/.claude/plugins/installed_plugins.json"

        guard let data = fm.contents(atPath: jsonPath),
              let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
              let plugins = json["plugins"] as? [String: [[String: Any]]] else { return }

        for (_, installations) in plugins {
            guard !Task.isCancelled else { return }
            for installation in installations {
                guard let installPath = installation["installPath"] as? String else { continue }
                let skillsDir = URL(fileURLWithPath: installPath).appendingPathComponent("skills")
                collectFromDirectory(skillsDir, toolSource: .claude, isGlobal: true, into: &results)
            }
        }
    }

    /// Scan Claude Desktop/Cowork plugin skills using manifests as source of truth.
    /// Only scans explicitly installed plugins — skips built-in Anthropic skills (skills-plugin/).
    private static func collectClaudeDesktopSkills(into results: inout [ScannedSkillData]) {
        let fm = FileManager.default
        let home = fm.homeDirectoryForCurrentUser.path
        let sessionsRoot = "\(home)/Library/Application Support/Claude/local-agent-mode-sessions"

        guard fm.fileExists(atPath: sessionsRoot) else { return }
        guard let sessionDirs = try? fm.contentsOfDirectory(atPath: sessionsRoot) else { return }

        for sessionDir in sessionDirs {
            guard !Task.isCancelled else { return }
            // Skip skills-plugin (Anthropic built-in skills, not user-installed)
            if sessionDir == "skills-plugin" { continue }

            let sessionPath = "\(sessionsRoot)/\(sessionDir)"
            guard let subDirs = try? fm.contentsOfDirectory(atPath: sessionPath) else { continue }

            for subDir in subDirs {
                guard !Task.isCancelled else { return }
                let subPath = "\(sessionPath)/\(subDir)"

                // Local cowork plugins: use installed_plugins.json as source of truth
                let installedJson = "\(subPath)/cowork_plugins/installed_plugins.json"
                if let data = fm.contents(atPath: installedJson),
                   let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
                   let plugins = json["plugins"] as? [String: [[String: Any]]] {
                    for (_, installations) in plugins {
                        guard !Task.isCancelled else { return }
                        for installation in installations {
                            guard let installPath = installation["installPath"] as? String else { continue }
                            let skillsDir = URL(fileURLWithPath: installPath).appendingPathComponent("skills")
                            collectFromDirectory(skillsDir, toolSource: .claudeDesktop, isGlobal: true, into: &results)
                        }
                    }
                }

                // Remote cowork plugins: use manifest.json as source of truth
                let remoteDir = "\(subPath)/remote_cowork_plugins"
                let manifestPath = "\(remoteDir)/manifest.json"
                if let data = fm.contents(atPath: manifestPath),
                   let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
                   let plugins = json["plugins"] as? [[String: Any]] {
                    for plugin in plugins {
                        guard !Task.isCancelled else { return }
                        guard let pluginId = plugin["id"] as? String else { continue }
                        let skillsDir = "\(remoteDir)/\(pluginId)/skills"
                        guard fm.fileExists(atPath: skillsDir) else { continue }
                        collectFromDirectory(
                            URL(fileURLWithPath: skillsDir),
                            toolSource: .claudeDesktop,
                            isGlobal: true,
                            into: &results
                        )
                    }
                }
            }
        }
    }

    /// Apply collected results to SwiftData. Must be called on main thread.
    @MainActor
    private func applyResults(_ results: [ScannedSkillData]) {
        let groupedResults = Dictionary(grouping: results, by: \.resolvedPath)
        let descriptor = FetchDescriptor<Skill>()
        let allSkills = (try? modelContext.fetch(descriptor)) ?? []
        let localSkills = allSkills.filter { !$0.isRemote }
        let existingByResolved = Dictionary(uniqueKeysWithValues: localSkills.map { ($0.resolvedPath, $0) })
        let scannedResolvedPaths = Set(groupedResults.keys)

        for (resolvedPath, installations) in groupedResults {
            guard let primary = installations.first else { continue }

            let installedPaths = Array(Set(installations.map(\.fileURL.path))).sorted()
            let toolSources = ToolSource.allCases.filter { tool in
                installations.contains { $0.toolSource == tool }
            }

            if let existing = existingByResolved[resolvedPath] {
                let preferredPath = installedPaths.contains(existing.filePath) ? existing.filePath : primary.fileURL.path
                let preferredData = installations.first(where: { $0.fileURL.path == preferredPath }) ?? primary

                existing.filePath = preferredPath
                existing.isDirectory = preferredData.isDirectory
                existing.name = preferredData.name
                existing.skillDescription = preferredData.skillDescription
                existing.content = preferredData.content
                existing.frontmatter = preferredData.frontmatter
                existing.fileModifiedDate = preferredData.modDate
                existing.fileSize = preferredData.fileSize
                existing.isGlobal = preferredData.isGlobal
                existing.installedPaths = installedPaths
                existing.toolSources = toolSources
                existing.itemKind = preferredData.kind
            } else {
                let skill = Skill(
                    filePath: primary.fileURL.path,
                    toolSource: primary.toolSource,
                    isDirectory: primary.isDirectory,
                    name: primary.name,
                    skillDescription: primary.skillDescription,
                    content: primary.content,
                    frontmatter: primary.frontmatter,
                    fileModifiedDate: primary.modDate,
                    fileSize: primary.fileSize,
                    isGlobal: primary.isGlobal,
                    resolvedPath: primary.resolvedPath,
                    kind: primary.kind
                )
                skill.installedPaths = installedPaths
                skill.toolSources = toolSources
                modelContext.insert(skill)
            }
        }

        for skill in localSkills where !scannedResolvedPaths.contains(skill.resolvedPath) {
            modelContext.delete(skill)
        }

        do { try modelContext.save() } catch {
            AppLogger.scanning.error("SwiftData save failed: \(error.localizedDescription)")
        }
    }

    // MARK: - Remote Server Scanning

    @MainActor
    func syncAllRemoteServers() async {
        let descriptor = FetchDescriptor<RemoteServer>()
        guard let servers = try? modelContext.fetch(descriptor) else { return }
        for server in servers {
            await scanRemoteServer(server)
        }
    }

    /// Scans a remote server for skills. Sets lastSyncError on failure.
    @MainActor
    func scanRemoteServer(_ server: RemoteServer) async {
        do {
            let remoteSkills = try await SSHService.findSkills(server)
            var foundPaths = Set<String>()

            for (path, content) in remoteSkills {
                let resolvedPath = "remote://\(server.id)/\(path)"
                foundPaths.insert(resolvedPath)

                let parsed = FrontmatterParser.parse(content)
                let name: String
                if !parsed.name.isEmpty {
                    name = parsed.name
                } else {
                    // Derive name from parent directory
                    let components = path.components(separatedBy: "/")
                    if let fileIndex = components.lastIndex(of: "SKILL.md"), fileIndex > 0 {
                        name = components[fileIndex - 1]
                    } else {
                        name = "Unknown"
                    }
                }

                let predicate = #Predicate<Skill> { $0.resolvedPath == resolvedPath }
                let fetchDescriptor = FetchDescriptor<Skill>(predicate: predicate)

                if let existing = try? modelContext.fetch(fetchDescriptor).first {
                    existing.content = parsed.content
                    existing.name = name
                    existing.skillDescription = parsed.description
                    existing.frontmatter = parsed.frontmatter
                } else {
                    let skill = Skill(
                        filePath: resolvedPath,
                        toolSource: .openclaw,
                        isDirectory: true,
                        name: name,
                        skillDescription: parsed.description,
                        content: parsed.content,
                        frontmatter: parsed.frontmatter,
                        isGlobal: true,
                        resolvedPath: resolvedPath
                    )
                    skill.remoteServer = server
                    skill.remotePath = path
                    modelContext.insert(skill)
                }
            }

            // Remove skills that no longer exist on the server
            let serverID = server.id
            let remotePredicate = #Predicate<Skill> { $0.resolvedPath.starts(with: "remote://") }
            if let existingRemoteSkills = try? modelContext.fetch(FetchDescriptor<Skill>(predicate: remotePredicate)) {
                for skill in existingRemoteSkills {
                    guard skill.remoteServer?.id == serverID else { continue }
                    if !foundPaths.contains(skill.resolvedPath) {
                        modelContext.delete(skill)
                    }
                }
            }

            server.lastSyncDate = .now
            server.lastSyncError = nil
            do { try modelContext.save() } catch {
                AppLogger.scanning.error("SwiftData save failed after sync: \(error.localizedDescription)")
            }
        } catch {
            server.lastSyncError = error.localizedDescription
            do { try modelContext.save() } catch {
                AppLogger.scanning.error("SwiftData save failed after sync error: \(error.localizedDescription)")
            }
        }
    }

    @MainActor
    func removeDeletedSkills() {
        let descriptor = FetchDescriptor<Skill>()
        guard let skills = try? modelContext.fetch(descriptor) else { return }
        let fm = FileManager.default

        for skill in skills {
            // Remove orphaned remote skills (server was deleted)
            if skill.resolvedPath.hasPrefix("remote://") && skill.remoteServer == nil {
                modelContext.delete(skill)
                continue
            }

            // Remote skills are managed by scanRemoteServer(), skip here
            if skill.isRemote { continue }

            // Plugin skills use canonical IDs, not filesystem paths. Let applyResults()
            // handle their lifecycle so updates don't delete and recreate user metadata.
            if Self.isSyntheticLocalResolvedPath(skill.resolvedPath) { continue }

            // Remove previously-scanned loose markdown files that are now filtered out.
            let fileName = URL(fileURLWithPath: skill.filePath).lastPathComponent
            if !skill.isDirectory, Self.shouldIgnoreLooseMarkdownFile(named: fileName) {
                modelContext.delete(skill)
                continue
            }

            let validPaths = skill.installedPaths.filter { fm.fileExists(atPath: $0) }
            if validPaths.isEmpty {
                modelContext.delete(skill)
            } else {
                skill.installedPaths = validPaths
                if !fm.fileExists(atPath: skill.filePath), let first = validPaths.first {
                    skill.filePath = first
                }
            }
        }
        do { try modelContext.save() } catch {
            AppLogger.scanning.error("SwiftData save failed: \(error.localizedDescription)")
        }
    }

    deinit {
        scanTask?.cancel()
    }
}
```

## File: `Chops/Services/SSHService.swift`
```
import Foundation

enum SSHError: LocalizedError {
    case connectionFailed(String)
    case commandFailed(String)

    var errorDescription: String? {
        switch self {
        case .connectionFailed(let msg): "SSH connection failed: \(msg)"
        case .commandFailed(let msg): "SSH command failed: \(msg)"
        }
    }
}

enum SSHService {
    private static let sshPath = "/usr/bin/ssh"

    private static func baseArgs(for server: RemoteServer) -> [String] {
        let home = FileManager.default.homeDirectoryForCurrentUser.path
        var args = [
            "-p", "\(server.port)",
            "-o", "ConnectTimeout=10",
            "-o", "BatchMode=yes",
            "-o", "StrictHostKeyChecking=accept-new",
        ]

        if let keyPath = server.sshKeyPath, !keyPath.isEmpty {
            // User-specified key path (expand ~ if present)
            let resolved = keyPath.hasPrefix("~/")
                ? home + keyPath.dropFirst(1)
                : keyPath
            args += ["-i", resolved]
        } else {
            // Auto-discover common default key names
            let defaultKeys = ["id_ed25519", "id_rsa", "id_ecdsa"]
            for name in defaultKeys {
                let path = "\(home)/.ssh/\(name)"
                if FileManager.default.fileExists(atPath: path) {
                    args += ["-i", path]
                    break
                }
            }
        }

        args.append(server.sshDestination)
        return args
    }

    /// Escapes a string for safe use inside single quotes in a shell command.
    private static func shellEscape(_ value: String) -> String {
        "'" + value.replacingOccurrences(of: "'", with: "'\\''") + "'"
    }

    // MARK: - Public API

    static func testConnection(_ server: RemoteServer) async throws {
        let (_, stderr, code) = try await run(
            args: baseArgs(for: server) + ["echo", "ok"]
        )
        if code != 0 {
            throw SSHError.connectionFailed(stderr)
        }
    }

    /// Escapes a path for the remote shell, handling tilde expansion.
    /// Uses double quotes so `$HOME` expands while spaces are preserved.
    private static func shellQuotePath(_ path: String) -> String {
        var expanded = path
        if expanded.hasPrefix("~/") {
            expanded = "$HOME/" + expanded.dropFirst(2)
        } else if expanded == "~" {
            expanded = "$HOME"
        }
        // Double-quote: preserves $HOME expansion, protects spaces and globs
        let escaped = expanded.replacingOccurrences(of: "\"", with: "\\\"")
        return "\"\(escaped)\""
    }

    static func findSkills(_ server: RemoteServer) async throws -> [(path: String, content: String)] {
        let basePath = shellQuotePath(server.skillsBasePath)

        // Find all SKILL.md files under the base path
        let findCmd = "find \(basePath) -name 'SKILL.md' -type f 2>/dev/null"
        let (stdout, stderr, code) = try await run(
            args: baseArgs(for: server) + [findCmd]
        )

        if code != 0 {
            throw SSHError.connectionFailed(stderr.isEmpty ? "Connection failed (exit code \(code))" : stderr)
        }

        let paths = stdout.split(separator: "\n").map(String.init).filter { !$0.isEmpty }
        if paths.isEmpty { return [] }

        // Read all files in a single SSH call
        let catCmds = paths.map { "echo '---CHOPS_DELIM:\($0)---' && cat \(shellEscape($0))" }
        let combined = catCmds.joined(separator: " && ")
        let (content, _, _) = try await run(
            args: baseArgs(for: server) + [combined]
        )

        return parseDelimitedOutput(content)
    }

    static func readFile(_ server: RemoteServer, path: String) async throws -> String {
        let (stdout, stderr, code) = try await run(
            args: baseArgs(for: server) + ["cat \(shellEscape(path))"]
        )
        if code != 0 {
            throw SSHError.commandFailed(stderr)
        }
        return stdout
    }

    static func writeFile(_ server: RemoteServer, path: String, content: String) async throws {
        // Ensure parent directory exists, then write via stdin
        let escaped = shellEscape(path)
        let mkdirCmd = "mkdir -p \"$(dirname \(escaped))\" && cat > \(escaped)"
        let (_, stderr, code) = try await run(
            args: baseArgs(for: server) + [mkdirCmd],
            stdin: content
        )
        if code != 0 {
            throw SSHError.commandFailed(stderr)
        }
    }

    // MARK: - Private

    private static func run(args: [String], stdin stdinContent: String? = nil) async throws -> (stdout: String, stderr: String, exitCode: Int32) {
        try await withCheckedThrowingContinuation { continuation in
            DispatchQueue.global(qos: .userInitiated).async {
                let process = Process()
                process.executableURL = URL(fileURLWithPath: sshPath)
                process.arguments = args

                let stdoutPipe = Pipe()
                let stderrPipe = Pipe()
                process.standardOutput = stdoutPipe
                process.standardError = stderrPipe

                if let stdinContent {
                    let stdinPipe = Pipe()
                    process.standardInput = stdinPipe
                    let data = stdinContent.data(using: .utf8) ?? Data()
                    stdinPipe.fileHandleForWriting.write(data)
                    stdinPipe.fileHandleForWriting.closeFile()
                }

                do {
                    try process.run()
                    process.waitUntilExit()

                    let stdoutData = stdoutPipe.fileHandleForReading.readDataToEndOfFile()
                    let stderrData = stderrPipe.fileHandleForReading.readDataToEndOfFile()
                    let stdout = String(data: stdoutData, encoding: .utf8) ?? ""
                    let stderr = String(data: stderrData, encoding: .utf8) ?? ""

                    continuation.resume(returning: (stdout, stderr, process.terminationStatus))
                } catch {
                    continuation.resume(throwing: SSHError.connectionFailed(error.localizedDescription))
                }
            }
        }
    }

    private static func parseDelimitedOutput(_ output: String) -> [(path: String, content: String)] {
        var results: [(path: String, content: String)] = []
        let lines = output.components(separatedBy: "\n")
        var currentPath: String?
        var currentLines: [String] = []

        for line in lines {
            if line.hasPrefix("---CHOPS_DELIM:") && line.hasSuffix("---") {
                // Save previous block
                if let path = currentPath {
                    results.append((path: path, content: currentLines.joined(separator: "\n")))
                }
                // Extract path from delimiter
                let start = line.index(line.startIndex, offsetBy: 15)
                let end = line.index(line.endIndex, offsetBy: -3)
                currentPath = String(line[start..<end])
                currentLines = []
            } else {
                currentLines.append(line)
            }
        }

        // Save last block
        if let path = currentPath {
            results.append((path: path, content: currentLines.joined(separator: "\n")))
        }

        return results
    }
}
```

## File: `Chops/Services/TemplateManager.swift`
```
import Foundation

// MARK: - Template Manager

/// Manages wizard templates for AI-assisted composition
@Observable
@MainActor
final class TemplateManager {
    static let shared = TemplateManager()

    private(set) var templates: [WizardTemplate] = []

    private let fileManager = FileManager.default

    private var templatesDirectory: URL {
        let appSupport = fileManager.urls(for: .applicationSupportDirectory, in: .userDomainMask).first
            ?? fileManager.temporaryDirectory
        return appSupport.appendingPathComponent("Chops/templates", isDirectory: true)
    }

    private init() {
        ensureTemplatesExist()
        loadTemplates()
    }

    // MARK: - Public API

    /// Get template for a specific type
    func template(for type: WizardTemplateType) -> WizardTemplate? {
        templates.first { $0.type == type }
    }

    /// Build a context-aware system prompt for a given template type.
    /// Substitutes `{{skill_name}}`, `{{skill_description}}`, `{{file_path}}`,
    /// `{{frontmatter}}`, and `{{kind}}` from the supplied skill context.
    func systemPrompt(
        for type: WizardTemplateType,
        skillName: String,
        skillDescription: String,
        filePath: String,
        frontmatter: [String: String]
    ) -> String {
        let base = systemPromptContent(for: type)
        let frontmatterText = frontmatter.isEmpty
            ? "(none)"
            : frontmatter.sorted(by: { $0.key < $1.key })
                .map { "\($0.key): \($0.value)" }.joined(separator: "\n")
        return base
            .replacingOccurrences(of: "{{skill_name}}", with: skillName.isEmpty ? "(unnamed)" : skillName)
            .replacingOccurrences(of: "{{skill_description}}", with: skillDescription.isEmpty ? "(no description)" : skillDescription)
            .replacingOccurrences(of: "{{file_path}}", with: filePath)
            .replacingOccurrences(of: "{{frontmatter}}", with: frontmatterText)
            .replacingOccurrences(of: "{{kind}}", with: type.rawValue)
    }

    private func systemPromptContent(for type: WizardTemplateType) -> String {
        switch type {
        case .skill: Self.defaultSkillSystemPrompt
        case .agent: Self.defaultAgentSystemPrompt
        case .rule: Self.defaultRuleSystemPrompt
        }
    }

    /// Save updated template content
    func save(_ template: WizardTemplate, preserveVersionMarker: Bool = false) {
        let url = templatesDirectory.appendingPathComponent(template.type.fileName)
        let persistedContent = preserveVersionMarker ? template.content : stripVersionMarker(from: template.content)
        do {
            try persistedContent.write(to: url, atomically: true, encoding: .utf8)
            if let index = templates.firstIndex(where: { $0.type == template.type }) {
                templates[index] = WizardTemplate(
                    type: template.type,
                    content: persistedContent,
                    lastModified: Date()
                )
            }
        } catch {
            AppLogger.fileIO.error("Failed to save template: \(error.localizedDescription)")
        }
    }

    /// Reset a template to bundled default
    func resetToDefault(_ type: WizardTemplateType) {
        guard let bundledContent = loadBundledTemplate(type) else { return }
        let template = WizardTemplate(type: type, content: bundledContent, lastModified: Date())
        save(template, preserveVersionMarker: true)
    }

    /// Reset all templates to defaults
    func resetAllToDefaults() {
        for type in WizardTemplateType.allCases {
            resetToDefault(type)
        }
    }

    // MARK: - Private

    private func ensureTemplatesExist() {
        do {
            try fileManager.createDirectory(at: templatesDirectory, withIntermediateDirectories: true)
        } catch {
            AppLogger.fileIO.error("Failed to create templates dir: \(error.localizedDescription)")
        }

        // Write bundled templates on first run; overwrite outdated stored versions.
        for type in WizardTemplateType.allCases {
            let destURL = templatesDirectory.appendingPathComponent(type.fileName)
            guard let bundled = loadBundledTemplate(type) else { continue }

            let needsWrite: Bool
            if !fileManager.fileExists(atPath: destURL.path) {
                needsWrite = true
            } else if let stored = try? String(contentsOf: destURL, encoding: .utf8) {
                needsWrite = templateNeedsUpdate(stored: stored, bundled: bundled)
            } else {
                needsWrite = false
            }

            if needsWrite {
                do {
                    try bundled.write(to: destURL, atomically: true, encoding: .utf8)
                } catch {
                    AppLogger.fileIO.error("Failed to write template \(type.rawValue): \(error.localizedDescription)")
                }
            }
        }
    }

    /// Returns true when a stored template's version marker is older than the bundled version.
    /// Only auto-updates templates that still carry the default version header — user-customized
    /// templates that omit the marker are left untouched.
    private func templateNeedsUpdate(stored: String, bundled: String) -> Bool {
        guard let storedVersion = extractVersion(from: stored),
              let bundledVersion = extractVersion(from: bundled) else {
            return false
        }
        return storedVersion < bundledVersion
    }

    private func extractVersion(from content: String) -> Int? {
        let prefix = "<!-- chops-template-version: "
        guard let start = content.range(of: prefix),
              let end = content.range(of: " -->", range: start.upperBound ..< content.endIndex) else {
            return nil
        }
        return Int(content[start.upperBound ..< end.lowerBound])
    }

    private func stripVersionMarker(from content: String) -> String {
        content.replacingOccurrences(
            of: #"^<!-- chops-template-version: \d+ -->\n?"#,
            with: "",
            options: .regularExpression
        )
    }

    private func loadTemplates() {
        templates = WizardTemplateType.allCases.compactMap { type in
            let url = templatesDirectory.appendingPathComponent(type.fileName)
            guard let content = try? String(contentsOf: url, encoding: .utf8) else {
                return nil
            }
            let attrs = try? fileManager.attributesOfItem(atPath: url.path)
            let modified = attrs?[.modificationDate] as? Date ?? Date()
            return WizardTemplate(type: type, content: content, lastModified: modified)
        }
    }

    private func loadBundledTemplate(_ type: WizardTemplateType) -> String? {
        guard let url = Bundle.main.url(
            forResource: type.rawValue + "-composer",
            withExtension: "md",
            subdirectory: "Templates"
        ) else {
            return defaultTemplateContent(for: type)
        }
        return try? String(contentsOf: url, encoding: .utf8)
    }

    private func defaultTemplateContent(for type: WizardTemplateType) -> String {
        switch type {
        case .skill: Self.defaultSkillTemplate
        case .agent: Self.defaultAgentTemplate
        case .rule: Self.defaultRuleTemplate
        }
    }

    // MARK: - Default Templates

    private static let defaultSkillTemplate = """
    <!-- chops-template-version: 2 -->
    # Skill Composer

    You are helping create or improve a skill definition.

    ## Context
    - File type: Skill
    - Skills are reusable knowledge/instructions for AI assistants

    ## Current Content
    {{file_content}}

    ## User Instructions
    {{user_instructions}}

    ## Guidelines
    1. Use YAML frontmatter for metadata (name, description)
    2. Write clear, actionable instructions
    3. Include examples where helpful
    4. Keep scope focused and composable
    """


    // MARK: - Default Agent / Rule Templates

    private static let defaultAgentTemplate = """
    <!-- chops-template-version: 1 -->
    # Agent Composer

    You are helping create or improve an agent definition.

    ## Context
    - File type: Agent
    - Agents are specialized AI assistants with a defined role, tools, and behavior

    ## Current Content
    {{file_content}}

    ## User Instructions
    {{user_instructions}}

    ## Guidelines
    1. Use YAML frontmatter for metadata (name, description)
    2. Define a clear, focused role for the agent
    3. Specify which tools and capabilities the agent should use
    4. Keep instructions concise and unambiguous
    """

    private static let defaultRuleTemplate = """
    <!-- chops-template-version: 1 -->
    # Rule Composer

    You are helping create or improve a rule definition.

    ## Context
    - File type: Rule
    - Rules are persistent instructions applied across all interactions in a tool

    ## Current Content
    {{file_content}}

    ## User Instructions
    {{user_instructions}}

    ## Guidelines
    1. Use YAML frontmatter for metadata (name, description)
    2. Write rules as clear, imperative directives
    3. Keep scope narrow — one concern per rule
    4. Avoid contradictions with other rules
    """

    // MARK: - Default System Prompts

    private static let defaultSkillSystemPrompt = """
    You are an expert in writing skills for AI coding assistants that use the Model Context Protocol (MCP).

    ## Current skill context
    - Name: {{skill_name}}
    - Description: {{skill_description}}
    - File: {{file_path}}
    - Frontmatter:
    {{frontmatter}}

    ## Your role
    When the user asks you to create or update this skill, use the ACP `write_text_file` tool to write the complete updated file content directly to the file path shown above.
    Do not show the content in a code block or ask for confirmation — write it directly via `write_text_file`.
    Always write the full file, including YAML frontmatter.
    """

    private static let defaultAgentSystemPrompt = """
    You are an expert in writing agent definitions for AI coding assistants.

    ## Current agent context
    - Name: {{skill_name}}
    - Description: {{skill_description}}
    - File: {{file_path}}
    - Frontmatter:
    {{frontmatter}}

    ## Your role
    When the user asks you to create or update this agent, use the ACP `write_text_file` tool to write the complete updated file content directly to the file path shown above.
    Do not show the content in a code block or ask for confirmation — write it directly via `write_text_file`.
    Always write the full file, including YAML frontmatter.
    """

    private static let defaultRuleSystemPrompt = """
    You are an expert in writing rules for AI coding assistants.

    ## Current rule context
    - Name: {{skill_name}}
    - Description: {{skill_description}}
    - File: {{file_path}}
    - Frontmatter:
    {{frontmatter}}

    ## Your role
    When the user asks you to create or update this rule, use the ACP `write_text_file` tool to write the complete updated file content directly to the file path shown above.
    Do not show the content in a code block or ask for confirmation — write it directly via `write_text_file`.
    Always write the full file, including YAML frontmatter.
    """

}

```

## File: `Chops/Services/ACP/ACPAgentFactory.swift`
```
import Foundation

/// Returns the vendor-specific agent for a given registry agent ID.
/// Maps known agent IDs to their subclass; unknown agents use the base class.
@MainActor
enum ACPAgentFactory {
    static func make(for agentId: String) -> BaseACPAgent {
        switch agentId {
        case "claude-acp": return ClaudeACPAgent()
        case "cursor":     return CursorACPAgent()
        case "auggie":     return BaseACPAgent()
        default:           return BaseACPAgent()
        }
    }
}
```

## File: `Chops/Services/ACP/ACPClient.swift`
```
import ACP
import ACPModel
import ACPRegistry
import Foundation

// MARK: - Permission Request

struct PermissionRequest: Identifiable, @unchecked Sendable {
    let id: UUID = UUID()
    let title: String
    let options: [PermissionOption]
    let continuation: CheckedContinuation<RequestPermissionResponse, Error>
}

struct PendingWrite: Sendable {
    let path: String
    let content: String
    let originalText: String?
    let originalData: Data?
    let existedBefore: Bool
}

/// Base class for ACP agent interaction. Owns an `ACP.Client` actor and conforms to `ClientDelegate`.
/// Subclass to override vendor-specific hooks: additionalFlags, postProcess, conversationalText,
/// resolvePermission, and the onXxx stream callbacks.
@Observable
@MainActor
open class BaseACPAgent: ClientDelegate {

    // MARK: - Observable State

    var responseText: String = ""
    var thoughtText: String = ""
    var currentActivity: String?
    var pendingWrites: [PendingWrite] = []
    private(set) var sessionConfigOptions: [SessionConfigOption] = []
    private(set) var pendingPermissionRequest: PermissionRequest?
    private(set) var isConnected: Bool = false
    private(set) var isConnecting: Bool = false
    private(set) var isProcessing: Bool = false
    private(set) var lastError: String?
    private(set) var currentAgentId: String?

    // MARK: - Private Handles

    private var acpClient: ACP.Client?
    private var sessionId: SessionId?
    private var connectTask: Task<Void, Never>?
    private var notificationTask: Task<Void, Never>?
    private var pendingSystemPrompt: String?

    // MARK: - Connect / Disconnect

    /// Starts connecting non-blocking. Observe isConnecting / isConnected / lastError for state.
    func startConnect(agent: RegistryAgent, workingDirectory: URL, systemPrompt: String?) {
        connectTask?.cancel()
        lastError = nil
        connectTask = Task {
            defer { connectTask = nil }
            do {
                try await connect(agent: agent, workingDirectory: workingDirectory, systemPrompt: systemPrompt)
            } catch is CancellationError {
                // user-initiated — no error shown
            } catch {
                acpLog.error("Connection failed: \(error.localizedDescription)")
                lastError = error.localizedDescription
            }
        }
    }

    private func connect(agent: RegistryAgent, workingDirectory: URL, systemPrompt: String?) async throws {
        guard ACPConfiguration.shared.isEnabled(agent.id) else {
            throw ACPClientError.agentNotConfigured(agent.id)
        }
        currentAgentId = agent.id
        acpLog.debug("Resolving agent: \(agent.id) v\(agent.version)")
        let installed = try await ACPConfiguration.shared.resolve(agent)
        acpLog.debug("Resolved: \(installed.executablePath) args=[\(installed.arguments.joined(separator: " "))]")
        try await attemptConnect(installed: installed, workingDirectory: workingDirectory, systemPrompt: systemPrompt)
    }

    private func attemptConnect(installed: InstalledAgent, workingDirectory: URL, systemPrompt: String?) async throws {
        pendingSystemPrompt = systemPrompt
        isConnecting = true
        defer { isConnecting = false }

        let arguments = installed.arguments + additionalFlags()
        let environment = installed.environment.isEmpty ? nil : installed.environment

        let execPath = await resolveExecutable(installed.executablePath)
        acpLog.debug("launch: \(execPath) | args: \(arguments.joined(separator: " "))")

        let client = ACP.Client()
        await client.setDelegate(self)

        // SDK's ProcessManager loads the full login-shell environment internally.
        // Custom env from the registry (e.g. API keys) is merged on top by the SDK.
        try await client.launch(
            agentPath: execPath,
            arguments: arguments,
            workingDirectory: workingDirectory.path,
            environment: environment
        )
        guard !Task.isCancelled else { await client.terminate(); return }

        let initResp = try await client.initialize(
            capabilities: ClientCapabilities(
                fs: FileSystemCapabilities(readTextFile: true, writeTextFile: true),
                terminal: false
            ),
            clientInfo: ClientInfo(name: "Chops", version: "1.0")
        )
        guard !Task.isCancelled else { await client.terminate(); return }
        acpLog.debug("Connected: \(initResp.agentInfo?.name ?? "?") (protocol v\(initResp.protocolVersion))")

        let cwd = sessionCwd(for: workingDirectory)
        let sessionResp = try await client.newSession(workingDirectory: cwd.path)
        guard !Task.isCancelled else { await client.terminate(); return }
        sessionId = sessionResp.sessionId
        sessionConfigOptions = sessionResp.configOptions ?? []
        acpLog.debug("Session created: \(sessionResp.sessionId) (\(sessionConfigOptions.count) config options)")

        acpClient = client
        isConnected = true
        startNotificationMonitor(client: client)
    }

    func disconnect() async {
        connectTask?.cancel()
        connectTask = nil
        notificationTask?.cancel()
        notificationTask = nil
        // Resume any parked permission continuation before tearing down —
        // CheckedContinuation will crash if it is never resumed.
        if let req = pendingPermissionRequest {
            pendingPermissionRequest = nil
            req.continuation.resume(returning: RequestPermissionResponse(outcome: PermissionOutcome(cancelled: true)))
        }
        let client = acpClient
        acpClient = nil
        sessionId = nil
        isConnected = false
        currentAgentId = nil
        lastError = nil
        sessionConfigOptions = []
        pendingSystemPrompt = nil
        await client?.terminate()
        acpLog.debug("Disconnected")
    }

    // MARK: - Notification Monitor

    private func startNotificationMonitor(client: ACP.Client) {
        notificationTask?.cancel()
        notificationTask = Task.detached { [weak self] in
            let stream = await client.notifications
            for await notification in stream {
                guard !Task.isCancelled else { break }
                guard notification.method == "session/update" else { continue }
                await self?.handleRawNotification(notification)
            }
            // Stream ended — agent process likely exited
            await self?.onAgentDisconnected()
        }
    }

    private func onAgentDisconnected() {
        if isConnected {
            isConnected = false
            // Resume any parked permission continuation so it doesn't leak.
            if let req = pendingPermissionRequest {
                pendingPermissionRequest = nil
                req.continuation.resume(returning: RequestPermissionResponse(outcome: PermissionOutcome(cancelled: true)))
            }
            acpLog.debug("Agent process ended")
        }
    }

    private func handleRawNotification(_ notification: JSONRPCNotification) {
        guard let params = notification.params else { return }
        do {
            let data = try JSONEncoder().encode(params)
            struct SessionUpdateParams: Codable {
                let sessionId: String
                let update: SessionUpdate
            }
            let decoded = try JSONDecoder().decode(SessionUpdateParams.self, from: data)
            handleUpdate(decoded.update)
        } catch {
            acpLog.debug("Failed to decode session update: \(error)")
        }
    }

    // MARK: - Session

    func setConfigOption(id: SessionConfigId, value: SessionConfigValueId) async throws {
        guard let client = acpClient, let sid = sessionId else { return }
        let resp = try await client.setConfigOption(sessionId: sid, configId: id, value: value)
        sessionConfigOptions = resp.configOptions
    }

    // MARK: - Prompt

    func prompt(_ text: String) async throws {
        guard let client = acpClient, let sid = sessionId else { throw ACPClientError.noSession }
        responseText = ""; thoughtText = ""; pendingWrites = []; currentActivity = nil
        isProcessing = true
        defer { isProcessing = false }

        // Prepend system prompt context to the first message of the session.
        let fullText: String
        if let sp = pendingSystemPrompt {
            pendingSystemPrompt = nil
            fullText = sp.isEmpty ? text : "\(sp)\n\n---\n\n\(text)"
        } else {
            fullText = text
        }

        let resp = try await client.sendPrompt(
            sessionId: sid,
            content: [.text(TextContent(text: fullText))]
        )
        currentActivity = nil
        acpLog.debug("Prompt done: \(resp.stopReason)")
    }

    func clearPendingWrites() { pendingWrites = [] }

    /// Sends a session/cancel notification to the agent to interrupt the current turn.
    func cancelPrompt() {
        guard let client = acpClient, let sid = sessionId else { return }
        Task {
            do {
                try await client.cancelSession(sessionId: sid)
            } catch {
                acpLog.error("Cancel failed: \(error.localizedDescription)")
            }
        }
    }

    // MARK: - Permission

    func parkPermissionRequest(title: String, options: [PermissionOption]) async throws -> RequestPermissionResponse {
        try await withCheckedThrowingContinuation { cont in
            pendingPermissionRequest = PermissionRequest(title: title, options: options, continuation: cont)
        }
    }

    func respondToPermission(optionId: String?) {
        guard let req = pendingPermissionRequest else { return }
        pendingPermissionRequest = nil
        if let id = optionId {
            req.continuation.resume(returning: RequestPermissionResponse(outcome: PermissionOutcome(optionId: id)))
        } else {
            req.continuation.resume(returning: RequestPermissionResponse(outcome: PermissionOutcome(cancelled: true)))
        }
    }

    // MARK: - ClientDelegate

    public func handleFileReadRequest(_ path: String, sessionId: String, line: Int?, limit: Int?) async throws -> ReadTextFileResponse {
        acpLog.debug("readTextFile: \(path)")
        let content = try await Task.detached { try String(contentsOfFile: path, encoding: .utf8) }.value
        return ReadTextFileResponse(content: content)
    }

    public func handleFileWriteRequest(_ path: String, content: String, sessionId: String) async throws -> WriteTextFileResponse {
        acpLog.debug("Write via ACP: \(path)")
        // Read original before writing so reject can revert.
        // Skip if a diff block already captured this path (e.g. ClaudeACPAgent.captureDiffs).
        // Resolve symlinks on both sides so that e.g. a symlink path and its target compare equal.
        let resolvedIncoming = URL(fileURLWithPath: path).resolvingSymlinksInPath().path
        let alreadyCaptured = pendingWrites.contains {
            URL(fileURLWithPath: $0.path).resolvingSymlinksInPath().path == resolvedIncoming
        }
        if !alreadyCaptured {
            let snapshot = await Task.detached {
                let existedBefore = FileManager.default.fileExists(atPath: path)
                let originalData: Data?
                if existedBefore {
                    do {
                        originalData = try Data(contentsOf: URL(fileURLWithPath: path))
                    } catch {
                        acpLog.error("Failed to read original for diff revert (\(path)): \(error.localizedDescription)")
                        originalData = nil
                    }
                } else {
                    originalData = nil
                }
                return (existedBefore, originalData, Self.decodeText(from: originalData))
            }.value
            pendingWrites.append(
                PendingWrite(
                    path: path,
                    content: content,
                    originalText: snapshot.2,
                    originalData: snapshot.1,
                    existedBefore: snapshot.0
                )
            )
        }
        // Write to disk — agent expects the file to be persisted.
        try await Task.detached {
            let url = URL(fileURLWithPath: path)
            let parent = url.deletingLastPathComponent()
            if !FileManager.default.fileExists(atPath: parent.path) {
                try FileManager.default.createDirectory(at: parent, withIntermediateDirectories: true)
            }
            try content.write(to: url, atomically: true, encoding: .utf8)
        }.value
        return WriteTextFileResponse()
    }

    public func handleTerminalCreate(command: String, sessionId: String, args: [String]?, cwd: String?, env: [EnvVariable]?, outputByteLimit: Int?) async throws -> CreateTerminalResponse {
        throw ACPClientError.terminalNotSupported
    }

    public func handleTerminalOutput(terminalId: TerminalId, sessionId: String) async throws -> TerminalOutputResponse {
        throw ACPClientError.terminalNotSupported
    }

    public func handleTerminalWaitForExit(terminalId: TerminalId, sessionId: String) async throws -> WaitForExitResponse {
        throw ACPClientError.terminalNotSupported
    }

    public func handleTerminalKill(terminalId: TerminalId, sessionId: String) async throws -> KillTerminalResponse {
        throw ACPClientError.terminalNotSupported
    }

    public func handleTerminalRelease(terminalId: TerminalId, sessionId: String) async throws -> ReleaseTerminalResponse {
        throw ACPClientError.terminalNotSupported
    }

    public func handlePermissionRequest(request: RequestPermissionRequest) async throws -> RequestPermissionResponse {
        let title = request.message ?? "Permission Required"
        let options = request.options ?? []
        acpLog.debug("Permission: \(title)")
        return try await resolvePermission(title: title, options: options)
    }

    // MARK: - Session Update Dispatch

    func handleUpdate(_ update: SessionUpdate) {
        switch update {
        case .agentMessageChunk(let c):   onMessageChunk(c)
        case .agentThoughtChunk(let c):   onThoughtChunk(c)
        case .toolCall(let t):            onToolCall(t)
        case .toolCallUpdate(let d):      onToolCallUpdate(d)
        case .configOptionUpdate(let u):  sessionConfigOptions = u
        case .sessionInfoUpdate(let i):   if let t = i.title { acpLog.debug("Session: \(t)") }
        default:                          break
        }
    }

    // MARK: - Vendor Hooks (override in subclass)

    func onThoughtChunk(_ content: ContentBlock) {
        if case .text(let t) = content { currentActivity = String(t.text.prefix(80)) }
    }

    func onMessageChunk(_ content: ContentBlock) {
        if case .text(let t) = content { responseText += t.text }
    }

    func onToolCall(_ update: ToolCallUpdate) {
        currentActivity = (update.status == .completed || update.status == .failed) ? nil : update.title
    }

    func onToolCallUpdate(_ update: ToolCallUpdateDetails) {
        if let status = update.status, status == .completed || status == .failed {
            currentActivity = nil
        } else if let title = update.title {
            currentActivity = title
        }
    }

    func additionalFlags() -> [String] { [] }
    func sessionCwd(for workingDirectory: URL) -> URL { workingDirectory }
    func postProcess(_ text: String) -> String { text }
    func conversationalText(from text: String) -> String { postProcess(text) }

    func resolvePermission(title: String, options: [PermissionOption]) async throws -> RequestPermissionResponse {
        try await parkPermissionRequest(title: title, options: options)
    }

    // MARK: - Helpers

    /// Resolves a bare executable name (e.g. "npx") to its absolute path via the user's shell PATH.
    /// Returns the original name unchanged if it is already absolute or not found in PATH.
    private func resolveExecutable(_ name: String) async -> String {
        guard !name.hasPrefix("/") else { return name }
        let env = await ShellEnvironment.loadUserShellEnvironmentAsync()
        let dirs = (env["PATH"] ?? "").split(separator: ":").map(String.init)
        for dir in dirs {
            let full = (dir as NSString).appendingPathComponent(name)
            if FileManager.default.isExecutableFile(atPath: full) {
                acpLog.debug("Resolved '\(name)' to \(full)")
                return full
            }
        }
        acpLog.error("'\(name)' not found in PATH — launch will likely fail")
        return name
    }

    nonisolated static func decodeText(from data: Data?) -> String? {
        guard let data else { return nil }
        return String(data: data, encoding: .utf8)
            ?? String(data: data, encoding: .utf16)
    }
}

// MARK: - Errors

/// Chops-specific errors not covered by the SDK's errors.
enum ACPClientError: Error, LocalizedError {
    case agentNotConfigured(String)
    case noSession
    case terminalNotSupported

    var errorDescription: String? {
        switch self {
        case .agentNotConfigured(let id): "Agent '\(id)' not enabled. Go to Settings → ACP."
        case .noSession:                  "No active ACP session."
        case .terminalNotSupported:       "Terminal operations are not supported."
        }
    }
}
```

## File: `Chops/Services/ACP/ACPLogger.swift`
```
import Foundation
import os.log

/// Centralized ACP logging with optional debug mode and file storage
final class ACPLogger: @unchecked Sendable {
    static let shared = ACPLogger()

    private let osLog = Logger(subsystem: "md.chops", category: "ACP")
    private let logFileURL: URL
    private let queue = DispatchQueue(label: "md.chops.acplogger", qos: .utility)
    private static let isoFormatter = ISO8601DateFormatter()
    private var fileHandle: FileHandle?

    /// Enable verbose debug logging (send/receive payloads)
    var debugEnabled: Bool {
        get { UserDefaults.standard.bool(forKey: "ACPDebugLogging") }
        set {
            UserDefaults.standard.set(newValue, forKey: "ACPDebugLogging")
            if newValue {
                info("Debug logging enabled")
            }
        }
    }

    private init() {
        let appSupport = FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask).first
            ?? FileManager.default.temporaryDirectory
        let logsDir = appSupport.appendingPathComponent("Chops/Logs", isDirectory: true)
        try? FileManager.default.createDirectory(at: logsDir, withIntermediateDirectories: true)

        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "yyyy-MM-dd"
        let filename = "acp-\(dateFormatter.string(from: Date())).log"
        logFileURL = logsDir.appendingPathComponent(filename)

        if !FileManager.default.fileExists(atPath: logFileURL.path) {
            FileManager.default.createFile(atPath: logFileURL.path, contents: nil)
        }
        fileHandle = try? FileHandle(forWritingTo: logFileURL)
        fileHandle?.seekToEndOfFile()
    }

    deinit {
        try? fileHandle?.close()
    }

    // MARK: - Public API

    func info(_ message: String) {
        log(level: .info, message: message)
    }

    func debug(_ message: String) {
        guard debugEnabled else { return }
        log(level: .debug, message: message)
    }

    func error(_ message: String) {
        log(level: .error, message: message)
    }

    enum Direction { case send, receive }

    /// Log a JSON-encodable value in debug mode. Centralises encoding so callers never duplicate it.
    func debugLogJSON<T: Encodable>(_ value: T, direction: Direction) {
        guard debugEnabled else { return }
        guard let data = try? JSONEncoder().encode(value),
              let str = String(data: data, encoding: .utf8) else { return }
        switch direction {
        case .send:    log(level: .debug, message: ">>> SEND: \(str)")
        case .receive: log(level: .debug, message: "<<< RECV: \(str)")
        }
    }

    /// Get the log file URL for viewing
    var logURL: URL { logFileURL }

    /// Get recent log content — runs on the logger's background queue, never blocks the caller.
    func recentLogs(lines: Int = 200) async -> String {
        await withCheckedContinuation { continuation in
            queue.async { [self] in
                guard let data = try? Data(contentsOf: logFileURL),
                      let content = String(data: data, encoding: .utf8) else {
                    continuation.resume(returning: "(No logs available)")
                    return
                }
                let allLines = content.components(separatedBy: .newlines)
                let recentLines = allLines.suffix(lines)
                continuation.resume(returning: recentLines.joined(separator: "\n"))
            }
        }
    }

    /// Clear logs — truncates the file and writes a single marker entry.
    func clearLogs() {
        queue.async { [weak self] in
            guard let self else { return }
            try? self.fileHandle?.truncate(atOffset: 0)
            self.fileHandle?.seek(toFileOffset: 0)
            // Call log() directly on the queue to avoid an extra async hop.
            let timestamp = Self.isoFormatter.string(from: Date())
            let line = "[\(timestamp)] [INFO] Logs cleared\n"
            if let data = line.data(using: .utf8) {
                self.fileHandle?.write(data)
            }
            self.osLog.info("Logs cleared")
        }
    }

    // MARK: - Private

    private enum Level: String {
        case info = "INFO"
        case debug = "DEBUG"
        case error = "ERROR"
    }

    private func log(level: Level, message: String) {
        let timestamp = Self.isoFormatter.string(from: Date())
        let line = "[\(timestamp)] [\(level.rawValue)] \(message)\n"

        switch level {
        case .info: osLog.info("\(message)")
        case .debug: osLog.debug("\(message)")
        case .error: osLog.error("\(message)")
        }

        queue.async { [weak self] in
            if let data = line.data(using: .utf8) {
                self?.fileHandle?.write(data)
            }
        }
    }
}

// MARK: - Global convenience

let acpLog = ACPLogger.shared
```

## File: `Chops/Services/ACP/Agents/ClaudeACPAgent.swift`
```
import Foundation
import ACPModel

/// ACP agent for Claude Code.
///
/// Claude-specific stream classification:
/// - `agentThoughtChunk` → accumulates into `thoughtText`; shown in collapsible Thinking section.
/// - `agentMessageChunk` → accumulates raw into `responseText`; tag stripping applied at read time.
/// - `toolCall`          → activity label only; Claude does not embed diffs here.
/// - `toolCallUpdate`    → diffs captured from status-less updates; completed/failed clears activity.
@Observable
@MainActor
final class ClaudeACPAgent: BaseACPAgent {

    // MARK: - Tag Stripping

    /// Claude uses both bare and `antml:` namespaced variants of these tags.
    private static let tagsToStrip = [
        "function_calls", "invoke", "parameter", "thinking",
        "antml:function_calls", "antml:invoke", "antml:parameter"
    ]

    // MARK: - Content Hooks

    /// Thought chunks are Claude's extended-thinking / reasoning stream.
    /// Accumulated in full into `thoughtText` for display in a collapsible "Thinking" section.
    /// `currentActivity` is set to a short label so the activity row shows "Thinking…"
    /// rather than truncated reasoning mid-sentence.
    override func onThoughtChunk(_ content: ContentBlock) {
        currentActivity = "Thinking…"
        if case .text(let t) = content, !t.text.isEmpty {
            thoughtText += t.text
        }
    }

    /// Message chunks are Claude's conversational reply.
    /// Accumulated raw into `responseText` — postProcess (tag stripping) is applied at
    /// read time by `conversationalText()`, not per-chunk, to avoid splitting tags across chunks.
    override func onMessageChunk(_ content: ContentBlock) {
        if case .text(let t) = content {
            responseText += t.text
            acpLog.debug("onMessageChunk: +\(t.text.count) chars, total=\(responseText.count)")
        }
    }

    /// `toolCall` notifications from Claude carry no diff content — update activity label only.
    override func onToolCall(_ toolCall: ToolCallUpdate) {
        switch toolCall.status {
        case .completed, .failed:
            currentActivity = nil
        default:
            currentActivity = toolCall.title
        }
    }

    /// `toolCallUpdate` is Claude's primary diff delivery channel.
    ///
    /// Claude emits two distinct `tool_call_update` shapes for the `Write` tool:
    ///
    /// 1. **Status-less** — carries `content[{type:"diff", path, newText, oldText}]`.
    ///    This is the pre-write preview delivered before the file is touched on disk.
    ///    Diffs are captured here so `oldText` (or a disk read) is reliable.
    ///
    /// 2. **Status: completed/failed** — carries `rawOutput` but no diff content.
    ///    Used only to clear the activity label.
    ///
    /// `inProgress` updates carry a `title` to display while the tool is running.
    override func onToolCallUpdate(_ update: ToolCallUpdateDetails) {
        captureDiffs(from: update.content)

        guard let status = update.status else { return }
        switch status {
        case .completed, .failed:
            currentActivity = nil
            logToolResultContent(update.content)
        case .inProgress:
            if let title = update.title { currentActivity = title }
        default:
            break
        }
    }

    // MARK: - Diff Capture

    /// Extracts `ToolCallContent.diff` blocks and appends them to `pendingWrites`.
    /// Reading `oldText` here is safe — the diff block is delivered before Claude's
    /// write tool has touched the file on disk.
    private func captureDiffs(from content: [ToolCallContent]?) {
        guard let content else { return }
        for item in content {
            guard case .diff(let d) = item else { continue }
            let existedBefore = FileManager.default.fileExists(atPath: d.path)
            let oldData: Data? = if let oldText = d.oldText {
                oldText.data(using: .utf8)
            } else if existedBefore {
                try? Data(contentsOf: URL(fileURLWithPath: d.path))
            } else {
                nil
            }
            let oldText = d.oldText ?? BaseACPAgent.decodeText(from: oldData)
            // Replace any existing entry for this path — Claude may emit multiple diff blocks
            // for the same file (preview then final). The last one is the most current.
            let resolvedPath = URL(fileURLWithPath: d.path).resolvingSymlinksInPath().path
            if let existing = pendingWrites.firstIndex(where: {
                URL(fileURLWithPath: $0.path).resolvingSymlinksInPath().path == resolvedPath
            }) {
                pendingWrites[existing] = PendingWrite(
                    path: d.path,
                    content: d.newText,
                    originalText: pendingWrites[existing].originalText,
                    originalData: pendingWrites[existing].originalData,
                    existedBefore: pendingWrites[existing].existedBefore
                )
            } else {
                pendingWrites.append(
                    PendingWrite(
                        path: d.path,
                        content: d.newText,
                        originalText: oldText,
                        originalData: oldData,
                        existedBefore: existedBefore
                    )
                )
            }
            acpLog.info("diff intercepted: \(d.path) original=\(oldText?.count ?? -1) chars (\(pendingWrites.count) total)")
        }
    }

    // MARK: - Response Post-Processing

    override func postProcess(_ text: String) -> String {
        Self.stripXMLTags(text, tags: Self.tagsToStrip)
    }

    // MARK: - Private Helpers

    private static func stripXMLTags(_ text: String, tags: [String]) -> String {
        var result = text
        for tag in tags {
            for prefix in ["</\(tag)", "<\(tag)"] {
                var i = result.startIndex
                while i < result.endIndex,
                      let open = result.range(of: prefix, range: i ..< result.endIndex) {
                    // Search for closing '>' starting after the tag prefix, not from its start.
                    guard let close = result.range(of: ">", range: open.upperBound ..< result.endIndex) else {
                        // No closing '>' — malformed tag, advance past prefix to avoid infinite loop.
                        i = open.upperBound
                        continue
                    }
                    result.removeSubrange(open.lowerBound ... close.lowerBound)
                    i = open.lowerBound
                }
            }
        }
        // Collapse runs of 3+ consecutive newlines down to 2.
        result = result.replacingOccurrences(of: "\n{3,}", with: "\n\n", options: .regularExpression)
        return result.trimmingCharacters(in: .whitespacesAndNewlines)
    }

    private func logToolResultContent(_ content: [ToolCallContent]?) {
        content?.forEach {
            if case .content(let cc) = $0, case .text(let t) = cc {
                acpLog.debug("Tool result: \(String(t.text.prefix(200)))")
            }
        }
    }
}
```

## File: `Chops/Services/ACP/Agents/CursorACPAgent.swift`
```
import Foundation
import ACPModel

/// ACP agent for Cursor.
///
/// Cursor delivers conversational replies via `agentMessageChunk` with no XML wrapping.
/// Diffs arrive through `handleFileWriteRequest` in the base class.
@Observable
@MainActor
final class CursorACPAgent: BaseACPAgent {

    override func onThoughtChunk(_ content: ContentBlock) {}

    override func postProcess(_ text: String) -> String {
        return text.trimmingCharacters(in: .newlines)
    }
}
```

## File: `Chops/Utilities/FrontmatterParser.swift`
```
import Foundation

struct ParsedSkill {
    var frontmatter: [String: String]
    var content: String
    var name: String
    var description: String
}

enum FrontmatterParser {
    static func parse(_ text: String) -> ParsedSkill {
        let lines = text.components(separatedBy: "\n")

        guard lines.first?.trimmingCharacters(in: .whitespaces) == "---" else {
            return ParsedSkill(frontmatter: [:], content: text, name: "", description: "")
        }

        var endIndex: Int?
        for i in 1..<lines.count {
            if lines[i].trimmingCharacters(in: .whitespaces) == "---" {
                endIndex = i
                break
            }
        }

        guard let end = endIndex else {
            return ParsedSkill(frontmatter: [:], content: text, name: "", description: "")
        }

        var frontmatter: [String: String] = [:]
        for i in 1..<end {
            let line = lines[i]
            if let colonIndex = line.firstIndex(of: ":") {
                let key = String(line[line.startIndex..<colonIndex]).trimmingCharacters(in: .whitespaces)
                let value = String(line[line.index(after: colonIndex)...]).trimmingCharacters(in: .whitespaces)
                if !key.isEmpty {
                    frontmatter[key] = value
                }
            }
        }

        let contentStartIndex = min(end + 1, lines.count)
        let contentLines = Array(lines[contentStartIndex...])
        let content = contentLines.joined(separator: "\n").trimmingCharacters(in: .whitespacesAndNewlines)

        return ParsedSkill(
            frontmatter: frontmatter,
            content: content,
            name: frontmatter["name"] ?? "",
            description: frontmatter["description"] ?? ""
        )
    }
}
```

## File: `Chops/Utilities/MarkdownRenderer.swift`
```
import Foundation
import Highlightr
import JavaScriptCore
import cmark

enum MarkdownRenderer {
    static func renderHTML(_ markdown: String, isDarkMode: Bool) -> String {
        guard !markdown.isEmpty else { return "" }

        let len = markdown.utf8.count
        let options = Int32(CMARK_OPT_STRIKETHROUGH_DOUBLE_TILDE)

        guard let buf = cmark_gfm_markdown_to_html(markdown, len, options) else { return "" }
        let html = String(cString: buf)
        free(buf)

        return PreviewCodeHighlighter.shared.highlightCodeBlocks(in: html, isDarkMode: isDarkMode)
    }

    static func themeCSS(isDarkMode: Bool) -> String {
        PreviewCodeHighlighter.shared.themeCSS(isDarkMode: isDarkMode)
    }
}

private final class PreviewCodeHighlighter {
    static let shared = PreviewCodeHighlighter()

    private static let codeBlockRegex = try! NSRegularExpression(
        pattern: #"<pre([^>]*)><code(?: class="([^"]*)")?>([\s\S]*?)</code></pre>"#,
        options: []
    )

    private let bundle: Bundle?
    private let hljs: JSValue?
    private var cssCache: [String: String] = [:]

    private init() {
        self.bundle = Self.resourceBundle()

        guard let jsContext = JSContext(),
              let bundle,
              let highlightPath = bundle.path(forResource: "highlight.min", ofType: "js"),
              let highlightJS = try? String(contentsOfFile: highlightPath, encoding: .utf8) else {
            self.hljs = nil
            return
        }

        jsContext.evaluateScript(highlightJS)
        self.hljs = jsContext.objectForKeyedSubscript("hljs")
    }

    func highlightCodeBlocks(in html: String, isDarkMode: Bool) -> String {
        let nsHTML = html as NSString
        let matches = Self.codeBlockRegex.matches(in: html, range: NSRange(location: 0, length: nsHTML.length))

        guard !matches.isEmpty else { return html }

        var rendered = ""
        var currentLocation = 0

        for match in matches {
            let blockRange = match.range(at: 0)
            rendered += nsHTML.substring(with: NSRange(location: currentLocation, length: blockRange.location - currentLocation))

            let preAttributes = substring(in: nsHTML, range: match.range(at: 1))
            let classNames = substring(in: nsHTML, range: match.range(at: 2))
            let encodedCode = substring(in: nsHTML, range: match.range(at: 3)) ?? ""

            let language = languageName(classNames: classNames, preAttributes: preAttributes)
            let code = decodeHTML(encodedCode)

            if let highlighted = highlightedHTML(for: code, language: language, isDarkMode: isDarkMode) {
                rendered += highlighted
            } else {
                rendered += nsHTML.substring(with: blockRange)
            }

            currentLocation = blockRange.location + blockRange.length
        }

        rendered += nsHTML.substring(from: currentLocation)
        return rendered
    }

    func themeCSS(isDarkMode: Bool) -> String {
        let themeName = isDarkMode ? "atom-one-dark" : "atom-one-light"

        if let cached = cssCache[themeName] {
            return cached
        }

        guard let bundle,
              let themePath = bundle.path(forResource: themeName + ".min", ofType: "css"),
              let css = try? String(contentsOfFile: themePath, encoding: .utf8) else {
            return ""
        }

        cssCache[themeName] = css
        return css
    }

    private func highlightedHTML(for code: String, language: String?, isDarkMode: Bool) -> String? {
        guard let hljs else { return nil }

        let result: JSValue?
        if let language, !language.isEmpty {
            let highlighted = hljs.invokeMethod("highlight", withArguments: [language, code, false])
            if highlighted?.isUndefined == false {
                result = highlighted
            } else {
                result = hljs.invokeMethod("highlightAuto", withArguments: [code])
            }
        } else {
            result = hljs.invokeMethod("highlightAuto", withArguments: [code])
        }

        guard let html = result?.objectForKeyedSubscript("value")?.toString() else {
            return nil
        }

        let languageClass = language.map { " language-\($0)" } ?? ""
        let themeClass = isDarkMode ? "dark" : "light"

        return """
        <pre class="highlighted-code \(themeClass)"><code class="hljs\(languageClass)">\(html)</code></pre>
        """
    }

    private func languageName(classNames: String?, preAttributes: String?) -> String? {
        if let classNames {
            for className in classNames.split(separator: " ") {
                if className.hasPrefix("language-") {
                    return String(className.dropFirst("language-".count))
                }
                if className.hasPrefix("lang-") {
                    return String(className.dropFirst("lang-".count))
                }
            }
        }

        guard let preAttributes else { return nil }

        let pattern = #"lang="([^"]+)""#
        guard let regex = try? NSRegularExpression(pattern: pattern),
              let match = regex.firstMatch(in: preAttributes, range: NSRange(location: 0, length: (preAttributes as NSString).length)) else {
            return nil
        }

        return substring(in: preAttributes as NSString, range: match.range(at: 1))
    }

    private func substring(in string: NSString, range: NSRange) -> String? {
        guard range.location != NSNotFound else { return nil }
        return string.substring(with: range)
    }

    private func decodeHTML(_ string: String) -> String {
        string
            .replacingOccurrences(of: "&amp;", with: "&")
            .replacingOccurrences(of: "&lt;", with: "<")
            .replacingOccurrences(of: "&gt;", with: ">")
            .replacingOccurrences(of: "&quot;", with: "\"")
            .replacingOccurrences(of: "&#39;", with: "'")
    }

    private static func resourceBundle() -> Bundle? {
        let bundleName = "Highlightr_Highlightr"
        let overrides: [URL]

        if let override = ProcessInfo.processInfo.environment["PACKAGE_RESOURCE_BUNDLE_PATH"]
            ?? ProcessInfo.processInfo.environment["PACKAGE_RESOURCE_BUNDLE_URL"] {
            overrides = [URL(fileURLWithPath: override)]
        } else {
            overrides = []
        }

        let candidates = overrides + [
            Bundle.main.resourceURL,
            Bundle(for: ResourceBundleFinder.self).resourceURL,
            Bundle.main.bundleURL
        ]

        for candidate in candidates {
            let bundlePath = candidate?.appendingPathComponent(bundleName + ".bundle")
            if let bundle = bundlePath.flatMap(Bundle.init(url:)) {
                return bundle
            }
        }

        return nil
    }
}

private final class ResourceBundleFinder {}
```

## File: `Chops/Utilities/MDCParser.swift`
```
import Foundation

/// Parser for Cursor .mdc rule files.
/// MDC files use a frontmatter-like format with YAML between --- delimiters,
/// followed by markdown content.
enum MDCParser {
    static func parse(_ text: String) -> ParsedSkill {
        // MDC files use the same frontmatter format as SKILL.md
        FrontmatterParser.parse(text)
    }
}
```

## File: `Chops/Views/Detail/ChopsTextView.swift`
```
import AppKit

final class ChopsTextView: NSTextView {

    // MARK: - Cursor

    override func mouseMoved(with event: NSEvent) {
        // If another view (e.g. a floating button) is in front at this point, don't set the I-beam.
        if let hitView = window?.contentView?.hitTest(event.locationInWindow),
           hitView !== self, !(hitView is NSClipView) {
            return
        }
        super.mouseMoved(with: event)
    }

    override func didAddSubview(_ subview: NSView) {
        super.didAddSubview(subview)
        if let indicator = subview as? NSTextInsertionIndicator {
            indicator.displayMode = .hidden
        }
    }

    override func drawInsertionPoint(in rect: NSRect, color: NSColor, turnedOn flag: Bool) {
        var adjusted = rect
        adjusted.size.width = 2
        super.drawInsertionPoint(in: adjusted, color: color, turnedOn: flag)
    }

    override func setNeedsDisplay(_ rect: NSRect, avoidAdditionalLayout flag: Bool) {
        var rect = rect
        rect.size.width += 2
        super.setNeedsDisplay(rect, avoidAdditionalLayout: flag)
    }

    // MARK: - Find

    @objc func showFindPanel(_ sender: Any?) {
        let item = NSMenuItem()
        item.tag = Int(NSFindPanelAction.showFindPanel.rawValue)
        performFindPanelAction(item)
    }

    override func performKeyEquivalent(with event: NSEvent) -> Bool {
        guard event.modifierFlags.contains(.command) else {
            return super.performKeyEquivalent(with: event)
        }
        if event.charactersIgnoringModifiers == "f" {
            showFindPanel(nil)
            return true
        }
        return super.performKeyEquivalent(with: event)
    }

    // MARK: - Markdown Formatting

    @objc func toggleBold(_ sender: Any?) {
        wrapSelection(prefix: "**", suffix: "**", placeholder: "bold text")
    }

    @objc func toggleItalic(_ sender: Any?) {
        wrapSelection(prefix: "*", suffix: "*", placeholder: "italic text")
    }

    @objc func insertLink(_ sender: Any?) {
        let range = selectedRange()
        let selected = (string as NSString).substring(with: range)
        if selected.isEmpty {
            insertText("[link text](url)", replacementRange: range)
            let urlStart = range.location + "[link text](".utf16.count
            setSelectedRange(NSRange(location: urlStart, length: "url".utf16.count))
        } else {
            insertText("[\(selected)](url)", replacementRange: range)
            let urlStart = range.location + "[\(selected)](".utf16.count
            setSelectedRange(NSRange(location: urlStart, length: "url".utf16.count))
        }
    }

    @objc func insertHeading(_ sender: Any?) {
        let range = selectedRange()
        let lineRange = (string as NSString).lineRange(for: range)
        let line = (string as NSString).substring(with: lineRange)

        let trimmed = line.drop(while: { $0 == "#" || $0 == " " })
        let hashes = line.prefix(while: { $0 == "#" })

        let newLine: String
        switch hashes.count {
        case 0: newLine = "# \(trimmed)"
        case 1: newLine = "## \(trimmed)"
        case 2: newLine = "### \(trimmed)"
        default: newLine = String(trimmed)
        }

        insertText(newLine, replacementRange: lineRange)
    }

    @objc func toggleStrikethrough(_ sender: Any?) {
        wrapSelection(prefix: "~~", suffix: "~~", placeholder: "strikethrough text")
    }

    @objc func toggleBulletList(_ sender: Any?) {
        toggleLinePrefix(prefix: "- ", placeholder: "list item")
    }

    @objc func toggleNumberedList(_ sender: Any?) {
        let range = selectedRange()
        let selected = (string as NSString).substring(with: range)
        if selected.isEmpty {
            insertText("1. list item", replacementRange: range)
            let start = range.location + "1. ".utf16.count
            setSelectedRange(NSRange(location: start, length: "list item".utf16.count))
            return
        }
        let lineRange = (string as NSString).lineRange(for: range)
        let block = (string as NSString).substring(with: lineRange)
        let lines = block.components(separatedBy: "\n")
        var result: [String] = []
        var num = 1
        for line in lines {
            if line.isEmpty {
                result.append(line)
            } else {
                result.append("\(num). \(line)")
                num += 1
            }
        }
        insertText(result.joined(separator: "\n"), replacementRange: lineRange)
    }

    @objc func toggleTodoList(_ sender: Any?) {
        toggleLinePrefix(prefix: "- [ ] ", placeholder: "task")
    }

    @objc func toggleBlockquote(_ sender: Any?) {
        toggleLinePrefix(prefix: "> ", placeholder: "quote")
    }

    @objc func insertHorizontalRule(_ sender: Any?) {
        let range = selectedRange()
        insertText("\n\n---\n\n", replacementRange: range)
    }

    @objc func insertMarkdownTable(_ sender: Any?) {
        let range = selectedRange()
        let table = "| Column 1 | Column 2 | Column 3 |\n| --- | --- | --- |\n| Cell | Cell | Cell |"
        insertText(table, replacementRange: range)
    }

    @objc func toggleInlineCode(_ sender: Any?) {
        wrapSelection(prefix: "`", suffix: "`", placeholder: "code")
    }

    @objc func insertCodeBlock(_ sender: Any?) {
        let range = selectedRange()
        let selected = (string as NSString).substring(with: range)
        if selected.isEmpty {
            let snippet = "```\ncode\n```"
            insertText(snippet, replacementRange: range)
            let start = range.location + "```\n".utf16.count
            setSelectedRange(NSRange(location: start, length: "code".utf16.count))
        } else {
            insertText("```\n\(selected)\n```", replacementRange: range)
        }
    }

    // MARK: - Context Menu

    override func menu(for event: NSEvent) -> NSMenu? {
        let menu = super.menu(for: event) ?? NSMenu()

        let formatMenu = NSMenu(title: "Text Format")

        formatMenu.addItem(withTitle: "Headers", action: #selector(insertHeading(_:)), keyEquivalent: "")
        formatMenu.addItem(.separator())

        let boldItem = formatMenu.addItem(withTitle: "Bold", action: #selector(toggleBold(_:)), keyEquivalent: "b")
        boldItem.keyEquivalentModifierMask = .command
        let italicItem = formatMenu.addItem(withTitle: "Italic", action: #selector(toggleItalic(_:)), keyEquivalent: "i")
        italicItem.keyEquivalentModifierMask = .command
        let strikeItem = formatMenu.addItem(withTitle: "Strikethrough", action: #selector(toggleStrikethrough(_:)), keyEquivalent: "x")
        strikeItem.keyEquivalentModifierMask = [.command, .shift]
        formatMenu.addItem(.separator())

        formatMenu.addItem(withTitle: "Insert Link", action: #selector(insertLink(_:)), keyEquivalent: "")
        formatMenu.addItem(.separator())

        formatMenu.addItem(withTitle: "List", action: #selector(toggleBulletList(_:)), keyEquivalent: "")
        formatMenu.addItem(withTitle: "Ordered List", action: #selector(toggleNumberedList(_:)), keyEquivalent: "")
        formatMenu.addItem(withTitle: "Todo", action: #selector(toggleTodoList(_:)), keyEquivalent: "")
        formatMenu.addItem(.separator())

        formatMenu.addItem(withTitle: "Quote", action: #selector(toggleBlockquote(_:)), keyEquivalent: "")
        formatMenu.addItem(withTitle: "Horizontal Rule", action: #selector(insertHorizontalRule(_:)), keyEquivalent: "")
        formatMenu.addItem(withTitle: "Table", action: #selector(insertMarkdownTable(_:)), keyEquivalent: "")
        formatMenu.addItem(.separator())

        formatMenu.addItem(withTitle: "Code", action: #selector(toggleInlineCode(_:)), keyEquivalent: "")
        formatMenu.addItem(withTitle: "Code Block", action: #selector(insertCodeBlock(_:)), keyEquivalent: "")

        let formatItem = NSMenuItem(title: "Text Format", action: nil, keyEquivalent: "")
        formatItem.submenu = formatMenu

        menu.insertItem(.separator(), at: 0)
        menu.insertItem(formatItem, at: 0)

        return menu
    }

    // MARK: - Helpers

    private func toggleLinePrefix(prefix: String, placeholder: String) {
        let range = selectedRange()
        let selected = (string as NSString).substring(with: range)
        if selected.isEmpty {
            let text = "\(prefix)\(placeholder)"
            insertText(text, replacementRange: range)
            let start = range.location + prefix.utf16.count
            setSelectedRange(NSRange(location: start, length: placeholder.utf16.count))
            return
        }
        let lineRange = (string as NSString).lineRange(for: range)
        let block = (string as NSString).substring(with: lineRange)
        let lines = block.components(separatedBy: "\n")
        let result = lines.map { $0.isEmpty ? $0 : "\(prefix)\($0)" }
        insertText(result.joined(separator: "\n"), replacementRange: lineRange)
    }

    private func wrapSelection(prefix: String, suffix: String, placeholder: String) {
        let range = selectedRange()
        let selected = (string as NSString).substring(with: range)
        if selected.isEmpty {
            let text = "\(prefix)\(placeholder)\(suffix)"
            insertText(text, replacementRange: range)
            let placeholderStart = range.location + prefix.utf16.count
            setSelectedRange(NSRange(location: placeholderStart, length: placeholder.utf16.count))
        } else {
            let text = "\(prefix)\(selected)\(suffix)"
            insertText(text, replacementRange: range)
        }
    }
}
```

## File: `Chops/Views/Detail/EditorTheme.swift`
```
import AppKit

enum EditorTheme {
    // MARK: - Editor Font

    static let editorFontSize: CGFloat = 13
    static let editorFont = NSFont.monospacedSystemFont(ofSize: editorFontSize, weight: .regular)

    // MARK: - Margins

    static let editorInsetX: CGFloat = 48
    static let editorInsetTop: CGFloat = 12

    // MARK: - Line Spacing

    static let lineSpacing: CGFloat = 6

    static var editorLineHeight: CGFloat {
        let font = editorFont
        return ceil(font.ascender - font.descender + font.leading) + lineSpacing
    }

    static var editorBaselineOffset: CGFloat {
        let font = editorFont
        let naturalHeight = ceil(font.ascender - font.descender + font.leading)
        return (editorLineHeight - naturalHeight) / 2
    }

    // MARK: - Dynamic Colors

    static let textColor = NSColor(name: "editorText") { appearance in
        appearance.isDark
            ? NSColor(red: 0.878, green: 0.878, blue: 0.878, alpha: 1)
            : NSColor(red: 0.133, green: 0.133, blue: 0.133, alpha: 1)
    }

    static let syntaxColor = NSColor(name: "editorSyntax") { appearance in
        appearance.isDark
            ? NSColor(red: 0.45, green: 0.45, blue: 0.45, alpha: 1)
            : NSColor(red: 0.6, green: 0.6, blue: 0.6, alpha: 1)
    }

    static let headingColor = NSColor(name: "editorHeading") { appearance in
        appearance.isDark
            ? NSColor(red: 0.95, green: 0.95, blue: 0.95, alpha: 1)
            : NSColor(red: 0.1, green: 0.1, blue: 0.1, alpha: 1)
    }

    static let boldColor = NSColor(name: "editorBold") { appearance in
        appearance.isDark
            ? NSColor(red: 0.9, green: 0.9, blue: 0.9, alpha: 1)
            : NSColor(red: 0.15, green: 0.15, blue: 0.15, alpha: 1)
    }

    static let italicColor = NSColor(name: "editorItalic") { appearance in
        appearance.isDark
            ? NSColor(red: 0.8, green: 0.8, blue: 0.8, alpha: 1)
            : NSColor(red: 0.25, green: 0.25, blue: 0.25, alpha: 1)
    }

    static let codeColor = NSColor(name: "editorCode") { appearance in
        appearance.isDark
            ? NSColor(red: 0.9, green: 0.45, blue: 0.45, alpha: 1)
            : NSColor(red: 0.75, green: 0.2, blue: 0.2, alpha: 1)
    }

    static let linkColor = NSColor(name: "editorLink") { appearance in
        appearance.isDark
            ? NSColor(red: 0.4, green: 0.6, blue: 0.9, alpha: 1)
            : NSColor(red: 0.2, green: 0.4, blue: 0.7, alpha: 1)
    }

    static let blockquoteColor = NSColor(name: "editorBlockquote") { appearance in
        appearance.isDark
            ? NSColor(red: 0.6, green: 0.6, blue: 0.6, alpha: 1)
            : NSColor(red: 0.4, green: 0.4, blue: 0.4, alpha: 1)
    }

    static let frontmatterColor = NSColor(name: "editorFrontmatter") { appearance in
        appearance.isDark
            ? NSColor(red: 0.55, green: 0.55, blue: 0.65, alpha: 1)
            : NSColor(red: 0.35, green: 0.35, blue: 0.5, alpha: 1)
    }
}

extension NSAppearance {
    var isDark: Bool {
        bestMatch(from: [.darkAqua, .aqua]) == .darkAqua
    }
}
```

## File: `Chops/Views/Detail/MarkdownSyntaxHighlighter.swift`
```
import AppKit

final class MarkdownSyntaxHighlighter: NSObject {

    private var isHighlighting = false

    // MARK: - Regex Patterns

    private static let frontmatterKeyRegex: NSRegularExpression? = try? NSRegularExpression(
        pattern: "^([\\w][\\w\\s.-]*)(:)",
        options: .anchorsMatchLines
    )

    private static let patterns: [(NSRegularExpression, HighlightStyle)] = {
        var result: [(NSRegularExpression, HighlightStyle)] = []

        func add(_ pattern: String, _ style: HighlightStyle, options: NSRegularExpression.Options = []) {
            if let regex = try? NSRegularExpression(pattern: pattern, options: options) {
                result.append((regex, style))
            }
        }

        // Frontmatter (--- ... ---) at very start of file
        add("\\A---[ \\t]*\\n([\\s\\S]*?)\\n---[ \\t]*(?:\\n|\\z)", .frontmatter)

        // Fenced code blocks (``` ... ```)
        add("^(`{3,})(.*?)\\n([\\s\\S]*?)^\\1\\s*$", .codeBlock, options: .anchorsMatchLines)

        // Headings: # Heading
        add("^(#{1,6}\\s+)(.+)$", .heading, options: .anchorsMatchLines)

        // Bold: **text** or __text__
        add("(\\*\\*|__)(.+?)(\\1)", .bold)

        // Italic: *text* or _text_
        add("(?<![\\w*])(\\*|_)(?!\\s)(.+?)(?<!\\s)\\1(?![\\w*])", .italic)

        // Strikethrough: ~~text~~
        add("(~~)(.+?)(~~)", .strikethrough)

        // Inline code: `code`
        add("(`+)(.+?)(\\1)", .inlineCode)

        // Links: [text](url)
        add("(\\[)(.+?)(\\]\\(.+?\\))", .link)

        // Blockquotes: > text
        add("^(>+\\s?)(.*)$", .blockquote, options: .anchorsMatchLines)

        // Unordered list markers: - or * or +
        add("^(\\s*[-*+]\\s)", .listMarker, options: .anchorsMatchLines)

        // Ordered list markers: 1.
        add("^(\\s*\\d+\\.\\s)", .listMarker, options: .anchorsMatchLines)

        // Task list: - [ ] or - [x]
        add("^(\\s*[-*+]\\s\\[[ xX]\\]\\s)", .listMarker, options: .anchorsMatchLines)

        // Horizontal rule
        add("^([-*_]{3,})\\s*$", .syntax, options: .anchorsMatchLines)

        return result
    }()

    // MARK: - Highlight Styles

    private enum HighlightStyle {
        case heading
        case bold
        case italic
        case strikethrough
        case inlineCode
        case codeBlock
        case link
        case blockquote
        case listMarker
        case syntax
        case frontmatter
    }

    // MARK: - Highlighting

    func highlightAll(_ textStorage: NSTextStorage) {
        guard !isHighlighting else { return }
        isHighlighting = true
        defer { isHighlighting = false }

        textStorage.beginEditing()
        let fullRange = NSRange(location: 0, length: textStorage.length)
        let text = textStorage.string

        // Reset to default style
        let paragraph = NSMutableParagraphStyle()
        paragraph.minimumLineHeight = EditorTheme.editorLineHeight
        paragraph.maximumLineHeight = EditorTheme.editorLineHeight

        textStorage.setAttributes([
            .font: EditorTheme.editorFont,
            .foregroundColor: EditorTheme.textColor,
            .paragraphStyle: paragraph,
            .baselineOffset: EditorTheme.editorBaselineOffset
        ], range: fullRange)

        // Track code/frontmatter block ranges to skip inner highlighting
        var codeBlockRanges: [NSRange] = []

        for (regex, style) in Self.patterns {
            regex.enumerateMatches(in: text, range: fullRange) { match, _, _ in
                guard let match = match else { return }

                // Skip if inside a protected block (unless this IS a protected block pattern)
                if style != .codeBlock && style != .frontmatter {
                    let matchRange = match.range
                    if codeBlockRanges.contains(where: { NSIntersectionRange($0, matchRange).length > 0 }) {
                        return
                    }
                }

                switch style {
                case .heading:
                    if match.numberOfRanges >= 3 {
                        let syntaxRange = match.range(at: 1)
                        let contentRange = match.range(at: 2)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: syntaxRange)
                        textStorage.addAttributes([
                            .foregroundColor: EditorTheme.headingColor,
                            .font: NSFont.monospacedSystemFont(ofSize: EditorTheme.editorFontSize + 4, weight: .bold)
                        ], range: contentRange)
                    }

                case .bold:
                    if match.numberOfRanges >= 4 {
                        let openRange = match.range(at: 1)
                        let contentRange = match.range(at: 2)
                        let closeRange = match.range(at: 3)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: openRange)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: closeRange)
                        textStorage.addAttributes([
                            .foregroundColor: EditorTheme.boldColor,
                            .font: NSFont.monospacedSystemFont(ofSize: EditorTheme.editorFontSize, weight: .bold)
                        ], range: contentRange)
                    }

                case .italic:
                    if match.numberOfRanges >= 3 {
                        let syntaxRange = match.range(at: 1)
                        let contentRange = match.range(at: 2)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: syntaxRange)
                        let closingStart = match.range(at: 2).upperBound
                        let closingRange = NSRange(location: closingStart, length: match.range(at: 1).length)
                        if closingRange.upperBound <= textStorage.length {
                            textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: closingRange)
                        }
                        let italicFont = NSFontManager.shared.convert(EditorTheme.editorFont, toHaveTrait: .italicFontMask)
                        textStorage.addAttributes([
                            .foregroundColor: EditorTheme.italicColor,
                            .font: italicFont
                        ], range: contentRange)
                    }

                case .strikethrough:
                    if match.numberOfRanges >= 4 {
                        let openRange = match.range(at: 1)
                        let contentRange = match.range(at: 2)
                        let closeRange = match.range(at: 3)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: openRange)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: closeRange)
                        textStorage.addAttributes([
                            .strikethroughStyle: NSUnderlineStyle.single.rawValue,
                            .foregroundColor: EditorTheme.syntaxColor
                        ], range: contentRange)
                    }

                case .inlineCode:
                    if match.numberOfRanges >= 4 {
                        let openRange = match.range(at: 1)
                        let contentRange = match.range(at: 2)
                        let closeRange = match.range(at: 3)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: openRange)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: closeRange)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.codeColor, range: contentRange)
                    }

                case .codeBlock:
                    codeBlockRanges.append(match.range)
                    textStorage.addAttribute(.foregroundColor, value: EditorTheme.codeColor, range: match.range)
                    if match.numberOfRanges >= 2 {
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: match.range(at: 1))
                    }

                case .link:
                    if match.numberOfRanges >= 4 {
                        let bracketRange = match.range(at: 1)
                        let textRange = match.range(at: 2)
                        let urlPartRange = match.range(at: 3)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: bracketRange)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.linkColor, range: textRange)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: urlPartRange)
                    }

                case .blockquote:
                    if match.numberOfRanges >= 3 {
                        let markerRange = match.range(at: 1)
                        let contentRange = match.range(at: 2)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: markerRange)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.blockquoteColor, range: contentRange)
                    }

                case .listMarker:
                    textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: match.range)

                case .syntax:
                    textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: match.range)

                case .frontmatter:
                    guard matchedText(text, range: match.range).hasPrefix("---") else { return }
                    codeBlockRanges.append(match.range)
                    let nsText = text as NSString
                    textStorage.addAttribute(.foregroundColor, value: EditorTheme.frontmatterColor, range: match.range)
                    // Color the opening --- delimiter
                    let openLineEnd = nsText.range(of: "\n", range: NSRange(location: match.range.location, length: match.range.length))
                    if openLineEnd.location != NSNotFound {
                        let openRange = NSRange(location: match.range.location, length: openLineEnd.location - match.range.location)
                        textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: openRange)
                    }
                    // Color the closing --- delimiter
                    let matchStr = nsText.substring(with: match.range) as NSString
                    let lastNewline = matchStr.range(of: "\n", options: .backwards)
                    if lastNewline.location != NSNotFound {
                        let closeStart = match.range.location + lastNewline.location + 1
                        let closeLen = match.range.location + match.range.length - closeStart
                        if closeLen > 0 {
                            let closeRange = NSRange(location: closeStart, length: closeLen)
                            textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: closeRange)
                        }
                    }
                    // Color YAML keys within the body
                    if match.numberOfRanges >= 2 {
                        let bodyRange = match.range(at: 1)
                        if bodyRange.location != NSNotFound, let keyRegex = Self.frontmatterKeyRegex {
                            keyRegex.enumerateMatches(in: text, range: bodyRange) { keyMatch, _, _ in
                                guard let keyMatch = keyMatch, keyMatch.numberOfRanges >= 3 else { return }
                                textStorage.addAttribute(.foregroundColor, value: EditorTheme.headingColor, range: keyMatch.range(at: 1))
                                textStorage.addAttribute(.foregroundColor, value: EditorTheme.syntaxColor, range: keyMatch.range(at: 2))
                            }
                        }
                    }
                }
            }
        }

        textStorage.endEditing()
    }

    private func matchedText(_ text: String, range: NSRange) -> String {
        (text as NSString).substring(with: range)
    }
}
```

## File: `Chops/Views/Detail/SkillDetailView.swift`
```
import SwiftUI
import SwiftData

/// Transparent NSView overlay that intercepts AppKit hit-testing so it owns
/// cursor management (pointing hand) and click handling, beating NSTextView's
/// aggressive I-beam cursor.
private struct ClickableCursorOverlay: NSViewRepresentable {
    var action: () -> Void

    func makeNSView(context: Context) -> OverlayNSView {
        let view = OverlayNSView()
        view.onTap = action
        return view
    }

    func updateNSView(_ nsView: OverlayNSView, context: Context) {
        nsView.onTap = action
    }

    final class OverlayNSView: NSView {
        var onTap: (() -> Void)?
        private var area: NSTrackingArea?

        override func updateTrackingAreas() {
            super.updateTrackingAreas()
            if let area { removeTrackingArea(area) }
            area = NSTrackingArea(
                rect: bounds,
                options: [.mouseEnteredAndExited, .cursorUpdate, .activeInKeyWindow],
                owner: self
            )
            addTrackingArea(area!)
        }

        override func hitTest(_ point: NSPoint) -> NSView? {
            let local = convert(point, from: superview)
            return bounds.contains(local) ? self : nil
        }

        override func cursorUpdate(with event: NSEvent) {
            NSCursor.pointingHand.set()
        }

        override func mouseEntered(with event: NSEvent) {
            NSCursor.pointingHand.set()
        }

        override func mouseExited(with event: NSEvent) {
            NSCursor.arrow.set()
        }

        override func mouseDown(with event: NSEvent) {
            onTap?()
        }

        override func resetCursorRects() {
            addCursorRect(bounds, cursor: .pointingHand)
        }
    }
}

struct SkillDetailView: View {
    private enum ActiveAlert: Identifiable {
        case confirmDelete
        case deleteError(String)

        var id: String {
            switch self {
            case .confirmDelete:
                return "confirm-delete"
            case .deleteError(let message):
                return "delete-error-\(message)"
            }
        }
    }

    @Bindable var skill: Skill
    @Environment(\.modelContext) private var modelContext
    @Environment(AppState.self) private var appState
    @AppStorage("preferPreview") private var preferPreview = false
    @State private var document = SkillEditorDocument()
    @State private var activeAlert: ActiveAlert?
    @State private var autoSaveTask: Task<Void, Never>?
    @State private var showingComposePanel = false

    var body: some View {
        @Bindable var document = document

        VStack(spacing: 0) {
            ZStack(alignment: .bottomTrailing) {
                if preferPreview {
                    SkillPreviewView(content: document.editorContent)
                } else {
                    SkillEditorView(document: document, isEditable: !skill.isReadOnly)
                }

                if !showingComposePanel && !skill.isReadOnly {
                    composeFloatingButton
                }
            }

            // Inline compose panel
            if showingComposePanel {
                ComposePanel(
                    content: $document.editorContent,
                    isVisible: $showingComposePanel,
                    skillName: skill.name,
                    skillDescription: skill.skillDescription,
                    frontmatter: skill.frontmatter,
                    filePath: skill.filePath,
                    workingDirectory: URL(fileURLWithPath: skill.filePath).deletingLastPathComponent(),
                    templateType: WizardTemplateType(rawValue: skill.itemKind.rawValue) ?? .skill,
                    onAccept: { document.save(to: skill) }
                )
                .id(skill.filePath)
            }

            Divider()

            SkillMetadataBar(skill: skill)
        }
        .navigationTitle(skill.name)
        .onAppear {
            document.load(from: skill)
        }
        .onChange(of: skill.filePath) {
            autoSaveTask?.cancel()
            document.load(from: skill)
        }
        .onChange(of: document.editorContent) {
            guard !skill.isReadOnly else { return }
            autoSaveTask?.cancel()
            autoSaveTask = Task {
                try? await Task.sleep(for: .seconds(1))
                guard !Task.isCancelled, document.hasUnsavedChanges else { return }
                document.save(to: skill)
            }
        }
        .onDisappear {
            autoSaveTask?.cancel()
        }
        .onReceive(NotificationCenter.default.publisher(for: .saveCurrentSkill)) { _ in
            guard !skill.isReadOnly else { return }
            document.save(to: skill)
        }
        .alert("Save Error", isPresented: $document.showingSaveError) {
            Button("OK") {}
        } message: {
            Text(document.saveErrorMessage)
        }
        .toolbar {
            ToolbarItem {
                Picker("Mode", selection: $preferPreview) {
                    Image(systemName: "pencil").tag(false)
                    Image(systemName: "eye").tag(true)
                }
                .pickerStyle(.segmented)
            }
            ToolbarItem {
                Button {
                    skill.isFavorite.toggle()
                    try? modelContext.save()
                } label: {
                    Image(systemName: skill.isFavorite ? "star.fill" : "star")
                        .foregroundStyle(skill.isFavorite ? .yellow : .secondary)
                }
            }
            if !skill.isRemote {
                ToolbarItem {
                    Button {
                        NSWorkspace.shared.selectFile(skill.filePath, inFileViewerRootedAtPath: "")
                    } label: {
                        Image(systemName: "folder")
                    }
                    .help("Show in Finder")
                }
            }
            if !skill.isReadOnly {
                ToolbarItem {
                    Button {
                        activeAlert = .confirmDelete
                    } label: {
                        Image(systemName: "trash")
                    }
                    .help("Delete \(skill.displayTypeName)")
                }
            }
        }
        .alert(item: $activeAlert) { alert in
            switch alert {
            case .confirmDelete:
                return Alert(
                    title: Text("Delete \(skill.displayTypeName)?"),
                    message: Text("This will permanently delete \"\(skill.name)\" from disk."),
                    primaryButton: .destructive(Text("Delete")) {
                        deleteSkill()
                    },
                    secondaryButton: .cancel()
                )
            case .deleteError(let message):
                return Alert(
                    title: Text("Delete Failed"),
                    message: Text(message),
                    dismissButton: .default(Text("OK"))
                )
            }
        }
    }

    private var composeFloatingButton: some View {
        Image(systemName: "sparkles")
            .font(.system(size: 14, weight: .semibold))
            .foregroundStyle(.white)
            .frame(width: 36, height: 36)
            .background(Circle().fill(Color.accentColor))
            .shadow(color: .black.opacity(0.25), radius: 4, y: 2)
            .overlay(ClickableCursorOverlay(action: { [self] in showingComposePanel.toggle() }))
            .help("Compose with AI")
            .padding(16)
    }

    private func deleteSkill() {
        guard !skill.isReadOnly else { return }
        do {
            try skill.deleteFromDisk()
            appState.selectedSkill = nil
            modelContext.delete(skill)
            try modelContext.save()
        } catch {
            activeAlert = .deleteError(error.localizedDescription)
        }
    }
}
```

## File: `Chops/Views/Detail/SkillEditorView.swift`
```
import SwiftUI
import AppKit
import os

@Observable
final class SkillEditorDocument {
    var editorContent: String = "" {
        didSet {
            guard !isLoading else { return }
            hasUnsavedChanges = editorContent != fullFileContent
        }
    }
    var hasUnsavedChanges = false
    var isLoadingRemote = false
    var isSavingRemote = false
    var showingSaveError = false
    var saveErrorMessage = ""

    private var fullFileContent: String = ""
    private var isLoading = false
    private var loadTask: Task<Void, Never>?
    private var loadGeneration = 0

    func load(from skill: Skill) {
        if skill.isRemote {
            loadRemote(skill)
        } else {
            loadLocal(skill)
        }
    }

    func save(to skill: Skill) {
        if skill.isRemote {
            saveRemote(skill)
        } else {
            saveLocal(skill)
        }
    }

    // MARK: - Local

    private func loadLocal(_ skill: Skill) {
        isLoading = true
        loadTask?.cancel()
        loadGeneration += 1

        let path = skill.filePath
        let fallback = skill.content
        let generation = loadGeneration

        loadTask = Task.detached { [weak self] in
            let start = CFAbsoluteTimeGetCurrent()
            let data: String
            if let fileData = try? String(contentsOfFile: path, encoding: .utf8) {
                data = fileData
            } else {
                AppLogger.fileIO.warning("Failed to read file, using cached content: \(path)")
                data = fallback
            }
            guard !Task.isCancelled else { return }
            let elapsed = CFAbsoluteTimeGetCurrent() - start
            AppLogger.fileIO.notice("Loaded \(path) in \(String(format: "%.3f", elapsed))s (\(data.count) chars)")

            await MainActor.run { [data] in
                guard let self, self.loadGeneration == generation else { return }
                self.editorContent = data
                self.fullFileContent = data
                self.isLoading = false
                self.hasUnsavedChanges = false
                self.showingSaveError = false
                self.saveErrorMessage = ""
            }
        }
    }

    private func saveLocal(_ skill: Skill) {
        do {
            try editorContent.write(toFile: skill.filePath, atomically: true, encoding: .utf8)
            fullFileContent = editorContent
            hasUnsavedChanges = false

            let parsed = FrontmatterParser.parse(editorContent)
            if !parsed.name.isEmpty {
                skill.name = parsed.name
            }
            skill.skillDescription = parsed.description
            skill.content = parsed.content
            skill.frontmatter = parsed.frontmatter

            let attrs = try? FileManager.default.attributesOfItem(atPath: skill.filePath)
            skill.fileModifiedDate = (attrs?[.modificationDate] as? Date) ?? skill.fileModifiedDate
            skill.fileSize = (attrs?[.size] as? Int) ?? skill.fileSize
            AppLogger.fileIO.info("Saved: \(skill.filePath)")
        } catch {
            AppLogger.fileIO.error("Save failed: \(error.localizedDescription)")
            saveErrorMessage = error.localizedDescription
            showingSaveError = true
        }
    }

    // MARK: - Remote

    private func loadRemote(_ skill: Skill) {
        guard let server = skill.remoteServer, let remotePath = skill.remotePath else {
            editorContent = skill.content
            fullFileContent = skill.content
            return
        }

        loadTask?.cancel()
        loadGeneration += 1
        let generation = loadGeneration
        let fallbackContent = skill.content

        isLoading = true
        isLoadingRemote = true

        loadTask = Task {
            do {
                let content = try await SSHService.readFile(server, path: remotePath)
                guard !Task.isCancelled, loadGeneration == generation else { return }
                await MainActor.run {
                    guard self.loadGeneration == generation else { return }
                    editorContent = content
                    fullFileContent = content
                    isLoading = false
                    isLoadingRemote = false
                    hasUnsavedChanges = false
                    showingSaveError = false
                    saveErrorMessage = ""
                }
            } catch {
                guard !Task.isCancelled, loadGeneration == generation else { return }
                await MainActor.run {
                    guard self.loadGeneration == generation else { return }
                    editorContent = fallbackContent
                    fullFileContent = fallbackContent
                    isLoading = false
                    isLoadingRemote = false
                    hasUnsavedChanges = false
                    saveErrorMessage = "Failed to load from server: \(error.localizedDescription)"
                    showingSaveError = true
                }
            }
        }
    }

    private func saveRemote(_ skill: Skill) {
        guard let server = skill.remoteServer, let remotePath = skill.remotePath else {
            saveErrorMessage = "Missing remote server or path"
            showingSaveError = true
            return
        }

        isSavingRemote = true

        Task {
            do {
                try await SSHService.writeFile(server, path: remotePath, content: editorContent)
                await MainActor.run {
                    fullFileContent = editorContent
                    hasUnsavedChanges = false
                    isSavingRemote = false

                    let parsed = FrontmatterParser.parse(editorContent)
                    if !parsed.name.isEmpty {
                        skill.name = parsed.name
                    }
                    skill.skillDescription = parsed.description
                    skill.content = parsed.content
                    skill.frontmatter = parsed.frontmatter
                    skill.fileModifiedDate = .now
                    skill.fileSize = editorContent.utf8.count
                }
            } catch {
                await MainActor.run {
                    saveErrorMessage = error.localizedDescription
                    showingSaveError = true
                    isSavingRemote = false
                }
            }
        }
    }

    deinit {
        loadTask?.cancel()
    }
}

struct SkillEditorView: View {
    @Bindable var document: SkillEditorDocument
    var isEditable: Bool = true

    var body: some View {
        ZStack(alignment: .topTrailing) {
            if document.isLoadingRemote {
                VStack {
                    ProgressView("Loading from server...")
                        .padding()
                }
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            } else {
                HighlightedTextEditor(text: $document.editorContent, isEditable: isEditable)
            }

            HStack(spacing: 6) {
                if document.isSavingRemote {
                    ProgressView()
                        .controlSize(.small)
                    Text("Saving...")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }

            }
            .padding(12)
        }
    }
}

// MARK: - Save notification for Cmd+S menu support

extension Notification.Name {
    static let saveCurrentSkill = Notification.Name("saveCurrentSkill")
}

// MARK: - Syntax-highlighted NSTextView wrapper

struct HighlightedTextEditor: NSViewRepresentable {
    @Binding var text: String
    var isEditable: Bool = true
    @Environment(\.colorScheme) private var colorScheme

    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }

    func makeNSView(context: Context) -> NSScrollView {
        let scrollView = NSScrollView()
        scrollView.hasVerticalScroller = true
        scrollView.hasHorizontalScroller = false
        scrollView.drawsBackground = false
        scrollView.autohidesScrollers = true

        let textView = ChopsTextView()
        textView.isEditable = isEditable
        textView.isRichText = false
        textView.allowsUndo = true
        textView.usesFindPanel = true
        textView.isAutomaticQuoteSubstitutionEnabled = false
        textView.isAutomaticDashSubstitutionEnabled = false
        textView.isAutomaticTextReplacementEnabled = false
        textView.isAutomaticSpellingCorrectionEnabled = false

        // Font & colors
        textView.font = EditorTheme.editorFont
        textView.textColor = EditorTheme.textColor
        textView.backgroundColor = .clear

        // Line height with baseline centering
        let paragraph = NSMutableParagraphStyle()
        paragraph.minimumLineHeight = EditorTheme.editorLineHeight
        paragraph.maximumLineHeight = EditorTheme.editorLineHeight
        textView.defaultParagraphStyle = paragraph
        textView.typingAttributes = [
            .font: EditorTheme.editorFont,
            .foregroundColor: EditorTheme.textColor,
            .paragraphStyle: paragraph,
            .baselineOffset: EditorTheme.editorBaselineOffset
        ]

        // Insets
        textView.textContainerInset = NSSize(width: EditorTheme.editorInsetX, height: EditorTheme.editorInsetTop)
        textView.textContainer?.lineFragmentPadding = 0

        // Layout
        textView.isVerticallyResizable = true
        textView.isHorizontallyResizable = false
        textView.autoresizingMask = [.width]
        textView.textContainer?.widthTracksTextView = true
        textView.layoutManager?.allowsNonContiguousLayout = true

        textView.insertionPointColor = EditorTheme.textColor

        // Set up highlighter and coordinator
        let highlighter = MarkdownSyntaxHighlighter()
        context.coordinator.highlighter = highlighter
        context.coordinator.textView = textView

        // Set text BEFORE attaching delegate to avoid triggering textDidChange during setup
        textView.string = text
        textView.delegate = context.coordinator

        scrollView.documentView = textView

        // Initial highlight
        highlighter.highlightAll(textView.textStorage!)

        return scrollView
    }

    func updateNSView(_ scrollView: NSScrollView, context: Context) {
        guard let textView = scrollView.documentView as? ChopsTextView else { return }

        context.coordinator.parent = self
        textView.isEditable = isEditable

        // Re-highlight on appearance change
        let currentScheme = colorScheme
        if context.coordinator.lastColorScheme != currentScheme {
            context.coordinator.lastColorScheme = currentScheme
            textView.insertionPointColor = EditorTheme.textColor

            let paragraph = NSMutableParagraphStyle()
            paragraph.minimumLineHeight = EditorTheme.editorLineHeight
            paragraph.maximumLineHeight = EditorTheme.editorLineHeight
            textView.typingAttributes = [
                .font: EditorTheme.editorFont,
                .foregroundColor: EditorTheme.textColor,
                .paragraphStyle: paragraph,
                .baselineOffset: EditorTheme.editorBaselineOffset
            ]

            context.coordinator.isHighlightingInProgress = true
            context.coordinator.highlighter?.highlightAll(textView.textStorage!)
            context.coordinator.isHighlightingInProgress = false
        }

        // Only update text if it changed externally (not from user typing)
        if !context.coordinator.isUpdating && textView.string != text {
            context.coordinator.isUpdating = true
            let selectedRanges = textView.selectedRanges
            textView.string = text
            context.coordinator.isHighlightingInProgress = true
            context.coordinator.highlighter?.highlightAll(textView.textStorage!)
            context.coordinator.isHighlightingInProgress = false
            textView.selectedRanges = selectedRanges
            context.coordinator.isUpdating = false
        }
    }

    // MARK: - Coordinator

    final class Coordinator: NSObject, NSTextViewDelegate {
        var parent: HighlightedTextEditor
        var isUpdating = false
        var isHighlightingInProgress = false
        var highlighter: MarkdownSyntaxHighlighter?
        weak var textView: ChopsTextView?
        var lastColorScheme: ColorScheme?

        init(_ parent: HighlightedTextEditor) {
            self.parent = parent
        }

        func textDidChange(_ notification: Notification) {
            guard let textView = notification.object as? NSTextView else { return }
            if isUpdating { return }

            // Highlight synchronously so colors appear on the same frame
            isHighlightingInProgress = true
            highlighter?.highlightAll(textView.textStorage!)
            isHighlightingInProgress = false

            // Update binding asynchronously to prevent re-entrant updateNSView
            let newText = textView.string
            DispatchQueue.main.async { [weak self] in
                guard let self else { return }
                self.isUpdating = true
                self.parent.text = newText
                self.isUpdating = false
            }
        }
    }
}
```

## File: `Chops/Views/Detail/SkillMetadataBar.swift`
```
import SwiftUI
import SwiftData

struct SkillMetadataBar: View {
    @Bindable var skill: Skill
    @Environment(\.modelContext) private var modelContext
    @Query(sort: \SkillCollection.sortOrder) private var allCollections: [SkillCollection]
    @State private var showingCollectionPicker = false

    var body: some View {
        HStack(spacing: 16) {
            HStack(spacing: 6) {
                ForEach(skill.toolSources) { tool in
                    ToolIcon(tool: tool, size: 14)
                }
            }
            .help(installedPathsSummary)

            Divider().frame(height: 16)

            if skill.isRemote, let server = skill.remoteServer {
                Label {
                    Text(server.label)
                } icon: {
                    Image(systemName: "server.rack")
                }
                .font(.caption)
                .foregroundStyle(.indigo)

                Divider().frame(height: 16)
            }

            Text(skill.isRemote ? (skill.remotePath ?? "") : displayPath)
                .font(.caption)
                .foregroundStyle(.secondary)
                .lineLimit(1)
                .truncationMode(.middle)
                .help(skill.isRemote ? (skill.remotePath ?? "") : installedPathsSummary)

            Divider().frame(height: 16)

            Text(formattedSize)
                .font(.caption)
                .foregroundStyle(.secondary)

            Divider().frame(height: 16)

            Button {
                showingCollectionPicker.toggle()
            } label: {
                Image(systemName: "tray")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
            .buttonStyle(.plain)
            .popover(isPresented: $showingCollectionPicker) {
                collectionPickerContent
            }

            Spacer()

            Text(skill.fileModifiedDate.formatted(.relative(presentation: .named)))
                .font(.caption)
                .foregroundStyle(.secondary)
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 8)
        .background(.bar)
    }

    private var displayPath: String {
        let additionalCount = max(0, displayInstalledPaths.count - 1)
        let suffix = additionalCount > 0 ? " (+\(additionalCount))" : ""
        return abbreviatedFilePath + suffix
    }

    private var abbreviatedFilePath: String {
        skill.filePath.replacingOccurrences(
            of: FileManager.default.homeDirectoryForCurrentUser.path,
            with: "~"
        )
    }

    private var formattedSize: String {
        ByteCountFormatter.string(fromByteCount: Int64(skill.fileSize), countStyle: .file)
    }

    private var installedPathsSummary: String {
        displayInstalledPaths
            .map { $0.replacingOccurrences(of: FileManager.default.homeDirectoryForCurrentUser.path, with: "~") }
            .joined(separator: "\n")
    }

    private var displayInstalledPaths: [String] {
        let otherPaths = skill.installedPaths
            .filter { $0 != skill.filePath }
            .sorted()
        return [skill.filePath] + otherPaths
    }

    private var collectionPickerContent: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text("Collections").font(.headline).padding(.bottom, 4)
            ForEach(allCollections) { collection in
                let isAssigned = skill.collections.contains(where: { $0.name == collection.name })
                Button {
                    if isAssigned {
                        skill.collections.removeAll { $0.name == collection.name }
                    } else {
                        skill.collections.append(collection)
                    }
                    try? modelContext.save()
                } label: {
                    HStack {
                        Image(systemName: collection.icon)
                        Text(collection.name)
                        Spacer()
                        if isAssigned {
                            Image(systemName: "checkmark")
                        }
                    }
                }
                .buttonStyle(.plain)
            }
            if allCollections.isEmpty {
                Text("No collections yet")
                    .foregroundStyle(.secondary)
                    .font(.caption)
            }
        }
        .padding()
        .frame(width: 200)
    }
}
```

## File: `Chops/Views/Detail/SkillPreviewView.swift`
```
import SwiftUI
import WebKit

struct SkillPreviewView: View {
    let content: String

    var body: some View {
        MarkdownWebView(content: content)
            .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

// MARK: - WKWebView Wrapper

private struct MarkdownWebView: NSViewRepresentable {
    let content: String
    @Environment(\.colorScheme) private var colorScheme

    private var contentHash: Int {
        var hasher = Hasher()
        hasher.combine(content)
        hasher.combine(colorScheme)
        return hasher.finalize()
    }

    func makeCoordinator() -> Coordinator {
        Coordinator()
    }

    func makeNSView(context: Context) -> WKWebView {
        let config = WKWebViewConfiguration()
        config.preferences.isElementFullscreenEnabled = false
        config.defaultWebpagePreferences.allowsContentJavaScript = false
        let webView = WKWebView(frame: .zero, configuration: config)
        webView.navigationDelegate = context.coordinator
        webView.underPageBackgroundColor = Self.dynamicBgColor
        loadHTML(in: webView, context: context)
        return webView
    }

    private static let dynamicBgColor = NSColor(name: nil) { appearance in
        appearance.bestMatch(from: [.darkAqua, .aqua]) == .darkAqua
            ? NSColor(red: 0x1A/255.0, green: 0x1A/255.0, blue: 0x1A/255.0, alpha: 1)
            : NSColor(red: 0xFA/255.0, green: 0xFA/255.0, blue: 0xFA/255.0, alpha: 1)
    }

    func updateNSView(_ webView: WKWebView, context: Context) {
        webView.underPageBackgroundColor = Self.dynamicBgColor
        if context.coordinator.lastContentHash != contentHash {
            loadHTML(in: webView, context: context)
        }
    }

    private func loadHTML(in webView: WKWebView, context: Context) {
        context.coordinator.lastContentHash = contentHash
        let parsed = RawFrontmatterParser.parse(content)
        let isDarkMode = colorScheme == .dark
        let markdownHTML = MarkdownRenderer.renderHTML(parsed?.content ?? content, isDarkMode: isDarkMode)
        let themeCSS = MarkdownRenderer.themeCSS(isDarkMode: isDarkMode)

        var bodyHTML = ""
        if let fm = parsed?.frontmatter {
            let escaped = fm
                .replacingOccurrences(of: "&", with: "&amp;")
                .replacingOccurrences(of: "<", with: "&lt;")
                .replacingOccurrences(of: ">", with: "&gt;")
            bodyHTML += "<pre class=\"frontmatter\">\(escaped)</pre>"
        }
        bodyHTML += markdownHTML

        let html = """
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; img-src data:;">
        <style>\(themeCSS)
        \(Self.css)</style>
        </head>
        <body>\(bodyHTML)</body>
        </html>
        """
        webView.loadHTMLString(html, baseURL: nil)
    }

    final class Coordinator: NSObject, WKNavigationDelegate {
        var lastContentHash: Int?

        func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
            if navigationAction.navigationType == .linkActivated,
               let url = navigationAction.request.url {
                NSWorkspace.shared.open(url)
                decisionHandler(.cancel)
            } else {
                decisionHandler(.allow)
            }
        }
    }

    // MARK: - CSS

    private static let css = """
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
        font-size: 16px;
        line-height: 1.6;
        max-width: 672px;
        margin: 0 auto;
        padding: 24px 24px 40px;
        color: #222222;
        background-color: #FAFAFA;
        -webkit-font-smoothing: antialiased;
        -webkit-user-select: text;
    }

    @media (prefers-color-scheme: dark) {
        body {
            color: #E0E0E0;
            background-color: #1A1A1A;
        }
        a { color: #6699CC; }
        code {
            background-color: #2A2A2A !important;
            color: #E07070 !important;
        }
        pre {
            background-color: #2A2A2A !important;
            border-color: #333333 !important;
            color: #E0E0E0 !important;
        }
        pre code {
            background: none !important;
            color: #E0E0E0 !important;
        }
        blockquote {
            border-left-color: #444444;
            color: #999999;
        }
        table th {
            background-color: #2A2A2A;
            border-color: #444444;
        }
        table td {
            border-color: #333333;
        }
        table tr:nth-child(even) {
            background-color: #222222;
        }
        hr {
            border-color: #333333;
        }
        pre.frontmatter {
            color: #999999;
            background-color: #222222;
            border-color: #333333;
        }
        pre.highlighted-code code.hljs {
            border-color: #333333;
        }
    }

    h1, h2, h3, h4, h5, h6 {
        font-weight: 700;
        line-height: 1.3;
        margin-top: 1.5em;
        margin-bottom: 0.5em;
    }

    body > *:first-child {
        margin-top: 0;
    }

    h1 { font-size: 2em; }
    h2 { font-size: 1.5em; }
    h3 { font-size: 1.25em; }
    h4 { font-size: 1.1em; }

    p {
        margin-bottom: 1em;
    }

    a {
        color: #3366AA;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }

    code {
        font-family: "SF Mono", SFMono-Regular, Menlo, monospace;
        font-size: 0.85em;
        background-color: #F0F0F0;
        color: #CC3333;
        padding: 0.15em 0.35em;
        border-radius: 3px;
    }

    pre {
        background-color: #F5F5F5;
        border: 1px solid #E0E0E0;
        border-radius: 4px;
        padding: 1em;
        margin-bottom: 1em;
        overflow-x: auto;
    }

    pre code {
        background: none;
        color: inherit;
        padding: 0;
        font-size: 0.85em;
    }

    pre.highlighted-code {
        background: none;
        border: none;
        padding: 0;
    }

    pre.highlighted-code code.hljs {
        border: 1px solid #E0E0E0;
        border-radius: 4px;
        font-size: 0.85em;
    }

    blockquote {
        border-left: 3px solid #CCCCCC;
        padding-left: 1em;
        margin-left: 0;
        margin-bottom: 1em;
        color: #666666;
        font-style: italic;
    }

    ul, ol {
        margin-bottom: 1em;
        padding-left: 1.5em;
    }

    li {
        margin-bottom: 0.25em;
    }

    ul.contains-task-list {
        list-style: none;
        padding-left: 0;
    }

    li.task-list-item {
        display: flex;
        align-items: baseline;
        gap: 0.5em;
    }

    li.task-list-item input[type="checkbox"] {
        margin: 0;
    }

    table {
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 1em;
    }

    th, td {
        text-align: left;
        padding: 0.5em 0.75em;
    }

    th {
        font-weight: 600;
        background-color: #F5F5F5;
        border-bottom: 2px solid #DDDDDD;
    }

    td {
        border-bottom: 1px solid #EEEEEE;
    }

    tr:nth-child(even) {
        background-color: #FAFAFA;
    }

    del {
        text-decoration: line-through;
        opacity: 0.6;
    }

    hr {
        border: none;
        border-top: 1px solid #DDDDDD;
        margin: 2em 0;
    }

    img {
        max-width: 100%;
        height: auto;
    }

    pre.frontmatter {
        font-family: "SF Mono", SFMono-Regular, Menlo, monospace;
        font-size: 12px;
        line-height: 1.5;
        color: #333333;
        background-color: #F0F0F0;
        border: 1px solid transparent;
        border-radius: 6px;
        padding: 10px 12px;
        margin-bottom: 24px;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
    """
}

private enum RawFrontmatterParser {
    struct Result {
        let frontmatter: String?
        let content: String
    }

    static func parse(_ text: String) -> Result? {
        let lines = text.components(separatedBy: "\n")

        guard lines.first?.trimmingCharacters(in: .whitespaces) == "---" else {
            return nil
        }

        for index in 1..<lines.count {
            if lines[index].trimmingCharacters(in: .whitespaces) == "---" {
                let frontmatterLines = Array(lines[1..<index])
                let frontmatter = frontmatterLines.joined(separator: "\n")
                    .trimmingCharacters(in: .whitespacesAndNewlines)
                let contentStart = min(index + 1, lines.count)
                let content = Array(lines[contentStart...]).joined(separator: "\n")
                    .trimmingCharacters(in: .whitespacesAndNewlines)
                return Result(
                    frontmatter: frontmatter.isEmpty ? nil : frontmatter,
                    content: content
                )
            }
        }

        return nil
    }
}
```

## File: `Chops/Views/Settings/ACPSettingsView.swift`
```
import ACPRegistry
import SwiftUI

struct ACPSettingsView: View {
    @State private var configuration = ACPConfiguration.shared
    @State private var templateManager = TemplateManager.shared
    @State private var templateContents: [WizardTemplateType: String] = [:]
    @State private var templateChanges: Set<WizardTemplateType> = []
    @State private var showingResetConfirm: WizardTemplateType?
    @State private var expandedTemplates: Set<WizardTemplateType> = []

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                Text("Enable AI assistants to help compose and improve skills, agents, and rules.")
                    .font(.callout)
                    .foregroundStyle(.secondary)

                agentListSection

                HStack {
                    Button("Refresh Registry") {
                        Task { await configuration.refreshRegistry() }
                    }
                    .disabled(configuration.isLoadingRegistry)
                }

                Divider()

                templateSection
            }
            .padding()
        }
        .frame(maxHeight: 550)
        .task { await configuration.loadRegistryIfNeeded() }
        .onAppear { loadAllTemplates() }
    }

    // MARK: - Agent List

    @ViewBuilder
    private var agentListSection: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Agents")
                .font(.headline)

            if configuration.isLoadingRegistry {
                HStack {
                    ProgressView()
                        .controlSize(.small)
                    Text("Loading registry…")
                        .foregroundStyle(.secondary)
                }
            } else if let error = configuration.registryError {
                HStack(spacing: 6) {
                    Image(systemName: "exclamationmark.triangle.fill")
                        .foregroundStyle(.orange)
                    Text(error)
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
            } else if configuration.registryAgents.isEmpty {
                Text("No agents found.")
                    .foregroundStyle(.secondary)
            } else {
                VStack(spacing: 0) {
                    ForEach(configuration.registryAgents) { agent in
                        AgentRow(agent: agent, configuration: configuration)
                        if agent.id != configuration.registryAgents.last?.id {
                            Divider()
                        }
                    }
                }
                .padding(8)
                .background(Color(NSColor.controlBackgroundColor))
                .clipShape(RoundedRectangle(cornerRadius: 6))
            }
        }
    }

    // MARK: - Wizard Templates

    private var templateSection: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Chat Rules")
                .font(.headline)

            VStack(spacing: 0) {
                ForEach(WizardTemplateType.allCases) { type in
                    VStack(spacing: 0) {
                        Button {
                            withAnimation(.easeInOut(duration: 0.15)) {
                                if expandedTemplates.contains(type) {
                                    expandedTemplates.remove(type)
                                } else {
                                    expandedTemplates.insert(type)
                                }
                            }
                        } label: {
                            HStack {
                                Image(systemName: "chevron.right")
                                    .font(.caption2)
                                    .rotationEffect(expandedTemplates.contains(type) ? .degrees(90) : .zero)
                                Label(type.displayName, systemImage: type.icon)
                                Spacer()
                            }
                            .padding(.horizontal, 8)
                            .padding(.vertical, 8)
                            .contentShape(Rectangle())
                        }
                        .buttonStyle(.plain)

                        if expandedTemplates.contains(type) {
                            templateEditor(for: type)
                                .padding(.horizontal, 8)
                                .padding(.bottom, 8)
                        }
                    }

                    if type != WizardTemplateType.allCases.last {
                        Divider()
                    }
                }
            }
            .padding(4)
            .background(Color(NSColor.controlBackgroundColor))
            .clipShape(RoundedRectangle(cornerRadius: 6))
        }
    }

    @ViewBuilder
    private func templateEditor(for type: WizardTemplateType) -> some View {
        let binding = Binding<String>(
            get: { templateContents[type] ?? "" },
            set: {
                templateContents[type] = $0
                templateChanges.insert(type)
            }
        )

        VStack(alignment: .leading, spacing: 8) {
            TextEditor(text: binding)
                .font(.system(.caption, design: .monospaced))
                .scrollContentBackground(.hidden)
                .frame(height: 200)
                .padding(6)
                .background(Color(NSColor.textBackgroundColor))
                .clipShape(RoundedRectangle(cornerRadius: 4))

            HStack {
                if templateChanges.contains(type) {
                    Text("Unsaved changes")
                        .font(.caption)
                        .foregroundStyle(.orange)
                }

                Spacer()

                Button("Reset to Default") {
                    showingResetConfirm = type
                }
                .buttonStyle(.plain)
                .foregroundStyle(.red)
                .font(.caption)

                Button("Save") {
                    saveTemplate(type)
                }
                .buttonStyle(.borderedProminent)
                .controlSize(.small)
                .disabled(!templateChanges.contains(type))
            }
        }
        .confirmationDialog(
            "Reset Template?",
            isPresented: Binding(
                get: { showingResetConfirm == type },
                set: { if !$0 { showingResetConfirm = nil } }
            ),
            titleVisibility: .visible
        ) {
            Button("Reset to Default", role: .destructive) {
                templateManager.resetToDefault(type)
                loadTemplate(type)
            }
            Button("Cancel", role: .cancel) {}
        } message: {
            Text("This will replace your custom template with the default version.")
        }
    }

    // MARK: - Template Helpers

    private func loadAllTemplates() {
        for type in WizardTemplateType.allCases {
            loadTemplate(type)
        }
    }

    private func loadTemplate(_ type: WizardTemplateType) {
        if let template = templateManager.template(for: type) {
            templateContents[type] = template.content
        }
        templateChanges.remove(type)
    }

    private func saveTemplate(_ type: WizardTemplateType) {
        guard let content = templateContents[type] else { return }
        let template = WizardTemplate(
            type: type,
            content: content,
            lastModified: Date()
        )
        templateManager.save(template)
        templateChanges.remove(type)
    }
}

// MARK: - Agent Row

private struct AgentRow: View {
    let agent: RegistryAgent
    @Bindable var configuration: ACPConfiguration

    var body: some View {
        HStack(spacing: 12) {
            VStack(alignment: .leading, spacing: 2) {
                Text(agent.name)
                    .fontWeight(.medium)
                Text(agent.description)
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .lineLimit(2)
                Text("v\(agent.version)")
                    .font(.caption2)
                    .foregroundStyle(.tertiary)
            }
            Spacer()
            Toggle("", isOn: Binding(
                get: { configuration.isEnabled(agent.id) },
                set: { configuration.setEnabled(agent.id, $0) }
            ))
            .labelsHidden()
        }
        .padding(.vertical, 4)
    }
}

// MARK: - Preview

#Preview {
    ACPSettingsView()
        .frame(width: 480)
}
```

## File: `Chops/Views/Settings/DiagnosticExporter.swift`
```
import AppKit
import Foundation
import OSLog
import SwiftData

enum DiagnosticExporter {
    static func export(modelContext: ModelContext) {
        var lines: [String] = []

        // System info
        let version = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String ?? "?"
        let build = Bundle.main.infoDictionary?["CFBundleVersion"] as? String ?? "?"
        let osVersion = ProcessInfo.processInfo.operatingSystemVersionString

        lines.append("# Chops Diagnostic Report")
        lines.append("Generated: \(ISO8601DateFormatter().string(from: .now))")
        lines.append("")
        lines.append("## System")
        lines.append("- App Version: \(version) (\(build))")
        lines.append("- macOS: \(osVersion)")
        lines.append("- Memory: \(ProcessInfo.processInfo.physicalMemory / 1_073_741_824) GB")
        lines.append("")

        // Skill counts
        let descriptor = FetchDescriptor<Skill>()
        let skills = (try? modelContext.fetch(descriptor)) ?? []
        let skillsOnly = skills.filter { $0.itemKind == .skill }
        let agentsOnly = skills.filter { $0.itemKind == .agent }
        lines.append("## Items")
        lines.append("- Total: \(skills.count)")
        lines.append("- Skills: \(skillsOnly.count)")
        lines.append("- Agents: \(agentsOnly.count)")
        for tool in ToolSource.allCases {
            let count = skills.filter { $0.toolSources.contains(tool) }.count
            if count > 0 {
                lines.append("- \(tool.displayName): \(count)")
            }
        }
        lines.append("")

        // Custom scan paths
        let customPaths = UserDefaults.standard.stringArray(forKey: "customScanPaths") ?? []
        lines.append("## Custom Scan Paths")
        if customPaths.isEmpty {
            lines.append("- (none)")
        } else {
            for path in customPaths {
                lines.append("- \(path)")
            }
        }
        lines.append("")

        // Recent logs
        lines.append("## Recent Logs")
        if let logEntries = collectRecentLogs() {
            lines.append(logEntries)
        } else {
            lines.append("(Unable to collect logs)")
        }

        let report = lines.joined(separator: "\n")

        // Save panel
        let panel = NSSavePanel()
        panel.nameFieldStringValue = "chops-diagnostic-\(dateStamp()).txt"
        panel.allowedContentTypes = [.plainText]

        if panel.runModal() == .OK, let url = panel.url {
            try? report.write(to: url, atomically: true, encoding: .utf8)
        }
    }

    private static func collectRecentLogs() -> String? {
        // Try system scope first (persisted logs, survives force quit)
        // Fall back to current process scope
        let store: OSLogStore
        if let systemStore = try? OSLogStore(scope: .system) {
            store = systemStore
        } else if let processStore = try? OSLogStore(scope: .currentProcessIdentifier) {
            store = processStore
        } else {
            return nil
        }

        let since = Date.now.addingTimeInterval(-3600) // last hour
        let subsystem = Bundle.main.bundleIdentifier ?? "com.shpigford.Chops"

        guard let entries = try? store.getEntries(
            at: store.position(date: since),
            matching: NSPredicate(format: "subsystem == %@", subsystem)
        ) else {
            return nil
        }

        var lines: [String] = []
        let formatter = DateFormatter()
        formatter.dateFormat = "HH:mm:ss.SSS"

        for entry in entries {
            guard let logEntry = entry as? OSLogEntryLog else { continue }
            let time = formatter.string(from: logEntry.date)
            lines.append("[\(time)] [\(logEntry.category)] \(logEntry.composedMessage)")
        }

        return lines.isEmpty ? "(No log entries in the last hour)" : lines.joined(separator: "\n")
    }

    private static func dateStamp() -> String {
        let f = DateFormatter()
        f.dateFormat = "yyyy-MM-dd-HHmmss"
        return f.string(from: .now)
    }
}
```

## File: `Chops/Views/Settings/LibrarySettingsView.swift`
```
import SwiftUI

/// Settings for the source-of-truth directory used when symlinking library items.
struct LibrarySettingsView: View {
    @AppStorage("sotDir") private var sotDir = FileManager.default.homeDirectoryForCurrentUser.path + "/.chops"
    @AppStorage("includePluginSkills") private var includePluginSkills = false

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            VStack(alignment: .leading, spacing: 4) {
                Toggle("Include plugin skills", isOn: $includePluginSkills)
                    .onChange(of: includePluginSkills) {
                        NotificationCenter.default.post(name: .customScanPathsChanged, object: nil)
                    }
                Text("When enabled, skills installed by Claude CLI and Claude Desktop plugins are listed in the library. These are read-only and managed by the plugin.")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
        }
        .padding()
    }

    private var displayPath: String {
        let home = FileManager.default.homeDirectoryForCurrentUser.path
        return sotDir.hasPrefix(home) ? "~" + sotDir.dropFirst(home.count) : sotDir
    }
}

private struct DirectoryPickerRow: View {
    let label: String
    @Binding var path: String

    var body: some View {
        HStack {
            VStack(alignment: .leading, spacing: 2) {
                Text(label)
                Text(displayPath)
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .lineLimit(1)
                    .truncationMode(.middle)
            }

            Spacer()

            Button("Choose...") {
                pickDirectory()
            }
        }
    }

    private var displayPath: String {
        let home = FileManager.default.homeDirectoryForCurrentUser.path
        return path.hasPrefix(home) ? "~" + path.dropFirst(home.count) : path
    }

    private func pickDirectory() {
        let panel = NSOpenPanel()
        panel.canChooseFiles = false
        panel.canChooseDirectories = true
        panel.allowsMultipleSelection = false
        panel.showsHiddenFiles = true
        panel.prompt = "Select"
        panel.directoryURL = URL(fileURLWithPath: (path as NSString).expandingTildeInPath)
        guard panel.runModal() == .OK, let url = panel.url else { return }
        path = url.path
    }
}
```

## File: `Chops/Views/Settings/RemoteServersSettingsView.swift`
```
import SwiftUI
import SwiftData

struct RemoteServersSettingsView: View {
    @Environment(\.modelContext) private var modelContext
    @Query(sort: \RemoteServer.label) private var servers: [RemoteServer]

    @State private var showingAddSheet = false

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Remote Servers")
                .font(.headline)

            Text("Connect to remote servers to browse and edit skills via SSH. Requires key-based authentication.")
                .font(.caption)
                .foregroundStyle(.secondary)

            ScrollView {
                VStack(spacing: 8) {
                    ForEach(servers) { server in
                        ServerRow(server: server)
                        if server.id != servers.last?.id {
                            Divider()
                        }
                    }
                }
            }
            .frame(minHeight: 120)

            HStack {
                Spacer()
                Button("Add Server...") {
                    showingAddSheet = true
                }
            }
        }
        .padding()
        .sheet(isPresented: $showingAddSheet) {
            AddServerSheet()
        }
    }
}

// MARK: - Server Row

private struct ServerRow: View {
    @Bindable var server: RemoteServer
    @Environment(\.modelContext) private var modelContext
    @State private var isTesting = false
    @State private var isSyncing = false
    @State private var testResult: TestResult?
    @State private var syncLog: String?
    @State private var showingEditSheet = false

    enum TestResult {
        case success
        case failure(String)
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            HStack {
                VStack(alignment: .leading, spacing: 2) {
                    Text(server.label)
                        .font(.body)
                    Text("\(server.username)@\(server.host):\(server.port)")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                        .fontDesign(.monospaced)
                    Text("Path: \(server.skillsBasePath)")
                        .font(.caption2)
                        .foregroundStyle(.tertiary)
                        .fontDesign(.monospaced)
                    if let lastSync = server.lastSyncDate {
                        Text("Synced \(lastSync.formatted(.relative(presentation: .named)))")
                            .font(.caption2)
                            .foregroundStyle(.tertiary)
                    }
                }

                Spacer()

                if let result = testResult {
                    switch result {
                    case .success:
                        Image(systemName: "checkmark.circle.fill")
                            .foregroundStyle(.green)
                    case .failure:
                        Image(systemName: "xmark.circle.fill")
                            .foregroundStyle(.red)
                    }
                }

                Button {
                    testConnection()
                } label: {
                    if isTesting {
                        ProgressView()
                            .controlSize(.small)
                    } else {
                        Text("Test")
                    }
                }
                .disabled(isTesting)

                Button {
                    syncNow()
                } label: {
                    if isSyncing {
                        ProgressView()
                            .controlSize(.small)
                    } else {
                        Text("Sync")
                    }
                }
                .disabled(isSyncing)

                Button {
                    showingEditSheet = true
                } label: {
                    Text("Edit")
                }

                Button(role: .destructive) {
                    modelContext.delete(server)
                    try? modelContext.save()
                } label: {
                    Image(systemName: "minus.circle.fill")
                        .foregroundStyle(.red)
                }
                .buttonStyle(.plain)
            }

            if let error = server.lastSyncError {
                Text("Error: \(error)")
                    .font(.caption)
                    .foregroundStyle(.red)
                    .textSelection(.enabled)
            }

            if let log = syncLog {
                Text(log)
                    .font(.caption)
                    .fontDesign(.monospaced)
                    .foregroundStyle(.secondary)
                    .textSelection(.enabled)
                    .padding(6)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(.quaternary.opacity(0.5))
                    .clipShape(RoundedRectangle(cornerRadius: 4))
            }
        }
        .sheet(isPresented: $showingEditSheet) {
            EditServerSheet(server: server)
        }
    }

    private func testConnection() {
        isTesting = true
        testResult = nil
        Task {
            do {
                try await SSHService.testConnection(server)
                await MainActor.run {
                    testResult = .success
                    isTesting = false
                }
            } catch {
                await MainActor.run {
                    testResult = .failure(error.localizedDescription)
                    isTesting = false
                }
            }
        }
    }

    private func syncNow() {
        isSyncing = true
        syncLog = "Connecting to \(server.sshDestination)..."
        Task { @MainActor in
            do {
                let skills = try await SSHService.findSkills(server)
                if skills.isEmpty {
                    syncLog = "find returned 0 results.\nPath searched: \(server.skillsBasePath)\nCommand: find <path> -name 'SKILL.md' -type f"
                } else {
                    let scanner = SkillScanner(modelContext: modelContext)
                    await scanner.scanRemoteServer(server)
                    syncLog = "Found \(skills.count) skill(s):\n" + skills.map { "  \($0.path)" }.joined(separator: "\n")
                }
            } catch {
                syncLog = "Sync failed: \(error.localizedDescription)"
            }
            isSyncing = false
        }
    }
}

// MARK: - Add Server Sheet

private struct AddServerSheet: View {
    @Environment(\.modelContext) private var modelContext
    @Environment(\.dismiss) private var dismiss

    @State private var label = ""
    @State private var host = ""
    @State private var port = "22"
    @State private var username = ""
    @State private var basePath = ""
    @State private var sshKeyPath = ""
    @State private var isTesting = false
    @State private var testPassed = false
    @State private var testError: String?

    var body: some View {
        VStack(spacing: 16) {
            Text("Add Remote Server")
                .font(.headline)

            Form {
                TextField("Label", text: $label, prompt: Text("Production Server"))
                TextField("Host", text: $host, prompt: Text("192.168.1.100"))
                TextField("Port", text: $port, prompt: Text("22"))
                TextField("Username", text: $username, prompt: Text("root"))
                TextField("Base Path", text: $basePath, prompt: Text("e.g. ~/.openclaw, ~/skills"))
                TextField("SSH Key Path", text: $sshKeyPath, prompt: Text("Optional — e.g. ~/.ssh/id_ed25519"))
            }
            .formStyle(.grouped)

            if let testError {
                Text(testError)
                    .font(.caption)
                    .foregroundStyle(.red)
            }

            if testPassed {
                Label("Connection successful", systemImage: "checkmark.circle.fill")
                    .foregroundStyle(.green)
                    .font(.caption)
            }

            HStack {
                Button("Cancel") {
                    dismiss()
                }
                .keyboardShortcut(.cancelAction)

                Spacer()

                Button("Test Connection") {
                    testConnection()
                }
                .disabled(host.isEmpty || username.isEmpty || isTesting)

                Button("Add") {
                    addServer()
                    dismiss()
                }
                .keyboardShortcut(.defaultAction)
                .disabled(label.isEmpty || host.isEmpty || username.isEmpty || basePath.isEmpty)
            }
        }
        .padding()
        .frame(width: 400)
    }

    private func testConnection() {
        isTesting = true
        testPassed = false
        testError = nil

        let server = RemoteServer(
            label: label,
            host: host,
            port: Int(port) ?? 22,
            username: username,
            skillsBasePath: basePath
        )
        server.sshKeyPath = sshKeyPath.isEmpty ? nil : sshKeyPath

        Task {
            do {
                try await SSHService.testConnection(server)
                await MainActor.run {
                    testPassed = true
                    isTesting = false
                }
            } catch {
                await MainActor.run {
                    testError = error.localizedDescription
                    isTesting = false
                }
            }
        }
    }

    private func addServer() {
        let server = RemoteServer(
            label: label,
            host: host,
            port: Int(port) ?? 22,
            username: username,
            skillsBasePath: basePath
        )
        server.sshKeyPath = sshKeyPath.isEmpty ? nil : sshKeyPath
        modelContext.insert(server)
        try? modelContext.save()

        Task {
            let scanner = SkillScanner(modelContext: modelContext)
            await scanner.scanRemoteServer(server)
        }
    }
}

// MARK: - Edit Server Sheet

private struct EditServerSheet: View {
    @Bindable var server: RemoteServer
    @Environment(\.modelContext) private var modelContext
    @Environment(\.dismiss) private var dismiss

    @State private var label: String = ""
    @State private var host: String = ""
    @State private var port: String = ""
    @State private var username: String = ""
    @State private var basePath: String = ""
    @State private var sshKeyPath: String = ""

    var body: some View {
        VStack(spacing: 16) {
            Text("Edit Server")
                .font(.headline)

            Form {
                TextField("Label", text: $label, prompt: Text("Production Server"))
                TextField("Host", text: $host, prompt: Text("192.168.1.100"))
                TextField("Port", text: $port, prompt: Text("22"))
                TextField("Username", text: $username, prompt: Text("root"))
                TextField("Base Path", text: $basePath, prompt: Text("e.g. ~/.openclaw, ~/skills"))
                TextField("SSH Key Path", text: $sshKeyPath, prompt: Text("Optional — e.g. ~/.ssh/id_ed25519"))
            }
            .formStyle(.grouped)

            HStack {
                Button("Cancel") {
                    dismiss()
                }
                .keyboardShortcut(.cancelAction)

                Spacer()

                Button("Save") {
                    let connectionChanged = server.host != host
                        || server.username != username
                        || server.skillsBasePath != basePath
                        || server.port != (Int(port) ?? 22)

                    server.label = label
                    server.host = host
                    server.port = Int(port) ?? 22
                    server.username = username
                    server.skillsBasePath = basePath
                    server.sshKeyPath = sshKeyPath.isEmpty ? nil : sshKeyPath

                    if connectionChanged {
                        // Purge stale skills — they may point to files on the old target
                        for skill in server.skills {
                            modelContext.delete(skill)
                        }
                    }

                    try? modelContext.save()
                    dismiss()

                    if connectionChanged {
                        Task {
                            let scanner = SkillScanner(modelContext: modelContext)
                            await scanner.scanRemoteServer(server)
                        }
                    }
                }
                .keyboardShortcut(.defaultAction)
                .disabled(label.isEmpty || host.isEmpty || username.isEmpty || basePath.isEmpty)
            }
        }
        .padding()
        .frame(width: 400)
        .onAppear {
            label = server.label
            host = server.host
            port = "\(server.port)"
            username = server.username
            basePath = server.skillsBasePath
            sshKeyPath = server.sshKeyPath ?? ""
        }
    }
}
```

## File: `Chops/Views/Settings/SettingsView.swift`
```
import SwiftUI
import Sparkle

extension Notification.Name {
    static let customScanPathsChanged = Notification.Name("customScanPathsChanged")
}

// MARK: - Settings Tab Definition

enum SettingsTab: String, CaseIterable, Identifiable {
    case general, library, aiAssist, scanDirs, servers, about

    var id: String { rawValue }

    var title: String {
        switch self {
        case .general: "General"
        case .library: "Library"
        case .aiAssist: "AI Assist"
        case .scanDirs: "Scan Directories"
        case .servers: "Servers"
        case .about: "About"
        }
    }

    var icon: String {
        switch self {
        case .general: "gearshape"
        case .library: "books.vertical"
        case .aiAssist: "sparkles"
        case .scanDirs: "folder.badge.gearshape"
        case .servers: "server.rack"
        case .about: "info.circle"
        }
    }
}

// MARK: - Settings View

struct SettingsView: View {
    private static let logger = AppLogger.settings

    let updater: SPUUpdater
    @State private var selectedTab: SettingsTab = .general
    @State private var customPaths: [String] = []
    @AppStorage("defaultTool") private var defaultTool: ToolSource = .claude

    var body: some View {
        VStack(spacing: 0) {
            // Tab bar
            HStack(spacing: 1) {
                ForEach(SettingsTab.allCases) { tab in
                    SettingsTabButton(tab: tab, isSelected: selectedTab == tab) {
                        selectedTab = tab
                    }
                }
            }
            .padding(.horizontal, 12)
            .padding(.top, 8)
            .padding(.bottom, 4)

            Divider()

            // Tab content — each pane sizes itself, no outer ScrollView
            tabContent
                .frame(maxWidth: .infinity, alignment: .leading)
        }
        .frame(width: 520)
        .fixedSize(horizontal: false, vertical: true)
        .onAppear {
            loadCustomPaths()
        }
    }

    @ViewBuilder
    private var tabContent: some View {
        switch selectedTab {
        case .general:
            generalSettings
        case .library:
            LibrarySettingsView()
        case .aiAssist:
            ACPSettingsView()
        case .scanDirs:
            scanSettings
        case .servers:
            RemoteServersSettingsView()
        case .about:
            aboutView
        }
    }

    private var generalSettings: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("General")
                .font(.headline)

            Picker("Default tool", selection: $defaultTool) {
                ForEach(ToolSource.allCases) { tool in
                    Text(tool.displayName).tag(tool)
                }
            }
            .frame(maxWidth: 300)
        }
        .padding()
    }

    private var scanSettings: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Custom Scan Directories")
                .font(.headline)

            Text("Add a parent directory (e.g. ~/Development) and Chops will scan each project inside it for tool-specific skills and agents.")
                .font(.caption)
                .foregroundStyle(.secondary)

            if !customPaths.isEmpty {
                VStack(spacing: 0) {
                    ForEach(customPaths, id: \.self) { path in
                        HStack {
                            Image(systemName: "folder")
                            Text(path)
                                .font(.system(.body, design: .monospaced))
                                .lineLimit(1)
                                .truncationMode(.middle)
                            Spacer()
                            Button {
                                customPaths.removeAll { $0 == path }
                                saveCustomPaths()
                            } label: {
                                Image(systemName: "minus.circle.fill")
                                    .foregroundStyle(.red)
                            }
                            .buttonStyle(.plain)
                        }
                        .padding(.vertical, 6)
                        .padding(.horizontal, 8)

                        if path != customPaths.last {
                            Divider()
                        }
                    }
                }
                .background(Color(NSColor.controlBackgroundColor))
                .clipShape(RoundedRectangle(cornerRadius: 6))
            } else {
                Text("No custom directories added.")
                    .foregroundStyle(.secondary)
                    .font(.callout)
            }

            HStack {
                Spacer()
                Button("Add Directory...") {
                    let panel = NSOpenPanel()
                    panel.canChooseFiles = false
                    panel.canChooseDirectories = true
                    panel.allowsMultipleSelection = false
                    if panel.runModal() == .OK, let url = panel.url {
                        let path = url.path
                        if !customPaths.contains(path) {
                            customPaths.append(path)
                            saveCustomPaths()
                        }
                    }
                }
            }
        }
        .padding()
    }

    private var aboutView: some View {
        VStack(spacing: 16) {
            if let icon = NSApp.applicationIconImage {
                Image(nsImage: icon)
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 80, height: 80)
            }

            Text("Chops")
                .font(.title)
                .fontWeight(.bold)

            Text("Version \(appVersion)")
                .font(.subheadline)
                .foregroundStyle(.secondary)

            Text("Your AI skills and agents, finally organized.")
                .font(.subheadline)
                .foregroundStyle(.secondary)

            HStack(spacing: 16) {
                Button("Check for Updates") {
                    updater.checkForUpdates()
                }

                Button("Website") {
                    if let url = URL(string: "https://chops.md") { NSWorkspace.shared.open(url) }
                }

                Button("@Shpigford") {
                    if let url = URL(string: "https://x.com/Shpigford") { NSWorkspace.shared.open(url) }
                }

                Button("GitHub") {
                    if let url = URL(string: "https://github.com/Shpigford/chops") { NSWorkspace.shared.open(url) }
                }
            }

            Text("Free and open source under the MIT License.")
                .font(.caption)
                .foregroundStyle(.tertiary)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 30)
    }

    private var appVersion: String {
        let version = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String ?? "?"
        let build = Bundle.main.infoDictionary?["CFBundleVersion"] as? String ?? "?"
        return "\(version) (\(build))"
    }

    private func loadCustomPaths() {
        customPaths = UserDefaults.standard.stringArray(forKey: "customScanPaths") ?? []
    }

    private func saveCustomPaths() {
        UserDefaults.standard.set(customPaths, forKey: "customScanPaths")
        NotificationCenter.default.post(name: .customScanPathsChanged, object: nil)
    }
}

// MARK: - Tab Button

private struct SettingsTabButton: View {
    let tab: SettingsTab
    let isSelected: Bool
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            VStack(spacing: 2) {
                Image(systemName: tab.icon)
                    .font(.system(size: 16))
                    .frame(height: 20)
                Text(tab.title)
                    .font(.caption2)
                    .lineLimit(1)
            }
            .frame(maxWidth: .infinity)
            .padding(.vertical, 6)
            .padding(.horizontal, 4)
            .background(isSelected ? Color.accentColor.opacity(0.15) : Color.clear)
            .clipShape(RoundedRectangle(cornerRadius: 6))
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
        .foregroundStyle(isSelected ? .primary : .secondary)
    }
}
```

## File: `Chops/Views/Shared/ACPLogViewer.swift`
```
import SwiftUI

/// Viewer for ACP debug logs
struct ACPLogViewer: View {
    @State private var logContent = ""
    @State private var debugEnabled = acpLog.debugEnabled
    @State private var autoRefresh = true
    @State private var refreshTask: Task<Void, Never>?

    var body: some View {
        VStack(spacing: 0) {
            // Toolbar
            HStack {
                Text("ACP Logs")
                    .font(.headline)

                Spacer()

                Toggle("Debug Mode", isOn: $debugEnabled)
                    .toggleStyle(.switch)
                    .controlSize(.small)
                    .onChange(of: debugEnabled) { _, newValue in
                        acpLog.debugEnabled = newValue
                    }

                Toggle("Auto-refresh", isOn: $autoRefresh)
                    .toggleStyle(.switch)
                    .controlSize(.small)

                Button {
                    refreshLogs()
                } label: {
                    Image(systemName: "arrow.clockwise")
                }
                .buttonStyle(.borderless)
                .help("Refresh")

                Button {
                    acpLog.clearLogs()
                    refreshLogs()
                } label: {
                    Image(systemName: "trash")
                }
                .buttonStyle(.borderless)
                .help("Clear Logs")

                Button {
                    NSWorkspace.shared.selectFile(acpLog.logURL.path, inFileViewerRootedAtPath: "")
                } label: {
                    Image(systemName: "folder")
                }
                .buttonStyle(.borderless)
                .help("Show in Finder")
            }
            .padding(.horizontal, 12)
            .padding(.vertical, 8)
            .background(Color(.controlBackgroundColor))

            Divider()

            // Log content
            ScrollViewReader { proxy in
                ScrollView {
                    Text(logContent)
                        .font(.system(.caption, design: .monospaced))
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .textSelection(.enabled)
                        .padding(8)
                        .id("bottom")
                }
                .onChange(of: logContent) { _, _ in
                    withAnimation {
                        proxy.scrollTo("bottom", anchor: .bottom)
                    }
                }
            }
            .background(Color(.textBackgroundColor))
        }
        .onAppear {
            refreshLogs()
            startAutoRefresh()
        }
        .onDisappear {
            refreshTask?.cancel()
        }
    }

    private func refreshLogs() {
        Task {
            let content = await acpLog.recentLogs(lines: 500)
            logContent = content
        }
    }

    private func startAutoRefresh() {
        refreshTask = Task {
            while !Task.isCancelled {
                try? await Task.sleep(for: .seconds(1))
                guard autoRefresh else { continue }
                let content = await acpLog.recentLogs(lines: 500)
                logContent = content
            }
        }
    }
}

#Preview {
    ACPLogViewer()
        .frame(width: 600, height: 400)
}
```

## File: `Chops/Views/Shared/ComposeModel.swift`
```
import Foundation

// MARK: - Chat Model

enum ChatRole { case user, assistant }

enum DiffStatus: Sendable { case pending, accepted, rejected }

struct ChatDiff: Sendable {
    let path: String
    /// Pre-edit content. `nil` means the file did not exist before the agent wrote it.
    let original: String?
    let originalData: Data?
    let existedBefore: Bool
    let proposed: String
    var status: DiffStatus = .pending
}

struct ChatMessage: Identifiable {
    let id: UUID
    let role: ChatRole
    var text: String
    var thoughtText: String
    var isError: Bool
    var diffs: [ChatDiff]

    init(
        id: UUID = UUID(),
        role: ChatRole,
        text: String,
        thoughtText: String = "",
        isError: Bool = false,
        diffs: [ChatDiff] = []
    ) {
        self.id = id
        self.role = role
        self.text = text
        self.thoughtText = thoughtText
        self.isError = isError
        self.diffs = diffs
    }
}

// MARK: - Layout Constants

enum ComposeConstants {
    static let defaultPanelHeight: CGFloat = 400
    static let bubbleWidthRatio: CGFloat = 0.80
}
```

## File: `Chops/Views/Shared/ComposePanel.swift`
```
import ACPModel
import ACPRegistry
import SwiftUI

/// Inline panel for composing/editing skill content with ACP
struct ComposePanel: View {
    @Binding var content: String
    @Binding var isVisible: Bool
    let skillName: String
    let skillDescription: String
    let frontmatter: [String: String]
    /// Absolute path of the file being edited — used to read source-of-truth from disk.
    let filePath: String
    let workingDirectory: URL
    /// Called after a diff is accepted — use to persist the change immediately.
    let onAccept: () -> Void

    @State private var selectedTemplateType: WizardTemplateType
    @State private var inputText = ""
    @AppStorage("ACPSelectedAgentId") private var selectedAgentId: String?
    @State private var acpClient: BaseACPAgent?
    @State private var showingDebugLogs = false

    /// Completed conversation history. Never holds in-flight messages — the SDK drives live state.
    @State private var messages: [ChatMessage] = []
    /// True until the first successful prompt in this session.
    @State private var isFirstTurn = true

    @AppStorage("ACPDebugLogging") private var debugLoggingEnabled = false
    @State private var panelHeight: CGFloat = ComposeConstants.defaultPanelHeight
    @State private var isDragging = false
    @State private var dragStartHeight: CGFloat?

    private static let minPanelHeight: CGFloat = 160
    private static let maxPanelHeight: CGFloat = 700

    init(
        content: Binding<String>,
        isVisible: Binding<Bool>,
        skillName: String,
        skillDescription: String = "",
        frontmatter: [String: String] = [:],
        filePath: String,
        workingDirectory: URL,
        templateType: WizardTemplateType,
        onAccept: @escaping () -> Void = {}
    ) {
        self._content = content
        self._isVisible = isVisible
        self.skillName = skillName
        self.skillDescription = skillDescription
        self.frontmatter = frontmatter
        self.filePath = filePath
        self.workingDirectory = workingDirectory
        self.onAccept = onAccept
        self._selectedTemplateType = State(initialValue: templateType)
    }

    private var configuredAgents: [RegistryAgent] { ACPConfiguration.shared.enabledAgents }
    private var selectedAgent: RegistryAgent? { configuredAgents.first { $0.id == selectedAgentId } }

    private var isConnected: Bool { acpClient?.isConnected ?? false }
    private var isConnecting: Bool { acpClient?.isConnecting ?? false }
    private var isProcessing: Bool { acpClient?.isProcessing ?? false }
    private var hasPendingDiffs: Bool { messages.contains { $0.diffs.contains { $0.status == .pending } } }

    var body: some View {
        VStack(spacing: 0) {
            resizeHandle

            if configuredAgents.isEmpty {
                noToolsConfiguredView
            } else if !isConnected && messages.isEmpty {
                agentPickerEmptyState
            } else {
                VStack(spacing: 0) {
                    topBar
                    Divider()
                    chatArea
                    Divider()
                    inputArea
                }
            }
        }
        .frame(height: panelHeight)
        .background(Color(.windowBackgroundColor))
        .onAppear {
            if selectedAgentId == nil {
                selectedAgentId = configuredAgents.first?.id
            }
        }
        .onDisappear {
            forceDisconnect()
        }
        .onChange(of: selectedAgentId) { _, _ in
            forceDisconnect()
        }
        .onChange(of: configuredAgents.map(\.id)) { _, newIds in
            if selectedAgentId == nil || !newIds.contains(selectedAgentId ?? "") {
                selectedAgentId = newIds.first
            }
        }
        .task { await ACPConfiguration.shared.loadRegistryIfNeeded() }
        .sheet(isPresented: Binding(
            get: { acpClient?.pendingPermissionRequest != nil },
            set: { if !$0 { acpClient?.respondToPermission(optionId: nil) } }
        )) {
            if let request = acpClient?.pendingPermissionRequest {
                permissionSheet(request: request)
            }
        }
    }

    @ViewBuilder
    private func permissionSheet(request: PermissionRequest) -> some View {
        VStack(alignment: .leading, spacing: 16) {
            Label("Permission Required", systemImage: "hand.raised.fill")
                .font(.headline)
            Text(request.title)
                .foregroundStyle(.secondary)
            Divider()
            VStack(alignment: .leading, spacing: 8) {
                ForEach(request.options, id: \.optionId) { option in
                    Button(option.name) {
                        acpClient?.respondToPermission(optionId: option.optionId)
                    }
                    .buttonStyle(.bordered)
                    .tint(permissionOptionTint(for: option.kind))
                }
            }
            Divider()
            Button("Cancel") {
                acpClient?.respondToPermission(optionId: nil)
            }
            .foregroundStyle(.secondary)
        }
        .padding(24)
        .frame(minWidth: 320, maxWidth: 440)
    }

    private func permissionOptionTint(for kind: String) -> Color {
        switch kind {
        case "allow_once", "allow_always": return .green
        case "reject_once", "reject_always": return .red
        default: return .secondary
        }
    }

    // MARK: - Views

    @Environment(\.openSettings) private var openSettings

    private var agentPickerEmptyState: some View {
        ZStack(alignment: .topTrailing) {
            VStack(spacing: 12) {
                Image(systemName: "sparkles")
                    .font(.largeTitle)
                    .foregroundStyle(.tertiary)
                Text("Choose an agent to get started")
                    .font(.callout)
                    .foregroundStyle(.secondary)
                Picker("", selection: $selectedAgentId) {
                    Text("Select agent…").tag(nil as String?)
                    ForEach(configuredAgents) { agent in
                        Text(agent.name).tag(Optional(agent.id))
                    }
                }
                .labelsHidden()
                .fixedSize()
                if selectedAgentId != nil {
                    if isConnecting {
                        HStack(spacing: 6) {
                            ProgressView().controlSize(.small)
                            Text("Connecting…")
                                .foregroundStyle(.secondary)
                        }
                        .font(.callout)
                    } else {
                        Button {
                            connect()
                        } label: {
                            Label("Connect", systemImage: "link")
                        }
                        .buttonStyle(.borderedProminent)
                        .controlSize(.regular)
                    }
                }
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity)

            closeButton
                .padding(12)
        }
    }

    private let configuration = ACPConfiguration.shared

    private var noToolsConfiguredView: some View {
        ZStack(alignment: .topTrailing) {
            VStack(spacing: 16) {
                Image(systemName: "sparkles")
                    .font(.largeTitle)
                    .foregroundStyle(.tertiary)
                Text("Enable an agent to get started")
                    .font(.callout)
                    .foregroundStyle(.secondary)

                VStack(spacing: 0) {
                    if configuration.isLoadingRegistry {
                        HStack(spacing: 6) {
                            ProgressView().controlSize(.small)
                            Text("Loading agents…").foregroundStyle(.secondary)
                        }
                        .padding(.vertical, 12)
                    } else {
                        ForEach(configuration.registryAgents) { agent in
                            HStack(spacing: 10) {
                                VStack(alignment: .leading, spacing: 1) {
                                    Text(agent.name)
                                        .font(.callout.weight(.medium))
                                    Text(agent.description)
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                        .lineLimit(1)
                                }
                                Spacer()
                                Toggle("", isOn: Binding(
                                    get: { configuration.isEnabled(agent.id) },
                                    set: { configuration.setEnabled(agent.id, $0) }
                                ))
                                .labelsHidden()
                            }
                            .padding(.horizontal, 12)
                            .padding(.vertical, 8)
                        }
                    }
                }
                .background(Color.primary.opacity(0.05))
                .clipShape(RoundedRectangle(cornerRadius: 8))
                .frame(maxWidth: 320)
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity)

            closeButton
                .padding(12)
        }
        .task { await configuration.loadRegistryIfNeeded() }
    }

    private var topBar: some View {
        HStack(spacing: 8) {
            // LEFT: Tool picker + connection + debug
            HStack(spacing: 8) {
                Picker("", selection: $selectedAgentId) {
                    Text("Select...").tag(nil as String?)
                    ForEach(configuredAgents) { agent in
                        Text(agent.name).tag(Optional(agent.id))
                    }
                }
                .labelsHidden()
                .frame(width: 120)

                connectionButton
                debugLogButton
            }

            Spacer()

            // Error indicator — connection errors reported by the agent.
            if let error = acpClient?.lastError {
                HStack(spacing: 4) {
                    Image(systemName: "exclamationmark.circle.fill")
                        .foregroundStyle(.red)
                    Text(error)
                        .font(.caption)
                        .foregroundStyle(.red)
                        .lineLimit(1)
                }
                .frame(maxWidth: 200)
            }

            // RIGHT: config options (when connected) + close
            HStack(spacing: 8) {
                inlineConfigOptions
                closeButton
            }
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 8)
        .background(Color(.controlBackgroundColor))
    }

    // MARK: - Config Options Bar

    /// Inline config option pickers shown in the top bar when connected.
    @ViewBuilder
    private var inlineConfigOptions: some View {
        let options = acpClient?.sessionConfigOptions ?? []
        if isConnected && !options.isEmpty {
            ForEach(options, id: \.id) { option in
                if case .select(let select) = option.kind {
                    configOptionPicker(option: option, select: select)
                }
            }
        }
    }

    @ViewBuilder
    private func configOptionPicker(option: SessionConfigOption, select: SessionConfigSelect) -> some View {
        let flatOptions: [SessionConfigSelectOption] = {
            switch select.options {
            case .ungrouped(let opts): return opts
            case .grouped(let groups): return groups.flatMap(\.options)
            }
        }()
        Picker(option.name, selection: Binding(
            get: { select.currentValue },
            set: { newValue in
                Task { try? await acpClient?.setConfigOption(id: option.id, value: newValue) }
            }
        )) {
            ForEach(flatOptions, id: \.value) { opt in
                Text(opt.name.replacingOccurrences(of: " (recommended)", with: "")).tag(opt.value)
            }
        }
        .fixedSize()
        .help(option.description ?? option.name)
    }

    // MARK: - Chat Area

    /// Completed messages worth showing — assistant turns with no text and no diffs are omitted.
    private var visibleMessages: [ChatMessage] {
        messages.filter { msg in
            guard msg.role == .assistant else { return true }
            return !msg.text.isEmpty || msg.isError || !msg.diffs.isEmpty
        }
    }

    private var chatArea: some View {
        GeometryReader { geo in
            let bubbleWidth = max(200, floor(geo.size.width * ComposeConstants.bubbleWidthRatio))
            ScrollViewReader { proxy in
                ScrollView {
                    LazyVStack(alignment: .leading, spacing: 12) {
                        if messages.isEmpty && !isProcessing {
                            if isConnected {
                                connectedPlaceholder
                                    .frame(height: geo.size.height - 24)
                            } else {
                                disconnectedPlaceholder
                                    .frame(height: geo.size.height - 24)
                            }
                        }
                        ForEach(visibleMessages) { message in
                            chatRow(message: message, bubbleWidth: bubbleWidth)
                                .id(message.id)
                        }
                        // Live assistant bubble — reads directly from the SDK while prompt is active.
                        if isProcessing {
                            liveAssistantRow(bubbleWidth: bubbleWidth)
                                .id("live-assistant")
                        }
                    }
                    .padding(12)
                }
                .background(Color(.textBackgroundColor).opacity(0.3))
                .onChange(of: messages.count) { _, _ in
                    withAnimation { proxy.scrollTo("live-assistant", anchor: .bottom) }
                }
                .onChange(of: isProcessing) { _, active in
                    if active {
                        withAnimation { proxy.scrollTo("live-assistant", anchor: .bottom) }
                    } else if let last = messages.last {
                        withAnimation { proxy.scrollTo(last.id, anchor: .bottom) }
                    }
                }
                .onChange(of: acpClient?.currentActivity) { _, _ in
                    if isProcessing {
                        withAnimation { proxy.scrollTo("live-assistant", anchor: .bottom) }
                    }
                }
            }
        }
    }

    private var disconnectedPlaceholder: some View {
        VStack(spacing: 12) {
            Image(systemName: "sparkles")
                .font(.largeTitle)
                .foregroundStyle(.tertiary)
            Text("Connect to start editing with AI")
                .font(.callout)
                .foregroundStyle(.secondary)
            Button {
                connect()
            } label: {
                Label("Connect", systemImage: "link")
            }
            .buttonStyle(.borderedProminent)
            .controlSize(.regular)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }

    private var connectedPlaceholder: some View {
        VStack(spacing: 8) {
            Text("Describe what you'd like to change")
                .font(.callout)
                .foregroundStyle(.secondary)
            Text("The agent will edit this skill based on your instructions")
                .font(.caption)
                .foregroundStyle(.tertiary)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }

    // MARK: - Live Assistant Row (SDK-driven, shown while prompt is active)

    @ViewBuilder
    private func liveAssistantRow(bubbleWidth: CGFloat) -> some View {
        let thoughtText = acpClient?.thoughtText ?? ""
        let responseText = acpClient?.responseText ?? ""
        let displayText = acpClient?.conversationalText(from: responseText) ?? responseText
        let activity = acpClient?.currentActivity

        VStack(alignment: .leading, spacing: 6) {
            if !thoughtText.isEmpty {
                ThinkingView(text: thoughtText, isStreaming: true)
                    .frame(maxWidth: bubbleWidth, alignment: .leading)
            }
            VStack(alignment: .leading, spacing: 0) {
                HStack(spacing: 4) {
                    Image(systemName: "sparkles").foregroundStyle(.secondary)
                    Text("Agent").foregroundStyle(.secondary)
                    Spacer()
                }
                .font(.caption)
                .padding(.horizontal, 10).padding(.top, 8).padding(.bottom, 4)

                Divider().padding(.horizontal, 8)

                if !displayText.isEmpty {
                    Text(displayText)
                        .font(.body)
                        .textSelection(.enabled)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .padding(.horizontal, 10).padding(.vertical, 8)
                } else if let activity {
                    HStack(spacing: 6) {
                        ProgressView().controlSize(.mini)
                        Text(activity).foregroundStyle(.secondary)
                    }
                    .font(.callout)
                    .padding(.horizontal, 10).padding(.vertical, 8)
                } else {
                    HStack(spacing: 6) {
                        ProgressView().controlSize(.mini)
                        Text("Working…").foregroundStyle(.secondary)
                    }
                    .font(.callout)
                    .padding(.horizontal, 10).padding(.vertical, 8)
                }
            }
            .frame(maxWidth: bubbleWidth, alignment: .leading)
            .background(Color.primary.opacity(0.09))
            .clipShape(RoundedRectangle(cornerRadius: 8))
            .overlay(RoundedRectangle(cornerRadius: 8).stroke(Color.secondary.opacity(0.2)))
        }
    }

    // MARK: - Completed Message Rows

    @ViewBuilder
    private func chatRow(message: ChatMessage, bubbleWidth: CGFloat) -> some View {
        VStack(alignment: message.role == .user ? .trailing : .leading, spacing: 6) {
            switch message.role {
            case .user:
                HStack(spacing: 0) {
                    Spacer(minLength: 16)
                    Text(message.text)
                        .font(.body)
                        .textSelection(.enabled)
                        .padding(.horizontal, 10)
                        .padding(.vertical, 7)
                        .background(Color.accentColor.opacity(0.22))
                        .clipShape(RoundedRectangle(cornerRadius: 8))
                        .frame(maxWidth: bubbleWidth, alignment: .trailing)
                }
            case .assistant:
                if !message.thoughtText.isEmpty {
                    ThinkingView(text: message.thoughtText, isStreaming: false)
                        .frame(maxWidth: bubbleWidth, alignment: .leading)
                }
                assistantCard(message: message)
                    .frame(maxWidth: bubbleWidth, alignment: .leading)
            }
            ForEach(message.diffs.indices, id: \.self) { i in
                diffCard(messageId: message.id, diffIndex: i, diff: message.diffs[i])
            }
        }
    }

    @ViewBuilder
    private func assistantCard(message: ChatMessage) -> some View {
        let displayText = message.text

        VStack(alignment: .leading, spacing: 0) {
            HStack(spacing: 4) {
                if message.isError {
                    Image(systemName: "exclamationmark.triangle.fill").foregroundStyle(.orange)
                    Text("Error").foregroundStyle(.orange)
                } else {
                    Image(systemName: "sparkles").foregroundStyle(.secondary)
                    Text("Agent").foregroundStyle(.secondary)
                }
                Spacer()
            }
            .font(.caption)
            .padding(.horizontal, 10)
            .padding(.top, 8)
            .padding(.bottom, 4)

            Divider()
                .padding(.horizontal, 8)

            if message.isError {
                Text(displayText)
                    .font(.body.italic())
                    .foregroundStyle(.orange)
                    .textSelection(.enabled)
                    .padding(.horizontal, 10)
                    .padding(.vertical, 8)
            } else if !displayText.isEmpty {
                MarkdownMessageView(text: displayText)
                    .font(.body)
                    .padding(.horizontal, 10)
                    .padding(.vertical, 8)
            }
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        // Use a primary-relative tint so the card is visibly distinct from the window
        // background in both light and dark mode (controlBackgroundColor is too similar).
        .background(message.isError ? Color.orange.opacity(0.08) : Color.primary.opacity(0.09))
        .clipShape(RoundedRectangle(cornerRadius: 8))
        .overlay(
            RoundedRectangle(cornerRadius: 8)
                .stroke(message.isError ? Color.orange.opacity(0.35) : Color.secondary.opacity(0.2))
        )
    }

    @ViewBuilder
    private func diffCard(messageId: UUID, diffIndex: Int, diff: ChatDiff) -> some View {
        switch diff.status {
        case .accepted:
            HStack(spacing: 6) {
                Label("Changes accepted", systemImage: "checkmark.circle.fill")
                    .foregroundStyle(.green)
                Text("· \(diff.path.split(separator: "/").last.map(String.init) ?? diff.path)")
                    .foregroundStyle(.secondary)
            }
            .font(.caption)
            .padding(.horizontal, 8)
        case .rejected:
            HStack(spacing: 6) {
                Label("Changes rejected", systemImage: "xmark.circle.fill")
                    .foregroundStyle(.secondary)
                Text("· \(diff.path.split(separator: "/").last.map(String.init) ?? diff.path)")
                    .foregroundStyle(.secondary)
            }
            .font(.caption)
            .padding(.horizontal, 8)
        case .pending:
            DiffReviewPanel(
                original: diff.original ?? "",
                proposed: diff.proposed,
                onAccept: { acceptDiff(messageId: messageId, diffIndex: diffIndex) },
                onReject: { rejectDiff(messageId: messageId, diffIndex: diffIndex) }
            )
            .frame(height: 260)
            .clipShape(RoundedRectangle(cornerRadius: 8))
            .overlay(RoundedRectangle(cornerRadius: 8).stroke(Color.secondary.opacity(0.2)))
        }
    }

    // MARK: - Input Area

    private var sendDisabled: Bool {
        !isConnected || inputText.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty || isProcessing || hasPendingDiffs
    }

    private var inputArea: some View {
        HStack(alignment: .bottom, spacing: 8) {
            TextField(isFirstTurn ? "Enter instructions…" : "Follow up…", text: $inputText, axis: .vertical)
                .font(.body)
                .textFieldStyle(.plain)
                .lineLimit(1...4)
                .disabled(isProcessing || !isConnected || hasPendingDiffs)
                .onSubmit {
                    if !sendDisabled { sendMessage() }
                }
                .padding(.horizontal, 8)
                .padding(.vertical, 8)
                .background(Color(.textBackgroundColor))
                .clipShape(RoundedRectangle(cornerRadius: 8))
                .overlay(RoundedRectangle(cornerRadius: 8).stroke(Color.secondary.opacity(0.25)))

            if isProcessing {
                Button {
                    acpClient?.cancelPrompt()
                } label: {
                    Image(systemName: "stop.fill")
                        .font(.body)
                        .foregroundStyle(.white)
                        .frame(width: 36)
                        .frame(maxHeight: .infinity)
                        .background(Color.red.opacity(0.8))
                        .clipShape(RoundedRectangle(cornerRadius: 8))
                }
                .buttonStyle(.plain)
                .help("Stop (⌘.)")
                .keyboardShortcut(".", modifiers: .command)
            } else {
                Button {
                    sendMessage()
                } label: {
                    Image(systemName: "paperplane.fill")
                        .font(.body)
                        .foregroundStyle(.white)
                        .frame(width: 36)
                        .frame(maxHeight: .infinity)
                        .background(sendDisabled ? Color.accentColor.opacity(0.4) : Color.accentColor)
                        .clipShape(RoundedRectangle(cornerRadius: 8))
                }
                .buttonStyle(.plain)
                .disabled(sendDisabled)
                .keyboardShortcut(.return, modifiers: .command)
                .help("Send (⌘↩)")
            }
        }
        .fixedSize(horizontal: false, vertical: true)
        .padding(.horizontal, 12)
        .padding(.vertical, 8)
        .background(Color(.controlBackgroundColor))
    }

    private var resizeHandle: some View {
        VStack(spacing: 0) {
            Color(.separatorColor)
                .frame(height: 1)
            RoundedRectangle(cornerRadius: 2)
                .fill(Color.secondary.opacity(isDragging ? 0.5 : 0.25))
                .frame(width: 36, height: 4)
                .padding(.vertical, 3)
        }
        .frame(maxWidth: .infinity)
        .contentShape(Rectangle())
        .onHover { hovering in
            if hovering {
                NSCursor.resizeUpDown.push()
            } else {
                NSCursor.pop()
            }
        }
        .gesture(
            DragGesture(minimumDistance: 1)
                .onChanged { value in
                    isDragging = true
                    if dragStartHeight == nil {
                        dragStartHeight = panelHeight
                    }
                    let newHeight = (dragStartHeight ?? panelHeight) - value.translation.height
                    panelHeight = max(Self.minPanelHeight, min(Self.maxPanelHeight, newHeight))
                }
                .onEnded { _ in
                    isDragging = false
                    dragStartHeight = nil
                }
        )
    }

    private var connectionButton: some View {
        Button {
            if isConnected || isConnecting {
                forceDisconnect()
            } else {
                connect()
            }
        } label: {
            Group {
                if isConnecting {
                    ProgressView().controlSize(.mini)
                } else {
                    Image(systemName: "link")
                        .foregroundStyle(isConnected ? .green : .red)
                }
            }
            .frame(width: 20, height: 20)
        }
        .buttonStyle(.plain)
        .help(isConnected ? "Disconnect" : isConnecting ? "Cancel connection" : "Connect to \(selectedAgent?.name ?? "agent")")
        .disabled(selectedAgentId == nil)
    }

    private var closeButton: some View {
        Button {
            forceDisconnect()
            isVisible = false
        } label: {
            Image(systemName: "xmark")
                .frame(width: 28, height: 28)
                .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
        .foregroundStyle(.secondary)
    }

    @ViewBuilder
    private var debugLogButton: some View {
        if debugLoggingEnabled {
            Button {
                showingDebugLogs = true
            } label: {
                Image(systemName: "ladybug")
                    .foregroundStyle(.orange)
            }
            .buttonStyle(.plain)
            .help("View ACP Logs")
            .popover(isPresented: $showingDebugLogs) {
                ACPLogViewer()
                    .frame(width: 600, height: 400)
            }
        }
    }

    // MARK: - Actions

    private func connect() {
        guard let agent = selectedAgent, !isConnected, !isConnecting else { return }
        let client = ACPAgentFactory.make(for: agent.id)
        acpClient = client  // agent's @Observable state drives the UI from this point
        let systemPrompt = TemplateManager.shared.systemPrompt(
            for: selectedTemplateType,
            skillName: skillName,
            skillDescription: skillDescription,
            filePath: filePath,
            frontmatter: frontmatter
        )
        client.startConnect(agent: agent, workingDirectory: workingDirectory, systemPrompt: systemPrompt)
    }

    private func sendMessage() {
        guard let client = acpClient else { return }
        let text = inputText.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !text.isEmpty else { return }

        inputText = ""
        messages.append(ChatMessage(role: .user, text: text))

        let assistantId = UUID()

        Task {
            do {
                let fp = filePath
                let original: String? = await readFile(at: fp)
                guard let original else {
                    messages.append(ChatMessage(id: assistantId, role: .assistant, text: "Cannot read file: \(filePath)", isError: true))
                    return
                }
                let prompt = buildPrompt(text: text, originalContent: original)
                try await client.prompt(prompt)
                isFirstTurn = false

                let raw = client.responseText
                let processed = client.conversationalText(from: raw)
                let finalText = processed.isEmpty ? raw : processed
                acpLog.info("Compose: turn done — raw=\(raw.count) chars, thought=\(client.thoughtText.count) chars")

                messages.append(ChatMessage(id: assistantId, role: .assistant, text: finalText, thoughtText: client.thoughtText))
                await handleWrites(client: client, messageId: assistantId, filePath: fp, originalContent: original)
            } catch {
                client.clearPendingWrites()
                messages.append(ChatMessage(id: assistantId, role: .assistant, text: error.localizedDescription, isError: true))
            }
        }
    }

    /// Reads a file off the main actor (UTF-8 with UTF-16 fallback).
    private func readFile(at path: String) async -> String? {
        await Task.detached(priority: .userInitiated) {
            (try? String(contentsOfFile: path, encoding: .utf8))
                ?? (try? String(contentsOfFile: path, encoding: .utf16))
        }.value
    }

    /// Expands the template on the first turn; returns plain text on subsequent turns.
    private func buildPrompt(text: String, originalContent: String) -> String {
        guard isFirstTurn, let template = TemplateManager.shared.template(for: selectedTemplateType) else {
            return text
        }
        return template.content
            .replacingOccurrences(of: "{{file_content}}", with: originalContent.isEmpty ? "(empty)" : originalContent)
            .replacingOccurrences(of: "{{user_instructions}}", with: text)
    }

    /// Attaches diffs from pending writes or disk changes; logs text-only turns.
    private func handleWrites(client: BaseACPAgent, messageId: UUID, filePath: String, originalContent: String) async {
        acpLog.info("Compose: handleWrites — filePath=\(filePath) originalContent.count=\(originalContent.count)")
        if !client.pendingWrites.isEmpty {
            acpLog.info("Compose: attaching \(client.pendingWrites.count) diff(s) from write_text_file")
            await attachDiffs(messageId: messageId, writes: client.pendingWrites, fallbackOriginal: originalContent)
            client.clearPendingWrites()
            return
        }
        client.clearPendingWrites()
        let newContent = await readFile(at: filePath) ?? originalContent
        if newContent != originalContent {
            await attachDiffs(
                messageId: messageId,
                writes: [
                    PendingWrite(
                        path: filePath,
                        content: newContent,
                        originalText: originalContent,
                        originalData: originalContent.data(using: .utf8),
                        existedBefore: true
                    )
                ],
                fallbackOriginal: originalContent
            )
        }
    }

    /// Converts pending writes into ChatDiff entries and attaches them to the message.
    /// Uses the pre-write snapshot captured by the ACP layer; do not reread disk here because
    /// the agent may already have mutated the file.
    /// Resolves `path` through symlinks so that e.g. a `.cursor/rules/foo.md` symlink
    /// and its target `~/.aidevtools/rules/foo.md` compare as equal.
    private func resolvedPath(_ path: String) -> String {
        URL(fileURLWithPath: path).resolvingSymlinksInPath().path
    }

    private func attachDiffs(
        messageId: UUID,
        writes: [PendingWrite],
        fallbackOriginal: String
    ) async {
        guard let idx = messages.firstIndex(where: { $0.id == messageId }) else { return }
        let resolvedFilePath = resolvedPath(filePath)
        acpLog.debug("Compose: attachDiffs — filePath=\(filePath) resolved=\(resolvedFilePath) fallback.count=\(fallbackOriginal.count)")
        var diffs: [ChatDiff] = []
        for write in writes {
            let writtenResolved = resolvedPath(write.path)
            let original: String?
            let originalData: Data?
            let existedBefore: Bool
            if let embedded = write.originalText {
                // Agent supplied the pre-edit content (e.g. DiffContent.oldText) — use it directly.
                original = embedded
                originalData = write.originalData
                existedBefore = write.existedBefore
            } else if write.path == filePath || writtenResolved == resolvedFilePath {
                // Path matches (accounting for symlinks) — use the in-memory content from before the turn.
                original = fallbackOriginal
                originalData = fallbackOriginal.data(using: .utf8)
                existedBefore = true
            } else {
                original = write.originalText
                originalData = write.originalData
                existedBefore = write.existedBefore
            }
            acpLog.debug("Compose: diff \(write.path) original=\(original?.count ?? -1) chars")
            diffs.append(
                ChatDiff(
                    path: write.path,
                    original: original,
                    originalData: originalData,
                    existedBefore: existedBefore,
                    proposed: write.content
                )
            )
        }
        messages[idx].diffs = diffs
    }

    private func pendingDiffs() -> [ChatDiff] {
        messages.flatMap(\.diffs).filter { $0.status == .pending }
    }

    nonisolated private static func revertDiffOnDisk(_ diff: ChatDiff) {
        let url = URL(fileURLWithPath: diff.path)
        if diff.existedBefore {
            do {
                if let originalData = diff.originalData {
                    try originalData.write(to: url)
                } else if let original = diff.original {
                    try original.write(to: url, atomically: true, encoding: .utf8)
                } else {
                    acpLog.error("Reject failed: missing original snapshot for \(diff.path)")
                }
            } catch {
                acpLog.error("Reject failed writing \(diff.path): \(error.localizedDescription)")
            }
        } else {
            do {
                try FileManager.default.removeItem(at: url)
            } catch {
                acpLog.error("Reject failed removing \(diff.path): \(error.localizedDescription)")
            }
        }
    }

    private func acceptDiff(messageId: UUID, diffIndex: Int) {
        guard let msgIdx = messages.firstIndex(where: { $0.id == messageId }),
              diffIndex < messages[msgIdx].diffs.count else { return }
        let diff = messages[msgIdx].diffs[diffIndex]
        messages[msgIdx].diffs[diffIndex].status = .accepted
        if resolvedPath(diff.path) == resolvedPath(filePath) {
            content = diff.proposed
            onAccept()
        }
    }

    private func rejectDiff(messageId: UUID, diffIndex: Int) {
        guard let msgIdx = messages.firstIndex(where: { $0.id == messageId }),
              diffIndex < messages[msgIdx].diffs.count else { return }
        let diff = messages[msgIdx].diffs[diffIndex]
        messages[msgIdx].diffs[diffIndex].status = .rejected
        Task.detached(priority: .userInitiated) {
            Self.revertDiffOnDisk(diff)
        }
    }

    private func forceDisconnect() {
        let client = acpClient
        let pendingDiffs = pendingDiffs()
        acpClient = nil
        isFirstTurn = true
        messages = []
        Task {
            if !pendingDiffs.isEmpty {
                await Task.detached(priority: .userInitiated) {
                    pendingDiffs.forEach(Self.revertDiffOnDisk)
                }.value
            }
            await client?.disconnect()
        }
    }
}

// MARK: - Preview

#Preview {
    @Previewable @State var content = "# Sample Skill\n\nThis is sample content."
    @Previewable @State var isVisible = true
    VStack {
        Text("Editor content above")
            .frame(maxWidth: .infinity, maxHeight: .infinity)
        ComposePanel(
            content: $content,
            isVisible: $isVisible,
            skillName: "sample-skill",
            filePath: "/tmp/sample-skill.md",
            workingDirectory: URL(fileURLWithPath: "/tmp"),
            templateType: .skill
        )
    }
    .frame(width: 600, height: 400)
}
```

## File: `Chops/Views/Shared/DiffReviewPanel.swift`
```
import SwiftUI

// MARK: - Diff Model

enum DiffLineKind {
    case unchanged, added, removed

    var prefix: String {
        switch self {
        case .unchanged: " "
        case .added:     "+"
        case .removed:   "-"
        }
    }

    var prefixColor: Color {
        switch self {
        case .unchanged: .secondary
        case .added:     .green
        case .removed:   .red
        }
    }

    var background: Color {
        switch self {
        case .unchanged: .clear
        case .added:     Color.green.opacity(0.12)
        case .removed:   Color.red.opacity(0.12)
        }
    }
}

struct DiffLine: Identifiable {
    let id = UUID()
    let text: String
    let kind: DiffLineKind
}

// MARK: - LCS Diff Engine

/// Computes a unified diff via LCS. O(n·m) — suitable for files up to ~3 000 lines.
/// Must not be called on the main actor for large inputs; use Task.detached at the call site.
func computeDiff(from original: String, to proposed: String) -> [DiffLine] {
    let a = original.components(separatedBy: .newlines)
    let b = proposed.components(separatedBy: .newlines)

    let m = a.count, n = b.count

    // Guard: ClosedRange 1...0 traps at runtime; handle empty inputs explicitly.
    guard m > 0, n > 0 else {
        let removals = a.map { DiffLine(text: $0, kind: .removed) }
        let additions = b.map { DiffLine(text: $0, kind: .added) }
        return removals + additions
    }

    // Guard: prevent OOM on very large files. Beyond 3 000 lines the LCS matrix
    // exceeds ~72 MB. Treat oversized input as a full replacement diff.
    let lineLimit = 3_000
    guard m <= lineLimit, n <= lineLimit else {
        let removals = a.map { DiffLine(text: $0, kind: .removed) }
        let additions = b.map { DiffLine(text: $0, kind: .added) }
        return removals + additions
    }

    var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
    for i in 1...m {
        for j in 1...n {
            dp[i][j] = a[i-1] == b[j-1] ? dp[i-1][j-1] + 1 : max(dp[i-1][j], dp[i][j-1])
        }
    }

    // Backtrack to collect LCS pairs (originalIndex, proposedIndex)
    var pairs: [(Int, Int)] = []
    var i = m, j = n
    while i > 0 && j > 0 {
        if a[i-1] == b[j-1] { pairs.append((i-1, j-1)); i -= 1; j -= 1 }
        else if dp[i-1][j] >= dp[i][j-1] { i -= 1 } else { j -= 1 }
    }
    pairs.reverse()

    // Walk both arrays, emitting diff lines
    var result: [DiffLine] = []
    var ai = 0, bi = 0
    for (oi, pi) in pairs {
        while ai < oi { result.append(DiffLine(text: a[ai], kind: .removed)); ai += 1 }
        while bi < pi { result.append(DiffLine(text: b[bi], kind: .added));   bi += 1 }
        result.append(DiffLine(text: a[ai], kind: .unchanged))
        ai += 1; bi += 1
    }
    while ai < m { result.append(DiffLine(text: a[ai], kind: .removed)); ai += 1 }
    while bi < n { result.append(DiffLine(text: b[bi], kind: .added));   bi += 1 }
    return result
}

// MARK: - DiffReviewPanel

/// Shows a unified diff between `original` and `proposed` with Accept / Reject controls.
struct DiffReviewPanel: View {
    let original: String
    let proposed: String
    let onAccept: () -> Void
    let onReject: () -> Void

    @State private var lines: [DiffLine] = []

    private var addedCount:   Int { lines.filter { $0.kind == .added   }.count }
    private var removedCount: Int { lines.filter { $0.kind == .removed }.count }

    var body: some View {
        VStack(spacing: 0) {
            header
            Divider()
            diffScroll
        }
        .task {
            // Compute off the main actor — LCS allocates O(n·m) memory; blocks UI for large files.
            let result = await Task.detached(priority: .userInitiated) {
                computeDiff(from: original, to: proposed)
            }.value
            lines = result
        }
    }

    // MARK: - Subviews

    private var header: some View {
        HStack(spacing: 10) {
            Image(systemName: "plusminus")
                .foregroundStyle(.secondary)

            Label("+\(addedCount)", systemImage: "")
                .font(.caption.monospaced())
                .foregroundStyle(.green)
            Label("-\(removedCount)", systemImage: "")
                .font(.caption.monospaced())
                .foregroundStyle(.red)

            Spacer()

            Text("Review Changes")
                .font(.caption)
                .foregroundStyle(.secondary)

            Spacer()

            Button("Reject", action: onReject)
                .buttonStyle(.bordered)
                .controlSize(.small)

            Button("Accept", action: onAccept)
                .buttonStyle(.borderedProminent)
                .controlSize(.small)
                .tint(.green)
                .keyboardShortcut(.return, modifiers: .command)
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 6)
        .background(Color(.controlBackgroundColor))
    }

    private var diffScroll: some View {
        ScrollView {
            LazyVStack(alignment: .leading, spacing: 0) {
                ForEach(lines) { line in
                    HStack(alignment: .top, spacing: 4) {
                        Text(line.kind.prefix)
                            .font(.system(.caption2, design: .monospaced))
                            .foregroundStyle(line.kind.prefixColor)
                            .frame(width: 10, alignment: .center)
                        Text(line.text.isEmpty ? " " : line.text)
                            .font(.system(.caption2, design: .monospaced))
                            .foregroundStyle(line.kind == .unchanged ? .primary : line.kind.prefixColor)
                            .frame(maxWidth: .infinity, alignment: .leading)
                    }
                    .padding(.horizontal, 8)
                    .padding(.vertical, 1)
                    .background(line.kind.background)
                }
            }
        }
        .background(Color(.textBackgroundColor))
    }
}

// MARK: - Preview

#Preview {
    DiffReviewPanel(
        original: "# My Skill\n\nOld content here.\nLine two.\n",
        proposed: "# My Skill\n\nNew content here.\nLine two.\nLine three added.\n",
        onAccept: {},
        onReject: {}
    )
    .frame(width: 600, height: 300)
}
```

## File: `Chops/Views/Shared/MarkdownMessageView.swift`
```
import SwiftUI

struct MarkdownMessageView: View {
    let text: String
    @State private var attributed: AttributedString?

    var body: some View {
        Text(attributed ?? AttributedString(text))
            .textSelection(.enabled)
            .frame(maxWidth: .infinity, alignment: .leading)
            .fixedSize(horizontal: false, vertical: true)
            .task(id: text) {
                let normalized = normalize(text)
                attributed = (try? AttributedString(markdown: normalized, options: .init(
                    allowsExtendedAttributes: true,
                    interpretedSyntax: .inlineOnlyPreservingWhitespace,
                    failurePolicy: .returnPartiallyParsedIfPossible
                ))) ?? AttributedString(normalized)
            }
    }

    private func normalize(_ input: String) -> String {
        var result = input
        while result.contains("\n\n\n") {
            result = result.replacingOccurrences(of: "\n\n\n", with: "\n\n")
        }
        return result.trimmingCharacters(in: .newlines)
    }
}
```

## File: `Chops/Views/Shared/NewSkillSheet.swift`
```
import SwiftUI
import SwiftData

struct NewSkillSheet: View {
    @Environment(\.dismiss) private var dismiss
    @Environment(\.modelContext) private var modelContext
    @Environment(AppState.self) private var appState
    @State private var skillName = ""
    @State private var selectedTool: ToolSource = .claude
    @State private var errorMessage: String?

    private var itemKind: ItemKind { appState.newItemKind }

    private var creatableTools: [ToolSource] {
        switch itemKind {
        case .skill:
            return [.claude, .agents, .cursor, .codex, .amp, .opencode, .pi, .antigravity]
        case .agent:
            return ToolSource.allCases.filter { !$0.globalAgentPaths.isEmpty }
        case .rule:
            return ToolSource.allCases.filter { !$0.globalRulePaths.isEmpty }
        }
    }

    var body: some View {
        VStack(spacing: 20) {
            Text("New \(itemKind.singularName)")
                .font(.title2)
                .fontWeight(.bold)

            Form {
                TextField("\(itemKind.singularName) name", text: $skillName)
                    .textFieldStyle(.roundedBorder)

                Picker("Tool", selection: $selectedTool) {
                    ForEach(creatableTools) { tool in
                        Label(tool.displayName, systemImage: tool.iconName)
                            .tag(tool)
                    }
                }
            }
            .formStyle(.grouped)

            if let error = errorMessage {
                Text(error)
                    .font(.caption)
                    .foregroundStyle(.red)
            }

            HStack {
                Button("Cancel") {
                    dismiss()
                }
                .keyboardShortcut(.cancelAction)

                Spacer()

                Button("Create") {
                    createItem()
                }
                .keyboardShortcut(.defaultAction)
                .disabled(skillName.isEmpty)
            }
        }
        .padding(24)
        .frame(width: 400)
        .onAppear {
            // Ensure selectedTool is valid for the current item kind
            if !creatableTools.contains(selectedTool) {
                selectedTool = creatableTools.first ?? .claude
            }
        }
    }

    private func createItem() {
        let fm = FileManager.default
        let configHome: String = {
            if let xdg = ProcessInfo.processInfo.environment["XDG_CONFIG_HOME"], !xdg.isEmpty {
                return xdg
            }
            return "\(fm.homeDirectoryForCurrentUser.path)/.config"
        }()
        let sanitizedName = skillName
            .lowercased()
            .replacingOccurrences(of: " ", with: "-")
            .filter { $0.isLetter || $0.isNumber || $0 == "-" }

        guard !sanitizedName.isEmpty else {
            errorMessage = "Invalid name"
            return
        }

        let basePath: String
        let fileName: String

        switch itemKind {
        case .agent:
            guard let dir = selectedTool.globalAgentPaths.first else {
                errorMessage = "This tool doesn't support agents"
                return
            }
            basePath = "\(dir)/\(sanitizedName)"
            fileName = "\(sanitizedName).md"
        case .rule:
            guard let dir = selectedTool.globalRulePaths.first else {
                errorMessage = "This tool doesn't support rules"
                return
            }
            basePath = dir
            fileName = "\(sanitizedName).md"
        case .skill:
            guard let dir = selectedTool.globalPaths.first else {
                errorMessage = "This tool doesn't support skills"
                return
            }
            basePath = "\(dir)/\(sanitizedName)"
            fileName = "SKILL.md"
        }

        do {
            try fm.createDirectory(atPath: basePath, withIntermediateDirectories: true)

            let filePath = "\(basePath)/\(fileName)"

            guard !fm.fileExists(atPath: filePath) else {
                errorMessage = "A \(itemKind.singularName.lowercased()) with this name already exists"
                return
            }

            let boilerplate = generateBoilerplate(name: skillName, skillID: sanitizedName, tool: selectedTool)
            try boilerplate.write(toFile: filePath, atomically: true, encoding: .utf8)

            let parsed = FrontmatterParser.parse(boilerplate)
            let skill = Skill(
                filePath: filePath,
                toolSource: selectedTool,
                isDirectory: itemKind != .rule,
                name: skillName,
                skillDescription: parsed.description,
                content: parsed.content,
                frontmatter: parsed.frontmatter,
                fileModifiedDate: .now,
                fileSize: boilerplate.count,
                isGlobal: true,
                resolvedPath: filePath,
                kind: itemKind
            )
            modelContext.insert(skill)
            try modelContext.save()

            switch itemKind {
            case .skill: appState.sidebarFilter = .allSkills
            case .agent: appState.sidebarFilter = .allAgents
            case .rule: appState.sidebarFilter = .allRules
            }
            appState.selectedSkill = skill
            dismiss()
        } catch {
            errorMessage = error.localizedDescription
        }
    }

    private func generateBoilerplate(name: String, skillID: String, tool: ToolSource) -> String {
        switch itemKind {
        case .agent:
            return """
            ---
            name: \(skillID)
            description: \(name)
            ---

            # \(name)

            ## Instructions

            Add your agent instructions here.
            """
        case .rule:
            return """
            # \(name)

            Add your rule content here.
            """
        case .skill:
            switch tool {
            case .claude, .cursor:
                return """
                ---
                name: \(skillID)
                description: \(name)
                ---

                # \(name)

                ## When to Use

                - Describe when this skill should be activated

                ## Instructions

                Add your skill instructions here.
                """
            default:
                return """
                ---
                name: \(skillID)
                description: \(name)
                ---

                # \(name)

                ## Instructions

                Add your skill instructions here.
                """
            }
        }
    }
}
```

## File: `Chops/Views/Shared/RegistrySheet.swift`
```
import SwiftUI

struct RegistrySheet: View {
    @Environment(\.dismiss) private var dismiss
    @State private var registry = SkillRegistry()
    @State private var searchText = ""
    @State private var results: [SkillRegistry.RegistrySkill] = []
    @State private var selectedSkill: SkillRegistry.RegistrySkill?
    @State private var skillContent: String?
    @State private var selectedAgents: Set<String> = []
    @State private var isSearching = false
    @State private var isFetchingContent = false
    @State private var isInstalling = false
    @State private var error: String?
    @State private var installSuccess = false
    @State private var searchTask: Task<Void, Never>?
    @State private var contentTask: Task<Void, Never>?

    private var installedAgents: [AgentTarget] {
        AgentTarget.installed
    }

    var body: some View {
        VStack(spacing: 0) {
            // Header
            HStack {
                if selectedSkill != nil {
                    Button {
                        withAnimation {
                            contentTask?.cancel()
                            selectedSkill = nil
                            skillContent = nil
                            error = nil
                            installSuccess = false
                            isFetchingContent = false
                        }
                    } label: {
                        Label("Back", systemImage: "chevron.left")
                    }
                    .buttonStyle(.plain)
                }

                Spacer()

                Text(selectedSkill != nil ? "Install Skill" : "Browse Skills")
                    .font(.title3)
                    .fontWeight(.semibold)

                Spacer()

                Button("Cancel") { dismiss() }
                    .keyboardShortcut(.cancelAction)
            }
            .padding(.horizontal, 20)
            .padding(.top, 20)
            .padding(.bottom, 12)

            Divider()

            if let skill = selectedSkill {
                installView(skill: skill)
            } else {
                searchView
            }
        }
        .frame(width: 560, height: 500)
        .onAppear {
            // Pre-select all installed agents
            selectedAgents = Set(installedAgents.map(\.id))
        }
        .onDisappear {
            searchTask?.cancel()
            contentTask?.cancel()
        }
    }

    // MARK: - Search Phase

    private var searchView: some View {
        VStack(spacing: 0) {
            // Search field
            HStack {
                Image(systemName: "magnifyingglass")
                    .foregroundStyle(.secondary)
                TextField("Search skills (e.g. react, testing, deploy)...", text: $searchText)
                    .textFieldStyle(.plain)
                if isSearching {
                    ProgressView()
                        .controlSize(.small)
                }
            }
            .padding(10)
            .background(.quaternary.opacity(0.5))
            .clipShape(RoundedRectangle(cornerRadius: 8))
            .padding(.horizontal, 20)
            .padding(.vertical, 12)
            .onChange(of: searchText) { _, newValue in
                debounceSearch(query: newValue)
            }

            Divider()

            // Results
            if results.isEmpty && !isSearching && searchText.isEmpty {
                ContentUnavailableView {
                    Label("Search the Skills Registry", systemImage: "globe")
                } description: {
                    Text("Find and install skills from the open agent skills ecosystem.")
                }
                .frame(maxHeight: .infinity)
            } else if results.isEmpty && !isSearching && !searchText.isEmpty {
                ContentUnavailableView.search(text: searchText)
                    .frame(maxHeight: .infinity)
            } else {
                List(results) { skill in
                    Button {
                        selectSkill(skill)
                    } label: {
                        HStack {
                            VStack(alignment: .leading, spacing: 3) {
                                Text(skill.name)
                                    .fontWeight(.medium)
                                Text(skill.source)
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                            }
                            Spacer()
                            Text("\(skill.formattedInstalls) installs")
                                .font(.caption)
                                .foregroundStyle(.tertiary)
                        }
                        .contentShape(Rectangle())
                    }
                    .buttonStyle(.plain)
                }
                .listStyle(.plain)
            }

            if let error {
                Text(error)
                    .font(.caption)
                    .foregroundStyle(.red)
                    .padding(.horizontal, 20)
                    .padding(.bottom, 8)
            }
        }
    }

    // MARK: - Install Phase

    private func installView(skill: SkillRegistry.RegistrySkill) -> some View {
        VStack(spacing: 0) {
            if isFetchingContent {
                Spacer()
                ProgressView("Loading skill content...")
                Spacer()
            } else if let content = skillContent {
                // Content preview
                ScrollView {
                    Text(content)
                        .font(.system(.caption, design: .monospaced))
                        .textSelection(.enabled)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .padding(16)
                }
                .frame(maxHeight: 200)
                .background(.quaternary.opacity(0.3))

                Divider()

                // Agent selection
                VStack(alignment: .leading, spacing: 6) {
                    HStack {
                        Text("Install to:")
                            .font(.subheadline)
                            .fontWeight(.medium)

                        Spacer()

                        if !installedAgents.isEmpty {
                            let allSelected = selectedAgents.count == installedAgents.count
                            Button(allSelected ? "Deselect All" : "Select All") {
                                if allSelected {
                                    selectedAgents.removeAll()
                                } else {
                                    selectedAgents = Set(installedAgents.map(\.id))
                                }
                            }
                            .font(.caption)
                            .buttonStyle(.plain)
                            .foregroundColor(.accentColor)
                        }
                    }

                    if installedAgents.isEmpty {
                        Text("No supported agents detected on this machine.")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    } else {
                        ScrollView {
                            VStack(spacing: 0) {
                                ForEach(installedAgents) { agent in
                                    HStack(spacing: 8) {
                                        Image(systemName: selectedAgents.contains(agent.id) ? "checkmark.circle.fill" : "circle")
                                            .foregroundColor(selectedAgents.contains(agent.id) ? .accentColor : .secondary)
                                            .font(.system(size: 14))

                                        Text(agent.displayName)
                                            .font(.system(size: 12))

                                        Spacer()
                                    }
                                    .contentShape(Rectangle())
                                    .onTapGesture {
                                        if selectedAgents.contains(agent.id) {
                                            selectedAgents.remove(agent.id)
                                        } else {
                                            selectedAgents.insert(agent.id)
                                        }
                                    }
                                    .padding(.vertical, 4)
                                    .padding(.horizontal, 4)
                                }
                            }
                        }
                        .frame(maxHeight: 140)
                    }
                }
                .padding(.horizontal, 20)
                .padding(.vertical, 10)

                Divider()

                // Install button
                HStack {
                    if let error {
                        Text(error)
                            .font(.caption)
                            .foregroundStyle(.red)
                            .lineLimit(2)
                    }

                    if installSuccess {
                        Label("Installed!", systemImage: "checkmark.circle.fill")
                            .font(.caption)
                            .foregroundStyle(.green)
                    }

                    Spacer()

                    Button {
                        performInstall(content: content, skillName: skill.skillId)
                    } label: {
                        if isInstalling {
                            ProgressView()
                                .controlSize(.small)
                        } else {
                            Text("Install")
                        }
                    }
                    .keyboardShortcut(.defaultAction)
                    .disabled(selectedAgents.isEmpty || isInstalling || installSuccess)
                }
                .padding(.horizontal, 20)
                .padding(.vertical, 12)
            } else if let error {
                Spacer()
                VStack(spacing: 8) {
                    Image(systemName: "exclamationmark.triangle")
                        .font(.title2)
                        .foregroundStyle(.secondary)
                    Text(error)
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                Spacer()
            }
        }
    }

    // MARK: - Actions

    private func debounceSearch(query: String) {
        searchTask?.cancel()
        error = nil

        guard query.count >= 2 else {
            results = []
            return
        }

        searchTask = Task {
            try? await Task.sleep(for: .milliseconds(300))
            guard !Task.isCancelled else { return }

            await MainActor.run { isSearching = true }

            do {
                let skills = try await registry.search(query: query)
                guard !Task.isCancelled else { return }
                await MainActor.run {
                    results = skills
                    isSearching = false
                }
            } catch {
                guard !Task.isCancelled else { return }
                await MainActor.run {
                    self.error = error.localizedDescription
                    isSearching = false
                }
            }
        }
    }

    private func selectSkill(_ skill: SkillRegistry.RegistrySkill) {
        contentTask?.cancel()
        selectedSkill = skill
        skillContent = nil
        error = nil
        installSuccess = false
        isFetchingContent = true

        contentTask = Task {
            do {
                let content = try await registry.fetchContent(skill: skill)
                guard !Task.isCancelled else { return }
                await MainActor.run {
                    guard selectedSkill?.id == skill.id else { return }
                    self.skillContent = content
                    self.isFetchingContent = false
                }
            } catch {
                guard !Task.isCancelled else { return }
                await MainActor.run {
                    guard selectedSkill?.id == skill.id else { return }
                    self.error = error.localizedDescription
                    self.isFetchingContent = false
                }
            }
        }
    }

    private func performInstall(content: String, skillName: String) {
        let agents = installedAgents.filter { selectedAgents.contains($0.id) }
        guard !agents.isEmpty else { return }

        isInstalling = true
        error = nil

        do {
            try registry.install(content: content, skillName: skillName, agents: agents)
            installSuccess = true
            isInstalling = false

            // Trigger re-scan so the new skill appears immediately
            NotificationCenter.default.post(name: .customScanPathsChanged, object: nil)

            // Auto-dismiss after brief delay
            Task {
                try? await Task.sleep(for: .milliseconds(800))
                await MainActor.run { dismiss() }
            }
        } catch {
            self.error = error.localizedDescription
            isInstalling = false
        }
    }
}
```

## File: `Chops/Views/Shared/ThinkingView.swift`
```
import SwiftUI

/// Collapsible "Thinking" section rendered outside the assistant bubble.
/// `isStreaming` is passed from the parent and should only flip false once (when the turn ends).
struct ThinkingView: View {
    let text: String
    let isStreaming: Bool

    @State private var isExpanded: Bool = false
    /// Latched true once streaming ends — shows brain icon instead of spinner.
    @State private var settled: Bool = false

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            Button {
                withAnimation(.easeInOut(duration: 0.2)) { isExpanded.toggle() }
            } label: {
                HStack(spacing: 5) {
                    Image(systemName: isExpanded ? "chevron.down" : "chevron.right")
                        .font(.caption2)
                        .foregroundStyle(.secondary)
                    if !settled {
                        ProgressView().controlSize(.mini)
                    } else {
                        Image(systemName: "brain")
                            .font(.caption2)
                            .foregroundStyle(.secondary)
                    }
                    Text("Thinking")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                    Spacer()
                }
                .contentShape(Rectangle())
            }
            .buttonStyle(.plain)
            .padding(.horizontal, 10)
            .padding(.vertical, 6)

            if isExpanded {
                ScrollView(.vertical) {
                    Text(text)
                        .font(.caption.monospaced())
                        .foregroundStyle(.secondary)
                        .opacity(0.75)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .textSelection(.enabled)
                        .padding(.horizontal, 10)
                        .padding(.bottom, 8)
                }
                .frame(maxHeight: 140)
            }
        }
        .padding(.bottom, 4)
        .onAppear {
            // Already settled when created for a completed message (isStreaming never flips).
            if !isStreaming {
                settled = true
                isExpanded = false
            }
        }
        .onChange(of: isStreaming) { _, streaming in
            if !streaming {
                settled = true
                withAnimation(.easeInOut(duration: 0.3)) { isExpanded = false }
            }
        }
    }
}
```

## File: `Chops/Views/Shared/ToolBadge.swift`
```
import SwiftUI

/// Small text badge for the metadata bar
struct ToolBadge: View {
    let tool: ToolSource

    var body: some View {
        Text(tool.shortLabel)
            .font(.system(size: 9, weight: .semibold, design: .rounded))
            .foregroundStyle(.secondary)
            .padding(.horizontal, 4)
            .padding(.vertical, 2)
            .background(.quaternary, in: RoundedRectangle(cornerRadius: 3))
    }
}

/// Icon for the sidebar — uses custom logo asset or SF Symbol fallback
struct ToolIcon: View {
    let tool: ToolSource
    var size: CGFloat = 16

    var body: some View {
        if let assetName = tool.logoAssetName {
            Image(assetName)
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: size, height: size)
        } else {
            Image(systemName: tool.iconName)
                .font(.system(size: size * 0.7))
                .frame(width: size, height: size)
        }
    }
}

extension ToolSource {
    var shortLabel: String {
        switch self {
        case .augment: "AU"
        case .claude: "CC"
        case .cursor: "CU"
        case .windsurf: "WS"
        case .codex: "CX"
        case .copilot: "CP"
        case .aider: "AI"
        case .amp: "AM"
        case .openclaw: "OC"
        case .opencode: "OP"
        case .pi: "PI"
        case .agents: "AG"
        case .antigravity: "AV"
        case .claudeDesktop: "CD"
        case .custom: "?"
        }
    }
}
```

## File: `Chops/Views/Sidebar/CollectionListView.swift`
```
import SwiftUI
import SwiftData

struct CollectionListView: View {
    @Environment(\.modelContext) private var modelContext
    @Environment(AppState.self) private var appState
    @Query(sort: \SkillCollection.sortOrder) private var collections: [SkillCollection]
    @State private var showingNewCollection = false
    @State private var newCollectionName = ""
    @State private var newCollectionIcon = "folder"
    @State private var editingCollectionID: PersistentIdentifier?
    @State private var editingName = ""
    @State private var errorMessage: String?
    @FocusState private var isRenameFocused: Bool

    private func normalizedName(_ name: String) -> String {
        name.trimmingCharacters(in: .whitespacesAndNewlines)
    }

    private func hasDuplicateName(_ name: String, excluding collectionID: PersistentIdentifier? = nil) -> Bool {
        collections.contains { collection in
            collection.persistentModelID != collectionID &&
            collection.name.localizedCaseInsensitiveCompare(name) == .orderedSame
        }
    }

    private func commitRename(_ collection: SkillCollection) {
        errorMessage = nil
        let trimmed = normalizedName(editingName)
        guard !trimmed.isEmpty else {
            editingCollectionID = nil
            return
        }
        guard trimmed != collection.name else {
            editingCollectionID = nil
            return
        }
        guard !hasDuplicateName(trimmed, excluding: collection.persistentModelID) else {
            errorMessage = "A collection with this name already exists"
            return
        }
        let oldName = collection.name
        collection.name = trimmed
        do {
            try modelContext.save()
            if appState.sidebarFilter == .collection(oldName) {
                appState.sidebarFilter = .collection(trimmed)
            }
            editingCollectionID = nil
        } catch {
            errorMessage = error.localizedDescription
        }
    }

    private func createCollection() {
        errorMessage = nil
        let trimmed = normalizedName(newCollectionName)
        guard !trimmed.isEmpty else {
            errorMessage = "Collection name can't be empty"
            return
        }
        guard !hasDuplicateName(trimmed) else {
            errorMessage = "A collection with this name already exists"
            return
        }

        let collection = SkillCollection(
            name: trimmed,
            icon: newCollectionIcon,
            sortOrder: collections.count
        )
        modelContext.insert(collection)

        do {
            try modelContext.save()
            newCollectionName = ""
            showingNewCollection = false
        } catch {
            errorMessage = error.localizedDescription
        }
    }

    private func handleDrop(_ resolvedPaths: [String], onto collection: SkillCollection) -> Bool {
        var added = false
        for path in resolvedPaths {
            let descriptor = FetchDescriptor<Skill>(
                predicate: #Predicate { $0.resolvedPath == path }
            )
            guard let skill = try? modelContext.fetch(descriptor).first else { continue }
            guard !collection.skills.contains(where: { $0.resolvedPath == path }) else { continue }
            collection.skills.append(skill)
            added = true
        }
        if added { try? modelContext.save() }
        return added
    }

    private let availableIcons = [
        "folder", "star", "bookmark", "tag", "tray",
        "archivebox", "doc.text", "gearshape", "wrench",
        "hammer", "paintbrush", "wand.and.stars", "terminal",
        "network", "globe", "bolt", "flame", "leaf"
    ]

    var body: some View {
        ForEach(collections) { collection in
            if editingCollectionID == collection.persistentModelID {
                TextField("Name", text: $editingName)
                    .textFieldStyle(.roundedBorder)
                    .focused($isRenameFocused)
                    .onAppear {
                        isRenameFocused = true
                        DispatchQueue.main.async {
                            NSApp.sendAction(#selector(NSText.selectAll(_:)), to: nil, from: nil)
                        }
                    }
                    .onSubmit {
                        commitRename(collection)
                    }
                    .onExitCommand {
                        editingCollectionID = nil
                    }
                    .tag(SidebarFilter.collection(collection.name))
            } else {
                Label(collection.name, systemImage: collection.icon)
                    .badge(collection.skills.count)
                    .tag(SidebarFilter.collection(collection.name))
                    .dropDestination(for: String.self) { resolvedPaths, _ in
                        handleDrop(resolvedPaths, onto: collection)
                    }
                    .contextMenu {
                        Button("Rename") {
                            errorMessage = nil
                            editingName = collection.name
                            editingCollectionID = collection.persistentModelID
                        }
                        Divider()
                        Button("Delete", role: .destructive) {
                            modelContext.delete(collection)
                            try? modelContext.save()
                        }
                    }
            }
        }

        Button {
            errorMessage = nil
            showingNewCollection = true
        } label: {
            Label("New Collection", systemImage: "plus.circle")
                .foregroundStyle(.secondary)
        }
        .buttonStyle(.plain)
        .popover(isPresented: $showingNewCollection) {
            VStack(spacing: 12) {
                TextField("Collection name", text: $newCollectionName)
                    .textFieldStyle(.roundedBorder)
                    .submitLabel(.done)
                    .onSubmit(createCollection)

                if let errorMessage {
                    Text(errorMessage)
                        .font(.caption)
                        .foregroundStyle(.red)
                }

                LazyVGrid(columns: Array(repeating: GridItem(.fixed(28)), count: 6), spacing: 8) {
                    ForEach(availableIcons, id: \.self) { icon in
                        Button {
                            newCollectionIcon = icon
                        } label: {
                            Image(systemName: icon)
                                .font(.body)
                                .frame(width: 28, height: 28)
                                .background(
                                    newCollectionIcon == icon ?
                                    Color.accentColor.opacity(0.2) :
                                    Color.clear,
                                    in: RoundedRectangle(cornerRadius: 4)
                                )
                        }
                        .buttonStyle(.plain)
                    }
                }

                HStack {
                    Button("Cancel") {
                        errorMessage = nil
                        showingNewCollection = false
                    }
                    Spacer()
                    Button("Create", action: createCollection)
                    .disabled(normalizedName(newCollectionName).isEmpty)
                }
            }
            .padding()
            .frame(width: 240)
        }
        .alert("Collection Error", isPresented: Binding(
            get: { errorMessage != nil && !showingNewCollection },
            set: { if !$0 { errorMessage = nil } }
        )) {
            Button("OK") {}
        } message: {
            Text(errorMessage ?? "")
        }
    }
}
```

## File: `Chops/Views/Sidebar/SidebarView.swift`
```
import SwiftUI
import SwiftData

struct SidebarView: View {
    @Environment(AppState.self) private var appState
    @Environment(\.modelContext) private var modelContext
    @Query(sort: \Skill.name) private var allSkills: [Skill]
    @Query(sort: \RemoteServer.label) private var servers: [RemoteServer]
    @State private var syncingServerIDs: Set<String> = []
    @State private var serverErrors: [String: String] = [:]
    @State private var showingErrorForServer: String?

    private var activeSources: [ToolSource] {
        ToolSource.allCases.filter { tool in
            guard tool.listable else { return false }
            return allSkills.contains { $0.toolSources.contains(tool) }
        }
    }

    private func toolCount(_ tool: ToolSource) -> Int {
        allSkills.filter { $0.toolSources.contains(tool) }.count
    }

    var body: some View {
        @Bindable var appState = appState

        List(selection: $appState.sidebarFilter) {
            Section("Library") {
                Label("Skills", systemImage: "doc.text")
                    .badge(allSkills.filter { $0.itemKind == .skill }.count)
                    .tag(SidebarFilter.allSkills)

                Label("Agents", systemImage: "person.crop.rectangle")
                    .badge(allSkills.filter { $0.itemKind == .agent }.count)
                    .tag(SidebarFilter.allAgents)

                Label("Rules", systemImage: "list.bullet.rectangle")
                    .badge(allSkills.filter { $0.itemKind == .rule }.count)
                    .tag(SidebarFilter.allRules)

                Label("Favorites", systemImage: "star")
                    .badge(allSkills.filter(\.isFavorite).count)
                    .tag(SidebarFilter.favorites)
            }

            Section("Tools") {
                ForEach(activeSources) { tool in
                    Label {
                        Text(tool.displayName)
                    } icon: {
                        ToolIcon(tool: tool)
                    }
                    .badge(toolCount(tool))
                    .tag(SidebarFilter.tool(tool))
                }
            }

            if !servers.isEmpty {
                Section("Servers") {
                    ForEach(servers) { server in
                        HStack {
                            Label {
                                Text(server.label)
                            } icon: {
                                Image(systemName: "server.rack")
                                    .foregroundStyle(.secondary)
                            }

                            Spacer()

                            if let error = serverErrors[server.id] {
                                Image(systemName: "exclamationmark.triangle.fill")
                                    .font(.caption)
                                    .foregroundStyle(.red)
                                    .popover(isPresented: Binding(
                                        get: { showingErrorForServer == server.id },
                                        set: { if !$0 { showingErrorForServer = nil } }
                                    )) {
                                        Text(error)
                                            .font(.caption)
                                            .padding()
                                            .frame(maxWidth: 250)
                                    }
                                    .onTapGesture {
                                        showingErrorForServer = server.id
                                    }
                            }

                            Button {
                                syncServer(server)
                            } label: {
                                if syncingServerIDs.contains(server.id) {
                                    ProgressView()
                                        .controlSize(.small)
                                } else {
                                    Image(systemName: "arrow.triangle.2.circlepath")
                                        .font(.caption)
                                        .foregroundStyle(.secondary)
                                }
                            }
                            .buttonStyle(.plain)
                            .help("Sync skills from server")
                            .disabled(syncingServerIDs.contains(server.id))
                        }
                        .badge(server.skills.count)
                        .tag(SidebarFilter.server(server.id))
                    }
                }
            }

            Section("Collections") {
                CollectionListView()
            }
        }
        .listStyle(.sidebar)
        .navigationTitle("Chops")
    }

    private func syncServer(_ server: RemoteServer) {
        syncingServerIDs.insert(server.id)
        serverErrors.removeValue(forKey: server.id)
        let context = modelContext
        Task {
            let scanner = SkillScanner(modelContext: context)
            await scanner.scanRemoteServer(server)
            syncingServerIDs.remove(server.id)
            if let error = server.lastSyncError {
                serverErrors[server.id] = error
            }
        }
    }
}
```

## File: `Chops/Views/Sidebar/SkillListView.swift`
```
import SwiftUI
import SwiftData

struct SkillListView: View {
    private enum ActiveAlert: Identifiable {
        case confirmDelete(Skill)
        case deleteError(String)

        var id: String {
            switch self {
            case .confirmDelete(let skill):
                return "confirm-delete-\(skill.filePath)"
            case .deleteError(let message):
                return "delete-error-\(message)"
            }
        }
    }

    @Environment(\.modelContext) private var modelContext
    @Environment(AppState.self) private var appState
    @Query(sort: \Skill.name) private var allSkills: [Skill]
    @Query(sort: \SkillCollection.name) private var allCollections: [SkillCollection]
    @State private var activeAlert: ActiveAlert?

    private var filteredSkills: [Skill] {
        var result = allSkills

        switch appState.sidebarFilter {
        case .allSkills:
            result = result.filter { $0.itemKind == .skill }
        case .allAgents:
            result = result.filter { $0.itemKind == .agent }
        case .allRules:
            result = result.filter { $0.itemKind == .rule }
        case .favorites:
            result = result.filter { $0.isFavorite }
        case .tool(let tool):
            result = result.filter { $0.toolSources.contains(tool) }
            if let kind = appState.toolKindFilter {
                result = result.filter { $0.itemKind == kind }
            }
        case .collection(let collName):
            result = result.filter { skill in
                skill.collections.contains { $0.name == collName }
            }
        case .server(let serverID):
            result = result.filter { $0.remoteServer?.id == serverID }
        }

        if !appState.searchText.isEmpty {
            result = result.filter {
                $0.name.localizedCaseInsensitiveContains(appState.searchText) ||
                $0.skillDescription.localizedCaseInsensitiveContains(appState.searchText) ||
                $0.content.localizedCaseInsensitiveContains(appState.searchText)
            }
        }

        return result
    }

    private var title: String {
        switch appState.sidebarFilter {
        case .allSkills: "Skills"
        case .allAgents: "Agents"
        case .allRules: "Rules"
        case .favorites: "Favorites"
        case .tool(let tool): tool.displayName
        case .collection(let name): name
        case .server(let id):
            allSkills.first(where: { $0.remoteServer?.id == id })?.remoteServer?.label ?? "Remote"
        }
    }

    /// Whether the current filter shows mixed item types (skills and agents together)
    private var showsTypeBadge: Bool {
        switch appState.sidebarFilter {
        case .allSkills, .allAgents, .allRules: false
        case .tool: appState.toolKindFilter == nil
        default: true
        }
    }

    private var availableKinds: [ItemKind] {
        guard case .tool(let tool) = appState.sidebarFilter else { return [] }
        let kinds = Set(allSkills.filter { $0.toolSources.contains(tool) }.map(\.itemKind))
        return ItemKind.allCases.filter { kinds.contains($0) }
    }

    @ViewBuilder
    private var emptyStateView: some View {
        if let kind = appState.toolKindFilter {
            ContentUnavailableView(
                "No \(kind.displayName)",
                systemImage: kind.icon,
                description: Text("No \(kind.displayName.lowercased()) match the current filter.")
            )
        } else {
            switch appState.sidebarFilter {
            case .allAgents:
                ContentUnavailableView("No Agents", systemImage: "person.crop.rectangle",
                    description: Text("No agents match the current filter."))
            case .allRules:
                ContentUnavailableView("No Rules", systemImage: "list.bullet.rectangle",
                    description: Text("No rules match the current filter."))
            default:
                ContentUnavailableView("No Skills", systemImage: "doc.text",
                    description: Text("No skills match the current filter."))
            }
        }
    }

    @ViewBuilder
    private func contextMenu(for skill: Skill) -> some View {
        Button(skill.isFavorite ? "Unfavorite" : "Favorite") {
            skill.isFavorite.toggle()
            try? modelContext.save()
        }
        if !allCollections.isEmpty {
            Menu("Collections") {
                ForEach(allCollections) { collection in
                    let isAssigned = skill.collections.contains(where: { $0.name == collection.name })
                    Button {
                        if isAssigned {
                            skill.collections.removeAll { $0.name == collection.name }
                        } else {
                            skill.collections.append(collection)
                        }
                        try? modelContext.save()
                    } label: {
                        Toggle(isOn: .constant(isAssigned)) {
                            Label(collection.name, systemImage: collection.icon)
                        }
                    }
                }
            }
        }
        if !skill.isRemote {
            Divider()
            Button("Show in Finder") {
                NSWorkspace.shared.selectFile(skill.filePath, inFileViewerRootedAtPath: "")
            }
        }
        if !skill.isReadOnly {
            Divider()
            Button("Delete", role: .destructive) {
                activeAlert = .confirmDelete(skill)
            }
        }
    }

    private func deleteSkill(_ skill: Skill) {
        guard !skill.isReadOnly else { return }
        do {
            try skill.deleteFromDisk()
            if appState.selectedSkill == skill {
                appState.selectedSkill = nil
            }
            modelContext.delete(skill)
            try modelContext.save()
        } catch {
            activeAlert = .deleteError(error.localizedDescription)
        }
    }

    var body: some View {
        @Bindable var appState = appState

        List(selection: $appState.selectedSkill) {
            ForEach(filteredSkills) { skill in
                SkillRow(skill: skill, showTypeBadge: showsTypeBadge)
                    .tag(skill)
                    .draggable(skill.resolvedPath)
                    .contextMenu { contextMenu(for: skill) }
            }
        }
        .navigationTitle(title)
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                HStack(spacing: 4) {
                    if case .tool = appState.sidebarFilter, availableKinds.count > 1 {
                        Menu {
                            Button {
                                appState.toolKindFilter = nil
                            } label: {
                                if appState.toolKindFilter == nil {
                                    Label("All", systemImage: "checkmark")
                                } else {
                                    Text("All")
                                }
                            }
                            Divider()
                            ForEach(availableKinds, id: \.self) { kind in
                                Button {
                                    appState.toolKindFilter = kind
                                } label: {
                                    if appState.toolKindFilter == kind {
                                        Label(kind.displayName, systemImage: "checkmark")
                                    } else {
                                        Text(kind.displayName)
                                    }
                                }
                            }
                        } label: {
                            Image(systemName: appState.toolKindFilter != nil ? "ellipsis.circle.fill" : "ellipsis.circle")
                        }
                    }
                    Menu {
                        Button {
                            appState.newItemKind = .skill
                            appState.showingNewSkillSheet = true
                        } label: {
                            Label("New Skill", systemImage: "doc.text")
                        }
                        Button {
                            appState.newItemKind = .agent
                            appState.showingNewSkillSheet = true
                        } label: {
                            Label("New Agent", systemImage: "person.crop.rectangle")
                        }
                        Button {
                            appState.newItemKind = .rule
                            appState.showingNewSkillSheet = true
                        } label: {
                            Label("New Rule", systemImage: "list.bullet.rectangle")
                        }
                        Divider()
                        Button {
                            appState.showingRegistrySheet = true
                        } label: {
                            Label("Browse Registry", systemImage: "globe")
                        }
                    } label: {
                        Image(systemName: "square.and.pencil")
                    }
                    .menuIndicator(.hidden)
                }
            }
        }
        .alert(item: $activeAlert) { alert in
            switch alert {
            case .confirmDelete(let skill):
                return Alert(
                    title: Text("Delete \(skill.displayTypeName)?"),
                    message: Text("This will permanently delete \"\(skill.name)\" from disk."),
                    primaryButton: .destructive(Text("Delete")) {
                        deleteSkill(skill)
                    },
                    secondaryButton: .cancel()
                )
            case .deleteError(let message):
                return Alert(
                    title: Text("Delete Failed"),
                    message: Text(message),
                    dismissButton: .default(Text("OK"))
                )
            }
        }
        .overlay {
            if filteredSkills.isEmpty { emptyStateView }
        }
        .onChange(of: appState.sidebarFilter) {
            if let selected = appState.selectedSkill, filteredSkills.contains(selected) {
                // Already selected something valid in this filter
            } else {
                appState.selectedSkill = filteredSkills.first
            }
        }
    }
}

struct SkillRow: View {
    let skill: Skill
    var showTypeBadge: Bool = false

    var body: some View {
        HStack(spacing: 6) {
            if showTypeBadge {
                let kindIcon: String = switch skill.itemKind {
                case .agent: "person.crop.rectangle"
                case .rule: "list.bullet.rectangle"
                case .skill: "doc.text"
                }
                Image(systemName: kindIcon)
                    .font(.caption2)
                    .foregroundStyle(.secondary)
            }

            Text(skill.name)
                .lineLimit(1)

            if skill.isFavorite {
                Image(systemName: "star.fill")
                    .font(.caption2)
                    .foregroundStyle(.yellow)
            }

            Spacer()

            if skill.isRemote, let serverLabel = skill.remoteServer?.label {
                Text(serverLabel)
                    .font(.caption)
                    .foregroundStyle(.tertiary)
                    .lineLimit(1)
            } else if let project = skill.projectName {
                Text(project)
                    .font(.caption)
                    .foregroundStyle(.tertiary)
                    .lineLimit(1)
            }

            HStack(spacing: 3) {
                ForEach(skill.toolSources, id: \.self) { tool in
                    ToolIcon(tool: tool, size: 14)
                        .help(tool.displayName)
                        .opacity(0.6)
                }
            }
        }
        .padding(.vertical, 4)
    }
}
```

## File: `Chops/Views/Sidebar/ToolFilterView.swift`
```
import SwiftUI
import SwiftData

struct ToolFilterView: View {
    @Environment(AppState.self) private var appState
    @Query(sort: \Skill.name) private var allSkills: [Skill]

    private func count(for tool: ToolSource) -> Int {
        allSkills.filter { $0.toolSources.contains(tool) }.count
    }

    private var activeSources: [ToolSource] {
        ToolSource.allCases.filter { tool in
            allSkills.contains { $0.toolSources.contains(tool) }
        }
    }

    var body: some View {
        ForEach(activeSources) { tool in
            Button {
                if appState.sidebarFilter == .tool(tool) {
                    appState.sidebarFilter = .allSkills
                } else {
                    appState.sidebarFilter = .tool(tool)
                }
            } label: {
                HStack {
                    Text(tool.displayName)
                    Spacer()
                    Text("\(count(for: tool))")
                        .foregroundStyle(.tertiary)
                        .font(.caption)
                }
            }
            .buttonStyle(.plain)
            .fontWeight(appState.sidebarFilter == .tool(tool) ? .semibold : .regular)
        }
    }
}
```

## File: `Chops.xcodeproj/project.pbxproj`
```
// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 77;
	objects = {

/* Begin PBXBuildFile section */
		038F5975DA97A3211EF4D448 /* ThinkingView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 2D07C2CD05E172DB71F63033 /* ThinkingView.swift */; };
		09D3F065191A83BDEE922789 /* SkillDetailView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 168E103488DEA623E712852B /* SkillDetailView.swift */; };
		0DC3536F86CAA3C4680958AF /* ACPModel in Frameworks */ = {isa = PBXBuildFile; productRef = 86292938A0949F325E358FA5 /* ACPModel */; };
		1BBEBC85C24BBC4E08AA1821 /* ACPLogViewer.swift in Sources */ = {isa = PBXBuildFile; fileRef = 5F236C158C893B626A51E385 /* ACPLogViewer.swift */; };
		2263A0A3B358FBA099D0086D /* SettingsView.swift in Sources */ = {isa = PBXBuildFile; fileRef = A924245DDDA4C6A59BE15567 /* SettingsView.swift */; };
		25A4FB387DB5BD96DB630C14 /* AppState.swift in Sources */ = {isa = PBXBuildFile; fileRef = 231C267216AF1BCA8628B667 /* AppState.swift */; };
		309B12E0B72A22C9772BBC99 /* ChopsApp.swift in Sources */ = {isa = PBXBuildFile; fileRef = 2787064DC7DF112E70C4E4D0 /* ChopsApp.swift */; };
		322C22C23073C29FC0C6098D /* MarkdownMessageView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 947EAED7376B7762A373EF08 /* MarkdownMessageView.swift */; };
		331F55021A7E6C9F0B666514 /* Sparkle in Frameworks */ = {isa = PBXBuildFile; productRef = 4338FC540625A275BBC9AAC9 /* Sparkle */; };
		3BF88469DCE0B56DD15DDB09 /* ACPClient.swift in Sources */ = {isa = PBXBuildFile; fileRef = 8DAD83C176F3A71A5B360BFD /* ACPClient.swift */; };
		3F0ED402E77D8D25C600BAED /* TemplateManager.swift in Sources */ = {isa = PBXBuildFile; fileRef = 12C5CD1627D4EFF58AEF4F71 /* TemplateManager.swift */; };
		480681BAD19F7CAF6AE154A2 /* RemoteServersSettingsView.swift in Sources */ = {isa = PBXBuildFile; fileRef = E684304D1723CA691F40335B /* RemoteServersSettingsView.swift */; };
		53C393C13E30EC439317509F /* ToolBadge.swift in Sources */ = {isa = PBXBuildFile; fileRef = A7B6AE242CAD6A285DD57079 /* ToolBadge.swift */; };
		590A98554CAF058BC006CC53 /* ACPAgentFactory.swift in Sources */ = {isa = PBXBuildFile; fileRef = 9BBC9E32924CF525F1C96BAE /* ACPAgentFactory.swift */; };
		5B81DED237A60776ADB04134 /* RemoteServer.swift in Sources */ = {isa = PBXBuildFile; fileRef = 3314080A44DEB895223E36D5 /* RemoteServer.swift */; };
		60A6711BAB0C3B8A3ACBF985 /* SkillParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = 5155D141EF812A3FE9ADF59C /* SkillParser.swift */; };
		62C6C8687D8A1E3C1EBBBC8C /* ClaudeACPAgent.swift in Sources */ = {isa = PBXBuildFile; fileRef = 5E201054F47FC1E66D6E0BE2 /* ClaudeACPAgent.swift */; };
		6A8E0927D95BB14C9F377F4E /* SkillScanner.swift in Sources */ = {isa = PBXBuildFile; fileRef = E6A5B26D335C1AFB6CDE8207 /* SkillScanner.swift */; };
		6E02BA7498763274DD403CD0 /* DiffReviewPanel.swift in Sources */ = {isa = PBXBuildFile; fileRef = B955C8B935BD62ED4811FCA2 /* DiffReviewPanel.swift */; };
		71E92A838AB4D1D6DC6174AF /* NewSkillSheet.swift in Sources */ = {isa = PBXBuildFile; fileRef = F02A00F80E4712872205EA7B /* NewSkillSheet.swift */; };
		72F7688C0EDA2DAF80C6512B /* ACPLogger.swift in Sources */ = {isa = PBXBuildFile; fileRef = 511C5A2149EFF77BDA7D4692 /* ACPLogger.swift */; };
		74045816B0CF10369DB51ADD /* ComposePanel.swift in Sources */ = {isa = PBXBuildFile; fileRef = 937F83BF3496CB231C535608 /* ComposePanel.swift */; };
		791AA125E9170DBA81BCBE62 /* Highlightr in Frameworks */ = {isa = PBXBuildFile; productRef = 704A14702546BFBD29BE27A8 /* Highlightr */; };
		7A17C99C5EFAE3AA9E788D50 /* Collection.swift in Sources */ = {isa = PBXBuildFile; fileRef = C9AFE1AF02B0F8057791C2A9 /* Collection.swift */; };
		7EC6156934D559226BC78859 /* CollectionListView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 4CA102A49ACFB23BC15794F8 /* CollectionListView.swift */; };
		7FD1DE6640F9339D5E97E09A /* MDCParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = 3A4F680B33C74A38FCF5ADD5 /* MDCParser.swift */; };
		801A39D725B59A2F2BAF5DF2 /* cmark in Frameworks */ = {isa = PBXBuildFile; productRef = 9F4BE66CFE1E8401894FEF1F /* cmark */; };
		846B58F3B105D1734DC6FA75 /* SkillRegistry.swift in Sources */ = {isa = PBXBuildFile; fileRef = 9FC9D3E83D8640CC258CF361 /* SkillRegistry.swift */; };
		87A469B631CC80C89B14B1C7 /* SkillMetadataBar.swift in Sources */ = {isa = PBXBuildFile; fileRef = 8C812515FD8DC222B89745F2 /* SkillMetadataBar.swift */; };
		87AEE95EAD9793D3241D4387 /* ACP in Frameworks */ = {isa = PBXBuildFile; productRef = F642568B19B420E64E62307D /* ACP */; };
		91EA572FCA75A2EA848C3429 /* ChopsTextView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 8A58EBE34E8A678FC897DFCB /* ChopsTextView.swift */; };
		95163AEB7980654C901EC693 /* Skill.swift in Sources */ = {isa = PBXBuildFile; fileRef = 27D6ED655F951177D2152351 /* Skill.swift */; };
		98434D3DDFEEC7239F6F7B79 /* RegistrySheet.swift in Sources */ = {isa = PBXBuildFile; fileRef = 7FCD6C2A8BE68F553A9CA392 /* RegistrySheet.swift */; };
		99EE8F6124FE91AC9576D6FD /* FileWatcher.swift in Sources */ = {isa = PBXBuildFile; fileRef = CAD26AA4787A2E0CDC86AADC /* FileWatcher.swift */; };
		A0862ECC573FDC0AA7CB9950 /* LibrarySettingsView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 03AA4FA049E1DADB40552060 /* LibrarySettingsView.swift */; };
		A500A6E37C3F2BF5B4428959 /* ChopsSettings.swift in Sources */ = {isa = PBXBuildFile; fileRef = 2D9B5801101BA69BB84EE28D /* ChopsSettings.swift */; };
		A99BA179E0520DCDC98E1382 /* AppLogger.swift in Sources */ = {isa = PBXBuildFile; fileRef = F45D5C8E8C732B2F4A867E43 /* AppLogger.swift */; };
		AAC4A3CBF2A9B4DF50608948 /* SSHService.swift in Sources */ = {isa = PBXBuildFile; fileRef = 6797D4AC1970DB9ACB5ACA73 /* SSHService.swift */; };
		AFDC3DAB708B352A7606F119 /* DiagnosticExporter.swift in Sources */ = {isa = PBXBuildFile; fileRef = D5D3C2567FBF8DBA4DE957B3 /* DiagnosticExporter.swift */; };
		B4526ECE136AC044CD3C7603 /* EditorTheme.swift in Sources */ = {isa = PBXBuildFile; fileRef = D24B049638C76AC6248FD5D2 /* EditorTheme.swift */; };
		B5B95B9DA63A734F25470FF5 /* SchemaVersions.swift in Sources */ = {isa = PBXBuildFile; fileRef = B1F8AA042D5D8A9F92F35CA3 /* SchemaVersions.swift */; };
		BD584933CCE2B650345C4CF1 /* ToolSource.swift in Sources */ = {isa = PBXBuildFile; fileRef = 5487D9027B97F7E9EE9A1F4A /* ToolSource.swift */; };
		BFF9964529E6C48F4F7BCB97 /* MarkdownSyntaxHighlighter.swift in Sources */ = {isa = PBXBuildFile; fileRef = 135976FA0E8358E099157DE1 /* MarkdownSyntaxHighlighter.swift */; };
		C30BEAE03E54BD36F257A925 /* ToolFilterView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 9A5774429CCE83C2AFBE046C /* ToolFilterView.swift */; };
		C6CFF37CC0B155E8846344A4 /* ChopsIcon.icon in Resources */ = {isa = PBXBuildFile; fileRef = 04C3C644B72DD508A7CBC403 /* ChopsIcon.icon */; };
		C983C685C6296C2EF73CE57D /* CursorACPAgent.swift in Sources */ = {isa = PBXBuildFile; fileRef = 07899C351E63B32277272A59 /* CursorACPAgent.swift */; };
		CBD8FECF1C5A453C8B021665 /* FrontmatterParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = 7C77C5B30E6C885B39444E5B /* FrontmatterParser.swift */; };
		CCD92CB102DFA0965D6AFDB5 /* SidebarView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 2CF7822031FD82A28978D9C5 /* SidebarView.swift */; };
		CECE9BEEC1D933C543B66A4E /* Assets.xcassets in Resources */ = {isa = PBXBuildFile; fileRef = 17F7FE50C96124BA4EE43A6F /* Assets.xcassets */; };
		D4C107BE303FC07CAF9C66AF /* ContentView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 60E0F71982C4AF0045962380 /* ContentView.swift */; };
		E15FE0630C11B3D0BC4C25ED /* ACPConfiguration.swift in Sources */ = {isa = PBXBuildFile; fileRef = D946A13468984E6DEBC20B9A /* ACPConfiguration.swift */; };
		E46A2BA5FA20531A06AFB418 /* ComposeModel.swift in Sources */ = {isa = PBXBuildFile; fileRef = 5CAA9B98C7A69F32C6950710 /* ComposeModel.swift */; };
		E6F4E1CF50F2F78F5BA9BAC9 /* SkillPreviewView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 77E332B9970E6E3D00DCFBA3 /* SkillPreviewView.swift */; };
		E7ED248D6F94C1B1DEF1E8BA /* MarkdownRenderer.swift in Sources */ = {isa = PBXBuildFile; fileRef = 372FA72F2C179B79470DF86A /* MarkdownRenderer.swift */; };
		E98F7490B18A194F82ED2C0E /* SkillListView.swift in Sources */ = {isa = PBXBuildFile; fileRef = AA64A368BBF950CD36C4F495 /* SkillListView.swift */; };
		F16A5D53C17EB72817E1282F /* WizardTemplate.swift in Sources */ = {isa = PBXBuildFile; fileRef = 181FD0056E54DEB3957FB4DC /* WizardTemplate.swift */; };
		F3F5B40B2B8F6C684313097D /* ACPRegistry in Frameworks */ = {isa = PBXBuildFile; productRef = 642A52CB994BF3466A09E6A6 /* ACPRegistry */; };
		F482F0222F6C14110B01D47F /* ACPSettingsView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 9C052B94D025127C9823E7BC /* ACPSettingsView.swift */; };
		F98B1E8579B139FD2A801650 /* SearchService.swift in Sources */ = {isa = PBXBuildFile; fileRef = 7FFC47BDE92105F4736B379F /* SearchService.swift */; };
		FB295303DD30AED03290C726 /* SkillEditorView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 31B4DB87833D5160A11E39C9 /* SkillEditorView.swift */; };
		FD8D2544AE423F4AB2843C0F /* AgentTarget.swift in Sources */ = {isa = PBXBuildFile; fileRef = 907E59B064AB8366B60BF611 /* AgentTarget.swift */; };
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		03AA4FA049E1DADB40552060 /* LibrarySettingsView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = LibrarySettingsView.swift; sourceTree = "<group>"; };
		04C3C644B72DD508A7CBC403 /* ChopsIcon.icon */ = {isa = PBXFileReference; lastKnownFileType = wrapper.icon; path = ChopsIcon.icon; sourceTree = "<group>"; };
		07899C351E63B32277272A59 /* CursorACPAgent.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CursorACPAgent.swift; sourceTree = "<group>"; };
		12C5CD1627D4EFF58AEF4F71 /* TemplateManager.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = TemplateManager.swift; sourceTree = "<group>"; };
		135976FA0E8358E099157DE1 /* MarkdownSyntaxHighlighter.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MarkdownSyntaxHighlighter.swift; sourceTree = "<group>"; };
		168E103488DEA623E712852B /* SkillDetailView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SkillDetailView.swift; sourceTree = "<group>"; };
		17F7FE50C96124BA4EE43A6F /* Assets.xcassets */ = {isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; path = Assets.xcassets; sourceTree = "<group>"; };
		181FD0056E54DEB3957FB4DC /* WizardTemplate.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = WizardTemplate.swift; sourceTree = "<group>"; };
		231C267216AF1BCA8628B667 /* AppState.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AppState.swift; sourceTree = "<group>"; };
		2787064DC7DF112E70C4E4D0 /* ChopsApp.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ChopsApp.swift; sourceTree = "<group>"; };
		27D6ED655F951177D2152351 /* Skill.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Skill.swift; sourceTree = "<group>"; };
		2CF7822031FD82A28978D9C5 /* SidebarView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SidebarView.swift; sourceTree = "<group>"; };
		2D07C2CD05E172DB71F63033 /* ThinkingView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ThinkingView.swift; sourceTree = "<group>"; };
		2D9B5801101BA69BB84EE28D /* ChopsSettings.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ChopsSettings.swift; sourceTree = "<group>"; };
		31B4DB87833D5160A11E39C9 /* SkillEditorView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SkillEditorView.swift; sourceTree = "<group>"; };
		3314080A44DEB895223E36D5 /* RemoteServer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RemoteServer.swift; sourceTree = "<group>"; };
		372FA72F2C179B79470DF86A /* MarkdownRenderer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MarkdownRenderer.swift; sourceTree = "<group>"; };
		3A4F680B33C74A38FCF5ADD5 /* MDCParser.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MDCParser.swift; sourceTree = "<group>"; };
		4CA102A49ACFB23BC15794F8 /* CollectionListView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CollectionListView.swift; sourceTree = "<group>"; };
		511C5A2149EFF77BDA7D4692 /* ACPLogger.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ACPLogger.swift; sourceTree = "<group>"; };
		5155D141EF812A3FE9ADF59C /* SkillParser.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SkillParser.swift; sourceTree = "<group>"; };
		5487D9027B97F7E9EE9A1F4A /* ToolSource.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ToolSource.swift; sourceTree = "<group>"; };
		5CAA9B98C7A69F32C6950710 /* ComposeModel.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ComposeModel.swift; sourceTree = "<group>"; };
		5E201054F47FC1E66D6E0BE2 /* ClaudeACPAgent.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ClaudeACPAgent.swift; sourceTree = "<group>"; };
		5F236C158C893B626A51E385 /* ACPLogViewer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ACPLogViewer.swift; sourceTree = "<group>"; };
		60E0F71982C4AF0045962380 /* ContentView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ContentView.swift; sourceTree = "<group>"; };
		6797D4AC1970DB9ACB5ACA73 /* SSHService.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SSHService.swift; sourceTree = "<group>"; };
		77E332B9970E6E3D00DCFBA3 /* SkillPreviewView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SkillPreviewView.swift; sourceTree = "<group>"; };
		7C77C5B30E6C885B39444E5B /* FrontmatterParser.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = FrontmatterParser.swift; sourceTree = "<group>"; };
		7FCD6C2A8BE68F553A9CA392 /* RegistrySheet.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RegistrySheet.swift; sourceTree = "<group>"; };
		7FFC47BDE92105F4736B379F /* SearchService.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SearchService.swift; sourceTree = "<group>"; };
		8A58EBE34E8A678FC897DFCB /* ChopsTextView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ChopsTextView.swift; sourceTree = "<group>"; };
		8C812515FD8DC222B89745F2 /* SkillMetadataBar.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SkillMetadataBar.swift; sourceTree = "<group>"; };
		8DAD83C176F3A71A5B360BFD /* ACPClient.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ACPClient.swift; sourceTree = "<group>"; };
		907E59B064AB8366B60BF611 /* AgentTarget.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AgentTarget.swift; sourceTree = "<group>"; };
		937F83BF3496CB231C535608 /* ComposePanel.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ComposePanel.swift; sourceTree = "<group>"; };
		947EAED7376B7762A373EF08 /* MarkdownMessageView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MarkdownMessageView.swift; sourceTree = "<group>"; };
		9A5774429CCE83C2AFBE046C /* ToolFilterView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ToolFilterView.swift; sourceTree = "<group>"; };
		9BBC9E32924CF525F1C96BAE /* ACPAgentFactory.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ACPAgentFactory.swift; sourceTree = "<group>"; };
		9C052B94D025127C9823E7BC /* ACPSettingsView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ACPSettingsView.swift; sourceTree = "<group>"; };
		9FC9D3E83D8640CC258CF361 /* SkillRegistry.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SkillRegistry.swift; sourceTree = "<group>"; };
		A7B6AE242CAD6A285DD57079 /* ToolBadge.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ToolBadge.swift; sourceTree = "<group>"; };
		A924245DDDA4C6A59BE15567 /* SettingsView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SettingsView.swift; sourceTree = "<group>"; };
		AA64A368BBF950CD36C4F495 /* SkillListView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SkillListView.swift; sourceTree = "<group>"; };
		B1F8AA042D5D8A9F92F35CA3 /* SchemaVersions.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SchemaVersions.swift; sourceTree = "<group>"; };
		B3F5CF5BB1FC8455FDDB004A /* Chops.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = Chops.app; sourceTree = BUILT_PRODUCTS_DIR; };
		B955C8B935BD62ED4811FCA2 /* DiffReviewPanel.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = DiffReviewPanel.swift; sourceTree = "<group>"; };
		C9AFE1AF02B0F8057791C2A9 /* Collection.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Collection.swift; sourceTree = "<group>"; };
		CAD26AA4787A2E0CDC86AADC /* FileWatcher.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = FileWatcher.swift; sourceTree = "<group>"; };
		D24B049638C76AC6248FD5D2 /* EditorTheme.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = EditorTheme.swift; sourceTree = "<group>"; };
		D5D3C2567FBF8DBA4DE957B3 /* DiagnosticExporter.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = DiagnosticExporter.swift; sourceTree = "<group>"; };
		D946A13468984E6DEBC20B9A /* ACPConfiguration.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ACPConfiguration.swift; sourceTree = "<group>"; };
		E684304D1723CA691F40335B /* RemoteServersSettingsView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RemoteServersSettingsView.swift; sourceTree = "<group>"; };
		E6A5B26D335C1AFB6CDE8207 /* SkillScanner.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SkillScanner.swift; sourceTree = "<group>"; };
		F02A00F80E4712872205EA7B /* NewSkillSheet.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = NewSkillSheet.swift; sourceTree = "<group>"; };
		F45D5C8E8C732B2F4A867E43 /* AppLogger.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AppLogger.swift; sourceTree = "<group>"; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		58F62ED0A413A9C746F9D783 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
				331F55021A7E6C9F0B666514 /* Sparkle in Frameworks */,
				791AA125E9170DBA81BCBE62 /* Highlightr in Frameworks */,
				801A39D725B59A2F2BAF5DF2 /* cmark in Frameworks */,
				87AEE95EAD9793D3241D4387 /* ACP in Frameworks */,
				0DC3536F86CAA3C4680958AF /* ACPModel in Frameworks */,
				F3F5B40B2B8F6C684313097D /* ACPRegistry in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		05CBDCA0595CF021CC38C7E4 /* Utilities */ = {
			isa = PBXGroup;
			children = (
				7C77C5B30E6C885B39444E5B /* FrontmatterParser.swift */,
				372FA72F2C179B79470DF86A /* MarkdownRenderer.swift */,
				3A4F680B33C74A38FCF5ADD5 /* MDCParser.swift */,
			);
			path = Utilities;
			sourceTree = "<group>";
		};
		08ECEAD013847D8F110E61B4 = {
			isa = PBXGroup;
			children = (
				198DFCB0614727F57F6D073D /* Chops */,
				D3558033A0A7B4EE7E7234CE /* Products */,
			);
			sourceTree = "<group>";
		};
		198DFCB0614727F57F6D073D /* Chops */ = {
			isa = PBXGroup;
			children = (
				04C3C644B72DD508A7CBC403 /* ChopsIcon.icon */,
				55B50A6F7E2143E2A7160C6D /* App */,
				75334DE5CD1545A8E1E63699 /* Models */,
				D17AEFDEFE1C95D34F0F5771 /* Resources */,
				665294B304954CDCE458E2FA /* Services */,
				05CBDCA0595CF021CC38C7E4 /* Utilities */,
				414F6727A94989246C3B7B36 /* Views */,
			);
			path = Chops;
			sourceTree = "<group>";
		};
		1B016A7C37052B1801FCFD6A /* Shared */ = {
			isa = PBXGroup;
			children = (
				5F236C158C893B626A51E385 /* ACPLogViewer.swift */,
				5CAA9B98C7A69F32C6950710 /* ComposeModel.swift */,
				937F83BF3496CB231C535608 /* ComposePanel.swift */,
				B955C8B935BD62ED4811FCA2 /* DiffReviewPanel.swift */,
				947EAED7376B7762A373EF08 /* MarkdownMessageView.swift */,
				F02A00F80E4712872205EA7B /* NewSkillSheet.swift */,
				7FCD6C2A8BE68F553A9CA392 /* RegistrySheet.swift */,
				2D07C2CD05E172DB71F63033 /* ThinkingView.swift */,
				A7B6AE242CAD6A285DD57079 /* ToolBadge.swift */,
			);
			path = Shared;
			sourceTree = "<group>";
		};
		3B8985D8816557B264BF0AD8 /* ACP */ = {
			isa = PBXGroup;
			children = (
				9BBC9E32924CF525F1C96BAE /* ACPAgentFactory.swift */,
				8DAD83C176F3A71A5B360BFD /* ACPClient.swift */,
				511C5A2149EFF77BDA7D4692 /* ACPLogger.swift */,
				89F9D9F176DFDB3FDF02DEFC /* Agents */,
			);
			path = ACP;
			sourceTree = "<group>";
		};
		40FF74A5B2D0A1E16B14B7A4 /* Settings */ = {
			isa = PBXGroup;
			children = (
				9C052B94D025127C9823E7BC /* ACPSettingsView.swift */,
				D5D3C2567FBF8DBA4DE957B3 /* DiagnosticExporter.swift */,
				03AA4FA049E1DADB40552060 /* LibrarySettingsView.swift */,
				E684304D1723CA691F40335B /* RemoteServersSettingsView.swift */,
				A924245DDDA4C6A59BE15567 /* SettingsView.swift */,
			);
			path = Settings;
			sourceTree = "<group>";
		};
		414F6727A94989246C3B7B36 /* Views */ = {
			isa = PBXGroup;
			children = (
				96A2A820C082754BBFB0237D /* Detail */,
				40FF74A5B2D0A1E16B14B7A4 /* Settings */,
				1B016A7C37052B1801FCFD6A /* Shared */,
				95530102A99D9A389717E414 /* Sidebar */,
			);
			path = Views;
			sourceTree = "<group>";
		};
		55B50A6F7E2143E2A7160C6D /* App */ = {
			isa = PBXGroup;
			children = (
				231C267216AF1BCA8628B667 /* AppState.swift */,
				2787064DC7DF112E70C4E4D0 /* ChopsApp.swift */,
				60E0F71982C4AF0045962380 /* ContentView.swift */,
			);
			path = App;
			sourceTree = "<group>";
		};
		665294B304954CDCE458E2FA /* Services */ = {
			isa = PBXGroup;
			children = (
				F45D5C8E8C732B2F4A867E43 /* AppLogger.swift */,
				CAD26AA4787A2E0CDC86AADC /* FileWatcher.swift */,
				7FFC47BDE92105F4736B379F /* SearchService.swift */,
				5155D141EF812A3FE9ADF59C /* SkillParser.swift */,
				9FC9D3E83D8640CC258CF361 /* SkillRegistry.swift */,
				E6A5B26D335C1AFB6CDE8207 /* SkillScanner.swift */,
				6797D4AC1970DB9ACB5ACA73 /* SSHService.swift */,
				12C5CD1627D4EFF58AEF4F71 /* TemplateManager.swift */,
				3B8985D8816557B264BF0AD8 /* ACP */,
			);
			path = Services;
			sourceTree = "<group>";
		};
		75334DE5CD1545A8E1E63699 /* Models */ = {
			isa = PBXGroup;
			children = (
				D946A13468984E6DEBC20B9A /* ACPConfiguration.swift */,
				907E59B064AB8366B60BF611 /* AgentTarget.swift */,
				2D9B5801101BA69BB84EE28D /* ChopsSettings.swift */,
				C9AFE1AF02B0F8057791C2A9 /* Collection.swift */,
				3314080A44DEB895223E36D5 /* RemoteServer.swift */,
				B1F8AA042D5D8A9F92F35CA3 /* SchemaVersions.swift */,
				27D6ED655F951177D2152351 /* Skill.swift */,
				5487D9027B97F7E9EE9A1F4A /* ToolSource.swift */,
				181FD0056E54DEB3957FB4DC /* WizardTemplate.swift */,
			);
			path = Models;
			sourceTree = "<group>";
		};
		89F9D9F176DFDB3FDF02DEFC /* Agents */ = {
			isa = PBXGroup;
			children = (
				5E201054F47FC1E66D6E0BE2 /* ClaudeACPAgent.swift */,
				07899C351E63B32277272A59 /* CursorACPAgent.swift */,
			);
			path = Agents;
			sourceTree = "<group>";
		};
		95530102A99D9A389717E414 /* Sidebar */ = {
			isa = PBXGroup;
			children = (
				4CA102A49ACFB23BC15794F8 /* CollectionListView.swift */,
				2CF7822031FD82A28978D9C5 /* SidebarView.swift */,
				AA64A368BBF950CD36C4F495 /* SkillListView.swift */,
				9A5774429CCE83C2AFBE046C /* ToolFilterView.swift */,
			);
			path = Sidebar;
			sourceTree = "<group>";
		};
		96A2A820C082754BBFB0237D /* Detail */ = {
			isa = PBXGroup;
			children = (
				8A58EBE34E8A678FC897DFCB /* ChopsTextView.swift */,
				D24B049638C76AC6248FD5D2 /* EditorTheme.swift */,
				135976FA0E8358E099157DE1 /* MarkdownSyntaxHighlighter.swift */,
				168E103488DEA623E712852B /* SkillDetailView.swift */,
				31B4DB87833D5160A11E39C9 /* SkillEditorView.swift */,
				8C812515FD8DC222B89745F2 /* SkillMetadataBar.swift */,
				77E332B9970E6E3D00DCFBA3 /* SkillPreviewView.swift */,
			);
			path = Detail;
			sourceTree = "<group>";
		};
		D17AEFDEFE1C95D34F0F5771 /* Resources */ = {
			isa = PBXGroup;
			children = (
				17F7FE50C96124BA4EE43A6F /* Assets.xcassets */,
			);
			path = Resources;
			sourceTree = "<group>";
		};
		D3558033A0A7B4EE7E7234CE /* Products */ = {
			isa = PBXGroup;
			children = (
				B3F5CF5BB1FC8455FDDB004A /* Chops.app */,
			);
			name = Products;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		9188DE9415462C6D3B3FA067 /* Chops */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 19BD727EBF8BFE5016E97A7A /* Build configuration list for PBXNativeTarget "Chops" */;
			buildPhases = (
				1D538A007981736680A1AD9B /* Sources */,
				C796CFFF04920C825B5A52FA /* Resources */,
				58F62ED0A413A9C746F9D783 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = Chops;
			packageProductDependencies = (
				4338FC540625A275BBC9AAC9 /* Sparkle */,
				704A14702546BFBD29BE27A8 /* Highlightr */,
				9F4BE66CFE1E8401894FEF1F /* cmark */,
				F642568B19B420E64E62307D /* ACP */,
				86292938A0949F325E358FA5 /* ACPModel */,
				642A52CB994BF3466A09E6A6 /* ACPRegistry */,
			);
			productName = Chops;
			productReference = B3F5CF5BB1FC8455FDDB004A /* Chops.app */;
			productType = "com.apple.product-type.application";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		0BF6016099FDE9BFD3432654 /* Project object */ = {
			isa = PBXProject;
			attributes = {
				BuildIndependentTargetsInParallel = YES;
				LastUpgradeCheck = 1430;
				TargetAttributes = {
				};
			};
			buildConfigurationList = 719777DE0F769FDB488A0FDB /* Build configuration list for PBXProject "Chops" */;
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				Base,
				en,
			);
			mainGroup = 08ECEAD013847D8F110E61B4;
			minimizedProjectReferenceProxies = 1;
			packageReferences = (
				EFEB40047FCA0FF6CF09B7EC /* XCRemoteSwiftPackageReference "swift-acp" */,
				7FA62842E4E9A8FD27AE24AF /* XCRemoteSwiftPackageReference "Highlightr" */,
				FD1D69AB767CC40E2CE9FED9 /* XCRemoteSwiftPackageReference "Sparkle" */,
				05A6F59368DE6489DCD607F1 /* XCRemoteSwiftPackageReference "cmark-gfm" */,
			);
			preferredProjectObjectVersion = 77;
			productRefGroup = D3558033A0A7B4EE7E7234CE /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				9188DE9415462C6D3B3FA067 /* Chops */,
			);
		};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		C796CFFF04920C825B5A52FA /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				CECE9BEEC1D933C543B66A4E /* Assets.xcassets in Resources */,
				C6CFF37CC0B155E8846344A4 /* ChopsIcon.icon in Resources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		1D538A007981736680A1AD9B /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				590A98554CAF058BC006CC53 /* ACPAgentFactory.swift in Sources */,
				3BF88469DCE0B56DD15DDB09 /* ACPClient.swift in Sources */,
				E15FE0630C11B3D0BC4C25ED /* ACPConfiguration.swift in Sources */,
				1BBEBC85C24BBC4E08AA1821 /* ACPLogViewer.swift in Sources */,
				72F7688C0EDA2DAF80C6512B /* ACPLogger.swift in Sources */,
				F482F0222F6C14110B01D47F /* ACPSettingsView.swift in Sources */,
				FD8D2544AE423F4AB2843C0F /* AgentTarget.swift in Sources */,
				A99BA179E0520DCDC98E1382 /* AppLogger.swift in Sources */,
				25A4FB387DB5BD96DB630C14 /* AppState.swift in Sources */,
				309B12E0B72A22C9772BBC99 /* ChopsApp.swift in Sources */,
				A500A6E37C3F2BF5B4428959 /* ChopsSettings.swift in Sources */,
				91EA572FCA75A2EA848C3429 /* ChopsTextView.swift in Sources */,
				62C6C8687D8A1E3C1EBBBC8C /* ClaudeACPAgent.swift in Sources */,
				7A17C99C5EFAE3AA9E788D50 /* Collection.swift in Sources */,
				7EC6156934D559226BC78859 /* CollectionListView.swift in Sources */,
				E46A2BA5FA20531A06AFB418 /* ComposeModel.swift in Sources */,
				74045816B0CF10369DB51ADD /* ComposePanel.swift in Sources */,
				D4C107BE303FC07CAF9C66AF /* ContentView.swift in Sources */,
				C983C685C6296C2EF73CE57D /* CursorACPAgent.swift in Sources */,
				AFDC3DAB708B352A7606F119 /* DiagnosticExporter.swift in Sources */,
				6E02BA7498763274DD403CD0 /* DiffReviewPanel.swift in Sources */,
				B4526ECE136AC044CD3C7603 /* EditorTheme.swift in Sources */,
				99EE8F6124FE91AC9576D6FD /* FileWatcher.swift in Sources */,
				CBD8FECF1C5A453C8B021665 /* FrontmatterParser.swift in Sources */,
				A0862ECC573FDC0AA7CB9950 /* LibrarySettingsView.swift in Sources */,
				7FD1DE6640F9339D5E97E09A /* MDCParser.swift in Sources */,
				322C22C23073C29FC0C6098D /* MarkdownMessageView.swift in Sources */,
				E7ED248D6F94C1B1DEF1E8BA /* MarkdownRenderer.swift in Sources */,
				BFF9964529E6C48F4F7BCB97 /* MarkdownSyntaxHighlighter.swift in Sources */,
				71E92A838AB4D1D6DC6174AF /* NewSkillSheet.swift in Sources */,
				98434D3DDFEEC7239F6F7B79 /* RegistrySheet.swift in Sources */,
				5B81DED237A60776ADB04134 /* RemoteServer.swift in Sources */,
				480681BAD19F7CAF6AE154A2 /* RemoteServersSettingsView.swift in Sources */,
				AAC4A3CBF2A9B4DF50608948 /* SSHService.swift in Sources */,
				B5B95B9DA63A734F25470FF5 /* SchemaVersions.swift in Sources */,
				F98B1E8579B139FD2A801650 /* SearchService.swift in Sources */,
				2263A0A3B358FBA099D0086D /* SettingsView.swift in Sources */,
				CCD92CB102DFA0965D6AFDB5 /* SidebarView.swift in Sources */,
				95163AEB7980654C901EC693 /* Skill.swift in Sources */,
				09D3F065191A83BDEE922789 /* SkillDetailView.swift in Sources */,
				FB295303DD30AED03290C726 /* SkillEditorView.swift in Sources */,
				E98F7490B18A194F82ED2C0E /* SkillListView.swift in Sources */,
				87A469B631CC80C89B14B1C7 /* SkillMetadataBar.swift in Sources */,
				60A6711BAB0C3B8A3ACBF985 /* SkillParser.swift in Sources */,
				E6F4E1CF50F2F78F5BA9BAC9 /* SkillPreviewView.swift in Sources */,
				846B58F3B105D1734DC6FA75 /* SkillRegistry.swift in Sources */,
				6A8E0927D95BB14C9F377F4E /* SkillScanner.swift in Sources */,
				3F0ED402E77D8D25C600BAED /* TemplateManager.swift in Sources */,
				038F5975DA97A3211EF4D448 /* ThinkingView.swift in Sources */,
				53C393C13E30EC439317509F /* ToolBadge.swift in Sources */,
				C30BEAE03E54BD36F257A925 /* ToolFilterView.swift in Sources */,
				BD584933CCE2B650345C4CF1 /* ToolSource.swift in Sources */,
				F16A5D53C17EB72817E1282F /* WizardTemplate.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		31FDAD4740108C316B09117A /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++14";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				MACOSX_DEPLOYMENT_TARGET = 15.0;
				MTL_ENABLE_DEBUG_INFO = NO;
				MTL_FAST_MATH = YES;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = macosx;
				SWIFT_COMPILATION_MODE = wholemodule;
				SWIFT_OPTIMIZATION_LEVEL = "-O";
				SWIFT_VERSION = 5.0;
			};
			name = Release;
		};
		48F3C139C64DA85863FE9C21 /* LocalRelease */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = ChopsIcon;
				CODE_SIGN_ENTITLEMENTS = Chops/ChopsLocalRelease.entitlements;
				COMBINE_HIDPI_IMAGES = YES;
				CURRENT_PROJECT_VERSION = 1;
				ENABLE_HARDENED_RUNTIME = YES;
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = Chops/Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/../Frameworks",
				);
				MACOSX_DEPLOYMENT_TARGET = 15.0;
				MARKETING_VERSION = 1.0.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.joshpigford.Chops;
				SDKROOT = macosx;
				SWIFT_STRICT_CONCURRENCY = minimal;
			};
			name = LocalRelease;
		};
		52738EE717474F8671BFB266 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = ChopsIcon;
				CODE_SIGN_ENTITLEMENTS = Chops/Chops.entitlements;
				COMBINE_HIDPI_IMAGES = YES;
				CURRENT_PROJECT_VERSION = 1;
				ENABLE_HARDENED_RUNTIME = YES;
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = Chops/Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/../Frameworks",
				);
				MACOSX_DEPLOYMENT_TARGET = 15.0;
				MARKETING_VERSION = 1.0.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.joshpigford.Chops;
				SDKROOT = macosx;
				SWIFT_STRICT_CONCURRENCY = minimal;
			};
			name = Debug;
		};
		58C6E63A67ADDC4C7CB7ED9D /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = ChopsIcon;
				CODE_SIGN_ENTITLEMENTS = Chops/Chops.entitlements;
				CODE_SIGN_IDENTITY = "Developer ID Application";
				COMBINE_HIDPI_IMAGES = YES;
				CURRENT_PROJECT_VERSION = 1;
				ENABLE_HARDENED_RUNTIME = YES;
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = Chops/Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/../Frameworks",
				);
				MACOSX_DEPLOYMENT_TARGET = 15.0;
				MARKETING_VERSION = 1.0.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.joshpigford.Chops;
				SDKROOT = macosx;
				SWIFT_STRICT_CONCURRENCY = minimal;
			};
			name = Release;
		};
		67CFFB04E52F4383BF75357C /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++14";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"$(inherited)",
					"DEBUG=1",
				);
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				MACOSX_DEPLOYMENT_TARGET = 15.0;
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				MTL_FAST_MATH = YES;
				ONLY_ACTIVE_ARCH = YES;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = macosx;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
				SWIFT_VERSION = 5.0;
			};
			name = Debug;
		};
		9095D323E2CCDA0C5D19CDAE /* LocalRelease */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++14";
				CLANG_CXX_LIBRARY = "libc++";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				MACOSX_DEPLOYMENT_TARGET = 15.0;
				MTL_ENABLE_DEBUG_INFO = NO;
				MTL_FAST_MATH = YES;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = macosx;
				SWIFT_COMPILATION_MODE = wholemodule;
				SWIFT_OPTIMIZATION_LEVEL = "-O";
				SWIFT_VERSION = 5.0;
			};
			name = LocalRelease;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		19BD727EBF8BFE5016E97A7A /* Build configuration list for PBXNativeTarget "Chops" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				52738EE717474F8671BFB266 /* Debug */,
				48F3C139C64DA85863FE9C21 /* LocalRelease */,
				58C6E63A67ADDC4C7CB7ED9D /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		719777DE0F769FDB488A0FDB /* Build configuration list for PBXProject "Chops" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				67CFFB04E52F4383BF75357C /* Debug */,
				9095D323E2CCDA0C5D19CDAE /* LocalRelease */,
				31FDAD4740108C316B09117A /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
/* End XCConfigurationList section */

/* Begin XCRemoteSwiftPackageReference section */
		05A6F59368DE6489DCD607F1 /* XCRemoteSwiftPackageReference "cmark-gfm" */ = {
			isa = XCRemoteSwiftPackageReference;
			repositoryURL = "https://github.com/brokenhandsio/cmark-gfm.git";
			requirement = {
				kind = upToNextMajorVersion;
				minimumVersion = 2.1.0;
			};
		};
		7FA62842E4E9A8FD27AE24AF /* XCRemoteSwiftPackageReference "Highlightr" */ = {
			isa = XCRemoteSwiftPackageReference;
			repositoryURL = "https://github.com/raspu/Highlightr";
			requirement = {
				kind = upToNextMajorVersion;
				minimumVersion = 2.2.1;
			};
		};
		EFEB40047FCA0FF6CF09B7EC /* XCRemoteSwiftPackageReference "swift-acp" */ = {
			isa = XCRemoteSwiftPackageReference;
			repositoryURL = "https://github.com/wiedymi/swift-acp";
			requirement = {
				branch = main;
				kind = branch;
			};
		};
		FD1D69AB767CC40E2CE9FED9 /* XCRemoteSwiftPackageReference "Sparkle" */ = {
			isa = XCRemoteSwiftPackageReference;
			repositoryURL = "https://github.com/sparkle-project/Sparkle";
			requirement = {
				kind = upToNextMajorVersion;
				minimumVersion = 2.6.0;
			};
		};
/* End XCRemoteSwiftPackageReference section */

/* Begin XCSwiftPackageProductDependency section */
		4338FC540625A275BBC9AAC9 /* Sparkle */ = {
			isa = XCSwiftPackageProductDependency;
			package = FD1D69AB767CC40E2CE9FED9 /* XCRemoteSwiftPackageReference "Sparkle" */;
			productName = Sparkle;
		};
		642A52CB994BF3466A09E6A6 /* ACPRegistry */ = {
			isa = XCSwiftPackageProductDependency;
			package = EFEB40047FCA0FF6CF09B7EC /* XCRemoteSwiftPackageReference "swift-acp" */;
			productName = ACPRegistry;
		};
		704A14702546BFBD29BE27A8 /* Highlightr */ = {
			isa = XCSwiftPackageProductDependency;
			package = 7FA62842E4E9A8FD27AE24AF /* XCRemoteSwiftPackageReference "Highlightr" */;
			productName = Highlightr;
		};
		86292938A0949F325E358FA5 /* ACPModel */ = {
			isa = XCSwiftPackageProductDependency;
			package = EFEB40047FCA0FF6CF09B7EC /* XCRemoteSwiftPackageReference "swift-acp" */;
			productName = ACPModel;
		};
		9F4BE66CFE1E8401894FEF1F /* cmark */ = {
			isa = XCSwiftPackageProductDependency;
			package = 05A6F59368DE6489DCD607F1 /* XCRemoteSwiftPackageReference "cmark-gfm" */;
			productName = cmark;
		};
		F642568B19B420E64E62307D /* ACP */ = {
			isa = XCSwiftPackageProductDependency;
			package = EFEB40047FCA0FF6CF09B7EC /* XCRemoteSwiftPackageReference "swift-acp" */;
			productName = ACP;
		};
/* End XCSwiftPackageProductDependency section */
	};
	rootObject = 0BF6016099FDE9BFD3432654 /* Project object */;
}
```

## File: `Chops.xcodeproj/project.xcworkspace/contents.xcworkspacedata`
```
<?xml version="1.0" encoding="UTF-8"?>
<Workspace
   version = "1.0">
   <FileRef
      location = "self:">
   </FileRef>
</Workspace>
```

## File: `Chops.xcodeproj/project.xcworkspace/xcshareddata/swiftpm/Package.resolved`
```
{
  "originHash" : "e0ac615d8e4bebcfc18f6c3a73bc868431f4021df8a008148a52f6b4be44d7d4",
  "pins" : [
    {
      "identity" : "cmark-gfm",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/brokenhandsio/cmark-gfm.git",
      "state" : {
        "revision" : "e97450a77a40f12b4f88f95891621c3b5d8669de",
        "version" : "2.1.0"
      }
    },
    {
      "identity" : "highlightr",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/raspu/Highlightr",
      "state" : {
        "revision" : "05e7fcc63b33925cd0c1faaa205cdd5681e7bbef",
        "version" : "2.3.0"
      }
    },
    {
      "identity" : "sparkle",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/sparkle-project/Sparkle",
      "state" : {
        "revision" : "21d8df80440b1ca3b65fa82e40782f1e5a9e6ba2",
        "version" : "2.9.0"
      }
    },
    {
      "identity" : "swift-acp",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/wiedymi/swift-acp",
      "state" : {
        "branch" : "main",
        "revision" : "c22dc706b8b985f7d140f245ba5de36a7a2a7493"
      }
    }
  ],
  "version" : 3
}
```

## File: `scripts/release.sh`
```bash
#!/bin/bash
set -euo pipefail

# Usage: ./scripts/release.sh 1.0.0
#
# Reads credentials from .env in the project root.
# See .env.example for required variables.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
if [ -f "$SCRIPT_DIR/../.env" ]; then
  set -a
  source "$SCRIPT_DIR/../.env"
  set +a
fi

VERSION="${1:?Usage: ./scripts/release.sh <version>}"

# Extract changelog entries for a version and convert to HTML <ul>
extract_changelog() {
  local version="$1"
  local changelog="$2"
  local in_section=false
  local html="<ul>"

  while IFS= read -r line; do
    if [[ "$line" =~ ^##\ \[${version}\] ]]; then
      in_section=true
      continue
    fi
    if $in_section && [[ "$line" =~ ^##\  ]]; then
      break
    fi
    if $in_section && [[ "$line" =~ ^-\ (.+) ]]; then
      html+="<li>${BASH_REMATCH[1]}</li>"
    fi
  done < "$changelog"

  html+="</ul>"
  if [ "$html" = "<ul></ul>" ]; then
    echo ""
  else
    echo "$html"
  fi
}

# Extract raw markdown changelog entries for a version
extract_changelog_markdown() {
  local version="$1"
  local changelog="$2"
  local in_section=false
  local md=""

  while IFS= read -r line; do
    if [[ "$line" =~ ^##\ \[${version}\] ]]; then
      in_section=true
      continue
    fi
    if $in_section && [[ "$line" =~ ^##\  ]]; then
      break
    fi
    if $in_section && [[ "$line" =~ ^-\ (.+) ]]; then
      md+="- ${BASH_REMATCH[1]}"$'\n'
    fi
  done < "$changelog"

  echo "$md"
}

TEAM_ID="${APPLE_TEAM_ID:?Set APPLE_TEAM_ID}"
SIGNING_IDENTITY="Developer ID Application: ${SIGNING_IDENTITY_NAME:?Set SIGNING_IDENTITY_NAME} ($TEAM_ID)"
APPLE_ID="${APPLE_ID:?Set APPLE_ID}"
BUNDLE_ID="com.joshpigford.Chops"

if ! xcrun notarytool history --keychain-profile "AC_PASSWORD" >/dev/null 2>&1; then
  echo "❌ Unable to use notarytool keychain profile \"AC_PASSWORD\"."
  echo "Create or refresh it with:"
  echo "  xcrun notarytool store-credentials \"AC_PASSWORD\" --apple-id \"$APPLE_ID\" --team-id \"$TEAM_ID\" --password \"<app-specific-password>\""
  exit 1
fi

create_chops_dmg() {
  hdiutil detach "/Volumes/Chops" 2>/dev/null || true
  rm -f build/Chops.dmg build/Chops_rw.dmg

  # Create writable DMG from the app
  hdiutil create -volname "Chops" -srcfolder build/export/Chops.app -fs HFS+ -format UDRW build/Chops_rw.dmg

  # Mount, add Applications symlink and background, apply Finder styling
  hdiutil attach build/Chops_rw.dmg
  ln -s /Applications "/Volumes/Chops/Applications"
  mkdir -p "/Volumes/Chops/.background"
  cp scripts/dmg-background.png "/Volumes/Chops/.background/background.png"

  osascript <<'APPLESCRIPT'
tell application "Finder"
  tell disk "Chops"
    open
    tell container window
      set current view to icon view
      set toolbar visible to false
      set statusbar visible to false
      set the bounds to {200, 120, 990, 600}
    end tell
    set opts to the icon view options of container window
    tell opts
      set icon size to 128
      set text size to 13
      set arrangement to not arranged
      set background picture to POSIX file "/Volumes/Chops/.background/background.png"
    end tell
    set position of item "Chops.app" to {195, 220}
    set position of item "Applications" to {595, 220}
    set the extension hidden of item "Chops.app" to true
    close
    open
    delay 1
    tell container window
      set the bounds to {200, 120, 980, 590}
    end tell
    delay 1
    tell container window
      set the bounds to {200, 120, 990, 600}
    end tell
    delay 3
  end tell
end tell
APPLESCRIPT

  hdiutil detach "/Volumes/Chops"
  hdiutil convert build/Chops_rw.dmg -format UDZO -o build/Chops.dmg
  rm -f build/Chops_rw.dmg
}

echo "🔨 Building Chops v$VERSION..."

# Generate Xcode project
xcodegen generate

# Clean build
rm -rf build
mkdir -p build

# Archive
xcodebuild -project Chops.xcodeproj \
  -scheme Chops \
  -configuration Release \
  -archivePath build/Chops.xcarchive \
  archive \
  DEVELOPMENT_TEAM="$TEAM_ID" \
  MARKETING_VERSION="$VERSION" \
  CURRENT_PROJECT_VERSION="$VERSION"

# Export
sed "s/\${APPLE_TEAM_ID}/$TEAM_ID/g" ExportOptions.plist > build/ExportOptions.plist
xcodebuild -exportArchive \
  -archivePath build/Chops.xcarchive \
  -exportOptionsPlist build/ExportOptions.plist \
  -exportPath build/export

echo "📦 Creating DMG..."
create_chops_dmg

echo "🔏 Notarizing..."
xcrun notarytool submit build/Chops.dmg \
  --keychain-profile "AC_PASSWORD" \
  --wait

echo "📎 Stapling..."
xcrun stapler staple build/export/Chops.app
create_chops_dmg
xcrun stapler staple build/Chops.dmg || echo "⚠️  DMG staple failed (normal — CDN propagation delay). App inside is stapled."

echo "🏷️  Tagging v$VERSION..."
git tag "v$VERSION"
git push --tags

echo "📡 Generating Sparkle appcast..."
SPARKLE_BIN=$(find ~/Library/Developer/Xcode/DerivedData/Chops-*/SourcePackages/artifacts/sparkle/Sparkle/bin -maxdepth 0 2>/dev/null | head -1)
SIGNATURE=$("$SPARKLE_BIN/sign_update" build/Chops.dmg 2>&1)
ED_SIG=$(echo "$SIGNATURE" | grep -o 'sparkle:edSignature="[^"]*"' | cut -d'"' -f2)
LENGTH=$(echo "$SIGNATURE" | grep -o 'length="[^"]*"' | cut -d'"' -f2)
PUB_DATE=$(date -u +"%a, %d %b %Y %H:%M:%S +0000")

# Extract release notes from CHANGELOG.md
RELEASE_NOTES=$(extract_changelog "$VERSION" "CHANGELOG.md")
if [ -z "$RELEASE_NOTES" ]; then
  echo "⚠️  No changelog entry for v$VERSION in CHANGELOG.md. Appcast will have no release notes."
fi

# Preserve existing items from current appcast (exclude current version if re-releasing)
EXISTING_ITEMS=""
if [ -f site/public/appcast.xml ]; then
  EXISTING_ITEMS=$(awk '
    /<item>/ { buf=""; capture=1 }
    capture { buf = buf $0 "\n" }
    /<\/item>/ {
      capture=0
      if (buf !~ /<sparkle:version>'"$VERSION"'</) printf "%s", buf
    }
  ' site/public/appcast.xml)
fi

# Build description element if we have release notes
DESC_ELEMENT=""
if [ -n "$RELEASE_NOTES" ]; then
  DESC_ELEMENT="      <description><![CDATA[$RELEASE_NOTES]]></description>"
fi

cat > build/appcast.xml << APPCAST
<?xml version="1.0" standalone="yes"?>
<rss xmlns:sparkle="http://www.andymatuschak.org/xml-namespaces/sparkle" xmlns:dc="http://purl.org/dc/elements/1.1/" version="2.0">
  <channel>
    <title>Chops</title>
    <item>
      <title>Version $VERSION</title>
      <sparkle:version>$VERSION</sparkle:version>
      <sparkle:shortVersionString>$VERSION</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <pubDate>$PUB_DATE</pubDate>
$DESC_ELEMENT
      <enclosure
        url="https://github.com/Shpigford/chops/releases/download/v$VERSION/Chops.dmg"
        sparkle:edSignature="$ED_SIG"
        length="$LENGTH"
        type="application/octet-stream"
      />
    </item>
$EXISTING_ITEMS
  </channel>
</rss>
APPCAST

echo "📡 Updating site appcast..."
cp build/appcast.xml site/public/appcast.xml
git add site/public/appcast.xml
git commit -m "chore: update appcast for v$VERSION" || true
git push

echo "🚀 Creating GitHub Release..."
CHANGELOG_MD=$(extract_changelog_markdown "$VERSION" "CHANGELOG.md")
if [ -n "$CHANGELOG_MD" ]; then
  gh release create "v$VERSION" build/Chops.dmg \
    --title "Chops v$VERSION" \
    --notes "$CHANGELOG_MD"
else
  gh release create "v$VERSION" build/Chops.dmg \
    --title "Chops v$VERSION" \
    --generate-notes
fi

echo "✅ Done! Release: https://github.com/Shpigford/chops/releases/tag/v$VERSION"
```

## File: `site/astro.config.mjs`
```
import { defineConfig } from 'astro/config';

export default defineConfig({});
```

## File: `site/package.json`
```json
{
  "name": "chops-site",
  "type": "module",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  },
  "dependencies": {
    "astro": "^6.0.5",
    "sharp": "^0.34.5"
  }
}
```

## File: `site/tsconfig.json`
```json
{
  "extends": "astro/tsconfigs/strict"
}
```

## File: `site/public/appcast.xml`
```xml
<?xml version="1.0" standalone="yes"?>
<rss xmlns:sparkle="http://www.andymatuschak.org/xml-namespaces/sparkle" xmlns:dc="http://purl.org/dc/elements/1.1/" version="2.0">
  <channel>
    <title>Chops</title>
    <item>
      <title>Version 1.11.0</title>
      <sparkle:version>1.11.0</sparkle:version>
      <sparkle:shortVersionString>1.11.0</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <pubDate>Sun, 29 Mar 2026 00:14:42 +0000</pubDate>
      <description><![CDATA[<ul><li>Chat with AI agents directly inside Chops (ACP support)</li><li>Cancel in-progress AI requests</li><li>Floating AI button for quick access to the compose panel</li><li>Improved compose panel layout and usability</li></ul>]]></description>
      <enclosure
        url="https://github.com/Shpigford/chops/releases/download/v1.11.0/Chops.dmg"
        sparkle:edSignature="VoAIFNjRVMUwqUsuTdEN+MHKD6o61PWqKl51RdzEFkLcOIahsXp5WcZd3joqcYmdM92RFcJ+6O2iZuqd+7LnCg=="
        length="5825308"
        type="application/octet-stream"
      />
    </item>
    <item>
      <title>Version 1.10.0</title>
      <sparkle:version>1.10.0</sparkle:version>
      <sparkle:shortVersionString>1.10.0</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <pubDate>Fri, 27 Mar 2026 23:59:11 +0000</pubDate>
      <description><![CDATA[<ul><li>Native markdown editor with syntax highlighting and formatting shortcuts (bold, italic, headings, links, lists)</li><li>Select and copy text from the skill preview</li><li>Find bar in the skill editor (Cmd+F)</li><li>Auto-save skill files after 1 second of inactivity</li></ul>]]></description>
      <enclosure
        url="https://github.com/Shpigford/chops/releases/download/v1.10.0/Chops.dmg"
        sparkle:edSignature="/mNmqpaHj33NSPue4AHFXyuLqxwUpfr/7lVFY3b9EZkrnPOGbLwLGD2D/CrRsfmeXX3ohloopq4JOsk2JqxuDQ=="
        length="4529350"
        type="application/octet-stream"
      />
    </item>
    <item>
      <title>Version 1.9.0</title>
      <sparkle:version>1.9.0</sparkle:version>
      <sparkle:shortVersionString>1.9.0</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <pubDate>Fri, 27 Mar 2026 11:52:04 +0000</pubDate>
      <description><![CDATA[<ul><li>Scan and display agents alongside skills</li></ul>]]></description>
      <enclosure
        url="https://github.com/Shpigford/chops/releases/download/v1.9.0/Chops.dmg"
        sparkle:edSignature="Ux0cW/DAVJLNRYALQXACS8c5eZ4WrneLoDFF9ah1zq0D2ig3nQhfkSIphlSwveGCUy2STeqMhG6KzC6Bb5ruCA=="
        length="5117326"
        type="application/octet-stream"
      />
    </item>
    <item>
      <title>Version 1.8.0</title>
      <sparkle:version>1.8.0</sparkle:version>
      <sparkle:shortVersionString>1.8.0</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <pubDate>Wed, 25 Mar 2026 11:45:30 +0000</pubDate>
      <description><![CDATA[<ul><li>Add skills to collections via right-click context menu</li><li>Drag and drop skills into sidebar collections</li><li>Detect skills from Claude Desktop and CLI plugins</li><li>Faster skill preview loading (eliminated ~2s delay)</li></ul>]]></description>
      <enclosure
        url="https://github.com/Shpigford/chops/releases/download/v1.8.0/Chops.dmg"
        sparkle:edSignature="61CLO9ZmLNdIEP3ItN9Qw/YNJKzJvkOb+b+o4CFmxQCDAoX23fvzMVFL9yfUnuoSr5DgBkMApJrkWZl/Wbo0Cg=="
        length="5092967"
        type="application/octet-stream"
      />
    </item>
    <item>
      <title>Version 1.7.0</title>
      <sparkle:version>1.7.0</sparkle:version>
      <sparkle:shortVersionString>1.7.0</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <pubDate>Wed, 25 Mar 2026 01:00:41 +0000</pubDate>
      <description><![CDATA[<ul><li>Rich markdown theme in skill preview</li><li>Support for Antigravity, OpenCode, Pi, Global Agents, and Copilot CLI as tool sources</li><li>Sidebar hides tools that aren't installed</li><li>Non-skill config files hidden from All Skills view</li><li>Fixed Sparkle minimum macOS version requirement</li></ul>]]></description>
      <enclosure
        url="https://github.com/Shpigford/chops/releases/download/v1.7.0/Chops.dmg"
        sparkle:edSignature="igfT1d3JChZNaJt6/o5bLuGAGVbejCvOeNhsfF0SKVls/ypS+cBIbo1G5Rr+TLi3I72qj/I+x/uDct7uEOCpAQ=="
        length="5066617"
        type="application/octet-stream"
      />
    </item>
    <item>
      <title>Version 1.6.0</title>
      <sparkle:version>1.6.0</sparkle:version>
      <sparkle:shortVersionString>1.6.0</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <pubDate>Sun, 22 Mar 2026 21:29:20 +0000</pubDate>
      <description><![CDATA[<ul><li>Fix layout freeze when selecting a skill</li><li>Press Enter to quickly create new collections</li><li>Rename collections from the right-click menu</li></ul>]]></description>
      <enclosure
        url="https://github.com/Shpigford/chops/releases/download/v1.6.0/Chops.dmg"
        sparkle:edSignature="c1/GR3wH3ToIK7Ie+Pd1pnVfIBRNRfO1XB62/E/6bH2KsPwJdYGoGjc2+EMKbNWtVuYh//E+Xa2ZG0VrvdNuDA=="
        length="5031217"
        type="application/octet-stream"
      />
    </item>
    <item>
      <title>Version 1.5.0</title>
      <sparkle:version>1.5.0</sparkle:version>
      <sparkle:shortVersionString>1.5.0</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <pubDate>Sat, 21 Mar 2026 17:17:31 +0000</pubDate>
      <description><![CDATA[<ul><li>Connect to remote servers (such as OpenClaw) to discover, browse, and edit skills (@t2)</li></ul>]]></description>
      <enclosure
        url="https://github.com/Shpigford/chops/releases/download/v1.5.0/Chops.dmg"
        sparkle:edSignature="LKJq0Pl5JbGei5RMgkTbckCYOOUUIzN+8ICYHh7pxMjfuq5b5PsnjIYsZj/tORGssYg68NVq2sHoTRfcP/+oAQ=="
        length="5028073"
        type="application/octet-stream"
      />
    </item>
    <item>
      <title>Version 1.4.0</title>
      <sparkle:version>1.4.0</sparkle:version>
      <sparkle:shortVersionString>1.4.0</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <pubDate>Sat, 21 Mar 2026 15:26:57 +0000</pubDate>
      <description><![CDATA[<ul><li>Delete skills directly from the context menu or toolbar</li><li>Diagnostic logging and fixes for UI freezing</li></ul>]]></description>
      <enclosure
        url="https://github.com/Shpigford/chops/releases/download/v1.4.0/Chops.dmg"
        sparkle:edSignature="BmqlyXVbU1nH7deMBivz82uLAQr1hAWX83k0ymE0HRQyh+1BSm6UMUnJdCGkffZtBT/MaAg5dqcs7HYj4Ic6Cw=="
        length="4854431"
        type="application/octet-stream"
      />
    </item>
    <item>
      <title>Version 1.3.0</title>
      <sparkle:version>1.3.0</sparkle:version>
      <sparkle:shortVersionString>1.3.0</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <pubDate>Sat, 21 Mar 2026 12:59:53 +0000</pubDate>
      <description><![CDATA[<ul><li>Markdown preview mode with syntax highlighting in the skill editor</li></ul>]]></description>
      <enclosure
        url="https://github.com/Shpigford/chops/releases/download/v1.3.0/Chops.dmg"
        sparkle:edSignature="pwIDvkJulZ+sySL8kHl11S1zBSUwW51CIbFLbBJHc8HU9VS7caO8aXm5q8aLppuHcJP6jRr2xheCpNt4AwDNBA=="
        length="4800773"
        type="application/octet-stream"
      />
    </item>
    <item>
      <title>Version 1.2.0</title>
      <sparkle:version>1.2.0</sparkle:version>
      <sparkle:shortVersionString>1.2.0</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <pubDate>Sat, 21 Mar 2026 12:00:18 +0000</pubDate>
      <description><![CDATA[<ul><li>Skills registry browser for discovering and installing community skills</li></ul>]]></description>
      <enclosure
        url="https://github.com/Shpigford/chops/releases/download/v1.2.0/Chops.dmg"
        sparkle:edSignature="LtEzDqwAraqYmW3MIdREbPGHkisMXZJbTp37gBHE3hiTFUytnVBHgGdHt1CYEaKGLxbWElf/LT6RTBvxQxI4DQ=="
        length="3359757"
        type="application/octet-stream"
      />
    </item>
    <item>
      <title>Version 1.1.0</title>
      <sparkle:version>1.1.0</sparkle:version>
      <sparkle:shortVersionString>1.1.0</sparkle:shortVersionString>
      <sparkle:minimumSystemVersion>15.0</sparkle:minimumSystemVersion>
      <pubDate>Thu, 19 Mar 2026 12:24:55 +0000</pubDate>
      <enclosure
        url="https://github.com/Shpigford/chops/releases/download/v1.1.0/Chops.dmg"
        sparkle:edSignature="8mJcAK7hO2JjAgr5rph42cBNQFMpyW/pwexBERFka4kvNQRL+0jvT4JfDxnFuC+ZG300K9n0dvR0EZqxLuieCw=="
        length="3225001"
        type="application/octet-stream"
      />
    </item>
  </channel>
</rss>
```

## File: `site/src/layouts/Layout.astro`
```
---
interface Props {
  title: string;
}

const { title } = Astro.props;
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="A free, open-source macOS app to manage your AI coding agent skills in one place." />
    <link rel="icon" type="image/png" href="/favicon.png" />
    <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  </head>
  <body>
    <slot />
  </body>
</html>

<style is:global>
  :root {
    --green: #34C759;
    --teal: #00C8B3;
    --gradient: linear-gradient(135deg, var(--green), var(--teal));
    --bg: #ffffff;
    --text: #1a1a1a;
    --text-secondary: #666;
    --text-tertiary: #999;
    --font: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  }

  *, *::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  html {
    font-family: var(--font);
    color: var(--text);
    background: var(--bg);
    -webkit-font-smoothing: antialiased;
  }

  body {
    min-height: 100vh;
  }

  a {
    color: inherit;
    text-decoration: none;
  }
</style>
```

## File: `site/src/pages/index.astro`
```
---
import Layout from '../layouts/Layout.astro';
---

<Layout title="Chops — Your AI agent skills, finally organized.">
  <main>
    <div class="hero">
      <img src="/icon.png" alt="Chops" class="icon" />
      <h1>Chops</h1>
      <p class="tagline">Your AI agent skills, finally organized.</p>
      <p class="description">
        One app to browse, edit, and manage skills across
        Claude Code, Cursor, Codex, Windsurf, and Amp.
        Free and open source.
      </p>
      <div class="buttons">
        <a href="https://github.com/Shpigford/chops/releases/latest/download/Chops.dmg" class="btn primary"><svg width="16" height="16" viewBox="0 0 814 1000" fill="currentColor"><path d="M788.1 340.9c-5.8 4.5-108.2 62.2-108.2 190.5 0 148.4 130.3 200.9 134.2 202.2-.6 3.2-20.7 71.9-68.7 141.9-42.8 61.6-87.5 123.1-155.5 123.1s-85.5-39.5-164-39.5c-76.5 0-103.7 40.8-165.9 40.8s-105.6-57.8-155.5-127.4c-58.5-81.7-105.3-209-105.3-329.1 0-193.1 125.6-295.7 249.2-295.7 65.7 0 120.5 43.2 161.7 43.2 39.2 0 100.4-45.8 174.5-45.8 28.2 0 129.3 2.6 196.3 99.8zm-135.5-183.1c31.1-36.9 53.1-88.1 53.1-139.3 0-7.1-.6-14.3-1.9-20.1-50.6 1.9-110.8 33.7-147.1 75.8-28.2 32.4-55.1 83.6-55.1 135.5 0 7.8 1.3 15.6 1.9 18.1 3.2.6 8.4 1.3 13.6 1.3 45.4 0 102.5-30.4 135.5-71.3z"/></svg> Download for macOS</a>
        <a href="https://github.com/Shpigford/chops" class="btn secondary">GitHub</a>
      </div>
      <p class="requires">v1.11.0 &middot; Requires macOS Sequoia</p>
    </div>

    <img src="/screenshot.png" alt="Chops app screenshot" class="screenshot" />

    <footer>
      <p>&copy; 2026 Chops &middot; <a href="https://github.com/Shpigford/chops">Open source</a> under MIT</p>
    </footer>
  </main>
</Layout>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    padding: 4rem 2rem 2rem;
    text-align: center;
  }

  .hero {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1;
    justify-content: center;
  }

  .icon {
    width: 160px;
    height: 160px;
    margin-bottom: 2rem;
  }

  h1 {
    font-size: 3rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
  }

  .tagline {
    font-size: 1.25rem;
    color: var(--text-secondary);
    margin-bottom: 1rem;
  }

  .description {
    font-size: 1rem;
    color: var(--text-tertiary);
    max-width: 420px;
    line-height: 1.6;
    margin-bottom: 2rem;
  }

  .buttons {
    display: flex;
    gap: 0.75rem;
    margin-bottom: 1.5rem;
  }

  .btn {
    padding: 0.65rem 1.5rem;
    border-radius: 8px;
    font-size: 0.95rem;
    font-weight: 500;
    transition: opacity 0.15s;
  }

  .btn:hover {
    opacity: 0.85;
  }

  .btn.primary {
    background: var(--gradient);
    color: white;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
  }

  .btn.primary svg {
    flex-shrink: 0;
  }

  .btn.secondary {
    background: #f0f0f0;
    color: var(--text);
  }

  .requires {
    font-size: 0.8rem;
    color: var(--text-tertiary);
  }

  .screenshot {
    max-width: 960px;
    width: 100%;
    margin-bottom: 4rem;
  }

  footer {
    padding: 2rem;
    font-size: 0.8rem;
    color: var(--text-tertiary);
  }

  footer a {
    text-decoration: underline;
    text-underline-offset: 2px;
  }
</style>
```

