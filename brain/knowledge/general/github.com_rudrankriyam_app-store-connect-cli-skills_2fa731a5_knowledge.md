---
id: github.com-rudrankriyam-app-store-connect-cli-skil
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:17.623273
---

# KNOWLEDGE EXTRACT: github.com_rudrankriyam_app-store-connect-cli-skills_2fa731a5
> **Extracted on:** 2026-04-01 14:12:35
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523768/github.com_rudrankriyam_app-store-connect-cli-skills_2fa731a5

---

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Rudrank Riyam

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
# asc cli skills

A collection of Agent Skills for shipping with the [asc cli](https://github.com/rudrankriyam/App-Store-Connect-CLI) (`asc`). These skills are designed for zero-friction automation around builds, TestFlight, metadata, submissions, and signing.

This is a community-maintained, unofficial skill pack and is not affiliated with Apple.

Skills follow the Agent Skills format.

## Installation

Install this skill pack:

```bash
npx skills add rudrankriyam/app-store-connect-cli-skills
```

## Available Skills

### asc-cli-usage

Guidance for running `asc` commands (canonical verbs, flags, pagination, output, auth).

**Use when:**
- You need the correct `asc` command or flag combination
- You want JSON-first output and pagination tips for automation

**Example:**

```bash
Find the right asc command to list all builds for app 123456789 as JSON and paginate through everything.
```

### asc-workflow

Define and run repo-local automation graphs using `asc workflow` and `.asc/workflow.json`.

**Use when:**
- You are migrating from lane-based automation to repo-local workflows
- You need multi-step orchestration with machine-parseable JSON output for CI/agents
- You need hooks (`before_all`, `after_all`, `error`), conditionals (`if`), and private helper sub-workflows
- You want validation (`asc workflow validate`) with cycle/reference checks before execution

**Example:**

```bash
Create an asc workflow that stages a release, validates it, and only submits when CONFIRM_RELEASE=true.
```

### asc-app-create-ui

Create a new App Store Connect app via browser automation when no API exists.

**Use when:**
- You need to create an app record (name, bundle ID, SKU, primary language)
- You are comfortable logging in to App Store Connect in a real browser

**Example:**

```bash
Create a new App Store Connect app for com.example.myapp with SKU MYAPP123 and primary language English (U.S.).
```

### asc-xcode-build

Build, archive, export, and manage Xcode version/build numbers before uploading.

**Use when:**
- You need to create an IPA or PKG for upload
- You're setting up CI/CD build pipelines
- You need to configure ExportOptions.plist
- You're troubleshooting encryption compliance issues

**Example:**

```bash
Archive and export my macOS app as a PKG I can upload to App Store Connect.
```

### asc-shots-pipeline

Agent-first screenshot pipeline using xcodebuild/simctl, AXe, JSON plans, `asc screenshots frame` (experimental), and `asc screenshots upload`.

**Use when:**
- You need a repeatable simulator screenshot automation flow
- You want AXe-based UI driving before capture
- You need a staged pipeline (capture -> frame -> upload)
- You need to discover supported frame devices (`asc screenshots list-frame-devices`)
- You want pinned Koubou guidance for deterministic framing (`koubou==0.18.1`)

**Example:**

```bash
Build my iOS app, capture the home and settings screens in the simulator, frame them, and prepare them for upload.
```

### asc-release-flow

Readiness-first App Store submission guidance, including `asc release stage`, `asc submit preflight`, and first-time release blockers.

**Use when:**
- You want the quickest answer to "can I submit this app now?"
- You need to separate API-fixable, web-session-fixable, and manual blockers
- You're handling first-time submission issues around availability, IAPs, subscriptions, Game Center, or App Privacy

**Example:**

```bash
Check whether version 2.4.0 of my iOS app is ready for App Store submission, show the blockers, and tell me the next `asc` command to run.
```

### asc-signing-setup

Bundle IDs, capabilities, certificates, provisioning profiles, and encrypted signing sync.

**Use when:**
- You are onboarding a new app or bundle ID
- You need to create or rotate signing assets

**Example:**

```bash
Set up signing for com.example.app with iCloud enabled, a distribution certificate, and an App Store profile.
```

### asc-id-resolver

Resolve IDs for apps, builds, versions, groups, and testers.

**Use when:**
- A command requires IDs and you only have names
- You want deterministic outputs for automation

**Example:**

```bash
Resolve the App Store Connect app ID, latest build ID, and TestFlight group IDs for MyApp.
```

### asc-metadata-sync

Metadata and localization sync (including legacy metadata format migration).

**Use when:**
- You are updating App Store metadata or localizations
- You need to validate character limits before upload
- You need to update privacy policy URL or app-level metadata

**Example:**

```bash
Pull my App Store metadata into ./metadata, update the privacy policy URL, and push the changes back safely.
```

### asc-localize-metadata

Translate App Store metadata (description, keywords, what's new, subtitle) to multiple locales using LLM translation prompts and push via `asc`.

**Use when:**
- You want to localize an app's App Store listing from a source locale (usually en-US)
- You need locale-aware keywords (not literal translations) and strict character limit enforcement
- You want a review-before-upload workflow for translations

**Example:**

```bash
Translate my en-US App Store metadata into German, French, and Japanese, then show me the changes before upload.
```

### asc-aso-audit

Run an offline ASO audit on canonical App Store metadata under `./metadata` and surface keyword gaps using Astro MCP.

**Use when:**
- You want to audit subtitle, keywords, description, and what's new fields for waste and formatting issues
- You want keyword-gap analysis against Astro-tracked rankings and competitor terms
- You want follow-up actions that map cleanly to `asc metadata keywords ...`

**Example:**

```bash
Audit ./metadata for ASO problems, then show the highest-value keyword gaps from Astro for my latest version.
```

### asc-whats-new-writer

Generate engaging, localized App Store release notes from git log, bullet points, or free text using canonical metadata under `./metadata`.

**Use when:**
- You want polished What's New copy from rough release inputs
- You want localized release notes across existing locales
- You want a review-before-upload workflow using `asc metadata push` or direct metadata edits

**Example:**

```bash
Turn these release bullet points into polished What's New notes for en-US and localize them across my existing metadata locales.
```

### asc-submission-health

Preflight checks, digital-goods readiness validation, submission, and review monitoring.

**Use when:**
- You want to reduce submission failures
- You need to track review status and re-submit safely
- You're troubleshooting "version not in valid state" errors

**Example:**

```bash
Preflight my iOS submission, check encryption/content-rights issues, and tell me what will block review.
```

### asc-testflight-orchestration

Beta groups, testers, build distribution, and What to Test notes.

**Use when:**
- You manage multiple TestFlight groups and testers
- You need consistent beta rollout steps

**Example:**

```bash
Export my current TestFlight config, create a new external group, add testers, and attach the latest build.
```

### asc-build-lifecycle

Build processing, latest build resolution, and cleanup.

**Use when:**
- You are waiting on build processing
- You want automated cleanup and retention policies

**Example:**

```bash
Find the latest processed build for app 123456789 and preview expiring all TestFlight builds older than 90 days.
```

### asc-ppp-pricing

Territory-specific pricing using purchasing power parity (PPP).

**Use when:**
- You want different prices for different countries
- You are implementing localized pricing strategies
- You need to adjust prices based on regional purchasing power

**Example:**

```bash
Update my subscription pricing for India, Brazil, and Mexico using a PPP-style rollout and verify the result.
```

### asc-subscription-localization

Bulk-localize subscription and IAP display names across all App Store locales.

**Use when:**
- You want to set the same subscription display name in every language at once
- You need to fill in missing subscription/group/IAP localizations
- You're tired of clicking through each locale in App Store Connect manually

**Example:**

```bash
Set the display name Monthly Pro across all missing locales for this subscription and verify which locales were created.
```

### asc-revenuecat-catalog-sync

Reconcile App Store Connect subscriptions/IAP with RevenueCat products, entitlements, offerings, and packages.

**Use when:**
- You want to sync ASC product catalogs to RevenueCat
- You need to create missing ASC subscriptions/IAPs before mapping them
- You want an audit-first workflow with explicit apply confirmation

**Example:**

```bash
Audit my App Store Connect subscriptions and IAPs against RevenueCat, then create any missing mappings after I approve the plan.
```

### asc-notarization

Archive, export, and notarize macOS apps with Developer ID signing.

**Use when:**
- You need to notarize a macOS app for distribution outside the App Store
- You want the full flow: archive → Developer ID export → zip → notarize → staple
- You're troubleshooting Developer ID signing or trust chain issues

**Example:**

```bash
Archive my macOS app, export it for Developer ID, notarize the ZIP, and staple the result.
```

### asc-crash-triage

Triage TestFlight crashes, beta feedback, and performance diagnostics.

**Use when:**
- You want to review recent TestFlight crash reports
- You need a crash summary grouped by signature, device, and build
- You want to check beta tester feedback and screenshots
- You need performance diagnostics (hangs, disk writes, launches) for a build

**Example:**

```bash
Show me the latest TestFlight crashes and feedback for MyApp, grouped by signature and affected build.
```

### asc-wall-submit

Submit or update an app entry in the App-Store-Connect-CLI Wall of Apps using `asc apps wall submit`.

**Use when:**
- You want to add your app to the Wall of Apps
- You want to update an existing Wall entry
- You want the built-in CLI Wall submission flow

**Example:**

```bash
Submit app 1234567890 to the Wall of Apps using the built-in asc apps wall submit flow.
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

## Skill Structure

Each skill contains:
- `SKILL.md` - Instructions for the agent
- `scripts/` - Helper scripts for automation (optional)
- `references/` - Supporting documentation (optional)

## License

MIT
```

## File: `skills/asc-app-create-ui/SKILL.md`
```markdown
---
name: asc-app-create-ui
description: Create a new App Store Connect app record via browser automation. Use when there is no public API for app creation and you need an agent to drive the New App form.
---

# asc app create (UI automation)

Use this skill to create a new App Store Connect app by driving the web UI.
This is opt-in, local-only automation that requires the user to be signed in.

## Preconditions
- A browser automation tool is available (Playwright, Cursor browser MCP, or equivalent).
- User is signed in to App Store Connect (or can complete login + 2FA).
- The **bundle ID must already be registered** in the Apple Developer portal.
- Required inputs are known:
  - app name (max 30 characters)
  - bundle ID (must exist and be unused by another app)
  - SKU
  - platform (iOS, macOS, tvOS, visionOS)
  - primary language
  - user access (Full Access or Limited Access)

## Safety Guardrails
- Never export or store cookies.
- Use a visible browser session only.
- Pause for a final confirmation before clicking "Create" (for standalone scripts).
- Do not retry the Create action automatically on failure.

## Workflow

### 1. Preflight: register bundle ID and verify no existing app
```bash
# Register the bundle ID via public API (if not already registered)
asc bundle-ids create --identifier "com.example.app" --name "My App" --platform IOS

# Confirm no app record exists yet
asc apps list --bundle-id "com.example.app" --output json
```

### 2. Open App Store Connect
Navigate to `https://appstoreconnect.apple.com/apps` and ensure the user is signed in.

### 3. Open the New App form
The "New App" button (blue "+" icon) opens a **dropdown menu**, not a dialog directly.
- Click the "New App" button to open the dropdown.
- Click the "New App" **menu item** inside the dropdown.
- The creation dialog/modal appears.

### 4. Fill required fields (in order)

#### Platform (checkboxes)
The platforms are **checkboxes** (not radio buttons). Click the checkbox for the desired platform(s):
- iOS, macOS, tvOS, visionOS
- Multiple can be selected.

#### Name (text input)
- Label: `Name`
- Max 30 characters.

#### Primary Language (select/combobox)
- Label: `Primary Language`
- Use `select_option` or equivalent with the language label (e.g., `"English (U.S.)"`).

#### Bundle ID (select/combobox)
- Label: `Bundle ID`
- This is a `<select>` dropdown. The options load asynchronously after platform selection.
- Wait for the dropdown to finish loading (it shows "Loading..." initially).
- Select by matching the label text which includes both the name and identifier:
  `"My App - com.example.app"`

#### SKU (text input)
- Label: `SKU`

#### User Access (radio buttons) -- REQUIRED
- **This field is required.** The Create button stays disabled until one option is selected.
- Options: `Limited Access` or `Full Access`.
- These are custom radio buttons with `<span>` overlays.
- **Known issue:** Accessibility-based clicks may be intercepted by the overlay `<span>`.
- **Workaround:** Use `scrollIntoView` on the radio element first, then click the radio ref directly. This bypasses the overlay interception.

### 5. Click Create
- The "Create" button is disabled until all required fields are filled **and** User Access is selected.
- After clicking, the button text changes to "Creating" while processing.
- Wait for navigation to the new app's page (URL pattern: `/apps/<APP_ID>/...`).

### 6. Verify creation via API
```bash
asc apps view --id "APP_ID" --output json --pretty
# or
asc apps list --bundle-id "com.example.app" --output json
```

### 7. Hand off to post-create setup
```bash
asc app-setup info set --app "APP_ID" --primary-locale "en-US"
asc app-setup categories set --app "APP_ID" --primary GAMES
asc web apps availability create \
  --app "APP_ID" \
  --territory "USA,GBR" \
  --available-in-new-territories true
```

Use the experimental web flow above only for the first availability bootstrap. If app availability already exists, switch to `asc pricing availability edit --app "APP_ID" ...` for later territory changes.

## Known UI Automation Issues

### "New App" is a dropdown menu, not a direct action
The first click opens a menu with "New App" and "New App Bundle". You must click the menu item, not just the button.

### User Access radio buttons have span overlays
Apple's custom radio buttons wrap the `<input type="radio">` in styled `<span>` elements. Direct ref-based clicks may fail with "click target intercepted". The fix is:
1. Scroll the radio element into view (`scrollIntoView`).
2. Click the radio ref directly (not via offset or label click).

### Bundle ID dropdown loads asynchronously
After selecting a platform, the Bundle ID dropdown shows "Loading..." and is disabled. Wait for it to become enabled and populated before selecting.

### browser_fill may not trigger form validation
Apple's Ember.js forms use custom change handlers. `browser_fill` (atomic set) may not trigger validation. If the Create button stays disabled after filling all fields:
- Retype the value slowly (character-by-character) in at least one text field.
- Or click the field, clear it, and type slowly.

## Failure Handling
- If any field or button cannot be located, stop and request user help.
- Capture a screenshot and report the last known step.
- Do not retry the Create click automatically.
- On failure, the user should check the browser for validation errors (red outlines, inline messages).

## Notes
- This skill is a workaround for a missing public API. Apple's docs explicitly state: "Don't use this API to create new apps; instead, create new apps on the App Store Connect website."
- UI selectors can change without notice. Prefer role/label/text selectors over CSS.
- The only manual step should be signing in. Everything else is agent-drivable.
```

## File: `skills/asc-aso-audit/SKILL.md`
```markdown
---
name: asc-aso-audit
description: Run an offline ASO audit on canonical App Store metadata under `./metadata` and surface keyword gaps using Astro MCP. Use after pulling metadata with `asc metadata pull`.
---

# asc ASO audit

Run a two-phase ASO audit: offline checks against local metadata files, then keyword gap analysis via Astro MCP.

## Preconditions

- Metadata pulled locally into canonical files via `asc metadata pull --app "APP_ID" --version "1.2.3" --dir "./metadata"`.
- If metadata came from `asc migrate export` or `asc localizations download`, normalize it into the canonical `./metadata` layout before running this skill.
- For Astro gap analysis: app tracked in Astro MCP (optional — offline checks run without it).

## Before You Start

1. Read `references/aso_rules.md` to understand the rules each check enforces.
2. Identify the **latest version directory** under `metadata/version/` (highest semantic version number). Use this for all version-level fields.
3. The **primary locale** is `en-US` unless the user specifies otherwise.

## Metadata File Paths

- **App-info fields** (`subtitle`): `metadata/app-info/{locale}.json`
- **Version fields** (`keywords`, `description`, `whatsNew`): `metadata/version/{latest-version}/{locale}.json`
- **App name**: May not be present in exported metadata. If `name` is missing from the app-info JSON, fetch it via `asc apps info list` or ask the user. Do not flag it as a missing-field error.

## Phase 1: Offline Checks

Run these 5 checks against the local metadata directory. No network calls required.

### 1. Keyword Waste

Tokenize the `subtitle` field (and `name` if available). Flag any token that also appears in the `keywords` field — it is already indexed and wastes keyword budget.

```
Severity: ⚠️ Warning
Example:  "quran" appears in subtitle AND keywords — remove from keywords to free 6 characters
```

How to check:
1. Read `metadata/app-info/{locale}.json` for `subtitle` (and `name` if present)
2. Read `metadata/version/{latest-version}/{locale}.json` for `keywords`
3. Tokenize subtitle (+ name):
   - **Latin/Cyrillic scripts:** split by whitespace, strip leading/trailing punctuation, lowercase
   - **Chinese/Japanese/Korean:** split by `、` `，` `,` or iterate characters — each character or character-group is a token. Whitespace tokenization does not work for CJK.
   - **Arabic:** split by whitespace, then also generate prefix-stripped variants (remove ال prefix) since Apple likely normalizes definite articles. For example, "القرآن" in subtitle should flag both "القرآن" and "قرآن" in keywords.
4. Split keywords by comma, trim whitespace, lowercase
5. Report intersection (including fuzzy matches from prefix stripping)

### 2. Underutilized Fields

Flag fields using less than their recommended minimum:

| Field | Minimum | Limit | Rationale |
|-------|---------|-------|-----------|
| Keywords | 90 chars | 100 | 90%+ usage maximizes indexing |
| Subtitle | 20 chars | 30 | 65%+ usage recommended |

```
Severity: ⚠️ Warning
Example:  keywords is 62/100 characters (62%) — 38 characters of indexing opportunity unused
```

### 3. Missing Fields

Flag empty or missing required fields: `subtitle`, `keywords`, `description`, `whatsNew`.

Note: `name` may not be in the export — only flag it if the app-info JSON explicitly contains a `name` key with an empty value.

```
Severity: ❌ Error
Example:  subtitle is empty for locale en-US
```

### 4. Bad Keyword Separators

Check the `keywords` field for formatting issues:
- Spaces after commas (`quran, recitation`)
- Semicolons instead of commas (`quran;recitation`)
- Pipes instead of commas (`quran|recitation`)

```
Severity: ❌ Error
Example:  keywords contain spaces after commas — wastes 3 characters
```

### 5. Cross-Locale Keyword Gaps

Compare `keywords` fields across all available locales. Flag locales where keywords are identical to the primary locale (`en-US` by default) — this usually means they were not localized.

```
Severity: ⚠️ Warning
Example:  ar keywords identical to en-US — likely not localized for Arabic market
```

How to check:
1. Load keywords for all locales
2. Compare each non-primary locale against the primary
3. Flag exact matches (case-insensitive)

### 6. Description Keyword Coverage

Check whether keywords appear naturally in the `description` field. While Apple does **not** index descriptions for search, users who see their search terms reflected in the description are more likely to download — this improves conversion rate, which indirectly boosts rankings.

```
Severity: 💡 Info
Example:  3 of 16 keywords not found in description: namaz, tarteel, adhan
```

How to check:
1. Load `keywords` and `description` for each locale
2. For each keyword, check if it appears as a substring in the description (case-insensitive)
3. Account for inflected forms: Arabic root matches, verb conjugations (e.g., "memorizar" ≈ "memorices"), and case declensions (e.g., Russian "сура" ≈ "суры")
4. Report missing keywords per locale — recommend weaving them naturally into existing sentences
5. Do NOT flag: Latin-script keywords in non-Latin descriptions (e.g., "quran" in Cyrillic text) — these target separate search paths

## Phase 2: Astro MCP Keyword Gap Analysis

If Astro MCP is available and the app is tracked, run keyword gap analysis. **Run this per store/locale, not just for the US store** — keyword popularity varies dramatically across markets.

### Steps

1. **Get current keywords**: Call `get_app_keywords` with the app ID to retrieve tracked keywords and their current rankings.

2. **Ensure multi-store tracking**: For each locale with a corresponding App Store territory (e.g., `ar-SA` → Saudi Arabia, `fr-FR` → France, `tr` → Turkey), use `add_keywords` to add keyword tracking in that store. Without this, `search_rankings` returns empty for non-US stores.

3. **Extract competitor keywords**: Call `extract_competitors_keywords` with 3-5 top competitor app IDs to find keyword gaps. This is the highest-value Astro tool — it reveals keywords competitors rank for that you don't. Run this per store when possible.

4. **Get suggestions**: Call `get_keyword_suggestions` with the app ID for additional recommendations based on category analysis.

5. **Check current rankings**: Call `search_rankings` to see where the app currently ranks for tracked keywords in each store.

6. **Diff against metadata**: Compare suggested and competitor keywords against the tokens present in `subtitle`, `name` (if available), and `keywords` fields from the local metadata.

7. **Surface gaps**: Report all gaps ranked by popularity score (highest first). Include the source (competitor analysis vs. suggestion).

### Cross-Field Combo Strategy

When recommending keyword additions, consider how single words combine across indexed fields (title + subtitle + keywords). For example:
- Adding "namaz" to keywords when "vakti" is already present enables matching the search "namaz vakti" (66 popularity)
- Adding "holy" to keywords when "Quran" is in the subtitle enables matching "holy quran" (58 popularity)

Flag high-value combos in recommendations.

### Skip Conditions

- Astro MCP not connected → skip with note: "Connect Astro MCP for keyword gap analysis"
- App not tracked in Astro → skip with note: "Add app to Astro with `mcp__astro__add_app` for gap analysis"
- Store not tracked for a locale → add tracking with `add_keywords` before querying

## Output Format

Present results as a single audit report. The report covers only the latest version directory.

```
### ASO Audit Report

**App:** [name] | **Primary Locale:** [locale]
**Metadata source:** [path including version number]

#### Field Utilization

| Field | Value | Length | Limit | Usage |
|-------|-------|--------|-------|-------|
| Name | ... | X | 30 | X% |
| Subtitle | ... | X | 30 | X% |
| Keywords | ... | X | 100 | X% |
| Promotional Text | ... | X | 170 | X% |
| Description | (first 50 chars)... | X | 4000 | X% |

#### Offline Checks

| # | Check | Severity | Field | Locale | Detail |
|---|-------|----------|-------|--------|--------|
| 1 | Keyword waste | ⚠️ | keywords | en-US | "quran" duplicated in subtitle |

**Summary:** X errors, Y warnings across Z locales

#### Keyword Gap Analysis (Astro MCP)

| Keyword | Popularity | In Metadata? | Suggested Action |
|---------|-----------|--------------|-----------------|
| quran recitation | 72 | ❌ | Add to keywords |

#### Recommendations

1. [Highest priority action — errors first]
2. [Next priority — keyword waste]
3. [Utilization improvements]
4. [Keyword gap opportunities]
```

## Notes

- Offline checks work without any network access — they read local files only.
- Astro gap analysis is additive — the audit is useful even without it.
- Run this skill after `asc metadata pull` to ensure canonical metadata files are current.
- For keyword-only follow-up after the audit, prefer the canonical keyword workflow:
  - `asc metadata keywords diff --app "APP_ID" --version "1.2.3" --dir "./metadata"`
  - `asc metadata keywords apply --app "APP_ID" --version "1.2.3" --dir "./metadata" --confirm`
  - `asc metadata keywords sync --app "APP_ID" --version "1.2.3" --dir "./metadata" --input "./keywords.csv"` when importing external keyword research
- After making changes, re-run the audit to verify fixes.
- The Field Utilization table includes promotional text for completeness, but no check validates its content (it is not indexed by Apple).
```

## File: `skills/asc-aso-audit/references/aso_rules.md`
```markdown
# ASO Rules Reference

Rules enforced by the asc-aso-audit skill. Each rule links to the check that tests it.

## Indexing Rules

- **Title, subtitle, and keyword field are indexed** for App Store search.
- **Description and promotional text are NOT indexed.** Description is for conversion (users see search terms reflected → higher download rate); promotional text is for seasonal messaging.
- **Description keyword coverage still matters** — while not indexed, descriptions that naturally include keyword terms improve conversion rate, which indirectly boosts search rankings.
- **Screenshot captions are OCR-indexed** (since June 2025 algorithm update). Use high-value keywords in caption text. *(Informational — not checked by this audit.)*
- **Apple Full Text Search combines words across title + subtitle + keywords.** Single words enable more combinations than multi-word phrases. Example: "quran" + "recitation" in separate fields still matches "quran recitation".
- **Cross-field combo optimization:** When adding keywords, consider what search queries they enable in combination with words already in title/subtitle. Example: adding "holy" to keywords when "Quran" is in subtitle enables the search "holy quran".

## Keyword Field Rules

- **Comma-separated, no spaces after commas.** Spaces waste characters. `quran,recitation` not `quran, recitation`.
- **Do not duplicate words already in title or subtitle.** Apple indexes all three fields together; repeating a word wastes keyword budget.
- **Do not use the app name in keywords.** It is already indexed.
- **Avoid plurals if the singular is already present** — Apple handles stemming.
- **Prefer single words over multi-word phrases** — single words enable more cross-field combinations and use fewer characters.
- **Always validate with popularity data** — never guess keyword value. Use Astro MCP or similar tools to check popularity scores before making swaps.

## Character Limits

| Field | Limit |
|-------|-------|
| Name | 30 |
| Subtitle | 30 |
| Keywords | 100 |
| Description | 4,000 |
| What's New | 4,000 |
| Promotional Text | 170 |

## Localization Rules

- **Localize keywords per market** — do not just translate your primary keywords. Research what users in each locale actually search for.
- **English (US) keywords may carry into other English-speaking storefronts** but dedicated localization always outperforms.
- **Identical keyword fields across locales** usually indicates untranslated/unlocalized metadata.
- **Track keywords in each locale's store** — keyword popularity varies dramatically across territories. A keyword with 70 popularity in the US store may have 5 popularity in France. Use Astro `add_keywords` to set up tracking per store before analyzing.
- **Use competitor analysis per store** — top competitors differ by market. Run `extract_competitors_keywords` with locale-relevant competitor apps.

## Non-Latin Script Rules

- **Arabic ال-prefix:** Apple likely normalizes the definite article ال. Treat "القرآن" (with ال) and "قرآن" (without) as probable duplicates when checking subtitle/keyword overlap.
- **Arabic hamza variants:** Users commonly search without hamza diacritics. "قران" (no hamza) and "قرآن" (with hamza) target different search queries — both may be worth including.
- **Chinese tokenization:** Chinese text has no word-separating spaces. Subtitle tokens are separated by `、` (enumeration comma) or `，` (full comma). Do not use whitespace tokenization for Chinese metadata.
- **Cyrillic transliteration:** Including the Latin spelling of terms (e.g., "quran" in a Russian keyword field) targets users who search in Latin script on Cyrillic storefronts.

## Utilization Guidelines

- **Keyword field:** aim for 90%+ character usage (90+ of 100 chars).
- **Subtitle:** aim for 65%+ character usage (20+ of 30 chars). Short subtitles waste indexing opportunity.
- **Name:** balance branding with keyword inclusion.
```

## File: `skills/asc-build-lifecycle/SKILL.md`
```markdown
---
name: asc-build-lifecycle
description: Track build processing, find latest builds, and clean up old builds with asc. Use when managing build retention or waiting on processing.
---

# asc build lifecycle

Use this skill to manage build state, processing, and retention.

## Find the right build
- Latest build:
  - `asc builds info --app "APP_ID" --latest --version "1.2.3" --platform IOS`
- Next safe build number:
  - `asc builds next-build-number --app "APP_ID" --version "1.2.3" --platform IOS`
- Recent builds:
  - `asc builds list --app "APP_ID" --sort -uploadedDate --limit 10`

## Inspect processing state
- `asc builds info --build-id "BUILD_ID"`

## Distribution flows
- Prefer end-to-end:
  - `asc publish testflight --app "APP_ID" --ipa "./app.ipa" --group "GROUP_ID" --wait`
  - `asc publish appstore --app "APP_ID" --ipa "./app.ipa" --version "1.2.3" --wait --submit --confirm`

## Cleanup
- Preview expiration:
  - `asc builds expire-all --app "APP_ID" --older-than 90d --dry-run`
- Apply expiration:
  - `asc builds expire-all --app "APP_ID" --older-than 90d --confirm`
- Single build:
  - `asc builds expire --build-id "BUILD_ID" --confirm`

## Notes
- `asc builds upload` prepares upload operations only; use `asc publish` for end-to-end flows.
- For long processing times, use `--wait`, `--poll-interval`, and `--timeout` where supported.
```

## File: `skills/asc-cli-usage/SKILL.md`
```markdown
---
name: asc-cli-usage
description: Guidance for using asc cli in this repo (flags, output formats, pagination, auth, and discovery). Use when asked to run or design asc commands or interact with App Store Connect via the CLI.
---

# asc cli usage

Use this skill when you need to run or design `asc` commands for App Store Connect.

## Command discovery
- Always use `--help` to discover commands and flags.
  - `asc --help`
  - `asc builds --help`
  - `asc builds list --help`

## Canonical verbs (current asc)
- Prefer `view` over legacy `get` aliases for read-only commands in docs and automation.
  - `asc apps view --id "APP_ID"`
  - `asc versions view --version-id "VERSION_ID"`
  - `asc pricing availability view --app "APP_ID"`
- Prefer `edit` for update-only availability surfaces and other canonical edit flows.
  - `asc pricing availability edit --app "APP_ID" --territory "USA,GBR" --available true`
  - `asc app-setup availability edit --app "APP_ID" --territory "USA,GBR" --available true`
  - `asc xcode version edit --build-number "42"`
- Keep `set` where the CLI intentionally models a higher-level replacement/configuration flow and `--help` still shows `set` as the canonical verb.

## Flag conventions
- Use explicit long flags (e.g., `--app`, `--output`).
- Prefer explicit flags in automation; some newer commands can prompt for missing fields when run interactively.
- Destructive operations require `--confirm`.
- Use `--paginate` when the user wants all pages.

## Output formats
- Output defaults are TTY-aware: `table` in interactive terminals, `json` when piped or non-interactive.
- Use `--output table` or `--output markdown` only for human-readable output.
- `--pretty` is only valid with JSON output.

## Authentication and defaults
- Prefer keychain auth via `asc auth login`.
- Fallback env vars: `ASC_KEY_ID`, `ASC_ISSUER_ID`, `ASC_PRIVATE_KEY_PATH`, `ASC_PRIVATE_KEY`, `ASC_PRIVATE_KEY_B64`.
- `ASC_APP_ID` can provide a default app ID.
- When permissions are unclear, inspect exact API key role coverage with `asc web auth capabilities`.
  - This lives under the experimental web auth surface.
  - It can resolve the current local auth by default, or inspect a specific key with `--key-id`.

## Timeouts
- `ASC_TIMEOUT` / `ASC_TIMEOUT_SECONDS` control request timeouts.
- `ASC_UPLOAD_TIMEOUT` / `ASC_UPLOAD_TIMEOUT_SECONDS` control upload timeouts.
```

## File: `skills/asc-crash-triage/SKILL.md`
```markdown
---
name: asc-crash-triage
description: Triage TestFlight crashes, beta feedback, and performance diagnostics using asc. Use when the user asks about TF crashes, TestFlight crash reports, beta tester feedback, app hangs, disk writes, launch diagnostics, or wants a crash summary for a build or app.
---

# asc crash triage

Use this skill to fetch, analyze, and summarize TestFlight crash reports, beta feedback, and performance diagnostics.

## Workflow

1. Resolve the app ID if not provided (use `asc apps list`).
2. Fetch data with the appropriate command.
3. Parse JSON output and present a human-readable summary.

## TestFlight crash reports

List recent crashes (newest first):

- `asc testflight crashes list --app "APP_ID" --sort -createdDate --limit 10`
- Filter by build: `asc testflight crashes list --app "APP_ID" --build "BUILD_ID" --sort -createdDate --limit 10`
- Filter by device/OS: `asc testflight crashes list --app "APP_ID" --device-model "iPhone16,2" --os-version "18.0"`
- All crashes: `asc testflight crashes list --app "APP_ID" --paginate`
- Table view: `asc testflight crashes list --app "APP_ID" --sort -createdDate --limit 10 --output table`

## TestFlight beta feedback

List recent feedback (newest first):

- `asc testflight feedback list --app "APP_ID" --sort -createdDate --limit 10`
- With screenshots: `asc testflight feedback list --app "APP_ID" --sort -createdDate --limit 10 --include-screenshots`
- Filter by build: `asc testflight feedback list --app "APP_ID" --build "BUILD_ID" --sort -createdDate`
- All feedback: `asc testflight feedback list --app "APP_ID" --paginate`

## Performance diagnostics (hangs, disk writes, launches)

Requires a build ID. Resolve via `asc builds info --app "APP_ID" --latest --platform IOS` or `asc builds list --app "APP_ID" --sort -uploadedDate --limit 5`.

- List diagnostic signatures: `asc performance diagnostics list --build "BUILD_ID"`
- Filter by type: `asc performance diagnostics list --build "BUILD_ID" --diagnostic-type "HANGS"`
  - Types: `HANGS`, `DISK_WRITES`, `LAUNCHES`
- View logs for a signature: `asc performance diagnostics view --id "SIGNATURE_ID"`
- Download all metrics: `asc performance download --build "BUILD_ID" --output ./metrics.json`

## Resolving IDs

- App ID from name: `asc apps list --name "AppName"` or `asc apps list --bundle-id "com.example.app"`
- Latest build ID: `asc builds info --app "APP_ID" --latest --platform IOS`
- Recent builds: `asc builds list --app "APP_ID" --sort -uploadedDate --limit 5`
- Set default: `export ASC_APP_ID="APP_ID"`

## Summary format

When presenting results, organize by severity and frequency:

1. **Total count** — how many crashes/feedbacks in the result set.
2. **Top crash signatures** — group by exception type or crash reason, ranked by count.
3. **Affected builds** — which build versions are impacted.
4. **Device & OS breakdown** — most affected device models and OS versions.
5. **Timeline** — when crashes started or spiked.

For performance diagnostics, highlight the highest-weight signatures first.

## Notes

- Default output is JSON; use `--output table` or `--output markdown` for quick human review.
- Use `--paginate` to fetch all pages when doing a full analysis.
- Use `--pretty` with JSON for debugging command output.
- Crash data from App Store Connect may have 24-48h delay.
```

## File: `skills/asc-id-resolver/SKILL.md`
```markdown
---
name: asc-id-resolver
description: Resolve App Store Connect IDs (apps, builds, versions, groups, testers) from human-friendly names using asc. Use when commands require IDs.
---

# asc id resolver

Use this skill to map names to IDs needed by other commands.

## App ID
- By bundle ID or name:
  - `asc apps list --bundle-id "com.example.app"`
  - `asc apps list --name "My App"`
- Fetch everything:
  - `asc apps --paginate`
- Set default:
  - `ASC_APP_ID=...`

## Build ID
- Latest build:
  - `asc builds info --app "APP_ID" --latest --version "1.2.3" --platform IOS`
- Recent builds:
  - `asc builds list --app "APP_ID" --sort -uploadedDate --limit 5`

## Version ID
- `asc versions list --app "APP_ID" --paginate`

## TestFlight IDs
- Groups:
  - `asc testflight groups list --app "APP_ID" --paginate`
- Testers:
  - `asc testflight testers list --app "APP_ID" --paginate`

## Pre-release version IDs
- `asc testflight pre-release list --app "APP_ID" --platform IOS --paginate`

## Review submission IDs
- `asc review submissions-list --app "APP_ID" --paginate`

## Output tips
- JSON is default; use `--pretty` for debug.
- For human viewing, use `--output table` or `--output markdown`.

## Guardrails
- Prefer `--paginate` on list commands to avoid missing IDs.
- Use `--sort` where available to make results deterministic.
```

## File: `skills/asc-localize-metadata/SKILL.md`
```markdown
---
name: asc-localize-metadata
description: Automatically translate and sync App Store metadata (description, keywords, what's new, subtitle) to multiple languages using LLM translation and asc CLI. Use when asked to localize an app's App Store listing, translate app descriptions, or add new languages to App Store Connect.
---

# asc localize metadata

Use this skill to pull English (or any source locale) App Store metadata, translate it with LLM, and push translations back to App Store Connect — all automated.

## Command discovery and output conventions

- Always confirm flags with `--help` for the exact `asc` version:
  - `asc localizations --help`
  - `asc localizations download --help`
  - `asc localizations upload --help`
  - `asc apps info edit --help`
- Prefer explicit long flags (`--app`, `--version`, `--version-id`, `--type`, `--app-info`).
- Default output is JSON; use `--output table` only for human verification steps.
- Prefer deterministic ID-based operations. Do not "pick the first row" via `head -1` unless the user explicitly agrees.

## Preconditions
- Auth configured (`asc auth login` or `ASC_*` env vars)
- Know your app ID (`asc apps list` to find it)
- At least one locale (typically en-US) already has metadata in App Store Connect

## Supported Locales

App Store Connect locales for version and app-info localizations:
```
ar-SA, ca, cs, da, de-DE, el, en-AU, en-CA, en-GB, en-US,
es-ES, es-MX, fi, fr-CA, fr-FR, he, hi, hr, hu, id, it,
ja, ko, ms, nl-NL, no, pl, pt-BR, pt-PT, ro, ru, sk,
sv, th, tr, uk, vi, zh-Hans, zh-Hant
```

## Two Types of Metadata

### Version Localizations (per-release)
Fields: `description`, `keywords`, `whatsNew`, `supportUrl`, `marketingUrl`, `promotionalText`

### App Info Localizations (app-level, persistent)
Fields: `name`, `subtitle`, `privacyPolicyUrl`, `privacyChoicesUrl`, `privacyPolicyText`

## Workflow

### Step 1: Resolve IDs

```bash
# Find app ID
asc apps list --output table

# Find latest version ID
asc versions list --app "APP_ID" --state READY_FOR_DISTRIBUTION --output table
# or for editable version:
asc versions list --app "APP_ID" --state PREPARE_FOR_SUBMISSION --output table

# Find app info ID (for app-level fields like name/subtitle)
asc apps info list --app "APP_ID" --output table
```

Notes:
- Version-localization fields (description, keywords, whatsNew, etc.) are per-version.
- App-info fields (name, subtitle, privacy URLs/text) are app-level and use `--type app-info`.
- If you only have names (app name, version string) and need IDs deterministically, use `asc-id-resolver`.

### Step 2: Download source locale

```bash
# Download version localizations to local .strings files
# (description, keywords, whatsNew, promotionalText, supportUrl, marketingUrl, ...)
asc localizations download --version "VERSION_ID" --path "./localizations"

# Download app-info localizations to local .strings files
# (name, subtitle, privacyPolicyUrl, privacyChoicesUrl, privacyPolicyText, ...)
asc localizations download --app "APP_ID" --type app-info --app-info "APP_INFO_ID" --path "./app-info-localizations"
```

This creates files like `./localizations/en-US.strings` and `./app-info-localizations/en-US.strings`. If download is unavailable, read fields individually:

```bash
# List version localizations to see existing locales and their content
asc localizations list --version "VERSION_ID" --output table
```

### Step 3: Translate with LLM

For each target locale, translate the source text. Follow these rules:

#### Translation Guidelines
- **Tone & Register**: Always use formal, polite language. Use formal "you" forms where the language distinguishes them (Russian: «вы», German: «Sie», French: «vous», Spanish: «usted», Dutch: «u», Italian: «Lei», Portuguese: «você» formal, etc.). App Store descriptions are professional marketing copy — never use casual or informal register.
- **description**: Translate naturally, adapt tone to local market. Keep formatting (line breaks, bullet points, emoji). Stay within 4000 chars.
- **keywords**: Do NOT literally translate. Research what users in that locale would search for. Comma-separated, max 100 chars total. No duplicates, no app name (Apple adds it automatically).
- **whatsNew**: Translate release notes. Keep it concise. Max 4000 chars.
- **promotionalText**: Translate marketing hook. Max 170 chars. This can be updated without a new version.
- **subtitle**: Translate or adapt tagline. Max 30 chars — this is very tight, may need creative adaptation.
- **name**: Usually keep the original app name. Only translate if the user explicitly asks. Max 30 chars.

#### LLM Translation Prompt Template

For each target locale, use this approach:

```
Translate the following App Store metadata from {source_locale} to {target_locale}.

Rules:
- description: Natural, fluent translation. Preserve formatting (line breaks, bullets, emoji). Max 4000 chars.
- keywords: Do NOT literally translate. Choose keywords native speakers would search for in the App Store. Comma-separated, max 100 chars total. Do not include the app name.
- whatsNew: Translate release notes naturally. Max 4000 chars.
- promotionalText: Translate marketing tagline. Max 170 chars.
- subtitle: Adapt tagline creatively to fit 30 chars max.
- name: Keep the original app name unless explicitly requested to translate it. Max 30 chars.
- Use formal, polite language and formal "you" forms (Russian: вы, German: Sie, French: vous, Spanish: usted, Dutch: u, etc.). App Store copy is professional marketing — never use informal register.
- Respect cultural context. A playful tone in English may need adjustment for formal markets (e.g., ja, de-DE).

Source ({source_locale}):
description: """
{description}
"""

keywords: {keywords}

whatsNew: """
{whatsNew}
"""

promotionalText: {promotionalText}

name: {name}

subtitle: {subtitle}
```

### Step 4: Upload translations

#### Option A: Via .strings files (bulk)

Create a `.strings` file per locale in the appropriate directory.

Version localization example:

```
// nl-NL.strings
"description" = "Je app-beschrijving hier";
"keywords" = "wiskunde,kinderen,tafels,leren";
"whatsNew" = "Bugfixes en verbeteringen";
"promotionalText" = "Leer de tafels van vermenigvuldiging!";
```

Then upload version localizations:
```bash
asc localizations upload --version "VERSION_ID" --path "./localizations"
```

App-info localization example:

```
// nl-NL.strings
"subtitle" = "Leer tafels spelenderwijs";
```

Then upload app-info localizations:
```bash
asc localizations upload --app "APP_ID" --type app-info --app-info "APP_INFO_ID" --path "./app-info-localizations"
```

#### Option B: Via individual commands (fine control)

```bash
# Version localization fields (fine control).
# Prefer passing the explicit version ID for determinism.
asc apps info edit --app "APP_ID" --version-id "VERSION_ID" --locale "nl-NL" \
  --description "Je beschrijving..." \
  --keywords "wiskunde,kinderen,tafels" \
  --whats-new "Bugfixes en verbeteringen"
```

For app-level fields:
```bash
# Subtitle/name (app-info localization) is managed via app-info localizations.
# Use the app-info localization .strings + upload flow (there is no `asc app-infos localizations ...` command).
#
# 1) Edit: ./app-info-localizations/nl-NL.strings
# "subtitle" = "Leer tafels spelenderwijs";
#
# 2) Upload:
asc localizations upload --app "APP_ID" --type app-info --app-info "APP_INFO_ID" --path "./app-info-localizations"
```

### Step 5: Verify

```bash
# Check all locales are present
asc localizations list --version "VERSION_ID" --output table

# Check app info localizations
asc localizations list --app "APP_ID" --type app-info --app-info "APP_INFO_ID" --output table
```

## Character Limits (enforce before upload!)

| Field | Limit |
|-------|-------|
| Name | 30 |
| Subtitle | 30 |
| Keywords | 100 (comma-separated) |
| Description | 4000 |
| What's New | 4000 |
| Promotional Text | 170 |

**Always validate** translated text fits within limits before uploading. Truncated text looks unprofessional. If translation exceeds the limit, shorten it — do not truncate mid-sentence.

## Full Example: Add nl-NL and ru to Roxy Math

```bash
# 1) Resolve IDs deterministically (do not auto-pick the "first" row)
# If you only have names, use asc-id-resolver skill.
asc apps list --output table
APP_ID="APP_ID_HERE"

asc versions list --app "$APP_ID" --state PREPARE_FOR_SUBMISSION --output table
VERSION_ID="VERSION_ID_HERE"

asc apps info list --app "$APP_ID" --output table
APP_INFO_ID="APP_INFO_ID_HERE"

# 2) Download English source (or your chosen source locale)
asc localizations download --version "$VERSION_ID" --path "./localizations"
asc localizations download --app "$APP_ID" --type app-info --app-info "$APP_INFO_ID" --path "./app-info-localizations"

# 3) Read en-US.strings, translate to nl-NL and ru (LLM step)

# 4) Write nl-NL.strings and ru.strings to:
#    - ./localizations/ (version localization fields)
#    - ./app-info-localizations/ (subtitle/name/privacy fields)

# 5) Upload all
asc localizations upload --version "$VERSION_ID" --path "./localizations"
asc localizations upload --app "$APP_ID" --type app-info --app-info "$APP_INFO_ID" --path "./app-info-localizations"

# 6) Verify
asc localizations list --version "$VERSION_ID" --output table
asc localizations list --app "$APP_ID" --type app-info --app-info "$APP_INFO_ID" --output table
```

## Agent Behavior

1. **Always start by reading the source locale** — never translate from memory or assumptions.
2. **Check existing localizations first** — don't overwrite existing translations unless the user asks to update them.
3. **Version vs app-info is different** — version fields live under `--version "VERSION_ID"`; subtitle/name/privacy live under `--app ... --type app-info`.
4. **Prefer deterministic IDs** — do not select IDs via `head -1` unless explicitly requested; use `--output table` for selection or `asc-id-resolver`.
5. **Validate character limits** before uploading. Count characters for each field. If over limit, re-translate shorter.
6. **Keywords are special** — do not literally translate. Research locale-appropriate search terms. Think like a user searching the App Store in that language.
7. **Show the user translations before uploading** — present a summary table of all fields × locales for approval. Do not push without confirmation.
8. **Process one locale at a time** if translating many languages — easier to review and catch errors.
9. **If upload fails** for a locale, log the error, continue with other locales, report all failures at the end.
10. **For updates to existing localizations** — download current, show diff of what will change, get approval, then upload.

## Notes
- Version localizations are tied to a specific version. Create the version first if it doesn't exist.
- `promotionalText` can be updated anytime without a new version submission.
- `whatsNew` is only relevant for updates, not the first version.
- Use `asc-id-resolver` skill if you only have app/version names instead of IDs.
- Use `asc-metadata-sync` skill for non-translation metadata operations.
- For subscription/IAP display name localization, use `asc-subscription-localization` skill instead.
```

## File: `skills/asc-metadata-sync/SKILL.md`
```markdown
---
name: asc-metadata-sync
description: Sync and validate App Store metadata and localizations with asc, including legacy metadata format migration. Use when updating metadata or translations.
---

# asc metadata sync

Use this skill to keep local metadata in sync with App Store Connect.

## Two Types of Localizations

### 1. Version Localizations (per-release)
Fields: `description`, `keywords`, `whatsNew`, `supportUrl`, `marketingUrl`, `promotionalText`

```bash
# List version localizations
asc localizations list --version "VERSION_ID"

# Download
asc localizations download --version "VERSION_ID" --path "./localizations"

# Upload from .strings files
asc localizations upload --version "VERSION_ID" --path "./localizations"
```

### 2. App Info Localizations (app-level)
Fields: `name`, `subtitle`, `privacyPolicyUrl`, `privacyChoicesUrl`, `privacyPolicyText`

```bash
# First, find the app info ID
asc apps info list --app "APP_ID"

# List app info localizations
asc localizations list --app "APP_ID" --type app-info --app-info "APP_INFO_ID"

# Upload app info localizations
asc localizations upload --app "APP_ID" --type app-info --app-info "APP_INFO_ID" --path "./app-info-localizations"
```

**Note:** If you get "multiple app infos found", you must specify `--app-info` with the correct ID.

## Legacy Fastlane Metadata Workflow

### Export current state
```bash
asc migrate export --app "APP_ID" --version-id "VERSION_ID" --output-dir "./fastlane"
```

### Validate local files
```bash
asc migrate validate --fastlane-dir "./fastlane"
```
This checks character limits and required fields.

### Import updates
```bash
asc migrate import --app "APP_ID" --version-id "VERSION_ID" --fastlane-dir "./fastlane" --dry-run
asc migrate import --app "APP_ID" --version-id "VERSION_ID" --fastlane-dir "./fastlane"
```

## Quick Field Updates

### Version-specific fields
```bash
# What's New
asc apps info edit --app "APP_ID" --locale "en-US" --whats-new "Bug fixes and improvements"

# Description
asc apps info edit --app "APP_ID" --locale "en-US" --description "Your app description here"

# Keywords
asc apps info edit --app "APP_ID" --locale "en-US" --keywords "keyword1,keyword2,keyword3"

# Support URL
asc apps info edit --app "APP_ID" --locale "en-US" --support-url "https://support.example.com"
```

### Version metadata
```bash
# Copyright
asc versions update --version-id "VERSION_ID" --copyright "2026 Your Company"

# Release type
asc versions update --version-id "VERSION_ID" --release-type AFTER_APPROVAL
```

### TestFlight notes
```bash
asc build-localizations create --build "BUILD_ID" --locale "en-US" --whats-new "TestFlight notes here"
```

## .strings File Format

For bulk updates, use .strings files:

```
// en-US.strings
"description" = "Your app description";
"keywords" = "keyword1,keyword2,keyword3";
"whatsNew" = "What's new in this version";
"supportUrl" = "https://support.example.com";
```

For app-info type:
```
// en-US.strings (app-info type)
"privacyPolicyUrl" = "https://example.com/privacy";
"name" = "Your App Name";
"subtitle" = "Your subtitle";
```

## Multi-Language Workflow

1. Export all localizations:
```bash
asc localizations download --version "VERSION_ID" --path "./localizations"
```

2. Translate the .strings files (or use translation service)

3. Upload all at once:
```bash
asc localizations upload --version "VERSION_ID" --path "./localizations"
```

4. Verify:
```bash
asc localizations list --version "VERSION_ID" --output table
```

## Character Limits

| Field | Limit |
|-------|-------|
| Name | 30 |
| Subtitle | 30 |
| Keywords | 100 (comma-separated) |
| Description | 4000 |
| What's New | 4000 |
| Promotional Text | 170 |

Use `asc metadata validate --dir "./metadata"` for canonical metadata trees.
Use `asc migrate validate --fastlane-dir "./fastlane"` for legacy fastlane-format metadata.

## Notes
- Version localizations and app info localizations are different; use the right command and `--type` flag.
- Use `asc localizations list` to confirm available locales and IDs.
- Privacy Policy URL is in app info localizations, not version localizations.
```

## File: `skills/asc-notarization/SKILL.md`
```markdown
---
name: asc-notarization
description: Archive, export, and notarize macOS apps using xcodebuild and asc. Use when you need to prepare a macOS app for distribution outside the App Store with Developer ID signing and Apple notarization.
---

# macOS Notarization

Use this skill when you need to notarize a macOS app for distribution outside the App Store.

## Preconditions
- Xcode installed and command line tools configured.
- Auth is configured (`asc auth login` or `ASC_*` env vars).
- A Developer ID Application certificate in the local keychain.
- The app's Xcode project builds for macOS.

## Preflight: Verify Signing Identity

Before archiving, confirm a valid Developer ID Application identity exists:

```bash
security find-identity -v -p codesigning | grep "Developer ID Application"
```

If no identity is found, create one at https://developer.apple.com/account/resources/certificates/add (the App Store Connect API does not support creating Developer ID certificates).

### Fix Broken Trust Settings

If `codesign` or `xcodebuild` fails with "Invalid trust settings" or "errSecInternalComponent", the certificate may have custom trust overrides that break the chain:

```bash
# Check for custom trust settings
security dump-trust-settings 2>&1 | grep -A1 "Developer ID"

# If overrides exist, export the cert and remove them
security find-certificate -c "Developer ID Application" -p ~/Library/Keychains/login.keychain-db > /tmp/devid-cert.pem
security remove-trusted-cert /tmp/devid-cert.pem
```

### Verify Certificate Chain

After fixing trust settings, verify the chain is intact:

```bash
codesign --deep --force --options runtime --sign "Developer ID Application: YOUR NAME (TEAM_ID)" /path/to/any.app 2>&1
```

The signing must show the chain: Developer ID Application → Developer ID Certification Authority → Apple Root CA.

## Step 1: Archive

```bash
xcodebuild archive \
  -scheme "YourMacScheme" \
  -configuration Release \
  -archivePath /tmp/YourApp.xcarchive \
  -destination "generic/platform=macOS"
```

## Step 2: Export with Developer ID

Create an ExportOptions plist for Developer ID distribution:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>method</key>
    <string>developer-id</string>
    <key>signingStyle</key>
    <string>automatic</string>
    <key>teamID</key>
    <string>YOUR_TEAM_ID</string>
</dict>
</plist>
```

Export the archive:

```bash
xcodebuild -exportArchive \
  -archivePath /tmp/YourApp.xcarchive \
  -exportPath /tmp/YourAppExport \
  -exportOptionsPlist ExportOptions.plist
```

This produces a `.app` bundle signed with Developer ID Application and a secure timestamp.

### Verify the Export

```bash
codesign -dvvv "/tmp/YourAppExport/YourApp.app" 2>&1 | grep -E "Authority|Timestamp"
```

Confirm:
- Authority chain starts with "Developer ID Application"
- A Timestamp is present

## Step 3: Create a ZIP for Notarization

```bash
ditto -c -k --keepParent "/tmp/YourAppExport/YourApp.app" "/tmp/YourAppExport/YourApp.zip"
```

## Step 4: Submit for Notarization

### Fire-and-forget
```bash
asc notarization submit --file "/tmp/YourAppExport/YourApp.zip"
```

### Wait for result
```bash
asc notarization submit --file "/tmp/YourAppExport/YourApp.zip" --wait
```

### Custom polling
```bash
asc notarization submit --file "/tmp/YourAppExport/YourApp.zip" --wait --poll-interval 30s --timeout 1h
```

## Step 5: Check Results

### Status
```bash
asc notarization status --id "SUBMISSION_ID" --output table
```

### Developer Log (for failures)
```bash
asc notarization log --id "SUBMISSION_ID"
```

Fetch the log URL to see detailed issues:
```bash
curl -sL "LOG_URL" | python3 -m json.tool
```

### List Previous Submissions
```bash
asc notarization list --output table
asc notarization list --limit 5 --output table
```

## Step 6: Staple (Optional)

After notarization succeeds, staple the ticket so the app works offline:

```bash
xcrun stapler staple "/tmp/YourAppExport/YourApp.app"
```

For DMG or PKG distribution, staple after creating the container:
```bash
# Create DMG
hdiutil create -volname "YourApp" -srcfolder "/tmp/YourAppExport/YourApp.app" -ov -format UDZO "/tmp/YourApp.dmg"
xcrun stapler staple "/tmp/YourApp.dmg"
```

## Supported File Formats

| Format | Use Case |
|--------|----------|
| `.zip`  | Simplest; zip a signed `.app` bundle |
| `.dmg`  | Disk image for drag-and-drop install |
| `.pkg`  | Installer package (requires Developer ID Installer certificate) |

## PKG Notarization

To notarize `.pkg` files, you need a **Developer ID Installer** certificate (separate from Developer ID Application). This certificate type is not available through the App Store Connect API — create it at https://developer.apple.com/account/resources/certificates/add.

Sign the package:
```bash
productsign --sign "Developer ID Installer: YOUR NAME (TEAM_ID)" unsigned.pkg signed.pkg
```

Then submit:
```bash
asc notarization submit --file signed.pkg --wait
```

## Troubleshooting

### "Invalid trust settings" during export
The Developer ID certificate has custom trust overrides. See the Preflight section above to remove them.

### "The binary is not signed with a valid Developer ID certificate"
The app was signed with a Development or App Store certificate. Re-export with `method: developer-id` in ExportOptions.plist.

### "The signature does not include a secure timestamp"
Add `--timestamp` to manual `codesign` calls, or use `xcodebuild -exportArchive` which adds timestamps automatically.

### Upload timeout for large files
Set a longer upload timeout:
```bash
ASC_UPLOAD_TIMEOUT=5m asc notarization submit --file ./LargeApp.zip --wait
```

### Notarization returns "Invalid" but signing looks correct
Fetch the developer log for specific issues:
```bash
asc notarization log --id "SUBMISSION_ID"
```

Common causes: unsigned nested binaries, missing hardened runtime, embedded libraries without timestamps.

## Notes
- The `asc notarization` commands use the Apple Notary API v2, not `xcrun notarytool`.
- Authentication uses the same API key as other `asc` commands.
- Files are uploaded directly to Apple's S3 bucket with streaming (no full-file buffering).
- Files over 5 GB use multipart upload automatically.
- Always use `--help` to verify flags: `asc notarization submit --help`.
```

## File: `skills/asc-ppp-pricing/SKILL.md`
```markdown
---
name: asc-ppp-pricing
description: Set territory-specific pricing for subscriptions and in-app purchases using current asc setup, pricing summary, price import, and price schedule commands. Use when adjusting prices by country or implementing localized PPP strategies.
---

# PPP pricing (per-territory pricing)

Use this skill to create or update localized pricing across territories based on purchasing power parity (PPP) or your own regional pricing strategy.

Prefer the current high-level flows:
- `asc subscriptions setup` and `asc iap setup` when you are creating a new product
- `asc subscriptions pricing ...` for subscription pricing changes
- `asc iap pricing summary` and `asc iap pricing schedules ...` for IAP pricing changes

## Preconditions
- Ensure credentials are set (`asc auth login` or `ASC_*` env vars).
- Prefer `ASC_APP_ID` or pass `--app` explicitly.
- Decide your base territory (usually `USA`) and baseline price.
- Use `asc pricing territories list --paginate` if you need supported territory IDs.

## Subscription PPP workflow

### New subscription: bootstrap with `setup`
Use `setup` when you are creating a new subscription and want to create the group, subscription, first localization, initial price, and availability in one verified flow.

```bash
asc subscriptions setup \
  --app "APP_ID" \
  --group-reference-name "Pro" \
  --reference-name "Pro Monthly" \
  --product-id "com.example.pro.monthly" \
  --subscription-period ONE_MONTH \
  --locale "en-US" \
  --display-name "Pro Monthly" \
  --description "Unlock everything" \
  --price "9.99" \
  --price-territory "USA" \
  --territories "USA,CAN,GBR" \
  --output json
```

Notes:
- `setup` verifies the created state by default.
- Use `--no-verify` only when you explicitly want speed over readback verification.
- Use `--tier` or `--price-point-id` instead of `--price` when your workflow is tier-driven.

### Inspect current subscription pricing before changes
Use the summary view first when you want a compact current-state snapshot.

```bash
asc subscriptions pricing summary --subscription-id "SUB_ID" --territory "USA"
asc subscriptions pricing summary --subscription-id "SUB_ID" --territory "IND"
asc subscriptions pricing prices list --subscription-id "SUB_ID" --paginate
```

Use `summary` for quick before/after spot checks and `prices list` when you need raw price records.

### Preferred bulk PPP update: import a CSV with dry run
For broad PPP rollouts, prefer the subscription pricing import command instead of manually adding territory prices one by one.

Example CSV:

```csv
territory,price,start_date,preserved
IND,2.99,2026-04-01,false
BRA,4.99,2026-04-01,false
MEX,4.99,2026-04-01,false
DEU,8.99,2026-04-01,false
```

Dry-run first:

```bash
asc subscriptions pricing prices import \
  --subscription-id "SUB_ID" \
  --input "./ppp-prices.csv" \
  --dry-run \
  --output table
```

Apply for real:

```bash
asc subscriptions pricing prices import \
  --subscription-id "SUB_ID" \
  --input "./ppp-prices.csv" \
  --output table
```

Notes:
- `--dry-run` validates rows and resolves price points without creating prices.
- `--continue-on-error=false` gives you a fail-fast mode.
- CSV required columns: `territory`, `price`
- CSV optional columns: `currency_code`, `start_date`, `preserved`, `preserve_current_price`, `price_point_id`
- When `price_point_id` is omitted, the CLI resolves the matching price point for the row's territory and price automatically.
- Territory inputs in import can be 3-letter IDs, 2-letter codes, or common territory names that map cleanly.

### One-off subscription territory changes
For a small number of manual overrides, use the canonical `set` command.

```bash
asc subscriptions pricing prices set --subscription-id "SUB_ID" --price "2.99" --territory "IND"
asc subscriptions pricing prices set --subscription-id "SUB_ID" --tier 5 --territory "BRA"
asc subscriptions pricing prices set --subscription-id "SUB_ID" --price-point "PRICE_POINT_ID" --territory "DEU"
```

Notes:
- Add `--start-date "YYYY-MM-DD"` to schedule a future change.
- Add `--preserved` when you want to preserve the current price relationship.
- The command handles both initial pricing and later price changes.

### Discover raw price points only when you need them
Use price-point lookup and equalizations when you want to inspect Apple's localized ladder directly or pin exact price point IDs.

```bash
asc subscriptions pricing price-points list --subscription-id "SUB_ID" --territory "USA" --paginate --price "9.99"
asc subscriptions pricing price-points equalizations --price-point-id "PRICE_POINT_ID" --paginate
```

### Verify after apply
Re-run the summary and raw list views after changes.

```bash
asc subscriptions pricing summary --subscription-id "SUB_ID" --territory "IND"
asc subscriptions pricing summary --subscription-id "SUB_ID" --territory "BRA"
asc subscriptions pricing prices list --subscription-id "SUB_ID" --paginate
```

If the subscription was newly created, you can also use `asc subscriptions setup` with verification enabled instead of stitching together separate create and pricing steps.

### Subscription availability
If you need to explicitly enable territories for an existing subscription, use the pricing availability family.

```bash
asc subscriptions pricing availability edit --subscription-id "SUB_ID" --territories "USA,CAN,IND,BRA"
asc subscriptions pricing availability view --subscription-id "SUB_ID"
```

## IAP PPP workflow

### New IAP: bootstrap with `setup`
Use `setup` when you are creating a new IAP and want to create the product, first localization, and initial price schedule in one verified flow.

```bash
asc iap setup \
  --app "APP_ID" \
  --type NON_CONSUMABLE \
  --reference-name "Pro Lifetime" \
  --product-id "com.example.pro.lifetime" \
  --locale "en-US" \
  --display-name "Pro Lifetime" \
  --description "Unlock everything forever" \
  --price "9.99" \
  --base-territory "USA" \
  --output json
```

Notes:
- `setup` verifies the created IAP, localization, and price schedule by default.
- Use `--start-date` for scheduled pricing.
- Use `--tier` or `--price-point-id` when you want deterministic tier- or ID-based setup.

### Inspect current IAP pricing before changes
Use `asc iap pricing summary` as the main current-state summary for PPP work.

```bash
asc iap pricing summary --iap-id "IAP_ID" --territory "USA"
asc iap pricing summary --iap-id "IAP_ID" --territory "IND"
```

This returns the base territory, current price, estimated proceeds, and scheduled changes for the requested territory.

### Discover candidate IAP price points
Use price-point lookup when you want to inspect or pin exact price point IDs.

```bash
asc iap pricing price-points list --iap-id "IAP_ID" --territory "USA" --paginate --price "9.99"
asc iap pricing price-points equalizations --id "PRICE_POINT_ID"
```

### Create or update an IAP price schedule
For manual PPP updates, create a price schedule directly.

```bash
asc iap pricing schedules create --iap-id "IAP_ID" --base-territory "USA" --price "4.99" --start-date "2026-04-01"
asc iap pricing schedules create --iap-id "IAP_ID" --base-territory "USA" --tier 5 --start-date "2026-04-01"
asc iap pricing schedules create --iap-id "IAP_ID" --base-territory "USA" --prices "PRICE_POINT_ID:2026-04-01"
```

Use these when you are intentionally creating or replacing schedule entries. For deeper inspection:

```bash
asc iap pricing schedules view --iap-id "IAP_ID"
asc iap pricing schedules manual-prices --schedule-id "SCHEDULE_ID" --paginate
asc iap pricing schedules automatic-prices --schedule-id "SCHEDULE_ID" --paginate
```

### Verify after apply
Use the summary command again after scheduling or applying pricing changes.

```bash
asc iap pricing summary --iap-id "IAP_ID" --territory "USA"
asc iap pricing summary --iap-id "IAP_ID" --territory "IND"
```

For future-dated schedules, expect scheduled changes rather than an immediately updated current price.

## Common PPP strategy patterns

### Base territory first
- Pick one baseline territory, usually `USA`.
- Set the baseline price there first.
- Derive lower or higher territory targets from that baseline.

### Tiered regional pricing
- High-income markets stay close to baseline.
- Mid-income markets get moderate discounts.
- Lower-income markets get stronger PPP adjustments.

### Spreadsheet-driven rollout
- Build the target territory list in a CSV.
- Dry-run the import.
- Fix any resolution failures.
- Apply the import.
- Re-run summary checks for the most important territories.

## Notes
- Prefer canonical commands in docs and automation: `asc subscriptions pricing ...`
- Older `asc subscriptions prices ...` paths still exist, but the canonical pricing family is clearer.
- Prefer canonical IAP commands in docs and automation: `asc iap pricing ...`
- `asc subscriptions pricing prices import --dry-run` is the safest subscription batch PPP path today.
- `asc subscriptions setup` and `asc iap setup` already provide built-in post-create verification.
- There is not yet a single first-class before/after PPP diff command; use the current summary commands before and after apply.
- Price changes may take time to propagate in App Store Connect and storefronts.
```

## File: `skills/asc-release-flow/SKILL.md`
```markdown
---
name: asc-release-flow
description: Determine whether an app is ready to submit, then drive the App Store release flow with asc, including first-time submission fixes for availability, in-app purchases, subscriptions, Game Center, and App Privacy.
---

# Release flow (readiness-first)

Use this skill when the real question is "Can my app be ready to submit?" and then guide the user through the shortest path to a clean App Store submission, especially for first-time releases.

## Preconditions
- Ensure credentials are set (`asc auth login` or `ASC_*` env vars).
- Resolve app ID, version string, and build ID up front.
- For lower-level or first-time flows, also be ready to resolve `VERSION_ID`, `SUBMISSION_ID`, `DETAIL_ID`, `GROUP_ID`, `SUB_ID`, `IAP_ID`, and related resource IDs. Use `asc-id-resolver` when needed.
- Have a metadata directory ready if you plan to use `asc release stage` or `asc release run`.
- If you use experimental web-session commands, use a user-owned Apple Account session and treat those commands as optional escape hatches, not the default path.

## How to answer
When using this skill, answer readiness questions in this order:
1. Is the app ready right now, or not yet?
2. What are the blocking issues?
3. Which blockers are API-fixable vs web-session-fixable?
4. What exact command should run next?

Group blockers like this:
- API-fixable: build validity, metadata, screenshots, review details, content rights, encryption, version/build attachment, IAP readiness, Game Center version and review-submission setup.
- Web-session-fixable: initial app availability bootstrap, first-review subscription attachment, App Privacy publish state.
- Manual fallback: first-time IAP selection from the app-version screen when no CLI attach flow exists, or any flow the user does not want to run through experimental web-session commands.

## Canonical path

### 1. Fast readiness check
Run this first when the user wants the quickest answer to "can I submit now?":

```bash
asc submit preflight --app "APP_ID" --version "1.2.3" --platform IOS
```

This is the fastest high-signal readiness check and prints fix guidance without mutating anything.

### 2. Real staging pass without submit
Run this when the user wants the version prepared in App Store Connect but wants a manual checkpoint before creating a review submission:

```bash
asc release stage \
  --app "APP_ID" \
  --version "1.2.3" \
  --build "BUILD_ID" \
  --metadata-dir "./metadata/version/1.2.3" \
  --confirm
```

Use `--copy-metadata-from "1.2.2"` instead of `--metadata-dir` when you want to carry metadata forward from an existing version. `asc release stage` requires exactly one metadata source and stops before submit.

### 3. Full-pipeline dry run
Run this when the user wants one command that approximates the whole release path:

```bash
asc release run \
  --app "APP_ID" \
  --version "1.2.3" \
  --build "BUILD_ID" \
  --metadata-dir "./metadata/version/1.2.3" \
  --dry-run \
  --output table
```

This is the best single-command rehearsal for:
1. ensuring or creating the version
2. applying metadata and localizations
3. attaching the build
4. running readiness checks
5. confirming the submission path is coherent

Add `--strict-validate` when you want warnings treated as blockers.

### 4. Deep API readiness audit
Run this when the user needs a fuller version-level checklist than `submit preflight`:

```bash
asc validate --app "APP_ID" --version "1.2.3" --platform IOS --output table
```

Prefer the version string form here so it stays aligned with `asc submit preflight` and `asc release run`. Switch to `VERSION_ID` only for lower-level commands that explicitly require it.

If the app sells digital goods, also run:

```bash
asc validate iap --app "APP_ID" --output table
asc validate subscriptions --app "APP_ID" --output table
```

In current asc, `asc validate subscriptions` expands `MISSING_METADATA` into per-subscription diagnostics. Use it to pinpoint missing review screenshots, promotional images, pricing or availability coverage, offer readiness, and app/build evidence before you retry submission or `attach-group`.

When territory coverage is wrong, the newest diagnostics name the exact missing territories instead of only reporting count mismatches. Use `--output json --pretty` when you want machine-readable diagnostics.

### 5. Actual submit
When the dry run looks clean:

```bash
asc release run \
  --app "APP_ID" \
  --version "1.2.3" \
  --build "BUILD_ID" \
  --metadata-dir "./metadata/version/1.2.3" \
  --confirm
```

## First-time submission blockers

### 1. Initial app availability does not exist yet
Symptoms:
- `asc pricing availability view --app "APP_ID"` reports no availability
- `asc pricing availability edit ...` fails because it only updates existing availability

Check:

```bash
asc pricing availability view --app "APP_ID"
```

Bootstrap the first availability record with the experimental web-session flow:

```bash
asc web apps availability create \
  --app "APP_ID" \
  --territory "USA,GBR" \
  --available-in-new-territories true
```

After bootstrap, use the normal public API command for ongoing updates:

```bash
asc pricing availability edit \
  --app "APP_ID" \
  --territory "USA,GBR" \
  --available true \
  --available-in-new-territories true
```

### 2. Subscriptions are READY_TO_SUBMIT but not attached to first review
For apps with subscriptions, check readiness explicitly:

```bash
asc validate subscriptions --app "APP_ID" --output table
```

If the validator shows `MISSING_METADATA`, read the row-level diagnostics literally. The newest CLI surfaces missing promotional images, review screenshots, pricing or availability coverage, offer readiness, and app/build evidence in one matrix, which is the quickest way to understand why first-review attach still fails.

List current first-review subscription state:

```bash
asc web review subscriptions list --app "APP_ID"
```

If the app is going through its first review and the group needs attaching:

```bash
asc web review subscriptions attach-group \
  --app "APP_ID" \
  --group-id "GROUP_ID" \
  --confirm
```

If `attach-group` still returns `MISSING_METADATA`, fix the validator-reported prerequisites first. The most common misses are broad pricing coverage and a subscription promotional image.

For one subscription instead of a whole group:

```bash
asc web review subscriptions attach \
  --app "APP_ID" \
  --subscription-id "SUB_ID" \
  --confirm
```

For later reviews, use the normal submission path:

```bash
asc subscriptions review submit --subscription-id "SUB_ID" --confirm
```

If review artifacts are missing, upload them before submission:

```bash
asc subscriptions review screenshots create --subscription-id "SUB_ID" --file "./screenshot.png"
asc subscriptions images create --subscription-id "SUB_ID" --file "./image.png"
```

Also make sure the app’s privacy policy URL is populated when the app sells subscriptions.

### 3. In-App Purchases need review readiness or first-version inclusion
For apps with one-time purchases, consumables, or non-consumables, check readiness explicitly:

```bash
asc validate iap --app "APP_ID" --output table
```

If the IAP is missing its App Review screenshot:

```bash
asc iap review-screenshots create --iap-id "IAP_ID" --file "./review.png"
```

For IAPs on a published app, submit them directly:

```bash
asc iap submit --iap-id "IAP_ID" --confirm
```

If this is the first IAP for the app, or the first time adding a new IAP type, Apple requires it to be included with a new app version. Current `asc` commands can validate and submit published-app IAPs, but there is no equivalent first-review attach flow like the subscription web commands yet. In that case:
- prepare the IAP with `asc validate iap`, pricing, localization, and review screenshot data first
- then select the IAP from the app version’s “In-App Purchases and Subscriptions” section in App Store Connect before submitting the app version

Also make sure the app’s privacy policy URL is populated when the app sells IAPs.

### 4. Game Center is enabled but the app version or review submission is incomplete
If the app uses Game Center, make sure the App Store version is Game Center-enabled:

```bash
asc game-center app-versions list --app "APP_ID"
asc game-center app-versions create --app-store-version-id "VERSION_ID"
```

If you are adding Game Center components for the first time, include them in the same submission as the app version. Resolve component version IDs first:

```bash
asc game-center achievements v2 versions list --achievement-id "ACH_ID"
asc game-center leaderboards v2 versions list --leaderboard-id "LEADERBOARD_ID"
asc game-center challenges versions list --challenge-id "CHALLENGE_ID"
asc game-center activities versions list --activity-id "ACTIVITY_ID"
```

Then use the review-submission flow so you can add the app version and the Game Center component versions to the same submission:

```bash
asc review submissions-create --app "APP_ID" --platform IOS
asc review items-add --submission "SUBMISSION_ID" --item-type appStoreVersions --item-id "VERSION_ID"
asc review items-add --submission "SUBMISSION_ID" --item-type gameCenterLeaderboardVersions --item-id "GC_LEADERBOARD_VERSION_ID"
asc review submissions-submit --id "SUBMISSION_ID" --confirm
```

`asc review items-add` also supports `gameCenterAchievementVersions`, `gameCenterActivityVersions`, `gameCenterChallengeVersions`, and `gameCenterLeaderboardSetVersions`.

If Game Center component versions need to ship with the app version, prefer the explicit `asc review submissions-*` flow over `asc release run --confirm`, because you need a chance to add all submission items before final submit.

### 5. App Privacy is still unpublished
The public API can warn about App Privacy readiness but cannot fully verify publish state.

If `asc submit preflight`, `asc validate`, or `asc release run` surfaces an App Privacy advisory, reconcile it with:

```bash
asc web privacy pull --app "APP_ID" --out "./privacy.json"
asc web privacy plan --app "APP_ID" --file "./privacy.json"
asc web privacy apply --app "APP_ID" --file "./privacy.json"
asc web privacy publish --app "APP_ID" --confirm
```

If the user does not want the experimental web-session flow, confirm App Privacy manually in App Store Connect:

```text
https://appstoreconnect.apple.com/apps/APP_ID/appPrivacy
```

### 6. Review details are incomplete
Check whether the version already has review details:

```bash
asc review details-for-version --version-id "VERSION_ID"
```

If needed, create or update them:

```bash
asc review details-create \
  --version-id "VERSION_ID" \
  --contact-first-name "Dev" \
  --contact-last-name "Support" \
  --contact-email "dev@example.com" \
  --contact-phone "+1 555 0100" \
  --notes "Explain the reviewer access path here."
```

```bash
asc review details-update \
  --id "DETAIL_ID" \
  --notes "Updated reviewer instructions."
```

Only set `--demo-account-required=true` when App Review truly needs demo credentials.

## Practical readiness checklist
An app is effectively ready to submit when:
- `asc submit preflight --app "APP_ID" --version "VERSION"` reports no blocking issues
- `asc validate --app "APP_ID" --version "VERSION"` is clean or only contains understood non-blocking warnings
- `asc release stage --confirm` successfully prepared the target version when you want a real pre-submit checkpoint
- `asc release run ... --dry-run` produces the expected plan
- the build is `VALID` and attached to the target version
- metadata, screenshots, and localizations are complete
- content rights and encryption requirements are resolved
- review details are present
- app availability exists
- if the app has IAPs or subscriptions, the privacy policy URL is present
- if the app has IAPs, they have localization/pricing/review screenshots and first-time IAPs are selected with the app version
- subscriptions, if any, are attached for first review or already submitted through the supported review path
- if the app uses Game Center, the app version is Game Center-enabled and any required Game Center component versions are in the same review submission
- any App Privacy advisory has been resolved through `asc web privacy ...` or manual confirmation

## Lower-level fallback
Use the lower-level flow only when the user needs explicit control over each step:

```bash
asc versions attach-build --version-id "VERSION_ID" --build "BUILD_ID"
asc submit preflight --app "APP_ID" --version "1.2.3" --platform IOS
asc submit create --app "APP_ID" --version "1.2.3" --build "BUILD_ID" --confirm
asc submit status --version-id "VERSION_ID"
# or, if you captured the review submission ID:
asc submit status --id "SUBMISSION_ID"
```

If the submission needs multiple review items, such as Game Center component versions, use the review-submission API directly instead:

```bash
asc review submissions-create --app "APP_ID" --platform IOS
asc review items-add --submission "SUBMISSION_ID" --item-type appStoreVersions --item-id "VERSION_ID"
asc review items-add --submission "SUBMISSION_ID" --item-type gameCenterChallengeVersions --item-id "GC_CHALLENGE_VERSION_ID"
asc review submissions-submit --id "SUBMISSION_ID" --confirm
```

## Platform notes
- Use `--platform MAC_OS`, `TV_OS`, or `VISION_OS` as needed.
- For macOS, upload the `.pkg` separately, then use the same readiness and submission flow.
- `asc publish testflight` is still the fastest TestFlight shortcut, but for App Store readiness prefer `asc submit preflight`, `asc release stage`, and `asc release run`.

## Notes
- `asc release stage --confirm` is the safest one-command way to prepare a version without submitting it.
- `asc release run --dry-run` is the closest thing to a one-command answer for "will this full release flow work?"
- `asc submit preflight` is the fastest first pass.
- `asc validate` is the deeper API-side checklist for version readiness.
- `asc validate subscriptions` now exposes much richer per-subscription diagnostics for `MISSING_METADATA` readiness failures.
- Web-session commands are experimental and should be presented as optional escape hatches when the public API cannot complete the first-time flow.
- First-time app-availability bootstrap now goes through the experimental `asc web apps availability create` flow or App Store Connect itself.
- First-review subscriptions have a concrete CLI attach path; first-review IAP selection still may require the App Store Connect version UI.
- Game Center can require explicit review-submission item management when components must ride with the app version.
- If the user asks "why did submission fail?" map the failure back into the three buckets above: API-fixable, web-session-fixable, or manual fallback.
```

## File: `skills/asc-revenuecat-catalog-sync/SKILL.md`
```markdown
---
name: asc-revenuecat-catalog-sync
description: Reconcile App Store Connect subscriptions and in-app purchases with RevenueCat products, entitlements, offerings, and packages using asc and RevenueCat MCP. Use when setting up or syncing subscription catalogs across ASC and RevenueCat.
---

# asc RevenueCat catalog sync

Use this skill to keep App Store Connect (ASC) and RevenueCat aligned, including creating missing ASC items and mapping them to RevenueCat resources.

## When to use
- You want to bootstrap RevenueCat from an existing ASC catalog.
- You want to create missing ASC subscriptions/IAPs, then map them into RevenueCat.
- You need a drift audit before release.
- You want deterministic product mapping based on identifiers.

## Preconditions
- `asc` authentication is configured (`asc auth login` or `ASC_*` env vars).
- RevenueCat MCP server is configured and authenticated.
- In Cursor and VS Code, OAuth auth is available for RevenueCat MCP. API key auth is also supported.
- You know:
  - ASC app ID (`APP_ID`)
  - RevenueCat `project_id`
  - target RevenueCat app type (`app_store` or `mac_app_store`) and bundle ID for create flows
- Use a write-enabled RevenueCat API v2 key when applying changes.

## Safety defaults
- Start in **audit mode** (read-only).
- Require explicit confirmation before writes.
- Never delete resources in this workflow.
- Continue on per-item failures and report all failures at the end.

## Canonical identifiers
- Primary cross-system key: ASC `productId` == RevenueCat `store_identifier`.
- Keep `productId` stable once products are live.
- Do not use display names as unique identifiers.

## Scope boundary
- RevenueCat MCP configures RevenueCat resources; it does not create App Store Connect products directly.
- Use `asc` commands to create missing ASC subscription groups, subscriptions, and IAPs before RevenueCat mapping.

## Modes

### 1) Audit mode (default)
1. Read ASC source catalog.
2. Read RevenueCat target catalog.
3. Build a diff with actions:
   - missing in ASC
   - missing in RevenueCat
   - mapping conflicts (identifier/type/app mismatch)
4. Present a plan and wait for confirmation.

### 2) Apply mode (explicit)
Execute approved actions in this order:
1. Ensure ASC groups/subscriptions/IAP exist.
2. Ensure RevenueCat app/products exist.
3. Ensure entitlements and product attachments.
4. Ensure offerings/packages and package attachments.
5. Verify and print a final reconciliation summary.

## Step-by-step workflow

### Step A - Read current ASC catalog

```bash
asc subscriptions groups list --app "APP_ID" --paginate --output json
asc iap list --app "APP_ID" --paginate --output json
# for each subscription group:
asc subscriptions list --group-id "GROUP_ID" --paginate --output json
```

### Step B - Read current RevenueCat catalog (MCP)

Use these MCP tools (with `project_id` and pagination where applicable):
- `mcp_RC_get_project`
- `mcp_RC_list_apps`
- `mcp_RC_list_products`
- `mcp_RC_list_entitlements`
- `mcp_RC_list_offerings`
- `mcp_RC_list_packages`

### Step C - Build mapping plan

Map ASC product types to RevenueCat product types:
- ASC subscription -> RevenueCat `subscription`
- ASC IAP `CONSUMABLE` -> RevenueCat `consumable`
- ASC IAP `NON_CONSUMABLE` -> RevenueCat `non_consumable`
- ASC IAP `NON_RENEWING_SUBSCRIPTION` -> RevenueCat `non_renewing_subscription`

Suggested entitlement policy:
- subscriptions: one entitlement per subscription group (or explicit map provided by user)
- non-consumable IAP: one entitlement per product
- consumable IAP: no entitlement by default unless user asks

### Step D - Ensure missing ASC items (if requested)

Create missing ASC resources first, then re-read ASC to capture canonical IDs.

```bash
# create subscription group
asc subscriptions groups create --app "APP_ID" --reference-name "Premium"

# create subscription
asc subscriptions create \
  --group-id "GROUP_ID" \
  --reference-name "Monthly" \
  --product-id "com.example.premium.monthly" \
  --subscription-period ONE_MONTH

# create iap
asc iap create \
  --app "APP_ID" \
  --type NON_CONSUMABLE \
  --ref-name "Lifetime" \
  --product-id "com.example.lifetime"
```

### Step E - Ensure RevenueCat app and products

Use MCP:
- create app if missing: `mcp_RC_create_app`
- create products: `mcp_RC_create_product`
  - `store_identifier` = ASC `productId`
  - `app_id` = RevenueCat app ID
  - `type` from mapping above

### Step F - Ensure entitlements and attachments

Use MCP:
- list/create entitlements: `mcp_RC_list_entitlements`, `mcp_RC_create_entitlement`
- attach products: `mcp_RC_attach_products_to_entitlement`
- verify attachments: `mcp_RC_get_products_from_entitlement`

### Step G - Ensure offerings and packages (optional)

Use MCP:
- list/create/update offerings:
  - `mcp_RC_list_offerings`
  - `mcp_RC_create_offering`
  - `mcp_RC_update_offering` (`is_current=true` only if requested)
- list/create packages:
  - `mcp_RC_list_packages`
  - `mcp_RC_create_package`
- attach products to packages:
  - `mcp_RC_attach_products_to_package` with `eligibility_criteria: "all"`

Recommended package keys:
- `ONE_WEEK` -> `$rc_weekly`
- `ONE_MONTH` -> `$rc_monthly`
- `TWO_MONTHS` -> `$rc_two_month`
- `THREE_MONTHS` -> `$rc_three_month`
- `SIX_MONTHS` -> `$rc_six_month`
- `ONE_YEAR` -> `$rc_annual`
- lifetime IAP -> `$rc_lifetime`
- custom -> `$rc_custom_<name>`

## Expected output format

Return a final summary with:
- ASC created counts (groups/subscriptions/IAP)
- RevenueCat created counts (apps/products/entitlements/offerings/packages)
- attachment counts (entitlement-products, package-products)
- skipped existing items
- failed items with actionable errors

Example:

```text
ASC: created groups=1 subscriptions=2 iap=1, skipped=14, failed=0
RC: created apps=0 products=3 entitlements=2 offerings=1 packages=2, skipped=27, failed=1
Attachments: entitlement_products=3 package_products=2
Failures:
- com.example.premium.annual: duplicate store_identifier exists on another RC app
```

## Agent behavior
- Always run audit first, even in apply mode.
- Ask for confirmation before create/update operations.
- Match by `store_identifier` first.
- Use full pagination (`--paginate` for ASC, `starting_after` for RevenueCat tools).
- Continue processing after per-item failures and report all failures together.
- Never auto-delete ASC or RevenueCat resources in this skill.

## Common pitfalls
- Wrong RevenueCat `project_id` or app ID.
- Creating RC products under the wrong platform app.
- Accidentally assigning consumables to entitlements.
- Skipping the post-create ASC re-read step.
- Missing offering/package verification after product creation.

## Additional resources
- Workflow examples: [examples.md](examples.md)
- Source references: [references.md](references.md)
```

## File: `skills/asc-revenuecat-catalog-sync/examples.md`
```markdown
# Examples: asc RevenueCat catalog sync

Use these examples as execution templates for realistic catalog synchronization workflows.

## Example 1: Drift audit only (read-only)

Goal: compare ASC and RevenueCat, produce a no-write reconciliation report.

### User request
`Audit my ASC subscriptions and IAP catalog against RevenueCat and show what is missing on either side.`

### Expected behavior
1. Read ASC:
   - `asc subscriptions groups list --app "APP_ID" --paginate --output json`
   - `asc iap list --app "APP_ID" --paginate --output json`
   - `asc subscriptions list --group-id "GROUP_ID" --paginate --output json` (for each group)
2. Read RevenueCat via MCP:
   - list apps/products/entitlements/offerings/packages for `project_id`
3. Build and present a diff:
   - missing in ASC
   - missing in RevenueCat
   - type mismatch
   - app/platform mismatch
4. Stop for confirmation (no writes).

## Example 2: Create missing ASC subscriptions, then map to RevenueCat

Goal: bootstrap both systems when store products are partially missing.

### User request
`Ensure monthly and annual subscriptions exist in ASC for app APP_ID, then sync them to RevenueCat project PROJECT_ID under my iOS app.`

### Expected behavior
1. Audit existing resources first.
2. If missing in ASC:
   - create group:
     - `asc subscriptions groups create --app "APP_ID" --reference-name "Premium"`
   - create subscriptions:
     - `asc subscriptions create --group-id "GROUP_ID" --reference-name "Monthly" --product-id "com.example.premium.monthly" --subscription-period ONE_MONTH`
     - `asc subscriptions create --group-id "GROUP_ID" --reference-name "Annual" --product-id "com.example.premium.annual" --subscription-period ONE_YEAR`
3. Re-read ASC to capture authoritative IDs.
4. In RevenueCat:
   - create app if missing (`type: app_store`, same bundle identifier)
   - create products with matching `store_identifier`
   - create entitlement (for example `premium`) and attach products
   - optionally create `default` offering with `$rc_monthly` and `$rc_annual`
5. Verify with final summary and failures list.

## Example 3: Sync one-time IAP and keep consumables entitlement-free

Goal: model recommended entitlement behavior by product type.

### User request
`Sync my non-consumable lifetime IAP and consumable coin pack to RevenueCat.`

### Expected behavior
1. Confirm product type mapping:
   - `NON_CONSUMABLE` -> `non_consumable`
   - `CONSUMABLE` -> `consumable`
2. Create missing ASC IAPs if requested:
   - `asc iap create --app "APP_ID" --type NON_CONSUMABLE --ref-name "Lifetime" --product-id "com.example.lifetime"`
   - `asc iap create --app "APP_ID" --type CONSUMABLE --ref-name "Coins 100" --product-id "com.example.coins.100"`
3. In RevenueCat:
   - create both products
   - attach **non-consumable** product to an entitlement (for example `lifetime_access`)
   - skip entitlement attachment for consumable by default (unless user explicitly asks)
4. Return created/skipped/failed counts.

## Example 4: Controlled apply in CI-style automation

Goal: make apply mode safe and repeatable in team workflows.

### User request
`Run a full sync and apply missing resources.`

### Expected behavior
1. Run audit and print plan.
2. Request explicit approval.
3. Apply in deterministic order:
   - ASC group/subscription/IAP
   - RC app/product
   - RC entitlement + attachments
   - RC offering/package + attachments
4. Continue after item failures and aggregate errors.
5. Print machine-readable summary plus human-readable recap.

## Suggested natural-language prompts for MCP

- `List all apps in RevenueCat project PROJECT_ID and show which one matches bundle id com.example.app`
- `Create RevenueCat product com.example.premium.monthly as subscription in app APP_ID`
- `Create entitlement premium and attach product PRODUCT_ID`
- `Create offering default with packages $rc_monthly and $rc_annual`
- `Show complete offering configuration including packages and attached products`
```

## File: `skills/asc-revenuecat-catalog-sync/references.md`
```markdown
# References

These sources were used to validate command/tool assumptions and workflow boundaries.

## RevenueCat MCP docs

- MCP overview:
  - https://www.revenuecat.com/docs/tools/mcp
- Setup and authentication (OAuth/API key, cloud endpoint):
  - https://www.revenuecat.com/docs/tools/mcp/setup
- Tools reference (tool names, parameters, enums, package naming):
  - https://www.revenuecat.com/docs/tools/mcp/tools-reference
- Usage examples (natural language interaction patterns):
  - https://www.revenuecat.com/docs/tools/mcp/usage-examples
- Best practices and troubleshooting:
  - https://www.revenuecat.com/docs/tools/mcp/best-practices-and-troubleshooting

## RevenueCat product model docs

- Configuring products (products, entitlements, offerings model):
  - https://www.revenuecat.com/docs/projects/configuring-products
- iOS product setup in App Store Connect (store-side creation details):
  - https://www.revenuecat.com/docs/getting-started/entitlements/ios-products

## RevenueCat MCP launch context

- Launch post and current beta limitations:
  - https://www.revenuecat.com/blog/company/introducing-revenuecat-mcp/
```

## File: `skills/asc-screenshot-resize/SKILL.md`
```markdown
---
name: asc-screenshot-resize
description: Resize and validate App Store screenshots for all device classes using macOS sips. Use when preparing or fixing screenshots for App Store Connect submission.
---

# asc screenshot resize

Use this skill to resize screenshots to the exact pixel dimensions required by App Store Connect and validate they pass upload requirements. Uses the built-in macOS `sips` tool — no third-party dependencies needed.

## Required Dimensions

### iPhone

| Display Size | Accepted Dimensions (portrait × landscape) |
|---|---|
| 6.9" | 1260 × 2736, 2736 × 1260, 1320 × 2868, 2868 × 1320, 1290 × 2796, 2796 × 1290 |
| 6.5" | 1242 × 2688, 2688 × 1242, 1284 × 2778, 2778 × 1284 |
| 6.3" | 1206 × 2622, 2622 × 1206, 1179 × 2556, 2556 × 1179 |
| 6.1" | 1125 × 2436, 2436 × 1125, 1080 × 2340, 2340 × 1080, 1170 × 2532, 2532 × 1170 |
| 5.5" | 1242 × 2208, 2208 × 1242 |
| 4.7" | 750 × 1334, 1334 × 750 |
| 4" | 640 × 1096, 640 × 1136, 1136 × 600, 1136 × 640 |
| 3.5" | 640 × 920, 640 × 960, 960 × 600, 960 × 640 |

**Note:** 6.9" accepts screenshots from 6.5", 6.7", and 6.9" devices. 6.3" accepts from 6.1" and 6.3". 6.1" accepts from 5.4", 5.8", and 6.1".

### iPad

| Display Size | Accepted Dimensions |
|---|---|
| 13" | 2064 × 2752, 2752 × 2064, 2048 × 2732, 2732 × 2048 |
| 11" | 1668 × 2420, 2420 × 1668, 1668 × 2388, 2388 × 1668, 1640 × 2360, 2360 × 1640, 1488 × 2266, 2266 × 1488 |
| iPad Pro 2nd gen 12.9" | 2048 × 2732, 2732 × 2048 |
| 10.5" | 1668 × 2224, 2224 × 1668 |
| 9.7" | 1536 × 2008, 1536 × 2048, 2048 × 1496, 2048 × 1536, 768 × 1004, 768 × 1024, 1024 × 748, 1024 × 768 |

### Apple Watch

| Device | Dimensions |
|---|---|
| Ultra 3 (49mm) | 422 × 514, 410 × 502 |
| Series 11 (46mm) | 416 × 496 |
| Series 9 (45mm) | 396 × 484 |
| Series 6 (44mm) | 368 × 448 |
| Series 3 (42mm) | 312 × 390 |

### Mac

| Dimensions |
|---|
| 1280 × 800 |
| 1440 × 900 |
| 2560 × 1600 |
| 2880 × 1800 |

### Apple TV

| Dimensions |
|---|
| 1920 × 1080 |
| 3840 × 2160 |

## Workflow

### 1. Fix Unicode filenames

macOS screenshots often contain hidden Unicode characters (e.g., `U+202F` narrow no-break space) that cause `sips` and other tools to fail with "not a valid file". Always sanitize first:

```bash
python3 -c "
import os
for f in os.listdir('.'):
    clean = f.replace('\u202f', ' ')
    if f != clean:
        os.rename(f, clean)
        print(f'Renamed: {clean}')
"
```

### 2. Check current dimensions

```bash
sips -g pixelWidth -g pixelHeight screenshot.png
```

### 3. Validate App Store readiness

Check for alpha channel and color space issues before uploading:

```bash
sips -g hasAlpha -g space screenshot.png
```

App Store Connect rejects screenshots with alpha transparency. Remove it by round-tripping through JPEG:

```bash
sips -s format jpeg input.png --out /tmp/temp.jpg
sips -s format png /tmp/temp.jpg --out output.png
rm /tmp/temp.jpg
```

Batch-strip alpha from all PNGs in a directory:

```bash
for f in *.png; do
  if sips -g hasAlpha "$f" | grep -q "yes"; then
    sips -s format jpeg "$f" --out /tmp/temp.jpg
    sips -s format png /tmp/temp.jpg --out "$f"
    rm /tmp/temp.jpg
    echo "Stripped alpha: $f"
  fi
done
```

### 4. Resize a single screenshot

```bash
# Portrait iPhone 6.5" (1284 × 2778)
sips -z 2778 1284 input.png --out output.png
```

**Note:** `sips -z` takes height first, then width: `sips -z <height> <width>`.

### 5. Batch resize all screenshots in a directory

```bash
mkdir -p resized
for f in *.png; do
  sips -z 2778 1284 "$f" --out "resized/$f"
done
```

### 6. Generate multiple device sizes from one source

```bash
mkdir -p appstore-screenshots
# iPhone
sips -z 2868 1320 input.png --out appstore-screenshots/iphone-6.9.png
sips -z 2778 1284 input.png --out appstore-screenshots/iphone-6.5.png
sips -z 2622 1206 input.png --out appstore-screenshots/iphone-6.3.png
sips -z 2532 1170 input.png --out appstore-screenshots/iphone-6.1.png
sips -z 2208 1242 input.png --out appstore-screenshots/iphone-5.5.png
```

### 7. Verify output

```bash
sips -g pixelWidth -g pixelHeight -g hasAlpha resized/*.png
```

Confirm all files show the target dimensions and `hasAlpha: no`.

## Guardrails

- `sips` stretches images to fit exact dimensions. For best results, use source screenshots captured at or near the target aspect ratio.
- Always output to a separate file or directory (`--out`) to preserve originals.
- App Store Connect requires PNG or JPEG format. `sips` preserves the input format by default.
- Screenshots **must not** include alpha transparency. Always validate with `sips -g hasAlpha` before upload.
- Color space must be sRGB. If screenshots use Display P3, convert with: `sips -m "/System/Library/ColorSync/Profiles/sRGB IEC61966-2.1.icc" input.png --out output.png`.
```

## File: `skills/asc-shots-pipeline/SKILL.md`
```markdown
---
name: asc-shots-pipeline
description: Orchestrate iOS screenshot automation with xcodebuild/simctl for build-run, AXe for UI actions, JSON settings and plan files, Koubou-based framing (`asc screenshots frame`), and screenshot upload (`asc screenshots upload`). Use when users ask for automated screenshot capture, AXe-driven simulator flows, frame composition, or screenshot-to-upload pipelines.
---

# asc screenshots pipeline (xcodebuild -> AXe -> frame -> asc)

Use this skill for agent-driven screenshot workflows where the app is built and launched with Xcode CLI tools, UI is driven with AXe, and screenshots are uploaded with `asc`.

## Current scope
- Implemented now: build/run, AXe plan capture, frame composition, and upload.
- Device discovery is built-in via `asc screenshots list-frame-devices`.
- Local screenshot automation commands are experimental in asc cli.
- Framing is pinned to Koubou `0.18.1` for deterministic output.
- Feedback/issues: https://github.com/rudrankriyam/App-Store-Connect-CLI/issues/new/choose

## Defaults
- Settings file: `.asc/shots.settings.json`
- Capture plan: `.asc/screenshots.json`
- Raw screenshots dir: `./screenshots/raw`
- Framed screenshots dir: `./screenshots/framed`
- Default frame device: `iphone-air`

## 1) Create settings JSON first

Create or update `.asc/shots.settings.json`:

```json
{
  "version": 1,
  "app": {
    "bundle_id": "com.example.app",
    "project": "MyApp.xcodeproj",
    "scheme": "MyApp",
    "simulator_udid": "booted"
  },
  "paths": {
    "plan": ".asc/screenshots.json",
    "raw_dir": "./screenshots/raw",
    "framed_dir": "./screenshots/framed"
  },
  "pipeline": {
    "frame_enabled": true,
    "upload_enabled": false
  },
  "upload": {
    "version_localization_id": "",
    "device_type": "IPHONE_65",
    "source_dir": "./screenshots/framed"
  }
}
```

If you intentionally skip framing, set:
- `"frame_enabled": false`
- `"upload.source_dir": "./screenshots/raw"`

## 2) Build and run app on simulator

Use Xcode CLI for build/install/launch:

```bash
xcrun simctl boot "$UDID" || true

xcodebuild \
  -project "MyApp.xcodeproj" \
  -scheme "MyApp" \
  -configuration Debug \
  -destination "platform=iOS Simulator,id=$UDID" \
  -derivedDataPath ".build/DerivedData" \
  build

xcrun simctl install "$UDID" ".build/DerivedData/Build/Products/Debug-iphonesimulator/MyApp.app"
xcrun simctl launch "$UDID" "com.example.app"
```

Use `xcodebuild -showBuildSettings` if the app bundle path differs from the default location.

## 3) Capture screenshots with AXe (or `asc screenshots run`)

Prefer plan-driven capture:

```bash
asc screenshots run --plan ".asc/screenshots.json" --udid "$UDID" --output json
```

Useful AXe primitives during plan authoring:

```bash
axe describe-ui --udid "$UDID"
axe tap --id "search_field" --udid "$UDID"
axe type "wwdc" --udid "$UDID"
axe screenshot --output "./screenshots/raw/home.png" --udid "$UDID"
```

Minimal `.asc/screenshots.json` example:

```json
{
  "version": 1,
  "app": {
    "bundle_id": "com.example.app",
    "udid": "booted",
    "output_dir": "./screenshots/raw"
  },
  "steps": [
    { "action": "launch" },
    { "action": "wait", "duration_ms": 800 },
    { "action": "screenshot", "name": "home" }
  ]
}
```

## 4) Frame screenshots with `asc screenshots frame`

asc cli pins framing to Koubou `0.18.1`.
Install and verify before running framing steps:

```bash
pip install koubou==0.18.1
kou --version  # expect 0.18.1
# If Koubou reports missing device frames, run once with network access:
kou setup-frames
```

List supported frame device values first:

```bash
asc screenshots list-frame-devices --output json
```

Frame one screenshot (defaults to `iphone-air`):

```bash
asc screenshots frame \
  --input "./screenshots/raw/home.png" \
  --output-dir "./screenshots/framed" \
  --device "iphone-air" \
  --output json
```

Supported `--device` values:
- `iphone-air` (default)
- `iphone-17-pro`
- `iphone-17-pro-max`
- `iphone-16e`
- `iphone-17`
- `mac`

## 5) Upload screenshots with asc

Generate and review artifacts before upload:

```bash
asc screenshots review-generate --framed-dir "./screenshots/framed" --output-dir "./screenshots/review"
asc screenshots review-open --output-dir "./screenshots/review"
asc screenshots review-approve --all-ready --output-dir "./screenshots/review"
```

Upload from the configured source directory (default `./screenshots/framed` when framing is enabled):

```bash
asc screenshots upload \
  --version-localization "LOC_ID" \
  --path "./screenshots/framed" \
  --device-type "IPHONE_65" \
  --output json
```

List or validate before upload when needed:

```bash
asc screenshots sizes --output table
asc screenshots list --version-localization "LOC_ID" --output table
```

## Agent behavior
- Always confirm exact flags with `--help` before running commands.
- Re-check command paths with `asc screenshots --help` because screenshot commands are evolving quickly.
- Keep outputs deterministic: default to JSON for machine steps.
- Prefer `asc screenshots list-frame-devices --output json` before selecting a frame device.
- Ensure screenshot files exist before upload.
- Use explicit long flags (`--app`, `--output`, `--version-localization`, etc.).
- Treat screenshot-local automation as experimental and call it out in user-facing handoff notes.
- If framing fails with a version error, re-install pinned Koubou: `pip install koubou==0.18.1`.
- If framing fails because device frames are missing, run `kou setup-frames` once with network access.

## 6) Multi-locale capture (optional)

Do not use `xcrun simctl launch ... -e AppleLanguages` for localization.
`-e` is an environment variable pattern and does not reliably switch app language.

For this pipeline, use simulator-wide locale defaults per UDID. This works with
`asc screenshots capture`, which relaunches the app internally.

```bash
# Map each locale to a dedicated simulator UDID.
# (Create these simulators once with `xcrun simctl create`.)
declare -A LOCALE_UDID=(
  ["en-US"]="UDID_EN_US"
  ["de-DE"]="UDID_DE_DE"
  ["fr-FR"]="UDID_FR_FR"
  ["ja-JP"]="UDID_JA_JP"
)

set_simulator_locale() {
  local UDID="$1"
  local LOCALE="$2"            # e.g. de-DE
  local LANG="${LOCALE%%-*}"   # de
  local APPLE_LOCALE="${LOCALE/-/_}" # de_DE

  xcrun simctl boot "$UDID" || true
  xcrun simctl spawn "$UDID" defaults write NSGlobalDomain AppleLanguages -array "$LANG"
  xcrun simctl spawn "$UDID" defaults write NSGlobalDomain AppleLocale -string "$APPLE_LOCALE"
}

for LOCALE in "${!LOCALE_UDID[@]}"; do
  UDID="${LOCALE_UDID[$LOCALE]}"
  echo "Capturing $LOCALE on $UDID..."
  set_simulator_locale "$UDID" "$LOCALE"

  xcrun simctl terminate "$UDID" "com.example.app" || true
  asc screenshots capture \
    --bundle-id "com.example.app" \
    --name "home" \
    --udid "$UDID" \
    --output-dir "./screenshots/raw/$LOCALE" \
    --output json
done
```

If you launch manually (outside `asc screenshots capture`), use app launch arguments:

```bash
xcrun simctl launch "$UDID" "com.example.app" -AppleLanguages "(de)" -AppleLocale "de_DE"
```

## 7) Parallel execution for speed

Run one locale per simulator UDID in parallel:

```bash
#!/bin/bash
# parallel-capture.sh

declare -A LOCALE_UDID=(
  ["en-US"]="UDID_EN_US"
  ["de-DE"]="UDID_DE_DE"
  ["fr-FR"]="UDID_FR_FR"
  ["ja-JP"]="UDID_JA_JP"
)

capture_locale() {
  local LOCALE="$1"
  local UDID="$2"
  local LANG="${LOCALE%%-*}"
  local APPLE_LOCALE="${LOCALE/-/_}"

  echo "Starting $LOCALE on $UDID"
  xcrun simctl boot "$UDID" || true
  xcrun simctl spawn "$UDID" defaults write NSGlobalDomain AppleLanguages -array "$LANG"
  xcrun simctl spawn "$UDID" defaults write NSGlobalDomain AppleLocale -string "$APPLE_LOCALE"
  xcrun simctl terminate "$UDID" "com.example.app" || true

  asc screenshots capture \
    --bundle-id "com.example.app" \
    --name "home" \
    --udid "$UDID" \
    --output-dir "./screenshots/raw/$LOCALE" \
    --output json

  echo "Completed $LOCALE"
}

for LOCALE in "${!LOCALE_UDID[@]}"; do
  capture_locale "$LOCALE" "${LOCALE_UDID[$LOCALE]}" &
done

wait
echo "All captures done. Now framing..."
```

Or use `xargs` with `locale:udid` pairs:

```bash
printf "%s\n" \
  "en-US:UDID_EN_US" \
  "de-DE:UDID_DE_DE" \
  "fr-FR:UDID_FR_FR" \
  "ja-JP:UDID_JA_JP" | xargs -P 4 -I {} bash -c '
    PAIR="{}"
    LOCALE="${PAIR%%:*}"
    UDID="${PAIR##*:}"
    LANG="${LOCALE%%-*}"
    APPLE_LOCALE="${LOCALE/-/_}"
    xcrun simctl boot "$UDID" || true
    xcrun simctl spawn "$UDID" defaults write NSGlobalDomain AppleLanguages -array "$LANG"
    xcrun simctl spawn "$UDID" defaults write NSGlobalDomain AppleLocale -string "$APPLE_LOCALE"
    xcrun simctl terminate "$UDID" "com.example.app" || true
    asc screenshots capture --bundle-id "com.example.app" --name "home" --udid "$UDID" --output-dir "./screenshots/raw/$LOCALE" --output json
  '
```

## 8) Full multi-locale pipeline example

```bash
#!/bin/bash
# full-pipeline-multi-locale.sh

declare -A LOCALE_UDID=(
  ["en-US"]="UDID_EN_US"
  ["de-DE"]="UDID_DE_DE"
  ["fr-FR"]="UDID_FR_FR"
  ["es-ES"]="UDID_ES_ES"
  ["ja-JP"]="UDID_JA_JP"
)

DEVICE="iphone-air"
RAW_DIR="./screenshots/raw"
FRAMED_DIR="./screenshots/framed"

# Step 1: Parallel capture with per-simulator locale defaults
for LOCALE in "${!LOCALE_UDID[@]}"; do
  (
    UDID="${LOCALE_UDID[$LOCALE]}"
    LANG="${LOCALE%%-*}"
    APPLE_LOCALE="${LOCALE/-/_}"

    xcrun simctl boot "$UDID" || true
    xcrun simctl spawn "$UDID" defaults write NSGlobalDomain AppleLanguages -array "$LANG"
    xcrun simctl spawn "$UDID" defaults write NSGlobalDomain AppleLocale -string "$APPLE_LOCALE"
    xcrun simctl terminate "$UDID" "com.example.app" || true

    asc screenshots capture \
      --bundle-id "com.example.app" \
      --name "home" \
      --udid "$UDID" \
      --output-dir "$RAW_DIR/$LOCALE" \
      --output json
    echo "Captured $LOCALE"
  ) &
done
wait

# Step 2: Parallel framing
for LOCALE in "${!LOCALE_UDID[@]}"; do
  (
    asc screenshots frame \
      --input "$RAW_DIR/$LOCALE/home.png" \
      --output-dir "$FRAMED_DIR/$LOCALE" \
      --device "$DEVICE" \
      --output json
    echo "Framed $LOCALE"
  ) &
done
wait

# Step 3: Generate review (single run, aggregates all locales)
asc screenshots review-generate \
  --framed-dir "$FRAMED_DIR" \
  --output-dir "./screenshots/review"

# Step 4: Upload (run per locale if needed)
for LOCALE in "${!LOCALE_UDID[@]}"; do
  asc screenshots upload \
    --version-localization "LOC_ID_FOR_$LOCALE" \
    --path "$FRAMED_DIR/$LOCALE" \
    --device-type "IPHONE_65" \
    --output json
done
```
```

## File: `skills/asc-signing-setup/SKILL.md`
```markdown
---
name: asc-signing-setup
description: Set up bundle IDs, capabilities, signing certificates, provisioning profiles, and encrypted signing sync with the asc cli. Use when onboarding a new app, rotating signing assets, or sharing them across a team.
---

# asc signing setup

Use this skill when you need to create or renew signing assets for iOS/macOS apps.

## Preconditions
- Auth is configured (`asc auth login` or `ASC_*` env vars).
- You know the bundle identifier and target platform.
- You have a CSR file for certificate creation.

## Workflow
1. Create or find the bundle ID:
   - `asc bundle-ids list --paginate`
   - `asc bundle-ids create --identifier "com.example.app" --name "Example" --platform IOS`
2. Configure bundle ID capabilities:
   - `asc bundle-ids capabilities list --bundle "BUNDLE_ID"`
   - `asc bundle-ids capabilities add --bundle "BUNDLE_ID" --capability ICLOUD`
   - Add capability settings when required:
     - `--settings '[{"key":"ICLOUD_VERSION","options":[{"key":"XCODE_13","enabled":true}]}]'`
3. Create a signing certificate:
   - `asc certificates list --certificate-type IOS_DISTRIBUTION`
   - `asc certificates create --certificate-type IOS_DISTRIBUTION --csr "./cert.csr"`
4. Create a provisioning profile:
   - `asc profiles create --name "AppStore Profile" --profile-type IOS_APP_STORE --bundle "BUNDLE_ID" --certificate "CERT_ID"`
   - Include devices for development/ad-hoc:
     - `asc profiles create --name "Dev Profile" --profile-type IOS_APP_DEVELOPMENT --bundle "BUNDLE_ID" --certificate "CERT_ID" --device "DEVICE_ID"`
5. Download the profile:
   - `asc profiles download --id "PROFILE_ID" --output "./profiles/AppStore.mobileprovision"`

## Rotation and cleanup
- Revoke old certificates:
  - `asc certificates revoke --id "CERT_ID" --confirm`
- Delete old profiles:
  - `asc profiles delete --id "PROFILE_ID" --confirm`

## Shared team storage with `asc signing sync`
Use this when you want a lightweight, non-interactive alternative to fastlane match for encrypted git-backed certificate/profile storage.

```bash
# Push current ASC signing assets into an encrypted git repo
asc signing sync push \
  --bundle-id "com.example.app" \
  --profile-type IOS_APP_STORE \
  --repo "git@github.com:team/certs.git" \
  --password "$MATCH_PASSWORD"

# Pull and decrypt them into a local directory
asc signing sync pull \
  --repo "git@github.com:team/certs.git" \
  --password "$MATCH_PASSWORD" \
  --output-dir "./signing"
```

Notes:
- `--password` falls back to `ASC_MATCH_PASSWORD`.
- The encrypted repo follows a familiar match-style git layout for certs and profiles.
- `pull` writes files to disk; keychain import or profile installation is a separate step.

## Notes
- Always check `--help` for the exact enum values (certificate types, profile types).
- Use `--paginate` for large accounts.
- `--certificate` accepts comma-separated IDs when multiple certificates are required.
- Device management uses `asc devices` commands (UDID required).
```

## File: `skills/asc-submission-health/SKILL.md`
```markdown
---
name: asc-submission-health
description: Preflight App Store submissions, submit builds, and monitor review status with asc. Use when shipping or troubleshooting review submissions.
---

# asc submission health

Use this skill to reduce review submission failures and monitor status.

## Preconditions
- Auth configured and app/version/build IDs resolved.
- Build is processed (not in processing state).
- All required metadata is complete.

## Pre-submission Checklist

### 1. Verify Build Status
```bash
asc builds info --build-id "BUILD_ID"
```
Check:
- `processingState` is `VALID`
- `usesNonExemptEncryption` - if `true`, requires encryption declaration

### 2. Encryption Compliance
If `usesNonExemptEncryption: true`:
```bash
# If the app should be exempt, patch the local plist helper, rebuild, and re-upload
asc encryption declarations exempt-declare --plist "./Info.plist"

# List existing declarations
asc encryption declarations list --app "APP_ID"

# Create declaration if needed
asc encryption declarations create \
  --app "APP_ID" \
  --app-description "Uses standard HTTPS/TLS" \
  --contains-proprietary-cryptography=false \
  --contains-third-party-cryptography=true \
  --available-on-french-store=true

# Assign to build
asc encryption declarations assign-builds \
  --id "DECLARATION_ID" \
  --build "BUILD_ID"
```

If the app truly uses only exempt transport encryption, prefer `asc encryption declarations exempt-declare --plist "./Info.plist"` and rebuild instead of creating a declaration that does not match the binary.

### 3. Content Rights Declaration
Required for all App Store submissions:
```bash
# Check current status
asc apps content-rights view --app "APP_ID"

# Set it for most apps
asc apps content-rights edit --app "APP_ID" --uses-third-party-content=false
```
Valid values:
- `DOES_NOT_USE_THIRD_PARTY_CONTENT`
- `USES_THIRD_PARTY_CONTENT`

### 4. Version Metadata
```bash
# Check version details
asc versions view --version-id "VERSION_ID" --include-build

# Verify copyright is set
asc versions update --version-id "VERSION_ID" --copyright "2026 Your Company"
```

### 5. Localizations Complete
```bash
# List version localizations
asc localizations list --version "VERSION_ID"

# Check required fields: description, keywords, whatsNew, supportUrl
```

### 6. Screenshots Present
Each locale needs screenshots for the target platform.

### 7. App Info Localizations (Privacy Policy)
```bash
# List app info IDs (if multiple exist)
asc apps info list --app "APP_ID"

# Check privacy policy URL
asc localizations list --app "APP_ID" --type app-info --app-info "APP_INFO_ID"
```

### 8. App Privacy readiness advisory
`asc` can warn about App Privacy readiness, but the public App Store Connect API
cannot verify whether App Privacy is fully published. Before final submission:

```bash
asc submit preflight --app "APP_ID" --version "1.2.3" --platform IOS
asc validate --app "APP_ID" --version "1.2.3" --platform IOS
```

Prefer the version string form for top-level readiness checks in this skill so it stays aligned with `asc submit preflight`. Lower-level commands later in this guide still use `VERSION_ID` where the API requires it.

If either command reports an App Privacy advisory, the public API cannot verify
publish state. Use the web-session privacy workflow if you rely on those endpoints:

```bash
asc web privacy pull --app "APP_ID" --out "./privacy.json"
asc web privacy plan --app "APP_ID" --file "./privacy.json"
asc web privacy apply --app "APP_ID" --file "./privacy.json"
asc web privacy publish --app "APP_ID" --confirm
```

If you do not want to use the experimental `asc web privacy ...` commands,
confirm App Privacy manually in App Store Connect:

```text
https://appstoreconnect.apple.com/apps/APP_ID/appPrivacy
```

### 9. Digital goods readiness (IAPs / subscriptions)
If the app sells subscriptions or in-app purchases, validate those separately before submit:

```bash
asc validate iap --app "APP_ID" --output table
asc validate subscriptions --app "APP_ID" --output table
```

In current asc, `asc validate subscriptions` expands `MISSING_METADATA` into a per-subscription diagnostics matrix. Use it to identify missing review screenshots, promotional images, pricing or availability coverage gaps, offer readiness, and app/build evidence before retrying submit or first-review attach.

Use `--output json --pretty` when you want exact territory gaps in machine-readable form.

## Submit

### Using Review Submissions API (Recommended)
```bash
# Create submission
asc review submissions-create --app "APP_ID" --platform IOS

# Add version to submission
asc review items-add \
  --submission "SUBMISSION_ID" \
  --item-type appStoreVersions \
  --item-id "VERSION_ID"

# Submit for review
asc review submissions-submit --id "SUBMISSION_ID" --confirm
```

### Using Submit Command
```bash
asc submit preflight --app "APP_ID" --version "1.2.3" --platform IOS
asc submit create --app "APP_ID" --version "1.2.3" --build "BUILD_ID" --confirm
```
Use `--platform` when multiple platforms exist.

## Monitor
```bash
# Check submission status
asc submit status --id "SUBMISSION_ID"
asc submit status --version-id "VERSION_ID"

# List all submissions
asc review submissions-list --app "APP_ID" --paginate
```

## Cancel / Retry
```bash
# Cancel submission
asc submit cancel --id "SUBMISSION_ID" --confirm

# Or via review API
asc review submissions-cancel --id "SUBMISSION_ID" --confirm
```
Fix issues, then re-submit.

## Common Submission Errors

### "Version is not in valid state"
Check:
1. Build is attached and VALID
2. Encryption declaration approved (or exempt)
3. Content rights declaration set
4. All localizations complete
5. Screenshots present for all locales
6. App Privacy has been reviewed and published in App Store Connect

### "Export compliance must be approved"
The build has `usesNonExemptEncryption: true`. Either:
- Upload export compliance documentation
- Or rebuild with `ITSAppUsesNonExemptEncryption = NO` in Info.plist

### "Multiple app infos found"
Use `--app-info` flag with the correct app info ID:
```bash
asc apps info list --app "APP_ID"
```

## Notes
- `asc submit create` uses the new reviewSubmissions API automatically.
- `asc submit preflight` can return non-blocking advisories; review them before submitting.
- App Privacy publish state is not verifiable via the public API.
- Prefer `asc apps content-rights view/edit` over ad-hoc app JSON inspection.
- `asc validate subscriptions` now provides much richer per-subscription diagnostics for `MISSING_METADATA` cases.
- If you use ASC web-session flows, `asc web privacy pull|plan|apply|publish` is the CLI path for App Privacy.
- If you avoid the experimental web-session commands, confirm App Privacy manually in App Store Connect.
- Use `--output table` when you want human-readable status.
- macOS submissions follow the same process but use `--platform MAC_OS`.
```

## File: `skills/asc-subscription-localization/SKILL.md`
```markdown
---
name: asc-subscription-localization
description: Bulk-localize subscription and in-app purchase display names across all App Store locales using asc. Use when you want to fill in subscription/IAP names for every language without clicking through App Store Connect manually.
---

# asc subscription localization

Use this skill to bulk-create or bulk-update display names (and descriptions) for subscriptions, subscription groups, and in-app purchases across all App Store Connect locales. This eliminates the tedious manual process of clicking through each language in App Store Connect to set the same display name.

## Preconditions
- Auth configured (`asc auth login` or `ASC_*` env vars).
- Know your app ID (`ASC_APP_ID` or `--app`).
- Subscription groups and subscriptions already exist.

## Supported App Store Locales

These are the locales supported by App Store Connect for subscription and IAP localizations:

```
ar-SA, ca, cs, da, de-DE, el, en-AU, en-CA, en-GB, en-US,
es-ES, es-MX, fi, fr-CA, fr-FR, he, hi, hr, hu, id, it,
ja, ko, ms, nl-NL, no, pl, pt-BR, pt-PT, ro, ru, sk,
sv, th, tr, uk, vi, zh-Hans, zh-Hant
```

## Workflow: Bulk-Localize a Subscription

### 1. Resolve IDs

```bash
# Find subscription groups
asc subscriptions groups list --app "APP_ID" --output table

# Find subscriptions within a group
asc subscriptions list --group-id "GROUP_ID" --output table
```

### 2. Check existing localizations

```bash
asc subscriptions localizations list --subscription-id "SUB_ID" --paginate --output table
```

This shows which locales already have a name set. Only create localizations for missing locales.

### 3. Create localizations for all missing locales

For each locale that does not already have a localization, run:

```bash
asc subscriptions localizations create \
  --subscription-id "SUB_ID" \
  --locale "LOCALE" \
  --name "Display Name"
```

For example, to set "Monthly Pro" across all locales:

```bash
# One command per locale (skip any that already exist)
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "ar-SA" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "ca" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "cs" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "da" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "de-DE" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "el" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "en-AU" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "en-CA" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "en-GB" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "es-ES" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "es-MX" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "fi" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "fr-CA" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "fr-FR" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "he" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "hi" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "hr" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "hu" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "id" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "it" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "ja" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "ko" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "ms" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "nl-NL" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "no" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "pl" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "pt-BR" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "pt-PT" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "ro" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "ru" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "sk" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "sv" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "th" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "tr" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "uk" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "vi" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "zh-Hans" --name "Monthly Pro"
asc subscriptions localizations create --subscription-id "SUB_ID" --locale "zh-Hant" --name "Monthly Pro"
```

### 4. Verify

```bash
asc subscriptions localizations list --subscription-id "SUB_ID" --paginate --output table
```

## Workflow: Bulk-Localize a Subscription Group

Subscription groups also have their own display name per locale (this is the "group name" shown to users in the subscription management sheet).

### 1. Check existing group localizations

```bash
asc subscriptions groups localizations list --group-id "GROUP_ID" --paginate --output table
```

### 2. Create for missing locales

```bash
asc subscriptions groups localizations create \
  --group-id "GROUP_ID" \
  --locale "LOCALE" \
  --name "Group Display Name"
```

Optional: set a custom app name for the group:

```bash
asc subscriptions groups localizations create \
  --group-id "GROUP_ID" \
  --locale "LOCALE" \
  --name "Group Display Name" \
  --custom-app-name "My App"
```

### 3. Verify

```bash
asc subscriptions groups localizations list --group-id "GROUP_ID" --paginate --output table
```

## Workflow: Bulk-Localize an In-App Purchase

IAPs have their own localization commands with the same pattern.

### 1. Resolve IAP ID

```bash
asc iap list --app "APP_ID" --output table
```

### 2. Check existing localizations

```bash
asc iap localizations list --iap-id "IAP_ID" --paginate --output table
```

### 3. Create for missing locales

```bash
asc iap localizations create \
  --iap-id "IAP_ID" \
  --locale "LOCALE" \
  --name "Display Name"
```

Optional description:

```bash
asc iap localizations create \
  --iap-id "IAP_ID" \
  --locale "LOCALE" \
  --name "Unlock All Features" \
  --description "One-time purchase to unlock all premium features"
```

### 4. Verify

```bash
asc iap localizations list --iap-id "IAP_ID" --paginate --output table
```

## Updating Existing Localizations

To change the display name for existing localizations:

### Subscriptions
```bash
asc subscriptions localizations update --id "LOC_ID" --name "New Name"
```

### Subscription Groups
```bash
asc subscriptions groups localizations update --id "LOC_ID" --name "New Group Name"
```

### In-App Purchases
```bash
asc iap localizations update --localization-id "LOC_ID" --name "New Name"
```

To bulk-update, list existing localizations first, extract the IDs, then update each one.

## Bulk-Localize All Subscriptions in an App

For a full app with multiple subscription groups and subscriptions:

```bash
# 1. List all groups
asc subscriptions groups list --app "APP_ID" --paginate

# 2. For each group, localize the group itself
#    (repeat group localization workflow above)

# 3. For each group, list subscriptions
asc subscriptions list --group-id "GROUP_ID" --paginate

# 4. For each subscription, localize it
#    (repeat subscription localization workflow above)
```

## Agent Behavior

- Always list existing localizations first to avoid duplicate creation errors.
- Skip locales that already have a localization; only create missing ones.
- When the user provides a single display name, use it for all locales (same name everywhere).
- When the user provides translated names per locale, use the locale-specific name for each.
- If a description is provided, pass `--description` on create. Otherwise omit it.
- Use `--output table` for verification steps so the user can visually confirm.
- Use default JSON output for intermediate automation steps.
- After bulk creation, always run the list command to verify completeness.
- For apps with many subscriptions, process them sequentially per group to keep output readable.
- If a create call fails for a locale, log the locale and error, then continue with the remaining locales. After the batch completes, report all failures together so the user can address them.

## Notes
- Subscription display names are what users see on the subscription management sheet and in purchase dialogs.
- Creating a localization for a locale that already exists will fail; always check first.
- There is no bulk API; each locale requires a separate create call.
- Use `--paginate` on list commands to ensure all existing localizations are returned.
- Use the `asc-id-resolver` skill if you only have app names instead of IDs.
```

## File: `skills/asc-testflight-orchestration/SKILL.md`
```markdown
---
name: asc-testflight-orchestration
description: Orchestrate TestFlight distribution, groups, testers, and What to Test notes using asc. Use when rolling out betas.
---

# asc TestFlight orchestration

Use this skill when managing TestFlight testers, groups, and build distribution.

## Export current config
- `asc testflight config export --app "APP_ID" --output "./testflight.yaml"`
- Include builds/testers:
  - `asc testflight config export --app "APP_ID" --output "./testflight.yaml" --include-builds --include-testers`

## Manage groups and testers
- Groups:
  - `asc testflight groups list --app "APP_ID" --paginate`
  - `asc testflight groups create --app "APP_ID" --name "Beta Testers"`
- Testers:
  - `asc testflight testers list --app "APP_ID" --paginate`
  - `asc testflight testers add --app "APP_ID" --email "tester@example.com" --group "Beta Testers"`
  - `asc testflight testers invite --app "APP_ID" --email "tester@example.com"`

## Distribute builds
- `asc builds add-groups --build-id "BUILD_ID" --group "GROUP_ID"`
- Remove from group:
  - `asc builds remove-groups --build-id "BUILD_ID" --group "GROUP_ID" --confirm`

## What to Test notes
- `asc builds test-notes create --build-id "BUILD_ID" --locale "en-US" --whats-new "Test instructions"`
- `asc builds test-notes update --localization-id "LOCALIZATION_ID" --whats-new "Updated notes"`

## Notes
- Use `--paginate` on large groups/tester lists.
- Prefer IDs for deterministic operations; use the ID resolver skill when needed.
```

## File: `skills/asc-wall-submit/SKILL.md`
```markdown
---
name: asc-wall-submit
description: Submit or update a Wall of Apps entry in the App-Store-Connect-CLI repository using `asc apps wall submit`. Use when the user says "submit to wall of apps", "add my app to the wall", or "wall-of-apps".
---

# asc wall submit

Use this skill to add or update a Wall of Apps entry with the built-in CLI flow.

## When to use

- User wants to submit an app to the Wall of Apps
- User wants to update an existing Wall of Apps entry
- User asks for the exact Wall submission flow

## Required inputs

Use one of these input paths:

- Standard App Store flow: `app` ID
- Manual/pre-release flow: `link` plus `name`

## Submission workflow

1. Run commands from the `App-Store-Connect-CLI` repository root.
2. Preview first:
   - `asc apps wall submit --app "1234567890" --dry-run`
   - or `asc apps wall submit --link "https://testflight.apple.com/join/ABCDEFG" --name "My Beta App" --dry-run`
3. Apply with confirmation:
   - `asc apps wall submit --app "1234567890" --confirm`
   - or `asc apps wall submit --link "https://testflight.apple.com/join/ABCDEFG" --name "My Beta App" --confirm`
4. Review the generated PR plan and resulting change to `docs/wall-of-apps.json`.

## Guardrails

- Do not modify unrelated entries in `docs/wall-of-apps.json`.
- If submission fails due to invalid input, fix the inputs and rerun the CLI command.
- Keep submission path PR-based unless maintainers define an issue-based intake flow.

## Examples

Add new app:

`asc apps wall submit --app "1234567890" --confirm`

Submit a non-App-Store/TestFlight entry:

`asc apps wall submit --link "https://testflight.apple.com/join/ABCDEFG" --name "My Beta App" --confirm`
```

## File: `skills/asc-whats-new-writer/SKILL.md`
```markdown
---
name: asc-whats-new-writer
description: Generate engaging, localized App Store release notes (What's New) from git log, bullet points, or free text using canonical metadata under `./metadata`. Optionally pairs with promotional text updates.
---

# asc What's New Writer

Generate engaging, localized release notes from flexible input. Optionally pair with promotional text updates.

## Preconditions

- Metadata pulled locally into canonical files via `asc metadata pull --app "APP_ID" --version "1.2.3" --dir "./metadata"`. OR: user provides keywords manually.
- Auth configured for upload (`asc auth login` or `ASC_*` env vars).
- The **primary locale** is `en-US` unless the user specifies otherwise.

## Before You Start

1. Read `references/release_notes_guidelines.md` for tone, structure, and examples.
2. Identify the **latest version directory** under `metadata/version/` (highest semver). Use this for all metadata reads.
3. Enumerate **existing locales** by listing the JSON files in that version directory.

## Phase 1: Gather Input

Accept one of three input modes (auto-detect):

### Git Log

Parse commits since the last tag:

```bash
# Find latest tag
git describe --tags --abbrev=0

# List commits since that tag
git log $(git describe --tags --abbrev=0)..HEAD --oneline --no-merges
```

Filter out noise: merge commits, dependency bumps, CI changes, formatting-only commits. Extract user-facing changes.

### Bullet Points

User provides rough bullets like:
- "improved search"
- "fixed crash on launch"
- "added sleep timer"

### Free Text

User describes changes conversationally:
> "We made search faster, fixed that annoying crash when you open the app, and added a sleep timer feature"

The skill extracts and structures the changes from the text.

### No Input Provided

Prompt the user: "What changed in this release? You can paste git log output, bullet points, or just describe the changes."

## Phase 2: Draft Notes (Primary Locale)

### Step 1: Classify Changes

Group changes into sections per the guidelines:
- **New** — new features or capabilities
- **Improved** — enhancements to existing features
- **Fixed** — bug fixes users would notice

Omit empty sections. If all changes are fixes, only show "Fixed."

### Step 2: Write Benefit-Focused Copy

Follow the tone rules from `references/release_notes_guidelines.md`:
- Describe user impact, not implementation details
- Use direct address ("you") and action verbs
- Be specific — mention concrete improvements

### Step 3: Front-Load the Hook

The first ~170 characters are the only visible part before "more." Lead with the single most impactful change in a complete, compelling sentence.

### Step 4: Echo Keywords for Conversion

1. Read `keywords` from `metadata/version/{latest}/{primary-locale}.json`
   - These canonical files are also what `asc metadata keywords ...` reads and writes.
2. If the field is empty or missing, skip this step
3. Identify keywords relevant to the changes being described
4. Weave them naturally into the notes — never force or stuff

### Step 5: Respect Character Limits

- Keep total length between 500-1500 characters in the primary locale
- This leaves room for localized expansions (some languages expand 30-40%)
- Hard limit: 4,000 characters

### Step 6: Optionally Draft Promotional Text

If the user wants it, draft a 170-char promotional text that:
- Summarizes the update's theme in one punchy line
- Can reference seasonal events
- Is updatable without a new submission

### Present Draft

Show the draft to the user with character count. Wait for approval before localizing.

## Phase 3: Localize

Translate the approved notes to all existing locales.

### Translation Rules

- Use formal register and formal "you" forms (Russian: вы, German: Sie, French: vous, Spanish: usted, Dutch: u, Italian: Lei)
- Adapt tone to local market — playful English may need adjustment for formal markets (ja, de-DE)
- Do NOT literally translate idioms — adapt them to local equivalents
- A playful tone in English may need to be more respectful or formal in other cultures

### Locale-Specific Keyword Echo

For each locale:
1. Read `keywords` from `metadata/version/{latest}/{locale}.json`
2. Echo locale-specific keywords naturally in the translated notes
3. If keywords field is empty, skip echo for that locale

### Validate

- All translations must be ≤ 4,000 characters
- Promotional text must be ≤ 170 characters per locale
- If a translation exceeds the limit, shorten it — never truncate mid-sentence

## Phase 4: Review & Upload

### Step 1: Present Summary

Show a table of all locales with their notes and character counts:

```
| Locale | What's New (first 80 chars...) | Chars | Promo Text | Chars |
|--------|-------------------------------|-------|------------|-------|
| en-US  | Search just got faster — ...   | 847   | New sleep… | 142   |
| ar-SA  | البحث أصبح أسرع — ...           | 923   | نوم جديد…  | 138   |
| ...    | ...                           | ...   | ...        | ...   |
```

### Step 2: Wait for Approval

Do not upload without user confirmation.

### Step 3: Upload

Upload via `asc` (verify exact syntax with `asc --help`):

```bash
# Individual locale direct update
asc apps info edit --app "APP_ID" --version-id "VERSION_ID" --locale "en-US" --whats-new "Your release notes here"

# Bulk canonical-metadata push after writing ./metadata/version/<version>/<locale>.json
asc metadata push --app "APP_ID" --version "1.2.3" --dir "./metadata" --dry-run
asc metadata push --app "APP_ID" --version "1.2.3" --dir "./metadata"
```

If promotional text was drafted, either include `--promotional-text "..."` in the direct update command or write `promotionalText` into the canonical JSON before `asc metadata push`.

### Step 4: Handle Failures

On partial upload failure:
- Report which locales succeeded and which failed
- Offer to retry failed locales

## Metadata File Paths

- **Keywords:** `metadata/version/{latest-version}/{locale}.json` → `keywords` field
- **Current What's New:** `metadata/version/{latest-version}/{locale}.json` → `whatsNew` field
- **Latest version:** highest semver directory under `metadata/version/`
- The canonical `./metadata` tree is what `asc metadata pull`, `asc metadata push`, and `asc metadata keywords ...` operate on.
- Follows the same metadata resolution conventions as `asc-aso-audit`

## Notes

- What's New is **not indexed** for App Store search — write for humans, not algorithms.
- Promotional text is the only metadata field updatable without a new submission.
- The 170-char visible window is the most important part of your release notes.
- Each app update triggers algorithm re-evaluation — the act of updating matters, even if the text doesn't affect ranking.
- Ideal update cadence: every 2-4 weeks.
- For full metadata translation (all fields), use `asc-localize-metadata` instead.
- For keyword research and optimization, use `asc-aso-audit` first.
- If the local keyword field is stale before drafting, refresh it with `asc metadata pull` or inspect planned keyword changes with `asc metadata keywords diff`.
```

## File: `skills/asc-whats-new-writer/references/release_notes_guidelines.md`
```markdown
# Release Notes Guidelines

Rules and examples for writing engaging App Store release notes (What's New).

## Structure

Three optional sections. Only include sections with content — omit empty ones.

- **New** — new features or capabilities
- **Improved** — enhancements to existing features
- **Fixed** — bug fixes users would notice

## The 170-Character Rule

The first ~170 characters of What's New are visible on the app page without tapping "more." This is the hook.

- Lead with the single most impactful change
- Write a complete, compelling sentence — not a truncated list
- Assume most users will never tap "more"

Example hook (168 chars):
"Search just got faster — find what you need in seconds. Plus: smarter notifications and smoother transitions throughout the app."

## Tone

- **Benefit-focused, not feature-focused.** "Find your favorites in seconds" not "Optimized search indexing algorithm."
- **Engaging but not fluffy** — every word earns its place
- **Direct address ("you")** to create connection
- **Action verbs** over passive descriptions ("Track your progress" not "Progress tracking added")
- **Specific over vague** — mention concrete improvements, not abstract promises

## Anti-Patterns

| Don't | Why |
|-------|-----|
| "Bug fixes and improvements" | Tells the user nothing. Wastes the conversion opportunity. |
| "Version 2.1.0 — We've been working hard!" | Version numbers in headings violate Apple guidelines. Self-congratulation wastes space. |
| Mentioning competitors by name | Against App Store Review Guidelines. |
| References to other platforms | "Now matching our Android version" alienates iOS users. |
| Keyword stuffing | What's New is NOT indexed for search. Every word should serve conversion, not SEO. |
| Marketing fluff with no substance | "The best update ever!" without specifics erodes trust. |
| Walls of text | Users skim. Use short paragraphs or bullet points. |

## Good vs. Bad Examples

**Bad:**
"Bug fixes and performance improvements."

**Good:**
"Search just got faster — find what you need in seconds. Plus: improved notification accuracy and smoother transitions throughout the app."

---

**Bad:**
"Version 2.1.0 — We've been working hard on improvements!"

**Good:**
"New sleep timer options let you drift off to soothing audio. Choose 15, 30, 45, or 60 minutes — perfect for winding down before bed."

---

**Bad:**
"Fixed bugs. Updated UI. Various improvements across the app."

**Good:**
"Real-time highlighting is now perfectly synced, even at 2x speed. Dark mode colors are easier on the eyes, and the app launches 40% faster."

---

**Bad:**
"We fixed a crash that some users reported. Also updated some things in the background."

**Good:**
"No more crashes when switching between tabs — thanks for reporting this! Background sync is now 3x faster, so your data stays up to date."

## Keyword Echo Strategy

What's New is **not indexed** for App Store search. Keywords here serve **conversion only** — users who see familiar search terms in the release notes feel confident they found the right app.

**How to echo:**
1. Read the locale's `keywords` field from local metadata
2. Identify keywords relevant to the changes being described
3. Weave them naturally into sentences — do NOT force irrelevant keywords
4. If the keywords field is empty or missing, skip this step

**Example:** If keywords include `workout,tracker,calories`:
"Improved workout tracking accuracy and real-time calorie counter updates" naturally echoes three keywords.

**Do NOT:** Insert keywords that have nothing to do with the update. "Bug fix for login screen" should not mention "workout" or "calories."

## Promotional Text Pairing

When drafting What's New, optionally draft a matching **Promotional Text** (170 chars max):

- Summarize the update's theme in one punchy line
- Can reference seasonal events (Ramadan, Eid, back-to-school, New Year)
- **Updatable without app submission** — the only "living" metadata field
- Not indexed for search — write purely for conversion
- Refresh monthly or with each major update for re-engagement

**Example:** "New sleep timer + faster search. Your evening routine just got better."

## Localization Notes

- **Formal register** across all languages — use formal "you" forms (Russian: вы, German: Sie, French: vous, Spanish: usted)
- **Cultural adaptation over literal translation** — idioms and playful phrases need local equivalents, not word-for-word translation
- **Load locale-specific keywords** and echo them in the translated notes (each locale has different keywords)
- **Account for text expansion** — some languages expand 30-40% vs. English. Aim for 500-1500 chars in English to leave room.
- **Validate** all translations fit within 4000-char limit
- If translation exceeds the limit, **shorten — never truncate mid-sentence**

## Character Limits

| Field | Limit | Indexed? | Requires Submission? |
|-------|-------|----------|---------------------|
| What's New | 4,000 | No | Yes |
| Promotional Text | 170 | No | No |
```

## File: `skills/asc-workflow/SKILL.md`
```markdown
---
name: asc-workflow
description: Define, validate, and run repo-local multi-step automations with `asc workflow` and `.asc/workflow.json`. Use when migrating from lane tools, wiring CI pipelines, or orchestrating repeatable `asc` + shell release flows with hooks, conditionals, and sub-workflows.
---

# asc workflow

Use this skill when you need lane-style automation inside the CLI using:
- `asc workflow run`
- `asc workflow validate`
- `asc workflow list`

This feature is best for deterministic automation that lives in your repo, is reviewable in PRs, and can run the same way locally and in CI.

## Command discovery

- Always use `--help` to confirm flags and subcommands:
  - `asc workflow --help`
  - `asc workflow run --help`
  - `asc workflow validate --help`
  - `asc workflow list --help`

## End-to-end flow

1. Author `.asc/workflow.json`
2. Validate structure and references:
   - `asc workflow validate`
3. Discover available workflows:
   - `asc workflow list`
   - `asc workflow list --all` (includes private helpers)
4. Preview execution without side effects:
   - `asc workflow run --dry-run beta`
5. Execute with runtime params:
   - `asc workflow run beta BUILD_ID:123456789 GROUP_ID:abcdef`

## File location and format

- Default path: `.asc/workflow.json`
- Override path: `asc workflow run --file ./path/to/workflow.json <name>`
- JSONC comments are supported (`//` and `/* ... */`)

## Output and CI contract

- `stdout`: structured JSON result (`status`, `steps`, durations)
- `stderr`: step command output, hook output, dry-run previews
- `asc workflow validate` always prints JSON and returns non-zero when invalid

This enables machine-safe checks:

```bash
asc workflow validate | jq -e '.valid == true'
asc workflow run beta BUILD_ID:123 GROUP_ID:xyz | jq -e '.status == "ok"'
```

## Schema (what the feature supports)

Top-level keys:
- `env`: global defaults
- `before_all`: command run once before steps
- `after_all`: command run once after successful steps
- `error`: command run when any failure occurs
- `workflows`: named workflow map

Workflow keys:
- `description`
- `private` (not directly runnable)
- `env`
- `steps`

Step forms:
- String shorthand: `"echo hello"` -> run step
- Object with:
  - `run`: shell command
  - `workflow`: call sub-workflow
  - `name`: label for reporting
  - `if`: conditional var name
  - `with`: env overrides for workflow-call steps only

## Runtime params (`KEY:VALUE` / `KEY=VALUE`)

- `asc workflow run <name> [KEY:VALUE ...]` supports both separators:
  - `VERSION:2.1.0`
  - `VERSION=2.1.0`
- If both separators exist, the first one wins.
- Repeated keys are last-write-wins.
- In step commands, reference params via shell expansion (`$VAR`).
- Avoid putting secrets in `.asc/workflow.json`; pass them via CI secrets/env.

## Run-tail flags

`asc workflow run` also accepts core flags after the workflow name:
- `--dry-run`
- `--pretty`
- `--file`

Examples:
- `asc workflow run beta --dry-run`
- `asc workflow run beta --file .asc/workflow.json BUILD_ID:123`

## Execution semantics

- `before_all` runs once before step execution
- `after_all` runs only when steps succeed
- `error` runs on failure (step failure, before/after hook failure)
- Sub-workflows are executed inline as part of the call step
- Maximum sub-workflow nesting depth is 16

## Env precedence

Main workflow run:
- `definition.env` < `workflow.env` < CLI params

Sub-workflow call step (`"workflow": "...", "with": {...}`):
- sub-workflow `env` defaults
- caller env (including CLI params) overrides
- step `with` overrides all

## Sub-workflows and private workflows

- Use `"workflow": "<name>"` to call helper workflows.
- Use `"private": true` for helper-only workflows.
- Private workflows:
  - cannot be run directly
  - can be called by other workflows
  - are hidden from `asc workflow list` unless `--all` is used
- Validation catches unknown workflow references and cyclic references.

## Conditionals (`if`)

- Add `"if": "VAR_NAME"` on a step.
- Step runs only if `VAR_NAME` is truthy.
- Truthy: `1`, `true`, `yes`, `y`, `on` (case-insensitive).
- Resolution order for `if` lookup:
  1. merged workflow env/params
  2. `os.Getenv(VAR_NAME)`

## Dry-run behavior

- `asc workflow run --dry-run <name>` does not execute commands.
- It prints previews to `stderr`.
- Dry-run shows raw commands (without env expansion), which helps avoid secret leakage in previews.

## Shell behavior

- Run steps use `bash -o pipefail -c` when bash is available.
- Fallback is `sh -c` when bash is unavailable.
- Pipelines therefore fail correctly in most CI shells when bash exists.

## Practical authoring rules

- Keep workflow files in version control.
- Use IDs in step commands where possible for deterministic automation.
- Use `--confirm` for destructive `asc` operations inside steps.
- Validate first, then dry-run, then real run.
- Keep hooks lightweight and side-effect aware.

```json
{
  "env": {
    "APP_ID": "123456789",
    "VERSION": "1.0.0"
  },
  "before_all": "asc auth status",
  "after_all": "echo workflow_done",
  "error": "echo workflow_failed",
  "workflows": {
    "beta": {
      "description": "Distribute a build to a TestFlight group and notify",
      "env": {
        "GROUP_ID": ""
      },
      "steps": [
        {
          "name": "list_builds",
          "run": "asc builds list --app $APP_ID --sort -uploadedDate --limit 5"
        },
        {
          "name": "list_groups",
          "run": "asc testflight groups list --app $APP_ID --limit 20"
        },
        {
          "name": "add_build_to_group",
          "if": "BUILD_ID",
          "run": "asc builds add-groups --build-id $BUILD_ID --group $GROUP_ID"
        },
        {
          "name": "notify",
          "if": "SLACK_WEBHOOK",
          "run": "echo sent_release_notice"
        }
      ]
    },
    "release": {
      "description": "Submit a version for App Store review",
      "steps": [
        {
          "workflow": "sync-metadata",
          "with": {
            "METADATA_DIR": "./metadata"
          }
        },
        {
          "name": "submit",
          "run": "asc submit create --app $APP_ID --version $VERSION --build $BUILD_ID --confirm"
        }
      ]
    },
    "sync-metadata": {
      "private": true,
      "description": "Private helper workflow (callable only via workflow steps)",
      "steps": [
        {
          "name": "migrate_validate",
          "run": "echo METADATA_DIR_is_$METADATA_DIR"
        }
      ]
    }
  }
}
```

## Useful invocations

```bash
# Validate and fail CI on invalid file
asc workflow validate | jq -e '.valid == true'

# Show discoverable workflows
asc workflow list --pretty

# Include private helpers
asc workflow list --all --pretty

# Preview a real run
asc workflow run --dry-run beta BUILD_ID:123 GROUP_ID:grp_abc

# Run with params and assert success
asc workflow run beta BUILD_ID:123 GROUP_ID:grp_abc | jq -e '.status == "ok"'
```
```

## File: `skills/asc-xcode-build/SKILL.md`
```markdown
---
name: asc-xcode-build
description: Build, archive, export, and manage Xcode version/build numbers with asc and xcodebuild before uploading to App Store Connect. Use when you need to create an IPA or PKG for upload.
---

# Xcode Build and Export

Use this skill when you need to build an app from source and prepare it for upload to App Store Connect.

## Preconditions
- Xcode installed and command line tools configured
- Valid signing identity and provisioning profiles (or automatic signing enabled)

## Manage version and build numbers with `asc`
Before archiving, prefer `asc xcode version ...` over manual `pbxproj` edits when you need to inspect or bump app versions.

```bash
asc xcode version view
asc xcode version edit --version "1.3.0" --build-number "42"
asc xcode version bump --type build
asc xcode version bump --type patch
```

Notes:
- Use `--project-dir "./MyApp"` when you are not running from the project root.
- Use `--target "App"` for deterministic reads in multi-target projects.
- These commands support both legacy `agvtool` projects and modern `MARKETING_VERSION` / `CURRENT_PROJECT_VERSION` setups.

## iOS Build Flow

### 1. Clean and Archive
```bash
xcodebuild clean archive \
  -scheme "YourScheme" \
  -configuration Release \
  -archivePath /tmp/YourApp.xcarchive \
  -destination "generic/platform=iOS"
```

### 2. Export IPA
```bash
xcodebuild -exportArchive \
  -archivePath /tmp/YourApp.xcarchive \
  -exportPath /tmp/YourAppExport \
  -exportOptionsPlist ExportOptions.plist \
  -allowProvisioningUpdates
```

A minimal `ExportOptions.plist` for App Store distribution:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>method</key>
    <string>app-store-connect</string>
    <key>teamID</key>
    <string>YOUR_TEAM_ID</string>
</dict>
</plist>
```

### 3. Upload with asc
```bash
asc builds upload --app "APP_ID" --ipa "/tmp/YourAppExport/YourApp.ipa"
```

## macOS Build Flow

### 1. Archive
```bash
xcodebuild archive \
  -scheme "YourMacScheme" \
  -configuration Release \
  -archivePath /tmp/YourMacApp.xcarchive \
  -destination "generic/platform=macOS"
```

### 2. Export PKG
```bash
xcodebuild -exportArchive \
  -archivePath /tmp/YourMacApp.xcarchive \
  -exportPath /tmp/YourMacAppExport \
  -exportOptionsPlist ExportOptions.plist \
  -allowProvisioningUpdates
```

### 3. Upload PKG with asc
macOS apps export as `.pkg` files. Upload with `asc`:
```bash
asc builds upload \
  --app "APP_ID" \
  --pkg "/tmp/YourMacAppExport/YourApp.pkg" \
  --version "1.0.0" \
  --build-number "123"
```

Notes:
- `--pkg` automatically sets platform to `MAC_OS`.
- For `.pkg` uploads, `--version` and `--build-number` are required (they are not auto-extracted like IPA uploads).
- Add `--wait` if you want to wait for build processing to complete.

## Build Number Management

Each upload requires a unique build number higher than previously uploaded builds.

In Xcode project settings:
- `CURRENT_PROJECT_VERSION` - build number (e.g., "316")
- `MARKETING_VERSION` - version string (e.g., "2.2.0")

Check existing builds:
```bash
asc builds list --app "APP_ID" --platform IOS --limit 5
```

## Troubleshooting

### "No profiles for bundle ID" during export
- Add `-allowProvisioningUpdates` flag
- Verify your Apple ID is logged into Xcode

### Build rejected for missing icon (macOS)
macOS requires ICNS format icons with all sizes:
- 16x16, 32x32, 128x128, 256x256, 512x512 (1x and 2x)

### CFBundleVersion too low
The build number must be higher than any previously uploaded build. Increment it with `asc xcode version bump --type build`, or resolve a remote-safe number with `asc builds next-build-number --app "APP_ID" --version "2.2.0" --platform IOS` and then apply it with `asc xcode version edit --build-number "NEXT_BUILD"` before rebuilding.

## Notes
- Always clean before archive for release builds
- Use `xcodebuild -showBuildSettings` to verify configuration
- For submission issues (encryption, content rights), see `asc-submission-health` skill
```

