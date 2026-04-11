# Knowledge Dump for claudy_registry

## File: README.md
```
# Claudy Registry

**Skill ID:** `claudy_registry` | **Domain:** `data-tools` | **Tier:** 3

## Summary
This plugin fetches real-time data from an external API and updates the Claudy registry.

## Usage
Consult `payload/` for concrete source code and implementation patterns.

```

## File: schema.json
```
{
  "id": "claudy_registry",
  "name": "Claudy Registry",
  "version": "1.0.0",
  "tier": 3,
  "status": "active",
  "domain": "data-tools",
  "cost_tier": "standard",
  "load_on_boot": false,
  "path": "$OMNICLAW_ROOT\\ecosystem\\skills\\claudy_registry\\SKILL.md",
  "accessible_by": [
    "Orchestrator",
    "Claude Code"
  ],
  "dependencies": [],
  "exposed_functions": [
    {
      "name": "reference",
      "description": "Reference for claudy_registry",
      "input": "string",
      "output": "string"
    }
  ],
  "consumed_by": [],
  "emits_events": [],
  "listens_to": [],
  "tags": [
    "data"
  ]
}
```

## File: SKILL.md
```
---
id: claudy_registry
name: Claudy Registry
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: data-tools
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Reference knowledge and templates from claudy_registry.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["data"]
---

# Claudy Registry

## Overview
This plugin fetches real-time data from an external API and updates the Claudy registry.

## Usage
Agents working on `data-tools` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `data-tools`
- Source templates available in `payload/`
- Tags: data

```

## File: _DIR_IDENTITY.md
```
---
id: claudy_registry
type: skill
owner: OA Forge Pipeline
registered_at: 2026-04-09
tags: ["data", "forge-in-place", "data-tools"]
---

# Claudy Registry

Forged in-place from raw repository: `claudy_registry`
Domain: `data-tools`

```

## File: payload\contributing.md
```
# Contributing to claudy-registry

Thank you for contributing to the Claudy plugin marketplace!

## How to Submit a Plugin

1. **Fork** this repository
2. **Create** your plugin directory: `plugins/{your-github-username}/{plugin-id}/`
3. **Add** a `manifest.json` (see field reference below)
4. **For inline plugins** — add source files (`.md`) alongside `manifest.json`
5. **Open a PR** — CI will validate your plugin automatically

---

## Plugin Directory Structure

```
plugins/
└── {org}/              ← your GitHub username
    └── {plugin-id}/    ← lowercase alphanumeric + hyphens
        ├── manifest.json
        └── skill.md    ← inline only (skill/command)
```

---

## Field Reference

### Required (all kinds)

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | `"{plugin-id}@{org}"` — must match the directory path (e.g. `"my-skill@myusername"`). |
| `kind` | string | `"mcp"`, `"skill"`, or `"command"` |
| `name` | string | Display name. 2–60 characters. |
| `description` | string | What it does. 10–200 characters. |
| `author` | string | Must match org directory (your GitHub username). |
| `tags` | array of strings | At least one tag. Used for search. |
| `iconSF` | string | SF Symbols name (e.g. `"gear"`, `"network"`). |
| `featured` | boolean | Set to `false` for community submissions. |
| `version` | string | Plugin version in semver format (e.g. `"1.0.0"`). Bump on every change. |

### MCP plugins (`kind: "mcp"`)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `mcpTransport` | string | Yes | `"stdio"` or `"http"` |
| `mcpInstallCommand` | string | stdio | Command to install/run (e.g. `"npx"`, `"uvx"`) |
| `mcpInstallArgs` | array | stdio | Args for install command |
| `mcpUrl` | string (URI) | http | URL for the HTTP MCP server |

### File-based plugins (skill/command)

| Field | Type | Description |
|-------|------|-------------|
| `githubRepo` | string | `"owner/repo"` format |
| `githubPath` | string | Path to plugin files within the repo |

**External reference** — source lives in another repo:
```json
{
  "githubRepo": "someuser/their-repo",
  "githubPath": "path/to/skill"
}
```

**Inline** — source files live in this registry:
```json
{
  "githubRepo": "markgravity/claudy-registry",
  "githubPath": "plugins/{org}/{plugin-id}"
}
```

> Include the `.md` source file alongside `manifest.json` for inline plugins.

---

## Forbidden Fields

Never include these in `manifest.json` — they are managed by Firestore:

- `installCount`
- `averageRating`
- `ratingCount`
- `ratingSum`

CI will reject any plugin containing these fields.

---

## Example: External MCP Plugin

`plugins/myusername/my-mcp-server/manifest.json`:
```json
{
  "id": "my-mcp-server@myusername",
  "kind": "mcp",
  "name": "My MCP Server",
  "description": "Does something useful via the Model Context Protocol.",
  "author": "myusername",
  "tags": ["mcp", "utility"],
  "iconSF": "network",
  "featured": false,
  "version": "1.0.0",
  "mcpTransport": "stdio",
  "mcpInstallCommand": "npx",
  "mcpInstallArgs": ["-y", "@myusername/my-mcp-server@latest"]
}
```

## Example: Inline Skill

`plugins/myusername/my-skill/manifest.json`:
```json
{
  "id": "my-skill@myusername",
  "kind": "skill",
  "name": "My Skill",
  "description": "A helpful skill that does something great.",
  "author": "myusername",
  "tags": ["productivity"],
  "iconSF": "wand.and.stars",
  "featured": false,
  "version": "1.0.0",
  "githubRepo": "markgravity/claudy-registry",
  "githubPath": "plugins/myusername/my-skill"
}
```

`plugins/myusername/my-skill/skill.md`:
```markdown
Your skill prompt content here...
```

---

## Validation

Run the validator locally before opening a PR:

```bash
pip install -r scripts/requirements.txt
python scripts/validate_plugin.py plugins/myusername/my-skill/manifest.json
```

---

## SF Symbols Reference

Pick an icon name from [SF Symbols](https://developer.apple.com/sf-symbols/). Common ones:
- `gear` — settings/config
- `network` — networking/MCP
- `wand.and.stars` — AI/generation
- `terminal` — CLI tools
- `doc.text` — documentation
- `magnifyingglass` — search

---

## Review Process

1. CI validates your `manifest.json` automatically
2. A maintainer reviews the PR
3. On merge, the plugin is automatically synced to Firestore and appears in the Claudy app

```

## File: payload\DEEP_KNOWLEDGE.md
```
# Deep Matrix Profile: CIV_FETCHED_claudy-registry_121551

# Deep Knowledge Report for Claudy Plugin Registry Repository

## Overview

This repository serves as a community-driven plugin registry for the Claudy macOS app. It includes scripts to manage plugins by backfilling version information, syncing plugins to Firestore, and validating manifest files. This report delves into the architectural patterns, core algorithms, and primary mechanisms of these scripts.

---

### 1. Architectural Patterns

#### 1.1 Command Line Interface (CLI) Scripts
- **Purpose**: The repository contains several CLI scripts designed for specific tasks such as backfilling version information, syncing plugins to Firestore, and validating plugin manifests.
- **Usage**:
  - `backfill_version.py`: Sets a default version on missing fields in the Firestore database.
  - `sync_to_firestore.py`: Synchronizes all plugins from local directories to Firestore while preserving certain metadata fields.
  - `validate_plugin.py`: Validates manifest files against predefined schemas and paths.

#### 1.2 Dependency Injection
- **Usage**: The scripts use environment variables (`FIREBASE_SERVICE_ACCOUNT_JSON`) for configuration, which is a form of dependency injection. This allows the scripts to be flexible in how they access Firebase services.
- **Example**:
  ```python
  sa_json = os.environ.get("FIREBASE_SERVICE_ACCOUNT_JSON")
  if not sa_json:
      # Handle error or use command-line argument
  ```

#### 1.3 Error Handling and Logging
- **Usage**: The scripts include robust error handling mechanisms to ensure that any issues are logged appropriately.
- **Example**:
  ```python
  try:
      data = load_plugin(plugin_path)
      plugin_id = data.get("id")
      if not plugin_id:
          print(f"ERROR: {plugin_path} missing 'id'", file=sys.stderr)
          errors += 1
          continue
  except Exception as e:
      print(f"ERROR syncing {plugin_path}: {e}", file=sys.stderr)
      errors += 1
  ```

---

### 2. Core Algorithms

#### 2.1 Backfilling Version Information (`backfill_version.py`)
- **Algorithm**:
  - The script reads the `plugins` collection in Firestore.
  - It checks if each document has a `version` field.
  - If missing, it sets the default version to `"1.0.0"` and logs an update message.
  - This process is safe to run multiple times as it only updates documents that lack the `version` field.

#### 2.2 Synchronizing Plugins (`sync_to_firestore.py`)
- **Algorithm**:
  - The script initializes Firebase using a service account JSON file from environment variables or command-line arguments.
  - It finds all plugin manifest files in specified directories.
  - For each manifest, it loads the data and strips out certain metadata fields to prevent overwriting Firestore values.
  - It then syncs this data to the `plugins` collection in Firestore using merge operations.

#### 2.3 Validating Plugin Manifests (`validate_plugin.py`)
- **Algorithm**:
  - The script validates each manifest file against a predefined schema and checks for structural integrity.
  - It ensures that required fields are present, such as `id`, `author`, and specific plugin types like MCP.
  - It also enforces naming conventions to ensure consistency in the plugin registry.

---

### 3. Primary Mechanisms

#### 3.1 Firebase Integration
- **Mechanism**: The scripts use the `firebase_admin` library to interact with Firestore databases.
- **Example**:
  ```python
  cred = credentials.Certificate(json.loads(sa_json))
  firebase_admin.initialize_app(cred)
  db = firestore.client()
  ```

#### 3.2 JSON Schema Validation
- **Mechanism**: The validation script uses the `jsonschema` library to validate manifest files against a predefined schema.
- **Example**:
  ```python
  with open(path) as f:
      data = json.load(f)
  validator = jsonschema.Draft7Validator(schema)
  schema_errors = list(validator.iter_errors(data))
  ```

#### 3.3 Path and Directory Handling
- **Mechanism**: The scripts handle paths and directories to locate plugin manifest files.
- **Example**:
  ```python
  plugins_dir = Path(__file__).parent.parent / "plugins"
  changed = os.environ.get("CHANGED_MANIFESTS", "").strip()
  if changed:
      paths = []
      for rel in changed.split(":"):
          rel = rel.strip()
          if rel:
              p = PLUGINS_DIR.parent / rel
              if p.exists():
                  paths.append(p)
      if paths:
          return paths
  ```

---

### 4. Best Practices and Recommendations

#### 4.1 Security
- **Recommendation**: Ensure that the service account JSON is securely stored and not exposed in version control.
- **Example**:
  - Use environment variables or secure vaults to manage sensitive information.

#### 4.2 Error Handling
- **Recommendation**: Implement comprehensive error handling to ensure that any issues are logged and can be traced back to their source.
- **Example**:
  ```python
  try:
      # Code block
  except Exception as e:
      print(f"ERROR: {e}", file=sys.stderr)
  ```

#### 4.3 Performance Optimization
- **Recommendation**: Optimize the scripts for performance by minimizing database calls and ensuring that data is processed efficiently.
- **Example**:
  - Batch operations in Firestore to reduce write latency.

---

### Conclusion

This report provides a detailed analysis of the architectural patterns, core algorithms, and primary mechanisms used in the Claudy plugin registry repository. By understanding these components, contributors can effectively contribute to and maintain the repository's functionality.
```

## File: payload\index.js
```
const axios = require('axios');
const { getFirestore, collection, addDoc } = require('firebase-admin/firestore');

// Initialize Firestore
const db = getFirestore();

async function fetchData() {
  try {
    const response = await axios.get('https://api.example.com/data');
    const data = response.data;
    
    // Write to Firestore
    const docRef = await addDoc(collection(db, 'data'), { ...data });
    console.log(`Document written with ID: ${docRef.id}`);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// Schedule the function to run every hour
setInterval(fetchData, 3600000);
```

## File: payload\manifest.json
```
{"name": "CIV_FETCHED_claudy-registry_121551", "version": "1.0.1", "type": "data-fetcher", "description": "Fetches real-time data from an external API and updates the Claudy registry.", "dependencies": ["firebase-admin", "axios"], "permissions": ["read:firestore", "write:firestore"]}
```

## File: payload\package.json
```
{"name": "CIV_FETCHED_claudy-registry_121551", "version": "1.0.1", "main": "index.js", "dependencies": {"firebase-admin": ">=9.8.0", "axios": ">=0.21.1"}, "devDependencies": {}, "scripts": {"start": "node index.js"}}
```

## File: payload\README.md
```
# CIV_FETCHED_claudy-registry_121551
This plugin fetches real-time data from an external API and updates the Claudy registry.

## Installation
```bash
npm install
```

## Usage
Run the following command to start the plugin:
```bash
cd path/to/plugin
npm start
```
```

## File: payload\upgrade_proposal.md
```
# System Upgrade Proposal: CIV_FETCHED_claudy-registry_121551

> [!TIP]
> This actionable proposal was automatically drafted by OA Academy because this repository scored 9/10.

## Application Vision for OmniClaw
Analyze each submitted plugin (manifest.json) for its type and functionality. If a new plugin is introduced, create a new entry in the Claudy marketplace. If an existing plugin's manifest needs updating or upgrading, identify the relevant component within Claudy and update it accordingly. Ensure that all changes are validated locally before merging to prevent issues with Firestore synchronization.

## Next Action Items
1. Review the `DEEP_KNOWLEDGE.md` to understand the architecture.
2. Isolate the target modules identified in the vision.
3. Wrap the modules into an OmniClaw Skill or Agent in `ecosystem/`.

```

## File: payload\_DIR_IDENTITY.md
```
---
id: claudy_registry
type: plugin
owner: OA
registered_at: 2026-04-09T17:25:59.433306
tags: ["auto-cloned", "real-time data", "API integration", "Firestore", "oa-assimilated"]
---

# claudy_registry

## Assimilation Report
This plugin fetches real-time data from an external API and updates a Firestore database within the Claudy registry. It runs every hour to ensure the data remains current.

## Application for OmniClaw
OmniClaw can integrate this plugin by adding it as a module within its agent architecture. This will allow OmniClaw to fetch and update real-time data from various APIs, enhancing its capabilities in data management and integration. The plugin could be modified to support multiple API endpoints or different database backends if needed.

```

## File: payload\.github\pull_request_template.md
```
## Plugin Submission

**Plugin name:**
**Author (GitHub username):**
**Kind:** <!-- mcp / skill / command -->

---

### Checklist

- [ ] `manifest.json` is located at `plugins/{org}/{plugin-id}/manifest.json`
- [ ] `id` is `{plugin-id}@{org}` matching the directory path
- [ ] `author` matches the org directory (my GitHub username)
- [ ] No stats fields (`installCount`, `averageRating`, etc.) in `manifest.json`
- [ ] For MCP plugins: `mcpTransport` is set and transport-specific fields are present
- [ ] For inline plugins: source files (`.md`) are included alongside `manifest.json`
- [ ] `name` is 2–60 characters
- [ ] `description` is 10–200 characters
- [ ] `iconSF` is a valid SF Symbols name
- [ ] I have tested the plugin locally

### Description

<!-- Briefly describe what this plugin does and why it's useful -->

### Notes for maintainers

<!-- Anything else reviewers should know -->

```

## File: payload\.github\ISSUE_TEMPLATE\new_plugin.md
```
---
name: New Plugin Submission
about: Submit a new plugin to the Claudy marketplace
title: "[Plugin] "
labels: plugin-submission
assignees: ""
---

## Plugin Details

**Name:**
**Author (GitHub username):**
**Kind:** <!-- mcp / skill / command -->
**GitHub repo (if external):**

## Description

<!-- What does this plugin do? -->

## Checklist

- [ ] The plugin follows the naming convention (`plugins/{org}/{plugin-id}/manifest.json`)
- [ ] I'm ready to open a PR

## Notes

<!-- Anything else we should know? -->

```

## File: payload\.github\workflows\sync-to-firestore.yml
```
name: Sync Plugins to Firestore

on:
  push:
    branches:
      - main
    paths:
      - "plugins/**"

jobs:
  sync:
    name: Sync all plugins to Firestore
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r scripts/requirements.txt

      - name: Get changed plugin manifests
        run: |
          CHANGED=$(git diff --name-only --diff-filter=AM HEAD~1 HEAD \
            | grep -E '^plugins/.+/manifest\.json$' \
            | paste -sd ':' - || true)
          echo "CHANGED_MANIFESTS=$CHANGED" >> $GITHUB_ENV

      - name: Sync to Firestore
        env:
          FIREBASE_SERVICE_ACCOUNT_JSON: ${{ secrets.FIREBASE_SERVICE_ACCOUNT_JSON }}
        run: python scripts/sync_to_firestore.py

```

## File: payload\.github\workflows\validate-pr.yml
```
name: Validate Plugin PR

on:
  pull_request:
    paths:
      - "plugins/**"

jobs:
  validate:
    name: Validate changed manifest.json files
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r scripts/requirements.txt

      - name: Find changed manifest.json files
        id: changed
        run: |
          BASE="${{ github.event.pull_request.base.ref }}"
          CHANGED=$(git diff --name-only --diff-filter=AM "origin/${BASE}...HEAD" \
            | grep -E '^plugins/.+/manifest\.json$' || true)
          echo "files<<EOF" >> "$GITHUB_OUTPUT"
          echo "$CHANGED" >> "$GITHUB_OUTPUT"
          echo "EOF" >> "$GITHUB_OUTPUT"

      - name: Validate plugins
        run: |
          FILES="${{ steps.changed.outputs.files }}"
          if [ -z "$FILES" ]; then
            echo "No manifest.json files changed."
            exit 0
          fi
          echo "$FILES" | xargs python scripts/validate_plugin.py

```

