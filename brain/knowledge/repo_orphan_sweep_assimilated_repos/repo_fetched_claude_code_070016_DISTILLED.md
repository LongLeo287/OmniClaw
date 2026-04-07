---
id: repo-fetched-claude-code-070016
type: knowledge
owner: OA
registered_at: 2026-04-05T04:16:28.579227
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_claude-code_070016

## Assimilation Report
Auto-cloned repository: FETCHED_claude-code_070016

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">

<h1>CLAURST</h1>
<h3><em>Your Favorite Terminal Coding Agent, now in Rust</em></h3>
<img src="public/Rustle.png" alt="Rustle the Crab" width="150" />


  <p>
    <a href="https://github.com/kuberwastaken/claurst"><img src="https://img.shields.io/badge/Built_with-Rust-CE4D2B?style=for-the-badge&logo=rust&logoColor=white" alt="Built with Rust"></a>
    <a href="https://github.com/kuberwastaken/claurst"><img src="https://img.shields.io/badge/Tracking-None-2E8B57?style=for-the-badge" alt="No Tracking"></a>
    <a href="https://github.com/kuberwastaken/claurst"><img src="https://img.shields.io/badge/Experimental_Features-Unlocked-6A0DAD?style=for-the-badge" alt="Experimental Features Unlocked"></a>
  </p>

  <br />

  <img src="public/screenshot.png" alt="CLAURST in action" width="1080" />
</div>

---

> [!NOTE]
> **100% Coverage complete from original source** on the [`src-rust`](https://github.com/kuberwastaken/claurst/tree/main/src-rust) and it's already much more memory effecient than the original port, along with no tracking, experimental features unlocked and more. We're at a stage where I'm using Claurst to further build Claurst in <2 days and it's incredibly exciting.
>
> A huge revision with multi provider support, many more features and optimisations is actively being worked on and will be pushed ideally by tomorrow :) I would love to hear thoughts, help you set up or squash any bugs you encounter in the process, please don't refrain from [reaching out](https://x.com/kuberwastaken) or [repoting any issues.](https://github.com/Kuberwastaken/claurst/issues/new) Thank you for your support !

---

# IMPORTANT NOTICE

This repository does not hold a copy of the proprietary Claude Code typescript source code.
This is a clean-room Rust reimplementation of Claude Code's behavior.

The process was explicitly two-phase:

Specification [`spec/`](https://github.com/kuberwastaken/claude-code/tree/main/spec) - An AI agent analyzed the source and produced exhaustive behavioral specifications and improvements, deviated from the original: architecture, data flows, tool contracts, system designs. No source code was carried forward.

Implementation [`src-rust/`](https://github.com/kuberwastaken/claude-code/tree/main/src-rust)- A separate AI agent implemented from the spec alone, never referencing the original TypeScript. The output is idiomatic Rust that reproduces the behavior, not the expression.

This mirrors the legal precedent established by Phoenix Technologies v. IBM (1984) — clean-room engineering of the BIOS — and the principle from Baker v. Selden (1879) that copyright protects expression, not ideas or behavior.

The analysis below is commentary on publicly available software, protected under fair use (17 U.S.C. § 107). Code excerpts are quoted to illustrate technical points from a public source - no unauthorized access was involved in this process or research.

# Claude Code's Entire Source Code Got Leaked via a Sourcemap in npm, Let's Talk About It

## Technical Breakdown

>**PS:** I've also published this [breakdown on my blog](https://kuber.studio/blog/AI/Claude-Code's-Entire-Source-Code-Got-Leaked-via-a-Sourcemap-in-npm,-Let's-Talk-About-it) with a better reading experience and UX :)

Earlier today (March 31st, 2026) - Chaofan Shou on X discovered something that Anthropic probably didn't want the world to see: the **entire source code** of Claude Code, Anthropic's official AI coding CLI, was sitting in plain sight on the npm registry via a sourcemap file bundled into the published package.

[![The tweet announcing the leak](https://raw.githubusercontent.com/kuberwastaken/claude-code/main/public/leak-tweet.png)](https://raw.githubusercontent.com/kuberwastaken/claude-code/main/public/leak-tweet.png)

This repository is a backup of that leaked source, and this README is a full breakdown of what's in it, how the leak happened and most importantly, the things we now know that were never meant to be public.

Let's get into it.

## How Did This Even Happen?

This is the part that honestly made me go "...really?"

When you publish a JavaScript/TypeScript package to npm, the build toolchain often generates **source map files** (`.map` files). These files are a bridge between the minified/bundled production code and the original source, they exist so that when something crashes in production the stack trace can point you to the *actual* line of code in the *original* file, not some unintelligible line 1, column 48293 of a minified blob.

But the fun part is **source maps contain the original source code**. The actual, literal, raw source code, embedded as strings inside a JSON file.

The structure of a `.map` file looks something like this:

```json
{
  "version": 3,
  "sources": ["../src/main.tsx", "../src/tools/BashTool.ts", "..."],
  "sourcesContent": ["// The ENTIRE original source code of each file", "..."],
  "mappings": "AAAA,SAAS,OAAO..."
}
```

That `sourcesContent` array? That's everything.
Every file. Every comment. Every internal constant. Every system prompt. All of it, sitting right there in a JSON file that npm happily serves to anyone who runs `npm pack` or even just browses the package contents.

This is not a novel attack vector. It's happened before and honestly it'll happen again.

The mistake is almost always the same: someone forgets to add `*.map` to their `.npmignore` or doesn't configure their bundler to skip source map generation for production builds. With Bun's bundler (which Claude Code uses), source maps are generated by default unless you explicitly turn them off.

[![Claude Code source files exposed in npm package](https://raw.githubusercontent.com/kuberwastaken/claude-code/main/public/claude-files.png)](https://raw.githubusercontent.com/kuberwastaken/claude-code/main/public/claude-files.png)

The funniest part is, there's an entire system called ["Undercover Mode"](#undercover-mode--do-not-blow-your-cover) specifically designed to prevent Anthropic's internal information from leaking.

They built a whole subsystem to stop their AI from accidentally revealing internal codenames in git commits... and then shipped the entire source in a `.map` file, likely by Claude.

---

## What's Claude Under The Hood?

If you've been living under a rock, Claude Code is Anthropic's official CLI tool for coding with Claude and the most popular AI coding agent.

From the outside, it looks like a polished but relatively simple CLI.

From the inside, It's a **785KB [`main.tsx`](https://github.com/kuberwastaken/claude-code/blob/main/src-rust/crates/cli/src/main.rs)** entry point, a custom React terminal renderer, 40+ tools, a multi-agent orchestration system, a background memory consolidation engine called "dream," and much more

Enough yapping, here's some parts about the source code that are genuinely cool that I found after an afternoon deep dive:

---

## BUDDY - A Tamagotchi Inside Your Terminal

I am not making this up.

Claude Code has a full **Tamagotchi-style companion pet system** called "Buddy." A **deterministic gacha system** with species rarity, shiny variants, procedurally generated stats, and a soul description written by Claude on first hatch like OpenClaw.

The entire thing lives in [`buddy/`](https://github.com/kuberwastaken/claude-code/tree/main/src-rust/crates) and is gated behind the `BUDDY` compile-time feature flag.

### The Gacha System

Your buddy's species is determined by a **Mulberry32 PRNG**, a fast 32-bit pseudo-random number generator seeded from your `userId` hash with the salt `'friend-2026-401'`:

```typescript
// Mulberry32 PRNG - deterministic, reproducible per-user
function mulberry32(seed: number): () => number {
  return function() {
    seed |= 0; seed = seed + 0x6D2B79F5 | 0;
    var t = Math.imul(seed ^ seed >>> 15, 1 | seed);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  }
}
```

Same user always gets the same buddy.

### 18 Species (Obfuscated in Code)

The species names are hidden via `String.fromCharCode()` arrays - Anthropic clearly didn't want these showing up in string searches. Decoded, the full species list is:

| Rarity | Species |
|--------|---------|
| **Common** (60%) | Pebblecrab, Dustbunny, Mossfrog, Twigling, Dewdrop, Puddlefish |
| **Uncommon** (25%) | Cloudferret, Gustowl, Bramblebear, Thornfox |
| **Rare** (10%) | Crystaldrake, Deepstag, Lavapup |
| **Epic** (4%) | Stormwyrm, Voidcat, Aetherling |
| **Legendary** (1%) | Cosmoshale, Nebulynx |

On top of that, there's a **1% shiny chance** completely independent of rarity. So a Shiny Legendary Nebulynx has a **0.01%** chance of being rolled. Dang.

### Stats, Eyes, Hats, and Soul

Each buddy gets procedurally generated:
- **5 stats**: `DEBUGGING`, `PATIENCE`, `CHAOS`, `WISDOM`, `SNARK` (0-100 each)
- **6 possible eye styles** and **8 hat options** (some gated by rarity)
- **A "soul"** as mentioned, the personality generated by Claude on first hatch, written in character

The sprites are rendered as **5-line-tall, 12-character-wide ASCII art** with multiple animation frames. There are idle animations, reaction animations, and they sit next to your input prompt.

### The Lore

The code references April 1-7, 2026 as a **teaser window** (so probably for easter?), with a full launch gated for May 2026. The companion has a system prompt that tells Claude:

```
A small {species} named {name} sits beside the user's input box and 
occasionally comments in a speech bubble. You're not {name} - it's a 
separate watcher.
```

So it's not just cosmetic - the buddy has its own personality and can respond when addressed by name. I really do hope they ship it.

---

## KAIROS - "Always-On Claude"

Inside [`assistant/`](https://github.com/kuberwastaken/claude-code/tree/main/src-rust/crates), there's an entire mode called **KAIROS** i.e. a persistent, always-running Claude assistant that doesn't wait for you to type. It watches, logs, and **proactively** acts on things it notices.

This is gated behind the `PROACTIVE` / `KAIROS` compile-time feature flags and is completely absent from external builds.

### How It Works

KAIROS maintains **append-only daily log files** - it writes observations, decisions, and actions throughout the day. On a regular interval, it receives `<tick>` prompts that let it decide whether to act proactively or stay quiet.

The system has a **15-second blocking budget**, any proactive action that would block the user's workflow for more than 15 seconds gets deferred. This is Claude trying to be helpful without being annoying.

### Brief Mode

When KAIROS is active, there's a special output mode called **Brief**, extremely concise responses designed for a persistent assistant that shouldn't flood your terminal. Think of it as the difference between a chatty friend and a professional assistant who only speaks when they have something valuable to say.

### Exclusive Tools

KAIROS gets tools that regular Claude Code doesn't have:

| Tool | What It Does |
|------|-------------|
| **SendUserFile** | Push files directly to the user (notifications, summaries) |
| **PushNotification** | Send push notifications to the user's device |
| **SubscribePR** | Subscribe to and monitor pull request activity |

 ---

## ULTRAPLAN - 30-Minute Remote Planning Sessions

Here's one that's wild from an infrastructure perspective.

**ULTRAPLAN** is a mode where Claude Code offloads a complex planning task to a **remote Cloud Container Runtime (CCR) session** running **Opus 4.6**, gives it up to **30 minutes** to think, and lets you approve the result from your browser.

The basic flow:

1. Claude Code identifies a task that needs deep planning
2. It spins up a remote CCR session via the `tengu_ultraplan_model` config
3. Your terminal shows a polling state - checking every **3 seconds** for the result
4. Meanwhile, a browser-based UI lets you watch the planning happen and approve/reject it
5. When approved, there's a special sentinel value `__ULTRAPLAN_TELEPORT_LOCAL__` that "teleports" the result back to your local terminal

---

## The "Dream" System - Claude Literally Dreams

Okay this is genuinely one of the coolest things in here.

Claude Code has a system called **autoDream** ([`services/autoDream/`](https://github.com/kuberwastaken/claude-code/tree/main/src-rust/crates)) - a background memory consolidation engine that runs as a **forked subagent**. The naming is very intentional. It's Claude... dreaming.

This is extremely funny because [I had the same idea for LITMUS last week - OpenClaw subagents creatively having leisure time to find fun new papers](https://github.com/Kuberwastaken/litmus)

### The Three-Gate Trigger

The dream doesn't just run whenever it feels like it. It has a **three-gate trigger system**:

1. **Time gate**: 24 hours since last dream
2. **Session gate**: At least 5 sessions since last dream  
3. **Lock gate**: Acquires a consolidation lock (prevents concurrent dreams)

All three must pass. This prevents both over-dreaming and under-dreaming.

### The Four Phases

When it runs, the dream follows four strict phases from the prompt in [`consolidationPrompt.ts`](https://github.com/kuberwastaken/claude-code/blob/main/src-rust/crates/query/src/compact.rs):

**Phase 1 - Orient**: `ls` the memory directory, read `MEMORY.md`, skim existing topic files to improve.

**Phase 2 - Gather Recent Signal**: Find new information worth persisting. Sources in priority: daily logs → drifted memories → transcript search.

**Phase 3 - Consolidate**: Write or update memory files. Convert relative dates to absolute. Delete contradicted facts.

**Phase 4 - Prune and Index**: Keep `MEMORY.md` under 200 lines AND ~25KB. Remove stale pointers. Resolve contradictions.

The prompt literally says:

> *"You are performing a dream - a reflective pass over your memory files. Synthesize what you've learned recently into durable, well-organized memories so that future sessions can orient quickly."*

The dream subagent gets **read-only bash** - it can look at your project but not modify anything. It's purely a memory consolidation pass.

---

## Undercover Mode - "Do Not Blow Your Cover"


This one is fascinating from a corporate strategy perspective.

Anthropic employees (identified by `USER_TYPE === 'ant'`) use Claude Code on public/open-source repositories. **Undercover Mode** ([`utils/undercover.ts`](https://github.com/kuberwastaken/claude-code/blob/main/src-rust/crates/core/src/lib.rs)) prevents the AI from accidentally revealing internal information in commits and PRs.

When active, it injects this into the system prompt:

```
## UNDERCOVER MODE - CRITICAL

You are operating UNDERCOVER in a PUBLIC/OPEN-SOURCE repository. Your commit
messages, PR titles, and PR bodies MUST NOT contain ANY Anthropic-internal
information. Do not blow your cover.

NEVER include in commit messages or PR descriptions:
- Internal model codenames (animal names like Capybar
... [TRUNCATED]
```

### File: LICENSE.md
```md
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Sourc
... [TRUNCATED]
```

### File: spec\00_overview.md
```md
# Claude Code — Master Architecture Overview

> **Repository:** `X:\Bigger-Projects\Claude-Code`
> **Primary Language:** TypeScript/TSX (~1,902 files, ~800K+ LOC)
> **Secondary Language:** Rust (~47 files, in-progress port)
> **Bundler:** Bun
> **UI Framework:** Custom Ink (React reconciler for terminal)
> **Runtime Target:** Node.js / Bun CLI

---

## 1. What Is Claude Code?

Claude Code is an AI-powered CLI tool and coding assistant. It is a full-featured interactive terminal application that:

- Embeds a Claude AI model as an agentic coding assistant
- Runs in the terminal using a custom React-based TUI (Terminal User Interface)
- Executes tools (file read/write, bash, grep, web search, etc.) with user permission
- Supports multi-agent task delegation, background agents, and swarm mode
- Integrates with IDEs (VS Code, JetBrains) via direct-connect bridge
- Supports remote sessions via WebSocket/SSE transports
- Has a plugin/skills marketplace
- Includes voice input (speech-to-text)
- Features a companion "buddy" system (Tamagotchi-style)
- Syncs sessions to the cloud via the bridge protocol

---

## 2. Repository Structure

```
Claude-Code/
├── src/                          # Main TypeScript/TSX source (34 MB, ~1,902 files)
│   ├── main.tsx                  # PRIMARY ENTRY POINT (4,683 lines)
│   ├── replLauncher.tsx          # REPL mode launcher
│   ├── query.ts                  # Main query/turn execution engine (69KB)
│   ├── QueryEngine.ts            # Query engine class (46KB)
│   ├── Tool.ts                   # Tool base framework (30KB)
│   ├── Task.ts                   # Task definitions
│   ├── commands.ts               # Command registry (25KB)
│   ├── context.ts                # Context management
│   ├── cost-tracker.ts           # Cost tracking (11KB)
│   ├── costHook.ts               # Cost hooks
│   ├── history.ts                # Session history (14KB)
│   ├── dialogLaunchers.tsx       # Dialog launchers (23KB)
│   ├── interactiveHelpers.tsx    # Interactive UI helpers (57KB)
│   ├── projectOnboardingState.ts # Project onboarding state
│   ├── setup.ts                  # Initialization (21KB)
│   ├── tasks.ts                  # Task management
│   ├── tools.ts                  # Tools registry (17KB)
│   ├── ink.ts                    # Ink export shim
│   │
│   ├── assistant/                # Assistant session history
│   ├── bootstrap/                # Bootstrap/state
│   ├── bridge/                   # Bridge protocol (31 files)
│   ├── buddy/                    # Companion pet system (6 files)
│   ├── cli/                      # CLI framework & transports (19 files)
│   ├── commands/                 # 87 slash commands (207 files)
│   ├── components/               # React/Ink UI components (389 files, 32 subdirs)
│   ├── constants/                # Constants & config values (21 files)
│   ├── context/                  # React context providers (9 files)
│   ├── coordinator/              # Coordinator mode logic
│   ├── entrypoints/              # Multiple entry points (8 files)
│   ├── hooks/                    # React hooks (104 files)
│   ├── ink/                      # Custom Ink terminal framework (96 files)
│   ├── keybindings/              # Keyboard shortcut system (14 files)
│   ├── memdir/                   # Memory directory system (8 files)
│   ├── migrations/               # Settings migrations (11 files)
│   ├── moreright/                # useMoreRight hook
│   ├── native-ts/                # Native TypeScript bindings (4 files)
│   ├── outputStyles/             # Output style loader
│   ├── plugins/                  # Plugin system (2 files)
│   ├── query/                    # Query helpers (4 files)
│   ├── remote/                   # Remote session management (4 files)
│   ├── schemas/                  # Zod/JSON schemas
│   ├── screens/                  # Top-level screen layouts (3 files)
│   ├── server/                   # Direct-connect server (3 files)
│   ├── services/                 # Business logic services (130 files)
│   ├── skills/                   # Claude skills/slash commands (20 files)
│   ├── tools/                    # Tool implementations (40+ tools, 184 files)
│   ├── types/                    # TypeScript type definitions
│   ├── utils/                    # Utility functions (~564 files)
│   └── voice/                    # Voice integration
│
├── claude-code-rust/             # Rust port (in-progress, 47 files)
│   ├── Cargo.toml                # Workspace manifest
│   ├── tools/                    # 27 files — tool implementations
│   ├── query/                    # 5 files — query system
│   ├── cli/                      # 3 files — CLI framework
│   ├── api/                      # 2 files — API bindings
│   ├── bridge/                   # 2 files — bridge protocol
│   ├── commands/                 # 2 files — command system
│   ├── core/                     # 2 files — core utilities
│   ├── mcp/                      # 2 files — MCP integration
│   └── tui/                      # 2 files — terminal UI
│
├── public/                       # Static assets
├── README.md                     # Main documentation (27KB)
└── .git/                         # Git metadata
```

---

## 3. High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                           │
│  Terminal (Ink TUI) ←→ React Components ←→ Hooks ←→ Context     │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                       MAIN APPLICATION                           │
│  main.tsx → REPL.tsx → PromptInput → MessageList                │
│  Commands (87) ←→ Command Registry ←→ Plugin System             │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                       QUERY ENGINE                               │
│  query.ts → QueryEngine.ts → Tool execution → Response handling  │
│  Token budget → Stop hooks → Compact → History                   │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                       TOOL SYSTEM (40+ tools)                    │
│  BashTool, FileReadTool, FileEditTool, FileWriteTool             │
│  GlobTool, GrepTool, WebFetchTool, WebSearchTool                 │
│  AgentTool, TaskCreateTool, MCPTool, SkillTool, ...              │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                       SERVICES LAYER                             │
│  API Client (claude.ts) → Analytics → SessionMemory             │
│  AutoDream → Compact → RateLimit → MCP servers                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                       TRANSPORT LAYER                            │
│  CLI (local) / Bridge (remote) / IDE direct-connect             │
│  SSETransport | WebSocketTransport | HybridTransport            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Core Subsystems

### 4.1 Query / Turn Execution (`query.ts`, `QueryEngine.ts`)
The core loop that:
1. Takes user input
2. Builds the API request (system prompt + history + tools)
3. Streams the response from Claude API
4. Handles tool use (executes tools, feeds results back)
5. Manages token budget and context compaction
6. Tracks cost

### 4.2 Tool Framework (`Tool.ts`, `tools/`)
- Base `Tool` abstract class/interface
- Input schema validation (Zod)
- Permission system (each tool declares required permissions)
- 40+ tool implementations
- Sandboxing for dangerous tools

### 4.3 Terminal UI (`ink/`, `components/`)
- Custom React reconciler that renders to terminal
- Layout engine based on Yoga (flexbox for terminal)
- Event system (keyboard, mouse, focus)
- ANSI/CSI/escape sequence processing
- Components: Messages, PromptInput, Spinner, Dialogs, etc.

### 4.4 Commands System (`commands/`, `commands.ts`)
- 87 slash commands (e.g., `/compact`, `/diff`, `/plan`, `/mcp`)
- Plugin-contributed commands
- Command registry with fuzzy matching
- Keybinding integration

### 4.5 Bridge Protocol (`bridge/`)
- Enables remote/cloud-synced sessions
- JWT-authenticated WebSocket/SSE connection to cloud backend servers
- REPL bridge for IDE integration
- Message polling, flush gates, session runners

### 4.6 Multi-Agent System (`tools/AgentTool.ts`, `components/agents/`)
- Spawn sub-agents as isolated Claude instances
- Background task execution
- Coordinator mode (orchestrate multiple agents)
- Swarm mode (parallel worker agents)
- Team system for collaborative agents

### 4.7 Memory System (`memdir/`, `services/SessionMemory/`, `services/autoDream/`)
- Short-term: session history
- Long-term: memdir (markdown files in `~/.claude/memory/`)
- Auto-consolidation: "dream" service consolidates memories during idle
- Memory scanning/relevance scoring for context injection

### 4.8 MCP Integration (`tools/MCPTool.ts`, `components/mcp/`, `entrypoints/mcp.ts`)
- Model Context Protocol server support
- Dynamic tool registration from MCP servers
- Resource management
- Elicitation dialog support

### 4.9 Plugin/Skills System (`plugins/`, `skills/`, `commands/plugin/`)
- Built-in plugins
- Marketplace for community plugins
- Skills: user-invocable slash command macros
- Plugin trust model with approval flow

### 4.10 IDE Integration (`bridge/`, `hooks/useIDEIntegration.tsx`)
- VS Code / JetBrains extensions connect via direct-connect
- Live diff viewing in IDE
- File selection sync (IDE → Claude)
- Status indicator in IDE

---

## 5. Data Flow: A User Turn

```
1. User types in PromptInput
2. Input submitted → useCommandQueue processes
3. If slash command: dispatched to command handler
4. If regular prompt: sent to query.ts runQuery()
5. QueryEngine builds API request:
   - System prompt (from constants/prompts.ts + CLAUDE.md)
   - Message history (from history.ts)
   - Available tools (filtered by permission)
   - Token budget constraints
6. Stream response from the Claude API (services/api/claude.ts)
7. For each content block:
   - text → render AssistantTextMessage
   - thinking → render AssistantThinkingMessage
   - tool_use → execute tool, show permission dialog if needed
8. Tool results fed back into next API request
9. Loop until stop condition (no more tool use, stop hook, budget exceeded)
10. Final response rendered, history updated, cost tracked
```

---

## 6. Key Files by Importance

| Rank | File | Size | Role |
|------|------|------|------|
| 1 | `src/main.tsx` | 4,683 lines | Primary entry point, app initialization |
| 2 | `src/query.ts` | 69KB | Main query execution loop |
| 3 | `src/QueryEngine.ts` | 46KB | Query engine class |
| 4 | `src/interactiveHelpers.tsx` | 57KB | Interactive UI helpers |
| 5 | `src/Tool.ts` | 30KB | Tool base framework |
| 6 | `src/commands.ts` | 25KB | Command registry |
| 7 | `src/dialogLaunchers.tsx` | 23KB | Dialog launch system |
| 8 | `src/setup.ts` | 21KB | Initialization |
| 9 | `src/tools.ts` | 17KB | Tools registry |
| 10 | `src/history.ts` | 14KB | Session history |

---

## 7. Permission Model

Claude Code uses a layered permission system:

1. **Automatic** — Read-only operations, info queries
2. **Ask Once** — Prompt user, remember for session
3. **Ask Always** — Prompt user every time
4. **Deny** — Block completely

Permission rules are stored in settings (global `~/.claude/settings.json`, project `.claude/settings.json`) and can be configured with patterns.

Permission categories:
- `Bash` — Shell command execution
- `FileRead` — Reading files/directories
- `FileEdit` — Editing existing files
- `FileWrite` — Creating new files
- `WebFetch` — HTTP requests
- `MCP` — MCP tool calls
- `Sandbox` — Sandboxed execution

---

## 8. Settings System

Layered settings (in priority order):
1. **Managed** — Enterprise/managed settings (read-only)
2. **Local project** — `.claude/settings.local.json` (gitignored)
3. **Project** — `.claude/settings.json` (shared)
4. **Global** — `~/.claude/settings.json`

Settings include: model selection, permission rules, API key, theme, keybindings, MCP server configurations, beta features.

---

## 9. Model Support

Based on migration files, the model evolution:
- `claude-3-sonnet` → `claude-sonnet-1m` → `claude-sonnet-4-5` → `claude-sonnet-4-6`
- `claude-3-opus` → `claude-opus-1m` → `claude-opus` → (various)
- `claude-3-5-haiku` → (current)
- `claude-haiku-4-5` (current haiku)

Current defaults (as of source): `claude-sonnet-4-6` and `claude-opus-4-6`

---

## 10. Analytics & Telemetry

- **First-party logging** — Session events to the backend (`services/analytics/`)
- **Datadog** — Performance metrics
- **Growthbook** — Feature flags / A/B testing
- **Opt-out** — `services/api/metricsOptOut.ts` handles user opt-out

---

## 11. Spec Document Index

| File | Contents |
|------|----------|
| `00_overview.md` | This file — master architecture overview |
| `01_core_entry_query.md` | Entry points, query system, history, cost tracking |
| `02_commands.md` | All 87 slash commands |
| `03_tools.md` | All 40+ tool implementations |
| `04_components_core_messages.md` | Top-level components and message components |
| `05_components_agents_permissions_design.md` | Agents, permissions, design system, feature modules |
| `06_services_context_state.md` | Services, context providers, state, screens, server |
| `07_hooks.md` | All React hooks |
| `08_ink_terminal.md` | Ink terminal rendering framework |
| `09_bridge_cli_remote.md` | Bridge protocol, CLI framework, remote sessions |
| `10_utils.md` | All utility functions (~564 files) |
| `11_special_systems.md` | Buddy, memory, keybindings, skills, voice, plugins |
| `12_constants_types.md` | All constants, types, and configuration |
| `13_rust_codebase.md` | Rust port/rewrite |
| `INDEX.md` | Quick-reference index |

---

*Generated from source analysis of the Claude Code codebase. ~1,902 TypeScript/TSX files, ~800K+ lines of code.*

```

### File: spec\01_core_entry_query.md
```md
# Claude Code — Core Entry Points & Query System

## Table of Contents

1. [entrypoints/cli.tsx — Bootstrap Dispatcher](#entrypointsclisx--bootstrap-dispatcher)
2. [main.tsx — Full CLI Entry Point](#maintsx--full-cli-entry-point)
3. [replLauncher.tsx — REPL UI Launcher](#repplaunchertsx--repl-ui-launcher)
4. [entrypoints/init.ts — Initialization & Telemetry](#entrypointsinits--initialization--telemetry)
5. [entrypoints/mcp.ts — MCP Server Entrypoint](#entrypointsmcpts--mcp-server-entrypoint)
6. [entrypoints/agentSdkTypes.ts — Agent SDK Public API](#entrypointsagentsdktypests--agent-sdk-public-api)
7. [entrypoints/sandboxTypes.ts — Sandbox Configuration Types](#entrypointssandboxtypests--sandbox-configuration-types)
8. [entrypoints/sdk/coreSchemas.ts — SDK Core Zod Schemas](#entrypointssdkcoreshematss--sdk-core-zod-schemas)
9. [entrypoints/sdk/coreTypes.ts — SDK Core TypeScript Types](#entrypointssdkcoretypests--sdk-core-typescript-types)
10. [entrypoints/sdk/controlSchemas.ts — SDK Control Protocol Schemas](#entrypointssdkcontrolschematss--sdk-control-protocol-schemas)
11. [query.ts — Core Async Query Loop](#queryts--core-async-query-loop)
12. [QueryEngine.ts — Stateful Query Engine (SDK/Headless)](#queryenginets--stateful-query-engine-sdkheadless)
13. [query/config.ts — Query Configuration Snapshot](#queryconfigts--query-configuration-snapshot)
14. [query/deps.ts — Query Dependency Injection](#querydepsts--query-dependency-injection)
15. [query/stopHooks.ts — Stop Hook Orchestration](#querystophooksts--stop-hook-orchestration)
16. [query/tokenBudget.ts — Token Budget Tracking](#querytokenbudgetts--token-budget-tracking)
17. [context.ts — System & User Context Providers](#contextts--system--user-context-providers)
18. [history.ts — Prompt History Management](#historyts--prompt-history-management)
19. [cost-tracker.ts — Session Cost Tracking](#cost-trackerts--session-cost-tracking)
20. [costHook.ts — React Cost Summary Hook](#costhookts--react-cost-summary-hook)
21. [projectOnboardingState.ts — Project Onboarding State](#projectonboardingstatets--project-onboarding-state)
22. [bootstrap/state.ts — Global Session State](#bootstrapstatets--global-session-state)
23. [assistant/sessionHistory.ts — Remote Session History Pagination](#assistantsessionhistoryts--remote-session-history-pagination)

---

## entrypoints/cli.tsx — Bootstrap Dispatcher

### Purpose

The very first module executed when a user runs `claude`. Acts as a lightweight bootstrap dispatcher that checks process arguments for known fast-paths **before** loading any heavy modules. Each fast-path dynamically imports only what it needs. The full CLI (`main.tsx`) is only loaded when no fast-path matches.

### Key Flow

```
process.argv parsing
  ├── --version / -v → print MACRO.VERSION, exit (zero imports)
  ├── --dump-system-prompt → dump rendered system prompt (ant-only, DUMP_SYSTEM_PROMPT feature)
  ├── --claude-in-chrome-mcp → runClaudeInChromeMcpServer()
  ├── --chrome-native-host → runChromeNativeHost()
  ├── --computer-use-mcp → runComputerUseMcpServer() (CHICAGO_MCP feature)
  ├── --daemon-worker=<kind> → runDaemonWorker() (DAEMON feature)
  ├── remote-control|rc|remote|sync|bridge → bridgeMain() (BRIDGE_MODE feature)
  ├── daemon → daemonMain() (DAEMON feature)
  ├── ps|logs|attach|kill|--bg|--background → bg handlers (BG_SESSIONS feature)
  ├── new|list|reply → templatesMain() (TEMPLATES feature)
  ├── environment-runner → environmentRunnerMain() (BYOC_ENVIRONMENT_RUNNER feature)
  ├── self-hosted-runner → selfHostedRunnerMain() (SELF_HOSTED_RUNNER feature)
  ├── --worktree + --tmux → execIntoTmuxWorktree()
  └── (default) → startCapturingEarlyInput() → import main.tsx → cliMain()
```

### Top-Level Side Effects (at module load time)

| Side Effect | Purpose |
|---|---|
| `process.env.COREPACK_ENABLE_AUTO_PIN = '0'` | Prevent yarnpkg from being added to package.json |
| `process.env.NODE_OPTIONS += '--max-old-space-size=8192'` | CCR environment (16GB containers) heap size |
| `ABLATION_BASELINE` flag | Sets multiple `CLAUDE_CODE_*` env vars for harness-science L0 ablation |

### Exports

```typescript
// No named exports — module executes main() IIFE at bottom
async function main(): Promise<void>  // internal, not exported
```

### Feature Flags Checked

- `DUMP_SYSTEM_PROMPT` — ant-only system prompt dump
- `CHICAGO_MCP` — computer-use MCP server
- `DAEMON` — daemon worker and supervisor
- `BRIDGE_MODE` — remote control bridge
- `BG_SESSIONS` — background session management
- `TEMPLATES` — template job commands
- `BYOC_ENVIRONMENT_RUNNER` — BYOC headless runner
- `SELF_HOSTED_RUNNER` — self-hosted runner
- `ABLATION_BASELINE` — harness-science baseline

### Dependencies

- `bun:bundle` (`feature`)
- `../utils/startupProfiler.js`
- `../utils/config.js` (enableConfigs)
- Various fast-path modules loaded dynamically

---

## main.tsx — Full CLI Entry Point

### Purpose

The main CLI module. Loaded only after `entrypoints/cli.tsx` determines no fast-path matches. Defines the Commander.js command tree, handles all CLI flags, orchestrates startup (migrations, trust dialog, MCP config, tool loading), and launches either the interactive REPL or the headless/print (`-p`) path.

### Exported Functions

```typescript
export async function main(): Promise<void>
export function startDeferredPrefetches(): void
```

#### `main()`

The primary entry point for the full CLI. Responsibilities in order:

1. **Security**: Sets `process.env.NoDefaultCurrentDirectoryInExePath = '1'` (Windows PATH attack prevention)
2. **Warning handler**: `initializeWarningHandler()`
3. **Signal handlers**: SIGINT (skip in print mode), exit cursor reset
4. **Early arg processing**:
   - `cc://` / `cc+unix://` URL rewriting (DIRECT_CONNECT feature)
   - `--handle-uri` deep link handling (LODESTONE feature)
   - `claude assistant [sessionId]` rewriting (KAIROS feature)
   - `claude ssh <host>` rewriting (SSH_REMOTE feature)
5. **Settings flag parsing**: `eagerLoadSettings()` runs before `init()`
6. **Commander.js setup**: Defines the complete command tree (see CLI flags below)
7. **`init()`** call: Validates configs, sets up network, telemetry loading promise
8. **Migration run**: `runMigrations()` at version `CURRENT_MIGRATION_VERSION = 11`
9. **Trust check**: Shows trust dialog if not previously accepted
10. **Telemetry init**: `initializeTelemetryAfterTrust()`
11. **Session setup**: model, permissions, MCP servers, tools, agents
12. **Launch**: Either `showSetupScreens()` + `launchRepl()`, or headless `runHeadless()`

#### `startDeferredPrefetches()`

Called after first REPL render to avoid blocking the initial paint. Skipped when:
- `CLAUDE_CODE_EXIT_AFTER_FIRST_RENDER=1`
- `--bare` mode (isBareMode())

Prefetches (fire-and-forget):
- `initUser()`
- `getUserContext()`
- `prefetchSystemContextIfSafe()`
- `getRelevantTips()`
- AWS/GCP credentials (if Bedrock/Vertex enabled)
- `countFilesRoundedRg()` (3 second timeout)
- `initializeAnalyticsGates()`
- `prefetchOfficialMcpUrls()`
- `refreshModelCapabilities()`
- `settingsChangeDetector.initialize()`
- `skillChangeDetector.initialize()` (non-bare only)

### Constants

| Constant | Value | Purpose |
|---|---|---|
| `CURRENT_MIGRATION_VERSION` | `11` | Version gate for running config migrations |

### CLI Flags (Commander.js)

| Flag | Type | Description |
|---|---|---|
| `-p, --print <prompt>` | `string` | Non-interactive/headless mode |
| `--model <model>` | `string` | Model override |
| `--fallback-model <model>` | `string` | Fallback model for retry |
| `--permission-mode <mode>` | enum | Permission mode for tool execution |
| `--dangerously-skip-permissions` | `boolean` | Bypass all permission checks |
| `--verbose` | `boolean` | Verbose output |
| `--debug` | `boolean` | Debug mode |
| `--mcp-config <file>` | `string` | MCP config file path |
| `--add-dir <dir>` | `string[]` | Additional directories for CLAUDE.md |
| `--resume [sessionId]` | `string?` | Resume previous session |
| `--bare` | `boolean` | Simple/stripped mode (no UI extras) |
| `--settings <path|json>` | `string` | Flag-layer settings override |
| `--setting-sources <sources>` | `string` | Allowed settings sources |
| `--output-format <format>` | string | Output format for headless mode |
| `--max-turns <n>` | `number` | Max turns in headless mode |
| `--max-budget-usd <n>` | `number` | Cost budget limit |
| `--task-budget <n>` | `number` | API task budget |
| `--no-streaming` | `boolean` | Disable streaming |
| `--worktree <branch>` | `string` | Git worktree mode |
| `--agent <type>` | `string` | Main thread agent type |
| `--tmux` / `--tmux=classic` | `boolean` | Use tmux |
| `--plugin-dir <dir>` | `string[]` | Session-only plugin directories |
| `--input-format <format>` | string | Input format |
| `--sdk-betas <betas>` | `string` | Comma-separated SDK beta headers |
| `--allowedTools <tools>` | `string` | Tool allowlist (CLI override) |
| `--disallowedTools <tools>` | `string` | Tool denylist (CLI override) |

### Migration Functions

Executed in `runMigrations()` when `globalConfig.migrationVersion !== 11`:

| Function | Purpose |
|---|---|
| `migrateAutoUpdatesToSettings()` | Move auto-update config |
| `migrateBypassPermissionsAcceptedToSettings()` | Move bypass flag |
| `migrateEnableAllProjectMcpServersToSettings()` | Move MCP enable setting |
| `resetProToOpusDefault()` | Reset Pro model to Opus |
| `migrateSonnet1mToSonnet45()` | Rename model string |
| `migrateLegacyOpusToCurrent()` | Upgrade legacy Opus |
| `migrateSonnet45ToSonnet46()` | Rename to Sonnet 4.6 |
| `migrateOpusToOpus1m()` | Rename to Opus 1m |
| `migrateReplBridgeEnabledToRemoteControlAtStartup()` | Rename bridge flag |
| `resetAutoModeOptInForDefaultOffer()` | Reset auto mode opt-in (TRANSCRIPT_CLASSIFIER) |
| `migrateFennecToOpus()` | ant-only Fennec model migration |

### Top-Level Side Effects

```typescript
profileCheckpoint('main_tsx_entry')    // startup profiling
startMdmRawRead()                       // parallel MDM subprocess (plutil/reg query)
startKeychainPrefetch()                 // parallel macOS keychain reads
```

### Key Internal Functions

```typescript
function logManagedSettings(): void
function isBeingDebugged(): boolean
function logSessionTelemetry(): void
function getCertEnvVarTelemetry(): Record<string, boolean>
async function logStartupTelemetry(): Promise<void>
function runMigrations(): void
function prefetchSystemContextIfSafe(): void
function loadSettingsFromFlag(settingsFile: string): void
function loadSettingSourcesFromFlag(settingSourcesArg: string): void
function eagerLoadSettings(): void
function initializeEntrypoint(isNonInteractive: boolean): void
```

### Pending State Types (feature-gated)

```typescript
type PendingConnect = {
  url: string | undefined
  authToken: string | undefined
  dangerouslySkipPermissions: boolean
}

type PendingAssistantChat = {
  sessionId?: string
  discover: boolean
}

type PendingSSH = {
  host: string | undefined
  cwd: string | undefined
  permissionMode: string | undefined
  dangerouslySkipPermissions: boolean
  local: boolean
  extraCliArgs: string[]
}
```

### Feature Flags

`DIRECT_CONNECT`, `KAIROS`, `SSH_REMOTE`, `LODESTONE`, `COORDINATOR_MODE`, `TRANSCRIPT_CLASSIFIER`, `BREAK_CACHE_COMMAND`, `HISTORY_SNIP`, `DAEMON`, `BG_SESSIONS`, `TEMPLATES`

---

## replLauncher.tsx — REPL UI Launcher

### Purpose

Thin async launcher that dynamically imports `App` and `REPL` components (avoiding circular dependencies) and renders them into the Ink root. Exists as a separate file so that `App` and `REPL` are loaded lazily.

### Exports

```typescript
export async function launchRepl(
  root: Root,
  appProps: AppWrapperProps,
  replProps: REPLProps,
  renderAndRun: (root: Root, element: React.ReactNode) => Promise<void>,
): Promise<void>
```

### Types

```typescript
type AppWrapperProps = {
  getFpsMetrics: () => FpsMetrics | undefined
  stats?: StatsStore
  initialState: AppState
}
```

### Implementation

Dynamically imports `./components/App.js` and `./screens/REPL.js`, then calls `renderAndRun(root, <App {...appProps}><REPL {...replProps} /></App>)`.

### Dependencies

- `react`
- `./context/stats.js` (type only)
- `./ink.js` (type only)
- `./screens/REPL.js` (type only)
- `./state/AppStateStore.js` (type only)
- `./utils/fpsTracker.js` (type only)

---

## entrypoints/init.ts — Initialization & Telemetry

### Purpose

Handles all early initialization tasks that must complete before the CLI can safely make API calls or show a UI. Memoized so it runs exactly once per process. Telemetry initialization is deferred until after trust is established.

### Exports

```typescript
export const init: () => Promise<void>  // memoized with lodash-es/memoize
export function initializeTelemetryAfterTrust(): void
```

#### `init()` — Memoized Async Initialization

Runs once. Sequence:

1. `enableConfigs()` — validate and activate config system
2. `applySafeConfigEnvironmentVariables()` — apply env vars that are safe before trust
3. `applyExtraCACertsFromConfig()` — inject `NODE_EXTRA_CA_CERTS` before first TLS connection
4. `setupGracefulShutdown()` — register flush/cleanup on exit
5. `initialize1PEventLogging()` + GrowthBook refresh listener (deferred)
6. `populateOAuthAccountInfoIfNeeded()` (fire-and-forget)
7. `initJetBrainsDetection()` (fire-and-forget)
8. `detectCurrentRepository()` (fire-and-forget)
9. `initializeRemoteManagedSettingsLoadingPromise()` (if eligible)
10. `initializePolicyLimitsLoadingPromise()` (if eligible)
11. `recordFirstStartTime()`
12. `configureGlobalMTLS()`
13. `configureGlobalAgents()` (proxy)
14. `preconnectAnthropicApi()` — overlap TCP+TLS with action handler work
15. Upstream proxy initialization (CLAUDE_CODE_REMOTE only)
16. `setShellIfWindows()` — configure git-bash on Windows
17. `registerCleanup(shutdownLspServerManager)`
18. `registerCleanup(cleanupSessionTeams)` (lazy import)
19. `ensureScratchpadDir()` (if scratchpad enabled)

**Error handling**: `ConfigParseError` → shows `InvalidConfigDialog` (interactive) or `stderr` (non-interactive). Other errors re-throw.

#### `initializeTelemetryAfterTrust()`

Called once after trust is established. For remote-settings-eligible users: waits for settings to load, then calls `applyConfigEnvironmentVariables()` before initializing. For SDK/headless with beta tracing: initializes eagerly first.

Internal: `doInitializeTelemetry()` → `setMeterState()` → `initializeTelemetry()` (lazy-loaded OpenTelemetry, ~400KB)

`AttributedCounter` factory: wraps OpenTelemetry `Counter` to always merge `getTelemetryAttributes()` with any additional attributes on each `add()` call.

### Dependencies

- `../bootstrap/state.js`
- `../utils/config.js`
- `../services/lsp/manager.js`
- `../services/oauth/client.js`
- `../services/policyLimits/index.js`
- `../services/remoteManagedSettings/index.js`
- `../utils/apiPreconnect.js`
- `../utils/caCertsConfig.js`
- `../utils/cleanupRegistry
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
