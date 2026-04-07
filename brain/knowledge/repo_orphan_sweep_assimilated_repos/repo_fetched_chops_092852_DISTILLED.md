---
id: repo-fetched-chops-092852
type: knowledge
owner: OA
registered_at: 2026-04-05T04:11:59.968662
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_chops_092852

## Assimilation Report
Auto-cloned repository: FETCHED_chops_092852

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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
- **Remote servers** — Connect to servers running [OpenClaw](https://openclaw.ai), [Hermes](https://github.com/NousResearch/hermes-agent), or other layouts to discover, browse, and install skills

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

### File: site\package.json
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

### File: CHANGELOG.md
```md
# Changelog

## [Unreleased]

## [1.14.0] - 2026-04-03

- Add Hermes as a tool source
- Fixed editor diffs overwriting content that hadn't changed
- Added Opus model option to the Claude agent model picker

## [1.13.1] - 2026-03-31

- Prevents data loss when the database schema changes between versions

## [1.13.0] - 2026-03-31

- New skills default to Global and are automatically symlinked to all installed agents
- Convert any tool-specific skill to Global via the right-click menu
- Global tool source now appears in the sidebar when skills exist
- AI Assist no longer writes files until you accept the diff
- Fixed false "not installed" detection for tools using symlinked agent directories

## [1.12.0] - 2026-03-31

- Browse and install skills from OpenClaw directly on your machine
- Organize skills, rules, and agents into separate categories
- Skills inside custom scan directories are now detected correctly
- Registry browsing no longer hits GitHub API rate limits

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

### File: CLAUDE.md
```md
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
SwiftData store path is explicit: `~/Library/Application Support/Chops/Chops.store`. Do not rely on the implicit `default.store`.

**State:** `AppState` is an `@Observable` singleton holding UI filters, search text, and selection state.

**Models (SwiftData):**
- `Skill` — a discovered skill file. Uniquely identified by resolved symlink path. Tracks which tools it's installed in.
- `SkillCollection` — user-created groupings of skills (pure user data, not filesystem-backed — data loss is permanent).

**Schema versioning:** SwiftData models use `VersionedSchema` + `SchemaMigrationPlan` (see `SchemaVersions.swift`). Each schema version must declare its own nested `@Model` snapshots; app code reaches the current version through top-level `typealias`es like `Skill = SchemaV1.Skill`. When adding or changing a stored property, freeze the previous schema in place, add a new schema version (e.g. `SchemaV2`) with its own nested models, move the typealiases to the new version, and add the corresponding `MigrationStage`. Never point an older schema version at live top-level models — future migrations will crash with duplicate checksums.

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

### File: SECURITY.md
```md
# Security Policy

If you discover a security vulnerability in Chops, please report it through
GitHub's [private vulnerability reporting](https://github.com/Shpigford/chops/security/advisories/new)
rather than opening a public issue.

```

### File: scripts\release.sh
```sh
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

### File: site\package-lock.json
```json
{
  "name": "chops-site",
  "version": "0.0.1",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "chops-site",
      "version": "0.0.1",
      "dependencies": {
        "astro": "^6.0.5",
        "sharp": "^0.34.5"
      }
    },
    "node_modules/@astrojs/compiler": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/@astrojs/compiler/-/compiler-3.0.1.tgz",
      "integrity": "sha512-z97oYbdebO5aoWzuJ/8q5hLK232+17KcLZ7cJ8BCWk6+qNzVxn/gftC0KzMBUTD8WAaBkPpNSQK6PXLnNrZ0CA==",
      "license": "MIT"
    },
    "node_modules/@astrojs/internal-helpers": {
      "version": "0.8.0",
      "resolved": "https://registry.npmjs.org/@astrojs/internal-helpers/-/internal-helpers-0.8.0.tgz",
      "integrity": "sha512-J56GrhEiV+4dmrGLPNOl2pZjpHXAndWVyiVDYGDuw6MWKpBSEMLdFxHzeM/6sqaknw9M+HFfHZAcvi3OfT3D/w==",
      "license": "MIT",
      "dependencies": {
        "picomatch": "^4.0.3"
      }
    },
    "node_modules/@astrojs/markdown-remark": {
      "version": "7.0.0",
      "resolved": "https://registry.npmjs.org/@astrojs/markdown-remark/-/markdown-remark-7.0.0.tgz",
      "integrity": "sha512-jTAXHPy45L7o1ljH4jYV+ShtOHtyQUa1mGp3a5fJp1soX8lInuTJQ6ihmldHzVM4Q7QptU4SzIDIcKbBJO7sXQ==",
      "license": "MIT",
      "dependencies": {
        "@astrojs/internal-helpers": "0.8.0",
        "@astrojs/prism": "4.0.0",
        "github-slugger": "^2.0.0",
        "hast-util-from-html": "^2.0.3",
        "hast-util-to-text": "^4.0.2",
        "js-yaml": "^4.1.1",
        "mdast-util-definitions": "^6.0.0",
        "rehype-raw": "^7.0.0",
        "rehype-stringify": "^10.0.1",
        "remark-gfm": "^4.0.1",
        "remark-parse": "^11.0.0",
        "remark-rehype": "^11.1.2",
        "remark-smartypants": "^3.0.2",
        "shiki": "^4.0.0",
        "smol-toml": "^1.6.0",
        "unified": "^11.0.5",
        "unist-util-remove-position": "^5.0.0",
        "unist-util-visit": "^5.1.0",
        "unist-util-visit-parents": "^6.0.2",
        "vfile": "^6.0.3"
      }
    },
    "node_modules/@astrojs/prism": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/@astrojs/prism/-/prism-4.0.0.tgz",
      "integrity": "sha512-NndtNPpxaGinRpRytljGBvYHpTOwHycSZ/c+lQi5cHvkqqrHKWdkPEhImlODBNmbuB+vyQUNUDXyjzt66CihJg==",
      "license": "MIT",
      "dependencies": {
        "prismjs": "^1.30.0"
      },
      "engines": {
        "node": "^20.19.1 || >=22.12.0"
      }
    },
    "node_modules/@astrojs/telemetry": {
      "version": "3.3.0",
      "resolved": "https://registry.npmjs.org/@astrojs/telemetry/-/telemetry-3.3.0.tgz",
      "integrity": "sha512-UFBgfeldP06qu6khs/yY+q1cDAaArM2/7AEIqQ9Cuvf7B1hNLq0xDrZkct+QoIGyjq56y8IaE2I3CTvG99mlhQ==",
      "license": "MIT",
      "dependencies": {
        "ci-info": "^4.2.0",
        "debug": "^4.4.0",
        "dlv": "^1.1.3",
        "dset": "^3.1.4",
        "is-docker": "^3.0.0",
        "is-wsl": "^3.1.0",
        "which-pm-runs": "^1.1.0"
      },
      "engines": {
        "node": "18.20.8 || ^20.3.0 || >=22.0.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
      "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
      "integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.29.2",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.29.2.tgz",
      "integrity": "sha512-4GgRzy/+fsBa72/RZVJmGKPmZu9Byn8o4MoLpmNe1m8ZfYnz5emHLQz3U4gLud6Zwl0RZIcgiLD7Uq7ySFuDLA==",
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.29.0"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.29.0.tgz",
      "integrity": "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A==",
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.28.5"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@capsizecss/unpack": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/@capsizecss/unpack/-/unpack-4.0.0.tgz",
      "integrity": "sha512-VERIM64vtTP1C4mxQ5thVT9fK0apjPFobqybMtA1UdUujWka24ERHbRHFGmpbbhp73MhV+KSsHQH9C6uOTdEQA==",
      "license": "MIT",
      "dependencies": {
        "fontkitten": "^1.0.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@clack/core": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@clack/core/-/core-1.1.0.tgz",
      "integrity": "sha512-SVcm4Dqm2ukn64/8Gub2wnlA5nS2iWJyCkdNHcvNHPIeBTGojpdJ+9cZKwLfmqy7irD4N5qLteSilJlE0WLAtA==",
      "license": "MIT",
      "dependencies": {
        "sisteransi": "^1.0.5"
      }
    },
    "node_modules/@clack/prompts": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/@clack/prompts/-/prompts-1.1.0.tgz",
      "integrity": "sha512-pkqbPGtohJAvm4Dphs2M8xE29ggupihHdy1x84HNojZuMtFsHiUlRvqD24tM2+XmI+61LlfNceM3Wr7U5QES5g==",
      "license": "MIT",
      "dependencies": {
        "@clack/core": "1.1.0",
        "sisteransi": "^1.0.5"
      }
    },
    "node_modules/@emnapi/runtime": {
      "version": "1.9.0",
      "resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.9.0.tgz",
      "integrity": "sha512-QN75eB0IH2ywSpRpNddCRfQIhmJYBCJ1x5Lb3IscKAL8bMnVAKnRg8dCoXbHzVLLH7P38N2Z3mtulB7W0J0FKw==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.27.4.tgz",
      "integrity": "sha512-cQPwL2mp2nSmHHJlCyoXgHGhbEPMrEEU5xhkcy3Hs/O7nGZqEpZ2sUtLaL9MORLtDfRvVl2/3PAuEkYZH0Ty8Q==",
      "cpu": [
        "ppc64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "aix"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.27.4.tgz",
      "integrity": "sha512-X9bUgvxiC8CHAGKYufLIHGXPJWnr0OCdR0anD2e21vdvgCI8lIfqFbnoeOz7lBjdrAGUhqLZLcQo6MLhTO2DKQ==",
      "cpu": [
        "arm"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.27.4.tgz",
      "integrity": "sha512-gdLscB7v75wRfu7QSm/zg6Rx29VLdy9eTr2t44sfTW7CxwAtQghZ4ZnqHk3/ogz7xao0QAgrkradbBzcqFPasw==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.27.4.tgz",
      "integrity": "sha512-PzPFnBNVF292sfpfhiyiXCGSn9HZg5BcAz+ivBuSsl6Rk4ga1oEXAamhOXRFyMcjwr2DVtm40G65N3GLeH1Lvw==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.27.4.tgz",
      "integrity": "sha512-b7xaGIwdJlht8ZFCvMkpDN6uiSmnxxK56N2GDTMYPr2/gzvfdQN8rTfBsvVKmIVY/X7EM+/hJKEIbbHs9oA4tQ==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.27.4.tgz",
      "integrity": "sha512-sR+OiKLwd15nmCdqpXMnuJ9W2kpy0KigzqScqHI3Hqwr7IXxBp3Yva+yJwoqh7rE8V77tdoheRYataNKL4QrPw==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.27.4.tgz",
      "integrity": "sha512-jnfpKe+p79tCnm4GVav68A7tUFeKQwQyLgESwEAUzyxk/TJr4QdGog9sqWNcUbr/bZt/O/HXouspuQDd9JxFSw==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.27.4.tgz",
      "integrity": "sha512-2kb4ceA/CpfUrIcTUl1wrP/9ad9Atrp5J94Lq69w7UwOMolPIGrfLSvAKJp0RTvkPPyn6CIWrNy13kyLikZRZQ==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.27.4.tgz",
      "integrity": "sha512-aBYgcIxX/wd5n2ys0yESGeYMGF+pv6g0DhZr3G1ZG4jMfruU9Tl1i2Z+Wnj9/KjGz1lTLCcorqE2viePZqj4Eg==",
      "cpu": [
        "arm"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.27.4.tgz",
      "integrity": "sha512-7nQOttdzVGth1iz57kxg9uCz57dxQLHWxopL6mYuYthohPKEK0vU0C3O21CcBK6KDlkYVcnDXY099HcCDXd9dA==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ia32": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.27.4.tgz",
      "integrity": "sha512-oPtixtAIzgvzYcKBQM/qZ3R+9TEUd1aNJQu0HhGyqtx6oS7qTpvjheIWBbes4+qu1bNlo2V4cbkISr8q6gRBFA==",
      "cpu": [
        "ia32"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-loong64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.27.4.tgz",
      "integrity": "sha512-8mL/vh8qeCoRcFH2nM8wm5uJP+ZcVYGGayMavi8GmRJjuI3g1v6Z7Ni0JJKAJW+m0EtUuARb6Lmp4hMjzCBWzA==",
      "cpu": [
        "loong64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-mips64el": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.27.4.tgz",
      "integrity": "sha512-1RdrWFFiiLIW7LQq9Q2NES+HiD4NyT8Itj9AUeCl0IVCA459WnPhREKgwrpaIfTOe+/2rdntisegiPWn/r/aAw==",
      "cpu": [
        "mips64el"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ppc64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.27.4.tgz",
      "integrity": "sha512-tLCwNG47l3sd9lpfyx9LAGEGItCUeRCWeAx6x2Jmbav65nAwoPXfewtAdtbtit/pJFLUWOhpv0FpS6GQAmPrHA==",
      "cpu": [
        "ppc64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-riscv64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.27.4.tgz",
      "integrity": "sha512-BnASypppbUWyqjd1KIpU4AUBiIhVr6YlHx/cnPgqEkNoVOhHg+YiSVxM1RLfiy4t9cAulbRGTNCKOcqHrEQLIw==",
      "cpu": [
        "riscv64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-s390x": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.27.4.tgz",
      "integrity": "sha512-+eUqgb/Z7vxVLezG8bVB9SfBie89gMueS+I0xYh2tJdw3vqA/0ImZJ2ROeWwVJN59ihBeZ7Tu92dF/5dy5FttA==",
      "cpu": [
        "s390x"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.27.4.tgz",
      "integrity": "sha512-S5qOXrKV8BQEzJPVxAwnryi2+Iq5pB40gTEIT69BQONqR7JH1EPIcQ/Uiv9mCnn05jff9umq/5nqzxlqTOg9NA==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-arm64/-/netbsd-arm64-0.27.4.tgz",
      "integrity": "sha512-xHT8X4sb0GS8qTqiwzHqpY00C95DPAq7nAwX35Ie/s+LO9830hrMd3oX0ZMKLvy7vsonee73x0lmcdOVXFzd6Q==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.27.4.tgz",
      "integrity": "sha512-RugOvOdXfdyi5Tyv40kgQnI0byv66BFgAqj
... [TRUNCATED]
```

### File: site\tsconfig.json
```json
{
  "extends": "astro/tsconfigs/strict"
}

```

### File: Chops\ChopsIcon.icon\icon.json
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

### File: .claude\skills\release\SKILL.md
```md
---
name: release
description: Determine the next version, update the marketing site, and run the full release pipeline.
---

Cut a new release of Chops. Determines the version from git history, updates the marketing site, and runs the release script.

## Instructions

### Step 1: Verify prerequisites

1. Confirm `.env` exists in the project root. If it does not, stop and tell the user:
   "Missing `.env` file. Copy `.env.example` to `.env` and fill in APPLE_TEAM_ID, APPLE_ID, and SIGNING_IDENTITY_NAME."
2. Confirm the notarytool keychain profile `AC_PASSWORD` works:
   ```bash
   xcrun notarytool history --keychain-profile "AC_PASSWORD" >/dev/null 2>&1
   ```
   If it fails, stop and tell the user to run:
   ```bash
   xcrun notarytool store-credentials "AC_PASSWORD" --apple-id "<APPLE_ID>" --team-id "<TEAM_ID>" --password "<app-specific-password>"
   ```
3. Confirm the working tree is clean (`git status --porcelain`). If there are uncommitted changes, stop and tell the user to commit or stash first.
4. Confirm you are on the `main` branch. If not, stop and tell the user to switch to `main` first.

### Step 2: Determine the next version

1. Get the latest tag:
   ```bash
   git tag -l 'v*' | sort -V | tail -1
   ```
2. Get commits since that tag:
   ```bash
   git log <latest_tag>..HEAD --oneline --format='%s'
   ```
3. If there are zero commits since the last tag, stop and tell the user there is nothing to release.
4. Apply semver logic to the current latest version:
   - If any commit message starts with `feat:` or `feat(` → **minor** bump (e.g. 1.1.0 → 1.2.0)
   - If all commits are `fix:`, `chore:`, `docs:`, or similar → **patch** bump (e.g. 1.1.0 → 1.1.1)
   - If any commit contains `BREAKING CHANGE` or uses a `!:` suffix → ask the user what version to use
   - If the commit messages are ambiguous or do not follow conventional commits, use `mcp__conductor__AskUserQuestion` to ask:
     - question: "Commits since the last release don't clearly indicate the version bump. What version should this release be?"
     - header: "Release version"
     - multiSelect: false
     - options with labels: "Patch (X.Y.Z+1)", "Minor (X.Y+1.0)", "Major (X+1.0.0)", "Custom"

### Step 3: Confirm the version

Always confirm the version before proceeding. Use `mcp__conductor__AskUserQuestion`:
- question: "Release as v<VERSION>? Commits included:\n<commit list>"
- header: "Confirm release"
- multiSelect: false
- options:
  - "Yes, release v<VERSION>"
  - "Use a different version"
  - "Cancel"

If the user picks "Use a different version", ask them for the version number. If they pick "Cancel", stop.

### Step 3.5: Update CHANGELOG.md

1. Check if `CHANGELOG.md` has an `## [Unreleased]` section with content (bullet points).
2. If the `## [Unreleased]` section is empty or missing, draft entries from commits since the last tag:
   - **Rewrite each entry to be user-facing.** Don't echo commit messages. Describe what changed from the user's perspective — what it enables, fixes, or improves.
   - Bad: "feat: add skills registry browser with multi-agent install"
   - Good: "Browse and install community skills directly from the app"
   - Keep entries succinct (one line each). No technical jargon, no commit prefixes.
   - Confirm the drafted entries with the user using `mcp__conductor__AskUserQuestion`.
3. Rename `## [Unreleased]` to `## [VERSION] - YYYY-MM-DD` (today's date).
4. Add a new empty `## [Unreleased]` section above it.

### Step 4: Update the marketing site version

1. Edit `site/src/pages/index.astro`. Find the line containing `class="requires"` and replace it with:
   ```html
   <p class="requires">v<VERSION> &middot; Requires macOS Sequoia</p>
   ```
   where `<VERSION>` is the confirmed version.
2. Commit this change along with the changelog:
   ```bash
   git add site/src/pages/index.astro CHANGELOG.md
   git commit -m "chore: update site version to v<VERSION>"
   git push
   ```

### Step 5: Run the release script

```bash
./scripts/release.sh <VERSION>
```

This handles: xcodegen → archive → export → DMG → notarize → staple → git tag → appcast → push → GitHub Release.

Let it run to completion. If it fails, report the error output to the user and stop. Do NOT retry automatically.

### Step 6: Push and report

Ensure all commits are on the remote:
```bash
git push
```

Tell the user:
- The version that was released
- Link: `https://github.com/Shpigford/chops/releases/tag/v<VERSION>`
- Remind them to deploy the marketing site if needed (`npm run build` from `site/`)

## Important Rules

- ALWAYS confirm the version with the user before proceeding
- NEVER run the release script if `.env` is missing or the working tree is dirty
- NEVER skip the marketing site version update
- If the release script fails, do NOT retry — report the error and stop
- The release script handles git tagging and GitHub release creation — do not duplicate those steps

```

### File: .claude\skills\setup\SKILL.md
```md
---
name: setup
description: Get a new developer up and running with the Chops codebase — prerequisites, build, architecture, and common tasks.
---

Set up the Chops development environment and orient a new contributor to the codebase.

## Instructions

### Step 1: Check prerequisites

Verify these are installed. If any are missing, tell the user what to install and stop.

1. **macOS 15+** — `sw_vers -productVersion` (must be ≥ 15.0)
2. **Xcode CLI tools** — `xcode-select -p` (if missing: `xcode-select --install`)
3. **Homebrew** — `which brew` (if missing: direct them to https://brew.sh)
4. **xcodegen** — `which xcodegen` (if missing: `brew install xcodegen`)

### Step 2: Generate Xcode project

```bash
xcodegen generate
```

This reads `project.yml` (the source of truth for all Xcode project settings) and generates `Chops.xcodeproj`. Re-run this anytime `project.yml` changes. Never edit the `.xcodeproj` directly.

### Step 3: Build and run

```bash
xcodebuild -scheme Chops -configuration Debug build
```

Or open in Xcode and hit Cmd+R:

```bash
open Chops.xcodeproj
```

### Step 4: Orient the developer

Share this architecture overview:

**Entry point:** `Chops/App/ChopsApp.swift` — sets up SwiftData ModelContainer (Skill + SkillCollection), starts Sparkle updater, injects AppState into environment.

**State:** `Chops/App/AppState.swift` — `@Observable` singleton holding UI state (selected tool, selected skill, search text, sidebar filter).

**Models (SwiftData):**
- `Chops/Models/Skill.swift` — a discovered skill file, uniquely identified by resolved symlink path
- `Chops/Models/Collection.swift` — user-created groupings of skills
- `Chops/Models/ToolSource.swift` — enum of supported tools with display names, icons, colors, and filesystem paths

**Services:**
- `Chops/Services/SkillScanner.swift` — probes tool directories, parses frontmatter, upserts into SwiftData. Deduplicates via resolved symlink paths.
- `Chops/Services/FileWatcher.swift` — FSEvents via DispatchSource, triggers re-scan on file changes
- `Chops/Services/SkillParser.swift` — dispatches to FrontmatterParser (.md) or MDCParser (.mdc)
- `Chops/Services/SearchService.swift` — in-memory full-text search

**Views:** Three-column NavigationSplitView (Sidebar → List → Detail). Editor wraps NSTextView for native text editing. Cmd+S save via FocusedValues.

**Key design decisions:**
- No sandbox — the app needs unrestricted filesystem access to read dotfiles across ~/
- Symlink dedup — same file in multiple tool dirs shows as one skill with multiple tool badges
- No test suite — validate manually by building, running, and observing

**Scanned tool paths:**

| Tool | Paths |
|------|-------|
| Claude Code | `~/.claude/skills/`, `~/.agents/skills` |
| Cursor | `~/.cursor/skills/`, `~/.cursor/rules` |
| Windsurf | `~/.codeium/windsurf/memories/`, `~/.windsurf/rules` |
| Codex | `~/.codex` |
| Amp | `~/.config/amp` |

Copilot and Aider detect project-level skills only (no global paths).

## Common tasks to be aware of

**Add a new tool:** Add a case to `ToolSource` enum in `Chops/Models/ToolSource.swift`. Fill in `displayName`, `iconName`, `color`, `globalPaths`. Update `SkillScanner` if the tool uses a non-standard file layout.

**Modify parsing:** Frontmatter → `Chops/Utilities/FrontmatterParser.swift`. Cursor .mdc → `Chops/Utilities/MDCParser.swift`. Dispatch logic → `Chops/Services/SkillParser.swift`.

**Change UI:** Views are in `Chops/Views/` (Sidebar/, Detail/, Settings/, Shared/). Main layout is `Chops/App/ContentView.swift`.

## Important Rules

- `project.yml` is the source of truth for Xcode settings — never edit `.xcodeproj` directly
- Sparkle (auto-updates) is the only external dependency — pulled automatically via SPM
- There is no test suite — always validate changes by building and running the app manually
- The app runs without sandbox — this is intentional and required

```

### File: Chops\Resources\Assets.xcassets\Contents.json
```json
{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}

```

### File: Chops\Resources\Assets.xcassets\AccentColor.colorset\Contents.json
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

### File: Chops\Resources\Assets.xcassets\tool-amp.imageset\Contents.json
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

### File: Chops\Resources\Assets.xcassets\tool-antigravity.imageset\Contents.json
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

### File: Chops\Resources\Assets.xcassets\tool-augment.imageset\Contents.json
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

### File: Chops\Resources\Assets.xcassets\tool-claude.imageset\Contents.json
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



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
