---
id: warp-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:45.460850
---

# KNOWLEDGE EXTRACT: Warp
> **Extracted on:** 2026-03-30 13:52:52
> **Source:** Warp

---

## File: `.gitignore`
```
.trunk/*

```

## File: `.gitmodules`
```
[submodule "themes"]
	path = themes
	url = git@github.com:warpdotdev/themes.git
[submodule "keysets"]
	path = keysets
	url = git@github.com:warpdotdev/keysets.git
[submodule "workflows"]
	path = workflows
	url = git@github.com:warpdotdev/workflows.git
```

## File: `LICENSE`
```
Warp (https://warp.dev) is currently closed-source. Whether Warp will be open sourced and the strategy around it if so, are both still a work in progress.
We're having a discussion on open sourcing Warp, possible licenses, and also the business model in [GitHub discussion #400](https://github.com/warpdotdev/Warp/discussions/400)
```

## File: `README.md`
```markdown
<a href="https://www.warp.dev">
    <img width="1024" alt="Warp Agentic Development Environment product preview" src="https://storage.googleapis.com/warpdotdev-content/Readme.png">
</a>

<p align="center">
  <a href="https://www.warp.dev">Website</a>
  ·
  <a href="https://www.warp.dev/code">Code</a>
  ·
  <a href="https://www.warp.dev/agents">Agents</a>
  ·
  <a href="https://www.warp.dev/terminal">Terminal</a>
  ·
  <a href="https://www.warp.dev/drive">Drive</a>
  ·
  <a href="https://docs.warp.dev">Docs</a>
  ·
  <a href="https://www.warp.dev/blog/how-warp-works">How Warp Works</a>
</p>

<h1></h1>

## About

This is an issues-only repo for [Warp](https://www.warp.dev) where you can submit issues, bugs and feature requests.

We built Warp to solve two problems we kept hitting as a team writing software: terminals haven't kept up with how developers work today, and agentic development tools don't scale beyond your laptop.

**Warp is a modern terminal built for coding with agents.** Warp brings the terminal into the 21st century with modern UI and code editing features. Use Warp’s SOTA built-in agent Oz, or run CLI coding agents like Claude Code, Codex, or Gemini CLI.

**Oz is an orchestration platform for cloud agents.** Spin up unlimited parallel coding agents that are programmable, auditable, and fully steerable. Automate repetitive tasks, build on agents, and run them in parallel in the cloud. [Create an agent →](http://warp.dev/oz) 

## Installation

You can [download Warp](https://www.warp.dev/download) and [read our docs](https://docs.warp.dev/) for platform-specific instructions.

## Changelog and Releases

We try to release an update weekly, typically on Thursdays. Read our [changelog (release notes).](https://docs.warp.dev/getting-started/changelog)

## Issues, Bugs, and Feature Requests

Please [search](https://github.com/warpdotdev/warp/issues?q=is%3Aissue+is%3Aopen+a+sort%3Areactions-%2B1-desc) through our existing issues for your bug (including workarounds) or feature request.

If you can't find a solution above, please file issue requests [in this repo!](https://github.com/warpdotdev/warp/issues/new/choose)
We kindly ask that you please use our issue templates to make the issues easier to track for our team.

## Open Source & Contributing

We are planning to first open-source our Rust UI framework, and then parts and potentially all of our client codebase. The server portion of Warp will remain closed-source for now.

You can see how we’re thinking about open source here: [https://github.com/warpdotdev/Warp/discussions/400](https://github.com/warpdotdev/Warp/discussions/400)

As a side note, we are open-sourcing our extension points as we go. The community has already been [contributing new themes](https://github.com/warpdotdev/themes), and our [Workflows repository](https://github.com/warpdotdev/workflows) is open for sharing and collaborating on useful command patterns.

Interested in joining the team? See our [open roles](https://www.warp.dev/careers) and feel free to email us: hello at warpdotdev

## Support and Questions

1. See our [docs](https://docs.warp.dev/) for a comprehensive guide to Warp's features.
2. Join our [Slack Community](https://go.warp.dev/join-preview) or [Discord](https://discord.com/invite/warpdotdev) to connect with other users and get help from the Warp team.
3. Try our [Preview build](https://www.warp.dev/download-preview) to test Warp's newest and latest experimental features.

For anything else, please don't hesitate to reach out via email at hello at warpdotdev

## Community Guidelines

At a high level, we ask everyone to be respectful and empathetic. We follow the [GitHub Community Guidelines](https://docs.github.com/en/github/site-policy/github-community-guidelines):

* Be welcoming and open-minded
* Respect each other
* Communicate with empathy
* Be clear and stay on topic

## Open Source Dependencies

We'd like to call out a few of the [open source dependencies](https://docs.warp.dev/help/licenses) that have helped Warp to get off the ground:

* [Tokio](https://github.com/tokio-rs/tokio)
* [NuShell](https://github.com/nushell/nushell)
* [Fig Completion Specs](https://github.com/withfig/autocomplete)
* [Warp Server Framework](https://github.com/seanmonstar/warp)
* [Alacritty](https://github.com/alacritty/alacritty)
* [Hyper HTTP library](https://github.com/hyperium/hyper)
* [FontKit](https://github.com/servo/font-kit)
* [Core-foundation](https://github.com/servo/core-foundation-rs)
* [Smol](https://github.com/smol-rs/smol)
```

