---
id: platform-design-skills
type: knowledge
owner: OA_Triage
---
# platform-design-skills
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

### File: AGENTS.md
```md
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

### File: CHANGELOG.md
```md
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

### File: CLAUDE.md
```md
AGENTS.md
```

### File: skills\web\AGENTS.md
```md
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

### File: skills\web\metadata.json
```json
{
  "version": "1.0.0",
  "organization": "Platform Design Skills",
  "date": "February 2026",
  "abstract": "Web platform design and accessibility guidelines. 70+ rules across 11 categories covering WCAG 2.2 accessibility, responsive design, semantic HTML, performance, forms, animations, typography, dark mode, internationalization, and Progressive Web Apps. Framework-agnostic with HTML/CSS/JS examples.",
  "references": [
    "https://www.w3.org/WAI/WCAG22/quickref/",
    "https://developer.mozilla.org/en-US/docs/Web",
    "https://web.dev",
    "https://www.a11yproject.com"
  ]
}

```

### File: skills\web\SKILL.md
```md
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
  <!--
... [TRUNCATED]
```

### File: skills\web\rules\_sections.md
```md
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
| 
... [TRUNCATED]
```

