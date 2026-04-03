---
id: sawyerhood-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:10.701729
---

# KNOWLEDGE EXTRACT: SawyerHood
> **Extracted on:** 2026-03-30 17:53:03
> **Source:** SawyerHood

---

## File: `dev-browser.md`
```markdown
# 📦 SawyerHood/dev-browser [🔖 PENDING/APPROVE]
🔗 https://github.com/SawyerHood/dev-browser


## Meta
- **Stars:** ⭐ 4629 | **Forks:** 🍴 284
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A Claude Skill to give your agent the ability to use a web browser

## README (trích đầu)
```
<p align="center">
  <img src="assets/header.png" alt="Dev Browser - Browser automation for Claude Code" width="100%">
</p>

Brought to you by [Do Browser](https://dobrowser.io).

A browser automation tool that lets AI agents and developers control browsers with sandboxed JavaScript scripts.

**Key features:**

- **Sandboxed execution** - Scripts run in a QuickJS WASM sandbox with no host access
- **Persistent pages** - Navigate once, interact across multiple scripts
- **Auto-connect** - Connect to your running Chrome or launch a fresh Chromium
- **Full Playwright API** - goto, click, fill, locators, evaluate, screenshots, and more

## CLI Installation

```bash
npm install -g dev-browser
dev-browser install    # installs Playwright + Chromium
```

### Quick start

```bash
# Launch a headless browser and run a script
dev-browser --headless <<'EOF'
const page = await browser.getPage("main");
await page.goto("https://example.com");
console.log(await page.title());
EOF

# Connect to your running Chrome (enable at chrome://inspect/#remote-debugging)
dev-browser --connect <<'EOF'
const tabs = await browser.listPages();
console.log(JSON.stringify(tabs, null, 2));
EOF
```

### Windows notes

PowerShell install:

```powershell
npm install -g dev-browser
dev-browser install
```

To attach to a running Chrome instance on Windows:

```powershell
chrome.exe --remote-debugging-port=9222
dev-browser --connect
```

Windows npm installs download the native `dev-browser-windows-x64.exe` release asset during `postinstall`, and the generated npm shims invoke that executable directly.

### Using with AI agents

After installing, just tell your agent to run `dev-browser --help` — the help output includes a full LLM usage guide with examples and API reference. No plugin or skill installation needed.

<details>
<summary>Allowing dev-browser in Claude Code without permission prompts</summary>

By default, Claude Code asks for approval each time it runs a bash command. You can pre-approve `dev-browser` so it runs without permission checks by adding it to the `allow` list in your settings.

**Per-project** — add to `.claude/settings.json` in your project root:

```json
{
  "permissions": {
    "allow": [
      "Bash(dev-browser *)"
    ]
  }
}
```

**Per-user (global)** — add to `~/.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(dev-browser *)"
    ]
  }
}
```

The pattern `Bash(dev-browser *)` matches any command starting with `dev-browser ` followed by arguments (e.g. `dev-browser --headless`, `dev-browser --connect`). This is safe because dev-browser scripts run in a sandboxed QuickJS WASM environment with no host filesystem or network access.

You can also allow related commands in the same list:

```json
{
  "permissions": {
    "allow": [
      "Bash(dev-browser *)",
      "Bash(npx dev-browser *)"
    ]
  }
}
```

> **Tip:** If you've already been prompted and clicked "Always allow", Claude Code adds the specific command pattern auto
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

