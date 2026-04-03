---
id: github.com-ehmo-platform-design-skills-b3f45cf0-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:45.429214
---

# KNOWLEDGE EXTRACT: github.com_ehmo_platform-design-skills_b3f45cf0
> **Extracted on:** 2026-04-01 14:31:55
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007523943/github.com_ehmo_platform-design-skills_b3f45cf0

---

## File: `.gitignore`
```
.DS_Store
node_modules/
*.zip
```

## File: `AGENTS.md`
```markdown
# Platform Design Skills

Agent skills for building and evaluating apps against official platform design guidelines.

Each skill in `skills/` follows the Agent Skills format:
- `SKILL.md` — Full guidelines with YAML frontmatter
- `metadata.json` — Version, references, abstract
- `rules/` — Contains `_sections.md`, a rule index/overview grouping all rules by category with IDs
- `AGENTS.md` — Quick agent context

## Platforms

| Skill | Platform | Source |
|-------|----------|--------|
| `ios` | iPhone | Apple HIG |
| `ipados` | iPad | Apple HIG |
| `macos` | Mac | Apple HIG |
| `watchos` | Apple Watch | Apple HIG |
| `visionos` | Apple Vision Pro | Apple HIG |
| `tvos` | Apple TV | Apple HIG |
| `android` | Android | Material Design 3 |
| `web` | Web | WCAG 2.2 + MDN |
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## v1.1.1 — March 2026

### Summary

Added a focused Human Processor Model pass across the skill pack as a supporting HCI lens, not a new top-level doctrine.

### Added

- Added HPM-informed guidance to the existing sections where it materially improves the rules:
  - iOS: recognition over recall in navigation; immediate waiting-state feedback in patterns
  - iPadOS: preserved visible navigation state; shortcut discoverability over memorization
  - macOS: stable menu command naming/location; lower-interruption feedback for routine actions
  - watchOS: tighter Digital Crown response guidance
  - tvOS: reduced re-orientation cost in focus navigation; lower-effort text-entry guidance
  - visionOS: immediate intent confirmation for eye/hand input; essential controls stay discoverable
  - Android: recognition over recall in navigation; explicit visible waiting states in components
  - Web: field-local instructions; prompt exposure of waiting states

### Documentation

- Updated `README.md` Sources to add the Human Processor Model references used for this pass
- Explicitly documented that HPM is a secondary reference and does not override Apple HIG, Material Design, or WCAG

### Notes

- No standalone HPM section was added to the repo
- Avoided turning HPM into hard numeric rules where the platform source is the real authority

## v1.1.0 — March 2026

### Summary

Comprehensive accuracy and coverage pass across all 8 platform skills. Fixes deprecated and fabricated API references, adds missing accessibility coverage, corrects WCAG citations, and brings rule counts and metadata up to date.

**Total changes:** 1,281 insertions across 33 files. Rule counts grew from ~300 to 450+ total rules.

---

### Bug fixes — incorrect or fabricated APIs

**iOS**
- Fixed `accessibilitySortPriority` code comments: higher values are read *first* by VoiceOver, not last
- Fixed `Rule 3.3`: removed inaccurate "`.bold` dynamic type variants" phrasing; added `@Environment(\.legibilityWeight)` SwiftUI path alongside UIKit `UIFontMetrics` path
- Fixed `Rule 9.6 LocationButton` code example: added missing `import CoreLocationUI` (caused compile error)
- Fixed `Rule 10.1`: interactive widgets with `Button`/`Toggle` + App Intents are supported since iOS 17 (rule incorrectly stated widgets are not interactive)

**iPadOS**
- Fixed `Rule 6.4` Pencil hover: replaced fabricated `override func pencilHoverChanged(_:)` UIKit method (does not exist) with correct `UIHoverGestureRecognizer` pattern
- Fixed `Rule 8.2`: replaced deprecated `UIScreen.didConnectNotification` (deprecated iOS 16) with scene-based `UIWindowScene` APIs
- Fixed `Rule 8.3`: replaced `UIScreen.bounds`/`UIScreen.scale` for external display queries (deprecated in multi-scene context) with `UIWindowScene.coordinateSpace.bounds` and `@Environment(\.displayScale)`
- Fixed screen size table: iPad is 11" (10th gen+), not 10.9"

**macOS**
- Fixed `Rule 1.3`: `CommandGroup(replacing: .toolbar)` was silently removing all built-in toolbar menu items; corrected to `CommandGroup(after: .toolbar)`
- Fixed keyboard quick reference: duplicate `Cmd+0` entry removed (had two conflicting actions assigned)
- Fixed `Rule 11.7`: removed fabricated SwiftUI environment key `\.accessibilityDisplayAdjustments` (does not exist); correct key is `\.colorSchemeContrast`
- Noted `Cmd+Ctrl+S` sidebar toggle is app-defined, not a HIG universal standard

**watchOS**
- Fixed `W-AC-05`/`W-AC-06`: replaced `UIAccessibility.isBoldTextEnabled` and `UIAccessibility.isDarkerSystemColorsEnabled` — UIKit is not available on watchOS; correct approach is `@Environment(\.legibilityWeight)` and `@Environment(\.colorSchemeContrast)`
- Fixed complication family names: replaced deprecated ClockKit names (`circularSmall`, `graphicCorner`, etc.) with current WidgetKit names (`accessoryCircular`, `accessoryCorner`, `accessoryRectangular`, `accessoryInline`)
- Fixed `metadata.json` reference: removed deprecated ClockKit documentation link; replaced with WidgetKit
- Fixed screen dimensions table: separated Series 9 (41mm/45mm) and Series 10 (42mm/46mm) which have different physical dimensions

**tvOS**
- Fixed `SHELF-01`: clarified that `TVTopShelfContentProvider` is current; `TVTopShelfProvider` was deprecated in tvOS 14
- Fixed `FOCUS-04`: replaced `TVMonogramView` parallax reference (it is a user-initials display component, unrelated to parallax) with correct LSR file and `didUpdateFocus` + `UIFocusAnimationCoordinator` approach; `UIMotionEffect` clarified as gyroscope micromotion only, not focus-driven animation
- Fixed parallax description: "device tilt" corrected to "Siri Remote motion" (Apple TV is stationary)
- Fixed `metadata.json`: removed deprecated TVUIKit documentation reference
- Fixed `ACCESS-07`: tvOS supports the "Larger Text" accessibility setting via `UIContentSizeCategory`

**visionOS**
- Fixed code example: `model3D` corrected to `Model3D` (capital M — actual SwiftUI/RealityKit component name)

**Android**
- Fixed `R2.10`/anti-patterns table/`AGENTS.md`: corrected back-navigation guidance — Compose apps use `BackHandler` (not `OnBackInvokedCallback`, which is for View-based apps only)
- Fixed `R6.9` code example: replaced `FontStyle.FontWeightBold` (does not exist — `FontStyle` only has `Normal`/`Italic`) with correct `fontWeightAdjustment >= 700` comparison
- Fixed `_sections.md` cross-reference table: corrected incorrect section pointers (several rows pointed to wrong sections)

**Web**
- Fixed WCAG citation: `SC 2.5.8` for 44px touch targets corrected to `SC 2.5.5` (Enhanced, AAA); SC 2.5.8 only requires 24px at AA
- Fixed `SC 2.3.3` compliance level: annotated as Level AAA, not AA; updated surrounding text to clarify "most rules are AA" rather than "all rules"
- Fixed `SC 2.4.11`/`SC 2.4.12` presentation: 2.4.11 is AA (required); 2.4.12 is AAA (enhanced) — now clearly annotated
- Fixed `Rule 7.6` description: `prefers-contrast: more` (macOS/iOS "Increase Contrast") and `prefers-contrast: forced` (Windows High Contrast Mode) are distinct OS features — clarified in prose

---

### New content

**Accessibility (all platforms)**

All Apple platforms now have a dedicated Accessibility section (CRITICAL impact) with evaluation checklist items:

| Platform | Rules added | Key coverage |
|----------|-------------|--------------|
| iPadOS | 9.1–9.7 | VoiceOver, Dynamic Type, pointer accessibility, Full Keyboard Access, Split View focus, Bold Text, Increase Contrast |
| macOS | 11.1–11.7 | VoiceOver, Full Keyboard Access, Reduce Motion, Bold Text (NSWorkspace), Increase Contrast |
| watchOS | W-AC-01–W-AC-06 | VoiceOver labels, Reduce Motion, accessibilityValue, Bold Text, Increase Contrast (SwiftUI-only APIs) |
| tvOS | ACCESS-01–ACCESS-07 | VoiceOver, Reduce Motion, Bold Text, Increase Contrast, Dynamic Type / Larger Text |
| visionOS | ACC-01–ACC-06 | VoiceOver for 3D objects, pointer/Switch Control, Reduce Motion, Bold Text, Increase Contrast |

**iOS**
- Added Rules 7.9–7.11: SF Symbols usage — rendering modes (monochrome/hierarchical/palette/multicolor), scale and weight matching, `symbolEffect` animations (iOS 17+)

**macOS**
- Added Section 10 (Popovers): 3 rules covering anchoring to source element, Esc dismissal, and sizing to content

**tvOS**
- Added `ACCESS-07`: Larger Text / Dynamic Type via `UIContentSizeCategory` and `UIFontMetrics`
- Added `R2.13`: Predictive back visual animation — interpolate using `BackEventCompat.progress` / `swipeEdge`

**Android**
- Added `R2.13`: Predictive back visual animation guidelines
- Added `R6.13`: `ExploreByTouchHelper` for custom canvas-drawn views (charts, games, custom pickers) — required for TalkBack accessibility on non-widget content
- Added `R6.9` API guidance: `Configuration.fontWeightAdjustment` (API 31+), `AccessibilityManager.isHighTextContrastEnabled()`, Material 3 automatic handling

**Web**
- Added Section 11 (Progressive Web Apps): 5 rules covering `manifest.json` required fields, `theme_color`/`background_color`, service worker registration, installability criteria, and app shortcuts
- Added Rule 7.6: `prefers-contrast` media query — `more` for macOS/iOS Increase Contrast, `forced` for Windows High Contrast Mode
- Added Rule 1.12: WCAG 2.5.3 Label in Name (Level A) — accessible name must contain visible text; `aria-label` must not replace visible text with different text

---

### Documentation and metadata

- Updated all `metadata.json` rule counts to accurate values
- Updated all `metadata.json` category counts after new sections were added
- Updated `README.md`: iOS "50+" → "67+"; total "300+" → "450+"
- Synced all `_sections.md` totals and section maps after every addition
- Updated all evaluation checklists to include newly added sections (Accessibility, Popovers, PWA, SF Symbols)
- Added "Never Do" quick-reference lists to all AGENTS.md files that were missing them (iPadOS, macOS, watchOS, tvOS, visionOS, Android, Web)
- Updated all AGENTS.md Rule Categories tables to include new sections with correct impact levels
- Fixed iPadOS Navigation impact: HIGH → CRITICAL (matches iOS and Android; sidebar navigation is the most foundational iPad HIG requirement)
- Updated `CLAUDE.md`: corrected description of `rules/` directory structure to match what actually exists (`_sections.md` rule index, not individual rule files)
```

## File: `CLAUDE.md`
```markdown
AGENTS.md
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026

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

## File: `README.md`
```markdown
# Platform Design Skills

Platform design skill pack: 450+ rules for Apple HIG, Material Design 3, and WCAG 2.2 across iOS, iPadOS, macOS, watchOS, visionOS, tvOS, Android, and Web.

Built by scraping the [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) (a compiled [PDF version](Apple_HIG.pdf) is included in this repo) and distilling it — along with Material Design 3 and WCAG 2.2 — into succinct but exhaustive skill files. Use them to evaluate, improve, or create your designs.

## Available Skills

### ios

Apple Human Interface Guidelines for iPhone. 67+ rules covering navigation, layout, accessibility, gestures, and iOS-specific components like tab bars, sheets, and Dynamic Island.

**Use when:**
- Building SwiftUI or UIKit interfaces for iPhone
- Reviewing iOS app code for HIG compliance
- Choosing between iOS navigation patterns
- Implementing accessibility, Dark Mode, Dynamic Type

### ipados

Apple HIG for iPad, covering multitasking, pointer support, sidebar navigation, keyboard shortcuts, and Stage Manager. Extends the iOS skill with iPad-specific patterns.

**Use when:**
- Building iPad-optimized interfaces
- Implementing Split View, Slide Over, Stage Manager support
- Adding pointer/trackpad and keyboard shortcut support
- Designing responsive layouts for iPad screen sizes

### macos

Apple HIG for Mac apps. Covers menu bars, window management, toolbars, keyboard-driven interaction, and the expectations of desktop power users.

**Use when:**
- Building macOS apps with SwiftUI or AppKit
- Implementing menu bars, toolbars, and sidebars
- Adding keyboard shortcuts and window management
- Designing for Catalyst or native macOS

### watchos

Apple HIG for Apple Watch. Covers glanceable interfaces, Digital Crown, complications, Always On display, and wrist-optimized interactions.

**Use when:**
- Building watchOS apps or complications
- Designing for small screens and short interactions
- Implementing health/fitness features on Watch

### visionos

Apple HIG for Apple Vision Pro. Covers spatial UI, eye and hand input, windows, volumes, immersive spaces, and ornaments.

**Use when:**
- Building visionOS apps with RealityKit or SwiftUI
- Designing for spatial computing and indirect gestures
- Implementing immersive experiences

### tvos

Apple HIG for Apple TV. Covers focus-based navigation, Siri Remote, Top Shelf, and living room viewing distances.

**Use when:**
- Building tvOS apps
- Implementing focus-based navigation with Siri Remote
- Designing for 10-foot viewing experiences

### android

Google Material Design 3 guidelines for Android. Covers Material You, dynamic color, navigation patterns, components, and Android-specific patterns.

**Use when:**
- Building Android apps with Jetpack Compose or XML layouts
- Reviewing Android code for Material Design compliance
- Implementing Material You and dynamic color
- Choosing between Android navigation patterns

### web

Web platform best practices covering responsive design, accessibility (WCAG), performance, progressive enhancement, and modern CSS/HTML patterns.

**Use when:**
- Building web interfaces with any framework
- Auditing sites for accessibility compliance
- Implementing responsive, performant web layouts
- Reviewing web UI code for best practices

## Installation

```bash
npx skills add ehmo/platform-design-skills
```

## Contributing (Pull Requests)

- Fork the repository and create a feature branch from the default branch.
- Keep PRs focused to one theme (one platform, one major design area, or one format rule set).
- Update affected skill docs in `skills/<platform>/SKILL.md` and keep `metadata.json` entries aligned when behavior changes.
- If adding or changing rule coverage, ensure:
  - platform skill descriptions remain accurate,
  - source signals in the skill files are still correct,
  - and examples still reflect current platform behavior.
- In the PR description include:
  - what changed,
  - why this matters for AI output quality,
  - and a short before/after usage sample.
- Suggested PR title format: `feat: ...`, `fix: ...`, `docs: ...`.

Example PR checklist:

- [ ] Scope matches the PR title
- [ ] One platform or one rule family per PR
- [ ] No broken relative links in touched files
- [ ] AGENTS/skill assumptions still stated clearly
- [ ] README and skill metadata remain consistent

## Usage

Skills activate automatically when agents detect platform-relevant tasks.

```
Review this SwiftUI view for iOS HIG compliance
```
```
Check this Android Compose screen against Material Design
```
```
Audit this web page for accessibility
```

## Skill Structure

Each skill contains:
- `SKILL.md` — Agent instructions with frontmatter metadata
- `metadata.json` — Version, references, and abstract
- `rules/` — Individual rule files with examples
- `AGENTS.md` — Quick context for agent consumption

## Sources

### Platform-normative sources

- Apple Human Interface Guidelines (2025) — developer.apple.com/design/human-interface-guidelines
- Material Design 3 — m3.material.io
- Web Content Accessibility Guidelines (WCAG) 2.2 — w3.org/WAI/WCAG22/quickref
- MDN Web Docs — developer.mozilla.org

### Supporting HCI references

These are secondary references used to sharpen guidance around recognition over recall, visible waiting states, and input effort. They do not override Apple HIG, Material, or WCAG.

- Stuart K. Card, Thomas P. Moran, and Allen Newell, *The Psychology of Human-Computer Interaction* (1983) — https://archive.org/details/psychologyofhuma0000card
- Allen Newell and Stuart K. Card, *Prospects for Psychological Science in Human-Computer Interaction* (includes Model Human Processor summary and operating principles) — https://iiif.library.cmu.edu/file/Newell_box00042_fld03533_doc0001/Newell_box00042_fld03533_doc0001.pdf
- Tiffany Jastrzembski and Neil Charness, *The Model Human Processor and the Older Adult: Parameter Estimation and Validation Within a Mobile Phone Task* (2007 / PMC) — https://pmc.ncbi.nlm.nih.gov/articles/PMC4591021/
- Human Processor Model overview (discovery/reference pointer) — https://en.wikipedia.org/wiki/Human_processor_model

## License

MIT
```

## File: `skills/android/AGENTS.md`
```markdown
# Android Design Skill

Material Design 3 guidelines and Android platform conventions for Jetpack Compose and XML layouts.

## Structure

- `SKILL.md` — Full guideline rules with code examples
- `rules/_sections.md` — Indexed section breakdown for quick lookup
- `metadata.json` — Version and reference metadata

## Usage

Apply these guidelines when:
- Building or reviewing Android UI code
- Implementing Material You / dynamic color
- Designing navigation, layout, or component architecture
- Auditing accessibility or platform compliance

## Priority

Rules marked **CRITICAL** must never be violated. Rules marked **HIGH** should be followed unless there is a documented reason. Rules marked **MEDIUM** are recommended best practices.

## Never Do

- Never hardcode color hex values — always use `MaterialTheme.colorScheme` color roles
- Never use `dp` for text sizes — use `sp` so user font scaling applies
- Never override `onBackPressed()` — use `BackHandler` (Compose) or `OnBackInvokedCallback` (View-based) for predictive back
- Never place touch targets below 48x48dp — accessibility violation
- Never request permissions at app launch — request in context with a rationale
- Never use pure black (#000000) for dark theme backgrounds — use Material surface roles
- Never put icon-only items in the navigation bar — labels are required
- Never use a dialog for non-critical information — prefer Snackbar or Bottom Sheet
- Never use more than one FAB on a screen — one FAB for the single primary action
- Never show full-width content on tablet layouts — use list-detail or max-width containers
```

## File: `skills/android/SKILL.md`
```markdown
---
name: android-design-guidelines
description: Material Design 3 and Android platform guidelines. Use when building Android apps with Jetpack Compose or XML layouts, implementing Material You, navigation, or accessibility. Triggers on tasks involving Android UI, Compose components, dynamic color, or Material Design compliance.
license: MIT
metadata:
  author: platform-design-skills
  version: "1.0.0"
---

# Android Platform Design Guidelines — Material Design 3

## 1. Material You & Theming [CRITICAL]

### 1.1 Dynamic Color

Enable dynamic color derived from the user's wallpaper. Dynamic color is the default on Android 12+ and should be the primary theming strategy.

```kotlin
// Compose: Dynamic color theme
@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = true,
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
            val context = LocalContext.current
            if (darkTheme) dynamicDarkColorScheme(context)
            else dynamicLightColorScheme(context)
        }
        darkTheme -> darkColorScheme()
        else -> lightColorScheme()
    }
    MaterialTheme(
        colorScheme = colorScheme,
        typography = AppTypography,
        content = content
    )
}
```

```xml
<!-- XML: Dynamic color in themes.xml -->
<style name="Theme.App" parent="Theme.Material3.DayNight.NoActionBar">
    <item name="dynamicColorThemeOverlay">@style/ThemeOverlay.Material3.DynamicColors.DayNight</item>
</style>
```

**Rules:**
- R1.1: Always provide a fallback static color scheme for devices below Android 12.
- R1.2: Never hardcode color hex values in components. Always reference color roles from the theme.
- R1.3: Test with at least 3 different wallpapers to verify dynamic color harmony.

### 1.2 Color Roles

Material 3 defines a structured set of color roles. Use them semantically, not aesthetically.

| Role | Usage | On-Role |
|------|-------|---------|
| `primary` | Key actions, active states, FAB | `onPrimary` |
| `primaryContainer` | Less prominent primary elements | `onPrimaryContainer` |
| `secondary` | Supporting UI, filter chips | `onSecondary` |
| `secondaryContainer` | Navigation bar active indicator | `onSecondaryContainer` |
| `tertiary` | Accent, contrast, complementary | `onTertiary` |
| `tertiaryContainer` | Input fields, less prominent accents | `onTertiaryContainer` |
| `surface` | Backgrounds, cards, sheets | `onSurface` |
| `surfaceVariant` | Decorative elements, dividers | `onSurfaceVariant` |
| `error` | Error states, destructive actions | `onError` |
| `errorContainer` | Error backgrounds | `onErrorContainer` |
| `outline` | Borders, dividers | — |
| `outlineVariant` | Subtle borders | — |
| `inverseSurface` | Snackbar background | `inverseOnSurface` |

```kotlin
// Correct: semantic color roles
Text(
    text = "Error message",
    color = MaterialTheme.colorScheme.error
)
Surface(color = MaterialTheme.colorScheme.errorContainer) {
    Text(text = "Error detail", color = MaterialTheme.colorScheme.onErrorContainer)
}

// WRONG: hardcoded colors
Text(text = "Error", color = Color(0xFFB00020)) // Anti-pattern
```

**Rules:**
- R1.4: Every foreground element must use the matching `on` color role for its background (e.g., `onPrimary` text on `primary` background).
- R1.5: Use `surface` and its variants for backgrounds. Never use `primary` or `secondary` as large background areas.
- R1.6: Use `tertiary` sparingly for accent and complementary contrast only.

### 1.3 Light and Dark Themes

Support both light and dark themes. Respect the system setting by default.

```kotlin
// Compose: Detect system theme
val darkTheme = isSystemInDarkTheme()
```

**Rules:**
- R1.7: Always support both light and dark themes. Never ship light-only.
- R1.8: Dark theme surfaces use elevation-based tonal mapping, not pure black (#000000). Use `surface` color roles which handle this automatically.
- R1.9: Provide a manual theme override in app settings (System / Light / Dark).

### 1.4 Custom Color Seeds

When branding requires custom colors, provide a seed color and generate tonal palettes using Material Theme Builder.

```kotlin
// Custom color scheme with brand seed
private val BrandLightColorScheme = lightColorScheme(
    primary = Color(0xFF1B6D2F),
    onPrimary = Color(0xFFFFFFFF),
    primaryContainer = Color(0xFFA4F6A8),
    onPrimaryContainer = Color(0xFF002107),
    // ... generate full palette from seed
)
```

**Rules:**
- R1.10: Generate tonal palettes from seed colors using Material Theme Builder. Never manually pick individual tones.
- R1.11: When using custom colors, still support dynamic color as the default and use custom colors as fallback.

---

## 2. Navigation [CRITICAL]

### 2.1 Navigation Bar (Bottom)

The primary navigation pattern for phones with 3-5 top-level destinations.

```kotlin
// Compose: Navigation Bar
NavigationBar {
    items.forEachIndexed { index, item ->
        NavigationBarItem(
            icon = {
                Icon(
                    imageVector = if (selectedItem == index) item.filledIcon else item.outlinedIcon,
                    contentDescription = item.label
                )
            },
            label = { Text(item.label) },
            selected = selectedItem == index,
            onClick = { selectedItem = index }
        )
    }
}
```

**Rules:**
- R2.1: Use Navigation Bar for 3-5 top-level destinations on compact screens. Never use for fewer than 3 or more than 5.
- R2.2: Always show labels on navigation bar items. Icon-only navigation bars are not permitted.
- R2.3: Use filled icons for the selected state and outlined icons for unselected states.
- R2.4: The active indicator uses `secondaryContainer` color. Do not override this.

### 2.2 Navigation Rail

For medium and expanded screens (tablets, foldables, desktop).

```kotlin
// Compose: Navigation Rail for larger screens
NavigationRail(
    header = {
        FloatingActionButton(
            onClick = { /* primary action */ },
            containerColor = MaterialTheme.colorScheme.tertiaryContainer
        ) {
            Icon(Icons.Default.Add, contentDescription = "Create")
        }
    }
) {
    items.forEachIndexed { index, item ->
        NavigationRailItem(
            icon = { Icon(item.icon, contentDescription = item.label) },
            label = { Text(item.label) },
            selected = selectedItem == index,
            onClick = { selectedItem = index }
        )
    }
}
```

**Rules:**
- R2.5: Use Navigation Rail on medium (600-839dp) and expanded (840dp+) window sizes. Pair it with Navigation Bar on compact.
- R2.6: Optionally include a FAB in the rail header for the primary action.
- R2.7: Labels are optional on the rail but recommended for clarity.

### 2.3 Navigation Drawer

For 5+ destinations or complex navigation hierarchies, typically on expanded screens.

```kotlin
// Compose: Permanent Navigation Drawer for large screens
PermanentNavigationDrawer(
    drawerContent = {
        PermanentDrawerSheet {
            Text("App Name", modifier = Modifier.padding(16.dp),
                 style = MaterialTheme.typography.titleMedium)
            HorizontalDivider()
            items.forEach { item ->
                NavigationDrawerItem(
                    label = { Text(item.label) },
                    selected = item == selectedItem,
                    onClick = { selectedItem = item },
                    icon = { Icon(item.icon, contentDescription = null) }
                )
            }
        }
    }
) {
    Scaffold { /* page content */ }
}
```

**Rules:**
- R2.8: Use modal drawer on compact screens, permanent drawer on expanded screens.
- R2.9: Group drawer items into sections with dividers and section headers.

### 2.4 Predictive Back Gesture

Android 13+ supports predictive back with an animation preview.

```kotlin
// Compose: Predictive back with BackHandler (androidx.activity.compose)
BackHandler(enabled = true) {
    // Called when back is confirmed; navigate back in your nav controller
    navController.popBackStack()
}
```

```kotlin
// Compose: Predictive back progress animation using predictiveBackHandler modifier
// (androidx.activity:activity-compose 1.8+)
Modifier.predictiveBackHandler(enabled = true) { progress ->
    // progress is a Flow<BackEventCompat> with x, y, swipeEdge, progress (0.0–1.0)
    progress.collect { backEvent ->
        animationState = backEvent.progress
    }
}
```

```xml
<!-- AndroidManifest.xml: opt in to predictive back -->
<application android:enableOnBackInvokedCallback="true">
```

**Rules:**
- R2.10: Opt in to predictive back in the manifest. In **Compose** apps, use `BackHandler` (from `androidx.activity.compose`) to intercept back events. In **View-based** apps, implement `OnBackInvokedCallback` (API 33+) or `OnBackPressedCallback` (AndroidX) instead of overriding `onBackPressed()`.
- R2.11: The system back gesture navigates back in the navigation stack. The Up button (toolbar arrow) navigates up in the app hierarchy. These may differ.
- R2.12: Never intercept system back to show "are you sure?" dialogs unless there is unsaved user input.
- R2.13: Do not suppress the system-provided back preview animation. If you implement custom enter/exit transitions, interpolate them using `BackEventCompat.progress` (0.0–1.0) and respect `BackEventCompat.swipeEdge` (`EDGE_LEFT`/`EDGE_RIGHT`) so the exiting screen scales down and shifts toward the initiating edge, matching the system animation.
- R2.14: Prefer recognition over recall. Keep destinations labeled, selected state visible, and back-stack context preserved so users do not reconstruct where they are after every navigation step.

```kotlin
// Compose: drive a custom animation from predictive back progress
Modifier.predictiveBackHandler(enabled = true) { progress ->
    progress.collect { backEvent ->
        // backEvent.progress: 0.0 (gesture start) → 1.0 (committed)
        // backEvent.swipeEdge: BackEventCompat.EDGE_LEFT or EDGE_RIGHT
        exitScale = 1f - (backEvent.progress * 0.1f)
        exitOffsetX = if (backEvent.swipeEdge == BackEventCompat.EDGE_LEFT) -backEvent.progress * 32.dp.toPx() else backEvent.progress * 32.dp.toPx()
    }
}
```

### 2.5 Navigation Component Selection

| Screen Size | 3-5 Destinations | 5+ Destinations |
|-------------|-------------------|-----------------|
| Compact (< 600dp) | Navigation Bar | Modal Drawer + Navigation Bar |
| Medium (600-839dp) | Navigation Rail | Modal Drawer + Navigation Rail |
| Expanded (840dp+) | Navigation Rail | Permanent Drawer |

---

## 3. Layout & Responsive [HIGH]

### 3.1 Window Size Classes

Use window size classes for adaptive layouts, not raw pixel breakpoints.

```kotlin
// Compose: Window size classes
val windowSizeClass = calculateWindowSizeClass(this)
when (windowSizeClass.widthSizeClass) {
    WindowWidthSizeClass.Compact -> CompactLayout()
    WindowWidthSizeClass.Medium -> MediumLayout()
    WindowWidthSizeClass.Expanded -> ExpandedLayout()
}
```

| Class | Width | Typical Device | Columns |
|-------|-------|----------------|---------|
| Compact | < 600dp | Phone portrait | 4 |
| Medium | 600-839dp | Tablet portrait, foldable | 8 |
| Expanded | 840dp+ | Tablet landscape, desktop | 12 |

**Rules:**
- R3.1: Always use `WindowSizeClass` from `material3-window-size-class` for responsive layout decisions.
- R3.2: Never use fixed pixel breakpoints. Device categories are fluid.
- R3.3: Support all three width size classes. At minimum, compact and expanded.

### 3.2 Material Grid

Apply canonical Material grid margins and gutters.

| Size Class | Margins | Gutters | Columns |
|------------|---------|---------|---------|
| Compact | 16dp | 8dp | 4 |
| Medium | 24dp | 16dp | 8 |
| Expanded | 24dp | 24dp | 12 |

**Rules:**
- R3.4: Content should not span the full width on expanded screens. Use a max content width of ~840dp or list-detail layout.
- R3.5: Apply consistent horizontal margins matching the grid spec.

### 3.3 Edge-to-Edge Display

Android 15+ enforces edge-to-edge. All apps should draw behind system bars.

```kotlin
// Compose: Edge-to-edge setup
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge()
        super.onCreate(savedInstanceState)
        setContent {
            Scaffold(
                modifier = Modifier.fillMaxSize(),
                // Scaffold handles insets for top/bottom bars automatically
            ) { innerPadding ->
                Content(modifier = Modifier.padding(innerPadding))
            }
        }
    }
}
```

**Rules:**
- R3.6: Call `enableEdgeToEdge()` before `setContent`. Draw behind both status bar and navigation bar.
- R3.7: Use `WindowInsets` to pad content away from system bars. `Scaffold` handles this for top bar and bottom bar content automatically.
- R3.8: Scrollable content should scroll behind transparent system bars with appropriate inset padding at the top and bottom of the list.

### 3.4 Foldable Device Support

```kotlin
// Compose: Detect fold posture
val foldingFeatures = WindowInfoTracker.getOrCreate(context)
    .windowLayoutInfo(context)
    .collectAsState(initial = WindowLayoutInfo(emptyList()))
```

**Rules:**
- R3.9: Detect hinge/fold position and avoid placing critical content across the fold.
- R3.10: Use `ListDetailPaneScaffold` or `SupportingPaneScaffold` from Material3 adaptive library for foldable-aware layouts.

---

## 4. Typography [HIGH]

### 4.1 Material Type Scale

| Role | Default Size | Default Weight | Usage |
|------|-------------|----------------|-------|
| displayLarge | 57sp | 400 | Hero text, onboarding |
| displayMedium | 45sp | 400 | Large feature text |
| displaySmall | 36sp | 400 | Prominent display |
| headlineLarge | 32sp | 400 | Screen titles |
| headlineMedium | 28sp | 400 | Section headers |
| headlineSmall | 24sp | 400 | Card titles |
| titleLarge | 22sp | 400 | Top app bar title |
| titleMedium | 16sp | 500 | Tabs, navigation |
| titleSmall | 14sp | 500 | Subtitles |
| bodyLarge | 16sp | 400 | Primary body text |
| bodyMedium | 14sp | 400 | Secondary body text |
| bodySmall | 12sp | 400 | Captions |
| labelLarge | 14sp | 500 | Buttons, prominent labels |
| labelMedium | 12sp | 500 | Chips, smaller labels |
| labelSmall | 11sp | 500 | Timestamps, annotations |

```kotlin
// Compose: Custom typography
val AppTypography = Typography(
    displayLarge = TextStyle(
        fontFamily = FontFamily(Font(R.font.brand_regular)),
        fontWeight = FontWeight.Normal,
        fontSize = 57.sp,
        lineHeight = 64.sp,
        letterSpacing = (-0.25).sp
    ),
    bodyLarge = TextStyle(
        fontFamily = FontFamily(Font(R.font.brand_regular)),
        fontWeight = FontWeight.Normal,
        fontSize = 16.sp,
        lineHeight = 24.sp,
        letterSpacing = 0.5.sp
    )
    // ... define all 15 roles
)
```

**Rules:**
- R4.1: Always use `sp` units for text sizes to support user font scaling preferences.
- R4.2: Never set text below 12sp for body content. Labels may go to 11sp minimum.
- R4.3: Reference typography roles from `MaterialTheme.typography`, not hardcoded sizes.
- R4.4: Support dynamic type scaling. Test at 200% font scale. Ensure no text is clipped or overlapping.
- R4.5: Line height should be approximately 1.2-1.5x the font size for readability.

---

## 5. Components [HIGH]

### 5.1 Floating Action Button (FAB)

The FAB represents the single most important action on a screen.

```kotlin
// Compose: FAB variants
// Standard FAB
FloatingActionButton(onClick = { /* action */ }) {
    Icon(Icons.Default.Add, contentDescription = "Create new item")
}

// Extended FAB (with label - preferred for clarity)
ExtendedFloatingActionButton(
    onClick = { /* action */ },
    icon = { Icon(Icons.Default.Edit, contentDescription = null) },
    text = { Text("Compose") }
)

// Large FAB
LargeFloatingActionButton(onClick = { /* action */ }) {
    Icon(Icons.Default.Add, contentDescription = "Create", modifier = Modifier.size(36.dp))
}
```

**Rules:**
- R5.1: Use at most one FAB per screen. It represents the primary action.
- R5.2: Place the FAB at the bottom-end of the screen. On screens with a Navigation Bar, the FAB floats above it.
- R5.3: The FAB should use `primaryContainer` color by default. Use `tertiaryContainer` for secondary screens.
- R5.4: Prefer `ExtendedFloatingActionButton` with a label for clarity. Collapse to icon-only on scroll if needed.

### 5.2 Top App Bar

```kotlin
// Compose: Top app bar variants
// Small (default)
TopAppBar(
    title = { Text("Page Title") },
    navigationIcon = {
        IconButton(onClick = { /* navigate up */ }) {
            Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Back")
        }
    },
    actions = {
        IconButton(onClick = { /* search */ }) {
            Icon(Icons.Default.Search, contentDescription = "Search")
        }
    }
)

// Medium — expands title area
MediumTopAppBar(
    title = { Text("Section Title") },
    scrollBehavior = TopAppBarDefaults.enterAlwaysScrollBehavior()
)

// Large — for prominent titles
LargeTopAppBar(
    title = { Text("Screen Title") },
    scrollBehavior = TopAppBarDefaults.exitUntilCollapsedScrollBehavior()
)
```

**Rules:**
- R5.5: Use `TopAppBar` (small) for most screens. Use `MediumTopAppBar` or `LargeTopAppBar` for prominent section or screen titles.
- R5.6: Connect scroll behavior to the app bar so it collapses/expands with content scrolling.
- R5.7: Limit action icons to 2-3. Overflow additional actions into a more menu.

### 5.3 Bottom Sheets

```kotlin
// Compose: Modal bottom sheet
ModalBottomSheet(
    onDismissRequest = { showSheet = false },
    sheetState = rememberModalBottomSheetState()
) {
    Column(modifier = Modifier.padding(16.dp)) {
        Text("Sheet Title", style = MaterialTheme.typography.titleLarge)
        Spacer(modifier = Modifier.height(16.dp))
        // Sheet content
    }
}
```

**Rules:**
- R5.8: Use modal bottom sheets for non-critical supplementary content. Use standard bottom sheets for persistent content.
- R5.9: Bottom sheets must have a visible drag handle for discoverability.
- R5.10: Sheet content must be scrollable if it can exceed the visible area.

### 5.4 Dialogs

```kotlin
// Compose: Alert dialog
AlertDialog(
    onDismissRequest = { showDialog = false },
    title = { Text("Discard draft?") },
    text = { Text("Your unsaved changes will be lost.") },
    confirmButton = {
        TextButton(onClick = { /* confirm */ }) { Text("Discard") }
    },
    dismissButton = {
        TextButton(onClick = { showDialog = false }) { Text("Cancel") }
    }
)
```

**Rules:**
- R5.11: Dialogs interrupt the user. Use them only for critical decisions requiring immediate attention.
- R5.12: Confirm button uses a text button, not a filled button. The dismiss button is always on the left.
- R5.13: Dialog titles should be concise questions or statements. Body text provides context.

### 5.5 Snackbar

```kotlin
// Compose: Snackbar with action
val snackbarHostState = remember { SnackbarHostState() }
Scaffold(snackbarHost = { SnackbarHost(snackbarHostState) }) {
    // trigger snackbar
    LaunchedEffect(key) {
        val result = snackbarHostState.showSnackbar(
            message = "Item archived",
            actionLabel = "Undo",
            duration = SnackbarDuration.Short
        )
        if (result == SnackbarResult.ActionPerformed) { /* undo */ }
    }
}
```

**Rules:**
- R5.14: Use snackbars for brief, non-critical feedback. They auto-dismiss and should not contain critical information.
- R5.15: Snackbars appear at the bottom of the screen, above the Navigation Bar and below the FAB.
- R5.16: Include an action (e.g., "Undo") when the operation is reversible. Limit to one action.

### 5.6 Chips

```kotlin
// Filter Chip
FilterChip(
    selected = isSelected,
    onClick = { isSelected = !isSelected },
    label = { Text("Filter") },
    leadingIcon = if (isSelected) {
        { Icon(Icons.Default.Check, contentDescription = null, modifier = Modifier.size(18.dp)) }
    } else null
)

// Assist Chip
AssistChip(
    onClick = { /* action */ },
    label = { Text("Add to calendar") },
    leadingIcon = { Icon(Icons.Default.CalendarToday, contentDescription = null) }
)
```

**Rules:**
- R5.17: Use `FilterChip` for toggling filters, `AssistChip` for smart suggestions, `InputChip` for user-entered content (tags), `SuggestionChip` for dynamically generated suggestions.
- R5.18: Chips should be arranged in a horizontally scrollable row or a flow layout, not stacked vertically.
- R5.19: Expose waiting states immediately. If an action cannot finish right away, acknowledge it with inline state change, progress, or another visible response rather than leaving the UI static.

### 5.7 Component Selection Guide

| Need | Component |
|------|-----------|
| Primary screen action | FAB |
| Brief feedback | Snackbar |
| Critical decision | Dialog |
| Supplementary content | Bottom Sheet |
| Toggle filter | Filter Chip |
| User-entered tag | Input Chip |
| Smart suggestion | Assist Chip |
| Content group | Card |
| Vertical list of items | LazyColumn with ListItem |
| Segmented option (2-5) | SegmentedButton |
| Binary toggle | Switch |
| Selection from list | Radio buttons or exposed dropdown menu |

---

## 6. Accessibility [CRITICAL]

### 6.1 TalkBack and Content Descriptions

```kotlin
// Compose: Accessible components
Icon(
    Icons.Default.Favorite,
    contentDescription = "Add to favorites" // Descriptive, not "heart icon"
)

// Decorative elements
Icon(
    Icons.Default.Star,
    contentDescription = null // null for purely decorative
)

// Merge semantics for compound elements
Row(modifier = Modifier.semantics(mergeDescendants = true) {}) {
    Icon(Icons.Default.Event, contentDescription = null)
    Text("March 15, 2026")
}

// Custom actions
Box(modifier = Modifier.semantics {
    customActions = listOf(
        CustomAccessibilityAction("Archive") { /* archive */ true },
        CustomAccessibilityAction("Delete") { /* delete */ true }
    )
})
```

**Rules:**
- R6.1: Every interactive element must have a `contentDescription` (or `null` if purely decorative).
- R6.2: Content descriptions must describe the action or meaning, not the visual appearance. Say "Add to favorites" not "Heart icon."
- R6.3: Use `mergeDescendants = true` to group related elements into a single TalkBack focus unit (e.g., a list item with icon + text + subtitle).
- R6.4: Provide `customActions` for swipe-to-dismiss or long-press actions so TalkBack users can access them.

### 6.2 Touch Targets

```kotlin
// Compose: Ensure minimum touch target
IconButton(onClick = { /* action */ }) {
    // IconButton already provides 48dp minimum touch target
    Icon(Icons.Default.Close, contentDescription = "Close")
}

// Manual minimum touch target
Box(
    modifier = Modifier
        .sizeIn(minWidth = 48.dp, minHeight = 48.dp)
        .clickable { /* action */ },
    contentAlignment = Alignment.Center
) {
    Icon(Icons.Default.Info, contentDescription = "Info", modifier = Modifier.size(24.dp))
}
```

**Rules:**
- R6.5: All interactive elements must have a minimum touch target of 48x48dp. Material 3 components handle this by default.
- R6.6: Do not reduce touch targets to save space. Use padding to increase the touchable area if the visual element is smaller.

### 6.3 Color Contrast and Visual

**Rules:**
- R6.7: Text contrast ratio must be at least 4.5:1 for normal text and 3:1 for large text (18sp+ or 14sp+ bold) against its background.
- R6.8: Never use color as the only means of conveying information. Pair with icons, text, or patterns.
- R6.9: Support bold text and high contrast accessibility settings. Use `Configuration.fontWeightAdjustment` (API 31+) to detect the user's bold text preference and scale custom font weights accordingly. Use `AccessibilityManager.isHighTextContrastEnabled()` to detect high contrast mode and substitute higher-contrast color values. Material 3 components handle both automatically; custom text rendering and color usage must opt in explicitly.

```kotlin
// Detect bold text preference (API 31+)
val fontWeightAdjustment = resources.configuration.fontWeightAdjustment
val isBoldText = fontWeightAdjustment >= 700 // equivalent to FontWeight.Bold.weight

// Detect high contrast mode
val am = getSystemService(Context.ACCESSIBILITY_SERVICE) as AccessibilityManager
val isHighContrast = am.isHighTextContrastEnabled

// Compose: use MaterialTheme.typography which respects fontWeightAdjustment automatically
Text(
    text = "Label",
    style = MaterialTheme.typography.bodyLarge // Adapts to fontWeightAdjustment
)

// For custom colors: provide high-contrast alternative
val labelColor = if (isHighContrast) {
    MaterialTheme.colorScheme.onSurface  // Strong contrast
} else {
    MaterialTheme.colorScheme.onSurfaceVariant  // Normal contrast
}
```

### 6.4 Focus and Traversal

```kotlin
// Compose: Custom focus order
Column {
    var focusRequester = remember { FocusRequester() }
    TextField(
        modifier = Modifier.focusRequester(focusRequester),
        value = text,
        onValueChange = { text = it }
    )
    LaunchedEffect(Unit) {
        focusRequester.requestFocus() // Auto-focus on screen load
    }
}
```

**Rules:**
- R6.10: Focus order must follow a logical reading sequence (top-to-bottom, start-to-end). Avoid custom `focusOrder` unless the default is incorrect.
- R6.11: After navigation or dialog dismissal, move focus to the most logical target element.
- R6.12: All screens must be fully operable using TalkBack, Switch Access, and external keyboard.

### 6.5 Custom Canvas Views

Custom `View` subclasses that draw content on a Canvas (charts, custom pickers, drawing surfaces) are invisible to TalkBack by default because they have no child views. Use `ExploreByTouchHelper` from `androidx.customview.widget` to define a virtual accessibility tree.

- R6.13: Custom canvas-drawn views must use `ExploreByTouchHelper` to expose a virtual accessibility tree to TalkBack. Override `getVirtualViewAt()` to map touch coordinates to virtual view IDs, and `onPopulateNodeForVirtualView()` to supply text, bounds, and actions for each virtual node.

```kotlin
import androidx.customview.widget.ExploreByTouchHelper

class PieChartView(context: Context) : View(context) {

    private val helper = object : ExploreByTouchHelper(this) {
        override fun getVirtualViewAt(x: Float, y: Float): Int {
            // Return virtual view ID for the slice at (x, y), or INVALID_ID
            return sliceIndexAt(x, y)
        }

        override fun getVisibleVirtualViews(virtualViewIds: MutableList<Int>) {
            slices.indices.forEach { virtualViewIds.add(it) }
        }

        override fun onPopulateNodeForVirtualView(
            virtualViewId: Int,
            node: AccessibilityNodeInfoCompat
        ) {
            val slice = slices[virtualViewId]
            node.text = "${slice.label}: ${slice.percentage}%"
            node.setBoundsInParent(slice.bounds)
            node.addAction(AccessibilityNodeInfoCompat.ACTION_CLICK)
        }

        override fun onPerformActionForVirtualView(
            virtualViewId: Int, action: Int, arguments: Bundle?
        ): Boolean {
            if (action == AccessibilityNodeInfoCompat.ACTION_CLICK) {
                onSliceSelected(virtualViewId)
                return true
            }
            return false
        }
    }

    init {
        ViewCompat.setAccessibilityDelegate(this, helper)
    }

    override fun dispatchHoverEvent(event: MotionEvent) =
        helper.dispatchHoverEvent(event) || super.dispatchHoverEvent(event)
}
```

---

## 7. Gestures & Input [MEDIUM]

### 7.1 System Gestures

**Rules:**
- R7.1: Never place interactive elements within the system gesture inset zones (bottom 20dp, left/right 24dp edges) as they conflict with system navigation gestures.
- R7.2: Use `WindowInsets.systemGestures` to detect and avoid gesture conflict zones.

### 7.2 Common Gesture Patterns

```kotlin
// Compose: Pull to refresh
PullToRefreshBox(
    isRefreshing = isRefreshing,
    onRefresh = { viewModel.refresh() }
) {
    LazyColumn { /* content */ }
}

// Compose: Swipe to dismiss
SwipeToDismissBox(
    state = rememberSwipeToDismissBoxState(),
    backgroundContent = {
        Box(
            modifier = Modifier.fillMaxSize().background(MaterialTheme.colorScheme.error),
            contentAlignment = Alignment.CenterEnd
        ) {
            Icon(Icons.Default.Delete, contentDescription = "Delete",
                 tint = MaterialTheme.colorScheme.onError)
        }
    }
) {
    ListItem(headlineContent = { Text("Swipeable item") })
}
```

**Rules:**
- R7.3: All swipe-to-dismiss actions must be undoable (show snackbar with undo) or require confirmation.
- R7.4: Provide alternative non-gesture ways to trigger all gesture-based actions (for accessibility).
- R7.5: Apply Material ripple effect on all tappable elements. Compose `clickable` modifier includes ripple by default.

### 7.3 Long Press

**Rules:**
- R7.6: Use long press for contextual menus and multi-select mode. Never use it as the only way to access a feature.
- R7.7: Provide haptic feedback on long press via `HapticFeedbackType.LongPress`.

---

## 8. Notifications [MEDIUM]

### 8.1 Notification Channels

```kotlin
// Create notification channel (required for Android 8+)
val channel = NotificationChannel(
    "messages",
    "Messages",
    NotificationManager.IMPORTANCE_HIGH
).apply {
    description = "New message notifications"
    enableLights(true)
    lightColor = Color.BLUE
}
notificationManager.createNotificationChannel(channel)
```

| Importance | Behavior | Use For |
|-----------|----------|---------|
| IMPORTANCE_HIGH | Sound + heads-up | Messages, calls |
| IMPORTANCE_DEFAULT | Sound | Social updates, emails |
| IMPORTANCE_LOW | No sound | Recommendations |
| IMPORTANCE_MIN | Silent, no status bar | Weather, ongoing |

**Rules:**
- R8.1: Create separate notification channels for each distinct notification type. Users can configure each independently.
- R8.2: Choose importance levels conservatively. Overusing `IMPORTANCE_HIGH` leads users to disable notifications entirely.
- R8.3: All notifications must have a tap action (PendingIntent) that navigates to relevant content.
- R8.4: Include a `contentDescription` in notification icons for accessibility.

### 8.2 Notification Design

**Rules:**
- R8.5: Use `MessagingStyle` for conversations. Include sender name and avatar.
- R8.6: Add direct reply actions to messaging notifications.
- R8.7: Provide a "Mark as read" action on message notifications.
- R8.8: Use expandable notifications (`BigTextStyle`, `BigPictureStyle`, `InboxStyle`) for rich content.
- R8.9: Foreground service notifications must accurately describe the ongoing operation and provide a stop action where appropriate.

---

## 9. Permissions & Privacy [HIGH]

### 9.1 Runtime Permissions

```kotlin
// Compose: Permission request
val permissionState = rememberPermissionState(Manifest.permission.CAMERA)

if (permissionState.status.isGranted) {
    CameraPreview()
} else {
    Column {
        Text("Camera access is needed to scan QR codes.")
        Button(onClick = { permissionState.launchPermissionRequest() }) {
            Text("Grant Camera Access")
        }
    }
}
```

**Rules:**
- R9.1: Request permissions in context, at the moment they are needed, not at app launch.
- R9.2: Always explain why the permission is needed before requesting it (rationale screen).
- R9.3: Gracefully handle permission denial. Provide degraded functionality rather than blocking the user.
- R9.4: Never request permissions you do not actively use. Google Play will reject apps with unnecessary permissions.

### 9.2 Privacy-Preserving APIs

```kotlin
// Photo picker: no permission needed
val pickMedia = rememberLauncherForActivityResult(
    ActivityResultContracts.PickVisualMedia()
) { uri ->
    uri?.let { /* handle selected media */ }
}
pickMedia.launch(PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))
```

**Rules:**
- R9.5: Use the Photo Picker (Android 13+) instead of requesting `READ_MEDIA_IMAGES`. No permission needed.
- R9.6: Use `ACCESS_COARSE_LOCATION` (approximate) unless precise location is essential for functionality.
- R9.7: Prefer one-time permissions for camera and microphone in non-recording contexts.
- R9.8: Display a privacy indicator when camera or microphone is actively in use.

---

## 10. System Integration [MEDIUM]

### 10.1 Widgets

```kotlin
// Compose Glance API widget
class TaskWidget : GlanceAppWidget() {
    override suspend fun provideGlance(context: Context, id: GlanceId) {
        provideContent {
            GlanceTheme {
                Column(
                    modifier = GlanceModifier
                        .fillMaxSize()
                        .background(GlanceTheme.colors.widgetBackground)
                        .padding(16.dp)
                ) {
                    Text(
                        text = "Tasks",
                        style = TextStyle(fontWeight = FontWeight.Bold,
                                         color = GlanceTheme.colors.onSurface)
                    )
                    // Widget content
                }
            }
        }
    }
}
```

**Rules:**
- R10.1: Use Glance API for new widgets. Support dynamic color via `GlanceTheme`.
- R10.2: Widgets must have a default configuration and work immediately after placement.
- R10.3: Provide multiple widget sizes (small, medium, large) where practical.
- R10.4: Use rounded corners matching the system widget shape (`system_app_widget_background_radius`).

### 10.2 App Shortcuts

```xml
<!-- shortcuts.xml -->
<shortcuts xmlns:android="http://schemas.android.com/apk/res/android">
    <shortcut
        android:shortcutId="compose"
        android:enabled="true"
        android:shortcutShortLabel="@string/compose_short"
        android:shortcutLongLabel="@string/compose_long"
        android:icon="@drawable/ic_shortcut_compose">
        <intent
            android:action="android.intent.action.VIEW"
            android:targetPackage="com.example.app"
            android:targetClass="com.example.app.ComposeActivity" />
    </shortcut>
</shortcuts>
```

**Rules:**
- R10.5: Provide 2-4 static shortcuts for common actions. Support dynamic shortcuts for recent content.
- R10.6: Shortcut icons should be simple, recognizable silhouettes on a circular background.
- R10.7: Test shortcuts with long-press on the app icon and in the Settings > Apps shortcut list.

### 10.3 Deep Links and Share

**Rules:**
- R10.8: Support Android App Links (verified deep links) for all public content URLs.
- R10.9: Implement the share sheet with `ShareCompat` or `Intent.createChooser`. Provide rich previews with title, description, and thumbnail.
- R10.10: Handle incoming share intents with appropriate content type filtering.

---

## Design Evaluation Checklist

Use this checklist to evaluate Android UI implementations:

### Theme & Color
- [ ] Dynamic color enabled with static fallback
- [ ] All colors reference Material theme roles (no hardcoded hex)
- [ ] Light and dark themes both supported
- [ ] On-colors match their background color roles
- [ ] Custom colors generated from seed via Material Theme Builder

### Navigation
- [ ] Correct navigation component for screen size and destination count
- [ ] Navigation bar labels always visible
- [ ] Predictive back gesture opted in and handled
- [ ] Up vs Back behavior correct

### Layout
- [ ] All three window size classes supported
- [ ] Edge-to-edge with proper inset handling
- [ ] Content does not span full width on large screens
- [ ] Foldable hinge area respected

### Typography
- [ ] All text uses sp units
- [ ] All text references MaterialTheme.typography roles
- [ ] Tested at 200% font scale with no clipping
- [ ] Minimum 12sp body, 11sp labels

### Components
- [ ] At most one FAB per screen
- [ ] Top app bar connected to scroll behavior
- [ ] Snackbars used for non-critical feedback only
- [ ] Dialogs reserved for critical interruptions

### Accessibility
- [ ] All interactive elements have contentDescription
- [ ] All touch targets >= 48dp
- [ ] Color contrast >= 4.5:1 for text
- [ ] No information conveyed by color alone
- [ ] Full TalkBack traversal tested
- [ ] Switch Access and keyboard navigation work

### Gestures
- [ ] No interactive elements in system gesture zones
- [ ] All gesture actions have non-gesture alternatives
- [ ] Swipe-to-dismiss is undoable

### Notifications
- [ ] Separate channels for each notification type
- [ ] Appropriate importance levels
- [ ] Tap action navigates to relevant content

### Permissions
- [ ] Permissions requested in context, not at launch
- [ ] Rationale shown before permission request
- [ ] Graceful degradation on denial
- [ ] Photo Picker used instead of media permission

### System Integration
- [ ] Widgets use Glance API with dynamic color
- [ ] App shortcuts provided for common actions
- [ ] Deep links handled for public content

---

## Anti-Patterns

| Anti-Pattern | Why It Is Wrong | Correct Approach |
|-------------|----------------|------------------|
| Hardcoded color hex values | Breaks dynamic color and dark theme | Use `MaterialTheme.colorScheme` roles |
| Using `dp` for text size | Ignores user font scaling | Use `sp` units |
| Custom bottom navigation bar | Inconsistent with platform | Use Material `NavigationBar` |
| Navigation bar without labels | Violates Material guidelines | Always show labels |
| Dialog for non-critical info | Interrupts user unnecessarily | Use Snackbar or Bottom Sheet |
| FAB for secondary actions | Dilutes primary action prominence | One FAB for the primary action only |
| `onBackPressed()` override | Deprecated; breaks predictive back | Use `BackHandler` (Compose) or `OnBackInvokedCallback` (View-based) for predictive back support |
| Touch targets < 48dp | Accessibility violation | Ensure minimum 48x48dp |
| Permission request at launch | Users deny without context | Request in context with rationale |
| Pure black (#000000) dark theme | Eye strain; not Material 3 | Use Material surface color roles |
| Icon-only navigation bar | Users cannot identify destinations | Always include text labels |
| Full-width content on tablets | Wastes space; poor readability | Max width or list-detail layout |
| `READ_EXTERNAL_STORAGE` for photos | Unnecessary since Android 13 | Use Photo Picker API |
| Blocking UI on permission denial | Punishes the user | Graceful degradation |
| Manual color palette selection | Inconsistent tonal relationships | Use Material Theme Builder |
```

## File: `skills/android/metadata.json`
```json
{
  "version": "1.0.0",
  "organization": "Platform Design Skills",
  "date": "February 2026",
  "abstract": "Material Design 3 and Android platform guidelines. 106 rules across 10 categories covering Material You, dynamic color, navigation patterns, Jetpack Compose components, accessibility, adaptive layouts, and Android-specific interactions. Each rule includes Compose and XML examples.",
  "references": [
    "https://m3.material.io",
    "https://developer.android.com/design",
    "https://developer.android.com/develop/ui/compose",
    "https://developer.android.com/guide/topics/ui/accessibility"
  ]
}
```

## File: `skills/android/rules/_sections.md`
```markdown
# Android Design Guidelines — Section Index

Quick reference for locating rules by category and ID.

## Section Map

| # | Section | Priority | Rules | Topics |
|---|---------|----------|-------|--------|
| 1 | Material You & Theming | CRITICAL | R1.1–R1.11 | Dynamic color, color roles, light/dark themes, custom seeds, tonal palettes |
| 2 | Navigation | CRITICAL | R2.1–R2.14 | Navigation bar, navigation rail, navigation drawer, predictive back, up vs back |
| 3 | Layout & Responsive | HIGH | R3.1–R3.10 | Window size classes, Material grid, edge-to-edge, insets, foldable support |
| 4 | Typography | HIGH | R4.1–R4.5 | Type scale, sp units, font scaling, line height, custom fonts |
| 5 | Components | HIGH | R5.1–R5.19 | FAB, top app bar, bottom sheets, dialogs, snackbars, chips, cards, waiting states |
| 6 | Accessibility | CRITICAL | R6.1–R6.13 | TalkBack, contentDescription, touch targets, contrast, focus order, custom canvas views |
| 7 | Gestures & Input | MEDIUM | R7.1–R7.7 | System gestures, pull to refresh, swipe to dismiss, long press, ripple |
| 8 | Notifications | MEDIUM | R8.1–R8.9 | Channels, importance, messaging style, expandable, foreground service |
| 9 | Permissions & Privacy | HIGH | R9.1–R9.8 | Runtime permissions, rationale, photo picker, approximate location |
| 10 | System Integration | MEDIUM | R10.1–R10.10 | Widgets (Glance), app shortcuts, deep links, share sheet |

## Rule Index

### 1. Material You & Theming [CRITICAL]

- **R1.1** — Provide fallback static color scheme for devices below Android 12
- **R1.2** — Never hardcode color hex values; use theme color roles
- **R1.3** — Test with at least 3 wallpapers for dynamic color harmony
- **R1.4** — Foreground elements must use matching `on` color role
- **R1.5** — Use `surface` variants for backgrounds, not `primary`/`secondary`
- **R1.6** — Use `tertiary` sparingly for accent only
- **R1.7** — Always support both light and dark themes
- **R1.8** — Dark theme uses tonal mapping, not pure black
- **R1.9** — Provide manual theme override (System/Light/Dark)
- **R1.10** — Generate tonal palettes from seed via Material Theme Builder
- **R1.11** — Support dynamic color as default; custom colors as fallback

### 2. Navigation [CRITICAL]

- **R2.1** — Navigation Bar for 3-5 destinations on compact screens
- **R2.2** — Always show labels on navigation bar items
- **R2.3** — Filled icons for selected, outlined for unselected
- **R2.4** — Active indicator uses `secondaryContainer`
- **R2.5** — Navigation Rail on medium (600dp+) and expanded screens
- **R2.6** — Optionally include FAB in rail header
- **R2.7** — Rail labels optional but recommended
- **R2.8** — Modal drawer on compact, permanent drawer on expanded
- **R2.9** — Group drawer items with dividers and section headers
- **R2.10** — Opt in to predictive back; use `BackHandler` (Compose) or `OnBackInvokedCallback` (View-based)
- **R2.11** — System back != Up button; they may navigate differently
- **R2.12** — No "are you sure?" on back unless unsaved user input
- **R2.13** — Do not suppress the system predictive back preview animation; interpolate custom transitions using `BackEventCompat.progress` and respect `BackEventCompat.swipeEdge`
- **R2.14** — Prefer recognition over recall; keep destinations labeled and visible state preserved

### 3. Layout & Responsive [HIGH]

- **R3.1** — Use `WindowSizeClass` for responsive decisions
- **R3.2** — Never use fixed pixel breakpoints
- **R3.3** — Support all three width size classes
- **R3.4** — Max content width ~840dp on expanded screens
- **R3.5** — Consistent horizontal margins per grid spec
- **R3.6** — Call `enableEdgeToEdge()` before `setContent`
- **R3.7** — Use `WindowInsets` to pad content from system bars
- **R3.8** — Scrollable content scrolls behind transparent system bars
- **R3.9** — Detect fold/hinge; avoid content across fold
- **R3.10** — Use `ListDetailPaneScaffold` for foldable-aware layouts

### 4. Typography [HIGH]

- **R4.1** — Use `sp` units for all text sizes
- **R4.2** — Minimum 12sp body text, 11sp labels
- **R4.3** — Reference `MaterialTheme.typography` roles, not hardcoded sizes
- **R4.4** — Test at 200% font scale; no clipping
- **R4.5** — Line height 1.2-1.5x font size

### 5. Components [HIGH]

- **R5.1** — At most one FAB per screen
- **R5.2** — FAB at bottom-end, above Navigation Bar
- **R5.3** — FAB uses `primaryContainer` by default
- **R5.4** — Prefer `ExtendedFloatingActionButton` with label
- **R5.5** — Small top app bar for most screens; medium/large for prominent titles
- **R5.6** — Connect scroll behavior to top app bar
- **R5.7** — Limit action icons to 2-3; overflow the rest
- **R5.8** — Modal bottom sheets for supplementary; standard for persistent
- **R5.9** — Bottom sheets must have visible drag handle
- **R5.10** — Sheet content must be scrollable if it overflows
- **R5.11** — Dialogs for critical decisions only
- **R5.12** — Confirm button is text button; dismiss on left
- **R5.13** — Dialog titles are concise questions or statements
- **R5.14** — Snackbars for brief non-critical feedback
- **R5.15** — Snackbars above Navigation Bar, below FAB
- **R5.16** — Include undo action when operation is reversible
- **R5.17** — Correct chip type for use case (Filter/Assist/Input/Suggestion)
- **R5.18** — Chips in horizontal scroll or flow layout, not stacked vertically
- **R5.19** — Expose waiting states immediately; acknowledge long-running work with visible progress

### 6. Accessibility [CRITICAL]

- **R6.1** — Every interactive element needs `contentDescription`
- **R6.2** — Describe action/meaning, not visual appearance
- **R6.3** — `mergeDescendants` for grouped related elements
- **R6.4** — Provide `customActions` for swipe/long-press actions
- **R6.5** — Minimum 48x48dp touch targets
- **R6.6** — Do not reduce touch targets to save space
- **R6.7** — Text contrast >= 4.5:1 normal, >= 3:1 large
- **R6.8** — Never use color alone to convey information
- **R6.9** — Support bold text and high contrast settings
- **R6.10** — Logical focus order (top-to-bottom, start-to-end)
- **R6.11** — Move focus to logical target after navigation/dialog dismissal
- **R6.12** — Full operability via TalkBack, Switch Access, keyboard
- **R6.13** — Custom canvas views must use ExploreByTouchHelper for a virtual accessibility tree

### 7. Gestures & Input [MEDIUM]

- **R7.1** — No interactive elements in system gesture zones
- **R7.2** — Use `WindowInsets.systemGestures` to detect conflict zones
- **R7.3** — Swipe-to-dismiss must be undoable or confirmed
- **R7.4** — Non-gesture alternatives for all gesture actions
- **R7.5** — Material ripple on all tappable elements
- **R7.6** — Long press for context menus; never the only access path
- **R7.7** — Haptic feedback on long press

### 8. Notifications [MEDIUM]

- **R8.1** — Separate channels for each notification type
- **R8.2** — Choose importance levels conservatively
- **R8.3** — All notifications must have a tap action
- **R8.4** — Notification icons need `contentDescription`
- **R8.5** — `MessagingStyle` for conversations
- **R8.6** — Direct reply actions on message notifications
- **R8.7** — "Mark as read" action on message notifications
- **R8.8** — Use expandable styles for rich content
- **R8.9** — Foreground service notifications describe operation + stop action

### 9. Permissions & Privacy [HIGH]

- **R9.1** — Request permissions in context, not at launch
- **R9.2** — Show rationale before requesting
- **R9.3** — Graceful degradation on denial
- **R9.4** — Never request unnecessary permissions
- **R9.5** — Use Photo Picker instead of `READ_MEDIA_IMAGES`
- **R9.6** — Prefer `ACCESS_COARSE_LOCATION` unless precise is essential
- **R9.7** — One-time permissions for camera/mic in non-recording contexts
- **R9.8** — Privacy indicator when camera/mic actively in use

### 10. System Integration [MEDIUM]

- **R10.1** — Glance API for widgets with dynamic color
- **R10.2** — Widgets must work immediately after placement
- **R10.3** — Multiple widget sizes where practical
- **R10.4** — Rounded corners matching system widget shape
- **R10.5** — 2-4 static shortcuts; support dynamic shortcuts
- **R10.6** — Shortcut icons: simple silhouettes on circular background
- **R10.7** — Test shortcuts via long-press and Settings
- **R10.8** — Android App Links for public content URLs
- **R10.9** — Share sheet with rich previews
- **R10.10** — Handle incoming share intents with content type filtering

## Cross-References

| Topic | Primary Section | Also See |
|-------|----------------|----------|
| Dark theme | 1.3 | 6.3 (contrast) |
| Touch targets | 6.2 | 7.1 (gesture zones) |
| System bars | 3.3 | 7.1 (gesture insets) |
| FAB placement | 5.1 | 2.2 (rail header), 5.15 (snackbar) |
| Font scaling | 4.1 | R4.4 (200% scale test), R6.9 (bold text) |
| Permissions | 9.1 | 9.5 (photo picker) |
| Navigation sizing | 2.5 (table) | 3.1 (window size classes) |
| Color roles | 1.2 | R2.4 (nav indicator active color), R5.3 (FAB color) |
```

## File: `skills/ios/AGENTS.md`
```markdown
# iOS Design Skill

Apple Human Interface Guidelines for iPhone apps — layout, navigation, typography, accessibility, and system integration rules with SwiftUI/UIKit examples.

**Reference:** https://developer.apple.com/design/human-interface-guidelines

## Rule Categories

| # | Category | Impact | Rules |
|---|----------|--------|-------|
| 1 | Layout & Safe Areas | CRITICAL | Touch targets, safe areas, thumb zone, screen sizes |
| 2 | Navigation | CRITICAL | Tab bars, large titles, back swipe, state preservation |
| 3 | Typography & Dynamic Type | HIGH | Text styles, Dynamic Type, UIFontMetrics, SF Pro |
| 4 | Color & Dark Mode | HIGH | Semantic colors, contrast, P3 gamut, accent color |
| 5 | Accessibility | CRITICAL | VoiceOver, Bold Text, Reduce Motion, Switch Control |
| 6 | Gestures & Input | HIGH | Standard gestures, system gesture protection, input methods |
| 7 | Components | HIGH | Buttons, alerts, sheets, lists, tab bars, search, menus, SF Symbols |
| 8 | Patterns | MEDIUM | Onboarding, loading, launch, modality, feedback |
| 9 | Privacy & Permissions | HIGH | Contextual requests, Sign in with Apple, ATT |
| 10 | System Integration | MEDIUM | Widgets, App Shortcuts, Spotlight, Live Activities |

## Never Do

- Never use hamburger menus — use a tab bar
- Never override swipe-from-left-edge back navigation
- Never hardcode text sizes — support Dynamic Type
- Never use only color to convey information
- Never request all permissions at launch
- Never place primary actions at the top of the screen (outside thumb zone)
- Never clip content under the status bar, home indicator, or Dynamic Island
- Never use blocking spinner overlays for loading states
- Never show splash screen logos — match the first screen of the app
- Never hide the tab bar during navigation within a tab
```

## File: `skills/ios/SKILL.md`
```markdown
---
name: ios-design-guidelines
description: Apple Human Interface Guidelines for iPhone. Use when building, reviewing, or refactoring SwiftUI/UIKit interfaces for iOS. Triggers on tasks involving iPhone UI, iOS components, accessibility, Dynamic Type, Dark Mode, or HIG compliance.
license: MIT
metadata:
  author: platform-design-skills
  version: "1.0.0"
---

# iOS Design Guidelines for iPhone

Comprehensive rules derived from Apple's Human Interface Guidelines. Apply these when building, reviewing, or refactoring any iPhone app interface.

---

## 1. Layout & Safe Areas
**Impact:** CRITICAL

### Rule 1.1: Minimum 44pt Touch Targets
All interactive elements must have a minimum tap target of 44x44 points. This includes buttons, links, toggles, and custom controls.

**Correct:**
```swift
Button("Save") { save() }
    .frame(minWidth: 44, minHeight: 44)
```

**Incorrect:**
```swift
// 20pt icon with no padding — too small to tap reliably
Button(action: save) {
    Image(systemName: "checkmark")
        .font(.system(size: 20))
}
// Missing .frame(minWidth: 44, minHeight: 44)
```

### Rule 1.2: Respect Safe Areas
Never place interactive or essential content under the status bar, Dynamic Island, or home indicator. Use SwiftUI's automatic safe area handling or UIKit's `safeAreaLayoutGuide`.

**Correct:**
```swift
struct ContentView: View {
    var body: some View {
        VStack {
            Text("Content")
        }
        // SwiftUI respects safe areas by default
    }
}
```

**Incorrect:**
```swift
struct ContentView: View {
    var body: some View {
        VStack {
            Text("Content")
        }
        .ignoresSafeArea() // Content will be clipped under notch/Dynamic Island
    }
}
```

Use `.ignoresSafeArea()` only for background fills, images, or decorative elements — never for text or interactive controls.

### Rule 1.3: Primary Actions in the Thumb Zone
Place primary actions at the bottom of the screen where the user's thumb naturally rests. Secondary actions and navigation belong at the top.

**Correct:**
```swift
VStack {
    ScrollView { /* content */ }
    Button("Continue") { next() }
        .buttonStyle(.borderedProminent)
        .padding()
}
```

**Incorrect:**
```swift
VStack {
    Button("Continue") { next() } // Top of screen — hard to reach one-handed
        .buttonStyle(.borderedProminent)
        .padding()
    ScrollView { /* content */ }
}
```

### Rule 1.4: Support All iPhone Screen Sizes
Design for iPhone SE (375pt wide) through iPhone Pro Max (430pt wide). Use flexible layouts, avoid hardcoded widths.

**Correct:**
```swift
HStack(spacing: 12) {
    ForEach(items) { item in
        CardView(item: item)
            .frame(maxWidth: .infinity) // Adapts to screen width
    }
}
```

**Incorrect:**
```swift
HStack(spacing: 12) {
    ForEach(items) { item in
        CardView(item: item)
            .frame(width: 180) // Breaks on SE, wastes space on Pro Max
    }
}
```

### Rule 1.5: 8pt Grid Alignment
Align spacing, padding, and element sizes to multiples of 8 points (8, 16, 24, 32, 40, 48). Use 4pt for fine adjustments.

### Rule 1.6: Landscape Support
Support landscape orientation unless the app is task-specific (e.g., camera). Use `ViewThatFits` or `GeometryReader` for adaptive layouts.

---

## 2. Navigation
**Impact:** CRITICAL

### Rule 2.1: Tab Bar for Top-Level Sections
Use a tab bar at the bottom of the screen for 3 to 5 top-level sections. Each tab should represent a distinct category of content or functionality.

**Correct:**
```swift
TabView {
    HomeView()
        .tabItem {
            Label("Home", systemImage: "house")
        }
    SearchView()
        .tabItem {
            Label("Search", systemImage: "magnifyingglass")
        }
    ProfileView()
        .tabItem {
            Label("Profile", systemImage: "person")
        }
}
```

**Incorrect:**
```swift
// Hamburger menu hidden behind three lines — discoverability is near zero
NavigationView {
    Button(action: { showMenu.toggle() }) {
        Image(systemName: "line.horizontal.3")
    }
}
```

### Rule 2.2: Never Use Hamburger Menus
Hamburger (drawer) menus hide navigation, reduce discoverability, and violate iOS conventions. Use a tab bar instead. If you have more than 5 sections, consolidate or use a "More" tab.

### Rule 2.3: Large Titles in Primary Views
Use `.navigationBarTitleDisplayMode(.large)` for top-level views. Titles transition to inline (`.inline`) when the user scrolls.

**Correct:**
```swift
NavigationStack {
    List(items) { item in
        ItemRow(item: item)
    }
    .navigationTitle("Messages")
    .navigationBarTitleDisplayMode(.large)
}
```

### Rule 2.4: Never Override Back Swipe
The swipe-from-left-edge gesture for back navigation is a system-level expectation. Never attach custom gesture recognizers that interfere with it.

**Incorrect:**
```swift
.gesture(
    DragGesture()
        .onChanged { /* custom drawer */ } // Conflicts with system back swipe
)
```

### Rule 2.5: Use NavigationStack for Hierarchical Content
Use `NavigationStack` (not the deprecated `NavigationView`) for drill-down content. Use `NavigationPath` for programmatic navigation.

**Correct:**
```swift
NavigationStack(path: $path) {
    List(items) { item in
        NavigationLink(value: item) {
            ItemRow(item: item)
        }
    }
    .navigationDestination(for: Item.self) { item in
        ItemDetail(item: item)
    }
}
```

### Rule 2.6: Preserve State Across Navigation
When users navigate back and then forward, or switch tabs, restore the previous scroll position and input state. Use `@SceneStorage` or `@State` to persist view state.

### Rule 2.7: Prefer Recognition Over Recall
Keep current location, recent choices, and available destinations visible. Restore tab, scroll, filter, and selection state so users continue from recognition instead of reconstructing context from memory.

---

## 3. Typography & Dynamic Type
**Impact:** HIGH

### Rule 3.1: Use Built-in Text Styles
Always use semantic text styles rather than hardcoded sizes. These scale automatically with Dynamic Type.

**Correct:**
```swift
VStack(alignment: .leading, spacing: 4) {
    Text("Section Title")
        .font(.headline)
    Text("Body content that explains the section.")
        .font(.body)
    Text("Last updated 2 hours ago")
        .font(.caption)
        .foregroundStyle(.secondary)
}
```

**Incorrect:**
```swift
VStack(alignment: .leading, spacing: 4) {
    Text("Section Title")
        .font(.system(size: 17, weight: .semibold)) // Won't scale with Dynamic Type
    Text("Body content")
        .font(.system(size: 15)) // Won't scale with Dynamic Type
}
```

### Rule 3.2: Support Dynamic Type Including Accessibility Sizes
Dynamic Type can scale text up to approximately 200% at the largest accessibility sizes. Layouts must reflow — never truncate or clip essential text.

**Correct:**
```swift
HStack {
    Image(systemName: "star")
    Text("Favorites")
        .font(.body)
}
// At accessibility sizes, consider using ViewThatFits or
// AnyLayout to switch from HStack to VStack
```

Use `@Environment(\.dynamicTypeSize)` to detect size category and adapt layouts:

```swift
@Environment(\.dynamicTypeSize) var dynamicTypeSize

var body: some View {
    if dynamicTypeSize.isAccessibilitySize {
        VStack { content }
    } else {
        HStack { content }
    }
}
```

### Rule 3.3: Custom Fonts Must Scale with Dynamic Type
If you use a custom typeface, scale it so it responds to Dynamic Type. The API differs by framework.

**Correct (SwiftUI):**
```swift
extension Font {
    static func scaledCustom(size: CGFloat, relativeTo textStyle: Font.TextStyle) -> Font {
        .custom("CustomFont-Regular", size: size, relativeTo: textStyle)
    }
}

// Usage
Text("Hello")
    .font(.scaledCustom(size: 17, relativeTo: .body))
```

**Correct (UIKit):**
```swift
let metrics = UIFontMetrics(forTextStyle: .body)
let customFont = UIFont(name: "CustomFont-Regular", size: 17)!
label.font = metrics.scaledFont(for: customFont)
label.adjustsFontForContentSizeCategory = true
```

### Rule 3.4: SF Pro as System Font
Use the system font (SF Pro) unless brand requirements dictate otherwise. SF Pro is optimized for legibility on Apple displays.

### Rule 3.5: Minimum 11pt Text
Never display text smaller than 11pt. Prefer 17pt for body text. Use the `caption2` style (11pt) as the absolute minimum.

### Rule 3.6: Hierarchy Through Weight and Size
Establish visual hierarchy through font weight and size. Do not rely solely on color to differentiate text levels.

---

## 4. Color & Dark Mode
**Impact:** HIGH

### Rule 4.1: Use Semantic System Colors
Use system-provided semantic colors that automatically adapt to light and dark modes.

**Correct:**
```swift
Text("Primary text")
    .foregroundStyle(.primary) // Adapts to light/dark

Text("Secondary info")
    .foregroundStyle(.secondary)

VStack { }
    .background(Color(.systemBackground)) // White in light, black in dark
```

**Incorrect:**
```swift
Text("Primary text")
    .foregroundColor(.black) // Invisible on dark backgrounds

VStack { }
    .background(.white) // Blinding in Dark Mode
```

### Rule 4.2: Provide Light and Dark Variants for Custom Colors
Define custom colors in the asset catalog with both Any Appearance and Dark Appearance variants.

```swift
// In Assets.xcassets, define "BrandBlue" with:
// Any Appearance: #0066CC
// Dark Appearance: #4DA3FF

Text("Brand text")
    .foregroundStyle(Color("BrandBlue")) // Automatically switches
```

### Rule 4.3: Never Rely on Color Alone
Always pair color with text, icons, or shapes to convey meaning. Approximately 8% of men have some form of color vision deficiency.

**Correct:**
```swift
HStack {
    Image(systemName: "exclamationmark.triangle.fill")
        .foregroundStyle(.red)
    Text("Error: Invalid email address")
        .foregroundStyle(.red)
}
```

**Incorrect:**
```swift
// Only color indicates the error — invisible to colorblind users
TextField("Email", text: $email)
    .border(isValid ? .green : .red)
```

### Rule 4.4: 4.5:1 Contrast Ratio Minimum
All text must meet WCAG AA contrast ratios: 4.5:1 for normal text, 3:1 for large text (18pt+ or 14pt+ bold).

### Rule 4.5: Support Display P3 Wide Gamut
Use Display P3 color space for vibrant, accurate colors on modern iPhones. Define colors in the asset catalog with the Display P3 gamut.

### Rule 4.6: Background Hierarchy
Use the three-level background hierarchy for depth:
- `systemBackground` — primary surface
- `secondarySystemBackground` — grouped content, cards
- `tertiarySystemBackground` — elements within grouped content

### Rule 4.7: One Accent Color for Interactive Elements
Choose a single tint/accent color for all interactive elements (buttons, links, toggles). This creates a consistent, learnable visual language.

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .tint(.indigo) // All interactive elements use indigo
        }
    }
}
```

---

## 5. Accessibility
**Impact:** CRITICAL

### Rule 5.1: VoiceOver Labels on All Interactive Elements
Every button, control, and interactive element must have a meaningful accessibility label.

**Correct:**
```swift
Button(action: addToCart) {
    Image(systemName: "cart.badge.plus")
}
.accessibilityLabel("Add to cart")
```

**Incorrect:**
```swift
Button(action: addToCart) {
    Image(systemName: "cart.badge.plus")
}
// VoiceOver reads "cart.badge.plus" — meaningless to users
```

### Rule 5.2: Logical VoiceOver Navigation Order
Ensure VoiceOver reads elements in a logical order. Use `.accessibilitySortPriority()` to adjust when the visual layout doesn't match the reading order.

```swift
VStack {
    Text("Price: $29.99")
        .accessibilitySortPriority(1) // Read second (lower number = lower priority)
    Text("Product Name")
        .accessibilitySortPriority(2) // Read first (higher number = higher priority)
}
```

### Rule 5.3: Support Bold Text
When the user enables Bold Text in Settings, custom-rendered text must adapt. SwiftUI text styles handle this automatically. For SwiftUI custom rendering, use `@Environment(\.legibilityWeight)` to apply heavier weights. UIKit code must check `UIAccessibility.isBoldTextEnabled` and re-query on `UIAccessibility.boldTextStatusDidChangeNotification`.

**Correct:**
```swift
// SwiftUI — standard text styles adapt automatically
Text("Section Header")
    .font(.headline)

// SwiftUI — custom rendering respects legibilityWeight
@Environment(\.legibilityWeight) var legibilityWeight

var body: some View {
    Text("Custom Label")
        .fontWeight(legibilityWeight == .bold ? .bold : .regular)
}
```

**Incorrect:**
```swift
// Hardcoded weight ignores Bold Text preference
label.font = UIFont.systemFont(ofSize: 17, weight: .regular)
// Missing: re-query font when UIAccessibility.boldTextStatusDidChangeNotification fires
```

### Rule 5.4: Support Reduce Motion
Disable decorative animations and parallax when Reduce Motion is enabled. Use `@Environment(\.accessibilityReduceMotion)`.

**Correct:**
```swift
@Environment(\.accessibilityReduceMotion) var reduceMotion

var body: some View {
    CardView()
        .animation(reduceMotion ? nil : .spring(), value: isExpanded)
}
```

### Rule 5.5: Support Increase Contrast
When the user enables Increase Contrast, ensure custom colors have higher-contrast variants. Use `@Environment(\.colorSchemeContrast)` to detect.

### Rule 5.6: Don't Convey Info Only by Color, Shape, or Position
Information must be available through multiple channels. Pair visual indicators with text or accessibility descriptions.

### Rule 5.7: Alternative Interactions for All Gestures
Every custom gesture must have an equivalent tap-based or menu-based alternative for users who cannot perform complex gestures.

### Rule 5.8: Support Switch Control and Full Keyboard Access
Ensure all interactions work with Switch Control (external switches) and Full Keyboard Access (Bluetooth keyboards). Test navigation order and focus behavior.

---

## 6. Gestures & Input
**Impact:** HIGH

### Rule 6.1: Use Standard Gestures
Use the standard iOS gesture vocabulary: tap, long press, swipe, pinch, rotate. Users already understand these.

| Gesture | Standard Use |
|---------|-------------|
| Tap | Primary action, selection |
| Long press | Context menu, preview |
| Swipe horizontal | Delete, archive, navigate back |
| Swipe vertical | Scroll, dismiss sheet |
| Pinch | Zoom in/out |
| Two-finger rotate | Rotate content |

### Rule 6.2: Never Override System Gestures
These gestures are reserved by the system and must not be intercepted:
- Swipe from left edge (back navigation)
- Swipe down from top-left (Notification Center)
- Swipe down from top-right (Control Center)
- Swipe up from bottom (home / app switcher)

### Rule 6.3: Custom Gestures Must Be Discoverable
If you add a custom gesture, provide visual hints (e.g., a grabber handle) and ensure the action is also available through a visible button or menu item.

### Rule 6.4: Support All Input Methods
Design for touch first, but also support:
- Hardware keyboards (iPad keyboard accessories, Bluetooth keyboards)
- Assistive devices (Switch Control, head tracking)
- Pointer input (assistive touch)

---

## 7. Components
**Impact:** HIGH

### Rule 7.1: Button Styles
Use the built-in button styles appropriately:
- `.borderedProminent` — primary call-to-action
- `.bordered` — secondary actions
- `.borderless` — tertiary or inline actions
- `.destructive` role — red tint for delete/remove

**Correct:**
```swift
VStack(spacing: 16) {
    Button("Purchase") { buy() }
        .buttonStyle(.borderedProminent)

    Button("Add to Wishlist") { wishlist() }
        .buttonStyle(.bordered)

    Button("Delete", role: .destructive) { delete() }
}
```

### Rule 7.2: Alerts — Critical Info Only
Use alerts sparingly for critical information that requires a decision. Prefer 2 buttons; maximum 3. The destructive option should use `.destructive` role.

**Correct:**
```swift
.alert("Delete Photo?", isPresented: $showAlert) {
    Button("Delete", role: .destructive) { deletePhoto() }
    Button("Cancel", role: .cancel) { }
} message: {
    Text("This photo will be permanently removed.")
}
```

**Incorrect:**
```swift
// Alert for non-critical info — should be a banner or toast
.alert("Tip", isPresented: $showTip) {
    Button("OK") { }
} message: {
    Text("Swipe left to delete items.")
}
```

### Rule 7.3: Sheets for Scoped Tasks
Present sheets for self-contained tasks. Always provide a way to dismiss (close button or swipe down). Use `.presentationDetents()` for half-height sheets.

```swift
.sheet(isPresented: $showCompose) {
    NavigationStack {
        ComposeView()
            .navigationTitle("New Message")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { showCompose = false }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Send") { send() }
                }
            }
    }
    .presentationDetents([.medium, .large])
}
```

### Rule 7.4: Lists — Inset Grouped Default
Use the `.insetGrouped` list style as the default. Support swipe actions for common operations. Minimum row height is 44pt.

**Correct:**
```swift
List {
    Section("Recent") {
        ForEach(recentItems) { item in
            ItemRow(item: item)
                .swipeActions(edge: .trailing) {
                    Button(role: .destructive) { delete(item) } label: {
                        Label("Delete", systemImage: "trash")
                    }
                    Button { archive(item) } label: {
                        Label("Archive", systemImage: "archivebox")
                    }
                    .tint(.blue)
                }
        }
    }
}
.listStyle(.insetGrouped)
```

### Rule 7.5: Tab Bar Behavior
- Use SF Symbols for tab icons — filled variant for the selected tab, outline for unselected
- Never hide the tab bar when navigating deeper within a tab
- Badge important counts with `.badge()`

```swift
TabView {
    MessagesView()
        .tabItem {
            Label("Messages", systemImage: "message")
        }
        .badge(unreadCount)
}
```

### Rule 7.6: Search
Place search using `.searchable()`. Provide search suggestions and support recent searches.

```swift
NavigationStack {
    List(filteredItems) { item in
        ItemRow(item: item)
    }
    .searchable(text: $searchText, prompt: "Search items")
    .searchSuggestions {
        ForEach(suggestions) { suggestion in
            Text(suggestion.title)
                .searchCompletion(suggestion.title)
        }
    }
}
```

### Rule 7.7: Context Menus
Use context menus (long press) for secondary actions. Never use a context menu as the only way to access an action.

```swift
PhotoView(photo: photo)
    .contextMenu {
        Button { share(photo) } label: {
            Label("Share", systemImage: "square.and.arrow.up")
        }
        Button { favorite(photo) } label: {
            Label("Favorite", systemImage: "heart")
        }
        Button(role: .destructive) { delete(photo) } label: {
            Label("Delete", systemImage: "trash")
        }
    }
```

### Rule 7.8: Progress Indicators
- Determinate (`ProgressView(value:total:)`) for operations with known duration
- Indeterminate (`ProgressView()`) for unknown duration
- Never block the entire screen with a spinner

### Rule 7.9: SF Symbols — Rendering Modes
Use the appropriate rendering mode for each symbol. Monochrome is the default; hierarchical, palette, and multicolor provide richer expression where appropriate. Always prefer the symbol rendering mode that best communicates meaning — do not default to monochrome when multicolor conveys critical state.

**Correct:**
```swift
// Hierarchical: single color with automatic opacity layers
Image(systemName: "person.crop.circle.fill")
    .symbolRenderingMode(.hierarchical)
    .foregroundStyle(.blue)

// Multicolor: system-defined color per layer (e.g., battery, weather)
Image(systemName: "battery.100percent.bolt")
    .symbolRenderingMode(.multicolor)

// Palette: explicit per-layer colors
Image(systemName: "folder.badge.plus")
    .symbolRenderingMode(.palette)
    .foregroundStyle(.white, .blue)
```

**Incorrect:**
```swift
// Monochrome on a symbol that has meaningful multicolor layers
Image(systemName: "battery.100percent.bolt")
    .foregroundColor(.gray) // loses the contextual color meaning
```

### Rule 7.10: SF Symbols — Weight and Scale
Match the symbol weight to adjacent text weight. Use scale variants (`.small`, `.medium`, `.large`) rather than resizing. The symbol weight should never appear heavier than adjacent text.

**Correct:**
```swift
Label("Download", systemImage: "arrow.down.circle.fill")
    .font(.body.weight(.semibold))
    // Symbol inherits .semibold weight automatically via Label
```

**Incorrect:**
```swift
HStack {
    Image(systemName: "arrow.down.circle.fill")
        .font(.system(size: 32)) // explicit size ignores type scale
    Text("Download")
        .font(.body)
}
```

### Rule 7.11: SF Symbols — Animations (iOS 17+)
Use `symbolEffect` for symbol state transitions. Prefer discrete effects (`.bounce`, `.pulse`) for actions and indefinite effects (`.variableColor`) for ongoing state. Do not use manual cross-fade between symbol names when `contentTransition(.symbolEffect)` is available.

**Correct:**
```swift
Image(systemName: isLoading ? "arrow.2.circlepath" : "checkmark.circle")
    .contentTransition(.symbolEffect(.replace))
    .symbolEffect(.pulse, isActive: isLoading)
```

**Incorrect:**
```swift
// Manual opacity cross-fade between symbol names
if isLoading {
    Image(systemName: "arrow.2.circlepath")
} else {
    Image(systemName: "checkmark.circle")
}
```

---

## 8. Patterns
**Impact:** MEDIUM

### Rule 8.1: Onboarding — Max 3 Pages, Skippable
Keep onboarding to 3 or fewer pages. Always provide a skip option. Defer sign-in until the user needs authenticated features.

```swift
TabView {
    OnboardingPage(
        image: "wand.and.stars",
        title: "Smart Suggestions",
        subtitle: "Get personalized recommendations based on your preferences."
    )
    OnboardingPage(
        image: "bell.badge",
        title: "Stay Updated",
        subtitle: "Receive notifications for things that matter to you."
    )
    OnboardingPage(
        image: "checkmark.shield",
        title: "Private & Secure",
        subtitle: "Your data stays on your device."
    )
}
.tabViewStyle(.page)
.overlay(alignment: .topTrailing) {
    Button("Skip") { completeOnboarding() }
        .padding()
}
```

### Rule 8.2: Loading — Skeleton Views, No Blocking Spinners
Use skeleton/placeholder views that match the layout of the content being loaded. Never show a full-screen blocking spinner.

**Correct:**
```swift
if isLoading {
    ForEach(0..<5) { _ in
        SkeletonRow() // Placeholder matching final row layout
            .redacted(reason: .placeholder)
    }
} else {
    ForEach(items) { item in
        ItemRow(item: item)
    }
}
```

**Incorrect:**
```swift
if isLoading {
    ProgressView("Loading...") // Blocks the entire view
} else {
    List(items) { item in ItemRow(item: item) }
}
```

### Rule 8.3: Launch Screen — Match First Screen
The launch storyboard must visually match the initial screen of the app. No splash logos, no branding screens. This creates the perception of instant launch.

### Rule 8.4: Modality — Use Sparingly
Present modal views only when the user must complete or abandon a focused task. Always provide a clear dismiss action. Never stack modals on top of modals.

### Rule 8.5: Notifications — High Value Only
Only send notifications for content the user genuinely cares about. Support actionable notifications. Categorize notifications so users can control them granularly.

### Rule 8.6: Settings Placement
- **Frequent settings:** In-app settings screen accessible from a profile or gear icon
- **Privacy/permission settings:** Defer to the system Settings app via URL scheme
- Never duplicate system-level controls in-app

### Rule 8.7: Feedback — Visual + Haptic
Provide immediate feedback for every user action:
- Visual state change (button highlight, animation)
- Haptic feedback for significant actions using `UIImpactFeedbackGenerator`, `UINotificationFeedbackGenerator`, or `UISelectionFeedbackGenerator`

```swift
Button("Complete") {
    let generator = UINotificationFeedbackGenerator()
    generator.notificationOccurred(.success)
    completeTask()
}
```

### Rule 8.8: Show Waiting States Immediately
If an action cannot complete immediately, acknowledge the tap at once, then show inline progress, skeletons, or partial results. Never leave the interface visually unchanged while work continues.

---

## 9. Privacy & Permissions
**Impact:** HIGH

### Rule 9.1: Request Permissions in Context
Request a permission at the moment the user takes an action that needs it — never at app launch.

**Correct:**
```swift
Button("Take Photo") {
    // Request camera permission only when the user taps this button
    AVCaptureDevice.requestAccess(for: .video) { granted in
        if granted { showCamera = true }
    }
}
```

**Incorrect:**
```swift
// In AppDelegate.didFinishLaunching — too early, no context
func application(_ application: UIApplication, didFinishLaunchingWithOptions ...) {
    AVCaptureDevice.requestAccess(for: .video) { _ in }
    CLLocationManager().requestWhenInUseAuthorization()
    UNUserNotificationCenter.current().requestAuthorization(options: [.alert]) { _, _ in }
}
```

### Rule 9.2: Explain Before System Prompt
Show a custom explanation screen before triggering the system permission dialog. The system dialog only appears once — if the user denies, the app must direct them to Settings.

```swift
struct LocationExplanation: View {
    var body: some View {
        VStack(spacing: 16) {
            Image(systemName: "location.fill")
                .font(.largeTitle)
            Text("Find Nearby Stores")
                .font(.headline)
            Text("We use your location to show stores within walking distance. Your location is never shared or stored.")
                .font(.body)
                .multilineTextAlignment(.center)
            Button("Enable Location") {
                locationManager.requestWhenInUseAuthorization()
            }
            .buttonStyle(.borderedProminent)
            Button("Not Now") { dismiss() }
                .foregroundStyle(.secondary)
        }
        .padding()
    }
}
```

### Rule 9.3: Support Sign in with Apple
If the app offers any third-party sign-in (Google, Facebook), it must also offer Sign in with Apple. Present it as the first option.

### Rule 9.4: Don't Require Accounts Unless Necessary
Let users explore the app before requiring sign-in. Gate only features that genuinely need authentication (purchases, sync, social features).

### Rule 9.5: App Tracking Transparency
If you track users across apps or websites, display the ATT prompt. Respect denial — do not degrade the experience for users who opt out.

### Rule 9.6: Location Button for One-Time Access
Use `LocationButton` for actions that need location once without requesting ongoing permission.

```swift
import CoreLocationUI

LocationButton(.currentLocation) {
    fetchNearbyStores()
}
.labelStyle(.titleAndIcon)
```

---

## 10. System Integration
**Impact:** MEDIUM

### Rule 10.1: Widgets for Glanceable Data
Provide widgets using WidgetKit for information users check frequently. Show the most useful snapshot. Since iOS 17, widgets support interactive controls: use `Button` and `Toggle` backed by App Intents for actions users perform directly from the widget without opening the app.

```swift
// iOS 17+ interactive widget with a Button
struct TimerWidgetView: View {
    let entry: TimerEntry

    var body: some View {
        VStack {
            Text(entry.remaining, style: .timer)
                .font(.title2.bold())
            Button(intent: ToggleTimerIntent()) {
                Label(entry.isRunning ? "Pause" : "Start",
                      systemImage: entry.isRunning ? "pause.fill" : "play.fill")
            }
            .buttonStyle(.borderedProminent)
        }
    }
}
```

### Rule 10.2: App Shortcuts for Key Actions
Define App Shortcuts so users can trigger key actions from Siri, Spotlight, and the Shortcuts app.

```swift
struct MyAppShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: StartWorkoutIntent(),
            phrases: ["Start a workout in \(.applicationName)"],
            shortTitle: "Start Workout",
            systemImageName: "figure.run"
        )
    }
}
```

### Rule 10.3: Spotlight Indexing
Index app content with `CSSearchableItem` so users can find it from Spotlight search.

### Rule 10.4: Share Sheet Integration
Support the system share sheet for content that users might want to send elsewhere. Implement `UIActivityItemSource` or use `ShareLink` in SwiftUI.

```swift
ShareLink(item: article.url) {
    Label("Share", systemImage: "square.and.arrow.up")
}
```

### Rule 10.5: Live Activities
Use Live Activities and the Dynamic Island for real-time, time-bound events (delivery tracking, sports scores, workouts).

### Rule 10.6: Handle Interruptions Gracefully
Save state and pause gracefully when interrupted by:
- Phone calls
- Siri invocations
- Notifications
- App switcher
- FaceTime SharePlay

Use `scenePhase` to detect transitions:

```swift
@Environment(\.scenePhase) var scenePhase

.onChange(of: scenePhase) { _, newPhase in
    switch newPhase {
    case .active: resumeActivity()
    case .inactive: pauseActivity()
    case .background: saveState()
    @unknown default: break
    }
}
```

---

## Quick Reference

| Need | Component | Notes |
|------|-----------|-------|
| Top-level sections (3-5) | `TabView` with `.tabItem` | Bottom tab bar, SF Symbols |
| Hierarchical drill-down | `NavigationStack` | Large title on root, inline on children |
| Self-contained task | `.sheet` | Swipe to dismiss, cancel/done buttons |
| Critical decision | `.alert` | 2 buttons preferred, max 3 |
| Secondary actions | `.contextMenu` | Long press; must also be accessible elsewhere |
| Scrolling content | `List` with `.insetGrouped` | 44pt min row, swipe actions |
| Text input | `TextField` / `TextEditor` | Label above, validation below |
| Selection (few options) | `Picker` | Segmented for 2-5, wheel for many |
| Selection (on/off) | `Toggle` | Aligned right in a list row |
| Search | `.searchable` | Suggestions, recent searches |
| Progress (known) | `ProgressView(value:total:)` | Show percentage or time remaining |
| Progress (unknown) | `ProgressView()` | Inline, never full-screen blocking |
| One-time location | `LocationButton` | No persistent permission needed |
| Sharing content | `ShareLink` | System share sheet |
| Haptic feedback | `UIImpactFeedbackGenerator` | `.light`, `.medium`, `.heavy` |
| Destructive action | `Button(role: .destructive)` | Red tint, confirm via alert |

---

## Evaluation Checklist

Use this checklist to audit an iPhone app for HIG compliance:

### Layout & Safe Areas
- [ ] All touch targets are at least 44x44pt
- [ ] No content is clipped under status bar, Dynamic Island, or home indicator
- [ ] Primary actions are in the bottom half of the screen (thumb zone)
- [ ] Layout adapts from iPhone SE to Pro Max without breaking
- [ ] Spacing aligns to the 8pt grid

### Navigation
- [ ] Tab bar is used for 3-5 top-level sections
- [ ] No hamburger/drawer menus
- [ ] Primary views use large titles
- [ ] Swipe-from-left-edge back navigation works throughout
- [ ] State is preserved when switching tabs

### Typography
- [ ] All text uses built-in text styles or custom fonts scaled with Dynamic Type (`Font.custom(_:size:relativeTo:)` in SwiftUI or `UIFontMetrics` in UIKit)
- [ ] Dynamic Type is supported up to accessibility sizes
- [ ] Layouts reflow at large text sizes (no truncation of essential text)
- [ ] Minimum text size is 11pt

### Color & Dark Mode
- [ ] App uses semantic system colors or provides light/dark asset variants
- [ ] Dark Mode looks intentional (not just inverted)
- [ ] No information conveyed by color alone
- [ ] Text contrast meets 4.5:1 (normal) or 3:1 (large)
- [ ] Single accent color for interactive elements

### Accessibility
- [ ] VoiceOver reads all screens logically with meaningful labels
- [ ] Bold Text preference is respected
- [ ] Reduce Motion disables decorative animations
- [ ] Increase Contrast variant exists for custom colors
- [ ] All gestures have alternative access paths

### Components
- [ ] Alerts are used only for critical decisions
- [ ] Sheets have a dismiss path (button and/or swipe)
- [ ] List rows are at least 44pt tall
- [ ] Tab bar is never hidden during navigation
- [ ] Destructive buttons use the `.destructive` role

### Privacy
- [ ] Permissions are requested in context, not at launch
- [ ] Custom explanation shown before each system permission dialog
- [ ] Sign in with Apple offered alongside other providers
- [ ] App is usable without an account for basic features
- [ ] ATT prompt is shown if tracking, and denial is respected

### System Integration
- [ ] Widgets show glanceable, up-to-date information
- [ ] App content is indexed for Spotlight
- [ ] Share Sheet is available for shareable content
- [ ] App handles interruptions (calls, background, Siri) gracefully

---

## Anti-Patterns

These are common mistakes that violate the iOS Human Interface Guidelines. Never do these:

1. **Hamburger menus** — Use a tab bar. Hamburger menus hide navigation and reduce feature discoverability by up to 50%.

2. **Custom back buttons that break swipe-back** — If you replace the back button, ensure the swipe-from-left-edge gesture still works via `NavigationStack`.

3. **Full-screen blocking spinners** — Use skeleton views or inline progress indicators. Blocking spinners make the app feel frozen.

4. **Splash screens with logos** — The launch screen must mirror the first screen of the app. Branding delays feel artificial.

5. **Requesting all permissions at launch** — Asking for camera, location, notifications, and contacts on first launch guarantees most will be denied.

6. **Hardcoded font sizes** — Use text styles. Hardcoded sizes ignore Dynamic Type and accessibility preferences, breaking the app for millions of users.

7. **Using only color to indicate state** — Red/green for valid/invalid excludes colorblind users. Always pair with icons or text.

8. **Alerts for non-critical information** — Alerts interrupt flow and require dismissal. Use banners, toasts, or inline messages for tips and non-critical information.

9. **Hiding the tab bar on push** — Tab bars should remain visible throughout navigation within a tab. Hiding them disorients users.

10. **Ignoring safe areas** — Using `.ignoresSafeArea()` on content views causes text and buttons to disappear under the notch, Dynamic Island, or home indicator.

11. **Non-dismissable modals** — Every modal must have a clear dismiss path (close button, cancel, swipe down). Trapping users in a modal is hostile.

12. **Custom gestures without alternatives** — A three-finger swipe for undo is unusable for many people. Provide a visible button or menu item as well.

13. **Tiny touch targets** — Buttons and links smaller than 44pt cause mis-taps, especially in lists and toolbars.

14. **Stacked modals** — Presenting a sheet on top of a sheet on top of a sheet creates navigation confusion. Use navigation within a single modal instead.

15. **Dark Mode as an afterthought** — Using hardcoded colors means the app is either broken in Dark Mode or light mode. Always use semantic colors.
```

## File: `skills/ios/metadata.json`
```json
{
  "version": "1.0.0",
  "organization": "Platform Design Skills",
  "date": "February 2026",
  "abstract": "Apple Human Interface Guidelines for iPhone apps. 67+ rules across 10 categories covering navigation, layout, typography, color, accessibility, gestures, components, patterns, privacy, and system integration. Each rule includes SwiftUI/UIKit examples with correct and incorrect implementations.",
  "references": [
    "https://developer.apple.com/design/human-interface-guidelines",
    "https://developer.apple.com/design/human-interface-guidelines/designing-for-ios",
    "https://developer.apple.com/documentation/swiftui",
    "https://developer.apple.com/documentation/uikit"
  ]
}
```

## File: `skills/ios/rules/_sections.md`
```markdown
# iOS Design Rule Sections

## 1. Layout & Safe Areas (layout)
**Impact:** CRITICAL
**Description:** Correct layout is foundational to every iPhone app. Violating safe areas causes content to be clipped under the status bar, Dynamic Island, or home indicator. Touch targets below 44pt cause mis-taps and frustration. Bottom-of-screen placement for primary actions respects the natural thumb zone. All layouts must adapt across the full range of iPhone screen sizes from iPhone SE to iPhone Pro Max.

## 2. Navigation (nav)
**Impact:** CRITICAL
**Description:** Navigation defines how users move through an app and directly affects whether they can find features and complete tasks. iOS users expect a tab bar at the bottom for top-level sections, large titles in primary views, and swipe-from-left-edge for back. Violating these conventions forces users to relearn interaction patterns they already know, increasing cognitive load and abandonment. Preserve visible state so users resume by recognition rather than memory.

## 3. Typography & Dynamic Type (type)
**Impact:** HIGH
**Description:** Typography is the primary way information is communicated in most apps. Supporting Dynamic Type is both an accessibility requirement and an App Store expectation. Users who set larger text sizes depend on apps respecting that preference. Using built-in text styles ensures automatic scaling, proper weight, and consistent hierarchy across the system.

## 4. Color & Dark Mode (color)
**Impact:** HIGH
**Description:** Color communicates state, hierarchy, and interactivity. Using semantic system colors ensures automatic Dark Mode support and consistency with the platform. Insufficient contrast makes text unreadable for users with low vision. Relying on color alone excludes colorblind users. A single accent color for interactive elements creates a clear, learnable visual language.

## 5. Accessibility (a11y)
**Impact:** CRITICAL
**Description:** Accessibility is not optional on iOS. VoiceOver is used by hundreds of thousands of users daily. Missing accessibility labels make an app completely unusable for blind users. Supporting Bold Text, Reduce Motion, and Increase Contrast respects user preferences set at the system level. Apps that fail accessibility are also likely to fail App Store review for certain categories.

## 6. Gestures & Input (gesture)
**Impact:** HIGH
**Description:** iOS is a gesture-driven platform. Users expect standard gestures like tap, swipe, pinch, and long press to work consistently. Overriding system gestures (edge swipes, notification pull-down) breaks fundamental navigation and creates confusion. All gesture-based interactions must have alternative access paths for users with motor impairments or those using assistive technologies.

## 7. Components (comp)
**Impact:** HIGH
**Description:** UIKit and SwiftUI provide a rich component library that users already understand. Using standard components correctly reduces learning curve and ensures accessibility, Dynamic Type, and Dark Mode support for free. Misusing components (e.g., alerts for non-critical information, hiding tab bars) violates user expectations and creates friction.

## 8. Patterns (pattern)
**Impact:** MEDIUM
**Description:** Common UX patterns like onboarding, loading, and modality shape the overall feel of an app. Skeleton views instead of blocking spinners make apps feel faster. Launch screens that match the first screen eliminate visual jarring. Limiting onboarding to three skippable pages respects user time. Acknowledge waiting states immediately so the app never appears inert after input. These patterns collectively determine whether an app feels native or foreign.

## 9. Privacy & Permissions (privacy)
**Impact:** HIGH
**Description:** Privacy is a core iOS platform value. Requesting permissions without context causes users to deny access reflexively. Explaining why a permission is needed before the system prompt significantly increases grant rates. Supporting Sign in with Apple and not requiring unnecessary account creation respects user privacy. App Tracking Transparency must be respected — denial is the user's right.

## 10. System Integration (system)
**Impact:** MEDIUM
**Description:** Deep system integration makes an app feel like a natural extension of the iPhone. Widgets provide glanceable information on the home screen. App Shortcuts enable Siri and Spotlight access to key actions. Live Activities surface real-time progress on the Lock Screen. Share Sheet integration lets users move data between apps seamlessly. Handling interruptions gracefully ensures the app works within the broader system context.
```

## File: `skills/ipados/AGENTS.md`
```markdown
# iPadOS Design Guidelines Skill

iPad-specific HIG rules extending iOS patterns for the larger, multitasking-capable canvas.

**Reference**: [Apple HIG - Designing for iPadOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados)

## Categories & Impact

| # | Category | Impact | Key Focus |
|---|----------|--------|-----------|
| 1 | Responsive Layout | CRITICAL | Adaptive layouts, size classes, column-based design |
| 2 | Multitasking | CRITICAL | Split View, Slide Over, Stage Manager, resizable windows |
| 3 | Navigation | CRITICAL | Sidebar, three-column layout, toolbar placement |
| 4 | Pointer & Trackpad | HIGH | Hover effects, magnetism, right-click, drag and drop |
| 5 | Keyboard | HIGH | Cmd shortcuts, discoverability overlay, tab navigation |
| 6 | Apple Pencil | MEDIUM | Scribble, hover detection, PencilKit |
| 7 | Drag and Drop | HIGH | Inter-app, multi-item, spring-loaded, Universal Control |
| 8 | External Display | MEDIUM | Extended content, AirPlay, display lifecycle |
| 9 | Accessibility | CRITICAL | VoiceOver labels, Dynamic Type, pointer accessibility, Full Keyboard Access |

## Key Differentiators from iOS

- **Sidebar replaces tab bar** in regular width size class
- **Multitasking is mandatory** -- app must function at all split sizes
- **Pointer support expected** -- hover states, magnetism, right-click menus
- **Keyboard shortcuts required** -- Cmd+key for all major actions with discoverability overlay
- **Drag and drop across apps** -- first-class interaction pattern
- **Stage Manager** -- freely resizable windows, multiple scenes
- **Toolbar at top** instead of bottom navigation
- **Three-column layouts** for deep hierarchies

## Never Do

- Never scale up an iPhone layout to fill the iPad screen — redesign for the larger canvas
- Never opt out of multitasking — every app must work in Split View and Slide Over
- Never use bottom tab bars in regular width — use sidebar navigation
- Never show popovers as full-screen sheets — anchor popovers to their source element
- Never hardcode pixel dimensions for specific iPad models
- Never omit hover states for interactive elements — trackpad users need visual feedback
- Never override system keyboard shortcuts (Cmd+H, Cmd+Tab, Cmd+Space)
- Never ignore drag and drop — at minimum support dragging text, images, and URLs
- Never block the keyboard from dismissing modal sheets on iPad
- Never present iPhone-style modals when a popover or inspector is more appropriate
- Never omit accessibility labels on icon-only buttons or custom interactive elements
- Never disable Dynamic Type scaling or clamp text size — iPad users rely on large type too
- Never create keyboard focus paths that trap or skip interactive elements in Split View
```

## File: `skills/ipados/SKILL.md`
```markdown
---
name: ipados-design-guidelines
description: Apple Human Interface Guidelines for iPad. Use when building iPad-optimized interfaces, implementing multitasking, pointer support, keyboard shortcuts, or responsive layouts. Triggers on tasks involving iPad, Split View, Stage Manager, sidebar navigation, or trackpad support.
license: MIT
metadata:
  author: platform-design-skills
  version: "1.0.0"
---

# iPadOS Design Guidelines

Comprehensive rules for building iPad-native apps following Apple's Human Interface Guidelines. iPad is not a big iPhone -- it demands adaptive layouts, multitasking support, pointer interactions, keyboard shortcuts, and inter-app drag and drop. These rules extend iOS patterns for the larger, more capable canvas.

---

## 1. Responsive Layout (CRITICAL)

### 1.1 Use Adaptive Size Classes

iPad presents two horizontal size classes: **regular** (full screen, large splits) and **compact** (Slide Over, narrow splits). Design for both. Never hardcode dimensions.

```swift
struct AdaptiveView: View {
    @Environment(\.horizontalSizeClass) var sizeClass

    var body: some View {
        if sizeClass == .regular {
            TwoColumnLayout()
        } else {
            StackedLayout()
        }
    }
}
```

### 1.2 Don't Scale Up iPhone UI

iPad layouts must be purpose-built. Stretching an iPhone layout across a 13" display wastes space and feels wrong. Use multi-column layouts, master-detail patterns, and increased information density in regular width.

### 1.3 Support All iPad Screen Sizes

Design for the full range: iPad Mini (8.3"), iPad (11"), iPad Air (11"/13"), and iPad Pro (11"/13"). Use flexible layouts that redistribute content rather than simply scaling.

### 1.4 Column-Based Layouts for Regular Width

In regular width, organize content into columns. Two-column is the most common (sidebar + detail). Three-column works for deep hierarchies (sidebar + list + detail). Avoid single-column full-width layouts on large screens.

```swift
struct ThreeColumnLayout: View {
    var body: some View {
        NavigationSplitView {
            SidebarView()
        } content: {
            ContentListView()
        } detail: {
            DetailView()
        }
    }
}
```

### 1.5 Respect Safe Areas

iPad safe areas differ from iPhone. Older iPads have no home indicator. iPads in landscape have different insets than portrait. Always use `safeAreaInset` and never hardcode padding for notches or indicators.

### 1.6 Support Both Orientations

iPad apps must work well in both portrait and landscape. Landscape is the dominant orientation for productivity. Portrait is common for reading. Adapt column counts and layout density to orientation.

---

## 2. Multitasking (CRITICAL)

### 2.1 Support Split View

Your app must function correctly at 1/3, 1/2, and 2/3 screen widths in Split View. At 1/3 width, your app receives compact horizontal size class. Content must remain usable at every split ratio.

### 2.2 Support Slide Over

Slide Over presents your app as a compact-width overlay on the right edge. It behaves like an iPhone-width app. Ensure all functionality remains accessible in this narrow mode.

### 2.3 Handle Stage Manager

Stage Manager allows freely resizable windows and multiple windows simultaneously. Your app must:
- Resize fluidly to arbitrary dimensions
- Support multiple scenes (windows) showing different content
- Not assume any fixed size or aspect ratio

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        // Support multiple windows
        WindowGroup("Detail", for: Item.ID.self) { $itemId in
            DetailView(itemId: itemId)
        }
    }
}
```

### 2.4 Never Assume Full Screen

The app may launch directly into Split View or Stage Manager. Do not depend on full-screen dimensions during setup, onboarding, or any flow. Test your app at every possible size.

### 2.5 Handle Size Transitions Gracefully

When the user resizes via multitasking, animate layout changes smoothly. Preserve scroll position, selection state, and user context across size transitions. Never reload content on resize.

### 2.6 Support Multiple Scenes

Use `UIScene` / SwiftUI `WindowGroup` to let users open multiple instances of your app showing different content. Each scene is independent. Support `NSUserActivity` for state restoration.

---

## 3. Navigation (CRITICAL)

### 3.1 Sidebar for Primary Navigation

In regular width, replace the iPhone tab bar with a sidebar. The sidebar provides more room for navigation items, supports sections, and feels native on iPad.

```swift
struct AppNavigation: View {
    @State private var selection: NavigationItem? = .inbox

    var body: some View {
        NavigationSplitView {
            List(selection: $selection) {
                Section("Main") {
                    Label("Inbox", systemImage: "tray")
                        .tag(NavigationItem.inbox)
                    Label("Drafts", systemImage: "doc")
                        .tag(NavigationItem.drafts)
                    Label("Sent", systemImage: "paperplane")
                        .tag(NavigationItem.sent)
                }
                Section("Labels") {
                    // Dynamic sections
                }
            }
            .navigationTitle("Mail")
        } detail: {
            DetailView(for: selection)
        }
    }
}
```

### 3.2 Automatic Tab-to-Sidebar Conversion

SwiftUI `TabView` with `.sidebarAdaptable` style automatically converts to a sidebar in regular width. Use this for seamless iPhone-to-iPad adaptation.

```swift
TabView {
    Tab("Home", systemImage: "house") { HomeView() }
    Tab("Search", systemImage: "magnifyingglass") { SearchView() }
    Tab("Profile", systemImage: "person") { ProfileView() }
}
.tabViewStyle(.sidebarAdaptable)
```

### 3.3 Three-Column Layout for Complex Hierarchies

Use `NavigationSplitView` with three columns when your information architecture has three levels: category > list > detail. Examples: mail (accounts > messages > message), file managers, settings.

### 3.4 Toolbar at Top

On iPad, toolbars live at the top of the screen in the navigation bar area, not at the bottom like iPhone. Place contextual actions in `.toolbar` with appropriate placement.

```swift
.toolbar {
    ToolbarItemGroup(placement: .primaryAction) {
        Button("Compose", systemImage: "square.and.pencil") { }
    }
    ToolbarItemGroup(placement: .secondaryAction) {
        Button("Archive", systemImage: "archivebox") { }
        Button("Delete", systemImage: "trash") { }
    }
}
```

### 3.5 Detail View Should Never Be Empty

When no item is selected in a list/sidebar, show a meaningful empty state in the detail area. Use a placeholder with icon and instruction text, not a blank screen.

### 3.6 Reduce Recall in Large-Canvas Navigation

Keep sidebar selection, search terms, and disclosure state visible and preserved across size changes and scene switches. In multi-column layouts, users should resume from structure on screen, not from memory.

---

## 4. Pointer & Trackpad (HIGH)

### 4.1 Add Hover Effects to Interactive Elements

All tappable elements should respond to pointer hover. The system provides automatic hover effects for standard controls. For custom views, use `.hoverEffect()`.

```swift
Button("Action") { }
    .hoverEffect(.highlight)  // Subtle highlight on hover

// Custom hover effect
MyCustomView()
    .hoverEffect(.lift)  // Lifts and adds shadow
```

### 4.2 Pointer Magnetism on Buttons

The pointer should snap to (be attracted toward) button bounds. Standard UIKit/SwiftUI buttons get this automatically. For custom hit targets, ensure the pointer region matches the tappable area using `.contentShape()`.

### 4.3 Support Right-Click Context Menus

Right-click (secondary click) should present context menus. Use `.contextMenu` which automatically supports both long-press (touch) and right-click (pointer).

```swift
Text(item.title)
    .contextMenu {
        Button("Copy", systemImage: "doc.on.doc") { }
        Button("Share", systemImage: "square.and.arrow.up") { }
        Divider()
        Button("Delete", systemImage: "trash", role: .destructive) { }
    }
```

### 4.4 Trackpad Scroll Behaviors

Support two-finger scrolling with momentum. Pinch to zoom where appropriate. Respect scroll direction preferences. For custom scroll views, ensure trackpad gestures feel natural alongside touch gestures.

### 4.5 Customize Cursor for Content Areas

Change cursor appearance based on context. Text areas show I-beam. Links show pointer hand. Resize handles show resize cursors. Draggable items show grab cursor.

### 4.6 Pointer-Driven Drag and Drop

Pointer users expect click-and-drag for rearranging, selecting, and moving content. Combine with multi-select via Shift-click and Cmd-click.

---

## 5. Keyboard (HIGH)

### 5.1 Cmd+Key Shortcuts for All Major Actions

Every primary action must have a keyboard shortcut. Standard shortcuts are mandatory:

| Shortcut | Action |
|----------|--------|
| Cmd+N | New item |
| Cmd+F | Find/Search |
| Cmd+S | Save |
| Cmd+Z | Undo |
| Cmd+Shift+Z | Redo |
| Cmd+C/V/X | Copy/Paste/Cut |
| Cmd+A | Select all |
| Cmd+P | Print |
| Cmd+W | Close window/tab |
| Cmd+, | Settings/Preferences |
| Delete | Delete selected item |

```swift
Button("New Document") { createDocument() }
    .keyboardShortcut("n", modifiers: .command)
```

### 5.2 Discoverability via Cmd-Hold Overlay

When the user holds the Cmd key, iPadOS shows a shortcut overlay. Register all shortcuts using `.keyboardShortcut()` so they appear in this overlay. Group related shortcuts logically.

### 5.3 Tab Key Navigation Between Fields

Support Tab to move forward and Shift+Tab to move backward between form fields and focusable elements. Use `.focusable()` and `@FocusState` to manage keyboard focus order.

```swift
struct FormView: View {
    @FocusState private var focusedField: Field?

    var body: some View {
        Form {
            TextField("Name", text: $name)
                .focused($focusedField, equals: .name)
            TextField("Email", text: $email)
                .focused($focusedField, equals: .email)
            TextField("Phone", text: $phone)
                .focused($focusedField, equals: .phone)
        }
    }
}
```

### 5.4 Never Override System Shortcuts

Do not claim shortcuts reserved by the system: Cmd+H (Home), Cmd+Tab (App Switcher), Cmd+Space (Spotlight), Globe key combinations. These will not work and create confusion.

### 5.5 Detect Hardware Keyboard

Adapt UI when a hardware keyboard is connected. Hide the on-screen keyboard shortcut bar. Show keyboard-optimized controls. Use `GCKeyboard` or track keyboard visibility to detect state.

### 5.6 Arrow Key Navigation

Support arrow keys for navigating lists, grids, and collections. Combine with Shift for multi-selection. This is essential for productivity-focused apps.

### 5.7 Shortcuts Must Be Discoverable

Do not rely on users memorizing shortcut vocabularies. Expose commands through the Cmd-hold overlay, menu labels, and visible focus movement so people learn shortcuts by recognition and repetition.

---

## 6. Apple Pencil (MEDIUM)

### 6.1 Support Scribble

iPadOS converts handwriting to text in any standard text field automatically. Do not disable Scribble. For custom text input, adopt `UIScribbleInteraction`. Test that Scribble works in all text entry points.

### 6.2 Double-Tap Tool Switching

Apple Pencil 2 and later supports double-tap to switch tools (e.g., pen to eraser). If your app has drawing tools, implement the `UIPencilInteraction` delegate to handle double-tap.

### 6.3 Pressure and Tilt for Drawing

For drawing apps, respond to `force` (pressure) and `altitudeAngle`/`azimuthAngle` (tilt) from pencil touch events. Use these for variable line width, opacity, or shading.

### 6.4 Hover Detection (M2+ Pencil)

Apple Pencil with hover (M2 iPad Pro and later) provides position data before the pencil touches the screen. Use this for preview effects, tool size indicators, and enhanced precision.

```swift
// UIKit hover support via UIHoverGestureRecognizer
let hoverRecognizer = UIHoverGestureRecognizer(target: self, action: #selector(pencilHoverChanged(_:)))
hoverRecognizer.allowedTouchTypes = [NSNumber(value: UITouch.TouchType.pencil.rawValue)]
canvas.addGestureRecognizer(hoverRecognizer)

@objc func pencilHoverChanged(_ hover: UIHoverGestureRecognizer) {
    let location = hover.location(in: canvas)
    showBrushPreview(at: location)
}
```

### 6.5 PencilKit Integration

For note-taking and annotation, use `PKCanvasView` from PencilKit. It provides a full drawing experience with tool picker, undo, and ink recognition out of the box.

```swift
import PencilKit

struct DrawingView: UIViewRepresentable {
    @Binding var canvasView: PKCanvasView

    func makeUIView(context: Context) -> PKCanvasView {
        canvasView.tool = PKInkingTool(.pen, color: .black, width: 5)
        canvasView.drawingPolicy = .anyInput
        return canvasView
    }
}
```

---

## 7. Drag and Drop (HIGH)

### 7.1 Inter-App Drag and Drop is Expected

iPad users expect to drag content between apps. Support dragging content out (as a source) and dropping content in (as a destination). This is a core iPad interaction.

```swift
// As drag source
Text(item.title)
    .draggable(item.title)

// As drop destination
DropTarget()
    .dropDestination(for: String.self) { items, location in
        handleDrop(items)
        return true
    }
```

### 7.2 Multi-Item Drag

Users can pick up one item, then tap additional items to add them to the drag. Support multi-item drag by providing multiple `NSItemProvider` items. Show a badge count on the drag preview.

### 7.3 Spring-Loaded Interactions

When dragging over a navigation element (folder, tab, sidebar item), pause briefly to "spring open" that destination. Implement spring-loading on navigation containers to enable deep drop targets.

### 7.4 Visual Feedback for Drag and Drop

Provide clear visual states:
- **Lift**: Item lifts with shadow when drag begins
- **Move**: Destination highlights when drag hovers over valid target
- **Drop**: Animate insertion at drop point
- **Cancel**: Item animates back to origin

### 7.5 Support Universal Control

Universal Control lets users drag between iPad and Mac. If your app supports drag and drop with standard `NSItemProvider` and UTTypes, Universal Control works automatically.

### 7.6 Drop Delegates for Custom Behavior

Use `DropDelegate` for fine-grained control over drop behavior: validating drop content, reordering within lists, and handling drop position.

```swift
struct ReorderDropDelegate: DropDelegate {
    let item: Item
    @Binding var items: [Item]
    @Binding var draggedItem: Item?

    func performDrop(info: DropInfo) -> Bool {
        draggedItem = nil
        return true
    }

    func dropEntered(info: DropInfo) {
        guard let draggedItem,
              let fromIndex = items.firstIndex(of: draggedItem),
              let toIndex = items.firstIndex(of: item) else { return }
        withAnimation {
            items.move(fromOffsets: IndexSet(integer: fromIndex),
                      toOffset: toIndex > fromIndex ? toIndex + 1 : toIndex)
        }
    }
}
```

---

## 8. External Display (MEDIUM)

### 8.1 Provide Extended Content, Not Just Mirroring

When connected to an external display, show complementary content rather than duplicating the iPad screen. Presentations, reference material, or expanded views belong on the external display while controls stay on iPad.

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        // Additional scene for external display
        WindowGroup(id: "presentation") {
            PresentationView()
        }
    }
}
```

### 8.2 Handle Display Connection and Disconnection

Observe external display lifecycle via `UIWindowScene` events in your `SceneDelegate` or by listening for `UIScene` session notifications (`UIApplication.didConnectSceneSessionNotification` / `UIApplication.didDisconnectSceneSessionNotification`). Transition gracefully — if the external display disconnects mid-presentation, bring content back to the iPad screen without data loss.

```swift
// SceneDelegate: detect when a scene (external display window) connects or disconnects
func scene(_ scene: UIScene,
           willConnectTo session: UISceneSession,
           options connectionOptions: UIScene.ConnectionOptions) {
    guard let windowScene = scene as? UIWindowScene else { return }
    configureExternalDisplay(for: windowScene)
}

func sceneDidDisconnect(_ scene: UIScene) {
    restoreContentToiPad()
}
```

### 8.3 Support Full External Display Resolution

Use the full resolution and aspect ratio of the external display. Do not letterbox or pillarbox your content. In iOS 16+ multi-scene contexts, `UIScreen.main` is deprecated — query the connected display via `UIWindowScene.coordinateSpace.bounds` and `UIWindowScene.screen.scale`, or use `@Environment(\.displayScale)` in SwiftUI.

---

## 9. Accessibility (CRITICAL)

**Impact:** CRITICAL

### Rule 9.1: VoiceOver Labels on All Interactive Elements

Every button, control, and interactive element must have a meaningful accessibility label. Icon-only toolbar items and custom views must use `.accessibilityLabel()`.

**Correct:**
```swift
Button(action: compose) {
    Image(systemName: "square.and.pencil")
}
.accessibilityLabel("Compose new message")
```

**Incorrect:**
```swift
Button(action: compose) {
    Image(systemName: "square.and.pencil")
}
// VoiceOver reads "square.and.pencil" — meaningless to users
```

### Rule 9.2: Support Dynamic Type Including Accessibility Sizes

Use semantic text styles (`title`, `body`, `caption`) so text scales with the user's preferred size. In iPad's larger canvas, never clamp text size or disable scaling. Test up to the five accessibility size steps.

```swift
Text("Section Header")
    .font(.headline)  // Scales with Dynamic Type automatically
```

### Rule 9.3: Pointer Accessibility — Hover Must Not Be the Only Cue

Hover states (`.hoverEffect`) enhance pointer input but must not be the sole indicator of interactivity. Ensure all interactive elements are also distinguishable via color, shape, or label for VoiceOver and keyboard-only users.

### Rule 9.4: Full Keyboard Access and Focus Routing

With Full Keyboard Access enabled, Tab must move focus through all interactive elements in logical order. In Split View and multi-window layouts, focus must not escape to a hidden or occluded window. Use `@FocusState` and `.focusable()` to control the keyboard focus graph.

```swift
struct FormView: View {
    @FocusState private var focusedField: Field?

    var body: some View {
        VStack {
            TextField("Name", text: $name)
                .focused($focusedField, equals: .name)
            TextField("Email", text: $email)
                .focused($focusedField, equals: .email)
        }
    }
}
```

### Rule 9.5: VoiceOver in Split View — Separate Focus Contexts

In Split View, each app has its own VoiceOver focus context. Your app must not assume it occupies the full screen. Ensure VoiceOver can navigate your entire visible interface even at 1/3 or 1/2 split width. Do not hide actionable content outside the visible region without also removing it from the accessibility tree.

### Rule 9.6: Respond to Bold Text

When the user enables Bold Text in Settings, custom-rendered text must adapt. SwiftUI text styles handle this automatically. UIKit code must check `UIAccessibility.isBoldTextEnabled` or use `@Environment(\.legibilityWeight)` in SwiftUI.

**Correct:**
```swift
// SwiftUI — handled automatically for standard text styles
Text("Section Header")
    .font(.headline)

// SwiftUI — custom rendering respects legibilityWeight
@Environment(\.legibilityWeight) var legibilityWeight

var body: some View {
    Text("Custom Label")
        .fontWeight(legibilityWeight == .bold ? .bold : .regular)
}
```

**Incorrect:**
```swift
// Hardcoded weight ignores Bold Text preference
label.font = UIFont.systemFont(ofSize: 17, weight: .regular)
// Missing: re-query font when UIAccessibility.boldTextStatusDidChangeNotification fires
```

### Rule 9.7: Respond to Increase Contrast

When the user enables Increase Contrast in Settings, custom colors must provide higher-contrast variants. Use `@Environment(\.colorSchemeContrast)` in SwiftUI or `UIAccessibility.isDarkerSystemColorsEnabled` in UIKit.

**Correct:**
```swift
// SwiftUI
@Environment(\.colorSchemeContrast) var contrast

var separatorColor: Color {
    contrast == .increased ? Color.primary : Color.secondary
}

// UIKit
let useHighContrast = UIAccessibility.isDarkerSystemColorsEnabled
let borderColor: UIColor = useHighContrast ? .label : .separator
```

**Incorrect:**
```swift
// Static color ignores Increase Contrast setting
let borderColor = UIColor.separator // Always low-contrast; ignores user preference
```

---

## Evaluation Checklist

Use this checklist to verify iPad-readiness:

### Layout & Multitasking
- [ ] App uses adaptive layout with `horizontalSizeClass`
- [ ] Tested at all Split View ratios (1/3, 1/2, 2/3)
- [ ] Tested in Slide Over (compact width)
- [ ] Stage Manager: resizes fluidly to arbitrary dimensions
- [ ] Multiple scenes/windows supported
- [ ] Both orientations (portrait and landscape) work correctly
- [ ] No content clipped at any size
- [ ] Safe areas respected on all iPad models

### Navigation
- [ ] Sidebar visible in regular width
- [ ] Tab bar used in compact width
- [ ] Detail view shows placeholder when no selection
- [ ] Toolbar items placed at top, not bottom
- [ ] Three-column layout used where appropriate

### Pointer & Trackpad
- [ ] Hover effects on all interactive elements
- [ ] Right-click context menus available
- [ ] Pointer cursor adapts to content (I-beam for text, etc.)
- [ ] Click-and-drag works for reordering

### Keyboard
- [ ] Cmd+key shortcuts for all major actions
- [ ] Shortcuts appear in Cmd-hold overlay
- [ ] Tab key navigates between form fields
- [ ] No system shortcut conflicts
- [ ] Arrow keys navigate lists and grids
- [ ] Return/Enter activates default action

### Apple Pencil
- [ ] Scribble works in all text fields
- [ ] Drawing apps support pressure and tilt
- [ ] Double-tap interaction handled (if applicable)

### Drag and Drop
- [ ] Content can be dragged out to other apps
- [ ] Content can be dropped in from other apps
- [ ] Multi-item drag supported
- [ ] Visual feedback for all drag states

### External Display
- [ ] Extended content shown (not just mirror)
- [ ] Graceful handling of connect/disconnect

### Accessibility
- [ ] VoiceOver labels on all icon-only buttons and custom interactive elements
- [ ] Text uses semantic type styles and scales with Dynamic Type (including accessibility sizes)
- [ ] All functionality reachable with Full Keyboard Access (Tab navigation, logical focus order)
- [ ] Interactive elements are distinguishable without relying solely on hover state
- [ ] VoiceOver navigates correctly at all Split View widths
- [ ] Bold Text preference respected (SwiftUI handles automatically; UIKit checks `UIAccessibility.isBoldTextEnabled`)
- [ ] Increase Contrast preference respected (custom colors provide higher-contrast variants via `colorSchemeContrast` or `isDarkerSystemColorsEnabled`)

---

## Anti-Patterns

### DO NOT: Scale Up iPhone Layouts
Stretching a single-column iPhone UI to fill an iPad screen wastes space, looks lazy, and provides a poor experience. Always redesign for the larger canvas.

### DO NOT: Disable Multitasking
Never opt out of multitasking support. Users expect every app to work in Split View and Slide Over. Requiring full screen is hostile to iPad workflows.

### DO NOT: Ignore the Keyboard
Many iPad users have Magic Keyboard or Smart Keyboard. An app with no keyboard shortcuts forces them to reach for the screen constantly. Provide shortcuts for all frequent actions.

### DO NOT: Use iPhone-Style Bottom Tab Bars in Regular Width
Tab bars at the bottom waste vertical space on iPad and look out of place. Convert to sidebar navigation in regular width. SwiftUI does this automatically with `.sidebarAdaptable`.

### DO NOT: Show Popovers as Full-Screen Sheets
On iPad, popovers should anchor to their source element as floating panels. Only use full-screen sheets for immersive content or flows that genuinely need the full screen. Avoid the iPhone pattern of everything being a sheet.

### DO NOT: Ignore Pointer Hover States
Missing hover effects make the app feel broken when using a trackpad. Users cannot tell what is interactive. Always add hover feedback to custom interactive elements.

### DO NOT: Hardcode Dimensions
Never hardcode widths, heights, or positions based on a specific iPad model. Use Auto Layout constraints, SwiftUI flexible frames, and `GeometryReader` for dynamic sizing.

### DO NOT: Forget Drag and Drop
On iPad, drag and drop between apps is a core workflow. Not supporting it makes your app a dead end for content. At minimum, support dragging text, images, and URLs in and out.

### DO NOT: Override System Keyboard Shortcuts
Claiming Cmd+H, Cmd+Tab, Cmd+Space, or Globe shortcuts will not work and confuses users who expect system behavior. Check Apple's reserved shortcuts list before assigning.

### DO NOT: Present Dense Content Without Scrolling
Large iPad screens tempt designers to show everything at once. Content should still scroll when it exceeds the visible area. Never truncate content to avoid scrolling.
```

## File: `skills/ipados/metadata.json`
```json
{
  "version": "1.0.0",
  "organization": "Platform Design Skills",
  "date": "February 2026",
  "abstract": "Apple Human Interface Guidelines for iPad apps. 50+ rules across 9 categories covering multitasking, pointer support, sidebar navigation, keyboard shortcuts, Stage Manager, responsive layout, accessibility, and iPad-specific adaptations. Extends iOS patterns for the larger canvas.",
  "references": [
    "https://developer.apple.com/design/human-interface-guidelines",
    "https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados",
    "https://developer.apple.com/documentation/swiftui",
    "https://developer.apple.com/documentation/uikit"
  ]
}
```

## File: `skills/ipados/rules/_sections.md`
```markdown
# iPadOS Design Guidelines - Sections

## Section 1: Responsive Layout
- **Impact**: CRITICAL
- **Scope**: Adaptive layouts, size classes, column-based design, safe areas, all iPad screen sizes
- **Applies when**: Building any iPad UI, handling regular/compact width transitions, supporting iPad Mini through 13" Pro

## Section 2: Multitasking
- **Impact**: CRITICAL
- **Scope**: Split View, Slide Over, Stage Manager, resizable windows, multiple scenes
- **Applies when**: App runs alongside other apps, user resizes windows, app enters compact width via multitasking

## Section 3: Navigation
- **Impact**: CRITICAL
- **Scope**: Sidebar navigation, tab-to-sidebar conversion, three-column layout, toolbar placement, detail views, preserved visible hierarchy and state
- **Applies when**: Designing primary navigation, building information hierarchies, placing toolbars and actions

## Section 4: Pointer & Trackpad
- **Impact**: HIGH
- **Scope**: Hover effects, pointer magnetism, right-click context menus, scroll behaviors, cursor customization, pointer-driven drag and drop
- **Applies when**: Any interactive element needs pointer adaptation, supporting Magic Keyboard or trackpad input

## Section 5: Keyboard
- **Impact**: HIGH
- **Scope**: Cmd+key shortcuts, discoverability overlay, tab navigation, hardware keyboard detection, system shortcut conflicts, shortcut learnability
- **Applies when**: Adding keyboard shortcuts, building forms, supporting hardware keyboard users

## Section 6: Apple Pencil
- **Impact**: MEDIUM
- **Scope**: Scribble handwriting input, double-tap tool switching, pressure/tilt sensitivity, hover detection, PencilKit
- **Applies when**: Building drawing or note-taking features, supporting handwriting input in text fields

## Section 7: Drag and Drop
- **Impact**: HIGH
- **Scope**: Inter-app drag and drop, multi-item selection, spring-loaded interactions, Universal Control, drop delegates
- **Applies when**: Content can be moved between apps, supporting file/image/text transfers, building content organization features

## Section 8: External Display
- **Impact**: MEDIUM
- **Scope**: Extended display content, AirPlay support, display connection/disconnection handling
- **Applies when**: App supports presentation mode, external monitors, or AirPlay output

## Section 9: Accessibility
- **Impact**: CRITICAL
- **Scope**: VoiceOver labels, Dynamic Type scaling, pointer accessibility, Full Keyboard Access, Split View focus routing, Bold Text, Increase Contrast
- **Applies when**: Building any interactive element, supporting keyboard users, testing with assistive technologies, adapting UI across split widths
- **Rules**: 9.1 VoiceOver labels, 9.2 Dynamic Type, 9.3 Hover accessibility, 9.4 Full Keyboard Access, 9.5 VoiceOver in Split View, 9.6 Bold Text, 9.7 Increase Contrast
```

## File: `skills/macos/AGENTS.md`
```markdown
# macOS Design Guidelines — Agent Instructions

## Purpose

This skill provides Apple Human Interface Guidelines for macOS. Apply these rules when building, reviewing, or designing Mac apps using SwiftUI or AppKit.

## When to Apply

- Building any macOS application
- Reviewing Mac UI code or designs
- Implementing menu bars, toolbars, sidebars, or window management
- Adding keyboard shortcuts or pointer interactions
- Porting iOS apps to Mac via Catalyst or Designed for iPad
- Evaluating desktop app usability

## How to Use

1. Read `SKILL.md` for the full rule set with code examples
2. Read `rules/_sections.md` for the categorized quick-reference
3. Use the evaluation checklist in SKILL.md before shipping

## Priority

Rules marked CRITICAL must never be skipped. Rules marked HIGH should be followed unless there is a documented reason. Rules marked MEDIUM are strong recommendations.

## Rule Categories

| # | Category | Impact |
|---|----------|--------|
| 1 | Menu Bar | CRITICAL |
| 2 | Windows | CRITICAL |
| 3 | Toolbars | HIGH |
| 4 | Sidebars | HIGH |
| 5 | Keyboard | CRITICAL |
| 6 | Pointer and Mouse | HIGH |
| 7 | Notifications and Alerts | MEDIUM |
| 8 | System Integration | MEDIUM |
| 9 | Visual Design | HIGH |
| 10 | Popovers | MEDIUM |
| 11 | Accessibility | CRITICAL |

## Key Principles

- Mac users expect menu bars, keyboard shortcuts, and multi-window support
- Every destructive action needs Cmd+Z undo
- Toolbars and sidebars should be user-customizable
- Respect system appearance (Dark Mode, accent color, font size)
- Support drag and drop everywhere it makes sense
- Desktop apps are power-user tools — don't hide functionality behind discoverability walls

## Never Do

- Never ship without a menu bar
- Never use hamburger menus — use the menu bar or a sidebar
- Never place a tab bar at the bottom of the screen
- Never hardcode colors — use semantic system colors for Dark Mode compatibility
- Never build non-resizable main windows
- Never omit keyboard shortcuts for common actions
- Never block full keyboard navigation — no keyboard traps
- Never override traffic light buttons or window chrome
- Never use floating action buttons — use toolbar and menu bar actions
- Never ignore VoiceOver — every control needs an accessibility label
```

## File: `skills/macos/SKILL.md`
```markdown
---
name: macos-design-guidelines
description: Apple Human Interface Guidelines for Mac. Use when building macOS apps with SwiftUI or AppKit, implementing menu bars, toolbars, window management, or keyboard shortcuts. Triggers on tasks involving Mac UI, desktop apps, or Mac Catalyst.
license: MIT
metadata:
  author: platform-design-skills
  version: "1.0.0"
---

# macOS Human Interface Guidelines

Mac apps serve power users who expect deep keyboard control, persistent menu bars, resizable multi-window layouts, and tight system integration. These guidelines codify Apple's HIG into actionable rules with SwiftUI and AppKit examples.

---

## 1. Menu Bar (CRITICAL)

Every Mac app must have a menu bar. It is the primary discovery mechanism for commands. Users who cannot find a feature will look in the menu bar before anywhere else.

### Rule 1.1 — Provide Standard Menus

Every app must include at minimum: **App**, **File**, **Edit**, **View**, **Window**, **Help**. Omit File only if the app is not document-based. Add app-specific menus between Edit and View or between View and Window.

```swift
// SwiftUI — Standard menu structure
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .commands {
            // Adds to existing standard menus
            CommandGroup(after: .newItem) {
                Button("New from Template...") { newFromTemplate() }
                    .keyboardShortcut("T", modifiers: [.command, .shift])
            }
            CommandMenu("Canvas") {
                Button("Zoom to Fit") { zoomToFit() }
                    .keyboardShortcut("0", modifiers: .command)
                Divider()
                Button("Add Artboard") { addArtboard() }
                    .keyboardShortcut("A", modifiers: [.command, .shift])
            }
        }
    }
}
```

```swift
// AppKit — Building menus programmatically
let editMenu = NSMenu(title: "Edit")
let undoItem = NSMenuItem(title: "Undo", action: #selector(UndoManager.undo), keyEquivalent: "z")
let redoItem = NSMenuItem(title: "Redo", action: #selector(UndoManager.redo), keyEquivalent: "Z")
editMenu.addItem(undoItem)
editMenu.addItem(redoItem)
editMenu.addItem(.separator())
```

### Rule 1.2 — Keyboard Shortcuts for All Menu Items

Every menu item that performs an action must have a keyboard shortcut. Use standard shortcuts for standard actions (Cmd+C, Cmd+V, Cmd+Z, etc.). Custom shortcuts should use Cmd plus a letter. Reserve Cmd+Shift, Cmd+Option, and Cmd+Ctrl combos for secondary actions.

**Standard Shortcut Reference:**

| Action | Shortcut |
|--------|----------|
| New | Cmd+N |
| Open | Cmd+O |
| Close | Cmd+W |
| Save | Cmd+S |
| Save As | Cmd+Shift+S |
| Print | Cmd+P |
| Undo | Cmd+Z |
| Redo | Cmd+Shift+Z |
| Cut | Cmd+X |
| Copy | Cmd+C |
| Paste | Cmd+V |
| Select All | Cmd+A |
| Find | Cmd+F |
| Find Next | Cmd+G |
| Preferences/Settings | Cmd+, |
| Hide App | Cmd+H |
| Quit | Cmd+Q |
| Minimize | Cmd+M |
| Fullscreen | Cmd+Ctrl+F |

### Rule 1.3 — Dynamic Menu Updates

Menu items must reflect current state. Disable items that are not applicable. Update titles to match context (e.g., "Undo Typing" not just "Undo"). Toggle checkmarks for on/off states.

```swift
// SwiftUI — Add sidebar toggle alongside existing toolbar menu commands
CommandGroup(after: .toolbar) {
    Button(showingSidebar ? "Hide Sidebar" : "Show Sidebar") {
        showingSidebar.toggle()
    }
    .keyboardShortcut("S", modifiers: [.command, .control])
}
```

```swift
// AppKit — Validate menu items
override func validateMenuItem(_ menuItem: NSMenuItem) -> Bool {
    if menuItem.action == #selector(delete(_:)) {
        menuItem.title = selectedItems.count > 1 ? "Delete \(selectedItems.count) Items" : "Delete"
        return !selectedItems.isEmpty
    }
    return super.validateMenuItem(menuItem)
}
```

### Rule 1.4 — Contextual Menus

Provide right-click context menus on all interactive elements. Context menus should contain the most relevant subset of menu bar actions for the clicked element, plus element-specific actions.

```swift
// SwiftUI
Text(item.name)
    .contextMenu {
        Button("Rename...") { rename(item) }
        Button("Duplicate") { duplicate(item) }
        Divider()
        Button("Delete", role: .destructive) { delete(item) }
    }
```

### Rule 1.5 — App Menu Structure

The App menu (leftmost, bold app name) must contain: About, Preferences/Settings (Cmd+,), Services submenu, Hide App (Cmd+H), Hide Others (Cmd+Option+H), Show All, Quit (Cmd+Q). Never rename or remove these standard items.

```swift
// SwiftUI — Settings scene
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup { ContentView() }
        Settings { SettingsView() }  // Automatically wired to Cmd+,
    }
}
```

### Rule 1.6 — Stable Command Names and Locations

Treat the menu bar as the app's command memory. Keep common actions in consistent menus with stable names and shortcuts so users recognize them quickly instead of searching for context-specific variants.

---

## 2. Windows (CRITICAL)

Mac users expect full control over window size, position, and lifecycle. An app that fights window management feels fundamentally broken on the Mac.

### Rule 2.1 — Resizable with Sensible Minimums

All main windows must be freely resizable. Set a minimum size that keeps the UI usable. Never set a maximum size unless the content truly cannot scale (rare).

```swift
// SwiftUI
WindowGroup {
    ContentView()
        .frame(minWidth: 600, minHeight: 400)
}
.defaultSize(width: 900, height: 600)
```

```swift
// AppKit
window.minSize = NSSize(width: 600, height: 400)
window.setContentSize(NSSize(width: 900, height: 600))
```

### Rule 2.2 — Support Fullscreen and Split View

Opt into native fullscreen by setting the appropriate window collection behavior. The green traffic-light button must either enter fullscreen or show the tile picker.

```swift
// AppKit
window.collectionBehavior.insert(.fullScreenPrimary)
```

SwiftUI windows get fullscreen support automatically.

### Rule 2.3 — Multiple Windows

Unless your app is a single-purpose utility, support multiple windows. Document-based apps must allow multiple documents open simultaneously. Use `WindowGroup` or `DocumentGroup` in SwiftUI.

```swift
// SwiftUI — Document-based app
@main
struct TextEditorApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextDocument()) { file in
            TextEditorView(document: file.$document)
        }
    }
}
```

### Rule 2.4 — Title Bar Shows Document Info

For document-based apps, the title bar must show the document name. Support proxy icon dragging. Show edited state (dot in close button). Support title bar renaming on click.

```swift
// AppKit
window.representedURL = document.fileURL
window.title = document.displayName
window.isDocumentEdited = document.hasUnsavedChanges
```

```swift
// SwiftUI — NavigationSplitView titles
NavigationSplitView {
    SidebarView()
} detail: {
    DetailView()
        .navigationTitle(document.name)
}
```

### Rule 2.5 — Remember Window State

Persist window position, size, and state across launches. Use `NSWindow.setFrameAutosaveName` or SwiftUI's built-in state restoration.

```swift
// AppKit
window.setFrameAutosaveName("MainWindow")

// SwiftUI — Automatic with WindowGroup
WindowGroup(id: "main") {
    ContentView()
}
.defaultPosition(.center)
```

### Rule 2.6 — Traffic Light Buttons

Never hide or reposition the close (red), minimize (yellow), or zoom (green) buttons. They must remain in the top-left corner. If using a custom title bar, the buttons must still be visible and functional.

```swift
// AppKit — Custom title bar that preserves traffic lights
window.titlebarAppearsTransparent = true
window.styleMask.insert(.fullSizeContentView)
// Traffic lights remain functional and visible
```

---

## 3. Toolbars (HIGH)

Toolbars are the secondary command surface after the menu bar. They provide quick access to frequent actions and should be customizable.

### Rule 3.1 — Unified Title Bar and Toolbar

Use the unified title bar + toolbar style for a modern appearance. The toolbar sits in the title bar area, saving vertical space.

```swift
// SwiftUI
WindowGroup {
    ContentView()
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                Button(action: compose) {
                    Label("Compose", systemImage: "square.and.pencil")
                }
            }
        }
}
.windowToolbarStyle(.unified)
```

```swift
// AppKit
window.titleVisibility = .hidden
window.toolbarStyle = .unified
```

### Rule 3.2 — User-Customizable Toolbars

Allow users to add, remove, and rearrange toolbar items. Provide a default set and a superset of available items.

```swift
// SwiftUI — Customizable toolbar
.toolbar(id: "main") {
    ToolbarItem(id: "compose", placement: .primaryAction) {
        Button(action: compose) {
            Label("Compose", systemImage: "square.and.pencil")
        }
    }
    ToolbarItem(id: "filter", placement: .secondaryAction) {
        Button(action: toggleFilter) {
            Label("Filter", systemImage: "line.3.horizontal.decrease")
        }
    }
}
.toolbarRole(.editor)
```

### Rule 3.3 — Segmented Controls for View Switching

Use a segmented control or picker in the toolbar for switching between content views (e.g., List/Grid/Column). This is a toolbar pattern, not a tab bar.

```swift
// SwiftUI
ToolbarItem(placement: .principal) {
    Picker("View Mode", selection: $viewMode) {
        Label("List", systemImage: "list.bullet").tag(ViewMode.list)
        Label("Grid", systemImage: "square.grid.2x2").tag(ViewMode.grid)
        Label("Column", systemImage: "rectangle.split.3x1").tag(ViewMode.column)
    }
    .pickerStyle(.segmented)
}
```

### Rule 3.4 — Search Field in Toolbar

Place the search field in the trailing area of the toolbar. Use `.searchable()` in SwiftUI for standard search behavior with suggestions and tokens.

```swift
// SwiftUI
NavigationSplitView {
    SidebarView()
} detail: {
    ContentListView()
        .searchable(text: $searchText, placement: .toolbar, prompt: "Search items")
        .searchSuggestions {
            ForEach(suggestions) { suggestion in
                Text(suggestion.title).searchCompletion(suggestion.title)
            }
        }
}
```

### Rule 3.5 — Toolbar Labels and Icons

Toolbar items should have both an icon (SF Symbol) and a text label. In compact mode, show icons only. Prefer labeled icons for discoverability. Use `Label` to supply both.

---

## 4. Sidebars (HIGH)

Sidebars are the primary navigation surface for Mac apps. They appear on the leading edge and provide persistent access to top-level sections and content libraries.

### Rule 4.1 — Leading Edge, Collapsible

Place the sidebar on the left (leading) edge. Make it collapsible via the toolbar button or a keyboard shortcut. Apple does not define a universal sidebar shortcut — choose one appropriate for your app (e.g., Cmd+Ctrl+S is common but not guaranteed to be free in all apps). Persist collapsed state.

```swift
// SwiftUI
NavigationSplitView(columnVisibility: $columnVisibility) {
    List(selection: $selection) {
        Section("Library") {
            Label("All Items", systemImage: "tray.full")
            Label("Favorites", systemImage: "star")
            Label("Recent", systemImage: "clock")
        }
        Section("Tags") {
            ForEach(tags) { tag in
                Label(tag.name, systemImage: "tag")
            }
        }
    }
    .navigationSplitViewColumnWidth(min: 180, ideal: 220, max: 320)
} detail: {
    DetailView(selection: selection)
}
.navigationSplitViewStyle(.prominentDetail)
```

### Rule 4.2 — Source List Style

Use the source list style (`.listStyle(.sidebar)`) for content-library navigation. Source lists have a translucent background that shows the desktop or window behind them with vibrancy effects.

```swift
// SwiftUI
List(selection: $selection) {
    ForEach(sections) { section in
        Section(section.name) {
            ForEach(section.items) { item in
                NavigationLink(value: item) {
                    Label(item.name, systemImage: item.icon)
                }
            }
        }
    }
}
.listStyle(.sidebar)
```

### Rule 4.3 — Outline Views for Hierarchies

When content is hierarchical (e.g., folder trees, project structures), use disclosure groups or outline views to let users expand and collapse levels.

```swift
// SwiftUI — Recursive outline
List(selection: $selection) {
    OutlineGroup(rootNodes, children: \.children) { node in
        Label(node.name, systemImage: node.icon)
    }
}
```

### Rule 4.4 — Drag to Reorder

Sidebar items that can be reordered (bookmarks, favorites, custom sections) must support drag-to-reorder. Implement `onMove` or `NSOutlineView` drag delegates.

```swift
// SwiftUI
ForEach(favorites) { item in
    Label(item.name, systemImage: item.icon)
}
.onMove { source, destination in
    favorites.move(fromOffsets: source, toOffset: destination)
}
```

### Rule 4.5 — Badge Counts

Show badge counts on sidebar items for unread counts, pending items, or notifications. Use the `.badge()` modifier.

```swift
// SwiftUI
Label("Inbox", systemImage: "tray")
    .badge(unreadCount)
```

---

## 5. Keyboard (CRITICAL)

Mac users rely on keyboard shortcuts more than any other platform. An app without comprehensive keyboard support is a broken Mac app.

### Rule 5.1 — Cmd Shortcuts for Everything

Every action reachable by mouse must have a keyboard equivalent. Primary actions use Cmd+letter. Secondary actions use Cmd+Shift or Cmd+Option. Tertiary actions use Cmd+Ctrl.

**Keyboard Shortcut Conventions:**

| Modifier Pattern | Usage |
|-----------------|-------|
| Cmd+letter | Primary actions (New, Open, Save, etc.) |
| Cmd+Shift+letter | Variant of primary (Save As, Find Previous) |
| Cmd+Option+letter | Alternative mode (Paste and Match Style) |
| Cmd+Ctrl+letter | Window/view controls (Fullscreen, Sidebar) |
| Ctrl+letter | Emacs-style text navigation (acceptable) |
| Fn+key | System functions (F11 Show Desktop, etc.) |

### Rule 5.2 — Full Keyboard Navigation

Support Tab to move between controls. Support arrow keys within lists, grids, and tables. Support Shift+Tab for reverse navigation. Use `focusable()` and `@FocusState` in SwiftUI.

```swift
// SwiftUI — Focus management
struct ContentView: View {
    @FocusState private var focusedField: Field?

    var body: some View {
        VStack {
            TextField("Name", text: $name)
                .focused($focusedField, equals: .name)
            TextField("Email", text: $email)
                .focused($focusedField, equals: .email)
        }
        .onSubmit { advanceFocus() }
    }
}
```

### Rule 5.3 — Escape to Cancel or Close

Esc must dismiss popovers, sheets, dialogs, and cancel in-progress operations. In text fields, Esc reverts to the previous value. In modal dialogs, Esc is equivalent to clicking Cancel.

```swift
// SwiftUI — Sheet with Esc support (automatic)
.sheet(isPresented: $showingSheet) {
    SheetView()  // Esc dismisses automatically
}

// AppKit — Custom responder
override func cancelOperation(_ sender: Any?) {
    dismiss(nil)
}
```

### Rule 5.4 — Return for Default Action

In dialogs and forms, Return/Enter activates the default button (visually emphasized in blue). The default button is always the safest primary action.

```swift
// SwiftUI
Button("Save") { save() }
    .keyboardShortcut(.defaultAction)  // Enter key

Button("Cancel") { cancel() }
    .keyboardShortcut(.cancelAction)   // Esc key
```

### Rule 5.5 — Delete for Removal

The Delete key (Backspace) must remove selected items in lists, tables, and collections. Cmd+Delete for more destructive removal (move to Trash). Always support Cmd+Z to undo deletion.

### Rule 5.6 — Space for Quick Look

When items support previewing, Space bar should invoke Quick Look. Use the `QLPreviewPanel` API in AppKit or `.quickLookPreview()` in SwiftUI.

```swift
// SwiftUI
List(selection: $selection) {
    ForEach(files) { file in
        FileRow(file: file)
    }
}
.quickLookPreview($quickLookItem, in: files)
```

### Rule 5.7 — Arrow Key Navigation

In lists and grids, Up/Down arrow keys move selection. Left/Right collapse/expand disclosure groups or navigate columns. Cmd+Up goes to the beginning, Cmd+Down goes to the end.

---

## 6. Pointer and Mouse (HIGH)

Mac is a pointer-driven platform. Every interactive element must respond to hover, click, right-click, and drag.

### Rule 6.1 — Hover States

All interactive elements must have a visible hover state. Buttons highlight, rows show a selection indicator, links change cursor. Use `.onHover` in SwiftUI.

```swift
// SwiftUI — Hover effect
struct HoverableRow: View {
    @State private var isHovered = false

    var body: some View {
        HStack {
            Text(item.name)
            Spacer()
            if isHovered {
                Button("Edit") { edit() }
                    .buttonStyle(.borderless)
            }
        }
        .padding(8)
        .background(isHovered ? Color.primary.opacity(0.05) : .clear)
        .cornerRadius(6)
        .onHover { hovering in isHovered = hovering }
    }
}
```

### Rule 6.2 — Right-Click Context Menus

Every interactive element must respond to right-click with a contextual menu. The context menu should contain the most relevant actions for the clicked item.

### Rule 6.3 — Drag and Drop

Support drag and drop for content manipulation: reordering items, moving between containers, importing files from Finder, and exporting content.

```swift
// SwiftUI — Drag and drop
ForEach(items) { item in
    ItemView(item: item)
        .draggable(item)
}
.dropDestination(for: Item.self) { items, location in
    handleDrop(items, at: location)
    return true
}
```

```swift
// Accepting file drops from Finder
.dropDestination(for: URL.self) { urls, location in
    importFiles(urls)
    return true
}
```

### Rule 6.4 — Scroll Behavior

Support both trackpad (smooth/inertial) and mouse wheel (discrete) scrolling. Use elastic/bounce scrolling at content boundaries. Support horizontal scrolling where appropriate.

### Rule 6.5 — Cursor Changes

Change the cursor to indicate affordances: pointer for clickable elements, I-beam for text, crosshair for drawing, resize handles at window/splitter edges, grab hand for draggable content.

```swift
// AppKit — Custom cursor
override func resetCursorRects() {
    addCursorRect(bounds, cursor: .crosshair)
}
```

### Rule 6.6 — Multi-Selection

Support Cmd+Click for non-contiguous selection and Shift+Click for range selection in lists, tables, and grids. This is a deeply ingrained Mac interaction pattern.

```swift
// SwiftUI — Tables with multi-selection
Table(items, selection: $selectedItems) {
    TableColumn("Name", value: \.name)
    TableColumn("Date", value: \.dateFormatted)
    TableColumn("Size", value: \.sizeFormatted)
}
```

---

## 7. Notifications and Alerts (MEDIUM)

Mac users are protective of their attention. Only interrupt when truly necessary.

### Rule 7.1 — Use Notification Center Appropriately

Send notifications only for events that happen outside the app or require user action. Never notify for routine operations. Notifications must be actionable.

```swift
// UserNotifications
let content = UNMutableNotificationContent()
content.title = "Download Complete"
content.body = "project-assets.zip is ready"
content.categoryIdentifier = "DOWNLOAD"
content.sound = .default

let request = UNNotificationRequest(identifier: UUID().uuidString, content: content, trigger: nil)
UNUserNotificationCenter.current().add(request)
```

### Rule 7.2 — Alerts with Suppression Option

For recurring alerts, provide a "Do not show this again" checkbox. Respect the user's choice and persist it.

```swift
// AppKit — Alert with suppression
let alert = NSAlert()
alert.messageText = "Remove from library?"
alert.informativeText = "The file will be moved to the Trash."
alert.alertStyle = .warning
alert.addButton(withTitle: "Remove")
alert.addButton(withTitle: "Cancel")
alert.showsSuppressionButton = true
alert.suppressionButton?.title = "Do not ask again"

let response = alert.runModal()
if alert.suppressionButton?.state == .on {
    UserDefaults.standard.set(true, forKey: "suppressRemoveAlert")
}
```

### Rule 7.3 — Don't Interrupt Unnecessarily

Never show alerts for successful operations. Use inline status indicators, toolbar badges, or subtle animations instead. Reserve modal alerts for destructive or irreversible actions.

### Rule 7.4 — Dock Badge

Show a badge on the Dock icon for notification counts. Clear it promptly when the user addresses the notifications.

```swift
// AppKit
NSApp.dockTile.badgeLabel = unreadCount > 0 ? "\(unreadCount)" : nil
```

### Rule 7.5 — Match Feedback to Cognitive Cost

Routine actions should acknowledge completion with inline status, toolbar state, or a subtle animation. Use modal alerts only when the user must stop, evaluate consequences, and choose.

---

## 8. System Integration (MEDIUM)

Mac apps exist in a rich ecosystem. Deep integration makes an app feel native.

### Rule 8.1 — Dock Icon and Menus

Provide a high-quality 1024x1024 app icon. Support Dock right-click menus for quick actions. Show recent documents in the Dock menu.

```swift
// AppKit — Dock menu
override func applicationDockMenu(_ sender: NSApplication) -> NSMenu? {
    let menu = NSMenu()
    menu.addItem(withTitle: "New Window", action: #selector(newWindow(_:)), keyEquivalent: "")
    menu.addItem(withTitle: "New Document", action: #selector(newDocument(_:)), keyEquivalent: "")
    menu.addItem(.separator())
    for doc in recentDocuments.prefix(5) {
        menu.addItem(withTitle: doc.name, action: #selector(openRecent(_:)), keyEquivalent: "")
    }
    return menu
}
```

### Rule 8.2 — Spotlight Integration

Index app content for Spotlight search using `CSSearchableItem` and Core Spotlight. Users expect to find app content via Cmd+Space.

```swift
import CoreSpotlight

let attributeSet = CSSearchableItemAttributeSet(contentType: .text)
attributeSet.title = document.title
attributeSet.contentDescription = document.summary
attributeSet.thumbnailData = document.thumbnail?.pngData()

let item = CSSearchableItem(uniqueIdentifier: document.id, domainIdentifier: "documents", attributeSet: attributeSet)
CSSearchableIndex.default().indexSearchableItems([item])
```

### Rule 8.3 — Quick Look Support

Provide Quick Look previews for custom file types via a Quick Look Preview Extension. Users expect Space to preview any file in Finder.

### Rule 8.4 — Share Extensions

Implement the Share menu so users can share content from your app to Messages, Mail, Notes, etc. Also accept shared content from other apps.

```swift
// SwiftUI
ShareLink(item: document.url) {
    Label("Share", systemImage: "square.and.arrow.up")
}
```

### Rule 8.5 — Services Menu

Register for the Services menu to receive text, URLs, or files from other apps. This is a uniquely Mac integration point that power users rely on.

### Rule 8.6 — Shortcuts and AppleScript

Support the Shortcuts app by providing App Intents. For advanced automation, add AppleScript/JXA scripting support via an `.sdef` scripting dictionary.

```swift
// App Intents for Shortcuts
struct CreateDocumentIntent: AppIntent {
    static var title: LocalizedStringResource = "Create Document"
    static var description = IntentDescription("Creates a new document with the given title.")

    @Parameter(title: "Title")
    var title: String

    func perform() async throws -> some IntentResult {
        let doc = DocumentManager.shared.create(title: title)
        return .result(value: doc.title)
    }
}
```

---

## 9. Visual Design (HIGH)

Mac apps should look and feel like they belong on the platform. Use system-provided materials, fonts, and colors.

### Rule 9.1 — Use System Fonts

Use SF Pro (the system font) at standard dynamic type sizes. Use SF Mono for code. Never hardcode font sizes; use semantic styles.

```swift
// SwiftUI — Semantic font styles
Text("Title").font(.title)
Text("Headline").font(.headline)
Text("Body text").font(.body)
Text("Caption").font(.caption)
Text("let x = 42").font(.system(.body, design: .monospaced))
```

### Rule 9.2 — Vibrancy and Materials

Use system materials for sidebar and toolbar backgrounds. Vibrancy lets the desktop or underlying content show through, anchoring the app to the Mac visual language.

```swift
// SwiftUI
List { ... }
    .listStyle(.sidebar)  // Automatic vibrancy

// Custom vibrancy
ZStack {
    VisualEffectView(material: .sidebar, blendingMode: .behindWindow)
    Text("Sidebar Content")
}
```

```swift
// AppKit — Visual effect view
let visualEffect = NSVisualEffectView()
visualEffect.material = .sidebar
visualEffect.blendingMode = .behindWindow
visualEffect.state = .followsWindowActiveState
```

### Rule 9.3 — Respect System Accent Color

Use the system accent color for selection, emphasis, and interactive elements. Never override it with a fixed brand color for standard controls. Use `.accentColor` or `.tint` only on custom views when appropriate.

```swift
// SwiftUI — Follows system accent automatically
Button("Action") { doSomething() }
    .buttonStyle(.borderedProminent)  // Uses system accent color

Toggle("Enable feature", isOn: $isEnabled)  // Toggle tint follows accent
```

### Rule 9.4 — Support Dark Mode

Every view must support both Light and Dark appearances. Use semantic colors (`Color.primary`, `Color.secondary`, `.background`) rather than hardcoded colors. Test in both modes.

```swift
// SwiftUI — Semantic colors
Text("Title").foregroundStyle(.primary)
Text("Subtitle").foregroundStyle(.secondary)

RoundedRectangle(cornerRadius: 8)
    .fill(Color(nsColor: .controlBackgroundColor))

// Asset catalog: define colors for Both Appearances
// Never use Color.white or Color.black for UI surfaces
```

### Rule 9.5 — Translucency

Respect the "Reduce transparency" accessibility setting. When transparency is reduced, replace translucent materials with solid backgrounds.

```swift
// SwiftUI
@Environment(\.accessibilityReduceTransparency) var reduceTransparency

var body: some View {
    if reduceTransparency {
        Color(nsColor: .windowBackgroundColor)
    } else {
        VisualEffectView(material: .sidebar, blendingMode: .behindWindow)
    }
}
```

### Rule 9.6 — Consistent Spacing and Layout

Use 20pt standard margins, 8pt spacing between related controls, 20pt spacing between groups. Align controls to a grid. Use SwiftUI's built-in spacing or AppKit's Auto Layout with system spacing constraints.

---

## 10. Popovers (MEDIUM)

Popovers present contextual content anchored to a control. They are common in Mac apps for options panels, color pickers, and contextual settings.

### Rule 10.1 — Use Popovers for Transient Context-Sensitive Content

Popovers attach to a source view and are dismissed by clicking outside or pressing Esc. Use them for settings or options that apply to a specific element. Do not use popovers for primary workflows or multi-step operations.

```swift
// SwiftUI
Button("Format...") { showingFormatPopover = true }
    .popover(isPresented: $showingFormatPopover, arrowEdge: .bottom) {
        FormatOptionsView()
            .frame(width: 280)
            .padding()
    }
```

### Rule 10.2 — Dismiss Popovers with Esc

Popovers must close when the user presses Esc. SwiftUI handles this automatically for `.popover`. AppKit's `NSPopover` also dismisses on Esc when `behavior` is set to `.transient` or `.semitransient`.

### Rule 10.3 — Size Popovers to Their Content

Set a reasonable width for the popover's content. Do not let the popover be wider than necessary. Content should not require scrolling unless the list is inherently long (e.g., a font picker).

---

## 11. Accessibility (CRITICAL)

Mac apps must support VoiceOver, Full Keyboard Access, Switch Control, and related assistive technologies.

### Rule 11.1 — VoiceOver Labels on All Interactive Elements

Every button, control, and interactive element must have a meaningful accessibility label. Icon-only toolbar items and image buttons must provide labels.

**Correct:**
```swift
Button(action: deleteSelected) {
    Image(systemName: "trash")
}
.accessibilityLabel("Delete selected items")
```

**Incorrect:**
```swift
Button(action: deleteSelected) {
    Image(systemName: "trash")
}
// VoiceOver reads "trash" — ambiguous without context
```

### Rule 11.2 — Full Keyboard Access

Every action reachable by mouse must also be reachable by keyboard. Tab must move focus between all controls. Arrow keys must navigate within lists, tables, and grids. No keyboard traps.

```swift
// SwiftUI — Ensure all custom views are focusable
MyCustomControl()
    .focusable()
    .onKeyPress(.return) { handleActivation(); return .handled }
```

### Rule 11.3 — Respect Reduce Motion

Disable or substitute decorative animations when the user enables Reduce Motion.

```swift
@Environment(\.accessibilityReduceMotion) var reduceMotion

var body: some View {
    ContentView()
        .animation(reduceMotion ? nil : .spring(), value: isExpanded)
}
```

### Rule 11.4 — Respect Reduce Transparency

Replace translucent materials with solid backgrounds when Reduce Transparency is enabled (see Rule 9.5).

### Rule 11.5 — Logical Focus Order

VoiceOver must traverse elements in a logical reading order (top-left to bottom-right for LTR). Use `.accessibilitySortPriority()` or `accessibilityElement(children:)` to correct order when the visual layout diverges.

### Rule 11.6 — Respond to Bold Text

When the user enables Bold Text in System Settings, custom-rendered text must adapt. SwiftUI text styles handle this automatically. For AppKit, check `NSWorkspace.shared.accessibilityDisplayShouldUseBoldText`, or use `@Environment(\.legibilityWeight)` in SwiftUI to apply heavier weights to custom text.

**Correct:**
```swift
// SwiftUI — environment handles bold text automatically for standard styles
Text("Section Header")
    .font(.headline)

// SwiftUI — custom rendering responds to legibilityWeight
@Environment(\.legibilityWeight) var legibilityWeight

var body: some View {
    Text("Custom Label")
        .fontWeight(legibilityWeight == .bold ? .bold : .regular)
}
```

**Incorrect:**
```swift
// Hardcoded weight ignores Bold Text preference
Text("Custom Label")
    .fontWeight(.regular) // Never adapts to Bold Text setting
```

### Rule 11.7 — Respond to Increase Contrast

When the user enables Increase Contrast in System Settings, custom colors must provide higher-contrast variants. Use `NSWorkspace.shared.accessibilityDisplayShouldIncreaseContrast` in AppKit, or `@Environment(\.colorSchemeContrast)` in SwiftUI to detect and apply appropriate values.

**Correct:**
```swift
// SwiftUI
@Environment(\.colorSchemeContrast) var contrast

var borderColor: Color {
    contrast == .increased ? Color.primary : Color.secondary
}

// AppKit
let shouldIncrease = NSWorkspace.shared.accessibilityDisplayShouldIncreaseContrast
let borderColor: NSColor = shouldIncrease ? .labelColor : .separatorColor
```

**Incorrect:**
```swift
// Static color ignores Increase Contrast setting
let borderColor = NSColor.separatorColor // Always low-contrast; ignores user preference
```

---

## Keyboard Shortcut Quick Reference

### Navigation
| Shortcut | Action |
|----------|--------|
| Cmd+N | New window/document |
| Cmd+O | Open |
| Cmd+W | Close window/tab |
| Cmd+Q | Quit app |
| Cmd+, | Settings/Preferences |
| Cmd+Tab | Switch apps |
| Cmd+` | Switch windows within app |
| Cmd+T | New tab |

### Editing
| Shortcut | Action |
|----------|--------|
| Cmd+Z | Undo |
| Cmd+Shift+Z | Redo |
| Cmd+X / C / V | Cut / Copy / Paste |
| Cmd+A | Select All |
| Cmd+D | Duplicate |
| Cmd+F | Find |
| Cmd+G | Find Next |
| Cmd+Shift+G | Find Previous |
| Cmd+E | Use Selection for Find |

### View
| Shortcut | Action |
|----------|--------|
| Cmd+Ctrl+F | Toggle fullscreen |
| Cmd+Ctrl+S | Toggle sidebar (app-defined; not a universal HIG standard) |
| Cmd++ / Cmd+- | Zoom in/out |
| Cmd+0 | Actual size |

---

## Evaluation Checklist

Before shipping a Mac app, verify:

### Menu Bar
- [ ] App has a complete menu bar with standard menus
- [ ] All actions have keyboard shortcuts
- [ ] Menu items dynamically update (enable/disable, title changes)
- [ ] Context menus on all interactive elements
- [ ] App menu has About, Settings, Hide, Quit

### Windows
- [ ] Windows are freely resizable with sensible minimums
- [ ] Fullscreen and Split View work
- [ ] Multiple windows supported (if appropriate)
- [ ] Window position and size persist across launches
- [ ] Traffic light buttons visible and functional
- [ ] Document title and edited state shown (if document-based)

### Toolbars
- [ ] Toolbar present with common actions
- [ ] Toolbar is user-customizable
- [ ] Search field available in toolbar

### Sidebars
- [ ] Sidebar for navigation (if app has multiple sections)
- [ ] Sidebar is collapsible
- [ ] Source list style with vibrancy

### Keyboard
- [ ] Full keyboard navigation (Tab, arrows, Enter, Esc)
- [ ] Cmd+Z undo for all destructive actions
- [ ] Space for Quick Look previews
- [ ] Delete key removes selected items
- [ ] No keyboard traps (user can always Tab out)

### Pointer
- [ ] Hover states on interactive elements
- [ ] Right-click context menus everywhere
- [ ] Drag and drop for content manipulation
- [ ] Cmd+Click for multi-selection
- [ ] Appropriate cursor changes

### Notifications
- [ ] Notifications only for important events
- [ ] Alerts have suppression option for recurring ones
- [ ] No modal alerts for routine operations

### System Integration
- [ ] High-quality Dock icon
- [ ] Content indexed in Spotlight (if applicable)
- [ ] Share menu works
- [ ] App Intents for Shortcuts

### Visual Design
- [ ] System fonts at semantic sizes
- [ ] Dark Mode fully supported
- [ ] System accent color respected
- [ ] Translucency respects accessibility setting
- [ ] Consistent spacing on 8pt grid

### Popovers
- [ ] Popover is anchored to its source element with an arrow pointing at it
- [ ] Pressing Esc dismisses the popover
- [ ] Popover is sized to its content without unnecessary scrolling

### Accessibility
- [ ] All icon-only toolbar items and image buttons have accessibility labels
- [ ] Every action reachable by mouse is also reachable by keyboard (Full Keyboard Access)
- [ ] Decorative animations disabled when Reduce Motion is enabled
- [ ] Translucent surfaces replaced with solid backgrounds when Reduce Transparency is enabled
- [ ] VoiceOver traversal order is logical (top-left to bottom-right)
- [ ] Bold Text preference respected (SwiftUI handles automatically; AppKit checks `accessibilityDisplayShouldUseBoldText`)
- [ ] Increase Contrast preference respected (custom colors provide higher-contrast variants via `colorSchemeContrast` or `accessibilityDisplayShouldIncreaseContrast`)

---

## Anti-Patterns

**Do not do these things in a Mac app:**

1. **No menu bar** — Every Mac app needs a menu bar. Period. A Mac app without menus is like a car without a steering wheel.

2. **Hamburger menus** — Never use a hamburger menu on Mac. The menu bar exists for this purpose. Hamburger menus signal a lazy iOS port.

3. **Tab bars at the bottom** — Mac apps use sidebars and toolbars, not iOS-style tab bars. If you need tabs, use actual document tabs in the tab bar (like Safari or Finder).

4. **Large touch-sized targets** — Mac controls should be compact (22-28pt height). Users have precise pointer input. Giant buttons waste space and look out of place.

5. **Floating action buttons** — FABs are a Material Design pattern. On Mac, place primary actions in the toolbar, menu bar, or as inline buttons.

6. **Sheet for every action** — Don't use modal sheets for simple operations. Use popovers, inline editing, or direct manipulation. Sheets should be reserved for multi-step workflows or important decisions.

7. **Custom window chrome** — Don't replace the standard title bar, traffic lights, or window controls with custom implementations. Users expect these to work consistently across all apps.

8. **Ignoring keyboard** — If a power user must reach for the mouse to perform common actions, your keyboard support is insufficient.

9. **Single-window only** — Unless your app is genuinely single-purpose (calculator, timer), support multiple windows. Users expect to Cmd+N for new windows.

10. **Fixed window size** — Non-resizable windows feel broken on Mac. Users have displays ranging from 13" laptops to 32" externals and expect to use that space.

11. **No Cmd+Z undo** — Every destructive or modifying action must be undoable. Users build muscle memory around Cmd+Z as their safety net.

12. **Notification spam** — Mac apps that send excessive notifications get their permissions revoked. Only notify for events that genuinely need attention.

13. **Ignoring Dark Mode** — A Mac app that looks wrong in Dark Mode appears abandoned. Always test both appearances.

14. **Hardcoded colors** — Use semantic system colors, not hardcoded hex values. Your colors should adapt to Light/Dark mode and accessibility settings automatically.

15. **No drag and drop** — Mac is a drag-and-drop platform. If users can see content, they expect to drag it somewhere.
```

## File: `skills/macos/metadata.json`
```json
{
  "version": "1.0.0",
  "organization": "Platform Design Skills",
  "date": "February 2026",
  "abstract": "Apple Human Interface Guidelines for macOS apps. 60+ rules across 11 categories covering menu bars, window management, toolbars, keyboard-driven interaction, sidebars, popovers, accessibility, and desktop power-user expectations. Each rule includes SwiftUI/AppKit examples.",
  "references": [
    "https://developer.apple.com/design/human-interface-guidelines",
    "https://developer.apple.com/design/human-interface-guidelines/designing-for-macos",
    "https://developer.apple.com/documentation/swiftui",
    "https://developer.apple.com/documentation/appkit"
  ]
}
```

## File: `skills/macos/rules/_sections.md`
```markdown
# macOS Design Guidelines — Section Index

Quick-reference for all 11 categories and 62 rules. See `../SKILL.md` for full details, code examples, and rationale.

---

## Section 1: Menu Bar [CRITICAL]

| Rule | Summary |
|------|---------|
| 1.1 | Provide standard menus: App, File, Edit, View, Window, Help |
| 1.2 | Keyboard shortcut for every menu item; follow standard conventions |
| 1.3 | Dynamic menu updates: disable unavailable items, update titles contextually |
| 1.4 | Right-click context menus on all interactive elements |
| 1.5 | App menu must contain About, Settings, Services, Hide, Quit |
| 1.6 | Keep common commands in stable menus with stable names and shortcuts |

**Key principle:** The menu bar is the primary command discovery surface and memory offload on Mac. Every action in the app must be reachable through the menu bar.

---

## Section 2: Windows [CRITICAL]

| Rule | Summary |
|------|---------|
| 2.1 | Resizable windows with sensible minimum sizes |
| 2.2 | Support native fullscreen and Split View |
| 2.3 | Support multiple simultaneous windows |
| 2.4 | Title bar shows document name, proxy icon, edited state |
| 2.5 | Persist window position, size, and state across launches |
| 2.6 | Never hide or reposition traffic light buttons |

**Key principle:** Users control window size and position. Never fight window management.

---

## Section 3: Toolbars [HIGH]

| Rule | Summary |
|------|---------|
| 3.1 | Use unified title bar + toolbar style |
| 3.2 | Allow user customization of toolbar items |
| 3.3 | Segmented controls for view mode switching |
| 3.4 | Search field in trailing area of toolbar |
| 3.5 | Toolbar items have both icon (SF Symbol) and text label |

**Key principle:** Toolbars provide fast access to frequent actions and should be user-configurable.

---

## Section 4: Sidebars [HIGH]

| Rule | Summary |
|------|---------|
| 4.1 | Leading edge, collapsible, with persistent state |
| 4.2 | Source list style with translucent vibrancy |
| 4.3 | Outline views for hierarchical content |
| 4.4 | Drag-to-reorder for user-arranged items |
| 4.5 | Badge counts for unread/pending indicators |

**Key principle:** Sidebars are the primary navigation pattern for Mac apps with multiple content sections.

---

## Section 5: Keyboard [CRITICAL]

| Rule | Summary |
|------|---------|
| 5.1 | Cmd+key shortcuts for all actions; follow modifier conventions |
| 5.2 | Full Tab/arrow key navigation between and within controls |
| 5.3 | Esc dismisses popovers, sheets, dialogs; cancels operations |
| 5.4 | Return/Enter activates the default (blue) button |
| 5.5 | Delete key removes selected items; Cmd+Z undoes |
| 5.6 | Space bar invokes Quick Look for previewable items |
| 5.7 | Arrow keys navigate lists, grids, disclosure groups |

**Key principle:** Every mouse action must have a keyboard equivalent. Power users live on the keyboard.

---

## Section 6: Pointer and Mouse [HIGH]

| Rule | Summary |
|------|---------|
| 6.1 | Visible hover states on all interactive elements |
| 6.2 | Right-click context menus on every interactive element |
| 6.3 | Drag and drop for reordering, moving, importing, exporting |
| 6.4 | Support smooth trackpad and discrete mouse wheel scrolling |
| 6.5 | Cursor changes to indicate affordance (pointer, I-beam, crosshair, resize) |
| 6.6 | Cmd+Click for non-contiguous, Shift+Click for range selection |

**Key principle:** Mac is a pointer-driven platform. Every element must respond to hover, click, right-click, and drag.

---

## Section 7: Notifications and Alerts [MEDIUM]

| Rule | Summary |
|------|---------|
| 7.1 | Notifications only for events outside the app or requiring action |
| 7.2 | Recurring alerts offer "Do not show again" suppression |
| 7.3 | Never show alerts for successful routine operations |
| 7.4 | Dock badge for notification counts; clear promptly |
| 7.5 | Match interruption style to the user's decision cost |

**Key principle:** Respect user attention. Give fast feedback for routine actions and interrupt only when genuinely necessary.

---

## Section 8: System Integration [MEDIUM]

| Rule | Summary |
|------|---------|
| 8.1 | High-quality Dock icon; Dock right-click menu with quick actions |
| 8.2 | Index app content in Spotlight via Core Spotlight |
| 8.3 | Quick Look Preview Extension for custom file types |
| 8.4 | Share menu for sending content to other apps |
| 8.5 | Services menu registration for receiving content |
| 8.6 | App Intents for Shortcuts; AppleScript/JXA scripting support |

**Key principle:** Mac apps exist in a rich ecosystem. Deep integration makes an app feel truly native.

---

## Section 9: Visual Design [HIGH]

| Rule | Summary |
|------|---------|
| 9.1 | SF Pro system font at semantic type sizes; SF Mono for code |
| 9.2 | Vibrancy and system materials for sidebar/toolbar backgrounds |
| 9.3 | System accent color for selection and emphasis; no brand override on standard controls |
| 9.4 | Full Dark Mode support with semantic colors |
| 9.5 | Respect "Reduce transparency" accessibility setting |
| 9.6 | 20pt margins, 8pt control spacing, 20pt group spacing |

**Key principle:** Use system-provided colors, fonts, and materials. Your app should feel like it belongs on the Mac.

---

## Section 10: Popovers [MEDIUM]

| Rule | Summary |
|------|---------|
| 10.1 | Use popovers for transient, context-sensitive content anchored to a control |
| 10.2 | Esc must dismiss all popovers |
| 10.3 | Size popovers to content; avoid unnecessary scrolling |

**Key principle:** Popovers are for focused, transient options. Not for primary flows or multi-step tasks.

---

## Section 11: Accessibility [CRITICAL]

| Rule | Summary |
|------|---------|
| 11.1 | VoiceOver label on every button, control, and interactive element |
| 11.2 | Full Keyboard Access: all actions reachable by keyboard, no traps |
| 11.3 | Respect Reduce Motion: disable decorative animations |
| 11.4 | Respect Reduce Transparency: replace translucent materials with solid backgrounds |
| 11.5 | Logical VoiceOver focus order; adjust with accessibilitySortPriority when needed |
| 11.6 | Respond to Bold Text: use legibilityWeight or NSWorkspace.accessibilityDisplayShouldUseBoldText |
| 11.7 | Respond to Increase Contrast: use colorSchemeContrast or NSWorkspace.accessibilityDisplayShouldIncreaseContrast |

**Key principle:** VoiceOver, Full Keyboard Access, and Switch Control must work flawlessly. Accessibility is not optional.

---

## Priority Summary

| Priority | Sections | Rule Count |
|----------|----------|------------|
| CRITICAL | Menu Bar, Windows, Keyboard, Accessibility | 26 rules |
| HIGH | Toolbars, Sidebars, Pointer/Mouse, Visual Design | 22 rules |
| MEDIUM | Notifications, System Integration, Popovers | 14 rules |
| **Total** | **11 sections** | **62 rules** |

---

## Cross-Cutting Concerns

These principles apply across all sections:

- **Undo everywhere** — Cmd+Z must work for any modifying action (Sections 1, 5)
- **Keyboard + pointer parity** — Every mouse action has a keyboard shortcut (Sections 1, 5, 6)
- **Respect system settings** — Dark Mode, accent color, transparency, font size (Section 9)
- **Consistent with platform** — No iOS patterns (tab bars, hamburger menus, FABs) on Mac (Anti-patterns)
- **User control** — Customizable toolbars, resizable windows, collapsible sidebars (Sections 2, 3, 4)
```

## File: `skills/tvos/AGENTS.md`
```markdown
# tvOS Design Guidelines

## Purpose

Provide Apple Human Interface Guidelines expertise for Apple TV app design. This skill covers focus-based navigation, Siri Remote interaction, 10-foot UI principles, Top Shelf extensions, media playback, and tab bar patterns.

## When to Use

- Designing or reviewing tvOS applications
- Building focus-based navigation systems
- Creating Top Shelf extensions
- Implementing media playback interfaces
- Adapting existing apps for the living room

## Key Principles

1. **Focus is everything** -- tvOS has no pointer or touch; all interaction is focus-driven
2. **Design for distance** -- assume 10-foot viewing; large text, bold imagery, high contrast
3. **Respect the remote** -- Siri Remote is simple; never require complex gestures
4. **Content first** -- TV is a lean-back, content-consumption experience
5. **Parallax communicates depth** -- use layered images to reinforce focus

## Rule Categories

| # | Category | Impact |
|---|----------|--------|
| 1 | Focus-Based Navigation | CRITICAL |
| 2 | Siri Remote | CRITICAL |
| 3 | 10-Foot UI | HIGH |
| 4 | Top Shelf | HIGH |
| 5 | Media & Playback | MEDIUM |
| 6 | Tab Bar | MEDIUM |
| 7 | Accessibility | CRITICAL |

## File Structure

- `SKILL.md` -- complete design rules and evaluation checklist
- `rules/_sections.md` -- categorized rules reference
- `metadata.json` -- version and source references

## Never Do

- Never use bottom tab bars — use the top tab bar
- Never trap focus — users must always be able to move away
- Never override the Menu button behavior
- Never require complex or multi-finger gestures on the Siri Remote
- Never repurpose the Play/Pause button for non-media actions
- Never use small touch targets — minimum 250x150pt for cards
- Never use body text below 29pt
- Never use TVTopShelfProvider (deprecated since tvOS 14) — use TVTopShelfContentProvider
- Never omit accessibility labels on image cards and icon buttons
- Never apply parallax animations without respecting Reduce Motion
```

## File: `skills/tvos/SKILL.md`
```markdown
---
name: tvos-design-guidelines
description: Apple Human Interface Guidelines for Apple TV. Use when building tvOS apps with focus-based navigation, Siri Remote input, or living room viewing experiences. Triggers on tasks involving Apple TV, tvOS, 10-foot UI, or media playback.
license: MIT
metadata:
  author: platform-design-skills
  version: "1.0.0"
---

# tvOS Design Guidelines

Apple TV is a living room device driven entirely by focus-based navigation and the Siri Remote. There is no pointer, no touch screen, and no mouse. Every design decision must account for the 10-foot viewing distance, the simplicity of the remote, and the lean-back nature of TV consumption.

---

## 1. Focus-Based Navigation (CRITICAL)

The focus system is the foundation of all tvOS interaction. There is no cursor -- users move focus between elements using the Siri Remote touch surface.

### Rules

**FOCUS-01: Every interactive element must have a clearly visible focus state.**
The focused item must be unmistakably distinguished from unfocused items. Use scaling (typically 1.05x-1.1x), elevation via shadow, brightness changes, or border highlights. Never rely on color alone.

**FOCUS-02: Focus movement must be predictable and follow a logical spatial layout.**
When a user swipes right, focus must move to the element visually to the right. Avoid layouts where focus jumps unexpectedly across the screen. Grid and linear layouts are safest.

**FOCUS-03: Use focus guides (UIFocusGuide) to bridge gaps in layouts.**
When visual gaps exist between focusable elements, add invisible focus guides so the user does not get stuck. Every swipe should move focus somewhere meaningful.

**FOCUS-04: Apply the parallax effect to focused items.**
Focused cards, posters, and icons should exhibit a subtle parallax tilt responding to touch surface movement. Use layered images (LSR format) with foreground, midground, and background layers. This communicates depth and confirms focus.

**Correct:**
```swift
// SwiftUI — custom focus engine with explicit focus state
struct ContentView: View {
    @FocusState private var focusedItem: String?

    var body: some View {
        HStack(spacing: 40) {
            ForEach(items) { item in
                CardView(item: item)
                    .focusable()
                    .focused($focusedItem, equals: item.id)
                    .scaleEffect(focusedItem == item.id ? 1.1 : 1.0)
                    .shadow(radius: focusedItem == item.id ? 20 : 0)
                    .animation(.easeInOut(duration: 0.15), value: focusedItem)
            }
        }
    }
}
```

**Incorrect:**
```swift
// SwiftUI — no focus state: unfocused and focused items look identical
struct ContentView: View {
    var body: some View {
        HStack(spacing: 40) {
            ForEach(items) { item in
                CardView(item: item)
                    .focusable()
                // No scale, shadow, or visual change on focus
                // User cannot tell which item is selected
            }
        }
    }
}
```

**FOCUS-05: Make focus targets large enough for comfortable navigation.**
Minimum recommended touch target is 250x150pt for cards. Smaller elements are difficult to land on with swipe-based navigation. Group small actions under a focused parent when possible.

**FOCUS-06: Provide a default focused element on every screen.**
When a view appears, one element must already hold focus. Choose the most likely user intent -- typically the primary content item or the first item in a collection.

**FOCUS-07: Preserve focus memory when returning to a screen.**
If a user navigates away and returns, focus should restore to the last focused item on that screen, not reset to the default.

**FOCUS-08: Never trap focus.**
Users must always be able to move focus away from any element. If focus cannot leave a region, the app feels broken.

**FOCUS-09: Reduce re-orientation cost.**
Keep row order stable, restore prior focus when returning, and prefer nearby focus destinations so users do not have to rescan the entire screen after each navigation step.

### Parallax Layer Reference

| Layer | Purpose | Movement Amount |
|-------|---------|-----------------|
| Background | Static backdrop, blurred imagery | Minimal (1-2pt) |
| Midground | Primary artwork or content image | Moderate (3-5pt) |
| Foreground | Title text, logos, badges | Maximum (5-8pt) |

Use Xcode's LSR (Layered Static Image) format for static layered images in the asset catalog — the system animates them automatically on focus. For custom programmatic parallax, stack `UIImageView` instances and use the focus engine callbacks (`didUpdateFocus(in:with:)` and `UIFocusAnimationCoordinator`) to drive layer movement during focus transitions. (`UIMotionEffect` responds only to subtle Siri Remote gyroscope micromotion and is not the mechanism for focus-driven parallax.)

---

## 2. Siri Remote (CRITICAL)

The Siri Remote is the primary (and often only) input device. It has a touch surface, Menu button, Play/Pause button, Siri/microphone button, volume buttons, and a power button.

### Rules

**REMOTE-01: Touch surface swipes control focus movement.**
Swiping moves focus in the corresponding direction. Clicking the touch surface selects the focused item. These are the two fundamental interactions -- design everything around them.

**REMOTE-02: Menu button must always navigate back.**
Pressing Menu should dismiss the current screen, close an overlay, or navigate up the hierarchy. At the top level, it returns to the Apple TV home screen. Never override this expectation.

**REMOTE-03: Play/Pause button must control media playback.**
If media is playing, Play/Pause should toggle playback regardless of what screen is visible. Do not repurpose this button for non-media actions.

**REMOTE-04: Never require complex or multi-finger gestures.**
The Siri Remote touch surface is small. Do not require pinch, rotate, multi-tap, or long-press gestures. Stick to single-finger swipe and click.

**REMOTE-05: Swipe directions must be intuitive and consistent.**
Horizontal swipes scroll horizontally; vertical swipes scroll vertically. Never invert axes. Diagonal content movement should follow the dominant swipe axis.

**REMOTE-06: Support Siri voice input for search and text entry.**
Text input via the on-screen keyboard is tedious on tvOS. Always support dictation and Siri search as alternatives to keyboard entry.

**REMOTE-07: Provide click feedback.**
When the user clicks the touch surface to select an item, provide immediate visual feedback (animation, highlight change, or haptic-style visual pulse) so the click feels responsive.

**REMOTE-08: Never make the on-screen keyboard the only practical text path.**
For search, sign-in, and setup, prefer dictation, recent queries, autofill, or short code-based flows over long remote-typed text. Remote text entry carries high motor and cognitive cost.

---

## 3. 10-Foot UI (HIGH)

Apple TV content is viewed from across a room, typically 8-12 feet (2.5-3.5 meters) from the screen. All visual design must account for this distance.

### Rules

**DISTANCE-01: Minimum body text size is 29pt.**
Text below 29pt becomes difficult to read at living room distances. Titles should be 48pt or larger. Use San Francisco Display or comparable high-legibility typeface.

**DISTANCE-02: Maintain high contrast between text and backgrounds.**
Use light text on dark backgrounds as the default. tvOS uses a dark theme. Contrast ratio should meet WCAG AA or higher (4.5:1 for body text, 3:1 for large text).

**DISTANCE-03: Limit text per screen.**
TV is a visual medium. Show headlines, short descriptions, and metadata -- not paragraphs. If extended text is necessary, use scrollable text overlays that the user explicitly opens.

**DISTANCE-04: Use bold, clear imagery at high resolution.**
Full-screen background images should be 1920x1080 or 3840x2160 (4K). Content artwork should be sharp and visually engaging. Avoid small, detailed illustrations that lose clarity at distance.

**DISTANCE-05: Keep layouts simple and spacious.**
Generous margins and padding. Do not crowd the screen with many small elements. A single row of 5-7 cards is preferable to a dense grid of 20+ thumbnails.

**DISTANCE-06: Use the TV-safe area.**
Keep all critical content within the safe area (60pt inset from edges). Content near screen edges may be cropped on some TV sets due to overscan.

**DISTANCE-07: Avoid thin fonts and hairline borders.**
Thin strokes disappear on TV displays, especially with motion blur and compression artifacts. Use medium or semibold weights minimum.

### Text Size Reference

| Element | Minimum Size | Recommended Size |
|---------|-------------|-----------------|
| Body text | 29pt | 31-35pt |
| Secondary labels | 25pt | 29pt |
| Titles | 48pt | 52-76pt |
| Large headers | 64pt | 76-96pt |
| Buttons | 29pt | 35-38pt |

---

## 4. Top Shelf (HIGH)

The Top Shelf is a prominent content area displayed when the user focuses on your app icon on the Apple TV home screen. It is prime real estate for showcasing content.

### Rules

**SHELF-01: Provide a Top Shelf extension.**
Apps should include a `TVTopShelfContentProvider` (tvOS 14+) that returns dynamic content. `TVTopShelfProvider` is deprecated since tvOS 14 — do not use it. A static Top Shelf is a missed opportunity for engagement.

**SHELF-02: Use the correct layout style for your content.**
- **Inset banner**: 1 large focused item with smaller items on either side. Best for featured or editorial content.
- **Sectioned content**: Multiple scrollable rows of items grouped by category. Best for media libraries.

**SHELF-03: Top Shelf items must deep-link into the app.**
Each item must open the corresponding content when selected. Never link all items to the same generic landing page.

**SHELF-04: Use high-quality, engaging imagery.**
Top Shelf images are displayed large on the home screen. Blurry, low-resolution, or text-heavy images look unprofessional. Recommended image sizes:
- Inset banner: 1940x624pt (@1x) or 3880x1248pt (@2x)
- Sectioned items: 404x608pt (@1x)

**SHELF-05: Keep Top Shelf content fresh.**
Update Top Shelf content regularly -- ideally reflecting recently added, trending, or personalized content. Stale Top Shelf content signals an abandoned app.

---

## 5. Media & Playback (MEDIUM)

Apple TV is primarily a media consumption device. Playback interfaces must follow established TV conventions.

### Rules

**MEDIA-01: Use standard transport controls.**
Provide play, pause, skip forward (10s), skip back (10s), and a scrubber timeline. Use `AVPlayerViewController` to get these for free with consistent behavior.

**MEDIA-02: Show an info overlay on swipe-down during playback.**
Swiping down during playback should reveal an info panel showing title, description, and metadata. Swiping down again or pressing Menu dismisses it.

**MEDIA-03: Support scrubbing via the touch surface.**
Swiping left/right on the touch surface during playback should scrub through the timeline. Show thumbnail previews during scrubbing when possible.

**MEDIA-04: Support subtitles and alternative audio tracks.**
Provide access to subtitle selection and audio track switching via the info overlay or the standard player controls.

**MEDIA-05: Support Picture in Picture where appropriate.**
For video content, allow PiP so users can browse other content while watching. Implement `AVPictureInPictureController` integration.

**MEDIA-06: Remember playback position.**
When a user returns to previously watched content, resume from where they left off. Display a progress indicator on content thumbnails.

**MEDIA-07: Handle interruptions gracefully.**
If the user presses the TV button or switches apps during playback, save position and pause cleanly. Resume without re-buffering when the user returns.

---

## 6. Tab Bar (MEDIUM)

The tvOS tab bar sits at the top of the screen, unlike iOS where it sits at the bottom. It provides primary navigation between app sections.

### Rules

**TAB-01: Place the tab bar at the top of the screen.**
This is the standard tvOS convention. Bottom tab bars are an iOS pattern and feel wrong on TV.

**TAB-02: Tab bar should be translucent and overlay content.**
The tab bar floats over content with a blur effect. When the user focuses on the tab bar, content shifts down to make room.

**TAB-03: Use 3-7 tabs.**
Fewer than 3 tabs suggests the app is too simple for tab navigation. More than 7 tabs becomes difficult to navigate with horizontal swiping.

**TAB-04: Every tab must have a text label.**
Icon-only tabs are insufficient at TV viewing distances. Text labels are required for clarity. Icons may accompany text but are not required.

**TAB-05: Focus on the tab bar should feel lightweight.**
When focus moves to the tab bar, it should appear smoothly. Content preview should be visible beneath the translucent bar. Switching tabs should update the content below immediately or show a loading state.

**TAB-06: Remember the selected tab across app launches.**
If the user was on the "Search" tab when they left the app, return to "Search" when they re-open it.

---

## 7. Accessibility (CRITICAL)

Apple TV supports VoiceOver. Sighted users use focus navigation; VoiceOver users additionally hear spoken descriptions. Both must work.

### Rules

**ACCESS-01: Every interactive element must have a meaningful accessibility label.**
Icon-only buttons and image cards must have labels. The focused item's name is announced by VoiceOver when focus arrives.

**ACCESS-02: Provide accessibility hints for non-obvious interactions.**
If tapping a card does something other than opening the content (e.g., launching a trailer rather than full playback), describe this with an accessibility hint.

**ACCESS-03: Ensure VoiceOver focus order matches visual focus order.**
VoiceOver must traverse elements in the same order that focus engine navigation produces. Custom focus ordering via `UIFocusGuide` must not create discontinuities in the VoiceOver reading order.

**ACCESS-04: Respect Reduce Motion.**
Parallax effects and other animations must be reduced or disabled when the user enables Reduce Motion in Accessibility settings.

**ACCESS-05: Respond to Bold Text.**
When the user enables Bold Text, custom-rendered text must adapt. SwiftUI dynamic type styles handle this automatically; custom text rendering must check `UIAccessibility.isBoldTextEnabled` or use `@Environment(\.legibilityWeight)`.

**ACCESS-06: Respond to Increase Contrast.**
When the user enables Increase Contrast (Darker System Colors), custom colors must provide higher-contrast variants. Use `@Environment(\.colorSchemeContrast)` in SwiftUI or `UIAccessibility.isDarkerSystemColorsEnabled` in UIKit to detect and apply appropriate values.

**ACCESS-07: Respect Dynamic Type / Larger Text.**
tvOS supports the "Larger Text" accessibility setting via `UIContentSizeCategory`. Use SwiftUI semantic text styles (`Font.TextStyle`) so text scales automatically. For UIKit, scale custom fonts with `UIFontMetrics` relative to a base `UIFont.TextStyle`.

**Correct:**
```swift
// SwiftUI — semantic text styles scale with Larger Text automatically
Text("Now Playing")
    .font(.title2)        // Scales with UIContentSizeCategory
Text("Episode description")
    .font(.body)          // Scales with UIContentSizeCategory

// UIKit — scale custom font with UIFontMetrics
let baseFont = UIFont(name: "CustomFont-Regular", size: 29)!
let scaledFont = UIFontMetrics(forTextStyle: .body).scaledFont(for: baseFont)
label.font = scaledFont
label.adjustsFontForContentSizeCategory = true
```

**Incorrect:**
```swift
// SwiftUI — hardcoded size ignores Larger Text preference
Text("Now Playing")
    .font(.system(size: 29)) // Does not scale

// UIKit — hardcoded font ignores UIContentSizeCategory
label.font = UIFont(name: "CustomFont-Regular", size: 29)
// Missing adjustsFontForContentSizeCategory = true
```

---

## Evaluation Checklist

Use this checklist when reviewing a tvOS app design or implementation.

### Focus System
- [ ] Every interactive element has a visible, distinct focus state
- [ ] Focus movement is predictable in all directions
- [ ] No focus traps exist anywhere in the app
- [ ] Focus guides bridge layout gaps
- [ ] Parallax effect is applied to content cards and icons
- [ ] Default focus is set on every screen
- [ ] Focus memory is preserved when navigating back

### Siri Remote
- [ ] Menu button navigates back on every screen
- [ ] Play/Pause controls media playback globally
- [ ] No complex gestures are required
- [ ] Click feedback is immediate and visible
- [ ] Siri/dictation supported for text input

### 10-Foot UI
- [ ] Body text is 29pt or larger
- [ ] High contrast ratios on all text
- [ ] Text content is concise, not paragraph-heavy
- [ ] Imagery is high resolution and visually clear
- [ ] Layout uses generous spacing with TV-safe margins
- [ ] No thin fonts or hairline strokes

### Top Shelf
- [ ] Top Shelf extension provides dynamic content
- [ ] All Top Shelf items deep-link correctly
- [ ] Images are high quality and correctly sized
- [ ] Content updates regularly

### Media & Playback
- [ ] Standard transport controls are available
- [ ] Scrubbing works via touch surface
- [ ] Subtitles and audio tracks are accessible
- [ ] Playback position is remembered
- [ ] Interruptions are handled gracefully

### Tab Bar
- [ ] Tab bar is at the top of the screen
- [ ] Tabs have text labels
- [ ] 3-7 tabs are used
- [ ] Selected tab persists across launches

### Accessibility
- [ ] Every interactive element and content card has a meaningful accessibility label
- [ ] Non-obvious interactions have accessibility hints
- [ ] VoiceOver focus order matches the visual focus engine order
- [ ] Parallax effects and decorative animations are disabled when Reduce Motion is enabled
- [ ] Bold Text preference is respected (SwiftUI handles automatically; custom text checks `isBoldTextEnabled`)
- [ ] Increase Contrast preference is respected (custom colors provide higher-contrast variants)
- [ ] Larger Text (Dynamic Type) preference is respected (use `Font.TextStyle` in SwiftUI or `UIFontMetrics` in UIKit)

---

## Anti-Patterns for TV

**Do not** bring mobile patterns directly to tvOS. The following are common mistakes:

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|-------------|-----------------|
| Bottom tab bar | iOS convention; feels wrong on TV | Use top tab bar |
| Small touch targets | Cannot precisely target with swipe navigation | Minimum 250x150pt cards |
| Dense text screens | Unreadable at 10-foot distance | Headlines + short descriptions only |
| Hamburger menus | No tap-to-reveal interaction on TV | Use tab bar or focus-driven menus |
| Pull-to-refresh | No pull gesture on Siri Remote | Auto-refresh or explicit refresh button |
| Toast notifications | Easy to miss on a large TV screen | Use modal alerts or persistent banners |
| Scroll indicators | Thin scrollbars invisible at distance | Use content peek (partially visible next item) |
| Pinch-to-zoom | Multi-finger gestures impossible on Siri Remote | Provide explicit zoom controls |
| Long forms | Keyboard input is painful on tvOS | Pre-fill, use profiles, or offload to iPhone |
| Thin/light typography | Disappears on TV displays | Medium weight minimum |
```

## File: `skills/tvos/metadata.json`
```json
{
  "version": "1.0.0",
  "organization": "Platform Design Skills",
  "date": "February 2026",
  "abstract": "Apple Human Interface Guidelines for Apple TV. 47+ rules across 7 categories covering focus-based navigation, Siri Remote, Top Shelf, parallax icons, living room viewing distances, media playback patterns, and accessibility.",
  "references": [
    "https://developer.apple.com/design/human-interface-guidelines",
    "https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos",
    "https://developer.apple.com/documentation/tvos-release-notes",
    "https://developer.apple.com/documentation/tvservices"
  ]
}
```

## File: `skills/tvos/rules/_sections.md`
```markdown
# tvOS Design Rules -- Sectioned Reference

Quick-access reference organized by category. Each rule has a severity and unique ID for citation.

---

## Section 1: Focus-Based Navigation

| ID | Rule | Severity |
|----|------|----------|
| FOCUS-01 | Every interactive element must have a clearly visible focus state | CRITICAL |
| FOCUS-02 | Focus movement must be predictable and follow logical spatial layout | CRITICAL |
| FOCUS-03 | Use UIFocusGuide to bridge gaps between focusable elements | CRITICAL |
| FOCUS-04 | Apply parallax effect to focused items using layered images (LSR) | CRITICAL |
| FOCUS-05 | Minimum card size 250x150pt for comfortable focus targeting | CRITICAL |
| FOCUS-06 | Provide a default focused element on every screen | CRITICAL |
| FOCUS-07 | Preserve focus memory when returning to a screen | HIGH |
| FOCUS-08 | Never trap focus; users must always be able to move away | CRITICAL |
| FOCUS-09 | Keep row order stable and focus moves local to reduce re-orientation | HIGH |

### Key APIs
- `UIFocusEnvironment`, `UIFocusGuide`, `UIFocusSystem`
- `didUpdateFocus(in:with:)` for tracking focus changes
- `preferredFocusEnvironments` for setting default focus
- Layered images: LSR format via Xcode asset catalog

---

## Section 2: Siri Remote

| ID | Rule | Severity |
|----|------|----------|
| REMOTE-01 | Touch surface swipes control focus; clicks select | CRITICAL |
| REMOTE-02 | Menu button must always navigate back | CRITICAL |
| REMOTE-03 | Play/Pause button must control media playback | CRITICAL |
| REMOTE-04 | Never require complex or multi-finger gestures | CRITICAL |
| REMOTE-05 | Swipe directions must be intuitive and axis-consistent | HIGH |
| REMOTE-06 | Support Siri voice input for search and text entry | HIGH |
| REMOTE-07 | Provide immediate click feedback (visual response) | HIGH |
| REMOTE-08 | Avoid long remote-typed text; prefer dictation, autofill, or code-based flows | HIGH |

### Input Model
- **Touch surface**: Swipe (directional), click (select), long press (context)
- **Menu button**: Back/dismiss -- do not override
- **Play/Pause**: Media transport -- always respect
- **Siri button**: Voice input and search
- **Volume**: System-controlled, do not intercept
- Game controllers supported as secondary input via `GCController`

---

## Section 3: 10-Foot UI

| ID | Rule | Severity |
|----|------|----------|
| DISTANCE-01 | Minimum body text 29pt; titles 48pt+ | HIGH |
| DISTANCE-02 | High contrast: light text on dark backgrounds | HIGH |
| DISTANCE-03 | Limit text per screen; headlines and short descriptions only | HIGH |
| DISTANCE-04 | High-resolution imagery: 1920x1080 minimum, 3840x2160 for 4K | HIGH |
| DISTANCE-05 | Simple, spacious layouts; avoid dense grids | HIGH |
| DISTANCE-06 | Keep content within TV-safe area (60pt inset from edges) | HIGH |
| DISTANCE-07 | Avoid thin fonts and hairline borders; use medium weight minimum | MEDIUM |

### Screen Specifications
- **Resolution**: 1920x1080 (HD), 3840x2160 (4K)
- **Safe area inset**: 60pt from all edges
- **Color space**: Display P3 (wide color) supported
- **Frame rate**: 24fps, 30fps, 60fps content supported
- **HDR**: Dolby Vision and HDR10 supported on Apple TV 4K

---

## Section 4: Top Shelf

| ID | Rule | Severity |
|----|------|----------|
| SHELF-01 | Provide a TVTopShelfContentProvider extension with dynamic content (use TVTopShelfContentProvider, not deprecated TVTopShelfProvider) | HIGH |
| SHELF-02 | Use correct layout: inset banner or sectioned content | HIGH |
| SHELF-03 | Every Top Shelf item must deep-link into corresponding content | HIGH |
| SHELF-04 | Use high-quality imagery at recommended dimensions | HIGH |
| SHELF-05 | Keep content fresh; update regularly | MEDIUM |

### Image Dimensions

| Layout | Asset | Size (@1x) | Size (@2x) |
|--------|-------|-----------|-----------|
| Inset banner | Wide image | 1940x624pt | 3880x1248pt |
| Sectioned | Poster | 404x608pt | 808x1216pt |

### Implementation
- Conform to `TVTopShelfContentProvider` protocol (tvOS 14+); `TVTopShelfProvider` is deprecated
- Return `TVTopShelfSectionedContent` or `TVTopShelfInsetContent`
- Each `TVTopShelfItem` takes a `URL` for deep linking
- System caches and refreshes on its own schedule; call `TVTopShelfContentProvider.topShelfContentDidChange()` to request update

---

## Section 5: Media & Playback

| ID | Rule | Severity |
|----|------|----------|
| MEDIA-01 | Use standard transport controls (play, pause, skip, scrub) | MEDIUM |
| MEDIA-02 | Swipe-down during playback shows info overlay | MEDIUM |
| MEDIA-03 | Support scrubbing via touch surface with thumbnail previews | MEDIUM |
| MEDIA-04 | Provide subtitle and audio track selection | MEDIUM |
| MEDIA-05 | Support Picture in Picture for video content | LOW |
| MEDIA-06 | Remember and resume playback position | MEDIUM |
| MEDIA-07 | Handle interruptions gracefully; save position on app switch | MEDIUM |

### Key APIs
- `AVPlayerViewController` -- standard playback UI with transport controls
- `AVPlayerItem` -- media item with metadata
- `AVPictureInPictureController` -- PiP management
- `AVMediaSelectionGroup` -- subtitle and audio track selection
- `NowPlayingInfo` via `MPNowPlayingInfoCenter` for system integration

---

## Section 6: Tab Bar

| ID | Rule | Severity |
|----|------|----------|
| TAB-01 | Tab bar at top of screen (not bottom) | MEDIUM |
| TAB-02 | Translucent tab bar overlays content with blur | MEDIUM |
| TAB-03 | Use 3-7 tabs | MEDIUM |
| TAB-04 | Every tab must have a text label | MEDIUM |
| TAB-05 | Focus on tab bar should feel lightweight and smooth | LOW |
| TAB-06 | Remember selected tab across app launches | LOW |

### Implementation
- Use `UITabBarController` which automatically positions at top on tvOS
- Tab bar items: `UITabBarItem(title:image:tag:)`
- Store selected tab index in `UserDefaults` for persistence
- Content beneath tab bar should use `additionalSafeAreaInsets` or standard layout guides

---

## Section 7: Accessibility

| ID | Rule | Severity |
|----|------|----------|
| ACCESS-01 | Accessibility label on every interactive element and card | CRITICAL |
| ACCESS-02 | Accessibility hints for non-obvious interactions | HIGH |
| ACCESS-03 | VoiceOver focus order matches visual focus order | HIGH |
| ACCESS-04 | Respect Reduce Motion; disable parallax and decorative animations | HIGH |
| ACCESS-05 | Respond to Bold Text; adapt custom text via legibilityWeight / isBoldTextEnabled | HIGH |
| ACCESS-06 | Respond to Increase Contrast; provide higher-contrast variants via colorSchemeContrast | HIGH |
| ACCESS-07 | Respect Dynamic Type / Larger Text; use Font.TextStyle in SwiftUI or UIFontMetrics in UIKit | HIGH |

**Key principle**: VoiceOver on tvOS navigates via the focus engine. Correct focus configuration ensures VoiceOver users have the same experience as sighted users.

---

## Rule Count by Severity

| Severity | Count |
|----------|-------|
| CRITICAL | 12 |
| HIGH | 22 |
| MEDIUM | 12 |
| LOW | 3 |
| **Total** | **49** |
```

## File: `skills/visionos/AGENTS.md`
```markdown
# visionOS Design Guidelines

Spatial computing design skill based on Apple Human Interface Guidelines for Apple Vision Pro.

## Purpose

Provide authoritative design guidance for visionOS apps covering spatial layout, eye and hand input, windows, volumes, immersive spaces, materials, and ornaments.

## Skill Files

| File | Contents |
|------|----------|
| `SKILL.md` | Complete design guidelines with rules, checklist, and anti-patterns |
| `rules/_sections.md` | Categorized rule reference with severity levels |
| `metadata.json` | Version, references, and abstract |

## Usage

This skill activates when tasks involve:
- visionOS or Apple Vision Pro development
- Spatial UI design and layout
- Eye and hand input implementation
- RealityKit or RealityComposer Pro
- Mixed reality or immersive experience design
- Window, volume, or immersive space architecture

## Rule Categories

| # | Category | Impact |
|---|----------|--------|
| 1 | Spatial Layout | CRITICAL |
| 2 | Eye & Hand Input | CRITICAL |
| 3 | Windows | HIGH |
| 4 | Volumes | HIGH |
| 5 | Immersive Spaces | HIGH |
| 6 | Materials & Depth | MEDIUM |
| 7 | Ornaments | MEDIUM |
| 8 | Accessibility | CRITICAL |

## Priority Levels

- **CRITICAL**: Violations break core spatial UX or cause user discomfort
- **HIGH**: Violations degrade experience significantly
- **MEDIUM**: Violations miss polish or platform conventions

## Never Do

- Never head-lock UI — all content must be world-anchored
- Never place interactive elements below 60pt in size
- Never skip hover/gaze feedback on interactive elements
- Never use gaze direction for analytics or content decisions (privacy violation)
- Never force immersion on launch — start in the Shared Space
- Never trap users in full immersion with no exit
- Never place content behind the user
- Never position windows or objects closer than ~0.5m (personal space)
- Never use opaque backgrounds in shared space (except media)
- Never omit accessibility labels on interactive elements and 3D objects
```

## File: `skills/visionos/SKILL.md`
```markdown
---
name: visionos-design-guidelines
description: Apple Human Interface Guidelines for Apple Vision Pro. Use when building spatial computing apps, implementing eye/hand input, or designing immersive experiences. Triggers on tasks involving visionOS, RealityKit, spatial UI, or mixed reality.
license: MIT
metadata:
  author: platform-design-skills
  version: "1.0.0"
---

# visionOS Design Guidelines

Comprehensive design rules for Apple Vision Pro based on Apple Human Interface Guidelines. These rules ensure spatial computing apps are comfortable, intuitive, and consistent with platform conventions.

---

## 1. Spatial Layout [CRITICAL]

Spatial layout determines user comfort and usability. Poor placement causes neck strain, disorientation, or inaccessible content.

### Rules

**SL-01: Center content in the field of view.**
Place primary windows and content directly ahead of the user at eye level. The comfortable vertical viewing range is approximately 30 degrees above and below eye level. Content outside this range requires head movement and causes fatigue.

**SL-02: Maintain comfortable distance.**
Position content at a natural distance from the user, typically 1-2 meters for windows. Content too close feels invasive; content too far is hard to read. The system default placement is approximately 1.5 meters. Respect this unless there is a strong reason to override.

**SL-03: Never place content behind the user.**
Users cannot see content behind them without physically turning around. All UI elements must appear within the forward-facing hemisphere. If content must surround the user, provide clear navigation to rotate or reposition.

**SL-04: Respect personal space.**
Do not place 3D objects or windows closer than arm's length (~0.5 meters) from the user's head. Objects inside personal space cause discomfort and a feeling of intrusion. Direct-touch interactions are the exception, where objects are intentionally within reach.

**SL-05: Use Z-depth to establish hierarchy.**
Elements closer to the user appear more prominent and interactive. Push secondary or background content further back. Use subtle depth offsets (a few centimeters) between layered elements rather than dramatic separation that fragments the interface.

**SL-06: Manage multiple windows thoughtfully.**
When displaying multiple windows, arrange them in a gentle arc around the user rather than stacking or overlapping. Each window should be individually repositionable. Avoid spawning too many simultaneous windows that overwhelm the space.

**SL-07: Anchor content to the environment, not the head.**
Windows and objects should stay fixed in world space as the user moves their head. Head-locked content (content that follows head movement) causes discomfort and motion sickness. Only use head-relative positioning for brief, transient elements like tooltips.

---

## 2. Eye & Hand Input [CRITICAL]

visionOS uses indirect interaction as its primary input model: users look at a target and pinch to select. This is fundamentally different from touch or mouse input.

### Rules

**EH-01: Design for look-and-pinch as the primary interaction.**
The standard interaction is: user looks at an element (eyes provide targeting), then pinches thumb and index finger together (hand provides confirmation). Design all primary interactions around this model. Users do not need to raise their hands or point at objects.

**EH-02: Minimum interactive target size is 60pt.**
Eye tracking has inherent imprecision. All tappable elements must be at least 60 points in diameter to be reliably targeted by gaze. This is larger than iOS touch targets (44pt). Smaller targets cause frustration and mis-selections.

**Correct:**
```swift
// visionOS — button meeting 60pt minimum
Button(action: confirmAction) {
    Label("Confirm", systemImage: "checkmark")
        .frame(minWidth: 60, minHeight: 60)
        .padding(.horizontal, 16)
}
.buttonStyle(.borderedProminent)
```

**Incorrect:**
```swift
// visionOS — 32pt button too small for reliable gaze targeting
Button(action: confirmAction) {
    Image(systemName: "checkmark")
        .frame(width: 32, height: 32)  // Below 60pt minimum; unreliable with eye tracking
}
```

**EH-03: Provide hover feedback on gaze.**
When the user's eyes rest on an interactive element, show a visible highlight or subtle expansion to confirm the element is targeted. This feedback is essential because there is no cursor. Without hover states, users cannot tell what they are about to select.

**EH-04: Support direct touch for close-range objects.**
When 3D objects or UI elements are within arm's reach, allow direct touch interaction (physically reaching out and tapping). Direct touch should feel natural: provide visual and audio feedback on contact. Use direct touch for immersive experiences where it enhances presence.

**EH-05: Never track gaze for content purposes.**
Eye position is used exclusively for system interaction targeting. Do not use gaze direction to infer user interest, change content based on what the user looks at, or record where the user looks. This is a core privacy principle of the platform. The system does not expose raw eye-tracking data to apps.

**EH-06: Keep custom gestures simple and intuitive.**
If you define custom hand gestures beyond the system pinch, ensure they are easy to discover, physically comfortable to perform, and do not conflict with system gestures. Avoid gestures that require sustained hand raising, complex finger patterns, or two-handed coordination for basic actions.

**EH-07: Do not require precise hand positioning.**
Users interact with hands resting naturally in their lap or at their sides. Do not require users to hold their hands in specific positions, reach to specific locations, or maintain sustained gestures. The indirect interaction model exists specifically to reduce physical effort.

**EH-08: Confirm intent at the start of the interaction.**
As soon as the system recognizes gaze target, pinch, drag pickup, or direct touch contact, show a visible state change. Delayed confirmation breaks the eye-hand loop and makes selection feel uncertain.

### Spatial Interaction Quick Reference

| Interaction | Method | Use Case |
|---|---|---|
| Tap / Select | Look + pinch | Buttons, links, list items |
| Scroll | Look + pinch-and-drag | Lists, long content |
| Zoom | Two-hand pinch | Maps, images, 3D models |
| Rotate | Two-hand twist | 3D object manipulation |
| Drag | Look + pinch-hold-and-move | Repositioning windows |
| Direct touch | Reach and tap | Close-range 3D objects |
| Long press | Look + pinch-and-hold | Context menus |

### Target Size Reference

| Element | Minimum Size | Recommended Size |
|---|---|---|
| Buttons | 60pt | 60-80pt |
| List rows | 60pt height | 80pt height |
| Tab bar items | 60pt | 72pt |
| Close/dismiss | 60pt | 60pt |
| Toolbar items | 60pt | 60pt |
| 3D interactive objects | 60pt equivalent | Scale to context |

---

## 3. Windows [HIGH]

Windows in visionOS float in the user's physical space. They use a glass material that blends with the real-world environment.

### Rules

**WN-01: Use glass material as the default window background.**
The system glass material dynamically adapts to the user's real-world surroundings, providing a consistent and readable backdrop. Do not replace glass with opaque solid colors unless you have a specific design reason (such as media playback). Glass grounds the interface in the shared space.

**WN-02: Maintain standard window controls.**
Windows include a system-provided window bar at the bottom for repositioning and a close button. Do not hide, override, or replace these controls. Users rely on consistent window management across all apps.

**WN-03: Make windows resizable when appropriate.**
If your content benefits from different sizes (documents, browsers, media), support window resizing. Use the system resize handle. Define reasonable minimum and maximum sizes. Adapt layout responsively as the window resizes.

**WN-04: Place the tab bar as a leading ornament (left side).**
On visionOS, the tab bar (app navigation) is positioned as a vertical ornament on the leading (left) edge of the window, not at the bottom as on iOS. This keeps navigation accessible without consuming window content area. Use SF Symbols for tab icons.

**WN-05: Place the toolbar as a bottom ornament.**
Primary action controls appear in a toolbar ornament anchored to the bottom edge of the window. This positions controls near the user's natural hand resting position and keeps the content area unobstructed.

**WN-06: Windows float in space with no fixed screen.**
There is no fixed display. Windows exist in the user's physical environment. Design content that looks correct when viewed from slight angles and at varying distances. Avoid designs that assume a fixed viewport size or pixel-perfect positioning.

---

## 4. Volumes [HIGH]

Volumes display 3D content within a bounded box. They are ideal for 3D models, visualizations, and objects users can examine from multiple angles.

### Rules

**VL-01: Contain 3D content within the volume bounds.**
All content must fit within the defined volume dimensions. Content that escapes the bounds will be clipped. Size the volume appropriately for the content it holds and respect the system-enforced limits.

**VL-02: Design for viewing from all angles.**
Users can physically walk around a volume or reposition it. Ensure 3D content looks correct from all viewing angles, not just the front. Avoid flat facades that look like cardboard cutouts from the side.

**VL-03: Do not require a specific viewing position.**
The user may view the volume from above, below, or any side. Content must remain comprehensible regardless of viewing angle. If orientation matters, use visual cues (a base, a label) rather than forcing a specific position.

**VL-04: Scale content appropriately for the space.**
Volumes should be sized relative to their content and the user's environment. A molecular model might be small and held at arm's length. An architectural visualization might fill a table. Consider the context in which users will interact with the volume.

**VL-05: Use volumes for self-contained 3D experiences.**
Volumes are not windows with 3D objects inside them. Use volumes when the 3D content is the primary experience (examining a product model, viewing a 3D chart). Use windows for primarily 2D interfaces that may include some 3D elements.

---

## 5. Immersive Spaces [HIGH]

visionOS supports a spectrum of immersion from shared space (apps alongside reality) to full immersion (complete virtual environment).

### Rules

**IS-01: Start in the Shared Space.**
Apps launch into the Shared Space by default, where multiple app windows coexist alongside the real world. Only transition to more immersive experiences when the user explicitly requests it. Do not force immersion on launch.

**IS-02: Use progressive immersion.**
Move through immersion levels gradually: Shared Space (windows alongside reality) to Full Space (your app takes over but passthrough remains) to Full Immersion (completely virtual environment). Each step should feel intentional and user-initiated.

**IS-03: Always provide an exit path.**
Users must always be able to return to a less immersive state or exit the experience entirely. The Digital Crown is the system-level escape. Within your app, provide clear controls to reduce immersion. Never trap users in an immersive experience.

**IS-04: Use passthrough for safety.**
In experiences where users might move physically, maintain passthrough of the real environment or provide a guardian boundary. Users need awareness of physical obstacles, other people, and room boundaries. Full immersion is only appropriate when the user is stationary.

**IS-05: Dim passthrough gradually.**
When transitioning to increased immersion, dim the passthrough environment gradually rather than cutting to black. Abrupt visual changes are disorienting. Use smooth, animated transitions between immersion levels.

**IS-06: Do not assume room layout or size.**
Users are in diverse physical spaces. Do not design experiences that require a minimum room size, assume a clear floor area, or expect specific furniture placement. Gracefully adapt to whatever physical space is available.

**IS-07: Provide spatial audio cues.**
In immersive spaces, use spatial audio to help users orient. Sounds should come from the direction of their source in the virtual environment. Audio cues can guide attention and provide feedback without requiring visual focus.

---

## 6. Materials & Depth [MEDIUM]

visionOS uses a physically-based material system that responds to real-world lighting. Proper use of materials creates depth hierarchy and ensures readability.

### Rules

**MD-01: Use the system glass material for UI surfaces.**
The glass material is the foundation of visionOS UI. It provides depth, translucency, and environmental integration. Use the system-provided glass variants (regular, thin, ultra-thin) rather than custom translucent materials.

**MD-02: Specular highlights respond to the environment.**
Materials in visionOS react to real-world lighting conditions. Design elements that leverage this: subtle specular highlights on interactive elements reinforce their dimensionality. Do not flatten materials with purely matte surfaces.

**MD-03: Layer materials to create depth hierarchy.**
Use lighter/thicker glass for foreground elements and darker/thinner glass for background. Sidebars use a slightly different glass tint than content areas. This layering creates natural visual hierarchy without sharp borders.

**MD-04: Apply vibrancy for text readability.**
Text over glass materials uses vibrancy effects to remain legible regardless of the background environment. Use the system text styles which include appropriate vibrancy. Custom text rendering over glass must account for varying background lightness and color.

**MD-05: Use shadows and highlights for elevation.**
Elements that float above the window surface (popovers, menus, hover states) should cast subtle shadows and show slight specular highlights on their upper edges. These depth cues help users understand the spatial relationship between interface layers.

**MD-06: Avoid fully opaque backgrounds in shared space.**
Opaque surfaces in the shared space create visual holes in the environment. Use translucent glass materials that let the environment show through. Exceptions include media playback (video, photos) where an opaque background improves the viewing experience.

---

## 7. Ornaments [MEDIUM]

Ornaments are UI controls that attach to the edges of windows, floating partially outside the window bounds. They provide toolbars, navigation, and contextual actions.

### Rules

**OR-01: Attach controls as ornaments rather than inline.**
Toolbars, tab bars, and persistent action buttons belong as ornaments, not embedded within the window content area. Ornaments keep the content area clean and establish a clear spatial hierarchy between controls and content.

**OR-02: Place primary actions in the bottom ornament.**
The bottom edge ornament is the primary location for action controls (play/pause, formatting tools, share). This position is ergonomically accessible and visually prominent without obscuring content.

**OR-03: Place navigation in the leading (left) ornament.**
App-level navigation (tab bar equivalent) attaches to the leading edge of the window. This keeps navigation persistent and accessible while leaving the content area and bottom ornament for contextual controls.

**OR-04: Do not occlude window content with ornaments.**
Ornaments extend outward from the window edge, not inward. They should not cover or overlap the window's content area. Size ornaments appropriately so they remain functional without becoming visually dominant over the content.

**OR-05: Show ornaments contextually when appropriate.**
Not all ornaments need to be visible at all times. Toolbars can appear on hover (when the user looks at the window) and fade when the user looks away. This keeps the interface clean while maintaining discoverability.

**OR-06: Use standard ornament styling.**
Ornaments use the same glass material system as windows but at a slightly different depth. Use system-provided ornament containers rather than custom floating UI. This ensures visual consistency with other visionOS apps.

**OR-07: Keep essential controls discoverable.**
Use ornaments for commands users must revisit repeatedly, such as navigation, playback, or primary actions. Do not hide essential controls behind memorized gestures or hover-only affordances.

---

## 8. Accessibility [CRITICAL]

visionOS supports VoiceOver, Switch Control, and pointer control alternatives. Spatial UI must be navigable without relying solely on eye and hand input.

### Rules

**ACC-01: Every interactive element must have a meaningful accessibility label.**
Buttons, controls, and 3D objects that users can interact with must have labels VoiceOver can announce. Do not rely on visual appearance or position alone.

**ACC-02: VoiceOver must be able to reach all interactive elements.**
Ensure the accessibility tree covers all focusable controls. Custom `RealityKit` entities that are interactive must be registered in the accessibility hierarchy.

**ACC-03: Support pointer control and Switch Control alternatives.**
Not all users can use eye tracking and hand pinch. Ensure the app is fully navigable via alternative input methods such as head pointer, Switch Control, or keyboard navigation.

**ACC-04: Respect Reduce Motion.**
Spatial animations, immersive transitions, and parallax effects must be disabled or reduced when Reduce Motion is enabled. Abrupt motion in a spatial environment can cause disorientation.

```swift
@Environment(\.accessibilityReduceMotion) var reduceMotion

var body: some View {
    Model3D(named: "SceneObject")
        .rotation3DEffect(reduceMotion ? .zero : rotation, axis: (0, 1, 0))
}
```

**ACC-05: Respond to Bold Text.**
When the user enables Bold Text, custom-rendered text in visionOS must adapt. SwiftUI dynamic type styles handle this automatically; custom rendering must check `UIAccessibility.isBoldTextEnabled` or use `@Environment(\.legibilityWeight)` to detect and apply heavier weights.

**ACC-06: Respond to Increase Contrast.**
When the user enables Increase Contrast, custom colors must provide higher-contrast variants. Use `@Environment(\.colorSchemeContrast)` in SwiftUI to detect `.increased` and substitute higher-contrast color values for text and UI elements rendered against glass or environment backgrounds.

---

## Evaluation Checklist

Use this checklist to evaluate a visionOS design or implementation.

### Spatial Layout
- [ ] Primary content centered in forward field of view
- [ ] Content placed at comfortable distance (1-2m for windows)
- [ ] No content placed behind the user
- [ ] Personal space respected (nothing closer than ~0.5m)
- [ ] Z-depth used meaningfully for hierarchy
- [ ] Multiple windows arranged in arc, not stacked
- [ ] Content anchored to world space, not head-locked

### Eye & Hand Input
- [ ] All interactions work with look-and-pinch
- [ ] All interactive targets >= 60pt
- [ ] Hover states visible on all interactive elements
- [ ] Direct touch supported for close-range objects
- [ ] No gaze tracking for content or analytics purposes
- [ ] Custom gestures are simple and discoverable
- [ ] No sustained hand-raising required

### Windows
- [ ] Glass material used as default background
- [ ] Standard window bar and close button present
- [ ] Tab bar positioned as leading ornament
- [ ] Toolbar positioned as bottom ornament
- [ ] Layout adapts to different window sizes
- [ ] Content designed for floating in space

### Volumes
- [ ] Content contained within volume bounds
- [ ] Content looks correct from all viewing angles
- [ ] No specific viewing position required
- [ ] Scale appropriate for content and context

### Immersive Spaces
- [ ] App starts in Shared Space
- [ ] Immersion increases progressively
- [ ] Clear exit path always available
- [ ] Passthrough maintained where safety requires it
- [ ] Transitions between immersion levels are smooth
- [ ] No assumptions about room size or layout

### Materials & Depth
- [ ] System glass material used for UI surfaces
- [ ] Material layering creates depth hierarchy
- [ ] Text uses vibrancy for readability over glass
- [ ] Shadows and highlights indicate elevation
- [ ] No fully opaque surfaces in shared space (except media)

### Ornaments
- [ ] Controls attached as ornaments, not inline
- [ ] Primary actions in bottom ornament
- [ ] Navigation in leading ornament
- [ ] Ornaments extend outward, not over content
- [ ] Standard ornament styling used

### Accessibility
- [ ] Bold Text preference respected (SwiftUI handles automatically; custom text checks `legibilityWeight` or `UIAccessibility.isBoldTextEnabled`)
- [ ] Increase Contrast preference respected (custom colors provide higher-contrast variants via `colorSchemeContrast`)
- [ ] All interactive elements and 3D objects have meaningful accessibility labels
- [ ] App is fully navigable via head pointer or Switch Control (not solely eye-and-pinch)
- [ ] Spatial animations and immersive transitions disabled or reduced when Reduce Motion is enabled
- [ ] Interactive RealityKit entities are registered in the accessibility hierarchy

---

## Anti-Patterns

These are common mistakes in visionOS design. Avoid them.

| Anti-Pattern | Problem | Correct Approach |
|---|---|---|
| Head-locked UI | Causes motion sickness, feels claustrophobic | Anchor UI to world space |
| Tiny tap targets | Eye tracking cannot reliably target < 60pt | Minimum 60pt interactive targets |
| No hover states | Users cannot tell what is interactive | Always show highlight on gaze |
| Opaque windows in shared space | Creates visual holes in environment | Use system glass material |
| Forced full immersion | Disorienting, traps users | Start in shared space, progressive immersion |
| Content behind user | Invisible, requires full body rotation | Keep content in forward hemisphere |
| Gaze-driven content | Privacy violation, feels surveilled | Use gaze only for system targeting |
| Flat 3D volumes | Looks like cardboard cutout from side | Design for all viewing angles |
| Inline toolbars | Wastes content space, breaks conventions | Use ornaments for controls |
| Small room assumptions | Fails in tight spaces | Adapt to available physical space |
| Abrupt immersion changes | Disorienting, breaks presence | Gradual transitions with animation |
| Sustained arm raising | Physical fatigue in minutes | Design for hands resting at sides |
| Custom window chrome | Breaks platform consistency | Use system window controls |
| Z-fighting layers | Visual flicker, unclear hierarchy | Use intentional depth offsets |
```

## File: `skills/visionos/metadata.json`
```json
{
  "version": "1.0.0",
  "organization": "Platform Design Skills",
  "date": "February 2026",
  "abstract": "Apple Human Interface Guidelines for Apple Vision Pro. 50+ rules across 8 categories covering spatial UI, eye and hand input, windows, volumes, immersive spaces, ornaments, materials for depth hierarchy, and accessibility.",
  "references": [
    "https://developer.apple.com/design/human-interface-guidelines",
    "https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos",
    "https://developer.apple.com/documentation/realitykit",
    "https://developer.apple.com/documentation/visionos"
  ]
}
```

## File: `skills/visionos/rules/_sections.md`
```markdown
# visionOS Design Rules — Categorized Reference

Quick-reference rule index organized by category and severity.

---

## CRITICAL

Rules where violations break core spatial UX or cause user discomfort.

### Spatial Layout

| ID | Rule | Summary |
|---|---|---|
| SL-01 | Center content in field of view | Primary content at eye level, directly ahead |
| SL-02 | Comfortable distance | Windows at 1-2m; default ~1.5m |
| SL-03 | No content behind user | All UI in forward hemisphere |
| SL-04 | Respect personal space | Nothing closer than ~0.5m to head |
| SL-07 | World-anchored, not head-locked | Content fixed in space, not following head |

### Eye & Hand Input

| ID | Rule | Summary |
|---|---|---|
| EH-01 | Look-and-pinch primary interaction | Eyes target, fingers confirm |
| EH-02 | 60pt minimum target size | All interactive elements >= 60pt |
| EH-03 | Hover feedback on gaze | Visible highlight when eye rests on element |
| EH-05 | No gaze tracking for content | Eye data is system-only, never for analytics |
| EH-07 | No precise hand positioning | Users interact with hands at rest |
| EH-08 | Immediate confirmation of gaze, pinch, drag, and touch intent | Visible state change as soon as interaction is recognized |

### Accessibility

| ID | Rule | Summary |
|---|---|---|
| ACC-01 | Accessibility label on all interactive elements | Every button and 3D object needs a label |
| ACC-02 | Full accessibility tree coverage | VoiceOver can reach all interactive elements |
| ACC-03 | Support pointer control and Switch Control | App navigable without eye/hand input |
| ACC-04 | Respect Reduce Motion | Disable spatial animations and transitions |
| ACC-05 | Respond to Bold Text | Custom text adapts via `legibilityWeight` / `isBoldTextEnabled` |
| ACC-06 | Respond to Increase Contrast | Custom colors provide higher-contrast variants via `colorSchemeContrast` |

---

## HIGH

Rules where violations significantly degrade the experience.

### Spatial Layout

| ID | Rule | Summary |
|---|---|---|
| SL-05 | Z-depth for hierarchy | Closer = more prominent; subtle offsets |
| SL-06 | Manage multiple windows | Arc arrangement, individually repositionable |

### Eye & Hand Input

| ID | Rule | Summary |
|---|---|---|
| EH-04 | Direct touch for close range | Physical tap on objects within reach |
| EH-06 | Simple custom gestures | Easy to discover, comfortable, no conflicts |

### Windows

| ID | Rule | Summary |
|---|---|---|
| WN-01 | Glass material background | System glass adapts to environment |
| WN-02 | Standard window controls | System window bar and close button |
| WN-03 | Resizable windows | Support resize with responsive layout |
| WN-04 | Tab bar as leading ornament | Vertical nav on left edge |
| WN-05 | Toolbar as bottom ornament | Primary actions along bottom edge |
| WN-06 | Windows float in space | No fixed screen assumptions |

### Volumes

| ID | Rule | Summary |
|---|---|---|
| VL-01 | Content within bounds | No clipping; size volume to content |
| VL-02 | Viewable from all angles | No flat facades |
| VL-03 | No required viewing position | Comprehensible from any angle |
| VL-04 | Appropriate scale | Size relative to content and environment |
| VL-05 | Volumes for 3D-primary experiences | Not windows with 3D inside |

### Immersive Spaces

| ID | Rule | Summary |
|---|---|---|
| IS-01 | Start in Shared Space | Default to windows alongside reality |
| IS-02 | Progressive immersion | Shared Space -> Full Space -> Full Immersion |
| IS-03 | Always provide exit path | Digital Crown + in-app controls |
| IS-04 | Passthrough for safety | Maintain awareness of physical environment |
| IS-05 | Gradual passthrough dimming | Smooth transitions, no hard cuts |
| IS-06 | No room assumptions | Adapt to available physical space |
| IS-07 | Spatial audio cues | Sound from source direction |

---

## MEDIUM

Rules where violations miss platform polish or conventions.

### Materials & Depth

| ID | Rule | Summary |
|---|---|---|
| MD-01 | System glass material | Use provided glass variants |
| MD-02 | Environment-responsive highlights | Materials react to real-world light |
| MD-03 | Layered materials for hierarchy | Lighter/thicker glass = foreground |
| MD-04 | Vibrancy for text | System text styles with vibrancy |
| MD-05 | Shadows and highlights for elevation | Depth cues on floating elements |
| MD-06 | No opaque backgrounds in shared space | Translucent glass; opaque only for media |

### Ornaments

| ID | Rule | Summary |
|---|---|---|
| OR-01 | Controls as ornaments | Not inline within content |
| OR-02 | Primary actions bottom | Bottom ornament for main controls |
| OR-03 | Navigation on leading edge | Tab bar on left side |
| OR-04 | No content occlusion | Ornaments extend outward |
| OR-05 | Contextual visibility | Show/hide on hover when appropriate |
| OR-06 | Standard ornament styling | System glass containers |
| OR-07 | Keep essential controls discoverable | Do not hide core actions behind memorized gestures or hover-only affordances |

---

## Rule Count Summary

| Category | Count | Severity |
|---|---|---|
| Spatial Layout | 7 | 5 CRITICAL, 2 HIGH |
| Eye & Hand Input | 8 | 6 CRITICAL, 2 HIGH |
| Windows | 6 | 6 HIGH |
| Volumes | 5 | 5 HIGH |
| Immersive Spaces | 7 | 7 HIGH |
| Materials & Depth | 6 | 6 MEDIUM |
| Ornaments | 7 | 7 MEDIUM |
| Accessibility | 6 | 6 CRITICAL |
| **Total** | **52** | |
```

## File: `skills/watchos/AGENTS.md`
```markdown
# watchOS Design Guidelines

## Purpose

This skill provides Apple Human Interface Guidelines for Apple Watch. Load it when working on watchOS apps, complications, workout features, or any wrist-based interaction design.

## When to Use

- Building or reviewing watchOS app interfaces
- Designing complications for watch faces
- Implementing Digital Crown interactions
- Creating workout or health tracking features
- Designing notifications for Apple Watch
- Evaluating glanceability of Watch UI
- Working with Always On display states

## File Structure

| File | Contents |
|------|----------|
| `SKILL.md` | Complete design rules, specifications, and evaluation checklist |
| `rules/_sections.md` | All rules organized by category with IDs for cross-reference |
| `metadata.json` | Version, references, and abstract |

## Key Principles

1. **Glanceable first** -- every screen must communicate its purpose within 2 seconds
2. **Respect the wrist** -- interactions should be brief; avoid complex multi-step flows
3. **Digital Crown is primary** -- scroll, select, and adjust values with the Crown
4. **Complications drive engagement** -- keep watch face data fresh and useful
5. **Always On awareness** -- dim gracefully, hide sensitive content

## Rule Categories

| # | Category | Priority |
|---|----------|----------|
| 1 | Glanceable Design | CRITICAL |
| 2 | Digital Crown | HIGH |
| 3 | Navigation | HIGH |
| 4 | Complications | HIGH |
| 5 | Always On Display | MEDIUM |
| 6 | Workouts & Health | MEDIUM |
| 7 | Notifications | MEDIUM |
| 8 | Accessibility | CRITICAL |

## Priority Reference

| Level | Meaning |
|-------|---------|
| CRITICAL | Glanceable design, accessibility -- violations make the app unusable on Watch |
| HIGH | Digital Crown, navigation, complications -- core Watch interaction patterns |
| MEDIUM | Always On, workouts, notifications -- important but context-dependent |

## Never Do

- Never place primary information off-screen (requires scrolling to see)
- Never ignore the Digital Crown for scrollable or value-picking content
- Never override system Crown behaviors (volume, Time Travel)
- Never support only one complication family
- Never use deprecated ClockKit APIs -- use WidgetKit complication families
- Never show sensitive health data in the Always On dimmed state
- Never omit accessibility labels on image-only interactive elements
- Never use laggy or batched responses to Crown rotation
```

## File: `skills/watchos/SKILL.md`
```markdown
---
name: watchos-design-guidelines
description: Apple Human Interface Guidelines for Apple Watch. Use when building watchOS apps, complications, or workout features. Triggers on tasks involving Watch UI, Digital Crown, glanceable interfaces, or wrist-based interactions.
license: MIT
metadata:
  author: platform-design-skills
  version: "1.0.0"
---

# watchOS Design Guidelines

Apple Watch is a personal, glanceable device worn on the wrist. Interactions are measured in seconds, not minutes. Every design decision must prioritize speed of comprehension and brevity of interaction.

---

## 1. Glanceable Design (CRITICAL)

The defining constraint of watchOS. If a user cannot extract the key information within 2 seconds of raising their wrist, the design has failed.

### Rules

- **W-GL-01**: Primary information must be visible without scrolling. The first screen is the only guaranteed screen.
- **W-GL-02**: Target interaction sessions of 5 seconds or less. Design for raise-glance-lower.
- **W-GL-03**: Use large, high-contrast text. Minimum effective body text is 16pt (system font). Titles should be 18pt or larger.
- **W-GL-04**: Limit text to essential content. Truncate or abbreviate aggressively. Use SF Symbols instead of text labels where meaning is unambiguous.
- **W-GL-05**: Respect wrist-down time. When the wrist lowers, the app enters an inactive state. Do not assume continuous user attention.
- **W-GL-06**: Prioritize a single piece of information per screen. If showing multiple data points, establish clear visual hierarchy with size, weight, and color.

### Screen Dimensions Reference

| Device | Screen Width | Screen Height | Corner Radius |
|--------|-------------|---------------|---------------|
| 41mm (Series 9) | 176px | 215px | 36px |
| 45mm (Series 9) | 198px | 242px | 39px |
| 42mm (Series 10) | 180px | 220px | 37px |
| 46mm (Series 10) | 205px | 251px | 40px |
| 49mm (Ultra 2) | 205px | 251px | 40px |

### Anti-Patterns

- Walls of text requiring scroll to understand context
- Small, dense data tables
- Requiring multiple taps before showing useful information
- Replicating an iPhone screen layout on Watch

---

## 2. Digital Crown (HIGH)

The Digital Crown is the primary physical input for scrolling and precise value selection. It provides haptic feedback and should feel purposeful.

### Rules

- **W-DC-01**: Use the Digital Crown as the primary scroll mechanism for vertical content. Do not rely solely on swipe gestures for scrolling.
- **W-DC-02**: For value pickers (time, quantity, sliders), bind the Crown to precise adjustments with haptic detents at each discrete value.
- **W-DC-03**: Do not override or conflict with system Crown behaviors. The system uses the Crown for volume control during media playback, scrolling in system UI, and Time Travel in complications.
- **W-DC-04**: Provide visual feedback synchronized with Crown rotation. The UI must respond frame-by-frame to Crown input with no perceptible lag.
- **W-DC-05**: Update on each Crown increment. Values, selection, and highlight states should move with each detent. Do not debounce Crown input until the gesture ends.

**Correct — Crown binding with haptic detents:**
```swift
struct VolumePickerView: View {
    @State private var volume: Double = 0.5

    var body: some View {
        VStack {
            Text("\(Int(volume * 100))%")
                .font(.title.bold())
            Image(systemName: "speaker.wave.3")
        }
        .focusable()
        .digitalCrownRotation(
            $volume,
            from: 0.0,
            through: 1.0,
            by: 0.05,
            sensitivity: .medium,
            isContinuous: false,
            isHapticFeedbackEnabled: true
        )
    }
}
```

**Incorrect — ignoring the Crown and forcing touch-only interaction:**
```swift
struct VolumePickerView: View {
    @State private var volume: Double = 0.5

    var body: some View {
        Slider(value: $volume)
        // No .digitalCrownRotation — Crown input is ignored
        // Users must use touch-only, which is imprecise and frustrating on Watch
    }
}
```

### Anti-Patterns

- Ignoring the Crown and forcing all interaction through touch
- Custom Crown behaviors that conflict with system expectations
- Missing haptic feedback on discrete value changes
- Laggy or batched responses to Crown rotation

---

## 3. Navigation (HIGH)

Watch navigation must be shallow and predictable. Users should never feel lost or unable to return to a known state.

### Rules

- **W-NV-01**: Use vertical page scrolling as the default content navigation pattern. Pages scroll top-to-bottom with the Digital Crown.
- **W-NV-02**: Use `TabView` for top-level sections (max 5 tabs). Swipe horizontally between tabs. Each tab is a distinct functional area.
- **W-NV-03**: Use `NavigationStack` for hierarchical drill-down. Limit hierarchy to 2-3 levels maximum. Every pushed view must have a back button (provided automatically by the system).
- **W-NV-04**: Avoid modal sheets for primary flows. Modals should be reserved for focused, single-purpose tasks (e.g., confirmation, quick input).
- **W-NV-05**: The app's most important action should be reachable within 1 tap from launch. Do not bury primary functionality behind menus or navigation.

### Navigation Pattern Reference

| Pattern | Use Case | Gesture |
|---------|----------|---------|
| Vertical scroll | Long-form content within a single view | Digital Crown / swipe up-down |
| TabView (horizontal pages) | Top-level app sections | Swipe left-right |
| NavigationStack (push/pop) | Hierarchical drill-down | Tap to push, swipe right or back button to pop |
| Modal sheet | Confirmation, focused input | Presented programmatically, dismiss via button or swipe down |

### Anti-Patterns

- Deep navigation hierarchies (4+ levels)
- Hamburger menus or hidden navigation drawers
- Tab bars with more than 5 items
- Forcing users to scroll through long lists to find key actions

---

## 4. Complications (HIGH)

Complications are the most visible surface of a Watch app. They live on the watch face and provide at-a-glance data without launching the app.

### Rules

- **W-CP-01**: Support multiple complication families to maximize watch face compatibility. At minimum support `accessoryCircular`, `accessoryCorner`, and `accessoryRectangular` (WidgetKit, watchOS 9+).
- **W-CP-02**: Provide both tinted (single-color) and full-color variants. Tinted complications must remain legible when the system applies a single tint color.
- **W-CP-03**: Update complications via `TimelineProvider`. Provide future timeline entries when data is predictable (e.g., next calendar event, weather forecast). Keep data fresh -- stale complications erode trust.
- **W-CP-04**: Complication content must be meaningful without context. A user glancing at their watch face should immediately understand the data (e.g., "72F" not "72").
- **W-CP-05**: Tapping a complication must launch the app to a relevant context, not just the app's root view.

**Correct — WidgetKit TimelineProvider for an accessoryCircular complication:**
```swift
struct StepCountProvider: TimelineProvider {
    func placeholder(in context: Context) -> StepEntry {
        StepEntry(date: Date(), steps: 5000)
    }

    func getSnapshot(in context: Context, completion: @escaping (StepEntry) -> Void) {
        completion(StepEntry(date: Date(), steps: HealthStore.shared.todaySteps))
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<StepEntry>) -> Void) {
        let entry = StepEntry(date: Date(), steps: HealthStore.shared.todaySteps)
        // Refresh in 15 minutes
        let nextUpdate = Calendar.current.date(byAdding: .minute, value: 15, to: Date())!
        completion(Timeline(entries: [entry], policy: .after(nextUpdate)))
    }
}

struct StepCountComplicationView: View {
    let entry: StepEntry

    var body: some View {
        Gauge(value: Double(entry.steps), in: 0...10000) {
            Image(systemName: "figure.walk")
        } currentValueLabel: {
            Text("\(entry.steps / 1000)k")
        }
        .gaugeStyle(.accessoryCircular)
    }
}
```

### Complication Family Reference

Use `WidgetFamily` values:

| Family | Shape | Typical Content |
|--------|-------|-----------------|
| `accessoryCircular` | Small circle | Single value, icon, or gauge |
| `accessoryCorner` | Curved, top corners | Gauge with label, or text with icon |
| `accessoryRectangular` | Wide rectangle | Multi-line text, chart, or detailed view |
| `accessoryInline` | Text row | Short label or value |

### Anti-Patterns

- Supporting only one complication family
- Stale data that does not update for hours
- Complication tap landing on generic app home instead of relevant content
- Illegible complications in tinted mode (insufficient contrast)

---

## 5. Always On Display (MEDIUM)

When the user's wrist is down, watchOS enters an Always On state showing a dimmed version of the current app. This must be handled intentionally.

### Rules

- **W-AO-01**: Reduce visual complexity in the Always On state. Remove animations, secondary UI elements, and non-essential detail. Keep only the most critical information visible.
- **W-AO-02**: Hide sensitive or private data (e.g., message content, health details, financial information) in the dimmed state. Use redacted or placeholder content.
- **W-AO-03**: Reduce update frequency in Always On. Update the display no more than once per minute. Use `TimelineView` with a `.everyMinute` schedule for time-sensitive content.
- **W-AO-04**: Use the system-provided dimming behaviors. Do not implement custom dimming. The system automatically reduces brightness and can apply a tint. Ensure your content remains legible at reduced brightness.
- **W-AO-05**: Test both active and Always On states. The transition between states must feel seamless -- layout should not shift or jump when the wrist raises.

### Anti-Patterns

- Showing identical UI in active and Always On states (wastes battery, may expose private data)
- Animations or frequent updates in Always On state
- Layout shifts when transitioning between active and dimmed states
- Forgetting to redact sensitive information

---

## 6. Workouts & Health (MEDIUM)

Workout and health apps have unique requirements: extended sessions, live metrics, and body-awareness features.

### Rules

- **W-WK-01**: Display live workout metrics in large, high-contrast text. Heart rate, duration, distance, and calories should be readable mid-exercise without stopping.
- **W-WK-02**: Use haptic feedback for milestones (lap completed, goal reached, heart rate zone change). Haptics are essential because users may not be looking at the screen during exercise.
- **W-WK-03**: Support auto-pause detection for relevant workout types (running, walking). Users expect the workout to pause when they stop moving and resume when they start again.
- **W-WK-04**: Enable WaterLock during swimming workouts. This disables the touchscreen to prevent water interaction. The Digital Crown is used to eject water and unlock.
- **W-WK-05**: Show a clear summary screen at workout completion with key metrics. Allow the user to save or discard the workout with a single action.

### Anti-Patterns

- Small metric text that requires squinting or stopping to read
- Missing haptic feedback for important workout events
- No auto-pause support for outdoor workouts
- Requiring complex interaction to end or save a workout

---

## 7. Notifications (MEDIUM)

Watch notifications must be brief and actionable. The user's wrist is raised for only a moment.

### Rules

- **W-NT-01**: Design Short Look notifications with only a title, app icon, and app name. This is what the user sees on initial wrist raise. It must communicate the notification's purpose instantly.
- **W-NT-02**: Design Long Look notifications with full content and up to 4 action buttons. The user reaches Long Look by continuing to look at the notification. Include the most useful actions inline.
- **W-NT-03**: Use appropriate haptic notification types. Match the urgency: `.notification` for standard alerts, `.directionUp` for positive events, `.directionDown` for negative events, `.success`/`.failure`/`.retry` for outcomes.
- **W-NT-04**: Do not over-notify. Excessive notifications cause users to disable them entirely. Batch non-urgent updates. Reserve Watch notifications for time-sensitive or actionable information.

### Haptic Type Reference

| Haptic | Use Case |
|--------|----------|
| `.notification` | General alerts |
| `.directionUp` | Positive event (goal reached, stock up) |
| `.directionDown` | Negative event (stock down, weather warning) |
| `.success` | Action completed successfully |
| `.failure` | Action failed |
| `.retry` | Try again prompt |
| `.start` | Activity beginning |
| `.stop` | Activity ending |
| `.click` | Discrete selection (Crown detent, picker) |

### Anti-Patterns

- Sending every iPhone notification to the Watch
- Notifications without actionable buttons (forcing app launch)
- Using the same haptic type for all notifications regardless of content
- Long notification text that requires extensive scrolling

---

## 8. Accessibility (CRITICAL)

Apple Watch supports VoiceOver and other assistive technologies. Complications and app UI must be accessible.

### Rules

- **W-AC-01**: Every interactive element must have a meaningful accessibility label. SF Symbol names are not sufficient labels. Use `.accessibilityLabel()` on image-only buttons.
- **W-AC-02**: VoiceOver must be able to navigate all app content. Do not hide essential information from the accessibility hierarchy.
- **W-AC-03**: Provide accessibility values and hints for custom controls (e.g., gauges, progress indicators, custom pickers). Use `.accessibilityValue()` and `.accessibilityHint()`.
- **W-AC-04**: Respect Reduce Motion. Disable or substitute decorative animations when enabled. Use `@Environment(\.accessibilityReduceMotion)`.
- **W-AC-05**: Respond to Bold Text. When the user enables Bold Text, custom text must adapt. SwiftUI dynamic type handles this automatically; custom-drawn text must check `@Environment(\.legibilityWeight)`.
- **W-AC-06**: Respond to Increase Contrast. When the user enables Increase Contrast, custom colors must provide higher-contrast variants. Use `@Environment(\.colorSchemeContrast)` to detect the user's preference.

**Correct:**
```swift
Button(action: startWorkout) {
    Image(systemName: "play.fill")
}
.accessibilityLabel("Start workout")
```

**Incorrect:**
```swift
Button(action: startWorkout) {
    Image(systemName: "play.fill")
}
// VoiceOver reads "play" — not clear what action this performs
```

### Anti-Patterns

- Image-only buttons with no accessibility label
- Custom controls with no accessibility value or hint
- Animations that do not respect Reduce Motion
- Hiding content from the accessibility tree that sighted users can see

---

## Evaluation Checklist

Use this checklist when reviewing a watchOS design or implementation.

### Glanceability
- [ ] Can the user understand the primary content within 2 seconds?
- [ ] Is the most important information visible without scrolling?
- [ ] Is body text at least 16pt with sufficient contrast?
- [ ] Are interactions completable in under 5 seconds?

### Digital Crown
- [ ] Does the Crown scroll vertical content?
- [ ] Do value pickers provide haptic detents?
- [ ] Are there no conflicts with system Crown behaviors?

### Navigation
- [ ] Is the primary action reachable within 1 tap from launch?
- [ ] Is the navigation hierarchy 3 levels or fewer?
- [ ] Does every pushed view have a back button?
- [ ] Are top-level sections organized in a TabView (if applicable)?

### Complications
- [ ] Are multiple complication families supported?
- [ ] Do complications work in both tinted and full-color modes?
- [ ] Is complication data updated via TimelineProvider?
- [ ] Does tapping a complication open relevant context?

### Always On
- [ ] Is sensitive data hidden in the dimmed state?
- [ ] Is visual complexity reduced when inactive?
- [ ] Is the update frequency limited to once per minute or less?
- [ ] Is the transition between active and dimmed seamless (no layout shift)?

### Workouts
- [ ] Are live metrics displayed in large, high-contrast text?
- [ ] Are haptics used for milestones?
- [ ] Is auto-pause supported for applicable workout types?
- [ ] Is the workout summary accessible with a single action?

### Notifications
- [ ] Is the Short Look meaningful (title + icon)?
- [ ] Does the Long Look include inline actions?
- [ ] Are haptic types matched to notification urgency?
- [ ] Is notification frequency appropriate (not excessive)?

### Accessibility
- [ ] All interactive elements have meaningful accessibility labels (no raw SF Symbol names)
- [ ] Custom controls provide accessibility values and hints via `.accessibilityValue()` / `.accessibilityHint()`
- [ ] VoiceOver can navigate all app content — no essential content hidden from the accessibility tree
- [ ] Animations respect Reduce Motion (`@Environment(\.accessibilityReduceMotion)`)
- [ ] Bold Text preference is respected (SwiftUI handles automatically; custom text checks `@Environment(\.legibilityWeight)`)
- [ ] Increase Contrast preference is respected (custom colors provide higher-contrast variants)
```

## File: `skills/watchos/metadata.json`
```json
{
  "version": "1.0.0",
  "organization": "Platform Design Skills",
  "date": "February 2026",
  "abstract": "Apple Human Interface Guidelines for Apple Watch. 40+ rules across 8 categories covering glanceable interfaces, Digital Crown, complications, Always On display, workout tracking, wrist-optimized interactions, and accessibility.",
  "references": [
    "https://developer.apple.com/design/human-interface-guidelines",
    "https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos",
    "https://developer.apple.com/documentation/watchkit",
    "https://developer.apple.com/documentation/widgetkit"
  ]
}
```

## File: `skills/watchos/rules/_sections.md`
```markdown
# watchOS Design Rules -- Section Index

All rules organized by category with stable IDs for cross-referencing.

---

## Section 1: Glanceable Design [CRITICAL]

| ID | Rule | Priority |
|----|------|----------|
| W-GL-01 | Primary info visible without scrolling | CRITICAL |
| W-GL-02 | Target 5-second interaction sessions | CRITICAL |
| W-GL-03 | Large, high-contrast text (min 16pt body, 18pt+ titles) | CRITICAL |
| W-GL-04 | Minimize text; use SF Symbols over labels | CRITICAL |
| W-GL-05 | Respect wrist-down (inactive) state | CRITICAL |
| W-GL-06 | One primary data point per screen; clear visual hierarchy | CRITICAL |

**Rationale**: The wrist is the most constrained display surface. Users raise their wrist for a glance, not a reading session. Every pixel must justify its presence.

---

## Section 2: Digital Crown [HIGH]

| ID | Rule | Priority |
|----|------|----------|
| W-DC-01 | Crown is primary scroll input for vertical content | HIGH |
| W-DC-02 | Bind Crown to value pickers with haptic detents | HIGH |
| W-DC-03 | Never override system Crown behaviors | HIGH |
| W-DC-04 | Visual feedback must be frame-synced to Crown rotation | HIGH |
| W-DC-05 | Update values and highlights on each Crown increment | HIGH |

**Rationale**: The Digital Crown is a precision input unique to Apple Watch. It enables interaction without obscuring the small display with fingers, but only if response stays causally linked to each detent.

---

## Section 3: Navigation [HIGH]

| ID | Rule | Priority |
|----|------|----------|
| W-NV-01 | Default to vertical page scrolling | HIGH |
| W-NV-02 | TabView for top-level sections (max 5 tabs) | HIGH |
| W-NV-03 | NavigationStack for hierarchy (max 2-3 levels deep) | HIGH |
| W-NV-04 | Reserve modals for focused single-purpose tasks | HIGH |
| W-NV-05 | Primary action reachable within 1 tap from launch | HIGH |

**Rationale**: Users do not explore on a Watch. They arrive with intent and must reach their goal immediately. Deep hierarchies create frustration on a small screen.

---

## Section 4: Complications [HIGH]

| ID | Rule | Priority |
|----|------|----------|
| W-CP-01 | Support multiple complication families | HIGH |
| W-CP-02 | Provide tinted and full-color variants | HIGH |
| W-CP-03 | Update via TimelineProvider; keep data fresh | HIGH |
| W-CP-04 | Content meaningful without context (include units/labels) | HIGH |
| W-CP-05 | Tap launches app to relevant context | HIGH |

**API Note**: Complications are built with WidgetKit (watchOS 9+). Use `accessoryCircular`, `accessoryCorner`, `accessoryRectangular`, and `accessoryInline` widget families. ClockKit is deprecated.

**Rationale**: Complications are the primary engagement surface. A well-designed complication delivers value without the user ever launching the app.

---

## Section 5: Always On Display [MEDIUM]

| ID | Rule | Priority |
|----|------|----------|
| W-AO-01 | Reduce visual complexity in dimmed state | MEDIUM |
| W-AO-02 | Hide sensitive/private data when inactive | MEDIUM |
| W-AO-03 | Limit updates to once per minute in Always On | MEDIUM |
| W-AO-04 | Use system dimming behaviors (no custom dimming) | MEDIUM |
| W-AO-05 | Seamless transition between active and dimmed (no layout shift) | MEDIUM |

**Rationale**: Always On extends the watch face into apps. Poor Always On implementation drains battery and may expose private information.

---

## Section 6: Workouts & Health [MEDIUM]

| ID | Rule | Priority |
|----|------|----------|
| W-WK-01 | Large, high-contrast live metrics during workouts | MEDIUM |
| W-WK-02 | Haptic feedback for milestones and zone changes | MEDIUM |
| W-WK-03 | Auto-pause for running/walking workouts | MEDIUM |
| W-WK-04 | WaterLock during swimming workouts | MEDIUM |
| W-WK-05 | Clear summary screen; save/discard in one action | MEDIUM |

**Rationale**: Workout apps run during physical exertion. The user cannot stop to carefully read or perform complex interactions. Design for motion and sweat.

---

## Section 7: Notifications [MEDIUM]

| ID | Rule | Priority |
|----|------|----------|
| W-NT-01 | Short Look: title + app icon only | MEDIUM |
| W-NT-02 | Long Look: full content + up to 4 action buttons | MEDIUM |
| W-NT-03 | Match haptic type to notification urgency | MEDIUM |
| W-NT-04 | Do not over-notify; batch non-urgent updates | MEDIUM |

**Rationale**: Every Watch notification buzzes the user's wrist. Excessive or poorly designed notifications train users to ignore or disable them entirely.

---

## Section 8: Accessibility [CRITICAL]

| ID | Rule | Priority |
|----|------|----------|
| W-AC-01 | Accessibility label on every interactive element | CRITICAL |
| W-AC-02 | VoiceOver can navigate all app content | CRITICAL |
| W-AC-03 | Custom controls have accessibilityValue and accessibilityHint | HIGH |
| W-AC-04 | Respect Reduce Motion; disable decorative animations | HIGH |
| W-AC-05 | Respond to Bold Text; adapt custom text via `@Environment(\.legibilityWeight)` | HIGH |
| W-AC-06 | Respond to Increase Contrast; provide higher-contrast variants via colorSchemeContrast | HIGH |

**Rationale**: VoiceOver is used on Apple Watch. Complications and health data must be accessible to all users.

---

## Cross-Reference: Rule Count Summary

| Section | Count | Priority |
|---------|-------|----------|
| Glanceable Design | 6 | CRITICAL |
| Digital Crown | 5 | HIGH |
| Navigation | 5 | HIGH |
| Complications | 5 | HIGH |
| Always On Display | 5 | MEDIUM |
| Workouts & Health | 5 | MEDIUM |
| Notifications | 4 | MEDIUM |
| Accessibility | 6 | CRITICAL |
| **Total** | **41** | |
```

## File: `skills/web/AGENTS.md`
```markdown
# Web Platform Design Skills

## Purpose

Framework-agnostic web design and accessibility guidelines based on WCAG 2.2, MDN Web Docs, and modern web platform standards.

## File Structure

```
web/
  metadata.json        # Version, references, abstract
  SKILL.md             # Full guidelines (load this)
  AGENTS.md            # This file
  rules/
    _sections.md       # Sectioned rules for selective loading
```

## Usage

- Load `SKILL.md` for complete guidelines when building or reviewing web UI.
- Load `rules/_sections.md` for individual category rules when working on a specific concern (e.g., only accessibility, only forms).

## When to Apply

- Building HTML/CSS/JS interfaces
- Auditing accessibility or WCAG compliance
- Implementing responsive layouts
- Reviewing web UI pull requests
- Optimizing web performance
- Adding dark mode or theming
- Internationalizing web content

## Priority Levels

| Level | Categories |
|-------|-----------|
| CRITICAL | Accessibility/WCAG, Responsive Design |
| HIGH | Forms, Typography, Performance |
| MEDIUM | Animation, Dark Mode, Navigation, Touch, i18n, Progressive Web Apps |

## Conventions

- Rules use imperative voice ("Use semantic HTML", not "You should use").
- Code examples are vanilla HTML/CSS/JS unless noted.
- WCAG success criteria referenced as (SC x.x.x).
- Priority in brackets: [CRITICAL], [HIGH], [MEDIUM].

## Never Do

- Never use `<div onclick>` when `<button>` exists — use semantic HTML
- Never set `maximum-scale=1` or `user-scalable=no` in the viewport meta tag
- Never rely on color alone to convey information — pair with text or icons
- Never use placeholder text as the only label for a form input
- Never build interactive elements that are only keyboard-accessible via `tabindex > 0`
- Never omit `alt` attributes on images — use `alt=""` for decorative images
- Never animate content that flashes more than 3 times per second (seizure risk)
- Never trap keyboard focus inside a component without providing a documented escape
- Never use `<table>` for layout — tables are for tabular data only
- Never set `font-size` in `px` on body text — use `rem` so user preferences apply
```

## File: `skills/web/SKILL.md`
```markdown
---
name: web-design-guidelines
description: Web platform design and accessibility guidelines. Use when building web interfaces, auditing accessibility, implementing responsive layouts, or reviewing web UI code. Triggers on tasks involving HTML, CSS, web components, WCAG compliance, responsive design, or web performance.
license: MIT
metadata:
  author: platform-design-skills
  version: "1.0.0"
---

# Web Platform Design Guidelines

Framework-agnostic rules for accessible, performant, responsive web interfaces. Based on WCAG 2.2, MDN Web Docs, and modern web platform APIs.

---

## 1. Accessibility / WCAG [CRITICAL]

Accessibility is not optional. Most rules in this section map to WCAG 2.2 success criteria at Level A or AA. A small number of best-practice rules (noted inline) target Level AAA or go beyond WCAG.

### 1.1 Use Semantic HTML Elements

Use elements for their intended purpose. Semantic structure provides free accessibility, SEO, and reader-mode support.

| Element | Purpose |
|---------|---------|
| `<main>` | Primary page content (one per page) |
| `<nav>` | Navigation blocks |
| `<header>` | Introductory content or navigational aids |
| `<footer>` | Footer for nearest sectioning content |
| `<article>` | Self-contained, independently distributable content |
| `<section>` | Thematic grouping with a heading |
| `<aside>` | Tangentially related content (sidebars, callouts) |
| `<figure>` / `<figcaption>` | Illustrations, diagrams, code listings |
| `<details>` / `<summary>` | Expandable/collapsible disclosure widget |
| `<dialog>` | Modal or non-modal dialog boxes |
| `<time>` | Machine-readable dates/times |
| `<mark>` | Highlighted/referenced text |
| `<address>` | Contact information for nearest article/body |

```html
<!-- Good -->
<main>
  <article>
    <h1>Article Title</h1>
    <p>Content...</p>
  </article>
  <aside>Related links</aside>
</main>

<!-- Bad: div soup -->
<div class="main">
  <div class="article">
    <div class="title">Article Title</div>
    <div class="content">Content...</div>
  </div>
</div>
```

**Anti-pattern**: Using `<div>` or `<span>` for interactive elements. Never write `<div onclick>` when `<button>` exists.

### 1.2 ARIA Labels on Interactive Elements

Every interactive element must have an accessible name. Prefer visible text; use `aria-label` or `aria-labelledby` only when visible text is insufficient (SC 4.1.2).

```html
<!-- Icon-only button: needs aria-label -->
<button aria-label="Close dialog">
  <svg aria-hidden="true">...</svg>
</button>

<!-- Linked by labelledby -->
<h2 id="section-title">Notifications</h2>
<ul aria-labelledby="section-title">...</ul>

<!-- Redundant: visible text is enough -->
<button>Save Changes</button> <!-- No aria-label needed -->
```

### 1.3 Keyboard Navigation

All interactive elements must be reachable and operable via keyboard (SC 2.1.1).

- Use native interactive elements (`<button>`, `<a href>`, `<input>`, `<select>`) which are keyboard-accessible by default.
- Custom widgets need `tabindex="0"` to enter tab order and keydown handlers for activation.
- Never use `tabindex` values greater than 0.
- Trap focus inside modals; return focus on close.

```js
// Focus trap for modal
dialog.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    const focusable = dialog.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }
});
```

### 1.4 Visible Focus Indicators

Never remove focus outlines without providing a visible replacement (SC 2.4.7, enhanced SC 2.4.11 (AA) and SC 2.4.12 (AAA) in WCAG 2.2).

```css
/* Good: custom focus indicator */
:focus-visible {
  outline: 3px solid var(--focus-color, #4A90D9);
  outline-offset: 2px;
}

/* Remove default only when :focus-visible is supported */
:focus:not(:focus-visible) {
  outline: none;
}

/* Bad: removing all focus styles */
/* *:focus { outline: none; } */
```

WCAG 2.2 requires focus indicators to have a minimum area of the perimeter of the component times 2px, with 3:1 contrast against adjacent colors.

### 1.5 Skip Navigation Links

Provide a mechanism to skip repeated blocks of content (SC 2.4.1).

```html
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>
  <nav>...</nav>
  <main id="main-content">...</main>
</body>
```

```css
.skip-link {
  position: absolute;
  top: -100%;
  left: 0;
  z-index: 1000;
  padding: 0.75rem 1.5rem;
  background: var(--color-primary);
  color: var(--color-on-primary);
}
.skip-link:focus {
  top: 0;
}
```

### 1.6 Alt Text for Images

Every `<img>` must have an `alt` attribute (SC 1.1.1).

- **Informative images**: describe the content and function. `alt="Bar chart showing sales doubled in Q4"`.
- **Decorative images**: use `alt=""` (empty string) so screen readers skip them.
- **Functional images** (inside links/buttons): describe the action. `alt="Search"`.
- **Complex images**: use `alt` for short description, link to long description or use `<figcaption>`.

```html
<img src="chart.png" alt="Revenue chart: Q1 $2M, Q2 $2.4M, Q3 $3.1M, Q4 $4.5M">
<img src="decorative-wave.svg" alt="">
```

### 1.7 Color Contrast

Maintain minimum contrast ratios (SC 1.4.3, 1.4.6, 1.4.11).

| Content | Minimum Ratio |
|---------|--------------|
| Normal text (<24px / <18.66px bold) | 4.5:1 |
| Large text (>=24px / >=18.66px bold) | 3:1 |
| UI components and graphical objects | 3:1 |

Do not rely on color alone to convey information (SC 1.4.1). Pair color with icons, text, or patterns.

```css
/* Check contrast of these tokens */
:root {
  --text-primary: #1a1a2e;    /* on white: ~16:1 */
  --text-secondary: #555770;  /* on white: ~6.5:1 */
  --text-disabled: #767693;   /* on white: ~4.5:1, borderline */
}
```

### 1.8 Form Labels

Every form input must have a programmatically associated label (SC 1.3.1, 3.3.2).

```html
<!-- Explicit label (preferred) -->
<label for="email">Email address</label>
<input id="email" type="email" autocomplete="email">

<!-- Implicit label (acceptable) -->
<label>
  Email address
  <input type="email" autocomplete="email">
</label>

<!-- Never: placeholder as sole label -->
<!-- <input placeholder="Email"> -->
```

### 1.9 Error Identification

Identify and describe errors in text (SC 3.3.1). Link error messages to inputs with `aria-describedby` or `aria-errormessage`.

```html
<label for="email">Email</label>
<input id="email" type="email" aria-describedby="email-error" aria-invalid="true">
<p id="email-error" role="alert">Enter a valid email address, e.g. name@example.com</p>
```

### 1.10 ARIA Live Regions

Announce dynamic content changes to screen readers (SC 4.1.3).

```html
<!-- Polite: announced when user is idle -->
<div aria-live="polite" aria-atomic="true">
  3 results found
</div>

<!-- Assertive: interrupts current speech -->
<div role="alert">
  Your session will expire in 2 minutes.
</div>

<!-- Status messages -->
<div role="status">
  File uploaded successfully.
</div>
```

Use `aria-live="polite"` by default. Reserve `role="alert"` / `aria-live="assertive"` for time-sensitive warnings.

### 1.11 ARIA Role Quick Reference

| Role | Purpose | Native Equivalent |
|------|---------|-------------------|
| `button` | Clickable action | `<button>` |
| `link` | Navigation | `<a href>` |
| `tab` / `tablist` / `tabpanel` | Tab interface | None |
| `dialog` | Modal | `<dialog>` |
| `alert` | Assertive live region | None |
| `status` | Polite live region | `<output>` |
| `navigation` | Nav landmark | `<nav>` |
| `main` | Main landmark | `<main>` |
| `complementary` | Aside landmark | `<aside>` |
| `search` | Search landmark | `<search>` (HTML5) |
| `img` | Image | `<img>` |
| `list` / `listitem` | List | `<ul>/<li>` |
| `heading` | Heading (with `aria-level`) | `<h1>`-`<h6>` |
| `menu` / `menuitem` | Menu widget | None |
| `tree` / `treeitem` | Tree view | None |
| `grid` / `row` / `gridcell` | Data grid | `<table>` |
| `progressbar` | Progress | `<progress>` |
| `slider` | Range input | `<input type="range">` |
| `switch` | Toggle | `<input type="checkbox">` |

**Rule**: Prefer native HTML over ARIA. Use ARIA only when no native element exists for the pattern.

### 1.12 Label in Name (WCAG 2.5.3 Level A)

When an interactive element has visible text, its accessible name must contain that visible text as a substring (SC 2.5.3). Voice control users (Dragon NaturallySpeaking, macOS Voice Control) speak the visible label to activate controls. If `aria-label` replaces or contradicts the visible text, voice commands fail.

```html
<!-- Correct: aria-label contains visible text as substring -->
<button aria-label="Delete item from cart">Delete</button>

<!-- Correct: no aria-label needed — visible text is the accessible name -->
<button>Save Changes</button>

<!-- Correct: icon button — no visible text, aria-label is fine -->
<button aria-label="Close dialog">
  <svg aria-hidden="true">...</svg>
</button>
```

```html
<!-- Incorrect: aria-label overrides visible text with different text -->
<button aria-label="Remove">Delete</button>

<!-- Incorrect: aria-label does not contain visible "Submit" -->
<button aria-label="Proceed to next step">Submit</button>
```

**Rule**: When visible text is present, `aria-label` must include that visible text (verbatim, case-insensitively). Prefer no `aria-label` at all when visible text is sufficient.

---

## 2. Responsive Design [CRITICAL]

### 2.1 Mobile-First Approach

Write base styles for the smallest viewport. Layer complexity with `min-width` media queries.

```css
/* Base: mobile */
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

/* Tablet */
@media (min-width: 48rem) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop */
@media (min-width: 64rem) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

### 2.2 Fluid Layouts with Modern CSS Functions

Use `clamp()`, `min()`, and `max()` for fluid sizing without breakpoints.

```css
/* Fluid typography */
h1 {
  font-size: clamp(1.75rem, 1.2rem + 2vw, 3rem);
}

/* Fluid spacing */
.section {
  padding: clamp(1.5rem, 4vw, 4rem);
}

/* Fluid container */
.container {
  width: min(90%, 72rem);
  margin-inline: auto;
}
```

### 2.3 Container Queries

Size components based on their container, not the viewport.

```css
.card-container {
  container-type: inline-size;
  container-name: card;
}

@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}

@container card (min-width: 700px) {
  .card {
    grid-template-columns: 300px 1fr;
    gap: 2rem;
  }
}
```

### 2.4 Content-Based Breakpoints

Set breakpoints where your content breaks, not at device widths. Common starting points:

```css
/* Content-based, not "iPhone" or "iPad" */
@media (min-width: 30rem)  { /* ~480px: single column gets cramped */ }
@media (min-width: 48rem)  { /* ~768px: room for 2 columns */ }
@media (min-width: 64rem)  { /* ~1024px: room for sidebar + content */ }
@media (min-width: 80rem)  { /* ~1280px: wide multi-column */ }
```

### 2.5 Touch Targets

Minimum 44x44 CSS pixels for touch targets (WCAG SC 2.5.5 AAA; SC 2.5.8 requires only 24x24px at AA). Provide at least 24px spacing between adjacent targets.

```css
button, a, input, select, textarea {
  min-height: 44px;
  min-width: 44px;
}

/* Enlarge tap area without changing visual size */
.icon-button {
  position: relative;
  width: 24px;
  height: 24px;
}
.icon-button::after {
  content: "";
  position: absolute;
  inset: -10px; /* expands clickable area */
}
```

### 2.6 Viewport Meta Tag

Always include in the document `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Never use `maximum-scale=1` or `user-scalable=no` -- these break pinch-to-zoom accessibility (SC 1.4.4).

### 2.7 No Horizontal Scrolling

Content must reflow at 320px width without horizontal scrolling (SC 1.4.10).

```css
/* Prevent overflow */
img, video, iframe, svg {
  max-width: 100%;
  height: auto;
}

/* Contain long words/URLs */
.prose {
  overflow-wrap: break-word;
}

/* Tables: scroll container, not page */
.table-wrapper {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
```

---

## 3. Forms [HIGH]

### 3.1 Label Every Input

Every input needs a visible, programmatically associated label. See section 1.8.

### 3.2 Autocomplete Attributes

Use `autocomplete` for common fields to enable browser autofill (SC 1.3.5).

```html
<input type="text" autocomplete="name" name="full-name">
<input type="email" autocomplete="email" name="email">
<input type="tel" autocomplete="tel" name="phone">
<input type="text" autocomplete="street-address" name="address">
<input type="text" autocomplete="postal-code" name="zip">
<input type="text" autocomplete="cc-name" name="card-name">
<input type="text" autocomplete="cc-number" name="card-number">
<input type="password" autocomplete="new-password" name="password">
<input type="password" autocomplete="current-password" name="current-pw">
```

### 3.3 Correct Input Types

Use the right `type` to trigger appropriate mobile keyboards and native validation.

| Type | Use For |
|------|---------|
| `email` | Email addresses |
| `tel` | Phone numbers |
| `url` | URLs |
| `number` | Numeric values with spinners (not for phone, zip, card numbers) |
| `search` | Search fields (shows clear button) |
| `date` / `time` / `datetime-local` | Temporal values |
| `password` | Passwords (triggers password manager) |
| `text` with `inputmode="numeric"` | Numeric data without spinners (PINs, zip codes) |

```html
<input type="tel" inputmode="numeric" pattern="[0-9]*" autocomplete="one-time-code">
```

### 3.4 Inline Validation

Validate on `blur` (not on every keystroke). Show success and error states.

```html
<div class="field" data-state="error">
  <label for="username">Username</label>
  <input id="username" type="text" aria-describedby="username-hint username-error" aria-invalid="true">
  <p id="username-hint" class="hint">3-20 characters, letters and numbers only</p>
  <p id="username-error" class="error" role="alert">Username must be at least 3 characters</p>
</div>
```

```css
.field[data-state="error"] input {
  border-color: var(--color-error);
  box-shadow: 0 0 0 1px var(--color-error);
}
.field[data-state="error"] .error { display: block; }
.field:not([data-state="error"]) .error { display: none; }
```

### 3.5 Fieldset and Legend for Groups

Group related inputs with `<fieldset>` and label the group with `<legend>`.

```html
<fieldset>
  <legend>Shipping Address</legend>
  <label for="street">Street</label>
  <input id="street" type="text" autocomplete="street-address">
  <!-- ... -->
</fieldset>

<fieldset>
  <legend>Preferred contact method</legend>
  <label><input type="radio" name="contact" value="email"> Email</label>
  <label><input type="radio" name="contact" value="phone"> Phone</label>
</fieldset>
```

### 3.6 Required Field Indication

Indicate required fields visually and programmatically. Use `required` attribute and visible markers.

```html
<label for="name">
  Full name <span aria-hidden="true">*</span>
  <span class="sr-only">(required)</span>
</label>
<input id="name" type="text" required autocomplete="name">
```

If most fields are required, indicate which are optional instead.

### 3.7 Submit Button State

Do not disable the submit button. Instead, validate on submit and show errors.

```html
<!-- Good: always enabled, validate on submit -->
<button type="submit">Create Account</button>

<!-- Bad: disabled button with no explanation -->
<!-- <button type="submit" disabled>Create Account</button> -->
```

Disabled buttons fail to communicate why the user cannot proceed. If you must disable, provide a visible explanation.

### 3.8 Keep Instructions Near the Field

Place format examples, constraints, and recovery text next to the relevant field via hint and error text. Never explain requirements only once in introductory copy and expect users to remember them later.

---

## 4. Typography [HIGH]

### 4.1 Font Stacks

Use system font stacks for performance, or web fonts with proper fallbacks.

```css
/* System font stack */
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

/* Monospace stack */
code, pre, kbd {
  font-family: ui-monospace, "Cascadia Code", "Source Code Pro", Menlo, Consolas, monospace;
}

/* Web font with fallbacks and size-adjust */
@font-face {
  font-family: "CustomFont";
  src: url("/fonts/custom.woff2") format("woff2");
  font-display: swap;
  font-weight: 100 900;
}
body {
  font-family: "CustomFont", system-ui, sans-serif;
}
```

### 4.2 Relative Units

Use `rem` for font sizes and spacing. Use `em` for component-relative sizing.

```css
html {
  font-size: 100%; /* = 16px default, respects user preference */
}

body {
  font-size: 1rem;       /* 16px */
}

h1 { font-size: 2.5rem; }  /* 40px */
h2 { font-size: 2rem; }    /* 32px */
h3 { font-size: 1.5rem; }  /* 24px */
small { font-size: 0.875rem; } /* 14px */

/* Never: font-size: 16px; (ignores user zoom settings) */
```

### 4.3 Line Height and Spacing

Body text line height of at least 1.5 (SC 1.4.12). Paragraph spacing at least 2x font size.

```css
body {
  line-height: 1.6;
}

h1, h2, h3 {
  line-height: 1.2;
}

p + p {
  margin-top: 1em;
}
```

### 4.4 Maximum Line Length

Limit line length to approximately 75 characters for readability.

```css
.prose {
  max-width: 75ch;
}

/* Or for a content column */
.content {
  max-width: 40rem; /* roughly 65-75ch depending on font */
  margin-inline: auto;
}
```

### 4.5 Typographic Details

Use real quotes, proper dashes, and tabular numbers for data.

```css
/* Smart quotes */
q { quotes: "\201C" "\201D" "\2018" "\2019"; } /* curly double then single */

/* Tabular numbers for aligned data */
.data-table td {
  font-variant-numeric: tabular-nums;
}

/* Oldstyle numbers for running prose (optional) */
.prose {
  font-variant-numeric: oldstyle-nums;
}

/* Proper list markers */
ul { list-style-type: disc; }
ol { list-style-type: decimal; }
```

### 4.6 Heading Hierarchy

Use `h1` through `h6` in order. Never skip levels. One `h1` per page.

```html
<!-- Good -->
<h1>Page Title</h1>
  <h2>Section</h2>
    <h3>Subsection</h3>
  <h2>Another Section</h2>

<!-- Bad: skipping h2 -->
<h1>Page Title</h1>
  <h3>Subsection</h3> <!-- Where is h2? -->
```

If you need visual styling that differs from the hierarchy, use CSS classes:

```html
<h2 class="text-lg">Visually smaller but semantically h2</h2>
```

---

## 5. Performance [HIGH]

### 5.1 Lazy Load Below-Fold Images

Use native lazy loading for images not visible on initial load.

```html
<!-- Above fold: load eagerly, add fetchpriority -->
<img src="hero.webp" alt="Hero image" fetchpriority="high" width="1200" height="600">

<!-- Below fold: lazy load -->
<img src="feature.webp" alt="Feature image" loading="lazy" width="600" height="400">
```

### 5.2 Explicit Image Dimensions

Always specify `width` and `height` to prevent layout shift (CLS).

```html
<img src="photo.webp" alt="Description" width="800" height="600">
```

```css
/* Responsive images with aspect ratio preservation */
img {
  max-width: 100%;
  height: auto;
}
```

### 5.3 Resource Hints

Use `preconnect` for third-party origins and `preload` for critical resources.

```html
<head>
  <!-- Preconnect to critical third-party origins -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://cdn.example.com" crossorigin>

  <!-- Preload critical resources -->
  <link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/css/critical.css" as="style">

  <!-- DNS prefetch for non-critical origins -->
  <link rel="dns-prefetch" href="https://analytics.example.com">
</head>
```

### 5.4 Code Splitting

Load JavaScript only when needed. Use dynamic `import()` for route-based and component-based splitting.

```js
// Route-based splitting
const routes = {
  '/dashboard': () => import('./pages/dashboard.js'),
  '/settings':  () => import('./pages/settings.js'),
};

// Interaction-based splitting
button.addEventListener('click', async () => {
  const { openEditor } = await import('./editor.js');
  openEditor();
});
```

### 5.5 Virtualize Long Lists

For lists exceeding a few hundred items, render only visible rows.

```js
// Concept: virtual scrolling
// Render only items in viewport + buffer
const visibleStart = Math.floor(scrollTop / itemHeight);
const visibleEnd = visibleStart + Math.ceil(containerHeight / itemHeight);
const buffer = 5;
const renderStart = Math.max(0, visibleStart - buffer);
const renderEnd = Math.min(totalItems, visibleEnd + buffer);
```

### 5.6 Avoid Layout Thrashing

Batch DOM reads and writes. Never interleave them.

```js
// Bad: read-write-read-write (forces synchronous layout)
elements.forEach(el => {
  const height = el.offsetHeight;     // read
  el.style.height = height + 10 + 'px'; // write
});

// Good: batch reads, then batch writes
const heights = elements.map(el => el.offsetHeight); // all reads
elements.forEach((el, i) => {
  el.style.height = heights[i] + 10 + 'px'; // all writes
});
```

### 5.7 Use `will-change` Sparingly

Only apply `will-change` to elements that will animate, and remove it after animation completes.

```css
/* Good: scoped and temporary */
.card:hover {
  will-change: transform;
}
.card.animating {
  will-change: transform, opacity;
}

/* Bad: blanket will-change */
/* * { will-change: transform; } */
```

### 5.8 Expose Waiting States Promptly

After a user action, acknowledge the new state immediately. If work cannot finish within a brief moment, show progress, skeletons, optimistic UI, or `aria-busy` feedback instead of leaving the interface unchanged.

---

## 6. Animation and Motion [MEDIUM]

### 6.1 Respect prefers-reduced-motion

Always provide a reduced-motion alternative (SC 2.3.3, Level AAA).

```css
/* Define animations normally */
.fade-in {
  animation: fadeIn 300ms ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Remove or reduce for users who prefer it */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

```js
// Check in JavaScript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
```

### 6.2 Compositor-Friendly Animations

Animate only `transform` and `opacity` for smooth 60fps animation. These run on the GPU compositor thread.

```css
/* Good: compositor-only properties */
.slide-in {
  transition: transform 200ms ease-out, opacity 200ms ease-out;
}

/* Bad: triggers layout/paint */
.slide-in-bad {
  transition: left 200ms, width 200ms, height 200ms;
}
```

### 6.3 No Flashing Content

Never flash content more than 3 times per second (SC 2.3.1). This can trigger seizures.

### 6.4 Transitions for State Changes

Use transitions for hover, focus, open/close, and other state changes to provide continuity.

```css
.dropdown {
  opacity: 0;
  transform: translateY(-4px);
  transition: opacity 150ms ease-out, transform 150ms ease-out;
  pointer-events: none;
}
.dropdown.open {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}
```

### 6.5 Meaningful Motion Only

Animation should communicate state, guide attention, or show spatial relationships. Never animate for decoration alone.

---

## 7. Dark Mode and Theming [MEDIUM]

### 7.1 System Preference Detection

```css
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f0f17;
    --text: #e4e4ef;
    --surface: #1c1c2e;
    --border: #2e2e44;
  }
}
```

### 7.2 CSS Custom Properties for Theming

Define all theme values as custom properties. Toggle themes by changing property values.

```css
:root {
  color-scheme: light dark;

  /* Light theme (default) */
  --color-bg: #ffffff;
  --color-surface: #f5f5f7;
  --color-text-primary: #1a1a2e;
  --color-text-secondary: #555770;
  --color-border: #d1d1e0;
  --color-primary: #2563eb;
  --color-primary-text: #ffffff;
  --color-error: #dc2626;
  --color-success: #16a34a;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #0f0f17;
    --color-surface: #1c1c2e;
    --color-text-primary: #e4e4ef;
    --color-text-secondary: #a0a0b8;
    --color-border: #2e2e44;
    --color-primary: #60a5fa;
    --color-primary-text: #0f0f17;
    --color-error: #f87171;
    --color-success: #4ade80;
  }
}
```

### 7.3 Color-Scheme Meta Tag

Tell the browser about supported color schemes for native UI elements (scrollbars, form controls).

```html
<meta name="color-scheme" content="light dark">
```

### 7.4 Maintain Contrast in Both Modes

Verify contrast ratios in both light and dark modes. Dark mode often suffers from low-contrast text on dark surfaces.

### 7.5 Adaptive Images

Provide appropriate images for light and dark contexts.

```html
<picture>
  <source srcset="logo-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="logo-light.svg" alt="Company logo">
</picture>
```

```css
/* Or use CSS filter for simple cases */
@media (prefers-color-scheme: dark) {
  .decorative-img {
    filter: brightness(0.9) contrast(1.1);
  }
}
```

### 7.6 Respect prefers-contrast

Honor the user's contrast preference using `@media (prefers-contrast: more)` and `@media (prefers-contrast: forced)`. `prefers-contrast: more` responds to macOS/iOS "Increase Contrast" in System Settings; `prefers-contrast: forced` responds to Windows High Contrast Mode — a distinct OS feature that overrides colors entirely.

```css
/* Default theme */
:root {
  --color-text: #555770;
  --color-border: #d1d1e0;
  --color-bg: #ffffff;
}

/* High contrast mode: stronger text and border colors */
@media (prefers-contrast: more) {
  :root {
    --color-text: #1a1a2e;       /* Darker text for higher ratio */
    --color-border: #1a1a2e;     /* Stronger borders */
    --color-bg: #ffffff;
  }

  /* Ensure interactive elements are clearly delineated */
  button, input, select, textarea {
    border: 2px solid currentColor;
  }
}

/* Forced colors (Windows High Contrast mode) */
@media (prefers-contrast: forced) {
  /* Use system color keywords to respect OS color palette */
  :root {
    --color-text: ButtonText;
    --color-bg: ButtonFace;
    --color-border: ButtonBorder;
  }
}
```

---

## 8. Navigation and State [MEDIUM]

### 8.1 URL Reflects State

Every meaningful view should have a unique URL. Users should be able to bookmark, share, and reload any state.

```js
// Update URL without full page reload
function updateFilters(filters) {
  const params = new URLSearchParams(filters);
  history.pushState(null, '', `?${params}`);
  renderResults(filters);
}

// Restore state from URL on load
const params = new URLSearchParams(location.search);
const initialFilters = Object.fromEntries(params);
```

### 8.2 Browser Back/Forward

Handle `popstate` to support browser navigation.

```js
window.addEventListener('popstate', () => {
  const params = new URLSearchParams(location.search);
  renderResults(Object.fromEntries(params));
});
```

### 8.3 Active Navigation States

Indicate the current page or section in navigation. Use `aria-current="page"` for the active link.

```html
<nav aria-label="Main">
  <a href="/" aria-current="page">Home</a>
  <a href="/products">Products</a>
  <a href="/about">About</a>
</nav>
```

```css
[aria-current="page"] {
  font-weight: 700;
  border-bottom: 2px solid var(--color-primary);
}
```

### 8.4 Breadcrumbs

Provide breadcrumbs for sites with deep hierarchies.

```html
<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/products">Products</a></li>
    <li><a href="/products/widgets" aria-current="page">Widgets</a></li>
  </ol>
</nav>
```

### 8.5 Scroll Restoration

Manage scroll position for SPA navigation.

```js
// Disable browser auto-restoration for manual control
if ('scrollRestoration' in history) {
  history.scrollRestoration = 'manual';
}

// Save scroll position before navigation
function saveScrollPosition() {
  sessionStorage.setItem(`scroll-${location.pathname}`, window.scrollY);
}

// Restore on back/forward
window.addEventListener('popstate', () => {
  const saved = sessionStorage.getItem(`scroll-${location.pathname}`);
  if (saved) {
    requestAnimationFrame(() => window.scrollTo(0, parseInt(saved)));
  }
});
```

---

## 9. Touch and Interaction [MEDIUM]

### 9.1 Touch-Action for Scroll Control

Use `touch-action` to control gesture behavior on interactive elements.

```css
/* Allow only vertical scrolling (disable horizontal pan and pinch-zoom) */
.vertical-scroll {
  touch-action: pan-y;
}

/* Carousel: horizontal scroll only */
.carousel {
  touch-action: pan-x;
}

/* Canvas/map: disable all browser gestures */
.canvas {
  touch-action: none;
}
```

### 9.2 Tap Highlight

Control the tap highlight on mobile WebKit browsers.

```css
button, a {
  -webkit-tap-highlight-color: transparent;
}
```

### 9.3 Hover and Focus Parity

Every hover interaction must also work with keyboard focus.

```css
/* Always pair :hover with :focus-visible */
.card:hover,
.card:focus-visible {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
}
```

### 9.4 No Hover-Only Interactions

Never hide essential functionality behind hover. Touch devices have no hover state.

```css
/* Bad: content only accessible on hover */
/* .tooltip { display: none; }
   .trigger:hover .tooltip { display: block; } */

/* Good: works with focus and click too */
.trigger:hover .tooltip,
.trigger:focus-within .tooltip,
.tooltip:focus-within {
  display: block;
}
```

### 9.5 Scroll Snap for Carousels

Use CSS scroll snap for card carousels and horizontal lists.

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  gap: 1rem;
  scroll-padding: 1rem;
}

.carousel > .slide {
  scroll-snap-align: start;
  flex: 0 0 min(85%, 400px);
}
```

---

## 10. Internationalization [MEDIUM]

### 10.1 dir and lang Attributes

Set `lang` on the `<html>` element. Use `dir="auto"` for user-generated content.

```html
<html lang="en" dir="ltr">

<!-- User-generated content: let browser detect direction -->
<p dir="auto">User-submitted text here</p>

<!-- Explicit override for known RTL content -->
<blockquote lang="ar" dir="rtl">...</blockquote>
```

### 10.2 Intl APIs for Formatting

Use the `Intl` API for locale-aware formatting. Never hard-code date or number formats.

```js
// Dates
new Intl.DateTimeFormat('en-US', { dateStyle: 'long' }).format(date);
// "January 15, 2026"

// Numbers
new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(1234.56);
// "1.234,56 EUR"

// Relative time
new Intl.RelativeTimeFormat('en', { numeric: 'auto' }).format(-1, 'day');
// "yesterday"

// Lists
new Intl.ListFormat('en', { style: 'long', type: 'conjunction' }).format(['a', 'b', 'c']);
// "a, b, and c"

// Plurals
const pr = new Intl.PluralRules('en');
const suffixes = { one: 'st', two: 'nd', few: 'rd', other: 'th' };
function ordinal(n) { return `${n}${suffixes[pr.select(n)]}`; }
```

### 10.3 Avoid Text in Images

Text in images cannot be translated, resized, or read by screen readers. Use HTML/CSS text with background images when a styled text overlay is needed.

### 10.4 CSS Logical Properties

Use logical properties instead of physical ones to support both LTR and RTL layouts.

```css
/* Physical (breaks in RTL) */
/* margin-left: 1rem; padding-right: 2rem; border-left: 1px solid; */

/* Logical (works in LTR and RTL) */
.sidebar {
  margin-inline-start: 1rem;
  padding-inline-end: 2rem;
  border-inline-start: 1px solid var(--color-border);
}

.stack > * + * {
  margin-block-start: 1rem;
}

/* Logical shorthands */
.box {
  margin-inline: auto;     /* left + right */
  padding-block: 2rem;     /* top + bottom */
  inset-inline-start: 0;   /* left in LTR, right in RTL */
  border-start-start-radius: 8px; /* top-left in LTR, top-right in RTL */
}
```

| Physical | Logical |
|----------|---------|
| `left` / `right` | `inline-start` / `inline-end` |
| `top` / `bottom` | `block-start` / `block-end` |
| `margin-left` | `margin-inline-start` |
| `padding-right` | `padding-inline-end` |
| `border-top-left-radius` | `border-start-start-radius` |
| `width` | `inline-size` |
| `height` | `block-size` |
| `text-align: left` | `text-align: start` |

### 10.5 RTL Layout Support

Test layouts in RTL mode. Flexbox and Grid handle RTL automatically with logical properties.

```css
/* This layout works in both LTR and RTL without changes */
.layout {
  display: flex;
  gap: 1rem;
}

/* Icons that indicate direction need flipping */
[dir="rtl"] .arrow-icon {
  transform: scaleX(-1);
}
```

---

## 11. Progressive Web Apps [MEDIUM]

PWAs allow web apps to be installed and run offline. When building an installable web app, the following rules ensure the experience is consistent and reliable.

### 11.1 Provide a Complete Web App Manifest

Include a `manifest.json` linked from `<head>` with all required fields for installability. Missing fields silently prevent install prompts.

```html
<link rel="manifest" href="/manifest.json">
```

```json
{
  "name": "My App",
  "short_name": "App",
  "start_url": "/",
  "display": "standalone",
  "icons": [
    { "src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

**Incorrect:**
```json
{
  "name": "My App"
  // Missing start_url, display, and icons — app is not installable
}
```

### 11.2 Set theme_color and background_color

`theme_color` tints the browser chrome and the OS task switcher. `background_color` fills the splash screen before the app loads. Both must match your brand colors.

```json
{
  "theme_color": "#1a73e8",
  "background_color": "#ffffff"
}
```

### 11.3 Register a Service Worker for Offline Support

A service worker is required for installability and offline capability. Cache critical assets on install; respond from cache when offline.

```js
// In your main entry point
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}
```

```js
// sw.js — cache on install, serve from cache when offline
const CACHE = 'v1';
const PRECACHE = ['/', '/index.html', '/app.js', '/app.css'];

self.addEventListener('install', e =>
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRECACHE)))
);

self.addEventListener('fetch', e =>
  e.respondWith(
    caches.match(e.request).then(hit => hit ?? fetch(e.request))
  )
);
```

### 11.4 Meet Installability Criteria

For the browser install prompt to appear: the app must be served over HTTPS, have a registered service worker with a `fetch` handler, and include a manifest with `name`, `icons`, `start_url`, and `display: standalone` (or `fullscreen`/`minimal-ui`).

### 11.5 Use display Mode Appropriately

| Value | Use When |
|-------|----------|
| `standalone` | App replaces browser UI; most common choice |
| `fullscreen` | Games or media apps needing the entire screen |
| `minimal-ui` | Retain minimal browser controls (back, reload) |
| `browser` | No installation behavior; opens in browser tab |

---

## Evaluation Checklist

Use this checklist when building or reviewing web interfaces.

### Accessibility
- [ ] All images have appropriate `alt` text
- [ ] Color contrast meets 4.5:1 (text) and 3:1 (UI components)
- [ ] All interactive elements are keyboard accessible
- [ ] Focus indicators are visible (3:1 contrast, 2px minimum perimeter)
- [ ] Skip navigation link is present
- [ ] Form inputs have associated labels
- [ ] Error messages are linked to their inputs
- [ ] Dynamic content updates use ARIA live regions
- [ ] No content flashes more than 3 times per second
- [ ] Page has proper heading hierarchy (h1-h6, no skips)
- [ ] Landmarks are used correctly (main, nav, header, footer)

### Responsive
- [ ] No horizontal scrolling at 320px width
- [ ] Touch targets are at least 44x44px
- [ ] Viewport meta tag is present (no user-scalable=no)
- [ ] Layout works on mobile, tablet, and desktop
- [ ] Text is readable without zooming on mobile

### Forms
- [ ] All inputs have visible labels
- [ ] Autocomplete attributes are set for common fields
- [ ] Correct input types trigger correct mobile keyboards
- [ ] Error messages are clear and specific
- [ ] Required fields are indicated
- [ ] Submit button is not disabled

### Performance
- [ ] Below-fold images use `loading="lazy"`
- [ ] Images have explicit `width` and `height`
- [ ] Critical fonts are preloaded
- [ ] Third-party origins use `preconnect`
- [ ] Large JS bundles are code-split

### Motion and Theming
- [ ] `prefers-reduced-motion` is respected
- [ ] Animations use only `transform` and `opacity`
- [ ] Dark mode maintains contrast ratios
- [ ] `color-scheme` meta tag is present
- [ ] Theme uses CSS custom properties
- [ ] `prefers-contrast: more` increases text and border contrast
- [ ] `prefers-contrast: forced` uses system color keywords

### Internationalization
- [ ] `lang` attribute on `<html>`
- [ ] CSS logical properties used (not physical)
- [ ] Dates/numbers formatted with Intl APIs
- [ ] No text embedded in images
- [ ] Layout tested in RTL mode

### Progressive Web App
- [ ] Web App Manifest linked from `<head>` with `name`, `icons`, `start_url`, and `display`
- [ ] `theme_color` and `background_color` match brand palette
- [ ] Service worker registered with a `fetch` handler for offline support
- [ ] App served over HTTPS

---

## Common Anti-Patterns

| Anti-Pattern | Fix |
|--------------|-----|
| `<div onclick="...">` | Use `<button>` |
| `outline: none` without replacement | Use `:focus-visible` with custom outline |
| `placeholder` as label | Add a `<label>` element |
| `tabindex="5"` | Use `tabindex="0"` or natural order |
| `user-scalable=no` | Remove it |
| `font-size: 12px` | Use `font-size: 0.75rem` |
| Animating `width`/`height`/`top`/`left` | Animate `transform` and `opacity` |
| Disabling submit button | Validate on submit, show errors |
| Color alone for status | Add icon, text, or pattern |
| `margin-left` / `padding-right` | Use `margin-inline-start` / `padding-inline-end` |
| `<img>` without dimensions | Add `width` and `height` attributes |
| Hover-only disclosure | Add `:focus-within` and click handler |
```

## File: `skills/web/metadata.json`
```json
{
  "version": "1.0.0",
  "organization": "Platform Design Skills",
  "date": "February 2026",
  "abstract": "Web platform design and accessibility guidelines. 70+ rules across 11 categories covering WCAG 2.2 accessibility, responsive design, semantic HTML, performance, forms, animations, typography, dark mode, internationalization, and Progressive Web Apps. Framework-agnostic with HTML/CSS/JS examples.",
  "references": [
    "https://www.w3.org/WAI/WCAG22/quickref/",
    "https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web",
    "https://web.dev",
    "https://www.a11yproject.com"
  ]
}
```

## File: `skills/web/rules/_sections.md`
```markdown
# Web Platform Design Rules (Sectioned)

Load individual sections as needed. Each section is self-contained.

---

<!-- SECTION: accessibility -->
## Accessibility / WCAG [CRITICAL]

### Rules

1. **Use semantic HTML elements.** Use `<main>`, `<nav>`, `<header>`, `<footer>`, `<article>`, `<section>`, `<aside>`, `<figure>`, `<dialog>`, `<details>` for their intended purpose. Never use `<div onclick>` when `<button>` exists.

2. **Add ARIA labels to interactive elements without visible text.** Icon buttons need `aria-label`. Groups need `aria-labelledby`. Do not add ARIA when visible text already provides the name.

3. **Ensure keyboard navigation.** All interactive elements reachable via Tab. Custom widgets need `tabindex="0"` and keydown handlers. Trap focus inside modals. Never use `tabindex` > 0.

4. **Provide visible focus indicators.** Use `:focus-visible` with 3px outline and 2px offset. WCAG 2.2 requires minimum 2px perimeter area with 3:1 contrast.

5. **Include skip navigation links.** Add `<a href="#main-content" class="skip-link">Skip to main content</a>` before the nav. Visually hidden until focused.

6. **Write appropriate alt text.** Informative images: describe content. Decorative images: `alt=""`. Functional images: describe the action. Complex images: short alt + linked long description.

7. **Meet color contrast ratios.** Normal text: 4.5:1. Large text (>=24px or >=18.66px bold): 3:1. UI components and graphics: 3:1. Never rely on color alone.

8. **Associate labels with form inputs.** Use `<label for="id">` or wrap input in `<label>`. Never use placeholder as the only label.

9. **Identify errors in text and link to inputs.** Use `aria-describedby` or `aria-errormessage` with `aria-invalid="true"`. Error text must describe how to fix the problem.

10. **Use ARIA live regions for dynamic updates.** `aria-live="polite"` for non-urgent updates. `role="alert"` for time-sensitive messages. `role="status"` for status messages.

11. **Prefer native HTML over ARIA roles.** Use `<button>` not `<div role="button">`. Use `<nav>` not `<div role="navigation">`. ARIA is a supplement, not a replacement.

12. **Accessible name must contain visible text (SC 2.5.3).** When an element has visible text, its accessible name must include that text as a substring. Do not use `aria-label` that replaces visible text with different text — voice control users speak the visible label to activate controls.

<!-- /SECTION: accessibility -->

---

<!-- SECTION: responsive -->
## Responsive Design [CRITICAL]

### Rules

1. **Build mobile-first.** Base styles for smallest viewport. Add complexity with `min-width` media queries.

2. **Use fluid sizing with `clamp()`, `min()`, `max()`.** Fluid typography: `font-size: clamp(1.75rem, 1.2rem + 2vw, 3rem)`. Fluid containers: `width: min(90%, 72rem)`.

3. **Use container queries for component-level responsiveness.** Set `container-type: inline-size` on wrappers. Use `@container` for layout changes based on available space.

4. **Set breakpoints at content, not device widths.** Break where your layout breaks. Common starting points: 30rem, 48rem, 64rem, 80rem.

5. **Ensure touch targets are 44x44px minimum.** Expand small icons with `::after` pseudo-element and negative `inset`. Maintain 24px spacing between adjacent targets.

6. **Include viewport meta tag.** `<meta name="viewport" content="width=device-width, initial-scale=1">`. Never use `maximum-scale=1` or `user-scalable=no`.

7. **Prevent horizontal scrolling.** Set `max-width: 100%; height: auto` on images/video/iframes. Use `overflow-wrap: break-word` for long text. Wrap tables in `overflow-x: auto` container.

<!-- /SECTION: responsive -->

---

<!-- SECTION: forms -->
## Forms [HIGH]

### Rules

1. **Label every input.** Use `<label for="id">` with matching `id` on the input. Every field needs a visible, programmatically associated label.

2. **Set autocomplete attributes.** Use `autocomplete="email"`, `autocomplete="tel"`, `autocomplete="name"`, `autocomplete="street-address"`, etc. Required by WCAG SC 1.3.5.

3. **Use correct input types.** `type="email"` for email, `type="tel"` for phone, `type="url"` for URLs, `inputmode="numeric"` for numeric data without spinners.

4. **Validate inline on blur.** Show errors after the user leaves a field, not on every keystroke. Use `aria-invalid` and `aria-describedby` to link errors.

5. **Group related fields with fieldset/legend.** Radio groups, checkbox groups, and address blocks belong in `<fieldset>` with a `<legend>`.

6. **Indicate required fields.** Use `required` attribute. Show a visible marker (asterisk or "(required)" text). If most fields are required, indicate optional fields instead.

7. **Keep submit buttons enabled.** Validate on submit and show errors. Disabled buttons fail to explain why the user cannot proceed.

8. **Keep instructions near the field.** Put examples, constraints, and recovery text next to the relevant input so users do not have to remember guidance from earlier copy.

<!-- /SECTION: forms -->

---

<!-- SECTION: typography -->
## Typography [HIGH]

### Rules

1. **Use system font stacks or web fonts with fallbacks.** System: `font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`. Web fonts: add `font-display: swap`.

2. **Use relative units.** `rem` for font sizes and spacing. `em` for component-relative sizing. Never set `font-size` in `px` on body text.

3. **Set body line height to at least 1.5.** Headings can use 1.2. Paragraph spacing at least 2x font size. Required by WCAG SC 1.4.12.

4. **Limit line length to ~75 characters.** Use `max-width: 75ch` or `max-width: 40rem` on prose containers.

5. **Use proper typographic details.** Curly quotes via CSS `quotes` property. Tabular numbers (`font-variant-numeric: tabular-nums`) for data columns.

6. **Maintain heading hierarchy.** `h1` through `h6` in order, no skipping. One `h1` per page. Style headings with classes if visual size differs from semantic level.

<!-- /SECTION: typography -->

---

<!-- SECTION: performance -->
## Performance [HIGH]

### Rules

1. **Lazy load below-fold images.** Use `loading="lazy"`. Above-fold hero images get `fetchpriority="high"`.

2. **Set explicit image dimensions.** Add `width` and `height` attributes to prevent Cumulative Layout Shift (CLS).

3. **Use resource hints.** `<link rel="preconnect">` for third-party origins. `<link rel="preload">` for critical fonts and CSS. `<link rel="dns-prefetch">` for non-critical origins.

4. **Code-split JavaScript.** Use dynamic `import()` for route-based and interaction-based splitting. Load heavy libraries only when needed.

5. **Virtualize long lists.** Render only visible rows plus a small buffer for lists exceeding a few hundred items.

6. **Avoid layout thrashing.** Batch all DOM reads, then batch all DOM writes. Never interleave reads and writes in a loop.

7. **Use `will-change` sparingly.** Apply only to elements that will animate. Remove after animation completes. Never apply globally.

8. **Expose waiting states promptly.** After user input, acknowledge the new state immediately. If work will take longer than a brief moment, show progress, skeletons, optimistic UI, or `aria-busy`.

<!-- /SECTION: performance -->

---

<!-- SECTION: animation -->
## Animation and Motion [MEDIUM]

### Rules

1. **Respect `prefers-reduced-motion`.** Wrap all animations in a media query check. Set `animation-duration: 0.01ms` and `transition-duration: 0.01ms` for reduced motion preference.

2. **Animate only compositor-friendly properties.** Use `transform` and `opacity`. Avoid animating `width`, `height`, `top`, `left`, `margin`, or `padding`.

3. **No flashing content above 3Hz.** Content that flashes more than 3 times per second can trigger seizures. WCAG SC 2.3.1.

4. **Use transitions for state changes.** Hover, focus, open/close, and visibility changes should transition smoothly (150-300ms).

5. **Motion must be meaningful.** Animate to communicate state, guide attention, or show spatial relationships. Never animate purely for decoration.

<!-- /SECTION: animation -->

---

<!-- SECTION: dark-mode -->
## Dark Mode and Theming [MEDIUM]

### Rules

1. **Detect system preference.** Use `@media (prefers-color-scheme: dark)` to switch theme tokens.

2. **Define themes with CSS custom properties.** All colors, shadows, and surfaces as `--custom-properties`. Toggle entire themes by redefining variables.

3. **Set the `color-scheme` meta tag.** `<meta name="color-scheme" content="light dark">`. Also set `color-scheme: light dark` in CSS for native form controls.

4. **Verify contrast in both modes.** Dark mode commonly fails contrast on secondary text and disabled states. Re-check all ratios.

5. **Adapt images to theme.** Use `<picture>` with `media="(prefers-color-scheme: dark)"` for alternate assets. Use `filter: brightness()` for simple adjustments.

6. **Respect `prefers-contrast`.** Use `@media (prefers-contrast: more)` to increase text and border contrast for users with OS-level "Increase Contrast" enabled. Use `@media (prefers-contrast: forced)` with system color keywords (`ButtonText`, `ButtonFace`, `ButtonBorder`) for Windows High Contrast mode.

<!-- /SECTION: dark-mode -->

---

<!-- SECTION: navigation -->
## Navigation and State [MEDIUM]

### Rules

1. **URL reflects state.** Every meaningful view has a unique URL. Use `URLSearchParams` and `history.pushState` for filters, tabs, and pagination.

2. **Support browser back/forward.** Handle `popstate` events to restore state from the URL.

3. **Mark active navigation items.** Use `aria-current="page"` on the active link. Style with `[aria-current="page"]` selector.

4. **Add breadcrumbs for deep hierarchies.** Use `<nav aria-label="Breadcrumb">` with an ordered list. Mark current page with `aria-current="page"`.

5. **Manage scroll restoration.** Set `history.scrollRestoration = 'manual'` in SPAs. Save and restore scroll position on navigation.

<!-- /SECTION: navigation -->

---

<!-- SECTION: touch -->
## Touch and Interaction [MEDIUM]

### Rules

1. **Use `touch-action` for scroll control.** `pan-y` for vertical-only scroll areas. `pan-x` for carousels. `none` for canvas/map elements.

2. **Disable tap highlight.** Set `-webkit-tap-highlight-color: transparent` on buttons and links; provide your own active state instead.

3. **Pair hover with focus-visible.** Every `:hover` style must have an equivalent `:focus-visible` style.

4. **No hover-only interactions.** Tooltips and dropdowns must work with `:focus-within` and click/tap. Touch devices have no hover state.

5. **Use CSS scroll snap for carousels.** `scroll-snap-type: x mandatory` on the container. `scroll-snap-align: start` on each item.

<!-- /SECTION: touch -->

---

<!-- SECTION: i18n -->
## Internationalization [MEDIUM]

### Rules

1. **Set `lang` and `dir` attributes.** Set `lang` on `<html>` using BCP 47 language tags (`en`, `fr`, `ar`, `zh-Hans`). Override with `lang` on elements containing different-language content. Use `dir="auto"` for user-generated content; use `dir="rtl"` or `dir="ltr"` when direction is known.

2. **Format with Intl APIs.** `Intl.DateTimeFormat` for dates. `Intl.NumberFormat` for numbers and currency. `Intl.RelativeTimeFormat` for relative time. `Intl.ListFormat` for lists.

3. **Avoid text in images.** Text in images cannot be translated, resized, or read by screen readers.

4. **Use CSS logical properties.** `margin-inline-start` not `margin-left`. `padding-block-end` not `padding-bottom`. `inset-inline-start` not `left`. `text-align: start` not `text-align: left`.

5. **Support RTL layouts.** Test in RTL mode. Flip directional icons with `transform: scaleX(-1)` in `[dir="rtl"]`. Flexbox and Grid handle flow reversal automatically with logical properties.

<!-- /SECTION: i18n -->

---

<!-- SECTION: pwa -->
## Progressive Web Apps [MEDIUM]

### Rules

1. **Provide a complete Web App Manifest.** Link `manifest.json` from `<head>`. Required fields: `name`, `short_name`, `start_url`, `display`, and `icons` (192px and 512px PNG). Missing fields prevent the install prompt.

2. **Set `theme_color` and `background_color`.** `theme_color` tints OS chrome and the task switcher. `background_color` fills the splash screen. Match both to your brand palette.

3. **Register a service worker with a fetch handler.** Required for installability. Cache critical assets on `install`; serve from cache when offline. Use a `fetch` event listener to intercept requests.

4. **Meet all installability criteria.** HTTPS is required. The service worker must have a `fetch` handler. The manifest must include `name`, `icons`, `start_url`, and `display: standalone` (or `fullscreen`/`minimal-ui`).

5. **Choose `display` mode intentionally.** Use `standalone` for most apps (replaces browser UI). Use `fullscreen` for games/media. Use `minimal-ui` to retain minimal browser controls. Avoid `browser` for installed app experiences.

<!-- /SECTION: pwa -->

---

## Quick Reference: Semantic HTML Elements

| Element | Use For | Replaces |
|---------|---------|----------|
| `<button>` | Actions, toggles | `<div onclick>`, `<a href="#">` |
| `<a href>` | Navigation to URLs | `<span onclick>` |
| `<nav>` | Navigation blocks | `<div class="nav">` |
| `<main>` | Primary content | `<div class="main">` |
| `<header>` | Page/section header | `<div class="header">` |
| `<footer>` | Page/section footer | `<div class="footer">` |
| `<article>` | Independent content | `<div class="article">` |
| `<section>` | Thematic group | `<div class="section">` |
| `<aside>` | Side content | `<div class="sidebar">` |
| `<dialog>` | Modal dialogs | `<div class="modal">` |
| `<details>/<summary>` | Disclosure | Custom accordion JS |
| `<fieldset>/<legend>` | Form groups | `<div class="group">` |
| `<figure>/<figcaption>` | Figures with captions | `<div class="image-wrap">` |
| `<time>` | Dates and times | `<span class="date">` |
| `<search>` | Search landmark | `<div role="search">` |
| `<output>` | Calculation result | `<span class="result">` |
| `<progress>` | Progress indicator | `<div class="progress">` |
| `<meter>` | Scalar measurement | `<div class="gauge">` |

## Quick Reference: Common ARIA Patterns

| Pattern | Key Attributes |
|---------|---------------|
| Tabs | `role="tablist"`, `role="tab"`, `role="tabpanel"`, `aria-selected`, `aria-controls` |
| Accordion | `<button aria-expanded>`, `aria-controls`, `<div role="region">` |
| Modal | `<dialog>` or `role="dialog"`, `aria-modal="true"`, `aria-labelledby` |
| Combobox | `role="combobox"`, `aria-expanded`, `aria-controls`, `aria-activedescendant` |
| Alert | `role="alert"` (assertive) or `role="status"` (polite) |
| Tooltip | `role="tooltip"`, `aria-describedby` on trigger |
| Menu | `role="menu"`, `role="menuitem"`, `aria-haspopup` |
| Tree | `role="tree"`, `role="treeitem"`, `aria-expanded` |
| Breadcrumb | `<nav aria-label="Breadcrumb">`, `aria-current="page"` |
| Live region | `aria-live="polite"` or `aria-live="assertive"`, `aria-atomic` |
```

