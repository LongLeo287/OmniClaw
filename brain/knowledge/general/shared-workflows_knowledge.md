---
id: shared-workflows-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.207695
---

# OmniClaw Knowledge Report: shared-workflows

## Tech Stack
Node.js/NPM

## File Statistics
```json
{
  "": 16,
  ".json": 15,
  ".yaml": 29,
  ".lock": 3,
  ".md": 69,
  ".mjs": 1,
  ".sh": 13,
  ".yml": 8,
  ".mod": 8,
  ".sum": 8,
  ".go": 39,
  ".js": 2,
  ".ts": 12,
  ".txt": 2,
  ".mustache": 1,
  ".bash": 1,
  ".bats": 1,
  ".png": 1
}
```

## README Snippet
```markdown
# shared-workflows

[![OpenSSF Scorecard][scorecard image]][scorecard]

A public-facing, centralized place to store reusable GitHub workflows and action
used by Grafana Labs. See the `actions/` directory for the individual actions
themselves.

[scorecard]: https://scorecard.dev/viewer/?uri=github.com/grafana/shared-workflows
[scorecard image]: https://api.scorecard.dev/projects/github.com/grafana/shared-workflows/badge

## Custom Renovate config

This is a monorepo containing several Actions. When we release a workflow, we create a tag `<workflow name>/v<workflow version>`.

While Dependabot can update references to these actions, Renovate can't do it out of the box. It can, however, be configured to do so:

```json
{
  "packageRules": [
    {
      "matchPackageNames": ["grafana/shared-workflows"],
      "versioning": "regex:^(?<compatibility>.*)[-/]v?(?<major>\\d+)\\.(?<minor>\\d+)\\.(?<patch>\\d+)?$",
      "additionalBranchPrefix": "{{ lookup (split newVersion \"/\") 0 }}-",
      "commitMessagePrefix": "chore(deps):",
      "commitMessageAction": "update",
      "commitMessageTopic": "{{depName}}/{{ lookup (split newVersion \"/\") 0 }} action",
      "commitMessageExtra": "to {{ lookup (split newVersion \"/\") 1 }}"
    }
  ]
}
```

## Notes

### Configure your IDE to run Prettier

[Prettier] will run in CI to ensure that files are formatted correctly. To ensure
that your code is formatted correctly before you commit, set up your IDE to run
Prettier on save.

Or from the
```

**Processed by OmniClaw Automated Intake**