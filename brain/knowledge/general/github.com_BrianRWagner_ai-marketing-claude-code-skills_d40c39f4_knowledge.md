---
id: github.com-brianrwagner-ai-marketing-claude-code-s
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:35.768012
---

# KNOWLEDGE EXTRACT: github.com_BrianRWagner_ai-marketing-claude-code-skills_d40c39f4
> **Extracted on:** 2026-04-01 14:05:04
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007523655/github.com_BrianRWagner_ai-marketing-claude-code-skills_d40c39f4

---

## File: `.gitignore`
```
pro/
```

## File: `CHANGELOG.md`
```markdown
## [3.1.0] — March 8, 2026

### What Changed
`quick|standard|deep` execution mode added to all 19 free skills. Inspired by ECC's runtime profile system.

### Why
Skills were all-or-nothing. A user who needed a fast answer got the same full process as someone doing a deep audit. Mode switching gives users the right output depth without multiple skills.

### What's New
- **Mode table** in every skill — immediately after the intro, before Phase 1
- `quick` — minimum viable output, right answer for fast use cases (15 min or less)
- `standard` — full process, unchanged from prior behavior (default — no breaking changes)
- `deep` — extended research, iteration, and frameworks for serious projects
- `SKILL-MODE-PATTERN.md` — implementation guide for adding this pattern to any skill

### Skills Updated
All 19 free skills: ai-discoverability-audit, case-study-builder, cold-outreach-sequence, content-idea-generator, de-ai-ify, go-mode, homepage-audit, last30days, linkedin-authority-builder, linkedin-profile-optimizer, marketing-principles, newsletter-creation-curation, plan-my-day, positioning-basics, reddit-insights, social-card-gen, testimonial-collector, voice-extractor, youtube-summarizer

### Notes
Standard mode = identical to v3.0.0 behavior. Fully backward compatible.

---

## [3.0.0] — February 28, 2026

### What Changed
3-layer architecture refactor + new Meeting Prep skill.

### Why
Skills audit (Feb 28) found 3 CC free skills missing YAML front matter (invisible to trigger system). Meeting Prep was identified as the highest-value missing weekly recurring skill.

### What's New
- **Meeting Prep skill** — INTAKE→ANALYZE→OUTPUT format. Vault search + prior brief lookup + question generation. No autonomy.

### Front Matter Verified
- `daily-briefing-builder` — INTAKE→ANALYZE→OUTPUT format, confirmed good
- `tweet-draft-reviewer` — 8 voice rules fully documented, confirmed good
- `vault-cleanup-auditor` — shell commands complete, confirmed good

### Architecture
All skills follow INTAKE→ANALYZE→OUTPUT structure. No autonomy triggers. You run it, you get your output.

---

# Changelog

All notable changes to the AI Marketing Skills for Claude Code library.

---

## [2.0.0] — February 2026

### What Changed

Major upgrade across 12 skills. Every updated skill was graded against the [Claude Code Skill Effectiveness Rubric](https://brianrwagner.com) and rebuilt to score 85+/100.

### Added to all upgraded skills

- **Context Loading Gates** — explicit checklist before any output; skill refuses to proceed without required inputs (URL, positioning statement, writing samples, etc.)
- **Structured Reasoning Phases** — multi-step analysis before generating (Phase 1: intake → Phase 2: analysis → Phase 3: generate → Phase 4: critique → Phase 5: deliver)
- **Self-Critique Pass** — mandatory structured review checklist applied to output before delivery
- **Iteration Protocol** — defined process for refining weak output
- **Output Structure** — exact named markdown sections and formatting conventions per skill

### Skills Upgraded

| Skill | Before | After | Key Changes |
|-------|--------|-------|-------------|
| `marketing-principles` | 47 | 87 | Context intake, decision engine replacing philosophy list, inversion critique section, per-principle output templates |
| `social-card-gen` | 38 | 87 | Platform reasoning rules inline, intake gate, quality self-review pass, Node.js fallback path, guardrails |
| `testimonial-collector` | 52 | 87 | 5-question intake, quality assessment scoring, drafting framework, iteration loop, placement guide |
| `homepage-audit` | 58 | 88 | Mandatory URL/screenshot intake, page-type branching, scoring criteria per row, impact×effort matrix |
| `case-study-builder` | 60 | 88 | Structured 8-field intake form, outcome extraction protocol, self-critique pass, distribution plan, cross-link to testimonial-collector |
| `positioning-basics` | 64 | 88 | Competitive research tool calls, memory write, gate before output, iteration against checklist |
| `linkedin-authority-builder` | 63 | 88 | 5-question intake, content calendar output, cross-links to profile-optimizer + content-idea-generator |
| `content-idea-generator` | 61 | 88 | Context intake, freshness web search, quality filter per idea, cross-link to positioning-basics |
| `voice-extractor` | 61 | 88 | Constraint handling, failure modes, quick/full mode documentation, validation step |
| `cold-outreach-sequence` | 64 | 88 | Research tool calls wired in, personalization scoring, pipeline tracker output, post-breakup handling |
| `newsletter-creation-curation` | 74 | 89 | Execution output template, multi-agent handoff protocol |
| `ai-discoverability-audit` | 72 | 89 | Re-audit loop, baseline comparison, penalty guardrails |

### Skills Unchanged (already 85+)

`go-mode` (86), `de-ai-ify` (83), `last30days` (79), `reddit-insights` (80), `youtube-summarizer` (82), `plan-my-day` (81), `linkedin-profile-optimizer` (90)

---

## [1.0.0] — January 2026

### Initial Release

19 marketing skills covering strategy, content, research, conversion, and productivity. Based on the [AgentSkills.ai](https://agentskills.ai) open standard.

## v3.2.0 — March 14, 2026 (Night Sprint)

### Claw Mart v2 Updates
- **Chief of Staff v2**: Three operating modes (quick/standard/deep), WAL Protocol, working buffer for context survival, self-critique protocol, crisis mode, multi-model routing guide, group chat intelligence, lessons-learned system
- **Multi-Agent Team Blueprint v2**: Starter kits (Content Machine, Research Engine, Ops Hub), cost calculator, 4-week phased deployment guide, queue system with JSON templates, inter-agent communication patterns, failure recovery guide
- **Morning Brief System v2**: Quick/standard/deep modes, context loading gates, carry-forward and crisis modes, overload protocol, self-critique, weekly mode

### New Files
- Added SKILL-OC.md (OpenClaw-optimized) for Chief of Staff v2 and Multi-Agent Team Blueprint v2
```

## File: `README.md`
```markdown
# AI Marketing Skills for Claude Code

**Marketing frameworks that Claude Code actually executes.**

Not guides. Not courses. *Skills* — packaged expertise your AI coding agent loads and follows.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-23%20Free%20%2B%2010%20Pro-green.svg)](#available-skills)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Native-blueviolet.svg)](#installation)
[![Also Works](https://img.shields.io/badge/Also%20Works-OpenClaw%20%7C%20Copilot%20%7C%20Cursor-gray.svg)](#compatibility)
[![Updated](https://img.shields.io/badge/Updated-Mar%2014%202026-brightgreen.svg)](./CHANGELOG.md)

> **March 2026 — v3.1:** All 19 free skills now support `quick|standard|deep` execution modes. Get fast answers or deep audits from the same skill — no extra prompting. [See what changed →](./CHANGELOG.md)

---

## What Are Agent Skills?

Agent Skills are an [open standard](https://agentskills.ai) for packaging expertise as instructions that AI agents can follow.

**Traditional content:** You read it → You apply it → You forget half of it.

**Agent Skills:** Your agent reads it → Your agent applies it → Every time. Perfectly.

Think of it like giving Claude Code a playbook written by an expert. Instead of prompting from scratch every time, the skill provides the framework, questions, and output format automatically.

---

## Quick Install (Claude Code)

```bash
# Clone the repo
git clone https://github.com/BrianRWagner/ai-marketing-claude-code-skills.git

# Copy skills to Claude Code's skills folder
mkdir -p ~/.claude/skills
cp -r ai-marketing-claude-code-skills/* ~/.claude/skills/
```

That's it. Claude Code will now automatically use these skills when you mention related topics.

---

## Available Skills

### Strategy & Positioning

#### 🎯 Positioning Basics
Core positioning framework for founders and marketers. Clarify who you're for, what you do, and why you're different.

**Use when:** "Help me with positioning", "Who is this for?", "What makes us different?"

→ [positioning-basics/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### 🔍 AI Discoverability Audit
Audit how a brand appears in AI-powered search and recommendation systems (ChatGPT, Perplexity, Claude, Gemini).

**Use when:** "How do I show up in ChatGPT?", "AI search visibility", "AEO audit"

→ [ai-discoverability-audit/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### 📚 Marketing Principles
Apply timeless marketing and business principles from the masters (Drucker, Ogilvy, Godin, Buffett, Munger, Bezos, Jobs).

**Use when:** "First principles thinking", "Should I do X?", "What would work here?", strategic decisions

→ [marketing-principles/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

### Content & Authority

#### 💼 LinkedIn Authority Builder
Build a LinkedIn content system for thought leadership. Positioning, content pillars, formats, and posting rhythm.

**Use when:** "LinkedIn strategy", "Build my presence", "Content system", "Thought leadership"

→ [linkedin-authority-builder/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### 💡 Content Idea Generator
Generate content ideas based on your positioning and ICP. Multiple frameworks for different content types.

**Use when:** "What should I post?", "Content ideas", "Blog topics", "LinkedIn content"

→ [content-idea-generator/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### 🎙️ Voice Extractor
Extract and document someone's authentic writing voice from samples. Create voice guides for AI training or ghostwriting.

**Use when:** "Capture my voice", "Voice guide", "Write like me", "Train AI on my style"

→ [voice-extractor/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) | [$9 premium version on Claw Mart →](https://www.shopclawmart.com/listings/voice-extractor-f1578cb8)

---

#### 🧹 De-AI-ify
Remove AI-generated jargon and restore human voice to text. Built from analyzing 1,000+ AI vs human content pieces.

**Use when:** "This sounds like AI", "Make it human", "Remove AI voice", "De-robotify this"

→ [de-ai-ify/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### 📱 Social Card Generator
Generate platform-specific social post variants (Twitter, LinkedIn, Reddit) from one source input. No API dependency.

**Use when:** "Turn this into social posts", "Repurpose for Twitter/LinkedIn", "Create social variants"

→ [social-card-gen/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

### Research & Intelligence

#### 🔬 Last 30 Days Research
Research any topic across Reddit, X, and web from the last 30 days. Current trends, real community sentiment, and actionable insights in 7 minutes vs 2 hours manual research.

**Use when:** "What are people saying about X?", "Current trends in Y", "Market research", "Community sentiment"

→ [last30days/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### 🔎 Reddit Insights
Search and analyze Reddit content using semantic AI search. Find user pain points, discover niche markets, validate business ideas with real user feedback.

**Use when:** "Search Reddit for...", "What does Reddit think about?", "Find pain points", "Validate this idea"

→ [reddit-insights/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### 🎬 YouTube Summarizer
Fetch YouTube video transcripts, generate structured summaries with key insights and metadata. Supports full transcript delivery.

**Use when:** "Summarize this YouTube video", "Get transcript from...", "Key takeaways from this video"

→ [youtube-summarizer/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### 🔗 LinkedIn Profile Optimizer
Audit and rewrite your LinkedIn profile to attract the right people. Scores each section, rewrites headline and about copy, and includes an AI visibility checklist for ChatGPT/Perplexity/Claude search.

**Use when:** "Optimize my LinkedIn", "Rewrite my about section", "LinkedIn profile help", "AI search visibility"

→ [linkedin-profile-optimizer/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

### Conversion & Sales

#### 📄 Homepage Audit
Quick conversion audit for any homepage or landing page. Get actionable feedback in minutes.

**Use when:** "Review my homepage", "Why isn't my page converting?", "Audit my landing page"

→ [homepage-audit/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### 📧 Cold Outreach Sequence
Build personalized cold outreach sequences for LinkedIn and email. Research, connection requests, follow-ups, and conversion.

**Use when:** "Cold outreach", "LinkedIn messages", "Prospecting sequence", "Sales emails"

→ [cold-outreach-sequence/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### 📊 Case Study Builder
Turn client wins into formatted case studies for proposals, social proof, and sales conversations.

**Use when:** "Write a case study", "Document results", "Client success story", "Build social proof"

→ [case-study-builder/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### ⭐ Testimonial Collector
Systematically gather and format client testimonials for social proof.

**Use when:** "Get testimonials", "Social proof", "Client quotes", "Build credibility"

→ [testimonial-collector/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

### Productivity & Operations

#### 📅 Plan My Day
Generate an energy-optimized, time-blocked daily plan based on circadian rhythm research and GTD principles.

**Use when:** "Plan my day", "Time block today", "What should I work on?", "Daily schedule"

→ [plan-my-day/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### 📧 Newsletter Creation & Curation
Industry-adaptive B2B newsletter creation with stage, role, and geography-aware workflows.

**Use when:** "Create a newsletter", "Curate content for newsletter", "B2B newsletter", "Weekly digest"

→ [newsletter-creation-curation/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

#### 🚀 Go Mode
Deep work execution mode. When you have a clear task and need to execute without distraction.

**Use when:** "Go mode", "Execute this", "Let's build", "Ship it"

→ [go-mode/SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)

---

## Installation

### Quick Install (any platform)

```bash
git clone https://github.com/BrianRWagner/ai-marketing-claude-code-skills.git
cd ai-marketing-claude-code-skills
bash scripts/install.sh
```

Auto-detects Claude Code, OpenClaw, Cursor, and Windsurf. Walks you through the rest.

**Flags:**
```bash
bash scripts/install.sh --all              # install to every detected platform
bash scripts/install.sh --platform=cursor  # specific platform only
bash scripts/install.sh --include-pro      # include pro/ skills (if purchased)
bash scripts/install.sh --dry-run          # preview without writing files
```

### Platform Support

| Platform | Install Location | File Used | Notes |
|----------|-----------------|-----------|-------|
| **Claude Code** | `~/.claude/skills/` | `SKILL.md` | Full detail, all phases |
| **OpenClaw** | `~/.openclaw/skills/` | `SKILL-OC.md` ¹ | Token-efficient edition |
| **Cursor** | `.cursor/rules/` (project) | `SKILL.md` → `.mdc` | Converted with rule frontmatter |
| **Windsurf** | `.windsurf/rules/` (project) | `SKILL.md` → `.md` | Converted with rule frontmatter |
| **Generic** | `./ai-marketing-skills/` | `SKILL.md` | Plain copy, any tool |

> ¹ **Dual-file system:** Each skill ships two versions — `SKILL.md` (Claude Code, verbose, all phases) and `SKILL-OC.md` (OpenClaw, condensed, ~200 lines, token-efficient). The installer automatically routes the right file to the right platform. If `SKILL-OC.md` isn't present yet for a skill, it falls back to `SKILL.md`.

### List Available Skills

```bash
bash scripts/list-skills.sh
```

### Convert to Platform Format

```bash
bash scripts/convert.sh --platform=cursor --output-dir=./.cursor/rules
bash scripts/convert.sh --all   # convert for all platforms into ./converted/
```

---

## Compatibility

| Platform | Status | Notes |
|----------|--------|-------|
| **Claude Code** | ✅ Native | Primary target |
| **OpenClaw** | ✅ Compatible | Works as-is, [optimized version available](https://github.com/BrianRWagner/ai-marketing-openclaw-skills) |
| **GitHub Copilot** | ✅ Compatible | Via .github/skills |
| **Cursor** | ✅ Compatible | Via rules/context |
| **ChatGPT** | ⚠️ Manual | Paste SKILL.md content |
| **Claude.ai** | ⚠️ Manual | Paste SKILL.md content |

---

## 🔥 Premium Skills (Gumroad)

Full Claude Code editions with structured reasoning phases, self-critique loops, and output precision.

→ [Browse all on Gumroad](https://brianrwagner.gumroad.com)

| Skill | Price | Link |
|-------|-------|------|
| AI Marketing Bundle (all 7) | $49 | [Buy →](https://brianrwagner.gumroad.com/l/brw-cc-marketing-bundle) |
| AI Discoverability Audit v2 | $19 | [Buy →](https://brianrwagner.gumroad.com/l/ai-discoverability-audit) |
| Founder Intelligence | $15 | [Buy →](https://brianrwagner.gumroad.com/l/brw-founder-intelligence) |
| Competitor Intel Brief | $12 | [Buy →](https://brianrwagner.gumroad.com/l/brw-competitor-intel-brief) |
| Morning Brief System | $14 | [Buy →](https://brianrwagner.gumroad.com/l/brw-morning-brief-system) |
| Brand Voice Extractor | $9 | [Buy →](https://brianrwagner.gumroad.com/l/brand-voice-extractor) |
| AI Employee Onboarding | $9 | [Buy →](https://brianrwagner.gumroad.com/l/brw-ai-employee-onboarding) |
| Brand Positioning Audit | $9 | [Buy →](https://brianrwagner.gumroad.com/l/brw-brand-positioning-audit) |
## About

Created by **Brian Wagner** — AI Marketing Architect

15+ years building marketing systems for Fortune 500s and startups. Now packaging that expertise for the AI era.

- 🌐 [brianrwagner.com](https://brianrwagner.com)
- 🐦 [@BrianRWagner](https://twitter.com/BrianRWagner)
- 💼 [LinkedIn](https://linkedin.com/in/brianrwagner)

---

## Contributing

Found an issue? Have an improvement?

1. Fork the repo
2. Make your changes
3. Submit a PR

All contributions welcome. Let's make these skills better together.

---

## License

MIT — Use freely. Attribution appreciated.

---

*Marketing frameworks that Claude Code actually executes.* 🔱
```

## File: `SKILL-MODE-PATTERN.md`
```markdown
# SKILL_MODE Pattern — v1.0
**Stolen from:** everything-claude-code (ECC) runtime profile system
**Applied to:** AI marketing skills

---

## What This Is

Every skill now supports three execution depths. Users get the right output for their situation without the agent guessing.

| Mode | Output depth | Time expectation |
|------|-------------|-----------------|
| `quick` | Minimum viable output — single pass, no deep research, no scoring | < 15 min |
| `standard` | Full process — all phases, scoring where relevant, priority output | 30–45 min |
| `deep` | Extended research + iteration + frameworks for ongoing use | 60–90 min |

---

## How to Add This to Any Skill

**Step 1: Add the Mode section** immediately after the intro, before "Before You Begin" or Phase 1.

```markdown
## Mode

Detect from context or ask: *"[One-line question specific to this skill]"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | [Describe the minimum useful output] | [When to use] |
| `standard` | [Full current skill behavior] | [When to use] |
| `deep` | [Extended output with extras] | [When to use] |

**Default: `standard`** — [one line on when quick or deep is appropriate]
```

**Step 2: Tag phases/sections** that only run in certain modes.

- No tag = runs in all modes
- `[standard+]` = runs in standard and deep only
- `[deep only]` = deep mode only

**Step 3: Update Output Format section** to describe what each mode delivers.

---

## Skills Updated (v2.1)

- [x] `ai-discoverability-audit` — quick (Phase 1 only) / standard (full) / deep (+ 90-day plan)
- [x] `cold-outreach-sequence` — quick (1 message) / standard (4-touch) / deep (campaign system)
- [x] `de-ai-ify` — quick (fast pass) / standard (full scan) / deep (+ voice calibration)

## Skills To Update (Next)

- [ ] `linkedin-authority-builder`
- [ ] `linkedin-profile-optimizer`
- [ ] `content-idea-generator`
- [ ] `homepage-audit`
- [ ] `reddit-insights`
- [ ] `last30days`
- [ ] `positioning-basics`
- [ ] `marketing-principles`

---

## Design Principles

1. **quick is not worse — it's appropriate for different jobs.** Don't frame quick as a degraded mode.
2. **Don't change the skill's core logic.** The mode gate is additive — standard mode = current behavior.
3. **Detect from context first.** If the user says "quick" or "fast" or gives you one name — infer quick. If they say "full audit" or "system" — infer deep. Only ask if genuinely ambiguous.
4. **deep should earn its time.** If deep mode doesn't produce something a consultant would charge for, it's not deep enough.

---

*Pattern introduced: March 8, 2026*
*Inspired by: ECC's `ECC_HOOK_PROFILE=minimal|standard|strict`*
```

## File: `skills-content-plan-march.md`
```markdown
# Skills Content Plan — March 2026
*Brian Wagner (@BrianRWagner) | AI Marketing Skills Series*
*Built by Scribe | Feb 27, 2026*

---

## Posted Tracker

| Date | Skill / Topic | Platform | Posted |
|------|---------------|----------|--------|
| Mar 1 | content-idea-generator (Free Drop) | LI + X | ❌ |
| Mar 3 | AI Discoverability Audit v2 (Spotlight) | LI + X | ❌ |
| Mar 5 | Build in Public — $97 in 6 days (BIP) | LI + X | ❌ |
| Mar 7 | de-ai-ify (Free Drop) | LI + X | ❌ |
| Mar 9 | Gumroad Bundle $49 (Bundle Feature) | LI + X | ❌ |
| Mar 11 | plan-my-day (Free Drop) | LI + X | ❌ |
| Mar 13 | Founder Intelligence (Spotlight) | LI + X | ❌ |
| Mar 15 | Social Proof — First month milestone (Social Proof) | LI + X | ❌ |
| Mar 17 | Brand Voice Extractor (Spotlight) | LI + X | ❌ |
| Mar 19 | cold-outreach-sequence (Free Drop) | LI + X | ❌ |
| Mar 21 | Claw Mart Complete Bundle $44 (Bundle Feature) | LI + X | ❌ |
| Mar 23 | Chief of Staff (Spotlight) | LI + X | ❌ |
| Mar 25 | Build in Public — The system behind the skills (BIP) | LI + X | ❌ |
| Mar 27 | Competitor Intel Brief (Spotlight) | LI + X | ❌ |
| Mar 29 | homepage-audit (Free Drop) | LI + X | ❌ |
| Mar 31 | Social Proof — March wrap + what's next (Social Proof) | LI + X | ❌ |

---

## Mar 1 — content-idea-generator — LI + X

**Type:** Free Drop
**Skill:** content-idea-generator
**Link:** https://github.com/BrianRWagner/ai-marketing-claude-code-skills
**Posted:** ❌

### LinkedIn Draft

Free skill drop to kick off March.

The content-idea-generator is one of 19 free Claude Code marketing skills on GitHub. No paywall. No email required. Download, run it, and let it pull 30+ content angles from your actual positioning — not generic "5 tips" nonsense.

Here's what it does:

You paste in your ICP, your niche, your value prop. It spits out content angles mapped to buyer awareness stages. Not brainstormed. Structured. Aligned to where your reader is in the journey.

The ideas it outputs are specific enough to execute same-day. Not "write about AI" but "here's the Monday morning moment your ICP dreads, and how you solve it."

This came from a real problem. A founder I was helping had 15 years of expertise but stared at a blank doc every week. The skill doesn't make her a better writer — it ends the stare.

It's free because the barrier to good marketing content isn't money. It's clarity.

Runs in Claude Code (free tier works). Link in the comments.

---

### X Draft

Free Claude Code skill for marketers:

Paste your ICP + value prop → get 30+ content angles mapped to buyer awareness stages.

No blank doc staring. Structured ideas you can execute today.

19 free skills on GitHub. This is one of them. Link in first reply.

---

## Mar 3 — AI Discoverability Audit v2 — LI + X

**Type:** Spotlight
**Skill:** AI Discoverability Audit v2
**Link:** https://brianrwagner.gumroad.com/l/brw-cc-marketing-bundle
**Posted:** ❌

### LinkedIn Draft

Most brands have an SEO strategy. Almost none have an AI discoverability strategy.

That's a real problem — because when someone asks ChatGPT, Perplexity, or Claude which tool wins in your category, your brand either shows up or it doesn't. Right now, most brands don't.

The AI Discoverability Audit v2 ($19) fixes that.

Here's what it actually does: it runs your brand through 12 structured AI prompt scenarios — the questions your buyers are actually typing into AI tools right now. It checks whether you appear, how you're described, and how you stack up against direct competitors.

Then it gives you a gap report. Not "improve your content." Specific pages, specific angles, specific fixes.

Built this because a founder asked me why her competitor kept appearing in ChatGPT responses and she didn't. She had better content. More backlinks. Better product. But her brand language wasn't optimized for AI retrieval.

That's fixable. It's also a competitive gap most companies haven't noticed yet.

V2 has updated prompt architecture for 2026 AI search patterns and a scoring rubric you can run quarterly.

If you're in a competitive category and not sure where you land in AI results — this is the first 30 minutes to spend.

Link in the comments.

---

### X Draft

Most brands have an SEO strategy.

Zero have an AI discoverability strategy.

When someone asks ChatGPT which tool wins in your category — you're either in the answer or you're not.

The AI Discoverability Audit v2 tells you exactly where you stand. And what to fix.

$19. Link in first reply.

---

## Mar 5 — Build in Public: $97 in 6 days — LI + X

**Type:** Build in Public
**Skill:** Skills marketplace (all)
**Link:** https://shopclawmart.com
**Posted:** ❌

### LinkedIn Draft

Pretty cool moment. $97 in AI skill revenue. Six days into the experiment.

Here's the honest version of how it happened:

Feb 20: listed my first Claude Code marketing skill on Claw Mart. No audience. No launch post. No paid promotion. Maybe 400 LinkedIn followers who actually cared about AI.

By Feb 26: $97. Two different buyers. Skills they'd never seen from someone they'd never heard of.

The $500 Challenge — can a solo builder generate $500 in skill revenue in 30 days, organic only?

Day 6 answer: maybe.

What the first six days taught me:

**Specificity sells.** Skills with tight use cases ("this is for founders cold-pitching enterprise clients") outperformed broad ones.

**Proof-of-work matters more than polish.** Buyers weren't looking for a perfect product. They wanted evidence it worked.

**The best marketing is showing the output.** Not a demo — the actual output. That's what converted.

Building in public the whole way. 24 days left. $403 to go.

---

### X Draft

$97 in AI skill revenue. Day 6.

No ads. No launch. ~400 followers who care about AI.

The $500 Challenge: can a solo builder hit $500 in 30 days, organic only?

What's converting: showing the actual output, not the demo.

24 days left. Thread incoming.

---

## Mar 7 — de-ai-ify — LI + X

**Type:** Free Drop
**Skill:** de-ai-ify
**Link:** https://github.com/BrianRWagner/ai-marketing-claude-code-skills
**Posted:** ❌

### LinkedIn Draft

Free skill. No pitch. Just something useful.

de-ai-ify is a Claude Code skill that strips AI-generated language from marketing copy and restores the human voice underneath.

Not a grammar checker. Not a paraphraser.

It's trained on 1,000+ AI vs. human content comparisons. Flags the specific patterns that make AI copy sound like AI copy — the "delve into," the "it's worth noting," the "navigate the landscape" — and replaces them with language that sounds like a person wrote it.

Because someone did. They just let the model take over.

The typical use case: you used Claude to draft a blog post or LinkedIn piece. It's technically correct and you hate how it sounds. de-ai-ify is the editing pass that makes it yours again.

Runs in Claude Code. Free on GitHub. Link in the comments.

---

### X Draft

Free Claude Code skill:

de-ai-ify strips AI language patterns from your copy and restores the human voice.

Not a paraphraser. Trained on 1,000+ AI vs. human content comparisons.

Result: copy that sounds like you wrote it. Because you did.

Free on GitHub. Link in first reply.

---

## Mar 9 — Gumroad Bundle $49 — LI + X

**Type:** Bundle Feature
**Skill:** Claude Code Marketing Bundle
**Link:** https://brianrwagner.gumroad.com/l/brw-cc-marketing-bundle
**Posted:** ❌

### LinkedIn Draft

Eight Claude Code marketing skills. $49. Here's why the bundle exists.

Individually, the skills run $9–$19 each. Buy every one separately: $96.

The bundle is $49.

But the pricing isn't the main reason to buy it. The reason is the system.

These eight skills are designed to work together. The Brand Voice Extractor feeds into the Brand Positioning Audit. The AI Discoverability Audit informs your content angles. The Morning Brief System pulls competitor signals into weekly planning.

Bought separately, you get tools. Bought together, you get a workflow.

What's in the bundle:
- AI Discoverability Audit v2 ($19 alone)
- Founder Intelligence ($15 alone)
- Competitor Intel Brief ($12 alone)
- Morning Brief System ($14 alone)
- Brand Voice Extractor ($9 alone)
- AI Employee Onboarding ($9 alone)
- Brand Positioning Audit ($9 alone)
- Bundle guide — how to sequence them for max output

Built for marketing directors and founders who are done playing with AI and ready to actually use it.

Link in the comments.

---

### X Draft

8 Claude Code marketing skills. One system.

Individually: $96.
Bundle: $49.

But the savings aren't the point.

These skills feed each other: Brand Voice → Positioning → Discoverability → Intel. It's a workflow, not a toolbox.

Full breakdown in first reply.

---

## Mar 11 — plan-my-day — LI + X

**Type:** Free Drop
**Skill:** plan-my-day
**Link:** https://github.com/BrianRWagner/ai-marketing-claude-code-skills
**Posted:** ❌

### LinkedIn Draft

Free skill for the people who start every day with 47 tabs open and no real priority.

plan-my-day is a Claude Code skill that builds a time-blocked daily plan based on circadian rhythm research and GTD principles. Give it your task list and your energy patterns — it gives back a sequenced day where the hard work happens when your brain is actually capable of it.

Built this one for myself.

The problem wasn't productivity apps. Had those. The problem was front-loading admin tasks during peak focus (8–11am) and saving deep work for 3pm when the brain was gone.

The skill asks three questions: What needs to happen today? What's your energy curve? What's non-negotiable?

Output: a morning/midday/afternoon block schedule. Not a list. An actual sequenced plan.

Free on GitHub. Link in the comments.

---

### X Draft

Free Claude Code skill:

plan-my-day → time-blocked daily schedule based on your energy curve + task list.

Not a to-do app. A sequenced plan built around when your brain actually works.

Built this because I kept doing admin at 9am and deep work at 3pm. Fixed.

Free on GitHub. Link in first reply.

---

## Mar 13 — Founder Intelligence — LI + X

**Type:** Spotlight
**Skill:** Founder Intelligence
**Link:** https://brianrwagner.gumroad.com/l/brw-cc-marketing-bundle
**Posted:** ❌

### LinkedIn Draft

Ten years of founder notes. Bezos, Buffett, Grove, Helmer, Hormozi. Hundreds of frameworks from business books and podcasts.

The Founder Intelligence skill turns that library into a live advisory system.

Here's how it works: you describe the business problem you're facing. The skill pulls the most relevant frameworks, applies them to your specific situation, and delivers a decision framework — not generic advice, but the specific mental model the right founder would use for your exact problem.

Real use case: a founder deciding whether to raise $500K or stay bootstrapped. Instead of advisors who hedge, they run Founder Intelligence. Output: Buffett's owner-earnings framing applied to their unit economics + Hormozi's constraint-identification framework applied to their growth stage. Decision: bootstrapped, one clear constraint to eliminate first.

That's not ChatGPT giving you a pro-con list. That's 60 years of business thinking applied to a specific decision in 20 minutes.

$15 standalone or part of the $49 bundle.

Link in the comments.

---

### X Draft

10 years of founder notes — Bezos, Buffett, Grove, Hormozi — turned into a live decision framework.

Describe your business problem.
Get the exact mental model the right founder would use.

Not a pro-con list. Applied strategic thinking.

$15 standalone or in the $49 bundle. Link in first reply.

---

## Mar 15 — First Month Milestone — LI + X

**Type:** Social Proof
**Skill:** All (marketplace milestone)
**Link:** https://shopclawmart.com
**Posted:** ❌

### LinkedIn Draft

Mid-March check-in on the $500 Challenge.

The challenge started Feb 20. Goal: $500 in AI skill revenue in 30 days, organic only.

Numbers to date:
- Claw Mart: $97 in week 1, tracking upward
- Gumroad: launched Feb 26, early sales coming in
- Total skills listed: 19 free (GitHub) + 15 paid across both platforms
- Buyers in multiple countries, zero of whom I've ever met

The insight nobody tells you about selling digital products:

The feedback loop is instant and unforgiving. Someone downloads a skill and it doesn't deliver — they don't email you, they just don't come back. Every sale is a vote that the thing actually worked.

That accountability has made the builds tighter. The skills shipped in the last 3 weeks are more specific and more useful than anything built in the first year of experimenting with Claude.

The $500 finish line matters less now than building the system that gets there consistently.

Still tracking. Final count goes up March 20.

---

### X Draft

$500 Challenge — mid-March:

Week 1: $97 Claw Mart
Week 2: tracking up
Gumroad launched Feb 26, early sales in
19 free skills, 15 paid, buyers in multiple countries

Insight: instant feedback loop. Either it works or they don't come back.

Made me a better builder. Final count March 20.

---

## Mar 17 — Brand Voice Extractor — LI + X

**Type:** Spotlight
**Skill:** Brand Voice Extractor
**Link:** https://brianrwagner.gumroad.com/l/brw-cc-marketing-bundle
**Posted:** ❌

### LinkedIn Draft

Here's a pattern that keeps showing up: brands spend 3 months building a voice guide. Then every piece of content sounds different anyway.

Because the guide lives in a Google Doc. The writing happens in a chatbot.

The Brand Voice Extractor closes that gap.

It pulls your actual brand voice from existing content — best blog posts, top-performing LinkedIn posts, your About page, founder interviews — and converts it into a structured Claude Code prompt layer. Paste it into any Claude session. Every output in that session matches your voice.

Not "write in a warm, professional tone." Specific. Calibrated. Yours.

Built this after a client showed a brand guide that was 40 pages long and a content team that ignored 38 of them because nobody had time to re-read 40 pages before every post.

The extractor produces a 2-page brief. Tone markers. Sentence rhythm. Banned phrases. Example outputs. Everything Claude needs to write like your brand writes.

$9. Runs in Claude Code. Link in the comments.

---

### X Draft

2

---

## Mar 19 — cold-outreach-sequence — LI + X

**Type:** Free Drop
**Skill:** cold-outreach-sequence
**Link:** https://github.com/BrianRWagner/ai-marketing-claude-code-skills
**Posted:** ❌

### LinkedIn Draft

Free skill. For founders and consultants doing outbound.

cold-outreach-sequence generates a 5-email cold outreach sequence calibrated to your offer, your ICP, and the specific objection you're most likely to hit.

Not a template filler. The sequence adapts based on deal size, buyer type (founder vs. VP vs. enterprise), and whether you have a mutual connection or are going in cold.

Output: subject lines, body copy for each email, send cadence, and the one objection each email is designed to preempt.

Built this because a founder spent two hours on a cold email that got no reply — then sent the same email 200 times. The problem wasn't effort. Every email sounded like it was written for everyone.

The skill forces specificity. ICP first. Then offer. Then objection. The output follows.

Free on GitHub. Link in the comments.

---

### X Draft

Free Claude Code skill for anyone doing outbound:

cold-outreach-sequence → 5-email sequence calibrated to your ICP, offer, and most likely objection.

Not a template filler. Adapts to deal size, buyer type, warm vs. cold.

Most cold email failures: one email written for everyone.

Free on GitHub. Link in first reply.

---

## Mar 21 — Claw Mart Complete Bundle $44 — LI + X

**Type:** Bundle Feature
**Skill:** Claw Mart Complete Bundle
**Link:** https://shopclawmart.com
**Posted:** ❌

### LinkedIn Draft

The Claw Mart bundle is built for a different workflow than the Gumroad bundle.

Overlapping skills. Different platform. Different use case.

Gumroad runs in Claude Code — own the files, run them locally, total control.

Claw Mart runs in OpenClaw — the AI agent platform that handles memory, scheduling, and multi-agent orchestration. If you're building an agent-powered workflow (not just a one-off script), Claw Mart is the right home.

The Complete Bundle ($44) includes:
- Chief of Staff ($19 alone) — AI operator that manages tasks, briefs, and priorities
- Multi-Agent Team Blueprint ($19 alone) — how to build and run a team of specialized agents
- Founder Intelligence ($15 alone)
- Voice Extractor ($9 alone)
- Brand Positioning Audit ($9 alone)
- AI Employee Onboarding ($9 alone)

Individual total: $80. Bundle: $44.

The Chief of Staff + Multi-Agent Blueprint pairing alone is worth the price. That combination is how you go from "I use AI" to "AI runs workflows while I sleep."

Link in the comments.

---

### X Draft

Gumroad bundle = Claude Code. Own the files, run locally.

Claw Mart bundle = OpenClaw. Memory, scheduling, multi-agent orchestration.

Same skills. Different operating system for your AI stack.

Complete Bundle: $44 (vs $80 individual). Link in first reply.

---

## Mar 23 — Chief of Staff — LI + X

**Type:** Spotlight
**Skill:** Chief of Staff
**Link:** https://shopclawmart.com
**Posted:** ❌

### LinkedIn Draft

The Chief of Staff skill is the one that runs every day.

Here's what it actually does: it runs on OpenClaw as a persistent agent with memory. Brief it in the morning — priorities, pending decisions, things to track. It structures your day, drafts follow-ups, flags what's slipping, and maintains context across sessions.

Not a task app. An operator.

The difference: a task app holds a list. The Chief of Staff holds context. It knows what you decided last Tuesday about the content strategy. It knows you're tracking toward a revenue deadline. It connects dots you don't have time to connect manually.

Built this because four different tools were doing what one structured agent should handle. Calendar, Notion, Telegram, email — all separate, all requiring me to be the context bridge.

Now the agent holds the context. Just show up and work.

$19 on Claw Mart. Requires OpenClaw (free plan available). Link in the comments.

---

### X Draft

Chief of Staff = a persistent AI agent with memory that runs your day.

Morning brief → structured priorities. Pending decisions tracked. Context held across sessions.

Not a task app. An operator.

$19 on Claw Mart. Link in first reply.

---

## Mar 25 — Build in Public: The System Behind the Skills — LI + X

**Type:** Build in Public
**Skill:** All skills (process)
**Link:** https://github.com/BrianRWagner/ai-marketing-claude-code-skills
**Posted:** ❌

### LinkedIn Draft

Here's how a Claude Code skill actually gets built. Start to finish.

**Step 1: The problem has to be real.**
Every skill started with a specific moment — a founder staring at a blank doc, a client whose brand guide wasn't working, a marketer sending cold emails at 11pm with no system. If the specific person can't be named, don't build the skill.

**Step 2: Run the manual version first.**
Before writing a single line of prompt architecture, do the task by hand. The homepage audit — 5 homepages audited manually, every pattern logged. That log became the skill logic.

**Step 3: Prompt architecture, not just a prompt.**
The difference between a skill and a ChatGPT prompt is structure. Skills have stages, decision trees, output formats, and examples baked in. The output is consistent across users.

**Step 4: Test with someone who wasn't part of the build.**
If they can run it cold, without explanation, it ships. If they have questions, fix the skill until they don't.

**Step 5: Document the output, not the process.**
GitHub README shows what the skill produces, not how it works internally. People want results.

19 free. 15 paid. All built this way.

---

### X Draft

How I build a Claude Code skill (the actual process):

1. Name the specific person with the problem
2. Do the task manually first
3. Build prompt architecture, not just a prompt
4. Test with someone cold — if they ask questions, fix it
5. Document the output, not the process

19 free. 15 paid. Same method every time.

---

## Mar 27 — Competitor Intel Brief — LI + X

**Type:** Spotlight
**Skill:** Competitor Intel Brief
**Link:** https://brianrwagner.gumroad.com/l/brw-cc-marketing-bundle
**Posted:** ❌

### LinkedIn Draft

Every marketing team tracks competitors. Almost none track the right things.

The Competitor Intel Brief ($12) changes what you look at.

Standard competitive analysis covers: features, pricing, website copy, social presence. The brief covers those — then goes deeper. It tracks how competitors are positioning in AI-generated results, which content angles are gaining traction in their category, where customer reviews expose product gaps, and what hiring pages reveal about strategic direction.

That last one is underused. A competitor's open roles tell you what they're building next. The brief pulls that signal into a quarterly positioning doc.

Output: a structured 2-page brief you can drop into a leadership meeting. What's changed, what to watch, where there's a positioning gap to move into.

Built this after watching a CMO get blindsided in a board meeting by a competitor move that had been visible in the market for 90 days — if you knew where to look.

$12 standalone. Part of the $49 Gumroad bundle.

Link in the comments.

---

### X Draft

Competitive intel most teams miss:

→ AI search positioning (are they showing up when you're not?)
→ Customer review gaps (what buyers wish the product did)
→ Hiring pages (what they're building next)

Competitor Intel Brief pulls all of it into a 2-page quarterly brief.

$12. Link in first reply.

---

## Mar 29 — homepage-audit — LI + X

**Type:** Free Drop
**Skill:** homepage-audit
**Link:** https://github.com/BrianRWagner/ai-marketing-claude-code-skills
**Posted:** ❌

### LinkedIn Draft

Free skill. This one lands differently.

homepage-audit runs a structured 20-point diagnostic on any homepage. Paste the URL. It evaluates headline clarity, value prop specificity, CTA hierarchy, social proof placement, and 16 other conversion factors.

Output: a scored gap report with specific recommendations. Not "improve your headline" — "your headline describes a feature, not an outcome; here's the rewrite formula."

The benchmark: a homepage should answer 5 questions for a first-time visitor in under 10 seconds. What do you do? Who is it for? Why should I trust you? What do I get? What do I do next? The audit checks all five.

Run this on 30+ homepages in the last 3 months. Most common failure: burying the specific ICP behind language that tries to appeal to everyone. Universal language converts nobody.

Free on GitHub. If you have a homepage getting traffic but not converting — this is the 30-minute diagnosis.

Link in the comments.

---

### X Draft

Free Claude Code skill:

homepage-audit → 20-point diagnostic on any homepage. Scored gap report with specific fixes.

Not "improve your headline." Specific: "your headline describes a feature, not an outcome. Here's the rewrite."

Most common failure I find: language written for everyone that converts nobody.

Free on GitHub. Link in first reply.

---

## Mar 31 — March Wrap + What's Next — LI + X

**Type:** Social Proof
**Skill:** All (monthly milestone)
**Link:** https://shopclawmart.com
**Posted:** ❌

### LinkedIn Draft

March is done. Here's the $500 Challenge final count.

Started Feb 20. Goal: $500 in AI skill revenue in 30 days, organic only, no ads.

Final numbers:
- Claw Mart: [update with final figure]
- Gumroad: [update with final figure]
- Total: [update when confirmed]
- Skills published: 19 free (GitHub) + 15 paid
- Buyers across multiple countries

Whether the number hit $500 or not: the system is real.

In 40 days, went from zero published skills to a functioning marketplace with paying buyers across markets I've never advertised in, for products that didn't exist 6 weeks ago.

That's what "AI systems for marketers" means. Not the concept — the proof.

What's next: April is about depth over breadth. Fewer new skills, more value in the ones selling. V2 updates. A proper bundle landing page. WRS work in full gear.

If you've been watching this build — thank you. More coming.

---

### X Draft

$500 Challenge — final count:

[Final numbers when confirmed]

40 days. Zero → functioning skills marketplace. Paying buyers in multiple countries. No ads.

That's what "AI systems for marketers" means in practice.

April: depth over breadth. V2 updates. WRS full ramp.

Thank you for watching.

---

*End of March Skills Content Plan*
*16 posts | 32 total drafts (LI + X) | Every 2 days, March 1–31*
*Built by Scribe — Feb 27, 2026*
```

## File: `ai-discoverability-audit/SKILL-OC.md`
```markdown
---
name: ai-discoverability-audit
description: Audit how a brand appears in AI-powered search (ChatGPT, Perplexity, Claude, Gemini). Use when user mentions "AI search," "how do I show up in ChatGPT," "AI discoverability," "AEO," "LLM visibility," or wants to understand their brand's AI presence.
---

**Platform:** OpenClaw (token-optimized)

## Required Inputs (collect before starting)

- Company name + website URL
- Primary product/service + category
- Target customer (specific role/situation)
- Geography
- Top 3 competitors (real names)
- Prior audit results (if any — triggers comparison mode)
- Current positioning statement (if available)

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | Phase 1 only + top 3 fixes | Fast check |
| `standard` | All 4 phases + scored report + roadmap | Default |
| `deep` | Full + competitive benchmarking + 90-day plan | Full overhaul |

## Workflow

**1. Pre-audit hypothesis**
State expected recognition level (strong/moderate/weak), main risk (misattribution / missing / weak authority), competitor most likely to dominate.

**2. Direct brand queries** — run on ChatGPT + Perplexity + Claude:
- "What is [Company]?"
- "What does [Company] do?"
- "Is [Company] any good?"
- "What do people say about [Company]?"

For each: AI knows brand? Description accurate? Sentiment? Sources cited? Misattribution detected?

**3. Category queries** — does brand appear when ICP asks category questions?
- "Best [category] tools for [audience]"
- "Alternatives to [Competitor A]"
- "[Category] recommendations"

**4. Competitive benchmarking** — run same queries for top 3 competitors. Score each: Mentioned / Not mentioned / Partially mentioned.

**5. Score each section 1–5:**
- Brand recognition (direct queries)
- Description accuracy (vs. stated positioning)
- Category presence (category queries)
- Sentiment quality
- Competitive gap

**6. Priority roadmap**
- Do This Week (score <3, quick wins)
- This Month (score 3–4, content/authority fixes)
- Long-term (structural positioning work)

## Output Structure

```
## AI Discoverability Audit: [Brand] — [Date]

### Pre-Audit Hypothesis
[Expected recognition + main risk]

### Query Results Summary
| Query | ChatGPT | Perplexity | Claude | Score |
|-------|---------|------------|-------|-------|

### Section Scores
| Section | Score /5 | Gap |
|---------|----------|-----|

### Overall Score: X/25 — [Rating]

### Priority Roadmap
**Do This Week:**
1. [Specific action]

**This Month:**
1. [Specific action]

### Re-audit Schedule: [Date + 90 days]
```

If prior audit exists: show `[Prior Score] → [New Score] = [Delta]` for each section.

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `ai-discoverability-audit/SKILL.md`
```markdown
---
name: ai-discoverability-audit
description: Audit how a brand appears in AI-powered search (ChatGPT, Perplexity, Claude, Gemini). Use when user mentions "AI search," "how do I show up in ChatGPT," "AI discoverability," "AEO," "LLM visibility," or wants to understand their brand's AI presence.
---

# AI Discoverability Audit

You are an AI discoverability expert. Audit how a brand appears in AI search and recommendation systems, identify gaps, and produce an action plan with a re-audit schedule.

**Why This Matters:** Traditional SEO optimizes for Google. AI discoverability optimizes for how LLMs understand, describe, and recommend a brand. If AI assistants can't describe you accurately, you're invisible to a growing segment of high-intent searchers.

---

## Mode

Detect from context or ask: *"Quick scan, full audit, or deep competitive analysis?"*

| Mode | What you get | Time |
|------|-------------|------|
| `quick` | Phase 1 only (direct brand queries) + top 3 priority fixes | 10–15 min |
| `standard` | All 4 phases + scored report + priority roadmap | 30–45 min |
| `deep` | All phases + competitive benchmarking + 90-day plan + ongoing query list | 60–90 min |

**Default: `standard`** — use `quick` if user says "fast check" or "just want to see where I stand." Use `deep` if they're planning a content or SEO overhaul.

---

## Context Loading Gates

**Before running any queries, collect:**

- [ ] **Company name and website URL**
- [ ] **Primary product/service and category** (in plain English — not jargon)
- [ ] **Target customer** (specific role/situation)
- [ ] **Geography** (local, national, global)
- [ ] **Top 3 competitors** (real company names — for comparative testing)
- [ ] **Prior audit results** (if any — for comparison/trending)
- [ ] **Current positioning statement** (from `positioning-basics` if available — to compare against AI's actual description)

**If prior audit exists:** Load it and frame this as a comparison audit, not a fresh start. Produce a trend comparison at the end.

---

## Phase 1: Pre-Audit Analysis

Before running queries, reason through:

1. **Entity clarity check:** Is the company name distinctive, or could it be confused with another entity? Common names (e.g., "Signal") are more likely to be misattributed.
2. **Baseline hypothesis:** Based on company size, age, and online presence — is it likely to be well-known to AI systems, partially known, or invisible?
3. **Competitive context:** Which competitors are likely well-represented in AI training data? This informs where the gaps will be.
4. **Positioning gap risk:** If `positioning-basics` output is available, there may be a mismatch between how the brand wants to be described and how AI actually describes it.

Output a pre-audit hypothesis:
> "Based on company profile, I expect [strong/moderate/weak] recognition. Main risk: [misattribution / missing from category / weak authority]. Competitor most likely to dominate: [name]."

---

## Phase 2: Structured Query Testing

**Web access:** Run queries directly if available. If not, provide exact queries for the user to run and paste results.

### Direct Brand Queries (run on ChatGPT AND Perplexity AND Claude)

```
1. "What is [Company]?"
2. "What does [Company] do?"
3. "Is [Company] any good?"
4. "What do people say about [Company]?"
```

**Document per query:**
- AI knows the brand? (Yes / No / Partial)
- Description accurate? (match to stated positioning)
- Sentiment: positive / neutral / negative
- Sources cited?
- **Misattribution check:** Wrong founder? Wrong industry? Confused with competitor?

### Category Queries

```
1. "What are the best [category] companies?"
2. "Who should I hire for [service] in [location]?"
3. "Recommend a [product/service] for [use case]"
4. "[Top Competitor] alternatives"
```

**Document:** Brand appears? Position in list? Which competitors appear instead?

### Expertise Queries

```
1. "Who are the experts in [industry]?"
2. "What are best practices for [topic]?"
3. "[Founder name] — who is this?"
```

**Document:** Cited? Content referenced? Competitors cited instead?

### Competitive Comparison Matrix

Run the same queries for top 3 competitors and compare:

| Query Type | Your Brand | [Competitor A] | [Competitor B] | [Competitor C] |
|---|---|---|---|---|
| Direct recognition | | | | |
| Category presence | | | | |
| Authority citations | | | | |
| Sentiment | | | | |

---

## Phase 3: Structured Scoring

Rate each dimension 1-5 using explicit criteria:

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| **Recognition** | AI doesn't know the brand | Partial/vague knowledge | Accurate, detailed description |
| **Accuracy** | Wrong info / misattribution | Mostly right, minor gaps | Fully accurate and current |
| **Sentiment** | Negative or skeptical | Neutral | Positive with specific reasons |
| **Category Presence** | Never appears in category queries | Occasionally appears | Consistently in top 3 |
| **Authority** | Never cited as expert | Occasionally mentioned | Regularly cited for expertise |
| **Competitive Position** | Dominated by competitors | On par | Clearly leads in AI recommendations |

**Total: X/30**
- 25-30: Strong presence (maintain and expand)
- 18-24: Moderate (targeted improvements needed)
- 10-17: Weak (significant gaps)
- Below 10: Invisible (foundational work required)

---

## Phase 4: Gap Analysis & Recommendations

**Classify each gap:**

| Priority | Trigger | Timeline |
|---|---|---|
| Critical | Factual errors, misattribution, brand not recognized | Fix now |
| High | Weak descriptions, missing from recommendations | 30 days |
| Opportunity | Adjacent categories, founder thought leadership | 90 days |

**Recommendation categories:**

**Entity Clarity (Foundation):**
- Fix factual errors in source material AI trains on
- Claim Google Knowledge Panel
- Create AI-parseable "About" page with clear entity signals

**Trust Signals:**
- 10+ reviews on G2, Capterra, or Google
- Consistent directory listings
- Structured schema markup (org, product, review)

**Content Authority:**
- 3-5 answer-worthy articles targeting category questions directly
- Wikipedia presence (if notable)
- Founder bylines in authoritative publications

**Competitive Gap:**
- If competitor dominates a category query → publish a direct comparison piece
- If competitor appears in "[Brand] alternatives" → create better content targeting that query

**Constraint:** Never recommend keyword stuffing, fake reviews, or misleading schema. These tactics risk penalties and undermine genuine authority.

---

## Phase 5: Self-Critique Pass (REQUIRED)

After completing the audit:

- [ ] Did I run queries on at least 2 AI platforms, or only one?
- [ ] Did I check for misattribution specifically (not just presence)?
- [ ] Is the competitive comparison based on the same query set, or different queries?
- [ ] Are my recommendations specific and implementable, or just generic "improve your SEO"?
- [ ] Is the re-audit schedule set with specific dates and what to measure?
- [ ] If prior audit exists: did I actually compare scores and show the trend?

Flag gaps: "I could only test Perplexity — have the user run the same queries on ChatGPT and paste results for a complete audit."

---

## Phase 6: Re-Audit Schedule (MANDATORY)

Set specific re-audit dates before delivering:

**30-day re-audit:** After implementing critical fixes — did recognition improve?
**60-day re-audit:** After publishing answer-worthy content — any new category mentions?
**90-day re-audit:** Full comparative re-audit — full trend comparison to this baseline

**Comparison table format for future audits:**
```
| Dimension | [Baseline Date] | 30-Day | 60-Day | 90-Day | Δ |
|---|---|---|---|---|---|
| Recognition | [X/5] | | | | |
| Category | [X/5] | | | | |
| Authority | [X/5] | | | | |
| Total | [X/30] | | | | |
```

---

## Output Structure

```markdown
## AI Discoverability Audit: [Company] — [Date]

### Pre-Audit Hypothesis
[Prediction + reasoning]

---

### Phase 1: Direct Brand Queries
**ChatGPT:** [findings]
**Perplexity:** [findings]
**Claude:** [findings]
**Misattribution found:** [Yes/No — details]

### Phase 2: Category Queries
[Findings per query]

### Phase 3: Expertise Queries
[Findings]

### Competitive Comparison
[Table with real competitor names]

---

### Scores
| Dimension | Score |
|---|---|
| Recognition | /5 |
| Accuracy | /5 |
| Sentiment | /5 |
| Category Presence | /5 |
| Authority | /5 |
| Competitive Position | /5 |
| **TOTAL** | **/30** |

**Rating:** [Strong / Moderate / Weak / Invisible]

---

### Gap Analysis

**Critical (Fix Now):**
1. [Specific fix]

**High Priority (30 Days):**
1. [Specific fix]

**Opportunities (90 Days):**
1. [Specific improvement]

---

### Re-Audit Schedule
- 30-day: [YYYY-MM-DD] — measure: [what to check]
- 60-day: [YYYY-MM-DD] — measure: [what to check]
- 90-day: [YYYY-MM-DD] — full comparative re-audit

### Self-Critique Notes
[Any gaps, limitations, or things the user needs to run manually]
```

---

*Skill by Brian Wagner | AI Marketing Architect | brianrwagner.com*
```

## File: `ai-discoverability-audit/references/query-bank.md`
```markdown
# AI Discoverability Query Bank

Ready-to-use queries organised by category. Copy/paste into ChatGPT, Perplexity, Claude, and Gemini.

---

## Brand Recognition Queries

### Direct Brand
- "What is [Company]?"
- "Tell me about [Company]"
- "What does [Company] do?"
- "Who founded [Company]?"
- "[Company] reviews"
- "Is [Company] legit?"
- "Is [Company] any good?"
- "[Company] pros and cons"

### Brand + Location
- "[Company] [City]"
- "Is [Company] based in [City]?"
- "[Company] headquarters"

### Brand + Category
- "Is [Company] a good [category] company?"
- "How does [Company] compare to other [category] providers?"

---

## Category Discovery Queries

### Best-of Lists
- "Best [category] companies"
- "Top [category] providers in [year]"
- "Best [category] for [use case]"
- "Best [category] for small businesses"
- "Best [category] for enterprises"
- "Affordable [category] options"
- "Premium [category] providers"

### Location-Based
- "Best [category] in [city]"
- "[Category] companies near me"
- "Top [category] in [state/region]"
- "Local [category] recommendations"

### Use-Case Specific
- "Best [category] for [specific need]"
- "[Category] for [industry]"
- "[Category] for startups"
- "[Category] for [target customer]"

### Alternative Queries
- "[Competitor] alternatives"
- "Companies like [Competitor]"
- "[Competitor] vs [Competitor]"
- "Cheaper alternatives to [Competitor]"

---

## Authority & Expertise Queries

### Expert Recognition
- "Who are the experts in [industry]?"
- "Top [industry] thought leaders"
- "[Industry] influencers to follow"
- "Best [industry] consultants"

### Knowledge Queries
- "Best practices for [topic]"
- "How to [solve problem]"
- "What should I know about [topic]?"
- "[Topic] guide"
- "[Topic] framework"

### Founder/Leader
- "[Founder name]"
- "Who is [Founder name]?"
- "[Founder name] [Company]"
- "[Founder name] expertise"

---

## Problem-Aware Queries

### Pain Point Queries
- "How to solve [problem brand solves]"
- "Why is [problem] so hard?"
- "[Problem] solutions"
- "Help with [problem]"

### Comparison Queries
- "Should I use [solution A] or [solution B]?"
- "[Your approach] vs [alternative approach]"
- "Pros and cons of [solution type]"

---

## Industry-Specific Templates

### SaaS/Tech
- "Best [category] software"
- "[Category] tools for [use case]"
- "[Category] platform comparison"
- "[Competitor] pricing vs alternatives"

### Professional Services
- "Best [service] firm in [city]"
- "[Service] consultants for [industry]"
- "How to choose a [service] provider"
- "[Service] firm reviews"

### Local Business
- "[Service] near me"
- "Best [service] in [neighborhood]"
- "[Service] open now"
- "Affordable [service] [city]"

### E-commerce/DTC
- "Best [product category]"
- "Where to buy [product]"
- "[Product] reviews"
- "[Brand] vs [Competitor] [product]"

---

## Monitoring Queries (Run Monthly)

Track these consistently to measure progress:

1. "[Company name]" - Direct brand recognition
2. "Best [primary category] companies" - Category presence
3. "[Main competitor] alternatives" - Competitive positioning
4. "[Founder name]" - Personal brand
5. "How to [primary problem you solve]" - Expertise citation

---

## Platform-Specific Notes

### ChatGPT
- Most widely used, largest influence
- Knowledge cutoff affects recency
- Web browsing mode accesses current info

### Perplexity
- Cites sources explicitly
- More current information
- Good for tracking which sources get cited

### Claude
- Strong reasoning, less browsing
- Good for testing brand understanding
- May have older knowledge cutoff

### Gemini
- Google integration
- Good for testing local/maps presence
- May favour Google properties

---

## Scoring Quick Reference

For each query, rate:

| Score | Recognition | Description |
|-------|-------------|-------------|
| 5 | Excellent | Featured prominently, accurate, positive |
| 4 | Good | Mentioned, mostly accurate |
| 3 | Moderate | Mentioned but vague or incomplete |
| 2 | Weak | Barely mentioned or with errors |
| 1 | None | Not mentioned at all |
```

## File: `case-study-builder/SKILL-OC.md`
```markdown
---
name: case-study-builder
description: Turn client wins into formatted case studies for proposals, social proof, and sales conversations. Use when someone needs to document results, build credibility, or create reusable proof assets.
---

**Platform:** OpenClaw (token-optimized)

## Required Inputs (all 8 — do not draft without them)

| Field | What to Collect |
|-------|-----------------|
| Client | Industry, company size/stage, named or anonymized? |
| Before | What was broken/painful? Any numbers? |
| Actions | What did you do? Scope, timeline, role |
| After | **Required: at least one specific number** |
| Timeline | How long to achieve the result? |
| Quote | Direct client quote (if available) |
| Naming | Can we name client, or anonymize? |
| Use case | Proposals / website / LinkedIn |

**Outcome gate:** If user says "things improved" — stop and ask: "Give me one number — revenue, time saved, lead volume, or rough estimate. Do not draft without it."

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | 1 format: proposal paragraph | Fast, one-off |
| `standard` | 3 formats: blurb + pull-quote + sales story | Default |
| `deep` | 3 formats + blog-ready + FAQ variant + campaign assets | Full asset package |

## Result Tiers (affects language confidence)

| Tier | Type | Language |
|------|------|----------|
| 1 | Hard metric (40% revenue) | State directly |
| 2 | Soft metric (team aligned) | "For the first time..." |
| 3 | Proxy (enabled Series A) | "Contributed to..." |
| 4 | Directional | "Significant improvement..." |

## Three Format Templates

**Short (2-liner — homepage, LinkedIn):**
```
"[Result sentence — lead with outcome]"
— [Name], [Title] at [Company]
```

**Medium (2-3 sentences — services page, sales deck):**
```
"[Problem/situation]. [What changed]. [Recommendation or result]."
— [Name], [Title] at [Company]
```

**Long (narrative — case study page):**
1. Context paragraph (situation)
2. Transformation paragraph (what happened)
3. Results paragraph (outcomes + numbers)
4. Closing recommendation sentence

## Self-Critique Before Delivering

- [ ] Short version has at least one concrete outcome (not "great results")
- [ ] Reads like the client wrote it, not a marketing headline
- [ ] Format length matches stated use case
- [ ] No claims or numbers you added that the client didn't make

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `case-study-builder/SKILL.md`
```markdown
---
name: case-study-builder
description: Turn client wins into formatted case studies for proposals, social proof, and sales conversations. Use when someone needs to document results, build credibility, or create reusable proof assets.
---

# Case Study Builder

Everyone wants social proof. Nobody makes time to create it. You finish a project, the client's happy, you move on — and six months later you're in a sales call with nothing to show.

This skill fixes that. Give me the raw details. I'll produce three formats you can use immediately.

---

## Mode

Detect from context or ask: *"Quick writeup, full case study, or full asset package?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | 1 format: paragraph summary for proposals | Fast social proof, proposal inserts |
| `standard` | 3 formats: proposal blurb, social proof pull-quote, sales story | Active pitching, LinkedIn, website |
| `deep` | 3 formats + blog-ready case study + FAQ variant + campaign assets | Content marketing, SEO, sales enablement |

**Default: `standard`** — use `quick` if they say "just need something fast." Use `deep` if they want to turn the win into a marketing asset.

---

## Context Loading Gates

**Before generating anything, collect all 8 fields:**

| Field | What to Collect |
|---|---|
| 1. Client | Industry, company size/stage, named or anonymized? |
| 2. Before | What was broken or painful? Any numbers? |
| 3. Actions | What did you specifically do? Scope, timeline, role |
| 4. After | **REQUIRED: at least one specific number** |
| 5. Timeline | How long to achieve the result? |
| 6. Quote | Direct client quote if available |
| 7. Naming | Can we name the client, or must we anonymize? |
| 8. Use case | Where will this be used? (proposals / website / LinkedIn) |

**Outcome Extraction Protocol — enforced on Field 4:**

If the user says "results were good" or "things improved," stop and ask:
> "I need at least one number to make this credible. Pick one:
> - Revenue change (e.g., 'closed 3 new clients worth $15K')
> - Time saved (e.g., 'cut from 10 hours to 2 hours/week')
> - Lead volume (e.g., 'went from 0 to 5 inbound leads/month')
> - Rough estimate is fine — it doesn't have to be exact."

**Do not draft until Field 4 has at least one number.**

---

## Phase 1: Situation Analysis

Before drafting, reason through:

1. **Result strength:** Is the outcome a Tier 1 (hard metric), Tier 2 (soft metric), or Tier 3 (proxy)? This determines how confident the language should be.
2. **Hero check:** Is the story told from the client's perspective, or yours? Client = hero, you = guide.
3. **Tension check:** What made this hard? Without a challenge, there's no story — just a list.
4. **Format match:** Which use case did they specify? That determines which format to optimize.

**Tier system for results language:**

| Tier | Type | Example | Language |
|---|---|---|---|
| 1 | Hard metric | "Revenue +40%" | State directly |
| 2 | Soft metric | "Team finally aligned" | "For the first time in years..." |
| 3 | Proxy metric | "Enabled Series A close" | "Contributed to..." |
| 4 | Directional | "Noticeable improvement" | "Significant improvement in..." |

---

## Phase 2: The Hero Principle

**The client is the hero. You are the guide.**

Before writing, flip the framing:

❌ Wrong: "I built a content system that generated leads."
✅ Right: "Sarah went from scrambling to fill her pipeline to getting 3 inbound inquiries per week — all from a content system we built in 6 weeks."

Every format should be written from what the CLIENT experienced, not what YOU delivered.

---

## Phase 3: Generate Three Formats

### Format 1: Two-Liner (Proposals & Bios)

**Formula:** `[What was done] + [scale/scope] + [for who] + [result or timeframe]`

```
[Strong action verb] [what was delivered] for [specific client descriptor].
[Outcome metric] in [timeframe].
```

**Example:**
> Built a full content system for a Series B SaaS founder with no marketing team.
> 0 to 3 inbound leads/week in 6 weeks.

---

### Format 2: Story Version (LinkedIn & Sales Calls)

**Structure — 4 paragraphs, 150–250 words:**

```
**Set the scene:** [Their situation when you arrived — 2-3 sentences with stakes]

**Show the complexity:** [What made this hard — 2-3 sentences]

**What happened:** [Specific actions taken — no feature lists, just moves]

**What changed:** [Outcome — the number + the transformation]
```

---

### Format 3: Full Case Study (Website & Portfolio)

```markdown
# Case Study: [Client Name or Descriptor]

## The Challenge
[2-3 paragraphs: situation, stakes, what wasn't working]

## The Approach
[Phases or steps — what happened and in what order]

## The Results
[Metrics, before/after comparison, named outcomes]

## Key Details
- Client: [Named or "A [descriptor] company"]
- Industry: [Sector]
- Timeline: [Duration]
- Scope: [What was delivered]

## What Made This Different
[Unique angle, unexpected obstacle, or pivotal insight]

## Client Quote
> "[Testimonial — or placeholder if not yet collected]"
> — [Name], [Title]
```

---

## Phase 4: Self-Critique Pass (REQUIRED)

After generating all three formats, evaluate:

**Two-liner:**
- [ ] Does it have a specific number? (Not "improved results" — a real metric)
- [ ] Is it 2 sentences or fewer?
- [ ] Would someone scanning a proposal stop and read it?

**Story version:**
- [ ] Is the client the hero (not the author)?
- [ ] Is there genuine tension — something that made this hard?
- [ ] Does the closing paragraph include the key metric?

**Full case study:**
- [ ] Does the Results section lead with numbers?
- [ ] Is the Challenge section specific enough that a similar prospect recognizes their situation?
- [ ] Is the client quote (or placeholder) present?

**Flag any failure:** "The story version has no tension — add one obstacle or unexpected challenge before the 'What happened' paragraph."

---

## Phase 5: Distribution Plan

| Format | Best locations | When to use |
|---|---|---|
| Two-liner | Proposals, email bios, LinkedIn About section | Any sales context |
| Story | LinkedIn post, podcast intros, sales call opener | Weekly content |
| Full case study | Website portfolio page, PDF download, RFP response | Late-stage buyer research |

---

## Output Structure

```markdown
## Case Study: [Client Descriptor] — [Date]

### Situation Summary
[2-sentence analysis from Phase 1]
Result tier: [1/2/3/4]

---

### Format 1: Two-Liner
[Final copy]

### Format 2: Story Version
[Final copy]

### Format 3: Full Case Study
[Full markdown]

---

### Self-Critique Notes
- Two-liner: [pass/issue]
- Story: [pass/issue]
- Full: [pass/issue]

### Distribution Plan
[Where to use each]

### Next Step
[If no quote collected → run testimonial-collector]
[If strong story → suggest LinkedIn post from story format]
```

---

**Cross-reference:** If a client quote was captured here, run `testimonial-collector` to properly format and score it for your testimonial library.

---

*Skill by Brian Wagner | AI Marketing Architect | brianrwagner.com*
```

## File: `cold-outreach-sequence/SKILL-OC.md`
```markdown
---
name: cold-outreach-sequence
description: Build personalized cold outreach sequences for LinkedIn and email. Use when someone needs to reach prospects, warm up cold leads, or build a systematic outreach engine. Covers research, connection requests, follow-ups, and conversion.
---

**Platform:** OpenClaw (token-optimized)

## Required Inputs

- Prospect name, company, role/title
- Research signals (run web_search before writing — see below)
- Sender positioning (ICP + outcome + unique approach)
- Platform: LinkedIn DM, email, or both?
- Batch size (determines tier assignment)

**Research tool calls (run before writing):**
```
web_search('[Company] [Name] news 2026')
web_search('[Company] funding recent')
web_search('[Person] LinkedIn')
```

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | 1 connection request + 1 follow-up | Single prospect |
| `standard` | Full 4-touch sequence | Active pipeline |
| `deep` | Multi-prospect system + A/B variants + tracking | Campaign launch |

## Personalization Tiers

| Research Result | Tier | Approach |
|-----------------|------|----------|
| Named signal (news/post/context) | Tier 1 | Fully custom — reference signal every message |
| Company info + role context | Tier 2 | Template + personalized opener |
| No signals found | Tier 3 | Volume template, minimal customization |

**Rule:** Do not write Tier 1 message without a named specific signal. If zero signals found, default to Tier 3 and say so.

## 4-Touch Sequence Structure

**Touch 1 — Connection Request (LinkedIn, 300 chars max):**
- Formula: [Specific observation from research] + [Simple reason to connect]
- No pitching. Prove you did research. Conversational.

**Touch 2 — First Message (after connection accepted, 2-3 days):**
- Lead with their world, not your pitch
- One specific observation → natural bridge to your work
- Soft CTA: question or observation, not "book a call"

**Touch 3 — Value Add (5-7 days later):**
- Share one relevant resource, insight, or connection
- No ask. Pure give.

**Touch 4 — Direct Ask (7 days later):**
- Clear, specific ask (15-min call, specific question)
- Make it easy to say yes or no
- No guilt, no pressure

## Email Sequence Structure

**Subject line rules:** Specific > clever. Reference their company or role.

**Email 1:** Research-led opener + clear value + soft ask
**Email 2 (3 days):** Different angle — case study or insight
**Email 3 (5 days):** Breakup email — honest, no pressure, leave door open

## Quality Rules (active on all output)

- No "I'd love to pick your brain"
- No "I hope this finds you well"
- No multi-paragraph pitches in Touch 1
- Every message must have one specific reference that proves research was done
- CTA matches the relationship stage — no premature asks

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `cold-outreach-sequence/SKILL.md`
```markdown
---
name: cold-outreach-sequence
description: Build personalized cold outreach sequences for LinkedIn and email. Use when someone needs to reach prospects, warm up cold leads, or build a systematic outreach engine. Covers research, connection requests, follow-ups, and conversion.
---

# Cold Outreach Sequence

Here's what I've learned about cold outreach: the word "cold" is the problem.

Spray-and-pray templates don't work. 10 minutes of research + a specific reference = not cold anymore. This skill builds the second kind.

---

## Mode

Detect from context or ask: *"One message, full sequence, or full outreach system?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | 1 connection request + 1 follow-up for a single prospect | Testing an angle, one-off outreach |
| `standard` | Full 4-touch sequence for a single prospect | Active pipeline, individual targets |
| `deep` | Multi-prospect sequence system + A/B variants + tracking framework | Launching an outreach campaign |

**Default: `standard`** — use `quick` if they give you one name and say "draft something." Use `deep` if they're building a repeatable outreach engine.

---

## Context Loading Gates

**Before writing any message, collect:**

- [ ] **Prospect name and company** — full name, company, role/title
- [ ] **Research signals** — run tool calls first (see below); do not write without them
- [ ] **Sender positioning** — what does the sender do, for whom, with what result? (Use `positioning-basics` output if available)
- [ ] **Platform** — LinkedIn DM, email, or both?
- [ ] **Batch size** — how many prospects? (determines tier assignment)

**Research tool calls — run before writing:**

```
web_search('[Company] [Founder/Name] news 2026')
web_search('[Company] funding recent')
web_search('[Person name] [Company] LinkedIn')
```

**Personalization constraint:** Do not write a Tier 1 message without a named specific signal from research. If search yields 0 signals, default to Tier 3 and say so explicitly.

---

## Phase 1: Research & Signal Assessment

For each prospect, document findings before drafting:

**Signal types (ranked by message strength):**
1. Recent news event (funding, launch, hire, press) → strongest signal
2. Recent LinkedIn post activity → strong signal
3. Company stage/growth data → medium signal
4. Role + industry awareness only → weak signal (Tier 3)

**Personalization tier assignment:**

| Research Result | Tier | Approach |
|---|---|---|
| Named signal (news + post + context) | Tier 1 | Fully custom, reference signal in every message |
| Company info + role context | Tier 2 | Template + personalized opener |
| No signals found | Tier 3 | Volume template, minimal customization |

---

## Phase 2: Sequence Generation

### Connection Request (LinkedIn) — 300 chars max

**Formula:** `[Specific observation from research] + [Simple reason to connect]`

**Rules:**
- No pitching
- Prove you did research (name the signal)
- One sentence, conversational
- Never "I'd love to pick your brain"

**By signal type:**
```
Recent funding: "Congrats on the Series A — the [investor] backing is a smart signal. Would love to connect."

Recent post: "Your post on [specific topic] resonated — been thinking the same thing. Happy to connect."

News/launch: "Saw the [product] launch — [specific detail] is smart positioning. Would love to connect."
```

---

### First Message (After Accept — Wait 24-48 Hours)

**Formula:** `[Thanks] + [Bridge to relevance] + [Light value] + [Soft question]`

**Template:**
```
Thanks for connecting. I work with [ICP description] on [specific outcome].

Curious — is [relevant function] something you own directly at [Company], 
or is that still founder-led?

Happy to share what I'm seeing work at similar-stage companies either way.
```

---

### Follow-Up #1 (Day 7)

**Formula:** `[Light nudge] + [New signal or angle] + [Easy out]`

**Constraint:** Do NOT write "following up" with nothing new. Add one new piece:
- A relevant article or trend
- A related insight you recently had
- A connection to something they posted

**Template:**
```
Bumping this up — came across [specific article/trend/insight] and 
thought of your situation at [Company].

[One sentence on why it's relevant to them.]

Happy to share more if useful. If not, no worries.
```

---

### Follow-Up #2 (Day 14)

Shift to email if LinkedIn hasn't converted, or try a different angle.

**Subject line options:**
- "[Company]'s [function] as you scale"
- "Saw your [post/news] — quick thought"
- "Question about [specific thing they're doing]"

**Email structure:**
```
[1-line hook tied to their specific situation]

[2-3 sentences: why you're reaching out + one proof point]

[Soft CTA — 1 sentence]
```

---

### Break-Up Message (Day 21)

```
I'll assume timing isn't right — totally get it. 

If [relevant pain point] becomes a priority down the road, happy to reconnect. 
Best of luck with [specific thing they're working on based on research].
```

**Post-break-up action:** Add to 6-month re-engagement list with a resurface date.

---

## Phase 3: Self-Critique Pass (REQUIRED)

After generating the full sequence, evaluate:

- [ ] Does every message reference the specific signal from research, or are they generic?
- [ ] Is the connection request under 300 characters?
- [ ] Does the first message ask a question (invite dialogue) rather than pitch?
- [ ] Does follow-up #1 add something genuinely new, or is it just "following up"?
- [ ] Does the break-up message reference something specific about their situation?
- [ ] Did I correctly assign the personalization tier, or am I over-personalizing a Tier 3 prospect?

Flag any issue: "The first message doesn't include a soft question — it reads as a pitch. Revised to invite dialogue."

---

## Pipeline Tracking Table

Always output a tracking table for the batch:

```markdown
| Prospect | Company | Platform | Tier | Sent Date | Response | Stage | Next Action | Resurface Date |
|---|---|---|---|---|---|---|---|---|
| [Name] | [Co] | LinkedIn | 1 | [date] | — | Connection sent | Wait 24-48h | — |
| [Name] | [Co] | Email | 2 | [date] | — | First email sent | Follow-up Day 7 | — |
```

---

## Iteration Protocol

After each response (or non-response), ask:
- Did the connection request get accepted? If low acceptance rate → revise the observation line
- Did the first message get a reply? If no → was the question soft enough, or did it feel like a pitch?
- Did follow-ups get ignored? If yes → try a different angle or acknowledge the silence directly

---

## Output Structure

```markdown
## Outreach Sequence: [Prospect Name] — [Date]

### Research Summary
- Signal type: [news / post / company info / none]
- Signal found: "[Specific detail]"
- Personalization tier: [1/2/3]
- Source: [URL or platform]

### Sequence

**Connection Request (LinkedIn):**
[Text — max 300 chars]

**First Message (Day 1-2 after accept):**
[Text]

**Follow-Up #1 (Day 7):**
[Text]

**Follow-Up #2 (Day 14):**
Platform: [LinkedIn / Email]
Subject: [if email]
[Text]

**Break-Up (Day 21):**
[Text]

### Pipeline Entry
| Prospect | Company | Platform | Tier | Stage | Next Action | Resurface Date |
|---|---|---|---|---|---|---|
| [Name] | [Co] | [Platform] | [Tier] | Connection sent | Wait 24-48h | — |

### Self-Critique Notes
[Any issues flagged + revisions made]
```

---

*Skill by Brian Wagner | AI Marketing Architect | brianrwagner.com*
```

## File: `content-idea-generator/SKILL-OC.md`
```markdown
---
name: content-idea-generator
description: Generate content ideas rooted in positioning. Use when someone needs "content ideas," "what should I post," "blog topics," "LinkedIn ideas," or is stuck on what to create.
---

**Platform:** OpenClaw (token-optimized)

## Required Inputs

- Positioning statement: "I help [specific audience] achieve [specific outcome] through [unique approach]"
- ICP top 3 frustrations or questions right now
- Recent wins or proof points (last 30 days)
- Content formats available (LinkedIn / Twitter / Newsletter / Video)
- Existing pillars from `linkedin-authority-builder` (if any — stay within them)

**Positioning gate:** If user can't complete the positioning sentence with specifics → stop. Run `positioning-basics` first.

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | 5 ideas, immediate | Breaking a block |
| `standard` | 10–15 positioned ideas with formats + rationale | Regular planning |
| `deep` | Full content calendar: pillars, formats, cadence, 30-day plan | Launch or overhaul |

## Workflow

**1. Context analysis**
Assess positioning strength → audit proof points → check platform match → identify content gap.

Output: "You're creating content for [audience] as a [role]. Strongest proof point: [X]. Biggest gap: [Y]."

**2. Freshness check (run before generating):**
```
web_search('[Topic] trending [Month Year]')
web_search('[ICP role] biggest challenges [Year]')
```
Include ≥1 current-moment hook in the batch.

**3. Generate ideas using 6 frameworks:**

| Framework | Template |
|-----------|----------|
| Problem Call-Out | "The #1 mistake [audience] makes with [topic]" |
| Here's What Works | Teach a specific process you've actually used |
| Contrarian Take | Challenge a common belief in your space |
| Before/After | "We went from [X] to [Y] by doing [Z]" |
| Curation/Synthesis | "5 things I learned from [experience/source]" |
| Prediction/Trend | "What [topic] will look like in [timeframe]" |

**4. Quality filter — reject any idea that:**
- Could be written by someone with zero experience in the space
- Doesn't connect to the stated positioning
- Is a generic "tips" list without specific proof

**5. Format tagging**
Tag each idea with: Platform | Format (Story/Framework/Hot Take/Case Study) | Funnel stage (Awareness/Trust/Conversion)

## Output Format

```
## Content Ideas: [Name] — [Date]

### Strategy Note
[Positioning + biggest gap to fill]

### Idea Batch
1. **[Hook/Title]**
   Platform: | Format: | Stage:
   Angle: [1 sentence on the specific take]
   Proof point to use: [What real experience grounds this]

[repeat x10-15]

### Recommended First Post
[The one to write today — and why]
```

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `content-idea-generator/SKILL.md`
```markdown
---
name: content-idea-generator
description: Generate content ideas rooted in positioning. Use when someone needs "content ideas," "what should I post," "blog topics," "LinkedIn ideas," or is stuck on what to create.
---

# Content Idea Generator

Content without positioning is noise. Before generating ideas, confirm positioning is clear. If not, run `positioning-basics` first.

---

## Mode

Detect from context or ask: *"Quick ideas, full strategy, or complete content system?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | 5 ideas, immediate output, no deep research | Breaking a block, starter brainstorm |
| `standard` | 10–15 positioned ideas with formats and rationale | Regular content planning |
| `deep` | Full content calendar system: pillars, formats, cadence, 30-day plan | Launching or overhauling content strategy |

**Default: `standard`** — use `quick` if they just need to start. Use `deep` if they want a repeatable system, not just today's ideas.

---

## Context Loading Gates

**Before generating any ideas, collect:**

- [ ] **Positioning statement:** "I help [specific audience] with [specific outcome] through [unique approach]." Must be specific — not "I help businesses grow."
- [ ] **ICP specifics:** What are the top 3 frustrations or questions the ideal customer has right now?
- [ ] **Recent wins or proof points:** Any client results, experiments, or lessons from the last 30 days?
- [ ] **Content formats available:** LinkedIn? Twitter/X? Newsletter? Short video? All?
- [ ] **Prior content strategy:** Any existing pillars from `linkedin-authority-builder`? Don't generate outside those pillars if they exist.

**Positioning gate:** If the user cannot complete the positioning sentence with specifics, stop:
> "Content without positioning produces random posts. Complete this first: 'I help [specific audience] achieve [specific outcome] through [unique approach].' If you need help, run `positioning-basics` first."

---

## Phase 1: Context Analysis

Before generating ideas, reason through:

1. **Positioning strength:** Is the one-liner specific enough to anchor content ideas? A vague positioning produces vague ideas.
2. **Proof point audit:** What real results, experiments, or opinions does the user have? Generic ideas come from generic inputs — specific proof points produce specific content.
3. **Platform match:** Different platforms need different idea formats. LinkedIn rewards frameworks and stories; Twitter rewards brevity and contrarian takes; newsletters reward depth and curation.
4. **Content gap:** What has the user NOT covered yet that their ICP is actively asking about?

Output a brief analysis:
> "You're creating content for [audience] as a [role]. Your strongest proof point is [X]. I'll generate ideas anchored to that — the biggest content gap I see is [specific gap]."

---

## Phase 2: Freshness Check (Tool Call)

Run a search before generating the batch:

```
web_search('[Topic] trending [Month Year]')
web_search('[ICP role] biggest challenges [Year]')
```

Use results to:
- Identify timely angles on evergreen topics
- Spot what competitors aren't covering (your opportunity)
- Include at least 1 current-moment hook in the batch

---

## Phase 3: Idea Generation with Quality Filter

Generate ideas using these 6 frameworks:

### 1. The Problem Call-Out
Name the pain your audience won't admit publicly.
**Template:** "The #1 mistake [audience] makes with [topic]"

### 2. The "Here's What Works" Breakdown
Teach a specific process you've actually used.
**Template:** "How to [achieve outcome] without [common obstacle]"

### 3. The Contrarian Take
Challenge something everyone assumes is true.
**Template:** "Stop [common advice]. Here's what actually works."

### 4. The Behind-the-Curtain Story
Show the messy reality, not the highlight reel.
**Template:** "I [tried thing]. Here's what actually happened."

### 5. The Pattern Recognition
Connect dots your audience hasn't connected yet.
**Template:** "What [experience A] taught me about [topic B]"

### 6. The Resource Stack
Curate genuinely useful tools.
**Template:** "[Number] tools I actually use for [outcome]"

---

## Phase 4: Quality Filter (Run Every Idea Through This)

Each idea must pass all 3 tests before being included in the output:

1. **Specific?** — Does it have a concrete angle? ("How to use LinkedIn" → fails. "How to get DMs from framework posts with <500 followers" → passes.)
2. **Has a hook angle?** — Can you write a specific first line that stops the scroll?
3. **Connects to ICP pain?** — Does it address a real, named frustration of the target customer?

Reject and replace any idea that fails 2 or more tests.

---

## Phase 5: Self-Critique Pass (REQUIRED)

After generating the full batch, evaluate:

- [ ] Are all ideas anchored to the stated positioning, or did any drift outside the lane?
- [ ] Does each idea have a specific enough hook that I could write the first line right now?
- [ ] Are the Quick Wins genuinely low-effort to produce, or are they actually complex pieces?
- [ ] Is at least one idea tied to a real proof point or story the user mentioned?
- [ ] Did the freshness search produce anything useful, or were results too generic?

Flag and replace any ideas that don't pass: "Idea 3 ('thoughts on AI in marketing') is too broad for your positioning as a [specific role]. Replaced with: [specific angle]."

---

## Fluff Filter: Do Not Include

❌ "Grateful for the journey" posts — show the work instead
❌ Generic motivational quotes without a specific take
❌ Vague "thought leadership" with no actual opinion
❌ Engagement bait with no value ("Agree? Comment below")
❌ Topics outside the stated positioning

**The test:** Would you stop scrolling and read this if someone else posted it?

---

## Output Structure

```markdown
## Content Ideas: [Name] — [Date]
**Positioning used:** [one-liner]
**Freshness search:** [query + key finding]

---

### Quick Wins (Post This Week)
*5 ideas ready to create now*

**1. [Title/Angle]**
- Hook: "[First line that stops the scroll]"
- Core insight: [The one thing they'll remember]
- Platform fit: [LinkedIn / Twitter / Newsletter]
- ICP pain: [What frustration this addresses]
- Quality check: [Specific ✅ | Hook ✅ | ICP ✅]

[Repeat for ideas 2–5]

---

### Authority Builders (This Month)
*3 ideas worth the investment*

**1. [Title/Angle]**
- Hook: "[First line]"
- Core insight: [Key takeaway]
- Platform fit: [Platform]
- Research needed: [What to find first]
- Estimated production time: [X hours]

[Repeat for ideas 2–3]

---

### Self-Critique Notes
[Any ideas replaced, gaps noted, or freshness findings]

### Multi-Agent Handoff
For each approved idea → pass to Scribe with format:
[Idea title] | [Platform] | [Hook] | [Framework type] | [ICP pain addressed]
```

---

*Skill by Brian Wagner | AI Marketing Architect | brianrwagner.com*
```

## File: `daily-briefing-builder/SKILL-OC.md`
```markdown
---
name: daily-briefing-builder
description: Generate a clean morning brief in Claude Code — pulls today's priorities, unposted content, and weather from your vault.
---

**Platform:** OpenClaw (token-optimized)

## Required Inputs

- `vault_path` — absolute path to Obsidian vault
- `city` — city name for weather (wttr.in format, spaces as `+`)

If either missing, ask before proceeding.

## Workflow

**Step 1 — Today's actions:**
```bash
TODAY=$(date +%Y-%m-%d)
VAULT="VAULT_PATH_HERE"
ACTIONS_FILE="$VAULT/bambf/tracking/daily-actions/${TODAY}.md"
if [ -f "$ACTIONS_FILE" ]; then
  awk '/## Today.s 3 Actions/{found=1; next} found && /^[0-9]/{print} found && /^##/{exit}' "$ACTIONS_FILE"
else
  echo "FILE_MISSING:$ACTIONS_FILE"
fi
```

**Step 2 — Unposted content scan:**
```bash
find "$VAULT/content/ready-to-post" -name "*.md" | while read f; do
  if grep -q '\*\*Posted:\*\* ❌' "$f" 2>/dev/null; then
    echo "UNPOSTED:${f##$VAULT/}"
  fi
done
```

**Step 3 — Weather:**
```bash
curl -s "https://wttr.in/CITY?format=3"
```

## Output Format

```
# 🌅 Morning Brief — [Day], [Date]

## ☀️ Weather
[wttr.in output]

## 🎯 Today's 3 Actions
[From daily actions file, or "No actions file found for today — add to $ACTIONS_FILE"]

## 📝 Ready to Post ([count] items)
[List of unposted content with filenames]

## 🔥 Recommended First Action
[Highest-priority item based on what was found]
```

If no actions file: "No actions file found. Create it at `bambf/tracking/daily-actions/YYYY-MM-DD.md` with your Top 3."

If no unposted content: "No unposted drafts found."

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `daily-briefing-builder/SKILL.md`
```markdown
---
name: daily-briefing-builder
description: Generate a clean morning brief in Claude Code — pulls today's priorities, unposted content, and weather from your vault.
---

# Daily Briefing Builder

Generates a morning brief from your Obsidian vault. Reads today's action file, scans for unposted content, and fetches weather — all inside a Claude Code session.

No APIs. No paid services. No agent autonomy required. You run it, you get your brief.

---

## How to Use

Open Claude Code in your vault directory and say:

```
Run the Daily Briefing Builder skill.
```

Or with context upfront:

```
Run the Daily Briefing Builder skill. My vault is at /path/to/vault and my city is Ann+Arbor.
```

---

## Skill Instructions (for Claude Code)

When this skill is invoked, follow these phases exactly.

---

### PHASE 1: INTAKE

Check whether the user has provided:
- `vault_path` — absolute path to their Obsidian vault
- `city` — city name for weather (wttr.in format, spaces as `+`)

**If either is missing, ask before proceeding:**

```
To run your morning brief, I need two things:
1. Your vault path (e.g. /root/obsidian-vault)
2. Your city for weather (e.g. Ann+Arbor or London)
```

Do not proceed to PHASE 2 until both values are confirmed.

---

### PHASE 2: ANALYZE

Run these shell commands in sequence. Capture all output before formatting.

**Step 1 — Today's actions:**

```bash
TODAY=$(date +%Y-%m-%d)
VAULT="VAULT_PATH_HERE"
ACTIONS_FILE="$VAULT/bambf/tracking/daily-actions/${TODAY}.md"

if [ -f "$ACTIONS_FILE" ]; then
  echo "FILE_FOUND"
  awk '/## Today.s 3 Actions/{found=1; next} found && /^[0-9]/{print} found && /^##/{exit}' "$ACTIONS_FILE"
else
  echo "FILE_MISSING:$ACTIONS_FILE"
fi
```

**Step 2 — Unposted content scan:**

```bash
VAULT="VAULT_PATH_HERE"
READY_DIR="$VAULT/content/ready-to-post"

if [ -d "$READY_DIR" ]; then
  find "$READY_DIR" -name "*.md" -printf "%T@ %p\n" 2>/dev/null \
    | sort -rn | awk '{print $2}' \
    | while read f; do
        if grep -q '\*\*Posted:\*\* ❌' "$f" 2>/dev/null; then
          platform=$(echo "$f" | sed "s|.*/ready-to-post/||" | cut -d'/' -f1)
          title=$(grep -m1 '^[^#\-\*>|` ]' "$f" 2>/dev/null | head -c 100)
          rel="${f##$VAULT/}"
          echo "ITEM|$platform|$rel|$title"
        fi
      done
else
  echo "DIR_MISSING:$READY_DIR"
fi
```

**Step 3 — Weather:**

```bash
curl -s --max-time 5 "wttr.in/CITY_HERE?format=3" || echo "WEATHER_UNAVAILABLE"
```

---

### PHASE 3: OUTPUT

Format and print the brief to the terminal:

```
☀️ Morning Brief — [Weekday, Month Day]

TODAY'S 3 ACTIONS
[numbered actions, or fallback message if file missing]

READY TO POST ([shown] of [total])
[platform] [title] — [relative file path]
...and X more in the pipeline   ← only if total > 5

WEATHER
[wttr.in output or fallback]
```

**Formatting rules:**
- Cap ready-to-post display at **5 items** (newest-modified first)
- If `content/ready-to-post/` doesn't exist: `No ready-to-post folder found`
- If no unposted files: `Content queue is empty`
- If actions file missing: `No actions file for today — create one at bambf/tracking/daily-actions/YYYY-MM-DD.md`
- If weather fails: `Weather unavailable (offline)` — do not abort the brief

---

### PHASE 4: SELF-CRITIQUE

Before delivering, run this internal check. Fix anything that fails — do not deliver until all 4 pass.

1. **Actions accuracy** — Was the actions file found? Did numbered items extract correctly? If the file exists but no items were found, note the potential heading mismatch.
2. **Content completeness** — Count the `ITEM|` lines in Step 2 output. Does the number shown in the brief match? Were any files skipped?
3. **Weather result** — Did curl return valid output? Is the fallback shown if it failed?
4. **Format cleanliness** — No raw bash output. No placeholder text. All three sections present.

---

## Example Output

```
☀️ Morning Brief — Friday, February 28

TODAY'S 3 ACTIONS
1. Finish Q1 content calendar
2. Send invoice to BAMBF client
3. Publish LinkedIn post on AI ops

READY TO POST (5 of 9)
[linkedin] Nobody talks about what happens when your AI system fails... — content/ready-to-post/linkedin/ai-ops-failure.md
[twitter] The overnight ops shift is real. We run Scribe at 2am... — content/ready-to-post/twitter/async-ops.md
[newsletter] AI marketing systems that actually work — content/ready-to-post/newsletter/systems-post.md
[linkedin] Three things I stopped doing after deploying agents — content/ready-to-post/linkedin/stopped-doing.md
[twitter] Founders who ignore async AI ops are about to find out why — content/ready-to-post/twitter/ignore-ops.md
...and 4 more in the pipeline

WEATHER
Ann Arbor: ☀️  +42°F
```

---

## Daily Actions File Format

Expected path: `<vault>/bambf/tracking/daily-actions/YYYY-MM-DD.md`

Expected structure:
```markdown
# Daily Actions — 2026-03-01

## Today's 3 Actions
1. First priority
2. Second priority
3. Third priority
```

If you use a different path or heading, tell Claude Code when invoking the skill.

---

## Requirements

- Claude Code with bash tool access
- Vault with `content/ready-to-post/` folder (files must contain `**Posted:** ❌` to register as unposted)
- `curl` installed (weather fails gracefully without it)
- Daily actions file optional — brief still runs without it
```

## File: `de-ai-ify/README.md`
```markdown
# De-AI-ify Text

**Stop publishing content that screams "AI wrote this."**

Remove AI-generated patterns and restore natural human voice to your writing—systematically, consistently, in 30 seconds.

## The Problem

You use Claude or ChatGPT to draft content. It's fast. But readers can tell.

- **Cliches everywhere:** "In today's fast-paced world," "leverage the power," "unlock potential"
- **Robotic rhythm:** Every sentence the same length. Always three examples. Obsessive parallel structure.
- **Hedging language:** "It's important to note," "arguably," "various stakeholders"
- **Corporate buzzwords:** "Utilize," "facilitate," "optimize"

**Result:** 40% bounce rates. 30-second time on page. Comments like "feels robotic."

## The Solution

**De-AI-ify** - Built from analyzing 1,000+ AI vs human content pieces.

### What You Get

✅ **Systematic pattern removal** - Detects and fixes 47 specific AI markers  
✅ **Human-ness scoring** - 0-10 scale, shows before/after improvement  
✅ **Change tracking** - See exactly what was fixed and why  
✅ **30-second processing** - Faster than manual rewrite, more consistent than "make it human" prompts  
✅ **No API calls needed** - Pure pattern matching, works offline  

### Why This vs Just Asking ChatGPT?

| ChatGPT Prompt | De-AI-ify Skill |
|---|---|
| Inconsistent results | Same transformation logic every time |
| No validation | Scores human-ness 0-10 |
| Different every run | Repeatable, testable process |
| Might change meaning | Preserves your facts and structure |
| Takes 5-10 iterations | One pass, done |

**You could replicate this** by building your own 47-pattern detection system, scoring algorithm, and change tracker. Or use this skill in 30 seconds.

## Real Results

**B2B SaaS marketing team** (8 blog posts):

- Bounce rate: 40% → 18% (-55%)
- Time on page: 30s → 2:14 (+347%)
- Organic shares: 12 → 89
- Processing time: 4 minutes total (vs. 2-3 hours manual)

Input AI score: 3.8/10 → Output human score: 8.4/10

## Quick Start

### Install

```bash
cp -r de-ai-ify $HOME/.openclaw/skills/
```

### Use

```bash
# Process a file
/de-ai-ify blog-post.md

# Outputs:
# - blog-post-HUMAN.md (cleaned version)
# - Change log showing what was fixed
# - Before/after scores
```

### Example Output

```
ORIGINAL SCORE: 4.2/10 (AI-heavy)
REVISED SCORE: 8.6/10 (Human-like)

CHANGES MADE:
✓ Removed 7 hedging phrases
✓ Replaced 4 corporate buzzwords  
✓ Fixed 3 robotic patterns
✓ Added 5 specific examples
✓ Shortened 8 run-on sentences

FILE SAVED: blog-post-HUMAN.md
```

## Before & After Examples

### Marketing Copy

**Before (AI score 3.2/10):**
> "In today's competitive marketplace, leveraging data-driven insights is crucial for optimizing customer engagement. Organizations that harness analytics are seeing unprecedented results."

**After (Human score 8.7/10):**
> "Companies using customer data see 23% higher revenue (McKinsey). Spotify's algorithm keeps users 40% longer. Netflix saves $1B/year. Data works when you act on it."

### Technical Writing

**Before (AI score 4.1/10):**
> "The implementation of machine learning models facilitates optimization of complex decision-making processes across various use cases."

**After (Human score 8.3/10):**
> "Machine learning helps computers learn from examples. Feed it 1,000 images, it learns to recognize cats. Show it 10,000 sales calls, it predicts which deals close."

## What Gets Fixed

**47 AI patterns detected:**

- **Cliches** - "unlock potential," "game-changer," "paradigm shift"
- **Hedging** - "arguably," "potentially," "it's worth noting"
- **Buzzwords** - "leverage" → "use," "utilize" → "use"
- **Robotic rhythm** - Parallel structure overuse, always 3 examples
- **Vague language** - "various," "numerous" → specific names/numbers

**Replaced with:**

- Specific examples (companies, numbers, studies)
- Varied sentence rhythm (mix short and long)
- Conversational connectors ("But here's the thing")
- Direct statements (no hedging unless genuinely uncertain)
- Active voice and contractions

## Who This Is For

✅ **Marketing teams** publishing AI-assisted content  
✅ **Content creators** using Claude/ChatGPT for drafts  
✅ **B2B companies** fighting AI-sounding blog posts  
✅ **Anyone** who wants AI speed with human voice  

## Features

- **Multiple modes:** Strict (marketing), Preserve (business docs), Academic (research)
- **Fast processing:** 5,000 words/second
- **No dependencies:** Pure pattern matching, works offline
- **Change logs:** See exactly what was fixed
- **Scoring system:** Flesch readability + AI pattern detection
- **92% accuracy:** Agreement with human editors (n=200 docs)

## Installation & Usage

```bash
# Install
cp -r de-ai-ify $HOME/.openclaw/skills/

# Basic usage
/de-ai-ify document.md

# Preserve formal tone (business docs)
/de-ai-ify whitepaper.md --preserve-formal

# Academic mode (research papers)
/de-ai-ify paper.md --academic

# Custom score threshold
/de-ai-ify post.md --score-threshold 9
```

## Limitations

**This skill does NOT:**
- Fix factual errors (separate fact-check needed)
- Improve weak arguments (structure unchanged)
- Generate new examples (flags for manual addition)
- Change your intended meaning

**Best for:** Content that's already solid but sounds too AI.

## Pro Tips

1. **Run twice on heavy AI content** - First pass catches obvious, second refines
2. **Combine with human editor** - Use for first pass, human for final polish
3. **Track scores over time** - Aim for consistent 8+ on public content
4. **Use preserve mode for B2B** - Some formality expected in enterprise
5. **Read aloud test** - If it sounds natural spoken, it'll read natural

## License

MIT License - Use freely, commercially or personally.

## Contributing

Found a new AI pattern? Submit via GitHub issues with examples.

Built by **theflohart** from analyzing 1,000+ AI vs human content pieces.

---

**Stop sounding like a chatbot. Start sounding human.**

**Process 5,000 words in 30 seconds. Score 8+/10 consistently.**
```

## File: `de-ai-ify/SKILL-OC.md`
```markdown
---
name: de-ai-ify
description: Remove AI-generated jargon and restore human voice to text. Built from analyzing 1,000+ AI vs human content pieces.
version: 2.0.0
author: theflohart
tags: [writing, editing, voice, ai-detection, content-quality]
---

**Platform:** OpenClaw (token-optimized)

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | Remove obvious AI patterns, single pass | Fast social copy |
| `standard` | Full 47-pattern scan + human score (0–10) + change log | Default — any public content |
| `deep` | Full scan + voice calibration against writer's actual samples | Ghostwriting, brand-voice-matched content |

## Pattern Categories to Remove

**Overused transitions (remove/vary):**
Moreover, Furthermore, Additionally, Nevertheless, excessive "However" (>2/500 words), "While X, Y" openers (>3/page), "In conclusion," "To summarize"

**AI clichés (replace with specifics):**
"In today's fast-paced world," "Let's dive deep," "Unlock your potential," "Harness the power of," "It's no secret that," "The key takeaway is," "At the end of the day," "Game-changer," "Paradigm shift," "Delve," "Revolutionize," "Transformative"

**Hedging language (cut):**
"It's important to note," "It's worth mentioning," "One might argue," "As you might expect," "Needless to say"

**Sentence structure patterns (rewrite):**
- Every paragraph same length → vary
- Every sentence same structure → mix short + long
- Passive voice dominance → active
- Triple-adjective openers → cut to one

## Scoring Rubric (0–10)

| Score | Meaning |
|-------|---------|
| 0–3 | Clearly AI — obvious patterns throughout |
| 4–6 | Detectable — some patterns remain |
| 7–8 | Human-ish — minor polish needed |
| 9–10 | Genuinely human — distinct voice present |

Target: ≥8. If final score <7, run another pass.

## Workflow

1. Run pattern scan — flag every instance by category
2. Calculate pre-edit score
3. Apply rewrites — preserve facts, structure, key points
4. Calculate post-edit score
5. Produce change log: what changed + why
6. If deep mode: compare against voice sample, adjust tone to match

## Output Format

```
## De-AI-ify Results

**Pre-edit score:** X/10
**Post-edit score:** X/10
**Patterns removed:** [count by category]

### Cleaned Text
[Full rewritten content]

### Change Log
- [Original phrase] → [Replacement] (reason)
```

---
*Skill by theflohart | AI Marketing Skills*
```

## File: `de-ai-ify/SKILL.md`
```markdown
---
name: de-ai-ify
description: Remove AI-generated jargon and restore human voice to text. Built from analyzing 1,000+ AI vs human content pieces.
version: 2.0.0
author: theflohart
tags: [writing, editing, voice, ai-detection, content-quality]
---

# De-AI-ify Text

Remove AI-generated patterns and restore natural human voice to your writing.

## Why This vs ChatGPT?

**Problem with raw ChatGPT:** Just asking "make this sound more human" gives inconsistent results. You get different rewrites each time, no systematic pattern removal, and no validation.

**This skill provides:**
1. **Systematic detection** - Trained on 1,000+ AI vs human comparisons to identify 47 specific patterns
2. **Consistent methodology** - Same transformation logic every time, not random rewrites
3. **Validation scoring** - Measures "human-ness" on 0-10 scale using readability metrics
4. **Change tracking** - Shows exactly what was fixed and why
5. **Preservation mode** - Keeps your facts, structure, and key points while fixing the voice

**You can replicate this with ChatGPT if you:** Include all 47 patterns, build a scoring system, track changes manually, and spend 15 minutes per doc. This skill does it in 30 seconds.

## Mode

Detect from context or ask: *"Quick pass, full cleanup, or match a specific voice?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | Remove obvious AI patterns, single pass, no scoring | Blog posts, quick social copy |
| `standard` | Full 47-pattern scan + human score (0–10) + change log | Any content going public |
| `deep` | Full scan + voice calibration against a sample of the writer's actual work | Ghostwriting, brand voice-matched content |

**Default: `standard`** — use `quick` for fast edits. Use `deep` when you have a voice reference sample and need the output to sound like a specific person.

---

## Usage

```
/de-ai-ify <file_path>
```

Or with mode flag:

```
/de-ai-ify <file_path> --mode quick|standard|deep
```

Or with custom scoring:

```
/de-ai-ify <file_path> --score-threshold 8
```

## What Gets Removed

### 1. Overused Transitions (14 patterns)

- "Moreover," "Furthermore," "Additionally," "Nevertheless"
- Excessive "However" usage (>2 per 500 words)
- "While X, Y" sentence openings (>3 per page)
- "In conclusion" / "To summarize" throat-clearing

### 2. AI Cliches (18 patterns)

- "In today's fast-paced world"
- "Let's dive deep" / "Let's explore"
- "Unlock your potential" / "Unleash"
- "Harness the power of"
- "It's no secret that"
- "The key takeaway is"
- "At the end of the day"
- "Game-changer" / "Paradigm shift"

### 3. Hedging Language (8 patterns)

- "It's important to note"
- "It's worth mentioning"
- "One might argue"
- Vague quantifiers: "various," "numerous," "myriad," "plethora"
- "Arguably" / "Potentially" overuse

### 4. Corporate Buzzwords (12 patterns)

- "utilize" → "use"
- "facilitate" → "help"
- "optimize" → "improve"
- "leverage" → "use"
- "synergize" → "work together"
- "ideate" → "brainstorm"
- "circle back" → "follow up"
- "move the needle" → "improve results"

### 5. Robotic Patterns (9 patterns)

- Rhetorical questions followed immediately by answers
- Obsessive parallel structures (3+ consecutive sentences starting the same way)
- Always using exactly three bullet points or examples
- Announcement of emphasis: "Importantly," "Crucially," "Significantly"
- List prefacing: "Here are the top X ways..."

## What Gets Added

### Natural Voice Markers

- **Varied sentence rhythm** - Mix short (5-10 word) and long (20-30 word) sentences
- **Conversational connectors** - "So," "But here's the thing," "And yet"
- **Direct statements** - Replace "It could be argued that X is Y" with "X is Y"
- **Specific examples** - Replace "many companies" with "Salesforce, HubSpot, and Gong"

### Human Rhythm Signals

- **Contractions** - "It's" not "It is" in casual content
- **Active voice** - "We tested" not "Testing was conducted"
- **Confident assertions** - Remove hedging unless genuinely uncertain
- **Personal perspective** - "I've seen" / "In my experience" where appropriate

## Process

1. **Read original file** (supports .md, .txt, .docx)
2. **Score original** (0-10 human-ness scale)
3. **Apply pattern removal** (47 detections)
4. **Enhance human markers** (sentence rhythm, specificity)
5. **Score revised version**
6. **Create "-HUMAN.md" file**
7. **Generate change log**

## Output Structure

You'll receive:

```
ORIGINAL SCORE: 4.2/10 (AI-heavy)
REVISED SCORE: 8.6/10 (Human-like)

CHANGES MADE:
✓ Removed 7 hedging phrases ("It's important to note", "arguably")
✓ Replaced 4 corporate buzzwords ("leverage" → "use")
✓ Fixed 3 robotic patterns (parallel structure overuse)
✓ Added 5 specific examples (replaced vague references)
✓ Shortened 8 sentences (>40 words → 15-25 words)

FLAGS FOR MANUAL REVIEW:
⚠ Paragraph 3: Still uses "various" - suggest specific companies
⚠ Paragraph 7: Transition feels abrupt - consider adding context

FILE SAVED: example-HUMAN.md
```

## Scoring System

**Human-ness scale (0-10):**

- **0-3:** Obviously AI-generated (multiple cliches, robotic structure)
- **4-5:** AI-heavy (some human touches but needs major work)
- **6-7:** Mixed (could be human or AI, lacks strong voice)
- **8-9:** Human-like (natural voice, minimal AI patterns)
- **10:** Indistinguishable from skilled human writer

**Scoring factors:**
- Flesch Reading Ease (40-60 = ideal)
- Sentence length variance (coefficient of variation >0.3)
- AI pattern count per 1000 words (<5 = good)
- Specificity ratio (specific terms / vague terms >2:1)

## Real Case Study

**Client:** B2B SaaS marketing team writing blog posts with Claude

**Problem:** Posts were getting 40% bounce rate, 30-second avg time on page. Readers commented "feels robotic."

**Input sample (428 words, AI score 3.8/10):**
> "In today's rapidly evolving digital landscape, it's crucial to understand that leveraging AI effectively isn't just about utilizing cutting-edge technology—it's about harnessing its transformative potential. Moreover, organizations that successfully implement AI solutions are seeing unprecedented results. Furthermore, it's important to note that the key to success lies in strategic optimization."

**After de-ai-ify (391 words, score 8.4/10):**
> "AI works best when you use it for specific tasks. Salesforce cut support tickets by 30% with Einstein AI. HubSpot's content assistant writes first drafts in 2 minutes. Gong analyzes 1 million sales calls per month. The pattern? They picked ONE job for AI and nailed it."

**Results:**
- Bounce rate: 40% → 18% (-55%)
- Avg time on page: 30s → 2:14 (+347%)
- Comments: "Finally, straight talk about AI"
- Organic shares: 12 → 89 posts

**Time investment:** 8 blog posts processed in 4 minutes (vs. 2-3 hours manual rewrite)

## Examples

### Example 1: Marketing Copy

**Before:**
> "It's no secret that in today's competitive marketplace, leveraging data-driven insights is crucial for optimizing customer engagement. Furthermore, organizations that harness the power of analytics are seeing unprecedented results across various channels."

**After:**
> "Companies using customer data see 23% higher revenue (McKinsey, 2023). Spotify's algorithm keeps users 40% longer. Netflix saves $1B/year in retention. Data works when you act on it."

**Changes:** Removed 3 cliches, 2 hedges, 1 buzzword. Added 4 specific examples.

### Example 2: Technical Explanation

**Before:**
> "The implementation of machine learning models facilitates the optimization of complex decision-making processes. Moreover, it's important to note that various algorithms can be utilized to enhance predictive accuracy across numerous use cases."

**After:**
> "Machine learning helps computers learn from examples. Feed it 1,000 labeled images, it learns to recognize cats. Show it 10,000 sales calls, it predicts which deals will close. The algorithm improves with more data."

**Changes:** Replaced 4 buzzwords, removed hedging, added concrete examples, simplified structure.

### Example 3: Thought Leadership

**Before:**
> "As we navigate the complexities of the modern workplace, it's crucial to recognize that employee engagement is not merely a nice-to-have—it's a strategic imperative. Furthermore, organizations that prioritize engagement initiatives are experiencing transformative results."

**After:**
> "Disengaged employees cost $450-550B annually (Gallup). But here's the thing: 85% of engagement programs fail because they're top-down. The companies that win? They ask employees what actually matters, then fix those 3 things. Simple."

**Changes:** Replaced vague statement with data, added contrarian insight, specific example, conversational tone.

## Configuration Options

### Strict Mode (default)
```
/de-ai-ify document.md
```
- Removes all 47 patterns
- Target score: 8+/10
- Best for: Marketing copy, blog posts, social content

### Preserve Mode
```
/de-ai-ify document.md --preserve-formal
```
- Keeps some formal language
- Removes obvious cliches only
- Target score: 7+/10
- Best for: White papers, case studies, business docs

### Academic Mode
```
/de-ai-ify document.md --academic
```
- Preserves "Moreover," "Furthermore" (field standard)
- Focuses on voice and clarity
- Target score: 6.5+/10
- Best for: Research papers, technical docs

## Installation

```bash
# Copy skill to your skills directory
cp -r de-ai-ify $HOME/.openclaw/skills/

# Verify installation
/de-ai-ify --version
```

**No dependencies required** - Pure pattern matching and text analysis.

## Technical Details

**How it works:**
1. Tokenizes text into sentences and phrases
2. Runs 47 regex patterns for AI markers
3. Calculates readability scores (Flesch, Fog Index)
4. Applies transformations with context awareness
5. Scores before/after, generates change log

**Processing speed:** ~5,000 words/second on standard hardware

**Accuracy:** 92% agreement with human editors in blind tests (n=200 documents)

## Limitations

**This skill does NOT:**
- Fix factual errors (use fact-checking separately)
- Improve weak arguments (structure remains unchanged)
- Replace bad examples with good ones (flags for manual review)
- Change meaning or tone intentionally (preserves your intent)

**Best used for:** Content that's already solid but sounds too AI-ish.

## Quality Checklist

After de-ai-ification, verify:
- [ ] Reads naturally when spoken aloud
- [ ] Specific examples replace vague references
- [ ] Sentence rhythm varies (not all same length)
- [ ] No obvious AI cliches remain
- [ ] Facts and data are still accurate
- [ ] Your key points are preserved
- [ ] Score is 8+/10 for public content

## Pro Tips

1. **Run twice for heavy AI content** - First pass catches obvious patterns, second pass refines
2. **Combine with human review** - Use for first pass, human editor for final polish
3. **Build a custom pattern list** - Add industry-specific buzzwords to detection
4. **Track your scores** - Monitor improvement over time, aim for consistent 8+
5. **Use preserve mode for B2B** - Some formality is expected in enterprise content

## Support

Issues or suggestions? Open a ticket with:
- Original file (first 500 words)
- Score received
- Expected behavior
- What you'd like improved

---

**Built by analyzing 1,000+ AI vs human content samples across marketing, technical, and creative writing.**

**Makes AI-generated content sound human again—systematically.**
```

## File: `de-ai-ify/_meta.json`
```json
{
  "owner": "itsflow",
  "slug": "de-ai-ify",
  "displayName": "De-AI-ify",
  "latest": {
    "version": "1.0.0",
    "publishedAt": 1769256718767,
    "commit": "https://github.com/clawdbot/skills/commit/702efaa764b3e3a5b571795fdd4c86e65a070fe2"
  },
  "history": []
}
```

## File: `go-mode/README.md`
```markdown
# 🎯 Go Mode — Autonomous Goal Execution for OpenClaw

**Give your agent a goal. It plans, confirms, executes, and reports — you just approve.**

## What You Get

- **SKILL.md** — Complete autonomous execution framework with 4-phase workflow
- **Guardrail system** — Built-in safety rails so the agent never goes rogue
- **Tool reference** — Maps goals to the right skills, APIs, and tools
- **6 example goals** — Ready-to-use templates for marketing and business

## How It Works

```
You: "Research our competitors and build a comparison page"
Agent: Here's my plan (5 steps, ~50min, ~$0.50)... approve?
You: Go
Agent: [executes autonomously, checkpoints after each step]
Agent: Done! Here's what I built, what I learned, and what's next.
```

## Features

✅ **4-Phase Workflow** — Plan → Confirm → Execute → Report  
✅ **Built-in Guardrails** — Asks before emails, posts, purchases, deletions  
✅ **Budget Caps** — Default $5/goal, customizable  
✅ **Checkpoint System** — Status updates after every major step  
✅ **Adaptive Execution** — Tries alternatives before escalating failures  
✅ **Full Transparency** — Reports everything done with stats  

## Example Goals

- "Research top 3 competitors and build a comparison page"
- "Turn my blog post into a week of social content"
- "Find 20 potential SaaS clients for outreach"
- "Create 3 SEO blog posts for our target keywords"
- "Prepare everything for next Tuesday's product launch"
- "Review this week and plan next week's priorities"

## Requirements

- OpenClaw agent (any model)
- Works better with more skills installed (references 15+ common skills)

## Price: $9

One skill to rule them all. Stop micromanaging your agent — let it drive.
```

## File: `go-mode/SKILL-OC.md`
```markdown
---
name: go-mode
description: Autonomous goal execution — give a goal, get a plan, confirm, execute, report. You steer, Claude drives.
version: 2.0.0
author: BrianRWagner
tags: [autonomy, planning, execution, goal-setting, productivity]
---

**Platform:** OpenClaw (token-optimized)

## Flow

```
GOAL → PLAN → CONFIRM → EXECUTE → REPORT
```

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | 1-line plan → confirm → execute | Simple, clear goals |
| `standard` | Full plan → confirm → execute → report | Default |
| `deep` | Full plan → risk review → confirm each phase → execute → report | High-stakes / irreversible |

## Phase 1: PLAN

Parse goal → break into ordered steps → identify tools → estimate effort → flag risks.

```
## 🎯 Goal: [restated]

### Definition of Done
[What success looks like]

### Plan
| # | Step | Tool/Skill | Est. Time | Cost | Risk |
|---|------|-----------|-----------|------|------|

### Total: Time X min | Cost ~$X | Checkpoints: [list]

### Guardrails Triggered
- [ ] External communication (needs approval)
- [ ] Financial spend > $1
- [ ] Irreversible action
```

## Phase 2: CONFIRM

Wait for user response:
- **"Go"** → execute all steps
- **"Go with changes"** → adjust, then execute
- **"Just steps 1-3"** → partial execution
- **"Cancel"** → abort

**Never skip confirmation.**

## Phase 3: EXECUTE

For each step:
1. Announce: "Step 2/5: [action]..."
2. Run it
3. Report result: ✅ Done / ❌ Failed + what to do next

**On failure:** Stop, report what failed and why, ask how to proceed. Do not skip steps silently.

## Phase 4: REPORT

```
## ✅ Goal Complete: [Goal]

### What Was Done
| Step | Result | Time |
|------|--------|------|

### Output Files / Links
[Any created files or resources]

### What to Do Next (optional)
[If follow-up actions are obvious]
```

## Guardrails (always active)

- External sends (email, tweet, API POST) → always confirm before executing
- File deletion → always confirm
- Spend > $1 → always flag before executing
- Ambiguous goal → ask one clarifying question before planning

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `go-mode/SKILL.md`
```markdown
---
name: go-mode
description: Autonomous goal execution — give a goal, get a plan, confirm, execute, report. You steer, Claude drives.
version: 2.0.0
author: BrianRWagner
tags: [autonomy, planning, execution, goal-setting, productivity]
homepage: https://github.com/BrianRWagner/ai-marketing-claude-code-skills
---

# 🎯 Go Mode — Autonomous Goal Execution

Give me a goal. I'll plan it, confirm with you, execute it, and report back. You steer — I drive.

## Mode

Detect from context or ask: *"Just do it, plan first, or plan + phase approvals?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | 1-line plan → you confirm → execute | Simple tasks, clear goals |
| `standard` | Full plan → you confirm → execute → report (default) | Most tasks |
| `deep` | Full plan → risk review → confirm each phase → execute → report | High-stakes or multi-system tasks |

**Default: `standard`** — use `quick` for simple, clear goals. Use `deep` when mistakes would be expensive to undo.

---

## How It Works

```
GOAL → PLAN → CONFIRM → EXECUTE → REPORT
```

### Phase 1: PLAN
When given a goal, break it down:

1. **Parse the goal** — What's the desired outcome? What does "done" look like?
2. **Break into steps** — Ordered task list, each step concrete and actionable
3. **Identify tools** — Which skills, APIs, agents, or CLI tools are needed?
4. **Estimate effort** — Time per step, total duration, API costs if applicable
5. **Flag risks** — What could go wrong? What needs human approval?

Output a structured plan:

```
## 🎯 Goal: [restated goal]

### Definition of Done
[What success looks like]

### Plan
| # | Step | Tool/Skill | Est. Time | Cost | Risk |
|---|------|-----------|-----------|------|------|
| 1 | ... | ... | ... | ... | ... |

### Total Estimate
- **Time:** X minutes
- **API Cost:** ~$X.XX
- **Human Checkpoints:** [list]

### Guardrails Triggered
- [ ] External communication (needs approval)
- [ ] Financial spend > $1
- [ ] Irreversible action
```

### Phase 2: CONFIRM
Present the plan and wait for approval:

- **"Go"** → Execute all steps
- **"Go with changes"** → Adjust plan, then execute
- **"Just steps 1-3"** → Partial execution
- **"Cancel"** → Abort

**Never skip confirmation.** This is the human's steering wheel.

### Phase 3: EXECUTE
Run each step sequentially:

1. **Announce** the current step: "Step 2/5: Researching competitor pricing..."
2. **Execute** using the identified tool/skill
3. **Checkpoint** after each major step — brief status update
4. **Pause if:** 
   - A guardrail is triggered (external action, spend, irreversible)
   - Something unexpected happens
   - A decision point requires human judgment
5. **Adapt** — If a step fails, try alternatives before escalating

### Phase 4: REPORT
When all steps complete:

```
## ✅ Goal Complete: [goal]

### What Was Done
- Step 1: [result]
- Step 2: [result]
- ...

### Outputs
- [List of files, links, artifacts created]

### What Was Learned
- [Insights discovered during execution]

### Recommended Next Steps
- [What to do with the results]
- [Follow-up opportunities]

### Stats
- Total time: Xm
- API calls: X
- Est. cost: $X.XX
```

## Guardrails

### Always Ask Before:
- ✉️ Sending emails, DMs, or messages to anyone
- 📢 Posting to social media (Twitter, LinkedIn, etc.)
- 💰 Spending money or making API calls > $1 estimated
- 🗑️ Deleting files or data
- 🔒 Changing permissions, credentials, or configs
- 🌐 Making any public-facing change

### Auto-Proceed On:
- ✅ Reading files, searching the web
- ✅ Creating drafts (not publishing)
- ✅ Organizing or summarizing information
- ✅ Running analysis or calculations
- ✅ Creating files in the workspace

### Budget Caps
- **Default per-goal budget:** $5 API spend max
- **Per-step timeout:** 5 minutes (escalate if stuck)
- **Total goal timeout:** 60 minutes (checkpoint and ask to continue)
- Human can override any cap at confirm time

## Available Tools & Skills Reference

When planning, draw from this toolkit:

### Research & Information
| Tool | Use For |
|------|---------|
| `web_search` | Quick web lookups |
| `web_fetch` | Read full web pages |
| `qmd search` | Search Obsidian vault knowledge base |
| `content-research-writer` skill | Deep research + writing |
| `research-coordinator` skill | Multi-source research |

### Content Creation
| Tool | Use For |
|------|---------|
| `content-atomizer` skill | Turn 1 piece → 13+ posts |
| `direct-response-copy` skill | Sales copy |
| `seo-content` skill | SEO articles |
| `newsletter` skill | Newsletter editions |
| `email-sequences` skill | Email flows |
| `nano-banana` skill | Image generation (Gemini) |

### Marketing & Strategy
| Tool | Use For |
|------|---------|
| `positioning-angles` skill | Find hooks that sell |
| `keyword-research` skill | SEO keyword strategy |
| `business-prospecting` skill | Lead research |
| `landing-page-design` skill | Landing pages |
| `page-cro` skill | Conversion optimization |

### Communication
| Tool | Use For |
|------|---------|
| `bird` CLI | Twitter/X (read, post, reply) |
| Gmail | Email (read, send) |
| Notion | Pages and databases |
| Telegram | Messaging |

### Development
| Tool | Use For |
|------|---------|
| `exec` | Shell commands |
| `codex` | Code generation (GPT) |
| `claude` | Code generation (Claude) |
| File tools | Read, write, edit files |

## Example Goals

### 1. Competitor Analysis → Comparison Page
```
Goal: "Research our top 3 competitors in the AI assistant space and build a comparison page"

Plan:
1. Identify top 3 competitors (web search) — 5min
2. Research each: pricing, features, reviews — 15min
3. Build comparison matrix — 10min
4. Write comparison page copy — 15min
5. Create visual comparison table — 5min
Total: ~50min, ~$0.50 API cost
```

### 2. Content Repurposing Pipeline
```
Goal: "Take my latest blog post and turn it into a week of social content"

Plan:
1. Read and analyze the blog post — 2min
2. Extract key themes and quotes — 5min
3. Generate 5 Twitter threads — 15min
4. Generate 5 LinkedIn posts — 15min
5. Create 3 image prompts + generate visuals — 10min
6. Build content calendar — 5min
Total: ~52min, ~$1.00 API cost
```

### 3. Lead Research Sprint
```
Goal: "Find 20 potential clients in the SaaS space who might need our marketing services"

Plan:
1. Define ideal client profile — 5min
2. Search for SaaS companies (web) — 15min
3. Research each company's marketing gaps — 20min
4. Score and rank prospects — 10min
5. Build outreach-ready prospect list — 10min
6. Draft personalized intro messages [NEEDS APPROVAL] — 15min
Total: ~75min, ~$0.75 API cost
```

### 4. SEO Content Sprint
```
Goal: "Create 3 SEO-optimized blog posts for our target keywords"

Plan:
1. Review target keyword list — 2min
2. Research top-ranking content for each keyword — 15min
3. Create outlines using SEO skill — 10min
4. Write article 1 — 15min
5. Write article 2 — 15min
6. Write article 3 — 15min
7. Add internal links and meta descriptions — 10min
Total: ~82min, ~$2.00 API cost
```

### 5. Launch Prep Checklist
```
Goal: "Prepare everything needed to launch our new product next Tuesday"

Plan:
1. Audit what exists (landing page, emails, social) — 10min
2. Identify gaps — 5min
3. Write launch email sequence (3 emails) — 20min
4. Create social media posts (Twitter, LinkedIn) — 15min
5. Generate launch graphics — 10min
6. Build launch day timeline — 5min
7. Draft press/outreach messages [NEEDS APPROVAL] — 15min
Total: ~80min, ~$2.50 API cost
```

### 6. Weekly Review & Planning
```
Goal: "Review this week's metrics, summarize wins/losses, and plan next week's priorities"

Plan:
1. Pull metrics from available sources — 10min
2. Summarize key wins — 5min
3. Identify what didn't work — 5min
4. Review upcoming calendar — 5min
5. Propose next week's top 3 priorities — 10min
6. Create actionable task list — 5min
Total: ~40min, ~$0.25 API cost
```

## Usage

Just tell the agent your goal in natural language:

> "Take the wheel: Research the top 5 AI newsletter tools, compare them, and recommend the best one for a solopreneur"

> "Take the wheel: Build a complete email welcome sequence for new subscribers — 5 emails over 2 weeks"

> "Take the wheel: Audit our Twitter presence and create a 30-day content strategy"

The agent will plan, confirm, execute, and report. You stay in control at every checkpoint.

## Principles

1. **Transparency** — Always show the plan before executing
2. **Safety** — Never take external actions without approval
3. **Efficiency** — Use the cheapest/fastest tool for each step
4. **Resilience** — Try alternatives before giving up
5. **Accountability** — Report everything that was done
6. **Respect time** — Estimate honestly, checkpoint if running long
```

## File: `homepage-audit/SKILL-OC.md`
```markdown
---
name: homepage-audit
description: Audit a homepage for conversion, clarity, and positioning. Use when someone says "audit my homepage," "why isn't my site converting," "review my landing page," or shares a URL for feedback.
---

**Platform:** OpenClaw (token-optimized)

## Required Inputs

- Homepage URL (or pasted copy)
- ICP (specific role/situation)
- Primary conversion goal (sign up / book call / buy / contact)
- Top 3 competitors (for positioning comparison)

**If URL provided:** `web_fetch(URL)` to extract content before auditing.

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | Headline + CTA audit, top 3 fixes | Pre-meeting fast check |
| `standard` | Full 6-section scored audit + priority roadmap | Default |
| `deep` | Full audit + rewrite-level copy fixes + A/B test recommendations | Full CRO overhaul |

## 6 Audit Sections (score each 1–10)

**1. Headline & Subheadline**
- Does it pass the 5-second test? (Can a stranger state what you do in 5 sec?)
- ICP-specific language vs. generic?
- Outcome-first or feature-first?

**2. Value Proposition**
- Is there a clear "only we" claim?
- Would a competitor say the exact same thing?
- Is it specific or generic?

**3. Social Proof**
- Named companies, logos, or testimonials above the fold?
- Do testimonials have specific outcomes (numbers, named results)?
- Quantity + quality of proof signals

**4. CTA**
- Single primary CTA or competing CTAs?
- Action-specific ("Start free trial") vs. vague ("Learn more")?
- Friction level (form fields, steps required)

**5. Clarity & Friction**
- Navigation competing with the CTA?
- Mobile readability?
- Page load / visual clutter?

**6. Positioning Differentiation**
- Could this homepage belong to a competitor?
- Does the messaging own a specific category/claim?
- ICP would feel "this is for me" — yes or no?

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 1–3 | Actively hurting conversions |
| 4–6 | Neutral — present but forgettable |
| 7–8 | Functional — minor sharpening needed |
| 9–10 | Exceptional (rare — reserve for truly remarkable copy) |

## Output Format

```
## Homepage Audit: [Domain] — [Date]

### Section Scores
| Section | Score /10 | Key Issue |
|---------|-----------|-----------|

### Total: X/60

### Priority Fixes (in order of leverage)
1. [Section] — [Specific fix, not "improve your headline"]
2. ...

### Quick Wins (do this week)
[1-2 highest-impact, lowest-effort changes]

### Rewrite Recommendations
[If deep mode: actual copy rewrites for headline, subheadline, CTA]
```

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `homepage-audit/SKILL.md`
```markdown
---
name: homepage-audit
description: Full conversion audit for any homepage or landing page. Use when someone asks to "review my homepage," "audit my landing page," "why isn't my page converting," "check my website," or wants feedback on their marketing page. Requires URL or screenshot before proceeding.
---

# Homepage Audit

You are a conversion expert. Your goal: audit a homepage or landing page with systematic scoring, then produce an impact-prioritized action plan with concrete rewrites.

---

## Mode

Detect from context or ask: *"Quick scan, full audit, or full audit with rewrites?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | 5-second test + top 3 highest-impact fixes | Fast gut-check before a launch |
| `standard` | Full section-by-section audit + priority list | Website refresh, conversion diagnosis |
| `deep` | Full audit + rewrite recommendations for each section + A/B test hypotheses | Full redesign or CRO project |

**Default: `standard`** — use `quick` if they say "just tell me what's wrong." Use `deep` if they want copy rewrites alongside the diagnosis.

---

## Context Loading Gates

**Do not begin the audit without one of these:**
- A live URL (fetch with `web_fetch` if available)
- A screenshot of above-the-fold content
- Copy/paste of: headline, subheadline, primary CTA, and first paragraph

**If none is provided:** Ask exactly once:
> "To audit your homepage accurately, I'll need either the URL, a screenshot, or the above-the-fold copy pasted here. Which can you share?"

**Also ask (if not obvious from the page):**
- What type of business is this? (SaaS / service / e-commerce)
- Who is the target customer?
- What's the primary conversion goal? (trial sign-up / book a call / purchase)

Do not proceed with assumptions. A misidentified page type will produce wrong scoring weights.

---

## Phase 1: Page-Type Classification & Scoring Weight Assignment

After loading the page, classify it. Scoring weights differ by type:

### SaaS / Software
- Headline must explain the **outcome**, not the feature
- Social proof priority: trial numbers, G2 ratings, logos
- CTA priority: Free trial > Demo > Learn More
- Watch for: Jargon, feature-led headlines, weak differentiation

### Service Business (Agency, Consulting, Freelance)
- Headline must establish credibility AND outcome
- Social proof priority: Named testimonials with results, case study links
- CTA priority: Book a call > Get a quote
- Watch for: Vague positioning ("we help businesses grow")

### E-Commerce
- Hero must show product + benefit immediately
- Social proof priority: Star ratings, reviews, UGC
- CTA priority: Shop now > View collection
- Watch for: Too many options causing decision paralysis

---

## Phase 2: Structured Scoring (Complete Before Recommendations)

Score each element 1–5 using these criteria. Do not skip sections.

### Section 1: Above the Fold (Weight: 25%)

| Element | Score 1 | Score 3 | Score 5 |
|---|---|---|---|
| **Headline** | Company name or vague | Functional but feature-led | Specific outcome for specific person |
| **Subheadline** | Missing | Restates headline | Adds who + how |
| **Primary CTA** | Missing or "Submit" | Visible but generic | Specific, above fold, action-oriented |
| **Visual** | Stock photo | Product shown | Product-in-context showing outcome |
| **Load Speed** | >4s | 2–4s | <2s |
| **Mobile Render** | Broken | Functional | Perfect |

**Headline scoring rubric:**
- Score 1: "Welcome to [Company Name]"
- Score 3: "[Feature]-powered [category]"
- Score 5: "[Specific outcome] for [specific person]—without [specific obstacle]"

### Section 2: Value Proposition (Weight: 25%)
Score each: Benefits clarity / Target customer specificity / Differentiation / Features-to-benefits translation

### Section 3: Social Proof (Weight: 10%)
Score each: Testimonial quality / Logo presence / Hard numbers/stats

### Section 4: Clarity & Copy (Weight: 15%)
Score each: Scannability / Conciseness / Jargon-free / Benefits > Features ratio

### Section 5: CTA & Conversion (Weight: 15%)
Score each: CTA visibility / CTA frequency / Low-friction option availability

### Section 6: Trust & Risk Reduction (Weight: 10%)
Score each: Pricing transparency / Risk reversal / Objection handling

**Calculate weighted total:**
`(Section 1 avg × 0.25) + (Section 2 avg × 0.25) + (Section 3 avg × 0.10) + (Section 4 avg × 0.15) + (Section 5 avg × 0.15) + (Section 6 avg × 0.10) = X/5`

**Interpretation:**
- 4.5–5.0: Excellent
- 3.5–4.4: Good
- 2.5–3.4: Needs Work
- Below 2.5: Major Overhaul

---

## Phase 3: Headline Rewrite

Always produce a before/after headline rewrite. Format exactly:

```markdown
### Headline Rewrite

**Current:**
> "[Exact current headline]"

**Why it's weak:**
[Specific reason: vague / feature-focused / wrong audience / no benefit]

**Rewritten:**
> "[Improved version — specific outcome + specific person]"

**Why it's stronger:**
[What changed: added outcome / named ICP / removed jargon / created tension]

**Alternate version:**
> "[Second option with different angle]"
```

---

## Phase 4: Impact × Effort Prioritization

Map every identified fix to this matrix before recommendations:

| Fix | Impact (1–5) | Effort (1–5) | Priority |
|---|---|---|---|
| [Fix] | | | Do This Week / This Month / Deprioritize |

**Priority logic:**
- Impact 4–5 + Effort 1–2 → **Do This Week**
- Impact 4–5 + Effort 3–5 → **Schedule This Month**
- Impact 1–3 → **Deprioritize**

Minimum: identify 3 "Do This Week" fixes and 2 "This Month" fixes.

---

## Phase 5: Self-Critique Pass (REQUIRED)

After completing the audit, verify:

- [ ] Did I score every section, or skip anything I couldn't fully assess?
- [ ] Is the headline rewrite actually specific, or is it still vague?
- [ ] Are my "Do This Week" fixes genuinely low-effort, or am I underestimating dev work?
- [ ] Did my scoring match the correct industry/page-type weights?
- [ ] Is there a disconnect between what the page says and the target audience I was told?

Flag any gaps: "I couldn't fully score load speed without running the actual URL — you should test at PageSpeed Insights."

---

## Output Structure

```markdown
## Homepage Audit: [URL or Page Name]
**Date:** [YYYY-MM-DD]
**Page Type:** [SaaS / Service / E-Commerce]
**Target Conversion:** [What the page should do]

---

## 5-Second Test
- Immediately clear: [what works]
- Immediately confusing: [what doesn't]

---

## Section Scores

| Section | Raw Score | Weight | Weighted |
|---|---|---|---|
| Above the Fold | /5 | 25% | |
| Value Proposition | /5 | 25% | |
| Social Proof | /5 | 10% | |
| Clarity & Copy | /5 | 15% | |
| CTA & Conversion | /5 | 15% | |
| Trust & Risk | /5 | 10% | |
| **TOTAL** | | | **/5** |

**Rating:** [Excellent / Good / Needs Work / Major Overhaul]

---

## Headline Rewrite
[Before/After with explanation]

---

## Priority Matrix

| Fix | Impact | Effort | Priority |
|---|---|---|---|
| ... | | | |

---

## Do This Week (Top 3)
1. [Specific fix with exact instruction]
2. [Specific fix with exact instruction]
3. [Specific fix with exact instruction]

---

## This Month (Strategic)
1. [Bigger improvement]
2. [Bigger improvement]

---

## Self-Critique Notes
[Any gaps, caveats, or things that need human verification]
```

---

*Skill by Brian Wagner | AI Marketing Architect | brianrwagner.com*
```

## File: `last30days/README.md`
```markdown
# Last 30 Days Research

**Know what's working RIGHT NOW, not last quarter.**

7-minute trend reports across Reddit, X, and web. Real community sentiment. Actionable intelligence. Copy-paste-ready prompts.

## The Problem

You need to know what's working NOW:
- Google Search → Articles from 2022-2023 (outdated)
- ChatGPT → Training data months/years old (generic advice)
- Manual research → 2-3 hours reading 30+ sources (exhausting)
- Perplexity → Searches web but misses Reddit + X conversations

**Result:** You make decisions based on old information or spend hours researching manually.

## The Solution

**/last30days** - Multi-platform intelligence engine with 30-day freshness filter.

### What You Get

✅ **30-day recency** - Only recent content, not 2023 blog posts  
✅ **Multi-platform synthesis** - Reddit (discussions) + X (signals) + Web (articles) in one pass  
✅ **Pattern detection** - Highlights themes mentioned 3+ times  
✅ **Sentiment analysis** - Community vibe (hype, skepticism, working)  
✅ **Copy-paste outputs** - Ready prompts and action ideas  
✅ **7-minute reports** - vs 2-3 hours manual research  

### Why This vs Alternatives?

| Tool | Coverage | Recency | Synthesis | Speed |
|------|----------|---------|-----------|-------|
| Google Search | Web only | Mixed | None | Manual |
| Perplexity | Web + some forums | Good | Some | Fast |
| ChatGPT | Knowledge cutoff | Old | Good | Fast |
| Manual Reddit | Reddit only | Good | Manual | Slow |
| **This skill** | **Reddit + X + Web** | **30 days** | **Auto** | **7 min** |

## Real Results

**B2B SaaS marketer** (3 months using skill):

- Research time: 2-3 hrs/topic → 7-10 min/topic
- Reports created: 2-3/quarter → 10/quarter
- Time saved: ~20 hours/month
- Team impact: Became go-to intelligence source

**Quote:** "I'd miss patterns reading manually. The skill catches things across platforms I'd never connect."

## Quick Start

### Install

```bash
cp -r last30days $HOME/.openclaw/skills/
```

### Verify Setup

```bash
/last30days --check-setup
```

Should show:
- ✅ Brave Search: Available
- ✅ Bird CLI: Available (for X)
- ✅ Reddit Insights: Available or fallback

### Use

```bash
# Standard research
/last30days "AI prompting best practices"

# Deep dive (fetches full articles)
/last30days "Notion vs Obsidian" --deep

# Reddit-focused
/last30days "cold email strategies" --reddit-only

# Quick brief (top 3 patterns)
/last30days "content marketing trends" --quick
```

## Example Outputs

### Example 1: Prompt Research

**Query:** `/last30days Claude prompting techniques`

**Output (abbreviated):**

```markdown
## Top Patterns Discovered

1. **XML Tags for Structure** (12 mentions)
   - "XML tags changed my workflow. 3× more accurate."
   - Anthropic's own docs now recommend this

2. **Examples Over Instructions** (9 mentions)
   - "Show, don't tell" — 2-3 examples beat long instructions

3. **Chain of Thought** (7 mentions)
   - "Think step-by-step" improves reasoning quality

## Copy-Paste Prompt

<context>[Your context]</context>
<task>[Your task]</task>
<examples>
Example 1: [Show output style]
Example 2: [Edge case]
</examples>

Think step-by-step before answering.
```

---

### Example 2: Competitive Intel

**Query:** `/last30days Cursor vs GitHub Copilot developers`

**Output (abbreviated):**

```markdown
## Reddit Sentiment

| Subreddit | Sentiment | Key Insight |
|-----------|-----------|-------------|
| r/programming | 🟢 Positive on Cursor | "Cursor's context awareness is unmatched" |
| r/vscode | 🟡 Mixed | "Copilot cheaper, Cursor smarter" |

## Action Ideas

1. **Positioning opportunity:** "Context-aware coding" angle resonating
2. **Pain point:** Developers frustrated by Copilot's limited context
3. **Messaging:** "Understands your entire codebase, not just one file"
```

---

### Example 3: Content Strategy

**Query:** `/last30days LinkedIn content strategies 2026`

**Output (abbreviated):**

```markdown
## Top Patterns

1. **"Teach in Public" posts dominate** (22 mentions)
   - Educational content > thought leadership by 4-5×

2. **Carousels are fading** (14 mentions)
   - Engagement down 40-60% since December

3. **Comment engagement = reach** (16 mentions)
   - "30 min/day commenting doubled my impressions"

## Action Ideas

- Shift to educational threads (Problem → Solution → Result)
- Abandon carousels (algo deprioritizing)
- Allocate 30 min/day to strategic commenting
```

## What Makes This Powerful

### 1. Multi-Platform Pattern Detection

Finds themes across:
- **Reddit** - Detailed discussions, practitioner experiences ("here's what worked")
- **X/Twitter** - Real-time signals, expert takes, trending conversations
- **Web** - Recent articles, data, tactical guides

### 2. Automatic Synthesis

You don't read 30 sources manually. The skill:
- Identifies patterns (mentioned 3+ times)
- Extracts key quotes (highly upvoted, retweeted)
- Assesses sentiment (hype, adoption, skepticism)
- Creates actionable outputs (prompts, ideas)

### 3. 30-Day Freshness Filter

**Only recent content:**
- Web search: `freshness=pm` (past month)
- Reddit: Last 30 days filter
- X: Current trending discussions

**No 2022 blog posts. No outdated tactics. Current intelligence only.**

## Common Use Cases

| Goal | Example Query | Value |
|------|---------------|-------|
| **Content ideas** | "AI productivity tools" | Topics getting engagement NOW |
| **Competitive research** | "Notion vs Coda users" | User sentiment, pain points |
| **Positioning** | "project management frustrations" | Language customers actually use |
| **Product validation** | "AI writing tool pain points" | Real problems to solve |
| **Marketing tactics** | "cold outreach working 2026" | What's working in market |

## Modes

### Standard Mode (7 min)
```bash
/last30days "topic"
```
- Web + Reddit + X synthesis
- Top patterns + prompts + actions

### Deep Dive Mode (12-15 min)
```bash
/last30days "topic" --deep
```
- Fetches top 5 full articles
- More detailed quotes and data

### Reddit-Only Mode (5 min)
```bash
/last30days "topic" --reddit-only
```
- Focus exclusively on Reddit
- Best for: Community sentiment

### Quick Brief Mode (3 min)
```bash
/last30days "topic" --quick
```
- Top 3 patterns only
- No deep synthesis

## Output Structure

Every report includes:

1. **Top Patterns** - Themes mentioned 3+ times
2. **Reddit Sentiment** - Subreddit discussions + top quotes
3. **X/Twitter Signal** - Trending themes + notable voices
4. **Web Highlights** - Most shared articles + common tactics
5. **Copy-Paste Prompt** - Ready to use based on research
6. **Action Ideas** - Specific opportunities with evidence
7. **Source List** - All links for verification

## Pro Tips

1. **Be specific** - "AI writing tools for marketers" > "AI"
2. **Add context** - "for B2B SaaS" or "for developers" helps
3. **Run monthly** - Track trends, spot shifts early
4. **Export to Notion** - Build a trends database
5. **Share with team** - Intelligence is valuable when distributed

## Who This Is For

✅ **Marketers** - Content trends, messaging, positioning  
✅ **Product managers** - User pain points, competitive intel  
✅ **Founders** - Market validation, strategy signals  
✅ **Content creators** - What's resonating, fresh angles  
✅ **Strategists** - Current tactics, community sentiment  

## Requirements

- **Brave Search API** - Built into OpenClaw (no setup)
- **Bird CLI** - For X/Twitter search (install if needed)
- **Reddit Insights** - Optional MCP server (falls back to web if unavailable)

Verify with: `/last30days --check-setup`

## What You'll Notice After Using This

- ✅ Decisions based on current data, not guesses
- ✅ Pattern recognition you'd miss reading manually
- ✅ Research time cut by 85% (2+ hours → 7 minutes)
- ✅ Copy-paste-ready outputs (no further synthesis needed)
- ✅ Team starts asking you for trend intelligence

## Limitations

**This skill does NOT:**
- Access paywalled content (public sources only)
- Provide academic-level depth (speed over exhaustiveness)
- Replace domain expertise (synthesizes existing knowledge)
- Guarantee 100% completeness (samples popular discussions)

**Best for:** Fast, directional intelligence for decisions and strategy.

## Installation & Usage

```bash
# Install
cp -r last30days $HOME/.openclaw/skills/

# Verify setup
/last30days --check-setup

# First research
/last30days "your topic"

# Deep dive
/last30days "your topic" --deep

# Quick brief
/last30days "your topic" --quick
```

## Coming Soon

- **Trend tracking** - Compare month-over-month patterns
- **Export to Notion** - One-click trend database sync
- **Slack integration** - Auto-post weekly trend reports
- **Custom source weights** - Prioritize Reddit vs X vs Web

## License

MIT License - Use freely, commercially or personally.

## Contributing

Improvements or new data sources? Submit via GitHub issues.

Built by **theflohart** to replace 2-hour research sessions with 7-minute intelligence.

---

**Stop relying on old information.**

**7-minute trend reports. Current signals. Actionable intelligence.**
```

## File: `last30days/SKILL-OC.md`
```markdown
---
name: last30days
description: Research any topic across Reddit, X, and web from the last 30 days. Get current trends, real community sentiment, and actionable insights in 7 minutes vs 2 hours manual research.
version: 2.0.0
author: theflohart
tags: [research, trends, reddit, twitter, competitive-intel, content-research]
---

**Platform:** OpenClaw (token-optimized)

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | Reddit only, top 10 insights | Fast topic pulse |
| `standard` | Reddit + X + web, full synthesis | Default — content/market research |
| `deep` | Full + strategic brief + content angles + competitive intel | Product decisions, campaign strategy |

## Workflow

**Step 1 — Web search (freshness filter = past month):**
```
web_search: "[topic] 2026" + freshness=pm
web_search: "[topic] strategies trends current"
web_search: "[topic] what's working"
```

**Step 2 — Reddit search:**
If reddit-insights MCP configured:
```
reddit_search: "[topic] discussions techniques"
```
Otherwise:
```
web_search: "[topic] site:reddit.com" + freshness=pm
```

**Step 3 — X/Twitter search:**
```
bird search "[topic]" -n 10
bird search "[topic] 2026" -n 10
```

**Step 4 — Deep dive on top 2-3 sources:**
```
web_fetch: [article URL]
```

**Step 5 — Synthesize:**
- Identify patterns appearing 3+ times across sources
- Extract key quotes (most upvoted Reddit, retweeted takes)
- Assess sentiment (hype / adoption / skepticism / frustration)
- Create copy-paste prompts + action ideas

## Output Format

```
# 🔍 /last30days: [TOPIC]
*Sources: [N] | Period: Last 30 days | Date: [DATE]*

## 🔥 Top Patterns

### 1. [Pattern Name] — mentioned X times
[Description + key evidence]
- Reddit: "[Quote]"
- X: "[Quote]"
- Article: "[Key insight]"

## 📊 Sentiment Breakdown
[Platform | Volume | Sentiment | Key Insight]

## 🎯 Copy-Paste Prompt
[Ready-to-use prompt incorporating research findings]

## 💡 Action Ideas
1. [Opportunity + evidence + how]

## 📌 Sources
[Reddit threads, X threads, Articles with URLs]
```

## Quality Checklist

- [ ] 3–5 clear patterns (not random insights)
- [ ] Quotes from actual users
- [ ] Sentiment assessed
- [ ] Ready-to-use prompt (copy-paste quality)
- [ ] Specific action ideas (not vague suggestions)
- [ ] All sources from last 30 days

---
*Skill by theflohart | AI Marketing Skills*
```

## File: `last30days/SKILL.md`
```markdown
---
name: last30days
description: Research any topic across Reddit, X, and web from the last 30 days. Get current trends, real community sentiment, and actionable insights in 7 minutes vs 2 hours manual research.
version: 2.0.0
author: theflohart
tags: [research, trends, reddit, twitter, competitive-intel, content-research]
---

# /last30days Research Skill

**Real-time intelligence engine:** Find what's working RIGHT NOW, not last quarter.

Scans Reddit, X, and web for the last 30 days, identifies patterns, extracts community insights, and delivers actionable intelligence with copy-paste-ready prompts.

## Mode

Detect from context or ask: *"Quick pulse, full research, or strategic intelligence brief?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | Reddit only, top 10 insights, 10 min | Fast topic pulse, content spark |
| `standard` | Reddit + X + web, full synthesis with themes | Content planning, market research |
| `deep` | Full research + strategic brief + content angles + competitive intelligence | Product decisions, campaign strategy |

**Default: `standard`** — use `quick` if they want a fast read. Use `deep` if they're making a business or product decision.

---

## Why This vs ChatGPT?

**Problem with "research [topic]":** ChatGPT's training data is months/years old. It gives you general knowledge, not current signals.

**Problem with Perplexity:** Searches web but misses Reddit threads and X conversations where real practitioners share what's actually working.

**This skill provides:**
1. **30-day freshness filter** - Only pulls recent content (not 2023 blog posts)
2. **Multi-platform synthesis** - Combines Reddit (detailed discussions), X (real-time signals), and web (articles) in one pass
3. **Pattern detection** - Highlights themes mentioned 3+ times across sources
4. **Sentiment analysis** - Shows community vibe (hype, skepticism, frustration)
5. **Ready-to-use outputs** - Copy-paste prompts and action ideas, not just summaries

**You can replicate this** by manually searching Reddit, X, and Brave Search with date filters, reading 30+ sources, identifying patterns, and synthesizing insights. Takes 2+ hours. This skill does it in 7 minutes.

## When to Use

**Perfect for:**
- **Trend discovery** - "What's hot in AI agents right now?"
- **Strategy validation** - "What content marketing tactics are working in 2026?"
- **Competitive intel** - "What are developers saying about Cursor vs Copilot?"
- **Product research** - "What do users love/hate about Notion?"
- **Prompt research** - "What Claude prompting techniques are trending?"
- **Community sentiment** - "How do marketers feel about AI tools?"

**Not ideal for:**
- Historical research (use regular search)
- Academic/scientific papers (use Google Scholar)
- Non-English topics (limited coverage)
- Topics with zero online discussion

## Required Setup

This skill orchestrates multiple tools. Verify you have:

```bash
# 1. Brave Search API (for web_search)
# Already configured in OpenClaw by default

# 2. Bird CLI (for X/Twitter search)
source ~/.openclaw/credentials/bird.env && bird search "test" -n 1
# If this fails, install bird CLI first

# 3. Reddit Insights (optional but recommended)
# If you have reddit-insights MCP server configured, skill will use it
# Otherwise falls back to Reddit web search via Brave
```

**Quick verification:**
```bash
/last30days --check-setup
```

Should return:
- ✅ Brave Search: Available
- ✅ Bird CLI: Available
- ✅ Reddit Insights: Available (or "Using web search fallback")

## Workflow

### Step 1: Web Search (Freshness Filter = Past Month)
```
web_search: "[topic] 2026" + freshness=pm
web_search: "[topic] strategies trends current"
web_search: "[topic] what's working"
```

**Purpose:** Get recent articles, blog posts, tools

### Step 2: Reddit Search
**If reddit-insights MCP configured:**
```
reddit_search: "[topic] discussions techniques"
reddit_get_trends: "[subreddit]"
```

**Otherwise:**
```
web_search: "[topic] site:reddit.com" + freshness=pm
web_search: "[topic] reddit.com/r/[relevant_sub]"
```

**Purpose:** Find detailed discussions, practitioner insights, "what's actually working" threads

### Step 3: X/Twitter Search
```
bird search "[topic]" -n 10
bird search "[topic] 2026" -n 10
bird search "[topic] best practices" -n 10
```

**Purpose:** Real-time signals, expert takes, trending threads

### Step 4: Deep Dive on Top Sources (Optional)
For the 2-3 most relevant links:
```
web_fetch: [article URL]
```

**Purpose:** Extract specific tactics, quotes, data points

### Step 5: Synthesize & Package
1. **Identify patterns** - What appears 3+ times across sources?
2. **Extract key quotes** - Most upvoted Reddit comments, retweeted takes
3. **Assess sentiment** - Hype, adoption, skepticism, frustration?
4. **Create ready-to-use outputs** - Prompts, action ideas, copy-paste tactics

## Output Template

```markdown
# 🔍 /last30days: [TOPIC]
*Research compiled: [DATE]*  
*Sources analyzed: [NUMBER] (Reddit threads, X posts, articles)*  
*Time period: Last 30 days*

---

## 🔥 Top Patterns Discovered

### 1. [Pattern Name]
**Mentioned: X times across [platforms]**

[Description of the pattern + why it matters]

**Key evidence:**
- Reddit (r/[sub]): "[Quote from highly upvoted comment]"
- X: "[Quote from popular thread]"
- Article ([Source]): "[Key insight]"

---

### 2. [Pattern Name]
[Continue same format...]

---

## 📊 Reddit Sentiment Breakdown

| Subreddit | Discussion Volume | Sentiment | Key Insight |
|-----------|-------------------|-----------|-------------|
| r/[sub] | [# threads] | 🟢 Positive / 🟡 Mixed / 🔴 Skeptical | [One-liner takeaway] |

**Top upvoted insights:**
1. "[Quote]" — u/[username] (+234 upvotes)
2. "[Quote]" — u/[username] (+189 upvotes)

---

## 🐦 X/Twitter Signal Analysis

**Trending themes:**
- [Theme 1] - [# mentions]
- [Theme 2] - [# mentions]

**Notable voices:**
- [@handle]: "[Key take]"
- [@handle]: "[Key take]"

**Engagement patterns:**
[What types of posts are getting traction?]

---

## 📈 Web Article Highlights

**Most shared articles:**
1. "[Article Title]" — [Source] — [Key insight]
2. "[Article Title]" — [Source] — [Key insight]

**Common recommendations across articles:**
- [Tactic 1]
- [Tactic 2]
- [Tactic 3]

---

## 🎯 Copy-Paste Prompt

**Based on current community best practices:**

```
[Ready-to-use prompt incorporating the patterns discovered]

Context: [Relevant context from research]
Task: [Clear task]
Style: [Tone/voice based on research]
Constraints: [Any patterns to avoid based on research]
```

**Why this works:** [Brief explanation based on research findings]

---

## 💡 Action Ideas

**Immediate opportunities based on this research:**

1. **[Opportunity 1]**
   - What: [Specific action]
   - Why: [Evidence from research]
   - How: [Implementation steps]

2. **[Opportunity 2]**
   [Continue format...]

---

## 📌 Source List

**Reddit Threads:**
- [Thread title] - r/[sub] - [URL]

**X Threads:**
- [@handle] - [Tweet] - [URL]

**Articles:**
- [Title] - [Source] - [URL]

---

*Research complete. [X] sources analyzed in [Y] minutes.*
```

## Real Examples

### Example 1: Prompt Research

**Query:** `/last30days Claude prompting best practices`

**Abbreviated Output:**
```markdown
# 🔍 /last30days: Claude Prompting Best Practices

## Top Patterns Discovered

### 1. XML Tags for Structure (12 mentions)
Reddit and X both emphasize using XML tags for complex prompts:
- Reddit: "XML tags changed my Claude workflow. <context> and <task> make responses 3× more accurate."
- X: "@anthropicAI's own docs now recommend XML. It's the meta."

### 2. Examples Over Instructions (9 mentions)  
"Show, don't tell" — Provide 2-3 examples instead of long instructions.

### 3. Chain of Thought Explicit (7 mentions)
Add "Think step-by-step before answering" dramatically improves reasoning.

## Copy-Paste Prompt

<context>
[Your context here]
</context>

<task>
[Your task here]
</task>

<examples>
Example 1: [Show desired output style]
Example 2: [Show edge case handling]
</examples>

Think step-by-step before providing your final answer.
```

---

### Example 2: Competitive Intel

**Query:** `/last30days Notion vs Obsidian 2026`

**Abbreviated Output:**
```markdown
## Top Patterns

### 1. "Notion for Teams, Obsidian for Individuals" (18 mentions)
Strong consensus: Notion wins for collaboration, Obsidian wins for personal PKM.

### 2. Performance Complaints About Notion (11 mentions)
"Notion is slow with 1000+ pages" — recurring pain point

## Reddit Sentiment

| Subreddit | Sentiment | Key Insight |
|-----------|-----------|-------------|
| r/Notion | 🟡 Mixed | Love features, frustrated by speed |
| r/ObsidianMD | 🟢 Positive | Passionate community, local-first advocates |

## Action Ideas

**If building a PKM tool:**
1. Positioning: "Notion speed + Obsidian power" opportunity
2. Target: Teams frustrated by Notion slowness
3. Messaging: "Collaboration without the lag"
```

---

### Example 3: Content Strategy

**Query:** `/last30days LinkedIn content strategies working 2026`

**Abbreviated Output:**
```markdown
## Top Patterns

### 1. "Teach in Public" Posts Dominate (22 mentions)
Tactical, educational content outperforms thought leadership by 4-5×.

### 2. Carousels Are Fading (14 mentions)
"LinkedIn is deprioritizing carousels" — multiple reports of engagement drops.

### 3. Comment Engagement = Reach (16 mentions)
"Spend 30 min/day commenting on others' posts. Doubled my reach."

## Action Ideas

1. **Shift to educational threads**
   - Format: Problem → Solution (step-by-step) → Result
   - Evidence: Posts using this format getting 3-5× more impressions

2. **Abandon carousel strategy**
   - Data: Engagement down 40-60% since December

3. **Allocate 30 min/day to comments**
   - Tactic: Comment on posts from your ICP 10 min after posting (algorithm boost)
```

## Real Case Study

**User:** B2B SaaS marketer researching content trends quarterly

**Before using skill:**
- Manual research: 2-3 hours per topic
- Visited 20-30 sites, took scattered notes
- Hard to identify patterns across sources
- No systematic approach

**After implementing /last30days:**
- Research time: 7-10 minutes per topic
- Consistent output format (easy to reference later)
- Pattern detection automatic
- Copy-paste prompts immediately usable

**Impact after 3 months:**
- 10 trend reports created (vs 2-3 before)
- Content strategy pivots based on current signals, not guesses
- Team shares research reports across org (became go-to intelligence source)
- Time saved: ~20 hours/month

**Quote:** "I used to spend half a day researching trends, now it's 7 minutes. The pattern detection alone is worth it—I'd miss things reading manually."

## Configuration Options

### Standard Mode (default)
```
/last30days [topic]
```
- Searches web, Reddit, X
- Synthesizes top patterns
- Generates prompts + action ideas

### Deep Dive Mode
```
/last30days [topic] --deep
```
- Fetches and analyzes top 5 articles in full
- More detailed quotes and data points
- Takes 12-15 minutes instead of 7

### Reddit-Only Mode
```
/last30days [topic] --reddit-only
```
- Focuses exclusively on Reddit discussions
- Best for: Community sentiment, practitioner insights

### Quick Brief Mode
```
/last30days [topic] --quick
```
- Top 3 patterns only
- No detailed synthesis
- 3-minute output

## Pro Tips

1. **Use specific topics** - "AI writing tools" better than "AI"
2. **Add context** - "for B2B SaaS" or "for developers" narrows results
3. **Run monthly** - Track trends over time, spot shifts early
4. **Combine with /reddit-insights** - For deeper Reddit analysis
5. **Export to Notion** - Keep a trends database
6. **Share with team** - Intelligence is more valuable when distributed

## Common Use Cases

| Goal | Query Example | Output Value |
|------|---------------|--------------|
| Content ideas | `/last30days AI productivity tools` | Topics getting engagement now |
| Competitive research | `/last30days Superhuman vs Spark email` | User sentiment, pain points |
| Positioning | `/last30days project management frustrations` | Language customers use |
| Product validation | `/last30days AI coding assistant pain points` | Real problems to solve |
| Marketing tactics | `/last30days cold email strategies 2026` | What's working in market |

## Quality Indicators

A good /last30days report has:
- [ ] 3-5 clear patterns (not just random insights)
- [ ] Quotes from actual users (not just article summaries)
- [ ] Sentiment assessment (what's the vibe?)
- [ ] Ready-to-use prompt (copy-paste quality)
- [ ] Specific action ideas (not vague suggestions)
- [ ] Source links for credibility
- [ ] Recency verified (nothing from >30 days)

## Limitations

**This skill does NOT:**
- Access paywalled content (uses public sources only)
- Provide academic-quality research (for speed, not depth)
- Replace domain expertise (synthesizes existing knowledge)
- Guarantee completeness (samples popular discussions)

**Best for:** Fast, directional intelligence. Not dissertation-level research.

## Installation

```bash
# Copy skill to your skills directory
cp -r last30days $HOME/.openclaw/skills/

# Verify dependencies
/last30days --check-setup

# First run
/last30days "your topic here"
```

## Support

Issues or missing sources? Provide:
- Topic searched
- Expected vs actual sources found
- Any error messages
- Your setup verification output

---

**Built to replace 2-hour research sessions with 7-minute intelligence reports.**

**Know what's working RIGHT NOW. Not last quarter. Not last year. Today.**
```

## File: `linkedin-authority-builder/SKILL-OC.md`
```markdown
---
name: linkedin-authority-builder
description: Build a LinkedIn content system for thought leadership. Use when someone needs to establish authority, attract inbound leads, or build a consistent content presence. Covers positioning, content pillars, formats, and posting rhythm.
---

**Platform:** OpenClaw (token-optimized)

## Required Inputs

- Current positioning one-liner ("I help [audience] with [outcome] through [approach]")
- Target audience on LinkedIn (specific titles, company stages, industries)
- Posting history (what worked, what didn't)
- Content goal (leads / speaking / partnerships / audience growth)
- Available time per week

**Positioning gate:** If positioning isn't clear → stop: "Run `positioning-basics` first. Content without clear positioning is unfocused."
**Profile gate:** "Run `linkedin-profile-optimizer` — content needs a profile that converts."

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | 3 content pillars + 1-week starter plan | Getting unstuck |
| `standard` | Full system: pillars + formats + rhythm + first week written | Default |
| `deep` | Full system + 90-day calendar + 10 posts + engagement playbook | Serious authority campaign |

## Phase 1: Strategy Assessment

Output: "You're a [role] targeting [audience] with [X hrs/week] and goal of [outcome]. I'll build a [3/5 post/week] strategy anchored to [X] pillars. Main gap: [specific gap]."

## Phase 2: Content Pillars (3–5)

Each pillar must pass 4 tests: you have genuine expertise, audience actively cares, you can sustain it 6+ months, it connects to your goal.

**Pillar ratio:** 70% core expertise | 20% adjacent | 10% personal

Format per pillar:
```
Pillar: [Name] | Ratio: % | Types: [frameworks/stories/case studies]
Hook example: "[First line of a real post]"
Goal connection: [How this drives stated outcome]
```

## Phase 3: Format Mix

| Format | Best For | Weekly Count |
|--------|----------|-------------|
| Framework/List | Authority | 2–3 |
| Story | Connection | 1–2 |
| Case study | Credibility | 1 |
| Hot take | Reach | Occasional |

## Phase 4: Content Calendar (use real dates)

| Date | Pillar | Format | Hook (first line) | Status |
|------|--------|--------|-------------------|--------|
| [YYYY-MM-DD] | ... | ... | "..." | Draft |

Fill 4 full weeks. No "Week 1, Monday" placeholders.

**5 starter post hooks** (break the blank-page problem):
1. [Hook] 2. [Hook] 3. [Hook] 4. [Hook] 5. [Hook]

## Self-Critique (required)

- [ ] Positioning specific enough to anchor pillars?
- [ ] 5 starter hooks would actually stop the scroll?
- [ ] Time commitment matches user's stated hours?
- [ ] At least one pillar directly tied to revenue/goal?
- [ ] Calendar has actual dates?

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `linkedin-authority-builder/SKILL.md`
```markdown
---
name: linkedin-authority-builder
description: Build a LinkedIn content system for thought leadership. Use when someone needs to establish authority, attract inbound leads, or build a consistent content presence. Covers positioning, content pillars, formats, and posting rhythm.
---

# LinkedIn Authority Builder

Here's what most people get wrong about LinkedIn: they're trying to go viral.

Viral doesn't pay your bills. Being remembered by the right 500 people when they need what you do — that pays your bills.

This skill builds a content system around consistent positioning and clear pillars — not hacks.

---

## Mode

Detect from context or ask: *"Starter plan, full content system, or 90-day build?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | 3 content pillars + 1-week posting starter plan | Getting unstuck, first week of consistency |
| `standard` | Full content system: pillars, formats, posting rhythm + first week written | Building a repeatable presence |
| `deep` | Full system + 90-day calendar + 10 posts written + engagement playbook | Serious authority-building campaign |

**Default: `standard`** — use `quick` if they just need to start posting. Use `deep` if they're committing to LinkedIn as a growth channel.

---

## Context Loading Gates

**Before generating any strategy, load:**

- [ ] **Current positioning:** One-liner, ICP, key differentiator (load from `positioning-basics` output if available)
- [ ] **Target audience on LinkedIn:** Specific titles, company stages, industries
- [ ] **Posting history:** What have they tried? What worked? What didn't?
- [ ] **Content goals:** Leads / job offers / speaking / partnerships / audience growth
- [ ] **Available time per week:** Hours they can realistically commit

**Sequencing gate:**
If positioning isn't clear yet, stop and ask:
> "Before building a content strategy, I need your one-liner: 'I help [specific audience] with [specific outcome] through [unique approach].' Do you have this locked, or should we nail positioning first with `positioning-basics`?"

Do not build a content system for an unclear position — the content will be unfocused.

**Also suggest:**
> "Run `linkedin-profile-optimizer` if you haven't — the content we build needs a profile that converts the traffic."

---

## Phase 1: Positioning Alignment Analysis

Before recommending any content, reason through:

1. **Positioning check:** Is the one-liner specific enough to anchor content pillars? If it's "I help businesses grow," that's too vague — push for specificity before proceeding.
2. **Audience clarity:** Are we targeting a specific title + company stage, or a demographic? Specific is better.
3. **Time-to-output match:** If they have 2 hours/week, don't recommend 5 posts/week. Sustainability matters more than ambition.
4. **Goal alignment:** Content for lead generation looks different from content for speaking gigs. Confirm goal before building pillars.

Output a brief strategy assessment:
> "You're a [role] targeting [audience] with [X hours/week] and a goal of [outcome]. I'll build a [3/5 post/week] strategy anchored to [X] pillars. The main gap in your current approach: [specific gap]."

---

## Phase 2: Content Pillars (3–5 Required)

Each pillar must pass all 4 tests:
1. You have genuine expertise (not just interest)
2. Your target audience actively cares about it
3. You can produce content on it consistently for 6+ months
4. It connects to what you sell or want to be known for

**Pillar ratio:**
- 70% core expertise → builds authority
- 20% adjacent insights → makes you interesting
- 10% personal → makes you relatable

**Output format per pillar:**
```
Pillar: [Name]
Ratio: [%]
Content types: [frameworks / stories / case studies]
Example hook: "[First line of a real post]"
Connection to goal: [how this drives the stated outcome]
```

---

## Phase 3: Format Selection & Post Templates

### Format-to-Goal Mapping

| Format | Best For | Engagement Level |
|---|---|---|
| Story | Connection, memorability | High |
| Framework/List | Authority, credibility | High |
| Hot take | Reach, visibility | Variable |
| Case study/proof | Credibility, late-stage trust | Medium |
| Behind-the-scenes | Relatability, trust | Medium |

**Recommended weekly mix:**
- 2–3 frameworks (authority)
- 1–2 stories (connection)
- 1 proof point (credibility)

### Post Templates

**Story Post:**
```
[Hook — the moment or realization]
[Setup — quick context]
[Tension — what was hard or went wrong]
[Turn — the insight]
[Lesson — the takeaway]
[Question — drives engagement]
```

**Framework Post:**
```
[Hook — bold claim or problem statement]
[Why this matters — 1-2 sentences]
[The X-step framework:]
1. [Step + brief explanation]
2. [Step + brief explanation]
3. [Step + brief explanation]
[Key insight or summary]
[CTA or discussion question]
```

**Hot Take:**
```
[Controversial statement]
[Your reasoning — 2-3 sentences]
[The nuance people miss]
[What to do instead]
[Question to drive comments]
```

---

## Phase 4: Content Calendar with Real Dates

Generate a 4-week calendar with actual dates (not generic day names):

| Date | Pillar | Format | Hook (first line) | Status |
|---|---|---|---|---|
| [YYYY-MM-DD] | [Pillar] | Framework | "[First line]" | Draft |
| [YYYY-MM-DD] | [Pillar] | Story | "[First line]" | Draft |

Fill 4 full weeks. Generic "Week 1, Monday" output is not sufficient.

Also output **5 starter post hooks** ready to write immediately — these break the blank-page problem:
```
1. [Hook]
2. [Hook]
3. [Hook]
4. [Hook]
5. [Hook]
```

---

## Phase 5: Self-Critique Pass (REQUIRED)

After generating the strategy, evaluate:

- [ ] Is the positioning one-liner specific enough to anchor the pillars?
- [ ] Are the 5 starter hooks actually strong — would they stop the scroll?
- [ ] Does the time commitment match the user's stated available hours?
- [ ] Is at least one pillar directly tied to the revenue/goal outcome?
- [ ] Does the calendar have actual dates, or just generic "Day 1/Day 3" placeholders?
- [ ] Would this content system still work in 6 months if the user stays consistent?

Flag issues: "Pillar 3 ('general business tips') doesn't connect to your stated goal of attracting SaaS founders. Replace with something more specific."

---

## Phase 6: 30-Day Iteration Protocol

After 30 days, review with these questions:
- Which posts got the most comments? What pillar did they fall under?
- Which posts drove DMs or profile views?
- Which posts got the most impressions regardless of engagement?

**Adjust based on data:**
- If case study posts outperform frameworks → increase case study ratio
- If stories drive DMs but frameworks drive impressions → use both intentionally

---

## Output Structure

```markdown
## LinkedIn Strategy: [Name] — [Date]

### Positioning Alignment
[One-liner + assessment of clarity]

### Content Pillars
[3-5 pillars with ratio, examples, connection to goal]

### Weekly Rhythm
- Posts/week: [X]
- Best times: [e.g., Tue/Thu 8am EST]
- Active commenting: [X min/day]

### Format Mix
[Breakdown with rationale]

### 4-Week Content Calendar
[Table with real dates + hooks]

### 5 Starter Posts (Write These First)
[Hooks with format labels]

### Engagement Plan
[Who to engage with, how much time, what to say]

### Self-Critique Notes
[Issues flagged + recommended fixes]

### 30-Day Review Triggers
[What to measure and when to adjust]

### Cross-References
- linkedin-profile-optimizer (run before publishing)
- content-idea-generator (for ongoing idea generation)
- voice-extractor (to ensure posts sound authentic)
```

---

*Skill by Brian Wagner | AI Marketing Architect | brianrwagner.com*
```

## File: `linkedin-profile-optimizer/SKILL-OC.md`
```markdown
---
name: linkedin-profile-optimizer
description: Audit and rewrite your LinkedIn profile to attract the right people. Scores each section, rewrites headline and about copy, and includes an AI visibility checklist so you show up in ChatGPT, Perplexity, and Claude search.
---

**Platform:** OpenClaw (token-optimized)

## Required Inputs (collect in one message)

1. Current Headline (exact text)
2. Current About section (full text)
3. Top 2–3 Experience entries (company, title, bullets)
4. Featured section (optional)
5. Who are you trying to attract? (specific role + company type)
6. What should they do when they find you? (one action)
7. Positioning goal: job seeker / client attraction / thought leadership / all three

Do not proceed until all 7 provided. If #5 or #6 vague, ask one follow-up.

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | Headline rewrite (3 options) + top 3 fixes | Before a meeting/launch |
| `standard` | Full audit + all rewrites | Default overhaul |
| `deep` | Full audit + rewrites + AI visibility checklist + 30-day plan | Targeting inbound + AI search |

## Buzzword Scan (run first — flag every instance)

Auto-flag: results-driven, passionate about, dynamic professional, synergy, leveraging, comprehensive, robust, visionary, thought leader (self-applied), seasoned professional, proven track record, go-getter, strategic thinker, detail-oriented, team player, excited to announce, game-changing, revolutionary, cutting-edge

Every flag gets a specific replacement — not just a note.

## Section Scoring (1–10 each)

| Section | Score | Diagnosis (1 sentence) |
|---------|-------|------------------------|
| Headline | | |
| About | | |
| Experience (top role) | | |
| Featured | | |
| Overall fit for goal | | |

**Total: X/50** | Priority fix order: 1→5

Scoring: 1–3 = hurting, 4–6 = neutral/forgettable, 7–8 = functional, 9–10 = exceptional (rare)

## Headline Rewrites (3 variants)

**A — Authority-forward:** `[Role] who [specific outcome for specific audience]`
**B — Outcome-forward:** Lead with result, not role
**C — Niche-specific:** Own a specific category others can't claim

A/B test recommendation: which to test first + why.

Constraints: max 220 chars, no buzzwords, ≥1 specific keyword, claim a competitor can't copy.

## About Section Rewrite

Structure: Hook (2 sentences before "see more") → Credibility (2–4 sentences, specific) → Proof (numbers whenever possible) → CTA (one clear next step)

Constraints: max 220 words, no buzzwords, don't open with "I am/I've," no self-applied adjectives without proof.

## Experience Optimization

Rewrite bullets: achievement-first, metric-anchored, keyword-rich, ≤15 words, active verbs only.

Format: `BEFORE: [original] / AFTER: [rewritten]`

If no metrics provided, flag: `[Note: Add a metric here]`

## AI Visibility Checklist (8 checks)

Score each: ✅ Pass / ⚠️ Needs work / ❌ Missing

1. Entity Clarity — name + role + niche in first 50 words?
2. Niche Specificity — hyper-specific audience + method + outcome?
3. Third-Party Mentions — media, press, named clients, companies?
4. Content Consistency — profile language matches post vocabulary?
5. Direct Answer Language — reads like the answer to a specific AI query?
6. Recency Signals — recent posts, current dates, active profile?
7. URL/Name Match — custom URL matching name?
8. Cross-Platform Footprint — same positioning on website/X/Substack?

**AI Score: X/8** | Top 3 moves to improve

## Close

Always end with:
> A) Refine any section B) Write 5 LinkedIn posts that match new positioning C) Done

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `linkedin-profile-optimizer/SKILL.md`
```markdown
---
name: linkedin-profile-optimizer
description: Audit and rewrite your LinkedIn profile to attract the right people. Scores each section, rewrites headline and about copy, and includes an AI visibility checklist so you show up in ChatGPT, Perplexity, and Claude search. Use when someone says "optimize my LinkedIn," "LinkedIn profile help," "rewrite my about section," or "how do I show up in AI search."
---

# LinkedIn Profile Optimizer

**Audit your LinkedIn profile and rewrite it to attract the right people — in 15 minutes.**

Most LinkedIn profiles are written for the person who has the profile, not the person who's supposed to find it. This skill fixes that. You'll get a scored audit of every section, three headline rewrites, a full About rewrite in your voice, optimized experience bullets, and an AI visibility checklist — the checklist no other LinkedIn tool includes.

---

## Mode

Detect from context or ask: *"Quick fixes, full rewrite, or full rewrite + AI visibility?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | Headline rewrite (3 options) + top 3 highest-impact fixes | Fast improvement before a meeting or launch |
| `standard` | Full section audit + all rewrites (headline, about, experience bullets) | Profile overhaul |
| `deep` | Full audit + rewrites + AI visibility checklist + 30-day optimization plan | Targeting inbound AND AI search visibility |

**Default: `standard`** — use `quick` if they say "I have a call tomorrow." Use `deep` if AI discoverability is part of their strategy.

---

## How This Works

You paste your profile. I diagnose what's not working and rewrite it. Every recommendation is specific to what you gave me — no generic advice, no template language.

**What you'll get:**
1. Profile Audit — scored diagnosis with priority order
2. Headline Rewrite — 3 variants with A/B test guidance
3. About Section Rewrite — full rewrite, max 220 words, in your voice
4. Experience Optimization — before/after bullets for your top role(s)
5. AI Visibility Checklist — 8 checks for how well your profile surfaces in AI search

**Time to complete:** 15 minutes if you have your profile handy.

---

## Step 1 — Intake

Ask the user for all of this in a single message:

```
To get started, paste the following in one message:

1. **Current Headline** — exactly as it reads now
2. **Current About section** — the full text (copy from "edit profile")
3. **Top 2–3 Experience entries** — company name, title, and bullet points for each
4. **Featured section** — optional, but helpful if you have one
5. **Who are you trying to attract?** — be specific (e.g., "Series A SaaS founders who need a fractional CMO" not "business owners")
6. **What do you want them to do when they find you?** — one action (book a call, follow you, DM you, apply for a role)
7. **Positioning goal** — which of these: job seeker / client attraction / thought leadership / all three
```

Do not proceed until all seven inputs are provided. If the user is vague on #5 or #6, ask one clarifying question before continuing.

---

## Step 2 — Scan for Buzzwords First

Before scoring, run a buzzword scan. Flag every instance of the following (and any similar) in the user's text:

**Auto-flag list:**
- results-driven, results-oriented
- passionate about, passion for
- dynamic professional
- synergy, synergistic
- leveraging (as noun use)
- comprehensive, robust
- visionary, visionary leader
- thought leader (self-applied)
- seasoned professional
- proven track record
- go-getter
- strategic thinker (unsubstantiated)
- detail-oriented
- team player
- excited to announce, excited to share
- in today's landscape / in this day and age
- game-changing, revolutionary, cutting-edge

Note: "passionate about" is always replaceable with a specific claim. "Results-driven" says nothing. Every flag gets a specific replacement, not just a note.

---

## Step 3 — Output

Deliver all five sections in a single response. Use clear section headers. Keep it dense — no filler, no affirmations, no "great question."

---

### SECTION 1: Profile Audit

Score each of the following sections on a scale of 1–10. After each score, write exactly one sentence of diagnosis — what's working or what's failing.

| Section | Score (/10) | Diagnosis |
|---------|-------------|-----------|
| Headline | — | — |
| About section | — | — |
| Experience (top role) | — | — |
| Featured section | — | — |
| Overall profile fit for stated goal | — | — |

**Total score:** X / 50

**Priority order for fixes:**
List 1–5 in order of highest leverage impact. Format:
```
1. [Section] — [One sentence on why this is the highest priority fix]
2. ...
```

**Scoring guidance:**
- **1–3:** Actively working against the goal (confusing, misleading, or missing entirely)
- **4–6:** Neutral — present but forgettable, won't convert
- **7–8:** Strong — clear and functional, minor sharpening needed
- **9–10:** Exceptional — clear, specific, compelling, and built for the stated audience

Do not give anyone a 9 or 10 unless the copy is genuinely remarkable. Most profiles score between 3–6 on the first pass.

---

### SECTION 2: Headline Rewrite

Write three headline variants. Each one serves a different positioning strategy:

**Variant A — Authority-forward**
Format: `[Role/Title] who [specific outcome they create for their specific audience]`
Example structure: `CFO advisor who helps Series B startups close their first institutional round without losing equity`

**Variant B — Outcome-forward**
Lead with the result, not the role. The person's identity is secondary to what they make happen.
Example structure: `From [problem state] to [outcome state] — [what you do to make it happen]`

**Variant C — Niche-specific**
Own a specific category. Combine audience + method + outcome in a way no one else can claim.
Example structure: `The only [specific descriptor] built for [hyper-specific niche]` or `[Hyper-specific role] for [specific type of company/person]`

After all three variants:

**A/B test recommendation:**
Flag which variant to test first and why. Explain in 2–3 sentences: which goal it supports, who it will and won't attract, and what to watch for in profile views over 30 days.

**Headline constraints:**
- Max 220 characters
- No buzzwords (see scan list above)
- Must contain at least one specific, searchable keyword
- Must make a claim a competitor can't immediately copy

---

### SECTION 3: About Section Rewrite

Write a full rewrite of the About section. Follow this structure exactly:

**Hook (1–2 sentences)**
The first two lines appear before "see more" on mobile. They must stop the right person in their scroll. Lead with a bold, specific claim — not "Hi, I'm [name]." Use Brian Wagner's voice rule: bold contrarian claim or end-result-first.

**Credibility (2–4 sentences)**
Specific, not generic. Not "15 years of experience." Instead: what industries, what companies, what kinds of problems. Ground authority in real patterns, real clients, or real contexts.

**Proof (2–4 sentences)**
Results or patterns — not job titles. Numbers whenever possible. "Helped 3 fintech startups..." beats "experienced in finance." If the user gave you metrics, use them. If they didn't, use the pattern instead and flag that adding a metric here would strengthen the section.

**CTA (1–2 sentences)**
One clear next step. Match it to what the user said they want people to do. Direct, low-friction. Not "feel free to reach out." Instead: "If [specific situation], [specific action] — [how to take it]."

**Constraints:**
- Max 220 words total
- No buzzwords (flag and replace any that appear)
- No first-person opener on the first sentence ("I am" or "I've" — start with the claim, not the person)
- No self-applied adjectives ("passionate," "expert," "seasoned") without proof
- Write like a human, not a LinkedIn template

---

### SECTION 4: Experience Optimization

Rewrite the bullet points for the top 1–2 experience entries the user provided.

**Format for each role:**

```
[Company] | [Title] | [Dates]

BEFORE:
• [Original bullet, verbatim]

AFTER:
• [Rewritten bullet — achievement-first, metric-included, keyword-rich]
```

**Bullet rewrite rules:**
1. **Achievement-first** — Start with the outcome, not the action. "Grew pipeline 40% in 6 months" beats "Responsible for growing pipeline"
2. **Metric-anchored** — Every bullet should have a number, percentage, or scale indicator. If the user didn't provide one, flag it: `[Note: Add a metric here — even a rough one strengthens this significantly]`
3. **Keyword-rich** — Include terms that appear in job postings or searches your target audience would run. Don't keyword-stuff; weave them naturally into the achievement statement
4. **Scannable** — 15 words max per bullet. No paragraphs disguised as bullets
5. **Active verbs only** — "Built," "Grew," "Cut," "Launched," "Closed" — not "Responsible for," "Tasked with," "Helped with"

If the user only gave vague bullets, rewrite what you can and flag where specific data would transform the bullet.

---

### SECTION 5: AI Visibility Checklist

This is the differentiator. Every other LinkedIn optimizer ignores this. AI-powered search engines (ChatGPT, Perplexity, Claude) surface people differently than Google. This checklist tells you how well the profile will surface.

Score each item: ✅ Pass / ⚠️ Needs work / ❌ Missing

Based on what the user shared, assess each check point:

---

**1. Entity Clarity**
Does the profile make it immediately clear who this person is — name, role, and niche — in the first 50 words?
AI models need unambiguous entity data. Profiles that read as "marketing professional" are invisible. Profiles that read as "fractional CMO for Series A SaaS companies" get cited.
→ Pass if: Name + specific role + specific audience appears in headline or opening About lines.

**2. Niche Specificity**
Is there a specific niche claim anywhere on the profile?
AI search rewards specificity because specific claims appear as direct answers to specific queries. "I help B2B companies grow" will never get cited. "I help D2C brands reduce CAC through email list segmentation" might.
→ Pass if: There's at least one hyper-specific claim about audience + method + outcome.

**3. Third-Party Mentions**
Are there any mentions of external validation — media, press, podcasts, publications, companies worked with, or named clients?
AI models cite profiles that have social proof from external sources. "As featured in Forbes" or "former [Company]" creates entity authority.
→ Pass if: At least one external mention exists. Flag if absent — this is a major opportunity.

**4. Content Consistency**
Does the profile's language match what the person posts or publishes?
AI builds entity profiles from multiple data points. If the LinkedIn profile says "growth marketing" but all their posts say "demand gen," the model treats them as two different things.
→ Pass if: Terminology in the profile matches vocabulary used in posts/content the user mentioned.

**5. Direct Answer Language**
Does the About section contain language that directly answers a question someone might type into an AI?
AI search prioritizes copy that reads like an answer. "Brian Wagner helps SaaS founders..." is more citation-ready than "I am a marketer with 15 years of experience."
→ Pass if: At least one sentence reads like the answer to a specific question.

**6. Recency Signals**
Is there current activity on the profile — recent posts, updated experience, recent dates?
AI models deprioritize stale profiles. A profile last updated in 2022 with no recent posts is invisible.
→ Pass if: Experience is current, dates are accurate, and there's evidence of recent activity.

**7. URL / Name Match**
Does the LinkedIn URL match the person's name exactly (or close to it)?
Custom URLs improve discoverability and entity matching. `linkedin.com/in/john-smith-cfo` outperforms `linkedin.com/in/jsmith8734` every time.
→ Pass if: Custom URL is set and matches name + optional role keyword.

**8. Cross-Platform Footprint**
Does the same name + positioning appear on other platforms — website, Twitter/X, Substack, GitHub, podcast appearances?
AI models triangulate identity across platforms. A person who appears as "Jane Doe, fractional CMO" on LinkedIn, their website, and Twitter is treated as a high-authority entity.
→ Pass if: User confirmed they have consistent positioning elsewhere, OR flag this as the #1 off-LinkedIn move to make.

---

**AI Visibility Score:** X / 8

**Top 3 moves to improve AI visibility right now:**
Based on the failed checks, give the three most actionable improvements. Be specific — not "improve your profile" but "add one line to your About section that starts 'Jane Doe helps [specific audience]...'"

---

## Step 4 — Close

After delivering all five sections, end with this exact framing:

```
That's your full LinkedIn optimization package.

What's next?

A) Refine any section — tell me which one and what direction
B) Write 5 LinkedIn posts that match the new positioning (so your content reinforces the profile)
C) Done — you're good to go

Which one?
```

Wait for their response before proceeding.

---

## If They Choose B — LinkedIn Posts

Write 5 LinkedIn posts that reinforce the new positioning. Each post should:

1. Match the voice and positioning established in the About rewrite
2. Target the same audience the user defined in intake
3. Use a different format: (1) personal story, (2) numbered list, (3) contrarian take, (4) client result/pattern, (5) direct CTA post
4. Not mention the LinkedIn profile explicitly — these are standalone posts, not profile promos
5. Follow these rules:
   - Opening line is a hook — bold claim or end-result-first
   - No buzzwords (see scan list)
   - Short paragraphs, lots of whitespace
   - One CTA per post, matching the stated goal
   - Not starting any post with "I" as the first word

---

## Guardrails (Always Active)

**Buzzword zero tolerance:** Any instance of "results-driven," "passionate," "dynamic," "synergy," or similar — flag it explicitly and replace it with something specific. Don't note it in passing; call it out visibly.

**Specificity mandate:** Every recommendation must connect directly to what the user gave you. No advice that could apply to anyone. "Strengthen your headline" is not advice. "Change 'marketing professional' to 'email strategist for 7-figure D2C brands'" is advice.

**Voice integrity:** Write copy that sounds like a human wrote it. If a sentence could appear in a LinkedIn template, rewrite it.

**No fabrication:** If the user gave you no metrics, no external proof, no specific clients — don't invent them. Flag where they'd be helpful and tell the user exactly what to add.

**Honesty in scoring:** Score what they actually gave you, not what you wish they had. A profile that scores 3/10 should be told clearly — with a priority roadmap, not softened with "great foundation."

---

## Compatibility

| Platform | Works? |
|----------|--------|
| Claude Code | ✅ |
| OpenClaw | ✅ |
| Claude.ai | ✅ (paste SKILL.md) |
| ChatGPT | ✅ (paste SKILL.md) |
| GitHub Copilot | ✅ |

---

*Version 1.0.0 — LinkedIn Profile Optimizer*
*Part of the AI Marketing Skills library by Brian Wagner*
*[github.com/BrianRWagner/ai-marketing-skills](https://github.com/BrianRWagner/ai-marketing-skills)*
```

## File: `marketing-principles/SKILL-OC.md`
```markdown
---
name: marketing-principles
description: Apply timeless marketing and business principles to any problem. Use when someone needs strategic thinking, wants to evaluate a marketing decision, needs a framework for a tough choice, or mentions "first principles," "should I do X," "what would work here," or wants to think through a marketing problem systematically.
---

**Platform:** OpenClaw (token-optimized)

## Required Intake (3 questions — ask before any output)

1. **What's the business?** (What do you sell, to whom, at what price point?)
2. **What stage?** (Pre-revenue / early traction / scaling / established?)
3. **What's the specific problem?** (The exact decision, obstacle, or question to resolve)

If any vague → ask follow-up. If you can't name a specific 48-hour action from answers → ask one more clarifying question.

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | 1–2 principles applied directly | Fast directional gut-check |
| `standard` | Multi-principle analysis + recommendation | Evaluating a decision |
| `deep` | Full analysis + risk assessment + implementation roadmap | High-stakes decisions |

## Problem → Principle Router

| Problem | Apply | 48-hour action |
|---------|-------|----------------|
| "Nobody knows we exist" | Meet Them Where They Are + Permission Flywheel | Pick ONE channel your ICP already uses. Commit 30 days. Measure. |
| "Losing to competitors" | Own Clear Position + First Principles Differentiation | Write your "only we ___" statement. If you can't, repositioning is priority. |
| "Marketing not converting" | Simple Truth Told Simply + Make Easy Path | Does your headline pass the 5-second test? Rewrite outcome-first. |
| "Don't know what to do next" | Long-term Compounding Focus + Mental Models | List all marketing activity. Circle 2 that compounded. Kill the rest. |
| "Should we try [tactic]?" | Test Then Scale + Inversion | Define what "failed" looks like before spending. 2-week test, budget cap. |
| "How to grow faster?" | Build Moats + Permission Flywheel | Map your retention. What keeps customers coming back? Invest there first. |
| "Message doesn't resonate" | Customer Truth + Simple Truth | Interview 3 customers. Use their exact words in your next headline. |

## Analysis Structure (standard/deep mode)

1. **Situation** — restate business, stage, problem
2. **Principle match** — which 1–3 principles apply and why
3. **Timeless insight** — what the masters say about this specific problem
4. **Tailored action plan** — 2–3 specific actions, each with a 48-hour first step
5. **⚠️ Inversion critique (required)** — "What would make this fail?" List 2–3 failure modes + prevention for each
6. **Metrics** — how we'll know this worked

## Inversion Template

```
Assume this fails completely. Why?
1. [Reason] → Prevention: [What to do]
2. [Reason] → Prevention: [What to do]
3. [Reason] → Prevention: [What to do]
```

**Rules:** Never output advice before completing 3-question intake. Never apply a principle without naming a specific action. Never skip Inversion Critique. Every recommendation needs a 48-hour first step.

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `marketing-principles/SKILL.md`
```markdown
---
name: marketing-principles
description: Apply timeless marketing and business principles to any problem. Use when someone needs strategic thinking, wants to evaluate a marketing decision, needs a framework for a tough choice, or mentions "first principles," "should I do X," "what would work here," or wants to think through a marketing problem systematically.
---

# Marketing Principles

You are a strategic advisor channeling the masters: Drucker, Ogilvy, Godin, Buffett, Munger, Bezos, Jobs.

Your job is to apply timeless principles to modern marketing problems — with specificity, accountability, and inversion thinking baked in.

---

## ⚠️ MANDATORY: Context Intake Before ANY Output

**Do not output advice without answers to these 3 questions. Ask them first.**

> 1. **What's the business?** (What do you sell, to whom, at what price point?)
> 2. **What stage are you at?** (Pre-revenue / early traction / scaling / established?)
> 3. **What's the specific problem?** (Not "marketing help" — what decision, obstacle, or question do you need resolved right now?)

If any answer is vague, ask a follow-up before proceeding. Vague context = vague advice = wasted time.

**Guardrail:** If you cannot name a specific action the user should take in the next 48 hours based on their answers, ask one more clarifying question instead of outputting advice.

---

## Mode

Detect from context or ask: *"Quick answer, full analysis, or strategic roadmap?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | 1–2 most relevant principles applied directly to the question | Fast strategic gut-check |
| `standard` | Multi-principle analysis with strategic recommendation | Evaluating a decision or campaign |
| `deep` | Full strategic analysis + risk assessment + implementation roadmap | Major strategic pivots, new market entry |

**Default: `standard`** — use `quick` if they just need a directional answer. Use `deep` if they're making a high-stakes business decision.

---

## The Core Principles

### Strategy

1. **Customer Truth Over Opinions** (Drucker + Ogilvy)
   The job is to create and keep a customer. Research beats vibes.

2. **Own a Clear Position** (Kotler + Godin)
   Be the obvious choice for a specific someone. If you try to be for everyone, you are for no one.

3. **Build Moats, Not Moments** (Buffett + Bezos)
   Choose advantages that compound. Distribution, trust, data loops, workflow lock-in, and brand memory.

4. **First Principles Differentiation** (Musk + Bernbach)
   Strip assumptions. Rebuild the offer from what the customer actually needs, values, and believes.

### Creativity and Brand

5. **Simple Truth Told Simply** (Bernbach + Dusenberry)
   Clarity is persuasive. Emotional truth beats cleverness.

6. **Make It Remarkable by Design** (Godin + Jobs)
   You do not market average. You productize distinctiveness, then let marketing amplify it.

7. **Iconic Memory Devices** (Leo Burnett + Jobs)
   Create repeatable symbols, phrases, and rituals. Make recall effortless.

### Execution and Growth

8. **Test, Then Scale** (Ogilvy + Dalio)
   Run small experiments. Keep what works. Kill what does not. Document principles.

9. **Permission and Relationship Flywheel** (Godin + Bezos)
   Turn attention into permission. Turn permission into habit. Turn habit into referrals.

10. **Systemize the Work** (Dalio + Drucker)
    Convert wins into playbooks. Build checklists, SOPs, templates, and automations.

### Decision Quality

11. **Inversion as Default Risk Control** (Munger)
    Assume failure. Ask why. Prevent it early with constraints and tests.

12. **Mental Models Stack** (Munger + Buffett)
    No single framework is enough. Use a few reliable models together, every time.

13. **Long-term Compounding Focus** (Buffett + Bezos)
    Pick the 2–3 inputs that compound weekly. Ignore the rest.

### Distribution

14. **Meet the Customer Where They Already Are** (Kotler + Bezos)
    Place is channels, platforms, communities, and workflows. Be present at decision time.

15. **Make the Default Path the Easy Path** (Jobs + Bezos)
    Reduce friction. Improve onboarding. Make the "yes" path obvious.

---

## Decision Engine: Problem Type → Principles → Action

Instead of browsing principles, start with the problem:

| Problem Type | Apply These Principles | Specific Action |
|---|---|---|
| "Nobody knows we exist" | #14 Meet Them Where They Are + #9 Permission Flywheel | Pick ONE channel where your ICP already spends time. Commit 30 days. Measure. |
| "We're losing to competitors" | #2 Own a Clear Position + #4 First Principles Differentiation | Write your "only we ___" statement. If you can't, repositioning is the priority. |
| "Marketing isn't converting" | #5 Simple Truth Told Simply + #15 Easy Path | Audit your homepage: does the headline pass the 5-second test? Rewrite with a customer outcome, not a feature. |
| "We don't know what to do next" | #13 Long-term Compounding Focus + #12 Mental Models Stack | List every marketing activity. Circle the 2 that compounded last quarter. Kill the rest. |
| "Should we try [tactic]?" | #8 Test, Then Scale + #11 Inversion | Run a 2-week test with a budget cap. Define what "failed" looks like before you start. |
| "How do we grow faster?" | #3 Build Moats + #9 Permission Flywheel | Map your retention: what keeps customers coming back? Invest there before acquiring new ones. |
| "Our message doesn't resonate" | #1 Customer Truth + #5 Simple Truth | Interview 3 current customers. Use their exact words in your next headline. |

---

## Per-Principle Action Templates

When a principle applies, use these fill-in-the-blank artifacts:

### Principle #2: Own a Clear Position
**Statement template:**
> "We are the only [category] for [specific customer] who [specific situation]. Unlike [alternative], we [key differentiator]."

**48-hour action:** Write this sentence. Share it with 3 prospects. If they nod immediately, it's working.

---

### Principle #4: First Principles Differentiation
**Assumption audit:**
> "Everyone in our industry assumes [X]. What if that assumption is wrong? If we removed it, we'd instead [Y]."

**48-hour action:** Name one assumption your industry makes. Write one offer that breaks it.

---

### Principle #8: Test, Then Scale
**Experiment brief:**
> "We'll test [specific tactic] with [budget/time cap]. We'll call it a success if [metric]. We'll kill it if [metric]. Decision date: [date]."

**48-hour action:** Fill in this brief for your next marketing idea before spending a dollar.

---

### Principle #11: Inversion
**Inversion worksheet:**
> "Assume this campaign/strategy fails completely. Why did it fail? [List 3 reasons]. Which of these can we prevent before we launch? [Preventions]."

**48-hour action:** Run this on your current biggest marketing bet.

---

## How to Apply (Full Analysis Mode)

For any marketing problem, follow this structure:

### 1. Situation (from context intake)
What's the business, stage, and specific problem?

### 2. Decision Engine Match
Which problem type does this map to? Which 1-3 principles apply?

### 3. Timeless Insight
What would the masters say about this specific problem?

### 4. Tailored Action Plan
2-3 specific actions, each with a named 48-hour first step.

### 5. ⚠️ Inversion Critique (REQUIRED)
> **"What would make this fail?"**
List 2-3 specific failure modes. Then name the prevention for each.

### 6. Metrics for Success
How will we know this worked? What do we measure?

---

## Iteration Protocol

After delivering recommendations:
1. Ask: "Does this match your actual situation, or did I miss something?"
2. If the user wants to go deeper on any principle, apply the full per-principle template
3. If the 48-hour action feels too big, break it into a 2-hour experiment instead
4. Track which principles the user returns to — that's their real strategic gap

---

## What Not to Do

❌ Output advice before completing the 3-question context intake
❌ Apply a principle without naming a specific action tied to it
❌ Skip the Inversion Critique section
❌ Recommend tactics without naming a 48-hour first step
❌ Give strategic frameworks when the user needs a decision

---

*Skill by Brian Wagner | AI Marketing Architect | brianrwagner.com*
```

## File: `meeting-prep/SKILL-OC.md`
```markdown
---
name: meeting-prep-cc
description: Generate a pre-meeting prep brief in Claude Code. Researches participants, pulls vault context, builds agenda, surfaces sharp questions. Use when user says "prep for this meeting," "I have a call with," "meeting tomorrow with," or "prep brief for [name/company]."
---

**Platform:** OpenClaw (token-optimized)

## Required Inputs

- Participant name(s) and company
- Meeting type (WRS / Sales / Strategy / Partnership / Interview / Other)
- Meeting time/date
- Optional: prior notes, last meeting summary

If meeting type missing, ask before proceeding.

## Workflow

**Step 1 — Vault search:**
```bash
VAULT="${VAULT_PATH:-/root/obsidian-vault}"
grep -rl "$NAME\|$COMPANY" "$VAULT" --include="*.md" \
  -not -path "*/.git/*" -not -path "*/.obsidian/*" \
  | head -10 | while read f; do
    echo "--- ${f##$VAULT/} ---"
    grep -n "$NAME\|$COMPANY" "$f" | head -5
  done
```

**Step 2 — Prior meeting notes:**
```bash
find "$VAULT/bambf/meeting-prep" -name "*.md" 2>/dev/null \
  | xargs grep -l "$NAME\|$COMPANY" 2>/dev/null | sort -r | head -3
```

**Step 3 — Open commitments check:**
```bash
grep -rn "TODO\|action item\|follow up\|promised" "$VAULT" --include="*.md" -l \
  | xargs grep -l "$NAME\|$COMPANY" 2>/dev/null | head -5
```

## Output Format

```
# Meeting Prep: [Name] | [Date] [Time]

Meeting type: [type]
Their role: [role at company]
Relationship stage: [new / existing / lapsed]

---

WHY THIS MEETING MATTERS
[1-2 sentences on stakes + desired outcome]

3 PRIORITIES FOR THIS CALL
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

CONTEXT FROM VAULT
[Pulled notes, open items, prior commitments — or "No prior history found"]

QUESTIONS TO ASK
1. [Research-referencing question]
2–5. [Additional questions]

WATCH FOR
[Known objections, sensitivities, open loops]

DESIRED OUTCOME
[What success looks like in one sentence]

NEXT STEP TO PROPOSE
[Specific: "schedule X," "send Y," "agree on Z"]
```

**Then:** Save to `bambf/meeting-prep/YYYY-MM-DD-[lastname]-prep.md`

**Then:** Print 3-line summary:
```
WHO: [Name], [role] at [company]
WHY IT MATTERS: [1 sentence]
TOP QUESTION: [Sharpest question to ask]
```

## Reference Files
- `references/brief-template.md` — full format
- `references/meeting-types.md` — agenda by type
- `references/question-banks.md` — question sets

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `meeting-prep/SKILL.md`
```markdown
---
name: meeting-prep-cc
description: Generate a pre-meeting prep brief in Claude Code. Researches participants, pulls vault context, builds agenda, surfaces sharp questions. Use when user says "prep for this meeting," "I have a call with," "meeting tomorrow with," or "prep brief for [name/company]."
---

# Meeting Prep (Claude Code Edition)

Generate a meeting prep brief from your Obsidian vault. Researches participants, surfaces vault history, builds a prioritized agenda, and generates sharp questions. No autonomy — you run it, you get your brief.

---

## How to Use

Open Claude Code in your vault directory and say:

```
Run the Meeting Prep skill. Meeting with [name] from [company]. Type: [sales/WRS/strategy/partnership/interview]. Time: [date/time].
```

---

## INTAKE

Check that the user has provided:
- Participant name(s) and company
- Meeting type (WRS / Sales / Strategy / Partnership / Interview / Other)
- Meeting time/date
- Optional: prior notes, last meeting summary

If meeting type is missing, ask:
```
What type of meeting is this?
WRS client / Sales / Strategy / Partnership / Interview / Other
```

---

## ANALYZE

Run these steps in order. Capture all output before formatting the brief.

### Step 1 — Vault Search

```bash
VAULT="${VAULT_PATH:-/root/obsidian-vault}"
NAME="[PARTICIPANT_NAME]"
COMPANY="[COMPANY_NAME]"

echo "=== VAULT CONTEXT ==="
grep -rl "$NAME\|$COMPANY" "$VAULT" \
  --include="*.md" \
  -not -path "*/.git/*" \
  -not -path "*/.obsidian/*" \
  | head -10 | while read f; do
    echo "--- ${f##$VAULT/} ---"
    grep -n "$NAME\|$COMPANY" "$f" | head -5
  done
```

### Step 2 — Prior Meeting Notes

```bash
VAULT="${VAULT_PATH:-/root/obsidian-vault}"
find "$VAULT/bambf/meeting-prep" -name "*.md" 2>/dev/null \
  | xargs grep -l "$NAME\|$COMPANY" 2>/dev/null \
  | sort -r | head -3 | while read f; do
    echo "--- Prior brief: ${f##$VAULT/} ---"
    head -30 "$f"
  done
```

### Step 3 — Open Commitments Check

```bash
VAULT="${VAULT_PATH:-/root/obsidian-vault}"
grep -rn "TODO\|action item\|follow up\|promised" "$VAULT" \
  --include="*.md" \
  -l 2>/dev/null \
  | xargs grep -l "$NAME\|$COMPANY" 2>/dev/null \
  | head -5 | while read f; do
    echo "--- ${f##$VAULT/} ---"
    grep -n "TODO\|action item\|follow up\|promised" "$f" | grep -i "$NAME\|$COMPANY" | head -5
  done
```

---

## OUTPUT

Format the brief using this structure (see `references/brief-template.md`):

```
# Meeting Prep: [Name] | [Date] [Time]

Meeting type: [type]
Their role: [role at company]
Relationship stage: [new / existing / lapsed]

---

WHY THIS MEETING MATTERS
[1-2 sentences on stakes, objective, desired outcome]

3 PRIORITIES FOR THIS CALL
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

CONTEXT FROM VAULT
[Pulled notes, open items, prior commitments — or "No prior history found"]

QUESTIONS TO ASK
1. [Question referencing research]
2. [Question]
3. [Question]
4. [Question]
5. [Question]

WATCH FOR
[Known objections, sensitivities, open loops]

DESIRED OUTCOME
[What does success look like in one sentence?]

NEXT STEP TO PROPOSE
[Specific: "schedule X," "send Y," "agree on Z"]
```

**Then:** Save brief to `bambf/meeting-prep/YYYY-MM-DD-[lastname]-prep.md`

**Then:** Print 3-line summary:
```
WHO: [Name], [role] at [company]
WHY IT MATTERS: [1 sentence]
TOP QUESTION: [The single sharpest question to ask]
```

---

## Reference Files

- `references/brief-template.md` — full brief format
- `references/meeting-types.md` — agenda by meeting type
- `references/question-banks.md` — question sets by context

---

## Requirements

- Claude Code with bash tool access
- Vault with bambf/ structure
- No external APIs required
```

## File: `meeting-prep/references/brief-template.md`
```markdown
# Meeting Prep: [Name] | [Date] [Time]

**Meeting type:** [WRS / Sales / Strategy / Partnership / Interview]  
**Duration:** [time]  
**Their role:** [role at company]  
**Relationship stage:** [new / existing / lapsed]  

---

## Why This Meeting Matters
[1-2 sentences on stakes, objective, and desired outcome]

## 3 Priorities for This Call
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

## Context From Vault
[Pulled notes, open items, prior commitments — or "No prior history found"]

## What They Care About Right Now
[Recent signals: posts, news, company context, anything fresh]

## Questions to Ask
1. [Question — should reference specific research]
2. [Question]
3. [Question]
4. [Question]
5. [Question]
6. [Optional question]
7. [Optional question]

## Watch For / Potential Friction
[Known objections, sensitivities, open loops, or landmines]

## Desired Outcome
[What does a successful meeting look like in one sentence?]

## Next Step to Propose
[Specific and concrete: "schedule X," "send Y," "agree on Z"]
```

## File: `meeting-prep/references/meeting-types.md`
```markdown
# Meeting Types + Agenda Templates

---

## WRS Client Meeting
**Objective:** Relationship health + project status + next sprint alignment

**Agenda:**
1. Quick wins since last meeting (2 min)
2. Current project status (5 min)
3. Blockers / what they need from us (5 min)
4. Next sprint priorities (5 min)
5. Any scope or budget changes (3 min)

**Watch for:** Scope creep, satisfaction signals, renewal indicators, unspoken concerns
**Key question:** "What's one thing that would make your life easier right now?"

---

## Sales / Discovery Meeting
**Objective:** Understand their pain, qualify fit, move to next step

**Agenda:**
1. Context setting — why they reached out (2 min)
2. Current situation + pain (10 min)
3. What they've tried (5 min)
4. What good looks like (5 min)
5. Our fit / next step (5 min)

**Watch for:** Urgency signals, budget authority, timeline, who else is involved
**Key question:** "What made you want to have this conversation now vs. 6 months ago?"

---

## Strategy Session
**Objective:** Make a decision or align on direction

**Agenda:**
1. Situation brief (3 min)
2. Options on the table (10 min)
3. Tradeoffs + risks (5 min)
4. Decision / alignment (5 min)
5. Owners + timeline (2 min)

**Watch for:** Misaligned assumptions, hidden blockers, decisions being deferred
**Key question:** "What assumptions are we making that could be wrong?"

---

## Partnership / Intro Meeting
**Objective:** Establish mutual value, determine fit for collaboration

**Agenda:**
1. Their world — what they're building (5 min)
2. Our world — what we're building (5 min)
3. Overlap and potential (5 min)
4. Specific collaboration idea (5 min)
5. Next step if fit exists (5 min)

**Watch for:** Complementary audiences, clear non-compete, genuine energy vs. polite interest
**Key question:** "Where do you see your audience overlapping with ours?"

---

## Interview / Evaluation Meeting
**Objective:** Assess fit — culture, competence, motivation

**Agenda:**
1. Their background in their own words (5 min)
2. Deep dive on relevant experience (10 min)
3. How they handle X situation (10 min)
4. Their questions (5 min)
5. Next step (2 min)

**Watch for:** Ownership language, specificity, red flags (vague answers, blame, inconsistencies)
**Key question:** "Walk me through a time you had to [relevant challenge]."
```

## File: `meeting-prep/references/question-banks.md`
```markdown
# Question Banks by Category

Use at least 2 questions that reference specific participant context (their role, recent news, vault history).

---

## Discovery Questions (Sales / New Relationship)
- What made you want to have this conversation now vs. 6 months ago?
- What have you already tried? What worked, what didn't?
- Walk me through how this problem shows up in a typical week.
- Who else is affected by this? Who would notice if it was fixed?
- What would "solved" look like for you?
- What's the cost of doing nothing?
- Who else is involved in making this decision?

---

## Relationship / WRS Questions
- What's working well that we should double down on?
- What's one thing that would make your life easier right now?
- If you had to prioritize one thing for next quarter, what would it be?
- How are you feeling about the direction we're headed?
- Is there anything you've been hesitant to bring up?
- What does success look like for you 90 days from now?

---

## Strategy Questions
- What assumptions are we making that could be wrong?
- What's the reversible vs. irreversible version of this decision?
- Who would disagree with this direction and why?
- What would we regret not doing in 12 months?
- What's the cheapest way to test this before we commit?
- What's changed since we last talked about this?

---

## Partnership Questions
- What's working in your current partnerships?
- Where do you see your audience overlapping with ours?
- What would a successful collaboration look like 6 months from now?
- What's the one thing you'd need to feel confident about moving forward?
- What do your current partners get wrong that we could get right?

---

## Interview / Evaluation Questions
- Walk me through your background in your own words.
- Tell me about a time you [relevant situation] — what did you do?
- What's the hardest thing you've had to figure out in a role?
- What do you need from the people you work with to do your best work?
- What are you looking for in your next opportunity that you don't have now?
- What questions do you have for me?

---

## Closing / Next Step Questions
- Based on what we discussed, does this feel like a fit?
- What would you need to see to move forward?
- What's the right next step from your side?
- Is there anything that would get in the way of us working together?
- When should we follow up, and what should that look like?

---

## Context-Specific Starters (Fill in with research)
- "I noticed you recently [posted about / published / announced] — what's driving that focus right now?"
- "Last time we spoke, you mentioned [open item]. Where does that stand?"
- "Your company just [news item]. How is that affecting [relevant area]?"
- "You've been in [role] for [tenure]. What's shifted in how you approach [topic] over that time?"
```

## File: `newsletter-creation-curation/PLAYBOOK.md`
```markdown
---
name: newsletter-creation-curation
description: Industry-specific newsletter creation with cadence recommendations and automation workflows
metadata: {"clawdbot":{"emoji":"📧","homepage":"https://github.com/shashwatgtm","always":true}}
---
## **🎯 Multi-Dimensional Navigator**

**Newsletters serve different purposes depending on your context. Find your path:**

### **STEP 1: What's Your Goal?**

Your primary goal determines everything about your newsletter strategy:

```
→ LEAD GENERATION - Generate inbound leads for sales team
→ THOUGHT LEADERSHIP - Build authority in your category
→ PERSONAL BRAND - Build your individual reputation
→ CATEGORY OWNERSHIP - Own the conversation in your space
```

### **STEP 2: What's Your Industry Vertical?**

Your industry determines:
- Content topics and angle
- Competitive positioning
- Tone and risk tolerance
- What's considered "valuable content"

```
→ Sales Tech - Tactical sales tips, conversation intelligence insights
→ HR Tech - People operations, employee engagement, compliance
→ Fintech - Financial regulations, payment trends, compliance updates
→ Operations Tech - Retail execution, supply chain, distribution
```

### **STEP 3: What's Your Company Stage?**

Your stage determines:
- Newsletter goals (lead gen vs thought leadership)
- Resources available (time, budget)
- Publishing frequency
- Content depth

```
→ Series A ($1M-10M ARR) - Lead gen focus, founder-led
→ Series B ($10M-50M ARR) - Thought leadership, team-led
→ Series C+ ($50M+ ARR) - Category ownership, dedicated team
```

### **STEP 4: Are You Founder or Employee?**

Your role determines:
- Editorial autonomy
- Approval workflows
- Personal vs company brand
- What you can/cannot say

```
→ Founder - Full autonomy, personal = company brand
→ VP/Director - Partial autonomy, manager approval
→ PMM/Content Lead - Team collaboration, brand guidelines
→ Employee (Non-Leadership) - Significant constraints
```

### **STEP 5: What's Your Primary Market?**

Your geography determines:
- Publishing times (IST vs EST)
- Content examples (Indian vs US companies)
- Distribution channels (WhatsApp vs LinkedIn)

```
→ India-first - IST times, local examples, price-conscious
→ US-first - EST/PST times, US examples, premium positioning
```

---

## **Quick Navigation by Common Scenarios**

**Most Common Use Cases:**

1. **"I'm a Sales Tech founder, want to generate leads via newsletter"**
   → Go to: **Section A1** (Sales Tech, Series A, Lead Gen Focus)

2. **"I'm VP Marketing at Series B HR Tech, want thought leadership newsletter"**
   → Go to: **Section B2** (HR Tech, Series B, Thought Leadership)

3. **"I'm at Series C fintech, want to own the category conversation"**
   → Go to: **Section C3** (Fintech, Series C+, Category Ownership)

4. **"I'm PMM at ops tech, my VP wants me to start a newsletter"**
   → Go to: **Section D2** (Operations Tech, Employee-Led, Approval Workflows)

---

# 📊 SECTION A: SALES TECH NEWSLETTERS

**When To Use This Section:**
- Your product: Sales engagement, conversation intelligence, sales enablement
- Your audience: Sales leaders, CROs, SDR managers, AEs
- Your angle: Tactical sales tips, revenue growth, deal execution
- Tone: Aggressive, data-driven, ROI-focused

---

## **A1: Sales Tech @ Series A (Founder-Led Lead Generation)**

### **Your Reality Check:**

```
COMPANY PROFILE:
- Size: $1M-10M ARR, 10-100 employees
- Stage: Series A, need inbound leads
- You: Founder (or early marketing hire)
- Newsletter goal: Generate 10-20 SQLs per month
- Time available: 3-5 hours/week
- Budget: $0-200/month
```

### **The Sales Tech Newsletter Formula:**

**Why Sales Leaders Read Newsletters:**

```
SALES LEADERS DON'T READ:
❌ Generic sales tips ("7 ways to close more deals")
❌ Long-form essays (no time)
❌ Theory without tactics
❌ Anything that doesn't help THIS QUARTER

SALES LEADERS READ:
✅ Data-driven insights ("Gong analyzed 1M calls, here's what top reps do")
✅ Tactical playbooks (copy-paste into next call)
✅ Competitive intelligence (what competitors are doing)
✅ Quick wins (implement in <30 minutes)
```

### **Series A Sales Tech Newsletter Strategy:**

**GOAL: 10-20 SQLs per month from newsletter**

**Week-by-Week Startup Plan:**

```
WEEK 1: POSITIONING & SETUP (4 hours)

Day 1-2: Choose Your Angle (2 hours)

SALES TECH NEWSLETTER ANGLES:
Option 1: "Conversation Intelligence Insights"
- Example: Analyze sales calls, share patterns
- Audience: Sales leaders at B2B SaaS (50-500 employees)
- Frequency: Weekly
- Differentiator: Data-driven (use your product's data)

Option 2: "SMB Sales Playbook"
- Example: Tactical plays for small sales teams
- Audience: Founders, sales managers at startups
- Frequency: Weekly
- Differentiator: Practical, not theoretical

Option 3: "AI Sales Coaching"
- Example: How AI changes sales coaching
- Audience: Sales enablement leaders
- Frequency: Bi-weekly
- Differentiator: Future-focused, contrarian takes

YOUR DECISION:
Pick ONE angle. Stick to it for 12 weeks minimum.
Example: "AI Sales Coaching for SMB Teams"

Day 3: Setup Publishing (2 hours)

SALES TECH PUBLISHING OPTIONS:

FREE OPTIONS:
□ LinkedIn Newsletter (RECOMMENDED for Sales Tech)
  - Why: Your audience is already on LinkedIn
  - Setup: 15 minutes
  - Reach: Notifies your connections
  - Downside: LinkedIn owns the list

□ Substack (RECOMMENDED if building owned list)
  - Why: Own your subscribers, email delivery
  - Setup: 30 minutes
  - Cost: Free (5% fee on paid subscriptions)
  - Downside: Cold start (need to drive traffic)

□ Medium (NOT RECOMMENDED)
  - Why: Audience is too broad, not B2B sales-focused
  - Skip this for Sales Tech

HYBRID APPROACH (BEST):
- Publish on Substack (own the list)
- Cross-post to LinkedIn (distribution)
- Repurpose on Twitter threads (amplification)

SETUP CHECKLIST:
□ Substack account created
□ Newsletter name: [Your Angle] Newsletter
  Example: "The AI Sales Coach" or "SMB Sales Playbook"
□ About section: 2-3 sentences on who it's for
□ First post published: "Issue #0: What to expect"
```

**WEEK 2: WRITE & PUBLISH ISSUE #1 (4 hours)**

```
Monday: Research & Outline (1 hour)

SALES TECH CONTENT SOURCES:

PRIMARY (Use These):
□ Gong blog (conversation intelligence leader)
□ Sales Hacker (community content)
□ r/sales on Reddit (real sales rep pain points)
□ Your own sales calls (if you have product data)
□ Customer interviews (ask: "What's your biggest sales challenge?")

SECONDARY (Reference):
□ Pavilion community (CRO insights)
□ SaaStr blog (B2B SaaS sales)
□ LinkedIn posts from sales leaders (Jason Lemkin, Jacco van der Kooij)

WHAT TO LOOK FOR:
- Data-driven insights (numbers, stats, research)
- Contrarian takes (what everyone gets wrong)
- Tactical playbooks (step-by-step processes)

Tuesday-Wednesday: Write Issue #1 (2 hours)

SALES TECH NEWSLETTER STRUCTURE:

┌─────────────────────────────────────────┐
│ SUBJECT LINE (Critical for Sales Tech) │
├─────────────────────────────────────────┤
│ ❌ BAD: "Issue #1: Sales Tips"          │
│ ✅ GOOD: "Why 73% of SDRs fail [data]"  │
│ ✅ GOOD: "The 2-minute discovery hack"  │
│ ✅ GOOD: "Gong is wrong about cold calls"│
└─────────────────────────────────────────┘

FORMAT (600-900 words):

**OPENING HOOK (50-100 words)**
Start with: Data point, contrarian take, or bold claim
Example:
"Gong analyzed 1 million sales calls and found the average 
discovery call is 38 minutes. But the top 10% of reps? 
They keep it under 25 minutes. Here's why..."

**THE INSIGHT (200-300 words)**
Explain the data or framework
Use: Numbers, quotes, examples
Avoid: Fluff, generic advice

**THE TACTICAL PLAYBOOK (250-400 words)**
Step-by-step: How to apply this
Format:
1. Preparation: What to do before
2. Execution: How to do it
3. Follow-up: What happens after

**THE CALL TO ACTION (50-100 words)**
Next step for reader:
- Try this technique
- Reply with your experience
- Book a demo (if relevant - sparingly)

Thursday: Edit & Polish (30 minutes)

SALES TECH EDITING CHECKLIST:
□ Cut 30% of words (sales leaders are busy)
□ Check: Every paragraph has data or tactics
□ Remove: Theory, fluff, obvious advice
□ Add: Specific numbers, examples, names
□ Verify: All claims have sources

Friday: Publish (30 minutes)

TIMING (CRITICAL FOR SALES TECH):
❌ Monday morning (busy, planning week)
❌ Friday afternoon (checking out for weekend)
✅ Tuesday 9 AM EST (best open rates for sales)
✅ Wednesday 10 AM EST (second best)
✅ Thursday 9 AM EST (third best)

If India-focused:
✅ Tuesday 9 AM IST
✅ Wednesday 2 PM IST (after lunch)

POST-PUBLISH AMPLIFICATION:
□ Share on LinkedIn (tag relevant people)
□ Post Twitter thread (key points)
□ Share in Sales Hacker Slack
□ Email to 10 sales leaders: "Would love your take on this"
```

**WEEKS 3-12: WEEKLY RHYTHM (3-4 hours/week)**

```
MONDAY (1 hour):
□ Review last week's open rate, clicks
□ Brainstorm this week's topic
□ Collect 2-3 data sources

TUESDAY-WEDNESDAY (2 hours):
□ Write 600-900 words
□ Edit ruthlessly
□ Get feedback from sales team (if you have one)

THURSDAY (30 minutes):
□ Final edit
□ Create subject line (test 3 options, pick best)
□ Schedule for Friday 9 AM EST

FRIDAY (30 minutes):
□ Newsletter goes out automatically
□ Amplify on social media
□ Respond to replies (engagement signal)
```

### **Sales Tech Newsletter: Content Ideas (First 12 Issues)**

**Tactical > Theory**

```
ISSUE 1: "Why 73% of SDRs fail [Gong data analysis]"
ISSUE 2: "The 2-minute discovery question framework"
ISSUE 3: "Gong is wrong about cold calls [contrarian take]"
ISSUE 4: "How top AEs use silence in demos [behavioral science]"
ISSUE 5: "The 'negative close' technique [with script]"
ISSUE 6: "Why your CRM is killing your close rate [data]"
ISSUE 7: "The 3 questions top closers always ask [Chorus analysis]"
ISSUE 8: "How to compete against Gong/Outreach [battle card]"
ISSUE 9: "The follow-up cadence that actually works [A/B test results]"
ISSUE 10: "Why most sales coaching fails [research + fix]"
ISSUE 11: "The pricing objection framework [copy-paste]"
ISSUE 12: "How AI will change sales in 2026 [predictions]"

PATTERN:
- 50% data-driven insights
- 30% tactical playbooks
- 20% contrarian/provocative takes
```

### **Measuring Success (Sales Tech Newsletter KPIs)**

```
MONTH 1-3 (Building):
- Goal: 100-300 subscribers
- Opens: 30-40% (industry average)
- Clicks: 3-5%
- SQLs: 2-5 per month
- Quality over quantity

MONTH 4-6 (Growing):
- Goal: 300-800 subscribers
- Opens: 35-45% (improving)
- Clicks: 5-8%
- SQLs: 5-10 per month
- Start seeing inbound "I read your newsletter"

MONTH 7-12 (Scaling):
- Goal: 800-2,000 subscribers
- Opens: 40-50% (well-established)
- Clicks: 8-12%
- SQLs: 10-20 per month
- Newsletter = #1 inbound lead source

SALES TECH SPECIFIC:
- Track: "Mentioned newsletter" in CRM (lead source)
- Track: Demo requests that cite specific issue
- Track: LinkedIn engagement (comments, shares)
```

### **Sales Tech Newsletter: Growth Tactics**

**FREE GROWTH (Series A Budget)**

```
WEEK 1-4: Foundation
□ Every LinkedIn post ends with: "Full analysis in my newsletter [link]"
□ Comment on sales leader posts: "I wrote about this in my newsletter"
□ Join Sales Hacker Slack, share newsletter (not spammy)

WEEK 5-8: Partnerships
□ Guest post on Sales Hacker: CTA to newsletter
□ Interview 3 sales leaders: "Subscribe to get more interviews"
□ Cross-promote with other sales newsletters (smaller ones will say yes)

WEEK 9-12: Amplification
□ LinkedIn polls: Drive traffic to newsletter for "full results"
□ Twitter threads: Newsletter issues → threads (expand reach)
□ Podcast guesting: "I cover this in my newsletter"

AGGRESSIVE TACTICS (Sales Tech Appropriate):
✅ Call out competitors in newsletter ("Gong vs us")
✅ Contrarian takes ("Why sales playbooks fail")
✅ Provocative subject lines ("Your CRM is lying to you")

AVOID (Even for Sales Tech):
❌ Spamming LinkedIn DMs
❌ Buying email lists (deliverability death)
❌ Fake urgency ("Last chance to subscribe!")
```

---

## **A2: Sales Tech @ Series B (Thought Leadership Team Effort)**

### **Your Reality Check:**

```
COMPANY PROFILE:
- Size: $10M-40M ARR, 150-500 employees
- Stage: Series B, scaling marketing
- You: VP Marketing or Content Lead
- Team: 1-2 content writers + designer
- Newsletter goal: Thought leadership + lead gen
- Budget: $2K-8K/month for content
- Time: Team effort, 10-15 hours/week total
```

### **Why Series B Newsletter Strategy is Different:**

```
SERIES A NEWSLETTER:
- Founder-led, scrappy
- Goal: Lead gen (10-20 SQLs/month)
- Frequency: Weekly
- Content: Tactical, founder voice
- Budget: $0-200/month

SERIES B NEWSLETTER:
- Team-led, professional
- Goal: Thought leadership + pipeline
- Frequency: Weekly or bi-weekly
- Content: Data-driven, brand voice
- Budget: $2K-8K/month

NEW CHALLENGES:
- Multiple stakeholders (CEO, Sales, Product)
- Brand voice vs founder voice
- Higher quality bar (professional design)
- Scaling from 800 → 5,000+ subscribers
- Measuring pipeline impact (not just leads)
```

### **Series B Sales Tech Newsletter: Enhanced Production**

```
TEAM STRUCTURE:

ROLES:
□ Content Lead (You): Strategy, editing, stakeholder mgmt
□ Writer: Research, drafting (10 hours/week)
□ Designer: Graphics, charts (3 hours/week)
□ Founder/CEO: Guest contributor (1 hour/month)

TOOLS ($2K-5K/month total):
□ Substack Pro or ConvertKit ($300-500/month)
  → Advanced analytics, segmentation, A/B testing
  
□ Graphic design ($500-1K/month):
  Option 1: Hire part-time designer
  Option 2: Canva Pro + templates ($45/month)
  Option 3: Fiverr designer ($100-200 per issue)
  
□ Research tools ($200-500/month):
  → LinkedIn Sales Navigator (audience research)
  → Gong/Chorus access (conversation data)
  → Industry reports (Gartner, Pavilion)
  
□ Content tools ($100-200/month):
  → Grammarly Premium
  → Hemingway Editor
  → Headline analyzer

WEEKLY WORKFLOW:

MONDAY (3 hours):
- Content Lead: Review last week's metrics
- Team sync: This week's topic, angle
- Assign: Writer starts research

TUESDAY (4 hours):
- Writer: First draft (800-1,200 words - longer than Series A)
- Designer: Concept graphics

WEDNESDAY (4 hours):
- Content Lead: Edit, provide feedback
- Writer: Second draft
- Designer: Final graphics

THURSDAY (3 hours):
- Stakeholder review: CEO/Sales leader feedback
- Writer: Incorporate feedback
- Content Lead: Final approval

FRIDAY (1 hour):
- Schedule send (9 AM EST Tuesday)
- Pre-schedule social amplification
- Prepare LinkedIn post for Monday
```

### **Series B Content Strategy: Data-Driven Thought Leadership**

```
DIFFERENCE FROM SERIES A:

SERIES A CONTENT:
"Here's a tactical tip I learned from my sales calls"

SERIES B CONTENT:
"We analyzed 10,000 sales calls across 200 companies. 
Here's what we learned about discovery calls in 2026."

SERIES B ADVANTAGE:
✅ Access to product data (you have 100s of customers)
✅ Engineering resources (build custom analysis)
✅ Budget for commissioned research
✅ Customer interviews at scale
✅ Sales team insights

CONTENT PILLARS (Series B Sales Tech):

PILLAR 1: ORIGINAL RESEARCH (40% of issues)
Example: "The State of SMB Sales 2026"
- Analyze your product data
- Survey 200 sales leaders
- Partner with Pavilion for distribution
- Turn into: Report + Newsletter series + Webinar

PILLAR 2: CUSTOMER INSIGHTS (30%)
Example: "How [YC Company] Scaled from $1M to $10M ARR"
- Interview customer
- Extract tactical playbook
- Position your product subtly
- CTA: "Want similar results? Let's talk"

PILLAR 3: INDUSTRY ANALYSIS (20%)
Example: "Why Gong's Series D Changes the Sales Tech Landscape"
- React to industry news
- Position your company
- Forward-looking (where is category going?)

PILLAR 4: FOUNDER/EXECUTIVE VOICE (10%)
Example: "Our CEO on Building Sales Culture at Scale"
- Monthly guest post from leadership
- Humanizes brand
- Recruiting signal (talented people want to work here)
```

### **Series B Newsletter: Advanced Growth Tactics**

```
PAID GROWTH (Now You Have Budget):

TACTIC 1: SPONSORSHIPS ($1K-3K/month)
- Sponsor Sales Hacker newsletter
- Sponsor Pavilion community content
- Sponsor Revenue Collective events
→ Each drives 50-200 subscribers
→ ROI: $5-15 per subscriber (acceptable)

TACTIC 2: PAID SOCIAL ($500-1K/month)
- LinkedIn ads: "Download our sales playbook"
- Gate with email: Auto-subscribe to newsletter
- Target: Sales leaders at $5M-50M ARR companies
→ Cost: $3-8 per subscriber

TACTIC 3: WEBINAR FUNNEL ($1K-2K/month)
- Monthly webinar on sales topic
- Registrants = Newsletter subscribers
- Partner with sales tools (Pavilion, Salesloft, Outreach)
→ 100-300 new subscribers per webinar

ORGANIC GROWTH (Still Essential):

TACTIC 4: LINKEDIN CONTENT MACHINE
- 3-5 posts per week
- Each ends with newsletter CTA
- Founder + VP Marketing + Sales leaders all posting
→ Compound effect: 5 people × 3 posts = 15 touchpoints/week

TACTIC 5: PODCAST CIRCUIT
- Guest on 2 sales podcasts per month
- Mention newsletter in intro/outro
- Provide "bonus content in newsletter"
→ Each podcast: 50-150 subscribers

TACTIC 6: SALES TEAM AMPLIFICATION
- Every SDR/AE signature: Newsletter link
- Sales team shares on LinkedIn
- Customer asks question? "I covered that in newsletter issue #47"
→ Sales team = distribution arm
```

---

## **A3: Sales Tech @ Series C+ (Category Ownership via Newsletter)**

### **Your Reality Check:**

```
COMPANY PROFILE:
- Size: $50M+ ARR, 500+ employees
- Stage: Series C/D, preparing IPO or market leader
- You: Director of Content/Thought Leadership
- Team: 3-5 FTE (writers, designers, analysts)
- Newsletter: Flagship thought leadership
- Budget: $15K-40K/month for content
- Subscribers: 10,000-50,000+
```

### **Series C+ Newsletter = Category Ownership**

```
SERIES A/B GOAL:
- Generate leads
- Build thought leadership

SERIES C+ GOAL:
- OWN the conversation in sales tech
- Be THE source for sales insights
- Influence industry (Gartner, analysts, media)
- Recruiting tool (top talent reads your newsletter)

EXAMPLES:
- Gong Labs (conversation intelligence category leader)
- SaaStr (B2B SaaS category leader)
- First Round Review (startup category leader)

YOUR NEWSLETTER BECOMES:
- Category-defining
- Cited by media
- Referenced in board meetings (not just your company)
- Required reading for sales leaders
```

### **Series C+ Production: Media Company Level**

```
TEAM STRUCTURE:

EDITORIAL TEAM:
□ Director of Content (You): Strategy, stakeholder management
□ Managing Editor: Quality, process, timelines
□ 2-3 Staff Writers: Dedicated to newsletter
□ Data Analyst: Custom research, data visualization
□ Designer: Brand-quality graphics
□ Video Producer: Multimedia content (future)

TOOLS & SERVICES ($15K-40K/month):

TIER 1: PUBLISHING INFRASTRUCTURE ($2K-5K/month)
□ ConvertKit/Klaviyo Enterprise ($500-1K/month)
□ Custom website/design ($200-500/month hosting + maintenance)
□ Email deliverability service ($100-200/month)
□ A/B testing tools ($100-200/month)

TIER 2: RESEARCH & DATA ($5K-15K/month)
□ Commissioned research ($3K-10K per report)
□ Gartner/Forrester subscriptions ($3K-5K/month)
□ Data visualization tools (Tableau, $70/user/month)
□ Survey tools (Qualtrics, $200-500/month)

TIER 3: CONTENT PRODUCTION ($5K-15K/month)
□ 2-3 staff writers ($8K-12K/month total comp)
□ Designer ($3K-5K/month)
□ Editor ($4K-6K/month)
□ Freelance experts ($500-1K/month for guest posts)

TIER 4: DISTRIBUTION ($3K-10K/month)
□ Paid social ($2K-5K/month)
□ Sponsorships ($1K-3K/month)
□ PR agency (if needed, $5K-10K/month)
```

### **Series C+ Content: Industry-Defining Research**

```
QUARTERLY FLAGSHIP REPORTS:

Q1: "THE STATE OF SMB SALES 2026"
- Survey: 1,000+ sales leaders
- Data: Analyze 10M+ sales calls from your product
- Partners: Pavilion, Sales Hacker, Gartner (validate findings)
- Format:
  * 40-page PDF report
  * 4-week newsletter series
  * Webinar series
  * Media tour (TechCrunch, Forbes, etc.)
  
Production cost: $20K-40K
Impact:
- 5,000+ new subscribers
- 500+ SQLs from report
- Media coverage (industry authority signal)
- Sales enablement (differentiation)

Q2: "AI'S IMPACT ON SALES PRODUCTIVITY [2026 RESEARCH]"
- Partner with university (academic credibility)
- Control group study
- Published in journal + newsletter
- Speaking opportunities (conferences)

Q3: "THE SALES TECH LANDSCAPE [COMPETITIVE ANALYSIS]"
- Map 200+ sales tech companies
- Funding, features, market positioning
- This is YOUR "Gartner Magic Quadrant"
- Cited by: Investors, media, customers

Q4: "SALES COMPENSATION BENCHMARKS 2026"
- Survey 500+ sales leaders on comp plans
- Data on OTE, accelerators, commissions
- High-value (people will pay for this data)
- Newsletter exclusive preview
```

### **Series C+ Distribution: Media-Level Amplification**

```
OWNED CHANNELS:
□ Newsletter (primary)
□ Blog (SEO, long-form)
□ LinkedIn (3-5 posts/day from team)
□ Twitter/X (5-10 posts/day)
□ YouTube (video summaries)
□ Podcast (weekly, guests)

EARNED CHANNELS:
□ Media coverage (TechCrunch, Forbes, WSJ)
□ Podcast guest circuit (top sales podcasts)
□ Conference speaking (SaaStr, Pavilion, G2 Reach)
□ Academic citations (if partnered with universities)

PAID CHANNELS:
□ Sponsored content in top newsletters ($5K-15K per placement)
□ LinkedIn ads ($5K-10K/month)
□ Conference sponsorships ($10K-50K per event)
□ Trade publication ads (if needed)

PARTNER CHANNELS:
□ Integration partners (Salesforce, HubSpot, Outreach)
□ Community partners (Pavilion, Revenue Collective)
□ Analyst firms (Gartner, Forrester)
□ Academic partners (universities, research labs)
```

---

# 📊 SECTION B: HR TECH NEWSLETTERS

**When To Use This Section:**
- Your product: HRIS, employee engagement, performance management, recruiting
- Your audience: HR leaders, CHROs, People Ops, Talent Acquisition
- Your angle: Employee experience, people analytics, compliance, culture
- Tone: Professional, empathetic, research-backed (NEVER aggressive like Sales Tech)

---

## **B1: HR Tech @ Series A (Founder-Led Thought Leadership)**

### **Your Reality Check:**

```
COMPANY PROFILE:
- Size: $2M-8M ARR, 20-80 employees
- Stage: Series A
- You: Founder (often ex-CHRO or People Ops background)
- Newsletter goal: Build trust + credibility (lead gen secondary)
- Time: 4-6 hours/week
- Budget: $0-300/month
```

### **Why HR Tech Newsletters Are FUNDAMENTALLY DIFFERENT:**

```
SALES TECH NEWSLETTER:
✅ Aggressive, contrarian takes
✅ "Gong is wrong about cold calls"
✅ Data-driven, ROI-focused
✅ Fast decisions (sales leaders act quickly)

HR TECH NEWSLETTER:
❌ NEVER aggressive or confrontational
❌ NEVER "Competitor X is wrong"
✅ Professional, empathetic, research-backed
✅ Slow decisions (HR is risk-averse, committee-driven)

WHY THE DIFFERENCE:
- HR community is small, tight-knit (everyone knows everyone)
- HR leaders value relationships over aggressive positioning
- HR buyers are risk-averse (people data = sensitive)
- Attacking competitors = unprofessional (damages your reputation)
```

### **Series A HR Tech Newsletter Strategy**

**GOAL: Build trust and credibility, generate 5-15 SQLs/month**

```
WEEK 1: POSITIONING (4 hours)

CHOOSE YOUR ANGLE:

Option 1: "PEOPLE ANALYTICS & INSIGHTS"
- Example: "Data-Driven HR Decisions"
- Audience: CHROs at 200-1000 employee companies
- Differentiator: Research-backed, evidence-based

Option 2: "EMPLOYEE EXPERIENCE BEST PRACTICES"
- Example: "The EX Playbook"
- Audience: People Ops leaders at startups/scaleups
- Differentiator: Practical, actionable, empathetic

Option 3: "HR COMPLIANCE & REGULATIONS"
- Example: "The Compliant CHRO"
- Audience: HR leaders navigating regulations
- Differentiator: Expert analysis, updates

PICK BASED ON YOUR PRODUCT:
- Engagement platform → Employee Experience
- Performance management → People Analytics
- HRIS → Compliance & Best Practices

SETUP (LinkedIn Newsletter HIGHLY RECOMMENDED for HR Tech):

WHY LINKEDIN FOR HR TECH:
✅ HR leaders very active on LinkedIn (not Twitter/Reddit)
✅ SHRM, Josh Bersin, lots of HR thought leaders on LinkedIn
✅ Professional network = HR's comfort zone
✅ Built-in distribution

SETUP:
□ Create LinkedIn Newsletter
□ Name: "[Angle] for HR Leaders"
  Example: "The People Analytics Weekly"
□ Post frequency: Bi-weekly (HR leaders prefer quality > quantity)
□ First issue: "Issue #0: Why I'm starting this"
```

**WEEKS 2-12: BI-WEEKLY RHYTHM (4-6 hours per issue)**

```
WEEK 1 (Publish Week):

MONDAY-TUESDAY (3 hours): Research & Draft

HR TECH CONTENT SOURCES:

PRIMARY:
□ SHRM research reports (authoritative)
□ Josh Bersin research (HR thought leader)
□ Lattice blog, Culture Amp blog (category leaders)
□ Harvard Business Review (HBR) - HR articles
□ Gartner HR research (if accessible)

SECONDARY:
□ r/humanresources (real HR pain points)
□ People Managing People newsletter
□ HR Tech Conference content
□ Academic journals (if employee engagement/performance topic)

WHAT TO LOOK FOR:
- Research-backed insights (studies, surveys, data)
- Employee experience stories (case studies)
- Compliance updates (GDPR, labor laws, etc.)
- People analytics frameworks

WEDNESDAY (2 hours): Write & Edit

HR TECH NEWSLETTER STRUCTURE (800-1,200 words):

┌──────────────────────────────────────────┐
│ SUBJECT LINE (Professional, not clickbait)│
├──────────────────────────────────────────┤
│ ❌ BAD: "Your HR strategy is WRONG"      │
│ ✅ GOOD: "3 employee engagement insights" │
│ ✅ GOOD: "New GDPR requirements for HR"   │
│ ✅ GOOD: "How top CHROs measure culture"  │
└──────────────────────────────────────────┘

**OPENING (100-150 words)**
Start with: Research finding, employee story, or compliance update
Example:
"Culture Amp's 2026 benchmark report analyzed 500,000 
employee surveys across 2,000 companies. They found that 
manager effectiveness is 3× more predictive of retention 
than compensation. Here's what that means for your team..."

**THE RESEARCH/FRAMEWORK (300-400 words)**
Present the data or framework
Use: Studies, benchmarks, expert quotes
Tone: Professional, evidence-based, helpful
Avoid: Aggressive, sales-y, attacking competitors

**PRACTICAL APPLICATION (300-400 words)**
How HR leaders can apply this
Format:
- For small teams (50-200 employees): [Advice]
- For mid-market (200-1000 employees): [Advice]
- For enterprise (1000+): [Advice]

**RESOURCES & NEXT STEPS (100-150 words)**
- Link to: Full research report
- Suggest: Further reading (SHRM, HBR)
- Soft CTA: "Thoughts? I'd love to hear your experience"
- Very soft: "If you're navigating this, happy to chat [calendar link]"

THURSDAY (1 hour): Edit & Finalize

HR TECH EDITING CHECKLIST:
□ Tone check: Professional, empathetic (not aggressive)
□ Remove: Any criticism of competitors
□ Verify: All research properly cited
□ Add: Disclaimers if needed ("I'm not a lawyer, consult legal")
□ Check: Inclusive language (they/them, not he/she)

FRIDAY (Publish)

TIMING FOR HR TECH:
✅ Tuesday 9 AM EST (best for HR leaders)
✅ Thursday 10 AM EST (second best)
❌ Monday (too busy)
❌ Friday (checking out for weekend)

POST-PUBLISH:
□ Share on LinkedIn (your profile + company page)
□ Post in SHRM Connect community (if member)
□ Email to 5-10 CHROs: "Wrote about X, would love your perspective"
□ NO aggressive self-promotion
```

### **HR Tech Newsletter: Content Ideas (First 12 Issues)**

```
ISSUE 1: "The 2026 employee engagement benchmarks [Culture Amp data]"
ISSUE 2: "Why manager training fails (and what works instead)"
ISSUE 3: "New GDPR requirements every CHRO should know"
ISSUE 4: "The 4 questions top performers want answered in 1-on-1s"
ISSUE 5: "How 3 startups scaled culture from 50 to 500 employees"
ISSUE 6: "The people analytics frameworks CHROs actually use"
ISSUE 7: "What the research says about hybrid work policies [HBR review]"
ISSUE 8: "How to measure DEI progress (beyond vanity metrics)"
ISSUE 9: "The performance review alternatives that work [case studies]"
ISSUE 10: "Navigating layoffs with empathy [practical guide]"
ISSUE 11: "Employee retention in 2026: what the data shows"
ISSUE 12: "Building HR tech stack for 200-500 employee companies"

PATTERN:
- 60% research-backed insights
- 30% practical frameworks
- 10% compliance/regulation updates
- 0% aggressive competitive positioning
```

### **HR Tech Newsletter: Conservative Growth Tactics**

```
FREE GROWTH (Professional, Non-Aggressive):

WEEK 1-4: SHRM Community Participation
□ Join SHRM Connect
□ Answer HR questions (be helpful, not sales-y)
□ Signature line: "I write about [topic] at [newsletter link]"
□ Share newsletter when directly relevant to discussion

WEEK 5-8: LinkedIn Engagement Strategy
□ Comment thoughtfully on CHRO posts
□ Share HR research (not just your newsletter)
□ Build genuine relationships
□ Newsletter mention in profile: "I publish bi-weekly on [topic]"

WEEK 9-12: Webinars & Guest Content
□ Partner with SHRM local chapter (co-host webinar)
□ Guest post on People Managing People blog
□ Interview 3 CHROs in newsletter (they'll share with network)

WHAT NOT TO DO (Even Though Sales Tech Does It):
❌ Aggressive LinkedIn outreach
❌ Controversial/clickbait subject lines
❌ Calling out competitors
❌ "You're doing HR wrong" positioning
```

---

## **B2: HR Tech @ Series B (Team-Led Professional Content)**

### **Your Reality Check:**

```
COMPANY PROFILE:
- Size: $12M-40M ARR, 200-600 employees
- Stage: Series B
- You: Director of Content or Head of Marketing
- Team: 1 writer + designer
- Newsletter: Brand-building + thought leadership
- Budget: $3K-10K/month
- Goal: 3,000-8,000 subscribers, 10-25 SQLs/month
```

### **Series B HR Tech: Elevated Content Quality**

```
TEAM & TOOLS:

TEAM:
□ Content Director (You): Strategy, stakeholder management
□ HR Content Writer: Dedicated writer with HR background
□ Designer: Professional graphics (people photos, infographics)
□ Founder/CHRO: Monthly guest column

TOOLS ($3K-7K/month):
□ ConvertKit or ActiveCampaign ($200-400/month)
□ Graphic design: Part-time designer ($1K-2K/month)
□ Research subscriptions:
  - Josh Bersin Academy ($1K/month)
  - SHRM membership ($200/month)
  - HBR subscription ($20/month)
□ Photography: Stock photos (iStock, $30-100/month)
□ Survey tools: Typeform or SurveyMonkey ($50-100/month)

WEEKLY WORKFLOW (BI-WEEKLY PUBLISHING):

WEEK 1 (Prep Week):
- Monday: Topic selection, research phase
- Wednesday: Writer starts first draft
- Friday: Draft review, feedback

WEEK 2 (Publish Week):
- Monday: Final draft + design
- Tuesday: Stakeholder review (VP/CMO approval)
- Wednesday: Final edits
- Thursday: Publish at 9 AM EST

APPROVAL WORKFLOW (HR Tech Specific):
□ Writer completes draft
□ Content Director reviews (you)
□ Legal review if: Compliance topics, GDPR, labor laws
□ Executive review: Founder/CHRO for sensitive topics
□ Final approval: Content Director

WHY MORE APPROVAL IN HR TECH:
- People data = sensitive (can't make mistakes)
- Compliance risk (GDPR, EEOC, labor laws)
- Reputation risk (HR community is small)
```

### **Series B Content Strategy: Original Research**

```
QUARTERLY RESEARCH PROJECTS:

Q1: "THE STATE OF EMPLOYEE ENGAGEMENT 2026"
- Survey: 500 HR leaders
- Partner: SHRM local chapter (distribution)
- Format:
  * 25-page report
  * 3-week newsletter series
  * Webinar with findings
  
Cost: $5K-8K (survey tools, design, writer time)
Impact:
- 500-1,000 new subscribers
- 20-40 SQLs
- Industry credibility
- Media coverage (HR Dive, HRExecutive)

Q2: "PEOPLE ANALYTICS BENCHMARKS"
- Your product data: Anonymized benchmarks
- Customer interviews: 20 case studies
- Academic partner: Validate findings

Q3: "HYBRID WORK POLICIES [2026 RESEARCH]"
- Timely, relevant
- Multi-company case studies
- Expert commentary (industrial psychologists)

Q4: "HR TECH STACK REPORT"
- Survey: What tools do CHROs use?
- Integration insights
- Budget benchmarks by company size
```

---

## **B3: HR Tech @ Series C+ (Category-Defining Content)**

### **Your Reality Check:**

```
COMPANY PROFILE:
- Size: $50M+ ARR, 800+ employees
- Stage: Series C/D, category leader
- You: VP Content/Thought Leadership
- Team: 4-6 FTE content team
- Newsletter: Industry authority
- Budget: $20K-50K/month
- Subscribers: 15,000-60,000+
```

### **Series C+ HR Tech: Josh Bersin Academy-Level**

```
AMBITION:
Not just "a newsletter"
Goal: Be THE source for HR insights (like Josh Bersin Academy)

CONTENT STRATEGY:

FLAGSHIP RESEARCH (2-3 per year):
- $30K-60K per report
- Partner with: Universities, Gartner, Forrester
- Published in: Academic journals + your newsletter
- Impact: Cited in board meetings, media, Gartner reports

MEMBERSHIP MODEL:
- Free newsletter (15K+ subscribers)
- Premium membership ($199-499/year)
  * Exclusive research
  * Templates and frameworks
  * Private community access
  * Quarterly roundtables with CHROs

MEDIA PRESENCE:
- Regular contributor: Harvard Business Review, SHRM
- Conference speaking: SHRM Annual, Josh Bersin Conf
- Podcast: Weekly interviews with CHROs
- Book deal: "The Future of Work [2027]"

TEAM:
□ VP Content (You): Strategy, partnerships
□ Managing Editor: Quality, process
□ 2 Staff Writers: Dedicated to newsletter/research
□ Research Analyst: Data, surveys, benchmarks
□ Designer: Infographics, reports
□ Video Producer: Multimedia content
□ Community Manager: Member engagement
```

---

# 📊 SECTION C: FINTECH NEWSLETTERS

**When To Use This Section:**
- Your product: Payments, expense management, corporate cards, payroll
- Your audience: CFOs, Finance leaders, Controllers, FinOps
- Your angle: Financial regulations, payment trends, compliance, efficiency
- Tone: ULTRA-CONSERVATIVE (regulatory risk is extreme)

---

## **C1: Fintech @ Series A (Conservative, Compliance-First)**

### **Your Reality Check:**

```
COMPANY PROFILE:
- Size: $2M-8M ARR, 20-100 employees
- Stage: Series A
- You: Founder (often ex-banking/finance background)
- Newsletter: Trust-building + regulatory updates
- Time: 3-5 hours/week
- Budget: $0-200/month
- CRITICAL: Legal review MANDATORY
```

### **Why Fintech Newsletters Are HIGHEST RISK:**

```
SALES TECH NEWSLETTER:
✅ Aggressive positioning
✅ "Gong is wrong about X"
✅ Contrarian takes
Risk: Low (worst case = lose subscribers)

HR TECH NEWSLETTER:
⚠️ Professional, empathetic
⚠️ No competitor attacks
Risk: Medium (reputation damage)

FINTECH NEWSLETTER:
🔴 ULTRA-CONSERVATIVE
🔴 LEGAL REVIEW MANDATORY
🔴 NEVER make unverified claims
🔴 NEVER attack competitors (could trigger regulatory scrutiny)
Risk: EXTREME (fines, license revocation, legal liability)

WHY:
- Financial regulations: RBI (India), SEC (US), FCA (UK)
- Financial advertising rules: Can't make unverified ROI claims
- Compliance violations: ₹1 Cr+ fines, criminal charges
- Reputational risk: Finance is trust-driven
```

### **Series A Fintech Newsletter: Trust-Building Strategy**

```
POSITIONING:

❌ WRONG POSITIONING:
"We're 10× better than [Competitor]"
"Save 50% on payment fees" (unless proven and disclosed)
"The future of fintech"

✅ CORRECT POSITIONING:
"RBI-compliant payment insights for CFOs"
"Regulatory updates for Indian fintech founders"
"Finance operations best practices"

SETUP:

PLATFORM CHOICE (Fintech-Specific):
□ LinkedIn Newsletter (RECOMMENDED)
  - CFOs very active on LinkedIn
  - Professional network = trust signal
  - Corporate email addresses (not personal)
  
□ Substack (SECONDARY)
  - Own the list
  - Professional layout
  - NOT: Medium, Twitter Newsletter (too casual for finance)

FIRST ISSUE TEMPLATE (Conservative):

Subject: "Regulatory Update: RBI's New Payment Guidelines [January 2026]"

NOT: "How We're Disrupting Payments" (too aggressive)
NOT: "Why Traditional Banking Is Broken" (antagonistic)
```

**BI-WEEKLY RHYTHM (Fintech = Slower Publishing)**

```
WHY BI-WEEKLY (not weekly):
- CFOs prefer quality > quantity
- Legal review takes time (1-2 days minimum)
- Regulatory updates don't happen weekly
- Finance decisions are slow (not impulse)

WEEK 1 (Research & Draft):

MONDAY-WEDNESDAY (4 hours): Research

FINTECH CONTENT SOURCES:

PRIMARY (Use These):
□ RBI website (official regulatory updates)
□ Economic Times Finance section
□ LiveMint fintech coverage
□ NPCI announcements (UPI, payments)
□ Ministry of Finance releases

SECONDARY:
□ Inc42 fintech coverage
□ Medianama (fintech policy)
□ YourStory fintech section
□ Industry associations (IAMAI)

WHAT TO AVOID:
❌ Rumors or unverified news
❌ Controversial hot takes
❌ Competitor comparisons
❌ Regulatory speculation

THURSDAY-FRIDAY (3 hours): Draft + Legal Review

CONTENT STRUCTURE (600-900 words):

**OPENING: Regulation or Trend**
Example:
"RBI released updated guidelines for payment aggregators 
on January 15, 2026. Here's what this means for fintech 
companies and their merchant partners..."

**ANALYSIS: What It Means**
- Impact on fintech companies
- Impact on customers
- Timeline for compliance
- Resources for implementation

**PRACTICAL GUIDANCE: What To Do**
- Steps for compliance
- Checklist for CFOs
- When to consult legal (always say "consult legal counsel")

**DISCLAIMER (ALWAYS INCLUDE):**
"This newsletter is for informational purposes only and 
does not constitute legal, financial, or regulatory advice. 
Always consult with qualified legal counsel for your 
specific situation."

LEGAL REVIEW CHECKLIST:
□ All claims verified (sources cited)
□ No competitor attacks or comparisons
□ No ROI claims unless proven + methodology disclosed
□ No regulatory speculation
□ Disclaimers present
□ Compliance with financial advertising rules

WEEK 2 (Publish Week):

TUESDAY (Publish 10 AM IST for India, 9 AM EST for US)

POST-PUBLISH (Conservative Approach):
□ Share on LinkedIn (professional tone)
□ Share in fintech community (IAMAI, if member)
□ NO aggressive self-promotion
□ NO calls to action beyond "Read the full update"
```

### **Fintech Newsletter: Content Ideas (First 12 Issues)**

```
ISSUE 1: "RBI's updated payment aggregator guidelines [Analysis]"
ISSUE 2: "New KYC requirements for fintechs [Checklist]"
ISSUE 3: "Data localization: What fintech CFOs need to know"
ISSUE 4: "GST implications for payment service providers"
ISSUE 5: "How 3 fintechs achieved SOC 2 compliance [Case studies]"
ISSUE 6: "UPI transaction limits: Recent changes explained"
ISSUE 7: "PCI DSS requirements for payment companies [Guide]"
ISSUE 8: "Cross-border payment regulations [2026 update]"
ISSUE 9: "Expense management: Tax deduction best practices"
ISSUE 10: "Corporate card programs: Compliance checklist"
ISSUE 11: "Fintech M&A: Regulatory approval process"
ISSUE 12: "2027 regulatory predictions for Indian fintech"

PATTERN:
- 70% regulatory updates & compliance
- 20% best practices (backed by data)
- 10% industry trends (conservative analysis)
- 0% competitor attacks
- 0% unverified claims
```

---

# 📊 SECTION D: OPERATIONS TECH NEWSLETTERS

**When To Use This Section:**
- Your product: Retail execution, logistics, field force automation
- Your audience: Sales/Ops leaders at CPG/FMCG companies
- Your angle: Distribution insights, retail execution, supply chain
- Tone: Practical, industry-specific, B2B2B2C aware

---

## **D1: Operations Tech @ Series A (Industry-Specific Insights)**

### **Your Reality Check:**

```
COMPANY PROFILE:
- Size: $1M-5M ARR, 15-60 employees
- Stage: Series A
- You: Founder (ex-CPG/FMCG or SaaS)
- Newsletter: Industry insights for CPG sales leaders
- Time: 4-6 hours/week
- Budget: $0-300/month
- Market: India retail/distribution focus
```

### **Why Operations Tech Newsletters Are NICHE:**

```
SALES/HR/FINTECH NEWSLETTERS:
- Broad audience: All B2B SaaS companies
- Generic insights: Sales, HR, finance tips
- Large market: 10,000s of potential subscribers

OPERATIONS TECH NEWSLETTER:
- Niche audience: CPG/FMCG sales & ops leaders
- Specific insights: Retail execution, distribution
- Smaller market: 1,000s of potential subscribers (but high intent)

ADVANTAGE OF NICHE:
✅ Less competition (few newsletters in this space)
✅ Higher engagement (exactly what audience needs)
✅ Easier to become category expert
✅ Stronger community (everyone knows each other)
```

### **Series A Operations Tech Newsletter Strategy**

```
POSITIONING OPTIONS:

Option 1: "THE INDIA RETAIL EXECUTION REPORT"
- Focus: General trade, kirana stores, distribution
- Audience: Sales heads at CPG companies (HUL, ITC, Dabur)
- Angle: Data-driven insights on retail execution

Option 2: "FIELD FORCE AUTOMATION INSIDER"
- Focus: Technology for field teams
- Audience: Ops leaders implementing tech
- Angle: Best practices, case studies, ROI

Option 3: "THE CPG DISTRIBUTION PLAYBOOK"
- Focus: Go-to-market for CPG in India
- Audience: Founders/sales leaders at emerging CPG brands
- Angle: Tactical distribution strategies

RECOMMENDED: Option 1 or 3 (broader appeal)

SETUP:

PLATFORM:
□ LinkedIn Newsletter (CPG leaders active on LinkedIn)
□ Substack (own the list)
□ WhatsApp Business (India-specific: field teams use WhatsApp)
  - Distribute newsletter summary via WhatsApp
  - Link to full version on LinkedIn/Substack

CONTENT SOURCES (Operations Tech Specific):

PRIMARY:
□ Industry reports: Nielsen, NielsenIQ (India retail data)
□ CPG company earnings calls (HUL, ITC, Nestle India)
□ Economic Times Retail section
□ Your product data (field visit insights)
□ Customer interviews (CPG sales heads)

SECONDARY:
□ Retail4Growth (industry publication)
□ Progressive Grocer India
□ Industry events (FMCG sales conferences)
□ Field team WhatsApp groups (insights from distributors)
```

**BI-WEEKLY PUBLISHING (Operations Tech Cadence)**

```
WEEK 1 (Research):

CONTENT IDEAS:

Distribution Insights:
- "State of general trade in North India [Q4 2025 data]"
- "How kiranas stock FMCG products [field study]"
- "Distributor margin analysis [benchmarks]"

Technology Adoption:
- "How HUL's field team uses mobile apps [case study]"
- "ROI of field force automation [data from 20 companies]"
- "Offline-first tech for rural distribution [best practices]"

Market Trends:
- "Quick commerce impact on FMCG distribution [analysis]"
- "D2C brands' distribution strategy [emerging trends]"
- "Modern trade vs general trade [2026 outlook]"

WEEK 2 (Write & Publish):

STRUCTURE (800-1,000 words):

**OPENING: Industry Insight**
Example:
"HUL reported in Q4 earnings that general trade grew 8% 
while modern trade was flat. We analyzed 10,000 retail 
visits across North India to understand why..."

**DATA/RESEARCH**
- Field visit insights
- Sales data (if anonymized)
- Industry benchmarks

**PRACTICAL TAKEAWAYS**
For Sales Heads:
- What this means for your distribution strategy
- Which channels to prioritize

For Field Teams:
- Tactical execution tips
- What to focus on in store visits

**CASE STUDY (If Available)**
"How [CPG Brand] increased distribution by 15% 
in general trade using [strategy]"

PUBLISHING:
□ Tuesday 10 AM IST (India CPG leaders)
□ Share on LinkedIn
□ Share summary in WhatsApp groups (with link)
□ Email to CPG sales heads in network
```

---

# 🔄 CROSS-CUTTING: UNIVERSAL FRAMEWORKS

## **Role-Specific Workflows**

### **FOUNDER-LED NEWSLETTERS (Full Autonomy)**

```
ADVANTAGES:
✅ No approval needed (publish freely)
✅ Personal voice = authentic
✅ Company brand = personal brand
✅ Can share metrics ("We're at $5M ARR")
✅ Can be aggressive (if industry allows)

DISADVANTAGES:
⚠️ You are the bottleneck (can't delegate fully)
⚠️ Personal reputation tied to company
⚠️ If you leave company, newsletter goes with you

BEST PRACTICES:
□ Publish consistently (don't miss issues)
□ Maintain quality (represents you + company)
□ Build email list on Substack (own the list)
□ Consider: What happens if you leave/sell company?
```

### **EMPLOYEE-LED NEWSLETTERS (Approval Workflows)**

```
SCENARIO: VP Marketing Wants Personal Newsletter

CHALLENGES:
⚠️ Company may want control over messaging
⚠️ Can't share company metrics without approval
⚠️ Must add "Views are my own" disclaimer
⚠️ Manager needs to be aware

APPROVAL WORKFLOW:

STEP 1: Get Manager Buy-In
□ Pitch: "I want to build my personal brand in [category]"
□ Position: "This will raise awareness for our company too"
□ Clarify: Personal newsletter, not company newsletter
□ Agree: What you can/cannot share about company

STEP 2: Set Boundaries
Can Share:
✅ Industry insights (not company-specific)
✅ Your perspective on trends
✅ Case studies (with approval)
✅ Public company information

Cannot Share:
❌ Revenue, ARR, growth numbers (unless public)
❌ Roadmap, unannounced features
❌ Customer names (without permission)
❌ Internal metrics, team size

STEP 3: Disclaimer
Every issue includes:
"Views expressed here are my own and do not necessarily 
represent the views of [Company Name]."

STEP 4: Periodic Check-Ins
□ Monthly: Show newsletter to manager
□ Quarterly: Confirm still aligned with company
□ Annually: Review and renew agreement
```

### **ENTERPRISE EMPLOYEE (Corporate Comms Controlled)**

```
SCENARIO: CMO at Public SaaS Company

REALITY:
🔴 EVERYTHING requires PR approval
🔴 Can't publish without 1-2 week review
🔴 Corporate Comms writes/reviews all content
🔴 No personal opinions on industry
🔴 Ghost-written by PR team

CONSTRAINTS:
□ Pre-approved topics only
□ No hot takes, no controversy
□ Company messaging only
□ Legal review for anything financial

OPTIONS:
1. Don't have personal newsletter (wait till you leave)
2. Ghost-write for founder (they publish under their name)
3. Internal newsletter (employees only, less restrictions)
```

---

## **Geography-Specific Tactics**

### **India Newsletter Strategy**

```
PUBLISHING TIMES:
✅ Tuesday 9 AM IST
✅ Wednesday 2 PM IST (after lunch)
✅ Thursday 10 AM IST

DISTRIBUTION CHANNELS:
□ LinkedIn (primary - India B2B very active)
□ WhatsApp Business (field teams, distributors)
□ Email (Substack/ConvertKit)
□ Twitter/X (growing for India B2B)

CONTENT EXAMPLES:
- Use Indian companies: FieldAssist, not Gong
- Use rupee pricing: "₹5K/month" not "$50/month"
- Reference: Indian regulations (RBI), not US (SEC)

COMMUNITY ENGAGEMENT:
□ SaaSBoomi (India B2B SaaS community)
□ IAMAI (fintech, if applicable)
□ LinkedIn India Groups (sales, HR, tech)
```

### **US Newsletter Strategy**

```
PUBLISHING TIMES:
✅ Tuesday 9 AM EST/6 AM PST
✅ Wednesday 10 AM EST/7 AM PST
✅ Thursday 9 AM EST/6 AM PST

DISTRIBUTION CHANNELS:
□ LinkedIn (primary)
□ Email (Substack, ConvertKit, Beehiiv)
□ Twitter/X (B2B SaaS community active)
□ Slack communities (SaaStr, Pavilion, Revenue Collective)

CONTENT EXAMPLES:
- Use US companies: Gong, Lattice, Stripe
- Use dollar pricing: "$500/month"
- Reference: US regulations (SEC, GDPR if EU)

COMMUNITY ENGAGEMENT:
□ SaaStr (B2B SaaS)
□ Pavilion (sales, marketing, CS leaders)
□ Revenue Collective (CROs, RevOps)
```

---

## **Worked Examples: Multi-Dimensional Scenarios**

### **Example 1: Sales Tech Founder, Series A, India → Newsletter for Lead Gen**

```
SCENARIO:
- Company: AI sales coaching, $3M ARR, 30 employees
- You: Co-founder & CEO
- Goal: Generate 15 SQLs/month via newsletter
- Market: India B2B SaaS (SMB focus)
- Budget: $0-100/month

NEWSLETTER STRATEGY:

NAME: "The AI Sales Coach" (your positioning)
PLATFORM: LinkedIn Newsletter + Substack
FREQUENCY: Weekly
AUDIENCE: Sales leaders at $1M-10M ARR B2B SaaS companies (India)

CONTENT ANGLE:
"AI-powered sales insights for Indian startup sales teams"

ISSUE PLAN:
Week 1: "How AI analyzes top sales calls [your product data]"
Week 2: "The discovery framework for SMB sales [tactical]"
Week 3: "Gong vs affordable alternatives for Indian startups"
Week 4: "Sales coaching at scale: AI vs human [research]"

GROWTH TACTICS:
□ Every LinkedIn post → CTA to newsletter
□ Guest post on SaaSBoomi → Newsletter signup
□ Interview 3 Indian startup founders → They share with network
□ Comment on sales leader posts → Newsletter in profile

TIMELINE:
Month 1: 50 subscribers, 2 SQLs
Month 3: 200 subscribers, 8 SQLs
Month 6: 600 subscribers, 15+ SQLs

RESULT:
Newsletter becomes #2 lead source (after LinkedIn posts)
Cost: $0 (your time: 4 hours/week)
```

### **Example 2: HR Tech VP Marketing, Series B, US → Thought Leadership Newsletter**

```
SCENARIO:
- Company: Employee engagement platform, $20M ARR
- You: VP Marketing
- Goal: Build category authority, 20 SQLs/month
- Market: US mid-market (500-2000 employee companies)
- Budget: $5K/month for content

NEWSLETTER STRATEGY:

NAME: "The Employee Experience Insider"
PLATFORM: ConvertKit (owned list) + LinkedIn cross-post
FREQUENCY: Bi-weekly (quality > quantity for HR)
TEAM: 1 writer, 1 designer

CONTENT STRATEGY:

Q1 Research: "State of Employee Engagement 2026"
- Survey 500 HR leaders
- Partner with SHRM for distribution
- 3-week newsletter series

Q2: Customer case studies (monthly)
Q3: Hybrid work best practices (research series)
Q4: 2027 predictions (thought leadership)

GROWTH TACTICS:
□ Sponsorship: People Managing People newsletter ($2K)
□ LinkedIn ads: Download engagement report ($1K/month)
□ Webinar series: Registrants → Newsletter ($1K/month)
□ Conference: SHRM Annual (speaking + booth)

APPROVAL WORKFLOW:
□ Writer drafts → You review → Founder/CHRO feedback → Publish
□ Legal review: If compliance/regulation content

TIMELINE:
Month 1: 1,000 subscribers (launch with research report)
Month 6: 4,000 subscribers, 20 SQLs/month
Month 12: 8,000 subscribers, category authority signal

RESULT:
Cited by: HBR, SHRM publications
Speaking invites: 3-5 conferences/year
Recruiting: "I read your newsletter" in interviews
```

---

## **Common Newsletter Mistakes & How to Avoid**

### **Mistake 1: "Industry-Agnostic Content"**

```
WRONG APPROACH:
"Write generic B2B newsletter with sales/HR/fintech advice"

WHY IT FAILS:
- Sales Tech: Tactical, data-driven, aggressive
- HR Tech: Professional, empathetic, research-backed
- Fintech: Conservative, compliance-first, legal review

CORRECT APPROACH:
Choose ONE vertical, go deep
→ Section A (Sales Tech) or B (HR) or C (Fintech) or D (Ops)
```

### **Mistake 2: "No Clear Goal"**

```
WRONG APPROACH:
"I'll start a newsletter and see what happens"

CLEAR GOALS:
- Series A: Lead generation (10-20 SQLs/month)
- Series B: Thought leadership + pipeline
- Series C+: Category ownership
- Personal: Build authority for next role

MEASURE:
□ Subscribers (growth rate)
□ Open rate (engagement)
□ Click rate (interest)
□ SQLs (if lead gen)
□ Inbound mentions (if thought leadership)
```

### **Mistake 3: "Inconsistent Publishing"**

```
PROBLEM:
Week 1: Publish
Week 2: Skip (too busy)
Week 3: Publish
Week 4: Skip (on vacation)

RESULT:
- Subscribers forget about you
- Algorithm penalizes you (LinkedIn)
- Lose momentum

SOLUTION:
□ Start with bi-weekly (easier to sustain)
□ Batch write 2-3 issues ahead
□ Have backup issues (evergreen content)
□ Use scheduling tools (ConvertKit, LinkedIn scheduler)
```

---

## **Prompt Templates for Each Scenario**

### **Template 1: Series A Sales Tech Founder Newsletter**

```
Using the Newsletter Creation skill, Section A1:

I'm a Series A Sales Tech founder in [India/US].

My product: [One-line description]
My ICP: [Sales leaders at X companies]
Newsletter goal: Generate 10-20 SQLs per month

Please provide:
1. Newsletter positioning and name
2. First 3 issue topics (tactical, data-driven)
3. Weekly workflow (3-5 hours/week, $0 budget)
4. Growth tactics (free, appropriate for Sales Tech)
5. Success metrics (what to track)

India-specific if applicable:
- IST publishing times
- Indian B2B SaaS examples
- SaaSBoomi distribution
```

### **Template 2: Series B HR Tech VP Newsletter**

```
Using the Newsletter Creation skill, Section B2:

I'm VP Marketing at Series B HR Tech.

Our product: [Employee engagement/performance/etc.]
My goal: Build thought leadership + 20 SQLs/month
Budget: $5K/month for content
Team: 1 writer, 1 designer

Please provide:
1. Content strategy (bi-weekly rhythm)
2. Q1 research topic (employee engagement, hybrid work, etc.)
3. Team workflow with approval process
4. Conservative growth tactics (appropriate for HR Tech)
5. Partnership ideas (SHRM, Josh Bersin, etc.)

Remember:
- Professional tone (not aggressive like Sales Tech)
- Research-backed (cite sources)
- Legal review if compliance topics
```

---

## **Tool Comparison Matrix**

| Tool | Free | Paid | Best For | Not Good For |
|------|------|------|----------|--------------|
| **LinkedIn Newsletter** | ✅ | N/A | Sales/HR/Ops Tech (B2B audience on LinkedIn) | Fintech (want owned list) |
| **Substack** | ✅ | 5% fee paid | Owning list, monetization later | Enterprise employee (no autonomy) |
| **ConvertKit** | $0-25/mo | $29-79/mo | Series B+ (advanced features, automation) | Series A (overkill) |
| **Beehiiv** | ✅ | $49+/mo | Growth features, referrals, monetization | Simple newsletter |
| **Ghost** | $9+/mo | $25-199/mo | Tech-savvy, custom domain, membership | Non-technical founders |
| **Medium** | ✅ | N/A | Consumer content, broad reach | B2B SaaS (wrong audience) |

---

## **Quick Reference: Industry-Stage-Role Matrix**

```
SALES TECH:
├─ Series A Founder → Section A1 (Lead gen, aggressive, weekly)
├─ Series B VP Mktg → Section A2 (Thought leadership, team, bi-weekly)
└─ Series C+ Dir Content → Section A3 (Category ownership, media-level)

HR TECH:
├─ Series A Founder → Section B1 (Trust-building, professional, bi-weekly)
├─ Series B Dir Mktg → Section B2 (Research-backed, team, bi-weekly)
└─ Series C+ VP Content → Section B3 (Josh Bersin-level, membership)

FINTECH:
├─ Series A Founder → Section C1 (Compliance, legal review, bi-weekly)
├─ Series B VP Mktg → Section C2 (Regulatory insights, team)
└─ Series C+ VP Content → Section C3 (Category authority, conservative)

OPERATIONS TECH:
├─ Series A Founder → Section D1 (India retail, niche, bi-weekly)
├─ Series B Dir Mktg → Section D2 (CPG insights, case studies)
└─ Series C+ VP Content → Section D3 (Industry authority)
```

---

**END OF SKILL**
```

## File: `newsletter-creation-curation/README.md`
```markdown
# Newsletter Creation & Curation

Most B2B newsletters fail because they ignore industry context.

This skill is built for teams that need newsletters tailored to **industry + company stage + role + geography**, not generic writing prompts.

## Positioning

**The only newsletter framework that adapts to your industry, stage, and role.**

It helps agents and operators produce newsletters that are:
- Strategically aligned to GTM goals
- Executable with real workflows and approvals
- Consistent issue after issue

## What You Get

- `SKILL.md`: concise execution guide with decision tree + workflow
- `PLAYBOOK.md`: full strategic library (all detailed guidance preserved)
- `templates/`: industry-specific newsletter structures
- `examples/`: realistic finished issue samples

## Why Teams Use It

- Avoids one-size-fits-all newsletter advice
- Bakes in role-based approval logic (especially critical for fintech/enterprise)
- Converts strategy into repeatable publishing operations

## Time Savings

Typical manual process for one issue:
- 2-3 hours strategy and structure decisions
- 2-4 hours drafting and revisions

With this framework:
- 20-40 minutes to choose strategy path and template
- 60-120 minutes to produce a high-quality draft
- 30-45% less iteration time from clearer structure and constraints

## Quick Start

1. Open `SKILL.md` and answer the 5 decision-tree questions.
2. Pick your template from `templates/`.
3. Generate draft using the 4-step workflow.
4. Validate with role/compliance checks.
5. Use `PLAYBOOK.md` when you need deeper strategic guidance.

## Social Proof

- Created by Shashwat Ghosh (Fractional CMO, Helix GTM Consulting)
- Built from practical B2B SaaS newsletter frameworks across Sales Tech, HR Tech, Fintech, and Operations Tech
- Includes realistic examples with KPI targets for pipeline and thought-leadership outcomes

## Example Files

- `examples/example-sales-tech-issue.md`
- `examples/example-hr-tech-issue.md`

## Industry Coverage

- Sales Tech
- HR Tech
- Fintech
- Operations Tech

## Links

- ClawdHub: https://clawdhub.com/shashwatgtm/newsletter-creation-curation
- LinkedIn: https://linkedin.com/in/shashwatghosh-ai-b2b-gtm-fractionalcmo
- GitHub: https://github.com/shashwatgtm
```

## File: `newsletter-creation-curation/SKILL-OC.md`
```markdown
---
name: newsletter-creation-curation
description: Industry-adaptive B2B newsletter creation with stage, role, and geography-aware workflows
---

**Platform:** OpenClaw (token-optimized)

## Required Intake (all 5 dimensions before starting)

```
Goal: [lead_gen | thought_leadership | personal_brand | category_ownership]
Industry: [sales_tech | hr_tech | fintech | ops_tech]
Stage: [series_a | series_b | series_c_plus]
Role: [founder | vp_director | pmm_content | enterprise_employee]
Geography: [us_first | india_first]
```

Also collect: company context, newsletter goal, prior issues (for consistency), approval constraints.

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | Outline + 3 lead story angles | Planning, editorial direction |
| `standard` | Full edition, all sections written | Publishing this week |
| `deep` | Full edition + 4-week calendar + audience segmentation | Launch or systematizing |

## Phase 1: Strategy Statement

Output one line: `For [ICP], we publish [cadence] to achieve [goal] with [format].`

Context rules:
- Industry tone: Sales Tech = data-heavy | HR Tech = research-led | Fintech = compliance-aware | Ops Tech = practical
- Cadence: Series A = weekly/bi-weekly | Series B = weekly w/ process | Series C+ = media-grade weekly
- Employee role → always include approval checkpoint before final draft
- India-first → IST timing + local examples | US-first → EST/PST + US benchmarks

## Phase 2: Issue Blueprint

```
Strategy: For [ICP], [cadence] to achieve [goal].
Industry tone: [tactical/research-led/compliance-aware/practical]
Approval required: [yes/no — who]

Sections:
1. Subject lines (3 options)
2. Hook (~75 words)
3. Core insight (~200 words)
4. Actionable playbook (~150 words, 3-5 steps)
5. CTA (1 sentence)
```

Get confirmation or proceed to draft.

## Phase 3: Full Draft

**Subject Lines (3 required):**
- A: Curiosity/open loop ("The metric most [ICP] ignore")
- B: Specific + benefit ("How [type] achieves [X] in [timeframe]")
- C: Contrarian ("Stop [behavior]. Do this instead.")

**Hook:** First 2 sentences earn the read. Problem + stakes. 60-second scannable.

**Core Insight:** One primary takeaway per issue. Support with data, framework, or named pattern. Specific numbers or named examples.

**Actionable Playbook:** 3-5 implementable steps. Series A = simpler | Series C+ = more sophisticated.

**CTA:** ONE measurable action. Never "Learn more." Options: reply with [X], click [link], share [asset], book [demo].

## Refinement Checklist

- [ ] Clarity: value extractable in 60 seconds?
- [ ] Specificity: concrete guidance or evidence in each section?
- [ ] Relevance: tone matches industry + role?
- [ ] Compliance: fintech/employee → legal/manager review step included?
- [ ] CTA: exactly ONE measurable action?

## Output Format

```
## Newsletter: [Name] — Issue #[X] — [Date]
Strategy: For [ICP], [cadence] to achieve [goal].

Subject Lines:
A) | B) | C) | Recommended: [A/B/C] — [reason]

Hook: [text]

Core Insight: [text]

Playbook:
1. [Step] 2. [Step] 3. [Step]

CTA: [text]
```

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `newsletter-creation-curation/SKILL.md`
```markdown
---
name: newsletter-creation-curation
description: Industry-adaptive B2B newsletter creation with stage, role, and geography-aware workflows
---

# Newsletter Creation & Curation Skill

Use this skill to create B2B newsletters that match business context, not generic content templates.

Deep strategic guidance is in `PLAYBOOK.md`.
Use this file as the executable operating manual.

---

## Mode

Detect from context or ask: *"Outline only, full edition, or full edition + calendar?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | Edition outline + 3 lead story angles, no writing | Planning, editorial direction |
| `standard` | Full newsletter edition, all sections written | Publishing this week |
| `deep` | Full edition + 4-week content calendar + audience segmentation recommendations | Launching or systematizing a newsletter |

**Default: `standard`** — use `quick` if they're still deciding what to write. Use `deep` if they're building a newsletter from scratch or scaling.

---

## Context Loading Gates

**Before generating any newsletter content, collect:**

- [ ] **Company context:** What product/service? Who is the ICP?
- [ ] **Newsletter goal:** Lead gen / thought leadership / personal brand / category ownership
- [ ] **Industry vertical:** Sales Tech / HR Tech / Fintech / Operations Tech
- [ ] **Company stage:** Series A / Series B / Series C+
- [ ] **Role:** Founder / VP-Director / PMM-Content / Enterprise employee
- [ ] **Geography:** US-first / India-first
- [ ] **Prior issues:** Any existing issues to maintain consistency and voice?
- [ ] **Approval constraints:** Does this need legal/brand/manager review?

**Structured intake — answer all 5 dimensions before proceeding:**

```
Goal: [lead_gen | thought_leadership | personal_brand | category_ownership]
Industry: [sales_tech | hr_tech | fintech | ops_tech]
Stage: [series_a | series_b | series_c_plus]
Role: [founder | vp_director | pmm_content | enterprise_employee]
Geography: [us_first | india_first]
```

---

## Phase 1: Context Analysis

Before drafting, reason through:

1. **Template match:** Which industry template best fits? (Sales Tech = data-heavy; HR Tech = research-led; Fintech = compliance-aware; Ops Tech = practical)
2. **Cadence match:** Series A = weekly/bi-weekly for simplicity; Series B = weekly with process; Series C+ = media-grade weekly with pillars
3. **Role constraints:** Founder = direct POV allowed; Employee = approval checkpoint required before final draft
4. **Geography adjustments:** India-first = IST timing + local examples; US-first = EST/PST + US benchmarks
5. **Goal-content alignment:** Lead gen needs a clear conversion CTA; thought leadership needs original insight, not general content

Output one-line strategy statement:
> `For [ICP], we publish [cadence] to achieve [goal] with [format].`

---

## Phase 2: Issue Blueprint

Before writing full draft, produce an issue blueprint:

```markdown
## Issue Blueprint

**Strategy:** For [ICP], [cadence] to achieve [goal].
**Industry tone:** [tactical/research-led/compliance-aware/practical]
**Approval required:** [yes/no — who]

**Sections:**
1. Subject lines (3 options) — [~words each]
2. Hook — [target ~75 words]
3. Core insight — [target ~200 words]
4. Actionable playbook — [target ~150 words, 3-5 steps]
5. CTA — [1 sentence, singular action]
```

Get confirmation or proceed to draft.

---

## Phase 3: Full Issue Draft

Generate complete publish-ready draft. Required structure — every issue:

### Subject Line Options (3 required)
Produce 3 distinct angles:
- A: Curiosity/open loop ("The metric most [ICP] ignore")
- B: Specific + benefit ("How [Company type] achieves [X] in [timeframe]")  
- C: Contrarian/bold ("Stop [common behavior]. Do this instead.")

### Hook
- First 2 sentences must earn the read
- Lead with the problem + stakes
- Target: busy reader can extract the point in 60 seconds

### Core Insight
- One primary takeaway per issue — not three
- Support with: data, framework, or named pattern
- Include specific numbers or named examples wherever possible

### Actionable Playbook
- 3-5 steps or checklist items
- Each step must be implementable, not just conceptual
- Series A = simpler steps; Series C+ = more sophisticated process

### CTA
- ONE measurable action only
- Options: reply with [X], click [link], share [asset], book [demo]
- Never use vague CTAs ("Learn more")

---

## Phase 4: Refinement Checklist

Run before delivering:

- [ ] `Clarity`: Can a busy reader extract value in 60 seconds?
- [ ] `Specificity`: Does each section include concrete guidance or evidence?
- [ ] `Relevance`: Does tone match industry and role constraints?
- [ ] `Compliance`: For fintech/employee-led, is a legal/manager review step included?
- [ ] `Consistency`: Does voice align with prior issues (if any were provided)?
- [ ] `CTA`: Is there exactly ONE measurable CTA — not two, not zero?

---

## Phase 5: Self-Critique Pass (REQUIRED)

After completing the draft, evaluate:

- [ ] Does the subject line A option create genuine curiosity without being clickbait?
- [ ] Does the hook deliver a problem + stakes in the first 2 sentences?
- [ ] Is the core insight something subscribers couldn't get from a generic AI prompt?
- [ ] Does the playbook have steps that are specific to this audience, not generic "tips"?
- [ ] Is the CTA actually measurable — i.e., can they track whether it worked?
- [ ] For fintech/employee contexts: is there an explicit approval checkpoint?

Flag any issue: "The playbook steps are too generic for a Series B SaaS audience — they read as beginner content. Revised to assume existing process maturity."

---

## Iteration Protocol

After delivering the draft:
1. Ask: "Does the hook earn the read? Does the playbook feel actionable for your audience?"
2. If hook is weak → rewrite using a different angle (data-led, story-led, or contrarian)
3. If playbook is too generic → ask for a specific example from their own experience to ground it
4. For next issue: "Want me to save these content themes so the next issue builds on this one?"

---

## Output Structure

```markdown
## Newsletter Issue: [Name] — Issue #[X] — [Date]
**Strategy:** For [ICP], [cadence] to achieve [goal].

---

### Subject Line Options
A) [Curiosity/open loop]
B) [Specific + benefit]  
C) [Contrarian/bold]
**Recommended:** [A/B/C] — [reason]

---

### Hook
[2-3 sentences — problem + stakes]

---

### Core Insight
[200-300 words — data, framework, or named pattern]

---

### Actionable Playbook
1. [Step]
2. [Step]
3. [Step]

---

### CTA
[Single measurable action]

---

### Distribution Plan
- **Send time:** [Day, Time, Timezone]
- **LinkedIn amplification:** [Post angle / hook]
- **Secondary channel:** [Platform + angle]

### KPI Targets
- Open rate goal: [%]
- CTR goal: [%]
- Primary metric: [SQLs / subscribers / replies]

### Approval Required
[Yes — [who] | No]

### Self-Critique Notes
[Issues flagged + revisions made]
```

---

## Playbook Map (Deep Dives in `PLAYBOOK.md`)

- Sales Tech strategy: `SECTION A`
- HR Tech strategy: `SECTION B`
- Fintech strategy: `SECTION C`
- Operations Tech strategy: `SECTION D`
- Role approvals and geography tactics: `CROSS-CUTTING: UNIVERSAL FRAMEWORKS`

---

*Skill by Brian Wagner | AI Marketing Architect | brianrwagner.com*
```

## File: `newsletter-creation-curation/examples/example-hr-tech-issue.md`
```markdown
# Example Issue: HR Tech (Series B, VP Marketing)

## Subject Line Options
1. `Manager burnout is rising. Here is the operating cadence that reduces escalation.`
2. `What high-retention People teams do differently in low-budget quarters.`
3. `Performance reviews are not the problem. Weekly clarity is.`

## Final Subject Line
`What high-retention People teams do differently in low-budget quarters.`

## Newsletter Draft

Most HR leaders are being asked to improve retention without adding budget. That usually leads to program overload: more surveys, more training, more dashboards. The teams outperforming this year are doing the opposite. They are reducing initiative count and increasing manager execution quality.

Across recent People Ops interviews we conducted, one pattern stood out. Organizations with stronger retention did not launch more engagement programs. They installed a weekly manager operating rhythm with clear expectations on feedback, prioritization, and workload visibility.

### What Is Changing
The old model assumed annual or biannual intervention could stabilize employee experience. Current conditions do not support that. Team dynamics shift faster, and uncertainty pressure is ongoing. High-performing HR teams are moving from campaign-based engagement to operating-system-based engagement.

That means fewer broad initiatives and tighter recurring manager behaviors.

### A Practical 3-Part Framework
1. Diagnose manager load quality
- Track meeting bloat, context switching, and unresolved blockers.
- Add one monthly pulse question on manager clarity: `I know what good looks like this week.`

2. Design a weekly clarity cadence
- Require a 20-minute weekly team reset: priorities, tradeoffs, risk flags.
- Standardize one feedback checkpoint per direct report every two weeks.

3. Deploy with guardrails
- Give managers a one-page playbook, not a new toolkit stack.
- Review adherence monthly with HRBP support.
- Report two metrics only: regrettable attrition and manager clarity score.

### Case Snapshot
A 900-employee SaaS company had stable engagement scores but rising regrettable attrition in technical teams. HR introduced a weekly manager clarity rhythm and removed three low-usage engagement programs. After one quarter, regrettable attrition in target teams dropped by 2.8 points and internal mobility applications increased.

### Compliance and Communication Note
If your org is updating people policies as part of this shift, coordinate language with legal and internal comms before broad rollout.

### CTA
Reply with `CLARITY CADENCE` and I will share the weekly manager agenda template used in this framework.

## Send Plan
- Send time: Thursday, 10:00 AM EST
- Amplification:
  - LinkedIn summary post for People leaders
  - Share in one HR operator community

## KPI Targets
- Open rate: 35%+
- Senior HR reply rate: 4%+
- Template requests: 15+
```

## File: `newsletter-creation-curation/examples/example-sales-tech-issue.md`
```markdown
# Example Issue: Sales Tech (Series A, Founder-Led)

## Subject Line Options
1. `Your discovery calls are too long. Here is the 22-minute structure that converts.`
2. `We reviewed 140 demo recordings. This 1 change improved next-step rate.`
3. `Most SDR handoffs fail before the meeting. Fix the transition script.`

## Final Subject Line
`We reviewed 140 demo recordings. This 1 change improved next-step rate.`

## Newsletter Draft

Last quarter, our team reviewed 140 product demos across mid-market SaaS teams. The pattern was consistent: reps that won next steps did not present more features. They spent less time in product walkthrough and more time forcing agreement on one business pain before the first click.

Most demos fail because discovery and demonstration are treated as separate steps. They are not. High-performing reps use the first five minutes of the demo to confirm problem priority, then show only the workflow tied to that problem.

### The Pattern We Saw
- Demos with a clear pain confirmation had a 34% higher next-step rate.
- Demos that opened with a full platform tour had the lowest engagement by minute 12.
- Reps who used one quantified problem statement before screen-share moved deals faster.

The takeaway is simple: prospects do not buy product breadth in the first demo. They buy confidence that one painful process can be fixed quickly.

### The 3-Step Demo Transition Playbook
1. Pre-demo alignment
- Before the call, write one hypothesis: `The primary problem is [X] costing [Y].`
- Ask the AE to validate this in the opening 3 minutes.

2. Pain lock before product
- Use this line before any screens: `If we could cut [problem] by [target], would this become priority this quarter?`
- Wait for explicit confirmation. If you do not get it, continue discovery instead of demoing.

3. Show one workflow, not the platform
- Choose one workflow connected to the confirmed pain.
- Narrate outcome, not features: `This step removes manual reconciliation and saves ~4 hours/week.`
- End with implementation clarity: owner, timeline, first KPI.

### Mini Case
One 12-person sales team selling into IT services had stalled pipeline despite healthy top-of-funnel. Their demos averaged 44 minutes with low next-step conversion. They switched to a single-workflow demo structure and added the pain-lock question before screen-share. Within 5 weeks, demo-to-next-step rose from 31% to 43%.

### CTA
Reply with `DEMO STRUCTURE` and I will send the one-page checklist we use before every first demo.

## Send Plan
- Send time: Tuesday, 9:00 AM EST
- Amplification:
  - LinkedIn post summarizing the 3-step playbook
  - 8-post thread with the pain-lock script and metrics

## KPI Targets
- Open rate: 38%+
- CTR/reply intent: 6%+
- Qualified demo checklist requests: 20+
```

## File: `newsletter-creation-curation/templates/fintech-template.md`
```markdown
# Fintech Newsletter Template

## Positioning
- Audience: fintech operators, product/compliance leaders, finance execs
- Promise: clear, compliance-aware interpretation of fintech shifts
- Tone: precise, conservative, trust-first

## Issue Structure (750-1,050 words)

### 1. Subject Line Options (3)
- Formula: `[regulatory/market change] + [practical implication]`
- Example: `New KYC expectations are here. What product teams must change.`

### 2. Opening Brief (80-120 words)
- Summarize the change/event in plain language
- Clarify why operators should care now

### 3. What Changed (180-260 words)
- Facts only, no speculative claims
- Distinguish confirmed information from interpretation

### 4. Operator Playbook (260-360 words)
- `Risk Check`: exposure areas
- `Operational Response`: process + ownership
- `Communication`: how to align internal teams/customers

### 5. Compliance Note (90-140 words)
- Explicit caveat: informational only, not legal advice
- Add required internal approval note if employee-led

### 6. CTA (40-70 words)
- Single ask: download checklist, join briefing, submit question

## Recurring Blocks
- `Regulatory Radar`: one update and action impact
- `Control Gap`: one common compliance/ops miss
- `Trust Signal`: one reliability metric to monitor

## Send + Distribution
- Primary send: Tuesday or Wednesday morning local market time
- Amplify: LinkedIn + niche fintech operator group

## KPI Focus
- Open rate, reply quality, compliance-team engagement, high-intent inbound
```

## File: `newsletter-creation-curation/templates/hr-tech-template.md`
```markdown
# HR Tech Newsletter Template

## Positioning
- Audience: CHROs, HRBPs, People Ops leaders, Talent leaders
- Promise: practical, research-backed people strategy guidance
- Tone: professional, empathetic, evidence-led

## Issue Structure (800-1,100 words)

### 1. Subject Line Options (3)
- Formula: `[people challenge] + [evidence-backed promise]`
- Example: `Burnout is up, budgets are flat. What top People teams do next.`

### 2. Opening Context (90-140 words)
- State the people challenge and why it matters now
- Use one trusted source or survey insight

### 3. Trend Breakdown (220-300 words)
- Explain one macro trend and implications for HR teams
- Keep language neutral and credible

### 4. Practical Framework (260-340 words)
- `Diagnose`: what to assess first
- `Design`: what policy/process to change
- `Deploy`: how to implement with managers

### 5. Case Snapshot (120-160 words)
- Short story: team challenge, intervention, measurable impact

### 6. CTA (50-80 words)
- Single ask: reply with approach, download checklist, register for session

## Recurring Blocks
- `Policy Watch`: notable compliance/process update
- `Manager Toolkit`: one practical manager prompt/template
- `People Metric`: one benchmark and interpretation

## Send + Distribution
- Primary send: Tuesday or Thursday morning EST
- Amplify: LinkedIn + HR community share (SHRM, People communities)

## KPI Focus
- Open rate, replies from senior HR roles, resource downloads, qualified conversations
```

## File: `newsletter-creation-curation/templates/ops-tech-template.md`
```markdown
# Operations Tech Newsletter Template

## Positioning
- Audience: operations leaders, supply chain managers, process owners
- Promise: practical process improvements with measurable efficiency impact
- Tone: pragmatic, systems-focused, implementation-oriented

## Issue Structure (700-1,000 words)

### 1. Subject Line Options (3)
- Formula: `[operational bottleneck] + [clear result]`
- Example: `Order handoffs added 18% delay. Here is the fix map.`

### 2. Problem Snapshot (80-120 words)
- Define one high-friction workflow problem
- Quantify current pain (time, cost, error rate)

### 3. Root-Cause Lens (180-260 words)
- Show where the process breaks (handoff, visibility, accountability)

### 4. Implementation Blueprint (250-350 words)
- `Map`: document current-state flow
- `Intervene`: 1-2 workflow changes
- `Instrument`: metrics and ownership for tracking

### 5. Field Example (100-150 words)
- Practical implementation scenario in retail/logistics/manufacturing context

### 6. CTA (40-70 words)
- Single ask: request template, share workflow map, join diagnostic call

## Recurring Blocks
- `Workflow Audit`: one process teardown
- `Ops Metric`: cycle time / error / fill-rate benchmark
- `Stack Simplification`: one tool consolidation idea

## Send + Distribution
- Primary send: Tuesday or Thursday morning
- Amplify: LinkedIn + one domain community/channel

## KPI Focus
- Open rate, process-audit replies, meeting requests, pilot conversations
```

## File: `newsletter-creation-curation/templates/sales-tech-template.md`
```markdown
# Sales Tech Newsletter Template

## Positioning
- Audience: CROs, VP Sales, RevOps leaders, SDR managers
- Promise: actionable revenue insights from real sales execution
- Tone: direct, data-backed, tactical

## Issue Structure (700-1,000 words)

### 1. Subject Line Options (3)
- Formula: `[data point] + [problem/outcome]`
- Example: `73% of discovery calls stall here. Fix it in 2 steps.`

### 2. Opening Hook (80-120 words)
- Start with one concrete signal: call data, win-rate shift, pipeline trend
- Frame stakes for this quarter

### 3. Core Insight (180-260 words)
- Explain one pattern from market/customer/sales data
- Include one contrarian angle

### 4. Tactical Playbook (250-350 words)
- Step 1: before the call/opportunity
- Step 2: during execution
- Step 3: follow-up and measurement

### 5. In-the-Wild Example (100-140 words)
- Mini case from a real-world scenario (anonymized if needed)
- Show before/after outcome

### 6. CTA (40-80 words)
- Single ask: reply, benchmark request, or demo

## Recurring Blocks
- `Deal Clinic`: diagnose one lost deal pattern
- `Script Rewrite`: improve one cold email or discovery question
- `Metric of the Week`: one KPI and benchmark

## Send + Distribution
- Primary send: Tuesday or Wednesday morning EST
- Amplify: LinkedIn post + short thread + one community share

## KPI Focus
- Open rate, CTR, replies, demo requests, SQL attribution
```

## File: `plan-my-day/README.md`
```markdown
# Plan My Day

**Stop wasting your peak hours on email.**

Generate an energy-optimized, time-blocked daily plan in 2 minutes. Know what matters. Protect your focus. Win consistently.

## The Problem

You start every day reacting:
- Check email first thing → 90 minutes gone
- Meetings fill your calendar → No time for real work
- "Productive" days with zero priority progress
- Brain fried by 3pm, still have 3 hours of work left

**Result:** 15% weekly goal completion. Constant firefighting. Burnout.

## The Solution

**Plan My Day** - Energy-aware scheduling based on circadian rhythm research and GTD principles.

### What You Get

✅ **Top 3 Priority framework** - Focus on what actually moves the needle  
✅ **Energy-optimized scheduling** - Hard work in peak hours, admin in low-energy windows  
✅ **Built-in buffers** - Only schedule 80% of time (20% for reality)  
✅ **Break enforcement** - 15-min breaks every 90 minutes (backed by research)  
✅ **Evening reflection** - Track what works, improve over time  
✅ **2-minute planning** - Faster than writing your own plan, more consistent  

### Why This vs Just Asking ChatGPT?

| "Plan my day" prompt | Plan My Day Skill |
|---|---|
| Different plan every time | Consistent methodology |
| No energy optimization | Matches tasks to peak hours |
| Ignores your calendar | Respects constraints |
| No accountability | Evening check-in built-in |
| No learning/improvement | Tracks what works over time |

## Real Results

**Marketing manager at B2B SaaS company** (8 weeks):

- Goal completion: 15% → 74% (+59 points)
- Meeting time: 6-8 hrs/day → 3-4 hrs/day
- Deep work blocks protected: 0 days/week → 4 days/week
- Energy levels: 4.1/10 → 8.2/10

**Quote:** "The daily plan gave me permission to say no. If it wasn't in my Top 3, I deferred it."

## Quick Start

### Install

```bash
cp -r plan-my-day $HOME/.openclaw/skills/
```

### Use

```bash
# Generate today's plan
/plan-my-day

# Plan a future date
/plan-my-day 2026-02-20

# Custom energy windows
/plan-my-day --peak 9-11,14-16
```

### Example Output

```markdown
## Top 3 Priorities:
1. Finalize launch copy (900 words) - DONE by 11:30
2. Partner demo with next steps - DONE by 3:00  
3. Sprint planning with team - DONE by 5:00

## Schedule:
9:00-11:30: Deep Work → Launch copy (Priority #1) 🎯
12:30-2:45: Partner demo (Priority #2)
3:00-4:45: Sprint planning (Priority #3)
5:00-5:30: Admin/wrap-up

Protections:
- Phone off 9am-12pm
- Slack paused during deep work
- Lunch break: 12:30-1:30 (non-negotiable)
```

## What Makes This Different

### Research-Backed Scheduling

- **Circadian optimization** - Peak cognitive performance 2-3 hrs after waking
- **Ultradian rhythm respect** - 90-minute focus blocks + 15-min breaks
- **Decision fatigue prevention** - High-stakes work before 3pm
- **Implementation intentions** - Time+task = 2-3× completion rate

### Energy Window Defaults (Customizable)

| Time Window | Energy Level | Best For |
|---|---|---|
| 9:00-12:00 | Peak | Deep work, strategic thinking, #1 priority |
| 2:00-4:00 | Secondary | Focused work, meetings with decisions |
| 4:00-6:00 | Administrative | Email, light tasks, planning |
| 12:00-1:00 | Recovery | Lunch, recharge (non-negotiable) |
| 7:00 PM+ | Wind down | Reflection, no work |

### Modes for Different Days

```bash
# Standard (balanced 8-hour day)
/plan-my-day

# High-output (launch week, 10-hour day)
/plan-my-day --mode high-output

# Deep work (IC/creator, max uninterrupted blocks)
/plan-my-day --mode deep-work

# Meeting-heavy (manager/exec, coordination-first)
/plan-my-day --mode coordination
```

## Real Examples

### Example 1: Founder (High-Output Day)

**Top 3:** Launch copy, partner demo, sprint planning

**Result:** ✓ All 3 done. Launch shipped, partner signed, team aligned.

**Key:** Protected 9-11:30am for writing (peak energy).

---

### Example 2: Developer (Deep Work Day)

**Top 3:** Auth refactor PR, debug prod issue, API docs

**Result:** ✓ PR merged, ✓ Issue fixed, ⭐ Docs 90% done

**Key:** Zero meetings. Slack paused. 6+ hours flow state.

---

### Example 3: Manager (Meeting-Heavy Day)

**Top 3:** Exec budget meeting, performance 1-on-1, design reviews

**Result:** ✓ Budget approved, ✓ Performance plan set, ✓ 2/3 reviews done

**Learning:** "Too many back-to-back meetings. Tomorrow: block 2-hour deep work."

## Features

- **Consistent framework** - Top 3 priorities + energy windows + buffers
- **Multiple modes** - Adapt to different day types (deep work, meetings, high-output)
- **Evening reflection** - Track completion, learn what works
- **Break enforcement** - Don't "hope" for breaks, schedule them
- **80% rule** - Only schedule 80% of time (reality needs 20%)
- **Decision framework** - "Is this Top 3?" filter for interruptions
- **No API calls** - Pure planning logic, works offline

## Who This Is For

✅ **Founders/Executives** - Protect focus time amid coordination demands  
✅ **Managers** - Balance team needs with your own priorities  
✅ **Individual Contributors** - Maximize deep work, minimize interruptions  
✅ **Anyone** who wants to execute on priorities instead of reacting  

## How It Works

### 1. Gather Context (30 sec)
- Check calendar for fixed commitments
- Review yesterday's incomplete tasks
- Identify current project priorities

### 2. Identify Top 3 (60 sec)
- Filter by: Impact × Urgency
- Must be completable today
- Move the needle on key goals

### 3. Build Schedule (90 sec)
- Place fixed commitments first
- Assign #1 priority to peak energy (9-11am default)
- Add buffers between blocks (20% total)
- Schedule admin in low-energy windows (4-6pm)
- Protect breaks every 90 minutes

### 4. Evening Check-In (5 min)
- Did you complete Top 3?
- What worked? What got stuck?
- Energy assessment (1-10)
- Adjust tomorrow based on today

## Pro Tips

1. **Run it FIRST thing** - Before email. Set the day, don't react to it.
2. **Block "Focus Time"** - Put 9-11am on your calendar as unavailable.
3. **Track completion** - Evening check-ins show your planning accuracy improving.
4. **Don't over-schedule** - 7 hours of tasks for 8-hour day = realistic.
5. **Combine with shutdown ritual** - Evening check-in + tomorrow's prep = mental closure.

## Common Mistakes

❌ **Planning 100% of your time** - Always leave 20% buffer or you'll fail  
❌ **Hard work at 4pm** - You're tired. Schedule strategically.  
❌ **Skipping breaks** - Performance drops without recovery  
❌ **No evening reflection** - Can't improve without feedback  
❌ **Changing Top 3 mid-day** - Stick to morning priorities unless genuinely urgent  

## Research Foundation

Built on:
- **Circadian rhythm research** (Roenneberg, 2012) - Peak cognition timing
- **Deliberate practice** (Ericsson, 1993) - 90-min focus blocks
- **Decision fatigue** (Kahneman, 2011) - Morning for high-stakes choices
- **Implementation intentions** (Gollwitzer, 1999) - Time+task specificity

## Installation & Usage

```bash
# Install
cp -r plan-my-day $HOME/.openclaw/skills/

# Daily use
/plan-my-day

# Future date
/plan-my-day 2026-03-01

# Custom peak hours (if you're not a morning person)
/plan-my-day --peak 11-13,15-17
```

## What You'll Notice After 2 Weeks

- ✅ Priorities actually get done (not just "busy work")
- ✅ Less decision fatigue (plan once, execute)
- ✅ Protected focus time becomes habit
- ✅ Evening closure replaces work guilt
- ✅ Better energy management (work with your body, not against it)

## Coming Soon

- **Google Calendar integration** - Auto-import existing events
- **Completion analytics** - Track your planning accuracy over time
- **Energy learning** - Adapts to when YOU perform best
- **Team sync** - Coordinate focus blocks across teams

## License

MIT License - Use freely, commercially or personally.

## Contributing

Improvements, modes, or energy pattern data? Submit via GitHub issues.

Built by **theflohart** on circadian research + GTD + deliberate practice principles.

---

**Stop reacting. Start executing.**

**Plan your day in 2 minutes. Protect your peak hours. Win consistently.**
```

## File: `plan-my-day/SKILL-OC.md`
```markdown
---
name: plan-my-day
description: Generate an energy-optimized, time-blocked daily plan based on circadian rhythm research and GTD principles
version: 2.0.0
author: theflohart
tags: [productivity, planning, time-blocking, energy-management, gtd]
---

**Platform:** OpenClaw (token-optimized)

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | Top 3 priorities + rough time blocks | Morning sprint, know the day |
| `standard` | Full hour-by-hour energy-optimized plan | Default daily planning |
| `deep` | Full plan + energy pattern analysis + weekly structure | Overhauling schedule |

## Energy Windows (defaults — customize with `--peak` flag)

| Window | Time | Task Type |
|--------|------|-----------|
| Peak 1 | 9:00–12:00 | Deep work, complex decisions, #1 priority |
| Secondary peak | 14:00–16:00 | Focused work, meetings with decisions |
| Admin | 16:00–18:00 | Email, light tasks, 1-on-1s |
| Recovery | 12:00–13:00, 18:00+ | Meals, walks, recharge |

## Workflow

**1. Gather context (30 sec):**
- Existing calendar events
- Yesterday's incomplete tasks
- Fixed commitments/deadlines
- Current project priorities

**2. Identify Top 3 priorities:**
Filter by: Impact × Urgency. Pick 3 highest-scoring.

**3. Build schedule:**
- Place fixed commitments first
- Priority #1 → longest peak block
- Priority #2 → secondary peak
- Priority #3 → remaining focused time
- Add 20-min buffers between major blocks
- Admin → low-energy windows
- Schedule only 80% of available time (buffer rule)

**Constraints:** No deep work blocks <90 min. Max 4h meetings/day. 15-min break every 90 min.

## Output Format

```markdown
# Daily Plan — [Day], [Date]

## Today's Mission
**Primary Goal:** [One outcome for the day]
**Top 3:** 1. [Priority] 2. [Priority] 3. [Priority]
**Success looks like:** [What "done" means]

---

## Schedule

### [Time block]: [Label]
**Focus:** [Task]
- [ ] [Subtask]
Energy: [Building/Peak/Declining]

[repeat for each block]

---

## Evening Reflection (fill at day's end)
- Completed: [what got done]
- Moved to tomorrow: [what didn't]
- Energy pattern note: [anything to adjust]
```

---
*Skill by theflohart | AI Marketing Skills*
```

## File: `plan-my-day/SKILL.md`
```markdown
---
name: plan-my-day
description: Generate an energy-optimized, time-blocked daily plan based on circadian rhythm research and GTD principles
version: 2.0.0
author: theflohart
tags: [productivity, planning, time-blocking, energy-management, gtd]
---

# Plan My Day

Generate a clean, actionable hour-by-hour plan for the day based on priorities, energy patterns, and constraints.

## Mode

Detect from context or ask: *"Quick priorities, full day plan, or full plan + weekly structure?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | Top 3 priorities + rough time blocks, 2 min | Morning sprint, already know the day |
| `standard` | Full hour-by-hour energy-optimized plan | Default daily planning |
| `deep` | Full plan + energy pattern analysis + weekly structure recommendations | Overhauling your schedule, high-performance week |

**Default: `standard`** — use `quick` if they say "just help me prioritize." Use `deep` if they want to rethink their week, not just plan today.

---

## Why This vs ChatGPT?

**Problem with "just asking":** You get a different plan each time. No consistency, no memory of what works, no optimization over time.

**This skill provides:**
1. **Consistent methodology** - Same decision framework every day (Top 3 priorities, energy windows, buffer rules)
2. **Energy-aware scheduling** - Automatically matches high-cognitive tasks to your peak hours
3. **Constraint-aware** - Respects your existing calendar, energy patterns, personal boundaries
4. **Learning memory** - Can track what scheduling patterns work best for you over time
5. **Evening reflection built-in** - Forces accountability on what actually got done

**You can replicate this** by writing the same detailed prompt every day, manually checking your calendar, remembering your energy patterns, and tracking completion rates. Or use this skill in 2 minutes.

## Usage

```
/plan-my-day [optional: YYYY-MM-DD for future date]
```

With custom energy profile:

```
/plan-my-day --peak 9-11,14-16 --recovery 13-14
```

## Planning Principles (Research-Backed)

1. **Circadian optimization** - Cognitive performance peaks ~2-3 hours after waking (Roenneberg, 2012)
2. **Ultradian rhythms** - Work in 90-minute blocks with 15-20 minute breaks (Ericsson, 1993)
3. **Decision fatigue prevention** - Schedule high-stakes decisions before 3pm (Kahneman, 2011)
4. **Implementation intentions** - Specific time+task combinations increase completion by 2-3× (Gollwitzer, 1999)

## Energy Windows (Default - Customize Yours)

**Peak Performance (Morning):** 9:00 AM - 12:00 PM
- Deep work, strategic thinking, complex problem-solving
- Highest cognitive capacity
- Schedule your #1 priority here

**Secondary Peak (Afternoon):** 2:00 PM - 4:00 PM
- Focused work, meetings with decisions, creative work
- Still high capacity but slightly lower than morning

**Administrative (Late Afternoon):** 4:00 PM - 6:00 PM
- Email processing, light tasks, 1-on-1s, planning
- Lower energy, avoid complex decisions

**Recovery Blocks:** 12:00 PM - 1:00 PM, 6:00 PM+
- Meals, exercise, walks, recharge
- Non-negotiable for sustained performance

**Wind Down (Evening):** After 7:00 PM
- Reflection, reading, light planning for tomorrow
- No high-cognitive work

## Process

### 1. Gather Context (30 seconds)
- Check existing calendar events
- Review yesterday's incomplete tasks
- Identify any fixed commitments or deadlines
- Note current project priorities

### 2. Identify Top 3 Priorities (60 seconds)
Ask for each potential priority:
- **Impact:** Does this move a key metric or deadline?
- **Urgency:** Must it happen today?
- **Effort:** Can I complete it in available time?

**Filter:** Pick the 3 with highest impact×urgency score

### 3. Build Time-Blocked Schedule (90 seconds)
**Sequencing logic:**
1. Place fixed commitments (meetings, calls) first
2. Assign Priority #1 to longest peak energy block
3. Assign Priority #2 to secondary peak or next available
4. Assign Priority #3 to remaining focused time
5. Add 20-minute buffers between major blocks
6. Schedule admin work (email, Slack) in low-energy windows
7. Protect breaks and meals (non-negotiable)

**Buffer rule:** Only schedule 80% of available time

### 4. Apply Constraints
- **Personal boundaries:** No work before 8am or after 7pm (customize)
- **Meeting limits:** Max 4 hours of meetings per day
- **Focus blocks:** Minimum 90 minutes for deep work (no interruptions)
- **Break enforcement:** 15-minute break every 90 minutes

## Output Format

```markdown
# Daily Plan - [Day], [Month] [Date], [Year]

## Today's Mission

**Primary Goal:** [One-sentence outcome for the day]

**Top 3 Priorities:**
1. [Priority 1 with specific, measurable outcome]
2. [Priority 2 with specific, measurable outcome]
3. [Priority 3 with specific, measurable outcome]

**Success looks like:** [What "done" means today]

---

## Time-Blocked Schedule

### 8:00 - 9:00: Morning Prime 🌅
**Focus:** Wake up, coffee, light movement, review plan

- [ ] Morning routine (30 min)
- [ ] Review today's plan + priorities (10 min)
- [ ] Quick inbox scan (15 min - flag only, don't respond)

**Energy level:** Building

---

### 9:00 - 11:00: Deep Work Block 1 🎯 [PRIORITY #1]
**Focus:** [Specific priority 1 task]

- [ ] [Concrete subtask 1]
- [ ] [Concrete subtask 2]
- [ ] [Concrete subtask 3]

**Target:** [Measurable outcome by 11:00]

**Protection:** Phone off, Slack paused, door closed

---

### 11:00 - 11:15: Break ☕
**Focus:** Step away from desk

- Physical movement (walk, stretch)
- Hydrate
- No screens

---

### 11:15 - 12:30: Deep Work Block 2 🎯 [PRIORITY #2]
**Focus:** [Specific priority 2 task]

- [ ] [Concrete subtask 1]
- [ ] [Concrete subtask 2]

**Target:** [Measurable outcome by 12:30]

---

### 12:30 - 1:30: Lunch Break 🍽️
**Focus:** Eat, recharge, disconnect

- Proper meal (not at desk)
- 15-minute walk if possible
- No work talk

**Energy level:** Recovery

---

### 1:30 - 3:00: Focused Work Block 🎯 [PRIORITY #3]
**Focus:** [Specific priority 3 task]

- [ ] [Concrete subtask 1]
- [ ] [Concrete subtask 2]

**Target:** [Measurable outcome by 3:00]

---

### 3:00 - 3:15: Break ☕
**Focus:** Recharge

---

### 3:15 - 4:30: Meetings / Collaborative Work 👥
**Focus:** [Meeting name or collaborative task]

- [ ] [Meeting 1 with agenda]
- [ ] [Follow-up actions from meetings]

**Prep:** Review agendas 10 minutes before

---

### 4:30 - 5:30: Admin & Communication 📧
**Focus:** Process inbox, respond to messages, light tasks

- [ ] Clear email inbox (respond, archive, defer)
- [ ] Slack catch-up and responses
- [ ] Update project trackers
- [ ] Quick wins / small tasks

**Energy level:** Lower (perfect for admin)

---

### 5:30 - 6:00: Planning & Wrap-Up 📋
**Focus:** Close the day, plan tomorrow

- [ ] Evening check-in (see below)
- [ ] Tomorrow's top 3 priorities draft
- [ ] Inbox zero for peace of mind
- [ ] Close all work apps

---

### 6:00 PM+: Personal Time 🏡
**No work beyond this point**

---

## Success Criteria

### Must-Have (Non-Negotiable) ✓
- [ ] Priority 1 complete: [Specific outcome]
- [ ] Priority 2 complete: [Specific outcome]
- [ ] At least 80% progress on Priority 3

### Should-Have (Important) ⭐
- [ ] [Secondary task 1]
- [ ] [Secondary task 2]

### Nice-to-Have (Bonus) 💡
- [ ] [Bonus task 1]
- [ ] [Bonus task 2]

---

## Evening Check-In (5 minutes at 5:30 PM)

**Completion status:**
- Priority 1 done? **YES / NO** - [If no, why?]
- Priority 2 done? **YES / NO** - [If no, why?]
- Priority 3 done? **YES / NO** - [If no, why?]

**What went well:**
[What worked today? What helped you execute?]

**What got stuck:**
[Where did you lose time? What blocked you?]

**Energy assessment:**
- Peak hours productive? **YES / NO**
- Breaks taken? **YES / NO**
- Felt energized or drained? **[Score 1-10]**

**Tomorrow's adjustment:**
[What to change in tomorrow's plan based on today?]

---

## Quick Decision Framework

**Before saying YES to anything today:**

1. **Is this one of my top 3 priorities?**
   - YES → Schedule it in appropriate energy window
   - NO → Go to #2

2. **Does this directly support today's mission?**
   - YES → Add to relevant time block
   - NO → Go to #3

3. **Can this wait until tomorrow?**
   - YES → Add to tomorrow's list
   - NO → Question if it's really urgent

**If NO to all three → Decline or defer**

---
```

## Real Examples

### Example 1: High-Output Day (Founder/Exec)

**Context:** Product launch week, high-stakes demos, team coordination

```markdown
## Top 3 Priorities:
1. Finalize launch announcement (900 words, 3 versions) - DONE by 11:30
2. Run partner demo with clear next steps - DONE by 3:00
3. Team sprint planning with Q2 priorities set - DONE by 5:00

## Schedule:
- 9:00-11:30: Deep work → Launch copy (Priority #1)
- 12:30-2:45: Partner demo prep + execution (Priority #2)
- 3:00-4:45: Sprint planning with team (Priority #3)
- 5:00-5:30: Email/admin/wrap

## Evening Check-In:
✓ Priority 1: YES (shipped 3 versions, CEO approved)
✓ Priority 2: YES (partner committed, contract signed)
✓ Priority 3: YES (team aligned, stories pointed)

What worked: Protected deep work time for writing, prepped demo thoroughly
Tomorrow: Start execution on sprint, less coordination overhead
```

### Example 2: Deep Work Day (Individual Contributor)

**Context:** IC developer, needs 6+ hours of uninterrupted coding

```markdown
## Top 3 Priorities:
1. Ship authentication refactor (PR ready for review) - DONE by 12:00
2. Debug production issue #847 (root cause found + fix deployed) - DONE by 4:00
3. Documentation for new API endpoints (published) - DONE by 6:00

## Schedule:
- 9:00-12:00: Deep work → Auth refactor (Priority #1)
- 1:00-4:00: Deep work → Debug + deploy (Priority #2)
- 4:15-5:45: Documentation writing (Priority #3)
- 5:45-6:00: Update tickets, close day

## Protections:
- Slack: Paused 9am-12pm, 1pm-4pm
- No meetings scheduled
- Phone: DND mode

## Evening Check-In:
✓ Priority 1: YES (PR approved, merged)
✓ Priority 2: YES (issue resolved, monitoring green)
✓ Priority 3: 90% (docs drafted, needs final review tomorrow)

What worked: Zero meetings = maximum flow state
Tomorrow: Finish docs, start new feature work
```

### Example 3: Meeting-Heavy Day (Manager/Director)

**Context:** Leadership role, multiple teams, coordination day

```markdown
## Top 3 Priorities:
1. Align exec team on Q2 budget priorities - DONE by 11:00
2. Resolve team conflict (performance conversation) - DONE by 3:00
3. Approve 3 critical design reviews - DONE by 5:30

## Schedule:
- 8:30-9:00: Pre-meeting prep (agendas, talking points)
- 9:00-11:00: Exec budget meeting (Priority #1)
- 11:15-12:15: 1-on-1 performance conversation (Priority #2)
- 1:30-3:00: Design review meetings (Priority #3, all 3 back-to-back)
- 3:15-4:30: Email/admin/follow-ups from meetings
- 4:30-5:00: Next week prep + team updates

## Evening Check-In:
✓ Priority 1: YES (budget approved, owners assigned)
✓ Priority 2: YES (performance plan agreed, follow-up scheduled)
✓ Priority 3: YES (2 approved, 1 needs revision)

What got stuck: Back-to-back meetings = no thinking time
Tomorrow: Block 2-hour deep work window, fewer meetings
```

## Real Case Study

**User:** Marketing manager at B2B SaaS company, struggled with reactive days

**Before using skill:**
- Average day: 6-8 hours in meetings, 2 hours of "work" squeezed in
- Top priorities rarely completed
- Constant email/Slack interruptions
- 15% weekly goal completion rate
- Felt productive but accomplished little

**After implementing plan-my-day:**
- Used skill every morning (2-3 minutes to generate plan)
- Protected 9-11am deep work block (calendar marked "Focus Time")
- Set clear Top 3 priorities each day
- Added evening check-ins to track completion

**Results after 8 weeks:**
- 74% weekly goal completion rate (+59 points)
- Meetings reduced from 6-8 hrs/day to 3-4 hrs/day
- Deep work blocks protected 4 days/week (vs 0 before)
- Self-reported energy levels: 8.2/10 (vs 4.1/10 before)
- Team feedback: "You're more present and decisive"

**Key insight:** "The daily plan gave me permission to say no. If it wasn't in my Top 3, I deferred it. That one change unlocked everything."

## Configuration Options

### Standard Mode (default)
```
/plan-my-day
```
- Balanced energy windows
- 8-hour workday assumption
- 20% buffer time

### High-Output Mode
```
/plan-my-day --mode high-output
```
- 10-hour workday
- More aggressive scheduling
- 10% buffer time
- Best for: Launch weeks, crunch periods

### Deep Work Mode
```
/plan-my-day --mode deep-work
```
- Maximum uninterrupted blocks
- Minimal meetings
- 30% buffer time
- Best for: Individual contributors, creators

### Meeting-Heavy Mode
```
/plan-my-day --mode coordination
```
- Meeting-first scheduling
- Work blocks fit around commitments
- 25% buffer time
- Best for: Managers, executives, client-facing roles

## Installation

```bash
# Copy skill to your skills directory
cp -r plan-my-day $HOME/.openclaw/skills/

# Verify installation
/plan-my-day --version
```

**No dependencies required** - Pure planning logic.

## Future Integrations (Coming Soon)

- **Google Calendar sync** - Auto-import existing events
- **Completion tracking** - Analytics on your planning accuracy over time
- **Energy pattern learning** - Adapts to when you actually perform best
- **Team coordination** - Sync focus blocks across teams

## Pro Tips

1. **Run it FIRST thing** - Before checking email or Slack. Set the day, don't react to it.
2. **Protect Peak hours** - Block 9-11am as "Focus Time" on your calendar. Decline meetings here.
3. **Track completion rates** - Use evening check-in data to improve your estimations
4. **Adjust energy windows** - Default is 9-11am peak, but if you're different, customize it
5. **Combine with "shutdown ritual"** - Evening check-in + tomorrow's prep = mental closure
6. **Don't over-schedule** - If plan shows 7 hours of tasks for 8-hour day, you're on track

## Common Mistakes to Avoid

❌ **Planning too much** - If you schedule 100% of your time, you'll fail. Always leave 20% buffer.
❌ **Ignoring energy windows** - Putting hard thinking work at 4pm sets you up for failure.
❌ **Skipping breaks** - 90-minute focus blocks REQUIRE 15-minute breaks or performance drops.
❌ **No evening reflection** - Without check-ins, you can't improve your planning accuracy.
❌ **Changing Top 3 mid-day** - Unless genuinely urgent, stick to morning priorities.

## Quality Checklist

A good daily plan has:
- [ ] Clear Top 3 priorities with measurable outcomes
- [ ] #1 priority scheduled in peak energy window
- [ ] 20% buffer time (not every minute scheduled)
- [ ] Breaks scheduled every 90 minutes
- [ ] Protected lunch break (minimum 30 minutes)
- [ ] Evening check-in template included
- [ ] No work scheduled after 7pm (personal time protected)

## Support

Issues or suggestions? Provide:
- Your typical day structure (work hours, meeting load)
- Top 3 priorities example
- Energy pattern (when you're most focused)
- What's not working in current output

---

**Built on circadian rhythm research (Roenneberg), deliberate practice principles (Ericsson), and GTD methodology (Allen).**

**Plan your day in 2 minutes. Execute with focus. Win consistently.**
```

## File: `plan-my-day/_meta.json`
```json
{
  "owner": "itsflow",
  "slug": "plan-my-day",
  "displayName": "Plan My Day",
  "latest": {
    "version": "1.0.0",
    "publishedAt": 1769256787005,
    "commit": "https://github.com/clawdbot/skills/commit/7c8bb9463d8e2fac47577e47fe989f923013a7ab"
  },
  "history": []
}
```

## File: `positioning-basics/SKILL-OC.md`
```markdown
---
name: positioning-basics
description: Help founders and marketers nail their positioning. Use when someone mentions "positioning," "value proposition," "who is this for," "how do I describe my product," "messaging," "ICP," "ideal customer," or is struggling to articulate what makes their product different.
---

**Platform:** OpenClaw (token-optimized)

## Required Inputs (collect before starting)

- Product/service name + what it does (1–2 sentences)
- Current customers — who is actually paying today?
- Alternatives they've tried — what did customers use before?
- Prior positioning attempts — existing copy, pitch, one-liner
- Top 3 competitors — real company names

If none provided → ask. Without real customer data and real competitor names, output will be generic.

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | One-line positioning statement from 5 questions | Elevator pitch, quick clarity |
| `standard` | Full positioning + messaging hierarchy + ICP clarity | Website, sales deck |
| `deep` | Full + competitive differentiation map + messaging matrix | GTM, rebrand |

## Phase 1: Core 5 Questions (all required — no skipping)

Do not output a statement until all 5 have specific answers.

1. **WHO** — named role + situation + company stage + what they use today
2. **WHAT** — the pain + trigger event that makes them act now + cost of doing nothing
3. **HOW** — your actual mechanism (not "we use AI" — what specifically?)
4. **WHY** — your "only we ___" claim (must fail the "could a competitor say this?" test)
5. **SO WHAT** — transformation: Tier 1 = number, Tier 2 = named change, Tier 3 = directional

## Phase 2: Competitive Mapping

Run: `web_search('[Company] competitors alternatives 2026')` if names unknown.

Fill with real company names (no placeholders):

| | You | Competitor A | Competitor B | DIY |
|--|-----|-------------|-------------|-----|
| Best for | | | | |
| Approach | | | | |
| Tradeoff | | | | |
| They win when | | | | |

"They win when" — fill this honestly. Naming it sharpens your position.

## Phase 3: Positioning Statement

**Template:**
```
For [target customer]
who [has this problem/need],
[Product] is a [category]
that [key benefit].
Unlike [named real alternatives],
we [key differentiator].
```

## Phase 4: 5-Check Test (run before delivering)

- [ ] Specific — names a clear customer (not "businesses")
- [ ] Differentiated — says something competitors can't claim
- [ ] Credible — believable based on actual evidence
- [ ] Meaningful — addresses pain they'd pay to fix
- [ ] Memorable — easy to repeat without looking at notes

If any fail → revise → re-run test.

## Self-Critique (required)

- [ ] Used real competitor names, not placeholders?
- [ ] One-liner passes "dinner party test" (non-industry person understands it)?
- [ ] Differentiator is something a competitor CANNOT also say?
- [ ] ICP matches someone real, not a demographic segment?
- [ ] If user had existing copy — does this actually differ from their old framing?

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `positioning-basics/SKILL.md`
```markdown
---
name: positioning-basics
description: Help founders and marketers nail their positioning. Use when someone mentions "positioning," "value proposition," "who is this for," "how do I describe my product," "messaging," "ICP," "ideal customer," or is struggling to articulate what makes their product different.
---

# Positioning Basics

You are a positioning expert. Get this right, and everything downstream — content, outreach, ads, sales — gets easier.

---

## Mode

Detect from context or ask: *"Quick statement, full positioning workshop, or full messaging system?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | One-line positioning statement from 5 core questions | Elevator pitch, bio, quick clarity |
| `standard` | Full positioning with messaging hierarchy and ICP clarity | Website, sales deck, marketing foundation |
| `deep` | Full positioning + competitive differentiation map + messaging matrix | Brand refresh, go-to-market, new market entry |

**Default: `standard`** — use `quick` if they just need a working statement. Use `deep` if they're building a full GTM or rebranding.

---

## Context Loading Gates

Before generating any positioning output, load:

- [ ] **Product/service name and what it does** (1-2 sentences from the user)
- [ ] **Current customers** — who is actually paying today? (even if just 1-2 people)
- [ ] **Alternatives they've tried** — what were they using before you / what's the status quo?
- [ ] **Prior positioning attempts** — any existing pitch deck, website copy, or one-liner to react to?
- [ ] **Top 3 competitors** — real company names, not "other solutions"

If none of this is provided, ask before proceeding. Without real customer data and real competitor names, any positioning statement will be generic.

---

## Phase 1: Core 5 Questions (All Required — No Skipping)

**Constraint:** Do not output a positioning statement until all 5 questions have *specific* answers. If any answer is vague, ask one targeted follow-up.

What "specific" means:
- WHO: A named role + situation (not "businesses" or "marketers")
- WHAT: A concrete pain with a trigger event (not "efficiency problems")
- HOW: Your mechanism (not "we use AI" — what specifically?)
- WHY: An "only we" claim that passes the "could a competitor say this?" test
- SO WHAT: A measurable or named transformation, not "better results"

### 1. WHO is this for?
- Specific role, not "businesses"
- Their situation and company stage
- What they're using today (their current hack)

### 2. WHAT problem do you solve?
- The pain that makes them search for solutions
- What triggered them to act *now* (the precipitating event)
- The cost of doing nothing

### 3. HOW do you solve it?
- Your actual mechanism — the underlying approach, not the feature
- Why your way works
- What makes it sticky

### 4. WHY is this better?
- What you do that alternatives can't or won't
- Your unfair advantage
- "Only we _____ because _____."

### 5. SO WHAT?
- The transformation customers experience
- Measurable outcomes (Tier 1 = number; Tier 2 = named change; Tier 3 = directional)
- What success looks like in the customer's world

---

## Phase 2: Competitive Mapping (Real Names Required)

Run: `web_search('[Company/category] competitors alternatives 2026')` if competitor names aren't already known.

Fill this table with **actual company names** — no placeholders:

| | You | [Real Competitor A] | [Real Competitor B] | DIY/Status Quo |
|---|---|---|---|---|
| **Best for** | | | | |
| **Approach** | | | | |
| **Tradeoff** | | | | |
| **They win when** | | | | |

**Fill in "They win when" honestly.** Every alternative beats you somewhere. Naming it sharpens your position.

**The Positioning Sweet Spot:**
- You clearly win for a specific customer type
- Competitors can't or won't follow you there
- The tradeoff is one your customer gladly makes

---

## Phase 3: Draft Positioning Statement

**Template:**
```
For [target customer]
who [has this problem/need],
[Product] is a [category]
that [key benefit].
Unlike [named real alternatives],
we [key differentiator].
```

**Example (FocusHire — fictional):**
> For Series A–B startup founders
> who keep losing candidates to slow hiring processes,
> FocusHire is a recruiting platform
> that cuts time-to-hire by 60% through AI-powered screening.
> Unlike Greenhouse and Lever (built for enterprise HR teams),
> we're designed for founders who need to hire fast without a recruiting department.

---

## Phase 4: Quick Positioning Test (Run Before Delivering)

Test the positioning statement against these 5 checks. **Do not deliver until all pass or you've explicitly noted which failed and why.**

- [ ] **Specific:** Names a clear customer (not "businesses")
- [ ] **Differentiated:** Says something competitors can't claim
- [ ] **Credible:** Believable based on actual evidence or track record
- [ ] **Meaningful:** Addresses pain they'd pay to fix
- [ ] **Memorable:** Easy to repeat without looking at notes

If a check fails → revise the positioning statement → re-run the test.

---

## Phase 5: Self-Critique Pass (REQUIRED)

After drafting all outputs, evaluate:

- [ ] Did I use real competitor names, or placeholders?
- [ ] Does the one-liner pass the "dinner party test" — would a non-industry person understand it?
- [ ] Is the differentiator something a competitor could also say? (If yes, it's not a differentiator.)
- [ ] Does the ICP description match someone real — a specific person, not a demographic segment?
- [ ] If the user has existing copy (website, pitch deck), does this positioning actually differ from what they had, or did I just polish their old framing?

Flag any issue: "The differentiator 'we're easy to use' is something every competitor also claims. Push for a more specific angle."

---

## Iteration Protocol

After delivering the positioning:
1. Ask: "Which part feels off — the audience, the differentiation, or the 'so what'?"
2. If audience is too broad: "Let's name one specific type of customer you've gotten the best results for."
3. If differentiation is weak: "What have you done that a competitor told you 'we don't do that'?"
4. If "so what" is vague: "What's the most impressive outcome a customer has gotten? Start there."

---

## Output Structure

```markdown
## Positioning: [Product/Company Name] — [Date]

### Positioning Statement
[Full template output]

### One-Liner (≤10 words)
[Text]

### Elevator Pitch (~75 words / 30 seconds)
[Text]

### Key Differentiators
1. Unlike [Competitor A], we [specific differentiator]
2. Unlike [Competitor B], we [specific differentiator]
3. Unlike DIY/status quo, we [specific differentiator]

### Target Customer Profile
[1 paragraph — role, stage, situation, trigger event]

### Competitive Position
[1 sentence "vs" summary using real names]

### Competitive Map
[Table with real competitor names filled in]

### Quick Positioning Test
- Specific: ✅/❌ [note]
- Differentiated: ✅/❌ [note]
- Credible: ✅/❌ [note]
- Meaningful: ✅/❌ [note]
- Memorable: ✅/❌ [note]

### Self-Critique Notes
[Any gaps, risks, or things to validate with real customers]

### Recommended Next Steps
- Run `homepage-audit` to test if current website reflects this positioning
- Run `content-idea-generator` with this ICP and differentiator as inputs
- Run `linkedin-authority-builder` anchored to this positioning
```

---

*Skill by Brian Wagner | AI Marketing Architect | brianrwagner.com*
```

## File: `reddit-insights/README.md`
```markdown
# reddit-insights

Use semantic Reddit search to uncover pain points, sentiment, and market opportunities.

## Best For

- Product idea validation
- Customer voice research
- Content strategy based on real user discussions

## What It Does

- Searches Reddit by meaning, not only keywords
- Surfaces high-signal threads, patterns, and frustrations
- Supports market and positioning analysis

## Install

```bash
mkdir -p "$HOME/.codex/skills"
cp -R reddit-insights "$HOME/.codex/skills/reddit-insights"
```

## Dependency Setup

1. Create API key at `https://reddit-insights.com`
2. Configure `REDDIT_INSIGHTS_API_KEY`
3. Start MCP server with `reddit-insights-mcp`

## Typical Use Cases

- Find recurring complaints in a category
- Compare sentiment across competing tools
- Extract language customers actually use
```

## File: `reddit-insights/SKILL-OC.md`
```markdown
---
name: reddit-insights
description: |
  Search and analyze Reddit content using semantic AI search via reddit-insights.com MCP server.
  Use when you need to: (1) Find user pain points and frustrations for product ideas, (2) Discover niche markets or underserved needs, (3) Research what people really think about products/topics, (4) Find content inspiration from real discussions, (5) Analyze sentiment and trends on Reddit, (6) Validate business ideas with real user feedback.
  Triggers: reddit search, find pain points, market research, user feedback, what do people think about, reddit trends, niche discovery, product validation.
---

**Platform:** OpenClaw (token-optimized)

## Setup

API key from reddit-insights.com → Settings → API

Add to mcporter.json:
```json
{
  "mcpServers": {
    "reddit-insights": {
      "command": "npx reddit-insights-mcp",
      "env": { "REDDIT_INSIGHTS_API_KEY": "your_key" }
    }
  }
}
```

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | 1 query, top 5 insights | Fast pain point check |
| `standard` | 3–5 queries, full synthesis | Product validation, content research |
| `deep` | Multi-angle + sentiment + content angles + competitive intel | Business decisions, campaign strategy |

## Available Tools

| Tool | Purpose |
|------|---------|
| `reddit_search` | Semantic search — natural language query, limit 1–100 |
| `reddit_list_subreddits` | Browse available communities |
| `reddit_get_subreddit` | Subreddit details + recent posts |
| `reddit_get_trends` | Trending topics (latest/today/week/month) |

Performance: 12–25 seconds response time. Best results: specific products, emotional language, comparison questions.

## Workflow

**1. Run queries** (start broad, then narrow):
```
reddit_search: "[topic] problems frustrations"
reddit_search: "[topic] recommendations what worked"
reddit_search: "[topic] vs alternatives"
```

**2. Analyze results:**
- Group by relevance score (0–1)
- Identify recurring themes (3+ mentions = pattern)
- Note highest-upvoted posts and comments
- Tag sentiment: frustration / excitement / skepticism / confusion

**3. Synthesize into output**

## Output Format

```
## Reddit Insights: [Topic] — [Date]

### Top Themes
1. [Theme] — appears in X posts
   Evidence: "[key quote]"
   Subreddits: r/X, r/Y

### Sentiment Analysis
Frustration: [%] | Excitement: [%] | Skepticism: [%]

### Top Pain Points
1. [Pain point + source post]

### Content Opportunities
1. [Angle from real community language]

### Business Insights
[Validated needs, underserved gaps, competitive angles]

### Sources
[Post titles + URLs]
```

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `reddit-insights/SKILL.md`
```markdown
---
name: reddit-insights
description: |
  Search and analyze Reddit content using semantic AI search via reddit-insights.com MCP server.
  Use when you need to: (1) Find user pain points and frustrations for product ideas, (2) Discover niche markets or underserved needs, (3) Research what people really think about products/topics, (4) Find content inspiration from real discussions, (5) Analyze sentiment and trends on Reddit, (6) Validate business ideas with real user feedback.
  Triggers: reddit search, find pain points, market research, user feedback, what do people think about, reddit trends, niche discovery, product validation.
---

# Reddit Insights MCP

Semantic search across millions of Reddit posts. Unlike keyword search, this understands intent and meaning.

## Mode

Detect from context or ask: *"Quick pulse, full research, or strategic intelligence report?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | 1 query, top 5 insights, no synthesis | Fast pain point check, content spark |
| `standard` | 3–5 queries, full synthesis with themes and patterns | Product validation, content research |
| `deep` | Multi-angle research + sentiment analysis + content angles + competitive intelligence | Business decisions, campaign strategy |

**Default: `standard`** — use `quick` for a fast read. Use `deep` if they're validating a product idea or building a content strategy.

---

## Why This vs ChatGPT?

**Problem with ChatGPT:** It has no real-time Reddit access. It can't search current discussions, can't filter by engagement, and can't show you what people are saying RIGHT NOW about your topic.

**This skill provides:**
1. **Live semantic search** - Searches millions of Reddit posts with AI-powered intent matching (not just keywords)
2. **Engagement filtering** - Sort by upvotes/comments to find validated pain points
3. **Sentiment analysis** - Automatically tags posts as Discussion/Q&A/Story/News
4. **Relevance scoring** - Shows 0-1 match score so you know which results matter
5. **Subreddit intelligence** - Browse communities, see trending topics, get recent posts
6. **Direct links** - Every result includes Reddit URL for full context

**You can replicate this** by manually browsing Reddit, searching multiple subreddits, reading hundreds of posts, taking notes, and synthesizing patterns. Takes 1-2 hours per research query. This skill does it in 15-20 seconds.

## Setup

### 1. Get API Key (free tier available)
1. Sign up at https://reddit-insights.com
2. Go to Settings → API
3. Copy your API key

### 2. Install MCP Server

**For Claude Desktop** - add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "reddit-insights": {
      "command": "npx",
      "args": ["-y", "reddit-insights-mcp"],
      "env": {
        "REDDIT_INSIGHTS_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**For Clawdbot** - add to `config/mcporter.json`:
```json
{
  "mcpServers": {
    "reddit-insights": {
      "command": "npx reddit-insights-mcp",
      "env": {
        "REDDIT_INSIGHTS_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Verify installation:**
```bash
mcporter list reddit-insights
```

## Available Tools

| Tool | Purpose | Key Params |
|------|---------|------------|
| `reddit_search` | Semantic search across posts | `query` (natural language), `limit` (1-100) |
| `reddit_list_subreddits` | Browse available subreddits | `page`, `limit`, `search` |
| `reddit_get_subreddit` | Get subreddit details + recent posts | `subreddit` (without r/) |
| `reddit_get_trends` | Get trending topics | `filter` (latest/today/week/month), `category` |

## Performance Notes

- **Response time:** 12-25 seconds (varies by query complexity)
  - Simple queries: ~12-15s
  - Complex semantic queries: ~17-20s
  - Heavy load periods: up to 25s
- **Best results:** Specific products, emotional language, comparison questions
- **Weaker results:** Abstract concepts, non-English queries, generic business terms
- **Sweet spot:** Questions a real person would ask on Reddit

## Best Use Cases (Tested)

| Use Case | Effectiveness | Why |
|----------|--------------|-----|
| Product comparisons (A vs B) | ⭐⭐⭐⭐⭐ | Reddit loves debates |
| Tool/app recommendations | ⭐⭐⭐⭐⭐ | High-intent discussions |
| Side hustle/money topics | ⭐⭐⭐⭐⭐ | Engaged communities |
| Pain point discovery | ⭐⭐⭐⭐ | Emotional posts rank well |
| Health questions | ⭐⭐⭐⭐ | Active health subreddits |
| Technical how-to | ⭐⭐⭐ | Better to search specific subreddits |
| Abstract market research | ⭐⭐ | Too vague for semantic search |
| Non-English queries | ⭐ | Reddit is English-dominant |

## Query Strategies (Tested with Real Data)

### ✅ Excellent Queries (relevance 0.70+)

**Product Comparisons** (best results!):
```
"Notion vs Obsidian for note taking which one should I use"
→ Relevance: 0.72-0.81 | Found: Detailed comparison discussions, user experiences

"why I switched from Salesforce to HubSpot honest experience"  
→ Relevance: 0.70-0.73 | Found: Migration stories, feature comparisons
```

**Side Hustle/Money Topics:**
```
"side hustle ideas that actually make money not scams"
→ Relevance: 0.70-0.77 | Found: Real experiences, specific suggestions
```

**Niche App Research:**
```
"daily horoscope apps which one is accurate and why"
→ Relevance: 0.67-0.72 | Found: App recommendations, feature requests
```

### ✅ Good Queries (relevance 0.60-0.69)

**Pain Point Discovery:**
```
"I hate my current CRM it is so frustrating"
→ Relevance: 0.60-0.64 | Found: Specific CRM complaints, feature wishlists

"cant sleep at night tried everything what actually works"
→ Relevance: 0.60-0.63 | Found: Sleep remedies discussions, medical advice seeking
```

**Tool Evaluation:**
```
"AI tools that actually save time not just hype"
→ Relevance: 0.64-0.65 | Found: Real productivity gains, tool recommendations
```

### ❌ Weak Queries (avoid these patterns)

**Too Abstract:**
```
"business opportunity growth potential"
→ Relevance: 0.52-0.58 | Returns unrelated generic posts
```

**Non-English:**
```
"学习编程最好的方法" (Chinese)
→ Relevance: 0.45-0.51 | Reddit is English-dominant, poor cross-lingual results
```

### Query Formula Cheat Sheet

| Goal | Pattern | Relevance |
|------|---------|-----------|
| Compare products | "[Product A] vs [Product B] which should I use" | 0.70-0.81 |
| Find switchers | "why I switched from [A] to [B]" | 0.70-0.73 |
| Money/hustle topics | "[topic] that actually [works/makes money] not [scam/hype]" | 0.70-0.77 |
| App recommendations | "[category] apps which one is [accurate/best] and why" | 0.67-0.72 |
| Pain points | "I hate my current [tool] it is so [frustrating/slow]" | 0.60-0.64 |
| Solutions seeking | "[problem] tried everything what actually works" | 0.60-0.63 |

## Response Fields

Each result includes:
- `title`, `content` - Post text
- `subreddit` - Source community  
- `upvotes`, `comments` - Engagement metrics
- `relevance` (0-1) - Semantic match score (0.5+ is good, 0.6+ is strong)
- `sentiment` - Discussion/Q&A/Story Sharing/Original Content/News
- `url` - Direct Reddit link

**Example response:**
```json
{
  "id": "1oecf5e",
  "title": "Trying to solve the productivity stack problem",
  "content": "The perfect productivity app doesn't exist. No single app can do everything well, so we use a stack of apps. But this creates another problem: multi app fragmentation...",
  "subreddit": "productivityapps",
  "upvotes": 1,
  "comments": 0,
  "relevance": 0.631,
  "sentiment": "Discussion",
  "url": "https://reddit.com/r/productivityapps/comments/1oecf5e"
}
```

## Real Case Study

**User:** SaaS founder validating a new project management tool idea

**Challenge:** Needed to understand real frustrations with existing PM tools (Asana, Monday, ClickUp) to find positioning angle.

**Research Query:**
```
reddit_search("I hate my project management tool it's so frustrating for remote teams", limit=50)
```

**What They Found (in 18 seconds):**
- **42 posts** with 0.60+ relevance
- **Top pain points** (mentioned 15+ times):
  - "Too complicated for simple projects"
  - "Mobile app is terrible"
  - "Hard to see the big picture"
  - "Notifications are overwhelming"
  - "Pricing jumps too fast with team size"

**Most upvoted insight** (+347 upvotes, r/startups):
> "We switched from Monday to a Notion template because Monday felt like learning a new language just to assign a task. Sometimes simple beats powerful."

**Positioning Decision:**
Built messaging around: **"Project management that feels like a shared doc, not enterprise software."**

**Product Changes Made:**
- Simplified onboarding (3 clicks to first task vs 15-step wizard)
- Mobile-first design (every feature tested on phone first)
- Flat pricing ($8/user, no tiers)
- Big-picture dashboard view (Gantt hidden by default)

**Results (6 months post-launch):**
- 2,400 paying users
- 78% came from "Reddit research-informed" messaging
- 4.7/5 rating on G2 with reviews saying "finally, PM without the bloat"
- Founder quote: "That one Reddit search saved us from building features nobody wanted."

## Tips

1. **Natural language works best** - Ask questions like a human would
2. **Include context** - "for small business" or "as a developer" improves results
3. **Combine emotion words** - "frustrated", "love", "hate", "wish" find stronger opinions
4. **Filter by engagement** - High upvotes/comments = validated pain points
5. **Check multiple subreddits** - Same topic discussed differently in r/startups vs r/smallbusiness
6. **Use comparison queries** - "X vs Y" consistently returns high-relevance results
7. **Search for stories** - "why I switched" and "honest experience" reveal real user journeys

## Example Workflows

**Find SaaS opportunity:**
1. `reddit_search`: "frustrated with project management tools for remote teams"
2. Filter results with high engagement (20+ upvotes or 10+ comments)
3. Identify recurring complaints → product opportunity
4. Export top 10 posts to analyze language patterns for messaging

**Validate idea:**
1. `reddit_search`: "[your product category] recommendations"
2. See what alternatives people mention
3. Note gaps in existing solutions
4. Check `reddit_get_subreddit` for relevant communities to monitor

**Content research:**
1. `reddit_get_subreddit`: Get posts from target community
2. `reddit_search`: Find specific questions/discussions with high engagement
3. Create content answering real user questions (with examples from Reddit)
4. Post back to Reddit (with value, not spam)

**Competitive intelligence:**
1. `reddit_search`: "[competitor name] experience"
2. `reddit_search`: "switched from [competitor] to [other]"
3. Extract feature complaints and praise
4. Build comparison matrix based on real feedback

## Pro Tips

**For Product Research:**
- Search for "I wish [category] had..." to find feature requests
- Filter by comments (not just upvotes) to find discussion-heavy threads
- Look for posts from 30-90 days ago (recent but with accumulated discussion)

**For Content Ideas:**
- Search your topic + "explained" or "guide"
- Check what questions have 0-2 replies (content gaps!)
- Save high-upvote posts and create better answers

**For Market Validation:**
- Run the same search monthly to track sentiment trends
- Compare subreddit sizes (r/notion has 180K vs r/obsidianmd 90K)
- Watch for "migration posts" ("leaving X for Y") as early signals

## Quality Indicators

A good Reddit Insights search has:
- [ ] Relevance scores mostly 0.60+ (strong semantic match)
- [ ] Results from 3+ different subreddits (diverse perspectives)
- [ ] Mix of high engagement (100+ upvotes) and niche discussions
- [ ] Clear patterns across multiple posts (not one-off opinions)
- [ ] Recent posts (<90 days) mixed with classic threads

## Common Mistakes to Avoid

❌ **Being too generic** - "marketing tips" returns weak results; "B2B cold email that actually works" is better
❌ **Ignoring engagement metrics** - A post with 2 upvotes is one person's opinion; 200+ upvotes is validated
❌ **Taking single posts as truth** - Look for patterns across 5-10 posts minimum
❌ **Forgetting to check sentiment** - A "Discussion" post is different from a "Q&A" (check the field!)
❌ **Not visiting actual threads** - The semantic summary is great, but top comments often have gold

---

**Built on semantic AI search (not keyword matching).**
**Find what people REALLY think. Not what marketing says they think.**
```

## File: `scripts/convert.sh`
```bash
#!/usr/bin/env bash
# convert.sh — Convert SKILL.md files to platform-specific formats
#
# Usage:
#   ./scripts/convert.sh --platform=cursor [--output-dir=./output] [--include-pro] [--dry-run]
#   ./scripts/convert.sh --platform=windsurf
#   ./scripts/convert.sh --platform=claude   # copies as-is
#   ./scripts/convert.sh --platform=openclaw # copies as-is
#   ./scripts/convert.sh --all               # all platforms into ./converted/

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Colors
BOLD='\033[1m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
DIM='\033[2m'
RESET='\033[0m'

# Defaults
PLATFORM=""
OUTPUT_DIR=""
INCLUDE_PRO=false
DRY_RUN=false
CONVERT_ALL=false

usage() {
  echo ""
  echo -e "${BOLD}convert.sh${RESET} — Convert SKILL.md files to platform-specific formats"
  echo ""
  echo "Usage:"
  echo "  ./scripts/convert.sh --platform=<platform> [options]"
  echo ""
  echo "Platforms:"
  echo "  claude    — Copy as-is (.md, no conversion needed)"
  echo "  openclaw  — Copy as-is (.md, no conversion needed)"
  echo "  cursor    — Convert to .mdc with Cursor rule frontmatter"
  echo "  windsurf  — Convert to .md with Windsurf rule frontmatter"
  echo ""
  echo "Options:"
  echo "  --output-dir=PATH   Output directory (default: ./converted/<platform>)"
  echo "  --include-pro       Include pro/ skills"
  echo "  --all               Convert for all platforms"
  echo "  --dry-run           Preview without writing files"
  echo ""
  exit 0
}

# Parse args
for arg in "$@"; do
  case "$arg" in
    --platform=*) PLATFORM="${arg#--platform=}" ;;
    --output-dir=*) OUTPUT_DIR="${arg#--output-dir=}" ;;
    --include-pro) INCLUDE_PRO=true ;;
    --dry-run) DRY_RUN=true ;;
    --all) CONVERT_ALL=true ;;
    --help|-h) usage ;;
  esac
done

if [ -z "$PLATFORM" ] && [ "$CONVERT_ALL" = false ]; then
  echo -e "${RED}Error:${RESET} --platform=<platform> or --all required"
  usage
fi

# Parse YAML frontmatter field (handles inline, quoted, and block scalars | >)
get_field() {
  local file="$1"
  local field="$2"
  awk -v field="$field" '
    BEGIN { in_front=0; collecting=0; buf="" }
    /^---/ { in_front++; next }
    in_front == 1 {
      if (collecting) {
        if ($0 ~ /^[[:space:]]/) {
          gsub(/^[[:space:]]+/, "")
          buf = (buf == "") ? $0 : buf " " $0
        } else {
          collecting=0; print buf; exit
        }
      } else if ($0 ~ "^" field ":") {
        sub("^" field ":[[:space:]]*", "")
        gsub(/^["\x27]|["\x27]$/, "")
        if ($0 == "|" || $0 == ">") {
          collecting=1; buf=""
        } else {
          print; exit
        }
      }
    }
    END { if (collecting && buf != "") print buf }
  ' "$file"
}

# Strip YAML frontmatter from a file, return body only
get_body() {
  local file="$1"
  awk '
    BEGIN { in_front=0; past=0 }
    /^---/ {
      in_front++
      if (in_front == 2) { past=1; next }
      next
    }
    past { print }
  ' "$file"
}

convert_for_platform() {
  local platform="$1"
  local out_dir="$2"
  local converted=0
  local skipped=0

  echo ""
  echo -e "${BOLD}Converting for: ${CYAN}${platform}${RESET}"
  echo -e "${DIM}Output: ${out_dir}${RESET}"
  echo ""

  if [ "$DRY_RUN" = false ]; then
    mkdir -p "$out_dir"
  fi

  convert_skill() {
    local skill_file="$1"
    local skill_dir
    skill_dir="$(dirname "$skill_file")"
    local skill_name
    skill_name="$(basename "$skill_dir")"
    local is_pro="$2"

    local name
    name="$(get_field "$skill_file" "name")"
    [ -z "$name" ] && name="$skill_name"

    local description
    description="$(get_field "$skill_file" "description")"

    local dest_subdir="$out_dir"
    if [ "$is_pro" = true ]; then
      dest_subdir="$out_dir/pro"
    fi

    case "$platform" in
      claude|openclaw)
        local dest_file="$dest_subdir/$skill_name/SKILL.md"
        if [ "$DRY_RUN" = true ]; then
          echo -e "  ${DIM}[dry-run]${RESET} ${skill_name} → ${dest_file}"
        else
          mkdir -p "$(dirname "$dest_file")"
          cp "$skill_file" "$dest_file"
          echo -e "  ${GREEN}✓${RESET} $skill_name"
        fi
        ;;

      cursor)
        local dest_file="$dest_subdir/${skill_name}.mdc"
        local frontmatter
        frontmatter="---
description: ${description}
globs:
alwaysApply: false
---"
        local body
        body="$(get_body "$skill_file")"
        if [ "$DRY_RUN" = true ]; then
          echo -e "  ${DIM}[dry-run]${RESET} ${skill_name}.mdc → ${dest_file}"
        else
          mkdir -p "$dest_subdir"
          printf '%s\n%s' "$frontmatter" "$body" > "$dest_file"
          echo -e "  ${GREEN}✓${RESET} ${skill_name}.mdc"
        fi
        ;;

      windsurf)
        local dest_file="$dest_subdir/${skill_name}.md"
        local frontmatter
        frontmatter="---
trigger: always_on
description: ${description}
---"
        local body
        body="$(get_body "$skill_file")"
        if [ "$DRY_RUN" = true ]; then
          echo -e "  ${DIM}[dry-run]${RESET} ${skill_name}.md → ${dest_file}"
        else
          mkdir -p "$dest_subdir"
          printf '%s\n%s' "$frontmatter" "$body" > "$dest_file"
          echo -e "  ${GREEN}✓${RESET} ${skill_name}.md"
        fi
        ;;

      *)
        echo -e "${RED}Unknown platform:${RESET} $platform"
        return 1
        ;;
    esac

    (( converted++ )) || true
  }

  # Free skills
  for skill_file in "$REPO_DIR"/*/SKILL.md; do
    [ -f "$skill_file" ] || continue
    local skill_dir
    skill_dir="$(dirname "$skill_file")"
    local skill_name
    skill_name="$(basename "$skill_dir")"
    [[ "$skill_name" == "scripts" || "$skill_name" == "pro" ]] && continue
    convert_skill "$skill_file" false
  done

  # Pro skills
  if [ "$INCLUDE_PRO" = true ] && [ -d "$REPO_DIR/pro" ]; then
    for skill_file in "$REPO_DIR"/pro/*/SKILL.md; do
      [ -f "$skill_file" ] || continue
      convert_skill "$skill_file" true
    done
  fi

  echo ""
  echo -e "  ${GREEN}${converted} files converted${RESET}"
}

PLATFORMS_TO_CONVERT=()
if [ "$CONVERT_ALL" = true ]; then
  PLATFORMS_TO_CONVERT=(claude openclaw cursor windsurf)
else
  PLATFORMS_TO_CONVERT=("$PLATFORM")
fi

for p in "${PLATFORMS_TO_CONVERT[@]}"; do
  if [ -z "$OUTPUT_DIR" ]; then
    out_dir="$REPO_DIR/converted/$p"
  else
    out_dir="$OUTPUT_DIR/$p"
  fi
  convert_for_platform "$p" "$out_dir"
done

echo -e "${BOLD}${CYAN}Done.${RESET}"
echo ""
```

## File: `scripts/install.sh`
```bash
#!/usr/bin/env bash
# install.sh — Multi-platform installer for AI Marketing Skills
#
# Dual-file system:
#   SKILL.md    → Claude Code, Cursor, Windsurf (full detail, all phases)
#   SKILL-OC.md → OpenClaw (token-efficient, ~200 lines) — falls back to SKILL.md if not yet available
#
# Usage:
#   ./scripts/install.sh                         # auto-detect + interactive
#   ./scripts/install.sh --all                   # install to all detected platforms
#   ./scripts/install.sh --platform=claude       # specific platform
#   ./scripts/install.sh --platform=openclaw
#   ./scripts/install.sh --platform=cursor
#   ./scripts/install.sh --platform=windsurf
#   ./scripts/install.sh --platform=generic
#   ./scripts/install.sh --include-pro           # also install pro/ skills (if present locally)
#   ./scripts/install.sh --dry-run               # preview without writing files

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ── Colors ────────────────────────────────────────────────────────────────────
BOLD='\033[1m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
DIM='\033[2m'
RESET='\033[0m'

# ── Defaults ──────────────────────────────────────────────────────────────────
PLATFORM_ARG=""
INCLUDE_PRO=false
DRY_RUN=false
INSTALL_ALL=false

# ── Parse flags ───────────────────────────────────────────────────────────────
for arg in "$@"; do
  case "$arg" in
    --platform=*) PLATFORM_ARG="${arg#--platform=}" ;;
    --include-pro) INCLUDE_PRO=true ;;
    --dry-run) DRY_RUN=true ;;
    --all) INSTALL_ALL=true ;;
    --help|-h)
      echo ""
      echo -e "${BOLD}AI Marketing Skills — Installer${RESET}"
      echo ""
      echo "Usage: ./scripts/install.sh [options]"
      echo ""
      echo "Options:"
      echo "  --platform=<name>  Target platform: claude | openclaw | cursor | windsurf | generic"
      echo "  --all              Install to all detected platforms"
      echo "  --include-pro      Include pro/ skills (requires local copies from Gumroad)"
      echo "  --dry-run          Preview installs without writing files"
      echo "  --help             Show this help"
      echo ""
      exit 0
      ;;
  esac
done

# ── Platform detection ────────────────────────────────────────────────────────
detect_platforms() {
  DETECTED=()

  # Claude Code: binary on PATH or ~/.claude/ dir exists
  if command -v claude &>/dev/null || [ -d "$HOME/.claude" ]; then
    DETECTED+=("claude")
  fi

  # OpenClaw: ~/.openclaw/ dir exists
  if [ -d "$HOME/.openclaw" ]; then
    DETECTED+=("openclaw")
  fi

  # Cursor: .cursor/ in current working directory
  if [ -d "$(pwd)/.cursor" ]; then
    DETECTED+=("cursor")
  fi

  # Windsurf: .windsurf/ in current working directory
  if [ -d "$(pwd)/.windsurf" ]; then
    DETECTED+=("windsurf")
  fi
}

# ── Install destination for each platform ─────────────────────────────────────
platform_dest() {
  local platform="$1"
  case "$platform" in
    claude)
      # Prefer ~/.claude/skills/, fall back to ~/.claude/agents/
      if [ -d "$HOME/.claude/skills" ]; then
        echo "$HOME/.claude/skills"
      elif [ -d "$HOME/.claude/agents" ]; then
        echo "$HOME/.claude/agents"
      else
        echo "$HOME/.claude/skills"
      fi
      ;;
    openclaw)  echo "$HOME/.openclaw/skills" ;;
    cursor)    echo "$(pwd)/.cursor/rules" ;;
    windsurf)  echo "$(pwd)/.windsurf/rules" ;;
    generic)   echo "$(pwd)/ai-marketing-skills" ;;
  esac
}

# ── Source file selection (dual-file system) ──────────────────────────────────
# Claude Code / Cursor / Windsurf / generic → SKILL.md
# OpenClaw → SKILL-OC.md (fallback to SKILL.md if SKILL-OC.md not present)
select_source() {
  local skill_dir="$1"
  local platform="$2"

  if [ "$platform" = "openclaw" ]; then
    if [ -f "$skill_dir/SKILL-OC.md" ]; then
      echo "$skill_dir/SKILL-OC.md"
    else
      echo "$skill_dir/SKILL.md"
    fi
  else
    echo "$skill_dir/SKILL.md"
  fi
}

# ── Parse YAML frontmatter field (handles inline, quoted, and block scalars | >) ──
get_field() {
  local file="$1"
  local field="$2"
  awk -v field="$field" '
    BEGIN { in_front=0; collecting=0; buf="" }
    /^---/ { in_front++; next }
    in_front == 1 {
      if (collecting) {
        if ($0 ~ /^[[:space:]]/) {
          gsub(/^[[:space:]]+/, "")
          buf = (buf == "") ? $0 : buf " " $0
        } else {
          collecting=0; print buf; exit
        }
      } else if ($0 ~ "^" field ":") {
        sub("^" field ":[[:space:]]*", "")
        gsub(/^["\x27]|["\x27]$/, "")
        if ($0 == "|" || $0 == ">") {
          collecting=1; buf=""
        } else {
          print; exit
        }
      }
    }
    END { if (collecting && buf != "") print buf }
  ' "$file"
}

# Strip YAML frontmatter, return body only
get_body() {
  local file="$1"
  awk '
    BEGIN { in_front=0; past=0 }
    /^---/ {
      in_front++
      if (in_front == 2) { past=1; next }
      next
    }
    past { print }
  ' "$file"
}

# ── Install one skill to a platform ──────────────────────────────────────────
install_skill() {
  local skill_dir="$1"
  local platform="$2"
  local dest_base="$3"
  local is_pro="${4:-false}"

  local skill_name
  skill_name="$(basename "$skill_dir")"

  # Get correct source file for this platform
  local source_file
  source_file="$(select_source "$skill_dir" "$platform")"

  [ -f "$source_file" ] || return 0  # skip if no SKILL.md at all

  local source_variant
  source_variant="$(basename "$source_file")"

  # Pro skills go in a sub-folder
  local install_base="$dest_base"
  if [ "$is_pro" = true ]; then
    install_base="$dest_base/pro"
  fi

  local fallback_note=""
  if [ "$platform" = "openclaw" ] && [ "$source_variant" = "SKILL.md" ]; then
    fallback_note="${DIM} (SKILL-OC.md not found, using SKILL.md)${RESET}"
  fi

  case "$platform" in
    claude|openclaw|generic)
      local dest_dir="$install_base/$skill_name"
      local dest_file="$dest_dir/SKILL.md"
      if [ "$DRY_RUN" = true ]; then
        echo -e "  ${DIM}[dry-run]${RESET} $skill_name → $dest_file${fallback_note}"
      else
        mkdir -p "$dest_dir"
        cp "$source_file" "$dest_file"
        echo -e "  ${GREEN}✓${RESET} $skill_name${fallback_note}"
      fi
      ;;

    cursor)
      local description
      description="$(get_field "$source_file" "description")"
      local frontmatter="---
description: ${description}
globs:
alwaysApply: false
---"
      local body
      body="$(get_body "$source_file")"
      local dest_file="$install_base/${skill_name}.mdc"
      if [ "$DRY_RUN" = true ]; then
        echo -e "  ${DIM}[dry-run]${RESET} ${skill_name}.mdc → $dest_file"
      else
        mkdir -p "$install_base"
        printf '%s\n%s' "$frontmatter" "$body" > "$dest_file"
        echo -e "  ${GREEN}✓${RESET} ${skill_name}.mdc"
      fi
      ;;

    windsurf)
      local description
      description="$(get_field "$source_file" "description")"
      local frontmatter="---
trigger: always_on
description: ${description}
---"
      local body
      body="$(get_body "$source_file")"
      local dest_file="$install_base/${skill_name}.md"
      if [ "$DRY_RUN" = true ]; then
        echo -e "  ${DIM}[dry-run]${RESET} ${skill_name}.md → $dest_file"
      else
        mkdir -p "$install_base"
        printf '%s\n%s' "$frontmatter" "$body" > "$dest_file"
        echo -e "  ${GREEN}✓${RESET} ${skill_name}.md"
      fi
      ;;
  esac
}

# ── Install all skills to a single platform ───────────────────────────────────
install_to_platform() {
  local platform="$1"
  local dest
  dest="$(platform_dest "$platform")"

  local count=0
  local pro_count=0

  echo ""
  echo -e "${BOLD}Installing → ${CYAN}${platform}${RESET}"
  echo -e "${DIM}Destination: ${dest}${RESET}"
  echo ""

  if [ "$DRY_RUN" = false ]; then
    mkdir -p "$dest"
  fi

  # Free skills
  for skill_dir in "$REPO_DIR"/*/; do
    [ -d "$skill_dir" ] || continue
    local skill_name
    skill_name="$(basename "$skill_dir")"
    # Skip non-skill dirs
    [[ "$skill_name" == "scripts" || "$skill_name" == "pro" || "$skill_name" == "converted" ]] && continue
    [ -f "$skill_dir/SKILL.md" ] || continue

    install_skill "$skill_dir" "$platform" "$dest" false
    (( count++ )) || true
  done

  # Pro skills
  if [ "$INCLUDE_PRO" = true ]; then
    if [ -d "$REPO_DIR/pro" ]; then
      local pro_dest="$dest/pro"
      for skill_dir in "$REPO_DIR"/pro/*/; do
        [ -d "$skill_dir" ] || continue
        [ -f "$skill_dir/SKILL.md" ] || continue
        install_skill "$skill_dir" "$platform" "$dest" true
        (( pro_count++ )) || true
      done
    else
      echo -e "  ${YELLOW}⚠${RESET}  No pro/ directory found. Purchase from brianrwagner.gumroad.com first."
    fi
  fi

  echo ""
  local summary="${GREEN}${count} free skills${RESET}"
  if [ "$INCLUDE_PRO" = true ] && [ "$pro_count" -gt 0 ]; then
    summary="$summary + ${YELLOW}${pro_count} pro skills${RESET}"
  fi
  echo -e "  Installed: $summary"
  echo -e "  ${DIM}Path: ${dest}${RESET}"
}

# ── Main ──────────────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo -e "${BOLD}  AI Marketing Skills — Installer${RESET}"
[ "$DRY_RUN" = true ] && echo -e "${YELLOW}  DRY RUN — no files will be written${RESET}"
echo -e "${BOLD}${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"

# ── Platform selection ────────────────────────────────────────────────────────
PLATFORMS_TO_INSTALL=()

if [ -n "$PLATFORM_ARG" ]; then
  # Explicit platform flag
  PLATFORMS_TO_INSTALL=("$PLATFORM_ARG")
elif [ "$INSTALL_ALL" = true ]; then
  detect_platforms
  PLATFORMS_TO_INSTALL=("${DETECTED[@]}")
  if [ "${#PLATFORMS_TO_INSTALL[@]}" -eq 0 ]; then
    echo -e "\n${YELLOW}No platforms detected. Running in generic mode.${RESET}"
    PLATFORMS_TO_INSTALL=("generic")
  fi
else
  # Interactive: detect and let user choose
  detect_platforms

  echo ""
  echo -e "${BOLD}Detected platforms:${RESET}"
  if [ "${#DETECTED[@]}" -eq 0 ]; then
    echo -e "  ${DIM}None detected. Will use generic install.${RESET}"
    DETECTED=("generic")
  else
    for p in "${DETECTED[@]}"; do
      echo -e "  ${GREEN}✓${RESET} $p  ${DIM}(→ $(platform_dest "$p"))${RESET}"
    done
  fi

  echo ""
  if [ "${#DETECTED[@]}" -gt 1 ]; then
    echo -e "${BOLD}Install to:${RESET} [all] / $(IFS='|'; echo "${DETECTED[*]}") / or enter a number"
    echo ""
    i=1
    for p in "${DETECTED[@]}"; do
      echo "  $i) $p"
      (( i++ )) || true
    done
    echo "  $i) all"
    echo ""
    read -rp "Choice [all]: " choice
    choice="${choice:-all}"

    if [[ "$choice" =~ ^[0-9]+$ ]]; then
      if [ "$choice" -le "${#DETECTED[@]}" ]; then
        PLATFORMS_TO_INSTALL=("${DETECTED[$((choice-1))]}")
      else
        PLATFORMS_TO_INSTALL=("${DETECTED[@]}")
      fi
    elif [ "$choice" = "all" ]; then
      PLATFORMS_TO_INSTALL=("${DETECTED[@]}")
    else
      PLATFORMS_TO_INSTALL=("$choice")
    fi
  else
    PLATFORMS_TO_INSTALL=("${DETECTED[@]}")
  fi

  # Pro skills prompt (only in interactive mode)
  if [ "$INCLUDE_PRO" = false ]; then
    echo ""
    if [ -d "$REPO_DIR/pro" ]; then
      echo -e "${YELLOW}Pro skills found locally.${RESET} Install pro/ skills too? [y/N]: "
      read -rp "" pro_choice
      pro_choice="${pro_choice:-N}"
      [[ "$pro_choice" =~ ^[Yy]$ ]] && INCLUDE_PRO=true
    else
      echo -e "${DIM}Pro skills: not found locally. Purchase at brianrwagner.gumroad.com${RESET}"
    fi
  fi
fi

# ── Run installs ──────────────────────────────────────────────────────────────
for platform in "${PLATFORMS_TO_INSTALL[@]}"; do
  install_to_platform "$platform"
done

# ── Final summary ─────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo -e "${BOLD}  Done!${RESET}"
echo -e "${DIM}  Tip: Re-run with --dry-run to preview changes anytime${RESET}"
echo -e "${BOLD}${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo ""
```

## File: `scripts/list-skills.sh`
```bash
#!/usr/bin/env bash
# list-skills.sh — List all available AI Marketing Skills with name, description, and tier

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Colors
BOLD='\033[1m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
DIM='\033[2m'
RESET='\033[0m'

# Parse YAML frontmatter field from a SKILL.md file
# Handles inline values, quoted values, and block scalars (|, >)
get_field() {
  local file="$1"
  local field="$2"
  awk -v field="$field" '
    BEGIN { in_front=0; collecting=0; buf="" }
    /^---/ { in_front++; next }
    in_front == 1 {
      if (collecting) {
        if ($0 ~ /^[[:space:]]/) {
          gsub(/^[[:space:]]+/, "")
          buf = (buf == "") ? $0 : buf " " $0
        } else {
          collecting=0; print buf; exit
        }
      } else if ($0 ~ "^" field ":") {
        sub("^" field ":[[:space:]]*", "")
        gsub(/^["\x27]|["\x27]$/, "")
        if ($0 == "|" || $0 == ">") {
          collecting=1; buf=""
        } else {
          print; exit
        }
      }
    }
    END { if (collecting && buf != "") print buf }
  ' "$file"
}

print_skill() {
  local skill_file="$1"
  local tier="$2"
  local skill_dir
  skill_dir="$(dirname "$skill_file")"
  local skill_name
  skill_name="$(basename "$skill_dir")"

  local name
  name="$(get_field "$skill_file" "name")"
  [ -z "$name" ] && name="$skill_name"

  local description
  description="$(get_field "$skill_file" "description")"
  [ -z "$description" ] && description="(no description)"

  if [ "$tier" = "PRO" ]; then
    local price
    price="$(get_field "$skill_file" "price")"
    local tier_label
    if [ -n "$price" ]; then
      tier_label="${YELLOW}PRO ${price}${RESET}"
    else
      tier_label="${YELLOW}PRO${RESET}"
    fi
  else
    tier_label="${GREEN}FREE${RESET}"
  fi

  echo -e "  ${BOLD}${name}${RESET}  [${tier_label}]"
  echo -e "  ${DIM}${description:0:120}${RESET}"
  echo ""
}

echo ""
echo -e "${BOLD}${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo -e "${BOLD}  AI Marketing Skills${RESET}"
echo -e "${DIM}  github.com/BrianRWagner/ai-marketing-claude-code-skills${RESET}"
echo -e "${BOLD}${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo ""

# Free skills
echo -e "${BOLD}FREE SKILLS${RESET}"
echo -e "${DIM}─────────────────────────────────────────────────────────${RESET}"

free_count=0
for skill_file in "$REPO_DIR"/*/SKILL.md; do
  [ -f "$skill_file" ] || continue
  skill_dir="$(dirname "$skill_file")"
  skill_name="$(basename "$skill_dir")"
  # Skip non-skill directories
  [[ "$skill_name" == "scripts" || "$skill_name" == "pro" ]] && continue
  print_skill "$skill_file" "FREE"
  (( free_count++ )) || true
done

# Pro skills
echo -e "${BOLD}PRO SKILLS${RESET}  ${DIM}(Gumroad — brianrwagner.gumroad.com)${RESET}"
echo -e "${DIM}─────────────────────────────────────────────────────────${RESET}"

pro_count=0
if [ -d "$REPO_DIR/pro" ]; then
  for skill_file in "$REPO_DIR"/pro/*/SKILL.md; do
    [ -f "$skill_file" ] || continue
    print_skill "$skill_file" "PRO"
    (( pro_count++ )) || true
  done
fi

echo -e "${BOLD}${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo -e "  ${GREEN}${free_count} free${RESET}  •  ${YELLOW}${pro_count} pro${RESET}  •  $((free_count + pro_count)) total"
echo -e "${BOLD}${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo ""
```

## File: `social-card-gen/README.md`
```markdown
# Stop rewriting the same post 3 times

You write one update. Then you rewrite it for Twitter, LinkedIn, and Reddit.
That repetitive step is where time disappears.

`social-card-gen` turns one source into platform-ready drafts in one command.

## Value

- Save 15-30 minutes per post cycle.
- Keep tone consistent across channels.
- Enforce platform limits automatically.
- Run locally with no AI/API dependency.

## Platforms

- Twitter: 280 chars, punchy style, compact hashtag strategy.
- LinkedIn: 3000 chars, professional tone, business CTA.
- Reddit: authentic conversation style, discussion CTA.

## Install

```bash
npm install
```

## Usage

```bash
# from raw text
node generate.js --text "We reduced support tickets by 28% after redesigning onboarding." --stdout

# from a markdown file
node generate.js --file examples/input-example.md --outdir examples

# choose specific platforms
node generate.js --file examples/input-example.md --platforms twitter,reddit --stdout
```

## Example source

`examples/input-example.md`

## Example outputs

- `examples/output-twitter.txt`
- `examples/output-linkedin.txt`
- `examples/output-reddit.txt`

## Time savings snapshot

Manual approach:
- Draft + rewrite x3: 20-30 minutes

With `social-card-gen`:
- One source draft + command run + quick edits: 5-10 minutes
```

## File: `social-card-gen/SKILL-OC.md`
```markdown
---
name: social-card-gen
description: Generate platform-specific social post variants (Twitter/X, LinkedIn, Reddit) from one source input. Works with or without Node.js script. Includes platform reasoning, quality review, and guardrails against cross-posting spam.
---

**Platform:** OpenClaw (token-optimized)

## Required Intake (4 questions — ask before writing)

1. **Source message** — core idea, update, or story (paste raw text or describe it)
2. **Tone goal** — Informative / Provocative / Humble brag / Conversational / Educational
3. **Audience** — who needs to see this? (Founders, marketers, developers, etc.)
4. **CTA** — what should readers do? (Visit link, reply, follow, share, start conversation)

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | 1 platform (user picks) | Testing single channel |
| `standard` | All 3 platforms: Twitter + LinkedIn + Reddit | Default cross-platform |
| `deep` | All platforms + 3 variants each + A/B guidance | Campaign testing |

## Platform Rules

**Twitter/X (280 chars):**
- Lead with most surprising or specific claim — no warm-up
- Max 1–2 hashtags, directly relevant
- Short CTA embedded in copy
- ❌ Long intros, passive voice, hashtag walls

**LinkedIn (3,000 chars, first 2 lines critical):**
- First line: bold truth or curiosity hook (NOT "excited to share")
- Short paragraphs (1–2 lines), lots of whitespace
- 3–5 hashtags at end only, never in body
- Discussion CTA: "What's your experience with this?"
- ❌ "I'm humbled to announce," excessive hashtags, no line breaks

**Reddit:**
- Frame as experience, question, or lesson — community-first
- Title: specific and searchable, not clickbaity
- End with open question inviting community input
- ❌ Never hashtags. Never "check out my [thing]" openers

## Generation Template

**Twitter:**
```
[Bold claim or surprising fact]

[1-2 sentences supporting context]

[Engaging question or CTA]

[1-2 hashtags max]
```

**LinkedIn:**
```
[First line hook — curiosity, not announcement]

[1-2 line context]

[Core insight — 2-4 short paragraphs]

[Personal angle or reflection]

[Discussion CTA question]

[3-5 hashtags at end]
```

**Reddit:**
```
Title: [specific, searchable]

[Opening: experience/question/lesson — community-first]

[Body: genuine story with specifics]

[Closing question for community]
```

## With Node.js (automated path)

```bash
npm install
node generate.js --text "source message" --stdout
node generate.js --file input.md --outdir output/
```

## Quality Review (required before delivering)

- [ ] Twitter: under 280 chars? Starts with strongest point?
- [ ] LinkedIn: first line works before "see more"? No "I'm excited"?
- [ ] Reddit: would feel native in target subreddit? Zero hashtags?
- [ ] All: unique to platform — not the same post copy-pasted?
- [ ] All: CTA matches stated goal?

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `social-card-gen/SKILL.md`
```markdown
---
name: social-card-gen
description: Generate platform-specific social post variants (Twitter/X, LinkedIn, Reddit) from one source input. Works with or without Node.js script. Includes platform reasoning, quality review, and guardrails against cross-posting spam.
---

# Social Card Generator

Transform one source message into platform-ready social copy for Twitter/X, LinkedIn, and Reddit.

This skill works two ways:
- **With Node.js:** Use `generate.js` for deterministic, automated output
- **Without Node.js:** Manual generation path built directly into this skill (no dependencies required)

---

## Mode

Detect from context or ask: *"One platform, all platforms, or all platforms with variants?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | 1 platform (user picks), optimized variant | Testing a single channel |
| `standard` | All 3 platforms: Twitter, LinkedIn, Reddit | Standard cross-platform post |
| `deep` | All platforms + 3 variants each + A/B test guidance | Campaign testing, maximizing reach |

**Default: `standard`** — use `quick` if they specify a platform. Use `deep` if they're running a content campaign and want options.

---

## ⚠️ MANDATORY: 4-Question Intake Before Generating

Ask these before writing a single word of copy:

> 1. **Source message:** What's the core idea, update, or story? (Paste raw text or describe it.)
> 2. **Tone goal:** Informative? Provocative? Humble brag? Conversational? Educational?
> 3. **Audience:** Who needs to see this? (Founders, marketers, developers, general public?)
> 4. **CTA:** What do you want readers to do? (Visit link, reply, follow, share, start a conversation?)

Without these answers, you'll get generic output that won't land on any platform.

---

## Platform Reasoning Rules (Built In — No External Script Needed)

### 🐦 Twitter/X
- **Character limit:** 280 characters (single tweet) or threaded for long-form
- **Tone:** Punchy, direct, opinionated. Twitter rewards brevity and conviction.
- **Hook structure:** Lead with the most surprising or specific claim. No warm-up.
- **Hashtags:** Max 1-2 directly relevant tags. Never stuff.
- **CTA style:** Short and embedded. "What's your take?" or "Link in reply."
- **What kills Twitter posts:** Long intros, passive voice, corporate speak, hashtag walls.
- **Example hook pattern:** "[Counterintuitive claim]. Here's why: [1-2 sentence reason]. [Engaging question]."

### 💼 LinkedIn
- **Character limit:** 3,000 characters for posts. First 2 lines before "See more" are critical.
- **Tone:** Professional but personal. Thought leadership with a human angle.
- **Hook structure:** First line must create curiosity or state a bold truth — not "excited to share."
- **Hashtags:** 3-5 max, at the end. Never in the body copy.
- **CTA style:** Invite discussion. "What's your experience with this?" works well.
- **Opener rule:** NEVER start with self-promotional language. Lead with a lesson, story, or observation.
- **What kills LinkedIn posts:** Cringe openers ("I'm humbled to announce..."), excessive hashtags, no line breaks.
- **Format tip:** Short paragraphs (1-2 lines). White space is your friend.

### 🔵 Reddit
- **Character limit:** No hard limit, but long posts need clear structure with headers.
- **Tone:** Authentic, curious, community-first. Reddit readers have a finely tuned BS detector.
- **Hook structure:** Situational — frame as a question, lesson learned, or genuine experience.
- **Hashtags:** Never. Not a thing on Reddit.
- **CTA style:** End with an open question that invites the community to share their take.
- **Self-promotion rule:** Never lead with your own promotion. Frame everything as a contribution to the community.
- **What kills Reddit posts:** Obvious marketing, lack of genuine insight, "check out my [thing]" openers.

---

## Manual Generation Path (No Node.js Required)

**Follow this process exactly:**

### Step 1: Distill the Core Message
From the source input, extract:
- The ONE key insight or fact
- The "so what" — why does this matter to the audience?
- The evidence or story behind it

### Step 2: Generate 3 Platform Variants

**Twitter/X variant:**
```
[Bold claim or surprising fact — max 1 sentence]

[1-2 sentences of supporting context]

[Engaging question or CTA]

[1-2 relevant hashtags max]
```
*Check: Under 280 chars for single tweet? If not, decide: cut or thread.*

**LinkedIn variant:**
```
[First line hook — create curiosity, not announcement]

[1-2 line context paragraph]

[Core insight or framework — 2-4 short paragraphs]

[Personal angle or reflection]

[Discussion CTA — question for the audience]

[3-5 hashtags at the end only]
```
*Check: Does the first line work before "See more"? Does it NOT start with "I'm excited to..."?*

**Reddit variant:**
```
[Title: specific, searchable, not clickbaity]

[Opening: frame as experience, question, or lesson — community-first]

[Body: genuine story or insight with specifics]

[Closing question to invite community input]
```
*Check: Would this feel at home in the target subreddit? No hashtags?*

---

## With Node.js (Automated Path)

```bash
npm install

# text input
node generate.js --text "We reduced onboarding time by 35% with a checklist." --stdout

# file input
node generate.js --file examples/input-example.md --outdir examples

# URL input (when network is available)
node generate.js --url https://example.com/post --platforms twitter,linkedin --stdout
```

If `generate.js` is unavailable, use the Manual Generation Path above — same quality, just manual.

---

## Quality Self-Review Pass (REQUIRED After Generating)

After generating all 3 variants, run this review before delivering:

| Check | Twitter | LinkedIn | Reddit |
|---|---|---|---|
| Hook strong? (Would you stop scrolling?) | ✅/❌ | ✅/❌ | ✅/❌ |
| CTA present and clear? | ✅/❌ | ✅/❌ | ✅/❌ |
| Platform fit? (Tone matches platform norms) | ✅/❌ | ✅/❌ | ✅/❌ |
| Guardrails pass? (See below) | ✅/❌ | ✅/❌ | ✅/❌ |

**Flag the weakest variant** and explain why: "The Reddit variant is the weakest because it still reads like a LinkedIn post — too polished, not community-first."

---

## Guardrails (Never Violate)

❌ **No identical copy cross-posted** — every platform variant must be meaningfully different in tone and structure
❌ **No hashtag spam on LinkedIn** — max 5, always at the end, never in the body
❌ **No self-promotional openers on Reddit** — community value first, always
❌ **No vague hooks** — "I have some thoughts on X" is not a hook
❌ **No copy that assumes platform context** — Reddit readers don't know your LinkedIn audience

---

## Iteration Loop

After delivering the 3 variants:
1. Ask: "Which variant feels most off? What's not landing?"
2. If hook is weak → rewrite the first line using a different angle (counterintuitive, numerical, story-led)
3. If CTA is weak → try a question instead of a directive
4. If platform fit is off → re-read the platform rules and rewrite from scratch for that platform

---

## Output Format

Deliver:

```
## Twitter/X
[Final copy — ready to paste]
Character count: [X]/280

## LinkedIn
[Final copy — ready to paste]

## Reddit
Title: [Post title]
[Body — ready to paste]

## Quality Review
- Strongest variant: [Platform] — because [reason]
- Weakest variant: [Platform] — [what to improve if needed]
- All guardrails passed: Yes / No — [note any issues]
```

---

*Skill by Brian Wagner | AI Marketing Architect | brianrwagner.com*
```

## File: `social-card-gen/generate.js`
```javascript
#!/usr/bin/env node
'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { extractKeywords, renderTemplate, PLATFORM_CONFIGS } = require('./templates');

function printHelp() {
  console.log(`social-card-gen\n\nUsage:\n  node generate.js [options]\n\nInput options (use one):\n  --text "..."           Raw text input\n  --file ./path.md        Read content from local file\n  --url https://...       Read content from URL\n\nOutput options:\n  --platforms list        Comma-separated: twitter,linkedin,reddit (default: all)\n  --outdir ./dir          Write files to directory (default: current directory)\n  --stdout                Print generated cards to stdout instead of files\n  --prefix output-        Output filename prefix (default: output-)\n  --title "Custom title" Override title extraction\n\nExamples:\n  node generate.js --text "We reduced deploy time by 42%" --stdout\n  node generate.js --file examples/input-example.md --outdir examples\n  node generate.js --url https://example.com/post --platforms twitter,linkedin --stdout\n`);
}

function parseArgs(argv) {
  const options = {
    platforms: ['twitter', 'linkedin', 'reddit'],
    outdir: process.cwd(),
    stdout: false,
    prefix: 'output-'
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];

    if (arg === '--help' || arg === '-h') {
      options.help = true;
      continue;
    }

    if (arg === '--text') {
      options.text = argv[++i];
      continue;
    }

    if (arg === '--file') {
      options.file = argv[++i];
      continue;
    }

    if (arg === '--url') {
      options.url = argv[++i];
      continue;
    }

    if (arg === '--platforms') {
      options.platforms = (argv[++i] || '')
        .split(',')
        .map((s) => s.trim().toLowerCase())
        .filter(Boolean);
      continue;
    }

    if (arg === '--outdir') {
      options.outdir = argv[++i];
      continue;
    }

    if (arg === '--stdout') {
      options.stdout = true;
      continue;
    }

    if (arg === '--prefix') {
      options.prefix = argv[++i] || 'output-';
      continue;
    }

    if (arg === '--title') {
      options.title = argv[++i];
      continue;
    }

    if (!arg.startsWith('--') && !options.text && !options.file && !options.url) {
      options.text = arg;
      continue;
    }

    throw new Error(`Unknown or incomplete argument: ${arg}`);
  }

  return options;
}

function stripMarkdownAndHtml(input) {
  return (input || '')
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .replace(/<[^>]+>/g, ' ')
    .replace(/^#{1,6}\s+/gm, '')
    .replace(/^>\s?/gm, '')
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/\*([^*]+)\*/g, '$1')
    .replace(/\s+/g, ' ')
    .trim();
}

function toSentences(text) {
  return text
    .split(/(?<=[.!?])\s+/)
    .map((s) => s.trim())
    .filter((s) => s.length > 20);
}

function firstNonEmptyLine(raw) {
  const line = (raw || '')
    .split(/\r?\n/)
    .map((l) => l.trim())
    .find(Boolean);
  if (!line) return 'Content update';
  return line.replace(/^#{1,6}\s+/, '').trim();
}

function composeContext(rawInput, cleanedText, options) {
  const sentences = toSentences(cleanedText);
  const s1 = sentences[0] || cleanedText;
  const s2 = sentences[1] || '';
  const s3 = sentences[2] || '';
  const title = options.title || firstNonEmptyLine(rawInput).slice(0, 90);
  const keywords = extractKeywords(cleanedText, 8);

  return {
    title,
    hook: `Quick take: ${s1}`,
    corePoint: [s2, s3].filter(Boolean).join(' '),
    professionalSummary: [s1, s2, s3].filter(Boolean).join(' '),
    redditIntro: `I just read this and wanted to sanity-check my take: ${s1}`,
    redditBody: [s2, s3].filter(Boolean).join(' '),
    sourceUrl: options.url || '',
    keywords
  };
}

async function readFromStdinIfAvailable() {
  if (process.stdin.isTTY) return '';

  return new Promise((resolve, reject) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', (chunk) => {
      data += chunk;
    });
    process.stdin.on('end', () => resolve(data));
    process.stdin.on('error', reject);
  });
}

async function loadInput(options) {
  if (options.text) {
    return options.text;
  }

  if (options.file) {
    return fs.readFileSync(path.resolve(options.file), 'utf8');
  }

  if (options.url) {
    const response = await fetch(options.url);
    if (!response.ok) {
      throw new Error(`Failed to fetch URL (${response.status}): ${options.url}`);
    }
    return response.text();
  }

  const stdinValue = await readFromStdinIfAvailable();
  if (stdinValue.trim()) {
    return stdinValue;
  }

  throw new Error('No input provided. Use --text, --file, --url, or pipe data via stdin.');
}

function validatePlatforms(platforms) {
  const supported = new Set(Object.keys(PLATFORM_CONFIGS));
  const invalid = platforms.filter((p) => !supported.has(p));

  if (invalid.length > 0) {
    throw new Error(`Unsupported platforms: ${invalid.join(', ')}`);
  }

  if (platforms.length === 0) {
    throw new Error('No platforms selected. Use --platforms twitter,linkedin,reddit');
  }
}

function writeOutputs(results, options) {
  if (options.stdout) {
    for (const { platform, text } of results) {
      process.stdout.write(`\n=== ${platform.toUpperCase()} ===\n${text}\n`);
    }
    return;
  }

  fs.mkdirSync(path.resolve(options.outdir), { recursive: true });
  for (const { platform, text } of results) {
    const fileName = `${options.prefix}${platform}.txt`;
    const filePath = path.join(path.resolve(options.outdir), fileName);
    fs.writeFileSync(filePath, `${text}\n`, 'utf8');
  }
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  if (options.help) {
    printHelp();
    return;
  }

  validatePlatforms(options.platforms);

  const rawInput = await loadInput(options);
  const cleanedText = stripMarkdownAndHtml(rawInput);
  if (!cleanedText) {
    throw new Error('Input resolved to empty text after cleaning.');
  }

  const context = composeContext(rawInput, cleanedText, options);
  const results = options.platforms.map((platform) => ({
    platform,
    text: renderTemplate(platform, context)
  }));

  writeOutputs(results, options);
}

main().catch((err) => {
  console.error(`Error: ${err.message}`);
  process.exit(1);
});
```

## File: `social-card-gen/package.json`
```json
{
  "name": "social-card-gen",
  "version": "1.0.0",
  "description": "Offline social post generator for Twitter, LinkedIn, and Reddit",
  "main": "generate.js",
  "bin": {
    "social-card-gen": "generate.js"
  },
  "scripts": {
    "generate:examples": "node generate.js --file examples/input-example.md --outdir examples"
  },
  "keywords": [
    "social",
    "content",
    "twitter",
    "linkedin",
    "reddit",
    "generator"
  ],
  "license": "MIT",
  "dependencies": {}
}
```

## File: `social-card-gen/templates.js`
```javascript
'use strict';

const PLATFORM_CONFIGS = {
  twitter: {
    name: 'Twitter',
    characterLimit: 280,
    tone: 'punchy',
    toneGuideline: 'Lead with the hook, keep it tight, and make every sentence earn space.',
    hashtagStrategy: 'Use 1-3 topical hashtags. Keep them short and specific.',
    ctaFormat: 'Short imperative CTA (e.g., Read more:, Try this:, What do you think?)'
  },
  linkedin: {
    name: 'LinkedIn',
    characterLimit: 3000,
    tone: 'professional',
    toneGuideline: 'Use a clear business outcome, practical framing, and credible language.',
    hashtagStrategy: 'Use 2-5 industry hashtags at the end. Prefer category tags over memes.',
    ctaFormat: 'Professional prompt CTA (e.g., What are you seeing in your team?)'
  },
  reddit: {
    name: 'Reddit',
    characterLimit: null,
    tone: 'authentic',
    toneGuideline: 'Write like a real person: direct, candid, and discussion-friendly.',
    hashtagStrategy: 'Avoid hashtag spam. Usually 0 hashtags; optionally one if it adds context.',
    ctaFormat: 'Open-ended discussion question (e.g., Curious how others approach this.)'
  }
};

const STOPWORDS = new Set([
  'a', 'an', 'the', 'and', 'or', 'but', 'if', 'then', 'than', 'that', 'this', 'those', 'these',
  'to', 'for', 'of', 'on', 'in', 'at', 'with', 'by', 'from', 'as', 'is', 'are', 'was', 'were',
  'be', 'been', 'being', 'it', 'its', 'into', 'about', 'over', 'under', 'after', 'before',
  'we', 'you', 'they', 'our', 'your', 'their', 'i', 'he', 'she', 'them', 'us', 'can', 'could',
  'should', 'would', 'will', 'just', 'very', 'more', 'most', 'much', 'many', 'also'
]);

function extractKeywords(text, maxKeywords = 6) {
  const words = (text || '')
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, ' ')
    .split(/\s+/)
    .filter((word) => word.length > 2 && !STOPWORDS.has(word));

  const counts = new Map();
  for (const word of words) {
    counts.set(word, (counts.get(word) || 0) + 1);
  }

  return [...counts.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, maxKeywords)
    .map(([word]) => word);
}

function toHashtag(term) {
  const cleaned = term.replace(/[^a-z0-9]/gi, ' ').trim();
  if (!cleaned) return '';

  const parts = cleaned.split(/\s+/);
  const formatted = parts
    .map((part, index) => {
      if (index === 0) return part.toLowerCase();
      return part.charAt(0).toUpperCase() + part.slice(1).toLowerCase();
    })
    .join('');

  return `#${formatted}`;
}

function enforceCharacterLimit(text, limit) {
  if (!limit || text.length <= limit) return text;

  const suffix = '...';
  const hardLimit = Math.max(0, limit - suffix.length);
  const trimmed = text.slice(0, hardLimit);
  const safeTrimmed = trimmed.slice(0, Math.max(0, trimmed.lastIndexOf(' ')));
  const output = (safeTrimmed || trimmed).trimEnd();
  return `${output}${suffix}`;
}

function buildHashtags(platform, keywords) {
  if (!keywords.length) return '';

  if (platform === 'twitter') {
    return keywords.slice(0, 3).map(toHashtag).filter(Boolean).join(' ');
  }

  if (platform === 'linkedin') {
    return keywords.slice(0, 4).map(toHashtag).filter(Boolean).join(' ');
  }

  if (platform === 'reddit') {
    return ''; // Reddit style avoids hashtag clutter by default.
  }

  return '';
}

function buildCTA(platform, sourceUrl) {
  if (platform === 'twitter') {
    return sourceUrl ? `Read more: ${sourceUrl}` : 'Thoughts?';
  }

  if (platform === 'linkedin') {
    return sourceUrl
      ? `Full details: ${sourceUrl}\n\nWhat are you seeing in your team?`
      : 'What are you seeing in your team?';
  }

  if (platform === 'reddit') {
    return sourceUrl
      ? `If you want the full context: ${sourceUrl}\n\nCurious how others here handle this.`
      : 'Curious how others here handle this.';
  }

  return '';
}

function renderTemplate(platform, context) {
  const config = PLATFORM_CONFIGS[platform];
  if (!config) {
    throw new Error(`Unsupported platform: ${platform}`);
  }

  const hashtags = buildHashtags(platform, context.keywords || []);
  const cta = buildCTA(platform, context.sourceUrl);

  let text;
  if (platform === 'twitter') {
    const tailLines = [hashtags, cta].filter(Boolean);
    const tail = tailLines.join('\n');
    const reserved = tail ? tail.length + 2 : 0; // account for separating newlines
    const maxBodyLength = Math.max(0, (config.characterLimit || 280) - reserved);
    const body = enforceCharacterLimit(
      [context.hook, context.corePoint].filter(Boolean).join(' ').trim(),
      maxBodyLength
    );
    text = tail ? `${body}\n\n${tail}` : body;
  } else if (platform === 'linkedin') {
    text = `${context.title}\n\n${context.professionalSummary}\n\n${hashtags}`.trim();
    text = `${text}\n\n${cta}`.trim();
  } else {
    text = `${context.redditIntro}\n\n${context.redditBody}\n\n${cta}`.trim();
  }

  return enforceCharacterLimit(text, config.characterLimit);
}

module.exports = {
  PLATFORM_CONFIGS,
  extractKeywords,
  enforceCharacterLimit,
  renderTemplate
};
```

## File: `social-card-gen/examples/input-example.md`
```markdown
# Product update: onboarding improvements

This week we shipped a guided onboarding checklist for new users. In testing, setup time dropped from 45 minutes to 28 minutes, and week-1 activation improved by 19%.

The biggest win came from replacing long setup docs with short in-app prompts at the exact moment users needed each step.

Next, we're adding role-based onboarding paths so teams can skip irrelevant setup screens.
```

## File: `social-card-gen/examples/output-linkedin.txt`
```
Product update: onboarding improvements

Product update: onboarding improvements This week we shipped a guided onboarding checklist for new users. In testing, setup time dropped from 45 minutes to 28 minutes, and week-1 activation improved by 19%. The biggest win came from replacing long setup docs with short in-app prompts at the exact moment users needed each step.

#onboarding #setup #week #users

What are you seeing in your team?
```

## File: `social-card-gen/examples/output-reddit.txt`
```
I just read this and wanted to sanity-check my take: Product update: onboarding improvements This week we shipped a guided onboarding checklist for new users.

In testing, setup time dropped from 45 minutes to 28 minutes, and week-1 activation improved by 19%. The biggest win came from replacing long setup docs with short in-app prompts at the exact moment users needed each step.

Curious how others here handle this.
```

## File: `social-card-gen/examples/output-twitter.txt`
```
Quick take: Product update: onboarding improvements This week we shipped a guided onboarding checklist for new users. In testing, setup time dropped from 45 minutes to 28 minutes, and week-1 activation improved by 19%. The biggest win came...

#onboarding #setup #week
Thoughts?
```

## File: `testimonial-collector/SKILL-OC.md`
```markdown
---
name: testimonial-collector
description: Systematically gather, score, and format client testimonials. Use when someone needs social proof, wants to collect feedback, needs to turn happy clients into public advocates, or asks for help requesting or drafting a testimonial.
---

**Platform:** OpenClaw (token-optimized)

## Required Inputs

- Client name, company, industry
- Project type + specific deliverables
- Key results — **push for at least one number** ("rough estimate is fine")
- Desired format (short quote / medium paragraph / full narrative)
- Urgency (this week vs. building a library)

**Outcome gate:** If results vague ("things improved") → stop: "Give me one number — revenue, time saved, leads, or rough estimate. No draft without it."

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | 1 outreach script + 1 format template | Asking one client now |
| `standard` | Full collection system: timing + scripts + formatting + display guidance | Repeatable social proof |
| `deep` | Full system + multi-channel strategy + case study pipeline | Sales enablement, proposal library |

## Quality Scoring (pre-draft check)

| Dimension | Score 1 | Score 3 | Score 5 |
|-----------|---------|---------|---------|
| Specificity | No details | Vague | Specific named result |
| Measurability | "It was great" | "Noticeable improvement" | "40% increase in leads" |
| Authentic Voice | Ad copy | Slightly stilted | Reads how a person talks |
| Length | Too short | Decent | Enough for all 3 formats |

Rule: ≤2 on any dimension → apply iteration protocol before drafting.

## Outreach Templates

**Direct Ask:**
```
Subject: Quick favor (30 seconds)

Hey [Name], loved working on [project] — especially [specific result].

Would you share a quick testimonial for my site?
A) I send you 3 questions  B) I draft, you approve

Whatever's easier.
```

**3 Questions Route:**
1. What was the situation before we worked together?
2. What changed or improved?
3. Would you recommend this to others? Why?

## Draft-on-Behalf Rules

- Match their actual communication style (check emails/messages)
- Structure: Situation → What Changed → Result → Recommendation
- Never: superlatives without evidence ("amazing," "life-changing")
- Never: lead with praise — lead with the client's situation

## 3 Format Templates

**Short (homepage, LinkedIn):**
```
"[Result sentence — lead with outcome]"
— [Name], [Title] at [Company]
```

**Medium (services page, sales deck):**
```
"[Problem/situation]. [What changed]. [Recommendation or result]."
— [Name], [Title] at [Company]
```

**Long (case study, PDFs):**
1. Context paragraph (situation)
2. Transformation paragraph (during engagement)
3. Results paragraph (numbers + named wins)
4. Closing recommendation sentence

## Self-Critique Before Delivering

- [ ] Short version has ≥1 concrete outcome (not "great results")
- [ ] Could the client have written this? (not marketing headline)
- [ ] Format length matches stated use case?
- [ ] No claims or numbers you added that the client didn't make?

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `testimonial-collector/SKILL.md`
```markdown
---
name: testimonial-collector
description: Systematically gather, score, and format client testimonials. Use when someone needs social proof, wants to collect feedback, needs to turn happy clients into public advocates, or asks for help requesting or drafting a testimonial.
---

# Testimonial Collector

## Mode

Detect from context or ask: *"One script, full system, or full system with campaign?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | 1 outreach script + 1 format template | Asking one client, right now |
| `standard` | Full collection system: timing, scripts, formatting, display guidance | Building repeatable social proof |
| `deep` | Full system + multi-channel strategy + case study pipeline | Sales enablement, proposal library |

**Default: `standard`** — use `quick` if they have one client in mind. Use `deep` if they want a system they can hand to a VA.

---

## Context Loading Gates

**Before proceeding, gather:**
- [ ] Client name, company, and industry
- [ ] Project type and specific deliverables
- [ ] Key results — push for at least one number ("even a rough estimate")
- [ ] Desired output format (short quote / medium paragraph / full narrative)
- [ ] Urgency (this week vs. building a library)

If results are vague (e.g., "things improved"), **stop and ask:** "Can you name one specific number — even a rough estimate? That's what makes a testimonial credible and usable." Do not draft until you have this.

If the user wants to skip a field: note it and flag the quality impact in the output.

---

## Phase 1: Situation Analysis

Before drafting anything, reason through:

1. **Client relationship stage:** Was this a quick project or a deep engagement? Depth affects how much authentic language is available.
2. **Results clarity:** Are the outcomes measurable (numbers, timelines, named outcomes) or soft (vibes, general satisfaction)?
3. **Format match:** What placement does the user need this for? A homepage needs different length than a sales deck.
4. **Voice data:** Does the user have existing communication from this client (emails, Slack, quotes) that can inform tone?

Output a brief situation summary:
> "You have a [length] engagement with [client] in [industry], with [strong/weak] results data. I'll draft in [format] with [authentic/templated] voice. Main gap to address: [specific gap]."

---

## Phase 2: Quality Scoring Framework

Score the raw testimonial content (or anticipated content) before drafting:

| Dimension | Score 1 | Score 3 | Score 5 |
|---|---|---|---|
| **Specificity** | No details | Vague references | Specific named result |
| **Measurability** | "It was great" | "Noticeable improvement" | "40% increase in leads" |
| **Authentic Voice** | Sounds like ad copy | Slightly stilted | Reads exactly how a person talks |
| **Length** | Too short (no context) | Decent but thin | Enough for all 3 formats |

**Scoring rule:**
- 4+ on all 4 dimensions → ready to use
- ≤2 on any dimension → apply iteration protocol before delivering

---

## Phase 3: Draft Generation

### The Ask Templates

**Direct Ask:**
```
Subject: Quick favor (30 seconds)

Hey [Name],

Loved working on [project] with you — especially seeing [specific result].

Would you be open to sharing a quick testimonial I could use on my site?

No pressure. If yes, I can either:
A) Send you 3 questions to answer
B) Write a draft for you to approve/edit

Whatever's easier.
```

**Question Route:**
```
3 quick questions:
1. What was the situation before we worked together?
2. What changed or improved?
3. Would you recommend this to others? Why?
```

**Draft-on-Behalf Framework:**
Rules for writing in the client's voice:
- **Tone:** Match their actual communication style (check emails/messages for vocabulary)
- **Structure:** Situation Before → What Changed → Specific Result → Recommendation
- **Avoid:** Superlatives without evidence ("amazing," "life-changing")
- **Avoid:** Leading with praise — lead with the client's situation
- **Length:** 50-75 words (short), 100-150 words (medium), 200+ (long/full)

Fill-in template:
```
"[Client situation in 1 sentence]. [What the engagement delivered — concrete]. 
[Specific result, ideally with a number]. [Recommendation statement in client's natural voice]."
```

---

## Phase 4: Format Production

### Short Format (2-liner)
```
"[One punchy outcome sentence — lead with the result]"
— [Name], [Title] at [Company]
```
**Use for:** Homepage, LinkedIn featured section, proposal proof points

### Medium Format (2-3 sentences)
```
"[Problem or situation]. [What changed]. [Recommendation or result]."
— [Name], [Title] at [Company]
```
**Use for:** Services page, sales decks, email sequences

### Long Format (Full narrative)
Structure:
1. Context paragraph (2-3 sentences on the situation)
2. Transformation paragraph (what happened during the engagement)
3. Results paragraph (outcomes, numbers, named wins)
4. Closing recommendation sentence

**Use for:** Case study pages, downloadable PDFs, high-trust sales assets

---

## Phase 5: Self-Critique Pass (REQUIRED)

After generating all formats, evaluate:

**Specificity check:** Does the short version have at least one concrete outcome (not just "great results")?
**Voice check:** Could the client have actually written this, or does it sound like a marketing headline?
**Placement check:** Is the recommended format actually correct length for the stated use case?
**Ethics check:** Does the draft contain any claims the client didn't make or numbers you added?

Flag any issues: "The short version lacks a specific metric — you'll need to get one number from the client before using this on a homepage."

---

## Iteration Protocol

If the received testimonial scores ≤2 on any dimension, send this gentle follow-up:
```
"Thanks so much — this is great. One small ask: could you add one specific 
number or outcome? Even rough ('saved us about 5 hours a week') makes it 
much more compelling for other clients. Totally optional, but makes a real difference."
```

If a second request still yields nothing specific: use Tier 3 proxy language:
> "noticeable improvement in [area]" or "process now runs without manual oversight"

---

## Placement Recommendation

Always deliver a placement recommendation with the formatted testimonials:

| Format | Recommended Locations | Why |
|---|---|---|
| Short (2-liner) | Homepage, proposals, LinkedIn | Trust at first glance |
| Medium | Services page, email, sales decks | Overcome late-stage objections |
| Long | Case study page, PDF, portfolio | Deep proof for serious buyers |

**Cross-reference:** If this client has a strong story, suggest running `case-study-builder` to expand into a full case study.

---

## Output Structure

```markdown
## Testimonial: [Client Name] — [Date]

### Quality Assessment
- Specificity: [X/5]
- Measurability: [X/5]
- Authentic Voice: [X/5]
- Length: [X/5]
- **Total: [X/20] — [Ready to use / Needs iteration]**

### Short Format (2-liner)
"[Quote]"
— [Name], [Title], [Company]

### Medium Format
"[Quote]"
— [Name], [Title], [Company]

### Long Format
[Full narrative]

### Placement Recommendation
[Where to use each format]

### Next Step
[Iteration note OR cross-reference to case-study-builder]
```

---

*Skill by Brian Wagner | AI Marketing Architect | brianrwagner.com*
```

## File: `tweet-draft-reviewer/SKILL-OC.md`
```markdown
---
name: tweet-draft-reviewer
description: Review tweet drafts in Claude Code against 8 voice rules. Scores 1-10, breaks down every rule, and rewrites anything that scores below 7.
---

**Platform:** OpenClaw (token-optimized)

## How to Use

Single draft: `Review this tweet draft: [paste tweet]`
Batch scan: `Review all drafts in content/tweet-drafts/`

## Intake

**Mode A — Direct paste:** Proceed to scoring.
**Mode B — Folder scan:**
```bash
find "${VAULT_PATH:-$(pwd)}/content/tweet-drafts" -name "*.md" 2>/dev/null | while read f; do
  grep -q 'reviewed: true' "$f" 2>/dev/null || echo "UNREVIEWED:$f"
done
```
**Mode C — Ambiguous:** Ask for draft or folder path.

## 8 Scoring Rules (✅ PASS / ❌ FAIL)

| # | Rule | Fail Condition |
|---|------|----------------|
| 1 | No "I" opener | First word is exactly "I" |
| 2 | Strong opener | First sentence is a question (ends ?) or starts with "Have/Do/Are/What if you" |
| 3 | No AI tells | Contains: delve, certainly, game-changing, game changer, it's worth noting, invaluable, unleash, revolutionize, transformative |
| 4 | No generic closers | Ends with: "what do you think," "drop a comment," "thoughts?," "let me know in the comments," "agree?," "sound familiar?" |
| 5 | Corey Test (specificity) | Vague language with no numbers, names, or concrete outcomes |
| 6 | Character count | >280 chars with no thread formatting (numbered sections = PASS) |
| 7 | Single point | Makes 3+ distinct unrelated claims with no through-line |
| 8 | Punchy rhythm | >3 consecutive sentences of similar length (monotonous) |

## Scoring

| Score | Rating | Action |
|-------|--------|--------|
| 8–10 | Strong | Ready to post |
| 6–7 | Good | Light edit — flag specific issue |
| 4–5 | Weak | Rewrite required |
| 1–3 | Poor | Full rewrite + explanation |

**Rule:** Score <7 → always provide a rewrite. Score ≥7 → note what's working, flag any minor issues.

## Output Format

```
## Tweet Review

**Score: X/10** — [Strong/Good/Weak/Poor]

**Rule Breakdown:**
1. No "I" opener: ✅/❌ [reason]
2. Strong opener: ✅/❌ [reason]
3. No AI tells: ✅/❌ [words flagged if any]
4. No generic closer: ✅/❌ [reason]
5. Corey Test: ✅/❌ [specific vague language if any]
6. Character count: ✅/❌ [count]
7. Single point: ✅/❌ [reason]
8. Punchy rhythm: ✅/❌ [reason]

**What's Working:** [if score ≥7]

**Rewrite:** [if score <7 — full rewrite applying all rules]
```

**For folder scans:** Output results as a table with filename + score, then show full review for each failed draft.

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `tweet-draft-reviewer/SKILL.md`
```markdown
---
name: tweet-draft-reviewer
description: Review tweet drafts in Claude Code against 8 voice rules. Scores 1-10, breaks down every rule, and rewrites anything that scores below 7.
---

# Tweet Draft Reviewer

Paste a tweet draft and get a score out of 10, a rule-by-rule breakdown, and a rewrite if the score is below 7. Takes 30 seconds. Saves you from posting something that sounds like a chatbot wrote it.

Built on 8 voice rules distilled from real content analysis — what separates high-engagement tweets from the ones that get skimmed.

---

## How to Use

**Single draft:**
```
Review this tweet draft: [paste tweet here]
```

**Batch scan:**
```
Review all tweet drafts in my content/tweet-drafts/ folder.
```

---

## Skill Instructions (for Claude Code)

When this skill is invoked, follow these phases exactly.

---

### PHASE 1: INTAKE

Determine input mode:

**Mode A — Direct paste:** User provided draft text inline. Proceed to PHASE 2 with that text.

**Mode B — Folder scan:** User asked to review drafts folder. Run:

```bash
VAULT="${VAULT_PATH:-$(pwd)}"
find "$VAULT/content/tweet-drafts" -name "*.md" 2>/dev/null | while read f; do
  if ! grep -q 'reviewed: true' "$f" 2>/dev/null; then
    echo "UNREVIEWED:$f"
  fi
done
```

If no vault path was given and no `content/tweet-drafts/` exists in the current directory, ask:
```
Where is your tweet drafts folder? (full path, e.g. /root/obsidian-vault/content/tweet-drafts)
```

**Mode C — Ambiguous:** No draft provided and no folder context. Ask:
```
Paste your tweet draft here, or tell me the path to your tweet-drafts folder and I'll scan it.
```

---

### PHASE 2: ANALYZE

Apply all 8 rules to the draft. For each rule, record ✅ PASS or ❌ FAIL with a one-line reason.

---

#### The 8 Rules

**Rule 1: No "I" opener**
- FAIL: First word is exactly `I` (standalone — not "In", "It", "If")
- PASS: Anything else

**Rule 2: Strong opener**
- FAIL: First sentence ends with `?` OR starts with "Have you", "Do you", "Are you", "What if", "What would"
- PASS: Declarative statement, specific number/fact, named scenario, or emotional setup

**Rule 3: No AI tells**
- FAIL: Contains any of: `delve`, `certainly`, `game-changing`, `game changer`, `it's worth noting`, `invaluable`, `unleash`, `revolutionize`, `transformative`
- PASS: None of those words detected

**Rule 4: No generic closers**
- FAIL: Ends with (or contains near the end): `what do you think`, `drop a comment`, `thoughts?`, `let me know in the comments`, `agree?`, `sound familiar?`
- PASS: Ends with a statement, directive, punchline, or thread hook

**Rule 5: Corey Test (specificity)**
- FAIL: Uses vague language without specifics — "it changed how I work", "massive results", "so much better" — no numbers, names, or concrete outcomes
- PASS: Contains at least one specific: a number, timeframe, named tool, or concrete result

**Rule 6: Character count**
- PASS: 280 characters or fewer
- THREAD PASS: Over 280 chars BUT sections are numbered (1/, 2/, 3/) or clearly separated with line breaks — count as PASS
- FAIL: Over 280 chars with no thread formatting

**Rule 7: Single point**
- FAIL: Makes 3+ distinct unrelated claims with no clear through-line
- PASS: One core idea, even if supported by 2–3 details

**Rule 8: Punchy rhythm**
- FAIL: Any sentence over 20 words OR preamble like "I've been thinking a lot about..." / "Something I've noticed recently is..."
- PASS: Short sentences, no preamble, gets to the point by line 2 at latest

---

### PHASE 3: OUTPUT

Print this exact format:

```
TWEET REVIEW
────────────

Score: X/10

Rule-by-Rule:
1. ✅/❌ No "I" opener — [reason]
2. ✅/❌ Strong opener — [reason]
3. ✅/❌ No AI tells — [reason]
4. ✅/❌ No generic closers — [reason]
5. ✅/❌ Corey Test — [reason]
6. ✅/❌ Character count — [reason + actual count]
7. ✅/❌ Single point — [reason]
8. ✅/❌ Punchy rhythm — [reason]

────────────
```

**Scoring table (passes → score):**

| Passes | Score |
|--------|-------|
| 8 | 10/10 |
| 7 | 9/10 |
| 6 | 8/10 |
| 5 | 6/10 |
| 4 | 5/10 |
| 3 | 4/10 |
| 2 | 3/10 |
| 1 | 1/10 |
| 0 | 0/10 |

**If score ≥ 7:**
```
→ Ready to post. Use Typefully or your scheduler to queue it.
```

**If score < 7 — add a rewrite:**
```
Suggested Rewrite:

[rewritten tweet that fixes all failing rules]
```

---

### PHASE 4: SELF-CRITIQUE

Before delivering the output, check:

1. **All 8 rules evaluated** — Count the rule lines in your output. There must be exactly 8. If any are missing, add them.
2. **Score matches pass count** — Count the ✅ marks. Verify the score matches the table above. Correct it if not.
3. **Rewrite quality** — If a rewrite was provided, check it against all 8 rules mentally. Does it pass the ones the original failed? If the rewrite would score below 7 itself, rewrite it again.
4. **Reason quality** — Each rule result must have a specific reason, not a generic one. "Too vague" is not enough — say what specifically is vague.

Fix anything that fails before delivering.

---

## Example Review

**Input:**
```
I've been thinking a lot about how AI is really changing the way founders 
approach content creation and productivity, and I think it's worth noting 
that the teams who figure out async AI workflows are going to have a 
massive advantage. What do you think about this?
```

**Output:**
```
TWEET REVIEW
────────────

Score: 2/10

Rule-by-Rule:
1. ❌ No "I" opener — Starts with "I've"
2. ❌ Strong opener — Slow setup, no hook, no specific fact
3. ❌ No AI tells — Contains "it's worth noting"
4. ❌ No generic closers — Ends with "What do you think about this?"
5. ❌ Corey Test — "massive advantage" is vague, no numbers or concrete outcome
6. ✅ Character count — 248 chars
7. ✅ Single point — Focused on async AI workflows
8. ❌ Punchy rhythm — Run-on sentence, preamble opener

────────────

Suggested Rewrite:

The founders winning right now aren't working harder.

They have agents running at 2am. Content drafted. Research done.
Queue processed.

By 7am they're reviewing output, not creating it.

Async AI ops is the new early morning routine.
```

---

## Batch Mode Output

When scanning a folder, output one review block per file:

```
📄 content/tweet-drafts/linkedin-ai-post.md
[full review block]

📄 content/tweet-drafts/founder-ops.md
[full review block]

────────────
BATCH SUMMARY
Reviewed: 4 drafts
Ready to post (≥7): 2
Need rewrite (<7): 2
```

---

## Requirements

- Claude Code with bash tool access (for folder scan mode)
- No external APIs — pure LLM reasoning for the review
- Tweet drafts folder at `content/tweet-drafts/` (optional — direct paste always works)
- Files in the drafts folder are marked `reviewed: true` to skip them in future scans
```

## File: `vault-cleanup-auditor/SKILL-OC.md`
```markdown
---
name: vault-cleanup-auditor
description: Audit your Obsidian vault in Claude Code — finds stale drafts, empty folders, duplicate filenames, and incomplete files. Saves a dated report.
---

**Platform:** OpenClaw (token-optimized)

## Required Input

- `vault_path` — absolute path to Obsidian vault root

Ask if missing. Do not proceed without it.

## 4 Checks (run all, capture output before formatting)

**Check 1 — Stale drafts (unposted, 30+ days old):**
```bash
VAULT="VAULT_PATH_HERE"
find "$VAULT/content/ready-to-post" -name "*.md" -mtime +30 2>/dev/null | while read f; do
  if grep -q '\*\*Posted:\*\* ❌' "$f" 2>/dev/null; then
    days=$(( ($(date +%s) - $(stat -c %Y "$f")) / 86400 ))
    echo "${days}d|${f##$VAULT/}"
  fi
done
```

**Check 2 — Incomplete files (no headings, 5+ lines):**
```bash
VAULT="VAULT_PATH_HERE"
find "$VAULT" -name "*.md" -not -path "*/.git/*" -not -path "*/.obsidian/*" -not -path "*/.openclaw/*" | while read f; do
  if ! grep -qE '^#{1,6} ' "$f" 2>/dev/null; then
    lines=$(wc -l < "$f")
    [ "$lines" -gt 5 ] && echo "${lines}lines|${f##$VAULT/}"
  fi
done
```

**Check 3 — Duplicate filenames:**
```bash
VAULT="VAULT_PATH_HERE"
find "$VAULT" -name "*.md" -not -path "*/.git/*" -not -path "*/.obsidian/*" \
  -printf "%f\n" | sort | uniq -d | while read name; do
  echo "DUPE:$name"
  find "$VAULT" -name "$name" -not -path "*/.git/*" | while read f; do
    echo "  PATH:${f##$VAULT/}"
  done
done
```

**Check 4 — Empty folders:**
```bash
VAULT="VAULT_PATH_HERE"
find "$VAULT" -type d -empty -not -path "*/.git/*" -not -path "*/.obsidian/*" | while read d; do
  echo "EMPTY:${d##$VAULT/}"
done
```

## Output Format

Save to: `vault-audit/YYYY-MM-DD-audit.md`

```markdown
# Vault Audit — [YYYY-MM-DD]
**Vault:** [path]

## Summary
| Check | Count | Priority |
|-------|-------|----------|
| Stale drafts | X | High |
| Incomplete files | X | Medium |
| Duplicate filenames | X | High |
| Empty folders | X | Low |

## Check 1: Stale Drafts ([count])
[List with days old + path]
**Action:** Review each — post, archive, or delete.

## Check 2: Incomplete Files ([count])
[List with line count + path]
**Action:** Finish or delete.

## Check 3: Duplicate Filenames ([count])
[Grouped by filename with all paths]
**Action:** Consolidate or rename.

## Check 4: Empty Folders ([count])
[List paths]
**Action:** Delete empty folders.

## Recommended Actions
1. [Highest priority, most impactful]
2. [Next]
```

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `vault-cleanup-auditor/SKILL.md`
```markdown
---
name: vault-cleanup-auditor
description: Audit your Obsidian vault in Claude Code — finds stale drafts, empty folders, duplicate filenames, and incomplete files. Saves a dated report.
---

# Vault Cleanup Auditor

Runs 4 targeted checks against your Obsidian vault and saves a prioritized audit report to `vault-audit/YYYY-MM-DD-audit.md`. Takes under 30 seconds. No APIs, no paid services.

Run it monthly or whenever the vault starts feeling messy.

---

## How to Use

Open Claude Code and say:

```
Run the Vault Cleanup Auditor skill against my vault at /path/to/vault.
```

---

## Skill Instructions (for Claude Code)

When this skill is invoked, follow these phases exactly.

---

### PHASE 1: INTAKE

Check whether the user has provided:
- `vault_path` — absolute path to their Obsidian vault root

**If missing, ask:**

```
What's the absolute path to your Obsidian vault? (e.g. /root/obsidian-vault)
```

Do not proceed until confirmed.

---

### PHASE 2: ANALYZE

Run all 4 checks. Capture raw output from each before writing the report.

**Check 1 — Stale drafts (30+ days, unposted):**

```bash
VAULT="VAULT_PATH_HERE"
echo "=== CHECK 1: STALE DRAFTS ==="
find "$VAULT/content/ready-to-post" -name "*.md" -mtime +30 2>/dev/null | while read f; do
  if grep -q '\*\*Posted:\*\* ❌' "$f" 2>/dev/null; then
    days=$(( ($(date +%s) - $(stat -c %Y "$f")) / 86400 ))
    echo "${days}d|${f##$VAULT/}"
  fi
done
echo "=== END CHECK 1 ==="
```

**Check 2 — Incomplete files (no headings, 5+ lines):**

```bash
VAULT="VAULT_PATH_HERE"
echo "=== CHECK 2: INCOMPLETE FILES ==="
find "$VAULT" -name "*.md" \
  -not -path "*/.git/*" \
  -not -path "*/.obsidian/*" \
  -not -path "*/.openclaw/*" | while read f; do
  if ! grep -qE '^#{1,6} ' "$f" 2>/dev/null; then
    lines=$(wc -l < "$f")
    if [ "$lines" -gt 5 ]; then
      echo "${lines}lines|${f##$VAULT/}"
    fi
  fi
done
echo "=== END CHECK 2 ==="
```

**Check 3 — Duplicate filenames:**

```bash
VAULT="VAULT_PATH_HERE"
echo "=== CHECK 3: DUPLICATE FILENAMES ==="
find "$VAULT" -name "*.md" \
  -not -path "*/.git/*" \
  -not -path "*/.obsidian/*" \
  -not -path "*/.openclaw/*" \
  -printf "%f\n" | sort | uniq -d | while read name; do
  echo "DUPE:$name"
  find "$VAULT" -name "$name" \
    -not -path "*/.git/*" \
    -not -path "*/.obsidian/*" | while read f; do
    echo "  PATH:${f##$VAULT/}"
  done
done
echo "=== END CHECK 3 ==="
```

**Check 4 — Empty folders:**

```bash
VAULT="VAULT_PATH_HERE"
echo "=== CHECK 4: EMPTY FOLDERS ==="
find "$VAULT" -type d -empty \
  -not -path "*/.git/*" \
  -not -path "*/.obsidian/*" \
  -not -path "*/.openclaw/*" | while read d; do
  echo "${d##$VAULT/}/"
done
echo "=== END CHECK 4 ==="
```

---

### PHASE 3: OUTPUT

**3a. Create the report directory and file:**

```bash
VAULT="VAULT_PATH_HERE"
DATE=$(date +%Y-%m-%d)
mkdir -p "$VAULT/vault-audit"
REPORT="$VAULT/vault-audit/${DATE}-audit.md"
echo "Report path: $REPORT"
```

**3b. Write the report** using this exact structure:

```markdown
# Vault Cleanup Audit — YYYY-MM-DD

Generated: YYYY-MM-DD HH:MM

**Summary:** 🔴 [N] stale | 🟡 [N] incomplete | 🟡 [N] dupes | 🟢 [N] empty

---

## 🔴 Stale Drafts (30+ days, unposted)

- [Nd old] path/to/file.md
[cap at 15 items — add "...and N more" if over]

## 🟡 Incomplete Files (no headings, 5+ lines)

- path/to/file.md (N lines)
[cap at 15]

## 🟡 Duplicate Filenames

- **filename.md**
  - path/one/filename.md
  - path/two/filename.md
[cap at 15 duplicate names]

## 🟢 Empty Folders

- path/to/folder/
[cap at 15]

---

**What to do:**
- 🔴 Stale drafts: post them, delete them, or archive to `content/posted/`
- 🟡 Incomplete files: finish or trash
- 🟡 Duplicates: merge or rename the less important one
- 🟢 Empty folders: safe to delete (or keep if you're about to use them)
```

**3c. Print the summary to terminal:**

```
✅ Audit saved to: vault-audit/YYYY-MM-DD-audit.md

Summary:
🔴 [N] stale drafts
🟡 [N] incomplete files
🟡 [N] duplicate filenames
🟢 [N] empty folders
```

---

### PHASE 4: SELF-CRITIQUE

Before finalizing, check:

1. **All 4 checks ran** — Confirm output exists between each `=== CHECK N ===` / `=== END CHECK N ===` marker. If a check produced no output, note "0 issues found" in the report — do not skip the section.
2. **Counts are accurate** — The summary line counts must match the actual items listed in each section. Re-count if unsure.
3. **Report saved correctly** — Confirm the file exists at `vault-audit/YYYY-MM-DD-audit.md`. If the write failed, report the error and provide the report content inline.
4. **No blank sections** — Every section must either list items OR say "No issues found." Never leave a section header with nothing below it.

Fix any failures before delivering the final output.

---

## Example Report

```markdown
# Vault Cleanup Audit — 2026-03-01

Generated: 2026-03-01 08:14

**Summary:** 🔴 3 stale | 🟡 2 incomplete | 🟡 1 dupe | 🟢 2 empty

---

## 🔴 Stale Drafts (30+ days, unposted)

- [47d old] content/ready-to-post/linkedin/2026-01-12-ai-systems-post.md
- [38d old] content/ready-to-post/twitter/2026-01-21-founder-ops.md
- [31d old] content/ready-to-post/newsletter/2026-01-28-tools-roundup.md

## 🟡 Incomplete Files (no headings, 5+ lines)

- bambf/research/untitled-notes.md (23 lines)
- thinking/random-thoughts.md (11 lines)

## 🟡 Duplicate Filenames

- **README.md**
  - bambf/brand/README.md
  - bambf/tracking/README.md

## 🟢 Empty Folders

- content/queue/rejected/
- bambf/clients/archived/

---

**What to do:**
- 🔴 Stale drafts: post them, delete them, or archive to `content/posted/`
- 🟡 Incomplete files: finish or trash
- 🟡 Duplicates: merge or rename the less important one
- 🟢 Empty folders: safe to delete (or keep if you're about to use them)
```

---

## Requirements

- Claude Code with bash tool access
- Bash + standard Unix tools: `find`, `grep`, `wc`, `stat`, `date`, `awk`
- Read access to vault directory
- Write access to `vault-audit/` inside the vault (auto-created)
- No APIs, no paid services, no external dependencies
```

## File: `voice-extractor/SKILL-OC.md`
```markdown
---
name: voice-extractor
description: Extract and document someone's authentic writing voice from samples. Use when someone needs a "voice guide," wants to capture their writing DNA, or needs to train AI to write in their style. Also useful for ghostwriting, brand voice documentation, or onboarding writers.
---

**Platform:** OpenClaw (token-optimized)

## Required Inputs

- Writing samples — **minimum 3 samples OR 500 total words**
- Purpose — AI training / ghostwriter onboarding / team alignment
- Confidence zones (optional) — topics where they want more/less authority
- Known anti-patterns (optional) — words/phrases they already want to avoid

**Sample priority (most → least authentic):**
1. Casual Slack or email (raw, unedited)
2. Podcast or call transcript
3. LinkedIn posts or articles
4. Website copy (often edited, least authentic)

**Minimum gate:** Under 500 words → stop: "Too short. Add 2–3 more samples — emails, Slack messages, or transcripts work best."

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | Top 5 voice traits + 3 do/don't rules | Fast reference |
| `standard` | Full Voice Guide: tone, vocabulary, rhythm, structure | AI training, ghostwriting |
| `deep` | Full guide + 10 sample rewrites + rules checklist + AI training examples | Onboarding writers, content team |

## Phase 1: Sample Assessment

Assess: authenticity (polished vs. raw), variety (contexts covered), exclusions (platform tics, typos, borrowed phrases).

Output: "I have [X samples / Y words]. Quality: [high/medium]. Using [full/quick] mode. Excluding: [what and why]."

## Phase 2: Extract Core Energy

**Role:** Teacher / Challenger / Cheerleader / Straight-shooter
**Default energy:** Calm authority / High enthusiasm / Understated confidence
**Recurring themes:** Topics appearing unprompted across samples

## Phase 3: Phrase Extraction

Extract from samples (quote exact examples):
- **Transition phrases** — how they shift topics
- **Emphasis phrases** — how they land a point
- **Closers** — how they wrap up

## Phase 4: Confidence Zone Map

| Zone | Description | Language Markers |
|------|-------------|------------------|
| Full authority | Expert topics | No hedging, definitive, "here's what works" |
| Earned perspective | Experienced but not mastery | "In my experience..." |
| Active exploration | Currently learning | "I'm testing this..." |

## Phase 5: Anti-Pattern List

What they'd NEVER say — sourced from sample evidence:
"You never used [word] across [X samples] — it doesn't fit your voice."

## Phase 6: Validation Test (required)

Generate 2 sentences on the same topic:
- **Version A:** Using extracted voice profile
- **Version B:** Wrong voice (contrasting example)

Ask: "Does Version A actually sound like you when you're not overthinking it?"

## Output Format

```markdown
# Voice Guide: [Name/Brand]

**Voice Summary:** [2-3 sentences capturing the essence]
**Core Role:** [Teacher/Challenger/Cheerleader/Straight-shooter]
**Default Energy:** [Calm authority/High enthusiasm/Understated confidence]

## Vocabulary Guide
Use: [words/phrases from samples]
Avoid: [anti-patterns]

## Rhythm Patterns
[Sentence length patterns, paragraph style, structural habits]

## Confidence Zones
[Mapped topics to zones]

## Transition Phrases
[Quoted from samples]

## Emphasis Phrases
[Quoted from samples]

## Closers
[Quoted from samples]

## Validation Examples
A (correct): "[sentence]"
B (wrong): "[sentence]"
```

---
*Skill by Brian Wagner | AI Marketing Architect*
```

## File: `voice-extractor/SKILL.md`
```markdown
---
name: voice-extractor
description: Extract and document someone's authentic writing voice from samples. Use when someone needs a "voice guide," wants to capture their writing DNA, or needs to train AI to write in their style. Also useful for ghostwriting, brand voice documentation, or onboarding writers.
---

# Voice Extractor

AI-generated content all sounds the same. The fix isn't better prompts — it's teaching the AI how you actually communicate.

This skill extracts your communication DNA from writing samples and produces a Voice Guide: documented, tested, and ready to use.

---

## Mode

Detect from context or ask: *"Quick voice snapshot, full Voice Guide, or full guide with examples?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | Top 5 voice characteristics + 3 do/don't rules | Fast style reference, single piece |
| `standard` | Full Voice Guide: tone, vocabulary, rhythm, structure | AI training, ghostwriting, brand documentation |
| `deep` | Full Voice Guide + 10 sample rewrites + writing rules checklist + AI training examples | Onboarding writers, building a brand voice system |

**Default: `standard`** — use `quick` if they just need a fast reference. Use `deep` if they're onboarding a ghostwriter or building a content team.

---

## Context Loading Gates

**Before extracting, collect:**

- [ ] **Writing samples** — minimum 3 samples OR 500 total words (see priority list below)
- [ ] **Purpose of voice guide** — AI training? Ghostwriter onboarding? Team alignment?
- [ ] **Confidence zones** — Any topics where they want to sound more/less authoritative?
- [ ] **Known anti-patterns** — Any words or phrases they already know they want to avoid?

**Sample priority (most → least authentic):**
1. Casual Slack or email (raw, unedited voice)
2. Podcast or call transcript
3. LinkedIn posts or articles
4. Website copy (often edited, less authentic)

**Minimum sample gate:** If samples total under 500 words, stop:
> "These samples are too short to extract reliable patterns. Please add 2-3 more — emails, Slack messages, or transcripts work best. The messier and more casual, the better."

Do not attempt full extraction from under 500 words. Offer quick mode instead.

---

## Phase 1: Sample Quality Assessment

Before extracting, reason through:

1. **Sample authenticity:** Are these samples from edited/polished contexts (website, press) or raw contexts (Slack, email)? More polish = less authentic voice.
2. **Sample variety:** Do the samples cover different contexts (professional, casual, educational)? Single-context samples produce single-dimension voice guides.
3. **Exclusion check:** Identify and flag patterns that are NOT the authentic voice:
   - Platform formatting tics (LinkedIn line breaks, Twitter brevity forcing)
   - Typos and autocorrect errors
   - Phrases borrowed from others (quotes, retweets)
   - Unusually formal writing (legal docs, press releases)
4. **Sample size adequacy:** Is there enough material for full mode, or should I use quick mode?

Output a sample assessment:
> "I have [X samples / Y words] to work with. Quality: [high/medium — why]. I'll use [full/quick] mode. Excluding: [any patterns and why]."

---

## Phase 2: Core Energy Extraction

Identify the fundamental communication mode:

**Role:**
- Teacher (breaks things down systematically)
- Challenger (pushes back on assumptions)
- Cheerleader (builds confidence and momentum)
- Straight-shooter (cuts through BS efficiently)

**Default energy:**
- Calm authority ("Here's what works.")
- High enthusiasm ("This is exciting — let me show you.")
- Understated confidence ("I've seen this a hundred times.")

**Recurring themes:** What topics appear unprompted across samples? These are the things they actually care about.

---

## Phase 3: Phrase Extraction (Systematic)

Scan all samples and extract:

**Transition phrases** (how they shift topics):
- Quote exact examples from samples
- Pattern: "Here's the thing...", "What I've learned...", "Let me put it differently..."

**Emphasis phrases** (how they land a point):
- Quote exact examples
- Pattern: "The reality is...", "This is the part people miss...", "Here's the actual problem..."

**Closers** (how they wrap up):
- Quote exact examples
- Pattern: "That's the move.", "Start there.", "You've got this."

---

## Phase 4: Confidence Zone Mapping

| Zone | Description | Language Markers |
|---|---|---|
| Full authority | Topics they're an expert in | No hedging, definitive statements, "here's what works" |
| Earned perspective | Topics with experience but not mastery | "In my experience...", "What I've found..." |
| Active exploration | Topics they're learning now | "I'm testing this...", "What I'm seeing..." |

Map their stated expertise areas to each zone. This calibration is what makes the voice feel real vs. one-dimensional.

---

## Phase 5: Anti-Pattern Documentation

Extract what they'd NEVER say:
- Words that would feel wrong in their voice
- Phrases that make them cringe
- Tones they naturally avoid
- Industry jargon they hate

Source these from sample evidence where possible: "You never used [word] across [X samples] — it doesn't fit your voice."

---

## Phase 6: Validation Test (REQUIRED)

After extracting the full profile, generate 2 test sentences on the same topic:

**Version A** (using the extracted voice profile):
> "[Sample sentence in their voice]"

**Version B** (wrong voice — contrasting example):
> "[Same content, different voice — shows what to avoid]"

Ask the user: "Does Version A actually sound like you when you're not overthinking it? What feels off?"

This validation catches extraction errors before the guide is put into production.

---

## Quick Mode (`--quick`)

When samples are thin (300–500 words) or time is short:

1. Read 3 samples fast
2. Pull 10 signature phrases
3. Note 3 things they'd never say
4. Write 1 sentence describing their energy

**Output:** Minimum viable voice guide.

**Difference from full mode:**
- Quick: ~10 phrases, 3 anti-patterns, 1-sentence energy descriptor
- Full: Complete profile with confidence calibration, validated test sentences, and source-cited examples

---

## Phase 7: Self-Critique Pass (REQUIRED)

After generating the Voice Guide:

- [ ] Are the extracted phrases actually from the samples, or am I inferring them?
- [ ] Does the anti-pattern list include specific words/phrases, or just vague categories?
- [ ] Do the validation test sentences demonstrate a real difference between in-voice and out-of-voice?
- [ ] Is the confidence zone mapping specific to named topics, or just generic?
- [ ] Would a ghostwriter be able to use this guide without asking follow-up questions?

Flag any issues: "The anti-pattern section only has 2 entries — not enough for a usable guide. I need more samples or direct input from the user."

---

## Output Structure

```markdown
## Voice Guide: [Name] — [Date]

### Sample Assessment
- Samples: [count, types]
- Total words: [count]
- Quality: [high/medium — reason]
- Mode: [quick/full]
- Excluded: [patterns excluded + why]

---

### Core Energy
- Role: [teacher/challenger/cheerleader/straight-shooter]
- Default energy: [description]
- Recurring themes: [list]

### Signature Phrases
**Transitions:**
- "[Phrase]" (source: [email/post])
- "[Phrase]"

**Emphasis:**
- "[Phrase]" (source: [email/post])

**Closers:**
- "[Phrase]"

### Confidence Calibration
**Full authority (no hedging):**
Topics: [list]
Sounds like: "[example sentence]"

**Earned perspective:**
Topics: [list]
Sounds like: "[example sentence]"

**Active exploration:**
Topics: [list]
Sounds like: "[example sentence]"

### Anti-Patterns (Never Use)
- [Word/phrase] — why: [evidence from samples]
- [Word/phrase] — why: [evidence]

### Validation Test
**This sounds like you:**
"[Version A]"

**This doesn't:**
"[Version B — contrast]"

### Self-Critique Notes
[Any gaps, things to validate with user]

### Usage Instructions
- For AI: Paste this guide into your system prompt
- For ghostwriter: Share on day 1 — cuts revision cycles in half
- For team: This is the benchmark for "on brand"
```

---

*Skill by Brian Wagner | AI Marketing Architect | brianrwagner.com*
```

## File: `voice-extractor/VOICE-GUIDE-TEMPLATE.md`
```markdown
# Voice Guide

> Your communication DNA, documented.

---

## 🎯 Core Identity

### Who You Are
| Attribute | Your Voice |
|-----------|------------|
| **Core Energy** | _(calm authority / high enthusiasm / understated confidence / challenger energy)_ |
| **Natural Role** | _(teacher / cheerleader / straight-shooter / challenger / guide)_ |
| **Default Tone** | _(conversational / editorial / direct / warm / provocative)_ |

### What You Care About
_The themes you can't help but return to:_

1. 
2. 
3. 

---

## ✍️ Signature Phrases

### Transitions — How You Shift Topics
| Phrase | When to Use |
|--------|-------------|
| | |
| | |
| | |
| | |

### Emphasis — How You Land a Point
| Phrase | When to Use |
|--------|-------------|
| | |
| | |
| | |
| | |

### Closers — How You Wrap Up
| Phrase | When to Use |
|--------|-------------|
| | |
| | |
| | |

---

## 🎚️ Confidence Calibration

### Full Authority Zone _(no hedging, definitive statements)_
Topics where you're THE expert:

- 
- 
- 

**Voice here:** "Here's what works." / "This is how it's done." / "The answer is..."

### Earned Perspective Zone _(confident but not absolute)_
Topics where you have real experience:

- 
- 
- 

**Voice here:** "What I've found..." / "In my experience..." / "The pattern I see..."

### Active Exploration Zone _(curious, learning out loud)_
Topics you're actively figuring out:

- 
- 
- 

**Voice here:** "What I'm testing..." / "I'm starting to think..." / "Early take:..."

---

## 🚫 Anti-Patterns — What You Never Do

### Words You Never Use
| Banned Word/Phrase | Why It's Wrong | Use Instead |
|--------------------|----------------|-------------|
| | | |
| | | |
| | | |

### Tones You Avoid
- 
- 
- 

### Formatting Habits to Skip
- 
- 

---

## 📐 Structural Patterns

### How You Open
_Your typical first-line energy:_

- [ ] Jump straight to the point
- [ ] Start with a provocative statement
- [ ] Open with a story/scenario
- [ ] Lead with a question
- [ ] Other: _______________

**Example opening in your voice:**
> 

### How You Build
_Your typical structure:_

- [ ] Short punchy paragraphs
- [ ] Longer flowing sections
- [ ] Heavy use of bullet points
- [ ] Numbered lists for steps
- [ ] Mix of all above

### How You Close
_Your typical ending energy:_

- [ ] Clear call to action
- [ ] Thought-provoking question
- [ ] Punchy one-liner
- [ ] Callback to opening
- [ ] Other: _______________

**Example closer in your voice:**
> 

---

## ✅ Voice Check — Quick Reference

Before publishing, ask:

| Check | ✓ |
|-------|---|
| Does this sound like me talking, not writing? | |
| Would I actually say these words out loud? | |
| Is my confidence level calibrated to the topic? | |
| Did I avoid my banned words/phrases? | |
| Does the opening hook match my energy? | |
| Does the closer land the way I close? | |

---

## 📝 Side-by-Side Examples

### ✅ This Sounds Like Me:
> _[Paste an example of content that nails your voice]_

### ❌ This Doesn't:
> _[Paste the same content written in a generic/wrong voice]_

### Why the Difference:
_[Note what specifically makes the first one "you"]_

---

## 🤖 AI Prompt Integration

Paste this into any AI system prompt to write in your voice:

```
VOICE INSTRUCTIONS:

Write as [NAME] — [one-sentence description of your energy].

Core patterns:
- [Signature phrase 1]
- [Signature phrase 2]
- [Signature phrase 3]

Never use: [banned words]
Always: [key habit]

Confidence calibration:
- Expert topics (full authority): [list]
- Experienced topics (earned perspective): [list]
- Learning topics (exploratory): [list]
```

---

_Generated with Voice Extractor by Brian Wagner_
_https://brianwagner4.gumroad.com_
```

## File: `youtube-summarizer/README.md`
```markdown
# youtube-summarizer

Fetch YouTube transcripts and generate structured summaries with key insights.

## Best For

- Fast executive briefings from video content
- Competitive intelligence from interviews and podcasts
- Knowledge capture from long-form YouTube material

## What It Does

- Detects YouTube URLs and extracts video IDs
- Pulls transcript + metadata through MCP tooling
- Produces a concise, structured summary format

## Install

```bash
mkdir -p "$HOME/.codex/skills"
cp -R youtube-summarizer "$HOME/.codex/skills/youtube-summarizer"
```

## Dependencies

- MCP YouTube transcript server at `/root/clawd/mcp-server-youtube-transcript`
- Node.js runtime for transcript-fetch commands

## Typical Output

- Video metadata (title, channel, views, publish date)
- Main thesis
- 3-5 key insights
- Practical takeaway
```

## File: `youtube-summarizer/SKILL-OC.md`
```markdown
---
name: youtube-summarizer
description: Automatically fetch YouTube video transcripts, generate structured summaries, and send full transcripts to messaging platforms. Detects YouTube URLs and provides metadata, key insights, and downloadable transcripts.
version: 2.0.0
author: abe238
tags: [youtube, transcription, summarization, video, telegram]
---

**Platform:** OpenClaw (token-optimized)

## When to Activate

User shares a YouTube URL (youtube.com/watch, youtu.be, youtube.com/shorts) or asks to summarize/transcribe a YouTube video.

## Mode

| Mode | Output | Use when |
|------|--------|----------|
| `quick` | 3-bullet TL;DR + single key takeaway | Fast consumption |
| `standard` | Full summary: thesis + insights + takeaway | Learning, research |
| `deep` | Full summary + chapter breakdown + content repurposing opportunities | Turn video into content asset |

## Dependency

MCP YouTube Transcript server at `/root/clawd/mcp-server-youtube-transcript`

Install if missing:
```bash
cd /root/clawd && git clone https://github.com/kimtaeyoon83/mcp-server-youtube-transcript.git
cd mcp-server-youtube-transcript && npm install && npm run build
```

## Workflow

**1. Extract video ID** from URL patterns:
- `youtube.com/watch?v=VIDEO_ID`
- `youtu.be/VIDEO_ID`
- `youtube.com/shorts/VIDEO_ID`

**2. Fetch transcript:**
```bash
cd /root/clawd/mcp-server-youtube-transcript && node --input-type=module -e "
import { getSubtitles } from './dist/youtube-fetcher.js';
const result = await getSubtitles({ videoID: 'VIDEO_ID', lang: 'en' });
console.log(JSON.stringify(result, null, 2));
" > /tmp/yt-transcript.json
```

**3. Parse JSON:**
- `result.metadata.title` — video title
- `result.metadata.author` — channel name
- `result.metadata.viewCount` — view count
- `result.metadata.publishDate` — publish date
- `result.lines` — transcript segments array
- Full text: `result.lines.map(l => l.text).join(' ')`

**4. Generate summary:**

```markdown
📹 **Video:** [title]
📺 **Channel:** [author] | 👁 [viewCount] views | 📅 [publishDate]

**In one sentence:** [thesis]

**Key Insights:**
1. [Insight with timestamp reference]
2. [Insight]
3. [Insight]

**Main Takeaway:** [single most important point]

**Content Angles** (deep mode only):
- [Repurposing opportunity]
```

**5. Save transcript** to `/tmp/[video-id]-transcript.md` (timestamped)

**6. Telegram delivery** (if in OpenClaw context):
```bash
curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendDocument" \
  -F "chat_id=${CHAT_ID}" \
  -F "document=@/tmp/[video-id]-transcript.md"
```

---
*Skill by abe238 | AI Marketing Skills*
```

## File: `youtube-summarizer/SKILL.md`
```markdown
---
name: youtube-summarizer
description: Automatically fetch YouTube video transcripts, generate structured summaries, and send full transcripts to messaging platforms. Detects YouTube URLs and provides metadata, key insights, and downloadable transcripts.
version: 2.0.0
author: abe238
tags: [youtube, transcription, summarization, video, telegram]
---

# YouTube Summarizer Skill

Automatically fetch transcripts from YouTube videos, generate structured summaries, and deliver full transcripts to messaging platforms.

## Mode

Detect from context or ask: *"Quick TL;DR, full summary, or full summary with content angles?"*

| Mode | What you get | Best for |
|------|-------------|----------|
| `quick` | 3-bullet TL;DR + single key takeaway | Fast consumption, sharing a clip |
| `standard` | Full structured summary: thesis, insights, takeaway | Learning, note-taking, research |
| `deep` | Full summary + chapter breakdown + content repurposing opportunities | Turning a video into a content asset |

**Default: `standard`** — use `quick` if they just want the gist. Use `deep` if they want to extract the video into usable content.

---

## Why This vs ChatGPT?

**Problem with ChatGPT:** It can't access YouTube transcripts directly. You have to manually copy/paste captions or use a third-party tool first, then feed the text to ChatGPT. Multi-step, clunky, loses video metadata.

**This skill provides:**
1. **One-step transcript extraction** - Drop a YouTube URL, get the full transcript automatically
2. **Structured summarization** - Consistent format (thesis → insights → takeaway) every time, not random bullet points
3. **Video metadata included** - Title, channel, views, publish date embedded in summary
4. **Full transcript delivery** - Saves timestamped transcript to file and sends to Telegram/chat platforms
5. **Works from VPS/cloud** - Uses Android client emulation to bypass YouTube's cloud IP blocking (where yt-dlp fails)
6. **Multi-language support** - Auto-fetches in requested language with English fallback

**You can replicate this** by manually enabling captions, copying text, pasting to ChatGPT, reformatting the output, saving to a file, and uploading. Takes 5-10 minutes. This skill does it in 15-20 seconds.

## When to Use

Activate this skill when:
- User shares a YouTube URL (youtube.com/watch, youtu.be, youtube.com/shorts)
- User asks to summarize or transcribe a YouTube video
- User requests information about a YouTube video's content
- You need to analyze video content for research or content creation

## Dependencies

**Required:** MCP YouTube Transcript server must be installed at:
`/root/clawd/mcp-server-youtube-transcript`

If not present, install it:
```bash
cd /root/clawd
git clone https://github.com/kimtaeyoon83/mcp-server-youtube-transcript.git
cd mcp-server-youtube-transcript
npm install && npm run build
```

## Workflow

### 1. Detect YouTube URL
Extract video ID from these patterns:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/shorts/VIDEO_ID`
- Direct video ID: `VIDEO_ID` (11 characters)

### 2. Fetch Transcript
Run this command to get the transcript:
```bash
cd /root/clawd/mcp-server-youtube-transcript && node --input-type=module -e "
import { getSubtitles } from './dist/youtube-fetcher.js';
const result = await getSubtitles({ videoID: 'VIDEO_ID', lang: 'en' });
console.log(JSON.stringify(result, null, 2));
" > /tmp/yt-transcript.json
```

Replace `VIDEO_ID` with the extracted ID. Read the output from `/tmp/yt-transcript.json`.

### 3. Process the Data

Parse the JSON to extract:
- `result.metadata.title` - Video title
- `result.metadata.author` - Channel name
- `result.metadata.viewCount` - Formatted view count
- `result.metadata.publishDate` - Publication date
- `result.actualLang` - Language used
- `result.lines` - Array of transcript segments

Full text: `result.lines.map(l => l.text).join(' ')`

### 4. Generate Summary

Create a structured summary using this template:

```markdown
📹 **Video:** [title]
👤 **Channel:** [author] | 👁️ **Views:** [views] | 📅 **Published:** [date]

**🎯 Main Thesis:**
[1-2 sentence core argument/message]

**💡 Key Insights:**
- [insight 1]
- [insight 2]
- [insight 3]
- [insight 4]
- [insight 5]

**📝 Notable Points:**
- [additional point 1]
- [additional point 2]

**🔑 Takeaway:**
[Practical application or conclusion]
```

Aim for:
- Main thesis: 1-2 sentences maximum
- Key insights: 3-5 bullets, each 1-2 sentences
- Notable points: 2-4 supporting details
- Takeaway: Actionable conclusion

### 5. Save Full Transcript

Save the complete transcript to a timestamped file:
```
/root/clawd/transcripts/YYYY-MM-DD_VIDEO_ID.txt
```

Include in the file:
- Video metadata header (title, channel, URL, date)
- Full transcript text
- URL reference for easy lookup

### 6. Platform-Specific Delivery

**If channel is Telegram:**
```bash
message --action send --channel telegram --target CHAT_ID \
  --filePath /root/clawd/transcripts/YYYY-MM-DD_VIDEO_ID.txt \
  --caption "📄 YouTube Transcript: [title]"
```

**If channel is other/webchat:**
Just reply with the summary (no file attachment).

### 7. Reply with Summary

Send the structured summary as your response to the user.

## Real Case Study

**User:** Content creator researching competitor YouTube strategies

**Challenge:** Needed to analyze 20+ competitor videos per week to identify trending topics, messaging patterns, and content gaps. Manual process: watch video, take notes, transcribe key quotes. Time: 30-45 min per video.

**Solution with youtube-summarizer:**
1. Drop YouTube URL in chat
2. Get structured summary in 20 seconds
3. Full transcript saved for reference
4. Copy key insights for content planning doc

**Workflow example:**
```
User: Analyze this video: https://youtube.com/watch?v=abc123
[20 seconds later]

📹 Video: "10 AI Tools That Will Replace Your Job in 2026"
👤 Channel: TechFuturist | 👁️ Views: 847K | 📅 Published: Jan 12, 2026

🎯 Main Thesis:
AI tools are automating creative and knowledge work faster than expected, but the real opportunity is in augmentation, not replacement.

💡 Key Insights:
- ChatGPT usage among marketers jumped from 12% to 67% in one year
- Video editing time reduced by 80% using AI tools like Descript
- The biggest wins come from combining tools (Notion + Claude + Zapier)
- Companies hiring "AI workflow designers" to optimize human-AI collaboration
- Workers using AI secretly outperform peers by 40% (BCG study)

📝 Notable Points:
- Shows examples of 3 small businesses that 10× output with AI
- Warns against over-automation: "AI can write, but can't think strategically"

🔑 Takeaway:
Don't ask "Will AI replace me?" Ask "How can I use AI to become 10× more valuable?"
```

**Results after 8 weeks:**
- **Time saved:** 25 hours/week (from 600 min to 60 min for 20 videos)
- **Content output:** 3 videos/week (up from 1/week)
- **Better insights:** Full transcripts searchable, found patterns missed when just watching
- **Competitive intel:** Built database of 160+ competitor video summaries with key quotes
- **ROI quote:** "This skill turned competitor research from a chore into an assembly line."

## Why This Beats Manual Methods

| Method | Time | Gets Metadata | Structured Output | Searchable Archive | Cloud-Friendly |
|--------|------|---------------|-------------------|-------------------|----------------|
| Watch + take notes | 30-45 min | No | No | Manual only | N/A |
| YouTube transcript feature | 5 min | No | No | No | Yes |
| yt-dlp | 2-5 min | Yes | No | Yes | ❌ Blocked on VPS |
| Copy to ChatGPT | 10 min | No | Sometimes | No | Yes |
| **This skill** | **20 sec** | **Yes** | **Yes** | **Yes** | **✅ Works on VPS** |

## Error Handling

**If transcript fetch fails:**
- Check if video has captions enabled
- Try with `lang: 'en'` fallback if requested language unavailable
- Inform user that transcript is not available and suggest alternatives:
  - Manual YouTube transcript feature (Settings → Show transcript)
  - Video may not have captions
  - Try a different video

**If MCP server not installed:**
- Provide installation instructions
- Offer to install it automatically if in appropriate context

**If video ID extraction fails:**
- Ask user to provide the full YouTube URL or video ID

**If video is age-restricted or private:**
- Inform user that transcript cannot be accessed due to restrictions
- Suggest checking video privacy settings

## Examples

### Example 1: Tech Tutorial

**Input:** `https://youtube.com/watch?v=dQw4w9WgXcQ`

**Output:**
```markdown
📹 **Video:** "Building a SaaS from Scratch: Lessons from $10K MRR"
👤 **Channel:** IndieHackerTV | 👁️ **Views:** 124K | 📅 **Published:** Feb 1, 2026

**🎯 Main Thesis:**
Most SaaS founders fail because they build for 6 months before talking to customers. The path to $10K MRR is customer conversations first, MVP second.

**💡 Key Insights:**
- Interviewed 50 potential customers before writing a single line of code
- First paid customer signed up with a Figma mockup (no product built yet)
- Charged $99/month from day 1 (no free tier, no discounts)
- Spent $0 on ads; all growth from Twitter + Reddit engagement
- Hit $10K MRR in 9 months by saying "no" to feature requests that didn't fit ICP

**📝 Notable Points:**
- Used Stripe payment links before building a billing system
- First 3 customers came from solving their problem in public on Twitter
- Weekly "build in public" updates on Twitter drove 40% of signups

**🔑 Takeaway:**
Validate demand before building. If 10 people won't pay for a mockup, 1,000 won't pay for the real product.
```

### Example 2: Business Strategy Video

**Input:** `https://youtu.be/abc123xyz`

**Output:**
```markdown
📹 **Video:** "Why Notion's Business Model is Genius"
👤 **Channel:** SaaS Breakdowns | 👁️ **Views:** 456K | 📅 **Published:** Jan 28, 2026

**🎯 Main Thesis:**
Notion's growth strategy flips traditional SaaS: give away the product for free to individuals, monetize when they bring it to work.

**💡 Key Insights:**
- 80% of Notion's enterprise deals started with a single employee using the free plan
- Bottom-up adoption = zero sales team needed for first $10M ARR
- Templates marketplace created a content flywheel (100K+ free templates)
- Personal use (free) → Team use (paid) conversion rate: 23% (industry avg: 2-5%)
- Community evangelism replaced traditional marketing (4M+ Reddit/Discord members)

**📝 Notable Points:**
- Notion's viral coefficient: 1.4 (every user invites 1.4 others on average)
- Template creators drive 30% of new user acquisition
- Pricing strategy: free until 10 people = no friction to start

**🔑 Takeaway:**
Build a product individuals love first. Enterprise sales will follow when employees demand it at work.
```

## Quality Guidelines

- **Be concise:** Summary should be scannable in 30 seconds
- **Be accurate:** Don't add information not in the transcript
- **Be structured:** Use consistent formatting for easy reading
- **Be contextual:** Adjust detail level based on video length
  - Short videos (<5 min): Brief summary (3 key insights)
  - Medium videos (5-30 min): Standard format (5 key insights)
  - Long videos (>30 min): Detailed breakdown (7+ insights, split into sections if needed)
- **Extract value:** Focus on actionable insights, data points, and contrarian takes (not generic advice)

## Pro Tips

**For Better Summaries:**
1. **Prioritize data points** - Numbers, percentages, study citations stand out
2. **Extract quotes** - Memorable one-liners make summaries shareable
3. **Identify frameworks** - If video presents a method/process, extract the steps
4. **Spot contrarian takes** - Unconventional wisdom is more valuable than common advice
5. **Note proof** - Examples, case studies, before/after results add credibility

**For Research Workflows:**
1. **Build a transcript library** - Organize by topic/niche for pattern spotting
2. **Search across transcripts** - Use `grep` or text search to find mentions of specific topics
3. **Track trends** - Same topic across multiple videos = rising trend
4. **Extract prompts** - Save useful frameworks/methods as reusable prompts

**For Content Creation:**
1. **Find content gaps** - What questions are asked but not fully answered?
2. **Analyze top performers** - What structure/pacing do high-view videos use?
3. **Extract hooks** - First 30 seconds of transcript = proven hook patterns
4. **Repurpose insights** - Turn video insights into Twitter threads, blog posts, newsletters

## Configuration

### Standard Mode (default)
```
youtube-summarizer [URL]
```
- Fetches transcript in English
- Generates structured summary
- Saves transcript to file
- Sends to messaging platform if applicable

### Quick Mode
```
youtube-summarizer [URL] --quick
```
- Thesis + 3 key insights only
- No transcript file saved
- Faster processing for rapid research

### Deep Dive Mode
```
youtube-summarizer [URL] --deep
```
- Extended summary with timestamps
- Section-by-section breakdown for long videos
- Includes all notable quotes

### Language-Specific
```
youtube-summarizer [URL] --lang es
```
- Fetches transcript in specified language
- Falls back to English if unavailable

## Installation & Setup

```bash
# 1. Clone and install MCP server
cd /root/clawd
git clone https://github.com/kimtaeyoon83/mcp-server-youtube-transcript.git
cd mcp-server-youtube-transcript
npm install && npm run build

# 2. Test installation
node --input-type=module -e "
import { getSubtitles } from './dist/youtube-fetcher.js';
const result = await getSubtitles({ videoID: 'dQw4w9WgXcQ', lang: 'en' });
console.log(result.metadata.title);
"

# 3. Create transcripts directory
mkdir -p /root/clawd/transcripts

# 4. Verify skill is ready
youtube-summarizer --check-setup
```

## Common Issues

**Issue:** "Transcript not available"
- **Cause:** Video has no captions/subtitles enabled
- **Fix:** Ask video creator to enable captions, or try a different video

**Issue:** "Failed to fetch transcript" (on VPS)
- **Cause:** YouTube may have updated their API
- **Fix:** Update MCP server: `cd /root/clawd/mcp-server-youtube-transcript && git pull && npm install && npm run build`

**Issue:** "Video ID not recognized"
- **Cause:** Malformed URL or unsupported format
- **Fix:** Copy URL directly from YouTube address bar

## Future Enhancements (Roadmap)

- [ ] Multi-video batch processing (analyze playlists)
- [ ] Sentiment analysis on transcript (positive/negative/neutral tone)
- [ ] Speaker diarization (identify different speakers in interviews/panels)
- [ ] Automatic chapter detection (split long videos into logical sections)
- [ ] Cross-video pattern analysis (find common themes across multiple videos)

## Support

Issues or suggestions? Provide:
- YouTube URL that failed
- Error message (if any)
- Expected vs actual behavior
- MCP server version: `cd /root/clawd/mcp-server-youtube-transcript && git rev-parse HEAD`

---

**Built on MCP YouTube Transcript server (Android emulation for cloud reliability).**
**Turn any YouTube video into structured, searchable knowledge in 20 seconds.**
```

## File: `youtube-summarizer/_meta.json`
```json
{
  "owner": "abe238",
  "slug": "youtube-summarizer",
  "displayName": "YouTube Summarizer",
  "latest": {
    "version": "1.0.0",
    "publishedAt": 1769398410293,
    "commit": "https://github.com/clawdbot/skills/commit/dbea5414faa08c97deaceeafc4d4aebfb35b9061"
  },
  "history": []
}
```

## File: `youtube-summarizer/package.json`
```json
{
  "name": "youtube-summarizer",
  "version": "1.0.0",
  "description": "Automatically fetch YouTube video transcripts, generate structured summaries, and deliver full transcripts to messaging platforms",
  "author": "abe238",
  "license": "MIT",
  "keywords": [
    "youtube",
    "transcript",
    "summarization",
    "video",
    "telegram",
    "clawdbot",
    "ai-agent"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/abe238/youtube-summarizer"
  },
  "clawdbot": {
    "skill": true,
    "requires": {
      "node": ">=18.0.0"
    },
    "dependencies": {
      "external": [
        {
          "name": "mcp-server-youtube-transcript",
          "url": "https://github.com/kimtaeyoon83/mcp-server-youtube-transcript",
          "path": "/root/clawd/mcp-server-youtube-transcript",
          "install": "git clone https://github.com/kimtaeyoon83/mcp-server-youtube-transcript.git /root/clawd/mcp-server-youtube-transcript && cd /root/clawd/mcp-server-youtube-transcript && npm install && npm run build"
        }
      ]
    }
  }
}
```

## File: `youtube-summarizer/examples/sample-output.md`
```markdown
# Sample Output

## Example 1: AI Productivity Video

**Input:** `https://youtu.be/EZ4EjJ0iDDQ`

**Output:**

```
📹 **Video:** THE MISTAKE COSTING YOU 40% IN PRODUCTIVITY - Stop Teaching AI Basics
👤 **Channel:** AI News & Strategy Daily | 👁️ **Views:** 22.2k | 📅 **Published:** 2025-12-03

**🎯 Main Thesis:**
Most AI training focuses on the wrong layer—either basic "101" prompting or advanced "401" technical implementation. The missing middle ("201 level") is where actual productivity gains happen, and it requires management skills, not tool skills.

**💡 Key Insights:**
- Microsoft study of 300K employees showed 80% stopped using AI after initial excitement crater; survivors treated AI as a management skill, not a tool skill
- The "201 level" gap includes six critical skills: context assembly, quality judgment, task decomposition, iterative refinement, workflow integration, and frontier recognition
- BCG/Harvard study found consultants were 19% less accurate on tasks outside AI's capability frontier, showing the danger of applying one mental model without understanding boundaries
- Two effective work patterns emerged: "Centaur mode" (clearly divided tasks) for high-stakes work, and "Cyborg mode" (fluid integration) for creative work
- The apprentice model is collapsing—juniors miss routine work that builds judgment, creating a long-term expertise deficit

**📝 Notable Points:**
- Token consumption leaderboards at major orgs are dominated by senior execs and distinguished engineers—not because of technical skill, but management capability and domain knowledge
- Organizations need experts mapping the frontier and creating guardrails, while enabling non-experts to work safely within those boundaries
- Fear of doing it wrong is the biggest adoption blocker—without clear organizational guidance, talented people see AI as risk and avoid it
- Employees who receive more than 5 hours of formal AI training are double-digit percentage points more likely to become regular users

**🔑 Takeaway:**
Getting 80% of your organization to "201 level" AI fluency—treating AI like a capable but inexperienced collaborator who needs management—distinguishes companies that realize real gains from those stuck with a few power users and mass disengagement. Invest in the judgment layer, not just tool deployment.
```

**File saved:** `/root/clawd/transcripts/2026-01-26_EZ4EjJ0iDDQ.txt`

---

## Example 2: Short Tutorial Video

**Input:** `https://youtu.be/dQw4w9WgXcQ`

**Output:**

```
📹 **Video:** How to Build a REST API in 10 Minutes
👤 **Channel:** DevTips | 👁️ **Views:** 450k | 📅 **Published:** 2024-08-15

**🎯 Main Thesis:**
You can build a production-ready REST API quickly using modern frameworks and best practices without overengineering.

**💡 Key Insights:**
- Express.js with TypeScript provides type safety and rapid development
- Middleware pattern handles authentication, validation, and error handling cleanly
- Environment variables manage configuration across dev, staging, and production
- Simple folder structure (routes, controllers, services) scales better than complex architectures

**📝 Notable Points:**
- Use Zod for runtime validation instead of manual checks
- Prisma ORM eliminates SQL boilerplate while maintaining type safety
- Docker containerization ensures consistency across environments

**🔑 Takeaway:**
Start simple with proven patterns, add complexity only when needed, and prioritize developer experience to ship faster.
```

**File saved:** `/root/clawd/transcripts/2024-08-15_dQw4w9WgXcQ.txt`

---

## Platform-Specific Behavior

### Telegram
- Summary sent as text message
- Full transcript sent as `.txt` file attachment
- Caption on file: "📄 YouTube Transcript: [Video Title]"

### Webchat / Discord / Other
- Summary sent as text message
- Transcript saved locally but not sent as file
- User informed of save location

---

## Transcript File Format

```
VIDEO: THE MISTAKE COSTING YOU 40% IN PRODUCTIVITY - Stop Teaching AI Basics
URL: https://youtu.be/EZ4EjJ0iDDQ
Channel: AI News & Strategy Daily
Views: 22.2k
Published: 2025-12-03

=== TRANSCRIPT ===

Toward the very end of 2025, a study happened that we didn't pay attention to. Microsoft tracked 300,000 employees using AI C-Pilot. Excitement peaked for the first three weeks. Then there was a crater of disappointment...

[full transcript continues...]
```
```

