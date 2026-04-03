---
id: claude-code-voice-hooks-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:03.236052
---

# KNOWLEDGE EXTRACT: claude-code-voice-hooks
> **Extracted on:** 2026-03-30 13:19:56
> **Source:** claude-code-voice-hooks

---

## File: `.gitignore`
```
.env
```

## File: `.mcp.json`
```json
{
  "mcpServers": {
    "elicit": {
      "command": "npx",
      "args": ["-y", "@blizzy/mcp-elicit"]
    }
  }
}
```

## File: `CLAUDE.md`
```markdown
# Claude Code Hooks

Sound notification system for all 26 Claude Code hooks. Plays sound effects when hook events fire.

## Project Structure

```
.claude/
  settings.json
  hooks/
    scripts/hooks.py
    config/hooks-config.json
    sounds/<hookname>/
    HOOKS-README.md
  agents/
    workflows/workflow-changelog-agent.md
    claude-code-test-agent.md
  commands/workflows/
    workflow-changelog.md
    workflow-add-hook.md
install/
  settings-mac.json
  settings-linux.json
  settings-windows.json
presentation/index.html
changelog/
  changelog.md
  verification-checklist.md
```

## Critical: Hook Count Consistency

The hook count (currently **26**) MUST match across ALL of these locations:
- `.claude/settings.json` hook entries
- `install/settings-mac.json`, `settings-linux.json`, `settings-windows.json`
- `hooks.py` HOOK_SOUND_MAP keys + docstring count
- `hooks-config.json` toggle count
- `HOOKS-README.md` heading + numbered list
- `README.md` badge + changelog table
- `presentation/index.html` (slides 2, 3, TOC, totalSlides)
- `claude-code-test-agent.md` frontmatter + body
- `demo/.claude/settings.json` hook entries
- `demo/.claude/hooks/scripts/demo-hooks.py` HOOK_SOUND_MAP + docstring
- `demo/hooks-lifecycle.html` flowchart SVG + prompt cards + branding count

When adding a hook, use `/workflows:workflow-add-hook` — it updates all 14 files.

## Agent Hooks

Only **6 of 26** hooks fire in agent sessions: PreToolUse, PostToolUse, PermissionRequest, PostToolUseFailure, Stop, SubagentStop. These are mapped in `AGENT_HOOK_SOUND_MAP` in hooks.py.

## Workflows

- `/workflows:workflow-changelog [N]` — Check last N versions for drift. Launches 2 agents in parallel, runs verification checklist, appends to changelog.md
- `/workflows:workflow-add-hook <HookName>` — Add a new hook across all files (sounds, config, settings, scripts, docs, presentation)
- `/commit` — Auto-generate commit message with timestamp and change count

## Conventions

- Hook names are **PascalCase** everywhere (e.g. `PreToolUse`, `InstructionsLoaded`)
- Sound folder names are **lowercase** (e.g. `pretooluse`, `instructionsloaded`)
- Settings files: timeout 5000 for all hooks except Setup (30000)
- `once: true` only on: PreCompact, SessionStart, SessionEnd
- `async: true` on all hooks
- Changelog entries use PKT timezone: `TZ=Asia/Karachi date`
- Version badge format: `v2.X.X | Mon DD, YYYY HH:MM AM/PM PKT`

## Memory

Persistent memory file: `~/.claude/projects/-Users-shayanraees-Documents-Github-claude-code-hooks/memory/MEMORY.md`

## Schema Note

`.claude/settings.json` is validated against Claude Code's bundled JSON schema. The schema's `propertyNames` enum may contain hidden/undocumented hooks not yet in the changelog. The workflow-changelog agent checks for these. As of v2.1.87, the schema has 26 hooks (all implemented in repo).
```

## File: `README.md`
```markdown
# Claude Code Hooks
[![Hooks](https://img.shields.io/badge/supports%20all-26%20hooks-white?style=flat&labelColor=555)](https://github.com/shanraisshan/claude-code-hooks/blob/main/.claude/hooks/HOOKS-README.md#hook-events-overview---official-26-hooks) [![Version](https://img.shields.io/badge/updated%20with%20Claude%20Code-v2.1.87%20(Mar%2029%2C%202026%207:47%20PM%20PKT)-white?style=flat&labelColor=555)](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) [![Stars](https://img.shields.io/github/stars/shanraisshan/claude-code-hooks?style=flat&label=%E2%98%85&labelColor=555&color=white)](https://github.com/shanraisshan/claude-code-hooks)

<p align="center">
  <img src="!/claude-speaking.svg" alt="Claude Code mascot speaking" width="168" height="108">
</p>

<p align="center">
  <img src="!/repo-description.svg" alt="Mouse click on PreToolUse, Keyboard on PostToolUse, Human voice on other hooks" height="56">
</p>

# [Demo Video + Presentation](https://youtu.be/6_y3AtkgjqA)

<p>
  <a href="https://youtu.be/6_y3AtkgjqA"><img src="!/pill-youtube-red.svg" alt="YouTube" height="36"></a>&nbsp;
  <a href="presentation/index.html"><img src="!/pill-slides.svg" alt="Slides" height="36"></a>
</p>

[![thumbnail](!/thumbnail/thumbnail3.jpg)](https://youtu.be/6_y3AtkgjqA)

## Installation

<p>
  <a href="install/README-mac.md"><img src="!/pill-mac.svg" alt="Mac" height="36"></a>&nbsp;
  <a href="install/README-linux.md"><img src="!/pill-linux.svg" alt="Linux" height="36"></a>&nbsp;
  <a href="install/README-windows.md"><img src="!/pill-windows.svg" alt="Windows" height="36"></a>
</p>

![How to Use](!/how-to-use.svg)

**Step 1.** Start Claude Code:
```bash
claude
```

**Step 2.** Send a prompt (e.g., `Hi`) — you'll hear a sound on session start, tool use, agent response, and more.

## Common Errors

If you don't follow the prerequisites, you will see the following error on claude code start

```
SessionStart:startup hook error
```

## Changelog
new hook addition changelogs only

| Date | Hooks | Changes | Claude Code Version | Demo |
|------|:-----:|---------|:-------------------:|:----:|
| Mar 26, 2026 | 26 | Added `TaskCreated` | [v2.1.84](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2184) | [Demo 4](https://youtu.be/MnpOsTEDzeY) |
| Mar 25, 2026 | 25 | Added `CwdChanged`, `FileChanged` | [v2.1.83](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2183) | |
| Mar 18, 2026 | 23 | Added `StopFailure` | [v2.1.78](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2178) | |
| Mar 14, 2026 | 22 | Added `PostCompact`, `Elicitation`, `ElicitationResult` | [v2.1.76](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2176) | |
| Mar 5, 2026 | 19 | Added `InstructionsLoaded` | [v2.1.69](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2169) | |
| Feb 21, 2026 | 18 | Added `WorktreeCreate` and `WorktreeRemove` | [v2.1.50](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2150) | |
| Feb 20, 2026 | 16 | Added `ConfigChange` | [v2.1.49](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2149) | |
| Feb 6, 2026 | 15 | Added `TeammateIdle` and `TaskCompleted` | [v2.1.33](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2133) | |
| — | 13 | Added `PostToolUseFailure` | — | [Demo 3](https://youtu.be/6_y3AtkgjqA) |
| Jan 17, 2026 | 12 | Added `Setup` | [v2.1.10](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2110) | |
| Jan 7, 2026 | 12 | Added subagent hooks: `PreToolUse`, `PostToolUse`, `Stop` | [v2.1.0](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#210) | |
| Nov 18, 2025 | 11 | Added `PermissionRequest` | [v2.0.45](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2045) | [Demo 2](https://youtu.be/JFPJtMNV8Qw) |
| Nov 17, 2025 | 10 | Added `SubagentStart` | [v2.0.43](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2043) | |
| Nov 10, 2025 | 9 | Added `Notification` | [v2.0.37](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2037) | [Demo 1](https://youtu.be/vgfdSUbz_b0) |
| Jul 28, 2025 | 8 | Added `SessionStart` | [v1.0.62](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#1062) | |
| Jul 16, 2025 | 7 | Added `UserPromptSubmit` | [v1.0.54](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#1054) | |
| Jul 10, 2025 | 6 | Added `PreCompact` | [v1.0.48](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#1048) | |
| Jul 2, 2025 | 5 | Split `Stop` into `Stop` and `SubagentStop` | [v1.0.41](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#1041) | |
| Jun 30, 2025 | 4 | Initial release: `PreToolUse`, `PostToolUse`, `Stop`, `SessionEnd` | [v1.0.38](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#1038) | |

### [Not in Official Docs](../claude_bp_repo/HOOKS-README.md#not-in-official-docs)

## Links

<p>
  <a href="https://www.youtube.com/watch?v=vgfdSUbz_b0"><img src="!/pill-youtube.svg" alt="YouTube" height="36"></a>&nbsp;
  <a href="https://www.linkedin.com/posts/shanraisshan_claudecode-aicoding-voicehooks-activity-7393305703697805312-4gl0"><img src="!/pill-linkedin.svg" alt="LinkedIn" height="36"></a>&nbsp;
  <a href="https://www.reddit.com/r/ClaudeCode/comments/1otaf7f/i_just_made_claude_code_speak_using_hooks/"><img src="!/pill-reddit.svg" alt="Reddit" height="36"></a>&nbsp;
  <a href="https://x.com/shanraisshan/status/1987817251966513620"><img src="!/pill-x.svg" alt="X" height="36"></a>&nbsp;
  <a href="https://medium.com/@shanraisshan/claude-code-just-got-a-voice-%25EF%25B8%258F-51008157305b"><img src="!/pill-medium.svg" alt="Medium" height="36"></a>
</p>

## Other Repos

<a href="https://github.com/shanraisshan/codex-cli-hooks"><img src="!/codex-speaking.svg" alt="Codex CLI Hooks" width="40" height="40" align="center"></a> <a href="https://github.com/shanraisshan/codex-cli-hooks"><strong>codex-cli-hooks</strong></a> · <a href="https://github.com/shanraisshan/claude-code-best-practice"><img src="!/claude-jumping.svg" alt="Claude Code Best Practice" width="40" height="40" align="center"></a> <a href="https://github.com/shanraisshan/claude-code-best-practice"><strong>claude-code-best-practice</strong></a> · <a href="https://github.com/shanraisshan/codex-cli-best-practice"><img src="!/codex-jumping.svg" alt="Codex CLI Best Practice" width="40" height="40" align="center"></a> <a href="https://github.com/shanraisshan/codex-cli-best-practice"><strong>codex-cli-best-practice</strong></a>

## Developed by

[![Developed by Claude Code](!/developed-by-claude-code.svg)](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/claude-code)

| Workflow | Description |
|---------|-------------|
| /workflows:workflow-changelog | Scan for new hooks and drift across all files |
| /workflows:workflow-add-hook <HookName>* | Add any recommended hook across all files in one command |

```

## File: `!/thumbnail/hook-lifecycle-explained.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hook Lifecycle Explained - Thumbnail</title>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html, body { height: 100%; overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        body { display: flex; height: 100vh; background: #0d1117; }

        /* === LEFT PANEL (dark) === */
        .left-panel {
            width: 45%;
            background: #ffffff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 40px 30px;
            padding-bottom: 140px;
            gap: 16px;
        }
        .header-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
        }
        .mascot svg { width: 160px; height: 100px; }
        .pixel-title {
            font-family: 'Press Start 2P', monospace;
            font-size: 2.6rem;
            color: #E07C4C;
            text-align: left;
            line-height: 1.5;
        }
        .heading {
            font-size: 2.8rem;
            font-weight: 700;
            text-align: center;
            white-space: nowrap;
            color: #1a1a1a;
            background: linear-gradient(90deg, #1a1a1a 0%, #1a1a1a 40%, #FFD700 50%, #1a1a1a 60%, #1a1a1a 100%);
            background-size: 300% 100%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer 3s ease-in-out infinite;
        }
        @keyframes shimmer {
            0% { background-position: 100% 0; }
            100% { background-position: -100% 0; }
        }
        .footer {
            font-size: 1rem;
            color: #888;
            text-align: center;
            margin-top: 8px;
        }

        /* === RIGHT PANEL === */
        .right-panel {
            width: 55%;
            background: #0d1117;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 10px;
            border-left: 1px solid #30363d;
        }
        .right-panel svg.flowchart { height: 96%; width: auto; max-width: 100%; }

        /* Flowchart styles (all-yellow) */
        .hook-rect { fill: #FFD700; stroke: #FFA500; stroke-width: 1.5; }
        .hook-rect-stop { fill: #FFD700; stroke: #FFA500; }
        .hook-rect-side { stroke-dasharray: 5 3; }
        .hook-text { fill: #1a1a1a; font-family: system-ui, sans-serif; font-size: 12px; font-weight: 600; }
        .hook-text-side { font-size: 10px; }
        .hook-subtitle { fill: #1a1a1a; font-family: system-ui, sans-serif; font-size: 8px; }
        .tool-rect { fill: #0d2137; stroke: #1f4a6e; stroke-width: 1.5; }
        .tool-text { fill: #58a6d4; font-family: system-ui, sans-serif; font-size: 12px; font-weight: 600; }
        .loop-rect { fill: none; stroke: #8b6914; stroke-width: 1.5; stroke-dasharray: 6 4; }
        .loop-label { fill: #8b6914; font-family: system-ui, sans-serif; font-size: 10px; font-weight: 700; }
        .arrow-line { stroke: #30363d; stroke-width: 1.5; fill: none; }
        .arrow-head { fill: #30363d; }
        .arrow-dashed { stroke-dasharray: 5 3; }
        .resume-label { fill: #484f58; font-family: system-ui, sans-serif; font-size: 9px; font-style: italic; }
        .connector-dashed { stroke: #30363d; stroke-width: 1; stroke-dasharray: 4 3; fill: none; }

        /* Mascot animations */
        .cb{animation:b .8s ease-in-out infinite;transform-origin:center bottom}
        .sh{animation:sp .8s ease-in-out infinite}
        .mo{animation:tk .3s ease-in-out infinite;transform-origin:center center}
        .le{animation:el .8s ease-in-out infinite;transform-origin:center bottom}
        .re{animation:er .8s ease-in-out infinite;transform-origin:center bottom}
        .w1{animation:we .8s ease-out infinite;transform-origin:left center}
        .w2{animation:we .8s ease-out infinite .2s;transform-origin:left center}
        .w3{animation:we .8s ease-out infinite .4s;transform-origin:left center}
        .n1{animation:f1 1.5s ease-out infinite}
        .n2{animation:f2 1.5s ease-out infinite .3s}
        .n3{animation:f3 1.5s ease-out infinite .6s}
        @keyframes b{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}
        @keyframes sp{0%,100%{transform:scaleX(1);opacity:.25}50%{transform:scaleX(.9);opacity:.2}}
        @keyframes tk{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.5)}}
        @keyframes el{0%,100%{transform:rotate(0)}50%{transform:rotate(-5deg)}}
        @keyframes er{0%,100%{transform:rotate(0)}50%{transform:rotate(5deg)}}
        @keyframes we{0%{opacity:.8;transform:scaleX(.3) scaleY(.8)}100%{opacity:0;transform:scaleX(1.2) scaleY(1)}}
        @keyframes f1{0%{opacity:1;transform:translate(0,0) rotate(0)}100%{opacity:0;transform:translate(15px,-25px) rotate(15deg)}}
        @keyframes f2{0%{opacity:1;transform:translate(0,0) rotate(0)}100%{opacity:0;transform:translate(20px,-30px) rotate(-10deg)}}
        @keyframes f3{0%{opacity:1;transform:translate(0,0) rotate(0)}100%{opacity:0;transform:translate(10px,-35px) rotate(20deg)}}
    </style>
</head>
<body>

<!-- LEFT PANEL: Mascot + Title + Heading + Version -->
<div class="left-panel">
    <div class="header-row">
        <div class="mascot">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 90">
                <ellipse class="sh" cx="50" cy="82" rx="22" ry="5" fill="#000"/>
                <g class="w1"><path d="M92 44Q100 44 100 52Q100 60 92 60" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
                <g class="w2"><path d="M96 38Q108 38 108 52Q108 66 96 66" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
                <g class="w3"><path d="M100 32Q116 32 116 52Q116 72 100 72" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
                <g class="n1"><ellipse cx="108" cy="28" rx="4" ry="3" fill="#E07C4C" transform="rotate(-20,108,28)"/><rect x="111" y="12" width="2" height="16" fill="#E07C4C"/><path d="M113 12Q118 14 118 18Q118 22 113 20" fill="#E07C4C"/></g>
                <g class="n2"><ellipse cx="122" cy="22" rx="4" ry="3" fill="#E07C4C" transform="rotate(-20,122,22)"/><rect x="125" y="6" width="2" height="16" fill="#E07C4C"/></g>
                <g class="n3"><ellipse cx="115" cy="42" rx="3" ry="2.5" fill="#E07C4C" transform="rotate(-20,115,42)"/><ellipse cx="125" cy="40" rx="3" ry="2.5" fill="#E07C4C" transform="rotate(-20,125,40)"/><rect x="117" y="26" width="2" height="16" fill="#E07C4C"/><rect x="127" y="24" width="2" height="16" fill="#E07C4C"/><rect x="117" y="26" width="12" height="2" fill="#E07C4C"/></g>
                <g class="cb">
                    <rect class="le" x="22" y="10" width="8" height="14" fill="#E07C4C"/>
                    <rect class="re" x="70" y="10" width="8" height="14" fill="#E07C4C"/>
                    <rect x="18" y="24" width="64" height="4" fill="#E07C4C"/>
                    <rect x="14" y="28" width="72" height="32" fill="#E07C4C"/>
                    <rect x="30" y="34" width="8" height="10" fill="#000"/>
                    <rect x="62" y="34" width="8" height="10" fill="#000"/>
                    <rect class="mo" x="44" y="50" width="12" height="6" fill="#000"/>
                    <rect x="2" y="40" width="12" height="8" fill="#E07C4C"/>
                    <rect x="86" y="40" width="12" height="8" fill="#E07C4C"/>
                    <rect x="24" y="60" width="12" height="14" fill="#E07C4C"/>
                    <rect x="64" y="60" width="12" height="14" fill="#E07C4C"/>
                </g>
            </svg>
        </div>
        <div class="pixel-title">CLAUDE<br>CODE</div>
    </div>
    <div class="heading">Hook Lifecycle Explained</div>
    <p class="footer">26 Hooks | As of Claude Code v2.1.87 | March 29, 2026</p>
</div>

<!-- RIGHT PANEL: All-yellow hooks flowchart -->
<div class="right-panel">
    <svg class="flowchart" viewBox="0 -32 520 552" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet">
        <defs>
            <marker id="ah" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto"><polygon points="0 0,6 2.5,0 5" class="arrow-head"/></marker>
        </defs>
        <g><rect class="hook-rect hook-rect-side" x="15" y="-27" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="-15" text-anchor="middle">InstructionsLoaded</text><text class="hook-subtitle" x="65" y="-5" text-anchor="middle">(Async)</text></g>
        <line class="connector-dashed" x1="65" y1="1" x2="65" y2="5"/>
        <g><rect class="hook-rect hook-rect-side" x="15" y="5" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="17" text-anchor="middle">Setup</text><text class="hook-subtitle" x="65" y="27" text-anchor="middle">(Init)</text></g>
        <line class="connector-dashed" x1="115" y1="19" x2="156" y2="19"/>
        <g><rect class="hook-rect" x="160" y="5" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="23" text-anchor="middle">SessionStart</text></g>
        <line class="arrow-line" x1="245" y1="33" x2="245" y2="41" marker-end="url(#ah)"/>
        <g><rect class="hook-rect" x="160" y="41" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="59" text-anchor="middle">UserPromptSubmit</text></g>
        <line class="arrow-line" x1="245" y1="69" x2="245" y2="105" marker-end="url(#ah)"/>
        <rect class="loop-rect" x="80" y="78" width="340" height="247" rx="6"/>
        <text class="loop-label" x="93" y="93">AGENTIC LOOP</text>
        <g><rect class="hook-rect" x="160" y="105" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="123" text-anchor="middle">PreToolUse</text></g>
        <line class="arrow-line" x1="245" y1="133" x2="245" y2="141" marker-end="url(#ah)"/>
        <g><rect class="hook-rect" x="160" y="141" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="159" text-anchor="middle">PermissionRequest</text></g>
        <line class="arrow-line" x1="245" y1="169" x2="245" y2="177" marker-end="url(#ah)"/>
        <g><rect class="tool-rect" x="170" y="179" width="150" height="20" rx="4"/><text class="tool-text" x="245" y="193" text-anchor="middle" style="font-size:10px">[tool executes]</text></g>
        <line class="arrow-line" x1="245" y1="199" x2="245" y2="213" marker-end="url(#ah)"/>
        <g><rect class="hook-rect hook-rect-side" x="15" y="150" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="162" text-anchor="middle">Elicitation</text><text class="hook-subtitle" x="65" y="172" text-anchor="middle">(MCP input)</text></g>
        <g><rect class="hook-rect hook-rect-side" x="15" y="180" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="192" text-anchor="middle">ElicitationResult</text><text class="hook-subtitle" x="65" y="202" text-anchor="middle">(MCP input)</text></g>
        <line class="connector-dashed" x1="115" y1="194" x2="156" y2="194"/>
        <g><rect class="hook-rect" x="120" y="213" width="250" height="28" rx="5"/><text class="hook-text" x="245" y="231" text-anchor="middle">PostToolUse / PostToolUseFailure</text></g>
        <line class="arrow-line" x1="245" y1="241" x2="245" y2="249" marker-end="url(#ah)"/>
        <g><rect class="hook-rect" x="125" y="249" width="240" height="28" rx="5"/><text class="hook-text" x="245" y="267" text-anchor="middle">SubagentStart / SubagentStop</text></g>
        <line class="arrow-line" x1="245" y1="277" x2="245" y2="285" marker-end="url(#ah)"/>
        <g><rect class="hook-rect hook-rect-side" x="395" y="270" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="445" y="282" text-anchor="middle">TaskCreated</text><text class="hook-subtitle" x="445" y="292" text-anchor="middle">(Teams)</text></g>
        <line class="connector-dashed" x1="330" y1="299" x2="395" y2="284"/>
        <g><rect class="hook-rect" x="160" y="285" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="303" text-anchor="middle">TaskCompleted</text></g>
        <path class="arrow-line" d="M 330,299 L 365,299 L 365,119 L 340,119"/><polygon points="340,115 330,119 340,123" class="arrow-head"/>
        <line class="arrow-line" x1="245" y1="313" x2="245" y2="335" marker-end="url(#ah)"/>
        <g><rect class="hook-rect hook-rect-stop" x="135" y="335" width="220" height="28" rx="5"/><text class="hook-text" x="245" y="353" text-anchor="middle">Stop / StopFailure</text></g>
        <line class="arrow-line" x1="245" y1="363" x2="245" y2="371" marker-end="url(#ah)"/>
        <g><rect class="hook-rect" x="160" y="371" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="389" text-anchor="middle">TeammateIdle</text></g>
        <line class="arrow-line" x1="245" y1="399" x2="245" y2="407" marker-end="url(#ah)"/>
        <g><rect class="hook-rect" x="160" y="407" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="425" text-anchor="middle">PreCompact</text></g>
        <line class="arrow-line" x1="245" y1="435" x2="245" y2="443" marker-end="url(#ah)"/>
        <g><rect class="hook-rect" x="160" y="443" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="461" text-anchor="middle">PostCompact</text></g>
        <line class="arrow-line" x1="245" y1="471" x2="245" y2="479" marker-end="url(#ah)"/>
        <g><rect class="hook-rect" x="160" y="479" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="497" text-anchor="middle">SessionEnd</text></g>
        <path class="arrow-line arrow-dashed" d="M 330,493 L 455,493 L 455,19 L 340,19"/><polygon points="340,15 330,19 340,23" class="arrow-head"/>
        <text class="resume-label" x="463" y="256" text-anchor="middle" transform="rotate(-90,463,256)">resumed sessions</text>
        <g><rect class="hook-rect hook-rect-side" x="15" y="305" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="317" text-anchor="middle">Notification</text><text class="hook-subtitle" x="65" y="327" text-anchor="middle">(Async)</text></g>
        <g><rect class="hook-rect hook-rect-side" x="15" y="335" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="347" text-anchor="middle">ConfigChange</text><text class="hook-subtitle" x="65" y="357" text-anchor="middle">(Async)</text></g>
        <g><rect class="hook-rect hook-rect-side" x="15" y="365" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="377" text-anchor="middle">WorktreeCreate</text><text class="hook-subtitle" x="65" y="387" text-anchor="middle">(Setup)</text></g>
        <g><rect class="hook-rect hook-rect-side" x="15" y="395" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="407" text-anchor="middle">WorktreeRemove</text><text class="hook-subtitle" x="65" y="417" text-anchor="middle">(Teardown)</text></g>
        <g><rect class="hook-rect hook-rect-side" x="15" y="425" width="100" height="40" rx="5"/><text class="hook-text hook-text-side" x="65" y="439" text-anchor="middle">CwdChanged</text><text class="hook-text hook-text-side" x="65" y="451" text-anchor="middle">FileChanged</text><text class="hook-subtitle" x="65" y="461" text-anchor="middle">(Env reactive)</text></g>
    </svg>
</div>

</body>
</html>
```

## File: `!/thumbnail/workflows-vs-no-workflows.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Workflows vs No Workflows</title>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: #ffffff;
            color: #1a1a1a;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            text-align: center;
            padding: 40px;
        }

        .header-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin-bottom: 40px;
        }

        .title-logo {
            width: 160px;
            height: 100px;
            flex-shrink: 0;
        }

        .title-logo svg {
            width: 100%;
            height: 100%;
        }

        .pixel-title {
            font-family: 'Press Start 2P', monospace;
            font-size: 2.8rem;
            color: #E07C4C;
            line-height: 1.4;
            text-align: left;
        }

        .subtitle {
            font-size: 3.5rem;
            color: #555;
            margin-bottom: 16px;
            font-weight: 600;
        }

        .project-line {
            font-size: 1.3rem;
            color: #666;
            margin-bottom: 50px;
            font-weight: 400;
        }

        .subtitle .workflows {
            display: inline-block;
            color: #16a34a;
            font-weight: 700;
            background: linear-gradient(90deg, #16a34a 0%, #4ade80 50%, #16a34a 100%);
            background-size: 200% 100%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer-seq 10s ease-in-out infinite;
        }

        .subtitle .no-workflows {
            display: inline-block;
            color: #dc2626;
            font-weight: 700;
            background: linear-gradient(90deg, #dc2626 0%, #f87171 50%, #dc2626 100%);
            background-size: 200% 100%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer-seq 10s ease-in-out infinite 5s;
        }

        .subtitle .label {
            display: block;
            font-size: 1.5rem;
            font-weight: 400;
            -webkit-text-fill-color: #16a34a;
            margin-top: 4px;
        }

        .subtitle .label-red {
            display: block;
            font-size: 1.5rem;
            font-weight: 400;
            -webkit-text-fill-color: #dc2626;
            margin-top: 4px;
        }

        .subtitle .vs-text {
            vertical-align: top;
        }

        @keyframes shimmer-seq {
            0% { background-position: 200% 0; }
            20% { background-position: -200% 0; }
            100% { background-position: -200% 0; }
        }

        .footer {
            margin-top: 60px;
            font-size: 0.95rem;
            color: #888;
        }
    </style>
</head>
<body>
    <div class="header-row">
    <div class="title-logo">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 90" width="160" height="100">
            <style>
                .tl-claude-body { animation: tl-bob 0.8s ease-in-out infinite; transform-origin: center bottom; }
                .tl-shadow { animation: tl-shadow-pulse 0.8s ease-in-out infinite; }
                .tl-mouth { animation: tl-talk 0.3s ease-in-out infinite; transform-origin: center center; }
                .tl-left-ear { animation: tl-ear-tilt-left 0.8s ease-in-out infinite; transform-origin: center bottom; }
                .tl-right-ear { animation: tl-ear-tilt-right 0.8s ease-in-out infinite; transform-origin: center bottom; }
                .tl-wave-1 { animation: tl-wave-expand 0.8s ease-out infinite; transform-origin: left center; }
                .tl-wave-2 { animation: tl-wave-expand 0.8s ease-out infinite 0.2s; transform-origin: left center; }
                .tl-wave-3 { animation: tl-wave-expand 0.8s ease-out infinite 0.4s; transform-origin: left center; }
                .tl-note-1 { animation: tl-float-note-1 1.5s ease-out infinite; }
                .tl-note-2 { animation: tl-float-note-2 1.5s ease-out infinite 0.3s; }
                .tl-note-3 { animation: tl-float-note-3 1.5s ease-out infinite 0.6s; }
                @keyframes tl-bob { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-3px); } }
                @keyframes tl-shadow-pulse { 0%, 100% { transform: scaleX(1); opacity: 0.25; } 50% { transform: scaleX(0.9); opacity: 0.2; } }
                @keyframes tl-talk { 0%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.5); } }
                @keyframes tl-ear-tilt-left { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(-5deg); } }
                @keyframes tl-ear-tilt-right { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(5deg); } }
                @keyframes tl-wave-expand { 0% { opacity: 0.8; transform: scaleX(0.3) scaleY(0.8); } 100% { opacity: 0; transform: scaleX(1.2) scaleY(1); } }
                @keyframes tl-float-note-1 { 0% { opacity: 1; transform: translate(0, 0) rotate(0deg); } 100% { opacity: 0; transform: translate(15px, -25px) rotate(15deg); } }
                @keyframes tl-float-note-2 { 0% { opacity: 1; transform: translate(0, 0) rotate(0deg); } 100% { opacity: 0; transform: translate(20px, -30px) rotate(-10deg); } }
                @keyframes tl-float-note-3 { 0% { opacity: 1; transform: translate(0, 0) rotate(0deg); } 100% { opacity: 0; transform: translate(10px, -35px) rotate(20deg); } }
            </style>
            <ellipse class="tl-shadow" cx="50" cy="82" rx="22" ry="5" fill="#000"/>
            <g class="tl-wave-1"><path d="M 92 44 Q 100 44, 100 52 Q 100 60, 92 60" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
            <g class="tl-wave-2"><path d="M 96 38 Q 108 38, 108 52 Q 108 66, 96 66" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
            <g class="tl-wave-3"><path d="M 100 32 Q 116 32, 116 52 Q 116 72, 100 72" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
            <g class="tl-note-1"><ellipse cx="108" cy="28" rx="4" ry="3" fill="#E07C4C" transform="rotate(-20, 108, 28)"/><rect x="111" y="12" width="2" height="16" fill="#E07C4C"/><path d="M 113 12 Q 118 14, 118 18 Q 118 22, 113 20" fill="#E07C4C"/></g>
            <g class="tl-note-2"><ellipse cx="122" cy="22" rx="4" ry="3" fill="#E07C4C" transform="rotate(-20, 122, 22)"/><rect x="125" y="6" width="2" height="16" fill="#E07C4C"/></g>
            <g class="tl-note-3"><ellipse cx="115" cy="42" rx="3" ry="2.5" fill="#E07C4C" transform="rotate(-20, 115, 42)"/><ellipse cx="125" cy="40" rx="3" ry="2.5" fill="#E07C4C" transform="rotate(-20, 125, 40)"/><rect x="117" y="26" width="2" height="16" fill="#E07C4C"/><rect x="127" y="24" width="2" height="16" fill="#E07C4C"/><rect x="117" y="26" width="12" height="2" fill="#E07C4C"/></g>
            <g class="tl-claude-body">
                <rect class="tl-left-ear" x="22" y="10" width="8" height="14" fill="#E07C4C"/>
                <rect class="tl-right-ear" x="70" y="10" width="8" height="14" fill="#E07C4C"/>
                <rect x="18" y="24" width="64" height="4" fill="#E07C4C"/>
                <rect x="14" y="28" width="72" height="32" fill="#E07C4C"/>
                <rect x="30" y="34" width="8" height="10" fill="#000000"/>
                <rect x="62" y="34" width="8" height="10" fill="#000000"/>
                <rect class="tl-mouth" x="44" y="50" width="12" height="6" fill="#000000"/>
                <rect x="2" y="40" width="12" height="8" fill="#E07C4C"/>
                <rect x="86" y="40" width="12" height="8" fill="#E07C4C"/>
                <rect x="24" y="60" width="12" height="14" fill="#E07C4C"/>
                <rect x="64" y="60" width="12" height="14" fill="#E07C4C"/>
            </g>
        </svg>
    </div>
    <div class="pixel-title">CLAUDE<br>CODE</div>
    </div>
    <p class="subtitle"><span class="workflows">WORKFLOWS<span class="label">(agentic engineering)</span></span> <span class="vs-text">vs</span> <span class="no-workflows">NO-WORKFLOWS<span class="label-red">(vibe coding)</span></span></p>
    <p class="project-line">Explained using live project <strong>Claude Code Hooks</strong></p>
    <p class="footer">As of Claude Code v2.1.83 | March 25, 2026</p>
</body>
</html>
```

## File: `changelog/changelog.md`
```markdown
# Workflow Changelog History

## Status Legend

| Status | Meaning |
|--------|---------|
| ✅ COMPLETE (reason) | Action was taken and resolved successfully |
| ❌ INVALID (reason) | Finding was incorrect, not applicable, or intentional |
| ✋ ON HOLD (reason) | Action deferred — waiting on external dependency or user decision |

---

## [2026-02-20 08:14 PM PKT] Claude Code v2.1.49

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Doc Fix | `agent_type` version attribution — README said v2.1.43, changelog disagrees | ✅ COMPLETE (marked as ~v2.1.43, unconfirmed) |
| 2 | MEDIUM | Agent Hook Docs | Agent frontmatter hooks — official docs say "all supported" vs repo's 6 | ✅ COMPLETE (added update note to HOOKS-README and README) |
| 3 | LOW | Hook Options Table | `notification_type`, `message`, `title` missing from Notification Options column | ✅ COMPLETE (added to HOOKS-README) |
| 4 | LOW | Hook Types/Env | Additional `CLAUDE_HOOK_*` env vars from blog sources | ❌ INVALID (false positive — not in official docs) |
| 5 | LOW | New Hook | `OpenInEditor` hook existence | ❌ INVALID (false positive — does not exist in official docs) |

---

## [2026-02-20 11:15 PM PKT] Claude Code v2.1.49

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Hook Options Table | UserPromptSubmit Options column missing `prompt` input field in HOOKS-README | ✅ COMPLETE (added `prompt` to Options column) |
| 2 | LOW | Agent Hook Docs | Agent frontmatter hooks — official docs say "all supported" vs repo's tested 6; needs re-testing | ✅ COMPLETE (reported upstream [#27153](https://github.com/anthropics/claude-code/issues/27153)) |

---

## [2026-02-20 11:57 PM PKT] Claude Code v2.1.49

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (already reported upstream [#27153](https://github.com/anthropics/claude-code/issues/27153); pending response) |

---

## [2026-02-21 06:41 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | /workflows:workflow-add-hook WorktreeCreate — new in v2.1.50 for agent worktree isolation VCS setup | ✅ COMPLETE (added — all 18 hooks consistent across files) |
| 2 | HIGH | New Hook | /workflows:workflow-add-hook WorktreeRemove — new in v2.1.50 for agent worktree isolation VCS teardown | ✅ COMPLETE (added — all 18 hooks consistent across files) |
| 3 | LOW | Hook Options Table | Add `tool_response` to PostToolUse Options column in HOOKS-README | ✅ COMPLETE (added to HOOKS-README) |
| 4 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream bug reported at [#27153](https://github.com/anthropics/claude-code/issues/27153); pending their fix) |

---

## [2026-02-21 07:57 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Presentation | Add can-block/cannot-block badge to WorktreeCreate and WorktreeRemove slides — all other 16 hook slides had this badge | ✅ COMPLETE (added "Cannot Block" badge to both slides) |
| 2 | LOW | Documentation | README.md changelog table missing v2.1.47 `last_assistant_message` — no action needed, table is for new hook additions only | ❌ INVALID (not applicable — editorial choice) |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream bug reported; pending their fix) |
| 4 | LOW | Presentation | Setup hook not shown in lifecycle diagram — fires separately via --init/--maintenance | ✅ COMPLETE (added Setup to lifecycle diagram with separate trigger section) |
| 5 | LOW | Workflow | Updated workflow-add-hook to require can-block badge on every new hook slide and update summary can-block list | ✅ COMPLETE (added explicit instructions to workflow) |

---

## [2026-02-21 08:13 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Documentation | Add `WorktreeCreate` and `WorktreeRemove` to "Not in Official Docs" table in HOOKS-README — they exist in changelog (v2.1.50) but are absent from official hooks reference | ✅ COMPLETE (added both rows to table) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open; tracked there) |
| 3 | LOW | Workflow | Updated workflow-add-hook to include "Not in Official Docs" table step when adding changelog-only hooks | ✅ COMPLETE (added instruction to HOOKS-README section) |

---

## [2026-02-21 09:10 AM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open; tracked there) |

---

## [2026-02-22 02:30 PM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Can-Block Fix | WorktreeCreate can-block status wrong in presentation — should be "Can Block" not "Cannot Block"; also missing from summary can-block list | ✅ COMPLETE (changed to "Can Block" + added to summary list) |
| 2 | HIGH | Doc Fix | HOOKS-README "Not in Official Docs" table stale — WorktreeCreate and WorktreeRemove ARE now in official docs (17 hooks listed, not 15) | ✅ COMPLETE (removed stale rows, updated count to 17) |
| 3 | MEDIUM | New Input Field | WorktreeCreate missing `name` input field in HOOKS-README Options column | ✅ COMPLETE (added `name` to Options column) |
| 4 | MEDIUM | New Input Field | WorktreeRemove missing `worktree_path` input field in HOOKS-README Options column | ✅ COMPLETE (added `worktree_path` to Options column) |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✅ COMPLETE (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open; tracked there) |

---

## [2026-02-23 01:08 PM PKT] Claude Code v2.1.50

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Documentation | HOOKS-README heading says "Official 18 Hooks" but only 17 are in official docs (Setup is unofficial) — heading wording misleading | ❌ INVALID (intentional wording) |
| 2 | MEDIUM | Matcher/Schema | HOOKS-README missing per-hook matcher values for SessionEnd, Notification, SubagentStart, SubagentStop, PreCompact, ConfigChange | ✅ COMPLETE (added Per-Hook Matcher Reference table) |
| 3 | LOW | Version Mismatch | TeammateIdle/TaskCompleted version — README says v2.1.33, CHANGELOG.md fetch suggests v2.1.45; needs verification | ✅ COMPLETE (v2.1.33 confirmed correct) |
| 4 | LOW | Documentation | Common input fields (session_id, transcript_path, cwd, permission_mode, hook_event_name) not in dedicated HOOKS-README section | ✅ COMPLETE (added Common Input Fields section) |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-24 10:02 AM PKT] Claude Code v2.1.51

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | ~~MEDIUM~~ | ~~Documentation~~ | ~~HOOKS-README heading says "Official 18 Hooks" but only 17 are in official docs (Setup is unofficial) — heading wording misleading~~ | ❌ INVALID (intentional wording) |
| 2 | MEDIUM | Matcher/Schema | HOOKS-README missing per-hook matcher values for SessionEnd, Notification, SubagentStart, SubagentStop, PreCompact, ConfigChange | ✅ COMPLETE (added to HOOKS-README) |
| 3 | MEDIUM | Hook Types/Env | HOOKS-README prompt/agent hook exclusion list only mentions TeammateIdle — should list all 9 command-only events | ✅ COMPLETE (updated exclusion list) |
| 4 | ~~MEDIUM~~ | ~~Config Drift~~ | ~~Windows settings use relative path — windows hooks won't work regardless~~ | ❌ INVALID (intentional platform difference) |
| 5 | LOW | Version Mismatch | TeammateIdle/TaskCompleted version — README says v2.1.33, CHANGELOG.md fetch suggests v2.1.45; needs verification | ✅ COMPLETE (researched and fixed) |
| 6 | LOW | Documentation | Common input fields (session_id, transcript_path, cwd, permission_mode, hook_event_name) not in dedicated HOOKS-README section | ✅ COMPLETE (added section) |
| 7 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-24 02:18 PM PKT] Claude Code v2.1.52

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Matcher/Schema | Specify SubagentStart/SubagentStop matcher values (Bash, Explore, Plan, custom) in HOOKS-README — currently says "Agent name string" | ✅ COMPLETE (updated to specific values) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-24 03:37 PM PKT] Claude Code v2.1.52

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Matcher/Schema | Add WorktreeCreate to HOOKS-README Decision Control Patterns table (stdout path + non-zero exit fails creation) | ✅ COMPLETE (added row to Decision Control Patterns table in HOOKS-README) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-24 04:38 PM PKT] Claude Code v2.1.52

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-25 10:10 AM PKT] Claude Code v2.1.55

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-26 10:21 AM PKT] Claude Code v2.1.59

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-27 10:08 AM PKT] Claude Code v2.1.62

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Hook Type Classification | Add Setup to command-only event list in HOOKS-README line 326 (Rule 1G: 9 + 8 = 17 ≠ 18) | ✅ COMPLETE (added Setup to command-only list — now 10 + 8 = 18) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-02-28 11:39 AM PKT] Claude Code v2.1.63

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Can-Block Fix | PostToolUse can-block status wrong in presentation — should be "Can Block" not "Cannot Block"; also missing from summary can-block list (Rules 2A + 2C) | ✅ COMPLETE (changed badge to "Can Block" + added PostToolUse to summary list) |
| 2 | LOW | Documentation | HTTP hook type (`type: "http"`) added in v2.1.63 — not documented in HOOKS-README Hook Types section | ✅ COMPLETE (added `type: "http"` section to HOOKS-README, updated count to "four hook handler types") |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-05 05:48 AM PKT] Claude Code v2.1.69

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Can-Block Fix | PostToolUseFailure can-block status wrong in presentation — should be "Can Block" not "Cannot Block"; also missing from summary can-block list and HOOKS-README Decision Control table (Rules 2A + 2C + 1H) | ✅ COMPLETE (changed badge to "Can Block" + added to summary list + added to Decision Control table) |
| 2 | MEDIUM | New Input Field | `agent_id`/`agent_type` now available on ALL hook events (not just SubagentStart/SubagentStop) — document in HOOKS-README Common Input Fields section | ✅ COMPLETE (added to Common Input Fields table as conditional fields) |
| 3 | MEDIUM | Schema Discovery | Elicitation and ElicitationResult hidden hooks found in v2.1.69 schema enum — document in Not-in-Official-Docs table | ✋ ON HOLD (recurring since 2026-03-04 v2.1.64; waiting for official documentation before adding) |
| 4 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves — official docs say "all supported" vs repo's tested 6 | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |
| 5 | LOW | Version Fix | InstructionsLoaded hook version corrected from v2.1.64 to v2.1.69 in HOOKS-README and README changelog table | ✅ COMPLETE (updated to v2.1.69) |

---

## [2026-03-06 08:20 AM PKT] Claude Code v2.1.70

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Input Field | Add 6 InstructionsLoaded fields (`file_path`, `memory_type`, `load_reason`, `globs`, `trigger_file_path`, `parent_file_path`) to HOOKS-README Options column | ✅ COMPLETE (added to Options column) |
| 2 | HIGH | New Input Field | Add `tool_use_id` to PreToolUse, PostToolUse, PostToolUseFailure Options columns in HOOKS-README | ✅ COMPLETE (added to Options columns) |
| 3 | MEDIUM | Decision Control | Update TeammateIdle/TaskCompleted in Decision Control table — v2.1.70 adds JSON `continue:false` support | ✅ COMPLETE (updated Decision Control table) |
| 4 | MEDIUM | Not-in-Docs Table | Remove InstructionsLoaded from Not-in-Docs table (now in official docs); update Setup note from "17 hooks" to "18 hooks" | ✅ COMPLETE (removed InstructionsLoaded row, updated Setup note) |
| 5 | LOW | Config Drift | Fix HOOKS-README line 387 cross-reference from "official 18 hooks" to "official 19 hooks" | ✅ COMPLETE (updated anchor link) |
| 6 | LOW | Presentation | Fix InstructionsLoaded slide version from "v2.1.64" to "v2.1.69" | ✅ COMPLETE (updated presentation slide) |
| 7 | LOW | Schema Discovery | Elicitation/ElicitationResult hidden hooks in schema — monitor | ✋ ON HOLD (recurring since 2026-03-04; waiting for official documentation) |
| 8 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-07 06:27 AM PKT] Claude Code v2.1.71

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Environment Variables | Add `${CLAUDE_SKILL_DIR}` to HOOKS-README env vars table (v2.1.69, skill-specific) | ✅ COMPLETE (added to env vars table) |
| 2 | LOW | Orphan Cleanup | Remove empty `.claude/hooks/sounds/elicitation/` orphan directory (no sound files, not in any map) | ✅ COMPLETE (removed empty directory) |
| 3 | LOW | Schema Discovery | Elicitation/ElicitationResult hidden hooks in schema — monitor | ✋ ON HOLD (recurring since 2026-03-04; waiting for official documentation) |
| 4 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-10 02:52 PM PKT] Claude Code v2.1.72

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Schema Discovery | Elicitation/ElicitationResult hidden hooks in schema — monitor | ✋ ON HOLD (recurring since 2026-03-04; waiting for official documentation) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-11 11:59 PM PKT] Claude Code v2.1.73

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Documentation | Fix HOOKS-README HTTP hook "Not supported" list — only mentions SessionStart/Setup, should reference all 11 command-only events | ✅ COMPLETE (updated to list all 11 command-only events) |
| 2 | LOW | Schema Discovery | Elicitation/ElicitationResult hidden hooks in schema — monitor | ✋ ON HOLD (recurring since 2026-03-04; waiting for official documentation) |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-12 12:22 PM PKT] Claude Code v2.1.74

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | New Env Var | Add `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` to HOOKS-README env vars table — SessionEnd hooks now respect configured timeout (v2.1.74 fix) | ✅ COMPLETE (added to HOOKS-README env vars table) |
| 2 | LOW | Schema Discovery | Elicitation/ElicitationResult hidden hooks in schema — monitor | ✋ ON HOLD (recurring since 2026-03-04; waiting for official documentation) |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-14 12:56 AM PKT] Claude Code v2.1.75

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | LOW | Schema Discovery | Elicitation/ElicitationResult hidden hooks in schema — monitor | ✋ ON HOLD (recurring since 2026-03-04; waiting for official documentation) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-14 08:59 AM PKT] Claude Code v2.1.76

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | `/workflows:workflow-add-hook PostCompact` — new in v2.1.76, fires after context compaction | ✅ COMPLETE (added to all files except settings.json — blocked by v2.1.75 schema; will add after Claude Code update) |
| 2 | HIGH | New Hook | `/workflows:workflow-add-hook Elicitation` — new in v2.1.76, MCP server user input request | ✅ COMPLETE (added to all 11 files) |
| 3 | HIGH | New Hook | `/workflows:workflow-add-hook ElicitationResult` — new in v2.1.76, user response to MCP elicitation | ✅ COMPLETE (added to all 11 files) |
| 4 | MEDIUM | Doc Fix | Update HOOKS-README "Not in Docs" Setup note: "18 hooks listed" → "21 hooks listed" | ✅ COMPLETE (updated to 21) |
| 5 | MEDIUM | Decision Control | Add Elicitation/ElicitationResult to HOOKS-README Decision Control table (both can block) | ✅ COMPLETE (added both rows) |
| 6 | LOW | Config Drift | Fix Setup sound file naming: `Setup.mp3` → `setup.mp3` for Linux case-sensitivity | ✅ COMPLETE (renamed to lowercase) |
| 7 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-17 12:44 PM PKT] Claude Code v2.1.77

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Matcher/Schema | Update PreToolUse matcher example in HOOKS-README line 426: add `Agent`, `WebFetch`, `WebSearch` tool names | ✅ COMPLETE (added 3 tool names to matcher example) |
| 2 | LOW | Config Drift | Fix HOOKS-README line 394 stale anchor `#hook-events-overview---official-19-hooks` → `#hook-events-overview---official-22-hooks` | ✅ COMPLETE (fixed internal anchor) |
| 3 | LOW | Schema Discovery | Document `asyncRewake` schema option in HOOKS-README (exists since v2.1.72, undocumented in official docs) | ✅ COMPLETE (added Hook Option subsection) |
| 4 | LOW | Presentation | Fix slide counter initial text "1 / 26" → "1 / 29" in presentation/index.html line 2376 | ✅ COMPLETE (updated to 1 / 29) |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-18 06:39 PM PKT] Claude Code v2.1.78

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | `/workflows:workflow-add-hook StopFailure` — new in v2.1.78, fires when turn ends due to API error (rate limit, auth failure) | ✅ COMPLETE (added to all files — 23 hooks consistent across repo) |
| 2 | LOW | Environment Variables | Add `CLAUDE_PLUGIN_DATA` to HOOKS-README env vars table (plugin persistent data directory, from official hooks reference) | ✅ COMPLETE (added to HOOKS-README env vars table) |
| 3 | LOW | Schema Discovery | Elicitation/ElicitationResult previously hidden hooks — now in official docs and repo | ✅ COMPLETE (resolved — both hooks added in v2.1.76 run, now fully documented) |
| 4 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-19 12:19 PM PKT] Claude Code v2.1.79

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Input Field | Add `error`, `error_details`, `last_assistant_message` to StopFailure Options column in HOOKS-README | ✅ COMPLETE (added 3 input fields to Options column) |
| 2 | HIGH | Matcher/Schema | Add InstructionsLoaded matcher (`load_reason`: session_start, nested_traversal, path_glob_match, include, compact) to Per-Hook Matcher Reference table | ✅ COMPLETE (added to matcher table) |
| 3 | HIGH | Matcher/Schema | Add StopFailure matcher (`error`: rate_limit, authentication_failed, billing_error, invalid_request, server_error, max_output_tokens, unknown) to Per-Hook Matcher Reference table | ✅ COMPLETE (added to matcher table) |
| 4 | MEDIUM | Config Drift | Fix HOOKS-README line 412 stale anchor `#hook-events-overview---official-22-hooks` → `#hook-events-overview---official-23-hooks` | ✅ COMPLETE (fixed internal anchor) |
| 5 | MEDIUM | Not-in-Docs | Remove StopFailure from "Not in Official Docs" table; update Setup note | ❌ INVALID (user confirmed StopFailure is not in official docs — keep in table) |
| 6 | LOW | Hook Options Table | Fix ElicitationResult Options: remove `action`/`content` (output fields), add `user_response`, `message` (input fields) | ✅ COMPLETE (fixed input/output field confusion) |
| 7 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-20 07:22 AM PKT] Claude Code v2.1.80

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Matcher/Schema | Add `resume` to SessionEnd matcher values in HOOKS-README line 452 and presentation slide 17 | ✅ COMPLETE (added `resume` to both HOOKS-README and presentation) |
| 2 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-23 09:44 PM PKT] Claude Code v2.1.81

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Not-in-Docs Table | Remove StopFailure from Not-in-Docs table; update Setup note from "21 hooks listed" to "22 hooks listed, Setup excluded" | ✋ ON HOLD (user decision: keep StopFailure in Not-in-Docs table like Setup) |
| 2 | LOW | Hook Options Table | Remove `mode` from ElicitationResult Options column — not in official docs for this hook (only for Elicitation) | ✅ COMPLETE (removed `mode` from ElicitationResult Options) |
| 3 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-25 09:43 PM PKT] Claude Code v2.1.83

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | `/workflows:workflow-add-hook CwdChanged` — v2.1.83, fires when working directory changes (reactive env management) | ✅ COMPLETE (added to all files — 25 hooks consistent across repo) |
| 2 | HIGH | New Hook | `/workflows:workflow-add-hook FileChanged` — v2.1.83, fires when files change | ✅ COMPLETE (added to all files — 25 hooks consistent across repo) |
| 3 | MEDIUM | Not-in-Docs Table | Update StopFailure entry — now confirmed in official docs by both agents; update Setup note "21 hooks" → "22 hooks listed, Setup excluded" | ✅ COMPLETE (removed StopFailure row, updated Setup note to "22 hooks listed, Setup excluded") |
| 4 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-26 08:39 PM PKT] Claude Code v2.1.84

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook | `/workflows:workflow-add-hook TaskCreated` — v2.1.84, fires when task created via TaskCreate tool | ✅ COMPLETE (added to all 14 files — 26 hooks consistent across repo) |
| 2 | HIGH | Not-in-Docs Table | Remove CwdChanged and FileChanged rows from HOOKS-README Not-in-Docs table — both now in official docs | ✅ COMPLETE (removed both rows from Not-in-Docs table) |
| 3 | HIGH | Not-in-Docs Table | Update Setup note from "(22 hooks listed, Setup excluded)" to "(25 hooks listed, Setup excluded)" | ✅ COMPLETE (updated to 25 hooks listed) |
| 4 | MEDIUM | Hook Options | Add `old_cwd`, `new_cwd` to CwdChanged Options column in HOOKS-README | ✅ COMPLETE (added to Options column) |
| 5 | MEDIUM | Env Var Docs | Fix `$CLAUDE_ENV_FILE` from "SessionStart only" to "SessionStart, CwdChanged, FileChanged" | ✅ COMPLETE (updated availability scope) |
| 6 | MEDIUM | Matcher Table | Add CwdChanged (no matcher) and FileChanged (filename basename) to Per-Hook Matcher Reference table | ✅ COMPLETE (added both entries to matcher table) |
| 7 | MEDIUM | Config Drift | Fix HOOKS-README stale anchor `#official-23-hooks` → `#official-26-hooks` | ✅ COMPLETE (updated anchor to match new heading) |
| 8 | MEDIUM | Can-Block Status | Investigate PostToolUseFailure — both agents report official docs say Cannot Block, but repo has Can Block since v2.1.69 | ✋ ON HOLD (needs investigation — keeping current Can Block status until confirmed) |
| 9 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-27 01:21 PM PKT] Claude Code v2.1.85

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | Presentation | Fix hook numbering bug — TaskCreated has duplicate number 16 (same as TaskCompleted); all 9 subsequent hooks (ConfigChange through FileChanged) are off by one (17→18 through 25→26) | ✅ COMPLETE (fixed 10 hook-number spans: TaskCreated→17, ConfigChange→18, WorktreeCreate→19, WorktreeRemove→20, InstructionsLoaded→21, Elicitation→22, ElicitationResult→23, StopFailure→24, CwdChanged→25, FileChanged→26) |
| 2 | MEDIUM | New Hook Option | Document new `if` conditional field for hooks — permission rule syntax (e.g., `Bash(git *)`) reduces unnecessary hook process spawning (v2.1.85) | ✋ ON HOLD (not yet in official docs pages — only in GitHub changelog; will document when docs update) |
| 3 | MEDIUM | Hook Enhancement | Document PreToolUse `updatedInput` for AskUserQuestion — enables headless integrations to auto-respond to user questions (v2.1.85) | ✋ ON HOLD (not yet in official docs pages — only in GitHub changelog; will document when docs update) |
| 4 | MEDIUM | Can-Block Status | PostToolUseFailure — official docs say Cannot Block (output is only `additionalContext`), but repo had Can Block since v2.1.69 in presentation badge, summary list, and HOOKS-README Decision Control table | ✅ COMPLETE (changed presentation badge to "Cannot Block", removed from summary can-block list, removed from HOOKS-README Decision Control blocking group) |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-28 06:07 PM PKT] Claude Code v2.1.86

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | HIGH | New Hook Option | Document `if` conditional field in HOOKS-README — now confirmed in official hooks guide (permission rule syntax, v2.1.85). Previously ON HOLD awaiting docs | ✅ COMPLETE (added Hook Option: `if` subsection to HOOKS-README with syntax, supported hooks, and examples) |
| 2 | LOW | Matcher/Schema | Add `AskUserQuestion`, `ExitPlanMode` to PreToolUse matcher example in HOOKS-README line 448 (official docs list these as matchable tool names) | ✅ COMPLETE (added both tool names to PreToolUse matcher example) |
| 3 | LOW | Hook Enhancement | Document PreToolUse `updatedInput` for AskUserQuestion — headless integration feature (v2.1.85) | ✅ COMPLETE (added subsection to HOOKS-README with example JSON and use cases) |
| 4 | LOW | Schema Discovery | Monitor `CronCreate` hook — mentioned in v2.1.85 changelog but NOT in schema or official docs | ❌ INVALID (not in schema propertyNames enum, not in official docs — likely internal/non-hook feature per Rule 6A) |
| 5 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |

---

## [2026-03-29 07:43 PM PKT] Claude Code v2.1.87

| # | Priority | Type | Action | Status |
|---|----------|------|--------|--------|
| 1 | MEDIUM | Hook Options Table | Update WorktreeCreate Options: `name` → `worktree_path`, `worktree_name`, `base_branch`; WorktreeRemove: add `worktree_name` — per official docs | ✅ COMPLETE (updated HOOKS-README Options column for both hooks) |
| 2 | MEDIUM | Hook Options Table | Update FileChanged Options: `event` → `change_type` per official docs | ✅ COMPLETE (updated HOOKS-README Options column) |
| 3 | MEDIUM | Hook Options Table | Update Elicitation Options: remove stale fields, add `tool_name`, `form_fields`; ElicitationResult: remove stale fields, add `tool_name`, `form_fields` — per official docs | ✅ COMPLETE (updated HOOKS-README Options column for both hooks) |
| 4 | MEDIUM | Hook Options Table | Update PreCompact/PostCompact: `trigger` → `compact_trigger`, remove undocumented `custom_instructions`/`compact_summary` — per official docs | ✅ COMPLETE (updated HOOKS-README Options column and matcher table) |
| 5 | MEDIUM | Can-Block Status | PostToolUse can-block — official docs confirm "No" (exit code 2 = feedback only, tool already ran). Updated presentation badge and summary list, removed from HOOKS-README Decision Control blocking group | ✅ COMPLETE (changed presentation badge to Cannot Block, removed from summary can-block list, updated Decision Control table) |
| 6 | LOW | Agent Hook Docs | Re-test agent frontmatter hooks when upstream #27153 resolves | ✋ ON HOLD (recurring since 2026-02-20; upstream issue [#27153](https://github.com/anthropics/claude-code/issues/27153) still open) |
```

## File: `changelog/verification-checklist.md`
```markdown
# Verification Checklist

Rules accumulate over time. Each workflow-changelog run MUST execute ALL rules at the specified depth. When a new type of drift is caught that an existing rule should have caught (but didn't exist or was too shallow), append a new rule here.

## Depth Levels

| Depth | Meaning | Example |
|-------|---------|---------|
| `exists` | Check if a section/table/file exists | "Does HOOKS-README have a matcher table?" |
| `presence-check` | Check if a specific item is present or absent | "Is WorktreeCreate in the Not-in-Docs table?" |
| `content-match` | Compare actual values word-by-word against source | "Do SubagentStart matcher values match official docs?" |
| `field-level` | Verify every individual field is accounted for | "Does each hook's Options column list every input field from docs?" |
| `cross-file` | Same value must match across multiple files | "Does hook count match across settings x4, hooks.py, config, README, HOOKS-README, presentation?" |

---

## 1. HOOKS-README Documentation

Rules that verify HOOKS-README content against official docs.

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 1A | Hook Options | For each hook, verify every input field listed in official docs appears in HOOKS-README Options column | field-level | hooks-reference page | 2026-02-20 | Notification fields (`notification_type`, `message`, `title`) were missing |
| 1B | Matcher Values | For each hook with a matcher, compare HOOKS-README per-hook matcher reference values against official docs values word-by-word | content-match | hooks-reference page | 2026-02-24 | SubagentStart said "Agent name string" instead of specific values (Bash, Explore, Plan, custom) |
| 1C | Not-in-Docs Table | For each hook listed in HOOKS-README "Not in Official Docs" table, verify it is actually absent from official docs; remove if now present | presence-check | hooks-reference page | 2026-02-22 | WorktreeCreate/WorktreeRemove were listed as "not in docs" but had been added |
| 1D | Command-Only Events | Verify HOOKS-README prompt/agent hook exclusion list includes ALL command-only events (not just a subset) | content-match | hooks-reference page | 2026-02-24 | List only mentioned TeammateIdle, omitted 8 other command-only events |
| 1E | Common Input Fields | Verify HOOKS-README common input fields section lists all fields from official docs (session_id, transcript_path, cwd, permission_mode, hook_event_name) | field-level | hooks-reference page | 2026-02-23 | Section was missing entirely |
| 1F | Environment Variables | Verify HOOKS-README env vars section lists all standard hook env vars from official docs | field-level | hooks-guide page | 2026-02-20 | Potential env var gaps flagged by external sources |
| 1G | Hook Type Classification Totals | Verify that (command-only event count) + (prompt/agent supported count) = total hook count. If they don't sum correctly, a hook is missing from one of the two lists | content-match | HOOKS-README hook types section | 2026-02-24 | Setup was omitted from both lists (9 command-only + 8 prompt/agent = 17, but total is 18) |
| 1H | Decision Control Table Completeness | For each hook that can-block per official docs, verify it has an entry in the HOOKS-README Decision Control Patterns table (lines 446+). Check both JSON-based decision hooks AND exit-code-only/stdout-based hooks | presence-check | hooks-reference page can-block list vs HOOKS-README Decision Control Patterns table | 2026-02-24 | WorktreeCreate was can-block in official docs and on presentation slide (fixed 2026-02-22) but was never added to the HOOKS-README Decision Control table — Rule 2A only checks presentation badges, not the HOOKS-README table |
| 1I | Hook Handler Types List | Verify HOOKS-README Hook Types section lists all handler types from official docs (command, http, prompt, agent). Check both the count in the intro text and the subsection headings. Handler types ≠ hook event classification (Rule 1G) | content-match | hooks-reference page | 2026-02-28 | HOOKS-README said "three hook handler types" but v2.1.63 added `http` as a fourth — no rule covered handler type completeness |

---

## 2. Presentation

Rules that verify presentation slides accuracy and completeness.

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 2A | Can-Block Status | For each hook, verify can-block/cannot-block badge in presentation matches official docs can-block table | content-match | hooks-reference page | 2026-02-22 | WorktreeCreate had "Cannot Block" but should have been "Can Block" |
| 2B | Presentation Slides | Verify totalSlides variable matches actual slide count, and each hook has a dedicated slide | cross-file | presentation index.html | 2026-02-21 | Slide count consistency after adding new hooks |
| 2C | Can-Block Summary Slide | Verify the presentation summary slide listing of blocking hooks matches the set of individual hook slides that have "Can Block" badge | cross-file | presentation individual slides vs summary slide | 2026-02-24 | WorktreeCreate was wrong on individual slide AND missing from summary — two independent errors, Rule 2A only checks individual slides vs docs |
| 2D | Lifecycle Diagram Completeness | Verify all hooks appear somewhere in the presentation lifecycle diagram (sequential flow, async section, or separate trigger section). Count hooks in diagram must equal total hook count | presence-check | presentation lifecycle diagram vs hook list | 2026-02-24 | Setup was missing from lifecycle diagram (caught 2026-02-21) but no rule was added to prevent recurrence |
| 2E | Presentation vs HOOKS-README Matcher Values | For hooks that show matcher values on presentation slides, verify those values match what HOOKS-README per-hook matcher reference table says | cross-file | presentation slides vs HOOKS-README | 2026-02-24 | Rule 1B checks HOOKS-README vs official docs, but presentation could drift independently from HOOKS-README |
| 2F | Hook Number Sequence | Verify all `<span class="hook-number">N</span>` values in presentation are sequential 1 through total-hook-count with no duplicates and no gaps. Extract all hook-number spans and check the sequence | cross-file | presentation hook-number spans | 2026-03-27 | TaskCreated was added with duplicate hook-number 16 (same as TaskCompleted) because workflow-add-hook did not increment hook-numbers for subsequent slides — only data-slide numbers were shifted |

---

## 3. Cross-File Consistency

Rules that verify the same value matches across multiple repo files.

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 3A | Version Badges | Compare version string across README badge, presentation title (line 543), presentation slide 2 (line 561), presentation slide 3 (line 599) | cross-file | changelog latest version | 2026-02-21 | Version staleness found in multiple locations on every run |
| 3B | Hook Count | Verify hook count is identical across: settings.json, settings-mac.json, settings-linux.json, settings-windows.json, hooks.py HOOK_SOUND_MAP, hooks-config.json, HOOKS-README heading, README badge, presentation (check ALL count locations: slide 2 "N Hooks Explained", slide 2 "supports N hooks (as of vX.X.XX)" use-case span, slide 3 TOC title, totalSlides variable) | cross-file | all listed files | 2026-02-21 | Count went from 16 to 18 but not all files were updated. The "supports N hooks" use-case span on slide 2 was missed during 2026-03-26 run |
| 3C | Hook Name Spelling | Verify all 18 hook names are spelled identically (exact PascalCase) across: settings.json hooks keys, settings-mac/linux/windows hooks keys, hooks.py HOOK_SOUND_MAP keys, hooks-config.json toggle names (disable[Name]Hook pattern), HOOKS-README table, presentation slide hook-name spans, presentation TOC items, lifecycle diagram | cross-file | all listed files | 2026-02-24 | Rule 3B only checks count — a misspelled hook would pass count check but break functionality |
| 3D | Agent Hook Consistency | Verify the 6 agent hooks are consistent across: AGENT_HOOK_SOUND_MAP in hooks.py (6 entries), agent sound folders (6 folders), HOOKS-README agent hooks section (6 listed), presentation agent slide (says "6 of N hooks") | cross-file | hooks.py, filesystem, HOOKS-README, presentation | 2026-02-24 | Agent hook count/names never had a cross-file consistency rule |

---

## 4. Settings & Config

Rules that verify settings files, config, and filesystem assets.

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 4A | Sound Folder Existence | For each entry in HOOK_SOUND_MAP and AGENT_HOOK_SOUND_MAP, verify corresponding folder exists under .claude/hooks/sounds/ and contains at least one .mp3 and one .wav file | presence-check | hooks.py maps vs filesystem | 2026-02-24 | Sound folders could be missing after manual edits; workflow-add-hook creates them but no verification existed |
| 4B | Settings Hook Structure | For each hook across all 4 settings files, verify: timeout value (5000 for all except Setup which is 30000), async is true, `once` flag only on PreCompact/SessionStart/SessionEnd, statusMessage matches hook name | field-level | settings.json vs settings-mac/linux/windows | 2026-02-24 | Wrong timeout or missing once flag would cause behavioral bugs not caught by name/count checks |
| 4C | hooks-config.json Toggle Pattern | Verify each hook has exactly one toggle key in hooks-config.json following the pattern `disable[ExactHookName]Hook`, and no extra/orphaned toggles exist | presence-check | hooks-config.json vs hook name list | 2026-02-24 | A renamed or removed hook could leave orphaned toggle keys or miss new ones |
| 4D | README Changelog Table | Verify latest row in README.md changelog table has current hook count and latest version. Hook count across rows should be monotonically non-decreasing | content-match | README.md changelog table vs current state | 2026-02-24 | Changelog table could show stale count or version after updates to other files |
| 4E | Handler Option Completeness | For each handler-level option documented in official docs (type, command, timeout, async, statusMessage, shell, if, asyncRewake, once, matcher), verify HOOKS-README has a corresponding Hook Option subsection or table entry documenting the option's behavior | field-level | hooks-reference + hooks-guide pages vs HOOKS-README Hook Option subsections | 2026-03-28 | The `if` conditional field (v2.1.85) was in official hooks guide but not documented in HOOKS-README — no rule checked handler-level option completeness (Rule 1A only covers per-hook input fields, Rule 4B only checks settings file structure) |

---

## 5. Schema & Hidden Hooks

Rules that verify the settings.json schema against official docs and local repo.

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 5A | Schema Hook Names | Locate the Claude Code settings.json JSON schema and extract the `propertyNames` enum from the `hooks` property. Compare the enum entries against: (a) official docs hook list, (b) local repo HOOK_SOUND_MAP keys. Flag hooks in schema but not in docs as "hidden/undocumented". Flag hooks in docs but not in schema as "schema outdated". Flag hooks in schema but not in local repo as "unsupported by project" | cross-file | settings.json schema vs hooks-reference page vs hooks.py HOOK_SOUND_MAP | 2026-03-04 | Elicitation and ElicitationResult were discovered in the schema enum during v2.1.64 InstructionsLoaded addition — no rule existed to detect hidden hooks in the schema |

---

## 6. Process

Meta-rules about the workflow verification process itself.

| # | Category | Check | Depth | Compare Against | Added | Origin |
|---|----------|-------|-------|-----------------|-------|--------|
| 6A | Source Credibility Guard | Only flag items as drift if confirmed by official sources (hooks-reference page, hooks-guide page, GitHub changelog). Third-party blog sources may be outdated or wrong — use them for leads only, verify against official docs before flagging | content-match | official docs only | 2026-02-24 | Past runs produced false positives: OpenInEditor hook (2026-02-20), CLAUDE_HOOK_* env vars (2026-02-20), Windows relative path (2026-02-24) — all sourced from blogs, not official docs |
```

## File: `demo/.mcp.json`
```json
{
  "mcpServers": {
    "elicit": {
      "command": "npx",
      "args": ["-y", "@blizzy/mcp-elicit"]
    }
  }
}
```

## File: `demo/hooks-lifecycle.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Demo - Claude Code Hooks</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 90' width='140' height='126'%3E%3Cstyle%3E.claude-body%7Banimation:jump .5s ease-in-out infinite;transform-origin:center bottom%7D.shadow%7Banimation:shadow-scale .5s ease-in-out infinite%7D.left-arm%7Banimation:wave-left .5s ease-in-out infinite;transform-origin:right center%7D.right-arm%7Banimation:wave-right .5s ease-in-out infinite;transform-origin:left center%7D.left-ear%7Banimation:ear-bounce .5s ease-in-out infinite;transform-origin:center bottom%7D.right-ear%7Banimation:ear-bounce .5s ease-in-out infinite .1s;transform-origin:center bottom%7D@keyframes jump%7B0%25,100%25%7Btransform:translateY(0) scaleY(1) scaleX(1)%7D30%25%7Btransform:translateY(-16px) scaleY(1.1) scaleX(.95)%7D50%25%7Btransform:translateY(-18px) scaleY(1.05) scaleX(.98)%7D80%25%7Btransform:translateY(-5px) scaleY(.95) scaleX(1.05)%7D%7D@keyframes shadow-scale%7B0%25,100%25%7Btransform:scaleX(1);opacity:.25%7D50%25%7Btransform:scaleX(.4);opacity:.08%7D%7D@keyframes wave-left%7B0%25,100%25%7Btransform:rotate(0)%7D50%25%7Btransform:rotate(-25deg)%7D%7D@keyframes wave-right%7B0%25,100%25%7Btransform:rotate(0)%7D50%25%7Btransform:rotate(25deg)%7D%7D@keyframes ear-bounce%7B0%25,100%25%7Btransform:scaleY(1)%7D40%25%7Btransform:scaleY(1.2)%7D60%25%7Btransform:scaleY(.85)%7D%7D%3C/style%3E%3Cellipse class='shadow' cx='50' cy='82' rx='22' ry='5' fill='%23000'/%3E%3Cg class='claude-body'%3E%3Crect class='left-ear' x='22' y='10' width='8' height='14' fill='%23E07C4C'/%3E%3Crect class='right-ear' x='70' y='10' width='8' height='14' fill='%23E07C4C'/%3E%3Crect x='18' y='24' width='64' height='4' fill='%23E07C4C'/%3E%3Crect x='14' y='28' width='72' height='32' fill='%23E07C4C'/%3E%3Crect x='30' y='34' width='8' height='10' fill='%23000'/%3E%3Crect x='62' y='34' width='8' height='10' fill='%23000'/%3E%3Crect class='left-arm' x='2' y='36' width='12' height='8' fill='%23E07C4C'/%3E%3Crect class='right-arm' x='86' y='36' width='12' height='8' fill='%23E07C4C'/%3E%3Crect x='24' y='60' width='12' height='14' fill='%23E07C4C'/%3E%3Crect x='64' y='60' width='12' height='14' fill='%23E07C4C'/%3E%3C/g%3E%3C/svg%3E">
<style>
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; height: 100%; overflow: hidden; font-family: system-ui, -apple-system, sans-serif; }
  body { display: flex; flex-direction: column; height: 100vh; background: #0d1117; }

  header { background: #161b22; border-bottom: 1px solid #30363d; padding: 4px 16px; display: flex; justify-content: space-between; align-items: center; flex-shrink: 0; height: 32px; }
  header h1 { margin: 0; font-size: 14px; color: #e6edf3; }
  .header-controls { display: flex; align-items: center; gap: 12px; }
  .status-indicator { display: flex; align-items: center; gap: 5px; }
  #status-dot { width: 7px; height: 7px; border-radius: 50%; background: #f85149; }
  #status-text { font-size: 11px; color: #8b949e; }
  .reset-btn { padding: 2px 10px; background: #21262d; color: #c9d1d9; border: 1px solid #30363d; border-radius: 4px; cursor: pointer; font-size: 11px; }
  .reset-btn:hover { background: #30363d; }

  .main-content { display: flex; flex: 1; overflow: hidden; }
  .resize-handle { width: 4px; background: #ccc; cursor: col-resize; flex-shrink: 0; transition: background 0.2s; }
  .resize-handle:hover, .resize-handle.dragging { background: #666; }

  /* ===== LEFT PANEL (LIGHT) ===== */
  .left-panel { flex: 1; min-width: 0; overflow-y: auto; padding: 8px 12px; background: #ffffff; color: #111; }
  .left-panel::-webkit-scrollbar { width: 4px; }
  .left-panel::-webkit-scrollbar-thumb { background: #ccc; border-radius: 2px; }

  .prompts-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4px; grid-auto-rows: 1fr; }

  .prompt-card { border: 1px solid #e0e0e0; border-radius: 5px; padding: 5px 10px; transition: border-color 0.4s; }
  .prompt-card.card-lit { border-color: #e6b800; }
  .prompt-header { display: flex; align-items: baseline; gap: 6px; flex-wrap: wrap; margin-bottom: 2px; }
  .prompt-step { font-size: 15px; font-weight: 700; color: #111; white-space: nowrap; }
  .prompt-hooks { display: flex; flex-wrap: wrap; gap: 5px; align-items: center; }
  .hook-tag { font-size: 11px; font-weight: 500; padding: 1px 5px; border-radius: 6px; background: #f0f0f0; color: #333; border: 1px solid #ddd; line-height: 1.3; }
  .prompt-code { font-family: 'SF Mono', 'Fira Code', monospace; font-size: 14px; color: #111; background: #f6f6f6; border-radius: 4px; padding: 2px 0; line-height: 1.4; }
  .prompt-code .prefix { color: #999; }
  .prompt-line { display: flex; align-items: center; padding: 1px 10px; gap: 6px; }
  .prompt-line-text { flex: 1; white-space: pre-wrap; }
  .copy-btn { flex-shrink: 0; background: none; border: none; cursor: pointer; padding: 2px; border-radius: 3px; opacity: 0; transition: opacity 0.15s; color: #999; }
  .prompt-line:hover .copy-btn { opacity: 1; }
  .copy-btn:hover { color: #333; background: #e0e0e0; }
  .copy-btn.copied { opacity: 1; color: #22863a; }
  .copy-btn svg { display: block; width: 14px; height: 14px; }

  .bonus-section { border: 1px solid #e0e0e0; border-radius: 6px; padding: 10px 14px; margin-bottom: 8px; }
  .bonus-title { font-size: 13px; font-weight: 700; color: #555; margin-bottom: 6px; }
  .bonus-item { font-size: 13px; color: #333; margin-bottom: 5px; line-height: 1.4; display: flex; align-items: center; gap: 5px; flex-wrap: wrap; }
  .bonus-item code { font-family: monospace; font-size: 12px; color: #111; background: #f0f0f0; padding: 1px 5px; border-radius: 2px; }

  /* ===== RIGHT PANEL (DARK) ===== */
  .right-panel { width: 40%; min-width: 30%; display: flex; flex-direction: column; overflow: hidden; position: relative; background: #0d1117; }

  .right-branding { position: absolute; top: 4px; right: 8px; display: flex; flex-direction: column; align-items: center; z-index: 5; }
  .right-branding svg { width: 90px; height: auto; }
  .right-branding-text { font-size: 11px; font-weight: 600; color: #8b949e; text-align: center; line-height: 1.3; margin-top: 4px; }
  .right-branding-text strong { color: #e6edf3; font-size: 13px; display: block; }

  .chart-container { flex: 1; display: flex; justify-content: center; align-items: center; padding: 0 4px 4px; overflow: hidden; }
  .chart-container svg { height: 100%; width: auto; max-width: 100%; }

  .hook-rect { fill: #161b22; stroke: #30363d; stroke-width: 1.5; transition: all 0.5s ease; }
  .hook-rect.lit { fill: #FFD700; stroke: #FFA500; filter: url(#glow); }
  .hook-rect-stop { fill: #2d1519; stroke: #6e2b2b; }
  .hook-text { fill: #484f58; font-family: system-ui, -apple-system, sans-serif; font-size: 12px; font-weight: 600; transition: fill 0.5s ease; pointer-events: none; }
  .hook-text.lit { fill: #1a1a1a; }
  .hook-text-side { font-size: 10px; }
  .hook-subtitle { fill: #484f58; font-family: system-ui, -apple-system, sans-serif; font-size: 8px; transition: fill 0.5s ease; pointer-events: none; }
  .hook-subtitle.lit { fill: #1a1a1a; }
  .hook-rect-side { stroke-dasharray: 5 3; }
  .tool-rect { fill: #0d2137; stroke: #1f4a6e; stroke-width: 1.5; }
  .tool-text { fill: #58a6d4; font-family: system-ui, -apple-system, sans-serif; font-size: 12px; font-weight: 600; pointer-events: none; }
  .loop-rect { fill: none; stroke: #8b6914; stroke-width: 1.5; stroke-dasharray: 6 4; }
  .loop-label { fill: #8b6914; font-family: system-ui, -apple-system, sans-serif; font-size: 10px; font-weight: 700; }
  .arrow-line { stroke: #30363d; stroke-width: 1.5; fill: none; }
  .arrow-head { fill: #30363d; }
  .arrow-dashed { stroke-dasharray: 5 3; }
  .resume-label { fill: #484f58; font-family: system-ui, -apple-system, sans-serif; font-size: 9px; font-style: italic; }
  .connector-dashed { stroke: #30363d; stroke-width: 1; stroke-dasharray: 4 3; fill: none; }
  @keyframes pulse-glow { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }
  .hook-group.just-fired .hook-rect.lit { animation: pulse-glow 0.6s ease-in-out; }
  .fire-count { font-size: 9px; font-weight: 700; fill: #000; display: none; font-family: system-ui, -apple-system, sans-serif; }
  .fire-count.visible { display: block; }

  #event-log { position: absolute; bottom: 0; left: 0; right: 0; background: rgba(13,17,23,0.95); border-top: 1px solid #30363d; padding: 6px 10px; height: 90px; overflow-y: auto; z-index: 10; }
  .log-header { font-size: 10px; color: #8b949e; margin-bottom: 3px; font-weight: 600; }
  #log-entries { font-family: monospace; font-size: 10px; color: #c9d1d9; }
</style>
</head>
<body>

<header>
  <h1>Claude Code Hooks Lifecycle Demo</h1>
  <div class="header-controls">
    <div class="status-indicator"><span id="status-dot"></span><span id="status-text">Disconnected</span></div>
    <button class="reset-btn" onclick="resetHooks()">Reset All</button>
  </div>
</header>

<div class="main-content">

  <!-- LEFT PANEL (white/light theme) -->
  <div class="left-panel">
    <div class="prompts-grid">
      <div class="prompt-card" data-card-hooks="SessionStart,InstructionsLoaded">
        <div class="prompt-header"><span class="prompt-step">1. Start Claude</span><div class="prompt-hooks"><span class="hook-tag">SessionStart</span><span class="hook-tag">InstructionsLoaded</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">$</span> claude</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="UserPromptSubmit,PreToolUse,PermissionRequest,PostToolUse,Stop">
        <div class="prompt-header"><span class="prompt-step">2. Use tools</span><div class="prompt-hooks"><span class="hook-tag">UserPromptSubmit</span><span class="hook-tag">PreToolUse</span><span class="hook-tag">PermissionRequest</span><span class="hook-tag">PostToolUse</span><span class="hook-tag">Stop</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">&gt;</span> What is the weather in Karachi?</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="SubagentStart,SubagentStop,TaskCompleted">
        <div class="prompt-header"><span class="prompt-step">3. Subagent</span><div class="prompt-hooks"><span class="hook-tag">SubagentStart</span><span class="hook-tag">SubagentStop</span><span class="hook-tag">TaskCompleted</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">&gt;</span> Use Explore agent to read the README.md file</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="PostToolUseFailure">
        <div class="prompt-header"><span class="prompt-step">4. Failure</span><div class="prompt-hooks"><span class="hook-tag">PostToolUseFailure</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">&gt;</span> ls ABC</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="PreCompact,PostCompact">
        <div class="prompt-header"><span class="prompt-step">5. Compact</span><div class="prompt-hooks"><span class="hook-tag">PreCompact</span><span class="hook-tag">PostCompact</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">&gt;</span> /compact</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="TeammateIdle">
        <div class="prompt-header"><span class="prompt-step">6. Teammate idle</span><div class="prompt-hooks"><span class="hook-tag">TeammateIdle</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">$</span> CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">&gt;</span> Create an agent team to QA this demo project</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="TaskCreated">
        <div class="prompt-header"><span class="prompt-step">7. Task created</span><div class="prompt-hooks"><span class="hook-tag">TaskCreated</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">&gt;</span> Create a task to add a login page</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="StopFailure">
        <div class="prompt-header"><span class="prompt-step">8. API error</span><div class="prompt-hooks"><span class="hook-tag">StopFailure</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">$</span> ANTHROPIC_API_KEY=sk-invalid claude</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">&gt;</span> Hi</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="Elicitation,ElicitationResult">
        <div class="prompt-header"><span class="prompt-step">9. Elicitation</span><div class="prompt-hooks"><span class="hook-tag">Elicitation</span><span class="hook-tag">ElicitationResult</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">&gt;</span> Use elicit_boolean to ask if I like pizza</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="WorktreeCreate,WorktreeRemove">
        <div class="prompt-header"><span class="prompt-step">10. Worktree</span><div class="prompt-hooks"><span class="hook-tag">WorktreeCreate</span><span class="hook-tag">WorktreeRemove</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">&gt;</span> Enter a worktree and save the current time to time.txt</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">&gt;</span> Exit the worktree</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="ConfigChange">
        <div class="prompt-header"><span class="prompt-step">11. Config change</span><div class="prompt-hooks"><span class="hook-tag">ConfigChange</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">$</span> Edit .claude/settings.json while running</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="Notification">
        <div class="prompt-header"><span class="prompt-step">12. Notification</span><div class="prompt-hooks"><span class="hook-tag">Notification</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text">Leave Claude idle</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="SessionEnd">
        <div class="prompt-header"><span class="prompt-step">13. End session</span><div class="prompt-hooks"><span class="hook-tag">SessionEnd</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">&gt;</span> exit</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="Setup">
        <div class="prompt-header"><span class="prompt-step">14. Setup</span><div class="prompt-hooks"><span class="hook-tag">Setup</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">$</span> claude --init-only</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="CwdChanged">
        <div class="prompt-header"><span class="prompt-step">15. Directory change</span><div class="prompt-hooks"><span class="hook-tag">CwdChanged</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">&gt;</span> cd to the parent directory</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div></div>
      </div>
      <div class="prompt-card" data-card-hooks="FileChanged">
        <div class="prompt-header"><span class="prompt-step">16. File change</span><div class="prompt-hooks"><span class="hook-tag">FileChanged</span></div></div>
        <div class="prompt-code"><div class="prompt-line"><span class="prompt-line-text"><span class="prefix">$</span> echo "X=1" >> .env</span><button class="copy-btn" onclick="copyLine(this)" title="Copy"></button></div><div class="prompt-line"><span class="prompt-line-text">Run in separate terminal; matcher configured</span></div></div>
      </div>
    </div>
  </div>

  <div class="resize-handle" id="resize-handle"></div>

  <!-- RIGHT PANEL (dark) -->
  <div class="right-panel" id="right-panel">

    <!-- Branding top-right -->
    <div class="right-branding">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 90">
        <style>
          .cb{animation:b .8s ease-in-out infinite;transform-origin:center bottom}
          .sh{animation:sp .8s ease-in-out infinite}
          .mo{animation:tk .3s ease-in-out infinite;transform-origin:center center}
          .le{animation:el .8s ease-in-out infinite;transform-origin:center bottom}
          .re{animation:er .8s ease-in-out infinite;transform-origin:center bottom}
          .w1{animation:we .8s ease-out infinite;transform-origin:left center}
          .w2{animation:we .8s ease-out infinite .2s;transform-origin:left center}
          .w3{animation:we .8s ease-out infinite .4s;transform-origin:left center}
          .n1{animation:f1 1.5s ease-out infinite}.n2{animation:f2 1.5s ease-out infinite .3s}.n3{animation:f3 1.5s ease-out infinite .6s}
          @keyframes b{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}
          @keyframes sp{0%,100%{transform:scaleX(1);opacity:.25}50%{transform:scaleX(.9);opacity:.2}}
          @keyframes tk{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.5)}}
          @keyframes el{0%,100%{transform:rotate(0)}50%{transform:rotate(-5deg)}}
          @keyframes er{0%,100%{transform:rotate(0)}50%{transform:rotate(5deg)}}
          @keyframes we{0%{opacity:.8;transform:scaleX(.3) scaleY(.8)}100%{opacity:0;transform:scaleX(1.2) scaleY(1)}}
          @keyframes f1{0%{opacity:1;transform:translate(0,0) rotate(0)}100%{opacity:0;transform:translate(15px,-25px) rotate(15deg)}}
          @keyframes f2{0%{opacity:1;transform:translate(0,0) rotate(0)}100%{opacity:0;transform:translate(20px,-30px) rotate(-10deg)}}
          @keyframes f3{0%{opacity:1;transform:translate(0,0) rotate(0)}100%{opacity:0;transform:translate(10px,-35px) rotate(20deg)}}
        </style>
        <ellipse class="sh" cx="50" cy="82" rx="22" ry="5" fill="#000"/>
        <g class="w1"><path d="M92 44Q100 44 100 52Q100 60 92 60" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
        <g class="w2"><path d="M96 38Q108 38 108 52Q108 66 96 66" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
        <g class="w3"><path d="M100 32Q116 32 116 52Q116 72 100 72" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
        <g class="n1"><ellipse cx="108" cy="28" rx="4" ry="3" fill="#E07C4C" transform="rotate(-20,108,28)"/><rect x="111" y="12" width="2" height="16" fill="#E07C4C"/><path d="M113 12Q118 14 118 18Q118 22 113 20" fill="#E07C4C"/></g>
        <g class="n2"><ellipse cx="122" cy="22" rx="4" ry="3" fill="#E07C4C" transform="rotate(-20,122,22)"/><rect x="125" y="6" width="2" height="16" fill="#E07C4C"/></g>
        <g class="n3"><ellipse cx="115" cy="42" rx="3" ry="2.5" fill="#E07C4C" transform="rotate(-20,115,42)"/><ellipse cx="125" cy="40" rx="3" ry="2.5" fill="#E07C4C" transform="rotate(-20,125,40)"/><rect x="117" y="26" width="2" height="16" fill="#E07C4C"/><rect x="127" y="24" width="2" height="16" fill="#E07C4C"/><rect x="117" y="26" width="12" height="2" fill="#E07C4C"/></g>
        <g class="cb"><rect class="le" x="22" y="10" width="8" height="14" fill="#E07C4C"/><rect class="re" x="70" y="10" width="8" height="14" fill="#E07C4C"/><rect x="18" y="24" width="64" height="4" fill="#E07C4C"/><rect x="14" y="28" width="72" height="32" fill="#E07C4C"/><rect x="30" y="34" width="8" height="10" fill="#000"/><rect x="62" y="34" width="8" height="10" fill="#000"/><rect class="mo" x="44" y="50" width="12" height="6" fill="#000"/><rect x="2" y="40" width="12" height="8" fill="#E07C4C"/><rect x="86" y="40" width="12" height="8" fill="#E07C4C"/><rect x="24" y="60" width="12" height="14" fill="#E07C4C"/><rect x="64" y="60" width="12" height="14" fill="#E07C4C"/></g>
      </svg>
      <div class="right-branding-text"><strong>Claude Code Hooks</strong>26 supported</div>
    </div>

    <!-- Chart -->
    <div class="chart-container">
      <svg viewBox="0 -32 520 552" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet">
        <defs>
          <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5" result="blur"/><feFlood flood-color="#FFD700" flood-opacity="0.5" result="color"/><feComposite in="color" in2="blur" operator="in" result="shadow"/><feMerge><feMergeNode in="shadow"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
          <marker id="ah" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto"><polygon points="0 0,6 2.5,0 5" class="arrow-head"/></marker>
        </defs>
        <g class="hook-group" data-hook="Setup"><rect class="hook-rect hook-rect-side" x="15" y="5" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="17" text-anchor="middle">Setup</text><text class="hook-subtitle" x="65" y="27" text-anchor="middle">(Init)</text><text class="fire-count" x="112" y="9" text-anchor="end"></text></g>
        <line class="connector-dashed" x1="115" y1="19" x2="156" y2="19"/>
        <g class="hook-group" data-hook="Elicitation"><rect class="hook-rect hook-rect-side" x="15" y="150" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="162" text-anchor="middle">Elicitation</text><text class="hook-subtitle" x="65" y="172" text-anchor="middle">(MCP input)</text><text class="fire-count" x="112" y="154" text-anchor="end"></text></g>
        <g class="hook-group" data-hook="ElicitationResult"><rect class="hook-rect hook-rect-side" x="15" y="180" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="192" text-anchor="middle">ElicitationResult</text><text class="hook-subtitle" x="65" y="202" text-anchor="middle">(MCP input)</text><text class="fire-count" x="112" y="184" text-anchor="end"></text></g>
        <line class="connector-dashed" x1="115" y1="194" x2="156" y2="194"/>
        <g class="hook-group" data-hook="Notification"><rect class="hook-rect hook-rect-side" x="15" y="305" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="317" text-anchor="middle">Notification</text><text class="hook-subtitle" x="65" y="327" text-anchor="middle">(Async)</text><text class="fire-count" x="112" y="309" text-anchor="end"></text></g>
        <g class="hook-group" data-hook="ConfigChange"><rect class="hook-rect hook-rect-side" x="15" y="335" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="347" text-anchor="middle">ConfigChange</text><text class="hook-subtitle" x="65" y="357" text-anchor="middle">(Async)</text><text class="fire-count" x="112" y="339" text-anchor="end"></text></g>
        <g class="hook-group" data-hook="WorktreeCreate"><rect class="hook-rect hook-rect-side" x="15" y="365" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="377" text-anchor="middle">WorktreeCreate</text><text class="hook-subtitle" x="65" y="387" text-anchor="middle">(Setup)</text><text class="fire-count" x="112" y="369" text-anchor="end"></text></g>
        <g class="hook-group" data-hook="WorktreeRemove"><rect class="hook-rect hook-rect-side" x="15" y="395" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="407" text-anchor="middle">WorktreeRemove</text><text class="hook-subtitle" x="65" y="417" text-anchor="middle">(Teardown)</text><text class="fire-count" x="112" y="399" text-anchor="end"></text></g>
        <g class="hook-group" data-hooks="CwdChanged,FileChanged"><rect class="hook-rect hook-rect-side" x="15" y="425" width="100" height="40" rx="5"/><text class="hook-text hook-text-side" x="65" y="439" text-anchor="middle">CwdChanged</text><text class="hook-text hook-text-side" x="65" y="451" text-anchor="middle">FileChanged</text><text class="hook-subtitle" x="65" y="461" text-anchor="middle">(Env reactive)</text><text class="fire-count" x="112" y="429" text-anchor="end"></text></g>
        <g class="hook-group" data-hook="InstructionsLoaded"><rect class="hook-rect hook-rect-side" x="15" y="-27" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="65" y="-15" text-anchor="middle">InstructionsLoaded</text><text class="hook-subtitle" x="65" y="-5" text-anchor="middle">(Async)</text><text class="fire-count" x="112" y="-23" text-anchor="end"></text></g>
        <line class="connector-dashed" x1="65" y1="1" x2="65" y2="5"/>
        <g class="hook-group" data-hook="SessionStart"><rect class="hook-rect" x="160" y="5" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="23" text-anchor="middle">SessionStart</text><text class="fire-count" x="327" y="9" text-anchor="end"></text></g>
        <line class="arrow-line" x1="245" y1="33" x2="245" y2="41" marker-end="url(#ah)"/>
        <g class="hook-group" data-hook="UserPromptSubmit"><rect class="hook-rect" x="160" y="41" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="59" text-anchor="middle">UserPromptSubmit</text><text class="fire-count" x="327" y="45" text-anchor="end"></text></g>
        <line class="arrow-line" x1="245" y1="69" x2="245" y2="105" marker-end="url(#ah)"/>
        <rect class="loop-rect" x="80" y="78" width="340" height="247" rx="6"/>
        <text class="loop-label" x="93" y="93">AGENTIC LOOP</text>
        <g class="hook-group" data-hook="PreToolUse"><rect class="hook-rect" x="160" y="105" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="123" text-anchor="middle">PreToolUse</text><text class="fire-count" x="327" y="109" text-anchor="end"></text></g>
        <line class="arrow-line" x1="245" y1="133" x2="245" y2="141" marker-end="url(#ah)"/>
        <g class="hook-group" data-hook="PermissionRequest"><rect class="hook-rect" x="160" y="141" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="159" text-anchor="middle">PermissionRequest</text><text class="fire-count" x="327" y="145" text-anchor="end"></text></g>
        <line class="arrow-line" x1="245" y1="169" x2="245" y2="177" marker-end="url(#ah)"/>
        <g><rect class="tool-rect" x="170" y="179" width="150" height="20" rx="4"/><text class="tool-text" x="245" y="193" text-anchor="middle" style="font-size:10px">[tool executes]</text></g>
        <line class="arrow-line" x1="245" y1="199" x2="245" y2="213" marker-end="url(#ah)"/>
        <g class="hook-group" data-hooks="PostToolUse,PostToolUseFailure"><rect class="hook-rect" x="120" y="213" width="250" height="28" rx="5"/><text class="hook-text" x="245" y="231" text-anchor="middle">PostToolUse / PostToolUseFailure</text><text class="fire-count" x="367" y="217" text-anchor="end"></text></g>
        <line class="arrow-line" x1="245" y1="241" x2="245" y2="249" marker-end="url(#ah)"/>
        <g class="hook-group" data-hooks="SubagentStart,SubagentStop"><rect class="hook-rect" x="125" y="249" width="240" height="28" rx="5"/><text class="hook-text" x="245" y="267" text-anchor="middle">SubagentStart / SubagentStop</text><text class="fire-count" x="362" y="253" text-anchor="end"></text></g>
        <line class="arrow-line" x1="245" y1="277" x2="245" y2="285" marker-end="url(#ah)"/>
        <g class="hook-group" data-hook="TaskCreated"><rect class="hook-rect hook-rect-side" x="395" y="270" width="100" height="28" rx="5"/><text class="hook-text hook-text-side" x="445" y="282" text-anchor="middle">TaskCreated</text><text class="hook-subtitle" x="445" y="292" text-anchor="middle">(Teams)</text><text class="fire-count" x="492" y="274" text-anchor="end"></text></g>
        <line class="connector-dashed" x1="330" y1="299" x2="395" y2="284"/>
        <g class="hook-group" data-hook="TaskCompleted"><rect class="hook-rect" x="160" y="285" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="303" text-anchor="middle">TaskCompleted</text><text class="fire-count" x="327" y="289" text-anchor="end"></text></g>
        <path class="arrow-line" d="M 330,299 L 365,299 L 365,119 L 340,119"/><polygon points="340,115 330,119 340,123" class="arrow-head"/>
        <line class="arrow-line" x1="245" y1="313" x2="245" y2="335" marker-end="url(#ah)"/>
        <g class="hook-group" data-hooks="Stop,StopFailure"><rect class="hook-rect hook-rect-stop" x="135" y="335" width="220" height="28" rx="5"/><text class="hook-text" x="245" y="353" text-anchor="middle">Stop / StopFailure</text><text class="fire-count" x="352" y="339" text-anchor="end"></text></g>
        <line class="arrow-line" x1="245" y1="363" x2="245" y2="371" marker-end="url(#ah)"/>
        <g class="hook-group" data-hook="TeammateIdle"><rect class="hook-rect" x="160" y="371" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="389" text-anchor="middle">TeammateIdle</text><text class="fire-count" x="327" y="375" text-anchor="end"></text></g>
        <line class="arrow-line" x1="245" y1="399" x2="245" y2="407" marker-end="url(#ah)"/>
        <g class="hook-group" data-hook="PreCompact"><rect class="hook-rect" x="160" y="407" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="425" text-anchor="middle">PreCompact</text><text class="fire-count" x="327" y="411" text-anchor="end"></text></g>
        <line class="arrow-line" x1="245" y1="435" x2="245" y2="443" marker-end="url(#ah)"/>
        <g class="hook-group" data-hook="PostCompact"><rect class="hook-rect" x="160" y="443" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="461" text-anchor="middle">PostCompact</text><text class="fire-count" x="327" y="447" text-anchor="end"></text></g>
        <line class="arrow-line" x1="245" y1="471" x2="245" y2="479" marker-end="url(#ah)"/>
        <g class="hook-group" data-hook="SessionEnd"><rect class="hook-rect" x="160" y="479" width="170" height="28" rx="5"/><text class="hook-text" x="245" y="497" text-anchor="middle">SessionEnd</text><text class="fire-count" x="327" y="483" text-anchor="end"></text></g>
        <path class="arrow-line arrow-dashed" d="M 330,493 L 455,493 L 455,19 L 340,19"/><polygon points="340,15 330,19 340,23" class="arrow-head"/>
        <text class="resume-label" x="463" y="256" text-anchor="middle" transform="rotate(-90,463,256)">resumed sessions</text>
      </svg>
    </div>

    <div id="event-log"><div class="log-header">Event Log</div><div id="log-entries"></div></div>
  </div>
</div>

<script>
const API_BASE = window.location.origin;
let previousState = {};

function addLogEntry(h){var n=new Date().toLocaleTimeString(),e=document.createElement('div');e.textContent=n+' - '+h+' fired';e.style.color='#FFD700';var l=document.getElementById('log-entries');l.appendChild(e);while(l.children.length>50)l.removeChild(l.firstChild);var p=document.getElementById('event-log');p.scrollTop=p.scrollHeight}

async function pollState(){try{var r=await fetch(API_BASE+'/api/state');var s=await r.json();updateVisualization(s);setConnectionStatus(true)}catch(e){setConnectionStatus(false)}setTimeout(pollState,500)}

function updateVisualization(state){
  // Single-hook boxes: detect fire_count changes (not just active transition)
  document.querySelectorAll('[data-hook]').forEach(function(g){
    var h=g.dataset.hook,s=state.hooks?state.hooks[h]:null;if(!s)return;
    var r=g.querySelector('.hook-rect'),t=g.querySelectorAll('.hook-text'),u=g.querySelectorAll('.hook-subtitle'),c=g.querySelector('.fire-count');
    var prevCount=(previousState[h]&&previousState[h].fire_count)||0;
    if(s.active){
      r.classList.add('lit');t.forEach(function(x){x.classList.add('lit')});u.forEach(function(x){x.classList.add('lit')});
      if(s.fire_count>prevCount){
        g.classList.remove('just-fired');void g.offsetWidth;g.classList.add('just-fired');
        for(var i=0;i<s.fire_count-prevCount;i++)addLogEntry(h);
        setTimeout(function(){g.classList.remove('just-fired')},700);
      }
    }else{r.classList.remove('lit');t.forEach(function(x){x.classList.remove('lit')});u.forEach(function(x){x.classList.remove('lit')})}
    if(c&&s.fire_count>0){c.textContent=s.fire_count;c.classList.add('visible')}
  });
  // Combined boxes: detect fire_count changes
  document.querySelectorAll('[data-hooks]').forEach(function(g){
    var hs=g.dataset.hooks.split(',');
    var a=hs.some(function(h){return state.hooks&&state.hooks[h]&&state.hooks[h].active});
    var tc=hs.reduce(function(s,h){return s+(state.hooks&&state.hooks[h]?(state.hooks[h].fire_count||0):0)},0);
    var prevTc=hs.reduce(function(s,h){return s+((previousState[h]&&previousState[h].fire_count)||0)},0);
    var r=g.querySelector('.hook-rect'),t=g.querySelectorAll('.hook-text'),c=g.querySelector('.fire-count');
    if(a){
      r.classList.add('lit');t.forEach(function(x){x.classList.add('lit')});
      if(tc>prevTc){
        g.classList.remove('just-fired');void g.offsetWidth;g.classList.add('just-fired');
        hs.forEach(function(h){
          var cur=(state.hooks&&state.hooks[h])?state.hooks[h].fire_count||0:0;
          var prev=(previousState[h])?previousState[h].fire_count||0:0;
          for(var i=0;i<cur-prev;i++)addLogEntry(h);
        });
        setTimeout(function(){g.classList.remove('just-fired')},700);
      }
    }else{r.classList.remove('lit');t.forEach(function(x){x.classList.remove('lit')})}
    if(c&&tc>0){c.textContent=tc;c.classList.add('visible')}
  });
  // Update card highlights on left panel
  document.querySelectorAll('[data-card-hooks]').forEach(function(card){
    var hooks=card.dataset.cardHooks.split(',');
    var anyActive=hooks.some(function(h){return state.hooks&&state.hooks[h]&&state.hooks[h].active});
    if(anyActive){card.classList.add('card-lit')}
    else{card.classList.remove('card-lit')}
  });
  previousState=state.hooks?JSON.parse(JSON.stringify(state.hooks)):{};
}

function setConnectionStatus(c){document.getElementById('status-dot').style.background=c?'#3fb950':'#f85149';document.getElementById('status-text').textContent=c?'Connected':'Disconnected'}

async function resetHooks(){try{await fetch(API_BASE+'/api/reset',{method:'POST'});previousState={};document.querySelectorAll('.lit').forEach(function(e){e.classList.remove('lit')});document.querySelectorAll('.fire-count').forEach(function(e){e.classList.remove('visible');e.textContent=''});document.querySelectorAll('.card-lit').forEach(function(e){e.classList.remove('card-lit')});document.getElementById('log-entries').innerHTML=''}catch(e){}}

// Resizable divider
(function(){var h=document.getElementById('resize-handle'),rp=document.getElementById('right-panel'),mc=document.querySelector('.main-content'),d=false;
h.addEventListener('mousedown',function(e){e.preventDefault();d=true;h.classList.add('dragging');document.body.style.cursor='col-resize';document.body.style.userSelect='none'});
document.addEventListener('mousemove',function(e){if(!d)return;var cr=mc.getBoundingClientRect(),tw=cr.width,mx=e.clientX-cr.left,rw=tw-mx-4;var mr=tw*0.3;if(rw<mr)rw=mr;if(tw-rw-4<200)return;rp.style.width=(rw/tw*100)+'%'});
document.addEventListener('mouseup',function(){if(d){d=false;h.classList.remove('dragging');document.body.style.cursor='';document.body.style.userSelect=''}})})();

// Copy button SVG + logic
var COPY_SVG='<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="5.5" y="5.5" width="8" height="8" rx="1.5"/><path d="M3.5 10.5h-1a1 1 0 01-1-1v-7a1 1 0 011-1h7a1 1 0 011 1v1"/></svg>';
var CHECK_SVG='<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 8.5l3.5 3.5 6.5-7"/></svg>';
document.querySelectorAll('.copy-btn').forEach(function(b){b.innerHTML=COPY_SVG});
function copyLine(btn){var t=btn.parentElement.querySelector('.prompt-line-text');var txt=t.textContent.replace(/^[$>]\s*/,'');navigator.clipboard.writeText(txt);btn.innerHTML=CHECK_SVG;btn.classList.add('copied');setTimeout(function(){btn.innerHTML=COPY_SVG;btn.classList.remove('copied')},1500)}

document.addEventListener('DOMContentLoaded',pollState);
</script>
</body>
</html>
```

## File: `demo/README.md`
```markdown
# Hooks Lifecycle Demo

Interactive real-time visualization of all 26 Claude Code hooks. As you use Claude Code in the demo directory, hooks light up on a flowchart diagram with sound effects.

## Quick Start

```bash
# Terminal 1 — start the visualization server
cd demo
./start-demo.sh
```

This starts a local server at `http://localhost:3456` and opens it in your browser.

```bash
# Terminal 2 — run Claude Code inside the demo directory
cd demo
claude
```

As you interact with Claude, each hook fires and lights up on the diagram in real-time.

## How It Works

```
demo/
  hooks-lifecycle.html           # Flowchart visualization (polls server for state)
  server.py                      # HTTP server — serves HTML + state API (port 3456)
  start-demo.sh                  # Convenience script — starts server + opens browser
  .claude/
    settings.json                # Hook config — all 26 hooks wired to demo-hooks.py
    hooks/
      scripts/demo-hooks.py      # Hook handler — updates state file + plays sounds
      state/hook-state.json      # Shared state — tracks which hooks have fired
  .mcp.json                      # MCP server config (elicitation)
```

**Flow:** Claude Code fires a hook → `demo-hooks.py` updates `hook-state.json` + plays a sound → the browser polls `/api/state` → the matching hook lights up on the flowchart.

## Components

### Visualization (`hooks-lifecycle.html`)

- SVG flowchart showing the full hook lifecycle
- Hooks glow gold when they fire, with pulse animation
- Fire count badges track how many times each hook has been triggered
- Event log at the bottom shows hook activity in real-time
- Resizable split panel — prompt guide on the left, flowchart on the right

### Server (`server.py`)

- `GET /` — serves the visualization page
- `GET /api/state` — returns current hook state as JSON
- `POST /api/reset` — resets all hooks to inactive

```bash
# Run with custom port
python3 server.py --port 8080
```

### Hook Handler (`demo-hooks.py`)

Receives hook events from Claude Code via stdin, then:
1. Writes the event to `hook-state.json` (atomic file write)
2. Plays the corresponding sound from the parent project's sound files

### Prompts to Try

The left panel of the visualization includes guided prompts to trigger different hooks. Some examples:

- **Basic interaction** — triggers SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop
- **Permission flow** — ask Claude to write a file to trigger PermissionRequest
- **Subagent hooks** — ask Claude to use the Agent tool for SubagentStart/SubagentStop
- **Compaction** — long conversations trigger PreCompact/PostCompact
- **Elicitation** — MCP elicitation triggers Elicitation/ElicitationResult

## Prerequisites

- Python 3
- The parent project's sound files (`.claude/hooks/sounds/`) must exist
- macOS (uses `afplay` for sound playback)

## Reset

Click the **Reset** button in the visualization header, or:

```bash
curl -X POST http://localhost:3456/api/reset
```
```

## File: `demo/server.py`
```python
#!/usr/bin/env python3
"""
HTTP server for the Claude Code Hooks Lifecycle Demo.
Serves the visualization page and hook state API.

Usage: python3 server.py [--port PORT]
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import sys
import argparse
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(BASE_DIR, ".claude", "hooks", "state", "hook-state.json")
HTML_FILE = os.path.join(BASE_DIR, "hooks-lifecycle.html")

ALL_HOOKS = [
    "SessionStart",
    "UserPromptSubmit",
    "PreToolUse",
    "PermissionRequest",
    "PostToolUse",
    "PostToolUseFailure",
    "Notification",
    "Stop",
    "SubagentStart",
    "SubagentStop",
    "PreCompact",
    "PostCompact",
    "SessionEnd",
    "Setup",
    "TeammateIdle",
    "TaskCompleted",
    "ConfigChange",
    "WorktreeCreate",
    "WorktreeRemove",
    "InstructionsLoaded",
    "Elicitation",
    "ElicitationResult",
    "TaskCreated",
    "StopFailure",
    "CwdChanged",
    "FileChanged",
]


def create_initial_state():
    """Return a fresh state dict with all 26 hooks inactive."""
    hooks = {}
    for hook_name in ALL_HOOKS:
        hooks[hook_name] = {
            "active": False,
            "last_fired": None,
            "fire_count": 0,
        }
    return {
        "hooks": hooks,
        "last_updated": None,
    }


def read_state():
    """Read the current hook state from disk."""
    try:
        with open(STATE_FILE, "r") as f:
            state = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return create_initial_state()
    # Backfill any hooks added after the state file was created
    for h in ALL_HOOKS:
        if h not in state.get("hooks", {}):
            state.setdefault("hooks", {})[h] = {
                "active": False,
                "last_fired": None,
                "fire_count": 0,
            }
    return state


def write_state(state):
    """Write state to disk (atomic)."""
    import tempfile

    state_dir = os.path.dirname(STATE_FILE)
    os.makedirs(state_dir, exist_ok=True)
    fd, temp_path = tempfile.mkstemp(dir=state_dir, suffix=".json")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(state, f, indent=2)
        os.replace(temp_path, STATE_FILE)
    except Exception:
        try:
            os.unlink(temp_path)
        except OSError:
            pass
        raise


def reset_state():
    """Reset all hooks to inactive."""
    state = create_initial_state()
    write_state(state)
    return state


class DemoHandler(BaseHTTPRequestHandler):
    """HTTP request handler for the lifecycle demo."""

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.serve_html()
        elif self.path == "/api/state":
            self.serve_state()
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        if self.path == "/api/reset":
            self.handle_reset()
        else:
            self.send_error(404, "Not Found")

    def serve_html(self):
        """Serve the hooks-lifecycle.html file."""
        try:
            with open(HTML_FILE, "r", encoding="utf-8") as f:
                content = f.read()
            body = content.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except FileNotFoundError:
            self.send_error(
                404,
                "hooks-lifecycle.html not found. "
                "Make sure it exists in the demo/ directory.",
            )

    def serve_state(self):
        """Serve the current hook state as JSON."""
        state = read_state()
        body = json.dumps(state).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-cache, no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def handle_reset(self):
        """Reset all hooks to inactive."""
        reset_state()
        body = json.dumps({"status": "ok"}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        """Suppress per-request logging to keep output clean."""
        pass


def main():
    parser = argparse.ArgumentParser(description="Claude Code Hooks Lifecycle Demo Server")
    parser.add_argument("--port", type=int, default=3456, help="Port to listen on (default: 3456)")
    args = parser.parse_args()

    port = args.port

    # Ensure state directory and initial state file exist
    state_dir = os.path.dirname(STATE_FILE)
    os.makedirs(state_dir, exist_ok=True)
    if not os.path.exists(STATE_FILE):
        write_state(create_initial_state())

    server = HTTPServer(("", port), DemoHandler)
    server.socket.setsockopt(__import__('socket').SOL_SOCKET, __import__('socket').SO_REUSEADDR, 1)

    print("==================================")
    print("  Claude Code Hooks Lifecycle Demo")
    print("==================================")
    print(f"  Server: http://localhost:{port}")
    print("")
    print("  Instructions:")
    print(f"  1. Open http://localhost:{port} in your browser")
    print("  2. Open another terminal")
    print("  3. cd to the demo/ directory")
    print("  4. Run: claude")
    print("  5. Watch hooks light up!")
    print("")
    print("  Press Ctrl+C to stop the server.")
    print("==================================")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()
        sys.exit(0)


if __name__ == "__main__":
    main()
```

## File: `demo/start-demo.sh`
```bash
#!/bin/bash
# Claude Code Hooks Lifecycle Demo - Start Script

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "Starting Claude Code Hooks Lifecycle Demo..."
echo ""

# Start the server in the background
python3 server.py &
SERVER_PID=$!

# Wait for server to start
sleep 1

# Check if server started successfully
if ! kill -0 $SERVER_PID 2>/dev/null; then
    echo "ERROR: Server failed to start."
    exit 1
fi

# Open browser (macOS)
if command -v open &>/dev/null; then
    open "http://localhost:3456"
elif command -v xdg-open &>/dev/null; then
    xdg-open "http://localhost:3456"
fi

echo ""
echo "Now open another terminal and run:"
echo "  cd $SCRIPT_DIR"
echo "  claude"
echo ""
echo "Press Ctrl+C to stop the server."

# Wait for server process, forward Ctrl+C
trap "kill $SERVER_PID 2>/dev/null; exit 0" INT TERM
wait $SERVER_PID
```

## File: `install/README-linux.md`
```markdown
# Installation - Linux

[⬅ Back to Main README](../../../README.md)

## Prerequisites

- **Python 3**: Required for running the hook scripts
  - Verify: `python3 --version`
  - Install: `sudo apt install python3` (Ubuntu/Debian) or `sudo yum install python3` (RHEL/CentOS)
- **Audio Player**: `paplay` from `pulseaudio-utils`
  - Install: `sudo apt install pulseaudio-utils`

All details are mentioned in [HOOKS-README.md](../claude_bp_repo/HOOKS-README.md)

---

## Installation

### Step 1: Copy hooks folder

Open terminal in your project directory and run the following commands:

```bash
mkdir -p .claude/hooks
git clone https://github.com/shanraisshan/claude-code-hooks.git temp-hooks
cp -r temp-hooks/.claude/hooks/* .claude/hooks/
rm -rf temp-hooks
```

### Step 2: Copy settings.json keys into your existing Claude settings file

1. If you don't have a `.claude/settings.json` file in your project, create one: `touch .claude/settings.json`
2. Open [`install/settings-linux.json`](settings-linux.json) and copy the keys (`disableAllHooks` and `hooks`) into your `.claude/settings.json`

> **Why separate settings files per platform?**
> - Python command: `python3` (macOS/Linux) vs `python` (Windows)
> - Script path: `${CLAUDE_PROJECT_DIR}` env variable (macOS/Linux) vs relative path (Windows)

### Step 3: Start Claude

Start Claude, you will hear "Claude session start" which is the sound played on startup.

```
claude
```

---

## Optional: Test Agent Hooks

To test the agent-specific hooks (PreToolUse, PostToolUse, Stop), copy the demo agent file:

```bash
mkdir -p .claude/agents
git clone https://github.com/shanraisshan/claude-code-hooks.git temp-hooks
cp temp-hooks/.claude/agents/claude-code-hook-agent.md .claude/agents/
rm -rf temp-hooks
```

After copying, run the agent in Claude Code with:
```
/agents claude-code-hook-agent
```

This agent fetches the weather for Dubai and demonstrates the PreToolUse, PostToolUse, and Stop hooks in action.
```

## File: `install/README-mac.md`
```markdown
# Installation - macOS

[⬅ Back to Main README](../../../README.md)

## Prerequisites

- **Python 3**: Required for running the hook scripts
  - Verify: `python3 --version`
  - Install: `brew install python3` (requires [Homebrew](https://brew.sh/))
- **Audio Player**: `afplay` (built-in, no installation needed)

All details are mentioned in [HOOKS-README.md](../claude_bp_repo/HOOKS-README.md)

---

## Installation

### Step 1: Copy hooks folder

Open terminal in your project directory and run the following commands:

```bash
mkdir -p .claude/hooks
git clone https://github.com/shanraisshan/claude-code-hooks.git temp-hooks
cp -r temp-hooks/.claude/hooks/* .claude/hooks/
rm -rf temp-hooks
```

### Step 2: Copy settings.json keys into your existing Claude settings file

1. If you don't have a `.claude/settings.json` file in your project, create one: `touch .claude/settings.json`
2. Open [`install/settings-mac.json`](settings-mac.json) and copy the keys (`disableAllHooks` and `hooks`) into your `.claude/settings.json`

> **Why separate settings files per platform?**
> - Python command: `python3` (macOS/Linux) vs `python` (Windows)
> - Script path: `${CLAUDE_PROJECT_DIR}` env variable (macOS/Linux) vs relative path (Windows)

### Step 3: Start Claude

Start Claude, you will hear "Claude session start" which is the sound played on startup.

```
claude
```

---

## Optional: Test Agent Hooks

To test the agent-specific hooks (PreToolUse, PostToolUse, Stop), copy the demo agent file:

```bash
mkdir -p .claude/agents
git clone https://github.com/shanraisshan/claude-code-hooks.git temp-hooks
cp temp-hooks/.claude/agents/claude-code-hook-agent.md .claude/agents/
rm -rf temp-hooks
```

After copying, run the agent in Claude Code with:
```
/agents claude-code-hook-agent
```

This agent fetches the weather for Dubai and demonstrates the PreToolUse, PostToolUse, and Stop hooks in action.
```

## File: `install/README-windows.md`
```markdown
# Installation - Windows

[⬅ Back to Main README](../../../README.md)

## Prerequisites

- **Python 3**: Required for running the hook scripts
  - Verify: `python --version`
  - Install: Download from [python.org](https://www.python.org/downloads/) or install via `winget install Python.Python.3`
- **Audio Player**: Built-in `winsound` module (included with Python)

All details are mentioned in [HOOKS-README.md](../claude_bp_repo/HOOKS-README.md)

---

## Installation

### Step 1: Copy hooks folder

Open terminal in your project directory and run the following commands:

**PowerShell:**
```powershell
New-Item -ItemType Directory -Force -Path .claude\hooks
git clone https://github.com/shanraisshan/claude-code-hooks.git temp-hooks
Copy-Item -Recurse -Force temp-hooks\.claude\hooks\* .claude\hooks\
Remove-Item -Recurse -Force temp-hooks
```

**Command Prompt:**
```cmd
if not exist .claude\hooks mkdir .claude\hooks
git clone https://github.com/shanraisshan/claude-code-hooks.git temp-hooks
xcopy /E /I /Y temp-hooks\.claude\hooks\* .claude\hooks\
rmdir /S /Q temp-hooks
```

### Step 2: Copy settings.json keys into your existing Claude settings file

1. If you don't have a `.claude/settings.json` file in your project, create one: `touch .claude/settings.json`
2. Open [`install/settings-windows.json`](settings-windows.json) and copy the keys (`disableAllHooks` and `hooks`) into your `.claude/settings.json`

> **Why separate settings files per platform?**
> - Python command: `python3` (macOS/Linux) vs `python` (Windows)
> - Script path: `${CLAUDE_PROJECT_DIR}` env variable (macOS/Linux) vs relative path (Windows)

### Step 3: Start Claude

Start Claude, you will hear "Claude session start" which is the sound played on startup.

```
claude
```

---

## Optional: Test Agent Hooks

To test the agent-specific hooks (PreToolUse, PostToolUse, Stop), copy the demo agent file:

**PowerShell:**
```powershell
New-Item -ItemType Directory -Force -Path .claude\agents
git clone https://github.com/shanraisshan/claude-code-hooks.git temp-hooks
Copy-Item temp-hooks\.claude\agents\claude-code-hook-agent.md .claude\agents\
Remove-Item -Recurse -Force temp-hooks
```

**Command Prompt:**
```cmd
if not exist .claude\agents mkdir .claude\agents
git clone https://github.com/shanraisshan/claude-code-hooks.git temp-hooks
copy temp-hooks\.claude\agents\claude-code-hook-agent.md .claude\agents\
rmdir /S /Q temp-hooks
```

After copying, run the agent in Claude Code with:
```
/agents claude-code-hook-agent
```

This agent fetches the weather for Dubai and demonstrates the PreToolUse, PostToolUse, and Stop hooks in action.
```

## File: `install/settings-linux.json`
```json
{
  "disableAllHooks": false,
  "hooks": {
    "PreToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PreToolUse"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PermissionRequest"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PostToolUse"
          }
        ]
      }
    ],
    "PostToolUseFailure": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PostToolUseFailure"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "UserPromptSubmit"
          }
        ]
      }
    ],
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "Notification"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "Stop"
          }
        ]
      }
    ],
    "SubagentStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "SubagentStart"
          }
        ]
      }
    ],
    "SubagentStop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "SubagentStop"
          }
        ]
      }
    ],
    "PreCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "once": true,
            "statusMessage": "PreCompact"
          }
        ]
      }
    ],
    "PostCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PostCompact"
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "once": true,
            "statusMessage": "SessionStart"
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "once": true,
            "statusMessage": "SessionEnd"
          }
        ]
      }
    ],
    "Setup": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 30000,
            "async": true,
            "statusMessage": "Setup"
          }
        ]
      }
    ],
    "TeammateIdle": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "TeammateIdle"
          }
        ]
      }
    ],
    "TaskCreated": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "TaskCreated"
          }
        ]
      }
    ],
    "TaskCompleted": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "TaskCompleted"
          }
        ]
      }
    ],
    "ConfigChange": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "ConfigChange"
          }
        ]
      }
    ],
    "WorktreeCreate": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "WorktreeCreate"
          }
        ]
      }
    ],
    "WorktreeRemove": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "WorktreeRemove"
          }
        ]
      }
    ],
    "InstructionsLoaded": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "InstructionsLoaded"
          }
        ]
      }
    ],
    "Elicitation": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "Elicitation"
          }
        ]
      }
    ],
    "ElicitationResult": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "ElicitationResult"
          }
        ]
      }
    ],
    "StopFailure": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "StopFailure"
          }
        ]
      }
    ],
    "CwdChanged": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "CwdChanged"
          }
        ]
      }
    ],
    "FileChanged": [
      {
        "matcher": ".envrc|.env|.env.local",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "FileChanged"
          }
        ]
      }
    ]
  }
}
```

## File: `install/settings-mac.json`
```json
{
  "disableAllHooks": false,
  "hooks": {
    "PreToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PreToolUse"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PermissionRequest"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PostToolUse"
          }
        ]
      }
    ],
    "PostToolUseFailure": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PostToolUseFailure"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "UserPromptSubmit"
          }
        ]
      }
    ],
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "Notification"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "Stop"
          }
        ]
      }
    ],
    "SubagentStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "SubagentStart"
          }
        ]
      }
    ],
    "SubagentStop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "SubagentStop"
          }
        ]
      }
    ],
    "PreCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "once": true,
            "statusMessage": "PreCompact"
          }
        ]
      }
    ],
    "PostCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PostCompact"
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "once": true,
            "statusMessage": "SessionStart"
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "once": true,
            "statusMessage": "SessionEnd"
          }
        ]
      }
    ],
    "Setup": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 30000,
            "async": true,
            "statusMessage": "Setup"
          }
        ]
      }
    ],
    "TeammateIdle": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "TeammateIdle"
          }
        ]
      }
    ],
    "TaskCreated": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "TaskCreated"
          }
        ]
      }
    ],
    "TaskCompleted": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "TaskCompleted"
          }
        ]
      }
    ],
    "ConfigChange": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "ConfigChange"
          }
        ]
      }
    ],
    "WorktreeCreate": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "WorktreeCreate"
          }
        ]
      }
    ],
    "WorktreeRemove": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "WorktreeRemove"
          }
        ]
      }
    ],
    "InstructionsLoaded": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "InstructionsLoaded"
          }
        ]
      }
    ],
    "Elicitation": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "Elicitation"
          }
        ]
      }
    ],
    "ElicitationResult": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "ElicitationResult"
          }
        ]
      }
    ],
    "StopFailure": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "StopFailure"
          }
        ]
      }
    ],
    "CwdChanged": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "CwdChanged"
          }
        ]
      }
    ],
    "FileChanged": [
      {
        "matcher": ".envrc|.env|.env.local",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "FileChanged"
          }
        ]
      }
    ]
  }
}
```

## File: `install/settings-windows.json`
```json
{
  "disableAllHooks": false,
  "hooks": {
    "PreToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PreToolUse"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PermissionRequest"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PostToolUse"
          }
        ]
      }
    ],
    "PostToolUseFailure": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PostToolUseFailure"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "UserPromptSubmit"
          }
        ]
      }
    ],
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "Notification"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "Stop"
          }
        ]
      }
    ],
    "SubagentStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "SubagentStart"
          }
        ]
      }
    ],
    "SubagentStop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "SubagentStop"
          }
        ]
      }
    ],
    "PreCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "once": true,
            "statusMessage": "PreCompact"
          }
        ]
      }
    ],
    "PostCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "PostCompact"
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "once": true,
            "statusMessage": "SessionStart"
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "once": true,
            "statusMessage": "SessionEnd"
          }
        ]
      }
    ],
    "Setup": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 30000,
            "async": true,
            "statusMessage": "Setup"
          }
        ]
      }
    ],
    "TeammateIdle": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "TeammateIdle"
          }
        ]
      }
    ],
    "TaskCreated": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "TaskCreated"
          }
        ]
      }
    ],
    "TaskCompleted": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "TaskCompleted"
          }
        ]
      }
    ],
    "ConfigChange": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "ConfigChange"
          }
        ]
      }
    ],
    "WorktreeCreate": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "WorktreeCreate"
          }
        ]
      }
    ],
    "WorktreeRemove": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "WorktreeRemove"
          }
        ]
      }
    ],
    "InstructionsLoaded": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "InstructionsLoaded"
          }
        ]
      }
    ],
    "Elicitation": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "Elicitation"
          }
        ]
      }
    ],
    "ElicitationResult": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "ElicitationResult"
          }
        ]
      }
    ],
    "StopFailure": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "StopFailure"
          }
        ]
      }
    ],
    "CwdChanged": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "CwdChanged"
          }
        ]
      }
    ],
    "FileChanged": [
      {
        "matcher": ".envrc|.env|.env.local",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/scripts/hooks.py",
            "timeout": 5000,
            "async": true,
            "statusMessage": "FileChanged"
          }
        ]
      }
    ]
  }
}
```

## File: `plans/add-new-hooks-teammate-idle-task-completed.md`
```markdown
# Plan: Add TeammateIdle and TaskCompleted Hooks

## Background

Claude Code v2.1.33 introduced two new hook events for multi-agent workflows:
- **TeammateIdle** - Fires when a teammate agent becomes idle in agent teams
- **TaskCompleted** - Fires when a background task completes

These are tied to the experimental agent teams feature (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`). Our repo currently supports all 13 established hooks but is missing these two new ones.

## Scope

Add full support for both hooks across all configuration files, scripts, sounds, and documentation — matching the existing pattern used by the other 13 hooks.

---

## Step 1: Add Sound Files

Create sound directories and generate TTS audio files (ElevenLabs, Samara X voice):

```
.claude/hooks/sounds/teammateidle/
  teammateidle.wav
  teammateidle.mp3

.claude/hooks/sounds/taskcompleted/
  taskcompleted.wav
  taskcompleted.mp3
```

**TTS phrases to generate:**
- TeammateIdle: "Teammate idle" or "Teammate is idle"
- TaskCompleted: "Task completed"

---

## Step 2: Update `.claude/settings.json` (macOS/Linux)

Add two new hook entries after the existing `Setup` hook:

```json
"TeammateIdle": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
        "timeout": 5000,
        "async": true,
        "statusMessage": "TeammateIdle"
      }
    ]
  }
],
"TaskCompleted": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python3 ${CLAUDE_PROJECT_DIR}/.claude/hooks/scripts/hooks.py",
        "timeout": 5000,
        "async": true,
        "statusMessage": "TaskCompleted"
      }
    ]
  }
]
```

---

## Step 3: Update `.claude/settings-windows.json`

Same as Step 2 but using `python` and relative path:

```json
"TeammateIdle": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python .claude/hooks/scripts/hooks.py",
        "timeout": 5000,
        "async": true,
        "statusMessage": "TeammateIdle"
      }
    ]
  }
],
"TaskCompleted": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "python .claude/hooks/scripts/hooks.py",
        "timeout": 5000,
        "async": true,
        "statusMessage": "TaskCompleted"
      }
    ]
  }
]
```

---

## Step 4: Update `.claude/hooks/config/hooks-config.json`

Add two new toggle flags:

```json
"disableTeammateIdleHook": false,
"disableTaskCompletedHook": false
```

---

## Step 5: Update `.claude/hooks/scripts/hooks.py`

### 5a: Add new event-to-disable mapping

In the config mapping section, add:

```python
"TeammateIdle": "disableTeammateIdleHook",
"TaskCompleted": "disableTaskCompletedHook",
```

### 5b: Add sound file resolution

Ensure the script maps the new event names to their sound directories:
- `"TeammateIdle"` -> `sounds/teammateidle/teammateidle.wav`
- `"TaskCompleted"` -> `sounds/taskcompleted/taskcompleted.wav`

The existing `event_name.lower()` logic should handle this automatically if the directory and file names follow the lowercase convention.

---

## Step 6: Update Documentation

### 6a: `.claude/hooks/HOOKS-README.md`

- Update the hook count from **13** to **15** in the heading and overview
- Add entries 14 and 15 to the numbered list:
  ```
  14. TeammateIdle: Runs when a teammate agent becomes idle (agent teams)
  15. TaskCompleted: Runs when a background task completes
  ```
- Update the shared configuration example to include the two new disable flags
- Add a note that these hooks require the experimental agent teams feature

### 6b: `README.md`

- Update "all 13 hooks" references to "all 15 hooks" throughout
- Add the two new hooks to both macOS/Linux and Windows inline JSON examples
- Update the Features section count

---

## Step 7: Verify

- [ ] Sound files exist in correct directories with both `.wav` and `.mp3` formats
- [ ] `settings.json` has 15 hook entries with `statusMessage`
- [ ] `settings-windows.json` has 15 hook entries with `statusMessage`
- [ ] `hooks-config.json` has 15 disable flags
- [ ] `hooks.py` handles both new event names
- [ ] `HOOKS-README.md` documents 15 hooks
- [ ] `README.md` references 15 hooks
- [ ] Test with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` if possible

---

## How to Enable Agent Teams (Required for These Hooks)

The `TeammateIdle` and `TaskCompleted` hooks only fire when the experimental agent teams feature is active. You must set the environment variable `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` when launching Claude Code.

### Option A: Set inline when launching Claude Code

**macOS/Linux:**
```bash
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude
```

**Windows (PowerShell):**
```powershell
$env:CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS="1"; claude
```

**Windows (Command Prompt):**
```cmd
set CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 && claude
```

### Option B: Export in your shell profile (persistent across sessions)

**macOS/Linux** - add to `~/.bashrc`, `~/.zshrc`, or equivalent:
```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```
Then restart your terminal or run `source ~/.zshrc` (or `~/.bashrc`).

**Windows** - set as a core/user environment variable:
```powershell
[System.Environment]::SetEnvironmentVariable("CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS", "1", "User")
```
Then restart your terminal.

### Option C: Add to `.claude/settings.local.json` env block

If your Claude Code version supports environment variables in settings, you can add:
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### Verifying It Works

Once agent teams are enabled, you can trigger the hooks by:
1. Starting a session that spawns teammate agents
2. `TeammateIdle` will fire when a teammate agent finishes its work and becomes idle
3. `TaskCompleted` will fire when a background task finishes

Without the environment variable set, these two hooks will simply never fire (but they won't cause errors either — they just remain dormant).

---

## Notes

- These hooks are part of an **experimental** feature (agent teams). They may change in future releases.
- The `TeammateIdle` and `TaskCompleted` hooks were introduced in v2.1.33 release notes with matcher support for multi-agent workflows.
- Until the feature is stable, consider adding a note in documentation that these two hooks require the experimental flag.
```

## File: `presentation/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Presentation - Claude Code Hooks</title>
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 90' width='140' height='126'%3E%3Cstyle%3E.claude-body%7Banimation:jump .5s ease-in-out infinite;transform-origin:center bottom%7D.shadow%7Banimation:shadow-scale .5s ease-in-out infinite%7D.left-arm%7Banimation:wave-left .5s ease-in-out infinite;transform-origin:right center%7D.right-arm%7Banimation:wave-right .5s ease-in-out infinite;transform-origin:left center%7D.left-ear%7Banimation:ear-bounce .5s ease-in-out infinite;transform-origin:center bottom%7D.right-ear%7Banimation:ear-bounce .5s ease-in-out infinite .1s;transform-origin:center bottom%7D@keyframes jump%7B0%25,100%25%7Btransform:translateY(0) scaleY(1) scaleX(1)%7D30%25%7Btransform:translateY(-16px) scaleY(1.1) scaleX(.95)%7D50%25%7Btransform:translateY(-18px) scaleY(1.05) scaleX(.98)%7D80%25%7Btransform:translateY(-5px) scaleY(.95) scaleX(1.05)%7D%7D@keyframes shadow-scale%7B0%25,100%25%7Btransform:scaleX(1);opacity:.25%7D50%25%7Btransform:scaleX(.4);opacity:.08%7D%7D@keyframes wave-left%7B0%25,100%25%7Btransform:rotate(0)%7D50%25%7Btransform:rotate(-25deg)%7D%7D@keyframes wave-right%7B0%25,100%25%7Btransform:rotate(0)%7D50%25%7Btransform:rotate(25deg)%7D%7D@keyframes ear-bounce%7B0%25,100%25%7Btransform:scaleY(1)%7D40%25%7Btransform:scaleY(1.2)%7D60%25%7Btransform:scaleY(.85)%7D%7D%3C/style%3E%3Cellipse class='shadow' cx='50' cy='82' rx='22' ry='5' fill='%23000'/%3E%3Cg class='claude-body'%3E%3Crect class='left-ear' x='22' y='10' width='8' height='14' fill='%23E07C4C'/%3E%3Crect class='right-ear' x='70' y='10' width='8' height='14' fill='%23E07C4C'/%3E%3Crect x='18' y='24' width='64' height='4' fill='%23E07C4C'/%3E%3Crect x='14' y='28' width='72' height='32' fill='%23E07C4C'/%3E%3Crect x='30' y='34' width='8' height='10' fill='%23000'/%3E%3Crect x='62' y='34' width='8' height='10' fill='%23000'/%3E%3Crect class='left-arm' x='2' y='36' width='12' height='8' fill='%23E07C4C'/%3E%3Crect class='right-arm' x='86' y='36' width='12' height='8' fill='%23E07C4C'/%3E%3Crect x='24' y='60' width='12' height='14' fill='%23E07C4C'/%3E%3Crect x='64' y='60' width='12' height='14' fill='%23E07C4C'/%3E%3C/g%3E%3C/svg%3E">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: #ffffff;
            color: #1a1a1a;
            line-height: 1.6;
        }

        .slide {
            display: none;
            min-height: 100vh;
            padding: 60px 80px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .slide.active {
            display: block;
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 600;
            margin-bottom: 40px;
            color: #1a1a1a;
            border-bottom: 2px solid #e5e5e5;
            padding-bottom: 20px;
        }

        h2 {
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 24px;
            color: #2a2a2a;
        }

        h3 {
            font-size: 1.3rem;
            font-weight: 600;
            margin: 24px 0 12px 0;
            color: #333;
        }

        p {
            font-size: 1.1rem;
            margin-bottom: 16px;
            color: #444;
        }

        .hook-number {
            display: inline-block;
            width: 36px;
            height: 36px;
            background: #1a1a1a;
            color: #fff;
            border-radius: 50%;
            text-align: center;
            line-height: 36px;
            font-weight: 600;
            margin-right: 12px;
            font-size: 1rem;
        }

        .hook-title {
            display: flex;
            align-items: center;
            margin-bottom: 24px;
        }

        .hook-name {
            font-family: 'SF Mono', Monaco, 'Courier New', monospace;
            font-size: 1.8rem;
            font-weight: 600;
            color: #1a1a1a;
        }

        .trigger-box {
            background: #f8f9fa;
            border-left: 4px solid #1a1a1a;
            padding: 20px 24px;
            margin: 24px 0;
        }

        .trigger-box h4 {
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #666;
            margin-bottom: 8px;
        }

        .trigger-box p {
            font-size: 1.05rem;
            color: #333;
            margin: 0;
        }

        .use-cases {
            margin: 32px 0;
        }

        .use-case-item {
            display: flex;
            align-items: flex-start;
            margin-bottom: 16px;
            padding: 16px 20px;
            background: #fafafa;
            border-radius: 8px;
        }

        .use-case-icon {
            font-size: 1.5rem;
            margin-right: 16px;
            min-width: 32px;
        }

        .use-case-text {
            flex: 1;
        }

        .use-case-text strong {
            display: block;
            font-size: 1.05rem;
            color: #1a1a1a;
            margin-bottom: 4px;
        }

        .use-case-text span {
            font-size: 0.95rem;
            color: #666;
        }

        .code-block {
            background: #1a1a1a;
            color: #e5e5e5;
            padding: 20px 24px;
            border-radius: 8px;
            font-family: 'SF Mono', Monaco, 'Courier New', monospace;
            font-size: 0.9rem;
            overflow-x: auto;
            margin: 20px 0;
        }

        .code-block .comment {
            color: #6a9955;
        }

        .code-block .key {
            color: #9cdcfe;
        }

        .code-block .string {
            color: #ce9178;
        }

        .navigation {
            position: fixed;
            bottom: 30px;
            right: 30px;
            display: flex;
            gap: 12px;
            z-index: 100;
        }

        .nav-btn {
            width: 50px;
            height: 50px;
            border: 2px solid #1a1a1a;
            background: #fff;
            border-radius: 50%;
            cursor: pointer;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }

        .nav-btn:hover {
            background: #1a1a1a;
            color: #fff;
        }

        .nav-btn:disabled {
            opacity: 0.3;
            cursor: not-allowed;
        }

        .progress {
            position: fixed;
            top: 0;
            left: 0;
            height: 4px;
            background: #1a1a1a;
            transition: width 0.3s;
        }

        .slide-counter {
            position: fixed;
            bottom: 40px;
            left: 40px;
            font-size: 0.9rem;
            color: #999;
        }

        .toc-list {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-top: 32px;
        }

        .toc-item {
            display: flex;
            align-items: center;
            padding: 16px 20px;
            background: #f8f9fa;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .toc-item:hover {
            background: #eee;
        }

        .toc-number {
            width: 28px;
            height: 28px;
            background: #1a1a1a;
            color: #fff;
            border-radius: 50%;
            text-align: center;
            line-height: 28px;
            font-size: 0.85rem;
            margin-right: 12px;
            font-weight: 600;
        }

        .toc-name {
            font-family: 'SF Mono', Monaco, 'Courier New', monospace;
            font-size: 1rem;
            color: #1a1a1a;
        }

        .lifecycle-diagram {
            background: #f8f9fa;
            padding: 32px;
            border-radius: 8px;
            margin: 24px 0;
        }

        .lifecycle-step {
            display: flex;
            align-items: center;
            margin-bottom: 16px;
        }

        .lifecycle-arrow {
            width: 24px;
            text-align: center;
            color: #999;
            margin-right: 16px;
        }

        .lifecycle-label {
            font-family: 'SF Mono', Monaco, 'Courier New', monospace;
            padding: 8px 16px;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 0.95rem;
        }

        .lifecycle-label.highlight {
            background: #1a1a1a;
            color: #fff;
            border-color: #1a1a1a;
        }

        .sound-demo {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            background: #f0f0f0;
            border-radius: 20px;
            font-size: 0.9rem;
            color: #666;
            margin-top: 16px;
        }

        .can-block {
            display: inline-block;
            padding: 4px 12px;
            background: #d4edda;
            color: #155724;
            border-radius: 4px;
            font-size: 0.85rem;
            margin-left: 12px;
        }

        .cannot-block {
            display: inline-block;
            padding: 4px 12px;
            background: #f8d7da;
            color: #721c24;
            border-radius: 4px;
            font-size: 0.85rem;
            margin-left: 12px;
        }

        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
            margin: 24px 0;
        }

        .info-card {
            background: #f8f9fa;
            padding: 24px;
            border-radius: 8px;
        }

        .info-card h4 {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #666;
            margin-bottom: 12px;
        }

        .keyboard-hint {
            position: fixed;
            bottom: 40px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 0.85rem;
            color: #999;
        }

        .keyboard-hint kbd {
            background: #f0f0f0;
            padding: 4px 8px;
            border-radius: 4px;
            border: 1px solid #ddd;
            font-family: inherit;
        }

        .intro-subtitle {
            font-size: 1.3rem;
            color: #666;
            margin-bottom: 40px;
        }

        .feature-list {
            list-style: none;
            margin: 24px 0;
        }

        .feature-list li {
            padding: 12px 0;
            border-bottom: 1px solid #eee;
            font-size: 1.05rem;
        }

        .feature-list li:last-child {
            border-bottom: none;
        }

        .matcher-values {
            margin: 16px 0;
        }

        .matcher-tag {
            display: inline-block;
            padding: 4px 10px;
            background: #e9ecef;
            border-radius: 4px;
            font-family: 'SF Mono', Monaco, 'Courier New', monospace;
            font-size: 0.85rem;
            margin: 4px 4px 4px 0;
            color: #495057;
        }

        .how-to-trigger {
            background: #e8f5e9;
            border-left: 4px solid #4caf50;
            padding: 20px 24px;
            margin: 16px 0 24px 0;
        }

        .how-to-trigger h4 {
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #2e7d32;
            margin-bottom: 8px;
        }

        .how-to-trigger p {
            font-size: 1.05rem;
            color: #1b5e20;
            margin: 0;
        }

        .how-to-trigger code {
            background: rgba(0,0,0,0.08);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'SF Mono', Monaco, 'Courier New', monospace;
            font-size: 0.95rem;
        }

        .trigger-example {
            margin-top: 12px;
            padding: 12px 16px;
            background: rgba(255,255,255,0.7);
            border-radius: 6px;
            font-family: 'SF Mono', Monaco, 'Courier New', monospace;
            font-size: 0.9rem;
            color: #333;
        }

        .header-logo {
            position: fixed;
            top: 20px;
            right: 40px;
            width: 140px;
            height: 90px;
            z-index: 50;
        }

        .header-logo svg {
            width: 100%;
            height: 100%;
        }

        /* Title Slide Styling */
        .slide.title-slide.active {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            text-align: center;
            padding: 40px;
        }

        .title-slide h1 {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 20px;
            border-bottom: none;
            padding-bottom: 0;
        }

        .title-slide .subtitle {
            font-size: 1.4rem;
            color: #555;
            margin-bottom: 50px;
            font-weight: 400;
        }

        .title-logo {
            width: 280px;
            height: 180px;
            margin-bottom: 40px;
        }

        .title-logo svg {
            width: 100%;
            height: 100%;
        }
    </style>
</head>
<body>
    <div class="progress" id="progress"></div>

    <!-- Slide 1: Title -->
    <div class="slide active title-slide" data-slide="1">
        <div class="title-logo">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 90" width="280" height="180">
                <style>
                    .tl-claude-body { animation: tl-bob 0.8s ease-in-out infinite; transform-origin: center bottom; }
                    .tl-shadow { animation: tl-shadow-pulse 0.8s ease-in-out infinite; }
                    .tl-mouth { animation: tl-talk 0.3s ease-in-out infinite; transform-origin: center center; }
                    .tl-left-ear { animation: tl-ear-tilt-left 0.8s ease-in-out infinite; transform-origin: center bottom; }
                    .tl-right-ear { animation: tl-ear-tilt-right 0.8s ease-in-out infinite; transform-origin: center bottom; }
                    .tl-wave-1 { animation: tl-wave-expand 0.8s ease-out infinite; transform-origin: left center; }
                    .tl-wave-2 { animation: tl-wave-expand 0.8s ease-out infinite 0.2s; transform-origin: left center; }
                    .tl-wave-3 { animation: tl-wave-expand 0.8s ease-out infinite 0.4s; transform-origin: left center; }
                    .tl-note-1 { animation: tl-float-note-1 1.5s ease-out infinite; }
                    .tl-note-2 { animation: tl-float-note-2 1.5s ease-out infinite 0.3s; }
                    .tl-note-3 { animation: tl-float-note-3 1.5s ease-out infinite 0.6s; }
                    @keyframes tl-bob { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-3px); } }
                    @keyframes tl-shadow-pulse { 0%, 100% { transform: scaleX(1); opacity: 0.25; } 50% { transform: scaleX(0.9); opacity: 0.2; } }
                    @keyframes tl-talk { 0%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.5); } }
                    @keyframes tl-ear-tilt-left { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(-5deg); } }
                    @keyframes tl-ear-tilt-right { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(5deg); } }
                    @keyframes tl-wave-expand { 0% { opacity: 0.8; transform: scaleX(0.3) scaleY(0.8); } 100% { opacity: 0; transform: scaleX(1.2) scaleY(1); } }
                    @keyframes tl-float-note-1 { 0% { opacity: 1; transform: translate(0, 0) rotate(0deg); } 100% { opacity: 0; transform: translate(15px, -25px) rotate(15deg); } }
                    @keyframes tl-float-note-2 { 0% { opacity: 1; transform: translate(0, 0) rotate(0deg); } 100% { opacity: 0; transform: translate(20px, -30px) rotate(-10deg); } }
                    @keyframes tl-float-note-3 { 0% { opacity: 1; transform: translate(0, 0) rotate(0deg); } 100% { opacity: 0; transform: translate(10px, -35px) rotate(20deg); } }
                </style>
                <ellipse class="tl-shadow" cx="50" cy="82" rx="22" ry="5" fill="#000"/>
                <g class="tl-wave-1"><path d="M 92 44 Q 100 44, 100 52 Q 100 60, 92 60" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
                <g class="tl-wave-2"><path d="M 96 38 Q 108 38, 108 52 Q 108 66, 96 66" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
                <g class="tl-wave-3"><path d="M 100 32 Q 116 32, 116 52 Q 116 72, 100 72" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
                <g class="tl-note-1"><ellipse cx="108" cy="28" rx="4" ry="3" fill="#E07C4C" transform="rotate(-20, 108, 28)"/><rect x="111" y="12" width="2" height="16" fill="#E07C4C"/><path d="M 113 12 Q 118 14, 118 18 Q 118 22, 113 20" fill="#E07C4C"/></g>
                <g class="tl-note-2"><ellipse cx="122" cy="22" rx="4" ry="3" fill="#E07C4C" transform="rotate(-20, 122, 22)"/><rect x="125" y="6" width="2" height="16" fill="#E07C4C"/></g>
                <g class="tl-note-3"><ellipse cx="115" cy="42" rx="3" ry="2.5" fill="#E07C4C" transform="rotate(-20, 115, 42)"/><ellipse cx="125" cy="40" rx="3" ry="2.5" fill="#E07C4C" transform="rotate(-20, 125, 40)"/><rect x="117" y="26" width="2" height="16" fill="#E07C4C"/><rect x="127" y="24" width="2" height="16" fill="#E07C4C"/><rect x="117" y="26" width="12" height="2" fill="#E07C4C"/></g>
                <g class="tl-claude-body">
                    <rect class="tl-left-ear" x="22" y="10" width="8" height="14" fill="#E07C4C"/>
                    <rect class="tl-right-ear" x="70" y="10" width="8" height="14" fill="#E07C4C"/>
                    <rect x="18" y="24" width="64" height="4" fill="#E07C4C"/>
                    <rect x="14" y="28" width="72" height="32" fill="#E07C4C"/>
                    <rect x="30" y="34" width="8" height="10" fill="#000000"/>
                    <rect x="62" y="34" width="8" height="10" fill="#000000"/>
                    <rect class="tl-mouth" x="44" y="50" width="12" height="6" fill="#000000"/>
                    <rect x="2" y="40" width="12" height="8" fill="#E07C4C"/>
                    <rect x="86" y="40" width="12" height="8" fill="#E07C4C"/>
                    <rect x="24" y="60" width="12" height="14" fill="#E07C4C"/>
                    <rect x="64" y="60" width="12" height="14" fill="#E07C4C"/>
                </g>
            </svg>
        </div>
        <h1>Claude Code Hooks</h1>
        <p class="subtitle">Explaining Claude Code Hooks and Subagent Hooks</p>
        <p style="margin-top: 60px; font-size: 0.95rem; color: #888;">As of Claude Code v2.1.87 | March 29, 2026</p>
    </div>

    <!-- Slide 2: Introduction -->
    <div class="slide" data-slide="2">
        <h1>What You'll Learn</h1>

        <div class="trigger-box">
            <h4>Why Hooks Matter</h4>
            <p>Hooks are one of the most powerful features introduced in Claude Code — they let you run custom code at specific moments in Claude's workflow.</p>
        </div>

        <h3>In This Video</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔢</span>
                <div class="use-case-text">
                    <strong>26 Hooks Explained</strong>
                    <span>Claude Code currently supports 26 hooks (as of v2.1.87)</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🎯</span>
                <div class="use-case-text">
                    <strong>When Each Hook Triggers</strong>
                    <span>Learn the exact moment each hook fires in Claude's workflow</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">💡</span>
                <div class="use-case-text">
                    <strong>Practical Use Cases</strong>
                    <span>Real-world examples of what you can build with each hook</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice Notifications Demo</strong>
                    <span>This repo integrates all 26 hooks with audio feedback</span>
                </div>
            </div>
        </div>

        <h3>What Hooks Enable</h3>
        <ul class="feature-list">
            <li>🤖 Automate repetitive tasks (auto-format code, run tests)</li>
            <li>🛡️ Add safety guardrails (block dangerous commands)</li>
            <li>🔔 Get audio/visual feedback while Claude works</li>
            <li>📎 Inject context dynamically based on what Claude is doing</li>
        </ul>
    </div>

    <!-- Slide 3: Table of Contents -->
    <div class="slide" data-slide="3">
        <h1>The 26 Hooks</h1>
        <p style="margin-top: -30px; margin-bottom: 24px; font-size: 1rem; color: #666;">Claude Code v2.1.87 | March 29, 2026 — More hooks may be added in future versions.</p>

        <div class="toc-list">
            <div class="toc-item" onclick="goToSlide(5)">
                <span class="toc-number">1</span>
                <span class="toc-name">SessionStart</span>
            </div>
            <div class="toc-item" onclick="goToSlide(6)">
                <span class="toc-number">2</span>
                <span class="toc-name">UserPromptSubmit</span>
            </div>
            <div class="toc-item" onclick="goToSlide(7)">
                <span class="toc-number">3</span>
                <span class="toc-name">PreToolUse</span>
            </div>
            <div class="toc-item" onclick="goToSlide(8)">
                <span class="toc-number">4</span>
                <span class="toc-name">PostToolUse</span>
            </div>
            <div class="toc-item" onclick="goToSlide(9)">
                <span class="toc-number">5</span>
                <span class="toc-name">PostToolUseFailure</span>
            </div>
            <div class="toc-item" onclick="goToSlide(10)">
                <span class="toc-number">6</span>
                <span class="toc-name">PermissionRequest</span>
            </div>
            <div class="toc-item" onclick="goToSlide(11)">
                <span class="toc-number">7</span>
                <span class="toc-name">Notification</span>
            </div>
            <div class="toc-item" onclick="goToSlide(12)">
                <span class="toc-number">8</span>
                <span class="toc-name">SubagentStart</span>
            </div>
            <div class="toc-item" onclick="goToSlide(13)">
                <span class="toc-number">9</span>
                <span class="toc-name">SubagentStop</span>
            </div>
            <div class="toc-item" onclick="goToSlide(14)">
                <span class="toc-number">10</span>
                <span class="toc-name">Stop</span>
            </div>
            <div class="toc-item" onclick="goToSlide(15)">
                <span class="toc-number">11</span>
                <span class="toc-name">PreCompact</span>
            </div>
            <div class="toc-item" onclick="goToSlide(16)">
                <span class="toc-number">12</span>
                <span class="toc-name">PostCompact</span>
            </div>
            <div class="toc-item" onclick="goToSlide(17)">
                <span class="toc-number">13</span>
                <span class="toc-name">SessionEnd</span>
            </div>
            <div class="toc-item" onclick="goToSlide(18)">
                <span class="toc-number">14</span>
                <span class="toc-name">Setup</span>
            </div>
            <div class="toc-item" onclick="goToSlide(19)">
                <span class="toc-number">15</span>
                <span class="toc-name">TeammateIdle</span>
            </div>
            <div class="toc-item" onclick="goToSlide(20)">
                <span class="toc-number">16</span>
                <span class="toc-name">TaskCompleted</span>
            </div>
            <div class="toc-item" onclick="goToSlide(21)">
                <span class="toc-number">17</span>
                <span class="toc-name">TaskCreated</span>
            </div>
            <div class="toc-item" onclick="goToSlide(22)">
                <span class="toc-number">18</span>
                <span class="toc-name">ConfigChange</span>
            </div>
            <div class="toc-item" onclick="goToSlide(23)">
                <span class="toc-number">19</span>
                <span class="toc-name">WorktreeCreate</span>
            </div>
            <div class="toc-item" onclick="goToSlide(24)">
                <span class="toc-number">20</span>
                <span class="toc-name">WorktreeRemove</span>
            </div>
            <div class="toc-item" onclick="goToSlide(25)">
                <span class="toc-number">21</span>
                <span class="toc-name">InstructionsLoaded</span>
            </div>
            <div class="toc-item" onclick="goToSlide(26)">
                <span class="toc-number">22</span>
                <span class="toc-name">Elicitation</span>
            </div>
            <div class="toc-item" onclick="goToSlide(27)">
                <span class="toc-number">23</span>
                <span class="toc-name">ElicitationResult</span>
            </div>
            <div class="toc-item" onclick="goToSlide(28)">
                <span class="toc-number">24</span>
                <span class="toc-name">StopFailure</span>
            </div>
            <div class="toc-item" onclick="goToSlide(29)">
                <span class="toc-number">25</span>
                <span class="toc-name">CwdChanged</span>
            </div>
            <div class="toc-item" onclick="goToSlide(30)">
                <span class="toc-number">26</span>
                <span class="toc-name">FileChanged</span>
            </div>
        </div>
    </div>

    <!-- Slide 4: Lifecycle Overview -->
    <div class="slide" data-slide="4">
        <h1>Hook Execution Flow</h1>
        <p>Hooks fire at specific points in Claude's workflow. Here's the execution order:</p>

        <div class="lifecycle-diagram">
            <div style="margin-bottom: 12px; padding: 12px 16px; background: #e8f4f8; border-left: 4px solid #17a2b8; border-radius: 4px;">
                <strong style="font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; color: #0c5460;">Separate trigger — <code>claude --init</code> / <code>--maintenance</code></strong>
                <div style="margin-top: 8px;">
                    <span class="matcher-tag">Setup</span>
                </div>
            </div>
            <div class="lifecycle-step">
                <span class="lifecycle-arrow">→</span>
                <span class="lifecycle-label highlight">SessionStart</span>
                <span style="margin-left: 16px; color: #666;">Session begins or resumes</span>
            </div>
            <div class="lifecycle-step">
                <span class="lifecycle-arrow">↓</span>
                <span class="lifecycle-label highlight">UserPromptSubmit</span>
                <span style="margin-left: 16px; color: #666;">User sends a message</span>
            </div>
            <div class="lifecycle-step">
                <span class="lifecycle-arrow">↓</span>
                <span class="lifecycle-label">PreToolUse</span>
                <span style="margin-left: 16px; color: #666;">Before each tool runs</span>
            </div>
            <div class="lifecycle-step">
                <span class="lifecycle-arrow">↓</span>
                <span class="lifecycle-label">PermissionRequest</span>
                <span style="margin-left: 16px; color: #666;">If permission needed</span>
            </div>
            <div class="lifecycle-step">
                <span class="lifecycle-arrow">↓</span>
                <span class="lifecycle-label">PostToolUse / PostToolUseFailure</span>
                <span style="margin-left: 16px; color: #666;">After tool completes</span>
            </div>
            <div class="lifecycle-step">
                <span class="lifecycle-arrow">↓</span>
                <span class="lifecycle-label">SubagentStart → SubagentStop</span>
                <span style="margin-left: 16px; color: #666;">If subagent spawned</span>
            </div>
            <div class="lifecycle-step">
                <span class="lifecycle-arrow">↓</span>
                <span class="lifecycle-label highlight">Stop</span>
                <span style="margin-left: 16px; color: #666;">Claude finishes responding</span>
            </div>
            <div class="lifecycle-step">
                <span class="lifecycle-arrow">↓</span>
                <span class="lifecycle-label">PreCompact</span>
                <span style="margin-left: 16px; color: #666;">If context needs compaction</span>
            </div>
            <div class="lifecycle-step">
                <span class="lifecycle-arrow">↓</span>
                <span class="lifecycle-label">PostCompact</span>
                <span style="margin-left: 16px; color: #666;">After compaction completes</span>
            </div>
            <div class="lifecycle-step">
                <span class="lifecycle-arrow">→</span>
                <span class="lifecycle-label highlight">SessionEnd</span>
                <span style="margin-left: 16px; color: #666;">Session terminates</span>
            </div>
            <div style="margin-top: 16px; padding: 12px 16px; background: #fff3cd; border-left: 4px solid #ffc107; border-radius: 4px;">
                <strong style="font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; color: #856404;">Async — Fire at any time during session</strong>
                <div style="margin-top: 8px;">
                    <span class="matcher-tag">Notification</span>
                    <span class="matcher-tag">TeammateIdle</span>
                    <span class="matcher-tag">TaskCompleted</span>
                    <span class="matcher-tag">TaskCreated</span>
                    <span class="matcher-tag">ConfigChange</span>
                    <span class="matcher-tag">WorktreeCreate</span>
                    <span class="matcher-tag">WorktreeRemove</span>
                    <span class="matcher-tag">InstructionsLoaded</span>
                    <span class="matcher-tag">Elicitation</span>
                    <span class="matcher-tag">ElicitationResult</span>
                    <span class="matcher-tag">StopFailure</span>
                </div>
            </div>
        </div>

        <p style="margin-top: 24px;"><strong>Note:</strong> Setup fires separately via <code>--init</code>/<code>--maintenance</code> CLI flags. Notification, TeammateIdle, TaskCompleted, TaskCreated, ConfigChange, WorktreeCreate, WorktreeRemove, InstructionsLoaded, Elicitation, ElicitationResult, StopFailure, CwdChanged, and FileChanged hooks fire asynchronously at any point during the session — they are not part of the sequential flow above.</p>
    </div>

    <!-- Slide 5: SessionStart -->
    <div class="slide" data-slide="5">
        <div class="hook-title">
            <span class="hook-number">1</span>
            <span class="hook-name">SessionStart</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When you start Claude Code or resume an existing session. This is the <strong>first hook</strong> to fire.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Run Claude Code from your terminal to start a new session:</p>
            <div class="trigger-example">$ claude</div>
            <p style="margin-top: 12px;">Or resume an existing session:</p>
            <div class="trigger-example">$ claude --resume</div>
        </div>

        <div class="matcher-values">
            <strong>Trigger Sources:</strong>
            <span class="matcher-tag">startup</span>
            <span class="matcher-tag">resume</span>
            <span class="matcher-tag">clear</span>
            <span class="matcher-tag">compact</span>
        </div>

        <div class="info-grid" style="margin: 16px 0;">
            <div class="info-card">
                <h4>Input Fields</h4>
                <p><code>model</code> — Model identifier (e.g., <code>claude-sonnet-4-6</code>)</p>
                <p><code>agent_type</code> — Agent name if started with <code>--agent</code> flag (since v2.1.43)</p>
            </div>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Claude session started"</strong>
                    <span>Audio notification when Claude Code is ready</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📊</span>
                <div class="use-case-text">
                    <strong>Load Git Status</strong>
                    <span>Inject current branch, uncommitted changes into Claude's context</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔧</span>
                <div class="use-case-text">
                    <strong>Set Environment Variables</strong>
                    <span>Configure API keys, paths, or project-specific settings</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📝</span>
                <div class="use-case-text">
                    <strong>Load Project Memory</strong>
                    <span>Restore previous context or project-specific instructions</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: sessionstart.wav — "Claude session started"
        </div>
    </div>

    <!-- Slide 6: UserPromptSubmit -->
    <div class="slide" data-slide="6">
        <div class="hook-title">
            <span class="hook-number">2</span>
            <span class="hook-name">UserPromptSubmit</span>
            <span class="can-block">Can Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When you submit a prompt, <strong>before</strong> Claude processes it. Fires once per user message.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Type any prompt and press <code>Enter</code>:</p>
            <div class="trigger-example">&gt; What is the weather in Karachi?</div>
            <p style="margin-top: 12px;">Or any other message to Claude:</p>
            <div class="trigger-example">&gt; Help me fix the bug in my code</div>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Processing your request"</strong>
                    <span>Audio confirmation that your prompt was received</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">✅</span>
                <div class="use-case-text">
                    <strong>Validate Prompt Content</strong>
                    <span>Block harmful, spam, or unauthorized requests</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📎</span>
                <div class="use-case-text">
                    <strong>Inject Dynamic Context</strong>
                    <span>Add relevant docs, git history, or environment info based on keywords</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📈</span>
                <div class="use-case-text">
                    <strong>Usage Tracking</strong>
                    <span>Log prompts for analytics or rate limiting</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: userpromptsubmit.wav — "Processing your request"
        </div>
    </div>

    <!-- Slide 7: PreToolUse -->
    <div class="slide" data-slide="7">
        <div class="hook-title">
            <span class="hook-number">3</span>
            <span class="hook-name">PreToolUse</span>
            <span class="can-block">Can Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>After Claude creates tool parameters but <strong>before</strong> the tool executes. Fires for every tool call (Bash, Edit, Write, Read, etc.).</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Ask Claude to do anything that requires a tool:</p>
            <div class="trigger-example">&gt; Read the README.md file</div>
            <div class="trigger-example" style="margin-top: 8px;">&gt; Run npm test</div>
            <div class="trigger-example" style="margin-top: 8px;">&gt; Create a commit with message "fix bug"</div>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Ding" (tool starting)</strong>
                    <span>Short audio cue when Claude is about to use a tool</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🛡️</span>
                <div class="use-case-text">
                    <strong>Block Dangerous Commands</strong>
                    <span>Prevent <code>rm -rf /</code>, <code>DROP TABLE</code>, or other destructive operations</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">✏️</span>
                <div class="use-case-text">
                    <strong>Modify Tool Inputs</strong>
                    <span>Sanitize paths, normalize commands, add default flags</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🎵</span>
                <div class="use-case-text">
                    <strong>Special Sound for Git Commits</strong>
                    <span>Play different sound when <code>git commit</code> is detected</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: pretooluse.wav — "Ding" | pretooluse-git-committing.wav for commits
        </div>
    </div>

    <!-- Slide 8: PostToolUse -->
    <div class="slide" data-slide="8">
        <div class="hook-title">
            <span class="hook-number">4</span>
            <span class="hook-name">PostToolUse</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>Immediately <strong>after</strong> a tool completes successfully. Does NOT fire if the tool fails.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Ask Claude to perform any successful tool operation:</p>
            <div class="trigger-example">&gt; Read the package.json file</div>
            <div class="trigger-example" style="margin-top: 8px;">&gt; List all files in the .claude project folder</div>
            <p style="margin-top: 12px;">Fires after the tool completes without errors.</p>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Dong" (tool completed)</strong>
                    <span>Short audio cue confirming tool execution succeeded</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🎨</span>
                <div class="use-case-text">
                    <strong>Auto-Format Code</strong>
                    <span>Run Prettier, Black, or gofmt after file edits</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🧪</span>
                <div class="use-case-text">
                    <strong>Run Tests Automatically</strong>
                    <span>Execute test suite after code changes</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📊</span>
                <div class="use-case-text">
                    <strong>Log Successful Operations</strong>
                    <span>Track what tools were used and their results</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: posttooluse.wav — "Dong"
        </div>
    </div>

    <!-- Slide 9: PostToolUseFailure -->
    <div class="slide" data-slide="9">
        <div class="hook-title">
            <span class="hook-number">5</span>
            <span class="hook-name">PostToolUseFailure</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>Immediately <strong>after</strong> a tool call fails (error or non-zero exit code). Does NOT fire if the tool succeeds.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Ask Claude to run a Bash command that exits with non-zero status:</p>
            <div class="trigger-example">&gt; Run the command: false</div>
            <div class="trigger-example" style="margin-top: 8px;">&gt; Run the command: ls /nonexistent/path/xyz</div>
            <p style="margin-top: 12px;">Fires when Bash exits with non-zero code (e.g., exit code 1 or 2).</p>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Tool failed"</strong>
                    <span>Audio alert when something goes wrong</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🚨</span>
                <div class="use-case-text">
                    <strong>Send Failure Alerts</strong>
                    <span>Notify via Slack, email, or desktop notification on errors</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔍</span>
                <div class="use-case-text">
                    <strong>Analyze Error Patterns</strong>
                    <span>Log failures for debugging and monitoring</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">💡</span>
                <div class="use-case-text">
                    <strong>Provide Recovery Context</strong>
                    <span>Inject helpful information to help Claude recover</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: posttoolusefailure.wav — "Tool failed"
        </div>
    </div>

    <!-- Slide 10: PermissionRequest -->
    <div class="slide" data-slide="10">
        <div class="hook-title">
            <span class="hook-number">6</span>
            <span class="hook-name">PermissionRequest</span>
            <span class="can-block">Can Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When a permission dialog is about to be shown. Fires once per permission prompt, allowing you to auto-approve or auto-deny.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Ask Claude to run a command that requires permission approval:</p>
            <div class="trigger-example">&gt; Create a directory ABC on project root</div>
            <div class="trigger-example" style="margin-top: 8px;">&gt; Run the build script</div>
            <p style="margin-top: 12px;">Claude will show a permission dialog before running the command.</p>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Permission required"</strong>
                    <span>Alert when Claude needs your approval for an action</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">✅</span>
                <div class="use-case-text">
                    <strong>Auto-Approve Safe Commands</strong>
                    <span>Skip permission dialog for trusted operations like <code>npm test</code></span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🚫</span>
                <div class="use-case-text">
                    <strong>Auto-Deny Dangerous Operations</strong>
                    <span>Block sensitive actions without showing dialog</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📋</span>
                <div class="use-case-text">
                    <strong>Audit Permission Requests</strong>
                    <span>Log all permission requests for compliance</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: permissionrequest.wav — "Permission required"
        </div>
    </div>

    <!-- Slide 11: Notification -->
    <div class="slide" data-slide="11">
        <div class="hook-title">
            <span class="hook-number">7</span>
            <span class="hook-name">Notification</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When Claude Code sends system notifications (permission prompts, idle alerts, auth success). Fires asynchronously, outside the main agentic loop.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Triggered automatically by system events:</p>
            <div class="trigger-example">• Leave Claude idle for a while → idle_prompt</div>
            <div class="trigger-example" style="margin-top: 8px;">• Claude asks for permission → permission_prompt</div>
            <div class="trigger-example" style="margin-top: 8px;">• Successfully authenticate → auth_success</div>
        </div>

        <div class="matcher-values">
            <strong>Notification Types:</strong>
            <span class="matcher-tag">permission_prompt</span>
            <span class="matcher-tag">idle_prompt</span>
            <span class="matcher-tag">auth_success</span>
            <span class="matcher-tag">elicitation_dialog</span>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Notification"</strong>
                    <span>Audio cue for system notifications</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🖥️</span>
                <div class="use-case-text">
                    <strong>Desktop Notifications</strong>
                    <span>Route notifications to macOS/Windows notification center</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">💬</span>
                <div class="use-case-text">
                    <strong>External Integrations</strong>
                    <span>Send to Slack, Discord, or webhook endpoints</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: notification.wav — System notification sound
        </div>
    </div>

    <!-- Slide 12: SubagentStart -->
    <div class="slide" data-slide="12">
        <div class="hook-title">
            <span class="hook-number">8</span>
            <span class="hook-name">SubagentStart</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When a subagent is spawned via the Task tool. Can happen multiple times per session (subagents can spawn subagents). Includes <code>agent_id</code> (unique identifier) and <code>agent_type</code> (agent name).</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Ask Claude to perform a task that spawns a subagent:</p>
            <div class="trigger-example">&gt; Use Explore agent to read the README.md file</div>
            <div class="trigger-example" style="margin-top: 8px;">&gt; Search for all API endpoints in this project</div>
            <p style="margin-top: 12px;">Claude will spawn an Explore, Plan, or Bash agent to help.</p>
        </div>

        <div class="matcher-values">
            <strong>Input Fields:</strong>
            <span class="matcher-tag">agent_id</span>
            <span class="matcher-tag">agent_type</span>
        </div>

        <div class="matcher-values" style="margin-top: 8px;">
            <strong>Agent Types:</strong>
            <span class="matcher-tag">Bash</span>
            <span class="matcher-tag">Explore</span>
            <span class="matcher-tag">Plan</span>
            <span class="matcher-tag">CustomAgentName</span>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Subagent started"</strong>
                    <span>Audio notification when a subagent begins work</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🛡️</span>
                <div class="use-case-text">
                    <strong>Inject Security Guidelines</strong>
                    <span>Add security rules to subagent context</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📊</span>
                <div class="use-case-text">
                    <strong>Monitor Subagent Spawning</strong>
                    <span>Track which agents are created and when</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📝</span>
                <div class="use-case-text">
                    <strong>Add Project Context</strong>
                    <span>Inject project-specific instructions into subagents</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: subagentstart.wav — "Subagent started"
        </div>
    </div>

    <!-- Slide 13: SubagentStop -->
    <div class="slide" data-slide="13">
        <div class="hook-title">
            <span class="hook-number">9</span>
            <span class="hook-name">SubagentStop</span>
            <span class="can-block">Can Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When a subagent finishes responding. Can be blocked to force the subagent to continue working. Includes <code>agent_id</code>, <code>agent_type</code>, <code>last_assistant_message</code> (since v2.1.47), and <code>agent_transcript_path</code>.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Fires automatically when a subagent completes its task:</p>
            <div class="trigger-example">&gt; Explore the codebase and find where authentication is handled</div>
            <p style="margin-top: 12px;">After the Explore agent finishes searching, SubagentStop fires.</p>
        </div>

        <div class="matcher-values">
            <strong>Input Fields:</strong>
            <span class="matcher-tag">agent_id</span>
            <span class="matcher-tag">agent_type</span>
            <span class="matcher-tag">last_assistant_message</span>
            <span class="matcher-tag">agent_transcript_path</span>
        </div>

        <div class="matcher-values" style="margin-top: 8px;">
            <strong>Agent Types:</strong>
            <span class="matcher-tag">Bash</span>
            <span class="matcher-tag">Explore</span>
            <span class="matcher-tag">Plan</span>
            <span class="matcher-tag">CustomAgentName</span>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Subagent completed"</strong>
                    <span>Audio notification when subagent finishes</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">✅</span>
                <div class="use-case-text">
                    <strong>Verify Task Completion</strong>
                    <span>Check if subagent actually completed its assigned task</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔄</span>
                <div class="use-case-text">
                    <strong>Force Continuation</strong>
                    <span>Block stopping if quality checks fail</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📈</span>
                <div class="use-case-text">
                    <strong>Log Completion Metrics</strong>
                    <span>Track subagent performance and duration</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: subagentstop.wav — "Subagent completed"
        </div>
    </div>

    <!-- Slide 14: Stop -->
    <div class="slide" data-slide="14">
        <div class="hook-title">
            <span class="hook-number">10</span>
            <span class="hook-name">Stop</span>
            <span class="can-block">Can Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When Claude finishes responding and is ready to stop. Does NOT fire on user interrupts (Ctrl+C). Includes <code>last_assistant_message</code> field with Claude's final response text (since v2.1.47).</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Simply wait for Claude to finish responding to any prompt:</p>
            <div class="trigger-example">&gt; Explain how this function works</div>
            <p style="margin-top: 12px;">When Claude completes its response and returns to the prompt, Stop fires.</p>
            <p style="margin-top: 8px; font-size: 0.9rem; color: #666;">Note: Does NOT fire if you press Ctrl+C to interrupt.</p>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Task completed"</strong>
                    <span>Audio confirmation that Claude finished responding</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🧪</span>
                <div class="use-case-text">
                    <strong>Verify Tests Pass</strong>
                    <span>Block stopping until all tests pass</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📋</span>
                <div class="use-case-text">
                    <strong>Check Task List</strong>
                    <span>Prevent stopping if there are unfinished tasks</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📝</span>
                <div class="use-case-text">
                    <strong>Analyze Last Response</strong>
                    <span>Use <code>last_assistant_message</code> to log or validate Claude's final output</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: stop.wav — "Task completed"
        </div>
    </div>

    <!-- Slide 15: PreCompact -->
    <div class="slide" data-slide="15">
        <div class="hook-title">
            <span class="hook-number">11</span>
            <span class="hook-name">PreCompact</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>Before context compaction occurs — either automatically when context window fills up, or when user runs <code>/compact</code>.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Manually run the compact command:</p>
            <div class="trigger-example">&gt; /compact</div>
            <p style="margin-top: 12px;">Or automatically when context window fills up after a long conversation.</p>
        </div>

        <div class="matcher-values">
            <strong>Trigger Types:</strong>
            <span class="matcher-tag">manual</span>
            <span class="matcher-tag">auto</span>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Compacting context"</strong>
                    <span>Audio alert before context is compressed</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">💾</span>
                <div class="use-case-text">
                    <strong>Preserve Critical Context</strong>
                    <span>Save important information before it's compacted</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📊</span>
                <div class="use-case-text">
                    <strong>Monitor Context Usage</strong>
                    <span>Track how often context fills up</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📝</span>
                <div class="use-case-text">
                    <strong>Re-Inject Guidelines</strong>
                    <span>Add project rules to be included after compaction</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: precompact.wav — "Compacting context"
        </div>
    </div>

    <!-- Slide 16: PostCompact -->
    <div class="slide" data-slide="16">
        <div class="hook-title">
            <span class="hook-number">12</span>
            <span class="hook-name">PostCompact</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>After context compaction completes — either automatically when context window fills up, or after user runs <code>/compact</code>. Use this to react to the new compacted state.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Fires automatically after any compaction:</p>
            <div class="trigger-example">&gt; /compact &nbsp;&nbsp;&nbsp;← Triggers PreCompact then PostCompact</div>
            <p style="margin-top: 12px;">Or automatically after auto-compact when context window fills up.</p>
        </div>

        <div class="matcher-values">
            <strong>Trigger Types:</strong>
            <span class="matcher-tag">manual</span>
            <span class="matcher-tag">auto</span>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Context compacted"</strong>
                    <span>Audio confirmation that compaction finished</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📋</span>
                <div class="use-case-text">
                    <strong>Log Compact Summary</strong>
                    <span>Save the generated conversation summary for audit</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔄</span>
                <div class="use-case-text">
                    <strong>Update External State</strong>
                    <span>Sync external tools with the new compacted context</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📊</span>
                <div class="use-case-text">
                    <strong>Track Compaction Frequency</strong>
                    <span>Monitor how often context fills up and gets compressed</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: postcompact.wav — "Context compacted"
        </div>
    </div>

    <!-- Slide 17: SessionEnd -->
    <div class="slide" data-slide="17">
        <div class="hook-title">
            <span class="hook-number">13</span>
            <span class="hook-name">SessionEnd</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When a session terminates. This is the <strong>last hook</strong> to fire — cannot prevent session from ending.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>End the session in any of these ways:</p>
            <div class="trigger-example">&gt; /clear &nbsp;&nbsp;&nbsp;← Clears conversation and ends session</div>
            <div class="trigger-example" style="margin-top: 8px;">&gt; exit &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;← Type exit at the prompt</div>
            <div class="trigger-example" style="margin-top: 8px;">Press Ctrl+D or Ctrl+C to exit</div>
        </div>

        <div class="matcher-values">
            <strong>End Reasons:</strong>
            <span class="matcher-tag">clear</span>
            <span class="matcher-tag">resume</span>
            <span class="matcher-tag">logout</span>
            <span class="matcher-tag">prompt_input_exit</span>
            <span class="matcher-tag">bypass_permissions_disabled</span>
            <span class="matcher-tag">other</span>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Session ended"</strong>
                    <span>Audio farewell when closing Claude Code</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🧹</span>
                <div class="use-case-text">
                    <strong>Cleanup Operations</strong>
                    <span>Delete temporary files, close connections</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📊</span>
                <div class="use-case-text">
                    <strong>Log Session Statistics</strong>
                    <span>Record session duration, tools used, etc.</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">💾</span>
                <div class="use-case-text">
                    <strong>Save Session State</strong>
                    <span>Archive transcript or project state</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: sessionend.wav — "Session ended"
        </div>
    </div>

    <!-- Slide 18: Setup -->
    <div class="slide" data-slide="18">
        <div class="hook-title">
            <span class="hook-number">14</span>
            <span class="hook-name">Setup</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When Claude Code runs the <code>/setup</code> command for project initialization. Rarely used compared to other hooks.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Run setup hooks without starting interactive mode:</p>
            <div class="trigger-example">$ claude --init-only</div>
            <p style="margin-top: 12px; font-size: 0.9rem; color: #2e7d32;">Note: <code>claude --init</code> does NOT trigger the Setup hook.</p>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Setup initiated"</strong>
                    <span>Audio notification when project setup begins</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📦</span>
                <div class="use-case-text">
                    <strong>Install Dependencies</strong>
                    <span>Run npm install, pip install, etc.</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">⚙️</span>
                <div class="use-case-text">
                    <strong>Configure Project</strong>
                    <span>Set up MCP servers, linters, formatters</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">✅</span>
                <div class="use-case-text">
                    <strong>Validate Environment</strong>
                    <span>Check required tools and versions are installed</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: setup.wav — "Setup initiated"
        </div>
    </div>

    <!-- Slide 19: TeammateIdle -->
    <div class="slide" data-slide="19">
        <div class="hook-title">
            <span class="hook-number">15</span>
            <span class="hook-name">TeammateIdle</span>
            <span class="can-block">Can Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When a teammate agent becomes idle in an experimental agent teams session. Requires the agent teams feature to be enabled. Includes <code>teammate_name</code> and <code>team_name</code> input fields (since v2.1.33).</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Enable agent teams and start a multi-agent session:</p>
            <div class="trigger-example">$ CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude</div>
            <p style="margin-top: 12px;">When a teammate agent finishes its current work and becomes idle, this hook fires.</p>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Teammate idle"</strong>
                    <span>Audio notification when a teammate agent is waiting for work</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📋</span>
                <div class="use-case-text">
                    <strong>Auto-Assign Tasks</strong>
                    <span>Automatically queue the next task for the idle teammate</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📊</span>
                <div class="use-case-text">
                    <strong>Monitor Team Utilization</strong>
                    <span>Track idle time across agents for workload balancing</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔔</span>
                <div class="use-case-text">
                    <strong>Notify Orchestrator</strong>
                    <span>Alert the main agent that a teammate is available</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: teammateidle.wav — "Teammate idle"
        </div>
    </div>

    <!-- Slide 20: TaskCompleted -->
    <div class="slide" data-slide="20">
        <div class="hook-title">
            <span class="hook-number">16</span>
            <span class="hook-name">TaskCompleted</span>
            <span class="can-block">Can Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When a background task completes in an experimental agent teams session. Requires the agent teams feature to be enabled. Includes <code>task_id</code>, <code>task_subject</code>, and <code>task_description</code> input fields (since v2.1.33).</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Enable agent teams and run background tasks:</p>
            <div class="trigger-example">$ CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude</div>
            <p style="margin-top: 12px;">When a background task finishes execution, this hook fires.</p>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Task completed"</strong>
                    <span>Audio notification when a background task finishes</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">✅</span>
                <div class="use-case-text">
                    <strong>Verify Task Results</strong>
                    <span>Run validation checks on the completed task output</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔄</span>
                <div class="use-case-text">
                    <strong>Trigger Follow-Up Tasks</strong>
                    <span>Automatically start dependent tasks in a pipeline</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📈</span>
                <div class="use-case-text">
                    <strong>Log Completion Metrics</strong>
                    <span>Track task duration, success rate, and throughput</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: taskcompleted.wav — "Task completed"
        </div>
    </div>

    <!-- Slide 21: TaskCreated -->
    <div class="slide" data-slide="21">
        <div class="hook-title">
            <span class="hook-number">17</span>
            <span class="hook-name">TaskCreated</span>
            <span class="can-block">Can Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>Runs when a task is being created via the TaskCreate tool. Fires in experimental agent teams sessions when a teammate creates a new task.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Fires when a teammate creates a task via TaskCreate:</p>
            <div class="trigger-example">$ CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude</div>
            <p style="margin-top: 12px;">When a teammate uses the TaskCreate tool, this hook fires before the task is finalized.</p>
        </div>

        <div class="info-grid" style="margin: 16px 0;">
            <div class="info-card">
                <h4>Input Fields</h4>
                <p><code>task_id</code> — Unique identifier for the task</p>
                <p><code>task_subject</code> — Subject line of the task</p>
                <p><code>task_description</code> — Full description of the task</p>
                <p><code>teammate_name</code> — Name of the teammate creating the task</p>
                <p><code>team_name</code> — Name of the team</p>
            </div>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">📝</span>
                <div class="use-case-text">
                    <strong>Enforce Task Naming Conventions</strong>
                    <span>Validate that task subjects follow team naming standards</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">✅</span>
                <div class="use-case-text">
                    <strong>Validate Task Descriptions</strong>
                    <span>Ensure task descriptions contain required fields or minimum detail</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🚫</span>
                <div class="use-case-text">
                    <strong>Prevent Unauthorized Task Creation</strong>
                    <span>Block task creation from unauthorized teammates or teams</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: taskcreated.wav — "Task created"
        </div>
        <p style="margin-top: 8px; font-size: 0.85rem; color: #999;">Added in v2.1.84</p>
    </div>

    <!-- Slide 22: ConfigChange -->
    <div class="slide" data-slide="22">
        <div class="hook-title">
            <span class="hook-number">18</span>
            <span class="hook-name">ConfigChange</span>
            <span class="can-block">Can Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When a configuration file changes during a session. Detects changes to user settings, project settings, local settings, policy settings, and skills. Includes optional <code>file_path</code> input field with the path to the modified config file (since v2.1.49).</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Modify any Claude Code configuration file while a session is active:</p>
            <div class="trigger-example">Edit .claude/settings.json while Claude is running</div>
            <div class="trigger-example" style="margin-top: 8px;">Change user settings via ~/.claude/settings.json</div>
            <p style="margin-top: 12px;">The hook fires when Claude detects the config file has been modified.</p>
        </div>

        <div class="matcher-values">
            <strong>Config Sources:</strong>
            <span class="matcher-tag">user_settings</span>
            <span class="matcher-tag">project_settings</span>
            <span class="matcher-tag">local_settings</span>
            <span class="matcher-tag">policy_settings</span>
            <span class="matcher-tag">skills</span>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Config changed"</strong>
                    <span>Audio notification when configuration is modified</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🛡️</span>
                <div class="use-case-text">
                    <strong>Audit Config Changes</strong>
                    <span>Log and validate configuration modifications for security</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔄</span>
                <div class="use-case-text">
                    <strong>Auto-Reload Settings</strong>
                    <span>Trigger reloads or re-initialization when config changes</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🚫</span>
                <div class="use-case-text">
                    <strong>Block Unsafe Changes</strong>
                    <span>Prevent unauthorized config modifications (except policy_settings)</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: configchange.wav — "Config changed"
        </div>
    </div>

    <!-- Slide 23: WorktreeCreate -->
    <div class="slide" data-slide="23">
        <div class="hook-title">
            <span class="hook-number">19</span>
            <span class="hook-name">WorktreeCreate</span>
            <span class="can-block">Can Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When agent worktree isolation creates worktrees, enabling custom VCS setup. This hook fires during the worktree creation process for agents that use <code>isolation: worktree</code> in their definitions (since v2.1.50).</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Use an agent configured with worktree isolation:</p>
            <div class="trigger-example">claude --agent my-isolated-agent (with isolation: worktree)</div>
            <p style="margin-top: 12px;">The hook fires when Claude creates a new git worktree for the agent's isolated workspace.</p>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Worktree created"</strong>
                    <span>Audio notification when a worktree is set up for an agent</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔧</span>
                <div class="use-case-text">
                    <strong>Custom VCS Setup</strong>
                    <span>Run setup scripts (install deps, configure git hooks) in the new worktree</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📋</span>
                <div class="use-case-text">
                    <strong>Log Worktree Activity</strong>
                    <span>Track which agents create worktrees and when</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔗</span>
                <div class="use-case-text">
                    <strong>Symlink Dependencies</strong>
                    <span>Symlink node_modules or other large directories to save disk space</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: worktreecreate.wav — "Worktree created"
        </div>
    </div>

    <!-- Slide 24: WorktreeRemove -->
    <div class="slide" data-slide="24">
        <div class="hook-title">
            <span class="hook-number">20</span>
            <span class="hook-name">WorktreeRemove</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When agent worktree isolation removes worktrees, enabling custom VCS teardown. This hook fires during the worktree removal process when agents with <code>isolation: worktree</code> finish their work (since v2.1.50).</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Triggered automatically when an isolated agent's worktree is cleaned up:</p>
            <div class="trigger-example">Agent completes work and worktree is removed</div>
            <p style="margin-top: 12px;">The hook fires when Claude removes a git worktree that was created for an agent's isolated workspace.</p>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Worktree removed"</strong>
                    <span>Audio notification when a worktree is cleaned up</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🧹</span>
                <div class="use-case-text">
                    <strong>Custom VCS Teardown</strong>
                    <span>Clean up temporary files, remove symlinks, or archive logs</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📋</span>
                <div class="use-case-text">
                    <strong>Log Cleanup Events</strong>
                    <span>Track when worktrees are removed for auditing</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">💾</span>
                <div class="use-case-text">
                    <strong>Reclaim Disk Space</strong>
                    <span>Trigger garbage collection or cache cleanup after worktree removal</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: worktreeremove.wav — "Worktree removed"
        </div>
    </div>

    <!-- Slide 25: InstructionsLoaded -->
    <div class="slide" data-slide="25">
        <div class="hook-title">
            <span class="hook-number">21</span>
            <span class="hook-name">InstructionsLoaded</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When CLAUDE.md or <code>.claude/rules/*.md</code> files are loaded into context. This fires whenever instructions are read, including at session start and after instruction reloads (since v2.1.69).</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Triggered automatically when Claude Code loads instruction files:</p>
            <div class="trigger-example">Start a session with CLAUDE.md or .claude/rules/*.md present</div>
            <p style="margin-top: 12px;">The hook fires each time instructions are loaded or reloaded into context.</p>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Instructions loaded"</strong>
                    <span>Audio notification when project instructions are loaded</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📝</span>
                <div class="use-case-text">
                    <strong>Log Instruction Loads</strong>
                    <span>Track when and which instruction files are loaded for auditing</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔄</span>
                <div class="use-case-text">
                    <strong>Validate Instructions</strong>
                    <span>Check that loaded instructions meet organizational standards</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📊</span>
                <div class="use-case-text">
                    <strong>Monitor Instruction Changes</strong>
                    <span>Detect when instructions change between sessions or reloads</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: instructionsloaded.wav — "Instructions loaded"
        </div>
    </div>

    <!-- Slide 26: Elicitation -->
    <div class="slide" data-slide="26">
        <div class="hook-title">
            <span class="hook-number">22</span>
            <span class="hook-name">Elicitation</span>
            <span class="can-block">Can Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When an MCP server requests user input during a tool call. Allows you to intercept, modify, or block elicitation requests before the user sees them.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Use an MCP server that sends elicitation requests (e.g. <code>@blizzy/mcp-elicit</code>):</p>
            <div class="trigger-example">"Use the elicit_boolean tool to ask me if I like pizza" → Elicitation hook fires</div>
        </div>

        <div class="matcher-values">
            <strong>Matcher:</strong>
            <span class="matcher-tag">MCP server name</span>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "MCP input requested"</strong>
                    <span>Audio alert when an MCP server needs user input</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🛡️</span>
                <div class="use-case-text">
                    <strong>Filter Sensitive Requests</strong>
                    <span>Block or modify elicitation requests from untrusted servers</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📝</span>
                <div class="use-case-text">
                    <strong>Audit MCP Interactions</strong>
                    <span>Log all elicitation requests for compliance tracking</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: elicitation.wav — "MCP input requested"
        </div>
    </div>

    <!-- Slide 27: ElicitationResult -->
    <div class="slide" data-slide="27">
        <div class="hook-title">
            <span class="hook-number">23</span>
            <span class="hook-name">ElicitationResult</span>
            <span class="can-block">Can Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>After a user responds to an MCP elicitation, before the response is sent back to the server. Allows you to intercept, modify, or block the user's response.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>User responds to an MCP elicitation dialog (e.g. the pizza question above):</p>
            <div class="trigger-example">User clicks Yes/No → ElicitationResult hook fires → Response sent to server</div>
        </div>

        <div class="matcher-values">
            <strong>Matcher:</strong>
            <span class="matcher-tag">MCP server name</span>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Response submitted"</strong>
                    <span>Audio confirmation when user responds to an MCP elicitation</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔒</span>
                <div class="use-case-text">
                    <strong>Sanitize Responses</strong>
                    <span>Strip sensitive data before it's sent to the MCP server</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📊</span>
                <div class="use-case-text">
                    <strong>Track User Decisions</strong>
                    <span>Log accept/decline/cancel actions for analytics</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: elicitationresult.wav — "Response submitted"
        </div>
    </div>

    <!-- Slide 28: StopFailure -->
    <div class="slide" data-slide="28">
        <div class="hook-title">
            <span class="hook-number">24</span>
            <span class="hook-name">StopFailure</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When the turn ends due to an API error (rate limit, auth failure, etc.). Unlike Stop, this fires on error conditions rather than successful completion. Introduced in v2.1.78 to prevent infinite loops when stop hooks re-feed blocking errors to the model.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>API error occurs during Claude's response (rate limit exceeded, authentication failure, network error):</p>
            <div class="trigger-example">Claude processing → API error → StopFailure hook fires</div>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Stop failure"</strong>
                    <span>Audio alert when a turn ends due to an API error</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📊</span>
                <div class="use-case-text">
                    <strong>Error Tracking</strong>
                    <span>Log API failures for monitoring rate limits and auth issues</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔔</span>
                <div class="use-case-text">
                    <strong>Alert on Failures</strong>
                    <span>Send desktop notification when API errors interrupt work</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: stopfailure.wav — "Stop failure"
        </div>
    </div>

    <!-- Slide 29: CwdChanged -->
    <div class="slide" data-slide="29">
        <div class="hook-title">
            <span class="hook-number">25</span>
            <span class="hook-name">CwdChanged</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When the working directory changes during a session. Designed for reactive environment management — for example, automatically loading environment variables via direnv when Claude navigates to a different project directory. Introduced in v2.1.83.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Claude changes the current working directory during a session:</p>
            <div class="trigger-example">Claude navigates to new directory → CwdChanged hook fires</div>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "Directory changed"</strong>
                    <span>Audio alert when Claude moves to a different directory</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🌍</span>
                <div class="use-case-text">
                    <strong>Environment Reload</strong>
                    <span>Automatically reload .env files or direnv when changing directories</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📂</span>
                <div class="use-case-text">
                    <strong>Context Awareness</strong>
                    <span>Load project-specific rules or configurations based on current directory</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: cwdchanged.wav — "Directory changed"
        </div>
    </div>

    <!-- Slide 30: FileChanged -->
    <div class="slide" data-slide="30">
        <div class="hook-title">
            <span class="hook-number">26</span>
            <span class="hook-name">FileChanged</span>
            <span class="cannot-block">Cannot Block</span>
        </div>

        <div class="trigger-box">
            <h4>When It Triggers</h4>
            <p>When files change during a session. Designed for reactive environment management — for example, automatically reloading configuration when a <code>.env</code> file is modified by an external process. Introduced in v2.1.83 alongside CwdChanged.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>A watched file changes during a Claude Code session:</p>
            <div class="trigger-example">File modified externally → FileChanged hook fires</div>
        </div>

        <h3>Use Cases</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔊</span>
                <div class="use-case-text">
                    <strong>Voice: "File changed"</strong>
                    <span>Audio alert when a watched file is modified</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔄</span>
                <div class="use-case-text">
                    <strong>Hot Reload</strong>
                    <span>Automatically reload environment variables or config when files change</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">📝</span>
                <div class="use-case-text">
                    <strong>Change Logging</strong>
                    <span>Track file modifications for audit or debugging purposes</span>
                </div>
            </div>
        </div>

        <div class="sound-demo">
            🔊 Sound: filechanged.wav — "File changed"
        </div>
    </div>

    <!-- Slide 31: Agent Hooks -->
    <div class="slide" data-slide="31">
        <h1>Agent Hooks (Bonus)</h1>
        <p>Claude Code 2.1.0 introduced support for agent-specific hooks defined in agent frontmatter files. These hooks only run within the agent's lifecycle.</p>

        <div class="trigger-box">
            <h4>Supported Agent Hooks</h4>
            <p>Agent frontmatter hooks support <strong>6 of 26 hooks</strong>: PreToolUse, PostToolUse, PermissionRequest, PostToolUseFailure, Stop, and SubagentStop.</p>
        </div>

        <div class="how-to-trigger">
            <h4>How to Trigger</h4>
            <p>Run the demo agent included in this repository:</p>
            <div class="trigger-example">&gt; /agents claude-code-hook-agent</div>
            <p style="margin-top: 12px;">This agent fetches Dubai weather and triggers all 6 agent hooks.</p>
        </div>

        <h3>The 6 Agent Hooks</h3>
        <div class="use-cases">
            <div class="use-case-item">
                <span class="use-case-icon">🔔</span>
                <div class="use-case-text">
                    <strong>PreToolUse</strong>
                    <span>Fires before the agent uses any tool (Read, Bash, WebFetch, etc.)</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">✅</span>
                <div class="use-case-text">
                    <strong>PostToolUse</strong>
                    <span>Fires after the agent's tool call completes successfully</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔐</span>
                <div class="use-case-text">
                    <strong>PermissionRequest</strong>
                    <span>Fires when a tool requires user permission</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">❌</span>
                <div class="use-case-text">
                    <strong>PostToolUseFailure</strong>
                    <span>Fires after a tool call fails</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🏁</span>
                <div class="use-case-text">
                    <strong>Stop</strong>
                    <span>Fires when the agent finishes its task and returns control</span>
                </div>
            </div>
            <div class="use-case-item">
                <span class="use-case-icon">🔚</span>
                <div class="use-case-text">
                    <strong>SubagentStop</strong>
                    <span>Fires when a subagent completes its work</span>
                </div>
            </div>
        </div>

        <h3>Agent Configuration Example (all 6 hooks)</h3>
        <div class="code-block">
<span class="comment"># .claude/agents/my-agent.md</span>
---
name: my-agent
hooks:
  <span class="key">PreToolUse</span>:
    - matcher: ".*"
      hooks:
        - type: command
          command: <span class="string">python3 .claude/hooks/scripts/hooks.py --agent=my-agent</span>
  <span class="key">PostToolUse</span>:
    - matcher: ".*"
      hooks:
        - type: command
          command: <span class="string">python3 .claude/hooks/scripts/hooks.py --agent=my-agent</span>
  <span class="key">PermissionRequest</span>:
    - matcher: ".*"
      hooks:
        - type: command
          command: <span class="string">python3 .claude/hooks/scripts/hooks.py --agent=my-agent</span>
  <span class="key">PostToolUseFailure</span>:
    - matcher: ".*"
      hooks:
        - type: command
          command: <span class="string">python3 .claude/hooks/scripts/hooks.py --agent=my-agent</span>
  <span class="key">Stop</span>:
    - hooks:
        - type: command
          command: <span class="string">python3 .claude/hooks/scripts/hooks.py --agent=my-agent</span>
  <span class="key">SubagentStop</span>:
    - hooks:
        - type: command
          command: <span class="string">python3 .claude/hooks/scripts/hooks.py --agent=my-agent</span>
---
        </div>

        <div class="sound-demo">
            🔊 Sounds: agent_pretooluse.wav, agent_posttooluse.wav, agent_permissionrequest.wav, agent_posttoolusefailure.wav, agent_stop.wav, agent_subagentstop.wav
        </div>
    </div>

    <!-- Slide 32: Configuration -->
    <div class="slide" data-slide="32">
        <h1>Configuration</h1>
        <p>Hooks are configured in <code>.claude/settings.json</code> and can be individually enabled/disabled.</p>

        <h3>Hook Configuration in settings.json</h3>
        <div class="code-block">
<span class="comment">// .claude/settings.json</span>
{
  <span class="key">"hooks"</span>: {
    <span class="key">"SessionStart"</span>: [{
      <span class="key">"hooks"</span>: [{
        <span class="key">"type"</span>: <span class="string">"command"</span>,
        <span class="key">"command"</span>: <span class="string">"python3 .claude/hooks/scripts/hooks.py"</span>,
        <span class="key">"timeout"</span>: 5000,
        <span class="key">"async"</span>: true,
        <span class="key">"once"</span>: true
      }]
    }]
  }
}
        </div>

        <h3>Disable All Hooks</h3>
        <div class="code-block">
<span class="comment">// .claude/settings.local.json (git-ignored)</span>
{
  <span class="key">"disableAllHooks"</span>: true
}
        </div>

        <h3>Disable Individual Hooks</h3>
        <div class="code-block">
<span class="comment">// .claude/hooks/config/hooks-config.local.json</span>
{
  <span class="key">"disablePreToolUseHook"</span>: true,
  <span class="key">"disablePostToolUseHook"</span>: true,
  <span class="key">"disableLogging"</span>: true
}
        </div>
    </div>

    <!-- Slide 33: Summary -->
    <div class="slide" data-slide="33">
        <h1>Summary</h1>

        <div class="info-grid">
            <div class="info-card">
                <h4>Session Lifecycle</h4>
                <p><strong>SessionStart</strong> — First hook, loads context</p>
                <p><strong>SessionEnd</strong> — Last hook, cleanup</p>
                <p><strong>PreCompact</strong> — Before context compression</p>
                <p><strong>PostCompact</strong> — After context compression</p>
                <p><strong>Setup</strong> — Project initialization</p>
                <p><strong>ConfigChange</strong> — Config file modified</p>
                <p><strong>WorktreeCreate</strong> — Agent worktree created</p>
                <p><strong>WorktreeRemove</strong> — Agent worktree removed</p>
                <p><strong>InstructionsLoaded</strong> — Instructions loaded into context</p>
                <p><strong>Elicitation</strong> — MCP server requests input</p>
                <p><strong>ElicitationResult</strong> — User responds to MCP</p>
                <p><strong>StopFailure</strong> — Turn ends due to API error</p>
                <p><strong>CwdChanged</strong> — Working directory changes</p>
                <p><strong>FileChanged</strong> — Files change during session</p>
            </div>
            <div class="info-card">
                <h4>User Interaction</h4>
                <p><strong>UserPromptSubmit</strong> — Before processing prompt</p>
                <p><strong>Notification</strong> — System alerts</p>
                <p><strong>PermissionRequest</strong> — Permission dialogs</p>
            </div>
            <div class="info-card">
                <h4>Tool Execution</h4>
                <p><strong>PreToolUse</strong> — Before tool runs</p>
                <p><strong>PostToolUse</strong> — After success</p>
                <p><strong>PostToolUseFailure</strong> — After failure</p>
            </div>
            <div class="info-card">
                <h4>Agents & Completion</h4>
                <p><strong>SubagentStart</strong> — Subagent spawned</p>
                <p><strong>SubagentStop</strong> — Subagent finished</p>
                <p><strong>Stop</strong> — Claude ready to stop</p>
                <p><strong>TeammateIdle</strong> — Teammate agent idle</p>
                <p><strong>TaskCompleted</strong> — Background task done</p>
                <p><strong>TaskCreated</strong> — Task being created</p>
            </div>
        </div>

        <h3 style="margin-top: 40px;">Hooks That Can Block Execution</h3>
        <p style="margin-bottom: 24px;">These hooks can prevent actions from proceeding:</p>
        <div class="matcher-values">
            <span class="matcher-tag">UserPromptSubmit</span>
            <span class="matcher-tag">PreToolUse</span>
            <span class="matcher-tag">PermissionRequest</span>
            <span class="matcher-tag">SubagentStop</span>
            <span class="matcher-tag">Stop</span>
            <span class="matcher-tag">TeammateIdle</span>
            <span class="matcher-tag">TaskCompleted</span>
            <span class="matcher-tag">TaskCreated</span>
            <span class="matcher-tag">ConfigChange</span>
            <span class="matcher-tag">WorktreeCreate</span>
            <span class="matcher-tag">Elicitation</span>
            <span class="matcher-tag">ElicitationResult</span>
        </div>

        <div style="margin-top: 40px; padding: 24px; background: #f8f9fa; border-radius: 8px;">
            <p><strong>Repository:</strong> github.com/shanraisshan/claude-code-hooks</p>
            <p><strong>Documentation:</strong> code.claude.com/brain/knowledge/docs_legacy/en/hooks</p>
        </div>
    </div>

    <!-- Animated Claude Speaking Logo -->
    <div class="header-logo">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 90">
            <style>
                .claude-body { animation: bob 0.8s ease-in-out infinite; transform-origin: center bottom; }
                .shadow { animation: shadow-pulse 0.8s ease-in-out infinite; }
                .mouth { animation: talk 0.3s ease-in-out infinite; transform-origin: center center; }
                .left-ear { animation: ear-tilt-left 0.8s ease-in-out infinite; transform-origin: center bottom; }
                .right-ear { animation: ear-tilt-right 0.8s ease-in-out infinite; transform-origin: center bottom; }
                .wave-1 { animation: wave-expand 0.8s ease-out infinite; transform-origin: left center; }
                .wave-2 { animation: wave-expand 0.8s ease-out infinite 0.2s; transform-origin: left center; }
                .wave-3 { animation: wave-expand 0.8s ease-out infinite 0.4s; transform-origin: left center; }
                .note-1 { animation: float-note-1 1.5s ease-out infinite; }
                .note-2 { animation: float-note-2 1.5s ease-out infinite 0.3s; }
                .note-3 { animation: float-note-3 1.5s ease-out infinite 0.6s; }
                @keyframes bob { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-3px); } }
                @keyframes shadow-pulse { 0%, 100% { transform: scaleX(1); opacity: 0.25; } 50% { transform: scaleX(0.9); opacity: 0.2; } }
                @keyframes talk { 0%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.5); } }
                @keyframes ear-tilt-left { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(-5deg); } }
                @keyframes ear-tilt-right { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(5deg); } }
                @keyframes wave-expand { 0% { opacity: 0.8; transform: scaleX(0.3) scaleY(0.8); } 100% { opacity: 0; transform: scaleX(1.2) scaleY(1); } }
                @keyframes float-note-1 { 0% { opacity: 1; transform: translate(0, 0) rotate(0deg); } 100% { opacity: 0; transform: translate(15px, -25px) rotate(15deg); } }
                @keyframes float-note-2 { 0% { opacity: 1; transform: translate(0, 0) rotate(0deg); } 100% { opacity: 0; transform: translate(20px, -30px) rotate(-10deg); } }
                @keyframes float-note-3 { 0% { opacity: 1; transform: translate(0, 0) rotate(0deg); } 100% { opacity: 0; transform: translate(10px, -35px) rotate(20deg); } }
            </style>
            <ellipse class="shadow" cx="50" cy="82" rx="22" ry="5" fill="#000"/>
            <g class="wave-1"><path d="M 92 44 Q 100 44, 100 52 Q 100 60, 92 60" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
            <g class="wave-2"><path d="M 96 38 Q 108 38, 108 52 Q 108 66, 96 66" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
            <g class="wave-3"><path d="M 100 32 Q 116 32, 116 52 Q 116 72, 100 72" fill="none" stroke="#E07C4C" stroke-width="3" stroke-linecap="round"/></g>
            <g class="note-1"><ellipse cx="108" cy="28" rx="4" ry="3" fill="#E07C4C" transform="rotate(-20, 108, 28)"/><rect x="111" y="12" width="2" height="16" fill="#E07C4C"/><path d="M 113 12 Q 118 14, 118 18 Q 118 22, 113 20" fill="#E07C4C"/></g>
            <g class="note-2"><ellipse cx="122" cy="22" rx="4" ry="3" fill="#E07C4C" transform="rotate(-20, 122, 22)"/><rect x="125" y="6" width="2" height="16" fill="#E07C4C"/></g>
            <g class="note-3"><ellipse cx="115" cy="42" rx="3" ry="2.5" fill="#E07C4C" transform="rotate(-20, 115, 42)"/><ellipse cx="125" cy="40" rx="3" ry="2.5" fill="#E07C4C" transform="rotate(-20, 125, 40)"/><rect x="117" y="26" width="2" height="16" fill="#E07C4C"/><rect x="127" y="24" width="2" height="16" fill="#E07C4C"/><rect x="117" y="26" width="12" height="2" fill="#E07C4C"/></g>
            <g class="claude-body">
                <rect class="left-ear" x="22" y="10" width="8" height="14" fill="#E07C4C"/>
                <rect class="right-ear" x="70" y="10" width="8" height="14" fill="#E07C4C"/>
                <rect x="18" y="24" width="64" height="4" fill="#E07C4C"/>
                <rect x="14" y="28" width="72" height="32" fill="#E07C4C"/>
                <rect x="30" y="34" width="8" height="10" fill="#000000"/>
                <rect x="62" y="34" width="8" height="10" fill="#000000"/>
                <rect class="mouth" x="44" y="50" width="12" height="6" fill="#000000"/>
                <rect x="2" y="40" width="12" height="8" fill="#E07C4C"/>
                <rect x="86" y="40" width="12" height="8" fill="#E07C4C"/>
                <rect x="24" y="60" width="12" height="14" fill="#E07C4C"/>
                <rect x="64" y="60" width="12" height="14" fill="#E07C4C"/>
            </g>
        </svg>
    </div>

    <div class="navigation">
        <button class="nav-btn" id="prevBtn" onclick="prevSlide()">←</button>
        <button class="nav-btn" id="nextBtn" onclick="nextSlide()">→</button>
    </div>

    <div class="slide-counter" id="slideCounter">1 / 33</div>

    <div class="keyboard-hint">
        <kbd>←</kbd> <kbd>→</kbd> or <kbd>Space</kbd> to navigate
    </div>

    <script>
        let currentSlide = 1;
        const totalSlides = 33;

        function showSlide(n) {
            const slides = document.querySelectorAll('.slide');
            slides.forEach(slide => slide.classList.remove('active'));

            if (n > totalSlides) currentSlide = totalSlides;
            if (n < 1) currentSlide = 1;

            document.querySelector(`[data-slide="${currentSlide}"]`).classList.add('active');

            document.getElementById('slideCounter').textContent = `${currentSlide} / ${totalSlides}`;
            document.getElementById('progress').style.width = `${(currentSlide / totalSlides) * 100}%`;

            document.getElementById('prevBtn').disabled = currentSlide === 1;
            document.getElementById('nextBtn').disabled = currentSlide === totalSlides;
        }

        function nextSlide() {
            currentSlide++;
            showSlide(currentSlide);
        }

        function prevSlide() {
            currentSlide--;
            showSlide(currentSlide);
        }

        function goToSlide(n) {
            currentSlide = n;
            showSlide(currentSlide);
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ') {
                e.preventDefault();
                nextSlide();
            } else if (e.key === 'ArrowLeft') {
                e.preventDefault();
                prevSlide();
            }
        });

        // Touch support for mobile
        let touchStartX = 0;
        document.addEventListener('touchstart', (e) => {
            touchStartX = e.touches[0].clientX;
        });

        document.addEventListener('touchend', (e) => {
            const touchEndX = e.changedTouches[0].clientX;
            const diff = touchStartX - touchEndX;

            if (Math.abs(diff) > 50) {
                if (diff > 0) nextSlide();
                else prevSlide();
            }
        });

        showSlide(currentSlide);
    </script>
</body>
</html>
```

## File: `tests-agents-hook/agent-hook-test.py`
```python
#!/usr/bin/env python3
"""Simple logger to test which agent frontmatter hooks actually trigger."""

import json
import sys
import os
from datetime import datetime
from pathlib import Path

# Hardcode log path next to this script for reliability
SCRIPT_DIR = Path(__file__).resolve().parent
LOG_FILE = SCRIPT_DIR.parent / "agent-hook-test.log"

try:
    # Read stdin JSON (same way hooks.py does it)
    stdin_data = ""
    try:
        stdin_data = sys.stdin.read().strip()
    except Exception:
        pass

    # Parse event name from stdin JSON
    hook_event = "no-stdin"
    if stdin_data:
        try:
            parsed = json.loads(stdin_data)
            hook_event = parsed.get("hook_event_name", "missing-field")
        except Exception:
            hook_event = "parse-error"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    entry = {
        "timestamp": timestamp,
        "hook_event": hook_event,
        "cwd": os.getcwd(),
        "claude_project_dir": os.environ.get("CLAUDE_PROJECT_DIR", "NOT_SET"),
        "stdin_len": len(stdin_data)
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

except Exception as e:
    # Last resort: write error to a fallback location
    fallback = Path("/tmp/agent-hook-test-error.log")
    with open(fallback, "a") as f:
        f.write(f"{datetime.now()}: {e}\n")
```

## File: `tests-agents-hook/dubai-weather-report.txt`
```
Dubai Weather Report - March 12, 2026
========================================

Current Conditions:
- Temperature: 78F (24C)
- RealFeel: 80F
- Humidity: 67-68%
- Wind: NNE at 10-20 mph (16.9 km/h)
- Conditions: Cloudy morning, partly cloudy afternoon, hazy

Tonight:
- Low: 71F
- Conditions: Generally clear and hazy

Summary: Pleasant spring day in Dubai with mild temperatures, some cloud
cover, and hazy conditions typical for the season.

Sources:
- AccuWeather: https://www.accuweather.com/en/ae/dubai/323091/current-weather/323091
- Weather Underground: https://www.wunderground.com/weather/ae/dubai
- Time and Date: https://www.timeanddate.com/weather/united-arab-emirates/dubai
```

