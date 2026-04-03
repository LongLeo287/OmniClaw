---
id: github.com-caido-caido-df68bb69-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:36.295628
---

# KNOWLEDGE EXTRACT: github.com_caido_caido_df68bb69
> **Extracted on:** 2026-04-01 16:00:10
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524892/github.com_caido_caido_df68bb69

---

## File: `README.md`
```markdown
<div align="center">
  <img width="1000" alt="image" src="https://user-images.githubusercontent.com/6225588/211916659-567751d1-0225-402b-9141-4145c18b0834.png">

  <br />
  <br />
  <a href="https://caido.io/">Website</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://dashboard.caido.io/">Dashboard</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://docs.caido.io/" target="_blank">Docs</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://links.caido.io/roadmap">Roadmap</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://github.com/caido/caido/tree/main/brand">Branding</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://links.caido.io/www-discord" target="_blank">Discord</a>
  <br />
  <hr />
</div>

## 👋 Welcome

Welcome to Caido! 

Caido aims to help security professionals and enthusiasts audit web applications with efficiency and ease.

Here you can get involved with the development of our software.

You can learn about upcoming Caido features on our [Roadmap](https://links.caido.io/roadmap). We try to release a new version at least once a month, which you can find in our [releases section](https://github.com/caido/caido/releases) or in your [Caido Dashboard](https://dashboard.caido.io).

<img width="1552" alt="intercept" src="https://user-images.githubusercontent.com/6225588/212757627-e1bdb779-7288-4f3f-8490-c932fb77f012.png">

## 💚 Community

Come join our [Discord](https://links.caido.io/www-discord) community and connect with other Caido users! We'd love to have you as part of the conversation and help with any questions you may have.
```

## File: `SECURITY.md`
```markdown
# Caido Security Policy

Thank you for helping make Caido safer for everyone.

## Reporting Security Issues

If you believe you've discovered a security vulnerability in Caido, please report it responsibly. Here’s how to submit your report:

- **Do not** open public GitHub issues, discussions, or pull requests for security vulnerabilities.
- **Instead**, please report a vulnerability via the [Advisory Form](https://github.com/caido/caido/security/advisories)

### Plugin Vulnerabilities

If you discover a security vulnerability in a plugin for Caido, we recommend reporting it directly to the plugin’s author through their Github advisory page. Reporting the issue directly to the author ensures a faster response and resolution, as they are best equipped to address vulnerabilities specific to their plugin. 

### Information to Include
To help us respond effectively, please provide as much of the following information as possible:

- **Type of vulnerability** (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- **Configuration requirements** needed to reproduce the issue
- **Steps to reproduce** the vulnerability (please be as detailed as possible)
- **Proof-of-concept or exploit code** (if available)
- **Potential impact** (how the vulnerability could be exploited)

This information will help us investigate and resolve issues as quickly as possible.

### Known Issues

#### Plugin Capabilities

Due to the flexible nature of our plugin system, plugins in Caido have unrestricted access within the environment. This includes the ability to:
- Access files on your computer.
- Connect to the internet.
- Install or execute additional programs.

**Important Note**: This is a known limitation of the plugin system that cannot be fully restricted at this time. 
We encourage users to exercise caution and verify the source of any plugin before installation.

### Exclusions

Any reported vulnerability that requires an attacker to already have code execution on the host system will be considered not applicable (N/A). This includes issues that depend on compromised environments or systems outside of Caido’s control.

### Response Expectations

As a small team, we appreciate your patience and understanding. 

While we don’t have a guaranteed response timeline, we aim to review all security reports as quickly as possible. 

We prioritize severe vulnerabilities and will keep you updated on our progress as we investigate and work on any necessary fixes.

### Disclosure Policy

We kindly ask that you:
- Allow us time to resolve the issue before making any information public.
- Maintain confidentiality regarding the vulnerability while we work on a fix.

Thank you for your contribution to Caido’s security!
```

## File: `brand/README.md`
```markdown
<h1 align="middle">Brand Guidelines</h1>
<p align="center">
  This is a friendly legal reminder that these graphics are the property of Caido Labs Inc. and are protected under intellectual property laws
</p>

## Definitions

- **Logo**: The C-shaped graphic representation of a fingerprint
- **Name**: The stylized graphic representation of the Caido word

## Please do

- Use the Logo independently from the Name, but show them both when possible
- Use the Colors provided when possible
- Use **Caido** with a capital C when referring to the product
- Place the Name either below or to the right of the Logo

## Please don’t

- Alter the graphics provided
- Display these graphics in a way that implies a relationship, affiliation, or endorsement by Caido Labs Inc. of your product, service, or business
- Use these graphics as part of your product, business, or service’s name
- Claim or cause confusion about the ownership of these graphics

## Colors

| Name       | Hex     | Color                                                                | Usage      |
| ---------- | ------- | -------------------------------------------------------------------- | ---------- |
| **Red**    | #A1223F | ![Red](https://img.shields.io/badge/--A1223F?style=for-the-badge)    | Accent 1   |
| **Yellow** | #D99E4A | ![Yellow](https://img.shields.io/badge/--D99E4A?style=for-the-badge) | Accent 2   |
| **Black**  | #25272D | ![Black](https://img.shields.io/badge/--25272D?style=for-the-badge)  | Background |
```

## File: `prompts/triage.md`
```markdown
# Triager Agent

## About Caido

Caido is a lightweight web security auditing toolkit designed to assist security professionals in identifying and addressing vulnerabilities within web applications. It provides comprehensive tools for traffic interception, analysis, and security testing.

### CLI

Caido consists of two main architectural components:

- Frontend: Handles all user interface elements and interactions
- Backend: Manages the core application logic and processing

These components work together to form the complete CLI experience.

### Desktop

The Desktop application serves as a wrapper around the CLI.

When launched, users can create and manage instances through this connection manager. Each instance provides access to the frontend interface while communicating with the backend services.

### Dashboard

The dashboard is our cloud platform where users can manage their account, teams and team members and subscriptions. It is split into two components:

- dashboard: Handles all user interface elements and interactions
- cloud: Manages the core application logic and processing

These components work together to form the complete dashboard experience.

### Extension

Caido also has a browser extension, which is used to configure the browser in order to interact with a Caido instance.

## Purpose

You are a GitHub issue triaging assistant that helps analyze and categorize GitHub issues.
Your key responsibility is to assign appropriate labels to issues.

### Label Types

You will be provided with the list of available labels and their description when given a triaging task.
Assign at least one of each type of label unless explicitely marked below as "Situational".

Labels are split into the following types:

#### Component

These labels refer to the affected component of the issue. Multiple components may be assigned.

For example, adding a "Race condition" feature would involve the following labels:

- component:backend
  - reason: this is a full feature that will perform request sending, which is done in the backend
- component:frontend
  - reason: this feature will require a UI to interact with the backend

If not explicitely stated, assume that the issue refers to the CLI/Desktop app, not the dashboard or extension.

#### Effort

These labels refer to the time required to implement the issue. If unsure, default to effort:medium

#### Topic

These labels represent various topics to be associated with the issue. You can add as many as necessary, but they must all be relevant to the issue.

#### Tag (Situational)

These labels are miscellaneous categories. Do not apply any unless the issue description explicitely mentions one of them.

#### Audience (Situational)

These labels refer to the user who requested the issue. Do not assign these labels unless the audience is specifically mentionned in the issue description.

#### Bug (Situational)

These labels should only be applied when the requested issue is a bug.

### Guidelines

- Always maintain a systematic and consistent approach to issue categorization.
- Always Be thorough in analyzing issue content before making decisions.
- Always use existing labels, do not suggest new ones.
- Never override existing assigned labels.
- Do not add assign labels if you think the current labels are accurate.
- Each issue should have at least the following label types:
  - Component
  - Effort
  - Topic
```

## File: `scripts/migrate-labels-to-issue-type.sh`
```bash
#!/bin/bash

# This script finds all issues in caido/caido with exactly one label of type 'kind:'
# and updates them to replace the 'kind:' label with 'type=Feature', preserving other labels.

REPO="caido/caido"

echo "Finding issues with exactly one 'kind:' label..."

# Get all issues with exactly one kind: label, outputting number and labels as JSON
issues=$(gh issue list --repo "$REPO" --state all --search 'label:"kind: question"' -L 100 --json number,labels --jq '
  .[] | select((.labels | map(select(.name | startswith("kind:"))) | length) == 1) | {number, labels}
')

# Use jq to iterate over each issue
echo "$issues" | jq -c '.' | while read -r issue; do
  number=$(echo "$issue" | jq -r '.number')
  echo "Updating issue #$number"

  # Update issue type
  gh api \
    --method PATCH \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    --silent \
    -f type=Question \
    /repos/$REPO/issues/$number

  # Remove kind: label
  gh api \
  --method DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  --silent \
  /repos/$REPO/issues/$number/labels/kind:%20question
done
```

## File: `scripts/strip-label-spaces.sh`
```bash
#!/bin/bash

# This script finds all labels in caido/caido and updates them to remove spaces.

REPO="caido/caido"

echo "Finding all labels and stripping spaces..."

# Get all labels as JSON
labels=$(gh label list --repo "$REPO" --json name --limit 1000)

# Use jq to iterate over each label
echo "$labels" | jq -c '.[]' | while read -r label; do
  old_name=$(echo "$label" | jq -r '.name')
  new_name=$(echo "$old_name" | tr -d ' ')
  
  if [ "$old_name" != "$new_name" ]; then
    echo "Renaming label '$old_name' to '$new_name'"
    gh label edit "$old_name" --repo "$REPO" -n "$new_name"
  fi
done
```

