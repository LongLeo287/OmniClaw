---
id: repo-fetched-atlos-094814
type: knowledge
owner: OA
registered_at: 2026-04-05T03:34:16.522500
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_Atlos_094814

## Assimilation Report
Auto-cloned repository: FETCHED_Atlos_094814

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Atlos
<ruby>
Atlos (= Atlas)
<rt>from Talos, an anagram trick</rt>
</ruby>is an open-source online map for the 3D RTSRPG game Arknights: Endfield (by Hypergryph). This repository contains the web client (codename “talos”) built with React + Vite, featuring an Endfield-esque UI, multilingual support, and a CDN‑friendly build pipeline.

PRs are warmly welcome—see [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

## Community

[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/2PMegCX4wJ)
[![Build](https://img.shields.io/github/actions/workflow/status/Terra-Online/Atlos/build.yml?branch=main&label=build&logo=github)](https://github.com/Terra-Online/Atlos/actions/workflows/build.yml)
[![License](https://img.shields.io/github/license/Terra-Online/Atlos?label=license)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

Come and chat with us on **Discord**: [https://discord.gg/BFMAKZSUG7](https://discord.gg/BFMAKZSUG7)

## Highlights

- Modern stack: React, TypeScript, Vite, SCSS Modules;
- Map rendering with Leaflet and custom hooks/components (verb.1, we consider to migrate current structure to Canvaskit in next version);
- The project is well organized in our JIRA Kanban, consider joining us and take some todos!
- Clean UI with Figma workflow;
- Full internationalization (UI/Game), clear fallback rules;
- CDN/OSS friendly build and publish scripts;

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for:
- environment setup
- coding standards & linting
- branch/commit/PR conventions
- translation workflow

## Repository layout

Top-level folders you’ll most likely interact with:

- `talos/` – the web app
	- `src/` – application source
		- `component/` – UI components (modal, sidebar, language selector, groups modal, etc.)
    		- `component/map/` – map integration (Leaflet + hooks)
		- `locale/` – i18n system, UI text resources
		- `store/` – global UI state (Zustand)
		- `styles/` – shared SCSS (palette, fonts, globals)
		- `utils/` – helpers (device, font loader/cache, logging, resources)
	- `public/` – public static assets
	- `config/` – build-time config (ignored by Git), see “Build & Deploy”
	- `scripts/` – helper scripts (e.g. publish to OSS/CDN)
	- `vite.config.js` – Vite configuration

## Getting started

Requirements:
- Node.js 20+
- pnpm 10+

Install & run (from the `talos` directory):

```bash
# 1) Install deps
pnpm install

# 2) Start dev server
pnpm dev

# 3) Type check (optional)
pnpm run type-check

# 4) Build for production
pnpm build
```

## Internationalization (i18n)

- UI language resources now live under `talos/src/locale/data/ui/`.
- The app distinguishes between “full support” (UI + in‑game terms) and “UI‑only” languages. When game content is not available, English will be used as a fallback for those parts.
- To add or improve translations, see the guidance in [CONTRIBUTING.md](CONTRIBUTING.md).

## Fonts
- Main latin letters are displayed in Novencento Sans Wide family provided by [Synthview Type Design](https://typography.synthview.com/novecento-sans-font-family.php).
- Variable font HMSans (weights 100–900) is used alongside region‑specific fonts.
- Fonts are loaded dynamically using the utilities in `src/utils/fontLoader.ts` and `src/utils/fontCache.ts`.

## License

This project is licensed under the **GNU Affero General Public License v3.0**. See [LICENSE](LICENSE) for the full text.

```

### File: CONTRIBUTING.md
```md
# Contributing to Atlos

Thank you for your interest in contributing! This guide explains how to set up your environment, follow coding standards, add features, and submit high‑quality pull requests.

## 1. Project Scope & Philosophy
Atlos aims to provide a performant, multilingual, map‑centric web client for Arknights: Endfield community knowledge and exploration. We value:
- **Performance**: lean renders, efficient data access, CDN‑friendly assets.
- **Clarity**: typed interfaces (TypeScript), explicit fallbacks for i18n.
- **Maintainability**: modular components, minimal global state, readable SCSS.
- **Openness**: transparent build/deploy flow without leaking secrets.

## 2. Tech Stack Summary
- React 18 + TypeScript (strict mode)
- Vite build system
- SCSS Modules for component styling
- Leaflet for interactive mapping
- Zustand for lightweight global state
- Progressive blur & transitions for UI polish

## 3. Repository Structure (key paths)
```
Atlos/
  talos/
    src/
      component/        # UI + map components
      component/map/    # Leaflet integration & hooks
      locale/           # i18n loader, language data
      store/            # Zustand stores
      styles/           # global SCSS (palette, fonts, curves)
      utils/            # helpers (device, fonts, logging, resources)
      data/             # static data (types, markers)
    config/             # build-time config (ignored from VCS)
    scripts/            # publish / utility scripts
    public/             # static public assets
    vite.config.js      # build config
```

## 4. Environment Setup
```bash
# Move into web client
cd talos

# Install dependencies
pnpm install --frozen-lockfile

# Start dev server
pnpm dev

# Type check
pnpm run type-check

# Build production bundle
pnpm build
```
Node 20+ and pnpm 8+ recommended.

## 5. Coding Standards
- **TypeScript**: prefer explicit types; avoid implicit `any`. Use discriminated unions for complex variants.
- **Components**: keep pure/presentational vs. stateful separated. Co-locate style file (`.module.scss`) with component.
- **Imports**: use path aliases (`@/utils/...`) instead of deep relative traversals.
- **Logging**: use provided util (`log.ts`) rather than raw `console.log` for future centralization.
- **Performance**: memoize expensive derived values; avoid unnecessary re-renders (React hooks discipline).
- **CSS/SCSS**: leverage variables from `palette.scss`, keep selectors shallow, avoid global leakage.

## 6. Git & Branching
- **Branches**: `feature/<name>` for new features; `fix/<name>` for bug fixes; `release/<tag>` for prep.
- **Commits**: Use concise imperative messages; group related changes. Examples:
  - `feat(map): add dynamic marker clustering`
  - `fix(locale): fallback when UI-only language lacks game terms`
  - `chore(build): add OSS skip logic`
- Rebase before opening PR to keep history linear if possible.

## 7. Pull Request Checklist
Before marking a PR ready for review:
- [ ] Builds (`pnpm build`) and passes type-check.
- [ ] No introduction of secret values (config.json remains Git‑ignored).
- [ ] i18n keys added have defaults/fallbacks.
- [ ] UI changes tested in light & dark theme.
- [ ] For new languages or keys: translation placeholders added.
- [ ] Added/updated docs if behavior changed.

## 8. Internationalization Workflow
- UI strings live under `src/locale/data/ui/<lang>.json`.
- Distinguish between full support and UI‑only languages; ensure English fallback for missing in‑game terms.
- When adding a new key:
  1. Add to all existing language JSON files (tentative translation or placeholder).
  2. If the language is UI‑only, confirm fallback logic still works.
  3. Test language switch via `LanguageModal`.

## 9. Fonts
- HMSans variable font (100–900 weight range) configured in `fontLoader.ts`.
- When introducing a new font: ensure proper licensing & add @font-face with range if variable.
- Avoid inlining large font files directly in code; rely on CDN/OSS distribution.

## 10. Map & Data Updates
- Marker type definitions live under `src/data/marker/` and related tree constants.
- For new marker categories:
  - Update marker type tree & ensure translation keys exist.
  - Provide appropriate icons in `src/assets/images/marker/` (if needed) – optional copy logic will include them.
- Keep large geo/asset datasets out of Git if they are dynamic—use external storage/CDN.

## 11. Build & Deployment Notes
- `talos/config/config.json` is intentionally Git‑ignored.
- Use `config/config.template.json` for structure reference; generate a real config in CI/ECS with your CDN + OSS credentials.
- Vite base path derives from `web.build.cdn + web.build.oss.prefix`.
- **Do not** commit secrets (access keys, GA IDs). Inject via environment variables or private config generation.

## 12. Secrets & Safety
- Keep all credentials out of the public repo.
- Provide fallbacks (empty strings) to avoid build crashes when config is absent during local dev.
- NEVER echo secret values in CI logs—mask or print length only.

## 13. Testing & Verification
Currently lightweight (no full test suite). Recommended before PR:
- Manual verification of language switching.
- Map renders without console errors.
- Sidebar interactions (open/close, filter list, triggers) work.

Future additions may include unit tests for utilities & integration smoke tests.

## 14. Adding Translations
1. Duplicate an existing language file as reference.
2. Translate new keys; maintain punctuation consistency.
3. Ensure hints end with a period (or appropriate CJK punctuation)。
4. Validate encoding (UTF‑8) and no trailing commas.

## 15. Submitting Your PR
1. Open PR against `main` (or designated integration branch).
2. Fill description: motivation, changes, any follow-up TODO.
3. Link related issues (if any).
4. Request review from maintainers.

## 16. Questions & Support
Join the Discord community: https://discord.gg/2PMegCX4wJ

## 17. License
Contributions are accepted under the existing project license: **GNU AGPL v3**. By submitting a PR you agree your code is licensed accordingly.

---
Thanks again for helping improve Atlos - Open Endfield Map!

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for atlos
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\agents\i18nAgent.agent.md
```md
# Talos i18n Translation Agent

## Purpose
This agent translates the Chinese source file (`zh-CN.json`) into other target languages while ensuring that structure, formatting, and inline markup remain fully consistent with the original.

The agent MUST guarantee that every translated language file is structurally identical to the source and safe for direct use in the production system.

---

## Responsibilities
1. Produce translations that strictly follow the structure of the source JSON file.
2. Preserve **every key**, **every nested object**, and **every value type**.
3. Maintain the **same ordering of keys** as the source file.
4. Preserve formatting such as:
   - Inline HTML tags (`<span>`, `<br>`, `<p>`, `<ul>`, `<li>`, etc.)
   - Newline sequences (`\n`)
   - Attributes within tags
5. Detect any issues and output clearly labeled warnings.

---

## Input Format
The agent receives:

1. The Chinese source file (`zh-CN.json`)
2. The target language to translate into
3. Optionally: A partially translated target JSON file (for updates or diffs)

---

## Output Requirements
### Required Output Format:
The agent must output a JSON object that:

- Matches the **exact structure** of `zh-CN.json`
- Maintains the **same key order**
- Preserves all inline formatting
- Contains translated string values only

### Prohibited:
- Modifying or renaming keys  
- Reordering keys  
- Adding new keys  
- Removing existing keys  
- Changing HTML tag structure  
- Removing escape sequences  
- Introducing extra whitespace or newlines  

---

## String Translation Rules

### 1. Structure Preservation
The following MUST remain unchanged:

- HTML tags  
- HTML attributes  
- Brackets and placeholders (`{}`, `%s`, `${}`, `{{value}}`)  
- Line breaks (`\n`)  
- Embedded formatting such as `<span class="keyword">`  

Examples:

- `<span class="keyword">Region</span>` → `<span class="keyword">Región</span>`
- `"You have selected \n the region."` → translated but with `\n` kept

---

### 2. Do Not Translate:
- Keys (left side of the JSON)
- HTML tag names
- Class names or attributes
- Numerical values
- URLs
- File names
- Placeholder variables

---

### 3. When Uncertain:
If the agent encounters ambiguous text or terms that might have multiple interpretations:

- **Do NOT guess.**
- Output a `WARNING:` message describing the issue.
- Produce a best-effort translation while maintaining original markup.

Example:
```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug report
about: Create a report to help us improve
title: "[BUG]"
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - OS: [e.g. MacOS Sequoia/15.7.1]
 - Browser [e.g. Chrome 141, Safari 26]

**Smartphone (please complete the following information):**
 - Device: [e.g. iPhone 16 Pro]
 - OS: [e.g. iOS 26.1]
 - Browser [e.g. Edge Mobile, Safari]

**Additional context**
Add any other context about the problem here.

```

### File: .github\ISSUE_TEMPLATE\feature_request.md
```md
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.

```

