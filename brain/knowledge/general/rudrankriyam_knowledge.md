---
id: rudrankriyam-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:10.116653
---

# KNOWLEDGE EXTRACT: rudrankriyam
> **Extracted on:** 2026-03-30 17:53:02
> **Source:** rudrankriyam

---

## File: `app-store-connect-cli-skills.md`
```markdown
# 📦 rudrankriyam/app-store-connect-cli-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/rudrankriyam/app-store-connect-cli-skills
🌐 https://asccli.sh

## Meta
- **Stars:** ⭐ 604 | **Forks:** 🍴 34
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Skills to automate app store deployed and everything related to it using the asc cli

## README (trích đầu)
```
# asc cli skills

A collection of Agent Skills for shipping with the [asc cli](https://github.com/rudrankriyam/App-Store-Connect-CLI) (`asc`). These skills are designed for zero-friction automation around builds, TestFlight, metadata, submissions, and signing.

This is a community-maintained, unofficial skill pack and is not affiliated with Apple.

Skills follow the Agent Skills format.

## Installation

Install this skill pack:

```bash
npx skills add rudrankriyam/app-store-connect-cli-skills
```

## Available Skills

### asc-cli-usage

Guidance for running `asc` commands (canonical verbs, flags, pagination, output, auth).

**Use when:**
- You need the correct `asc` command or flag combination
- You want JSON-first output and pagination tips for automation

**Example:**

```bash
Find the right asc command to list all builds for app 123456789 as JSON and paginate through everything.
```

### asc-workflow

Define and run repo-local automation graphs using `asc workflow` and `.asc/workflow.json`.

**Use when:**
- You are migrating from lane-based automation to repo-local workflows
- You need multi-step orchestration with machine-parseable JSON output for CI/agents
- You need hooks (`before_all`, `after_all`, `error`), conditionals (`if`), and private helper sub-workflows
- You want validation (`asc workflow validate`) with cycle/reference checks before execution

**Example:**

```bash
Create an asc workflow that stages a release, validates it, and only submits when CONFIRM_RELEASE=true.
```

### asc-app-create-ui

Create a new App Store Connect app via browser automation when no API exists.

**Use when:**
- You need to create an app record (name, bundle ID, SKU, primary language)
- You are comfortable logging in to App Store Connect in a real browser

**Example:**

```bash
Create a new App Store Connect app for com.example.myapp with SKU MYAPP123 and primary language English (U.S.).
```

### asc-xcode-build

Build, archive, export, and manage Xcode version/build numbers before uploading.

**Use when:**
- You need to create an IPA or PKG for upload
- You're setting up CI/CD build pipelines
- You need to configure ExportOptions.plist
- You're troubleshooting encryption compliance issues

**Example:**

```bash
Archive and export my macOS app as a PKG I can upload to App Store Connect.
```

### asc-shots-pipeline

Agent-first screenshot pipeline using xcodebuild/simctl, AXe, JSON plans, `asc screenshots frame` (experimental), and `asc screenshots upload`.

**Use when:**
- You need a repeatable simulator screenshot automation flow
- You want AXe-based UI driving before capture
- You need a staged pipeline (capture -> frame -> upload)
- You need to discover supported frame devices (`asc screenshots list-frame-devices`)
- You want pinned Koubou guidance for deterministic framing (`koubou==0.18.0`)

**Example:**

```bash
Build my iOS app, capture the home and settings screens in the simulator, frame them, and prepare them for upload.
```

### asc-release-f
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

