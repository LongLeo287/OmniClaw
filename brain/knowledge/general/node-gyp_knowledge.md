---
id: node-gyp-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:12.019809
---

# OmniClaw Knowledge Report: node-gyp

## Tech Stack
Node.js/NPM

## File Statistics
```json
{
  "": 11,
  ".json": 7,
  ".gypi": 3,
  ".md": 23,
  ".sh": 2,
  ".py": 64,
  ".js": 37,
  ".bat": 1,
  ".toml": 1,
  ".ninja": 1,
  ".cc": 3,
  ".APACHE": 1,
  ".BSD": 1,
  ".typed": 1,
  ".el": 2,
  ".gyp": 3,
  ".fontified": 1,
  ".pbfilespec": 1,
  ".xclangspec": 1,
  ".cs": 1,
  ".txt": 13,
  ".c": 1
}
```

## README Snippet
```markdown
# `node-gyp` - Node.js native addon build tool

This is a fork of the original and excellent `node-gyp` with only one feature added: Support for Node v12. The Electron maintainers took this step to ensure that our community can easily build their Electron apps on macOS Sequoia. Here is what happened:

- Python 3.12 has removed `distutils`, which `node-gyp` below v10 depended on.
- macOS Sequoia updated their default version of Python to 3.12.
- When installing a native Node addon, a lot of code bases suddenly showed `ModuleNotFoundError: No module named 'distutils'` error messages that are cryptic for anyone who doesn't have a full understanding of the dependency chain involved

This left the Electron maintainers with the following choices:

1. **Tell the community to manually install either Python 3.11 or `setuptools`**. While this fixes the issue, it requires manual user intervention and requires our users to first search for the error message.
2. **Upgrade to `node-gyp` v10**. That would have required a bump in minimum Node.js version for `@electron/rebuild` and in turn all other packages that depend on it, resulting in major version bumps across the entire ecosystem. This too doesn't fix the issue for our users without them performing manual major version upgrades.
3. **Fork node-gyp v10, make it compatible with Node.js v12, and only patch our tools**: We chose this option to get a fix out to our users as quickly and painless as possible.

Electron has a major version bum
```

**Processed by OmniClaw Automated Intake**