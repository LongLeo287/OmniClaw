---
id: nullclaw-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:13.208690
---

# KNOWLEDGE EXTRACT: nullclaw
> **Extracted on:** 2026-03-30 17:49:31
> **Source:** nullclaw

---

## File: `nullclaw.md`
```markdown
# 📦 nullclaw/nullclaw [🔖 PENDING/APPROVE]
🔗 https://github.com/nullclaw/nullclaw
🌐 https://nullclaw.io

## Meta
- **Stars:** ⭐ 6793 | **Forks:** 🍴 812
- **Language:** Zig | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

## README (trích đầu)
```
Want a simpler way to install and configure nullclaw with a UI? Try [nullhub](https://github.com/nullclaw/nullhub)! (currently in beta)

[nullhub](https://github.com/nullclaw/nullhub) provides a UI layer for the Null ecosystem: simpler nullclaw setup and configuration, orchestration from [nullboiler](https://github.com/nullclaw/nullboiler), observability from [nullwatch](https://github.com/nullclaw/nullwatch), and task tracking from [nulltickets](https://github.com/nullclaw/nulltickets).

<p align="center">
  <img src="nullclaw.png" alt="nullclaw" width="200" />
</p>

<h1 align="center">NullClaw</h1>

<p align="center">
  <strong>Null overhead. Null compromise. 100% Zig. 100% Agnostic.</strong><br>
  <strong>678 KB binary. ~1 MB RAM. Boots in <2 ms. Runs on anything with a CPU.</strong>
</p>

<p align="center">
  <a href="https://github.com/nullclaw/nullclaw/actions/workflows/ci.yml"><img src="https://github.com/nullclaw/nullclaw/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://nullclaw.github.io"><img src="https://img.shields.io/badge/docs-nullclaw.github.io-informational" alt="Documentation" /></a>
  <a href="https://discord.gg/Bfmdua22Ud"><img src="https://img.shields.io/badge/discord-join%20community-5865F2?logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT" /></a>
</p>

The smallest fully autonomous AI assistant infrastructure — a static Zig binary that fits on any $5 board, boots in milliseconds, and requires nothing but libc.

Docs: [English](../../../README.md) · [中文](../../../README.md) · [Contributing](CONTRIBUTING.md) · [Discord](https://discord.gg/Bfmdua22Ud)

```
678 KB binary · <2 ms startup · 5,300+ tests · 50+ providers · 19 channels · Pluggable everything
```

### Features

- **Impossibly Small:** 678 KB static binary — no runtime, no VM, no framework overhead.
- **Near-Zero Memory:** ~1 MB peak RSS. Runs comfortably on the cheapest ARM SBCs and microcontrollers.
- **Instant Startup:** <2 ms on Apple Silicon, <8 ms on a 0.8 GHz edge core.
- **True Portability:** Single self-contained binary across ARM, x86, and RISC-V. Drop it anywhere, it just runs.
- **Feature-Complete:** 50+ providers, 19 channels, 35+ tools, 10 memory engines, multi-layer sandbox, tunnels, hardware peripherals, MCP, subagents, streaming, voice — the full stack.

### Why nullclaw

- **Lean by default:** Zig compiles to a tiny static binary. No allocator overhead, no garbage collector, no runtime.
- **Secure by design:** pairing, strict sandboxing (landlock, firejail, bubblewrap, docker), explicit allowlists, workspace scoping, encrypted secrets.
- **Fully swappable:** core systems are vtable interfaces (providers, channels, tools, memory, tunnels, peripherals, observers, runtimes).
- **No lock-in:** OpenAI-compatible provider support + pluggable custom endpoints.

## Benchmark Snapshot

Local machine benchmark (macOS arm64, Feb 2026), normaliz
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

