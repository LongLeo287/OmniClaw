---
id: ios
type: knowledge
owner: OA_Triage
---
# ios
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<img src=".github/ios-26-badge-icon.png" alt="Preview" width="25%" />

# iOS 26 by Examples

![Xcode 26+](https://img.shields.io/badge/Xcode-26%2B-blue?logo=xcode&logoColor=white)
![iOS 26.0+](https://img.shields.io/badge/iOS-26.0%2B-orange?logo=apple&logoColor=white)

A collection of hands-on examples demonstrating new features and APIs introduced in iOS 26, built with SwiftUI. Each example is self-contained and showcases a specific capability or UI enhancement available in the latest iOS release.

<img src=".github/preview.png" alt="Preview" width="50%" />

## Examples

- **[AnimatableView](iOS-26-by-Examples/Views/AnimatableView.swift)**: Demonstrates custom animatable shapes and interactive animation using SwiftUI's new `@Animatable` macro.
- **[BackgroundExtensionEffectView](iOS-26-by-Examples/Views/BackgroundExtensionEffectView.swift)**: Shows how to use the new `.backgroundExtensionEffect()` modifier for immersive backgrounds.
- **[Chart3DView](iOS-26-by-Examples/Views/Chart3DView.swift)**: Explores the new 3D charting capabilities with `Chart3D` and `SurfacePlot`.
- **[GlassEffectContainerView](iOS-26-by-Examples/Views/GlassEffectContainerView.swift)**: Showcases advanced glassmorphism effects and container unions using `GlassEffectContainer` and related APIs.
- **[GlassEffectView](iOS-26-by-Examples/Views/GlassEffectView.swift)**: Demonstrates the new GlassEffect API for creating translucent, glass-like UI elements.
- **[LabelSpacingView](iOS-26-by-Examples/Views/LabelSpacingView.swift)**: Demonstrates new label spacing and icon width customization with `.labelIconToTitleSpacing` and `.labelReservedIconWidth`.
- **[ListSectionIndexLabel](iOS-26-by-Examples/Views/ListSectionIndexLabel.swift)**: Uses `.sectionIndexLabel` and `.listSectionIndexVisibility` for improved list navigation.
- **[NativeWebView](iOS-26-by-Examples/Views/NativeWebView.swift)**: Integrates a native `WebView` with SwiftUI, loading a web page on appear.
- **[NewTabView](iOS-26-by-Examples/Views/NewTabView.swift)**: Presents the enhanced `TabView` with new tab roles, bottom accessories, and minimize behavior.
- **[RichTextEditor](iOS-26-by-Examples/Views/RichTextEditor.swift)**: Utilizes the improved `TextEditor` for rich text editing with attributed strings.
- **[SFSymbolsView](iOS-26-by-Examples/Views/SFSymbolsView.swift)**: Animates and customizes SF Symbols with new symbol effects and variable values.
- **[ToolbarSpacerView](iOS-26-by-Examples/Views/ToolbarSpacerView.swift)**: Demonstrates the new toolbar spacer API for flexible and adaptive toolbar layouts.

## Contributing

Contributions are welcome! If you have an example, improvement, or fix to share, feel free to open a pull request or submit an issue. Please ensure your code follows the style of the existing examples.

## Author

Artem Novichkov, https://artemnovichkov.com

## License

The project is available under the MIT license. See the [LICENSE](./LICENSE) file for more info.

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a SwiftUI application called "Developer Horoscope" that generates personalized horoscopes for developers using Apple's Foundation Models. The app integrates with GitHub to fetch user data and creates witty horoscopes based on zodiac signs and coding activity.

### Key Technologies
- **SwiftUI** - Primary UI framework
- **Foundation Models** - Apple's AI/ML framework for horoscope generation
- **ZodiacKit** - Custom framework for zodiac sign handling
- **AppIntents** - Siri Shortcuts and system integration
- **TipKit** - User onboarding and tips
- **WidgetKit** - Home screen widgets

## Build Commands

### Build Documentation
```bash
./build-docc.sh
```
This script builds DocC documentation and generates static hosting files in the `docs/` directory.

### Xcode Build
The project uses Xcode's standard build system. Build using:
- **Scheme**: "Horoscope" 
- **Target**: iOS/macOS/visionOS
- **Requirements**: Xcode 26.0 beta 4+, iOS 26.0+

## Architecture

### Core Components

1. **HoroscopeService** (`HoroscopeService.swift`)
   - Central service for AI-powered horoscope generation
   - Uses Foundation Models' `LanguageModelSession` with custom tools
   - Supports both streaming and complete result generation
   - Includes prewarming for reduced latency

2. **Tools Architecture** (`Tools/`)
   - **GithubInfoTool**: Fetches GitHub user profile and repository data
   - **UserInfoTool**: Retrieves zodiac sign and gender from Apple Health
   - Tools conform to Foundation Models' `Tool` protocol

3. **Model Layer**
   - **Horoscope** struct: Core data model for generated horoscopes
   - Uses `@Generable` for Foundation Models integration
   - Equatable for SwiftUI state management

4. **Views**
   - **ContentView**: Main app interface with mesh gradient background
   - **HoroscopeView**: Displays generated horoscope results
   - **SettingsView**: User preferences (macOS only)

5. **App Intents Integration**
   - **HoroscopeIntent**: Siri Shortcuts support
   - **HoroscopeShortcutProvider**: Dynamic shortcut management
   - Enables Spotlight search and Action Button integration

### Data Flow
1. User enters GitHub username
2. HoroscopeService creates LanguageModelSession with tools
3. UserInfoTool fetches zodiac/gender from HealthKit
4. GithubInfoTool fetches GitHub profile and repositories
5. Foundation Models generates personalized horoscope
6. Result displays in SwiftUI interface

### Platform-Specific Features
- **iOS**: Bottom toolbar, TipKit integration, sensory feedback
- **macOS**: Settings window, Spotlight integration
- **visionOS**: Adapted navigation and UI

## Testing

No explicit test targets found. Testing likely relies on:
- Xcode's built-in testing for UI components
- Manual testing with real GitHub usernames
- Foundation Models validation through usage

## Dependencies

External frameworks managed through Swift Package Manager:
- ZodiacKit (custom zodiac handling)
- Foundation Models (Apple's AI framework)

## Development Notes

- Dark color scheme enforced app-wide
- Extensive use of `@AppStorage` for username persistence
- Error handling for Foundation Models availability
- Caching implemented in GithubInfoTool for API efficiency
- Documentation built with DocC and hosted statically
```

