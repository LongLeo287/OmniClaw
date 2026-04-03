---
id: github.com-socratespap-grabbit-7d4217e6-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:23.996446
---

# KNOWLEDGE EXTRACT: github.com_socratespap_Grabbit_7d4217e6
> **Extracted on:** 2026-04-01 14:26:28
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523886/github.com_socratespap_Grabbit_7d4217e6

---

## File: `.gitignore`
```
GEMINI.md
refactor_plan.md
test_links.html
zendesk_repro.html
rules.md
features_to_add.md
smart_select.md
Grabbit.zip
.agent
CLAUDE.md
wordpress-plugin/
Landing Page/
PRIVACY_POLICY.md
backup_script.bat
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 socratisp.com

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
# Grabbit - Chrome Extension

![Users](https://img.shields.io/badge/Users-50,000%2B-blue?style=for-the-badge&logo=googlechrome&logoColor=white)
![Rating](https://img.shields.io/badge/Rating-4.1%20%2F%205%20Stars-brightgreen?style=for-the-badge&logo=starship&logoColor=white)

**Grabbit** is a powerful Chrome Extension (Manifest V3) that enables users to select multiple links on a webpage using a customizable drag-select interface. Users can perform various actions on selected links, such as opening them in new tabs/windows or copying their URLs to the clipboard.

[Available on the Chrome Web Store](https://chromewebstore.google.com/detail/grabbit/madmdgpjgagdmmmiddpiggdnpgjglcdk)

## BrowserStack

This project is tested with BrowserStack

## Key Features

*   **Drag-Select:** Intuitive visual selection box.
*   **Custom Actions:** Configurable mouse/keyboard combinations including **A-Z keys** (e.g., G + Right Click to Copy).
*   **Adaptive Smart Selection:** Intelligent pattern-based filtering that automatically detects and selects consistent groups of links (e.g., repeating video titles, grid items) while ignoring clutter.
*   **Linkify:** Automatically converts plain text URLs on web pages into clickable links. Includes an **Aggressive Mode** for domain-only recognition (e.g., `google.com`) and support for links inside code blocks.
*   **Exclusion Filters:** Global keyword and Regular Expression (Regex) filtering to automatically skip unwanted links during drag-selection. Manageable via a dynamic tag-based UI.
*   **Disabled Domains:** Blocklist feature to completely disable Grabbit (Selection, Linkify, Visited tracking) on specific domains. Includes a visual "OFF" badge and a popup overlay with an "Enable" button.
*   **Options Page:** Extensive customization for colors, behavior, and granular filtering rules.
*   **Enhanced Copy Formatting:** Expanded "Copy URLs with Titles" action with support for **Markdown**, **JSON**, and customizable separators (Comma, Dot, Tab, etc.).
*   **Create Bookmarks:** Select multiple links and instantly save them as bookmarks in a folder named after the current page title.
*   **Advanced Options:** Dedicated section for power-user features. Now includes **animated toggle switches**, a dynamic UI that adapts to selected features, and a robust filter/domain management system.
*   **Configurable "Mark as Visited":** (New) Per-action setting in Advanced Options to visually mark links as visited (purple) in the browser.
*   **Dynamic Link Detection:** (New) Automatically detects and allows selection of new links that appear during a drag (e.g., from **infinite scroll** or lazy loading).
*   **Duplicate Link Highlighter:** (New) Visually identifies links with the same URL on a page using unique colored underlines. Helps in finding repetitive content and managing navigation.
*   **AI Product Comparison:** (New) Select multiple product tabs and generate a comprehensive AI-powered comparison table with a clear winner, pros/cons, and feature breakdown.
*   **AI Article Summarization:** (New) Summarize articles and blog posts with AI-generated key takeaways, topic tags, and bottom line analysis.
*   **AI YouTube Video Summarization:** (New) Summarize YouTube videos with chapter-by-chapter breakdowns, key points, and detailed summaries for each section. Automatically extracts transcripts and creates intelligent chapter markers.
*   **Modern Architecture:** Refactored into a modular structure for better maintainability and performance.


## Architecture & Technology

The project is built using standard web technologies and the Chrome WebExtensions API. It does **not** require a build step (no Webpack/Rollup) and runs directly as an unpacked extension.

### High-Level Structure

```
Frontend (Chrome Extension)
├── Content Scripts (injected into webpages)
│   ├── Event handling (drag selection, mouse/keyboard)
│   ├── UI rendering (selection box, counter label)
│   ├── Business logic (collision detection, link processing)
│   └── Special features (linkify, visited tracking, smart selection)
├── Background Service Worker (privileged operations)
│   ├── Tab/window management
│   ├── Bookmark creation
│   ├── Clipboard operations
│   ├── Payment integration (ExtPay)
│   └── AI features coordination (comparison, summarization)
├── Options Page (settings UI)
│   ├── Action management (create/edit/delete actions)
│   ├── Advanced options (filters, disabled domains, linkify)
│   ├── Popup customization (button order, visibility)
│   └── Format preview (copy formatting)
├── Popup (quick actions)
│   ├── Tab management (copy/open URLs)
│   └── AI feature triggers (compare, summarize)
└── AI Features Pages
    ├── Product Comparison (AI Features/compare/)
    └── Article Summarization (AI Features/summarize/)
    └── YouTube Video Summarization (AI Features/youtube-summary/)

Backend (WordPress Plugin)
├── Secure API proxy (OpenRouter API)
├── ExtPay integration (payment validation)
├── Rate limiting (monthly quotas with automatic reset)
└── User management (subscribers, usage tracking, manual subscriber management)
```

### Component Interaction Flow

1. **User Action**: Content scripts detect mouse/keyboard input on webpages
2. **Event Processing**: `grabbit.js` orchestrates event handling through modular components
3. **Action Execution**: For privileged operations (tabs, bookmarks), messages sent to `background.js`
4. **AI Features**: Comparison data sent through WordPress backend proxy (API keys never exposed to client)
5. **Result Display**: UI components render feedback (selection box, success messages, comparison tables)
6. **Settings Management**: Options pages use modular components (sidebar, footer) with auto-initialization
7. **Popup Actions**: Popup loads configuration from storage, renders buttons based on user preferences
8. **Premium Features**: ExtPay validates subscription, backend enforces rate limiting

### Core Technologies
*   **JavaScript (Vanilla):** Core logic, utilizing ES6+ features.
*   **HTML/CSS:** UI for Popup and Options pages. Leveraging **CSS Variables** for a centralized design system.
*   **Chrome APIs:** `storage`, `tabs`, `windows`, `clipboard`, `scripting`, `bookmarks`.
*   **Manifest V3:** Adheres to the latest Chrome extension security and background service worker requirements.
*   **Backend (PHP/WordPress):** Secure server-side proxy for handling OpenRouter AI requests and Stripe integration.
*   **AI:** OpenRouter API for product comparison, article summarization, and YouTube video summarization.
*   **Payments:** ExtPay (Chrome extension payment platform), Stripe API.

### Directory Structure

*   **`manifest.json`**: The entry point. Defines permissions, background scripts, and the order of content script injection.
*   **`css/`**: Global styles and design tokens.
    *   `variables.css`: **Single Source of Truth** for design tokens (colors, gradients, fonts, shadows, transitions).
    *   `options.css`: Main layout and component styles for the settings page.
    *   `sidebar.css`: Styles for the navigation sidebar.
*   **`popup/`**: The small window that appears when clicking the extension icon.
    *   `popup.html`: Structure of the popup, featuring a **Modern Glassmorphism** design.
    *   `popup.js`: Logic for quick actions (e.g., "Copy all tabs"). Handles dynamic success states for nested button elements.
    *   `popup.css`: **Complete Redesign** featuring animated background orbs, dark glassmorphism cards, and gradient icon boxes. Standardized using global variables.
*   **`options.html` / `js/options/`**: The full settings page for configuring actions and appearance, now refactored into ES modules.
*   **Advanced Options:** Dedicated sub-page for power-user settings.
    *   `advancedOptions.html`: Layout for experimental features including Linkify, **Exclusion Filters**, and **Disabled Domains**.
    *   `advancedOptions.js`: Logic for saving/loading advanced settings, managing the exclusion filter list, and the domain blocklist.
    *   `advancedOptions.css`: Specific styling for advanced controls (toggle switches, filter tags).
*   **`AI Features/compare/`**: (New) Standalone page for AI-powered product comparisons.
    *   `compare.html`: Comparison page structure.
    *   `compare.js`: Logic for comparison workflow and UI.
    *   `compare.css`: Premium Glassmorphism styling.
*   **`AI Features/summarize/`**: (New) Standalone page for AI-powered article summarization.
    *   `summarize.html`: Summary page structure.
    *   `summarize.js`: Logic for summarization workflow and UI.
    *   `summarize.css`: Premium Glassmorphism styling.
*   **`AI Features/youtube-summary/`**: (New) Standalone page for AI-powered YouTube video summarization.
    *   `youtube-summary.html`: YouTube summary page structure with loading states and chapter-by-chapter result views.
    *   `youtube-summary.js`: Logic for YouTube summarization workflow, handles transcript extraction via InnerTube API, and renders chapter summaries.
    *   `youtube-summary.css`: Premium Glassmorphism styling specific to the YouTube summary interface.
*   **`wordpress-plugin/`**: Server-side backend code.
    *   `grabbit-backend.php`: Secure proxy and user management plugin.
    *   `README.md`: Backend setup guide.
*   **`js/linkify.js`**: (New) Scans the page for plain text URLs and converts them to clickable `<a>` tags if enabled.
*   **`js/visited.js`**: (New) Handles persistent tracking and visual marking of visited links to bypass browser redirect limitations.

### 4. Modular Options Page
The options page has been refactored from a single monolithic file into multiple ES modules, improving code reuse and testing:
- **`main.js`**: Orchestrates initialization.
- **`env.js`**: Environment constants (OS detection, Extension context).
- **`storage.js`**: Handles saving/loading actions to `chrome.storage.sync`.
- **`utils.js`**: Helpers for colors, key labels, and tooltips.
- **`preview.js`**: Live format preview for "Copy URLs & Titles".
- **`card.js`**: Component for managing action cards.
- **`modal.js`**: Manages the "Add/Edit Action" modal lifecycle.
- **`popup-config.js`**: Popup button management and drag-and-drop reordering.

### 5. Critical Content Script Loading Order

The order in `manifest.json` → `content_scripts` → `js` is **critical**. Scripts share a global scope:

1. `js/state.js` - **MUST LOAD FIRST** - Defines `GrabbitState` global object and `CONSTANTS`
2. `js/utils.js` - Helper functions used by other modules
3. `js/ui.js` - DOM manipulation functions
4. `js/visited.js` - Visited link tracking
5. `js/smart-select.js` - Adaptive pattern-based selection
6. `js/logic.js` - Core business logic
7. `js/linkify.js` - Text-to-link conversion
8. `js/duplicate-highlighter.js` - Duplicate link highlighting
9. `js/grabbit.js` - **MUST LOAD LAST** - Main entry point and event orchestrator

**Never reorder these scripts without understanding dependencies**. Many modules reference `GrabbitState` or functions from earlier-loaded scripts.

## CSS Architecture & Design System

The project uses a **"No Build Step"** CSS architecture that leverages modern browser features to maintain a clean and scalable codebase.

### 1. Centralized Variables (`css/variables.css`)
All design tokens are defined in the `:root` pseudo-class within `variables.css`. This file acts as the single source of truth for:
*   **Color Palette**: Integrated primary/secondary colors and status colors (success, warning, error).
*   **Gradients**: Standardized linear gradients for buttons, backgrounds, and the sidebar.
*   **Typography**: A unified font stack across all extension pages.
*   **Shadows & Transitions**: Consistent depth and motion tokens.

### 2. Externalized & Redesigned Popup Styles
To maintain separation of concerns and benefit from caching, styles have been extracted from `popup.html` into `popup.css`. The popup has been completely redesigned with a premium aesthetic:
*   **Glassmorphism**: Using `backdrop-filter` and semi-transparent backgrounds for a modern "frosted glass" look.
*   **Animated Components**: Decorative floating background orbs and pulsing logo glows for a living UI.
*   **Visual Hierarchy**: Buttons now feature distinct icon boxes with custom gradients, primary titles, and descriptive subtitles.
*   **Dynamic States**: Success states are handled gracefully with color transitions and content updates via JavaScript.

### 3. Component-Based Styles
Styles are organized by component area (Options, Sidebar, Popup), each inheriting variables from the global pool. This allows for rapid UI adjustments without global "find and replace" operations.

## Codebase Reference

### Content Scripts (Shared Scope)

**`js/grabbit.js`** - Main Entry Point & Event Orchestrator
- Initializes by loading saved actions from `chrome.storage.sync`
- Core event listeners: `mousedown` (start tracking), `mousemove` (check 5px drag threshold), `mouseup` (finalize selection), `keydown` (modifiers/ESC), `window.blur` (cleanup)
- Delegates specific logic to specialized modules
- Activates selection UI only after 5px drag threshold (prevents accidental selections)

**`js/state.js`** - State Management
- `GrabbitState`: Global state object (mouse position, selection status, cached links, active modifiers, filters)
- `CONSTANTS`: Drag threshold (5px), scroll speed, link refresh interval (500ms for infinite scroll), debounce delays

**`js/logic.js`** - Core Business Logic
- `updateSelectionBox()`: Calculates geometry relative to document
- `handleScroll(mouseY)`: LinkClump-style auto-scrolling near viewport edges
- `isLinkExcluded(url)`: Checks URLs against keyword/regex filters
- `updateSelectedLinks()`: Collision detection, Smart Select orchestration, exclusion filtering
- `processSelectedLinks(matchedAction)`: Executes actions (open/copy/bookmark) with deduplication and formatting

**`js/ui.js`** - DOM & Visuals
- `createSelectionBox()`: Absolute-positioned selection overlay
- `createCounterLabel()`: Floating status label with action text
- `updateVisualStyles()`: Syncs box colors, border styles, counter text
- `cleanupSelection()`: Removes UI, resets state, clears intervals

**`js/utils.js`** - Helper Functions
- `getOS()`: Cross-platform OS detection
- `checkKeyCombination(e, mouseButton)`: Matches input against saved actions
- `getMouseButton(e)`: Normalizes mouse button codes
- `isElementSticky(element)`: Collision detection helper for sticky headers
- `isDomainDisabled(disabledDomains)`: Checks current domain against blocklist
- `debounce(func, wait)`: Performance wrapper for high-frequency events
- `getAllLinks(root)`: Deep link discovery including Shadow DOM traversal

**`js/smart-select.js`** - Adaptive Pattern-Based Selection
- `apply(linksInBox)`: Analyzes links in selection, builds frequency map of signatures
- `getLinkSignature(link, style)`: Generates unique signature based on structure, tag name, font weight/size
- `isLinkImportant(link, style)`: Heuristic engine for semantically/visually important links (headings, bold)
- Filters selection to repeating patterns (count >= 2), prioritizing "important" links

**`js/visited.js`** - Persistent Visited State Management
- Bypasses privacy restrictions (e.g., Google Search redirects) using `chrome.storage.local`
- `injectGrabbitVisitedStyles()`: Injects CSS for `.grabbit-visited` class
- `applyGrabbitVisitedStyling()`: Restores visited styling on page load
- `markLinksAsGrabbitVisited(urls, anchorElements)`: Persists and updates UI

**`js/linkify.js`** - Text-to-Link Conversion
- Regex engine for `http`, `https`, `ftp`, `www` URLs
- Aggressive Mode: Prefix-less domain recognition (e.g., `github.com/user/repo`)
- DOM traversal: Recursive walk, skipping `<a>`, `<script>`, `<style>`, `<textarea>`
- Code block support: Includes `<code>` and `<pre>` tags
- Shadow DOM support: Handles URLs inside Shadow Roots
- Linkified elements get `.grabbit-linkified` class

**`js/duplicate-highlighter.js`** - Duplicate Link Highlighting
- Automatically highlights links that share the same URL on a page.
- Uses vibrant, unique colors for each group of duplicate links.
- Uses `MutationObserver` to handle dynamic content (infinite scroll).
- Supports Shadow DOM for deep link discovery.
- Respects domain blocklist and user settings.

### Background Service Worker

**`js/background.js`** - Privileged API Bridge
- `chrome.runtime.onInstalled`: Sets defaults on first run
- `chrome.runtime.onMessage`: Bridges content script requests to privileged APIs
  - `tabs.create`: Opens links in new tabs
  - `windows.create`: Opens links in new windows
  - `bookmarks.create`: Creates bookmarks
  - Clipboard operations via `chrome.clipboard`
- `updateIconState(tabId, url)`: Manages "OFF" badge for disabled domains
- `createBookmarksInFolder(parentId)`: Recursive helper for batch bookmark creation
- Coordinates AI comparison workflow with backend

### Options Page (Modular ES6)

**`js/options/main.js`** - Orchestrator
- `initialize()`: Main entry point
- `setupExtensionButtons()`: Pin and Rate button logic

**`js/options/modal.js`** - Add/Edit Dialog
- `openModal()` / `closeModal()`: Lifecycle management
- `handleSaveAction()`: Form validation and persistence
- `setupFormValidation()`: Real-time UI feedback
- `updateFormatOptionVisibility()`: Dynamic UI toggling

**`js/options/card.js`** - Action Cards
- `createActionCard(action)`: Visual representation of saved actions
- `openEditModal(action, card)`: Pre-populates modal for editing

**`js/options/preview.js`** - Format Preview
- `updateFormatPreview()`: Live terminal-style preview for copy formatting
- `setupPreviewListeners()`: Attaches change events

**`js/options/storage.js`** - Persistence
- `saveActionsToStorage(actions)`: Syncs to `chrome.storage.sync`
- `loadActionsFromStorage()`: Retrieves settings on load

**`js/options/env.js`** - Environment Detection
- `isExtension`: Checks if running in Chrome extension context
- `currentOS`: Cross-platform OS detection for UI customization

**`js/options/utils.js`** - Options Page Utilities
- `generateUniqueColor()`: Assigns colors to action cards from predefined palette
- `updateKeyLabels()`: Updates modifier key labels based on OS (e.g., Command ⌘ on Mac)
- `initializeTooltips()`: Sets up fixed positioning for tooltips
- `isDuplicateCombination()`: Validates for duplicate key+mouse combinations

**`js/options/popup-config.js`** - Popup Button Management
- `POPUP_BUTTONS`: Registry of all popup buttons with metadata
- `loadPopupConfig()` / `savePopupConfig()`: Persist button order and enabled state
- `initializePopupConfig()`: Renders drag-and-drop button list
- Drag-and-drop reordering with `setupDragAndDrop()`
- Toggle switches for enabling/disabling buttons
- `getButtonIcon()`: Returns SVG HTML for button icons

### AI Features Pages

**`AI Features/compare/compare.js`** - Comparison Workflow & UI
- Checks for pending comparison data from `chrome.storage.local`
- `runComparison()`: Orchestrates 3-step process (Extract → Analyze → Build)
- Communicates with `background.js` to trigger AI analysis
- Handles error states (premium required, monthly limit reached)
- `renderResults(data)`: Builds Winner Banner, Products Grid, Features Table
- `updateStep(stepNumber)`: Progress tracker visualization

**`AI Features/summarize/summarize.js`** - Summarization Workflow & UI
- Checks for pending summary data from `chrome.storage.local`
- `runSummary()`: Orchestrates summarization process (Extract → Summarize → Render)
- Communicates with `background.js` to trigger AI analysis
- Handles error states (premium required, monthly limit reached)
- `renderResults(data)`: Builds Summary Banner, Key Takeaways, Topics, Bottom Line

**`AI Features/youtube-summary/youtube-summary.js`** - YouTube Summary Workflow & UI
- Checks for pending YouTube summary data from `chrome.storage.local`
- `runSummary()`: Orchestrates YouTube summarization process (Extract Transcript → Summarize → Render Chapters)
- Communicates with `background.js` to trigger transcript extraction via YouTube InnerTube API
- Handles error states (premium required, monthly limit reached, no transcript available)
- `renderResults(data)`: Builds Summary Banner, Key Points, Chapter-by-Chapter Breakdown with detailed summaries
- Each chapter includes timestamp, short summary (2 sentences), and detailed summary (8-10 sentences)

### Popup (Quick Access Interface)

**`popup/popup.js`** - Main Popup Script
- Loads popup configuration from `popup-config.js`
- Renders enabled buttons in configured order
- **Copy Selected Tabs**: Copies URLs of currently selected tabs
- **Copy All Tabs**: Copies all open tab URLs in current window
- **Open Copied Links**: Opens links from clipboard (one per line)
- **Compare Products**: Triggers AI product comparison workflow
- **Summarize Page**: Triggers AI article summarization workflow
- Premium badge display and ExtPay integration
- Glassmorphism UI with animated backgrounds

**`popup/popup.html`** - Popup Interface
- Glassmorphism design with animated background orbs
- Dynamic button rendering based on configuration
- Premium features with PRO badges
- Responsive layout for various screen sizes

**`popup/popup.css`** - Popup Styling
- Glassmorphism effects with backdrop-filter
- Animated gradient backgrounds and orbs
- Button hover effects and transitions
- Premium badge styling
- Inherits all design tokens from `css/variables.css`

### Reusable Components

**`js/components/sidebar.js`** - Navigation Sidebar Component
- `GrabbitSidebar` class: Auto-initializing component
- Renders navigation menu with links to Main Options, Popup Options, Advanced Options
- Handles active section highlighting and hash-based navigation
- Internal page section switching without page reload

**`js/components/footer.js`** - Footer Component
- `GrabbitFooter` class: Auto-initializing component
- Renders footer with support links (PayPal, Revolut)
- Displays contributor list with GitHub links
- "Contribute on GitHub" callout button
- Handles rate and pin extension button functionality

### Premium & Payment Integration

**`js/premium.js`** - ExtPay Payment Manager
- `Premium.init()`: Initializes ExtPay background service
- `Premium.getUser()`: Returns payment status, email, trial status
- `Premium.openPaymentPage()`: Opens ExtPay payment flow
- `Premium.openLoginPage()`: Opens ExtPay login for existing users
- `Premium.validateWithBackend(email)`: Validates license with WordPress backend
- Syncs with ExtPay dashboard (extension ID: `grabbit-premium`)

**`js/ExtPay.js`** - Third-Party Payment Library
- External ExtPay library for Chrome extension payments
- Handles subscription management, trial periods, payment processing
- Injected as content script on `extensionpay.com` domain
- DO NOT MODIFY - External dependency

### AI Features Handlers (background.js)

**`handleYouTubeSummary()`** - YouTube Video Summarization Orchestrator
- Verifies premium status and fetches API token
- Extracts YouTube video data via `extractYouTubeDataFromPage()` using InnerTube API
- Sends transcript and metadata to WordPress backend `/youtube-summary` endpoint
- Handles monthly quota limits and error states (no captions, subscription inactive)
- Returns structured chapter-by-chapter summary with timestamps and detailed summaries

**`extractYouTubeDataFromPage()`** - YouTube Data Extraction (Injected Function)
- **Executed in MAIN world** to access YouTube's `window.ytcfg` object
- **Extracts**:
  - Video title from `h1.ytd-video-primary-info-renderer`
  - Channel name from channel element
  - Chapters from video player or description (timestamp pattern matching)
  - InnerTube API key for authenticated requests
- **InnerTube Player API Call**:
  - Uses ANDROID client (bypasses restrictions)
  - Fetches caption tracks in JSON3 format
  - Prefers English captions, falls back to first available
- **Transcript Processing**:
  - Inserts timestamp markers every 30 seconds for AI chapter accuracy
  - Formats timestamps as `[MM:SS]` or `[HH:MM:SS]`
  - Limits to 60,000 characters for long videos
  - Stores video duration for validation
- **Error Handling**: Returns structured error object if transcript unavailable

**`handleArticleSummary()`** - Article Summarization Orchestrator
- Verifies premium status and fetches API token
- Extracts article content via `extractArticleDataFromPage()`
- Sends to WordPress backend `/summarize` endpoint
- Handles monthly quota limits and subscription validation
- Returns structured summary with key takeaways and topics

**`handleProductComparison()`** - Product Comparison Orchestrator
- Verifies premium status and fetches API token
- Extracts product data from multiple tabs via `extractProductDataFromPage()`
- Sends to WordPress backend `/compare` endpoint
- Handles monthly quota limits and subscription validation
- Returns structured comparison with winner, pros/cons, and feature tables

**`getApiToken()`** - API Token Management
- Caches API token in `chrome.storage.local` to reduce backend requests
- Fetches token from `/get-token` endpoint with email authentication
- Throws descriptive errors with status codes and details
- Used by all AI feature handlers for authenticated requests

### Content Extraction

**`js/content-extractor.js`** - Product Content Extractor
- `extractProductData()`: Intelligently extracts product information for AI comparison
- **Title Extraction**: H1, product-title selectors, OG meta tags, document.title fallback
- **Price Extraction**: Multiple selector strategies (Amazon `.a-price-whole`, `.pdp-price`, etc.)
- **Description Extraction**: Product descriptions, meta descriptions, feature bullets (Amazon)
- **Specs Extraction**: Tables, definition lists, spec containers (limited to 5 blocks)
- Returns structured object with title, price, description, specs, URL, site name
- Used via `scripting.executeScript` in background.js for AI features

### Advanced Options Page

**`advancedOptions/advancedOptions.js`** - Advanced Settings Management
- **Linkify Settings**: Toggle linkify on/off, aggressive mode toggle
- **Exclusion Filters**: Add/remove keyword/regex patterns to filter out links
- **Disabled Domains**: Blocklist for domains where Grabbit should not activate
- Real-time validation, duplicate checking, status messages
- Persists all settings to `chrome.storage.sync`

**`advancedOptions/advancedOptions.html`** - Advanced Options UI
- Separate page from main options.html
- Linkify controls (enable/disable, aggressive mode)
- Exclusion filter management with tag-based UI
- Disabled domains blocklist management
- Loaded via sidebar navigation

**`advancedOptions/advancedOptions.css`** - Advanced Options Styling
- Form controls, toggle switches, input fields
- Tag-based filter list styling
- Status message animations
- Inherits from `css/variables.css`

### Popup Customization

**`popup/popupOptions/popupOptions.js`** - Popup Button Customization
- Allows users to reorder and enable/disable popup buttons
- Drag-and-drop interface for button reordering
- Toggle switches for button visibility
- Persists configuration to `chrome.storage.sync`

**`popup/popupOptions/popupOptions.html`** - Popup Options UI
- Separate settings page for popup customization
- Lists all popup buttons with icons, titles, subtitles
- Drag handles for reordering
- Reset to defaults button

**`popup/popupOptions/popupOptions.css`** - Popup Options Styling
- Drag-and-drop visual feedback
- Toggle switch styling
- Button preview cards
- PRO badge styling for premium features

## Development & Installation

Since there is no build process, you can work directly on the source files.

1.  **Load Unpacked:**
    *   Open Chrome and go to `chrome://extensions/`.
    *   Enable **Developer Mode** (top right).
    *   Click **Load unpacked**.
    *   Select the root directory of this project (where `manifest.json` is located).

2.  **Reloading Changes:**
    *   After modifying any file (especially `manifest.json` or background scripts), go to `chrome://extensions/` and click the **Reload** (circular arrow) icon on the Grabbit card.
    *   **Crucial:** You must also refresh any web pages where you are testing the content script for the changes to take effect.

## Key Development Patterns

### Global State Management
- `GrabbitState` in `js/state.js` is the single source of truth for:
  - Mouse positions (startX, startY, currentX, currentY)
  - Selection status (isSelecting, selectionBox, counterLabel)
  - Matched action and modifiers
  - Cached links and refresh interval
  - Active exclusion filters and disabled domains

### Event Handling Flow
1. `mousedown` in `grabbit.js`: Stores start position, doesn't activate UI
2. `mousemove`: Checks 5px drag threshold, then calls `activateSelection()`
3. `activateSelection()`: Creates UI elements, starts link refresh timer
4. `updateSelectedLinks()`: Collision detection, Smart Select, filtering
5. `mouseup`: Calls `processSelectedLinks()` with matched action
6. `cleanupSelection()`: Removes UI, resets state, clears intervals

### Action Matching System
- Actions stored in `chrome.storage.sync` with structure:
  ```javascript
  {
    mouseButton: 0|1|2,  // 0=left, 1=middle, 2=right
    modifierKey: "ctrl"|"shift"|"alt"|"meta"|"A"-"Z"|"",
    actionType: "open"|"copy"|"bookmark",
    settings: { /* action-specific config */ }
  }
  ```
- `checkKeyCombination()` in `utils.js` matches input against saved actions
- Modifiers include Ctrl, Shift, Alt, Meta, and letter keys A-Z

### Smart Selection Algorithm
1. Build frequency map of link signatures in selection box
2. Signature = structure + tag name + font weight + font size
3. If patterns repeat (count >= 2), filter to match those patterns
4. Prioritize "important" links (headings, bold text)
5. Reduces selection clutter on complex pages

### Infinite Scroll Support
- `refreshCachedLinks()` called every 500ms during selection
- Scans DOM for new links that appeared since selection started
- Handles lazy loading and infinite scroll scenarios
- Updates link cache without interrupting drag operation

## Common Tasks

### Adding a New Action Type
1. Update action type enum in `js/options/modal.js`
2. Add UI configuration in modal form
3. Add handling in `processSelectedLinks()` in `js/logic.js`
4. Add background message handler in `js/background.js` (if privileged API needed)
5. Test on various websites

### Modifying CSS
1. Check if token exists in `css/variables.css`
2. If not, add new token to `:root`
3. Reference token in component CSS
4. Test across different pages to ensure no conflicts

### Adding New Content Script Module
1. Create file in `js/` directory
2. Add to `manifest.json` → `content_scripts` → `js` array
3. **Critical**: Place in correct dependency order (state → utils → feature modules → grabbit.js)
4. If using `GrabbitState`, ensure it loads after `state.js`
5. Test by reloading extension and refreshing test pages

### Using Reusable Components

**Sidebar Component:**
- Add `<div id="sidebar-placeholder"></div>` to any settings page HTML
- Include `<script src="js/components/sidebar.js"></script>` before closing body tag
- Component auto-initializes on DOMContentLoaded
- Set active section with `data-active-section` attribute: `<div id="sidebar-placeholder" data-active-section="popup-options"></div>`

**Footer Component:**
- Add `<div id="footer-placeholder"></div>` to any settings page HTML
- Include `<script src="js/components/footer.js"></script>` before closing body tag
- Component auto-initializes and renders footer with support links and contributors
- Handles rate and pin button functionality automatically

Both components use class-based architecture with `render()` and `initLogic()` methods for easy customization.

### Customizing Popup Buttons

1. Navigate to Options page → Popup Options
2. Drag buttons to reorder (changes reflect immediately in popup)
3. Use toggle switches to enable/disable buttons
4. Configuration persists to `chrome.storage.sync` via `popup-config.js`
5. Popup reads configuration on load and renders buttons accordingly
6. To add new button types:
   - Add to `POPUP_BUTTONS` registry in `js/options/popup-config.js`
   - Implement handler in `popup/popup.js`
   - Add icon SVG to `getButtonIcon()` function

## Debugging

### Debugging Content Scripts
1. Open Chrome DevTools on test webpage
2. Check Console for errors
3. Inspect `GrabbitState` in Console: `console.log(GrabbitState)`
4. Use `debugger;` statements in content script files
5. Remember to reload extension and refresh page after code changes

### Debugging Background Script
1. Go to `chrome://extensions/`
2. Click "Service worker" link under Grabbit
3. Opens DevTools for background worker
4. Check Console for errors
5. Inspect messages received/sent

## Testing

### Testing Link Selection

**Recommended Test Sites:**
- Hacker News (news.ycombinator.com) - Clean link lists
- Reddit - Complex nested links
- Amazon/e-commerce sites - Product links for AI comparison
- Google Search - Test visited link tracking and redirects

**Testing Edge Cases:**
- Sticky headers that overlap content
- Infinite scroll (Twitter, Facebook feeds)
- Shadow DOM (web components)
- Links within iframes
- Very long pages (test auto-scrolling)

## Usage

1. Click the extension icon to access quick actions
2. Visit the options page to configure custom actions
3. On any webpage:
	- Hold configured mouse button (and key if set)
	- Drag to select multiple links
	- Release to perform the configured action

## Configuration

Access the options page to:
- Create new actions with custom key combinations
- Set different colors for selection boxes
- Configure smart selection options
- Manage existing actions
- Set default behaviors

## Tested via BrowserStack on

- Windows 10
- Windows 11, Chrome Latest Version (28 Jan 2026)
- MacOS Tahoe, Chrome Latest Version (28 Jan 2026)
- Linux, Chrome Latest Version (28 Jan 2026)

## Known Issues & Limitations

- 🔴 ESC key conflicts with Windows shortcuts when used with Ctrl/Shift/Alt
- 🔴 **Letter keys (A-Z)** as modifiers may not work with some laptop trackpads (palm rejection)
- 🔴 Not compatible with Netsuite
- 🟢 Add two actions. Action 1: Ctrl + Right Mouse for copy link. Action 2: Right mouse for open links - Copy links with CTRL + Right Mouse, release the CTRL, it does not change to open links while the opposite works.
- 🟢 Add two actions. Action 1: Ctrl + Right Mouse for copy link. Action 2: Ctrl + Left mouse for open links. Only action with right mouse works
- 🟢 Lifting keyboard key and no action is found for mouse only actions, is still selecting
- 🟢 Removed unused context menu permission
- 🟢 Fix naming of buttons in Mac
- ⚠️ Limited to Chrome (Manifest V3)
- ⚠️ No automated test suite (manual testing only)
- ⚠️ ExtPay.js is a third-party dependency - updates may require testing payment flow
- ⚠️ AI features require active internet connection and valid subscription

## Features to be added

- 🟢 Open Links/tabs in reverse order
- 🟢 Copy links with titles
- 🟢  Provide different color on add new action
- 🟢  Added A-Z keys as modifier options for actions
- 🟢 Duplicate Link Highlighter
- 🔴 Append Urls to clipboard. Clipboard = selected links + clipboard
- 🟢 Add rating button
- 🟢 Open tabs next to active tab
- 🟢 Recognize <a> tags that are not visible
- 🟢 Include Compatibility with Youtube Subscriptions links
- 🟢 Add delay when opening tabs
- 🟢 Include option when copying URLs ("Title tab Url, instead of Title \n Url")
- 🟢 Create Bookmarks
- 🔴 Fix compatibility with Netsuite
- 🔴 Improve trackpad compatibility for letter key modifiers

## Technology Stack

- **Frontend**: Vanilla JavaScript (ES6+), HTML, CSS
- **Chrome APIs**: storage, tabs, windows, clipboard, scripting, bookmarks
- **Backend**: PHP/WordPress plugin
- **AI**: OpenRouter API
- **Payments**: ExtPay (Chrome extension payment platform), Stripe API
- **Database**: WordPress MySQL database
- **Content Extraction**: Custom DOM parsing for e-commerce sites
- **Component Architecture**: Class-based reusable components with auto-initialization
- **Design System**: CSS Variables, Glassmorphism design, component-based styling
- **Testing**: Manual testing on BrowserStack across multiple platforms

## Changelog

Please refer to the [changelog](changelog.md) for detailed changes in each version.

## Contributions
- @TheTacoScott - https://github.com/TheTacoScott
- @oaustegard - https://github.com/oaustegard
- @digirat - https://github.com/digirat
- Subtiltee - https://subtiltee.com/all-extensions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Tags

- This is a Linkclump replacement/alternative
- This is a Copy All Urls replacement/alternative
```

## File: `changelog.md`
```markdown
## Version 3.8.2 Changelog:
- **New Feature: Duplicate Link Highlighter**: Automatically highlights links that share the same URL on a page with unique colored underlines.
- **Visual Grouping**: Each group of duplicate links is assigned a distinct, vibrant color for easy identification.
- **Dynamic Content Support**: Uses a MutationObserver to automatically detect and highlight new duplicate links that appear during infinite scrolling or lazy loading.
- **Shadow DOM Support**: Intelligently scans inside Shadow Roots to ensure all links on the page are accounted for.
- **Granular Control**: Can be enabled or disabled via the Advanced Options page and respects the domain blocklist.

## Version 3.8.1 Changelog:
- **Improved YouTube Summarization for Long Videos**: Now supports videos up to 2+ hours by significantly increasing character limits.
- **Extended Chapter Support**: Increased maximum chapter limit from 20 to 50 to ensure deep analysis of long-form content.

## Version 3.8.0 Changelog:
- **New Feature: AI YouTube Video Summarization**: Summarize YouTube videos with AI-generated insights from video transcripts.
  - Comprehensive video overview with AI-generated summary
  - Chapter-by-chapter breakdown with timestamps for easy navigation
  - Short and detailed summaries for each chapter (expandable UI)
  - Key takeaways highlighting main points from the video
  - Topic tags for content categorization
  - Video thumbnail, title, and channel information display
  - Export options: Copy summary to clipboard, Download as Text file, Download as standalone HTML page
  - Works on YouTube video pages (youtube.com/watch) via popup button
  
## Version 3.7.0 Changelog:
- **New Feature: AI Product Comparison**: Select multiple product tabs (2-5) and generate comprehensive AI-powered comparisons.
  - Winner selection with clear reasoning
  - Detailed pros/cons analysis for each product
  - Side-by-side feature comparison table
  - Product scores (1-10 scale) and ratings
  - Premium feature with daily quota tracking
- **New Feature: AI Article Summarization**: Summarize articles and blog posts with AI-generated insights.
  - 3-4 sentence comprehensive summary
  - 5 key takeaways highlighting main points
  - Topic tags for categorization
  - Bottom line verdict with recommendations
  - Works on current active tab
  - Premium feature with daily quota tracking
- **Secure Backend Integration**: Both features use WordPress plugin as secure proxy for AI API.
- **Enhanced Rate Limiting**: Enforced daily quotas (default 25) per premium subscriber across both AI features
- **Premium UI Updates**: Added new "Summarize Page" button to popup with premium styling and PRO badge

## Version 3.6.0 Changelog:
- **Optional Bookmarks Permission**: Moved the "bookmarks" permission to optional permissions to improve user privacy.
- **Runtime Permission Request**: The extension now only requests bookmark access when you specifically use the "Create Bookmarks" action.
- **Improved Transparency**: Reduced initial installation permission footprint.

## Version 3.5.9 Changelog:
- **Dynamic Link Detection**: Implemented periodic link re-caching (every 500ms) while the selection box is active.
- **Support for Infinite Scroll**: Newly loaded links (e.g., from lazy loading or infinite scrolling) are now automatically recognized and selectable without restarting the selection.
- **Performance Optimized**: Re-caching only scans for new link elements that weren't already in the cache.
- **Robust Cleanup**: Improved state management to ensure all intervals are correctly cleared when selection ends.

## Version 3.5.8 Changelog:
- **Update Notification System**: Added a new notification system to alert users when a new version is installed.
- **Extension Icon Badge**: Shows a green "!" badge on the extension logo across all tabs when an update occurs.
- **Interactive Version Badge**: The version label in the popup footer is now interactive and shows a pulsing notification dot when an update is pending.
- **Changelog Integration**: Clicking the version badge automatically clears the notification and opens the official changelog in a new tab.

## Version 3.5.7 Changelog:
- **Storage Migration & Validation**: Implemented automatic migration logic that validates and repairs saved actions on extension install/update.
- **Upgrade Compatibility Fix**: Prevents extension breakage when users upgrade from very old versions with incompatible storage schemas.
- **Data Preservation**: Actions with missing properties are automatically repaired with sensible defaults; only completely corrupted actions are removed.
- **Console Logging**: Added informative console messages when migration or repair occurs.

## Version 3.5.6 Changelog:
- **Simplified Pattern-Based Smart Select**: Completely rewrote the Smart Select algorithm. It now detects repeating link patterns and automatically filters to select only consistent link types.
- **Frequency-Based Filtering**: If a link pattern appears 2+ times, only those matching links are selected. If all links are unique, all are selected.
- **Important Pattern Priority**: When multiple patterns repeat, "important" patterns (headings, bold text) are prioritized over standard ones.
- **New Module: `js/smart-select.js`**: Extracted Smart Select logic into a standalone module for better maintainability.

## Version 3.5.5 Changelog:
- **Universal Adaptive Smart Select**: Upgraded Smart Select to "learn" from your first selection. If you start dragging on a specific type of link (e.g., a YouTube video title, a DeviantArt card, or a bold Reddit post), Grabbit will automatically filter subsequent selections to match that exact type, ignoring clutter like channel names or author links.
- **Deep Inspection Engine**: Enhanced the detection logic to support modern complex websites where links wrap headings or bold text (common in card/grid layouts), ensuring robust performance across virtually all sites.

## Version 3.5.4 Changelog:
- **Improved Link Detection (Google Search)**: Implemented smart filtering for Google Search results to only capture primary results.
- **Internal Link Filtering**: Automatically skips Google tracking URLs, search query links, and embedded ngrams when browsing Google Search.
- **Nested Link Prevention**: Added a global safeguard to skip anchor tags that are descendants of other anchor tags, preventing duplicate/junk selections on complex pages.

## Version 3.5.3 Changelog:
- **New Feature: Configurable "Mark as Visited"**: Users can now enable or disable the "Mark links as visited" behavior on a per-action basis via the Advanced Options in the Action Modal.

## Version 3.5.2 Changelog:
- **Removed `history` Permission**: Addressed user complaints about the "Read your browsing history" permission request by removing the `chrome.history` API usage.
- **Reduced Permission Footprint**: The extension no longer explicitly adds opened links to browser history; Chrome handles this natively when tabs are viewed.

## Version 3.5.1 Changelog:
- **UI Overhaul: Modern Toggle Switches**: Replaced all advanced option checkboxes and "On/Off" dropdowns in the Action Modal with beautiful, animated toggle switches.
- **Improved UX**: Enhanced the visual consistency of the configuration modal with sleek gradients and smoother interaction feedback.
- **Premium Aesthetics**: Integrated the same high-end toggle style from the Advanced Options page into the main Action Modal for a cohesive design experience.

## Version 3.5.0 Changelog:
- **New Feature: Disabled Domains (Blocklist)**: Users can now specify domains where Grabbit will be completely inactive.
- **Visual "OFF" State**: The extension icon now displays a dark gray "OFF" badge when browsing a blocked domain.
- **Smart Popup Overlay**: Implemented a dedicated "Disabled" state in the popup with an easy "Enable for this site" button.
- **Global Feature Blocking**: Ensures all core modules (Drag-Select, Linkify, Visited Tracking) respect the domain blocklist.

## Version 3.4.0 Changelog:
- **New Feature: A-Z Modifier Support**: Users can now use any letter key (A-Z) as a modifier for actions, in addition to Ctrl, Shift, and Alt.
- **Improved Action Flexibility**: Significantly expanded the range of possible custom keyboard + mouse shortcuts.
- **Smart Key Tracking**: Implemented a robust real-time tracking system for letter keys to ensure reliable multi-key activation.
- **Trackpad Compatibility Warning**: Added an intelligent warning notice in the options UI to alert users about potential palm rejection or hardware limitations on some laptop trackpads when using letter keys.
- **State Management Update**: Integrated a new `pressedKeys` state container for consistent handling of non-standard modifier combinations.

## Version 3.3.0 Changelog:
- **New Feature: Create Bookmarks**: Users can now select multiple links and save them directly to a bookmark folder.
- **Dynamic Folder Management**: Automatically creates bookmark folders named after the current page title and intelligently reuses existing folders with the same name.
- **Improved UI Feedback**: The selection counter label now dynamically updates to "be saved as bookmarks" when the bookmarking action is active.
- **Core Updates**: Added "bookmarks" permission support to core extension logic.

## Version 3.2.8 Changelog:
- **Major Copy Action Upgrade**: Enhanced "Copy URLs with Titles" action with **Markdown** and **JSON** support.
- **Custom Separators**: Added options for **Comma** and **Dot** separators in addition to Newline, Space, and Tab.
- **Format-Aware UI**: The Action Modal now intelligently hides irrelevant separator options when Markdown or JSON formats are selected.
- **Action Card Updates**: Saved action cards now clearly display the chosen format (Markdown/JSON) and separator type.

## Version 3.2.7 Changelog:
- **Modular Codebase**: Refactored `options.js` into 7 separate ES modules (`main`, `env`, `storage`, `utils`, `preview`, `card`, `modal`) for improved maintainability.
- **Modernized Options Page**: Updated `options.html` to use native ES module imports.

## Version 3.2.6 Changelog:
- **New Feature: Format Preview**: Added a live, syntax-highlighted preview to the "Copy URLs with Titles" action. Users can now see exactly how their output will look in real-time while adjusting format patterns, separators, and link spacing.
- **UI Enhancement**: Implemented a code-themed terminal preview box in the action configuration modal for immediate visual feedback.

## Version 3.2.5 Changelog:
- **New Feature: Global Exclusion Filters**: Users can now define keywords and Regular Expressions to automatically exclude specific links from being selected.
- **Improved Filter Management**: Added a dedicated UI in Advanced Options to add, view, and remove filter tags.
- **Performance Optimization**: Implemented pre-compiled regex objects for fast URL matching during drag-selection.
- **Robust Pattern Matching**: Includes fallback to case-insensitive substring matching for invalid regex entries.

## Version 3.2.4 Changelog:
- **Linkify: Code Block Support**: Enabled linkification within `<code>` and `<pre>` tags.
- **Aggressive Linkify Mode**: Added a new optional toggle to recognize prefix-less domains (e.g., `google.com`).
- **Enhanced Detection Engine**: Improved regex to support subdomains, deep paths, and complex query parameters for both standard and aggressive modes.
- **Dynamic Advanced UI**: Enhanced user experience by hiding Aggressive Linkify options when the main feature is disabled.
- **UI Organization**: Added a dedicated section heading for Linkify in Advanced Options for better future extensibility.
- **Expanded Testing**: Updated `test_links.html` with complex real-world URL scenarios and a dedicated section for "Potential False Positives".

## Version 3.2.3 Changelog:
- **New Feature: Linkify**: Automatically converts plain text URLs on web pages into clickable links.
- **Advanced Options Page**: Integrated experimental features into a dedicated "Advanced Options" settings page.
- **UI Refinement**: Cleaned up sidebar navigation by merging Global and Advanced options for a more intuitive settings experience.
- **Engine Optimization**: Added `js/linkify.js` with comprehensive URL regex matching and Shadow DOM support.

## Version 3.2.2 Changelog:
- **Major Popup UI Redesign**: Implemented a modern glassmorphism aesthetic with a dark premium theme.
- **Animated Components**: Added decorative floating background orbs and pulsing logo effects.
- **Enhanced Button Layout**: Replaced basic buttons with interactive cards featuring gradient icon boxes, titles, and subtitles.
- **Refined UX**: Improved visual hierarchy, smooth hover transitions, and dynamic success states for better interaction feedback.

## Version 2.0.9 Changelog:
- Centralized CSS architecture using a unified variable system (`variables.css`).
- Extracted inline styles from `popup.html` into a dedicated `popup.css` stylesheet.
- Standardized all design tokens (colors, fonts, gradients, shadows) for consistent branding.
- Improved codebase maintainability by removing hardcoded visual values.

## Version 2.0.8 Changelog:
- Redesigned the Action Modal UI with a modern, compact two-column layout and scrollable body.
- Implemented glassmorphism styling, premium gradients, and interactive collapsible sections.
- Improved iconography and fixed character encoding issues in the Options UI.
- Set "Smart Select" to off by default for new actions to improve initial user experience.
- Optimized CSS by removing redundant styles and fixing syntax errors.
- Synchronized saved action card left borders with their respective selection box colors.

## Version 2.0.7 Changelog:
- Implemented LinkClump-style Smart Select: dynamic filtering that switches to heading-only (H1-H6) mode when a heading link is touched.
- Split "Smart Select" into two independent features: "Smart Select (heading filter)" and "Avoid Duplicates".
- Updated Options UI with separate toggles for granular control over filtering and deduplication.

## Version 2.0.6 Changelog:
- Implemented Persistent Visited Link Marking.
- Added `js/visited.js` to track and visually mark links opened via Grabbit using `chrome.storage.local`.
- Bypassed browser limitations where redirect URLs (like Google Search) fail to show native `:visited` styling.
- Integrated `chrome.history` API to ensure opened links are correctly added to the browser's global history.

## Version 2.0.5 Changelog:
- Implemented robust Cross-Platform Key Recognition.
- Centralized OS detection in `js/utils.js` for Windows, macOS, and Linux.
- Improved ESC key handling: selection cancellation now works consistently and prevents default page behavior while Grabbit is active.
- Corrected key mapping for macOS (Command ⌘, Option ⌥, Shift ⇧) in Options UI and selection logic.

## Version 2.0.4 Changelog:
- Implemented Drag Threshold for selection activation.
- Selection box now waits for a 5-pixel drag before appearing, preventing accidental activation on simple clicks.
- Improved UX by removing visual flashes and zero-size selections on accidental triggers.

## Version 2.0.3 Changelog:
- Added Shadow DOM support for link detection.
- Links inside Shadow DOM components are now properly recognized and selectable.

## Version 2.0.2 Changelog:
- Modularized Settings into sections (Main, Popup, Advanced, Global).
- Created standalone Advanced Options page.
- Updated Sidebar component to include Advanced Options navigation.
- Implemented real-time section switching for all pages.
- Enforced absolute paths for extension resources.

## Version 2.0.1 Changelog:
- Refactor grabbit.js into smaller parts:
logic.js
ui.js
utils.js
state.js

## Version 2.0.0 Changelog:

- New Brand Logo
- New Brand Images in Chrome's Store
- New Sidebar UI
- New Options Page UI
- Added border thickness and style customization.

## Version 1.0.8 Changelog:
- Added "Copy all tab URLs" in popup.html
- Changed delay timer from 0 to 30 seconds with step 0.5
- Added advanced option 'Open tabs at the end of opened tabs' when 'Open links in new tabs' is selected
- Added custom options for "Copy Title & Urls" action

## Version 1.0.7 Changelog:
- Small fix for youtube subscriptions but still have work to do
- Fix reverse order bug
- Fixed too much debounce link delay
- Won't allow user to add duplicate actions with the same combination keys
- Added new action - Copy URL Titles

## Version 1.0.6 Changelog:
- fix memory leak for ESC by oaustegard
- debounce link selection by oaustegard

## Version 1.0.5 Changelog:
Added delay option when tabs are opened by TheTacoScott

## Version 1.0.4 Changelog:
- Open Links/tabs in reverse order option added
- Show correct combination keys for each OS (Option and Command for MacOs)

## Version 1.0.3 Changelog:

- Opens Tabs next to active tab
- Recognize <a> tags that are not visible

## Version 1.0.2 Changelog:

Added activeTab permission

## Version 1.0.1 Changelog:

Removed unused context menu permission
```

## File: `manifest.json`
```json
{
  "manifest_version": 3,
  "name": "Grabbit",
  "version": "3.8.4",
  "description": "Drag to open multiple links, copy URLs with formatting, or create bookmarks instantly. Premium: AI-powered product comparison.",
  "icons": {
    "16": "icons/icon16.png",
    "32": "icons/icon32.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  },
  "permissions": [
    "activeTab",
    "storage",
    "clipboardWrite",
    "clipboardRead",
    "tabs",
    "windows",
    "scripting"
  ],
  "host_permissions": [
    "<all_urls>",
    "https://grabbit.socratisp.com/*"
  ],
  "optional_permissions": [
    "bookmarks"
  ],
  "action": {
    "default_popup": "popup/popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "32": "icons/icon32.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "options_page": "options.html",
  "content_scripts": [
    {
      "matches": [
        "<all_urls>"
      ],
      "js": [
        "js/state.js",
        "js/utils.js",
        "js/ui.js",
        "js/visited.js",
        "js/smart-select.js",
        "js/logic.js",
        "js/linkify.js",
        "js/duplicate-highlighter.js",
        "js/grabbit.js"
      ],
      "all_frames": true,
      "run_at": "document_end"
    }
  ],
  "background": {
    "service_worker": "js/background.js",
    "type": "module"
  }
}
```

## File: `options.html`
```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Grabbit Options</title>
    <link rel="stylesheet" href="/css/variables.css">
    <link rel="stylesheet" href="/css/components/sidebar.css">
    <link rel="stylesheet" href="/css/options.css">
    <link rel="stylesheet" href="/css/components/footer.css">
</head>

<body>
    <div id="sidebar-placeholder"></div>
    <div class="container">
        <div id="main-options">
            <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 2rem;">
                <img src="icons/icon128.png" alt="Grabbit Logo" style="width: 64px; height: 64px;">
                <h1 style="margin: 0;">Grabbit Settings</h1>
            </div>

            <div class="card rate-card">
                <div class="rate-content">
                    <h3>Enjoying Grabbit?</h3>
                    <p>Your 5-star rating helps others discover this extension!</p>
                    <button id="rateExtensionButton" class="rate-extension-button">
                        <span class="star-icons">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
                        Rate on Chrome Web Store
                    </button>
                    <button id="reportIssueButton" class="rate-extension-button">
                        <span class="star-icons">&#128172;</span>
                        Report an Issue
                    </button>
                </div>
            </div>




            <div class="card instructions-container">
                <div class="instructions-split">
                    <div class="instructions-panel">
                        <h2>How to Use Grabbit</h2>
                        <ul class="instructions-list">
                            <li>Click the "Add New Action" button</li>
                            <li>Configure your activation keys</li>
                            <li>Choose a color for your action</li>
                            <li>Determine the action to perform</li>
                            <li>Toggle smart select on or off</li>
                            <li>Press "Save" to apply changes</li>
                            <li>Use activation keys and mouse to start selecting links</li>
                        </ul>
                    </div>

                    <div class="instructions-panel">
                        <h2>How to Use Grabbit Popup</h2>
                        <ul class="instructions-list">
                            <li>
                                <button id="pinExtensionButton" class="pin-button">
                                    Pin Extension to Toolbar
                                </button>
                            </li>
                            <li>Select Multiple Tabs (Ctrl or Shift + Click)</li>
                            <li>Click extension icon to open popup</li>
                            <li>Use "Copy Selected Tab URLs" to copy links</li>
                            <li>Use "Open Copied Links" to open copied URLs in new tabs</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div id="savedActions">
                <!-- Saved actions will be displayed here -->
            </div>

            <div class="card">
                <button class="action-button">
                    Add New Action
                </button>
            </div>
        </div>

        <div id="footer-placeholder"></div>
    </div>

    <!-- Modal -->
    <div class="modal" id="actionModal">
        <div class="modal-content">
            <!-- Modal Header -->
            <div class="modal-header">
                <h2 id="modalTitle">Create New Action</h2>
                <button class="modal-close">&times;</button>
            </div>

            <!-- Modal Body - Scrollable -->
            <div class="modal-body">
                <!-- Activation Section -->
                <div class="modal-section">
                    <div class="section-header">
                        <span class="section-icon">&#9889;</span>
                        <h3>Activation</h3>
                        <span class="section-badge required-badge">Required</span>
                    </div>
                    <p class="section-description">Configure how to trigger this action</p>

                    <div class="two-column-grid">
                        <div class="input-group compact">
                            <label>Mouse button</label>
                            <select class="key-select required" id="mouseButton" required>
                                <option value="">Select...</option>
                                <option value="left">Left Click</option>
                                <option value="right">Right Click</option>
                                <option value="middle">Middle Click</option>
                            </select>
                        </div>
                        <div class="input-group compact">
                            <label>+ Modifier Key</label>
                            <select class="key-select" id="combinedKey">
                                <option value="none">None</option>
                                <optgroup label="Modifier Keys">
                                    <option value="ctrl">Ctrl</option>
                                    <option value="shift">Shift</option>
                                    <option value="alt">Alt</option>
                                </optgroup>
                                <optgroup label="Letter Keys">
                                    <option value="a">A</option>
                                    <option value="b">B</option>
                                    <option value="c">C</option>
                                    <option value="d">D</option>
                                    <option value="e">E</option>
                                    <option value="f">F</option>
                                    <option value="g">G</option>
                                    <option value="h">H</option>
                                    <option value="i">I</option>
                                    <option value="j">J</option>
                                    <option value="k">K</option>
                                    <option value="l">L</option>
                                    <option value="m">M</option>
                                    <option value="n">N</option>
                                    <option value="o">O</option>
                                    <option value="p">P</option>
                                    <option value="q">Q</option>
                                    <option value="r">R</option>
                                    <option value="s">S</option>
                                    <option value="t">T</option>
                                    <option value="u">U</option>
                                    <option value="v">V</option>
                                    <option value="w">W</option>
                                    <option value="x">X</option>
                                    <option value="y">Y</option>
                                    <option value="z">Z</option>
                                </optgroup>
                            </select>
                        </div>
                        <div class="input-group compact">
                            <label>Box color</label>
                            <input type="color" class="color-picker" id="boxColor" value="#2196F3">
                        </div>
                        <div class="input-group compact">
                            <label>Border</label>
                            <div class="inline-inputs">
                                <input type="number" class="key-select small-input" id="borderThickness" min="1"
                                    max="10" value="2" title="Thickness (px)">
                                <select class="key-select" id="borderStyle">
                                    <option value="solid">Solid</option>
                                    <option value="dashed">Dashed</option>
                                    <option value="dotted">Dotted</option>
                                    <option value="double">Double</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="error-message" id="mouseButtonError">Please select a mouse button</div>
                    <div class="error-message" id="combinationError">This key and mouse combination is already in use!
                    </div>
                    <div class="warning-message" id="letterKeyWarning">
                        <span class="warning-icon">⚠️</span> Letter keys may not work correctly with laptop trackpads.
                        Consider using Ctrl, Shift, or Alt instead.
                    </div>
                </div>

                <!-- Action Section -->
                <div class="modal-section">
                    <div class="section-header">
                        <span class="section-icon">&#127919;</span>
                        <h3>Action</h3>
                        <span class="section-badge required-badge">Required</span>
                    </div>
                    <div class="input-group">
                        <label>This action should...</label>
                        <select class="key-select required" id="actionType" required>
                            <option value="">Select Action Type</option>
                            <option value="openLinks">Open links in new tabs</option>
                            <option value="openWindow">Open links in a new window</option>
                            <option value="copyUrls">Copy URLs to clipboard</option>
                            <option value="copyUrlsAndTitles">Copy URLs with page titles</option>
                            <option value="copyTitles">Copy page titles only</option>
                            <option value="createBookmarks">Create Bookmarks</option>
                        </select>
                    </div>
                    <div class="error-message" id="actionTypeError">Please select an action type</div>
                </div>

                <!-- Format Options Section (conditionally shown) -->
                <div class="modal-section" id="formatOptionsContainer" style="display: none;">
                    <div class="section-header">
                        <span class="section-icon">&#128221;</span>
                        <h3>Format Options</h3>
                        <span class="section-badge optional-badge">Optional</span>
                    </div>
                    <p class="section-description">Customize how URLs and titles are formatted</p>

                    <div class="two-column-grid">
                        <div class="input-group compact">
                            <label>Format pattern</label>
                            <select class="key-select" id="formatPattern">
                                <option value="titleFirst">Title → URL</option>
                                <option value="urlFirst">URL → Title</option>
                                <option value="markdown">Markdown [Title](URL)</option>
                                <option value="json">JSON [{"title":"...","url":"..."}]</option>
                            </select>
                        </div>
                        <div class="input-group compact">
                            <label>Separator type</label>
                            <select class="key-select" id="separatorType">
                                <option value="newline">New line</option>
                                <option value="space">Space</option>
                                <option value="tab">Tab (Excel)</option>
                                <option value="comma">Comma (,)</option>
                                <option value="dot">Dot (.)</option>
                            </select>
                        </div>
                        <div class="input-group compact">
                            <label>Separator count</label>
                            <input type="number" id="separatorCount" class="key-select" min="1" max="10" value="1">
                        </div>
                        <div class="input-group compact">
                            <label>Lines between links</label>
                            <input type="number" id="linkSeparatorCount" class="key-select" min="0" max="10" value="0">
                        </div>
                    </div>

                    <!-- Format Preview -->
                    <div class="format-preview-container">
                        <label class="preview-label">Preview</label>
                        <div class="format-preview" id="formatPreview">
                            <!-- Preview will be generated by JavaScript -->
                        </div>
                    </div>
                </div>

                <!-- Advanced Options Section - Collapsible -->
                <div class="modal-section collapsible-section">
                    <div class="collapsible-header" id="advancedOptionsToggle">
                        <div class="section-header">
                            <span class="section-icon">&#9881;</span>
                            <h3>Advanced Options</h3>
                            <span class="section-badge optional-badge">Optional</span>
                        </div>
                        <span class="collapse-icon">&#9660;</span>
                    </div>
                    <div class="collapsible-content" id="advancedOptionsContent">
                        <div class="advanced-grid">
                            <div class="advanced-option-row">
                                <div class="option-info">
                                    <label>Smart select (heading filter)</label>
                                    <div class="smart-select-info">
                                        <div class="tooltip">When enabled, if your selection touches a main title or
                                            heading link, only similar important links will be selected — ignoring
                                            navigation menus, footers, and other clutter.</div>
                                    </div>
                                </div>
                                <label class="toggle-switch">
                                    <input type="checkbox" id="smartSelect">
                                    <span class="toggle-slider"></span>
                                </label>
                            </div>

                            <div class="advanced-option-row">
                                <div class="option-info">
                                    <label>Avoid duplicates</label>
                                    <div class="smart-select-info">
                                        <div class="tooltip">Removes duplicate URLs when selecting multiple links.</div>
                                    </div>
                                </div>
                                <label class="toggle-switch">
                                    <input type="checkbox" id="avoidDuplicates" checked>
                                    <span class="toggle-slider"></span>
                                </label>
                            </div>

                            <div class="advanced-option-row">
                                <div class="option-info">
                                    <label>Reverse order</label>
                                    <div class="smart-select-info">
                                        <div class="tooltip">Open/copy links in reverse order of selection.</div>
                                    </div>
                                </div>
                                <label class="toggle-switch">
                                    <input type="checkbox" id="reverseOrder">
                                    <span class="toggle-slider"></span>
                                </label>
                            </div>

                            <div class="advanced-option-row">
                                <div class="option-info">
                                    <label>Mark links as visited</label>
                                    <div class="smart-select-info">
                                        <div class="tooltip">Visually mark processed links as visited (purple) in the browser.</div>
                                    </div>
                                </div>
                                <label class="toggle-switch">
                                    <input type="checkbox" id="markVisited">
                                    <span class="toggle-slider"></span>
                                </label>
                            </div>

                            <div class="advanced-option-row" id="openAtEndContainer">
                                <div class="option-info">
                                    <label>Open at end of tabs</label>
                                    <div class="smart-select-info">
                                        <div class="tooltip">New tabs open at the end of all tabs instead of after the
                                            current tab.</div>
                                    </div>
                                </div>
                                <label class="toggle-switch">
                                    <input type="checkbox" id="openAtEnd">
                                    <span class="toggle-slider"></span>
                                </label>
                            </div>

                            <div class="advanced-option-row" id="delayOptionContainer">
                                <div class="option-info">
                                    <label>Tab delay</label>
                                    <div class="smart-select-info">
                                        <div class="tooltip">Delay between opening each tab (seconds).</div>
                                    </div>
                                </div>
                                <div class="delay-control">
                                    <input type="range" id="tabDelay" min="0" max="30" value="0" step="0.5">
                                    <span id="delayValue">0s</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Modal Footer -->
            <div class="modal-footer">
                <button class="modal-button cancel-button" id="cancelButton">Cancel</button>
                <button class="modal-button save-button" id="saveButton">Save Action</button>
            </div>
        </div>
    </div>

    <script src="js/components/sidebar.js"></script>
    <script src="js/components/footer.js"></script>
    <script src="js/utils.js"></script>
    <script type="module" src="js/options/main.js"></script>

</body>

</html>
```

## File: `AI Features/compare/compare.css`
```css
/* =========================================================================
   Shopping Comparison - Friendly & Human-Centered Design
   ========================================================================= */

:root {
    /* Warm, friendly color palette */
    --color-bg: #f8f9fc;
    --color-surface: #ffffff;
    --color-surface-alt: #f1f3f8;

    /* Friendly blues */
    --color-primary: #3b82f6;
    --color-primary-dark: #2563eb;
    --color-primary-light: #eff6ff;

    /* Warm accents */
    --color-accent: #8b5cf6;
    --color-success: #10b981;
    --color-success-light: #d1fae5;

    /* Text colors */
    --color-text: #1e293b;
    --color-text-muted: #64748b;
    --color-text-light: #94a3b8;

    /* Borders */
    --color-border: #e2e8f0;
    --color-border-light: #f1f5f9;

    /* Spacing */
    --spacing-xs: 0.5rem;
    --spacing-sm: 0.75rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
    --spacing-2xl: 3rem;

    /* Radius */
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-full: 9999px;

    /* Shadows */
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
}

/* === Reset & Base === */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: var(--color-bg);
    color: var(--color-text);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    min-height: 100vh;
}

/* === Layout === */
.page-wrapper {
    max-width: 900px;
    margin: 0 auto;
    padding: var(--spacing-lg) var(--spacing-md);
}

/* === Header === */
.header {
    margin-bottom: var(--spacing-2xl);
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: var(--spacing-lg);
    border-bottom: 2px solid var(--color-border);
}

.logo {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    font-size: 1.125rem;
    font-weight: 700;
    color: var(--color-text);
}

.logo img {
    display: block;
    width: 24px;
    height: 24px;
}

.close-link {
    color: var(--color-text-muted);
    text-decoration: none;
    font-size: 0.9375rem;
    font-weight: 500;
    padding: var(--spacing-xs) var(--spacing-md);
    border-radius: var(--radius-sm);
    transition: all 0.2s;
}

.close-link:hover {
    background-color: var(--color-surface-alt);
    color: var(--color-text);
}

.header-actions {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
}

.customize-link {
    display: flex;
    align-items: center;
    gap: var(--spacing-xs);
    color: var(--color-text-muted);
    text-decoration: none;
    font-size: 0.875rem;
    font-weight: 500;
    padding: var(--spacing-xs) var(--spacing-sm);
    border-radius: var(--radius-sm);
    transition: all 0.2s;
}

.customize-link:hover {
    background-color: var(--color-surface-alt);
    color: var(--color-primary);
}

.customize-link svg {
    display: block;
    width: 16px;
    height: 16px;
}

.header-divider {
    width: 1px;
    height: 16px;
    background-color: var(--color-border);
}

/* === Loading State === */
.loading-state {
    text-align: center;
    padding: var(--spacing-2xl) var(--spacing-md);
    max-width: 400px;
    margin: var(--spacing-2xl) auto;
}

.loading-animation {
    margin-bottom: var(--spacing-xl);
}

.pulse-dots {
    display: inline-flex;
    gap: var(--spacing-sm);
}

.pulse-dots span {
    width: 12px;
    height: 12px;
    background-color: var(--color-primary);
    border-radius: var(--radius-full);
    animation: pulse 1.4s ease-in-out infinite;
}

.pulse-dots span:nth-child(2) {
    animation-delay: 0.2s;
}

.pulse-dots span:nth-child(3) {
    animation-delay: 0.4s;
}

@keyframes pulse {
    0%, 80%, 100% {
        transform: scale(0.8);
        opacity: 0.5;
    }
    40% {
        transform: scale(1);
        opacity: 1;
    }
}

.loading-state h2 {
    font-size: 1.375rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: var(--spacing-sm);
}

.loading-subtitle {
    color: var(--color-text-muted);
    font-size: 0.9375rem;
}

/* === Error State === */
.error-state {
    text-align: center;
    padding: var(--spacing-2xl) var(--spacing-md);
    background: var(--color-surface);
    border-radius: var(--radius-lg);
    border: 1px solid var(--color-border);
    max-width: 480px;
    margin: var(--spacing-2xl) auto;
    box-shadow: var(--shadow-md);
}

.error-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 56px;
    height: 56px;
    background-color: var(--color-surface-alt);
    border-radius: var(--radius-full);
    color: var(--color-text-muted);
    margin-bottom: var(--spacing-lg);
}

.error-state h3 {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: var(--spacing-sm);
}

.error-message {
    color: var(--color-text-muted);
    font-size: 0.9375rem;
    margin-bottom: var(--spacing-xl);
    line-height: 1.6;
}

/* === Results State === */
.results-state {
    animation: fadeIn 0.4s ease-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(8px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* === Top Pick Banner === */
.top-pick-banner {
    background: linear-gradient(135deg, var(--color-primary-light) 0%, var(--color-surface) 100%);
    border: 1px solid var(--color-primary-light);
    border-radius: var(--radius-lg);
    padding: var(--spacing-xl) var(--spacing-lg);
    margin-bottom: var(--spacing-xl);
    box-shadow: var(--shadow-md);
    position: relative;
    overflow: hidden;
}

.top-pick-banner::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 200px;
    height: 200px;
    background: radial-gradient(circle, rgba(59, 130, 246, 0.08) 0%, transparent 70%);
    border-radius: 50%;
    transform: translate(30%, -30%);
}

.top-pick-content {
    position: relative;
    display: flex;
    gap: var(--spacing-md);
    align-items: flex-start;
}

.top-pick-badge {
    display: inline-flex;
    align-items: center;
    gap: var(--spacing-xs);
    background-color: var(--color-primary);
    color: white;
    font-size: 0.8125rem;
    font-weight: 600;
    padding: var(--spacing-xs) var(--spacing-sm);
    border-radius: var(--radius-sm);
    white-space: nowrap;
}

.top-pick-info h2 {
    font-size: 1.625rem;
    font-weight: 700;
    color: var(--color-text);
    margin-bottom: var(--spacing-sm);
    line-height: 1.3;
}

.top-pick-reason {
    color: var(--color-text-muted);
    font-size: 1rem;
    line-height: 1.6;
}

/* === Summary Section === */
.summary-section {
    background-color: var(--color-surface);
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    margin-bottom: var(--spacing-xl);
    border: 1px solid var(--color-border);
    box-shadow: var(--shadow-sm);
}

.summary-section h3 {
    font-size: 1.0625rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: var(--spacing-md);
}

.summary-text {
    color: var(--color-text-muted);
    font-size: 0.9375rem;
    line-height: 1.7;
}

/* === Section Headings === */
.section-heading {
    font-size: 1.0625rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: var(--spacing-lg);
    margin-top: var(--spacing-xl);
}

.section-heading:first-of-type {
    margin-top: 0;
}

/* === Products Grid === */
.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: var(--spacing-md);
    margin-bottom: var(--spacing-xl);
}

.product-card {
    background-color: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    cursor: pointer;
    transition: all 0.2s ease;
    position: relative;
    display: flex;
    flex-direction: column;
}

.product-card:hover {
    transform: translateY(-2px);
    border-color: var(--color-primary);
    box-shadow: var(--shadow-md);
}

.product-card.is-top-pick {
    border-color: var(--color-primary);
    background-color: var(--color-primary-light);
    box-shadow: var(--shadow-md);
}

.p-header {
    margin-bottom: var(--spacing-md);
}

.p-name {
    font-weight: 700;
    font-size: 1rem;
    color: var(--color-text);
    margin-bottom: var(--spacing-xs);
    line-height: 1.4;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.p-price {
    color: var(--color-primary);
    font-weight: 600;
    font-size: 0.9375rem;
}

.p-rating {
    display: inline-flex;
    align-items: center;
    gap: var(--spacing-xs);
    font-size: 0.8125rem;
    color: var(--color-text-muted);
    margin-top: var(--spacing-xs);
}

.p-rating svg {
    width: 14px;
    height: 14px;
    color: #fbbf24;
}

.p-score-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: var(--spacing-xs);
    font-size: 0.8125rem;
}

.p-score-label {
    color: var(--color-text-muted);
    font-weight: 500;
}

.p-score-value {
    color: var(--color-primary);
    font-weight: 700;
    font-size: 0.875rem;
}

.p-score-bar {
    height: 6px;
    background-color: var(--color-surface-alt);
    border-radius: var(--radius-full);
    margin-bottom: var(--spacing-md);
    overflow: hidden;
}

.p-score-fill {
    height: 100%;
    background-color: var(--color-primary);
    border-radius: var(--radius-full);
    transition: width 0.6s ease;
}

.is-top-pick .p-score-fill {
    background-color: var(--color-accent);
}

.p-lists {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--spacing-md);
    font-size: 0.8125rem;
    margin-bottom: var(--spacing-md);
}

.p-list h4 {
    font-size: 0.6875rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--color-text-light);
    margin-bottom: var(--spacing-sm);
    font-weight: 700;
}

.p-list ul {
    list-style: none;
}

.p-list li {
    margin-bottom: var(--spacing-xs);
    padding-left: 1.25rem;
    position: relative;
    color: var(--color-text-muted);
    line-height: 1.5;
}

.p-pros li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 6px;
    width: 14px;
    height: 14px;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2310b981' stroke-width='3'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E");
    background-size: contain;
    background-repeat: no-repeat;
}

.p-cons li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 5px;
    width: 14px;
    height: 14px;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23ef4444' stroke-width='3'%3E%3Cline x1='18' y1='6' x2='6' y2='18'%3E%3C/line%3E%3Cline x1='6' y1='6' x2='18' y2='18'%3E%3C/line%3E%3C/svg%3E");
    background-size: contain;
    background-repeat: no-repeat;
}

.p-best-for {
    padding-top: var(--spacing-md);
    border-top: 1px solid var(--color-border-light);
    font-size: 0.8125rem;
    color: var(--color-text-muted);
}

.p-best-for strong {
    color: var(--color-text);
}

/* === Comparison Table === */
.comparison-section {
    margin-bottom: var(--spacing-xl);
}

.comparison-table-wrapper {
    background-color: var(--color-surface);
    border-radius: var(--radius-lg);
    border: 1px solid var(--color-border);
    overflow-x: auto;
    box-shadow: var(--shadow-sm);
}

.comparison-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.875rem;
}

.comparison-table th,
.comparison-table td {
    padding: var(--spacing-md) var(--spacing-lg);
    text-align: left;
    border-bottom: 1px solid var(--color-border-light);
}

.comparison-table th {
    background-color: var(--color-surface-alt);
    font-weight: 600;
    color: var(--color-text);
    white-space: nowrap;
}

.comparison-table td {
    color: var(--color-text-muted);
}

.comparison-table td:first-child {
    font-weight: 500;
    color: var(--color-text);
}

.comparison-table tr:last-child td {
    border-bottom: none;
}

/* === Bottom Line Section === */
.bottom-line-section {
    background-color: var(--color-surface);
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    margin-bottom: var(--spacing-xl);
    border: 1px solid var(--color-border);
    box-shadow: var(--shadow-sm);
}

.bottom-line-section h3 {
    font-size: 1.0625rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: var(--spacing-md);
}

.bottom-line-text {
    color: var(--color-text-muted);
    font-size: 0.9375rem;
    line-height: 1.7;
}

/* === Actions Bar === */
.actions-bar {
    display: flex;
    justify-content: center;
    gap: var(--spacing-md);
    margin-top: var(--spacing-2xl);
    padding-top: var(--spacing-lg);
    border-top: 1px solid var(--color-border);
}

/* === Buttons === */
button {
    font-family: inherit;
    font-size: 0.9375rem;
    font-weight: 500;
    padding: var(--spacing-sm) var(--spacing-lg);
    border-radius: var(--radius-md);
    border: none;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: var(--spacing-xs);
}

.btn-primary {
    background-color: var(--color-primary);
    color: white;
    box-shadow: var(--shadow-sm);
}

.btn-primary:hover {
    background-color: var(--color-primary-dark);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.btn-primary:active {
    transform: translateY(0);
}

.btn-secondary {
    background-color: var(--color-surface);
    color: var(--color-text);
    border: 1px solid var(--color-border);
}

.btn-secondary:hover {
    background-color: var(--color-surface-alt);
    border-color: var(--color-text-muted);
}

/* === Utilities === */
.hidden {
    display: none !important;
}

/* === Responsive === */
@media (max-width: 640px) {
    .page-wrapper {
        padding: var(--spacing-md);
    }

    .top-pick-content {
        flex-direction: column;
        gap: var(--spacing-sm);
    }

    .top-pick-banner {
        padding: var(--spacing-lg);
    }

    .top-pick-info h2 {
        font-size: 1.375rem;
    }

    .products-grid {
        grid-template-columns: 1fr;
    }

    .actions-bar {
        flex-direction: column;
    }

    .actions-bar button {
        width: 100%;
    }
}
```

## File: `AI Features/compare/compare.html`
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopping Comparison | Grabbit</title>
    <link rel="stylesheet" href="compare.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>

<body>

    <div class="page-wrapper">
        <!-- Header -->
        <header class="header">
            <div class="header-content">
                <div class="logo">
                    <img src="../../icons/icon48.png" alt="Grabbit" width="24" height="24">
                    <span>Grabbit</span>
                </div>
                <div class="header-actions">
                    <a href="#" class="close-link" id="close-btn">Done</a>
                </div>
            </div>
        </header>

        <!-- Loading State -->
        <div id="loading-state" class="loading-state">
            <div class="loading-animation">
                <div class="pulse-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
            <h2>Looking at your options...</h2>
            <p class="loading-subtitle">This will just take a moment</p>
        </div>

        <!-- Error State -->
        <div id="error-state" class="error-state hidden">
            <div class="error-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="8" x2="12" y2="12"></line>
                    <line x1="12" y1="16" x2="12.01" y2="16"></line>
                </svg>
            </div>
            <h3>Oops, something went wrong</h3>
            <p id="error-message" class="error-message">Please try again</p>
            <button id="retry-btn" class="btn-primary">Try Again</button>
        </div>

        <!-- Results State -->
        <div id="results-state" class="results-state hidden">

            <!-- Top Pick Banner -->
            <div class="top-pick-banner">
                <div class="top-pick-content">
                    <div class="top-pick-badge">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                            <path
                                d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
                        </svg>
                        Top Pick
                    </div>
                    <div class="top-pick-info">
                        <h2 id="top-pick-name">Finding the best option...</h2>
                        <p id="top-pick-reason">Analyzing what makes this one special</p>
                    </div>
                </div>
            </div>

            <!-- Quick Summary -->
            <div class="summary-section">
                <h3>Here's what matters</h3>
                <p id="summary-text" class="summary-text">Looking at the details for you...</p>
            </div>

            <!-- Products -->
            <h3 class="section-heading">Your Options</h3>
            <div id="products-grid" class="products-grid">
                <!-- Cards injected via JS -->
            </div>

            <!-- Feature Comparison -->
            <div class="comparison-section">
                <h3 class="section-heading">Side by side</h3>
                <div class="comparison-table-wrapper">
                    <table id="comparison-table" class="comparison-table">
                        <thead>
                            <tr id="table-header"></tr>
                        </thead>
                        <tbody id="table-body"></tbody>
                    </table>
                </div>
            </div>

            <!-- Bottom Line -->
            <div class="bottom-line-section">
                <h3>The Bottom Line</h3>
                <p id="verdict-text" class="bottom-line-text">...</p>
            </div>

            <!-- Actions -->
            <div class="actions-bar">
                <button id="open-top-pick" class="btn-primary">Open Top Pick</button>
                <button id="copy-summary" class="btn-secondary">Copy Summary</button>
            </div>

        </div>
    </div>

    <script src="compare.js"></script>
</body>

</html>
```

## File: `AI Features/compare/compare.js`
```javascript
/**
 * Shopping Comparison Page
 * Friendly, human-centered product comparison
 */

// State
let comparisonData = null;
let selectedTabs = [];

// DOM Elements
const loadingState = document.getElementById('loading-state');
const errorState = document.getElementById('error-state');
const resultsState = document.getElementById('results-state');

/**
 * Initialize the comparison page
 */
async function init() {
    // Get the tabs data from storage
    const stored = await chrome.storage.local.get(['pendingComparison']);

    if (!stored.pendingComparison || !stored.pendingComparison.tabs?.length) {
        showError('No products to compare. Please select tabs from the popup.');
        return;
    }

    selectedTabs = stored.pendingComparison.tabs;

    // Clear the pending comparison
    await chrome.storage.local.remove(['pendingComparison']);

    // Start the comparison
    runComparison();
}

/**
 * Run the comparison
 */
async function runComparison() {
    showLoading();

    try {
        // Add a small delay for visual smoothness
        await delay(600);

        // Send comparison request to background
        const response = await chrome.runtime.sendMessage({
            action: 'compareProducts',
            tabs: selectedTabs
        });

        if (response.error) {
            // Handle different error types
            if (response.error === 'Premium required') {
                chrome.runtime.sendMessage({ action: 'openPaymentPage' });
                showError('Premium subscription required. Opening payment page...');
                return;
            }

            if (response.error.includes('Subscription not active') ||
                response.error.includes('subscription')) {
                showError('Your subscription is not active. Please check your payment.');
                setTimeout(() => {
                    chrome.runtime.sendMessage({ action: 'openPaymentPage' });
                }, 2000);
                return;
            }

            if (response.error.includes('Monthly limit') ||
                response.error.includes('limit reached')) {
                showError('Monthly comparison limit reached. Try again next month!');
                return;
            }

            throw new Error(response.error);
        }

        comparisonData = response.results;

        // Show quota if available
        if (comparisonData._remaining !== undefined) {
            const actionsBar = document.querySelector('.actions-bar');
            if (actionsBar) {
                // Remove existing if present
                const existing = document.getElementById('quota-display');
                if (existing) existing.remove();

                const quotaEl = document.createElement('div');
                quotaEl.id = 'quota-display';
                quotaEl.style.cssText = 'width: 100%; text-align: center; font-size: 0.8125rem; color: var(--color-text-muted); margin-top: 1rem; opacity: 0.8;';
                quotaEl.textContent = `AI calls remaining this month: ${comparisonData._remaining}`;

                actionsBar.insertAdjacentElement('afterend', quotaEl);
            }
        }

        renderResults(comparisonData);
        showResults();

    } catch (error) {
        console.error('Comparison failed:', error);
        showError(error.message);
    }
}

/**
 * Show loading state
 */
function showLoading() {
    loadingState.classList.remove('hidden');
    errorState.classList.add('hidden');
    resultsState.classList.add('hidden');
}

/**
 * Show error state
 */
function showError(message) {
    loadingState.classList.add('hidden');
    errorState.classList.remove('hidden');
    resultsState.classList.add('hidden');
    document.getElementById('error-message').textContent = message;
}

/**
 * Show results state
 */
function showResults() {
    loadingState.classList.add('hidden');
    errorState.classList.add('hidden');
    resultsState.classList.remove('hidden');
}

/**
 * Render comparison results
 */
function renderResults(data) {
    // Top Pick Banner
    const topProduct = data.products[data.winner];
    document.getElementById('top-pick-name').textContent = topProduct?.name || 'Best Choice';
    document.getElementById('top-pick-reason').textContent = data.winnerReason || '';

    // Summary
    document.getElementById('summary-text').textContent = data.summary || '';

    // Products Grid
    const productsGrid = document.getElementById('products-grid');
    productsGrid.innerHTML = '';

    data.products.forEach((product, index) => {
        const isTopPick = index === data.winner;
        const card = document.createElement('div');
        card.className = `product-card ${isTopPick ? 'is-top-pick' : ''}`;
        card.dataset.url = selectedTabs[index]?.url || '';

        // Build the card HTML
        card.innerHTML = `
            ${isTopPick ? `
                <div style="position: absolute; top: 1rem; right: 1rem; background: var(--color-primary); color: white; font-size: 0.6875rem; font-weight: 700; padding: 0.25rem 0.5rem; border-radius: var(--radius-sm); letter-spacing: 0.05em;">
                    TOP PICK
                </div>
            ` : ''}
            <div class="p-header">
                <div class="p-name">${escapeHtml(product.name)}</div>
                <div class="p-price">${escapeHtml(product.price || 'Price N/A')}</div>
                ${product.rating ? `
                    <div class="p-rating">
                        <svg viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                        </svg>
                        ${escapeHtml(product.rating)}
                    </div>
                ` : ''}
            </div>

            <div class="p-score-row">
                <span class="p-score-label">Our Score</span>
                <span class="p-score-value">${(product.score || 0).toFixed(1)}<span style="color:var(--color-text-muted); font-size:0.75rem; font-weight:400;">/10</span></span>
            </div>
            <div class="p-score-bar">
                <div class="p-score-fill" style="width: ${((product.score || 0) / 10) * 100}%"></div>
            </div>

            <div class="p-lists">
                <div class="p-list p-pros">
                    <h4>Why you'll like it</h4>
                    <ul>
                        ${(product.pros || []).map(p => `<li>${escapeHtml(p)}</li>`).join('')}
                    </ul>
                </div>
                <div class="p-list p-cons">
                    <h4>Things to know</h4>
                    <ul>
                        ${(product.cons || []).map(c => `<li>${escapeHtml(c)}</li>`).join('')}
                    </ul>
                </div>
            </div>

            <div class="p-best-for">
                <strong>Great for:</strong> ${escapeHtml(product.bestFor || 'Everyday use')}
            </div>
        `;

        // Click to open product
        card.addEventListener('click', () => {
            if (card.dataset.url) {
                chrome.tabs.create({ url: card.dataset.url });
            }
        });

        productsGrid.appendChild(card);
    });

    // Feature Table
    const tableHeader = document.getElementById('table-header');
    const tableBody = document.getElementById('table-body');

    tableHeader.innerHTML = '<th>Feature</th>' +
        data.products.map(p => `<th>${escapeHtml(p.name.substring(0, 25))}${p.name.length > 25 ? '…' : ''}</th>`).join('');

    tableBody.innerHTML = '';
    (data.features || []).forEach(feature => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${escapeHtml(feature.label)}</td>` +
            (feature.values || []).map(v => `<td>${escapeHtml(v)}</td>`).join('');
        tableBody.appendChild(row);
    });

    // Bottom Line
    document.getElementById('verdict-text').textContent = data.verdict || '';
}

/**
 * Helper: Escape HTML
 */
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Helper: Delay
 */
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Event Listeners
document.getElementById('close-btn').addEventListener('click', (e) => {
    e.preventDefault();
    window.close();
});

document.getElementById('retry-btn').addEventListener('click', () => {
    if (selectedTabs.length) {
        runComparison();
    } else {
        window.close();
    }
});

document.getElementById('copy-summary').addEventListener('click', async () => {
    if (comparisonData) {
        const text = `${comparisonData.summary}\n\nTop Pick: ${comparisonData.products[comparisonData.winner]?.name}\n\n${comparisonData.verdict}`;
        await navigator.clipboard.writeText(text);

        const btn = document.getElementById('copy-summary');
        const originalText = btn.textContent;
        btn.textContent = 'Copied!';
        setTimeout(() => btn.textContent = originalText, 2000);
    }
});

document.getElementById('open-top-pick').addEventListener('click', () => {
    if (comparisonData && selectedTabs[comparisonData.winner]) {
        chrome.tabs.create({ url: selectedTabs[comparisonData.winner].url });
    }
});

// Initialize
init();
```

## File: `AI Features/summarize/summarize.css`
```css
/* =========================================================================
   Article Summary - Friendly & Human-Centered Design
   ========================================================================= */

:root {
    /* Warm, friendly color palette */
    --color-bg: #f8f9fc;
    --color-surface: #ffffff;
    --color-surface-alt: #f1f3f8;

    /* Friendly blues and purples */
    --color-primary: #3b82f6;
    --color-primary-dark: #2563eb;
    --color-primary-light: #eff6ff;

    /* Warm accents */
    --color-accent: #8b5cf6;
    --color-success: #10b981;
    --color-success-light: #d1fae5;

    /* Text colors */
    --color-text: #1e293b;
    --color-text-muted: #64748b;
    --color-text-light: #94a3b8;

    /* Borders */
    --color-border: #e2e8f0;
    --color-border-light: #f1f5f9;

    /* Spacing */
    --spacing-xs: 0.5rem;
    --spacing-sm: 0.75rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
    --spacing-2xl: 3rem;

    /* Radius */
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-full: 9999px;

    /* Shadows */
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
}

/* === Reset & Base === */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: var(--color-bg);
    color: var(--color-text);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    min-height: 100vh;
}

/* === Layout === */
.page-wrapper {
    max-width: 800px;
    margin: 0 auto;
    padding: var(--spacing-lg) var(--spacing-md);
}

/* === Header === */
.header {
    margin-bottom: var(--spacing-2xl);
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: var(--spacing-lg);
    border-bottom: 2px solid var(--color-border);
}

.logo {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
    font-size: 1.125rem;
    font-weight: 700;
    color: var(--color-text);
}

.logo img {
    display: block;
    width: 24px;
    height: 24px;
}

.close-link {
    color: var(--color-text-muted);
    text-decoration: none;
    font-size: 0.9375rem;
    font-weight: 500;
    padding: var(--spacing-xs) var(--spacing-md);
    border-radius: var(--radius-sm);
    transition: all 0.2s;
}

.close-link:hover {
    background-color: var(--color-surface-alt);
    color: var(--color-text);
}

.header-actions {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
}

.customize-link {
    display: flex;
    align-items: center;
    gap: var(--spacing-xs);
    color: var(--color-text-muted);
    text-decoration: none;
    font-size: 0.875rem;
    font-weight: 500;
    padding: var(--spacing-xs) var(--spacing-sm);
    border-radius: var(--radius-sm);
    transition: all 0.2s;
}

.customize-link:hover {
    background-color: var(--color-surface-alt);
    color: var(--color-primary);
}

.customize-link svg {
    display: block;
    width: 16px;
    height: 16px;
}

.header-divider {
    width: 1px;
    height: 16px;
    background-color: var(--color-border);
}

/* === Loading State === */
.loading-state {
    text-align: center;
    padding: var(--spacing-2xl) var(--spacing-md);
    max-width: 400px;
    margin: var(--spacing-2xl) auto;
}

.loading-animation {
    margin-bottom: var(--spacing-xl);
}

.pulse-dots {
    display: inline-flex;
    gap: var(--spacing-sm);
}

.pulse-dots span {
    width: 12px;
    height: 12px;
    background-color: var(--color-primary);
    border-radius: var(--radius-full);
    animation: pulse 1.4s ease-in-out infinite;
}

.pulse-dots span:nth-child(2) {
    animation-delay: 0.2s;
}

.pulse-dots span:nth-child(3) {
    animation-delay: 0.4s;
}

@keyframes pulse {
    0%, 80%, 100% {
        transform: scale(0.8);
        opacity: 0.5;
    }
    40% {
        transform: scale(1);
        opacity: 1;
    }
}

.loading-state h2 {
    font-size: 1.375rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: var(--spacing-sm);
}

.loading-subtitle {
    color: var(--color-text-muted);
    font-size: 0.9375rem;
}

/* === Error State === */
.error-state {
    text-align: center;
    padding: var(--spacing-2xl) var(--spacing-md);
    background: var(--color-surface);
    border-radius: var(--radius-lg);
    border: 1px solid var(--color-border);
    max-width: 480px;
    margin: var(--spacing-2xl) auto;
    box-shadow: var(--shadow-md);
}

.error-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 56px;
    height: 56px;
    background-color: var(--color-surface-alt);
    border-radius: var(--radius-full);
    color: var(--color-text-muted);
    margin-bottom: var(--spacing-lg);
}

.error-state h3 {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: var(--spacing-sm);
}

.error-message {
    color: var(--color-text-muted);
    font-size: 0.9375rem;
    margin-bottom: var(--spacing-xl);
    line-height: 1.6;
}

/* === Results State === */
.results-state {
    animation: fadeIn 0.4s ease-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(8px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* === Article Info === */
.article-info {
    margin-bottom: var(--spacing-xl);
}

.article-title {
    font-size: 2rem;
    font-weight: 700;
    color: var(--color-text);
    margin-bottom: var(--spacing-sm);
    line-height: 1.3;
}

.article-source {
    color: var(--color-text-muted);
    font-size: 0.9375rem;
}

/* === Summary Banner === */
.summary-banner {
    background: linear-gradient(135deg, var(--color-primary-light) 0%, var(--color-surface) 100%);
    border: 1px solid var(--color-primary-light);
    border-radius: var(--radius-lg);
    padding: var(--spacing-xl) var(--spacing-lg);
    margin-bottom: var(--spacing-xl);
    box-shadow: var(--shadow-md);
    position: relative;
    overflow: hidden;
}

.summary-banner::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 200px;
    height: 200px;
    background: radial-gradient(circle, rgba(59, 130, 246, 0.08) 0%, transparent 70%);
    border-radius: 50%;
    transform: translate(30%, -30%);
}

.summary-badge {
    display: inline-flex;
    align-items: center;
    gap: var(--spacing-xs);
    background-color: var(--color-primary);
    color: white;
    font-size: 0.8125rem;
    font-weight: 600;
    padding: var(--spacing-xs) var(--spacing-sm);
    border-radius: var(--radius-sm);
    white-space: nowrap;
    margin-bottom: var(--spacing-md);
}

.summary-content {
    position: relative;
    font-size: 1.0625rem;
    line-height: 1.8;
    color: var(--color-text);
}

/* === Key Points Section === */
.key-points-section {
    background-color: var(--color-surface);
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    margin-bottom: var(--spacing-xl);
    border: 1px solid var(--color-border);
    box-shadow: var(--shadow-sm);
}

.key-points-section h3 {
    font-size: 1.0625rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: var(--spacing-md);
}

.key-points-list {
    list-style: none;
}

.key-points-list li {
    padding: var(--spacing-sm) 0 var(--spacing-sm) var(--spacing-lg);
    position: relative;
    color: var(--color-text-muted);
    line-height: 1.7;
    border-bottom: 1px solid var(--color-border-light);
}

.key-points-list li:last-child {
    border-bottom: none;
}

.key-points-list li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0.75rem;
    width: 8px;
    height: 8px;
    background: var(--color-accent);
    border-radius: var(--radius-full);
}

/* === Topics Section === */
.topics-section {
    background-color: var(--color-surface);
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    margin-bottom: var(--spacing-xl);
    border: 1px solid var(--color-border);
    box-shadow: var(--shadow-sm);
}

.topics-section h3 {
    font-size: 1.0625rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: var(--spacing-md);
}

.topics-list {
    display: flex;
    flex-wrap: wrap;
    gap: var(--spacing-sm);
}

.topic-tag {
    display: inline-block;
    background-color: var(--color-surface-alt);
    color: var(--color-text);
    padding: var(--spacing-xs) var(--spacing-md);
    border-radius: var(--radius-full);
    font-size: 0.875rem;
    font-weight: 500;
}

/* === Bottom Line Section === */
.bottom-line-section {
    background-color: var(--color-surface);
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    margin-bottom: var(--spacing-xl);
    border: 1px solid var(--color-border);
    box-shadow: var(--shadow-sm);
}

.bottom-line-section h3 {
    font-size: 1.0625rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: var(--spacing-md);
}

.bottom-line-text {
    color: var(--color-text-muted);
    font-size: 0.9375rem;
    line-height: 1.7;
}

/* === Actions Bar === */
.actions-bar {
    display: flex;
    justify-content: center;
    gap: var(--spacing-md);
    margin-top: var(--spacing-2xl);
    padding-top: var(--spacing-lg);
    border-top: 1px solid var(--color-border);
}

/* === Buttons === */
button {
    font-family: inherit;
    font-size: 0.9375rem;
    font-weight: 500;
    padding: var(--spacing-sm) var(--spacing-lg);
    border-radius: var(--radius-md);
    border: none;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: var(--spacing-xs);
}

.btn-primary {
    background-color: var(--color-primary);
    color: white;
    box-shadow: var(--shadow-sm);
}

.btn-primary:hover {
    background-color: var(--color-primary-dark);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
}

.btn-primary:active {
    transform: translateY(0);
}

.btn-secondary {
    background-color: var(--color-surface);
    color: var(--color-text);
    border: 1px solid var(--color-border);
}

.btn-secondary:hover {
    background-color: var(--color-surface-alt);
    border-color: var(--color-text-muted);
}

/* === Utilities === */
.hidden {
    display: none !important;
}

/* === Responsive === */
@media (max-width: 640px) {
    .page-wrapper {
        padding: var(--spacing-md);
    }

    .summary-banner {
        padding: var(--spacing-lg);
    }

    .article-title {
        font-size: 1.5rem;
    }

    .actions-bar {
        flex-direction: column;
    }

    .actions-bar button {
        width: 100%;
    }
}
```

## File: `AI Features/summarize/summarize.html`
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Article Summary | Grabbit</title>
    <link rel="stylesheet" href="summarize.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>

<body>

    <div class="page-wrapper">
        <!-- Header -->
        <header class="header">
            <div class="header-content">
                <div class="logo">
                    <img src="../../icons/icon48.png" alt="Grabbit" width="24" height="24">
                    <span>Grabbit</span>
                </div>
                <div class="header-actions">
                    <a href="#" class="close-link" id="close-btn">Done</a>
                </div>
            </div>
        </header>

        <!-- Loading State -->
        <div id="loading-state" class="loading-state">
            <div class="loading-animation">
                <div class="pulse-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
            <h2>Reading the article...</h2>
            <p class="loading-subtitle">This will just take a moment</p>
        </div>

        <!-- Error State -->
        <div id="error-state" class="error-state hidden">
            <div class="error-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="8" x2="12" y2="12"></line>
                    <line x1="12" y1="16" x2="12.01" y2="16"></line>
                </svg>
            </div>
            <h3>Oops, something went wrong</h3>
            <p id="error-message" class="error-message">Please try again</p>
            <button id="retry-btn" class="btn-primary">Try Again</button>
        </div>

        <!-- Results State -->
        <div id="results-state" class="results-state hidden">

            <!-- Article Info -->
            <div class="article-info">
                <h1 id="article-title" class="article-title">Article Title</h1>
                <p id="article-source" class="article-source">Source: example.com</p>
            </div>

            <!-- Summary Banner -->
            <div class="summary-banner">
                <div class="summary-badge">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                        <line x1="16" y1="13" x2="8" y2="13"></line>
                        <line x1="16" y1="17" x2="8" y2="17"></line>
                        <polyline points="10 9 9 9 8 9"></polyline>
                    </svg>
                    AI Summary
                </div>
                <div id="summary-text" class="summary-content">
                    Loading summary...
                </div>
            </div>

            <!-- Key Points -->
            <div class="key-points-section">
                <h3>Key Takeaways</h3>
                <ul id="key-points-list" class="key-points-list">
                    <!-- Key points injected via JS -->
                </ul>
            </div>

            <!-- Topics -->
            <div id="topics-section" class="topics-section">
                <h3>Topics Covered</h3>
                <div id="topics-list" class="topics-list">
                    <!-- Topics injected via JS -->
                </div>
            </div>

            <!-- Bottom Line -->
            <div class="bottom-line-section">
                <h3>The Bottom Line</h3>
                <p id="verdict-text" class="bottom-line-text">...</p>
            </div>

            <!-- Actions -->
            <div class="actions-bar">
                <button id="open-article" class="btn-primary">Open Full Article</button>
                <button id="copy-summary" class="btn-secondary">Copy Summary</button>
            </div>

        </div>
    </div>

    <script src="summarize.js"></script>
</body>

</html>
```

## File: `AI Features/summarize/summarize.js`
```javascript
/**
 * Article Summary Page
 * AI-powered article summarization
 */

// State
let summaryData = null;
let articleTab = null;

// DOM Elements
const loadingState = document.getElementById('loading-state');
const errorState = document.getElementById('error-state');
const resultsState = document.getElementById('results-state');

/**
 * Initialize the summary page
 */
async function init() {
    // Get the tab data from storage
    const stored = await chrome.storage.local.get(['pendingSummary']);

    if (!stored.pendingSummary || !stored.pendingSummary.tab) {
        showError('No article to summarize. Please try again from the popup.');
        return;
    }

    articleTab = stored.pendingSummary.tab;

    // Clear the pending summary
    await chrome.storage.local.remove(['pendingSummary']);

    // Start the summarization
    runSummary();
}

/**
 * Run the summary
 */
async function runSummary() {
    showLoading();

    try {
        // Add a small delay for visual smoothness
        await delay(600);

        // Send summary request to background
        const response = await chrome.runtime.sendMessage({
            action: 'summarizePage',
            tab: articleTab
        });

        if (response.error) {
            // Handle different error types
            if (response.error === 'Premium required') {
                chrome.runtime.sendMessage({ action: 'openPaymentPage' });
                showError('Premium subscription required. Opening payment page...');
                return;
            }

            if (response.error.includes('Subscription not active') ||
                response.error.includes('subscription')) {
                showError('Your subscription is not active. Please check your payment.');
                setTimeout(() => {
                    chrome.runtime.sendMessage({ action: 'openPaymentPage' });
                }, 2000);
                return;
            }

            if (response.error.includes('Monthly limit') ||
                response.error.includes('limit reached')) {
                showError('Monthly summary limit reached. Try again next month!');
                return;
            }

            throw new Error(response.error);
        }

        summaryData = response.results;

        // Show quota if available
        if (summaryData._remaining !== undefined) {
            const actionsBar = document.querySelector('.actions-bar');
            if (actionsBar) {
                // Remove existing if present
                const existing = document.getElementById('quota-display');
                if (existing) existing.remove();

                const quotaEl = document.createElement('div');
                quotaEl.id = 'quota-display';
                quotaEl.style.cssText = 'width: 100%; text-align: center; font-size: 0.8125rem; color: var(--color-text-muted); margin-top: 1rem; opacity: 0.8;';
                quotaEl.textContent = `AI calls remaining this month: ${summaryData._remaining}`;

                actionsBar.insertAdjacentElement('afterend', quotaEl);
            }
        }

        renderResults(summaryData);
        showResults();

    } catch (error) {
        console.error('Summary failed:', error);
        showError(error.message);
    }
}

/**
 * Show loading state
 */
function showLoading() {
    loadingState.classList.remove('hidden');
    errorState.classList.add('hidden');
    resultsState.classList.add('hidden');
}

/**
 * Show error state
 */
function showError(message) {
    loadingState.classList.add('hidden');
    errorState.classList.remove('hidden');
    resultsState.classList.add('hidden');
    document.getElementById('error-message').textContent = message;
}

/**
 * Show results state
 */
function showResults() {
    loadingState.classList.add('hidden');
    errorState.classList.add('hidden');
    resultsState.classList.remove('hidden');
}

/**
 * Render summary results
 */
function renderResults(data) {
    // Article Info
    document.getElementById('article-title').textContent = data.title || articleTab.title || 'Article Summary';
    document.getElementById('article-source').textContent = `Source: ${new URL(articleTab.url).hostname}`;

    // Summary
    document.getElementById('summary-text').textContent = data.summary || '';

    // Key Points
    const keyPointsList = document.getElementById('key-points-list');
    keyPointsList.innerHTML = '';
    (data.keyPoints || []).forEach(point => {
        const li = document.createElement('li');
        li.textContent = point;
        keyPointsList.appendChild(li);
    });

    // Topics (optional)
    if (data.topics && data.topics.length > 0) {
        const topicsSection = document.getElementById('topics-section');
        const topicsList = document.getElementById('topics-list');
        topicsList.innerHTML = '';

        data.topics.forEach(topic => {
            const tag = document.createElement('span');
            tag.className = 'topic-tag';
            tag.textContent = topic;
            topicsList.appendChild(tag);
        });

        topicsSection.classList.remove('hidden');
    } else {
        document.getElementById('topics-section').classList.add('hidden');
    }

    // Bottom Line
    document.getElementById('verdict-text').textContent = data.verdict || '';
}

/**
 * Helper: Escape HTML
 */
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Helper: Delay
 */
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Event Listeners
document.getElementById('close-btn').addEventListener('click', (e) => {
    e.preventDefault();
    window.close();
});

document.getElementById('retry-btn').addEventListener('click', () => {
    if (articleTab) {
        runSummary();
    } else {
        window.close();
    }
});

document.getElementById('copy-summary').addEventListener('click', async () => {
    if (summaryData) {
        const text = `Article Summary: ${summaryData.title || articleTab.title}\n\nSummary:\n${summaryData.summary}\n\nKey Takeaways:\n${(summaryData.keyPoints || []).map(p => `• ${p}`).join('\n')}\n\n${summaryData.verdict}`;
        await navigator.clipboard.writeText(text);

        const btn = document.getElementById('copy-summary');
        const originalText = btn.textContent;
        btn.textContent = 'Copied!';
        setTimeout(() => btn.textContent = originalText, 2000);
    }
});

document.getElementById('open-article').addEventListener('click', () => {
    if (articleTab) {
        chrome.tabs.create({ url: articleTab.url });
    }
});

// Initialize
init();
```

## File: `AI Features/youtube-summary/youtube-summary.css`
```css
/**
 * YouTube Summary Page Styles
 * Premium UI with left sidebar and chapter navigation
 */

:root {
    --color-bg: #0f0f10;
    --color-surface: #1a1a1d;
    --color-surface-elevated: #222225;
    --color-border: rgba(255, 255, 255, 0.08);
    --color-text: #f5f5f7;
    --color-text-secondary: #a1a1a6;
    --color-text-muted: #6e6e73;
    --color-primary: #6366f1;
    --color-primary-glow: rgba(99, 102, 241, 0.3);
    --color-youtube: #FF0000;
    --color-youtube-glow: rgba(255, 0, 0, 0.2);
    --color-success: #10b981;
    --color-error: #ef4444;
    --radius-sm: 6px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
    --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.4);
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: var(--font-sans);
    background: var(--color-bg);
    color: var(--color-text);
    min-height: 100vh;
    line-height: 1.6;
}

.page-wrapper {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

/* Header */
.header {
    position: sticky;
    top: 0;
    background: rgba(15, 15, 16, 0.9);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--color-border);
    z-index: 100;
}

.header-content {
    max-width: 1400px;
    margin: 0 auto;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 600;
    color: var(--color-text);
}

.logo img {
    border-radius: var(--radius-sm);
}

.close-link {
    color: var(--color-primary);
    text-decoration: none;
    font-weight: 500;
    padding: 0.5rem 1rem;
    border-radius: var(--radius-sm);
    transition: background 0.2s;
}

.close-link:hover {
    background: rgba(99, 102, 241, 0.1);
}

/* Loading State */
.loading-state {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 4rem 2rem;
    animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.loading-animation {
    margin-bottom: 2rem;
}

.youtube-loader {
    position: relative;
    animation: pulse 1.5s ease-in-out infinite;
}

@keyframes pulse {

    0%,
    100% {
        transform: scale(1);
        opacity: 1;
    }

    50% {
        transform: scale(1.1);
        opacity: 0.8;
    }
}

.loading-state h2 {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: var(--color-text);
}

.loading-subtitle {
    color: var(--color-text-secondary);
    margin-bottom: 2rem;
}

.loading-credit {
    color: var(--color-text-muted);
    font-size: 0.75rem;
    margin-top: -1rem;
    margin-bottom: 2rem;
}

.loading-credit a {
    color: var(--color-text-muted);
    text-decoration: none;
    border-bottom: 1px dotted var(--color-text-muted);
    transition: color 0.2s;
}

.loading-credit a:hover {
    color: var(--color-primary);
    border-bottom-color: var(--color-primary);
}


.loading-steps {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    text-align: left;
}

.loading-steps .step {
    color: var(--color-text-muted);
    font-size: 0.875rem;
    padding-left: 1.5rem;
    position: relative;
    transition: color 0.3s;
}

.loading-steps .step::before {
    content: '';
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--color-text-muted);
    transition: background 0.3s, box-shadow 0.3s;
}

.loading-steps .step.active {
    color: var(--color-text);
}

.loading-steps .step.active::before {
    background: var(--color-youtube);
    box-shadow: 0 0 10px var(--color-youtube-glow);
}

/* Error State */
.error-state {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 4rem 2rem;
}

.error-state.hidden {
    display: none;
}

.error-icon {
    color: var(--color-error);
    margin-bottom: 1.5rem;
}

.error-state h3 {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.error-message {
    color: var(--color-text-secondary);
    margin-bottom: 1.5rem;
    max-width: 400px;
}

/* Buttons */
.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: linear-gradient(135deg, var(--color-primary), #8b5cf6);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    font-size: 0.9375rem;
    font-weight: 500;
    border-radius: var(--radius-md);
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}

.btn-primary:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 16px var(--color-primary-glow);
}

.btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--color-surface-elevated);
    color: var(--color-text);
    border: 1px solid var(--color-border);
    padding: 0.75rem 1.5rem;
    font-size: 0.9375rem;
    font-weight: 500;
    border-radius: var(--radius-md);
    cursor: pointer;
    transition: background 0.2s, border-color 0.2s;
}

.btn-secondary:hover {
    background: var(--color-surface);
    border-color: rgba(255, 255, 255, 0.15);
}

/* Results State */
.results-state {
    flex: 1;
    padding: 2rem;
    animation: fadeIn 0.4s ease;
}

.results-state.hidden {
    display: none;
}

.results-layout {
    max-width: 1400px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 320px 1fr;
    gap: 2rem;
}

/* Video Sidebar */
.video-sidebar {
    position: sticky;
    top: 80px;
    height: fit-content;
}

.video-card {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-lg);
    overflow: hidden;
}

.thumbnail-wrapper {
    position: relative;
    aspect-ratio: 16/9;
    overflow: hidden;
    cursor: pointer;
}

.video-thumbnail {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s;
}

.thumbnail-wrapper:hover .video-thumbnail {
    transform: scale(1.05);
}

.play-overlay {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 64px;
    height: 64px;
    background: rgba(0, 0, 0, 0.7);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.3s;
}

.thumbnail-wrapper:hover .play-overlay {
    opacity: 1;
}

.video-title {
    font-size: 1rem;
    font-weight: 600;
    padding: 1rem 1rem 0.5rem;
    line-height: 1.4;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.video-channel {
    font-size: 0.875rem;
    color: var(--color-text-secondary);
    padding: 0 1rem 1rem;
}

/* Chapters Navigation */
.chapters-nav {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-lg);
    margin-top: 1rem;
    overflow: hidden;
}

.chapters-title {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.875rem;
    font-weight: 600;
    padding: 1rem;
    border-bottom: 1px solid var(--color-border);
    color: var(--color-text-secondary);
}

.chapters-list {
    list-style: none;
    max-height: 400px;
    overflow-y: auto;
}

.chapters-list::-webkit-scrollbar {
    width: 4px;
}

.chapters-list::-webkit-scrollbar-thumb {
    background: var(--color-border);
    border-radius: 2px;
}

.chapter-item {
    padding: 0.75rem 1rem;
    border-bottom: 1px solid var(--color-border);
    cursor: pointer;
    transition: background 0.2s;
    display: flex;
    gap: 0.75rem;
}

.chapter-item:last-child {
    border-bottom: none;
}

.chapter-item:hover {
    background: var(--color-surface-elevated);
}

.chapter-item.active {
    background: rgba(99, 102, 241, 0.1);
    border-left: 3px solid var(--color-primary);
}

.chapter-timestamp {
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--color-youtube);
    min-width: 45px;
}

.chapter-name {
    font-size: 0.8125rem;
    color: var(--color-text);
    line-height: 1.4;
}

/* Summary Content */
.summary-content {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.summary-section {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
}

.section-header {
    margin-bottom: 1rem;
}

.section-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.375rem 0.75rem;
    border-radius: var(--radius-sm);
}

.ai-badge {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(139, 92, 246, 0.15));
    color: var(--color-primary);
    border: 1px solid rgba(99, 102, 241, 0.3);
}

.summary-section h3 {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: var(--color-text);
}

.summary-text {
    font-size: 1rem;
    line-height: 1.7;
    color: var(--color-text-secondary);
}

/* Key Points */
.key-points-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

.key-points-list li {
    position: relative;
    padding-left: 1.5rem;
    color: var(--color-text-secondary);
    font-size: 0.9375rem;
    line-height: 1.6;
}

.key-points-list li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0.5rem;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--color-primary);
}

/* Chapter Summaries */
.chapter-summaries {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.chapter-summary-card {
    background: var(--color-surface-elevated);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    padding: 1.25rem;
    transition: border-color 0.2s;
}

.chapter-summary-card:hover {
    border-color: rgba(255, 255, 255, 0.15);
}

.chapter-summary-card.highlight {
    border-color: var(--color-primary);
    box-shadow: 0 0 20px var(--color-primary-glow);
}

.chapter-summary-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.75rem;
}

.chapter-summary-timestamp {
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--color-youtube);
    background: rgba(255, 0, 0, 0.1);
    padding: 0.25rem 0.5rem;
    border-radius: var(--radius-sm);
}

.chapter-summary-title {
    font-size: 0.9375rem;
    font-weight: 600;
    color: var(--color-text);
}

.chapter-summary-text {
    font-size: 0.875rem;
    color: var(--color-text-secondary);
    line-height: 1.6;
}

.chapter-summary-text.hidden {
    display: none;
}

.chapter-detailed {
    margin-top: 0.75rem;
}

.chapter-detailed.hidden {
    display: none;
}

.expand-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 0.75rem;
    padding: 0.5rem 0.75rem;
    font-size: 0.8125rem;
    font-weight: 500;
    color: var(--color-primary);
    background: rgba(99, 102, 241, 0.1);
    border: 1px solid rgba(99, 102, 241, 0.2);
    border-radius: var(--radius-sm);
    cursor: pointer;
    transition: background 0.2s, border-color 0.2s;
}

.expand-btn:hover {
    background: rgba(99, 102, 241, 0.15);
    border-color: rgba(99, 102, 241, 0.4);
}

.expand-icon {
    transition: transform 0.3s ease;
}

/* Topics */
.topics-section.hidden {
    display: none;
}

.topics-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.topic-tag {
    background: var(--color-surface-elevated);
    color: var(--color-text-secondary);
    padding: 0.375rem 0.75rem;
    border-radius: 50px;
    font-size: 0.8125rem;
    border: 1px solid var(--color-border);
    transition: border-color 0.2s, color 0.2s;
}

.topic-tag:hover {
    border-color: var(--color-primary);
    color: var(--color-text);
}

/* Actions Bar */
.actions-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    padding-top: 0.5rem;
}

/* Responsive */
@media (max-width: 1024px) {
    .results-layout {
        grid-template-columns: 1fr;
    }

    .video-sidebar {
        position: static;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
    }

    .chapters-nav {
        margin-top: 0;
    }
}

@media (max-width: 640px) {
    .header-content {
        padding: 1rem;
    }

    .results-state {
        padding: 1rem;
    }

    .video-sidebar {
        grid-template-columns: 1fr;
    }

    .summary-section {
        padding: 1rem;
    }

    .actions-bar {
        flex-direction: column;
    }
}
```

## File: `AI Features/youtube-summary/youtube-summary.html`
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Summary | Grabbit</title>
    <link rel="stylesheet" href="youtube-summary.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>

<body>

    <div class="page-wrapper">
        <!-- Header -->
        <header class="header">
            <div class="header-content">
                <div class="logo">
                    <img src="../../icons/icon48.png" alt="Grabbit" width="24" height="24">
                    <span>Grabbit</span>
                </div>
                <div class="header-actions">
                    <a href="#" class="close-link" id="close-btn">Done</a>
                </div>
            </div>
        </header>

        <!-- Loading State -->
        <div id="loading-state" class="loading-state">
            <div class="loading-animation">
                <div class="youtube-loader">
                    <svg width="64" height="64" viewBox="0 0 24 24" fill="#FF0000">
                        <path
                            d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814z" />
                        <polygon fill="white" points="9.545,15.568 15.818,12 9.545,8.432" />
                    </svg>
                </div>
            </div>
            <h2>Reading the transcript...</h2>
            <p class="loading-subtitle">Analyzing video content with AI</p>
            <p class="loading-credit">Feature by <a href="https://subtiltee.com/all-extensions"
                    target="_blank">Subtiltee</a></p>
            <div class="loading-steps">
                <div class="step active" id="step-extract">Extracting transcript...</div>
                <div class="step" id="step-analyze">Analyzing with AI...</div>
                <div class="step" id="step-render">Building summary...</div>
            </div>
        </div>

        <!-- Error State -->
        <div id="error-state" class="error-state hidden">
            <div class="error-icon">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="8" x2="12" y2="12"></line>
                    <line x1="12" y1="16" x2="12.01" y2="16"></line>
                </svg>
            </div>
            <h3>Oops, something went wrong</h3>
            <p id="error-message" class="error-message">Please try again</p>
            <button id="retry-btn" class="btn-primary">Try Again</button>
        </div>

        <!-- Results State -->
        <div id="results-state" class="results-state hidden">
            <div class="results-layout">

                <!-- Left Sidebar - Video Info -->
                <aside class="video-sidebar">
                    <div class="video-card">
                        <div class="thumbnail-wrapper">
                            <img id="video-thumbnail" src="" alt="Video Thumbnail" class="video-thumbnail">
                            <div class="play-overlay">
                                <svg width="48" height="48" viewBox="0 0 24 24" fill="white">
                                    <polygon points="5,3 19,12 5,21" />
                                </svg>
                            </div>
                        </div>
                        <h2 id="video-title" class="video-title">Video Title</h2>
                        <p id="video-channel" class="video-channel">Channel Name</p>
                    </div>

                    <!-- Chapters Navigation -->
                    <div class="chapters-nav" id="chapters-nav">
                        <h3 class="chapters-title">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2">
                                <line x1="8" y1="6" x2="21" y2="6"></line>
                                <line x1="8" y1="12" x2="21" y2="12"></line>
                                <line x1="8" y1="18" x2="21" y2="18"></line>
                                <line x1="3" y1="6" x2="3.01" y2="6"></line>
                                <line x1="3" y1="12" x2="3.01" y2="12"></line>
                                <line x1="3" y1="18" x2="3.01" y2="18"></line>
                            </svg>
                            Chapters
                        </h3>
                        <ul id="chapters-list" class="chapters-list">
                            <!-- Chapters injected via JS -->
                        </ul>
                    </div>
                </aside>

                <!-- Main Content - Summary -->
                <main class="summary-content">

                    <!-- Overall Summary -->
                    <section class="summary-section overall-summary">
                        <div class="section-header">
                            <div class="section-badge ai-badge">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2">
                                    <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
                                    <path d="M2 17l10 5 10-5"></path>
                                    <path d="M2 12l10 5 10-5"></path>
                                </svg>
                                AI Summary
                            </div>
                        </div>
                        <p id="overall-summary" class="summary-text">
                            Loading summary...
                        </p>
                    </section>

                    <!-- Key Points -->
                    <section class="summary-section key-points-section">
                        <h3>Key Takeaways</h3>
                        <ul id="key-points-list" class="key-points-list">
                            <!-- Key points injected via JS -->
                        </ul>
                    </section>

                    <!-- Chapter Summaries -->
                    <section class="summary-section chapters-section" id="chapters-section">
                        <h3>Chapter Breakdown</h3>
                        <div id="chapter-summaries" class="chapter-summaries">
                            <!-- Chapter summaries injected via JS -->
                        </div>
                    </section>

                    <!-- Topics -->
                    <section id="topics-section" class="summary-section topics-section hidden">
                        <h3>Topics Covered</h3>
                        <div id="topics-list" class="topics-list">
                            <!-- Topics injected via JS -->
                        </div>
                    </section>

                    <!-- Actions -->
                    <div class="actions-bar">
                        <button id="open-video" class="btn-primary">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2">
                                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                                <polyline points="15 3 21 3 21 9"></polyline>
                                <line x1="10" y1="14" x2="21" y2="3"></line>
                            </svg>
                            Open Video
                        </button>
                        <button id="copy-summary" class="btn-secondary">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2">
                                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                            </svg>
                            Copy Summary
                        </button>
                        <button id="download-txt" class="btn-secondary">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2">
                                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                                <polyline points="7 10 12 15 17 10"></polyline>
                                <line x1="12" y1="15" x2="12" y2="3"></line>
                            </svg>
                            Download Text
                        </button>
                        <button id="download-html" class="btn-secondary">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                <polyline points="14 2 14 8 20 8"></polyline>
                                <line x1="16" y1="13" x2="8" y2="13"></line>
                                <line x1="16" y1="17" x2="8" y2="17"></line>
                            </svg>
                            Download Page
                        </button>
                    </div>

                </main>
            </div>
        </div>
    </div>

    <script src="youtube-summary.js"></script>
</body>

</html>
```

## File: `AI Features/youtube-summary/youtube-summary.js`
```javascript
/**
 * YouTube Summary Page
 * AI-powered video summarization using transcript data
 */

// State
let summaryData = null;
let videoTab = null;

// DOM Elements
const loadingState = document.getElementById('loading-state');
const errorState = document.getElementById('error-state');
const resultsState = document.getElementById('results-state');

/**
 * Initialize the YouTube summary page
 */
async function init() {
    // Get the tab data from storage
    const stored = await chrome.storage.local.get(['pendingYoutubeSummary']);

    if (!stored.pendingYoutubeSummary || !stored.pendingYoutubeSummary.tab) {
        showError('No video to summarize. Please try again from the popup.');
        return;
    }

    videoTab = stored.pendingYoutubeSummary.tab;

    // Clear the pending summary
    await chrome.storage.local.remove(['pendingYoutubeSummary']);

    // Start the summarization
    runSummary();
}

/**
 * Run the summary
 */
async function runSummary() {
    showLoading();

    try {
        // Update loading step
        await delay(400);
        updateLoadingStep('step-extract');

        // Send summary request to background
        const response = await chrome.runtime.sendMessage({
            action: 'summarizeYoutube',
            tab: videoTab
        });

        // Update loading step
        updateLoadingStep('step-analyze');
        await delay(300);

        if (response.error) {
            // Handle different error types
            if (response.error === 'Premium required') {
                chrome.runtime.sendMessage({ action: 'openPaymentPage' });
                showError('Premium subscription required. Opening payment page...');
                return;
            }

            if (response.error.includes('Subscription not active') ||
                response.error.includes('subscription')) {
                showError('Your subscription is not active. Please check your payment.');
                setTimeout(() => {
                    chrome.runtime.sendMessage({ action: 'openPaymentPage' });
                }, 2000);
                return;
            }

            if (response.error.includes('Monthly limit') ||
                response.error.includes('limit reached')) {
                showError('Monthly summary limit reached. Try again next month!');
                return;
            }

            if (response.error.includes('No transcript') ||
                response.error.includes('captions')) {
                showError('No transcript available for this video. The video may not have captions enabled.');
                return;
            }

            throw new Error(response.error);
        }

        // Update loading step
        updateLoadingStep('step-render');
        await delay(300);

        summaryData = response.results;

        // Show quota if available
        if (summaryData._remaining !== undefined) {
            const actionsBar = document.querySelector('.actions-bar');
            if (actionsBar) {
                const existing = document.getElementById('quota-display');
                if (existing) existing.remove();

                const quotaEl = document.createElement('div');
                quotaEl.id = 'quota-display';
                quotaEl.style.cssText = 'width: 100%; text-align: center; font-size: 0.8125rem; color: var(--color-text-muted); margin-top: 1rem; opacity: 0.8;';
                quotaEl.textContent = `AI calls remaining this month: ${summaryData._remaining}`;

                actionsBar.insertAdjacentElement('afterend', quotaEl);
            }
        }

        renderResults(summaryData);
        showResults();

    } catch (error) {
        console.error('YouTube Summary failed:', error);
        showError(error.message);
    }
}

/**
 * Update loading step indicator
 */
function updateLoadingStep(stepId) {
    document.querySelectorAll('.loading-steps .step').forEach(s => s.classList.remove('active'));
    const activeStep = document.getElementById(stepId);
    if (activeStep) activeStep.classList.add('active');
}

/**
 * Show loading state
 */
function showLoading() {
    loadingState.classList.remove('hidden');
    loadingState.style.display = 'flex';
    errorState.classList.add('hidden');
    resultsState.classList.add('hidden');
}

/**
 * Show error state
 */
function showError(message) {
    loadingState.classList.add('hidden');
    loadingState.style.display = 'none';
    errorState.classList.remove('hidden');
    resultsState.classList.add('hidden');
    document.getElementById('error-message').textContent = message;
}

/**
 * Show results state
 */
function showResults() {
    loadingState.classList.add('hidden');
    loadingState.style.display = 'none';
    errorState.classList.add('hidden');
    resultsState.classList.remove('hidden');
}

/**
 * Extract video ID from YouTube URL
 */
function getVideoId(url) {
    const match = url.match(/[?&]v=([^&]+)/);
    return match ? match[1] : null;
}

/**
 * Render summary results
 */
function renderResults(data) {
    // Video Info
    const videoId = getVideoId(videoTab.url);
    const thumbnail = document.getElementById('video-thumbnail');

    if (videoId) {
        thumbnail.src = `https://img.youtube.com/vi/${videoId}/maxresdefault.jpg`;
        thumbnail.onerror = () => {
            // Fallback to lower resolution
            thumbnail.src = `https://img.youtube.com/vi/${videoId}/hqdefault.jpg`;
        };
    }

    document.getElementById('video-title').textContent = data.title || videoTab.title || 'Video Summary';
    document.getElementById('video-channel').textContent = data.channel || '';

    // Make thumbnail clickable to open video
    document.querySelector('.thumbnail-wrapper').addEventListener('click', () => {
        chrome.tabs.create({ url: videoTab.url });
    });

    // Overall Summary
    document.getElementById('overall-summary').textContent = data.overallSummary || data.summary || '';

    // Key Points
    const keyPointsList = document.getElementById('key-points-list');
    keyPointsList.innerHTML = '';
    (data.keyPoints || []).forEach(point => {
        const li = document.createElement('li');
        li.textContent = point;
        keyPointsList.appendChild(li);
    });

    // Chapters Navigation & Summaries
    const chaptersNav = document.getElementById('chapters-nav');
    const chaptersList = document.getElementById('chapters-list');
    const chapterSummaries = document.getElementById('chapter-summaries');
    const chaptersSection = document.getElementById('chapters-section');

    if (data.chapters && data.chapters.length > 0) {
        chaptersNav.style.display = 'block';
        chaptersSection.style.display = 'block';
        chaptersList.innerHTML = '';
        chapterSummaries.innerHTML = '';

        data.chapters.forEach((chapter, index) => {
            // Navigation item
            const li = document.createElement('li');
            li.className = 'chapter-item';
            li.dataset.index = index;
            li.innerHTML = `
                <span class="chapter-timestamp">${chapter.timestamp || ''}</span>
                <span class="chapter-name">${chapter.title || `Chapter ${index + 1}`}</span>
            `;
            li.addEventListener('click', () => scrollToChapter(index));
            chaptersList.appendChild(li);

            // Summary card with expandable content
            const card = document.createElement('div');
            card.className = 'chapter-summary-card';
            card.id = `chapter-${index}`;

            // Use shortSummary if available, fallback to summary
            const shortSummary = chapter.shortSummary || chapter.summary || '';
            const detailedSummary = chapter.detailedSummary || '';
            const hasDetails = detailedSummary && detailedSummary !== shortSummary;

            card.innerHTML = `
                <div class="chapter-summary-header">
                    <span class="chapter-summary-timestamp">${chapter.timestamp || ''}</span>
                    <span class="chapter-summary-title">${chapter.title || `Chapter ${index + 1}`}</span>
                </div>
                <p class="chapter-summary-text chapter-short">${shortSummary}</p>
                ${hasDetails ? `
                    <div class="chapter-detailed hidden">
                        <p class="chapter-summary-text">${detailedSummary}</p>
                    </div>
                    <button class="expand-btn" data-expanded="false">
                        <svg class="expand-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                        <span class="expand-text">Show detailed summary</span>
                    </button>
                ` : ''}
            `;

            // Add expand/collapse functionality
            if (hasDetails) {
                const expandBtn = card.querySelector('.expand-btn');
                expandBtn.addEventListener('click', () => toggleChapterDetails(card, expandBtn));
            }

            chapterSummaries.appendChild(card);
        });
    } else {
        // No chapters - hide chapters UI
        chaptersNav.style.display = 'none';
        chaptersSection.style.display = 'none';
    }

    // Topics
    const topicsSection = document.getElementById('topics-section');
    const topicsList = document.getElementById('topics-list');

    if (data.topics && data.topics.length > 0) {
        topicsSection.classList.remove('hidden');
        topicsList.innerHTML = '';

        data.topics.forEach(topic => {
            const tag = document.createElement('span');
            tag.className = 'topic-tag';
            tag.textContent = topic;
            topicsList.appendChild(tag);
        });
    } else {
        topicsSection.classList.add('hidden');
    }
}

/**
 * Scroll to and highlight a chapter summary
 */
function scrollToChapter(index) {
    // Update active chapter in navigation
    document.querySelectorAll('.chapter-item').forEach(item => {
        item.classList.toggle('active', parseInt(item.dataset.index) === index);
    });

    // Scroll to chapter summary
    const chapterCard = document.getElementById(`chapter-${index}`);
    if (chapterCard) {
        chapterCard.scrollIntoView({ behavior: 'smooth', block: 'center' });

        // Highlight briefly
        chapterCard.classList.add('highlight');
        setTimeout(() => chapterCard.classList.remove('highlight'), 2000);
    }
}

/**
 * Toggle chapter detailed summary visibility
 */
function toggleChapterDetails(card, btn) {
    const detailed = card.querySelector('.chapter-detailed');
    const shortText = card.querySelector('.chapter-short');
    const isExpanded = btn.dataset.expanded === 'true';

    if (isExpanded) {
        // Collapse
        detailed.classList.add('hidden');
        shortText.classList.remove('hidden');
        btn.dataset.expanded = 'false';
        btn.querySelector('.expand-text').textContent = 'Show detailed summary';
        btn.querySelector('.expand-icon').style.transform = 'rotate(0deg)';
    } else {
        // Expand
        detailed.classList.remove('hidden');
        shortText.classList.add('hidden');
        btn.dataset.expanded = 'true';
        btn.querySelector('.expand-text').textContent = 'Show short summary';
        btn.querySelector('.expand-icon').style.transform = 'rotate(180deg)';
    }
}

/**
 * Helper: Delay
 */
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Event Listeners
document.getElementById('close-btn').addEventListener('click', (e) => {
    e.preventDefault();
    window.close();
});

document.getElementById('retry-btn').addEventListener('click', () => {
    if (videoTab) {
        runSummary();
    } else {
        window.close();
    }
});

document.getElementById('copy-summary').addEventListener('click', async () => {
    if (summaryData) {
        let text = `YouTube Video Summary: ${summaryData.title || videoTab.title}\n\n`;
        text += `Summary:\n${summaryData.overallSummary || summaryData.summary || ''}\n\n`;

        if (summaryData.keyPoints && summaryData.keyPoints.length > 0) {
            text += `Key Takeaways:\n${summaryData.keyPoints.map(p => `• ${p}`).join('\n')}\n\n`;
        }

        if (summaryData.chapters && summaryData.chapters.length > 0) {
            text += `Chapter Breakdown:\n`;
            summaryData.chapters.forEach(ch => {
                const summary = ch.detailedSummary || ch.shortSummary || ch.summary || '';
                text += `\n[${ch.timestamp}] ${ch.title}\n${summary}\n`;
            });
        }

        await navigator.clipboard.writeText(text);

        const btn = document.getElementById('copy-summary');
        const originalText = btn.innerHTML;
        btn.textContent = 'Copied!';
        setTimeout(() => btn.innerHTML = originalText, 2000);
    }
});

document.getElementById('open-video').addEventListener('click', () => {
    if (videoTab) {
        chrome.tabs.create({ url: videoTab.url });
    }
});

// Download as Text file
document.getElementById('download-txt').addEventListener('click', () => {
    if (!summaryData) return;

    const text = generateSummaryText();
    const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
    const filename = sanitizeFilename(summaryData.title || videoTab.title || 'youtube-summary') + '.txt';
    downloadBlob(blob, filename);
});

// Download as HTML page
document.getElementById('download-html').addEventListener('click', async () => {
    if (!summaryData) return;

    const html = await generateStandaloneHTML();
    const blob = new Blob([html], { type: 'text/html;charset=utf-8' });
    const filename = sanitizeFilename(summaryData.title || videoTab.title || 'youtube-summary') + '.html';
    downloadBlob(blob, filename);
});

/**
 * Generate plain text summary (same format as copy)
 */
function generateSummaryText() {
    let text = `YouTube Video Summary: ${summaryData.title || videoTab.title}\n`;
    text += `URL: ${videoTab.url}\n\n`;
    text += `═══════════════════════════════════════════════════════════════\n\n`;
    text += `SUMMARY\n`;
    text += `───────────────────────────────────────────────────────────────\n`;
    text += `${summaryData.overallSummary || summaryData.summary || ''}\n\n`;

    if (summaryData.keyPoints && summaryData.keyPoints.length > 0) {
        text += `KEY TAKEAWAYS\n`;
        text += `───────────────────────────────────────────────────────────────\n`;
        text += summaryData.keyPoints.map(p => `• ${p}`).join('\n') + '\n\n';
    }

    if (summaryData.chapters && summaryData.chapters.length > 0) {
        text += `CHAPTER BREAKDOWN\n`;
        text += `───────────────────────────────────────────────────────────────\n`;
        summaryData.chapters.forEach(ch => {
            const summary = ch.detailedSummary || ch.shortSummary || ch.summary || '';
            text += `\n[${ch.timestamp}] ${ch.title}\n`;
            text += `${summary}\n`;
        });
    }

    if (summaryData.topics && summaryData.topics.length > 0) {
        text += `\nTOPICS: ${summaryData.topics.join(', ')}\n`;
    }

    text += `\n═══════════════════════════════════════════════════════════════\n`;
    text += `Generated by Grabbit - https://grabbit.socratisp.com\n`;

    return text;
}

/**
 * Generate standalone HTML page with embedded CSS
 */
async function generateStandaloneHTML() {
    const videoId = getVideoId(videoTab.url);
    const thumbnailUrl = videoId ? `https://img.youtube.com/vi/${videoId}/maxresdefault.jpg` : '';

    // Get the current CSS
    const cssResponse = await fetch(chrome.runtime.getURL('AI Features/youtube-summary/youtube-summary.css'));
    const css = await cssResponse.text();

    // Build chapters HTML
    let chaptersHTML = '';
    if (summaryData.chapters && summaryData.chapters.length > 0) {
        chaptersHTML = summaryData.chapters.map((ch, i) => {
            const shortSummary = ch.shortSummary || ch.summary || '';
            const detailedSummary = ch.detailedSummary || '';
            return `
                <div class="chapter-summary-card">
                    <div class="chapter-summary-header">
                        <span class="chapter-summary-timestamp">${ch.timestamp || ''}</span>
                        <span class="chapter-summary-title">${ch.title || `Chapter ${i + 1}`}</span>
                    </div>
                    <p class="chapter-summary-text">${shortSummary}</p>
                    ${detailedSummary ? `<div class="chapter-detailed"><p class="chapter-summary-text">${detailedSummary}</p></div>` : ''}
                </div>
            `;
        }).join('');
    }

    // Build key points HTML
    let keyPointsHTML = '';
    if (summaryData.keyPoints && summaryData.keyPoints.length > 0) {
        keyPointsHTML = summaryData.keyPoints.map(p => `<li>${p}</li>`).join('');
    }

    // Build topics HTML
    let topicsHTML = '';
    if (summaryData.topics && summaryData.topics.length > 0) {
        topicsHTML = summaryData.topics.map(t => `<span class="topic-tag">${t}</span>`).join('');
    }

    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${summaryData.title || 'YouTube Summary'} | Grabbit</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>${css}</style>
</head>
<body>
    <div class="page-wrapper">
        <header class="header">
            <div class="header-content">
                <div class="logo"><span>📹 YouTube Summary</span></div>
                <div class="header-actions">
                    <a href="${videoTab.url}" target="_blank" class="close-link">Watch Video</a>
                </div>
            </div>
        </header>

        <div class="results-state" style="display: block;">
            <div class="results-layout">
                <aside class="video-sidebar">
                    <div class="video-card">
                        <div class="thumbnail-wrapper">
                            <img src="${thumbnailUrl}" alt="Video Thumbnail" class="video-thumbnail">
                        </div>
                        <h2 class="video-title">${summaryData.title || ''}</h2>
                        <p class="video-channel">${summaryData.channel || ''}</p>
                    </div>
                </aside>

                <main class="summary-content">
                    <section class="summary-section overall-summary">
                        <div class="section-header">
                            <div class="section-badge ai-badge">AI Summary</div>
                        </div>
                        <p class="summary-text">${summaryData.overallSummary || summaryData.summary || ''}</p>
                    </section>

                    <section class="summary-section key-points-section">
                        <h3>Key Takeaways</h3>
                        <ul class="key-points-list">${keyPointsHTML}</ul>
                    </section>

                    <section class="summary-section chapters-section">
                        <h3>Chapter Breakdown</h3>
                        <div class="chapter-summaries">${chaptersHTML}</div>
                    </section>

                    ${topicsHTML ? `
                    <section class="summary-section topics-section">
                        <h3>Topics Covered</h3>
                        <div class="topics-list">${topicsHTML}</div>
                    </section>
                    ` : ''}

                    <div class="actions-bar" style="margin-top: 2rem;">
                        <a href="${videoTab.url}" target="_blank" class="btn-primary" style="text-decoration: none;">Open Video</a>
                    </div>
                </main>
            </div>
        </div>
    </div>
    <p style="text-align: center; color: #6e6e73; padding: 2rem; font-size: 0.875rem;">
        Generated by Grabbit • ${new Date().toLocaleDateString()}
    </p>
</body>
</html>`;
}

/**
 * Helper: Sanitize filename
 */
function sanitizeFilename(name) {
    return name.replace(/[<>:"/\\|?*]/g, '').replace(/\s+/g, '_').substring(0, 100);
}

/**
 * Helper: Trigger download
 */
function downloadBlob(blob, filename) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Initialize
init();
```

## File: `advancedOptions/advancedOptions.css`
```css
/* Switch Styling */
.switch {
    position: relative;
    display: inline-block;
    width: 50px;
    height: 24px;
    flex-shrink: 0;
}

.switch input {
    opacity: 0;
    width: 0;
    height: 0;
}

.slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    transition: .4s;
}

.slider:before {
    position: absolute;
    content: "";
    height: 16px;
    width: 16px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    transition: .4s;
}

input:checked+.slider {
    background-color: var(--primary-color, #2196f3);
}

input:focus+.slider {
    box-shadow: 0 0 1px var(--primary-color, #2196f3);
}

input:checked+.slider:before {
    transform: translateX(26px);
}

.slider.round {
    border-radius: 24px;
}

.slider.round:before {
    border-radius: 50%;
}

.option-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 0;
    border-bottom: 1px solid #eee;
}

.option-item:last-child {
    border-bottom: none;
}

.option-label label {
    font-weight: 600;
    display: block;
    margin-bottom: 5px;
}

.description {
    font-size: 14px;
    color: #777;
    margin: 0;
}

.status-message {
    margin-top: 20px;
    text-align: center;
    color: green;
    font-weight: bold;
    min-height: 20px;
}

/* Exclusion Filters Styles */
.filter-input-row {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

.filter-input {
    flex: 1;
    padding: 0.6rem 0.8rem;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 14px;
    transition: border-color 0.2s, box-shadow 0.2s;
}

.filter-input:focus {
    outline: none;
    border-color: var(--primary-color, #2196f3);
    box-shadow: 0 0 0 3px rgba(33, 150, 243, 0.15);
}

.btn {
    padding: 0.6rem 1.2rem;
    border: none;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.2s, transform 0.1s;
}

.btn:hover {
    transform: translateY(-1px);
}

.btn:active {
    transform: translateY(0);
}

.btn-primary {
    background-color: var(--primary-color, #2196f3);
    color: white;
}

.btn-primary:hover {
    background-color: #1976d2;
}

.btn-secondary {
    background-color: #e0e0e0;
    color: #333;
}

.btn-secondary:hover {
    background-color: #bdbdbd;
}

.filter-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.filter-tag {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.4rem 0.6rem 0.4rem 0.8rem;
    background: linear-gradient(135deg, #f5f5f5, #eeeeee);
    border: 1px solid #ddd;
    border-radius: 20px;
    font-size: 13px;
    color: #333;
    font-family: 'Consolas', 'Monaco', monospace;
}

.filter-tag .delete-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 18px;
    height: 18px;
    border: none;
    border-radius: 50%;
    background-color: rgba(0, 0, 0, 0.1);
    color: #666;
    font-size: 14px;
    cursor: pointer;
    transition: background-color 0.2s, color 0.2s;
    line-height: 1;
}

.filter-tag .delete-btn:hover {
    background-color: #d32f2f;
    color: white;
}
```

## File: `advancedOptions/advancedOptions.html`
```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Grabbit - Advanced Options</title>
    <link rel="stylesheet" href="/css/variables.css">
    <link rel="stylesheet" href="/css/components/sidebar.css">
    <link rel="stylesheet" href="/css/options.css">
    <link rel="stylesheet" href="advancedOptions.css">
</head>

<body>
    <div id="sidebar-placeholder" data-active-section="advanced-options"></div>

    <div class="container">
        <div id="advanced-options">
            <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 2rem;">
                <img src="/icons/icon128.png" alt="Grabbit Logo" style="width: 64px; height: 64px;">
                <h1 style="margin: 0;">Advanced Options</h1>
            </div>

            <div class="card">
                <h2>Experimental Features</h2>
                <p style="color: #666; margin-bottom: 1.5rem;">Configure advanced behavior and experimental
                    functionality.</p>

                <!-- Linkify Section -->
                <h3 style="margin-bottom: 0.75rem; color: #333; border-bottom: 1px solid #eee; padding-bottom: 0.5rem;">
                    🔗 Linkify</h3>

                <div class="option-item">
                    <div class="option-label">
                        <label for="linkify-toggle">Auto-Linkify Plain Text URLs</label>
                        <p class="description">Automatically converts text that looks like a URL (e.g.
                            https://google.com, www.example.com) into clickable links. Includes support for links inside
                            code blocks.</p>
                    </div>
                    <label class="switch">
                        <input type="checkbox" id="linkify-toggle">
                        <span class="slider round"></span>
                    </label>
                </div>

                <div class="option-item" id="linkify-aggressive-container"
                    style="margin-top: 1rem; border-top: 1px solid #eee; padding-top: 1rem;">
                    <div class="option-label">
                        <label for="linkify-aggressive">Aggressive Linkify (Domain-only)</label>
                        <p class="description">Recognizes links without prefixes (e.g., "google.com").
                            <span style="color: #d32f2f; display: block; margin-top: 0.25rem;">⚠️ Note: This may cause
                                false positives on filenames or version numbers (e.g. app.js).</span>
                        </p>
                    </div>
                    <label class="switch">
                        <input type="checkbox" id="linkify-aggressive">
                        <span class="slider round"></span>
                    </label>
                </div>

                <!-- Duplicate Link Highlighter Section -->
                <h3 style="margin-top: 2rem; margin-bottom: 0.75rem; color: #333; border-bottom: 1px solid #eee; padding-bottom: 0.5rem;">
                    ✨ Duplicate Link Highlighter</h3>

                <div class="option-item">
                    <div class="option-label">
                        <label for="duplicate-highlighter-toggle">Enable Duplicate Highlighter</label>
                        <p class="description">Visually highlights links that appear more than once on the page with a colored underline. Different colors are used for each set of duplicate links.</p>
                    </div>
                    <label class="switch">
                        <input type="checkbox" id="duplicate-highlighter-toggle">
                        <span class="slider round"></span>
                    </label>
                </div>

                <!-- Exclusion Filters Section -->
                <h3
                    style="margin-top: 2rem; margin-bottom: 1rem; color: #333; border-bottom: 1px solid #eee; padding-bottom: 0.5rem;">
                    🚫 Exclusion Filters
                </h3>

                <!-- URL Filters -->
                <div class="option-item" style="flex-direction: column; align-items: stretch; margin-bottom: 1.5rem;">
                    <div class="option-label" style="margin-bottom: 1rem;">
                        <label>URL Filters</label>
                        <p class="description">Add keywords or Regular Expressions to exclude matching links from
                            drag-selection.
                            <br>Links containing these patterns in the <b><u>URL</u></b> will be automatically skipped.</p>
                    </div>

                    <div class="filter-input-row">
                        <input type="text"
                               id="filter-input"
                               placeholder="e.g., google.com or ^https?://ad\."
                               class="filter-input">
                        <button id="add-filter-btn" class="btn btn-primary">Add</button>
                    </div>

                    <ul id="filter-list" class="filter-list"></ul>

                    <div id="clear-filters-container" style="margin-top: 1rem; text-align: right; display: none;">
                        <button id="clear-all-filters-btn" class="btn btn-secondary btn-sm">Clear All URL Filters</button>
                    </div>
                </div>

                <!-- Link Text Filters -->
                <div class="option-item" style="flex-direction: column; align-items: stretch;">
                    <div class="option-label" style="margin-bottom: 1rem;">
                        <label>Link Text Filters</label>
                        <p class="description">Add keywords or Regular Expressions to exclude matching links from
                            drag-selection based on their visible text (anchor text, aria-label, title, or image alt).
                            <br>Links containing these patterns in the <b><u>visible text</u></b> will be automatically skipped.</p>
                    </div>

                    <div class="filter-input-row">
                        <input type="text"
                               id="link-text-filter-input"
                               placeholder="e.g., download or ^buy\s+now"
                               class="filter-input">
                        <button id="add-link-text-filter-btn" class="btn btn-primary">Add</button>
                    </div>

                    <ul id="link-text-filter-list" class="filter-list"></ul>

                    <div id="clear-link-text-filters-container" style="margin-top: 1rem; text-align: right; display: none;">
                        <button id="clear-all-link-text-filters-btn" class="btn btn-secondary btn-sm">Clear All Link Text Filters</button>
                    </div>
                </div>

                <!-- Disabled Domains Section -->
                <h3
                    style="margin-top: 2rem; margin-bottom: 0.75rem; color: #333; border-bottom: 1px solid #eee; padding-bottom: 0.5rem;">
                    ⛔ Disabled Domains</h3>

                <div class="option-item" style="flex-direction: column; align-items: stretch;">
                    <div class="option-label" style="margin-bottom: 1rem;">
                        <label>Blocklist</label>
                        <p class="description">Prevent Grabbit from running on these domains entirely (e.g.,
                            `google.com`, `figma.com`).</p>
                    </div>

                    <div class="filter-input-row">
                        <input type="text" id="disabled-domain-input" placeholder="e.g. google.com"
                            class="filter-input">
                        <button id="add-disabled-domain-btn" class="btn btn-primary">Add</button>
                    </div>

                    <ul id="disabled-domains-list" class="filter-list"></ul>
                </div>

                <div id="status" class="status-message"></div>
            </div>

            <footer class="footer">
                <p style="color: #999; font-size: 0.85rem;">These features are experimental and may change in future
                    updates.</p>
            </footer>
        </div>
    </div>

    <script src="/js/components/sidebar.js"></script>
    <script src="advancedOptions.js"></script>
</body>

</html>
```

## File: `advancedOptions/advancedOptions.js`
```javascript
/**
 * Grabbit Advanced Options JavaScript
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log('Advanced Options initialized');

    const linkifyToggle = document.getElementById('linkify-toggle');
    const linkifyAggressive = document.getElementById('linkify-aggressive');
    const aggressiveContainer = document.getElementById('linkify-aggressive-container');
    const duplicateHighlighterToggle = document.getElementById('duplicate-highlighter-toggle');
    const status = document.getElementById('status');

    // URL Filters elements (backwards-compatible storage key: exclusionFilters)
    const urlFilterInput = document.getElementById('filter-input');
    const addUrlFilterBtn = document.getElementById('add-filter-btn');
    const urlFilterList = document.getElementById('filter-list');
    const clearUrlFiltersContainer = document.getElementById('clear-filters-container');
    const clearAllUrlFiltersBtn = document.getElementById('clear-all-filters-btn');

    // Link Text Filters elements (new storage key: linkTextExclusionFilters)
    const linkTextFilterInput = document.getElementById('link-text-filter-input');
    const addLinkTextFilterBtn = document.getElementById('add-link-text-filter-btn');
    const linkTextFilterList = document.getElementById('link-text-filter-list');
    const clearLinkTextFiltersContainer = document.getElementById('clear-link-text-filters-container');
    const clearAllLinkTextFiltersBtn = document.getElementById('clear-all-link-text-filters-btn');

    // Disabled Domains elements
    const disabledDomainInput = document.getElementById('disabled-domain-input');
    const addDisabledDomainBtn = document.getElementById('add-disabled-domain-btn');
    const disabledDomainsList = document.getElementById('disabled-domains-list');

    // Local state for filters
    let exclusionFilters = [];
    let linkTextExclusionFilters = [];
    let disabledDomains = [];

    // === Linkify Section ===
    if (linkifyToggle && linkifyAggressive) {
        // Load saved settings
        chrome.storage.sync.get(['linkifyEnabled', 'linkifyAggressive', 'duplicateHighlighterEnabled'], (result) => {
            linkifyToggle.checked = result.linkifyEnabled || false;
            linkifyAggressive.checked = result.linkifyAggressive || false;
            if (duplicateHighlighterToggle) {
                duplicateHighlighterToggle.checked = result.duplicateHighlighterEnabled || false;
            }
            updateAggressiveUI();
        });

        // Save settings on change
        linkifyToggle.addEventListener('change', () => {
            chrome.storage.sync.set({ linkifyEnabled: linkifyToggle.checked }, () => {
                showStatus('Settings saved!');
                updateAggressiveUI();
            });
        });

        linkifyAggressive.addEventListener('change', () => {
            chrome.storage.sync.set({ linkifyAggressive: linkifyAggressive.checked }, () => {
                showStatus('Settings saved!');
            });
        });

        if (duplicateHighlighterToggle) {
            duplicateHighlighterToggle.addEventListener('change', () => {
                chrome.storage.sync.set({ duplicateHighlighterEnabled: duplicateHighlighterToggle.checked }, () => {
                    showStatus('Settings saved!');
                });
            });
        }

        function updateAggressiveUI() {
            if (linkifyToggle.checked) {
                aggressiveContainer.style.display = 'flex';
            } else {
                aggressiveContainer.style.display = 'none';
            }
        }
    }

    // === Exclusion Filters Section ===
    // Load saved filters
    chrome.storage.sync.get(['exclusionFilters', 'linkTextExclusionFilters', 'disabledDomains'], (result) => {
        exclusionFilters = result.exclusionFilters || [];
        linkTextExclusionFilters = result.linkTextExclusionFilters || [];
        disabledDomains = result.disabledDomains || [];
        renderUrlFilterList();
        renderLinkTextFilterList();
        renderDisabledDomainsList();
    });

    // === URL Filters Section ===
    if (urlFilterInput && addUrlFilterBtn && urlFilterList) {
        addUrlFilterBtn.addEventListener('click', addUrlFilter);

        // Add filter on Enter key
        urlFilterInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                addUrlFilter();
            }
        });

        // Clear all URL filters
        if (clearAllUrlFiltersBtn) {
            clearAllUrlFiltersBtn.addEventListener('click', () => {
                exclusionFilters = [];
                saveUrlFilters();
                renderUrlFilterList();
                showStatus('All filters cleared!');
            });
        }
    }

    // === Link Text Filters Section ===
    if (linkTextFilterInput && addLinkTextFilterBtn && linkTextFilterList) {
        addLinkTextFilterBtn.addEventListener('click', addLinkTextFilter);

        linkTextFilterInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                addLinkTextFilter();
            }
        });

        if (clearAllLinkTextFiltersBtn) {
            clearAllLinkTextFiltersBtn.addEventListener('click', () => {
                linkTextExclusionFilters = [];
                saveLinkTextFilters();
                renderLinkTextFilterList();
                showStatus('All link text filters cleared!');
            });
        }
    }

    // === Disabled Domains Section ===
    if (disabledDomainInput && addDisabledDomainBtn && disabledDomainsList) {
        addDisabledDomainBtn.addEventListener('click', addDisabledDomain);
        disabledDomainInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                addDisabledDomain();
            }
        });
    }

    /**
     * Adds a new disabled domain
     */
    function addDisabledDomain() {
        const value = disabledDomainInput.value.trim();
        if (!value) {
            showStatus('Please enter a domain', true);
            return;
        }

        if (disabledDomains.includes(value)) {
            showStatus('Domain already in blocklist', true);
            return;
        }

        disabledDomains.push(value);
        saveDisabledDomains();
        renderDisabledDomainsList();
        disabledDomainInput.value = '';
        showStatus('Domain added to blocklist!');
    }

    /**
     * Removes a disabled domain at the specified index
     * @param {number} index
     */
    function removeDisabledDomain(index) {
        disabledDomains.splice(index, 1);
        saveDisabledDomains();
        renderDisabledDomainsList();
        showStatus('Domain removed from blocklist!');
    }

    /**
     * Saves disabled domains to storage
     */
    function saveDisabledDomains() {
        chrome.storage.sync.set({ disabledDomains: disabledDomains });
    }

    /**
     * Renders the disabled domains list
     */
    function renderDisabledDomainsList() {
        if (!disabledDomainsList) return;

        disabledDomainsList.innerHTML = '';

        disabledDomains.forEach((domain, index) => {
            const li = document.createElement('li');
            li.className = 'filter-tag'; // Reuse filter-tag style

            const span = document.createElement('span');
            span.textContent = domain;

            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete-btn';
            deleteBtn.innerHTML = '×';
            deleteBtn.title = 'Remove domain';
            deleteBtn.addEventListener('click', () => removeDisabledDomain(index));

            li.appendChild(span);
            li.appendChild(deleteBtn);
            disabledDomainsList.appendChild(li);
        });
    }

    /**
     * Adds a new URL filter from the input field
     */
    function addUrlFilter() {
        const value = urlFilterInput.value.trim();
        if (!value) {
            showStatus('Please enter a URL filter pattern', true);
            return;
        }

        // Check for duplicates
        if (exclusionFilters.includes(value)) {
            showStatus('Filter already exists', true);
            return;
        }

        exclusionFilters.push(value);
        saveUrlFilters();
        renderUrlFilterList();
        urlFilterInput.value = '';
        showStatus('Filter added!');
    }

    /**
     * Removes a URL filter at the specified index
     * @param {number} index - Index of filter to remove
     */
    function removeUrlFilter(index) {
        exclusionFilters.splice(index, 1);
        saveUrlFilters();
        renderUrlFilterList();
        showStatus('Filter removed!');
    }

    /**
     * Saves the current URL filters to chrome.storage.sync
     */
    function saveUrlFilters() {
        chrome.storage.sync.set({ exclusionFilters: exclusionFilters });
    }

    /**
     * Renders the URL filter list UI
     */
    function renderUrlFilterList() {
        if (!urlFilterList) return;

        urlFilterList.innerHTML = '';

        exclusionFilters.forEach((filter, index) => {
            const li = document.createElement('li');
            li.className = 'filter-tag';

            const span = document.createElement('span');
            span.textContent = filter;

            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete-btn';
            deleteBtn.innerHTML = '×';
            deleteBtn.title = 'Remove filter';
            deleteBtn.addEventListener('click', () => removeUrlFilter(index));

            li.appendChild(span);
            li.appendChild(deleteBtn);
            urlFilterList.appendChild(li);
        });

        if (clearUrlFiltersContainer) {
            clearUrlFiltersContainer.style.display = exclusionFilters.length > 0 ? 'block' : 'none';
        }
    }

    /**
     * Adds a new link text filter from the input field
     */
    function addLinkTextFilter() {
        const value = linkTextFilterInput.value.trim();
        if (!value) {
            showStatus('Please enter a text filter pattern', true);
            return;
        }

        if (linkTextExclusionFilters.includes(value)) {
            showStatus('Text filter already exists', true);
            return;
        }

        linkTextExclusionFilters.push(value);
        saveLinkTextFilters();
        renderLinkTextFilterList();
        linkTextFilterInput.value = '';
        showStatus('Text filter added!');
    }

    /**
     * Removes a link text filter at the specified index
     * @param {number} index - Index of filter to remove
     */
    function removeLinkTextFilter(index) {
        linkTextExclusionFilters.splice(index, 1);
        saveLinkTextFilters();
        renderLinkTextFilterList();
        showStatus('Text filter removed!');
    }

    /**
     * Saves the current link text filters to chrome.storage.sync
     */
    function saveLinkTextFilters() {
        chrome.storage.sync.set({ linkTextExclusionFilters: linkTextExclusionFilters });
    }

    /**
     * Renders the link text filter list UI
     */
    function renderLinkTextFilterList() {
        if (!linkTextFilterList) return;

        linkTextFilterList.innerHTML = '';

        linkTextExclusionFilters.forEach((filter, index) => {
            const li = document.createElement('li');
            li.className = 'filter-tag';

            const span = document.createElement('span');
            span.textContent = filter;

            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete-btn';
            deleteBtn.innerHTML = '×';
            deleteBtn.title = 'Remove text filter';
            deleteBtn.addEventListener('click', () => removeLinkTextFilter(index));

            li.appendChild(span);
            li.appendChild(deleteBtn);
            linkTextFilterList.appendChild(li);
        });

        // Show/hide clear all button
        if (clearLinkTextFiltersContainer) {
            clearLinkTextFiltersContainer.style.display = linkTextExclusionFilters.length > 0 ? 'block' : 'none';
        }
    }

    /**
     * Shows a status message
     * @param {string} message - Message to display
     * @param {boolean} isError - Whether this is an error message
     */
    function showStatus(message, isError = false) {
        if (!status) return;
        status.textContent = message;
        status.style.color = isError ? '#d32f2f' : 'green';
        setTimeout(() => {
            status.textContent = '';
        }, 2000);
    }
});
```

## File: `css/options.css`
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    transition: var(--transition-standard);
}

body {
    font-family: var(--font-stack);
    background: var(--bg-color);
    color: var(--text-color);
    line-height: 1.6;
}

/* Adjust container for sidebar */
.container {
    max-width: 900px;
    margin: -0.5% auto;
    margin-left: calc(190px + (100% - 210px - 900px) / 2);
    /* Center content while accounting for smaller sidebar */
    padding: 3%;
    animation: fadeIn 0.8s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

h1 {
    color: var(--primary-color);
    text-align: center;
    margin-bottom: 2rem;
    font-size: 2.5rem;
    animation: pulseAndGlow 3s ease-in-out infinite;
}

@keyframes pulseAndGlow {

    0%,
    100% {
        transform: scale(1);
        text-shadow: 0 0 5px rgba(33, 150, 243, 0.1);
    }

    50% {
        transform: scale(1.05);
        text-shadow: 0 0 20px rgba(33, 150, 243, 0.5);
    }
}

@keyframes slideDown {
    from {
        transform: translateY(-50px);
        opacity: 0;
    }

    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.card {
    background: white;
    border-radius: 10px;
    padding: 4%;
    margin-bottom: 4%;
    box-shadow: var(--shadow-standard);
    transform: translateY(0);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-hover);
}

.instructions {
    background: linear-gradient(135deg, #f6f8fa 0%, #ffffff 100%);
    position: relative;
}

.instructions h2 {
    color: var(--primary-color);
    margin-bottom: 1rem;
}

.instructions-list {
    list-style: none;
    padding: 0;
    margin: 2rem 0;
}

.instructions-list li {
    position: relative;
    padding-left: 1.5rem;
    margin-bottom: 1rem;
    color: #666;
    line-height: 1.5;
    display: flex;
    align-items: center;
}

.instructions-list li::before {
    content: "\2192";
    position: absolute;
    left: 0;
    color: var(--primary-color);
    font-size: 1.2rem;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
    display: flex;
    align-items: center;
    height: 100%;
}

.rate-button {
    position: absolute;
    top: 1rem;
    right: 1rem;
    padding: 0.5rem 1rem;
    background: #FF9800;
    color: white;
    border: none;
    border-radius: 20px;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.rate-button:hover {
    background: #F57C00;
    transform: scale(1.05);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.action-button {
    display: block;
    width: 100%;
    padding: 1rem;
    background: var(--primary-color);
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1.1rem;
    cursor: pointer;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: all 0.3s ease;
}

.action-button:hover {
    background: var(--secondary-color);
    animation: magic-pulse 1s ease-in-out infinite;
    box-shadow: 0 0 15px var(--primary-color);
}

@keyframes magic-pulse {
    0% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.05);
    }

    100% {
        transform: scale(1);
    }
}

/* Modal Styles */
.modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(4px);
    justify-content: center;
    align-items: center;
    z-index: 1000;
    animation: fadeIn 0.3s ease;
}

.modal.active {
    display: flex;
}

.modal-content {
    background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
    border-radius: 16px;
    width: 90%;
    max-width: 580px;
    max-height: 85vh;
    position: relative;
    animation: slideIn 0.3s ease;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.25), 0 0 0 1px rgba(255, 255, 255, 0.1);
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

@keyframes slideIn {
    from {
        transform: translateY(-30px) scale(0.95);
        opacity: 0;
    }

    to {
        transform: translateY(0) scale(1);
        opacity: 1;
    }
}

/* Modal Header */
.modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1.5rem;
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
    flex-shrink: 0;
}

.modal-header h2 {
    margin: 0;
    font-size: 1.25rem;
    font-weight: 600;
    letter-spacing: 0.3px;
}

.modal-close {
    background: rgba(255, 255, 255, 0.2);
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
    line-height: 1;
}

.modal-close:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: scale(1.1);
}

/* Modal Body - Scrollable */
.modal-body {
    flex: 1;
    overflow-y: auto;
    padding: 1rem 1.5rem;
    scrollbar-width: thin;
    scrollbar-color: var(--primary-color) transparent;
}

.modal-body::-webkit-scrollbar {
    width: 6px;
}

.modal-body::-webkit-scrollbar-track {
    background: transparent;
}

.modal-body::-webkit-scrollbar-thumb {
    background-color: var(--primary-color);
    border-radius: 3px;
}

/* Modal Sections */
.modal-section {
    background: rgba(255, 255, 255, 0.7);
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 0.75rem;
    border: 1px solid rgba(0, 0, 0, 0.06);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.modal-section:last-child {
    margin-bottom: 0;
}

/* Section Header with Icon and Badge */
.section-header {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
}

.section-icon {
    font-size: 1.1rem;
}

.section-header h3 {
    color: var(--text-color);
    font-size: 1rem;
    font-weight: 600;
    margin: 0;
    flex-grow: 1;
}

.section-badge {
    font-size: 0.65rem;
    padding: 2px 8px;
    border-radius: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.required-badge {
    background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
    color: #1565c0;
}

.optional-badge {
    background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%);
    color: #7b1fa2;
}

.section-description {
    color: #666;
    font-size: 0.8rem;
    margin: 0 0 0.75rem 0;
}

/* Two Column Grid Layout */
.two-column-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
}

/* Compact Input Groups */
.input-group {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
}

.input-group.compact {
    margin-bottom: 0;
}

.input-group label {
    font-size: 0.8rem;
    font-weight: 500;
    color: #555;
    text-align: left;
    min-width: auto;
}

/* Inline inputs for border controls */
.inline-inputs {
    display: flex;
    gap: 0.5rem;
    align-items: center;
}

.small-input {
    width: 55px !important;
    min-width: 55px !important;
}

/* Key Select Styling */
.key-select {
    padding: 0.5rem 0.75rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.85rem;
    background: white;
    cursor: pointer;
    transition: all 0.2s ease;
    width: 100%;
}

.key-select:focus {
    border-color: var(--primary-color);
    outline: none;
    box-shadow: 0 0 0 3px rgba(33, 150, 243, 0.15);
}

.key-select.required {
    border-left: 3px solid var(--primary-color);
}

.compact-select {
    width: 80px;
    min-width: 80px;
}

/* Color Picker */
.color-picker {
    -webkit-appearance: none;
    appearance: none;
    width: 100%;
    height: 36px;
    padding: 2px;
    border: 1px solid #ddd;
    border-radius: 8px;
    cursor: pointer;
    background: white;
}

.color-picker::-webkit-color-swatch-wrapper {
    padding: 2px;
}

.color-picker::-webkit-color-swatch {
    border: none;
    border-radius: 5px;
}

/* Collapsible Section */
.collapsible-section {
    padding: 0;
    overflow: hidden;
}

.collapsible-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem;
    cursor: pointer;
    transition: background 0.2s ease;
    border-radius: 12px;
}

.collapsible-header:hover {
    background: rgba(33, 150, 243, 0.05);
}

.collapsible-header .section-header {
    margin-bottom: 0;
}

.collapse-icon {
    font-size: 0.75rem;
    color: #888;
    transition: transform 0.3s ease;
}

.collapsible-section.collapsed .collapse-icon {
    transform: rotate(-90deg);
}

.collapsible-content {
    padding: 0 1rem 1rem 1rem;
    max-height: 400px;
    overflow: visible;
    transition: all 0.3s ease;
}

.collapsible-section.collapsed .collapsible-content {
    max-height: 0;
    padding-top: 0;
    padding-bottom: 0;
}

/* Advanced Options Grid */
.advanced-grid {
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
}

.advanced-option-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.5rem 0.75rem;
    background: rgba(0, 0, 0, 0.02);
    border-radius: 8px;
    gap: 0.75rem;
}

.option-info {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    flex: 1;
}

.option-info label {
    font-size: 0.8rem;
    color: #444;
    font-weight: 500;
}

/* Delay Control */
.delay-control {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.delay-control input[type="range"] {
    width: 100px;
    height: 4px;
    appearance: none;
    background: #ddd;
    border-radius: 2px;
    cursor: pointer;
}

.delay-control input[type="range"]::-webkit-slider-thumb {
    appearance: none;
    width: 14px;
    height: 14px;
    background: var(--primary-color);
    border-radius: 50%;
    cursor: pointer;
}

.delay-control span {
    font-size: 0.75rem;
    color: #666;
    min-width: 24px;
}

/* Toggle Switch Styling */
.toggle-switch {
    position: relative;
    display: inline-block;
    width: 44px;
    height: 24px;
    flex-shrink: 0;
}

.toggle-switch input {
    opacity: 0;
    width: 0;
    height: 0;
}

.toggle-slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    transition: 0.3s ease;
    border-radius: 24px;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
}

.toggle-slider:before {
    position: absolute;
    content: "";
    height: 18px;
    width: 18px;
    left: 3px;
    bottom: 3px;
    background-color: white;
    transition: 0.3s ease;
    border-radius: 50%;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.toggle-switch input:checked + .toggle-slider {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1), 0 0 8px rgba(33, 150, 243, 0.3);
}

.toggle-switch input:focus + .toggle-slider {
    box-shadow: 0 0 0 3px rgba(33, 150, 243, 0.2);
}

.toggle-switch input:checked + .toggle-slider:before {
    transform: translateX(20px);
}

.toggle-switch:hover .toggle-slider {
    background-color: #bbb;
}

.toggle-switch:hover input:checked + .toggle-slider {
    background: linear-gradient(135deg, #1e88e5 0%, #1565c0 100%);
}

/* Modal Footer */
.modal-footer {
    display: flex;
    justify-content: flex-end;
    gap: 0.75rem;
    padding: 1rem 1.5rem;
    background: rgba(0, 0, 0, 0.02);
    border-top: 1px solid rgba(0, 0, 0, 0.06);
    flex-shrink: 0;
}

.modal-button {
    padding: 0.6rem 1.5rem;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.2s ease;
}

.save-button {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
    box-shadow: 0 2px 8px rgba(33, 150, 243, 0.3);
}

.save-button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(33, 150, 243, 0.4);
}

.cancel-button {
    background: #e8e8e8;
    color: #555;
}

.cancel-button:hover {
    background: #d8d8d8;
}

/* Error Messages */
.error-message {
    color: #dc3545;
    font-size: 0.75rem;
    margin-top: 0.25rem;
    display: none;
}

.error-message.visible {
    display: block;
}

/* Warning Messages */
.warning-message {
    color: #856404;
    background-color: #fff3cd;
    border: 1px solid #ffeeba;
    font-size: 0.75rem;
    margin-top: 0.5rem;
    padding: 0.5rem 0.75rem;
    border-radius: 6px;
    display: none;
}

.warning-message.visible {
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

.warning-icon {
    font-size: 0.9rem;
}

/* Tooltip Styles */
.smart-select-info {
    position: relative;
    display: inline-flex;
    align-items: center;
    color: var(--primary-color);
    cursor: help;
}

.smart-select-info::after {
    content: "?";
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 14px;
    height: 14px;
    border: 1px solid currentColor;
    border-radius: 50%;
    font-size: 9px;
    font-weight: bold;
}

.smart-select-info:hover .tooltip {
    visibility: visible;
    opacity: 1;
}

.tooltip {
    visibility: hidden;
    position: fixed;
    padding: 6px 10px;
    background: #333;
    color: white;
    border-radius: 6px;
    font-size: 11px;
    line-height: 1.4;
    opacity: 0;
    transition: opacity 0.2s ease, visibility 0.2s ease;
    z-index: 10000;
    width: max-content;
    max-width: 250px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    white-space: normal;
    pointer-events: none;
}

.tooltip::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%);
    border-width: 5px;
    border-style: solid;
    border-color: #333 transparent transparent transparent;
}

/* Responsive adjustments */
@media (max-width: 600px) {
    .two-column-grid {
        grid-template-columns: 1fr;
    }

    .modal-content {
        max-height: 90vh;
        margin: 1rem;
    }
}

/* Saved Action Cards */
.saved-action {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 5px;
    margin-bottom: 1rem;
    border-left: 4px solid #ddd;
}

.action-details {
    flex-grow: 1;
}

.action-combination {
    font-weight: bold;
    color: var(--primary-color);
    margin-bottom: 0.5rem;
}

.action-features {
    color: #666;
    font-size: 0.9rem;
}

.action-feature {
    background-color: #e3f2fd;
    color: #1565c0;
    padding: 2px 8px;
    border-radius: 12px;
    font-size: 12px;
    margin-right: 4px;
}

.delete-action {
    background: none;
    border: none;
    color: #dc3545;
    cursor: pointer;
    padding: 0.5rem;
    font-size: 1.2rem;
    transition: color 0.3s ease;
}

.delete-action:hover {
    color: #c82333;
}

.action-buttons {
    display: flex;
    gap: 0.5rem;
}

.edit-action {
    background: none;
    border: none;
    color: var(--primary-color);
    cursor: pointer;
    padding: 0.5rem;
    font-size: 1.2rem;
    transition: color 0.3s ease;
}

.edit-action:hover {
    color: var(--secondary-color);
}

#savedActions {
    margin-bottom: 1rem;
}

.key-select.required {
    border-left: 3px solid #dc3545;
}



.instructions-container {
    padding: 2rem;
}

.instructions-split {
    display: flex;
    gap: 2rem;
    justify-content: space-between;
}

.instructions-panel {
    flex: 1;
    padding: 1.5rem;
    background: linear-gradient(135deg, #f6f8fa 0%, #ffffff 100%);
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.instructions-panel h2 {
    color: var(--primary-color);
    margin-bottom: 1.5rem;
    font-size: 1.4rem;
}

/* Responsive design */
@media (max-width: 768px) {
    .instructions-split {
        flex-direction: column;
    }

    .container {
        margin-left: 180px;
    }
}

@media (max-width: 576px) {
    .container {
        margin-left: 66px;
    }
}

.pin-button {
    background: var(--primary-color);
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.pin-button:hover {
    background: var(--secondary-color);
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.rate-card {
    background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%);
    color: white;
    margin-bottom: 1.5rem;
    text-align: center;
    padding: 1rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
    border-radius: 12px;
}

.rate-content h3 {
    font-size: 1.2rem;
    margin-bottom: 0.3rem;
}

.rate-content p {
    opacity: 0.9;
    margin-bottom: 0.8rem;
    font-size: 0.9rem;
}

.rate-extension-button {
    background: white;
    color: #2196F3;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.star-icons {
    color: #FFD700;
    letter-spacing: 2px;
    font-size: 16px;
    display: inline-flex;
    align-items: center;
    text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.1);
}

/* Format Preview Styles */
.format-preview-container {
    margin-top: 1rem;
    padding-top: 0.75rem;
    border-top: 1px dashed rgba(0, 0, 0, 0.1);
}

.preview-label {
    display: block;
    font-size: 0.75rem;
    font-weight: 600;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.5rem;
}

.format-preview {
    background: #1e1e1e;
    border-radius: 8px;
    padding: 0.75rem 1rem;
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    font-size: 0.75rem;
    line-height: 1.5;
    color: #d4d4d4;
    overflow-x: auto;
    white-space: pre-wrap;
    word-break: break-all;
    max-height: 120px;
    overflow-y: auto;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}

.format-preview .preview-title {
    color: #4ec9b0;
}

.format-preview .preview-url {
    color: #ce9178;
}

.format-preview .preview-separator {
    color: #6a9955;
    opacity: 0.7;
}
/* =========================================================================
   Popup Customization Card
   ========================================================================= */

.popup-config-card {
    margin-bottom: 2rem;
}

.popup-config-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.popup-config-header h2 {
    margin: 0;
    font-size: 1.25rem;
    color: var(--color-text);
}

.reset-button {
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
    background: var(--button-secondary-bg);
    color: var(--color-text);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-sm);
    cursor: pointer;
    transition: all 0.2s ease;
}

.reset-button:hover {
    background: var(--color-surface-alt);
    border-color: var(--color-text-muted);
}

.config-description {
    color: var(--color-text-muted);
    font-size: 0.9375rem;
    margin-bottom: 1.5rem;
}

.config-warning {
    color: #f59e0b;
    font-size: 0.875rem;
    margin-top: 1rem;
    margin-bottom: 0;
}

/* Button List */
.popup-button-list {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

.popup-button-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    background: var(--color-surface-alt);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    cursor: move;
    transition: all 0.2s ease;
}

.popup-button-item:hover {
    background: var(--color-surface);
    box-shadow: var(--shadow-sm);
}

.popup-button-item.dragging {
    opacity: 0.5;
    transform: scale(0.98);
}

.popup-button-item.drag-over {
    border-color: var(--color-primary);
    box-shadow: var(--shadow-md);
}

/* Drag Handle */
.drag-handle {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    color: var(--color-text-muted);
    cursor: grab;
    flex-shrink: 0;
}

.drag-handle:active {
    cursor: grabbing;
}

.drag-handle svg {
    width: 16px;
    height: 16px;
}

/* Button Preview */
.button-preview {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    flex: 1;
}

.button-icon-preview {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.button-icon-preview svg {
    width: 18px;
    height: 18px;
    color: white;
}

/* Color variants */
.button-icon-preview.blue {
    background: var(--button-primary-bg);
    box-shadow: 0 4px 15px rgba(33, 150, 243, 0.4);
}

.button-icon-preview.purple {
    background: var(--button-purple-bg);
    box-shadow: 0 4px 15px rgba(156, 39, 176, 0.4);
}

.button-icon-preview.orange {
    background: var(--button-orange-bg);
    box-shadow: 0 4px 15px rgba(255, 152, 0, 0.4);
}

.button-icon-preview.premium {
    background: linear-gradient(135deg, #a855f7, #6366f1);
    box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4);
}

/* Button Info */
.button-info {
    flex: 1;
}

.button-info-title {
    font-size: 0.9375rem;
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: 0.125rem;
}

.button-info-subtitle {
    font-size: 0.8125rem;
    color: var(--color-text-muted);
}

.pro-badge-mini {
    display: inline-block;
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    color: #000;
    font-size: 0.6875rem;
    font-weight: 800;
    padding: 0.125rem 0.375rem;
    border-radius: 4px;
    letter-spacing: 0.05em;
    margin-left: 0.5rem;
}

/* Toggle Switch */
.button-toggle {
    flex-shrink: 0;
}

/* Disabled state */
.popup-button-item.disabled {
    opacity: 0.5;
}

.popup-button-item.disabled .button-preview {
    pointer-events: none;
}

```

## File: `css/variables.css`
```css
:root {
    /* Colors */
    --primary-color: #2196F3;
    --secondary-color: #1976D2;
    --text-color: #333;
    --bg-color: #f5f5f5;
    --success-color: #4CAF50;
    --warning-color: #FF9800;
    --error-color: #dc3545;

    /* Gradients */
    --sidebar-bg: linear-gradient(145deg, #1976D2 0%, #2196F3 90%);
    --button-primary-bg: linear-gradient(135deg, #2196F3, #1976D2);
    --button-success-bg: linear-gradient(135deg, #4CAF50, #388E3C);
    --button-purple-bg: linear-gradient(135deg, #9C27B0, #7B1FA2);
    --button-orange-bg: linear-gradient(135deg, #FF9800, #F57C00);
    --body-bg-gradient: linear-gradient(145deg, #ffffff, #f0f0f0);

    /* Fonts */
    --font-stack: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;

    /* Shadows */
    --shadow-standard: 0 4px 6px rgba(0, 0, 0, 0.1);
    --shadow-hover: 0 6px 12px rgba(0, 0, 0, 0.15);
    --shadow-button: 0 2px 4px rgba(33, 150, 243, 0.2);
    --shadow-button-hover: 0 4px 8px rgba(33, 150, 243, 0.3);

    /* Transitions */
    --transition-standard: all 0.3s ease;
}
```

## File: `css/components/footer.css`
```css
/**
 * Footer Component Styles
 * Modern Grid Layout
 */

.footer {
    width: 100%;
    background-color: #f8f9fa; /* Light gray background to separate from content */
    border-top: 1px solid rgba(0, 0, 0, 0.05);
    margin-top: 4rem;
    padding: 3rem 0;
    color: var(--text-color, #333);
    font-size: 14px;
}

/* Container for the grid */
.footer-content {
    display: grid;
    grid-template-columns: 1.5fr 1fr 1fr;
    gap: 3rem;
    max-width: 1000px; /* Restrain width for readability */
    margin: 0 auto;
    padding: 0 2rem;
}

/* Headings */
.footer-heading {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #64748b; /* Slate-500 */
    font-weight: 700;
    margin-bottom: 1.2rem;
}

/* --- Brand Column --- */
.brand-col {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding-right: 2rem;
}

.footer-brand {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.footer-logo {
    width: 32px;
    height: 32px;
}

.brand-name {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--primary-color, #2196F3);
    letter-spacing: -0.02em;
}

.brand-desc {
    color: #666;
    line-height: 1.6;
    font-size: 0.95rem;
    max-width: 300px;
    margin: 0;
}

.footer-meta {
    margin-top: auto; /* Push to bottom of flex container if height is fixed */
    padding-top: 1rem;
    font-size: 0.85rem;
    color: #999;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.dot {
    font-size: 0.6rem;
    opacity: 0.5;
}

/* --- Community Column --- */
.community-col {
    display: flex;
    flex-direction: column;
}

.contributors-wrapper {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
}

.contributor-tag {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 10px;
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    font-size: 0.85rem;
    color: #475569;
    text-decoration: none;
    transition: all 0.2s ease;
}

.contributor-tag svg {
    width: 14px;
    height: 14px;
    fill: currentColor;
    opacity: 0.7;
}

.contributor-tag:hover {
    border-color: var(--primary-color, #2196F3);
    color: var(--primary-color, #2196F3);
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.github-cta {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 600;
    color: var(--text-color, #333);
    text-decoration: none;
    padding: 0.5rem 0;
    transition: color 0.2s ease;
}

.github-cta svg {
    width: 18px;
    height: 18px;
    fill: currentColor;
}

.github-cta:hover {
    color: var(--primary-color, #2196F3);
}

/* --- Support Column --- */
.support-col {
    display: flex;
    flex-direction: column;
}

.support-text {
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 1rem;
    line-height: 1.5;
}

.support-actions {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
}

.footer-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    padding: 0.6rem 1rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
    transition: all 0.2s ease;
    border: 1px solid transparent;
}

.footer-btn svg {
    height: 24px;
    width: auto;
    fill: currentColor;
}

/* PayPal Button */
.paypal-button {
    background-color: white;
    border: 1px solid #e2e8f0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.paypal-button:hover {
    background-color: #f8fafc;
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Revolut Button */
.revolut-button {
    background-color: white;
    border: 1px solid #e2e8f0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.revolut-button:hover {
    background-color: #f8fafc;
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.revolut-button svg {
    /* Use default size from .footer-btn svg */
}

/* General Links */
.text-link {
    color: inherit;
    text-decoration: none;
    border-bottom: 1px dotted #999;
    transition: border-color 0.2s ease, color 0.2s ease;
}

.text-link:hover {
    color: var(--primary-color, #2196F3);
    border-bottom-color: var(--primary-color, #2196F3);
}

/* Responsive Design */
@media (max-width: 768px) {
    .footer-content {
        grid-template-columns: 1fr;
        gap: 2.5rem;
    }

    .brand-col {
        padding-right: 0;
        align-items: center;
        text-align: center;
    }

    .footer-brand {
        justify-content: center;
    }

    .footer-heading {
        text-align: center;
    }

    .contributors-wrapper {
        justify-content: center;
    }

    .github-cta {
        margin: 0 auto;
    }

    .support-col {
        text-align: center;
    }
}
```

## File: `css/components/sidebar.css`
```css
/* Sidebar Styles */
.sidebar {
    position: fixed;
    left: 16px;
    top: 50%;
    transform: translateY(-50%);
    width: 180px;
    height: 50%;
    background: var(--sidebar-bg);
    color: white;
    padding: 16px 0;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
    z-index: 100;
    transition: var(--transition-standard);
    overflow-y: auto;
    border-radius: 10px;
}

.sidebar-header {
    display: flex;
    align-items: center;
    padding: 0 16px 16px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 16px;
}

.sidebar-logo {
    width: 28px;
    height: 28px;
    margin-right: 8px;
    border-radius: 6px;
}

.sidebar-header h2 {
    margin: 0;
    font-size: 16px;
    font-weight: 600;
    color: white;
    letter-spacing: 0.3px;
}

.sidebar-nav {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.sidebar-link {
    display: flex;
    align-items: center;
    padding: 10px 16px;
    color: rgba(255, 255, 255, 0.85);
    text-decoration: none;
    transition: all 0.2s ease;
    border-left: 2px solid transparent;
    gap: 8px;
    font-size: 14px;
}

.sidebar-link:hover {
    background: rgba(255, 255, 255, 0.1);
    color: white;
}

.sidebar-link.active {
    background: rgba(255, 255, 255, 0.15);
    color: white;
    border-left-color: white;
}

.sidebar-link svg {
    opacity: 0.8;
    transition: all 0.2s ease;
}

.sidebar-link:hover svg,
.sidebar-link.active svg {
    opacity: 1;
}

/* Responsive design for sidebar */
@media (max-width: 768px) {
    .sidebar {
        width: 160px;
        left: 12px;
        top: 50%;
        transform: translateY(-50%);
        height: 80%;
    }
}

@media (max-width: 576px) {
    .sidebar {
        width: 50px;
        overflow: hidden;
        left: 8px;
        top: 8px;
        height: calc(100% - 16px);
    }

    .sidebar-header h2 {
        display: none;
    }

    .sidebar-link span {
        display: none;
    }

    .sidebar-link {
        justify-content: center;
        padding: 12px 0;
    }

    .sidebar-logo {
        margin-right: 0;
        width: 24px;
        height: 24px;
    }

    .sidebar-header {
        justify-content: center;
        padding-bottom: 12px;
    }
}
```

## File: `js/ExtPay.js`
```javascript
'use strict';

	var commonjsGlobal = typeof globalThis !== 'undefined' ? globalThis : typeof window !== 'undefined' ? window : typeof global !== 'undefined' ? global : typeof self !== 'undefined' ? self : {};

	function createCommonjsModule(fn) {
		var module = { exports: {} };
		return fn(module, module.exports), module.exports;
	}

	var browserPolyfill = createCommonjsModule(function (module, exports) {
		(function (global, factory) {
			{
				factory(module);
			}
		})(typeof globalThis !== "undefined" ? globalThis : typeof self !== "undefined" ? self : commonjsGlobal, function (module) {

			if (typeof browser === "undefined" || Object.getPrototypeOf(browser) !== Object.prototype) {
				const CHROME_SEND_MESSAGE_CALLBACK_NO_RESPONSE_MESSAGE = "The message port closed before a response was received.";
				const SEND_RESPONSE_DEPRECATION_WARNING = "Returning a Promise is the preferred way to send a reply from an onMessage/onMessageExternal listener, as the sendResponse will be removed from the specs (See https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage)";

				const wrapAPIs = extensionAPIs => {
					const apiMetadata = {
						"alarms": {
							"clear": { "minArgs": 0, "maxArgs": 1 },
							"clearAll": { "minArgs": 0, "maxArgs": 0 },
							"get": { "minArgs": 0, "maxArgs": 1 },
							"getAll": { "minArgs": 0, "maxArgs": 0 }
						},
						"bookmarks": {
							"create": { "minArgs": 1, "maxArgs": 1 },
							"get": { "minArgs": 1, "maxArgs": 1 },
							"getChildren": { "minArgs": 1, "maxArgs": 1 },
							"getRecent": { "minArgs": 1, "maxArgs": 1 },
							"getSubTree": { "minArgs": 1, "maxArgs": 1 },
							"getTree": { "minArgs": 0, "maxArgs": 0 },
							"move": { "minArgs": 2, "maxArgs": 2 },
							"remove": { "minArgs": 1, "maxArgs": 1 },
							"removeTree": { "minArgs": 1, "maxArgs": 1 },
							"search": { "minArgs": 1, "maxArgs": 1 },
							"update": { "minArgs": 2, "maxArgs": 2 }
						},
						"browserAction": {
							"disable": { "minArgs": 0, "maxArgs": 1, "fallbackToNoCallback": true },
							"enable": { "minArgs": 0, "maxArgs": 1, "fallbackToNoCallback": true },
							"getBadgeBackgroundColor": { "minArgs": 1, "maxArgs": 1 },
							"getBadgeText": { "minArgs": 1, "maxArgs": 1 },
							"getPopup": { "minArgs": 1, "maxArgs": 1 },
							"getTitle": { "minArgs": 1, "maxArgs": 1 },
							"openPopup": { "minArgs": 0, "maxArgs": 0 },
							"setBadgeBackgroundColor": { "minArgs": 1, "maxArgs": 1, "fallbackToNoCallback": true },
							"setBadgeText": { "minArgs": 1, "maxArgs": 1, "fallbackToNoCallback": true },
							"setIcon": { "minArgs": 1, "maxArgs": 1 },
							"setPopup": { "minArgs": 1, "maxArgs": 1, "fallbackToNoCallback": true },
							"setTitle": { "minArgs": 1, "maxArgs": 1, "fallbackToNoCallback": true }
						},
						"browsingData": {
							"remove": { "minArgs": 2, "maxArgs": 2 },
							"removeCache": { "minArgs": 1, "maxArgs": 1 },
							"removeCookies": { "minArgs": 1, "maxArgs": 1 },
							"removeDownloads": { "minArgs": 1, "maxArgs": 1 },
							"removeFormData": { "minArgs": 1, "maxArgs": 1 },
							"removeHistory": { "minArgs": 1, "maxArgs": 1 },
							"removeLocalStorage": { "minArgs": 1, "maxArgs": 1 },
							"removePasswords": { "minArgs": 1, "maxArgs": 1 },
							"removePluginData": { "minArgs": 1, "maxArgs": 1 },
							"settings": { "minArgs": 0, "maxArgs": 0 }
						},
						"commands": {
							"getAll": { "minArgs": 0, "maxArgs": 0 }
						},
						"contextMenus": {
							"remove": { "minArgs": 1, "maxArgs": 1 },
							"removeAll": { "minArgs": 0, "maxArgs": 0 },
							"update": { "minArgs": 2, "maxArgs": 2 }
						},
						"cookies": {
							"get": { "minArgs": 1, "maxArgs": 1 },
							"getAll": { "minArgs": 1, "maxArgs": 1 },
							"getAllCookieStores": { "minArgs": 0, "maxArgs": 0 },
							"remove": { "minArgs": 1, "maxArgs": 1 },
							"set": { "minArgs": 1, "maxArgs": 1 }
						},
						"devtools": {
							"inspectedWindow": {
								"eval": { "minArgs": 1, "maxArgs": 2, "singleCallbackArg": false }
							},
							"panels": {
								"create": { "minArgs": 3, "maxArgs": 3, "singleCallbackArg": true },
								"elements": {
									"createSidebarPane": { "minArgs": 1, "maxArgs": 1 }
								}
							}
						},
						"downloads": {
							"cancel": { "minArgs": 1, "maxArgs": 1 },
							"download": { "minArgs": 1, "maxArgs": 1 },
							"erase": { "minArgs": 1, "maxArgs": 1 },
							"getFileIcon": { "minArgs": 1, "maxArgs": 2 },
							"open": { "minArgs": 1, "maxArgs": 1, "fallbackToNoCallback": true },
							"pause": { "minArgs": 1, "maxArgs": 1 },
							"removeFile": { "minArgs": 1, "maxArgs": 1 },
							"resume": { "minArgs": 1, "maxArgs": 1 },
							"search": { "minArgs": 1, "maxArgs": 1 },
							"show": { "minArgs": 1, "maxArgs": 1, "fallbackToNoCallback": true }
						},
						"extension": {
							"isAllowedFileSchemeAccess": { "minArgs": 0, "maxArgs": 0 },
							"isAllowedIncognitoAccess": { "minArgs": 0, "maxArgs": 0 }
						},
						"history": {
							"addUrl": { "minArgs": 1, "maxArgs": 1 },
							"deleteAll": { "minArgs": 0, "maxArgs": 0 },
							"deleteRange": { "minArgs": 1, "maxArgs": 1 },
							"deleteUrl": { "minArgs": 1, "maxArgs": 1 },
							"getVisits": { "minArgs": 1, "maxArgs": 1 },
							"search": { "minArgs": 1, "maxArgs": 1 }
						},
						"i18n": {
							"detectLanguage": { "minArgs": 1, "maxArgs": 1 },
							"getAcceptLanguages": { "minArgs": 0, "maxArgs": 0 }
						},
						"identity": {
							"launchWebAuthFlow": { "minArgs": 1, "maxArgs": 1 }
						},
						"idle": {
							"queryState": { "minArgs": 1, "maxArgs": 1 }
						},
						"management": {
							"get": { "minArgs": 1, "maxArgs": 1 },
							"getAll": { "minArgs": 0, "maxArgs": 0 },
							"getSelf": { "minArgs": 0, "maxArgs": 0 },
							"setEnabled": { "minArgs": 2, "maxArgs": 2 },
							"uninstallSelf": { "minArgs": 0, "maxArgs": 1 }
						},
						"notifications": {
							"clear": { "minArgs": 1, "maxArgs": 1 },
							"create": { "minArgs": 1, "maxArgs": 2 },
							"getAll": { "minArgs": 0, "maxArgs": 0 },
							"getPermissionLevel": { "minArgs": 0, "maxArgs": 0 },
							"update": { "minArgs": 2, "maxArgs": 2 }
						},
						"pageAction": {
							"getPopup": { "minArgs": 1, "maxArgs": 1 },
							"getTitle": { "minArgs": 1, "maxArgs": 1 },
							"hide": { "minArgs": 1, "maxArgs": 1, "fallbackToNoCallback": true },
							"setIcon": { "minArgs": 1, "maxArgs": 1 },
							"setPopup": { "minArgs": 1, "maxArgs": 1, "fallbackToNoCallback": true },
							"setTitle": { "minArgs": 1, "maxArgs": 1, "fallbackToNoCallback": true },
							"show": { "minArgs": 1, "maxArgs": 1, "fallbackToNoCallback": true }
						},
						"permissions": {
							"contains": { "minArgs": 1, "maxArgs": 1 },
							"getAll": { "minArgs": 0, "maxArgs": 0 },
							"remove": { "minArgs": 1, "maxArgs": 1 },
							"request": { "minArgs": 1, "maxArgs": 1 }
						},
						"runtime": {
							"getBackgroundPage": { "minArgs": 0, "maxArgs": 0 },
							"getPlatformInfo": { "minArgs": 0, "maxArgs": 0 },
							"openOptionsPage": { "minArgs": 0, "maxArgs": 0 },
							"requestUpdateCheck": { "minArgs": 0, "maxArgs": 0 },
							"sendMessage": { "minArgs": 1, "maxArgs": 3 },
							"sendNativeMessage": { "minArgs": 2, "maxArgs": 2 },
							"setUninstallURL": { "minArgs": 1, "maxArgs": 1 }
						},
						"sessions": {
							"getDevices": { "minArgs": 0, "maxArgs": 1 },
							"getRecentlyClosed": { "minArgs": 0, "maxArgs": 1 },
							"restore": { "minArgs": 0, "maxArgs": 1 }
						},
						"storage": {
							"local": {
								"clear": { "minArgs": 0, "maxArgs": 0 },
								"get": { "minArgs": 0, "maxArgs": 1 },
								"getBytesInUse": { "minArgs": 0, "maxArgs": 1 },
								"remove": { "minArgs": 1, "maxArgs": 1 },
								"set": { "minArgs": 1, "maxArgs": 1 }
							},
							"managed": {
								"get": { "minArgs": 0, "maxArgs": 1 },
								"getBytesInUse": { "minArgs": 0, "maxArgs": 1 }
							},
							"sync": {
								"clear": { "minArgs": 0, "maxArgs": 0 },
								"get": { "minArgs": 0, "maxArgs": 1 },
								"getBytesInUse": { "minArgs": 0, "maxArgs": 1 },
								"remove": { "minArgs": 1, "maxArgs": 1 },
								"set": { "minArgs": 1, "maxArgs": 1 }
							}
						},
						"tabs": {
							"captureVisibleTab": { "minArgs": 0, "maxArgs": 2 },
							"create": { "minArgs": 1, "maxArgs": 1 },
							"detectLanguage": { "minArgs": 0, "maxArgs": 1 },
							"discard": { "minArgs": 0, "maxArgs": 1 },
							"duplicate": { "minArgs": 1, "maxArgs": 1 },
							"executeScript": { "minArgs": 1, "maxArgs": 2 },
							"get": { "minArgs": 1, "maxArgs": 1 },
							"getCurrent": { "minArgs": 0, "maxArgs": 0 },
							"getZoom": { "minArgs": 0, "maxArgs": 1 },
							"getZoomSettings": { "minArgs": 0, "maxArgs": 1 },
							"goBack": { "minArgs": 0, "maxArgs": 1 },
							"goForward": { "minArgs": 0, "maxArgs": 1 },
							"highlight": { "minArgs": 1, "maxArgs": 1 },
							"insertCSS": { "minArgs": 1, "maxArgs": 2 },
							"move": { "minArgs": 2, "maxArgs": 2 },
							"query": { "minArgs": 1, "maxArgs": 1 },
							"reload": { "minArgs": 0, "maxArgs": 2 },
							"remove": { "minArgs": 1, "maxArgs": 1 },
							"removeCSS": { "minArgs": 1, "maxArgs": 2 },
							"sendMessage": { "minArgs": 2, "maxArgs": 3 },
							"setZoom": { "minArgs": 1, "maxArgs": 2 },
							"setZoomSettings": { "minArgs": 1, "maxArgs": 2 },
							"update": { "minArgs": 1, "maxArgs": 2 }
						},
						"topSites": {
							"get": { "minArgs": 0, "maxArgs": 0 }
						},
						"webNavigation": {
							"getAllFrames": { "minArgs": 1, "maxArgs": 1 },
							"getFrame": { "minArgs": 1, "maxArgs": 1 }
						},
						"webRequest": {
							"handlerBehaviorChanged": { "minArgs": 0, "maxArgs": 0 }
						},
						"windows": {
							"create": { "minArgs": 0, "maxArgs": 1 },
							"get": { "minArgs": 1, "maxArgs": 2 },
							"getAll": { "minArgs": 0, "maxArgs": 1 },
							"getCurrent": { "minArgs": 0, "maxArgs": 1 },
							"getLastFocused": { "minArgs": 0, "maxArgs": 1 },
							"remove": { "minArgs": 1, "maxArgs": 1 },
							"update": { "minArgs": 2, "maxArgs": 2 }
						}
					};

					if (Object.keys(apiMetadata).length === 0) {
						throw new Error("api-metadata.json has not been included in browser-polyfill");
					}

					class DefaultWeakMap extends WeakMap {
						constructor(createItem, items = undefined) {
							super(items);
							this.createItem = createItem;
						}

						get(key) {
							if (!this.has(key)) {
								this.set(key, this.createItem(key));
							}
							return super.get(key);
						}
					}

					const isThenable = value => {
						return value && typeof value === "object" && typeof value.then === "function";
					};

					const makeCallback = (promise, metadata) => {
						return (...callbackArgs) => {
							if (extensionAPIs.runtime.lastError) {
								promise.reject(extensionAPIs.runtime.lastError);
							} else if (metadata.singleCallbackArg || callbackArgs.length <= 1 && metadata.singleCallbackArg !== false) {
								promise.resolve(callbackArgs[0]);
							} else {
								promise.resolve(callbackArgs);
							}
						};
					};

					const pluralizeArguments = numArgs => numArgs == 1 ? "argument" : "arguments";

					const wrapAsyncFunction = (name, metadata) => {
						return function asyncFunctionWrapper(target, ...args) {
							if (args.length < metadata.minArgs) {
								throw new Error(`Expected at least ${metadata.minArgs} ${pluralizeArguments(metadata.minArgs)} for ${name}(), got ${args.length}`);
							}

							if (args.length > metadata.maxArgs) {
								throw new Error(`Expected at most ${metadata.maxArgs} ${pluralizeArguments(metadata.maxArgs)} for ${name}(), got ${args.length}`);
							}

							return new Promise((resolve, reject) => {
								if (metadata.fallbackToNoCallback) {
									try {
										target[name](...args, makeCallback({ resolve, reject }, metadata));
									} catch (cbError) {
										console.warn(`${name} API method doesn't seem to support the callback parameter, falling back to call it without a callback: `, cbError);
										target[name](...args);
										metadata.fallbackToNoCallback = false;
										metadata.noCallback = true;
										resolve();
									}
								} else if (metadata.noCallback) {
									target[name](...args);
									resolve();
								} else {
									target[name](...args, makeCallback({ resolve, reject }, metadata));
								}
							});
						};
					};

					const wrapMethod = (target, method, wrapper) => {
						return new Proxy(method, {
							apply(targetMethod, thisObj, args) {
								return wrapper.call(thisObj, target, ...args);
							}
						});
					};

					let hasOwnProperty = Function.call.bind(Object.prototype.hasOwnProperty);

					const wrapObject = (target, wrappers = {}, metadata = {}) => {
						let cache = Object.create(null);
						let handlers = {
							has(proxyTarget, prop) {
								return prop in target || prop in cache;
							},

							get(proxyTarget, prop, receiver) {
								if (prop in cache) {
									return cache[prop];
								}

								if (!(prop in target)) {
									return undefined;
								}

								let value = target[prop];

								if (typeof value === "function") {
									if (typeof wrappers[prop] === "function") {
										value = wrapMethod(target, target[prop], wrappers[prop]);
									} else if (hasOwnProperty(metadata, prop)) {
										let wrapper = wrapAsyncFunction(prop, metadata[prop]);
										value = wrapMethod(target, target[prop], wrapper);
									} else {
										value = value.bind(target);
									}
								} else if (typeof value === "object" && value !== null && (hasOwnProperty(wrappers, prop) || hasOwnProperty(metadata, prop))) {
									value = wrapObject(value, wrappers[prop], metadata[prop]);
								} else if (hasOwnProperty(metadata, "*")) {
									value = wrapObject(value, wrappers[prop], metadata["*"]);
								} else {
									Object.defineProperty(cache, prop, {
										configurable: true,
										enumerable: true,
										get() {
											return target[prop];
										},
										set(value) {
											target[prop] = value;
										}
									});
									return value;
								}

								cache[prop] = value;
								return value;
							},

							set(proxyTarget, prop, value, receiver) {
								if (prop in cache) {
									cache[prop] = value;
								} else {
									target[prop] = value;
								}
								return true;
							},

							defineProperty(proxyTarget, prop, desc) {
								return Reflect.defineProperty(cache, prop, desc);
							},

							deleteProperty(proxyTarget, prop) {
								return Reflect.deleteProperty(cache, prop);
							}
						};

						let proxyTarget = Object.create(target);
						return new Proxy(proxyTarget, handlers);
					};

					const wrapEvent = wrapperMap => ({
						addListener(target, listener, ...args) {
							target.addListener(wrapperMap.get(listener), ...args);
						},

						hasListener(target, listener) {
							return target.hasListener(wrapperMap.get(listener));
						},

						removeListener(target, listener) {
							target.removeListener(wrapperMap.get(listener));
						}
					});

					let loggedSendResponseDeprecationWarning = false;
					const onMessageWrappers = new DefaultWeakMap(listener => {
						if (typeof listener !== "function") {
							return listener;
						}

						return function onMessage(message, sender, sendResponse) {
							let didCallSendResponse = false;
							let wrappedSendResponse;
							let sendResponsePromise = new Promise(resolve => {
								wrappedSendResponse = function (response) {
									if (!loggedSendResponseDeprecationWarning) {
										console.warn(SEND_RESPONSE_DEPRECATION_WARNING, new Error().stack);
										loggedSendResponseDeprecationWarning = true;
									}
									didCallSendResponse = true;
									resolve(response);
								};
							});
							let result;

							try {
								result = listener(message, sender, wrappedSendResponse);
							} catch (err) {
								result = Promise.reject(err);
							}

							const isResultThenable = result !== true && isThenable(result);

							if (result !== true && !isResultThenable && !didCallSendResponse) {
								return false;
							}

							const sendPromisedResult = promise => {
								promise.then(msg => {
									sendResponse(msg);
								}, error => {
									let message;
									if (error && (error instanceof Error || typeof error.message === "string")) {
										message = error.message;
									} else {
										message = "An unexpected error occurred";
									}
									sendResponse({
										__mozWebExtensionPolyfillReject__: true,
										message
									});
								}).catch(err => {
									console.error("Failed to send onMessage rejected reply", err);
								});
							};

							if (isResultThenable) {
								sendPromisedResult(result);
							} else {
								sendPromisedResult(sendResponsePromise);
							}

							return true;
						};
					});

					const wrappedSendMessageCallback = ({ reject, resolve }, reply) => {
						if (extensionAPIs.runtime.lastError) {
							if (extensionAPIs.runtime.lastError.message === CHROME_SEND_MESSAGE_CALLBACK_NO_RESPONSE_MESSAGE) {
								resolve();
							} else {
								reject(extensionAPIs.runtime.lastError);
							}
						} else if (reply && reply.__mozWebExtensionPolyfillReject__) {
							reject(new Error(reply.message));
						} else {
							resolve(reply);
						}
					};

					const wrappedSendMessage = (name, metadata, apiNamespaceObj, ...args) => {
						if (args.length < metadata.minArgs) {
							throw new Error(`Expected at least ${metadata.minArgs} ${pluralizeArguments(metadata.minArgs)} for ${name}(), got ${args.length}`);
						}

						if (args.length > metadata.maxArgs) {
							throw new Error(`Expected at most ${metadata.maxArgs} ${pluralizeArguments(metadata.maxArgs)} for ${name}(), got ${args.length}`);
						}

						return new Promise((resolve, reject) => {
							const wrappedCb = wrappedSendMessageCallback.bind(null, { resolve, reject });
							args.push(wrappedCb);
							apiNamespaceObj.sendMessage(...args);
						});
					};

					const staticWrappers = {
						runtime: {
							onMessage: wrapEvent(onMessageWrappers),
							onMessageExternal: wrapEvent(onMessageWrappers),
							sendMessage: wrappedSendMessage.bind(null, "sendMessage", { minArgs: 1, maxArgs: 3 })
						},
						tabs: {
							sendMessage: wrappedSendMessage.bind(null, "sendMessage", { minArgs: 2, maxArgs: 3 })
						}
					};

					const settingMetadata = {
						clear: { minArgs: 1, maxArgs: 1 },
						get: { minArgs: 1, maxArgs: 1 },
						set: { minArgs: 1, maxArgs: 1 }
					};

					apiMetadata.privacy = {
						network: { "*": settingMetadata },
						services: { "*": settingMetadata },
						websites: { "*": settingMetadata }
					};

					return wrapObject(extensionAPIs, staticWrappers, apiMetadata);
				};

				if (typeof chrome != "object" || !chrome || !chrome.runtime || !chrome.runtime.id) {
					throw new Error("This script should only be loaded in a browser extension.");
				}

				module.exports = wrapAPIs(chrome);
			} else {
				module.exports = browser;
			}
		});

	});

	// Sign up at https://extensionpay.com to use this library. AGPLv3 licensed.

	// For running as a content script. Receive a message from the successful payments page
	// and pass it on to the background page to query if the user has paid.
	if (typeof window !== 'undefined') {
		window.addEventListener('message', (event) => {
			if (event.origin !== 'https://extensionpay.com') return;
			if (event.source != window) return;
			if (event.data === 'extpay-fetch-user' || event.data === 'extpay-trial-start') {
				window.postMessage(`${event.data}-received`);
				browserPolyfill.runtime.sendMessage(event.data);
			}
		}, false);
	}

	function ExtPay(extension_id) {

		const HOST = `https://extensionpay.com`;
		const EXTENSION_URL = `${HOST}/extension/${extension_id}`;

		function timeout(ms) {
			return new Promise(resolve => setTimeout(resolve, ms));
		}
		async function get(key) {
			try {
				return await browserPolyfill.storage.sync.get(key)
			} catch (e) {
				// if sync not available (like with Firefox temp addons), fall back to local
				return await browserPolyfill.storage.local.get(key)
			}
		}
		async function set(dict) {
			try {
				return await browserPolyfill.storage.sync.set(dict)
			} catch (e) {
				// if sync not available (like with Firefox temp addons), fall back to local
				return await browserPolyfill.storage.local.set(dict)
			}
		}

		// ----- start configuration checks
		browserPolyfill.management && browserPolyfill.management.getSelf().then(async (ext_info) => {
			if (!ext_info.permissions.includes('storage')) {
				var permissions = ext_info.hostPermissions.concat(ext_info.permissions);
				throw `ExtPay Setup Error: please include the "storage" permission in manifest.json["permissions"] or else ExtensionPay won't work correctly.

You can copy and paste this to your manifest.json file to fix this error:

"permissions": [
    ${permissions.map(x => `"    ${x}"`).join(',\n')}${permissions.length > 0 ? ',' : ''}
    "storage"
]
`
			}

		});
		// ----- end configuration checks

		// run on "install"
		get(['extensionpay_installed_at', 'extensionpay_user']).then(async (storage) => {
			if (storage.extensionpay_installed_at) return;

			// Migration code: before v2.1 installedAt came from the server
			// so use that stored datetime instead of making a new one.
			const user = storage.extensionpay_user;
			const date = user ? user.installedAt : (new Date()).toISOString();
			await set({ 'extensionpay_installed_at': date });
		});

		const paid_callbacks = [];
		const trial_callbacks = [];

		async function create_key() {
			var body = {};
			var ext_info;
			if (browserPolyfill.management) {
				ext_info = await browserPolyfill.management.getSelf();
			} else if (browserPolyfill.runtime) {
				ext_info = await browserPolyfill.runtime.sendMessage('extpay-extinfo');
				if (!ext_info) {
					const is_dev_mode = !('update_url' in browserPolyfill.runtime.getManifest());
					ext_info = { installType: is_dev_mode ? 'development' : 'normal' };
				}
			} else {
				throw 'ExtPay needs to be run in a browser extension context'
			}

			if (ext_info.installType == 'development') {
				body.development = true;
			}

			const resp = await fetch(`${EXTENSION_URL}/api/new-key`, {
				method: 'POST',
				headers: {
					'Accept': 'application/json',
					'Content-type': 'application/json',
				},
				body: JSON.stringify(body),
			});
			if (!resp.ok) {
				throw resp.status, `${HOST}/home`
			}
			const api_key = await resp.json();
			await set({ extensionpay_api_key: api_key });
			return api_key;
		}

		async function get_key() {
			const storage = await get(['extensionpay_api_key']);
			if (storage.extensionpay_api_key) {
				return storage.extensionpay_api_key;
			}
			return null;
		}

		const datetime_re = /^\d\d\d\d-\d\d-\d\dT/;

		async function fetch_user() {
			var storage = await get(['extensionpay_user', 'extensionpay_installed_at']);
			const api_key = await get_key();
			if (!api_key) {
				return {
					paid: false,
					paidAt: null,
					installedAt: storage.extensionpay_installed_at ? new Date(storage.extensionpay_installed_at) : new Date(),
					trialStartedAt: null,
				}
			}

			const resp = await fetch(`${EXTENSION_URL}/api/v2/user?api_key=${api_key}`, {
				method: 'GET',
				headers: {
					'Accept': 'application/json',
				}
			});
			if (!resp.ok) throw 'ExtPay error while fetching user: ' + (await resp.text())

			const user_data = await resp.json();

			const parsed_user = {};
			for (var [key, value] of Object.entries(user_data)) {
				if (value && value.match && value.match(datetime_re)) {
					value = new Date(value);
				}
				parsed_user[key] = value;
			}
			parsed_user.installedAt = new Date(storage.extensionpay_installed_at);


			if (parsed_user.paidAt) {
				if (!storage.extensionpay_user || (storage.extensionpay_user && !storage.extensionpay_user.paidAt)) {
					paid_callbacks.forEach(cb => cb(parsed_user));
				}
			}
			if (parsed_user.trialStartedAt) {
				if (!storage.extensionpay_user || (storage.extensionpay_user && !storage.extensionpay_user.trialStartedAt)) {
					trial_callbacks.forEach(cb => cb(parsed_user));
				}
			}
			await set({ extensionpay_user: user_data });

			return parsed_user;
		}

		async function get_plans() {
			const resp = await fetch(`${EXTENSION_URL}/api/v2/current-plans`, {
				method: 'GET',
				headers: {
					'Accept': 'application/json',
					'Content-type': 'application/json',
				},
			});
			if (!resp.ok) {
				throw `ExtPay: HTTP error while getting plans. Received http code: ${resp.status}`
			}
			return await resp.json();
		}

		async function open_popup(url, width, height) {
			if (browserPolyfill.windows && browserPolyfill.windows.create) {
				const current_window = await browserPolyfill.windows.getCurrent();
				const left = Math.round((current_window.width - width) * 0.5 + current_window.left);
				const top = Math.round((current_window.height - height) * 0.5 + current_window.top);
				try {
					browserPolyfill.windows.create({
						url: url,
						type: "popup",
						focused: true,
						width,
						height,
						left,
						top
					});
				} catch (e) {
					browserPolyfill.windows.create({
						url: url,
						type: "popup",
						width,
						height,
						left,
						top
					});
				}
			} else {
				window.open(url, null, `toolbar=no,location=no,directories=no,status=no,menubar=no,width=${width},height=${height},left=450`);
			}
		}

		async function open_payment_page(plan_nickname) {
			var api_key = await get_key();
			if (!api_key) {
				api_key = await create_key();
			}
			let url = `${EXTENSION_URL}/choose-plan?api_key=${api_key}`;
			if (plan_nickname) {
				url = `${EXTENSION_URL}/choose-plan/${plan_nickname}?api_key=${api_key}`;
			}
			if (browserPolyfill.tabs && browserPolyfill.tabs.create) {
				await browserPolyfill.tabs.create({ url, active: true });
			} else {
				window.open(url, '_blank');
			}
		}

		async function open_trial_page(period) {
			var api_key = await get_key();
			if (!api_key) {
				api_key = await create_key();
			}
			var url = `${EXTENSION_URL}/trial?api_key=${api_key}`;
			if (period) {
				url += `&period=${period}`;
			}
			open_popup(url, 500, 700);
		}

		async function open_login_page() {
			var api_key = await get_key();
			if (!api_key) {
				api_key = await create_key();
			}
			const url = `${EXTENSION_URL}/reactivate?api_key=${api_key}&back=choose-plan&v2`;
			open_popup(url, 500, 800);
		}

		var polling = false;
		async function poll_user_paid() {
			if (polling) return;
			polling = true;
			var user = await fetch_user();
			for (var i = 0; i < 2 * 60; ++i) {
				if (user.paidAt) {
					polling = false;
					return user;
				}
				await timeout(1000);
				user = await fetch_user();
			}
			polling = false;
		}

		return {
			getUser: function () {
				return fetch_user()
			},
			onPaid: {
				addListener: function (callback) {
					const content_script_template = `"content_scripts": [
                {
            "matches": ["${HOST}/*"],
            "js": ["ExtPay.js"],
            "run_at": "document_start"
        }]`;
					const manifest = browserPolyfill.runtime.getManifest();
					if (!manifest.content_scripts) {
						throw `ExtPay setup error: To use the onPaid callback handler, please include ExtPay as a content script in your manifest.json. You can copy the example below into your manifest.json or check the docs: https://github.com/Glench/ExtPay#2-configure-your-manifestjson

        ${content_script_template}`
					}
					const extpay_content_script_entry = manifest.content_scripts.find(obj => {
						return obj.matches.includes(HOST.replace(':3000', '') + '/*')
					});
					if (!extpay_content_script_entry) {
						throw `ExtPay setup error: To use the onPaid callback handler, please include ExtPay as a content script in your manifest.json matching "${HOST}/*". You can copy the example below into your manifest.json or check the docs: https://github.com/Glench/ExtPay#2-configure-your-manifestjson

        ${content_script_template}`
					} else {
						if (!extpay_content_script_entry.run_at || extpay_content_script_entry.run_at !== 'document_start') {
							throw `ExtPay setup error: To use the onPaid callback handler, please make sure the ExtPay content script in your manifest.json runs at document start. You can copy the example below into your manifest.json or check the docs: https://github.com/Glench/ExtPay#2-configure-your-manifestjson

        ${content_script_template}`
						}
					}

					paid_callbacks.push(callback);
				},
			},
			getPlans: get_plans,
			openPaymentPage: open_payment_page,
			openTrialPage: open_trial_page,
			openLoginPage: open_login_page,
			onTrialStarted: {
				addListener: function (callback) {
					trial_callbacks.push(callback);
				}
			},
			startBackground: function () {
				browserPolyfill.runtime.onMessage.addListener(function (message, sender, send_response) {
					if (message == 'extpay-fetch-user') {
						poll_user_paid();
					} else if (message == 'extpay-trial-start') {
						fetch_user();
					} else if (message == 'extpay-extinfo' && browserPolyfill.management) {
						return browserPolyfill.management.getSelf()
					}
				});
			}
		}
	}

export default ExtPay;

```

## File: `js/background.js`
```javascript
import { Premium } from './premium.js';
// AI comparison now handled server-side for security

//=============================================================================
// STORAGE MIGRATION & VALIDATION
//=============================================================================

/**
 * Required properties for each action with their default values.
 * Used to repair actions that may be missing properties after upgrades.
 */
const REQUIRED_ACTION_PROPERTIES = {
    combination: { key: 'none', mouseButton: 'right' },
    openLinks: false,
    openWindow: false,
    copyUrls: false,
    copyUrlsAndTitles: false,
    copyTitles: false,
    createBookmarks: false,
    smartSelect: 'off',
    avoidDuplicates: 'on',
    reverseOrder: false,
    openAtEnd: false,
    boxColor: '#FF0000',
    tabDelay: 0,
    borderThickness: 2,
    borderStyle: 'solid',
    markAsVisited: true
};

/**
 * Validates if an action has the minimum required structure.
 * An action is valid if it's an object with a combination property.
 * @param {Object} action - The action to validate
 * @returns {boolean} True if action has valid base structure
 */
function validateAction(action) {
    if (!action || typeof action !== 'object') return false;
    if (!action.combination || typeof action.combination !== 'object') return false;
    // Must have at least a mouseButton defined
    if (!action.combination.mouseButton) return false;
    return true;
}

/**
 * Repairs an action by filling in missing properties with defaults.
 * Preserves all existing valid properties.
 * @param {Object} action - The action to repair
 * @returns {Object} A new action object with all required properties
 */
function repairAction(action) {
    const repairedAction = {};

    // For each required property, use existing value or default
    for (const [key, defaultValue] of Object.entries(REQUIRED_ACTION_PROPERTIES)) {
        if (key === 'combination') {
            // Special handling for combination object
            repairedAction.combination = {
                key: action.combination?.key ?? defaultValue.key,
                mouseButton: action.combination?.mouseButton ?? defaultValue.mouseButton
            };
        } else if (action.hasOwnProperty(key)) {
            // Keep existing value
            repairedAction[key] = action[key];
        } else {
            // Use default value
            repairedAction[key] = defaultValue;
        }
    }

    // Preserve any extra properties not in REQUIRED_ACTION_PROPERTIES
    // (for forward compatibility)
    for (const [key, value] of Object.entries(action)) {
        if (!repairedAction.hasOwnProperty(key)) {
            repairedAction[key] = value;
        }
    }

    return repairedAction;
}

/**
 * Migrates stored actions by validating and repairing each one.
 * @param {Array} actions - The stored actions array
 * @returns {Object} Object with: { actions: Array, wasRepaired: boolean, invalidCount: number }
 */
function migrateStoredActions(actions) {
    // If not an array or empty, return null to trigger default action creation
    if (!Array.isArray(actions) || actions.length === 0) {
        return null;
    }

    const repairedActions = [];
    let wasRepaired = false;
    let invalidCount = 0;

    for (const action of actions) {
        if (validateAction(action)) {
            // Check if repair is needed by comparing property count
            const originalKeys = Object.keys(action).length;
            const repaired = repairAction(action);
            const repairedKeys = Object.keys(repaired).length;

            if (repairedKeys > originalKeys) {
                wasRepaired = true;
            }
            repairedActions.push(repaired);
        } else {
            // Action is too corrupted to repair, skip it
            invalidCount++;
            wasRepaired = true;
        }
    }

    // If all actions were invalid, return null to trigger defaults
    if (repairedActions.length === 0) {
        return null;
    }

    return { actions: repairedActions, wasRepaired, invalidCount };
}

//=============================================================================
// EXTENSION LIFECYCLE
//=============================================================================

//open options page on extension install
chrome.runtime.onInstalled.addListener((details) => {
    // We use a version-specific flag to ensure we reset the highlighter to 'false' 
    // exactly once for users who might have received the accidental 'true' default.
    const RESET_FLAG = 'highlighterDefaultReset_3_8_2';

    chrome.storage.sync.get(['linkifyEnabled', 'duplicateHighlighterEnabled', RESET_FLAG, 'savedActions'], (result) => {
        if (result.linkifyEnabled === undefined) {
            chrome.storage.sync.set({ linkifyEnabled: true });
        }
        
        // If the reset flag is missing, force the highlighter to false (one-time fix)
        if (!result[RESET_FLAG]) {
            const update = { duplicateHighlighterEnabled: false };
            update[RESET_FLAG] = true;
            chrome.storage.sync.set(update);
            console.log('Grabbit: Duplicate Highlighter default reset to false.');
        } else if (result.duplicateHighlighterEnabled === undefined) {
            // Fallback for new installs if the flag somehow exists but setting doesn't
            chrome.storage.sync.set({ duplicateHighlighterEnabled: false });
        }

        // Migrate/validate stored actions
        const migrationResult = migrateStoredActions(result.savedActions);

        if (migrationResult === null) {
            // No valid actions found, set defaults
            const defaultActions = [
                {
                    combination: { key: 'none', mouseButton: 'right' },
                    openLinks: true,
                    openWindow: false,
                    copyUrls: false,
                    copyUrlsAndTitles: false,
                    copyTitles: false,
                    createBookmarks: false,
                    smartSelect: 'off',
                    avoidDuplicates: 'on',
                    reverseOrder: false,
                    openAtEnd: false,
                    boxColor: '#FF0000', // Red
                    tabDelay: 0,
                    borderThickness: 2,
                    borderStyle: 'solid',
                    markAsVisited: false
                },
                {
                    combination: { key: 'ctrl', mouseButton: 'right' },
                    openLinks: false,
                    openWindow: false,
                    copyUrls: true,
                    copyUrlsAndTitles: false,
                    copyTitles: false,
                    createBookmarks: false,
                    smartSelect: 'off',
                    avoidDuplicates: 'on',
                    reverseOrder: false,
                    openAtEnd: false,
                    boxColor: '#0000FF', // Blue
                    tabDelay: 0,
                    borderThickness: 2,
                    borderStyle: 'solid',
                    markAsVisited: false
                }
            ];

            chrome.storage.sync.set({ savedActions: defaultActions });
        } else if (migrationResult.wasRepaired) {
            // Actions were repaired, save them
            chrome.storage.sync.set({ savedActions: migrationResult.actions });
        }
        // If no repair was needed, do nothing (keep existing actions)
    });

    if (details.reason === 'install') {
        // Open options page on first install
        chrome.runtime.openOptionsPage();
    } else if (details.reason === 'update') {
        // Extension was updated - show badge on icon and set flag for popup
        const manifest = chrome.runtime.getManifest();
        chrome.action.setBadgeText({ text: '!' });
        chrome.action.setBadgeBackgroundColor({ color: '#4CAF50' });
        chrome.storage.local.set({
            updateAvailable: true,
            updatedVersion: manifest.version
        });
    }
});

// create windows
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    //create windows
    if (request.action === 'openLinks') {
        const delay = request.delay || 0; // Get delay in seconds

        // Create new window with first URL
        chrome.windows.create({
            url: request.urls[0],
            focused: true,
        }, (newWindow) => {

            // Create tabs for remaining URLs in the new window with delay
            if (delay > 0) {
                // Open tabs with delay - only process the remaining URLs (not the first one)
                request.urls.slice(1).forEach((url, index) => {
                    setTimeout(() => {
                        chrome.tabs.create({
                            windowId: newWindow.id,
                            url: url,
                            active: false
                        });
                    }, delay * 1000 * (index + 1)); // Convert seconds to milliseconds and multiply by index
                });
            } else {
                // Open tabs without delay - only process the remaining URLs (not the first one)
                request.urls.slice(1).forEach(url => {
                    chrome.tabs.create({
                        windowId: newWindow.id,
                        url: url,
                        active: false
                    });
                });
            }
        });
    }

    // Create tabs with delay
    if (request.action === 'createTabs') {
        const delay = request.delay || 0; // Get delay in seconds
        const currentIndex = sender.tab.index;
        const currentWindowId = sender.tab.windowId;
        const openAtEnd = request.openAtEnd || false; // Get openAtEnd preference

        // If openAtEnd is true, we'll need to get the total number of tabs
        if (openAtEnd && delay === 0) {
            // For tabs without delay, get tab count first then create tabs
            chrome.tabs.query({ windowId: currentWindowId }, function (tabs) {
                const tabCount = tabs.length;
                // Create all tabs at the end
                request.urls.forEach((url, index) => {
                    chrome.tabs.create({
                        url: url,
                        windowId: currentWindowId,
                        index: tabCount + index, // Place at the end
                        active: false
                    });
                });
            });
        } else if (openAtEnd && delay > 0) {
            // For tabs with delay, get tab count before each creation
            request.urls.forEach((url, index) => {
                setTimeout(() => {
                    chrome.tabs.query({ windowId: currentWindowId }, function (tabs) {
                        const tabCount = tabs.length;
                        chrome.tabs.create({
                            url: url,
                            windowId: currentWindowId,
                            index: tabCount, // Place at the end
                            active: false
                        });
                    });
                }, delay * 1000 * index);
            });
        } else if (delay > 0) {
            // Original behavior: Open tabs with delay after current tab
            request.urls.forEach((url, index) => {
                setTimeout(() => {
                    chrome.tabs.create({
                        url: url,
                        windowId: currentWindowId,
                        index: currentIndex + index + 1,
                        active: false
                    });
                }, delay * 1000 * index); // Convert seconds to milliseconds and multiply by index
            });
        } else {
            // Original behavior: Open tabs without delay after current tab
            request.urls.forEach((url, index) => {
                chrome.tabs.create({
                    url: url,
                    windowId: currentWindowId,
                    index: currentIndex + index + 1,
                    active: false
                });
            });
        }
    }

});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action !== 'createBookmarks') return;

    const { bookmarks, folderName } = request;
    if (!bookmarks || bookmarks.length === 0) return;

    const runWithPermission = () => {
        // Function to create bookmarks in a specific folder
        const createBookmarksInFolder = parentId => {
            bookmarks.forEach(bookmark => {
                chrome.bookmarks.create({
                    parentId,
                    title: bookmark.title,
                    url: bookmark.url
                });
            });
        };

        // Search for existing folder with the same name
        chrome.bookmarks.search({ title: folderName }, results => {
            // Filter to find a folder (not a bookmark) with the exact name
            const existingFolder = results.find(item => !item.url && item.title === folderName);

            if (existingFolder) {
                // Folder exists, add bookmarks to it
                createBookmarksInFolder(existingFolder.id);
            } else {
                // Folder doesn't exist, create it then add bookmarks
                // We'll create it under "Other Bookmarks" (usually id '2') or '1' depending on browser,
                // but not specifying parentId usually defaults to "Other Bookmarks" in Chrome.
                chrome.bookmarks.create({ title: folderName }, newFolder => {
                    createBookmarksInFolder(newFolder.id);
                });
            }
        });
    };

    chrome.permissions.contains({ permissions: ["bookmarks"] }, hasPermission => {
        if (hasPermission) {
            runWithPermission();
        } else {
            chrome.permissions.request({ permissions: ["bookmarks"] }, granted => {
                if (granted) {
                    runWithPermission();
                }
            });
        }
    });
});

/**
 * Updates the extension icon state based on whether the domain is disabled.
 * Uses a badge since we don't have gray icon assets yet.
 */
function updateIconState(tabId, url) {
    if (!url) return;
    try {
        const hostname = new URL(url).hostname;
        chrome.storage.sync.get(['disabledDomains'], (result) => {
            const disabledDomains = result.disabledDomains || [];
            const isDisabled = disabledDomains.some(domain => hostname.includes(domain));

            if (isDisabled) {
                // Set Badge to "OFF" with a dark gray background
                chrome.action.setBadgeText({ text: "OFF", tabId: tabId });
                chrome.action.setBadgeBackgroundColor({ color: '#555555', tabId: tabId });
                // If gray icons existed: chrome.action.setIcon({ path: "icons/icon_gray.png", tabId: tabId });
            } else {
                // Clear Badge
                chrome.action.setBadgeText({ text: "", tabId: tabId });
            }
        });
    } catch (e) {
        // Invalid URL, ignore
    }
}

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete' && tab.url) {
        updateIconState(tabId, tab.url);
    }
});

chrome.tabs.onActivated.addListener((activeInfo) => {
    chrome.tabs.get(activeInfo.tabId, (tab) => {
        if (tab.url) {
            updateIconState(activeInfo.tabId, tab.url);
        }
    });
});


//=============================================================================
// PREMIUM FEATURES
//=============================================================================

// Initialize Premium module (ExtPay listeners)
Premium.init();

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'checkPremiumStatus') {
        Premium.getUser().then(user => {
            sendResponse({ isPremium: user.paid });
        });
        return true; // Keep channel open for async response
    }

    if (request.action === 'openPaymentPage') {
        Premium.openPaymentPage();
    }
});

// Pro Account page message handlers
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'GET_PRO_STATUS') {
        (async () => {
            try {
                const user = await Premium.getUser();

                // Get cached credits from storage (saved after each AI action)
                let credits = null;
                if (user.paid) {
                    try {
                        const stored = await chrome.storage.local.get(['cachedCredits', 'cachedCreditsTimestamp']);
                        console.log('[ProAccount] Cached credits from storage:', stored);

                        if (stored.cachedCredits !== undefined) {
                            credits = {
                                _remaining: stored.cachedCredits
                            };
                        }
                    } catch (e) {
                        console.warn('Failed to get cached credits:', e);
                    }
                }

                sendResponse({
                    user: {
                        paid: user.paid,
                        email: user.email,
                        trialActive: user.trialActive,
                        paidAt: user.paidAt || null
                    },
                    credits: credits
                });
            } catch (error) {
                sendResponse({ error: error.message });
            }
        })();
        return true; // Keep channel open for async response
    }

    if (request.action === 'OPEN_LOGIN_PAGE') {
        Premium.openLoginPage();
        sendResponse({ success: true });
        return true;
    }

    if (request.action === 'LOGOUT') {
        // Clear cached credits AND ExtPay user data to fully log out
        chrome.storage.local.remove([
            'cachedCredits',
            'cachedCreditsTimestamp',
            'extensionpay_user',      // User data
            'extensionpay_api_key'    // API key (force new key generation on next login)
        ]);

        // Open login page (allows explicit switch, though local clear is immediate)
        Premium.openLoginPage();
        sendResponse({ success: true });
        return true;
    }

    if (request.action === 'OPEN_PAYMENT_PAGE') {
        Premium.openPaymentPage();
        sendResponse({ success: true });
        return true;
    }

    if (request.action === 'OPEN_BILLING_PORTAL') {
        // ExtensionPay generic account page
        chrome.tabs.create({
            url: 'https://extensionpay.com/account',
            active: true
        });
        sendResponse({ success: true });
        return true;
    }

    if (request.action === 'CANCEL_SUBSCRIPTION') {
        // ExtPay docs suggest openPaymentPage handles cancellation for existing subscribers
        Premium.openPaymentPage();
        sendResponse({ success: true });
        return true;
    }
});

// Handle compareProducts action
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'compareProducts') {
        handleProductComparison(request.tabs)
            .then(results => sendResponse({ results }))
            .catch(error => sendResponse({ error: error.message }));
        return true;
    }
});

// Handle summarizePage action
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'summarizePage') {
        handleArticleSummary(request.tab)
            .then(results => sendResponse({ results }))
            .catch(error => sendResponse({ error: error.message }));
        return true;
    }
});

// Handle summarizeYoutube action
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'summarizeYoutube') {
        handleYouTubeSummary(request.tab)
            .then(results => sendResponse({ results }))
            .catch(error => sendResponse({ error: error.message }));
        return true;
    }
});

/**
 * Fetch API token for authenticated requests
 */
async function getApiToken(email) {
    const stored = await chrome.storage.local.get(['grabbit_api_token']);
    if (stored.grabbit_api_token) return stored.grabbit_api_token;

    const response = await fetch('https://grabbit.socratisp.com/wp-json/grabbit/v1/get-token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email })
    });

    if (response.ok) {
        const data = await response.json();
        await chrome.storage.local.set({ grabbit_api_token: data.token });
        return data.token;
    }

    // Try to get more error details
    let errorDetails = '';
    try {
        const errorData = await response.json();
        errorDetails = errorData.message || JSON.stringify(errorData);
    } catch (e) {
        errorDetails = response.statusText || 'Unknown error';
    }

    console.error('[Grabbit] Failed to get API token. Status:', response.status, 'Details:', errorDetails);
    throw new Error(`Failed to get API token (${response.status}: ${errorDetails})`);
}

/**
 * Main handler for AI Product Comparison
 * Uses server-side proxy - API key never sent to client
 */
async function handleProductComparison(tabs) {
    // 1. Verify premium status (client-side check)
    const user = await Premium.getUser();

    if (!user.paid) {
        throw new Error('Premium required');
    }

    if (!user.email) {
        throw new Error('No email associated with your account. Please log in to ExtPay.');
    }

    // 2. Fetch API token
    const token = await getApiToken(user.email);

    // 3. Extract content from each tab
    const products = [];
    for (const tab of tabs) {
        try {
            // Check if tab still exists before injecting script
            let targetTab;
            try {
                targetTab = await chrome.tabs.get(tab.id);
            } catch (tabError) {
                console.warn('Product tab was closed:', tab.id);
                products.push({
                    title: tab.title,
                    price: '',
                    rawContent: 'Page Title: ' + tab.title + '\nURL: ' + tab.url,
                    siteName: new URL(tab.url).hostname,
                    url: tab.url
                });
                continue; // Skip to next tab
            }

            const [result] = await chrome.scripting.executeScript({
                target: { tabId: tab.id },
                func: extractProductDataFromPage
            });
            products.push({
                title: result.result?.title || tab.title,
                price: result.result?.price || '',
                rawContent: result.result?.rawContent || '',
                siteName: result.result?.siteName || new URL(tab.url).hostname,
                url: tab.url
            });
        } catch (e) {
            console.warn('Could not extract from tab ' + tab.id + ':', e);
            products.push({
                title: tab.title,
                price: '',
                rawContent: 'Page Title: ' + tab.title + '\nURL: ' + tab.url,
                siteName: new URL(tab.url).hostname,
                url: tab.url
            });
        }
    }

    // 4. Send to server-side proxy (API key stays on server)
    const response = await fetch('https://grabbit.socratisp.com/wp-json/grabbit/v1/compare', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            email: user.email,
            token: token,
            products: products
        })
    });

    const data = await response.json();

    if (!response.ok) {
        // Handle specific errors
        if (response.status === 403) {
            throw new Error('Subscription not active. Please check your payment status.');
        } else if (response.status === 429) {
            throw new Error(data.message || 'Monthly limit reached. Try again next month.');
        } else {
            throw new Error(data.message || 'Comparison failed. Please try again.');
        }
    }

    // Cache remaining credits for Pro Account page
    if (data.remaining_month !== undefined) {
        chrome.storage.local.set({
            cachedCredits: data.remaining_month,
            cachedCreditsTimestamp: Date.now()
        });
    }

    // Return comparison results (and remaining quota info)
    return {
        ...data.comparison,
        _remaining: data.remaining_month
    };
}

/**
 * Main handler for AI Article Summary
 * Uses server-side proxy - API key never sent to client
 */
async function handleArticleSummary(tab) {
    // 1. Verify premium status (client-side check)
    const user = await Premium.getUser();

    if (!user.paid) {
        throw new Error('Premium required');
    }

    if (!user.email) {
        throw new Error('No email associated with your account. Please log in to ExtPay.');
    }

    // 2. Fetch API token
    const token = await getApiToken(user.email);

    // 3. Extract article content from the tab
    try {
        // Check if tab still exists before injecting script
        let targetTab;
        try {
            targetTab = await chrome.tabs.get(tab.id);
        } catch (tabError) {
            console.warn('Article tab was closed:', tab.id);
            throw new Error('The article tab was closed. Please reopen the article and try again.');
        }

        const [result] = await chrome.scripting.executeScript({
            target: { tabId: tab.id },
            func: extractArticleDataFromPage
        });

        const pageData = {
            title: result.result?.title || tab.title,
            url: tab.url,
            rawContent: result.result?.rawContent || ''
        };

        // 4. Send to server-side proxy (API key stays on server)
        const response = await fetch('https://grabbit.socratisp.com/wp-json/grabbit/v1/summarize', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                email: user.email,
                token: token,
                pageData: pageData
            })
        });

        const data = await response.json();

        if (!response.ok) {
            // Handle specific errors
            if (response.status === 403) {
                throw new Error('Subscription not active. Please check your payment status.');
            } else if (response.status === 429) {
                throw new Error(data.message || 'Monthly limit reached. Try again next month.');
            } else {
                throw new Error(data.message || 'Summary failed. Please try again.');
            }
        }

        // Cache remaining credits for Pro Account page
        console.log('[Summarize] Response data.remaining_month:', data.remaining_month);
        if (data.remaining_month !== undefined) {
            console.log('[Summarize] Caching credits:', data.remaining_month);
            chrome.storage.local.set({
                cachedCredits: data.remaining_month,
                cachedCreditsTimestamp: Date.now()
            });
        } else {
            console.warn('[Summarize] remaining_month is undefined, not caching');
        }

        // Return summary results (and remaining quota info)
        return {
            ...data.summary,
            _remaining: data.remaining_month
        };

    } catch (e) {
        console.warn('Could not extract from tab ' + tab.id + ':', e);

        // Fallback: send minimal data
        const pageData = {
            title: tab.title,
            url: tab.url,
            rawContent: 'Page Title: ' + tab.title + '\nURL: ' + tab.url
        };

        const response = await fetch('https://grabbit.socratisp.com/wp-json/grabbit/v1/summarize', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                email: user.email,
                token: token,
                pageData: pageData
            })
        });

        const data = await response.json();

        if (!response.ok) {
            if (response.status === 403) {
                throw new Error('Subscription not active. Please check your payment status.');
            } else if (response.status === 429) {
                throw new Error(data.message || 'Monthly limit reached. Try again next month.');
            } else {
                throw new Error(data.message || 'Summary failed. Please try again.');
            }
        }

        // Cache remaining credits for Pro Account page
        if (data.remaining_month !== undefined) {
            chrome.storage.local.set({
                cachedCredits: data.remaining_month,
                cachedCreditsTimestamp: Date.now()
            });
        }

        return {
            ...data.summary,
            _remaining: data.remaining_month
        };
    }
}

/**
 * This function is injected into each tab to extract product data.
 * Simplified - just extract raw content and let AI identify the product name.
 */
function extractProductDataFromPage() {
    const url = window.location.href;
    const siteName = window.location.hostname;

    // Try to get basic info, but don't stress about perfect extraction
    let title = document.title || '';
    let price = '';
    let description = '';
    let features = [];
    let specs = [];

    // Quick price extraction (just one attempt)
    const priceEl = document.querySelector('[data-price], .price, .product-price, [itemprop="price"]');
    if (priceEl?.textContent?.trim()) {
        price = priceEl.textContent.trim().replace(/\s+/g, ' ');
    }

    // Quick description extraction (just one attempt)
    const descEl = document.querySelector('.product-description, #productDescription, [itemprop="description"]');
    if (descEl) {
        description = (descEl.content || descEl.textContent?.trim() || '').substring(0, 3000);
    }

    // Grab feature bullets if present
    document.querySelectorAll('#feature-bullets li, .feature-list li').forEach(el => {
        const text = el.textContent?.trim();
        if (text && text.length > 10 && text.length < 500 && features.length < 10) {
            features.push(text);
        }
    });

    // Grab main product content
    const mainContent = document.querySelector('main, #content, article, .product-page');
    let contentText = mainContent?.innerText?.substring(0, 8000) || document.body.innerText?.substring(0, 8000) || '';

    // Build raw content - let AI figure out the real product name
    let rawContent = `URL: ${url}\n`;
    rawContent += `Site: ${siteName}\n`;
    rawContent += `Page Title: ${title}\n`;

    if (price) {
        rawContent += `Price: ${price}\n`;
    }

    if (description) {
        rawContent += `\nDescription:\n${description}\n`;
    }

    if (features.length > 0) {
        rawContent += `\nKey Features:\n${features.join('\n• ')}\n`;
    }

    rawContent += `\nPage Content:\n${contentText}\n`;

    return {
        title: title, // Just send page title - AI will identify real product name
        url: url,
        siteName: siteName,
        rawContent: rawContent
    };
}

/**
 * This function is injected into the tab to extract article/blog post data.
 * Optimized for long-form text content like articles, blog posts, documentation.
 */
function extractArticleDataFromPage() {
    const data = {
        title: '',
        author: '',
        date: '',
        content: '',
        headings: [],
        rawContent: ''
    };

    // Title - prioritize article/blog post titles
    const titleSelectors = [
        'h1',
        'article h1',
        '.post-title',
        '.entry-title',
        '[itemprop="headline"]',
        '.article-title',
        '.blog-title',
        '#article-title',
        '.post-title h1'
    ];

    for (const selector of titleSelectors) {
        const el = document.querySelector(selector);
        if (el?.textContent?.trim()) {
            data.title = el.textContent.trim();
            break;
        }
    }

    // Fallback to document.title
    if (!data.title) {
        data.title = document.title;
    }

    // Author
    const authorSelectors = [
        '[itemprop="author"]',
        '.author',
        '.post-author',
        '.entry-author',
        '.article-author',
        '.byline',
        '.writer',
        '[class*="author"]'
    ];

    for (const selector of authorSelectors) {
        const el = document.querySelector(selector);
        if (el?.textContent?.trim()) {
            data.author = el.textContent.trim();
            break;
        }
    }

    // Date
    const dateSelectors = [
        '[itemprop="datePublished"]',
        'time',
        '.post-date',
        '.entry-date',
        '.publish-date',
        '.article-date',
        '[class*="date"]',
        '[datetime]'
    ];

    for (const selector of dateSelectors) {
        const el = document.querySelector(selector);
        const date = el?.getAttribute('datetime') || el?.textContent?.trim();
        if (date) {
            data.date = date;
            break;
        }
    }

    // Main article content - comprehensive selectors
    const contentSelectors = [
        'article',
        '[itemprop="articleBody"]',
        '.post-content',
        '.entry-content',
        '.article-content',
        '.content',
        '#content',
        'main',
        '.blog-content',
        '.post-body'
    ];

    let mainContent = '';
    for (const selector of contentSelectors) {
        const el = document.querySelector(selector);
        if (el) {
            mainContent = el.innerText || el.textContent;
            break;
        }
    }

    // If no main content found, grab body but filter out nav/footer
    if (!mainContent || mainContent.length < 200) {
        const body = document.body;
        if (body) {
            // Clone to avoid modifying actual page
            const clone = body.cloneNode(true);

            // Remove unwanted elements
            const unwantedSelectors = [
                'nav', 'header', 'footer', '.sidebar', '.navigation',
                '.menu', '.comments', '.related-posts', '.advertisement',
                'script', 'style', 'noscript', 'iframe'
            ];

            unwantedSelectors.forEach(sel => {
                clone.querySelectorAll(sel).forEach(el => el.remove());
            });

            mainContent = clone.innerText || clone.textContent;
        }
    }

    // Extract headings for structure
    const headingElements = document.querySelectorAll('h1, h2, h3, h4');
    headingElements.forEach(h => {
        const text = h.textContent?.trim();
        if (text && text.length > 0 && text.length < 200) {
            data.headings.push(`[${h.tagName}] ${text}`);
        }
    });

    // Build comprehensive rawContent
    let rawContent = `Title: ${data.title}\n`;

    if (data.author) {
        rawContent += `Author: ${data.author}\n`;
    }

    if (data.date) {
        rawContent += `Published: ${data.date}\n`;
    }

    rawContent += `URL: ${window.location.href}\n\n`;

    if (data.headings.length > 0) {
        rawContent += `--- ARTICLE STRUCTURE ---\n`;
        rawContent += data.headings.join('\n') + '\n\n';
    }

    rawContent += `--- ARTICLE CONTENT ---\n`;
    rawContent += mainContent.substring(0, 12000); // Limit to 12K chars for context

    return {
        title: data.title,
        author: data.author,
        date: data.date,
        url: window.location.href,
        rawContent: rawContent
    };
}

/**
 * Main handler for AI YouTube Summary
 * Uses server-side proxy - API key never sent to client
 */
async function handleYouTubeSummary(tab) {
    // 1. Verify premium status (client-side check)
    const user = await Premium.getUser();

    if (!user.paid) {
        throw new Error('Premium required');
    }

    if (!user.email) {
        throw new Error('No email associated with your account. Please log in to ExtPay.');
    }

    // 2. Fetch API token
    const token = await getApiToken(user.email);

    // 3. Extract YouTube data (transcript, chapters, metadata) from the tab
    try {
        // Check if tab still exists before injecting script
        let targetTab;
        try {
            targetTab = await chrome.tabs.get(tab.id);
        } catch (tabError) {
            console.warn('YouTube video tab was closed:', tab.id);
            throw new Error('The YouTube video tab was closed. Please reopen the video and try again.');
        }

        const [result] = await chrome.scripting.executeScript({
            target: { tabId: tab.id },
            func: extractYouTubeDataFromPage,
            world: 'MAIN' // Required to access window.ytcfg from YouTube's page
        });

        const videoData = result.result;

        // Check for extraction errors
        if (videoData && videoData.error) {
            console.error('YouTube extraction failed:', videoData.error);
            throw new Error(videoData.error);
        }

        if (!videoData || !videoData.transcript) {
            throw new Error('No transcript available for this video. The video may not have captions enabled.');
        }

        // 4. Send to server-side proxy (API key stays on server)
        const response = await fetch('https://grabbit.socratisp.com/wp-json/grabbit/v1/youtube-summary', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                email: user.email,
                token: token,
                videoData: videoData
            })
        });

        const data = await response.json();

        if (!response.ok) {
            // Handle specific errors
            if (response.status === 403) {
                throw new Error('Subscription not active. Please check your payment status.');
            } else if (response.status === 429) {
                throw new Error(data.message || 'Monthly limit reached. Try again next month.');
            } else {
                throw new Error(data.message || 'YouTube summary failed. Please try again.');
            }
        }

        // Return summary results (and remaining quota info)
        return {
            ...data.summary,
            _remaining: data.remaining_month
        };

    } catch (e) {
        console.error('YouTube extraction error:', e);
        throw new Error(e.message || 'Failed to extract video data. Please try again.');
    }
}

/**
 * This function is injected into the YouTube tab to extract video data using InnerTube API.
 * Extracts: title, channel, transcript, chapters
 */
async function extractYouTubeDataFromPage() {
    const data = {
        title: '',
        channel: '',
        videoId: '',
        transcript: '',
        chapters: [],
        url: window.location.href
    };

    try {
        // Extract video ID from URL
        const urlParams = new URLSearchParams(window.location.search);
        data.videoId = urlParams.get('v') || '';

        if (!data.videoId) {
            throw new Error('Could not find video ID');
        }

        // Get title from page
        const titleEl = document.querySelector('h1.ytd-video-primary-info-renderer, h1.ytd-watch-metadata');
        data.title = titleEl?.textContent?.trim() || document.title.replace(' - YouTube', '');

        // Get channel name
        const channelEl = document.querySelector('#channel-name a, ytd-channel-name a, #owner-name a');
        data.channel = channelEl?.textContent?.trim() || '';

        // Try to get chapters from description or chapter markers
        const chapters = [];

        // Method 1: Check for chapter markers in the video player
        const chapterElements = document.querySelectorAll('.ytp-chapter-container [class*="title"]');
        if (chapterElements.length > 0) {
            chapterElements.forEach((el, i) => {
                chapters.push({
                    timestamp: '',
                    title: el.textContent?.trim() || `Chapter ${i + 1}`
                });
            });
        }

        // Method 2: Parse chapters from description
        const descriptionEl = document.querySelector('#description-inline-expander, #description');
        const descriptionText = descriptionEl?.textContent || '';

        // Look for timestamp patterns like "0:00 Introduction" or "00:00 - Introduction"
        const timestampRegex = /(\d{1,2}:\d{2}(?::\d{2})?)\s*[-–—]?\s*(.+?)(?=\n|$)/gm;
        let match;
        while ((match = timestampRegex.exec(descriptionText)) !== null) {
            const timestamp = match[1].trim();
            const title = match[2].trim();
            if (title.length > 2 && title.length < 100) {
                chapters.push({ timestamp, title });
            }
        }

        data.chapters = chapters.slice(0, 50); // Support long videos with many chapters

        // Get InnerTube API key
        const apiKey = window.ytcfg?.get?.('INNERTUBE_API_KEY');

        if (!apiKey) {
            throw new Error('Could not get InnerTube API key');
        }

        // Call InnerTube Player API to get caption tracks
        // Use ANDROID client - returns directly accessible subtitle URLs without restrictions
        const playerResponse = await fetch(`https://www.youtube.com/youtubei/v1/player?key=${apiKey}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                context: {
                    client: {
                        clientName: 'ANDROID',
                        clientVersion: '19.29.37',
                        hl: window.ytcfg?.get?.('HL') || 'en',
                    },
                },
                videoId: data.videoId,
            }),
        });

        if (!playerResponse.ok) {
            throw new Error('Failed to get player data');
        }

        const playerData = await playerResponse.json();

        // Get caption tracks
        const captionTracks = playerData?.captions?.playerCaptionsTracklistRenderer?.captionTracks;

        if (!captionTracks || captionTracks.length === 0) {
            throw new Error('No captions available');
        }

        // Prefer English captions, fallback to first available
        let selectedTrack = captionTracks.find(t => t.languageCode === 'en') ||
            captionTracks.find(t => t.languageCode?.startsWith('en')) ||
            captionTracks[0];

        if (!selectedTrack?.baseUrl) {
            throw new Error('No valid caption track found');
        }

        // Fetch transcript in json3 format (JSON - avoids Trusted Types restrictions with DOMParser)
        const transcriptUrl = new URL(selectedTrack.baseUrl);
        transcriptUrl.searchParams.set('fmt', 'json3');

        const transcriptResponse = await fetch(transcriptUrl.toString());

        if (!transcriptResponse.ok) {
            throw new Error('Failed to fetch transcript');
        }

        const transcriptJson = await transcriptResponse.json();

        // Parse JSON transcript with timestamps
        let fullTranscript = '';
        let timestampedTranscript = '';
        let lastTimestamp = -1;

        // Helper to format milliseconds to MM:SS or HH:MM:SS
        const formatTime = (ms) => {
            const totalSeconds = Math.floor(ms / 1000);
            const hours = Math.floor(totalSeconds / 3600);
            const minutes = Math.floor((totalSeconds % 3600) / 60);
            const seconds = totalSeconds % 60;

            if (hours > 0) {
                return `${hours}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
            }
            return `${minutes}:${String(seconds).padStart(2, '0')}`;
        };

        if (transcriptJson.events) {
            transcriptJson.events.forEach(event => {
                if (event.segs) {
                    const startMs = event.tStartMs || 0;
                    const startSeconds = Math.floor(startMs / 1000);

                    // Add timestamp marker every 30 seconds for AI reference
                    if (startSeconds >= lastTimestamp + 30 || lastTimestamp === -1) {
                        const timestamp = formatTime(startMs);
                        timestampedTranscript += `\n[${timestamp}] `;
                        lastTimestamp = startSeconds;
                    }

                    event.segs.forEach(seg => {
                        const text = seg.utf8 || '';
                        const cleanText = text.replace(/\s+/g, ' ').trim();
                        if (cleanText && cleanText !== '\n') {
                            fullTranscript += cleanText + ' ';
                            timestampedTranscript += cleanText + ' ';
                        }
                    });
                }
            });
        }

        // Store video duration from last timestamp for validation
        if (transcriptJson.events && transcriptJson.events.length > 0) {
            const lastEvent = transcriptJson.events[transcriptJson.events.length - 1];
            if (lastEvent.tStartMs) {
                data.videoDuration = formatTime(lastEvent.tStartMs);
            }
        }

        // Use timestamped transcript for AI - 200K chars supports 2+ hour videos
        data.transcript = timestampedTranscript.trim().substring(0, 200000); // 200K chars for 2+ hour videos

        return data;

    } catch (error) {
        console.error('YouTube extraction error:', error);
        // Return what we have, even if incomplete
        data.error = error.message;
        return data;
    }
}
```

## File: `js/content-extractor.js`
```javascript
/**
 * Product Content Extractor
 * Intelligently extracts product information from various e-commerce sites
 * Used within the context of the page during scripting.executeScript
 */

export function extractProductData() {
    const data = {
        title: '',
        price: '',
        description: '',
        specs: [],
        url: window.location.href,
        siteName: window.location.hostname
    };

    // 1. Extract Title
    data.title = document.querySelector('h1')?.textContent?.trim() ||
        document.querySelector('[data-testid="product-title"]')?.textContent?.trim() ||
        document.querySelector('.product-title')?.textContent?.trim() ||
        document.querySelector('meta[property="og:title"]')?.content ||
        document.title;

    // 2. Extract Price
    const priceSelectors = [
        '[data-price]',
        '.price',
        '.product-price',
        '[class*="price-item"]',
        '[class*="Price"]',
        '[id*="price"]',
        '.a-price-whole', // Amazon
        '.pdp-price',
        '[data-testid="price"]'
    ];
    for (const sel of priceSelectors) {
        const el = document.querySelector(sel);
        if (el?.textContent && el.textContent.trim().length > 0) {
            data.price = el.textContent.trim();
            break;
        }
    }

    // 3. Extract Description
    const descSelectors = [
        '[data-testid="product-description"]',
        '.product-description',
        '#product-description',
        '[class*="description"]',
        'meta[name="description"]',
        '#feature-bullets' // Amazon
    ];
    for (const sel of descSelectors) {
        const el = document.querySelector(sel);
        if (el) {
            const content = el.content || el.textContent?.trim();
            if (content && content.length > 20) {
                data.description = content;
                break;
            }
        }
    }

    // 4. Extract Specifications / Features
    const specContainers = document.querySelectorAll('table, dl, ul.specs, .specifications, .technical-details, #productDetails_techSpec_section_1');
    specContainers.forEach(container => {
        const text = container.innerText.trim();
        if (text.length > 50 && data.specs.length < 5) { // Limit to 5 meaningful blocks
            data.specs.push(text.substring(0, 1000));
        }
    });

    // 5. Fallback: Get significant text content if description is thin
    if (!data.description || data.description.length < 100) {
        const mainContent = document.querySelector('main, #content, .main-content, article');
        if (mainContent) {
            data.description = mainContent.innerText.substring(0, 2000).trim();
        }
    }

    return {
        title: data.title,
        price: data.price,
        description: data.description,
        specs: data.specs,
        url: data.url,
        siteName: data.siteName,
        rawContent: `
Title: ${data.title}
Price: ${data.price}
URL: ${data.url}
Site: ${data.siteName}

Description:
${data.description}

Specifications:
${data.specs.join('\n\n')}
        `.trim()
    };
}
```

## File: `js/duplicate-highlighter.js`
```javascript
/**
 * Duplicate Link Highlighter Module
 * Highlights links that appear more than once on the page.
 */

const DuplicateHighlighter = (() => {
    let highlightedElements = [];
    let observer = null;

    /**
     * Generates a random color using HSL for better control over lightness and saturation.
     * Ensures the color is vibrant and not too close to black or white.
     */
    function getRandomColor() {
        const hue = Math.floor(Math.random() * 360);
        const saturation = 75 + Math.floor(Math.random() * 25); // 75-100%
        const lightness = 45 + Math.floor(Math.random() * 10); // 45-55%
        return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
    }

    /**
     * Scans the page for links, identifies duplicates by their href,
     * and applies a colored underline to them.
     */
    function highlightDuplicates() {
        // We don't necessarily want to clear everything if we are doing incremental updates,
        // but for simplicity and correctness with dynamic content, we clear and re-apply.
        clearHighlights();

        // Use utility function if available to include Shadow DOM links
        const links = typeof getAllLinks === 'function' ? getAllLinks() : Array.from(document.querySelectorAll('a[href]'));
        const linkGroups = {};

        links.forEach(link => {
            // Get absolute URL
            try {
                const href = link.href;
                // Skip empty, anchors, or javascript links
                if (!href || href.startsWith('javascript:') || href.startsWith('data:') || href === window.location.href + '#') return;
                
                // Normalizing URL (removing trailing slash for better matching)
                const normalizedHref = href.replace(/\/$/, "");

                if (!linkGroups[normalizedHref]) {
                    linkGroups[normalizedHref] = [];
                }
                linkGroups[normalizedHref].push(link);
            } catch (e) {
                // Ignore invalid URLs
            }
        });

        Object.keys(linkGroups).forEach(href => {
            const group = linkGroups[href];
            if (group.length > 1) {
                const color = getRandomColor();
                group.forEach(link => {
                    // Apply highlight using border-bottom
                    // We use !important to ensure it shows up over site styles
                    link.style.setProperty('border-bottom', `3px solid ${color}`, 'important');
                    link.classList.add('grabbit-duplicate-highlight');
                    highlightedElements.push(link);
                });
            }
        });
    }

    /**
     * Removes all highlights applied by this module.
     */
    function clearHighlights() {
        highlightedElements.forEach(el => {
            if (el) {
                el.style.removeProperty('border-bottom');
                el.classList.remove('grabbit-duplicate-highlight');
            }
        });
        highlightedElements = [];
    }

    /**
     * Initializes the module based on user settings.
     */
    function init() {
        chrome.storage.sync.get(['duplicateHighlighterEnabled', 'disabledDomains'], (result) => {
            // Use utility function if available, otherwise fallback
            const isDisabled = typeof isDomainDisabled === 'function' 
                ? isDomainDisabled(result.disabledDomains || [])
                : false;

            if (isDisabled) {
                console.log('Grabbit Duplicate Highlighter: Disabled on this domain.');
                return;
            }

            if (result.duplicateHighlighterEnabled) {
                console.log('Grabbit: Duplicate Highlighter enabled. Scanning page...');
                
                // Initial highlight
                highlightDuplicates();

                // Setup observer for dynamic content (infinite scroll, etc.)
                // Use debounce from utils.js if available
                const debounceFunc = typeof debounce === 'function' ? debounce : (fn, ms) => {
                    let timeout;
                    return (...args) => {
                        clearTimeout(timeout);
                        timeout = setTimeout(() => fn.apply(this, args), ms);
                    };
                };

                if (observer) observer.disconnect();
                
                observer = new MutationObserver(debounceFunc(() => {
                    highlightDuplicates();
                }, 1000));
                
                observer.observe(document.body, { childList: true, subtree: true });
            } else {
                clearHighlights();
                if (observer) {
                    observer.disconnect();
                    observer = null;
                }
            }
        });

        // Listen for settings changes
        chrome.storage.onChanged.addListener((changes, area) => {
            if (area === 'sync' && changes.duplicateHighlighterEnabled) {
                init(); // Re-initialize when setting changes
            }
        });
    }

    return {
        init,
        clearHighlights
    };
})();

// Auto-init
if (typeof window !== 'undefined') {
    DuplicateHighlighter.init();
}
```

## File: `js/grabbit.js`
```javascript
/**
 * Grabbit V2.0.0
 * An improved version of the Grabbit Chrome extension for selecting and manipulating multiple links
 * with enhanced performance, better code organization, and improved user experience.
 *
 * This content script provides the core functionality for selecting multiple links on a webpage
 * by drawing a selection box with the mouse while holding specific key combinations.
 *
 * @author Grabbit Team
 * @version 2.0.0
 */

//=============================================================================
// INITIALIZATION
//=============================================================================

/**
 * Load saved actions from chrome storage on initialization
 */
chrome.storage.sync.get(['savedActions', 'boxColor', 'exclusionFilters', 'linkTextExclusionFilters', 'disabledDomains'], function (result) {
  GrabbitState.savedActions = result.savedActions || [];
  GrabbitState.exclusionFilters = result.exclusionFilters || [];
  GrabbitState.linkTextExclusionFilters = result.linkTextExclusionFilters || [];
  GrabbitState.disabledDomains = result.disabledDomains || [];

  // Check if disabled
  if (isDomainDisabled(GrabbitState.disabledDomains)) {
    GrabbitState.isDisabled = true;
    console.log('Grabbit: Disabled on this domain.');
    return; // Stop further initialization if necessary
  }

  compileExclusionFilters();
  compileLinkTextExclusionFilters();
});

/**
 * Compiles URL exclusion filter patterns into RegExp objects for performance.
 * Falls back to substring matching for invalid regex patterns.
 */
function compileExclusionFilters() {
  GrabbitState.compiledExclusionFilters = GrabbitState.exclusionFilters.map(pattern => {
    try {
      // Try to compile as regex with case-insensitive flag
      return { regex: new RegExp(pattern, 'i'), pattern: pattern };
    } catch (e) {
      // Invalid regex - will use substring matching
      return { regex: null, pattern: pattern };
    }
  });
}

/**
 * Compiles link text exclusion filter patterns into RegExp objects for performance.
 * Falls back to substring matching for invalid regex patterns.
 */
function compileLinkTextExclusionFilters() {
  GrabbitState.compiledLinkTextExclusionFilters = GrabbitState.linkTextExclusionFilters.map(pattern => {
    try {
      // Try to compile as regex with case-insensitive flag
      return { regex: new RegExp(pattern, 'i'), pattern: pattern };
    } catch (e) {
      // Invalid regex - will use substring matching
      return { regex: null, pattern: pattern };
    }
  });
}


//=============================================================================
// EVENT LISTENERS
//=============================================================================

/**
 * Handles the mousedown event to start the selection process
 */
document.addEventListener('mousedown', (e) => {
  if (GrabbitState.isDisabled) return;
  const mouseButton = getMouseButton(e);
  GrabbitState.currentMouseButton = mouseButton; // Store the initial mouse button

  const matchedAction = checkKeyCombination(e, mouseButton); // Check for matching action

  if (matchedAction) {
    GrabbitState.currentMatchedAction = matchedAction;
    GrabbitState.isMouseDown = true;
    GrabbitState.isSelectionActive = false; // Selection not active until threshold is crossed
    GrabbitState.startX = e.clientX;
    GrabbitState.startY = e.clientY + window.scrollY; // Add scroll offset to initial Y position
    GrabbitState.initialScrollY = window.scrollY;
    e.preventDefault();
  }
});

/**
 * Activates the selection UI after drag threshold is crossed.
 * This function is called from mousemove when the user has dragged far enough.
 */
function activateSelection() {
  GrabbitState.isSelectionActive = true;

  // PRE-CACHE LINKS
  // We do this once when selection activates to avoid expensive DOM queries
  // and getBoundingClientRect during the drag operation.
  const scrollX = window.scrollX;
  const scrollY = window.scrollY;

  // Query all links (including those in Shadow DOM)
  const allLinks = getAllLinks();
  GrabbitState.cachedLinks = [];

  allLinks.forEach(link => {
    // Skip links without href
    if (!link.href) return;

    // Skip nested links (links that are descendants of other links)
    // This prevents selecting duplicate/internal links like those in Google search results
    let isNested = false;
    let parentElement = link.parentElement;
    while (parentElement && parentElement !== document.body) {
      if (parentElement.tagName === 'A') {
        isNested = true;
        break;
      }
      parentElement = parentElement.parentElement;
    }
    if (isNested) return;

    // On Google Search pages, filter out Google's internal navigation/tracking links
    // This only affects google.com/search pages - other sites are unaffected
    const isGoogleSearch = window.location.hostname.includes('google.') &&
      window.location.pathname.startsWith('/search');
    if (isGoogleSearch) {
      try {
        const linkUrl = new URL(link.href);
        const linkHost = linkUrl.hostname.toLowerCase();
        // Skip Google internal links (search, tracking, books, ngrams, etc.)
        if (linkHost.includes('google.') &&
          (linkUrl.pathname.startsWith('/search') ||
            linkUrl.pathname.startsWith('/url') ||
            linkHost.includes('books.google') ||
            linkHost.includes('ngrams'))) {
          return;
        }
      } catch (e) {
        // Invalid URL, skip it
        return;
      }
    }

    // Visibility check
    // Note: getComputedStyle can be expensive, but doing it once on activation
    // is much better than on every mousemove
    const style = window.getComputedStyle(link);
    if (style.display === 'none' || style.visibility === 'hidden' || style.opacity === '0') {
      return;
    }

    // Sticky/Fixed check
    const isYouTubeSubscription = window.location.hostname.includes('youtube.com') &&
      (link.href.includes('/channel/') || link.href.includes('/c/') ||
        link.href.includes('/user/') || link.href.includes('@'));

    if (!isYouTubeSubscription && isElementSticky(link)) {
      return;
    }

    // Get dimensions
    let clientRect = link.getBoundingClientRect();
    if ((clientRect.width === 0 || clientRect.height === 0) && link.children.length > 0) {
      clientRect = link.children[0].getBoundingClientRect();
    }

    if (clientRect.width === 0 && clientRect.height === 0) return;

    // Check if link is "important" (using SmartSelect heuristics)
    const isImportant = SmartSelect.isLinkImportant(link, style);

    // Generate signature for adaptive smart select
    const signature = SmartSelect.getLinkSignature(link, style);

    // Store document-relative coordinates and importance flag
    GrabbitState.cachedLinks.push({
      link: link,
      box: {
        top: clientRect.top + scrollY,
        bottom: clientRect.bottom + scrollY,
        left: clientRect.left + scrollX,
        right: clientRect.right + scrollX
      },
      isImportant: isImportant,
      signature: signature
    });
  });

  const matchedAction = GrabbitState.currentMatchedAction;
  GrabbitState.selectionBox = createSelectionBox();

  // Apply border styling
  const borderThickness = matchedAction.borderThickness || 2;
  const borderStyle = matchedAction.borderStyle || 'solid';
  GrabbitState.selectionBox.style.border = `${borderThickness}px ${borderStyle}`;
  GrabbitState.selectionBox.style.borderColor = matchedAction.boxColor;
  GrabbitState.selectionBox.style.backgroundColor = `${matchedAction.boxColor}19`;
  GrabbitState.selectionBox.style.position = 'absolute';
  GrabbitState.selectionBox.style.left = `${GrabbitState.startX}px`;
  GrabbitState.selectionBox.style.top = `${GrabbitState.startY}px`; // Use absolute position from document top
  document.body.appendChild(GrabbitState.selectionBox);
  GrabbitState.counterLabel = createCounterLabel();
  document.body.appendChild(GrabbitState.counterLabel);
  GrabbitState.selectedLinks.clear();

  // Start periodic link re-caching to detect dynamically loaded content
  GrabbitState.linkRefreshInterval = setInterval(() => {
    refreshCachedLinks();
  }, CONSTANTS.LINK_REFRESH_INTERVAL);
}

/**
 * Refreshes the cached links to detect any new links that appeared
 * (e.g., from lazy loading, infinite scroll, or dynamic content).
 * This is called periodically while the selection is active.
 */
function refreshCachedLinks() {
  if (!GrabbitState.isSelectionActive) return;

  const scrollX = window.scrollX;
  const scrollY = window.scrollY;

  // Get current cached link elements for comparison
  const existingLinkElements = new Set(GrabbitState.cachedLinks.map(item => item.link));

  // Query all links (including those in Shadow DOM)
  const allLinks = getAllLinks();

  allLinks.forEach(link => {
    // Skip if already cached
    if (existingLinkElements.has(link)) return;

    // Skip links without href
    if (!link.href) return;

    // Skip nested links (links that are descendants of other links)
    let isNested = false;
    let parentElement = link.parentElement;
    while (parentElement && parentElement !== document.body) {
      if (parentElement.tagName === 'A') {
        isNested = true;
        break;
      }
      parentElement = parentElement.parentElement;
    }
    if (isNested) return;

    // On Google Search pages, filter out Google's internal navigation/tracking links
    const isGoogleSearch = window.location.hostname.includes('google.') &&
      window.location.pathname.startsWith('/search');
    if (isGoogleSearch) {
      try {
        const linkUrl = new URL(link.href);
        const linkHost = linkUrl.hostname.toLowerCase();
        if (linkHost.includes('google.') &&
          (linkUrl.pathname.startsWith('/search') ||
            linkUrl.pathname.startsWith('/url') ||
            linkHost.includes('books.google') ||
            linkHost.includes('ngrams'))) {
          return;
        }
      } catch (e) {
        return;
      }
    }

    // Visibility check
    const style = window.getComputedStyle(link);
    if (style.display === 'none' || style.visibility === 'hidden' || style.opacity === '0') {
      return;
    }

    // Sticky/Fixed check
    const isYouTubeSubscription = window.location.hostname.includes('youtube.com') &&
      (link.href.includes('/channel/') || link.href.includes('/c/') ||
        link.href.includes('/user/') || link.href.includes('@'));

    if (!isYouTubeSubscription && isElementSticky(link)) {
      return;
    }

    // Get dimensions
    let clientRect = link.getBoundingClientRect();
    if ((clientRect.width === 0 || clientRect.height === 0) && link.children.length > 0) {
      clientRect = link.children[0].getBoundingClientRect();
    }

    if (clientRect.width === 0 && clientRect.height === 0) return;

    // Check if link is "important" (using SmartSelect heuristics)
    const isImportant = SmartSelect.isLinkImportant(link, style);

    // Generate signature for adaptive smart select
    const signature = SmartSelect.getLinkSignature(link, style);

    // Add to cache with document-relative coordinates
    GrabbitState.cachedLinks.push({
      link: link,
      box: {
        top: clientRect.top + scrollY,
        bottom: clientRect.bottom + scrollY,
        left: clientRect.left + scrollX,
        right: clientRect.right + scrollX
      },
      isImportant: isImportant,
      signature: signature
    });
  });

  // Trigger link selection update to include any new links
  debouncedUpdateLinks();
}

/**
 * Handles the mousemove event to update the selection box
 */
document.addEventListener('mousemove', (e) => {
  if (GrabbitState.isDisabled) return;
  if (!GrabbitState.isMouseDown) return;

  const currentX = e.clientX;
  const currentY = e.clientY + window.scrollY; // Add scroll offset to current Y position
  GrabbitState.lastMouseX = currentX;
  GrabbitState.lastMouseY = e.clientY; // Store viewport Y position for scroll handling

  // Check if we need to activate selection (threshold check)
  if (!GrabbitState.isSelectionActive) {
    // Calculate distance from start position (using viewport coordinates for consistency)
    const distance = Math.hypot(currentX - GrabbitState.startX, currentY - GrabbitState.startY);

    // If below threshold, don't activate yet
    if (distance < CONSTANTS.DRAG_THRESHOLD) {
      return;
    }

    // Threshold crossed - activate selection
    activateSelection();
  }

  // At this point, selection is active - proceed with normal logic
  if (!GrabbitState.selectionBox) return;

  // Calculate box dimensions using absolute positions
  const left = Math.min(GrabbitState.startX, currentX);
  const top = Math.min(GrabbitState.startY, currentY);
  const width = Math.abs(currentX - GrabbitState.startX);
  const height = Math.abs(currentY - GrabbitState.startY);

  // Update selection box position and size
  GrabbitState.selectionBox.style.left = `${left}px`;
  GrabbitState.selectionBox.style.top = `${top}px`;
  GrabbitState.selectionBox.style.width = `${width}px`;
  GrabbitState.selectionBox.style.height = `${height}px`;

  handleScroll(e.clientY);

  // Use debounced version for link selection
  debouncedUpdateLinks();

  if (GrabbitState.counterLabel) {
    GrabbitState.counterLabel.style.left = `${e.clientX}px`;
    GrabbitState.counterLabel.style.top = `${e.clientY}px`;
    updateVisualStyles();
  }
});

/**
 * Handles the mouseup event to finalize the selection
 */
document.addEventListener('mouseup', (e) => {
  if (GrabbitState.isDisabled) return;
  // Clear any scroll interval
  if (GrabbitState.scrollInterval) {
    clearInterval(GrabbitState.scrollInterval);
    GrabbitState.scrollInterval = null;
  }

  if (!GrabbitState.isMouseDown) return;

  // Prevent default context menu if links are selected and right mouse clicked or if selection box is a bit big
  if (e.button === 2 && GrabbitState.selectedLinks.size > 0 ||
    (GrabbitState.selectionBox && GrabbitState.selectionBox.offsetWidth > 100 && GrabbitState.selectionBox.offsetHeight > 100)) {
    document.addEventListener('contextmenu', function preventContextMenu(e) {
      e.preventDefault();
      document.removeEventListener('contextmenu', preventContextMenu);
    }, { once: true });
  }

  // Use the action that started (or was active during) the selection, not the current key state.
  // This fixes the case where the user releases the modifier key (e.g. Ctrl) before releasing
  // the mouse button — the selection should still be processed with the original action.
  const actionToUse = GrabbitState.currentMatchedAction;

  // Process selected links only if selection was actually activated and there's a matched action
  if (GrabbitState.isSelectionActive && actionToUse && GrabbitState.selectedLinks.size > 0) {
    processSelectedLinks(actionToUse);
  }

  // Clean up
  cleanupSelection();
});

/**
 * Prevents the default right-click menu when using right mouse button during selection
 */
document.addEventListener('contextmenu', (e) => {
  if (GrabbitState.isMouseDown) {
    e.preventDefault();
  }
});

/**
 * Handles keydown events during selection to update the action
 */
document.addEventListener('keydown', (e) => {
  if (GrabbitState.isDisabled) return;
  // Track letter keys (A-Z) for modifier key support
  if (e.key && e.key.length === 1 && /^[a-z]$/i.test(e.key)) {
    GrabbitState.pressedKeys.add(e.key.toLowerCase());
  }

  // Handle ESC key to cancel selection
  // Cancel if ESC is pressed during mouse down OR with any modifier key held
  if (e.key === 'Escape') {
    if (GrabbitState.isMouseDown || GrabbitState.isSelectionActive) {
      // Always prevent the page from reacting to ESC while Grabbit is active
      e.preventDefault();
      e.stopPropagation();
      cleanupSelection();
      return;
    }
  }

  // Handle key combinations during selection
  if (GrabbitState.isMouseDown && GrabbitState.selectionBox) {
    const newMatchedAction = checkKeyCombination(e, GrabbitState.currentMouseButton);

    // Store current action before switching
    if (!GrabbitState.previousAction) {
      GrabbitState.previousAction = GrabbitState.currentMatchedAction;
    }

    // Update to new action if found
    if (newMatchedAction) {
      GrabbitState.previousAction = GrabbitState.currentMatchedAction;
      GrabbitState.currentMatchedAction = newMatchedAction;
      updateVisualStyles();
    }
  }
});

/**
 * Handles keyup events during selection to revert to previous action
 */
document.addEventListener('keyup', (e) => {
  if (GrabbitState.isDisabled) return;
  // Remove letter keys from pressedKeys when released
  if (e.key && e.key.length === 1 && /^[a-z]$/i.test(e.key)) {
    GrabbitState.pressedKeys.delete(e.key.toLowerCase());
  }

  if (GrabbitState.isMouseDown && GrabbitState.selectionBox) {
    const currentKeyState = {
      ctrlKey: e.ctrlKey,
      shiftKey: e.shiftKey,
      altKey: e.altKey,
      metaKey: e.metaKey
    };

    const matchedAction = checkKeyCombination(currentKeyState, GrabbitState.currentMouseButton);
    GrabbitState.currentMatchedAction = matchedAction || GrabbitState.previousAction || GrabbitState.currentMatchedAction;
    updateVisualStyles();
  }
});

/**
 * Cleans up the selection when the window loses focus
 */
window.addEventListener('blur', () => {
  GrabbitState.pressedKeys.clear(); // Clear all pressed letter keys
  cleanupSelection();
});

/**
 * Listens for changes in storage to update settings in real-time
 */
chrome.storage.onChanged.addListener((changes, namespace) => {
  if (namespace === 'sync') {
    // Update savedActions if they changed
    if (changes.savedActions) {
      GrabbitState.savedActions = changes.savedActions.newValue;
    }

    // Update boxColor if it changed
    if (changes.boxColor) {
      // Update any active selection boxes with new color
      if (GrabbitState.selectionBox) {
        GrabbitState.selectionBox.style.borderColor = changes.boxColor.newValue;
        GrabbitState.selectionBox.style.backgroundColor = `${changes.boxColor.newValue}19`;
      }

      // Update highlighted links with new color
      GrabbitState.selectedLinks.forEach(link => {
        link.style.backgroundColor = `${changes.boxColor.newValue}33`;
      });
    }

    // Update URL exclusionFilters if they changed
    if (changes.exclusionFilters) {
      GrabbitState.exclusionFilters = changes.exclusionFilters.newValue || [];
      compileExclusionFilters();
    }

    // Update linkTextExclusionFilters if they changed
    if (changes.linkTextExclusionFilters) {
      GrabbitState.linkTextExclusionFilters = changes.linkTextExclusionFilters.newValue || [];
      compileLinkTextExclusionFilters();
    }
  }
});
```

## File: `js/linkify.js`
```javascript
/**
 * Linkify Module
 * Scans the document for plain text URLs and converts them to clickable links.
 */

const Linkify = (() => {
    // Regex for matching URLs. This is a simplified version, can be robustified.
    // Matches http/https/ftp or www.
    const URL_REGEX = /((?:https?|ftp):\/\/[^\s/$.?#].[^\s]*)|(www\.[^\s/$.?#].[^\s]*)/gi;

    const BLACKLIST_TAGS = ['A', 'SCRIPT', 'STYLE', 'TEXTAREA', 'INPUT', 'BUTTON', 'SELECT', 'OPTION'];

    function linkifyNode(node) {
        if (node.nodeType === Node.TEXT_NODE) {
            if (node.parentNode && BLACKLIST_TAGS.includes(node.parentNode.tagName)) {
                return;
            }

            const text = node.textContent;
            if (!text || text.trim().length === 0) return;

            // Basic check to see if we even need to regex
            if (!text.includes('http') && !text.includes('www.')) return;

            if (URL_REGEX.test(text)) {
                const fragment = document.createDocumentFragment();
                let lastIndex = 0;

                // Reset regex state
                URL_REGEX.lastIndex = 0;

                let match;
                let foundMatch = false;

                // We need to re-run execution because simple .test() advances index if global
                // But safer to just use matchAll or a loop with exec

                // clone regex to avoid side effects
                const regex = new RegExp(URL_REGEX);

                while ((match = regex.exec(text)) !== null) {
                    foundMatch = true;

                    // Text before match
                    if (match.index > lastIndex) {
                        fragment.appendChild(document.createTextNode(text.slice(lastIndex, match.index)));
                    }

                    const url = match[0];
                    const fullUrl = url.startsWith('www.') ? 'http://' + url : url;

                    const a = document.createElement('a');
                    a.href = fullUrl;
                    a.textContent = url;
                    a.target = '_blank';
                    a.className = 'grabbit-linkified'; // Marker class
                    a.style.textDecoration = 'underline'; // Ensure visibility
                    fragment.appendChild(a);

                    lastIndex = regex.lastIndex;
                }

                if (foundMatch) {
                    // Remaining text
                    if (lastIndex < text.length) {
                        fragment.appendChild(document.createTextNode(text.slice(lastIndex)));
                    }
                    node.parentNode.replaceChild(fragment, node);
                }
            }
        } else if (node.nodeType === Node.ELEMENT_NODE) {
            if (BLACKLIST_TAGS.includes(node.tagName)) return;

            // Handle Shadow DOM
            if (node.shadowRoot) {
                linkifyContainer(node.shadowRoot);
            }

            // Recurse
            Array.from(node.childNodes).forEach(child => linkifyNode(child));
        }
    }

    function linkifyContainer(container) {
        Array.from(container.childNodes).forEach(child => linkifyNode(child));
    }

    function init() {
        chrome.storage.sync.get(['linkifyEnabled', 'linkifyAggressive', 'disabledDomains'], (result) => {
            if (result.disabledDomains && isDomainDisabled(result.disabledDomains)) {
                console.log('Grabbit Linkify: Disabled on this domain.');
                return;
            }

            if (result.linkifyEnabled) {
                console.log('Grabbit: Linkify enabled (Aggressive: ' + !!result.linkifyAggressive + '). Scanning page...');

                if (result.linkifyAggressive) {
                    // Aggressive regex: handles standard schemes AND domain-only patterns
                    // Now captures subdomains, paths, AND query parameters
                    // The path portion uses [^\s<>] to match paths/queries while avoiding HTML tags and whitespace
                    const AGGRESSIVE_REGEX = /((?:https?|ftp):\/\/[^\s/$.?#].[^\s]*)|(www\.[^\s/$.?#].[^\s]*)|([a-z0-9](?:[a-z0-9-]*[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)*\.[a-z]{2,}(?:[/][^\s<>]*)?)/gi;

                    // Closure to pass regex
                    function linkifyAggressiveNode(node) {
                        // Original linkifyNode uses URL_REGEX. We'll override the regex used in the loop.
                        // Since Linkify is a module with internal state, let's just re-implement or parameterize.
                        // For simplicity in this logic, we'll temporarily swap the REGEX or call a parameterized version.
                        linkifyNodeParam(node, AGGRESSIVE_REGEX);
                    }

                    linkifyContainerParam(document.body, AGGRESSIVE_REGEX);
                } else {
                    linkifyContainerParam(document.body, URL_REGEX);
                }
            }
        });
    }

    // Refactored to accept regex
    function linkifyNodeParam(node, regexToUse) {
        if (node.nodeType === Node.TEXT_NODE) {
            if (node.parentNode && BLACKLIST_TAGS.includes(node.parentNode.tagName)) {
                return;
            }

            const text = node.textContent;
            if (!text || text.trim().length === 0) return;

            // Adjust quick check
            const hasPossibleLink = text.includes('http') || text.includes('www.') || text.includes('.');
            if (!hasPossibleLink) return;

            const regex = new RegExp(regexToUse);
            let match;
            let foundMatch = false;
            const fragment = document.createDocumentFragment();
            let lastIndex = 0;

            while ((match = regex.exec(text)) !== null) {
                foundMatch = true;

                if (match.index > lastIndex) {
                    fragment.appendChild(document.createTextNode(text.slice(lastIndex, match.index)));
                }

                const url = match[0];
                let fullUrl = url;
                if (url.startsWith('www.')) {
                    fullUrl = 'http://' + url;
                } else if (!url.includes('://')) {
                    fullUrl = 'http://' + url;
                }

                const a = document.createElement('a');
                a.href = fullUrl;
                a.textContent = url;
                a.target = '_blank';
                a.className = 'grabbit-linkified';
                a.style.textDecoration = 'underline';
                fragment.appendChild(a);

                lastIndex = regex.lastIndex;
            }

            if (foundMatch) {
                if (lastIndex < text.length) {
                    fragment.appendChild(document.createTextNode(text.slice(lastIndex)));
                }
                node.parentNode.replaceChild(fragment, node);
            }
        } else if (node.nodeType === Node.ELEMENT_NODE) {
            if (BLACKLIST_TAGS.includes(node.tagName)) return;
            if (node.shadowRoot) linkifyContainerParam(node.shadowRoot, regexToUse);
            Array.from(node.childNodes).forEach(child => linkifyNodeParam(child, regexToUse));
        }
    }

    function linkifyContainerParam(container, regexToUse) {
        Array.from(container.childNodes).forEach(child => linkifyNodeParam(child, regexToUse));
    }

    return {
        init: init
    };
})();

// Auto-init if this script is loaded. 
// Depending on how we load it (module vs part of grabbit.js), we might call it differently.
// For now, let's expose it or run it.
if (typeof window !== 'undefined') {
    // If loaded as a standalone content script
    Linkify.init();
}
```

## File: `js/logic.js`
```javascript
//=============================================================================
// SELECTION BOX AND SCROLLING MANAGEMENT
//=============================================================================

/**
 * Updates the selection box position and size during scrolling
 */
function updateSelectionBox() {
    if (!GrabbitState.selectionBox || !GrabbitState.isMouseDown) return;

    // Get current scroll position
    const currentScroll = window.scrollY;
    GrabbitState.currentScrollY = currentScroll;

    // Calculate positions relative to the document
    const documentStartY = GrabbitState.startY;
    const documentCurrentY = GrabbitState.lastMouseY + currentScroll - GrabbitState.initialScrollY;

    // Calculate box dimensions relative to document
    const left = Math.min(GrabbitState.startX, GrabbitState.lastMouseX);
    const top = Math.min(documentStartY, documentCurrentY);
    const width = Math.abs(GrabbitState.lastMouseX - GrabbitState.startX);
    const height = Math.abs(documentCurrentY - documentStartY);

    // Update selection box position and size
    GrabbitState.selectionBox.style.position = 'absolute';
    GrabbitState.selectionBox.style.left = `${left}px`;
    GrabbitState.selectionBox.style.top = `${top}px`;
    GrabbitState.selectionBox.style.width = `${width}px`;
    GrabbitState.selectionBox.style.height = `${height}px`;

    // Update link selection using debounced function
    debouncedUpdateLinks();
}

/**
 * Handles auto-scrolling when the mouse is near the viewport edges
 * @param {number} mouseY - The current mouse Y position
 */
function handleScroll(mouseY) {
    const viewportHeight = window.innerHeight;
    const scrollTop = window.scrollY;
    const pageHeight = document.documentElement.scrollHeight;

    // Calculate distances from viewport edges
    const distanceFromTop = mouseY;
    const distanceFromBottom = viewportHeight - mouseY;

    // Clear any existing scroll interval
    if (GrabbitState.scrollInterval) {
        clearInterval(GrabbitState.scrollInterval);
        GrabbitState.scrollInterval = null;
    }

    // Start scrolling if within threshold and page has more content
    if (distanceFromTop < CONSTANTS.SCROLL_THRESHOLD || distanceFromBottom < CONSTANTS.SCROLL_THRESHOLD) {
        GrabbitState.scrollInterval = setInterval(() => {
            if (distanceFromTop < CONSTANTS.SCROLL_THRESHOLD && scrollTop > 0) {
                // Scroll up if not at top
                window.scrollBy(0, -CONSTANTS.SCROLL_SPEED);
                updateSelectionBox();
            } else if (distanceFromBottom < CONSTANTS.SCROLL_THRESHOLD &&
                (scrollTop + viewportHeight) < pageHeight) {
                // Scroll down only if not at bottom
                window.scrollBy(0, CONSTANTS.SCROLL_SPEED);
                updateSelectionBox();
            }
        }, CONSTANTS.SCROLL_INTERVAL);
    }
}

//=============================================================================
// LINK SELECTION AND HIGHLIGHTING
//=============================================================================

/**
 * Checks if a string matches any compiled URL exclusion filter.
 * Used for both href and link text when applying URL filters.
 */
function urlFilterMatchesText(text, filters) {
    if (!filters || filters.length === 0) return { matched: false };
    const lower = text.toLowerCase();
    for (let i = 0; i < filters.length; i++) {
        const filter = filters[i];
        const matched = filter.regex
            ? filter.regex.test(text)
            : lower.includes(filter.pattern.toLowerCase());
        if (matched) return { matched: true, pattern: filter.pattern };
    }
    return { matched: false };
}

/**
 * Checks if a link URL or visible text matches any URL exclusion filter.
 * Uses pre-compiled RegExp objects for performance.
 * Falls back to substring matching for invalid regex patterns.
 * @param {Element} link - The anchor element to check
 * @returns {boolean} True if the link should be excluded
 */
function isLinkExcluded(link) {
    const filters = GrabbitState.compiledExclusionFilters;
    if (!filters || filters.length === 0) return false;

    const url = link.href || '';
    let result = urlFilterMatchesText(url, filters);
        if (result.matched) return true;

    const linkText = getLinkTextForFiltering(link);
    if (linkText) {
        result = urlFilterMatchesText(linkText, filters);
        if (result.matched) return true;
    }
    return false;
}

/**
 * Checks if a link's visible text matches any link text exclusion filter.
 * Uses pre-compiled RegExp objects for performance.
 * Falls back to substring matching for invalid regex patterns.
 * @param {Element} link - The anchor element to check
 * @returns {boolean} True if the link should be excluded
 */
function isLinkTextExcluded(link) {
    const filters = GrabbitState.compiledLinkTextExclusionFilters;
    if (!filters || filters.length === 0) return false;

    const text = getLinkTextForFiltering(link);
    if (!text) return false;

    for (let i = 0; i < filters.length; i++) {
        const filter = filters[i];
        const matched = filter.regex
            ? filter.regex.test(text)
            : text.toLowerCase().includes(filter.pattern.toLowerCase());
        if (matched) return true;
    }
    return false;
}

/**
 * Derives visible text for a link (anchor text, aria-label, title, or image alt) for filtering.
 * @param {Element} link - The anchor element
 * @returns {string} The derived text
 */
function getLinkTextForFiltering(link) {
    if (!link) return '';

    const textContent = (link.textContent || '').trim().replace(/\s+/g, ' ');
    if (textContent) return textContent;

    const ariaLabel = (link.getAttribute && link.getAttribute('aria-label')) ? link.getAttribute('aria-label').trim() : '';
    if (ariaLabel) return ariaLabel;

    const title = (link.getAttribute && link.getAttribute('title')) ? link.getAttribute('title').trim() : '';
    if (title) return title;

    const img = link.querySelector ? link.querySelector('img') : null;
    if (img) {
        const alt = (img.getAttribute && img.getAttribute('alt')) ? img.getAttribute('alt').trim() : '';
        if (alt) return alt;

        const imgAria = (img.getAttribute && img.getAttribute('aria-label')) ? img.getAttribute('aria-label').trim() : '';
        if (imgAria) return imgAria;
    }

    return '';
}

/**
 * Updates the selected links based on the current selection box
 * Uses SmartSelect module for pattern-based adaptive filtering.
 * Also applies exclusion filters to skip matching links.
 */
function updateSelectedLinks() {
    if (!GrabbitState.selectionBox || !GrabbitState.isMouseDown) return;

    // Get current selection box dimensions in document coordinates
    const boxLeft = parseInt(GrabbitState.selectionBox.style.left || 0);
    const boxTop = parseInt(GrabbitState.selectionBox.style.top || 0);
    const boxWidth = parseInt(GrabbitState.selectionBox.style.width || 0);
    const boxHeight = parseInt(GrabbitState.selectionBox.style.height || 0);

    const boxRight = boxLeft + boxWidth;
    const boxBottom = boxTop + boxHeight;

    // Check if smart select is enabled for current action
    const smartSelectEnabled = GrabbitState.currentMatchedAction?.smartSelect === 'on';

    // Collect all links in the selection box
    const linksInBox = [];

    GrabbitState.cachedLinks.forEach(item => {
        const { link, box, isImportant, signature } = item;

        // Skip links matching URL exclusion filters
        if (isLinkExcluded(link)) return;

        // Skip links matching link text exclusion filters
        if (isLinkTextExcluded(link)) return;

        // Check if link is within selection box
        const isInBox = !(box.left > boxRight ||
            box.right < boxLeft ||
            box.top > boxBottom ||
            box.bottom < boxTop);

        if (isInBox) {
            linksInBox.push({ link, isImportant, signature });
        }
    });

    // Clear previous selection
    GrabbitState.selectedLinks.forEach(link => {
        link.style.backgroundColor = '';
    });
    GrabbitState.selectedLinks.clear();

    // Determine which links to select
    let selectedLinkElements;

    if (smartSelectEnabled && linksInBox.length > 0) {
        // Use Smart Select pattern-based filtering
        selectedLinkElements = SmartSelect.apply(linksInBox);
    } else {
        // No smart select - select all links in box
        selectedLinkElements = linksInBox.map(item => item.link);
    }

    // Apply selection
    selectedLinkElements.forEach(link => {
        GrabbitState.selectedLinks.add(link);
        if (GrabbitState.currentMatchedAction) {
            link.style.backgroundColor = `${GrabbitState.currentMatchedAction.boxColor}33`;
        }
    });

    // Update the counter label after links selection changes
    updateVisualStyles();
}

// Create debounced version of updateSelectedLinks - depends on debounce from utils.js, so logic.js must be loaded after utils.js
const debouncedUpdateLinks = debounce(updateSelectedLinks, CONSTANTS.DEBOUNCE_DELAY);

//=============================================================================
// LINK PROCESSING
//=============================================================================

/**
 * Processes the selected links based on the matched action
 * @param {Object} matchedAction - The matched action configuration
 */
function processSelectedLinks(matchedAction) {
    if (!matchedAction || GrabbitState.selectedLinks.size === 0) return;

    let urls = Array.from(GrabbitState.selectedLinks).map(link => link.href);

    // Apply deduplication if avoidDuplicates is enabled (default: on for backward compatibility)
    const shouldDedupe = matchedAction.avoidDuplicates !== 'off';
    let finalUrls = shouldDedupe ? [...new Set(urls)] : urls;

    // Apply reverse order if enabled
    if (matchedAction.reverseOrder) {
        finalUrls = finalUrls.reverse();
    }

    if (matchedAction.openLinks) {
        // Send message to background script to handle tab creation
        chrome.runtime.sendMessage({
            action: 'createTabs',
            urls: finalUrls,
            delay: matchedAction.tabDelay || 0,
            openAtEnd: matchedAction.openAtEnd || false
        });
        // Mark links as visited (persistent storage) if enabled for this action
        if (matchedAction.markVisited) {
            markLinksAsGrabbitVisited(finalUrls, Array.from(GrabbitState.selectedLinks));
        }

    } else if (matchedAction.openWindow) {
        // Send message to background script to handle window creation
        chrome.runtime.sendMessage({
            action: 'openLinks',
            urls: finalUrls,
            delay: matchedAction.tabDelay || 0
        });
        // Mark links as visited (persistent storage) if enabled for this action
        if (matchedAction.markVisited) {
            markLinksAsGrabbitVisited(finalUrls, Array.from(GrabbitState.selectedLinks));
        }

    } else if (matchedAction.copyUrls) {
        // Copy URLs to clipboard
        navigator.clipboard.writeText(finalUrls.join('\n'));
    } else if (matchedAction.copyUrlsAndTitles) {
        // Format URLs and titles based on formatting options
        const urlsAndTitles = finalUrls.map(url => {
            const link = Array.from(GrabbitState.selectedLinks).find(l => l.href === url);
            const title = link.textContent.trim();

            // Get formatting options with defaults
            const formatPattern = matchedAction.formatPattern || 'titleFirst';
            const separatorType = matchedAction.separatorType || 'newline';
            const separatorCount = matchedAction.separatorCount || 1;

            // Handle JSON format separately (it ignores other separators)
            if (formatPattern === 'json') {
                return { title, url };
            }

            // Create separator based on type and count
            let separator;
            if (separatorType === 'newline') {
                separator = '\n'.repeat(separatorCount);
            } else if (separatorType === 'space') {
                separator = ' '.repeat(separatorCount);
            } else if (separatorType === 'tab') {
                separator = '\t'.repeat(separatorCount);
            } else if (separatorType === 'comma') {
                separator = ','.repeat(separatorCount);
            } else if (separatorType === 'dot') {
                separator = '.'.repeat(separatorCount);
            } else {
                separator = '\n'; // Fallback to newline
            }

            // Format based on pattern
            if (formatPattern === 'markdown') {
                return `[${title}](${url})`;
            } else if (formatPattern === 'titleFirst') {
                return `${title}${separator}${url}`;
            } else if (formatPattern === 'urlFirst') {
                return `${url}${separator}${title}`;
            } else {
                return `${title}${separator}${url}`; // Fallback to titleFirst
            }
        });

        let formattedText;
        if (matchedAction.formatPattern === 'json') {
            formattedText = JSON.stringify(urlsAndTitles);
        } else {
            // Get link separator count with default
            const linkSeparatorCount = matchedAction.linkSeparatorCount || 0;

            // Create link separator based on linkSeparatorCount
            const linkSeparator = linkSeparatorCount > 0 ? '\n'.repeat(linkSeparatorCount + 1) : '\n';

            // Join the formatted links with the appropriate separator
            formattedText = urlsAndTitles.join(linkSeparator);
        }

        navigator.clipboard.writeText(formattedText);
    } else if (matchedAction.copyTitles) {
        // Copy titles to clipboard
        const titles = finalUrls.map(url => {
            const link = Array.from(GrabbitState.selectedLinks).find(l => l.href === url);
            return link.textContent.trim();
        }).join('\n');

        navigator.clipboard.writeText(titles);
        navigator.clipboard.writeText(titles);
    } else if (matchedAction.createBookmarks) {
        // Create bookmarks in a folder named after the current page title
        const bookmarks = [];
        Array.from(GrabbitState.selectedLinks).forEach(link => {
            // Re-check if this link is in our finalUrls list (to respect dedupe/reverse)
            if (finalUrls.includes(link.href)) {
                bookmarks.push({
                    title: link.textContent.trim() || link.href, // Fallback to URL if title is empty
                    url: link.href
                });
            }
        });

        // If deduplication or reverse happened, we might have multiple links with same URL but different titles?
        // Actually, logic above iterates DOM elements.
        // Let's rely on mapping finalUrls back to titles to strictly follow the processed list (order/dedupe).

        const processedBookmarks = finalUrls.map(url => {
            // Find the first matching link element for this URL to get the title
            // (If we deduped, we just take the first one found)
            const linkElement = Array.from(GrabbitState.selectedLinks).find(l => l.href === url);
            const title = linkElement ? linkElement.textContent.trim() : '';

            return {
                title: title || url,
                url: url
            };
        });

        chrome.runtime.sendMessage({
            action: 'createBookmarks',
            bookmarks: processedBookmarks,
            folderName: document.title || 'Grabbit Bookmarks'
        });
    }

}
```

## File: `js/premium.js`
```javascript
/**
 * Grabbit Premium State Manager
 * Handles ExtPay integration and license validation
 */

import ExtPay from './ExtPay.js';

const EXTENSION_ID = 'grabbit-premium'; // Configured in ExtPay dashboard
const extpay = ExtPay(EXTENSION_ID);

export const Premium = {
    /**
     * Initialize ExtPay - call this in background.js
     */
    async init() {
        extpay.startBackground();
    },

    /**
     * Get current user payment status
     * @returns {Promise<{paid: boolean, email: string|null, trialActive: boolean}>}
     */
    async getUser() {
        try {
            const user = await extpay.getUser();
            return {
                paid: user.paid || false,
                email: user.email || null,
                trialActive: user.trialStartedAt && !user.paid,
                paidAt: user.paidAt || null
            };
        } catch (e) {
            console.error('ExtPay getUser error:', e);
            return { paid: false, email: null, trialActive: false };
        }
    },

    /**
     * Open ExtPay payment page
     */
    openPaymentPage() {
        extpay.openPaymentPage();
    },

    /**
     * Open ExtPay login page (for existing users)
     */
    openLoginPage() {
        extpay.openLoginPage();
    },

    /**
     * Validate license with WordPress backend
     * @param {string} email - User's email from ExtPay
     * @returns {Promise<{valid: boolean, remainingCredits: number}>}
     */
    async validateWithBackend(email) {
        try {
            const response = await fetch('https://grabbit.socratisp.com/wp-json/grabbit/v1/validate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email })
            });

            if (!response.ok) {
                throw new Error(`Backend validation failed: ${response.status}`);
            }

            return await response.json();
        } catch (e) {
            console.error('Backend validation error:', e);
            // In case of error (e.g. offline), we might want to default to denying or allowing based on ExtPay
            // For now, fail safe if ExtPay says paid
            return { valid: false, remainingCredits: 0 };
        }
    }
};
```

## File: `js/smart-select.js`
```javascript
//=============================================================================
// SMART SELECT MODULE
// Pattern-based adaptive link selection for Grabbit
//=============================================================================

const SmartSelect = (() => {
    /**
     * Helper to check visual prominence based on style object
     * @param {CSSStyleDeclaration} style - The computed style
     * @returns {boolean} True if visually prominent
     */
    function isVisuallyProminent(style) {
        const weight = style.fontWeight;
        if (weight === 'bold' || parseInt(weight) >= 600) {
            return true;
        }
        const fontSize = parseFloat(style.fontSize);
        if (fontSize >= 16) {
            return true;
        }
        return false;
    }

    /**
     * Determines if a link is "important" based on heuristics
     * (Headings, ARIA roles, Font weight/size, deep visual check)
     * @param {HTMLAnchorElement} link - The link element
     * @param {CSSStyleDeclaration} style - The computed style of the link
     * @returns {boolean} True if the link is considered important
     */
    function isLinkImportant(link, style) {
        const headingRegex = /^H[1-6]$/;

        // Check immediate parent
        if (link.parentElement && headingRegex.test(link.parentElement.tagName)) return true;

        // Walk up a few levels
        let parentNode = link.parentNode;
        for (let i = 0; i < 3 && parentNode && parentNode !== document.body; i++) {
            if (headingRegex.test(parentNode.nodeName)) {
                return true;
            }
            parentNode = parentNode.parentNode;
        }

        // ARIA Roles
        if (link.getAttribute('role') === 'heading') return true;
        if (link.closest && link.closest('[role="heading"]')) return true;

        // Visual Prominence (Self)
        if (isVisuallyProminent(style)) return true;

        // Deep Inspection (Children)
        if (link.querySelector('h1, h2, h3, h4, h5, h6')) return true;

        const children = Array.from(link.children);
        for (const child of children) {
            if (headingRegex.test(child.tagName)) return true;

            const childStyle = window.getComputedStyle(child);
            if (isVisuallyProminent(childStyle)) return true;

            if (child.children.length > 0) {
                const grandChildren = Array.from(child.children);
                for (const grandChild of grandChildren) {
                    if (headingRegex.test(grandChild.tagName)) return true;
                    const grandChildStyle = window.getComputedStyle(grandChild);
                    if (isVisuallyProminent(grandChildStyle)) return true;
                }
            }
        }

        return false;
    }

    /**
     * Generates a signature string for a link to identify its "type".
     * @param {HTMLAnchorElement} link - The link element
     * @param {CSSStyleDeclaration} style - The computed style of the link
     * @returns {string} A signature string for grouping
     */
    function getLinkSignature(link, style) {
        let structureType = 'standard';
        let primaryTag = 'A';

        // Check if it wraps a heading
        if (link.querySelector('h1, h2, h3, h4, h5, h6')) {
            structureType = 'wrapper-heading';
            primaryTag = link.querySelector('h1, h2, h3, h4, h5, h6').tagName;
        } else {
            // Check parent for heading
            const headingRegex = /^H[1-6]$/;
            let parentNode = link.parentNode;
            for (let i = 0; i < 3 && parentNode && parentNode !== document.body; i++) {
                if (headingRegex.test(parentNode.nodeName)) {
                    structureType = 'inside-heading';
                    primaryTag = parentNode.tagName;
                    break;
                }
                parentNode = parentNode.parentNode;
            }
        }

        const isBold = style.fontWeight === 'bold' || parseInt(style.fontWeight) >= 600;
        const fontSize = Math.round(parseFloat(style.fontSize) || 0);

        // Create a simple signature string
        // Format: structureType|primaryTag|isBold|fontSize
        return `${structureType}|${primaryTag}|${isBold}|${fontSize}`;
    }

    /**
     * Applies the simplified pattern-based Smart Select algorithm.
     * 
     * Logic:
     * - Count signature frequencies
     * - If no signature repeats (all unique): Select ALL links
     * - If signatures repeat:
     *   - Prioritize "important" repeating signatures
     *   - If no important ones, use all repeating signatures
     * 
     * @param {Array} linksInBox - Array of {link, isImportant, signature} objects
     * @returns {Array} Filtered array of link elements to select
     */
    function apply(linksInBox) {
        if (linksInBox.length === 0) return [];

        // Step 1: Build signature frequency map
        const signatureCounts = new Map();
        const importantSignatures = new Set();

        linksInBox.forEach(item => {
            const sig = item.signature;
            signatureCounts.set(sig, (signatureCounts.get(sig) || 0) + 1);
            if (item.isImportant) {
                importantSignatures.add(sig);
            }
        });

        // Step 2: Find repeating signatures (count >= 2)
        const repeatingSignatures = new Set();
        signatureCounts.forEach((count, sig) => {
            if (count >= 2) {
                repeatingSignatures.add(sig);
            }
        });

        // Step 3: Determine selection logic
        if (repeatingSignatures.size === 0) {
            // No repeats - select ALL links
            return linksInBox.map(item => item.link);
        }

        // Repeats exist - filter by importance
        const importantRepeating = new Set();
        repeatingSignatures.forEach(sig => {
            if (importantSignatures.has(sig)) {
                importantRepeating.add(sig);
            }
        });

        // Choose which signatures to use
        const targetSignatures = importantRepeating.size > 0 ? importantRepeating : repeatingSignatures;

        // Step 4: Filter links to those matching target signatures
        const selectedLinks = linksInBox
            .filter(item => targetSignatures.has(item.signature))
            .map(item => item.link);

        return selectedLinks;
    }

    // Public API
    return {
        apply: apply,
        isLinkImportant: isLinkImportant,
        getLinkSignature: getLinkSignature
    };
})();
```

## File: `js/state.js`
```javascript
//=============================================================================
// STATE MANAGEMENT
//=============================================================================

/**
 * Central state object for better organization and tracking of application state
 * @type {Object}
 */
const GrabbitState = {
    isMouseDown: false,         // Flag to track if mouse is down
    isSelectionActive: false,   // Flag to track if drag threshold has been crossed
    isDisabled: false,          // Master switch for the current page
    startX: 0,                  // Starting X position
    startY: 0,                  // Starting Y position
    lastMouseX: 0,              // Last mouse X position for tracking movement
    lastMouseY: 0,              // Last mouse Y position for tracking movement
    initialScrollY: 0,          // Initial scroll position
    currentScrollY: 0,          // Current scroll position
    selectionBox: null,         // DOM element for selection box
    counterLabel: null,         // DOM element for counter label
    selectedLinks: new Set(),   // Set of selected link elements
    currentMatchedAction: null, // Current matched action configuration
    previousAction: null,       // Previous matched action for state tracking
    currentMouseButton: null,   // Current mouse button being used
    scrollInterval: null,       // Interval ID for auto-scrolling
    savedActions: [],           // Saved actions from storage
    cachedLinks: [],            // Cache for link elements and their positions
    smartSelectActive: false,   // Flag for LinkClump-style smart select mode (only important links)
    exclusionFilters: [],       // Raw filter strings from user settings (URL filters)
    linkTextExclusionFilters: [], // Raw link text filter strings from user settings
    disabledDomains: [],        // List of domains to block
    compiledExclusionFilters: [], // Pre-compiled RegExp objects for performance (URL filters)
    compiledLinkTextExclusionFilters: [], // Pre-compiled RegExp objects for performance (link text)
    pressedKeys: new Set(),     // Set of currently pressed letter keys (for A-Z modifiers)
    linkRefreshInterval: null   // Interval ID for periodic link re-caching during selection
};

//=============================================================================
// CONSTANTS
//=============================================================================

/**
 * Application constants for better readability and maintenance
 * @type {Object}
 */
const CONSTANTS = {
    SCROLL_THRESHOLD: 20,       // Pixels from viewport edge to trigger scrolling
    SCROLL_SPEED: 35,           // Pixels per frame on scroll
    SCROLL_INTERVAL: 16,        // Milliseconds between scroll updates (~60fps)
    DEBOUNCE_DELAY: 5,          // Milliseconds for debouncing link selection
    DEFAULT_BOX_COLOR: '#2196F3', // Default selection box color
    DRAG_THRESHOLD: 5,          // Pixels to drag before activating selection
    LINK_REFRESH_INTERVAL: 500  // Milliseconds between link re-caching during selection
};
```

## File: `js/ui.js`
```javascript
//=============================================================================
// UI ELEMENT CREATION
//=============================================================================

/**
 * Creates a selection box element with the specified styles
 * @returns {HTMLElement} The created selection box element
 */
function createSelectionBox() {
    const box = document.createElement('div');
    box.style.cssText = `
    position: fixed;
    background-color: rgba(33, 150, 243, 0.1);
    z-index: 10000;
    pointer-events: none;
  `;
    return box;
}

/**
 * Creates a counter label element to display the number of selected links
 * @returns {HTMLElement} The created counter label element
 */
function createCounterLabel() {
    const label = document.createElement('div');
    label.style.cssText = `
    position: fixed;
    background-color: #333;
    color: white;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    pointer-events: none;
    z-index: 10001;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    transform: translate(10px, 10px);
  `;
    return label;
}

/**
 * Updates visual styles for selection box, highlighted links and counter label
 */
function updateVisualStyles() {
    if (!GrabbitState.currentMatchedAction) return;

    // Update selection box
    if (GrabbitState.selectionBox && GrabbitState.currentMatchedAction) {
        const borderThickness = GrabbitState.currentMatchedAction.borderThickness || 2;
        const borderStyle = GrabbitState.currentMatchedAction.borderStyle || 'solid';
        GrabbitState.selectionBox.style.border = `${borderThickness}px ${borderStyle}`;
        GrabbitState.selectionBox.style.borderColor = GrabbitState.currentMatchedAction.boxColor;
        GrabbitState.selectionBox.style.backgroundColor = `${GrabbitState.currentMatchedAction.boxColor}19`;
    }

    // Update highlighted links
    GrabbitState.selectedLinks.forEach(link => {
        link.style.backgroundColor = `${GrabbitState.currentMatchedAction.boxColor}33`;
    });

    // Update counter label
    if (GrabbitState.counterLabel) {
        const urls = Array.from(GrabbitState.selectedLinks).map(link => link.href);
        const shouldDedupe = GrabbitState.currentMatchedAction.avoidDuplicates !== 'off';
        const count = shouldDedupe ?
            new Set(urls).size :
            urls.length;

        const actionType =
            GrabbitState.currentMatchedAction.openLinks ? 'be opened in new tabs' :
                GrabbitState.currentMatchedAction.openWindow ? 'be opened in a new window' :
                    GrabbitState.currentMatchedAction.createBookmarks ? 'be saved as bookmarks' :
                        GrabbitState.currentMatchedAction.copyUrlsAndTitles ? 'be copied including page titles' :
                            GrabbitState.currentMatchedAction.copyTitles ? 'copy their page titles only' :
                                'be copied to clipboard';

        GrabbitState.counterLabel.textContent = `${count} URLs to ${actionType}`;
    }
}

/**
 * Cleans up the selection box, counter label, and selected links
 */
function cleanupSelection() {
    GrabbitState.isMouseDown = false;
    GrabbitState.isSelectionActive = false;

    if (GrabbitState.selectionBox) {
        GrabbitState.selectionBox.remove();
        GrabbitState.selectionBox = null;
    }

    if (GrabbitState.counterLabel) {
        GrabbitState.counterLabel.remove();
        GrabbitState.counterLabel = null;
    }

    GrabbitState.selectedLinks.forEach(link => link.style.backgroundColor = '');
    GrabbitState.selectedLinks.clear();
    GrabbitState.cachedLinks = []; // Clear cache
    GrabbitState.smartSelectActive = false; // Reset smart select mode

    if (GrabbitState.scrollInterval) {
        clearInterval(GrabbitState.scrollInterval);
        GrabbitState.scrollInterval = null;
    }

    if (GrabbitState.linkRefreshInterval) {
        clearInterval(GrabbitState.linkRefreshInterval);
        GrabbitState.linkRefreshInterval = null;
    }
}
```

## File: `js/utils.js`
```javascript
//=============================================================================
// UTILITIES
//=============================================================================

/**
 * Detects the user's operating system
 * @returns {string} The detected OS ('mac', 'windows', or 'linux')
 */
function getOS() {
    // Modern API (Chrome 90+, Edge 90+)
    if (navigator.userAgentData?.platform) {
        const platform = navigator.userAgentData.platform.toLowerCase();
        if (platform.includes('mac')) return 'mac';
        if (platform.includes('win')) return 'windows';
        if (platform.includes('linux')) return 'linux';
    }

    // Fallback to userAgent
    const ua = navigator.userAgent.toLowerCase();
    if (ua.includes('mac')) return 'mac';
    if (ua.includes('win')) return 'windows';
    if (ua.includes('linux')) return 'linux';

    return 'windows'; // Default to Windows
}

/**
 * Checks if a key combination matches a saved action
 * @param {Event} e - The keyboard event
 * @param {string} mouseButton - The mouse button being used
 * @returns {Object|null} The matched action or null if no match
 */
function checkKeyCombination(e, mouseButton) {
    const isMac = getOS() === 'mac';

    return GrabbitState.savedActions.find(action => {
        // First check if mouse buttons match exactly
        const mouseMatch = action.combination.mouseButton === mouseButton;
        if (!mouseMatch) return false;

        // Then check key modifier match based on OS
        let keyMatch = false;

        if (action.combination.key === 'none') {
            // No modifier key required - ensure no modifiers are pressed
            keyMatch = !e.ctrlKey && !e.shiftKey && !e.altKey && !e.metaKey && GrabbitState.pressedKeys.size === 0;
        } else if (action.combination.key === 'ctrl') {
            // Use metaKey (Command ⌘) on Mac, ctrlKey on other platforms
            keyMatch = isMac ? e.metaKey : e.ctrlKey;
        } else if (action.combination.key === 'shift' || action.combination.key === 'alt') {
            // For shift and alt, use standard properties
            keyMatch = e[`${action.combination.key}Key`];
        } else if (action.combination.key.length === 1 && /^[a-z]$/i.test(action.combination.key)) {
            // For letter keys (A-Z), check if the key is in pressedKeys
            keyMatch = GrabbitState.pressedKeys.has(action.combination.key.toLowerCase());
        }

        return keyMatch && mouseMatch;
    });
}

/**
 * Gets the mouse button name from the event
 * @param {MouseEvent} e - The mouse event
 * @returns {string|null} The mouse button name or null
 */
function getMouseButton(e) {
    switch (e.button) {
        case 0: return 'left';
        case 1: return 'middle';
        case 2: return 'right';
        default: return null;
    }
}

/**
 * Checks if an element is sticky or fixed positioned
 * @param {HTMLElement} element - The element to check
 * @returns {boolean} True if the element is sticky or fixed
 */
function isElementSticky(element) {
    let currentElement = element;
    while (currentElement && currentElement !== document.body) {
        const position = window.getComputedStyle(currentElement).position;
        if (position === 'sticky' || position === 'fixed') {
            return true;
        }
        currentElement = currentElement.parentElement;
    }
    return false;
}

/**
 * Checks if the extension should be disabled for the current domain.
 * @param {string[]} disabledDomains - List of domains to block
 * @param {string} [hostname] - Optional hostname to check (defaults to current window location)
 * @returns {boolean}
 */
function isDomainDisabled(disabledDomains, hostname) {
    if (!disabledDomains || !Array.isArray(disabledDomains)) return false;
    const targetHostname = hostname || window.location.hostname;
    return disabledDomains.some(domain => targetHostname.includes(domain));
}

/**
 * Standard debounce implementation
 */
function debounce(func, wait) {

    let timeout;
    return function (...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

/**
 * Queries all links in the document, including those inside Shadow DOM
 * @param {Document|ShadowRoot} root - The root element to start searching from
 * @returns {Array<HTMLAnchorElement>} Array of all anchor elements found
 */
function getAllLinks(root = document) {
    const links = [];

    // Get all links in the current root
    const directLinks = root.querySelectorAll('a');
    links.push(...directLinks);

    // Find all elements that might have a shadow root
    const allElements = root.querySelectorAll('*');

    allElements.forEach(element => {
        if (element.shadowRoot) {
            // Recursively query links in the shadow root
            const shadowLinks = getAllLinks(element.shadowRoot);
            links.push(...shadowLinks);
        }
    });

    return links;
}

/**
 * Determines if a link is "important" based on heuristics
 * (Headings, ARIA roles, Font weight/size, deep visual check)
 * @param {HTMLAnchorElement} link - The link element
 * @param {CSSStyleDeclaration} style - The computed style of the link
 * @returns {boolean} True if the link is considered important
 */
function isLinkImportant(link, style) {
    // 1. Semantic Headings (H1-H6) - Check Upwards
    const headingRegex = /^H[1-6]$/;
    // Check immediate parent first (fastest)
    if (link.parentElement && headingRegex.test(link.parentElement.tagName)) return true;

    // Walk up a few levels (e.g. 3) to find a heading tag
    let parentNode = link.parentNode;
    for (let i = 0; i < 3 && parentNode && parentNode !== document.body; i++) {
        if (headingRegex.test(parentNode.nodeName)) {
            return true;
        }
        parentNode = parentNode.parentNode;
    }

    // 2. ARIA Roles
    if (link.getAttribute('role') === 'heading') return true;
    if (link.closest && link.closest('[role="heading"]')) return true;

    // 3. Visual Prominence (Self)
    if (isVisuallyProminent(style)) return true;

    // 4. Deep Inspection (Children)
    // If the link itself isn't bold/large, check if it WRAPS something important
    // Check for H tags inside
    if (link.querySelector('h1, h2, h3, h4, h5, h6')) return true;

    // Check immediate children for visual importance
    // We limit depth to avoid perf hit, just check direct children and maybe one level down
    const children = Array.from(link.children);
    for (const child of children) {
        if (headingRegex.test(child.tagName)) return true; // Direct child is H tag

        const childStyle = window.getComputedStyle(child);
        if (isVisuallyProminent(childStyle)) return true;

        // One more level deep? (e.g. Link > Div > Span(Bold))
        if (child.children.length > 0) {
            const grandChildren = Array.from(child.children);
            for (const grandChild of grandChildren) {
                if (headingRegex.test(grandChild.tagName)) return true;
                const grandChildStyle = window.getComputedStyle(grandChild);
                if (isVisuallyProminent(grandChildStyle)) return true;
            }
        }
    }

    return false;
}

/**
 * Helper to check visual prominence based on style object
 */
function isVisuallyProminent(style) {
    // Check for bold (>= 600 or 'bold')
    const weight = style.fontWeight;
    if (weight === 'bold' || parseInt(weight) >= 600) {
        return true;
    }
    // Check for large font (>= 16px)
    const fontSize = parseFloat(style.fontSize);
    if (fontSize >= 16) {
        return true;
    }
    return false;
}

/**
 * Generates a signature for a link to identifying its "type" for adaptive selection.
 * @param {HTMLAnchorElement} link - The link element
 * @param {CSSStyleDeclaration} style - The computed style of the link
 * @returns {Object} The signature object
 */
function getLinkSignature(link, style) {
    // improved signature to capture "deep" structure
    let structureType = 'standard'; // standard, wrapper-heading, wrapper-bold
    let primaryTag = link.tagName;

    // Check if it's a wrapper
    if (link.querySelector('h1, h2, h3, h4, h5, h6')) {
        structureType = 'wrapper-heading';
        primaryTag = link.querySelector('h1, h2, h3, h4, h5, h6').tagName;
    } else {
        // Check parent for heading
        const headingRegex = /^H[1-6]$/;
        let parentNode = link.parentNode;
        for (let i = 0; i < 3 && parentNode && parentNode !== document.body; i++) {
            if (headingRegex.test(parentNode.nodeName)) {
                structureType = 'inside-heading';
                primaryTag = parentNode.tagName;
                break;
            }
            parentNode = parentNode.parentNode;
        }
    }

    return {
        structureType: structureType,
        primaryTag: primaryTag,
        classList: Array.from(link.classList),
        // If it's a wrapper, 'isBold' might be false on the link itself, but true on child
        // For signature matching, we care about the link's own class/style consistency mostly
        isBold: style.fontWeight === 'bold' || parseInt(style.fontWeight) >= 600,
        fontSize: parseFloat(style.fontSize) || 0
    };
}

/**
 * Checks if a candidate signature matches the reference signature
 * @param {Object} refSig - The signature of the reference link
 * @param {Object} candSig - The signature of the candidate link
 * @returns {boolean} True if they match
 */
function signaturesMatch(refSig, candSig) {
    if (!refSig || !candSig) return false;

    // 1. Structure Match (Wrapper vs Inside-Heading vs Standard)
    if (refSig.structureType !== candSig.structureType) return false;

    // 2. Visual Weight Match (only if not a wrapper, as wrappers might vary on outer style)
    if (refSig.structureType === 'standard' || refSig.structureType === 'inside-heading') {
        if (refSig.isBold !== candSig.isBold) return false;
    }

    // 3. Class Intersection
    if (refSig.classList.length > 0 && candSig.classList.length > 0) {
        const intersection = refSig.classList.filter(c => candSig.classList.includes(c));
        if (intersection.length === 0) return false;
    }

    return true;
}
```

## File: `js/visited.js`
```javascript
//=============================================================================
// GRABBIT VISITED LINKS TRACKING
//=============================================================================
// This module provides persistent "visited" marking for links opened via Grabbit.
// Since browser :visited styling depends on exact URL matching (which fails for
// redirect URLs like Google Search), this module uses chrome.storage.local to
// track opened URLs and applies a custom CSS class to visually mark them.
//=============================================================================

const GRABBIT_VISITED_STORAGE_KEY = 'grabbit_visited_urls';
const GRABBIT_VISITED_CLASS = 'grabbit-visited';

/**
 * Injects the CSS styles for visited links into the page.
 * This is called once on page load.
 */
function injectGrabbitVisitedStyles() {
    // Check if styles are already injected
    if (document.getElementById('grabbit-visited-styles')) return;

    const style = document.createElement('style');
    style.id = 'grabbit-visited-styles';
    style.textContent = `
        .${GRABBIT_VISITED_CLASS},
        .${GRABBIT_VISITED_CLASS}:link,
        .${GRABBIT_VISITED_CLASS}:visited {
            color: #551A8B !important; /* Standard visited link purple */
        }
    `;
    document.head.appendChild(style);
}

/**
 * Applies the grabbit-visited class to all anchor elements on the page
 * that match any of the stored visited URLs.
 * This is called on page load to restore visited state.
 */
function applyGrabbitVisitedStyling() {
    chrome.storage.local.get([GRABBIT_VISITED_STORAGE_KEY], (result) => {
        const visitedUrls = result[GRABBIT_VISITED_STORAGE_KEY] || [];
        if (visitedUrls.length === 0) return;

        // Create a Set for faster lookup
        const visitedSet = new Set(visitedUrls);

        // Find all anchors and mark those that match
        const allAnchors = document.querySelectorAll('a[href]');
        allAnchors.forEach(anchor => {
            if (visitedSet.has(anchor.href)) {
                anchor.classList.add(GRABBIT_VISITED_CLASS);
            }
        });
    });
}

/**
 * Marks links as visited by storing their URLs and applying the visited class.
 * @param {string[]} urls - Array of URLs to mark as visited
 * @param {HTMLAnchorElement[]} [anchorElements] - Optional array of anchor elements to mark immediately
 */
function markLinksAsGrabbitVisited(urls, anchorElements = []) {
    if (!urls || urls.length === 0) return;

    // Store URLs in chrome.storage.local
    chrome.storage.local.get([GRABBIT_VISITED_STORAGE_KEY], (result) => {
        const existingUrls = result[GRABBIT_VISITED_STORAGE_KEY] || [];

        // Merge and deduplicate URLs
        const allUrls = [...new Set([...existingUrls, ...urls])];

        // Store updated list (limit to last 10000 URLs to prevent unbounded growth)
        const urlsToStore = allUrls.slice(-10000);

        chrome.storage.local.set({ [GRABBIT_VISITED_STORAGE_KEY]: urlsToStore });
    });

    // Immediately apply class to provided anchor elements
    anchorElements.forEach(anchor => {
        if (anchor && anchor.classList) {
            anchor.classList.add(GRABBIT_VISITED_CLASS);
        }
    });

    // Also try to find and mark any other anchors on the page with matching URLs
    const urlSet = new Set(urls);
    const allAnchors = document.querySelectorAll('a[href]');
    allAnchors.forEach(anchor => {
        if (urlSet.has(anchor.href)) {
            anchor.classList.add(GRABBIT_VISITED_CLASS);
        }
    });
}

// Initialize on page load
chrome.storage.sync.get(['disabledDomains'], (result) => {
    if (result.disabledDomains && isDomainDisabled(result.disabledDomains)) {
        return;
    }

    injectGrabbitVisitedStyles();
    applyGrabbitVisitedStyling();
});
```

## File: `js/components/footer.js`
```javascript
/**
 * Footer Component for Grabbit
 * Handles the footer template and its interactions
 */

const SVGS = {
    PAYPAL: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path fill="#27346a" d="M18.998825 2.02199C17.91065 0.7817275 15.94365 0.25 13.427375 0.25H6.12425c-0.514825 0 -0.9523 0.37442 -1.0329 0.882095L2.0504975 20.417925c-0.060455 0.380275 0.23401 0.7248 0.6194775 0.7248h4.508625l1.132375 -7.182225 -0.0351 0.224925c0.0806 -0.5077 0.514825 -0.8821 1.029 -0.8821h2.1425c4.208975 0 7.50465 -1.7096 8.467325 -6.65505 0.028625 -0.14625 0.053325 -0.2886 0.074775 -0.427725 -0.121575 -0.06435 -0.121575 -0.06435 0 0 0.28665 -1.8279 -0.00195 -3.07205 -0.99065 -4.19856Z" stroke-width="0.25"></path><path fill="#27346a" d="M10.03615 5.562075c0.12025 -0.0572 0.254175 -0.08905 0.394575 -0.08905h5.7255c0.677975 0 1.31045 0.0442 1.88835 0.13715 0.16575 0.02665 0.3263 0.0572 0.482325 0.0923 0.156 0.03445 0.30745 0.07345 0.454375 0.11635 0.07345 0.02145 0.1456 0.043575 0.21645 0.066975 0.284075 0.0949 0.548625 0.2054 0.79175 0.33475 0.28665 -1.82855 -0.00195 -3.07205 -0.99065 -4.19856C17.91 0.7817275 15.94365 0.25 13.427375 0.25H6.1236c-0.514175 0 -0.95165 0.37442 -1.03225 0.882095L2.0504975 20.417275c-0.0604525 0.380925 0.2340125 0.7248 0.6188275 0.7248h4.509275l2.349225 -14.897475c0.0481 -0.3055 0.244425 -0.555775 0.508325 -0.682525Z" stroke-width="0.25"></path><path fill="#2790c3" d="M19.914675 6.6483c-0.9627 4.9448 -4.258375 6.65505 -8.467325 6.65505h-2.143175c-0.514175 0 -0.9484 0.374425 -1.02835 0.8821l-1.408625 8.93015c-0.05265 0.3328 0.204775 0.634425 0.541475 0.634425h3.80075c0.449825 0 0.8327 -0.327625 0.9029 -0.771575l0.03705 -0.193725 0.71635 -4.539825 0.04615 -0.250925c0.0702 -0.443975 0.453075 -0.771575 0.902875 -0.771575h0.5688c3.681775 0 6.564675 -1.495725 7.407125 -5.8217 0.35165 -1.80775 0.16965 -3.317125 -0.76055 -4.377325 -0.2821 -0.321125 -0.632475 -0.586325 -1.0407 -0.8028 -0.0221 0.139775 -0.04615 0.281475 -0.07475 0.427725Z" stroke-width="0.25"></path><path fill="#1f264f" d="M18.982 5.81885c-0.1469 -0.0429 -0.29835 -0.081925 -0.454375 -0.116375 -0.156 -0.03445 -0.3172 -0.065 -0.482325 -0.09165 -0.578525 -0.0936 -1.21035 -0.1378 -1.888975 -0.1378H10.431475c-0.14105 0 -0.274975 0.03185 -0.394575 0.0897 -0.26455 0.12675 -0.460225 0.376375 -0.508325 0.682525l-1.21685 7.71525 -0.035125 0.224925c0.079975 -0.507675 0.5142 -0.8821 1.028375 -0.8821h2.14315c4.208975 0 7.504625 -1.7096 8.467325 -6.65505 0.0286 -0.14625 0.05265 -0.28795 0.07475 -0.427725 -0.24375 -0.1287 -0.507675 -0.23985 -0.791725 -0.3341 -0.07085 -0.0234 -0.143 -0.04615 -0.216475 -0.0676Z" stroke-width="0.25"></path></svg>',
    REVOLUT: '<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M20.9133 6.9566C20.9133 3.1208 17.7898 0 13.9503 0H2.424v3.8605h10.9782c1.7376 0 3.177 1.3651 3.2087 3.043 0.016 0.84 -0.2994 1.633 -0.8878 2.2324 -0.5886 0.5998 -1.375 0.9303 -2.2144 0.9303H9.2322a0.2756 0.2756 0 0 0 -0.2755 0.2752v3.431c0 0.0585 0.018 0.1142 0.052 0.1612L16.2646 24h5.3114l-7.2727 -10.094c3.6625 -0.1838 6.61 -3.2612 6.61 -6.9494zM6.8943 5.9229H2.424V24h4.4704z" fill="currentColor" stroke-width="1"></path></svg>',
    GITHUB: '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="github-icon"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>'
};

class GrabbitFooter {
    constructor(containerId) {
        this.container = document.getElementById(containerId);

        this.contributors = [
            { name: '@TheTacoScott', url: 'https://github.com/TheTacoScott' },
            { name: '@oaustegard', url: 'https://github.com/oaustegard' },
            { name: '@digirat', url: 'https://github.com/digirat' },
            { name: 'Subtiltee', url: 'https://subtiltee.com/all-extensions' }
        ];

        this.supportLinks = [
            {
                name: '',
                url: 'https://paypal.me/tinycobra',
                icon: SVGS.PAYPAL,
                className: 'paypal-button'
            },
            {
                name: '',
                url: 'https://revolut.me/socratespap',
                icon: SVGS.REVOLUT,
                className: 'revolut-button'
            }
        ];

        if (this.container) {
            this.render();
            this.initLogic();
        }
    }

    renderSupportButtons() {
        return this.supportLinks.map(link => `
            <a href="${link.url}" target="_blank" class="footer-btn ${link.className}">
                ${link.icon}
                ${link.name ? `<span>${link.name}</span>` : ''}
            </a>
        `).join('');
    }

    renderContributors() {
        return this.contributors.map(contributor => `
            <a href="${contributor.url}" target="_blank" class="contributor-tag">
                ${SVGS.GITHUB}
                <span>${contributor.name}</span>
            </a>
        `).join('');
    }

    render() {
        this.container.innerHTML = `
            <footer class="footer">
                <div class="footer-content">
                    <!-- Brand Column -->
                    <div class="footer-col brand-col">
                        <div class="footer-brand">
                            <img src="/icons/icon48.png" alt="Grabbit" class="footer-logo">
                            <span class="brand-name">Grabbit</span>
                        </div>
                        <p class="brand-desc">
                            The ultimate drag-select productivity tool for Chrome. 
                            Built by <a href="https://socratisp.com" target="_blank" class="text-link">Socrates</a>.
                        </p>
                        <div class="footer-meta">
                            <span>© ${new Date().getFullYear()} Grabbit</span>
                        </div>
                    </div>

                    <!-- Community Column -->
                    <div class="footer-col community-col">
                        <h4 class="footer-heading">Community</h4>
                        <div class="contributors-wrapper">
                            ${this.renderContributors()}
                        </div>
                        <a href="https://github.com/socratespap/Grabbit" target="_blank" class="github-cta">
                            ${SVGS.GITHUB}
                            <span>Contribute on GitHub</span>
                        </a>
                    </div>

                    <!-- Support Column -->
                    <div class="footer-col support-col">
                        <h4 class="footer-heading">Support Development</h4>
                        <p class="support-text">Your support keeps this project alive and ad-free.</p>
                        <div class="support-actions">
                            ${this.renderSupportButtons()}
                        </div>
                    </div>
                </div>
            </footer>
        `;
    }

    initLogic() {
        // Rate button functionality (if rate button exists)
        const rateButton = document.getElementById('rateExtensionButton');
        if (rateButton) {
            rateButton.addEventListener('click', () => {
                chrome.webstore.postRating();
            });
        }

        // Pin button functionality (if pin button exists)
        const pinButton = document.getElementById('pinExtensionButton');
        if (pinButton) {
            pinButton.addEventListener('click', () => {
                // Open a guide on how to pin extensions
                window.open('https://support.google.com/chrome_webstore/answer/3060053', '_blank');
            });
        }
    }
}

// Auto-initialize if the script is loaded and a placeholder exists
document.addEventListener('DOMContentLoaded', () => {
    const placeholder = document.getElementById('footer-placeholder');
    if (placeholder) {
        new GrabbitFooter('footer-placeholder');
    }
});
```

## File: `js/components/sidebar.js`
```javascript
/**
 * Sidebar Component for Grabbit
 * Handles both the template and the navigation logic
 */

class GrabbitSidebar {
    constructor(containerId, activeSection = 'main-options') {
        this.container = document.getElementById(containerId);
        this.activeSection = activeSection;
        if (this.container) {
            this.render();
            this.initLogic();
        }
    }

    render() {
        this.container.innerHTML = `
            <div class="sidebar">
                <div class="sidebar-header">
                    <img src="/icons/icon48.png" alt="Grabbit Logo" class="sidebar-logo">
                    <h2>Grabbit</h2>
                </div>
                <nav class="sidebar-nav">
                    <a href="/options.html#main-options" class="sidebar-link ${this.activeSection === 'main-options' ? 'active' : ''}" data-section="main-options">
                        <svg viewBox="0 0 24 24" width="18" height="18">
                            <path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z" fill="currentColor" />
                        </svg>
                        Main Options
                    </a>
                    <a href="/popup/popupOptions/popupOptions.html" class="sidebar-link ${this.activeSection === 'popup-options' ? 'active' : ''}" data-section="popup-options">
                        <svg viewBox="0 0 24 24" width="18" height="18">
                            <path d="M19 3H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V5a2 2 0 00-2-2zm0 16H5V5h14v14z" fill="currentColor" />
                            <path d="M7 10h10v2H7z" fill="currentColor" />
                            <path d="M7 14h7v2H7z" fill="currentColor" />
                        </svg>
                        Popup Options
                    </a>
                    <a href="/advancedOptions/advancedOptions.html" class="sidebar-link ${this.activeSection === 'advanced-options' ? 'active' : ''}" data-section="advanced-options">
                        <svg viewBox="0 0 24 24" width="18" height="18">
                            <path d="M11 15h2v2h-2zm0-8h2v6h-2zm.99-5C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z" fill="currentColor" />
                        </svg>
                        Advanced Options
                    </a>
                    <a href="/proAccount/proAccount.html" class="sidebar-link ${this.activeSection === 'pro-account' ? 'active' : ''}" data-section="pro-account">
                        <svg viewBox="0 0 24 24" width="18" height="18">
                            <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" fill="currentColor" />
                        </svg>
                        Pro Account
                    </a>

                </nav>
            </div>
        `;
    }

    initLogic() {
        const sidebarLinks = this.container.querySelectorAll('.sidebar-link');

        sidebarLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                const targetSectionId = link.getAttribute('data-section');
                const targetSection = document.getElementById(targetSectionId);

                // If the target section exists on the current page, we handle internal switching
                if (targetSection) {
                    e.preventDefault();

                    // Remove active class from all links
                    sidebarLinks.forEach(l => l.classList.remove('active'));

                    // Add active class to clicked link
                    link.classList.add('active');

                    // Show target section and hide others (if we have other sections on the same page)
                    const sections = ['main-options', 'popup-options', 'advanced-options', 'pro-account'];
                    sections.forEach(sectionId => {
                        const section = document.getElementById(sectionId);
                        if (section) {
                            section.style.display = sectionId === targetSectionId ? 'block' : 'none';
                        }
                    });

                    // Update hash without jumping if it's the options page
                    if (window.location.pathname.endsWith('options.html')) {
                        history.pushState(null, null, `#${targetSectionId}`);
                    }
                }
                // Otherwise, the default link behavior (navigation to options.html) will happen
            });
        });
    }
}

// Auto-initialize if the script is loaded and a placeholder exists
document.addEventListener('DOMContentLoaded', () => {
    const placeholder = document.getElementById('sidebar-placeholder');
    if (placeholder) {
        // Determine active section from hash or data attribute
        const currentHash = window.location.hash.substring(1) || 'main-options';
        const defaultSection = placeholder.getAttribute('data-active-section') || currentHash;
        new GrabbitSidebar('sidebar-placeholder', defaultSection);
    }
});
```

## File: `js/options/card.js`
```javascript
/**
 * Action Card module for Grabbit Options
 * Handles UI generation for Action Cards
 */

import { currentOS } from './env.js';
import { saveActionsToStorage } from './storage.js';
import { updateFormatPreview } from './preview.js';

/**
 * Creates a visual card representing a user-defined action with all its functionality
 * @param {Object} action - The action configuration object
 * @param {HTMLElement} savedActionsContainer - Container for saved actions
 * @param {HTMLElement} modal - The modal element
 * @returns {HTMLElement} The created card DOM element
 */
export function createActionCard(action, savedActionsContainer, modal) {
    const card = document.createElement('div');
    card.className = 'card saved-action';
    card.style.borderLeftColor = action.boxColor || '#2196F3';

    // Create combination text for display (e.g., "CTRL + Left Mouse Click")
    let combinationText = [];
    if (action.combination.key !== 'none') {
        // Display OS-specific key name
        let keyText = action.combination.key.toUpperCase();
        if (action.combination.key === 'ctrl') {
            keyText = currentOS === 'mac' ? 'COMMAND' : 'CTRL';
        }
        combinationText.push(keyText);
    }
    if (action.combination.mouseButton !== 'none') {
        // Convert mouse button values to user-friendly text
        if (action.combination.mouseButton === 'left') combinationText.push('Left Mouse Click');
        if (action.combination.mouseButton === 'right') combinationText.push('Right Mouse Click');
        if (action.combination.mouseButton === 'middle') combinationText.push('Middle Mouse Click');
    }

    // Create features array for display
    const features = [];
    if (action.openLinks) features.push('Open Links');
    if (action.openWindow) features.push('Open in Window');
    if (action.copyUrls) features.push('Copy URLs');
    if (action.smartSelect === 'on') features.push('Smart Select');
    if (action.avoidDuplicates === 'on') features.push('Avoid Duplicates');
    if (action.copyUrlsAndTitles) {
        features.push('Copy URLs & Titles');
        // Add formatting details for Copy URLs & Titles
        if (action.formatPattern) {
            let formatText = '';
            if (action.formatPattern === 'markdown') {
                formatText = 'Markdown';
            } else if (action.formatPattern === 'json') {
                formatText = 'JSON';
            } else {
                formatText = action.formatPattern === 'titleFirst' ? 'Title&rarr;URL' : 'URL&rarr;Title';
            }
            features.push(formatText);
        }
        if (action.separatorType && action.formatPattern !== 'json' && action.formatPattern !== 'markdown') {
            let separatorText = '';
            switch (action.separatorType) {
                case 'newline':
                    separatorText = 'Newline';
                    break;
                case 'space':
                    separatorText = 'Space';
                    break;
                case 'tab':
                    separatorText = 'Tab';
                    break;
                case 'comma':
                    separatorText = 'Comma';
                    break;
                case 'dot':
                    separatorText = 'Dot';
                    break;
            }
            if (action.separatorCount > 1) {
                separatorText += ` x${action.separatorCount}`;
            }
            features.push(separatorText);
        }
        // Add link separator info if set
        if (action.linkSeparatorCount > 0) {
            features.push(`Link Gap: ${action.linkSeparatorCount}`);
        }
    }
    if (action.copyTitles) features.push('Copy Titles');
    if (action.createBookmarks) features.push('Create Bookmarks');
    if (action.markVisited) features.push('Mark Visited');
    if (action.reverseOrder) features.push('Reverse Order');
    if (action.openLinks && action.openAtEnd) features.push('Open at End');
    if ((action.openLinks || action.openWindow) && action.tabDelay > 0) features.push(`${action.tabDelay}s Delay`);

    // Add border styling info
    if (action.borderThickness && action.borderThickness !== 2) {
        features.push(`${action.borderThickness}px Border`);
    }
    if (action.borderStyle && action.borderStyle !== 'solid') {
        features.push(`${action.borderStyle.charAt(0).toUpperCase() + action.borderStyle.slice(1)} Border`);
    }

    // Create color preview
    const colorPreview = `<span class="color-preview" style="background-color: ${action.boxColor || '#2196F3'}"></span>`;

    // Create the HTML structure for the card
    card.innerHTML = `
        <div class="action-details">
            <div class="action-combination">${combinationText.join(' + ') || 'No Combination'}</div>
            <div class="action-features">
                ${colorPreview}
                ${features.map(f => `<span class="action-feature">${f}</span>`).join('')}
            </div>
        </div>
        <div class="action-buttons">
            <button class="edit-action" title="Edit Action">&#9998;</button>
            <button class="delete-action" title="Delete Action">&times;</button>
        </div>
    `;

    // Store the action data in the card for later use
    card.actionData = action;

    // Add edit functionality to the card
    const editButton = card.querySelector('.edit-action');
    editButton.addEventListener('click', () => {
        openEditModal(action, card, modal);
    });

    // Add delete functionality to the card
    const deleteButton = card.querySelector('.delete-action');
    deleteButton.addEventListener('click', () => {
        card.remove();
        // Update storage after deletion
        const remainingActions = Array.from(savedActionsContainer.children).map(c => c.actionData);
        saveActionsToStorage(remainingActions);
    });

    return card;
}

/**
 * Opens the modal in edit mode with the action's data
 * @param {Object} action - The action to edit
 * @param {HTMLElement} card - The card being edited
 * @param {HTMLElement} modal - The modal element
 */
function openEditModal(action, card, modal) {
    // Populate the modal with current action data
    document.getElementById('combinedKey').value = action.combination.key;
    document.getElementById('mouseButton').value = action.combination.mouseButton;

    // Show/hide letter key warning based on the action's key
    const letterKeyWarning = document.getElementById('letterKeyWarning');
    if (letterKeyWarning) {
        const isLetterKey = /^[a-z]$/.test(action.combination.key);
        letterKeyWarning.classList.toggle('visible', isLetterKey);
    }
    document.getElementById('actionType').value = action.openLinks ? 'openLinks' :
        (action.openWindow ? 'openWindow' :
            (action.copyUrlsAndTitles ? 'copyUrlsAndTitles' :
                (action.copyTitles ? 'copyTitles' :
                    (action.createBookmarks ? 'createBookmarks' : 'copyUrls'))));
    document.getElementById('smartSelect').checked = action.smartSelect === 'on';
    document.getElementById('avoidDuplicates').checked = action.avoidDuplicates !== 'off';
    document.getElementById('reverseOrder').checked = action.reverseOrder || false;
    document.getElementById('markVisited').checked = action.markVisited || false;
    document.getElementById('openAtEnd').checked = action.openAtEnd || false;
    document.getElementById('boxColor').value = action.boxColor || '#2196F3';
    document.getElementById('tabDelay').value = action.tabDelay || 0;
    document.getElementById('delayValue').textContent = (action.tabDelay || 0).toFixed(1) + 's';
    document.getElementById('borderThickness').value = action.borderThickness || 2;
    document.getElementById('borderStyle').value = action.borderStyle || 'solid';

    // Show/hide conditional UI elements based on action type
    const delayContainer = document.getElementById('delayOptionContainer');
    const openAtEndContainer = document.getElementById('openAtEndContainer');
    const formatOptionsContainer = document.getElementById('formatOptionsContainer');

    // Show delay option only for actions that open tabs/windows
    if (action.openLinks || action.openWindow) {
        delayContainer.style.display = 'flex';
    } else {
        delayContainer.style.display = 'none';
    }

    // Show openAtEnd option only for actions that open links
    if (action.openLinks) {
        openAtEndContainer.style.display = 'flex';
    } else {
        openAtEndContainer.style.display = 'none';
    }

    // Show format options only for copyUrlsAndTitles action
    if (action.copyUrlsAndTitles) {
        formatOptionsContainer.style.display = 'block';
        // Populate format options if they exist
        if (action.formatPattern) document.getElementById('formatPattern').value = action.formatPattern;
        if (action.separatorType) {
            const separatorTypeSelect = document.getElementById('separatorType');
            separatorTypeSelect.value = action.separatorType;
        }
        if (action.separatorCount) document.getElementById('separatorCount').value = action.separatorCount;
        if (action.linkSeparatorCount !== undefined) document.getElementById('linkSeparatorCount').value = action.linkSeparatorCount;
        // Update the preview with the loaded settings
        setTimeout(updateFormatPreview, 0);
    } else {
        formatOptionsContainer.style.display = 'none';
    }

    // Show the modal and mark it as editing
    modal.classList.add('active');
    modal.editingCard = card;

    // Set modal title for editing
    const modalTitleEl = document.getElementById('modalTitle');
    if (modalTitleEl) modalTitleEl.textContent = 'Edit Action';

    // Expand advanced options when editing (so user can see current settings)
    const collapsibleSectionEl = document.querySelector('.collapsible-section');
    if (collapsibleSectionEl) collapsibleSectionEl.classList.remove('collapsed');
}
```

## File: `js/options/env.js`
```javascript
/**
 * Environment detection module for Grabbit Options
 * Handles OS detection and extension context checking
 */

// Check if we're in a Chrome extension context to handle API calls safely
export const isExtension = typeof chrome !== 'undefined' && chrome.storage;

// Get the current OS for UI customization
// Uses shared getOS() from utils.js if available, with fallback
export const currentOS = typeof getOS !== 'undefined' ? getOS() : 'windows';
```

## File: `js/options/main.js`
```javascript
/**
 * Grabbit Options Page - Main Entry Point
 * 
 * This is the main module that initializes and orchestrates all options page functionality.
 * It imports all other modules and sets up event listeners and initialization logic.
 */

import { isExtension } from './env.js';
import { loadActionsFromStorage, saveBoxColorToStorage } from './storage.js';
import { updateKeyLabels, initializeTooltips } from './utils.js';
import { setupPreviewListeners } from './preview.js';
import { createActionCard } from './card.js';
import { initializeModal, setupModalListeners, setupFormValidation } from './modal.js';

// ============================================================================
// DOM ELEMENT REFERENCES
// ============================================================================

const actionButton = document.querySelector('.action-button');
const modal = document.getElementById('actionModal');
const closeButton = document.querySelector('.modal-close');
const cancelButton = document.getElementById('cancelButton');
const combinedKeySelect = document.getElementById('combinedKey');
const savedActionsContainer = document.getElementById('savedActions');
const boxColorInput = document.getElementById('boxColor');
const advancedOptionsToggle = document.getElementById('advancedOptionsToggle');
const collapsibleSection = advancedOptionsToggle?.closest('.collapsible-section');
const modalTitle = document.getElementById('modalTitle');

// ============================================================================
// INITIALIZATION
// ============================================================================

/**
 * Initialize the options page
 */
function initialize() {
    // Initialize the modal module with required DOM references
    initializeModal({
        modal,
        savedActionsContainer,
        collapsibleSection,
        modalTitle
    });

    // Set up modal event listeners
    setupModalListeners({
        actionButton,
        closeButton,
        cancelButton,
        advancedOptionsToggle
    });

    // Set up form validation
    setupFormValidation();

    // Set up preview listeners
    setupPreviewListeners();

    // Update key labels based on OS
    updateKeyLabels(combinedKeySelect);

    // Initialize tooltips
    initializeTooltips();

    // Set up box color change handler
    boxColorInput.addEventListener('change', (e) => {
        saveBoxColorToStorage(e.target.value);
    });

    // Set up letter key warning handler
    combinedKeySelect.addEventListener('change', (e) => {
        const letterKeyWarning = document.getElementById('letterKeyWarning');
        if (letterKeyWarning) {
            // Check if selected value is a single letter (a-z)
            const isLetterKey = /^[a-z]$/.test(e.target.value);
            letterKeyWarning.classList.toggle('visible', isLetterKey);
        }
    });

    // Set up extension management buttons
    setupExtensionButtons();

    // Load saved actions from storage
    if (isExtension) {
        loadActionsFromStorage(
            (actions) => {
                actions.forEach(action => {
                    savedActionsContainer.appendChild(createActionCard(action, savedActionsContainer, modal));
                });
            },
            boxColorInput
        );
    }
}

/**
 * Set up extension management buttons (pin, rate)
 */
function setupExtensionButtons() {
    // Handle pin extension button
    const pinExtensionButton = document.getElementById('pinExtensionButton');
    if (pinExtensionButton) {
        pinExtensionButton.addEventListener('click', async () => {
            try {
                const extensionId = chrome.runtime.id;
                await chrome.action.setPopup({ popup: 'popup/popup.html' });
                await chrome.action.enable();
                await chrome.tabs.create({
                    url: 'chrome://extensions/?id=' + extensionId
                });
            } catch (error) {
                console.error('Failed to pin extension:', error);
            }
        });
    }

    // Handle rate extension button
    const rateExtensionButton = document.getElementById('rateExtensionButton');
    if (rateExtensionButton) {
        rateExtensionButton.addEventListener('click', () => {
            const extensionId = chrome.runtime.id;
            chrome.tabs.create({
                url: `https://chrome.google.com/webstore/detail/${extensionId}/reviews`
            });
        });
    }

    // Handle report issue button
    const reportIssueButton = document.getElementById('reportIssueButton');
    if (reportIssueButton) {
        reportIssueButton.addEventListener('click', () => {
            chrome.tabs.create({
                url: 'https://chromewebstore.google.com/detail/madmdgpjgagdmmmiddpiggdnpgjglcdk/support'
            });
        });
    }
}

// ============================================================================
// START APPLICATION
// ============================================================================

// Run initialization when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize);
} else {
    // DOM is already ready
    initialize();
}
```

## File: `js/options/modal.js`
```javascript
/**
 * Modal module for Grabbit Options
 * Handles the "Add/Edit Action" modal lifecycle and form logic
 */

import { saveActionsToStorage } from './storage.js';
import { generateUniqueColor, isDuplicateCombination } from './utils.js';
import { createActionCard } from './card.js';
import { updateFormatPreview } from './preview.js';

// Module-level references to DOM elements (set during initialization)
let modal;
let savedActionsContainer;
let collapsibleSection;
let modalTitle;

/**
 * Initializes modal module with required DOM element references
 * @param {Object} elements - Object containing DOM element references
 */
export function initializeModal(elements) {
    modal = elements.modal;
    savedActionsContainer = elements.savedActionsContainer;
    collapsibleSection = elements.collapsibleSection;
    modalTitle = elements.modalTitle;
}

/**
 * Opens the modal for creating a new action
 */
export function openModal() {
    modal.classList.add('active');

    // Set modal title for creating new action
    if (modalTitle) modalTitle.textContent = 'Create New Action';

    // Collapse advanced options by default when creating new action
    if (collapsibleSection) collapsibleSection.classList.add('collapsed');

    // Set a unique color when opening the modal
    document.getElementById('boxColor').value = generateUniqueColor(savedActionsContainer);
}

/**
 * Closes the modal and resets its state
 */
export function closeModal() {
    modal.classList.remove('active');
    modal.editingCard = null;
    // Reset all form selections
    document.getElementById('combinedKey').value = 'none';
    document.getElementById('mouseButton').value = '';
    document.getElementById('actionType').value = '';
    document.getElementById('smartSelect').checked = false;
    document.getElementById('avoidDuplicates').checked = true;
    document.getElementById('reverseOrder').checked = false;
    document.getElementById('markVisited').checked = false;
    document.getElementById('openAtEnd').checked = false;
    document.getElementById('tabDelay').value = 0;
    document.getElementById('delayValue').textContent = '0.0s';
    document.getElementById('borderThickness').value = 2;
    document.getElementById('borderStyle').value = 'solid';
    // Reset all error messages
    document.querySelectorAll('.error-message').forEach(error => error.classList.remove('visible'));
    // Reset warning messages
    document.querySelectorAll('.warning-message').forEach(warning => warning.classList.remove('visible'));
    // Hide conditional UI elements by default
    document.getElementById('delayOptionContainer').style.display = 'none';
    document.getElementById('openAtEndContainer').style.display = 'none';
}

/**
 * Handles the save button click - validates and saves the action
 */
export function handleSaveAction() {
    const mouseButton = document.getElementById('mouseButton');
    const mouseButtonError = document.getElementById('mouseButtonError');
    const actionType = document.getElementById('actionType');
    const actionTypeError = document.getElementById('actionTypeError');
    const combinationError = document.getElementById('combinationError');

    // Reset error messages
    mouseButtonError.classList.remove('visible');
    actionTypeError.classList.remove('visible');
    if (combinationError) combinationError.classList.remove('visible');

    // Validate mouse button selection
    if (!mouseButton.value) {
        mouseButtonError.classList.add('visible');
        mouseButton.focus();
        return;
    }

    // Validate action type selection
    if (!actionType.value) {
        actionTypeError.classList.add('visible');
        actionType.focus();
        return;
    }

    // Create combination object to check for duplicates
    const newCombination = {
        key: document.getElementById('combinedKey').value,
        mouseButton: mouseButton.value
    };

    // Check for duplicate combinations
    if (isDuplicateCombination(newCombination, savedActionsContainer, modal.editingCard)) {
        // If combinationError doesn't exist, create it
        if (!combinationError) {
            const errorDiv = document.createElement('div');
            errorDiv.id = 'combinationError';
            errorDiv.className = 'error-message';
            errorDiv.textContent = 'This key and mouse combination is already in use!';
            mouseButton.parentNode.appendChild(errorDiv);
        } else {
            combinationError.classList.add('visible');
        }
        return;
    }

    // Create action object with form data
    const action = {
        combination: newCombination,
        openLinks: actionType.value === 'openLinks',
        openWindow: actionType.value === 'openWindow',
        copyUrls: actionType.value === 'copyUrls',
        copyUrlsAndTitles: actionType.value === 'copyUrlsAndTitles',
        copyTitles: actionType.value === 'copyTitles',
        createBookmarks: actionType.value === 'createBookmarks',
        smartSelect: document.getElementById('smartSelect').checked ? 'on' : 'off',
        avoidDuplicates: document.getElementById('avoidDuplicates').checked ? 'on' : 'off',
        reverseOrder: document.getElementById('reverseOrder').checked,
        markVisited: document.getElementById('markVisited').checked,
        openAtEnd: document.getElementById('openAtEnd').checked,
        boxColor: document.getElementById('boxColor').value,
        tabDelay: parseFloat(document.getElementById('tabDelay').value),
        borderThickness: parseInt(document.getElementById('borderThickness').value) || 2,
        borderStyle: document.getElementById('borderStyle').value || 'solid'
    };

    // Add formatting options if copyUrlsAndTitles is selected
    if (action.copyUrlsAndTitles) {
        action.formatPattern = document.getElementById('formatPattern')?.value || 'titleFirst';
        action.separatorType = document.getElementById('separatorType')?.value || 'newline';
        action.separatorCount = parseInt(document.getElementById('separatorCount')?.value || '1', 10);
        action.linkSeparatorCount = parseInt(document.getElementById('linkSeparatorCount')?.value || '0', 10);
    }

    // Handle editing vs creating new action
    if (modal.editingCard) {
        const updatedCard = createActionCard(action, savedActionsContainer, modal);
        modal.editingCard.replaceWith(updatedCard);
        modal.editingCard = null;
    } else {
        savedActionsContainer.appendChild(createActionCard(action, savedActionsContainer, modal));
    }

    // Save all actions to storage
    const allActions = Array.from(savedActionsContainer.children).map(card => card.actionData);
    saveActionsToStorage(allActions);

    closeModal();
}

/**
 * Sets up all modal-related event listeners
 * @param {Object} elements - Object containing button references
 */
export function setupModalListeners(elements) {
    const { actionButton, closeButton, cancelButton, advancedOptionsToggle } = elements;

    // Open modal button
    actionButton.addEventListener('click', openModal);

    // Close buttons
    closeButton.addEventListener('click', closeModal);
    cancelButton.addEventListener('click', closeModal);

    // Close modal when clicking outside
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Advanced options toggle
    if (advancedOptionsToggle && collapsibleSection) {
        advancedOptionsToggle.addEventListener('click', () => {
            collapsibleSection.classList.toggle('collapsed');
        });
    }

    // Save button
    document.getElementById('saveButton').addEventListener('click', handleSaveAction);

    // Tab delay slider
    const tabDelaySlider = document.getElementById('tabDelay');
    const delayValueDisplay = document.getElementById('delayValue');
    tabDelaySlider.addEventListener('input', (e) => {
        const value = parseFloat(e.target.value);
        delayValueDisplay.textContent = value.toFixed(1) + 's';
    });
}

/**
 * Sets up form validation and action type change handlers
 */
export function setupFormValidation() {
    // Mouse button validation
    document.getElementById('mouseButton').addEventListener('change', (e) => {
        const mouseButtonError = document.getElementById('mouseButtonError');
        if (!e.target.value) {
            mouseButtonError.classList.add('visible');
        } else {
            mouseButtonError.classList.remove('visible');
        }
    });

    // Action type validation and conditional UI
    document.getElementById('actionType').addEventListener('change', (e) => {
        const actionTypeError = document.getElementById('actionTypeError');
        if (!e.target.value) {
            actionTypeError.classList.add('visible');
        } else {
            actionTypeError.classList.remove('visible');
        }

        // Show/hide conditional UI elements based on action type
        const delayContainer = document.getElementById('delayOptionContainer');
        const openAtEndContainer = document.getElementById('openAtEndContainer');
        const formatOptionsContainer = document.getElementById('formatOptionsContainer');

        if (e.target.value === 'openLinks' || e.target.value === 'openWindow') {
            delayContainer.style.display = 'flex';
        } else {
            delayContainer.style.display = 'none';
        }

        if (e.target.value === 'openLinks') {
            openAtEndContainer.style.display = 'flex';
        } else {
            openAtEndContainer.style.display = 'none';
        }

        if (e.target.value === 'copyUrlsAndTitles') {
            formatOptionsContainer.style.display = 'block';
            // Update the preview with the loaded settings
            updateFormatOptionVisibility();
            setTimeout(updateFormatPreview, 0);
        } else {
            formatOptionsContainer.style.display = 'none';
        }
    });

    // Format pattern change handler
    document.getElementById('formatPattern')?.addEventListener('change', () => {
        updateFormatOptionVisibility();
        updateFormatPreview();
    });
}

/**
 * Updates the visibility of format options based on selected pattern
 */
function updateFormatOptionVisibility() {
    const formatPattern = document.getElementById('formatPattern')?.value;
    const separatorCountContainer = document.getElementById('separatorCount')?.closest('.input-group');
    const linkSeparatorCountContainer = document.getElementById('linkSeparatorCount')?.closest('.input-group');
    const separatorTypeContainer = document.getElementById('separatorType')?.closest('.input-group');

    if (!separatorCountContainer || !linkSeparatorCountContainer || !separatorTypeContainer) return;

    // Reset all to visible first
    separatorCountContainer.style.display = 'flex';
    linkSeparatorCountContainer.style.display = 'flex';
    separatorTypeContainer.style.display = 'flex';

    if (formatPattern === 'markdown') {
        // Markdown: hide separator count (uses standard markdown format)
        separatorCountContainer.style.display = 'none';
        separatorTypeContainer.style.display = 'none'; // Also hide separator type for Markdown as it's fixed
    } else if (formatPattern === 'json') {
        // JSON: hide all separator options
        separatorCountContainer.style.display = 'none';
        linkSeparatorCountContainer.style.display = 'none';
        separatorTypeContainer.style.display = 'none';
    }
}
```

## File: `js/options/popup-config.js`
```javascript
/**
 * Popup Configuration Module
 * Manages which buttons appear in the popup and their order
 */

// Button registry with metadata
export const POPUP_BUTTONS = {
    copyUrls: {
        id: 'copyUrls',
        title: 'Copy Selected Tabs',
        subtitle: 'Selected tabs only',
        color: 'blue',
        icon: 'copy',
        isPremium: false
    },
    copyAllUrls: {
        id: 'copyAllUrls',
        title: 'Copy All Tabs',
        subtitle: 'All open tabs in window',
        color: 'purple',
        icon: 'clipboard',
        isPremium: false
    },
    openUrls: {
        id: 'openUrls',
        title: 'Open Copied Links',
        subtitle: 'From clipboard',
        color: 'orange',
        icon: 'external',
        isPremium: false
    },
    compareProducts: {
        id: 'compareProducts',
        title: 'Compare Products by AI',
        subtitle: 'Premium Analysis',
        color: 'premium',
        icon: 'layers',
        isPremium: true
    },
    summarizePage: {
        id: 'summarizePage',
        title: 'Summarize Page',
        subtitle: 'AI Article Summary',
        color: 'premium',
        icon: 'document',
        isPremium: true
    },
    youtubeSummary: {
        id: 'youtubeSummary',
        title: 'YouTube Summary',
        subtitle: 'Summarize Video by AI',
        color: 'premium',
        icon: 'youtube',
        isPremium: true
    }
};

// Default configuration
const DEFAULT_CONFIG = {
    buttons: [
        { id: 'copyUrls', enabled: true, order: 0 },
        { id: 'copyAllUrls', enabled: true, order: 1 },
        { id: 'openUrls', enabled: true, order: 2 },
        { id: 'compareProducts', enabled: true, order: 3 },
        { id: 'summarizePage', enabled: true, order: 4 },
        { id: 'youtubeSummary', enabled: true, order: 5 }
    ]
};

/**
 * Load popup configuration from storage
 * @returns {Promise<Object>} Popup configuration
 */
export async function loadPopupConfig() {
    return new Promise((resolve) => {
        chrome.storage.sync.get(['popupConfig'], (result) => {
            if (!result.popupConfig || !validateConfig(result.popupConfig)) {
                // Set defaults if invalid or missing
                const defaults = JSON.parse(JSON.stringify(DEFAULT_CONFIG));
                chrome.storage.sync.set({ popupConfig: defaults }, () => {
                    resolve(defaults);
                });
            } else {
                resolve(result.popupConfig);
            }
        });
    });
}

/**
 * Save popup configuration to storage
 * @param {Object} config - Popup configuration to save
 * @returns {Promise<void>}
 */
export async function savePopupConfig(config) {
    return new Promise((resolve) => {
        chrome.storage.sync.set({ popupConfig: config }, () => {
            resolve();
        });
    });
}

/**
 * Validate popup configuration structure
 * @param {Object} config - Config to validate
 * @returns {boolean} True if valid
 */
function validateConfig(config) {
    if (!config || !config.buttons || !Array.isArray(config.buttons)) {
        return false;
    }

    // Check that all IDs exist in registry
    const validIds = Object.keys(POPUP_BUTTONS);
    const configIds = config.buttons.map(b => b.id);

    // Filter out any unknown IDs (for future compatibility)
    const filteredIds = configIds.filter(id => validIds.includes(id));

    // At least one button must exist
    return filteredIds.length > 0;
}

/**
 * Reset popup configuration to defaults
 * @returns {Promise<Object>} Default configuration
 */
export async function resetPopupConfig() {
    const defaults = JSON.parse(JSON.stringify(DEFAULT_CONFIG));
    await savePopupConfig(defaults);
    return defaults;
}

/**
 * Get icon SVG HTML for a button
 * @param {string} iconName - Name of the icon
 * @returns {string} SVG HTML
 */
export function getButtonIcon(iconName) {
    const icons = {
        copy: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
        </svg>`,
        clipboard: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
            <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
        </svg>`,
        external: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
            <polyline points="15 3 21 3 21 9"></polyline>
            <line x1="10" y1="14" x2="21" y2="3"></line>
        </svg>`,
        layers: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
            <path d="M2 17l10 5 10-5"></path>
            <path d="M2 12l10 5 10-5"></path>
        </svg>`,
        document: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
            <polyline points="10 9 9 9 8 9"></polyline>
        </svg>`,
        youtube: `<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
            <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814z"/>
            <polygon fill="white" points="9.545,15.568 15.818,12 9.545,8.432"/>
        </svg>`
    };

    return icons[iconName] || icons.copy;
}

/**
 * Initialize the popup customization UI
 */
export async function initializePopupConfig() {
    const container = document.getElementById('popupButtonList');
    if (!container) return;

    const config = await loadPopupConfig();

    // Sort buttons by order
    const sortedButtons = config.buttons
        .filter(b => POPUP_BUTTONS[b.id])
        .sort((a, b) => a.order - b.order);

    // Clear container
    container.innerHTML = '';

    // Render each button
    sortedButtons.forEach((buttonConfig, index) => {
        const buttonMeta = POPUP_BUTTONS[buttonConfig.id];
        const item = createButtonListItem(buttonConfig, buttonMeta, index);
        container.appendChild(item);
    });

    // Setup drag and drop
    setupDragAndDrop(container);

    // Setup toggle switches
    setupToggleSwitches(container, config);

    // Setup reset button
    const resetBtn = document.getElementById('resetPopupConfig');
    if (resetBtn) {
        resetBtn.addEventListener('click', async () => {
            if (confirm('Reset to default button configuration?')) {
                const defaults = await resetPopupConfig();
                await initializePopupConfig();
            }
        });
    }
}

/**
 * Create a button list item
 */
function createButtonListItem(buttonConfig, buttonMeta, index) {
    const item = document.createElement('div');
    item.className = 'popup-button-item';
    item.dataset.id = buttonConfig.id;
    item.dataset.index = index;
    item.draggable = true;

    item.innerHTML = `
        <div class="drag-handle">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="9" cy="5" r="1"></circle>
                <circle cx="9" cy="12" r="1"></circle>
                <circle cx="9" cy="19" r="1"></circle>
                <circle cx="15" cy="5" r="1"></circle>
                <circle cx="15" cy="12" r="1"></circle>
                <circle cx="15" cy="19" r="1"></circle>
            </svg>
        </div>
        <div class="button-preview">
            <div class="button-icon-preview ${buttonMeta.color}">
                ${getButtonIcon(buttonMeta.icon)}
            </div>
            <div class="button-info">
                <div class="button-info-title">
                    ${buttonMeta.title}
                    ${buttonMeta.isPremium ? '<span class="pro-badge-mini">PRO</span>' : ''}
                </div>
                <div class="button-info-subtitle">${buttonMeta.subtitle}</div>
            </div>
        </div>
        <div class="button-toggle">
            <label class="toggle-switch">
                <input type="checkbox" class="toggle-checkbox" ${buttonConfig.enabled ? 'checked' : ''}>
                <span class="toggle-slider"></span>
            </label>
        </div>
    `;

    if (!buttonConfig.enabled) {
        item.classList.add('disabled');
    }

    return item;
}

/**
 * Setup drag and drop functionality
 */
function setupDragAndDrop(container) {
    let draggedItem = null;

    container.addEventListener('dragstart', (e) => {
        const item = e.target.closest('.popup-button-item');
        if (!item) return;

        draggedItem = item;
        item.classList.add('dragging');
        e.dataTransfer.effectAllowed = 'move';
    });

    container.addEventListener('dragend', (e) => {
        const item = e.target.closest('.popup-button-item');
        if (!item) return;

        item.classList.remove('dragging');
        document.querySelectorAll('.popup-button-item').forEach(i => {
            i.classList.remove('drag-over');
        });

        // Save new order
        saveNewOrder();
    });

    container.addEventListener('dragover', (e) => {
        e.preventDefault();
        const item = e.target.closest('.popup-button-item');
        if (!item || item === draggedItem) return;

        item.classList.add('drag-over');
    });

    container.addEventListener('dragleave', (e) => {
        const item = e.target.closest('.popup-button-item');
        if (!item) return;

        item.classList.remove('drag-over');
    });

    container.addEventListener('drop', (e) => {
        e.preventDefault();
        const item = e.target.closest('.popup-button-item');
        if (!item || item === draggedItem) return;

        const items = [...container.querySelectorAll('.popup-button-item')];
        const draggedIndex = items.indexOf(draggedItem);
        const targetIndex = items.indexOf(item);

        if (draggedIndex < targetIndex) {
            item.parentNode.insertBefore(draggedItem, item.nextSibling);
        } else {
            item.parentNode.insertBefore(draggedItem, item);
        }

        item.classList.remove('drag-over');
    });
}

/**
 * Save new button order after drag
 */
async function saveNewOrder() {
    const container = document.getElementById('popupButtonList');
    const items = container.querySelectorAll('.popup-button-item');

    const config = await loadPopupConfig();
    const buttonMap = new Map(config.buttons.map(b => [b.id, b]));

    items.forEach((item, index) => {
        const id = item.dataset.id;
        if (buttonMap.has(id)) {
            buttonMap.get(id).order = index;
        }
    });

    config.buttons = Array.from(buttonMap.values());
    await savePopupConfig(config);
}

/**
 * Setup toggle switches
 */
function setupToggleSwitches(container, config) {
    const toggles = container.querySelectorAll('.toggle-checkbox');

    toggles.forEach(toggle => {
        toggle.addEventListener('change', async (e) => {
            const item = e.target.closest('.popup-button-item');
            const id = item.dataset.id;
            const enabled = e.target.checked;

            // Count enabled buttons
            const allToggles = container.querySelectorAll('.toggle-checkbox');
            const enabledCount = [...allToggles].filter(t => t.checked).length;

            // Prevent disabling last button
            if (!enabled && enabledCount === 0) {
                e.target.checked = true;
                alert('At least one button must remain enabled!');
                return;
            }

            // Update config
            const buttonConfig = config.buttons.find(b => b.id === id);
            if (buttonConfig) {
                buttonConfig.enabled = enabled;
                await savePopupConfig(config);

                // Update visual state
                if (enabled) {
                    item.classList.remove('disabled');
                } else {
                    item.classList.add('disabled');
                }
            }
        });
    });
}

```

## File: `js/options/preview.js`
```javascript
/**
 * Format Preview module for Grabbit Options
 * Handles the live preview for "Copy URLs & Titles" formatting
 */

/**
 * Updates the format preview to show how URLs with titles will look
 * based on the current format options settings
 */
export function updateFormatPreview() {
    const formatPreview = document.getElementById('formatPreview');
    if (!formatPreview) return;

    // Get current format settings
    const formatPattern = document.getElementById('formatPattern')?.value || 'titleFirst';
    const separatorType = document.getElementById('separatorType')?.value || 'newline';
    const separatorCount = parseInt(document.getElementById('separatorCount')?.value || '1', 10);
    const linkSeparatorCount = parseInt(document.getElementById('linkSeparatorCount')?.value || '0', 10);

    // Sample data for preview
    const sampleLinks = [
        { title: 'Google Homepage', url: 'https://google.com' },
        { title: 'GitHub', url: 'https://github.com' }
    ];

    // Determine the separator string
    let separator = '';
    switch (separatorType) {
        case 'newline':
            separator = '\n'.repeat(separatorCount);
            break;
        case 'space':
            separator = ' '.repeat(separatorCount);
            break;
        case 'tab':
            separator = '\t'.repeat(separatorCount);
            break;
        case 'comma':
            separator = ','.repeat(separatorCount);
            break;
        case 'dot':
            separator = '.'.repeat(separatorCount);
            break;
    }

    // Build the preview output
    const formattedLinks = sampleLinks.map(link => {
        if (formatPattern === 'markdown') {
            return `[${link.title}](${link.url})`;
        } else if (formatPattern === 'json') {
            return JSON.stringify({ title: link.title, url: link.url });
        } else if (formatPattern === 'titleFirst') {
            return `<span class="preview-title">${link.title}</span>${separator}<span class="preview-url">${link.url}</span>`;
        } else {
            return `<span class="preview-url">${link.url}</span>${separator}<span class="preview-title">${link.title}</span>`;
        }
    });

    // Special handling for JSON to show valid array
    if (formatPattern === 'json') {
        const jsonObjects = sampleLinks.map(link => ({ title: link.title, url: link.url }));
        formatPreview.textContent = JSON.stringify(jsonObjects);
        return;
    }

    // Join links with the link separator (extra blank lines between links)
    const linkSeparator = '\n'.repeat(linkSeparatorCount + 1);
    const output = formattedLinks.join(linkSeparator);

    // Display in preview with proper formatting
    // Convert tabs and newlines to visible representation for display
    formatPreview.innerHTML = output
        .replace(/\t/g, '<span class="preview-separator">→</span>')
        .replace(/\n/g, '<br>');
}

/**
 * Sets up event listeners for format options to update preview in real-time
 */
export function setupPreviewListeners() {
    document.getElementById('formatPattern')?.addEventListener('change', updateFormatPreview);
    document.getElementById('separatorType')?.addEventListener('change', updateFormatPreview);
    document.getElementById('separatorCount')?.addEventListener('input', updateFormatPreview);
    document.getElementById('linkSeparatorCount')?.addEventListener('input', updateFormatPreview);
}
```

## File: `js/options/storage.js`
```javascript
/**
 * Storage module for Grabbit Options
 * Manages Chrome storage interactions for actions and settings
 */

import { isExtension } from './env.js';

/**
 * Saves user-defined actions to Chrome storage
 * @param {Array} actions - Array of action objects to save
 */
export function saveActionsToStorage(actions) {
    if (!isExtension) return;
    chrome.storage.sync.set({ savedActions: actions }, function () {
        console.log('Actions saved:', actions);
    });
}

/**
 * Saves the selection box color preference to Chrome storage
 * @param {string} color - Hex color code
 */
export function saveBoxColorToStorage(color) {
    if (!isExtension) return;
    chrome.storage.sync.set({ boxColor: color }, function () {
        console.log('Box color saved:', color);
    });
}

/**
 * Loads saved actions and preferences from Chrome storage
 * @param {Function} onActionsLoaded - Callback to handle loaded actions
 * @param {HTMLElement} boxColorInput - The color input element to update
 */
export function loadActionsFromStorage(onActionsLoaded, boxColorInput) {
    if (!isExtension) return;
    chrome.storage.sync.get(['savedActions', 'boxColor'], function (result) {
        // Load saved actions
        if (result.savedActions && onActionsLoaded) {
            onActionsLoaded(result.savedActions);
        }
        // Load saved box color
        if (result.boxColor && boxColorInput) {
            boxColorInput.value = result.boxColor;
        }
    });
}
```

## File: `js/options/utils.js`
```javascript
/**
 * Utility functions for Grabbit Options
 * Contains helper functions for colors, tooltips, and key labels
 */

import { currentOS } from './env.js';

/**
 * Generates a unique color for a new action from a predefined set of colors
 * Avoids using colors that are already in use by other actions
 * @param {HTMLElement} savedActionsContainer - Container with existing action cards
 * @returns {string} A hex color code
 */
export function generateUniqueColor(savedActionsContainer) {
    // Define our 6 specific colors
    const colors = [
        '#FF0000', // red
        '#0000FF', // blue
        '#008000', // green
        '#FFD700', // yellow
        '#00FFFF', // aqua
        '#FFA500'  // orange
    ];

    // Get all existing action colors
    const existingColors = Array.from(savedActionsContainer.children)
        .map(card => card.actionData?.boxColor)
        .filter(Boolean);

    // Filter out colors that are already in use
    const availableColors = colors.filter(color =>
        !existingColors.includes(color)
    );

    // If all colors are used, return the first color from the original list
    if (availableColors.length === 0) {
        return colors[0];
    }

    // Return a random color from available colors
    const randomIndex = Math.floor(Math.random() * availableColors.length);
    return availableColors[randomIndex];
}

/**
 * Updates key labels in the UI based on the user's operating system
 * (e.g., showing Command ⌘ instead of Ctrl on macOS)
 * @param {HTMLElement} combinedKeySelect - The modifier key dropdown element
 */
export function updateKeyLabels(combinedKeySelect) {
    if (!combinedKeySelect) return;

    // Update the combinedKey dropdown options based on OS
    const ctrlOption = combinedKeySelect.querySelector('option[value="ctrl"]');
    if (ctrlOption) {
        ctrlOption.textContent = currentOS === 'mac' ? 'Command ⌘' : 'Ctrl';
    }

    // Update the Alt option to show as Option for macOS
    const altOption = combinedKeySelect.querySelector('option[value="alt"]');
    if (altOption) {
        altOption.textContent = currentOS === 'mac' ? 'Option ⌥' : 'Alt';
    }

    // Update the Shift option to include symbol for macOS
    const shiftOption = combinedKeySelect.querySelector('option[value="shift"]');
    if (shiftOption) {
        shiftOption.textContent = currentOS === 'mac' ? 'Shift ⇧' : 'Shift';
    }
}

/**
 * Initializes dynamic positioning for fixed tooltips
 * Required because fixed positioning needs viewport coordinates
 */
export function initializeTooltips() {
    const tooltipTriggers = document.querySelectorAll('.smart-select-info');

    tooltipTriggers.forEach(trigger => {
        const tooltip = trigger.querySelector('.tooltip');
        if (!tooltip) return;

        trigger.addEventListener('mouseenter', () => {
            const rect = trigger.getBoundingClientRect();
            // Position tooltip above the trigger, centered horizontally
            tooltip.style.left = rect.left + (rect.width / 2) + 'px';
            tooltip.style.top = (rect.top - 8) + 'px';
            tooltip.style.transform = 'translate(-50%, -100%)';
        });
    });
}

/**
 * Checks if a key+mouse combination already exists in saved actions
 * @param {Object} newCombination - The combination to check
 * @param {HTMLElement} savedActionsContainer - Container with existing action cards
 * @param {HTMLElement} editingCard - The card being edited (to exclude from check)
 * @returns {boolean} True if the combination is a duplicate
 */
export function isDuplicateCombination(newCombination, savedActionsContainer, editingCard = null) {
    // Get all existing actions
    const existingActions = Array.from(savedActionsContainer.children);

    // Check each action for matching combination
    return existingActions.some(card => {
        // Skip the card being edited
        if (editingCard === card) return false;

        const action = card.actionData;
        return action.combination.key === newCombination.key &&
            action.combination.mouseButton === newCombination.mouseButton;
    });
}
```

## File: `popup/popup.css`
```css
/* ============================================
   Grabbit Popup - Modern Glassmorphism Design
   ============================================ */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: var(--font-stack);
}

html {
    background-color: #0f0f23;
}

body {
    width: 320px;
    min-height: 280px;
    background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 50%, #0d0d1f 100%);
    overflow: hidden;
    position: relative;
}

/* Background Orbs - Decorative animated elements */
.bg-orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(60px);
    opacity: 0.5;
    pointer-events: none;
    will-change: transform;
}

.orb-1 {
    width: 120px;
    height: 120px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    top: -20px;
    right: -20px;
    animation-delay: 0s;
}

.orb-2 {
    width: 100px;
    height: 100px;
    background: linear-gradient(135deg, #f093fb, #f5576c);
    bottom: 50px;
    left: -30px;
    animation-delay: -3s;
}

.orb-3 {
    width: 80px;
    height: 80px;
    background: linear-gradient(135deg, #4facfe, #00f2fe);
    bottom: -10px;
    right: 30px;
    animation-delay: -5s;
}

@keyframes float {

    0%,
    100% {
        transform: translate(0, 0) scale(1);
    }

    33% {
        transform: translate(8px, -12px) scale(1.02);
    }

    66% {
        transform: translate(-4px, 8px) scale(0.98);
    }
}

/* Main Container */
.popup-container {
    position: relative;
    z-index: 1;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 16px;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Header Section */
.popup-header {
    display: flex;
    align-items: center;
    gap: 14px;
    padding-bottom: 8px;
}

.logo-wrapper {
    position: relative;
    width: 42px;
    height: 42px;
}

.logo {
    width: 42px;
    height: 42px;
    background: url('../icons/icon48.png');
    background-size: cover;
    border-radius: 12px;
    position: relative;
    z-index: 2;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.logo-glow {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50px;
    height: 50px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 16px;
    filter: blur(15px);
    opacity: 0.6;
    animation: pulse 3s ease-in-out infinite;
}

@keyframes pulse {

    0%,
    100% {
        opacity: 0.6;
        transform: translate(-50%, -50%) scale(1);
    }

    50% {
        opacity: 0.8;
        transform: translate(-50%, -50%) scale(1.1);
    }
}

.header-text {
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.title {
    font-size: 22px;
    font-weight: 700;
    background: linear-gradient(135deg, #ffffff 0%, #a8b4ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.5px;
}

.tagline {
    font-size: 11px;
    color: rgba(255, 255, 255, 0.5);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-weight: 500;
}

/* Actions Section */
.actions-section {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

/* Action Buttons - Glassmorphism Style */
.action-button {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 16px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 14px;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.action-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, transparent 0%, rgba(255, 255, 255, 0.05) 100%);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.action-button:hover {
    transform: translateY(-2px);
    border-color: rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.action-button:hover::before {
    opacity: 1;
}

.action-button:active {
    transform: translateY(0);
}

/* Button Icon Styles */
.button-icon {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.action-button:hover .button-icon {
    transform: scale(1.05);
}

/* Color Variants */
.action-button.blue .button-icon {
    background: var(--button-primary-bg);
    box-shadow: 0 4px 15px rgba(33, 150, 243, 0.4);
    color: white;
}

.action-button.purple .button-icon {
    background: var(--button-purple-bg);
    box-shadow: 0 4px 15px rgba(156, 39, 176, 0.4);
    color: white;
}

.action-button.orange .button-icon {
    background: var(--button-orange-bg);
    box-shadow: 0 4px 15px rgba(255, 152, 0, 0.4);
    color: white;
}

/* Button Content */
.button-content {
    display: flex;
    flex-direction: column;
    gap: 2px;
    flex: 1;
    text-align: left;
}

.button-title {
    font-size: 14px;
    font-weight: 600;
    color: #ffffff;
    letter-spacing: -0.2px;
}

.button-subtitle {
    font-size: 11px;
    color: rgba(255, 255, 255, 0.5);
    font-weight: 400;
}

/* Button Arrow */
.button-arrow {
    color: rgba(255, 255, 255, 0.3);
    transition: all 0.3s ease;
}

.action-button:hover .button-arrow {
    color: rgba(255, 255, 255, 0.7);
    transform: translateX(3px);
}

/* Success State */
.action-button.success .button-icon {
    background: var(--button-success-bg) !important;
    box-shadow: 0 4px 15px rgba(76, 175, 80, 0.4) !important;
}

.action-button.success .button-title {
    color: var(--success-color);
}

/* Footer Section */
.popup-footer {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    padding-top: 8px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.footer-link {
    display: flex;
    align-items: center;
    gap: 6px;
    color: rgba(255, 255, 255, 0.5);
    text-decoration: none;
    font-size: 12px;
    font-weight: 500;
    padding: 6px 10px;
    border-radius: 8px;
    transition: all 0.2s ease;
}

.footer-link:hover {
    color: #ffffff;
    background: rgba(255, 255, 255, 0.1);
}

.footer-link svg {
    opacity: 0.7;
    transition: opacity 0.2s ease;
}

.footer-link:hover svg {
    opacity: 1;
}

.footer-divider {
    width: 1px;
    height: 16px;
    background: rgba(255, 255, 255, 0.15);
}

.version-badge {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 10px;
    font-weight: 600;
    color: rgba(255, 255, 255, 0.4);
    background: rgba(255, 255, 255, 0.08);
    padding: 4px 8px;
    border-radius: 6px;
    letter-spacing: 0.5px;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.2s ease;
    position: relative;
}

.version-badge:hover {
    color: rgba(255, 255, 255, 0.8);
    background: rgba(255, 255, 255, 0.15);
}

.version-badge.has-update {
    color: #4CAF50;
    background: rgba(76, 175, 80, 0.15);
    border: 1px solid rgba(76, 175, 80, 0.3);
    animation: gentleGlow 2s ease-in-out infinite;
}

.version-badge.has-update:hover {
    background: rgba(76, 175, 80, 0.25);
}

@keyframes gentleGlow {
    0%, 100% {
        box-shadow: 0 0 5px rgba(76, 175, 80, 0.3);
    }
    50% {
        box-shadow: 0 0 12px rgba(76, 175, 80, 0.5);
    }
}

.update-dot {
    width: 6px;
    height: 6px;
    background: #4CAF50;
    border-radius: 50%;
    animation: pulse-dot 1.5s ease-in-out infinite;
}

@keyframes pulse-dot {
    0%, 100% {
        opacity: 1;
        transform: scale(1);
    }
    50% {
        opacity: 0.7;
        transform: scale(1.2);
    }
}

/* Scrollbar Styling */
::-webkit-scrollbar {
    width: 6px;
}

::-webkit-scrollbar-track {
    background: transparent;
}

::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.3);
}

/* Disabled State Overlay */
.disabled-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(15, 15, 35, 0.85);
    backdrop-filter: blur(8px);
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
}

.disabled-content {
    text-align: center;
    padding: 20px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
}

.disabled-icon {
    font-size: 32px;
    margin-bottom: 12px;
}

.disabled-content h3 {
    font-size: 18px;
    font-weight: 600;
    color: white;
    margin-bottom: 6px;
}

.disabled-content p {
    font-size: 12px;
    color: rgba(255, 255, 255, 0.6);
    margin-bottom: 16px;
}

.action-button.small {
    padding: 8px 16px;
    width: 100%;
    justify-content: center;
    font-size: 13px;
    font-weight: 600;
    color: #fff;
    background: rgba(255, 255, 255, 0.1);
}

.action-button.small:hover {
    background: rgba(255, 255, 255, 0.2);
}

/* Premium Action Button */
.action-button.premium {
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.15), rgba(99, 102, 241, 0.15));
    border: 1px solid rgba(168, 85, 247, 0.3);
}

.action-button.premium .button-icon {
    background: linear-gradient(135deg, #a855f7, #6366f1);
    box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4);
}

.action-button.premium:hover {
    border-color: rgba(168, 85, 247, 0.5);
    box-shadow: 0 8px 32px rgba(168, 85, 247, 0.2);
}

.pro-badge {
    position: absolute;
    top: 8px;
    right: 8px;
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    color: #000;
    font-size: 9px;
    font-weight: 800;
    padding: 2px 6px;
    border-radius: 4px;
    letter-spacing: 0.5px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

body.modal-open {
    width: 600px;
    height: 500px;
    transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
```

## File: `popup/popup.html`
```html
<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="../css/variables.css">
    <link rel="stylesheet" href="popup.css">
    <link rel="stylesheet" href="compare-modal.css">
</head>

<body>
    <div class="popup-container">
        <!-- Disabled State Overlay -->
        <div id="disabled-state" class="disabled-overlay" style="display: none;">
            <div class="disabled-content">
                <div class="disabled-icon">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ef5350" stroke-width="1.5"
                        stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="4.93" y1="4.93" x2="19.07" y2="19.07"></line>
                    </svg>
                </div>
                <h3>Grabbit is Disabled</h3>
                <p>This domain is in your blocklist.</p>
                <button id="enable-site-btn" class="action-button small">Enable for this site</button>
            </div>
        </div>

        <!-- Decorative background elements -->
        <div class="bg-orb orb-1"></div>
        <div class="bg-orb orb-2"></div>
        <div class="bg-orb orb-3"></div>

        <!-- Header Section -->
        <div class="popup-header">
            <div class="logo-wrapper">
                <div class="logo"></div>
                <div class="logo-glow"></div>
            </div>
            <div class="header-text">
                <h1 class="title">Grabbit</h1>
                <span class="tagline">Link Manager</span>
            </div>
        </div>

        <!-- Actions Section -->
        <div class="actions-section" id="actionsSection">
            <!-- Buttons will be dynamically rendered via JS -->
        </div>

        <!-- Footer Section -->
        <div class="popup-footer">
            <a href="/options.html" class="footer-link" target="_blank">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="3"></circle>
                    <path
                        d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z">
                    </path>
                </svg>
                <span>Settings</span>
            </a>
            <div class="footer-divider"></div>
            <a href="/popup/popupOptions/popupOptions.html" class="footer-link customize-popup-link" target="_blank">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="3"></circle>
                    <path d="M12 1L9 6l5-5 5 5-3-5M12 23l-3-5 5-5 5 5-3-5" />
                </svg>
                <span>Customize</span>
            </a>
            <div class="footer-divider"></div>
            <a id="version-link" class="version-badge" title="View changelog">
                <span class="version-text"></span>
                <span class="update-dot" style="display: none;"></span>
            </a>
        </div>
    </div>
    <script src="popup.js"></script>

    <!-- AI Comparison Modal Structure -->
    <div id="compare-modal" class="compare-modal" style="display: none;">
        <div class="compare-overlay"></div>
        <div class="compare-content">
            <div class="compare-header">
                <div class="compare-title">
                    <div class="ai-icon-container">
                        <svg class="ai-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 2L2 7l10 5 10-5-10-5z" />
                            <path d="M2 17l10 5 10-5" />
                            <path d="M2 12l10 5 10-5" />
                        </svg>
                        <div class="ai-glow"></div>
                    </div>
                    <h2>AI Comparison Dashboard</h2>
                </div>
                <button id="close-compare" class="compare-close" aria-label="Close">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                </button>
            </div>

            <div class="compare-body">
                <div id="compare-loading" class="compare-state">
                    <div class="loading-animation">
                        <div class="pulse-ring"></div>
                        <div class="ai-loader-icon">
                            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="1.5">
                                <path d="M12 2L2 7l10 5 10-5-10-5z" />
                                <path d="M2 17l10 5 10-5" />
                                <path d="M2 12l10 5 10-5" />
                            </svg>
                        </div>
                    </div>
                    <h3>Analyzing Products...</h3>
                    <p>Scanning features, prices, and reviews...</p>
                    <div class="loading-steps">
                        <div class="step active" id="step-extract">Extracting web data...</div>
                        <div class="step" id="step-analyze">Analyzing with AI...</div>
                        <div class="step" id="step-render">Building dashboard...</div>
                    </div>
                </div>

                <div id="compare-error" class="compare-state" style="display: none;">
                    <div class="error-icon">
                        <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="1.5">
                            <circle cx="12" cy="12" r="10"></circle>
                            <line x1="12" y1="8" x2="12" y2="12"></line>
                            <line x1="12" y1="16" x2="12.01" y2="16"></line>
                        </svg>
                    </div>
                    <h3>Analysis Failed</h3>
                    <p id="error-text">We couldn't reach the AI server. Please check your internet connection or API
                        key.</p>
                    <button class="retry-btn">Try Again</button>
                </div>

                <div id="compare-results" class="compare-state" style="display: none;">
                    <div class="results-grid">
                        <div class="results-main">
                            <div class="verdict-card">
                                <div class="verdict-header">
                                    <span class="badge purple">🏆 Top Choice</span>
                                    <h3 id="winner-name">Product Name</h3>
                                </div>
                                <p id="winner-reason">Connecting the dots...</p>
                                <div class="verdict-stats">
                                    <div class="stat">
                                        <span class="stat-label">AI Score</span>
                                        <span class="stat-value" id="winner-score">9.5</span>
                                    </div>
                                    <div class="stat">
                                        <span class="stat-label">Price</span>
                                        <span class="stat-value" id="winner-price">$ --</span>
                                    </div>
                                </div>
                            </div>

                            <div class="details-section">
                                <h4>Comparison Table</h4>
                                <div class="table-frame">
                                    <table id="comparison-table">
                                        <thead>
                                            <tr id="table-head">
                                                <th>Feature</th>
                                            </tr>
                                        </thead>
                                        <tbody id="table-body"></tbody>
                                    </table>
                                </div>
                            </div>
                        </div>

                        <div class="results-sidebar">
                            <h4>Product Breakdown</h4>
                            <div id="product-list" class="product-list"></div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="compare-footer">
                <p></p>
                <div class="footer-actions">
                    <button id="copy-summary" class="footer-btn">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2">
                            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                        </svg>
                        Copy Results
                    </button>
                </div>
            </div>
        </div>
    </div>
</body>

</html>
```

## File: `popup/popup.js`
```javascript
/**
 * Grabbit Popup Script
 * Handles button interactions and AI Comparison Dashboard
 */

// Button registry (mirrors popup-config.js)
const POPUP_BUTTONS = {
    copyUrls: {
        id: 'copyUrls',
        title: 'Copy Selected Tabs',
        subtitle: 'Selected tabs only',
        color: 'blue',
        icon: 'copy',
        isPremium: false
    },
    copyAllUrls: {
        id: 'copyAllUrls',
        title: 'Copy All Tabs',
        subtitle: 'All open tabs in window',
        color: 'purple',
        icon: 'clipboard',
        isPremium: false
    },
    openUrls: {
        id: 'openUrls',
        title: 'Open Copied Links',
        subtitle: 'From clipboard',
        color: 'orange',
        icon: 'external',
        isPremium: false
    },
    compareProducts: {
        id: 'compareProducts',
        title: 'Compare Products by AI',
        subtitle: 'Premium Analysis',
        color: 'premium',
        icon: 'layers',
        isPremium: true
    },
    summarizePage: {
        id: 'summarizePage',
        title: 'Summarize Page',
        subtitle: 'AI Article Summary',
        color: 'premium',
        icon: 'document',
        isPremium: true
    },
    youtubeSummary: {
        id: 'youtubeSummary',
        title: 'YouTube Summary',
        subtitle: 'Summarize Video by AI',
        color: 'premium',
        icon: 'youtube',
        isPremium: true
    }
};

// Get icon SVG HTML
function getButtonIcon(iconName) {
    const icons = {
        copy: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
        </svg>`,
        clipboard: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
            <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
        </svg>`,
        external: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
            <polyline points="15 3 21 3 21 9"></polyline>
            <line x1="10" y1="14" x2="21" y2="3"></line>
        </svg>`,
        layers: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
            <path d="M2 17l10 5 10-5"></path>
            <path d="M2 12l10 5 10-5"></path>
        </svg>`,
        document: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
            <polyline points="10 9 9 9 8 9"></polyline>
        </svg>`,
        youtube: `<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
            <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814z"/>
            <polygon fill="white" points="9.545,15.568 15.818,12 9.545,8.432"/>
        </svg>`
    };
    return icons[iconName] || icons.copy;
}

// Load popup configuration
async function loadPopupConfig() {
    return new Promise((resolve) => {
        chrome.storage.sync.get(['popupConfig'], (result) => {
            resolve(result.popupConfig || {
                buttons: [
                    { id: 'copyUrls', enabled: true, order: 0 },
                    { id: 'copyAllUrls', enabled: true, order: 1 },
                    { id: 'openUrls', enabled: true, order: 2 },
                    { id: 'compareProducts', enabled: true, order: 3 },
                    { id: 'summarizePage', enabled: true, order: 4 },
                    { id: 'youtubeSummary', enabled: true, order: 5 }
                ]
            });
        });
    });
}

// Render buttons dynamically
function renderButtons(config, buttonElements) {
    const actionsSection = document.getElementById('actionsSection');
    if (!actionsSection) return;

    // Clear existing content
    actionsSection.innerHTML = '';

    // Filter enabled buttons and sort by order
    const sortedButtons = config.buttons
        .filter(b => b.enabled && POPUP_BUTTONS[b.id])
        .sort((a, b) => a.order - b.order);

    // Create and append each button
    sortedButtons.forEach(buttonConfig => {
        const buttonMeta = POPUP_BUTTONS[buttonConfig.id];
        const button = createActionButton(buttonMeta, buttonConfig.id);
        actionsSection.appendChild(button);

        // Store reference for event listeners
        buttonElements[buttonConfig.id] = button;
    });
}

// Create a single action button
function createActionButton(buttonMeta, buttonId) {
    const button = document.createElement('div');
    button.className = `action-button ${buttonMeta.color}`;
    button.id = buttonId;

    button.innerHTML = `
        <div class="button-icon">
            ${getButtonIcon(buttonMeta.icon)}
        </div>
        <div class="button-content">
            <div class="button-title">${buttonMeta.title}</div>
            <div class="button-subtitle">${buttonMeta.subtitle}</div>
        </div>
        ${buttonMeta.isPremium ? '<span class="pro-badge">PRO</span>' : ''}
    `;

    return button;
}

document.addEventListener('DOMContentLoaded', async () => {
    // Button elements map (will be populated after rendering)
    const buttonElements = {};

    // Modal UI Elements
    const compareModal = document.getElementById('compare-modal');
    const closeCompare = document.getElementById('close-compare');
    const resultsContainer = document.getElementById('compare-results');
    const loadingContainer = document.getElementById('compare-loading');
    const errorContainer = document.getElementById('compare-error');
    const copySummaryBtn = document.getElementById('copy-summary');

    /**
     * Helper: Show Success State on Buttons
     */
    function showSuccess(button, message, originalTitle, originalSubtitle) {
        const titleEl = button.querySelector('.button-title');
        const subtitleEl = button.querySelector('.button-subtitle');
        if (!titleEl || !subtitleEl) return;

        button.classList.add('success');
        titleEl.textContent = message;
        subtitleEl.textContent = 'Success!';

        setTimeout(() => {
            button.classList.remove('success');
            titleEl.textContent = originalTitle;
            subtitleEl.textContent = originalSubtitle;
        }, 2000);
    }

    /**
     * Helper: Show Modal State
     */
    function showModalState(state) {
        loadingContainer.style.display = state === 'loading' ? 'flex' : 'none';
        resultsContainer.style.display = state === 'results' ? 'flex' : 'none';
        errorContainer.style.display = state === 'error' ? 'flex' : 'none';

        if (state === 'results' || state === 'loading' || state === 'error') {
            compareModal.style.display = 'flex';
            document.body.classList.add('modal-open');
        } else {
            compareModal.style.display = 'none';
            document.body.classList.remove('modal-open');
        }
    }

    /**
     * Helper: Update Loading Steps
     */
    function updateLoadingStep(stepId) {
        document.querySelectorAll('.loading-steps .step').forEach(s => s.classList.remove('active'));
        const activeStep = document.getElementById(stepId);
        if (activeStep) activeStep.classList.add('active');
    }

    /**
     * Attach event listeners to buttons
     * This function is called AFTER buttons are rendered
     */
    function attachButtonListeners() {
        // --- STANDARD BUTTON HANDLERS ---

        // Copy Selected Tabs
        if (buttonElements.copyUrls) {
            buttonElements.copyUrls.addEventListener('click', async () => {
                const tabs = await chrome.tabs.query({ currentWindow: true, highlighted: true });
                const urls = tabs.map(tab => tab.url).join('\n');
                await navigator.clipboard.writeText(urls);
                showSuccess(buttonElements.copyUrls, `${tabs.length} URLs Copied!`, 'Copy Selected Tabs', 'Selected tabs only');
            });
        }

        // Copy All Tabs
        if (buttonElements.copyAllUrls) {
            buttonElements.copyAllUrls.addEventListener('click', async () => {
                const tabs = await chrome.tabs.query({ currentWindow: true });
                const urls = tabs.map(tab => tab.url).join('\n');
                await navigator.clipboard.writeText(urls);
                showSuccess(buttonElements.copyAllUrls, `${tabs.length} URLs Copied!`, 'Copy All Tabs', 'All open tabs in window');
            });
        }

        // Open Copied Links
        if (buttonElements.openUrls) {
            buttonElements.openUrls.addEventListener('click', async () => {
                try {
                    const clipboardText = await navigator.clipboard.readText();
                    const urls = clipboardText.split('\n')
                        .filter(url => url.trim().toLowerCase().match(/^https?:\/\/|^www\./))
                        .map(url => url.toLowerCase().startsWith('www.') ? 'https://' + url : url);

                    urls.forEach(url => chrome.tabs.create({ url }));
                    showSuccess(buttonElements.openUrls, `${urls.length} Links Opened!`, 'Open Copied Links', 'From clipboard');
                } catch (error) {
                    console.error(error);
                }
            });
        }

        // --- PREMIUM AI COMPARISON HANDLERS ---

        if (buttonElements.compareProducts) {
            buttonElements.compareProducts.addEventListener('click', async () => {
                // 1. Check Tabs
                const tabs = await chrome.tabs.query({ currentWindow: true, highlighted: true });

                if (tabs.length < 2) {
                    alert('Please select at least 2 product tabs (Ctrl+Click on tabs) to compare.');
                    return;
                }

                if (tabs.length > 5) {
                    alert('AI comparison is limited to 5 products at a time for better accuracy.');
                    return;
                }

                // 2. Store the tabs data for the comparison page
                await chrome.storage.local.set({
                    pendingComparison: {
                        tabs: tabs.map(t => ({ id: t.id, url: t.url, title: t.title })),
                        timestamp: Date.now()
                    }
                });

                // 3. Open the comparison page in a new tab
                chrome.tabs.create({
                    url: chrome.runtime.getURL('AI Features/compare/compare.html')
                });

                // Close popup
                window.close();
            });
        }

        // --- PREMIUM AI SUMMARIZATION HANDLERS ---

        if (buttonElements.summarizePage) {
            buttonElements.summarizePage.addEventListener('click', async () => {
                // 1. Get current active tab
                const tabs = await chrome.tabs.query({ active: true, currentWindow: true });

                if (!tabs[0]) {
                    alert('Could not access the current tab. Please try again.');
                    return;
                }

                // 2. Store the tab data for the summary page
                await chrome.storage.local.set({
                    pendingSummary: {
                        tab: { id: tabs[0].id, url: tabs[0].url, title: tabs[0].title },
                        timestamp: Date.now()
                    }
                });

                // 3. Open the summary page in a new tab
                chrome.tabs.create({
                    url: chrome.runtime.getURL('AI Features/summarize/summarize.html')
                });

                // Close popup
                window.close();
            });
        }

        // --- PREMIUM YOUTUBE SUMMARY HANDLERS ---

        if (buttonElements.youtubeSummary) {
            buttonElements.youtubeSummary.addEventListener('click', async () => {
                // 1. Get current active tab
                const tabs = await chrome.tabs.query({ active: true, currentWindow: true });

                if (!tabs[0]) {
                    alert('Could not access the current tab. Please try again.');
                    return;
                }

                // 2. Validate it's a YouTube video page
                const url = tabs[0].url || '';
                if (!url.includes('youtube.com/watch')) {
                    alert('This feature only works on YouTube video pages. Please navigate to a YouTube video first.');
                    return;
                }

                // 3. Store the tab data for the YouTube summary page
                await chrome.storage.local.set({
                    pendingYoutubeSummary: {
                        tab: { id: tabs[0].id, url: tabs[0].url, title: tabs[0].title },
                        timestamp: Date.now()
                    }
                });

                // 4. Open the YouTube summary page in a new tab
                chrome.tabs.create({
                    url: chrome.runtime.getURL('AI Features/youtube-summary/youtube-summary.html')
                });

                // Close popup
                window.close();
            });
        }
    }


    function renderResults(data) {
        // Winner Section
        document.getElementById('winner-name').textContent = data.products[data.winner].name;
        document.getElementById('winner-reason').textContent = data.winnerReason;
        document.getElementById('winner-score').textContent = data.products[data.winner].score;
        document.getElementById('winner-price').textContent = data.products[data.winner].price || 'N/A';

        // Table Header
        const tableHead = document.getElementById('table-head');
        tableHead.innerHTML = '<th>Feature</th>';
        data.products.forEach(p => {
            const th = document.createElement('th');
            th.textContent = p.name;
            tableHead.appendChild(th);
        });

        // Table Body
        const tableBody = document.getElementById('table-body');
        tableBody.innerHTML = '';
        data.features.forEach(feature => {
            const tr = document.createElement('tr');
            tr.innerHTML = `<td><strong>${feature.label}</strong></td>`;
            feature.values.forEach(val => {
                const td = document.createElement('td');
                td.textContent = val;
                tr.appendChild(td);
            });
            tableBody.appendChild(tr);
        });

        // Product Cards
        const productList = document.getElementById('product-list');
        productList.innerHTML = '';
        data.products.forEach((p, i) => {
            const card = document.createElement('div');
            card.className = `product-mini-card ${i === data.winner ? 'winner' : ''}`;
            card.innerHTML = `
                <div class="mini-card-title">${p.name}</div>
                <div class="mini-card-price">${p.price || '--'}</div>
                <div style="font-size: 0.75rem; color: #9ca3af; margin-top: 4px;">Score: ${p.score}/10</div>
            `;
            productList.appendChild(card);
        });

        // Store data for copying
        copySummaryBtn.onclick = () => {
            const summaryText = `AI Product Comparison Results:\n\nWinner: ${data.products[data.winner].name}\nReason: ${data.winnerReason}\n\nOverall Summary: ${data.summary}`;
            navigator.clipboard.writeText(summaryText);
            copySummaryBtn.textContent = 'Copied!';
            setTimeout(() => copySummaryBtn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> Copy Results', 2000);
        };
    }

    closeCompare.addEventListener('click', () => showModalState('none'));

    // --- OTHER UI LOGIC ---

    // Display version and handle update notification
    const versionBadge = document.querySelector('.version-badge');
    if (versionBadge) {
        const manifest = chrome.runtime.getManifest();
        const vText = versionBadge.querySelector('.version-text');
        if (vText) vText.textContent = `v${manifest.version}`;

        chrome.storage.local.get(['updateAvailable'], (result) => {
            if (result.updateAvailable) {
                versionBadge.classList.add('has-update');
                const updateDot = document.querySelector('.update-dot');
                if (updateDot) updateDot.style.display = 'inline-block';
            }
        });

        versionBadge.addEventListener('click', (e) => {
            e.preventDefault();
            chrome.storage.local.set({ updateAvailable: false });
            chrome.tabs.create({ url: 'https://github.com/socratespap/Grabbit/blob/main/changelog.md' });
        });
    }

    // Check for disabled domain
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        if (!tabs[0]?.url) return;
        try {
            const hostname = new URL(tabs[0].url).hostname;
            chrome.storage.sync.get(['disabledDomains'], (result) => {
                const disabled = (result.disabledDomains || []).some(d => hostname.includes(d));
                if (disabled) {
                    const overlay = document.getElementById('disabled-state');
                    if (overlay) overlay.style.display = 'flex';
                    document.querySelector('.actions-section').style.opacity = '0.3';
                    document.querySelector('.actions-section').style.pointerEvents = 'none';

                    document.getElementById('enable-site-btn')?.addEventListener('click', () => {
                        const next = result.disabledDomains.filter(d => !hostname.includes(d));
                        chrome.storage.sync.set({ disabledDomains: next }, () => {
                            chrome.tabs.reload(tabs[0].id);
                            window.close();
                        });
                    });
                }
            });
        } catch (e) { }
    });

    // --- INITIALIZE BUTTONS FROM CONFIGURATION ---
    // Load configuration and render buttons
    const config = await loadPopupConfig();
    renderButtons(config, buttonElements);

    // Attach event listeners to the rendered buttons
    attachButtonListeners();
});
```

## File: `popup/popupOptions/popupOptions.html`
```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grabbit - Popup Options</title>
    <link rel="stylesheet" href="/css/variables.css">
    <link rel="stylesheet" href="/css/components/sidebar.css">
    <link rel="stylesheet" href="/css/options.css">
    <link rel="stylesheet" href="popupOptions.css">
</head>

<body>
    <div id="sidebar-placeholder" data-active-section="popup-options"></div>

    <div class="container">
        <div id="popup-options">
            <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 2rem;">
                <img src="/icons/icon128.png" alt="Grabbit Logo" style="width: 64px; height: 64px;">
                <h1 style="margin: 0;">Popup Options</h1>
            </div>

            <div class="card popup-config-card">
                <div class="popup-config-header">
                    <h2>Popup Button Customization</h2>
                    <button id="resetPopupConfig" class="reset-button">Reset to Default</button>
                </div>
                <p class="config-description">Configure which buttons appear in the popup and their order</p>

                <div id="popupButtonList" class="popup-button-list">
                    <!-- Buttons will be rendered here via JS -->
                </div>

                <p class="config-warning">⚠️ At least one button must remain enabled</p>
            </div>

            <footer class="footer">
                <p style="color: #999; font-size: 0.85rem;">These features are experimental and may change in future
                    updates.</p>
            </footer>
        </div>
    </div>

    <script src="/js/components/sidebar.js"></script>
    <script type="module" src="popupOptions.js"></script>
</body>

</html>
```

## File: `popup/popupOptions/popupOptions.js`
```javascript
/**
 * Grabbit Popup Options Page
 * Handles popup button customization
 */

import { initializePopupConfig } from '/js/options/popup-config.js';

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializePopupConfig);
} else {
    // DOM is already ready
    initializePopupConfig();
}
```

## File: `proAccount/proAccount.css`
```css
/* Pro Account Page Styles */

/* Account Status Card */
.account-status-card h2 {
    color: var(--primary-color);
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
}

.account-status-card h2 svg {
    fill: var(--primary-color);
}

/* Status Section */
.status-section {
    padding: 1.5rem;
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    border-radius: 12px;
    border: 1px solid rgba(0, 0, 0, 0.06);
}

/* Loading State */
#loading-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    color: #666;
}

.loading-spinner {
    width: 40px;
    height: 40px;
    border: 3px solid #e0e0e0;
    border-top-color: var(--primary-color);
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}

/* Status Display */
.status-row {
    display: flex;
    align-items: center;
    padding: 0.75rem 0;
    border-bottom: 1px solid rgba(0, 0, 0, 0.06);
}

.status-row:last-child {
    border-bottom: none;
}

.status-label {
    font-weight: 500;
    color: #555;
    min-width: 160px;
}

.status-value {
    color: #333;
    font-weight: 500;
}

/* Status Badges */
.status-badge {
    display: inline-flex;
    align-items: center;
    padding: 0.35rem 0.85rem;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.badge-free {
    background: linear-gradient(135deg, #e0e0e0 0%, #bdbdbd 100%);
    color: #424242;
}

.badge-pro {
    background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
    color: white;
    box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
}

.badge-trial {
    background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
    color: white;
    box-shadow: 0 2px 8px rgba(255, 152, 0, 0.3);
}

/* Credits Section */
.credits-section {
    margin-top: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(0, 0, 0, 0.08);
}

.credits-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.credits-title {
    font-weight: 600;
    color: #333;
    font-size: 1rem;
}

.credits-reset {
    font-size: 0.8rem;
    color: #888;
    background: #f0f0f0;
    padding: 0.25rem 0.75rem;
    border-radius: 12px;
}

/* Credits Single Display */
.credits-single-display {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border-radius: 12px;
    border: 1px solid rgba(0, 0, 0, 0.06);
    padding: 1.5rem;
    text-align: center;
}

.credits-main-value {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    margin-bottom: 0.5rem;
}

.credits-main-value .credit-icon {
    font-size: 2rem;
    margin-bottom: 0;
}

.credits-main-value .credit-value {
    font-size: 2.5rem;
    font-weight: 700;
}

.credits-description {
    color: #666;
    font-size: 0.9rem;
    margin: 0;
}

.credits-value.low {
    color: #ff9800;
}

.credits-value.empty {
    color: #f44336;
}

/* Error State */
#error-state {
    text-align: center;
    color: #d32f2f;
}

.error-icon {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

#error-state p {
    margin-bottom: 1rem;
}

/* Actions Card */
.actions-card h2 {
    color: var(--primary-color);
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
}

.actions-card h2 svg {
    fill: var(--primary-color);
}

.actions-container {
    padding: 1rem 0;
}

.actions-description {
    color: #666;
    margin-bottom: 1.5rem;
    font-size: 1rem;
}

.pro-description {
    color: #2E7D32;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* Action Buttons */
.action-buttons-row {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.85rem 1.5rem;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
}

.btn svg {
    flex-shrink: 0;
}

.btn-primary {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
    box-shadow: 0 4px 12px rgba(33, 150, 243, 0.3);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(33, 150, 243, 0.4);
}

.btn-secondary {
    background: #f5f5f5;
    color: #333;
    border: 1px solid #ddd;
}

.btn-secondary:hover {
    background: #e8e8e8;
    border-color: #ccc;
}

.btn-premium {
    background: linear-gradient(135deg, #FFD700 0%, #FFA000 100%);
    color: #333;
    box-shadow: 0 4px 12px rgba(255, 215, 0, 0.4);
    font-weight: 600;
}

.btn-premium:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(255, 215, 0, 0.5);
}

.btn-premium svg {
    fill: #333;
}

.btn-full {
    width: 100%;
}

/* Features Card */
.features-card h2 {
    color: var(--primary-color);
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
}

.features-card h2 svg {
    fill: var(--primary-color);
}

.features-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.features-list li {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 1rem;
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    border-radius: 10px;
    margin-bottom: 0.75rem;
    border: 1px solid rgba(0, 0, 0, 0.04);
    transition: all 0.3s ease;
}

.features-list li:hover {
    transform: translateX(5px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.features-list li:last-child {
    margin-bottom: 0;
}

.feature-icon {
    font-size: 1.5rem;
    flex-shrink: 0;
}

.feature-text {
    color: #555;
    line-height: 1.5;
}

.feature-text strong {
    color: #333;
}

/* Footer */
.footer {
    text-align: center;
    padding-top: 2rem;
}

/* Responsive */
@media (max-width: 600px) {
    .action-buttons-row {
        flex-direction: column;
    }

    .btn {
        width: 100%;
    }

    .status-row {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.5rem;
    }

    .status-label {
        min-width: auto;
    }

    .credits-grid {
        grid-template-columns: 1fr;
        gap: 0.75rem;
    }

    .credit-item {
        flex-direction: row;
        justify-content: space-between;
        padding: 0.75rem 1rem;
    }

    .credit-icon {
        margin-bottom: 0;
        margin-right: 0.75rem;
    }

    .credit-label {
        flex: 1;
        margin-bottom: 0;
    }

    .credits-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.5rem;
    }
}
```

## File: `proAccount/proAccount.html`
```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Grabbit - Pro Account</title>
    <link rel="stylesheet" href="/css/variables.css">
    <link rel="stylesheet" href="/css/components/sidebar.css">
    <link rel="stylesheet" href="/css/options.css">
    <link rel="stylesheet" href="proAccount.css">
</head>

<body>
    <div id="sidebar-placeholder" data-active-section="pro-account"></div>

    <div class="container">
        <div id="pro-account">
            <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 2rem;">
                <img src="/icons/icon128.png" alt="Grabbit Logo" style="width: 64px; height: 64px;">
                <h1 style="margin: 0;">Pro Account</h1>
            </div>

            <!-- Account Status Card -->
            <div class="card account-status-card">
                <h2>
                    <svg viewBox="0 0 24 24" width="24" height="24"
                        style="vertical-align: middle; margin-right: 0.5rem;">
                        <path
                            d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"
                            fill="currentColor" />
                    </svg>
                    Account Status
                </h2>

                <!-- Loading State -->
                <div id="loading-state" class="status-section">
                    <div class="loading-spinner"></div>
                    <p>Loading account information...</p>
                </div>

                <!-- Status Display (hidden by default) -->
                <div id="status-display" class="status-section" style="display: none;">
                    <div class="status-row">
                        <span class="status-label">Status:</span>
                        <span id="subscription-badge" class="status-badge badge-free">FREE</span>
                    </div>
                    <div class="status-row" id="email-row" style="display: none;">
                        <span class="status-label">Email:</span>
                        <span id="user-email" class="status-value">-</span>
                    </div>
                    <div class="status-row" id="subscribed-since-row" style="display: none;">
                        <span class="status-label">Subscribed since:</span>
                        <span id="subscribed-since" class="status-value">-</span>
                    </div>
                    <div class="status-row" id="next-billing-row" style="display: none;">
                        <span class="status-label">Next billing date:</span>
                        <span id="next-billing" class="status-value">-</span>
                    </div>

                    <!-- Credits Section -->
                    <div id="credits-section" class="credits-section" style="display: none;">
                        <div class="credits-header">
                            <span class="credits-title">Monthly AI Credits</span>
                            <span id="credits-reset" class="credits-reset">Resets in - days</span>
                        </div>
                        <div class="credits-single-display">
                            <div class="credits-main-value">
                                <span class="credit-icon">⚡</span>
                                <span id="credits-total" class="credit-value">-</span>
                            </div>
                            <p class="credits-description">Shared credits for all AI features (Compare, Summarize,
                                YouTube)</p>
                        </div>
                    </div>
                </div>

                <!-- Error State -->
                <div id="error-state" class="status-section" style="display: none;">
                    <div class="error-icon">⚠️</div>
                    <p id="error-message">Unable to load account information. Please try again.</p>
                    <button id="retry-btn" class="btn btn-secondary">Retry</button>
                </div>
            </div>

            <!-- Actions Card -->
            <div class="card actions-card">
                <h2>
                    <svg viewBox="0 0 24 24" width="24" height="24"
                        style="vertical-align: middle; margin-right: 0.5rem;">
                        <path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z" fill="currentColor" />
                    </svg>
                    Actions
                </h2>

                <!-- Actions for non-subscribed users -->
                <div id="free-actions" class="actions-container">
                    <p class="actions-description">Unlock premium AI features with a Pro subscription!</p>
                    <div class="action-buttons-row">
                        <button id="login-btn" class="btn btn-secondary">
                            <svg viewBox="0 0 24 24" width="18" height="18">
                                <path
                                    d="M11 7L9.6 8.4l2.6 2.6H2v2h10.2l-2.6 2.6L11 17l5-5-5-5zm9 12h-8v2h8c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2h-8v2h8v14z"
                                    fill="currentColor" />
                            </svg>
                            Log In
                        </button>
                        <button id="subscribe-btn" class="btn btn-primary btn-premium">
                            <svg viewBox="0 0 24 24" width="18" height="18">
                                <path
                                    d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"
                                    fill="currentColor" />
                            </svg>
                            Subscribe to Pro
                        </button>
                    </div>
                </div>

                <!-- Actions for subscribed users -->
                <div id="pro-actions" class="actions-container" style="display: none;">
                    <p class="actions-description pro-description">
                        <svg viewBox="0 0 24 24" width="20" height="20" style="vertical-align: middle;">
                            <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z" fill="#4CAF50" />
                        </svg>
                        You're enjoying Grabbit Pro!
                    </p>
                    <button id="logout-btn" class="btn btn-secondary btn-full"
                        style="margin-top: 0.75rem; background: transparent; border: 1px solid #ddd; color: #666;">
                        <svg viewBox="0 0 24 24" width="18" height="18">
                            <path
                                d="M17 7l-1.41 1.41L18.17 11H8v2h10.17l-2.58 2.58L17 17l5-5zM4 5h8V3H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h8v-2H4V5z"
                                fill="currentColor" />
                        </svg>
                        Log Out
                    </button>
                    <div style="text-align: center; margin-top: 1rem;">
                        <a href="#" id="cancel-subscription-link"
                            style="color: #999; font-size: 0.8rem; text-decoration: underline;">Cancel Subscription</a>
                    </div>
                </div>
            </div>

            <!-- Features Card -->
            <div class="card features-card">
                <h2>
                    <svg viewBox="0 0 24 24" width="24" height="24"
                        style="vertical-align: middle; margin-right: 0.5rem;">
                        <path
                            d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"
                            fill="currentColor" />
                    </svg>
                    Pro Features
                </h2>
                <ul class="features-list">
                    <li>
                        <span class="feature-icon">🔄</span>
                        <span class="feature-text"><strong>AI Product Comparison</strong> - Compare products with
                            AI-powered analysis</span>
                    </li>
                    <li>
                        <span class="feature-icon">📝</span>
                        <span class="feature-text"><strong>Article Summarization</strong> - Get AI summaries of any
                            article</span>
                    </li>
                    <li>
                        <span class="feature-icon">🎬</span>
                        <span class="feature-text"><strong>YouTube Summaries</strong> - Summarize YouTube videos with
                            chapters</span>
                    </li>
                    <li>
                        <span class="feature-icon">♾️</span>
                        <span class="feature-text"><strong>Monthly Credits</strong> - Generous monthly AI usage
                            allowance</span>
                    </li>
                </ul>
            </div>

            <footer class="footer">
                <p style="color: #999; font-size: 0.85rem;">
                    Payments are securely processed by Stripe via ExtensionPay.
                </p>
            </footer>
        </div>
    </div>

    <script src="/js/components/sidebar.js"></script>
    <script src="proAccount.js" type="module"></script>
</body>

</html>
```

## File: `proAccount/proAccount.js`
```javascript
/**
 * Pro Account Page JavaScript
 * Handles ExtPay integration for login, subscription, and account management
 */

// DOM Elements (initialized in init)
let loadingState, statusDisplay, errorState, subscriptionBadge;
let emailRow, userEmail, subscribedSinceRow, subscribedSince, nextBillingRow, nextBilling;
let creditsSection, creditsReset, creditsTotal;
let freeActions, proActions;
let loginBtn, subscribeBtn, logoutBtn, retryBtn, cancelSubscriptionLink;

/**
 * Initialize DOM elements
 */
function initElements() {
    loadingState = document.getElementById('loading-state');
    statusDisplay = document.getElementById('status-display');
    errorState = document.getElementById('error-state');
    subscriptionBadge = document.getElementById('subscription-badge');
    emailRow = document.getElementById('email-row');
    userEmail = document.getElementById('user-email');
    subscribedSinceRow = document.getElementById('subscribed-since-row');
    subscribedSince = document.getElementById('subscribed-since');
    nextBillingRow = document.getElementById('next-billing-row');
    nextBilling = document.getElementById('next-billing');
    creditsSection = document.getElementById('credits-section');
    creditsReset = document.getElementById('credits-reset');
    creditsTotal = document.getElementById('credits-total');
    freeActions = document.getElementById('free-actions');
    proActions = document.getElementById('pro-actions');
    loginBtn = document.getElementById('login-btn');
    subscribeBtn = document.getElementById('subscribe-btn');
    logoutBtn = document.getElementById('logout-btn');
    retryBtn = document.getElementById('retry-btn');
    cancelSubscriptionLink = document.getElementById('cancel-subscription-link');

    // Add event listeners here to ensure buttons exist
    if (loginBtn) loginBtn.addEventListener('click', handleLogin);
    if (subscribeBtn) subscribeBtn.addEventListener('click', handleSubscribe);
    if (logoutBtn) logoutBtn.addEventListener('click', handleLogout);
    if (retryBtn) retryBtn.addEventListener('click', fetchUserStatus);
    if (cancelSubscriptionLink) cancelSubscriptionLink.addEventListener('click', (e) => {
        e.preventDefault();
        chrome.runtime.sendMessage({ action: 'CANCEL_SUBSCRIPTION' });
    });
}

/**
 * Show a specific state (loading, status, or error)
 */
function showState(state) {
    loadingState.style.display = 'none';
    statusDisplay.style.display = 'none';
    errorState.style.display = 'none';

    switch (state) {
        case 'loading':
            loadingState.style.display = 'flex';
            break;
        case 'status':
            statusDisplay.style.display = 'block';
            break;
        case 'error':
            errorState.style.display = 'block';
            break;
    }
}

/**
 * Format date to readable string
 */
function formatDate(dateString) {
    if (!dateString) return '-';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

/**
 * Calculate days until end of month (for credits reset)
 */
function getDaysUntilReset() {
    const now = new Date();
    const lastDay = new Date(now.getFullYear(), now.getMonth() + 1, 0);
    const daysLeft = lastDay.getDate() - now.getDate();
    return daysLeft;
}

/**
 * Calculate next billing date (one month from paidAt)
 */
function getNextBillingDate(paidAt) {
    if (!paidAt) return null;
    const paidDate = new Date(paidAt);
    const now = new Date();

    // Calculate next billing date based on subscription anniversary
    let nextBilling = new Date(paidDate);
    while (nextBilling <= now) {
        nextBilling.setMonth(nextBilling.getMonth() + 1);
    }
    return nextBilling;
}

/**
 * Update credit value styling based on amount
 */
function updateCreditStyle(element, value) {
    element.textContent = value;
    element.classList.remove('low', 'empty');
    if (value === 0) {
        element.classList.add('empty');
    } else if (value <= 5) {
        element.classList.add('low');
    }
}

/**
 * Update the UI with user status
 */
function updateUI(user, credits = null) {
    showState('status');

    // Update badge
    if (user.paid) {
        subscriptionBadge.textContent = 'PRO ✓';
        subscriptionBadge.className = 'status-badge badge-pro';
        freeActions.style.display = 'none';
        proActions.style.display = 'block';
    } else if (user.trialActive) {
        subscriptionBadge.textContent = 'TRIAL';
        subscriptionBadge.className = 'status-badge badge-trial';
        freeActions.style.display = 'block';
        proActions.style.display = 'none';
    } else {
        subscriptionBadge.textContent = 'FREE';
        subscriptionBadge.className = 'status-badge badge-free';
        freeActions.style.display = 'block';
        proActions.style.display = 'none';
    }

    // Update email
    if (user.email) {
        emailRow.style.display = 'flex';
        userEmail.textContent = user.email;
    } else {
        emailRow.style.display = 'none';
    }

    // Update subscribed since and billing
    if (user.paid) {
        subscribedSinceRow.style.display = 'flex';
        subscribedSince.textContent = user.paidAt ? formatDate(user.paidAt) : '-';

        // Calculate and show next billing date
        const nextBillingDate = getNextBillingDate(user.paidAt);
        nextBillingRow.style.display = 'flex';
        nextBilling.textContent = nextBillingDate ? formatDate(nextBillingDate) : '-';
    } else {
        subscribedSinceRow.style.display = 'none';
        nextBillingRow.style.display = 'none';
    }

    // Update credits section
    // Update credits section
    if (user.paid) {
        creditsSection.style.display = 'block';

        // Update credits reset countdown
        const daysLeft = getDaysUntilReset();
        creditsReset.textContent = `Resets in ${daysLeft} day${daysLeft !== 1 ? 's' : ''}`;
        console.log('[ProAccount] Displaying credits section, credits object:', credits);

        if (credits && credits._remaining !== undefined) {
            updateCreditStyle(creditsTotal, credits._remaining);
        } else {
            // No cached credits yet - user needs to use an AI feature first
            creditsTotal.textContent = '—';
            creditsTotal.classList.remove('low', 'empty');
            // Update description to explain
            const desc = document.querySelector('.credits-description');
            if (desc) {
                desc.textContent = 'Use an AI feature to see your remaining credits';
            }
        }
    } else {
        creditsSection.style.display = 'none';
    }
}

/**
 * Fetch user status from background script
 */
async function fetchUserStatus() {
    showState('loading');

    try {
        const response = await chrome.runtime.sendMessage({ action: 'GET_PRO_STATUS' });
        console.log('[ProAccount] Received response:', response);
        console.log('[ProAccount] User:', response.user);
        console.log('[ProAccount] Credits:', response.credits);

        if (response.error) {
            throw new Error(response.error);
        }

        updateUI(response.user, response.credits);
    } catch (error) {
        console.error('Error fetching user status:', error);
        document.getElementById('error-message').textContent =
            error.message || 'Unable to load account information. Please try again.';
        showState('error');
    }
}

/**
 * Handle login button click
 */
async function handleLogin() {
    try {
        loginBtn.disabled = true;
        loginBtn.textContent = 'Opening...';

        await chrome.runtime.sendMessage({ action: 'OPEN_LOGIN_PAGE' });

        // Re-enable after a delay
        setTimeout(() => {
            loginBtn.disabled = false;
            loginBtn.innerHTML = `
                <svg viewBox="0 0 24 24" width="18" height="18">
                    <path d="M11 7L9.6 8.4l2.6 2.6H2v2h10.2l-2.6 2.6L11 17l5-5-5-5zm9 12h-8v2h8c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2h-8v2h8v14z" fill="currentColor" />
                </svg>
                Log In
            `;
            // Refresh status after login attempt
            fetchUserStatus();
        }, 2000);
    } catch (error) {
        console.error('Error opening login page:', error);
        loginBtn.disabled = false;
    }
}

/**
 * Handle subscribe button click
 */
async function handleSubscribe() {
    try {
        subscribeBtn.disabled = true;
        subscribeBtn.textContent = 'Opening...';

        await chrome.runtime.sendMessage({ action: 'OPEN_PAYMENT_PAGE' });

        // Re-enable after a delay
        setTimeout(() => {
            subscribeBtn.disabled = false;
            subscribeBtn.innerHTML = `
                <svg viewBox="0 0 24 24" width="18" height="18">
                    <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" fill="currentColor" />
                </svg>
                Subscribe to Pro
            `;
            // Refresh status after subscription attempt
            fetchUserStatus();
        }, 2000);
    } catch (error) {
        console.error('Error opening payment page:', error);
        subscribeBtn.disabled = false;
    }
}

/**
 * Handle logout button click
 */
async function handleLogout() {
    try {
        if (logoutBtn) {
            logoutBtn.disabled = true;
            logoutBtn.textContent = 'Logging out...';
        }

        await chrome.runtime.sendMessage({ action: 'LOGOUT' });

        // Reset button state after a delay (logging out usually opens a new tab/window)
        setTimeout(() => {
            if (logoutBtn) {
                logoutBtn.disabled = false;
                logoutBtn.innerHTML = `
                    <svg viewBox="0 0 24 24" width="18" height="18">
                        <path d="M17 7l-1.41 1.41L18.17 11H8v2h10.17l-2.58 2.58L17 17l5-5zM4 5h8V3H4c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h8v-2H4V5z" fill="currentColor"/>
                    </svg>
                    Log Out
                `;
            }
            // Refresh status - though user might still be logged in until they act on the ExtPay page
            fetchUserStatus();
        }, 1000);
    } catch (error) {
        console.error('Error logging out:', error);
        if (logoutBtn) logoutBtn.disabled = false;
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    initElements();
    fetchUserStatus();
});
```

