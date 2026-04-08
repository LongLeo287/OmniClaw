---
id: repo-fetched-antigravity-pm-course-151806
type: knowledge
owner: OA
registered_at: 2026-04-05T03:25:26.616451
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_antigravity-pm-course_151806

## Assimilation Report
Auto-cloned repository: FETCHED_antigravity-pm-course_151806

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: IMPLEMENTATION_SPEC.md
```md
# Antigravity PM Course - Implementation Spec

## Overview
Converting Cursor PM Course to Antigravity PM Course with minimal changes.

## Key Mappings

| Cursor | Antigravity |
|--------|-------------|
| `.cursor/` | `.agent/` |
| `.cursor/commands/` | `.agent/workflows/` |
| `.cursor/rules/` | `.agent/rules/` |
| `*.mdc` | `*.md` |
| AI Pane | Conversation view / Agent Manager |
| Composer | Agent Manager |
| Ask Mode | Review-driven mode |
| Agent Mode | Agent-assisted / Agent-driven mode |
| Plan Mode | Planning Mode (with Fast Mode alternative) |
| Cmd+I / Cmd+L | Agent Manager interface |
| Cmd+K | Quick Edit (similar) |

## Antigravity-Specific Concepts to Introduce

### Autonomy Levels (replaces Three Modes)
1. **Agent-driven**: Full autopilot - agent plans, writes, tests independently
2. **Agent-assisted** (recommended): Collaborative - agent suggests, human controls
3. **Review-driven**: Agent only analyzes/reviews, doesn't generate (like Ask mode)

### Planning vs Fast Mode
- **Planning Mode**: Deep thinking, creates artifacts (task.md, implementation_plan.md)
- **Fast Mode**: Quick execution, skips planning

### Agent Manager Interface
- **Inbox**: Tracks all agent conversations
- **Workspaces**: Open different project folders
- **Conversation view**: Where you chat with the agent
- **Editor view**: Toggle to code editor mode
- **Browser integration**: Agents can test in Chrome

### Artifacts System
- `task.md` - Living checklist
- `implementation_plan.md` - Technical blueprint
- `walkthrough.md` - Proof of work with screenshots/videos

### Configuration Locations
- Global rules: `~/.gemini/GEMINI.md`
- Global workflows: `~/.gemini/antigravity/global_workflows/`
- Workspace rules: `.agent/rules/`
- Workspace workflows: `.agent/workflows/`

## Files to Create

### Folder Structure
```
antigravity-pm-course/
└── course-materials/
    ├── .agent/
    │   ├── workflows/
    │   │   ├── start-1-1.md
    │   │   ├── start-1-2.md
    │   │   ├── start-1-3.md
    │   │   ├── start-1-4.md
    │   │   ├── start-1-5.md
    │   │   ├── start-1-6.md
    │   │   ├── start-2-1.md
    │   │   ├── start-2-2.md
    │   │   └── start-2-3.md
    │   └── rules/
    │       ├── course-instructor.md
    │       ├── taskflow-context.md
    │       ├── taskflow-terminology.md
    │       └── SCRIPT_INSTRUCTIONS.md
    ├── company-context/
    │   ├── COMPANY.md
    │   ├── PRODUCT.md
    │   ├── PERSONAS.md
    │   └── COMPETITIVE.md
    └── lesson-modules/
        ├── 1.1-welcome/
        │   └── SCRIPT.md
        ├── 1.2-interface/
        │   ├── SCRIPT.md (REWRITE)
        │   └── interface-practice.md
        ├── 1.3-first-tasks/
        │   ├── SCRIPT.md
        │   ├── meeting-notes-raw.md
        │   ├── product-sync-notes.md
        │   └── user-interviews/
        ├── 1.4-templates-workflows/
        │   ├── SCRIPT.md
        │   └── [supporting files]
        ├── 1.5-three-modes/
        │   ├── SCRIPT.md (REWRITE → autonomy-modes)
        │   └── [supporting files]
        ├── 1.6-project-rules/
        │   └── SCRIPT.md
        ├── 2.1-write-prd/
        │   ├── SCRIPT.md
        │   └── [all supporting files]
        ├── 2.2-analyze-data/
        │   ├── SCRIPT.md
        │   └── [CSV files]
        └── 2.3-product-strategy/
            ├── SCRIPT.md
            └── [frameworks]
```

## Checklist

- [ ] Create folder structure
- [ ] Create workflow files (9 start-*.md)
- [ ] Create rules files (4 files)
- [ ] Copy company-context (4 files, unchanged)
- [ ] Copy/update 1.1-welcome
- [ ] REWRITE 1.2-interface for Agent Manager
- [ ] Copy/update 1.3-first-tasks + supporting files
- [ ] Copy/update 1.4-templates-workflows + supporting files
- [ ] REWRITE 1.5-three-modes for Autonomy Levels
- [ ] Copy/update 1.6-project-rules
- [ ] Copy/update 2.1-write-prd + supporting files
- [ ] Copy/update 2.2-analyze-data + CSV files
- [ ] Copy/update 2.3-product-strategy + frameworks
- [ ] Verify no stray "Cursor" or ".cursor" references

## Find/Replace Rules

1. "Cursor" → "Antigravity" (except in comparisons)
2. "Cursor for Product Managers" → "Antigravity for Product Managers"
3. ".cursor/" → ".agent/"
4. "AI Pane" → "conversation view"
5. "Composer" → "Agent Manager"
6. "Cmd+I" → (varies - Agent Manager doesn't have same shortcut)
7. "Cmd+L" → (varies)
8. ".mdc" → ".md" (in file references)

## Module 1.2 Rewrite Notes (Interface)

Cursor teaches:
- File explorer, Editor pane, AI Pane (3-pane layout)
- Markdown preview (Cmd+Shift+V)
- @ mentions, drag files, Add to Chat
- Cmd+K for inline edits
- Model selector

Antigravity equivalent:
- Agent Manager (Inbox, Workspaces, Conversation view)
- Editor view (toggle from Agent Manager)
- File explorer in editor
- @ mentions work similarly
- Autonomy level selector (Agent-driven/Agent-assisted/Review-driven)
- Model selector (Gemini 3 Pro, Claude options)

## Module 1.5 Rewrite Notes (Three Modes → Autonomy & Planning)

Cursor teaches:
- Ask Mode (read-only)
- Agent Mode (autonomous execution)
- Plan Mode (research → clarify → plan → execute)

Antigravity equivalent:
- Review-driven (like Ask mode - analyze only)
- Agent-assisted (recommended - collaborative)
- Agent-driven (full autopilot)
- Planning Mode vs Fast Mode (separate from autonomy)
- Artifacts system (task.md, implementation_plan.md, walkthrough.md)

```

### File: launch-post-draft-1.md
```md
# Draft 1: The "No More Excuses" Angle

Google's new Cursor competitor: 100% free
My new course to teach it to you: 100% free
My holiday gift to you! 🎁

Antigravity is Google's answer to Cursor.
It's an AI tool to work with files directly on your device.
Not just for developers!
For ANYONE who works with text.

It's 100% free right now.
Access to Gemini 3 Pro.
Even Claude Opus 4.5 (!)
Generate images with Nano Banana Pro right in the chat.
No subscription. No trial. No credit card.

This won't last forever.

I've been teaching Cursor to PMs for months.
But Cursor costs $20/month.
Antigravity removes that barrier completely.

So I rebuilt the entire course for AG.

As usual, it's an Antigravity course taught IN Antigravity.
So everything you do is directly applicable!
The AI IN the tool is your teacher.

What you'll learn:
→ Write PRDs with AI assistance
→ Analyze CSV data and survey results
→ Create strategy documents
→ Build reusable templates and workflows

But here's what most people don't realize:

This isn't just for PM work.

The real I wanted to get this out today...

On-device AI assistants are useful for LIFE:
🔹 Want to reorganize your files?
🔹 Rename hundreds of photos?
🔹 Clean up your Downloads folder?
🔹 Convert documents between formats?
🔹 Troubleshoot why something isn't working?

Just open the files and ask.
Talk to it like a person.
I spend all day in these tools now and am unbelievably productive.

Using AI in a browser is like wearing a straightjacket.
This is a terrible week for a launch.
But I genuinely want to free you!

You've been meaning to learn this stuff.
You've got the time.
The course is free.
The tool is free.
No excuses now!

This is my gift to you.
Happy Holidays 🌲

👉 Comment "Antigravity" and I'll send you the link to the course
```

### File: launch-post-draft-2.md
```md
# Draft 2: The "Holiday Gift" Angle

I have a holiday gift for you.
It's not a PDF.
It's not a webinar.
It's a skill that will save you hundreds of hours.

Google quietly released something called Antigravity.
Think of it as their competitor to Cursor.
An AI-powered workspace that lets you:
- Edit files through conversation
- Analyze data by just asking questions
- Generate documents, images, and more

The wildest part?
It's completely free right now.
Gemini 3 Pro. Claude Opus 4.5. Nano Banana Pro for images.
All of it. Free.

(This won't last forever.)

I've spent the last few months teaching Cursor to product managers.
But Cursor costs $20/month.
Not everyone wanted to pay to learn.

Antigravity changes that.

So I rebuilt my entire PM course for Antigravity.
From scratch.
Completely free.

Here's what you'll actually DO in the course:
✓ Write a real PRD using AI collaboration
✓ Analyze activation data and survey results
✓ Build product strategy documents
✓ Create reusable templates for your workflow

But honestly?
This goes way beyond PM work.

Having an AI assistant on your computer is life-changing for everyday tasks:

Want to find duplicate files cluttering your drive?
Want to batch rename your vacation photos?
Want to convert a folder of files to a different format?
Want to figure out what's eating your disk space?

You just... ask.
Like talking to a helpful friend who happens to be a computer expert.

It's a slow week.
You have time.
The tool is free.
The course is free.

No excuses left.

👉 Comment "ANTIGRAVITY" and I'll send you the link.

Happy holidays.

```

### File: launch-post-draft-3.md
```md
# Draft 3: The "Anyone Can Use This" Angle

You don't need to be a developer to have an AI assistant on your computer.

Want to reorganize thousands of files?
Rename your photos by date?
Find and delete duplicates?
Convert documents between formats?
Figure out what's slowing down your machine?
Clean up years of Downloads folder chaos?

Just ask.
Talk to it like a person.
It figures out the rest.

This is what Antigravity does.

Google's new AI-powered workspace.
Their answer to Cursor.
But here's the thing nobody's talking about:

It's 100% free right now.
Gemini 3 Pro.
Claude Opus 4.5.
Nano Banana Pro for generating images.
All free. No subscription. No trial period.

This will not last.

I've been teaching Cursor to product managers all year.
The #1 objection?
"I don't want to pay $20/month just to learn."

Fair.

Antigravity removes that objection entirely.

So I rebuilt my entire course.
From scratch.
For Antigravity.
Also free.

For PMs specifically, you'll learn:
→ How to write PRDs with AI assistance
→ How to analyze data just by asking questions
→ How to build strategy documents faster
→ How to create templates you'll use forever

But the real unlock?
Once you learn to work with an AI assistant...
You'll use it for everything.
Work. Life. Random Tuesday night projects.

The holidays are quiet.
You've got time.
Tool = free.
Course = free.
Excuses = zero.

My gift to you this year.

👉 Comment "ANTIGRAVITY" and I'll send you the course link.

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for antigravity_pm_course
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: WEBSITE_MIGRATION_PLAN.md
```md
# Antigravity for PMs - Website Migration Plan

## Executive Summary

Clone cursorforpms.com → antigravityforpms.com with the Antigravity PM course content. The site uses Next.js/Nextra documentation framework with course delivery via GitHub releases (users download ZIP, open in Antigravity, run slash commands).

---

## Phase 1: Repository Setup

### 1.1 Create New GitHub Repo

```
Repo name: antigravity-pm-course
Structure:
├── website/                    # Nextra docs site (clone of cursorforpms.com)
│   ├── pages/
│   │   ├── index.mdx          # Homepage
│   │   ├── module-0/          # Getting Started
│   │   ├── module-1/          # Fundamentals
│   │   ├── module-2/          # Advanced PM Work
│   │   └── reference/         # Company context docs
│   ├── public/
│   │   ├── images/
│   │   └── videos/
│   ├── theme.config.tsx
│   ├── next.config.js
│   └── package.json
│
├── course-materials/           # The actual course (current folder)
│   ├── .agent/
│   ├── company-context/
│   └── lesson-modules/
│
├── releases/                   # GitHub release assets
│   └── antigravity-pm-course-v1.0.zip
│
└── README.md
```

### 1.2 Clone Cursor Website Source

**Option A:** If you have access to cursorforpms.com source code, copy it directly
**Option B:** Rebuild using Nextra template with same structure

**Recommended:** Option A if available, otherwise scaffold fresh Nextra site

---

## Phase 2: Content Swap (Cursor → Antigravity)

### 2.1 Global Find & Replace

| Find | Replace With |
|------|--------------|
| Cursor | Antigravity |
| cursor | antigravity |
| cursorforpms.com | antigravityforpms.com |
| Cursor Pro | Antigravity subscription |
| $20/month | [Antigravity pricing] |
| Cursor AI | Antigravity AI |
| Claude | [Antigravity's AI - check branding] |

### 2.2 Branding Updates

| Element | Current (Cursor) | New (Antigravity) |
|---------|------------------|-------------------|
| Logo | Cursor logo | Antigravity logo |
| Primary color | Cursor purple/blue | Antigravity brand colors |
| Favicon | cursor favicon | antigravity favicon |
| OG images | cursor social cards | antigravity social cards |
| Hero video | Cursor demo | Antigravity demo (NEW NEEDED) |

### 2.3 Feature/Concept Name Changes

| Cursor Concept | Antigravity Equivalent |
|----------------|------------------------|
| Composer | Editor view |
| Agent mode | Planning mode |
| Normal mode | Fast mode |
| .cursor/rules | .agent/rules |
| .cursorrules | .agent/rules/*.md |
| Cmd+I / Ctrl+I | [Antigravity shortcut] |
| @codebase | @Files / @Folders |

---

## Phase 3: Website Pages to Update

### 3.1 Homepage (index.mdx)

**Hero Section:**
- [ ] New headline: "Antigravity for Product Managers"
- [ ] New subheadline about Antigravity's PM capabilities
- [ ] New hero video showing Antigravity in action
- [ ] Update CTA buttons

**Who This Is For:**
- [ ] Update tool references (Antigravity not Cursor)
- [ ] Same PM audience targeting

**What You'll Learn:**
- [ ] Update feature names (Editor view, Planning mode, etc.)
- [ ] Keep PM-focused outcomes

**Module Overview:**
- [ ] Update module descriptions
- [ ] Keep same time estimates (~3 hours based on 1.1 update)
- [ ] Update module count if different

**Download CTA:**
- [ ] Link to GitHub releases for Antigravity course
- [ ] Update installation instructions

### 3.2 Module 0: Getting Started

**Pages needed:**
- [ ] `0.1-installation.mdx` - How to install Antigravity
- [ ] `0.2-setup.mdx` - Course folder setup
- [ ] `0.3-first-launch.mdx` - Opening the course

**Content changes:**
- [ ] Antigravity installation steps (different from Cursor)
- [ ] .agent folder structure explanation
- [ ] Slash command system explanation

### 3.3 Module 1: Fundamentals (6 pages)

| Page | Content Source | Key Changes |
|------|----------------|-------------|
| 1.1 Welcome | lesson-modules/1.1-welcome/ | TaskFlow intro |
| 1.2 Interface | lesson-modules/1.2-interface/ | Editor view focus |
| 1.3 First Tasks | lesson-modules/1.3-first-tasks/ | @ mentions |
| 1.4 Templates | lesson-modules/1.4-templates-workflows/ | Communication styles |
| 1.5 Planning Mode | lesson-modules/1.5-autonomy-modes/ | Planning vs Fast mode |
| 1.6 Project Rules | lesson-modules/1.6-project-rules/ | .agent/rules |

### 3.4 Module 2: Advanced PM Work (3 pages)

| Page | Content Source | Key Changes |
|------|----------------|-------------|
| 2.1 Write PRD | lesson-modules/2.1-write-prd/ | PRD workflow |
| 2.2 Analyze Data | lesson-modules/2.2-analyze-data/ | CSV analysis |
| 2.3 Product Strategy | lesson-modules/2.3-product-strategy/ | Strategic frameworks |

### 3.5 Reference Section

**Pages to create from company-context/:**
- [ ] TaskFlow Company Overview (from COMPANY.md)
- [ ] Product Details (from PRODUCT.md)
- [ ] User Personas (from PERSONAS.md)
- [ ] Competitive Landscape (from COMPETITIVE.md)

---

## Phase 4: Technical Setup

### 4.1 Domain & Hosting

- [ ] Purchase antigravityforpms.com
- [ ] Set up Vercel project (or current hosting provider)
- [ ] Configure DNS
- [ ] Set up SSL certificate

### 4.2 Analytics & Tracking

- [ ] Create new Google Analytics property
- [ ] Update GA tracking ID in site config
- [ ] Set up conversion tracking for downloads

### 4.3 GitHub Releases

- [ ] Create first release (v1.0.0)
- [ ] Attach course-materials.zip
- [ ] Write release notes

### 4.4 SEO & Social

- [ ] Update meta titles/descriptions
- [ ] Create OG images for social sharing
- [ ] Update schema.org Course markup
- [ ] Set canonical URLs

---

## Phase 5: Content Creation Needed

### 5.1 New Assets Required

| Asset | Description | Priority |
|-------|-------------|----------|
| Hero video | Screen recording of Antigravity PM workflow | HIGH |
| Logo | Antigravity for PMs logo/wordmark | HIGH |
| Favicon | Site favicon | HIGH |
| OG image | Social share card (1200x630) | MEDIUM |
| Screenshots | UI screenshots for each module page | MEDIUM |
| Module thumbnails | Visual cards for module overview | LOW |

### 5.2 Written Content Updates

| Content | Status | Notes |
|---------|--------|-------|
| Homepage copy | NEEDS UPDATE | Swap Cursor → Antigravity |
| Module descriptions | NEEDS UPDATE | Already done in SCRIPT.md files |
| Installation guide | NEEDS CREATION | Antigravity-specific |
| FAQ | NEEDS UPDATE | Antigravity-specific questions |
| About/Credits | NEEDS UPDATE | Carl Vellotti / Full Stack PM |

---

## Phase 6: Quality Assurance

### 6.1 Pre-Launch Checklist

- [ ] All Cursor references removed
- [ ] All links working (no 404s)
- [ ] GitHub release downloads working
- [ ] Course ZIP extracts correctly
- [ ] Slash commands work in Antigravity
- [ ] Mobile responsive
- [ ] Dark/light mode working
- [ ] Analytics tracking

### 6.2 Course Testing

- [ ] Run through Module 1.1 → 1.6 in Antigravity
- [ ] Run through Module 2.1 → 2.3 in Antigravity
- [ ] Verify all file references work
- [ ] Verify CSV data analysis works
- [ ] Test on fresh Antigravity install

---

## Phase 7: Launch

### 7.1 Soft Launch

1. Deploy to antigravityforpms.com
2. Test with 2-3 beta users
3. Collect feedback
4. Fix issues

### 7.2 Public Launch

1. Announce on LinkedIn
2. Post in Full Stack PM community
3. Share on Twitter/X
4. Email newsletter announcement

---

## Migration Checklist Summary

### Repository
- [ ] Create antigravity-pm-course repo
- [ ] Copy/scaffold Nextra website
- [ ] Copy course-materials folder
- [ ] Create initial GitHub release

### Content
- [ ] Global find/replace (Cursor → Antigravity)
- [ ] Update all concept names (Composer → Editor, etc.)
- [ ] Update homepage content
- [ ] Update/create Module 0 pages
- [ ] Update Module 1 pages
- [ ] Update Module 2 pages
- [ ] Create Reference section pages

### Assets
- [ ] Create hero video
- [ ] Create logo/favicon
- [ ] Create OG images
- [ ] Take screenshots

### Technical
- [ ] Purchase domain
- [ ] Set up hosting
- [ ] Configure analytics
- [ ] Set up GitHub releases

### Testing
- [ ] Full course walkthrough
- [ ] Link checking
- [ ] Mobile testing
- [ ] Cross-browser testing

---

## Questions to Resolve

1. **Do you have the cursorforpms.com source code?** If yes, direct clone is fastest. If no, we scaffold fresh.

2. **Antigravity branding assets?** Do you have official logo, colors, etc. or creating custom "Antigravity for PMs" branding?

3. **Antigravity installation process?** Need to document how users install/access Antigravity (different from Cursor).

4. **Pricing model?** Is the course free like Cursor version? Any premium tiers planned?

5. **Hero video?** Will you record a new demo video or use screenshots initially?

6. **Module 3 (Nano Banana)?** The Cursor site has a Module 3 for visual design. Do you want this for Antigravity? (You mentioned Nano Banana Pro in 1.5 and 1.6)

---

## Estimated Timeline

| Phase | Duration | Dependencies |
|-------|----------|--------------|
| Phase 1: Repo Setup | 1 day | Source code access |
| Phase 2: Content Swap | 1-2 days | None |
| Phase 3: Page Updates | 2-3 days | Content decisions |
| Phase 4: Technical Setup | 1 day | Domain purchase |
| Phase 5: Asset Creation | 2-3 days | Video recording |
| Phase 6: QA | 1-2 days | All above complete |
| Phase 7: Launch | 1 day | QA passed |

**Total: ~10-14 days** (can be compressed with parallel work)

---

## Next Steps

1. **Answer the questions above** (source code, branding, etc.)
2. **Create the GitHub repo**
3. **Start with Phase 1-2** (repo setup + content swap)
4. **Parallel: Create assets** (video, logo, screenshots)
5. **Deploy and test**
6. **Launch!**

```

