---
id: n8n-skills
type: knowledge
owner: OA_Triage
---
# n8n-skills
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# n8n-skills

**Expert Claude Code skills for building flawless n8n workflows using the n8n-mcp MCP server**

[![GitHub stars](https://img.shields.io/github/stars/czlonkowski/n8n-skills?style=social)](https://github.com/czlonkowski/n8n-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![n8n-mcp](https://img.shields.io/badge/n8n--mcp-compatible-green.svg)](https://github.com/czlonkowski/n8n-mcp)

## Watch the Introduction Video

[![n8n Skills Introduction](skills.png)](https://youtu.be/e6VvRqmUY2Y?si=6Igply3cadjO6Xx0)

---

## 🎯 What is this?

This repository contains **7 complementary Claude Code skills** that teach AI assistants how to build production-ready n8n workflows using the [n8n-mcp](https://github.com/czlonkowski/n8n-mcp) MCP server.

### Why These Skills Exist

Building n8n workflows programmatically can be challenging. Common issues include:
- Using MCP tools incorrectly or inefficiently
- Getting stuck in validation error loops
- Not knowing which workflow patterns to use
- Misconfiguring nodes and their dependencies

These skills solve these problems by teaching Claude:
- ✅ Correct n8n expression syntax ({{}} patterns)
- ✅ How to use n8n-mcp tools effectively
- ✅ Proven workflow patterns from real-world usage
- ✅ Validation error interpretation and fixing
- ✅ Operation-aware node configuration

---

## 📚 The 7 Skills

### 1. **n8n Expression Syntax**
Teaches correct n8n expression syntax and common patterns.

**Activates when**: Writing expressions, using {{}} syntax, accessing $json/$node variables, troubleshooting expression errors.

**Key Features**:
- Core variables ($json, $node, $now, $env)
- **Critical gotcha**: Webhook data is under `$json.body`
- Common mistakes catalog with fixes
- When NOT to use expressions (Code nodes!)

### 2. **n8n MCP Tools Expert** (HIGHEST PRIORITY)
Expert guide for using n8n-mcp MCP tools effectively.

**Activates when**: Searching for nodes, validating configurations, accessing templates, managing workflows.

**Key Features**:
- Tool selection guide (which tool for which task)
- nodeType format differences (nodes-base.* vs n8n-nodes-base.*)
- Validation profiles (minimal/runtime/ai-friendly/strict)
- Smart parameters (branch="true" for IF nodes)
- Auto-sanitization system explained

**Most Important**: Teaches correct MCP tool usage patterns and parameter formats

### 3. **n8n Workflow Patterns**
Build workflows using 5 proven architectural patterns.

**Activates when**: Creating workflows, connecting nodes, designing automation.

**Key Features**:
- 5 proven patterns (webhook processing, HTTP API, database, AI, scheduled)
- Workflow creation checklist
- Real examples from 2,653+ n8n templates
- Connection best practices
- Pattern selection guide

### 4. **n8n Validation Expert**
Interpret validation errors and guide fixing.

**Activates when**: Validation fails, debugging workflow errors, handling false positives.

**Key Features**:
- Validation loop workflow
- Real error catalog
- Auto-sanitization behavior explained
- False positives guide
- Profile selection for different stages

### 5. **n8n Node Configuration**
Operation-aware node configuration guidance.

**Activates when**: Configuring nodes, understanding property dependencies, setting up AI workflows.

**Key Features**:
- Property dependency rules (e.g., sendBody → contentType)
- Operation-specific requirements
- AI connection types (8 types for AI Agent workflows)
- Common configuration patterns

### 6. **n8n Code JavaScript**
Write effective JavaScript code in n8n Code nodes.

**Activates when**: Writing JavaScript in Code nodes, troubleshooting Code node errors, making HTTP requests with $helpers, working with dates.

**Key Features**:
- Data access patterns ($input.all(), $input.first(), $input.item)
- **Critical gotcha**: Webhook data under `$json.body`
- Correct return format: `[{json: {...}}]`
- Built-in functions ($helpers.httpRequest(), DateTime, $jmespath())
- Top 5 error patterns with solutions (covering 62%+ of failures)
- 10 production-tested patterns

### 7. **n8n Code Python**
Write Python code in n8n Code nodes with proper limitations awareness.

**Activates when**: Writing Python in Code nodes, need to know Python limitations, working with standard library.

**Key Features**:
- **Important**: Use JavaScript for 95% of use cases
- Python data access (_input, _json, _node)
- **Critical limitation**: No external libraries (requests, pandas, numpy)
- Standard library reference (json, datetime, re, etc.)
- Workarounds for missing libraries
- Common Python patterns for n8n

---

## 🚀 Installation

### Prerequisites

1. **n8n-mcp MCP server** installed and configured ([Installation Guide](https://github.com/czlonkowski/n8n-mcp))
2. **Claude Code**, Claude.ai, or Claude API access
3. `.mcp.json` configured with n8n-mcp server

### Claude Code

**Method 1: Plugin Installation** (Recommended)
```bash
# Install directly as a Claude Code plugin
/plugin install czlonkowski/n8n-skills
```

**Method 2: Via Marketplace**
```bash
# Add as marketplace, then browse and install
/plugin marketplace add czlonkowski/n8n-skills

# Then browse available plugins
/plugin install
# Select "n8n-mcp-skills" from the list
```

**Method 3: Manual Installation**
```bash
# 1. Clone this repository
git clone https://github.com/czlonkowski/n8n-skills.git

# 2. Copy skills to your Claude Code skills directory
cp -r n8n-skills/skills/* ~/.claude/skills/

# 3. Reload Claude Code
# Skills will activate automatically
```

### Claude.ai

1. Download individual skill folders from `skills/`
2. Zip each skill folder
3. Upload via Settings → Capabilities → Skills

### API / SDK

See [docs/INSTALLATION.md](docs/INSTALLATION.md) for detailed instructions.

---

## 💡 Usage

Skills activate **automatically** when relevant queries are detected:

```
"How do I write n8n expressions?"
→ Activates: n8n Expression Syntax

"Find me a Slack node"
→ Activates: n8n MCP Tools Expert

"Build a webhook workflow"
→ Activates: n8n Workflow Patterns

"Why is validation failing?"
→ Activates: n8n Validation Expert

"How do I configure the HTTP Request node?"
→ Activates: n8n Node Configuration

"How do I access webhook data in a Code node?"
→ Activates: n8n Code JavaScript

"Can I use pandas in Python Code node?"
→ Activates: n8n Code Python
```

### Skills Work Together

When you ask: **"Build and validate a webhook to Slack workflow"**

1. **n8n Workflow Patterns** identifies webhook processing pattern
2. **n8n MCP Tools Expert** searches for webhook and Slack nodes
3. **n8n Node Configuration** guides node setup
4. **n8n Code JavaScript** helps process webhook data with proper .body access
5. **n8n Expression Syntax** helps with data mapping in other nodes
6. **n8n Validation Expert** validates the final workflow

All skills compose seamlessly!

---

## 📖 Documentation

- [Installation Guide](docs/INSTALLATION.md) - Detailed installation for all platforms
- [Usage Guide](docs/USAGE.md) - How to use skills effectively
- [Development Guide](docs/DEVELOPMENT.md) - Contributing and testing
- [MCP Testing Log](docs/MCP_TESTING_LOG.md) - Real tool responses used in skills

---


## 🧪 Testing

Each skill includes 3+ evaluations for quality assurance:

```bash
# Run evaluations (if testing framework available)
npm test

# Or manually test with Claude
claude-code --skill n8n-expression-syntax "Test webhook data access"
```

---

## 🤝 Contributing

Contributions welcome! Please see [DEVELOPMENT.md](docs/DEVELOPMENT.md) for guidelines.

### Development Approach

1. **Evaluation-First**: Write test scenarios before implementation
2. **MCP-Informed**: Test tools, document real responses
3. **Iterative**: Test against evaluations, iterate until 100% pass
4. **Concise**: Keep SKILL.md under 500 lines
5. **Real Examples**: All examples from real templates/tools

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

**Conceived by Romuald Członkowski**
- Website: [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)
- Part of the [n8n-mcp project](https://github.com/czlonkowski/n8n-mcp)

---

## 🔗 Related Projects

- [n8n-mcp](https://github.com/czlonkowski/n8n-mcp) - MCP server for n8n
- [n8n](https://n8n.io/) - Workflow automation platform

---

## 📊 What's Included

- **7** complementary skills that work together
- **525+** n8n nodes supported
- **2,653+** workflow templates for examples
- **10** production-tested Code node patterns
- **Comprehensive** error catalogs and troubleshooting guides

---

**Ready to build flawless n8n workflows? Get started now!** 🚀

```

### File: build.sh
```sh
#!/bin/bash
# Build script for n8n-skills distribution packages
# Creates zip files for both Claude.ai (individual skills) and Claude Code (bundle)

set -e

DIST_DIR="dist"
VERSION="1.4.0"

echo "🔨 Building n8n-skills distribution packages..."

# Create dist directory if it doesn't exist
mkdir -p "$DIST_DIR"

# Remove old zips
echo "🗑️  Removing old zip files..."
rm -f "$DIST_DIR"/*.zip

# Build individual skill zips (for Claude.ai)
# Structure: skill-name/SKILL.md at zip root (not nested under skills/)
echo "📦 Building individual skill zips for Claude.ai..."

SKILLS=(
    "n8n-expression-syntax"
    "n8n-mcp-tools-expert"
    "n8n-workflow-patterns"
    "n8n-validation-expert"
    "n8n-node-configuration"
    "n8n-code-javascript"
    "n8n-code-python"
)

for skill in "${SKILLS[@]}"; do
    echo "   - $skill"
    (cd skills && zip -rq "../$DIST_DIR/${skill}-v${VERSION}.zip" "${skill}/" -x "*.DS_Store")
done

# Build complete bundle (for Claude Code)
echo "📦 Building complete bundle for Claude Code..."
zip -rq "$DIST_DIR/n8n-mcp-skills-v${VERSION}.zip" \
    .claude-plugin/ \
    README.md \
    LICENSE \
    skills/ \
    -x "*.DS_Store"

# Show results
echo ""
echo "✅ Build complete! Files in $DIST_DIR/:"
echo ""
ls -lh "$DIST_DIR"/*.zip
echo ""
echo "📊 Package sizes:"
du -h "$DIST_DIR"/*.zip

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **n8n-skills** repository - a collection of Claude Code skills designed to teach AI assistants how to build flawless n8n workflows using the n8n-mcp MCP server.

**Repository**: https://github.com/czlonkowski/n8n-skills

**Purpose**: 7 complementary skills that provide expert guidance on using n8n-mcp MCP tools effectively for building n8n workflows.

**Architecture**:
- **n8n-mcp MCP Server**: Provides data access (800+ nodes, validation, templates, workflow management)
- **Claude Skills**: Provides expert guidance on HOW to use MCP tools
- **Together**: Expert workflow builder with progressive disclosure

## Repository Structure

```
n8n-skills/
├── README.md              # Project overview with video
├── LICENSE                # MIT License
├── skills/                # Individual skill implementations
│   ├── n8n-expression-syntax/
│   ├── n8n-mcp-tools-expert/
│   ├── n8n-workflow-patterns/
│   ├── n8n-validation-expert/
│   ├── n8n-node-configuration/
│   ├── n8n-code-javascript/
│   └── n8n-code-python/
├── evaluations/           # Test scenarios for each skill
├── docs/                  # Documentation
├── dist/                  # Distribution packages
└── .claude-plugin/        # Claude Code plugin configuration
```

## The 7 Skills

### 1. n8n Expression Syntax
- Teaches correct n8n expression syntax ({{}} patterns)
- Covers common mistakes and fixes
- Critical gotcha: Webhook data under `$json.body`

### 2. n8n MCP Tools Expert (HIGHEST PRIORITY)
- Teaches how to use n8n-mcp MCP tools effectively
- Covers unified tools: `get_node`, `validate_node`, `search_nodes`
- Workflow management with `n8n_update_partial_workflow`
- New: `n8n_deploy_template`, `n8n_workflow_versions`, `activateWorkflow`

### 3. n8n Workflow Patterns
- Teaches proven workflow architectural patterns
- 5 patterns: webhook, HTTP API, database, AI, scheduled

### 4. n8n Validation Expert
- Interprets validation errors and guides fixing
- Handles false positives and validation loops
- Auto-fix with `n8n_autofix_workflow`

### 5. n8n Node Configuration
- Operation-aware node configuration guidance
- Property dependencies and common patterns

### 6. n8n Code JavaScript
- Write JavaScript in n8n Code nodes
- Data access patterns, `$helpers`, DateTime

### 7. n8n Code Python
- Write Python in n8n Code nodes
- Limitations awareness (no external libraries)

## Key MCP Tools

The n8n-mcp server provides these unified tools:

### Node Discovery
- `search_nodes` - Find nodes by keyword
- `get_node` - Unified node info with detail levels (minimal, standard, full) and modes (info, docs, search_properties, versions)

### Validation
- `validate_node` - Unified validation with modes (minimal, full) and profiles (runtime, ai-friendly, strict)
- `validate_workflow` - Complete workflow validation

### Workflow Management
- `n8n_create_workflow` - Create new workflows
- `n8n_update_partial_workflow` - Incremental updates (19 operation types including `patchNodeField`, `activateWorkflow`, `transferWorkflow`)
- `n8n_validate_workflow` - Validate by ID
- `n8n_autofix_workflow` - Auto-fix common issues
- `n8n_deploy_template` - Deploy template to n8n instance
- `n8n_workflow_versions` - Version history and rollback
- `n8n_test_workflow` - Test execution
- `n8n_executions` - Manage executions

### Data Tables
- `n8n_manage_datatable` - Manage data tables and rows (CRUD, filtering, dry-run)

### Credential Management
- `n8n_manage_credentials` - Full credential CRUD (list, get, create, update, delete) + schema discovery (`getSchema`)

### Security & Audit
- `n8n_audit_instance` - Security audit combining n8n built-in audit (5 risk categories) + custom deep scan (hardcoded secrets, unauthenticated webhooks, error handling, data retention)

### Templates
- `search_templates` - Multiple modes (keyword, by_nodes, by_task, by_metadata)
- `get_template` - Get template details

### Other Workflow Tools
- `n8n_list_workflows` - List workflows with filtering/pagination
- `n8n_get_workflow` - Get workflow details (full, structure, minimal modes)
- `n8n_delete_workflow` - Permanently delete workflows
- `n8n_update_full_workflow` - Full workflow replacement

### Guides
- `tools_documentation` - Meta-documentation for all tools
- `ai_agents_guide` - AI agent workflow guidance

## Important Patterns

### Most Common Tool Usage Pattern
```
search_nodes → get_node (18s avg between steps)
```

### Most Common Validation Pattern
```
n8n_update_partial_workflow → n8n_validate_workflow (7,841 occurrences)
Avg 23s thinking, 58s fixing
```

### Most Used Tool
```
n8n_update_partial_workflow (38,287 uses, 99.0% success)
Avg 56 seconds between edits
```

## Working with This Repository

### When Adding New Skills
1. Create skill directory under `skills/`
2. Write SKILL.md with frontmatter
3. Add reference files as needed
4. Create 3+ evaluations in `evaluations/`
5. Test thoroughly before committing

### Skill Activation
Skills activate automatically when queries match their description triggers:
- "How do I write n8n expressions?" → n8n Expression Syntax
- "Find me a Slack node" → n8n MCP Tools Expert
- "Build a webhook workflow" → n8n Workflow Patterns

### Cross-Skill Integration
Skills are designed to work together:
- Use n8n Workflow Patterns to identify structure
- Use n8n MCP Tools Expert to find nodes
- Use n8n Node Configuration for setup
- Use n8n Expression Syntax for data mapping
- Use n8n Code JavaScript/Python for custom logic
- Use n8n Validation Expert to validate

## Requirements

- n8n-mcp MCP server installed and configured
- Claude Code, Claude.ai, or Claude API access
- Understanding of n8n workflow concepts

## Distribution

Available as:
1. **GitHub Repository**: Full source code and documentation
2. **Claude Code Plugin**: `npm install @anthropic/claude-code-plugin-n8n-skills`
3. **Individual Skill Uploads**: For Claude.ai users

## Credits

Conceived by Romuald Członkowski - [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)

Part of the n8n-mcp project.

## License

MIT License - See LICENSE file for details.

```

### File: .claude-plugin\marketplace.json
```json
{
  "name": "n8n-mcp-skills",
  "description": "Expert skills for building n8n workflows",
  "owner": {
    "name": "Romuald Członkowski",
    "url": "https://www.aiadvisors.pl/en"
  },
  "plugins": [
    {
      "name": "n8n-mcp-skills",
      "source": "./",
      "description": "Complete bundle: 7 expert skills for building flawless n8n workflows using n8n-mcp MCP server. Includes skills for expression syntax, MCP tools usage, workflow patterns, validation, node configuration, JavaScript code, and Python code.",
      "version": "1.4.0",
      "author": {
        "name": "Romuald Członkowski",
        "url": "https://www.aiadvisors.pl/en"
      },
      "category": "automation",
      "keywords": [
        "n8n",
        "workflow",
        "mcp",
        "automation",
        "validation",
        "expressions",
        "code",
        "javascript",
        "python",
        "skills"
      ],
      "homepage": "https://github.com/czlonkowski/n8n-skills",
      "repository": "https://github.com/czlonkowski/n8n-skills",
      "license": "MIT"
    }
  ]
}

```

### File: .claude-plugin\plugin.json
```json
{
  "name": "n8n-mcp-skills",
  "version": "1.4.0",
  "description": "Expert skills for building n8n workflows with n8n-mcp",
  "author": {
    "name": "Romuald Członkowski",
    "url": "https://www.aiadvisors.pl/en"
  },
  "license": "MIT",
  "keywords": [
    "n8n",
    "workflow",
    "automation",
    "mcp",
    "validation",
    "expressions",
    "code",
    "javascript",
    "python"
  ],
  "repository": "https://github.com/czlonkowski/n8n-skills",
  "homepage": "https://github.com/czlonkowski/n8n-skills"
}

```

### File: docs\CODE_NODE_BEST_PRACTICES.md
```md
# n8n CODE Node - Best Practices & Pattern Analysis

**Analysis Period:** Last 60 days | **Data Quality:** 38,094 CODE node instances analyzed

---

## Executive Summary

- **47.16% of workflows use CODE nodes** (15,202 workflows from 4,461 unique users)
- **Top 3 data access patterns:** `$input.all()` (26% usage), `$input.first()` (25%), `$input.item` (19%)
- **Critical finding:** 39% validation failures are due to empty code or missing return values
- **Best return pattern:** `return [{json: {...}}]` (39% of successful nodes)

---

## 1. Node Configuration Essentials

### Choosing the Right Mode

The Code node offers two execution modes that determine how your code processes input data:

#### **Run Once for All Items** (Default - Recommended for most use cases)
- Code executes **once** regardless of input count
- Access all items via `$input.all()` or `items` array
- **Best for:** Aggregation, filtering, batch processing, transformations
- **Performance:** Faster for multiple items (single execution)
- **Usage:** 78% of successful workflows use this mode

```javascript
// Example: Process all items together
const allItems = $input.all();
const total = allItems.reduce((sum, item) => sum + item.json.amount, 0);
return [{json: {total, count: allItems.length}}];
```

#### **Run Once for Each Item**
- Code executes **separately** for each input item
- Access current item via `$input.item` or `$item`
- **Best for:** Item-specific logic, independent operations, item validation
- **Performance:** Slower for large datasets (multiple executions)
- **Usage:** 22% of workflows (specialized cases)

```javascript
// Example: Process each item independently
const item = $input.item;
return [{
  json: {
    ...item.json,
    processed: true,
    processedAt: new Date().toISOString()
  }
}];
```

**Decision Guide:**
- ✅ Use "All Items" when: Comparing items, calculating totals, sorting, deduplication
- ✅ Use "Each Item" when: Item-specific API calls, individual validations, per-item errors

---

### Language Selection

| Language | Use Case | Performance | Built-ins | Beta Status |
|----------|----------|-------------|-----------|-------------|
| **JavaScript** | General purpose, web APIs, JSON | Fast | Full n8n helpers | Stable |
| **Python (Beta)** | Data science, ML, complex math | Slower | `_` syntax helpers | Beta |
| **Python (Native)** | Standard Python, no helpers | Medium | `_items`, `_item` only | Beta |

**Recommendation:** Use JavaScript for 95% of use cases. Only use Python when you need specific libraries or data science capabilities.

---

## 2. Top 10 Successful CODE Node Patterns

### Pattern 1: Multi-source Data Aggregation
```javascript
// Process and structure collected data from multiple sources
const allItems = $input.all();
let processedArticles = [];

// Handle different source formats
for (const item of allItems) {
  const sourceName = item.json.name || 'Unknown';
  const sourceData = item.json;

  // Parse source-specific structure
  if (sourceName === 'Hacker News' && sourceData.hits) {
    for (const hit of sourceData.hits) {
      processedArticles.push({
        title: hit.title,
        url: hit.url,
        summary: hit.story_text || 'No summary',
        source: 'Hacker News',
        score: hit.points || 0
      });
    }
  }
}

return processedArticles.map(article => ({ json: article }));
```
**Use Case:** Aggregating data from APIs, RSS feeds, webhooks
**Key Techniques:** Loop iteration, conditional parsing, data normalization

---

### Pattern 2: Regex Filtering & Pattern Matching
```javascript
// Extract and filter mentions using regex patterns
const etfPattern = /\b([A-Z]{2,5})\b/g;
const knownETFs = ['VOO', 'VTI', 'VT', 'SCHD', 'QYLD', 'VXUS'];

const etfMentions = {};

for (const item of $input.all()) {
  const data = item.json.data;
  if (!data?.children) continue;

  for (const post of data.children) {
    const combinedText = (post.data.title + ' ' + post.data.selftext).toUpperCase();
    const matches = combinedText.match(etfPattern);

    if (matches) {
      for (const match of matches) {
        if (knownETFs.includes(match)) {
          if (!etfMentions[match]) {
            etfMentions[match] = { count: 0, totalScore: 0, posts: [] };
          }
          etfMentions[match].count++;
        }
      }
    }
  }
}

return Object.entries(etfMentions)
  .map(([etf, data]) => ({ json: { etf, ...data } }))
  .sort((a, b) => b.json.count - a.json.count);
```
**Use Case:** Content analysis, keyword extraction, mention tracking
**Key Techniques:** Regex matching, object aggregation, sorting/ranking

---

### Pattern 3: Markdown Parsing & Structured Data Extraction
```javascript
// Parse markdown and extract structured information
const markdown = $input.first().json.data.markdown;
const adRegex = /##\s*(.*?)\n(.*?)(?=\n##|\n---|$)/gs;

const ads = [];
let match;

function parseTimeToMinutes(timeStr) {
  if (!timeStr) return 999999;

  const hourMatch = timeStr.match(/(\d+)\s*hour/);
  const dayMatch = timeStr.match(/(\d+)\s*day/);

  let totalMinutes = 0;
  if (hourMatch) totalMinutes += parseInt(hourMatch[1]) * 60;
  if (dayMatch) totalMinutes += parseInt(dayMatch[1]) * 1440;

  return totalMinutes;
}

while ((match = adRegex.exec(markdown)) !== null) {
  const title = match[1]?.trim() || 'No title';
  const content = match[2]?.trim() || '';

  const districtMatch = content.match(/\*\*District:\*\*\s*(.*?)(?:\n|$)/);
  const timeMatch = content.match(/Posted:\s*(.*?)\*/);

  ads.push({
    title: title,
    district: districtMatch?.[1].trim() || 'Unknown',
    timeInMinutes: parseTimeToMinutes(timeMatch?.[1]),
    fullContent: content
  });
}

return ads.map(ad => ({ json: ad }));
```
**Use Case:** Parsing formatted text, extracting structured fields
**Key Techniques:** Regex grouping, helper functions, data normalization

---

### Pattern 4: JSON Comparison & Validation
```javascript
// Compare and validate JSON objects from different sources
const orderJsonKeys = (jsonObj) => {
  const ordered = {};
  Object.keys(jsonObj).sort().forEach(key => {
    ordered[key] = jsonObj[key];
  });
  return ordered;
};

const origWorkflow = JSON.parse(
  Buffer.from($input.all()[0].json.content, 'base64').toString()
);
const n8nWorkflow = $input.all()[1].json;

const orderedOriginal = orderJsonKeys(origWorkflow);
const orderedActual = orderJsonKeys(n8nWorkflow);

const isSame = JSON.stringify(orderedOriginal) === JSON.stringify(orderedActual);

$input.all()[0].json.status = isSame ? 'same' : 'different';
$input.all()[0].json.original_data = orderedOriginal;

return $input.all();
```
**Use Case:** Workflow versioning, configuration validation, change detection
**Key Techniques:** JSON ordering, base64 decoding, deep comparison

---

### Pattern 5: CRM Data Transformation
```javascript
// Transform form data into CRM-compatible format
const item = $input.all()[0];
const { name, email, phone, company, course_interest, message, timestamp } = item.json;

const nameParts = name.split(' ');
const firstName = nameParts[0] || '';
const lastName = nameParts.slice(1).join(' ') || 'Unknown';

const crmData = {
  data: {
    type: 'Contact',
    attributes: {
      first_name: firstName,
      last_name: lastName,
      email1: email,
      phone_work: phone,
      account_name: company,
      description: `Course: ${course_interest}\nMessage: ${message}\nTimestamp: ${timestamp}`
    }
  }
};

return [{
  json: {
    ...item.json,
    crmData,
    processed: true
  }
}];
```
**Use Case:** Lead enrichment, data normalization, API preparation
**Key Techniques:** Object destructuring, data mapping, format conversion

---

### Pattern 6: Release Information Processing
```javascript
// Extract and filter stable releases from GitHub API
const allReleases = $input.first().json;
const stableReleases = allReleases
  .filter(release => !release.prerelease && !release.draft)
  .slice(0, 10)
  .map(release => ({
    tag: release.tag_name,
    name: release.name,
    published: release.published_at,
    publishedDate: new Date(release.published_at).toLocaleDateString(),
    author: release.author.login,
    url: release.html_url,
    changelog: release.body || '(No changelog)',
    highlights: release.body?.split('## Highlights:')[1]?.split('##')[0]?.trim()
      || release.body?.substring(0, 500) + '...'
      || 'No highlights available',
    assetCount: release.assets.length
  }));

return stableReleases.map(release => ({ json: release }));
```
**Use Case:** Version management, changelog parsing, release notes generation
**Key Techniques:** Array filtering, conditional field extraction, date formatting

---

### Pattern 7: Array Transformation with Context
```javascript
// Transform and map data with additional context
const stableReleases = $input.first().json
  .filter(release => !release.prerelease && !release.draft)
  .slice(0, 10)
  .map(release => ({
    version: release.tag_name,
    assetCount: release.assets.length,
    assetsCountText: release.assets.length === 1 ? 'file' : 'files'
  }));

return stableReleases.map(release => ({ json: release }));
```
**Use Case:** Quick data transformation, simple field mapping
**Key Techniques:** Array methods chaining, pluralization logic

---

### Pattern 8: Slack Block Kit Formatting
```javascript
// Create Slack-formatted message with structured blocks
const date = new Date().toISOString().split('T')[0];

return [{
  json: {
    text: `Daily Report - ${date}`,
    blocks: [
      {
        type: "header",
        text: {
          type: "plain_text",
          text: `📊 Daily Security Report - ${date}`
        }
      },
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: `*Status:* ✅ All Clear\n*Alerts:* 0\n*Updated:* ${new Date().toLocaleString()}`
        }
      },
      {
        type: "context",
        elements: [{
          type: "mrkdwn",
          text: `Report generated automatically`
        }]
      }
    ]
  }
}];
```
**Use Case:** Chat notifications, rich message formatting
**Key Techniques:** Template literals, nested objects, Block Kit syntax

---

### Pattern 9: Top N Filtering
```javascript
// Filter and rank by score, return top N results
const ragResponse = $input.item.json;
const chunks = ragResponse.chunks || [];

const topChunks = chunks
  .sort((a, b) => (b.similarity || 0) - (a.similarity || 0))
  .slice(0, 6);

return [{
  json: {
    topChunks: topChunks,
    count: topChunks.length
  }
}];
```
**Use Case:** RAG pipelines, ranking algorithms, result filtering
**Key Techniques:** Sorting, slicing, null coalescing

---

### Pattern 10: String Aggregation & Reporting
```javascript
// Aggregate multiple text inputs into formatted report
const ragResponse = $input.item.json;
const markdown = ragResponse.data.markdown;

const finalReport = $input.all()
  .map(item => item.json.message)
  .join('\n\n---\n\n');

const header = `🎯 **Report**\n📅 ${new Date().toLocaleString()}\n\n`;

return [{
  json: {
    report: header + finalReport,
    timestamp: new Date().toISOString()
  }
}];
```
**Use Case:** Report generation, log aggregation, content concatenation
**Key Techniques:** Array joining, string concatenation, timestamp handling

---

## 2. Python Code Examples & Best Practices

### Python vs JavaScript: Key Differences

| Feature | JavaScript | Python (Beta) | Python (Native) |
|---------|-----------|---------------|-----------------|
| Input access | `$input.all()` | `_input.all()` | `_items` |
| Single item | `$input.first()` | `_input.first()` | `_items[0]` |
| Current item | `$input.item` | `_input.item` | `_item` |
| Return format | `[{json: {...}}]` | `[{json: {...}}]` | `[{"json": {...}}]` |
| Date helper | `$now` | `_now` | Standard datetime |
| JSON query | `$jmespath()` | `_jmespath()` | Not available |

### Python Pattern 1: Data Transformation (Run Once for All Items)

```python
# Python (Beta) - Using n8n helpers
items = _input.all()
processed = []

for item in items:
    data = item["json"]
    processed.append({
        "json": {
            "id": data.get("id"),
            "name": data.get("name", "Unknown"),
            "processed": True,
            "timestamp": _now.isoformat()
        }
    })

return processed
```

```python
# Python (Native) - Standard Python
processed = []

for item in _items:
    data = item["json"]
    processed.append({
        "json": {
            "id": data.get("id"),
            "name": data.get("name", "Unknown"),
            "processed": True,
            "timestamp": str(_now)  # _now is datetime object
        }
    })

return processed
```

### Python Pattern 2: Filtering & Aggregation

```python
# Filter and sum amounts
items = _input.all()
total = 0
valid_items = []

for item in items:
    amount = item["json"].get("amount", 0)
    if amount > 0:
        total += amount
        valid_items.append(item["json"])

return [{
    "json": {
        "total": total,
        "count": len(valid_items),
        "items": valid_items
    }
}]
```

### Python Pattern 3: String Processing with Regex

```python
import re

# Extract emails from text
items = _input.all()
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

all_emails = []
for item in items:
    text = item["json"].get("text", "")
    emails = re.findall(email_pattern, text)
    all_emails.extend(emails)

# Remove duplicates
unique_emails = list(set(all_emails))

return [{
    "json": {
        "emails": unique_emails,
        "count": len(unique_emails)
    }
}]
```

### Python Pattern 4: Data Science Operations

```python
# Calculate statistics (Python Native with standard library)
from statistics import mean, median, stdev

items = _items
values = [item["json"].get("value", 0) for item in items if "value" in item["json"]]

if len(values) > 0:
    return [{
        "json": {
            "mean": mean(values),
            "median": median(values),
            "std_dev": stdev(values) if len(values) > 1 else 0,
            "min": min(values),
            "max": max(values),
            "count": len(values)
        }
    }]
else:
    return [{"json": {"error": "No values found"}}]
```

### Python Pattern 5: Dictionary/Object Manipulation

```python
# Merge and deduplicate objects by key
items = _input.all()
merged = {}

for item in items:
    data = item["json"]
    key = data.get("id")

    if key:
        if key not in merged:
            merged[key] = data
        else:
            # Merge properties, preferring newer values
            merged[key].update({k: v for k, v in data.items() if v})

# Convert back to array format
result = [{"json": value} for value in merged.values()]
return result
```

### Python Best Practices

1. **Always use `.get()` for dictionary access** to avoid KeyError
   ```python
   # ✅ Safe
   value = item["json"].get("field", "default")

   # ❌ Risky
   value = item["json"]["field"]  # Crashes if field missing
   ```

2. **Handle None/null values explicitly**
   ```
... [TRUNCATED]
```

### File: docs\DEVELOPMENT.md
```md
# Development Guide

Guidelines for contributing to n8n-skills and developing new skills.

---

## Development Philosophy

### 1. Evaluation-Driven Development (EDD)

Write tests **before** writing skills!

**Process**:
```
1. Create 3+ evaluation scenarios
2. Test baseline (without skill)
3. Write minimal SKILL.md
4. Test against evaluations
5. Iterate until 100% pass
6. Add reference files as needed
```

**Why**: Ensures skills solve real problems and can be tested objectively.

### 2. MCP-Informed Content

All content based on **real MCP tool responses**, not assumptions.

**Process**:
```
1. Test MCP tools thoroughly
2. Document actual responses
3. Use real examples in skills
4. Verify all code snippets work
```

**See**: [MCP_TESTING_LOG.md](MCP_TESTING_LOG.md) for reference data.

### 3. Keep Skills Concise

**Guideline**: SKILL.md should be under 500 lines

**Why**: Longer skills are harder to maintain and slower to load.

**Solution**: Split complex content into reference files:
- SKILL.md: Core concepts and quick reference
- REFERENCE_*.md: Detailed information
- EXAMPLES.md: Working examples

### 4. Real Examples Only

**Never** invent examples. Always use:
- Real templates from n8n-mcp
- Actual MCP tool responses
- Verified node configurations

---

## Repository Structure

```
n8n-skills/
├── skills/                    # Skill implementations
│   ├── n8n-expression-syntax/
│   │   ├── SKILL.md          # Main skill content (< 500 lines)
│   │   ├── COMMON_MISTAKES.md
│   │   ├── EXAMPLES.md
│   │   └── README.md         # Skill metadata
│   └── ...
├── evaluations/               # Test scenarios
│   ├── expression-syntax/
│   │   ├── eval-001-*.json
│   │   └── ...
│   └── ...
├── docs/                      # Documentation
│   ├── INSTALLATION.md
│   ├── USAGE.md
│   ├── DEVELOPMENT.md (this file)
│   └── MCP_TESTING_LOG.md    # Real MCP responses
├── README.md                  # Project overview
├── LICENSE                    # MIT License
└── .gitignore
```

---

## Creating a New Skill

### Step 1: Define Scope

**Questions to answer**:
- What problem does this skill solve?
- When should it activate?
- What MCP tools will it teach?
- What are 3 key examples?

**Document in**: `skills/[skill-name]/README.md`

### Step 2: Create Evaluations

**Create**: `evaluations/[skill-name]/eval-001-description.json`

**Format**:
```json
{
  "id": "skill-001",
  "skills": ["skill-name"],
  "query": "User question or scenario",
  "expected_behavior": [
    "Skill should identify X",
    "Skill should provide Y guidance",
    "Skill should reference Z content"
  ],
  "baseline_without_skill": {
    "likely_response": "Generic answer",
    "expected_quality": "Low"
  },
  "with_skill_expected": {
    "response_quality": "High",
    "uses_skill_content": true,
    "provides_correct_guidance": true
  }
}
```

**Create at least 3 evaluations** covering:
1. Basic usage
2. Common mistake
3. Advanced scenario

### Step 3: Test MCP Tools

**Document tool responses** in `docs/MCP_TESTING_LOG.md`:

```markdown
## [Your Skill Name] - MCP Testing

### Tool: tool_name

**Test**:
```javascript
tool_name({param: "value"})
```

**Response**:
```json
{actual response}
```

**Key Insights**:
- Finding 1
- Finding 2
```

### Step 4: Write SKILL.md

**Required frontmatter**:
```markdown
---
name: Skill Name
description: When to use this skill. Use when [trigger conditions].
---
```

**Recommended structure**:
```markdown
# Skill Name

## Quick Reference
[Table or list of most common patterns]

## Core Concepts
[Essential knowledge]

## Common Patterns
[Real examples with code]

## Common Mistakes
[Errors and fixes]

## Advanced Topics
[Link to reference files]

## Related Skills
[Cross-references]
```

**Guidelines**:
- Under 500 lines for SKILL.md
- Use real examples from MCP testing
- Include quick fixes table
- Link to reference files
- Cross-reference other skills

### Step 5: Add Reference Files

Create as needed:
- `COMMON_MISTAKES.md` - Error catalog
- `EXAMPLES.md` - Working examples
- `PATTERNS.md` - Common patterns
- `ADVANCED.md` - Deep dive topics

**Each file**:
- Should be focused on one topic
- Under 200 lines
- Real examples only
- Cross-linked from SKILL.md

### Step 6: Test Against Evaluations

**Process**:
1. Run evaluation scenarios with Claude
2. Check if expected behaviors occur
3. Document results
4. Iterate SKILL.md if needed
5. Repeat until 100% pass

**Success criteria**:
- All evaluations pass
- Skill activates correctly
- Content is accurate
- Examples work

### Step 7: Document Metadata

**Create**: `skills/[skill-name]/README.md`

```markdown
# Skill Name

**Purpose**: One-sentence description

**Activates on**: keyword1, keyword2, keyword3

**File Count**: X files, ~Y lines

**Dependencies**:
- n8n-mcp tools: tool1, tool2
- Other skills: skill1, skill2

**Coverage**:
- Topic 1
- Topic 2
- Topic 3

**Evaluations**: X scenarios (X% pass rate)

**Last Updated**: YYYY-MM-DD
```

---

## Evaluation Guidelines

### Good Evaluations

**Characteristics**:
- Specific, measurable expected behavior
- Based on real user queries
- Cover common and edge cases
- Include baseline comparison

**Example**:
```json
{
  "id": "expr-001",
  "query": "Why is {{$json.email}} undefined in my webhook workflow?",
  "expected_behavior": [
    "Identifies webhook data structure issue",
    "Explains data is under $json.body",
    "Provides corrected expression: {{$json.body.email}}",
    "References webhook structure documentation"
  ]
}
```

### Bad Evaluations

**Avoid**:
- Vague expected behaviors
- Unrealistic scenarios
- No baseline comparison
- Too simple or too complex

---

## Testing

### Manual Testing

```
1. Start Claude Code
2. Load skill
3. Ask evaluation query
4. Verify expected behaviors
5. Document results
```

### Automated Testing

*Coming soon: Evaluation framework*

---

## MCP Tool Testing Guidelines

### Before Writing Skills

**Test these tools**:
```javascript
// Node discovery
search_nodes({query: "keyword"})
search_nodes({category: "trigger"})
get_node({nodeType: "nodes-base.webhook"})

// Validation
validate_node({mode: "minimal"})({nodeType: "nodes-base.slack", config: {}})
validate_node({nodeType: "nodes-base.slack", config: {...}, profile: "runtime"})

// Templates
search_templates({query: "webhook"})
get_template({templateId: 2947, mode: "structure"})

// Workflow management (if API available)
n8n_create_workflow({...})
n8n_update_partial_workflow({...})
n8n_validate_workflow({...})
```

### Document Findings

**In MCP_TESTING_LOG.md**:
- Actual responses
- Performance (timing)
- Gotchas discovered
- Format differences
- Error messages

### Use Real Data

**Extract from tools**:
- Node structures
- Template examples
- Validation errors
- Property dependencies

**Use in skills**:
- Real node configurations
- Actual error messages
- Working template IDs
- Proven patterns

---

## Code Standards

### Markdown

**Formatting**:
```markdown
# H1 - Skill Title
## H2 - Major Sections
### H3 - Subsections

**Bold** for emphasis
`code` for inline code
\`\`\`language for code blocks
```

**Code blocks**:
```javascript
// Always specify language
// Include comments
// Use real, working examples
```

### JSON (Evaluations)

**Format**:
```json
{
  "id": "kebab-case-id",
  "skills": ["exact-skill-name"],
  "query": "Natural user question",
  "expected_behavior": [
    "Specific measurable behavior"
  ]
}
```

---

## Git Workflow

### Branching

```bash
# Feature branch
git checkout -b skill/skill-name

# Bug fix
git checkout -b fix/issue-description
```

### Commits

**Format**:
```
type(scope): brief description

Longer description if needed.

Refs: #issue-number
```

**Types**:
- `feat`: New skill or feature
- `fix`: Bug fix
- `docs`: Documentation
- `test`: Evaluations
- `refactor`: Code improvement

**Examples**:
```
feat(expression-syntax): add webhook data structure guide
fix(mcp-tools): correct nodeType format examples
docs(usage): add cross-skill composition examples
test(validation): add auto-sanitization evaluation
```

### Pull Requests

**Include**:
- Description of changes
- Evaluation results (if new skill)
- MCP testing performed
- Documentation updated

**Template**:
```markdown
## Description
[What changed and why]

## Evaluations
- [ ] eval-001: PASS
- [ ] eval-002: PASS
- [ ] eval-003: PASS

## MCP Testing
- Tested tools: [list]
- New findings: [list]

## Documentation
- [ ] SKILL.md updated
- [ ] README.md updated
- [ ] MCP_TESTING_LOG.md updated

## Checklist
- [ ] SKILL.md under 500 lines
- [ ] Real examples only
- [ ] All evaluations pass
- [ ] Cross-references added
```

---

## File Naming Conventions

### Skills

```
skills/skill-name/
  SKILL.md              # Main content
  COMMON_MISTAKES.md    # Error catalog
  EXAMPLES.md           # Working examples
  README.md             # Metadata
  [optional files].md   # Additional references
```

### Evaluations

```
evaluations/skill-name/
  eval-001-short-description.json
  eval-002-short-description.json
  eval-003-short-description.json
```

**Naming**: `eval-NNN-kebab-case-description.json`

---

## Documentation Standards

### SKILL.md Frontmatter

**Required**:
```yaml
---
name: Exact Skill Name
description: When this skill activates. Use when [triggers]. Include specific keywords.
---
```

### Cross-References

**Link to**:
- Related skills
- Reference files
- MCP tool documentation
- Real templates

**Format**:
```markdown
See [n8n MCP Tools Expert](../n8n-mcp-tools-expert/SKILL.md)
See [COMMON_MISTAKES.md](COMMON_MISTAKES.md)
See template #2947 for example
```

---

## Quality Checklist

Before submitting a skill:

### Content Quality
- [ ] All examples tested with real MCP tools
- [ ] No invented/fake examples
- [ ] SKILL.md under 500 lines
- [ ] Clear, actionable guidance
- [ ] Real error messages included

### Testing
- [ ] 3+ evaluations created
- [ ] All evaluations pass
- [ ] Baseline comparison documented
- [ ] Cross-skill integration tested

### Documentation
- [ ] Frontmatter correct
- [ ] README.md metadata complete
- [ ] MCP_TESTING_LOG.md updated
- [ ] Cross-references added
- [ ] Examples documented

### Code Standards
- [ ] Markdown properly formatted
- [ ] Code blocks have language specified
- [ ] Consistent naming conventions
- [ ] Proper git commits

---

## Common Pitfalls

### ❌ Don't

- Invent examples or data
- Exceed 500 lines in SKILL.md
- Skip MCP tool testing
- Write skills without evaluations
- Use generic error messages
- Assume tool behavior

### ✅ Do

- Test tools and document responses
- Use real templates and configurations
- Write evaluations first
- Keep skills concise
- Cross-reference related skills
- Verify all code works

---

## Release Process

### Version Numbering

**Format**: `MAJOR.MINOR.PATCH`

- **MAJOR**: New skills added
- **MINOR**: Skill improvements
- **PATCH**: Bug fixes, typos

### Changelog

Update `CHANGELOG.md`:
```markdown
## [1.1.0] - 2025-10-20

### Added
- New skill: n8n Expression Syntax
- 3 evaluations for expression syntax

### Changed
- Improved MCP Tools Expert validation guidance

### Fixed
- Corrected nodeType format in examples
```

---

## Support

### Getting Help

- **Issues**: https://github.com/czlonkowski/n8n-skills/issues
- **Discussions**: https://github.com/czlonkowski/n8n-skills/discussions
- **n8n-mcp**: https://github.com/romualdczlonkowski/n8n-mcp

### Reporting Bugs

**Include**:
- Skill name and version
- Evaluation that fails
- Expected vs actual behavior
- MCP tool versions

---

## License

All contributions must be compatible with MIT License.

---

**Happy developing!** 🚀

---

Conceived by Romuald Członkowski - [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)

```

### File: docs\INSTALLATION.md
```md
# Installation Guide

Complete installation instructions for n8n-skills across all platforms.

---

## Prerequisites

### 1. n8n-mcp MCP Server

You **must** have the n8n-mcp MCP server installed and configured before using these skills.

**Install n8n-mcp**:
```bash
npm install -g n8n-mcp
```

**Configure MCP server** in `.mcp.json`:
```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "npx",
      "args": ["n8n-mcp"],
      "env": {
        "MCP_MODE": "stdio",
        "LOG_LEVEL": "error",
        "DISABLE_CONSOLE_OUTPUT": "true",
        "N8N_API_URL": "https://your-n8n-instance.com",
        "N8N_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

**Note**: `N8N_API_URL` and `N8N_API_KEY` are optional but enable workflow creation/management tools.

### 2. Claude Access

You need one of:
- **Claude Code** (desktop application)
- **Claude.ai** (web interface)
- **Claude API** (via SDK)

---

## Installation Methods

### Method 1: Claude Code (Recommended)

**Step 1**: Clone the repository
```bash
git clone https://github.com/czlonkowski/n8n-skills.git
cd n8n-skills
```

**Step 2**: Copy skills to Claude Code skills directory

**macOS/Linux**:
```bash
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

**Windows**:
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills"
Copy-Item -Recurse skills\* "$env:USERPROFILE\.claude\skills\"
```

**Step 3**: Verify installation
```bash
ls ~/.claude/skills/
# Should show: n8n-expression-syntax, n8n-mcp-tools-expert, etc.
```

**Step 4**: Reload Claude Code
- Restart Claude Code application
- Skills will activate automatically

---

### Method 2: Claude.ai (Web Interface)

**Step 1**: Download skill folders

Download the repository and navigate to `skills/` directory. You'll need to upload each skill individually.

**Step 2**: Zip each skill
```bash
cd skills
zip -r n8n-expression-syntax.zip n8n-expression-syntax/
zip -r n8n-mcp-tools-expert.zip n8n-mcp-tools-expert/
zip -r n8n-workflow-patterns.zip n8n-workflow-patterns/
zip -r n8n-validation-expert.zip n8n-validation-expert/
zip -r n8n-node-configuration.zip n8n-node-configuration/
```

**Step 3**: Upload to Claude.ai

1. Go to Claude.ai
2. Navigate to **Settings** → **Capabilities** → **Skills**
3. Click **Upload Skill**
4. Upload each `.zip` file individually
5. Confirm each upload

**Step 4**: Verify skills are active

In a new conversation, type:
```
"List my active skills"
```

You should see all 5 n8n skills listed.

---

### Method 3: Claude API / SDK

**Step 1**: Install via package manager

If you're building an application with Claude SDK:

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

// Load skills from directory
const skillsDir = './skills';
const skills = loadSkillsFromDirectory(skillsDir);

const response = await client.messages.create({
  model: 'claude-sonnet-4-5-20250929',
  messages: [{
    role: 'user',
    content: 'Build a webhook to Slack workflow'
  }],
  skills: skills // Pass loaded skills
});
```

**Step 2**: Skill loading function

```typescript
import fs from 'fs';
import path from 'path';

function loadSkillsFromDirectory(dir: string) {
  const skillDirs = fs.readdirSync(dir);
  return skillDirs.map(skillName => {
    const skillPath = path.join(dir, skillName, 'SKILL.md');
    const skillContent = fs.readFileSync(skillPath, 'utf-8');

    return {
      name: skillName,
      content: skillContent
    };
  });
}
```

---

## Verification

### Test Installation

**1. Check MCP server availability**
```
Ask Claude: "Can you search for the webhook node using n8n-mcp?"
```

Expected response:
```
[Uses search_nodes tool]
Found: nodes-base.webhook (Webhook trigger node)
```

**2. Test skill activation**
```
Ask Claude: "How do I access webhook data in n8n expressions?"
```

Expected response:
```
[n8n Expression Syntax skill activates]
Webhook data is under $json.body...
```

**3. Test cross-skill composition**
```
Ask Claude: "Build and validate a webhook to Slack workflow"
```

Expected: All 5 skills should activate and work together.

---

## Troubleshooting

### Skills Not Activating

**Problem**: Skills don't activate when expected

**Solutions**:
1. Verify skills are in correct directory:
   - Claude Code: `~/.claude/skills/`
   - Check each skill has `SKILL.md` with frontmatter

2. Check SKILL.md frontmatter format:
   ```markdown
   ---
   name: n8n Expression Syntax
   description: Validate n8n expression syntax...
   ---
   ```

3. Reload Claude Code or clear cache

### MCP Tools Not Available

**Problem**: "n8n-mcp tools not available"

**Solutions**:
1. Verify `.mcp.json` is in correct location
2. Check n8n-mcp is installed: `npm list -g n8n-mcp`
3. Test MCP server: `npx n8n-mcp`
4. Restart Claude Code

### N8N API Tools Missing

**Problem**: "n8n_create_workflow not available"

**Solutions**:
1. Verify `N8N_API_URL` and `N8N_API_KEY` in `.mcp.json`
2. Test API access: `curl -H "X-N8N-API-KEY: your-key" https://your-n8n-instance/api/v1/workflows`
3. Skills will still work with read-only tools (search, validate, templates)

### Permission Issues

**Problem**: Cannot write to skills directory

**macOS/Linux**:
```bash
sudo chown -R $USER ~/.claude
chmod -R 755 ~/.claude/skills
```

**Windows**: Run PowerShell as Administrator

---

## Uninstallation

### Remove All Skills

**Claude Code**:
```bash
rm -rf ~/.claude/skills/n8n-*
```

**Claude.ai**:
1. Go to Settings → Capabilities → Skills
2. Delete each n8n skill individually

### Remove Specific Skill

```bash
rm -rf ~/.claude/skills/n8n-expression-syntax
```

---

## Updating

### Update All Skills

```bash
cd n8n-skills
git pull origin main
cp -r skills/* ~/.claude/skills/
```

### Update Single Skill

```bash
cp -r skills/n8n-expression-syntax ~/.claude/skills/
```

---

## Advanced Configuration

### Custom Skill Location

If using custom skills directory:

```bash
# Set environment variable
export CLAUDE_SKILLS_DIR="/path/to/custom/skills"

# Copy skills
cp -r skills/* $CLAUDE_SKILLS_DIR/
```

### Selective Installation

Install only specific skills:

```bash
# Only expression syntax and MCP tools expert
cp -r skills/n8n-expression-syntax ~/.claude/skills/
cp -r skills/n8n-mcp-tools-expert ~/.claude/skills/
```

---

## Next Steps

✅ Installation complete? Continue to [USAGE.md](USAGE.md) for usage examples.

---

## Support

- **Issues**: https://github.com/czlonkowski/n8n-skills/issues
- **Discussions**: https://github.com/czlonkowski/n8n-skills/discussions
- **n8n-mcp**: https://github.com/romualdczlonkowski/n8n-mcp

---

Conceived by Romuald Członkowski - [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
