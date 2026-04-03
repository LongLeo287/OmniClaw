---
id: affitor-affiliate-skills-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:40.115278
---

# KNOWLEDGE EXTRACT: affitor-affiliate-skills
> **Extracted on:** 2026-03-30 17:29:02
> **Source:** affitor-affiliate-skills

---

## File: `.cursorrules`
```
# Affitor Affiliate Skills — Cursor Rules

## What This Repo Is
32 AI-powered skills for affiliate marketers. Each skill automates a specific workflow
(content creation, program research, SEO, outreach, analytics, etc.) using live data
from the Affitor API.

## How Skills Work
- Each skill lives in `skills/<stage>/<skill-name>/SKILL.md`
- `SKILL.md` is a self-contained instruction file: it defines inputs, workflow steps, and expected outputs
- Skills are designed to be chained — the output of one skill feeds the next
- Run a skill by reading its `SKILL.md` and executing the documented workflow

## Directory Layout
```
skills/          # Skills grouped by stage (research, content, blog, landing, distribution, analytics, automation, meta)
registry.json    # Master index of all 32 skills with metadata
API.md           # Full Affitor API reference
prompts/         # Bootstrap prompt for any AI
shared/
  references/    # Cross-skill reference docs (FTC rules, glossary, branding)
```

## Affitor API
- Base URL: `https://list.affitor.com/api/v1`
- Programs endpoint: `GET /programs`
- Key fields per program:
  - `reward_value` — commission amount or percentage
  - `reward_type` — "cps_recurring" | "cps_one_time" | "cps_lifetime" | "cpl" | "cpc"
  - `cookie_days` — attribution window in days
  - `stars_count` — community star count (popularity signal)
  - `slug`, `name`, `tags[]`, `url`, `description`
- Always fetch real data from the API. Never fabricate program details.

## Key Rules
1. **FTC disclosure required** — any content that promotes an affiliate program must include
   a clear disclosure ("I may earn a commission..."). See `shared/references/ftc-compliance.md`.
2. **Data from API, not guesses** — commission rates, cookie windows, and program names
   must come from live API responses.
3. **Portable output** — skill outputs must work standalone (markdown, plain text, CSV).
   No platform-specific formatting unless the skill explicitly targets one.
4. **Follow the SKILL.md workflow exactly** — each step is intentional. Don't skip steps.
5. **Chain outputs** — skills are composable. Pass structured output from one skill as
   input to the next when building multi-step workflows.

## Adding or Editing Skills
- Register new skills in `registry.json` (stage, name, description, inputs, outputs)
- Keep `SKILL.md` under 150 lines — concise instruction, not documentation
- Use frontmatter at the top of `SKILL.md` for metadata (stage, version, inputs, outputs)
```

## File: `.gitignore`
```
node_modules/
tools/dist/
*.log
.env
.env.local
```

## File: `API.md`
```markdown
# list.affitor.com API Reference

Public and authenticated access to the Affitor affiliate program directory.

- **Base URL:** `https://list.affitor.com/api/v1`
- **Format:** JSON (unless noted)
- **Last updated:** 2026-03-16

---

## Authentication

API keys are created at `https://list.affitor.com/settings` (requires a free account). Keys need the `programs:read` scope at minimum.

Pass the key in the `Authorization` header:

```
Authorization: Bearer afl_xxxxx
```

**Free tier (no key):** All endpoints work without authentication, but results are capped at **5 per request**. The response will include `"tier": "free"` and a notice message.

---

## Endpoints

### GET /programs

List and search published affiliate programs.

#### Query Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `q` | string | — | Full-text search on name and description (case-insensitive, partial match) |
| `type` | string | `affiliate_program` | Filter by type: `affiliate_program` or `skill` |
| `sort` | string | `trending` | Sort order: `trending`, `new`, or `top` |
| `limit` | integer | `30` | Results per page. Maximum: `100`. Free tier: max `5`. |
| `offset` | integer | `0` | Pagination offset |
| `reward_type` | string | — | Filter by reward structure (see Reward Types below) |
| `tags` | string | — | Comma-separated tags to filter by. Matches programs tagged with ANY of the given tags. Example: `ai,video` |
| `min_cookie_days` | integer | — | Minimum cookie duration in days |

All parameters can be combined. Example — search for recurring AI tools with a 30-day minimum cookie:

```
GET /api/v1/programs?q=AI&reward_type=cps_recurring&min_cookie_days=30&sort=top&limit=10
```

#### Response

```json
{
  "data": [
    {
      "id": "3f2a1b4c-...",
      "slug": "heygen",
      "name": "HeyGen",
      "url": "https://heygen.com",
      "description": "AI video generation platform. Create studio-quality videos from text.",
      "reward_type": "cps_recurring",
      "reward_value": "30%",
      "reward_duration": "12 months",
      "cookie_days": 60,
      "stars_count": 42,
      "views_count": 1200,
      "comments_count": 5,
      "category": "ai-tools",
      "tags": ["ai", "video"],
      "type": "affiliate_program",
      "stage": null,
      "status": "published",
      "created_at": "2026-01-15T10:00:00.000Z",
      "profiles": {
        "handle": "sonpiaz",
        "avatar_url": "https://...",
        "name": "Son Piaz"
      }
    }
  ],
  "count": 1
}
```

**Free tier response** additionally includes:

```json
{
  "data": [...],
  "count": 5,
  "tier": "free",
  "message": "Free tier: max 5 results. Get an API key at list.affitor.com/settings for unlimited access."
}
```

#### Field Reference

| Field | Type | Notes |
|---|---|---|
| `id` | string (UUID) | Unique program identifier |
| `slug` | string | URL-friendly identifier, e.g. `heygen` |
| `name` | string | Display name |
| `url` | string \| null | Product website |
| `description` | string | Program description |
| `reward_type` | string \| null | Commission structure (see Reward Types) |
| `reward_value` | string \| null | Commission amount as a string, e.g. `"30%"` or `"$50"` |
| `reward_duration` | string \| null | Duration of recurring commissions, e.g. `"12 months"` |
| `cookie_days` | integer \| null | Cookie window in days |
| `stars_count` | integer | Community star count (popularity signal) |
| `views_count` | integer | Page view count |
| `comments_count` | integer | Number of comments |
| `category` | string \| null | Top-level category |
| `tags` | string[] \| null | Tag array for filtering |
| `type` | string | `affiliate_program` or `skill` |
| `status` | string | `published` for visible programs |
| `created_at` | string (ISO 8601) | Submission date |
| `profiles` | object | Submitter's public profile |

> **Field naming:** Use `reward_value`, `reward_type`, `cookie_days`, and `stars_count` exactly as shown. Do not substitute `commission_rate`, `upvotes`, or `cookie_duration` — those field names do not exist in the schema.

---

### GET /programs/:id

Retrieve a single program by UUID.

**Requires authentication** (`programs:read` scope).

#### Response

Returns the same `Program` object under a `data` key:

```json
{
  "data": { ...program object... }
}
```

Returns `404` if no program is found with the given ID.

---

### GET /skills/:slug/raw

Returns the raw Markdown content of a skill file as `text/plain`.

**Public — no authentication required.**

Example:

```
GET /api/v1/skills/affiliate-program-search/raw
```

---

## Reward Types

| Value | Meaning |
|---|---|
| `cpc` | Cost per click |
| `cpl` | Cost per lead |
| `cps_one_time` | One-time sale commission |
| `cps_recurring` | Recurring sale commission |
| `cps_lifetime` | Lifetime recurring commission |
| `other` | Non-standard structure |

---

## Error Responses

| HTTP Status | Meaning |
|---|---|
| `401 Unauthorized` | API key is invalid or malformed |
| `403 Forbidden` | API key lacks `programs:read` scope |
| `404 Not Found` | Program ID does not exist |
| `429 Too Many Requests` | Rate limit exceeded |

---

## Rate Limits

- **Authenticated:** 60 requests per minute per API key
- **Unauthenticated (free tier):** Lower limits apply; exact threshold not published
- Responses should be cached within a session to avoid redundant requests

---

## Code Examples

### curl

**Search with no API key (free tier):**

```bash
curl "https://list.affitor.com/api/v1/programs?q=AI+video&sort=top&limit=5"
```

**Authenticated search with filters:**

```bash
curl \
  -H "Authorization: Bearer afl_xxxxx" \
  "https://list.affitor.com/api/v1/programs?q=AI&reward_type=cps_recurring&min_cookie_days=30&sort=top&limit=20"
```

**Get a single program:**

```bash
curl \
  -H "Authorization: Bearer afl_xxxxx" \
  "https://list.affitor.com/api/v1/programs/3f2a1b4c-0000-0000-0000-000000000000"
```

---

### JavaScript / fetch

**Search programs:**

```js
async function searchPrograms(query, options = {}) {
  const url = new URL("https://list.affitor.com/api/v1/programs");

  if (query) url.searchParams.set("q", query);
  if (options.rewardType) url.searchParams.set("reward_type", options.rewardType);
  if (options.tags) url.searchParams.set("tags", options.tags.join(","));
  if (options.minCookieDays) url.searchParams.set("min_cookie_days", String(options.minCookieDays));
  if (options.sort) url.searchParams.set("sort", options.sort);
  if (options.limit) url.searchParams.set("limit", String(options.limit));
  if (options.offset) url.searchParams.set("offset", String(options.offset));

  const headers = { "Accept": "application/json" };
  if (process.env.AFFITOR_API_KEY) {
    headers["Authorization"] = `Bearer ${process.env.AFFITOR_API_KEY}`;
  }

  const res = await fetch(url.toString(), { headers });
  if (!res.ok) throw new Error(`API error: ${res.status}`);

  return res.json(); // { data: Program[], count: number, tier?: "free" }
}

// Usage
const result = await searchPrograms("AI video", {
  rewardType: "cps_recurring",
  minCookieDays: 30,
  sort: "top",
  limit: 10,
});

for (const program of result.data) {
  console.log(`${program.name} — ${program.reward_value} (${program.reward_type}), ${program.cookie_days}d cookie`);
}
```

**Get a single program by UUID:**

```js
async function getProgram(id) {
  const res = await fetch(`https://list.affitor.com/api/v1/programs/${id}`, {
    headers: {
      "Accept": "application/json",
      "Authorization": `Bearer ${process.env.AFFITOR_API_KEY}`,
    },
  });
  if (res.status === 404) return null;
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  const json = await res.json();
  return json.data;
}
```

---

## Fallback: Web Scraping

If you do not have an API key or the API is unavailable, program data can be extracted from list.affitor.com pages directly.

**Method:**

1. Search: `site:list.affitor.com [category or keyword]` using a web search tool
2. Fetch the relevant page with a web fetch tool
3. Parse the page content:
   - Program name from the card heading
   - Reward info: look for patterns like `"30% recurring"` or `"$50 one-time"`
   - Cookie duration: look for `"Xd"` or `"X day cookie"`
   - Stars: star icon followed by a number
   - Description: paragraph text below the program name

**Program detail page format:** `https://list.affitor.com/@[handle]/[slug]`

Example: `https://list.affitor.com/@sonpiaz/heygen`

---

## Getting an API Key

1. Sign up (free) at [list.affitor.com](https://list.affitor.com)
2. Go to **Settings → API Keys**
3. Create a key with the `programs:read` scope
4. Set the environment variable: `AFFITOR_API_KEY=afl_xxxxx`

The free tier (no key) supports up to 5 results per request and is suitable for lightweight lookups.
```

## File: `CLAUDE.md`
```markdown
# Affiliate Skills by Affitor

32 AI-powered skills for affiliate marketers. Full funnel across 8 stages: Research, Content, Blog, Landing, Distribution, Analytics, Automation, Meta.

## Repo structure

- `skills/{stage}/{skill-name}/SKILL.md` — main skill file (stages: research, content, blog, landing, distribution, analytics, automation, meta)
- `skills/{stage}/{skill-name}/references/` — supplementary docs read by the skill
- `shared/references/` — cross-skill references (FTC, glossary, branding)
- `tools/src/` — `affiliate-check` CLI source (Bun persistent daemon)
- `tools/dist/affiliate-check` — compiled binary (gitignored, build with `bun build --compile tools/src/cli.ts --outfile tools/dist/affiliate-check`)
- `registry.json` — machine-readable index of all skills (auto-generated by `scripts/generate-registry.js`)
- `evals/` — test cases
- `brain/knowledge/docs_legacy/` — contributor documentation

## CLI tool: affiliate-check

Persistent Bun daemon querying list.affitor.com API. Port 9500, 5min cache, 30min idle shutdown.

```bash
affiliate-check search "AI video"          # search programs
affiliate-check top                        # top by stars
affiliate-check info heygen                # detailed info
affiliate-check compare heygen synthesia   # side-by-side
affiliate-check status                     # server status
affiliate-check stop                       # stop daemon
```

Set `AFFITOR_API_KEY` for unlimited results (without key: free tier, max 5 results).

## Key rules

- Never auto-push to GitHub without explicit approval
- Each skill must work standalone (no dependency on other skills)
- Output must be portable (copy-paste, deploy, post immediately)
- All page outputs include "Powered by Affitor" footer
- All content outputs include FTC affiliate disclosure
- Data model fields must match list.affitor.com DB schema exactly

## Data source

- Primary: list.affitor.com API (`GET /api/v1/programs`, free tier or API key with `programs:read`)
- Fallback: `web_fetch` / `web_search` on list.affitor.com pages
- Programs use: `reward_value`, `reward_type`, `cookie_days`, `stars_count`, `tags[]`
- NOT: `commission_rate`, `upvotes`, `cookie_duration` (these are wrong field names)

## Skill chaining

- Skills pass data through conversation context, not files
- S1 output `recommended_program` → S2/S3 input `product`
- Each skill defines Input Schema and Output Schema for agent interop

## Commands

- `.claude/commands/new-skill.md` — scaffold a new skill from template
- `.claude/commands/review.md` — review skill quality against checklist
- `.claude/commands/test-skill.md` — run test prompts against a skill
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Affiliate Skills

Thanks for contributing! This guide explains how to add your own skill to the collection.

## How Skills Are Organized

Skills live in stage directories under `skills/`:

```
skills/
├── research/          S1: Find and evaluate programs
├── content/           S2: Create promotional content
├── blog/              S3: Write SEO articles
├── landing/           S4: Build conversion pages
├── distribution/      S5: Deploy and distribute
├── analytics/         S6: Track and optimize
├── automation/        S7: Automate and scale
└── meta/              S8: Plan, comply, improve
```

| Stage | Focus | Example Skills |
|-------|-------|---------------|
| S1: Research | Find and evaluate programs | `affiliate-program-search`, `niche-opportunity-finder` |
| S2: Content | Create promotional content | `viral-post-writer`, `tiktok-script-writer` |
| S3: Blog | Write SEO articles | `affiliate-blog-builder`, `comparison-post-writer` |
| S4: Landing | Build conversion pages | `landing-page-creator`, `product-showcase-page` |
| S5: Distribution | Deploy and distribute | `bio-link-deployer`, `github-pages-deployer` |
| S6: Analytics | Track and optimize | `conversion-tracker`, `seo-audit` |
| S7: Automation | Automate and scale | `content-repurposer`, `email-automation-builder` |
| S8: Meta | Plan, comply, improve | `funnel-planner`, `compliance-checker` |

Pick a stage, build a skill.

## Creating a New Skill

### 1. Fork and clone

```bash
git clone https://github.com/affitor/affiliate-skills.git
cd affiliate-skills
```

### 2. Scaffold your skill

Pick a stage and create the directory:

```bash
# Replace {stage} with: research, content, blog, landing, distribution, analytics, automation, or meta
mkdir -p skills/{stage}/your-skill-name/references
cp template/SKILL.md skills/{stage}/your-skill-name/SKILL.md
cp LICENSE skills/{stage}/your-skill-name/LICENSE.txt
```

Naming convention: `kebab-case`, `verb-noun` format (e.g., `viral-post-writer`, `affiliate-blog-builder`).

### 3. Write your skill

Fill in `SKILL.md` with:

- **Frontmatter:** name and a pushy description (cover multiple trigger phrases)
- **Input Schema:** what the skill needs (required vs optional fields)
- **Workflow:** step-by-step what the skill does
- **Output Schema:** structured output for agent chaining
- **Output Format:** human-readable output (tables, markdown, HTML)
- **Error Handling:** what to do when things go wrong
- **Examples:** at least 2 realistic prompts with expected output summaries

If any reference content exceeds 50 lines, put it in `references/` as a separate file.

### 4. Test your skill

Run these three tests:

1. **Stranger test:** Someone who's never heard of Affitor types a natural prompt. Does the output make sense?
2. **Chain test:** Paste the output into a new conversation. Can the next skill in the funnel understand it?
3. **Platform test:** Copy the output outside your AI. Does it work? (Post to X, deploy to Vercel, paste into WordPress)

### 5. Submit a PR

- Create your skill in `skills/{stage}/[skill-name]/`
- Include: `SKILL.md` + `references/` + 3 test prompts in PR description
- PR description: which stage, what it does, test results

## Quality Checklist

Before submitting, verify:

- [ ] `SKILL.md` has frontmatter with `name` and `description`
- [ ] Description is pushy — covers 5+ trigger phrases
- [ ] At least 2 examples with realistic prompts
- [ ] References in separate files if >50 lines
- [ ] Output is portable (user can use it immediately outside the AI)
- [ ] Tested in at least 2 different AI platforms (e.g., Claude + ChatGPT, or Cursor + Gemini)
- [ ] Includes affiliate disclosure guidance
- [ ] Works standalone (no dependency on other skills)
- [ ] Works in chain (picks up context from conversation if available)
- [ ] Input Schema and Output Schema defined
- [ ] Error handling covers common failure modes
- [ ] Tested with 3 different prompts

## After Merge

Your skill will be automatically added to `registry.json` via CI and published to [list.affitor.com/skills](https://list.affitor.com/skills). You'll be credited as the author.

See [`spec/`](spec/) for the full skill format specification.

## Questions?

Open an issue or reach out on [list.affitor.com](https://list.affitor.com).
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `package.json`
```json
{
  "name": "affiliate-skills",
  "version": "1.0.0",
  "description": "AI-powered affiliate marketing skills for any AI agent",
  "scripts": {
    "build": "bun build --compile tools/src/cli.ts --outfile tools/dist/affiliate-check",
    "dev": "bun run tools/src/cli.ts",
    "test": "bun test tools/test/"
  },
  "license": "MIT",
  "devDependencies": {}
}
```

## File: `QUICKSTART.md`
```markdown
# Quick Start Guide

Pick your AI platform and follow the steps. You'll be running affiliate marketing skills in under 5 minutes.

---

## Claude Code

Full integration with slash commands and the `affiliate-check` CLI tool.

**Requirements:** [Claude Code](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/claude-code), [Git](https://git-scm.com/), [Bun](https://bun.sh/) v1.0+

**Steps:**

1. Open Claude Code and paste:

> Install affiliate-skills: run `git clone https://github.com/Affitor/affiliate-skills.git ~/.claude/skills/affiliate-skills && cd ~/.claude/skills/affiliate-skills && ./setup` then add an "affiliate-skills" section to CLAUDE.md that says to use `/affiliate-check` for all affiliate program lookups, and lists the available skills: 32 skills across 8 stages (research, content, blog, landing, distribution, analytics, automation, meta). Set `AFFITOR_API_KEY` env var for unlimited access.

2. Claude Code auto-discovers all 32 skills from the `SKILL.md` files
3. Use naturally: *"Find me the best AI video affiliate program"* or *"Write a LinkedIn post about HeyGen"*

**What you get:** Slash commands, `affiliate-check` CLI with live data, automatic skill chaining.

---

## ChatGPT / GPT Projects

Works with ChatGPT Plus, Team, or Enterprise. No code required.

**Option A — Quick start (no install):**

1. Open ChatGPT
2. Copy the entire content of [`prompts/bootstrap.md`](../../../core/security/QUARANTINE/vetted/repos/codymaster/commands/bootstrap.md) (everything below the `---` line)
3. Paste it as your first message or add it to a GPT Project's instructions
4. Start prompting: *"Find me the best SaaS affiliate programs with recurring commission"*

**Option B — Custom GPT:**

1. Go to [ChatGPT → Create a GPT](https://chatgpt.com/gpts/editor)
2. In **Instructions**, paste the content of [`prompts/bootstrap.md`](../../../core/security/QUARANTINE/vetted/repos/codymaster/commands/bootstrap.md)
3. Enable **Web Browsing** (so it can call the API and browse list.affitor.com)
4. Optionally upload [`registry.json`](registry.json) and [`API.md`](API.md) as knowledge files
5. Save and share with your team

**Option C — Upload the repo:**

1. Download this repo as a ZIP from GitHub
2. In a ChatGPT conversation, upload the ZIP or individual SKILL.md files you need
3. Say: *"Use these skill files to help me with affiliate marketing"*

---

## Cursor / Windsurf / AI Code Editors

Skills auto-activate when you open the repo.

**Steps:**

1. Clone the repo into your project:
   ```bash
   git clone https://github.com/Affitor/affiliate-skills.git
   ```
2. Open the folder in Cursor — it reads `.cursorrules` automatically
3. For Windsurf, the SKILL.md files work as context when referenced
4. Start prompting in the AI chat: *"Search for affiliate programs in the AI niche"*

**Tip:** For the `affiliate-check` CLI, run `cd affiliate-skills && ./setup` in the terminal first.

---

## Gemini

Works with Gemini Advanced (file upload) or Google AI Studio.

**Option A — Quick start:**

1. Open [Gemini](https://gemini.google.com)
2. Copy the content of [`prompts/bootstrap.md`](../../../core/security/QUARANTINE/vetted/repos/codymaster/commands/bootstrap.md) and paste as your first message
3. Start prompting

**Option B — With full context:**

1. Upload these files to a Gemini conversation:
   - `prompts/bootstrap.md` — core instructions
   - `API.md` — API reference
   - `registry.json` — skill index
   - Any specific `SKILL.md` files for skills you want to use
2. Say: *"You are my affiliate marketing agent. Use these files as your instructions."*

**Note:** Gemini can browse the web, so API calls to list.affitor.com work directly.

---

## Any Other AI (Universal Method)

Works with any AI that accepts text input — OpenClaw, Perplexity, Mistral, local models, or custom agent frameworks.

**Steps:**

1. Open [`prompts/bootstrap.md`](../../../core/security/QUARANTINE/vetted/repos/codymaster/commands/bootstrap.md)
2. Copy everything below the `---` line
3. Paste it into your AI as the system prompt or first message
4. Start with: *"Search for the best affiliate programs for [your niche]"*

**For AI agents with HTTP access:** The bootstrap prompt includes API details. The AI will call `list.affitor.com/api/v1/programs` directly.

**For AI without HTTP access:** Ask the AI to generate the search URL, visit it yourself, and paste the JSON response back.

**For developers building agent pipelines:**
- Use [`registry.json`](registry.json) as a machine-readable skill index
- Each skill's `SKILL.md` has typed Input/Output schemas for structured data exchange
- See [`API.md`](API.md) for endpoint documentation
- Skills in `agents/openai.yaml` format are available for OpenAI-compatible tool definitions

---

## Without Installing Anything

Want to try before you commit? Paste this into any AI right now:

```
Search the Affitor affiliate directory for AI video tools.
Use this API: GET https://list.affitor.com/api/v1/programs?q=AI+video&sort=top&limit=5
Show me the results in a table with: Name, Commission, Cookie Duration, Stars.
Then recommend the best one and explain why.
```

No API key needed. Free tier returns up to 5 results.

---

## Next Steps

- Browse programs: [list.affitor.com](https://list.affitor.com)
- Full skill reference: [README.md](README.md)
- API documentation: [API.md](API.md)
- Contribute a skill: [CONTRIBUTING.md](CONTRIBUTING.md)
```

## File: `README.md`
```markdown
# affiliate-skills

**Turn any AI into your affiliate marketing team.**

32 AI-powered skills that take you from zero to first commission. Research programs, write content, build pages, deploy, track, optimize, scale — with any AI agent.

Works with: **Claude Code** · **ChatGPT** · **Gemini** · **Cursor** · **Windsurf** · **OpenClaw** · **any AI that reads text**

### Try it now — no install needed

Paste this into any AI:

```
Search the Affitor affiliate directory for AI video tools.
Use this API: GET https://list.affitor.com/api/v1/programs?q=AI+video&sort=top&limit=5
Show me the results in a table with: Name, Commission, Cookie Duration, Stars.
Then recommend the best one and explain why.
```

### Without affiliate-skills

- You Google "best affiliate programs" and get SEO spam written to rank, not to help
- You write a blog review and guess if the CTA, headline, or disclosure is any good
- You have no idea which content actually drives clicks — you just hope
- You spend 4 hours on a landing page that converts at 0.2%
- You pick programs by vibes instead of data

### With affiliate-skills

| Skill | Mode | What it does |
|-------|------|--------------|
| Program Search | Data analyst | Live program data from list.affitor.com — commissions, cookies, comparisons. |
| Research | Scout | Score and rank programs. Find the best one for your niche. |
| Funnel Planner | Strategist | Week-by-week roadmap from zero to revenue. Chain skills automatically. |
| Content, Blog, Landing, Distribution | Creator | 20 skills that write posts, articles, pages, and deploy them. |
| Analytics, Automation | Optimizer | Track conversions, A/B test, repurpose content, scale what works. |
| Compliance, Self-improver | Safety net | FTC audit before you publish. Retrospective after you launch. |

## Demo: zero to first commission

```
You:  I want to promote AI video tools. What's the best program?

AI:   [queries list.affitor.com API]

       Name                      Commission           Cookie     Stars
       ─────────────────────────────────────────────────────────────────
       HeyGen                    30% recurring        60 days    ★ 127
       Synthesia                 25% one-time         30 days    ★ 84
       D-ID                      20% recurring        45 days    ★ 52

      HeyGen is the clear winner: highest commission, recurring, longest
      cookie. Let me research it in depth.

You:  Write a blog review of HeyGen for content creators.

AI:   [runs affiliate-blog-builder skill]
      [2,000-word SEO review with pros/cons, comparison table,
       FTC disclosure, and affiliate CTA]

You:  Create a landing page for this.

AI:   [runs landing-page-creator skill]
      [single-file HTML/CSS page, AIDA framework, mobile-responsive,
       ready to deploy]

You:  Plan my full funnel — I have 5 hours/week and I blog.

AI:   [runs funnel-planner skill]

      Week 1: Research (affiliate-program-search) → select 2-3 programs
      Week 2: Content (viral-post-writer) → 5 LinkedIn + Twitter posts
      Week 3: Blog (affiliate-blog-builder) → 1 review article
      Week 4: Deploy (bio-link-deployer) → bio link page live
      Week 5: Analytics (seo-audit) → fix SEO issues
      Week 6: Optimize (ab-test-generator) → test headlines

      Success metric: first affiliate click by week 3, first commission
      by week 6.
```

## Who this is for

You want to do affiliate marketing with AI — not by hand. You want data-driven program selection, not guesswork. You want content that converts, not content that exists.

This is not a prompt pack for beginners. It is an operating system for affiliates who ship.

## Get Started

> **[QUICKSTART.md](QUICKSTART.md)** — Platform-specific setup for Claude Code, ChatGPT, Cursor, Gemini, and more.

### Fastest way (any AI, no install)

1. Copy the [bootstrap prompt](../../../core/security/QUARANTINE/vetted/repos/codymaster/commands/bootstrap.md) (everything below the `---` line)
2. Paste it into your AI
3. Start: *"Find me the best SaaS affiliate programs with recurring commission"*

### Claude Code (full integration)

```bash
git clone https://github.com/Affitor/affiliate-skills.git ~/.claude/skills/affiliate-skills
cd ~/.claude/skills/affiliate-skills && ./setup
```

Then tell Claude to add affiliate-skills to your project's CLAUDE.md. You get slash commands, the `affiliate-check` CLI, and automatic skill discovery.

### ChatGPT / Gemini / Any AI

1. Copy [`prompts/bootstrap.md`](../../../core/security/QUARANTINE/vetted/repos/codymaster/commands/bootstrap.md) into your conversation or project instructions
2. Optionally upload [`registry.json`](registry.json) and [`API.md`](API.md) as knowledge files
3. Done — your AI is now an affiliate marketing agent

### Cursor / Windsurf

```bash
git clone https://github.com/Affitor/affiliate-skills.git
```

Open the folder — `.cursorrules` configures the AI automatically.

---

## The Affiliate Funnel — 8 Stages, 32 Skills

```
  S1 RESEARCH ──▶ S2 CONTENT ──▶ S3 BLOG ──▶ S4 LANDING
       │                                         │
       ▼                                         ▼
  S6 ANALYTICS ◀──────── S5 DISTRIBUTION ◀──────┘
       │
       ▼
  S7 AUTOMATION ──▶ SCALE
       │
  S8 META (plan, comply, improve) ── across all stages
```

### S1: Research & Discovery
Find and evaluate the best affiliate programs to promote.

| Skill | Description |
|-------|-------------|
| [affiliate-program-search](skills/research/affiliate-program-search/) | Research and score programs from list.affitor.com |
| [niche-opportunity-finder](skills/research/niche-opportunity-finder/) | Find underserved niches with high potential |
| [competitor-spy](skills/research/competitor-spy/) | Analyze competitor affiliate strategies |
| [commission-calculator](skills/research/commission-calculator/) | Calculate and compare commission structures |

### S2: Content Creation
Write viral social media content that drives clicks.

| Skill | Description |
|-------|-------------|
| [viral-post-writer](skills/content/viral-post-writer/) | LinkedIn, X, Reddit, Facebook posts |
| [twitter-thread-writer](skills/content/twitter-thread-writer/) | Multi-tweet threads with hooks |
| [reddit-post-writer](skills/content/reddit-post-writer/) | Authentic Reddit posts with disclosure |
| [tiktok-script-writer](skills/content/tiktok-script-writer/) | Short-form video scripts |

### S3: Blog & SEO
Long-form SEO-optimized articles that rank and convert.

| Skill | Description |
|-------|-------------|
| [affiliate-blog-builder](skills/blog/affiliate-blog-builder/) | Full review and how-to articles |
| [comparison-post-writer](skills/blog/comparison-post-writer/) | Head-to-head product comparisons |
| [listicle-generator](skills/blog/listicle-generator/) | "Top N" roundup articles |
| [how-to-tutorial-writer](skills/blog/how-to-tutorial-writer/) | Tutorial articles with product integration |

### S4: Landing Pages
High-converting pages in pure HTML/CSS — no framework, no dependencies.

| Skill | Description |
|-------|-------------|
| [landing-page-creator](skills/landing/landing-page-creator/) | AIDA-framework landing pages |
| [product-showcase-page](skills/landing/product-showcase-page/) | Single-product showcase |
| [squeeze-page-builder](skills/landing/squeeze-page-builder/) | Lead capture pages |
| [webinar-registration-page](skills/landing/webinar-registration-page/) | Event-based promotion |

### S5: Distribution & Deployment
Get your content live and distributed.

| Skill | Description |
|-------|-------------|
| [bio-link-deployer](skills/distribution/bio-link-deployer/) | Linktree alternative you own |
| [email-drip-sequence](skills/distribution/email-drip-sequence/) | 5-7 email nurture sequence |
| [social-media-scheduler](skills/distribution/social-media-scheduler/) | Posting schedule and calendar |
| [github-pages-deployer](skills/distribution/github-pages-deployer/) | Deploy to GitHub Pages |

### S6: Analytics & Optimization
Track, measure, and optimize your affiliate performance.

| Skill | Description |
|-------|-------------|
| [conversion-tracker](skills/analytics/conversion-tracker/) | UTM links, tracking pixels, attribution |
| [ab-test-generator](skills/analytics/ab-test-generator/) | A/B test variants for headlines and CTAs |
| [performance-report](skills/analytics/performance-report/) | Weekly/monthly KPI reports |
| [seo-audit](skills/analytics/seo-audit/) | 10-dimension SEO scorecard |

### S7: Automation & Scale
Automate workflows and scale what's working.

| Skill | Description |
|-------|-------------|
| [email-automation-builder](skills/automation/email-automation-builder/) | Branching email flows with conditions |
| [content-repurposer](skills/automation/content-repurposer/) | One piece of content → multiple formats |
| [multi-program-manager](skills/automation/multi-program-manager/) | Affiliate program portfolio strategy |
| [paid-ad-copy-writer](skills/automation/paid-ad-copy-writer/) | Ad copy for Facebook, Google, TikTok |

### S8: Meta
Cross-cutting skills for discovery, planning, compliance, and self-improvement.

| Skill | Description |
|-------|-------------|
| [skill-finder](skills/meta/skill-finder/) | Find the right skill for any goal |
| [funnel-planner](skills/meta/funnel-planner/) | Plan a complete affiliate funnel roadmap |
| [compliance-checker](skills/meta/compliance-checker/) | FTC compliance and platform rules audit |
| [self-improver](skills/meta/self-improver/) | Campaign retrospective and improvement plan |

---

Machine-readable index: [`registry.json`](registry.json) · API docs: [`API.md`](API.md) · Skill template: [`template/SKILL.md`](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) · Spec: [`spec/`](spec/)

## How it works

Each skill is a single Markdown file (`SKILL.md`) that tells any AI exactly how to execute a specific affiliate marketing task. Skills define:

- **When to trigger** — natural language patterns that activate the skill
- **Input/Output schemas** — structured data for agent interop
- **Workflow** — step-by-step procedure with decision points
- **Chaining** — how outputs from one skill feed into the next

Skills pass data through conversation context, not files. Run S1 to find a program, then S2 uses that program's data automatically — no copy-pasting.

## Entry points

You don't have to start from S1. Jump in wherever you are:

- **New to affiliate marketing:** S8 `funnel-planner` → it plans everything for you
- **Have a product already:** S2 (write content) or S3 (write a review)
- **Have content, need pages:** S4 (landing page) or S5 (bio link)
- **Want to optimize:** S6 (analytics + SEO audit)
- **Ready to scale:** S7 (automation + paid ads)
- **Not sure which skill:** S8 `skill-finder`

## For Developers

Building an agent pipeline? Here's what you need:

- **[`registry.json`](registry.json)** — machine-readable index of all 32 skills with metadata
- **[`API.md`](API.md)** — full REST API documentation for list.affitor.com
- **[`prompts/bootstrap.md`](../../../core/security/QUARANTINE/vetted/repos/codymaster/commands/bootstrap.md)** — system prompt that bootstraps the full agent
- **`agents/openai.yaml`** — OpenAI-compatible tool definitions (in skills that have them)
- **Input/Output schemas** — every SKILL.md has typed schemas for structured data exchange

## Contributing

We welcome skills from the community. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to submit your own skill.

Every merged skill gets published to [list.affitor.com/skills](https://list.affitor.com/skills).

## License

MIT

---

Built by [Affitor](https://affitor.com). Directory: [list.affitor.com](https://list.affitor.com)
```

## File: `registry.json`
```json
{
  "version": "1.0.0",
  "generated_at": "2026-03-16T03:47:13.132Z",
  "stages": {
    "research": {
      "label": "Research & Discovery",
      "description": "Find and evaluate affiliate programs",
      "order": 1
    },
    "content": {
      "label": "Content Creation",
      "description": "Create viral social media content",
      "order": 2
    },
    "blog": {
      "label": "Blog & SEO",
      "description": "Long-form SEO-optimized articles",
      "order": 3
    },
    "landing": {
      "label": "Landing Pages",
      "description": "High-converting affiliate pages",
      "order": 4
    },
    "distribution": {
      "label": "Distribution & Deployment",
      "description": "Link hubs, bio pages, deployment",
      "order": 5
    },
    "analytics": {
      "label": "Analytics & Optimization",
      "description": "Track, measure, and optimize affiliate performance",
      "order": 6
    },
    "automation": {
      "label": "Automation & Scale",
      "description": "Automate workflows and scale what's working",
      "order": 7
    },
    "meta": {
      "label": "Meta",
      "description": "Cross-cutting skills for discovery, planning, compliance, and self-improvement",
      "order": 8
    }
  },
  "skills": [
    {
      "name": "affiliate-program-search",
      "slug": "affiliate-program-search",
      "stage": "research",
      "version": "1.0.0",
      "description": "> Research and evaluate affiliate programs to find the best ones to promote. Use this skill when the user asks anything about finding affiliate programs, comparing commission rates, evaluating affiliate opportunities, searching for products to promote, picking a niche, or mentions list.affitor.com. Also trigger for: \"which SaaS should I promote\", \"best affiliate programs for X\", \"high commission programs\", \"recurring commission affiliate\", \"compare these affiliate programs\", \"is X affiliate program worth it\", \"find me something to promote\", \"what pays the most\", \"affiliate programs with long cookie duration\".",
      "path": "skills/research/affiliate-program-search",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "commission-calculator",
      "slug": "commission-calculator",
      "stage": "research",
      "version": "1.0.0",
      "description": "> Calculate realistic affiliate earnings projections before committing to a program. Use this skill when the user asks about affiliate earnings, projecting income, calculating commissions, estimating how much they can make, comparing program payouts, or says \"how much can I make promoting X\", \"calculate my affiliate income\", \"is this commission worth it\", \"how long to first $1000\", \"compare earnings between programs\", \"traffic to income calculator\", \"what conversion rate should I expect\", \"earnings estimate for affiliate program\", \"how many sales do I need\".",
      "path": "skills/research/commission-calculator",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "competitor-spy",
      "slug": "competitor-spy",
      "stage": "research",
      "version": "1.0.0",
      "description": "> Reverse-engineer successful affiliate strategies from competitors. Use this skill when the user asks about spying on competitors, researching what other affiliates promote, analyzing competitor affiliate sites, understanding how top affiliates in a niche make money, or says \"what programs does X promote\", \"how does [site] make money\", \"what affiliate strategy does this site use\", \"spy on competitor affiliates\", \"reverse engineer affiliate site\", \"copy what works in my niche\", \"who are the top affiliates in X niche\", \"what content gets traffic in my niche\", \"competitor affiliate analysis\".",
      "path": "skills/research/competitor-spy",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "niche-opportunity-finder",
      "slug": "niche-opportunity-finder",
      "stage": "research",
      "version": "1.0.0",
      "description": "> Find untapped affiliate niches with real earning potential. Use this skill when the user asks about picking a niche, finding a niche to start affiliate marketing, what niche to get into, niche research, niche ideas, beginner niche selection, low competition niches, profitable niches, or says \"I don't know what to promote\", \"help me pick a niche\", \"what niche should I start with\", \"find me a niche with less competition\", \"niche ideas for affiliate\", \"is X a good niche for affiliate marketing\", \"best niches 2024\", \"untapped niches\".",
      "path": "skills/research/niche-opportunity-finder",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "reddit-post-writer",
      "slug": "reddit-post-writer",
      "stage": "content",
      "version": "1.0.0",
      "description": "> Write Reddit posts and comments that recommend affiliate products without getting banned or flagged as spam. Subreddit-native content that adds value first. Use this skill when the user asks about Reddit posts for affiliate marketing, writing Reddit comments that mention products, how to promote affiliate links on Reddit, or says \"write a Reddit post for X\", \"how to mention affiliate on Reddit\", \"Reddit comment promoting product\", \"Reddit-friendly affiliate content\", \"post for r/[subreddit] about X\", \"share affiliate link on Reddit without getting banned\", \"genuine Reddit recommendation\", \"organic Reddit affiliate post\", \"Reddit thread idea for product\".",
      "path": "skills/content/reddit-post-writer",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "tiktok-script-writer",
      "slug": "tiktok-script-writer",
      "stage": "content",
      "version": "1.0.0",
      "description": "> Write short-form video scripts for TikTok, Instagram Reels, and YouTube Shorts that promote affiliate products with strong hooks, demos, and CTAs. Use this skill when the user asks about TikTok scripts, Reels scripts, Shorts scripts, short-form video for affiliate marketing, or says \"write a TikTok for X\", \"script a Reel promoting X\", \"YouTube Shorts script affiliate\", \"60-second video script\", \"hook for TikTok affiliate\", \"write a video promoting X\", \"TikTok script that converts\", \"short video script for product review\", \"viral TikTok affiliate script\", \"how to promote X on TikTok\".",
      "path": "skills/content/tiktok-script-writer",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "twitter-thread-writer",
      "slug": "twitter-thread-writer",
      "stage": "content",
      "version": "1.0.0",
      "description": "> Write X/Twitter threads that get bookmarked, shared, and drive affiliate clicks. Use this skill when the user asks about writing Twitter threads, X threads, tweet threads for affiliate marketing, or says \"write a thread about X\", \"Twitter thread promoting X\", \"X thread for affiliate\", \"write tweets that go viral\", \"thread that sells without selling\", \"educational thread with affiliate CTA\", \"Twitter content for affiliate marketing\", \"how to promote X on Twitter\", \"write a thread my audience will bookmark\", \"tweet storm about affiliate product\".",
      "path": "skills/content/twitter-thread-writer",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "viral-post-writer",
      "slug": "viral-post-writer",
      "stage": "content",
      "version": "1.0.0",
      "description": "> Write viral social media posts that promote affiliate products naturally. Use this skill when the user asks anything about writing social media content for affiliate marketing, creating posts for LinkedIn/X/Reddit/Facebook, promoting a product on social media, writing affiliate content, or mentions \"viral post\", \"social media post\", \"content for affiliate\". Also trigger for: \"write a post about X\", \"help me promote X on LinkedIn\", \"create a thread about X\", \"make a Reddit post for X\", \"draft tweets for X\", \"social media content for affiliate program\", \"how to promote X on social\", \"write something that goes viral\", \"LinkedIn post for affiliate\", \"X thread about this tool\", \"help me sell X naturally on social media\".",
      "path": "skills/content/viral-post-writer",
      "agent_compatible": true,
      "tools": [
        "web_search",
        "web_browse"
      ],
      "author": "Affitor"
    },
    {
      "name": "affiliate-blog-builder",
      "slug": "affiliate-blog-builder",
      "stage": "blog",
      "version": "1.0.0",
      "description": "> Write SEO-optimized affiliate blog articles, product reviews, comparison posts, listicles, and how-to guides. Triggers on: \"write a blog post about\", \"review of [product]\", \"best [category] article\", \"comparison blog\", \"affiliate blog\", \"SEO article\", \"write a review\", \"product roundup\", \"blog content for affiliate\", \"how to use [product] blog post\", \"listicle about [category]\", \"[product] vs [product] blog\", \"content for my affiliate site\".",
      "path": "skills/blog/affiliate-blog-builder",
      "agent_compatible": true,
      "tools": [
        "web_search",
        "web_browse"
      ],
      "author": "Affitor"
    },
    {
      "name": "comparison-post-writer",
      "slug": "comparison-post-writer",
      "stage": "blog",
      "version": "1.0.0",
      "description": "> Write \"X vs Y\" comparison blog posts that help readers choose between two competing products. Triggers on: \"write a comparison post\", \"X vs Y blog post\", \"compare [product A] and [product B]\", \"which is better [A] or [B]\", \"head to head comparison\", \"[product] vs [product] article\", \"comparison review\", \"write a versus article\", \"side by side comparison blog\", \"which should I choose [A] or [B]\", \"compare these two products for my blog\".",
      "path": "skills/blog/comparison-post-writer",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "how-to-tutorial-writer",
      "slug": "how-to-tutorial-writer",
      "stage": "blog",
      "version": "1.0.0",
      "description": "> Write how-to guides and tutorials that naturally integrate affiliate product recommendations. Triggers on: \"write a how-to guide\", \"tutorial for [task]\", \"step by step guide to [goal]\", \"how to [verb] with [product]\", \"write a tutorial blog post\", \"guide on how to [task]\", \"beginner guide to [topic]\", \"walkthrough for [product]\", \"write an educational article\", \"how do I [task] blog post\", \"write a tutorial that promotes [product]\".",
      "path": "skills/blog/how-to-tutorial-writer",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "listicle-generator",
      "slug": "listicle-generator",
      "stage": "blog",
      "version": "1.0.0",
      "description": "> Write \"Top N best...\" listicle articles for affiliate marketing with mini-reviews, pricing, pros/cons, and CTAs per entry. Triggers on: \"write a best of list\", \"top 10 [category] tools\", \"best [product category] article\", \"roundup post\", \"listicle about [category]\", \"write a top tools article\", \"best [N] alternatives to [product]\", \"product roundup\", \"write a tools comparison list\", \"best software for [use case]\", \"top picks for [category]\".",
      "path": "skills/blog/listicle-generator",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "landing-page-creator",
      "slug": "landing-page-creator",
      "stage": "landing",
      "version": "1.0.0",
      "description": "> Build high-converting affiliate landing pages as single self-contained HTML files. Triggers on: \"create a landing page for\", \"build a landing page\", \"product landing page\", \"affiliate landing page\", \"comparison page for\", \"vs page\", \"single product page\", \"conversion page\", \"sales page for affiliate\", \"landing page HTML\", \"build me a page for\", \"create a page to promote [product]\", \"I need a landing page\", \"make a page for [product]\".",
      "path": "skills/landing/landing-page-creator",
      "agent_compatible": true,
      "tools": [
        "web_search",
        "web_browse"
      ],
      "author": "Affitor"
    },
    {
      "name": "product-showcase-page",
      "slug": "product-showcase-page",
      "stage": "landing",
      "version": "1.0.0",
      "description": "> Build a single-product deep-dive showcase page as a self-contained HTML file. Triggers on: \"build a product showcase page\", \"deep dive landing page for [product]\", \"create a product spotlight page\", \"product feature page\", \"single product page\", \"detailed page about [product]\", \"build a page showing everything about [product]\", \"create a long-form product page\", \"build a sales page for [product]\", \"product deep dive page\", \"make a feature breakdown page for [product]\".",
      "path": "skills/landing/product-showcase-page",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "squeeze-page-builder",
      "slug": "squeeze-page-builder",
      "stage": "landing",
      "version": "1.0.0",
      "description": "> Build email capture landing pages (squeeze pages) as single self-contained HTML files. Triggers on: \"build a squeeze page\", \"email capture page\", \"lead magnet page\", \"create an opt-in page\", \"build an email list page\", \"lead capture landing page\", \"create a freebie page\", \"build a page to collect emails\", \"opt-in landing page\", \"email signup page for [product/niche]\", \"create a lead magnet landing page\", \"build a page that captures emails before sending to affiliate offer\".",
      "path": "skills/landing/squeeze-page-builder",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "webinar-registration-page",
      "slug": "webinar-registration-page",
      "stage": "landing",
      "version": "1.0.0",
      "description": "> Build a webinar or live event registration page as a self-contained HTML file with countdown timer, speaker bio, agenda, and registration form. Triggers on: \"build a webinar registration page\", \"create a webinar sign-up page\", \"event registration landing page\", \"live training registration page\", \"workshop sign-up page\", \"create a webinar page\", \"build an event page\", \"free webinar landing page\", \"live demo registration page\", \"online event page\", \"create a registration page for my webinar\", \"build a training event page\".",
      "path": "skills/landing/webinar-registration-page",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "bio-link-deployer",
      "slug": "bio-link-deployer",
      "stage": "distribution",
      "version": "1.0.0",
      "description": "> Create a Linktree-style bio link hub page as a single self-contained HTML file. Triggers on: \"create a bio link page\", \"make a linktree\", \"link in bio page\", \"bio link\", \"link hub\", \"create my link page\", \"all my links on one page\", \"linktree alternative\", \"build a link page\", \"bio page for my affiliate links\", \"I need a link in bio\", \"make a page with all my links\", \"link aggregator page\".",
      "path": "skills/distribution/bio-link-deployer",
      "agent_compatible": true,
      "tools": [
        "web_search"
      ],
      "author": "Affitor"
    },
    {
      "name": "email-drip-sequence",
      "slug": "email-drip-sequence",
      "stage": "distribution",
      "version": "1.0.0",
      "description": "> Write an email drip sequence for affiliate marketing. Triggers on: \"write me an email sequence\", \"create a drip campaign\", \"email nurture sequence\", \"affiliate email funnel\", \"welcome email series\", \"email onboarding sequence\", \"write emails for my list\", \"set up a drip sequence\", \"email campaign for [product]\", \"nurture my subscribers\", \"email follow-up sequence\", \"build my email funnel\", \"write 5 emails promoting [product]\", \"email automation sequence\".",
      "path": "skills/distribution/email-drip-sequence",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "github-pages-deployer",
      "slug": "github-pages-deployer",
      "stage": "distribution",
      "version": "1.0.0",
      "description": "> Deploy affiliate content to GitHub Pages for free hosting. Triggers on: \"deploy to GitHub Pages\", \"host on GitHub Pages\", \"free hosting for my affiliate site\", \"push to GitHub Pages\", \"GitHub Pages setup\", \"deploy my landing page to GitHub\", \"host my bio link on GitHub\", \"free affiliate website hosting\", \"github pages affiliate\", \"set up GitHub Pages for my site\", \"deploy HTML to GitHub\", \"free static hosting\", \"publish my affiliate page for free\", \"github pages custom domain\".",
      "path": "skills/distribution/github-pages-deployer",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "social-media-scheduler",
      "slug": "social-media-scheduler",
      "stage": "distribution",
      "version": "1.0.0",
      "description": "> Create a 30-day social media content calendar for affiliate marketing. Triggers on: \"create a social media calendar\", \"30-day content plan\", \"social media schedule\", \"content calendar for [product]\", \"plan my social posts\", \"social media strategy\", \"schedule my affiliate posts\", \"content plan for LinkedIn\", \"30 days of content\", \"social posting schedule\", \"what should I post this month\", \"write my social content\", \"create posts for LinkedIn X Facebook\", \"affiliate content calendar\", \"social media plan for my affiliate program\".",
      "path": "skills/distribution/social-media-scheduler",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "ab-test-generator",
      "slug": "ab-test-generator",
      "stage": "analytics",
      "version": "1.0.0",
      "description": "> Generate A/B test variants for affiliate content. Triggers on: \"create A/B test\", \"test my headline\", \"optimize my CTA\", \"generate variants\", \"split test ideas\", \"improve click-through rate\", \"test my landing page copy\", \"headline alternatives\", \"CTA variations\", \"which version is better\", \"optimize conversions\", \"test my email subject line\", \"compare approaches\".",
      "path": "skills/analytics/ab-test-generator",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "conversion-tracker",
      "slug": "conversion-tracker",
      "stage": "analytics",
      "version": "1.0.0",
      "description": "> Set up affiliate conversion tracking with UTM parameters and link tagging. Triggers on: \"set up tracking\", \"create UTM links\", \"track my affiliate links\", \"tracking pixels\", \"click attribution\", \"organize my links\", \"UTM parameters\", \"tag my links\", \"campaign tracking\", \"link tracking setup\", \"prepare for launch\", \"debug attribution\", \"tracking spreadsheet\".",
      "path": "skills/analytics/conversion-tracker",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "performance-report",
      "slug": "performance-report",
      "stage": "analytics",
      "version": "1.0.0",
      "description": "> Generate affiliate performance reports with KPIs and recommendations. Triggers on: \"show my affiliate report\", \"how are my programs doing\", \"performance review\", \"earnings report\", \"monthly affiliate report\", \"weekly report\", \"analyze my affiliate earnings\", \"which program is best\", \"EPC report\", \"conversion rate analysis\", \"revenue breakdown\", \"campaign performance\".",
      "path": "skills/analytics/performance-report",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "seo-audit",
      "slug": "seo-audit",
      "stage": "analytics",
      "version": "1.0.0",
      "description": "> Audit affiliate blog posts and landing pages for SEO issues. Triggers on: \"audit my blog post for SEO\", \"check my SEO\", \"SEO review\", \"improve my rankings\", \"SEO checklist\", \"on-page SEO audit\", \"keyword optimization check\", \"why isn't my page ranking\", \"SEO score\", \"content quality audit\", \"check my meta tags\", \"internal linking audit\", \"quick SEO wins\".",
      "path": "skills/analytics/seo-audit",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "content-repurposer",
      "slug": "content-repurposer",
      "stage": "automation",
      "version": "1.0.0",
      "description": "> Repurpose one piece of affiliate content into multiple formats. Triggers on: \"repurpose my content\", \"turn my blog into tweets\", \"cross-post this\", \"content recycling\", \"convert to newsletter\", \"make a tweet thread from this\", \"adapt for TikTok\", \"omnichannel content\", \"scale my content\", \"turn this into a LinkedIn post\", \"repurpose for email\", \"content multiplication\".",
      "path": "skills/automation/content-repurposer",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "email-automation-builder",
      "slug": "email-automation-builder",
      "stage": "automation",
      "version": "1.0.0",
      "description": "> Build multi-sequence email automation flows with branching logic. Triggers on: \"build email automation\", \"create email funnel\", \"email automation flow\", \"welcome series with branches\", \"conditional email sequence\", \"set up automation\", \"email workflow builder\", \"segmented email flow\", \"advanced email sequence\", \"nurture funnel\", \"cart abandonment sequence\", \"win-back email flow\".",
      "path": "skills/automation/email-automation-builder",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "multi-program-manager",
      "slug": "multi-program-manager",
      "stage": "automation",
      "version": "1.0.0",
      "description": "> Manage and compare multiple affiliate programs as a portfolio. Triggers on: \"manage my affiliate programs\", \"compare my programs\", \"portfolio overview\", \"which program should I focus on\", \"diversify my affiliate income\", \"program switching\", \"affiliate portfolio\", \"program comparison\", \"revenue allocation\", \"which programs to drop\", \"add new programs\", \"affiliate program strategy\".",
      "path": "skills/automation/multi-program-manager",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "paid-ad-copy-writer",
      "slug": "paid-ad-copy-writer",
      "stage": "automation",
      "version": "1.0.0",
      "description": "> Write paid ad copy for affiliate offers across ad platforms. Triggers on: \"write ad copy\", \"Facebook ad for affiliate\", \"Google Ads copy\", \"TikTok ad script\", \"Pinterest ad\", \"paid traffic to affiliate\", \"create ad campaign\", \"ad headlines\", \"ad descriptions\", \"scale with paid ads\", \"run ads for my affiliate link\", \"write Facebook ad\", \"Google Search ad copy\".",
      "path": "skills/automation/paid-ad-copy-writer",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "compliance-checker",
      "slug": "compliance-checker",
      "stage": "meta",
      "version": "1.0.0",
      "description": "> Check affiliate content for FTC compliance and platform rules. Triggers on: \"check my content for compliance\", \"FTC disclosure check\", \"is this legal\", \"review for compliance\", \"check affiliate disclosure\", \"am I FTC compliant\", \"audit my content\", \"compliance review\", \"legal check\", \"platform rules check\", \"check before publishing\", \"disclosure audit\", \"review my ad copy\".",
      "path": "skills/meta/compliance-checker",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "funnel-planner",
      "slug": "funnel-planner",
      "stage": "meta",
      "version": "1.0.0",
      "description": "> Plan a complete affiliate funnel from research to revenue. Triggers on: \"plan my affiliate funnel\", \"create a funnel strategy\", \"affiliate business plan\", \"how to start affiliate marketing\", \"full funnel roadmap\", \"plan from scratch\", \"week by week affiliate plan\", \"chain skills together\", \"build my funnel\", \"affiliate marketing roadmap\", \"step by step affiliate plan\", \"onboarding plan\".",
      "path": "skills/meta/funnel-planner",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "self-improver",
      "slug": "self-improver",
      "stage": "meta",
      "version": "1.0.0",
      "description": "> Review affiliate campaign results and improve strategy. Triggers on: \"review my results\", \"what went wrong\", \"how to improve conversions\", \"analyze my campaign\", \"affiliate retrospective\", \"why am I not converting\", \"improve my strategy\", \"what should I change\", \"campaign review\", \"optimize my approach\", \"learn from my results\", \"post-mortem on my campaign\".",
      "path": "skills/meta/self-improver",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    },
    {
      "name": "skill-finder",
      "slug": "skill-finder",
      "stage": "meta",
      "version": "1.0.0",
      "description": "> Find the right Affitor skill for your goal. Triggers on: \"which skill should I use\", \"find me a skill\", \"what skills are available\", \"help me choose a skill\", \"skill for SEO\", \"skill for email\", \"explore skills\", \"I'm new to Affitor\", \"what can Affitor do\", \"search skills\", \"skill for blog writing\", \"skill for landing pages\", \"skill for analytics\".",
      "path": "skills/meta/skill-finder",
      "agent_compatible": true,
      "tools": [],
      "author": "Affitor"
    }
  ]
}
```

## File: `setup`
```
#!/usr/bin/env bash
# Setup script for affiliate-skills
# Builds the affiliate-check binary and creates skill symlinks
# Pattern: gstack/setup

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "[affiliate-skills] Setting up..."

# 1. Check Bun
if ! command -v bun &>/dev/null; then
  echo "[affiliate-skills] Bun is required but not installed."
  echo "  Install: curl -fsSL https://bun.sh/install | bash"
  exit 1
fi

# 2. Install dependencies (if any)
if [ -f package.json ]; then
  bun install --frozen-lockfile 2>/dev/null || bun install
fi

# 3. Build affiliate-check binary
NEEDS_BUILD=false
if [ ! -f tools/dist/affiliate-check ]; then
  NEEDS_BUILD=true
else
  # Check if source is newer than binary
  for src in tools/src/*.ts; do
    if [ "$src" -nt tools/dist/affiliate-check ]; then
      NEEDS_BUILD=true
      break
    fi
  done
  if [ package.json -nt tools/dist/affiliate-check ]; then
    NEEDS_BUILD=true
  fi
fi

if [ "$NEEDS_BUILD" = true ]; then
  echo "[affiliate-skills] Building affiliate-check binary..."
  mkdir -p tools/dist
  bun build --compile tools/src/cli.ts --outfile tools/dist/affiliate-check
  echo "[affiliate-skills] Binary built: tools/dist/affiliate-check"
else
  echo "[affiliate-skills] Binary up to date."
fi

# 4. Platform-specific setup
PLATFORM="generic"

if [[ "$SCRIPT_DIR" == *".claude/skills/"* ]]; then
  PLATFORM="claude-code"
  SKILLS_DIR="$(dirname "$SCRIPT_DIR")"
  REPO_NAME="$(basename "$SCRIPT_DIR")"

  # Symlink affiliate-check as a top-level skill
  if [ -f "$SCRIPT_DIR/SKILL.md" ]; then
    ln -snf "$REPO_NAME" "$SKILLS_DIR/affiliate-check" 2>/dev/null || true
  fi

  echo "[affiliate-skills] Claude Code detected — symlinks created in $SKILLS_DIR"
elif command -v cursor &>/dev/null || [[ "$SCRIPT_DIR" == *"cursor"* ]]; then
  PLATFORM="cursor"
  echo "[affiliate-skills] Cursor detected — .cursorrules is ready"
elif [[ -n "${WINDSURF_HOME:-}" ]]; then
  PLATFORM="windsurf"
  echo "[affiliate-skills] Windsurf detected — skill files are ready"
else
  echo "[affiliate-skills] Generic setup — use prompts/bootstrap.md with any AI"
fi

# 5. Generate registry
if [ -f scripts/generate-registry.js ]; then
  node scripts/generate-registry.js 2>/dev/null || true
fi

echo "[affiliate-skills] Setup complete! (platform: $PLATFORM)"
echo ""
echo "  Binary:  $SCRIPT_DIR/tools/dist/affiliate-check"
echo "  Skills:  32 skills across 8 stages"
echo ""
if [ "$PLATFORM" = "claude-code" ]; then
  echo "  Quick start (Claude Code):"
  echo "    affiliate-check search \"AI video tools\""
  echo "    affiliate-check top"
  echo "    affiliate-check compare heygen synthesia"
elif [ "$PLATFORM" = "cursor" ] || [ "$PLATFORM" = "windsurf" ]; then
  echo "  Quick start ($PLATFORM):"
  echo "    Open this folder in $PLATFORM — skills are auto-discovered."
  echo "    For CLI: ./tools/dist/affiliate-check search \"AI video tools\""
else
  echo "  Quick start (any AI):"
  echo "    1. Copy prompts/bootstrap.md into your AI"
  echo "    2. Start: \"Find me the best AI affiliate programs\""
  echo "    3. CLI: ./tools/dist/affiliate-check search \"AI video tools\""
fi
echo ""
echo "  Set AFFITOR_API_KEY for unlimited access:"
echo "    export AFFITOR_API_KEY=afl_..."
echo "    Get one: list.affitor.com/settings → API Keys (free)"
echo ""
```

## File: `SKILL.md`
```markdown
---
name: affiliate-check
version: 1.0.0
description: |
  Live affiliate program data from list.affitor.com. Search programs, compare commissions,
  check cookie days, find top performers. Use when researching affiliate programs,
  comparing options, or checking program details. Persistent daemon with cache — first call
  starts server (~2s), subsequent calls ~100ms.
allowed-tools:
  - Bash
  - Read
---

# affiliate-check: Live Affiliate Program Data

Query affiliate program data from list.affitor.com in real-time. Persistent daemon
with in-memory cache — first call auto-starts the server, every subsequent call is instant.

## SETUP (run this check BEFORE any affiliate-check command)

Before using any command, find the skill and check if the binary exists:

```bash
# Check project-level first, then user-level
if test -x .claude/skills/affiliate-skills/tools/dist/affiliate-check; then
  A=.claude/skills/affiliate-skills/tools/dist/affiliate-check
elif test -x ~/.claude/skills/affiliate-skills/tools/dist/affiliate-check; then
  A=~/.claude/skills/affiliate-skills/tools/dist/affiliate-check
else
  echo "NEEDS_SETUP"
fi
```

Set `A` to whichever path exists and use it for all commands.

If `NEEDS_SETUP`:
1. Tell the user: "affiliate-check needs a one-time build (~10 seconds). OK to proceed?"
2. If approved, run: `cd <SKILL_DIR> && ./setup`
3. If `bun` is not installed: `curl -fsSL https://bun.sh/install | bash`

## Quick Reference

```bash
A=~/.claude/skills/affiliate-skills/tools/dist/affiliate-check

# Search programs
$A search "AI video tools"
$A search --recurring --tags ai

# Top programs
$A top
$A top --sort trending

# Program details
$A info heygen

# Compare programs side-by-side
$A compare heygen synthesia

# Server management
$A status
$A stop
```

## Commands

### Search
```
affiliate-check search <query>                    Search by name/keyword
affiliate-check search --recurring                Filter recurring commissions
affiliate-check search --tags ai,video            Filter by tags
affiliate-check search --min-cookie 30            Min cookie days
affiliate-check search --sort new                 Sort: trending | new | top
affiliate-check search --limit 20                 Result limit
```

### Discovery
```
affiliate-check top                               Top programs by stars
affiliate-check top --sort trending               Trending programs
affiliate-check top --sort new                    Newest programs
```

### Details
```
affiliate-check info <name>                       Detailed program card
affiliate-check compare <name1> <name2> [name3]   Side-by-side comparison
```

### Server
```
affiliate-check status                            Uptime, cache, API key status
affiliate-check stop                              Shutdown daemon
affiliate-check help                              Full help
```

## Environment

```
AFFITOR_API_KEY    Optional. API key from list.affitor.com
                   Without: free tier (max 5 results per query)
                   With: unlimited access
                   Get one: list.affitor.com/settings → API Keys (free)
```

## Architecture

- Persistent Bun daemon on localhost (port 9500-9510)
- In-memory cache with 5-minute TTL
- State file: `/tmp/affiliate-check.json`
- Auto-shutdown after 30 min idle
- Server crash → auto-restarts on next command
```

## File: `VERSION`
```
1.0.0
```

## File: `_VET_REPORT.md`
```markdown
﻿# Strix Vet Report: affitor-affiliate-skills
**Date:** 2026-03-17 10:09:19
**Status:** PASS
**Critical Findings:** 0
**Warnings:** 2

## Verdict

PASS - Repo passed all security checks. Safe to extract specific files into AI OS.

## Findings

| Level | Category | Detail | File |
|-------|----------|--------|------|
| PASS | GIT_HOOK | No active hooks found | `` |
| WARN | SENSITIVE_ACCESS | .env file access | `D:\Project\QUARANTINE\affitor-affiliate-skills\tools\src\cli.ts` |
| WARN | SENSITIVE_ACCESS | .env file access | `D:\Project\QUARANTINE\affitor-affiliate-skills\tools\src\server.ts` |


## Next Step

Proceed to content extraction. Copy only needed files into D:\APP\AI OS\knowledge\ or relevant skill folder.
```

## File: `brain/knowledge/docs_legacy/affiliate-funnel-overview.md`
```markdown
# Affiliate Funnel Overview

This document explains the five-stage affiliate funnel that organizes all skills in this repo. If you're contributing a new skill, read this first.

## The Five Stages

Every affiliate marketer, regardless of experience level, goes through these stages:

### S1: Research

**Question:** "What should I promote?"

Find and evaluate affiliate programs. Score them on earning potential, content potential, market demand, competition, and trust. Pick the best fit for your niche and audience.

**Path:** `skills/research/`
**Current skill:** `affiliate-program-search`
**Open for contribution:** industry-specific scanners (crypto, fintech, health tech)

### S2: Content

**Question:** "How do I tell people about it?"

Create promotional content for social media platforms. Each platform has different rules, formats, and audiences. Content should be genuine recommendations, not ads.

**Path:** `skills/content/`
**Current skill:** `viral-post-writer`
**Open for contribution:** TikTok script writer, email sequence builder, YouTube script writer

### S3: Blog

**Question:** "How do I rank on Google for this?"

Write SEO-optimized blog posts that rank for buyer-intent keywords. Reviews, comparisons, and listicles that drive organic traffic and convert over months/years.

**Path:** `skills/blog/`
**Current skill:** `affiliate-blog-builder`
**Open for contribution:** podcast show notes, newsletter builder

### S4: Landing

**Question:** "Where do I send traffic?"

Build dedicated landing pages that warm up visitors before sending them to the merchant's site. Higher conversion than sending people directly to a product page.

**Path:** `skills/landing/`
**Current skill:** `landing-page-creator`
**Open for contribution:** webinar registration page, quiz funnel builder

### S5: Distribution

**Question:** "How do I get my links out there?"

Create a central hub for all your affiliate links. Bio link pages, portfolio sites, link aggregators. Deploy to any static host.

**Path:** `skills/distribution/`
**Current skill:** `bio-link-deployer`
**Open for contribution:** GitHub Pages deployer, Notion portfolio builder

## How Stages Connect

```
S1 → picks a program
  ↓
S2 → writes content about it (social media, quick distribution)
  ↓
S3 → writes long-form content (blog, SEO, long-term traffic)
  ↓
S4 → builds a dedicated page (highest conversion)
  ↓
S5 → creates a hub linking everything together
```

Output of each stage feeds naturally into the next. But each stage also works independently.

## Two Paths

Not everyone follows the same order:

**Social path (fast, needs consistency):**
S1 → S2 → repeat. Post regularly, build audience, earn from day one.

**Content path (slow, compounds over time):**
S1 → S3 → S4. Write once, rank on Google, earn passively for years.

Most successful affiliates do both.

## Contributing a New Skill

1. Pick a stage that your skill belongs to
2. Read `template/SKILL.md` and existing skills in that stage
3. Create your skill at `skills/{stage}/{skill-name}/SKILL.md`
4. Build with Input/Output Schemas for agent chaining
5. Test with 3 prompts, submit a PR
6. See `CONTRIBUTING.md` for full details
```

## File: `brain/knowledge/docs_legacy/skill-roadmap.md`
```markdown
# Skill Roadmap

## Shipped

| Skill | Stage | Path | Description |
|-------|-------|------|-------------|
| `affiliate-program-search` | S1: Research | `skills/research/` | Research and score programs from list.affitor.com |
| `commission-calculator` | S1: Research | `skills/research/` | Calculate and compare affiliate commissions |
| `competitor-spy` | S1: Research | `skills/research/` | Analyze competitor affiliate strategies |
| `niche-opportunity-finder` | S1: Research | `skills/research/` | Find underserved affiliate niches |
| `viral-post-writer` | S2: Content | `skills/content/` | Write viral social media posts for affiliate products |
| `reddit-post-writer` | S2: Content | `skills/content/` | Write authentic Reddit posts with affiliate disclosure |
| `tiktok-script-writer` | S2: Content | `skills/content/` | Short-form video scripts for affiliate products |
| `twitter-thread-writer` | S2: Content | `skills/content/` | Twitter/X threads for affiliate products |
| `affiliate-blog-builder` | S3: Blog | `skills/blog/` | SEO reviews, comparisons, listicles, how-to guides |
| `comparison-post-writer` | S3: Blog | `skills/blog/` | Head-to-head product comparison articles |
| `how-to-tutorial-writer` | S3: Blog | `skills/blog/` | Tutorial articles with affiliate product integration |
| `listicle-generator` | S3: Blog | `skills/blog/` | "Top N" listicle articles for affiliate products |
| `landing-page-creator` | S4: Landing | `skills/landing/` | Single/comparison HTML landing pages with AIDA conversion framework |
| `product-showcase-page` | S4: Landing | `skills/landing/` | Single-product showcase landing pages |
| `squeeze-page-builder` | S4: Landing | `skills/landing/` | Lead capture squeeze pages |
| `webinar-registration-page` | S4: Landing | `skills/landing/` | Event-based affiliate promotion pages |
| `bio-link-deployer` | S5: Distribution | `skills/distribution/` | Linktree-style bio link hub page, 3 themes, self-contained HTML |
| `email-drip-sequence` | S5: Distribution | `skills/distribution/` | 5-7 email drip sequence for affiliate nurture |
| `github-pages-deployer` | S5: Distribution | `skills/distribution/` | Deploy affiliate pages to GitHub Pages |
| `social-media-scheduler` | S5: Distribution | `skills/distribution/` | Social media posting schedule and calendar |
| `conversion-tracker` | S6: Analytics | `skills/analytics/` | UTM parameters, tracking pixels, link attribution |
| `ab-test-generator` | S6: Analytics | `skills/analytics/` | A/B test variants for headlines, CTAs, content |
| `performance-report` | S6: Analytics | `skills/analytics/` | Weekly/monthly affiliate performance reports with KPIs |
| `seo-audit` | S6: Analytics | `skills/analytics/` | On-page SEO audit with 10-dimension scorecard |
| `email-automation-builder` | S7: Automation | `skills/automation/` | Branching email automation flows with conditional logic |
| `content-repurposer` | S7: Automation | `skills/automation/` | Repurpose one piece of content into multiple formats |
| `multi-program-manager` | S7: Automation | `skills/automation/` | Affiliate program portfolio strategy and management |
| `paid-ad-copy-writer` | S7: Automation | `skills/automation/` | Paid ad copy for Facebook, Google, TikTok, Pinterest |
| `skill-finder` | S8: Meta | `skills/meta/` | Find the right Affitor skill for any goal |
| `funnel-planner` | S8: Meta | `skills/meta/` | Plan a complete affiliate funnel roadmap |
| `compliance-checker` | S8: Meta | `skills/meta/` | FTC compliance and platform rules audit |
| `self-improver` | S8: Meta | `skills/meta/` | Campaign retrospective and improvement planning |

## In Progress

| Skill | Stage | Target | Owner |
|-------|-------|--------|-------|
| API search filters | Infrastructure | Phase 2b | Affitor team |

## Open for Community Contribution

These are skills we'd love to see but aren't building ourselves yet. Pick one and submit a PR!

### S1: Research (`skills/research/`)
- `crypto-affiliate-scanner` — specialized for crypto/DeFi affiliate programs
- `saas-lifetime-deal-finder` — find AppSumo/lifetime deal affiliate opportunities

### S2: Content (`skills/content/`)
- `youtube-script-writer` — long-form YouTube review/tutorial scripts
- `pinterest-pin-writer` — Pinterest pin descriptions optimized for affiliate content

### S3: Blog (`skills/blog/`)
- `podcast-show-notes` — SEO-optimized show notes with affiliate links
- `newsletter-builder` — weekly newsletter template with product recommendations

### S4: Landing (`skills/landing/`)
- `quiz-funnel-builder` — interactive quiz that recommends affiliate products
- `comparison-table-page` — multi-product comparison table landing page

### S5: Distribution (`skills/distribution/`)
- `notion-portfolio` — Notion-based affiliate link portfolio

### S6: Analytics (`skills/analytics/`)
- `competitor-rank-tracker` — track competitor rankings for your target keywords
- `revenue-forecaster` — predict affiliate revenue based on historical data

### S7: Automation (`skills/automation/`)
- `social-calendar-generator` — automated content calendar across platforms
- `link-rotator` — rotate affiliate links based on performance

### S8: Meta (`skills/meta/`)
- `skill-builder` — help community members create new Affitor skills
- `niche-selector` — help complete beginners pick a niche before S1

## How to Claim a Skill

1. Open an issue titled "Claiming: [skill-name]"
2. Describe your approach in 3-5 sentences
3. We'll confirm and you can start building
4. Submit a PR when ready
```

## File: `evals/evals.json`
```json
{
  "version": "1.0",
  "description": "Test cases for affiliate-skills. Each case has an input prompt, expected patterns in output, and pass criteria.",
  "skills": {
    "affiliate-program-search": {
      "tests": [
        {
          "id": "s1-001",
          "name": "Category search with filters",
          "input_prompt": "I want to promote AI video tools, commission recurring, at least 20%",
          "expected_patterns": [
            "Programs Found",
            "Top Pick:",
            "Score",
            "Earning Potential",
            "Content Potential",
            "cps_recurring",
            "Next Steps"
          ],
          "pass_criteria": "Output contains a comparison table with at least 2 programs, a scored recommendation with all 5 dimensions, and actionable next steps. Programs shown must have recurring commission ≥20%."
        },
        {
          "id": "s1-002",
          "name": "Head-to-head comparison",
          "input_prompt": "Compare HeyGen vs Synthesia for my LinkedIn audience",
          "expected_patterns": [
            "HeyGen",
            "Synthesia",
            "LinkedIn",
            "Score",
            "Content Potential"
          ],
          "pass_criteria": "Output contains side-by-side comparison of both programs with scores. Content Potential and platform fit for LinkedIn are explicitly discussed. Clear winner recommendation."
        },
        {
          "id": "s1-003",
          "name": "Beginner with no criteria",
          "input_prompt": "I'm new to affiliate marketing. What should I promote?",
          "expected_patterns": [
            "beginner",
            "free",
            "recurring",
            "Top Pick:",
            "Next Steps"
          ],
          "pass_criteria": "Output defaults to beginner-friendly criteria (AI/SaaS, recurring, easy to demo). Recommends products with free tiers and low payout thresholds. Includes clear next steps."
        }
      ]
    },
    "viral-post-writer": {
      "tests": [
        {
          "id": "s2-001",
          "name": "LinkedIn post for a specific product",
          "input_prompt": "Write a LinkedIn post promoting HeyGen",
          "expected_patterns": [
            "HeyGen",
            "Post Content",
            "Link placement",
            "#ad",
            "Engagement Tips"
          ],
          "pass_criteria": "Output contains a ready-to-copy LinkedIn post with a clear hook in the first line, no external link in the post body (link in comments), FTC disclosure, and posting tips. Must NOT start with 'I'm excited to share'."
        },
        {
          "id": "s2-002",
          "name": "X thread for SEO tool",
          "input_prompt": "Create an X thread about Semrush for SEO marketers",
          "expected_patterns": [
            "Semrush",
            "Tweet 1",
            "Thread",
            "#ad",
            "SEO"
          ],
          "pass_criteria": "Output contains a multi-tweet thread (5+ tweets), numbered or clearly separated. First tweet has a compelling hook. Last tweet contains CTA, link, and #ad disclosure. Content is specific to SEO use cases."
        },
        {
          "id": "s2-003",
          "name": "Reddit post with personal experience",
          "input_prompt": "I've been using Notion for 2 years, help me write a Reddit post",
          "expected_patterns": [
            "Notion",
            "pros",
            "cons",
            "disclosure",
            "affiliate"
          ],
          "pass_criteria": "Output includes both pros and cons (Reddit requires honesty). Uses the user's personal experience. Includes 'Full disclosure: affiliate link' at the bottom. Suggests relevant subreddits. Does NOT read like an ad."
        },
        {
          "id": "s2-004",
          "name": "All platforms for a single product",
          "input_prompt": "Promote GetResponse on all platforms",
          "expected_patterns": [
            "GetResponse",
            "LinkedIn",
            "Reddit"
          ],
          "pass_criteria": "Output contains at least 3 separate posts for different platforms (LinkedIn, X, Reddit). Each post is formatted differently and tailored to the platform. Each has appropriate FTC disclosure for that platform."
        }
      ]
    },
    "conversion-tracker": {
      "tests": [
        {
          "id": "s6-001",
          "name": "Basic tracking setup",
          "input_prompt": "Set up tracking for my HeyGen affiliate link (heygen.com/ref/abc123) on blog and Twitter",
          "expected_patterns": [
            "utm_source",
            "utm_medium",
            "utm_campaign",
            "heygen",
            "blog",
            "twitter"
          ],
          "pass_criteria": "Output contains UTM-tagged links for both blog and Twitter. Each link has proper utm_source, utm_medium, and utm_campaign parameters. Includes a naming convention and setup guide."
        },
        {
          "id": "s6-002",
          "name": "Multi-platform campaign",
          "input_prompt": "Create tracking links for Semrush across LinkedIn, Twitter, Reddit, blog, and email",
          "expected_patterns": [
            "linkedin",
            "twitter",
            "reddit",
            "blog",
            "email",
            "utm_source"
          ],
          "pass_criteria": "Output contains at least 5 distinct UTM-tagged links, one per platform. Naming convention is consistent. Includes tracking setup guide."
        }
      ]
    },
    "ab-test-generator": {
      "tests": [
        {
          "id": "s6-003",
          "name": "Headline A/B test",
          "input_prompt": "Test this headline: 'HeyGen Review: Is It Worth It in 2026?'",
          "expected_patterns": [
            "Original",
            "Variant",
            "hypothesis",
            "test"
          ],
          "pass_criteria": "Output contains the original headline plus at least 3 variants. Each variant has a hypothesis explaining why it might outperform. Includes a test plan with sample size and duration."
        },
        {
          "id": "s6-004",
          "name": "CTA optimization",
          "input_prompt": "Optimize this CTA: 'Start Free Trial'",
          "expected_patterns": [
            "Original",
            "Variant",
            "CTA",
            "clicks"
          ],
          "pass_criteria": "Output contains at least 3 CTA alternatives with different approaches (outcome-focused, friction-reducing, urgency). Each has a hypothesis. Test plan included."
        }
      ]
    },
    "performance-report": {
      "tests": [
        {
          "id": "s6-005",
          "name": "Multi-program monthly report",
          "input_prompt": "Monthly report: HeyGen 500 clicks 15 conversions $450, Semrush 1200 clicks 8 conversions $320, Notion 300 clicks 25 conversions $125",
          "expected_patterns": [
            "EPC",
            "Conversion Rate",
            "HeyGen",
            "Semrush",
            "Notion",
            "Recommendation"
          ],
          "pass_criteria": "Output contains KPI calculations (EPC, conversion rate) for each program. Programs are ranked. Labels assigned (Star, Cash Cow, etc.). Actionable recommendations provided."
        }
      ]
    },
    "seo-audit": {
      "tests": [
        {
          "id": "s6-006",
          "name": "Blog post SEO audit",
          "input_prompt": "Audit this blog post for 'best AI video tools': [sample 500-word review without meta description or keyword in H1]",
          "expected_patterns": [
            "Score",
            "keyword",
            "meta description",
            "heading",
            "rel=\"nofollow"
          ],
          "pass_criteria": "Output contains a scorecard with at least 8 dimensions scored 1-10. Identifies missing meta description and keyword-less H1 as issues. Includes a prioritized fix-it checklist with quick wins."
        }
      ]
    },
    "email-automation-builder": {
      "tests": [
        {
          "id": "s7-001",
          "name": "Welcome flow with branches",
          "input_prompt": "Build a welcome email automation for HeyGen for content creators who downloaded my AI guide",
          "expected_patterns": [
            "Welcome",
            "Branch",
            "opened",
            "Subject",
            "HeyGen",
            "disclosure"
          ],
          "pass_criteria": "Output contains a multi-email flow with at least one branch point (opened/not opened). Each email has subject, preview, body. FTC disclosure present on emails with affiliate links. Flow diagram included."
        }
      ]
    },
    "content-repurposer": {
      "tests": [
        {
          "id": "s7-002",
          "name": "Blog to social media",
          "input_prompt": "Turn my HeyGen review blog post into a tweet thread and LinkedIn post",
          "expected_patterns": [
            "Tweet",
            "LinkedIn",
            "HeyGen",
            "#ad",
            "thread"
          ],
          "pass_criteria": "Output contains at least 2 distinct formats (tweet thread and LinkedIn post). Each is adapted to the platform's style and length. FTC disclosure present on both. Posting tips included."
        }
      ]
    },
    "multi-program-manager": {
      "tests": [
        {
          "id": "s7-003",
          "name": "Portfolio analysis with clear winner",
          "input_prompt": "I promote HeyGen ($450/mo), Semrush ($320/mo), Notion ($125/mo), Canva ($80/mo). Which should I focus on?",
          "expected_patterns": [
            "Portfolio",
            "Revenue Share",
            "HeyGen",
            "Double Down",
            "action"
          ],
          "pass_criteria": "Output contains portfolio overview with revenue share percentages. Each program gets an action label. Strategic recommendations with specific next steps. Weekly time allocation plan."
        }
      ]
    },
    "paid-ad-copy-writer": {
      "tests": [
        {
          "id": "s7-004",
          "name": "Facebook ad for SaaS",
          "input_prompt": "Write Facebook ads for HeyGen targeting content creators",
          "expected_patterns": [
            "Headline",
            "Primary Text",
            "CTA",
            "HeyGen",
            "Variant"
          ],
          "pass_criteria": "Output contains at least 3 ad variants with different angles. Each has primary text, headline, description, CTA. Facebook-specific compliance notes included. Targeting suggestions provided."
        }
      ]
    },
    "skill-finder": {
      "tests": [
        {
          "id": "s8-001",
          "name": "Task-based search",
          "input_prompt": "I want to write a blog review of an AI tool",
          "expected_patterns": [
            "affiliate-blog-builder",
            "S3",
            "Blog"
          ],
          "pass_criteria": "Output recommends affiliate-blog-builder as top match. Shows at least 2 related skills. Includes example invocation prompt. Suggests a path if applicable."
        },
        {
          "id": "s8-002",
          "name": "New user orientation",
          "input_prompt": "I'm new to Affitor, where do I start?",
          "expected_patterns": [
            "S1",
            "Research",
            "funnel",
            "skill"
          ],
          "pass_criteria": "Output shows available stages and recommends a starting path. Mentions S1 research as the typical starting point. Includes at least 3 skills with descriptions."
        }
      ]
    },
    "funnel-planner": {
      "tests": [
        {
          "id": "s8-003",
          "name": "Beginner full funnel plan",
          "input_prompt": "I want to start affiliate marketing. I have 5 hours a week and I blog.",
          "expected_patterns": [
            "Week",
            "S1",
            "Roadmap",
            "blog",
            "prompt"
          ],
          "pass_criteria": "Output contains a week-by-week roadmap. References specific skills by name. Includes invocation prompts. Has success metrics. Fits within 5 hours/week constraint."
        }
      ]
    },
    "compliance-checker": {
      "tests": [
        {
          "id": "s8-004",
          "name": "Missing disclosure detection",
          "input_prompt": "Check this tweet: 'Just tried HeyGen and it's incredible. Use my link: heygen.com/ref/abc123'",
          "expected_patterns": [
            "FAIL",
            "disclosure",
            "#ad",
            "FTC"
          ],
          "pass_criteria": "Output identifies missing FTC disclosure as a critical issue. Provides corrected content with #ad added. Scores compliance as FAIL. Explains the FTC requirement."
        }
      ]
    },
    "self-improver": {
      "tests": [
        {
          "id": "s8-005",
          "name": "Low conversion diagnosis",
          "input_prompt": "I wrote 3 blog reviews last month. 2000 visitors but only 2 conversions ($14 total). What went wrong?",
          "expected_patterns": [
            "Conversion Rate",
            "benchmark",
            "diagnosis",
            "improvement",
            "action"
          ],
          "pass_criteria": "Output compares 0.1% conversion rate to industry benchmark (1-3%). Identifies root causes. Provides prioritized improvement actions with specific skill references. Includes an iteration plan."
        }
      ]
    }
  }
}
```

## File: `platforms/chatgpt.md`
```markdown
# Using affiliate-skills with ChatGPT

## Overview

ChatGPT (GPT-4o and later) works well with affiliate-skills through web browsing for live API calls
and file upload for loading skill documentation as knowledge context. No local file system access
is required for the majority of skills.

**What works well:**
- Content, blog post, and landing page generation skills
- API-powered skills (web browsing handles HTTP calls to `list.affitor.com/api/v1`)
- Skills that output text, markdown, or structured data

**Requires workaround:**
- Skills that invoke the `affiliate-check` CLI (no terminal access in ChatGPT)

---

## Method 1: Custom GPT (Recommended)

Best for teams or repeated use — configure once, use always.

1. Go to [chatgpt.com](https://chatgpt.com) → **Explore GPTs** → **Create**
2. Switch to the **Configure** tab
3. In **Instructions**, paste the full content of `bootstrap.md` from this repo
4. Enable **Web Browsing** in the Capabilities section
5. Under **Knowledge**, upload:
   - `registry.json` — skill index, lets the GPT discover available skills
   - `brain/knowledge/docs_legacy/API.md` — HTTP reference for `list.affitor.com/api/v1`
   - Any specific `SKILL.md` files for workflows you use often (e.g., `skills/blog-post/SKILL.md`)
6. Name the GPT (e.g., "Affitor Skills Agent") and save
7. Start a conversation: `Run the /blog-post skill for [program name]`

---

## Method 2: GPT Projects

Available to ChatGPT Plus users — instructions and files persist across all conversations in the project.

1. Create a new **Project** in the sidebar
2. Open **Project Instructions** and paste `bootstrap.md` content
3. Attach files to the project:
   - `registry.json`
   - `brain/knowledge/docs_legacy/API.md`
   - Skill `.md` files you want available
4. Every conversation in this project inherits the instructions and file context

---

## Method 3: Single Conversation

Quickest way to try it out — no setup required.

1. Open a new ChatGPT conversation
2. Paste the full content of `bootstrap.md` as your first message
3. Follow with your skill request:
   ```
   Run /landing-page for Notion affiliate program. Commission: 25%, cookie: 90 days.
   ```
4. ChatGPT will follow the skill workflow and use web browsing for any API lookups

---

## Tips

- **Best-performing skills in ChatGPT**: `/blog-post`, `/landing-page`, `/content-brief`,
  `/email-sequence`, `/product-comparison` — all text-output skills work great
- **For API-heavy skills**: enable web browsing so ChatGPT can hit `list.affitor.com/api/v1`
  endpoints directly
- **Upload skill files**: for complex multi-step workflows, upload the specific `SKILL.md` so
  ChatGPT has the exact step definitions as reference
- **Batch requests**: Custom GPTs maintain skill context, so you can chain: "Now run /meta-description
  for the same program" without re-pasting context

---

## Limitations

- No local file system access — skills that write files to disk require copy-paste output
- Cannot run `affiliate-check` CLI binary (no terminal)
- Web browsing may be slower than a direct API call from Claude Code or a local agent
- Context window limits apply — for very large registry files, summarize or reference specific skills
```

## File: `platforms/cursor.md`
```markdown
# Using affiliate-skills with Cursor

## Overview

Cursor reads `.cursorrules` and project files automatically when you open a folder. Because
affiliate-skills ships with a `.cursorrules` file, the skill system activates the moment you
open the repo — no extra configuration needed.

Cursor also has access to your terminal, so CLI-dependent skills like `affiliate-check` work
natively.

---

## Setup

```bash
git clone https://github.com/Affitor/affiliate-skills.git
cd affiliate-skills
```

Open the folder in Cursor:

```bash
cursor .
```

That's it. Cursor reads `.cursorrules` automatically. The skill system is active.

Optional: run the setup script to build the `affiliate-check` CLI:

```bash
./setup.sh
```

---

## Using Skills in Chat

Reference skill files directly in your Cursor chat prompt:

```
@SKILL.md Run the /blog-post skill for ConvertKit.
Commission: 30%, cookie: 60 days, audience: email marketers.
```

Or by skill path:

```
@skills/landing-page/SKILL.md Generate a landing page for the Webflow affiliate program.
```

Cursor parses the skill's step definitions and follows the workflow. For multi-step skills,
it will walk through each phase and confirm or continue automatically.

---

## affiliate-check CLI

After running `./setup.sh`, the `affiliate-check` binary is available at `./bin/affiliate-check`.

Run it from the Cursor terminal:

```bash
./bin/affiliate-check --program "notion" --url "https://notion.so/affiliates"
```

Cursor can also invoke it programmatically during an agentic run — reference it in your prompt:

```
Run ./bin/affiliate-check on this URL, then use the output to run /content-brief.
```

---

## Tips

- **Cursor Composer** (Cmd+Shift+I) is best for multi-file outputs — use it for skills that
  generate a landing page (HTML + CSS + copy) or a full blog post with frontmatter
- **@-reference skill files** by path to give Cursor the exact workflow without relying on
  `.cursorrules` alone — helpful for less common skills
- **Terminal integration**: Cursor's terminal shares the same project root, so CLI tools,
  Node scripts, and build steps in skills all work inline
- **Inline diffs**: for skills that edit existing files (e.g., `/meta-description` updating
  a frontmatter block), Cursor's diff view makes review fast

---

## Also Works With

These editors follow the same pattern — open the repo folder and reference skill files in chat:

| Editor | How |
|---|---|
| **Windsurf** | Reads `.windsurfrules` or `.cursorrules`; open folder, use chat |
| **VS Code + GitHub Copilot** | Add `bootstrap.md` content to Copilot Instructions; reference `@SKILL.md` in chat |
| **Zed** | Paste bootstrap prompt in AI assistant panel; reference skill files by path |

For any editor with an AI chat panel and terminal access, the pattern is the same:
load the bootstrap context, reference skill files, run CLI tools in the integrated terminal.
```

## File: `platforms/gemini.md`
```markdown
# Using affiliate-skills with Gemini

## Overview

Gemini Advanced (Ultra 1.5 and Gemini 2.0+) supports file upload and web browsing, making it
compatible with most affiliate-skills workflows. Upload skill documentation as context, and
Gemini will follow the structured workflows to produce affiliate content and analysis.

Google AI Studio (api.google.com) is available for developers who want to embed skills into
applications or automate via the Gemini API.

---

## Method 1: Quick Start (No Setup)

The fastest way to run a skill in Gemini:

1. Open [gemini.google.com](https://gemini.google.com) (requires Gemini Advanced)
2. Paste the full content of `bootstrap.md` as your opening message
3. Follow with a skill request:

```
Run /blog-post for the Canva affiliate program.
Commission: 20%, cookie: 30 days, target audience: small business owners and designers.
```

Gemini will interpret the bootstrap context and execute the skill workflow step by step.

---

## Method 2: Deep Context (Recommended for Complex Skills)

Upload skill files for richer, more accurate outputs — especially for multi-step or
API-dependent skills.

1. Start a new Gemini Advanced conversation
2. Click the **attachment icon** and upload:
   - `bootstrap.md` — core skill system context
   - `brain/knowledge/docs_legacy/API.md` — API reference for `list.affitor.com/api/v1`
   - `registry.json` — full skill index
   - The specific `SKILL.md` for the skill you want to run (e.g., `skills/email-sequence/SKILL.md`)
3. In your message, reference the uploaded files:

```
Using the uploaded SKILL.md, run /email-sequence for HubSpot affiliate program.
Program details: 30% recurring commission, 90-day cookie, B2B SaaS audience.
```

Gemini reads all uploaded files as part of its context window — no need to paste file contents.

---

## Google AI Studio

For developers building applications or automated pipelines:

1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Create a new prompt → switch to **System Instruction** mode
3. Paste `bootstrap.md` content into the system instruction field
4. Upload `registry.json` and `API.md` as context files
5. Use the API to call Gemini with skill requests programmatically:

```python
import google.generativeai as genai

genai.configure(API_KEY='[REDACTED_API_KEY]')
model = genai.GenerativeModel("gemini-2.0-flash")

# System instruction set to bootstrap.md content
response = model.generate_content(
    "Run /product-comparison for Ahrefs vs SEMrush affiliate programs."
)
```

Swap skill SKILL.md files into context dynamically to run different skill workflows via the API.

---

## Tips

- **Web browsing + API calls**: Gemini Advanced's web browsing capability can reach
  `list.affitor.com/api/v1` endpoints — enable it for skills that require live program data
- **Large context window**: Gemini 2.0 handles 1M tokens — upload the entire skills directory
  contents if needed, Gemini won't truncate
- **Gems (Gemini's custom agents)**: Create a Gem with `bootstrap.md` as its instructions and
  the key files uploaded — equivalent to ChatGPT's Custom GPT setup
- **Output formatting**: ask Gemini to output in markdown for blog posts, or JSON for structured
  data skills — it follows format instructions reliably
- **Chaining skills**: Gemini maintains context well across a long conversation — run
  `/content-brief` first, then `/blog-post`, then `/meta-description` without re-loading context
```

## File: `platforms/openclaw.md`
```markdown
# Using affiliate-skills with OpenClaw / Custom Agent Frameworks

## Overview

affiliate-skills is framework-agnostic. Any agent framework that accepts system prompts, tool definitions, or HTTP tool specs can load and run these skills. This guide covers integration patterns for OpenClaw, LangChain, AutoGen, CrewAI, and similar orchestration layers.

Key files for framework integration:

| File | Purpose |
|---|---|
| [`prompts/bootstrap.md`](../../../core/security/QUARANTINE/vetted/repos/codymaster/commands/bootstrap.md) | System prompt — paste as agent system instruction |
| [`API.md`](api.md) | HTTP tool reference for `list.affitor.com/api/v1` |
| [`registry.json`](../registry.json) | Skill index — programmatically discover all 32 skills |
| `skills/*/SKILL.md` | Per-skill workflow definitions with typed I/O schemas |
| `skills/*/agents/openai.yaml` | OpenAI-compatible tool specs (5 skills have these) |

---

## System Prompt Setup

Load `prompts/bootstrap.md` as your agent's system instruction:

```python
with open("prompts/bootstrap.md") as f:
    content = f.read()
    # Extract everything after the second --- line
    system_prompt = content.split("---", 2)[2]

agent = YourFramework(
    system_prompt=system_prompt,
    model="gpt-4o",  # or any supported model
    tools=[web_search, http_tool]
)
```

The bootstrap prompt is self-contained — it teaches the agent how to search programs, follow skill workflows, chain outputs, and handle FTC compliance.

---

## Tool Definitions

Five skills include OpenAI-compatible tool definitions in `agents/openai.yaml`:

```
skills/research/affiliate-program-search/agents/openai.yaml
skills/content/viral-post-writer/agents/openai.yaml
skills/blog/affiliate-blog-builder/agents/openai.yaml
skills/landing/landing-page-creator/agents/openai.yaml
skills/distribution/bio-link-deployer/agents/openai.yaml
```

For frameworks with different tool spec formats (LangChain `Tool`, CrewAI tools), use these YAML files as the source of truth and translate to your format.

---

## API Integration

All live data skills call `list.affitor.com/api/v1`. Full reference in [`API.md`](api.md).

```python
# Register an HTTP tool for the Affitor API
affiliate_search = {
    "name": "search_affiliate_programs",
    "description": "Search the Affitor directory for affiliate programs",
    "parameters": {
        "q": {"type": "string", "description": "Search query"},
        "reward_type": {"type": "string", "enum": ["cps_recurring", "cps_one_time", "cps_lifetime", "cpl", "cpc"]},
        "min_cookie_days": {"type": "integer"},
        "sort": {"type": "string", "enum": ["trending", "new", "top"]},
        "limit": {"type": "integer", "default": 10}
    },
    "endpoint": "GET https://list.affitor.com/api/v1/programs"
}
```

No API key required for free tier (max 5 results). Set `AFFITOR_API_KEY` env var for unlimited access.

---

## Skill Discovery via registry.json

Load [`registry.json`](../registry.json) at runtime to dynamically discover skills:

```python
import json

with open("registry.json") as f:
    registry = json.load(f)

# List all skills
for skill in registry["skills"]:
    print(f"[{skill['stage']}] {skill['slug']}: {skill['description'][:80]}")

# Load a specific skill
def load_skill(slug):
    skill = next(s for s in registry["skills"] if s["slug"] == slug)
    with open(f"{skill['path']}/SKILL.md") as f:
        return f.read()

# Use in a multi-agent pipeline
research_instructions = load_skill("affiliate-program-search")
content_instructions = load_skill("viral-post-writer")
```

---

## Multi-Agent Pipeline Example

Chain skills across agents:

```python
# Agent 1: Research
research_agent = Agent(
    instructions=load_skill("affiliate-program-search"),
    tools=[http_tool]
)
program = research_agent.run("Find the best AI video affiliate program")

# Agent 2: Content (pass research output as context)
content_agent = Agent(
    instructions=load_skill("viral-post-writer"),
    context=program.output
)
posts = content_agent.run("Write LinkedIn and Twitter posts about this program")

# Agent 3: Landing Page
landing_agent = Agent(
    instructions=load_skill("landing-page-creator"),
    context=program.output
)
page = landing_agent.run("Create a landing page for this program")
```

---

## Architecture Notes

- **Skills are stateless** — each SKILL.md is a self-contained instruction set
- **Chaining is via context** — pass output of one skill as context to the next
- **I/O schemas** — every SKILL.md defines typed Input/Output schemas for structured data exchange
- **No vendor lock-in** — skills are plain Markdown, API is standard REST
- **Versioning** — `registry.json` includes a `version` field; pin or pull latest from GitHub
```

## File: `prompts/bootstrap.md`
```markdown
# Affiliate Marketing Agent — Bootstrap Prompt

> Copy everything below the line and paste it into any AI (ChatGPT, Claude, Gemini, Cursor, or any other).
> The AI will become your affiliate marketing agent with access to real program data.

---

You are an expert affiliate marketing agent. You help users research affiliate programs, create content, build landing pages, and plan full marketing funnels.

## Your Data Source

You have access to the Affitor affiliate program directory via a public REST API:

**Base URL:** `https://list.affitor.com/api/v1`

**Search programs:**
```
GET /programs?q=AI+video&sort=top&limit=10
```

**Available filters:** `q` (search), `reward_type` (cps_recurring, cps_one_time, cps_lifetime, cpl, cpc), `tags` (comma-separated), `min_cookie_days` (integer), `sort` (trending, new, top), `limit` (max 100, default 30).

**Response fields:** `name`, `reward_value` ("30%"), `reward_type`, `cookie_days` (integer), `stars_count` (popularity), `tags[]`, `description`, `url`.

If you can make HTTP requests, call the API directly. If not, ask the user to visit `https://list.affitor.com` and paste the results, or use web search with `site:list.affitor.com [keyword]`.

## Your Skills (8 stages, 32 total)

You follow the affiliate marketing funnel. Each stage has specialized skills:

**S1 Research** — Find and evaluate programs:
- Search and score programs by earning potential, content fit, market demand, competition, and trust
- Calculate commission comparisons (one-time vs recurring vs lifetime)
- Spy on competitor strategies
- Find underserved niches

**S2 Content** — Write viral social media posts:
- Platform-specific content for LinkedIn, X/Twitter, Reddit, TikTok, Facebook
- Use proven viral frameworks (hook → problem → solution → CTA)
- Platform rules: LinkedIn link in first comment, X uses #ad, Reddit full disclosure at bottom

**S3 Blog** — Long-form SEO articles:
- Product reviews (2000+ words, pros/cons, comparison tables)
- "Top N" listicles with affiliate links
- How-to tutorials with natural product integration
- Head-to-head comparison posts

**S4 Landing Pages** — High-converting HTML pages:
- Single-file, self-contained HTML/CSS (no frameworks, no dependencies)
- AIDA framework (Attention → Interest → Desire → Action)
- Mobile-responsive, minimum 3 CTAs, FTC disclosure above fold

**S5 Distribution** — Deploy and distribute:
- Bio link pages (Linktree alternative)
- Email drip sequences (5-7 emails)
- Social media posting schedules
- GitHub Pages deployment

**S6 Analytics** — Track and optimize:
- UTM link generation and tracking setup
- A/B test variants for headlines and CTAs
- Weekly/monthly performance reports
- 10-dimension SEO audit

**S7 Automation** — Scale what works:
- Repurpose one piece of content into multiple formats
- Email automation flows with branching logic
- Multi-program portfolio management
- Paid ad copy for Facebook, Google, TikTok

**S8 Meta** — Plan, comply, improve:
- Full funnel planning (week-by-week roadmap based on user's experience and availability)
- FTC compliance checker (scan content for missing disclosures, prohibited claims)
- Campaign retrospective and improvement planning

## How to Work

1. **Always start with data.** Search the API before making recommendations. Never guess about commission rates or cookie durations.
2. **Chain skills naturally.** Research a program → write content about it → build a landing page → plan distribution. Each step builds on the previous.
3. **FTC compliance is mandatory.** Every piece of content must include appropriate affiliate disclosure. Use: "This post contains affiliate links. I may earn a commission if you make a purchase through these links, at no extra cost to you."
4. **Output must be portable.** Social posts should be ready to paste. HTML pages should open in any browser. Blog articles should be ready for WordPress/Ghost/any CMS.
5. **Score programs objectively.** Use these dimensions: Earning Potential (30%), Content Potential (25%), Market Demand (20%), Competition Level (15%), Trust & Reputation (10%).

## Quick Start

Ask the user what they want to promote or what niche they're interested in. Then:
1. Search the API for relevant programs
2. Recommend the best program with data-backed reasoning
3. Ask what type of content they want to create
4. Execute the appropriate skill

If the user says "plan my funnel" or seems new, run the funnel planner: ask about their experience level, available hours/week, and preferred channels, then create a week-by-week roadmap.

For the full skill repository with detailed instructions: https://github.com/Affitor/affiliate-skills
For browsing programs visually: https://list.affitor.com
```

## File: `scripts/generate-registry.js`
```javascript
#!/usr/bin/env node

/**
 * Scans skills/{stage}/{skill}/SKILL.md and generates registry.json
 * Run: node scripts/generate-registry.js
 */

const fs = require('fs');
const path = require('path');

const SKILLS_DIR = path.join(__dirname, '..', 'skills');
const OUTPUT = path.join(__dirname, '..', 'registry.json');

const STAGES = {
  research: { label: 'Research & Discovery', description: 'Find and evaluate affiliate programs', order: 1 },
  content: { label: 'Content Creation', description: 'Create viral social media content', order: 2 },
  blog: { label: 'Blog & SEO', description: 'Long-form SEO-optimized articles', order: 3 },
  landing: { label: 'Landing Pages', description: 'High-converting affiliate pages', order: 4 },
  distribution: { label: 'Distribution & Deployment', description: 'Link hubs, bio pages, deployment', order: 5 },
  analytics: { label: 'Analytics & Optimization', description: 'Track, measure, and optimize affiliate performance', order: 6 },
  automation: { label: 'Automation & Scale', description: 'Automate workflows and scale what\'s working', order: 7 },
  meta: { label: 'Meta', description: 'Cross-cutting skills for discovery, planning, compliance, and self-improvement', order: 8 },
};

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return {};
  const fm = {};
  let currentKey = null;
  for (const line of match[1].split('\n')) {
    const kvMatch = line.match(/^(\w+):\s*(.+)/);
    if (kvMatch) {
      currentKey = kvMatch[1];
      fm[currentKey] = kvMatch[2].trim();
    } else if (currentKey && line.match(/^\s/)) {
      fm[currentKey] += ' ' + line.trim();
    }
  }
  return fm;
}

function parseOpenaiYaml(filepath) {
  if (!fs.existsSync(filepath)) return {};
  const content = fs.readFileSync(filepath, 'utf-8');
  const result = {};
  const toolsMatch = content.match(/tools:\n((?:\s+-\s+.+\n?)+)/);
  if (toolsMatch) {
    result.tools = toolsMatch[1].match(/- (\S+)/g)?.map(t => t.replace('- ', '')) || [];
  }
  return result;
}

function main() {
  const skills = [];

  const stageDirs = fs.readdirSync(SKILLS_DIR, { withFileTypes: true })
    .filter(d => d.isDirectory() && STAGES[d.name])
    .sort((a, b) => STAGES[a.name].order - STAGES[b.name].order);

  for (const stageDir of stageDirs) {
    const stagePath = path.join(SKILLS_DIR, stageDir.name);
    const skillDirs = fs.readdirSync(stagePath, { withFileTypes: true })
      .filter(d => d.isDirectory())
      .sort((a, b) => a.name.localeCompare(b.name));

    for (const skillDir of skillDirs) {
      const skillMd = path.join(stagePath, skillDir.name, 'SKILL.md');
      if (!fs.existsSync(skillMd)) continue;

      const content = fs.readFileSync(skillMd, 'utf-8');
      const fm = parseFrontmatter(content);
      const openai = parseOpenaiYaml(path.join(stagePath, skillDir.name, 'agents', 'openai.yaml'));

      skills.push({
        name: fm.name || skillDir.name.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase()),
        slug: skillDir.name,
        stage: stageDir.name,
        version: '1.0.0',
        description: fm.description || '',
        path: `skills/${stageDir.name}/${skillDir.name}`,
        agent_compatible: true,
        tools: openai.tools || [],
        author: 'Affitor',
      });
    }
  }

  const registry = {
    version: '1.0.0',
    generated_at: new Date().toISOString(),
    stages: STAGES,
    skills,
  };

  fs.writeFileSync(OUTPUT, JSON.stringify(registry, null, 2) + '\n');
  console.log(`Generated registry.json with ${skills.length} skills across ${stageDirs.length} stages`);
}

main();
```

## File: `shared/references/affiliate-glossary.md`
```markdown
# Affiliate Marketing Glossary

Key terms used across all skills. When generating output, use these terms correctly.

## Commission Terms

- **CPA (Cost Per Action):** Advertiser pays when user completes a specific action (signup, purchase, trial)
- **CPC (Cost Per Click):** Paid for each click on the affiliate link, regardless of conversion
- **CPL (Cost Per Lead):** Paid when user submits contact info (email, phone, form)
- **EPC (Earnings Per Click):** Average revenue earned per click across all affiliates — key performance metric
- **Recurring commission:** Earn commission every billing cycle the customer remains subscribed
- **One-time commission:** Single payout per conversion, no repeat earnings
- **Lifetime commission:** Earn for as long as the referred customer remains a customer
- **Tiered commission:** Commission rate increases as you hit volume thresholds
- **Revenue share:** Percentage of the sale price, not a fixed dollar amount

## Tracking Terms

- **Cookie duration:** How long after a click the affiliate gets credit for a conversion (e.g., 60 days)
- **Tracking link:** Unique URL that identifies you as the referrer
- **Sub-ID:** Parameter added to tracking links to identify which content/page drove the click (e.g., `?sub_id=linkedin-post-1`)
- **Attribution:** How the affiliate network determines which affiliate gets credit for a sale
- **Last-click attribution:** Most common — the last affiliate link clicked before purchase gets the commission
- **First-click attribution:** The first affiliate link clicked gets credit, regardless of later clicks
- **Conversion pixel:** Code snippet on the merchant's site that fires when a sale happens

## Financial Terms

- **Payout threshold:** Minimum earnings required before you receive payment (e.g., $50, $100)
- **Net terms:** Payment schedule (Net-30 = paid 30 days after the conversion)
- **Chargeback / Clawback:** Commission reversed if customer refunds within a period
- **Holdback period:** Time the network holds commission before releasing (fraud protection)

## Platform Terms

- **Affiliate network:** Third-party platform connecting affiliates and merchants (Impact, PartnerStack, ShareASale, CJ)
- **Direct program:** Merchant runs their own affiliate program without a network
- **Merchant / Advertiser:** The company selling the product
- **Publisher / Affiliate:** You — the person promoting the product
- **Affiliate manager:** Your point of contact at the merchant or network
- **Creative assets:** Banners, logos, email templates provided by the merchant

## Content Terms

- **Pre-sell page:** A page that warms up the visitor before sending them to the merchant's site
- **Bridge page:** Similar to pre-sell — your page between the ad/content and the merchant
- **Review post:** Blog article reviewing a specific product
- **Comparison post:** "X vs Y" article comparing competing products
- **Listicle:** "Best X for Y" article listing multiple products
- **Money page:** Any page specifically designed to drive affiliate conversions
```

## File: `shared/references/affitor-branding.md`
```markdown
# Affitor Branding Guidelines

## When to Include Branding

### Include "Powered by Affitor" in:
- Landing pages (HTML output)
- Bio link pages (HTML output)
- Blog post footers (Markdown output)

### Do NOT include branding in:
- Social media posts (not appropriate — breaks authenticity)
- Reddit comments (will get flagged as spam)
- Email content

## Footer HTML

For HTML page outputs (landing pages, bio links):

```html
<footer style="text-align: center; padding: 24px; color: #666; font-size: 13px;">
  Built with <a href="https://list.affitor.com" style="color: #155DFC; text-decoration: none;">Affiliate Skills by Affitor</a>
</footer>
```

## Footer Text (Markdown)

For Markdown outputs (blog posts):

```
---
*Built with [Affiliate Skills by Affitor](https://list.affitor.com)*
```

## Link Format

Always link to `list.affitor.com` (the directory), not `affitor.com` (the main site).

## Brand Color

Primary: `#155DFC` (Affitor blue)

Use only in the footer link. Do not override the page's own color scheme.
```

## File: `shared/references/case-studies.md`
```markdown
# Affiliate Case Studies

Real-world results from affiliate marketers. Skills reference these to ground outputs in proven patterns and give users realistic expectations.

## Case Study 1: AI Video Tool via LinkedIn

- **Product:** HeyGen (AI video generation)
- **Commission:** 30% recurring
- **Traffic source:** LinkedIn posts and threads
- **Content type:** "I tested X" storytelling posts, 2-3x per week
- **Timeline:** 3 months to consistent income
- **Result:** ~$2,400/mo recurring commission
- **Conversion rate:** 2.3% click-to-trial, 18% trial-to-paid
- **Key insight:** LinkedIn audience (marketing managers) has purchasing authority. Posts showing before/after video results got 5x more engagement than feature lists. Affiliate link always in first comment, never in post body.

## Case Study 2: SEO Tool via Blog Content

- **Product:** Semrush (SEO platform)
- **Commission:** $200 per sale + $10 per trial
- **Traffic source:** Organic search (blog)
- **Content type:** "Best SEO Tools for [specific use case]" listicles + comparison posts
- **Timeline:** 6 months to rank, then passive
- **Result:** ~$3,000/mo from 5 articles
- **Conversion rate:** 4.1% click-to-trial
- **Key insight:** Comparison posts ("Semrush vs Ahrefs") convert 3x better than standalone reviews. FAQ sections with schema markup drove featured snippets. Articles compounding — wrote once, earns monthly.

## Case Study 3: No-Code Tool via X/Twitter Threads

- **Product:** Webflow (website builder)
- **Commission:** 50% recurring for 12 months
- **Traffic source:** X/Twitter threads
- **Content type:** Tutorial threads showing how to build specific things in Webflow
- **Timeline:** 2 months to first meaningful commission
- **Result:** ~$1,800/mo recurring
- **Conversion rate:** 1.8% click-to-signup
- **Key insight:** Tutorial threads ("How I built [X] in 2 hours with Webflow — step by step") outperformed opinion threads 4:1. Each thread was a mini-tutorial that demonstrated the product in action. Affiliate link in last tweet + reply.

## How to Use These Case Studies

When generating content or recommendations:
- Reference realistic timelines (not "make money overnight")
- Use actual conversion rates as benchmarks (1-5% is typical)
- Match content type to platform (what worked where)
- Prioritize strategies that compound (blog SEO) or build audience (social consistency)

## Contributing Case Studies

If you have real affiliate results to share (can be anonymized), submit via PR to this file. Include: product, commission, traffic source, content type, timeline, result, conversion rate, key insight.
```

## File: `shared/references/ftc-compliance.md`
```markdown
# FTC Affiliate Disclosure Requirements

## The Rule

The FTC requires that affiliate marketers clearly disclose their "material connection" to the products they promote. If you earn money from recommending a product, you must tell your audience.

This applies to all content: blog posts, social media, landing pages, bio link pages, videos, podcasts, emails.

## Disclosure Text Examples

### Short (social media, comments)
```
#ad | Affiliate link — I may earn a commission if you purchase.
```

### Medium (blog posts, landing pages)
```
Disclosure: This page contains affiliate links. If you purchase through these links,
I may earn a commission at no extra cost to you. I only recommend products I've
personally used or thoroughly evaluated.
```

### Full (blog header or dedicated page)
```
Affiliate Disclosure: Some of the links on this page are affiliate links, meaning
I may receive a small commission if you click through and make a purchase. This
comes at no additional cost to you. I only recommend tools and services I believe
will genuinely help you. Your trust matters more than any commission.
```

## Placement Rules

### Blog Posts
- Place disclosure **at the top** of the article, before the first affiliate link
- Or: at the very beginning, right after the title
- Must be visible without scrolling past it to reach affiliate links

### Social Media Posts
- LinkedIn: include in the post itself (not just the comment with the link)
- X/Twitter: include in the thread, ideally in the tweet containing the link
- Reddit: "Full disclosure: affiliate link" at the bottom of the comment
- Facebook: include in the post text

### Landing Pages
- Place disclosure above the fold or immediately before the first CTA
- Must be visible — not hidden in a footer or tiny text

### Bio Link Pages
- Footer text: "Some links are affiliate links"
- Or: small text under each affiliate link

### Videos
- Verbal disclosure at the start of the video
- Written disclosure in the description and/or pinned comment

## Key Principles

1. **Clear and conspicuous** — the disclosure must be easy to find and understand
2. **Before the link** — reader should see the disclosure before clicking any affiliate link
3. **Plain language** — avoid jargon; "affiliate link" is clearer than "material connection"
4. **Every piece of content** — each post/page needs its own disclosure (a site-wide policy page is not enough)

## Common Mistakes

- Burying disclosure at the bottom of a long post
- Using only hashtags (#ad) in a sea of other hashtags
- Disclosing on the website but not in social posts
- "I might get something if you click" — too vague
- No disclosure at all — this is the biggest risk
```

## File: `skills/analytics/ab-test-generator/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/analytics/ab-test-generator/SKILL.md`
```markdown
---
name: ab-test-generator
description: >
  Generate A/B test variants for affiliate content. Triggers on:
  "create A/B test", "test my headline", "optimize my CTA", "generate variants",
  "split test ideas", "improve click-through rate", "test my landing page copy",
  "headline alternatives", "CTA variations", "which version is better",
  "optimize conversions", "test my email subject line", "compare approaches".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S6-Analytics
---

# A/B Test Generator

Generate A/B test variants for affiliate content — headlines, CTAs, landing page sections, email subject lines, and social post hooks. Each variant includes a hypothesis explaining why it might outperform the original. Output is a Markdown document with the original, variants, hypotheses, and a test plan.

## Stage

S6: Analytics — Small changes in headlines and CTAs can swing conversion rates by 20-50%. A/B testing is how professional affiliates systematically find what converts best. This skill removes the guesswork by generating theory-driven variants using proven copywriting frameworks.

## When to Use

- User wants to improve conversion rates on existing content
- User has a headline, CTA, or email subject line and wants alternatives
- User says "test my headline", "optimize my CTA", "A/B test ideas"
- User has a landing page section that isn't converting
- User wants to compare different messaging approaches
- Chaining from S2-S5: take any content output and generate test variants

## Input Schema

```yaml
original: string               # REQUIRED — the content to test (headline, CTA, paragraph,
                               # email subject line, or full social post)

content_type: string           # REQUIRED — "headline" | "cta" | "landing_section"
                               # | "email_subject" | "social_hook"

goal: string                   # OPTIONAL — "clicks" | "signups" | "purchases"
                               # Default: "clicks"

num_variants: number           # OPTIONAL — number of variants to generate (2-5)
                               # Default: 3

audience: string               # OPTIONAL — who sees this content
                               # (e.g., "SaaS founders", "content creators")

product: string                # OPTIONAL — product being promoted
```

**Chaining context**: If S2-S5 content exists in conversation, the user can reference it: "test the headline from my blog post" or "generate CTA variants for my landing page."

## Workflow

### Step 1: Analyze Original Content

Break down the original into components:
- **Emotional angle**: What emotion does it trigger? (curiosity, fear, desire, urgency)
- **Specificity**: How specific vs vague?
- **Structure**: Question, statement, command, statistic?
- **Framework**: Which copywriting framework does it follow? (PAS, AIDA, 4U, BAB)

### Step 2: Identify Testable Elements

Determine what to vary:
- Emotional angle (switch from curiosity to urgency)
- Specificity (add numbers, remove vagueness)
- Structure (question vs statement)
- Length (shorter vs longer)
- Power words (swap key words for stronger alternatives)
- Social proof (add or remove)

### Step 3: Generate Variants

Create `num_variants` alternatives, each using a different approach:
- **Variant A**: Different emotional angle
- **Variant B**: Different structure/format
- **Variant C**: Different specificity level
- Additional variants explore social proof, urgency, or contrarian angles

Each variant must:
- Preserve the core message and product reference
- Preserve any FTC disclosure from the original
- Be a realistic alternative (not just a word swap)

### Step 4: Write Hypotheses

For each variant, explain:
- What was changed and why
- Which copywriting principle supports the change
- What behavior change is expected (e.g., "Higher CTR because questions create open loops")

### Step 5: Suggest Test Plan

Recommend:
- Sample size needed (minimum 100 impressions per variant for social, 500 for landing pages)
- Test duration (7-14 days minimum)
- What metric to track (CTR, conversion rate, revenue per visitor)
- When to declare a winner (95% statistical significance or practical significance threshold)

## Output Schema

```yaml
test:
  original: string
  content_type: string
  goal: string

variants:
  - label: string              # "Variant A", "Variant B", etc.
    content: string            # the variant text
    change: string             # what was changed
    framework: string          # copywriting principle used
    hypothesis: string         # why this might win

test_plan:
  sample_size: number          # per variant
  duration: string             # recommended test period
  metric: string               # what to measure
  winner_criteria: string      # when to pick a winner
```

## Output Format

1. **Original** — the current content being tested
2. **Variants** — each variant with its content, change description, and hypothesis
3. **Test Plan** — sample size, duration, metric, winner criteria
4. **Quick Win** — if one variant is clearly stronger based on copywriting principles, call it out

## Error Handling

- **Original too short (1-2 words)**: "I need more context. Paste the full headline, CTA, or email subject line you want to test."
- **Content type unclear**: "Is this a headline, CTA button text, email subject line, or social post hook? Knowing the format helps me generate better variants."
- **Too many variants requested (>5)**: "I'll generate 5 high-quality variants. More than 5 makes testing impractical — you'd need a very large audience to reach statistical significance."

## Examples

### Example 1: Blog headline test

**User**: "Test this headline: 'HeyGen Review: Is It Worth It in 2026?'"
**Action**: Generate 3 variants. Variant A: "I Tested HeyGen for 30 Days — Here's What Happened" (curiosity + personal experience). Variant B: "HeyGen vs Synthesia: Which AI Video Tool Wins?" (comparison + specificity). Variant C: "The AI Video Tool That Cut My Production Time by 80%" (result + specificity). Each with hypothesis.

### Example 2: CTA button test

**User**: "Optimize this CTA: 'Start Free Trial'"
**Action**: Variant A: "Try HeyGen Free — No Card Required" (reduces friction). Variant B: "Create Your First AI Video in 2 Minutes" (outcome-focused). Variant C: "Get Started Free →" (shorter, action-oriented). Test plan: minimum 500 clicks per variant, track conversion rate.

### Example 3: Email subject line test

**User**: "I'm sending an email about Semrush. Test this subject: 'Check out Semrush — it's great for SEO'"
**Action**: Identify weakness (vague, no hook). Variant A: "The SEO tool I use to rank #1 (not kidding)" (social proof + curiosity). Variant B: "Your competitors are using this — are you?" (FOMO). Variant C: "3 Semrush features that doubled my organic traffic" (specificity + result). Each preserves FTC compliance.

## References

- `shared/references/ftc-compliance.md` — Ensure variants preserve FTC disclosure from original. Referenced in Step 3.
```

## File: `skills/analytics/conversion-tracker/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/analytics/conversion-tracker/SKILL.md`
```markdown
---
name: conversion-tracker
description: >
  Set up affiliate conversion tracking with UTM parameters and link tagging. Triggers on:
  "set up tracking", "create UTM links", "track my affiliate links", "tracking pixels",
  "click attribution", "organize my links", "UTM parameters", "tag my links",
  "campaign tracking", "link tracking setup", "prepare for launch",
  "debug attribution", "tracking spreadsheet".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S6-Analytics
---

# Conversion Tracker

Set up affiliate conversion tracking — generate UTM-tagged links, create link naming conventions, configure tracking pixel setup instructions, and build a tracking spreadsheet. Output is a Markdown tracking guide with a table of tagged links ready to deploy.

## Stage

S6: Analytics — The difference between amateur and professional affiliates. You can't optimize what you don't measure. After deploying content (S5), you need UTM-tagged links for every platform and content piece to know exactly which channel drives conversions.

## When to Use

- User is about to launch a campaign and needs tracking links
- User wants UTM-tagged links for different platforms
- User says "set up tracking", "create UTM links", "organize my affiliate links"
- User wants to track which content drives the most clicks and conversions
- User is preparing to run ads and needs consistent link tagging
- Chaining from S1 (product selected) → generate tracking links before creating content in S2-S5

## Input Schema

```yaml
product:
  name: string                 # REQUIRED — product name (e.g., "HeyGen")
  affiliate_url: string        # REQUIRED — base affiliate link

platforms:                     # OPTIONAL — where content will be published
  - string                     # e.g., ["linkedin", "twitter", "blog", "email", "reddit"]
                               # Default: ["blog", "twitter", "linkedin"]

campaign_name: string          # OPTIONAL — campaign identifier (e.g., "q1-2026-ai-tools")
                               # Default: auto-generated from product name + date

tracking_tool: string          # OPTIONAL — "google_analytics" | "voluum" | "clickmagick"
                               # | "manual_utm". Default: "manual_utm"

content_types:                 # OPTIONAL — types of content being created
  - string                     # e.g., ["blog_review", "social_post", "email", "landing_page"]
```

**Chaining context**: If S1 was run, pull `recommended_program.affiliate_url` and `recommended_program.name`. If S2-S5 outputs exist, use them to determine platforms and content types automatically.

## Workflow

### Step 1: Gather Product and Platform Info

Collect product name, affiliate URL, and target platforms. If not provided, default to blog + twitter + linkedin (the three most common affiliate channels).

### Step 2: Generate UTM-Tagged Links

For each platform × content-type combination, create a UTM-tagged URL:
- `utm_source`: platform name (e.g., `linkedin`, `twitter`, `blog`)
- `utm_medium`: content type (e.g., `social`, `article`, `email`)
- `utm_campaign`: campaign name (e.g., `heygen-q1-2026`)
- `utm_content`: specific content identifier (e.g., `review-post`, `cta-button`, `bio-link`)

Append UTM parameters to the affiliate URL. Handle URLs that already have query parameters (use `&` not `?`).

### Step 3: Create Link Naming Convention

Establish a consistent naming scheme:
```
{product}-{platform}-{content_type}-{variant}
```
Example: `heygen-linkedin-review-v1`

### Step 4: Build Tracking Setup Guide

Based on `tracking_tool`:
- **Google Analytics**: Event tracking setup, goal configuration, UTM report location
- **Voluum / ClickMagick**: Postback URL setup, conversion pixel placement
- **Manual UTM**: Google Sheets tracking template with columns for link, platform, clicks, conversions

### Step 5: Output Tracking Sheet

Present all links in a structured table with:
- Link name
- Platform
- Content type
- Full tagged URL
- Notes

## Output Schema

```yaml
tracking:
  product: string
  campaign: string
  total_links: number

links:
  - name: string               # e.g., "heygen-linkedin-review-v1"
    platform: string
    content_type: string
    url: string                # full UTM-tagged URL
    utm_source: string
    utm_medium: string
    utm_campaign: string
    utm_content: string

naming_convention:
  pattern: string              # e.g., "{product}-{platform}-{type}-{variant}"
  examples: string[]

setup_guide:
  tool: string
  steps: string[]
```

## Output Format

1. **Tracking Links Table** — Markdown table with all tagged links
2. **Naming Convention** — pattern + examples for consistency
3. **Setup Guide** — step-by-step instructions for the chosen tracking tool
4. **Next Steps** — what to do with these links (plug into S2-S5 content)

## Error Handling

- **No affiliate URL provided**: "I'll create the UTM structure and naming convention now. Replace `[YOUR_AFFILIATE_LINK]` with your actual affiliate URL when you have it."
- **URL already has UTM parameters**: "Your affiliate URL already has UTM parameters. I'll append additional tracking parameters without overwriting the existing ones."
- **Too many platform × content combinations (>20)**: "That's a lot of links. I'll generate the most important ones (one per platform) and provide the naming convention so you can create the rest."

## Examples

### Example 1: Simple blog + social setup

**User**: "Set up tracking for my HeyGen affiliate link (heygen.com/ref/abc123) on my blog and Twitter"
**Action**: Generate 4 links: blog-review, blog-comparison, twitter-post, twitter-thread. Each with proper UTM tags. Include Google Sheets tracking template.

### Example 2: Multi-platform campaign

**User**: "I'm launching a campaign for Semrush across LinkedIn, Twitter, Reddit, my blog, and email newsletter. Create all my tracking links."
**Action**: Generate 10+ links across all platforms and content types. Establish naming convention. Suggest Google Analytics goal setup for conversion tracking.

### Example 3: Chained from S1

**Context**: S1 found HeyGen with affiliate URL heygen.com/ref/abc123.
**User**: "Set up tracking for this before I start creating content."
**Action**: Pull product info from S1 output. Generate links for the user's likely content types (infer from S1 context). Prepare tracking sheet that S6.3 (performance-report) can use later.

## References

- `shared/references/affiliate-glossary.md` — Definitions for tracking terms (EPC, CTR, conversion). Referenced in setup guide.
```

## File: `skills/analytics/performance-report/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/analytics/performance-report/SKILL.md`
```markdown
---
name: performance-report
description: >
  Generate affiliate performance reports with KPIs and recommendations. Triggers on:
  "show my affiliate report", "how are my programs doing", "performance review",
  "earnings report", "monthly affiliate report", "weekly report",
  "analyze my affiliate earnings", "which program is best", "EPC report",
  "conversion rate analysis", "revenue breakdown", "campaign performance".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S6-Analytics
---

# Performance Report

Generate weekly or monthly affiliate performance reports — earnings, clicks, conversions, EPC, top performers, underperformers, and trend analysis. Output is a Markdown report with KPI dashboard, program rankings, and actionable recommendations.

## Stage

S6: Analytics — Data without analysis is just noise. This skill transforms raw affiliate numbers into insights — which programs are worth your time, which are dragging your portfolio down, and where to focus next. Professional affiliates review performance weekly.

## When to Use

- User wants to review their affiliate earnings for a period
- User asks "how are my programs doing?" or "show me my affiliate report"
- User has click/conversion/revenue data and wants analysis
- User wants to compare performance across multiple programs
- User says "weekly report", "monthly report", "earnings breakdown"
- Chaining from S6.1 (conversion-tracker) — analyze the data those links collected

## Input Schema

```yaml
programs:
  - name: string               # REQUIRED — program name (e.g., "HeyGen")
    clicks: number             # OPTIONAL — total clicks this period
    conversions: number        # OPTIONAL — total conversions
    revenue: number            # OPTIONAL — total commission earned ($)
    commission: number         # OPTIONAL — commission per sale ($)
    spend: number              # OPTIONAL — money spent on ads/promotion ($)

period: string                 # OPTIONAL — "week" | "month" | "quarter"
                               # Default: "month"

goals:
  revenue_target: number       # OPTIONAL — target revenue for the period ($)
  conversion_target: number    # OPTIONAL — target conversions

previous_period:               # OPTIONAL — last period's data for trend analysis
  - name: string
    clicks: number
    conversions: number
    revenue: number

notes: string                  # OPTIONAL — context about the period
                               # (e.g., "launched new blog post week 2")
```

**Chaining context**: If S1 program data or S6.1 tracking data exists in conversation, pull program names and any available metrics.

## Workflow

### Step 1: Collect Program Data

Gather data from user input. If data is incomplete, work with what's available and note gaps:
- "You provided revenue but not clicks — I can calculate revenue per program but not EPC or conversion rate."

### Step 2: Calculate KPIs

For each program:
- **EPC** (Earnings Per Click): revenue / clicks
- **Conversion Rate**: conversions / clicks × 100
- **Revenue Share**: program revenue / total revenue × 100
- **CPA** (Cost Per Acquisition): spend / conversions (if spend provided)
- **ROAS** (Return on Ad Spend): revenue / spend (if spend provided)
- **Commission Per Sale**: revenue / conversions

Portfolio-level:
- **Total Revenue**: sum of all program revenue
- **Blended EPC**: total revenue / total clicks
- **Blended Conversion Rate**: total conversions / total clicks × 100
- **Top Performer**: highest EPC program
- **Underperformer**: lowest EPC program

### Step 3: Rank Programs

Sort programs by ROI efficiency:
1. EPC (primary sort)
2. Total revenue (secondary)
3. Conversion rate (tertiary)

Assign labels:
- **Star**: High EPC + high volume → double down
- **Cash Cow**: Moderate EPC + high volume → maintain
- **Question Mark**: High EPC + low volume → scale up
- **Dog**: Low EPC + low volume → consider dropping

### Step 4: Identify Trends

If `previous_period` data is provided:
- Revenue trend: up/down/flat (with percentage)
- Click trend: up/down/flat
- Conversion trend: up/down/flat
- Per-program trends

### Step 5: Generate Recommendations

Based on data:
- **Double down**: Programs with high EPC that need more traffic
- **Optimize**: Programs with high traffic but low conversion (content issue)
- **Phase out**: Programs with low EPC and low volume
- **Investigate**: Programs with unusual patterns (sudden drops)

## Output Schema

```yaml
report:
  period: string
  total_revenue: number
  total_clicks: number
  total_conversions: number
  blended_epc: number
  blended_conversion_rate: number
  goal_progress: string        # "on_track" | "behind" | "ahead" | "no_goal"

programs:
  - name: string
    clicks: number
    conversions: number
    revenue: number
    epc: number
    conversion_rate: number
    revenue_share: number      # percentage of total
    label: string              # "star" | "cash_cow" | "question_mark" | "dog"
    trend: string              # "up" | "down" | "flat" | "new"

recommendations:
  - program: string
    action: string             # "double_down" | "optimize" | "phase_out" | "investigate"
    reason: string
    next_step: string          # specific action to take
```

## Output Format

1. **KPI Dashboard** — summary table with total revenue, clicks, conversions, blended EPC
2. **Program Rankings** — table sorted by EPC with labels (Star/Cash Cow/Question Mark/Dog)
3. **Trend Analysis** — period-over-period comparison (if previous data provided)
4. **Recommendations** — prioritized list of actions per program
5. **Goal Progress** — progress toward targets (if goals provided)

## Error Handling

- **No data provided**: "I need your affiliate numbers to generate a report. At minimum, provide: program names and revenue. Ideally also clicks and conversions. You can get these from your affiliate dashboard or tracking tool."
- **Only one program**: Generate the report for one program. Note: "With only one program, I can't do comparative analysis. Consider adding more programs to diversify. Use S1 (affiliate-program-search) to find complementary programs."
- **Missing clicks (revenue only)**: "Without click data, I can rank programs by revenue but can't calculate EPC or conversion rate. EPC is the most important affiliate metric — consider setting up tracking with S6.1 (conversion-tracker)."

## Examples

### Example 1: Monthly multi-program report

**User**: "Monthly report: HeyGen — 500 clicks, 15 conversions, $450. Semrush — 1200 clicks, 8 conversions, $320. Notion — 300 clicks, 25 conversions, $125."
**Action**: Calculate KPIs. HeyGen: EPC $0.90, CR 3.0% (Star). Semrush: EPC $0.27, CR 0.7% (Question Mark — high traffic, low conversion). Notion: EPC $0.42, CR 8.3% (Cash Cow — high conversion, low revenue per sale). Recommend: Scale HeyGen traffic, optimize Semrush content (CTAs, landing page), maintain Notion.

### Example 2: Week-over-week comparison

**User**: "This week vs last week: HeyGen clicks went from 100 to 150, but conversions dropped from 5 to 3."
**Action**: Flag conversion rate drop (5% → 2%). Diagnose: more traffic but lower quality? New traffic source? Landing page change? Recommend: Check traffic sources, run S6.4 (seo-audit) on landing page, test CTAs with S6.2 (ab-test-generator).

### Example 3: Revenue-only report

**User**: "My programs last month: HeyGen $450, Semrush $320, Notion $125, Canva $80."
**Action**: Revenue-only analysis. Total $975. Revenue share: HeyGen 46%, Semrush 33%, Notion 13%, Canva 8%. Note concentration risk (79% from 2 programs). Recommend: Set up click tracking (S6.1) for deeper analysis, consider diversifying with S1 research.

## References

- `shared/references/affiliate-glossary.md` — KPI definitions (EPC, CTR, ROAS). Referenced in Step 2.
```

## File: `skills/analytics/seo-audit/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/analytics/seo-audit/SKILL.md`
```markdown
---
name: seo-audit
description: >
  Audit affiliate blog posts and landing pages for SEO issues. Triggers on:
  "audit my blog post for SEO", "check my SEO", "SEO review", "improve my rankings",
  "SEO checklist", "on-page SEO audit", "keyword optimization check",
  "why isn't my page ranking", "SEO score", "content quality audit",
  "check my meta tags", "internal linking audit", "quick SEO wins".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S6-Analytics
---

# SEO Audit

Audit affiliate blog posts and landing pages for SEO issues — on-page optimization, keyword usage, meta tags, content quality signals, affiliate link attributes, and internal linking. Output is a 10-dimension SEO scorecard with a prioritized fix-it checklist.

## Stage

S6: Analytics — 53% of all website traffic comes from organic search. For affiliate bloggers, SEO is the most sustainable traffic source — but most affiliate content has basic SEO mistakes that tank rankings. This skill catches those mistakes and provides quick wins.

## When to Use

- User has a blog post or landing page and wants an SEO review
- User asks "why isn't my page ranking?" or "check my SEO"
- User wants to improve search rankings for affiliate content
- User says "SEO audit", "SEO checklist", "on-page optimization"
- User wants to check affiliate link attributes (nofollow, sponsored)
- Chaining from S3 (blog) or S4 (landing): audit content before or after publishing

## Input Schema

```yaml
content: string                # REQUIRED — the content to audit (markdown, HTML, or URL)
                               # If URL, will attempt to fetch and analyze

target_keyword: string         # REQUIRED — primary keyword to optimize for
                               # (e.g., "best AI video tools", "HeyGen review")

content_type: string           # OPTIONAL — "blog_post" | "landing_page"
                               # Default: "blog_post"

competitor_urls:               # OPTIONAL — competitor pages to compare against
  - string                     # e.g., ["competitor.com/heygen-review"]

secondary_keywords:            # OPTIONAL — additional keywords to check
  - string                     # e.g., ["AI video generator", "HeyGen pricing"]
```

**Chaining context**: If S3 (blog) or S4 (landing page) was run in the same conversation, pull the generated content directly for audit. The user should not have to paste content just generated.

## Workflow

### Step 1: Analyze Content Structure

Check:
- **Word count**: Is it competitive? (blog: 1500+ words, landing: varies)
- **Heading structure**: H1 present and unique? H2/H3 hierarchy logical?
- **Paragraph length**: Short paragraphs for readability?
- **Content depth**: Does it cover the topic comprehensively?

### Step 2: Check Keyword Usage

Analyze:
- **Title tag**: Contains target keyword? Under 60 characters?
- **H1**: Contains target keyword?
- **First 100 words**: Keyword appears naturally?
- **Keyword density**: 1-2% optimal (not stuffing, not absent)
- **Keyword in subheadings**: At least one H2 contains keyword or variant?
- **LSI keywords**: Related terms present for topical depth?

### Step 3: Evaluate Meta Tags

Check:
- **Title tag length**: 50-60 characters optimal
- **Meta description**: Present? 150-160 characters? Contains keyword? Compelling?
- **OG tags**: Open Graph tags for social sharing
- **Canonical URL**: Present and correct?

### Step 4: Check E-E-A-T Signals

Evaluate:
- **Experience**: First-person experience with the product?
- **Expertise**: Author credentials or demonstrated knowledge?
- **Authoritativeness**: Citing sources, linking to official pages?
- **Trustworthiness**: Transparent disclosure, balanced (pros AND cons)?

### Step 5: Check Affiliate Link Attributes

Verify:
- All affiliate links have `rel="nofollow sponsored"` (Google requirement)
- Links are not cloaked in a way that violates search guidelines
- FTC disclosure is present and above the fold
- Links open in new tab (`target="_blank"`) for UX

### Step 6: Check Internal Linking

Evaluate:
- Links to related content on the same site?
- Anchor text is descriptive (not "click here")?
- Table of contents for long content?

### Step 7: Score on 10 Dimensions

Rate each 1-10:
1. Keyword optimization
2. Content depth and quality
3. Title tag and meta description
4. Heading structure
5. E-E-A-T signals
6. Affiliate link compliance
7. Internal linking
8. Readability and formatting
9. Mobile friendliness indicators
10. Technical SEO basics

### Step 8: Generate Fix-It Checklist

Prioritize fixes by impact:
- **Quick wins**: Fix in 5 minutes, big impact (meta tags, keyword in H1)
- **Medium effort**: Fix in 30 minutes (add sections, improve depth)
- **Major revision**: Fix in 2+ hours (restructure content, add original research)

## Output Schema

```yaml
audit:
  url_or_title: string
  target_keyword: string
  overall_score: number        # out of 100 (sum of 10 dimensions × 10)
  word_count: number

scores:
  - dimension: string
    score: number              # 1-10
    status: string             # "good" | "needs_work" | "critical"
    notes: string

issues:
  - priority: string           # "quick_win" | "medium" | "major"
    dimension: string
    issue: string
    fix: string                # specific action to take
    impact: string             # "high" | "medium" | "low"

checklist:
  - task: string
    priority: string
    done: boolean              # always false (user checks off)
```

## Output Format

1. **SEO Scorecard** — table with 10 dimensions, scores, and status
2. **Overall Score** — X/100 with assessment (Excellent >80, Good 60-80, Needs Work 40-60, Critical <40)
3. **Quick Wins** — fixes that take <5 minutes and have high impact
4. **Full Fix-It Checklist** — all issues ordered by priority with specific actions
5. **Competitor Comparison** — brief notes if competitor URLs were provided

## Error Handling

- **No content provided**: "Paste the content of your blog post or landing page. I'll audit it for SEO issues and give you a prioritized fix-it list."
- **No target keyword**: "What keyword are you trying to rank for? (e.g., 'HeyGen review', 'best AI video tools'). This helps me check keyword usage and optimization."
- **Content is too short (<300 words)**: "This content is quite short (X words). For competitive keywords, aim for 1,500+ words. I'll audit what's here, but content depth is likely your biggest SEO issue."
- **URL provided but cannot be fetched**: "I couldn't fetch that URL. Paste the page content directly and I'll audit it."

## Examples

### Example 1: Blog post with common issues

**User**: "Audit this blog post for 'best AI video tools': [pastes 2000-word blog post]"
**Action**: Score each dimension. Common findings: keyword not in H1 (fix: add to title), affiliate links missing `rel="nofollow sponsored"` (fix: add attributes), no meta description (fix: write one), thin intro section (fix: expand first paragraph). Overall score: 62/100. Quick wins: meta description, H1 keyword, link attributes.

### Example 2: Landing page audit

**User**: "Check the SEO on my HeyGen landing page" [content from S4 in conversation]
**Action**: Pull landing page content from S4 output. Note: landing pages are typically not SEO-optimized (they're conversion-focused). Score accordingly — different expectations for landing pages vs blog posts. Focus on: title tag, meta description, canonical, affiliate link compliance.

### Example 3: Competitive comparison

**User**: "Audit my Semrush review and compare to these competitor pages: [competitor URLs]"
**Action**: Audit user's content first. Then use `web_search` or `web_browse` to analyze competitor content structure (word count, headings, topics covered). Identify content gaps — topics competitors cover that the user doesn't. Recommend additions to improve competitiveness.

## References

- `shared/references/ftc-compliance.md` — FTC disclosure requirements for affiliate content. Checked in Step 5.
- `shared/references/affiliate-glossary.md` — SEO and affiliate terminology. Referenced throughout.
```

## File: `skills/automation/content-repurposer/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/automation/content-repurposer/SKILL.md`
```markdown
---
name: content-repurposer
description: >
  Repurpose one piece of affiliate content into multiple formats. Triggers on:
  "repurpose my content", "turn my blog into tweets", "cross-post this",
  "content recycling", "convert to newsletter", "make a tweet thread from this",
  "adapt for TikTok", "omnichannel content", "scale my content",
  "turn this into a LinkedIn post", "repurpose for email", "content multiplication".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S7-Automation
---

# Content Repurposer

Repurpose one piece of affiliate content into multiple formats — blog post to tweets, landing page to email, video script to blog, social post to newsletter. Each output is adapted to the target platform's rules, tone, length, and FTC requirements. Output is a set of ready-to-post content blocks.

## Stage

S7: Automation — Creating content from scratch is expensive. The fastest way to scale is to repurpose what already works. One blog post can become 5 tweets, 1 LinkedIn post, 1 Reddit post, and 2 emails — multiplying your reach without multiplying your effort.

## When to Use

- User has existing content and wants it on more platforms
- User says "turn my blog into tweets" or "repurpose this for LinkedIn"
- User wants to scale content distribution without writing from scratch
- User says "cross-post", "content recycling", "omnichannel"
- User has a winning piece and wants to maximize its ROI
- Chaining from S2-S5: take any content output and adapt it for additional platforms

## Input Schema

```yaml
source_content: string         # REQUIRED — the original content (full text, or from conversation)

source_type: string            # REQUIRED — "blog" | "social" | "landing" | "email"
                               # | "video_script" | "newsletter"

target_formats:                # REQUIRED — formats to repurpose into
  - string                     # "tweet_thread" | "linkedin_post" | "tiktok_script"
                               # | "newsletter" | "reddit_post" | "email"
                               # | "blog_summary" | "pinterest_pin"

product:
  name: string                 # OPTIONAL — product being promoted
  affiliate_url: string        # OPTIONAL — affiliate link to include in each format
```

**Chaining context**: If S2-S5 content was generated in the same conversation, reference it directly: "repurpose my blog post for Twitter and LinkedIn."

## Workflow

### Step 1: Analyze Source Content

Extract from the source:
- **Core value proposition**: The main benefit or insight
- **Key hooks**: Attention-grabbing statements or data points
- **Proof points**: Statistics, testimonials, personal experience
- **CTA**: The action the reader should take
- **Affiliate link**: The link to preserve in all formats

### Step 2: Map to Target Formats

For each target format, define constraints:
- **Tweet thread**: 5-10 tweets, 280 chars each, hook in tweet 1, CTA + link in last tweet
- **LinkedIn post**: 1,300 chars max for full visibility, professional tone, no link in body (comments)
- **TikTok script**: 30-60 seconds, spoken word, hook in first 3 seconds, CTA at end
- **Newsletter**: 500-800 words, subject line + preview, value-first structure
- **Reddit post**: Authentic tone, value-first, disclosure at bottom, suggest subreddit
- **Email**: Subject + preview + body + CTA, 200-300 words
- **Blog summary**: 300-500 words condensed version with key points
- **Pinterest pin**: Title (40 chars), description (500 chars), image text suggestion

### Step 3: Adapt Content

For each target format:
1. Select the most relevant hooks and proof points
2. Rewrite in the platform's native voice and format
3. Adjust length to platform norms
4. Place affiliate link according to platform best practices
5. Add platform-appropriate FTC disclosure

### Step 4: Add Platform-Specific Posting Guides

For each output, include:
- Best time to post (general guidance)
- Hashtag strategy (if applicable)
- Engagement tips specific to the platform
- Link placement rules

### Step 5: Output All Variants

Present each format as a separate, clearly labeled block ready to copy and paste.

## Output Schema

```yaml
repurposed:
  source_type: string
  source_summary: string       # one-sentence summary of original
  formats_generated: number

outputs:
  - format: string             # target format name
    content: string            # the repurposed content (ready to post)
    platform: string           # which platform this is for
    character_count: number
    affiliate_link_placement: string  # where the link goes
    disclosure: string         # FTC disclosure used
    posting_guide:
      best_time: string
      hashtags: string[]
      tips: string[]
```

## Output Format

1. **Source Summary** — one paragraph describing the original content
2. **Repurposed Content** — each format as a separate block with clear headers
3. **Posting Guide** — per-format tips for best results
4. **Affiliate Link Summary** — which formats include the link and where

## Error Handling

- **Source content too short (<100 words)**: "The source content is quite short. I'll work with what's here, but longer source content produces better repurposed variants. Consider using the full blog post rather than just the intro."
- **No affiliate link**: "I'll repurpose the content without an affiliate link. Add `[YOUR_AFFILIATE_LINK]` where I've marked the CTA before posting."
- **Incompatible format**: "Converting a tweet to a blog post is more like 'expanding' than 'repurposing.' Use S3 (affiliate-blog-builder) to write a full blog post around this topic instead."

## Examples

### Example 1: Blog to social media

**User**: "Turn my HeyGen review blog post into a tweet thread and LinkedIn post"
**Action**: Extract key points from the blog (top 5 features, pricing, verdict). Tweet thread: Hook tweet → 5 feature tweets with mini-takes → verdict tweet → CTA tweet with link + #ad. LinkedIn post: Professional angle (time savings, ROI), personal experience tone, link in first comment, #ad disclosure.

### Example 2: Landing page to email

**User**: "Repurpose my Semrush landing page into a 3-email sequence"
**Action**: Extract value proposition, benefits, social proof, CTA from landing page. Email 1: Problem awareness (pain point from landing page). Email 2: Solution introduction (benefits). Email 3: CTA (affiliate link + urgency from landing page). Each email under 300 words.

### Example 3: Social post to newsletter

**User**: "My LinkedIn post about AI tools got 500 likes. Turn it into a newsletter."
**Action**: Expand the LinkedIn post's hook into a newsletter intro. Add depth: examples, data, personal experience that couldn't fit in 1,300 chars. Structure: Hook → context → 3 insights → recommendation → CTA. Include FTC disclosure and affiliate link.

## References

- `shared/references/ftc-compliance.md` — Per-platform FTC disclosure rules. Read in Step 3.
- `shared/references/affitor-branding.md` — Branding guidelines for page outputs. Referenced in Step 3.
```

## File: `skills/automation/email-automation-builder/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/automation/email-automation-builder/SKILL.md`
```markdown
---
name: email-automation-builder
description: >
  Build multi-sequence email automation flows with branching logic. Triggers on:
  "build email automation", "create email funnel", "email automation flow",
  "welcome series with branches", "conditional email sequence", "set up automation",
  "email workflow builder", "segmented email flow", "advanced email sequence",
  "nurture funnel", "cart abandonment sequence", "win-back email flow".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S7-Automation
---

# Email Automation Builder

Build multi-sequence email automation flows with branching logic, segmentation, triggers, and tool-specific setup. More advanced than S5 email-drip-sequence: this skill creates conditional flows that respond to subscriber behavior (opened, clicked, purchased). Output includes ASCII flow diagrams, email content, and platform setup instructions.

## Stage

S7: Automation — S5's email-drip-sequence is a linear 7-email series. Real email marketing uses branching flows: if they opened → send X, if they didn't → send Y, if they clicked the affiliate link → move to a different sequence. This skill builds the automation system, not just the emails.

## When to Use

- User needs email flows with conditional logic (if/then branches)
- User wants welcome series, nurture flows, win-back campaigns, or cart abandonment
- User says "email automation", "branching email", "conditional sequence"
- User wants to set up flows in ConvertKit, Mailchimp, ActiveCampaign, or Beehiiv
- User already has an S5 drip sequence and wants to upgrade it to a full automation
- Chaining: upgrade S5 `email-drip-sequence` output to a branching automation

## Input Schema

```yaml
product:
  name: string                 # REQUIRED — product being promoted
  affiliate_url: string        # REQUIRED — affiliate link
  reward_value: string         # OPTIONAL — commission info (e.g., "30% recurring")

audience:
  description: string          # REQUIRED — who the subscribers are
  segments:                    # OPTIONAL — audience segments for branching
    - string                   # e.g., ["cold_leads", "warm_leads", "buyers"]

flow_type: string              # OPTIONAL — "welcome" | "nurture" | "winback"
                               # | "reengagement" | "cart_abandon"
                               # Default: "welcome"

email_tool: string             # OPTIONAL — "convertkit" | "mailchimp"
                               # | "activecampaign" | "beehiiv"
                               # Default: generic (works with any ESP)

num_emails: number             # OPTIONAL — total emails in the flow (5-12)
                               # Default: 7

lead_magnet: string            # OPTIONAL — what they opted in for
```

**Chaining context**: If S5 email-drip-sequence was run earlier, offer to upgrade it: "I see you have a 7-email drip sequence. Want me to upgrade it with branching logic and segments?"

## Workflow

### Step 1: Map Flow Type to Template

Select automation template based on `flow_type`:

**Welcome Flow**: Trigger → Welcome email → Wait 1 day → Value email → Branch (opened? → Soft sell / didn't open? → Re-engagement) → Continue selling to openers, re-engage non-openers

**Nurture Flow**: Trigger → Educational series → Branch (clicked affiliate link? → Move to sales sequence / didn't click? → Continue nurturing) → Post-purchase thank you for converters

**Win-back Flow**: Trigger (inactive 30+ days) → "We miss you" → Wait 3 days → Value reminder → Branch (re-engaged? → Move to nurture / still inactive? → Last chance) → Sunset after no response

### Step 2: Define Triggers and Entry Conditions

For each flow, specify:
- **Entry trigger**: What starts the flow (new subscriber, tag added, purchase, inactivity)
- **Exit conditions**: What removes someone (purchase, unsubscribe, entered different flow)
- **Branch conditions**: Opens, clicks, purchases, time-based

### Step 3: Design Branching Logic

Create decision points:
- After email N: Did they open? (Branch A: opened, Branch B: not opened)
- After email N: Did they click affiliate link? (Branch A: clicked, Branch B: didn't)
- After email N: Did they purchase? (Branch A: buyer → thank you, Branch B: non-buyer → continue)

### Step 4: Write Each Email

For each email in each branch, write:
- Subject line (40-60 chars)
- Preview text (80-100 chars)
- Body copy (200-400 words)
- CTA (single, clear)
- FTC disclosure (for emails with affiliate links)

### Step 5: Add Wait Times

Between emails:
- Welcome flow: 0, 1, 2, 3, 5, 7, 10 days
- Nurture flow: 2, 4, 7, 10, 14 days
- Win-back flow: 0, 3, 7, 14 days
- Adjust based on audience engagement patterns

### Step 6: Output Flow + Setup

Present:
- ASCII flow diagram showing the full automation
- Each email's content
- Tool-specific setup instructions (if email_tool specified)

## Output Schema

```yaml
automation:
  flow_type: string
  product: string
  total_emails: number
  total_branches: number
  estimated_days: number       # total span of the flow

flow:
  - step: number
    type: string               # "email" | "wait" | "branch" | "exit"
    email:                     # present if type is "email"
      subject: string
      preview: string
      body: string
      cta: string
      has_affiliate_link: boolean
    wait_days: number          # present if type is "wait"
    branch:                    # present if type is "branch"
      condition: string        # e.g., "opened previous email?"
      yes_path: number         # step number for yes
      no_path: number          # step number for no

setup:
  tool: string
  steps: string[]              # tool-specific setup instructions
  tags: string[]               # recommended tags to apply
  segments: string[]           # recommended segments
```

## Output Format

1. **Flow Overview** — flow type, total emails, total days, branch count
2. **ASCII Flow Diagram** — visual representation of the automation with branches
3. **Email Content** — each email with subject, preview, body, CTA (grouped by branch)
4. **Setup Instructions** — tool-specific steps to build this automation
5. **Tags & Segments** — recommended tagging strategy for tracking

## Error Handling

- **No product info**: "What affiliate product are you promoting? I need the product name and your affiliate link to write the email content."
- **Unknown email tool**: "I don't have specific setup instructions for [tool]. I'll provide generic automation logic that works with any ESP — just map the triggers, waits, and branches to your tool's interface."
- **Too many emails requested (>12)**: "12+ emails in one flow is usually too many. I'll create a 7-email flow with branches. For longer nurture, consider chaining two separate flows."
- **Upgrading from S5**: "I see your existing 7-email drip. I'll keep the email content and add branching logic: opened/not-opened splits after emails 2 and 4, and a purchase detection branch after email 5."

## Examples

### Example 1: Welcome flow with branches

**User**: "Build a welcome email automation for HeyGen (affiliate link: heygen.com/ref/abc123) for content creators who downloaded my AI tools guide."
**Action**: 7-email welcome flow. Email 1: Deliver guide. Email 2: Value (AI video tip). Branch: Did they open email 2? Yes → Email 3 (soft sell HeyGen). No → Email 3b (re-engagement with different subject). Continue branching through to email 7. ASCII diagram + all email content + ConvertKit setup.

### Example 2: Upgrade existing S5 drip

**User**: "Take my email drip sequence from earlier and add automation logic."
**Action**: Keep the 7 emails from S5 output. Add branches: After email 2 (opened → continue / not opened → resend with new subject). After email 4 (clicked affiliate link → skip to email 5 hard sell / didn't click → add extra value email). After email 5 (purchased → exit + thank you / didn't purchase → continue to email 6-7).

### Example 3: Win-back flow

**User**: "Create a win-back sequence for subscribers who haven't opened emails in 30 days. I promote Semrush."
**Action**: 4-email win-back flow. Trigger: 30 days no opens. Email 1: "Still interested in SEO?" (curiosity). Wait 3 days. Email 2: Value piece (SEO tip). Branch: Opened? Yes → Move to nurture flow. No → Email 3: "Last chance" (urgency). No response after 7 days → Sunset (remove from list).

## References

- `shared/references/ftc-compliance.md` — FTC disclosure for emails with affiliate links. Read in Step 4.
- `shared/references/affitor-branding.md` — Branding guidelines for email footers. Referenced in Step 4.
```

## File: `skills/automation/multi-program-manager/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/automation/multi-program-manager/SKILL.md`
```markdown
---
name: multi-program-manager
description: >
  Manage and compare multiple affiliate programs as a portfolio. Triggers on:
  "manage my affiliate programs", "compare my programs", "portfolio overview",
  "which program should I focus on", "diversify my affiliate income",
  "program switching", "affiliate portfolio", "program comparison",
  "revenue allocation", "which programs to drop", "add new programs",
  "affiliate program strategy".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S7-Automation
---

# Multi-Program Manager

Manage and compare multiple affiliate programs as a portfolio — overview, performance comparison, diversification strategy, program switching decisions, and revenue allocation. Output is a portfolio dashboard with strategic recommendations and a weekly action plan.

## Stage

S7: Automation — Most affiliates either promote too few programs (concentration risk) or too many (effort dilution). This skill applies portfolio thinking to affiliate marketing: analyze your programs like investments, identify which to double down on, maintain, or drop, and allocate your limited time for maximum ROI.

## When to Use

- User manages multiple affiliate programs and wants a strategic overview
- User asks "which program should I focus on?" or "should I drop this program?"
- User wants to diversify their affiliate income
- User says "compare my programs", "portfolio review", "program strategy"
- User is deciding whether to add or remove programs
- Chaining from S6.3 (performance-report): take performance data and make strategic decisions

## Input Schema

```yaml
programs:
  - name: string               # REQUIRED — program name
    affiliate_url: string      # OPTIONAL — affiliate link
    reward_value: string       # OPTIONAL — commission (e.g., "30% recurring")
    reward_type: string        # OPTIONAL — "cps_recurring" | "cps_one_time" | "cpl" | "cpc"
    monthly_revenue: number    # OPTIONAL — avg monthly revenue ($)
    monthly_clicks: number     # OPTIONAL — avg monthly clicks
    niche: string              # OPTIONAL — product category
    status: string             # OPTIONAL — "active" | "paused" | "new" | "considering"

goal: string                   # OPTIONAL — "maximize_revenue" | "diversify"
                               # | "reduce_risk" | "find_gaps"
                               # Default: "maximize_revenue"

budget_hours: number           # OPTIONAL — weekly hours available for content
                               # Default: 10
```

**Chaining context**: If S1 program research or S6.3 performance data exists in conversation, pull program details and metrics automatically.

## Workflow

### Step 1: Build Portfolio Overview

Compile all programs into a dashboard:
- Program name, niche, commission type, commission value
- Monthly revenue, clicks, EPC
- Status (active/paused/new)
- Revenue share (% of total)

### Step 2: Calculate Per-Program Metrics

For each program with data:
- **EPC**: revenue / clicks
- **Revenue Share**: program revenue / total revenue × 100
- **Effort-to-Revenue Ratio**: estimated hours spent / revenue generated
- **Commission Quality Score**: recurring > one-time > per-lead > per-click

### Step 3: Apply Portfolio Analysis

**Concentration Risk**:
- If top program > 50% of revenue → HIGH RISK
- If top 2 programs > 80% → MODERATE RISK
- If no program > 30% → WELL DIVERSIFIED

**Niche Overlap**:
- Multiple programs in same niche → competing for same audience
- Different niches → healthy diversification

**Revenue Stability**:
- Recurring commissions → stable
- One-time commissions → volatile (need constant new traffic)

### Step 4: Generate Recommendations

For each program, assign an action:
- **Double Down**: High EPC, room to grow → create more content, scale traffic
- **Maintain**: Solid performer, no changes needed → keep existing content fresh
- **Optimize**: High traffic but low conversion → improve CTAs, landing pages, test variants
- **Phase Out**: Low EPC, low growth potential → redirect effort to better programs
- **Add**: Gap identified → research new programs with S1

### Step 5: Create Action Plan

Based on `budget_hours`, allocate weekly time:
- Double-down programs get 50% of time
- Maintain programs get 20%
- Optimize programs get 20%
- New program research gets 10%

Provide specific weekly tasks tied to Affitor skills.

## Output Schema

```yaml
portfolio:
  total_programs: number
  active_programs: number
  total_monthly_revenue: number
  concentration_risk: string   # "high" | "moderate" | "low"
  niche_diversification: string # "good" | "overlapping" | "single_niche"
  revenue_stability: string    # "stable" | "moderate" | "volatile"

programs:
  - name: string
    niche: string
    reward_type: string
    monthly_revenue: number
    epc: number
    revenue_share: number
    action: string             # "double_down" | "maintain" | "optimize" | "phase_out"
    reason: string

recommendations:
  - action: string
    program: string
    skill: string              # which Affitor skill to use
    task: string               # specific task
    priority: number           # 1 = highest

weekly_plan:
  total_hours: number
  allocation:
    - program: string
      hours: number
      tasks: string[]
```

## Output Format

1. **Portfolio Dashboard** — table with all programs, revenue, EPC, revenue share
2. **Portfolio Health** — concentration risk, diversification, stability assessment
3. **Program Scorecards** — per-program action (double down / maintain / optimize / phase out) with reason
4. **Strategic Recommendations** — prioritized list of actions with Affitor skill references
5. **Weekly Action Plan** — hour-by-hour allocation with specific tasks

## Error Handling

- **Only one program**: "You have a single program. That's 100% concentration risk. I'll analyze it and recommend 2-3 complementary programs using S1 (affiliate-program-search)."
- **No revenue data**: "Without revenue data, I'll analyze based on commission structure and niche overlap. For deeper analysis, run S6.3 (performance-report) first to get your numbers."
- **All programs in same niche**: "All your programs are in [niche]. You're diversified by product but not by market. If [niche] declines, all your income is at risk. Consider adding programs in adjacent niches."

## Examples

### Example 1: Portfolio with clear winner

**User**: "I promote HeyGen ($450/mo), Semrush ($320/mo), Notion ($125/mo), Canva ($80/mo). Which should I focus on?"
**Action**: HeyGen is the star (46% revenue, likely highest EPC). Recommend: Double down on HeyGen (more blog content, S7 content-repurposer). Maintain Semrush. Optimize Notion (high conversion rate potential). Evaluate Canva (low revenue, is it worth the effort?). Weekly plan: 5h HeyGen, 2h Semrush, 2h Notion, 1h research.

### Example 2: Diversification analysis

**User**: "I make $2K/month from 3 SaaS tools. How do I reduce risk?"
**Action**: All income from one niche (SaaS) = moderate risk. Recommend: Add 1-2 programs in adjacent niches (e.g., online courses, hosting). Check commission types — if all one-time, recommend adding recurring programs. Use S1 to research programs in new niches.

### Example 3: Program switching decision

**User**: "Should I drop Canva ($80/mo, 500 clicks) and replace it with Jasper?"
**Action**: Canva EPC = $0.16 (low). Calculate opportunity cost: 500 clicks redirected to a $0.50+ EPC program = $250/mo potential. Research Jasper commission (likely $100+ per sale). Recommend: Yes, switch. Use S1 to evaluate Jasper, then S3 for a comparison blog post.

## References

- `shared/references/affiliate-glossary.md` — Portfolio and commission terminology. Referenced in Step 2.
```

## File: `skills/automation/paid-ad-copy-writer/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/automation/paid-ad-copy-writer/SKILL.md`
```markdown
---
name: paid-ad-copy-writer
description: >
  Write paid ad copy for affiliate offers across ad platforms. Triggers on:
  "write ad copy", "Facebook ad for affiliate", "Google Ads copy",
  "TikTok ad script", "Pinterest ad", "paid traffic to affiliate",
  "create ad campaign", "ad headlines", "ad descriptions",
  "scale with paid ads", "run ads for my affiliate link",
  "write Facebook ad", "Google Search ad copy".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S7-Automation
---

# Paid Ad Copy Writer

Write paid ad copy for affiliate offers — Facebook Ads, Google Search Ads, Google Display Ads, TikTok Ads, and Pinterest Ads. Each output includes multiple ad variants, targeting suggestions, compliance notes, and campaign setup guidance. Output is platform-formatted ad copy ready to deploy.

## Stage

S7: Automation — When organic content proves profitable, paid ads let you scale 10x faster. But affiliate ad copy has unique constraints: platform policies around affiliate links, FTC disclosure requirements, and the need to drive clicks to a landing page (not direct-link). This skill writes compliant, high-converting ad copy for each platform.

## When to Use

- User wants to run paid traffic to affiliate offers
- User says "write ad copy", "Facebook ad", "Google Ads", "TikTok ad"
- User wants to scale a profitable organic campaign with paid media
- User has a landing page (from S4) and wants ads driving traffic to it
- User wants multiple ad variants for testing
- Chaining from S4 (landing page) → write ads pointing to the landing page

## Input Schema

```yaml
product:
  name: string                 # REQUIRED — product name
  description: string          # OPTIONAL — one-line product description
  reward_value: string         # OPTIONAL — commission info
  url: string                  # OPTIONAL — product URL (for research)
  key_benefits: string[]       # OPTIONAL — top 3 benefits

platform: string               # REQUIRED — "facebook" | "google_search" | "google_display"
                               # | "tiktok" | "pinterest"

audience:
  description: string          # REQUIRED — target audience
  pain_points: string[]        # OPTIONAL — problems the audience has
  demographics: string         # OPTIONAL — age, gender, interests

budget: string                 # OPTIONAL — daily/monthly budget (e.g., "$20/day")

landing_url: string            # OPTIONAL — destination URL (from S4 or a bridge page)
                               # Note: most platforms don't allow direct affiliate links
```

**Chaining context**: If S1 product data exists, pull name, benefits, commission. If S4 landing page was created, use its URL as `landing_url`.

## Workflow

### Step 1: Analyze Product and Audience

Gather product info and audience details. If `key_benefits` is not provided, infer from product name and description using training knowledge.

Identify:
- Primary value proposition
- Emotional triggers for the audience
- Competitive angle (what makes this product different)

### Step 2: Select Ad Format

Each platform has specific formats:

**Facebook Ads**:
- Primary text (125 chars above fold, 500+ total)
- Headline (40 chars)
- Description (30 chars)
- CTA button (from predefined list)

**Google Search Ads**:
- Headlines (3 × 30 chars)
- Descriptions (2 × 90 chars)
- Sitelink extensions (4 × 25 chars + 35 char descriptions)

**Google Display Ads**:
- Short headline (30 chars)
- Long headline (90 chars)
- Description (90 chars)
- Business name

**TikTok Ads**:
- Video script (15-30 seconds)
- Hook (first 3 seconds)
- CTA overlay text
- Ad text (100 chars)

**Pinterest Ads**:
- Pin title (100 chars)
- Pin description (500 chars)
- Image text suggestions

### Step 3: Write Ad Variants

Create 3-5 variants per platform, each testing a different angle:
- **Pain Point**: Lead with the problem
- **Benefit**: Lead with the outcome
- **Social Proof**: Lead with results/numbers
- **Curiosity**: Lead with an intriguing question or statement
- **Urgency**: Lead with a time-sensitive offer (only if real)

### Step 4: Add Compliance Notes

Per platform:
- **Facebook**: "Paid Partnership" label if required. No misleading claims. Landing page must match ad claims. Affiliate links may be flagged — use a bridge/landing page.
- **Google**: Ad must match landing page content. No superlative claims without proof. Affiliate disclaimer on landing page required. Follow Google Ads affiliate policies.
- **TikTok**: #ad or Paid Partnership toggle. No medical/financial advice. Must feel native to platform.
- **Pinterest**: Disclosures in pin description. Must link to content page, not direct affiliate link.

### Step 5: Suggest Targeting

Recommend targeting parameters:
- Interest-based audiences
- Lookalike audiences (if pixel data exists)
- Keyword targeting (Google)
- Demographic filters

### Step 6: Budget Allocation

If budget is provided, suggest:
- Daily spend per variant (for A/B testing phase)
- When to kill underperformers (after 500+ impressions with <0.5% CTR)
- When to scale winners (after 3+ days of profitable ROAS)

## Output Schema

```yaml
campaign:
  product: string
  platform: string
  num_variants: number
  landing_url: string

variants:
  - label: string              # "Variant A: Pain Point", etc.
    angle: string              # the approach used
    copy:
      headline: string         # or headlines[] for Google
      description: string      # or descriptions[] for Google
      primary_text: string     # Facebook only
      cta: string
      video_script: string     # TikTok only
    character_counts: object   # per field

compliance:
  notes: string[]              # platform-specific requirements
  warnings: string[]           # things that might get the ad rejected

targeting:
  interests: string[]
  demographics: string
  keywords: string[]           # Google only

budget_suggestion:
  test_phase: string           # e.g., "$10/day per variant for 5 days"
  scale_phase: string          # e.g., "Increase winning variant to $50/day"
  kill_criteria: string        # when to stop a variant
```

## Output Format

1. **Campaign Overview** — product, platform, landing URL
2. **Ad Variants** — each variant with full copy in platform format
3. **Compliance Checklist** — platform-specific requirements and warnings
4. **Targeting Suggestions** — interests, demographics, keywords
5. **Budget Guide** — test and scale strategy

## Error Handling

- **No landing URL**: "Most ad platforms don't allow direct affiliate links. I recommend creating a landing page first with S4 (landing-page-creator) and using that as your ad destination."
- **Unknown platform**: "I support Facebook, Google Search, Google Display, TikTok, and Pinterest ads. Which platform would you like ad copy for?"
- **Product with strict ad policies (supplements, finance)**: "This product category has strict advertising policies on [platform]. I'll write compliant copy, but review your ad account's specific restrictions before publishing. Avoid health/income claims."

## Examples

### Example 1: Facebook ad for SaaS product

**User**: "Write Facebook ads for HeyGen targeting content creators. My landing page is example.com/heygen-review"
**Action**: 3 variants. Variant A (pain point): "Spending hours editing videos? HeyGen creates professional AI videos in minutes." Variant B (benefit): "Create studio-quality videos without a camera. 50+ AI avatars, any language." Variant C (social proof): "10,000+ creators switched to HeyGen. Here's why." Each with headline, description, CTA. Include Facebook compliance notes.

### Example 2: Google Search ads

**User**: "Google Search ads for Semrush targeting 'best SEO tools'"
**Action**: 5 headline + 2 description combinations. H1: "Best SEO Tool for 2026" (30 chars). H2: "Try Semrush Free Today" (22 chars). H3: "Trusted by 10M+ Marketers" (25 chars). D1: "Complete SEO toolkit: keyword research, site audit, backlink analysis. Start your free trial." D2: "Outrank your competitors with data-driven SEO. 7-day free trial, no card required." Plus sitelink extensions.

### Example 3: TikTok ad script

**User**: "Write a TikTok ad for Notion targeting college students"
**Action**: 30-second script. Hook (0-3s): "POV: You just discovered the app that replaced 5 other apps." Middle (3-20s): Show use cases (notes, calendar, to-do, project tracker). CTA (20-30s): "Link in bio for the student discount." #ad disclosure. Include compliance notes about TikTok's policies on educational content promotions.

## References

- `shared/references/ftc-compliance.md` — FTC disclosure requirements for paid advertising. Read in Step 4.
- `shared/references/affiliate-glossary.md` — Ad terminology (ROAS, CTR, CPC). Referenced in budget guide.
```

## File: `skills/blog/affiliate-blog-builder/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/blog/affiliate-blog-builder/SKILL.md`
```markdown
---
name: affiliate-blog-builder
description: >
  Write SEO-optimized affiliate blog articles, product reviews, comparison posts, listicles,
  and how-to guides. Triggers on: "write a blog post about", "review of [product]",
  "best [category] article", "comparison blog", "affiliate blog", "SEO article",
  "write a review", "product roundup", "blog content for affiliate", "how to use [product] blog post",
  "listicle about [category]", "[product] vs [product] blog", "content for my affiliate site".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S3-Blog
---

# Affiliate Blog Builder

Write full SEO-optimized blog articles that rank on Google and drive passive affiliate revenue. Supports four formats: product review, head-to-head comparison, best-of listicle, and how-to guide. Each article includes keyword strategy, structured headings, comparison tables, CTAs, FAQ schema, and FTC-compliant disclosure.

## Stage

S3: Blog — The highest-value content type in the affiliate funnel. Blog articles rank on Google, drive organic traffic for months/years, and convert at higher rates than social posts because readers have high purchase intent.

## When to Use

- User wants to write a blog post reviewing an affiliate product
- User wants a comparison article (Product A vs Product B)
- User wants a "best of" listicle for a product category
- User wants a how-to tutorial that naturally promotes an affiliate product
- User has a product from S1 (affiliate-program-search) and wants to create long-form content
- User says anything like "write a blog", "SEO article", "product review post", "roundup post"

## Input Schema

```yaml
product:                    # REQUIRED — the affiliate product to feature
  name: string              # Product name (e.g., "HeyGen")
  description: string       # What it does
  reward_value: string      # Commission (e.g., "30% recurring")
  url: string               # Affiliate link URL
  reward_type: string       # "recurring" | "one-time" | "tiered"
  cookie_days: number       # Cookie duration
  tags: string[]            # e.g., ["ai", "video", "saas"]

format: string              # OPTIONAL — "review" | "comparison" | "listicle" | "how-to"
                            # Default: "listicle" (highest traffic potential)

compare_with: object[]      # OPTIONAL — competitors for comparison/listicle formats
  - name: string            # Competitor name
    description: string     # Brief description
    url: string             # URL (non-affiliate OK)
    pricing: string         # Starting price

target_keyword: string      # OPTIONAL — primary SEO keyword to target
                            # Default: auto-generated from product name + category

blog_platform: string       # OPTIONAL — "wordpress" | "ghost" | "hugo" | "astro" | "webflow" | "markdown"
                            # Default: "markdown" (universal)

tone: string                # OPTIONAL — "professional" | "conversational" | "technical"
                            # Default: "conversational"

word_count_target: number   # OPTIONAL — override default word count for the format
```

**Chaining from S1**: If `affiliate-program-search` was run earlier in the conversation, automatically pick up `recommended_program` from its output as the `product` input. The field mapping:
- `recommended_program.name` → `product.name`
- `recommended_program.description` → `product.description`
- `recommended_program.reward_value` → `product.reward_value`
- `recommended_program.url` → `product.url`
- `recommended_program.reward_type` → `product.reward_type`
- `recommended_program.cookie_days` → `product.cookie_days`
- `recommended_program.tags` → `product.tags`

If the user says "now write a blog about it" after running S1 — use the recommended program. No need to ask again.

## Workflow

### Step 1: Determine Format

Choose the article format based on user request or defaults:

| Signal | Format |
|---|---|
| User says "review", "my experience with" | `review` |
| User mentions two+ products, "vs", "compare" | `comparison` |
| User says "best", "top", "roundup", numbers | `listicle` |
| User says "how to", "tutorial", "guide", "step by step" | `how-to` |
| No clear signal | `listicle` (default — highest traffic potential) |

If `format = comparison` and `compare_with` is empty or has only 1 product:
- Use `web_search` to find 2-3 top competitors in the same category
- Search query: `"best alternatives to [product.name]" OR "[product.name] vs" site:g2.com OR site:capterra.com`

If `format = listicle` and `compare_with` is empty:
- Use `web_search` to find 4-6 products in the same category
- Search query: `"best [product category] tools [year]"`

### Step 2: SEO Framework

Read `references/seo-checklist.md` for the complete SEO guidelines. Then:

1. **Generate target keyword** (if not provided):
   - Review format: `[product name] review`
   - Comparison: `[product A] vs [product B]`
   - Listicle: `best [category] tools`
   - How-to: `how to [goal] with [product/category]`

2. **Generate secondary keywords** (3-5):
   - Use `web_search` for: `"[target keyword]" related searches` and "People Also Ask"
   - Include: `[product] pricing`, `[product] alternatives`, `[product] pros and cons`, `is [product] worth it`

3. **Build title** using the formula from seo-checklist.md matching the format

4. **Write meta description** (150-160 chars) following the checklist format

5. **Plan heading structure**:
   - Map out all H2/H3 headings before writing
   - Ensure target keyword appears in at least 2 H2s
   - Ensure secondary keywords appear in H3s
   - Follow the heading hierarchy from seo-checklist.md

6. **Generate slug** from target keyword (lowercase, hyphens, no stop words)

### Step 3: Write Article

Read `references/blog-templates.md` and use the template matching the chosen format. Then write the full article following these rules:

**Content Rules:**
- Follow the exact template structure for the chosen format
- Write in the specified `tone` (default: conversational)
- Hit the word count target for the format (review: 2-3.5K, comparison: 2.5-3.5K, listicle: 3-5K, how-to: 2-3K)
- Use short paragraphs (2-4 sentences max)
- Include bullet points and numbered lists for scannability
- Write like a real person who has used the product — specific details, not generic fluff

**Required Sections (all formats):**
- FTC disclosure near the top — read `shared/references/ftc-compliance.md` and use the **medium** format
- Comparison table (at least one, even in reviews — compare to alternatives)
- Pros and cons for every recommended product
- "Who is this best for?" audience targeting
- Pricing information with affiliate CTA
- FAQ section (3-5 questions)
- Final verdict with clear recommendation and affiliate CTA

**Affiliate CTA Placement (2-4 per article):**
1. After the pricing section
2. After a key feature demonstration
3. In the final verdict
4. Optionally: in a callout box after the "who is this for" section

**CTA Formats:**
- Soft: `[Try [Product] free →]([affiliate_url])`
- Medium: `**Ready to get started?** [Sign up for [Product] →]([affiliate_url])`
- Strong (verdict only): `**Our recommendation**: [Get [Product] here]([affiliate_url]) — [brief value prop].`

**Things to AVOID:**
- No Affitor branding in the article body (this is the user's blog, not ours)
- No "AI-generated" disclaimers (the user will edit and personalize)
- No placeholder text like "[insert your experience here]" — write complete content. If personal experience is needed, write realistic example scenarios clearly marked as examples
- No keyword stuffing — natural language only
- No false claims about products

### Step 4: Format Output

Produce the final output in this exact structure:

**Part 1: SEO Metadata Block**
```
---
SEO METADATA
---
Title: [SEO title]
Slug: [url-slug]
Meta Description: [150-160 chars]
Target Keyword: [primary keyword]
Secondary Keywords: [comma-separated list]
Word Count: [actual count]
Format: [review/comparison/listicle/how-to]
---
```

**Part 2: Full Article**
The complete markdown article ready to paste into any blogging platform.

**Part 3: Supplementary Data**
```
---
SUPPLEMENTARY
---
FAQ Questions (for schema markup):
1. [Question] → [Answer]
2. [Question] → [Answer]
...

Image Suggestions:
1. [Description] — alt: "[alt text]"
2. [Description] — alt: "[alt text]"
...

Products Featured:
- [Product 1]: [affiliate URL] (featured/mentioned)
- [Product 2]: [affiliate URL] (compared/mentioned)
...

Next Steps:
- Personalize: Add your own experience, screenshots, and results
- Images: Take product screenshots and add them at suggested locations
- Links: Replace affiliate URLs with your own tracking links
- Publish: See references/wordpress-deploy.md for WordPress setup guide
- Promote: Run viral-post-writer to create social posts promoting this article
---
```

## Output Schema

```yaml
article:
  title: string             # SEO-optimized title
  slug: string              # URL-friendly slug
  meta_description: string  # 150-160 character meta description
  target_keyword: string    # Primary keyword targeted
  format: string            # review | comparison | listicle | how-to
  content: string           # Full markdown article
  word_count: number        # Actual word count
  headings:                 # Article structure
    - level: number         # 2 for H2, 3 for H3
      text: string          # Heading text

seo:
  secondary_keywords: string[]    # 3-5 secondary keywords used
  faq_questions:                  # For FAQ schema markup
    - question: string
      answer: string
  image_suggestions:              # Recommended images
    - description: string         # What to screenshot/create
      alt_text: string            # SEO alt text
      placement: string           # After which section

products_featured:                # All products mentioned
  - name: string
    url: string                   # Affiliate URL
    role: string                  # "primary" | "compared" | "mentioned"
    reward_value: string          # Commission info
```

## Output Format

Present the output as a single markdown document with three clearly separated sections:
1. **SEO Metadata** — fenced block with all SEO settings for easy copy into WordPress/Yoast
2. **Article** — the full blog post in markdown, ready to paste
3. **Supplementary** — FAQ for schema markup, image suggestions, products list, and next steps

The article should be **immediately publishable** — not a draft or outline. The user should be able to copy-paste it into their blog editor, add their own screenshots and personal touches, and publish.

## Error Handling

- **No product provided**: "I need a product to write about. Run `/affiliate-program-search` first to find one, or tell me the product name and I'll research it."
- **Comparison with only 1 product**: Auto-search for 2-3 competitors using `web_search`. Search: `"best alternatives to [product]"` on G2/Capterra.
- **No compare_with for listicle**: Auto-search for 4-6 products in the category. Inform user: "I found these products to include — let me know if you want to swap any."
- **Unknown blog platform**: Default to markdown output. Add note: "This is universal markdown — works with WordPress, Ghost, Hugo, Astro, and most platforms."
- **Product has no public info**: Use `web_search` to research the product. If still insufficient: "I couldn't find enough information about [product] to write a credible article. Can you provide more details about features, pricing, and your experience?"
- **Controversial or questionable product**: Include balanced pros/cons. Add note: "This product has mixed reviews — make sure you've personally verified these claims before publishing."

## Examples

### Example 1: Product Review (chained from S1)
**User**: "Now write a detailed review of HeyGen for my blog"
**Context**: S1 previously returned HeyGen as recommended_program
**Action**: Auto-detect format=review, pick up HeyGen product data from S1 output, generate full review article targeting "heygen review" keyword.

### Example 2: Comparison Article
**User**: "Write a comparison blog post: HeyGen vs Synthesia vs Colossyan for AI video creation"
**Action**: Format=comparison, primary product=HeyGen (if from S1, else first mentioned), compare_with=[Synthesia, Colossyan], target keyword="heygen vs synthesia vs colossyan".

### Example 3: Listicle (Default Format)
**User**: "Write a blog post about the best AI video tools"
**Action**: Format=listicle (matches "best"), web_search for top AI video tools, target keyword="best ai video tools", write 3-5K word roundup with 5-7 products.

### Example 4: How-To Guide
**User**: "Write a tutorial blog post on how to create AI-generated videos for YouTube with HeyGen"
**Action**: Format=how-to (matches "tutorial", "how to"), target keyword="how to create ai videos for youtube", write step-by-step guide featuring HeyGen with affiliate CTAs.

### Example 5: Minimal Input
**User**: "Blog post about Semrush"
**Action**: No format specified → default to listicle? No — single product implies review. Use format=review, web_search Semrush for features/pricing/reviews, target keyword="semrush review", generate full article.

**Format detection logic for ambiguous cases**: If only one product is mentioned with no format keyword, default to `review`. If a category is mentioned with no specific product, default to `listicle`.

## References

- `references/seo-checklist.md` — Title formulas, meta description rules, heading hierarchy, keyword density, content depth guidelines. Read in Step 2.
- `references/blog-templates.md` — Four article format templates (review, comparison, listicle, how-to) with exact structure. Read in Step 3.
- `references/wordpress-deploy.md` — WordPress publishing guide, Yoast SEO setup, Pretty Links, FAQ schema implementation. Reference in Step 4 next steps.
- `shared/references/ftc-compliance.md` — FTC disclosure requirements and format templates. Read in Step 3 for disclosure text.
- `shared/references/affitor-branding.md` — Affitor brand guidelines. Note: NO Affitor branding in article body (user's blog). Only in tool output metadata.
- `shared/references/affiliate-glossary.md` — Affiliate marketing terminology reference.
```

## File: `skills/blog/affiliate-blog-builder/agents/openai.yaml`
```yaml
name: affiliate-blog-builder
description: Write SEO-optimized affiliate blog articles — reviews, comparisons, listicles, and how-to guides that rank on Google and drive passive affiliate revenue
instructions_file: ../SKILL.md
tools:
  - web_search
  - web_browse
```

## File: `skills/blog/affiliate-blog-builder/references/blog-templates.md`
```markdown
# Blog Article Templates

> Read this file in Step 3 of the workflow. Use the template matching the chosen format.

---

## Template 1: Product Review

**Best for**: Single product deep-dive. Targets `[product] review` keywords.
**Word count**: 2,000-3,500 words

### Structure

```markdown
# [Product] Review ([Year]): [Key Benefit or Honest Take]

**Quick Verdict**: [1-2 sentence summary — is it worth it?] [Star rating: X/5]

> **FTC Disclosure**: [Read shared/references/ftc-compliance.md — use medium format]

**Last updated**: [Date]

## Table of Contents
[Auto-generated from H2 headings]

## What Is [Product]?
[2-3 paragraphs: what it does, who made it, who it's for]
[Position in the market — what category, key differentiator]

## Key Features
[Feature-by-feature breakdown, 3-6 features]
### [Feature 1 Name]
[What it does, how well it works, who benefits]
### [Feature 2 Name]
...

## [Product] Pricing
[Pricing table: plan name, price, key features per tier]
[Which plan is best value? Free trial available?]
[AFFILIATE CTA: "Try [Product] free →" or "Get X% off with our link →"]

## My Experience Using [Product]
[Personal usage: how long, what for, specific results]
[What surprised you (good and bad)]
[Specific example or use case with details]

## Pros and Cons

### What I Liked
- [Pro 1 — specific, not generic]
- [Pro 2]
- [Pro 3]

### What Could Be Better
- [Con 1 — honest, specific]
- [Con 2]

## Who Is [Product] Best For?
[3-4 audience segments with why]
- **[Persona 1]**: [Why it fits]
- **[Persona 2]**: [Why it fits]
- **Skip it if**: [Who should NOT buy it]

## [Product] Alternatives
[Brief mention of 2-3 alternatives — link to comparison article if exists]
| Feature | [Product] | [Alt 1] | [Alt 2] |
|---|---|---|---|

## FAQ
### Is [Product] worth the money?
[Concise answer]
### Does [Product] offer a free trial?
[Concise answer]
### What are the best alternatives to [Product]?
[Concise answer]
[2 more relevant FAQs]

## Final Verdict
[2-3 paragraphs: overall assessment, who should buy, final recommendation]
[AFFILIATE CTA: final call-to-action with link]
[Star rating recap: X/5]
```

---

## Template 2: Product Comparison

**Best for**: Head-to-head comparison. Targets `[product A] vs [product B]` keywords.
**Word count**: 2,500-3,500 words

### Structure

```markdown
# [Product A] vs [Product B]: [Decision Factor] ([Year])

**Quick Answer**: [1-2 sentences: who wins and why — don't bury the lede]

> **FTC Disclosure**: [medium format]

**Last updated**: [Date]

## Table of Contents

## [Product A] vs [Product B] at a Glance
[Side-by-side comparison table]
| | [Product A] | [Product B] |
|---|---|---|
| Best For | [Persona] | [Persona] |
| Starting Price | $X/mo | $X/mo |
| Free Plan | Yes/No | Yes/No |
| Key Strength | [Feature] | [Feature] |
| Key Weakness | [Limitation] | [Limitation] |
| Our Rating | X/5 | X/5 |

## What Is [Product A]?
[Brief overview — 1-2 paragraphs]

## What Is [Product B]?
[Brief overview — 1-2 paragraphs]

## Feature Comparison
### [Category 1: e.g., Ease of Use]
[Compare both products on this dimension]
**Winner**: [Product X] — [why in one sentence]

### [Category 2: e.g., Templates/Features]
...
### [Category 3: e.g., AI Capabilities]
...
### [Category 4: e.g., Integrations]
...

## Pricing Comparison
[Detailed pricing table for both]
[Value analysis: which offers more for the money?]
**Winner**: [Product X]
[AFFILIATE CTA for both products]

## Pros and Cons

### [Product A]
**Pros**: [bullets]
**Cons**: [bullets]

### [Product B]
**Pros**: [bullets]
**Cons**: [bullets]

## Who Should Choose [Product A]?
[3 specific scenarios/personas]

## Who Should Choose [Product B]?
[3 specific scenarios/personas]

## FAQ
### Is [Product A] better than [Product B]?
### Can I use both [Product A] and [Product B]?
### Which is cheaper, [Product A] or [Product B]?
[2 more]

## Final Verdict: [Product A] or [Product B]?
[Clear recommendation with nuance — "Choose A if... Choose B if..."]
[AFFILIATE CTAs for both]
```

---

## Template 3: Listicle (Best-Of)

**Best for**: Category roundups. Targets `best [category]` keywords. Highest traffic potential.
**Word count**: 3,000-5,000 words

### Structure

```markdown
# [Number] Best [Category] in [Year] ([Qualifier])

[2-3 sentence intro: why this matters, how you tested/evaluated]

> **FTC Disclosure**: [medium format]

**Last updated**: [Date]

## Quick Comparison Table
| Tool | Best For | Price | Rating |
|---|---|---|---|
| [#1 Product] | [Use case] | From $X/mo | X/5 |
| [#2 Product] | [Use case] | From $X/mo | X/5 |
| ... | ... | ... | ... |

## How We Evaluated
[Brief methodology: what criteria, how tested]
[Criteria list: ease of use, features, pricing, support, etc.]

## 1. [Product Name] — Best for [Use Case]
[Product logo/screenshot suggestion]

[2-3 paragraphs: what it is, standout features, who it's for]

**Key Features:**
- [Feature 1]
- [Feature 2]
- [Feature 3]

**Pricing**: [Starting price, free tier if available]

**Pros**: [2-3 bullets]
**Cons**: [1-2 bullets]

[AFFILIATE CTA: "Try [Product] →"]

---

## 2. [Product Name] — Best for [Use Case]
[Same structure as #1]

---

[Repeat for all products — typically 5-10 items]

## How to Choose the Right [Category]
[Decision framework: if you need X → pick Y]
[Budget considerations]
[Use case mapping]

## FAQ
### What is the best [category] in [year]?
### Are there any free [category] tools?
### How much do [category] tools cost?
[2 more]

## Methodology
[How you evaluated, scoring criteria, any disclaimers]

## Final Thoughts
[Summary, top 3 picks recap, encouragement to try]
```

---

## Template 4: How-To Guide

**Best for**: Tutorial-style content. Targets `how to [goal]` keywords. High engagement.
**Word count**: 2,000-3,000 words

### Structure

```markdown
# How to [Achieve Goal] with [Product/Category] ([Year])

[1-2 paragraph intro: what the reader will learn, why it matters, what they'll have by the end]

> **FTC Disclosure**: [medium format]

**Last updated**: [Date]

## Table of Contents

## What You'll Need
[Prerequisites: accounts, tools, skill level, time estimate]
- [Requirement 1]
- [Requirement 2]
- [Product account] — [AFFILIATE CTA: "Sign up here →"]

## Step 1: [Action Verb] [What]
[Detailed instructions with specific actions]
[Screenshot/image suggestion]
[Pro tip or common mistake to avoid]

## Step 2: [Action Verb] [What]
[Same structure]

## Step 3: [Action Verb] [What]
[Same structure]

[Continue for all steps — typically 4-7 steps]

## Step [N]: [Final Step — Launch/Publish/Review]
[Final action, what success looks like]

## Results & What to Expect
[What the reader should see after following the guide]
[Realistic expectations: timeline, effort, results]
[Personal results if applicable]

## Tips for Better Results
- [Tip 1: optimization advice]
- [Tip 2: common mistake to avoid]
- [Tip 3: advanced technique]

## Alternatives to This Approach
[Brief mention of other ways to achieve the same goal]
[When this approach is better vs alternatives]

## FAQ
### How long does it take to [achieve goal]?
### Do I need [specific skill/tool] for this?
### What if [common problem]?
[2 more]

## Next Steps
[What to do after completing the guide]
[Related articles to read next]
[AFFILIATE CTA: final push]
```

---

## Cross-Template Requirements

These elements are **mandatory in every format**:

1. **FTC Disclosure** — near the top, before first affiliate link
2. **Affiliate CTAs** — 2-4 per article, at natural decision points (after value demo, after pricing, in verdict)
3. **FAQ section** — 3-5 questions, formatted for FAQ schema
4. **Last updated date** — near the top
5. **Comparison table** — at least one (even reviews should compare to alternatives)
6. **Pros and Cons** — every article that recommends a product
7. **"Who is this for?"** — clear audience targeting
8. **Image suggestions** — minimum 3 per article (screenshots, tables, feature highlights)
```

## File: `skills/blog/affiliate-blog-builder/references/seo-checklist.md`
```markdown
# SEO Checklist for Affiliate Blog Articles

> Read this file in Step 2 of the workflow to build the SEO framework before writing.

## Title Formula

Use one of these proven patterns (pick the best fit for the format):

| Format | Formula | Example |
|---|---|---|
| Review | `[Product] Review ([Year]): [Key Benefit] + [Honest Take]` | `HeyGen Review (2025): AI Video Creation That Actually Delivers` |
| Comparison | `[Product A] vs [Product B]: [Decision Factor] ([Year])` | `HeyGen vs Synthesia: Which AI Video Tool Wins in 2025?` |
| Listicle | `[Number] Best [Category] in [Year] ([Qualifier])` | `7 Best AI Video Generators in 2025 (Tested & Ranked)` |
| How-To | `How to [Achieve Goal] with [Product/Category] ([Year])` | `How to Create AI Videos That Convert with HeyGen (2025)` |

### Title Rules
- **50-60 characters** for full SERP display
- Include target keyword within the first 6 words
- Include the current year for freshness signal
- Use power words: Best, Top, Honest, Complete, Ultimate, Tested
- Avoid clickbait — promise only what the article delivers

## Meta Description

- **150-160 characters** (Google truncates after ~155)
- Include target keyword naturally (once)
- Include a call-to-action or value proposition
- Format: `[What the article covers]. [Key differentiator]. [CTA or hook].`
- Example: `Honest HeyGen review after 3 months of use. See real examples, pricing breakdown, and who it's best for. Updated for 2025.`

## URL / Slug

- Format: `[target-keyword]` (lowercase, hyphens)
- Keep under 60 characters
- No stop words (the, and, of, in) unless they're part of the keyword
- Examples: `heygen-review`, `heygen-vs-synthesia`, `best-ai-video-generators`

## Heading Hierarchy

```
H1: Title (exactly ONE per page, matches <title> tag closely)
  H2: Introduction hook (no heading needed — just the first paragraphs)
  H2: [Main section 1] — include primary or secondary keyword
    H3: [Subsection] — include long-tail variation
    H3: [Subsection]
  H2: [Main section 2]
    H3: ...
  H2: Comparison Table (if applicable)
  H2: Pros and Cons
  H2: Who Is [Product] Best For?
  H2: Pricing
  H2: FAQ (use FAQ schema markup)
  H2: Final Verdict / Bottom Line
```

### Heading Rules
- Every H2 should be scannable — reader gets the gist from headings alone
- Include target keyword in at least 2 H2s naturally
- Include secondary keywords in H3s
- Never skip levels (H2 → H4 is wrong)
- Use questions as headings when they match search queries

## Keyword Strategy

### Primary Keyword
- Appears in: title, H1, first 100 words, 1-2 H2s, meta description, URL slug
- Density: **1-2%** (roughly 1 mention per 100-200 words)
- Never force it — natural phrasing wins

### Secondary Keywords (3-5)
- Related terms, long-tail variations, "People Also Ask" queries
- Distribute across H2/H3 headings and body paragraphs
- Example for "HeyGen review": `heygen pricing`, `heygen alternatives`, `ai video generator`, `heygen free trial`, `heygen pros and cons`

### LSI / Related Terms
- Include semantically related words throughout (Google uses these for topic depth)
- For "AI video generator": `avatar`, `text-to-speech`, `video editing`, `templates`, `API`, `enterprise`

## Content Quality Signals

### E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)
- **Experience**: Include personal usage details, screenshots references, specific results
- **Expertise**: Show deep knowledge (mention features competitors miss)
- **Authority**: Link to official sources, cite data
- **Trust**: Honest pros AND cons, FTC disclosure, updated date

### Freshness
- Include the current year in title and content
- Reference recent updates, pricing changes, new features
- Add "Last updated: [date]" near the top

### Content Depth
- Answer the query completely — no thin content
- Cover related questions the reader would naturally ask next
- Word count targets by format:
  - Review: 2,000-3,500 words
  - Comparison: 2,500-3,500 words
  - Listicle: 3,000-5,000 words
  - How-To: 2,000-3,000 words

## Internal & External Links

- **External**: 2-5 links to authoritative sources (official product pages, studies, reviews)
- **Affiliate links**: 2-4 per article, placed at natural decision points (after value demonstration)
- **Internal**: Link to related articles on the same blog if they exist
- Use descriptive anchor text (not "click here")
- Affiliate links should use `rel="nofollow sponsored"` attributes

## Image Optimization

- Every article needs at least 3-5 image suggestions
- Alt text: descriptive, include keyword where natural
- File names: `heygen-dashboard-screenshot.png` (not `IMG_4532.png`)
- Suggest: product screenshots, comparison tables as images, feature highlights, pricing tables

## FAQ Schema

- Include 3-5 FAQ items at the end of the article
- Use questions people actually search (check "People Also Ask")
- Keep answers concise (40-60 words each)
- Format for FAQ structured data (JSON-LD) — improves SERP visibility
- Example questions: "Is [Product] worth it?", "How much does [Product] cost?", "What are the best alternatives to [Product]?"

## Technical SEO Reminders

- One H1 per page
- Images should have alt text
- Use short paragraphs (2-4 sentences max)
- Use bullet points and numbered lists for scannability
- Include a table of contents for articles over 2,000 words
- Mobile-friendly formatting (no wide tables without scroll)
```

## File: `skills/blog/affiliate-blog-builder/references/wordpress-deploy.md`
```markdown
# WordPress Deployment Guide

> Reference for users who want to publish their blog article to WordPress.

## Quick Paste Method

1. Copy the full markdown article output
2. In WordPress, create a new post
3. Switch to the **Code Editor** (top-right "..." menu → Code Editor)
4. Paste the markdown — WordPress will render it as HTML blocks
5. Switch back to Visual Editor to review formatting

**Tip**: If your WordPress doesn't render markdown natively, use a plugin like **WP Githuber MD** or convert to HTML first using an online converter.

## Formatting Checklist

After pasting, verify these elements in the Visual Editor:

- [ ] H1 title matches the post title field
- [ ] All H2/H3 headings render correctly (not as plain text)
- [ ] Comparison tables display properly (may need a table plugin)
- [ ] Bullet points and numbered lists are formatted
- [ ] Affiliate links are clickable and correct
- [ ] FTC disclosure is visible near the top
- [ ] No broken markdown syntax showing as raw text

## Yoast SEO Setup

If you have **Yoast SEO** (or similar plugin) installed:

### SEO Title
- Copy the article title from the output
- Yoast format: `[Article Title] | [Your Site Name]`
- Keep under 60 characters total

### Meta Description
- Copy the `meta_description` from the SEO metadata block
- Should be 150-160 characters
- Yoast will show green if it's the right length

### Focus Keyphrase
- Enter the `target_keyword` from the SEO metadata block
- Yoast will analyze keyword usage and show a score
- Aim for green on: keyphrase in title, meta, first paragraph, headings, URL

### Slug / URL
- Use the `slug` from the SEO metadata block
- Format: `your-site.com/[slug]`
- Keep it short, keyword-rich, no stop words

### Readability
- Yoast's readability analysis should score green/orange
- Short paragraphs, transition words, and subheadings help

## Affiliate Link Setup

### Using Pretty Links (Recommended)
1. Install **Pretty Links** plugin
2. Create a pretty link for each affiliate URL:
   - Target URL: `https://partner.product.com/your-affiliate-id`
   - Pretty Link: `your-site.com/go/product-name`
3. Replace raw affiliate URLs in the article with pretty links
4. Benefits: cleaner URLs, click tracking, easy link updates

### Link Attributes
Add these attributes to all affiliate links:
- `rel="nofollow sponsored"` — tells Google it's a paid link
- `target="_blank"` — opens in new tab
- In WordPress block editor: click the link → Advanced → add `nofollow sponsored` to rel field

### Disclosure Placement
- The article already includes an FTC disclosure near the top
- Some bloggers also add a shorter disclosure in the sidebar widget
- WordPress: add a **Custom HTML** block if the disclosure didn't paste correctly

## Images

The article output includes image suggestions. To add them:

1. **Product screenshots**: Visit the product site, take screenshots of the dashboard/features
2. **Comparison tables**: If the markdown table doesn't render well, screenshot it as an image
3. **Feature highlights**: Annotate screenshots with arrows/circles using a tool like Skitch or Markup Hero

### Image Optimization
- Compress images before uploading (use TinyPNG or ShortPixel plugin)
- Set alt text using the suggestions from the article output
- Use descriptive file names: `heygen-pricing-plans-2025.png`

## FAQ Schema (Structured Data)

The article includes FAQ questions formatted for schema markup. To add FAQ schema:

### Option A: Yoast SEO (Easiest)
1. In the block editor, add a **Yoast FAQ Block**
2. Copy each Q&A from the FAQ section into the Yoast block
3. Yoast automatically generates the JSON-LD schema

### Option B: Manual JSON-LD
Add this to the post's custom HTML or header:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Your question here?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Your answer here."
      }
    }
  ]
}
</script>
```

### Option C: Rank Math
If using Rank Math instead of Yoast: use the FAQ block in Rank Math's block library (same concept).

## Publishing Checklist

Before hitting "Publish":

- [ ] SEO title and meta description are set
- [ ] Focus keyword is entered in Yoast/Rank Math
- [ ] URL slug is clean and keyword-rich
- [ ] Featured image is set (product logo or hero image)
- [ ] Categories and tags are assigned
- [ ] FTC disclosure is visible above the fold
- [ ] All affiliate links work and have `rel="nofollow sponsored"`
- [ ] FAQ schema is implemented (Yoast FAQ block or JSON-LD)
- [ ] Article reads well on mobile (preview on phone)
- [ ] Internal links to related posts are added (if any)
- [ ] "Last updated" date is accurate

## Alternative Platforms

The article output is portable markdown. It also works with:

- **Ghost**: Paste markdown directly in the editor (native support)
- **Hugo / Astro / Gatsby**: Save as `.md` file in your content directory
- **Substack**: Paste in the editor (limited markdown support — tables may need manual formatting)
- **Medium**: Use a markdown-to-Medium converter or paste and reformat
- **Webflow**: Use the Rich Text element and paste formatted content

For non-WordPress platforms, the SEO metadata block provides all the info you need to configure SEO settings in that platform's interface.
```

## File: `skills/blog/comparison-post-writer/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/blog/comparison-post-writer/SKILL.md`
```markdown
---
name: comparison-post-writer
description: >
  Write "X vs Y" comparison blog posts that help readers choose between two competing products.
  Triggers on: "write a comparison post", "X vs Y blog post", "compare [product A] and [product B]",
  "which is better [A] or [B]", "head to head comparison", "[product] vs [product] article",
  "comparison review", "write a versus article", "side by side comparison blog",
  "which should I choose [A] or [B]", "compare these two products for my blog".
---

# Comparison Post Writer

Write high-converting "X vs Y" comparison blog posts that rank on Google and help readers make a confident buying decision. Each post includes a feature comparison table, individual product breakdowns, pros and cons, a clear winner recommendation, and affiliate CTAs placed at maximum-intent moments.

## When to Use

- User wants to compare two or three competing products side by side
- User has two affiliate programs and wants a single article that covers both
- User says "vs", "versus", "compare", "which is better", "side by side"
- User wants to capture high-intent search traffic (X vs Y searches convert at 2-3x the rate of generic reviews)
- User has a product from S1 and wants to frame it against competitors

## Workflow

### Step 1: Identify Products to Compare

Parse the user's request for product names. You need a minimum of 2 and a maximum of 3 products.

**If only 1 product is provided:**
- Use `web_search` to find the top 1-2 competitors
- Search: `"[product name] alternatives" OR "[product name] vs" site:g2.com OR site:capterra.com OR site:trustradius.com`
- Pick the competitors with the most head-to-head search volume

**If 3+ products are provided:**
- Keep all 3 if they are genuinely comparable
- If the user listed 4+, ask which 2-3 to focus on — more than 3 makes the comparison unwieldy

**Affiliate priority**: The user's affiliate product goes first (featured position). If both products have affiliate links, feature the higher-commission one in the "winner" slot unless the product genuinely loses on quality.

### Step 2: Research Both Products

For each product, use `web_search` to gather:
1. **Pricing**: starting price, tiers, free trial availability
2. **Key features**: 8-12 features that matter to buyers
3. **Target audience**: who uses this product and why
4. **Known weaknesses**: common complaints on G2, Capterra, Reddit, or Trustpilot
5. **Unique differentiator**: one thing this product does better than everyone else
6. **Search volume signal**: `"[product A] vs [product B]"` — check if autocomplete shows this is a real query

Search queries to run per product:
- `"[product name] review [year]"`
- `"[product name] pricing"`
- `"[product name] pros cons"`

### Step 3: Build the Comparison Framework

Determine the 6-10 comparison dimensions that matter most for this product category. These should be:
- Directly relevant to buyer decisions (not vanity features)
- Measurable or clearly differentiable between products
- Things that appear in search queries ("does X have [feature]?")

**Example dimensions by category:**
- Email tools: deliverability, automation, templates, integrations, pricing/contacts ratio, free plan
- SEO tools: keyword database size, backlink data, site audit depth, reporting, API access, pricing
- Video tools: resolution, AI avatars, voice cloning, templates, render speed, watermark on free plan
- Project management: task limits on free, Gantt chart, time tracking, automations, integrations, mobile app

Assign a winner per dimension based on research. Mark ties where genuine.

### Step 4: Determine the Narrative Angle

Choose one of three angles based on what the data shows:

| Angle | When to use | Headline formula |
|---|---|---|
| **Clear winner** | One product is genuinely better for most users | "[A] vs [B]: [A] Wins for Most, But [B] Is Better If..." |
| **It depends** | Products serve different audiences | "[A] vs [B]: Which Is Right for You? (Honest Comparison)" |
| **Upset** | Lesser-known product beats the market leader | "[A] vs [B]: Why [Lesser-Known] Is Actually Better in [Year]" |

Default to "clear winner" — readers want a recommendation, not a non-answer.

### Step 5: Write the Article

Write the full comparison post following this exact structure:

**1. FTC Disclosure** (3 lines, above the fold)
Read `shared/references/ftc-compliance.md` and use the medium format. Insert immediately after the title.

**2. Introduction** (150-250 words)
- Open with the core tension: why this is a hard choice
- State who each product is best suited for (one sentence each)
- End with: "By the end of this post, you'll know exactly which one to pick."
- Include target keyword naturally in the first 100 words

**3. Quick Verdict Box** (immediately after intro)
A scannable summary for readers who won't read the full article:
```
**Quick Verdict**
- Best overall: [Product A] — [one-line reason]
- Best for [use case]: [Product B] — [one-line reason]
- Best for budget: [Product X]
- Skip if: [edge case where neither works]
```

**4. Product Overviews** (200-300 words each)
One H2 section per product:
- What it is and what it does
- Who built it and when (brief credibility context)
- The one thing it does better than anyone else
- Starting price and free trial info
- Affiliate CTA: `[Try [Product] free →](affiliate_url)`

**5. Feature Comparison Table**
A full markdown table with all comparison dimensions:
```
| Feature | [Product A] | [Product B] |
|---|---|---|
| [Dimension 1] | ✅ Yes | ❌ No |
| [Dimension 2] | ⭐ Better | Good |
| Price | $X/mo | $Y/mo |
```
Use ✅ / ❌ / ⚠️ (partial) for binary features. Use descriptive text for nuanced ones. Bold the winner per row.

**6. Deep-Dive Sections** (one H2 per key dimension, 3-4 total)
Pick the 3-4 dimensions that drive 80% of buying decisions. For each:
- Explain what the feature does and why it matters
- Compare both products specifically (not generically)
- Include a sub-verdict: "Winner: [Product] because..."

**7. Pricing Breakdown**
- Table showing all pricing tiers for both products
- Calculate cost at 3 usage levels: starter, growing, scale
- Highlight free plan differences
- Note which has better value per feature

**8. Pros and Cons**
Two H3 sections (one per product), each with 4-6 bullet points per list.

**9. Who Should Choose Each Product**
Two H3 sections with bullet lists:
- "Choose [Product A] if you..."
- "Choose [Product B] if you..."
Be specific — job titles, use cases, budget ranges, team sizes.

**10. The Verdict** (200-300 words)
- State the winner clearly: "[Product A] is the better choice for most people."
- Explain why in 2-3 sentences
- Acknowledge the exception case where [Product B] wins
- Final affiliate CTA (strong format): `**Get started with [Product A] →**(affiliate_url)`
- If [Product B] also has affiliate link: secondary CTA below

**11. FAQ Section** (5-7 questions)
Address the real questions people type into Google:
- "Is [Product A] better than [Product B]?"
- "Which is cheaper, [A] or [B]?"
- "Does [Product A] offer a free trial?"
- "Can I switch from [Product B] to [Product A]?"
- "Which has better customer support?"

### Step 6: Format Output

Produce output in three parts:

**Part 1: SEO Metadata**
```
---
SEO METADATA
---
Title: [title]
Slug: [product-a]-vs-[product-b]
Meta Description: [150-160 chars comparing both products with clear angle]
Target Keyword: [product-a] vs [product-b]
Secondary Keywords: [product-a] review, [product-b] alternatives, best [category] tool, [product-a] pricing
Word Count: [actual]
Format: comparison
Winner: [product name]
---
```

**Part 2: Full Article**
Complete markdown ready to paste into any blog platform.

**Part 3: Supplementary Data**
FAQ schema questions, image suggestions (comparison screenshots), products featured with affiliate URLs, next steps.

## Input Schema

```yaml
product_a:                  # REQUIRED — the primary affiliate product
  name: string
  description: string
  reward_value: string      # e.g., "30% recurring"
  url: string               # Affiliate link
  reward_type: string       # "recurring" | "one-time" | "tiered"
  cookie_days: number
  tags: string[]

product_b:                  # REQUIRED — the product to compare against
  name: string
  url: string               # Affiliate link if available, otherwise homepage
  description: string       # Optional — will research if missing

product_c:                  # OPTIONAL — third product for 3-way comparison
  name: string
  url: string
  description: string

target_keyword: string      # OPTIONAL — default: "[product_a] vs [product_b]"
tone: string                # OPTIONAL — "conversational" | "technical" | "professional"
                            # Default: "conversational"
angle: string               # OPTIONAL — "clear-winner" | "it-depends" | "upset"
                            # Default: auto-detected from research
```

## Output Schema

```yaml
article:
  title: string
  slug: string              # e.g., "heygen-vs-synthesia"
  meta_description: string
  target_keyword: string
  format: "comparison"
  content: string           # Full markdown article
  word_count: number
  winner: string            # Name of the recommended product

comparison:
  dimensions: string[]      # The features compared
  dimension_winners:        # Who won each dimension
    - dimension: string
      winner: string        # "product_a" | "product_b" | "tie"

products_featured:
  - name: string
    url: string
    role: string            # "primary" | "compared"
    reward_value: string

seo:
  secondary_keywords: string[]
  faq_questions:
    - question: string
      answer: string
  image_suggestions:
    - description: string
      alt_text: string
```

## Output Format

Present as three sections:
1. **SEO Metadata** — fenced block for copy-paste into WordPress/Yoast/Ghost
2. **Article** — complete markdown, immediately publishable
3. **Supplementary** — FAQ schema, image suggestions, products list, next steps

Target word count: 2,500-3,500 words. Longer for complex SaaS tools with many features.

## Error Handling

- **Only 1 product provided**: Auto-search for top 2 competitors. Inform user: "I found [B] and [C] as the main competitors — using those. Let me know if you want different ones."
- **No affiliate link for product_b**: Use homepage URL. Note in output: "No affiliate link for [B] — using homepage. You can still earn on [A] clicks."
- **Products in completely different categories**: Stop and ask — comparing an email tool to a project management tool is not useful.
- **Controversial product (MLM, scam accusations)**: Add warning note: "This product has mixed reputation signals. Review carefully before publishing — your credibility is at stake."
- **Tie on most dimensions**: Use "it depends" angle. Never force a winner that isn't real — readers trust honest comparisons more.

## Examples

**Example 1: Two affiliate products**
User: "Write a comparison post: HeyGen vs Synthesia"
Action: product_a=HeyGen (affiliate), product_b=Synthesia (affiliate), research both, detect angle=clear-winner (or it-depends based on data), write 3,000-word comparison targeting "heygen vs synthesia".

**Example 2: Chained from S1**
User: "Compare it with its top competitor"
Context: S1 returned HeyGen as recommended_program
Action: product_a=HeyGen from S1 output, web_search for top competitor, write comparison.

**Example 3: Three-way comparison**
User: "HeyGen vs Synthesia vs Colossyan comparison post"
Action: Three-way comparison, determine winner + runners-up, write 3,500-4,000 word article with side-by-side table.

**Example 4: Underdog angle**
User: "Compare Ahrefs vs Ubersuggest — I'm promoting Ubersuggest"
Action: product_a=Ubersuggest (affiliate), product_b=Ahrefs, angle=upset (lesser-known vs market leader), frame Ubersuggest as the budget-friendly winner for specific use cases.

## References

- `shared/references/ftc-compliance.md` — FTC disclosure text. Read in Step 5.
- `shared/references/affitor-branding.md` — Do NOT add Affitor branding to blog body. Only applies to landing pages.
- `shared/references/affiliate-glossary.md` — Terminology reference.
```

## File: `skills/blog/how-to-tutorial-writer/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/blog/how-to-tutorial-writer/SKILL.md`
```markdown
---
name: how-to-tutorial-writer
description: >
  Write how-to guides and tutorials that naturally integrate affiliate product recommendations.
  Triggers on: "write a how-to guide", "tutorial for [task]", "step by step guide to [goal]",
  "how to [verb] with [product]", "write a tutorial blog post", "guide on how to [task]",
  "beginner guide to [topic]", "walkthrough for [product]", "write an educational article",
  "how do I [task] blog post", "write a tutorial that promotes [product]".
---

# How-To Tutorial Writer

Write practical, step-by-step tutorial blog posts that solve a real reader problem and naturally recommend affiliate products as the best tool for the job. Uses the "problem → solution → tool" pattern: establish what the reader wants to do, show them exactly how to do it, and position the affiliate product as the right instrument for each step.

## When to Use

- User wants to create educational content that drives affiliate conversions indirectly
- User says "how to", "tutorial", "guide", "walkthrough", "step by step"
- User wants to rank for "how to [task]" keywords (high traffic, lower competition than "best" keywords)
- User has a product that is best understood through demonstration, not just description
- User wants to build authority and trust in a niche before making a sale

## Workflow

### Step 1: Define the Tutorial Goal

Parse the request to identify:
- **The task**: what the reader wants to accomplish (e.g., "create AI videos for YouTube")
- **The tool**: which affiliate product enables the task (e.g., HeyGen)
- **The audience**: who is asking this question (beginner / intermediate / advanced)
- **The end state**: what the reader will have built or achieved by the end

If the task is vague ("write a tutorial about HeyGen"), default to the most popular use case for that tool — search for it: `"[product name] tutorial" OR "how to use [product name]"` — pick the highest-traffic query.

**Tutorial types** — detect from user's phrasing:
| Signal | Type | Format |
|---|---|---|
| "How to get started", "beginners guide", "first time" | `quickstart` | 5-8 steps, 1,500-2,000 words |
| "Step by step", "complete guide", "full tutorial" | `deep-dive` | 8-15 steps, 2,500-3,500 words |
| "How to [specific feature]" | `feature-focus` | 5-8 steps on one feature, 1,500-2,000 words |
| "How to [goal] without [product]" → redirect to product | `problem-solution` | 6-10 steps, 2,000-2,500 words |

### Step 2: Research the Tutorial Content

Use `web_search` to gather:
1. The actual step-by-step process for accomplishing the task
2. Common mistakes or gotchas beginners encounter
3. Official documentation or help articles for the product
4. What the top-ranking tutorials already cover (identify gaps)

Search queries:
- `"how to [task] with [product]"` — understand existing guides
- `"[product] tutorial [year]"` — find current instructions
- `"[product] [feature] settings"` — get accurate step names
- `"[task] mistakes beginners make"` — find pain points to address

**Content accuracy rule**: Never invent product UI details. If unsure about a specific button name or menu path, describe the action generically ("navigate to the settings section") rather than naming something that may be wrong.

### Step 3: Plan the Tutorial Structure

Map every section before writing. A well-structured tutorial follows this flow:

**What readers need before starting (Prerequisites):**
- Account requirements (free plan vs. paid tier needed for tutorial steps)
- Technical requirements
- Assets they should have ready (images, scripts, data)

**The steps themselves:**
- Each step = one atomic action (not a cluster of actions)
- Steps should be numbered, not just bulleted
- Each step has: action verb headline + explanation + expected result
- Decision points get callout boxes: "If you see X, do Y instead"

**Affiliate integration points** (natural, not forced):
1. In the Prerequisites section: "You'll need a [Product] account. [Sign up free here →](url)"
2. At the step where the product's key feature is used: contextual CTA
3. After showing the final result: "You just did X with [Product]. Here's what else it can do: [affiliate CTA]"
4. In the "Next Steps" section at the end

**Rule**: Never interrupt a step sequence with a hard sell. CTAs belong at natural pause points — before the reader starts, after they finish a major phase, and at the very end.

### Step 4: Write the Full Tutorial

**Title formula:**
- `How to [Task] with [Product]: Step-by-Step Guide ([Year])`
- `How to [Task]: A Beginner's Guide Using [Product]`
- `[Goal]: How to [Task] in [N] Steps (Even If You're New to [Topic])`

**Introduction (150-200 words):**
- Open with the reader's problem/desire (not with "In this tutorial...")
- State the end result: "By the end, you'll have [specific output]"
- Mention how long it takes and what level of experience is needed
- One-sentence product intro: "[Product] is what makes this possible — here's how to use it."
- Affiliate CTA if they need to sign up before starting

**Prerequisites section:**
```
**What you need before starting:**
- A [Product] account (free plan works / Pro plan required for [specific feature])
  → [Create your free account →](affiliate_url)
- [Any other required tool/vault/assets/knowledge]
- Estimated time: [X minutes]
```

**Step-by-Step Section:**
Write each step as:
```
## Step [N]: [Action Verb] + [What You're Doing]

[2-4 sentence explanation of what this step does and why it matters]

1. [Specific sub-action with exact UI element names where known]
2. [Next sub-action]
3. [Continue...]

**You should see:** [description of what the expected result looks like]

> **Note:** [Optional callout for a common mistake or alternative path]
```

**Result/Output Section:**
After all steps, show what the reader has built:
- Describe the final output in concrete terms
- Include what they can do with it now
- Contextual affiliate CTA: "Now that you've [achieved X], you can use [Product]'s [feature] to take it further."

**Troubleshooting Section** (optional, high SEO value):
3-5 common issues readers might hit:
- "Error: [X]" → "This usually means [Y]. Fix it by [Z]."
- "Step 4 doesn't work if [condition]" → "Instead, try [alternative]."

**Next Steps Section:**
- What to do with the result
- Related features of the product to explore next
- Related tutorials (if user has other content)
- Final strong affiliate CTA

**FAQ Section (4-6 questions):**
- "Do I need a paid plan for [product] to follow this tutorial?"
- "How long does [task] take?"
- "Can I do this without [product]?"
- "Is [product] free to use for [task]?"
- "What should I do if [common problem]?"

### Step 5: Format Output

**Part 1: SEO Metadata**
```
---
SEO METADATA
---
Title: [title]
Slug: how-to-[task-slug]
Meta Description: [150-160 chars — include "how to", the task, and product name]
Target Keyword: how to [task] with [product]
Secondary Keywords: [product] tutorial, [task] guide, how to [task] [year], [product] for beginners
Word Count: [actual]
Format: how-to
Steps: [N]
---
```

**Part 2: Full Article**
Complete markdown ready to publish.

**Part 3: Supplementary Data**
- FAQ schema questions/answers
- Screenshot suggestions (one per major step)
- Products featured with affiliate URLs
- Video script outline (optional — if user wants to turn this into a YouTube tutorial)

## Input Schema

```yaml
task:                       # REQUIRED — what the reader wants to accomplish
  description: string       # e.g., "create an AI avatar video for YouTube"
  goal: string              # The end state — "a published YouTube video with AI avatar"

product:                    # REQUIRED — the affiliate tool that enables the task
  name: string
  description: string
  reward_value: string
  url: string               # Affiliate link
  reward_type: string
  cookie_days: number
  tags: string[]

tutorial_type: string       # OPTIONAL — "quickstart" | "deep-dive" | "feature-focus" | "problem-solution"
                            # Default: auto-detected from task complexity

audience_level: string      # OPTIONAL — "beginner" | "intermediate" | "advanced"
                            # Default: "beginner" (wider audience)

supporting_tools: object[]  # OPTIONAL — other tools used alongside the primary product
  - name: string
    url: string
    purpose: string         # What role this tool plays in the tutorial

target_keyword: string      # OPTIONAL — override default "how to [task]" keyword

tone: string                # OPTIONAL — "conversational" | "technical"
                            # Default: "conversational"

include_video_outline: boolean  # OPTIONAL — generate a YouTube video script outline alongside
                                # Default: false
```

## Output Schema

```yaml
article:
  title: string
  slug: string
  meta_description: string
  target_keyword: string
  format: "how-to"
  tutorial_type: string     # quickstart | deep-dive | feature-focus | problem-solution
  content: string
  word_count: number
  steps:
    - number: number
      headline: string      # Step heading
      affiliate_cta: boolean # Whether this step contains a CTA

products_featured:
  - name: string
    url: string
    role: string            # "primary-tool" | "supporting-tool"
    reward_value: string
    cta_placement: string[] # Which sections contain CTAs for this product

seo:
  secondary_keywords: string[]
  faq_questions:
    - question: string
      answer: string
  screenshot_suggestions:   # One per major step — high-value for tutorials
    - step: number
      description: string
      alt_text: string

video_outline:              # Only if include_video_outline=true
  title: string
  hook: string              # First 30 seconds script
  chapters:
    - timestamp: string     # e.g., "0:00"
      title: string
  description_for_youtube: string
  tags: string[]
```

## Output Format

Present as three sections:
1. **SEO Metadata** — fenced block for copy-paste into CMS
2. **Article** — complete markdown, immediately publishable
3. **Supplementary** — FAQ schema, screenshot suggestions, affiliate URLs, optional video outline

Target word count: 1,500-3,500 words based on tutorial type. Quality over length — do not pad steps.

## Error Handling

- **Task too vague** ("tutorial about email marketing"): Ask: "What specific task should the tutorial walk through? For example: 'how to set up an automated welcome email sequence in Mailchimp'."
- **No product provided**: "Which product should this tutorial feature? If you don't have one in mind, I can suggest the best tool for [task]."
- **Product feature requires paid plan**: Note clearly in Prerequisites section and add affiliate CTA. Do not hide paid requirements.
- **Task not suited for a single tutorial** (too complex): "This task has multiple phases — I'll write a [quickstart] tutorial focused on [first phase]. Let me know if you want additional tutorials for the other phases."
- **Product UI has changed**: Use generic action descriptions where UI details are uncertain. Add note: "Screenshots may vary slightly from your current version of [Product]."

## Examples

**Example 1: Product-driven tutorial**
User: "Write a tutorial on how to create AI avatar videos with HeyGen"
Action: task="create AI avatar video", product=HeyGen, audience=beginner, tutorial_type=deep-dive, write 12-step guide targeting "how to create ai avatar video with heygen".

**Example 2: Goal-driven tutorial**
User: "Write a how-to guide for automating social media posts"
Action: web_search for best social media automation tool, present to user for affiliate selection (or auto-select if S1 already ran), write problem-solution tutorial targeting "how to automate social media posts".

**Example 3: Feature-specific tutorial**
User: "Tutorial on how to use Semrush keyword magic tool"
Action: task="find keywords with Semrush Keyword Magic Tool", tutorial_type=feature-focus, write focused 8-step guide, affiliate CTAs at start and end.

**Example 4: With video outline**
User: "Write a HeyGen tutorial that I can also use as a YouTube video script"
Action: Same as Example 1 but with include_video_outline=true, output includes full video description, chapter markers, and hook script.

## References

- `shared/references/ftc-compliance.md` — FTC disclosure text. Insert after title.
- `shared/references/affiliate-glossary.md` — Terminology reference.
```

## File: `skills/blog/listicle-generator/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/blog/listicle-generator/SKILL.md`
```markdown
---
name: listicle-generator
description: >
  Write "Top N best..." listicle articles for affiliate marketing with mini-reviews, pricing,
  pros/cons, and CTAs per entry. Triggers on: "write a best of list", "top 10 [category] tools",
  "best [product category] article", "roundup post", "listicle about [category]",
  "write a top tools article", "best [N] alternatives to [product]", "product roundup",
  "write a tools comparison list", "best software for [use case]", "top picks for [category]".
---

# Listicle Generator

Write "Top N Best [Category]" roundup articles that rank on Google, capture featured snippets, and drive affiliate conversions across multiple products. Each list entry is a self-contained mini-review with features, pricing, pros/cons, audience fit, and a CTA. The article is structured to win both the featured snippet and the "People Also Ask" box.

## When to Use

- User wants to cover an entire product category with multiple affiliate links
- User says "best", "top", "roundup", "list of", or mentions a number with a category
- User wants to capture high-volume generic keywords ("best email marketing tools") vs. specific product searches
- User has multiple affiliate programs in the same category and wants one article to cover them all
- User wants an article format that benefits from regular updates (add/remove products as market evolves)

## Workflow

### Step 1: Determine List Parameters

Parse the user's request for:
- **Category**: what type of product (e.g., "email marketing tools", "AI video generators")
- **List size (N)**: explicitly stated number, or auto-select based on category depth
  - Niche/specialized categories: 5-7 products
  - Broad/competitive categories: 7-10 products
  - Very broad (e.g., "project management tools"): 10-12 products
- **Target audience**: inferred from category + any context clues (beginners, enterprises, specific industries)
- **Year**: always use current year in the title for freshness signal

**If no affiliate product is specified:**
- Ask: "Which product are you promoting? I'll feature it prominently in the list."
- If user says to proceed anyway, generate a balanced list and note where they should insert their affiliate link.

### Step 2: Research the Product Landscape

Use `web_search` to build the product list:

1. **Seed query**: `"best [category] tools [year]" site:g2.com OR site:capterra.com OR site:trustradius.com`
2. **Validate with traffic**: `"best [category]"` — check autocomplete for common phrasings
3. **Find affiliate programs**: `"[category] affiliate program"` — identify which products offer commissions

For each candidate product, gather:
- Product name and one-line description
- Starting price and free plan availability
- G2/Capterra rating (if available)
- The one thing it does best (unique angle)
- Who it's primarily designed for

**Affiliate prioritization rules:**
- Position the user's affiliate product at #1 or #2 (never lower than #3 unless it genuinely cannot be defended in the top 3)
- #1 position gets the most clicks — use it for the highest-commission or best-converting product
- If the user has multiple affiliate programs, spread them in positions 1, 2, and 4
- Non-affiliate products fill the remaining slots to make the list credible and balanced

### Step 3: Plan the Article Structure

Map out every section before writing:

**Article structure:**
1. Title (with year, number, category)
2. FTC disclosure
3. Introduction (150-200 words)
4. "At a Glance" summary table
5. Evaluation criteria (H2)
6. Individual product entries × N (H2 each)
7. Comparison table (all products × key dimensions)
8. How to Choose (H2)
9. FAQ (H2)
10. Final Recommendation (H2)

**Per-entry structure** (400-600 words each):
- H2: `[Rank]. [Product Name] — [One-line Value Prop]`
- Opening paragraph: what it is, who made it, why it's on this list
- Key features section (3-5 bullet points)
- Pricing table (free / starter / pro / enterprise)
- Pros list (4-5 bullets)
- Cons list (2-3 bullets — be honest, builds trust)
- Best for: one sentence naming the ideal user
- Affiliate CTA button: `[Try [Product] free →](url)`

### Step 4: Write the Full Article

**Title formula:** `[N] Best [Category] Tools in [Year] (Ranked and Reviewed)`
Alternative: `Best [Category] Software: Top [N] Picks for [Year]`

**Introduction (150-200 words):**
- Open with the core problem this category solves
- Mention how many tools you evaluated and your selection criteria
- Name-drop 2-3 products from the list to signal comprehensiveness
- End with a transition: "Here are the [N] best options I found."

**"At a Glance" Table** (immediately after intro, captures featured snippet):
```
| Tool | Best For | Starting Price | Free Plan |
|---|---|---|---|
| [Product 1] | [Use case] | $X/mo | ✅ |
| [Product 2] | [Use case] | $Y/mo | ❌ |
```

**Evaluation Criteria (H2, before the list):**
List the 4-6 criteria used to rank products. This builds credibility and explains why your #1 pick is #1.
Example criteria: ease of use, feature depth, pricing value, customer support quality, integration ecosystem, scalability.

**Individual Product Entries:**
Write each entry following the per-entry structure above. Vary the opening sentence — don't start every entry the same way. Include specific, verifiable details (actual feature names, real pricing tiers, concrete limitations) — not generic praise.

**Master Comparison Table:**
After all product entries, include a comprehensive feature matrix:
```
| Feature | [P1] | [P2] | [P3] | [P4] | [P5] |
|---|---|---|---|---|---|
| Free plan | ✅ | ❌ | ✅ | ⚠️ | ✅ |
| [Key feature] | ✅ | ✅ | ❌ | ✅ | ❌ |
| [Key feature] | ⭐ Best | Good | Limited | Good | Basic |
| Starting price | $X | $Y | $Z | $A | Free |
```

**How to Choose (H2, 300-400 words):**
A decision framework for readers who are still unsure after reading the list:
- "If you're a beginner with a tight budget → [Product X]"
- "If you need [specific feature] → [Product Y]"
- "If you're scaling a team → [Product Z]"
- "If you're migrating from [common competitor] → [Product A]"

**FAQ Section (5-7 questions):**
- "What is the best [category] tool?"
- "What is the cheapest [category] tool?"
- "What [category] tool has the best free plan?"
- "Is [top product] worth it?"
- "How do I choose [category] software?"

**Final Recommendation (H2):**
- Restate the #1 pick with a 2-sentence reason
- Give a backup pick for a different audience
- Strong CTA: `**Start with [Product] — it's free to try.** [Get started →](affiliate_url)`

### Step 5: Format Output

**Part 1: SEO Metadata**
```
---
SEO METADATA
---
Title: [title with year and number]
Slug: best-[category-slug]-tools
Meta Description: [150-160 chars, include number + year + top product name]
Target Keyword: best [category] tools
Secondary Keywords: [category] software, [product 1] review, [product 2] alternatives, top [category] [year]
Word Count: [actual]
Format: listicle
Products: [N]
---
```

**Part 2: Full Article**
Complete markdown ready to publish.

**Part 3: Supplementary Data**
- FAQ questions for schema markup
- Image suggestions (product screenshots, comparison screenshots)
- All products with affiliate URLs flagged
- Update reminder: "This article should be refreshed every 6 months to keep rankings."

## Input Schema

```yaml
category:                   # REQUIRED — product category to cover
  name: string              # e.g., "AI video generators", "email marketing platforms"
  tags: string[]            # Optional — helps with research targeting

primary_product:            # OPTIONAL but recommended — the affiliate product to feature at #1
  name: string
  description: string
  reward_value: string
  url: string               # Affiliate link
  reward_type: string
  cookie_days: number
  tags: string[]

additional_affiliates:      # OPTIONAL — other affiliate products to include in the list
  - name: string
    url: string
    reward_value: string

list_size: number           # OPTIONAL — how many products (5-12). Default: auto-select.

target_audience: string     # OPTIONAL — "beginners" | "enterprise" | "freelancers" | "agencies"
                            # Default: inferred from category

year: number                # OPTIONAL — year for title/freshness. Default: current year.

target_keyword: string      # OPTIONAL — override default keyword
tone: string                # OPTIONAL — "conversational" | "professional". Default: "conversational"
```

## Output Schema

```yaml
article:
  title: string
  slug: string
  meta_description: string
  target_keyword: string
  format: "listicle"
  content: string
  word_count: number
  product_count: number

products_featured:
  - name: string
    url: string
    rank: number            # Position in the list (1 = top)
    role: string            # "affiliate-primary" | "affiliate-secondary" | "editorial"
    reward_value: string

seo:
  secondary_keywords: string[]
  at_a_glance_table: string   # Markdown table — can be extracted for featured snippet
  faq_questions:
    - question: string
      answer: string
  image_suggestions:
    - description: string
      alt_text: string
      placement: string

update_schedule:
  recommended_frequency: string   # "every 6 months" for most categories
  items_to_check: string[]        # What to verify on next update
```

## Output Format

Present as three sections:
1. **SEO Metadata** — fenced block for copy-paste into blog CMS
2. **Article** — full markdown, immediately publishable
3. **Supplementary** — FAQ schema, image suggestions, affiliate URLs, update notes

Target word count: 3,000-5,000 words depending on list size (aim for 400-500 words per product entry plus structural sections).

## Error Handling

- **No category provided**: "What category of products should this listicle cover? For example: 'best email marketing tools' or 'top AI writing assistants'."
- **No affiliate product specified**: Generate a balanced editorial list. Flag in output: "Affiliate link not set — insert your tracking URL for [top pick] before publishing."
- **Category too broad** ("best software"): Narrow it. Ask: "That's very broad — can you narrow it down? For example: 'best project management software for small teams'."
- **Category too niche** (fewer than 5 good products exist): Reduce list size and be transparent: "Only 5 strong options exist in this niche — I've included all of them."
- **Product research returns low-quality results**: Use web_search with 3 different query variations before giving up. Fallback: base entries on official product pages + G2 reviews.

## Examples

**Example 1: Standard category listicle**
User: "Write a top 10 best AI video tools article"
Action: category="AI video generators", list_size=10, research top tools, position user's affiliate at #1, write 4,500-word listicle targeting "best ai video tools [year]".

**Example 2: Niche with specific audience**
User: "Best email marketing tools for e-commerce, I'm promoting Klaviyo"
Action: category="email marketing for e-commerce", primary_product=Klaviyo, target_audience="e-commerce store owners", list_size=7, write article with Klaviyo at #1.

**Example 3: Alternatives format**
User: "Write a 'best alternatives to Mailchimp' article"
Action: Treat as listicle where Mailchimp is the incumbent being replaced. Title: "7 Best Mailchimp Alternatives in [Year] (Cheaper + More Powerful)". Position user's affiliate at #1 as top alternative.

**Example 4: Chained from S1**
User: "Now write a roundup post for the category"
Context: S1 returned Semrush in the SEO tools category
Action: category=SEO tools, primary_product=Semrush, auto-select list_size=8, write "Best SEO Tools [year]" with Semrush at #1.

## References

- `shared/references/ftc-compliance.md` — FTC disclosure text. Read before Step 4.
- `shared/references/affiliate-glossary.md` — Terminology reference.
```

## File: `skills/content/reddit-post-writer/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/content/reddit-post-writer/SKILL.md`
```markdown
---
name: reddit-post-writer
description: >
  Write Reddit posts and comments that recommend affiliate products without getting
  banned or flagged as spam. Subreddit-native content that adds value first.
  Use this skill when the user asks about Reddit posts for affiliate marketing,
  writing Reddit comments that mention products, how to promote affiliate links on
  Reddit, or says "write a Reddit post for X", "how to mention affiliate on Reddit",
  "Reddit comment promoting product", "Reddit-friendly affiliate content", "post
  for r/[subreddit] about X", "share affiliate link on Reddit without getting banned",
  "genuine Reddit recommendation", "organic Reddit affiliate post", "Reddit thread
  idea for product".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S2-Content
---

# Reddit Post Writer

Write Reddit posts and comments that earn upvotes by leading with genuine value.
The affiliate recommendation comes second — after trust is built. Reddit users
have a finely tuned spam detector. This skill helps affiliates write like Redditors,
not marketers.

## Stage

This skill belongs to Stage S2: Content

## When to Use

- User wants to drive affiliate traffic from Reddit
- User wants to recommend a product in a relevant subreddit
- User is active in a community and wants to add a helpful product mention
- User has a genuine experience with a product and wants to share it naturally
- User asks how to participate on Reddit without getting banned for self-promotion

## Input Schema

```
{
  product: {
    name: string              # (required) "Notion"
    description: string       # (optional) What the product does
    url: string               # (optional) Affiliate link — used in disclosure only
    reward_value: string      # (optional) Commission — never revealed in post
  }
  subreddit: string           # (optional) Target subreddit, e.g., "r/productivity"
  post_type: string           # (optional, default: auto) "post" | "comment_reply" | "ama_style"
  trigger_question: string    # (optional) Specific Reddit question or post you're replying to
  personal_experience: string # (optional) Real experience with the product to use as anchor
  audience: string            # (optional) Who reads this subreddit — "students", "developers"
  tone: string                # (optional, default: "genuine") "genuine" | "analytical" | "casual"
  problem_focus: string       # (optional) The specific problem this post addresses
}
```

## Workflow

### Step 1: Understand Reddit Culture First

Before writing, confirm the target subreddit context. If subreddit is provided,
use `web_search "reddit r/[subreddit] rules affiliate"` to check:
- Are affiliate links explicitly banned? (many subreddits ban them outright)
- What post formats are most common? (links, text posts, discussions)
- What gets upvoted vs. downvoted in this community?
- Is there a community expectation of neutrality or personal experience?

**Subreddits that generally tolerate product mentions:**
r/productivity, r/entrepreneur, r/Entrepreneur, r/sidehustle, r/personalfinance,
r/freelance, r/marketing, r/SEO, r/webdev, r/startups, r/smallbusiness

**Subreddits that are extremely ban-happy about promotion:**
r/frugal, r/cscareerquestions, r/AskReddit, r/personalfinance (strict on direct links)

If subreddit bans affiliate links: do NOT write a post with a link. Instead, write
a post that mentions the product by name with a note like "Search for [product]
affiliate program if interested." Disclose and redirect.

### Step 2: Determine the Post Type

**Option A — Original Post (new thread):**
Best when there's no existing discussion. Write a story, question, or breakdown that
organically leads to a product mention.
- "How I went from X to Y — the exact tools I used"
- "Anyone else use [product] for [use case]? Here's my 6-month review"
- "I tested 5 [category] tools so you don't have to — honest breakdown"

**Option B — Comment Reply (responding to an existing post):**
Highest trust format. Someone asks "what tool do you use for X?" and you reply helpfully.
- Write a substantive answer that doesn't mention the product until the 3rd+ paragraph
- Add value even without the product mention — if removed, the comment should still be helpful
- Product mention: "Personally, I use [product] and it's been solid for [specific use case]"

**Option C — AMA-Style / Experience Share:**
"I've been doing [X] for [N] years. Happy to share what's worked."
- Opens conversation, positions creator as authority
- Product naturally comes up when people ask "what tools do you use?"

If `trigger_question` is provided → use Option B. Otherwise, default to Option A.

### Step 3: Research Product and Find Reddit-Specific Angles

Use `web_search "reddit [product name] review"` to find:
- What real Reddit users are saying about the product (use their language)
- Common objections raised on Reddit (address these proactively)
- How competitors are discussed (context for framing)
- Questions people ask that your post can answer

Also use `web_search "reddit [problem space] best tools"` to understand:
- What alternatives Redditors currently recommend
- How to frame your recommendation as additive, not replacing their preferences
- What not to say (phrases that get downvoted in this community)

### Step 4: Write the Post

**Reddit post structure that converts:**

1. **Title** (for new posts): specific, searchable, sounds like a real person's question or story
   - Good: "I tried 4 project management tools over 2 years — here's what I actually use now"
   - Bad: "The BEST productivity tool I've ever used!! (link in post)"
   - Good: "[6 months update] How I finally stopped context-switching between apps"

2. **Opening paragraph**: establish credibility or relatability. NO product mention here.
   - "I've been freelancing for 3 years and I'm embarrassed by how long I tried to manage
     everything in spreadsheets."

3. **Body**: share the actual useful content — your experience, the problem, what you tried.
   This section should be valuable even without the product mention.

4. **Product introduction** (70-80% through the post): introduce naturally.
   - "Eventually I landed on [product] and I've stuck with it for [X months]."
   - Specific use case: what exactly you use it for, not vague praise
   - ONE honest con: "It's not perfect — the mobile app is weak — but for desktop work
     it's exactly what I needed." Cons dramatically increase trust.

5. **FTC disclosure** (at the bottom):
   - "Full disclosure: the link in my profile leads to an affiliate link. No extra cost
     to you, and I would recommend this tool regardless."
   - Or if not posting a link: "Not affiliated, just a genuine fan."
   - Per `shared/references/ftc-compliance.md` — disclosure is required for Reddit too.

6. **Closing**: invite discussion, not clicks.
   - "Happy to answer questions about my workflow in the comments."
   - Ask a question back: "What does your current setup look like?"

### Step 5: Anti-Spam Checklist

Before finalizing, run through this checklist:

- [ ] Post adds value even if the product mention is removed
- [ ] No exclamation marks in praise ("This tool is AMAZING!!")
- [ ] No superlatives without evidence ("best tool I've ever used" → needs qualifier)
- [ ] Affiliate link goes in comments or profile bio, NOT the main post body (most subreddits)
- [ ] FTC disclosure is present and clear
- [ ] Post doesn't read like a press release
- [ ] Includes at least one real limitation or caveat about the product
- [ ] Tone matches the subreddit (match voice to community)
- [ ] Username context matters — new accounts posting affiliate content get instant downvotes

### Step 6: Add Engagement Strategy

Reddit rewards participation, not broadcasting. Include:
1. **Reply strategy**: when commenters respond, how to keep conversation going naturally
2. **Upvote path**: what type of engagement to solicit (awards, saves, discussion)
3. **Subreddit timing**: best day/time to post in this subreddit
4. **Cross-post candidates**: which other subreddits this post could work in

## Output Schema

```
{
  post: {
    type: string              # "post" | "comment_reply" | "ama_style"
    subreddit: string         # "r/productivity"
    title: string | null      # For new posts only
    body: string              # Full post/comment body
    link_placement: string    # Where to put the affiliate link
    disclosure: string        # The disclosure text used
    char_count: number
  }
  subreddit_notes: {
    allows_affiliate_links: boolean
    community_tone: string
    best_post_time: string
    cross_post_subreddits: string[]
  }
  engagement_tips: string[]
  product_name: string
  content_angle: string
}
```

## Output Format

```
## Reddit Post: [Product Name]

**Type:** [New Post / Comment Reply / AMA-style]
**Target Subreddit:** [r/subreddit]
**Subreddit allows affiliate links:** [Yes / No / Link in comments only]

---

### Post Title (for new posts)

[Post title here]

---

### Post Body

[Full post text, formatted with Reddit markdown — use **bold**, *italic*, > quotes
as appropriate. Paragraphs separated by blank lines.]

---

### Link Placement

[Where to put the affiliate link — in post, in comment, or profile bio — and why]

---

### Subreddit Notes

- **Community tone:** [What vibe this subreddit has]
- **Best time to post:** [Day and time]
- **Watch out for:** [Specific rules or sensitivities]

---

### Cross-Post Opportunities

This post could also work in:
1. [r/subreddit2] — [why]
2. [r/subreddit3] — [why]

---

### Engagement Tips

1. [How to respond to likely comments]
2. [How to handle skeptics or downvotes]
3. [When to resurface this content]

---

### Alternative Angles

- **[Alternative 1]:** [Different framing for the same product]
- **[Alternative 2]:** [...]
```

## Error Handling

- **Subreddit bans affiliate links outright:** Flag this clearly. Rewrite without a direct
  link — mention the product by name only, disclosure becomes "not affiliated, genuine rec."
  Suggest building karma in the subreddit first with unrelated helpful posts.
- **No personal experience provided:** Write from a researched perspective but clearly label
  it as such ("Based on what I've seen from other users..."). Recommend the user add their
  own experience before posting — fabricated personal experience on Reddit gets called out.
- **Product is controversial on Reddit:** Acknowledge the controversy directly in the post.
  "I know [product] gets mixed reviews here. Here's my honest take after [X months]..."
  This signals authenticity and pre-empts downvote brigading.
- **User asks to mass-post the same content:** Refuse this pattern. It's spam and will
  result in account bans. Write unique versions for each subreddit.
- **New Reddit account:** Add warning: "New accounts posting affiliate content are
  immediately suspect. Build 3-6 months of genuine participation first."
- **Product has no free tier / high price:** Don't hide this. State the price early.
  "It's not cheap — $X/mo — but here's why it's been worth it for me."

## Examples

**Example 1:**
User: "Write a Reddit post for r/productivity recommending Notion"
→ No trigger question → write original post
→ Title: "Finally stopped fighting my productivity system — 18 months with Notion"
→ Body: relatable struggle with scattered notes → what I tried → landed on Notion →
  specific workflows I use → honest con (learning curve) → disclosure at bottom
→ Affiliate link in first comment, not the post body

**Example 2:**
User: "Someone on r/freelance asked 'what tools do you use to manage clients?' — write a reply"
→ Comment reply format, responding to that specific question
→ Open with the full workflow (3-4 tools) — Notion is one of several, not the only mention
→ Position Notion as the project management layer specifically
→ Mention it's in my profile link if they want the affiliate version
→ Disclosure at bottom of comment

**Example 3:**
User: "Write a Reddit post about HeyGen for r/videography"
→ Check r/videography rules — likely strict about promotion
→ Frame as experience share: "I tried AI avatar video for client work — here's my honest take"
→ Include real limitations prominently (not real filmmaker footage, uncanny valley)
→ Position as "works for explainer/promo videos, not cinema" — niche and honest
→ Disclosure present, link in comments only

## References

- `shared/references/ftc-compliance.md` — FTC disclosure requirements for Reddit
- `shared/references/platform-rules.md` — Reddit-specific format and link rules
- `shared/references/affiliate-glossary.md` — terminology
```

## File: `skills/content/tiktok-script-writer/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/content/tiktok-script-writer/SKILL.md`
```markdown
---
name: tiktok-script-writer
description: >
  Write short-form video scripts for TikTok, Instagram Reels, and YouTube Shorts
  that promote affiliate products with strong hooks, demos, and CTAs.
  Use this skill when the user asks about TikTok scripts, Reels scripts, Shorts
  scripts, short-form video for affiliate marketing, or says "write a TikTok for X",
  "script a Reel promoting X", "YouTube Shorts script affiliate", "60-second video
  script", "hook for TikTok affiliate", "write a video promoting X", "TikTok script
  that converts", "short video script for product review", "viral TikTok affiliate
  script", "how to promote X on TikTok".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S2-Content
---

# TikTok Script Writer

Write punchy 30-60 second video scripts for TikTok, Instagram Reels, and YouTube
Shorts that stop the scroll, demo the product naturally, and drive affiliate link
clicks. Every script is structured for vertical video: hook → problem → demo →
result → CTA.

## Stage

This skill belongs to Stage S2: Content

## When to Use

- User wants to promote an affiliate product on short-form video platforms
- User has an affiliate program picked (from S1) and needs TikTok/Reels content
- User asks for video script ideas for TikTok affiliate marketing
- User wants a hook-first script that converts viewers to buyers
- User creates content on TikTok, Instagram Reels, or YouTube Shorts

## Input Schema

```
{
  product: {
    name: string              # (required) "HeyGen"
    description: string       # (optional) What it does — will be researched if missing
    url: string               # (optional) Affiliate link or product URL
    reward_value: string      # (optional) Commission info — never shown in script
  }
  duration: number            # (optional, default: 45) Target duration in seconds: 15 | 30 | 45 | 60
  platform: string            # (optional, default: "tiktok") "tiktok" | "reels" | "shorts" | "all"
  hook_style: string          # (optional, default: auto) "question" | "shock" | "relatable" | "bold_claim" | "demo_first"
  creator_persona: string     # (optional) "beginner marketer" | "tech reviewer" | "productivity nerd"
  has_product_access: boolean # (optional, default: true) Can creator do live demo?
  personal_experience: string # (optional) Real experience to weave in
  audience: string            # (optional) "freelancers" | "small business owners" | "students"
}
```

## Workflow

### Step 1: Research the Product

If product details are sparse, use `web_search "[product name] what it does tutorial"` to find:
- The single most impressive thing the product does (demo-able in <20 seconds)
- The main pain it eliminates (hook material)
- A specific result users achieve (e.g., "make a talking avatar video in 2 minutes")
- Any free trial or free tier (reduces friction for CTA)

Concrete specifics > vague claims. "Creates a 2-minute video in 30 seconds" beats
"saves time on video creation".

### Step 2: Select the Hook Style

Short-form video is won or lost in seconds 1-3. Pick the hook based on the product's
strongest angle:

| Hook Style | Template | Best For |
|------------|----------|----------|
| **Question** | "What if you could [result] without [pain]?" | Products that remove a hard task |
| **Shock/Stat** | "I replaced [expensive thing] with a $[price]/mo tool" | Cost/efficiency wins |
| **Relatable** | "[Frustrating situation]? Same. Then I found this." | Niche audience pain |
| **Bold Claim** | "This [tool] is the reason I [impressive result]" | Strong ROI proof |
| **Demo First** | [Open with screen recording of the coolest feature immediately] | Visual/AI tools |
| **Story Opener** | "6 months ago I was [before state]. Now [after state]. Here's why." | Transformation |

For AI tools and visual products → **Demo First** almost always wins on TikTok.
For SaaS productivity tools → **Relatable** or **Shock/Stat** hooks work well.

### Step 3: Structure the Script

Every script follows this structure (adapt timing to duration):

**For 45-second scripts:**
- 0-3s: Hook (spoken + on-screen text)
- 3-8s: Relatable pain or setup
- 8-30s: Live demo OR narrated walkthrough of key feature
- 30-38s: Specific result / proof
- 38-44s: CTA (bio link, comment for link, or "link in bio")
- 44-45s: FTC disclosure overlay

**For 30-second scripts:**
- 0-3s: Hook
- 3-15s: Demo the #1 feature
- 15-25s: Result + social proof
- 25-30s: CTA + disclosure

**For 60-second scripts:**
- 0-3s: Hook
- 3-10s: Problem setup
- 10-40s: Full demo (2-3 features)
- 40-52s: Results + pricing mention (anchoring)
- 52-58s: CTA
- 58-60s: FTC disclosure

### Step 4: Write the Script

Format scripts with:
- **[VISUAL]** — what's on screen (screen recording, hands typing, reaction face, b-roll)
- **[SPOKEN]** — what the creator says (keep sentences short, max 10 words each)
- **[TEXT OVERLAY]** — on-screen text (keywords for silent viewers — 40% watch with no sound)
- **[CAPTION]** — suggested TikTok caption + hashtags

Writing rules:
1. Sentences under 10 words. TikTok viewers process fast.
2. No filler phrases: "basically", "literally", "you know what I mean"
3. Every 3-5 seconds: new visual cut, new text overlay, or spoken transition
4. Sound-optional: the text overlay should tell the whole story without audio
5. End the hook WITH the setup — don't just ask a question, tease the answer
6. The demo must be REAL — no vague "and then it does this amazing thing"

### Step 5: Add FTC Disclosure

Per `shared/references/ftc-compliance.md` for short-form video:
- Verbal disclosure if spoken at all (not required but best practice)
- Text overlay "#ad" or "Affiliate link in bio" must appear during CTA section
- Disclosure must be visible for at least 3 seconds
- Do NOT bury in caption — overlay is required per FTC guidance

### Step 6: Add Production Notes

Include brief notes for the creator:
- What to screen-record vs. film on camera
- Suggested background music BPM range (fast = tech demos, mid = tutorials)
- Caption and hashtag strategy for the platform
- Best time to post on each platform

## Output Schema

```
{
  scripts: [
    {
      platform: string          # "tiktok" | "reels" | "shorts"
      duration_seconds: number  # 45
      hook_style: string        # "demo_first"
      scenes: [
        {
          timecode: string      # "0-3s"
          visual: string
          spoken: string
          text_overlay: string
        }
      ]
      caption: string           # Full TikTok caption
      hashtags: string[]        # Suggested hashtags
      disclosure: string        # How and when FTC disclosure appears
    }
  ]
  product_name: string
  content_angle: string
  hook_used: string
}
```

## Output Format

```
## TikTok Script: [Product Name] ([Duration]s)

**Hook Style:** [Style name]
**Platform:** [TikTok / Reels / Shorts]
**Target Audience:** [Who this is for]

---

### Script

| Time | Visual | Spoken | Text Overlay |
|------|--------|--------|-------------|
| 0-3s | [What's on screen] | "[Hook line]" | [On-screen text] |
| 3-8s | [Visual] | "[Spoken]" | [Overlay] |
| ... | ... | ... | ... |

---

### Caption

[Full caption text — optimized for TikTok SEO]

**Hashtags:** #[tag1] #[tag2] #[tag3] (5-8 tags max)

---

### Production Notes

- **Film:** [Camera vs screen recording breakdown]
- **Music:** [BPM and mood suggestion]
- **Best time to post:** [Platform-specific optimal time]
- **Disclosure:** #ad text overlay appears at [timecode] for [X] seconds

---

### Hook Alternatives

Want a different opening? Try:
- **[Hook Style 2]:** "[Alternative opening line]"
- **[Hook Style 3]:** "[Alternative opening line]"
```

## Error Handling

- **No product info:** Ask what product they're promoting. If they came from S1, pull
  `recommended_program` from context.
- **Product isn't visual / hard to demo:** Shift to reaction/testimonial format —
  creator's face on screen reacting to the tool, narrating the discovery.
- **User has no product access:** Write a "third-person discovery" script —
  "My friend showed me this tool and I had to share it"
- **Duration feels too long for the content:** Cut the demo to single strongest moment.
  If 30s still feels crowded, suggest two separate videos (problem setup + solution).
- **Platform unspecified:** Default to TikTok. Mention Reels and Shorts are the same script
  with minor caption/hashtag adjustments.

## Examples

**Example 1:**
User: "Write a 45-second TikTok script for HeyGen"
→ Research: HeyGen creates AI avatar videos, talking head from text
→ Hook: Demo first — open with a finished AI video playing
→ Script: [0-3s] Show output video → [3-8s] "Made this in 2 minutes, no camera" →
  [8-30s] Screen record: paste script → avatar speaks → [30-38s] "Used this for
  my client, saved 4 hours" → [38-44s] "Link in bio, 30-day free trial" → [44-45s] "#ad overlay"

**Example 2:**
User: "TikTok script for Notion affiliate, targeting students"
→ Hook: Relatable — "POV: it's 2am before finals and your notes are chaos"
→ Demo: Notion AI organizing scattered notes into a study guide
→ CTA: "Free forever plan — link in bio"
→ Caption: "study with me + notion hacks" for algorithm reach

**Example 3:**
User: "I need 3 different hooks for a ConvertKit TikTok script"
→ Write hook-only variants: Question / Shock / Bold Claim
→ Full script for the strongest one, alternative openings for others
→ Note which hook style historically performs best for SaaS on TikTok

## References

- `shared/references/ftc-compliance.md` — disclosure rules for short-form video
- `shared/references/affiliate-glossary.md` — reward_type and program terminology
- `shared/references/platform-rules.md` — TikTok/Reels/Shorts format specs
```

## File: `skills/content/twitter-thread-writer/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/content/twitter-thread-writer/SKILL.md`
```markdown
---
name: twitter-thread-writer
description: >
  Write X/Twitter threads that get bookmarked, shared, and drive affiliate clicks.
  Use this skill when the user asks about writing Twitter threads, X threads, tweet
  threads for affiliate marketing, or says "write a thread about X", "Twitter thread
  promoting X", "X thread for affiliate", "write tweets that go viral", "thread that
  sells without selling", "educational thread with affiliate CTA", "Twitter content
  for affiliate marketing", "how to promote X on Twitter", "write a thread my
  audience will bookmark", "tweet storm about affiliate product".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S2-Content
---

# Twitter Thread Writer

Write X/Twitter threads that deliver genuine value, build authority, and naturally
recommend affiliate products without feeling like ads. The best affiliate threads
get bookmarked for the insights and clicked for the product recommendation.

## Stage

This skill belongs to Stage S2: Content

## When to Use

- User wants to promote an affiliate product on X/Twitter
- User wants to build an audience on X while monetizing with affiliate links
- User has expertise to share and wants to weave in a product recommendation
- User asks how to write threads that convert without being spammy
- User wants content that compounds (bookmarks → future impressions)

## Input Schema

```
{
  product: {
    name: string              # (required) "ConvertKit"
    description: string       # (optional) What it does
    url: string               # (optional) Affiliate link
    reward_value: string      # (optional) For context only — never shown in thread
  }
  thread_angle: string        # (optional, default: auto) See Thread Frameworks below
  expertise_area: string      # (optional) Creator's area of authority — "email marketing", "SaaS growth"
  audience: string            # (optional) "founders", "freelancers", "content creators"
  tone: string                # (optional, default: "direct") "direct" | "educational" | "storytelling" | "contrarian"
  tweet_count: number         # (optional, default: 8) Number of tweets in thread: 5-15
  personal_story: string      # (optional) Real experience or result to anchor the thread
  cta_style: string           # (optional, default: "soft") "soft" | "direct" | "question"
}
```

## Workflow

### Step 1: Research the Product and Angle

Use `web_search "[product name] best features use cases"` and
`web_search "[product name] vs [competitor]"` to find:
- The 2-3 strongest use cases (thread body material)
- The problem it solves that X audiences care about
- Any recent updates, launches, or news (recency boosts engagement)
- Real user testimonials or case study numbers (third-party proof)

Also search `web_search "site:twitter.com [product name] affiliate"` to see what
existing threads look like — then do something different or better.

### Step 2: Select the Thread Framework

| Framework | Structure | Best For |
|-----------|-----------|----------|
| **Lessons Learned** | "I used [product] for X months. Here's what I learned:" → 7 insights → CTA | Tools you've genuinely used |
| **Problem → Solution** | Hook pain → Agitate it → Introduce solution → Show how it solves each pain → CTA | High-awareness problems |
| **Contrarian Take** | "Everyone says [common advice]. I disagree. [product] changed my mind." | Standing out in crowded niches |
| **Numbers Story** | "From [before metric] to [after metric] using [product]. Here's how:" → step-by-step → CTA | When you have real results |
| **How-to Tutorial** | "How to [achieve outcome] with [product] in [timeframe]:" → step-by-step → CTA | Educational, drives bookmarks |
| **Tool Stack** | "My [role] tool stack in 2024: Thread on each → [product] gets its own deep-dive tweet → CTA | Multi-product threads |
| **Myth Busting** | "5 myths about [problem space] — and what actually works:" → each myth → [product] as the solution | High engagement, saves |

Auto-select based on:
- Has personal experience → Numbers Story or Lessons Learned
- No personal experience → How-to Tutorial or Problem → Solution
- Large audience, strong takes → Contrarian Take
- Beginner-friendly product → How-to Tutorial

### Step 3: Write the Hook Tweet (Tweet 1)

The hook tweet determines if anyone reads tweet 2. It must:
- Promise a specific, tangible outcome ("how I 3x'd my email open rate")
- Or state a bold, curiosity-generating claim ("most email marketing advice is wrong")
- Or open a story loop ("6 months ago I had 400 email subscribers. Today I have 12,000.")
- End with a signal that a thread follows: "A thread:" or "Here's how:" or "Thread 🧵"

Never start with: "I want to share...", "In this thread...", "Have you ever..."
Never use buzzwords as hooks: "game-changing", "revolutionary", "must-read"

**Hook formula:** [Specific outcome or bold claim] + [Credibility signal] + [Thread signal]

### Step 4: Write the Body Tweets (Tweets 2-N)

Each tweet in the body must:
1. **Deliver a complete thought** — readable as a standalone tweet
2. **Build on the previous tweet** — threads should reward people who read all the way
3. **Include a specific detail** — numbers, names, steps, not vague generalizations
4. **Stay under 280 characters** — hard limit. No tweet should require expanding
5. **Use whitespace** — line breaks between ideas, not wall-of-text tweets

Place the product recommendation at 60-70% through the thread (tweet 5-7 of 8-10).
It should feel discovered, not pitched:
- "The tool that actually made this easy for me: [product name]"
- "I tried 4 tools before finding [product]. Here's why it worked:"
- "If I had to pick one tool for this: [product]"

Mention the product once prominently. A brief second mention in the CTA tweet is fine.

### Step 5: Write the CTA Tweet (Last Tweet)

The CTA tweet should:
1. Summarize what the thread delivered
2. Recommend action (try the product, sign up, or check it out)
3. Include the affiliate link OR direct to bio for the link
4. Include FTC disclosure "#ad" per `shared/references/ftc-compliance.md`

Soft CTA example: "If you want to try [product], there's a free trial at [link]. I use it daily. #ad"
Direct CTA: "[Product] is how I [result]. Link to try it free: [link] #ad"

### Step 6: Add Engagement Mechanics

Increase bookmark and retweet probability:
1. **Add a summary tweet** after the CTA: "TL;DR: [3 bullets from the thread]"
   Summaries drive bookmarks from skimmers.
2. **First reply** (pinned under thread): "If you found this useful, follow me for more [topic]."
3. **Engagement question** somewhere in thread: "Which of these do you do already?
   Drop your answer below." (Boosts reply count → algorithm boost)

### Step 7: Format Output

Present tweets numbered and ready to paste. Include character count for each.
Flag any tweet at 250+ characters for potential trimming.

## Output Schema

```
{
  thread: [
    {
      tweet_number: number      # 1, 2, 3...
      content: string           # Full tweet text
      char_count: number        # Character count
      role: string              # "hook" | "body" | "product_mention" | "cta" | "summary"
    }
  ]
  framework: string             # Which framework was used
  product_mention_tweet: number # Which tweet number introduces the product
  disclosure_tweet: number      # Which tweet has #ad
  suggested_hashtags: string[]  # 2-3 hashtags for the thread
  best_time_to_post: string     # Optimal posting time for X
  product_name: string
  content_angle: string
}
```

## Output Format

```
## Twitter Thread: [Product Name]

**Framework:** [Name]
**Angle:** [Content angle]
**Tweets:** [N] tweets

---

**Tweet 1 (Hook)** — [X chars]
[Tweet content]

---

**Tweet 2** — [X chars]
[Tweet content]

---

*...continue for all tweets...*

---

**Tweet [N] (CTA)** — [X chars]
[Tweet content including #ad disclosure]

---

**Pinned Reply** — [X chars]
[Suggested first reply to boost engagement]

---

### Posting Guide

| Detail | Value |
|--------|-------|
| Best time to post | [Day + time] |
| First action after posting | [Like all tweets to boost visibility, pin reply] |
| Expected engagement pattern | [What metrics to watch] |

### Alternate Hook Options

- **[Hook style 2]:** "[Alternative tweet 1]"
- **[Hook style 3]:** "[Alternative tweet 1]"
```

## Error Handling

- **No product info:** Pull `recommended_program` from S1 context if available.
  Otherwise ask what product they want to promote.
- **No personal experience:** Write research-based content. Flag that personal
  experience threads get 2-3x more engagement and suggest adding a real data point.
- **Thread feels too promotional too early:** Move product mention to tweet 6+.
  Add 1-2 more value tweets before the recommendation.
- **Content is too generic:** Use `web_search` to add specific stats, quotes, or
  examples. Replace every vague claim with a concrete number or example.
- **Tweet over 280 characters:** Auto-split or suggest cut. Never truncate — the
  full thought must fit in one tweet.
- **Creator has no X following:** Add note: "New accounts should engage in replies
  for 1-2 weeks before posting threads. Algorithm rewards accounts with engagement history."

## Examples

**Example 1:**
User: "Write a Twitter thread promoting ConvertKit to freelancers"
→ Angle: "How I built a 3,000-subscriber email list as a freelancer — what worked"
→ Framework: Numbers Story
→ 9 tweets: Hook (metrics) → 6 lessons → ConvertKit mention at tweet 6 → CTA + #ad
→ Emphasis: free plan, creator-friendly, no bloat

**Example 2:**
User: "I want to write a contrarian thread about email marketing tools"
→ Angle: "Most people pick the wrong email platform. Here's why:"
→ Framework: Contrarian Take
→ Myths to bust: "Mailchimp is fine for beginners", "you need fancy automations"
→ Natural product mention: "After trying 5 tools, I settled on ConvertKit because..."

**Example 3:**
User: "8-tweet thread about HeyGen for video creators"
→ Framework: How-to Tutorial — "How to create a talking-head video without a camera"
→ Step-by-step: sign up → upload script → pick avatar → generate → edit → export
→ Product mention woven in at step 1 (that's HeyGen)
→ CTA: "HeyGen has a free plan — I made my first 3 videos for free: [link] #ad"

## References

- `shared/references/ftc-compliance.md` — #ad placement rules for Twitter/X
- `shared/references/platform-rules.md` — X character limits, link handling, thread best practices
- `shared/references/affiliate-glossary.md` — terminology
```

## File: `skills/content/viral-post-writer/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/content/viral-post-writer/SKILL.md`
```markdown
---
name: viral-post-writer
description: >
  Write viral social media posts that promote affiliate products naturally.
  Use this skill when the user asks anything about writing social media content
  for affiliate marketing, creating posts for LinkedIn/X/Reddit/Facebook,
  promoting a product on social media, writing affiliate content, or mentions
  "viral post", "social media post", "content for affiliate".
  Also trigger for: "write a post about X", "help me promote X on LinkedIn",
  "create a thread about X", "make a Reddit post for X", "draft tweets for X",
  "social media content for affiliate program", "how to promote X on social",
  "write something that goes viral", "LinkedIn post for affiliate", "X thread
  about this tool", "help me sell X naturally on social media".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S2-Content
---

# Viral Post Writer

Write high-converting social media posts that promote affiliate products without feeling salesy. Each post uses proven viral frameworks, is tailored to the target platform, and includes proper FTC disclosure.

## Stage

This skill belongs to Stage S2: Content

## When to Use

- User wants to promote an affiliate product on social media
- User asks for LinkedIn posts, X/Twitter threads, Reddit posts, or Facebook posts
- User has picked a program (from S1 or manually) and needs content
- User wants "viral" or "engaging" social media content for affiliate marketing
- User asks how to naturally promote a product on a specific platform

## Input Schema

```
{
  product: {                  # (required) Product to promote — from S1 output or user-provided
    name: string              # "HeyGen"
    description: string       # What the product does (1-2 sentences)
    reward_value: string      # "30%" (for context — never shown in post)
    url: string               # Product website or affiliate link
  }
  platform: string            # (required) "linkedin" | "x" | "reddit" | "facebook" | "all"
  angle: string               # (optional, default: auto-selected) Content angle — see Viral Frameworks
  tone: string                # (optional, default: "conversational") "conversational" | "professional" | "casual" | "storytelling"
  audience: string            # (optional, default: inferred from platform) Target audience description
  personal_experience: string # (optional) User's real experience with the product — makes content authentic
  cta_style: string           # (optional, default: "soft") "soft" | "direct" | "question"
}
```

## Workflow

### Step 1: Gather Context

If not clear from conversation:
1. What product are they promoting? (Check if S1 ran earlier — use `recommended_program` from context)
2. Which platform? (If "all", generate for LinkedIn + X + Reddit)
3. Any personal experience with the product? (Authentic stories convert 3-5x better)

If user just says "write a post for HeyGen" → default to LinkedIn, conversational tone, soft CTA.

If product details are missing, use `web_search "[product name] features pricing"` to research.

### Step 2: Research the Product

Even if product info is provided, do a quick `web_search` to find:
- Recent product updates or launches (recency = virality)
- Common pain points the product solves (hook material)
- Competitor comparisons (contrast = engagement)
- Real user testimonials or reviews (social proof)

Extract 2-3 **specific details** — exact numbers, real features, concrete use cases. Generic "this tool is amazing" posts don't go viral.

### Step 3: Pick the Viral Framework

Select from `references/viral-frameworks.md` based on product + platform + angle.

If user specified an `angle`, use that framework. Otherwise, auto-select:

| Platform | Best Default Framework |
|----------|----------------------|
| LinkedIn | Transformation Story or Contrarian Take |
| X | Thread (Problem → Solution) or Hot Take |
| Reddit | Genuine Recommendation or Problem-Solve |
| Facebook | Before/After or Listicle |

### Step 4: Write the Post

Apply the selected framework from `references/viral-frameworks.md`.

**Critical rules:**
1. **Hook in first line** — reader decides in 1.5 seconds whether to keep reading
2. **Specific > generic** — "saved 4 hours/week on video editing" beats "great tool"
3. **Story > pitch** — wrap the recommendation in a narrative or discovery
4. **Platform-native format** — see `references/platform-specs.md` for formatting rules
5. **One CTA only** — don't overwhelm. One clear next step
6. **FTC compliance** — include disclosure per `shared/references/ftc-compliance.md` placement rules

**Never do:**
- Start with "I'm excited to share..." (LinkedIn death sentence)
- Use "game-changer", "revolutionary", "hands down the best" (empty superlatives)
- Put the link in the main post body on LinkedIn (algorithm penalty)
- Hard-sell in the first sentence
- Mention commission rates or that you're an affiliate (FTC requires disclosure, not details)
- Include "Powered by Affitor" branding (see `shared/references/affitor-branding.md`)

### Step 5: Add FTC Disclosure

Per platform (from `shared/references/ftc-compliance.md`):
- **LinkedIn:** "#ad | Affiliate link" at the end of the post body
- **X:** "#ad" in the tweet containing the link (usually last tweet in thread)
- **Reddit:** "Full disclosure: affiliate link" at the bottom
- **Facebook:** "#ad | Affiliate link" at the end

### Step 6: Format Output

Present the post ready to copy-paste. Include:
1. The post content (formatted for the platform)
2. Where to place the affiliate link
3. Best time to post (platform-specific)
4. 2-3 engagement tips for the specific platform

## Output Schema

Other skills can consume these fields from conversation context:

```
{
  posts: [
    {
      platform: string         # "linkedin" | "x" | "reddit" | "facebook"
      framework: string        # Which viral framework was used
      content: string          # The full post text, ready to copy-paste
      link_placement: string   # Where to put the affiliate link
      disclosure: string       # FTC disclosure text included
      hashtags: string[]       # Suggested hashtags (if applicable)
      best_time: string        # Best posting time for this platform
    }
  ]
  product_name: string         # For downstream skill chaining
  content_angle: string        # The angle used (for consistency across content)
}
```

## Output Format

```
## Viral Post: [Product Name] on [Platform]

**Framework:** [Name of viral framework used]
**Angle:** [The content angle]

---

### Post Content

[Full post text, formatted for the platform. Ready to copy-paste.]

---

### Posting Guide

| Detail | Value |
|--------|-------|
| Link placement | [Where to put the link] |
| Best time to post | [Platform-specific optimal time] |
| Expected engagement | [What metrics to watch] |

### Engagement Tips

1. [Tip specific to this platform + content type]
2. [Tip about responding to comments]
3. [Tip about amplifying reach]

### Variations

Want more options? Try these angles:
- **[Framework 2]:** [1-line preview of alternative approach]
- **[Framework 3]:** [1-line preview of alternative approach]
```

When platform = "all", generate separate sections for LinkedIn, X, and Reddit.

## Error Handling

- **No product info:** Ask the user what product they want to promote. Suggest running `affiliate-program-search` first.
- **Unknown platform:** Default to LinkedIn. Mention available platforms.
- **No personal experience:** Generate research-based content. Flag that personal stories convert better and suggest the user adds their own experience.
- **Product has no public info:** Use `web_search` to find product details. If truly nothing found, ask user to describe the product.
- **Controversial product:** If the product has significant negative reviews or ethical concerns, flag this to the user and suggest adjusting the angle.

## Examples

**Example 1:**
User: "Write a LinkedIn post promoting HeyGen"
→ Research HeyGen (AI video, 30% recurring, 60-day cookie)
→ Select "Transformation Story" framework for LinkedIn
→ Write: hook about video creation pain → discovered HeyGen → specific result → soft CTA
→ Link in first comment, FTC disclosure in post body

**Example 2:**
User: "Create an X thread about Semrush for SEO marketers"
→ Research Semrush features + recent updates
→ Select "Thread: Problem → Solution" framework
→ Write: 5-7 tweet thread, hook → pain points → how Semrush solves each → results → CTA in last tweet
→ FTC "#ad" in the tweet with the link

**Example 3:**
User: "I've been using Notion for 2 years, help me write a Reddit post"
→ Use personal experience as the core (authenticity = Reddit gold)
→ Select "Genuine Recommendation" framework
→ Write: problem context → how they discovered Notion → specific workflows → natural mention
→ "Full disclosure: affiliate link" at bottom
→ Recommend posting in r/productivity or r/Notion

**Example 4:**
User: "Promote GetResponse on all platforms"
→ Research GetResponse (email marketing, 33% recurring)
→ Generate 3 posts: LinkedIn (Transformation Story), X (Thread), Reddit (Genuine Recommendation)
→ Each tailored to platform format, audience, and link rules

## References

- `references/viral-frameworks.md` — the viral content frameworks with templates and examples
- `references/platform-specs.md` — character limits, formatting, optimal posting times per platform
- `shared/references/ftc-compliance.md` — FTC disclosure requirements and placement rules
- `shared/references/affitor-branding.md` — when to include/exclude Affitor branding (social = NO branding)
- `shared/references/affiliate-glossary.md` — affiliate marketing terminology
```

## File: `skills/content/viral-post-writer/agents/openai.yaml`
```yaml
name: viral-post-writer
description: Write viral social media posts that promote affiliate products naturally
instructions_file: ../SKILL.md
tools:
  - web_search
  - web_browse
```

## File: `skills/content/viral-post-writer/references/platform-specs.md`
```markdown
# Platform Specifications for Affiliate Posts

Quick reference for character limits, formatting, link behavior, and optimal posting times.

## LinkedIn

| Spec | Value |
|------|-------|
| Character limit | 3,000 (post body) |
| Ideal length | 800-1,500 characters (short enough to read, long enough for depth) |
| Line breaks | Double-enter for spacing. LinkedIn collapses single line breaks |
| Link behavior | External links in post body = algorithm penalty (~40% less reach). Put links in first comment |
| Hashtags | 3-5 max. Place at the end. Use niche hashtags (50K-500K followers), not generic ones |
| Images | Posts with images get 2x engagement. Carousel posts get 3x |
| Best time | Tue-Thu, 8-10am local time (target audience timezone) |
| Hook cutoff | First ~210 characters show before "...see more". Hook MUST be in this window |

### LinkedIn Formatting Tips
- Use arrows (→), bullets (•), and line breaks for scanability
- Emojis: 1-2 per post max. Never emoji-heavy
- Bold not supported in post body — use CAPS sparingly for emphasis
- Tag relevant people or companies (but only if genuinely relevant)
- First comment with link should be posted immediately (within 30 seconds)

---

## X (Twitter)

| Spec | Value |
|------|-------|
| Character limit | 280 per tweet (threads = unlimited) |
| Thread length | 5-10 tweets optimal. More than 12 loses readers |
| Link behavior | Links don't penalize reach (unlike LinkedIn). Include in-tweet |
| Images | 1 image = significant engagement boost. Screenshots of the product work well |
| Hashtags | 1-2 max. Many X power users use zero hashtags |
| Best time | Mon-Fri, 9-11am EST or 1-3pm EST |
| Hook cutoff | Full 280 chars visible. First tweet is make-or-break |

### X Formatting Tips
- Thread format: number tweets (1/, 2/, etc.) or use 🧵 emoji on first tweet
- Each tweet should standalone — some people see individual tweets, not the full thread
- Last tweet = CTA + link + #ad disclosure
- Quote-tweet your own thread to boost it later
- Reply to your own thread with additional context (algorithm treats it as engagement)

---

## Reddit

| Spec | Value |
|------|-------|
| Character limit | 40,000 (text post) |
| Ideal length | 300-800 words for recommendation posts |
| Link behavior | Self-post (text) preferred over link posts for recommendations. Link in body is fine |
| Formatting | Markdown supported. Use headers, bullets, bold. Well-formatted posts get more upvotes |
| Best time | Mon-Wed, 6-9am EST (early risers + Europe) |
| Disclosure | "Full disclosure: affiliate link" at the bottom. Clear and honest |

### Reddit Critical Rules
- **Check subreddit rules FIRST** — many ban affiliate links or self-promotion
- **Account age matters** — posts from new accounts get auto-removed in most subreddits
- **Never lead with the product** — lead with the problem or story
- **Include cons** — Reddit users will call out one-sided reviews instantly
- **Engage in comments** — Reddit rewards active participation in your own thread
- **Good subreddits for affiliate content:** r/[product-category], r/SaaS, r/startups, r/Entrepreneur, r/marketing, r/affiliatemarketing
- **Avoid:** r/technology, r/programming (strict anti-promotion rules)

### Reddit Post Structure
```
Title: [Question or problem statement — NOT the product name]

Body:
[Context — why you needed a solution]
[What you tried]
[How you found this product]
[Honest review with pros AND cons]
[Who it's best for]
[Link + disclosure]
```

---

## Facebook

| Spec | Value |
|------|-------|
| Character limit | 63,206 (practically unlimited) |
| Ideal length | 300-700 characters (short posts get more engagement) |
| Link behavior | Facebook suppresses posts with links. Use "link in comments" strategy |
| Images | Posts with images get 2.3x more engagement. Native video gets 6x |
| Best time | Wed-Fri, 11am-1pm local time |
| Groups | Group posts get 5x more reach than page posts. Join relevant groups |

### Facebook Tips
- Facebook Groups > Facebook Pages for affiliate content
- "Link in comments" works same as LinkedIn — post link immediately
- Ask a question at the end to drive comments (comments = reach)
- Personal stories perform best on Facebook (it's a "friends" platform)
- Avoid looking like an ad — Facebook users scroll past anything that looks promotional

---

## Cross-Platform Best Practices

### Hook Patterns That Work Everywhere

| Pattern | Example |
|---------|---------|
| Specific number | "I cut my video editing time from 6 hours to 45 minutes" |
| Contrarian | "Stop using [popular tool] for [task]" |
| Question | "Why are [audience] still [painful process]?" |
| Before/After | "Before: 3 hours editing. After: 20 minutes" |
| Curiosity gap | "I found something that changed how I [task]" |
| Social proof | "10,000 marketers are already using this" |

### Universal Don'ts

1. Never use "game-changer", "revolutionary", "hands down the best"
2. Never start with "I'm excited to share..."
3. Never mention your commission or that you're "an affiliate partner"
4. Never post the same content across all platforms (tailor each)
5. Never use more than 5 hashtags on any platform
6. Never hard-sell in the first sentence — earn attention first

### Engagement Multipliers

- **Respond to every comment** in the first 2 hours (algorithm reward)
- **Ask a question** at the end of every post (2-3x more comments)
- **Post consistently** — 3x/week minimum on any platform
- **Repurpose, don't copy** — same angle, different format per platform
```

## File: `skills/content/viral-post-writer/references/viral-frameworks.md`
```markdown
# Viral Content Frameworks for Affiliate Marketing

Proven frameworks that drive engagement and conversions on social media. Each framework includes the structure, when to use it, and a template.

## 1. Transformation Story

**Best for:** LinkedIn, Facebook
**When:** You or the user has personal experience with the product. Works for tools that save time, money, or effort.

**Structure:**
1. Hook: state the "before" pain (specific, relatable)
2. Turning point: how you discovered the product
3. Transformation: specific results with numbers
4. Reflection: what you learned
5. Soft CTA: invite curiosity, don't hard-sell

**Template:**
```
[Specific pain point — something the audience feels daily]

I spent [X hours/dollars] on [old way of doing things].

Then [how you found the product — a friend mentioned it, saw a post, stumbled on it].

In [timeframe], I [specific result with numbers]:
→ [Result 1 with metric]
→ [Result 2 with metric]
→ [Result 3 with metric]

The biggest surprise? [Unexpected benefit].

If you [do the thing the product helps with], [product name] is worth checking out.

[Link in the comments / check my bio]

#ad | Affiliate link — I may earn a commission if you sign up.
```

**Why it works:** Stories activate the brain's narrative processing. Specific numbers create credibility. The "discovery" moment makes it feel like a recommendation from a friend, not an ad.

---

## 2. Contrarian Take

**Best for:** LinkedIn, X
**When:** You can challenge a popular belief about the product's category. Works when the product does something differently.

**Structure:**
1. Hook: bold, disagreeable statement about the category
2. Common wisdom: what most people believe
3. Counter-evidence: why the common belief is wrong
4. The alternative: naturally introduce the product
5. Proof: specific example or data
6. Invitation: ask for opinions (drives comments)

**Template:**
```
[Bold statement that challenges conventional wisdom]

Most [role] think [common belief about category].

Here's why that's costing them [time/money/results]:

[2-3 points explaining why the old way is broken]

I switched to [product] because [specific reason].

Result: [specific outcome with numbers]

The old way: [painful process]
The new way: [streamlined process with product]

Agree or disagree? I'd love to hear your take.
```

**Why it works:** Disagreement is the #1 driver of comments on LinkedIn. Comments = algorithm boost = reach. The product introduction feels like evidence for your argument, not a pitch.

---

## 3. Problem → Solution Thread

**Best for:** X (Twitter threads)
**When:** The product solves a well-known problem. Good for technical or multi-feature products.

**Structure:**
1. Tweet 1 (hook): State the problem + promise a solution
2. Tweets 2-4: Break down the problem (pain amplification)
3. Tweets 5-7: Show how the product solves each pain
4. Tweet 8: Results/social proof
5. Tweet 9: CTA + link + disclosure

**Template:**
```
Tweet 1:
[Problem statement] is costing [audience] [time/money].

I found a fix. Here's the breakdown: 🧵

Tweet 2:
Problem #1: [Specific pain point]

[1-2 sentences explaining why this hurts]

Tweet 3:
Problem #2: [Second pain point]

[1-2 sentences]

Tweet 4:
Problem #3: [Third pain point]

[1-2 sentences]

Tweet 5:
Here's what I switched to: [Product name]

[What it does in 1 sentence]

Tweet 6:
For Problem #1 → [How product solves it]

[Optional: screenshot or visual description]

Tweet 7:
For Problem #2 → [How product solves it]

For Problem #3 → [How product solves it]

Tweet 8:
Results after [timeframe]:
• [Metric 1]
• [Metric 2]
• [Metric 3]

Tweet 9:
Try it here: [link]

#ad
```

**Why it works:** Threads get 3-5x more engagement than single tweets. Each tweet in the thread is a mini-hook. The problem-first structure makes readers nod along before the solution appears.

---

## 4. Hot Take

**Best for:** X, LinkedIn
**When:** You have a strong opinion about the category. Works when the product represents a trend or shift.

**Structure:**
1. Hook: provocative 1-liner
2. Expansion: 2-3 sentences explaining the take
3. Evidence: why you believe this
4. Product mention: natural tie-in
5. Question: invite debate

**Template:**
```
[Provocative statement about the industry/category]

[2-3 sentences expanding on why this matters]

[Evidence: a trend, a stat, or personal observation]

That's why I've been using [product] — it [specific value prop that supports the take].

What's your take? [Question that invites responses]

#ad
```

**Why it works:** Hot takes polarize — people either agree loudly or disagree loudly. Both drive engagement. The product mention is subordinate to the opinion, so it doesn't feel promotional.

---

## 5. Genuine Recommendation

**Best for:** Reddit, Facebook groups
**When:** Authenticity is critical. Reddit especially punishes anything that feels like marketing.

**Structure:**
1. Context: why you were looking for a solution (relatable setup)
2. Journey: what you tried before (builds credibility)
3. Discovery: how you found this product
4. Honest review: pros AND cons (critical for Reddit)
5. Verdict: who it's best for
6. Link: natural placement with disclosure

**Template:**
```
[Context: I've been [doing X] for [timeframe] and [specific problem]]

I've tried [Alternative 1] — [brief honest opinion].
I've tried [Alternative 2] — [brief honest opinion].

Recently switched to [Product] and wanted to share my experience after [timeframe of use].

What I like:
- [Pro 1 — specific]
- [Pro 2 — specific]
- [Pro 3 — specific]

What could be better:
- [Con 1 — honest]
- [Con 2 — honest]

Best for: [Specific use case or user type]
Not great for: [Who shouldn't use it]

If anyone's curious: [link]

Full disclosure: affiliate link
```

**Why it works:** Reddit detects and punishes inauthentic content. Including cons builds trust. The "journey" establishes you as a real user, not a shill. This format regularly hits the top of subreddits.

---

## 6. Before/After

**Best for:** LinkedIn, Facebook, X
**When:** The product has a measurable impact. Great for productivity tools, design tools, video tools.

**Structure:**
1. Hook: the contrast (before = pain, after = gain)
2. Before details: what life looked like
3. The switch: 1 sentence introducing the product
4. After details: specific improvements
5. CTA: curiosity-driven

**Template:**
```
Before [product]: [painful reality in 1 line]
After [product]: [improved reality in 1 line]

Here's what changed:

BEFORE:
→ [Painful step 1]
→ [Painful step 2]
→ [Painful step 3]
→ Time spent: [X hours/week]

AFTER:
→ [Improved step 1]
→ [Improved step 2]
→ [Improved step 3]
→ Time spent: [Y hours/week]

That's [X-Y] hours/week I got back.

[Soft CTA — "Link in comments if you want to try it"]

#ad | Affiliate link
```

**Why it works:** Contrast is one of the most powerful persuasion tools. The side-by-side format makes the value immediately visible. Numbers make it concrete and believable.

---

## 7. Listicle / Tool Stack

**Best for:** X threads, LinkedIn
**When:** Promoting a product as part of a curated list. Lower pressure, higher reach.

**Structure:**
1. Hook: "X tools I use for [goal]"
2. List: 5-7 tools (the affiliate product is #1 or #2)
3. For each: name + 1-line value prop
4. CTA: "Which ones do you use?"

**Template:**
```
[X] tools I use daily for [goal]:

1. [Product name] — [1-line value prop] ← (the affiliate product)
2. [Tool 2] — [1-line value prop]
3. [Tool 3] — [1-line value prop]
4. [Tool 4] — [1-line value prop]
5. [Tool 5] — [1-line value prop]

#1 has been the biggest [time/money] saver for me.

What's in your stack? Anything I'm missing?

[Link to #1 in comments]

#ad | Affiliate link for [product]
```

**Why it works:** Lists get saved and shared. Putting the affiliate product at #1 feels natural in a list context. The "what do you use?" question drives high engagement in comments.

---

## Choosing the Right Framework

| Situation | Recommended Framework |
|-----------|----------------------|
| User has personal experience | Transformation Story or Genuine Recommendation |
| Product challenges status quo | Contrarian Take or Hot Take |
| Product is technical/multi-feature | Problem → Solution Thread |
| Product has measurable ROI | Before/After |
| Promoting alongside other tools | Listicle / Tool Stack |
| Posting on Reddit | Genuine Recommendation (always) |
| Want maximum comments | Contrarian Take or Hot Take |
| Want maximum saves/shares | Listicle or Before/After |
```

## File: `skills/distribution/bio-link-deployer/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/distribution/bio-link-deployer/SKILL.md`
```markdown
---
name: bio-link-deployer
description: >
  Create a Linktree-style bio link hub page as a single self-contained HTML file.
  Triggers on: "create a bio link page", "make a linktree", "link in bio page",
  "bio link", "link hub", "create my link page", "all my links on one page",
  "linktree alternative", "build a link page", "bio page for my affiliate links",
  "I need a link in bio", "make a page with all my links", "link aggregator page".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S5-Distribution
---

# Bio Link Deployer

Create a Linktree-style hub page that links all your affiliate content — blog posts, landing pages, social profiles, and product links — in one place. Output is a single self-contained HTML file with 3 theme options, mobile-first (90%+ bio link traffic is mobile), deployable anywhere.

## Stage

S5: Distribution — The central hub that ties your entire affiliate funnel together. Put this link in your social media bios, email signatures, and anywhere you need one link to rule them all. Unlike Linktree, you own the page and pay nothing.

## When to Use

- User wants a link-in-bio page for social media profiles
- User wants a single page linking all their affiliate content
- User says anything like "linktree", "bio link", "link page", "link in bio", "all my links"
- User has multiple affiliate products/blog posts/landing pages and needs a hub
- User wants a free alternative to Linktree/Beacons/Stan Store

## Input Schema

```yaml
user_name: string           # REQUIRED — display name or handle (e.g., "@alexcreator")

tagline: string             # OPTIONAL — short bio under the name
                            # Default: auto-generated from link categories

avatar_url: string          # OPTIONAL — URL to profile image
                            # Default: emoji placeholder based on niche

links:                      # REQUIRED — at least 3 links
  - label: string           # Display text (e.g., "HeyGen — AI Video Creator")
    url: string             # Destination URL
    category: string        # Group label (e.g., "Tools", "My Content", "Connect")
    icon: string            # OPTIONAL — emoji for visual (e.g., "🎬")

theme: string               # OPTIONAL — "minimal" | "dark" | "gradient"
                            # Default: "minimal"
```

**Chaining context**: If earlier skills (S1-S4) were run in the conversation:
- Products from S1 → add as "Featured Tools" links
- Blog posts from S3 → add as "My Content" links
- Landing pages from S4 → add as "Featured Tools" or "Landing Pages" links
- Social posts from S2 → link to the social platform profiles

If the user says "make me a bio link with everything we've done" — gather all products, blog posts, and landing pages from the conversation and organize them into categories.

## Workflow

### Step 1: Gather Links

Collect links from one of these sources:

**Option A — User provides links directly:**
Use the `links` array as-is. Ensure each link has a label, url, and category.

**Option B — Gather from conversation context:**
If prior skills (S1-S4) were run, collect:
- Product affiliate URLs → category: "Featured Tools"
- Blog post URLs → category: "My Content"
- Landing page URLs → category: "Landing Pages"
- Social media profiles (if mentioned) → category: "Connect"

**Option C — User provides partial info:**
Ask for missing required fields. Minimum: user_name + 3 links.

Organize links by category. Suggested category order:
1. "Featured Tools" (affiliate product links — money links first)
2. "My Content" (blog posts, landing pages, videos)
3. "Connect" (social media, email, website)

### Step 2: Build Page

Read `templates/bio-link.html` for the page structure and all three theme variants.

Apply the chosen `theme`:

**Minimal (default):**
- Clean white background, subtle borders
- Dark text, light gray accents
- Rounded corners (12px)
- Best for: professional, clean look

**Dark:**
- Dark navy background (#0f172a)
- Light text, blue accents
- Subtle card borders
- Best for: tech, gaming, modern brands

**Gradient:**
- Purple-to-blue gradient background
- White text, frosted-glass link cards
- Large rounded corners (24px)
- Best for: creative, lifestyle, bold brands

Set CSS variables in `:root` based on the chosen theme. Remove the other theme blocks from the template.

If `avatar_url` is provided, use an `<img>` tag. Otherwise, use the emoji placeholder div with an emoji matching the user's niche (default: 🚀).

### Step 3: Output

Present the final output in this structure:

**Part 1: Page Summary**
```
---
BIO LINK PAGE
---
Name: [user_name]
Theme: [minimal/dark/gradient]
Links: [count]
Categories: [list]
---
```

**Part 2: Complete HTML**
The full HTML file in a fenced code block (```html). Save as `index.html` (or `links.html`) and open in any browser.

**Part 3: Deploy Instructions**
Read `references/domain-setup.md` and provide the deploy options:
```
---
DEPLOY
---
1. Save as `index.html`
2. Preview: open the file in your browser
3. Deploy (pick one):
   - Netlify Drop: drag the file to https://app.netlify.com/drop (30 seconds)
   - Vercel: `npx vercel deploy --prod` (needs Node.js)
   - GitHub Pages: push to repo → Settings → Pages → main branch
4. Add to your social bios: paste the URL in your Instagram, X, TikTok, LinkedIn bio
5. Custom domain: see references/domain-setup.md for DNS setup guide
---
```

## Output Schema

```yaml
bio_link:
  user_name: string         # Display name
  theme: string             # Applied theme
  html: string              # Complete self-contained HTML
  filename: string          # Suggested filename (e.g., "index.html")
  link_count: number        # Total links on the page
  categories: string[]      # Categories used

deploy:
  local: string             # "Open index.html in browser"
  netlify: string           # Netlify Drop instructions
  vercel: string            # Vercel deploy command
  github_pages: string      # GitHub Pages instructions
```

## Output Format

Present the output as three clearly separated sections:
1. **Page Summary** — name, theme, link count, categories
2. **HTML** — the complete file in a code block, ready to save
3. **Deploy Instructions** — how to get the page live and add to social bios

The HTML should be **immediately usable** — save as `.html`, open in browser, and it works. No build step, no dependencies, mobile-optimized.

## Error Handling

- **No links provided**: "I need at least 3 links to create your bio page. List your affiliate product URLs, blog posts, social profiles, or landing pages."
- **No user_name**: "What name or handle should I display? (e.g., @yourusername)"
- **Invalid avatar_url**: Use emoji placeholder instead. Note: "I couldn't load the avatar image, so I used an emoji placeholder. You can replace it later by editing the HTML."
- **Unknown theme**: Default to minimal. Inform: "I used the 'minimal' theme. Available themes: minimal, dark, gradient."
- **Too many links (20+)**: Include all but suggest: "That's a lot of links — consider featuring your top 10-15 and linking to a full directory page for the rest."
- **No categories provided**: Auto-categorize based on URL patterns (social domains → "Connect", blog URLs → "My Content", product URLs → "Tools").

## Examples

### Example 1: Full Input
**User**: "Create a dark-themed bio link page for @sarahcontent with these links: HeyGen (heygen.com/ref), Semrush (semrush.com/ref), My HeyGen Review (blog.com/heygen), Follow on X (x.com/sarah)"
**Action**: theme=dark, organize into 3 categories (Tools, Content, Connect), generate HTML.

### Example 2: From Conversation Context
**User**: "Make me a bio link page with everything we've done today"
**Context**: S1 found HeyGen, S3 wrote a blog post, S4 made a landing page
**Action**: Gather all URLs from conversation, auto-categorize, default theme=minimal, generate HTML.

### Example 3: Minimal Input
**User**: "I need a link in bio page"
**Action**: Ask for user_name and links. Provide example: "What's your display name and what links do you want? For example: product URLs, blog posts, social profiles."

## References

- `templates/bio-link.html` — Bio link page template with 3 theme variants (minimal, dark, gradient). Read in Step 2.
- `references/domain-setup.md` — Hosting and domain setup guide for Netlify Drop, Vercel, GitHub Pages. Read in Step 3.
- `shared/references/ftc-compliance.md` — FTC disclosure for bio link pages (footer text). Reference in Step 2.
- `shared/references/affitor-branding.md` — Affitor footer HTML. Reference in Step 2.
```

## File: `skills/distribution/bio-link-deployer/agents/openai.yaml`
```yaml
name: bio-link-deployer
description: Create a Linktree-style bio link hub page as a single self-contained HTML file — link all your affiliate content in one place
instructions_file: ../SKILL.md
tools:
  - web_search
```

## File: `skills/distribution/bio-link-deployer/references/domain-setup.md`
```markdown
# Domain & Hosting Setup Guide

## Quick Deploy Options

### Option 1: Netlify Drop (Easiest — 30 seconds)

1. Go to https://app.netlify.com/drop
2. Drag your `.html` file onto the page
3. Done — you get a URL like `random-name-123.netlify.app`
4. Optional: sign up to claim a custom subdomain (`yourname.netlify.app`)

**Custom domain on Netlify:**
1. Sign up at netlify.com (free tier is fine)
2. Go to Site Settings → Domain Management → Add custom domain
3. Enter your domain (e.g., `links.yourdomain.com`)
4. Add the DNS records Netlify provides:
   - CNAME: `links` → `your-site.netlify.app`
   - Or: A record → Netlify's load balancer IP
5. Enable HTTPS (automatic via Let's Encrypt)

### Option 2: Vercel (Developer-friendly)

1. Install Vercel CLI: `npm i -g vercel`
2. Create a directory with your `.html` file
3. Run: `npx vercel deploy --prod`
4. Follow the prompts — you get a URL like `your-project.vercel.app`

**Custom domain on Vercel:**
1. Go to your project dashboard → Settings → Domains
2. Add your domain
3. Add DNS records as instructed (CNAME or nameserver delegation)
4. HTTPS is automatic

### Option 3: GitHub Pages (Free, version-controlled)

1. Create a new GitHub repository (can be private with Pages on free tier)
2. Add your `.html` file as `index.html`
3. Go to Settings → Pages → Source: "Deploy from a branch" → `main` → `/ (root)`
4. Your site is live at `username.github.io/repo-name`

**Custom domain on GitHub Pages:**
1. In repo Settings → Pages → Custom domain, enter your domain
2. Add DNS records:
   - CNAME: `links` → `username.github.io`
   - Or A records: GitHub's IPs (185.199.108-111.153)
3. Check "Enforce HTTPS"
4. Add a `CNAME` file to the repo root with your domain name

### Option 4: Local Only (Preview)

Just double-click the `.html` file — it opens in your default browser. No server needed since it's a self-contained file.

## Domain Recommendations

For a bio link page, use a short, memorable subdomain:

- `links.yourdomain.com` — professional, branded
- `go.yourdomain.com` — short and clean
- `bio.yourdomain.com` — obvious purpose

If you don't have a domain, free options:
- `yourname.netlify.app` (Netlify)
- `yourname.vercel.app` (Vercel)
- `username.github.io/links` (GitHub Pages)

## DNS Basics

If you're new to DNS, here's what you need to know:

- **A record**: Points a domain to an IP address. Use for root domains (`yourdomain.com`).
- **CNAME record**: Points a subdomain to another domain. Use for subdomains (`links.yourdomain.com`).
- **TTL**: How long DNS records are cached. Set to 300 (5 minutes) while testing, 3600 (1 hour) when stable.
- **Propagation**: DNS changes take 1-48 hours to spread globally. Usually under 30 minutes.

Common domain registrars: Namecheap, Cloudflare, Google Domains, Porkbun.

## SSL/HTTPS

All three hosting options (Netlify, Vercel, GitHub Pages) provide free automatic HTTPS via Let's Encrypt. No configuration needed — just add your domain and wait a few minutes.

**Important**: Always use `https://` links in your bio page. Mixed content (HTTP on an HTTPS page) will cause browser warnings.
```

## File: `skills/distribution/bio-link-deployer/templates/bio-link.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>@alexcreator — Tools & Resources I Recommend</title>
  <meta name="description" content="Curated tools, resources, and content from @alexcreator. Find the best AI, productivity, and marketing tools.">
  <style>
    /* ================================================================
       BIO LINK PAGE — 3 Theme Variants
       AI: Choose one theme block and delete the other two.
       Set the active theme's variables in :root.
       ================================================================ */

    /* --- THEME: MINIMAL (default) --- */
    /*
    :root {
      --color-primary: #1e293b;
      --color-primary-hover: #0f172a;
      --color-bg: #ffffff;
      --color-surface: #f8fafc;
      --color-text: #1e293b;
      --color-text-light: #64748b;
      --color-border: #e2e8f0;
      --color-link-bg: #ffffff;
      --color-link-border: #e2e8f0;
      --color-link-hover: #f1f5f9;
      --avatar-border: #e2e8f0;
      --radius: 12px;
    }
    */

    /* --- THEME: DARK --- */
    /*
    :root {
      --color-primary: #3b82f6;
      --color-primary-hover: #60a5fa;
      --color-bg: #0f172a;
      --color-surface: #1e293b;
      --color-text: #f1f5f9;
      --color-text-light: #94a3b8;
      --color-border: #334155;
      --color-link-bg: #1e293b;
      --color-link-border: #334155;
      --color-link-hover: #334155;
      --avatar-border: #334155;
      --radius: 12px;
    }
    */

    /* --- THEME: GRADIENT --- */
    /*
    :root {
      --color-primary: #ffffff;
      --color-primary-hover: #f0f0f0;
      --color-bg: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      --color-surface: rgba(255,255,255,0.1);
      --color-text: #ffffff;
      --color-text-light: rgba(255,255,255,0.75);
      --color-border: rgba(255,255,255,0.2);
      --color-link-bg: rgba(255,255,255,0.15);
      --color-link-border: rgba(255,255,255,0.2);
      --color-link-hover: rgba(255,255,255,0.25);
      --avatar-border: rgba(255,255,255,0.3);
      --radius: 24px;
    }
    */

    /* === ACTIVE THEME — AI: set the chosen theme's values here === */
    :root {
      --color-primary: #1e293b;
      --color-primary-hover: #0f172a;
      --color-bg: #ffffff;
      --color-surface: #f8fafc;
      --color-text: #1e293b;
      --color-text-light: #64748b;
      --color-border: #e2e8f0;
      --color-link-bg: #ffffff;
      --color-link-border: #e2e8f0;
      --color-link-hover: #f1f5f9;
      --avatar-border: #e2e8f0;
      --radius: 12px;
    }

    /* === RESET & BASE === */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--color-text);
      background: var(--color-bg);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      -webkit-font-smoothing: antialiased;
    }
    a { color: inherit; text-decoration: none; }

    /* === MAIN CONTAINER === */
    .bio-container {
      width: 100%;
      max-width: 480px;
      padding: 48px 20px 32px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    /* === AVATAR === */
    .avatar {
      width: 96px;
      height: 96px;
      border-radius: 50%;
      border: 3px solid var(--avatar-border);
      object-fit: cover;
      margin-bottom: 16px;
    }
    .avatar-placeholder {
      width: 96px;
      height: 96px;
      border-radius: 50%;
      border: 3px solid var(--avatar-border);
      background: var(--color-surface);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 40px;
      margin-bottom: 16px;
    }

    /* === PROFILE INFO === */
    .profile-name {
      font-size: 22px;
      font-weight: 700;
      margin-bottom: 4px;
      text-align: center;
    }
    .profile-tagline {
      font-size: 15px;
      color: var(--color-text-light);
      text-align: center;
      margin-bottom: 32px;
      line-height: 1.4;
      max-width: 360px;
    }

    /* === CATEGORY LABEL === */
    .category-label {
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--color-text-light);
      margin-bottom: 12px;
      margin-top: 8px;
      width: 100%;
      text-align: left;
      padding-left: 4px;
    }

    /* === LINK BUTTON === */
    .link-list {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .link-item {
      display: flex;
      align-items: center;
      gap: 12px;
      width: 100%;
      padding: 14px 20px;
      background: var(--color-link-bg);
      border: 1px solid var(--color-link-border);
      border-radius: var(--radius);
      transition: background 0.15s, transform 0.1s;
      cursor: pointer;
    }
    .link-item:hover {
      background: var(--color-link-hover);
      transform: translateY(-1px);
    }
    .link-item:active {
      transform: translateY(0);
    }
    .link-icon {
      font-size: 20px;
      flex-shrink: 0;
    }
    .link-label {
      font-size: 15px;
      font-weight: 500;
      flex-grow: 1;
    }
    .link-arrow {
      font-size: 14px;
      color: var(--color-text-light);
      flex-shrink: 0;
    }

    /* === SPACER === */
    .spacer { height: 16px; }

    /* === FOOTER === */
    .bio-footer {
      margin-top: 40px;
      text-align: center;
      font-size: 12px;
      color: var(--color-text-light);
      line-height: 1.6;
    }
    .bio-footer a {
      color: #155DFC;
    }
    .disclosure-text {
      font-size: 11px;
      color: var(--color-text-light);
      margin-bottom: 8px;
      max-width: 360px;
    }

    /* === MOBILE OPTIMIZATIONS === */
    @media (max-width: 480px) {
      .bio-container { padding: 32px 16px 24px; }
      .link-item { padding: 14px 16px; }
    }

    /* Ensure full height on mobile browsers */
    @supports (-webkit-touch-callout: none) {
      body { min-height: -webkit-fill-available; }
    }
  </style>
</head>
<body>

  <div class="bio-container">

    <!-- AVATAR — AI: replace with user's avatar_url or use placeholder -->
    <!-- Option A: Image avatar -->
    <!-- <img class="avatar" src="https://example.com/avatar.jpg" alt="Alex Creator"> -->
    <!-- Option B: Emoji/initial placeholder (use when no avatar_url provided) -->
    <div class="avatar-placeholder">🚀</div>

    <!-- PROFILE INFO -->
    <h1 class="profile-name">@alexcreator</h1>
    <p class="profile-tagline">AI tools enthusiast. Sharing the best products I use to create content faster and earn affiliate income.</p>

    <!-- LINKS BY CATEGORY -->

    <!-- Category: Featured Tools -->
    <div class="category-label">Featured Tools</div>
    <div class="link-list">
      <a href="https://www.heygen.com/?ref=YOUR_ID" target="_blank" rel="noopener" class="link-item">
        <span class="link-icon">🎬</span>
        <span class="link-label">HeyGen — AI Video Creator</span>
        <span class="link-arrow">→</span>
      </a>
      <a href="https://www.semrush.com/?ref=YOUR_ID" target="_blank" rel="noopener" class="link-item">
        <span class="link-icon">🔍</span>
        <span class="link-label">Semrush — SEO & Marketing</span>
        <span class="link-arrow">→</span>
      </a>
      <a href="https://www.jasper.ai/?ref=YOUR_ID" target="_blank" rel="noopener" class="link-item">
        <span class="link-icon">✍️</span>
        <span class="link-label">Jasper — AI Writing Assistant</span>
        <span class="link-arrow">→</span>
      </a>
    </div>

    <div class="spacer"></div>

    <!-- Category: My Content -->
    <div class="category-label">My Content</div>
    <div class="link-list">
      <a href="https://yourblog.com/best-ai-video-tools" target="_blank" rel="noopener" class="link-item">
        <span class="link-icon">📝</span>
        <span class="link-label">Best AI Video Tools (2026)</span>
        <span class="link-arrow">→</span>
      </a>
      <a href="https://yourblog.com/heygen-review" target="_blank" rel="noopener" class="link-item">
        <span class="link-icon">⭐</span>
        <span class="link-label">My HeyGen Review</span>
        <span class="link-arrow">→</span>
      </a>
    </div>

    <div class="spacer"></div>

    <!-- Category: Connect -->
    <div class="category-label">Connect</div>
    <div class="link-list">
      <a href="https://twitter.com/alexcreator" target="_blank" rel="noopener" class="link-item">
        <span class="link-icon">𝕏</span>
        <span class="link-label">Follow me on X</span>
        <span class="link-arrow">→</span>
      </a>
      <a href="https://youtube.com/@alexcreator" target="_blank" rel="noopener" class="link-item">
        <span class="link-icon">▶️</span>
        <span class="link-label">YouTube Channel</span>
        <span class="link-arrow">→</span>
      </a>
      <a href="mailto:alex@example.com" class="link-item">
        <span class="link-icon">✉️</span>
        <span class="link-label">Email Me</span>
        <span class="link-arrow">→</span>
      </a>
    </div>

    <!-- FOOTER — FTC disclosure + Affitor branding -->
    <div class="bio-footer">
      <p class="disclosure-text">Some links on this page are affiliate links. I may earn a commission if you purchase through them, at no extra cost to you.</p>
      <p>Built with <a href="https://list.affitor.com">Affiliate Skills by Affitor</a></p>
    </div>

  </div>

</body>
</html>
```

## File: `skills/distribution/email-drip-sequence/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/distribution/email-drip-sequence/SKILL.md`
```markdown
---
name: email-drip-sequence
description: >
  Write an email drip sequence for affiliate marketing. Triggers on:
  "write me an email sequence", "create a drip campaign", "email nurture sequence",
  "affiliate email funnel", "welcome email series", "email onboarding sequence",
  "write emails for my list", "set up a drip sequence", "email campaign for [product]",
  "nurture my subscribers", "email follow-up sequence", "build my email funnel",
  "write 5 emails promoting [product]", "email automation sequence".
---

# Email Drip Sequence

Write a 5-7 email drip sequence that nurtures new subscribers from cold to warm to buyer. Follows the Welcome → Value → Value → Soft Sell → Hard Sell → Objection Handling → Follow-Up pattern. Each email includes subject line, preview text, body copy, and a single clear CTA.

## Stage

S5: Distribution — Email is the highest-ROI channel for affiliate marketers (avg $42 return per $1 spent). This skill turns a list of subscribers into a predictable revenue stream by delivering value first and selling second.

## When to Use

- User has an email list and wants to promote an affiliate product
- User just launched a lead magnet or opt-in form and needs a welcome sequence
- User wants to automate affiliate promotions via email automation (ConvertKit, Mailchimp, Beehiiv, ActiveCampaign, etc.)
- User says anything like "email sequence", "drip campaign", "email funnel", "nurture series"
- User wants a sequence for a specific product or niche
- Chaining from S1 (research) — user found a product and now wants an email sequence for it

## Input Schema

```yaml
product:
  name: string              # REQUIRED — product name (e.g., "HeyGen")
  affiliate_url: string     # REQUIRED — the affiliate link to promote
  category: string          # OPTIONAL — product category (e.g., "AI video tool")
  reward_value: string      # OPTIONAL — commission amount/percentage (e.g., "30% recurring")
  key_benefits: string[]    # OPTIONAL — top 3 benefits. Auto-researched if not provided.
  price: string             # OPTIONAL — product pricing (e.g., "$29/mo")

audience:
  description: string       # REQUIRED — who are the subscribers? (e.g., "content creators", "SaaS founders")
  pain_point: string        # OPTIONAL — main problem they want solved
  awareness_level: string   # OPTIONAL — "cold" | "warm" | "hot". Default: "cold"

sequence:
  length: number            # OPTIONAL — number of emails: 5, 6, or 7. Default: 7
  send_days: number[]       # OPTIONAL — days to send (e.g., [0, 1, 3, 5, 7, 10, 14])
                            # Default: [0, 1, 3, 5, 7, 10, 14]
  sender_name: string       # OPTIONAL — from name (e.g., "Alex from ContentPro")
  tone: string              # OPTIONAL — "conversational" | "professional" | "bold"
                            # Default: "conversational"
  lead_magnet: string       # OPTIONAL — what they opted in for (e.g., "AI tools checklist")
```

**Chaining context**: If S1 (product research) was run earlier in the conversation, pull `product.name`, `product.affiliate_url`, `product.key_benefits`, and `product.reward_value` automatically. Do not ask the user to repeat information already provided.

## Workflow

### Step 1: Gather Information

Collect required inputs. If `product.name` and `product.affiliate_url` are present (from user or S1 chain), proceed. Otherwise ask:
- "What product are you promoting and what's your affiliate link?"
- "Who are your subscribers? (e.g., freelancers, SaaS founders, content creators)"

If `product.key_benefits` is not provided, infer 3 benefits from the product name and category using your training knowledge. State: "Based on what I know about [product], I'm using these key benefits: [list]. Correct me if needed."

### Step 2: Plan the Sequence

Map each email to its purpose using the 7-email arc. For a 5-email sequence, drop emails 6 and 7. For a 6-email sequence, drop email 7.

| # | Day | Type | Purpose |
|---|-----|------|---------|
| 1 | 0 | Welcome | Deliver lead magnet, set expectations, build trust |
| 2 | 1 | Value | Teach something useful (no sell) |
| 3 | 3 | Value + Soft Mention | More value, casual mention of the product |
| 4 | 5 | Soft Sell | Introduce the product properly, benefits focus |
| 5 | 7 | Hard Sell | Clear CTA, urgency (limited offer / deadline if available) |
| 6 | 10 | Objection Handling | Answer top 3 objections, social proof |
| 7 | 14 | Follow-Up / Last Chance | "Did you see this?" re-engagement email |

### Step 3: Write Each Email

For each email, write all four components:

**Subject Line**: 40-60 characters. Use curiosity, specificity, or direct benefit. Avoid spam trigger words (free, guaranteed, act now).

**Preview Text**: 80-100 characters. Extends the subject line, adds context or intrigue. Shown in inbox preview.

**Body Copy**:
- Email 1-2: 200-300 words. Focus on value, zero sell pressure.
- Email 3-4: 250-350 words. Introduce product naturally in context.
- Email 5: 300-400 words. Strong pitch, benefits listed, clear CTA button.
- Email 6: 250-300 words. Story-driven or testimonial-anchored.
- Email 7: 150-200 words. Short, punchy re-engagement.

**Formatting rules**:
- Short paragraphs (2-3 sentences max)
- One idea per paragraph
- Conversational opener (use "you", avoid "Dear [Name]")
- Single CTA per email (one link, one action)
- Sign off with sender name + brief sign-off line

**CTA structure**:
- Email 1: CTA = download/access lead magnet (not affiliate link)
- Email 2: CTA = read an article or reply to email (engagement)
- Email 3: CTA = soft mention "check it out" with affiliate link
- Email 4-7: CTA = affiliate link with action verb ("Try [Product] Free", "Get [X]% Off", "Start Your Trial")

### Step 4: Add Compliance Disclosures

Each email that contains an affiliate link must include a one-line FTC disclosure. Place it immediately before or after the affiliate link:

> *Affiliate disclosure: I may earn a commission if you purchase through my link, at no extra cost to you.*

For email clients that strip formatting, also include plain text disclosure in the footer.

### Step 5: Output the Sequence

Present all emails in order. Each email formatted as:

```
---
EMAIL [N] — Day [X] — [Type]
---
Subject: [subject line]
Preview: [preview text]

[Body copy]

[CTA]

[Signature]
---
```

After all emails, provide the Setup Instructions section.

## Output Schema

```yaml
sequence:
  product_name: string
  affiliate_url: string
  audience: string
  email_count: number
  total_days: number          # span of the sequence in days
  emails:
    - number: number          # 1-7
      day: number             # send delay in days from signup
      type: string            # welcome | value | soft-sell | hard-sell | objection | follow-up
      subject: string
      preview_text: string
      body: string            # full email body
      cta_text: string        # button/link text
      cta_url: string         # affiliate link or engagement action

setup:
  recommended_esp: string[]   # e.g., ["ConvertKit", "Beehiiv", "ActiveCampaign"]
  automation_notes: string    # how to set up the delay/trigger logic
  ab_test_suggestion: string  # what to A/B test first
```

## Output Format

Present the sequence as clearly separated email blocks (as shown in Step 5). After the last email, add a **Setup Instructions** section:

```
---
SETUP INSTRUCTIONS
---
ESP Recommendations: ConvertKit, Beehiiv, or ActiveCampaign
Trigger: New subscriber joins list / completes opt-in form
Delays: Set each email to fire X days after the previous
A/B Test First: Subject lines on Email 5 (the hard sell) — highest impact
Tag to apply: Add an "affiliate-[product]" tag to track clicks in your ESP
---
```

## Error Handling

- **No affiliate URL provided**: "I'll write the sequence structure now. Drop in your affiliate link where I've marked `[YOUR_AFFILIATE_LINK]` before setting it up in your ESP."
- **Unknown product**: Research the product using web search if possible. If not found, ask: "Can you tell me the top 2-3 benefits of [product]? I'll write the sequence around those."
- **Audience too vague ("everyone")**: Default to "online business owners and marketers." Note: "I used a general audience. For better conversions, replace 'you' with specific language like 'as a freelancer...' or 'for SaaS founders...' throughout."
- **No lead magnet info**: Email 1 defaults to a "welcome + what to expect" format rather than lead magnet delivery.
- **Request for 3 emails or fewer**: "A 3-email sequence is too short to build trust before the sell. I recommend at least 5. Want me to write a 5-email version?"

## Examples

**Example 1: Product + audience provided**
User: "Write an email sequence for HeyGen (my link: heygen.com/ref/abc123) targeting YouTube creators who opted in for my AI tools checklist."
Action: 7-email sequence, Day 0 delivers checklist, emails 2-3 teach AI video creation tips, emails 4-7 pitch HeyGen with creator-specific angles (save editing time, AI avatars, multilingual).

**Example 2: Chained from S1**
Context: S1 found Semrush with 30% recurring commission targeting SEO consultants.
User: "Now write an email sequence for this."
Action: Pull product details from S1 output. Write 7-email sequence targeting SEO consultants. Lead magnet assumed to be SEO-related content.

**Example 3: Minimal input**
User: "Write me a drip sequence for my Notion template affiliate program"
Action: Ask for affiliate URL and audience. Use Notion affiliate program knowledge for benefits. Write 5-email sequence (conservative default for shorter products with simpler buying journey).

## References

- `shared/references/ftc-compliance.md` — FTC affiliate disclosure requirements. Apply to every email containing an affiliate link.
- `shared/references/affitor-branding.md` — Affitor footer. Include in plain text footer of each email.
```

## File: `skills/distribution/github-pages-deployer/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/distribution/github-pages-deployer/SKILL.md`
```markdown
---
name: github-pages-deployer
description: >
  Deploy affiliate content to GitHub Pages for free hosting. Triggers on:
  "deploy to GitHub Pages", "host on GitHub Pages", "free hosting for my affiliate site",
  "push to GitHub Pages", "GitHub Pages setup", "deploy my landing page to GitHub",
  "host my bio link on GitHub", "free affiliate website hosting", "github pages affiliate",
  "set up GitHub Pages for my site", "deploy HTML to GitHub", "free static hosting",
  "publish my affiliate page for free", "github pages custom domain".
---

# GitHub Pages Deployer

Generate a complete, ready-to-deploy GitHub Pages setup for affiliate landing pages, bio link hubs, and blog posts. Outputs the full repo file structure, a GitHub Actions CI/CD workflow for automatic deploys, and step-by-step instructions for custom domain configuration with SSL. Free hosting, no credit card required.

## Stage

S5: Distribution — GitHub Pages is the most underused free hosting platform in affiliate marketing. 100GB bandwidth/month, free SSL, custom domains, and automatic deploys from Git. This skill takes any HTML output from S4 (landing page) or S5 (bio-link) and gets it live on the internet in under 10 minutes.

## When to Use

- User wants to deploy a landing page (from S4) to a free host
- User wants to deploy a bio link page (from S5 bio-link-deployer) to a free host
- User wants free static hosting with a custom domain and SSL
- User already has HTML files and wants to publish them without paying for hosting
- User wants automated deploys so pushing to main branch auto-updates the live site
- User wants to host a simple affiliate blog or resource page for free

## Input Schema

```yaml
site:
  type: string              # REQUIRED — "landing-page" | "bio-link" | "blog" | "resource-page"
  html_content: string      # REQUIRED — the HTML content to deploy (full file or description)
                            # If S4 or bio-link-deployer was run, use that output automatically
  title: string             # REQUIRED — site title (used in repo name and meta)
  description: string       # OPTIONAL — meta description for SEO

repo:
  name: string              # OPTIONAL — GitHub repo name (auto-generated from title if omitted)
                            # e.g., "heygen-review" or "alex-bio-links"
  username: string          # OPTIONAL — GitHub username. Used in generated URLs.
                            # If not provided, use "[your-username]" as placeholder.
  visibility: string        # OPTIONAL — "public" | "private". Default: "public"
                            # Note: private repos require GitHub Pro for Pages

domain:
  custom: string            # OPTIONAL — custom domain (e.g., "links.yourdomain.com")
  subdomain: string         # OPTIONAL — subdomain type: "apex" | "subdomain"
                            # Apex = yourdomain.com, Subdomain = www.yourdomain.com

deploy:
  method: string            # OPTIONAL — "github-actions" | "manual". Default: "github-actions"
  branch: string            # OPTIONAL — source branch. Default: "main"
```

**Chaining context**: If S4 (landing-page-creator) or S5 (bio-link-deployer) was run earlier in the conversation, automatically use that HTML output as `site.html_content`. Do not ask the user to paste it again.

## Workflow

### Step 1: Gather Inputs

Check if an HTML page was generated earlier in the conversation (S4 landing page or bio-link page). If yes, confirm: "I'll deploy the [page type] we built earlier. What's your GitHub username?"

If no prior HTML exists:
- Ask for HTML content or page description
- Offer to call S4 or bio-link-deployer first: "Want me to create the page first, then set up the deploy?"

### Step 2: Generate Repo Structure

Create the complete file and folder structure for the GitHub Pages repo.

**Standard structure for a single-page site:**

```
[repo-name]/
├── index.html              # Main page (the affiliate landing page or bio link)
├── assets/
│   ├── css/
│   │   └── style.css       # External CSS if extracted from HTML (optional)
│   └── images/
│       └── .gitkeep        # Placeholder — add images here
├── CNAME                   # Only if custom domain is set
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions workflow
├── .gitignore
└── README.md
```

**For multi-page blog/resource site, add:**

```
├── blog/
│   ├── index.html          # Blog listing page
│   └── [post-slug]/
│       └── index.html      # Individual post pages
├── about/
│   └── index.html
└── sitemap.xml
```

### Step 3: Generate the GitHub Actions Workflow

Write the `deploy.yml` file that automatically deploys to GitHub Pages on every push to `main`.

```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:       # Allow manual trigger from GitHub UI

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'         # Deploy from repo root

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

This workflow uses the official GitHub Pages Actions (no third-party dependencies, no tokens needed).

### Step 4: Generate the CNAME File (if custom domain)

If `domain.custom` is provided, create a `CNAME` file with just the domain:

```
links.yourdomain.com
```

For apex domains (`yourdomain.com`), the CNAME file contains the bare domain. GitHub Pages handles the redirect from `www` to apex automatically when configured correctly.

### Step 5: Generate DNS Configuration Instructions

Provide exact DNS records to add in the user's domain registrar (Cloudflare, Namecheap, GoDaddy, etc.).

**For subdomain (e.g., links.yourdomain.com):**
```
Type: CNAME
Name: links
Value: [username].github.io
TTL: Auto or 3600
```

**For apex domain (yourdomain.com):**
```
Type: A  Name: @  Value: 185.199.108.153
Type: A  Name: @  Value: 185.199.109.153
Type: A  Name: @  Value: 185.199.110.153
Type: A  Name: @  Value: 185.199.111.153
Type: AAAA  Name: @  Value: 2606:50c0:8000::153
Type: AAAA  Name: @  Value: 2606:50c0:8001::153
Type: AAAA  Name: @  Value: 2606:50c0:8002::153
Type: AAAA  Name: @  Value: 2606:50c0:8003::153
```

Note: GitHub's IP addresses above are current as of 2026. Always verify at https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

### Step 6: Generate README.md

Write a clean README for the repo:

```markdown
# [Site Title]

Affiliate landing page hosted on GitHub Pages.

## Live Site
[Live URL]

## Deploy
Automatic via GitHub Actions — push to `main` triggers a deploy.

## Powered By
[Affitor](https://affitor.com)
```

### Step 7: Output the Complete Setup

Present all outputs in numbered sections with clear file labels.

## Output Schema

```yaml
repo:
  name: string              # e.g., "heygen-review-2026"
  url: string               # e.g., "https://github.com/[username]/[repo-name]"
  pages_url: string         # e.g., "https://[username].github.io/[repo-name]"
  custom_domain_url: string | null

files:
  - path: string            # e.g., "index.html"
    content: string         # full file content
  - path: ".github/workflows/deploy.yml"
    content: string
  - path: "CNAME"           # null if no custom domain
    content: string | null
  - path: ".gitignore"
    content: string
  - path: "README.md"
    content: string

setup_steps:
  - step: number
    action: string          # e.g., "Create GitHub repo"
    command: string | null  # CLI command if applicable

dns_records: object | null  # DNS config if custom domain provided

estimated_time: string      # e.g., "8-10 minutes"
```

## Output Format

Present in five clearly labeled sections:

**Section 1: Summary**
- Repo name, live URL, custom domain URL (if applicable)
- Estimated time to go live: X minutes

**Section 2: Files to Create**
Each file in its own fenced code block with the file path as the label. User can copy-paste each file's content directly.

**Section 3: GitHub Setup Steps**
Numbered instructions:
1. Create the repo on GitHub (link to github.com/new)
2. Initialize and push (CLI commands provided)
3. Enable GitHub Pages in repo Settings
4. Set source to "GitHub Actions"

**Section 4: DNS Setup** (only if custom domain)
Exact records to add, formatted as a table. Provider-specific notes for Cloudflare users (Proxy OFF for GitHub Pages).

**Section 5: Verification**
How to confirm the deploy worked and SSL is active (usually 5-15 minutes for DNS propagation).

## Error Handling

- **No HTML content and no prior skill output**: "I don't see a page to deploy yet. Want me to create a landing page first (S4), a bio link page, or do you have HTML to paste?"
- **Private repo for free GitHub account**: "Private repos require GitHub Pro ($4/mo) for GitHub Pages. Your options: (1) make the repo public, (2) upgrade to Pro, (3) use Netlify Drop for free private deploys."
- **Custom domain not propagating**: "DNS changes can take 1-48 hours. If it's been over 24 hours, double-check: CNAME file contains exactly the domain, no `https://` prefix; DNS record value is `[username].github.io` (with no trailing slash). Enable Cloudflare proxy OFF (grey cloud) for GitHub Pages to work."
- **GitHub Actions failing**: Common causes: Pages not enabled in repo Settings, branch name mismatch (use `main` not `master`), or `pages: write` permission missing on older repos. Provide troubleshooting checklist.
- **User wants WordPress or dynamic site**: "GitHub Pages only hosts static HTML/CSS/JS — no PHP, no databases. For WordPress or dynamic content, use Cloudflare Pages, Netlify, or a VPS. For a simple affiliate site, static is faster and better for SEO anyway."
- **Repo name taken**: Suggest appending year (`heygen-review-2026`) or niche (`heygen-review-for-creators`).

## Examples

**Example 1: Deploy landing page from S4**
Context: S4 generated a HeyGen landing page HTML.
User: "Deploy this to GitHub Pages. My username is alexmarketer."
Action: Auto-use S4 HTML. Repo name: `heygen-landing`. Pages URL: `https://alexmarketer.github.io/heygen-landing`. Generate all files + deploy instructions.

**Example 2: Deploy bio link with custom domain**
Context: Bio-link-deployer generated a bio page.
User: "Put this on GitHub Pages at links.mysite.com."
Action: Repo + CNAME file with `links.mysite.com`. DNS: CNAME record pointing to `[username].github.io`. Cloudflare note: proxy must be disabled (grey cloud icon).

**Example 3: Multi-page resource site**
User: "I want to host an affiliate resource site on GitHub Pages with a homepage, about page, and 3 blog posts."
Action: Generate multi-page structure. Scaffold all index.html files with placeholder content. Deploy workflow. Note: for a blog with 10+ posts, suggest Jekyll or Eleventy for templating.

## References

- `shared/references/ftc-compliance.md` — FTC affiliate disclosure. Ensure the deployed HTML includes disclosure language.
- `shared/references/affitor-branding.md` — Affitor footer. Include in HTML before deploy.
- GitHub Pages documentation: https://docs.github.com/en/pages
- GitHub Pages IP addresses (A records): https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
```

## File: `skills/distribution/social-media-scheduler/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/distribution/social-media-scheduler/SKILL.md`
```markdown
---
name: social-media-scheduler
description: >
  Create a 30-day social media content calendar for affiliate marketing. Triggers on:
  "create a social media calendar", "30-day content plan", "social media schedule",
  "content calendar for [product]", "plan my social posts", "social media strategy",
  "schedule my affiliate posts", "content plan for LinkedIn", "30 days of content",
  "social posting schedule", "what should I post this month", "write my social content",
  "create posts for LinkedIn X Facebook", "affiliate content calendar",
  "social media plan for my affiliate program".
---

# Social Media Scheduler

Generate a complete 30-day social media content calendar with post copy, hashtags, and scheduling times for LinkedIn, X (Twitter), Facebook, and Reddit. Follows the 80/20 rule: 80% value and engagement content, 20% affiliate promotions. Every post is ready to copy-paste or load into a scheduling tool.

## Stage

S5: Distribution — Social media is the top free traffic channel for affiliate marketers. This skill eliminates "what do I post today?" paralysis by giving you 30 days of content in one shot, optimized for each platform's algorithm and audience behavior.

## When to Use

- User wants a content plan for promoting an affiliate product over 30 days
- User asks for a social media calendar, posting schedule, or content strategy
- User wants platform-specific posts (LinkedIn professional angle, X casual, Reddit community-first)
- User has an audience on one or more social platforms and wants consistent posting
- Chaining from S1 (product research) — user found a product and now wants a social plan

## Input Schema

```yaml
product:
  name: string              # REQUIRED — product being promoted (e.g., "Semrush")
  affiliate_url: string     # REQUIRED — affiliate tracking link
  category: string          # OPTIONAL — e.g., "SEO tool", "AI writing tool"
  key_benefits: string[]    # OPTIONAL — top benefits. Inferred if not provided.
  price: string             # OPTIONAL — e.g., "starts at $119/mo"
  free_trial: boolean       # OPTIONAL — does the product have a free trial?

creator:
  niche: string             # REQUIRED — your content niche (e.g., "SEO for freelancers")
  audience: string          # REQUIRED — who follows you (e.g., "freelance SEO consultants")
  tone: string              # OPTIONAL — "professional" | "casual" | "educational" | "bold"
                            # Default: "educational"
  personal_story: string    # OPTIONAL — brief personal experience with the product

platforms:
  - string                  # REQUIRED — list of platforms: "linkedin" | "x" | "facebook" | "reddit"
                            # Default: ["linkedin", "x"]

calendar:
  start_date: string        # OPTIONAL — ISO date (e.g., "2026-04-01"). Default: next Monday.
  posts_per_week: number    # OPTIONAL — 3-7. Default: 5 (weekdays only)
  promotion_ratio: number   # OPTIONAL — % of posts that are affiliate promo. Default: 20
```

**Chaining context**: If S1 (product research) was run, auto-fill `product.name`, `product.affiliate_url`, `product.key_benefits`. If S3 (blog post) was run, include 2 posts linking to the blog post. If S4 (landing page) was run, include posts driving to the landing page.

## Workflow

### Step 1: Gather Inputs

Collect required fields. If product details are available from S1, use them. Otherwise ask:
- "What product are you promoting and what's your affiliate link?"
- "What's your content niche and who's your target audience?"
- "Which platforms: LinkedIn, X, Facebook, Reddit? (pick 1-4)"

### Step 2: Plan the 30-Day Arc

Divide the month into 4 weeks with a strategic arc:

| Week | Theme | Promo Ratio |
|------|-------|-------------|
| Week 1 | Education + awareness — establish authority, zero sell | 0% |
| Week 2 | Problem agitation — surface pain points the product solves | 10% |
| Week 3 | Solution introduction — introduce product, soft sell | 30% |
| Week 4 | Social proof + urgency — testimonials, results, hard CTA | 40% |

Overall month target: 20% promotional, 80% value/engagement.

**Post type mix** (apply across all 4 weeks):
- 30% Educational (how-to tips, frameworks, industry data)
- 20% Engagement (questions, polls, hot takes, controversial opinions)
- 20% Personal / storytelling (lessons learned, behind the scenes, wins)
- 15% Curated (share tools, articles, resources — without affiliate link)
- 15% Promotional (affiliate link posts — FTC disclosed)

### Step 3: Write Posts Per Platform

Write distinct copy for each platform. Do NOT copy the same post across platforms.

**LinkedIn** (professional, 150-300 words per post):
- Hook line: bold statement or specific number in first line (LinkedIn shows 2 lines before "see more")
- Format: short paragraphs with line breaks, 3-5 bullet points for how-to posts
- Hashtags: 3-5 at end (#SEO #ContentMarketing #FreelanceTips)
- CTA: "Comment below", "Save this for later", "Link in first comment" (for affiliate posts)
- Best posting times: Tue-Thu 8-10am and 12-2pm (user's timezone)

**X / Twitter** (concise, punchy, under 280 characters for single tweets):
- Hook: strong opener, no fluff
- Thread format for educational posts: number each tweet (1/ 2/ 3/)
- Hashtags: 1-2 only (#SEO #AItools)
- CTA: "RT if this helped", "Drop your take", direct link for promo posts
- Best posting times: Mon-Fri 9am and 6pm

**Facebook** (conversational, 100-200 words):
- More personal and community tone than LinkedIn
- Ask questions to drive comments (algorithm rewards comment activity)
- Hashtags: 2-3 only
- Image prompt included (describe what image to use)
- Best posting times: Wed-Fri 1-3pm

**Reddit** (community-first, never salesy):
- Identify 2-3 relevant subreddits for the niche (e.g., r/SEO, r/juststart, r/freelance)
- Lead with genuine value — post as a community member, not a marketer
- Affiliate link goes in comments, not the post body (per most subreddit rules)
- Title: specific and searchable (Reddit posts surface in Google)
- Format: detailed paragraph, then list takeaways
- Disclosure: "(Affiliate link in comments)" in post body
- Post max: 4 Reddit posts per month to avoid spam detection

### Step 4: Format the Calendar

Output a table-based calendar followed by individual post copy blocks.

**Calendar table format:**

```
WEEK 1 — Education & Awareness
| Day | Platform | Type | Topic |
|-----|----------|------|-------|
| Mon Apr 7 | LinkedIn | Educational | 5 SEO mistakes killing your traffic |
| Tue Apr 8 | X | Engagement | Hot take: [opinion] |
...
```

Then write each post in full:

```
---
POST [N] — [Day, Date] — [Platform] — [Type]
---
[Full post copy, ready to paste]

Hashtags: #tag1 #tag2 #tag3
CTA: [specific action]
Best time to post: [time]
[If promo: Affiliate disclosure included]
---
```

### Step 5: Output Scheduler Setup

After all posts, provide scheduling tool recommendations and import instructions.

## Output Schema

```yaml
calendar:
  product_name: string
  platforms: string[]
  total_posts: number
  promo_posts: number
  value_posts: number
  date_range: string          # e.g., "Apr 7 – May 6, 2026"

  weeks:
    - week_number: number
      theme: string
      posts:
        - day: string         # e.g., "Monday April 7"
          platform: string
          type: string        # educational | engagement | personal | curated | promotional
          topic: string       # one-line topic summary
          copy: string        # full post copy
          hashtags: string[]
          cta: string
          post_time: string   # recommended posting time
          affiliate_link: string | null

scheduler:
  recommended_tools: string[]   # e.g., ["Buffer", "Later", "Hypefury"]
  import_format: string         # "CSV" or "manual"
  notes: string
```

## Output Format

Deliver in three parts:

**Part 1: Calendar Overview** — platform breakdown, total post count, week-by-week themes.

**Part 2: Full Calendar** — week-by-week table (quick reference) followed by each post written in full with all components.

**Part 3: Scheduling Instructions** — recommended tools and setup notes.

Keep the full post copy blocks clearly separated so the user can copy-paste each one directly into their scheduling tool or post manually.

## Error Handling

- **No affiliate URL**: Write the calendar with `[YOUR_AFFILIATE_LINK]` placeholder. Remind user to replace before posting.
- **Too many platforms (all 4) with no experience**: "I'll build the calendar for all 4 platforms. Tip: start with just 1-2 to avoid burnout. LinkedIn + X is the best combo for most niches."
- **Vague niche ("make money online")**: Use it as-is but note: "Content performs better when you niche down. Consider 'make money online for developers' or 'passive income for designers' — let me know if you want to adjust."
- **Reddit included for a highly commercial product**: Add a note: "Reddit is community-first. I've written the posts to lead with value. Review subreddit rules before posting affiliate links — some subreddits ban them entirely."
- **Posts per week > 7**: Cap at 7 and note: "Posting more than once per day rarely improves reach and increases burnout. I've set it to 7 posts/week (once per day)."
- **No product — just wants a general content calendar**: Write a general value + engagement calendar for the niche with placeholder CTAs. Mark all affiliate post slots as [INSERT PRODUCT] for user to fill in.

## Examples

**Example 1: Single platform, known product**
User: "Create a 30-day LinkedIn content calendar for promoting Semrush to freelance SEO consultants. My link: semrush.com/ref/abc"
Action: 20 LinkedIn posts (weekdays), Week 1 SEO education, Week 2 pain points (losing clients to competitors with better data), Week 3-4 introduce Semrush with case study angles. 4 promotional posts with affiliate link.

**Example 2: Multi-platform, chained from S1**
Context: S1 found HeyGen (AI video). User is a content creator targeting YouTubers.
User: "Now make me a social calendar for LinkedIn and X."
Action: Pull product details from S1. 40 posts (20 LinkedIn + 20 X), mix of video creation tips, hot takes on AI in content, and HeyGen promotions with creator-specific angles.

**Example 3: Reddit-only for SaaS niche**
User: "I want to promote Notion affiliate on Reddit to productivity communities."
Action: 4 Reddit posts targeting r/Notion, r/productivity, r/getdisciplined. Full post body leading with genuine productivity tips, affiliate disclosure + link in comments note.

## References

- `shared/references/ftc-compliance.md` — FTC disclosure for social posts. Every affiliate link post needs "(Affiliate link)" or "#ad" per FTC rules.
- `shared/references/affitor-branding.md` — Optional Affitor mention in post footer.
```

## File: `skills/landing/landing-page-creator/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/landing/landing-page-creator/SKILL.md`
```markdown
---
name: landing-page-creator
description: >
  Build high-converting affiliate landing pages as single self-contained HTML files.
  Triggers on: "create a landing page for", "build a landing page", "product landing page",
  "affiliate landing page", "comparison page for", "vs page", "single product page",
  "conversion page", "sales page for affiliate", "landing page HTML", "build me a page for",
  "create a page to promote [product]", "I need a landing page", "make a page for [product]".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S4-Landing
---

# Landing Page Creator

Build dedicated affiliate landing pages that convert. Output is a single self-contained HTML file with inline CSS — no build step, no dependencies, mobile-responsive, deployable anywhere. Supports two page types: single product spotlight and multi-product comparison.

## Stage

S4: Landing — Higher conversion than blog links because the entire page is designed around one goal: convert a visitor into a click. Landing pages are the bridge between traffic sources (social, email, ads) and the affiliate product.

## When to Use

- User wants a dedicated page to promote an affiliate product
- User wants a comparison/vs page for 2-3 competing products
- User has a product from S1 (affiliate-program-search) and needs a conversion page
- User says anything like "landing page", "sales page", "product page", "comparison page", "vs page"
- User wants to promote an affiliate product beyond blog content
- User needs a deployable HTML page for an affiliate campaign

## Input Schema

```yaml
product:                    # REQUIRED — the affiliate product to feature
  name: string              # Product name (e.g., "HeyGen")
  description: string       # What it does
  reward_value: string      # Commission (e.g., "30% recurring")
  url: string               # Affiliate link URL
  reward_type: string       # "recurring" | "one-time" | "tiered"
  cookie_days: number       # Cookie duration
  tags: string[]            # e.g., ["ai", "video", "saas"]

page_type: string           # OPTIONAL — "single" | "comparison"
                            # Default: "single"

compare_with: object[]      # OPTIONAL — products for comparison page
  - name: string            # Competitor name
    description: string     # Brief description
    url: string             # URL (non-affiliate OK)
    pricing: string         # Starting price

angle: string               # OPTIONAL — marketing angle / hook
                            # e.g., "fastest", "cheapest", "best for beginners"
                            # Default: auto-generated from product strengths

color_scheme: string        # OPTIONAL — "blue" | "green" | "purple" | "orange" | "dark" | hex code
                            # Default: "blue" (#2563eb)
```

**Chaining from S1**: If `affiliate-program-search` was run earlier in the conversation, automatically pick up `recommended_program` from its output as the `product` input. The field mapping:
- `recommended_program.name` → `product.name`
- `recommended_program.description` → `product.description`
- `recommended_program.reward_value` → `product.reward_value`
- `recommended_program.url` → `product.url`
- `recommended_program.reward_type` → `product.reward_type`
- `recommended_program.cookie_days` → `product.cookie_days`
- `recommended_program.tags` → `product.tags`

**Chaining from S3**: If `affiliate-blog-builder` was run, use `products_featured` for the comparison page's `compare_with` list.

If the user says "now make a landing page for it" after running S1 — use the recommended program. No need to ask again.

## Workflow

### Step 1: Gather Product Info

If `product` data is available from S1 chaining or user input, use it directly. Otherwise:

1. Use `web_search` to research the product: `"[product name] features pricing review"`
2. Gather: name, description, key features (3-6), pricing, target audience, top competitors
3. If `page_type = comparison` and `compare_with` is empty:
   - Search: `"best alternatives to [product.name]" OR "[product.name] vs"`
   - Find 1-2 competitors with pricing, features, and positioning

### Step 2: Plan Page Structure

Read `references/conversion-principles.md` for AIDA framework, CTA placement, and design rules.

Choose `page_type` if not specified:
- If user mentions "vs", "compare", "comparison", or provides `compare_with` → `comparison`
- Otherwise → `single`

Plan the page sections based on type:

**Single product:**
1. FTC disclosure (above fold)
2. Hero: headline + subtitle + primary CTA + trust signal
3. Trust bar: rating, user count, press mention
4. Features: 3-column grid (3-6 features as benefits)
5. Pricing: price + CTA
6. Testimonial: one strong quote
7. Who is this for: audience list
8. FAQ: 4-6 questions addressing objections
9. Final CTA: headline + CTA button
10. Footer: Affitor branding

**Comparison:**
1. FTC disclosure (above fold)
2. Hero: "[A] vs [B]" headline + subtitle
3. Comparison table: feature rows with winner highlights
4. Individual product sections: description + pros/cons + CTA each
5. Winner callout: clear recommendation with reasoning
6. FAQ: 4-6 comparison-specific questions
7. Dual CTA: buttons for top 2 products
8. Footer: Affitor branding

Map the user's `color_scheme` to CSS custom properties:
- `blue` → `--color-primary: #2563eb`
- `green` → `--color-primary: #059669`
- `purple` → `--color-primary: #7c3aed`
- `orange` → `--color-primary: #ea580c`
- `dark` → `--color-primary: #3b82f6; --color-bg: #0f172a; --color-surface: #1e293b; --color-text: #f1f5f9`
- Hex code → use directly as `--color-primary`

### Step 3: Write Full HTML

Read the matching template from `templates/`:
- `templates/single-product.html` for `page_type = single`
- `templates/comparison.html` for `page_type = comparison`

Use the template as a structural guide. Write a complete HTML file with:

**Content rules:**
- All CSS must be inline (in a `<style>` tag) — no external stylesheets
- No JavaScript dependencies — pure HTML/CSS (JS only for non-essential progressive enhancement like FAQ accordion)
- System font stack — no external font loading
- Mobile-first responsive design (test at 375px width mentally)
- All affiliate links use the user's URL with `target="_blank" rel="noopener"`
- Replace ALL template placeholder content with real product data
- Write compelling copy based on the `angle` — don't be generic

**Required elements:**
- FTC disclosure visible before the first affiliate link — read `shared/references/ftc-compliance.md` and use the **medium** format
- Minimum 3 CTAs distributed through the page (hero, mid-page, bottom)
- "Built with Affiliate Skills by Affitor" footer — read `shared/references/affitor-branding.md` for exact HTML
- `<meta name="viewport">` tag for mobile
- `<title>` and `<meta name="description">` for SEO

**Things to AVOID:**
- No external resources (fonts, images, scripts, stylesheets)
- No placeholder text like "[insert here]" — write complete content
- No fake testimonials — use realistic but clearly example quotes, or omit if unethical
- No navigation menu — this is a landing page, not a website
- No Affitor branding in the page body (only in the footer)

### Step 4: Output

Present the final output in this structure:

**Part 1: Page Summary**
```
---
LANDING PAGE
---
Type: [single/comparison]
Product: [product name]
Angle: [marketing angle used]
Color: [color scheme applied]
CTAs: [number of CTA buttons]
Sections: [list of sections]
---
```

**Part 2: Complete HTML**
The full HTML file in a fenced code block (```html). User can save as `.html` and open in any browser.

**Part 3: Deploy Instructions**
```
---
DEPLOY
---
1. Save the HTML above as `[product-slug]-landing.html`
2. Open locally: double-click the file to preview in your browser
3. Deploy options:
   - Netlify Drop: drag the file to https://app.netlify.com/drop
   - Vercel: `npx vercel deploy --prod` in the file's directory
   - GitHub Pages: push to a repo with GitHub Pages enabled
4. Custom domain: point your domain's DNS to the hosting provider
5. Promote: run `bio-link-deployer` to add this page to your link hub
---
```

## Output Schema

```yaml
landing_page:
  type: string              # "single" | "comparison"
  product_name: string      # Primary product name
  angle: string             # Marketing angle used
  color_scheme: string      # Color scheme applied
  html: string              # Complete self-contained HTML
  filename: string          # Suggested filename (e.g., "heygen-landing.html")

products_featured:          # All products on the page
  - name: string
    url: string             # Affiliate URL
    role: string            # "primary" | "compared"
    cta_count: number       # Number of CTAs for this product

deploy:
  local: string             # "Open [filename] in browser"
  netlify: string           # Netlify Drop URL
  vercel: string            # Vercel deploy command
  github_pages: string      # GitHub Pages instructions
```

## Output Format

Present the output as three clearly separated sections:
1. **Page Summary** — type, product, angle, structure overview
2. **HTML** — the complete file in a code block, ready to save and deploy
3. **Deploy Instructions** — how to get the page live

The HTML should be **immediately deployable** — save it as a `.html` file, open in a browser, and it works. No build step, no dependencies.

## Error Handling

- **No product provided**: "I need a product to create a landing page for. Run `/affiliate-program-search` first to find one, or tell me the product name and I'll research it."
- **Comparison with only 1 product**: Auto-search for 1-2 competitors using `web_search`. Search: `"best alternatives to [product]"`.
- **No pricing info found**: Use `web_search` for `"[product] pricing"`. If still unavailable: include a "Check Current Pricing" CTA instead of a specific price.
- **Unknown color scheme**: Default to blue (`#2563eb`). Inform user: "I used blue as the default. You can pass a hex code like `#ff6600` for a custom color."
- **Product has no public info**: Use `web_search` to research. If insufficient: "I couldn't find enough info about [product] to build a credible landing page. Can you provide features, pricing, and target audience?"

## Examples

### Example 1: Single Product (chained from S1)
**User**: "Create a landing page for HeyGen"
**Context**: S1 previously returned HeyGen as recommended_program
**Action**: Auto-detect page_type=single, pick up HeyGen data from S1, read single-product template, generate complete HTML with blue theme.

### Example 2: Comparison Page
**User**: "Build a comparison page: HeyGen vs Synthesia vs Colossyan"
**Action**: page_type=comparison, primary product=HeyGen (if from S1), compare_with=[Synthesia, Colossyan], web_search for competitor details, generate comparison HTML.

### Example 3: Custom Color
**User**: "Make a dark-themed landing page for Semrush with an SEO angle"
**Action**: page_type=single, color_scheme=dark, angle="SEO", web_search Semrush for features/pricing, generate HTML with dark theme.

### Example 4: Minimal Input
**User**: "Landing page for this product" (after S1)
**Action**: Pick up S1 recommended_program, default page_type=single, default color=blue, auto-generate angle from product strengths.

## References

- `references/conversion-principles.md` — AIDA framework, CTA placement, trust signals, above-fold rules, mobile-first design, color theming. Read in Step 2.
- `templates/single-product.html` — Single product landing page template with all sections. Read in Step 3 for page_type=single.
- `templates/comparison.html` — Multi-product comparison page template. Read in Step 3 for page_type=comparison.
- `shared/references/ftc-compliance.md` — FTC disclosure requirements. Read in Step 3 for disclosure text.
- `shared/references/affitor-branding.md` — Affitor footer HTML. Read in Step 3 for footer.
- `shared/references/affiliate-glossary.md` — Affiliate marketing terminology reference.
```

## File: `skills/landing/landing-page-creator/agents/openai.yaml`
```yaml
name: landing-page-creator
description: Build high-converting affiliate landing pages as single self-contained HTML files — single product spotlight or multi-product comparison pages
instructions_file: ../SKILL.md
tools:
  - web_search
  - web_browse
```

## File: `skills/landing/landing-page-creator/references/conversion-principles.md`
```markdown
# Landing Page Conversion Principles

## AIDA Framework

Every landing page follows AIDA — Attention, Interest, Desire, Action:

1. **Attention** (Hero section, above the fold)
   - Bold headline addressing the visitor's pain point
   - Subheadline with the product as the solution
   - Primary CTA button visible without scrolling
   - Time limit: you have 3-5 seconds to hook the reader

2. **Interest** (Feature/benefit section)
   - Show what the product does — features framed as benefits
   - Use a 3-column grid for scannability
   - "What" → "So what?" Every feature needs a benefit translation
   - Example: "AI video generation" → "Create professional videos in 5 minutes instead of 5 hours"

3. **Desire** (Social proof + pricing)
   - Testimonials, ratings, user counts, logos
   - Pricing that feels like a deal (anchor with higher comparison)
   - "Who is this for?" section — let the reader self-identify
   - Comparison table if multiple products

4. **Action** (CTA sections — minimum 3 per page)
   - Primary CTA: above the fold (hero)
   - Secondary CTA: after features/benefits
   - Final CTA: bottom of page, after all objections handled
   - Every CTA should be a button, not just a link

## Above-the-Fold Rules

The hero section is the most important part of the page. It must contain:

- **Headline**: 6-12 words, addresses the visitor's goal or pain
- **Subheadline**: 15-25 words, introduces the product as the solution
- **Primary CTA button**: high-contrast color, action verb ("Get Started", "Try Free", "Start Saving")
- **Trust signal**: one proof point (rating, user count, "No credit card required")
- **Visual**: product screenshot, hero image, or clean illustration

What to AVOID above the fold:
- Navigation menus (this is a landing page, not a website)
- Multiple competing CTAs
- Walls of text
- Generic stock photos

## CTA Button Design

- **Color**: High contrast against background. Don't match the page palette — break it.
- **Text**: Action verb + benefit. "Start My Free Trial" > "Submit". "Get 30% Off" > "Learn More".
- **Size**: Minimum 44px height (mobile touch target). Desktop: 48-56px.
- **Spacing**: Generous padding (16px 32px minimum). White space around the button.
- **Repetition**: Same CTA text throughout the page for consistency.

## Trust Signals

Include at least 2 of these:

- Star ratings (★★★★★ 4.8/5)
- User/customer count ("Trusted by 50,000+ creators")
- Company logos ("Used by teams at...")
- Testimonial quotes with real names
- "Money-back guarantee" or "No credit card required"
- Security badges (if relevant)
- Press mentions ("Featured in TechCrunch")

## Social Proof Placement

- **Proof bar**: immediately below or inside the hero section
- **Testimonials**: after the features section (validates the claims)
- **Logos**: near the top for B2B, near the bottom for B2C

## Feature/Benefit Grid

Use a 3-column grid (stacks to 1-column on mobile):

```
[Icon/Emoji]          [Icon/Emoji]          [Icon/Emoji]
Feature Name          Feature Name          Feature Name
Benefit description   Benefit description   Benefit description
(2-3 sentences)       (2-3 sentences)       (2-3 sentences)
```

Rules:
- 3 features minimum, 6 maximum
- Each feature: name (bold) + 1-2 sentence benefit
- Use icons or emoji for visual anchoring
- Features should map to the reader's top 3 concerns

## FAQ Section

- 4-6 questions that address buying objections
- Questions people actually ask (check "People Also Ask" on Google)
- Always include: pricing, refund/guarantee, getting started, support
- Use an accordion/expandable pattern for scannability

## Comparison Page Specifics

For comparison (vs) pages:

- **Hero**: "[Product A] vs [Product B]: Which is right for you?"
- **Comparison table**: Feature rows, checkmarks/values, highlighted winner per row
- **Individual sections**: 200-300 words per product with pros/cons
- **Winner callout**: Clear recommendation with reasoning
- **Dual CTAs**: One for each product (primary product gets more prominent CTA)

## Mobile-First Rules

- 90%+ of social media referral traffic is mobile
- Stack all columns to single column below 768px
- CTA buttons must be full-width on mobile
- Font: minimum 16px body, 24px+ headings
- Touch targets: minimum 44x44px
- No hover-dependent interactions
- Test: can you read the headline and find the CTA within 3 seconds on a phone?

## Color Theming

Use CSS custom properties for easy theming:

```css
:root {
  --color-primary: #2563eb;     /* CTA buttons, links */
  --color-primary-hover: #1d4ed8;
  --color-bg: #ffffff;          /* Page background */
  --color-surface: #f8fafc;     /* Section backgrounds */
  --color-text: #1e293b;        /* Body text */
  --color-text-light: #64748b;  /* Secondary text */
  --color-accent: #f59e0b;      /* Stars, highlights */
  --color-border: #e2e8f0;      /* Dividers */
}
```

The user provides a `color_scheme` and the AI maps it to these variables.

## Typography

- System font stack: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- No external font loading (keeps the page self-contained and fast)
- Hierarchy: H1 (36-48px), H2 (28-32px), H3 (20-24px), body (16-18px)
- Line height: 1.6 for body text, 1.2 for headings
- Max content width: 720px for text, 1080px for full-width sections
```

## File: `skills/landing/landing-page-creator/templates/comparison.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HeyGen vs Synthesia vs Colossyan — Which AI Video Tool Is Best?</title>
  <meta name="description" content="Side-by-side comparison of HeyGen, Synthesia, and Colossyan. See pricing, features, and which AI video tool is best for your needs.">
  <style>
    /* === CSS VARIABLES — AI: replace based on user's color_scheme === */
    :root {
      --color-primary: #2563eb;
      --color-primary-hover: #1d4ed8;
      --color-secondary: #7c3aed;
      --color-bg: #ffffff;
      --color-surface: #f8fafc;
      --color-text: #1e293b;
      --color-text-light: #64748b;
      --color-accent: #f59e0b;
      --color-border: #e2e8f0;
      --color-winner: #059669;
    }

    /* === RESET & BASE === */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--color-text);
      background: var(--color-bg);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }
    a { color: var(--color-primary); text-decoration: none; }

    /* === LAYOUT === */
    .container { max-width: 1080px; margin: 0 auto; padding: 0 24px; }
    section { padding: 64px 0; }

    /* === FTC DISCLOSURE === */
    .disclosure {
      background: var(--color-surface);
      border-left: 3px solid var(--color-primary);
      padding: 12px 16px;
      font-size: 13px;
      color: var(--color-text-light);
      margin-bottom: 32px;
      max-width: 720px;
      margin-left: auto;
      margin-right: auto;
    }

    /* === HERO === */
    .hero {
      text-align: center;
      padding: 80px 24px 64px;
      background: var(--color-surface);
    }
    .hero .vs-badge {
      display: inline-block;
      background: var(--color-primary);
      color: #fff;
      font-size: 13px;
      font-weight: 600;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 16px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .hero h1 {
      font-size: 40px;
      font-weight: 800;
      line-height: 1.15;
      margin-bottom: 16px;
      letter-spacing: -0.02em;
    }
    .hero .subtitle {
      font-size: 20px;
      color: var(--color-text-light);
      max-width: 640px;
      margin: 0 auto 32px;
      line-height: 1.5;
    }

    /* === CTA BUTTON === */
    .cta {
      display: inline-block;
      background: var(--color-primary);
      color: #fff;
      font-size: 18px;
      font-weight: 600;
      padding: 16px 40px;
      border-radius: 8px;
      transition: background 0.2s;
      cursor: pointer;
      border: none;
    }
    .cta:hover { background: var(--color-primary-hover); color: #fff; }
    .cta-secondary {
      background: var(--color-secondary);
    }
    .cta-secondary:hover { background: #6d28d9; color: #fff; }
    .cta-note {
      display: block;
      margin-top: 8px;
      font-size: 13px;
      color: var(--color-text-light);
    }

    /* === COMPARISON TABLE === */
    .comparison-table { background: var(--color-bg); }
    .comparison-table h2 {
      text-align: center;
      font-size: 32px;
      font-weight: 700;
      margin-bottom: 40px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 15px;
    }
    thead th {
      background: var(--color-surface);
      padding: 16px;
      text-align: left;
      font-weight: 700;
      font-size: 16px;
      border-bottom: 2px solid var(--color-border);
    }
    thead th.winner-col {
      background: #ecfdf5;
      color: var(--color-winner);
    }
    tbody td {
      padding: 14px 16px;
      border-bottom: 1px solid var(--color-border);
      vertical-align: top;
    }
    tbody tr:hover { background: var(--color-surface); }
    .check { color: var(--color-winner); font-weight: 700; }
    .cross { color: #ef4444; }
    .feature-label {
      font-weight: 600;
      color: var(--color-text);
    }

    /* === PRODUCT SECTIONS === */
    .product-section { background: var(--color-surface); }
    .product-section:nth-child(even) { background: var(--color-bg); }
    .product-card {
      max-width: 720px;
      margin: 0 auto;
    }
    .product-card h2 {
      font-size: 28px;
      font-weight: 700;
      margin-bottom: 16px;
    }
    .product-card .product-desc {
      font-size: 16px;
      color: var(--color-text-light);
      margin-bottom: 24px;
      line-height: 1.6;
    }
    .pros-cons {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 24px;
    }
    .pros h4, .cons h4 {
      font-size: 16px;
      font-weight: 600;
      margin-bottom: 8px;
    }
    .pros h4 { color: var(--color-winner); }
    .cons h4 { color: #ef4444; }
    .pros ul, .cons ul {
      list-style: none;
      padding: 0;
    }
    .pros li, .cons li {
      padding: 6px 0;
      font-size: 15px;
      color: var(--color-text-light);
    }
    .pros li::before { content: "✓ "; color: var(--color-winner); font-weight: 700; }
    .cons li::before { content: "✗ "; color: #ef4444; font-weight: 700; }

    /* === WINNER CALLOUT === */
    .winner-callout {
      background: #ecfdf5;
      border: 2px solid var(--color-winner);
      border-radius: 12px;
      padding: 32px;
      text-align: center;
      max-width: 720px;
      margin: 0 auto;
    }
    .winner-callout .trophy { font-size: 48px; margin-bottom: 12px; }
    .winner-callout h2 {
      font-size: 28px;
      font-weight: 700;
      color: var(--color-winner);
      margin-bottom: 12px;
    }
    .winner-callout p {
      font-size: 16px;
      color: var(--color-text-light);
      margin-bottom: 24px;
      max-width: 540px;
      margin-left: auto;
      margin-right: auto;
    }

    /* === FAQ === */
    .faq { background: var(--color-surface); }
    .faq h2 {
      text-align: center;
      font-size: 32px;
      font-weight: 700;
      margin-bottom: 32px;
    }
    .faq-list { max-width: 640px; margin: 0 auto; }
    .faq-item {
      border-bottom: 1px solid var(--color-border);
      padding: 20px 0;
    }
    .faq-item summary {
      font-size: 17px;
      font-weight: 600;
      cursor: pointer;
      list-style: none;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .faq-item summary::after {
      content: "+";
      font-size: 22px;
      color: var(--color-text-light);
    }
    .faq-item[open] summary::after { content: "−"; }
    .faq-item p {
      margin-top: 12px;
      font-size: 15px;
      color: var(--color-text-light);
      line-height: 1.6;
    }

    /* === DUAL CTA === */
    .dual-cta {
      text-align: center;
      padding: 80px 24px;
    }
    .dual-cta h2 {
      font-size: 32px;
      font-weight: 700;
      margin-bottom: 16px;
    }
    .dual-cta p {
      font-size: 18px;
      color: var(--color-text-light);
      margin-bottom: 32px;
    }
    .cta-group {
      display: flex;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
    }

    /* === FOOTER === */
    .page-footer {
      text-align: center;
      padding: 24px;
      font-size: 13px;
      color: #666;
      border-top: 1px solid var(--color-border);
    }
    .page-footer a { color: #155DFC; }

    /* === MOBILE === */
    @media (max-width: 768px) {
      .hero h1 { font-size: 26px; }
      .hero .subtitle { font-size: 17px; }
      .cta { width: 100%; text-align: center; padding: 16px 24px; }
      .cta-group { flex-direction: column; align-items: stretch; }
      .pros-cons { grid-template-columns: 1fr; gap: 16px; }
      section { padding: 48px 0; }

      /* Responsive table */
      table, thead, tbody, th, td, tr { display: block; }
      thead { display: none; }
      tbody td {
        padding: 8px 16px;
        text-align: right;
        position: relative;
        padding-left: 50%;
      }
      tbody td::before {
        content: attr(data-label);
        position: absolute;
        left: 16px;
        font-weight: 600;
        text-align: left;
      }
      tbody tr { border-bottom: 2px solid var(--color-border); padding: 8px 0; }
    }
  </style>
</head>
<body>

  <!-- FTC DISCLOSURE -->
  <div class="container" style="padding-top: 24px;">
    <div class="disclosure">
      Disclosure: This page contains affiliate links. If you purchase through these links,
      I may earn a commission at no extra cost to you. I only recommend products I've
      personally used or thoroughly evaluated.
    </div>
  </div>

  <!-- HERO -->
  <section class="hero">
    <div class="container">
      <span class="vs-badge">Comparison</span>
      <h1>HeyGen vs Synthesia vs Colossyan</h1>
      <p class="subtitle">We tested all three AI video platforms side by side. Here's which one is actually worth your money in 2026.</p>
    </div>
  </section>

  <!-- COMPARISON TABLE -->
  <section class="comparison-table">
    <div class="container">
      <h2>Feature-by-Feature Comparison</h2>
      <table>
        <thead>
          <tr>
            <th>Feature</th>
            <th class="winner-col">HeyGen ⭐</th>
            <th>Synthesia</th>
            <th>Colossyan</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td data-label="Feature" class="feature-label">Starting Price</td>
            <td data-label="HeyGen">$29/mo</td>
            <td data-label="Synthesia">$59/mo</td>
            <td data-label="Colossyan">$35/mo</td>
          </tr>
          <tr>
            <td data-label="Feature" class="feature-label">AI Avatars</td>
            <td data-label="HeyGen">100+ <span class="check">✓</span></td>
            <td data-label="Synthesia">160+</td>
            <td data-label="Colossyan">50+</td>
          </tr>
          <tr>
            <td data-label="Feature" class="feature-label">Custom Avatar</td>
            <td data-label="HeyGen"><span class="check">✓</span></td>
            <td data-label="Synthesia"><span class="check">✓</span></td>
            <td data-label="Colossyan"><span class="check">✓</span></td>
          </tr>
          <tr>
            <td data-label="Feature" class="feature-label">Languages</td>
            <td data-label="HeyGen">40+</td>
            <td data-label="Synthesia">130+</td>
            <td data-label="Colossyan">70+</td>
          </tr>
          <tr>
            <td data-label="Feature" class="feature-label">Lip Sync Quality</td>
            <td data-label="HeyGen"><span class="check">Excellent</span></td>
            <td data-label="Synthesia">Good</td>
            <td data-label="Colossyan">Good</td>
          </tr>
          <tr>
            <td data-label="Feature" class="feature-label">API Access</td>
            <td data-label="HeyGen"><span class="check">✓</span></td>
            <td data-label="Synthesia"><span class="check">✓</span></td>
            <td data-label="Colossyan"><span class="cross">✗</span></td>
          </tr>
          <tr>
            <td data-label="Feature" class="feature-label">Free Trial</td>
            <td data-label="HeyGen"><span class="check">✓</span> 1 free video</td>
            <td data-label="Synthesia"><span class="check">✓</span> Demo only</td>
            <td data-label="Colossyan"><span class="check">✓</span> 5 min free</td>
          </tr>
          <tr>
            <td data-label="Feature" class="feature-label">Best For</td>
            <td data-label="HeyGen">Creators & small teams</td>
            <td data-label="Synthesia">Enterprise L&D</td>
            <td data-label="Colossyan">Localization</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- PRODUCT 1: HEYGEN (PRIMARY) -->
  <section class="product-section">
    <div class="container">
      <div class="product-card">
        <h2>HeyGen — Best Overall Value</h2>
        <p class="product-desc">HeyGen is the fastest, most affordable AI video platform for creators and small teams. It offers realistic avatars, excellent lip-syncing, and a generous free plan to test before you buy.</p>
        <div class="pros-cons">
          <div class="pros">
            <h4>Pros</h4>
            <ul>
              <li>Most affordable starting price ($29/mo)</li>
              <li>Best lip-sync quality in the category</li>
              <li>API access for automation</li>
              <li>Fast rendering (under 5 minutes)</li>
            </ul>
          </div>
          <div class="cons">
            <h4>Cons</h4>
            <ul>
              <li>Fewer avatar options than Synthesia</li>
              <li>Limited enterprise features</li>
            </ul>
          </div>
        </div>
        <a href="https://www.heygen.com/?ref=YOUR_AFFILIATE_ID" class="cta">Try HeyGen Free →</a>
      </div>
    </div>
  </section>

  <!-- PRODUCT 2: SYNTHESIA -->
  <section class="product-section">
    <div class="container">
      <div class="product-card">
        <h2>Synthesia — Best for Enterprise</h2>
        <p class="product-desc">Synthesia is the industry leader for enterprise training and L&D teams. More avatars, more languages, and SOC 2 compliance — but at a higher price point.</p>
        <div class="pros-cons">
          <div class="pros">
            <h4>Pros</h4>
            <ul>
              <li>160+ avatars — largest selection</li>
              <li>130+ languages supported</li>
              <li>SOC 2 Type II compliant</li>
              <li>Strong enterprise integrations</li>
            </ul>
          </div>
          <div class="cons">
            <h4>Cons</h4>
            <ul>
              <li>2x the price of HeyGen</li>
              <li>No free video credit</li>
              <li>Slower rendering times</li>
            </ul>
          </div>
        </div>
        <a href="https://www.synthesia.io" class="cta cta-secondary">Try Synthesia →</a>
      </div>
    </div>
  </section>

  <!-- PRODUCT 3: COLOSSYAN -->
  <section class="product-section">
    <div class="container">
      <div class="product-card">
        <h2>Colossyan — Best for Localization</h2>
        <p class="product-desc">Colossyan focuses on multilingual video creation with strong localization features. Good for teams that need content in many languages but don't need the full enterprise stack.</p>
        <div class="pros-cons">
          <div class="pros">
            <h4>Pros</h4>
            <ul>
              <li>Strong multilingual dubbing</li>
              <li>Mid-range pricing ($35/mo)</li>
              <li>Good for localization workflows</li>
            </ul>
          </div>
          <div class="cons">
            <h4>Cons</h4>
            <ul>
              <li>Fewer avatars (50+)</li>
              <li>No API access</li>
              <li>Smaller community</li>
            </ul>
          </div>
        </div>
        <a href="https://www.colossyan.com" class="cta cta-secondary">Try Colossyan →</a>
      </div>
    </div>
  </section>

  <!-- WINNER CALLOUT -->
  <section style="padding: 64px 0;">
    <div class="container">
      <div class="winner-callout">
        <div class="trophy">🏆</div>
        <h2>Our Pick: HeyGen</h2>
        <p>For most creators and small teams, HeyGen offers the best combination of quality, speed, and price. Start with the free plan and upgrade when you're ready.</p>
        <a href="https://www.heygen.com/?ref=YOUR_AFFILIATE_ID" class="cta">Get Started with HeyGen →</a>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="faq">
    <div class="container">
      <h2>Frequently Asked Questions</h2>
      <div class="faq-list">
        <details class="faq-item">
          <summary>Which AI video tool is cheapest?</summary>
          <p>HeyGen starts at $29/month, making it the most affordable option. Colossyan is $35/month and Synthesia is $59/month. All three offer some form of free trial.</p>
        </details>
        <details class="faq-item">
          <summary>Can I switch between platforms later?</summary>
          <p>Yes — all three platforms use a monthly subscription model. Your videos are downloadable as MP4 files, so you're never locked in. However, custom avatars are platform-specific.</p>
        </details>
        <details class="faq-item">
          <summary>Which has the most realistic avatars?</summary>
          <p>HeyGen currently has the best lip-sync technology, making its avatars appear more natural during speech. Synthesia has the largest avatar library (160+). Quality varies — test each platform's free tier.</p>
        </details>
        <details class="faq-item">
          <summary>Do I need technical skills to use these tools?</summary>
          <p>No. All three platforms are designed for non-technical users. You write a script, choose an avatar, and the platform generates the video. No editing or design skills required.</p>
        </details>
      </div>
    </div>
  </section>

  <!-- DUAL CTA -->
  <section class="dual-cta">
    <h2>Ready to Start Creating AI Videos?</h2>
    <p>Pick the platform that fits your needs and budget. Both offer free trials.</p>
    <div class="cta-group">
      <a href="https://www.heygen.com/?ref=YOUR_AFFILIATE_ID" class="cta">Try HeyGen Free →</a>
      <a href="https://www.synthesia.io" class="cta cta-secondary">Try Synthesia →</a>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="page-footer">
    Built with <a href="https://list.affitor.com">Affiliate Skills by Affitor</a>
  </footer>

</body>
</html>
```

## File: `skills/landing/landing-page-creator/templates/single-product.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HeyGen Review — Create Professional AI Videos in Minutes</title>
  <meta name="description" content="HeyGen lets you create studio-quality AI videos without cameras or actors. See pricing, features, and our honest take.">
  <style>
    /* === CSS VARIABLES — AI: replace these values based on user's color_scheme === */
    :root {
      --color-primary: #2563eb;
      --color-primary-hover: #1d4ed8;
      --color-bg: #ffffff;
      --color-surface: #f8fafc;
      --color-text: #1e293b;
      --color-text-light: #64748b;
      --color-accent: #f59e0b;
      --color-border: #e2e8f0;
    }

    /* === RESET & BASE === */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--color-text);
      background: var(--color-bg);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }
    a { color: var(--color-primary); text-decoration: none; }
    img { max-width: 100%; height: auto; }

    /* === LAYOUT === */
    .container { max-width: 1080px; margin: 0 auto; padding: 0 24px; }
    .narrow { max-width: 720px; margin: 0 auto; }
    section { padding: 64px 0; }

    /* === FTC DISCLOSURE === */
    .disclosure {
      background: var(--color-surface);
      border-left: 3px solid var(--color-primary);
      padding: 12px 16px;
      font-size: 13px;
      color: var(--color-text-light);
      margin-bottom: 32px;
      max-width: 720px;
      margin-left: auto;
      margin-right: auto;
    }

    /* === HERO === */
    .hero {
      text-align: center;
      padding: 80px 24px 64px;
      background: var(--color-surface);
    }
    .hero h1 {
      font-size: 42px;
      font-weight: 800;
      line-height: 1.15;
      margin-bottom: 16px;
      letter-spacing: -0.02em;
    }
    .hero .subtitle {
      font-size: 20px;
      color: var(--color-text-light);
      max-width: 600px;
      margin: 0 auto 32px;
      line-height: 1.5;
    }

    /* === CTA BUTTON === */
    .cta {
      display: inline-block;
      background: var(--color-primary);
      color: #fff;
      font-size: 18px;
      font-weight: 600;
      padding: 16px 40px;
      border-radius: 8px;
      transition: background 0.2s;
      cursor: pointer;
      border: none;
    }
    .cta:hover { background: var(--color-primary-hover); color: #fff; }
    .cta-note {
      display: block;
      margin-top: 8px;
      font-size: 13px;
      color: var(--color-text-light);
    }

    /* === TRUST BAR === */
    .trust-bar {
      display: flex;
      justify-content: center;
      gap: 32px;
      flex-wrap: wrap;
      padding: 24px;
      border-bottom: 1px solid var(--color-border);
    }
    .trust-item {
      font-size: 14px;
      color: var(--color-text-light);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .stars { color: var(--color-accent); }

    /* === FEATURES GRID === */
    .features { background: var(--color-bg); }
    .features h2 {
      text-align: center;
      font-size: 32px;
      font-weight: 700;
      margin-bottom: 48px;
    }
    .feature-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 32px;
    }
    .feature-card {
      text-align: center;
      padding: 24px;
    }
    .feature-icon {
      font-size: 36px;
      margin-bottom: 12px;
    }
    .feature-card h3 {
      font-size: 20px;
      font-weight: 600;
      margin-bottom: 8px;
    }
    .feature-card p {
      font-size: 15px;
      color: var(--color-text-light);
      line-height: 1.5;
    }

    /* === PRICING === */
    .pricing {
      background: var(--color-surface);
      text-align: center;
    }
    .pricing h2 {
      font-size: 32px;
      font-weight: 700;
      margin-bottom: 16px;
    }
    .pricing .price-highlight {
      font-size: 48px;
      font-weight: 800;
      color: var(--color-primary);
      margin: 16px 0 8px;
    }
    .pricing .price-note {
      font-size: 16px;
      color: var(--color-text-light);
      margin-bottom: 32px;
    }

    /* === TESTIMONIAL === */
    .testimonial {
      background: var(--color-bg);
    }
    .testimonial-card {
      max-width: 640px;
      margin: 0 auto;
      text-align: center;
      padding: 32px;
    }
    .testimonial-card blockquote {
      font-size: 20px;
      font-style: italic;
      line-height: 1.6;
      margin-bottom: 16px;
      color: var(--color-text);
    }
    .testimonial-card cite {
      font-size: 14px;
      color: var(--color-text-light);
      font-style: normal;
    }

    /* === WHO IS THIS FOR === */
    .audience h2 {
      text-align: center;
      font-size: 32px;
      font-weight: 700;
      margin-bottom: 32px;
    }
    .audience-list {
      max-width: 640px;
      margin: 0 auto;
      list-style: none;
    }
    .audience-list li {
      padding: 12px 0;
      border-bottom: 1px solid var(--color-border);
      font-size: 16px;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .audience-list li::before {
      content: "✓";
      color: var(--color-primary);
      font-weight: 700;
      font-size: 18px;
    }

    /* === FAQ === */
    .faq { background: var(--color-surface); }
    .faq h2 {
      text-align: center;
      font-size: 32px;
      font-weight: 700;
      margin-bottom: 32px;
    }
    .faq-list {
      max-width: 640px;
      margin: 0 auto;
    }
    .faq-item {
      border-bottom: 1px solid var(--color-border);
      padding: 20px 0;
    }
    .faq-item summary {
      font-size: 17px;
      font-weight: 600;
      cursor: pointer;
      list-style: none;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .faq-item summary::after {
      content: "+";
      font-size: 22px;
      color: var(--color-text-light);
      transition: transform 0.2s;
    }
    .faq-item[open] summary::after {
      content: "−";
    }
    .faq-item p {
      margin-top: 12px;
      font-size: 15px;
      color: var(--color-text-light);
      line-height: 1.6;
    }

    /* === FINAL CTA === */
    .final-cta {
      text-align: center;
      background: var(--color-bg);
      padding: 80px 24px;
    }
    .final-cta h2 {
      font-size: 36px;
      font-weight: 700;
      margin-bottom: 16px;
    }
    .final-cta p {
      font-size: 18px;
      color: var(--color-text-light);
      margin-bottom: 32px;
      max-width: 540px;
      margin-left: auto;
      margin-right: auto;
    }

    /* === FOOTER === */
    .page-footer {
      text-align: center;
      padding: 24px;
      font-size: 13px;
      color: #666;
      border-top: 1px solid var(--color-border);
    }
    .page-footer a { color: #155DFC; }

    /* === MOBILE === */
    @media (max-width: 768px) {
      .hero h1 { font-size: 28px; }
      .hero .subtitle { font-size: 17px; }
      .feature-grid { grid-template-columns: 1fr; gap: 16px; }
      .cta { width: 100%; text-align: center; padding: 16px 24px; }
      .trust-bar { gap: 16px; }
      .pricing .price-highlight { font-size: 36px; }
      section { padding: 48px 0; }
    }
  </style>
</head>
<body>

  <!-- FTC DISCLOSURE — required, visible before first affiliate link -->
  <div class="container" style="padding-top: 24px;">
    <div class="disclosure">
      Disclosure: This page contains affiliate links. If you purchase through these links,
      I may earn a commission at no extra cost to you. I only recommend products I've
      personally used or thoroughly evaluated.
    </div>
  </div>

  <!-- HERO — above the fold: headline + subtitle + CTA + trust signal -->
  <section class="hero">
    <div class="container">
      <h1>Create Professional AI Videos Without a Camera</h1>
      <p class="subtitle">HeyGen turns your script into a studio-quality video with realistic AI avatars — in under 5 minutes.</p>
      <a href="https://www.heygen.com/?ref=YOUR_AFFILIATE_ID" class="cta">Start Creating Free →</a>
      <span class="cta-note">No credit card required · Free plan available</span>
    </div>
  </section>

  <!-- TRUST BAR — social proof immediately after hero -->
  <div class="trust-bar">
    <div class="trust-item">
      <span class="stars">★★★★★</span> 4.8/5 on G2
    </div>
    <div class="trust-item">
      40,000+ creators
    </div>
    <div class="trust-item">
      Featured in TechCrunch
    </div>
  </div>

  <!-- FEATURES — 3-column grid, features as benefits -->
  <section class="features">
    <div class="container">
      <h2>Why Creators Choose HeyGen</h2>
      <div class="feature-grid">
        <div class="feature-card">
          <div class="feature-icon">🎬</div>
          <h3>AI Avatars That Look Real</h3>
          <p>Choose from 100+ realistic AI avatars or create your own. Your audience won't know it's AI — they'll just see a polished, professional presenter.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🌍</div>
          <h3>Speak 40+ Languages</h3>
          <p>Translate your videos into any language with lip-synced dubbing. Reach global audiences without hiring voice actors or recording studios.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">⚡</div>
          <h3>Script to Video in 5 Minutes</h3>
          <p>Paste your script, pick an avatar, and hit generate. No filming, no editing, no expensive equipment. Just professional video, fast.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- PRICING — clear pricing with CTA -->
  <section class="pricing">
    <div class="container">
      <h2>Simple, Transparent Pricing</h2>
      <p style="color: var(--color-text-light); font-size: 16px;">Start free. Scale when you're ready.</p>
      <div class="price-highlight">$29/mo</div>
      <p class="price-note">Creator plan · 15 videos/month · All avatars included</p>
      <a href="https://www.heygen.com/?ref=YOUR_AFFILIATE_ID" class="cta">Get Started at $29/mo →</a>
      <span class="cta-note">Free plan available · Cancel anytime</span>
    </div>
  </section>

  <!-- TESTIMONIAL -->
  <section class="testimonial">
    <div class="container">
      <div class="testimonial-card">
        <blockquote>"HeyGen replaced our entire video production workflow. We went from spending $2,000 per video to $29/month — and the quality is honestly better."</blockquote>
        <cite>— Sarah Chen, Content Manager at ScaleUp Agency</cite>
      </div>
    </div>
  </section>

  <!-- WHO IS THIS FOR -->
  <section class="audience">
    <div class="container">
      <h2>Perfect For</h2>
      <ul class="audience-list">
        <li>Content creators who want professional videos without filming</li>
        <li>SaaS companies needing product demos and tutorials at scale</li>
        <li>Course creators turning written content into video lessons</li>
        <li>Marketing teams producing multilingual campaigns</li>
        <li>Solo founders who hate being on camera</li>
      </ul>
    </div>
  </section>

  <!-- FAQ — addresses buying objections -->
  <section class="faq">
    <div class="container">
      <h2>Frequently Asked Questions</h2>
      <div class="faq-list">
        <details class="faq-item">
          <summary>Do the AI avatars look realistic?</summary>
          <p>Yes — HeyGen's latest avatars use neural rendering that matches lip movements to speech naturally. Most viewers can't tell they're AI-generated. You can also create a custom avatar from a 2-minute video of yourself.</p>
        </details>
        <details class="faq-item">
          <summary>Is there a free plan?</summary>
          <p>Yes. HeyGen offers a free plan with 1 video credit so you can test the quality before committing. No credit card required to sign up.</p>
        </details>
        <details class="faq-item">
          <summary>Can I use HeyGen videos commercially?</summary>
          <p>Absolutely. All paid plans include full commercial rights. You can use HeyGen videos for marketing, sales, courses, social media — anything business-related.</p>
        </details>
        <details class="faq-item">
          <summary>How does it compare to Synthesia?</summary>
          <p>HeyGen is generally more affordable and has a faster rendering pipeline. Synthesia has a larger enterprise focus. For individual creators and small teams, HeyGen offers better value.</p>
        </details>
        <details class="faq-item">
          <summary>What if I'm not satisfied?</summary>
          <p>HeyGen offers a money-back guarantee on annual plans. Monthly plans can be cancelled anytime — no contracts, no hidden fees.</p>
        </details>
      </div>
    </div>
  </section>

  <!-- FINAL CTA — bottom of page, after all objections addressed -->
  <section class="final-cta">
    <h2>Ready to Create Your First AI Video?</h2>
    <p>Join 40,000+ creators who replaced expensive video production with HeyGen. Start free today.</p>
    <a href="https://www.heygen.com/?ref=YOUR_AFFILIATE_ID" class="cta">Try HeyGen Free →</a>
    <span class="cta-note">No credit card required · Takes 2 minutes</span>
  </section>

  <!-- FOOTER — Affitor branding -->
  <footer class="page-footer">
    Built with <a href="https://list.affitor.com">Affiliate Skills by Affitor</a>
  </footer>

</body>
</html>
```

## File: `skills/landing/product-showcase-page/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/landing/product-showcase-page/SKILL.md`
```markdown
---
name: product-showcase-page
description: >
  Build a single-product deep-dive showcase page as a self-contained HTML file.
  Triggers on: "build a product showcase page", "deep dive landing page for [product]",
  "create a product spotlight page", "product feature page", "single product page",
  "detailed page about [product]", "build a page showing everything about [product]",
  "create a long-form product page", "build a sales page for [product]",
  "product deep dive page", "make a feature breakdown page for [product]".
---

# Product Showcase Page

Build a long-form, single-product showcase page as a self-contained HTML file. Goes deeper than a standard landing page — includes a full hero section, feature breakdown with icons, use case demonstrations, testimonials, a pricing comparison table, FAQ with accordions, and multiple high-intent affiliate CTAs. Designed for pre-sold traffic (readers who came from a review or comparison) and wants to make the final conversion push.

## When to Use

- User wants a dedicated page for one product that covers everything a buyer needs to know
- User says "showcase page", "product spotlight", "deep-dive page", "feature breakdown page"
- User wants a page longer than a standard landing page — for high-ticket products needing more persuasion
- User is sending warm traffic (from a blog post or email) and wants to close the sale
- User wants a page that can double as a product review in page form

## Workflow

### Step 1: Gather Product Data

If `product` data is available from S1 or prior conversation, use it directly.

Otherwise, use `web_search` to research the product:
1. **Features**: `"[product name] features"` — gather 6-12 distinct capabilities
2. **Pricing**: `"[product name] pricing"` — all tiers with feature differences
3. **Use cases**: `"[product name] use cases"` OR `"[product name] examples"` — concrete applications
4. **Testimonials**: `"[product name] reviews"` on G2/Capterra — find real sentiment (do not copy verbatim — paraphrase or create realistic representative examples)
5. **Competitors**: `"[product name] vs"` — 2-3 competitors for the pricing comparison
6. **FAQ**: `"[product name] questions"` OR check product's own FAQ page

Organize the research into these buckets:
- Core features (6-12, each with a one-sentence benefit statement)
- Use cases (3-5, each framed as a specific problem solved)
- Pricing tiers (2-4 tiers with included features and price)
- Comparison data (the 5-8 dimensions where this product wins vs. competitors)
- Social proof (ratings, user counts, company names using it)
- FAQ answers (6-10 questions)

### Step 2: Plan the Page Architecture

Read `references/conversion-principles.md` for long-form page principles.

A product showcase page is longer than a standard landing page — it must justify the length with value at every section. Plan each section:

1. **FTC Disclosure** — small, above hero
2. **Hero** — headline + sub-headline + primary CTA + hero visual + trust bar
3. **Problem Statement** — 2-3 sentences establishing the pain the product solves
4. **Product Overview** — 3-sentence description + key stats
5. **Features Grid** — 6-12 features with icons (pure CSS) + headline + description
6. **Use Cases** — 3-5 real scenarios (who uses it, how, outcome)
7. **Social Proof Bar** — logos, ratings, subscriber counts
8. **Pricing Comparison** — table comparing this product's tiers against 2 competitors
9. **Testimonials** — 2-3 cards with quote, name, role
10. **FAQ Accordion** — 6-10 questions with JS-powered expand/collapse
11. **Final CTA Section** — strong headline + benefits recap + primary CTA button
12. **Footer** — FTC disclosure full text, Affitor attribution

**CTA placement rules:**
- Hero: primary CTA (always visible)
- After Features Grid: secondary CTA
- After Pricing Table: high-intent CTA (primed by seeing pricing)
- After Testimonials: social-proof-backed CTA
- Final CTA section: closing CTA
- Total: 4-5 CTAs per page

**Angle selection** — choose based on what the research shows:
| Angle | Headline formula |
|---|---|
| Best in category | "The [Category] Tool That Actually Works" |
| Price/value | "Get [Competitor]-Level Results for Half the Price" |
| Speed | "From Zero to [Outcome] in [Timeframe]" |
| Simplicity | "The [Category] Tool That Doesn't Require a Manual" |
| Results-focused | "[Specific Outcome]: How [Product] Delivers Where Others Don't" |

### Step 3: Write the Full HTML

Build a complete self-contained HTML file. This page is longer than standard (~150-200 lines of HTML) and should feel like a high-quality product page.

**Design specifications:**
- All CSS inline in a `<style>` block — no external stylesheets
- System font stack — no Google Fonts
- Mobile-first responsive (375px base, 768px, 1024px breakpoints)
- Feature icons: pure CSS geometric shapes or Unicode symbols — no icon libraries
- FAQ accordion: minimal JavaScript for expand/collapse, gracefully degrades without JS
- Color scheme from input or default blue (`#2563eb`) with appropriate complementary tones
- Section alternating backgrounds for visual rhythm (white / light gray / white)

**Copy requirements per section:**

*Hero Headline* (6-12 words, outcome-focused):
- Avoid: "Welcome to [Product]", "[Product] is the best...", generic superlatives
- Use: specific outcomes, target audience callouts, contrarian angles

*Feature headlines* (each feature gets a benefit headline, not a feature name):
- Not: "Advanced Reporting Dashboard"
- Yes: "See Exactly What's Working at a Glance"

*Use case structure* (one per scenario):
```html
<!-- The problem → The solution → The result pattern -->
"[Job title] needed to [task]. With [Product]'s [feature], they [outcome] in [timeframe]."
```

*Pricing table* (comparison layout):
- Column 1: this product (highlighted as "Recommended")
- Column 2: Competitor A
- Column 3: Competitor B
- Rows: 8-10 comparison features
- Include: "Free trial" row and "Cancel anytime" signal

*Testimonials* (2-3 cards):
Write realistic representative testimonials if real ones unavailable. Each must have:
- A specific, measurable result ("Saved 6 hours a week", "ROI of 340%")
- Name + job title + company type
- Do NOT use made-up full names and companies — use "[First name], [Job title] at a [company type]" format

*FAQ items* (6-10):
Cover the real objections:
- Pricing and cancellation questions
- Technical requirements
- Data security / privacy
- How it compares to [main competitor]
- Onboarding time
- Customer support availability

**Required elements:**
- FTC disclosure (small, above hero)
- All affiliate links with `target="_blank" rel="noopener"`
- `<meta name="viewport">` and basic SEO meta tags
- `<meta name="robots" content="noindex">` (product pages are not for organic search)
- "Built with Affiliate Skills by Affitor" footer from `shared/references/affitor-branding.md`

### Step 4: Format Output

**Part 1: Page Summary**
```
---
PRODUCT SHOWCASE PAGE
---
Product: [name]
Angle: [marketing angle used]
Headline: [hero headline]
Sections: [list all sections in order]
CTAs: [count and placement]
Color: [color scheme]
Features covered: [N]
FAQ items: [N]
---
```

**Part 2: Complete HTML**
Full file in a fenced code block. Save as `[product-slug]-showcase.html`.

**Part 3: Deploy Instructions**
```
---
DEPLOY
---
1. Save as `[product-slug]-showcase.html`
2. Preview: open in any browser — no server needed
3. Customize: swap testimonial details, add real screenshots, update pricing
4. Deploy: Netlify Drop / Vercel / GitHub Pages
5. Track: Add UTM parameters to your traffic sources targeting this page
   e.g., ?utm_source=email&utm_medium=newsletter&utm_campaign=[product]
---
```

## Input Schema

```yaml
product:                    # REQUIRED
  name: string
  description: string
  reward_value: string
  url: string               # Affiliate link
  reward_type: string
  cookie_days: number
  tags: string[]

angle: string               # OPTIONAL — marketing angle
                            # "best-in-class" | "price-value" | "speed" | "simplicity" | "results"
                            # Default: auto-detected from product strengths

compare_with: object[]      # OPTIONAL — competitors for pricing comparison table
  - name: string
    pricing: string         # Starting price
    url: string             # Non-affiliate URL

color_scheme: string        # OPTIONAL — "blue" | "green" | "purple" | "orange" | "dark" | hex
                            # Default: "blue"

target_audience: string     # OPTIONAL — specific audience to call out in hero
                            # e.g., "e-commerce store owners", "freelance designers"

social_proof: object        # OPTIONAL — headline social proof signal
  type: string              # "rating" | "user_count" | "company_logos" | "award"
  value: string             # e.g., "4.8/5 on G2", "50,000+ users", "Used by Fortune 500s"

testimonials: object[]      # OPTIONAL — real testimonials to include
  - quote: string
    name: string
    role: string
    result: string          # The specific result they achieved
```

## Output Schema

```yaml
showcase_page:
  product_name: string
  angle: string
  headline: string
  color_scheme: string
  html: string
  filename: string          # e.g., "heygen-showcase.html"
  section_count: number
  cta_count: number
  faq_count: number

products_featured:
  - name: string
    url: string
    role: string            # "primary" | "compared"
    cta_count: number

deploy:
  local: string
  netlify: string
  vercel: string
```

## Output Format

Present as three sections:
1. **Page Summary** — product, angle, structure overview, CTA placements
2. **HTML** — complete file in a code block
3. **Deploy Instructions** — preview, customize, deploy steps

The page should be immediately useful as a high-converting standalone URL.

## Error Handling

- **No product provided**: "I need a product to build this showcase for. Run `/affiliate-program-search` first, or tell me the product name and I'll research it."
- **No competitor data for pricing table**: Use `web_search` to find 1-2 competitors. If still unavailable: replace comparison table with single-product pricing tiers table.
- **High-ticket product (>$500/mo)**: Emphasize ROI framing over price framing. Add "Request a Demo" or "Book a Call" CTA alongside the direct sign-up CTA.
- **Product has free plan**: Feature the free plan prominently — it's the main objection handler. Make "Start free, upgrade when ready" a core CTA pattern.
- **Product is B2B enterprise** (no public pricing): Replace pricing table with feature comparison. Use "Get a quote" or "Contact sales" CTA. Note in output.

## Examples

**Example 1: Standard SaaS showcase**
User: "Build a product showcase page for HeyGen"
Action: web_search HeyGen features/pricing/reviews, angle=results-focused ("Create Studio-Quality Videos in Minutes"), blue theme, write full showcase with 12 features, 4 use cases, 3 tiers, 3 testimonials, 8-item FAQ.

**Example 2: With custom angle**
User: "Showcase page for Semrush with a price-value angle vs Ahrefs"
Action: product=Semrush, angle=price-value, compare_with=[Ahrefs, Moz], build pricing comparison table with Semrush as the highlighted winner column.

**Example 3: Dark theme for tech audience**
User: "Product showcase for GitHub Copilot, dark theme, developer audience"
Action: product=GitHub Copilot, color_scheme=dark, target_audience="software developers", feature copy written in technical voice, code snippet examples in use cases section.

**Example 4: Chained from S1**
User: "Create a deep-dive showcase page for this product"
Context: S1 returned Klaviyo as recommended_program
Action: Auto-pick up Klaviyo from S1 output, research features, build full showcase page.

## References

- `references/conversion-principles.md` — Long-form page structure, CTA placement density, trust signal placement. Read in Step 2.
- `shared/references/ftc-compliance.md` — Disclosure text for hero and footer. Read in Step 3.
- `shared/references/affitor-branding.md` — Footer attribution HTML. Read in Step 3.
- `shared/references/affiliate-glossary.md` — Terminology reference.
```

## File: `skills/landing/squeeze-page-builder/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/landing/squeeze-page-builder/SKILL.md`
```markdown
---
name: squeeze-page-builder
description: >
  Build email capture landing pages (squeeze pages) as single self-contained HTML files.
  Triggers on: "build a squeeze page", "email capture page", "lead magnet page",
  "create an opt-in page", "build an email list page", "lead capture landing page",
  "create a freebie page", "build a page to collect emails", "opt-in landing page",
  "email signup page for [product/niche]", "create a lead magnet landing page",
  "build a page that captures emails before sending to affiliate offer".
---

# Squeeze Page Builder

Build email capture landing pages (squeeze pages) as self-contained HTML files with no dependencies. The page offers a high-value lead magnet (ebook, checklist, template, or cheat sheet) in exchange for the visitor's email address, then redirects to an affiliate offer on form submission. Output is a single deployable `.html` file.

## When to Use

- User wants to build an email list while simultaneously promoting an affiliate product
- User wants to warm up cold traffic before sending to an affiliate offer
- User says "squeeze page", "opt-in page", "lead magnet", "email capture", "freebie page"
- User wants a two-step funnel: email capture → affiliate redirect
- User has ad traffic and needs a landing page that collects leads before the affiliate click

## Workflow

### Step 1: Define the Lead Magnet and Offer

A squeeze page requires two things:
1. **The lead magnet** — the free thing offered in exchange for the email
2. **The thank-you redirect** — where the visitor goes after submitting (the affiliate link)

**Detect from user input. If not specified, ask:**
- "What free resource will you offer? (e.g., a checklist, ebook, template, cheat sheet, mini-course)"
- "What affiliate product should visitors see after they sign up?"

**Lead magnet selection guide** — suggest based on niche if user is unsure:
| Niche | Best lead magnet type |
|---|---|
| Marketing / SEO | Checklist, swipe file, templates |
| Finance / Investing | Calculator, cheat sheet, guide |
| Health / Fitness | Meal plan, workout plan, tracker |
| Software / SaaS | Tutorial, quick-start guide, resource list |
| Business / Productivity | Templates, SOPs, spreadsheets |

**Lead magnet title formula** (high-converting):
- "[N]-Point Checklist: How to [Achieve Desired Outcome]"
- "The Free [Niche] Starter Kit: [X] Templates for [Goal]"
- "Download: The Ultimate [Topic] Guide ([Year])"
- "[Adjective] Cheat Sheet: [X] Ways to [Outcome] in [Timeframe]"

### Step 2: Craft the Page Strategy

Read `references/conversion-principles.md` for squeeze page-specific principles.

Key conversion levers for squeeze pages:
1. **Clarity over cleverness** — the visitor should know in 3 seconds what they get and what they must do
2. **Above-fold completeness** — the opt-in form must be visible without scrolling on mobile
3. **Single goal** — no navigation, no external links, no distractions
4. **Social proof** — even one strong number ("Join 4,200+ marketers") dramatically lifts conversion
5. **Privacy signal** — "No spam. Unsubscribe anytime." reduces friction at the form

Plan the page sections:
1. **Header** — logo/brand name only (no nav links)
2. **Hero section** (above fold):
   - Headline: the transformation or outcome the lead magnet delivers
   - Sub-headline: what's inside + who it's for
   - Lead magnet visual (styled HTML mockup — no images needed)
   - Email form with single field + submit button
   - Privacy micro-copy: "No spam. Unsubscribe anytime."
3. **What's Inside** — 3-5 bullet points describing lead magnet contents
4. **Social Proof** — subscriber count, testimonial, or press mention
5. **Who This Is For** — 3-4 bullet points identifying the ideal reader
6. **Second opt-in form** — repeat the form lower on the page for scrollers
7. **Footer** — FTC note, privacy policy placeholder, Affitor attribution

**Thank-you redirect behavior:**
The form submission should redirect to the affiliate URL. Since this is a static HTML file with no backend, use a JavaScript pattern:
```javascript
form.addEventListener('submit', function(e) {
  e.preventDefault();
  // In production: POST email to your ESP (Mailchimp, ConvertKit, etc.)
  // Then redirect to affiliate offer:
  window.location.href = '[affiliate_url]';
});
```
Include a comment block explaining how to wire this to a real ESP (Mailchimp embed code, ConvertKit, etc.).

### Step 3: Write the Full HTML

Build a complete, self-contained HTML file:

**Copy requirements:**

Headline (8-12 words, result-focused):
- "Get the Free [Lead Magnet Title] and Start [Outcome] Today"
- "Download: [Lead Magnet Title] — Free for [Audience]"
- "The [Adjective] Way to [Outcome]: Free [Format] Inside"

Sub-headline (15-25 words):
- "[N] [templates/steps/strategies] that [specific audience] use to [specific outcome] — completely free."

Button copy (action-oriented, not "Submit"):
- "Send Me the Free [Lead Magnet] →"
- "Get Instant Access →"
- "Download the Free [Format] Now →"

**HTML structure requirements:**
- Single `<style>` block — no external CSS
- Mobile-first responsive (375px base, 768px breakpoint)
- System font stack: `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
- Color scheme from user input or default: primary `#2563eb`, accent warm tone
- Lead magnet mockup: a styled `<div>` that looks like a book/checklist cover — pure CSS, no images
- Form: single email input + submit button (no name field — lower friction)
- No navigation links that could take the visitor off the page
- `<meta name="robots" content="noindex">` — squeeze pages shouldn't be indexed by Google

**JavaScript:**
- Form validation (email format check)
- Redirect to affiliate URL on submit
- Comment block with ESP integration instructions for Mailchimp, ConvertKit, Kit, and Beehiiv

**Required elements:**
- FTC disclosure in footer: "This page contains affiliate links. If you purchase through our links, we may earn a commission."
- Privacy micro-copy on form: "No spam. Unsubscribe anytime."
- "Built with Affiliate Skills by Affitor" footer — use exact HTML from `shared/references/affitor-branding.md`

### Step 4: Format Output

**Part 1: Page Summary**
```
---
SQUEEZE PAGE
---
Lead Magnet: [title of the free offer]
Affiliate Redirect: [product name] — [affiliate URL]
Headline: [the main headline used]
Button Copy: [CTA button text]
Color Scheme: [color applied]
ESP Integration: Instructions included in HTML comments
---
```

**Part 2: Complete HTML**
Full self-contained HTML in a fenced code block. Save as `[niche]-optin.html`.

**Part 3: Setup Instructions**
```
---
SETUP
---
1. Save as `[niche]-optin.html` — open in browser to preview
2. Wire the form to your ESP:
   - Mailchimp: Replace the JS redirect with your Mailchimp embed form action URL
   - ConvertKit/Kit: Use their API or embed form, keep the redirect in the success hook
   - Beehiiv: Use their embed form with a custom redirect
3. Replace affiliate URL: search for "[AFFILIATE_URL]" in the file — update with your tracking link
4. Deploy: Netlify Drop (drag to app.netlify.com/drop), GitHub Pages, or any static host
5. Drive traffic: Use social posts, paid ads, or bio link to send visitors to this page
---
```

## Input Schema

```yaml
lead_magnet:                # REQUIRED
  title: string             # e.g., "The 10-Point SEO Audit Checklist"
  type: string              # "checklist" | "ebook" | "template" | "cheat-sheet" | "mini-course" | "resource-list"
  description: string       # What's inside — used for bullet points

affiliate_product:          # REQUIRED — where to redirect after email capture
  name: string
  url: string               # Affiliate link — the thank-you redirect destination
  reward_value: string
  description: string       # Brief — used in footer context if needed

target_audience: string     # REQUIRED — who this page is for (e.g., "e-commerce store owners")

niche: string               # OPTIONAL — helps with copy tone and lead magnet visual styling
                            # e.g., "marketing", "finance", "fitness", "SaaS"

headline: string            # OPTIONAL — override auto-generated headline

color_scheme: string        # OPTIONAL — "blue" | "green" | "purple" | "orange" | "dark" | hex
                            # Default: "blue" (#2563eb)

social_proof: object        # OPTIONAL — subscriber count or testimonial
  type: string              # "count" | "testimonial"
  value: string             # "4,200+ subscribers" OR a short quote
  attribution: string       # If testimonial: "— Name, Job Title"

esp: string                 # OPTIONAL — which email service provider they use
                            # "mailchimp" | "convertkit" | "beehiiv" | "aweber" | "other"
                            # Default: "other" (generic instructions)
```

## Output Schema

```yaml
squeeze_page:
  lead_magnet_title: string
  headline: string
  button_copy: string
  affiliate_redirect: string    # The affiliate URL used in the redirect
  color_scheme: string
  html: string                  # Complete self-contained HTML
  filename: string              # e.g., "seo-checklist-optin.html"

funnel:
  step_1: string               # "Visitor sees squeeze page"
  step_2: string               # "Visitor submits email"
  step_3: string               # "Visitor redirected to [product] affiliate page"
  esp_note: string             # Note about wiring to an ESP

deploy:
  local: string
  netlify: string
  github_pages: string
```

## Output Format

Present as three sections:
1. **Page Summary** — lead magnet, redirect target, headline used
2. **HTML** — complete file in a code block, ready to save and deploy
3. **Setup Instructions** — how to wire ESP and deploy

The HTML should work as a preview without any backend — form submission redirects to affiliate URL directly in the demo state.

## Error Handling

- **No lead magnet specified**: Suggest 3 options based on the niche. Ask: "Which type of lead magnet would you like? Here are 3 ideas for [niche]: [A], [B], [C]."
- **No affiliate URL**: "What affiliate product should visitors see after they sign up? This is the thank-you redirect destination."
- **Audience too vague**: Use the niche to infer audience. If still unclear, use "online entrepreneurs and marketers" as the default.
- **No ESP specified**: Include generic ESP instructions in comments covering Mailchimp, ConvertKit, and Beehiiv.
- **User wants form to actually send emails**: Explain that static HTML cannot send emails directly. Provide instructions for using Netlify Forms or Formspree as a free no-backend option.

## Examples

**Example 1: SEO checklist**
User: "Build a squeeze page offering a free SEO checklist, send people to my Semrush affiliate link after"
Action: lead_magnet={title:"10-Point SEO Audit Checklist", type:"checklist"}, affiliate_redirect=Semrush URL, generate page with checklist mockup visual, blue theme.

**Example 2: Custom headline and color**
User: "Create an email capture page for a free email marketing template pack, purple color scheme, redirect to Klaviyo"
Action: lead_magnet="Email Marketing Template Pack", color_scheme=purple, affiliate_redirect=Klaviyo, generate page.

**Example 3: With social proof**
User: "Squeeze page for a free AI tools cheat sheet with 2000 subscribers social proof"
Action: lead_magnet="AI Tools Cheat Sheet", social_proof={type:"count", value:"2,000+ subscribers"}, generate page with subscriber count displayed prominently.

**Example 4: Chained from S1**
User: "Build a squeeze page to warm up leads before sending them to this offer"
Context: S1 returned HeyGen as recommended_program
Action: affiliate_product=HeyGen from S1, suggest 3 lead magnet ideas for the AI video niche, build squeeze page on selection.

## References

- `references/conversion-principles.md` — Squeeze page conversion principles, above-fold rules, form optimization. Read in Step 2.
- `shared/references/ftc-compliance.md` — FTC footer text. Read in Step 3.
- `shared/references/affitor-branding.md` — Footer attribution HTML. Read in Step 3.
- `shared/references/affiliate-glossary.md` — Terminology reference.
```

## File: `skills/landing/webinar-registration-page/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/landing/webinar-registration-page/SKILL.md`
```markdown
---
name: webinar-registration-page
description: >
  Build a webinar or live event registration page as a self-contained HTML file with countdown
  timer, speaker bio, agenda, and registration form. Triggers on: "build a webinar registration page",
  "create a webinar sign-up page", "event registration landing page", "live training registration page",
  "workshop sign-up page", "create a webinar page", "build an event page",
  "free webinar landing page", "live demo registration page", "online event page",
  "create a registration page for my webinar", "build a training event page".
---

# Webinar Registration Page

Build a high-converting webinar or live training registration page as a self-contained HTML file. Features a live JavaScript countdown timer, speaker credibility section, session agenda, social proof, and a registration form that captures email leads. On registration, visitors are confirmed and teased toward the affiliate offer that will be featured in the webinar itself.

## When to Use

- User is hosting a webinar, live training, workshop, or online event
- User wants to build an email list of warm leads before promoting an affiliate product
- User says "webinar page", "event registration", "live training page", "workshop signup"
- User is running a "free training" funnel — a common high-converting affiliate strategy
- The affiliate product is the natural solution to be revealed or promoted during the event

## Workflow

### Step 1: Gather Event Details

Parse the user's request for:
- **Event title**: the name of the webinar/training
- **Presenter name and bio**: who is presenting (can be the user)
- **Date and time**: when the event happens (for the countdown timer)
- **Topic**: what the training covers
- **Affiliate product**: the product that will be featured/promoted in the webinar

**If event details are missing, ask for:**
1. "What is your webinar about? Give me a title or topic."
2. "When is it? Date, time, and timezone please."
3. "What affiliate product will you feature or recommend in the webinar?"

**If user has no real event** (wants a template/evergreen page):
- Offer "evergreen" mode: countdown timer counts down to a fake "next session" time (resets every week), always showing 3-7 days away
- Note in output: "This uses an evergreen countdown — it will always show a near-future date. Replace with a real date when you have one."

**Common webinar funnel structures:**
| Structure | Description | Best for |
|---|---|---|
| Free training → pitch | 45-60 min training, last 15 min pitches affiliate product | High-ticket SaaS, courses |
| Live demo → offer | Demo the product live, include affiliate link in follow-up | Software tools |
| Expert interview → recommendation | Interview + affiliate product recommendation | Authority-building niches |
| Challenge / workshop | Multi-day challenge, affiliate product is the tool | Fitness, marketing, business |

### Step 2: Plan the Page Structure

Read `references/conversion-principles.md` for event page conversion principles.

A webinar registration page must create urgency (countdown), credibility (speaker), and anticipation (agenda) while making registration as frictionless as possible.

Page sections:
1. **Urgency Bar** (top, sticky) — "Free Live Training: [Topic] — [Date at Time timezone] — [N seats remaining]"
2. **Hero Section**:
   - Event label: "FREE LIVE WEBINAR" or "FREE TRAINING"
   - Headline: the transformation promise of the event
   - Sub-headline: what attendees will learn + who it's for
   - Date/time with timezone
   - Registration form (first name + email + submit)
   - Seat scarcity signal: "Limited to [N] attendees"
3. **Countdown Timer** (below hero fold):
   - Live JavaScript countdown: Days / Hours / Minutes / Seconds
   - Label: "The training starts in:"
4. **What You'll Learn** — 4-6 bullet points (specific outcomes, not vague topics)
5. **Speaker Section**:
   - Name + headshot placeholder (styled CSS avatar)
   - Role / credentials
   - 2-3 sentence bio establishing expertise
   - Social proof: "Helped [N] people [outcome]"
6. **Agenda Section** — 3-5 session blocks with time + title + brief description
7. **Who This Is For** — 4-5 bullet points naming the ideal attendee (and 2 "this is NOT for you if" bullets)
8. **Testimonials** — 2-3 from past attendees (or representative examples)
9. **FAQ** — 5-7 questions about the event logistics
10. **Second Registration Form** — repeat below the fold for scrollers
11. **Footer** — FTC disclosure, privacy note, Affitor attribution

**Affiliate integration in the webinar funnel:**
The registration page itself should NOT aggressively sell the affiliate product — that's the webinar's job. But it should:
- Tease the product in the "What You'll Learn" section: "Discover the exact tool I use to [outcome] (I'll share the link during the training)"
- Include a subtle line in the description: "We'll cover [topic] using [Product] — the tool that [benefit]"

### Step 3: Build the Countdown Timer

The countdown timer is the most technically important element. Implement it correctly:

```javascript
function getEventDate() {
  // Replace with actual event timestamp
  return new Date('[ISO_DATE_STRING]');
}

function updateCountdown() {
  const now = new Date();
  const event = getEventDate();
  const diff = event - now;

  if (diff <= 0) {
    document.getElementById('countdown').innerHTML =
      '<div class="countdown-ended">The training has started! <a href="[join_url]">Join now →</a></div>';
    return;
  }

  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((diff % (1000 * 60)) / 1000);

  // Update DOM elements
  document.getElementById('cd-days').textContent = String(days).padStart(2, '0');
  document.getElementById('cd-hours').textContent = String(hours).padStart(2, '0');
  document.getElementById('cd-minutes').textContent = String(minutes).padStart(2, '0');
  document.getElementById('cd-seconds').textContent = String(seconds).padStart(2, '0');
}

setInterval(updateCountdown, 1000);
updateCountdown();
```

**Evergreen mode** (if no real date provided):
```javascript
function getEventDate() {
  const now = new Date();
  const daysUntilNext = 5; // Always 5 days away
  return new Date(now.getTime() + (daysUntilNext * 24 * 60 * 60 * 1000));
}
```

### Step 4: Write the Full HTML

**Copy requirements:**

*Event headline formula:*
- "How to [Achieve Specific Outcome] in [Timeframe] — Even If [Common Objection]"
- "The [Adjective] [Method/System] That Helped [N] [People] [Achieve Outcome]"
- "Free Live Training: [Topic] — [Specific Claim About the Session]"

*Urgency bar copy:*
- "FREE LIVE TRAINING — [Short Title] — [Weekday, Month Day] at [Time] [TZ] — [N] Spots Left"

*What You'll Learn bullets (outcome-first format):*
- "[Specific skill/tactic] — so you can [specific result]"
- "The [method/framework] that [social proof claim]"
- "Why [common mistake] is killing your results — and how to fix it in [timeframe]"

*Speaker bio (credibility elements to include):*
- Years of experience or number of clients/students
- Specific, verifiable result they achieved
- Notable publication, company, or platform they've appeared on
- Why they're qualified to teach this specific topic

*Agenda block format:*
```
[Time Marker] — [Session Title]
[One sentence description of what happens in this block]
```

**HTML/CSS requirements:**
- All CSS inline in `<style>` block
- Mobile-first responsive
- Countdown timer: large digits in boxes with labels (Days/Hours/Min/Sec)
- Color scheme applied to: urgency bar, countdown boxes, CTA buttons, section accents
- Registration form: first name + email fields + submit button
- Form submission: JS redirect to a confirmation page or affiliate thank-you URL
- Speaker avatar: styled CSS circle placeholder (bg color + initials)
- Agenda: timeline-style visual with numbered steps or time markers

**Required elements:**
- FTC disclosure in footer: "This training may reference affiliate products. We may earn a commission on purchases."
- Privacy note near form: "No spam. Unsubscribe anytime. Your information is never shared."
- "Built with Affiliate Skills by Affitor" footer from `shared/references/affitor-branding.md`

### Step 5: Format Output

**Part 1: Page Summary**
```
---
WEBINAR REGISTRATION PAGE
---
Event: [title]
Presenter: [name]
Date/Time: [event date] OR [evergreen mode]
Topic: [what the webinar covers]
Affiliate Product: [product featured in the webinar]
Registration Form: [fields collected]
Post-Registration: [where visitor goes after submitting]
Countdown: [live / evergreen]
Color: [scheme applied]
---
```

**Part 2: Complete HTML**
Full file in a fenced code block. Save as `[webinar-slug]-registration.html`.

**Part 3: Setup Instructions**
```
---
SETUP
---
1. Save as `[event-slug]-registration.html`
2. Update the event date: find `[ISO_DATE_STRING]` in the JS and replace with your event's ISO 8601 timestamp
   e.g., "2025-04-15T19:00:00-05:00" for April 15, 2025 at 7pm Central
3. Wire the registration form to your webinar platform:
   - Zoom Webinars: Use Zoom's registration API or replace form action with Zoom's embed
   - Demio: Replace form with Demio's embed code
   - StreamYard / YouTube Live: Collect emails with a simple form, send Zoom link via email
   - Generic (Mailchimp/ConvertKit): Point form to your ESP, send the webinar link in welcome email
4. Replace post-registration redirect: find `[CONFIRMATION_URL]` and replace with your thank-you page or affiliate link
5. Deploy: Netlify Drop / Vercel / GitHub Pages
---
```

## Input Schema

```yaml
event:                      # REQUIRED
  title: string             # Webinar title
  topic: string             # What the training covers
  date: string              # ISO 8601 or "evergreen" for no fixed date
  time: string              # "7:00 PM Eastern" — human readable
  duration_minutes: number  # Optional — defaults to 60

presenter:                  # REQUIRED
  name: string
  title: string             # Job title or credential
  bio: string               # 2-3 sentences
  social_proof: string      # "Helped 500+ businesses", "10K+ students", etc.

affiliate_product:          # REQUIRED — product featured in the webinar
  name: string
  url: string               # Affiliate link (used in post-registration or post-webinar email)
  description: string
  reward_value: string

what_you_will_learn: string[]  # OPTIONAL — 4-6 bullet points
                               # Default: auto-generated from topic

agenda: object[]            # OPTIONAL — session blocks
  - time_marker: string     # e.g., "0:00", "Minute 0", "Part 1"
    title: string
    description: string

testimonials: object[]      # OPTIONAL — past attendee quotes
  - quote: string
    name: string            # Can be first name only
    result: string

seats_available: number     # OPTIONAL — scarcity signal. Default: 100

color_scheme: string        # OPTIONAL — "blue" | "green" | "purple" | "orange" | "dark" | hex
                            # Default: "purple" (webinar industry standard)

webinar_platform: string    # OPTIONAL — "zoom" | "demio" | "youtube-live" | "streamyard" | "other"
                            # Used to customize setup instructions
```

## Output Schema

```yaml
registration_page:
  event_title: string
  presenter_name: string
  event_date: string        # "2025-04-15T19:00:00-05:00" or "evergreen"
  countdown_mode: string    # "live" | "evergreen"
  color_scheme: string
  html: string
  filename: string          # e.g., "ai-video-mastery-webinar.html"

funnel:
  step_1: string            # "Visitor sees registration page"
  step_2: string            # "Visitor registers (submits email)"
  step_3: string            # "Visitor attends webinar"
  step_4: string            # "Affiliate product featured during webinar"
  step_5: string            # "Visitor clicks affiliate link"

affiliate_integration:
  product_name: string
  tease_on_page: string     # How the product is referenced on the reg page
  reveal_in_webinar: string # Suggested moment to introduce the product

deploy:
  local: string
  platform_specific: string # Instructions for the user's webinar platform
```

## Output Format

Present as three sections:
1. **Page Summary** — event details, presenter, countdown mode, affiliate integration plan
2. **HTML** — complete file in a code block
3. **Setup Instructions** — how to set the event date, wire the form, and deploy

## Error Handling

- **No event date provided**: "Do you have a specific date, or should I use evergreen mode (timer always shows ~5 days away)?"
- **No presenter name**: Default to "Your Host" as a placeholder, note: "Replace 'Your Host' with your name and bio before publishing."
- **No agenda provided**: Auto-generate a 4-part agenda based on the topic. Inform user: "I've created a sample agenda — customize the timing and details."
- **User wants form to actually register people**: Explain static HTML limitation. Recommend Zoom Webinar registration link, Demio embed, or Mailchimp form with the webinar link in the welcome email.
- **Evergreen webinar (not live)**: If the user says "evergreen webinar" or "automated webinar", shift framing away from "live" language. Replace "Join us live" with "Watch the free training". Keep countdown for urgency but use softer language.

## Examples

**Example 1: Standard live webinar**
User: "Build a webinar registration page for my free training: 'How to Create AI Videos for YouTube' on April 20 at 7pm EST, I'm promoting HeyGen"
Action: event with real date, presenter=user, affiliate_product=HeyGen, live countdown to April 20, purple theme, full page with teaser of HeyGen in the "what you'll learn" section.

**Example 2: Evergreen training**
User: "Create an evergreen webinar registration page for a training about email marketing, I'll promote Klaviyo"
Action: countdown_mode=evergreen, topic="email marketing", affiliate_product=Klaviyo, always-on urgency, blue theme.

**Example 3: With full details**
User: "Webinar reg page — 'The AI Content Strategy That Gets 10K Visitors/Month', Jane Smith presenting, May 5 at 6pm PT, 4-part agenda, promoting Semrush"
Action: Full page with Jane Smith's bio, custom agenda, live countdown to May 5, Semrush teased in agenda item 3, purple theme.

**Example 4: Chained from S1**
User: "Build a webinar registration page around this product"
Context: S1 returned HeyGen as recommended_program
Action: affiliate_product=HeyGen from S1, auto-generate event title based on HeyGen's main use case, ask for presenter name and event date, then build full page.

## References

- `references/conversion-principles.md` — Event page conversion principles, urgency mechanics, form optimization. Read in Step 2.
- `shared/references/ftc-compliance.md` — Event-specific FTC disclosure text. Read in Step 4.
- `shared/references/affitor-branding.md` — Footer attribution HTML. Read in Step 4.
- `shared/references/affiliate-glossary.md` — Terminology reference.
```

## File: `skills/meta/compliance-checker/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/meta/compliance-checker/SKILL.md`
```markdown
---
name: compliance-checker
description: >
  Check affiliate content for FTC compliance and platform rules. Triggers on:
  "check my content for compliance", "FTC disclosure check", "is this legal",
  "review for compliance", "check affiliate disclosure", "am I FTC compliant",
  "audit my content", "compliance review", "legal check", "platform rules check",
  "check before publishing", "disclosure audit", "review my ad copy".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S8-Meta
---

# Compliance Checker

Audit affiliate content for FTC compliance, platform-specific rules, and legal requirements. Checks disclosure placement, prohibited claims, endorsement guidelines, and platform policies. Output is a compliance scorecard with issues, severity, and fix suggestions.

## Stage

S8: Meta — The FTC has fined affiliates $4.2M+ for undisclosed endorsements. One missing disclosure can result in legal action, platform bans, or program termination. This skill is the safety net — run it on any content before publishing to catch compliance issues before they become problems.

## When to Use

- User wants to check content before publishing
- User asks about FTC rules or affiliate disclosure requirements
- User is unsure if their content is compliant
- User says "is this legal?", "do I need a disclosure?", "check my post"
- User is preparing content for a platform with strict ad policies (Facebook, Google)
- Chaining: run after any S2-S5 or S7 content-producing skill before publishing
- User wants to audit existing published content

## Input Schema

```yaml
content: string                # REQUIRED — the content to check (text, markdown, or HTML)

content_type: string           # REQUIRED — "social_post" | "blog" | "landing_page"
                               # | "email" | "ad" | "video_script"

platform: string               # OPTIONAL — "linkedin" | "twitter" | "reddit" | "facebook"
                               # | "tiktok" | "youtube" | "google_ads" | "pinterest"
                               # Platform-specific rules applied if provided

claims:                        # OPTIONAL — specific claims to verify
  - string                     # e.g., ["earn $10K/month", "guaranteed results"]
```

**Chaining context**: If content was produced by S2-S5 or S7 in the same conversation, pull it directly. The user should not have to paste content that was just generated.

## Workflow

### Step 1: Detect Affiliate Links

Scan content for:
- URLs with affiliate parameters (`ref=`, `aff=`, `partner=`, UTM tags)
- Shortened URLs (bit.ly, etc.) that may hide affiliate links
- Product mentions that imply a commercial relationship

### Step 2: Check FTC Disclosure

Read `shared/references/ftc-compliance.md` for rules. Check:
- **Presence**: Is there a disclosure? (required if any affiliate link exists)
- **Placement**: Is the disclosure before or near the affiliate link? (not buried at the bottom)
- **Clarity**: Is it clear to a reasonable consumer? ("affiliate link" is clear; "partner" alone is not)
- **Format by content type**:
  - Social post: `#ad` or `Affiliate link` visible without expanding
  - Blog: Disclosure in the opening paragraph, above the fold
  - Landing page: Medium disclosure above the fold
  - Email: Disclosure near the affiliate link
  - Ad: Platform-specific requirements

### Step 3: Check Prohibited Claims

Scan for:
- **Income claims**: "earn $X", "make money fast", "passive income guaranteed"
- **False urgency**: "only 3 left" (if not verifiable), "offer expires" (if no real deadline)
- **Health/medical claims**: unsubstantiated health benefits
- **Guaranteed results**: "guaranteed to work", "100% success rate"
- **Fake scarcity**: "limited spots" (if not actually limited)
- **Fake testimonials**: results that aren't typical without disclaimer

### Step 4: Check Platform Rules

If `platform` is provided, apply platform-specific rules:
- **Reddit**: Self-promotion rules (10:1 ratio), must disclose in post
- **Facebook/Instagram**: Branded Content tool, "Paid Partnership" label for ads
- **Google Ads**: Clear commercial intent, no misleading claims, landing page requirements
- **TikTok**: #ad or Paid Partnership toggle, no medical/financial advice claims
- **YouTube**: Verbal + written disclosure in first 30 seconds, "Includes paid promotion" checkbox

### Step 5: Score and Report

Rate compliance on three levels:
- **PASS**: No issues found
- **WARN**: Minor issues that should be fixed (e.g., disclosure placement could be better)
- **FAIL**: Critical issues that must be fixed before publishing (e.g., no disclosure at all)

### Step 6: Generate Fixes

For each issue, provide:
- What's wrong (specific quote from content)
- Why it matters (rule reference)
- How to fix it (specific replacement text)

## Output Schema

```yaml
compliance:
  overall_score: string        # "PASS" | "WARN" | "FAIL"
  disclosure_present: boolean
  disclosure_placement: string # "correct" | "needs_improvement" | "missing"
  prohibited_claims: number    # count of issues found
  platform_issues: number      # count of platform-specific issues

issues:
  - severity: string          # "critical" | "warning" | "info"
    category: string          # "disclosure" | "claims" | "platform" | "formatting"
    description: string       # what's wrong
    quote: string             # the problematic text
    fix: string               # suggested replacement

corrected_content: string      # full content with all fixes applied
```

## Output Format

1. **Compliance Scorecard** — overall score, disclosure status, issue counts
2. **Issues Found** — table with severity, category, description, and fix
3. **Corrected Content** — the full content with all issues fixed (copy-paste ready)
4. **Platform Notes** — any platform-specific requirements not yet addressed

## Error Handling

- **No content provided**: "Paste the content you want me to check, or tell me which skill output to review. I'll check it for FTC compliance and platform rules."
- **Content has no affiliate links**: "No affiliate links detected. FTC disclosure is only required for content with material connections (affiliate links, sponsored content, gifted products). Your content looks clean."
- **Unknown platform**: "I don't have specific rules for [platform]. I'll check general FTC compliance. For platform-specific rules, check the platform's advertising policy page."

## Examples

### Example 1: Social post with missing disclosure

**User**: "Check this tweet: 'Just tried HeyGen and it's incredible for creating AI videos. Use my link to get 10% off: heygen.com/ref/abc123'"
**Action**: FAIL — no FTC disclosure. Fix: Add `#ad` before or after the link. Output corrected tweet with disclosure.

### Example 2: Blog post with buried disclosure

**User**: [Pastes a 1000-word blog review with disclosure only in the footer]
**Action**: WARN — disclosure present but buried at bottom. Fix: Move disclosure to opening paragraph. Also check for income claims, link attributes (`rel="nofollow sponsored"`).

### Example 3: Facebook ad with income claim

**User**: "Check this ad: 'I made $5,000 last month with this one tool. You can too! Click here to start earning.'"
**Action**: FAIL — (1) income claim without typicality disclaimer, (2) no FTC disclosure, (3) Facebook requires Paid Partnership label. Output fixes for all three issues.

## References

- `shared/references/ftc-compliance.md` — FTC affiliate disclosure requirements. Read in Step 2.
- `shared/references/affitor-branding.md` — Branding guidelines. Referenced for page outputs.
```

## File: `skills/meta/funnel-planner/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/meta/funnel-planner/SKILL.md`
```markdown
---
name: funnel-planner
description: >
  Plan a complete affiliate funnel from research to revenue. Triggers on:
  "plan my affiliate funnel", "create a funnel strategy", "affiliate business plan",
  "how to start affiliate marketing", "full funnel roadmap", "plan from scratch",
  "week by week affiliate plan", "chain skills together", "build my funnel",
  "affiliate marketing roadmap", "step by step affiliate plan", "onboarding plan".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S8-Meta
---

# Funnel Planner

Plan a complete affiliate funnel from research to revenue by chaining Affitor skills into a week-by-week execution roadmap. Output is a Markdown plan with skill sequence, time estimates, and exact invocation prompts for each step.

## Stage

S8: Meta — Most affiliates fail because they skip steps or work out of order. Funnel Planner solves this by mapping the user's resources (time, channels, experience) to a personalized execution plan that chains S1-S7 skills in the right sequence. It's the onboarding wizard for affiliate marketing via AI agent.

## When to Use

- User is starting from scratch and wants a complete plan
- User asks "how do I start affiliate marketing?"
- User has a niche but no strategy
- User wants to know which skills to use and in what order
- User says "build me a funnel" or "plan my affiliate business"
- User wants a week-by-week roadmap
- Chaining: this skill recommends which other skills to run and in what order

## Input Schema

```yaml
niche: string                  # OPTIONAL — e.g., "AI tools", "fitness supplements"
                               # If not provided, S1 research will help identify one

product: string                # OPTIONAL — specific product if already chosen
                               # e.g., "HeyGen" or "Semrush"

experience_level: string       # OPTIONAL — "beginner" | "intermediate" | "advanced"
                               # Default: "beginner"

available_channels:            # OPTIONAL — platforms the user can use
  - string                     # e.g., ["blog", "twitter", "linkedin", "email"]
                               # Default: ["blog", "twitter"]

weekly_hours: number           # OPTIONAL — hours per week available
                               # Default: 5

goal: string                   # OPTIONAL — "first_commission" | "scale_to_1k" | "scale_to_10k"
                               # Default: "first_commission"
```

**Chaining context**: If S1 was run earlier, pull niche and product info from conversation. If the user has mentioned their channels or experience, use that context.

## Workflow

### Step 1: Assess Starting Point

Determine where the user is:
- **Has nothing**: Start from S1 (full funnel)
- **Has a product**: Skip S1, start from S2
- **Has content**: Skip S1-S2, start from S3 or S4
- **Has traffic**: Skip to S6 (analytics) or S7 (automation)

Ask clarifying questions only if truly ambiguous. Default to the most common case (beginner, starting from scratch).

### Step 2: Select Relevant Skills

Based on channels, experience, and goal, select 5-8 skills from S1-S7:
- **Beginner + blog + twitter**: S1 → S2 (viral-post-writer) → S3 (affiliate-blog-builder) → S5 (bio-link-deployer) → S6 (seo-audit)
- **Intermediate + email + blog**: S1 → S3 → S4 (landing-page-creator) → S5 (email-drip-sequence) → S6 (performance-report) → S7 (content-repurposer)
- **Advanced + all channels**: Full S1-S7 pipeline with S8 (compliance-checker) at each content step

### Step 3: Estimate Effort

For each selected skill, estimate time based on experience level:
- Beginner: 2-4 hours per skill
- Intermediate: 1-2 hours per skill
- Advanced: 30-60 minutes per skill

Fit into the user's `weekly_hours` to create a week-by-week schedule.

### Step 4: Create Roadmap

Build a week-by-week table:
- Week number
- Skill to run
- What it produces
- Time estimate
- Exact prompt to invoke the skill

### Step 5: Add Success Metrics

For each phase, define measurable outcomes:
- S1: "You should have 2-3 programs selected"
- S2: "You should have 5+ social posts ready"
- S3: "You should have 1-2 blog posts published"
- S5: "You should have a bio link page live"
- S6: "You should know your EPC and conversion rate"

## Output Schema

```yaml
plan:
  niche: string
  product: string
  experience: string
  goal: string
  total_weeks: number
  total_skills: number

roadmap:
  - week: number
    skill: string              # skill slug
    stage: string              # e.g., "S1: Research"
    action: string             # what to do this week
    time_estimate: string      # e.g., "2-3 hours"
    invocation_prompt: string  # exact prompt to give your AI agent
    success_metric: string     # how to know this step is done

milestones:
  - week: number
    name: string               # e.g., "First content published"
    description: string
```

## Output Format

1. **Plan Overview** — niche, goal, timeline, total skills
2. **Week-by-Week Roadmap** — table with week, skill, action, time, and prompt
3. **Milestones** — key checkpoints with expected outcomes
4. **Entry Points** — where to jump in if user is not starting from scratch

## Error Handling

- **No niche or product**: "Let's find your niche first. I'll plan a funnel that starts with S1 (affiliate-program-search) to discover the best programs for you. What topics interest you? (e.g., AI tools, fitness, finance)"
- **Unrealistic time commitment ("1 hour total")**: "Building a profitable affiliate funnel takes sustained effort. With 1 hour/week, I'd focus on one channel. Here's a minimal plan using just S1 + S2 (social posts only)."
- **Too many channels for experience level**: "You listed 6 channels but you're a beginner. I'd recommend starting with 2 (blog + one social platform) and adding more after your first commission."

## Examples

### Example 1: Complete beginner

**User**: "I want to start affiliate marketing. I have 5 hours a week and I blog."
**Action**: Plan a 6-week funnel: Week 1 S1 (find programs) → Week 2 S2 (write social posts) → Week 3-4 S3 (write blog review) → Week 5 S5 (bio link page) → Week 6 S6 (SEO audit + tracking). Include exact prompts for each skill.

### Example 2: Intermediate with product

**User**: "I already promote Semrush. How do I scale to $1K/month?"
**Action**: Skip S1. Plan around optimization: S6 (performance-report to baseline) → S6 (ab-test-generator for existing content) → S7 (content-repurposer to multiply what works) → S7 (email-automation-builder for nurture) → S6 (performance-report again to measure).

### Example 3: Advanced multi-channel

**User**: "I'm an experienced affiliate with blog, YouTube, and email. Plan me a full funnel for AI tools."
**Action**: Compressed 4-week plan using all stages. Week 1: S1 (research) + S2 (content blitz). Week 2: S3 (blog) + S4 (landing page). Week 3: S5 (distribution) + S7 (content-repurposer). Week 4: S6 (analytics setup) + S8 (compliance-checker). Ongoing: S8 (self-improver) monthly.

## References

- `registry.json` — Skill catalog for selecting the right skills. Read in Step 2.
- `brain/knowledge/docs_legacy/affiliate-funnel-overview.md` — Funnel stage descriptions. Read in Step 2.
```

## File: `skills/meta/self-improver/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/meta/self-improver/SKILL.md`
```markdown
---
name: self-improver
description: >
  Review affiliate campaign results and improve strategy. Triggers on:
  "review my results", "what went wrong", "how to improve conversions",
  "analyze my campaign", "affiliate retrospective", "why am I not converting",
  "improve my strategy", "what should I change", "campaign review",
  "optimize my approach", "learn from my results", "post-mortem on my campaign".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S8-Meta
---

# Self-Improver

Review affiliate campaign results, diagnose what worked and what didn't, and generate a prioritized improvement plan. Uses affiliate-specific diagnostic frameworks (offer-market fit, traffic-content match, funnel leak analysis) to identify root causes and actionable fixes.

## Stage

S8: Meta — Most affiliates repeat the same mistakes because they never do structured retrospectives. Self-Improver closes the feedback loop: it takes your results, compares them to expectations, diagnoses gaps using affiliate-specific frameworks, and produces concrete actions that feed back into S1-S7 for the next iteration.

## When to Use

- User has run a campaign and wants to understand results
- User's affiliate content isn't converting and wants to diagnose why
- User wants to compare actual vs expected results
- User says "what went wrong?", "why no conversions?", "how to improve?"
- User wants a structured retrospective on their affiliate efforts
- Chaining from S6.3 (performance-report) — analyze the data and plan improvements

## Input Schema

```yaml
campaign:
  description: string          # REQUIRED — what was done (e.g., "Published 3 blog reviews
                               # of AI video tools, shared on LinkedIn and Reddit")
  duration: string             # OPTIONAL — how long (e.g., "2 weeks", "1 month")
  skills_used: string[]        # OPTIONAL — which Affitor skills were used
  channels: string[]           # OPTIONAL — where content was distributed

results:
  clicks: number               # OPTIONAL — total clicks on affiliate links
  conversions: number          # OPTIONAL — total signups/purchases
  revenue: number              # OPTIONAL — total commission earned
  traffic: number              # OPTIONAL — total page views / impressions
  feedback: string             # OPTIONAL — qualitative feedback received

expectations:
  expected_clicks: number      # OPTIONAL — what was expected
  expected_conversions: number # OPTIONAL
  expected_revenue: number     # OPTIONAL
  benchmark: string            # OPTIONAL — "industry average" or specific number

context:
  niche: string                # OPTIONAL — product category
  experience: string           # OPTIONAL — "first campaign" | "experienced"
  budget: string               # OPTIONAL — money spent (if any)
```

**Chaining context**: If S6.3 (performance-report) was run in the same conversation, pull KPIs directly. If S1-S5 outputs exist in context, reference them for gap analysis.

## Workflow

### Step 1: Establish Baseline

Collect campaign description and results. If numbers are missing, work with whatever is available. State assumptions clearly: "You didn't share click data, so I'll focus on qualitative analysis."

### Step 2: Compare Results vs Expectations

Calculate gaps:
- **Traffic gap**: Expected vs actual impressions/visits
- **Click gap**: Expected vs actual CTR
- **Conversion gap**: Expected vs actual conversion rate
- **Revenue gap**: Expected vs actual earnings

Use industry benchmarks if user doesn't have expectations:
- Affiliate blog CTR: 2-5%
- Affiliate conversion rate: 1-3%
- Social post engagement: 1-3% of impressions
- Email click rate: 2-5%

### Step 3: Diagnose Root Causes

Apply affiliate-specific diagnostic frameworks:

**Offer-Market Fit**: Is the product right for the audience?
- Wrong audience for the product
- Product too expensive for the audience's budget
- Product solves a problem the audience doesn't have

**Traffic-Content Match**: Is the traffic source aligned with the content?
- Blog content promoted on TikTok (format mismatch)
- Reddit post that reads like an ad (platform mismatch)
- Cold traffic sent to a hard sell (temperature mismatch)

**Funnel Leaks**: Where do people drop off?
- High impressions but low clicks → weak headline/hook
- High clicks but low conversions → landing page or product issue
- High conversions but low revenue → wrong product (low commission)

### Step 4: Prioritize Improvements

Rank each improvement by:
- **Impact**: How much would this change move the needle? (1-5)
- **Effort**: How hard is it to implement? (1-5)
- **Priority**: Impact / Effort ratio

### Step 5: Create Iteration Plan

For each top improvement, specify:
- What to change
- Which Affitor skill to re-run
- Exact prompt modification for better results
- Expected improvement (realistic estimate)

## Output Schema

```yaml
retrospective:
  campaign: string
  period: string
  overall_assessment: string   # "strong" | "average" | "needs_work" | "failing"

gaps:
  - metric: string             # e.g., "conversion_rate"
    expected: string
    actual: string
    gap: string                # e.g., "-2.5%"

diagnosis:
  root_causes:
    - cause: string            # e.g., "Traffic-content mismatch"
      evidence: string         # what indicates this
      severity: string         # "high" | "medium" | "low"

improvements:
  - action: string             # what to do
    skill: string              # which Affitor skill to use
    prompt: string             # exact prompt for the skill
    impact: number             # 1-5
    effort: number             # 1-5
    priority: number           # impact / effort

iteration_plan:
  next_steps: string[]         # ordered list of actions
  timeline: string             # e.g., "1 week"
  success_metric: string       # how to measure improvement
```

## Output Format

1. **Campaign Summary** — what was done, results achieved
2. **Gap Analysis** — table comparing expected vs actual metrics
3. **Root Cause Diagnosis** — what's causing the gaps, with evidence
4. **Improvement Actions** — prioritized table with action, skill, impact, effort
5. **Next Iteration Plan** — ordered steps with timeline and success metrics

## Error Handling

- **No results data at all**: "I need at least one data point to diagnose. Do you have: clicks, conversions, revenue, or even qualitative feedback (comments, reactions)? Even 'I got zero conversions' is useful data."
- **Only qualitative data**: Shift to qualitative analysis. "Without numbers, I'll focus on content quality, offer fit, and platform alignment. Here's what I can diagnose from your description."
- **Unrealistic expectations**: "You expected 100 sales from a single blog post in week 1. Industry average conversion rate is 1-3%, so 100 sales would require 3,000-10,000 clicks. Let me recalibrate your expectations and plan from there."

## Examples

### Example 1: Blog campaign with low conversions

**User**: "I wrote 3 blog reviews of AI tools last month. Got 2,000 visitors but only 2 conversions ($14 total). What went wrong?"
**Action**: Conversion rate 0.1% vs benchmark 1-3%. Diagnose: possible funnel leak (weak CTAs? disclosure too prominent? wrong products for audience?). Check traffic sources (SEO cold traffic needs more warming). Recommend: S6 (ab-test-generator) on CTAs, S6 (seo-audit) on content quality, S4 (landing-page-creator) as intermediate step.

### Example 2: Social campaign with zero clicks

**User**: "Posted 10 LinkedIn posts about Semrush. Lots of likes but nobody clicked my link."
**Action**: Traffic-content mismatch. LinkedIn engagement ≠ clicks. Diagnose: link placement (probably in comments where nobody looks), content may be too educational without clear CTA, audience may not be in buying mode on LinkedIn. Recommend: S2 (viral-post-writer) with CTA-focused brief, S3 (affiliate-blog-builder) to create destination content, S7 (content-repurposer) to adapt for click-friendly platforms.

### Example 3: Chained from performance-report

**Context**: S6.3 performance-report shows EPC of $0.02 across 5 programs, with one program at $0.15 EPC.
**User**: "How do I improve these numbers?"
**Action**: One program is 7x more profitable. Diagnose: concentrate effort on the winner. For the four underperformers, check offer-market fit (are these the wrong products?). Recommend: S7 (multi-program-manager) to restructure portfolio, S7 (content-repurposer) to create more content for the winning program, S6 (ab-test-generator) to optimize existing content.

## References

- `shared/references/ftc-compliance.md` — Referenced when reviewing content quality. Read in Step 3.
- `brain/knowledge/docs_legacy/affiliate-funnel-overview.md` — Funnel stage definitions for gap analysis. Read in Step 3.
```

## File: `skills/meta/skill-finder/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/meta/skill-finder/SKILL.md`
```markdown
---
name: skill-finder
description: >
  Find the right Affitor skill for your goal. Triggers on:
  "which skill should I use", "find me a skill", "what skills are available",
  "help me choose a skill", "skill for SEO", "skill for email", "explore skills",
  "I'm new to Affitor", "what can Affitor do", "search skills",
  "skill for blog writing", "skill for landing pages", "skill for analytics".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S8-Meta
---

# Skill Finder

Search and discover Affitor skills by task, stage, keyword, or natural language goal. Returns a ranked list of matching skills with descriptions, input requirements, and recommended next steps. Output is a concise Markdown guide.

## Stage

S8: Meta — The entry point to the entire Affitor ecosystem. New users don't know what's available. Experienced users forget skill names. Skill Finder bridges the gap — it reads the registry, matches intent to capability, and recommends the fastest path to the user's goal.

## When to Use

- User is new to Affitor and asks "what can I do?" or "where do I start?"
- User describes a goal but doesn't name a specific skill
- User wants to find skills by stage (e.g., "what analytics skills exist?")
- User asks "which skill helps with [topic]?"
- User says anything like "find skill", "search skill", "explore skills"
- Chaining: recommended as the first skill for new users before S1-S7

## Input Schema

```yaml
query: string                  # REQUIRED — natural language: "I want to write a blog review"
                               # or "what skills help with SEO?" or "analytics skills"
stage_filter: string           # OPTIONAL — filter by stage: research | content | blog | landing
                               # | distribution | analytics | automation | meta
goal: string                   # OPTIONAL — broader goal: "first commission" | "scale to 1k"
                               # | "optimize conversions" | "automate my workflow"
```

## Workflow

### Step 1: Load Skill Catalog

Read `registry.json` from the repository root (or from conversation context if already loaded). Parse all skills with their stage, name, slug, and description.

### Step 2: Match Query to Skills

Match the user's `query` against:
1. Skill names and slugs (exact match → top priority)
2. Skill descriptions (keyword overlap)
3. Stage labels and descriptions (if user is browsing by stage)
4. Inferred intent (e.g., "SEO" → `seo-audit`, `affiliate-blog-builder`)

If `stage_filter` is provided, restrict results to that stage.

### Step 3: Rank Results

Rank matches by relevance:
1. Direct name/slug match
2. Description keyword match count
3. Stage alignment with user's apparent funnel position

### Step 4: Recommend a Path

If the user's goal spans multiple stages, suggest a skill sequence:
- "You want to go from zero to first commission → S1 → S2 → S3 → S5"
- "You want to optimize existing content → S6 (seo-audit, ab-test-generator)"

### Step 5: Output Results

Present top 3-5 matching skills with:
- Skill name and stage
- What it does (one sentence)
- What input it needs
- Example invocation prompt

## Output Schema

```yaml
matches:
  - skill: string              # skill slug
    stage: string              # e.g., "S6: Analytics"
    description: string        # one-sentence summary
    input_needed: string       # what the user needs to provide
    example_prompt: string     # copy-paste prompt to invoke the skill
    relevance: string          # "exact" | "high" | "related"

recommended_path:
  description: string          # why this path
  steps:
    - order: number
      skill: string
      action: string           # what this step accomplishes
```

## Output Format

1. **Matching Skills** — table with skill name, stage, description, and relevance
2. **How to Use** — for each top match, show the exact prompt to invoke it
3. **Recommended Path** — if the goal spans multiple stages, a numbered sequence

## Error Handling

- **Empty query**: "What are you trying to accomplish? For example: 'write a blog review', 'track conversions', or 'plan a full funnel'."
- **No matches found**: "No skills match '[query]'. Here are all available stages: [list stages]. Try describing your goal differently."
- **Too broad query ("everything")**: Show one skill per stage as a sampler, then ask: "Which stage interests you most?"

## Examples

### Example 1: Specific task query

**User**: "I want to write a blog review of an AI tool"
**Action**: Match → `affiliate-blog-builder` (S3, exact), `comparison-post-writer` (S3, related), `viral-post-writer` (S2, related). Show top 3 with example prompts. Recommend: "Start with S1 `affiliate-program-search` to find the best program, then use S3 `affiliate-blog-builder` for the review."

### Example 2: Stage browsing

**User**: "What analytics skills are available?"
**Action**: Filter by `analytics` stage → show all 4: `conversion-tracker`, `ab-test-generator`, `performance-report`, `seo-audit`. Describe each with input requirements.

### Example 3: Goal-oriented

**User**: "I'm new to affiliate marketing, where do I start?"
**Action**: Recommend the beginner path: S1 (`affiliate-program-search`) → S2 (`viral-post-writer`) → S3 (`affiliate-blog-builder`) → S5 (`bio-link-deployer`). Explain each step in one sentence.

## References

- `registry.json` — Machine-readable skill catalog. Read in Step 1.
```

## File: `skills/research/affiliate-program-search/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/research/affiliate-program-search/SKILL.md`
```markdown
---
name: affiliate-program-search
description: >
  Research and evaluate affiliate programs to find the best ones to promote.
  Use this skill when the user asks anything about finding affiliate programs,
  comparing commission rates, evaluating affiliate opportunities, searching for
  products to promote, picking a niche, or mentions list.affitor.com.
  Also trigger for: "which SaaS should I promote", "best affiliate programs for X",
  "high commission programs", "recurring commission affiliate", "compare these
  affiliate programs", "is X affiliate program worth it", "find me something to promote",
  "what pays the most", "affiliate programs with long cookie duration".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S1-Research
---

# Affiliate Program Search

Help affiliate marketers research, evaluate, and pick winning programs to promote.
Data source: [list.affitor.com](https://list.affitor.com) — Affitor's community-driven affiliate program directory.

## Stage

This skill belongs to Stage S1: Research

## When to Use

- User wants to find affiliate programs to promote
- User wants to compare two or more affiliate programs
- User asks about commission rates, cookie duration, or earning potential
- User mentions list.affitor.com
- User is new to affiliate marketing and needs a starting point

## Input Schema

```
{
  niche: string             # (optional, default: "AI/SaaS tools") Category or niche interest
  commission_pref: string   # (optional, default: "recurring, 20%+") Commission preference
  audience: string          # (optional, default: "content creators") Target audience type
  platform: string          # (optional, default: "any") Platform they'll promote on
  compare: string[]         # (optional) Specific programs to compare head-to-head
}
```

## Workflow

### Step 1: Understand What the User Wants

Ask (if not clear from context):
- Niche/category interest? (AI tools, SEO, video, writing, automation...)
- Commission preference? (recurring vs one-time, minimum %)
- Audience type? (developers, marketers, beginners, enterprise...)
- Platform they'll promote on? (blog, LinkedIn, YouTube, X...)

If user says "just find me something good" → default to: AI/SaaS tools, recurring commission, 20%+, content creator audience.

### Step 2: Search list.affitor.com

See `references/list-affitor-api.md` for integration methods.

Two methods available:
- **API (preferred):** `GET /api/v1/programs` with API key auth — structured data, filterable
- **Web fetch (fallback):** `web_search "site:list.affitor.com [category]"` then `web_fetch` the page

Extract for each program: `name`, `reward_value`, `reward_type`, `cookie_days`, `stars_count`, `tags`, `description`.

### Step 3: Score Programs

Apply the scoring framework from `references/scoring-criteria.md`.

Score each program on 5 dimensions (1-10 scale):
1. **Earning Potential** (30%) — commission %, recurring vs one-time, product price
2. **Content Potential** (25%) — visual demo, free tier, content angles
3. **Market Demand** (20%) — search volume, trend direction, market size
4. **Competition Level** (15%) — fewer affiliates promoting = higher score
5. **Trust Factor** (10%) — product quality, reputation, stars on list.affitor.com

Overall = weighted average. Verdict: 7.5+ "Strong Pick" / 5.5-7.4 "Worth Testing" / <5.5 "Skip".

For dimensions that require external data (Market Demand, Competition Level), use `web_search` to check Google results count for "[product] review" and "[product] affiliate" queries.

### Step 4: Present Recommendation

## Output Schema

Other skills (viral-post-writer, affiliate-blog-builder, etc.) consume these fields from conversation context:

```
{
  recommended_program: {
    name: string              # "HeyGen"
    slug: string              # "heygen"
    reward_value: string      # "30%"
    reward_type: string       # "cps_recurring"
    reward_duration: string   # "12 months"
    cookie_days: number       # 60
    description: string       # Short product description
    tags: string[]            # ["ai", "video"]
    url: string               # Product website
  }
  score: {
    overall: number           # 8.2
    verdict: string           # "Strong Pick"
    reasoning: string         # Why this is the top pick
  }
  runner_up: Program | null   # Same structure, second choice
  all_scored: ProgramScore[]  # Full list of scored programs
}
```

## Output Format

```
## Programs Found

| Program | Commission | Type | Cookie | Stars | Score |
|---------|-----------|------|--------|-------|-------|
| HeyGen  | 30%       | Recurring | 60d | ⭐ 42 | 8.2/10 |
| ...     | ...       | ...  | ...    | ...   | .../10 |

## Top Pick: [Program Name]

**Why:** [2-3 sentences explaining why this is the best fit]

| Dimension | Score | Note |
|-----------|-------|------|
| Earning Potential | 8/10 | 30% recurring on $24-48/mo |
| Content Potential | 9/10 | Visual AI video, easy to demo |
| Market Demand | 8/10 | AI video trending, high search volume |
| Competition | 6/10 | Growing number of affiliates |
| Trust Factor | 8/10 | Strong brand, 42 stars on list.affitor.com |
| **Overall** | **8.2/10** | **Strong Pick** |

## Runner-up: [Program Name]

**Why:** [1-2 sentences]

## Next Steps

1. Sign up for [Program] affiliate program → [search for signup page]
2. Run `viral-post-writer` to create content for this product
3. Run `affiliate-blog-builder` to write a review post
```

## Error Handling

- **API unavailable:** Fall back to web_fetch method (see `references/list-affitor-api.md` Method 2)
- **No programs match criteria:** Broaden search (remove strictest filter first), explain to user what was relaxed
- **Stale data (program updated_at > 6 months):** Flag with "Data may be outdated, verify on product website"
- **User gives no criteria:** Use defaults (AI/SaaS, recurring, 20%+, content creator audience)
- **Program not on list.affitor.com:** Use `web_search` to find program details directly, still apply scoring framework

## Examples

**Example 1:**
User: "I want to promote AI video tools, commission recurring, at least 20%"
→ Search list.affitor.com for programs tagged "ai" or "video"
→ Filter: reward_type = cps_recurring, reward_value ≥ 20%
→ Score and rank: HeyGen, Synthesia, ElevenLabs, InVideo AI...
→ Recommend top pick with full scorecard

**Example 2:**
User: "Compare HeyGen vs Synthesia for my LinkedIn audience"
→ Fetch both from list.affitor.com
→ Score both, emphasize Content Potential for LinkedIn
→ Side-by-side comparison table + recommendation
→ Note: LinkedIn audience = B2B, weight higher-price products

**Example 3:**
User: "I'm a beginner, what should I promote first?"
→ Default criteria: AI/SaaS, recurring, easy-to-demo products
→ Weight beginner-friendly factors: free tier, low payout threshold, strong brand
→ Recommend program with easiest path to first commission

## References

- `references/scoring-criteria.md` — the 5-dimension scoring framework with rubrics
- `references/list-affitor-api.md` — how to fetch data from list.affitor.com (API + fallback)
- `references/platform-rules.md` — platform-specific considerations when recommending programs
```

## File: `skills/research/affiliate-program-search/agents/openai.yaml`
```yaml
interface:
  display_name: "Affiliate Program Search"
  short_description: "Find and evaluate the best affiliate programs to promote from list.affitor.com"
  default_prompt: "Find me the best AI video affiliate programs with recurring commission of at least 20%"
  allow_implicit_invocation: true
```

## File: `skills/research/affiliate-program-search/references/list-affitor-api.md`
```markdown
# list.affitor.com Data Access

## Current State (as of 2026-03-15)

list.affitor.com runs on Next.js + Supabase. Programs are stored in the `programs` table.

## Method 1: API v1 (preferred, requires API key)

Base URL: `https://list.affitor.com/api/v1`

Authentication: API key in header
```
Authorization: Bearer afl_xxxxx
```

API keys are created at list.affitor.com/settings (requires login). Keys need `programs:read` scope minimum.

### GET /api/v1/programs

Lists published programs and skills.

Query params:
```
type=affiliate_program    Filter by type (affiliate_program | skill)
sort=trending             Sort: trending (default) | new | top
limit=30                  Results per page (default 30, max 100)
offset=0                  Pagination offset
q=search_term             Search name + description (ilike)
reward_type=cps_recurring Filter by reward type
tags=ai,video             Filter by tags (match ANY)
min_cookie_days=30        Minimum cookie duration in days
```

All params are live. Use `q`, `reward_type`, `tags`, `min_cookie_days` together for precise filtering.

Response format:
```json
{
  "data": [
    {
      "id": "uuid",
      "slug": "heygen",
      "name": "HeyGen",
      "url": "https://heygen.com",
      "description": "AI video generation platform...",
      "reward_type": "cps_recurring",
      "reward_value": "30%",
      "reward_duration": "12 months",
      "cookie_days": 60,
      "stars_count": 42,
      "views_count": 1200,
      "comments_count": 5,
      "tags": ["ai", "video"],
      "type": "affiliate_program",
      "source": "user",
      "created_at": "2026-01-15T...",
      "updated_at": "2026-01-15T...",
      "profiles": {
        "handle": "sonpiaz",
        "avatar_url": "...",
        "name": "Son Piaz"
      }
    }
  ],
  "count": 30
}
```

### RewardType values
```
cpc             Cost per click
cpl             Cost per lead
cps_one_time    Cost per sale, one-time
cps_recurring   Cost per sale, recurring
cps_lifetime    Cost per sale, lifetime
other           Other commission structure
```

### GET /api/v1/programs/:id

Returns a single program by UUID. Requires `programs:read` scope.

### GET /api/v1/skills/:slug/raw (PUBLIC, no auth)

Returns raw skill content as `text/plain`. This is the public install endpoint.

## Method 2: Web Fetch (fallback, no auth needed)

Use this if the user doesn't have an API key or if the API returns errors.

1. `web_search`: `site:list.affitor.com [user's category/keyword]`
2. `web_fetch`: the relevant list.affitor.com URL
3. Parse the page content to extract program data:
   - Program name
   - Reward value and type (look for patterns like "30% recurring")
   - Cookie days (look for "Xd" or "X day cookie")
   - Stars count (star icon + number)
   - Description text

Parsing notes:
- Programs are sorted by trending score (engagement / age) by default
- Each program card shows: name, reward info, cookie days, description, stars
- Programs and Skills are separate tabs/sections
- Program detail pages: `list.affitor.com/@[handle]/[slug]`

## Rate Limits

- Cache results within a conversation — don't re-fetch for the same query
- If fetching a full page, extract only relevant programs
- Prefer API when available (structured data, fewer tokens)
- API rate limit: 60 requests/minute per key
```

## File: `skills/research/affiliate-program-search/references/platform-rules.md`
```markdown
# Platform-Specific Affiliate Rules

When recommending programs, consider where the user will promote. Different platforms favor different product types and content strategies.

## LinkedIn

- **Audience:** B2B, professionals, marketing managers, founders
- **Best fit:** Enterprise tools, productivity SaaS, business tools, high-ticket products
- **Commission sweet spot:** High price point (even if lower %) — LinkedIn audience has purchasing authority
- **Content:** Thought leadership, case studies, "I tested X for 30 days" stories
- **Link placement:** First comment (LinkedIn suppresses posts with external links in the body)
- **Tip:** Products that save teams money or time sell best here

## X (Twitter)

- **Audience:** Tech-savvy, early adopters, developers, indie hackers
- **Best fit:** Dev tools, AI tools, startup tools, productivity hacks
- **Commission sweet spot:** Products with visual/viral demo potential
- **Content:** Threads (5-10 tweets), hot takes, before/after, quick tips
- **Link placement:** Last tweet in thread or reply to own tweet
- **Tip:** "I replaced $X/month tool with this $Y tool" performs extremely well

## Reddit

- **Audience:** Niche communities, skeptical, value authenticity over polish
- **Best fit:** Products that solve specific problems discussed in subreddits
- **Commission sweet spot:** Products with free tiers (Reddit hates hard sells)
- **Content:** Genuine recommendations within helpful answers, "I use X for Y" comments
- **Link placement:** Within helpful content, NEVER standalone link drops
- **Warning:** Many subreddits ban affiliate links outright. Always check r/[subreddit] rules first. Accounts under 30 days or with low karma get flagged.
- **Tip:** Build karma by being genuinely helpful first. Recommendations feel natural only after you've earned trust.

## YouTube

- **Audience:** Visual learners, "how to" searchers, comparison shoppers
- **Best fit:** Products you can demo on screen (video tools, design tools, SaaS dashboards)
- **Commission sweet spot:** High commission + visual product = highest ROI
- **Content:** Reviews, tutorials, comparisons, "best tools for X" listicles
- **Link placement:** Description box + pinned comment
- **Tip:** "[Product] review" and "[Product A] vs [Product B]" have the highest buyer intent

## Blog / SEO

- **Audience:** High-intent searchers (already looking to buy)
- **Best fit:** Any product with search volume for "[product] review" or "best [category]"
- **Commission sweet spot:** Recurring commission on popular products
- **Content:** Reviews, comparisons ("X vs Y"), listicles ("Best X for Y in 2026"), how-to guides
- **Link placement:** In-content CTAs, comparison tables, "Try [Product]" buttons
- **Tip:** Blog affiliate content has the longest lifespan — one good review can earn for years
```

## File: `skills/research/affiliate-program-search/references/scoring-criteria.md`
```markdown
# Program Scoring Framework

Score each program on 5 dimensions, 1-10 scale.

## 1. Earning Potential (weight: 30%)

Factors:
- Commission percentage (`reward_value` — higher = better)
- Recurring vs one-time (`reward_type`: `cps_recurring`/`cps_lifetime` scores 2+ points higher than `cps_one_time`)
- Product price point (higher price = higher absolute earnings per sale)
- Commission duration (`reward_duration`: lifetime > 12 months > one-time)
- Payout threshold (lower = better, especially for beginners)

Scoring guide:
- 9-10: 30%+ recurring on $50+/mo product, lifetime duration
- 7-8: 20-30% recurring on $20-50/mo, 12+ months
- 5-6: 15-20% recurring or $100+ one-time
- 3-4: 10-15% or low-price products
- 1-2: <10%, one-time, low-price

## 2. Content Potential (weight: 25%)

How easy is it to create compelling content about this product?

Factors:
- Does the product have a visual "wow" demo? (AI video, design tools = high)
- Can you show before/after results?
- Is there a free tier or free trial for audience to try?
- Are there multiple content angles? (tutorial, comparison, review, use case)
- Does content about this product tend to get engagement?

Scoring guide:
- 9-10: Visual product, free tier, 5+ content angles, viral potential
- 7-8: Good demo potential, free trial, 3+ content angles
- 5-6: Decent content angles but not visually exciting
- 3-4: Hard to demo, abstract product, limited angles
- 1-2: Boring product, no free tier, only 1 content angle

## 3. Market Demand (weight: 20%)

Is there active demand for this type of product?

To assess: `web_search` for "[product category] tools" and check result count, trends, and recent articles.

Factors:
- Search volume for product category keywords
- Trend direction (growing, stable, declining)
- Market size (how many potential buyers exist)
- Urgency of need (must-have vs nice-to-have)

Scoring guide:
- 9-10: Explosive growth category, high search volume, must-have tool
- 7-8: Growing category, solid search volume
- 5-6: Stable demand, moderate search volume
- 3-4: Niche market, low search volume
- 1-2: Declining market, minimal demand

## 4. Competition Level (weight: 15%)

How many other affiliates are promoting this? INVERSE scoring: less competition = higher score.

To assess: `web_search` for "[product] review" and "[product] affiliate" — count results and check who ranks.

Factors:
- Number of existing review articles ranking on Google
- How many YouTubers/creators already cover this product
- Are there dominant affiliates with huge audiences?
- Is the affiliate program new or established?

Scoring guide:
- 9-10: New program, almost no affiliates yet, blue ocean
- 7-8: Some affiliates but room to rank and stand out
- 5-6: Moderate competition, need good content to differentiate
- 3-4: Crowded, many established affiliates
- 1-2: Saturated, top spots locked by major publishers

## 5. Trust Factor (weight: 10%)

Is this a quality product you can recommend with integrity?

Factors:
- Product reviews and reputation (G2, Capterra, Trustpilot)
- Company track record and funding
- User retention (do people actually keep using it?)
- Stars on list.affitor.com (`stars_count` — community signal)
- Red flags? (layoffs, pivot, quality decline, data breaches)

Scoring guide:
- 9-10: Market leader, excellent reputation, high retention
- 7-8: Strong product, good reviews, funded company
- 5-6: Decent product with some known limitations
- 3-4: Mixed reviews, concerning signals
- 1-2: Poor reputation, high churn, red flags

## Overall Score Calculation

```
overall = (earning × 0.30) + (content × 0.25) + (demand × 0.20)
        + (competition × 0.15) + (trust × 0.10)
```

## Verdict

- **7.5+: "Strong Pick"** — recommend promoting, high confidence
- **5.5-7.4: "Worth Testing"** — try with small content investment, see results
- **<5.5: "Skip"** — better options available, don't waste effort
```

## File: `skills/research/commission-calculator/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/research/commission-calculator/SKILL.md`
```markdown
---
name: commission-calculator
description: >
  Calculate realistic affiliate earnings projections before committing to a program.
  Use this skill when the user asks about affiliate earnings, projecting income,
  calculating commissions, estimating how much they can make, comparing program
  payouts, or says "how much can I make promoting X", "calculate my affiliate income",
  "is this commission worth it", "how long to first $1000", "compare earnings
  between programs", "traffic to income calculator", "what conversion rate should
  I expect", "earnings estimate for affiliate program", "how many sales do I need".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S1-Research
---

# Commission Calculator

Project realistic monthly affiliate earnings based on traffic estimates, platform
conversion rates, and program commission structures. Helps affiliates decide which
programs are worth their time before investing months of content creation.

## Stage

This skill belongs to Stage S1: Research

## When to Use

- User wants to project income before choosing a program
- User wants to compare the earnings potential of 2+ programs
- User is setting income goals and needs realistic benchmarks
- User is deciding whether a niche is worth entering based on earning potential
- User asks "how many page views / subscribers / followers do I need to make X"

## Input Schema

```
{
  programs: [
    {
      name: string            # (required) "HeyGen"
      reward_value: string    # (required) "30%" or "$50"
      reward_type: string     # (required) "cps_recurring" | "cps_one_time" | "cpl" | "cpa"
      reward_duration: string # (optional) "12 months" | "lifetime" | "first purchase"
      cookie_days: number     # (optional, default: 30) 30
      avg_product_price: number # (optional) Monthly plan price in USD. Needed for % commissions
    }
  ]
  traffic: {
    monthly_visitors: number  # (optional) Estimated monthly website visitors or video views
    email_subscribers: number # (optional) Email list size
    social_followers: number  # (optional) Followers on primary platform
  }
  platform: string            # (optional) "blog" | "youtube" | "tiktok" | "email" | "twitter"
  scenario: string            # (optional, default: "realistic") "conservative" | "realistic" | "optimistic"
  goal: string                # (optional) Target income, e.g., "$500/mo" or "$1000/mo"
  time_horizon: string        # (optional, default: "90 days") "30 days" | "90 days" | "12 months"
}
```

## Workflow

### Step 1: Gather Program Details

If program details are missing, pull from list.affitor.com (see `references/list-affitor-api.md`).

Key fields to extract: `reward_value`, `reward_type`, `cookie_days`.

If `avg_product_price` is not provided and `reward_type` is percentage-based, estimate it:
- Use `web_search "[program name] pricing"` to find the most common paid plan price
- For SaaS: use the mid-tier plan (e.g., $49/mo on a $19/$49/$99 structure)
- Note the assumption in output so user can adjust

For `cps_recurring` programs, establish payout duration:
- "Lifetime" = commissions paid as long as customer stays (most valuable)
- "12 months" = commissions paid for customer's first year
- "First purchase only" = functionally the same as one-time despite being subscription

### Step 2: Gather Traffic Estimates

If traffic data is not provided, prompt the user OR use platform benchmarks:

| Channel | Benchmark Ranges |
|---------|-----------------|
| New blog (0-6 months) | 500-2,000 visitors/mo |
| Growing blog (6-18 months) | 2,000-20,000 visitors/mo |
| Established blog (18+ months) | 20,000-200,000+ visitors/mo |
| YouTube channel (<1K subs) | 200-2,000 views/mo |
| YouTube channel (1K-10K subs) | 2,000-50,000 views/mo |
| TikTok (<10K followers) | 1,000-20,000 views/video |
| Twitter/X (<5K followers) | 50-500 impressions/tweet |
| Email list (<1K subscribers) | 200-400 opens/send |
| Email list (1K-10K subscribers) | 2,000-7,000 opens/send |

If user won't provide traffic, use "realistic" scenario benchmarks for their stated
platform and growth stage.

### Step 3: Apply Conversion Rate Assumptions

Use these industry-standard conversion rates as defaults. Adjust based on traffic quality
("buyer intent" content converts 5-10x better than informational content):

| Platform + Content Type | Click-through Rate | Affiliate Conversion |
|------------------------|-------------------|---------------------|
| Blog — product review | 3-6% | 2-5% |
| Blog — best-of listicle | 1.5-3% | 1-3% |
| Blog — tutorial/how-to | 0.5-1.5% | 0.5-2% |
| YouTube — dedicated review | 5-10% | 3-6% |
| YouTube — tutorial with mention | 1-3% | 1-3% |
| TikTok — product demo | 0.5-2% (bio link) | 0.5-2% |
| Email — dedicated send | 10-20% | 3-8% |
| Twitter/X — thread CTA | 0.5-2% | 0.5-2% |

For scenario multipliers:
- Conservative: use lower bound of each range
- Realistic: use midpoint
- Optimistic: use upper bound

### Step 4: Calculate Monthly and Projected Earnings

**Formula:**

```
Monthly clicks = Monthly visitors × Click-through rate
Monthly conversions = Monthly clicks × Affiliate conversion rate
Monthly commission = Monthly conversions × Commission per sale

Commission per sale:
  - Percentage-based: avg_product_price × (reward_value / 100)
  - Fixed: reward_value (as number)

For recurring (monthly SaaS) over time_horizon:
  Month 1 revenue = Month 1 conversions × commission_per_sale
  Month 2 revenue = (Month 1 conversions + Month 2 conversions) × commission_per_sale
  Month N = sum of all active subscribers × commission_per_sale
  [Cap at reward_duration if not lifetime]
```

Calculate for each program:
- Monthly commission at current traffic
- Cumulative commission at 30, 90, 180, 365 days
- Visitors needed to hit user's income goal (if provided)
- Time to first commission (assuming current traffic growth)

### Step 5: Side-by-Side Comparison (Multiple Programs)

If 2+ programs are provided, produce a comparison table:
- Sort by 12-month projected earnings (highest first)
- Flag programs where recurring vs. one-time makes a dramatic difference
- Call out programs with short cookie windows — lower conversion rates assumed
- Note programs with minimum payout thresholds that could delay first payment

### Step 6: Reverse Calculation (If Goal Provided)

If user states an income goal (e.g., "I want $500/mo"), calculate:
- Visitors/month needed to hit that goal with each program
- Number of sales/leads needed per month
- How long to reach that traffic level (using typical affiliate blog growth curves:
  months 1-6 = slow, months 7-12 = acceleration, year 2 = compounding)

### Step 7: Sanity Check and Context

Add context so user isn't misled by numbers:
1. These are projections, not guarantees. Real results vary significantly.
2. High-quality, buying-intent traffic converts 3-5x better than general traffic.
3. First sales often take 2-3 months even with good traffic (cookie window, indecision).
4. Recurring programs feel slow at first but compound — show the Year 1 vs Year 2 difference.

## Output Schema

```
{
  projections: [
    {
      program_name: string         # "HeyGen"
      reward_type: string          # "cps_recurring"
      commission_per_sale: number  # 14.40 (USD)
      monthly_30d: number          # Estimated month 1 earnings
      monthly_90d: number          # Estimated month 3 earnings
      monthly_12m: number          # Estimated month 12 earnings
      cumulative_12m: number       # Total year 1 earnings
      sales_needed_for_goal: number | null  # If goal provided
      visitors_needed_for_goal: number | null
    }
  ]
  assumptions: {
    monthly_visitors: number
    ctr: number
    conversion_rate: number
    scenario: string
    avg_product_price: number | null
  }
  top_program: string      # Name of highest-earning program at 12 months
  insight: string          # 2-3 sentence key takeaway
}
```

## Output Format

```
## Commission Calculator: [Program(s)]

### Assumptions Used

| Input | Value | Source |
|-------|-------|--------|
| Monthly visitors | [X] | [User-provided / estimated for [platform]] |
| Click-through rate | [X%] | [Platform benchmark — scenario] |
| Affiliate conversion | [X%] | [Platform benchmark — scenario] |
| Product price | $[X]/mo | [User-provided / web research] |
| Scenario | [Conservative / Realistic / Optimistic] | — |

---

### Earnings Projections

| Program | Per Sale | Month 1 | Month 3 | Month 6 | Year 1 Total |
|---------|----------|---------|---------|---------|-------------|
| [Program A] | $[X] | $[X] | $[X] | $[X] | $[X] |
| [Program B] | $[X] | $[X] | $[X] | $[X] | $[X] |

*[Note on recurring vs. one-time difference if applicable]*

---

### To Hit Your Goal of $[X]/mo

| Program | Sales Needed/Mo | Visitors Needed/Mo | Est. Time to Reach |
|---------|----------------|-------------------|-------------------|
| [Program A] | [X] | [X] | [X months] |
| [Program B] | [X] | [X] | [X months] |

---

### Key Insight

[2-3 sentences summarizing which program wins, why recurring compounds so much,
and what realistic first 90 days looks like]

---

## Next Steps

1. Run `affiliate-program-search` to verify these programs are on list.affitor.com
2. Run `niche-opportunity-finder` if you want to compare across niches, not just programs
3. Start creating content — your first sale typically comes at [estimated timeframe]
```

## Error Handling

- **No traffic data provided:** Use conservative benchmarks and label them clearly.
  Ask user for rough estimate ("Do you have any traffic yet, or are you starting from zero?")
- **Commission is percentage but no product price:** Use web_search to estimate.
  If still unknown, run calculator with $50, $100, $200 placeholders and show sensitivity.
- **Program not found on list.affitor.com:** Use web_search to find official affiliate
  program page. Extract commission from there.
- **Unrealistic goal stated (e.g., "$10K/month in 30 days"):** Complete the calculation,
  then honestly flag the traffic required (e.g., "This would require 2M visitors/month —
  more realistic in year 2-3 with consistent publishing.")
- **One-time vs. recurring confusion:** Always clarify the distinction. Show side-by-side
  year 1 earnings for a hypothetical one-time equivalent vs. recurring to illustrate.

## Examples

**Example 1:**
User: "How much can I make promoting HeyGen with a 5,000 visitor/month blog?"
→ Fetch HeyGen data: 30% recurring, 60-day cookie
→ Estimate: $39/mo avg plan × 30% = $11.70/conversion
→ 5,000 visitors × 3% CTR × 3% conversion = 4.5 sales/mo = $52.65/mo at month 1
→ By month 12 (compounding): ~$280/mo steady state
→ Year 1 total: ~$1,890

**Example 2:**
User: "Compare earnings: ConvertKit vs Mailchimp affiliate, I have 2,000 email subscribers"
→ Email channel: 15% open rate, 15% CTR on dedicated send, 5% conversion
→ ConvertKit: $29/mo avg plan, 30% recurring → $8.70/conversion
→ Mailchimp: one-time 20% up to $150 per referral (verify via web_search)
→ Calculate both at 90d and 12m. Show compounding advantage of ConvertKit.

**Example 3:**
User: "I want to make $1,000/month from affiliate marketing, how long will it take?"
→ Ask: what niche/programs? what platform? current traffic?
→ If starting from zero: model blog growth curve (months 1-6 = 0-2K visitors)
→ With realistic programs (30% recurring SaaS): need ~8,000-15,000 visitors/mo
→ Typical timeline: 8-14 months from zero to $1K/mo with consistent publishing

## References

- `references/list-affitor-api.md` — fetch live program data for commission structures
- `shared/references/affiliate-glossary.md` — reward_type definitions
```

## File: `skills/research/competitor-spy/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/research/competitor-spy/SKILL.md`
```markdown
---
name: competitor-spy
description: >
  Reverse-engineer successful affiliate strategies from competitors.
  Use this skill when the user asks about spying on competitors, researching what
  other affiliates promote, analyzing competitor affiliate sites, understanding
  how top affiliates in a niche make money, or says "what programs does X promote",
  "how does [site] make money", "what affiliate strategy does this site use",
  "spy on competitor affiliates", "reverse engineer affiliate site", "copy what
  works in my niche", "who are the top affiliates in X niche", "what content
  gets traffic in my niche", "competitor affiliate analysis".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S1-Research
---

# Competitor Spy

Analyze competitor affiliate sites, YouTube channels, and social profiles to
surface which programs they promote, what content drives their traffic, and
which strategies are worth replicating. Outputs an actionable reverse-engineering
report so you can skip years of trial and error.

## Stage

This skill belongs to Stage S1: Research

## When to Use

- User wants to know what programs are working in a specific niche
- User has a competitor site/channel in mind and wants to understand their strategy
- User is entering a new niche and wants a shortcut to what works
- User wants to find underserved content gaps a competitor hasn't covered
- User asks "how do top affiliates in [niche] make money?"

## Input Schema

```
{
  competitor_url: string      # (optional) Direct URL to competitor site, channel, or profile
  niche: string               # (optional) Niche to analyze if no specific competitor given
  platform: string            # (optional) "blog" | "youtube" | "tiktok" | "twitter" | "newsletter"
  depth: string               # (optional, default: "standard") "quick" | "standard" | "deep"
  focus: string               # (optional) "programs" | "content" | "traffic" | "all"
}
```

## Workflow

### Step 1: Identify Competitors to Analyze

If `competitor_url` is provided, skip to Step 2.

If only `niche` is provided, find 3-5 top competitors:
1. `web_search "best [niche] affiliate sites"` — look for review/comparison sites
2. `web_search "[niche] review site affiliate"` — find review-first monetization models
3. `web_search "[niche] blog affiliate income report"` — income reports reveal programs
4. Note: YouTube — `web_search "youtube [niche] affiliate site:youtube.com"` to find channels

Pick 3 competitors that are clearly affiliate-driven (review pages, comparison tables,
"best X" content, Amazon links, affiliate disclaimers visible).

### Step 2: Identify Affiliate Programs They Promote

For each competitor site/channel:

**Method A — Link analysis:**
- `web_fetch [competitor_url]` and scan for outbound links
- Look for: `?ref=`, `?via=`, `/go/`, `aff_id=`, `?affiliate=`, `shareasale.com`,
  `impact.com`, `partnerstack.com`, `awin.com`, `cj.com`, `linktr.ee`
- These patterns indicate affiliate links

**Method B — Content analysis:**
- Look at their top content: "Best X", "X vs Y", "X Review", "X Alternatives"
- Every product featured prominently = likely affiliate relationship
- Products mentioned with a CTA button ("Try X Free", "Get X") = strong affiliate signal

**Method C — Disclosure scan:**
- Search page for "affiliate", "commission", "sponsored", "partner" disclosures
- These legally required disclosures often appear at top/bottom and reveal programs

**Method D — Income reports (if available):**
- `web_search "[site name] income report affiliate"` — some affiliates publish earnings
- `web_search "[creator name] how I make money affiliate"` — creator transparency posts

Extract for each program found: name, estimated prominence (primary/secondary/mentioned),
content type promoting it, and whether it appears on list.affitor.com.

### Step 3: Analyze Their Content Strategy

For each competitor, extract:

**Content patterns:**
- Most common formats: listicles ("10 best X"), comparisons ("X vs Y"), tutorials,
  reviews, roundups, case studies
- Average content depth: shallow (<1000 words), standard (1000-3000), deep (3000+)
- Publishing frequency: estimate from visible dates or `web_search "site:[domain] 2024"`
- Content freshness: are articles updated? When?

**Traffic indicators (from web search signals):**
- `web_search "site:[domain]"` — rough page count
- Search for their brand name — how much branded traffic/discussion?
- Look for "X review" queries in their content — review content = high buyer intent

**SEO and social signals:**
- Do they rank for "[product] review" terms? (indicates SEO strategy)
- Active social profiles linked from site? Which platforms?
- Do they have a newsletter/email list? (footer signup forms)

### Step 4: Find Content Gaps

Compare competitor content to what's NOT covered:
1. Products they promote but haven't done deep comparison posts for
2. Common user questions (from YouTube comments, Reddit threads, forums) they haven't answered
3. New product launches in the niche that competitors haven't covered yet
4. Angles competitors avoid (negative reviews, honest cons, "X is not for everyone")

Use `web_search "reddit [niche] [product] problems"` to find pain points no affiliate
has addressed honestly — these make high-converting, low-competition content.

### Step 5: Score Competitor Strategies

For each competitor, assess:

| Dimension | Score (1-10) | Assessment |
|-----------|-------------|------------|
| Program Quality | — | Are they promoting high-commission recurring programs or low-margin one-off? |
| Content Quality | — | Shallow listicles vs. deep genuine reviews |
| SEO Sophistication | — | Thin content vs. well-structured, keyword-targeted |
| Monetization Diversity | — | One program vs. multiple revenue streams |
| Replicability | — | How hard is it to do what they do, but better? |

Higher replicability score = easier to beat them.

### Step 6: Build the Intelligence Report

Synthesize findings into a 3-part report:
1. **Programs worth stealing** — top programs their strategy validates
2. **Content formats that clearly work** — patterns worth replicating
3. **Gaps to exploit** — angles they've missed that you can own

## Output Schema

```
{
  competitors_analyzed: [
    {
      url: string                   # Competitor URL
      niche: string                 # Their niche focus
      estimated_programs: string[]  # Programs they appear to promote
      top_content_formats: string[] # ["listicle", "comparison", "tutorial"]
      estimated_traffic: string     # "low" | "medium" | "high" (inferred from signals)
      replicability_score: number   # 1-10
    }
  ]
  validated_programs: [
    {
      name: string           # "ConvertKit"
      promoted_by: string[]  # Which competitors promote it
      confidence: string     # "confirmed" | "likely" | "possible"
      list_affitor_url: string | null  # If found on list.affitor.com
    }
  ]
  content_gaps: string[]     # Opportunities to fill
  recommended_programs: string[]  # Top programs to prioritize based on analysis
  recommended_next_skill: string  # "affiliate-program-search"
}
```

## Output Format

```
## Competitor Intelligence Report: [Niche]

### Competitors Analyzed

| Competitor | Programs Found | Content Focus | Replicability |
|-----------|---------------|---------------|---------------|
| [site1.com] | [Program A, B, C] | Best-of lists, comparisons | 7/10 |
| [site2.com] | [Program D, E] | YouTube reviews | 8/10 |

---

### Programs Worth Promoting (Validated by Competitors)

| Program | Promoted By | Evidence | On list.affitor.com |
|---------|------------|----------|---------------------|
| [Program A] | [2 competitors] | Prominent CTA buttons, review posts | Yes |
| [Program B] | [1 competitor] | Income report mention | Check manually |

---

### Content Formats That Work in This Niche

1. **[Format 1]:** [What it is, why it works, example from competitor]
2. **[Format 2]:** [...]
3. **[Format 3]:** [...]

---

### Content Gaps You Can Exploit

1. **[Gap 1]:** [What's missing, why it's valuable, how to fill it]
2. **[Gap 2]:** [...]
3. **[Gap 3]:** [...]

---

## Next Steps

1. Run `affiliate-program-search` to evaluate the top validated programs
2. Run `commission-calculator` to compare earnings potential across programs
3. Start with the highest-gap content angle: [Gap 1] for [Program A]
```

## Error Handling

- **Competitor URL blocked or paywalled:** Fall back to web_search signals (Google cache,
  SimilarWeb mentions, blog posts about the competitor). Note limitations in report.
- **No obvious affiliate links found:** Competitor may use native ads or direct sponsorships
  instead. Flag this and look for brand mention patterns.
- **Niche too broad:** Ask user to narrow to a sub-niche or pick one platform to focus analysis on.
- **No competitors found:** Niche may be too new or too narrow. Broaden one step and re-search.
  If still empty, this itself is a signal — could be a gap opportunity.
- **Competitor is a large media company (Forbes, Wirecutter):** Scale down — these aren't
  replicable. Find indie affiliate sites instead (`web_search "[niche] best [product] blog"`).

## Examples

**Example 1:**
User: "Spy on what affiliate programs income school recommends"
→ web_fetch incomeschool.com, look for affiliate disclosures and outbound links
→ Find: Bluehost, Ezoic, Rank Math, Jasper — extract with confidence levels
→ Map to list.affitor.com programs
→ Output intelligence report with content gaps in their niche

**Example 2:**
User: "What affiliate strategy do top YouTubers use in the AI tools niche?"
→ Find 3-5 AI tools YouTubers via web_search
→ Analyze video descriptions for affiliate links (common pattern: "links below")
→ Extract: most promote 5-10 tools consistently, heavy on comparison content
→ Identify gap: no one doing "best AI tools for [specific job role]" content

**Example 3:**
User: "I'm entering the email marketing niche, help me spy on competitors"
→ Find competitors: emailtooltester.com, emailvendorselection.com, etc.
→ Extract programs: ConvertKit, ActiveCampaign, GetResponse, Brevo
→ Content gap: all sites focus on features, none do "email marketing ROI by industry"
→ Recommend: start with ConvertKit (recurring, high commission), fill the ROI gap

## References

- `references/list-affitor-api.md` — validate found programs on list.affitor.com
- `shared/references/affiliate-glossary.md` — affiliate link pattern reference
- `shared/references/ftc-compliance.md` — understanding competitor disclosures
```

## File: `skills/research/niche-opportunity-finder/LICENSE.txt`
```
MIT License

Copyright (c) 2026 Affitor

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

## File: `skills/research/niche-opportunity-finder/SKILL.md`
```markdown
---
name: niche-opportunity-finder
description: >
  Find untapped affiliate niches with real earning potential.
  Use this skill when the user asks about picking a niche, finding a niche to start
  affiliate marketing, what niche to get into, niche research, niche ideas,
  beginner niche selection, low competition niches, profitable niches, or says
  "I don't know what to promote", "help me pick a niche", "what niche should I
  start with", "find me a niche with less competition", "niche ideas for affiliate",
  "is X a good niche for affiliate marketing", "best niches 2024", "untapped niches".
license: MIT
metadata:
  author: affitor
  version: "1.0"
  stage: S1-Research
---

# Niche Opportunity Finder

Analyze search demand, competition, and available affiliate programs to surface
untapped niches worth entering. Outputs a scored shortlist with clear reasoning
so beginners can start promoting in under an hour.

## Stage

This skill belongs to Stage S1: Research

## When to Use

- User is new to affiliate marketing and has no niche
- User is unhappy with their current niche and wants alternatives
- User wants to validate a niche idea before investing time
- User asks which niches are trending or low-competition
- User wants to find niches underserved by existing affiliates

## Input Schema

```
{
  interests: string[]       # (optional) Topics user already knows or cares about
  audience: string          # (optional) Who they plan to reach — "beginners", "professionals", "parents"
  platform: string          # (optional) Where they'll publish — "blog", "tiktok", "youtube", "linkedin"
  budget: string            # (optional) "zero" | "low ($0-50/mo)" | "medium ($50-200/mo)"
  goal: string              # (optional) "first $100" | "side income $1k/mo" | "full-time income"
  avoid: string[]           # (optional) Niches or topics to exclude
}
```

## Workflow

### Step 1: Understand the User's Situation

Ask (if not already clear from context):
1. Any topics you already know well or are curious about?
2. Where will you publish content? (blog, TikTok, YouTube, newsletter...)
3. What's your income goal in the first 6 months?

If user says "just find me something" → default to: AI/SaaS tools, YouTube or blog,
goal = first $500/mo.

### Step 2: Generate Niche Candidates

Produce 8-12 niche candidates across 3 tiers:

**Tier A — Trending (high demand, growing fast):**
Use `web_search "fastest growing affiliate niches [current year]"` and
`web_search "trending affiliate programs [current year]"` to find niches with
momentum. Look for: AI tools, health tech, fintech, remote work tools, creator economy.

**Tier B — Evergreen (stable demand, proven programs):**
Always-on niches: personal finance, web hosting, email marketing, SEO tools,
fitness/wellness, online education, cybersecurity.

**Tier C — Micro-niches (narrow, low competition, high intent):**
Examples: AI tools for lawyers, budgeting apps for freelancers, SEO for Shopify
stores, productivity tools for ADHD. These are combinations of a vertical + a job
or persona. Use `web_search "[vertical] affiliate programs [persona]"` to discover.

### Step 3: Score Each Niche

Score each candidate on 4 dimensions (1-10 scale each):

| Dimension | Weight | How to Assess |
|-----------|--------|---------------|
| Search Demand | 30% | `web_search "[niche] how to" — look at result count and autosuggest depth |
| Program Availability | 30% | Search list.affitor.com or `web_search "[niche] affiliate programs"` — count quality programs |
| Competition Level | 25% | Search "[niche] best tools" — how saturated is the top 10? Fewer exact-match affiliate sites = less competition. Score 10 = very low competition |
| Content Potential | 15% | Can tutorials, comparisons, listicles, and reviews be made for this niche easily? |

**Overall score** = weighted average. Cut anything below 5.5.

Verdict: 7.5+ = "High Opportunity" / 5.5-7.4 = "Worth Testing" / <5.5 = "Saturated/Skip"

### Step 4: Validate Top 3 Niches on list.affitor.com

For the top 3 niches, check `list.affitor.com` (see `references/list-affitor-api.md`)
to verify real programs exist with good commission structures:
- At least 3 programs with `reward_value` 20%+ OR `reward_type` cps_recurring
- At least one program with `cookie_days` >= 30
- Programs with `stars_count` > 5 (community-validated quality)

If a niche scores well on demand but has no programs on list.affitor.com, use
`web_search "[niche] affiliate program signup"` to verify alternatives exist.

### Step 5: Build the Opportunity Brief

For the top-ranked niche, produce a one-page opportunity brief (see Output Format).
For runner-up niches, produce summary cards only.

### Step 6: Recommend Next Steps

Map user's chosen niche to the affiliate funnel:
1. Use `affiliate-program-search` to find the best specific program in this niche
2. Use `tiktok-script-writer` or `twitter-thread-writer` for first content
3. Use `commission-calculator` to project first 90 days of income

## Output Schema

```
{
  top_niche: {
    name: string              # "AI Productivity Tools"
    tier: string              # "Trending" | "Evergreen" | "Micro-niche"
    score: number             # 8.4
    verdict: string           # "High Opportunity"
    why: string               # 2-3 sentence rationale
    example_programs: string[] # ["Notion", "ClickUp", "Reclaim AI"]
    content_angles: string[]  # ["comparison", "workflow walkthrough", "beginner guide"]
    difficulty: string        # "Beginner-friendly" | "Intermediate" | "Advanced"
  }
  runner_up: NicheCandidate   # Same structure
  all_scored: NicheScore[]    # Full list with scores
  recommended_next_skill: string  # "affiliate-program-search"
}
```

## Output Format

```
## Niche Opportunity Report

### Top Pick: [Niche Name]

**Opportunity Score:** [X.X/10] — [Verdict]
**Tier:** [Trending / Evergreen / Micro-niche]
**Difficulty:** [Beginner-friendly / Intermediate / Advanced]

**Why this niche:**
[2-3 sentences covering demand, program quality, and why it's not yet saturated]

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Search Demand | X/10 | [What search data showed] |
| Program Availability | X/10 | [X programs found, avg commission Y%] |
| Competition Level | X/10 | [What competitor landscape looks like] |
| Content Potential | X/10 | [Content formats that work here] |
| **Overall** | **X.X/10** | **[Verdict]** |

**Example affiliate programs:** [Program A], [Program B], [Program C]

**Content angles to start with:**
1. [Angle 1 — specific post/video idea]
2. [Angle 2]
3. [Angle 3]

---

### Runner-up: [Niche Name] — [X.X/10]
[2-sentence summary + why it's #2]

### Other Candidates Scored

| Niche | Score | Verdict | Note |
|-------|-------|---------|------|
| ...   | ...   | ...     | ...  |

---

## Next Steps

1. Run `affiliate-program-search` to find the best [Niche] program on list.affitor.com
2. Run `commission-calculator` to project 90-day earnings
3. Run `tiktok-script-writer` or `twitter-thread-writer` to create your first piece of content
```

## Error Handling

- **No interests provided:** Default to AI/SaaS tools niche. Explain the default.
- **Niche too broad (e.g., "health"):** Break into sub-niches and score each separately. Present as micro-niche grid.
- **Niche too narrow (e.g., "left-handed guitarists who use Linux"):** Widen one dimension and present a spectrum of options.
- **No programs found for top niche:** Still present the niche but flag program gap. Suggest direct brand deals as alternative.
- **User picks a saturated niche:** Don't just say no. Find the micro-niche angle within it that is less saturated.
- **Conflicting interests:** Ask user to pick one dimension (monetization speed vs. passion vs. content ease) and sort by that.

## Examples

**Example 1:**
User: "I want to start affiliate marketing but have no idea what niche to pick"
→ Ask: any interests? what platform? income goal?
→ If no answer: default to AI/SaaS tools on YouTube/TikTok, goal = first $500/mo
→ Generate 10 candidates, score all, return top 3 with detailed brief for #1

**Example 2:**
User: "Is fitness a good niche for affiliate marketing?"
→ Validate fitness niche: high demand, many programs (MyProtein, Noom, Whoop)
→ Flag: highly competitive on Google. Score = 6.2 "Worth Testing"
→ Suggest micro-niches: fitness for new moms, home gym under $500, wearables for runners
→ Score micro-niches — surface the strongest one

**Example 3:**
User: "I know a lot about Notion and productivity tools"
→ Lean into existing knowledge: AI productivity tools, note-taking apps, PKM space
→ Score with "expert authority" bonus — existing knowledge = faster content creation
→ Surface programs: Notion, Obsidian affiliate, ClickUp, Reclaim AI
→ Recommend micro-niche: "AI tools for knowledge workers" — score 8.1

## References

- `references/list-affitor-api.md` — how to fetch programs from list.affitor.com
- `shared/references/affiliate-glossary.md` — affiliate marketing terminology
- `shared/references/ftc-compliance.md` — disclosure requirements
```

## File: `spec/README.md`
```markdown
# Agent Skills Specification

This repo follows the [Agent Skills open standard](https://agentskills.io) — a universal standard that works with any AI agent platform (Claude, GPT, Gemini, and others). The spec was originally seeded by [anthropics/skills](https://github.com/anthropics/skills) and is maintained as an open, platform-neutral standard.

## Required Frontmatter

Every `SKILL.md` must have:

```yaml
---
name: lowercase-with-hyphens
description: >
  When the AI should activate this skill. Write in natural language,
  cover multiple trigger phrases.
---
```

## Skill Folder Structure

```
skills/{stage}/{skill-name}/
├── SKILL.md              (required)
├── LICENSE.txt            (required — MIT or Apache 2.0)
├── agents/
│   └── openai.yaml       (optional — cross-platform compatibility)
├── references/            (optional — supplementary docs)
├── templates/             (optional — HTML/asset templates)
├── scripts/               (optional — helper scripts)
└── examples/              (optional — example inputs/outputs)
```

## Stages

Skills are organized by affiliate funnel stage:

| Stage | Directory | Purpose |
|---|---|---|
| S1 | `skills/research/` | Find and evaluate programs |
| S2 | `skills/content/` | Create social media content |
| S3 | `skills/blog/` | Write SEO articles |
| S4 | `skills/landing/` | Build conversion pages |
| S5 | `skills/distribution/` | Deploy and distribute |
| S6 | `skills/analytics/` | Track and analyze performance |
| S7 | `skills/automation/` | Automate and scale workflows |
| S8 | `skills/meta/` | Cross-stage orchestration and planning |

## References

- [Agent Skills Spec](https://agentskills.io) — canonical open standard
- [anthropics/skills](https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md) — one reference implementation
- [Equipping agents for the real world](https://www.anthropic.com/engineering/agent-skills) — Anthropic engineering blog (origin post)
```

## File: `template/SKILL.md`
```markdown
---
name: your-skill-name
description: >
  Replace with when the AI should activate this skill. Be pushy — cover multiple
  phrasings so the AI activates for a wide range of user prompts.
---

# Your Skill Name

What this skill does in 2-3 sentences.

## When to Use

Specific scenarios and trigger phrases.

## Workflow

Step-by-step what the skill does.

## Examples

**Example 1:** [realistic user prompt] → [expected output summary]

**Example 2:** [different scenario]
```

## File: `tools/src/api.ts`
```typescript
/**
 * list.affitor.com API client
 * Handles both public (no key, max 5 results) and authenticated access
 */

const API_BASE = "https://list.affitor.com/api/v1";

export interface Program {
  id: string;
  slug: string;
  name: string;
  url: string | null;
  description: string;
  reward_type: string | null;
  reward_value: string | null;
  cookie_days: number | null;
  stars_count: number;
  views_count: number;
  comments_count: number;
  category: string | null;
  tags: string[] | null;
  type: string;
  stage: string | null;
  status: string;
  created_at: string;
  profiles: {
    handle: string | null;
    avatar_url: string | null;
    name: string | null;
  };
}

export interface ProgramsResponse {
  data: Program[];
  count: number;
  tier?: "free";
  message?: string;
}

export interface SearchParams {
  q?: string;
  type?: "affiliate_program" | "skill";
  sort?: "trending" | "new" | "top";
  limit?: number;
  offset?: number;
  reward_type?: string;
  tags?: string;
  min_cookie_days?: number;
}

export async function fetchPrograms(
  params: SearchParams,
  apiKey?: string
): Promise<ProgramsResponse> {
  const url = new URL(`${API_BASE}/programs`);

  if (params.q) url.searchParams.set("q", params.q);
  if (params.type) url.searchParams.set("type", params.type);
  if (params.sort) url.searchParams.set("sort", params.sort);
  if (params.limit) url.searchParams.set("limit", String(params.limit));
  if (params.offset) url.searchParams.set("offset", String(params.offset));
  if (params.reward_type) url.searchParams.set("reward_type", params.reward_type);
  if (params.tags) url.searchParams.set("tags", params.tags);
  if (params.min_cookie_days) url.searchParams.set("min_cookie_days", String(params.min_cookie_days));

  const headers: Record<string, string> = {
    "Accept": "application/json",
    "User-Agent": "affiliate-check/1.0",
  };

  if (apiKey) {
    headers["Authorization"] = `Bearer ${apiKey}`;
  }

  const response = await fetch(url.toString(), { headers });

  if (!response.ok) {
    const body = await response.text();
    if (response.status === 401) {
      throw new Error("Invalid API key. Get one at list.affitor.com/settings → API Keys (free).");
    }
    if (response.status === 403) {
      throw new Error("API key missing 'programs:read' scope. Create a new key with the correct scope.");
    }
    if (response.status === 429) {
      throw new Error("Rate limit exceeded. Try again later or use an API key for unlimited access.");
    }
    throw new Error(`API error (${response.status}): ${body}`);
  }

  return response.json() as Promise<ProgramsResponse>;
}

export async function fetchProgram(
  id: string,
  apiKey?: string
): Promise<Program | null> {
  const headers: Record<string, string> = {
    "Accept": "application/json",
    "User-Agent": "affiliate-check/1.0",
  };
  if (apiKey) headers["Authorization"] = `Bearer ${apiKey}`;

  const response = await fetch(`${API_BASE}/programs/${id}`, { headers });

  if (!response.ok) {
    if (response.status === 404) return null;
    throw new Error(`API error (${response.status})`);
  }

  const json = await response.json();
  return json.data as Program;
}
```

## File: `tools/src/cache.ts`
```typescript
/**
 * In-memory program cache with TTL
 * Shared across requests via the persistent daemon
 */

import type { Program } from "./api";

const CACHE_TTL_MS = 5 * 60 * 1000; // 5 minutes

interface CacheEntry {
  data: Program[];
  timestamp: number;
  key: string;
}

class ProgramCache {
  private entries: Map<string, CacheEntry> = new Map();
  private maxEntries = 200;

  get(key: string): Program[] | null {
    const entry = this.entries.get(key);
    if (!entry) return null;
    if (Date.now() - entry.timestamp > CACHE_TTL_MS) {
      this.entries.delete(key);
      return null;
    }
    return entry.data;
  }

  set(key: string, data: Program[]): void {
    // Evict oldest if at capacity
    if (this.entries.size >= this.maxEntries) {
      const oldest = Array.from(this.entries.entries()).sort(
        (a, b) => a[1].timestamp - b[1].timestamp
      )[0];
      if (oldest) this.entries.delete(oldest[0]);
    }
    this.entries.set(key, { data, timestamp: Date.now(), key });
  }

  stats(): { entries: number; maxEntries: number; oldestAge: string } {
    let oldestTs = Date.now();
    for (const entry of this.entries.values()) {
      if (entry.timestamp < oldestTs) oldestTs = entry.timestamp;
    }
    const ageMs = this.entries.size > 0 ? Date.now() - oldestTs : 0;
    const ageSec = Math.round(ageMs / 1000);
    const ageStr = ageSec < 60 ? `${ageSec}s` : `${Math.round(ageSec / 60)}m`;
    return {
      entries: this.entries.size,
      maxEntries: this.maxEntries,
      oldestAge: ageStr,
    };
  }

  clear(): void {
    this.entries.clear();
  }
}

export const cache = new ProgramCache();
```

## File: `tools/src/cli.ts`
```typescript
#!/usr/bin/env bun
/**
 * affiliate-check CLI
 * Thin client that talks to the persistent daemon server.
 * If no server is running, starts one automatically.
 *
 * Usage:
 *   affiliate-check search <query>       Search programs
 *   affiliate-check top [--sort trending|new|top]  Top programs
 *   affiliate-check info <name>          Program details
 *   affiliate-check compare <a> <b> [c]  Compare programs
 *   affiliate-check status               Server status
 *   affiliate-check stop                 Stop server
 *   affiliate-check help                 Show help
 */

import { existsSync } from "fs";
import { resolve, dirname } from "path";

const STATE_FILE = "/tmp/affiliate-check.json";
const STARTUP_TIMEOUT = 5000; // 5 seconds

interface ServerState {
  port: number;
  pid: number;
  token: string;
  started: string;
}

function readState(): ServerState | null {
  try {
    if (!existsSync(STATE_FILE)) return null;
    const content = require("fs").readFileSync(STATE_FILE, "utf-8");
    return JSON.parse(content);
  } catch {
    return null;
  }
}

function isProcessAlive(pid: number): boolean {
  try {
    process.kill(pid, 0);
    return true;
  } catch {
    return false;
  }
}

async function healthCheck(port: number): Promise<boolean> {
  try {
    const response = await fetch(`http://127.0.0.1:${port}/health`, {
      signal: AbortSignal.timeout(1000),
    });
    return response.ok;
  } catch {
    return false;
  }
}

async function ensureServer(): Promise<number> {
  // Check existing server
  const state = readState();
  if (state && isProcessAlive(state.pid)) {
    const healthy = await healthCheck(state.port);
    if (healthy) return state.port;
  }

  // Start new server
  const serverPath = resolve(dirname(process.argv[1] || __filename), "server.ts");

  // Check if running from compiled binary or source
  const isCompiled = !process.argv[1]?.endsWith(".ts");
  const toolsDir = dirname(isCompiled ? process.execPath : process.argv[1] || __filename);
  const serverScript = isCompiled
    ? resolve(toolsDir, "..", "src", "server.ts")
    : resolve(toolsDir, "server.ts");

  const proc = Bun.spawn(["bun", "run", serverScript], {
    stdio: ["ignore", "pipe", "pipe"],
    env: { ...process.env },
  });

  // Wait for server to be ready
  const start = Date.now();
  while (Date.now() - start < STARTUP_TIMEOUT) {
    const newState = readState();
    if (newState && isProcessAlive(newState.pid)) {
      const healthy = await healthCheck(newState.port);
      if (healthy) return newState.port;
    }
    await new Promise((r) => setTimeout(r, 200));
  }

  throw new Error("Failed to start affiliate-check server. Is Bun installed?");
}

async function request(port: number, path: string): Promise<string> {
  const response = await fetch(`http://127.0.0.1:${port}${path}`, {
    signal: AbortSignal.timeout(10000),
  });
  return response.text();
}

function printHelp() {
  console.log(`
  ${"\x1b[1m"}affiliate-check${"\x1b[0m"} — Live affiliate program data from list.affitor.com

  ${"\x1b[1m"}USAGE${"\x1b[0m"}
    affiliate-check search <query>              Search programs by name/keyword
    affiliate-check search --recurring          Filter by recurring commission
    affiliate-check search --tags ai,video      Filter by tags
    affiliate-check search --min-cookie 30      Filter by minimum cookie days
    affiliate-check top                         Top programs by stars
    affiliate-check top --sort trending         Top by trending
    affiliate-check info <name>                 Detailed info on a program
    affiliate-check compare <a> <b> [c...]      Side-by-side comparison
    affiliate-check status                      Server status + cache info
    affiliate-check stop                        Stop the background server
    affiliate-check help                        Show this help

  ${"\x1b[1m"}ENVIRONMENT${"\x1b[0m"}
    AFFITOR_API_KEY    API key from list.affitor.com (optional)
                       Without key: free tier (max 5 results)
                       Get one: list.affitor.com/settings → API Keys (free)

  ${"\x1b[1m"}EXAMPLES${"\x1b[0m"}
    affiliate-check search "AI video"
    affiliate-check search --recurring --tags ai
    affiliate-check compare heygen synthesia
    affiliate-check top --sort new
`);
}

async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0 || args[0] === "help" || args[0] === "--help") {
    printHelp();
    return;
  }

  const command = args[0];

  try {
    const port = await ensureServer();

    switch (command) {
      case "search": {
        const params = new URLSearchParams();

        // Parse flags and positional query
        const positional: string[] = [];
        for (let i = 1; i < args.length; i++) {
          if (args[i] === "--recurring") {
            params.set("reward_type", "cps_recurring");
          } else if (args[i] === "--tags" && args[i + 1]) {
            params.set("tags", args[++i]);
          } else if (args[i] === "--min-cookie" && args[i + 1]) {
            params.set("min_cookie_days", args[++i]);
          } else if (args[i] === "--sort" && args[i + 1]) {
            params.set("sort", args[++i]);
          } else if (args[i] === "--limit" && args[i + 1]) {
            params.set("limit", args[++i]);
          } else if (!args[i].startsWith("--")) {
            positional.push(args[i]);
          }
        }

        if (positional.length > 0) {
          params.set("q", positional.join(" "));
        }

        const output = await request(port, `/search?${params.toString()}`);
        console.log(output);
        break;
      }

      case "top": {
        const params = new URLSearchParams();
        for (let i = 1; i < args.length; i++) {
          if (args[i] === "--sort" && args[i + 1]) {
            params.set("sort", args[++i]);
          } else if (args[i] === "--limit" && args[i + 1]) {
            params.set("limit", args[++i]);
          }
        }
        const output = await request(port, `/top?${params.toString()}`);
        console.log(output);
        break;
      }

      case "info": {
        const name = args.slice(1).join(" ");
        if (!name) {
          console.log("\x1b[31m  Error: Usage: affiliate-check info <program-name>\x1b[0m");
          process.exit(1);
        }
        const output = await request(port, `/info?name=${encodeURIComponent(name)}`);
        console.log(output);
        break;
      }

      case "compare": {
        const names = args.slice(1);
        if (names.length < 2) {
          console.log("\x1b[31m  Error: Usage: affiliate-check compare <program1> <program2>\x1b[0m");
          process.exit(1);
        }
        const output = await request(
          port,
          `/compare?names=${encodeURIComponent(names.join(","))}`
        );
        console.log(output);
        break;
      }

      case "status": {
        const output = await request(port, "/status");
        console.log(output);
        break;
      }

      case "stop": {
        const output = await request(port, "/stop");
        console.log(output);
        break;
      }

      default: {
        console.log(`\x1b[31m  Unknown command: ${command}\x1b[0m`);
        printHelp();
        process.exit(1);
      }
    }
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    console.error(`\x1b[31m  Error: ${msg}\x1b[0m`);
    process.exit(1);
  }
}

main();
```

## File: `tools/src/format.ts`
```typescript
/**
 * Terminal output formatting for affiliate-check
 * Clean, readable output without external dependencies
 */

import type { Program } from "./api";

const RESET = "\x1b[0m";
const BOLD = "\x1b[1m";
const DIM = "\x1b[2m";
const GREEN = "\x1b[32m";
const YELLOW = "\x1b[33m";
const CYAN = "\x1b[36m";
const WHITE = "\x1b[37m";

function rewardLabel(program: Program): string {
  const value = program.reward_value || "—";
  const typeMap: Record<string, string> = {
    cps_recurring: "recurring",
    cps_one_time: "one-time",
    cps_lifetime: "lifetime",
    cpl: "per lead",
    cpc: "per click",
  };
  const type = program.reward_type ? typeMap[program.reward_type] || program.reward_type : "";
  return type ? `${value} ${type}` : value;
}

function cookieLabel(days: number | null): string {
  if (!days) return "—";
  return `${days} days`;
}

function starsLabel(count: number): string {
  if (count === 0) return "—";
  return `★ ${count}`;
}

function truncate(str: string, max: number): string {
  if (str.length <= max) return str;
  return str.slice(0, max - 1) + "…";
}

export function formatProgramCard(p: Program): string {
  const lines: string[] = [];
  lines.push("");
  lines.push(`  ${BOLD}${WHITE}${p.name}${RESET}`);
  lines.push(`  ${DIM}${"─".repeat(Math.max(p.name.length, 25))}${RESET}`);
  lines.push(`  ${CYAN}Commission:${RESET}  ${rewardLabel(p)}`);
  lines.push(`  ${CYAN}Cookie:${RESET}      ${cookieLabel(p.cookie_days)}`);
  lines.push(`  ${CYAN}Stars:${RESET}       ${starsLabel(p.stars_count)}`);
  if (p.category) {
    lines.push(`  ${CYAN}Category:${RESET}    ${p.category}`);
  }
  if (p.tags?.length) {
    lines.push(`  ${CYAN}Tags:${RESET}        ${p.tags.join(", ")}`);
  }
  if (p.url) {
    lines.push(`  ${CYAN}URL:${RESET}         ${DIM}${p.url}${RESET}`);
  }
  if (p.description) {
    lines.push(`  ${DIM}${truncate(p.description, 80)}${RESET}`);
  }
  return lines.join("\n");
}

export function formatProgramTable(programs: Program[]): string {
  if (programs.length === 0) return "\n  No programs found.\n";

  const lines: string[] = [];
  lines.push("");
  lines.push(
    `  ${BOLD}${WHITE}${"Name".padEnd(25)} ${"Commission".padEnd(20)} ${"Cookie".padEnd(10)} ${"Stars".padEnd(8)}${RESET}`
  );
  lines.push(`  ${DIM}${"─".repeat(65)}${RESET}`);

  for (const p of programs) {
    const name = truncate(p.name, 24).padEnd(25);
    const commission = truncate(rewardLabel(p), 19).padEnd(20);
    const cookie = cookieLabel(p.cookie_days).padEnd(10);
    const stars = starsLabel(p.stars_count).padEnd(8);
    lines.push(`  ${name} ${commission} ${cookie} ${stars}`);
  }

  lines.push("");
  return lines.join("\n");
}

export function formatComparison(programs: Program[]): string {
  if (programs.length < 2) return "\n  Need at least 2 programs to compare.\n";

  const lines: string[] = [];
  const fields = [
    { label: "Commission", fn: (p: Program) => rewardLabel(p) },
    { label: "Cookie", fn: (p: Program) => cookieLabel(p.cookie_days) },
    { label: "Stars", fn: (p: Program) => starsLabel(p.stars_count) },
    { label: "Category", fn: (p: Program) => p.category || "—" },
    { label: "Tags", fn: (p: Program) => p.tags?.join(", ") || "—" },
    { label: "URL", fn: (p: Program) => p.url || "—" },
  ];

  // Header
  lines.push("");
  const header = `  ${"".padEnd(15)} ${programs.map((p) => BOLD + truncate(p.name, 24).padEnd(25) + RESET).join(" ")}`;
  lines.push(header);
  lines.push(`  ${DIM}${"─".repeat(15 + 26 * programs.length)}${RESET}`);

  // Rows
  for (const field of fields) {
    const row = `  ${CYAN}${field.label.padEnd(15)}${RESET}${programs.map((p) => truncate(field.fn(p), 24).padEnd(25)).join(" ")}`;
    lines.push(row);
  }

  lines.push("");
  return lines.join("\n");
}

export function formatFreeTierNotice(): string {
  return `\n  ${YELLOW}Free tier: max 5 results, no pagination.${RESET}\n  ${DIM}Get unlimited → list.affitor.com/settings → API Keys (free)${RESET}\n`;
}

export function formatError(message: string): string {
  return `\n  ${BOLD}\x1b[31mError:${RESET} ${message}\n`;
}

export function formatStatus(info: {
  uptime: string;
  cache: { entries: number; oldestAge: string };
  apiKey: boolean;
  port: number;
}): string {
  const lines: string[] = [];
  lines.push("");
  lines.push(`  ${BOLD}${WHITE}affiliate-check status${RESET}`);
  lines.push(`  ${DIM}${"─".repeat(30)}${RESET}`);
  lines.push(`  ${CYAN}Server:${RESET}    running on port ${info.port}`);
  lines.push(`  ${CYAN}Uptime:${RESET}    ${info.uptime}`);
  lines.push(`  ${CYAN}Cache:${RESET}     ${info.cache.entries} entries (oldest: ${info.cache.oldestAge})`);
  lines.push(`  ${CYAN}API Key:${RESET}   ${info.apiKey ? `${GREEN}configured${RESET}` : `${YELLOW}not set (free tier)${RESET}`}`);
  lines.push("");
  return lines.join("\n");
}
```

## File: `tools/src/server.ts`
```typescript
/**
 * affiliate-check persistent daemon
 * Bun HTTP server that caches API responses from list.affitor.com
 * Auto-shuts down after 30 min idle. Pattern from gstack/browse.
 */

import { fetchPrograms, type SearchParams } from "./api";
import { cache } from "./cache";
import {
  formatProgramCard,
  formatProgramTable,
  formatComparison,
  formatFreeTierNotice,
  formatError,
  formatStatus,
} from "./format";

const PORT_RANGE_START = 9500;
const PORT_RANGE_END = 9510;
const IDLE_TIMEOUT_MS = 30 * 60 * 1000; // 30 minutes
const STATE_FILE = "/tmp/affiliate-check.json";

let lastActivity = Date.now();
let startTime = Date.now();
let idleTimer: ReturnType<typeof setTimeout>;
const apiKey = process.env.AFFITOR_API_KEY || "";

function resetIdleTimer() {
  lastActivity = Date.now();
  clearTimeout(idleTimer);
  idleTimer = setTimeout(() => {
    console.log("[affiliate-check] Idle timeout — shutting down");
    cleanup();
    process.exit(0);
  }, IDLE_TIMEOUT_MS);
}

function cacheKey(params: SearchParams): string {
  return JSON.stringify(params);
}

function uptimeStr(): string {
  const ms = Date.now() - startTime;
  const sec = Math.floor(ms / 1000);
  if (sec < 60) return `${sec}s`;
  const min = Math.floor(sec / 60);
  if (min < 60) return `${min}m ${sec % 60}s`;
  const hr = Math.floor(min / 60);
  return `${hr}h ${min % 60}m`;
}

async function handleRequest(req: Request): Promise<Response> {
  resetIdleTimer();

  const url = new URL(req.url);
  const path = url.pathname;

  // Health check
  if (path === "/health") {
    return Response.json({ status: "ok", uptime: uptimeStr() });
  }

  // Status
  if (path === "/status") {
    const stats = cache.stats();
    const output = formatStatus({
      uptime: uptimeStr(),
      cache: { entries: stats.entries, oldestAge: stats.oldestAge },
      apiKey: !!apiKey,
      port: parseInt(url.port),
    });
    return new Response(output, { headers: { "Content-Type": "text/plain" } });
  }

  // Stop server
  if (path === "/stop") {
    setTimeout(() => {
      cleanup();
      process.exit(0);
    }, 100);
    return new Response("Shutting down.\n", { headers: { "Content-Type": "text/plain" } });
  }

  // Search programs
  if (path === "/search") {
    const params: SearchParams = {
      q: url.searchParams.get("q") || undefined,
      type: (url.searchParams.get("type") as SearchParams["type"]) || "affiliate_program",
      sort: (url.searchParams.get("sort") as SearchParams["sort"]) || "trending",
      limit: parseInt(url.searchParams.get("limit") || "10"),
      reward_type: url.searchParams.get("reward_type") || undefined,
      tags: url.searchParams.get("tags") || undefined,
      min_cookie_days: url.searchParams.get("min_cookie_days")
        ? parseInt(url.searchParams.get("min_cookie_days")!)
        : undefined,
    };

    const key = cacheKey(params);
    let programs = cache.get(key);
    let fromCache = true;

    if (!programs) {
      fromCache = false;
      try {
        const response = await fetchPrograms(params, apiKey || undefined);
        programs = response.data;
        cache.set(key, programs);

        if (response.tier === "free") {
          const output = formatProgramTable(programs) + formatFreeTierNotice();
          return new Response(output, { headers: { "Content-Type": "text/plain" } });
        }
      } catch (err) {
        const msg = err instanceof Error ? err.message : String(err);
        return new Response(formatError(msg), {
          status: 502,
          headers: { "Content-Type": "text/plain" },
        });
      }
    }

    const output = formatProgramTable(programs);
    return new Response(output, { headers: { "Content-Type": "text/plain" } });
  }

  // Top programs
  if (path === "/top") {
    const sort = (url.searchParams.get("sort") as SearchParams["sort"]) || "top";
    const limit = parseInt(url.searchParams.get("limit") || "10");
    const params: SearchParams = { sort, limit, type: "affiliate_program" };

    const key = cacheKey({ ...params, _cmd: "top" } as any);
    let programs = cache.get(key);

    if (!programs) {
      try {
        const response = await fetchPrograms(params, apiKey || undefined);
        programs = response.data;
        cache.set(key, programs);

        if (response.tier === "free") {
          const output = formatProgramTable(programs) + formatFreeTierNotice();
          return new Response(output, { headers: { "Content-Type": "text/plain" } });
        }
      } catch (err) {
        const msg = err instanceof Error ? err.message : String(err);
        return new Response(formatError(msg), {
          status: 502,
          headers: { "Content-Type": "text/plain" },
        });
      }
    }

    const output = formatProgramTable(programs);
    return new Response(output, { headers: { "Content-Type": "text/plain" } });
  }

  // Info (single program by name search)
  if (path === "/info") {
    const name = url.searchParams.get("name");
    if (!name) {
      return new Response(formatError("Usage: affiliate-check info <program-name>"), {
        status: 400,
        headers: { "Content-Type": "text/plain" },
      });
    }

    const key = `info:${name}`;
    let programs = cache.get(key);

    if (!programs) {
      try {
        const response = await fetchPrograms(
          { q: name, limit: 1, type: "affiliate_program" },
          apiKey || undefined
        );
        programs = response.data;
        if (programs.length > 0) cache.set(key, programs);
      } catch (err) {
        const msg = err instanceof Error ? err.message : String(err);
        return new Response(formatError(msg), {
          status: 502,
          headers: { "Content-Type": "text/plain" },
        });
      }
    }

    if (!programs || programs.length === 0) {
      return new Response(formatError(`No program found matching "${name}".`), {
        status: 404,
        headers: { "Content-Type": "text/plain" },
      });
    }

    const output = formatProgramCard(programs[0]);
    return new Response(output, { headers: { "Content-Type": "text/plain" } });
  }

  // Compare (multiple programs)
  if (path === "/compare") {
    const names = url.searchParams.get("names")?.split(",").map((n) => n.trim());
    if (!names || names.length < 2) {
      return new Response(
        formatError("Usage: affiliate-check compare <program1> <program2> [program3...]"),
        { status: 400, headers: { "Content-Type": "text/plain" } }
      );
    }

    const programs = [];
    for (const name of names) {
      try {
        const response = await fetchPrograms(
          { q: name, limit: 1, type: "affiliate_program" },
          apiKey || undefined
        );
        if (response.data.length > 0) {
          programs.push(response.data[0]);
        }
      } catch (err) {
        // Skip failed lookups
      }
    }

    if (programs.length < 2) {
      return new Response(formatError("Could not find enough programs to compare."), {
        status: 404,
        headers: { "Content-Type": "text/plain" },
      });
    }

    const output = formatComparison(programs);
    return new Response(output, { headers: { "Content-Type": "text/plain" } });
  }

  return new Response(
    `\n  affiliate-check server\n\n  Endpoints:\n    /search?q=...    Search programs\n    /top             Top programs\n    /info?name=...   Program details\n    /compare?names=a,b  Compare programs\n    /status          Server status\n    /health          Health check\n    /stop            Stop server\n\n`,
    { headers: { "Content-Type": "text/plain" } }
  );
}

function cleanup() {
  clearTimeout(idleTimer);
  try {
    const fs = require("fs");
    fs.unlinkSync(STATE_FILE);
  } catch {}
}

async function findPort(): Promise<number> {
  for (let port = PORT_RANGE_START; port <= PORT_RANGE_END; port++) {
    try {
      const server = Bun.serve({ port, fetch: () => new Response("") });
      server.stop(true);
      return port;
    } catch {
      continue;
    }
  }
  throw new Error(`No available port in range ${PORT_RANGE_START}-${PORT_RANGE_END}`);
}

async function main() {
  const port = await findPort();
  const token = crypto.randomUUID();

  const server = Bun.serve({
    port,
    fetch: handleRequest,
  });

  // Write state file
  const state = {
    port,
    pid: process.pid,
    token,
    started: new Date().toISOString(),
  };
  await Bun.write(STATE_FILE, JSON.stringify(state, null, 2));

  startTime = Date.now();
  resetIdleTimer();

  console.log(`[affiliate-check] Server running on port ${port} (PID ${process.pid})`);
  console.log(`[affiliate-check] API key: ${apiKey ? "configured" : "not set (free tier)"}`);
  console.log(`[affiliate-check] Auto-shutdown after 30 min idle`);

  // Handle signals
  process.on("SIGINT", () => {
    cleanup();
    process.exit(0);
  });
  process.on("SIGTERM", () => {
    cleanup();
    process.exit(0);
  });
}

main();
```

