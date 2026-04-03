---
id: github.com-ghuntley-how-to-ralph-wiggum-f1d6e067-k
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:53.289761
---

# KNOWLEDGE EXTRACT: github.com_ghuntley_how-to-ralph-wiggum_f1d6e067
> **Extracted on:** 2026-04-01 11:05:58
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521229/github.com_ghuntley_how-to-ralph-wiggum_f1d6e067

---

## File: `.gitignore`
```
/.DS_Store
```

## File: `README.md`
```markdown
# The Ralph Playbook

December 2025 boiled [Ralph's](https://ghuntley.com/ralph/) powerful yet dumb little face to the top of most AI-related timelines.

I try to pay attention to the crazy-smart insights [@GeoffreyHuntley](https://x.com/GeoffreyHuntley) shares, but I can't say Ralph really clicked for me this summer. Now, all of the recent hubbub has made it hard to ignore.

[@mattpocockuk](https://x.com/mattpocockuk/status/2008200878633931247) and [@ryancarson](https://x.com/ryancarson/status/2008548371712135632)'s overviews helped a lot - right until Geoff came in and [said 'nah'](https://x.com/GeoffreyHuntley/status/2008731415312236984).

<img src="references/nah.png" alt="nah" width="500" />

## So what is the optimal way to Ralph?

Many folks seem to be getting good results with various shapes - but I wanted to read the tea leaves as closely as possible from the person who not only captured this approach but also has had the most ass-time in the seat putting it through its paces.

So I dug in to really _RTFM_ on [recent videos](https://www.youtube.com/watch?v=O2bBWDoxO4s) and Geoff's [original post](https://ghuntley.com/ralph/) to try and untangle for myself what works best.

Below is the result - a (likely OCD-fueled) Ralph Playbook that organizes the miscellaneous details for putting this all into practice w/o hopefully neutering it in the process.

> Digging into all of this has also brought to mind some possibly valuable [additional enhancements](#enhancements) to the core approach that aim to stay aligned with the guidelines that make Ralph work so well.

> [!TIP] > [📖 View as Formatted Guide →](https://ClaytonFarr.github.io/ralph-playbook/)

---

## Table of Contents

- [Workflow](#workflow)
- [Key Principles](#key-principles)
- [Loop Mechanics](#loop-mechanics)
- [Files](#files)
- [Enhancements?](#enhancements)

---

## Workflow

A picture is worth a thousand tweets and an hour-long video. Geoff's [overview here](https://ghuntley.com/ralph/) (sign up to his newsletter to see full article) really helped clarify the workflow details for moving from 1) idea → 2) individual JTBD-aligned specs → 3) comprehensive implementation plan → 4) Ralph work loops.

![ralph-diagram.png](references/ralph-diagram.png)

### 🗘 Three Phases, Two Prompts, One Loop

This diagram clarified for me that Ralph isn't just "a loop that codes." It's a funnel with 3 Phases, 2 Prompts, and 1 Loop.

#### Phase 1. Define Requirements (LLM conversation)

- Discuss project ideas → identify Jobs to Be Done (JTBD)
- Break individual JTBD into topic(s) of concern
- Use subagents to load info from URLs into context
- LLM understands JTBD topic of concern: subagent writes `specs/FILENAME.md` for each topic

#### Phase 2 / 3. Run Ralph Loop (two modes, swap `PROMPT.md` as needed)

Same loop mechanism, different prompts for different objectives:

| Mode       | When to use                            | Prompt focus                                            |
| ---------- | -------------------------------------- | ------------------------------------------------------- |
| _PLANNING_ | No plan exists, or plan is stale/wrong | Generate/update `IMPLEMENTATION_PLAN.md` only           |
| _BUILDING_ | Plan exists                            | Implement from plan, commit, update plan as side effect |

_Prompt differences per mode:_

- 'PLANNING' prompt does gap analysis (specs vs code) and outputs a prioritized TODO list—no implementation, no commits.
- 'BUILDING' prompt assumes plan exists, picks tasks from it, implements, runs tests (backpressure), commits.

_Why use the loop for both modes?_

- BUILDING requires it: inherently iterative (many tasks × fresh context = isolation)
- PLANNING uses it for consistency: same execution model, though often completes in 1-2 iterations
- Flexibility: if plan needs refinement, loop allows multiple passes reading its own output
- Simplicity: one mechanism for everything; clean file I/O; easy stop/restart

_Context loaded each iteration:_ `PROMPT.md` + `AGENTS.md`

_PLANNING mode loop lifecycle:_

1. Subagents study `specs/*` and existing `/src`
2. Compare specs against code (gap analysis)
3. Create/update `IMPLEMENTATION_PLAN.md` with prioritized tasks
4. No implementation

_BUILDING mode loop lifecycle:_

1. _Orient_ – subagents study `specs/*` (requirements)
2. _Read plan_ – study `IMPLEMENTATION_PLAN.md`
3. _Select_ – pick the most important task
4. _Investigate_ – subagents study relevant `/src` ("don't assume not implemented")
5. _Implement_ – N subagents for file operations
6. _Validate_ – 1 subagent for build/tests (backpressure)
7. _Update `IMPLEMENTATION_PLAN.md`_ – mark task done, note discoveries/bugs
8. _Update `AGENTS.md`_ – if operational learnings
9. _Commit_
10. _Loop ends_ → context cleared → next iteration starts fresh

#### Concepts

| Term                    | Definition                                                      |
| ----------------------- | --------------------------------------------------------------- |
| _Job to be Done (JTBD)_ | High-level user need or outcome                                 |
| _Topic of Concern_      | A distinct aspect/component within a JTBD                       |
| _Spec_                  | Requirements doc for one topic of concern (`specs/FILENAME.md`) |
| _Task_                  | Unit of work derived from comparing specs to code               |

_Relationships:_

- 1 JTBD → multiple topics of concern
- 1 topic of concern → 1 spec
- 1 spec → multiple tasks (specs are larger than tasks)

_Example:_

- JTBD: "Help designers create mood boards"
- Topics: image collection, color extraction, layout, sharing
- Each topic → one spec file
- Each spec → many tasks in implementation plan

_Topic Scope Test: "One Sentence Without 'And'"_

- Can you describe the topic of concern in one sentence without conjoining unrelated capabilities?
  - ✓ "The color extraction system analyzes images to identify dominant colors"
  - ✗ "The user system handles authentication, profiles, and billing" → 3 topics
- If you need "and" to describe what it does, it's probably multiple topics

---

## Key Principles

### ⏳ Context Is _Everything_

- When 200K+ tokens advertised = ~176K truly usable
- And 40-60% context utilization for "smart zone"
- Tight tasks + 1 task per loop = _100% smart zone context utilization_

This informs and drives everything else:

- _Use the main agent/context as a scheduler_
  - Don't allocate expensive work to main context; spawn subagents whenever possible instead
- _Use subagents as memory extension_
  - Each subagent gets ~156kb that's garbage collected
  - Fan out to avoid polluting main context
- _Simplicity and brevity win_
  - Applies to number of parts in system, loop config, and content
  - Verbose inputs degrade determinism
- _Prefer Markdown over JSON_
  - To define and track work, for better token efficiency

### 🧭 Steering Ralph: Patterns + Backpressure

Creating the right signals & gates to steer Ralph's successful output is **critical**. You can steer from two directions:

- _Steer upstream_
  - Ensure deterministic setup:
    - Allocate first ~5,000 tokens for specs
    - Every loop's context is allocated with the same files so model starts from known state (`PROMPT.md` + `AGENTS.md`)
  - Your existing code shapes what gets used and generated
  - If Ralph is generating wrong patterns, add/update utilities and existing code patterns to steer it toward correct ones
- _Steer downstream_
  - Create backpressure via tests, typechecks, lints, builds, etc. that will reject invalid/unacceptable work
  - Prompt says "run tests" generically. `AGENTS .md` specifies actual commands to make backpressure project-specific
  - Backpressure can extend beyond code validation: some acceptance criteria resist programmatic checks - creative quality, aesthetics, UX feel. LLM-as-judge tests can provide backpressure for subjective criteria with binary pass/fail. ([More detailed thoughts below](#non-deterministic-backpressure) on how to approach this with Ralph.)
- _Remind Ralph to create/use backpressure_
  - Remind Ralph to use backpressure when implementing: "Important: When authoring documentation, capture the why — tests and implementation importance."

### 🙏 Let Ralph Ralph

Ralph's effectiveness comes from how much you trust it do the right thing (eventually) and engender its ability to do so.

- _Let Ralph Ralph_
  - Lean into LLM's ability to self-identify, self-correct and self-improve
  - Applies to implementation plan, task definition and prioritization
  - Eventual consistency achieved through iteration
- _Use protection_
  - To operate autonomously, Ralph requires `--dangerously-skip-permissions` - asking for approval on every tool call would break the loop. This bypasses Claude's permission system entirely - so a sandbox becomes your only security boundary.
  - Philosophy: "It's not if it gets popped, it's when. And what is the blast radius?"
  - Running without a sandbox exposes credentials, browser cookies, SSH keys, and access tokens on your machine
  - Run in isolated environments with minimum viable access:
    - Only the API keys and deploy keys needed for the task
    - No access to private data beyond requirements
    - Restrict network connectivity where possible
  - Options: Docker sandboxes (local), Fly Sprites/E2B/etc. (remote/production) - [additional notes](references/sandbox-environments.md)
  - Additional escape hatches: Ctrl+C stops the loop; `git reset --hard` reverts uncommitted changes; regenerate plan if trajectory goes wrong

### 🚦 Move Outside the Loop

To get the most out of Ralph, you need to get out of his way. Ralph should be doing _all_ of the work, including decided which planned work to implement next and how to implement it. Your job is now to sit on the loop, not in it - to engineer the setup and environment that will allow Ralph to succeed.

_Observe and course correct_ – especially early on, sit and watch. What patterns emerge? Where does Ralph go wrong? What signs does he need? The prompts you start with won't be the prompts you end with - they evolve through observed failure patterns.

_Tune it like a guitar_ – instead of prescribing everything upfront, observe and adjust reactively. When Ralph fails a specific way, add a sign to help him next time.

But signs aren't just prompt text. They're _anything_ Ralph can discover:

- Prompt guardrails - explicit instructions like "don't assume not implemented"
- `AGENTS .md` - operational learnings about how to build/test
- Utilities in your codebase - when you add a pattern, Ralph discovers it and follows it
- Other discoverable, relevant inputs…

And remember, _the plan is disposable:_

- If it's wrong, throw it out, and start over
- Regeneration cost is one Planning loop; cheap compared to Ralph going in circles
- Regenerate when:
  - Ralph is going off track (implementing wrong things, duplicating work)
  - Plan feels stale or doesn't match current state
  - Too much clutter from completed items
  - You've made significant spec changes
  - You're confused about what's actually done

---

## Loop Mechanics

### Outer Loop Control

Geoff's initial minimal form of `loop.sh` script:

```bash
while :; do cat PROMPT.md | claude ; done
```

_Note:_ The same approach can be used with other CLIs; e.g. `amp`, `codex`, `opencode`, etc.

_What controls task continuation?_

The continuation mechanism is elegantly simple:

1. _Bash loop runs_ → feeds `PROMPT.md` to claude
2. _PROMPT.md instructs_ → "Study IMPLEMENTATION_PLAN.md and choose the most important thing"
3. _Agent completes one task_ → updates IMPLEMENTATION_PLAN.md on disk, commits, exits
4. _Bash loop restarts immediately_ → fresh context window
5. _Agent reads updated plan_ → picks next most important thing

_Key insight:_ The IMPLEMENTATION_PLAN.md file persists on disk between iterations and acts as shared state between otherwise isolated loop executions. Each iteration deterministically loads the same files (`PROMPT.md` + `AGENTS.md` + `specs/*`) and reads the current state from disk.

_No sophisticated orchestration needed_ - just a dumb bash loop that keeps restarting the agent, and the agent figures out what to do next by reading the plan file each time.

### Inner Loop Control (Task Execution)

A single task execution has no hard technical limit. Control relies on:

- _Scope discipline_ - PROMPT.md instructs "one task" and "commit when tests pass"
- _Backpressure_ - tests/build failures force the agent to fix issues before committing
- _Natural completion_ - agent exits after successful commit

_Ralph can go in circles, ignore instructions, or take wrong directions_ - this is expected and part of the tuning process. When Ralph "tests you" by failing in specific ways, you add guardrails to the prompt or adjust backpressure mechanisms. The nondeterminism is manageable through observation and iteration.

### Enhanced Loop Example

Wraps core loop with mode selection (plan/build), max-iterations support, and git push after each iteration.

_This enhancement uses two saved prompt files:_

- `PROMPT_plan.md` - Planning mode (gap analysis, generates/updates plan)
- `PROMPT_build.md` - Building mode (implements from plan)

```bash
#!/bin/bash
# Usage: ./loop.sh [plan] [max_iterations]
# Examples:
#   ./loop.sh              # Build mode, unlimited iterations
#   ./loop.sh 20           # Build mode, max 20 iterations
#   ./loop.sh plan         # Plan mode, unlimited iterations
#   ./loop.sh plan 5       # Plan mode, max 5 iterations

# Parse arguments
if [ "$1" = "plan" ]; then
    # Plan mode
    MODE="plan"
    PROMPT_FILE="PROMPT_plan.md"
    MAX_ITERATIONS=${2:-0}
elif [[ "$1" =~ ^[0-9]+$ ]]; then
    # Build mode with max iterations
    MODE="build"
    PROMPT_FILE="PROMPT_build.md"
    MAX_ITERATIONS=$1
else
    # Build mode, unlimited (no arguments or invalid input)
    MODE="build"
    PROMPT_FILE="PROMPT_build.md"
    MAX_ITERATIONS=0
fi

ITERATION=0
CURRENT_BRANCH=$(git branch --show-current)

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Mode:   $MODE"
echo "Prompt: $PROMPT_FILE"
echo "Branch: $CURRENT_BRANCH"
[ $MAX_ITERATIONS -gt 0 ] && echo "Max:    $MAX_ITERATIONS iterations"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Verify prompt file exists
if [ ! -f "$PROMPT_FILE" ]; then
    echo "Error: $PROMPT_FILE not found"
    exit 1
fi

while true; do
    if [ $MAX_ITERATIONS -gt 0 ] && [ $ITERATION -ge $MAX_ITERATIONS ]; then
        echo "Reached max iterations: $MAX_ITERATIONS"
        break
    fi

    # Run Ralph iteration with selected prompt
    # -p: Headless mode (non-interactive, reads from stdin)
    # --dangerously-skip-permissions: Auto-approve all tool calls (YOLO mode)
    # --output-format=stream-json: Structured output for logging/monitoring
    # --model opus: Primary agent uses Opus for complex reasoning (task selection, prioritization)
    #               Can use 'sonnet' in build mode for speed if plan is clear and tasks well-defined
    # --verbose: Detailed execution logging
    cat "$PROMPT_FILE" | claude -p \
        --dangerously-skip-permissions \
        --output-format=stream-json \
        --model opus \
        --verbose

    # Push changes after each iteration
    git push origin "$CURRENT_BRANCH" || {
        echo "Failed to push. Creating remote branch..."
        git push -u origin "$CURRENT_BRANCH"
    }

    ITERATION=$((ITERATION + 1))
    echo -e "\n\n======================== LOOP $ITERATION ========================\n"
done
```

_Mode selection:_

- No keyword → Uses `PROMPT_build.md` for building (implementation)
- `plan` keyword → Uses `PROMPT_plan.md` for planning (gap analysis, plan generation)

_Max-iterations:_

- Limits the _outer loop_ (number of tasks attempted; NOT tool calls within a single task)
- Each iteration = one fresh context window = one task from IMPLEMENTATION_PLAN.md = one commit
- `./loop.sh` runs unlimited (manual stop with Ctrl+C)
- `./loop.sh 20` runs max 20 iterations then stops

_Claude CLI flags:_

- `-p` (headless mode): Enables non-interactive operation, reads prompt from stdin
- `--dangerously-skip-permissions`: Bypasses all permission prompts for fully automated runs
- `--output-format=stream-json`: Outputs structured JSON for logging/monitoring/visualization
- `--model opus`: Primary agent uses Opus for task selection, prioritization, and coordination (can use `sonnet` for speed if tasks are clear)
- `--verbose`: Provides detailed execution logging

---

## Files

```
project-root/
├── loop.sh                         # Ralph loop script
├── PROMPT_build.md                 # Build mode instructions
├── PROMPT_plan.md                  # Plan mode instructions
├── AGENTS.md                       # Operational guide loaded each iteration
├── IMPLEMENTATION_PLAN.md          # Prioritized task list (generated/updated by Ralph)
├── specs/                          # Requirement specs (one per JTBD topic)
│   ├── [jtbd-topic-a].md
│   └── [jtbd-topic-b].md
├── src/                            # Application source code
└── src/lib/                        # Shared utilities & components
```

### `loop.sh`

The outer loop script that orchestrates Ralph iterations.

See [Loop Mechanics](#loop-mechanics) section for detailed implementation examples and configuration options.

_Setup:_ Make the script executable before first use:

```bash
chmod +x loop.sh
```

_Core function:_ Continuously feeds prompt file to claude, manages iteration limits, and pushes changes after each task completion.

### PROMPTS

The instruction set for each loop iteration. Swap between PLANNING and BUILDING versions as needed.

_Prompt Structure:_

| Section                | Purpose                                               |
| ---------------------- | ----------------------------------------------------- |
| _Phase 0_ (0a, 0b, 0c) | Orient: study specs, source location, current plan    |
| _Phase 1-4_            | Main instructions: task, validation, commit           |
| _999... numbering_     | Guardrails/invariants (higher number = more critical) |

_Key Language Patterns_ (Geoff's specific phrasing):

- "study" (not "read" or "look at")
- "don't assume not implemented" (critical - the Achilles' heel)
- "using parallel subagents" / "up to N subagents"
- "only 1 subagent for build/tests" (backpressure control)
- "Think extra hard" (now "Ultrathink)
- "capture the why"
- "keep it up to date"
- "if functionality is missing then it's your job to add it"
- "resolve them or document them"

#### `PROMPT_plan.md` Template

_Notes:_

- Update [project-specific goal] placeholder below.
- Current subagents names presume using Claude.

```
0a. Study `specs/*` with up to 250 parallel Sonnet subagents to learn the application specifications.
0b. Study @IMPLEMENTATION_PLAN.md (if present) to understand the plan so far.
0c. Study `src/lib/*` with up to 250 parallel Sonnet subagents to understand shared utilities & components.
0d. For reference, the application source code is in `src/*`.

1. Study @IMPLEMENTATION_PLAN.md (if present; it may be incorrect) and use up to 500 Sonnet subagents to study existing source code in `src/*` and compare it against `specs/*`. Use an Opus subagent to analyze findings, prioritize tasks, and create/update @IMPLEMENTATION_PLAN.md as a bullet point list sorted in priority of items yet to be implemented. Ultrathink. Consider searching for TODO, minimal implementations, placeholders, skipped/flaky tests, and inconsistent patterns. Study @IMPLEMENTATION_PLAN.md to determine starting point for research and keep it up to date with items considered complete/incomplete using subagents.

IMPORTANT: Plan only. Do NOT implement anything. Do NOT assume functionality is missing; confirm with code search first. Treat `src/lib` as the project's standard library for shared utilities and components. Prefer consolidated, idiomatic implementations there over ad-hoc copies.

ULTIMATE GOAL: We want to achieve [project-specific goal]. Consider missing elements and plan accordingly. If an element is missing, search first to confirm it doesn't exist, then if needed author the specification at specs/FILENAME.md. If you create a new element then document the plan to implement it in @IMPLEMENTATION_PLAN.md using a subagent.
```

#### `PROMPT_build.md` Template

_Note:_ Current subagents names presume using Claude.

```
0a. Study `specs/*` with up to 500 parallel Sonnet subagents to learn the application specifications.
0b. Study @IMPLEMENTATION_PLAN.md.
0c. For reference, the application source code is in `src/*`.

1. Your task is to implement functionality per the specifications using parallel subagents. Follow @IMPLEMENTATION_PLAN.md and choose the most important item to address. Before making changes, search the codebase (don't assume not implemented) using Sonnet subagents. You may use up to 500 parallel Sonnet subagents for searches/reads and only 1 Sonnet subagent for build/tests. Use Opus subagents when complex reasoning is needed (debugging, architectural decisions).
2. After implementing functionality or resolving problems, run the tests for that unit of code that was improved. If functionality is missing then it's your job to add it as per the application specifications. Ultrathink.
3. When you discover issues, immediately update @IMPLEMENTATION_PLAN.md with your findings using a subagent. When resolved, update and remove the item.
4. When the tests pass, update @IMPLEMENTATION_PLAN.md, then `git add -A` then `git commit` with a message describing the changes. After the commit, `git push`.

99999. Important: When authoring documentation, capture the why — tests and implementation importance.
999999. Important: Single sources of truth, no migrations/adapters. If tests unrelated to your work fail, resolve them as part of the increment.
9999999. As soon as there are no build or test errors create a git tag. If there are no git tags start at 0.0.0 and increment patch by 1 for example 0.0.1  if 0.0.0 does not exist.
99999999. You may add extra logging if required to debug issues.
999999999. Keep @IMPLEMENTATION_PLAN.md current with learnings using a subagent — future work depends on this to avoid duplicating efforts. Update especially after finishing your turn.
9999999999. When you learn something new about how to run the application, update @AGENTS.md using a subagent but keep it brief. For example if you run commands multiple times before learning the correct command then that file should be updated.
99999999999. For any bugs you notice, resolve them or document them in @IMPLEMENTATION_PLAN.md using a subagent even if it is unrelated to the current piece of work.
999999999999. Implement functionality completely. Placeholders and stubs waste efforts and time redoing the same work.
9999999999999. When @IMPLEMENTATION_PLAN.md becomes large periodically clean out the items that are completed from the file using a subagent.
99999999999999. If you find inconsistencies in the specs/* then use an Opus 4.5 subagent with 'ultrathink' requested to update the specs.
999999999999999. IMPORTANT: Keep @AGENTS.md operational only — status updates and progress notes belong in `IMPLEMENTATION_PLAN.md`. A bloated AGENTS.md pollutes every future loop's context.
```

### `AGENTS.md`

Single, canonical "heart of the loop" - a concise, operational "how to run/build" guide.

- NOT a changelog or progress diary
- Describes how to build/run the project
- Captures operational learnings that improve the loop
- Keep brief (~60 lines)

Status, progress, and planning belong in `IMPLEMENTATION_PLAN.md`, not here.

_Loopback / Immediate Self-Evaluation:_

AGENTS.md should contain the project-specific commands that enable loopback - the ability for Ralph to immediately evaluate his work within the same loop. This includes:

- Build commands
- Test commands (targeted and full suite)
- Typecheck/lint commands
- Any other validation tools

The BUILDING prompt says "run tests" generically; AGENTS.md specifies the actual commands. This is how backpressure gets wired in per-project.

#### Example

```
## Build & Run

Succinct rules for how to BUILD the project:

## Validation

Run these after implementing to get immediate feedback:

- Tests: `[test command]`
- Typecheck: `[typecheck command]`
- Lint: `[lint command]`

## Operational Notes

Succinct learnings about how to RUN the project:

...

### Codebase Patterns

...
```

### `IMPLEMENTATION_PLAN.md`

Prioritized bullet-point list of tasks derived from gap analysis (specs vs code) - generated by Ralph.

- _Created_ via PLANNING mode
- _Updated_ during BUILDING mode (mark complete, add discoveries, note bugs)
- _Can be regenerated_ – Geoff: "I have deleted the TODO list multiple times" → switch to PLANNING mode
- _Self-correcting_ – BUILDING mode can even create new specs if missing

The circularity is intentional: eventual consistency through iteration.

_No pre-specified template_ - let Ralph/LLM dictate and manage format that works best for it.

### `specs/*`

One markdown file per topic of concern. These are the source of truth for what should be built.

- Created during Requirements phase (human + LLM conversation)
- Consumed by both PLANNING and BUILDING modes
- Can be updated if inconsistencies discovered (rare, use subagent)

_No pre-specified template_ - let Ralph/LLM dictate and manage format that works best for it.

### `src/` and `src/lib/`

Application source code and shared utilities/components.

Referenced in `PROMPT.md` templates for orientation steps.

---

## Enhancements?

I'm (Clayton) still determining the value/viability of these possible enhancements, but the opportunities sound promising.

I'm still determining the value/viability of these, but the opportunities sound promising:

- [Claude's AskUserQuestionTool for Planning](#use-claudes-askuserquestiontool-for-planning) - use Claude's built-in interview tool to systematically clarify JTBD, edge cases, and acceptance criteria for specs.
- [Acceptance-Driven Backpressure](#acceptance-driven-backpressure) - Derive test requirements during planning from acceptance criteria. Prevents "cheating" - can't claim done without appropriate tests passing.
- [Non-Deterministic Backpressure](#non-deterministic-backpressure) - Using LLM-as-judge for tests against subjective tasks (tone, aesthetics, UX). Binary pass/fail reviews that iterate until pass.
- [Ralph-Friendly Work Branches](#ralph-friendly-work-branches) - Asking Ralph to "filter to feature X" at runtime is unreliable. Instead, create scoped plan per branch upfront.
- [JTBD → Story Map → SLC Release](#jtbd--story-map--slc-release) - Push the power of "Letting Ralph Ralph" to connect JTBD's audience and activities to Simple/Lovable/Complete releases.

---

### Use Claude's AskUserQuestionTool for Planning

During Phase 1 (Define Requirements), use Claude's built-in `AskUserQuestionTool` to systematically explore JTBD, topics of concern, edge cases, and acceptance criteria through structured interview before writing specs.

_When to use:_ Minimal/vague initial requirements, need to clarify constraints, or multiple valid approaches exist.

_Invoke:_ "Interview me using AskUserQuestion to understand [JTBD/topic/acceptance criteria/...]"

Claude will ask targeted questions to clarify requirements and ensure alignment before producing `specs/*.md` files.

_Flow:_

1. Start with known information →
2. _Claude interviews via AskUserQuestion_ →
3. Iterate until clear →
4. Claude writes specs with acceptance criteria →
5. Proceed to planning/building

No code or prompt changes needed - this simply enhances Phase 1 using existing Claude Code capabilities.

_Inspiration_ - [Thariq's X post](https://x.com/trq212/status/2005315275026260309):

---

### Acceptance-Driven Backpressure

Geoff's Ralph _implicitly_ connects specs → implementation → tests through emergent iteration. This enhancement would make that connection _explicit_ by deriving test requirements during planning, creating a direct line from "what success looks like" to "what verifies it."

This enhancement connects acceptance criteria (in specs) directly to test requirements (in implementation plan), improving backpressure quality by:

- _Preventing "no cheating"_ - Can't claim done without required tests derived from acceptance criteria
- _Enabling TDD workflow_ - Test requirements known before implementation starts
- _Improving convergence_ - Clear completion signal (required tests pass) vs ambiguous ("seems done?")
- _Maintaining determinism_ - Test requirements in plan (known state) not emergent (probabilistic)

#### Compatibility with Core Philosophy

| Principle             | Maintained? | How                                                         |
| --------------------- | ----------- | ----------------------------------------------------------- |
| Monolithic operation  | ✅ Yes      | One agent, one task, one loop at a time                     |
| Backpressure critical | ✅ Yes      | Tests are the mechanism, just derived explicitly now        |
| Context efficiency    | ✅ Yes      | Planning decides tests once vs building rediscovering       |
| Deterministic setup   | ✅ Yes      | Test requirements in plan (known state) not emergent        |
| Let Ralph Ralph       | ✅ Yes      | Ralph still prioritizes and chooses implementation approach |
| Plan is disposable    | ✅ Yes      | Wrong test requirements? Regenerate plan                    |
| "Capture the why"     | ✅ Yes      | Test intent documented in plan before implementation        |
| No cheating           | ✅ Yes      | Required tests prevent placeholder implementations          |

#### The Prescriptiveness Balance

The critical distinction:

_Acceptance criteria_ (in specs) = Behavioral outcomes, observable results, what success looks like

- ✅ "Extracts 5-10 dominant colors from any uploaded image"
- ✅ "Processes images <5MB in <100ms"
- ✅ "Handles edge cases: grayscale, single-color, transparent backgrounds"

_Test requirements_ (in implementation plan) = Verification points derived from acceptance criteria

- ✅ "Required tests: Extract 5-10 colors, Performance <100ms, Handle grayscale edge case"

_Implementation approach_ (up to Ralph) = Technical decisions about how to achieve it

- ❌ "Use K-means clustering with 3 iterations and LAB color space conversion"

The key: _Specify WHAT to verify (outcomes), not HOW to implement (approach)_

This maintains "Let Ralph Ralph" principle - Ralph decides implementation details while having clear success signals.

#### Architecture: Three-Phase Connection

```
Phase 1: Requirements Definition
    specs/*.md + Acceptance Criteria
    ↓
Phase 2: Planning (derives test requirements)
    IMPLEMENTATION_PLAN.md + Required Tests
    ↓
Phase 3: Building (implements with tests)
    Implementation + Tests → Backpressure
```

#### Phase 1: Requirements Definition

During the human + LLM conversation that produces specs:

- Discuss JTBD and break into topics of concern
- Use subagents to load external context as needed
- _Discuss and define acceptance criteria_ - what observable, verifiable outcomes indicate success
- Keep criteria behavioral (outcomes), not implementation (how to build it)
- LLM writes specs including acceptance criteria however makes most sense for the spec
- Acceptance criteria become the foundation for deriving test requirements in planning phase

#### Phase 2: Planning Mode Enhancement

Modify `PROMPT_plan.md` instruction 1 to include test derivation. Add after the first sentence:

```markdown
For each task in the plan, derive required tests from acceptance criteria in specs - what specific outcomes need verification (behavior, performance, edge cases). Tests verify WHAT works, not HOW it's implemented. Include as part of task definition.
```

#### Phase 3: Building Mode Enhancement

Modify `PROMPT_build.md` instructions:

_Instruction 1:_ Add after "choose the most important item to address":

```markdown
Tasks include required tests - implement tests as part of task scope.
```

_Instruction 2:_ Replace "run the tests for that unit of code" with:

```markdown
run all required tests specified in the task definition. All required tests must exist and pass before the task is considered complete.
```

_Prepend new guardrail_ (in the 9s sequence):

```markdown
999. Required tests derived from acceptance criteria must exist and pass before committing. Tests are part of implementation scope, not optional. Test-driven development approach: tests can be written first or alongside implementation.
```

---

### Non-Deterministic Backpressure

Some acceptance criteria resist programmatic validation:

- _Creative quality_ - Writing tone, narrative flow, engagement
- _Aesthetic judgments_ - Visual harmony, design balance, brand consistency
- _UX quality_ - Intuitive navigation, clear information hierarchy
- _Content appropriateness_ - Context-aware messaging, audience fit

These require human-like judgment but need backpressure to meet acceptance criteria during building loop.

_Solution:_ Add LLM-as-Judge tests as backpressure with binary pass/fail.

LLM reviews are non-deterministic (same artifact may receive different judgments across runs). This aligns with Ralph philosophy: "deterministically bad in an undeterministic world." The loop provides eventual consistency through iteration—reviews run until pass, accepting natural variance.

#### What Needs to Be Created (First Step)

Create two files in `src/lib/`:

```
src/lib/
  llm-review.ts          # Core fixture - single function, clean API
  llm-review.test.ts     # Reference examples showing the pattern (Ralph learns from these)
```

##### `llm-review.ts` - Binary pass/fail API Ralph discovers:

```typescript
interface ReviewResult {
  pass: boolean;
  feedback?: string; // Only present when pass=false
}

function createReview(config: {
  criteria: string; // What to evaluate (behavioral, observable)
  artifact: string; // Text content OR screenshot path
  intelligence?: "fast" | "smart"; // Optional, defaults to 'fast'
}): Promise<ReviewResult>;
```

_Multimodal support:_ Both intelligence levels would use multimodal model (text + vision). Artifact type detection is automatic:

- Text evaluation: `artifact: "Your content here"` → Routes as text input
- Vision evaluation: `artifact: "./tmp/screenshot.png"` → Routes as vision input (detects .png, .jpg, .jpeg extensions)

_Intelligence levels_ (quality of judgment, not capability type):

- `fast` (default): Quick, cost-effective models for straightforward evaluations
  - Example: Gemini 3.0 Flash (multimodal, fast, cheap)
- `smart`: Higher-quality models for nuanced aesthetic/creative judgment
  - Example: GPT 5.1 (multimodal, better judgment, higher cost)

The fixture implementation selects appropriate models. (Examples are current options, not requirements.)

##### `llm-review.test.ts` - Shows Ralph how to use it (text and vision examples):

```typescript
import { createReview } from "@/lib/llm-review";

// Example 1: Text evaluation
test("welcome message tone", async () => {
  const message = generateWelcomeMessage();
  const result = await createReview({
    criteria:
      "Message uses warm, conversational tone appropriate for design professionals while clearly conveying value proposition",
    artifact: message, // Text content
  });
  expect(result.pass).toBe(true);
});

// Example 2: Vision evaluation (screenshot path)
test("dashboard visual hierarchy", async () => {
  await page.screenshot({ path: "./tmp/dashboard.png" });
  const result = await createReview({
    criteria:
      "Layout demonstrates clear visual hierarchy with obvious primary action",
    artifact: "./tmp/dashboard.png", // Screenshot path
  });
  expect(result.pass).toBe(true);
});

// Example 3: Smart intelligence for complex judgment
test("brand visual consistency", async () => {
  await page.screenshot({ path: "./tmp/homepage.png" });
  const result = await createReview({
    criteria:
      "Visual design maintains professional brand identity suitable for financial services while avoiding corporate sterility",
    artifact: "./tmp/homepage.png",
    intelligence: "smart", // Complex aesthetic judgment
  });
  expect(result.pass).toBe(true);
});
```

_Ralph learns from these examples:_ Both text and screenshots work as artifacts. Choose based on what needs evaluation. The fixture handles the rest internally.

_Future extensibility:_ Current design uses single `artifact: string` for simplicity. Can expand to `artifact: string | string[]` if clear patterns emerge requiring multiple artifacts (before/after comparisons, consistency across items, multi-perspective evaluation). Composite screenshots or concatenated text could handle most multi-item needs.

#### Integration with Ralph Workflow

_Planning Phase_ - Update `PROMPT_plan.md`:

After:

```
...Study @IMPLEMENTATION_PLAN.md to determine starting point for research and keep it up to date with items considered complete/incomplete using subagents.
```

Insert this:

```
When deriving test requirements from acceptance criteria, identify whether verification requires programmatic validation (measurable, inspectable) or human-like judgment (perceptual quality, tone, aesthetics). Both types are equally valid backpressure mechanisms. For subjective criteria that resist programmatic validation, explore src/lib for non-deterministic evaluation patterns.
```

_Building Phase_ - Update `PROMPT_build.md`:

Prepend new guardrail (in the 9s sequence):

```markdown
9999. Create tests to verify implementation meets acceptance criteria and include both conventional tests (behavior, performance, correctness) and perceptual quality tests (for subjective criteria, see src/lib patterns).
```

_Discovery, not documentation:_ Ralph learns LLM review patterns from `llm-review.test.ts` examples during `src/lib` exploration (Phase 0c). No AGENTS.md updates needed - the code examples are the documentation.

#### Compatibility with Core Philosophy

| Principle             | Maintained? | How                                                                                                                                          |
| --------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Backpressure critical | ✅ Yes      | Extends backpressure to non-programmatic acceptance                                                                                          |
| Deterministic setup   | ⚠️ Partial  | Criteria in plan (deterministic), evaluation non-deterministic but converges through iteration. Intentional tradeoff for subjective quality. |
| Context efficiency    | ✅ Yes      | Fixture reused via `src/lib`, small test definitions                                                                                         |
| Let Ralph Ralph       | ✅ Yes      | Ralph discovers pattern, chooses when to use, writes criteria                                                                                |
| Plan is disposable    | ✅ Yes      | Review requirements part of plan, regenerate if wrong                                                                                        |
| Simplicity wins       | ✅ Yes      | Single function, binary result, no scoring complexity                                                                                        |
| Add signs for Ralph   | ✅ Yes      | Light prompt additions, learning from code exploration                                                                                       |

---

### Ralph-Friendly Work Branches

_The Critical Principle:_ Geoff's Ralph works from a single, disposable plan where Ralph picks "most important." To use branches with Ralph while maintaining this pattern, you must scope at plan creation, not at task selection.

_Why this matters:_

- ❌ _Wrong approach_: Create full plan, then ask Ralph to "filter" tasks at runtime → unreliable (70-80%), violates determinism
- ✅ _Right approach_: Create a scoped plan upfront for each work branch → deterministic, simple, maintains "plan is disposable"

_Solution:_ Add a `plan-work` mode to create a work-scoped IMPLEMENTATION_PLAN.md on the current branch. User creates work branch, then runs `plan-work` with a natural language description of the work focus. The LLM uses this description to scope the plan. Post planning, Ralph builds from this already-scoped plan with zero semantic filtering - just picks "most important" as always.

_Terminology:_ "Work" is intentionally broad - it can describe features, topics of concern, refactoring efforts, infrastructure changes, bug fixes, or any coherent body of related changes. The work description you pass to `plan-work` is natural language for the LLM - it can be prose, not constrained by git branch naming rules.

#### Design Principles

- ✅ _Each Ralph session operates monolithically_ on ONE body of work per branch
- ✅ _User creates branches manually_ - full control over naming conventions and strategy (e.g. worktrees)
- ✅ _Natural language work descriptions_ - pass prose to LLM, unconstrained by git naming rules
- ✅ _Scoping at plan creation_ (deterministic) not task selection (probabilistic)
- ✅ _Single plan per branch_ - one IMPLEMENTATION_PLAN.md per branch
- ✅ _Plan remains disposable_ - regenerate scoped plan when wrong/stale for a branch
- ✅ No dynamic branch switching within a loop session
- ✅ Maintains simplicity and determinism
- ✅ Optional - main branch workflow still works
- ✅ No semantic filtering at build time - Ralph just picks "most important"

#### Workflow

_1. Full Planning (on main branch)_

```bash
./loop.sh plan
# Generate full IMPLEMENTATION_PLAN.md for entire project
```

_2. Create Work Branch_

User performs:

```bash
git checkout -b ralph/user-auth-oauth
# Create branch with whatever naming convention you prefer
# Suggestion: ralph/* prefix for work branches
```

_3. Scoped Planning (on work branch)_

```bash
./loop.sh plan-work "user authentication system with OAuth and session management"
# Pass natural language description - LLM uses this to scope the plan
# Creates focused IMPLEMENTATION_PLAN.md with only tasks for this work
```

_4. Build from Plan (on work branch)_

```bash
./loop.sh
# Ralph builds from scoped plan (no filtering needed)
# Picks most important task from already-scoped plan
```

_5. PR Creation (when work complete)_

User performs:

```bash
gh pr create --base main --head ralph/user-auth-oauth --fill
```

#### Work-Scoped Loop Script

Extends the base enhanced loop script to add work branch support with scoped planning:

```bash
#!/bin/bash
set -euo pipefail

# Usage:
#   ./loop.sh [plan] [max_iterations]       # Plan/build on current branch
#   ./loop.sh plan-work "work description"  # Create scoped plan on current branch
# Examples:
#   ./loop.sh                               # Build mode, unlimited
#   ./loop.sh 20                            # Build mode, max 20
#   ./loop.sh plan 5                        # Full planning, max 5
#   ./loop.sh plan-work "user auth"         # Scoped planning

# Parse arguments
MODE="build"
PROMPT_FILE="PROMPT_build.md"

if [ "$1" = "plan" ]; then
    # Full planning mode
    MODE="plan"
    PROMPT_FILE="PROMPT_plan.md"
    MAX_ITERATIONS=${2:-0}
elif [ "$1" = "plan-work" ]; then
    # Scoped planning mode
    if [ -z "$2" ]; then
        echo "Error: plan-work requires a work description"
        echo "Usage: ./loop.sh plan-work \"description of the work\""
        exit 1
    fi
    MODE="plan-work"
    WORK_DESCRIPTION="$2"
    PROMPT_FILE="PROMPT_plan_work.md"
    MAX_ITERATIONS=${3:-5}  # Default 5 for work planning
elif [[ "$1" =~ ^[0-9]+$ ]]; then
    # Build mode with max iterations
    MAX_ITERATIONS=$1
else
    # Build mode, unlimited
    MAX_ITERATIONS=0
fi

ITERATION=0
CURRENT_BRANCH=$(git branch --show-current)

# Validate branch for plan-work mode
if [ "$MODE" = "plan-work" ]; then
    if [ "$CURRENT_BRANCH" = "main" ] || [ "$CURRENT_BRANCH" = "master" ]; then
        echo "Error: plan-work should be run on a work branch, not main/master"
        echo "Create a work branch first: git checkout -b ralph/your-work"
        exit 1
    fi

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Mode:    plan-work"
    echo "Branch:  $CURRENT_BRANCH"
    echo "Work:    $WORK_DESCRIPTION"
    echo "Prompt:  $PROMPT_FILE"
    echo "Plan:    Will create scoped IMPLEMENTATION_PLAN.md"
    [ "$MAX_ITERATIONS" -gt 0 ] && echo "Max:     $MAX_ITERATIONS iterations"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    # Warn about uncommitted changes to IMPLEMENTATION_PLAN.md
    if [ -f "IMPLEMENTATION_PLAN.md" ] && ! git diff --quiet IMPLEMENTATION_PLAN.md 2>/dev/null; then
        echo "Warning: IMPLEMENTATION_PLAN.md has uncommitted changes that will be overwritten"
        read -p "Continue? [y/N] " -n 1 -r
        echo
        [[ ! $REPLY =~ ^[Yy]$ ]] && exit 1
    fi

    # Export work description for PROMPT_plan_work.md
    export WORK_SCOPE="$WORK_DESCRIPTION"
else
    # Normal plan/build mode
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Mode:   $MODE"
    echo "Branch: $CURRENT_BRANCH"
    echo "Prompt: $PROMPT_FILE"
    echo "Plan:   IMPLEMENTATION_PLAN.md"
    [ "$MAX_ITERATIONS" -gt 0 ] && echo "Max:    $MAX_ITERATIONS iterations"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
fi

# Verify prompt file exists
if [ ! -f "$PROMPT_FILE" ]; then
    echo "Error: $PROMPT_FILE not found"
    exit 1
fi

# Main loop
while true; do
    if [ "$MAX_ITERATIONS" -gt 0 ] && [ "$ITERATION" -ge "$MAX_ITERATIONS" ]; then
        echo "Reached max iterations: $MAX_ITERATIONS"

        if [ "$MODE" = "plan-work" ]; then
            echo ""
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo "Scoped plan created: $WORK_DESCRIPTION"
            echo "To build, run:"
            echo "  ./loop.sh 20"
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        fi
        break
    fi

    # Run Ralph iteration with selected prompt
    # -p: Headless mode (non-interactive, reads from stdin)
    # --dangerously-skip-permissions: Auto-approve all tool calls (YOLO mode)
    # --output-format=stream-json: Structured output for logging/monitoring
    # --model opus: Primary agent uses Opus for complex reasoning (task selection, prioritization)
    #               Can use 'sonnet' for speed if plan is clear and tasks well-defined
    # --verbose: Detailed execution logging

    # For plan-work mode, substitute ${WORK_SCOPE} in prompt before piping
    if [ "$MODE" = "plan-work" ]; then
        envsubst < "$PROMPT_FILE" | claude -p \
            --dangerously-skip-permissions \
            --output-format=stream-json \
            --model opus \
            --verbose
    else
        cat "$PROMPT_FILE" | claude -p \
            --dangerously-skip-permissions \
            --output-format=stream-json \
            --model opus \
            --verbose
    fi

    # Push to current branch
    CURRENT_BRANCH=$(git branch --show-current)
    git push origin "$CURRENT_BRANCH" || {
        echo "Failed to push. Creating remote branch..."
        git push -u origin "$CURRENT_BRANCH"
    }

    ITERATION=$((ITERATION + 1))
    echo -e "\n\n======================== LOOP $ITERATION ========================\n"
done
```

#### `PROMPT_plan_work.md` Template

_Note:_ Identical to `PROMPT_plan.md` but with scoping instructions and `WORK_SCOPE` env var substituted (automatically by the loop script).

```
0a. Study `specs/*` with up to 250 parallel Sonnet subagents to learn the application specifications.
0b. Study @IMPLEMENTATION_PLAN.md (if present) to understand the plan so far.
0c. Study `src/lib/*` with up to 250 parallel Sonnet subagents to understand shared utilities & components.
0d. For reference, the application source code is in `src/*`.

1. You are creating a SCOPED implementation plan for work: "${WORK_SCOPE}". Study @IMPLEMENTATION_PLAN.md (if present; it may be incorrect) and use up to 500 Sonnet subagents to study existing source code in `src/*` and compare it against `specs/*`. Use an Opus subagent to analyze findings, prioritize tasks, and create/update @IMPLEMENTATION_PLAN.md as a bullet point list sorted in priority of items yet to be implemented. Ultrathink. Consider searching for TODO, minimal implementations, placeholders, skipped/flaky tests, and inconsistent patterns. Study @IMPLEMENTATION_PLAN.md to determine starting point for research and keep it up to date with items considered complete/incomplete using subagents.

IMPORTANT: This is SCOPED PLANNING for "${WORK_SCOPE}" only. Create a plan containing ONLY tasks directly related to this work scope. Be conservative - if uncertain whether a task belongs to this work, exclude it. The plan can be regenerated if too narrow. Plan only. Do NOT implement anything. Do NOT assume functionality is missing; confirm with code search first. Treat `src/lib` as the project's standard library for shared utilities and components. Prefer consolidated, idiomatic implementations there over ad-hoc copies.

ULTIMATE GOAL: We want to achieve the scoped work "${WORK_SCOPE}". Consider missing elements related to this work and plan accordingly. If an element is missing, search first to confirm it doesn't exist, then if needed author the specification at specs/FILENAME.md. If you create a new element then document the plan to implement it in @IMPLEMENTATION_PLAN.md using a subagent.
```

#### Compatibility with Core Philosophy

| Principle              | Maintained? | How                                                                      |
| ---------------------- | ----------- | ------------------------------------------------------------------------ |
| Monolithic operation   | ✅ Yes      | Ralph still operates as single process within branch                     |
| One task per loop      | ✅ Yes      | Unchanged                                                                |
| Fresh context          | ✅ Yes      | Unchanged                                                                |
| Deterministic          | ✅ Yes      | Scoping at plan creation (deterministic), not runtime (prob.)            |
| Simple                 | ✅ Yes      | Optional enhancement, main workflow still works                          |
| Plan-driven            | ✅ Yes      | One IMPLEMENTATION_PLAN.md per branch                                    |
| Single source of truth | ✅ Yes      | One plan per branch - scoped plan replaces full plan on branch           |
| Plan is disposable     | ✅ Yes      | Regenerate scoped plan anytime: `./loop.sh plan-work "work description"` |
| Markdown over JSON     | ✅ Yes      | Still markdown plans                                                     |
| Let Ralph Ralph        | ✅ Yes      | Ralph picks "most important" from already-scoped plan - no filter        |

---

### JTBD → Story Map → SLC Release

#### Topics of Concern → Activities

Geoff's [suggested workflow](https://ghuntley.com/content/images/size/w2400/2025/07/The-ralph-Process.png) already aligns planning with Jobs-to-be-Done — breaking JTBDs into topics of concern, which in turn become specs. I love this and I think there's an opportunity to lean further into the product benefits this approach affords by reframing _topics of concern_ as _activities_.

Activities are verbs in a journey ("upload photo", "extract colors") rather than capabilities ("color extraction system"). They're naturally scoped by user intent.

> Topics: "color extraction", "layout engine" → capability-oriented
> Activities: "upload photo", "see extracted colors", "arrange layout" → journey-oriented

#### Activities → User Journey

Activities — and their constituent steps — sequence naturally into a user flow, creating a _journey structure_ that makes gaps and dependencies visible. A _[User Story Map](https://www.nngroup.com/articles/user-story-mapping/)_ organizes activities as columns (the journey backbone) with capability depths as rows — the full space of what _could_ be built:

```
UPLOAD    →   EXTRACT    →   ARRANGE     →   SHARE

basic         auto           manual          export
bulk          palette        templates       collab
batch         AI themes      auto-layout     embed
```

#### User Journey → Release Slices

Horizontal slices through the map become candidate releases. Not every activity needs new capability in every release — some cells stay empty, and that's fine if the slice is still coherent:

```
                  UPLOAD    →   EXTRACT    →   ARRANGE     →   SHARE

Release 1:        basic         auto                           export
                  ───────────────────────────────────────────────────
Release 2:                      palette        manual
                  ───────────────────────────────────────────────────
Release 3:        batch         AI themes      templates       embed
```

#### Release Slices → SLC Releases

The story map gives you _structure_ for slicing. Jason Cohen's _[Simple, Lovable, Complete (SLC)](https://longform.asmartbear.com/slc/)_ gives you _criteria_ for what makes a slice good:

- _Simple_ — Narrow scope you can ship fast. Not every activity, not every depth.
- _Complete_ — Fully accomplishes a job within that scope. Not a broken preview.
- _Lovable_ — People actually want to use it. Delightful within its boundaries.

_Why SLC over MVP?_ MVPs optimize for learning at the customer's expense — "minimum" often means broken or frustrating. SLC flips this: learn in-market _while_ delivering real value. If it succeeds, you have optionality. If it fails, you still treated users well.

Each slice can become a release with a clear value and identity:

```
                  UPLOAD    →   EXTRACT    →   ARRANGE     →   SHARE

Palette Picker:   basic         auto                           export
                  ───────────────────────────────────────────────────
Mood Board:                     palette        manual
                  ───────────────────────────────────────────────────
Design Studio:    batch         AI themes      templates       embed
```

- _Palette Picker_ — Upload, extract, export. Instant value from day one.
- _Mood Board_ — Adds arrangement. Creative expression enters the journey.
- _Design Studio_ — Professional features: batch processing, AI themes, embeddable output.

---

#### Operationalizing with Ralph

The concepts above — activities, story maps, SLC releases — are the _thinking tools_. How do we translate them into Ralph's workflow?

_Default Ralph approach:_

1. _Define Requirements_: Human + LLM define JTBD topics of concern → `specs/*.md`
2. _Create Tasks Plan_: LLM analyzes all specs + current code → `IMPLEMENTATION_PLAN.md`
3. _Build_: Ralph builds against full scope

This works well for capability-focused work (features, refactors, infrastructure). But it doesn't naturally produce valuable (SLC) product releases - it produces "whatever the specs describe".

_Activities → SLC Release approach:_

To get SLC releases, we need to ground activities in audience context. Audience defines WHO has the JTBDs, which in turn informs WHAT activities matter and what "lovable" means.

```
Audience (who)
    └── has JTBDs (why)
            └── fulfilled by Activities (how)
```

##### Workflow

_I. Requirements Phase (2 steps):_

Still performed in LLM conversations with the human, similar to the default Ralph approach.

1. _Define audience and their JTBDs_ — WHO are we building for and what OUTCOMES do they want?

   - Human + LLM discuss and determine the audience(s) and their JTBDs (outcomes they want)
   - May contain multiple connected audiences (e.g. "designer" creates, "client" reviews)
   - Generates `AUDIENCE_JTBD.md`

2. _Define activities_ — WHAT do users do to accomplish their JTBDs?

   - Informed by `AUDIENCE_JTBD.md`
   - For each JTBD, identify activities necessary to accomplish it
   - For each activity, determine:
     - Capability depths (basic → enhanced) — levels of sophistication
     - Desired outcome(s) at each depth — what does success look like?
   - Generates `specs/*.md` (one per activity)

   The discrete steps within activities are implicit and LLM can infer them during planning.

_II. Planning Phase:_

Performed in Ralph loop with _updated_ planning prompt.

- LLM analyzes:
  - `AUDIENCE_JTBD.md` (who, desired outcomes)
  - `specs/*` (what could be built)
  - Current code state (what exists)
- LLM determines next SLC slice (which activities, at what capability depths) and plans tasks for that slice
- LLM generates `IMPLEMENTATION_PLAN.md`
- _Human verifies_ plan before building:
  - Does the scope represent a coherent SLC release?
  - Are the right activities included at the right depths?
  - If wrong → re-run planning loop to regenerate plan, optionally updating inputs or planning prompt
  - If right → proceed to building

_III. Building Phase:_

Performed in Ralph loop with standard building prompt.

##### Updated Planning Prompt

Variant of `PROMPT_plan.md` that adds audience context and SLC-oriented slice recommendation.

_Notes:_

- Unlike the default template, this does not have a `[project-specific goal]` placeholder — the goal is implicit: recommend the most valuable next release for the audience.
- Current subagents names presume using Claude.

```
0a. Study @AUDIENCE_JTBD.md to understand who we're building for and their Jobs to Be Done.
0b. Study `specs/*` with up to 250 parallel Sonnet subagents to learn JTBD activities.
0c. Study @IMPLEMENTATION_PLAN.md (if present) to understand the plan so far.
0d. Study `src/lib/*` with up to 250 parallel Sonnet subagents to understand shared utilities & components.
0e. For reference, the application source code is in `src/*`.

1. Sequence the activities in `specs/*` into a user journey map for the audience in @AUDIENCE_JTBD.md. Consider how activities flow into each other and what dependencies exist.

2. Determine the next SLC release. Use up to 500 Sonnet subagents to compare `src/*` against `specs/*`. Use an Opus subagent to analyze findings. Ultrathink. Given what's already implemented recommend which activities (at what capability depths) form the most valuable next release. Prefer thin horizontal slices - the narrowest scope that still delivers real value. A good slice is Simple (narrow, achievable), Lovable (people want to use it), and Complete (fully accomplishes a meaningful job, not a broken preview).

3. Use an Opus subagent (ultrathink) to analyze and synthesize the findings, prioritize tasks, and create/update @IMPLEMENTATION_PLAN.md as a bullet point list sorted in priority of items yet to be implemented for the recommended SLC release. Begin plan with a summary of the recommended SLC release (what's included and why), then list prioritized tasks for that scope. Consider TODOs, placeholders, minimal implementations, skipped tests - but scoped to the release. Note discoveries outside scope as future work.

IMPORTANT: Plan only. Do NOT implement anything. Do NOT assume functionality is missing; confirm with code search first. Treat `src/lib` as the project's standard library for shared utilities and components. Prefer consolidated, idiomatic implementations there over ad-hoc copies.

ULTIMATE GOAL: We want to achieve the most valuable next release for the audience in @AUDIENCE_JTBD.md. Consider missing elements and plan accordingly. If an element is missing, search first to confirm it doesn't exist, then if needed author the specification at specs/FILENAME.md. If you create a new element then document the plan to implement it in @IMPLEMENTATION_PLAN.md using a subagent.
```

##### Notes

_Why `AUDIENCE_JTBD.md` as a separate artifact:_

- Single source of truth — prevents drift across specs
- Enables holistic reasoning: "What does this audience need MOST?"
- JTBDs captured alongside audience (the "why" lives with the "who")
- Referenced twice: during spec creation AND SLC planning
- Keeps activity specs focused on WHAT, not repeating WHO

_Cardinalities:_

- One audience → many JTBDs ("Designer" has "capture space", "explore concepts", "present to client")
- One JTBD → many activities ("capture space" includes upload, measurements, room detection)
- One activity → can serve multiple JTBDs ("upload photo" serves both "capture" and "gather inspiration")
```

## File: `index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>The Ralph Playbook</title>
    <meta
      name="description"
      content="A comprehensive guide to running AI coding loops with Geoff Huntley's Ralph methodology."
    />

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
      rel="stylesheet"
    />

    <style>
      /* ==========================================================================
       CSS Custom Properties
       ========================================================================== */
      :root {
        /* Font Families */
        --font-heading: "Space Grotesk", sans-serif;
        --font-body: "Plus Jakarta Sans", sans-serif;
        --font-mono: "JetBrains Mono", monospace;

        /* Type Scale (Minor Third ~1.2) */
        --text-xs: 0.75rem; /* 12-13px */
        --text-sm: 0.875rem; /* 14-15px */
        --text-base: 1rem; /* 16-17px body */
        --text-lg: 1.125rem; /* 18-19px leads */
        --text-xl: 1.3rem; /* ~22px h4 */
        --text-2xl: 1.55rem; /* ~26px h3 */
        --text-3xl: 1.875rem; /* ~32px h2 */
        --text-4xl: 2.25rem; /* ~38px h1 */

        /* Line Heights - Calibrated Per Size */
        --leading-tight: 1.15; /* display headings */
        --leading-snug: 1.25; /* subheadings h3-h4 */
        --leading-normal: 1.55; /* body text */
        --leading-relaxed: 1.65; /* lead paragraphs */
        --leading-code: 1.5;

        /* Spacing */
        --space-xs: 0.25rem;
        --space-sm: 0.5rem;
        --space-md: 1rem;
        --space-lg: 1.5rem;
        --space-xl: 2rem;
        --space-2xl: 2.5rem;
        --space-3xl: 4rem;
        --space-4xl: 6rem;

        /* Colors - Near monochrome with muted green accent */
        --color-text: #333;
        --color-text-muted: #555;
        --color-text-faint: #888;
        --color-heading: #1a1a1a;
        --color-link: #2d5a27;
        --color-link-hover: #1e3d1a;
        --color-accent: #2d5a27;
        --color-accent-light: #e8f0e7;
        --color-bg: #ffffff;
        --color-bg-subtle: #fafaf9;
        --color-bg-code: #1e1e1e;
        --color-border: #e5e5e3;
        --color-border-strong: #d1d1cf;

        /* Callout Colors - Desaturated/Lighter */
        --color-note-bg: #f5f8fb;
        --color-note-border: #5588bb;
        --color-warning-bg: #fdfaf4;
        --color-warning-border: #b89a50;
        --color-danger-bg: #fdf7f7;
        --color-danger-border: #b85555;
        --color-tip-bg: #f6faf7;
        --color-tip-border: #5a9a6a;

        /* Content Width */
        --content-width: 720px;
        --content-width-wide: 900px;
        --toc-width: 220px;
      }

      /* ==========================================================================
       Base Styles
       ========================================================================== */
      *,
      *::before,
      *::after {
        box-sizing: border-box;
      }

      html {
        font-size: 15px;
        scroll-behavior: smooth;
      }

      @media (min-width: 640px) {
        html {
          font-size: 15px;
        }
      }

      @media (min-width: 1024px) {
        html {
          font-size: 15px;
        }
      }

      body {
        font-family: var(--font-body);
        font-size: var(--text-base);
        font-weight: 400;
        line-height: 1.65;
        font-optical-sizing: auto;
        color: var(--color-text);
        background: var(--color-bg);
        margin: 0;
        padding: 0;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        font-feature-settings: "kern" 1, "liga" 1;
        letter-spacing: 0;
        text-rendering: optimizeLegibility;
      }

      /* Hyphenation control */
      p,
      li {
        hyphens: auto;
        text-wrap: pretty;
      }

      h1,
      h2,
      h3,
      h4,
      h5,
      h6,
      code,
      pre {
        hyphens: none;
      }

      :target {
        scroll-margin-top: 2rem;
      }

      @media (prefers-reduced-motion: reduce) {
        html {
          scroll-behavior: auto;
        }
        * {
          transition-duration: 0ms !important;
        }
      }

      /* ==========================================================================
       Layout
       ========================================================================== */
      .page-wrapper {
        display: flex;
        justify-content: center;
        min-height: 100vh;
      }

      .content-wrapper {
        display: flex;
        max-width: 1200px;
        width: 100%;
        padding: 0 var(--space-lg);
      }

      .main-content {
        flex: 1;
        min-width: 0;
        max-width: var(--content-width);
        padding: var(--space-xl) 0;
      }

      @media (min-width: 1024px) {
        .main-content {
          padding: var(--space-4xl) var(--space-xl);
        }
      }

      /* Sidebar TOC */
      .toc-sidebar {
        display: none;
      }

      @media (min-width: 960px) {
        .toc-sidebar {
          display: block;
          width: var(--toc-width);
          flex-shrink: 0;
          padding-left: var(--space-2xl);
        }

        .toc-nav {
          position: sticky;
          top: var(--space-4xl);
          max-height: calc(100vh - var(--space-4xl));
          overflow-y: auto;
          padding-right: var(--space-md);
        }
      }

      .toc-title {
        font-size: var(--text-sm);
        font-weight: 500;
        letter-spacing: 0.01em;
        color: var(--color-text-faint);
        margin-bottom: var(--space-md);
      }

      .toc-list {
        list-style: none;
        padding: 0;
        margin: 0;
      }

      .toc-link {
        display: block;
        padding: var(--space-xs) 0;
        padding-left: var(--space-sm);
        font-size: var(--text-sm);
        color: var(--color-text-faint);
        text-decoration: none;
        border-left: 2px solid transparent;
        transition: all 150ms ease;
      }

      .toc-link:hover {
        color: var(--color-text-muted);
      }

      .toc-link.active {
        color: var(--color-text-muted);
        border-left-color: var(--color-border-strong);
        font-weight: 500;
      }

      .toc-link--nested {
        padding-left: var(--space-lg);
        font-size: var(--text-xs);
      }

      /* ==========================================================================
       Typography - Headings
       ========================================================================== */
      .article-header {
        margin-bottom: var(--space-3xl);
      }

      .article-title {
        font-family: var(--font-heading);
        font-size: var(--text-4xl);
        font-weight: 700;
        line-height: var(--leading-tight);
        letter-spacing: -0.025em;
        color: var(--color-heading);
        margin: 0 0 var(--space-lg);
        text-wrap: balance;
      }

      .article-subtitle {
        text-wrap: balance;
        font-size: var(--text-lg);
        font-weight: 400;
        line-height: var(--leading-relaxed);
        color: var(--color-text-muted);
        margin: 0;
      }

      .article-meta {
        margin-top: var(--space-lg);
        font-size: var(--text-sm);
        color: var(--color-text-faint);
      }

      h2 {
        font-family: var(--font-heading);
        font-size: var(--text-3xl);
        font-weight: 600;
        line-height: var(--leading-tight);
        letter-spacing: -0.02em;
        color: var(--color-heading);
        margin-top: 3.5rem;
        margin-bottom: 1.25rem;
        padding-top: var(--space-lg);
        border-top: 1px solid var(--color-border);
        text-wrap: balance;
      }

      h2:first-of-type {
        margin-top: 0;
        padding-top: 0;
        border-top: none;
      }

      h3 {
        font-family: var(--font-heading);
        font-size: var(--text-2xl);
        font-weight: 600;
        line-height: var(--leading-snug);
        letter-spacing: -0.015em;
        color: var(--color-heading);
        margin-top: var(--space-2xl);
        text-wrap: balance;
      }

      h4 {
        font-family: var(--font-heading);
        font-size: var(--text-xl);
        font-weight: 500;
        line-height: var(--leading-snug);
        letter-spacing: -0.01em;
        color: var(--color-heading);
        margin-top: var(--space-xl);
        text-wrap: balance;
      }

      h5 {
        font-family: var(--font-heading);
        font-size: var(--text-base);
        font-weight: 500;
        line-height: var(--leading-normal);
        color: var(--color-heading);
        margin-top: var(--space-lg);
        margin-bottom: var(--space-md);
        text-wrap: balance;
      }

      /* ==========================================================================
       Typography - Body
       ========================================================================== */
      p {
        margin: 0 0 1.25rem;
      }

      .lead {
        font-size: var(--text-lg);
        line-height: var(--leading-relaxed);
        color: var(--color-text-muted);
        margin-bottom: var(--space-xl);
        text-wrap: balance;
      }

      a {
        color: var(--color-link);
        text-decoration: underline;
        text-decoration-thickness: 1px;
        text-underline-offset: 2px;
        transition: color 150ms ease;
      }

      a:hover {
        color: var(--color-link-hover);
      }

      strong,
      b {
        font-weight: 600;
      }

      em {
        font-style: italic;
      }

      small {
        font-size: var(--text-sm);
      }

      /* ==========================================================================
       TL;DR Box
       ========================================================================== */
      .tldr {
        background: var(--color-accent-light);
        border-radius: 3px;
        border-left: 3px solid var(--color-accent);
        padding: var(--space-lg) var(--space-xl);
        margin-bottom: var(--space-3xl);
      }

      .tldr-title {
        font-size: var(--text-sm);
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: var(--color-accent);
        margin-bottom: var(--space-sm);
      }

      .tldr p:last-child {
        margin-bottom: 0;
      }

      /* ==========================================================================
       Code
       ========================================================================== */
      code {
        font-family: var(--font-mono);
        font-size: 0.85em;
        background: var(--color-bg-subtle);
        padding: 0.15em 0.4em;
        border-radius: 3px;
        color: var(--color-text);
      }

      pre {
        font-family: var(--font-mono);
        font-size: 0.875rem;
        line-height: var(--leading-code);
        background: var(--color-bg-code);
        color: #d4d4d4;
        padding: var(--space-lg);
        border-radius: 4px;
        overflow-x: auto;
        margin: var(--space-xl) 0;
      }

      pre code {
        background: none;
        padding: 0;
        color: inherit;
        font-size: 0.8125rem;
        border-radius: 0;
      }

      .code-block {
        position: relative;
        margin: var(--space-xl) 0;
      }

      .code-block-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #2d2d2d;
        padding: var(--space-sm) var(--space-md);
        border-radius: 4px 4px 0 0;
        font-size: var(--text-sm);
        color: #999;
      }

      .code-block-header + pre {
        margin-top: 0;
        border-radius: 0 0 4px 4px;
      }

      .copy-btn {
        background: transparent;
        border: 1px solid #555;
        color: #999;
        padding: var(--space-xs) var(--space-sm);
        border-radius: 4px;
        font-size: var(--text-xs);
        cursor: pointer;
        transition: all 150ms ease;
      }

      .copy-btn:hover {
        background: #555;
        color: #fff;
      }

      /* Syntax highlighting (minimal) */
      .token-comment {
        color: #6a9955;
      }
      .token-string {
        color: #ce9178;
      }
      .token-keyword {
        color: #569cd6;
      }
      .token-function {
        color: #dcdcaa;
      }
      .token-variable {
        color: #9cdcfe;
      }

      /* ==========================================================================
       Lists
       ========================================================================== */
      ul,
      ol {
        margin: 0 0 var(--space-lg);
        padding-left: var(--space-lg);
      }

      li {
        margin-bottom: var(--space-sm);
        line-height: var(--leading-normal);
      }

      li > ul,
      li > ol {
        margin: var(--space-sm) 0 0;
      }

      /* ==========================================================================
       Tables
       ========================================================================== */
      .table-wrapper {
        overflow-x: auto;
        margin: var(--space-xl) 0;
        border-radius: 4px;
        border: 1px solid var(--color-border);
      }

      table {
        width: 100%;
        border-collapse: collapse;
        font-size: var(--text-sm);
        font-feature-settings: "tnum" 1, "lnum" 1;
      }

      thead {
        border-bottom: 2px solid var(--color-border);
      }

      th {
        text-align: left;
        padding: var(--space-sm) var(--space-md);
        background: var(--color-bg-subtle);
        font-weight: 600;
        font-size: var(--text-xs);
        text-transform: uppercase;
        letter-spacing: 0.04em;
        color: var(--color-text-muted);
        text-wrap: pretty;
      }

      td {
        padding: var(--space-sm) var(--space-md);
        border-bottom: 1px solid var(--color-border);
        vertical-align: top;
        text-wrap: pretty;
      }

      tr:last-child td {
        border-bottom: none;
      }

      td:first-child {
        font-weight: 500;
      }

      td code {
        font-size: 0.85em;
      }

      /* ==========================================================================
       Blockquotes & Callouts
       ========================================================================== */
      blockquote {
        margin: var(--space-xl) 0;
        padding: 0 0 0 var(--space-lg);
        border-left: 2px solid var(--color-border-strong);
        color: var(--color-text-muted);
        font-style: italic;
      }

      blockquote p:last-child {
        margin-bottom: 0;
      }

      .callout {
        margin: var(--space-xl) 0;
        padding: var(--space-lg) var(--space-xl);
        border-radius: 2px;
        border-left: 2px solid;
      }

      .callout > *:last-child {
        margin-bottom: 0;
      }

      .callout-title {
        font-weight: 600;
        /* font-size: var(--text-sm); */
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: var(--space-sm);
      }

      .callout-note {
        background: var(--color-note-bg);
        border-color: var(--color-note-border);
      }
      .callout-note .callout-title {
        color: var(--color-note-border);
      }

      .callout-warning {
        background: var(--color-warning-bg);
        border-color: var(--color-warning-border);
      }
      .callout-warning .callout-title {
        color: var(--color-warning-border);
      }

      .callout-danger {
        background: var(--color-danger-bg);
        border-color: var(--color-danger-border);
      }
      .callout-danger .callout-title {
        color: var(--color-danger-border);
      }

      .callout-tip {
        background: var(--color-tip-bg);
        border-color: var(--color-tip-border);
      }
      .callout-tip .callout-title {
        color: var(--color-tip-border);
      }

      /* ==========================================================================
       Figures & Images
       ========================================================================== */
      figure {
        margin: var(--space-xl) 0;
      }

      figure img {
        max-width: 100%;
        height: auto;
        border-radius: 4px;
        border: 1px solid var(--color-border);
      }

      figcaption {
        margin-top: var(--space-sm);
        font-size: var(--text-sm);
        font-weight: 450;
        letter-spacing: 0.01em;
        color: var(--color-text-faint);
        text-align: left;
      }

      small,
      .text-sm {
        font-weight: 450;
        letter-spacing: 0.01em;
      }

      /* ==========================================================================
       Horizontal Rules
       ========================================================================== */
      hr {
        border: none;
        border-top: 1px solid var(--color-border);
        margin: var(--space-3xl) 0;
      }

      /* ==========================================================================
       Section Headers with Emoji Icons
       ========================================================================== */
      .section-icon {
        margin-right: var(--space-sm);
      }

      /* ==========================================================================
       Collapsible Sections (Details/Summary)
       ========================================================================== */
      details {
        margin: var(--space-lg) 0;
        border: 1px solid var(--color-border);
        border-radius: 3px;
        background: var(--color-bg);
      }

      summary {
        padding: var(--space-md) var(--space-lg);
        padding-right: calc(var(--space-lg) + 1.5rem);
        cursor: pointer;
        font-weight: 500;
        list-style: none;
        display: flex;
        position: relative;
        user-select: none;
      }

      summary::-webkit-details-marker {
        display: none;
      }

      summary::after {
        content: "+";
        font-size: 1.25rem;
        color: var(--color-text-muted);
        font-weight: 400;
        position: absolute;
        right: var(--space-lg);
        top: var(--space-md);
      }

      details[open] summary::after {
        content: "−";
        color: #fff;
      }

      details[open] summary {
        border-bottom: 1px solid var(--color-border);
        background: var(--color-heading);
        color: #fff;
      }

      details[open] summary .summary-desc {
        color: rgba(255, 255, 255, 0.7);
      }

      .details-content {
        padding: var(--space-lg);
      }

      .details-content > *:last-child {
        margin-bottom: 0;
      }

      /* Summary with title and description */
      summary {
        flex-wrap: wrap;
      }

      .summary-title {
        flex: 1 1 100%;
        display: block;
      }

      .summary-desc {
        flex: 1 1 100%;
        display: block;
        font-size: var(--text-sm);
        font-weight: 400;
        color: var(--color-text-muted);
        margin-top: var(--space-xs);
      }

      /* Expanded panels (non-collapsible, same appearance as details) */
      .expanded-panel {
        margin: var(--space-lg) 0;
        border: 1px solid var(--color-border);
        border-radius: 3px;
        background: var(--color-bg);
      }

      .expanded-panel-header {
        padding: var(--space-md) var(--space-lg);
        font-weight: 500;
        border-bottom: 1px solid var(--color-border);
      }

      /* Colored check/x marks */
      .mark-pass {
        color: #2d7a3a;
      }

      .mark-fail {
        color: #c53030;
      }

      /* ==========================================================================
       Enhancement Section (Experimental)
       ========================================================================== */
      .enhancements-section {
        background: var(--color-bg-subtle);
        border-radius: 4px;
        padding: var(--space-xl);
        margin-top: var(--space-3xl);
      }

      .experimental-badge {
        display: inline-flex;
        align-items: center;
        gap: var(--space-xs);
        background: var(--color-warning-bg);
        color: var(--color-warning-border);
        padding: var(--space-xs) var(--space-sm);
        border-radius: 3px;
        font-size: var(--text-xs);
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: var(--space-md);
      }

      .enhancements-section h2 {
        margin-top: 0;
        padding-top: 0;
        border-top: none;
      }

      /* ==========================================================================
       Inline TOC (Mobile)
       ========================================================================== */
      .inline-toc {
        background: var(--color-bg-subtle);
        border-radius: 4px;
        padding: var(--space-lg);
        margin-bottom: var(--space-xl);
      }

      @media (min-width: 960px) {
        .inline-toc {
          display: none;
        }
      }

      .inline-toc-title {
        font-size: var(--text-sm);
        font-weight: 600;
        margin-bottom: var(--space-md);
        color: var(--color-text-muted);
      }

      .inline-toc ul {
        margin: 0;
        padding-left: var(--space-lg);
      }

      .inline-toc li {
        margin-bottom: var(--space-xs);
      }

      .inline-toc a {
        font-size: var(--text-sm);
        text-decoration: none;
      }

      .inline-toc a:hover {
        text-decoration: underline;
      }

      /* ==========================================================================
       Footer
       ========================================================================== */
      .article-footer {
        margin-top: var(--space-4xl);
        padding-top: var(--space-xl);
        border-top: 1px solid var(--color-border);
        font-size: var(--text-sm);
        color: var(--color-text-faint);
      }

      /* ==========================================================================
       Print Styles
       ========================================================================== */
      @media print {
        .toc-sidebar,
        .copy-btn,
        .inline-toc {
          display: none !important;
        }

        details {
          display: block !important;
        }

        details[open] summary::after {
          display: none;
        }

        .main-content {
          max-width: 100%;
        }
      }
    </style>
  </head>
  <body>
    <!--
  =====================================================================
  SYNC GUIDE FOR CLAUDE
  =====================================================================

  This HTML mirrors README.md content with styled presentation.

  SOURCE OF TRUTH: README.md

  SYNC RULES:
  - Content inside !-- HTML-ONLY: description --
    blocks is NOT in README → Preserve these blocks exactly when syncing - All
    other content should match README.md → Update to match README when syncing -
    Preserve HTML structure/styling (classes, wrappers) while syncing text
    HTML-ONLY CONTENT TYPES: - TL;DR summary box - Lead paragraphs (.lead class)
    under major section headings - Article header/subtitle/meta - Inline TOC
    (mobile) - Figure captions - Files table with "Modified By" column - Styled
    callout wrappers (content comes from README, styling is HTML-only) TO SYNC:
    "Update index.html to match README.md - preserve HTML-ONLY blocks"
    ===================================================================== -->
    <div class="page-wrapper">
      <div class="content-wrapper">
        <main class="main-content">
          <!-- HTML-ONLY: Article header with subtitle and source link -->
          <header id="intro" class="article-header">
            <h1 class="article-title">The Ralph Playbook</h1>
            <p class="article-subtitle">
              A comprehensive guide to running autonomous AI coding loops.
            </p>
            <div class="article-meta">
              <p style="margin-bottom: .5rem;">
                Thought up by
                <a href="https://x.com/GeoffreyHuntley">Geoff Huntley</a> &nbsp;&middot;&nbsp; Regurgitated by
                <a href="https://x.com/ClaytonFarr">Clayton Farr</a>
              </p>
              <p>
                Original source -
                <a href="https://ghuntley.com/ralph/">ghuntley.com/ralph</a>
              </p>
            </div>
          </header>
          <!-- /HTML-ONLY -->

          <!-- HTML-ONLY: TL;DR summary box -->
          <div class="tldr">
            <div class="tldr-title">TL;DR</div>
            <p>
              <strong>Ralph</strong> is an autonomous coding methodology that
              runs Claude in a continuous loop, using file-based state to
              maintain context across iterations. Each loop: read plan → pick
              task → implement → test → commit → clear context → repeat.
            </p>
            <p>
              <strong>Why it works:</strong> Fresh context each iteration keeps
              the AI in its "smart zone." File-based memory (specs, plan, agents
              file) persists learnings. Backpressure (utilities, tests, builds)
              forces self-correction.
            </p>
            <p>
              <strong>Key files:</strong> <code>PROMPT.md</code> (instructions)
              + <code>AGENTS.md</code> (operational guide) +
              <code>IMPLEMENTATION_PLAN.md</code> (task list) +
              <code>specs/*</code> (requirements)
            </p>
          </div>
          <!-- /HTML-ONLY -->

          <!-- HTML-ONLY: Inline TOC for mobile -->
          <nav class="inline-toc" aria-label="Table of contents">
            <div class="inline-toc-title">On This Page</div>
            <ul>
              <li><a href="#workflow">Workflow</a></li>
              <li><a href="#key-principles">Key Principles</a></li>
              <li><a href="#loop-mechanics">Loop Mechanics</a></li>
              <li><a href="#files">Files</a></li>
              <li><a href="#enhancements">Enhancements?</a></li>
            </ul>
          </nav>
          <!-- /HTML-ONLY -->

          <!-- Introduction -->
          <section>
            <p>
              December 2025 boiled
              <a href="https://ghuntley.com/ralph/">Ralph's</a> powerful yet
              dumb little face to the top of most AI-related timelines.
            </p>

            <p>
              I try to pay attention to the crazy-smart insights
              <a href="https://x.com/GeoffreyHuntley">@GeoffreyHuntley</a>
              shares, but I can't say Ralph really clicked for me this summer.
              Now, all of the recent hubbub has made it hard to ignore.
            </p>

            <p>
              <a href="https://x.com/mattpocockuk/status/2008200878633931247"
                >@mattpocockuk</a
              >
              and
              <a href="https://x.com/ryancarson/status/2008548371712135632"
                >@ryancarson</a
              >'s overviews helped a lot – right until Geoff came in and
              <a href="https://x.com/GeoffreyHuntley/status/2008731415312236984"
                >said 'nah'</a
              >.
            </p>

            <figure>
              <img
                src="https://raw.githubusercontent.com/ClaytonFarr/ralph-playbook/main/references/nah.png"
                alt="Geoff Huntley responding 'nah' to various Ralph interpretations"
                width="500"
              />
            </figure>

            <h3>So what is the optimal way to Ralph?</h3>

            <p>
              Many folks seem to be getting good results with various shapes –
              but I wanted to read the tea leaves as closely as possible from
              the person who not only captured this approach but also has had
              the most ass-time in the seat putting it through its paces.
            </p>

            <p>
              So I dug in to really <em>RTFM</em> on
              <a href="https://www.youtube.com/watch?v=O2bBWDoxO4s"
                >recent videos</a
              >
              and Geoff's
              <a href="https://ghuntley.com/ralph/">original post</a> to try and
              untangle for myself what works best.
            </p>

            <p>
              Below is the result – a (likely OCD-fueled) Ralph Playbook that
              organizes the miscellaneous details for putting this all into
              practice w/o hopefully neutering it in the process.
            </p>

            <div class="callout callout-note">
              <div class="callout-title">Note</div>
              <p>
                Digging into all of this has also brought to mind some possibly
                valuable <a href="#enhancements">additional enhancements</a> to
                the core approach that aim to stay aligned with the guidelines
                that make Ralph work so well.
              </p>
            </div>
          </section>

          <p>Hope this helps you out - <a href="https://x.com/ClaytonFarr">Clayton</a></p>

          <hr />

          <!-- Workflow -->
          <section id="workflow">
            <h2>Workflow</h2>

            <p>
              A picture is worth a thousand tweets and an hour-long video.
              Geoff's
              <a href="https://ghuntley.com/ralph/">overview here</a> (sign up
              to his newsletter to see full article) really helped clarify the
              workflow details for moving from 1) idea → 2) individual
              JTBD-aligned specs → 3) comprehensive implementation plan → 4)
              Ralph work loops.
            </p>

            <figure>
              <a
                href="https://raw.githubusercontent.com/ClaytonFarr/ralph-playbook/main/references/ralph-diagram.png"
                target="_blank"
                rel="noopener"
              >
                <img
                  src="https://raw.githubusercontent.com/ClaytonFarr/ralph-playbook/main/references/ralph-diagram.png"
                  alt="Ralph workflow diagram showing the three phases"
                />
              </a>
              <!-- HTML-ONLY: Figure caption -->
              <figcaption>
                The Ralph Process: From idea to implementation through specs,
                planning, and building loops
              </figcaption>
              <!-- /HTML-ONLY -->
            </figure>

            <h3>
              <span class="section-icon">🗘</span> Three Phases, Two Prompts, One
              Loop
            </h3>

            <h4>Phase 1: Define Requirements (LLM conversation)</h4>
            <ul>
              <li>Discuss project ideas → identify Jobs to Be Done (JTBD)</li>
              <li>Break individual JTBD into topic(s) of concern</li>
              <li>Use subagents to load info from URLs into context</li>
              <li>
                LLM understands JTBD topic of concern: subagent writes
                <code>specs/FILENAME.md</code> for each topic
              </li>
            </ul>

            <h4>Phase 2 / 3: Run Ralph Loop</h4>
            <p>
              Same loop mechanism, different prompts for different objectives:
            </p>

            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Mode</th>
                    <th>When to use</th>
                    <th>Prompt focus</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><em>PLANNING</em></td>
                    <td>No plan exists, or plan is stale/wrong</td>
                    <td>
                      Generate/update <code>IMPLEMENTATION_PLAN.md</code> only
                    </td>
                  </tr>
                  <tr>
                    <td><em>BUILDING</em></td>
                    <td>Plan exists</td>
                    <td>
                      Implement from plan, commit, update plan as side effect
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h5>Prompt differences per mode:</h5>
            <ul>
              <li>
                <strong>PLANNING</strong> prompt does gap analysis (specs vs
                code) and outputs a prioritized TODO list – no implementation,
                no commits.
              </li>
              <li>
                <strong>BUILDING</strong> prompt assumes plan exists, picks
                tasks from it, implements, runs tests (backpressure), commits.
              </li>
            </ul>

            <h5>Why use the loop for both modes?</h5>
            <ul>
              <li>
                <strong>BUILDING requires it:</strong> inherently iterative
                (many tasks × fresh context = isolation)
              </li>
              <li>
                <strong>PLANNING uses it for consistency:</strong> same
                execution model, though often completes in 1-2 iterations
              </li>
              <li>
                <strong>Flexibility:</strong> if plan needs refinement, loop
                allows multiple passes reading its own output
              </li>
              <li>
                <strong>Simplicity:</strong> one mechanism for everything; clean
                file I/O; easy stop/restart
              </li>
            </ul>

            <p>
              <strong>Context loaded each iteration:</strong>
              <code>PROMPT.md</code> + <code>AGENTS.md</code>
            </p>

            <div class="expanded-panel">
              <div class="expanded-panel-header">
                PLANNING mode loop lifecycle
              </div>
              <div class="details-content">
                <ol>
                  <li>
                    Subagents study <code>specs/*</code> and existing
                    <code>/src</code>
                  </li>
                  <li>Compare specs against code (gap analysis)</li>
                  <li>
                    Create/update <code>IMPLEMENTATION_PLAN.md</code> with
                    prioritized tasks
                  </li>
                  <li>No implementation</li>
                </ol>
              </div>
            </div>

            <div class="expanded-panel">
              <div class="expanded-panel-header">
                BUILDING mode loop lifecycle
              </div>
              <div class="details-content">
                <ol>
                  <li>
                    <strong>Orient</strong> – subagents study
                    <code>specs/*</code> (requirements)
                  </li>
                  <li>
                    <strong>Read plan</strong> – study
                    <code>IMPLEMENTATION_PLAN.md</code>
                  </li>
                  <li>
                    <strong>Select</strong> – pick the most important task
                  </li>
                  <li>
                    <strong>Investigate</strong> – subagents study relevant
                    <code>/src</code> ("don't assume not implemented")
                  </li>
                  <li>
                    <strong>Implement</strong> – N subagents for file operations
                  </li>
                  <li>
                    <strong>Validate</strong> – 1 subagent for build/tests
                    (backpressure)
                  </li>
                  <li>
                    <strong>Update <code>IMPLEMENTATION_PLAN.md</code></strong>
                    – mark task done, note discoveries/bugs
                  </li>
                  <li>
                    <strong>Update <code>AGENTS.md</code></strong> – if
                    operational learnings
                  </li>
                  <li><strong>Commit</strong></li>
                  <li>
                    <strong>Loop ends</strong> → context cleared → next
                    iteration starts fresh
                  </li>
                </ol>
              </div>
            </div>

            <h3>Concepts</h3>

            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Term</th>
                    <th>Definition</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><em>Job to be Done (JTBD)</em></td>
                    <td>High-level user need or outcome</td>
                  </tr>
                  <tr>
                    <td><em>Topic of Concern</em></td>
                    <td>A distinct aspect/component within a JTBD</td>
                  </tr>
                  <tr>
                    <td><em>Spec</em></td>
                    <td>
                      Requirements doc for one topic of concern
                      (<code>specs/FILENAME.md</code>)
                    </td>
                  </tr>
                  <tr>
                    <td><em>Task</em></td>
                    <td>Unit of work derived from comparing specs to code</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <p><strong>Relationships:</strong></p>
            <ul>
              <li>1 JTBD → multiple topics of concern</li>
              <li>1 topic of concern → 1 spec</li>
              <li>1 spec → multiple tasks (specs are larger than tasks)</li>
            </ul>

            <div class="expanded-panel">
              <div class="expanded-panel-header">Example: JTBD breakdown</div>
              <div class="details-content">
                <ul>
                  <li>
                    <strong>JTBD:</strong> "Help designers create mood boards"
                  </li>
                  <li>
                    <strong>Topics:</strong> image collection, color extraction,
                    layout, sharing
                  </li>
                  <li><strong>Each topic</strong> → one spec file</li>
                  <li>
                    <strong>Each spec</strong> → many tasks in implementation
                    plan
                  </li>
                </ul>
              </div>
            </div>

            <div class="callout callout-tip">
              <div class="callout-title">Topic Scope Test</div>
              <p>
                <strong>"One Sentence Without 'And'"</strong> – Can you describe
                the topic of concern in one sentence without conjoining
                unrelated capabilities?
              </p>
              <ul>
                <li>
                  <span class="mark-pass">✓</span> "The color extraction system
                  analyzes images to identify dominant colors"
                </li>
                <li>
                  <span class="mark-fail">✗</span> "The user system handles
                  authentication, profiles, and billing" → 3 topics
                </li>
              </ul>
              <p>
                If you need "and" to describe what it does, it's probably
                multiple topics.
              </p>
            </div>
          </section>

          <hr />

          <!-- Key Principles -->
          <section id="key-principles">
            <h2>Key Principles</h2>

            <!-- HTML-ONLY: Section lead paragraph -->
            <p class="lead">
              Four principles drive Ralph's effectiveness: constrained context,
              backpressure, autonomous action, and human oversight over the loop
              - not in it.
            </p>
            <!-- /HTML-ONLY -->

            <h3>
              <span class="section-icon">⏳</span> Context Is
              <em>Everything</em>
            </h3>

            <ul>
              <li>When 200K+ tokens advertised = ~176K truly usable</li>
              <li>And 40-60% context utilization for "smart zone"</li>
              <li>
                Tight tasks + 1 task per loop =
                <strong>100% smart zone context utilization</strong>
              </li>
            </ul>

            <p>This informs and drives everything else:</p>

            <ul>
              <li>
                <strong>Use the main agent/context as a scheduler</strong> –
                Don't allocate expensive work to main context; spawn subagents
                whenever possible instead
              </li>
              <li>
                <strong>Use subagents as memory extension</strong> – Each
                subagent gets ~156kb that's garbage collected. Fan out to avoid
                polluting main context
              </li>
              <li>
                <strong>Simplicity and brevity win</strong> – Applies to number
                of parts in system, loop config, and content. Verbose inputs
                degrade determinism
              </li>
              <li>
                <strong>Prefer Markdown over JSON</strong> – To define and track
                work, for better token efficiency
              </li>
            </ul>

            <h3>
              <span class="section-icon">🧭</span> Steering Ralph: Patterns +
              Backpressure
            </h3>

            <p>
              Creating the right signals &amp; gates to steer Ralph's successful
              output is <strong>critical</strong>. You can steer from two
              directions:
            </p>

            <h5>Steer upstream</h5>
            <ul>
              <li>
                Ensure deterministic setup:
                <ul>
                  <li>Allocate first ~5,000 tokens for specs</li>
                  <li>
                    Every loop's context is allocated with the same files so
                    model starts from known state (<code>PROMPT.md</code> +
                    <code>AGENTS.md</code>)
                  </li>
                </ul>
              </li>
              <li>Your existing code shapes what gets used and generated</li>
              <li>
                If Ralph is generating wrong patterns, add/update utilities and
                existing code patterns to steer it toward correct ones
              </li>
            </ul>

            <h5>Steer downstream</h5>
            <ul>
              <li>Create backpressure to reject invalid work</li>
              <li>
                Wire in whatever validates your code: tests, typechecks, lints,
                builds, etc.
              </li>
              <li>
                Prompt says "run tests" generically.
                <code>AGENTS.md</code> specifies actual commands to make
                backpressure project-specific
              </li>
              <li>
                Backpressure can extend beyond code validation: some acceptance
                criteria resist programmatic checks - creative quality,
                aesthetics, UX feel. LLM-as-judge tests can provide backpressure
                for subjective criteria with binary pass/fail. (<a
                  href="#non-deterministic-backpressure"
                  >More detailed thoughts below</a
                >
                on how to approach this with Ralph.)
              </li>
            </ul>

            <div class="callout callout-note">
              <div class="callout-title">
                Remind Ralph in Prompt.md to use backpressure:
              </div>
              <p>
                "Important: When authoring documentation, capture the why -
                tests and implementation importance."
              </p>
            </div>

            <h3><span class="section-icon">🙏</span> Let Ralph Ralph</h3>

            <p>
              Ralph's effectiveness comes from how much you trust it do the
              right thing (eventually) and engender its ability to do so.
            </p>

            <h5>Let Ralph Ralph</h5>
            <ul>
              <li>
                Lean into LLM's ability to self-identify, self-correct and
                self-improve.
              </li>
              <li>
                Applies to implementation plan, task definition and
                prioritization.
              </li>
              <li>Eventual consistency achieved through iteration.</li>
            </ul>

            <h5>
              Use Protection (<span style="color: var(--color-danger-border)"
                >Really</span
              >)
            </h5>
            <ul>
              <li>
                To operate autonomously, Ralph requires
                <code>--dangerously-skip-permissions</code> - asking for
                approval on every tool call would break the loop. This bypasses
                Claude's permission system entirely - so a sandbox becomes your
                only security boundary.
              </li>
              <li>
                <em>Philosophy</em> - "It's not if it gets popped, it's when.
                And what is the blast radius?"
              </li>
              <li>
                Running without a sandbox exposes credentials, browser cookies,
                SSH keys, and access tokens on your machine.
              </li>
              <li>
                Run in isolated environments with minimum viable access:
                <ul>
                  <li>Only the API keys and deploy keys needed for the task</li>
                  <li>No access to private data beyond requirements</li>
                  <li>Restrict network connectivity where possible</li>
                </ul>
              </li>
              <li>
                <em>Options</em> - Docker sandboxes (local), Fly
                Sprites/E2B/etc. (remote/production).
                <a href="references/sandbox-environments.md"
                  >Additional notes on options.</a
                >
              </li>
              <li>
                <em>Additional escape hatches</em> - Ctrl+C stops the loop;
                <code>git reset --hard</code> reverts uncommitted changes;
                regenerate plan if trajectory goes wrong.
              </li>
            </ul>

            <h3><span class="section-icon">🚦</span> Move Outside the Loop</h3>

            <p>
              To get the most out of Ralph, you need to get out of his way.
              Ralph should be doing <em>all</em> of the work, including decided
              which planned work to implement next and how to implement it. Your
              job is now to sit on the loop, not in it – to engineer the setup
              and environment that will allow Ralph to succeed.
            </p>

            <p>
              <strong>Observe and course correct</strong> – especially early on,
              sit and watch. What patterns emerge? Where does Ralph go wrong?
              What signs does he need? The prompts you start with won't be the
              prompts you end with – they evolve through observed failure
              patterns.
            </p>

            <p>
              <strong>Tune it like a guitar</strong> – instead of prescribing
              everything upfront, observe and adjust reactively. When Ralph
              fails a specific way, add a sign to help him next time.
            </p>

            <p>
              But signs aren't just prompt text. They're <em>anything</em> Ralph
              can discover:
            </p>
            <ul>
              <li>
                <strong>Prompt guardrails</strong> – explicit instructions like
                "don't assume not implemented"
              </li>
              <li>
                <strong><code>AGENTS.md</code></strong> – operational learnings
                about how to build/test
              </li>
              <li>
                <strong>Utilities in your codebase</strong> – when you add a
                pattern, Ralph discovers it and follows it
              </li>
              <li>Other discoverable, relevant inputs…</li>
            </ul>

            <div class="callout callout-tip">
              <div class="callout-title">The plan is designed to be disposable…</div>
              <ul>
                <li>If it's wrong, throw it out and start over</li>
                <li>
                  Regeneration cost is one Planning loop; cheap compared to
                  Ralph going in circles
                </li>
                <li>
                  Regenerate when:
                  <ul>
                    <li>
                      Ralph is going off track (implementing wrong things,
                      duplicating work)
                    </li>
                    <li>Plan feels stale or doesn't match current state</li>
                    <li>Too much clutter from completed items</li>
                    <li>You've made significant spec changes</li>
                    <li>You're confused about what's actually done</li>
                  </ul>
                </li>
              </ul>
            </div>
          </section>

          <hr />

          <!-- Loop Mechanics -->
          <section id="loop-mechanics">
            <h2>Loop Mechanics</h2>

            <!-- HTML-ONLY: Section lead paragraph -->
            <p class="lead">
              The mechanical details of how the outer bash loop and inner task
              execution work together.
            </p>
            <!-- /HTML-ONLY -->

            <h3><span class="section-icon">🔄</span> Outer Loop Control</h3>

            <p>Geoff's initial minimal form of `loop.sh` script:</p>

            <div class="code-block">
              <div class="code-block-header">
                <span>bash</span>
                <button class="copy-btn" onclick="copyCode(this)">Copy</button>
              </div>
              <pre><code>while :; do cat PROMPT.md | claude ; done</code></pre>
            </div>

            <p>
              <em>Note:</em> The same approach can be used with other CLIs; e.g.
              <code>amp</code>, <code>codex</code>, <code>opencode</code>, etc.
            </p>

            <h4>What controls task continuation?</h4>

            <p>The continuation mechanism is elegantly simple:</p>
            <ol>
              <li>
                <strong>Bash loop runs</strong> → feeds
                <code>PROMPT.md</code> to claude
              </li>
              <li>
                <strong>PROMPT.md instructs</strong> → "Study
                IMPLEMENTATION_PLAN.md and choose the most important thing"
              </li>
              <li>
                <strong>Agent completes one task</strong> → updates
                IMPLEMENTATION_PLAN.md on disk, commits, exits
              </li>
              <li>
                <strong>Bash loop restarts immediately</strong> → fresh context
                window
              </li>
              <li>
                <strong>Agent reads updated plan</strong> → picks next most
                important thing
              </li>
            </ol>

            <div class="callout callout-note">
              <div class="callout-title">Key insight</div>
              <p>
                The IMPLEMENTATION_PLAN.md file persists on disk between
                iterations and acts as shared state between otherwise isolated
                loop executions. Each iteration deterministically loads the same
                files (<code>PROMPT.md</code> + <code>AGENTS.md</code> +
                <code>specs/*</code>) and reads the current state from disk.
              </p>
              <p>
                No sophisticated orchestration needed – just a dumb bash loop
                that keeps restarting the agent, and the agent figures out what
                to do next by reading the plan file each time.
              </p>
            </div>

            <h3>Inner Loop Control (Task Execution)</h3>

            <p>
              A single task execution has no hard technical limit. Control
              relies on:
            </p>
            <ul>
              <li>
                <strong>Scope discipline</strong> – PROMPT.md instructs "one
                task" and "commit when tests pass"
              </li>
              <li>
                <strong>Backpressure</strong> – tests/build failures force the
                agent to fix issues before committing
              </li>
              <li>
                <strong>Natural completion</strong> – agent exits after
                successful commit
              </li>
            </ul>

            <p>
              <strong
                >Ralph can go in circles, ignore instructions, or take wrong
                directions</strong
              >
              – this is expected and part of the tuning process. When Ralph
              "tests you" by failing in specific ways, you add guardrails to the
              prompt or adjust backpressure mechanisms. The nondeterminism is
              manageable through observation and iteration.
            </p>

            <h3>Enhanced Loop Code Example</h3>

            <p>
              Wraps core loop with mode selection (plan/build), max-iterations
              support, and git push after each iteration.
            </p>

            <p><em>This enhancement uses two saved prompt files:</em></p>
            <ul>
              <li>
                <code>PROMPT_plan.md</code> – Planning mode (gap analysis,
                generates/updates plan)
              </li>
              <li>
                <code>PROMPT_build.md</code> – Building mode (implements from
                plan)
              </li>
            </ul>

            <details>
              <summary>Enhanced `loop.sh` script</summary>
              <div class="details-content">
                <div class="code-block">
                  <div class="code-block-header">
                    <span>loop.sh</span>
                    <button class="copy-btn" onclick="copyCode(this)">
                      Copy
                    </button>
                  </div>
                  <pre><code><span class="token-comment">#!/bin/bash</span>
<span class="token-comment"># Usage: ./loop.sh [plan] [max_iterations]</span>
<span class="token-comment"># Examples:</span>
<span class="token-comment">#   ./loop.sh              # Build mode, unlimited iterations</span>
<span class="token-comment">#   ./loop.sh 20           # Build mode, max 20 iterations</span>
<span class="token-comment">#   ./loop.sh plan         # Plan mode, unlimited iterations</span>
<span class="token-comment">#   ./loop.sh plan 5       # Plan mode, max 5 iterations</span>

<span class="token-comment"># Parse arguments</span>
<span class="token-keyword">if</span> [ <span class="token-string">"$1"</span> = <span class="token-string">"plan"</span> ]; <span class="token-keyword">then</span>
    <span class="token-comment"># Plan mode</span>
    MODE=<span class="token-string">"plan"</span>
    PROMPT_FILE=<span class="token-string">"PROMPT_plan.md"</span>
    MAX_ITERATIONS=<span class="token-variable">${2:-0}</span>
<span class="token-keyword">elif</span> [[ <span class="token-string">"$1"</span> =~ ^[0-9]+$ ]]; <span class="token-keyword">then</span>
    <span class="token-comment"># Build mode with max iterations</span>
    MODE=<span class="token-string">"build"</span>
    PROMPT_FILE=<span class="token-string">"PROMPT_build.md"</span>
    MAX_ITERATIONS=$1
<span class="token-keyword">else</span>
    <span class="token-comment"># Build mode, unlimited</span>
    MODE=<span class="token-string">"build"</span>
    PROMPT_FILE=<span class="token-string">"PROMPT_build.md"</span>
    MAX_ITERATIONS=0
<span class="token-keyword">fi</span>

ITERATION=0
CURRENT_BRANCH=$(<span class="token-function">git branch --show-current</span>)

<span class="token-function">echo</span> <span class="token-string">"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"</span>
<span class="token-function">echo</span> <span class="token-string">"Mode:   $MODE"</span>
<span class="token-function">echo</span> <span class="token-string">"Prompt: $PROMPT_FILE"</span>
<span class="token-function">echo</span> <span class="token-string">"Branch: $CURRENT_BRANCH"</span>
[ $MAX_ITERATIONS -gt 0 ] && <span class="token-function">echo</span> <span class="token-string">"Max:    $MAX_ITERATIONS iterations"</span>
<span class="token-function">echo</span> <span class="token-string">"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"</span>

<span class="token-comment"># Verify prompt file exists</span>
<span class="token-keyword">if</span> [ ! -f <span class="token-string">"$PROMPT_FILE"</span> ]; <span class="token-keyword">then</span>
    <span class="token-function">echo</span> <span class="token-string">"Error: $PROMPT_FILE not found"</span>
    exit 1
<span class="token-keyword">fi</span>

<span class="token-keyword">while</span> true; <span class="token-keyword">do</span>
    <span class="token-keyword">if</span> [ $MAX_ITERATIONS -gt 0 ] && [ $ITERATION -ge $MAX_ITERATIONS ]; <span class="token-keyword">then</span>
        <span class="token-function">echo</span> <span class="token-string">"Reached max iterations: $MAX_ITERATIONS"</span>
        <span class="token-keyword">break</span>
    <span class="token-keyword">fi</span>

    <span class="token-comment"># Run Ralph iteration with selected prompt</span>
    <span class="token-comment"># -p: Headless mode (non-interactive, reads from stdin)</span>
    <span class="token-comment"># --dangerously-skip-permissions: Auto-approve all tool calls (YOLO mode)</span>
    <span class="token-comment"># --output-format=stream-json: Structured output for logging/monitoring</span>
    <span class="token-comment"># --model opus: Primary agent uses Opus for complex reasoning (task selection, prioritization)</span>
    <span class="token-comment">#               Can use 'sonnet' in build mode for speed if plan is clear and tasks well-defined</span>
    <span class="token-comment"># --verbose: Detailed execution logging</span>
    <span class="token-function">cat</span> <span class="token-string">"$PROMPT_FILE"</span> | claude -p \
        --dangerously-skip-permissions \
        --output-format=stream-json \
        --model opus \
        --verbose

    <span class="token-comment"># Push changes after each iteration</span>
    <span class="token-function">git push</span> origin <span class="token-string">"$CURRENT_BRANCH"</span> || {
        <span class="token-function">echo</span> <span class="token-string">"Failed to push. Creating remote branch..."</span>
        <span class="token-function">git push</span> -u origin <span class="token-string">"$CURRENT_BRANCH"</span>
    }

    ITERATION=$((ITERATION + 1))
    <span class="token-function">echo</span> -e <span class="token-string">"\n\n======================== LOOP $ITERATION ========================\n"</span>
<span class="token-keyword">done</span></code></pre>
                </div>
              </div>
            </details>

            <h4>Mode Selection</h4>
            <ul>
              <li>
                No keyword → Uses <code>PROMPT_build.md</code> for building
                (implementation)
              </li>
              <li>
                <code>plan</code> keyword → Uses <code>PROMPT_plan.md</code> for
                planning (gap analysis, plan generation)
              </li>
            </ul>

            <h4>Max-Iterations</h4>
            <ul>
              <li>
                Limits the <em>outer loop</em> (number of tasks attempted; NOT
                tool calls within a single task)
              </li>
              <li>
                Each iteration = one fresh context window = one task from
                IMPLEMENTATION_PLAN.md = one commit
              </li>
              <li>
                <code>./loop.sh</code> runs unlimited (manual stop with Ctrl+C)
              </li>
              <li>
                <code>./loop.sh 20</code> runs max 20 iterations then stops
              </li>
            </ul>

            <h4>Claude CLI Flags Explained</h4>
            <ul>
              <li>
                <code>-p</code> (headless mode): Enables non-interactive
                operation, reads prompt from stdin
              </li>
              <li>
                <code>--dangerously-skip-permissions</code>: Bypasses all
                permission prompts for fully automated runs
              </li>
              <li>
                <code>--output-format=stream-json</code>: Outputs structured
                JSON for logging/monitoring/visualization
              </li>
              <li>
                <code>--model opus</code>: Primary agent uses Opus for task
                selection, prioritization, and coordination (can use
                <code>sonnet</code> for speed if tasks are clear)
              </li>
              <li>
                <code>--verbose</code>: Provides detailed execution logging
              </li>
            </ul>
          </section>

          <hr />

          <!-- Files -->
          <section id="files">
            <h2><span class="section-icon">📁</span> Files</h2>

            <!-- HTML-ONLY: Section lead paragraph -->
            <p class="lead">
              The file structure and templates that make Ralph work.
            </p>
            <!-- /HTML-ONLY -->

            <div class="code-block">
              <div class="code-block-header">
                <span>structure</span>
                <button class="copy-btn" onclick="copyCode(this)">Copy</button>
              </div>
              <pre><code>project-root/
├── loop.sh                         <span class="token-comment"># Ralph loop script</span>
├── PROMPT_build.md                 <span class="token-comment"># Build mode instructions</span>
├── PROMPT_plan.md                  <span class="token-comment"># Plan mode instructions</span>
├── AGENTS.md                       <span class="token-comment"># Operational guide loaded each iteration</span>
├── IMPLEMENTATION_PLAN.md          <span class="token-comment"># Prioritized task list (generated/updated by Ralph)</span>
├── specs/                          <span class="token-comment"># Requirement specs (one per JTBD topic)</span>
│   ├── [jtbd-topic-a].md
│   └── [jtbd-topic-b].md
├── src/                            <span class="token-comment"># Application source code</span>
└── src/lib/                        <span class="token-comment"># Shared utilities & components</span></code></pre>
            </div>

            <!-- HTML-ONLY: Files table with Modified By column -->
            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>File</th>
                    <th>Purpose</th>
                    <th>Modified By</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>loop.sh</code></td>
                    <td>Outer loop orchestration</td>
                    <td>You (setup)</td>
                  </tr>
                  <tr>
                    <td><code>PROMPT_*.md</code></td>
                    <td>Instructions per mode</td>
                    <td>You (tuning)</td>
                  </tr>
                  <tr>
                    <td><code>AGENTS.md</code></td>
                    <td>Operational guide</td>
                    <td>Ralph + You</td>
                  </tr>
                  <tr>
                    <td><code>IMPLEMENTATION_PLAN.md</code></td>
                    <td>Prioritized task list</td>
                    <td>Ralph</td>
                  </tr>
                  <tr>
                    <td><code>specs/*</code></td>
                    <td>Requirements per topic</td>
                    <td>You + Ralph</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <!-- /HTML-ONLY -->

            <h3><code>loop.sh</code></h3>
            <p>The outer loop script that orchestrates Ralph iterations.</p>
            <p>
              See <a href="#loop-mechanics">Loop Mechanics</a> section for
              detailed implementation examples and configuration options.
            </p>
            <p><em>Setup:</em> Make the script executable before first use:</p>
            <div class="code-block">
              <div class="code-block-header">
                <span>bash</span>
                <button class="copy-btn" onclick="copyCode(this)">Copy</button>
              </div>
              <pre><code>chmod +x loop.sh</code></pre>
            </div>
            <p>
              <em>Core function:</em> Continuously feeds prompt file to claude,
              manages iteration limits, and pushes changes after each task
              completion.
            </p>

            <h3>PROMPTS</h3>

            <p style="text-wrap: balance">
              The instruction set for each loop iteration. Swap between PLANNING
              and BUILDING versions as needed.
            </p>

            <h4>Prompt Structure</h4>

            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Section</th>
                    <th>Purpose</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Phase 0 (0a, 0b, 0c)</td>
                    <td>Orient: study specs, source location, current plan</td>
                  </tr>
                  <tr>
                    <td>Phase 1-4</td>
                    <td>Main instructions: task, validation, commit</td>
                  </tr>
                  <tr>
                    <td>999... numbering</td>
                    <td>
                      Guardrails/invariants (higher number = more critical)
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h4>Key Language Patterns (Geoff's specific phrasing)</h4>
            <ul>
              <li>"study" (not "read" or "look at")</li>
              <li>
                "don't assume not implemented" (critical – the Achilles' heel)
              </li>
              <li>"using parallel subagents" / "up to N subagents"</li>
              <li>"only 1 subagent for build/tests" (backpressure control)</li>
              <li>"Think extra hard" (now "Ultrathink")</li>
              <li>"capture the why"</li>
              <li>"keep it up to date"</li>
              <li>
                "if functionality is missing then it's your job to add it"
              </li>
              <li>"resolve them or document them"</li>
            </ul>

            <h4><code>PROMPT_*.md</code> Templates</h4>

            <p><em>Notes:</em></p>
            <ul>
              <li>Update [project-specific goal] placeholder below.</li>
              <li>Current subagents names presume using Claude.</li>
            </ul>

            <details>
              <summary>PROMPT_plan.md Template</summary>
              <div class="details-content">
                <div class="code-block">
                  <div class="code-block-header">
                    <span>PROMPT_plan.md</span>
                    <button class="copy-btn" onclick="copyCode(this)">
                      Copy
                    </button>
                  </div>
                  <pre><code>0a. Study `specs/*` with up to 250 parallel Sonnet subagents to learn the application specifications.
0b. Study @IMPLEMENTATION_PLAN.md (if present) to understand the plan so far.
0c. Study `src/lib/*` with up to 250 parallel Sonnet subagents to understand shared utilities & components.
0d. For reference, the application source code is in `src/*`.

1. Study @IMPLEMENTATION_PLAN.md (if present; it may be incorrect) and use up to 500 Sonnet subagents to study existing source code in `src/*` and compare it against `specs/*`. Use an Opus subagent to analyze findings, prioritize tasks, and create/update @IMPLEMENTATION_PLAN.md as a bullet point list sorted in priority of items yet to be implemented. Ultrathink. Consider searching for TODO, minimal implementations, placeholders, skipped/flaky tests, and inconsistent patterns. Study @IMPLEMENTATION_PLAN.md to determine starting point for research and keep it up to date with items considered complete/incomplete using subagents.

IMPORTANT: Plan only. Do NOT implement anything. Do NOT assume functionality is missing; confirm with code search first. Treat `src/lib` as the project's standard library for shared utilities and components. Prefer consolidated, idiomatic implementations there over ad-hoc copies.

ULTIMATE GOAL: We want to achieve [project-specific goal]. Consider missing elements and plan accordingly. If an element is missing, search first to confirm it doesn't exist, then if needed author the specification at specs/FILENAME.md. If you create a new element then document the plan to implement it in @IMPLEMENTATION_PLAN.md using a subagent.</code></pre>
                </div>
              </div>
            </details>

            <details>
              <summary>PROMPT_build.md Template</summary>
              <div class="details-content">
                <div class="code-block">
                  <div class="code-block-header">
                    <span>PROMPT_build.md</span>
                    <button class="copy-btn" onclick="copyCode(this)">
                      Copy
                    </button>
                  </div>
                  <pre><code>0a. Study `specs/*` with up to 500 parallel Sonnet subagents to learn the application specifications.
0b. Study @IMPLEMENTATION_PLAN.md.
0c. For reference, the application source code is in `src/*`.

1. Your task is to implement functionality per the specifications using parallel subagents. Follow @IMPLEMENTATION_PLAN.md and choose the most important item to address. Before making changes, search the codebase (don't assume not implemented) using Sonnet subagents. You may use up to 500 parallel Sonnet subagents for searches/reads and only 1 Sonnet subagent for build/tests. Use Opus subagents when complex reasoning is needed (debugging, architectural decisions).
2. After implementing functionality or resolving problems, run the tests for that unit of code that was improved. If functionality is missing then it's your job to add it as per the application specifications. Ultrathink.
3. When you discover issues, immediately update @IMPLEMENTATION_PLAN.md with your findings using a subagent. When resolved, update and remove the item.
4. When the tests pass, update @IMPLEMENTATION_PLAN.md, then `git add -A` then `git commit` with a message describing the changes. After the commit, `git push`.

99999. Important: When authoring documentation, capture the why – tests and implementation importance.
999999. Important: Single sources of truth, no migrations/adapters. If tests unrelated to your work fail, resolve them as part of the increment.
9999999. As soon as there are no build or test errors create a git tag. If there are no git tags start at 0.0.0 and increment patch by 1 for example 0.0.1  if 0.0.0 does not exist.
99999999. You may add extra logging if required to debug issues.
999999999. Keep @IMPLEMENTATION_PLAN.md current with learnings using a subagent – future work depends on this to avoid duplicating efforts. Update especially after finishing your turn.
9999999999. When you learn something new about how to run the application, update @AGENTS.md using a subagent but keep it brief. For example if you run commands multiple times before learning the correct command then that file should be updated.
99999999999. For any bugs you notice, resolve them or document them in @IMPLEMENTATION_PLAN.md using a subagent even if it is unrelated to the current piece of work.
999999999999. Implement functionality completely. Placeholders and stubs waste efforts and time redoing the same work.
9999999999999. When @IMPLEMENTATION_PLAN.md becomes large periodically clean out the items that are completed from the file using a subagent.
99999999999999. If you find inconsistencies in the specs/* then use an Opus 4.5 subagent with 'ultrathink' requested to update the specs.
999999999999999. IMPORTANT: Keep @AGENTS.md operational only – status updates and progress notes belong in `IMPLEMENTATION_PLAN.md`. A bloated AGENTS.md pollutes every future loop's context.</code></pre>
                </div>
              </div>
            </details>

            <h3><code>AGENTS.md</code></h3>

            <p>
              Single, canonical "heart of the loop" – a concise, operational
              "how to run/build" guide.
            </p>

            <ul>
              <li><strong>NOT</strong> a changelog or progress diary</li>
              <li>Describes how to build/run the project</li>
              <li>Captures operational learnings that improve the loop</li>
              <li>Keep brief (~60 lines)</li>
            </ul>

            <p>
              Status, progress, and planning belong in
              <code>IMPLEMENTATION_PLAN.md</code>, not here.
            </p>

            <h5>Loopback / Immediate Self-Evaluation</h5>
            <p>
              AGENTS.md should contain the project-specific commands that enable
              loopback – the ability for Ralph to immediately evaluate his work
              within the same loop. This includes:
            </p>
            <ul>
              <li>Build commands</li>
              <li>Test commands (targeted and full suite)</li>
              <li>Typecheck/lint commands</li>
              <li>Any other validation tools</li>
            </ul>
            <p>
              The BUILDING prompt says "run tests" generically; AGENTS.md
              specifies the actual commands. This is how backpressure gets wired
              in per-project.
            </p>

            <details>
              <summary>AGENTS.md Example Structure</summary>
              <div class="details-content">
                <div class="code-block">
                  <div class="code-block-header">
                    <span>AGENTS.md</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>## Build & Run

Succinct rules for how to BUILD the project:

## Validation

Run these after implementing to get immediate feedback:

- Tests: `[test command]`
- Typecheck: `[typecheck command]`
- Lint: `[lint command]`

## Operational Notes

Succinct learnings about how to RUN the project:

...

### Codebase Patterns

...</code></pre>
                </div>
              </div>
            </details>

            <h3><code>IMPLEMENTATION_PLAN.md</code></h3>

            <p>
              Prioritized bullet-point list of tasks derived from gap analysis
              (specs vs code) – generated by Ralph.
            </p>

            <ul>
              <li><strong>Created</strong> via PLANNING mode</li>
              <li>
                <strong>Updated</strong> during BUILDING mode (mark complete,
                add discoveries, note bugs)
              </li>
              <li>
                <strong>Can be regenerated</strong> – Geoff: "I have deleted the
                TODO list multiple times" → switch to PLANNING mode
              </li>
              <li>
                <strong>Self-correcting</strong> – BUILDING mode can even create
                new specs if missing
              </li>
            </ul>

            <p>
              The circularity is intentional: eventual consistency through
              iteration.
            </p>

            <p>
              <em>No pre-specified template</em> – let Ralph/LLM dictate and
              manage format that works best for it.
            </p>

            <h3><code>specs/*</code></h3>

            <p>
              One markdown file per topic of concern. These are the source of
              truth for what should be built.
            </p>

            <ul>
              <li>
                Created during Requirements phase (human + LLM conversation)
              </li>
              <li>Consumed by both PLANNING and BUILDING modes</li>
              <li>
                Can be updated if inconsistencies discovered (rare, use
                subagent)
              </li>
            </ul>

            <p>
              <em>No pre-specified template</em> – let Ralph/LLM dictate and
              manage format that works best for it.
            </p>

            <h3><code>src/</code> and <code>src/lib/</code></h3>
            <p>Application source code and shared utilities/components.</p>
            <p>
              Referenced in <code>PROMPT.md</code> templates for orientation
              steps.
            </p>
          </section>

          <hr />

          <!-- Enhancements -->
          <section id="enhancements" class="enhancements-section">
            <h2>Enhancements?</h2>

            <!-- HTML-ONLY: Section lead paragraph -->
            <p class="lead">
              Clayton: I'm still determining the value/viability of these, but
              the opportunities sound promising:
            </p>
            <!-- /HTML-ONLY -->

            <details>
              <summary>
                <span class="summary-title"
                  >Use Claude's AskUserQuestionTool for Planning</span
                >
                <span class="summary-desc"
                  >Use Claude's built-in interview tool to systematically
                  clarify JTBD, edge cases, and acceptance criteria for
                  specs.</span
                >
              </summary>
              <div class="details-content">
                <p>
                  During Phase 1 (Define Requirements), use Claude's built-in
                  <code>AskUserQuestionTool</code> to systematically explore
                  JTBD, topics of concern, edge cases, and acceptance criteria
                  through structured interview before writing specs.
                </p>

                <p>
                  <strong>When to use:</strong> Minimal/vague initial
                  requirements, need to clarify constraints, or multiple valid
                  approaches exist.
                </p>

                <p>
                  <strong>Invoke:</strong> "Interview me using AskUserQuestion
                  to understand [JTBD/topic/acceptance criteria/...]"
                </p>

                <p>
                  Claude will ask targeted questions to clarify requirements and
                  ensure alignment before producing
                  <code>specs/*.md</code> files.
                </p>

                <p><strong>Flow:</strong></p>
                <ol>
                  <li>Start with known information →</li>
                  <li>Claude interviews via AskUserQuestion →</li>
                  <li>Iterate until clear →</li>
                  <li>Claude writes specs with acceptance criteria →</li>
                  <li>Proceed to planning/building</li>
                </ol>

                <p>
                  No code or prompt changes needed – this simply enhances Phase
                  1 using existing Claude Code capabilities.
                </p>

                <p>
                  <em>Inspiration</em> -
                  <a href="https://x.com/trq212/status/2005315275026260309"
                    >Thariq's X post</a
                  >
                </p>
              </div>
            </details>

            <details>
              <summary>
                <span class="summary-title"
                  >Acceptance-Driven Backpressure</span
                >
                <span class="summary-desc"
                  >Derive test requirements during planning from acceptance
                  criteria. Prevents "cheating" - can't claim done without
                  appropriate tests passing.</span
                >
              </summary>
              <div class="details-content">
                <p>
                  Geoff's Ralph <em>implicitly</em> connects specs →
                  implementation → tests through emergent iteration. This
                  enhancement would make that connection <em>explicit</em> by
                  deriving test requirements during planning, creating a direct
                  line from "what success looks like" to "what verifies it."
                </p>

                <p>
                  This enhancement connects acceptance criteria (in specs)
                  directly to test requirements (in implementation plan),
                  improving backpressure quality by:
                </p>
                <ul>
                  <li>
                    <strong>Preventing "no cheating"</strong> – Can't claim done
                    without required tests derived from acceptance criteria
                  </li>
                  <li>
                    <strong>Enabling TDD workflow</strong> – Test requirements
                    known before implementation starts
                  </li>
                  <li>
                    <strong>Improving convergence</strong> – Clear completion
                    signal (required tests pass) vs ambiguous ("seems done?")
                  </li>
                  <li>
                    <strong>Maintaining determinism</strong> – Test requirements
                    in plan (known state) not emergent (probabilistic)
                  </li>
                </ul>

                <h5>Compatibility with Core Philosophy</h5>
                <div class="table-wrapper">
                  <table>
                    <thead>
                      <tr>
                        <th>Principle</th>
                        <th>Maintained?</th>
                        <th>How</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Monolithic operation</td>
                        <td>✅ Yes</td>
                        <td>One agent, one task, one loop at a time</td>
                      </tr>
                      <tr>
                        <td>Backpressure critical</td>
                        <td>✅ Yes</td>
                        <td>
                          Tests are the mechanism, just derived explicitly now
                        </td>
                      </tr>
                      <tr>
                        <td>Context efficiency</td>
                        <td>✅ Yes</td>
                        <td>
                          Planning decides tests once vs building rediscovering
                        </td>
                      </tr>
                      <tr>
                        <td>Deterministic setup</td>
                        <td>✅ Yes</td>
                        <td>
                          Test requirements in plan (known state) not emergent
                        </td>
                      </tr>
                      <tr>
                        <td>Let Ralph Ralph</td>
                        <td>✅ Yes</td>
                        <td>
                          Ralph still prioritizes and chooses implementation
                          approach
                        </td>
                      </tr>
                      <tr>
                        <td>Plan is disposable</td>
                        <td>✅ Yes</td>
                        <td>Wrong test requirements? Regenerate plan</td>
                      </tr>
                      <tr>
                        <td>"Capture the why"</td>
                        <td>✅ Yes</td>
                        <td>
                          Test intent documented in plan before implementation
                        </td>
                      </tr>
                      <tr>
                        <td>No cheating</td>
                        <td>✅ Yes</td>
                        <td>
                          Required tests prevent placeholder implementations
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <h5>The Prescriptiveness Balance</h5>

                <p><em>The critical distinction:</em></p>
                <p>
                  Acceptance criteria (in specs) = Behavioral outcomes,
                  observable results
                </p>
                <ul>
                  <li>
                    ✓ "Extracts 5-10 dominant colors from any uploaded image"
                  </li>
                  <li>✓ "Processes images &lt;5MB in &lt;100ms"</li>
                  <li>
                    ✓ "Handles edge cases: grayscale, single-color, transparent
                    backgrounds"
                  </li>
                </ul>

                <p>
                  Test requirements (in plan) = Verification points derived from
                  acceptance criteria
                </p>
                <ul>
                  <li>
                    ✓ "Required tests: Extract 5-10 colors, Performance
                    &lt;100ms"
                  </li>
                </ul>

                <p>
                  Implementation approach (up to Ralph) = Technical decisions
                </p>
                <ul>
                  <li>✗ "Use K-means clustering with 3 iterations"</li>
                </ul>

                <p>
                  <em>
                    <strong>The key:</strong> Specify WHAT to verify (outcomes),
                    not HOW to implement (approach).</em
                  >
                </p>

                <p>
                  This maintains "Let Ralph Ralph" principle - Ralph decides
                  implementation details while having clear success signals.
                </p>

                <h5>Architecture: Three-Phase Connection</h5>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>diagram</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>Phase 1: Requirements Definition
    specs/*.md + Acceptance Criteria
    ↓
Phase 2: Planning (derives test requirements)
    IMPLEMENTATION_PLAN.md + Required Tests
    ↓
Phase 3: Building (implements with tests)
    Implementation + Tests → Backpressure</code></pre>
                </div>

                <h5>Phase 1: Requirements Definition</h5>
                <p>During the human + LLM conversation that produces specs:</p>
                <ul>
                  <li>Discuss JTBD and break into topics of concern</li>
                  <li>Use subagents to load external context as needed</li>
                  <li>
                    <em>Discuss and define acceptance criteria</em> – what
                    observable, verifiable outcomes indicate success
                  </li>
                  <li>
                    Keep criteria behavioral (outcomes), not implementation (how
                    to build it)
                  </li>
                  <li>
                    LLM writes specs including acceptance criteria however makes
                    most sense for the spec
                  </li>
                  <li>
                    Acceptance criteria become the foundation for deriving test
                    requirements in planning phase
                  </li>
                </ul>

                <h5>Phase 2: Planning Mode Enhancement</h5>
                <p>
                  Modify <code>PROMPT_plan.md</code> instruction 1 to include
                  test derivation. Add after the first sentence:
                </p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>instruction</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>For each task in the plan, derive required tests from acceptance criteria in specs - what specific outcomes need verification (behavior, performance, edge cases). Tests verify WHAT works, not HOW it's implemented. Include as part of task definition.</code></pre>
                </div>

                <h5>Phase 3: Building Mode Enhancement</h5>
                <p>Modify <code>PROMPT_build.md</code> instructions:</p>
                <p>
                  <em>Instruction 1:</em> Add after "choose the most important
                  item to address":
                </p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>instruction</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>Tasks include required tests - implement tests as part of task scope.</code></pre>
                </div>
                <p>
                  <em>Instruction 2:</em> Replace "run the tests for that unit
                  of code" with:
                </p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>instruction</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>run all required tests specified in the task definition. All required tests must exist and pass before the task is considered complete.</code></pre>
                </div>
                <p><em>Prepend new guardrail</em> (in the 9s sequence):</p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>instruction</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>999. Required tests derived from acceptance criteria must exist and pass before committing. Tests are part of implementation scope, not optional. Test-driven development approach: tests can be written first or alongside implementation.</code></pre>
                </div>
              </div>
            </details>

            <details>
              <summary>
                <span class="summary-title"
                  >Non-Deterministic Backpressure</span
                >
                <span class="summary-desc"
                  >Using LLM-as-judge for tests against subjective tasks (tone,
                  aesthetics, UX). Binary pass/fail reviews that iterate until
                  pass.</span
                >
              </summary>
              <div class="details-content">
                <p>Some acceptance criteria resist programmatic validation:</p>
                <ul>
                  <li>
                    <strong>Creative quality</strong> – Writing tone, narrative
                    flow, engagement
                  </li>
                  <li>
                    <strong>Aesthetic judgments</strong> – Visual harmony,
                    design balance, brand consistency
                  </li>
                  <li>
                    <strong>UX quality</strong> – Intuitive navigation, clear
                    information hierarchy
                  </li>
                  <li>
                    <strong>Content appropriateness</strong> – Context-aware
                    messaging, audience fit
                  </li>
                </ul>

                <p>
                  <strong>Solution:</strong> Add LLM-as-Judge tests as
                  backpressure with binary pass/fail.
                </p>

                <p>
                  LLM reviews are non-deterministic (same artifact may receive
                  different judgments across runs). This aligns with Ralph
                  philosophy: "deterministically bad in an undeterministic
                  world." The loop provides eventual consistency through
                  iteration–reviews run until pass, accepting natural variance.
                </p>

                <h5>What Needs to Be Created (First Step)</h5>

                <p>Create two files in <code>src/lib/</code>:</p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>structure</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>src/lib/
  llm-review.ts          # Core fixture - single function, clean API
  llm-review.test.ts     # Reference examples showing the pattern (Ralph learns from these)</code></pre>
                </div>

                <h5>
                  <code>llm-review.ts</code> - Binary pass/fail API Ralph
                  discovers:
                </h5>

                <div class="code-block">
                  <div class="code-block-header">
                    <span>llm-review.ts</span>
                  </div>
                  <pre><code>interface ReviewResult {
  pass: boolean;
  feedback?: string; // Only present when pass=false
}

function createReview(config: {
  criteria: string;    // What to evaluate
  artifact: string;    // Text content OR screenshot path
  intelligence?: "fast" | "smart";
}): Promise&lt;ReviewResult&gt;;</code></pre>
                </div>

                <p>
                  <strong>Multimodal support:</strong> Both intelligence levels
                  use multimodal models (text + vision). Artifact type detection
                  is automatic:
                </p>
                <ul>
                  <li>
                    Text evaluation:
                    <code>artifact: "Your content here"</code> → Routes as text
                    input
                  </li>
                  <li>
                    Vision evaluation:
                    <code>artifact: "./tmp/screenshot.png"</code> → Routes as
                    vision input (detects .png, .jpg, .jpeg extensions)
                  </li>
                </ul>

                <p>
                  <strong>Intelligence levels</strong> (quality of judgment, not
                  capability type):
                </p>
                <ul>
                  <li>
                    <code>fast</code> (default): Quick, cost-effective models
                    for straightforward evaluations (e.g., Gemini 3.0 Flash)
                  </li>
                  <li>
                    <code>smart</code>: Higher-quality models for nuanced
                    aesthetic/creative judgment (e.g., GPT 5.1)
                  </li>
                </ul>
                <p>
                  The fixture implementation selects appropriate models.
                  (Examples are current options, not requirements.)
                </p>

                <h5>
                  <code>llm-review.test.ts</code> - Shows Ralph how to use it
                  (text and vision examples):
                </h5>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>llm-review.test.ts examples</span>
                  </div>
                  <pre><code>import { createReview } from "@/lib/llm-review";

// Example 1: Text evaluation
test("welcome message tone", async () =&gt; {
  const message = generateWelcomeMessage();
  const result = await createReview({
    criteria: "Message uses warm, conversational tone appropriate for design professionals while clearly conveying value proposition",
    artifact: message, // Text content
  });
  expect(result.pass).toBe(true);
});

// Example 2: Vision evaluation (screenshot path)
test("dashboard visual hierarchy", async () =&gt; {
  await page.screenshot({ path: "./tmp/dashboard.png" });
  const result = await createReview({
    criteria: "Layout demonstrates clear visual hierarchy with obvious primary action",
    artifact: "./tmp/dashboard.png", // Screenshot path
  });
  expect(result.pass).toBe(true);
});

// Example 3: Smart intelligence for complex judgment
test("brand visual consistency", async () =&gt; {
  await page.screenshot({ path: "./tmp/homepage.png" });
  const result = await createReview({
    criteria: "Visual design maintains professional brand identity suitable for financial services while avoiding corporate sterility",
    artifact: "./tmp/homepage.png",
    intelligence: "smart", // Complex aesthetic judgment
  });
  expect(result.pass).toBe(true);
});</code></pre>
                </div>

                <p>
                  <em>Ralph learns from these examples:</em> Both text and
                  screenshots work as artifacts. Choose based on what needs
                  evaluation. The fixture handles the rest internally.
                </p>

                <p>
                  <em>Future extensibility:</em> Current design uses single
                  <code>artifact: string</code> for simplicity. Can expand to
                  <code>artifact: string | string[]</code> if clear patterns
                  emerge requiring multiple artifacts (before/after comparisons,
                  consistency across items, multi-perspective evaluation).
                  Composite screenshots or concatenated text could handle most
                  multi-item needs.
                </p>

                <h5>Integration with Ralph Workflow</h5>
                <p>
                  <em>Planning Phase</em> - Update <code>PROMPT_plan.md</code>:
                </p>
                <p>
                  After "...Study @IMPLEMENTATION_PLAN.md to determine starting
                  point for research and keep it up to date with items
                  considered complete/incomplete using subagents." insert:
                </p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>instruction</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>When deriving test requirements from acceptance criteria, identify whether verification requires programmatic validation (measurable, inspectable) or human-like judgment (perceptual quality, tone, aesthetics). Both types are equally valid backpressure mechanisms. For subjective criteria that resist programmatic validation, explore src/lib for non-deterministic evaluation patterns.</code></pre>
                </div>
                <p>
                  <em>Building Phase</em> - Update <code>PROMPT_build.md</code>:
                </p>
                <p>Prepend new guardrail (in the 9s sequence):</p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>instruction</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>9999. Create tests to verify implementation meets acceptance criteria and include both conventional tests (behavior, performance, correctness) and perceptual quality tests (for subjective criteria, see src/lib patterns).</code></pre>
                </div>
                <p>
                  <em>Discovery, not documentation:</em> Ralph learns LLM review
                  patterns from <code>llm-review.test.ts</code> examples during
                  <code>src/lib</code> exploration (Phase 0c). No AGENTS.md
                  updates needed - the code examples are the documentation.
                </p>

                <h5>Compatibility with Core Philosophy</h5>
                <div class="table-wrapper">
                  <table>
                    <thead>
                      <tr>
                        <th>Principle</th>
                        <th>Maintained?</th>
                        <th>How</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Backpressure critical</td>
                        <td>✅ Yes</td>
                        <td>
                          Extends backpressure to non-programmatic acceptance
                        </td>
                      </tr>
                      <tr>
                        <td>Deterministic setup</td>
                        <td>⚠️ Partial</td>
                        <td>
                          Criteria in plan (deterministic), evaluation
                          non-deterministic but converges through iteration
                        </td>
                      </tr>
                      <tr>
                        <td>Context efficiency</td>
                        <td>✅ Yes</td>
                        <td>
                          Fixture reused via src/lib, small test definitions
                        </td>
                      </tr>
                      <tr>
                        <td>Let Ralph Ralph</td>
                        <td>✅ Yes</td>
                        <td>
                          Ralph discovers pattern, chooses when to use, writes
                          criteria
                        </td>
                      </tr>
                      <tr>
                        <td>Plan is disposable</td>
                        <td>✅ Yes</td>
                        <td>
                          Review requirements part of plan, regenerate if wrong
                        </td>
                      </tr>
                      <tr>
                        <td>Simplicity wins</td>
                        <td>✅ Yes</td>
                        <td>
                          Single function, binary result, no scoring complexity
                        </td>
                      </tr>
                      <tr>
                        <td>Add signs for Ralph</td>
                        <td>✅ Yes</td>
                        <td>
                          Light prompt additions, learning from code exploration
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </details>

            <details>
              <summary>
                <span class="summary-title">Ralph-Friendly Work Branches</span>
                <span class="summary-desc"
                  >Asking Ralph to "filter to feature X" at runtime is
                  unreliable. Instead, create scoped plan per branch
                  upfront.</span
                >
              </summary>
              <div class="details-content">
                <p>
                  <strong>The Critical Principle:</strong> Geoff's Ralph works
                  from a single, disposable plan where Ralph picks "most
                  important." To use branches with Ralph while maintaining this
                  pattern, you must scope at plan creation, not at task
                  selection.
                </p>

                <ul>
                  <li>
                    ❌ &nbsp;<em> Wrong Approach:</em> Create full plan, then
                    ask Ralph to "filter" tasks at runtime → unreliable
                    (70-80%), violates determinism
                  </li>
                  <li>
                    ✓ &nbsp;<em>Right Approach:</em> Create a scoped plan
                    upfront for each work branch → deterministic, simple,
                    maintains "plan is disposable"
                  </li>
                </ul>

                <p>
                  <strong>Solution:</strong> Add a <code>plan-work</code> mode
                  to create a work-scoped <code>IMPLEMENTATION_PLAN.md</code> on
                  the current branch. User creates work branch, then runs
                  <code>plan-work</code> with a natural language description of
                  the work focus. The LLM uses this description to scope the
                  plan. Post planning, Ralph builds from this already-scoped
                  plan with zero semantic filtering – just picks "most
                  important" as always.
                </p>

                <p>
                  "Work" is intentionally a broad term – it can describe
                  features, topics of concern, refactoring efforts,
                  infrastructure changes, bug fixes, or any coherent body of
                  related changes. The work description you pass to
                  <code>plan-work</code> is natural language for the LLM – it
                  can be prose, not constrained by git branch naming rules.
                </p>

                <h5>Design Principles</h5>
                <ul>
                  <li>
                    ✅
                    <em>Each Ralph session operates monolithically</em> on ONE
                    body of work per branch
                  </li>
                  <li>
                    ✅ <em>User creates branches manually</em> - full control
                    over naming conventions and strategy (e.g. worktrees)
                  </li>
                  <li>
                    ✅ <em>Natural language work descriptions</em> - pass prose
                    to LLM, unconstrained by git naming rules
                  </li>
                  <li>
                    ✅ <em>Scoping at plan creation</em> (deterministic) not
                    task selection (probabilistic)
                  </li>
                  <li>
                    ✅ <em>Single plan per branch</em> - one
                    IMPLEMENTATION_PLAN.md per branch
                  </li>
                  <li>
                    ✅ <em>Plan remains disposable</em> - regenerate scoped plan
                    when wrong/stale for a branch
                  </li>
                  <li>✅ No dynamic branch switching within a loop session</li>
                  <li>✅ Maintains simplicity and determinism</li>
                  <li>✅ Optional - main branch workflow still works</li>
                  <li>
                    ✅ No semantic filtering at build time - Ralph just picks
                    "most important"
                  </li>
                </ul>

                <p><strong>Workflow:</strong></p>
                <ol>
                  <li>
                    <p><em>Full Planning (on main branch)</em></p>
                    <div class="code-block">
                      <div class="code-block-header">
                        <span>bash</span>
                        <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                      </div>
                      <pre><code>./loop.sh plan
# Generate full IMPLEMENTATION_PLAN.md for entire project</code></pre>
                    </div>
                  </li>
                  <li>
                    <p><em>Create Work Branch</em></p>
                    <p>User performs:</p>
                    <div class="code-block">
                      <div class="code-block-header">
                        <span>bash</span>
                        <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                      </div>
                      <pre><code>git checkout -b ralph/user-auth-oauth
# Create branch with whatever naming convention you prefer
# Suggestion: ralph/* prefix for work branches</code></pre>
                    </div>
                  </li>
                  <li>
                    <p><em>Scoped Planning (on work branch)</em></p>
                    <div class="code-block">
                      <div class="code-block-header">
                        <span>bash</span>
                        <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                      </div>
                      <pre><code>./loop.sh plan-work "user authentication system with OAuth and session management"
# Pass natural language description - LLM uses this to scope the plan
# Creates focused IMPLEMENTATION_PLAN.md with only tasks for this work</code></pre>
                    </div>
                  </li>
                  <li>
                    <p><em>Build from Plan (on work branch)</em></p>
                    <div class="code-block">
                      <div class="code-block-header">
                        <span>bash</span>
                        <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                      </div>
                      <pre><code>./loop.sh
# Ralph builds from scoped plan (no filtering needed)
# Picks most important task from already-scoped plan</code></pre>
                    </div>
                  </li>
                  <li>
                    <p><em>PR Creation (when work complete)</em></p>
                    <p>User performs:</p>
                    <div class="code-block">
                      <div class="code-block-header">
                        <span>bash</span>
                        <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                      </div>
                      <pre><code>gh pr create --base main --head ralph/user-auth --fill</code></pre>
                    </div>
                  </li>
                </ol>

                <h5>Work-Scoped <code>loop.sh</code></h5>
                <p>
                  Extends the base enhanced loop script to add work branch
                  support with scoped planning:
                </p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>loop.sh</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>#!/bin/bash
set -euo pipefail

# Usage:
#   ./loop.sh [plan] [max_iterations]       # Plan/build on current branch
#   ./loop.sh plan-work "work description"  # Create scoped plan on current branch

# Parse arguments
MODE="build"
PROMPT_FILE="PROMPT_build.md"

if [ "$1" = "plan" ]; then
    MODE="plan"
    PROMPT_FILE="PROMPT_plan.md"
    MAX_ITERATIONS=${2:-0}
elif [ "$1" = "plan-work" ]; then
    if [ -z "$2" ]; then
        echo "Error: plan-work requires a work description"
        exit 1
    fi
    MODE="plan-work"
    WORK_DESCRIPTION="$2"
    PROMPT_FILE="PROMPT_plan_work.md"
    MAX_ITERATIONS=${3:-5}
elif [[ "$1" =~ ^[0-9]+$ ]]; then
    MAX_ITERATIONS=$1
else
    MAX_ITERATIONS=0
fi

# ... (see README for full script)</code></pre>
                </div>

                <h5><code>PROMPT_plan_work.md</code> Template</h5>

                <p>
                  <em>Note:</em> Identical to <code>PROMPT_plan.md</code> but
                  with scoping instructions and <code>WORK_SCOPE</code>
                  env var substituted (automatically by the loop script).
                </p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>PROMPT_plan_work.md</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>0a. Study `specs/*` with up to 250 parallel Sonnet subagents to learn the application specifications.
0b. Study @IMPLEMENTATION_PLAN.md (if present) to understand the plan so far.
0c. Study `src/lib/*` with up to 250 parallel Sonnet subagents to understand shared utilities &amp; components.
0d. For reference, the application source code is in `src/*`.

1. You are creating a SCOPED implementation plan for work: "${WORK_SCOPE}". Study @IMPLEMENTATION_PLAN.md (if present; it may be incorrect) and use up to 500 Sonnet subagents to study existing source code in `src/*` and compare it against `specs/*`. Use an Opus subagent to analyze findings, prioritize tasks, and create/update @IMPLEMENTATION_PLAN.md as a bullet point list sorted in priority of items yet to be implemented. Ultrathink. Consider searching for TODO, minimal implementations, placeholders, skipped/flaky tests, and inconsistent patterns. Study @IMPLEMENTATION_PLAN.md to determine starting point for research and keep it up to date with items considered complete/incomplete using subagents.

IMPORTANT: This is SCOPED PLANNING for "${WORK_SCOPE}" only. Create a plan containing ONLY tasks directly related to this work scope. Be conservative - if uncertain whether a task belongs to this work, exclude it. The plan can be regenerated if too narrow. Plan only. Do NOT implement anything. Do NOT assume functionality is missing; confirm with code search first. Treat `src/lib` as the project's standard library for shared utilities and components. Prefer consolidated, idiomatic implementations there over ad-hoc copies.

ULTIMATE GOAL: We want to achieve the scoped work "${WORK_SCOPE}". Consider missing elements related to this work and plan accordingly. If an element is missing, search first to confirm it doesn't exist, then if needed author the specification at specs/FILENAME.md. If you create a new element then document the plan to implement it in @IMPLEMENTATION_PLAN.md using a subagent.</code></pre>
                </div>

                <h5>Compatibility with Core Philosophy</h5>
                <div class="table-wrapper">
                  <table>
                    <thead>
                      <tr>
                        <th>Principle</th>
                        <th>Maintained?</th>
                        <th>How</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>Monolithic operation</td>
                        <td>✅ Yes</td>
                        <td>
                          Ralph still operates as single process within branch
                        </td>
                      </tr>
                      <tr>
                        <td>One task per loop</td>
                        <td>✅ Yes</td>
                        <td>Unchanged</td>
                      </tr>
                      <tr>
                        <td>Fresh context</td>
                        <td>✅ Yes</td>
                        <td>Unchanged</td>
                      </tr>
                      <tr>
                        <td>Deterministic</td>
                        <td>✅ Yes</td>
                        <td>
                          Scoping at plan creation (deterministic), not runtime
                        </td>
                      </tr>
                      <tr>
                        <td>Simple</td>
                        <td>✅ Yes</td>
                        <td>Optional enhancement, main workflow still works</td>
                      </tr>
                      <tr>
                        <td>Plan-driven</td>
                        <td>✅ Yes</td>
                        <td>One IMPLEMENTATION_PLAN.md per branch</td>
                      </tr>
                      <tr>
                        <td>Single source of truth</td>
                        <td>✅ Yes</td>
                        <td>
                          One plan per branch – scoped plan replaces full plan
                          on branch
                        </td>
                      </tr>
                      <tr>
                        <td>Plan is disposable</td>
                        <td>✅ Yes</td>
                        <td>
                          Regenerate scoped plan anytime:
                          <code>./loop.sh plan-work "work description"</code>
                        </td>
                      </tr>
                      <tr>
                        <td>Markdown over JSON</td>
                        <td>✅ Yes</td>
                        <td>Still markdown plans</td>
                      </tr>
                      <tr>
                        <td>Let Ralph Ralph</td>
                        <td>✅ Yes</td>
                        <td>
                          Ralph picks "most important" from already-scoped plan
                          – no filter
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </details>

            <details>
              <summary>
                <span class="summary-title"
                  >JTBD → Story Map → SLC Release</span
                >
                <span class="summary-desc"
                  >Push the power of "Letting Ralph Ralph" to connect JTBD's
                  audience and activities to Simple/Lovable/Complete
                  releases.</span
                >
              </summary>
              <div class="details-content">
                <h5>Topics of Concern → Activities</h5>
                <p>
                  Geoff's
                  <a
                    href="https://ghuntley.com/content/images/size/w2400/2025/07/The-ralph-Process.png"
                    >suggested workflow</a
                  >
                  already aligns planning with Jobs-to-be-Done – breaking JTBDs
                  into topics of concern, which in turn become specs. I think
                  there's an opportunity to lean further into the product
                  benefits this approach affords by reframing
                  <em>topics of concern</em> as <em>activities</em>.
                </p>
                <p>
                  Activities are verbs in a journey ("upload photo", "extract
                  colors") rather than capabilities ("color extraction system").
                  They're naturally scoped by user intent.
                </p>
                <blockquote>
                  <p style="margin-bottom: 0.5rem">
                    Topics: "color extraction", "layout engine" →
                    capability-oriented
                  </p>
                  <p>
                    Activities: "upload photo", "see extracted colors", "arrange
                    layout" → journey-oriented
                  </p>
                </blockquote>
                <h5>Activities → User Journey</h5>
                <p>
                  Activities – and their constituent steps – sequence naturally
                  into a user flow, creating a <em>journey structure</em> that
                  makes gaps and dependencies visible. A
                  <a href="https://www.nngroup.com/articles/user-story-mapping/"
                    >User Story Map</a
                  >
                  organizes activities as columns (the journey backbone) with
                  capability depths as rows – the full space of what
                  <em>could</em> be built:
                </p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>diagram</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>UPLOAD    →   EXTRACT    →   ARRANGE     →   SHARE

basic         auto           manual          export
bulk          palette        templates       collab
batch         AI themes      auto-layout     embed</code></pre>
                </div>

                <h5>User Journey → Release Slices</h5>
                <p>
                  Horizontal slices through the map become candidate releases.
                  Not every activity needs new capability in every release —
                  some cells stay empty, and that's fine if the slice is still
                  coherent:
                </p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>diagram</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>              UPLOAD    →   EXTRACT    →   ARRANGE     →   SHARE

Release 1:    basic         auto                           export
              ───────────────────────────────────────────────────
Release 2:                  palette        manual
              ───────────────────────────────────────────────────
Release 3:    batch         AI themes      templates       embed</code></pre>
                </div>

                <h5>Release Slices → SLC Releases</h5>
                <p>
                  The story map gives you <em>structure</em> for slicing. Jason
                  Cohen's
                  <a href="https://longform.asmartbear.com/slc/"
                    >Simple, Lovable, Complete (SLC)</a
                  >
                  gives you <em>criteria</em> for what makes a slice good:
                </p>
                <ul>
                  <li>
                    <em>Simple</em> – Narrow scope you can ship fast. Not every
                    activity, not every depth.
                  </li>
                  <li>
                    <em>Complete</em> – Fully accomplishes a job within that
                    scope. Not a broken preview.
                  </li>
                  <li>
                    <em>Lovable</em> – People actually want to use it.
                    Delightful within its boundaries.
                  </li>
                </ul>

                <p>
                  <strong>Why SLC over MVP?</strong> MVPs optimize for learning
                  at the customer's expense – "minimum" often means broken or
                  frustrating. SLC flips this: learn in-market
                  <em>while</em> delivering real value. If it succeeds, you have
                  optionality. If it fails, you still treated users well.
                </p>

                <p>
                  Each slice can become a release with a clear value and
                  identity:
                </p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>diagram</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>                 UPLOAD  →   EXTRACT    →   ARRANGE     →   SHARE

Palette Picker:  basic       auto                           export
                 ───────────────────────────────────────────────────
Mood Board:                  palette        manual
                ───────────────────────────────────────────────────
Design Studio:   batch       AI themes      templates       embed</code></pre>
                </div>
                <ul>
                  <li>
                    <em>Palette Picker</em> – Upload, extract, export. Instant
                    value from day one.
                  </li>
                  <li>
                    <em>Mood Board</em> – Adds arrangement. Creative expression
                    enters the journey.
                  </li>
                  <li>
                    <em>Design Studio</em> – Professional features: batch
                    processing, AI themes, embeddable output.
                  </li>
                </ul>

                <h5>Operationalizing with Ralph</h5>
                <p>
                  The concepts above – activities, story maps, SLC releases –
                  are the <em>thinking tools</em>. How do we translate them into
                  Ralph's workflow?
                </p>

                <p><em>Default Ralph approach:</em></p>
                <ol>
                  <li>
                    <em>Define Requirements</em>: Human + LLM define JTBD topics
                    of concern → <code>specs/*.md</code>
                  </li>
                  <li>
                    <em>Create Tasks Plan</em>: LLM analyzes all specs + current
                    code → <code>IMPLEMENTATION_PLAN.md</code>
                  </li>
                  <li><em>Build</em>: Ralph builds against full scope</li>
                </ol>

                <p>
                  This works well for capability-focused work (features,
                  refactors, infrastructure). But it doesn't naturally produce
                  valuable (SLC) product releases – it produces "whatever the
                  specs describe".
                </p>

                <p><em>Activities → SLC Release approach:</em></p>
                <p>
                  To get SLC releases, we need to ground activities in audience
                  context. Audience defines WHO has the JTBDs, which in turn
                  informs WHAT activities matter and what "lovable" means.
                </p>
                <div class="code-block">
                  <div class="code-block-header">
                    <span>diagram</span>
                    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
                  </div>
                  <pre><code>Audience (who)
    └── has JTBDs (why)
            └── fulfilled by Activities (how)</code></pre>
                </div>

                <h5>Workflow</h5>
                <p><em>I. Requirements Phase (2 steps):</em></p>
                <p>
                  Still performed in LLM conversations with the human, similar
                  to the default Ralph approach.
                </p>
                <ol>
                  <li>
                    <em>Define audience and their JTBDs</em> – WHO are we
                    building for and what OUTCOMES do they want?
                    <ul>
                      <li>
                        Human + LLM discuss and determine the audience(s) and
                        their JTBDs (outcomes they want)
                      </li>
                      <li>
                        May contain multiple connected audiences (e.g.
                        "designer" creates, "client" reviews)
                      </li>
                      <li>Generates <code>AUDIENCE_JTBD.md</code></li>
                    </ul>
                  </li>
                  <li>
                    <em>Define activities</em> – WHAT do users do to accomplish
                    their JTBDs?
                    <ul>
                      <li>Informed by <code>AUDIENCE_JTBD.md</code></li>
                      <li>
                        For each JTBD, identify activities necessary to
                        accomplish it
                      </li>
                      <li>
                        For each activity, determine:
                        <ul>
                          <li>
                            Capability depths (basic → enhanced) – levels of
                            sophistication
                          </li>
                          <li>
                            Desired outcome(s) at each depth – what does success
                            look like?
                          </li>
                        </ul>
                      </li>
                      <li>
                        Generates <code>specs/*.md</code> (one per activity)
                      </li>
                    </ul>
                  </li>
                </ol>
                <p>
                  The discrete steps within activities are implicit and LLM can
                  infer them during planning.
                </p>

                <p><em>II. Planning Phase:</em></p>
                <p>
                  Performed in Ralph loop with <em>updated</em> planning prompt.
                </p>
                <ul>
                  <li>
                    LLM analyzes:
                    <ul>
                      <li>
                        <code>AUDIENCE_JTBD.md</code> (who, desired outcomes)
                      </li>
                      <li><code>specs/*</code> (what could be built)</li>
                      <li>Current code state (what exists)</li>
                    </ul>
                  </li>
                  <li>
                    LLM determines next SLC slice (which activities, at what
                    capability depths) and plans tasks for that slice
                  </li>
                  <li>LLM generates <code>IMPLEMENTATION_PLAN.md</code></li>
                  <li>
                    <em>Human verifies</em> plan before building:
                    <ul>
                      <li>Does the scope represent a coherent SLC release?</li>
                      <li>
                        Are the right activities included at the right depths?
                      </li>
                      <li>
                        If wrong → re-run planning loop to regenerate plan,
                        optionally updating inputs or planning prompt
                      </li>
                      <li>If right → proceed to building</li>
                    </ul>
                  </li>
                </ul>

                <p>
                  <em>III. Building Phase:</em> Performed in Ralph loop with
                  standard building prompt.
                </p>

                  <h5>Updated <code></code>PROMPT_plan_slc.md</code> Template</h5>
                    <p>
                      Variant of <code>PROMPT_plan.md</code> that adds audience
                      context and SLC-oriented slice recommendation.
                    </p>
                    <p>
                      <em>Notes:</em>
                      <ul>
                        <li>Unlike the default template, this does not
                      have a <code>[project-specific goal]</code> placeholder –
                      the goal is implicit: recommend the most valuable next
                      release for the audience.
                      </li>
                      <li>
                        Current subagents names presume using Claude.
                      </li>
                    </ul>
                    </p>
                    <div class="code-block">
                      <div class="code-block-header">
                        <span>PROMPT_plan_slc.md</span>
                        <button class="copy-btn" onclick="copyCode(this)">
                          Copy
                        </button>
                      </div>
                      <pre><code>0a. Study @AUDIENCE_JTBD.md to understand who we're building for and their Jobs to Be Done.
0b. Study `specs/*` with up to 250 parallel Sonnet subagents to learn JTBD activities.
0c. Study @IMPLEMENTATION_PLAN.md (if present) to understand the plan so far.
0d. Study `src/lib/*` with up to 250 parallel Sonnet subagents to understand shared utilities &amp; components.
0e. For reference, the application source code is in `src/*`.

1. Sequence the activities in `specs/*` into a user journey map for the audience in @AUDIENCE_JTBD.md. Consider how activities flow into each other and what dependencies exist.

2. Determine the next SLC release. Use up to 500 Sonnet subagents to compare `src/*` against `specs/*`. Use an Opus subagent to analyze findings. Ultrathink. Given what's already implemented recommend which activities (at what capability depths) form the most valuable next release. Prefer thin horizontal slices - the narrowest scope that still delivers real value. A good slice is Simple (narrow, achievable), Lovable (people want to use it), and Complete (fully accomplishes a meaningful job, not a broken preview).

3. Use an Opus subagent (ultrathink) to analyze and synthesize the findings, prioritize tasks, and create/update @IMPLEMENTATION_PLAN.md as a bullet point list sorted in priority of items yet to be implemented for the recommended SLC release. Begin plan with a summary of the recommended SLC release (what's included and why), then list prioritized tasks for that scope. Consider TODOs, placeholders, minimal implementations, skipped tests - but scoped to the release. Note discoveries outside scope as future work.

IMPORTANT: Plan only. Do NOT implement anything. Do NOT assume functionality is missing; confirm with code search first. Treat `src/lib` as the project's standard library for shared utilities and components. Prefer consolidated, idiomatic implementations there over ad-hoc copies.

ULTIMATE GOAL: We want to achieve the most valuable next release for the audience in @AUDIENCE_JTBD.md. Consider missing elements and plan accordingly. If an element is missing, search first to confirm it doesn't exist, then if needed author the specification at specs/FILENAME.md. If you create a new element then document the plan to implement it in @IMPLEMENTATION_PLAN.md using a subagent.</code></pre>
                    </div>

                <h5>Notes</h5>
                <p>
                  <em
                    >Why <code>AUDIENCE_JTBD.md</code> as a separate
                    artifact:</em
                  >
                </p>
                <ul>
                  <li>Single source of truth – prevents drift across specs</li>
                  <li>
                    Enables holistic reasoning: "What does this audience need
                    MOST?"
                  </li>
                  <li>
                    JTBDs captured alongside audience (the "why" lives with the
                    "who")
                  </li>
                  <li>
                    Referenced twice: during spec creation AND SLC planning
                  </li>
                  <li>
                    Keeps activity specs focused on WHAT, not repeating WHO
                  </li>
                </ul>

                <p><em>Cardinalities:</em></p>
                <ul>
                  <li>
                    One audience → many JTBDs ("Designer" has "capture space",
                    "explore concepts", "present to client")
                  </li>
                  <li>
                    One JTBD → many activities ("capture space" includes upload,
                    measurements, room detection)
                  </li>
                  <li>
                    One activity → can serve multiple JTBDs ("upload photo"
                    serves both "capture" and "gather inspiration")
                  </li>
                </ul>
              </div>
            </details>
          </section>

          <!-- Footer -->
          <footer class="article-footer">
            <p>
              View source on
              <a href="https://github.com/ClaytonFarr/ralph-playbook">GitHub</a
              >.
            </p>
          </footer>
        </main>

        <!-- Sidebar TOC -->
        <aside class="toc-sidebar">
          <nav class="toc-nav" aria-label="Table of contents">
            <ul class="toc-list">
              <li><a href="#intro" class="toc-link">Intro</a></li>
              <li><a href="#workflow" class="toc-link">Workflow</a></li>
              <li>
                <a href="#key-principles" class="toc-link">Key Principles</a>
              </li>
              <li>
                <a href="#loop-mechanics" class="toc-link">Loop Mechanics</a>
              </li>
              <li><a href="#files" class="toc-link">Files</a></li>
              <li>
                <a href="#enhancements" class="toc-link">Enhancements?</a>
              </li>
            </ul>
          </nav>
        </aside>
      </div>
    </div>

    <script>
      // Copy to clipboard functionality
      function copyCode(button) {
        const codeBlock = button
          .closest(".code-block")
          .querySelector("pre code");
        const text = codeBlock.textContent;

        navigator.clipboard.writeText(text).then(() => {
          const originalText = button.textContent;
          button.textContent = "Copied!";
          button.style.color = "#00aa44";
          setTimeout(() => {
            button.textContent = originalText;
            button.style.color = "";
          }, 2000);
        });
      }

      // Highlight current TOC item on scroll
      const tocLinks = document.querySelectorAll(".toc-link");
      const sections = document.querySelectorAll("section[id], header[id]");

      function updateTocHighlight() {
        const scrollPos = window.scrollY + 100;
        let activeSet = false;

        // Check if we're at the very top (intro section)
        if (scrollPos < 200) {
          tocLinks.forEach((link) => {
            link.classList.remove("active");
            if (link.getAttribute("href") === "#intro") {
              link.classList.add("active");
            }
          });
          return;
        }

        sections.forEach((section) => {
          const sectionTop = section.offsetTop;
          const sectionHeight = section.offsetHeight;
          const sectionId = section.getAttribute("id");

          if (
            scrollPos >= sectionTop &&
            scrollPos < sectionTop + sectionHeight
          ) {
            tocLinks.forEach((link) => {
              link.classList.remove("active");
              if (link.getAttribute("href") === "#" + sectionId) {
                link.classList.add("active");
                activeSet = true;
              }
            });
          }
        });
      }

      window.addEventListener("scroll", updateTocHighlight);
      updateTocHighlight();
    </script>
  </body>
</html>
```

## File: `files/AGENTS.md`
```markdown
## Build & Run

Succinct rules for how to BUILD the project:

## Validation

Run these after implementing to get immediate feedback:

- Tests: `[test command]`
- Typecheck: `[typecheck command]`
- Lint: `[lint command]`

## Operational Notes

Succinct learnings about how to RUN the project:

...

### Codebase Patterns

...
```

## File: `files/IMPLEMENTATION_PLAN.md`
```markdown
<!-- Generated by LLM with content and structure it deems most appropriate -->
```

## File: `files/PROMPT_build.md`
```markdown
0a. Study `specs/*` with up to 500 parallel Sonnet subagents to learn the application specifications.
0b. Study @IMPLEMENTATION_PLAN.md.
0c. For reference, the application source code is in `src/*`.

1. Your task is to implement functionality per the specifications using parallel subagents. Follow @IMPLEMENTATION_PLAN.md and choose the most important item to address. Before making changes, search the codebase (don't assume not implemented) using Sonnet subagents. You may use up to 500 parallel Sonnet subagents for searches/reads and only 1 Sonnet subagent for build/tests. Use Opus subagents when complex reasoning is needed (debugging, architectural decisions).
2. After implementing functionality or resolving problems, run the tests for that unit of code that was improved. If functionality is missing then it's your job to add it as per the application specifications. Ultrathink.
3. When you discover issues, immediately update @IMPLEMENTATION_PLAN.md with your findings using a subagent. When resolved, update and remove the item.
4. When the tests pass, update @IMPLEMENTATION_PLAN.md, then `git add -A` then `git commit` with a message describing the changes. After the commit, `git push`.

99999. Important: When authoring documentation, capture the why — tests and implementation importance.
999999. Important: Single sources of truth, no migrations/adapters. If tests unrelated to your work fail, resolve them as part of the increment.
9999999. As soon as there are no build or test errors create a git tag. If there are no git tags start at 0.0.0 and increment patch by 1 for example 0.0.1  if 0.0.0 does not exist.
99999999. You may add extra logging if required to debug issues.
999999999. Keep @IMPLEMENTATION_PLAN.md current with learnings using a subagent — future work depends on this to avoid duplicating efforts. Update especially after finishing your turn.
9999999999. When you learn something new about how to run the application, update @AGENTS.md using a subagent but keep it brief. For example if you run commands multiple times before learning the correct command then that file should be updated.
99999999999. For any bugs you notice, resolve them or document them in @IMPLEMENTATION_PLAN.md using a subagent even if it is unrelated to the current piece of work.
999999999999. Implement functionality completely. Placeholders and stubs waste efforts and time redoing the same work.
9999999999999. When @IMPLEMENTATION_PLAN.md becomes large periodically clean out the items that are completed from the file using a subagent.
99999999999999. If you find inconsistencies in the specs/* then use an Opus 4.5 subagent with 'ultrathink' requested to update the specs.
999999999999999. IMPORTANT: Keep @AGENTS.md operational only — status updates and progress notes belong in `IMPLEMENTATION_PLAN.md`. A bloated AGENTS.md pollutes every future loop's context.
```

## File: `files/PROMPT_plan.md`
```markdown
0a. Study `specs/*` with up to 250 parallel Sonnet subagents to learn the application specifications.
0b. Study @IMPLEMENTATION_PLAN.md (if present) to understand the plan so far.
0c. Study `src/lib/*` with up to 250 parallel Sonnet subagents to understand shared utilities & components.
0d. For reference, the application source code is in `src/*`.

1. Study @IMPLEMENTATION_PLAN.md (if present; it may be incorrect) and use up to 500 Sonnet subagents to study existing source code in `src/*` and compare it against `specs/*`. Use an Opus subagent to analyze findings, prioritize tasks, and create/update @IMPLEMENTATION_PLAN.md as a bullet point list sorted in priority of items yet to be implemented. Ultrathink. Consider searching for TODO, minimal implementations, placeholders, skipped/flaky tests, and inconsistent patterns. Study @IMPLEMENTATION_PLAN.md to determine starting point for research and keep it up to date with items considered complete/incomplete using subagents.

IMPORTANT: Plan only. Do NOT implement anything. Do NOT assume functionality is missing; confirm with code search first. Treat `src/lib` as the project's standard library for shared utilities and components. Prefer consolidated, idiomatic implementations there over ad-hoc copies.

ULTIMATE GOAL: We want to achieve [project-specific goal]. Consider missing elements and plan accordingly. If an element is missing, search first to confirm it doesn't exist, then if needed author the specification at specs/FILENAME.md. If you create a new element then document the plan to implement it in @IMPLEMENTATION_PLAN.md using a subagent.
```

## File: `files/loop.sh`
```bash
#!/bin/bash
# Usage: ./loop.sh [plan] [max_iterations]
# Examples:
#   ./loop.sh              # Build mode, unlimited iterations
#   ./loop.sh 20           # Build mode, max 20 iterations
#   ./loop.sh plan         # Plan mode, unlimited iterations
#   ./loop.sh plan 5       # Plan mode, max 5 iterations

# Parse arguments
if [ "$1" = "plan" ]; then
    # Plan mode
    MODE="plan"
    PROMPT_FILE="PROMPT_plan.md"
    MAX_ITERATIONS=${2:-0}
elif [[ "$1" =~ ^[0-9]+$ ]]; then
    # Build mode with max iterations
    MODE="build"
    PROMPT_FILE="PROMPT_build.md"
    MAX_ITERATIONS=$1
else
    # Build mode, unlimited (no arguments or invalid input)
    MODE="build"
    PROMPT_FILE="PROMPT_build.md"
    MAX_ITERATIONS=0
fi

ITERATION=0
CURRENT_BRANCH=$(git branch --show-current)

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Mode:   $MODE"
echo "Prompt: $PROMPT_FILE"
echo "Branch: $CURRENT_BRANCH"
[ $MAX_ITERATIONS -gt 0 ] && echo "Max:    $MAX_ITERATIONS iterations"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Verify prompt file exists
if [ ! -f "$PROMPT_FILE" ]; then
    echo "Error: $PROMPT_FILE not found"
    exit 1
fi

while true; do
    if [ $MAX_ITERATIONS -gt 0 ] && [ $ITERATION -ge $MAX_ITERATIONS ]; then
        echo "Reached max iterations: $MAX_ITERATIONS"
        break
    fi

    # Run Ralph iteration with selected prompt
    # -p: Headless mode (non-interactive, reads from stdin)
    # --dangerously-skip-permissions: Auto-approve all tool calls (YOLO mode)
    # --output-format=stream-json: Structured output for logging/monitoring
    # --model opus: Primary agent uses Opus for complex reasoning (task selection, prioritization)
    #               Can use 'sonnet' in build mode for speed if plan is clear and tasks well-defined
    # --verbose: Detailed execution logging
    cat "$PROMPT_FILE" | claude -p \
        --dangerously-skip-permissions \
        --output-format=stream-json \
        --model opus \
        --verbose

    # Push changes after each iteration
    git push origin "$CURRENT_BRANCH" || {
        echo "Failed to push. Creating remote branch..."
        git push -u origin "$CURRENT_BRANCH"
    }

    ITERATION=$((ITERATION + 1))
    echo -e "\n\n======================== LOOP $ITERATION ========================\n"
done
```

## File: `references/sandbox-environments.md`
```markdown
<!-- cSpell:disable -->

# Sandbox Environments for AI Agent Workflows

_Security model:_ The sandbox (Docker/E2B) provides the security boundary. Inside the sandbox, Claude runs with full permissions because the container itself is isolated.

_Security philosophy:_

> "It's not if it gets popped, it's when it gets popped. And what is the blast radius?"

Run on dedicated VMs or local Docker sandboxes. Restrict network connectivity, provide only necessary credentials, and ensure no access to private data beyond what the task requires.

---

## Options

### Sprites (Fly.io)

- Persistent Linux environments that survive between executions indefinitely
- Firecracker VM isolation with up to 8 vCPUs and 8GB RAM
- Fast checkpoint/restore (~300ms create, <1s restore)
- Auto-sleep after 30 seconds of inactivity
- Unique HTTPS URL per Sprite for webhooks, APIs, public access
- Layer 3 network policies for egress control (whitelist domains or use default LLM-friendly list)
- CLI, REST API, JavaScript SDK, Go SDK (Python and Elixir coming soon)
- Pre-installed tools: Claude Code, Codex CLI, Gemini CLI, Python 3.13, Node.js 22.20
- $30 free credits to start (~500 Sprites worth)

_Philosophy:_ Fly.io argues that "ephemeral sandboxes are obsolete" and that AI agents need persistent computers, not disposable containers. Sprites treat sandboxes as "actual computers" where data, packages, and services persist across executions on ext4 NVMe storage—no need to rebuild environments repeatedly. As they put it: "Claude doesn't want a stateless container."

_Unique Features:_

- _Stateful persistence_: Files, packages, databases survive between runs indefinitely
- _Transactional snapshots_: Copy-on-write checkpoints capture entire disk state; stores last 5 checkpoints
- _Idle cost optimization_: Auto-sleep when inactive (30s timeout), resume on request (<1s wake)
- _Cold start_: Creation in 1-2 seconds, restore under 1 second
- _Claude integration_: Pre-installed skills teach Claude how to use Sprites (port forwarding, etc.)
- _Storage billing_: Pay only for blocks written, not allocated space; TRIM-friendly
- _No time limits_: Unlike ephemeral sandboxes (typically 15-minute limits), Sprites support long-running workloads

_Pricing:_

| Resource | Cost             | Minimum             |
| -------- | ---------------- | ------------------- |
| CPU      | $0.07/CPU-hour   | 6.25% utilization/s |
| Memory   | $0.04375/GB-hour | 250MB per second    |
| Storage  | $0.00068/GB-hour | Actual blocks only  |

- Free trial: $30 in credits (~500 Sprites)
- Plan: $20/month includes monthly credits; overages at published rates
- Example costs: 4-hour coding session ~$0.46, web app with 30 active hours ~$4/month

_Specs:_

| Spec         | Value                                                          |
| ------------ | -------------------------------------------------------------- |
| Isolation    | Firecracker microVM (hardware-isolated)                        |
| Resources    | Up to 8 vCPUs, 8GB RAM per execution (fixed, not configurable) |
| Storage      | 100GB initial ext4 partition on NVMe, auto-scaling capacity    |
| Cold Start   | <1 second restore, 1-2 seconds creation                        |
| Timeout      | None (persistent); auto-sleeps after 30 seconds inactivity     |
| Active Limit | 10 simultaneous active Sprites on base plan; unlimited cold    |
| Network      | Port 8080 proxied for HTTP services; isolated networks         |

_Limitations:_

- Resource caps (8 vCPU, 8GB RAM, 100GB storage) not configurable yet
- 30-second idle timeout not configurable
- Region selection not available (auto-assigned based on geographic location)
- Maximum 10 active sprites on base plan (unlimited cold/inactive sprites allowed)
- Best for personal/organizational tools; not designed for million-user scale apps

_Links:_

- Official: https://sprites.dev/
- Documentation: https://docs.sprites.dev/
- Fly.io Blog: https://fly.io/blog/code-and-let-live/
- JavaScript SDK: https://github.com/superfly/sprites-js
- Go SDK: https://github.com/superfly/sprites-go
- Elixir SDK: https://github.com/superfly/sprites-ex
- Community: https://community.fly.io/c/sprites/

---

### E2B

- Purpose-built for AI agents and LLM workflows
- Pre-built template `anthropic-claude-code` ships with Claude Code CLI ready
- Single-line SDK calls in Python or JavaScript (v1.5.1+)
- Full filesystem + git for progress.txt, prd.json, and repo operations
- 24-hour session limits on Pro plan (1 hour on Hobby)
- Native access to 200+ MCP tools via Docker partnership (GitHub, Notion, Stripe, etc.)
- Configurable compute: 1-8 vCPU, 512MB-8GB RAM

_Philosophy:_ E2B believes AI agents need transient, immutable workloads with hardware-level kernel isolation. Each sandbox runs in its own Firecracker microVM, providing the same isolation as AWS Lambda. The focus is on developer experience—one SDK call to create a sandbox.

_Unique Features:_

- _Fastest cold start_: ~150-200ms via Firecracker microVMs
- _Pre-built Claude template_: Zero-setup Claude Code integration
- _Docker MCP Partnership_: Native access to 200+ MCP tools from Docker's catalog
- _Pause/Resume (Beta)_: Save full VM state including memory (~4s per 1GB to pause, ~1s to resume, state persists up to 30 days)
- _Network controls_: `allowInternetAccess` toggle, `network.allowOut`/`network.denyOut` for granular CIDR/domain filtering
- _Domain filtering_: Works for HTTP (port 80) and TLS (port 443) via SNI inspection

_Pricing:_

| Plan       | Monthly Fee | Session Limit | Notes                       |
| ---------- | ----------- | ------------- | --------------------------- |
| Hobby      | $0          | 1 hour        | + $100 one-time credit      |
| Pro        | $150        | 24 hours      | + usage costs               |
| Enterprise | Custom      | Custom        | SSO, SLA, dedicated support |

_Usage Rates (per second):_

| Resource | Rate           |
| -------- | -------------- |
| 2 vCPU   | $0.000028/s    |
| Memory   | $0.0000045/GiB |

_Specs:_

| Spec          | Value                                  |
| ------------- | -------------------------------------- |
| Isolation     | Firecracker microVM                    |
| Cold Start    | ~150-200ms                             |
| Timeout       | 1 hour (Hobby), 24 hours (Pro)         |
| Compute       | 1-8 vCPU, 512MB-8GB RAM (configurable) |
| Filesystem    | Full Linux with git support            |
| Pre-installed | Node.js, curl, ripgrep, Claude Code    |

_Limitations:_

- No native sandbox clone/fork functionality
- No bulk file reading API
- Domain filtering limited to HTTP/HTTPS ports (UDP/QUIC not supported)
- Self-hosted version lacks built-in network policies
- Occasional 502 timeout errors on long operations
- Sandbox "not found" errors near timeout boundaries

_Links:_

- Official: https://e2b.dev/
- Documentation: https://e2b.dev/docs
- Pricing: https://e2b.dev/pricing
- Python Guide: https://e2b.dev/blog/python-guide-run-claude-code-in-an-e2b-sandbox
- JavaScript Guide: https://e2b.dev/blog/javascript-guide-run-claude-code-in-an-e2b-sandbox
- Claude Code Template: https://e2b.dev/brain/knowledge/docs_legacy/code-interpreter/claude-code
- MCP Server: https://github.com/e2b-dev/mcp-server
- GitHub: https://github.com/e2b-dev/E2B

---

### Modal

Modal Sandboxes are the Modal primitive for safely running untrusted code from LLMs, users, or third-party sources. Built on Modal's serverless container fabric with gVisor isolation.

_Key Features:_

- Pure Python SDK for defining sandboxes with one line of code (also JS/Go SDKs)
- Execute arbitrary commands with `sandbox.exec()` and stream output
- Autoscale from zero to 10,000+ concurrent sandboxes
- Dynamic image definition at runtime from model output
- Built-in tunneling for HTTP/WebSocket connections to sandbox servers
- Granular egress policies via CIDR allowlists
- Named sandboxes for persistent reference and pooling
- Production-proven: Lovable and Quora run millions of code executions daily

_Philosophy:_ Modal treats sandboxes as secure, ephemeral compute units that inherit its serverless fabric. The focus is on Python-first AI/ML workloads with aggressive cost optimization through scale-to-zero, trading cold start latency for resource efficiency.

_Unique Features:_

- _Sandbox Connect Tokens_: Authenticated HTTP/WebSocket access with unspoofable `X-Verified-User-Data` headers for access control
- _Memory Snapshots_: Capture container memory state to reduce cold starts to <3s even with large dependencies like PyTorch
- _Idle Timeout_: Auto-terminate sandboxes after configurable inactivity period
- _Filesystem Snapshots_: Preserve state across sandbox instances for 24+ hour workflows
- _No pre-provisioning_: Sandboxes created on-demand without capacity planning

_Pricing (as of late 2025, after 65% price reduction):_

| Plan       | Monthly Fee | Credits Included | Seats | Container Limits                |
| ---------- | ----------- | ---------------- | ----- | ------------------------------- |
| Starter    | $0          | $30/month        | 3     | 100 containers, 10 GPU          |
| Team       | $250        | $100/month       | ∞     | 1,000 containers, 50 GPU        |
| Enterprise | Custom      | Volume discounts | ∞     | Custom limits, HIPAA, SSO, etc. |

_Compute Rates (per second):_

| Resource              | Rate             | Notes                        |
| --------------------- | ---------------- | ---------------------------- |
| Sandbox/Notebook CPU  | $0.00003942/core | Per physical core (= 2 vCPU) |
| Standard Function CPU | $0.0000131/core  | Per physical core            |
| Memory                | $0.00000222/GiB  | Pay for actual usage         |
| GPU (A10G)            | $0.000306/s      | ~$1.10/hr                    |
| GPU (A100 40GB)       | $0.000583/s      | ~$2.10/hr                    |
| GPU (H100)            | $0.001097/s      | ~$3.95/hr                    |

_Special Credits:_ Startups up to $25k, Academics up to $10k free compute

_Specs:_

| Spec               | Value                                         |
| ------------------ | --------------------------------------------- |
| Isolation          | gVisor (Google's container runtime)           |
| Cold Start         | ~1s container boot, 2-5s typical with imports |
| With Snapshots     | <3s even with large dependencies              |
| Default Timeout    | 5 minutes                                     |
| Max Timeout        | 24 hours (use snapshots for longer)           |
| Idle Timeout       | Configurable auto-termination                 |
| Filesystem         | Ephemeral (use Volumes for persistence)       |
| Network Default    | Secure-by-default, no incoming connections    |
| Egress Control     | `block_network=True` or `cidr_allowlist`      |
| Concurrent Scaling | 10,000+ sandboxes                             |

_Volumes (Persistent Storage):_

- High-performance distributed filesystem (up to 2.5 GB/s bandwidth)
- Volumes v2 (beta): No file count limit, 1 TiB max file size, HIPAA-compliant deletion
- Explicit `commit()` required to persist changes
- Last-write-wins for concurrent modifications to same file
- Best for model weights, checkpoints, and datasets

_Limitations:_

- Cold start penalties when containers spin down (2-5s typical)
- No on-premises deployment option
- Sandboxes cannot access other Modal workspace resources by default
- Single-language focus (Python-optimized, less suited for multi-language untrusted code)
- Volumes require explicit reload to see changes from other containers
- Less suited for persistent, long-lived environments vs microVM solutions

_Modal vs E2B for AI Agents:_

| Aspect           | Modal                           | E2B                            |
| ---------------- | ------------------------------- | ------------------------------ |
| Isolation        | gVisor containers               | Firecracker microVMs           |
| Cold Start       | 2-5s typical, <3s with snapshot | ~150ms                         |
| Session Duration | Up to 24h (stateless)           | Up to 24h (Pro), persistent    |
| Self-Hosting     | No (managed only)               | Experimental                   |
| Multi-Language   | Python-focused                  | Python, JS, Ruby, C++          |
| Network Control  | Granular egress policies        | Allow/deny lists               |
| Best For         | Python ML/AI, batch workloads   | Multi-language agent sandboxes |

_Links:_

- Sandbox Product: https://modal.com/use-cases/sandboxes
- Sandbox Docs: https://modal.com/brain/knowledge/docs_legacy/guide/sandboxes
- Sandbox Networking: https://modal.com/brain/knowledge/docs_legacy/guide/sandbox-networking
- API Reference: https://modal.com/brain/knowledge/docs_legacy/reference/modal.Sandbox
- Safe Code Execution Example: https://modal.com/brain/knowledge/docs_legacy/examples/safe_code_execution
- Coding Agent Example: https://modal.com/brain/knowledge/docs_legacy/examples/agent
- Pricing: https://modal.com/pricing
- Cold Start Guide: https://modal.com/brain/knowledge/docs_legacy/guide/cold-start
- Volumes: https://modal.com/brain/knowledge/docs_legacy/guide/volumes
- Security: https://modal.com/brain/knowledge/docs_legacy/guide/security

---

### Cloudflare Sandboxes

- Open Beta (announced June 2025), still experimental
- Edge-native (330+ global locations)
- Pay for active CPU only (not provisioned resources)
- Best if already in Cloudflare ecosystem
- R2 bucket mounting via FUSE enables data persistence (added November 2025)
- Git operations support (added August 2025)
- Rich output: charts, tables, HTML, JSON, images

_Philosophy:_ Cloudflare takes a security-first approach using a "bindings" model where code has zero network access by default and can only access external APIs through explicitly defined bindings. This eliminates entire classes of security vulnerabilities by making capabilities explicitly opt-in.

_Unique Features:_

- _Edge-native execution_: Run sandboxes in 330+ global locations
- _Bindings model_: Zero network access by default; explicit opt-in for external APIs
- _R2 FUSE mounting_: S3-compatible storage mounting for persistence (R2, S3, GCS, Backblaze B2, MinIO)
- _Preview URLs_: Public URLs for exposing services from sandboxes
- _`keepAlive: true`_: Option for indefinite runtime

_Pricing (as of November 2025):_

| Resource       | Cost             | Included (Workers Paid) |
| -------------- | ---------------- | ----------------------- |
| Base Plan      | $5/month         | -                       |
| CPU            | $0.000020/vCPU-s | 375 vCPU-minutes        |
| Memory         | $0.0000025/GiB-s | 25 GiB-hours            |
| Disk           | $0.00000007/GB-s | 200 GB-hours            |
| Network Egress | $0.025-$0.05/GB  | Varies by region        |

_Instance Types (added October 2025):_

| Type       | vCPU | Memory  | Disk  |
| ---------- | ---- | ------- | ----- |
| lite       | 1/16 | 256 MiB | 2 GB  |
| basic      | 1/4  | 1 GiB   | 4 GB  |
| standard-1 | 1    | 3 GiB   | 5 GB  |
| standard-2 | 2    | 6 GiB   | 10 GB |
| standard-4 | 4    | 12 GiB  | 20 GB |

_Specs:_

| Spec           | Value                                   |
| -------------- | --------------------------------------- |
| Isolation      | Container                               |
| Cold Start     | 1-5 seconds                             |
| Edge Locations | 330+ global                             |
| Storage        | Ephemeral; persistent via R2 FUSE mount |
| Network        | Bindings model (zero access by default) |
| Max Memory     | 400 GiB concurrent (account limit)      |
| Max CPU        | 100 vCPU concurrent (account limit)     |
| Max Disk       | 2 TB concurrent                         |
| Image Storage  | 50 GB per account                       |

_Limitations:_

- Cold starts 1-5 seconds (slower than Workers' milliseconds)
- Binary network controls without bindings
- Bucket mounting only works with `wrangler deploy`, not `wrangler dev`
- SDK/container version must match
- Sandbox ID case sensitivity issues with preview URLs
- Still in open beta; ecosystem maturing

_Links:_

- Official: https://sandbox.cloudflare.com/
- SDK Documentation: https://developers.cloudflare.com/sandbox/
- Containers Pricing: https://developers.cloudflare.com/containers/pricing/
- Container Limits: https://developers.cloudflare.com/containers/platform-details/limits/
- Persistent Storage Tutorial: https://developers.cloudflare.com/sandbox/tutorials/persistent-vault/
- GitHub SDK: https://github.com/cloudflare/sandbox-sdk

---

## Comparison Table

| Feature          | Sprites             | E2B                 | Modal                | Cloudflare         |
| ---------------- | ------------------- | ------------------- | -------------------- | ------------------ |
| Setup            | Easy                | Very Easy           | Easy                 | Easy               |
| Free Tier        | $30 credit          | $100 credit         | $30/month            | $5/mo Workers Paid |
| Isolation        | Firecracker microVM | Firecracker microVM | gVisor container     | Container          |
| Cold Start       | <1 second           | ~150ms              | 2-5s (or <3s w/snap) | 1-5 seconds        |
| Max Timeout      | None (persistent)   | 24 hours (Pro)      | 24 hours             | Configurable       |
| Claude CLI       | Pre-installed       | Prebuilt template   | Manual               | Manual             |
| Git Support      | Yes                 | Yes                 | Yes                  | Yes                |
| Persistent Files | Yes (permanent)     | 24 hours            | Via Volumes          | Via R2 FUSE mount  |
| Checkpoints      | Yes (~300ms)        | Pause/Resume (Beta) | Memory Snapshots     | No                 |
| Network Controls | Layer 3 policies    | Allow/deny lists    | CIDR allowlists      | Bindings model     |
| Edge Locations   | Fly.io regions      | -                   | -                    | 330+ global        |
| Max Concurrent   | 10 active (base)    | Plan-based          | 10,000+              | Plan-based         |
| Self-Hosting     | Fly.io only         | Experimental        | No                   | No                 |
| MCP Tools        | -                   | 200+ (Docker)       | -                    | -                  |
| Best For         | Long-running agents | AI agent loops      | Python ML workloads  | Edge apps          |

---

## Other Options

### Daytona

Founded by the creators of Codeanywhere (2009), pivoted in February 2025 from development environments to AI code execution infrastructure. 35,000+ GitHub stars (AGPL-3.0 license).

_Key Features:_

- Sub-90ms sandbox creation (container-based, faster than E2B's ~150ms microVM)
- Python SDK (`daytona_sdk` on PyPI) and TypeScript SDK
- Official LangChain integration (`langchain-daytona-data-analysis`)
- MCP Server support for Claude/Anthropic integrations
- OCI/Docker image compatibility
- Built-in Git and LSP support
- GPU support for ML workloads (enterprise tier)
- Unlimited persistence (sandboxes can live forever via object storage archiving)
- Virtual desktops (Linux, Windows, macOS with programmatic control)

_Philosophy:_ Daytona believes AI will automate the majority of programming tasks. Their agent-agnostic architecture enables parallel sandboxed environments for testing solutions simultaneously without affecting the developer's primary workspace.

_Unique Features:_

- _Fastest cold start_: ~90ms (container-based, faster than E2B's microVM)
- _LangChain integration_: Official `langchain-daytona-data-analysis` package
- _MCP Server_: Native Claude/Anthropic integration support
- _Virtual desktops_: Linux, Windows, macOS with programmatic control
- _Unlimited persistence_: Sandboxes can live forever via object storage archiving

_Pricing:_

| Item            | Cost                                          |
| --------------- | --------------------------------------------- |
| Free Credits    | $200 (requires credit card)                   |
| Startup Program | Up to $50k in credits                         |
| Small Sandbox   | ~$0.067/hour (1 vCPU, 1 GiB RAM)              |
| Billing         | Pay-per-second; stopped/archived minimal cost |

_Specs:_

| Spec       | Default     | Maximum              |
| ---------- | ----------- | -------------------- |
| vCPU       | 1           | 4 (contact for more) |
| RAM        | 1 GB        | 8 GB                 |
| Disk       | 3 GiB       | 10 GB                |
| Auto-stop  | 15 min idle | Disabled             |
| Cold start | ~90ms       | -                    |
| Isolation  | Docker/OCI  | Kata/Sysbox optional |

_Network Egress Tiers:_

- Tier 1 & 2: Restricted network access
- Tier 3 & 4: Full internet with custom CIDR rules
- All tiers whitelist essential services (NPM, PyPI, GitHub, Anthropic/OpenAI APIs, etc.)

_Limitations:_

- Container isolation by default (not microVM like E2B)
- Cannot snapshot running sandboxes
- Long-session stability still maturing
- Young ecosystem compared to E2B
- Requires credit card for free credits

_Daytona vs E2B:_

| Aspect           | Daytona            | E2B                 |
| ---------------- | ------------------ | ------------------- |
| Isolation        | Docker containers  | Firecracker microVM |
| Cold start       | ~90ms              | ~150ms              |
| Free credits     | $200 (CC required) | $100 (no CC)        |
| Max session      | Unlimited          | 24 hours (Pro)      |
| GitHub stars     | 35k+               | 10k+                |
| Network controls | Tier-based         | Allow/deny lists    |

_Links:_

- Official: https://www.daytona.io/
- Documentation: https://www.daytona.io/brain/knowledge/docs_legacy/en/
- GitHub: https://github.com/daytonaio/daytona
- Python SDK: https://pypi.org/project/daytona_sdk/
- Network Limits: https://www.daytona.io/brain/knowledge/docs_legacy/en/network-limits/
- Sandbox Management: https://www.daytona.io/brain/knowledge/docs_legacy/en/sandbox-management/
- LangChain Integration: https://docs.langchain.com/oss/python/integrations/tools/daytona_data_analysis
- MCP Servers Guide: https://www.daytona.io/dotfiles/production-ready-mcp-servers-at-scale-with-claude-daytona

---

### Google Cloud Run

Google Cloud's serverless container platform with strong security isolation, designed for production workloads at scale.

_Key Features:_

- Two-layer sandbox isolation (hardware + kernel)
- Automatic scaling (including scale-to-zero)
- Pay-per-second billing (100ms granularity)
- NVIDIA L4 GPU support for AI inference (24 GB VRAM)
- Direct VPC egress with firewall controls
- Cloud Storage and NFS volume mounts for persistence
- Request timeout up to 60 minutes (services), 7 days (jobs)
- Up to 1000 concurrent requests per instance
- Built-in HTTPS, IAM, Secret Manager integration
- Source-based deployment (no Dockerfile required)

_Philosophy:_ Google's approach treats Cloud Run as the "easy button" for serverless containers. Unlike dedicated AI sandbox providers, Cloud Run is a general-purpose platform that happens to work well for AI agents. The security model provides defense-in-depth through gVisor (1st gen) or Linux microVMs (2nd gen), with seccomp filtering in both. For AI-specific workloads, Google offers Agent Engine (fully managed) and GKE Agent Sandbox (Kubernetes-native) as alternatives.

_Unique Features:_

- _Dual execution environments_: 1st gen (gVisor-based, smaller attack surface) or 2nd gen (Linux microVM, more compatibility)
- _GPU scale-to-zero_: L4 GPUs spin down when idle, eliminating GPU idle costs
- _Startup CPU Boost_: Temporarily increases CPU during cold start (up to 50% faster startups for Java)
- _VPC Flow Logs_: Full visibility into network traffic for compliance
- _Network tags_: Granular firewall rules via VPC network tags on revisions
- _Volume mounts_: Cloud Storage FUSE or NFS (Cloud Filestore) for persistent data

_Pricing (Tier 1 regions, e.g., us-central1):_

| Resource | On-Demand             | Free Tier (Monthly)                  |
| -------- | --------------------- | ------------------------------------ |
| CPU      | $0.000024/vCPU-second | 180,000 vCPU-seconds (~50 hrs)       |
| Memory   | $0.0000025/GiB-second | 360,000 GiB-seconds (~100 hrs @ 1GB) |
| Requests | $0.40/million         | 2 million                            |
| GPU (L4) | ~$0.67/hour           | None                                 |

- Always-on billing is ~30% cheaper than on-demand
- Tier 2 regions (Asia, South America) are ~40% more expensive
- GPU requires minimum 4 vCPU + 16 GiB memory
- New customers: $300 free credits for 90 days

_Specs:_

| Spec            | Value                                                                  |
| --------------- | ---------------------------------------------------------------------- |
| Isolation       | Two-layer: hardware (x86 virtualization) + kernel (gVisor/microVM)     |
| Cold Start      | 2-5 seconds typical; sub-second with Startup CPU Boost + min instances |
| Max Timeout     | 60 minutes (services), 168 hours/7 days (jobs)                         |
| Max Memory      | 32 GiB                                                                 |
| Max CPU         | 8 vCPU (or 4 vCPU with GPU)                                            |
| Max Concurrency | 1000 requests/instance (default 80)                                    |
| Max Instances   | 1000 (configurable)                                                    |
| GPU             | NVIDIA L4 (24 GB VRAM), 1 per instance, <5s startup                    |
| Storage         | Ephemeral; use Cloud Storage or NFS mounts for persistence             |

_Network/Egress Controls:_

- Direct VPC egress without Serverless VPC Access connector
- Network tags on service revisions for firewall rules
- VPC Service Controls for data exfiltration prevention
- Organization policies to enforce VPC-only egress
- Cloud NAT supported for outbound IP control
- VPC Flow Logs for traffic visibility

_Limitations:_

- No persistent local disk (must use Cloud Storage or NFS volume mounts)
- Cold start latency higher than E2B/Sprites (2-5s vs <1s) without pre-warming
- Setup complexity: Requires GCP project, billing, IAM configuration
- VPC complexity: Network egress controls require VPC setup
- Job connection breaks: Jobs >1 hour may experience connection breaks during maintenance
- GPU regions limited: L4 GPUs only available in select regions
- No pre-built AI agent template (unlike E2B)
- Memory/session management must be built manually

_Google Cloud AI Agent Options Comparison:_

| Criteria               | Cloud Run                    | Agent Engine     | GKE Agent Sandbox       |
| ---------------------- | ---------------------------- | ---------------- | ----------------------- |
| Setup Complexity       | Medium                       | Low              | High                    |
| Infrastructure Control | Medium                       | Low              | High                    |
| Memory/Session Mgmt    | Manual                       | Built-in         | Manual                  |
| Isolation              | gVisor/microVM               | Built-in sandbox | gVisor + Kata           |
| Cold Start             | 2-5s (sub-second w/pre-warm) | Sub-second       | Sub-second (warm pools) |
| Best For               | Flexible serverless          | Fastest to prod  | Enterprise scale        |

_SDK/API Options:_

- Python: `pip install google-cloud-run`
- Node.js: `npm install @google-cloud/run`
- Go, Java, .NET, Ruby, PHP, Rust client libraries available
- REST API and gcloud CLI
- Terraform provider for IaC

_Links:_

- Documentation: https://cloud.google.com/run/docs
- AI Agents Guide: https://cloud.google.com/run/brain/knowledge/docs_legacy/ai-agents
- Pricing: https://cloud.google.com/run/pricing
- Security Design: https://cloud.google.com/run/brain/knowledge/docs_legacy/securing/security
- Quotas & Limits: https://cloud.google.com/run/quotas
- GPU Support: https://cloud.google.com/run/brain/knowledge/docs_legacy/configuring/services/gpu
- VPC Egress: https://cloud.google.com/run/brain/knowledge/docs_legacy/configuring/vpc-direct-vpc
- Volume Mounts: https://cloud.google.com/run/brain/knowledge/docs_legacy/configuring/services/cloud-storage-volume-mounts
- Python SDK: https://pypi.org/project/google-cloud-run/
- Quickstarts: https://cloud.google.com/run/brain/knowledge/docs_legacy/quickstarts

---

### Replit

Full development environment with built-in LLM agent (Agent 3).

_Key Features:_

- Agent 3 can run autonomously for up to 200 minutes without supervision
- Self-testing loop: executes code, identifies errors, fixes, and reruns until tests pass
- Proprietary testing system claimed to be 3x faster and 10x more cost-effective than Computer Use models
- Can build other agents and automations from natural language descriptions
- Built on 10+ years of infrastructure investment (custom file system, VM orchestration)

_Philosophy:_ Replit positions as an "agent-first" platform focused on eliminating "accidental complexity" (per CEO Amjad Masad). Target audience: anyone who wants to build software, not just engineers. The goal is to make Agent the primary interface for software creation.

_Unique Features:_

- _Agent 3 autonomy_: Up to 200 minutes of autonomous execution
- _Self-testing loop_: Automatic error detection and fixing
- _Agent building_: Can create other agents from natural language
- _Full IDE integration_: Complete development environment, not just sandbox
- _MCP support_: Integration guide available

_Pricing:_

| Plan       | Monthly  | Agent Access        | Compute           | Storage |
| ---------- | -------- | ------------------- | ----------------- | ------- |
| Starter    | Free     | Limited (daily cap) | 1 vCPU, 2 GiB RAM | 2 GiB   |
| Core       | $25      | Full Agent 3        | 4 vCPU, 8 GiB RAM | 50 GiB  |
| Teams      | $40/user | Full Agent 3 + RBAC | 4 vCPU, 8 GiB RAM | 50 GiB  |
| Enterprise | Custom   | Full + SSO/SAML     | Custom            | Custom  |

- Core plan includes $25/month in AI credits
- Teams plan includes $40/month in credits + 50 viewer seats
- Annual billing: ~20% discount

_Specs:_

| Spec       | Starter      | Core/Teams    |
| ---------- | ------------ | ------------- |
| vCPU       | 1            | 4             |
| RAM        | 2 GiB        | 8 GiB         |
| Storage    | 2 GiB        | 50 GiB        |
| Agent Time | Daily limits | Up to 200 min |

_Limitations:_

- **No public API for programmatic Agent access** — designed exclusively for in-browser interactive use, not for CI/CD pipelines or external autonomous agent orchestration
- Agent frequently gets stuck in loops on simple tasks
- Over-autonomy risk (can override user intent)
- External API authentication problems reported
- Unpredictable credit consumption ($100-300/month reported overages)
- Over 60% of developers report agent stalls/errors regularly (per surveys)
- Notable July 2025 incident where Agent deleted a production database

_Links:_

- Official: https://replit.com/
- Pricing: https://replit.com/pricing
- Agent 3 Announcement: https://blog.replit.com/introducing-agent-3-our-most-autonomous-agent-yet
- 2025 Year in Review: https://blog.replit.com/2025-replit-in-review
- AI Billing Docs: https://docs.replit.com/billing/ai-billing
- MCP Integration Guide: https://docs.replit.com/tutorials/mcp-in-3
- Fast Mode Docs: https://docs.replit.com/replitai/fast-mode

---

## Local Docker Options

### Docker Official Sandboxes

_Quick Start:_

```bash
docker sandbox run claude                  # Basic
docker sandbox run -w ~/my-project claude  # Custom workspace
docker sandbox run claude "your task"      # With prompt
docker sandbox run claude -c               # Continue last session
```

_Key Details:_

- Credentials stored in persistent volume `docker-claude-sandbox-data`
- `--dangerously-skip-permissions` enabled by default
- Base image includes: Node.js, Python 3, Go, Git, Docker CLI, GitHub CLI, ripgrep, jq
- Container persists in background; re-running reuses same container
- Non-root user with sudo access

_Links:_ https://docs.docker.com/ai/sandboxes/claude-code/

---

## Comparison: E2B vs Docker Local

| Aspect            | E2B (Cloud)         | Docker Local           |
| ----------------- | ------------------- | ---------------------- |
| Setup             | SDK call            | `docker sandbox run`   |
| Isolation         | Firecracker microVM | Container              |
| Cost              | ~$0.05/hr           | Free (your hardware)   |
| Max Duration      | 24 hours            | Unlimited              |
| Network           | Full internet       | Full internet          |
| State Persistence | Session-based       | Volume-based           |
| Multi-tenant Safe | Yes                 | No (local only)        |
| Best For          | Production, CI/CD   | Local dev, prototyping |

---

## Recommendation for This Project

### For Production/Multi-tenant: Use E2B

1. Pre-built Claude Code template = zero setup friction
2. 24-hour sessions handle long-running autonomous agents
3. Full filesystem for progress.txt, prd.json, git repos
4. Proven in production (Lovable, Quora use it)
5. True isolation (Firecracker microVM)
6. 200+ MCP tools via Docker partnership

### For Long-Running Persistent Agents: Use Sprites

1. No session time limits (persistent environments)
2. Transactional snapshots for version control of entire OS
3. Auto-sleep when idle reduces costs
4. Pre-installed Claude Code and AI CLI tools
5. Best for agents that need to maintain state across days/weeks

### For Local Development: Use Docker Sandboxes

1. _Quick prototyping_: `docker sandbox run claude`
2. _With git automation_: `claude-sandbox` (TextCortex)
3. _Minimal setup_: Uses persistent credentials volume
4. Free - runs on your own hardware
5. Unlimited session duration
```

