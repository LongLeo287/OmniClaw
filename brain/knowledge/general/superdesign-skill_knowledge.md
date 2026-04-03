---
id: superdesign-skill-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:19.189775
---

# KNOWLEDGE EXTRACT: superdesign-skill
> **Extracted on:** 2026-03-30 13:22:44
> **Source:** superdesign-skill

---

## File: `.gitignore`
```
.claude
```

## File: `README.md`
```markdown
SuperDesign helps you (1) find design inspirations/styles and (2) generate/iterate design drafts on an infinite canvas.

---

# Core scenarios (what this skill handles)

1. **Help me design X** (feature/page/flow)
2. **Set design system**
3. **Help me improve design of X**

# Quickstart

Install CLI
```
npm install -g @superdesign/cli@latest
```

Install skills for any coding agent
```
npx skills add superdesigndev/superdesign-skill
```

Prompt in any agent
```
/superdesign help me design X
```

--

## Tooling overview

### A) Inspiration & Style Tools (generic, always available)

Use these to discover style direction, references, and brand context:

- **Search prompt library** (style/components/pages)

  ```bash
  superdesign search-prompts --keyword "<keyword>" --json
  superdesign search-prompts --tags "style" --json
  superdesign search-prompts --tags "style" --keyword "<style keyword>" --json
  ```

- **Get full prompt details**

  ```bash
  superdesign get-prompts --slugs "<slug1,slug2,...>" --json
  ```

- **Extract brand guide from a URL**
  ```bash
  superdesign extract-brand-guide --url https://example.com --json
  ```

### B) Canvas Design Tools

Use design agent to generate high quality design drafts:
- Create project (supports prompt / prompt file / HTML)
- Create design draft
- Iterate design draft (replace / branch)
- Plan flow pages → execute flow pages
- Fetch specific design draft

---

## Overall SOP for designing features on top of existing app:
1. Investigate existing UI, workflow
2. Setup design system file if not exist yet
3. Requirements gathering: use askQuestion tool to clarify requirements with users (Optionally use Inspiration tool to find inspiration when needed)
4. Ask user whether ready to design in superdesign OR implement UI directly
5. If yes to superdesign
  5.1 Create/update a pixel perfect html replica of current UI of page that we will design on top of in `.superdesign/replica_html_template/<name>.html` (html should only contain & reflect how UI look now, the actual design should be handled by superdesign agent)
  5.2 Create project with this replica html + design system guide
  5.3 Start desigining by iterating & branching design draft based on designDraft ID returned from project


## Always-on rules
- Design system should live at: `.superdesign/design-system.md`
- If `.superdesign/design-system.md` is missing, run **Design System Setup** first.
- Use `askQuestion` to ask high-signal questions (constraints, taste, tradeoffs).
- Always use `--json` for machine parsing.

---

## replica_html_template rules (Canvas only)

The purpose of replica html template is creating a lightweight version of existing UI so design agent can iterate on top of it (Since superdesign doesn't have access to your codebase directly, this is important context)

Overall process for designing features on top of existing app:
1. Identify & understand existing UI of page related
2. Create/update a pixel perfect replica html in `.superdesign/replica_html_template/<name>.html` (Only replicate how UI look now, do NOT design)
  - If design task is redesign profile page, then replicate current profile page UI pixel perfectly
  - If design task is add new button to side panel, identify which page side panel is using, then replicate that page UI pixel perfectly

**replica_html_template = BEFORE state (what exists now).** It provides context for SuperDesign agent.
Actual design will be done via superdesign agent, by passing the prompt

The replica_html_template must contain **ONLY UI that currently exists in the codebase**. 
- **DO NOT** design or improve anything in the replica_html_template
- **DO NOT** add placeholder sections like `<!-- NEW FEATURE - DESIGN THIS -->`
- **DO** create pixel-perfect replica of current UI state
- Save to: `.superdesign/replica_html_template/<name>.html`

### Naming & Reuse

**Naming convention** 
Name replica_html_template for reusability: Use the page route (e.g., `home.html`, `settings-profile.html`, `dashboard.html`)
This makes it easy to identify if a page_template already exists.

**Before creating a replica_html_template:**
1. Check if `.superdesign/replica_html_template/` already contains a matching file
2. If exists: reuse it or update to reflect the latest existing UI
3. If not exists: create the neww file

### Example: Adding a "Book Demo" section to home page

**BAD approach:**

```html
<!-- replica_html_template includes a sketched Book Demo section -->
<section class="book-demo">
  <!-- DESIGN THIS - Add CTA here -->
  <h3>Book a Demo</h3>
  <button>Schedule</button>
</section>
```

**GOOD approach:**

```html
<!-- replica_html_template is pure replica of existing home page (hero + projects) -->
```

Then in the iterate command:
1/ create project passing this replica html
2/ create design draft based on design draft id

---

# 1) Design System Setup

### Step 0 — Ask user (one question)

"Do you want to **create a new design system** or **extract from the current codebase**?"

### A) Extract from codebase

1. Investigate codebase:
   - Product context: what is being built, target users, core value proposition, key user journeys and page structure
   - design tokens, typography, colors, spacing, radius, shadows
   - motion/animation patterns
   - example components usage + implementation patterns
2. Write standalone design system to:
   - `.superdesign/design-system.md`
   - Must be implementable without the codebase

### B) Create a new design system (to improve current UI)

1. Investigate codebase to understand:
   - Product context: what is being built, target users, core value proposition, key user journeys and page structure
   - needed pages/components
2. Gather inspirations (generic tools):
   - `superdesign search-prompts --tags "style" --json`
   - `superdesign get-prompts --slugs ... --json`
   - optional: `superdesign extract-brand-guide --url ... --json`
3. Interview user (`askQuestion`) to choose direction
4. Write:
   - `.superdesign/design-system.md` (product context + UX flows + visual design, adapted to references)

---

# 2) Designing X (feature/page/flow)

### Example workflow - Add feature to existing page

1. Investigate existing design and Ask targeted questions (`askQuestion`) about requirements + taste
2. After clarifying, Ask user whether ready to design in superdesign OR implement UI directly
3. If design in superdesign
  3.1 Ensure `.superdesign/design-system.md` exists (setup if missing)
  3.2 Identify page most relevant, and build a pixel-perfect replica in replica_html_template:
    - `.superdesign/replica_html_template/<page>-<feature>.html`
  3.3 Create project with replica_html_template (returns `draftId`):
    ```bash
    superdesign create-project \
      --title "<feature>" \
      --html-file .superdesign/replica_html_template/<file>.html \
      --set-project-prompt-file .superdesign/design-system.md \
      --json
    ```
    → Note: `draftId` in response is the baseline draft
  3.4 Branch designs from baseline (use `draftId` from step 3.3)
    ```bash
    superdesign iterate-design-draft \
      --draft-id <draftId> \
      -p "Dark theme with neon accents" \
      -p "Minimal with more whitespace" \
      -p "Bold gradients and shadows" \
      --mode branch \
      --json
    ```
  3.5 Share design title & preview URL → collect feedback → iterate


### Advanced usage

#### Design multiple page OR a full user journey

Execute:

```bash
superdesign execute-flow-pages \
  --draft-id <draftId> \
  --pages '[{"title":"Signup","prompt":"..."},{"title":"Payment","prompt":"..."}]' \
  --json
```

#### Get HTML reference from a draft

```bash
superdesign get-design --draft-id <draftId> --output ./design.html
```

---

## Quick reference (key commands)

```bash
# Inspirations
superdesign search-prompts --keyword "<keyword>" --json
superdesign search-prompts --tags "style" --json
superdesign get-prompts --slugs "<slug1,slug2>" --json
superdesign extract-brand-guide --url https://example.com --json

# Canvas - Create project
# Options: -s/--set-project-prompt (inline), --set-project-prompt-file (from file)
superdesign create-project --title "X" --set-project-prompt "..." --json
superdesign create-project --title "X" --set-project-prompt-file .superdesign/design-system.md --json
superdesign create-project --title "X" --html-file ./index.html --set-project-prompt-file .superdesign/design-system.md --json

# Iterate: replace mode (single variation, updates in place)
superdesign iterate-design-draft --draft-id <id> -p "..." --mode replace --json

# Iterate: Explore multiple versions & variations (each prompt = one variation, prompt should be just directional, do not specify color, style, let superdesign design expert fill in details, you just give direction)
superdesign iterate-design-draft --draft-id <id> -p "dark theme" -p "minimal" -p "bold" --mode branch --json

# Iterate: Auto explore (only give exploration direction, and let Superdesign fill in details, e.g. explore different styles; Default do not use this)
superdesign iterate-design-draft --draft-id <id> -p "..." --mode branch --count 3 --json

# Fetch & get designs
superdesign fetch-design-nodes --project-id <id> --json
superdesign get-design --draft-id <id> --json

# Create new design from scracth without any reference - ONLY use this for creating brand new design, default NEVER use this
superdesign create-design-draft --project-id <id> --title "X" -p "..." --json
```
```

## File: `skills/superdesign/INIT.md`
```markdown
You are performing a **SuperDesign Init** — analyzing this repository to build UI context files that SuperDesign agent will use for design tasks.

## Output Directory
Write all files to `.superdesign/init/` in the project root.

## Analysis Steps

### 1. Detect Framework & Component Library
Scan `package.json`, config files (`next.config.*`, `vite.config.*`, `rsbuild.config.*`, `nuxt.config.*`, etc.), and import patterns to determine:
- Framework: React, Vue, Svelte, Angular, etc.
- Meta-framework: Next.js, Nuxt, Remix, Astro, etc.
- Component library: shadcn/ui, Ant Design, MUI, Chakra, Radix, custom, etc.
- CSS approach: Tailwind, CSS Modules, styled-components, vanilla CSS, etc.

### 2. Write `components.md`
Identify the project's shared/reusable UI component directory (e.g., `src/components/ui/`, `components/`, `packages/ui/`).

**IMPORTANT**: Include FULL source code for each component, not just descriptions. SuperDesign needs the actual implementation to reproduce accurately.

For each component, include:
- File path
- Component name
- Brief description (1 line)
- Key props if obvious from the export
- **FULL source code** in fenced code blocks

Focus on **shared UI primitives** (Button, Input, Dialog, Card, Select, Checkbox, Table, Tabs, etc.), not page-specific components.

⚠️ This file should contain the ACTUAL CODE of components, not just a list of names.

### 3. Write `layouts.md`
Find and READ all shared layout components. These are the components that appear on every page or across multiple pages:
- App shell / root layout
- Navigation bar (top nav, bottom nav)
- Sidebar
- Header / top bar
- Footer
- Breadcrumb
- Layout wrappers / HOCs

For each, include:
- File path
- Full source code (copy the entire file content)
- Brief description of what it renders

This is critical — SuperDesign needs the actual layout code to reproduce pages accurately.

### 4. Write `routes.md`
Map out the page/route structure:
- For file-based routing (Next.js, Nuxt): list route files and their paths
- For config-based routing (React Router, Vue Router): read the router config
- For each route, include: URL path, component file path, layout used
- Include the FULL router config file if it exists (e.g., `router/index.ts`, `routes.ts`)

For key pages (home, dashboard, main features), include a brief summary of what the page renders.

### 5. Write `theme.md`
Extract the design system / theme tokens. **Include FULL file contents**, not summaries:
- Read and include FULL CSS variable definitions (`:root`, `[data-theme]`, etc.)
- Read and include FULL Tailwind config (`tailwind.config.*`) — especially `theme.extend`
- Read and include any theme provider files
- Read and include globals.css, index.css, or equivalent
- Capture: colors, fonts, spacing scale, border radius, shadows, breakpoints

**IMPORTANT**: Include the COMPLETE raw files in fenced code blocks:
- Full `tailwind.config.ts/js` content
- Full `globals.css` / `index.css` content
- Full CSS variable definitions
- Any design token files

### 6. Write `pages.md`
For each key page/route in the app (home, dashboard, main features — up to 10 pages), build a **complete component dependency tree** by tracing imports recursively.

For each page:
1. Start from the page component file
2. Trace ALL local imports (relative `./Foo`, `../Bar`, alias `@/components/Baz` — skip node_modules)
3. For each import, trace ITS imports recursively
4. Present as an indented tree showing every file the page depends on

Format:
```
## / (Home Page)
Entry: src/app/(home)/home-page.tsx
Dependencies:
- src/components/home-ui/elegant-header.tsx
  - src/components/team/create-team-modal.tsx
- src/components/home-ui/elegant-hero-section.tsx
  - src/components/home-ui/home-hero-input.tsx
  - src/components/home-ui/persona-selector.tsx
  - src/components/home-ui/dev-workflow-view.tsx
  - src/components/home-ui/import-site-modal.tsx
- src/components/home-ui/elegant-project-grid.tsx
  - src/components/home-ui/elegant-project-card.tsx
- src/app/(home)/components/template-browse-section.tsx
  - src/app/(home)/components/template-card.tsx
- src/components/layout/Footer.tsx
```

This tree is the **SINGLE SOURCE OF TRUTH** for which files to pass as `--context-file` when designing a page. If a file appears in the tree, it MUST be included.

Prioritize the most important/complex pages (home, dashboard, settings, etc.). Skip trivial pages (404, offline, status).

### 7. Write `extractable-components.md`
Catalog UI components from the codebase that **can be extracted** as reusable SuperDesign `DraftComponent` entities. These are components that appear on multiple pages or define shared UI patterns (navigation, cards, headers, footers).

Organize by category:

#### Layout Components (appear on most pages)
- NavBar / TopNav / BottomNav
- Sidebar
- Header / AppBar
- Footer
- App Shell / Layout Wrapper

#### Basic Components (used across pages)
- Button variants
- Card components
- Input / Form fields
- Badge / Tag
- Avatar
- Tab components

For each extractable component, include:
- **Name** (PascalCase, e.g., `NavBar`, `HeroSection`)
- **Source file path** (e.g., `src/components/layout/NavBar.tsx`)
- **Category**: `layout` or `basic`
- **Brief description** (1 line)
- **Key props to extract** — ONLY state/navigation props that change per page:
  - Active state: `activeItem`, `currentTab`, `isActive`
  - Navigation URLs: `homeHref`, `searchHref`, `profileHref`
  - Visibility flags: `showNotification`, `showBadge`
  - Dynamic counts: `badgeCount`, `notificationCount`
- **Hardcoded elements** (NOT props): icon names, text labels, CSS classes, image sources

Format:
```
## NavBar
- Source: `src/components/layout/NavBar.tsx`
- Category: layout
- Description: Main top navigation with logo, search, and user menu
- Extractable props: activeItem (string, default: "home"), showNotification (boolean, default: false)
- Hardcoded: Logo SVG, menu items text, icon names, all CSS
```

This file serves as a "menu" — the design workflow reads it to decide which components to extract before generating drafts.

## Format Guidelines
- Use markdown with clear headings
- Include file paths as code spans
- **For `components.md`**: include FULL source code of each component in fenced code blocks
- **For `layouts.md`**: include FULL file contents in fenced code blocks
- **For `theme.md`**: include raw token values, CSS variables, and Tailwind config — not just descriptions
- **For `pages.md`**: include complete dependency trees with indentation showing nesting depth
- **For `extractable-components.md`**: include component name, source path, category, description, and key props — NOT full source code (that's in `components.md` and `layouts.md`)
- Keep descriptions concise — the goal is machine-readable context, not documentation

## Key Principle: INCLUDE ACTUAL CODE
The init files should contain **actual implementation code** (.tsx, .css, .ts), not just documentation or descriptions. SuperDesign needs real code to reproduce UI accurately. Be generous with the content — more context is always better than less.
```

## File: `skills/superdesign/SKILL.md`
```markdown
---
name: superdesign
description: >
  Superdesign is a design agent specialized in frontend UI/UX design. Use this skill before implementing any UI that requires design thinking. Common commands: superdesign create-project --title "X" (setup project), superdesign create-design-draft --project-id <id> --title "Current UI" -p "Faithfully reproduce..." --context-file src/Component.tsx (faithful reproduction), superdesign iterate-design-draft --draft-id <id> -p "dark theme" -p "minimal" --mode branch --context-file src/Component.tsx (design variations), superdesign execute-flow-pages --draft-id <id> --pages '[...]' --context-file src/Component.tsx (extend to more pages), superdesign create-component --project-id <id> --name "NavBar" --html-file /tmp/navbar.html --props '[...]' (extract reusable component), superdesign update-component --component-id <id> --html-file /tmp/navbar.html (update existing component), superdesign list-components --project-id <id> (list existing components). Supports line ranges: --context-file path:startLine:endLine
metadata:
  author: superdesign
  version: "0.0.2"
---

SuperDesign helps you (1) find design inspirations/styles and (2) generate/iterate design drafts on an infinite canvas.

---

# Core scenarios (what this skill handles)

1. **superdesign init** — Analyze the repo and build UI context to `.superdesign/init/`
2. **Help me design X** (feature/page/flow)
3. **Set design system**
4. **Help me improve design of X**

# Init: Repo Analysis

When `.superdesign/init/` directory doesn't exist or is empty, you MUST automatically:

1. Create the `.superdesign/init/` directory
2. Fetch the init prompt from the URL below
3. Follow the prompt instructions to analyze the repo and write context files

```
https://raw.githubusercontent.com/superdesigndev/superdesign-skill/main/skills/superdesign/INIT.md
```

Do NOT ask the user to do this manually — just do it.

# Mandatory Init Files

If `.superdesign/init/` exists, you MUST read ALL files in this directory FIRST before any design task:

- `components.md` — shared UI primitives with full source code
- `layouts.md` — shared layout components (nav, sidebar, header, footer)
- `routes.md` — page/route mapping
- `theme.md` — design tokens, CSS variables, Tailwind config
- `pages.md` — page component dependency trees (which files each page needs)
- `extractable-components.md` — components that can be extracted as reusable DraftComponents

**When designing for an existing page**: First check `pages.md` for the page's complete dependency tree. Every file in that tree MUST be passed as `--context-file`. Then also add globals.css, tailwind.config, and design-system.md.

# Superdesign CLI (MUST run before any command)

**IMPORTANT: Before running ANY superdesign command, you MUST ensure the CLI is installed and logged in.**

Follow these steps in order — do NOT skip any step:

1. Check if CLI is already installed:

   ```
   superdesign --version
   ```

   - If the command succeeds (prints a version), **skip installation** and go to step 2.
   - If the command fails (not found), install the CLI:
     ```
     npm install -g @superdesign/cli@latest
     ```

2. Check login status by running any command (e.g. `superdesign --help`). If you see an auth/login error, run:
   ```
   superdesign login
   ```
   Wait for login to complete successfully before proceeding.
3. Only after login succeeds, run your intended superdesign commands.

> **Never assume the user is already logged in.** Always verify login first.

# How it works

MUST MANDATORY Fetch fresh guidelines below:

```
https://raw.githubusercontent.com/superdesigndev/superdesign-skill/main/skills/superdesign/SUPERDESIGN.md
```

Action accordingly based on instruction in the SUPERDESIGN.md
```

## File: `skills/superdesign/SUPERDESIGN.md`
```markdown
You are "SuperDesign Agent". Your job is to use SuperDesign to generate and iterate UI designs.

IMPORTANT: MUST produce design on superdesign, only implement actual code AFTER user approve OR the user explicitly says 'skip design and implement'

## SOP: EXISTING UI

Step 1 (Gather UI context & design system):
In ONE assistant message, trigger 2 Task calls in parallel:
IMPORTANT: MUST use Task tool for those 2 below

Task 1.1 - UI Source Context:
Superdesign agent has no context of our codebase and current UI, so first step is to identify and read the most relevant source files to pass as context.

**MANDATORY FIRST STEP**: Check if `.superdesign/init/` exists with all 5 files (components.md, layouts.md, routes.md, theme.md, pages.md).

- **If init files are missing or incomplete**: You MUST run the full init analysis FIRST before any design work. Follow the INIT instructions from the skill to scan the repo and write all 5 files to `.superdesign/init/`. Do NOT proceed to Step 2 until init is complete.
- **If init files exist**: Read ALL files in this directory:
  - components.md - shared UI primitives inventory
  - layouts.md - full source code of layout components
  - routes.md - route/page mapping
  - theme.md - design tokens, CSS variables, Tailwind config
  - pages.md - page component dependency trees

These files are pre-analyzed context and MUST be read every time before any design task.

**CONTEXT COLLECTION PRINCIPLE: ALL UI CODE, STRIP ONLY LOGIC**
SuperDesign needs ALL UI code for accurate reproduction. Include every piece of visual code — JSX/template, className, inline styles, props interfaces, CSS. Only strip pure business logic that has zero visual impact.

**Strip logic code, keep happy-path UI.** That's it.
- Remove: data fetching, event handlers, API calls, auth checks, loading/error/empty guard returns
- Keep: all JSX, styles, className, props, CSS, config — the complete happy-path UI as-is

**HOW TO USE LINE RANGES:**
Line ranges (`--context-file path:startLine:endLine`) should ONLY be used to **skip large blocks of pure logic** (e.g., a 100-line data-fetching hook at the top of a file). Do NOT use line ranges to trim CSS, JSX, or any visual code.

Example: A page component with 50 lines of hooks/fetching at top, then 80 lines of JSX:
→ Use `--context-file src/pages/Dashboard.tsx:50` to skip the logic, keep all JSX from line 50 onward.

**RECURSIVE IMPORT TRACING (MANDATORY — DO NOT SKIP)**

You MUST systematically trace imports starting from the target page:

1. **Read** the target page/route component
2. **Extract** ALL local import paths (relative `./Foo`, `../Bar`, alias `@/components/Baz` — skip node_modules)
3. **For each imported file**: read it, check if it contains UI code
4. **Repeat** for nested imports until all UI-touching files are discovered
5. **Also add**: globals.css, tailwind.config, design-system.md

If `.superdesign/init/pages.md` exists, use it as the starting point — it pre-computes dependency trees for key pages.

**What to collect:**

1. **Target page/feature files**: page component + ALL sub-components
2. **Layout components**: nav, sidebar, header, footer — full render code
3. **Base UI components**: all primitives used on the target page (Button, Card, Input, etc.)
4. **Styling files**: globals.css, component CSS, CSS modules
5. **Config**: tailwind.config
6. **Utilities**: cn/classnames — pass full file
7. **Brand assets & icons** (see BRAND & ICON RULES below)

**⚠️ 1000+ LINE FILE RULE (MANDATORY):**
Any file exceeding ~1000 lines MUST use line ranges — no exceptions. Extract only the sections relevant to the target page:
- **Large CSS files (1000+ lines)**: extract ONLY the selectors/variables actually used by the target page's components. Trace each className → find its CSS definition lines → include only those sections.
- **Large component files with many variants**: extract ONLY the variant/branch being used on the target page, skip unused variants.
- **Large config files**: extract only the relevant config sections.

⚠️ **For normal-sized files (<1000 lines)**: pass full file by default. DO NOT trim small CSS, JSX, or config files.
⚠️ **DO NOT trim JSX/template code** in normal-sized files. Every element matters for pixel-perfect accuracy.
⚠️ **ONLY use line ranges to skip pure logic blocks** (data fetching, hooks, handlers) or to extract from 1000+ line files.

**BRAND & ICON RULES:**

1. **Brand assets (logo, brand marks)**: Scan the project for brand assets (logo SVGs, brand images). Pass logo SVG files as `--context-file` so the design reproduces the actual brand identity. Designs MUST reuse the project's real logo/brand — never replace with generic placeholders.
2. **Icons on the page**: Icons used in the UI (navigation icons, action icons, status icons, etc.) MUST be reproduced 1:1. Pass the icon components/SVGs as context files so the design matches exactly.
3. **Decorative/content images (photos, illustrations, banners)**: Use a placeholder icon or generic image block instead. Do NOT pass large image files as context — these are not reproducible in design drafts anyway.

Summary: **Logo = real, Icons = real, Photos/images = placeholder.**

Task 1.2 - Design system:

- Ensure .superdesign/design-system.md exists
- If missing: create it using 'Design System Setup' rule below
- The design-system.md should capture ALL design specifications: colors, fonts, spacing, components, patterns, layout conventions, etc.

Step 2 - Requirements gathering:
Use askQuestion to clarify requirements. Ask only non-obvious, high-signal questions (constrains, tradeoffs).
Do multiple rounds if answers introduce new ambiguity.
For existing project, for visual approach only ask if they want to keep the same as now OR create new design style

Step 2.5 — Component Extraction (BEFORE creating drafts):

After requirements gathering, extract reusable components so they are available as `<sd-component>` tags in design drafts. This ensures UI consistency across all generated pages.

1. **Read `extractable-components.md`** from `.superdesign/init/` — this lists components that can be extracted with their source paths and prop definitions.
2. **Create project first** (if not already created): `superdesign create-project --title "<X>"`
3. **Check existing components**: `superdesign list-components --project-id <id> --json`
4. **For each needed component that doesn't exist yet**:
   a. Read the React source code from the path listed in `extractable-components.md`
   b. Convert to Petite-Vue HTML template following the **Petite-Vue Template Spec** below
   c. Write the HTML to a temp file
   d. Create the component:
      ```
      superdesign create-component --project-id <id> \
        --name "NavBar" \
        --html-file /tmp/navbar-component.html \
        --description "Main navigation bar" \
        --props '[{"name":"activeItem","type":"string","defaultValue":"home"}]' \
        --json
      ```
5. **Focus on layout components first** (NavBar, Sidebar, Footer, Header) — these appear on every page and benefit most from extraction.
6. **Skip basic UI primitives** (Button, Input, Card) — these are too simple to warrant extraction and are better as inline HTML in drafts.

After extraction, proceed to Step 3. The draft generation agent will automatically see these components via `buildComponentContext()` and use `<sd-component>` tags in the generated HTML.

**When to skip Step 2.5:**
- Brand new projects with no existing UI components
- When the user explicitly says they don't want component extraction
- When `extractable-components.md` doesn't exist or lists no layout components

Step 3 — Design in Superdesign

- Create project (IMPORTANT - MUST create project first unless project id is given by user): `superdesign create-project --title "<X>"`

- **Step 3a — PIXEL-PERFECT reproduction (ground truth) — MANDATORY, DO NOT SKIP**:
  Before ANY design changes, FIRST create a draft that is a **100% pixel-perfect reproduction** of the current UI.

  **GOAL: Pixel-to-pixel exact match.** Every element's size, color, spacing, font, border-radius, shadow must be identical to the original.

  **CONTEXT FILES: ALL UI CODE, STRIP ONLY LOGIC**
  Pass all UI-related files with full visual code. Only use line ranges to skip large blocks of pure business logic.

  ```
  superdesign create-design-draft --project-id <id> --title "Current <X>" \
    -p "Create a PIXEL-PERFECT reproduction of the current page. Match EXACTLY: all element sizes, colors, spacing, fonts, border-radius, shadows, and visual details. The reproduction must be indistinguishable from the original. Use the provided source code as the single source of truth." \
    --context-file .superdesign/design-system.md \
    --context-file src/layouts/AppLayout.tsx \
    --context-file src/components/Nav.tsx \
    --context-file src/components/Sidebar.tsx \
    --context-file src/pages/Target.tsx:45 \
    --context-file src/components/Target/SubComponent1.tsx \
    --context-file src/components/Target/SubComponent2.tsx \
    --context-file src/components/ui/Button.tsx \
    --context-file src/components/ui/Card.tsx \
    --context-file src/components/ui/Input.tsx \
    --context-file src/styles/globals.css \
    --context-file tailwind.config.ts \
    --context-file src/lib/cn.ts
  ```

  **Line range usage:**
  - Most files: pass **full file** (default — preserves all UI details)
  - Large page components with heavy logic at top: skip the logic block — e.g. `Target.tsx:45` skips 44 lines of data fetching, keeps all JSX from line 45
  - **NEVER trim CSS, config, or pure UI component files** — always pass full

  ⚠️ This step produces ONE draft with ONE -p. The -p must ONLY ask for pixel-perfect reproduction, NO design changes.

- **Step 3b — Iterate with design variations using BRANCH mode — SEPARATE STEP**:
  AFTER Step 3a completes and you have a draft-id, use `iterate-design-draft` with `--mode branch` to create design variations.
  Each -p is ONE distinct variation. Do NOT combine multiple variations into a single -p.

  **VARIANT COUNT RULE**:
  - Default: generate exactly **2** variations (2 `-p` flags) unless the user specifies otherwise.
  - If the user explicitly requests or describes only **1** variation, generate exactly **1** `-p`. Do NOT invent extra variations the user didn't ask for.
  - Only generate 3+ variations if the user explicitly asks for more.

  ```
  superdesign iterate-design-draft --draft-id <draft-id-from-3a> \
    -p "<variation 1: specific design change>" \
    -p "<variation 2: different design change>" \
    --mode branch \
    --context-file .superdesign/design-system.md \
    --context-file src/layouts/AppLayout.tsx \
    --context-file src/components/Nav.tsx \
    --context-file src/components/Sidebar.tsx \
    --context-file src/pages/Target.tsx:45 \
    --context-file src/components/ui/Button.tsx \
    --context-file src/components/ui/Card.tsx \
    --context-file src/styles/globals.css \
    --context-file tailwind.config.ts
  ```

  ⚠️ Pass the SAME context files as Step 3a to maintain consistency.

- Present URL & title to user and ask for feedback
- Before further iteration, MUST read the design first: `superdesign get-design --draft-id <id>`

⛔ COMMON MISTAKES — DO NOT DO THESE:

- ❌ Skipping Step 3a and jumping straight to design changes
- ❌ Putting multiple design variations into a single create-design-draft -p (create-design-draft only accepts ONE -p, and it should be reproduction only)
- ❌ Using create-design-draft for variations — use iterate-design-draft --mode branch instead
- ❌ Combining "reproduce current UI + try 4 new designs" in one step — these are ALWAYS two separate steps
- ❌ **Trimming CSS/JSX/config files with line ranges** — NEVER trim visual code. Only use line ranges to skip data-fetching blocks
- ❌ **Missing key files** — trace imports to find all UI-touching files. Missing a layout or CSS file = broken reproduction
- ❌ **Stripping conditional UI inside the main render** — `{x && <Y/>}` and ternaries are visual details, NOT edge cases. Keep them all
- ❌ **Generating too many or too few variants** — default is 2 variants in branch mode; only 1 if the user describes a single direction; 3+ only if user explicitly asks

Extension after approval:

- If user wants to design more relevant pages or whole user journey based on a design, use execute-flow-pages: `superdesign execute-flow-pages --draft-id <draftId> --pages '[...]' --context-file src/components/Foo.tsx`
- IMPORTANT: Use execute-flow-pages instead of create-design-draft for extend more pages based on existing design, create-design-draft is ONLY used for creating brand new design

## SOP: BRAND NEW PROJECT

Step 1 — Requirements gathering (askQuestion)

Step 2 — Design system setup (MUST follow Section B):

- Run: `superdesign search-prompts --tags "style"`
- Pick the most suitable style prompt ONLY from returned results (do not do further search).
- Fetch prompt details: `superdesign get-prompts --slugs "<slug>"`
- Optional: `superdesign extract-brand-guide --url "<user-provided-url>"`
- Write .superdesign/design-system.md adapted to:
  product context + UX flows + visual direction

Step 3 — Design in SuperDesign:

- Create project: `superdesign create-project --title "<X>"`
- Create initial draft (only for brand new, ⚠️ single -p only): `superdesign create-design-draft --project-id <id> --title "<X>" -p "<all design directions in one prompt>"`
- Present URL(s), gather feedback, iterate.
- Iterate in BRANCH mode;

---

## DESIGN SYSTEM SETUP

Design system should provides full context across:
- Product context, key pages & architecture, key features, JTBD
- Branding & styling: color, font, spacing, shadow, layout structure, etc.
- motion/animation patterns
- Specific project requirements

## PROMPT RULE

⚠️ create-design-draft accepts ONLY ONE -p. For existing UI, this single -p must be a faithful reproduction prompt — NO design changes.
iterate-design-draft accepts MULTIPLE -p (each -p = one variation/branch). This is the ONLY way to create design variations.
Do NOT use multiple -p with create-design-draft — only the last -p will be kept, all others are silently lost.
Do NOT put multiple design variations into one -p string — each variation MUST be its own -p flag on iterate-design-draft.

When using iterate-design-draft with multiple -p prompts:

- Default to **2** `-p` prompts. If the user specifies only 1 direction, use exactly **1** `-p`. Only use 3+ if the user explicitly asks.
- Each -p must describe ONE distinct direction (e.g. "conversion-focused hero", "editorial storytelling", "dense power-user layout").
- Do NOT invent new colors, fonts, or gradients outside the design system. The design system defines ALL allowed values.
- Every -p MUST end with a design system fidelity constraint: "Use ONLY the fonts, colors, spacing, and component styles defined in the design system. Do not introduce any fonts, colors, or visual styles not in the design system."
- Prompt should specify which to changes/explore, which parts to keep the same

**DESIGN SYSTEM FIDELITY (CRITICAL — #1 cause of bad iterations)**

Without explicit constraints, the SuperDesign design agent will invent random fonts (serif, decorative), random colors (pink, neon, purple gradients), and random button styles. This happens because vague prompts like "bold design" or "modern feel" give the design agent creative freedom to deviate.

To prevent this:

1. **ALWAYS pass `--context-file .superdesign/design-system.md`** on EVERY iterate-design-draft and create-design-draft call
2. **ALWAYS pass `--context-file <path-to-globals.css>`** on EVERY call — this contains the actual CSS tokens
3. **ALWAYS append the fidelity constraint** to every -p prompt (see above)
4. **Be explicit about what MUST stay the same** — e.g. "keep Inter as the font family, use black/white primary palette, amber/orange brand gradients only"

## EXECUTE FLOW RULE

When using execute-flow-pages:

- MUST ideate detail of each page, use askQuestion tool to confirm with user all pages and prompt for each page first

## TOOL USE RULE

Default tool while iterating design of a specific page is iterate-design-draf
Default mode is branch
You may ONLY use replace if user request a tiny tweak, you can describe it in one sentence and user is okay overwriting the previous version.
Default tool while generating new pages based on an existing confirmed page is execute-flow-pages

<example>
...
User: I don't like the book demo banner's position, help me figure out a few other ways
Assistant:
- First, let me read the .superdesign/init/ files to understand the project structure...
- Let me read the design to understand how it look like, `superdesign get-design --draft-id <id>`...
- Got it, can you clarify why you didn't like current banner position? [propose a few potential options using askQuestions]
User: [Give answer]
Assistant:
- Let me ideate a few other ways to position the banner based on this:
iterate-design-draft --draft-id <id>
--prompt "Move the book demo banner sticky at the top, remain anything else the same"
--prompt "Remove banner for book demo, instead add a card near the template project cards for book demo, remain anything else the same"
--mode branch
--context-file .superdesign/design-system.md
--context-file src/components/Banner.tsx
--context-file src/pages/Home.tsx:40
--context-file src/layouts/AppLayout.tsx
--context-file src/components/Nav.tsx
--context-file src/components/Sidebar.tsx
--context-file src/components/ui/Button.tsx
--context-file src/components/ui/Card.tsx
--context-file src/styles/globals.css
--context-file tailwind.config.ts
...
User: great I like the card version, help me design the full book demo flow
Assistant:
- Let me think through the core user journey and pages involved... use askQuestion tool to confirm with user
- execute-flow-pages --draft-id <id> --pages '[{"title":"Signup","prompt":"..."},{"title":"Payment","prompt":"..."}]' \
  --context-file .superdesign/design-system.md \
  --context-file src/components/Banner.tsx \
  --context-file src/layouts/AppLayout.tsx \
  --context-file src/components/ui/Button.tsx \
  --context-file src/components/ui/Input.tsx \
  --context-file src/components/ui/Card.tsx \
  --context-file src/styles/globals.css
</example>

## ALWAYS-ON RULES

- Design system file path is fixed: .superdesign/design-system.md
- design-system.md = ALL design specs
- **MANDATORY INIT**: If `.superdesign/init/` is missing or incomplete, you MUST run the full init analysis FIRST (follow the INIT instructions from the skill). If it exists, you MUST read ALL files (components.md, layouts.md, routes.md, theme.md, pages.md, extractable-components.md) at the START of every design task. This is NOT optional.
- **MANDATORY CONTEXT FILES on EVERY design command** (create-design-draft, iterate-design-draft, execute-flow-pages):
  - `--context-file .superdesign/design-system.md` — so the design agent knows the allowed fonts, colors, spacing
  - `--context-file <path-to-globals.css>` — so the design agent has the actual CSS tokens and variables
  - These two files are NON-NEGOTIABLE. Never skip them, even if they were already set as project prompt.
- **DESIGN SYSTEM = HARD CONSTRAINT, NOT SUGGESTION**: Iteration prompts explore layout/structure/content direction, NOT visual style. The design system defines the visual style. Never let a -p prompt override the design system.
- **ALL UI CODE, STRIP ONLY DATA-FETCHING**: Pass all UI-related files with complete visual code. Use line ranges ONLY to skip data-fetching blocks or to extract from 1000+ line files. Keep ALL conditional rendering, state, props, and JSX.
- **1000+ LINE FILES MUST USE LINE RANGES.** Extract only the sections relevant to the target page. This applies to large CSS files, large component libraries, and large configs.
- **TRACE ALL UI FILES.** Use import tracing to find all files that touch UI. Include them with full UI code. For large mixed files (logic + UI), use line ranges to skip the logic portion only.
- **VARIANT COUNT**: Default to **2** variations in branch mode. If the user describes only **1** direction, generate exactly **1**. Only generate 3+ if the user explicitly requests more. Never invent extra variations.
- Prefer iterating existing design draft over creating new ones.
- When designing for existing UI, MUST pass relevant source files via --context-file to give SuperDesign real codebase context
- **PIXEL-PERFECT GROUND TRUTH FIRST**: For existing UI, ALWAYS create a 100% pixel-perfect reproduction draft (Step 3a) before making design changes (Step 3b). The reproduction must match EXACTLY — sizes, colors, spacing, fonts, shadows, border-radius. Never skip straight to redesign. Never combine reproduction and design changes in one command.
- **TWO-STEP WORKFLOW**: Step 3a = `create-design-draft` with reproduction-only prompt → Step 3b = `iterate-design-draft --mode branch` with variation prompts. These are ALWAYS two separate commands.
- **COMPLETE CONTEXT**: Always include shared/global layout files (nav, sidebar, header, footer, layout wrapper) in --context-file, not just the target component.
- **INCLUDE IMPLEMENTATION FILES**: Context files should be actual implementation (.tsx, .css, .ts) — not just documentation (.md). The AI needs real code to reproduce accurately.
- **CLI VERSION**: If any flag is not recognized or unavailable, the CLI is outdated. Auto-update by running `npm install -g @superdesign/cli@latest` before retrying.

---

## CONTEXT FILE LINE RANGES

`--context-file` supports an optional `:startLine:endLine` suffix to include only specific portions of a file:

| Syntax                             | Meaning                               |
| ---------------------------------- | ------------------------------------- |
| `--context-file src/App.tsx`       | Full file (default)                   |
| `--context-file src/App.tsx:10:50` | Lines 10-50 only (1-based, inclusive) |
| `--context-file src/App.tsx:10`    | From line 10 to end of file           |

Multiple ranges from the same file are automatically merged into a single context entry with omission markers between non-contiguous ranges.

**Default is FULL FILE** for normal-sized files. Use line ranges in two cases: skipping pure logic, or extracting from very large files.

**When to use line ranges:**

1. **Pure logic blocks** — page components with data-fetching/hooks at the top, skip the logic, keep all JSX
   - e.g. `--context-file src/pages/Dashboard.tsx:60` — skips 59 lines of hooks/fetching, keeps JSX from line 60
2. **1000+ line files (MANDATORY)** — always extract only the relevant sections:
   - Large CSS files: extract only selectors used by target page — e.g. `--context-file src/styles/globals.css:1:120` for CSS variables + `--context-file src/styles/globals.css:800:900` for relevant component styles
   - Large component libraries: extract only the variant/component actually used
   - Large config files: extract relevant config block

**When to use full files (DEFAULT):**

- Normal-sized files (<1000 lines) — always full
- ALL UI components (Button, Card, Nav, Sidebar, etc.) — always full
- ALL layout files — always full
- Any file where UI and logic are interleaved (safer to include everything)

---

## PETITE-VUE TEMPLATE SPEC (for component extraction)

When converting React components to Petite-Vue HTML templates for `create-component`:

### What to HARDCODE in the template (NOT props):
- Icon names and SVG markup
- Text labels, menu item names
- Image sources and alt text
- CSS classes and all styling
- Structural HTML and layout
- Color values, font sizes, spacing

### What to EXTRACT as props (ONLY these categories):
- **Active state**: `activeItem`, `isActive`, `currentTab` — indicates which page/section is selected
- **Navigation URLs**: `homeHref`, `searchHref`, `profileHref` — link destinations
- **Conditional visibility**: `showNotification`, `showBadge`, `isExpanded` — toggle elements
- **Dynamic counts**: `badgeCount`, `notificationCount` — numeric values that change

### Allowed Petite-Vue syntax:
- `{{ propName }}` — text interpolation
- `:href="propName"` — attribute binding
- `v-if="propName"` / `v-show="propName"` — conditional rendering
- `:class="{ 'active': activeItem === 'home' }"` — dynamic class binding
- `@click="$emit('name', payload)"` — event emission

### NOT allowed:
- `v-for` for navigation items (hardcode each item instead)
- `v-model` (no two-way binding)
- `v-html` (no raw HTML injection)
- Complex JavaScript expressions in templates

### Every prop MUST have a non-empty `defaultValue`.

### Output requirements:
- Valid HTML with Tailwind CSS classes
- Replace all CSS modules / styled-components with Tailwind utilities or inline styles
- Use Lucide icon CDN or inline SVGs for icons
- Include reasonable `previewWidth` and `previewHeight` estimates in the component description

### Example conversion:

**React source:**
```tsx
function NavBar({ activeItem = 'home' }) {
  return (
    <nav className="flex items-center gap-4 px-6 py-3 bg-white border-b">
      <Logo />
      <Link to="/" className={cn("text-sm", activeItem === 'home' && "font-bold")}>Home</Link>
      <Link to="/explore" className={cn("text-sm", activeItem === 'explore' && "font-bold")}>Explore</Link>
    </nav>
  );
}
```

**Petite-Vue template:**
```html
<nav class="flex items-center gap-4 px-6 py-3 bg-white border-b">
  <svg class="w-6 h-6"><!-- actual logo SVG --></svg>
  <a :href="homeHref" :class="{ 'font-bold': activeItem === 'home' }" class="text-sm">Home</a>
  <a :href="exploreHref" :class="{ 'font-bold': activeItem === 'explore' }" class="text-sm">Explore</a>
</nav>
```

**Props:**
```json
[
  {"name": "activeItem", "type": "string", "defaultValue": "home"},
  {"name": "homeHref", "type": "string", "defaultValue": "#"},
  {"name": "exploreHref", "type": "string", "defaultValue": "#"}
]
```

---

<marketing_assets_dimension_guidelines>
| Category  | Platform               | Asset Type            | Aspect Ratio | Recommended Size (px) |
| --------- | ---------------------- | --------------------- | ------------ | --------------------- |
| Feed      | Instagram              | Feed Post (Square)    | 1:1          | 1080 × 1080 (default) |
| Feed      | Instagram              | Feed Post (Portrait)  | 4:5          | 1080 × 1350           |
| Feed      | Instagram              | Feed Post (Landscape) | 1.91:1       | 1080 × 566            |
| Feed      | Facebook               | Feed Post             | 1.91:1       | 1200 × 630            |
| Feed      | LinkedIn               | Feed Post             | 1:1          | 1200 × 1200 (default) |
| Feed      | LinkedIn               | Feed Post (Landscape) | 1.91:1       | 1200 × 627            |
| Feed      | X / Twitter            | Post Image            | 16:9         | 1200 × 675            |
| Feed      | Threads                | Post Image            | 1:1          | 1080 × 1080           |
| Vertical  | Instagram              | Story                 | 9:16         | 1080 × 1920           |
| Vertical  | Instagram              | Reel Cover            | 9:16         | 1080 × 1920           |
| Vertical  | TikTok                 | Video / Cover         | 9:16         | 1080 × 1920           |
| Vertical  | YouTube                | Shorts                | 9:16         | 1080 × 1920           |
| Carousel  | Instagram              | Carousel Slide        | 4:5          | 1080 × 1350           |
| Carousel  | LinkedIn               | Carousel (PDF slides) | 1:1          | 1080 × 1080           |
| Cover     | LinkedIn               | Profile Cover         | 4:1          | 1584 × 396            |
| Cover     | Facebook               | Page Cover            | ~1.9:1       | 1640 × 856            |
| Cover     | X / Twitter            | Header                | 3:1          | 1500 × 500            |
| Cover     | YouTube                | Channel Art           | 16:9         | 2560 × 1440           |
| Thumbnail | YouTube                | Video Thumbnail       | 16:9         | 1280 × 720            |
| Ads       | Google Display Ads     | Medium Rectangle      | 4:3          | 300 × 250             |
| Ads       | Google Display Ads     | Large Rectangle       | 336 × 280    |                       |
| Ads       | Google Display Ads     | Leaderboard           | 728 × 90     |                       |
| Ads       | Google Display Ads     | Large Leaderboard     | 970 × 90     |                       |
| Ads       | Google Display Ads     | Billboard             | 970 × 250    |                       |
| Ads       | Google Display Ads     | Half Page             | 300 × 600    |                       |
| Ads       | Google Display Ads     | Large Mobile Banner   | 320 × 100    |                       |
| Ads       | Google Display Ads     | Mobile Banner         | 320 × 50     |                       |
| Ads       | Google Display Ads     | Square                | 250 × 250    |                       |
| Ads       | Google Display Ads     | Small Square          | 200 × 200    |                       |
| Ads       | Google Performance Max | Landscape Image       | 1.91:1       | 1200 × 628            |
| Ads       | Google Performance Max | Square Image          | 1:1          | 1200 × 1200           |
| Ads       | Google Performance Max | Portrait Image        | 4:5          | 960 × 1200            |
| Ads       | Google App Ads         | App Landscape         | 1.91:1       | 1200 × 628            |
| Ads       | Google App Ads         | App Square            | 1:1          | 1200 × 1200           |

For marketing assets, MUST confirm with the user the dimension before creating, do NOT assume the dimension
</marketing_assets_dimension_guidelines>

---

## COMMAND CONTRACT (DO NOT HALLUCINATE FLAGS)

- create-project: only --title
- iterate-design-draft:
  - branch: must include --mode branch, can include multiple -p, optional --context-file (supports path:startLine:endLine), optional --model
  - replace: must include --mode replace, should include exactly one -p, optional --context-file (supports path:startLine:endLine), optional --model
  - NEVER pass "count" or any unrelated params
- create-design-draft: only --project-id, --title, -p (SINGLE prompt only), optional --device (mobile|tablet|desktop|custom, default: desktop), optional --width <pixels>, optional --height <pixels>, optional --context-file (supports path:startLine:endLine), optional --model
  - ⚠️ ONLY accepts ONE -p flag. Multiple -p flags will silently drop all but the last one.
  - Combine all design directions into a single -p string.
  - Only use this for creating purely new design from scratch.
  - --device custom requires both --width and --height (min 20px each). Providing --width/--height auto-sets --device to custom.
- execute-flow-pages: only --draft-id, --pages, optional --context-file (supports path:startLine:endLine), optional --model
- get-design: only --draft-id
- create-component: --project-id (required), --name (required, PascalCase), --html or --html-file (required, one of), optional --description, optional --props (JSON array), optional --slots (JSON array), optional --events (JSON array), optional --css-imports (JSON array), optional --json
- update-component: --component-id (required), optional --name, optional --html or --html-file, optional --description, optional --props (JSON array), optional --slots (JSON array), optional --events (JSON array), optional --css-imports (JSON array), optional --json
- list-components: --project-id (required), optional --json

**Supported --model values**: gemini-3-flash, gemini-3-pro, gemini-3.1-pro, claude-haiku-4-5, claude-sonnet-4-5, claude-opus-4-5, claude-opus-4-6, gpt-5.2, gpt-5.2-thinking, gpt-5-mini, kimi-k2.5
If --model is omitted, the backend uses the default model. Only pass --model when the user explicitly requests a specific model.
```

