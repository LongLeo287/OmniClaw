---
id: github.com-czlonkowski-n8n-skills-2a4dafee-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:42.721568
---

# KNOWLEDGE EXTRACT: github.com_czlonkowski_n8n-skills_2a4dafee
> **Extracted on:** 2026-04-01 08:45:01
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007519770/github.com_czlonkowski_n8n-skills_2a4dafee

---

## File: `.gitignore`
```
.mcp.json
```

## File: `.mcp.json.example`
```
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

## File: `CLAUDE.md`
```markdown
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
├── brain/knowledge/docs_legacy/                  # Documentation
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
- `n8n_update_partial_workflow` - Incremental updates (18 operation types including `activateWorkflow`, `transferWorkflow`)
- `n8n_validate_workflow` - Validate by ID
- `n8n_autofix_workflow` - Auto-fix common issues
- `n8n_deploy_template` - Deploy template to n8n instance
- `n8n_workflow_versions` - Version history and rollback
- `n8n_test_workflow` - Test execution
- `n8n_executions` - Manage executions

### Data Tables
- `n8n_manage_datatable` - Manage data tables and rows (CRUD, filtering, dry-run)

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

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Romuald Członkowski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
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

See [brain/knowledge/docs_legacy/INSTALLATION.md](installation.md) for detailed instructions.

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

- [Installation Guide](installation.md) - Detailed installation for all platforms
- [Usage Guide](usage.md) - How to use skills effectively
- [Development Guide](../../../core/security/QUARANTINE/vetted/repos/llm_lean_log/docs/development.md) - Contributing and testing
- [MCP Testing Log](brain/knowledge/docs_legacy/MCP_TESTING_LOG.md) - Real tool responses used in skills

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

Contributions welcome! Please see [DEVELOPMENT.md](../../../core/security/QUARANTINE/vetted/repos/llm_lean_log/docs/development.md) for guidelines.

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

## File: `build.sh`
```bash
#!/bin/bash
# Build script for n8n-skills distribution packages
# Creates zip files for both Claude.ai (individual skills) and Claude Code (bundle)

set -e

DIST_DIR="dist"
VERSION="1.1.0"

echo "🔨 Building n8n-skills distribution packages..."

# Create dist directory if it doesn't exist
mkdir -p "$DIST_DIR"

# Remove old zips
echo "🗑️  Removing old zip files..."
rm -f "$DIST_DIR"/*.zip

# Build individual skill zips (for Claude.ai)
echo "📦 Building individual skill zips for Claude.ai..."

SKILLS=(
    "n8n-expression-syntax"
    "n8n-mcp-tools-expert"
    "n8n-workflow-patterns"
    "n8n-validation-expert"
    "n8n-node-configuration"
)

for skill in "${SKILLS[@]}"; do
    echo "   - $skill"
    zip -rq "$DIST_DIR/${skill}-v${VERSION}.zip" "skills/${skill}/" -x "*.DS_Store"
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

## File: `brain/knowledge/docs_legacy/CODE_NODE_BEST_PRACTICES.md`
```markdown
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
   ```python
   amount = item["json"].get("amount") or 0  # Default to 0
   text = item["json"].get("text", "").strip()  # Default to empty string
   ```

3. **Use list comprehensions for filtering**
   ```python
   # ✅ Pythonic
   valid = [item for item in items if item["json"].get("active")]

   # ❌ Verbose
   valid = []
   for item in items:
       if item["json"].get("active"):
           valid.append(item)
   ```

4. **Return consistent structure**
   ```python
   # Always return list of objects with "json" key
   return [{"json": result}]  # Single result
   return results  # Multiple results (already formatted)
   return []  # No results
   ```

5. **Debug with print() statements**
   ```python
   print(f"Processing {len(items)} items")  # Appears in browser console
   print(f"Item data: {item['json']}")
   ```

---

## 3. Common Data Access Patterns

### Usage Distribution
| Pattern | Usage % | Best For |
|---------|---------|----------|
| `$input.all()` | 26% | Processing arrays, batch operations |
| `$input.first()` | 25% | Single item operations, first-last logic |
| `$input.item` | 19% | Item-by-item processing in loops |
| Other patterns | 16% | Complex scenarios |
| `$json` | 11% | Direct field access |
| `$node` | 1% | Referencing other node outputs |
| `$env` | 0.2% | Environment variables |
| `$binary` | 0.1% | Binary data processing |

### Key Recommendations
1. **Use `$input.all()` when:** Processing multiple records, aggregating data, batch transformations
2. **Use `$input.first()` when:** Working with single objects, API responses, initial data processing
3. **Use `$input.item` when:** In split/loop contexts, iterating collections, item-by-item logic
4. **Avoid `$json` alone:** Always use `$input.first().json` or `$input.item.json` to ensure data availability

---

## 3. Return Value Structures

### Recommended Return Patterns
```javascript
// Pattern 1: Single object transformation (39% of successful nodes)
return [{
  json: {
    field1: value1,
    field2: value2
  }
}];

// Pattern 2: Array passthrough (24% of successful nodes)
return $input.all();

// Pattern 3: Mapped transformation (most common)
const transformed = $input.all()
  .filter(item => item.json.valid)
  .map(item => ({
    json: {
      id: item.json.id,
      processed: true,
      timestamp: new Date().toISOString()
    }
  }));
return transformed;

// Pattern 4: Conditional returns
if (shouldProcess) {
  return [{json: processedData}];
} else {
  return [];  // Empty array when no data
}

// Pattern 5: Multiple outputs
const results = [];
for (const item of $input.all()) {
  if (item.json.valid) {
    results.push({json: item.json});
  }
}
return results;
```

### What NOT to Return
```javascript
// ❌ Incorrect: Raw data without json wrapper
return $input.all();  // Missing .map()

// ❌ Incorrect: String instead of object
return "processed";

// ❌ Incorrect: Object without array wrapper
return {
  json: {field: value}
};

// ❌ Incorrect: Incomplete structure
return [{data: value}];  // Should be: {json: value}

// ❌ Incorrect: Throwing without structure
throw new Error("Something failed");  // No graceful handling
```

---

## 4. Top 5 Error Patterns to Avoid

### Error #1: Empty Code (23% of validation failures)
```
Message: "Code cannot be empty"
Occurrences: 58

Solution: Always include meaningful code or use a different node type
```

**What to Do:**
```javascript
// Always provide implementation
const items = $input.all();
return items.map(item => ({
  json: {
    ...item.json,
    processed: true
  }
}));
```

---

### Error #2: Missing Return Statement (15% of validation failures)
```
Message: "Code must return data for the next node"
Occurrences: 29

Solution: Always return data, even if empty
```

**What to Do:**
```javascript
const items = $input.all();

// Always include a return statement
if (items.length === 0) {
  return [];  // Return empty array if no items
}

return items.map(item => ({json: item.json}));
```

---

### Error #3: Expression Syntax Confusion (8% of validation failures)
```
Message: "Expression syntax {{...}} is not valid in Code nodes"
Occurrences: 5

Solution: Use JavaScript template literals, NOT n8n expressions
```

**What to Do:**
```javascript
// ❌ Wrong: Using n8n expression syntax
const value = "{{ $json.field }}";

// ✅ Correct: Using JavaScript template literals
const value = `${$json.field}`;

// ✅ Also correct: Direct access
const value = $input.first().json.field;
```

---

### Error #4: Unmatched Expression Brackets (6% of validation failures)
```
Message: "Unmatched expression brackets: 0 opening, 1 closing"
Occurrences: 4

Solution: Ensure quote/bracket balance in JSONB storage
```

**What to Do:**
```javascript
// When storing multi-line strings, escape properly
const code = `const text = 'It\\'s working correctly';
const result = text.split('\\n');
return [{json: {result}}];`;

// Test: Check all quotes are properly escaped
```

---

### Error #5: Incorrect Return Wrapper (5% of validation failures)
```
Message: "Return value must be an array of objects"
Occurrences: 3

Solution: Always wrap output in array, each element must have json property
```

**What to Do:**
```javascript
// ❌ Wrong: Single object
return {
  json: {field: value}
};

// ✅ Correct: Array of objects
return [{
  json: {field: value}
}];

// ✅ Also correct: Array with multiple items
return [
  {json: {id: 1, data: 'first'}},
  {json: {id: 2, data: 'second'}}
];
```

---

## 5. Performance & Best Practices

### Success Rate Metrics
- **47.16% of workflows** use CODE nodes
- **4,461 unique users** creating workflows with CODE nodes
- **Average patterns:** Most successful nodes combine 2-3 common techniques

### Common Node Sequence Patterns
Most successful workflows follow this pattern:
1. HTTP Request / Webhook (data ingestion)
2. CODE node (transformation)
3. CODE node (normalization/enrichment)
4. Database write / API output

### Optimization Tips

**1. Use `$input.all()` over loops when possible:**
```javascript
// ❌ Slower: Multiple loops
let results = [];
for (const item of $input.all()) {
  results.push({json: item.json});
}

// ✅ Faster: Single map operation
return $input.all().map(item => ({json: item.json}));
```

**2. Filter early, process late:**
```javascript
// ✅ Good: Filter first, then transform
const processed = $input.all()
  .filter(item => item.json.valid)
  .map(item => ({json: normalize(item.json)}));
```

**3. Pre-compile regex patterns:**
```javascript
// ✅ Define outside loop
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

for (const item of $input.all()) {
  if (emailRegex.test(item.json.email)) {
    // Process valid email
  }
}
```

**4. Use guard clauses:**
```javascript
// ✅ Fail fast
if (!$input.first().json.data) {
  return [];
}

const data = $input.first().json.data;
// Continue processing
```

---

## 6. Library & Built-in Availability

### n8n Built-in Methods & Variables (JavaScript)

#### Core Data Access
| Method | Description | Example |
|--------|-------------|---------|
| `$input.all()` | Get all input items | `const items = $input.all();` |
| `$input.first()` | Get first input item | `const first = $input.first();` |
| `$input.last()` | Get last input item | `const last = $input.last();` |
| `$input.item` | Current item (Each Item mode) | `const current = $input.item;` |
| `items` | Array of all items (legacy) | `items[0].json.field` |
| `$json` | Current item JSON (Each Item mode) | `const field = $json.field;` |
| `$binary` | Current item binary data | `$binary.data` |

#### Node & Workflow Context
| Method | Description | Example |
|--------|-------------|---------|
| `$node` | Reference other node outputs | `$node['HTTP Request'].json.data` |
| `$prevNode` | Access previous node data | `$prevNode.name` |
| `$workflow` | Workflow metadata | `$workflow.name`, `$workflow.id` |
| `$execution` | Execution context | `$execution.id`, `$execution.mode` |
| `$env` | Environment variables | `$env.MY_VAR` |

#### Date & Time Helpers (Luxon-based)
| Variable | Description | Example Output |
|----------|-------------|----------------|
| `$now` | Current datetime object | Luxon DateTime |
| `$today` | Today at midnight | Luxon DateTime |
| `$now.toISO()` | ISO 8601 format | `"2025-01-20T10:30:00.000Z"` |
| `$now.toFormat('yyyy-MM-dd')` | Custom format | `"2025-01-20"` |
| `$now.plus({days: 7})` | Date arithmetic | 7 days from now |
| `$now.minus({hours: 2})` | Subtract time | 2 hours ago |

```javascript
// Date examples
const tomorrow = $now.plus({days: 1}).toISO();
const lastWeek = $now.minus({weeks: 1}).toFormat('yyyy-MM-dd');
const isWeekend = $now.weekday > 5;  // 6 = Saturday, 7 = Sunday
```

#### Data Querying with JMESPath
| Method | Description | Example |
|--------|-------------|---------|
| `$jmespath(data, query)` | Query JSON structures | `$jmespath(data, 'users[?age > `21`].name')` |

```javascript
// JMESPath examples
const data = $input.first().json;

// Filter array
const adults = $jmespath(data, 'users[?age >= `18`]');

// Extract specific fields
const names = $jmespath(data, 'users[*].name');

// Complex queries
const topScores = $jmespath(data, 'scores | sort_by(@, &value) | reverse(@) | [0:5]');
```

#### Utility Methods
| Method | Description | Example |
|--------|-------------|---------|
| `$getWorkflowStaticData()` | Persistent workflow data | `const counter = $getWorkflowStaticData().counter \|\| 0;` |
| `$evaluateExpression(expr, itemIndex)` | Evaluate n8n expression | `$evaluateExpression('{{ $json.field }}', 0)` |

### Python Built-in Methods (Beta)

| Python | JavaScript | Description |
|--------|------------|-------------|
| `_input.all()` | `$input.all()` | Get all items |
| `_input.first()` | `$input.first()` | Get first item |
| `_input.last()` | `$input.last()` | Get last item |
| `_input.item` | `$input.item` | Current item |
| `_items` | `items` | All items array (Native) |
| `_item` | `$item` | Current item (Native) |
| `_now` | `$now` | Current datetime |
| `_today` | `$today` | Today at midnight |
| `_jmespath(data, query)` | `$jmespath()` | Query JSON |

```python
# Python (Beta) examples
from datetime import timedelta

# Date operations
tomorrow = _now + timedelta(days=1)
last_week = _now - timedelta(weeks=1)

# JMESPath querying
data = _input.first()["json"]
adults = _jmespath(data, 'users[?age >= `18`]')
```

### Standard JavaScript/Python Objects (No imports needed)

**JavaScript:**
- `Math` - Math functions: `Math.max()`, `Math.random()`, etc.
- `Date` - Date operations: `new Date()`, `.toISOString()`
- `JSON` - JSON parsing: `JSON.parse()`, `JSON.stringify()`
- `Buffer` - Base64: `Buffer.from(data, 'base64')`
- `console` - Logging: `console.log()`, `console.error()`
- `Object` - Object methods: `Object.keys()`, `Object.entries()`
- `Array` - Array methods: `.map()`, `.filter()`, `.reduce()`

**Python:**
- `re` - Regular expressions
- `json` - JSON parsing
- `datetime` - Date/time operations
- `statistics` - Statistical functions
- `base64` - Base64 encoding/decoding
- `print()` - Debug logging

### Common Code Patterns

**Base64 Encoding/Decoding:**
```javascript
// Decode
const decoded = Buffer.from(encoded, 'base64').toString();

// Encode
const encoded = Buffer.from(text).toString('base64');
```

**Date Formatting:**
```javascript
// ISO format
const iso = new Date().toISOString();

// Locale string
const local = new Date().toLocaleString('en-US');

// Custom format
const parts = new Date().toISOString().split('T');
const date = parts[0];  // YYYY-MM-DD
```

**JSON Operations:**
```javascript
// Parse with default
const data = JSON.parse(jsonString || '{}');

// Stringify with formatting
const pretty = JSON.stringify(data, null, 2);

// Ordered keys
const ordered = {};
Object.keys(data).sort().forEach(key => {
  ordered[key] = data[key];
});
```

---

## 7. Real-World Template Examples

The following examples are from popular n8n workflow templates (214K+ views):

### Example 1: Scene Extraction with Error Handling
```javascript
// From: "Generate AI Viral Videos" workflow (214,907 views)
function findSceneEntries(obj) {
  const scenes = [];

  for (const [key, value] of Object.entries(obj)) {
    if (key.toLowerCase().startsWith("scene") && typeof value === "string") {
      scenes.push(value);
    } else if (typeof value === "object" && value !== null) {
      scenes.push(...findSceneEntries(value));  // Recursive search
    }
  }

  return scenes;
}

let output = [];

try {
  const inputData = items[0].json;
  const scenes = findSceneEntries(inputData);

  if (scenes.length === 0) {
    throw new Error("No scene keys found at any level.");
  }

  output = scenes.map(scene => ({ description: scene }));
} catch (e) {
  throw new Error("Could not extract scenes properly. Details: " + e.message);
}

return output;
```
**Key Techniques:** Recursive object traversal, try-catch error handling, validation

### Example 2: Array to Object Property Mapping
```javascript
// From: "Generate AI Viral Videos" workflow (214,907 views)
// Collect video URLs from multiple items into single object
return [
  {
    video_urls: items.map(item => item.json.video.url)
  }
];
```
**Key Techniques:** Array mapping, property extraction, single result aggregation

### Example 3: Binary Data Manipulation
```javascript
// From: "Automate Social Media Content" workflow (205,470 views)
// Rename binary property for downstream processing
$input.first().binary.data = $input.first().binary.Upload_Image__optional_
delete $input.first().binary.Upload_Image__optional_
return $input.first()
```
**Key Techniques:** Binary property manipulation, object mutation, passthrough pattern

---

## 8. Quick Reference Checklist

Before deploying CODE nodes, verify:

- [ ] **Code is not empty** - Must have meaningful logic
- [ ] **Return statement exists** - Must return array of objects
- [ ] **Proper return format** - Each item: `{json: {...}}`
- [ ] **Data access correct** - Using `$input.all()`, `$input.first()`, or `$input.item`
- [ ] **No n8n expressions** - Use JavaScript template literals instead: `` `${value}` ``
- [ ] **Error handling** - Guard clauses for null/undefined inputs
- [ ] **Quote escaping** - Properly escape strings in JSONB
- [ ] **Loop logic correct** - Avoid infinite loops, use proper conditions
- [ ] **Performance** - Prefer map/filter over manual loops for small datasets
- [ ] **Output consistent** - All paths return same structure

---

## 9. Additional Resources

### Official n8n Documentation
- **Code Node Guide:** https://docs.n8n.io/code/code-node/
- **Code Examples:** https://docs.n8n.io/code/cookbook/code-node/
- **Built-in Methods Reference:** https://docs.n8n.io/code-examples/methods-variables-reference/
- **n8n Expressions:** https://docs.n8n.io/code/expressions/
- **Luxon Date Library:** https://moment.github.io/luxon/

### Common Use Cases Quick Reference
- **Data transformation:** See Section 2, Patterns 1, 3, 5
- **Filtering & ranking:** See Section 2, Patterns 2, 6, 9
- **Format conversion:** See Section 2, Patterns 4, 7, 8
- **Python examples:** See Section 2 (Python patterns)
- **Error handling:** See Section 5 (Performance tips, guard clauses)
- **Real-world examples:** See Section 7 (Template examples)

### When to Use CODE Node vs Other Nodes
| Scenario | Use This | Not CODE Node |
|----------|----------|---------------|
| Simple field mapping | Set node | ✓ Simpler UI |
| Basic filtering | Filter node | ✓ Visual interface |
| Conditional routing | If/Switch node | ✓ Better clarity |
| Complex transformations | **CODE node** | ✗ Too limited |
| Multi-step logic | **CODE node** | ✗ Needs chaining |
| Custom calculations | **CODE node** | ✗ No built-in |
| API response parsing | **CODE node** | ✗ Complex structure |
| Recursive operations | **CODE node** | ✗ Not possible |

### Related n8n Nodes
- **If/Switch:** Conditional logic (use CODE for complex conditions with multiple criteria)
- **Set:** Simple field mapping (use CODE for transformations requiring logic)
- **Merge:** Combining data (use CODE for custom merge logic with conflict resolution)
- **Split:** Array handling (use CODE for complex filtering and grouping)
- **Function:** Legacy node (CODE node is the modern replacement)
- **Execute Command:** Shell commands (use CODE for JavaScript/Python processing)

### n8n Community Resources
- **Community Forum:** https://community.n8n.io/c/questions/code-node
- **Workflow Templates:** https://n8n.io/workflows (filter by "Code" node)
- **GitHub Discussions:** https://github.com/n8n-io/n8n/discussions

---

## 10. Summary & Key Takeaways

### Essential Rules for CODE Node Success

1. **Choose the Right Mode**
   - Use "Run Once for All Items" (default) for 95% of use cases
   - Only use "Each Item" mode for independent per-item operations

2. **Master Data Access Patterns**
   - `$input.all()` for batch processing and aggregation (26% usage)
   - `$input.first()` for single-item operations (25% usage)
   - `$input.item` only in "Each Item" mode (19% usage)

3. **Always Return Correct Format**
   - Single result: `return [{json: {...}}]`
   - Multiple results: `return items.map(item => ({json: item}))`
   - No results: `return []`
   - Never return raw objects, strings, or missing array wrapper

4. **Use JavaScript Unless You Need Python**
   - JavaScript: 95% of use cases, faster, full n8n helpers
   - Python: Data science, ML, specific library requirements only

5. **Implement Error Handling**
   - Use guard clauses for null/undefined checks
   - Provide fallback values with `.get()` or `||` operator
   - Wrap risky operations in try-catch blocks
   - Return meaningful error messages

6. **Optimize for Performance**
   - Prefer `.map()`, `.filter()`, `.reduce()` over manual loops
   - Filter early, process late
   - Pre-compile regex patterns outside loops
   - Use early returns to avoid unnecessary processing

7. **Debug Effectively**
   - JavaScript: `console.log()` outputs to browser console
   - Python: `print()` statements for debugging
   - Test with minimal data first, then scale up
   - Validate with n8n's built-in execution viewer

### Common Pitfalls to Avoid

❌ **Empty code or missing return statement** (39% of failures)
❌ **Using n8n expression syntax `{{}}` instead of JavaScript template literals**
❌ **Returning raw objects without `[{json: {...}}]` wrapper**
❌ **Accessing properties without null checks** (causes crashes)
❌ **Using wrong mode** (Each Item when All Items would be better)

### Success Metrics from Real-World Data

- **47.16% of all n8n workflows** use CODE nodes (15,202 workflows analyzed)
- **4,461 unique users** creating CODE node workflows
- **78% use "All Items" mode** (more efficient for batch operations)
- **39% success rate improvement** when following return format patterns

### Next Steps

1. **Start Simple:** Begin with basic transformations using the patterns in Section 2
2. **Study Examples:** Review the 10 successful patterns and template examples (Sections 2.1-2.10, 7)
3. **Test Incrementally:** Start with 1-2 items, then scale to production data
4. **Use the Checklist:** Follow Section 8 before deploying to production
5. **Learn n8n Helpers:** Master `$input`, `$now`, and `$jmespath` (Section 6)
6. **Join the Community:** Ask questions on the n8n forum for specific use cases

With these patterns, best practices, and real-world insights, you'll create robust, maintainable CODE nodes that process data efficiently and reliably across your n8n workflows.

---

**Document Metadata:**
- **Based on:** 38,094 CODE node instances from 15,202 workflows
- **Analysis Period:** Last 60 days
- **Data Sources:** n8n telemetry database, workflow templates, official documentation
- **Last Updated:** January 2025
- **n8n Version:** Supports Code node v2.x (JavaScript, Python Beta, Python Native Beta)

---

**Conceived by Romuald Członkowski** - [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)
```

## File: `brain/knowledge/docs_legacy/DEVELOPMENT.md`
```markdown
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
├── brain/knowledge/docs_legacy/                      # Documentation
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

**Document tool responses** in `brain/knowledge/docs_legacy/MCP_TESTING_LOG.md`:

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
See [n8n MCP Tools Expert](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)
See [COMMON_MISTAKES.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/creative_design/c4_architecture/references/common_mistakes.md)
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

## File: `brain/knowledge/docs_legacy/INSTALLATION.md`
```markdown
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

## File: `brain/knowledge/docs_legacy/MCP_TESTING_LOG.md`
```markdown
# MCP Tool Testing Log
## Generated: 2025-10-20
## Purpose: Document actual tool responses for skill content creation

This log contains real responses from n8n-mcp tools to inform accurate skill content.

---

## n8n API Status

**Health Check Result**:
```json
{
  "status": "ok",
  "apiUrl": "https://n8n-test.n8n-mcp.com",
  "mcpVersion": "2.20.3",
  "versionCheck": "up to date",
  "responseTime": 798ms
}
```

✅ **n8n API Tools Available**: All workflow creation/management tools functional

---

## Database Statistics

```json
{
  "totalNodes": 537,
  "totalTemplates": 2653,
  "statistics": {
    "aiTools": 270,
    "triggers": 108,
    "versionedNodes": 141,
    "nodesWithDocumentation": 470,
    "documentationCoverage": "88%"
  },
  "packageBreakdown": [
    {"package": "@n8n/n8n-nodes-langchain", "nodeCount": 100},
    {"package": "n8n-nodes-base", "nodeCount": 437}
  ]
}
```

**Key Insights**:
- 537 nodes total (437 base + 100 langchain)
- 270 AI-capable tools
- 108 trigger nodes
- 88% documentation coverage
- 2,653 templates with avg 4,115 views

---

## Search Tool Testing

### search_nodes - Common Queries

**Query: "webhook"** → Returns Webhook (trigger), Respond to Webhook (transform)
- nodeType format: `nodes-base.webhook`
- workflowNodeType format: `n8n-nodes-base.webhook`
- ⚠️ **Critical**: Use different formats for different tools!

**Query: "http"** → Returns HTTP Request, HTTP Request Tool (AI), Code Tool
- Regular: `nodes-base.httpRequest`
- AI Tool: `nodes-langchain.toolHttpRequest`

**Query: "database"** → Returns Firebase, Redis Vector Store, etc.

---

## Node Essentials Testing

### Webhook Node

**Key Properties**:
- `httpMethod`: GET, POST, PUT, DELETE, etc. (default: GET)
- `path`: Webhook URL path (e.g., "form-submit")
- `responseMode`: onReceived, lastNode, responseNode
- **CRITICAL**: Webhook data structure is `$json.body.*` not `$json.*`

**Output Structure**:
```javascript
{
  "headers": {...},
  "params": {...},
  "query": {...},
  "body": {  // ⚠️ User data is HERE!
    "name": "John",
    "email": "john@example.com"
  }
}
```

---

## Validation Testing

### Validation Profiles Comparison

**Test Config**: `{resource: "channel", operation: "create"}` on Slack node

**Result**: Missing required field "name"
- All profiles detected this error
- Fix provided: "Provide a channel name"
- Warning about rate limits (best practice)

---

## Template Analysis

**Total Templates**: 2,653
**Popular Templates** (webhook + slack):
- #2947: Weather via Slack (1,500 views) - Webhook → OpenStreetMap → NWS → Slack
- #4039: Download Slack Media (778 views) - SlackTrigger → HTTP Request
- #5529: Jamf Patch to Slack (147 views) - Complex multi-node

**Key Pattern**: Webhook → Transform → Action → Notify (5-7 nodes avg)

---

## Critical Findings for Skills

### 1. Expression Syntax (Skill #1)
- ✅ Webhook data under `.body` (not root)
- ✅ Code nodes use direct access ($json), NOT expressions ({{}})
- ✅ Node references: `$node["Node Name"].json.field`

### 2. MCP Tools Expert (Skill #2)
- ✅ nodeType formats differ: `nodes-base.*` vs `n8n-nodes-base.*`
- ✅ get_node preferred over get_node({detail: "full"}) (5KB vs 100KB+)
- ✅ Validation profiles: minimal/runtime/ai-friendly/strict
- ✅ Smart parameters: branch="true"/"false" for IF, case=N for Switch
- ✅ Auto-sanitization runs on ALL nodes during any update

### 3. Workflow Patterns (Skill #3)
- ✅ 2,653 real templates available
- ✅ Template metadata includes complexity, setup time, services
- ✅ Common pattern: Trigger → Process → Act (5-7 nodes)
- ✅ Webhook workflows: 27.6% of all workflows

### 4. Validation Expert (Skill #4)
- ✅ Real validation errors documented
- ✅ Auto-sanitization fixes operator structures
- ✅ Binary operators (equals, contains) vs unary (isEmpty, isNotEmpty)

### 5. Node Configuration (Skill #5)
- ✅ Property dependencies documented (e.g., sendBody → contentType)
- ✅ Operation-specific requirements vary
- ✅ 8 AI connection types supported

---

## Tools Availability Summary

**Available WITHOUT n8n API**:
- search_nodes, search_nodes, get_node ✅
- validate_node({mode: "minimal"}), validate_node ✅
- validate_workflow, get_node({mode: "search_properties"}) ✅
- search_templates, get_template, list_tasks ✅

**Requires n8n API** (AVAILABLE at n8n-test.n8n-mcp.com):
- n8n_create_workflow ✅
- n8n_update_partial_workflow ✅
- n8n_validate_workflow (by ID) ✅
- n8n_list_workflows, n8n_get_workflow ✅
- n8n_trigger_webhook_workflow ✅

---

**Testing Complete**: Ready for skill implementation with real data!
```

## File: `brain/knowledge/docs_legacy/USAGE.md`
```markdown
# Usage Guide

Learn how to use n8n-skills effectively with Claude.

---

## How Skills Activate

Skills activate **automatically** based on your query content. You don't need to manually invoke them.

### Activation Triggers

Each skill has specific triggers defined in its frontmatter:

```markdown
---
name: n8n Expression Syntax
description: Validate n8n expression syntax and fix common errors. Use when writing n8n expressions, using {{}} syntax, accessing $json/$node variables, or troubleshooting expression errors in workflows.
---
```

When your query matches the description keywords, the skill activates.

---

## Individual Skill Usage

### 1. n8n Expression Syntax

**Activates on**: expression, {{}}  syntax, $json, $node, webhook data access

**Example Queries**:
```
"How do I write n8n expressions?"
"Why is {{$json.email}} showing undefined?"
"Access webhook data in Slack node"
"What's wrong with my $node reference?"
```

**What You'll Learn**:
- Correct {{}} syntax
- Webhook data structure ($json.body.*)
- Node references ($node["Node Name"].json)
- Common mistakes and fixes
- When NOT to use expressions (Code nodes)

**Example Response**:
```
[Skill activates]

n8n expressions must be wrapped in double curly braces:

✅ Correct: {{$json.body.email}}
❌ Wrong: $json.body.email

For webhook data, remember it's under .body:
{{$json.body.name}}  // Webhook form data
{{$json.body.message}}  // Webhook message

In Code nodes, use direct access (no {{}}):
const email = $json.body.email;  // Correct in Code node
```

---

### 2. n8n MCP Tools Expert

**Activates on**: search nodes, validate, find node, MCP tools, template, workflow

**Example Queries**:
```
"Find me a Slack node"
"How do I search for database nodes?"
"Validate this node configuration"
"What's the difference between get_node({detail: "full"}) and get_node?"
"Which MCP tool should I use to create workflows?"
```

**What You'll Learn**:
- Tool selection (which tool for which task)
- nodeType format differences
- Validation profiles (minimal/runtime/ai-friendly/strict)
- Common MCP tool mistakes
- Workflow management tools

**Example Response**:
```
[Skill activates]

To find the Slack node, use search_nodes:

search_nodes({query: "slack"})

This returns:
- nodeType: "nodes-base.slack" (for search/validate tools)
- workflowNodeType: "n8n-nodes-base.slack" (for workflows)

⚠️ Important: Use different formats for different tools!

Next, get node details:
get_node({nodeType: "nodes-base.slack"})

This returns focused 5KB data vs 100KB+ from get_node({detail: "full"}).
```

---

### 3. n8n Workflow Patterns

**Activates on**: build workflow, webhook, pattern, architecture, workflow structure

**Example Queries**:
```
"Build a webhook to Slack workflow"
"What's the best pattern for API integration?"
"Create a scheduled database workflow"
"Show me webhook processing pattern"
```

**What You'll Learn**:
- 5 proven patterns (webhook, HTTP API, database, AI, scheduled)
- Workflow creation checklist
- Node connection best practices
- Real template examples
- Pattern selection guide

**Example Response**:
```
[Skill activates]

For webhook to Slack, use the Webhook Processing pattern:

Pattern Structure:
Webhook Trigger → [Transform] → Slack Notification

Workflow Checklist:
□ Search for nodes (search_nodes)
□ Get node configurations (get_node)
□ Create workflow structure
□ Add data mappings (expressions)
□ Validate workflow
□ Test with sample data

Real Example from Template #2947:
Webhook → OpenStreetMap → NWS → Slack
(1,500 views, proven pattern)
```

---

### 4. n8n Validation Expert

**Activates on**: validation, error, fix, debug, validate workflow

**Example Queries**:
```
"Why is my workflow validation failing?"
"Fix this validation error"
"Explain this validation warning"
"What does auto-sanitization do?"
```

**What You'll Learn**:
- Validation loop workflow
- Error interpretation
- Auto-sanitization system
- False positives handling
- Profile selection

**Example Response**:
```
[Skill activates]

Validation Error: "Required field 'channel' missing"

Fix:
validate_node({
  nodeType: "nodes-base.slack",
  config: {
    resource: "message",
    operation: "post",
    channel: "#general",  // Add this!
    text: "Message"
  },
  profile: "runtime"
})

Auto-sanitization will fix:
✅ Binary operator structures (equals, contains)
✅ Unary operator structures (isEmpty, isNotEmpty)
✅ Missing metadata in IF/Switch nodes

But cannot fix:
❌ Broken connections
❌ Branch count mismatches
```

---

### 5. n8n Node Configuration

**Activates on**: configure node, property, operation, dependencies, AI workflow

**Example Queries**:
```
"How do I configure the HTTP Request node?"
"What properties does the Slack node need?"
"Explain property dependencies"
"Set up AI Agent workflow"
```

**What You'll Learn**:
- Operation-specific requirements
- Property dependencies (sendBody → contentType)
- AI connection types (8 types)
- Common configuration patterns

**Example Response**:
```
[Skill activates]

HTTP Request node property dependencies:

1. Set sendBody = true
   ↓ Reveals: contentType

2. Set contentType = "json"
   ↓ Reveals: specifyBody

3. Set specifyBody = "json"
   ↓ Reveals: jsonBody

This cascade of 32 dependencies ensures you see only relevant properties!

For AI workflows, 8 connection types:
- ai_languageModel (OpenAI, Anthropic)
- ai_tool (HTTP Request Tool, Code Tool)
- ai_memory (Window Buffer Memory)
- ai_outputParser, ai_embedding, ai_vectorStore...
```

---

## Cross-Skill Composition

Skills work **together automatically**. Here's how:

### Example: Complete Workflow Build

**Your Query**:
```
"Build and validate a webhook to Slack workflow with proper data mapping"
```

**What Happens** (all automatic):

**Step 1**: n8n Workflow Patterns activates
```
→ Identifies: Webhook Processing Pattern
→ Provides: Workflow structure
```

**Step 2**: n8n MCP Tools Expert activates
```
→ Searches: search_nodes({query: "webhook"})
→ Searches: search_nodes({query: "slack"})
→ Gets details: get_node for both
```

**Step 3**: n8n Node Configuration activates
```
→ Guides: Webhook node setup (path, httpMethod)
→ Guides: Slack node setup (resource, operation, channel)
```

**Step 4**: n8n Expression Syntax activates
```
→ Provides: {{$json.body.message}} for data mapping
→ Warns: Webhook data is under .body!
```

**Step 5**: n8n Validation Expert activates
```
→ Validates: Complete workflow structure
→ Checks: Node configurations
→ Reports: Any errors or warnings
```

**Result**: Complete, validated, working workflow!

---

## Common Use Cases

### Use Case 1: Quick Node Search

```
You: "Find email nodes"

[n8n MCP Tools Expert activates]
Claude: Uses search_nodes({query: "email"})
Returns: Gmail, Email Send, IMAP Email, etc.
```

### Use Case 2: Fix Expression Error

```
You: "My {{$json.name}} is showing undefined in webhook workflow"

[n8n Expression Syntax activates]
Claude: Webhook data is under .body!
Fix: {{$json.body.name}}
```

### Use Case 3: Understand Validation Error

```
You: "Validation says 'binary operator cannot have singleValue'"

[n8n Validation Expert activates]
Claude: Binary operators (equals, contains) should NOT have singleValue.
Auto-sanitization will fix this on next update.
```

### Use Case 4: Build AI Workflow

```
You: "Create an AI Agent workflow with HTTP Request tool"

[n8n Workflow Patterns + Node Configuration activate]
Claude: AI Agent Workflow Pattern:
1. Connect language model: sourceOutput="ai_languageModel"
2. Connect tool: sourceOutput="ai_tool"
3. Connect memory: sourceOutput="ai_memory"

[Provides complete configuration]
```

---

## Best Practices

### 1. Be Specific

**Good**: "Build a webhook that receives form data and posts to Slack"
**Better**: "Build a webhook to Slack workflow with form validation and error handling"

**Why**: More specific queries activate relevant skills with better context.

### 2. Ask Follow-Up Questions

Skills provide deep knowledge. Don't hesitate to ask:
```
"Explain property dependencies in HTTP Request node"
"Show me more webhook examples"
"What are validation profiles?"
```

### 3. Request Validation

Always ask for validation:
```
"Build this workflow AND validate it"
"Check if this configuration is correct"
```

### 4. Leverage Cross-Skill Knowledge

```
"Build, validate, and explain the expressions in this workflow"
→ Activates: Patterns + Validation + Expression Syntax
```

### 5. Reference Real Templates

```
"Show me template #2947 and explain how it works"
→ Uses n8n-mcp tools to fetch and analyze real templates
```

---

## Skill Limitations

### What Skills CAN Do:
✅ Teach n8n concepts
✅ Guide MCP tool usage
✅ Provide workflow patterns
✅ Interpret validation errors
✅ Explain configurations
✅ Reference real templates

### What Skills CANNOT Do:
❌ Execute workflows (use n8n for that)
❌ Access your n8n instance directly (use n8n-mcp API tools)
❌ Modify running workflows
❌ Debug runtime execution errors (only configuration errors)

---

## Tool Availability

**Always Available** (no n8n API needed):
- search_nodes, search_nodes, get_node ✅
- validate_node({mode: "minimal"}), validate_node ✅
- validate_workflow, get_node({mode: "search_properties"}) ✅
- search_templates, get_template ✅

**Requires n8n API** (N8N_API_URL + N8N_API_KEY):
- n8n_create_workflow ⚠️
- n8n_update_partial_workflow ⚠️
- n8n_validate_workflow (by ID) ⚠️
- n8n_list_workflows, n8n_get_workflow ⚠️
- n8n_trigger_webhook_workflow ⚠️

If API tools unavailable, skills use templates and validation-only workflows.

---

## Troubleshooting

### Skill Not Activating

**Problem**: Skill doesn't activate when expected

**Solution**: Rephrase query to match activation keywords
```
Instead of: "How do I use expressions?"
Try: "How do I write n8n expressions with {{}} syntax?"
```

### Wrong Skill Activates

**Problem**: Different skill than expected activates

**Solution**: This is usually fine! Skills complement each other.
If needed, be more specific:
```
"Using n8n MCP tools, search for webhook node"
```

### Multiple Skills Needed

**Problem**: Need knowledge from multiple skills

**Solution**: Ask a comprehensive question:
```
"Build, configure, and validate a webhook workflow with explanations"
```

All relevant skills will activate automatically.

---

## Advanced Usage

### Request Specific Tool Usage

```
"Use get_node to show me Slack node configuration"
```

### Ask for Real Examples

```
"Show me real template examples of webhook workflows"
```

### Request Step-by-Step

```
"Step by step: build a webhook to database workflow with validation at each step"
```

### Debug with Skills

```
"My workflow fails validation. Debug it using validation expert knowledge."
```

---

## Next Steps

- **Getting Started**: Try example queries above
- **Deep Dive**: Read individual SKILL.md files in skills/
- **Contribute**: See [DEVELOPMENT.md](../../../core/security/QUARANTINE/vetted/repos/llm_lean_log/docs/development.md)

---

## Support

- **Issues**: https://github.com/czlonkowski/n8n-skills/issues
- **Discussions**: https://github.com/czlonkowski/n8n-skills/discussions

---

**Ready to build amazing n8n workflows with Claude? Start asking questions!** 🚀

---

Conceived by Romuald Członkowski - [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)
```

## File: `evaluations/code-javascript/eval-001-webhook-body-gotcha.json`
```json
{
  "id": "code-js-001",
  "skills": ["n8n-code-javascript"],
  "query": "I'm getting undefined when trying to access data from my webhook in a Code node. My code is: const name = $json.name; const email = $json.email; Why isn't this working?",
  "expected_behavior": [
    "Activate n8n-code-javascript skill",
    "Explain that webhook data is nested under the .body property",
    "Show correct syntax: $json.body.name and $json.body.email",
    "Reference DATA_ACCESS.md for webhook structure details",
    "Mention this is the #1 most common mistake",
    "Optionally show alternative: const webhookData = $json.body; then access webhookData.name"
  ],
  "expected_content": [
    "webhook data",
    ".body",
    "$json.body.name",
    "DATA_ACCESS.md"
  ],
  "priority": "high",
  "notes": "This is the MOST common mistake. Skill must clearly explain .body nesting."
}
```

## File: `evaluations/code-javascript/eval-002-return-format-error.json`
```json
{
  "id": "code-js-002",
  "skills": ["n8n-code-javascript"],
  "query": "My Code node is showing an error: 'Return value must be an array of objects'. My code returns: return {json: {result: 'success', data: processedData}}; What's wrong?",
  "expected_behavior": [
    "Activate n8n-code-javascript skill",
    "Explain the return format must be an ARRAY of objects",
    "Show correct syntax: return [{json: {result: 'success', data: processedData}}];",
    "Note the square brackets [] wrapping the object",
    "Reference ERROR_PATTERNS.md #3 for detailed explanation",
    "Show multiple items format as well",
    "Emphasize this is error #3 in top 5 errors (5% of failures)"
  ],
  "expected_content": [
    "array",
    "[{json:",
    "ERROR_PATTERNS.md",
    "square brackets"
  ],
  "priority": "high",
  "notes": "Return format error is 5% of all failures. Must clearly show array wrapper requirement."
}
```

## File: `evaluations/code-javascript/eval-003-http-request.json`
```json
{
  "id": "code-js-003",
  "skills": ["n8n-code-javascript"],
  "query": "How do I make an HTTP API call from inside a JavaScript Code node in n8n? I need to call an external API with authentication.",
  "expected_behavior": [
    "Activate n8n-code-javascript skill",
    "Explain $helpers.httpRequest() built-in function",
    "Show complete example with method, url, headers",
    "Include authentication example (Bearer token or API key)",
    "Show try-catch error handling pattern",
    "Reference BUILTIN_FUNCTIONS.md for complete API reference",
    "Mention this is async, needs await",
    "Show both GET and POST examples if appropriate"
  ],
  "expected_content": [
    "$helpers.httpRequest",
    "await",
    "headers",
    "Authorization",
    "BUILTIN_FUNCTIONS.md",
    "try-catch"
  ],
  "priority": "medium",
  "notes": "$helpers.httpRequest() is a key built-in function that many users need to learn."
}
```

## File: `evaluations/code-javascript/eval-004-aggregation-pattern.json`
```json
{
  "id": "code-js-004",
  "skills": ["n8n-code-javascript"],
  "query": "I need to sum up all the 'amount' values from multiple items in my Code node. How do I access all items and calculate a total?",
  "expected_behavior": [
    "Activate n8n-code-javascript skill",
    "Show $input.all() to get all items",
    "Demonstrate reduce() function for summing",
    "Include null handling (item.json.amount || 0)",
    "Show complete return format with result",
    "Reference COMMON_PATTERNS.md for aggregation patterns",
    "Reference DATA_ACCESS.md for $input.all() details",
    "Emphasize 'Run Once for All Items' mode",
    "Optionally show additional aggregations (count, average)"
  ],
  "expected_content": [
    "$input.all()",
    "reduce",
    "COMMON_PATTERNS.md",
    "DATA_ACCESS.md",
    "All Items"
  ],
  "priority": "high",
  "notes": "Aggregation is a very common use case. Tests understanding of $input.all() and array methods."
}
```

## File: `evaluations/code-javascript/eval-005-expression-syntax-confusion.json`
```json
{
  "id": "code-js-005",
  "skills": ["n8n-code-javascript"],
  "query": "I'm trying to access a field in my Code node but it's not working. My code is: const userName = '{{ $json.name }}'; I'm getting the literal string instead of the value. What am I doing wrong?",
  "expected_behavior": [
    "Activate n8n-code-javascript skill",
    "Explain that {{ }} expression syntax does NOT work in Code nodes",
    "Clarify distinction: {{ }} is for OTHER nodes (Set, IF, HTTP Request)",
    "Show correct JavaScript syntax: const userName = $json.name;",
    "Show JavaScript template literals for string interpolation: `Hello ${$json.name}`",
    "Reference ERROR_PATTERNS.md #2 for detailed explanation",
    "Emphasize this is error #2 in top 5 errors (8% of failures)",
    "Provide comparison table of when to use expressions vs JavaScript"
  ],
  "expected_content": [
    "{{ }}",
    "expression syntax",
    "JavaScript",
    "$json.name",
    "template literals",
    "ERROR_PATTERNS.md",
    "backticks"
  ],
  "priority": "high",
  "notes": "Expression syntax confusion is 8% of failures. Critical to understand Code nodes use JavaScript, not expressions."
}
```

## File: `evaluations/code-python/eval-001-module-import-error.json`
```json
{
  "id": "code-python-001",
  "skill": "n8n-code-python",
  "name": "Module Import Error - External Libraries Not Available",
  "description": "Tests understanding that Python Code nodes have NO external libraries",
  "query": "I'm writing a Python Code node to fetch data from an API. Here's my code:\n\n```python\nimport requests\n\nurl = \"https://api.example.com/users\"\nresponse = requests.get(url)\ndata = response.json()\n\nreturn [{\"json\": data}]\n```\n\nBut I'm getting a ModuleNotFoundError. What's wrong?",
  "expected_behavior": [
    "Immediately identify this is the #1 Python Code node limitation",
    "Explain that NO external libraries are available (no requests, pandas, numpy)",
    "Recommend using JavaScript Code node instead (95% recommendation)",
    "Suggest alternative: Use HTTP Request node BEFORE Python Code node",
    "Mention urllib.request from standard library as limited workaround",
    "Emphasize JavaScript has $helpers.httpRequest() built-in",
    "Reference ERROR_PATTERNS.md Error #1"
  ],
  "expected_output_includes": [
    "ModuleNotFoundError",
    "NO external libraries",
    "Use JavaScript",
    "HTTP Request node",
    "standard library only"
  ],
  "should_not_include": [
    "pip install",
    "install requests",
    "add requirements.txt"
  ]
}
```

## File: `evaluations/code-python/eval-002-dictionary-keyerror.json`
```json
{
  "id": "code-python-002",
  "skill": "n8n-code-python",
  "name": "Dictionary KeyError - Use .get() Instead",
  "description": "Tests understanding of safe dictionary access with .get()",
  "query": "My Python Code node is failing with this error:\n\n```\nKeyError: 'email'\n```\n\nHere's my code:\n\n```python\nitem = _input.first()[\"json\"]\n\nname = item[\"name\"]\nemail = item[\"email\"]\nage = item[\"age\"]\n\nreturn [{\n    \"json\": {\n        \"name\": name,\n        \"email\": email,\n        \"age\": age\n    }\n}]\n```\n\nHow do I fix this?",
  "expected_behavior": [
    "Identify KeyError is from direct dictionary key access",
    "Explain that some items may not have 'email' field",
    "Recommend using .get() method with default values",
    "Show corrected code with .get()",
    "Mention this is Error #3 in ERROR_PATTERNS.md",
    "Explain difference between item['key'] and item.get('key', default)"
  ],
  "expected_output_includes": [
    "KeyError",
    ".get()",
    "default value",
    "item.get(\"email\", \"default\")"
  ],
  "should_not_include": [
    "try/except KeyError",
    "if 'email' in item"
  ],
  "correct_code_pattern": "item.get(\"email\", "
}
```

## File: `evaluations/code-python/eval-003-webhook-body-gotcha.json`
```json
{
  "id": "code-python-003",
  "skill": "n8n-code-python",
  "name": "Webhook Body Gotcha - Data Under [\"body\"]",
  "description": "Tests understanding that webhook data is nested under [\"body\"] key",
  "query": "I have a Webhook node receiving this JSON:\n\n```json\n{\n  \"name\": \"Alice\",\n  \"email\": \"alice@example.com\",\n  \"age\": 30\n}\n```\n\nIn my Python Code node, I'm trying to access the data:\n\n```python\ndata = _input.first()[\"json\"]\n\nname = data[\"name\"]  # KeyError!\nemail = data[\"email\"]  # KeyError!\n\nreturn [{\"json\": {\"name\": name, \"email\": email}}]\n```\n\nBut I'm getting KeyError. The webhook is receiving data correctly. What's wrong?",
  "expected_behavior": [
    "Immediately recognize this is the webhook .body gotcha",
    "Explain webhook node wraps incoming data under 'body' key",
    "Show the actual structure with headers, params, query, body",
    "Provide corrected code accessing data[\"body\"]",
    "Mention this is a CRITICAL gotcha highlighted in DATA_ACCESS.md",
    "Recommend using .get() for safe access: data.get(\"body\", {})"
  ],
  "expected_output_includes": [
    "[\"body\"]",
    "webhook wraps",
    "nested under body",
    "data.get(\"body\", {})"
  ],
  "correct_code_pattern": "data.get(\"body\", {})",
  "should_emphasize": "This is the MOST COMMON webhook mistake"
}
```

## File: `evaluations/code-python/eval-004-return-format-error.json`
```json
{
  "id": "code-python-004",
  "skill": "n8n-code-python",
  "name": "Return Format Error - Must Return Array with json Key",
  "description": "Tests understanding of correct return format for n8n Code nodes",
  "query": "My Python Code node isn't outputting any data to the next node. Here's my code:\n\n```python\nall_items = _input.all()\n\ntotal = sum(item[\"json\"].get(\"amount\", 0) for item in all_items)\naverage = total / len(all_items) if all_items else 0\n\nreturn {\n    \"total\": total,\n    \"count\": len(all_items),\n    \"average\": average\n}\n```\n\nThe code runs without errors, but the next node receives nothing. What's wrong?",
  "expected_behavior": [
    "Identify incorrect return format (missing array wrapper and json key)",
    "Explain n8n expects array of objects with 'json' key",
    "Show corrected code with proper format: [{\"json\": {...}}]",
    "Mention this is Error #5 in ERROR_PATTERNS.md",
    "Emphasize: MUST return array, even for single result"
  ],
  "expected_output_includes": [
    "[{\"json\":",
    "array",
    "return format",
    "must wrap"
  ],
  "correct_code_pattern": "return [{\"json\": {",
  "should_not_include": [
    "return {",
    "return total"
  ]
}
```

## File: `evaluations/code-python/eval-005-standard-library-usage.json`
```json
{
  "id": "code-python-005",
  "skill": "n8n-code-python",
  "name": "Standard Library Usage - Know What's Available",
  "description": "Tests knowledge of available standard library modules",
  "query": "I need to do the following in a Python Code node:\n\n1. Parse JSON from a string\n2. Calculate SHA256 hash of some data\n3. Format the current date as ISO string\n4. Extract email addresses using regex\n\nWhat modules are available? Can I use external libraries?",
  "expected_behavior": [
    "Emphasize NO external libraries available",
    "List available standard library modules for these tasks",
    "json module for JSON parsing",
    "hashlib module for SHA256",
    "datetime module for dates",
    "re module for regex",
    "Provide code examples for each task",
    "Reference STANDARD_LIBRARY.md"
  ],
  "expected_output_includes": [
    "import json",
    "import hashlib",
    "import datetime",
    "import re",
    "standard library only",
    "NO external libraries"
  ],
  "should_not_include": [
    "import requests",
    "import pandas",
    "pip install"
  ],
  "correct_modules": [
    "json",
    "hashlib",
    "datetime",
    "re"
  ]
}
```

## File: `evaluations/expression-syntax/eval-001-missing-braces.json`
```json
{
  "id": "expr-001",
  "skills": ["n8n-expression-syntax"],
  "query": "I'm trying to access an email field in my n8n Slack node using $json.email but it's showing as literal text '$json.email' in the message. What's wrong?",
  "expected_behavior": [
    "Identifies missing curly braces around the expression",
    "Explains that n8n expressions must be wrapped in {{ }}",
    "Provides the corrected expression: {{$json.email}}",
    "Explains that without braces, it's treated as literal text",
    "References expression format documentation from SKILL.md"
  ],
  "baseline_without_skill": {
    "likely_response": "May suggest general JavaScript or template syntax, might not know n8n-specific {{ }} requirement",
    "expected_quality": "Low - lacks n8n-specific knowledge about expression syntax"
  },
  "with_skill_expected": {
    "response_quality": "High - precise fix with n8n-specific guidance",
    "uses_skill_content": true,
    "provides_correct_syntax": true,
    "explains_why_it_failed": true
  }
}
```

## File: `evaluations/expression-syntax/eval-002-webhook-body-data.json`
```json
{
  "id": "expr-002",
  "skills": ["n8n-expression-syntax"],
  "query": "My webhook workflow is showing {{$json.name}} as undefined even though I'm sending {\"name\": \"John\"} in the webhook POST request. What am I doing wrong?",
  "expected_behavior": [
    "Identifies that webhook data is nested under .body property",
    "Explains the webhook node output structure",
    "Provides the corrected expression: {{$json.body.name}}",
    "Shows the complete webhook data structure with headers, params, query, and body",
    "Emphasizes this is a CRITICAL gotcha specific to webhook nodes"
  ],
  "baseline_without_skill": {
    "likely_response": "May suggest debugging or checking data format, unlikely to know webhook-specific structure",
    "expected_quality": "Low - would miss the webhook .body nesting"
  },
  "with_skill_expected": {
    "response_quality": "High - identifies webhook-specific issue immediately",
    "uses_skill_content": true,
    "provides_correct_syntax": true,
    "explains_webhook_structure": true,
    "warns_about_common_gotcha": true
  }
}
```

## File: `evaluations/expression-syntax/eval-003-code-node-confusion.json`
```json
{
  "id": "expr-003",
  "skills": ["n8n-expression-syntax"],
  "query": "I'm trying to use {{$json.email}} in my Code node to get the email address, but it's not working. The code shows the literal string '{{$json.email}}' instead of the value. How do I fix this?",
  "expected_behavior": [
    "Identifies that Code nodes use direct JavaScript access, NOT expressions",
    "Explains that {{ }} syntax is NOT used inside Code nodes",
    "Provides the corrected Code node syntax: $json.email or $input.item.json.email",
    "Explains when NOT to use expressions (Code nodes, Function nodes)",
    "References Code node guide or documentation"
  ],
  "baseline_without_skill": {
    "likely_response": "May suggest template literal syntax or string interpolation, unlikely to know n8n Code node specifics",
    "expected_quality": "Low - would not understand Code node vs expression node difference"
  },
  "with_skill_expected": {
    "response_quality": "High - immediately identifies Code node vs expression context",
    "uses_skill_content": true,
    "provides_correct_code_syntax": true,
    "explains_when_not_to_use_expressions": true,
    "clear_distinction_between_contexts": true
  }
}
```

## File: `evaluations/expression-syntax/eval-004-node-reference.json`
```json
{
  "id": "expr-004",
  "skills": ["n8n-expression-syntax"],
  "query": "How do I reference data from my 'HTTP Request' node in a later Slack node? I need to access the response data.",
  "expected_behavior": [
    "Provides correct $node syntax with quotes around node name",
    "Shows example: {{$node[\"HTTP Request\"].json.fieldName}}",
    "Explains that node names with spaces require bracket notation and quotes",
    "Warns that node names are case-sensitive and must match exactly",
    "Provides multiple examples from real workflows"
  ],
  "baseline_without_skill": {
    "likely_response": "May suggest generic data passing or variable references, might not know n8n $node syntax",
    "expected_quality": "Medium - might guess at syntax but miss specifics like quotes and case sensitivity"
  },
  "with_skill_expected": {
    "response_quality": "High - precise $node syntax with proper quoting",
    "uses_skill_content": true,
    "provides_correct_syntax": true,
    "explains_case_sensitivity": true,
    "shows_multiple_examples": true
  }
}
```

## File: `evaluations/mcp-tools/eval-001-tool-selection.json`
```json
{
  "id": "mcp-001",
  "skills": ["n8n-mcp-tools-expert"],
  "query": "I need to find a node that can send messages to Slack. Which n8n-mcp tool should I use and how?",
  "expected_behavior": [
    "Recommends search_nodes as the starting tool",
    "Provides correct syntax: search_nodes({query: 'slack'})",
    "Explains the nodeType format returned (nodes-base.slack)",
    "Suggests following up with get_node_essentials for configuration details",
    "References the search → essentials workflow pattern",
    "Mentions the tool is <20ms fast"
  ],
  "baseline_without_skill": {
    "likely_response": "May suggest searching documentation or using generic search, unlikely to know specific MCP tool names and syntax",
    "expected_quality": "Low - would not know n8n-mcp specific tools"
  },
  "with_skill_expected": {
    "response_quality": "High - precise tool recommendation with syntax",
    "uses_skill_content": true,
    "provides_correct_tool": true,
    "shows_proper_workflow": true,
    "explains_nodeType_format": true
  }
}
```

## File: `evaluations/mcp-tools/eval-002-nodetype-format.json`
```json
{
  "id": "mcp-002",
  "skills": ["n8n-mcp-tools-expert"],
  "query": "I'm getting 'node not found' errors when calling get_node_essentials. I'm using 'slack' as the nodeType. What's wrong?",
  "expected_behavior": [
    "Identifies incorrect nodeType format",
    "Explains need for prefix: 'nodes-base.slack' not just 'slack'",
    "Distinguishes between nodeType (nodes-base.*) and workflowNodeType (n8n-nodes-base.*)",
    "Provides correct syntax: get_node_essentials({nodeType: 'nodes-base.slack'})",
    "References nodeType format documentation from SKILL.md",
    "Warns about common format confusion"
  ],
  "baseline_without_skill": {
    "likely_response": "May suggest checking spelling or tool availability, unlikely to know specific prefix requirements",
    "expected_quality": "Low - would not understand nodeType format nuances"
  },
  "with_skill_expected": {
    "response_quality": "High - immediately identifies format issue",
    "uses_skill_content": true,
    "provides_correct_format": true,
    "explains_prefix_difference": true,
    "gives_working_example": true
  }
}
```

## File: `evaluations/mcp-tools/eval-003-validation-workflow.json`
```json
{
  "id": "mcp-003",
  "skills": ["n8n-mcp-tools-expert"],
  "query": "I've created a Slack node configuration and want to make sure it's valid before deploying. Walk me through the validation process using n8n-mcp tools.",
  "expected_behavior": [
    "Recommends validate_node_operation tool",
    "Explains validation profiles (minimal, runtime, ai-friendly, strict)",
    "Recommends 'runtime' profile for pre-deployment",
    "Shows complete validation syntax with all parameters",
    "Explains validation loop pattern (validate → fix → validate again)",
    "References VALIDATION_GUIDE.md",
    "Mentions 23s avg thinking time, 58s avg fixing time from telemetry"
  ],
  "baseline_without_skill": {
    "likely_response": "May suggest testing the workflow or checking documentation, unlikely to know validation tools and profiles",
    "expected_quality": "Medium - might guess at validation but miss profile options"
  },
  "with_skill_expected": {
    "response_quality": "High - complete validation workflow with profiles",
    "uses_skill_content": true,
    "recommends_correct_profile": true,
    "shows_validation_loop": true,
    "explains_error_handling": true
  }
}
```

## File: `evaluations/mcp-tools/eval-004-essentials-vs-info.json`
```json
{
  "id": "mcp-004",
  "skills": ["n8n-mcp-tools-expert"],
  "query": "Should I use get_node_info or get_node_essentials to understand how to configure a node? What's the difference?",
  "expected_behavior": [
    "Strongly recommends get_node_essentials for most cases",
    "Explains size difference (5KB vs 100KB+)",
    "Explains success rate difference (91.7% vs 80%)",
    "Lists when to use get_node_info (debugging complex issues, need full schema)",
    "Provides performance comparison (<10ms vs slower)",
    "References the 20% failure rate for get_node_info",
    "Shows examples of both tool calls"
  ],
  "baseline_without_skill": {
    "likely_response": "May assume more data is better, unlikely to know performance and reliability differences",
    "expected_quality": "Low - would not understand the critical difference"
  },
  "with_skill_expected": {
    "response_quality": "High - clear recommendation with data-driven reasoning",
    "uses_skill_content": true,
    "recommends_essentials": true,
    "explains_trade_offs": true,
    "provides_both_examples": true
  }
}
```

## File: `evaluations/mcp-tools/eval-005-smart-parameters.json`
```json
{
  "id": "mcp-005",
  "skills": ["n8n-mcp-tools-expert"],
  "query": "I'm using n8n_update_partial_workflow to connect an IF node to two different handlers. How do I specify which branch (true or false) each connection should use?",
  "expected_behavior": [
    "Explains smart parameters for multi-output nodes",
    "Shows branch parameter: branch='true' or branch='false'",
    "Provides complete example with addConnection operation",
    "Explains this is simpler than using sourceIndex manually",
    "Mentions Switch nodes use case=N parameter",
    "References WORKFLOW_GUIDE.md for more details",
    "Shows both true and false branch connections"
  ],
  "baseline_without_skill": {
    "likely_response": "May suggest using output indices without knowing semantic parameters exist",
    "expected_quality": "Medium - might work but miss the easier smart parameter approach"
  },
  "with_skill_expected": {
    "response_quality": "High - teaches smart parameters for cleaner code",
    "uses_skill_content": true,
    "shows_branch_parameter": true,
    "provides_working_example": true,
    "mentions_switch_equivalent": true
  }
}
```

## File: `evaluations/node-configuration/eval-001-property-dependencies.json`
```json
{
  "id": "node-config-001",
  "skills": ["n8n-node-configuration"],
  "query": "I'm configuring an HTTP Request node with method=POST. What other fields become required or visible when I set this?",
  "expected_behavior": [
    "Explains property dependencies (displayOptions)",
    "Identifies that sendBody becomes visible for POST",
    "Explains that body becomes required when sendBody=true",
    "Suggests using get_property_dependencies to see all dependencies",
    "Provides guidance on checking conditional requirements",
    "May reference DEPENDENCIES.md for detailed dependency rules"
  ]
}
```

## File: `evaluations/node-configuration/eval-002-operation-specific-config.json`
```json
{
  "id": "node-config-002",
  "skills": ["n8n-node-configuration"],
  "query": "How do I configure a Slack node to post a message? What fields are required for this specific operation?",
  "expected_behavior": [
    "Identifies need to set resource='message' and operation='post'",
    "Explains operation-specific required fields (channel, text)",
    "Suggests using get_node_essentials with operation context",
    "Provides example configuration for this operation",
    "May reference OPERATION_PATTERNS.md for Slack patterns",
    "Explains that different operations have different requirements"
  ]
}
```

## File: `evaluations/node-configuration/eval-003-conditional-fields.json`
```json
{
  "id": "node-config-003",
  "skills": ["n8n-node-configuration"],
  "query": "My IF node configuration is valid with operation='equals', but when I change to operation='isEmpty', validation fails. Why?",
  "expected_behavior": [
    "Explains that isEmpty is a unary operator (single value)",
    "Identifies that value2 is not needed for unary operators",
    "Explains singleValue property dependency",
    "Mentions auto-sanitization will fix operator structure",
    "Suggests using get_property_dependencies to understand operator rules",
    "May reference DEPENDENCIES.md for operator-specific dependencies"
  ]
}
```

## File: `evaluations/node-configuration/eval-004-essentials-vs-info.json`
```json
{
  "id": "node-config-004",
  "skills": ["n8n-node-configuration"],
  "query": "Should I use get_node_essentials or get_node_info when configuring a new node? What's the difference?",
  "expected_behavior": [
    "Recommends get_node_essentials for configuration (91.7% success rate)",
    "Explains essentials provides required fields and options",
    "Explains get_node_info provides full schema (use when essentials insufficient)",
    "Suggests starting with essentials, escalate to info if needed",
    "May provide telemetry insight (essentials used 9,835 times)",
    "References progressive disclosure approach"
  ]
}
```

## File: `evaluations/validation-expert/eval-001-missing-required-field.json`
```json
{
  "id": "validation-001",
  "skills": ["n8n-validation-expert"],
  "query": "I'm getting a validation error: 'Missing required field: channel'. What does this mean and how do I fix it?",
  "expected_behavior": [
    "Identifies this as a 'missing_required' error type",
    "Explains that the node configuration is incomplete",
    "Provides guidance on finding what value to provide",
    "Suggests using get_node_essentials to see required fields",
    "Explains where to add the missing field in the node configuration",
    "May reference ERROR_CATALOG.md for details"
  ]
}
```

## File: `evaluations/validation-expert/eval-002-false-positive.json`
```json
{
  "id": "validation-002",
  "skills": ["n8n-validation-expert"],
  "query": "Validation is warning me about 'best_practice' issues like error handling and retries. Do I need to fix these?",
  "expected_behavior": [
    "Identifies these as warnings, not errors",
    "Explains difference between errors (must fix) and warnings (should fix)",
    "Discusses when warnings can be acceptable (false positives)",
    "References FALSE_POSITIVES.md",
    "Suggests using 'ai-friendly' validation profile to reduce false positives",
    "Explains that warnings don't prevent workflow activation",
    "Provides guidance on when to address warnings vs when to accept them"
  ]
}
```

## File: `evaluations/validation-expert/eval-003-auto-sanitization.json`
```json
{
  "id": "validation-003",
  "skills": ["n8n-validation-expert"],
  "query": "I'm getting an error about 'Binary operator cannot have singleValue property'. What does this mean?",
  "expected_behavior": [
    "Identifies this as an operator structure issue",
    "Explains auto-sanitization system",
    "States that this error will be automatically fixed on next workflow update",
    "Explains binary vs unary operator distinction",
    "References the auto-sanitization section",
    "Suggests that user doesn't need to manually fix this",
    "May suggest running n8n_update_partial_workflow or validate_workflow to trigger auto-fix"
  ]
}
```

## File: `evaluations/validation-expert/eval-004-validation-loop.json`
```json
{
  "id": "validation-004",
  "skills": ["n8n-validation-expert"],
  "query": "I fixed one validation error but now I'm getting a different one. How do I systematically fix all validation errors?",
  "expected_behavior": [
    "Explains the validation loop pattern",
    "References telemetry data (7,841 validate → fix cycles, avg 23s thinking + 58s fixing)",
    "Provides step-by-step process: validate → read errors → fix → validate again",
    "Emphasizes iterative approach",
    "Suggests fixing errors one at a time",
    "May recommend validate_node_operation for individual nodes",
    "Explains that this is normal workflow (not a problem)"
  ]
}
```

## File: `evaluations/workflow-patterns/eval-001-webhook-workflow.json`
```json
{
  "id": "pattern-001",
  "skills": ["n8n-workflow-patterns"],
  "query": "I need to build a workflow that receives webhook data and sends it to Slack. What's the best way to structure this?",
  "expected_behavior": [
    "Identifies this as a Webhook Processing pattern",
    "References the webhook_processing.md pattern file",
    "Explains the basic structure: Webhook → Transform → Output",
    "Mentions data is nested under $json.body for webhook payloads",
    "Suggests validation and error handling",
    "May reference real template examples",
    "Provides checklist: trigger, validation, transformation, output, error handling"
  ]
}
```

## File: `evaluations/workflow-patterns/eval-002-http-api-workflow.json`
```json
{
  "id": "pattern-002",
  "skills": ["n8n-workflow-patterns"],
  "query": "I want to fetch data from a REST API, transform it, and store it in my database. How should I structure this workflow?",
  "expected_behavior": [
    "Identifies this as an HTTP API Integration pattern",
    "References the http_api_integration.md pattern file",
    "Explains the structure: Trigger → HTTP Request → Transform → Database → Error Handler",
    "Discusses authentication handling (credentials)",
    "Mentions pagination for large datasets",
    "Suggests retry logic for API failures",
    "Provides guidance on response parsing and data mapping"
  ]
}
```

## File: `evaluations/workflow-patterns/eval-003-database-sync.json`
```json
{
  "id": "pattern-003",
  "skills": ["n8n-workflow-patterns"],
  "query": "How do I build a workflow that syncs data between two databases? I need to read from Postgres and write to MySQL.",
  "expected_behavior": [
    "Identifies this as a Database Operations pattern",
    "References the database_operations.md pattern file",
    "Explains the structure: Schedule/Trigger → Read DB → Transform → Write DB → Error Handler",
    "Discusses batch processing for large datasets",
    "Mentions transaction handling and rollback considerations",
    "Suggests incremental sync strategies (last_modified timestamps)",
    "Warns about connection pooling and performance",
    "Provides guidance on data type mapping between databases"
  ]
}
```

## File: `evaluations/workflow-patterns/eval-004-ai-agent.json`
```json
{
  "id": "pattern-004",
  "skills": ["n8n-workflow-patterns"],
  "query": "I want to build an AI agent that can use tools to answer questions. What's the recommended workflow pattern?",
  "expected_behavior": [
    "Identifies this as an AI Agent Workflow pattern",
    "References the ai_agent_workflow.md pattern file",
    "Explains the structure: Trigger → AI Agent (with Language Model + Tools + Memory)",
    "Discusses the 8 AI connection types (ai_languageModel, ai_tool, ai_memory, etc.)",
    "Mentions that ANY node can be an AI tool (connected via ai_tool port)",
    "Suggests memory integration for conversation context",
    "Provides guidance on tool configuration and result handling",
    "May mention langchain package nodes"
  ]
}
```

## File: `evaluations/workflow-patterns/eval-005-scheduled-report.json`
```json
{
  "id": "pattern-005",
  "skills": ["n8n-workflow-patterns"],
  "query": "I need to generate a daily report that fetches analytics data and emails it to my team. What's the best workflow structure?",
  "expected_behavior": [
    "Identifies this as a Scheduled Tasks pattern",
    "References the scheduled_tasks.md pattern file",
    "Explains the structure: Schedule Trigger → Fetch Data → Transform/Aggregate → Format Report → Send Email",
    "Discusses cron expression configuration",
    "Mentions timezone considerations",
    "Suggests error handling and failure notifications",
    "Provides guidance on data aggregation and report formatting",
    "May suggest using templates for consistent report structure"
  ]
}
```

## File: `skills/n8n-code-javascript/BUILTIN_FUNCTIONS.md`
```markdown
# Built-in Functions - JavaScript Code Node

Complete reference for n8n's built-in JavaScript functions and helpers.

---

## Overview

n8n Code nodes provide powerful built-in functions beyond standard JavaScript. This guide covers:

1. **$helpers.httpRequest()** - Make HTTP requests
2. **DateTime (Luxon)** - Advanced date/time operations
3. **$jmespath()** - Query JSON structures
4. **$getWorkflowStaticData()** - Persistent storage
5. **Standard JavaScript Globals** - Math, JSON, console, etc.
6. **Available Node.js Modules** - crypto, Buffer, URL

---

## 1. $helpers.httpRequest() - HTTP Requests

Make HTTP requests directly from Code nodes without using HTTP Request node.

### Basic Usage

```javascript
const response = await $helpers.httpRequest({
  method: 'GET',
  url: 'https://api.example.com/users'
});

return [{json: {data: response}}];
```

### Complete Options

```javascript
const response = await $helpers.httpRequest({
  method: 'POST',  // GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS
  url: 'https://api.example.com/users',
  headers: {
    'Authorization': 'Bearer token123',
    'Content-Type': 'application/json',
    'User-Agent': 'n8n-workflow'
  },
  body: {
    name: 'John Doe',
    email: 'john@example.com'
  },
  qs: {  // Query string parameters
    page: 1,
    limit: 10
  },
  timeout: 10000,  // Milliseconds (default: no timeout)
  json: true,  // Auto-parse JSON response (default: true)
  simple: false,  // Don't throw on HTTP errors (default: true)
  resolveWithFullResponse: false  // Return only body (default: false)
});
```

### GET Request

```javascript
// Simple GET
const users = await $helpers.httpRequest({
  method: 'GET',
  url: 'https://api.example.com/users'
});

return [{json: {users}}];
```

```javascript
// GET with query parameters
const results = await $helpers.httpRequest({
  method: 'GET',
  url: 'https://api.example.com/search',
  qs: {
    q: 'javascript',
    page: 1,
    per_page: 50
  }
});

return [{json: results}];
```

### POST Request

```javascript
// POST with JSON body
const newUser = await $helpers.httpRequest({
  method: 'POST',
  url: 'https://api.example.com/users',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + $env.API_KEY
  },
  body: {
    name: $json.body.name,
    email: $json.body.email,
    role: 'user'
  }
});

return [{json: newUser}];
```

### PUT/PATCH Request

```javascript
// Update resource
const updated = await $helpers.httpRequest({
  method: 'PATCH',
  url: `https://api.example.com/users/${userId}`,
  body: {
    name: 'Updated Name',
    status: 'active'
  }
});

return [{json: updated}];
```

### DELETE Request

```javascript
// Delete resource
await $helpers.httpRequest({
  method: 'DELETE',
  url: `https://api.example.com/users/${userId}`,
  headers: {
    'Authorization': 'Bearer ' + $env.API_KEY
  }
});

return [{json: {deleted: true, userId}}];
```

### Authentication Patterns

```javascript
// Bearer Token
const response = await $helpers.httpRequest({
  url: 'https://api.example.com/data',
  headers: {
    'Authorization': `Bearer ${$env.API_TOKEN}`
  }
});
```

```javascript
// API Key in Header
const response = await $helpers.httpRequest({
  url: 'https://api.example.com/data',
  headers: {
    'X-API-Key': $env.API_KEY
  }
});
```

```javascript
// Basic Auth (manual)
const credentials = Buffer.from(`${username}:${password}`).toString('base64');

const response = await $helpers.httpRequest({
  url: 'https://api.example.com/data',
  headers: {
    'Authorization': `Basic ${credentials}`
  }
});
```

### Error Handling

```javascript
// Handle HTTP errors gracefully
try {
  const response = await $helpers.httpRequest({
    method: 'GET',
    url: 'https://api.example.com/users',
    simple: false  // Don't throw on 4xx/5xx
  });

  if (response.statusCode >= 200 && response.statusCode < 300) {
    return [{json: {success: true, data: response.body}}];
  } else {
    return [{
      json: {
        success: false,
        status: response.statusCode,
        error: response.body
      }
    }];
  }
} catch (error) {
  return [{
    json: {
      success: false,
      error: error.message
    }
  }];
}
```

### Full Response Access

```javascript
// Get full response including headers and status
const response = await $helpers.httpRequest({
  url: 'https://api.example.com/data',
  resolveWithFullResponse: true
});

return [{
  json: {
    statusCode: response.statusCode,
    headers: response.headers,
    body: response.body,
    rateLimit: response.headers['x-ratelimit-remaining']
  }
}];
```

---

## 2. DateTime (Luxon) - Date & Time Operations

n8n includes Luxon for powerful date/time handling. Access via `DateTime` global.

### Current Date/Time

```javascript
// Current time
const now = DateTime.now();

// Current time in specific timezone
const nowTokyo = DateTime.now().setZone('Asia/Tokyo');

// Today at midnight
const today = DateTime.now().startOf('day');

return [{
  json: {
    iso: now.toISO(),  // "2025-01-20T15:30:00.000Z"
    formatted: now.toFormat('yyyy-MM-dd HH:mm:ss'),  // "2025-01-20 15:30:00"
    unix: now.toSeconds(),  // Unix timestamp
    millis: now.toMillis()  // Milliseconds since epoch
  }
}];
```

### Formatting Dates

```javascript
const now = DateTime.now();

return [{
  json: {
    isoFormat: now.toISO(),  // ISO 8601: "2025-01-20T15:30:00.000Z"
    sqlFormat: now.toSQL(),  // SQL: "2025-01-20 15:30:00.000"
    httpFormat: now.toHTTP(),  // HTTP: "Mon, 20 Jan 2025 15:30:00 GMT"

    // Custom formats
    dateOnly: now.toFormat('yyyy-MM-dd'),  // "2025-01-20"
    timeOnly: now.toFormat('HH:mm:ss'),  // "15:30:00"
    readable: now.toFormat('MMMM dd, yyyy'),  // "January 20, 2025"
    compact: now.toFormat('yyyyMMdd'),  // "20250120"
    withDay: now.toFormat('EEEE, MMMM dd, yyyy'),  // "Monday, January 20, 2025"
    custom: now.toFormat('dd/MM/yy HH:mm')  // "20/01/25 15:30"
  }
}];
```

### Parsing Dates

```javascript
// From ISO string
const dt1 = DateTime.fromISO('2025-01-20T15:30:00');

// From specific format
const dt2 = DateTime.fromFormat('01/20/2025', 'MM/dd/yyyy');

// From SQL
const dt3 = DateTime.fromSQL('2025-01-20 15:30:00');

// From Unix timestamp
const dt4 = DateTime.fromSeconds(1737384600);

// From milliseconds
const dt5 = DateTime.fromMillis(1737384600000);

return [{json: {parsed: dt1.toISO()}}];
```

### Date Arithmetic

```javascript
const now = DateTime.now();

return [{
  json: {
    // Adding time
    tomorrow: now.plus({days: 1}).toISO(),
    nextWeek: now.plus({weeks: 1}).toISO(),
    nextMonth: now.plus({months: 1}).toISO(),
    inTwoHours: now.plus({hours: 2}).toISO(),

    // Subtracting time
    yesterday: now.minus({days: 1}).toISO(),
    lastWeek: now.minus({weeks: 1}).toISO(),
    lastMonth: now.minus({months: 1}).toISO(),
    twoHoursAgo: now.minus({hours: 2}).toISO(),

    // Complex operations
    in90Days: now.plus({days: 90}).toFormat('yyyy-MM-dd'),
    in6Months: now.plus({months: 6}).toFormat('yyyy-MM-dd')
  }
}];
```

### Time Comparisons

```javascript
const now = DateTime.now();
const targetDate = DateTime.fromISO('2025-12-31');

return [{
  json: {
    // Comparisons
    isFuture: targetDate > now,
    isPast: targetDate < now,
    isEqual: targetDate.equals(now),

    // Differences
    daysUntil: targetDate.diff(now, 'days').days,
    hoursUntil: targetDate.diff(now, 'hours').hours,
    monthsUntil: targetDate.diff(now, 'months').months,

    // Detailed difference
    detailedDiff: targetDate.diff(now, ['months', 'days', 'hours']).toObject()
  }
}];
```

### Timezone Operations

```javascript
const now = DateTime.now();

return [{
  json: {
    // Current timezone
    local: now.toISO(),

    // Convert to different timezone
    tokyo: now.setZone('Asia/Tokyo').toISO(),
    newYork: now.setZone('America/New_York').toISO(),
    london: now.setZone('Europe/London').toISO(),
    utc: now.toUTC().toISO(),

    // Get timezone info
    timezone: now.zoneName,  // "America/Los_Angeles"
    offset: now.offset,  // Offset in minutes
    offsetFormatted: now.toFormat('ZZ')  // "+08:00"
  }
}];
```

### Start/End of Period

```javascript
const now = DateTime.now();

return [{
  json: {
    startOfDay: now.startOf('day').toISO(),
    endOfDay: now.endOf('day').toISO(),
    startOfWeek: now.startOf('week').toISO(),
    endOfWeek: now.endOf('week').toISO(),
    startOfMonth: now.startOf('month').toISO(),
    endOfMonth: now.endOf('month').toISO(),
    startOfYear: now.startOf('year').toISO(),
    endOfYear: now.endOf('year').toISO()
  }
}];
```

### Weekday & Month Info

```javascript
const now = DateTime.now();

return [{
  json: {
    // Day info
    weekday: now.weekday,  // 1 = Monday, 7 = Sunday
    weekdayShort: now.weekdayShort,  // "Mon"
    weekdayLong: now.weekdayLong,  // "Monday"
    isWeekend: now.weekday > 5,  // Saturday or Sunday

    // Month info
    month: now.month,  // 1-12
    monthShort: now.monthShort,  // "Jan"
    monthLong: now.monthLong,  // "January"

    // Year info
    year: now.year,  // 2025
    quarter: now.quarter,  // 1-4
    daysInMonth: now.daysInMonth  // 28-31
  }
}];
```

---

## 3. $jmespath() - JSON Querying

Query and transform JSON structures using JMESPath syntax.

### Basic Queries

```javascript
const data = $input.first().json;

// Extract specific field
const names = $jmespath(data, 'users[*].name');

// Filter array
const adults = $jmespath(data, 'users[?age >= `18`]');

// Get specific index
const firstUser = $jmespath(data, 'users[0]');

return [{json: {names, adults, firstUser}}];
```

### Advanced Queries

```javascript
const data = $input.first().json;

// Sort and slice
const top5 = $jmespath(data, 'users | sort_by(@, &score) | reverse(@) | [0:5]');

// Extract nested fields
const emails = $jmespath(data, 'users[*].contact.email');

// Multi-field extraction
const simplified = $jmespath(data, 'users[*].{name: name, email: contact.email}');

// Conditional filtering
const premium = $jmespath(data, 'users[?subscription.tier == `premium`]');

return [{json: {top5, emails, simplified, premium}}];
```

### Common Patterns

```javascript
// Pattern 1: Filter and project
const query1 = $jmespath(data, 'products[?price > `100`].{name: name, price: price}');

// Pattern 2: Aggregate functions
const query2 = $jmespath(data, 'sum(products[*].price)');
const query3 = $jmespath(data, 'max(products[*].price)');
const query4 = $jmespath(data, 'length(products)');

// Pattern 3: Nested filtering
const query5 = $jmespath(data, 'categories[*].products[?inStock == `true`]');

return [{json: {query1, query2, query3, query4, query5}}];
```

---

## 4. $getWorkflowStaticData() - Persistent Storage

Store data that persists across workflow executions.

### Basic Usage

```javascript
// Get static data storage
const staticData = $getWorkflowStaticData();

// Initialize counter if doesn't exist
if (!staticData.counter) {
  staticData.counter = 0;
}

// Increment counter
staticData.counter++;

return [{
  json: {
    executionCount: staticData.counter
  }
}];
```

### Use Cases

```javascript
// Use Case 1: Rate limiting
const staticData = $getWorkflowStaticData();
const now = Date.now();

if (!staticData.lastRun) {
  staticData.lastRun = now;
  staticData.runCount = 1;
} else {
  const timeSinceLastRun = now - staticData.lastRun;

  if (timeSinceLastRun < 60000) {  // Less than 1 minute
    return [{json: {error: 'Rate limit: wait 1 minute between runs'}}];
  }

  staticData.lastRun = now;
  staticData.runCount++;
}

return [{json: {allowed: true, totalRuns: staticData.runCount}}];
```

```javascript
// Use Case 2: Tracking last processed ID
const staticData = $getWorkflowStaticData();
const currentItems = $input.all();

// Get last processed ID
const lastId = staticData.lastProcessedId || 0;

// Filter only new items
const newItems = currentItems.filter(item => item.json.id > lastId);

// Update last processed ID
if (newItems.length > 0) {
  staticData.lastProcessedId = Math.max(...newItems.map(item => item.json.id));
}

return newItems;
```

```javascript
// Use Case 3: Accumulating results
const staticData = $getWorkflowStaticData();

if (!staticData.accumulated) {
  staticData.accumulated = [];
}

// Add current items to accumulated list
const currentData = $input.all().map(item => item.json);
staticData.accumulated.push(...currentData);

return [{
  json: {
    currentBatch: currentData.length,
    totalAccumulated: staticData.accumulated.length,
    allData: staticData.accumulated
  }
}];
```

---

## 5. Standard JavaScript Globals

### Math Object

```javascript
return [{
  json: {
    // Rounding
    rounded: Math.round(3.7),  // 4
    floor: Math.floor(3.7),  // 3
    ceil: Math.ceil(3.2),  // 4

    // Min/Max
    max: Math.max(1, 5, 3, 9, 2),  // 9
    min: Math.min(1, 5, 3, 9, 2),  // 1

    // Random
    random: Math.random(),  // 0-1
    randomInt: Math.floor(Math.random() * 100),  // 0-99

    // Other
    abs: Math.abs(-5),  // 5
    sqrt: Math.sqrt(16),  // 4
    pow: Math.pow(2, 3)  // 8
  }
}];
```

### JSON Object

```javascript
// Parse JSON string
const jsonString = '{"name": "John", "age": 30}';
const parsed = JSON.parse(jsonString);

// Stringify object
const obj = {name: "John", age: 30};
const stringified = JSON.stringify(obj);

// Pretty print
const pretty = JSON.stringify(obj, null, 2);

return [{json: {parsed, stringified, pretty}}];
```

### console Object

```javascript
// Debug logging (appears in browser console, press F12)
console.log('Processing items:', $input.all().length);
console.log('First item:', $input.first().json);

// Other console methods
console.error('Error message');
console.warn('Warning message');
console.info('Info message');

// Continues to return data
return [{json: {processed: true}}];
```

### Object Methods

```javascript
const obj = {name: "John", age: 30, city: "NYC"};

return [{
  json: {
    keys: Object.keys(obj),  // ["name", "age", "city"]
    values: Object.values(obj),  // ["John", 30, "NYC"]
    entries: Object.entries(obj),  // [["name", "John"], ...]

    // Check property
    hasName: 'name' in obj,  // true

    // Merge objects
    merged: Object.assign({}, obj, {country: "USA"})
  }
}];
```

### Array Methods

```javascript
const arr = [1, 2, 3, 4, 5];

return [{
  json: {
    mapped: arr.map(x => x * 2),  // [2, 4, 6, 8, 10]
    filtered: arr.filter(x => x > 2),  // [3, 4, 5]
    reduced: arr.reduce((sum, x) => sum + x, 0),  // 15
    some: arr.some(x => x > 3),  // true
    every: arr.every(x => x > 0),  // true
    find: arr.find(x => x > 3),  // 4
    includes: arr.includes(3),  // true
    joined: arr.join(', ')  // "1, 2, 3, 4, 5"
  }
}];
```

---

## 6. Available Node.js Modules

### crypto Module

```javascript
const crypto = require('crypto');

// Hash functions
const hash = crypto.createHash('sha256')
  .update('my secret text')
  .digest('hex');

// MD5 hash
const md5 = crypto.createHash('md5')
  .update('my text')
  .digest('hex');

// Random values
const randomBytes = crypto.randomBytes(16).toString('hex');

return [{json: {hash, md5, randomBytes}}];
```

### Buffer (built-in)

```javascript
// Base64 encoding
const encoded = Buffer.from('Hello World').toString('base64');

// Base64 decoding
const decoded = Buffer.from(encoded, 'base64').toString();

// Hex encoding
const hex = Buffer.from('Hello').toString('hex');

return [{json: {encoded, decoded, hex}}];
```

### URL / URLSearchParams

```javascript
// Parse URL
const url = new URL('https://example.com/path?param1=value1&param2=value2');

// Build query string
const params = new URLSearchParams({
  search: 'query',
  page: 1,
  limit: 10
});

return [{
  json: {
    host: url.host,
    pathname: url.pathname,
    search: url.search,
    queryString: params.toString()  // "search=query&page=1&limit=10"
  }
}];
```

---

## What's NOT Available

**External npm packages are NOT available:**
- ❌ axios
- ❌ lodash
- ❌ moment (use DateTime/Luxon instead)
- ❌ request
- ❌ Any other npm package

**Workaround**: Use $helpers.httpRequest() for HTTP, or add data to workflow via HTTP Request node.

---

## Summary

**Most Useful Built-ins**:
1. **$helpers.httpRequest()** - API calls without HTTP Request node
2. **DateTime** - Professional date/time handling
3. **$jmespath()** - Complex JSON queries
4. **Math, JSON, Object, Array** - Standard JavaScript utilities

**Common Patterns**:
- API calls: Use $helpers.httpRequest()
- Date operations: Use DateTime (Luxon)
- Data filtering: Use $jmespath() or JavaScript .filter()
- Persistent data: Use $getWorkflowStaticData()
- Hashing: Use crypto module

**See Also**:
- [SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) - Overview
- [COMMON_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/frontend_dev_guidelines/resources/common_patterns.md) - Real usage examples
- [ERROR_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/render_deploy/references/error_patterns.md) - Error prevention
```

## File: `skills/n8n-code-javascript/COMMON_PATTERNS.md`
```markdown
# Common Patterns - JavaScript Code Node

Production-tested patterns for n8n Code nodes. These patterns are proven in real workflows.

---

## Overview

This guide covers the 10 most useful Code node patterns for n8n workflows. Each pattern includes:
- **Use Case**: When to use this pattern
- **Key Techniques**: Important coding techniques demonstrated
- **Complete Example**: Working code you can adapt
- **Variations**: Common modifications

**Pattern Categories:**
- Data Aggregation (Patterns 1, 5, 10)
- Content Processing (Patterns 2, 3)
- Data Validation & Comparison (Patterns 4)
- Data Transformation (Patterns 5, 6, 7)
- Output Formatting (Pattern 8)
- Filtering & Ranking (Pattern 9)

---

## Pattern 1: Multi-Source Data Aggregation

**Use Case**: Combining data from multiple APIs, RSS feeds, webhooks, or databases

**When to use:**
- Collecting data from multiple services
- Normalizing different API response formats
- Merging data sources into unified structure
- Building aggregated reports

**Key Techniques**: Loop iteration, conditional parsing, data normalization

### Complete Example

```javascript
// Process and structure data collected from multiple sources
const allItems = $input.all();
let processedArticles = [];

// Handle different source formats
for (const item of allItems) {
  const sourceName = item.json.name || 'Unknown';
  const sourceData = item.json;

  // Parse source-specific structure - Hacker News format
  if (sourceName === 'Hacker News' && sourceData.hits) {
    for (const hit of sourceData.hits) {
      processedArticles.push({
        title: hit.title,
        url: hit.url,
        summary: hit.story_text || 'No summary',
        source: 'Hacker News',
        score: hit.points || 0,
        fetchedAt: new Date().toISOString()
      });
    }
  }

  // Parse source-specific structure - Reddit format
  else if (sourceName === 'Reddit' && sourceData.data?.children) {
    for (const post of sourceData.data.children) {
      processedArticles.push({
        title: post.data.title,
        url: post.data.url,
        summary: post.data.selftext || 'No summary',
        source: 'Reddit',
        score: post.data.score || 0,
        fetchedAt: new Date().toISOString()
      });
    }
  }

  // Parse source-specific structure - RSS feed format
  else if (sourceName === 'RSS' && sourceData.items) {
    for (const rssItem of sourceData.items) {
      processedArticles.push({
        title: rssItem.title,
        url: rssItem.link,
        summary: rssItem.description || 'No summary',
        source: 'RSS Feed',
        score: 0,
        fetchedAt: new Date().toISOString()
      });
    }
  }
}

// Sort by score (highest first)
processedArticles.sort((a, b) => b.score - a.score);

return processedArticles.map(article => ({json: article}));
```

### Variations

```javascript
// Variation 1: Add source weighting
for (const article of processedArticles) {
  const weights = {
    'Hacker News': 1.5,
    'Reddit': 1.0,
    'RSS Feed': 0.8
  };

  article.weightedScore = article.score * (weights[article.source] || 1.0);
}

// Variation 2: Filter by minimum score
processedArticles = processedArticles.filter(article => article.score >= 10);

// Variation 3: Deduplicate by URL
const seen = new Set();
processedArticles = processedArticles.filter(article => {
  if (seen.has(article.url)) {
    return false;
  }
  seen.add(article.url);
  return true;
});
```

---

## Pattern 2: Regex Filtering & Pattern Matching

**Use Case**: Content analysis, keyword extraction, mention tracking, text parsing

**When to use:**
- Extracting mentions or tags from text
- Finding patterns in unstructured data
- Counting keyword occurrences
- Validating formats (emails, phone numbers)

**Key Techniques**: Regex matching, object aggregation, sorting/ranking

### Complete Example

```javascript
// Extract and track mentions using regex patterns
const etfPattern = /\b([A-Z]{2,5})\b/g;
const knownETFs = ['VOO', 'VTI', 'VT', 'SCHD', 'QYLD', 'VXUS', 'SPY', 'QQQ'];

const etfMentions = {};

for (const item of $input.all()) {
  const data = item.json.data;

  // Skip if no data or children
  if (!data?.children) continue;

  for (const post of data.children) {
    // Combine title and body text
    const title = post.data.title || '';
    const body = post.data.selftext || '';
    const combinedText = (title + ' ' + body).toUpperCase();

    // Find all matches
    const matches = combinedText.match(etfPattern);

    if (matches) {
      for (const match of matches) {
        // Only count known ETFs
        if (knownETFs.includes(match)) {
          if (!etfMentions[match]) {
            etfMentions[match] = {
              count: 0,
              totalScore: 0,
              posts: []
            };
          }

          etfMentions[match].count++;
          etfMentions[match].totalScore += post.data.score || 0;
          etfMentions[match].posts.push({
            title: post.data.title,
            url: post.data.url,
            score: post.data.score
          });
        }
      }
    }
  }
}

// Convert to array and sort by mention count
return Object.entries(etfMentions)
  .map(([etf, data]) => ({
    json: {
      etf,
      mentions: data.count,
      totalScore: data.totalScore,
      averageScore: data.totalScore / data.count,
      topPosts: data.posts
        .sort((a, b) => b.score - a.score)
        .slice(0, 3)
    }
  }))
  .sort((a, b) => b.json.mentions - a.json.mentions);
```

### Variations

```javascript
// Variation 1: Email extraction
const emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g;
const emails = text.match(emailPattern) || [];

// Variation 2: Phone number extraction
const phonePattern = /\b\d{3}[-.]?\d{3}[-.]?\d{4}\b/g;
const phones = text.match(phonePattern) || [];

// Variation 3: Hashtag extraction
const hashtagPattern = /#(\w+)/g;
const hashtags = [];
let match;
while ((match = hashtagPattern.exec(text)) !== null) {
  hashtags.push(match[1]);
}

// Variation 4: URL extraction
const urlPattern = /https?:\/\/[^\s]+/g;
const urls = text.match(urlPattern) || [];
```

---

## Pattern 3: Markdown Parsing & Structured Data Extraction

**Use Case**: Parsing formatted text, extracting structured fields, content transformation

**When to use:**
- Parsing markdown or HTML
- Extracting data from structured text
- Converting formatted content to JSON
- Processing documentation or articles

**Key Techniques**: Regex grouping, helper functions, data normalization, while loops for iteration

### Complete Example

```javascript
// Parse markdown and extract structured information
const markdown = $input.first().json.data.markdown;
const adRegex = /##\s*(.*?)\n(.*?)(?=\n##|\n---|$)/gs;

const ads = [];
let match;

// Helper function to parse time strings to minutes
function parseTimeToMinutes(timeStr) {
  if (!timeStr) return 999999;  // Sort unparseable times last

  const hourMatch = timeStr.match(/(\d+)\s*hour/);
  const dayMatch = timeStr.match(/(\d+)\s*day/);
  const minMatch = timeStr.match(/(\d+)\s*min/);

  let totalMinutes = 0;
  if (dayMatch) totalMinutes += parseInt(dayMatch[1]) * 1440;  // 24 * 60
  if (hourMatch) totalMinutes += parseInt(hourMatch[1]) * 60;
  if (minMatch) totalMinutes += parseInt(minMatch[1]);

  return totalMinutes;
}

// Extract all job postings from markdown
while ((match = adRegex.exec(markdown)) !== null) {
  const title = match[1]?.trim() || 'No title';
  const content = match[2]?.trim() || '';

  // Extract structured fields from content
  const districtMatch = content.match(/\*\*District:\*\*\s*(.*?)(?:\n|$)/);
  const salaryMatch = content.match(/\*\*Salary:\*\*\s*(.*?)(?:\n|$)/);
  const timeMatch = content.match(/Posted:\s*(.*?)\*/);

  ads.push({
    title: title,
    district: districtMatch?.[1].trim() || 'Unknown',
    salary: salaryMatch?.[1].trim() || 'Not specified',
    postedTimeAgo: timeMatch?.[1] || 'Unknown',
    timeInMinutes: parseTimeToMinutes(timeMatch?.[1]),
    fullContent: content,
    extractedAt: new Date().toISOString()
  });
}

// Sort by recency (posted time)
ads.sort((a, b) => a.timeInMinutes - b.timeInMinutes);

return ads.map(ad => ({json: ad}));
```

### Variations

```javascript
// Variation 1: Parse HTML table to JSON
const tableRegex = /<tr>(.*?)<\/tr>/gs;
const cellRegex = /<td>(.*?)<\/td>/g;

const rows = [];
let tableMatch;

while ((tableMatch = tableRegex.exec(htmlTable)) !== null) {
  const cells = [];
  let cellMatch;

  while ((cellMatch = cellRegex.exec(tableMatch[1])) !== null) {
    cells.push(cellMatch[1].trim());
  }

  if (cells.length > 0) {
    rows.push(cells);
  }
}

// Variation 2: Extract code blocks from markdown
const codeBlockRegex = /```(\w+)?\n(.*?)```/gs;
const codeBlocks = [];

while ((match = codeBlockRegex.exec(markdown)) !== null) {
  codeBlocks.push({
    language: match[1] || 'plain',
    code: match[2].trim()
  });
}

// Variation 3: Parse YAML frontmatter
const frontmatterRegex = /^---\n(.*?)\n---/s;
const frontmatterMatch = content.match(frontmatterRegex);

if (frontmatterMatch) {
  const yamlLines = frontmatterMatch[1].split('\n');
  const metadata = {};

  for (const line of yamlLines) {
    const [key, ...valueParts] = line.split(':');
    if (key && valueParts.length > 0) {
      metadata[key.trim()] = valueParts.join(':').trim();
    }
  }
}
```

---

## Pattern 4: JSON Comparison & Validation

**Use Case**: Workflow versioning, configuration validation, change detection, data integrity

**When to use:**
- Comparing two versions of data
- Detecting changes in configurations
- Validating data consistency
- Checking for differences

**Key Techniques**: JSON ordering, base64 decoding, deep comparison, object manipulation

### Complete Example

```javascript
// Compare and validate JSON objects from different sources
const orderJsonKeys = (jsonObj) => {
  const ordered = {};
  Object.keys(jsonObj).sort().forEach(key => {
    ordered[key] = jsonObj[key];
  });
  return ordered;
};

const allItems = $input.all();

// Assume first item is base64-encoded original, second is current
const origWorkflow = JSON.parse(
  Buffer.from(allItems[0].json.content, 'base64').toString()
);
const currentWorkflow = allItems[1].json;

// Order keys for consistent comparison
const orderedOriginal = orderJsonKeys(origWorkflow);
const orderedCurrent = orderJsonKeys(currentWorkflow);

// Deep comparison
const isSame = JSON.stringify(orderedOriginal) === JSON.stringify(orderedCurrent);

// Find differences
const differences = [];
for (const key of Object.keys(orderedOriginal)) {
  if (JSON.stringify(orderedOriginal[key]) !== JSON.stringify(orderedCurrent[key])) {
    differences.push({
      field: key,
      original: orderedOriginal[key],
      current: orderedCurrent[key]
    });
  }
}

// Check for new keys
for (const key of Object.keys(orderedCurrent)) {
  if (!(key in orderedOriginal)) {
    differences.push({
      field: key,
      original: null,
      current: orderedCurrent[key],
      status: 'new'
    });
  }
}

return [{
  json: {
    identical: isSame,
    differenceCount: differences.length,
    differences: differences,
    original: orderedOriginal,
    current: orderedCurrent,
    comparedAt: new Date().toISOString()
  }
}];
```

### Variations

```javascript
// Variation 1: Simple equality check
const isEqual = JSON.stringify(obj1) === JSON.stringify(obj2);

// Variation 2: Deep diff with detailed changes
function deepDiff(obj1, obj2, path = '') {
  const changes = [];

  for (const key in obj1) {
    const currentPath = path ? `${path}.${key}` : key;

    if (!(key in obj2)) {
      changes.push({type: 'removed', path: currentPath, value: obj1[key]});
    } else if (typeof obj1[key] === 'object' && typeof obj2[key] === 'object') {
      changes.push(...deepDiff(obj1[key], obj2[key], currentPath));
    } else if (obj1[key] !== obj2[key]) {
      changes.push({
        type: 'modified',
        path: currentPath,
        from: obj1[key],
        to: obj2[key]
      });
    }
  }

  for (const key in obj2) {
    if (!(key in obj1)) {
      const currentPath = path ? `${path}.${key}` : key;
      changes.push({type: 'added', path: currentPath, value: obj2[key]});
    }
  }

  return changes;
}

// Variation 3: Schema validation
function validateSchema(data, schema) {
  const errors = [];

  for (const field of schema.required || []) {
    if (!(field in data)) {
      errors.push(`Missing required field: ${field}`);
    }
  }

  for (const [field, type] of Object.entries(schema.types || {})) {
    if (field in data && typeof data[field] !== type) {
      errors.push(`Field ${field} should be ${type}, got ${typeof data[field]}`);
    }
  }

  return {
    valid: errors.length === 0,
    errors
  };
}
```

---

## Pattern 5: CRM Data Transformation

**Use Case**: Lead enrichment, data normalization, API preparation, form data processing

**When to use:**
- Processing form submissions
- Preparing data for CRM APIs
- Normalizing contact information
- Enriching lead data

**Key Techniques**: Object destructuring, data mapping, format conversion, field splitting

### Complete Example

```javascript
// Transform form data into CRM-compatible format
const item = $input.all()[0];
const {
  name,
  email,
  phone,
  company,
  course_interest,
  message,
  timestamp
} = item.json;

// Split name into first and last
const nameParts = name.split(' ');
const firstName = nameParts[0] || '';
const lastName = nameParts.slice(1).join(' ') || 'Unknown';

// Format phone number
const cleanPhone = phone.replace(/[^\d]/g, '');  // Remove non-digits

// Build CRM data structure
const crmData = {
  data: {
    type: 'Contact',
    attributes: {
      first_name: firstName,
      last_name: lastName,
      email1: email,
      phone_work: cleanPhone,
      account_name: company,
      description: `Course Interest: ${course_interest}\n\nMessage: ${message}\n\nSubmitted: ${timestamp}`,
      lead_source: 'Website Form',
      status: 'New'
    }
  },
  metadata: {
    original_submission: timestamp,
    processed_at: new Date().toISOString()
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

### Variations

```javascript
// Variation 1: Multiple contact processing
const contacts = $input.all();

return contacts.map(item => {
  const data = item.json;
  const [firstName, ...lastNameParts] = data.name.split(' ');

  return {
    json: {
      firstName,
      lastName: lastNameParts.join(' ') || 'Unknown',
      email: data.email.toLowerCase(),
      phone: data.phone.replace(/[^\d]/g, ''),
      tags: [data.source, data.interest_level].filter(Boolean)
    }
  };
});

// Variation 2: Field validation and normalization
function normalizePContact(raw) {
  return {
    first_name: raw.firstName?.trim() || '',
    last_name: raw.lastName?.trim() || 'Unknown',
    email: raw.email?.toLowerCase().trim() || '',
    phone: raw.phone?.replace(/[^\d]/g, '') || '',
    company: raw.company?.trim() || 'Unknown',
    title: raw.title?.trim() || '',
    valid: Boolean(raw.email && raw.firstName)
  };
}

// Variation 3: Lead scoring
function calculateLeadScore(data) {
  let score = 0;

  if (data.email) score += 10;
  if (data.phone) score += 10;
  if (data.company) score += 15;
  if (data.title?.toLowerCase().includes('director')) score += 20;
  if (data.title?.toLowerCase().includes('manager')) score += 15;
  if (data.message?.length > 100) score += 10;

  return score;
}
```

---

## Pattern 6: Release Information Processing

**Use Case**: Version management, changelog parsing, release notes generation, GitHub API processing

**When to use:**
- Processing GitHub releases
- Filtering stable versions
- Generating changelog summaries
- Extracting version information

**Key Techniques**: Array filtering, conditional field extraction, date formatting, string manipulation

### Complete Example

```javascript
// Extract and filter stable releases from GitHub API
const allReleases = $input.first().json;

const stableReleases = allReleases
  .filter(release => !release.prerelease && !release.draft)
  .slice(0, 10)
  .map(release => {
    // Extract highlights section from changelog
    const body = release.body || '';
    let highlights = 'No highlights available';

    if (body.includes('## Highlights:')) {
      highlights = body.split('## Highlights:')[1]?.split('##')[0]?.trim();
    } else {
      // Fallback to first 500 chars
      highlights = body.substring(0, 500) + '...';
    }

    return {
      tag: release.tag_name,
      name: release.name,
      published: release.published_at,
      publishedDate: new Date(release.published_at).toLocaleDateString(),
      author: release.author.login,
      url: release.html_url,
      changelog: body,
      highlights: highlights,
      assetCount: release.assets.length,
      assets: release.assets.map(asset => ({
        name: asset.name,
        size: asset.size,
        downloadCount: asset.download_count,
        downloadUrl: asset.browser_download_url
      }))
    };
  });

return stableReleases.map(release => ({json: release}));
```

### Variations

```javascript
// Variation 1: Version comparison
function compareVersions(v1, v2) {
  const parts1 = v1.replace('v', '').split('.').map(Number);
  const parts2 = v2.replace('v', '').split('.').map(Number);

  for (let i = 0; i < Math.max(parts1.length, parts2.length); i++) {
    const num1 = parts1[i] || 0;
    const num2 = parts2[i] || 0;

    if (num1 > num2) return 1;
    if (num1 < num2) return -1;
  }

  return 0;
}

// Variation 2: Breaking change detection
function hasBreakingChanges(changelog) {
  const breakingKeywords = [
    'BREAKING CHANGE',
    'breaking change',
    'BC:',
    '💥'
  ];

  return breakingKeywords.some(keyword => changelog.includes(keyword));
}

// Variation 3: Extract version numbers
const versionPattern = /v?(\d+)\.(\d+)\.(\d+)/;
const match = tagName.match(versionPattern);

if (match) {
  const [_, major, minor, patch] = match;
  const version = {major: parseInt(major), minor: parseInt(minor), patch: parseInt(patch)};
}
```

---

## Pattern 7: Array Transformation with Context

**Use Case**: Quick data transformation, field mapping, adding computed fields

**When to use:**
- Transforming arrays with additional context
- Adding calculated fields
- Simplifying complex objects
- Pluralization logic

**Key Techniques**: Array methods chaining, ternary operators, computed properties

### Complete Example

```javascript
// Transform releases with contextual information
const releases = $input.first().json
  .filter(release => !release.prerelease && !release.draft)
  .slice(0, 10)
  .map(release => ({
    version: release.tag_name,
    assetCount: release.assets.length,
    assetsCountText: release.assets.length === 1 ? 'file' : 'files',
    downloadUrl: release.html_url,
    isRecent: new Date(release.published_at) > new Date(Date.now() - 30 * 24 * 60 * 60 * 1000),
    age: Math.floor((Date.now() - new Date(release.published_at)) / (24 * 60 * 60 * 1000)),
    ageText: `${Math.floor((Date.now() - new Date(release.published_at)) / (24 * 60 * 60 * 1000))} days ago`
  }));

return releases.map(release => ({json: release}));
```

### Variations

```javascript
// Variation 1: Add ranking
const items = $input.all()
  .sort((a, b) => b.json.score - a.json.score)
  .map((item, index) => ({
    json: {
      ...item.json,
      rank: index + 1,
      medal: index < 3 ? ['🥇', '🥈', '🥉'][index] : ''
    }
  }));

// Variation 2: Add percentage calculations
const total = $input.all().reduce((sum, item) => sum + item.json.value, 0);

const itemsWithPercentage = $input.all().map(item => ({
  json: {
    ...item.json,
    percentage: ((item.json.value / total) * 100).toFixed(2) + '%'
  }
}));

// Variation 3: Add category labels
const categorize = (value) => {
  if (value > 100) return 'High';
  if (value > 50) return 'Medium';
  return 'Low';
};

const categorized = $input.all().map(item => ({
  json: {
    ...item.json,
    category: categorize(item.json.value)
  }
}));
```

---

## Pattern 8: Slack Block Kit Formatting

**Use Case**: Chat notifications, rich message formatting, interactive messages

**When to use:**
- Sending formatted Slack messages
- Creating interactive notifications
- Building rich content for chat platforms
- Status reports and alerts

**Key Techniques**: Template literals, nested objects, Block Kit syntax, date formatting

### Complete Example

```javascript
// Create Slack-formatted message with structured blocks
const date = new Date().toISOString().split('T')[0];
const data = $input.first().json;

return [{
  json: {
    text: `Daily Report - ${date}`,  // Fallback text
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
          text: `*Status:* ${data.status === 'ok' ? '✅ All Clear' : '⚠️ Issues Detected'}\n*Alerts:* ${data.alertCount || 0}\n*Updated:* ${new Date().toLocaleString()}`
        }
      },
      {
        type: "divider"
      },
      {
        type: "section",
        fields: [
          {
            type: "mrkdwn",
            text: `*Failed Logins:*\n${data.failedLogins || 0}`
          },
          {
            type: "mrkdwn",
            text: `*API Errors:*\n${data.apiErrors || 0}`
          },
          {
            type: "mrkdwn",
            text: `*Uptime:*\n${data.uptime || '100%'}`
          },
          {
            type: "mrkdwn",
            text: `*Response Time:*\n${data.avgResponseTime || 'N/A'}ms`
          }
        ]
      },
      {
        type: "context",
        elements: [{
          type: "mrkdwn",
          text: `Report generated automatically by n8n workflow`
        }]
      }
    ]
  }
}];
```

### Variations

```javascript
// Variation 1: Interactive buttons
const blocksWithButtons = [
  {
    type: "section",
    text: {
      type: "mrkdwn",
      text: "Would you like to approve this request?"
    },
    accessory: {
      type: "button",
      text: {
        type: "plain_text",
        text: "Approve"
      },
      style: "primary",
      value: "approve",
      action_id: "approve_button"
    }
  }
];

// Variation 2: List formatting
const items = ['Item 1', 'Item 2', 'Item 3'];
const formattedList = items.map((item, i) => `${i + 1}. ${item}`).join('\n');

// Variation 3: Status indicators
function getStatusEmoji(status) {
  const statusMap = {
    'success': '✅',
    'warning': '⚠️',
    'error': '❌',
    'info': 'ℹ️'
  };

  return statusMap[status] || '•';
}

// Variation 4: Truncate long messages
function truncate(text, maxLength = 3000) {
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength - 3) + '...';
}
```

---

## Pattern 9: Top N Filtering & Ranking

**Use Case**: RAG pipelines, ranking algorithms, result filtering, leaderboards

**When to use:**
- Getting top results by score
- Filtering best/worst performers
- Building leaderboards
- Relevance ranking

**Key Techniques**: Sorting, slicing, null coalescing, score calculations

### Complete Example

```javascript
// Filter and rank by similarity score, return top results
const ragResponse = $input.item.json;
const chunks = ragResponse.chunks || [];

// Sort by similarity (highest first)
const topChunks = chunks
  .sort((a, b) => (b.similarity || 0) - (a.similarity || 0))
  .slice(0, 6);

return [{
  json: {
    query: ragResponse.query,
    topChunks: topChunks,
    count: topChunks.length,
    maxSimilarity: topChunks[0]?.similarity || 0,
    minSimilarity: topChunks[topChunks.length - 1]?.similarity || 0,
    averageSimilarity: topChunks.reduce((sum, chunk) => sum + (chunk.similarity || 0), 0) / topChunks.length
  }
}];
```

### Variations

```javascript
// Variation 1: Top N with minimum threshold
const threshold = 0.7;
const topItems = $input.all()
  .filter(item => item.json.score >= threshold)
  .sort((a, b) => b.json.score - a.json.score)
  .slice(0, 10);

// Variation 2: Bottom N (worst performers)
const bottomItems = $input.all()
  .sort((a, b) => a.json.score - b.json.score)  // Ascending
  .slice(0, 5);

// Variation 3: Top N by multiple criteria
const ranked = $input.all()
  .map(item => ({
    ...item,
    compositeScore: (item.json.relevance * 0.6) + (item.json.recency * 0.4)
  }))
  .sort((a, b) => b.compositeScore - a.compositeScore)
  .slice(0, 10);

// Variation 4: Percentile filtering
const allScores = $input.all().map(item => item.json.score).sort((a, b) => b - a);
const percentile95 = allScores[Math.floor(allScores.length * 0.05)];

const topPercentile = $input.all().filter(item => item.json.score >= percentile95);
```

---

## Pattern 10: String Aggregation & Reporting

**Use Case**: Report generation, log aggregation, content concatenation, summary creation

**When to use:**
- Combining multiple text outputs
- Generating reports from data
- Aggregating logs or messages
- Creating formatted summaries

**Key Techniques**: Array joining, string concatenation, template literals, timestamp handling

### Complete Example

```javascript
// Aggregate multiple text inputs into formatted report
const allItems = $input.all();

// Collect all messages
const messages = allItems.map(item => item.json.message);

// Build report
const header = `🎯 **Daily Summary Report**\n📅 ${new Date().toLocaleString()}\n📊 Total Items: ${messages.length}\n\n`;
const divider = '\n\n---\n\n';
const footer = `\n\n---\n\n✅ Report generated at ${new Date().toISOString()}`;

const finalReport = header + messages.join(divider) + footer;

return [{
  json: {
    report: finalReport,
    messageCount: messages.length,
    generatedAt: new Date().toISOString(),
    reportLength: finalReport.length
  }
}];
```

### Variations

```javascript
// Variation 1: Numbered list
const numberedReport = allItems
  .map((item, index) => `${index + 1}. ${item.json.title}\n   ${item.json.description}`)
  .join('\n\n');

// Variation 2: Markdown table
const headers = '| Name | Status | Score |\n|------|--------|-------|\n';
const rows = allItems
  .map(item => `| ${item.json.name} | ${item.json.status} | ${item.json.score} |`)
  .join('\n');

const table = headers + rows;

// Variation 3: HTML report
const htmlReport = `
<!DOCTYPE html>
<html>
<head><title>Report</title></head>
<body>
  <h1>Report - ${new Date().toLocaleDateString()}</h1>
  <ul>
    ${allItems.map(item => `<li>${item.json.title}: ${item.json.value}</li>`).join('\n    ')}
  </ul>
</body>
</html>
`;

// Variation 4: JSON summary
const summary = {
  generated: new Date().toISOString(),
  totalItems: allItems.length,
  items: allItems.map(item => item.json),
  statistics: {
    total: allItems.reduce((sum, item) => sum + (item.json.value || 0), 0),
    average: allItems.reduce((sum, item) => sum + (item.json.value || 0), 0) / allItems.length,
    max: Math.max(...allItems.map(item => item.json.value || 0)),
    min: Math.min(...allItems.map(item => item.json.value || 0))
  }
};
```

---

## Choosing the Right Pattern

### Pattern Selection Guide

| Your Goal | Use Pattern |
|-----------|-------------|
| Combine multiple API responses | Pattern 1 (Multi-source Aggregation) |
| Extract mentions or keywords | Pattern 2 (Regex Filtering) |
| Parse formatted text | Pattern 3 (Markdown Parsing) |
| Detect changes in data | Pattern 4 (JSON Comparison) |
| Prepare form data for CRM | Pattern 5 (CRM Transformation) |
| Process GitHub releases | Pattern 6 (Release Processing) |
| Add computed fields | Pattern 7 (Array Transformation) |
| Format Slack messages | Pattern 8 (Block Kit Formatting) |
| Get top results | Pattern 9 (Top N Filtering) |
| Create text reports | Pattern 10 (String Aggregation) |

### Combining Patterns

Many real workflows combine multiple patterns:

```javascript
// Example: Multi-source aggregation + Top N filtering
const allItems = $input.all();
const aggregated = [];

// Pattern 1: Aggregate from different sources
for (const item of allItems) {
  // ... aggregation logic
  aggregated.push(normalizedItem);
}

// Pattern 9: Get top 10 by score
const top10 = aggregated
  .sort((a, b) => b.score - a.score)
  .slice(0, 10);

// Pattern 10: Generate report
const report = `Top 10 Items:\n\n${top10.map((item, i) => `${i + 1}. ${item.title} (${item.score})`).join('\n')}`;

return [{json: {report, items: top10}}];
```

---

## Summary

**Most Useful Patterns**:
1. Multi-source Aggregation - Combining data from APIs, databases
2. Top N Filtering - Rankings, leaderboards, best results
3. Data Transformation - CRM data, field mapping, enrichment

**Key Techniques Across Patterns**:
- Array methods (map, filter, reduce, sort, slice)
- Regex for pattern matching
- Object manipulation and destructuring
- Error handling with optional chaining
- Template literals for formatting

**See Also**:
- [DATA_ACCESS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/drugbank_database/references/data_access.md) - Data access methods
- [ERROR_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/render_deploy/references/error_patterns.md) - Avoid common mistakes
- [BUILTIN_FUNCTIONS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_code_javascript/BUILTIN_FUNCTIONS.md) - Built-in helpers
```

## File: `skills/n8n-code-javascript/DATA_ACCESS.md`
```markdown
# Data Access Patterns - JavaScript Code Node

Comprehensive guide to accessing data in n8n Code nodes using JavaScript.

---

## Overview

In n8n Code nodes, you access data from previous nodes using built-in variables and methods. Understanding which method to use is critical for correct workflow execution.

**Data Access Priority** (by common usage):
1. **`$input.all()`** - Most common - Batch operations, aggregations
2. **`$input.first()`** - Very common - Single item operations
3. **`$input.item`** - Common - Each Item mode only
4. **`$node["NodeName"].json`** - Specific node references
5. **`$json`** - Direct current item (legacy, use `$input` instead)

---

## Pattern 1: $input.all() - Process All Items

**Usage**: Most common pattern for batch processing

**When to use:**
- Processing multiple records
- Aggregating data (sum, count, average)
- Filtering arrays
- Transforming datasets
- Comparing items
- Sorting or ranking

### Basic Usage

```javascript
// Get all items from previous node
const allItems = $input.all();

// allItems is an array of objects like:
// [
//   {json: {id: 1, name: "Alice"}},
//   {json: {id: 2, name: "Bob"}}
// ]

console.log(`Received ${allItems.length} items`);

return allItems;
```

### Example 1: Filter Active Items

```javascript
const allItems = $input.all();

// Filter only active items
const activeItems = allItems.filter(item => item.json.status === 'active');

return activeItems;
```

### Example 2: Transform All Items

```javascript
const allItems = $input.all();

// Map to new structure
const transformed = allItems.map(item => ({
  json: {
    id: item.json.id,
    fullName: `${item.json.firstName} ${item.json.lastName}`,
    email: item.json.email,
    processedAt: new Date().toISOString()
  }
}));

return transformed;
```

### Example 3: Aggregate Data

```javascript
const allItems = $input.all();

// Calculate total
const total = allItems.reduce((sum, item) => {
  return sum + (item.json.amount || 0);
}, 0);

return [{
  json: {
    total,
    count: allItems.length,
    average: total / allItems.length
  }
}];
```

### Example 4: Sort and Limit

```javascript
const allItems = $input.all();

// Get top 5 by score
const topFive = allItems
  .sort((a, b) => (b.json.score || 0) - (a.json.score || 0))
  .slice(0, 5);

return topFive.map(item => ({json: item.json}));
```

### Example 5: Group By Category

```javascript
const allItems = $input.all();

// Group items by category
const grouped = {};

for (const item of allItems) {
  const category = item.json.category || 'Uncategorized';

  if (!grouped[category]) {
    grouped[category] = [];
  }

  grouped[category].push(item.json);
}

// Convert to array format
return Object.entries(grouped).map(([category, items]) => ({
  json: {
    category,
    items,
    count: items.length
  }
}));
```

### Example 6: Deduplicate by ID

```javascript
const allItems = $input.all();

// Remove duplicates by ID
const seen = new Set();
const unique = [];

for (const item of allItems) {
  const id = item.json.id;

  if (!seen.has(id)) {
    seen.add(id);
    unique.push(item);
  }
}

return unique;
```

---

## Pattern 2: $input.first() - Get First Item

**Usage**: Very common for single-item operations

**When to use:**
- Previous node returns single object
- Working with API responses
- Getting initial/first data point
- Configuration or metadata access

### Basic Usage

```javascript
// Get first item from previous node
const firstItem = $input.first();

// Access the JSON data
const data = firstItem.json;

console.log('First item:', data);

return [{json: data}];
```

### Example 1: Process Single API Response

```javascript
// Get API response (typically single object)
const response = $input.first().json;

// Extract what you need
return [{
  json: {
    userId: response.data.user.id,
    userName: response.data.user.name,
    status: response.status,
    fetchedAt: new Date().toISOString()
  }
}];
```

### Example 2: Transform Single Object

```javascript
const data = $input.first().json;

// Transform structure
return [{
  json: {
    id: data.id,
    contact: {
      email: data.email,
      phone: data.phone
    },
    address: {
      street: data.street,
      city: data.city,
      zip: data.zip
    }
  }
}];
```

### Example 3: Validate Single Item

```javascript
const item = $input.first().json;

// Validation logic
const isValid = item.email && item.email.includes('@');

return [{
  json: {
    ...item,
    valid: isValid,
    validatedAt: new Date().toISOString()
  }
}];
```

### Example 4: Extract Nested Data

```javascript
const response = $input.first().json;

// Navigate nested structure
const users = response.data?.users || [];

return users.map(user => ({
  json: {
    id: user.id,
    name: user.profile?.name || 'Unknown',
    email: user.contact?.email || 'no-email'
  }
}));
```

### Example 5: Combine with Other Methods

```javascript
// Get first item's data
const firstData = $input.first().json;

// Use it to filter all items
const allItems = $input.all();
const matching = allItems.filter(item =>
  item.json.category === firstData.targetCategory
);

return matching;
```

---

## Pattern 3: $input.item - Current Item (Each Item Mode)

**Usage**: Common in "Run Once for Each Item" mode

**When to use:**
- Mode is set to "Run Once for Each Item"
- Need to process items independently
- Per-item API calls or validations
- Item-specific error handling

**IMPORTANT**: Only use in "Each Item" mode. Will be undefined in "All Items" mode.

### Basic Usage

```javascript
// In "Run Once for Each Item" mode
const currentItem = $input.item;
const data = currentItem.json;

console.log('Processing item:', data.id);

return [{
  json: {
    ...data,
    processed: true
  }
}];
```

### Example 1: Add Processing Metadata

```javascript
const item = $input.item;

return [{
  json: {
    ...item.json,
    processed: true,
    processedAt: new Date().toISOString(),
    processingDuration: Math.random() * 1000  // Simulated duration
  }
}];
```

### Example 2: Per-Item Validation

```javascript
const item = $input.item;
const data = item.json;

// Validate this specific item
const errors = [];

if (!data.email) errors.push('Email required');
if (!data.name) errors.push('Name required');
if (data.age && data.age < 18) errors.push('Must be 18+');

return [{
  json: {
    ...data,
    valid: errors.length === 0,
    errors: errors.length > 0 ? errors : undefined
  }
}];
```

### Example 3: Item-Specific API Call

```javascript
const item = $input.item;
const userId = item.json.userId;

// Make API call specific to this item
const response = await $helpers.httpRequest({
  method: 'GET',
  url: `https://api.example.com/users/${userId}/details`
});

return [{
  json: {
    ...item.json,
    details: response
  }
}];
```

### Example 4: Conditional Processing

```javascript
const item = $input.item;
const data = item.json;

// Process based on item type
if (data.type === 'premium') {
  return [{
    json: {
      ...data,
      discount: 0.20,
      tier: 'premium'
    }
  }];
} else {
  return [{
    json: {
      ...data,
      discount: 0.05,
      tier: 'standard'
    }
  }];
}
```

---

## Pattern 4: $node - Reference Other Nodes

**Usage**: Less common, but powerful for specific scenarios

**When to use:**
- Need data from specific named node
- Combining data from multiple nodes
- Accessing metadata about workflow execution

### Basic Usage

```javascript
// Get output from specific node
const webhookData = $node["Webhook"].json;
const apiData = $node["HTTP Request"].json;

return [{
  json: {
    fromWebhook: webhookData,
    fromAPI: apiData
  }
}];
```

### Example 1: Combine Multiple Sources

```javascript
// Reference multiple nodes
const webhook = $node["Webhook"].json;
const database = $node["Postgres"].json;
const api = $node["HTTP Request"].json;

return [{
  json: {
    combined: {
      webhook: webhook.body,
      dbRecords: database.length,
      apiResponse: api.status
    },
    processedAt: new Date().toISOString()
  }
}];
```

### Example 2: Compare Across Nodes

```javascript
const oldData = $node["Get Old Data"].json;
const newData = $node["Get New Data"].json;

// Compare
const changes = {
  added: newData.filter(n => !oldData.find(o => o.id === n.id)),
  removed: oldData.filter(o => !newData.find(n => n.id === o.id)),
  modified: newData.filter(n => {
    const old = oldData.find(o => o.id === n.id);
    return old && JSON.stringify(old) !== JSON.stringify(n);
  })
};

return [{
  json: {
    changes,
    summary: {
      added: changes.added.length,
      removed: changes.removed.length,
      modified: changes.modified.length
    }
  }
}];
```

### Example 3: Access Node Metadata

```javascript
// Get data from specific execution path
const ifTrueBranch = $node["IF True"].json;
const ifFalseBranch = $node["IF False"].json;

// Use whichever branch executed
const result = ifTrueBranch || ifFalseBranch || {};

return [{json: result}];
```

---

## Critical: Webhook Data Structure

**MOST COMMON MISTAKE**: Forgetting webhook data is nested under `.body`

### The Problem

Webhook node wraps all incoming data under a `body` property. This catches many developers by surprise.

### Structure

```javascript
// Webhook node output structure:
{
  "headers": {
    "content-type": "application/json",
    "user-agent": "...",
    // ... other headers
  },
  "params": {},
  "query": {},
  "body": {
    // ← YOUR DATA IS HERE
    "name": "Alice",
    "email": "alice@example.com",
    "message": "Hello!"
  }
}
```

### Wrong vs Right

```javascript
// ❌ WRONG: Trying to access directly
const name = $json.name;  // undefined
const email = $json.email;  // undefined

// ✅ CORRECT: Access via .body
const name = $json.body.name;  // "Alice"
const email = $json.body.email;  // "alice@example.com"

// ✅ CORRECT: Extract body first
const webhookData = $json.body;
const name = webhookData.name;  // "Alice"
const email = webhookData.email;  // "alice@example.com"
```

### Example: Full Webhook Processing

```javascript
// Get webhook data from previous node
const webhookOutput = $input.first().json;

// Access the actual payload
const payload = webhookOutput.body;

// Access headers if needed
const contentType = webhookOutput.headers['content-type'];

// Access query parameters if needed
const apiKey = webhookOutput.query.api_key;

// Process the actual data
return [{
  json: {
    // Data from webhook body
    userName: payload.name,
    userEmail: payload.email,
    message: payload.message,

    // Metadata
    receivedAt: new Date().toISOString(),
    contentType: contentType,
    authenticated: !!apiKey
  }
}];
```

### POST Data, Query Params, and Headers

```javascript
const webhook = $input.first().json;

return [{
  json: {
    // POST body data
    formData: webhook.body,

    // Query parameters (?key=value)
    queryParams: webhook.query,

    // HTTP headers
    userAgent: webhook.headers['user-agent'],
    contentType: webhook.headers['content-type'],

    // Request metadata
    method: webhook.method,  // POST, GET, etc.
    url: webhook.url
  }
}];
```

### Common Webhook Scenarios

```javascript
// Scenario 1: Form submission
const formData = $json.body;
const name = formData.name;
const email = formData.email;

// Scenario 2: JSON API webhook
const apiPayload = $json.body;
const eventType = apiPayload.event;
const data = apiPayload.data;

// Scenario 3: Query parameters
const apiKey = $json.query.api_key;
const userId = $json.query.user_id;

// Scenario 4: Headers
const authorization = $json.headers['authorization'];
const signature = $json.headers['x-signature'];
```

---

## Choosing the Right Pattern

### Decision Tree

```
Do you need ALL items from previous node?
├─ YES → Use $input.all()
│
└─ NO → Do you need just the FIRST item?
    ├─ YES → Use $input.first()
    │
    └─ NO → Are you in "Each Item" mode?
        ├─ YES → Use $input.item
        │
        └─ NO → Do you need specific node data?
            ├─ YES → Use $node["NodeName"]
            └─ NO → Use $input.first() (default)
```

### Quick Reference Table

| Scenario | Use This | Example |
|----------|----------|---------|
| Sum all amounts | `$input.all()` | `allItems.reduce((sum, i) => sum + i.json.amount, 0)` |
| Get API response | `$input.first()` | `$input.first().json.data` |
| Process each independently | `$input.item` | `$input.item.json` (Each Item mode) |
| Combine two nodes | `$node["Name"]` | `$node["API"].json` |
| Filter array | `$input.all()` | `allItems.filter(i => i.json.active)` |
| Transform single object | `$input.first()` | `{...input.first().json, new: true}` |
| Webhook data | `$input.first()` | `$input.first().json.body` |

---

## Common Mistakes

### Mistake 1: Using $json Without Context

```javascript
// ❌ WRONG: $json is ambiguous
const value = $json.field;

// ✅ CORRECT: Be explicit
const value = $input.first().json.field;
```

### Mistake 2: Forgetting .json Property

```javascript
// ❌ WRONG: Trying to access fields on item object
const items = $input.all();
const names = items.map(item => item.name);  // undefined

// ✅ CORRECT: Access via .json
const names = items.map(item => item.json.name);
```

### Mistake 3: Using $input.item in All Items Mode

```javascript
// ❌ WRONG: $input.item is undefined in "All Items" mode
const data = $input.item.json;  // Error!

// ✅ CORRECT: Use appropriate method
const data = $input.first().json;  // Or $input.all()
```

### Mistake 4: Not Handling Empty Arrays

```javascript
// ❌ WRONG: Crashes if no items
const first = $input.all()[0].json;

// ✅ CORRECT: Check length first
const items = $input.all();
if (items.length === 0) {
  return [];
}
const first = items[0].json;

// ✅ ALSO CORRECT: Use $input.first()
const first = $input.first().json;  // Built-in safety
```

### Mistake 5: Modifying Original Data

```javascript
// ❌ RISKY: Mutating original
const items = $input.all();
items[0].json.modified = true;  // Modifies original
return items;

// ✅ SAFE: Create new objects
const items = $input.all();
return items.map(item => ({
  json: {
    ...item.json,
    modified: true
  }
}));
```

---

## Advanced Patterns

### Pattern: Pagination Handling

```javascript
const currentPage = $input.all();
const pageNumber = $node["Set Page"].json.page || 1;

// Combine with previous pages
const allPreviousPages = $node["Accumulator"]?.json.accumulated || [];

return [{
  json: {
    accumulated: [...allPreviousPages, ...currentPage],
    currentPage: pageNumber,
    totalItems: allPreviousPages.length + currentPage.length
  }
}];
```

### Pattern: Conditional Node Reference

```javascript
// Access different nodes based on condition
const condition = $input.first().json.type;

let data;
if (condition === 'api') {
  data = $node["API Response"].json;
} else if (condition === 'database') {
  data = $node["Database"].json;
} else {
  data = $node["Default"].json;
}

return [{json: data}];
```

### Pattern: Multi-Node Aggregation

```javascript
// Collect data from multiple named nodes
const sources = ['Source1', 'Source2', 'Source3'];
const allData = [];

for (const source of sources) {
  const nodeData = $node[source]?.json;
  if (nodeData) {
    allData.push({
      source,
      data: nodeData
    });
  }
}

return allData.map(item => ({json: item}));
```

---

## Summary

**Most Common Patterns**:
1. `$input.all()` - Process multiple items, batch operations
2. `$input.first()` - Single item, API responses
3. `$input.item` - Each Item mode processing

**Critical Rule**:
- Webhook data is under `.body` property

**Best Practice**:
- Be explicit: Use `$input.first().json.field` instead of `$json.field`
- Always check for null/undefined
- Use appropriate method for your mode (All Items vs Each Item)

**See Also**:
- [SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) - Overview and quick start
- [COMMON_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/frontend_dev_guidelines/resources/common_patterns.md) - Production patterns
- [ERROR_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/render_deploy/references/error_patterns.md) - Avoid common mistakes
```

## File: `skills/n8n-code-javascript/ERROR_PATTERNS.md`
```markdown
# Error Patterns - JavaScript Code Node

Complete guide to avoiding the most common Code node errors.

---

## Overview

This guide covers the **top 5 error patterns** encountered in n8n Code nodes. Understanding and avoiding these errors will save you significant debugging time.

**Error Frequency**:
1. Empty Code / Missing Return - **38% of failures**
2. Expression Syntax Confusion - **8% of failures**
3. Incorrect Return Wrapper - **5% of failures**
4. Unmatched Expression Brackets - **6% of failures**
5. Missing Null Checks - **Common runtime error**

---

## Error #1: Empty Code or Missing Return Statement

**Frequency**: Most common error (38% of all validation failures)

**What Happens**:
- Workflow execution fails
- Next nodes receive no data
- Error: "Code cannot be empty" or "Code must return data"

### The Problem

```javascript
// ❌ ERROR: No code at all
// (Empty code field)
```

```javascript
// ❌ ERROR: Code executes but doesn't return anything
const items = $input.all();

// Process items
for (const item of items) {
  console.log(item.json.name);
}

// Forgot to return!
```

```javascript
// ❌ ERROR: Early return path exists, but not all paths return
const items = $input.all();

if (items.length === 0) {
  return [];  // ✅ This path returns
}

// Process items
const processed = items.map(item => ({json: item.json}));

// ❌ Forgot to return processed!
```

### The Solution

```javascript
// ✅ CORRECT: Always return data
const items = $input.all();

// Process items
const processed = items.map(item => ({
  json: {
    ...item.json,
    processed: true
  }
}));

return processed;  // ✅ Return statement present
```

```javascript
// ✅ CORRECT: Return empty array if no items
const items = $input.all();

if (items.length === 0) {
  return [];  // Valid: empty array when no data
}

// Process and return
return items.map(item => ({json: item.json}));
```

```javascript
// ✅ CORRECT: All code paths return
const items = $input.all();

if (items.length === 0) {
  return [];
} else if (items.length === 1) {
  return [{json: {single: true, data: items[0].json}}];
} else {
  return items.map(item => ({json: item.json}));
}

// All paths covered
```

### Checklist

- [ ] Code field is not empty
- [ ] Return statement exists
- [ ] ALL code paths return data (if/else branches)
- [ ] Return format is correct (`[{json: {...}}]`)
- [ ] Return happens even on errors (use try-catch)

---

## Error #2: Expression Syntax Confusion

**Frequency**: 8% of validation failures

**What Happens**:
- Syntax error in code execution
- Error: "Unexpected token" or "Expression syntax is not valid in Code nodes"
- Template variables not evaluated

### The Problem

n8n has TWO distinct syntaxes:
1. **Expression syntax** `{{ }}` - Used in OTHER nodes (Set, IF, HTTP Request)
2. **JavaScript** - Used in CODE nodes (no `{{ }}`)

Many developers mistakenly use expression syntax inside Code nodes.

```javascript
// ❌ WRONG: Using n8n expression syntax in Code node
const userName = "{{ $json.name }}";
const userEmail = "{{ $json.body.email }}";

return [{
  json: {
    name: userName,
    email: userEmail
  }
}];

// Result: Literal string "{{ $json.name }}", NOT the value!
```

```javascript
// ❌ WRONG: Trying to evaluate expressions
const value = "{{ $now.toFormat('yyyy-MM-dd') }}";
```

### The Solution

```javascript
// ✅ CORRECT: Use JavaScript directly (no {{ }})
const userName = $json.name;
const userEmail = $json.body.email;

return [{
  json: {
    name: userName,
    email: userEmail
  }
}];
```

```javascript
// ✅ CORRECT: JavaScript template literals (use backticks)
const message = `Hello, ${$json.name}! Your email is ${$json.email}`;

return [{
  json: {
    greeting: message
  }
}];
```

```javascript
// ✅ CORRECT: Direct variable access
const item = $input.first().json;

return [{
  json: {
    name: item.name,
    email: item.email,
    timestamp: new Date().toISOString()  // JavaScript Date, not {{ }}
  }
}];
```

### Comparison Table

| Context | Syntax | Example |
|---------|--------|---------|
| Set node | `{{ }}` expressions | `{{ $json.name }}` |
| IF node | `{{ }}` expressions | `{{ $json.age > 18 }}` |
| HTTP Request URL | `{{ }}` expressions | `{{ $json.userId }}` |
| **Code node** | **JavaScript** | `$json.name` |
| **Code node strings** | **Template literals** | `` `Hello ${$json.name}` `` |

### Quick Fix Guide

```javascript
// WRONG → RIGHT conversions

// ❌ "{{ $json.field }}"
// ✅ $json.field

// ❌ "{{ $now }}"
// ✅ new Date().toISOString()

// ❌ "{{ $node['HTTP Request'].json.data }}"
// ✅ $node["HTTP Request"].json.data

// ❌ `{{ $json.firstName }} {{ $json.lastName }}`
// ✅ `${$json.firstName} ${$json.lastName}`
```

---

## Error #3: Incorrect Return Wrapper Format

**Frequency**: 5% of validation failures

**What Happens**:
- Error: "Return value must be an array of objects"
- Error: "Each item must have a json property"
- Next nodes receive malformed data

### The Problem

Code nodes MUST return:
- **Array** of objects
- Each object MUST have a **`json` property**

```javascript
// ❌ WRONG: Returning object instead of array
return {
  json: {
    result: 'success'
  }
};
// Missing array wrapper []
```

```javascript
// ❌ WRONG: Returning array without json wrapper
return [
  {id: 1, name: 'Alice'},
  {id: 2, name: 'Bob'}
];
// Missing json property
```

```javascript
// ❌ WRONG: Returning plain value
return "processed";
```

```javascript
// ❌ WRONG: Returning items without mapping
return $input.all();
// Works if items already have json property, but not guaranteed
```

```javascript
// ❌ WRONG: Incomplete structure
return [{data: {result: 'success'}}];
// Should be {json: {...}}, not {data: {...}}
```

### The Solution

```javascript
// ✅ CORRECT: Single result
return [{
  json: {
    result: 'success',
    timestamp: new Date().toISOString()
  }
}];
```

```javascript
// ✅ CORRECT: Multiple results
return [
  {json: {id: 1, name: 'Alice'}},
  {json: {id: 2, name: 'Bob'}},
  {json: {id: 3, name: 'Carol'}}
];
```

```javascript
// ✅ CORRECT: Transforming array
const items = $input.all();

return items.map(item => ({
  json: {
    id: item.json.id,
    name: item.json.name,
    processed: true
  }
}));
```

```javascript
// ✅ CORRECT: Empty result
return [];
// Valid when no data to return
```

```javascript
// ✅ CORRECT: Conditional returns
if (shouldProcess) {
  return [{json: {result: 'processed'}}];
} else {
  return [];
}
```

### Return Format Checklist

- [ ] Return value is an **array** `[...]`
- [ ] Each array element has **`json` property**
- [ ] Structure is `[{json: {...}}]` or `[{json: {...}}, {json: {...}}]`
- [ ] NOT `{json: {...}}` (missing array wrapper)
- [ ] NOT `[{...}]` (missing json property)

### Common Scenarios

```javascript
// Scenario 1: Single object from API
const response = $input.first().json;

// ✅ CORRECT
return [{json: response}];

// ❌ WRONG
return {json: response};


// Scenario 2: Array of objects
const users = $input.all();

// ✅ CORRECT
return users.map(user => ({json: user.json}));

// ❌ WRONG
return users;  // Risky - depends on existing structure


// Scenario 3: Computed result
const total = $input.all().reduce((sum, item) => sum + item.json.amount, 0);

// ✅ CORRECT
return [{json: {total}}];

// ❌ WRONG
return {total};


// Scenario 4: No results
// ✅ CORRECT
return [];

// ❌ WRONG
return null;
```

---

## Error #4: Unmatched Expression Brackets

**Frequency**: 6% of validation failures

**What Happens**:
- Parsing error during save
- Error: "Unmatched expression brackets"
- Code appears correct but fails validation

### The Problem

This error typically occurs when:
1. Strings contain unbalanced quotes
2. Multi-line strings with special characters
3. Template literals with nested brackets

```javascript
// ❌ WRONG: Unescaped quote in string
const message = "It's a nice day";
// Single quote breaks string
```

```javascript
// ❌ WRONG: Unbalanced brackets in regex
const pattern = /\{(\w+)\}/;  // JSON storage issue
```

```javascript
// ❌ WRONG: Multi-line string with quotes
const html = "
  <div class="container">
    <p>Hello</p>
  </div>
";
// Quote balance issues
```

### The Solution

```javascript
// ✅ CORRECT: Escape quotes
const message = "It\\'s a nice day";
// Or use different quotes
const message = "It's a nice day";  // Double quotes work
```

```javascript
// ✅ CORRECT: Escape regex properly
const pattern = /\\{(\\w+)\\}/;
```

```javascript
// ✅ CORRECT: Template literals for multi-line
const html = `
  <div class="container">
    <p>Hello</p>
  </div>
`;
// Backticks handle multi-line and quotes
```

```javascript
// ✅ CORRECT: Escape backslashes
const path = "C:\\\\Users\\\\Documents\\\\file.txt";
```

### Escaping Guide

| Character | Escape As | Example |
|-----------|-----------|---------|
| Single quote in single-quoted string | `\\'` | `'It\\'s working'` |
| Double quote in double-quoted string | `\\"` | `"She said \\"hello\\""` |
| Backslash | `\\\\` | `"C:\\\\path"` |
| Newline | `\\n` | `"Line 1\\nLine 2"` |
| Tab | `\\t` | `"Column1\\tColumn2"` |

### Best Practices

```javascript
// ✅ BEST: Use template literals for complex strings
const message = `User ${name} said: "Hello!"`;

// ✅ BEST: Use template literals for HTML
const html = `
  <div class="${className}">
    <h1>${title}</h1>
    <p>${content}</p>
  </div>
`;

// ✅ BEST: Use template literals for JSON
const jsonString = `{
  "name": "${name}",
  "email": "${email}"
}`;
```

---

## Error #5: Missing Null Checks / Undefined Access

**Frequency**: Very common runtime error

**What Happens**:
- Workflow execution stops
- Error: "Cannot read property 'X' of undefined"
- Error: "Cannot read property 'X' of null"
- Crashes on missing data

### The Problem

```javascript
// ❌ WRONG: No null check - crashes if user doesn't exist
const email = item.json.user.email;
```

```javascript
// ❌ WRONG: Assumes array has items
const firstItem = $input.all()[0].json;
```

```javascript
// ❌ WRONG: Assumes nested property exists
const city = $json.address.city;
```

```javascript
// ❌ WRONG: No validation before array operations
const names = $json.users.map(user => user.name);
```

### The Solution

```javascript
// ✅ CORRECT: Optional chaining
const email = item.json?.user?.email || 'no-email@example.com';
```

```javascript
// ✅ CORRECT: Check array length
const items = $input.all();

if (items.length === 0) {
  return [];
}

const firstItem = items[0].json;
```

```javascript
// ✅ CORRECT: Guard clauses
const data = $input.first().json;

if (!data.address) {
  return [{json: {error: 'No address provided'}}];
}

const city = data.address.city;
```

```javascript
// ✅ CORRECT: Default values
const users = $json.users || [];
const names = users.map(user => user.name || 'Unknown');
```

```javascript
// ✅ CORRECT: Try-catch for risky operations
try {
  const email = item.json.user.email.toLowerCase();
  return [{json: {email}}];
} catch (error) {
  return [{
    json: {
      error: 'Invalid user data',
      details: error.message
    }
  }];
}
```

### Safe Access Patterns

```javascript
// Pattern 1: Optional chaining (modern, recommended)
const value = data?.nested?.property?.value;

// Pattern 2: Logical OR with default
const value = data.property || 'default';

// Pattern 3: Ternary check
const value = data.property ? data.property : 'default';

// Pattern 4: Guard clause
if (!data.property) {
  return [];
}
const value = data.property;

// Pattern 5: Try-catch
try {
  const value = data.nested.property.value;
} catch (error) {
  const value = 'default';
}
```

### Webhook Data Safety

```javascript
// Webhook data requires extra safety

// ❌ RISKY: Assumes all fields exist
const name = $json.body.user.name;
const email = $json.body.user.email;

// ✅ SAFE: Check each level
const body = $json.body || {};
const user = body.user || {};
const name = user.name || 'Unknown';
const email = user.email || 'no-email';

// ✅ BETTER: Optional chaining
const name = $json.body?.user?.name || 'Unknown';
const email = $json.body?.user?.email || 'no-email';
```

### Array Safety

```javascript
// ❌ RISKY: No length check
const items = $input.all();
const firstId = items[0].json.id;

// ✅ SAFE: Check length
const items = $input.all();

if (items.length > 0) {
  const firstId = items[0].json.id;
} else {
  // Handle empty case
  return [];
}

// ✅ BETTER: Use $input.first()
const firstItem = $input.first();
const firstId = firstItem.json.id;  // Built-in safety
```

### Object Property Safety

```javascript
// ❌ RISKY: Direct access
const config = $json.settings.advanced.timeout;

// ✅ SAFE: Step by step with defaults
const settings = $json.settings || {};
const advanced = settings.advanced || {};
const timeout = advanced.timeout || 30000;

// ✅ BETTER: Optional chaining
const timeout = $json.settings?.advanced?.timeout ?? 30000;
// Note: ?? (nullish coalescing) vs || (logical OR)
```

---

## Error Prevention Checklist

Use this checklist before deploying Code nodes:

### Code Structure
- [ ] Code field is not empty
- [ ] Return statement exists
- [ ] All code paths return data

### Return Format
- [ ] Returns array: `[...]`
- [ ] Each item has `json` property: `{json: {...}}`
- [ ] Format is `[{json: {...}}]`

### Syntax
- [ ] No `{{ }}` expression syntax (use JavaScript)
- [ ] Template literals use backticks: `` `${variable}` ``
- [ ] All quotes and brackets balanced
- [ ] Strings properly escaped

### Data Safety
- [ ] Null checks for optional properties
- [ ] Array length checks before access
- [ ] Webhook data accessed via `.body`
- [ ] Try-catch for risky operations
- [ ] Default values for missing data

### Testing
- [ ] Test with empty input
- [ ] Test with missing fields
- [ ] Test with unexpected data types
- [ ] Check browser console for errors

---

## Quick Error Reference

| Error Message | Likely Cause | Fix |
|---------------|--------------|-----|
| "Code cannot be empty" | Empty code field | Add meaningful code |
| "Code must return data" | Missing return statement | Add `return [...]` |
| "Return value must be an array" | Returning object instead of array | Wrap in `[...]` |
| "Each item must have json property" | Missing `json` wrapper | Use `{json: {...}}` |
| "Unexpected token" | Expression syntax `{{ }}` in code | Remove `{{ }}`, use JavaScript |
| "Cannot read property X of undefined" | Missing null check | Use optional chaining `?.` |
| "Cannot read property X of null" | Null value access | Add guard clause or default |
| "Unmatched expression brackets" | Quote/bracket imbalance | Check string escaping |

---

## Debugging Tips

### 1. Use console.log()

```javascript
const items = $input.all();
console.log('Items count:', items.length);
console.log('First item:', items[0]);

// Check browser console (F12) for output
```

### 2. Return Intermediate Results

```javascript
// Debug by returning current state
const items = $input.all();
const processed = items.map(item => ({json: item.json}));

// Return to see what you have
return processed;
```

### 3. Try-Catch for Troubleshooting

```javascript
try {
  // Your code here
  const result = riskyOperation();
  return [{json: {result}}];
} catch (error) {
  // See what failed
  return [{
    json: {
      error: error.message,
      stack: error.stack
    }
  }];
}
```

### 4. Validate Input Structure

```javascript
const items = $input.all();

// Check what you received
console.log('Input structure:', JSON.stringify(items[0], null, 2));

// Then process
```

---

## Summary

**Top 5 Errors to Avoid**:
1. **Empty code / missing return** (38%) - Always return data
2. **Expression syntax `{{ }}`** (8%) - Use JavaScript, not expressions
3. **Wrong return format** (5%) - Always `[{json: {...}}]`
4. **Unmatched brackets** (6%) - Escape strings properly
5. **Missing null checks** - Use optional chaining `?.`

**Quick Prevention**:
- Return `[{json: {...}}]` format
- Use JavaScript, NOT `{{ }}` expressions
- Check for null/undefined before accessing
- Test with empty and invalid data
- Use browser console for debugging

**See Also**:
- [SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) - Overview and best practices
- [DATA_ACCESS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/drugbank_database/references/data_access.md) - Safe data access patterns
- [COMMON_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/frontend_dev_guidelines/resources/common_patterns.md) - Working examples
```

## File: `skills/n8n-code-javascript/README.md`
```markdown
# n8n Code JavaScript

Expert guidance for writing JavaScript code in n8n Code nodes.

---

## Purpose

Teaches how to write effective JavaScript in n8n Code nodes, avoid common errors, and use built-in functions effectively.

---

## Activates On

**Trigger keywords**:
- "javascript code node"
- "write javascript in n8n"
- "code node javascript"
- "$input syntax"
- "$json syntax"
- "$helpers.httpRequest"
- "DateTime luxon"
- "code node error"
- "webhook data code"
- "return format code node"

**Common scenarios**:
- Writing JavaScript code in Code nodes
- Troubleshooting Code node errors
- Making HTTP requests from code
- Working with dates and times
- Accessing webhook data
- Choosing between All Items and Each Item mode

---

## What You'll Learn

### Quick Start
- Mode selection (All Items vs Each Item)
- Data access patterns ($input.all(), $input.first(), $input.item)
- Correct return format: `[{json: {...}}]`
- Webhook data structure (.body nesting)
- Built-in functions overview

### Data Access Mastery
- $input.all() - Batch operations (most common)
- $input.first() - Single item operations
- $input.item - Each Item mode processing
- $node - Reference other workflow nodes
- **Critical gotcha**: Webhook data under `.body`

### Common Patterns (Production-Tested)
1. Multi-source Data Aggregation
2. Regex Filtering & Pattern Matching
3. Markdown Parsing & Structured Extraction
4. JSON Comparison & Validation
5. CRM Data Transformation
6. Release Information Processing
7. Array Transformation with Context
8. Slack Block Kit Formatting
9. Top N Filtering & Ranking
10. String Aggregation & Reporting

### Error Prevention
Top 5 errors to avoid:
1. **Empty code / missing return** (38% of failures)
2. **Expression syntax confusion** (using `{{}}` in code)
3. **Incorrect return format** (missing array wrapper or json property)
4. **Unmatched brackets** (string escaping issues)
5. **Missing null checks** (crashes on undefined)

### Built-in Functions
- **$helpers.httpRequest()** - Make HTTP requests
- **DateTime (Luxon)** - Advanced date/time operations
- **$jmespath()** - Query JSON structures
- **$getWorkflowStaticData()** - Persistent storage
- Standard JavaScript globals (Math, JSON, console)
- Available Node.js modules (crypto, Buffer, URL)

---

## File Structure

```
n8n-code-javascript/
├── SKILL.md (500 lines)
│   Overview, quick start, mode selection, best practices
│   - Mode selection guide (All Items vs Each Item)
│   - Data access patterns overview
│   - Return format requirements
│   - Critical webhook gotcha
│   - Error prevention overview
│   - Quick reference checklist
│
├── DATA_ACCESS.md (400 lines)
│   Complete data access patterns
│   - $input.all() - Most common (26% usage)
│   - $input.first() - Very common (25% usage)
│   - $input.item - Each Item mode (19% usage)
│   - $node - Reference other nodes
│   - Webhook data structure (.body nesting)
│   - Choosing the right pattern
│   - Common mistakes to avoid
│
├── COMMON_PATTERNS.md (600 lines)
│   10 production-tested patterns
│   - Pattern 1: Multi-source Aggregation
│   - Pattern 2: Regex Filtering
│   - Pattern 3: Markdown Parsing
│   - Pattern 4: JSON Comparison
│   - Pattern 5: CRM Transformation
│   - Pattern 6: Release Processing
│   - Pattern 7: Array Transformation
│   - Pattern 8: Slack Block Kit
│   - Pattern 9: Top N Filtering
│   - Pattern 10: String Aggregation
│   - Pattern selection guide
│
├── ERROR_PATTERNS.md (450 lines)
│   Top 5 errors with solutions
│   - Error #1: Empty Code / Missing Return (38%)
│   - Error #2: Expression Syntax Confusion (8%)
│   - Error #3: Incorrect Return Wrapper (5%)
│   - Error #4: Unmatched Brackets (6%)
│   - Error #5: Missing Null Checks
│   - Error prevention checklist
│   - Quick error reference
│   - Debugging tips
│
├── BUILTIN_FUNCTIONS.md (450 lines)
│   Complete built-in function reference
│   - $helpers.httpRequest() API reference
│   - DateTime (Luxon) complete guide
│   - $jmespath() JSON querying
│   - $getWorkflowStaticData() persistent storage
│   - Standard JavaScript globals
│   - Available Node.js modules
│   - What's NOT available
│
└── README.md (this file)
    Skill metadata and overview
```

**Total**: ~2,400 lines across 6 files

---

## Coverage

### Mode Selection
- **Run Once for All Items** - Recommended for 95% of use cases
- **Run Once for Each Item** - Specialized cases only
- Decision guide and performance implications

### Data Access
- Most common patterns with usage statistics
- Webhook data structure (critical .body gotcha)
- Safe access patterns with null checks
- When to use which pattern

### Error Prevention
- Top 5 errors covering 62%+ of all failures
- Clear wrong vs right examples
- Error prevention checklist
- Debugging tips and console.log usage

### Production Patterns
- 10 patterns from real workflows
- Complete working examples
- Use cases and key techniques
- Pattern selection guide

### Built-in Functions
- Complete $helpers.httpRequest() reference
- DateTime/Luxon operations (formatting, parsing, arithmetic)
- $jmespath() for JSON queries
- Persistent storage with $getWorkflowStaticData()
- Standard JavaScript and Node.js modules

---

## Critical Gotchas Highlighted

### #1: Webhook Data Structure
**MOST COMMON MISTAKE**: Webhook data is under `.body`

```javascript
// ❌ WRONG
const name = $json.name;

// ✅ CORRECT
const name = $json.body.name;
```

### #2: Return Format
**CRITICAL**: Must return array with json property

```javascript
// ❌ WRONG
return {json: {result: 'success'}};

// ✅ CORRECT
return [{json: {result: 'success'}}];
```

### #3: Expression Syntax
**Don't use `{{}}` in Code nodes**

```javascript
// ❌ WRONG
const value = "{{ $json.field }}";

// ✅ CORRECT
const value = $json.field;
```

---

## Integration with Other Skills

### n8n Expression Syntax
- **Distinction**: Expressions use `{{}}` in OTHER nodes
- **Code nodes**: Use JavaScript directly (no `{{}}`)
- **When to use each**: Code vs expressions decision guide

### n8n MCP Tools Expert
- Find Code node: `search_nodes({query: "code"})`
- Get configuration: `get_node("nodes-base.code")`
- Validate code: `validate_node()`

### n8n Node Configuration
- Mode selection (All Items vs Each Item)
- Language selection (JavaScript vs Python)
- Understanding property dependencies

### n8n Workflow Patterns
- Code nodes in transformation step
- Webhook → Code → API pattern
- Error handling in workflows

### n8n Validation Expert
- Validate Code node configuration
- Handle validation errors
- Auto-fix common issues

---

## When to Use Code Node

**Use Code node when:**
- ✅ Complex transformations requiring multiple steps
- ✅ Custom calculations or business logic
- ✅ Recursive operations
- ✅ API response parsing with complex structure
- ✅ Multi-step conditionals
- ✅ Data aggregation across items

**Consider other nodes when:**
- ❌ Simple field mapping → Use **Set** node
- ❌ Basic filtering → Use **Filter** node
- ❌ Simple conditionals → Use **IF** or **Switch** node
- ❌ HTTP requests only → Use **HTTP Request** node

**Code node excels at**: Complex logic that would require chaining many simple nodes

---

## Success Metrics

**Before this skill**:
- Users confused by mode selection
- Frequent return format errors
- Expression syntax mistakes
- Webhook data access failures
- Missing null check crashes

**After this skill**:
- Clear mode selection guidance
- Understanding of return format
- JavaScript vs expression distinction
- Correct webhook data access
- Safe null-handling patterns
- Production-ready code patterns

---

## Quick Reference

### Essential Rules
1. Choose "All Items" mode (recommended)
2. Access data: `$input.all()`, `$input.first()`, `$input.item`
3. **MUST return**: `[{json: {...}}]` format
4. **Webhook data**: Under `.body` property
5. **No `{{}}` syntax**: Use JavaScript directly

### Most Common Patterns
- Batch processing → $input.all() + map/filter
- Single item → $input.first()
- Aggregation → reduce()
- HTTP requests → $helpers.httpRequest()
- Date handling → DateTime (Luxon)

### Error Prevention
- Always return data
- Check for null/undefined
- Use try-catch for risky operations
- Test with empty input
- Use console.log() for debugging

---

## Related Documentation

- **n8n Code Node Guide**: https://docs.n8n.io/code/code-node/
- **Built-in Methods Reference**: https://docs.n8n.io/code-examples/methods-variables-reference/
- **Luxon Documentation**: https://moment.github.io/luxon/

---

## Evaluations

**5 test scenarios** covering:
1. Webhook body gotcha (most common mistake)
2. Return format error (missing array wrapper)
3. HTTP request with $helpers.httpRequest()
4. Aggregation pattern with $input.all()
5. Expression syntax confusion (using `{{}}`)

Each evaluation tests skill activation, correct guidance, and reference to appropriate documentation files.

---

## Version History

- **v1.0** (2025-01-20): Initial implementation
  - SKILL.md with comprehensive overview
  - DATA_ACCESS.md covering all access patterns
  - COMMON_PATTERNS.md with 10 production patterns
  - ERROR_PATTERNS.md covering top 5 errors
  - BUILTIN_FUNCTIONS.md complete reference
  - 5 evaluation scenarios

---

## Author

Conceived by Romuald Członkowski - [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)

Part of the n8n-skills collection.
```

## File: `skills/n8n-code-javascript/SKILL.md`
```markdown
---
name: n8n-code-javascript
description: Write JavaScript code in n8n Code nodes. Use when writing JavaScript in n8n, using $input/$json/$node syntax, making HTTP requests with $helpers, working with dates using DateTime, troubleshooting Code node errors, or choosing between Code node modes.
---

# JavaScript Code Node

Expert guidance for writing JavaScript code in n8n Code nodes.

---

## Quick Start

```javascript
// Basic template for Code nodes
const items = $input.all();

// Process data
const processed = items.map(item => ({
  json: {
    ...item.json,
    processed: true,
    timestamp: new Date().toISOString()
  }
}));

return processed;
```

### Essential Rules

1. **Choose "Run Once for All Items" mode** (recommended for most use cases)
2. **Access data**: `$input.all()`, `$input.first()`, or `$input.item`
3. **CRITICAL**: Must return `[{json: {...}}]` format
4. **CRITICAL**: Webhook data is under `$json.body` (not `$json` directly)
5. **Built-ins available**: $helpers.httpRequest(), DateTime (Luxon), $jmespath()

---

## Mode Selection Guide

The Code node offers two execution modes. Choose based on your use case:

### Run Once for All Items (Recommended - Default)

**Use this mode for:** 95% of use cases

- **How it works**: Code executes **once** regardless of input count
- **Data access**: `$input.all()` or `items` array
- **Best for**: Aggregation, filtering, batch processing, transformations, API calls with all data
- **Performance**: Faster for multiple items (single execution)

```javascript
// Example: Calculate total from all items
const allItems = $input.all();
const total = allItems.reduce((sum, item) => sum + (item.json.amount || 0), 0);

return [{
  json: {
    total,
    count: allItems.length,
    average: total / allItems.length
  }
}];
```

**When to use:**
- ✅ Comparing items across the dataset
- ✅ Calculating totals, averages, or statistics
- ✅ Sorting or ranking items
- ✅ Deduplication
- ✅ Building aggregated reports
- ✅ Combining data from multiple items

### Run Once for Each Item

**Use this mode for:** Specialized cases only

- **How it works**: Code executes **separately** for each input item
- **Data access**: `$input.item` or `$item`
- **Best for**: Item-specific logic, independent operations, per-item validation
- **Performance**: Slower for large datasets (multiple executions)

```javascript
// Example: Add processing timestamp to each item
const item = $input.item;

return [{
  json: {
    ...item.json,
    processed: true,
    processedAt: new Date().toISOString()
  }
}];
```

**When to use:**
- ✅ Each item needs independent API call
- ✅ Per-item validation with different error handling
- ✅ Item-specific transformations based on item properties
- ✅ When items must be processed separately for business logic

**Decision Shortcut:**
- **Need to look at multiple items?** → Use "All Items" mode
- **Each item completely independent?** → Use "Each Item" mode
- **Not sure?** → Use "All Items" mode (you can always loop inside)

---

## Data Access Patterns

### Pattern 1: $input.all() - Most Common

**Use when**: Processing arrays, batch operations, aggregations

```javascript
// Get all items from previous node
const allItems = $input.all();

// Filter, map, reduce as needed
const valid = allItems.filter(item => item.json.status === 'active');
const mapped = valid.map(item => ({
  json: {
    id: item.json.id,
    name: item.json.name
  }
}));

return mapped;
```

### Pattern 2: $input.first() - Very Common

**Use when**: Working with single objects, API responses, first-in-first-out

```javascript
// Get first item only
const firstItem = $input.first();
const data = firstItem.json;

return [{
  json: {
    result: processData(data),
    processedAt: new Date().toISOString()
  }
}];
```

### Pattern 3: $input.item - Each Item Mode Only

**Use when**: In "Run Once for Each Item" mode

```javascript
// Current item in loop (Each Item mode only)
const currentItem = $input.item;

return [{
  json: {
    ...currentItem.json,
    itemProcessed: true
  }
}];
```

### Pattern 4: $node - Reference Other Nodes

**Use when**: Need data from specific nodes in workflow

```javascript
// Get output from specific node
const webhookData = $node["Webhook"].json;
const httpData = $node["HTTP Request"].json;

return [{
  json: {
    combined: {
      webhook: webhookData,
      api: httpData
    }
  }
}];
```

**See**: [DATA_ACCESS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/drugbank_database/references/data_access.md) for comprehensive guide

---

## Critical: Webhook Data Structure

**MOST COMMON MISTAKE**: Webhook data is nested under `.body`

```javascript
// ❌ WRONG - Will return undefined
const name = $json.name;
const email = $json.email;

// ✅ CORRECT - Webhook data is under .body
const name = $json.body.name;
const email = $json.body.email;

// Or with $input
const webhookData = $input.first().json.body;
const name = webhookData.name;
```

**Why**: Webhook node wraps all request data under `body` property. This includes POST data, query parameters, and JSON payloads.

**See**: [DATA_ACCESS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/drugbank_database/references/data_access.md) for full webhook structure details

---

## Return Format Requirements

**CRITICAL RULE**: Always return array of objects with `json` property

### Correct Return Formats

```javascript
// ✅ Single result
return [{
  json: {
    field1: value1,
    field2: value2
  }
}];

// ✅ Multiple results
return [
  {json: {id: 1, data: 'first'}},
  {json: {id: 2, data: 'second'}}
];

// ✅ Transformed array
const transformed = $input.all()
  .filter(item => item.json.valid)
  .map(item => ({
    json: {
      id: item.json.id,
      processed: true
    }
  }));
return transformed;

// ✅ Empty result (when no data to return)
return [];

// ✅ Conditional return
if (shouldProcess) {
  return [{json: processedData}];
} else {
  return [];
}
```

### Incorrect Return Formats

```javascript
// ❌ WRONG: Object without array wrapper
return {
  json: {field: value}
};

// ❌ WRONG: Array without json wrapper
return [{field: value}];

// ❌ WRONG: Plain string
return "processed";

// ❌ WRONG: Raw data without mapping
return $input.all();  // Missing .map()

// ❌ WRONG: Incomplete structure
return [{data: value}];  // Should be {json: value}
```

**Why it matters**: Next nodes expect array format. Incorrect format causes workflow execution to fail.

**See**: [ERROR_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/render_deploy/references/error_patterns.md) #3 for detailed error solutions

---

## Common Patterns Overview

Based on production workflows, here are the most useful patterns:

### 1. Multi-Source Data Aggregation
Combine data from multiple APIs, webhooks, or nodes

```javascript
const allItems = $input.all();
const results = [];

for (const item of allItems) {
  const sourceName = item.json.name || 'Unknown';
  // Parse source-specific structure
  if (sourceName === 'API1' && item.json.data) {
    results.push({
      json: {
        title: item.json.data.title,
        source: 'API1'
      }
    });
  }
}

return results;
```

### 2. Filtering with Regex
Extract patterns, mentions, or keywords from text

```javascript
const pattern = /\b([A-Z]{2,5})\b/g;
const matches = {};

for (const item of $input.all()) {
  const text = item.json.text;
  const found = text.match(pattern);

  if (found) {
    found.forEach(match => {
      matches[match] = (matches[match] || 0) + 1;
    });
  }
}

return [{json: {matches}}];
```

### 3. Data Transformation & Enrichment
Map fields, normalize formats, add computed fields

```javascript
const items = $input.all();

return items.map(item => {
  const data = item.json;
  const nameParts = data.name.split(' ');

  return {
    json: {
      first_name: nameParts[0],
      last_name: nameParts.slice(1).join(' '),
      email: data.email,
      created_at: new Date().toISOString()
    }
  };
});
```

### 4. Top N Filtering & Ranking
Sort and limit results

```javascript
const items = $input.all();

const topItems = items
  .sort((a, b) => (b.json.score || 0) - (a.json.score || 0))
  .slice(0, 10);

return topItems.map(item => ({json: item.json}));
```

### 5. Aggregation & Reporting
Sum, count, group data

```javascript
const items = $input.all();
const total = items.reduce((sum, item) => sum + (item.json.amount || 0), 0);

return [{
  json: {
    total,
    count: items.length,
    average: total / items.length,
    timestamp: new Date().toISOString()
  }
}];
```

**See**: [COMMON_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/frontend_dev_guidelines/resources/common_patterns.md) for 10 detailed production patterns

---

## Error Prevention - Top 5 Mistakes

### #1: Empty Code or Missing Return (Most Common)

```javascript
// ❌ WRONG: No return statement
const items = $input.all();
// ... processing code ...
// Forgot to return!

// ✅ CORRECT: Always return data
const items = $input.all();
// ... processing ...
return items.map(item => ({json: item.json}));
```

### #2: Expression Syntax Confusion

```javascript
// ❌ WRONG: Using n8n expression syntax in code
const value = "{{ $json.field }}";

// ✅ CORRECT: Use JavaScript template literals
const value = `${$json.field}`;

// ✅ CORRECT: Direct access
const value = $input.first().json.field;
```

### #3: Incorrect Return Wrapper

```javascript
// ❌ WRONG: Returning object instead of array
return {json: {result: 'success'}};

// ✅ CORRECT: Array wrapper required
return [{json: {result: 'success'}}];
```

### #4: Missing Null Checks

```javascript
// ❌ WRONG: Crashes if field doesn't exist
const value = item.json.user.email;

// ✅ CORRECT: Safe access with optional chaining
const value = item.json?.user?.email || 'no-email@example.com';

// ✅ CORRECT: Guard clause
if (!item.json.user) {
  return [];
}
const value = item.json.user.email;
```

### #5: Webhook Body Nesting

```javascript
// ❌ WRONG: Direct access to webhook data
const email = $json.email;

// ✅ CORRECT: Webhook data under .body
const email = $json.body.email;
```

**See**: [ERROR_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/render_deploy/references/error_patterns.md) for comprehensive error guide

---

## Built-in Functions & Helpers

### $helpers.httpRequest()

Make HTTP requests from within code:

```javascript
const response = await $helpers.httpRequest({
  method: 'GET',
  url: 'https://api.example.com/data',
  headers: {
    'Authorization': 'Bearer token',
    'Content-Type': 'application/json'
  }
});

return [{json: {data: response}}];
```

### DateTime (Luxon)

Date and time operations:

```javascript
// Current time
const now = DateTime.now();

// Format dates
const formatted = now.toFormat('yyyy-MM-dd');
const iso = now.toISO();

// Date arithmetic
const tomorrow = now.plus({days: 1});
const lastWeek = now.minus({weeks: 1});

return [{
  json: {
    today: formatted,
    tomorrow: tomorrow.toFormat('yyyy-MM-dd')
  }
}];
```

### $jmespath()

Query JSON structures:

```javascript
const data = $input.first().json;

// Filter array
const adults = $jmespath(data, 'users[?age >= `18`]');

// Extract fields
const names = $jmespath(data, 'users[*].name');

return [{json: {adults, names}}];
```

**See**: [BUILTIN_FUNCTIONS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_code_javascript/BUILTIN_FUNCTIONS.md) for complete reference

---

## Best Practices

### 1. Always Validate Input Data

```javascript
const items = $input.all();

// Check if data exists
if (!items || items.length === 0) {
  return [];
}

// Validate structure
if (!items[0].json) {
  return [{json: {error: 'Invalid input format'}}];
}

// Continue processing...
```

### 2. Use Try-Catch for Error Handling

```javascript
try {
  const response = await $helpers.httpRequest({
    url: 'https://api.example.com/data'
  });

  return [{json: {success: true, data: response}}];
} catch (error) {
  return [{
    json: {
      success: false,
      error: error.message
    }
  }];
}
```

### 3. Prefer Array Methods Over Loops

```javascript
// ✅ GOOD: Functional approach
const processed = $input.all()
  .filter(item => item.json.valid)
  .map(item => ({json: {id: item.json.id}}));

// ❌ SLOWER: Manual loop
const processed = [];
for (const item of $input.all()) {
  if (item.json.valid) {
    processed.push({json: {id: item.json.id}});
  }
}
```

### 4. Filter Early, Process Late

```javascript
// ✅ GOOD: Filter first to reduce processing
const processed = $input.all()
  .filter(item => item.json.status === 'active')  // Reduce dataset first
  .map(item => expensiveTransformation(item));  // Then transform

// ❌ WASTEFUL: Transform everything, then filter
const processed = $input.all()
  .map(item => expensiveTransformation(item))  // Wastes CPU
  .filter(item => item.json.status === 'active');
```

### 5. Use Descriptive Variable Names

```javascript
// ✅ GOOD: Clear intent
const activeUsers = $input.all().filter(item => item.json.active);
const totalRevenue = activeUsers.reduce((sum, user) => sum + user.json.revenue, 0);

// ❌ BAD: Unclear purpose
const a = $input.all().filter(item => item.json.active);
const t = a.reduce((s, u) => s + u.json.revenue, 0);
```

### 6. Debug with console.log()

```javascript
// Debug statements appear in browser console
const items = $input.all();
console.log(`Processing ${items.length} items`);

for (const item of items) {
  console.log('Item data:', item.json);
  // Process...
}

return result;
```

---

## When to Use Code Node

Use Code node when:
- ✅ Complex transformations requiring multiple steps
- ✅ Custom calculations or business logic
- ✅ Recursive operations
- ✅ API response parsing with complex structure
- ✅ Multi-step conditionals
- ✅ Data aggregation across items

Consider other nodes when:
- ❌ Simple field mapping → Use **Set** node
- ❌ Basic filtering → Use **Filter** node
- ❌ Simple conditionals → Use **IF** or **Switch** node
- ❌ HTTP requests only → Use **HTTP Request** node

**Code node excels at**: Complex logic that would require chaining many simple nodes

---

## Integration with Other Skills

### Works With:

**n8n Expression Syntax**:
- Expressions use `{{ }}` syntax in other nodes
- Code nodes use JavaScript directly (no `{{ }}`)
- When to use expressions vs code

**n8n MCP Tools Expert**:
- How to find Code node: `search_nodes({query: "code"})`
- Get configuration help: `get_node({nodeType: "nodes-base.code"})`
- Validate code: `validate_node({nodeType: "nodes-base.code", config: {...}})`

**n8n Node Configuration**:
- Mode selection (All Items vs Each Item)
- Language selection (JavaScript vs Python)
- Understanding property dependencies

**n8n Workflow Patterns**:
- Code nodes in transformation step
- Webhook → Code → API pattern
- Error handling in workflows

**n8n Validation Expert**:
- Validate Code node configuration
- Handle validation errors
- Auto-fix common issues

---

## Quick Reference Checklist

Before deploying Code nodes, verify:

- [ ] **Code is not empty** - Must have meaningful logic
- [ ] **Return statement exists** - Must return array of objects
- [ ] **Proper return format** - Each item: `{json: {...}}`
- [ ] **Data access correct** - Using `$input.all()`, `$input.first()`, or `$input.item`
- [ ] **No n8n expressions** - Use JavaScript template literals: `` `${value}` ``
- [ ] **Error handling** - Guard clauses for null/undefined inputs
- [ ] **Webhook data** - Access via `.body` if from webhook
- [ ] **Mode selection** - "All Items" for most cases
- [ ] **Performance** - Prefer map/filter over manual loops
- [ ] **Output consistent** - All code paths return same structure

---

## Additional Resources

### Related Files
- [DATA_ACCESS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/drugbank_database/references/data_access.md) - Comprehensive data access patterns
- [COMMON_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/frontend_dev_guidelines/resources/common_patterns.md) - 10 production-tested patterns
- [ERROR_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/render_deploy/references/error_patterns.md) - Top 5 errors and solutions
- [BUILTIN_FUNCTIONS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_code_javascript/BUILTIN_FUNCTIONS.md) - Complete built-in reference

### n8n Documentation
- Code Node Guide: https://docs.n8n.io/code/code-node/
- Built-in Methods: https://docs.n8n.io/code-examples/methods-variables-reference/
- Luxon Documentation: https://moment.github.io/luxon/

---

**Ready to write JavaScript in n8n Code nodes!** Start with simple transformations, use the error patterns guide to avoid common mistakes, and reference the pattern library for production-ready examples.
```

## File: `skills/n8n-code-python/COMMON_PATTERNS.md`
```markdown
# Common Patterns - Python Code Node

Production-tested Python patterns for n8n Code nodes.

---

## ⚠️ Important: JavaScript First

**Use JavaScript for 95% of use cases.**

Python in n8n has **NO external libraries** (no requests, pandas, numpy).

Only use Python when:
- You have complex Python-specific logic
- You need Python's standard library features
- You're more comfortable with Python than JavaScript

For most workflows, **JavaScript is the better choice**.

---

## Pattern Overview

These 10 patterns cover common n8n Code node scenarios using Python:

1. **Multi-Source Data Aggregation** - Combine data from multiple nodes
2. **Regex-Based Filtering** - Filter items using pattern matching
3. **Markdown to Structured Data** - Parse markdown into structured format
4. **JSON Object Comparison** - Compare two JSON objects for changes
5. **CRM Data Transformation** - Transform CRM data to standard format
6. **Release Notes Processing** - Parse and categorize release notes
7. **Array Transformation** - Reshape arrays and extract fields
8. **Dictionary Lookup** - Create and use lookup dictionaries
9. **Top N Filtering** - Get top items by score/value
10. **String Aggregation** - Aggregate strings with formatting

---

## Pattern 1: Multi-Source Data Aggregation

**Use case**: Combine data from multiple sources (APIs, webhooks, databases).

**Scenario**: Aggregate news articles from multiple sources.

### Implementation

```python
from datetime import datetime

all_items = _input.all()
processed_articles = []

for item in all_items:
    source_name = item["json"].get("name", "Unknown")
    source_data = item["json"]

    # Process Hacker News source
    if source_name == "Hacker News" and source_data.get("hits"):
        for hit in source_data["hits"]:
            processed_articles.append({
                "title": hit.get("title", "No title"),
                "url": hit.get("url", ""),
                "summary": hit.get("story_text") or "No summary",
                "source": "Hacker News",
                "score": hit.get("points", 0),
                "fetched_at": datetime.now().isoformat()
            })

    # Process Reddit source
    elif source_name == "Reddit" and source_data.get("data"):
        for post in source_data["data"].get("children", []):
            post_data = post.get("data", {})
            processed_articles.append({
                "title": post_data.get("title", "No title"),
                "url": post_data.get("url", ""),
                "summary": post_data.get("selftext", "")[:200],
                "source": "Reddit",
                "score": post_data.get("score", 0),
                "fetched_at": datetime.now().isoformat()
            })

# Sort by score descending
processed_articles.sort(key=lambda x: x["score"], reverse=True)

# Return as n8n items
return [{"json": article} for article in processed_articles]
```

### Key Techniques

- Process multiple data sources in one loop
- Normalize different data structures
- Use datetime for timestamps
- Sort by criteria
- Return properly formatted items

---

## Pattern 2: Regex-Based Filtering

**Use case**: Filter items based on pattern matching in text fields.

**Scenario**: Filter support tickets by priority keywords.

### Implementation

```python
import re

all_items = _input.all()
priority_tickets = []

# High priority keywords pattern
high_priority_pattern = re.compile(
    r'\b(urgent|critical|emergency|asap|down|outage|broken)\b',
    re.IGNORECASE
)

for item in all_items:
    ticket = item["json"]

    # Check subject and description
    subject = ticket.get("subject", "")
    description = ticket.get("description", "")
    combined_text = f"{subject} {description}"

    # Find matches
    matches = high_priority_pattern.findall(combined_text)

    if matches:
        priority_tickets.append({
            "json": {
                **ticket,
                "priority": "high",
                "matched_keywords": list(set(matches)),
                "keyword_count": len(matches)
            }
        })
    else:
        priority_tickets.append({
            "json": {
                **ticket,
                "priority": "normal",
                "matched_keywords": [],
                "keyword_count": 0
            }
        })

# Sort by keyword count (most urgent first)
priority_tickets.sort(key=lambda x: x["json"]["keyword_count"], reverse=True)

return priority_tickets
```

### Key Techniques

- Use re.compile() for reusable patterns
- re.IGNORECASE for case-insensitive matching
- Combine multiple text fields for searching
- Extract and deduplicate matches
- Sort by priority indicators

---

## Pattern 3: Markdown to Structured Data

**Use case**: Parse markdown text into structured data.

**Scenario**: Extract tasks from markdown checklist.

### Implementation

```python
import re

markdown_text = _input.first()["json"]["body"].get("markdown", "")

# Parse markdown checklist
tasks = []
lines = markdown_text.split("\n")

for line in lines:
    # Match: - [ ] Task or - [x] Task
    match = re.match(r'^\s*-\s*\[([ x])\]\s*(.+)$', line, re.IGNORECASE)

    if match:
        checked = match.group(1).lower() == 'x'
        task_text = match.group(2).strip()

        # Extract priority if present (e.g., [P1], [HIGH])
        priority_match = re.search(r'\[(P\d|HIGH|MEDIUM|LOW)\]', task_text, re.IGNORECASE)
        priority = priority_match.group(1).upper() if priority_match else "NORMAL"

        # Remove priority tag from text
        clean_text = re.sub(r'\[(P\d|HIGH|MEDIUM|LOW)\]', '', task_text, flags=re.IGNORECASE).strip()

        tasks.append({
            "text": clean_text,
            "completed": checked,
            "priority": priority,
            "original_line": line.strip()
        })

return [{
    "json": {
        "tasks": tasks,
        "total": len(tasks),
        "completed": sum(1 for t in tasks if t["completed"]),
        "pending": sum(1 for t in tasks if not t["completed"])
    }
}]
```

### Key Techniques

- Line-by-line parsing
- Multiple regex patterns for extraction
- Extract metadata from text
- Calculate summary statistics
- Return structured data

---

## Pattern 4: JSON Object Comparison

**Use case**: Compare two JSON objects to find differences.

**Scenario**: Compare old and new user profile data.

### Implementation

```python
import json

all_items = _input.all()

# Assume first item is old data, second is new data
old_data = all_items[0]["json"] if len(all_items) > 0 else {}
new_data = all_items[1]["json"] if len(all_items) > 1 else {}

changes = {
    "added": {},
    "removed": {},
    "modified": {},
    "unchanged": {}
}

# Find all unique keys
all_keys = set(old_data.keys()) | set(new_data.keys())

for key in all_keys:
    old_value = old_data.get(key)
    new_value = new_data.get(key)

    if key not in old_data:
        # Added field
        changes["added"][key] = new_value
    elif key not in new_data:
        # Removed field
        changes["removed"][key] = old_value
    elif old_value != new_value:
        # Modified field
        changes["modified"][key] = {
            "old": old_value,
            "new": new_value
        }
    else:
        # Unchanged field
        changes["unchanged"][key] = old_value

return [{
    "json": {
        "changes": changes,
        "summary": {
            "added_count": len(changes["added"]),
            "removed_count": len(changes["removed"]),
            "modified_count": len(changes["modified"]),
            "unchanged_count": len(changes["unchanged"]),
            "has_changes": len(changes["added"]) > 0 or len(changes["removed"]) > 0 or len(changes["modified"]) > 0
        }
    }
}]
```

### Key Techniques

- Set operations for key comparison
- Dictionary .get() for safe access
- Categorize changes by type
- Create summary statistics
- Return detailed comparison

---

## Pattern 5: CRM Data Transformation

**Use case**: Transform CRM data to standard format.

**Scenario**: Normalize data from different CRM systems.

### Implementation

```python
from datetime import datetime
import re

all_items = _input.all()
normalized_contacts = []

for item in all_items:
    raw_contact = item["json"]
    source = raw_contact.get("source", "unknown")

    # Normalize email
    email = raw_contact.get("email", "").lower().strip()

    # Normalize phone (remove non-digits)
    phone_raw = raw_contact.get("phone", "")
    phone = re.sub(r'\D', '', phone_raw)

    # Parse name
    if "full_name" in raw_contact:
        name_parts = raw_contact["full_name"].split(" ", 1)
        first_name = name_parts[0] if len(name_parts) > 0 else ""
        last_name = name_parts[1] if len(name_parts) > 1 else ""
    else:
        first_name = raw_contact.get("first_name", "")
        last_name = raw_contact.get("last_name", "")

    # Normalize status
    status_raw = raw_contact.get("status", "").lower()
    status = "active" if status_raw in ["active", "enabled", "true", "1"] else "inactive"

    # Create normalized contact
    normalized_contacts.append({
        "json": {
            "id": raw_contact.get("id", ""),
            "first_name": first_name.strip(),
            "last_name": last_name.strip(),
            "full_name": f"{first_name} {last_name}".strip(),
            "email": email,
            "phone": phone,
            "status": status,
            "source": source,
            "normalized_at": datetime.now().isoformat(),
            "original_data": raw_contact
        }
    })

return normalized_contacts
```

### Key Techniques

- Multiple field name variations handling
- String cleaning and normalization
- Regex for phone number cleaning
- Name parsing logic
- Status normalization
- Preserve original data

---

## Pattern 6: Release Notes Processing

**Use case**: Parse release notes and categorize changes.

**Scenario**: Extract features, fixes, and breaking changes from release notes.

### Implementation

```python
import re

release_notes = _input.first()["json"]["body"].get("notes", "")

categories = {
    "features": [],
    "fixes": [],
    "breaking": [],
    "other": []
}

# Split into lines
lines = release_notes.split("\n")

for line in lines:
    line = line.strip()

    # Skip empty lines and headers
    if not line or line.startswith("#"):
        continue

    # Remove bullet points
    clean_line = re.sub(r'^[\*\-\+]\s*', '', line)

    # Categorize
    if re.search(r'\b(feature|add|new)\b', clean_line, re.IGNORECASE):
        categories["features"].append(clean_line)
    elif re.search(r'\b(fix|bug|patch|resolve)\b', clean_line, re.IGNORECASE):
        categories["fixes"].append(clean_line)
    elif re.search(r'\b(breaking|deprecated|remove)\b', clean_line, re.IGNORECASE):
        categories["breaking"].append(clean_line)
    else:
        categories["other"].append(clean_line)

return [{
    "json": {
        "categories": categories,
        "summary": {
            "features": len(categories["features"]),
            "fixes": len(categories["fixes"]),
            "breaking": len(categories["breaking"]),
            "other": len(categories["other"]),
            "total": sum(len(v) for v in categories.values())
        }
    }
}]
```

### Key Techniques

- Line-by-line parsing
- Pattern-based categorization
- Bullet point removal
- Skip headers and empty lines
- Summary statistics

---

## Pattern 7: Array Transformation

**Use case**: Reshape arrays and extract specific fields.

**Scenario**: Transform user data array to extract specific fields.

### Implementation

```python
all_items = _input.all()

# Extract and transform
transformed = []

for item in all_items:
    user = item["json"]

    # Extract nested fields
    profile = user.get("profile", {})
    settings = user.get("settings", {})

    transformed.append({
        "json": {
            "user_id": user.get("id"),
            "email": user.get("email"),
            "name": profile.get("name", "Unknown"),
            "avatar": profile.get("avatar_url"),
            "bio": profile.get("bio", "")[:100],  # Truncate to 100 chars
            "notifications_enabled": settings.get("notifications", True),
            "theme": settings.get("theme", "light"),
            "created_at": user.get("created_at"),
            "last_login": user.get("last_login_at")
        }
    })

return transformed
```

### Key Techniques

- Field extraction from nested objects
- Default values with .get()
- String truncation
- Flattening nested structures

---

## Pattern 8: Dictionary Lookup

**Use case**: Create lookup dictionary for fast data access.

**Scenario**: Look up user details by ID.

### Implementation

```python
all_items = _input.all()

# Build lookup dictionary
users_by_id = {}

for item in all_items:
    user = item["json"]
    user_id = user.get("id")

    if user_id:
        users_by_id[user_id] = {
            "name": user.get("name"),
            "email": user.get("email"),
            "status": user.get("status")
        }

# Example: Look up specific users
lookup_ids = [1, 3, 5]
looked_up = []

for user_id in lookup_ids:
    if user_id in users_by_id:
        looked_up.append({
            "json": {
                "id": user_id,
                **users_by_id[user_id],
                "found": True
            }
        })
    else:
        looked_up.append({
            "json": {
                "id": user_id,
                "found": False
            }
        })

return looked_up
```

### Key Techniques

- Dictionary comprehension alternative
- O(1) lookup time
- Handle missing keys gracefully
- Preserve lookup order

---

## Pattern 9: Top N Filtering

**Use case**: Get top items by score or value.

**Scenario**: Get top 10 products by sales.

### Implementation

```python
all_items = _input.all()

# Extract products with sales
products = []

for item in all_items:
    product = item["json"]
    products.append({
        "id": product.get("id"),
        "name": product.get("name"),
        "sales": product.get("sales", 0),
        "revenue": product.get("revenue", 0.0),
        "category": product.get("category")
    })

# Sort by sales descending
products.sort(key=lambda p: p["sales"], reverse=True)

# Get top 10
top_10 = products[:10]

return [
    {
        "json": {
            **product,
            "rank": index + 1
        }
    }
    for index, product in enumerate(top_10)
]
```

### Key Techniques

- List sorting with custom key
- Slicing for top N
- Add ranking information
- Enumerate for index

---

## Pattern 10: String Aggregation

**Use case**: Aggregate strings with formatting.

**Scenario**: Create summary text from multiple items.

### Implementation

```python
all_items = _input.all()

# Collect messages
messages = []

for item in all_items:
    data = item["json"]

    user = data.get("user", "Unknown")
    message = data.get("message", "")
    timestamp = data.get("timestamp", "")

    # Format each message
    formatted = f"[{timestamp}] {user}: {message}"
    messages.append(formatted)

# Join with newlines
summary = "\n".join(messages)

# Create statistics
total_length = sum(len(msg) for msg in messages)
average_length = total_length / len(messages) if messages else 0

return [{
    "json": {
        "summary": summary,
        "message_count": len(messages),
        "total_characters": total_length,
        "average_length": round(average_length, 2)
    }
}]
```

### Key Techniques

- String formatting with f-strings
- Join lists with separator
- Calculate string statistics
- Handle empty lists

---

## Pattern Comparison: Python vs JavaScript

### Data Access

```python
# Python
all_items = _input.all()
first_item = _input.first()
current = _input.item
webhook_data = _json["body"]

# JavaScript
const allItems = $input.all();
const firstItem = $input.first();
const current = $input.item;
const webhookData = $json.body;
```

### Dictionary/Object Access

```python
# Python - Dictionary key access
name = user["name"]           # May raise KeyError
name = user.get("name", "?")  # Safe with default

# JavaScript - Object property access
const name = user.name;              // May be undefined
const name = user.name || "?";       // Safe with default
```

### Array Operations

```python
# Python - List comprehension
filtered = [item for item in items if item["active"]]

# JavaScript - Array methods
const filtered = items.filter(item => item.active);
```

### Sorting

```python
# Python
items.sort(key=lambda x: x["score"], reverse=True)

# JavaScript
items.sort((a, b) => b.score - a.score);
```

---

## Best Practices

### 1. Use .get() for Safe Access

```python
# ✅ SAFE: Use .get() with defaults
name = user.get("name", "Unknown")
email = user.get("email", "no-email@example.com")

# ❌ RISKY: Direct key access
name = user["name"]  # KeyError if missing!
```

### 2. Handle Empty Lists

```python
# ✅ SAFE: Check before processing
items = _input.all()
if items:
    first = items[0]
else:
    return [{"json": {"error": "No items"}}]

# ❌ RISKY: Assume items exist
first = items[0]  # IndexError if empty!
```

### 3. Use List Comprehensions

```python
# ✅ PYTHONIC: List comprehension
active = [item for item in items if item["json"].get("active")]

# ❌ VERBOSE: Traditional loop
active = []
for item in items:
    if item["json"].get("active"):
        active.append(item)
```

### 4. Return Proper Format

```python
# ✅ CORRECT: Array of objects with "json" key
return [{"json": {"field": "value"}}]

# ❌ WRONG: Just the data
return {"field": "value"}

# ❌ WRONG: Array without "json" wrapper
return [{"field": "value"}]
```

### 5. Use Standard Library

```python
# ✅ GOOD: Use standard library
import statistics
average = statistics.mean(numbers)

# ✅ ALSO GOOD: Built-in functions
average = sum(numbers) / len(numbers) if numbers else 0

# ❌ CAN'T DO: External libraries
import numpy as np  # ModuleNotFoundError!
```

---

## When to Use Each Pattern

| Pattern | When to Use |
|---------|-------------|
| Multi-Source Aggregation | Combining data from different nodes/sources |
| Regex Filtering | Text pattern matching, validation, extraction |
| Markdown Parsing | Processing formatted text into structured data |
| JSON Comparison | Detecting changes between objects |
| CRM Transformation | Normalizing data from different systems |
| Release Notes | Categorizing text by keywords |
| Array Transformation | Reshaping data, extracting fields |
| Dictionary Lookup | Fast ID-based lookups |
| Top N Filtering | Getting best/worst items by criteria |
| String Aggregation | Creating formatted text summaries |

---

## Summary

**Key Takeaways**:
- Use `.get()` for safe dictionary access
- List comprehensions are pythonic and efficient
- Handle empty lists/None values
- Use standard library (json, datetime, re)
- Return proper n8n format: `[{"json": {...}}]`

**Remember**:
- JavaScript is recommended for 95% of use cases
- Python has NO external libraries
- Use n8n nodes for complex operations
- Code node is for data transformation, not API calls

**See Also**:
- [SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) - Python Code overview
- [DATA_ACCESS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/drugbank_database/references/data_access.md) - Data access patterns
- [STANDARD_LIBRARY.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_code_python/STANDARD_LIBRARY.md) - Available modules
- [ERROR_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/render_deploy/references/error_patterns.md) - Avoid common mistakes
```

## File: `skills/n8n-code-python/DATA_ACCESS.md`
```markdown
# Data Access Patterns - Python Code Node

Complete guide to accessing data in n8n Code nodes using Python.

---

## Overview

In n8n Python Code nodes, you access data using **underscore-prefixed** variables: `_input`, `_json`, `_node`.

**Data Access Priority** (by common usage):
1. **`_input.all()`** - Most common - Batch operations, aggregations
2. **`_input.first()`** - Very common - Single item operations
3. **`_input.item`** - Common - Each Item mode only
4. **`_node["NodeName"]["json"]`** - Specific node references
5. **`_json`** - Direct current item (use `_input` instead)

**Python vs JavaScript**:
| JavaScript | Python (Beta) | Python (Native) |
|------------|---------------|-----------------|
| `$input.all()` | `_input.all()` | `_items` |
| `$input.first()` | `_input.first()` | `_items[0]` |
| `$input.item` | `_input.item` | `_item` |
| `$json` | `_json` | `_item["json"]` |
| `$node["Name"]` | `_node["Name"]` | Not available |

---

## Pattern 1: _input.all() - Process All Items

**Usage**: Most common pattern for batch processing

**When to use:**
- Processing multiple records
- Aggregating data (sum, count, average)
- Filtering lists
- Transforming datasets

### Basic Usage

```python
# Get all items from previous node
all_items = _input.all()

# all_items is a list of dictionaries like:
# [
#   {"json": {"id": 1, "name": "Alice"}},
#   {"json": {"id": 2, "name": "Bob"}}
# ]

print(f"Received {len(all_items)} items")

return all_items
```

### Example 1: Filter Active Items

```python
all_items = _input.all()

# Filter only active items
active_items = [
    item for item in all_items
    if item["json"].get("status") == "active"
]

return active_items
```

### Example 2: Transform All Items

```python
all_items = _input.all()

# Transform to new structure
transformed = []
for item in all_items:
    transformed.append({
        "json": {
            "id": item["json"].get("id"),
            "full_name": f"{item['json'].get('first_name', '')} {item['json'].get('last_name', '')}",
            "email": item["json"].get("email"),
            "processed_at": datetime.now().isoformat()
        }
    })

return transformed
```

### Example 3: Aggregate Data

```python
all_items = _input.all()

# Calculate total
total = sum(item["json"].get("amount", 0) for item in all_items)

return [{
    "json": {
        "total": total,
        "count": len(all_items),
        "average": total / len(all_items) if all_items else 0
    }
}]
```

### Example 4: Sort and Limit

```python
all_items = _input.all()

# Get top 5 by score
sorted_items = sorted(
    all_items,
    key=lambda item: item["json"].get("score", 0),
    reverse=True
)
top_five = sorted_items[:5]

return [{"json": item["json"]} for item in top_five]
```

### Example 5: Group By Category

```python
all_items = _input.all()

# Group items by category
grouped = {}
for item in all_items:
    category = item["json"].get("category", "Uncategorized")

    if category not in grouped:
        grouped[category] = []

    grouped[category].append(item["json"])

# Convert to list format
return [
    {
        "json": {
            "category": category,
            "items": items,
            "count": len(items)
        }
    }
    for category, items in grouped.items()
]
```

### Example 6: Deduplicate by ID

```python
all_items = _input.all()

# Remove duplicates by ID
seen = set()
unique = []

for item in all_items:
    item_id = item["json"].get("id")

    if item_id and item_id not in seen:
        seen.add(item_id)
        unique.append(item)

return unique
```

---

## Pattern 2: _input.first() - Get First Item

**Usage**: Very common for single-item operations

**When to use:**
- Previous node returns single object
- Working with API responses
- Getting initial/first data point

### Basic Usage

```python
# Get first item from previous node
first_item = _input.first()

# Access the JSON data
data = first_item["json"]

print(f"First item: {data}")

return [{"json": data}]
```

### Example 1: Process Single API Response

```python
# Get API response (typically single object)
response = _input.first()["json"]

# Extract what you need
return [{
    "json": {
        "user_id": response.get("data", {}).get("user", {}).get("id"),
        "user_name": response.get("data", {}).get("user", {}).get("name"),
        "status": response.get("status"),
        "fetched_at": datetime.now().isoformat()
    }
}]
```

### Example 2: Transform Single Object

```python
data = _input.first()["json"]

# Transform structure
return [{
    "json": {
        "id": data.get("id"),
        "contact": {
            "email": data.get("email"),
            "phone": data.get("phone")
        },
        "address": {
            "street": data.get("street"),
            "city": data.get("city"),
            "zip": data.get("zip")
        }
    }
}]
```

### Example 3: Validate Single Item

```python
item = _input.first()["json"]

# Validation logic
is_valid = bool(item.get("email") and "@" in item.get("email", ""))

return [{
    "json": {
        **item,
        "valid": is_valid,
        "validated_at": datetime.now().isoformat()
    }
}]
```

### Example 4: Extract Nested Data

```python
response = _input.first()["json"]

# Navigate nested structure
users = response.get("data", {}).get("users", [])

return [
    {
        "json": {
            "id": user.get("id"),
            "name": user.get("profile", {}).get("name", "Unknown"),
            "email": user.get("contact", {}).get("email", "no-email")
        }
    }
    for user in users
]
```

---

## Pattern 3: _input.item - Current Item (Each Item Mode)

**Usage**: Common in "Run Once for Each Item" mode

**When to use:**
- Mode is set to "Run Once for Each Item"
- Need to process items independently
- Per-item API calls or validations

**IMPORTANT**: Only use in "Each Item" mode. Will be undefined in "All Items" mode.

### Basic Usage

```python
# In "Run Once for Each Item" mode
current_item = _input.item
data = current_item["json"]

print(f"Processing item: {data.get('id')}")

return [{
    "json": {
        **data,
        "processed": True
    }
}]
```

### Example 1: Add Processing Metadata

```python
item = _input.item

return [{
    "json": {
        **item["json"],
        "processed": True,
        "processed_at": datetime.now().isoformat(),
        "processing_duration": random.random() * 1000  # Simulated
    }
}]
```

### Example 2: Per-Item Validation

```python
item = _input.item
data = item["json"]

# Validate this specific item
errors = []

if not data.get("email"):
    errors.append("Email required")
if not data.get("name"):
    errors.append("Name required")
if data.get("age") and data["age"] < 18:
    errors.append("Must be 18+")

return [{
    "json": {
        **data,
        "valid": len(errors) == 0,
        "errors": errors if errors else None
    }
}]
```

### Example 3: Conditional Processing

```python
item = _input.item
data = item["json"]

# Process based on item type
if data.get("type") == "premium":
    return [{
        "json": {
            **data,
            "discount": 0.20,
            "tier": "premium"
        }
    }]
else:
    return [{
        "json": {
            **data,
            "discount": 0.05,
            "tier": "standard"
        }
    }]
```

---

## Pattern 4: _node - Reference Other Nodes

**Usage**: Less common, but powerful for specific scenarios

**When to use:**
- Need data from specific named node
- Combining data from multiple nodes

### Basic Usage

```python
# Get output from specific node
webhook_data = _node["Webhook"]["json"]
api_data = _node["HTTP Request"]["json"]

return [{
    "json": {
        "from_webhook": webhook_data,
        "from_api": api_data
    }
}]
```

### Example 1: Combine Multiple Sources

```python
# Reference multiple nodes
webhook = _node["Webhook"]["json"]
database = _node["Postgres"]["json"]
api = _node["HTTP Request"]["json"]

return [{
    "json": {
        "combined": {
            "webhook": webhook.get("body", {}),
            "db_records": len(database) if isinstance(database, list) else 1,
            "api_response": api.get("status")
        },
        "processed_at": datetime.now().isoformat()
    }
}]
```

### Example 2: Compare Across Nodes

```python
old_data = _node["Get Old Data"]["json"]
new_data = _node["Get New Data"]["json"]

# Simple comparison
changes = {
    "added": [n for n in new_data if n.get("id") not in [o.get("id") for o in old_data]],
    "removed": [o for o in old_data if o.get("id") not in [n.get("id") for n in new_data]]
}

return [{
    "json": {
        "changes": changes,
        "summary": {
            "added": len(changes["added"]),
            "removed": len(changes["removed"])
        }
    }
}]
```

---

## Critical: Webhook Data Structure

**MOST COMMON MISTAKE**: Forgetting webhook data is nested under `["body"]`

### The Problem

Webhook node wraps all incoming data under a `"body"` property.

### Structure

```python
# Webhook node output structure:
{
    "headers": {
        "content-type": "application/json",
        "user-agent": "..."
    },
    "params": {},
    "query": {},
    "body": {
        # ← YOUR DATA IS HERE
        "name": "Alice",
        "email": "alice@example.com",
        "message": "Hello!"
    }
}
```

### Wrong vs Right

```python
# ❌ WRONG: Trying to access directly
name = _json["name"]  # KeyError!
email = _json["email"]  # KeyError!

# ✅ CORRECT: Access via ["body"]
name = _json["body"]["name"]  # "Alice"
email = _json["body"]["email"]  # "alice@example.com"

# ✅ SAFER: Use .get() for safe access
webhook_data = _json.get("body", {})
name = webhook_data.get("name")  # None if missing
email = webhook_data.get("email", "no-email")  # Default value
```

### Example: Full Webhook Processing

```python
# Get webhook data from previous node
webhook_output = _input.first()["json"]

# Access the actual payload
payload = webhook_output.get("body", {})

# Access headers if needed
content_type = webhook_output.get("headers", {}).get("content-type")

# Access query parameters if needed
api_key = webhook_output.get("query", {}).get("api_key")

# Process the actual data
return [{
    "json": {
        # Data from webhook body
        "user_name": payload.get("name"),
        "user_email": payload.get("email"),
        "message": payload.get("message"),

        # Metadata
        "received_at": datetime.now().isoformat(),
        "content_type": content_type,
        "authenticated": bool(api_key)
    }
}]
```

### POST Data, Query Params, and Headers

```python
webhook = _input.first()["json"]

return [{
    "json": {
        # POST body data
        "form_data": webhook.get("body", {}),

        # Query parameters (?key=value)
        "query_params": webhook.get("query", {}),

        # HTTP headers
        "user_agent": webhook.get("headers", {}).get("user-agent"),
        "content_type": webhook.get("headers", {}).get("content-type"),

        # Request metadata
        "method": webhook.get("method"),  # POST, GET, etc.
        "url": webhook.get("url")
    }
}]
```

---

## Choosing the Right Pattern

### Decision Tree

```
Do you need ALL items from previous node?
├─ YES → Use _input.all()
│
└─ NO → Do you need just the FIRST item?
    ├─ YES → Use _input.first()
    │
    └─ NO → Are you in "Each Item" mode?
        ├─ YES → Use _input.item
        │
        └─ NO → Do you need specific node data?
            ├─ YES → Use _node["NodeName"]
            └─ NO → Use _input.first() (default)
```

### Quick Reference Table

| Scenario | Use This | Example |
|----------|----------|---------|
| Sum all amounts | `_input.all()` | `sum(i["json"].get("amount", 0) for i in items)` |
| Get API response | `_input.first()` | `_input.first()["json"].get("data")` |
| Process each independently | `_input.item` | `_input.item["json"]` (Each Item mode) |
| Combine two nodes | `_node["Name"]` | `_node["API"]["json"]` |
| Filter list | `_input.all()` | `[i for i in items if i["json"].get("active")]` |
| Transform single object | `_input.first()` | `{**_input.first()["json"], "new": True}` |
| Webhook data | `_input.first()` | `_input.first()["json"]["body"]` |

---

## Common Mistakes

### Mistake 1: Using _json Without Context

```python
# ❌ RISKY: _json is ambiguous
value = _json["field"]

# ✅ CLEAR: Be explicit
value = _input.first()["json"]["field"]
```

### Mistake 2: Forgetting ["json"] Property

```python
# ❌ WRONG: Trying to access fields on item dictionary
items = _input.all()
names = [item["name"] for item in items]  # KeyError!

# ✅ CORRECT: Access via ["json"]
names = [item["json"]["name"] for item in items]
```

### Mistake 3: Using _input.item in All Items Mode

```python
# ❌ WRONG: _input.item is None in "All Items" mode
data = _input.item["json"]  # AttributeError!

# ✅ CORRECT: Use appropriate method
data = _input.first()["json"]  # Or _input.all()
```

### Mistake 4: Not Handling Empty Lists

```python
# ❌ WRONG: Crashes if no items
first = _input.all()[0]["json"]  # IndexError!

# ✅ CORRECT: Check length first
items = _input.all()
if items:
    first = items[0]["json"]
else:
    return []

# ✅ ALSO CORRECT: Use _input.first()
first = _input.first()["json"]  # Built-in safety
```

### Mistake 5: Direct Dictionary Access (KeyError)

```python
# ❌ RISKY: Crashes if key missing
value = item["json"]["field"]  # KeyError!

# ✅ SAFE: Use .get()
value = item["json"].get("field", "default")
```

---

## Advanced Patterns

### Pattern: Safe Nested Access

```python
# Deep nested access with .get()
value = (
    _input.first()["json"]
    .get("level1", {})
    .get("level2", {})
    .get("level3", "default")
)
```

### Pattern: List Comprehension with Filtering

```python
items = _input.all()

# Filter and transform in one step
result = [
    {
        "json": {
            "id": item["json"]["id"],
            "name": item["json"]["name"].upper()
        }
    }
    for item in items
    if item["json"].get("active") and item["json"].get("verified")
]

return result
```

### Pattern: Dictionary Comprehension

```python
items = _input.all()

# Create lookup dictionary
lookup = {
    item["json"]["id"]: item["json"]
    for item in items
    if "id" in item["json"]
}

return [{"json": lookup}]
```

---

## Summary

**Most Common Patterns**:
1. `_input.all()` - Process multiple items, batch operations
2. `_input.first()` - Single item, API responses
3. `_input.item` - Each Item mode processing

**Critical Rule**:
- Webhook data is under `["body"]` property

**Best Practice**:
- Use `.get()` for dictionary access to avoid KeyError
- Always check for empty lists
- Be explicit: Use `_input.first()["json"]["field"]` instead of `_json["field"]`

**See Also**:
- [SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) - Overview and quick start
- [COMMON_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/frontend_dev_guidelines/resources/common_patterns.md) - Python-specific patterns
- [ERROR_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/render_deploy/references/error_patterns.md) - Avoid common mistakes
```

## File: `skills/n8n-code-python/ERROR_PATTERNS.md`
```markdown
# Error Patterns - Python Code Node

Common Python Code node errors and how to fix them.

---

## Error Overview

**Top 5 Python Code Node Errors**:

1. **ModuleNotFoundError** - Trying to import external libraries (Python-specific)
2. **Empty Code / Missing Return** - No code or return statement
3. **KeyError** - Dictionary access without .get()
4. **IndexError** - List access without bounds checking
5. **Incorrect Return Format** - Wrong data structure returned

These 5 errors cover the majority of Python Code node failures.

---

## Error #1: ModuleNotFoundError (MOST CRITICAL)

**Frequency**: Very common in Python Code nodes

**What it is**: Attempting to import external libraries that aren't available.

### The Problem

```python
# ❌ WRONG: External libraries not available
import requests  # ModuleNotFoundError: No module named 'requests'
import pandas    # ModuleNotFoundError: No module named 'pandas'
import numpy     # ModuleNotFoundError: No module named 'numpy'
import bs4       # ModuleNotFoundError: No module named 'bs4'
import pymongo   # ModuleNotFoundError: No module named 'pymongo'
import psycopg2  # ModuleNotFoundError: No module named 'psycopg2'

# This code will FAIL - these libraries are not installed!
response = requests.get("https://api.example.com/data")
```

### The Solution

**Option 1: Use JavaScript Instead** (Recommended for 95% of cases)

```javascript
// ✅ JavaScript Code node with $helpers.httpRequest()
const response = await $helpers.httpRequest({
  method: 'GET',
  url: 'https://api.example.com/data'
});

return [{json: response}];
```

**Option 2: Use n8n HTTP Request Node**

```python
# ✅ Add HTTP Request node BEFORE Python Code node
# Access the response in Python Code node

response = _input.first()["json"]

return [{
    "json": {
        "status": response.get("status"),
        "data": response.get("body"),
        "processed": True
    }
}]
```

**Option 3: Use Standard Library Only**

```python
# ✅ Use urllib from standard library (limited functionality)
from urllib.request import urlopen
from urllib.parse import urlencode
import json

# Simple GET request (no headers, no auth)
url = "https://api.example.com/data"
with urlopen(url) as response:
    data = json.loads(response.read())

return [{"json": data}]
```

### Common Library Replacements

| Need | ❌ External Library | ✅ Alternative |
|------|-------------------|----------------|
| HTTP requests | `requests` | Use HTTP Request node or JavaScript |
| Data analysis | `pandas` | Use Python list comprehensions |
| Database | `psycopg2`, `pymongo` | Use n8n database nodes |
| Web scraping | `beautifulsoup4` | Use HTML Extract node |
| Excel | `openpyxl` | Use Spreadsheet File node |
| Image processing | `pillow` | Use external API or node |

### Available Standard Library Modules

```python
# ✅ THESE WORK - Standard library only
import json          # JSON parsing
import datetime      # Date/time operations
import re            # Regular expressions
import base64        # Base64 encoding
import hashlib       # Hashing (MD5, SHA256)
import urllib.parse  # URL parsing and encoding
import math          # Math functions
import random        # Random numbers
import statistics    # Statistical functions
import collections   # defaultdict, Counter, etc.
```

---

## Error #2: Empty Code / Missing Return

**Frequency**: Common across all Code nodes

**What it is**: Code node has no code or no return statement.

### The Problem

```python
# ❌ WRONG: Empty code
# (nothing here)

# ❌ WRONG: Code but no return
items = _input.all()
processed = [item for item in items if item["json"].get("active")]
# Forgot to return!

# ❌ WRONG: Return in wrong scope
if _input.all():
    return [{"json": {"result": "success"}}]
# Return is inside if block - may not execute!
```

### The Solution

```python
# ✅ CORRECT: Always return
all_items = _input.all()

if not all_items:
    # Return empty array or error
    return [{"json": {"error": "No items"}}]

# Process items
processed = [item for item in all_items if item["json"].get("active")]

# Always return at the end
return processed if processed else [{"json": {"message": "No active items"}}]
```

### Best Practice

```python
# ✅ GOOD: Return at end of function (unconditional)
def process_items():
    items = _input.all()

    if not items:
        return [{"json": {"error": "Empty input"}}]

    # Process
    result = []
    for item in items:
        result.append({"json": item["json"]})

    return result

# Call function and return result
return process_items()
```

---

## Error #3: KeyError

**Frequency**: Very common in Python Code nodes

**What it is**: Accessing dictionary key that doesn't exist.

### The Problem

```python
# ❌ WRONG: Direct key access
item = _input.first()["json"]

name = item["name"]        # KeyError if "name" doesn't exist!
email = item["email"]      # KeyError if "email" doesn't exist!
age = item["age"]          # KeyError if "age" doesn't exist!

return [{
    "json": {
        "name": name,
        "email": email,
        "age": age
    }
}]
```

### Error Message

```
KeyError: 'name'
```

### The Solution

```python
# ✅ CORRECT: Use .get() with defaults
item = _input.first()["json"]

name = item.get("name", "Unknown")
email = item.get("email", "no-email@example.com")
age = item.get("age", 0)

return [{
    "json": {
        "name": name,
        "email": email,
        "age": age
    }
}]
```

### Nested Dictionary Access

```python
# ❌ WRONG: Nested key access
webhook = _input.first()["json"]
name = webhook["body"]["user"]["name"]  # Multiple KeyErrors possible!

# ✅ CORRECT: Safe nested access
webhook = _input.first()["json"]
body = webhook.get("body", {})
user = body.get("user", {})
name = user.get("name", "Unknown")

# ✅ ALSO CORRECT: Chained .get()
name = (
    webhook
    .get("body", {})
    .get("user", {})
    .get("name", "Unknown")
)

return [{"json": {"name": name}}]
```

### Webhook Body Access (Critical!)

```python
# ❌ WRONG: Forgetting webhook data is under "body"
webhook = _input.first()["json"]
name = webhook["name"]        # KeyError!
email = webhook["email"]      # KeyError!

# ✅ CORRECT: Access via ["body"]
webhook = _input.first()["json"]
body = webhook.get("body", {})
name = body.get("name", "Unknown")
email = body.get("email", "no-email")

return [{
    "json": {
        "name": name,
        "email": email
    }
}]
```

---

## Error #4: IndexError

**Frequency**: Common when processing arrays/lists

**What it is**: Accessing list index that doesn't exist.

### The Problem

```python
# ❌ WRONG: Assuming items exist
all_items = _input.all()
first_item = all_items[0]        # IndexError if list is empty!
second_item = all_items[1]       # IndexError if only 1 item!

return [{
    "json": {
        "first": first_item["json"],
        "second": second_item["json"]
    }
}]
```

### Error Message

```
IndexError: list index out of range
```

### The Solution

```python
# ✅ CORRECT: Check length first
all_items = _input.all()

if len(all_items) >= 2:
    first_item = all_items[0]["json"]
    second_item = all_items[1]["json"]

    return [{
        "json": {
            "first": first_item,
            "second": second_item
        }
    }]
else:
    return [{
        "json": {
            "error": f"Expected 2+ items, got {len(all_items)}"
        }
    }]
```

### Safe First Item Access

```python
# ✅ CORRECT: Use _input.first() instead of [0]
# This is safer than manual indexing
first_item = _input.first()["json"]

return [{"json": first_item}]

# ✅ ALSO CORRECT: Check before accessing
all_items = _input.all()
if all_items:
    first_item = all_items[0]["json"]
else:
    first_item = {}

return [{"json": first_item}]
```

### Slice Instead of Index

```python
# ✅ CORRECT: Use slicing (never raises IndexError)
all_items = _input.all()

# Get first 5 items (won't fail if fewer than 5)
first_five = all_items[:5]

# Get items after first (won't fail if empty)
rest = all_items[1:]

return [{"json": item["json"]} for item in first_five]
```

---

## Error #5: Incorrect Return Format

**Frequency**: Common for new users

**What it is**: Returning data in wrong format (n8n expects array of objects with "json" key).

### The Problem

```python
# ❌ WRONG: Returning plain dictionary
return {"name": "Alice", "age": 30}

# ❌ WRONG: Returning array without "json" wrapper
return [{"name": "Alice"}, {"name": "Bob"}]

# ❌ WRONG: Returning None
return None

# ❌ WRONG: Returning string
return "success"

# ❌ WRONG: Returning single item (not array)
return {"json": {"name": "Alice"}}
```

### The Solution

```python
# ✅ CORRECT: Array of objects with "json" key
return [{"json": {"name": "Alice", "age": 30}}]

# ✅ CORRECT: Multiple items
return [
    {"json": {"name": "Alice"}},
    {"json": {"name": "Bob"}}
]

# ✅ CORRECT: Transform items
all_items = _input.all()
return [
    {"json": item["json"]}
    for item in all_items
]

# ✅ CORRECT: Empty array (valid)
return []

# ✅ CORRECT: Single item still needs array wrapper
return [{"json": {"result": "success"}}]
```

### Common Scenarios

**Scenario 1: Aggregation (Return Single Result)**

```python
# Calculate total
all_items = _input.all()
total = sum(item["json"].get("amount", 0) for item in all_items)

# ✅ CORRECT: Wrap in array with "json"
return [{
    "json": {
        "total": total,
        "count": len(all_items)
    }
}]
```

**Scenario 2: Filtering (Return Multiple Results)**

```python
# Filter active items
all_items = _input.all()
active = [item for item in all_items if item["json"].get("active")]

# ✅ CORRECT: Already in correct format
return active

# ✅ ALSO CORRECT: If transforming
return [
    {"json": {**item["json"], "filtered": True}}
    for item in active
]
```

**Scenario 3: No Results**

```python
# ✅ CORRECT: Return empty array
return []

# ✅ ALSO CORRECT: Return error message
return [{"json": {"error": "No results found"}}]
```

---

## Bonus Error: AttributeError

**What it is**: Using _input.item in wrong mode.

### The Problem

```python
# ❌ WRONG: Using _input.item in "All Items" mode
current = _input.item        # None in "All Items" mode
data = current["json"]       # AttributeError: 'NoneType' object has no attribute '__getitem__'
```

### The Solution

```python
# ✅ CORRECT: Check mode or use appropriate method
# In "All Items" mode, use:
all_items = _input.all()

# In "Each Item" mode, use:
current_item = _input.item

# ✅ SAFE: Check if item exists
current = _input.item
if current:
    data = current["json"]
    return [{"json": data}]
else:
    # Running in "All Items" mode
    return _input.all()
```

---

## Error Prevention Checklist

Before running your Python Code node, verify:

- [ ] **No external imports**: Only standard library (json, datetime, re, etc.)
- [ ] **Code returns data**: Every code path ends with `return`
- [ ] **Correct format**: Returns `[{"json": {...}}]` (array with "json" key)
- [ ] **Safe dictionary access**: Uses `.get()` instead of `[]` for dictionaries
- [ ] **Safe list access**: Checks length before indexing or uses slicing
- [ ] **Webhook body access**: Accesses webhook data via `_json["body"]`
- [ ] **No None returns**: Returns empty array `[]` instead of `None`
- [ ] **Mode awareness**: Uses `_input.all()`, `_input.first()`, or `_input.item` appropriately

---

## Quick Fix Reference

| Error | Quick Fix |
|-------|-----------|
| `ModuleNotFoundError` | Use JavaScript or HTTP Request node instead |
| `KeyError: 'field'` | Change `data["field"]` to `data.get("field", default)` |
| `IndexError: list index out of range` | Check `if len(items) > 0:` before `items[0]` |
| Empty output | Add `return [{"json": {...}}]` at end |
| `AttributeError: 'NoneType'` | Check mode setting or verify `_input.item` exists |
| Wrong format error | Wrap result: `return [{"json": result}]` |
| Webhook KeyError | Access via `_json.get("body", {})` |

---

## Testing Your Code

### Test Pattern 1: Handle Empty Input

```python
# ✅ Always test with empty input
all_items = _input.all()

if not all_items:
    return [{"json": {"message": "No items to process"}}]

# Continue with processing
# ...
```

### Test Pattern 2: Test with Missing Fields

```python
# ✅ Use .get() with defaults
item = _input.first()["json"]

# These won't fail even if fields missing
name = item.get("name", "Unknown")
email = item.get("email", "no-email")
age = item.get("age", 0)

return [{"json": {"name": name, "email": email, "age": age}}]
```

### Test Pattern 3: Test Both Modes

```python
# ✅ Code that works in both modes
try:
    # Try "Each Item" mode first
    current = _input.item
    if current:
        return [{"json": current["json"]}]
except:
    pass

# Fall back to "All Items" mode
all_items = _input.all()
return all_items if all_items else [{"json": {"message": "No data"}}]
```

---

## Summary

**Top 5 Errors to Avoid**:
1. **ModuleNotFoundError** - Use JavaScript or n8n nodes instead
2. **Missing return** - Always end with `return [{"json": {...}}]`
3. **KeyError** - Use `.get()` for dictionary access
4. **IndexError** - Check length before indexing
5. **Wrong format** - Return `[{"json": {...}}]`, not plain objects

**Golden Rules**:
- NO external libraries (use JavaScript instead)
- ALWAYS use `.get()` for dictionaries
- ALWAYS return `[{"json": {...}}]` format
- CHECK lengths before list access
- ACCESS webhook data via `["body"]`

**Remember**:
- JavaScript is recommended for 95% of use cases
- Python has limitations (no requests, pandas, numpy)
- Use n8n nodes for complex operations

**See Also**:
- [SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) - Python Code overview
- [DATA_ACCESS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/drugbank_database/references/data_access.md) - Data access patterns
- [STANDARD_LIBRARY.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_code_python/STANDARD_LIBRARY.md) - Available modules
- [COMMON_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/frontend_dev_guidelines/resources/common_patterns.md) - Production patterns
```

## File: `skills/n8n-code-python/README.md`
```markdown
# n8n Code Python Skill

Expert guidance for writing Python code in n8n Code nodes.

---

## ⚠️ Important: JavaScript First

**Use JavaScript for 95% of use cases.**

Python in n8n has **NO external libraries** (no requests, pandas, numpy).

**When to use Python**:
- You have complex Python-specific logic
- You need Python's standard library features
- You're more comfortable with Python than JavaScript

**When to use JavaScript** (recommended):
- HTTP requests ($helpers.httpRequest available)
- Date/time operations (Luxon library included)
- Most data transformations
- When in doubt

---

## What This Skill Teaches

### Core Concepts

1. **Critical Limitation**: No external libraries
2. **Data Access**: `_input.all()`, `_input.first()`, `_input.item`
3. **Webhook Gotcha**: Data is under `_json["body"]`
4. **Return Format**: Must return `[{"json": {...}}]`
5. **Standard Library**: json, datetime, re, base64, hashlib, etc.

### Top 5 Error Prevention

This skill emphasizes **error prevention**:

1. **ModuleNotFoundError** (trying to import external libraries)
2. **Empty code / missing return**
3. **KeyError** (dictionary access without .get())
4. **IndexError** (list access without bounds checking)
5. **Incorrect return format**

These 5 errors are the most common in Python Code nodes.

---

## Skill Activation

This skill activates when you:
- Write Python in Code nodes
- Ask about Python limitations
- Need to know available standard library
- Troubleshoot Python Code node errors
- Work with Python data structures

**Example queries**:
- "Can I use pandas in Python Code node?"
- "How do I access webhook data in Python?"
- "What Python libraries are available?"
- "Write Python code to process JSON"
- "Why is requests module not found?"

---

## File Structure

### SKILL.md (719 lines)
**Quick start** and overview
- When to use Python vs JavaScript
- Critical limitation (no external libraries)
- Mode selection (All Items vs Each Item)
- Data access overview
- Return format requirements
- Standard library overview

### DATA_ACCESS.md (703 lines)
**Complete data access patterns**
- `_input.all()` - Process all items
- `_input.first()` - Get first item
- `_input.item` - Current item (Each Item mode)
- `_node["Name"]` - Reference other nodes
- Webhook body structure (critical gotcha!)
- Pattern selection guide

### STANDARD_LIBRARY.md (850 lines)
**Available Python modules**
- json - JSON parsing
- datetime - Date/time operations
- re - Regular expressions
- base64 - Encoding/decoding
- hashlib - Hashing
- urllib.parse - URL operations
- math, random, statistics
- What's NOT available (requests, pandas, numpy)
- Workarounds for missing libraries

### COMMON_PATTERNS.md (895 lines)
**10 production-tested patterns**
1. Multi-source data aggregation
2. Regex-based filtering
3. Markdown to structured data
4. JSON object comparison
5. CRM data transformation
6. Release notes processing
7. Array transformation
8. Dictionary lookup
9. Top N filtering
10. String aggregation

### ERROR_PATTERNS.md (730 lines)
**Top 5 errors with solutions**
1. ModuleNotFoundError (external libraries)
2. Empty code / missing return
3. KeyError (dictionary access)
4. IndexError (list access)
5. Incorrect return format
- Error prevention checklist
- Quick fix reference
- Testing patterns

---

## Integration with Other Skills

This skill works with:

### n8n Expression Syntax
- Python uses code syntax, not {{}} expressions
- Data access patterns differ ($ vs _)

### n8n MCP Tools Expert
- Use MCP tools to validate Code node configurations
- Check node setup with `get_node`

### n8n Workflow Patterns
- Code nodes fit into larger workflow patterns
- Often used after HTTP Request or Webhook nodes

### n8n Code JavaScript
- Compare Python vs JavaScript approaches
- Understand when to use which language
- JavaScript recommended for 95% of cases

### n8n Node Configuration
- Configure Code node mode (All Items vs Each Item)
- Set up proper connections

---

## Success Metrics

After using this skill, you should be able to:

- [ ] **Know the limitation**: Python has NO external libraries
- [ ] **Choose language**: JavaScript for 95% of cases, Python when needed
- [ ] **Access data**: Use `_input.all()`, `_input.first()`, `_input.item`
- [ ] **Handle webhooks**: Access data via `_json["body"]`
- [ ] **Return properly**: Always return `[{"json": {...}}]`
- [ ] **Avoid KeyError**: Use `.get()` for dictionary access
- [ ] **Use standard library**: Know what's available (json, datetime, re, etc.)
- [ ] **Prevent errors**: Avoid top 5 common errors
- [ ] **Choose alternatives**: Use n8n nodes when libraries needed
- [ ] **Write production code**: Use proven patterns

---

## Quick Reference

### Data Access
```python
all_items = _input.all()
first_item = _input.first()
current_item = _input.item  # Each Item mode only
other_node = _node["NodeName"]
```

### Webhook Data
```python
webhook = _input.first()["json"]
body = webhook.get("body", {})
name = body.get("name")
```

### Safe Dictionary Access
```python
# ✅ Use .get() with defaults
value = data.get("field", "default")

# ❌ Risky - may raise KeyError
value = data["field"]
```

### Return Format
```python
# ✅ Correct format
return [{"json": {"result": "success"}}]

# ❌ Wrong - plain dict
return {"result": "success"}
```

### Standard Library
```python
# ✅ Available
import json
import datetime
import re
import base64
import hashlib

# ❌ NOT available
import requests  # ModuleNotFoundError!
import pandas    # ModuleNotFoundError!
import numpy     # ModuleNotFoundError!
```

---

## Common Use Cases

### Use Case 1: Process Webhook Data
```python
webhook = _input.first()["json"]
body = webhook.get("body", {})

return [{
    "json": {
        "name": body.get("name"),
        "email": body.get("email"),
        "processed": True
    }
}]
```

### Use Case 2: Filter and Transform
```python
all_items = _input.all()

active = [
    {"json": {**item["json"], "filtered": True}}
    for item in all_items
    if item["json"].get("status") == "active"
]

return active
```

### Use Case 3: Aggregate Statistics
```python
import statistics

all_items = _input.all()
amounts = [item["json"].get("amount", 0) for item in all_items]

return [{
    "json": {
        "total": sum(amounts),
        "average": statistics.mean(amounts) if amounts else 0,
        "count": len(amounts)
    }
}]
```

### Use Case 4: Parse JSON String
```python
import json

data = _input.first()["json"]["body"]
json_string = data.get("payload", "{}")

try:
    parsed = json.loads(json_string)
    return [{"json": parsed}]
except json.JSONDecodeError:
    return [{"json": {"error": "Invalid JSON"}}]
```

---

## Limitations and Workarounds

### Limitation 1: No HTTP Requests Library
**Problem**: No `requests` library
**Workaround**: Use HTTP Request node or JavaScript

### Limitation 2: No Data Analysis Library
**Problem**: No `pandas` or `numpy`
**Workaround**: Use list comprehensions and standard library

### Limitation 3: No Database Drivers
**Problem**: No `psycopg2`, `pymongo`, etc.
**Workaround**: Use n8n database nodes (Postgres, MySQL, MongoDB)

### Limitation 4: No Web Scraping
**Problem**: No `beautifulsoup4` or `selenium`
**Workaround**: Use HTML Extract node

---

## Best Practices

1. **Use JavaScript for most cases** (95% recommendation)
2. **Use .get() for dictionaries** (avoid KeyError)
3. **Check lengths before indexing** (avoid IndexError)
4. **Always return proper format**: `[{"json": {...}}]`
5. **Access webhook data via ["body"]**
6. **Use standard library only** (no external imports)
7. **Handle empty input** (check `if items:`)
8. **Test both modes** (All Items and Each Item)

---

## When Python is the Right Choice

Use Python when:
- Complex text processing (re module)
- Mathematical calculations (math, statistics)
- Date/time manipulation (datetime)
- Cryptographic operations (hashlib)
- You have existing Python logic to reuse
- Team is more comfortable with Python

Use JavaScript instead when:
- Making HTTP requests
- Working with dates (Luxon included)
- Most data transformations
- When in doubt

---

## Learning Path

**Beginner**:
1. Read SKILL.md - Understand the limitation
2. Try DATA_ACCESS.md examples - Learn `_input` patterns
3. Practice safe dictionary access with `.get()`

**Intermediate**:
4. Study STANDARD_LIBRARY.md - Know what's available
5. Try COMMON_PATTERNS.md examples - Use proven patterns
6. Learn ERROR_PATTERNS.md - Avoid common mistakes

**Advanced**:
7. Combine multiple patterns
8. Use standard library effectively
9. Know when to switch to JavaScript
10. Write production-ready code

---

## Support

**Questions?**
- Check ERROR_PATTERNS.md for common issues
- Review COMMON_PATTERNS.md for examples
- Consider using JavaScript instead

**Related Skills**:
- n8n Code JavaScript - Alternative (recommended for 95% of cases)
- n8n Expression Syntax - For {{}} expressions in other nodes
- n8n Workflow Patterns - Bigger picture workflow design

---

## Version

**Version**: 1.0.0
**Status**: Production Ready
**Compatibility**: n8n Code node (Python mode)

---

## Credits

Part of the n8n-skills project.

**Conceived by Romuald Członkowski**
- Website: [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)
- Part of [n8n-mcp project](https://github.com/czlonkowski/n8n-mcp)

---

**Remember**: JavaScript is recommended for 95% of use cases. Use Python only when you specifically need Python's standard library features.
```

## File: `skills/n8n-code-python/SKILL.md`
```markdown
---
name: n8n-code-python
description: Write Python code in n8n Code nodes. Use when writing Python in n8n, using _input/_json/_node syntax, working with standard library, or need to understand Python limitations in n8n Code nodes.
---

# Python Code Node (Beta)

Expert guidance for writing Python code in n8n Code nodes.

---

## ⚠️ Important: JavaScript First

**Recommendation**: Use **JavaScript for 95% of use cases**. Only use Python when:
- You need specific Python standard library functions
- You're significantly more comfortable with Python syntax
- You're doing data transformations better suited to Python

**Why JavaScript is preferred:**
- Full n8n helper functions ($helpers.httpRequest, etc.)
- Luxon DateTime library for advanced date/time operations
- No external library limitations
- Better n8n documentation and community support

---

## Quick Start

```python
# Basic template for Python Code nodes
items = _input.all()

# Process data
processed = []
for item in items:
    processed.append({
        "json": {
            **item["json"],
            "processed": True,
            "timestamp": datetime.now().isoformat()
        }
    })

return processed
```

### Essential Rules

1. **Consider JavaScript first** - Use Python only when necessary
2. **Access data**: `_input.all()`, `_input.first()`, or `_input.item`
3. **CRITICAL**: Must return `[{"json": {...}}]` format
4. **CRITICAL**: Webhook data is under `_json["body"]` (not `_json` directly)
5. **CRITICAL LIMITATION**: **No external libraries** (no requests, pandas, numpy)
6. **Standard library only**: json, datetime, re, base64, hashlib, urllib.parse, math, random, statistics

---

## Mode Selection Guide

Same as JavaScript - choose based on your use case:

### Run Once for All Items (Recommended - Default)

**Use this mode for:** 95% of use cases

- **How it works**: Code executes **once** regardless of input count
- **Data access**: `_input.all()` or `_items` array (Native mode)
- **Best for**: Aggregation, filtering, batch processing, transformations
- **Performance**: Faster for multiple items (single execution)

```python
# Example: Calculate total from all items
all_items = _input.all()
total = sum(item["json"].get("amount", 0) for item in all_items)

return [{
    "json": {
        "total": total,
        "count": len(all_items),
        "average": total / len(all_items) if all_items else 0
    }
}]
```

### Run Once for Each Item

**Use this mode for:** Specialized cases only

- **How it works**: Code executes **separately** for each input item
- **Data access**: `_input.item` or `_item` (Native mode)
- **Best for**: Item-specific logic, independent operations, per-item validation
- **Performance**: Slower for large datasets (multiple executions)

```python
# Example: Add processing timestamp to each item
item = _input.item

return [{
    "json": {
        **item["json"],
        "processed": True,
        "processed_at": datetime.now().isoformat()
    }
}]
```

---

## Python Modes: Beta vs Native

n8n offers two Python execution modes:

### Python (Beta) - Recommended
- **Use**: `_input`, `_json`, `_node` helper syntax
- **Best for**: Most Python use cases
- **Helpers available**: `_now`, `_today`, `_jmespath()`
- **Import**: `from datetime import datetime`

```python
# Python (Beta) example
items = _input.all()
now = _now  # Built-in datetime object

return [{
    "json": {
        "count": len(items),
        "timestamp": now.isoformat()
    }
}]
```

### Python (Native) (Beta)
- **Use**: `_items`, `_item` variables only
- **No helpers**: No `_input`, `_now`, etc.
- **More limited**: Standard Python only
- **Use when**: Need pure Python without n8n helpers

```python
# Python (Native) example
processed = []

for item in _items:
    processed.append({
        "json": {
            "id": item["json"].get("id"),
            "processed": True
        }
    })

return processed
```

**Recommendation**: Use **Python (Beta)** for better n8n integration.

---

## Data Access Patterns

### Pattern 1: _input.all() - Most Common

**Use when**: Processing arrays, batch operations, aggregations

```python
# Get all items from previous node
all_items = _input.all()

# Filter, transform as needed
valid = [item for item in all_items if item["json"].get("status") == "active"]

processed = []
for item in valid:
    processed.append({
        "json": {
            "id": item["json"]["id"],
            "name": item["json"]["name"]
        }
    })

return processed
```

### Pattern 2: _input.first() - Very Common

**Use when**: Working with single objects, API responses

```python
# Get first item only
first_item = _input.first()
data = first_item["json"]

return [{
    "json": {
        "result": process_data(data),
        "processed_at": datetime.now().isoformat()
    }
}]
```

### Pattern 3: _input.item - Each Item Mode Only

**Use when**: In "Run Once for Each Item" mode

```python
# Current item in loop (Each Item mode only)
current_item = _input.item

return [{
    "json": {
        **current_item["json"],
        "item_processed": True
    }
}]
```

### Pattern 4: _node - Reference Other Nodes

**Use when**: Need data from specific nodes in workflow

```python
# Get output from specific node
webhook_data = _node["Webhook"]["json"]
http_data = _node["HTTP Request"]["json"]

return [{
    "json": {
        "combined": {
            "webhook": webhook_data,
            "api": http_data
        }
    }
}]
```

**See**: [DATA_ACCESS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/drugbank_database/references/data_access.md) for comprehensive guide

---

## Critical: Webhook Data Structure

**MOST COMMON MISTAKE**: Webhook data is nested under `["body"]`

```python
# ❌ WRONG - Will raise KeyError
name = _json["name"]
email = _json["email"]

# ✅ CORRECT - Webhook data is under ["body"]
name = _json["body"]["name"]
email = _json["body"]["email"]

# ✅ SAFER - Use .get() for safe access
webhook_data = _json.get("body", {})
name = webhook_data.get("name")
```

**Why**: Webhook node wraps all request data under `body` property. This includes POST data, query parameters, and JSON payloads.

**See**: [DATA_ACCESS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/drugbank_database/references/data_access.md) for full webhook structure details

---

## Return Format Requirements

**CRITICAL RULE**: Always return list of dictionaries with `"json"` key

### Correct Return Formats

```python
# ✅ Single result
return [{
    "json": {
        "field1": value1,
        "field2": value2
    }
}]

# ✅ Multiple results
return [
    {"json": {"id": 1, "data": "first"}},
    {"json": {"id": 2, "data": "second"}}
]

# ✅ List comprehension
transformed = [
    {"json": {"id": item["json"]["id"], "processed": True}}
    for item in _input.all()
    if item["json"].get("valid")
]
return transformed

# ✅ Empty result (when no data to return)
return []

# ✅ Conditional return
if should_process:
    return [{"json": processed_data}]
else:
    return []
```

### Incorrect Return Formats

```python
# ❌ WRONG: Dictionary without list wrapper
return {
    "json": {"field": value}
}

# ❌ WRONG: List without json wrapper
return [{"field": value}]

# ❌ WRONG: Plain string
return "processed"

# ❌ WRONG: Incomplete structure
return [{"data": value}]  # Should be {"json": value}
```

**Why it matters**: Next nodes expect list format. Incorrect format causes workflow execution to fail.

**See**: [ERROR_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/render_deploy/references/error_patterns.md) #2 for detailed error solutions

---

## Critical Limitation: No External Libraries

**MOST IMPORTANT PYTHON LIMITATION**: Cannot import external packages

### What's NOT Available

```python
# ❌ NOT AVAILABLE - Will raise ModuleNotFoundError
import requests  # ❌ No
import pandas  # ❌ No
import numpy  # ❌ No
import scipy  # ❌ No
from bs4 import BeautifulSoup  # ❌ No
import lxml  # ❌ No
```

### What IS Available (Standard Library)

```python
# ✅ AVAILABLE - Standard library only
import json  # ✅ JSON parsing
import datetime  # ✅ Date/time operations
import re  # ✅ Regular expressions
import base64  # ✅ Base64 encoding/decoding
import hashlib  # ✅ Hashing functions
import urllib.parse  # ✅ URL parsing
import math  # ✅ Math functions
import random  # ✅ Random numbers
import statistics  # ✅ Statistical functions
```

### Workarounds

**Need HTTP requests?**
- ✅ Use **HTTP Request node** before Code node
- ✅ Or switch to **JavaScript** and use `$helpers.httpRequest()`

**Need data analysis (pandas/numpy)?**
- ✅ Use Python **statistics** module for basic stats
- ✅ Or switch to **JavaScript** for most operations
- ✅ Manual calculations with lists and dictionaries

**Need web scraping (BeautifulSoup)?**
- ✅ Use **HTTP Request node** + **HTML Extract node**
- ✅ Or switch to **JavaScript** with regex/string methods

**See**: [STANDARD_LIBRARY.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_code_python/STANDARD_LIBRARY.md) for complete reference

---

## Common Patterns Overview

Based on production workflows, here are the most useful Python patterns:

### 1. Data Transformation
Transform all items with list comprehensions

```python
items = _input.all()

return [
    {
        "json": {
            "id": item["json"].get("id"),
            "name": item["json"].get("name", "Unknown").upper(),
            "processed": True
        }
    }
    for item in items
]
```

### 2. Filtering & Aggregation
Sum, filter, count with built-in functions

```python
items = _input.all()
total = sum(item["json"].get("amount", 0) for item in items)
valid_items = [item for item in items if item["json"].get("amount", 0) > 0]

return [{
    "json": {
        "total": total,
        "count": len(valid_items)
    }
}]
```

### 3. String Processing with Regex
Extract patterns from text

```python
import re

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

### 4. Data Validation
Validate and clean data

```python
items = _input.all()
validated = []

for item in items:
    data = item["json"]
    errors = []

    # Validate fields
    if not data.get("email"):
        errors.append("Email required")
    if not data.get("name"):
        errors.append("Name required")

    validated.append({
        "json": {
            **data,
            "valid": len(errors) == 0,
            "errors": errors if errors else None
        }
    })

return validated
```

### 5. Statistical Analysis
Calculate statistics with statistics module

```python
from statistics import mean, median, stdev

items = _input.all()
values = [item["json"].get("value", 0) for item in items if "value" in item["json"]]

if values:
    return [{
        "json": {
            "mean": mean(values),
            "median": median(values),
            "stdev": stdev(values) if len(values) > 1 else 0,
            "min": min(values),
            "max": max(values),
            "count": len(values)
        }
    }]
else:
    return [{"json": {"error": "No values found"}}]
```

**See**: [COMMON_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/frontend_dev_guidelines/resources/common_patterns.md) for 10 detailed Python patterns

---

## Error Prevention - Top 5 Mistakes

### #1: Importing External Libraries (Python-Specific!)

```python
# ❌ WRONG: Trying to import external library
import requests  # ModuleNotFoundError!

# ✅ CORRECT: Use HTTP Request node or JavaScript
# Add HTTP Request node before Code node
# OR switch to JavaScript and use $helpers.httpRequest()
```

### #2: Empty Code or Missing Return

```python
# ❌ WRONG: No return statement
items = _input.all()
# Processing...
# Forgot to return!

# ✅ CORRECT: Always return data
items = _input.all()
# Processing...
return [{"json": item["json"]} for item in items]
```

### #3: Incorrect Return Format

```python
# ❌ WRONG: Returning dict instead of list
return {"json": {"result": "success"}}

# ✅ CORRECT: List wrapper required
return [{"json": {"result": "success"}}]
```

### #4: KeyError on Dictionary Access

```python
# ❌ WRONG: Direct access crashes if missing
name = _json["user"]["name"]  # KeyError!

# ✅ CORRECT: Use .get() for safe access
name = _json.get("user", {}).get("name", "Unknown")
```

### #5: Webhook Body Nesting

```python
# ❌ WRONG: Direct access to webhook data
email = _json["email"]  # KeyError!

# ✅ CORRECT: Webhook data under ["body"]
email = _json["body"]["email"]

# ✅ BETTER: Safe access with .get()
email = _json.get("body", {}).get("email", "no-email")
```

**See**: [ERROR_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/render_deploy/references/error_patterns.md) for comprehensive error guide

---

## Standard Library Reference

### Most Useful Modules

```python
# JSON operations
import json
data = json.loads(json_string)
json_output = json.dumps({"key": "value"})

# Date/time
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)
formatted = now.strftime("%Y-%m-%d")

# Regular expressions
import re
matches = re.findall(r'\d+', text)
cleaned = re.sub(r'[^\w\s]', '', text)

# Base64 encoding
import base64
encoded = base64.b64encode(data).decode()
decoded = base64.b64decode(encoded)

# Hashing
import hashlib
hash_value = hashlib.sha256(text.encode()).hexdigest()

# URL parsing
import urllib.parse
params = urllib.parse.urlencode({"key": "value"})
parsed = urllib.parse.urlparse(url)

# Statistics
from statistics import mean, median, stdev
average = mean([1, 2, 3, 4, 5])
```

**See**: [STANDARD_LIBRARY.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_code_python/STANDARD_LIBRARY.md) for complete reference

---

## Best Practices

### 1. Always Use .get() for Dictionary Access

```python
# ✅ SAFE: Won't crash if field missing
value = item["json"].get("field", "default")

# ❌ RISKY: Crashes if field doesn't exist
value = item["json"]["field"]
```

### 2. Handle None/Null Values Explicitly

```python
# ✅ GOOD: Default to 0 if None
amount = item["json"].get("amount") or 0

# ✅ GOOD: Check for None explicitly
text = item["json"].get("text")
if text is None:
    text = ""
```

### 3. Use List Comprehensions for Filtering

```python
# ✅ PYTHONIC: List comprehension
valid = [item for item in items if item["json"].get("active")]

# ❌ VERBOSE: Manual loop
valid = []
for item in items:
    if item["json"].get("active"):
        valid.append(item)
```

### 4. Return Consistent Structure

```python
# ✅ CONSISTENT: Always list with "json" key
return [{"json": result}]  # Single result
return results  # Multiple results (already formatted)
return []  # No results
```

### 5. Debug with print() Statements

```python
# Debug statements appear in browser console (F12)
items = _input.all()
print(f"Processing {len(items)} items")
print(f"First item: {items[0] if items else 'None'}")
```

---

## When to Use Python vs JavaScript

### Use Python When:
- ✅ You need `statistics` module for statistical operations
- ✅ You're significantly more comfortable with Python syntax
- ✅ Your logic maps well to list comprehensions
- ✅ You need specific standard library functions

### Use JavaScript When:
- ✅ You need HTTP requests ($helpers.httpRequest())
- ✅ You need advanced date/time (DateTime/Luxon)
- ✅ You want better n8n integration
- ✅ **For 95% of use cases** (recommended)

### Consider Other Nodes When:
- ❌ Simple field mapping → Use **Set** node
- ❌ Basic filtering → Use **Filter** node
- ❌ Simple conditionals → Use **IF** or **Switch** node
- ❌ HTTP requests only → Use **HTTP Request** node

---

## Integration with Other Skills

### Works With:

**n8n Expression Syntax**:
- Expressions use `{{ }}` syntax in other nodes
- Code nodes use Python directly (no `{{ }}`)
- When to use expressions vs code

**n8n MCP Tools Expert**:
- How to find Code node: `search_nodes({query: "code"})`
- Get configuration help: `get_node({nodeType: "nodes-base.code"})`
- Validate code: `validate_node({nodeType: "nodes-base.code", config: {...}})`

**n8n Node Configuration**:
- Mode selection (All Items vs Each Item)
- Language selection (Python vs JavaScript)
- Understanding property dependencies

**n8n Workflow Patterns**:
- Code nodes in transformation step
- When to use Python vs JavaScript in patterns

**n8n Validation Expert**:
- Validate Code node configuration
- Handle validation errors
- Auto-fix common issues

**n8n Code JavaScript**:
- When to use JavaScript instead
- Comparison of JavaScript vs Python features
- Migration from Python to JavaScript

---

## Quick Reference Checklist

Before deploying Python Code nodes, verify:

- [ ] **Considered JavaScript first** - Using Python only when necessary
- [ ] **Code is not empty** - Must have meaningful logic
- [ ] **Return statement exists** - Must return list of dictionaries
- [ ] **Proper return format** - Each item: `{"json": {...}}`
- [ ] **Data access correct** - Using `_input.all()`, `_input.first()`, or `_input.item`
- [ ] **No external imports** - Only standard library (json, datetime, re, etc.)
- [ ] **Safe dictionary access** - Using `.get()` to avoid KeyError
- [ ] **Webhook data** - Access via `["body"]` if from webhook
- [ ] **Mode selection** - "All Items" for most cases
- [ ] **Output consistent** - All code paths return same structure

---

## Additional Resources

### Related Files
- [DATA_ACCESS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/drugbank_database/references/data_access.md) - Comprehensive Python data access patterns
- [COMMON_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/frontend_dev_guidelines/resources/common_patterns.md) - 10 Python patterns for n8n
- [ERROR_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/render_deploy/references/error_patterns.md) - Top 5 errors and solutions
- [STANDARD_LIBRARY.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_code_python/STANDARD_LIBRARY.md) - Complete standard library reference

### n8n Documentation
- Code Node Guide: https://docs.n8n.io/code/code-node/
- Python in n8n: https://docs.n8n.io/code/builtin/python-modules/

---

**Ready to write Python in n8n Code nodes - but consider JavaScript first!** Use Python for specific needs, reference the error patterns guide to avoid common mistakes, and leverage the standard library effectively.
```

## File: `skills/n8n-code-python/STANDARD_LIBRARY.md`
```markdown
# Standard Library Reference - Python Code Node

Complete guide to available Python standard library modules in n8n Code nodes.

---

## ⚠️ Critical Limitation

**NO EXTERNAL LIBRARIES AVAILABLE**

Python Code nodes in n8n have **ONLY** the Python standard library. No pip packages.

```python
# ❌ NOT AVAILABLE - Will cause ModuleNotFoundError
import requests      # No HTTP library!
import pandas        # No data analysis!
import numpy         # No numerical computing!
import bs4          # No web scraping!
import selenium     # No browser automation!
import psycopg2     # No database drivers!
import pymongo      # No MongoDB!
import sqlalchemy   # No ORMs!

# ✅ AVAILABLE - Standard library only
import json
import datetime
import re
import base64
import hashlib
import urllib.parse
import urllib.request
import math
import random
import statistics
```

**Recommendation**: Use **JavaScript** for 95% of use cases. JavaScript has more capabilities in n8n.

---

## Available Modules

### Priority 1: Most Useful (Use These)

1. **json** - JSON parsing and generation
2. **datetime** - Date and time operations
3. **re** - Regular expressions
4. **base64** - Base64 encoding/decoding
5. **hashlib** - Hashing (MD5, SHA256, etc.)
6. **urllib.parse** - URL parsing and encoding

### Priority 2: Moderately Useful

7. **math** - Mathematical functions
8. **random** - Random number generation
9. **statistics** - Statistical functions
10. **collections** - Specialized data structures

### Priority 3: Occasionally Useful

11. **itertools** - Iterator tools
12. **functools** - Higher-order functions
13. **operator** - Standard operators as functions
14. **string** - String constants and templates
15. **textwrap** - Text wrapping utilities

---

## Module 1: json - JSON Operations

**Most common module** - Parse and generate JSON data.

### Parse JSON String

```python
import json

# Parse JSON string to Python dict
json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)

return [{
    "json": {
        "name": data["name"],
        "age": data["age"],
        "parsed": True
    }
}]
```

### Generate JSON String

```python
import json

# Convert Python dict to JSON string
data = {
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ],
    "total": 2
}

json_string = json.dumps(data, indent=2)

return [{
    "json": {
        "json_output": json_string,
        "length": len(json_string)
    }
}]
```

### Handle JSON Errors

```python
import json

webhook_data = _input.first()["json"]["body"]
json_string = webhook_data.get("data", "")

try:
    parsed = json.loads(json_string)
    status = "valid"
    error = None
except json.JSONDecodeError as e:
    parsed = None
    status = "invalid"
    error = str(e)

return [{
    "json": {
        "status": status,
        "data": parsed,
        "error": error
    }
}]
```

### Pretty Print JSON

```python
import json

# Format JSON with indentation
data = _input.first()["json"]

pretty_json = json.dumps(data, indent=2, sort_keys=True)

return [{
    "json": {
        "formatted": pretty_json
    }
}]
```

---

## Module 2: datetime - Date and Time

**Very common** - Date parsing, formatting, calculations.

### Current Date and Time

```python
from datetime import datetime

now = datetime.now()

return [{
    "json": {
        "timestamp": now.isoformat(),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "formatted": now.strftime("%B %d, %Y at %I:%M %p")
    }
}]
```

### Parse Date String

```python
from datetime import datetime

date_string = "2025-01-15T14:30:00"
dt = datetime.fromisoformat(date_string)

return [{
    "json": {
        "year": dt.year,
        "month": dt.month,
        "day": dt.day,
        "hour": dt.hour,
        "weekday": dt.strftime("%A")
    }
}]
```

### Date Calculations

```python
from datetime import datetime, timedelta

now = datetime.now()

# Calculate future/past dates
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
next_week = now + timedelta(weeks=1)
one_hour_ago = now - timedelta(hours=1)

return [{
    "json": {
        "now": now.isoformat(),
        "tomorrow": tomorrow.isoformat(),
        "yesterday": yesterday.isoformat(),
        "next_week": next_week.isoformat(),
        "one_hour_ago": one_hour_ago.isoformat()
    }
}]
```

### Compare Dates

```python
from datetime import datetime

date1 = datetime(2025, 1, 15)
date2 = datetime(2025, 1, 20)

# Calculate difference
diff = date2 - date1

return [{
    "json": {
        "days_difference": diff.days,
        "seconds_difference": diff.total_seconds(),
        "date1_is_earlier": date1 < date2,
        "date2_is_later": date2 > date1
    }
}]
```

### Format Dates

```python
from datetime import datetime

dt = datetime.now()

return [{
    "json": {
        "iso": dt.isoformat(),
        "us_format": dt.strftime("%m/%d/%Y"),
        "eu_format": dt.strftime("%d/%m/%Y"),
        "long_format": dt.strftime("%A, %B %d, %Y"),
        "time_12h": dt.strftime("%I:%M %p"),
        "time_24h": dt.strftime("%H:%M:%S")
    }
}]
```

---

## Module 3: re - Regular Expressions

**Common** - Pattern matching, text extraction, validation.

### Pattern Matching

```python
import re

text = "Email: alice@example.com, Phone: 555-1234"

# Find email
email_match = re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
email = email_match.group(0) if email_match else None

# Find phone
phone_match = re.search(r'\d{3}-\d{4}', text)
phone = phone_match.group(0) if phone_match else None

return [{
    "json": {
        "email": email,
        "phone": phone
    }
}]
```

### Extract All Matches

```python
import re

text = "Tags: #python #automation #workflow #n8n"

# Find all hashtags
hashtags = re.findall(r'#(\w+)', text)

return [{
    "json": {
        "tags": hashtags,
        "count": len(hashtags)
    }
}]
```

### Replace Patterns

```python
import re

text = "Price: $99.99, Discount: $10.00"

# Remove dollar signs
cleaned = re.sub(r'\$', '', text)

# Replace multiple spaces with single space
normalized = re.sub(r'\s+', ' ', cleaned)

return [{
    "json": {
        "original": text,
        "cleaned": cleaned,
        "normalized": normalized
    }
}]
```

### Validate Format

```python
import re

email = _input.first()["json"]["body"].get("email", "")

# Email validation pattern
email_pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
is_valid = bool(re.match(email_pattern, email))

return [{
    "json": {
        "email": email,
        "valid": is_valid
    }
}]
```

### Split on Pattern

```python
import re

text = "apple,banana;orange|grape"

# Split on multiple delimiters
items = re.split(r'[,;|]', text)

# Clean up whitespace
items = [item.strip() for item in items]

return [{
    "json": {
        "items": items,
        "count": len(items)
    }
}]
```

---

## Module 4: base64 - Encoding/Decoding

**Common** - Encode binary data, API authentication.

### Encode String to Base64

```python
import base64

text = "Hello, World!"

# Encode to base64
encoded_bytes = base64.b64encode(text.encode('utf-8'))
encoded_string = encoded_bytes.decode('utf-8')

return [{
    "json": {
        "original": text,
        "encoded": encoded_string
    }
}]
```

### Decode Base64 to String

```python
import base64

encoded = "SGVsbG8sIFdvcmxkIQ=="

# Decode from base64
decoded_bytes = base64.b64decode(encoded)
decoded_string = decoded_bytes.decode('utf-8')

return [{
    "json": {
        "encoded": encoded,
        "decoded": decoded_string
    }
}]
```

### Basic Auth Header

```python
import base64

username = "admin"
password = "secret123"

# Create Basic Auth header
credentials = f"{username}:{password}"
encoded = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
auth_header = f"Basic {encoded}"

return [{
    "json": {
        "authorization": auth_header
    }
}]
```

---

## Module 5: hashlib - Hashing

**Common** - Generate checksums, hash passwords, create IDs.

### MD5 Hash

```python
import hashlib

text = "Hello, World!"

# Generate MD5 hash
md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()

return [{
    "json": {
        "original": text,
        "md5": md5_hash
    }
}]
```

### SHA256 Hash

```python
import hashlib

data = _input.first()["json"]["body"]
text = data.get("password", "")

# Generate SHA256 hash (more secure than MD5)
sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()

return [{
    "json": {
        "hashed": sha256_hash
    }
}]
```

### Generate Unique ID

```python
import hashlib
from datetime import datetime

# Create unique ID from multiple values
unique_string = f"{datetime.now().isoformat()}-{_json.get('user_id', 'unknown')}"
unique_id = hashlib.sha256(unique_string.encode('utf-8')).hexdigest()[:16]

return [{
    "json": {
        "id": unique_id,
        "generated_at": datetime.now().isoformat()
    }
}]
```

---

## Module 6: urllib.parse - URL Operations

**Common** - Parse URLs, encode parameters.

### Parse URL

```python
from urllib.parse import urlparse

url = "https://example.com/path?key=value&foo=bar#section"

parsed = urlparse(url)

return [{
    "json": {
        "scheme": parsed.scheme,      # "https"
        "netloc": parsed.netloc,      # "example.com"
        "path": parsed.path,          # "/path"
        "query": parsed.query,        # "key=value&foo=bar"
        "fragment": parsed.fragment    # "section"
    }
}]
```

### URL Encode Parameters

```python
from urllib.parse import urlencode

params = {
    "name": "Alice Smith",
    "email": "alice@example.com",
    "message": "Hello, World!"
}

# Encode parameters for URL
encoded = urlencode(params)

return [{
    "json": {
        "query_string": encoded,
        "full_url": f"https://api.example.com/submit?{encoded}"
    }
}]
```

### Parse Query String

```python
from urllib.parse import parse_qs

query_string = "name=Alice&age=30&tags=python&tags=n8n"

# Parse query string
params = parse_qs(query_string)

return [{
    "json": {
        "name": params.get("name", [""])[0],
        "age": int(params.get("age", ["0"])[0]),
        "tags": params.get("tags", [])
    }
}]
```

### URL Encode/Decode Strings

```python
from urllib.parse import quote, unquote

text = "Hello, World! 你好"

# URL encode
encoded = quote(text)

# URL decode
decoded = unquote(encoded)

return [{
    "json": {
        "original": text,
        "encoded": encoded,
        "decoded": decoded
    }
}]
```

---

## Module 7: math - Mathematical Operations

**Moderately useful** - Advanced math functions.

### Basic Math Functions

```python
import math

number = 16.7

return [{
    "json": {
        "ceiling": math.ceil(number),      # 17
        "floor": math.floor(number),       # 16
        "rounded": round(number),          # 17
        "square_root": math.sqrt(16),      # 4.0
        "power": math.pow(2, 3),          # 8.0
        "absolute": math.fabs(-5.5)       # 5.5
    }
}]
```

### Trigonometry

```python
import math

angle_degrees = 45
angle_radians = math.radians(angle_degrees)

return [{
    "json": {
        "sine": math.sin(angle_radians),
        "cosine": math.cos(angle_radians),
        "tangent": math.tan(angle_radians),
        "pi": math.pi,
        "e": math.e
    }
}]
```

### Logarithms

```python
import math

number = 100

return [{
    "json": {
        "log10": math.log10(number),     # 2.0
        "natural_log": math.log(number), # 4.605...
        "log2": math.log2(number)        # 6.644...
    }
}]
```

---

## Module 8: random - Random Numbers

**Moderately useful** - Generate random data, sampling.

### Random Numbers

```python
import random

return [{
    "json": {
        "random_float": random.random(),           # 0.0 to 1.0
        "random_int": random.randint(1, 100),      # 1 to 100
        "random_range": random.randrange(0, 100, 5) # 0, 5, 10, ..., 95
    }
}]
```

### Random Choice

```python
import random

colors = ["red", "green", "blue", "yellow"]
users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

return [{
    "json": {
        "random_color": random.choice(colors),
        "random_user": random.choice(users)
    }
}]
```

### Shuffle List

```python
import random

items = [1, 2, 3, 4, 5]
shuffled = items.copy()
random.shuffle(shuffled)

return [{
    "json": {
        "original": items,
        "shuffled": shuffled
    }
}]
```

### Random Sample

```python
import random

items = list(range(1, 101))

# Get 10 random items without replacement
sample = random.sample(items, 10)

return [{
    "json": {
        "sample": sample,
        "count": len(sample)
    }
}]
```

---

## Module 9: statistics - Statistical Functions

**Moderately useful** - Calculate stats from data.

### Basic Statistics

```python
import statistics

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

return [{
    "json": {
        "mean": statistics.mean(numbers),           # 55.0
        "median": statistics.median(numbers),       # 55.0
        "mode": statistics.mode([1, 2, 2, 3]),     # 2
        "stdev": statistics.stdev(numbers),        # 30.28...
        "variance": statistics.variance(numbers)   # 916.67...
    }
}]
```

### Aggregate from Items

```python
import statistics

all_items = _input.all()

# Extract amounts
amounts = [item["json"].get("amount", 0) for item in all_items]

if amounts:
    return [{
        "json": {
            "count": len(amounts),
            "total": sum(amounts),
            "average": statistics.mean(amounts),
            "median": statistics.median(amounts),
            "min": min(amounts),
            "max": max(amounts),
            "range": max(amounts) - min(amounts)
        }
    }]
else:
    return [{"json": {"error": "No data"}}]
```

---

## Workarounds for Missing Libraries

### HTTP Requests (No requests library)

```python
# ❌ Can't use requests library
# import requests  # ModuleNotFoundError!

# ✅ Use HTTP Request node instead
# Add HTTP Request node BEFORE Code node
# Access the response in Code node

response_data = _input.first()["json"]

return [{
    "json": {
        "status": response_data.get("status"),
        "data": response_data.get("body"),
        "processed": True
    }
}]
```

### Data Processing (No pandas)

```python
# ❌ Can't use pandas
# import pandas as pd  # ModuleNotFoundError!

# ✅ Use Python's built-in list comprehensions
all_items = _input.all()

# Filter
active_items = [
    item for item in all_items
    if item["json"].get("status") == "active"
]

# Group by
from collections import defaultdict
grouped = defaultdict(list)

for item in all_items:
    category = item["json"].get("category", "other")
    grouped[category].append(item["json"])

# Aggregate
import statistics
amounts = [item["json"].get("amount", 0) for item in all_items]
total = sum(amounts)
average = statistics.mean(amounts) if amounts else 0

return [{
    "json": {
        "active_count": len(active_items),
        "grouped": dict(grouped),
        "total": total,
        "average": average
    }
}]
```

### Database Operations (No drivers)

```python
# ❌ Can't use database drivers
# import psycopg2  # ModuleNotFoundError!
# import pymongo   # ModuleNotFoundError!

# ✅ Use n8n database nodes instead
# Add Postgres/MySQL/MongoDB node BEFORE Code node
# Process results in Code node

db_results = _input.first()["json"]

return [{
    "json": {
        "record_count": len(db_results) if isinstance(db_results, list) else 1,
        "processed": True
    }
}]
```

---

## Complete Standard Library List

**Available** (commonly useful):
- json
- datetime, time
- re
- base64
- hashlib
- urllib.parse, urllib.request, urllib.error
- math
- random
- statistics
- collections (defaultdict, Counter, namedtuple)
- itertools
- functools
- operator
- string
- textwrap

**Available** (less common):
- os.path (path operations only)
- copy
- typing
- enum
- decimal
- fractions

**NOT Available** (external libraries):
- requests (HTTP)
- pandas (data analysis)
- numpy (numerical computing)
- bs4/beautifulsoup4 (HTML parsing)
- selenium (browser automation)
- psycopg2, pymongo, sqlalchemy (databases)
- flask, fastapi (web frameworks)
- pillow (image processing)
- openpyxl, xlsxwriter (Excel)

---

## Best Practices

### 1. Use Standard Library When Possible

```python
# ✅ GOOD: Use standard library
import json
import datetime
import re

data = _input.first()["json"]
processed = json.loads(data.get("json_string", "{}"))

return [{"json": processed}]
```

### 2. Fall Back to n8n Nodes

```python
# For operations requiring external libraries,
# use n8n nodes instead:
# - HTTP Request for API calls
# - Postgres/MySQL for databases
# - Extract from File for parsing

# Then process results in Code node
result = _input.first()["json"]
return [{"json": {"processed": result}}]
```

### 3. Combine Multiple Modules

```python
import json
import base64
import hashlib
from datetime import datetime

# Combine modules for complex operations
data = _input.first()["json"]["body"]

# Hash sensitive data
user_id = hashlib.sha256(data.get("email", "").encode()).hexdigest()[:16]

# Encode for storage
encoded_data = base64.b64encode(json.dumps(data).encode()).decode()

return [{
    "json": {
        "user_id": user_id,
        "encoded_data": encoded_data,
        "timestamp": datetime.now().isoformat()
    }
}]
```

---

## Summary

**Most Useful Modules**:
1. json - Parse/generate JSON
2. datetime - Date operations
3. re - Regular expressions
4. base64 - Encoding
5. hashlib - Hashing
6. urllib.parse - URL operations

**Critical Limitation**:
- NO external libraries (requests, pandas, numpy, etc.)

**Recommended Approach**:
- Use **JavaScript** for 95% of use cases
- Use Python only when specifically needed
- Use n8n nodes for operations requiring external libraries

**See Also**:
- [SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) - Python Code overview
- [DATA_ACCESS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/drugbank_database/references/data_access.md) - Data access patterns
- [COMMON_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/frontend_dev_guidelines/resources/common_patterns.md) - Production patterns
- [ERROR_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/development/render_deploy/references/error_patterns.md) - Avoid common mistakes
```

## File: `skills/n8n-expression-syntax/COMMON_MISTAKES.md`
```markdown
# Common n8n Expression Mistakes

Complete catalog of expression errors with explanations and fixes.

---

## 1. Missing Curly Braces

**Problem**: Expression not recognized, shows as literal text

❌ **Wrong**:
```
$json.email
```

✅ **Correct**:
```
{{$json.email}}
```

**Why it fails**: n8n treats text without {{ }} as a literal string. Expressions must be wrapped to be evaluated.

**How to identify**: Field shows exact text like "$json.email" instead of actual value.

---

## 2. Webhook Body Access

**Problem**: Undefined values when accessing webhook data

❌ **Wrong**:
```
{{$json.name}}
{{$json.email}}
{{$json.message}}
```

✅ **Correct**:
```
{{$json.body.name}}
{{$json.body.email}}
{{$json.body.message}}
```

**Why it fails**: Webhook node wraps incoming data under `.body` property. The root `$json` contains headers, params, query, and body.

**Webhook structure**:
```javascript
{
  "headers": {...},
  "params": {...},
  "query": {...},
  "body": {         // User data is HERE!
    "name": "John",
    "email": "john@example.com"
  }
}
```

**How to identify**: Webhook workflow shows "undefined" for fields that are definitely being sent.

---

## 3. Spaces in Field Names

**Problem**: Syntax error or undefined value

❌ **Wrong**:
```
{{$json.first name}}
{{$json.user data.email}}
```

✅ **Correct**:
```
{{$json['first name']}}
{{$json['user data'].email}}
```

**Why it fails**: Spaces break dot notation. JavaScript interprets space as end of property name.

**How to identify**: Error message about unexpected token, or undefined when field exists.

---

## 4. Spaces in Node Names

**Problem**: Cannot access other node's data

❌ **Wrong**:
```
{{$node.HTTP Request.json.data}}
{{$node.Respond to Webhook.json}}
```

✅ **Correct**:
```
{{$node["HTTP Request"].json.data}}
{{$node["Respond to Webhook"].json}}
```

**Why it fails**: Node names are treated as object property names and need quotes when they contain spaces.

**How to identify**: Error like "Cannot read property 'Request' of undefined"

---

## 5. Incorrect Node Reference Case

**Problem**: Undefined or wrong data returned

❌ **Wrong**:
```
{{$node["http request"].json.data}}  // lowercase
{{$node["Http Request"].json.data}}  // wrong capitalization
```

✅ **Correct**:
```
{{$node["HTTP Request"].json.data}}  // exact match
```

**Why it fails**: Node names are **case-sensitive**. Must match exactly as shown in workflow.

**How to identify**: Undefined value even though node exists and has data.

---

## 6. Double Wrapping

**Problem**: Literal {{ }} appears in output

❌ **Wrong**:
```
{{{$json.field}}}
```

✅ **Correct**:
```
{{$json.field}}
```

**Why it fails**: Only one set of {{ }} is needed. Extra braces are treated as literal characters.

**How to identify**: Output shows "{{value}}" instead of just "value".

---

## 7. Array Access with Dots

**Problem**: Syntax error or undefined

❌ **Wrong**:
```
{{$json.items.0.name}}
{{$json.users.1.email}}
```

✅ **Correct**:
```
{{$json.items[0].name}}
{{$json.users[1].email}}
```

**Why it fails**: Array indices require brackets, not dots. Number after dot is invalid JavaScript.

**How to identify**: Syntax error or "Cannot read property '0' of undefined"

---

## 8. Using Expressions in Code Nodes

**Problem**: Literal string instead of value, or errors

❌ **Wrong (in Code node)**:
```javascript
const email = '{{$json.email}}';
const name = '={{$json.body.name}}';
```

✅ **Correct (in Code node)**:
```javascript
const email = $json.email;
const name = $json.body.name;

// Or using Code node API
const email = $input.item.json.email;
const allItems = $input.all();
```

**Why it fails**: Code nodes have **direct access** to data. The {{ }} syntax is for expression fields in other nodes, not for JavaScript code.

**How to identify**: Literal string "{{$json.email}}" appears in Code node output instead of actual value.

---

## 9. Missing Quotes in $node Reference

**Problem**: Syntax error

❌ **Wrong**:
```
{{$node[HTTP Request].json.data}}
```

✅ **Correct**:
```
{{$node["HTTP Request"].json.data}}
```

**Why it fails**: Node names must be quoted strings inside brackets.

**How to identify**: Syntax error "Unexpected identifier"

---

## 10. Incorrect Property Path

**Problem**: Undefined value

❌ **Wrong**:
```
{{$json.data.items.name}}       // items is an array
{{$json.user.email}}            // user doesn't exist, it's userData
```

✅ **Correct**:
```
{{$json.data.items[0].name}}    // access array element
{{$json.userData.email}}        // correct property name
```

**Why it fails**: Wrong path to data. Arrays need index, property names must be exact.

**How to identify**: Check actual data structure using expression editor preview.

---

## 11. Using = Prefix Outside JSON

**Problem**: Literal "=" appears in output

❌ **Wrong (in text field)**:
```
Email: ={{$json.email}}
```

✅ **Correct (in text field)**:
```
Email: {{$json.email}}
```

**Note**: The `=` prefix is **only** needed in JSON mode or when you want to set entire field value to expression result:

```javascript
// JSON mode (set property to expression)
{
  "email": "={{$json.body.email}}"
}

// Text mode (no = needed)
Hello {{$json.body.name}}!
```

**Why it fails**: The `=` is parsed as literal text in non-JSON contexts.

**How to identify**: Output shows "=john@example.com" instead of "john@example.com"

---

## 12. Expressions in Webhook Path

**Problem**: Path doesn't update, validation error

❌ **Wrong**:
```
path: "{{$json.user_id}}/webhook"
path: "users/={{$env.TENANT_ID}}"
```

✅ **Correct**:
```
path: "my-webhook"              // Static paths only
path: "user-webhook/:userId"    // Use dynamic URL parameters instead
```

**Why it fails**: Webhook paths must be static. Use dynamic URL parameters (`:paramName`) instead of expressions.

**How to identify**: Webhook path doesn't change or validation warns about invalid path.

---

## 13. Forgetting .json in $node Reference

**Problem**: Undefined or wrong data

❌ **Wrong**:
```
{{$node["HTTP Request"].data}}          // Missing .json
{{$node["Webhook"].body.email}}         // Missing .json
```

✅ **Correct**:
```
{{$node["HTTP Request"].json.data}}
{{$node["Webhook"].json.body.email}}
```

**Why it fails**: Node data is always under `.json` property (or `.binary` for binary data).

**How to identify**: Undefined value when you know the node has data.

---

## 14. String Concatenation Confusion

**Problem**: Attempting JavaScript template literals

❌ **Wrong**:
```
`Hello ${$json.name}!`          // Template literal syntax
"Hello " + $json.name + "!"     // String concatenation
```

✅ **Correct**:
```
Hello {{$json.name}}!           // n8n expressions auto-concatenate
```

**Why it fails**: n8n expressions don't use JavaScript template literal syntax. Adjacent text and expressions are automatically concatenated.

**How to identify**: Literal backticks or + symbols appear in output.

---

## 15. Empty Expression Brackets

**Problem**: Literal {{}} in output

❌ **Wrong**:
```
{{}}
{{ }}
```

✅ **Correct**:
```
{{$json.field}}                 // Include expression content
```

**Why it fails**: Empty expression brackets have nothing to evaluate.

**How to identify**: Literal "{{ }}" text appears in output.

---

## Quick Reference Table

| Error | Symptom | Fix |
|-------|---------|-----|
| No {{ }} | Literal text | Add {{ }} |
| Webhook data | Undefined | Add `.body` |
| Space in field | Syntax error | Use `['field name']` |
| Space in node | Undefined | Use `["Node Name"]` |
| Wrong case | Undefined | Match exact case |
| Double {{ }} | Literal braces | Remove extra {{ }} |
| .0 array | Syntax error | Use [0] |
| {{ }} in Code | Literal string | Remove {{ }} |
| No quotes in $node | Syntax error | Add quotes |
| Wrong path | Undefined | Check data structure |
| = in text | Literal = | Remove = prefix |
| Dynamic path | Doesn't work | Use static path |
| Missing .json | Undefined | Add .json |
| Template literals | Literal text | Use {{ }} |
| Empty {{ }} | Literal braces | Add expression |

---

## Debugging Process

When expression doesn't work:

1. **Check braces**: Is it wrapped in {{ }}?
2. **Check data source**: Is it webhook data? Add `.body`
3. **Check spaces**: Field or node name has spaces? Use brackets
4. **Check case**: Does node name match exactly?
5. **Check path**: Is the property path correct?
6. **Use expression editor**: Preview shows actual result
7. **Check context**: Is it a Code node? Remove {{ }}

---

**Related**: See [EXAMPLES.md](EXAMPLES.md) for working examples of correct syntax.
```

## File: `skills/n8n-expression-syntax/EXAMPLES.md`
```markdown
# n8n Expression Examples

Real working examples from n8n workflows.

---

## Example 1: Webhook Form Submission

**Scenario**: Form submission webhook posts to Slack

**Workflow**: Webhook → Slack

**Webhook Input** (POST):
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "company": "Acme Corp",
  "message": "Interested in your product"
}
```

**Webhook Node Output**:
```json
{
  "headers": {"content-type": "application/json"},
  "params": {},
  "query": {},
  "body": {
    "name": "John Doe",
    "email": "john@example.com",
    "company": "Acme Corp",
    "message": "Interested in your product"
  }
}
```

**In Slack Node** (text field):
```
New form submission! 📝

Name: {{$json.body.name}}
Email: {{$json.body.email}}
Company: {{$json.body.company}}
Message: {{$json.body.message}}
```

**Output**:
```
New form submission! 📝

Name: John Doe
Email: john@example.com
Company: Acme Corp
Message: Interested in your product
```

---

## Example 2: HTTP API to Database

**Scenario**: Fetch user data from API and insert into database

**Workflow**: Schedule → HTTP Request → Postgres

**HTTP Request Returns**:
```json
{
  "data": {
    "users": [
      {
        "id": 123,
        "name": "Alice Smith",
        "email": "alice@example.com",
        "role": "admin"
      }
    ]
  }
}
```

**In Postgres Node** (INSERT statement):
```sql
INSERT INTO users (user_id, name, email, role, synced_at)
VALUES (
  {{$json.data.users[0].id}},
  '{{$json.data.users[0].name}}',
  '{{$json.data.users[0].email}}',
  '{{$json.data.users[0].role}}',
  '{{$now.toFormat('yyyy-MM-dd HH:mm:ss')}}'
)
```

**Result**: User inserted with current timestamp

---

## Example 3: Multi-Node Data Flow

**Scenario**: Webhook → HTTP Request → Email

**Workflow Structure**:
1. Webhook receives order ID
2. HTTP Request fetches order details
3. Email sends confirmation

### Node 1: Webhook

**Receives**:
```json
{
  "body": {
    "order_id": "ORD-12345"
  }
}
```

### Node 2: HTTP Request

**URL field**:
```
https://api.example.com/orders/{{$json.body.order_id}}
```

**Returns**:
```json
{
  "order": {
    "id": "ORD-12345",
    "customer": "Bob Jones",
    "total": 99.99,
    "items": ["Widget", "Gadget"]
  }
}
```

### Node 3: Email

**Subject**:
```
Order {{$node["Webhook"].json.body.order_id}} Confirmed
```

**Body**:
```
Dear {{$node["HTTP Request"].json.order.customer}},

Your order {{$node["Webhook"].json.body.order_id}} has been confirmed!

Total: ${{$node["HTTP Request"].json.order.total}}
Items: {{$node["HTTP Request"].json.order.items.join(', ')}}

Thank you for your purchase!
```

**Email Result**:
```
Subject: Order ORD-12345 Confirmed

Dear Bob Jones,

Your order ORD-12345 has been confirmed!

Total: $99.99
Items: Widget, Gadget

Thank you for your purchase!
```

---

## Example 4: Date Formatting

**Scenario**: Various date format outputs

**Current Time**: 2025-10-20 14:30:45

### ISO Format
```javascript
{{$now.toISO()}}
```
**Output**: `2025-10-20T14:30:45.000Z`

### Custom Date Format
```javascript
{{$now.toFormat('yyyy-MM-dd')}}
```
**Output**: `2025-10-20`

### Time Only
```javascript
{{$now.toFormat('HH:mm:ss')}}
```
**Output**: `14:30:45`

### Full Readable Format
```javascript
{{$now.toFormat('MMMM dd, yyyy')}}
```
**Output**: `October 20, 2025`

### Date Math - Future
```javascript
{{$now.plus({days: 7}).toFormat('yyyy-MM-dd')}}
```
**Output**: `2025-10-27`

### Date Math - Past
```javascript
{{$now.minus({hours: 24}).toFormat('yyyy-MM-dd HH:mm')}}
```
**Output**: `2025-10-19 14:30`

---

## Example 5: Array Operations

**Data**:
```json
{
  "users": [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"}
  ]
}
```

### First User
```javascript
{{$json.users[0].name}}
```
**Output**: `Alice`

### Last User
```javascript
{{$json.users[$json.users.length - 1].name}}
```
**Output**: `Charlie`

### All Emails (Join)
```javascript
{{$json.users.map(u => u.email).join(', ')}}
```
**Output**: `alice@example.com, bob@example.com, charlie@example.com`

### Array Length
```javascript
{{$json.users.length}}
```
**Output**: `3`

---

## Example 6: Conditional Logic

**Data**:
```json
{
  "order": {
    "status": "completed",
    "total": 150
  }
}
```

### Ternary Operator
```javascript
{{$json.order.status === 'completed' ? 'Order Complete ✓' : 'Pending...'}}
```
**Output**: `Order Complete ✓`

### Default Values
```javascript
{{$json.order.notes || 'No notes provided'}}
```
**Output**: `No notes provided` (if notes field doesn't exist)

### Multiple Conditions
```javascript
{{$json.order.total > 100 ? 'Premium Customer' : 'Standard Customer'}}
```
**Output**: `Premium Customer`

---

## Example 7: String Manipulation

**Data**:
```json
{
  "user": {
    "email": "JOHN@EXAMPLE.COM",
    "message": "  Hello World  "
  }
}
```

### Lowercase
```javascript
{{$json.user.email.toLowerCase()}}
```
**Output**: `john@example.com`

### Uppercase
```javascript
{{$json.user.message.toUpperCase()}}
```
**Output**: `  HELLO WORLD  `

### Trim
```javascript
{{$json.user.message.trim()}}
```
**Output**: `Hello World`

### Substring
```javascript
{{$json.user.email.substring(0, 4)}}
```
**Output**: `JOHN`

### Replace
```javascript
{{$json.user.message.replace('World', 'n8n')}}
```
**Output**: `  Hello n8n  `

---

## Example 8: Fields with Spaces

**Data**:
```json
{
  "user data": {
    "first name": "Jane",
    "last name": "Doe",
    "phone number": "+1234567890"
  }
}
```

### Bracket Notation
```javascript
{{$json['user data']['first name']}}
```
**Output**: `Jane`

### Combined
```javascript
{{$json['user data']['first name']}} {{$json['user data']['last name']}}
```
**Output**: `Jane Doe`

### Nested Spaces
```javascript
Contact: {{$json['user data']['phone number']}}
```
**Output**: `Contact: +1234567890`

---

## Example 9: Code Node (Direct Access)

**Code Node**: Transform webhook data

**Input** (from Webhook node):
```json
{
  "body": {
    "items": ["apple", "banana", "cherry"]
  }
}
```

**Code** (JavaScript):
```javascript
// ✅ Direct access (no {{ }})
const items = $json.body.items;

// Transform to uppercase
const uppercased = items.map(item => item.toUpperCase());

// Return in n8n format
return [{
  json: {
    original: items,
    transformed: uppercased,
    count: items.length
  }
}];
```

**Output**:
```json
{
  "original": ["apple", "banana", "cherry"],
  "transformed": ["APPLE", "BANANA", "CHERRY"],
  "count": 3
}
```

---

## Example 10: Environment Variables

**Setup**: Environment variable `API_KEY=secret123`

### In HTTP Request (Headers)
```javascript
Authorization: Bearer {{$env.API_KEY}}
```
**Result**: `Authorization: Bearer secret123`

### In URL
```javascript
https://api.example.com/data?key={{$env.API_KEY}}
```
**Result**: `https://api.example.com/data?key=secret123`

---

## Template from Real Workflow

**Based on n8n template #2947** (Weather to Slack)

### Workflow Structure
Webhook → OpenStreetMap API → Weather API → Slack

### Webhook Slash Command
**Input**: `/weather London`

**Webhook receives**:
```json
{
  "body": {
    "text": "London"
  }
}
```

### OpenStreetMap API
**URL**:
```
https://nominatim.openstreetmap.org/search?q={{$json.body.text}}&format=json
```

### Weather API (NWS)
**URL**:
```
https://api.weather.gov/points/{{$node["OpenStreetMap"].json[0].lat}},{{$node["OpenStreetMap"].json[0].lon}}
```

### Slack Message
```
Weather for {{$json.body.text}}:

Temperature: {{$node["Weather API"].json.properties.temperature.value}}°C
Conditions: {{$node["Weather API"].json.properties.shortForecast}}
```

---

## Summary

**Key Patterns**:
1. Webhook data is under `.body`
2. Use `{{}}` for expressions (except Code nodes)
3. Reference other nodes with `$node["Node Name"].json`
4. Use brackets for field names with spaces
5. Node names are case-sensitive

**Most Common Uses**:
- `{{$json.body.field}}` - Webhook data
- `{{$node["Name"].json.field}}` - Other node data
- `{{$now.toFormat('yyyy-MM-dd')}}` - Timestamps
- `{{$json.array[0].field}}` - Array access
- `{{$json.field || 'default'}}` - Default values

---

**Related**: See [COMMON_MISTAKES.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/creative_design/c4_architecture/references/common_mistakes.md) for error examples and fixes.
```

## File: `skills/n8n-expression-syntax/README.md`
```markdown
# n8n Expression Syntax

Expert guide for writing correct n8n expressions in workflows.

---

## Purpose

Teaches correct n8n expression syntax ({{ }} patterns) and fixes common mistakes, especially the critical webhook data structure gotcha.

## Activates On

- expression
- {{}} syntax
- $json, $node, $now, $env
- webhook data
- troubleshoot expression error
- undefined in workflow

## File Count

4 files, ~450 lines total

## Dependencies

**n8n-mcp tools**:
- None directly (syntax knowledge skill)
- Works with n8n-mcp validation tools

**Related skills**:
- n8n Workflow Patterns (uses expressions in examples)
- n8n MCP Tools Expert (validates expressions)
- n8n Node Configuration (when expressions are needed)

## Coverage

### Core Topics
- Expression format ({{ }})
- Core variables ($json, $node, $now, $env)
- **Webhook data structure** ($json.body.*)
- When NOT to use expressions (Code nodes)

### Common Patterns
- Accessing nested fields
- Referencing other nodes
- Array and object access
- Date/time formatting
- String manipulation

### Error Prevention
- 15 common mistakes with fixes
- Quick reference table
- Debugging process

## Evaluations

4 scenarios (100% coverage expected):
1. **eval-001**: Missing curly braces
2. **eval-002**: Webhook body data access (critical!)
3. **eval-003**: Code node vs expression confusion
4. **eval-004**: Node reference syntax

## Key Features

✅ **Critical Gotcha Highlighted**: Webhook data under `.body`
✅ **Real Examples**: From MCP testing and real templates
✅ **Quick Fixes Table**: Fast reference for common errors
✅ **Code vs Expression**: Clear distinction
✅ **Comprehensive**: Covers 95% of expression use cases

## Files

- **SKILL.md** (285 lines) - Main content with all essential knowledge
- **COMMON_MISTAKES.md** (380 lines) - Complete error catalog with 15 common mistakes
- **EXAMPLES.md** (450 lines) - 10 real working examples
- **README.md** (this file) - Skill metadata

## Success Metrics

**Expected outcomes**:
- Users correctly wrap expressions in {{ }}
- Zero webhook `.body` access errors
- No expressions used in Code nodes
- Correct $node reference syntax

## Last Updated

2025-10-20

---

**Part of**: n8n-skills repository
**Conceived by**: Romuald Członkowski - [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)
```

## File: `skills/n8n-expression-syntax/SKILL.md`
```markdown
---
name: n8n-expression-syntax
description: Validate n8n expression syntax and fix common errors. Use when writing n8n expressions, using {{}} syntax, accessing $json/$node variables, troubleshooting expression errors, or working with webhook data in workflows.
---

# n8n Expression Syntax

Expert guide for writing correct n8n expressions in workflows.

---

## Expression Format

All dynamic content in n8n uses **double curly braces**:

```
{{expression}}
```

**Examples**:
```
✅ {{$json.email}}
✅ {{$json.body.name}}
✅ {{$node["HTTP Request"].json.data}}
❌ $json.email  (no braces - treated as literal text)
❌ {$json.email}  (single braces - invalid)
```

---

## Core Variables

### $json - Current Node Output

Access data from the current node:

```javascript
{{$json.fieldName}}
{{$json['field with spaces']}}
{{$json.nested.property}}
{{$json.items[0].name}}
```

### $node - Reference Other Nodes

Access data from any previous node:

```javascript
{{$node["Node Name"].json.fieldName}}
{{$node["HTTP Request"].json.data}}
{{$node["Webhook"].json.body.email}}
```

**Important**:
- Node names **must** be in quotes
- Node names are **case-sensitive**
- Must match exact node name from workflow

### $now - Current Timestamp

Access current date/time:

```javascript
{{$now}}
{{$now.toFormat('yyyy-MM-dd')}}
{{$now.toFormat('HH:mm:ss')}}
{{$now.plus({days: 7})}}
```

### $env - Environment Variables

Access environment variables:

```javascript
{{$env.API_KEY}}
{{$env.DATABASE_URL}}
```

---

## 🚨 CRITICAL: Webhook Data Structure

**Most Common Mistake**: Webhook data is **NOT** at the root!

### Webhook Node Output Structure

```javascript
{
  "headers": {...},
  "params": {...},
  "query": {...},
  "body": {           // ⚠️ USER DATA IS HERE!
    "name": "John",
    "email": "john@example.com",
    "message": "Hello"
  }
}
```

### Correct Webhook Data Access

```javascript
❌ WRONG: {{$json.name}}
❌ WRONG: {{$json.email}}

✅ CORRECT: {{$json.body.name}}
✅ CORRECT: {{$json.body.email}}
✅ CORRECT: {{$json.body.message}}
```

**Why**: Webhook node wraps incoming data under `.body` property to preserve headers, params, and query parameters.

---

## Common Patterns

### Access Nested Fields

```javascript
// Simple nesting
{{$json.user.email}}

// Array access
{{$json.data[0].name}}
{{$json.items[0].id}}

// Bracket notation for spaces
{{$json['field name']}}
{{$json['user data']['first name']}}
```

### Reference Other Nodes

```javascript
// Node without spaces
{{$node["Set"].json.value}}

// Node with spaces (common!)
{{$node["HTTP Request"].json.data}}
{{$node["Respond to Webhook"].json.message}}

// Webhook node
{{$node["Webhook"].json.body.email}}
```

### Combine Variables

```javascript
// Concatenation (automatic)
Hello {{$json.body.name}}!

// In URLs
https://api.example.com/users/{{$json.body.user_id}}

// In object properties
{
  "name": "={{$json.body.name}}",
  "email": "={{$json.body.email}}"
}
```

---

## When NOT to Use Expressions

### ❌ Code Nodes

Code nodes use **direct JavaScript access**, NOT expressions!

```javascript
// ❌ WRONG in Code node
const email = '={{$json.email}}';
const name = '{{$json.body.name}}';

// ✅ CORRECT in Code node
const email = $json.email;
const name = $json.body.name;

// Or using Code node API
const email = $input.item.json.email;
const allItems = $input.all();
```

### ❌ Webhook Paths

```javascript
// ❌ WRONG
path: "{{$json.user_id}}/webhook"

// ✅ CORRECT
path: "user-webhook"  // Static paths only
```

### ❌ Credential Fields

```javascript
// ❌ WRONG
apiKey: "={{$env.API_KEY}}"

// ✅ CORRECT
Use n8n credential system, not expressions
```

---

## Validation Rules

### 1. Always Use {{}}

Expressions **must** be wrapped in double curly braces.

```javascript
❌ $json.field
✅ {{$json.field}}
```

### 2. Use Quotes for Spaces

Field or node names with spaces require **bracket notation**:

```javascript
❌ {{$json.field name}}
✅ {{$json['field name']}}

❌ {{$node.HTTP Request.json}}
✅ {{$node["HTTP Request"].json}}
```

### 3. Match Exact Node Names

Node references are **case-sensitive**:

```javascript
❌ {{$node["http request"].json}}  // lowercase
❌ {{$node["Http Request"].json}}  // wrong case
✅ {{$node["HTTP Request"].json}}  // exact match
```

### 4. No Nested {{}}

Don't double-wrap expressions:

```javascript
❌ {{{$json.field}}}
✅ {{$json.field}}
```

---

## Common Mistakes

For complete error catalog with fixes, see [COMMON_MISTAKES.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/creative_design/c4_architecture/references/common_mistakes.md)

### Quick Fixes

| Mistake | Fix |
|---------|-----|
| `$json.field` | `{{$json.field}}` |
| `{{$json.field name}}` | `{{$json['field name']}}` |
| `{{$node.HTTP Request}}` | `{{$node["HTTP Request"]}}` |
| `{{{$json.field}}}` | `{{$json.field}}` |
| `{{$json.name}}` (webhook) | `{{$json.body.name}}` |
| `'={{$json.email}}'` (Code node) | `$json.email` |

---

## Working Examples

For real workflow examples, see [EXAMPLES.md](EXAMPLES.md)

### Example 1: Webhook to Slack

**Webhook receives**:
```json
{
  "body": {
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hello!"
  }
}
```

**In Slack node text field**:
```
New form submission!

Name: {{$json.body.name}}
Email: {{$json.body.email}}
Message: {{$json.body.message}}
```

### Example 2: HTTP Request to Email

**HTTP Request returns**:
```json
{
  "data": {
    "items": [
      {"name": "Product 1", "price": 29.99}
    ]
  }
}
```

**In Email node** (reference HTTP Request):
```
Product: {{$node["HTTP Request"].json.data.items[0].name}}
Price: ${{$node["HTTP Request"].json.data.items[0].price}}
```

### Example 3: Format Timestamp

```javascript
// Current date
{{$now.toFormat('yyyy-MM-dd')}}
// Result: 2025-10-20

// Time
{{$now.toFormat('HH:mm:ss')}}
// Result: 14:30:45

// Full datetime
{{$now.toFormat('yyyy-MM-dd HH:mm')}}
// Result: 2025-10-20 14:30
```

---

## Data Type Handling

### Arrays

```javascript
// First item
{{$json.users[0].email}}

// Array length
{{$json.users.length}}

// Last item
{{$json.users[$json.users.length - 1].name}}
```

### Objects

```javascript
// Dot notation (no spaces)
{{$json.user.email}}

// Bracket notation (with spaces or dynamic)
{{$json['user data'].email}}
```

### Strings

```javascript
// Concatenation (automatic)
Hello {{$json.name}}!

// String methods
{{$json.email.toLowerCase()}}
{{$json.name.toUpperCase()}}
```

### Numbers

```javascript
// Direct use
{{$json.price}}

// Math operations
{{$json.price * 1.1}}  // Add 10%
{{$json.quantity + 5}}
```

---

## Advanced Patterns

### Conditional Content

```javascript
// Ternary operator
{{$json.status === 'active' ? 'Active User' : 'Inactive User'}}

// Default values
{{$json.email || 'no-email@example.com'}}
```

### Date Manipulation

```javascript
// Add days
{{$now.plus({days: 7}).toFormat('yyyy-MM-dd')}}

// Subtract hours
{{$now.minus({hours: 24}).toISO()}}

// Set specific date
{{DateTime.fromISO('2025-12-25').toFormat('MMMM dd, yyyy')}}
```

### String Manipulation

```javascript
// Substring
{{$json.email.substring(0, 5)}}

// Replace
{{$json.message.replace('old', 'new')}}

// Split and join
{{$json.tags.split(',').join(', ')}}
```

---

## Debugging Expressions

### Test in Expression Editor

1. Click field with expression
2. Open expression editor (click "fx" icon)
3. See live preview of result
4. Check for errors highlighted in red

### Common Error Messages

**"Cannot read property 'X' of undefined"**
→ Parent object doesn't exist
→ Check your data path

**"X is not a function"**
→ Trying to call method on non-function
→ Check variable type

**Expression shows as literal text**
→ Missing {{ }}
→ Add curly braces

---

## Expression Helpers

### Available Methods

**String**:
- `.toLowerCase()`, `.toUpperCase()`
- `.trim()`, `.replace()`, `.substring()`
- `.split()`, `.includes()`

**Array**:
- `.length`, `.map()`, `.filter()`
- `.find()`, `.join()`, `.slice()`

**DateTime** (Luxon):
- `.toFormat()`, `.toISO()`, `.toLocal()`
- `.plus()`, `.minus()`, `.set()`

**Number**:
- `.toFixed()`, `.toString()`
- Math operations: `+`, `-`, `*`, `/`, `%`

---

## Best Practices

### ✅ Do

- Always use {{ }} for dynamic content
- Use bracket notation for field names with spaces
- Reference webhook data from `.body`
- Use $node for data from other nodes
- Test expressions in expression editor

### ❌ Don't

- Don't use expressions in Code nodes
- Don't forget quotes around node names with spaces
- Don't double-wrap with extra {{ }}
- Don't assume webhook data is at root (it's under .body!)
- Don't use expressions in webhook paths or credentials

---

## Related Skills

- **n8n MCP Tools Expert**: Learn how to validate expressions using MCP tools
- **n8n Workflow Patterns**: See expressions in real workflow examples
- **n8n Node Configuration**: Understand when expressions are needed

---

## Summary

**Essential Rules**:
1. Wrap expressions in {{ }}
2. Webhook data is under `.body`
3. No {{ }} in Code nodes
4. Quote node names with spaces
5. Node names are case-sensitive

**Most Common Mistakes**:
- Missing {{ }} → Add braces
- `{{$json.name}}` in webhooks → Use `{{$json.body.name}}`
- `{{$json.email}}` in Code → Use `$json.email`
- `{{$node.HTTP Request}}` → Use `{{$node["HTTP Request"]}}`

For more details, see:
- [COMMON_MISTAKES.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/creative_design/c4_architecture/references/common_mistakes.md) - Complete error catalog
- [EXAMPLES.md](EXAMPLES.md) - Real workflow examples

---

**Need Help?** Reference the n8n expression documentation or use n8n-mcp validation tools to check your expressions.
```

## File: `skills/n8n-mcp-tools-expert/README.md`
```markdown
# n8n MCP Tools Expert

Expert guide for using n8n-mcp MCP tools effectively.

---

## Purpose

Teaches how to use n8n-mcp MCP server tools correctly for efficient workflow building.

## Activates On

- search nodes
- find node
- validate
- MCP tools
- template
- workflow
- n8n-mcp
- tool selection

## File Count

5 files, ~1,150 lines total

## Priority

**HIGHEST** - Essential for correct MCP tool usage

## Dependencies

**n8n-mcp tools**: All of them! (40+ tools)

**Related skills**:
- n8n Expression Syntax (write expressions for workflows)
- n8n Workflow Patterns (use tools to build patterns)
- n8n Validation Expert (interpret validation results)
- n8n Node Configuration (configure nodes found with tools)

## Coverage

### Core Topics
- Tool selection guide (which tool for which task)
- nodeType format differences (nodes-base.* vs n8n-nodes-base.*)
- Validation profiles (minimal/runtime/ai-friendly/strict)
- Smart parameters (branch, case for multi-output nodes)
- Auto-sanitization system
- Workflow management (18 operation types)
- AI connection types (8 types)

### Tool Categories
- Node Discovery (search_nodes, get_node with detail levels and modes)
- Configuration Validation (minimal, operation, workflow)
- Workflow Management (create, update, validate)
- Template Library (search, get)
- Documentation (tools, database stats)

## Evaluations

5 scenarios (100% coverage expected):
1. **eval-001**: Tool selection (search_nodes)
2. **eval-002**: nodeType format (nodes-base.* prefix)
3. **eval-003**: Validation workflow (profiles)
4. **eval-004**: standard vs full detail (1-2KB vs 3-8KB)
5. **eval-005**: Smart parameters (branch, case)

## Key Features

✅ **Tool Selection Guide**: Which tool to use for each task
✅ **Common Patterns**: Most effective tool usage sequences
✅ **Format Guidance**: nodeType format differences explained
✅ **Smart Parameters**: Semantic branch/case routing for multi-output nodes
✅ **Auto-Sanitization**: Explains automatic validation fixes
✅ **Comprehensive**: Covers all 40+ MCP tools

## Files

- **SKILL.md** (480 lines) - Core tool usage guide
- **SEARCH_GUIDE.md** (220 lines) - Node discovery tools
- **VALIDATION_GUIDE.md** (250 lines) - Validation tools and profiles
- **WORKFLOW_GUIDE.md** (200 lines) - Workflow management
- **README.md** (this file) - Skill metadata

## What You'll Learn

- Correct nodeType formats (nodes-base.* for search tools)
- When to use get_node vs get_node({detail: "full"})
- How to use validation profiles effectively
- Smart parameters for multi-output nodes (IF/Switch)
- Common tool usage patterns and workflows

## Last Updated

2025-10-20

---

**Part of**: n8n-skills repository
**Conceived by**: Romuald Członkowski - [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)
```

## File: `skills/n8n-mcp-tools-expert/SEARCH_GUIDE.md`
```markdown
# Node Discovery Tools Guide

Complete guide for finding and understanding n8n nodes.

---

## search_nodes (START HERE!)

**Speed**: <20ms

**Use when**: You know what you're looking for (keyword, service, use case)

**Syntax**:
```javascript
search_nodes({
  query: "slack",      // Required: search keywords
  mode: "OR",          // Optional: OR (default), AND, FUZZY
  limit: 20,           // Optional: max results (default 20)
  source: "all",       // Optional: all, core, community, verified
  includeExamples: false  // Optional: include template configs
})
```

**Returns**:
```javascript
{
  "query": "slack",
  "results": [
    {
      "nodeType": "nodes-base.slack",                    // For search/validate tools
      "workflowNodeType": "n8n-nodes-base.slack",       // For workflow tools
      "displayName": "Slack",
      "description": "Consume Slack API",
      "category": "output",
      "relevance": "high"
    }
  ]
}
```

**Tips**:
- Common searches: webhook, http, database, email, slack, google, ai
- `OR` mode (default): matches any word
- `AND` mode: requires all words
- `FUZZY` mode: typo-tolerant (finds "slak" → Slack)
- Use `source: "core"` for only built-in nodes
- Use `includeExamples: true` for real-world configs

---

## get_node (UNIFIED NODE INFORMATION)

The `get_node` tool provides all node information with different detail levels and modes.

### Detail Levels (mode="info")

| Detail | Tokens | Use When |
|--------|--------|----------|
| `minimal` | ~200 | Quick metadata check |
| `standard` | ~1-2K | **Most use cases (DEFAULT)** |
| `full` | ~3-8K | Complex debugging only |

### Standard Detail (RECOMMENDED)

**Speed**: <10ms | **Size**: ~1-2K tokens

**Use when**: You've found the node and need configuration details

```javascript
get_node({
  nodeType: "nodes-base.slack",      // Required: SHORT prefix format
  includeExamples: true              // Optional: get real template configs
})
// detail="standard" is the default
```

**Returns**:
- Available operations and resources
- Essential properties (10-20 most common)
- Metadata (isAITool, isTrigger, hasCredentials)
- Real examples from templates (if includeExamples: true)

### Minimal Detail

**Speed**: <5ms | **Size**: ~200 tokens

**Use when**: Just need basic metadata

```javascript
get_node({
  nodeType: "nodes-base.slack",
  detail: "minimal"
})
```

**Returns**: nodeType, displayName, description, category

### Full Detail (USE SPARINGLY)

**Speed**: <100ms | **Size**: ~3-8K tokens

**Use when**: Debugging complex configuration, need complete schema

```javascript
get_node({
  nodeType: "nodes-base.httpRequest",
  detail: "full"
})
```

**Warning**: Large payload! Use `standard` for most cases.

---

## get_node Modes

### mode="docs" (READABLE DOCUMENTATION)

**Use when**: Need human-readable documentation with examples

```javascript
get_node({
  nodeType: "nodes-base.slack",
  mode: "docs"
})
```

**Returns**: Formatted markdown with:
- Usage examples
- Authentication guide
- Common patterns
- Best practices

**Better than raw schema for learning!**

### mode="search_properties" (FIND SPECIFIC FIELDS)

**Use when**: Looking for specific property in a node

```javascript
get_node({
  nodeType: "nodes-base.httpRequest",
  mode: "search_properties",
  propertyQuery: "auth",           // Required for this mode
  maxPropertyResults: 20           // Optional: default 20
})
```

**Returns**: Property paths and descriptions matching query

**Common searches**: auth, header, body, json, url, method, credential

### mode="versions" (VERSION HISTORY)

**Use when**: Need to check node version history

```javascript
get_node({
  nodeType: "nodes-base.executeWorkflow",
  mode: "versions"
})
```

**Returns**: Version history with breaking changes flags

### mode="compare" (COMPARE VERSIONS)

**Use when**: Need to see differences between versions

```javascript
get_node({
  nodeType: "nodes-base.httpRequest",
  mode: "compare",
  fromVersion: "3.0",
  toVersion: "4.1"       // Optional: defaults to latest
})
```

**Returns**: Property-level changes between versions

### mode="breaking" (BREAKING CHANGES ONLY)

**Use when**: Checking for breaking changes before upgrades

```javascript
get_node({
  nodeType: "nodes-base.httpRequest",
  mode: "breaking",
  fromVersion: "3.0"
})
```

**Returns**: Only breaking changes (not all changes)

### mode="migrations" (AUTO-MIGRATABLE)

**Use when**: Checking what can be auto-migrated

```javascript
get_node({
  nodeType: "nodes-base.httpRequest",
  mode: "migrations",
  fromVersion: "3.0"
})
```

**Returns**: Changes that can be automatically migrated

---

## Additional Parameters

### includeTypeInfo

Add type structure metadata (validation rules, JS types)

```javascript
get_node({
  nodeType: "nodes-base.if",
  includeTypeInfo: true   // Adds ~80-120 tokens per property
})
```

Use for complex nodes like filter, resourceMapper

### includeExamples

Include real-world configuration examples from templates

```javascript
get_node({
  nodeType: "nodes-base.slack",
  includeExamples: true   // Adds ~200-400 tokens per example
})
```

Only works with `mode: "info"` and `detail: "standard"`

---

## Common Workflow: Finding & Configuring

```
Step 1: Search
search_nodes({query: "slack"})
→ Returns: nodes-base.slack

Step 2: Get Operations (18s avg thinking time)
get_node({
  nodeType: "nodes-base.slack",
  includeExamples: true
})
→ Returns: operations list + example configs

Step 3: Validate Config
validate_node({
  nodeType: "nodes-base.slack",
  config: {resource: "channel", operation: "create"},
  profile: "runtime"
})
→ Returns: validation result

Step 4: Use in Workflow
(Configuration ready!)
```

**Most common pattern**: search → get_node (18s average)

---

## Quick Comparison

| Tool/Mode | When to Use | Speed | Size |
|-----------|-------------|-------|------|
| `search_nodes` | Find by keyword | <20ms | Small |
| `get_node (standard)` | **Get config (DEFAULT)** | <10ms | 1-2K |
| `get_node (minimal)` | Quick metadata | <5ms | 200 |
| `get_node (full)` | Complex debugging | <100ms | 3-8K |
| `get_node (docs)` | Learn usage | Fast | Medium |
| `get_node (search_properties)` | Find specific field | Fast | Small |
| `get_node (versions)` | Check versions | Fast | Small |

**Best Practice**: search → get_node(standard) → validate

---

## nodeType Format (CRITICAL!)

**Search/Validate Tools** (SHORT prefix):
```javascript
"nodes-base.slack"
"nodes-base.httpRequest"
"nodes-langchain.agent"
```

**Workflow Tools** (FULL prefix):
```javascript
"n8n-nodes-base.slack"
"n8n-nodes-base.httpRequest"
"@n8n/n8n-nodes-langchain.agent"
```

**Conversion**: search_nodes returns BOTH formats:
```javascript
{
  "nodeType": "nodes-base.slack",          // Use with get_node, validate_node
  "workflowNodeType": "n8n-nodes-base.slack"  // Use with n8n_create_workflow
}
```

---

## Examples

### Find and Configure HTTP Request

```javascript
// Step 1: Search
search_nodes({query: "http request"})

// Step 2: Get standard info
get_node({nodeType: "nodes-base.httpRequest"})

// Step 3: Find auth options
get_node({
  nodeType: "nodes-base.httpRequest",
  mode: "search_properties",
  propertyQuery: "authentication"
})

// Step 4: Validate config
validate_node({
  nodeType: "nodes-base.httpRequest",
  config: {method: "POST", url: "https://api.example.com"},
  profile: "runtime"
})
```

### Explore AI Nodes

```javascript
// Find all AI-related nodes
search_nodes({query: "ai agent", source: "all"})

// Get AI Agent documentation
get_node({nodeType: "nodes-langchain.agent", mode: "docs"})

// Get configuration details with examples
get_node({
  nodeType: "nodes-langchain.agent",
  includeExamples: true
})
```

### Check Version Compatibility

```javascript
// See all versions
get_node({nodeType: "nodes-base.executeWorkflow", mode: "versions"})

// Check breaking changes from v1 to v2
get_node({
  nodeType: "nodes-base.executeWorkflow",
  mode: "breaking",
  fromVersion: "1.0"
})
```

---

## Related

- [VALIDATION_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_mcp_tools_expert/VALIDATION_GUIDE.md) - Validate node configs
- [WORKFLOW_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_game_studios/docs/workflow_guide.md) - Use nodes in workflows
```

## File: `skills/n8n-mcp-tools-expert/SKILL.md`
```markdown
---
name: n8n-mcp-tools-expert
description: Expert guide for using n8n-mcp MCP tools effectively. Use when searching for nodes, validating configurations, accessing templates, managing workflows, or using any n8n-mcp tool. Provides tool selection guidance, parameter formats, and common patterns.
---

# n8n MCP Tools Expert

Master guide for using n8n-mcp MCP server tools to build workflows.

---

## Tool Categories

n8n-mcp provides tools organized into categories:

1. **Node Discovery** → [SEARCH_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_mcp_tools_expert/SEARCH_GUIDE.md)
2. **Configuration Validation** → [VALIDATION_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_mcp_tools_expert/VALIDATION_GUIDE.md)
3. **Workflow Management** → [WORKFLOW_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_game_studios/docs/workflow_guide.md)
4. **Template Library** - Search and deploy 2,700+ real workflows
5. **Data Tables** - Manage n8n data tables and rows (`n8n_manage_datatable`)
6. **Documentation & Guides** - Tool docs, AI agent guide, Code node guides

---

## Quick Reference

### Most Used Tools (by success rate)

| Tool | Use When | Speed |
|------|----------|-------|
| `search_nodes` | Finding nodes by keyword | <20ms |
| `get_node` | Understanding node operations (detail="standard") | <10ms |
| `validate_node` | Checking configurations (mode="full") | <100ms |
| `n8n_create_workflow` | Creating workflows | 100-500ms |
| `n8n_update_partial_workflow` | Editing workflows (MOST USED!) | 50-200ms |
| `validate_workflow` | Checking complete workflow | 100-500ms |
| `n8n_deploy_template` | Deploy template to n8n instance | 200-500ms |
| `n8n_manage_datatable` | Managing data tables and rows | 50-500ms |
| `n8n_autofix_workflow` | Auto-fix validation errors | 200-1500ms |

---

## Tool Selection Guide

### Finding the Right Node

**Workflow**:
```
1. search_nodes({query: "keyword"})
2. get_node({nodeType: "nodes-base.name"})
3. [Optional] get_node({nodeType: "nodes-base.name", mode: "docs"})
```

**Example**:
```javascript
// Step 1: Search
search_nodes({query: "slack"})
// Returns: nodes-base.slack

// Step 2: Get details
get_node({nodeType: "nodes-base.slack"})
// Returns: operations, properties, examples (standard detail)

// Step 3: Get readable documentation
get_node({nodeType: "nodes-base.slack", mode: "docs"})
// Returns: markdown documentation
```

**Common pattern**: search → get_node (18s average)

### Validating Configuration

**Workflow**:
```
1. validate_node({nodeType, config: {}, mode: "minimal"}) - Check required fields
2. validate_node({nodeType, config, profile: "runtime"}) - Full validation
3. [Repeat] Fix errors, validate again
```

**Common pattern**: validate → fix → validate (23s thinking, 58s fixing per cycle)

### Managing Workflows

**Workflow**:
```
1. n8n_create_workflow({name, nodes, connections})
2. n8n_validate_workflow({id})
3. n8n_update_partial_workflow({id, operations: [...]})
4. n8n_validate_workflow({id}) again
5. n8n_update_partial_workflow({id, operations: [{type: "activateWorkflow"}]})
```

**Common pattern**: iterative updates (56s average between edits)

---

## Critical: nodeType Formats

**Two different formats** for different tools!

### Format 1: Search/Validate Tools
```javascript
// Use SHORT prefix
"nodes-base.slack"
"nodes-base.httpRequest"
"nodes-base.webhook"
"nodes-langchain.agent"
```

**Tools that use this**:
- search_nodes (returns this format)
- get_node
- validate_node
- validate_workflow

### Format 2: Workflow Tools
```javascript
// Use FULL prefix
"n8n-nodes-base.slack"
"n8n-nodes-base.httpRequest"
"n8n-nodes-base.webhook"
"@n8n/n8n-nodes-langchain.agent"
```

**Tools that use this**:
- n8n_create_workflow
- n8n_update_partial_workflow

### Conversion

```javascript
// search_nodes returns BOTH formats
{
  "nodeType": "nodes-base.slack",          // For search/validate tools
  "workflowNodeType": "n8n-nodes-base.slack"  // For workflow tools
}
```

---

## Common Mistakes

### Mistake 1: Wrong nodeType Format

**Problem**: "Node not found" error

```javascript
// WRONG
get_node({nodeType: "slack"})  // Missing prefix
get_node({nodeType: "n8n-nodes-base.slack"})  // Wrong prefix

// CORRECT
get_node({nodeType: "nodes-base.slack"})
```

### Mistake 2: Using detail="full" by Default

**Problem**: Huge payload, slower response, token waste

```javascript
// WRONG - Returns 3-8K tokens, use sparingly
get_node({nodeType: "nodes-base.slack", detail: "full"})

// CORRECT - Returns 1-2K tokens, covers 95% of use cases
get_node({nodeType: "nodes-base.slack"})  // detail="standard" is default
get_node({nodeType: "nodes-base.slack", detail: "standard"})
```

**When to use detail="full"**:
- Debugging complex configuration issues
- Need complete property schema with all nested options
- Exploring advanced features

**Better alternatives**:
1. `get_node({detail: "standard"})` - for operations list (default)
2. `get_node({mode: "docs"})` - for readable documentation
3. `get_node({mode: "search_properties", propertyQuery: "auth"})` - for specific property

### Mistake 3: Not Using Validation Profiles

**Problem**: Too many false positives OR missing real errors

**Profiles**:
- `minimal` - Only required fields (fast, permissive)
- `runtime` - Values + types (recommended for pre-deployment)
- `ai-friendly` - Reduce false positives (for AI configuration)
- `strict` - Maximum validation (for production)

```javascript
// WRONG - Uses default profile
validate_node({nodeType, config})

// CORRECT - Explicit profile
validate_node({nodeType, config, profile: "runtime"})
```

### Mistake 4: Ignoring Auto-Sanitization

**What happens**: ALL nodes sanitized on ANY workflow update

**Auto-fixes**:
- Binary operators (equals, contains) → removes singleValue
- Unary operators (isEmpty, isNotEmpty) → adds singleValue: true
- IF/Switch nodes → adds missing metadata

**Cannot fix**:
- Broken connections
- Branch count mismatches
- Paradoxical corrupt states

```javascript
// After ANY update, auto-sanitization runs on ALL nodes
n8n_update_partial_workflow({id, operations: [...]})
// → Automatically fixes operator structures
```

### Mistake 5: Not Using Smart Parameters

**Problem**: Complex sourceIndex calculations for multi-output nodes

**Old way** (manual):
```javascript
// IF node connection
{
  type: "addConnection",
  source: "IF",
  target: "Handler",
  sourceIndex: 0  // Which output? Hard to remember!
}
```

**New way** (smart parameters):
```javascript
// IF node - semantic branch names
{
  type: "addConnection",
  source: "IF",
  target: "True Handler",
  branch: "true"  // Clear and readable!
}

{
  type: "addConnection",
  source: "IF",
  target: "False Handler",
  branch: "false"
}

// Switch node - semantic case numbers
{
  type: "addConnection",
  source: "Switch",
  target: "Handler A",
  case: 0
}
```

### Mistake 6: Not Using intent Parameter

**Problem**: Less helpful tool responses

```javascript
// WRONG - No context for response
n8n_update_partial_workflow({
  id: "abc",
  operations: [{type: "addNode", node: {...}}]
})

// CORRECT - Better AI responses
n8n_update_partial_workflow({
  id: "abc",
  intent: "Add error handling for API failures",
  operations: [{type: "addNode", node: {...}}]
})
```

---

## Tool Usage Patterns

### Pattern 1: Node Discovery (Most Common)

**Common workflow**: 18s average between steps

```javascript
// Step 1: Search (fast!)
const results = await search_nodes({
  query: "slack",
  mode: "OR",  // Default: any word matches
  limit: 20
});
// → Returns: nodes-base.slack, nodes-base.slackTrigger

// Step 2: Get details (~18s later, user reviewing results)
const details = await get_node({
  nodeType: "nodes-base.slack",
  includeExamples: true  // Get real template configs
});
// → Returns: operations, properties, metadata
```

### Pattern 2: Validation Loop

**Typical cycle**: 23s thinking, 58s fixing

```javascript
// Step 1: Validate
const result = await validate_node({
  nodeType: "nodes-base.slack",
  config: {
    resource: "channel",
    operation: "create"
  },
  profile: "runtime"
});

// Step 2: Check errors (~23s thinking)
if (!result.valid) {
  console.log(result.errors);  // "Missing required field: name"
}

// Step 3: Fix config (~58s fixing)
config.name = "general";

// Step 4: Validate again
await validate_node({...});  // Repeat until clean
```

### Pattern 3: Workflow Editing

**Most used update tool**: 99.0% success rate, 56s average between edits

```javascript
// Iterative workflow building (NOT one-shot!)
// Edit 1
await n8n_update_partial_workflow({
  id: "workflow-id",
  intent: "Add webhook trigger",
  operations: [{type: "addNode", node: {...}}]
});

// ~56s later...

// Edit 2
await n8n_update_partial_workflow({
  id: "workflow-id",
  intent: "Connect webhook to processor",
  operations: [{type: "addConnection", source: "...", target: "..."}]
});

// ~56s later...

// Edit 3 (validation)
await n8n_validate_workflow({id: "workflow-id"});

// Ready? Activate!
await n8n_update_partial_workflow({
  id: "workflow-id",
  intent: "Activate workflow for production",
  operations: [{type: "activateWorkflow"}]
});
```

---

## Detailed Guides

### Node Discovery Tools
See [SEARCH_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_mcp_tools_expert/SEARCH_GUIDE.md) for:
- search_nodes
- get_node with detail levels (minimal, standard, full)
- get_node modes (info, docs, search_properties, versions)

### Validation Tools
See [VALIDATION_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_mcp_tools_expert/VALIDATION_GUIDE.md) for:
- Validation profiles explained
- validate_node with modes (minimal, full)
- validate_workflow complete structure
- Auto-sanitization system
- Handling validation errors

### Workflow Management
See [WORKFLOW_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_game_studios/docs/workflow_guide.md) for:
- n8n_create_workflow
- n8n_update_partial_workflow (18 operation types!)
- Smart parameters (branch, case)
- AI connection types (8 types)
- Workflow activation (activateWorkflow/deactivateWorkflow)
- n8n_deploy_template
- n8n_workflow_versions

---

## Template Usage

### Search Templates

```javascript
// Search by keyword (default mode)
search_templates({
  query: "webhook slack",
  limit: 20
});

// Search by node types
search_templates({
  searchMode: "by_nodes",
  nodeTypes: ["n8n-nodes-base.httpRequest", "n8n-nodes-base.slack"]
});

// Search by task type
search_templates({
  searchMode: "by_task",
  task: "webhook_processing"
});

// Search by metadata (complexity, setup time)
search_templates({
  searchMode: "by_metadata",
  complexity: "simple",
  maxSetupMinutes: 15
});
```

### Get Template Details

```javascript
get_template({
  templateId: 2947,
  mode: "structure"  // nodes+connections only
});

get_template({
  templateId: 2947,
  mode: "full"  // complete workflow JSON
});
```

### Deploy Template Directly

```javascript
// Deploy template to your n8n instance
n8n_deploy_template({
  templateId: 2947,
  name: "My Weather to Slack",  // Custom name (optional)
  autoFix: true,  // Auto-fix common issues (default)
  autoUpgradeVersions: true  // Upgrade node versions (default)
});
// Returns: workflow ID, required credentials, fixes applied
```

---

## Data Table Management

### n8n_manage_datatable

Unified tool for managing n8n data tables and rows. Supports CRUD operations on tables and rows with filtering, pagination, and dry-run support.

**Table Actions**: `createTable`, `listTables`, `getTable`, `updateTable`, `deleteTable`
**Row Actions**: `getRows`, `insertRows`, `updateRows`, `upsertRows`, `deleteRows`

```javascript
// Create a data table
n8n_manage_datatable({
  action: "createTable",
  name: "Contacts",
  columns: [
    {name: "email", type: "string"},
    {name: "score", type: "number"}
  ]
})

// Get rows with filter
n8n_manage_datatable({
  action: "getRows",
  tableId: "dt-123",
  filter: {
    filters: [{columnName: "status", condition: "eq", value: "active"}]
  },
  limit: 50
})

// Insert rows
n8n_manage_datatable({
  action: "insertRows",
  tableId: "dt-123",
  data: [{email: "a@b.com", score: 10}],
  returnType: "all"
})

// Update with dry run (preview changes)
n8n_manage_datatable({
  action: "updateRows",
  tableId: "dt-123",
  filter: {filters: [{columnName: "score", condition: "lt", value: 5}]},
  data: {status: "inactive"},
  dryRun: true
})

// Upsert (update or insert)
n8n_manage_datatable({
  action: "upsertRows",
  tableId: "dt-123",
  filter: {filters: [{columnName: "email", condition: "eq", value: "a@b.com"}]},
  data: {score: 15},
  returnData: true
})
```

**Filter conditions**: `eq`, `neq`, `like`, `ilike`, `gt`, `gte`, `lt`, `lte`

**Best practices**:
- Use `dryRun: true` before bulk updates/deletes to verify filter correctness
- Define column types upfront (`string`, `number`, `boolean`, `date`)
- Use `returnType: "count"` (default) for insertRows to minimize response size
- `deleteRows` requires a filter - cannot delete all rows without one

---

## Self-Help Tools

### Get Tool Documentation

```javascript
// Overview of all tools
tools_documentation()

// Specific tool details
tools_documentation({
  topic: "search_nodes",
  depth: "full"
})

// Code node guides
tools_documentation({topic: "javascript_code_node_guide", depth: "full"})
tools_documentation({topic: "python_code_node_guide", depth: "full"})
```

### AI Agent Guide

```javascript
// Comprehensive AI workflow guide
ai_agents_guide()
// Returns: Architecture, connections, tools, validation, best practices

// Or via tools_documentation
tools_documentation({topic: "ai_agents_guide", depth: "full"})
```

### Health Check

```javascript
// Quick health check
n8n_health_check()

// Detailed diagnostics
n8n_health_check({mode: "diagnostic"})
// → Returns: status, env vars, tool status, API connectivity
```

---

## Tool Availability

**Always Available** (no n8n API needed):
- search_nodes, get_node
- validate_node, validate_workflow
- search_templates, get_template
- tools_documentation, ai_agents_guide

**Requires n8n API** (N8N_API_URL + N8N_API_KEY):
- n8n_create_workflow
- n8n_update_partial_workflow, n8n_update_full_workflow
- n8n_validate_workflow (by ID)
- n8n_list_workflows, n8n_get_workflow, n8n_delete_workflow
- n8n_test_workflow
- n8n_executions
- n8n_deploy_template
- n8n_workflow_versions
- n8n_autofix_workflow
- n8n_manage_datatable

If API tools unavailable, use templates and validation-only workflows.

---

## Unified Tool Reference

### get_node (Unified Node Information)

**Detail Levels** (mode="info", default):
- `minimal` (~200 tokens) - Basic metadata only
- `standard` (~1-2K tokens) - Essential properties + operations (RECOMMENDED)
- `full` (~3-8K tokens) - Complete schema (use sparingly)

**Operation Modes**:
- `info` (default) - Node schema with detail level
- `docs` - Readable markdown documentation
- `search_properties` - Find specific properties (use with propertyQuery)
- `versions` - List all versions with breaking changes
- `compare` - Compare two versions
- `breaking` - Show only breaking changes
- `migrations` - Show auto-migratable changes

```javascript
// Standard (recommended)
get_node({nodeType: "nodes-base.httpRequest"})

// Get documentation
get_node({nodeType: "nodes-base.webhook", mode: "docs"})

// Search for properties
get_node({nodeType: "nodes-base.httpRequest", mode: "search_properties", propertyQuery: "auth"})

// Check versions
get_node({nodeType: "nodes-base.executeWorkflow", mode: "versions"})
```

### validate_node (Unified Validation)

**Modes**:
- `full` (default) - Comprehensive validation with errors/warnings/suggestions
- `minimal` - Quick required fields check only

**Profiles** (for mode="full"):
- `minimal` - Very lenient
- `runtime` - Standard (default, recommended)
- `ai-friendly` - Balanced for AI workflows
- `strict` - Most thorough (production)

```javascript
// Full validation with runtime profile
validate_node({nodeType: "nodes-base.slack", config: {...}, profile: "runtime"})

// Quick required fields check
validate_node({nodeType: "nodes-base.webhook", config: {}, mode: "minimal"})
```

---

## Performance Characteristics

| Tool | Response Time | Payload Size |
|------|---------------|--------------|
| search_nodes | <20ms | Small |
| get_node (standard) | <10ms | ~1-2KB |
| get_node (full) | <100ms | 3-8KB |
| validate_node (minimal) | <50ms | Small |
| validate_node (full) | <100ms | Medium |
| validate_workflow | 100-500ms | Medium |
| n8n_create_workflow | 100-500ms | Medium |
| n8n_update_partial_workflow | 50-200ms | Small |
| n8n_deploy_template | 200-500ms | Medium |

---

## Best Practices

### Do
- Use `get_node({detail: "standard"})` for most use cases
- Specify validation profile explicitly (`profile: "runtime"`)
- Use smart parameters (`branch`, `case`) for clarity
- Include `intent` parameter in workflow updates
- Follow search → get_node → validate workflow
- Iterate workflows (avg 56s between edits)
- Validate after every significant change
- Use `includeExamples: true` for real configs
- Use `n8n_deploy_template` for quick starts

### Don't
- Use `detail: "full"` unless necessary (wastes tokens)
- Forget nodeType prefix (`nodes-base.*`)
- Skip validation profiles
- Try to build workflows in one shot (iterate!)
- Ignore auto-sanitization behavior
- Use full prefix (`n8n-nodes-base.*`) with search/validate tools
- Forget to activate workflows after building

---

## Summary

**Most Important**:
1. Use **get_node** with `detail: "standard"` (default) - covers 95% of use cases
2. nodeType formats differ: `nodes-base.*` (search/validate) vs `n8n-nodes-base.*` (workflows)
3. Specify **validation profiles** (`runtime` recommended)
4. Use **smart parameters** (`branch="true"`, `case=0`)
5. Include **intent parameter** in workflow updates
6. **Auto-sanitization** runs on ALL nodes during updates
7. Workflows can be **activated via API** (`activateWorkflow` operation)
8. Workflows are built **iteratively** (56s avg between edits)
9. **Data tables** managed with `n8n_manage_datatable` (CRUD + filtering)
10. **AI agent guide** available via `ai_agents_guide()` tool

**Common Workflow**:
1. search_nodes → find node
2. get_node → understand config
3. validate_node → check config
4. n8n_create_workflow → build
5. n8n_validate_workflow → verify
6. n8n_update_partial_workflow → iterate
7. activateWorkflow → go live!

For details, see:
- [SEARCH_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_mcp_tools_expert/SEARCH_GUIDE.md) - Node discovery
- [VALIDATION_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_mcp_tools_expert/VALIDATION_GUIDE.md) - Configuration validation
- [WORKFLOW_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_game_studios/docs/workflow_guide.md) - Workflow management

---

**Related Skills**:
- n8n Expression Syntax - Write expressions in workflow fields
- n8n Workflow Patterns - Architectural patterns from templates
- n8n Validation Expert - Interpret validation errors
- n8n Node Configuration - Operation-specific requirements
- n8n Code JavaScript - Write JavaScript in Code nodes
- n8n Code Python - Write Python in Code nodes
```

## File: `skills/n8n-mcp-tools-expert/VALIDATION_GUIDE.md`
```markdown
# Configuration Validation Tools Guide

Complete guide for validating node configurations and workflows.

---

## Validation Philosophy

**Validate early, validate often**

Validation is typically iterative with validate → fix cycles

---

## validate_node (UNIFIED VALIDATION)

The `validate_node` tool provides all validation capabilities with different modes.

### Quick Check (mode="minimal")

**Speed**: <50ms

**Use when**: Checking what fields are required

```javascript
validate_node({
  nodeType: "nodes-base.slack",
  config: {},  // Empty to see all required fields
  mode: "minimal"
})
```

**Returns**:
```javascript
{
  "valid": true,           // Usually true (most nodes have no strict requirements)
  "missingRequiredFields": []
}
```

**When to use**: Planning configuration, seeing basic requirements

### Full Validation (mode="full", DEFAULT)

**Speed**: <100ms

**Use when**: Validating actual configuration before deployment

```javascript
validate_node({
  nodeType: "nodes-base.slack",
  config: {
    resource: "channel",
    operation: "create",
    channel: "general"
  },
  profile: "runtime"  // Recommended!
})
// mode="full" is the default
```

---

## Validation Profiles

Choose based on your stage:

**minimal** - Only required fields
- Fastest
- Most permissive
- Use: Quick checks during editing

**runtime** - Values + types (**RECOMMENDED**)
- Balanced validation
- Catches real errors
- Use: Pre-deployment validation

**ai-friendly** - Reduce false positives
- For AI-generated configs
- Tolerates minor issues
- Use: When AI configures nodes

**strict** - Maximum validation
- Strictest rules
- May have false positives
- Use: Production deployment

---

## Validation Response

```javascript
{
  "nodeType": "nodes-base.slack",
  "workflowNodeType": "n8n-nodes-base.slack",
  "displayName": "Slack",
  "valid": false,
  "errors": [
    {
      "type": "missing_required",
      "property": "name",
      "message": "Channel name is required",
      "fix": "Provide a channel name (lowercase, no spaces, 1-80 characters)"
    }
  ],
  "warnings": [
    {
      "type": "best_practice",
      "property": "errorHandling",
      "message": "Slack API can have rate limits",
      "suggestion": "Add onError: 'continueRegularOutput' with retryOnFail"
    }
  ],
  "suggestions": [],
  "summary": {
    "hasErrors": true,
    "errorCount": 1,
    "warningCount": 1,
    "suggestionCount": 0
  }
}
```

### Error Types

- `missing_required` - Must fix
- `invalid_value` - Must fix
- `type_mismatch` - Must fix
- `best_practice` - Should fix (warning)
- `suggestion` - Optional improvement

---

## validate_workflow (STRUCTURE VALIDATION)

**Speed**: 100-500ms

**Use when**: Checking complete workflow before execution

**Syntax**:
```javascript
validate_workflow({
  workflow: {
    nodes: [...],        // Array of nodes
    connections: {...}   // Connections object
  },
  options: {
    validateNodes: true,       // Default: true
    validateConnections: true, // Default: true
    validateExpressions: true, // Default: true
    profile: "runtime"         // For node validation
  }
})
```

**Validates**:
- Node configurations
- Connection validity (no broken references)
- Expression syntax ({{ }} patterns)
- Workflow structure (triggers, flow)
- AI connections (8 types)

**Returns**: Comprehensive validation report with errors, warnings, suggestions

### Validate by Workflow ID

```javascript
// Validate workflow already in n8n
n8n_validate_workflow({
  id: "workflow-id",
  options: {
    validateNodes: true,
    validateConnections: true,
    validateExpressions: true,
    profile: "runtime"
  }
})
```

---

## Validation Loop Pattern

**Typical cycle**: 23s thinking, 58s fixing

```
1. Configure node
   ↓
2. validate_node (23s thinking about errors)
   ↓
3. Fix errors
   ↓
4. validate_node again (58s fixing)
   ↓
5. Repeat until valid
```

**Example**:
```javascript
// Iteration 1
let config = {
  resource: "channel",
  operation: "create"
};

const result1 = validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "runtime"
});
// → Error: Missing "name"

// Iteration 2 (~58s later)
config.name = "general";

const result2 = validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "runtime"
});
// → Valid!
```

---

## Auto-Sanitization System

**When it runs**: On ANY workflow update (create or update_partial)

**What it fixes** (automatically on ALL nodes):
1. Binary operators (equals, contains, greaterThan) → removes `singleValue`
2. Unary operators (isEmpty, isNotEmpty, true, false) → adds `singleValue: true`
3. Invalid operator structures → corrects to proper format
4. IF v2.2+ nodes → adds complete `conditions.options` metadata
5. Switch v3.2+ nodes → adds complete `conditions.options` for all rules

**What it CANNOT fix**:
- Broken connections (references to non-existent nodes)
- Branch count mismatches (3 Switch rules but only 2 outputs)
- Paradoxical corrupt states (API returns corrupt, rejects updates)

**Example**:
```javascript
// Before auto-sanitization
{
  "type": "boolean",
  "operation": "equals",
  "singleValue": true  // Binary operators shouldn't have this
}

// After auto-sanitization (automatic!)
{
  "type": "boolean",
  "operation": "equals"
  // singleValue removed automatically
}
```

**Recovery tools**:
- `cleanStaleConnections` operation - removes broken connections
- `n8n_autofix_workflow({id})` - preview/apply fixes

---

## n8n_autofix_workflow (AUTO-FIX TOOL)

**Use when**: Validation errors need automatic fixes

```javascript
// Preview fixes (default - doesn't apply)
n8n_autofix_workflow({
  id: "workflow-id",
  applyFixes: false,  // Preview mode
  confidenceThreshold: "medium"  // high, medium, low
})

// Apply fixes
n8n_autofix_workflow({
  id: "workflow-id",
  applyFixes: true
})
```

**Fix Types**:
- `expression-format` - Fix missing `=` prefix in expressions
- `typeversion-correction` - Downgrade unsupported typeVersions
- `error-output-config` - Remove conflicting onError settings
- `node-type-correction` - Fix unknown node types via similarity matching (90%+ confidence)
- `webhook-missing-path` - Generate UUIDs for webhook nodes missing paths
- `typeversion-upgrade` - Smart upgrade nodes to latest versions with auto-migration
- `version-migration` - Guidance for complex breaking changes (manual steps)

**Confidence Threshold**: `high` (90%+), `medium` (70-89%, default), `low` (any)

**Post-update guidance**: Check `postUpdateGuidance` in the response for version upgrade migration steps.

---

## Binary vs Unary Operators

**Binary operators** (compare two values):
- equals, notEquals, contains, notContains
- greaterThan, lessThan, startsWith, endsWith
- **Must NOT have** `singleValue: true`

**Unary operators** (check single value):
- isEmpty, isNotEmpty, true, false
- **Must have** `singleValue: true`

**Auto-sanitization fixes these automatically!**

---

## Handling Validation Errors

### Process

```
1. Read error message carefully
2. Check if it's a known false positive
3. Fix real errors
4. Validate again
5. Iterate until clean
```

### Common Errors

**"Required field missing"**
→ Add the field with appropriate value

**"Invalid value"**
→ Check allowed values in get_node output

**"Type mismatch"**
→ Convert to correct type (string/number/boolean)

**"Cannot have singleValue"**
→ Auto-sanitization will fix on next update

**"Missing operator metadata"**
→ Auto-sanitization will fix on next update

### False Positives

Some validation warnings may be acceptable:
- Optional best practices
- Node-specific edge cases
- Profile-dependent issues

Use **ai-friendly** profile to reduce false positives.

---

## Best Practices

### Do

- Use **runtime** profile for pre-deployment
- Validate after every configuration change
- Fix errors immediately (avg 58s)
- Iterate validation loop
- Trust auto-sanitization for operator issues
- Use `mode: "minimal"` for quick checks
- Use `n8n_autofix_workflow` for bulk fixes
- Activate workflows via API when ready (`activateWorkflow` operation)

### Don't

- Skip validation before deployment
- Ignore error messages
- Use strict profile during development (too many warnings)
- Assume validation passed (check result)
- Try to manually fix auto-sanitization issues

---

## Example: Complete Validation Workflow

```javascript
// Step 1: Get node requirements (quick check)
validate_node({
  nodeType: "nodes-base.slack",
  config: {},
  mode: "minimal"
});
// → Know what's required

// Step 2: Configure node
const config = {
  resource: "message",
  operation: "post",
  channel: "#general",
  text: "Hello!"
};

// Step 3: Validate configuration (full validation)
const result = validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "runtime"
});

// Step 4: Check result
if (result.valid) {
  console.log("Configuration valid!");
} else {
  console.log("Errors:", result.errors);
  // Fix and validate again
}

// Step 5: Validate in workflow context
validate_workflow({
  workflow: {
    nodes: [{...config as node...}],
    connections: {...}
  }
});

// Step 6: Apply auto-fixes if needed
n8n_autofix_workflow({
  id: "workflow-id",
  applyFixes: true
});
```

---

## Summary

**Key Points**:
1. Use **runtime** profile (balanced validation)
2. Validation loop: validate → fix (58s) → validate again
3. Auto-sanitization fixes operator structures automatically
4. Binary operators ≠ singleValue, Unary operators = singleValue: true
5. Iterate until validation passes
6. Use `n8n_autofix_workflow` for automatic fixes

**Tool Selection**:
- **validate_node({mode: "minimal"})**: Quick required fields check
- **validate_node({profile: "runtime"})**: Full config validation (**use this!**)
- **validate_workflow**: Complete workflow check
- **n8n_validate_workflow({id})**: Validate existing workflow
- **n8n_autofix_workflow({id})**: Auto-fix common issues

**Related**:
- [SEARCH_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_mcp_tools_expert/SEARCH_GUIDE.md) - Find nodes
- [WORKFLOW_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_game_studios/docs/workflow_guide.md) - Build workflows
```

## File: `skills/n8n-mcp-tools-expert/WORKFLOW_GUIDE.md`
```markdown
# Workflow Management Tools Guide

Complete guide for creating, updating, and managing n8n workflows.

---

## Tool Availability

**Requires n8n API**: All tools in this guide need `N8N_API_URL` and `N8N_API_KEY` configured.

If unavailable, use template examples and validation-only workflows.

---

## n8n_create_workflow

**Speed**: 100-500ms

**Use when**: Creating new workflows from scratch

**Syntax**:
```javascript
n8n_create_workflow({
  name: "Webhook to Slack",  // Required
  nodes: [...],              // Required: array of nodes
  connections: {...},        // Required: connections object
  settings: {...}            // Optional: workflow settings
})
```

**Returns**: Created workflow with ID

**Example**:
```javascript
n8n_create_workflow({
  name: "Webhook to Slack",
  nodes: [
    {
      id: "webhook-1",
      name: "Webhook",
      type: "n8n-nodes-base.webhook",  // Full prefix!
      typeVersion: 2,
      position: [250, 300],
      parameters: {
        path: "slack-notify",
        httpMethod: "POST"
      }
    },
    {
      id: "slack-1",
      name: "Slack",
      type: "n8n-nodes-base.slack",
      typeVersion: 2,
      position: [450, 300],
      parameters: {
        resource: "message",
        operation: "post",
        channel: "#general",
        text: "={{$json.body.message}}"
      }
    }
  ],
  connections: {
    "Webhook": {
      "main": [[{node: "Slack", type: "main", index: 0}]]
    }
  }
})
```

**Notes**:
- Workflows created **inactive** (activate with `activateWorkflow` operation)
- Auto-sanitization runs on creation
- Validate before creating for best results

---

## n8n_update_partial_workflow (MOST USED!)

**Speed**: 50-200ms | **Uses**: 38,287 (most used tool!)

**Use when**: Making incremental changes to workflows

**Common pattern**: 56s average between edits (iterative building!)

### 18 Operation Types

**Node Operations** (6 types):
1. `addNode` - Add new node
2. `removeNode` - Remove node by ID or name
3. `updateNode` - Update node properties (use dot notation)
4. `moveNode` - Change position
5. `enableNode` - Enable disabled node
6. `disableNode` - Disable active node

**Connection Operations** (5 types):
7. `addConnection` - Connect nodes (supports smart params)
8. `removeConnection` - Remove connection (supports ignoreErrors)
9. `rewireConnection` - Change connection target
10. `cleanStaleConnections` - Auto-remove broken connections
11. `replaceConnections` - Replace entire connections object

**Metadata Operations** (4 types):
12. `updateSettings` - Workflow settings
13. `updateName` - Rename workflow
14. `addTag` - Add tag
15. `removeTag` - Remove tag

**Activation Operations** (2 types):
16. `activateWorkflow` - Activate workflow for automatic execution
17. `deactivateWorkflow` - Deactivate workflow

**Project Management Operations** (1 type):
18. `transferWorkflow` - Transfer workflow to a different project (enterprise/cloud)

### Intent Parameter (IMPORTANT!)

Always include `intent` for better responses:

```javascript
n8n_update_partial_workflow({
  id: "workflow-id",
  intent: "Add error handling for API failures",  // Describe what you're doing
  operations: [...]
})
```

### Smart Parameters

**IF nodes** - Use semantic branch names:
```javascript
{
  type: "addConnection",
  source: "IF",
  target: "True Handler",
  branch: "true"  // Instead of sourceIndex: 0
}

{
  type: "addConnection",
  source: "IF",
  target: "False Handler",
  branch: "false"  // Instead of sourceIndex: 1
}
```

**Switch nodes** - Use semantic case numbers:
```javascript
{
  type: "addConnection",
  source: "Switch",
  target: "Handler A",
  case: 0
}

{
  type: "addConnection",
  source: "Switch",
  target: "Handler B",
  case: 1
}
```

### AI Connection Types (8 types)

**Full support** for AI workflows:

```javascript
// Language Model
{
  type: "addConnection",
  source: "OpenAI Chat Model",
  target: "AI Agent",
  sourceOutput: "ai_languageModel"
}

// Tool
{
  type: "addConnection",
  source: "HTTP Request Tool",
  target: "AI Agent",
  sourceOutput: "ai_tool"
}

// Memory
{
  type: "addConnection",
  source: "Window Buffer Memory",
  target: "AI Agent",
  sourceOutput: "ai_memory"
}

// All 8 types:
// - ai_languageModel
// - ai_tool
// - ai_memory
// - ai_outputParser
// - ai_embedding
// - ai_vectorStore
// - ai_document
// - ai_textSplitter
```

### Property Removal with null

Remove properties by setting them to `null`:

```javascript
// Remove a property
{
  type: "updateNode",
  nodeName: "HTTP Request",
  updates: { onError: null }
}

// Migrate from deprecated property
{
  type: "updateNode",
  nodeName: "HTTP Request",
  updates: {
    continueOnFail: null,  // Remove old
    onError: "continueErrorOutput"  // Add new
  }
}
```

### Activation Operations

```javascript
// Activate workflow
n8n_update_partial_workflow({
  id: "workflow-id",
  intent: "Activate workflow for production",
  operations: [{type: "activateWorkflow"}]
})

// Deactivate workflow
n8n_update_partial_workflow({
  id: "workflow-id",
  intent: "Deactivate workflow for maintenance",
  operations: [{type: "deactivateWorkflow"}]
})
```

### Example Usage

```javascript
n8n_update_partial_workflow({
  id: "workflow-id",
  intent: "Add transform node after IF condition",
  operations: [
    // Add node
    {
      type: "addNode",
      node: {
        name: "Transform",
        type: "n8n-nodes-base.set",
        position: [400, 300],
        parameters: {}
      }
    },
    // Connect it (smart parameter)
    {
      type: "addConnection",
      source: "IF",
      target: "Transform",
      branch: "true"  // Clear and semantic!
    }
  ]
})
```

### Cleanup & Recovery

**cleanStaleConnections** - Remove broken connections:
```javascript
{type: "cleanStaleConnections"}
```

**rewireConnection** - Change target atomically:
```javascript
{
  type: "rewireConnection",
  source: "Webhook",
  from: "Old Handler",
  to: "New Handler"
}
```

**Best-effort mode** - Apply what works:
```javascript
n8n_update_partial_workflow({
  id: "workflow-id",
  operations: [...],
  continueOnError: true  // Don't fail if some operations fail
})
```

**Validate before applying**:
```javascript
n8n_update_partial_workflow({
  id: "workflow-id",
  operations: [...],
  validateOnly: true  // Preview without applying
})
```

---

## n8n_deploy_template (QUICK START!)

**Speed**: 200-500ms

**Use when**: Deploying a template directly to n8n instance

```javascript
n8n_deploy_template({
  templateId: 2947,  // Required: from n8n.io
  name: "My Weather to Slack",  // Optional: custom name
  autoFix: true,  // Default: auto-fix common issues
  autoUpgradeVersions: true,  // Default: upgrade node versions
  stripCredentials: true  // Default: remove credential refs
})
```

**Returns**:
- Workflow ID
- Required credentials
- Fixes applied

**Example**:
```javascript
// Deploy a webhook to Slack template
const result = n8n_deploy_template({
  templateId: 2947,
  name: "Production Slack Notifier"
});

// Result includes:
// - id: "new-workflow-id"
// - requiredCredentials: ["slack"]
// - fixesApplied: ["typeVersion upgraded", "expression format fixed"]
```

---

## n8n_workflow_versions (VERSION CONTROL)

**Use when**: Managing workflow history, rollback, cleanup

### List Versions
```javascript
n8n_workflow_versions({
  mode: "list",
  workflowId: "workflow-id",
  limit: 10
})
```

### Get Specific Version
```javascript
n8n_workflow_versions({
  mode: "get",
  versionId: 123
})
```

### Rollback to Previous Version
```javascript
n8n_workflow_versions({
  mode: "rollback",
  workflowId: "workflow-id",
  versionId: 123,  // Optional: specific version
  validateBefore: true  // Default: validate before rollback
})
```

### Delete Versions
```javascript
// Delete specific version
n8n_workflow_versions({
  mode: "delete",
  workflowId: "workflow-id",
  versionId: 123
})

// Delete all versions for workflow
n8n_workflow_versions({
  mode: "delete",
  workflowId: "workflow-id",
  deleteAll: true
})
```

### Prune Old Versions
```javascript
n8n_workflow_versions({
  mode: "prune",
  workflowId: "workflow-id",
  maxVersions: 10  // Keep 10 most recent
})
```

---

## n8n_test_workflow (TRIGGER EXECUTION)

**Use when**: Testing workflow execution

**Auto-detects** trigger type (webhook, form, chat)

```javascript
// Test webhook workflow
n8n_test_workflow({
  workflowId: "workflow-id",
  triggerType: "webhook",  // Optional: auto-detected
  httpMethod: "POST",
  data: {message: "Hello!"},
  waitForResponse: true,
  timeout: 120000
})

// Test chat workflow
n8n_test_workflow({
  workflowId: "workflow-id",
  triggerType: "chat",
  message: "Hello, AI agent!",
  sessionId: "session-123"  // For conversation continuity
})
```

---

## n8n_validate_workflow (by ID)

**Use when**: Validating workflow stored in n8n

```javascript
n8n_validate_workflow({
  id: "workflow-id",
  options: {
    validateNodes: true,
    validateConnections: true,
    validateExpressions: true,
    profile: "runtime"
  }
})
```

---

## n8n_get_workflow

**Use when**: Retrieving workflow details

**Modes**:
- `full` (default) - Complete workflow JSON
- `details` - Full + execution stats
- `structure` - Nodes + connections only
- `minimal` - ID, name, active, tags

```javascript
// Full workflow
n8n_get_workflow({id: "workflow-id"})

// Just structure
n8n_get_workflow({id: "workflow-id", mode: "structure"})

// Minimal metadata
n8n_get_workflow({id: "workflow-id", mode: "minimal"})
```

---

## n8n_executions (EXECUTION MANAGEMENT)

**Use when**: Managing workflow executions

### Get Execution Details
```javascript
n8n_executions({
  action: "get",
  id: "execution-id",
  mode: "summary"  // preview, summary, filtered, full, error
})

// Error mode for debugging
n8n_executions({
  action: "get",
  id: "execution-id",
  mode: "error",
  includeStackTrace: true
})
```

### List Executions
```javascript
n8n_executions({
  action: "list",
  workflowId: "workflow-id",
  status: "error",  // success, error, waiting
  limit: 100
})
```

### Delete Execution
```javascript
n8n_executions({
  action: "delete",
  id: "execution-id"
})
```

---

## Workflow Lifecycle

**Standard pattern**:
```
1. CREATE
   n8n_create_workflow({...})
   → Returns workflow ID

2. VALIDATE
   n8n_validate_workflow({id})
   → Check for errors

3. EDIT (iterative! 56s avg between edits)
   n8n_update_partial_workflow({id, intent: "...", operations: [...]})
   → Make changes

4. VALIDATE AGAIN
   n8n_validate_workflow({id})
   → Verify changes

5. ACTIVATE
   n8n_update_partial_workflow({
     id,
     intent: "Activate workflow",
     operations: [{type: "activateWorkflow"}]
   })
   → Workflow now runs on triggers!

6. MONITOR
   n8n_executions({action: "list", workflowId: id})
   n8n_executions({action: "get", id: execution_id})
```

---

## Common Patterns from Telemetry

### Pattern 1: Edit → Validate (7,841 occurrences)
```javascript
n8n_update_partial_workflow({...})
// ↓ 23s (thinking about what to validate)
n8n_validate_workflow({id})
```

### Pattern 2: Validate → Fix (7,266 occurrences)
```javascript
n8n_validate_workflow({id})
// ↓ 58s (fixing errors)
n8n_update_partial_workflow({...})
```

### Pattern 3: Iterative Building (31,464 occurrences)
```javascript
update → update → update → ... (56s avg between edits)
```

**This shows**: Workflows are built **iteratively**, not in one shot!

---

## Best Practices

### Do

- Build workflows **iteratively** (avg 56s between edits)
- Include **intent** parameter for better responses
- Use **smart parameters** (branch, case) for clarity
- Validate **after** significant changes
- Use **atomic mode** (default) for critical updates
- Specify **sourceOutput** for AI connections
- Clean stale connections after node renames/deletions
- Use `n8n_deploy_template` for quick starts
- Activate workflows via API when ready

### Don't

- Try to build workflows in one shot
- Skip the intent parameter
- Use sourceIndex when branch/case available
- Skip validation before activation
- Forget to test workflows after creation
- Ignore auto-sanitization behavior

---

## Summary

**Most Important**:
1. **n8n_update_partial_workflow** is most-used tool (38,287 uses)
2. Include **intent** parameter for better responses
3. Workflows built **iteratively** (56s avg between edits)
4. Use **smart parameters** (branch="true", case=0) for clarity
5. **AI connections** supported (8 types with sourceOutput)
6. **Workflow activation** supported via API (`activateWorkflow` operation)
7. **Auto-sanitization** runs on all operations
8. Use **n8n_deploy_template** for quick starts

**Additional Tools**:
- `n8n_deploy_template` - Deploy templates directly
- `n8n_workflow_versions` - Version control & rollback
- `n8n_test_workflow` - Trigger execution
- `n8n_executions` - Manage executions
- `n8n_manage_datatable` - Data table and row management
- `n8n_delete_workflow` - Permanently delete workflows
- `n8n_list_workflows` - List workflows with filtering
- `n8n_update_full_workflow` - Full workflow replacement

**Related**:
- [SEARCH_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_mcp_tools_expert/SEARCH_GUIDE.md) - Find nodes to add
- [VALIDATION_GUIDE.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_mcp_tools_expert/VALIDATION_GUIDE.md) - Validate workflows
```

## File: `skills/n8n-node-configuration/DEPENDENCIES.md`
```markdown
# Property Dependencies Guide

Deep dive into n8n property dependencies and displayOptions mechanism.

---

## What Are Property Dependencies?

**Definition**: Rules that control when fields are visible or required based on other field values.

**Mechanism**: `displayOptions` in node schema

**Purpose**:
- Show relevant fields only
- Hide irrelevant fields
- Simplify configuration UX
- Prevent invalid configurations

---

## displayOptions Structure

### Basic Format

```javascript
{
  "name": "fieldName",
  "type": "string",
  "displayOptions": {
    "show": {
      "otherField": ["value1", "value2"]
    }
  }
}
```

**Translation**: Show `fieldName` when `otherField` equals "value1" OR "value2"

### Show vs Hide

#### show (Most Common)

**Show field when condition matches**:
```javascript
{
  "name": "body",
  "displayOptions": {
    "show": {
      "sendBody": [true]
    }
  }
}
```

**Meaning**: Show `body` when `sendBody = true`

#### hide (Less Common)

**Hide field when condition matches**:
```javascript
{
  "name": "advanced",
  "displayOptions": {
    "hide": {
      "simpleMode": [true]
    }
  }
}
```

**Meaning**: Hide `advanced` when `simpleMode = true`

### Multiple Conditions (AND Logic)

```javascript
{
  "name": "body",
  "displayOptions": {
    "show": {
      "sendBody": [true],
      "method": ["POST", "PUT", "PATCH"]
    }
  }
}
```

**Meaning**: Show `body` when:
- `sendBody = true` AND
- `method IN (POST, PUT, PATCH)`

**All conditions must match** (AND logic)

### Multiple Values (OR Logic)

```javascript
{
  "name": "someField",
  "displayOptions": {
    "show": {
      "method": ["POST", "PUT", "PATCH"]
    }
  }
}
```

**Meaning**: Show `someField` when:
- `method = POST` OR
- `method = PUT` OR
- `method = PATCH`

**Any value matches** (OR logic)

---

## Common Dependency Patterns

### Pattern 1: Boolean Toggle

**Use case**: Optional feature flag

**Example**: HTTP Request sendBody
```javascript
// Field: sendBody (boolean)
{
  "name": "sendBody",
  "type": "boolean",
  "default": false
}

// Field: body (depends on sendBody)
{
  "name": "body",
  "displayOptions": {
    "show": {
      "sendBody": [true]
    }
  }
}
```

**Flow**:
1. User sees sendBody checkbox
2. When checked → body field appears
3. When unchecked → body field hides

### Pattern 2: Resource/Operation Cascade

**Use case**: Different operations show different fields

**Example**: Slack message operations
```javascript
// Operation: post
{
  "name": "channel",
  "displayOptions": {
    "show": {
      "resource": ["message"],
      "operation": ["post"]
    }
  }
}

// Operation: update
{
  "name": "messageId",
  "displayOptions": {
    "show": {
      "resource": ["message"],
      "operation": ["update"]
    }
  }
}
```

**Flow**:
1. User selects resource="message"
2. User selects operation="post" → sees channel
3. User changes to operation="update" → channel hides, messageId shows

### Pattern 3: Type-Specific Configuration

**Use case**: Different types need different fields

**Example**: IF node conditions
```javascript
// String operations
{
  "name": "value2",
  "displayOptions": {
    "show": {
      "conditions.string.0.operation": ["equals", "notEquals", "contains"]
    }
  }
}

// Unary operations (isEmpty) don't show value2
{
  "displayOptions": {
    "hide": {
      "conditions.string.0.operation": ["isEmpty", "isNotEmpty"]
    }
  }
}
```

### Pattern 4: Method-Specific Fields

**Use case**: HTTP methods have different options

**Example**: HTTP Request
```javascript
// Query parameters (all methods can have)
{
  "name": "queryParameters",
  "displayOptions": {
    "show": {
      "sendQuery": [true]
    }
  }
}

// Body (only certain methods)
{
  "name": "body",
  "displayOptions": {
    "show": {
      "sendBody": [true],
      "method": ["POST", "PUT", "PATCH", "DELETE"]
    }
  }
}
```

---

## Finding Property Dependencies

### Using get_node with search_properties Mode

```javascript
// Find properties related to "body"
get_node({
  nodeType: "nodes-base.httpRequest",
  mode: "search_properties",
  propertyQuery: "body"
});
```

### Using get_node with Full Detail

```javascript
// Get complete schema with displayOptions
get_node({
  nodeType: "nodes-base.httpRequest",
  detail: "full"
});
```

### When to Use

**✅ Use when**:
- Validation fails with "missing field" but you don't see that field
- A field appears/disappears unexpectedly
- You need to understand what controls field visibility
- Building dynamic configuration tools

**❌ Don't use when**:
- Simple configuration (use `get_node` with standard detail)
- Just starting configuration
- Field requirements are obvious

---

## Complex Dependency Examples

### Example 1: HTTP Request Complete Flow

**Scenario**: Configuring POST with JSON body

**Step 1**: Set method
```javascript
{
  "method": "POST"
  // → sendBody becomes visible
}
```

**Step 2**: Enable body
```javascript
{
  "method": "POST",
  "sendBody": true
  // → body field becomes visible AND required
}
```

**Step 3**: Configure body
```javascript
{
  "method": "POST",
  "sendBody": true,
  "body": {
    "contentType": "json"
    // → content field becomes visible AND required
  }
}
```

**Step 4**: Add content
```javascript
{
  "method": "POST",
  "sendBody": true,
  "body": {
    "contentType": "json",
    "content": {
      "name": "John",
      "email": "john@example.com"
    }
  }
}
// ✅ Valid!
```

**Dependency chain**:
```
method=POST
  → sendBody visible
    → sendBody=true
      → body visible + required
        → body.contentType=json
          → body.content visible + required
```

### Example 2: IF Node Operator Dependencies

**Scenario**: String comparison with different operators

**Binary operator** (equals):
```javascript
{
  "conditions": {
    "string": [
      {
        "operation": "equals"
        // → value1 required
        // → value2 required
        // → singleValue should NOT be set
      }
    ]
  }
}
```

**Unary operator** (isEmpty):
```javascript
{
  "conditions": {
    "string": [
      {
        "operation": "isEmpty"
        // → value1 required
        // → value2 should NOT be set
        // → singleValue should be true (auto-added)
      }
    ]
  }
}
```

**Dependency table**:

| Operator | value1 | value2 | singleValue |
|---|---|---|---|
| equals | Required | Required | false |
| notEquals | Required | Required | false |
| contains | Required | Required | false |
| isEmpty | Required | Hidden | true |
| isNotEmpty | Required | Hidden | true |

### Example 3: Slack Operation Matrix

**Scenario**: Different Slack operations show different fields

```javascript
// post message
{
  "resource": "message",
  "operation": "post"
  // Shows: channel (required), text (required), attachments, blocks
}

// update message
{
  "resource": "message",
  "operation": "update"
  // Shows: messageId (required), text (required), channel (optional)
}

// delete message
{
  "resource": "message",
  "operation": "delete"
  // Shows: messageId (required), channel (required)
  // Hides: text, attachments, blocks
}

// get message
{
  "resource": "message",
  "operation": "get"
  // Shows: messageId (required), channel (required)
  // Hides: text, attachments, blocks
}
```

**Field visibility matrix**:

| Field | post | update | delete | get |
|---|---|---|---|---|
| channel | Required | Optional | Required | Required |
| text | Required | Required | Hidden | Hidden |
| messageId | Hidden | Required | Required | Required |
| attachments | Optional | Optional | Hidden | Hidden |
| blocks | Optional | Optional | Hidden | Hidden |

---

## Nested Dependencies

### What Are They?

**Definition**: Dependencies within object properties

**Example**: HTTP Request body.contentType controls body.content structure

```javascript
{
  "body": {
    "contentType": "json",
    // → content expects JSON object
    "content": {
      "key": "value"
    }
  }
}

{
  "body": {
    "contentType": "form-data",
    // → content expects form fields array
    "content": [
      {
        "name": "field1",
        "value": "value1"
      }
    ]
  }
}
```

### How to Handle

**Strategy**: Configure parent first, then children

```javascript
// Step 1: Parent
{
  "body": {
    "contentType": "json"  // Set parent first
  }
}

// Step 2: Children (structure determined by parent)
{
  "body": {
    "contentType": "json",
    "content": {           // JSON object format
      "key": "value"
    }
  }
}
```

---

## Auto-Sanitization and Dependencies

### What Auto-Sanitization Fixes

**Operator structure issues** (IF/Switch nodes):

**Example**: singleValue property
```javascript
// You configure (missing singleValue)
{
  "type": "boolean",
  "operation": "isEmpty"
  // Missing singleValue
}

// Auto-sanitization adds it
{
  "type": "boolean",
  "operation": "isEmpty",
  "singleValue": true  // ✅ Added automatically
}
```

### What It Doesn't Fix

**Missing required fields**:
```javascript
// You configure (missing channel)
{
  "resource": "message",
  "operation": "post",
  "text": "Hello"
  // Missing required field: channel
}

// Auto-sanitization does NOT add
// You must add it yourself
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",  // ← You must add
  "text": "Hello"
}
```

---

## Troubleshooting Dependencies

### Problem 1: "Field X is required but not visible"

**Error**:
```json
{
  "type": "missing_required",
  "property": "body",
  "message": "body is required"
}
```

**But you don't see body field in configuration!**

**Solution**:
```javascript
// Check field dependencies using search_properties
get_node({
  nodeType: "nodes-base.httpRequest",
  mode: "search_properties",
  propertyQuery: "body"
});

// Find that body shows when sendBody=true
// Add sendBody
{
  "method": "POST",
  "sendBody": true,  // ← Now body appears!
  "body": {...}
}
```

### Problem 2: "Field disappears when I change operation"

**Scenario**:
```javascript
// Working configuration
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",
  "text": "Hello"
}

// Change operation
{
  "resource": "message",
  "operation": "update",  // Changed
  "channel": "#general",  // Still here
  "text": "Updated"       // Still here
  // Missing: messageId (required for update!)
}
```

**Validation error**: "messageId is required"

**Why**: Different operation = different required fields

**Solution**:
```javascript
// Check requirements for new operation
get_node({
  nodeType: "nodes-base.slack"
});

// Configure for update operation
{
  "resource": "message",
  "operation": "update",
  "messageId": "1234567890",  // Required for update
  "text": "Updated",
  "channel": "#general"       // Optional for update
}
```

### Problem 3: "Validation passes but field doesn't save"

**Scenario**: Field hidden by dependencies after validation

**Example**:
```javascript
// Configure
{
  "method": "GET",
  "sendBody": true,  // ❌ GET doesn't support body
  "body": {...}      // This will be stripped
}

// After save
{
  "method": "GET"
  // body removed because method=GET hides it
}
```

**Solution**: Respect dependencies from the start

```javascript
// Correct approach - check property dependencies
get_node({
  nodeType: "nodes-base.httpRequest",
  mode: "search_properties",
  propertyQuery: "body"
});

// See that body only shows for POST/PUT/PATCH/DELETE
// Use correct method
{
  "method": "POST",
  "sendBody": true,
  "body": {...}
}
```

---

## Advanced Patterns

### Pattern 1: Conditional Required with Fallback

**Example**: Channel can be string OR expression

```javascript
// Option 1: String
{
  "channel": "#general"
}

// Option 2: Expression
{
  "channel": "={{$json.channelName}}"
}

// Validation accepts both
```

### Pattern 2: Mutually Exclusive Fields

**Example**: Use either ID or name, not both

```javascript
// Use messageId
{
  "messageId": "1234567890"
  // name not needed
}

// OR use messageName
{
  "messageName": "thread-name"
  // messageId not needed
}

// Dependencies ensure only one is required
```

### Pattern 3: Progressive Complexity

**Example**: Simple mode vs advanced mode

```javascript
// Simple mode
{
  "mode": "simple",
  "text": "{{$json.message}}"
  // Advanced fields hidden
}

// Advanced mode
{
  "mode": "advanced",
  "attachments": [...],
  "blocks": [...],
  "metadata": {...}
  // Simple field hidden, advanced fields shown
}
```

---

## Best Practices

### ✅ Do

1. **Check dependencies when stuck**
   ```javascript
   get_node({nodeType: "...", mode: "search_properties", propertyQuery: "..."});
   ```

2. **Configure parent properties first**
   ```javascript
   // First: method, resource, operation
   // Then: dependent fields
   ```

3. **Validate after changing operation**
   ```javascript
   // Operation changed → requirements changed
   validate_node({nodeType: "...", config: {...}, profile: "runtime"});
   ```

4. **Read validation errors for dependency hints**
   ```
   Error: "body required when sendBody=true"
   → Hint: Set sendBody=true to enable body
   ```

### ❌ Don't

1. **Don't ignore dependency errors**
   ```javascript
   // Error: "body not visible" → Check displayOptions
   ```

2. **Don't hardcode all possible fields**
   ```javascript
   // Bad: Adding fields that will be hidden
   ```

3. **Don't assume operations are identical**
   ```javascript
   // Each operation has unique requirements
   ```

---

## Summary

**Key Concepts**:
- `displayOptions` control field visibility
- `show` = field appears when conditions match
- `hide` = field disappears when conditions match
- Multiple conditions = AND logic
- Multiple values = OR logic

**Common Patterns**:
1. Boolean toggle (sendBody → body)
2. Resource/operation cascade (different operations → different fields)
3. Type-specific config (string vs boolean conditions)
4. Method-specific fields (GET vs POST)

**Troubleshooting**:
- Field required but not visible → Check dependencies
- Field disappears after change → Operation changed requirements
- Field doesn't save → Hidden by dependencies

**Tools**:
- `get_node({mode: "search_properties"})` - Find property dependencies
- `get_node({detail: "full"})` - See complete schema with displayOptions
- `get_node` - See operation requirements (standard detail)
- Validation errors - Hints about dependencies

**Related Files**:
- **[SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)** - Main configuration guide
- **[OPERATION_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_node_configuration/OPERATION_PATTERNS.md)** - Common patterns by node type
```

## File: `skills/n8n-node-configuration/OPERATION_PATTERNS.md`
```markdown
# Operation Patterns Guide

Common node configuration patterns organized by node type and operation.

---

## Overview

**Purpose**: Quick reference for common node configurations

**Coverage**: Top 20 most-used nodes from 525 available

**Pattern format**:
- Minimal valid configuration
- Common options
- Real-world examples
- Gotchas and tips

---

## HTTP & API Nodes

### HTTP Request (nodes-base.httpRequest)

Most versatile node for HTTP operations

#### GET Request

**Minimal**:
```javascript
{
  "method": "GET",
  "url": "https://api.example.com/users",
  "authentication": "none"
}
```

**With query parameters**:
```javascript
{
  "method": "GET",
  "url": "https://api.example.com/users",
  "authentication": "none",
  "sendQuery": true,
  "queryParameters": {
    "parameters": [
      {
        "name": "limit",
        "value": "100"
      },
      {
        "name": "offset",
        "value": "={{$json.offset}}"
      }
    ]
  }
}
```

**With authentication**:
```javascript
{
  "method": "GET",
  "url": "https://api.example.com/users",
  "authentication": "predefinedCredentialType",
  "nodeCredentialType": "httpHeaderAuth"
}
```

#### POST with JSON

**Minimal**:
```javascript
{
  "method": "POST",
  "url": "https://api.example.com/users",
  "authentication": "none",
  "sendBody": true,
  "body": {
    "contentType": "json",
    "content": {
      "name": "John Doe",
      "email": "john@example.com"
    }
  }
}
```

**With expressions**:
```javascript
{
  "method": "POST",
  "url": "https://api.example.com/users",
  "authentication": "none",
  "sendBody": true,
  "body": {
    "contentType": "json",
    "content": {
      "name": "={{$json.name}}",
      "email": "={{$json.email}}",
      "metadata": {
        "source": "n8n",
        "timestamp": "={{$now.toISO()}}"
      }
    }
  }
}
```

**Gotcha**: Remember `sendBody: true` for POST/PUT/PATCH!

#### PUT/PATCH Request

**Pattern**: Same as POST, but method changes
```javascript
{
  "method": "PUT",  // or "PATCH"
  "url": "https://api.example.com/users/123",
  "authentication": "none",
  "sendBody": true,
  "body": {
    "contentType": "json",
    "content": {
      "name": "Updated Name"
    }
  }
}
```

#### DELETE Request

**Minimal** (no body):
```javascript
{
  "method": "DELETE",
  "url": "https://api.example.com/users/123",
  "authentication": "none"
}
```

**With body** (some APIs allow):
```javascript
{
  "method": "DELETE",
  "url": "https://api.example.com/users",
  "authentication": "none",
  "sendBody": true,
  "body": {
    "contentType": "json",
    "content": {
      "ids": ["123", "456"]
    }
  }
}
```

---

### Webhook (nodes-base.webhook)

Most common trigger - 813 searches!

#### Basic Webhook

**Minimal**:
```javascript
{
  "path": "my-webhook",
  "httpMethod": "POST",
  "responseMode": "onReceived"
}
```

**Gotcha**: Webhook data is under `$json.body`, not `$json`!

```javascript
// ❌ Wrong
{
  "text": "={{$json.email}}"
}

// ✅ Correct
{
  "text": "={{$json.body.email}}"
}
```

#### Webhook with Authentication

**Header auth**:
```javascript
{
  "path": "secure-webhook",
  "httpMethod": "POST",
  "responseMode": "onReceived",
  "authentication": "headerAuth",
  "options": {
    "responseCode": 200,
    "responseData": "{\n  \"success\": true\n}"
  }
}
```

#### Webhook Returning Data

**Custom response**:
```javascript
{
  "path": "my-webhook",
  "httpMethod": "POST",
  "responseMode": "lastNode",  // Return data from last node
  "options": {
    "responseCode": 201,
    "responseHeaders": {
      "entries": [
        {
          "name": "Content-Type",
          "value": "application/json"
        }
      ]
    }
  }
}
```

---

## Communication Nodes

### Slack (nodes-base.slack)

Popular choice for AI agent workflows

#### Post Message

**Minimal**:
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",
  "text": "Hello from n8n!"
}
```

**With dynamic content**:
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "={{$json.channel}}",
  "text": "New user: {{$json.name}} ({{$json.email}})"
}
```

**With attachments**:
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "#alerts",
  "text": "Error Alert",
  "attachments": [
    {
      "color": "#ff0000",
      "fields": [
        {
          "title": "Error Type",
          "value": "={{$json.errorType}}"
        },
        {
          "title": "Timestamp",
          "value": "={{$now.toLocaleString()}}"
        }
      ]
    }
  ]
}
```

**Gotcha**: Channel must start with `#` for public channels or be a channel ID!

#### Update Message

**Minimal**:
```javascript
{
  "resource": "message",
  "operation": "update",
  "messageId": "1234567890.123456",  // From previous message post
  "text": "Updated message content"
}
```

**Note**: `messageId` required, `channel` optional (can be inferred)

#### Create Channel

**Minimal**:
```javascript
{
  "resource": "channel",
  "operation": "create",
  "name": "new-project-channel",  // Lowercase, no spaces
  "isPrivate": false
}
```

**Gotcha**: Channel name must be lowercase, no spaces, 1-80 chars!

---

### Gmail (nodes-base.gmail)

Popular for email automation

#### Send Email

**Minimal**:
```javascript
{
  "resource": "message",
  "operation": "send",
  "to": "user@example.com",
  "subject": "Hello from n8n",
  "message": "This is the email body"
}
```

**With dynamic content**:
```javascript
{
  "resource": "message",
  "operation": "send",
  "to": "={{$json.email}}",
  "subject": "Order Confirmation #{{$json.orderId}}",
  "message": "Dear {{$json.name}},\n\nYour order has been confirmed.\n\nThank you!",
  "options": {
    "ccList": "admin@example.com",
    "replyTo": "support@example.com"
  }
}
```

#### Get Email

**Minimal**:
```javascript
{
  "resource": "message",
  "operation": "getAll",
  "returnAll": false,
  "limit": 10
}
```

**With filters**:
```javascript
{
  "resource": "message",
  "operation": "getAll",
  "returnAll": false,
  "limit": 50,
  "filters": {
    "q": "is:unread from:important@example.com",
    "labelIds": ["INBOX"]
  }
}
```

---

## Database Nodes

### Postgres (nodes-base.postgres)

Database operations - 456 templates

#### Execute Query

**Minimal** (SELECT):
```javascript
{
  "operation": "executeQuery",
  "query": "SELECT * FROM users WHERE active = true LIMIT 100"
}
```

**With parameters** (SQL injection prevention):
```javascript
{
  "operation": "executeQuery",
  "query": "SELECT * FROM users WHERE email = $1 AND active = $2",
  "additionalFields": {
    "mode": "list",
    "queryParameters": "user@example.com,true"
  }
}
```

**Gotcha**: ALWAYS use parameterized queries for user input!

```javascript
// ❌ BAD - SQL injection risk!
{
  "query": "SELECT * FROM users WHERE email = '{{$json.email}}'"
}

// ✅ GOOD - Parameterized
{
  "query": "SELECT * FROM users WHERE email = $1",
  "additionalFields": {
    "mode": "list",
    "queryParameters": "={{$json.email}}"
  }
}
```

#### Insert

**Minimal**:
```javascript
{
  "operation": "insert",
  "table": "users",
  "columns": "name,email,created_at",
  "additionalFields": {
    "mode": "list",
    "queryParameters": "John Doe,john@example.com,NOW()"
  }
}
```

**With expressions**:
```javascript
{
  "operation": "insert",
  "table": "users",
  "columns": "name,email,metadata",
  "additionalFields": {
    "mode": "list",
    "queryParameters": "={{$json.name}},={{$json.email}},{{JSON.stringify($json)}}"
  }
}
```

#### Update

**Minimal**:
```javascript
{
  "operation": "update",
  "table": "users",
  "updateKey": "id",
  "columns": "name,email",
  "additionalFields": {
    "mode": "list",
    "queryParameters": "={{$json.id}},Updated Name,newemail@example.com"
  }
}
```

---

## Data Transformation Nodes

### Set (nodes-base.set)

Most used transformation - 68% of workflows!

#### Set Fixed Values

**Minimal**:
```javascript
{
  "mode": "manual",
  "duplicateItem": false,
  "assignments": {
    "assignments": [
      {
        "name": "status",
        "value": "active",
        "type": "string"
      },
      {
        "name": "count",
        "value": 100,
        "type": "number"
      }
    ]
  }
}
```

#### Set from Input Data

**Mapping data**:
```javascript
{
  "mode": "manual",
  "duplicateItem": false,
  "assignments": {
    "assignments": [
      {
        "name": "fullName",
        "value": "={{$json.firstName}} {{$json.lastName}}",
        "type": "string"
      },
      {
        "name": "email",
        "value": "={{$json.email.toLowerCase()}}",
        "type": "string"
      },
      {
        "name": "timestamp",
        "value": "={{$now.toISO()}}",
        "type": "string"
      }
    ]
  }
}
```

**Gotcha**: Use correct `type` for each field!

```javascript
// ❌ Wrong type
{
  "name": "age",
  "value": "25",      // String
  "type": "string"    // Will be string "25"
}

// ✅ Correct type
{
  "name": "age",
  "value": 25,        // Number
  "type": "number"    // Will be number 25
}
```

---

### Code (nodes-base.code)

JavaScript execution - 42% of workflows

#### Simple Transformation

**Minimal**:
```javascript
{
  "mode": "runOnceForAllItems",
  "jsCode": "return $input.all().map(item => ({\n  json: {\n    name: item.json.name.toUpperCase(),\n    email: item.json.email\n  }\n}));"
}
```

**Per-item processing**:
```javascript
{
  "mode": "runOnceForEachItem",
  "jsCode": "// Process each item\nconst data = $input.item.json;\n\nreturn {\n  json: {\n    fullName: `${data.firstName} ${data.lastName}`,\n    email: data.email.toLowerCase(),\n    timestamp: new Date().toISOString()\n  }\n};"
}
```

**Gotcha**: In Code nodes, use `$input.item.json` or `$input.all()`, NOT `{{...}}`!

```javascript
// ❌ Wrong - expressions don't work in Code nodes
{
  "jsCode": "const name = '={{$json.name}}';"
}

// ✅ Correct - direct access
{
  "jsCode": "const name = $input.item.json.name;"
}
```

---

## Conditional Nodes

### IF (nodes-base.if)

Conditional logic - 38% of workflows

#### String Comparison

**Equals** (binary):
```javascript
{
  "conditions": {
    "string": [
      {
        "value1": "={{$json.status}}",
        "operation": "equals",
        "value2": "active"
      }
    ]
  }
}
```

**Contains** (binary):
```javascript
{
  "conditions": {
    "string": [
      {
        "value1": "={{$json.email}}",
        "operation": "contains",
        "value2": "@example.com"
      }
    ]
  }
}
```

**isEmpty** (unary):
```javascript
{
  "conditions": {
    "string": [
      {
        "value1": "={{$json.email}}",
        "operation": "isEmpty"
        // No value2 - unary operator
        // singleValue: true added by auto-sanitization
      }
    ]
  }
}
```

**Gotcha**: Unary operators (isEmpty, isNotEmpty) don't need value2!

#### Number Comparison

**Greater than**:
```javascript
{
  "conditions": {
    "number": [
      {
        "value1": "={{$json.age}}",
        "operation": "larger",
        "value2": 18
      }
    ]
  }
}
```

#### Boolean Comparison

**Is true**:
```javascript
{
  "conditions": {
    "boolean": [
      {
        "value1": "={{$json.isActive}}",
        "operation": "true"
        // Unary - no value2
      }
    ]
  }
}
```

#### Multiple Conditions (AND)

**All must match**:
```javascript
{
  "conditions": {
    "string": [
      {
        "value1": "={{$json.status}}",
        "operation": "equals",
        "value2": "active"
      }
    ],
    "number": [
      {
        "value1": "={{$json.age}}",
        "operation": "larger",
        "value2": 18
      }
    ]
  },
  "combineOperation": "all"  // AND logic
}
```

#### Multiple Conditions (OR)

**Any can match**:
```javascript
{
  "conditions": {
    "string": [
      {
        "value1": "={{$json.status}}",
        "operation": "equals",
        "value2": "active"
      },
      {
        "value1": "={{$json.status}}",
        "operation": "equals",
        "value2": "pending"
      }
    ]
  },
  "combineOperation": "any"  // OR logic
}
```

---

### Switch (nodes-base.switch)

Multi-way routing - 18% of workflows

#### Basic Switch

**Minimal**:
```javascript
{
  "mode": "rules",
  "rules": {
    "rules": [
      {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.status}}",
              "operation": "equals",
              "value2": "active"
            }
          ]
        }
      },
      {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.status}}",
              "operation": "equals",
              "value2": "pending"
            }
          ]
        }
      }
    ]
  },
  "fallbackOutput": "extra"  // Catch-all for non-matching
}
```

**Gotcha**: Number of rules must match number of outputs!

---

## AI Nodes

### OpenAI (nodes-langchain.openAi)

AI operations - 234 templates

#### Chat Completion

**Minimal**:
```javascript
{
  "resource": "chat",
  "operation": "complete",
  "messages": {
    "values": [
      {
        "role": "user",
        "content": "={{$json.prompt}}"
      }
    ]
  }
}
```

**With system prompt**:
```javascript
{
  "resource": "chat",
  "operation": "complete",
  "messages": {
    "values": [
      {
        "role": "system",
        "content": "You are a helpful assistant specialized in customer support."
      },
      {
        "role": "user",
        "content": "={{$json.userMessage}}"
      }
    ]
  },
  "options": {
    "temperature": 0.7,
    "maxTokens": 500
  }
}
```

---

## Schedule Nodes

### Schedule Trigger (nodes-base.scheduleTrigger)

Time-based workflows - 28% have schedule triggers

#### Daily at Specific Time

**Minimal**:
```javascript
{
  "rule": {
    "interval": [
      {
        "field": "hours",
        "hoursInterval": 24
      }
    ],
    "hour": 9,
    "minute": 0,
    "timezone": "America/New_York"
  }
}
```

**Gotcha**: Always set timezone explicitly!

```javascript
// ❌ Bad - uses server timezone
{
  "rule": {
    "interval": [...]
  }
}

// ✅ Good - explicit timezone
{
  "rule": {
    "interval": [...],
    "timezone": "America/New_York"
  }
}
```

#### Every N Minutes

**Minimal**:
```javascript
{
  "rule": {
    "interval": [
      {
        "field": "minutes",
        "minutesInterval": 15
      }
    ]
  }
}
```

#### Cron Expression

**Advanced scheduling**:
```javascript
{
  "mode": "cron",
  "cronExpression": "0 */2 * * *",  // Every 2 hours
  "timezone": "America/New_York"
}
```

---

## Summary

**Key Patterns by Category**:

| Category | Most Common | Key Gotcha |
|---|---|---|
| HTTP/API | GET, POST JSON | Remember sendBody: true |
| Webhooks | POST receiver | Data under $json.body |
| Communication | Slack post | Channel format (#name) |
| Database | SELECT with params | Use parameterized queries |
| Transform | Set assignments | Correct type per field |
| Conditional | IF string equals | Unary vs binary operators |
| AI | OpenAI chat | System + user messages |
| Schedule | Daily at time | Set timezone explicitly |

**Configuration Approach**:
1. Use patterns as starting point
2. Adapt to your use case
3. Validate configuration
4. Iterate based on errors
5. Deploy when valid

**Related Files**:
- **[SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)** - Configuration workflow and philosophy
- **[DEPENDENCIES.md](DEPENDENCIES.md)** - Property dependency rules
```

## File: `skills/n8n-node-configuration/README.md`
```markdown
# n8n Node Configuration

Expert guidance for operation-aware node configuration with property dependencies.

## Overview

**Skill Name**: n8n Node Configuration
**Priority**: Medium
**Purpose**: Teach operation-aware configuration with progressive discovery and dependency awareness

## The Problem This Solves

Node configuration patterns:

- get_node is the primary discovery tool (18s avg from search → standard detail)
- 91.7% success rate with standard detail configuration
- 56 seconds average between configuration edits

**Key insight**: Most configurations only need standard detail, not full schema!

## What This Skill Teaches

### Core Concepts

1. **Operation-Aware Configuration**
   - Resource + operation determine required fields
   - Different operations = different requirements
   - Always check requirements when changing operation

2. **Property Dependencies**
   - Fields appear/disappear based on other field values
   - displayOptions control visibility
   - Conditional required fields
   - Understanding dependency chains

3. **Progressive Discovery**
   - Start with get_node standard detail (91.7% success)
   - Escalate to get_node({mode: "search_properties"}) if needed
   - Use get_node({detail: "full"}) only when necessary
   - Right tool for right job

4. **Configuration Workflow**
   - Identify → Discover → Configure → Validate → Iterate
   - Average 2-3 validation cycles
   - Read errors for dependency hints
   - 56 seconds between edits average

5. **Common Patterns**
   - Resource/operation nodes (Slack, Sheets)
   - HTTP-based nodes (HTTP Request, Webhook)
   - Database nodes (Postgres, MySQL)
   - Conditional logic nodes (IF, Switch)

## File Structure

```
n8n-node-configuration/
├── SKILL.md (692 lines)
│   Main configuration guide
│   - Configuration philosophy (progressive disclosure)
│   - Core concepts (operation-aware, dependencies)
│   - Configuration workflow (8-step process)
│   - get_node vs get_node({detail: "full"})
│   - Property dependencies deep dive
│   - Common node patterns (4 categories)
│   - Operation-specific examples
│   - Conditional requirements
│   - Anti-patterns and best practices
│
├── DEPENDENCIES.md (671 lines)
│   Property dependencies reference
│   - displayOptions mechanism
│   - show vs hide rules
│   - Multiple conditions (AND logic)
│   - Multiple values (OR logic)
│   - 4 common dependency patterns
│   - Using get_node({mode: "search_properties"})
│   - Complex dependency examples
│   - Nested dependencies
│   - Auto-sanitization interaction
│   - Troubleshooting guide
│   - Advanced patterns
│
├── OPERATION_PATTERNS.md (783 lines)
│   Common configurations by node type
│   - HTTP Request (GET/POST/PUT/DELETE)
│   - Webhook (basic/auth/response)
│   - Slack (post/update/create)
│   - Gmail (send/get)
│   - Postgres (query/insert/update)
│   - Set (values/mapping)
│   - Code (per-item/all-items)
│   - IF (string/number/boolean)
│   - Switch (rules/fallback)
│   - OpenAI (chat completion)
│   - Schedule (daily/interval/cron)
│   - Gotchas and tips for each
│
└── README.md (this file)
    Skill metadata and statistics
```

**Total**: ~2,146 lines across 4 files + 4 evaluations

## Usage Statistics

Configuration metrics:

| Metric | Value | Insight |
|---|---|---|
| get_node | Primary tool | Most popular discovery pattern |
| Success rate (standard) | 91.7% | Standard detail sufficient for most |
| Avg time search→get_node | 18 seconds | Fast discovery workflow |
| Avg time between edits | 56 seconds | Iterative configuration |

## Tool Usage Pattern

**Most common discovery pattern**:
```
search_nodes → get_node (18s average)
```

**Configuration cycle**:
```
get_node → configure → validate → iterate (56s avg per edit)
```

## Key Insights

### 1. Progressive Disclosure Works

**91.7% success rate** with get_node (standard detail) proves most configurations don't need full schema.

**Strategy**:
1. Start with standard detail
2. Escalate to search_properties mode if stuck
3. Use full schema only when necessary

### 2. Operations Determine Requirements

**Same node, different operation = different requirements**

Example: Slack message
- `operation="post"` → needs channel + text
- `operation="update"` → needs messageId + text (different!)

### 3. Dependencies Control Visibility

**Fields appear/disappear based on other values**

Example: HTTP Request
- `method="GET"` → body hidden
- `method="POST"` + `sendBody=true` → body required

### 4. Configuration is Iterative

**Average 56 seconds between edits** shows configuration is iterative, not one-shot.

**Normal workflow**:
1. Configure minimal
2. Validate → error
3. Add missing field
4. Validate → error
5. Adjust value
6. Validate → valid ✅

### 5. Common Gotchas Exist

**Top 5 gotchas** from patterns:
1. Webhook data under `$json.body` (not `$json`)
2. POST needs `sendBody: true`
3. Slack channel format (`#name`)
4. SQL parameterized queries (injection prevention)
5. Timezone must be explicit (schedule nodes)

## Usage Examples

### Example 1: Basic Configuration Flow

```javascript
// Step 1: Get standard info
const info = get_node({
  nodeType: "nodes-base.slack"
});

// Step 2: Configure for operation
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",
  "text": "Hello!"
}

// Step 3: Validate
validate_node({...});
// ✅ Valid!
```

### Example 2: Handling Dependencies

```javascript
// Step 1: Configure HTTP POST
{
  "method": "POST",
  "url": "https://api.example.com/create"
}

// Step 2: Validate → Error: "sendBody required"
// Step 3: Check dependencies
get_node({mode: "search_properties"})({
  nodeType: "nodes-base.httpRequest"
});
// Shows: body visible when sendBody=true

// Step 4: Fix
{
  "method": "POST",
  "url": "https://api.example.com/create",
  "sendBody": true,
  "body": {
    "contentType": "json",
    "content": {...}
  }
}
// ✅ Valid!
```

### Example 3: Operation Change

```javascript
// Initial config (post operation)
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",
  "text": "Hello"
}

// Change operation
{
  "resource": "message",
  "operation": "update",  // Changed!
  // Need to check new requirements
}

// Get standard info for update operation
get_node({nodeType: "nodes-base.slack"});
// Shows: messageId required, channel optional

// Correct config
{
  "resource": "message",
  "operation": "update",
  "messageId": "1234567890.123456",
  "text": "Updated"
}
```

## When This Skill Activates

**Trigger phrases**:
- "how to configure"
- "what fields are required"
- "property dependencies"
- "get_node vs get_node({detail: "full"})"
- "operation-specific"
- "field not visible"

**Common scenarios**:
- Configuring new nodes
- Understanding required fields
- Field appears/disappears unexpectedly
- Choosing between discovery tools
- Switching operations
- Learning common patterns

## Integration with Other Skills

### Works With:
- **n8n MCP Tools Expert** - How to call discovery tools correctly
- **n8n Validation Expert** - Interpret missing_required errors
- **n8n Expression Syntax** - Configure expression fields
- **n8n Workflow Patterns** - Apply patterns with proper node config

### Complementary:
- Use MCP Tools Expert to learn tool selection
- Use Validation Expert to fix configuration errors
- Use Expression Syntax for dynamic field values
- Use Workflow Patterns to understand node relationships

## Testing

**Evaluations**: 4 test scenarios

1. **eval-001-property-dependencies.json**
   - Tests understanding of displayOptions
   - Guides to get_node({mode: "search_properties"})
   - Explains conditional requirements

2. **eval-002-operation-specific-config.json**
   - Tests operation-aware configuration
   - Identifies resource + operation pattern
   - References OPERATION_PATTERNS.md

3. **eval-003-conditional-fields.json**
   - Tests unary vs binary operators
   - Explains singleValue dependency
   - Mentions auto-sanitization

4. **eval-004-standard-vs-full.json**
   - Tests tool selection knowledge
   - Explains progressive disclosure
   - Provides success rate statistics

## Success Metrics

**Before this skill**:
- Using get_node({detail: "full"}) for everything (slow, overwhelming)
- Not understanding property dependencies
- Confused when fields appear/disappear
- Not aware of operation-specific requirements
- Trial and error configuration

**After this skill**:
- Start with get_node standard detail (91.7% success)
- Understand displayOptions mechanism
- Predict field visibility based on dependencies
- Check requirements when changing operations
- Systematic configuration approach
- Know common patterns by node type

## Coverage

**Node types covered**: Top 20 most-used nodes

| Category | Nodes | Coverage |
|---|---|---|
| HTTP/API | HTTP Request, Webhook | Complete |
| Communication | Slack, Gmail | Common operations |
| Database | Postgres, MySQL | CRUD operations |
| Transform | Set, Code | All modes |
| Conditional | IF, Switch | All operator types |
| AI | OpenAI | Chat completion |
| Schedule | Schedule Trigger | All modes |

## Related Documentation

- **n8n-mcp MCP Server**: Provides discovery tools
- **n8n Node API**: get_node, get_node({mode: "search_properties"}), get_node({detail: "full"})
- **n8n Schema**: displayOptions mechanism, property definitions

## Version History

- **v1.0** (2025-10-20): Initial implementation
  - SKILL.md with configuration workflow
  - DEPENDENCIES.md with displayOptions deep dive
  - OPERATION_PATTERNS.md with 20+ node patterns
  - 4 evaluation scenarios

## Author

Conceived by Romuald Członkowski - [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)

Part of the n8n-skills meta-skill collection.
```

## File: `skills/n8n-node-configuration/SKILL.md`
```markdown
---
name: n8n-node-configuration
description: Operation-aware node configuration guidance. Use when configuring nodes, understanding property dependencies, determining required fields, choosing between get_node detail levels, or learning common configuration patterns by node type.
---

# n8n Node Configuration

Expert guidance for operation-aware node configuration with property dependencies.

---

## Configuration Philosophy

**Progressive disclosure**: Start minimal, add complexity as needed

Configuration best practices:
- `get_node` with `detail: "standard"` is the most used discovery pattern
- 56 seconds average between configuration edits
- Covers 95% of use cases with 1-2K tokens response

**Key insight**: Most configurations need only standard detail, not full schema!

---

## Core Concepts

### 1. Operation-Aware Configuration

**Not all fields are always required** - it depends on operation!

**Example**: Slack node
```javascript
// For operation='post'
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",  // Required for post
  "text": "Hello!"        // Required for post
}

// For operation='update'
{
  "resource": "message",
  "operation": "update",
  "messageId": "123",     // Required for update (different!)
  "text": "Updated!"      // Required for update
  // channel NOT required for update
}
```

**Key**: Resource + operation determine which fields are required!

### 2. Property Dependencies

**Fields appear/disappear based on other field values**

**Example**: HTTP Request node
```javascript
// When method='GET'
{
  "method": "GET",
  "url": "https://api.example.com"
  // sendBody not shown (GET doesn't have body)
}

// When method='POST'
{
  "method": "POST",
  "url": "https://api.example.com",
  "sendBody": true,       // Now visible!
  "body": {               // Required when sendBody=true
    "contentType": "json",
    "content": {...}
  }
}
```

**Mechanism**: displayOptions control field visibility

### 3. Progressive Discovery

**Use the right detail level**:

1. **get_node({detail: "standard"})** - DEFAULT
   - Quick overview (~1-2K tokens)
   - Required fields + common options
   - **Use first** - covers 95% of needs

2. **get_node({mode: "search_properties", propertyQuery: "..."})** (for finding specific fields)
   - Find properties by name
   - Use when looking for auth, body, headers, etc.

3. **get_node({detail: "full"})** (complete schema)
   - All properties (~3-8K tokens)
   - Use only when standard detail is insufficient

---

## Configuration Workflow

### Standard Process

```
1. Identify node type and operation
   ↓
2. Use get_node (standard detail is default)
   ↓
3. Configure required fields
   ↓
4. Validate configuration
   ↓
5. If field unclear → get_node({mode: "search_properties"})
   ↓
6. Add optional fields as needed
   ↓
7. Validate again
   ↓
8. Deploy
```

### Example: Configuring HTTP Request

**Step 1**: Identify what you need
```javascript
// Goal: POST JSON to API
```

**Step 2**: Get node info
```javascript
const info = get_node({
  nodeType: "nodes-base.httpRequest"
});

// Returns: method, url, sendBody, body, authentication required/optional
```

**Step 3**: Minimal config
```javascript
{
  "method": "POST",
  "url": "https://api.example.com/create",
  "authentication": "none"
}
```

**Step 4**: Validate
```javascript
validate_node({
  nodeType: "nodes-base.httpRequest",
  config,
  profile: "runtime"
});
// → Error: "sendBody required for POST"
```

**Step 5**: Add required field
```javascript
{
  "method": "POST",
  "url": "https://api.example.com/create",
  "authentication": "none",
  "sendBody": true
}
```

**Step 6**: Validate again
```javascript
validate_node({...});
// → Error: "body required when sendBody=true"
```

**Step 7**: Complete configuration
```javascript
{
  "method": "POST",
  "url": "https://api.example.com/create",
  "authentication": "none",
  "sendBody": true,
  "body": {
    "contentType": "json",
    "content": {
      "name": "={{$json.name}}",
      "email": "={{$json.email}}"
    }
  }
}
```

**Step 8**: Final validation
```javascript
validate_node({...});
// → Valid! ✅
```

---

## get_node Detail Levels

### Standard Detail (DEFAULT - Use This!)

**✅ Starting configuration**
```javascript
get_node({
  nodeType: "nodes-base.slack"
});
// detail="standard" is the default
```

**Returns** (~1-2K tokens):
- Required fields
- Common options
- Operation list
- Metadata

**Use**: 95% of configuration needs

### Full Detail (Use Sparingly)

**✅ When standard isn't enough**
```javascript
get_node({
  nodeType: "nodes-base.slack",
  detail: "full"
});
```

**Returns** (~3-8K tokens):
- Complete schema
- All properties
- All nested options

**Warning**: Large response, use only when standard insufficient

### Search Properties Mode

**✅ Looking for specific field**
```javascript
get_node({
  nodeType: "nodes-base.httpRequest",
  mode: "search_properties",
  propertyQuery: "auth"
});
```

**Use**: Find authentication, headers, body fields, etc.

### Decision Tree

```
┌─────────────────────────────────┐
│ Starting new node config?       │
├─────────────────────────────────┤
│ YES → get_node (standard)       │
└─────────────────────────────────┘
         ↓
┌─────────────────────────────────┐
│ Standard has what you need?     │
├─────────────────────────────────┤
│ YES → Configure with it         │
│ NO  → Continue                  │
└─────────────────────────────────┘
         ↓
┌─────────────────────────────────┐
│ Looking for specific field?     │
├─────────────────────────────────┤
│ YES → search_properties mode    │
│ NO  → Continue                  │
└─────────────────────────────────┘
         ↓
┌─────────────────────────────────┐
│ Still need more details?        │
├─────────────────────────────────┤
│ YES → get_node({detail: "full"})│
└─────────────────────────────────┘
```

---

## Property Dependencies Deep Dive

### displayOptions Mechanism

**Fields have visibility rules**:

```javascript
{
  "name": "body",
  "displayOptions": {
    "show": {
      "sendBody": [true],
      "method": ["POST", "PUT", "PATCH"]
    }
  }
}
```

**Translation**: "body" field shows when:
- sendBody = true AND
- method = POST, PUT, or PATCH

### Common Dependency Patterns

#### Pattern 1: Boolean Toggle

**Example**: HTTP Request sendBody
```javascript
// sendBody controls body visibility
{
  "sendBody": true   // → body field appears
}
```

#### Pattern 2: Operation Switch

**Example**: Slack resource/operation
```javascript
// Different operations → different fields
{
  "resource": "message",
  "operation": "post"
  // → Shows: channel, text, attachments, etc.
}

{
  "resource": "message",
  "operation": "update"
  // → Shows: messageId, text (different fields!)
}
```

#### Pattern 3: Type Selection

**Example**: IF node conditions
```javascript
{
  "type": "string",
  "operation": "contains"
  // → Shows: value1, value2
}

{
  "type": "boolean",
  "operation": "equals"
  // → Shows: value1, value2, different operators
}
```

### Finding Property Dependencies

**Use get_node with search_properties mode**:
```javascript
get_node({
  nodeType: "nodes-base.httpRequest",
  mode: "search_properties",
  propertyQuery: "body"
});

// Returns property paths matching "body" with descriptions
```

**Or use full detail for complete schema**:
```javascript
get_node({
  nodeType: "nodes-base.httpRequest",
  detail: "full"
});

// Returns complete schema with displayOptions rules
```

**Use this when**: Validation fails and you don't understand why field is missing/required

---

## Common Node Patterns

### Pattern 1: Resource/Operation Nodes

**Examples**: Slack, Google Sheets, Airtable

**Structure**:
```javascript
{
  "resource": "<entity>",      // What type of thing
  "operation": "<action>",     // What to do with it
  // ... operation-specific fields
}
```

**How to configure**:
1. Choose resource
2. Choose operation
3. Use get_node to see operation-specific requirements
4. Configure required fields

### Pattern 2: HTTP-Based Nodes

**Examples**: HTTP Request, Webhook

**Structure**:
```javascript
{
  "method": "<HTTP_METHOD>",
  "url": "<endpoint>",
  "authentication": "<type>",
  // ... method-specific fields
}
```

**Dependencies**:
- POST/PUT/PATCH → sendBody available
- sendBody=true → body required
- authentication != "none" → credentials required

### Pattern 3: Database Nodes

**Examples**: Postgres, MySQL, MongoDB

**Structure**:
```javascript
{
  "operation": "<query|insert|update|delete>",
  // ... operation-specific fields
}
```

**Dependencies**:
- operation="executeQuery" → query required
- operation="insert" → table + values required
- operation="update" → table + values + where required

### Pattern 4: Conditional Logic Nodes

**Examples**: IF, Switch, Merge

**Structure**:
```javascript
{
  "conditions": {
    "<type>": [
      {
        "operation": "<operator>",
        "value1": "...",
        "value2": "..."  // Only for binary operators
      }
    ]
  }
}
```

**Dependencies**:
- Binary operators (equals, contains, etc.) → value1 + value2
- Unary operators (isEmpty, isNotEmpty) → value1 only + singleValue: true

---

## Operation-Specific Configuration

### Slack Node Examples

#### Post Message
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",      // Required
  "text": "Hello!",           // Required
  "attachments": [],          // Optional
  "blocks": []                // Optional
}
```

#### Update Message
```javascript
{
  "resource": "message",
  "operation": "update",
  "messageId": "1234567890",  // Required (different from post!)
  "text": "Updated!",         // Required
  "channel": "#general"       // Optional (can be inferred)
}
```

#### Create Channel
```javascript
{
  "resource": "channel",
  "operation": "create",
  "name": "new-channel",      // Required
  "isPrivate": false          // Optional
  // Note: text NOT required for this operation
}
```

### HTTP Request Node Examples

#### GET Request
```javascript
{
  "method": "GET",
  "url": "https://api.example.com/users",
  "authentication": "predefinedCredentialType",
  "nodeCredentialType": "httpHeaderAuth",
  "sendQuery": true,                    // Optional
  "queryParameters": {                  // Shows when sendQuery=true
    "parameters": [
      {
        "name": "limit",
        "value": "100"
      }
    ]
  }
}
```

#### POST with JSON
```javascript
{
  "method": "POST",
  "url": "https://api.example.com/users",
  "authentication": "none",
  "sendBody": true,                     // Required for POST
  "body": {                             // Required when sendBody=true
    "contentType": "json",
    "content": {
      "name": "John Doe",
      "email": "john@example.com"
    }
  }
}
```

### IF Node Examples

#### String Comparison (Binary)
```javascript
{
  "conditions": {
    "string": [
      {
        "value1": "={{$json.status}}",
        "operation": "equals",
        "value2": "active"              // Binary: needs value2
      }
    ]
  }
}
```

#### Empty Check (Unary)
```javascript
{
  "conditions": {
    "string": [
      {
        "value1": "={{$json.email}}",
        "operation": "isEmpty",
        // No value2 - unary operator
        "singleValue": true             // Auto-added by sanitization
      }
    ]
  }
}
```

---

## Handling Conditional Requirements

### Example: HTTP Request Body

**Scenario**: body field required, but only sometimes

**Rule**:
```
body is required when:
  - sendBody = true AND
  - method IN (POST, PUT, PATCH, DELETE)
```

**How to discover**:
```javascript
// Option 1: Read validation error
validate_node({...});
// Error: "body required when sendBody=true"

// Option 2: Search for the property
get_node({
  nodeType: "nodes-base.httpRequest",
  mode: "search_properties",
  propertyQuery: "body"
});
// Shows: body property with displayOptions rules

// Option 3: Try minimal config and iterate
// Start without body, validation will tell you if needed
```

### Example: IF Node singleValue

**Scenario**: singleValue property appears for unary operators

**Rule**:
```
singleValue should be true when:
  - operation IN (isEmpty, isNotEmpty, true, false)
```

**Good news**: Auto-sanitization fixes this!

**Manual check**:
```javascript
get_node({
  nodeType: "nodes-base.if",
  detail: "full"
});
// Shows complete schema with operator-specific rules
```

---

## Configuration Anti-Patterns

### ❌ Don't: Over-configure Upfront

**Bad**:
```javascript
// Adding every possible field
{
  "method": "GET",
  "url": "...",
  "sendQuery": false,
  "sendHeaders": false,
  "sendBody": false,
  "timeout": 10000,
  "ignoreResponseCode": false,
  // ... 20 more optional fields
}
```

**Good**:
```javascript
// Start minimal
{
  "method": "GET",
  "url": "...",
  "authentication": "none"
}
// Add fields only when needed
```

### ❌ Don't: Skip Validation

**Bad**:
```javascript
// Configure and deploy without validating
const config = {...};
n8n_update_partial_workflow({...});  // YOLO
```

**Good**:
```javascript
// Validate before deploying
const config = {...};
const result = validate_node({...});
if (result.valid) {
  n8n_update_partial_workflow({...});
}
```

### ❌ Don't: Ignore Operation Context

**Bad**:
```javascript
// Same config for all Slack operations
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",
  "text": "..."
}

// Then switching operation without updating config
{
  "resource": "message",
  "operation": "update",  // Changed
  "channel": "#general",  // Wrong field for update!
  "text": "..."
}
```

**Good**:
```javascript
// Check requirements when changing operation
get_node({
  nodeType: "nodes-base.slack"
});
// See what update operation needs (messageId, not channel)
```

---

## Best Practices

### ✅ Do

1. **Start with get_node (standard detail)**
   - ~1-2K tokens response
   - Covers 95% of configuration needs
   - Default detail level

2. **Validate iteratively**
   - Configure → Validate → Fix → Repeat
   - Average 2-3 iterations is normal
   - Read validation errors carefully

3. **Use search_properties mode when stuck**
   - If field seems missing, search for it
   - Understand what controls field visibility
   - `get_node({mode: "search_properties", propertyQuery: "..."})`

4. **Respect operation context**
   - Different operations = different requirements
   - Always check get_node when changing operation
   - Don't assume configs are transferable

5. **Trust auto-sanitization**
   - Operator structure fixed automatically
   - Don't manually add/remove singleValue
   - IF/Switch metadata added on save

### ❌ Don't

1. **Jump to detail="full" immediately**
   - Try standard detail first
   - Only escalate if needed
   - Full schema is 3-8K tokens

2. **Configure blindly**
   - Always validate before deploying
   - Understand why fields are required
   - Use search_properties for conditional fields

3. **Copy configs without understanding**
   - Different operations need different fields
   - Validate after copying
   - Adjust for new context

4. **Manually fix auto-sanitization issues**
   - Let auto-sanitization handle operator structure
   - Focus on business logic
   - Save and let system fix structure

---

## Detailed References

For comprehensive guides on specific topics:

- **[DEPENDENCIES.md](DEPENDENCIES.md)** - Deep dive into property dependencies and displayOptions
- **[OPERATION_PATTERNS.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_node_configuration/OPERATION_PATTERNS.md)** - Common configuration patterns by node type

---

## Summary

**Configuration Strategy**:
1. Start with `get_node` (standard detail is default)
2. Configure required fields for operation
3. Validate configuration
4. Search properties if stuck
5. Iterate until valid (avg 2-3 cycles)
6. Deploy with confidence

**Key Principles**:
- **Operation-aware**: Different operations = different requirements
- **Progressive disclosure**: Start minimal, add as needed
- **Dependency-aware**: Understand field visibility rules
- **Validation-driven**: Let validation guide configuration

**Related Skills**:
- **n8n MCP Tools Expert** - How to use discovery tools correctly
- **n8n Validation Expert** - Interpret validation errors
- **n8n Expression Syntax** - Configure expression fields
- **n8n Workflow Patterns** - Apply patterns with proper configuration
```

## File: `skills/n8n-validation-expert/ERROR_CATALOG.md`
```markdown
# Error Catalog

Comprehensive catalog of n8n validation errors with real examples and fixes.

---

## Error Types Overview

Common validation errors by priority:

| Error Type | Priority | Severity | Auto-Fix |
|---|---|---|---|
| missing_required | Highest | Error | ❌ |
| invalid_value | High | Error | ❌ |
| type_mismatch | Medium | Error | ❌ |
| invalid_expression | Medium | Error | ❌ |
| invalid_reference | Low | Error | ❌ |
| operator_structure | Lowest | Warning | ✅ |

---

## Errors (Must Fix)

### 1. missing_required

**What it means**: Required field is not provided in node configuration

**When it occurs**:
- Creating new nodes without all required fields
- Copying configurations between different operations
- Switching operations that have different requirements

**Most common validation error**

#### Example 1: Slack Channel Missing

**Error**:
```json
{
  "type": "missing_required",
  "property": "channel",
  "message": "Channel name is required",
  "node": "Slack",
  "path": "parameters.channel"
}
```

**Broken Configuration**:
```javascript
{
  "resource": "message",
  "operation": "post"
  // Missing: channel
}
```

**Fix**:
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "#general"  // ✅ Added required field
}
```

**How to identify required fields**:
```javascript
// Use get_node to see what's required
const info = get_node({
  nodeType: "nodes-base.slack"
});
// Check properties marked as "required": true
```

#### Example 2: HTTP Request Missing URL

**Error**:
```json
{
  "type": "missing_required",
  "property": "url",
  "message": "URL is required for HTTP Request",
  "node": "HTTP Request",
  "path": "parameters.url"
}
```

**Broken Configuration**:
```javascript
{
  "method": "GET",
  "authentication": "none"
  // Missing: url
}
```

**Fix**:
```javascript
{
  "method": "GET",
  "authentication": "none",
  "url": "https://api.example.com/data"  // ✅ Added
}
```

#### Example 3: Database Query Missing Connection

**Error**:
```json
{
  "type": "missing_required",
  "property": "query",
  "message": "SQL query is required",
  "node": "Postgres",
  "path": "parameters.query"
}
```

**Broken Configuration**:
```javascript
{
  "operation": "executeQuery"
  // Missing: query
}
```

**Fix**:
```javascript
{
  "operation": "executeQuery",
  "query": "SELECT * FROM users WHERE active = true"  // ✅ Added
}
```

#### Example 4: Conditional Fields

**Error**:
```json
{
  "type": "missing_required",
  "property": "body",
  "message": "Request body is required when sendBody is true",
  "node": "HTTP Request",
  "path": "parameters.body"
}
```

**Broken Configuration**:
```javascript
{
  "method": "POST",
  "url": "https://api.example.com/create",
  "sendBody": true
  // Missing: body (required when sendBody=true)
}
```

**Fix**:
```javascript
{
  "method": "POST",
  "url": "https://api.example.com/create",
  "sendBody": true,
  "body": {
    "contentType": "json",
    "content": {
      "name": "John",
      "email": "john@example.com"
    }
  }  // ✅ Added conditional required field
}
```

---

### 2. invalid_value

**What it means**: Provided value doesn't match allowed options or format

**When it occurs**:
- Using wrong enum value
- Typos in operation names
- Invalid format for specialized fields (emails, URLs, channels)

**Second most common error**

#### Example 1: Invalid Operation

**Error**:
```json
{
  "type": "invalid_value",
  "property": "operation",
  "message": "Operation must be one of: post, update, delete, get",
  "current": "send",
  "allowed": ["post", "update", "delete", "get"]
}
```

**Broken Configuration**:
```javascript
{
  "resource": "message",
  "operation": "send"  // ❌ Invalid - should be "post"
}
```

**Fix**:
```javascript
{
  "resource": "message",
  "operation": "post"  // ✅ Use valid operation
}
```

#### Example 2: Invalid HTTP Method

**Error**:
```json
{
  "type": "invalid_value",
  "property": "method",
  "message": "Method must be one of: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS",
  "current": "FETCH",
  "allowed": ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"]
}
```

**Broken Configuration**:
```javascript
{
  "method": "FETCH",  // ❌ Invalid
  "url": "https://api.example.com"
}
```

**Fix**:
```javascript
{
  "method": "GET",  // ✅ Use valid HTTP method
  "url": "https://api.example.com"
}
```

#### Example 3: Invalid Channel Format

**Error**:
```json
{
  "type": "invalid_value",
  "property": "channel",
  "message": "Channel name must start with # and be lowercase (e.g., #general)",
  "current": "General"
}
```

**Broken Configuration**:
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "General"  // ❌ Wrong format
}
```

**Fix**:
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "#general"  // ✅ Correct format
}
```

#### Example 4: Invalid Enum with Case Sensitivity

**Error**:
```json
{
  "type": "invalid_value",
  "property": "resource",
  "message": "Resource must be one of: channel, message, user, file",
  "current": "Message",
  "allowed": ["channel", "message", "user", "file"]
}
```

**Note**: Enums are case-sensitive!

**Broken Configuration**:
```javascript
{
  "resource": "Message",  // ❌ Capital M
  "operation": "post"
}
```

**Fix**:
```javascript
{
  "resource": "message",  // ✅ Lowercase
  "operation": "post"
}
```

---

### 3. type_mismatch

**What it means**: Value is wrong data type (string instead of number, etc.)

**When it occurs**:
- Hardcoding values that should be numbers
- Using expressions where literals are expected
- JSON serialization issues

**Common error**

#### Example 1: String Instead of Number

**Error**:
```json
{
  "type": "type_mismatch",
  "property": "limit",
  "message": "Expected number, got string",
  "expected": "number",
  "current": "100"
}
```

**Broken Configuration**:
```javascript
{
  "operation": "executeQuery",
  "query": "SELECT * FROM users",
  "limit": "100"  // ❌ String
}
```

**Fix**:
```javascript
{
  "operation": "executeQuery",
  "query": "SELECT * FROM users",
  "limit": 100  // ✅ Number
}
```

#### Example 2: Number Instead of String

**Error**:
```json
{
  "type": "type_mismatch",
  "property": "channel",
  "message": "Expected string, got number",
  "expected": "string",
  "current": 12345
}
```

**Broken Configuration**:
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": 12345  // ❌ Number (even if channel ID)
}
```

**Fix**:
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "#general"  // ✅ String (channel name, not ID)
}
```

#### Example 3: Boolean as String

**Error**:
```json
{
  "type": "type_mismatch",
  "property": "sendHeaders",
  "message": "Expected boolean, got string",
  "expected": "boolean",
  "current": "true"
}
```

**Broken Configuration**:
```javascript
{
  "method": "GET",
  "url": "https://api.example.com",
  "sendHeaders": "true"  // ❌ String "true"
}
```

**Fix**:
```javascript
{
  "method": "GET",
  "url": "https://api.example.com",
  "sendHeaders": true  // ✅ Boolean true
}
```

#### Example 4: Object Instead of Array

**Error**:
```json
{
  "type": "type_mismatch",
  "property": "tags",
  "message": "Expected array, got object",
  "expected": "array",
  "current": {"tag": "important"}
}
```

**Broken Configuration**:
```javascript
{
  "name": "New Channel",
  "tags": {"tag": "important"}  // ❌ Object
}
```

**Fix**:
```javascript
{
  "name": "New Channel",
  "tags": ["important", "alerts"]  // ✅ Array
}
```

---

### 4. invalid_expression

**What it means**: n8n expression has syntax errors or invalid references

**When it occurs**:
- Missing `{{}}` around expressions
- Typos in variable names
- Referencing non-existent nodes or fields
- Invalid JavaScript syntax in expressions

**Moderately common**

**Related**: See **n8n Expression Syntax** skill for comprehensive expression guidance

#### Example 1: Missing Curly Braces

**Error**:
```json
{
  "type": "invalid_expression",
  "property": "text",
  "message": "Expressions must be wrapped in {{}}",
  "current": "$json.name"
}
```

**Broken Configuration**:
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",
  "text": "$json.name"  // ❌ Missing {{}}
}
```

**Fix**:
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",
  "text": "={{$json.name}}"  // ✅ Wrapped in {{}}
}
```

#### Example 2: Invalid Node Reference

**Error**:
```json
{
  "type": "invalid_expression",
  "property": "value",
  "message": "Referenced node 'HTTP Requets' does not exist",
  "current": "={{$node['HTTP Requets'].json.data}}"
}
```

**Broken Configuration**:
```javascript
{
  "field": "data",
  "value": "={{$node['HTTP Requets'].json.data}}"  // ❌ Typo in node name
}
```

**Fix**:
```javascript
{
  "field": "data",
  "value": "={{$node['HTTP Request'].json.data}}"  // ✅ Correct node name
}
```

#### Example 3: Invalid Property Access

**Error**:
```json
{
  "type": "invalid_expression",
  "property": "text",
  "message": "Cannot access property 'user' of undefined",
  "current": "={{$json.data.user.name}}"
}
```

**Broken Configuration**:
```javascript
{
  "text": "={{$json.data.user.name}}"  // ❌ Structure doesn't exist
}
```

**Fix** (with safe navigation):
```javascript
{
  "text": "={{$json.data?.user?.name || 'Unknown'}}"  // ✅ Safe navigation + fallback
}
```

#### Example 4: Webhook Data Access Error

**Error**:
```json
{
  "type": "invalid_expression",
  "property": "value",
  "message": "Property 'email' not found in $json",
  "current": "={{$json.email}}"
}
```

**Common Gotcha**: Webhook data is under `.body`!

**Broken Configuration**:
```javascript
{
  "field": "email",
  "value": "={{$json.email}}"  // ❌ Missing .body
}
```

**Fix**:
```javascript
{
  "field": "email",
  "value": "={{$json.body.email}}"  // ✅ Webhook data under .body
}
```

---

### 5. invalid_reference

**What it means**: Configuration references a node that doesn't exist in the workflow

**When it occurs**:
- Node was renamed or deleted
- Typo in node name
- Copy-pasting from another workflow

**Less common error**

#### Example 1: Deleted Node Reference

**Error**:
```json
{
  "type": "invalid_reference",
  "property": "expression",
  "message": "Node 'Transform Data' does not exist in workflow",
  "referenced_node": "Transform Data"
}
```

**Broken Configuration**:
```javascript
{
  "value": "={{$node['Transform Data'].json.result}}"  // ❌ Node deleted
}
```

**Fix**:
```javascript
// Option 1: Update to existing node
{
  "value": "={{$node['Set'].json.result}}"
}

// Option 2: Remove expression if not needed
{
  "value": "default_value"
}
```

#### Example 2: Connection to Non-Existent Node

**Error**:
```json
{
  "type": "invalid_reference",
  "message": "Connection references node 'Slack1' which does not exist",
  "source": "HTTP Request",
  "target": "Slack1"
}
```

**Fix**: Use `cleanStaleConnections` operation:
```javascript
n8n_update_partial_workflow({
  id: "workflow-id",
  operations: [{
    type: "cleanStaleConnections"
  }]
})
```

#### Example 3: Renamed Node Not Updated

**Error**:
```json
{
  "type": "invalid_reference",
  "property": "expression",
  "message": "Node 'Get Weather' does not exist (did you mean 'Weather API'?)",
  "referenced_node": "Get Weather",
  "suggestions": ["Weather API"]
}
```

**Broken Configuration**:
```javascript
{
  "value": "={{$node['Get Weather'].json.temperature}}"  // ❌ Old name
}
```

**Fix**:
```javascript
{
  "value": "={{$node['Weather API'].json.temperature}}"  // ✅ Current name
}
```

---

## Warnings (Should Fix)

### 6. best_practice

**What it means**: Configuration works but doesn't follow best practices

**Severity**: Warning (doesn't block execution)

**When acceptable**: Development, testing, simple workflows

**When to fix**: Production workflows, critical operations

#### Example 1: Missing Error Handling

**Warning**:
```json
{
  "type": "best_practice",
  "property": "onError",
  "message": "Slack API can have rate limits and connection issues",
  "suggestion": "Add error handling: onError: 'continueRegularOutput'"
}
```

**Current Configuration**:
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "#alerts"
  // No error handling ⚠️
}
```

**Recommended Fix**:
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "#alerts",
  "continueOnFail": true,
  "retryOnFail": true,
  "maxTries": 3
}
```

#### Example 2: No Retry Logic

**Warning**:
```json
{
  "type": "best_practice",
  "property": "retryOnFail",
  "message": "External API calls should retry on failure",
  "suggestion": "Add retryOnFail: true, maxTries: 3, waitBetweenTries: 1000"
}
```

**When to ignore**: Idempotent operations, APIs with their own retry logic

**When to fix**: Flaky external services, production automation

---

### 7. deprecated

**What it means**: Using old API version or deprecated feature

**Severity**: Warning (still works but may stop working in future)

**When to fix**: Always (eventually)

#### Example 1: Old typeVersion

**Warning**:
```json
{
  "type": "deprecated",
  "property": "typeVersion",
  "message": "typeVersion 1 is deprecated for Slack node, use version 2",
  "current": 1,
  "recommended": 2
}
```

**Fix**:
```javascript
{
  "type": "n8n-nodes-base.slack",
  "typeVersion": 2,  // ✅ Updated
  // May need to update configuration for new version
}
```

---

### 8. performance

**What it means**: Configuration may cause performance issues

**Severity**: Warning

**When to fix**: High-volume workflows, large datasets

#### Example 1: Unbounded Query

**Warning**:
```json
{
  "type": "performance",
  "property": "query",
  "message": "SELECT without LIMIT can return massive datasets",
  "suggestion": "Add LIMIT clause or use pagination"
}
```

**Current**:
```sql
SELECT * FROM users WHERE active = true
```

**Fix**:
```sql
SELECT * FROM users WHERE active = true LIMIT 1000
```

---

## Auto-Sanitization Fixes

### 9. operator_structure

**What it means**: IF/Switch operator structure issues

**Severity**: Warning

**Auto-Fix**: ✅ YES - Fixed automatically on workflow save

**Rare** (mostly auto-fixed)

#### Fixed Automatically: Binary Operators

**Before** (you create this):
```javascript
{
  "type": "boolean",
  "operation": "equals",
  "singleValue": true  // ❌ Wrong for binary operator
}
```

**After** (auto-sanitization fixes it):
```javascript
{
  "type": "boolean",
  "operation": "equals"
  // singleValue removed ✅
}
```

**You don't need to do anything** - this is fixed on save!

#### Fixed Automatically: Unary Operators

**Before**:
```javascript
{
  "type": "boolean",
  "operation": "isEmpty"
  // Missing singleValue ❌
}
```

**After**:
```javascript
{
  "type": "boolean",
  "operation": "isEmpty",
  "singleValue": true  // ✅ Added automatically
}
```

**What you should do**: Trust auto-sanitization, don't manually fix these!

---

## Recovery Patterns

### Pattern 1: Progressive Validation

**Problem**: Too many errors at once

**Solution**:
```javascript
// Step 1: Minimal valid config
let config = {
  resource: "message",
  operation: "post",
  channel: "#general",
  text: "Hello"
};

validate_node({nodeType: "nodes-base.slack", config, profile: "runtime"});
// ✅ Valid

// Step 2: Add features one by one
config.attachments = [...];
validate_node({nodeType: "nodes-base.slack", config, profile: "runtime"});

config.blocks = [...];
validate_node({nodeType: "nodes-base.slack", config, profile: "runtime"});
```

### Pattern 2: Error Triage

**Problem**: Multiple errors

**Solution**:
```javascript
const result = validate_node({...});

// 1. Fix errors (must fix)
result.errors.forEach(error => {
  console.log(`MUST FIX: ${error.property} - ${error.message}`);
});

// 2. Review warnings (should fix)
result.warnings.forEach(warning => {
  console.log(`SHOULD FIX: ${warning.property} - ${warning.message}`);
});

// 3. Consider suggestions (optional)
result.suggestions.forEach(sug => {
  console.log(`OPTIONAL: ${sug.message}`);
});
```

### Pattern 3: Use get_node

**Problem**: Don't know what's required

**Solution**:
```javascript
// Before configuring, check requirements
const info = get_node({
  nodeType: "nodes-base.slack"
});

// Look for required fields
info.properties.forEach(prop => {
  if (prop.required) {
    console.log(`Required: ${prop.name} (${prop.type})`);
  }
});
```

---

## Summary

**Most Common Errors**:
1. `missing_required` (45%) - Always check get_node
2. `invalid_value` (28%) - Check allowed values
3. `type_mismatch` (12%) - Use correct data types
4. `invalid_expression` (8%) - Use Expression Syntax skill
5. `invalid_reference` (5%) - Clean stale connections

**Auto-Fixed**:
- `operator_structure` - Trust auto-sanitization!

**Related Skills**:
- **[SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)** - Main validation guide
- **[FALSE_POSITIVES.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_validation_expert/FALSE_POSITIVES.md)** - When to ignore warnings
- **n8n Expression Syntax** - Fix expression errors
- **n8n MCP Tools Expert** - Use validation tools correctly
```

## File: `skills/n8n-validation-expert/FALSE_POSITIVES.md`
```markdown
# False Positives Guide

When validation warnings are acceptable and how to handle them.

---

## What Are False Positives?

**Definition**: Validation warnings that are technically "issues" but acceptable in your specific use case.

**Key insight**: Not all warnings need to be fixed!

Many warnings are context-dependent:
- ~40% of warnings are acceptable in specific use cases
- Using `ai-friendly` profile reduces false positives by 60%

---

## Philosophy

### ✅ Good Practice
```
1. Run validation with 'runtime' profile
2. Fix all ERRORS
3. Review each WARNING
4. Decide if acceptable for your use case
5. Document why you accepted it
6. Deploy with confidence
```

### ❌ Bad Practice
```
1. Ignore all warnings blindly
2. Use 'minimal' profile to avoid warnings
3. Deploy without understanding risks
```

---

## Common False Positives

### 1. Missing Error Handling

**Warning**:
```json
{
  "type": "best_practice",
  "message": "No error handling configured",
  "suggestion": "Add continueOnFail: true and retryOnFail: true"
}
```

#### When Acceptable

**✅ Development/Testing Workflows**
```javascript
// Testing workflow - failures are obvious
{
  "name": "Test Slack Integration",
  "nodes": [{
    "type": "n8n-nodes-base.slack",
    "parameters": {
      "resource": "message",
      "operation": "post",
      "channel": "#test"
      // No error handling - OK for testing
    }
  }]
}
```

**Reasoning**: You WANT to see failures during testing.

**✅ Non-Critical Notifications**
```javascript
// Nice-to-have notification
{
  "name": "Optional Slack Notification",
  "parameters": {
    "channel": "#general",
    "text": "FYI: Process completed"
    // If this fails, no big deal
  }
}
```

**Reasoning**: Notification failure doesn't affect core functionality.

**✅ Manual Trigger Workflows**
```javascript
// Manual workflow - user is watching
{
  "nodes": [{
    "type": "n8n-nodes-base.webhook",
    "parameters": {
      "path": "manual-test"
      // No error handling - user will retry manually
    }
  }]
}
```

**Reasoning**: User is present to see and handle errors.

#### When to Fix

**❌ Production Automation**
```javascript
// BAD: Critical workflow without error handling
{
  "name": "Process Customer Orders",
  "nodes": [{
    "type": "n8n-nodes-base.postgres",
    "parameters": {
      "query": "INSERT INTO orders..."
      // ❌ Should have error handling!
    }
  }]
}
```

**Fix**:
```javascript
{
  "parameters": {
    "query": "INSERT INTO orders...",
    "continueOnFail": true,
    "retryOnFail": true,
    "maxTries": 3,
    "waitBetweenTries": 1000
  }
}
```

**❌ Critical Integrations**
```javascript
// BAD: Payment processing without error handling
{
  "name": "Process Payment",
  "type": "n8n-nodes-base.stripe"
  // ❌ Payment failures MUST be handled!
}
```

---

### 2. No Retry Logic

**Warning**:
```json
{
  "type": "best_practice",
  "message": "External API calls should retry on failure",
  "suggestion": "Add retryOnFail: true with exponential backoff"
}
```

#### When Acceptable

**✅ APIs with Built-in Retry**
```javascript
// Stripe has its own retry mechanism
{
  "type": "n8n-nodes-base.stripe",
  "parameters": {
    "resource": "charge",
    "operation": "create"
    // Stripe SDK retries automatically
  }
}
```

**✅ Idempotent Operations**
```javascript
// GET request - safe to retry manually if needed
{
  "method": "GET",
  "url": "https://api.example.com/status"
  // Read-only, no side effects
}
```

**✅ Local/Internal Services**
```javascript
// Internal API with high reliability
{
  "url": "http://localhost:3000/process"
  // Local service, failures are rare and obvious
}
```

#### When to Fix

**❌ Flaky External APIs**
```javascript
// BAD: Known unreliable API without retries
{
  "url": "https://unreliable-api.com/data"
  // ❌ Should retry!
}

// GOOD:
{
  "url": "https://unreliable-api.com/data",
  "retryOnFail": true,
  "maxTries": 3,
  "waitBetweenTries": 2000
}
```

**❌ Non-Idempotent Operations**
```javascript
// BAD: POST without retry - may lose data
{
  "method": "POST",
  "url": "https://api.example.com/create"
  // ❌ Could timeout and lose data
}
```

---

### 3. Missing Rate Limiting

**Warning**:
```json
{
  "type": "best_practice",
  "message": "API may have rate limits",
  "suggestion": "Add rate limiting or batch requests"
}
```

#### When Acceptable

**✅ Internal APIs**
```javascript
// Internal microservice - no rate limits
{
  "url": "http://internal-api/process"
  // Company controls both ends
}
```

**✅ Low-Volume Workflows**
```javascript
// Runs once per day
{
  "trigger": {
    "type": "n8n-nodes-base.cron",
    "parameters": {
      "mode": "everyDay",
      "hour": 9
    }
  },
  "nodes": [{
    "type": "n8n-nodes-base.httpRequest",
    "parameters": {
      "url": "https://api.example.com/daily-report"
      // Once per day = no rate limit concerns
    }
  }]
}
```

**✅ APIs with Server-Side Limits**
```javascript
// API returns 429 and n8n handles it
{
  "url": "https://api.example.com/data",
  "options": {
    "response": {
      "response": {
        "neverError": false  // Will error on 429
      }
    }
  },
  "retryOnFail": true  // Retry on 429
}
```

#### When to Fix

**❌ High-Volume Public APIs**
```javascript
// BAD: Loop hitting rate-limited API
{
  "nodes": [{
    "type": "n8n-nodes-base.splitInBatches",
    "parameters": {
      "batchSize": 100
    }
  }, {
    "type": "n8n-nodes-base.httpRequest",
    "parameters": {
      "url": "https://api.github.com/..."
      // ❌ GitHub has strict rate limits!
    }
  }]
}

// GOOD: Add rate limiting
{
  "type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "url": "https://api.github.com/...",
    "options": {
      "batching": {
        "batch": {
          "batchSize": 10,
          "batchInterval": 1000  // 1 second between batches
        }
      }
    }
  }
}
```

---

### 4. Unbounded Database Queries

**Warning**:
```json
{
  "type": "performance",
  "message": "SELECT without LIMIT can return massive datasets",
  "suggestion": "Add LIMIT clause or use pagination"
}
```

#### When Acceptable

**✅ Small Known Datasets**
```javascript
// Config table with ~10 rows
{
  "query": "SELECT * FROM app_config"
  // Known to be small, no LIMIT needed
}
```

**✅ Aggregation Queries**
```javascript
// COUNT/SUM operations
{
  "query": "SELECT COUNT(*) as total FROM users WHERE active = true"
  // Aggregation, not returning rows
}
```

**✅ Development/Testing**
```javascript
// Testing with small dataset
{
  "query": "SELECT * FROM test_users"
  // Test database has 5 rows
}
```

#### When to Fix

**❌ Production Queries on Large Tables**
```javascript
// BAD: User table could have millions of rows
{
  "query": "SELECT * FROM users"
  // ❌ Could return millions of rows!
}

// GOOD: Add LIMIT
{
  "query": "SELECT * FROM users LIMIT 1000"
}

// BETTER: Use pagination
{
  "query": "SELECT * FROM users WHERE id > {{$json.lastId}} LIMIT 1000"
}
```

---

### 5. Missing Input Validation

**Warning**:
```json
{
  "type": "best_practice",
  "message": "Webhook doesn't validate input data",
  "suggestion": "Add IF node to validate required fields"
}
```

#### When Acceptable

**✅ Internal Webhooks**
```javascript
// Webhook from your own backend
{
  "type": "n8n-nodes-base.webhook",
  "parameters": {
    "path": "internal-trigger"
    // Your backend already validates
  }
}
```

**✅ Trusted Sources**
```javascript
// Webhook from Stripe (cryptographically signed)
{
  "type": "n8n-nodes-base.webhook",
  "parameters": {
    "path": "stripe-webhook",
    "authentication": "headerAuth"
    // Stripe signature validates authenticity
  }
}
```

#### When to Fix

**❌ Public Webhooks**
```javascript
// BAD: Public webhook without validation
{
  "type": "n8n-nodes-base.webhook",
  "parameters": {
    "path": "public-form-submit"
    // ❌ Anyone can send anything!
  }
}

// GOOD: Add validation
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook"
    },
    {
      "name": "Validate Input",
      "type": "n8n-nodes-base.if",
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{$json.body.email}}",
              "operation": "isNotEmpty"
            },
            {
              "value1": "={{$json.body.email}}",
              "operation": "regex",
              "value2": "^[^@]+@[^@]+\\.[^@]+$"
            }
          ]
        }
      }
    }
  ]
}
```

---

### 6. Hardcoded Credentials

**Warning**:
```json
{
  "type": "security",
  "message": "Credentials should not be hardcoded",
  "suggestion": "Use n8n credential system"
}
```

#### When Acceptable

**✅ Public APIs (No Auth)**
```javascript
// Truly public API with no secrets
{
  "url": "https://api.ipify.org"
  // No credentials needed
}
```

**✅ Demo/Example Workflows**
```javascript
// Example workflow in documentation
{
  "url": "https://example.com/api",
  "headers": {
    "Authorization": "Bearer DEMO_TOKEN"
  }
  // Clearly marked as example
}
```

#### When to Fix (Always!)

**❌ Real Credentials**
```javascript
// BAD: Real API key in workflow
{
  "headers": {
    "Authorization": "Bearer sk_live_abc123..."
  }
  // ❌ NEVER hardcode real credentials!
}

// GOOD: Use credentials system
{
  "authentication": "headerAuth",
  "credentials": {
    "headerAuth": {
      "id": "credential-id",
      "name": "My API Key"
    }
  }
}
```

---

## Validation Profile Strategies

### Strategy 1: Progressive Strictness

**Development**:
```javascript
validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "ai-friendly"  // Fewer warnings during development
})
```

**Pre-Production**:
```javascript
validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "runtime"  // Balanced validation
})
```

**Production Deployment**:
```javascript
validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "strict"  // All warnings, review each one
})
```

### Strategy 2: Profile by Workflow Type

**Quick Automations**:
- Profile: `ai-friendly`
- Accept: Most warnings
- Fix: Only errors + security warnings

**Business-Critical Workflows**:
- Profile: `strict`
- Accept: Very few warnings
- Fix: Everything possible

**Integration Testing**:
- Profile: `minimal`
- Accept: All warnings (just testing connections)
- Fix: Only errors that prevent execution

---

## Decision Framework

### Should I Fix This Warning?

```
┌─────────────────────────────────┐
│ Is it a SECURITY warning?       │
├─────────────────────────────────┤
│ YES → Always fix                │
│ NO  → Continue                  │
└─────────────────────────────────┘
         ↓
┌─────────────────────────────────┐
│ Is this a production workflow?  │
├─────────────────────────────────┤
│ YES → Continue                  │
│ NO  → Probably acceptable       │
└─────────────────────────────────┘
         ↓
┌─────────────────────────────────┐
│ Does it handle critical data?   │
├─────────────────────────────────┤
│ YES → Fix the warning           │
│ NO  → Continue                  │
└─────────────────────────────────┘
         ↓
┌─────────────────────────────────┐
│ Is there a known workaround?    │
├─────────────────────────────────┤
│ YES → Acceptable if documented  │
│ NO  → Fix the warning           │
└─────────────────────────────────┘
```

---

## Documentation Template

When accepting a warning, document why:

```javascript
// workflows/customer-notifications.json

{
  "nodes": [{
    "name": "Send Slack Notification",
    "type": "n8n-nodes-base.slack",
    "parameters": {
      "channel": "#notifications"
      // ACCEPTED WARNING: No error handling
      // Reason: Non-critical notification, failures are acceptable
      // Reviewed: 2025-10-20
      // Reviewer: Engineering Team
    }
  }]
}
```

---

## Known n8n Issues

### Issue #304: IF Node Metadata Warning

**Warning**:
```json
{
  "type": "metadata_incomplete",
  "message": "IF node missing conditions.options metadata",
  "node": "IF"
}
```

**Status**: False positive for IF v2.2+

**Why it occurs**: Auto-sanitization adds metadata, but validation runs before sanitization

**What to do**: Ignore - metadata is added on save

### Issue #306: Switch Branch Count

**Warning**:
```json
{
  "type": "configuration_mismatch",
  "message": "Switch has 3 rules but 4 output connections",
  "node": "Switch"
}
```

**Status**: False positive when using "fallback" mode

**Why it occurs**: Fallback creates extra output

**What to do**: Ignore if using fallback intentionally

### Issue #338: Credential Validation in Test Mode

**Warning**:
```json
{
  "type": "credentials_invalid",
  "message": "Cannot validate credentials without execution context"
}
```

**Status**: False positive during static validation

**Why it occurs**: Credentials validated at runtime, not build time

**What to do**: Ignore - credentials are validated when workflow runs

---

## Summary

### Always Fix
- ❌ Security warnings
- ❌ Hardcoded credentials
- ❌ SQL injection risks
- ❌ Production workflow errors

### Usually Fix
- ⚠️ Error handling (production)
- ⚠️ Retry logic (external APIs)
- ⚠️ Input validation (public webhooks)
- ⚠️ Rate limiting (high volume)

### Often Acceptable
- ✅ Error handling (dev/test)
- ✅ Retry logic (internal APIs)
- ✅ Rate limiting (low volume)
- ✅ Query limits (small datasets)

### Always Acceptable
- ✅ Known n8n issues (#304, #306, #338)
- ✅ Auto-sanitization warnings
- ✅ Metadata completeness (auto-fixed)

**Golden Rule**: If you accept a warning, document WHY.

**Related Files**:
- **[SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)** - Main validation guide
- **[ERROR_CATALOG.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_validation_expert/ERROR_CATALOG.md)** - Error types and fixes
```

## File: `skills/n8n-validation-expert/README.md`
```markdown
# n8n Validation Expert

Expert guidance for interpreting and fixing n8n validation errors.

## Overview

**Skill Name**: n8n Validation Expert
**Priority**: Medium
**Purpose**: Interpret validation errors and guide systematic fixing through the validation loop

## The Problem This Solves

Validation errors are common:

- Validation often requires iteration (79% lead to feedback loops)
- **7,841 validate → fix cycles** (avg 23s thinking + 58s fixing)
- **2-3 iterations** average to achieve valid configuration

**Key insight**: Validation is an iterative process, not a one-shot fix!

## What This Skill Teaches

### Core Concepts

1. **Error Severity Levels**
   - Errors (must fix) - Block execution
   - Warnings (should fix) - Don't block but indicate issues
   - Suggestions (optional) - Nice-to-have improvements

2. **The Validation Loop**
   - Configure → Validate → Read errors → Fix → Validate again
   - Average 2-3 iterations to success
   - 23 seconds thinking + 58 seconds fixing per cycle

3. **Validation Profiles**
   - `minimal` - Quick checks, most permissive
   - `runtime` - Recommended for most use cases
   - `ai-friendly` - Reduces false positives for AI workflows
   - `strict` - Maximum safety, many warnings

4. **Auto-Sanitization System**
   - Automatically fixes operator structure issues
   - Runs on every workflow save
   - Fixes binary/unary operator problems
   - Adds IF/Switch metadata

5. **False Positives**
   - Not all warnings need fixing
   - 40% of warnings are acceptable in context
   - Use `ai-friendly` profile to reduce by 60%
   - Document accepted warnings

## File Structure

```
n8n-validation-expert/
├── SKILL.md (690 lines)
│   Core validation concepts and workflow
│   - Validation philosophy
│   - Error severity levels
│   - The validation loop pattern
│   - Validation profiles
│   - Common error types
│   - Auto-sanitization system
│   - Workflow validation
│   - Recovery strategies
│   - Best practices
│
├── ERROR_CATALOG.md (865 lines)
│   Complete error reference with examples
│   - 9 error types with real examples
│   - missing_required (45% of errors)
│   - invalid_value (28%)
│   - type_mismatch (12%)
│   - invalid_expression (8%)
│   - invalid_reference (5%)
│   - operator_structure (2%, auto-fixed)
│   - Recovery patterns
│   - Summary with frequencies
│
├── FALSE_POSITIVES.md (669 lines)
│   When warnings are acceptable
│   - Philosophy of warning acceptance
│   - 6 common false positive types
│   - When acceptable vs when to fix
│   - Validation profile strategies
│   - Decision framework
│   - Documentation template
│   - Known n8n issues (#304, #306, #338)
│
└── README.md (this file)
    Skill metadata and statistics
```

**Total**: ~2,224 lines across 4 files

## Common Error Types

| Error Type | Priority | Auto-Fix | Severity |
|---|---|---|---|
| missing_required | Highest | ❌ | Error |
| invalid_value | High | ❌ | Error |
| type_mismatch | Medium | ❌ | Error |
| invalid_expression | Medium | ❌ | Error |
| invalid_reference | Low | ❌ | Error |
| operator_structure | Low | ✅ | Warning |

## Key Insights

### 1. Validation is Iterative
Don't expect to get it right on the first try. Multiple validation cycles (typically 2-3) are normal and expected!

### 2. False Positives Exist
Many validation warnings are acceptable in production workflows. This skill helps you recognize which ones to address vs. which to ignore.

### 3. Auto-Sanitization Works
Certain error types (like operator structure issues) are automatically fixed by n8n. Don't waste time manually fixing these!

### 4. Profile Matters
- `ai-friendly` reduces false positives by 60%
- `runtime` is the sweet spot for most use cases
- `strict` has value pre-production but is noisy

### 5. Error Messages Help
Validation errors include fix guidance - read them carefully!

## Usage Examples

### Example 1: Basic Validation Loop

```javascript
// Iteration 1
let config = {
  resource: "channel",
  operation: "create"
};

const result1 = validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "runtime"
});
// → Error: Missing "name"

// Iteration 2
config.name = "general";
const result2 = validate_node({...});
// → Valid! ✅
```

### Example 2: Handling False Positives

```javascript
// Run validation
const result = validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "runtime"
});

// Fix errors (must fix)
if (!result.valid) {
  result.errors.forEach(error => {
    console.log(`MUST FIX: ${error.message}`);
  });
}

// Review warnings (context-dependent)
result.warnings.forEach(warning => {
  if (warning.type === 'best_practice' && isDevWorkflow) {
    console.log(`ACCEPTABLE: ${warning.message}`);
  } else {
    console.log(`SHOULD FIX: ${warning.message}`);
  }
});
```

### Example 3: Using Auto-Fix

```javascript
// Check what can be auto-fixed
const preview = n8n_autofix_workflow({
  id: "workflow-id",
  applyFixes: false  // Preview mode
});

console.log(`Can auto-fix: ${preview.fixCount} issues`);

// Apply fixes
if (preview.fixCount > 0) {
  n8n_autofix_workflow({
    id: "workflow-id",
    applyFixes: true
  });
}
```

## When This Skill Activates

**Trigger phrases**:
- "validation error"
- "validation failing"
- "what does this error mean"
- "false positive"
- "validation loop"
- "operator structure"
- "validation profile"

**Common scenarios**:
- Encountering validation errors
- Stuck in validation feedback loops
- Wondering if warnings need fixing
- Choosing the right validation profile
- Understanding auto-sanitization

## Integration with Other Skills

### Works With:
- **n8n MCP Tools Expert** - How to use validation tools correctly
- **n8n Expression Syntax** - Fix invalid_expression errors
- **n8n Node Configuration** - Understand required fields
- **n8n Workflow Patterns** - Validate pattern implementations

### Complementary:
- Use MCP Tools Expert to call validation tools
- Use Expression Syntax to fix expression errors
- Use Node Configuration to understand dependencies
- Use Workflow Patterns to validate structure

## Testing

**Evaluations**: 4 test scenarios

1. **eval-001-missing-required-field.json**
   - Tests error interpretation
   - Guides to get_node
   - References ERROR_CATALOG.md

2. **eval-002-false-positive.json**
   - Tests warning vs error distinction
   - Explains false positives
   - References FALSE_POSITIVES.md
   - Suggests ai-friendly profile

3. **eval-003-auto-sanitization.json**
   - Tests auto-sanitization understanding
   - Explains operator structure fixes
   - Advises trusting auto-fix

4. **eval-004-validation-loop.json**
   - Tests iterative validation process
   - Explains 2-3 iteration pattern
   - Provides systematic approach

## Success Metrics

**Before this skill**:
- Users confused by validation errors
- Multiple failed attempts to fix
- Frustration with "validation loops"
- Fixing issues that auto-fix handles
- Fixing all warnings unnecessarily

**After this skill**:
- Systematic error resolution
- Understanding of iteration process
- Recognition of false positives
- Trust in auto-sanitization
- Context-aware warning handling
- 94% success within 3 iterations

## Related Documentation

- **n8n-mcp MCP Server**: Provides validation tools
- **n8n Validation API**: validate_node, validate_workflow, n8n_autofix_workflow
- **n8n Issues**: #304 (IF metadata), #306 (Switch branches), #338 (credentials)

## Version History

- **v1.0** (2025-10-20): Initial implementation
  - SKILL.md with core concepts
  - ERROR_CATALOG.md with 9 error types
  - FALSE_POSITIVES.md with 6 false positive patterns
  - 4 evaluation scenarios

## Author

Conceived by Romuald Członkowski - [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)

Part of the n8n-skills meta-skill collection.
```

## File: `skills/n8n-validation-expert/SKILL.md`
```markdown
---
name: n8n-validation-expert
description: Interpret validation errors and guide fixing them. Use when encountering validation errors, validation warnings, false positives, operator structure issues, or need help understanding validation results. Also use when asking about validation profiles, error types, or the validation loop process.
---

# n8n Validation Expert

Expert guide for interpreting and fixing n8n validation errors.

---

## Validation Philosophy

**Validate early, validate often**

Validation is typically iterative:
- Expect validation feedback loops
- Usually 2-3 validate → fix cycles
- Average: 23s thinking about errors, 58s fixing them

**Key insight**: Validation is an iterative process, not one-shot!

---

## Error Severity Levels

### 1. Errors (Must Fix)
**Blocks workflow execution** - Must be resolved before activation

**Types**:
- `missing_required` - Required field not provided
- `invalid_value` - Value doesn't match allowed options
- `type_mismatch` - Wrong data type (string instead of number)
- `invalid_reference` - Referenced node doesn't exist
- `invalid_expression` - Expression syntax error

**Example**:
```json
{
  "type": "missing_required",
  "property": "channel",
  "message": "Channel name is required",
  "fix": "Provide a channel name (lowercase, no spaces, 1-80 characters)"
}
```

### 2. Warnings (Should Fix)
**Doesn't block execution** - Workflow can be activated but may have issues

**Types**:
- `best_practice` - Recommended but not required
- `deprecated` - Using old API/feature
- `performance` - Potential performance issue

**Example**:
```json
{
  "type": "best_practice",
  "property": "errorHandling",
  "message": "Slack API can have rate limits",
  "suggestion": "Add onError: 'continueRegularOutput' with retryOnFail"
}
```

### 3. Suggestions (Optional)
**Nice to have** - Improvements that could enhance workflow

**Types**:
- `optimization` - Could be more efficient
- `alternative` - Better way to achieve same result

---

## The Validation Loop

### Pattern from Telemetry
**7,841 occurrences** of this pattern:

```
1. Configure node
   ↓
2. validate_node (23 seconds thinking about errors)
   ↓
3. Read error messages carefully
   ↓
4. Fix errors
   ↓
5. validate_node again (58 seconds fixing)
   ↓
6. Repeat until valid (usually 2-3 iterations)
```

### Example
```javascript
// Iteration 1
let config = {
  resource: "channel",
  operation: "create"
};

const result1 = validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "runtime"
});
// → Error: Missing "name"

// ⏱️  23 seconds thinking...

// Iteration 2
config.name = "general";

const result2 = validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "runtime"
});
// → Error: Missing "text"

// ⏱️  58 seconds fixing...

// Iteration 3
config.text = "Hello!";

const result3 = validate_node({
  nodeType: "nodes-base.slack",
  config,
  profile: "runtime"
});
// → Valid! ✅
```

**This is normal!** Don't be discouraged by multiple iterations.

---

## Validation Profiles

Choose the right profile for your stage:

### minimal
**Use when**: Quick checks during editing

**Validates**:
- Only required fields
- Basic structure

**Pros**: Fastest, most permissive
**Cons**: May miss issues

### runtime (RECOMMENDED)
**Use when**: Pre-deployment validation

**Validates**:
- Required fields
- Value types
- Allowed values
- Basic dependencies

**Pros**: Balanced, catches real errors
**Cons**: Some edge cases missed

**This is the recommended profile for most use cases**

### ai-friendly
**Use when**: AI-generated configurations

**Validates**:
- Same as runtime
- Reduces false positives
- More tolerant of minor issues

**Pros**: Less noisy for AI workflows
**Cons**: May allow some questionable configs

### strict
**Use when**: Production deployment, critical workflows

**Validates**:
- Everything
- Best practices
- Performance concerns
- Security issues

**Pros**: Maximum safety
**Cons**: Many warnings, some false positives

---

## Common Error Types

### 1. missing_required
**What it means**: A required field is not provided

**How to fix**:
1. Use `get_node` to see required fields
2. Add the missing field to your configuration
3. Provide an appropriate value

**Example**:
```javascript
// Error
{
  "type": "missing_required",
  "property": "channel",
  "message": "Channel name is required"
}

// Fix
config.channel = "#general";
```

### 2. invalid_value
**What it means**: Value doesn't match allowed options

**How to fix**:
1. Check error message for allowed values
2. Use `get_node` to see options
3. Update to a valid value

**Example**:
```javascript
// Error
{
  "type": "invalid_value",
  "property": "operation",
  "message": "Operation must be one of: post, update, delete",
  "current": "send"
}

// Fix
config.operation = "post";  // Use valid operation
```

### 3. type_mismatch
**What it means**: Wrong data type for field

**How to fix**:
1. Check expected type in error message
2. Convert value to correct type

**Example**:
```javascript
// Error
{
  "type": "type_mismatch",
  "property": "limit",
  "message": "Expected number, got string",
  "current": "100"
}

// Fix
config.limit = 100;  // Number, not string
```

### 4. invalid_expression
**What it means**: Expression syntax error

**How to fix**:
1. Use n8n Expression Syntax skill
2. Check for missing `{{}}` or typos
3. Verify node/field references

**Example**:
```javascript
// Error
{
  "type": "invalid_expression",
  "property": "text",
  "message": "Invalid expression: $json.name",
  "current": "$json.name"
}

// Fix
config.text = "={{$json.name}}";  // Add {{}}
```

### 5. invalid_reference
**What it means**: Referenced node doesn't exist

**How to fix**:
1. Check node name spelling
2. Verify node exists in workflow
3. Update reference to correct name

**Example**:
```javascript
// Error
{
  "type": "invalid_reference",
  "property": "expression",
  "message": "Node 'HTTP Requets' does not exist",
  "current": "={{$node['HTTP Requets'].json.data}}"
}

// Fix - correct typo
config.expression = "={{$node['HTTP Request'].json.data}}";
```

---

## Auto-Sanitization System

### What It Does
**Automatically fixes common operator structure issues** on ANY workflow update

**Runs when**:
- `n8n_create_workflow`
- `n8n_update_partial_workflow`
- Any workflow save operation

### What It Fixes

#### 1. Binary Operators (Two Values)
**Operators**: equals, notEquals, contains, notContains, greaterThan, lessThan, startsWith, endsWith

**Fix**: Removes `singleValue` property (binary operators compare two values)

**Before**:
```javascript
{
  "type": "boolean",
  "operation": "equals",
  "singleValue": true  // ❌ Wrong!
}
```

**After** (automatic):
```javascript
{
  "type": "boolean",
  "operation": "equals"
  // singleValue removed ✅
}
```

#### 2. Unary Operators (One Value)
**Operators**: isEmpty, isNotEmpty, true, false

**Fix**: Adds `singleValue: true` (unary operators check single value)

**Before**:
```javascript
{
  "type": "boolean",
  "operation": "isEmpty"
  // Missing singleValue ❌
}
```

**After** (automatic):
```javascript
{
  "type": "boolean",
  "operation": "isEmpty",
  "singleValue": true  // ✅ Added
}
```

#### 3. IF/Switch Metadata
**Fix**: Adds complete `conditions.options` metadata for IF v2.2+ and Switch v3.2+

### What It CANNOT Fix

#### 1. Broken Connections
References to non-existent nodes

**Solution**: Use `cleanStaleConnections` operation in `n8n_update_partial_workflow`

#### 2. Branch Count Mismatches
3 Switch rules but only 2 output connections

**Solution**: Add missing connections or remove extra rules

#### 3. Paradoxical Corrupt States
API returns corrupt data but rejects updates

**Solution**: May require manual database intervention

---

## False Positives

### What Are They?
Validation warnings that are technically "wrong" but acceptable in your use case

### Common False Positives

#### 1. "Missing error handling"
**Warning**: No error handling configured

**When acceptable**:
- Simple workflows where failures are obvious
- Testing/development workflows
- Non-critical notifications

**When to fix**: Production workflows handling important data

#### 2. "No retry logic"
**Warning**: Node doesn't retry on failure

**When acceptable**:
- APIs with their own retry logic
- Idempotent operations
- Manual trigger workflows

**When to fix**: Flaky external services, production automation

#### 3. "Missing rate limiting"
**Warning**: No rate limiting for API calls

**When acceptable**:
- Internal APIs with no limits
- Low-volume workflows
- APIs with server-side rate limiting

**When to fix**: Public APIs, high-volume workflows

#### 4. "Unbounded query"
**Warning**: SELECT without LIMIT

**When acceptable**:
- Small known datasets
- Aggregation queries
- Development/testing

**When to fix**: Production queries on large tables

### Reducing False Positives

**Use `ai-friendly` profile**:
```javascript
validate_node({
  nodeType: "nodes-base.slack",
  config: {...},
  profile: "ai-friendly"  // Fewer false positives
})
```

---

## Validation Result Structure

### Complete Response
```javascript
{
  "valid": false,
  "errors": [
    {
      "type": "missing_required",
      "property": "channel",
      "message": "Channel name is required",
      "fix": "Provide a channel name (lowercase, no spaces)"
    }
  ],
  "warnings": [
    {
      "type": "best_practice",
      "property": "errorHandling",
      "message": "Slack API can have rate limits",
      "suggestion": "Add onError: 'continueRegularOutput'"
    }
  ],
  "suggestions": [
    {
      "type": "optimization",
      "message": "Consider using batch operations for multiple messages"
    }
  ],
  "summary": {
    "hasErrors": true,
    "errorCount": 1,
    "warningCount": 1,
    "suggestionCount": 1
  }
}
```

### How to Read It

#### 1. Check `valid` field
```javascript
if (result.valid) {
  // ✅ Configuration is valid
} else {
  // ❌ Has errors - must fix before deployment
}
```

#### 2. Fix errors first
```javascript
result.errors.forEach(error => {
  console.log(`Error in ${error.property}: ${error.message}`);
  console.log(`Fix: ${error.fix}`);
});
```

#### 3. Review warnings
```javascript
result.warnings.forEach(warning => {
  console.log(`Warning: ${warning.message}`);
  console.log(`Suggestion: ${warning.suggestion}`);
  // Decide if you need to address this
});
```

#### 4. Consider suggestions
```javascript
// Optional improvements
// Not required but may enhance workflow
```

---

## Workflow Validation

### validate_workflow (Structure)
**Validates entire workflow**, not just individual nodes

**Checks**:
1. **Node configurations** - Each node valid
2. **Connections** - No broken references
3. **Expressions** - Syntax and references valid
4. **Flow** - Logical workflow structure

**Example**:
```javascript
validate_workflow({
  workflow: {
    nodes: [...],
    connections: {...}
  },
  options: {
    validateNodes: true,
    validateConnections: true,
    validateExpressions: true,
    profile: "runtime"
  }
})
```

### Common Workflow Errors

#### 1. Broken Connections
```json
{
  "error": "Connection from 'Transform' to 'NonExistent' - target node not found"
}
```

**Fix**: Remove stale connection or create missing node

#### 2. Circular Dependencies
```json
{
  "error": "Circular dependency detected: Node A → Node B → Node A"
}
```

**Fix**: Restructure workflow to remove loop

#### 3. Multiple Start Nodes
```json
{
  "warning": "Multiple trigger nodes found - only one will execute"
}
```

**Fix**: Remove extra triggers or split into separate workflows

#### 4. Disconnected Nodes
```json
{
  "warning": "Node 'Transform' is not connected to workflow flow"
}
```

**Fix**: Connect node or remove if unused

---

## Recovery Strategies

### Strategy 1: Start Fresh
**When**: Configuration is severely broken

**Steps**:
1. Note required fields from `get_node`
2. Create minimal valid configuration
3. Add features incrementally
4. Validate after each addition

### Strategy 2: Binary Search
**When**: Workflow validates but executes incorrectly

**Steps**:
1. Remove half the nodes
2. Validate and test
3. If works: problem is in removed nodes
4. If fails: problem is in remaining nodes
5. Repeat until problem isolated

### Strategy 3: Clean Stale Connections
**When**: "Node not found" errors

**Steps**:
```javascript
n8n_update_partial_workflow({
  id: "workflow-id",
  operations: [{
    type: "cleanStaleConnections"
  }]
})
```

### Strategy 4: Use Auto-fix
**When**: Validation errors that can be automatically resolved

**Steps**:
```javascript
// Preview fixes (default - doesn't apply)
n8n_autofix_workflow({
  id: "workflow-id",
  applyFixes: false,
  confidenceThreshold: "medium"  // high, medium, low
})

// Review fixes, then apply
n8n_autofix_workflow({
  id: "workflow-id",
  applyFixes: true
})
```

---

## Auto-Fix Capabilities

The `n8n_autofix_workflow` tool can fix these issue types:

1. **expression-format** - Missing `=` prefix in expressions (e.g., `{{ $json.field }}` → `={{ $json.field }}`)
2. **typeversion-correction** - Downgrades nodes with unsupported typeVersions
3. **error-output-config** - Removes conflicting onError settings
4. **node-type-correction** - Fixes unknown node types using similarity matching (90%+ confidence)
5. **webhook-missing-path** - Generates UUIDs for webhook nodes missing path configuration
6. **typeversion-upgrade** - Smart upgrades to latest node versions with auto-migration
7. **version-migration** - Guidance for complex breaking changes requiring manual steps

**Confidence levels**: `high` (90%+, safe to auto-apply), `medium` (70-89%, review recommended), `low` (<70%, manual review required)

```javascript
// Preview all fixes
n8n_autofix_workflow({id: "workflow-id"})

// Only apply high-confidence fixes
n8n_autofix_workflow({
  id: "workflow-id",
  applyFixes: true,
  confidenceThreshold: "high"
})

// Target specific fix types
n8n_autofix_workflow({
  id: "workflow-id",
  fixTypes: ["expression-format", "typeversion-upgrade"],
  applyFixes: true
})
```

**Post-update guidance**: For version upgrades, check the `postUpdateGuidance` field in the response for step-by-step migration instructions.

---

## Best Practices

### ✅ Do

- Validate after every significant change
- Read error messages completely
- Fix errors iteratively (one at a time)
- Use `runtime` profile for pre-deployment
- Check `valid` field before assuming success
- Trust auto-sanitization for operator issues
- Use `get_node` when unclear about requirements
- Document false positives you accept

### ❌ Don't

- Skip validation before activation
- Try to fix all errors at once
- Ignore error messages
- Use `strict` profile during development (too noisy)
- Assume validation passed (always check result)
- Manually fix auto-sanitization issues
- Deploy with unresolved errors
- Ignore all warnings (some are important!)

---

## Detailed Guides

For comprehensive error catalogs and false positive examples:

- **[ERROR_CATALOG.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_validation_expert/ERROR_CATALOG.md)** - Complete list of error types with examples
- **[FALSE_POSITIVES.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_validation_expert/FALSE_POSITIVES.md)** - When warnings are acceptable

---

## Summary

**Key Points**:
1. **Validation is iterative** (avg 2-3 cycles, 23s + 58s)
2. **Errors must be fixed**, warnings are optional
3. **Auto-sanitization** fixes operator structures automatically
4. **Use runtime profile** for balanced validation
5. **False positives exist** - learn to recognize them
6. **Read error messages** - they contain fix guidance

**Validation Process**:
1. Validate → Read errors → Fix → Validate again
2. Repeat until valid (usually 2-3 iterations)
3. Review warnings and decide if acceptable
4. Deploy with confidence

**Related Skills**:
- n8n MCP Tools Expert - Use validation tools correctly
- n8n Expression Syntax - Fix expression errors
- n8n Node Configuration - Understand required fields
```

## File: `skills/n8n-workflow-patterns/README.md`
```markdown
# n8n Workflow Patterns

Proven architectural patterns for building n8n workflows.

---

## Purpose

Teaches architectural patterns for building n8n workflows. Provides structure, best practices, and proven approaches for common use cases.

## Activates On

- build workflow
- workflow pattern
- workflow architecture
- workflow structure
- webhook processing
- http api
- api integration
- database sync
- ai agent
- chatbot
- scheduled task
- automation pattern

## File Count

7 files, ~3,700 lines total

## Priority

**HIGH** - Addresses 813 webhook searches (most common use case)

## Dependencies

**n8n-mcp tools**:
- search_nodes (find nodes for patterns)
- get_node (understand node operations)
- search_templates (find example workflows)
- ai_agents_guide (AI pattern guidance)

**Related skills**:
- n8n MCP Tools Expert (find and configure nodes)
- n8n Expression Syntax (write expressions in patterns)
- n8n Node Configuration (configure pattern nodes)
- n8n Validation Expert (validate pattern implementations)

## Coverage

### The 5 Core Patterns

1. **Webhook Processing** (Most Common - 813 searches)
   - Receive HTTP requests → Process → Respond
   - Critical gotcha: Data under $json.body
   - Authentication, validation, error handling

2. **HTTP API Integration** (892 templates)
   - Fetch from REST APIs → Transform → Store/Use
   - Authentication methods, pagination, rate limiting
   - Error handling and retries

3. **Database Operations** (456 templates)
   - Read/Write/Sync database data
   - Batch processing, transactions, performance
   - Security: parameterized queries, read-only access

4. **AI Agent Workflow** (234 templates, 270 AI nodes)
   - AI agents with tool access and memory
   - 8 AI connection types
   - ANY node can be an AI tool

5. **Scheduled Tasks** (28% of all workflows)
   - Recurring automation workflows
   - Cron schedules, timezone handling
   - Monitoring and error handling

### Cross-Cutting Concerns

- Data flow patterns (linear, branching, parallel, loops)
- Error handling strategies
- Performance optimization
- Security best practices
- Testing approaches
- Monitoring and logging

## Evaluations

5 scenarios (100% coverage expected):
1. **eval-001**: Webhook workflow structure
2. **eval-002**: HTTP API integration pattern
3. **eval-003**: Database sync pattern
4. **eval-004**: AI agent workflow with tools
5. **eval-005**: Scheduled report generation

## Key Features

✅ **5 Proven Patterns**: Webhook, HTTP API, Database, AI Agent, Scheduled tasks
✅ **Complete Examples**: Working workflow configurations for each pattern
✅ **Best Practices**: Proven approaches from real-world n8n usage
✅ **Common Gotchas**: Documented mistakes and their fixes
✅ **Integration Guide**: How patterns work with other skills
✅ **Template Examples**: Real examples from 2,653+ n8n templates

## Files

- **SKILL.md** (486 lines) - Pattern overview, selection guide, checklist
- **webhook_processing.md** (554 lines) - Webhook patterns, data structure, auth
- **http_api_integration.md** (763 lines) - REST APIs, pagination, rate limiting
- **database_operations.md** (854 lines) - DB operations, batch processing, security
- **ai_agent_workflow.md** (918 lines) - AI agents, tools, memory, 8 connection types
- **scheduled_tasks.md** (845 lines) - Cron schedules, timezone, monitoring
- **README.md** (this file) - Skill metadata

## Success Metrics

**Expected outcomes**:
- Users select appropriate pattern for their use case
- Workflows follow proven structural patterns
- Common gotchas avoided (webhook $json.body, SQL injection, etc.)
- Proper error handling implemented
- Security best practices followed

## Pattern Selection Stats

Common workflow composition:

**Trigger Distribution**:
- Webhook: 35% (most common)
- Schedule: 28%
- Manual: 22%
- Service triggers: 15%

**Transformation Nodes**:
- Set: 68%
- Code: 42%
- IF: 38%
- Switch: 18%

**Output Channels**:
- HTTP Request: 45%
- Slack: 32%
- Database: 28%
- Email: 24%

**Complexity**:
- Simple (3-5 nodes): 42%
- Medium (6-10 nodes): 38%
- Complex (11+ nodes): 20%

## Critical Insights

**Webhook Processing**:
- 813 searches (most common use case!)
- #1 gotcha: Data under $json.body (not $json directly)
- Must choose response mode: onReceived vs lastNode

**API Integration**:
- Authentication via credentials (never hardcode!)
- Pagination essential for large datasets
- Rate limiting prevents API bans
- continueOnFail: true for error handling

**Database Operations**:
- Always use parameterized queries (SQL injection prevention)
- Batch processing for large datasets
- Read-only access for AI tools
- Transaction handling for multi-step operations

**AI Agents**:
- 8 AI connection types (ai_languageModel, ai_tool, ai_memory, etc.)
- ANY node can be an AI tool (connect to ai_tool port)
- Memory essential for conversations (Window Buffer recommended)
- Tool descriptions critical (AI uses them to decide when to call)

**Scheduled Tasks**:
- Set workflow timezone explicitly (DST handling)
- Prevent overlapping executions (use locks)
- Error Trigger workflow for alerts
- Batch processing for large data

## Workflow Creation Checklist

Every pattern follows this checklist:

### Planning Phase
- [ ] Identify the pattern (webhook, API, database, AI, scheduled)
- [ ] List required nodes (use search_nodes)
- [ ] Understand data flow (input → transform → output)
- [ ] Plan error handling strategy

### Implementation Phase
- [ ] Create workflow with appropriate trigger
- [ ] Add data source nodes
- [ ] Configure authentication/credentials
- [ ] Add transformation nodes (Set, Code, IF)
- [ ] Add output/action nodes
- [ ] Configure error handling

### Validation Phase
- [ ] Validate each node configuration
- [ ] Validate complete workflow
- [ ] Test with sample data
- [ ] Handle edge cases

### Deployment Phase
- [ ] Review workflow settings
- [ ] Activate workflow
- [ ] Monitor first executions
- [ ] Document workflow

## Real Template Examples

**Weather to Slack** (Template #2947):
```
Schedule (daily 8 AM) → HTTP Request (weather) → Set → Slack
```

**Webhook Processing**: 1,085 templates
**HTTP API Integration**: 892 templates
**Database Operations**: 456 templates
**AI Workflows**: 234 templates

Use `search_templates` to find examples for your use case!

## Integration with Other Skills

**Pattern Selection** (this skill):
1. Identify use case
2. Select appropriate pattern
3. Follow pattern structure

**Node Discovery** (n8n MCP Tools Expert):
4. Find nodes for pattern (search_nodes)
5. Understand node operations (get_node)

**Implementation** (n8n Expression Syntax + Node Configuration):
6. Write expressions ({{$json.body.field}})
7. Configure nodes properly

**Validation** (n8n Validation Expert):
8. Validate workflow structure
9. Fix validation errors

## Last Updated

2025-10-20

---

**Part of**: n8n-skills repository
**Conceived by**: Romuald Członkowski - [www.aiadvisors.pl/en](https://www.aiadvisors.pl/en)
```

## File: `skills/n8n-workflow-patterns/SKILL.md`
```markdown
---
name: n8n-workflow-patterns
description: Proven workflow architectural patterns from real n8n workflows. Use when building new workflows, designing workflow structure, choosing workflow patterns, planning workflow architecture, or asking about webhook processing, HTTP API integration, database operations, AI agent workflows, or scheduled tasks.
---

# n8n Workflow Patterns

Proven architectural patterns for building n8n workflows.

---

## The 5 Core Patterns

Based on analysis of real workflow usage:

1. **[Webhook Processing](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/webhook_processing.md)** (Most Common)
   - Receive HTTP requests → Process → Output
   - Pattern: Webhook → Validate → Transform → Respond/Notify

2. **[HTTP API Integration](http_api_integration.md)**
   - Fetch from REST APIs → Transform → Store/Use
   - Pattern: Trigger → HTTP Request → Transform → Action → Error Handler

3. **[Database Operations](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/database_operations.md)**
   - Read/Write/Sync database data
   - Pattern: Schedule → Query → Transform → Write → Verify

4. **[AI Agent Workflow](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/ai_agent_workflow.md)**
   - AI agents with tools and memory
   - Pattern: Trigger → AI Agent (Model + Tools + Memory) → Output

5. **[Scheduled Tasks](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/scheduled_tasks.md)**
   - Recurring automation workflows
   - Pattern: Schedule → Fetch → Process → Deliver → Log

---

## Pattern Selection Guide

### When to use each pattern:

**Webhook Processing** - Use when:
- Receiving data from external systems
- Building integrations (Slack commands, form submissions, GitHub webhooks)
- Need instant response to events
- Example: "Receive Stripe payment webhook → Update database → Send confirmation"

**HTTP API Integration** - Use when:
- Fetching data from external APIs
- Synchronizing with third-party services
- Building data pipelines
- Example: "Fetch GitHub issues → Transform → Create Jira tickets"

**Database Operations** - Use when:
- Syncing between databases
- Running database queries on schedule
- ETL workflows
- Example: "Read Postgres records → Transform → Write to MySQL"

**AI Agent Workflow** - Use when:
- Building conversational AI
- Need AI with tool access
- Multi-step reasoning tasks
- Example: "Chat with AI that can search docs, query database, send emails"

**Scheduled Tasks** - Use when:
- Recurring reports or summaries
- Periodic data fetching
- Maintenance tasks
- Example: "Daily: Fetch analytics → Generate report → Email team"

---

## Common Workflow Components

All patterns share these building blocks:

### 1. Triggers
- **Webhook** - HTTP endpoint (instant)
- **Schedule** - Cron-based timing (periodic)
- **Manual** - Click to execute (testing)
- **Polling** - Check for changes (intervals)

### 2. Data Sources
- **HTTP Request** - REST APIs
- **Database nodes** - Postgres, MySQL, MongoDB
- **Service nodes** - Slack, Google Sheets, etc.
- **Code** - Custom JavaScript/Python

### 3. Transformation
- **Set** - Map/transform fields
- **Code** - Complex logic
- **IF/Switch** - Conditional routing
- **Merge** - Combine data streams

### 4. Outputs
- **HTTP Request** - Call APIs
- **Database** - Write data
- **Communication** - Email, Slack, Discord
- **Storage** - Files, cloud storage

### 5. Error Handling
- **Error Trigger** - Catch workflow errors
- **IF** - Check for error conditions
- **Stop and Error** - Explicit failure
- **Continue On Fail** - Per-node setting

---

## Workflow Creation Checklist

When building ANY workflow, follow this checklist:

### Planning Phase
- [ ] Identify the pattern (webhook, API, database, AI, scheduled)
- [ ] List required nodes (use search_nodes)
- [ ] Understand data flow (input → transform → output)
- [ ] Plan error handling strategy

### Implementation Phase
- [ ] Create workflow with appropriate trigger
- [ ] Add data source nodes
- [ ] Configure authentication/credentials
- [ ] Add transformation nodes (Set, Code, IF)
- [ ] Add output/action nodes
- [ ] Configure error handling

### Validation Phase
- [ ] Validate each node configuration (validate_node)
- [ ] Validate complete workflow (validate_workflow)
- [ ] Test with sample data
- [ ] Handle edge cases (empty data, errors)

### Deployment Phase
- [ ] Review workflow settings (execution order, timeout, error handling)
- [ ] Activate workflow using `activateWorkflow` operation
- [ ] Monitor first executions
- [ ] Document workflow purpose and data flow

---

## Data Flow Patterns

### Linear Flow
```
Trigger → Transform → Action → End
```
**Use when**: Simple workflows with single path

### Branching Flow
```
Trigger → IF → [True Path]
             └→ [False Path]
```
**Use when**: Different actions based on conditions

### Parallel Processing
```
Trigger → [Branch 1] → Merge
       └→ [Branch 2] ↗
```
**Use when**: Independent operations that can run simultaneously

### Loop Pattern
```
Trigger → Split in Batches → Process → Loop (until done)
```
**Use when**: Processing large datasets in chunks

### Error Handler Pattern
```
Main Flow → [Success Path]
         └→ [Error Trigger → Error Handler]
```
**Use when**: Need separate error handling workflow

---

## Common Gotchas

### 1. Webhook Data Structure
**Problem**: Can't access webhook payload data

**Solution**: Data is nested under `$json.body`
```javascript
❌ {{$json.email}}
✅ {{$json.body.email}}
```
See: n8n Expression Syntax skill

### 2. Multiple Input Items
**Problem**: Node processes all input items, but I only want one

**Solution**: Use "Execute Once" mode or process first item only
```javascript
{{$json[0].field}}  // First item only
```

### 3. Authentication Issues
**Problem**: API calls failing with 401/403

**Solution**:
- Configure credentials properly
- Use the "Credentials" section, not parameters
- Test credentials before workflow activation

### 4. Node Execution Order
**Problem**: Nodes executing in unexpected order

**Solution**: Check workflow settings → Execution Order
- v0: Top-to-bottom (legacy)
- v1: Connection-based (recommended)

### 5. Expression Errors
**Problem**: Expressions showing as literal text

**Solution**: Use {{}} around expressions
- See n8n Expression Syntax skill for details

---

## Integration with Other Skills

These skills work together with Workflow Patterns:

**n8n MCP Tools Expert** - Use to:
- Find nodes for your pattern (search_nodes)
- Understand node operations (get_node)
- Create workflows (n8n_create_workflow)
- Deploy templates (n8n_deploy_template)
- Use `ai_agents_guide()` for AI pattern guidance
- Manage data tables with `n8n_manage_datatable`

**n8n Expression Syntax** - Use to:
- Write expressions in transformation nodes
- Access webhook data correctly ({{$json.body.field}})
- Reference previous nodes ({{$node["Node Name"].json.field}})

**n8n Node Configuration** - Use to:
- Configure specific operations for pattern nodes
- Understand node-specific requirements

**n8n Validation Expert** - Use to:
- Validate workflow structure
- Fix validation errors
- Ensure workflow correctness before deployment

---

## Pattern Statistics

Common workflow patterns:

**Most Common Triggers**:
1. Webhook - 35%
2. Schedule (periodic tasks) - 28%
3. Manual (testing/admin) - 22%
4. Service triggers (Slack, email, etc.) - 15%

**Most Common Transformations**:
1. Set (field mapping) - 68%
2. Code (custom logic) - 42%
3. IF (conditional routing) - 38%
4. Switch (multi-condition) - 18%

**Most Common Outputs**:
1. HTTP Request (APIs) - 45%
2. Slack - 32%
3. Database writes - 28%
4. Email - 24%

**Average Workflow Complexity**:
- Simple (3-5 nodes): 42%
- Medium (6-10 nodes): 38%
- Complex (11+ nodes): 20%

---

## Quick Start Examples

### Example 1: Simple Webhook → Slack
```
1. Webhook (path: "form-submit", POST)
2. Set (map form fields)
3. Slack (post message to #notifications)
```

### Example 2: Scheduled Report
```
1. Schedule (daily at 9 AM)
2. HTTP Request (fetch analytics)
3. Code (aggregate data)
4. Email (send formatted report)
5. Error Trigger → Slack (notify on failure)
```

### Example 3: Database Sync
```
1. Schedule (every 15 minutes)
2. Postgres (query new records)
3. IF (check if records exist)
4. MySQL (insert records)
5. Postgres (update sync timestamp)
```

### Example 4: AI Assistant
```
1. Webhook (receive chat message)
2. AI Agent
   ├─ OpenAI Chat Model (ai_languageModel)
   ├─ HTTP Request Tool (ai_tool)
   ├─ Database Tool (ai_tool)
   └─ Window Buffer Memory (ai_memory)
3. Webhook Response (send AI reply)
```

### Example 5: API Integration
```
1. Manual Trigger (for testing)
2. HTTP Request (GET /api/users)
3. Split In Batches (process 100 at a time)
4. Set (transform user data)
5. Postgres (upsert users)
6. Loop (back to step 3 until done)
```

---

## Detailed Pattern Files

For comprehensive guidance on each pattern:

- **[webhook_processing.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/webhook_processing.md)** - Webhook patterns, data structure, response handling
- **[http_api_integration.md](http_api_integration.md)** - REST APIs, authentication, pagination, retries
- **[database_operations.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/database_operations.md)** - Queries, sync, transactions, batch processing
- **[ai_agent_workflow.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/ai_agent_workflow.md)** - AI agents, tools, memory, langchain nodes
- **[scheduled_tasks.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/scheduled_tasks.md)** - Cron schedules, reports, maintenance tasks

---

## Real Template Examples

From n8n template library:

**Template #2947**: Weather to Slack
- Pattern: Scheduled Task
- Nodes: Schedule → HTTP Request (weather API) → Set → Slack
- Complexity: Simple (4 nodes)

**Webhook Processing**: Most common pattern
- Most common: Form submissions, payment webhooks, chat integrations

**HTTP API**: Common pattern
- Most common: Data fetching, third-party integrations

**Database Operations**: Common pattern
- Most common: ETL, data sync, backup workflows

**AI Agents**: Growing in usage
- Most common: Chatbots, content generation, data analysis

Use `search_templates` and `get_template` from n8n-mcp tools to find examples!

---

## Best Practices

### ✅ Do

- Start with the simplest pattern that solves your problem
- Plan your workflow structure before building
- Use error handling on all workflows
- Test with sample data before activation
- Follow the workflow creation checklist
- Use descriptive node names
- Document complex workflows (notes field)
- Monitor workflow executions after deployment

### ❌ Don't

- Build workflows in one shot (iterate! avg 56s between edits)
- Skip validation before activation
- Ignore error scenarios
- Use complex patterns when simple ones suffice
- Hardcode credentials in parameters
- Forget to handle empty data cases
- Mix multiple patterns without clear boundaries
- Deploy without testing

---

## Summary

**Key Points**:
1. **5 core patterns** cover 90%+ of workflow use cases
2. **Webhook processing** is the most common pattern
3. Use the **workflow creation checklist** for every workflow
4. **Plan pattern** → **Select nodes** → **Build** → **Validate** → **Deploy**
5. Integrate with other skills for complete workflow development

**Next Steps**:
1. Identify your use case pattern
2. Read the detailed pattern file
3. Use n8n MCP Tools Expert to find nodes
4. Follow the workflow creation checklist
5. Use n8n Validation Expert to validate

**Related Skills**:
- n8n MCP Tools Expert - Find and configure nodes
- n8n Expression Syntax - Write expressions correctly
- n8n Validation Expert - Validate and fix errors
- n8n Node Configuration - Configure specific operations
```

## File: `skills/n8n-workflow-patterns/ai_agent_workflow.md`
```markdown
# AI Agent Workflow Pattern

**Use Case**: Build AI agents with tool access, memory, and reasoning capabilities.

---

## Pattern Structure

```
Trigger → AI Agent (Model + Tools + Memory) → [Process Response] → Output
```

**Key Characteristic**: AI-powered decision making with tool use

---

## Core AI Connection Types

n8n supports **8 AI connection types** for building agent workflows:

1. **ai_languageModel** - The LLM (OpenAI, Anthropic, etc.)
2. **ai_tool** - Functions the agent can call
3. **ai_memory** - Conversation context
4. **ai_outputParser** - Parse structured outputs
5. **ai_embedding** - Vector embeddings
6. **ai_vectorStore** - Vector database
7. **ai_document** - Document loaders
8. **ai_textSplitter** - Text chunking

---

## Core Components

### 1. Trigger
**Options**:
- **Webhook** - Chat interfaces, API calls (most common)
- **Manual** - Testing and development
- **Schedule** - Periodic AI tasks

### 2. AI Agent Node
**Purpose**: Orchestrate LLM with tools and memory

**Configuration**:
```javascript
{
  agent: "conversationalAgent",  // or "openAIFunctionsAgent"
  promptType: "define",
  text: "You are a helpful assistant that can search docs, query databases, and send emails."
}
```

**Connections**:
- **ai_languageModel input** - Connected to LLM node
- **ai_tool inputs** - Connected to tool nodes
- **ai_memory input** - Connected to memory node (optional)

### 3. Language Model
**Available providers**:
- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude)
- Google (Gemini)
- Local models (Ollama, LM Studio)

**Example** (OpenAI Chat Model):
```javascript
{
  model: "gpt-4",
  temperature: 0.7,
  maxTokens: 1000
}
```

### 4. Tools (ANY Node Can Be a Tool!)
**Critical insight**: Connect ANY n8n node to agent via `ai_tool` port

**Common tool types**:
- HTTP Request - Call APIs
- Database nodes - Query data
- Code - Custom functions
- Search nodes - Web/document search
- Pre-built tool nodes (Calculator, Wikipedia, etc.)

### 5. Memory (Optional but Recommended)
**Purpose**: Maintain conversation context

**Types**:
- **Buffer Memory** - Store recent messages
- **Window Buffer Memory** - Store last N messages
- **Summary Memory** - Summarize conversation

### 6. Output Processing
**Purpose**: Format AI response for delivery

**Common patterns**:
- Return directly (chat response)
- Store in database (conversation history)
- Send to communication channel (Slack, email)

---

## Common Use Cases

### 1. Conversational Chatbot
**Flow**: Webhook (chat message) → AI Agent → Webhook Response

**Example** (Customer support bot):
```
1. Webhook (path: "chat", POST)
   - Receives: {user_id, message, session_id}

2. Window Buffer Memory (load context by session_id)

3. AI Agent
   ├─ OpenAI Chat Model (gpt-4)
   ├─ HTTP Request Tool (search knowledge base)
   ├─ Database Tool (query customer orders)
   └─ Window Buffer Memory (conversation context)

4. Code (format response)

5. Webhook Response (send reply)
```

**AI Agent prompt**:
```
You are a customer support assistant.
You can:
1. Search the knowledge base for answers
2. Look up customer orders
3. Provide shipping information

Be helpful and professional.
```

### 2. Document Q&A
**Flow**: Upload docs → Embed → Store → Query with AI

**Example** (Internal documentation assistant):
```
Setup Phase (run once):
1. Read Files (load documentation)
2. Text Splitter (chunk into paragraphs)
3. Embeddings (OpenAI Embeddings)
4. Vector Store (Pinecone/Qdrant) (store vectors)

Query Phase (recurring):
1. Webhook (receive question)
2. AI Agent
   ├─ OpenAI Chat Model (gpt-4)
   ├─ Vector Store Tool (search similar docs)
   └─ Buffer Memory (context)
3. Webhook Response (answer with citations)
```

### 3. Data Analysis Assistant
**Flow**: Request → AI Agent (with data tools) → Analysis → Visualization

**Example** (SQL analyst agent):
```
1. Webhook (data question: "What were sales last month?")

2. AI Agent
   ├─ OpenAI Chat Model (gpt-4)
   ├─ Postgres Tool (execute queries)
   └─ Code Tool (data analysis)

3. Code (generate visualization data)

4. Webhook Response (answer + chart data)
```

**Postgres Tool Configuration**:
```javascript
{
  name: "query_database",
  description: "Execute SQL queries to analyze sales data. Use SELECT queries only.",
  // Node executes AI-generated SQL
}
```

### 4. Workflow Automation Agent
**Flow**: Command → AI Agent → Execute actions → Report

**Example** (DevOps assistant):
```
1. Slack (slash command: /deploy production)

2. AI Agent
   ├─ OpenAI Chat Model (gpt-4)
   ├─ HTTP Request Tool (GitHub API)
   ├─ HTTP Request Tool (Deploy API)
   └─ Postgres Tool (deployment logs)

3. Agent actions:
   - Check if tests passed
   - Create deployment
   - Log deployment
   - Notify team

4. Slack (deployment status)
```

### 5. Email Processing Agent
**Flow**: Email received → AI Agent → Categorize → Route → Respond

**Example** (Support ticket router):
```
1. Email Trigger (new support email)

2. AI Agent
   ├─ OpenAI Chat Model (gpt-4)
   ├─ Vector Store Tool (search similar tickets)
   └─ HTTP Request Tool (create Jira ticket)

3. Agent actions:
   - Categorize urgency (low/medium/high)
   - Find similar past tickets
   - Create ticket in appropriate project
   - Draft response

4. Email (send auto-response)
5. Slack (notify assigned team)
```

---

## Tool Configuration

### Making ANY Node an AI Tool

**Critical concept**: Any n8n node can become an AI tool!

**Requirements**:
1. Connect node to AI Agent via `ai_tool` port (NOT main port)
2. Configure tool name and description
3. Define input schema (optional)

**Example** (HTTP Request as tool):
```javascript
{
  // Tool metadata (for AI)
  name: "search_github_issues",
  description: "Search GitHub issues by keyword. Returns issue titles and URLs.",

  // HTTP Request configuration
  method: "GET",
  url: "https://api.github.com/search/issues",
  sendQuery: true,
  queryParameters: {
    "q": "={{$json.query}} repo:{{$json.repo}}",
    "per_page": "5"
  }
}
```

**How it works**:
1. AI Agent sees tool: `search_github_issues(query, repo)`
2. AI decides to use it: `search_github_issues("bug", "n8n-io/n8n")`
3. n8n executes HTTP Request with parameters
4. Result returned to AI Agent
5. AI Agent processes result and responds

### Pre-built Tool Nodes

**Available in @n8n/n8n-nodes-langchain**:

- **Calculator Tool** - Math operations
- **Wikipedia Tool** - Wikipedia search
- **Serper Tool** - Google search
- **Wolfram Alpha Tool** - Computational knowledge
- **Custom Tool** - Define with Code node
- **AI Agent Tool** - Sub-agents for specialized tasks
- **MCP Client Tool** - Model Context Protocol servers

**Example** (Calculator Tool):
```
AI Agent
  ├─ OpenAI Chat Model
  └─ Calculator Tool (ai_tool connection)

User: "What's 15% of 2,847?"
AI: *uses calculator tool* → "426.05"
```

### MCP Client Tool
**Use when**: Connecting to MCP servers (filesystem, databases, etc.)

```javascript
{
  name: "Filesystem Tool",
  type: "@n8n/n8n-nodes-langchain.mcpClientTool",
  parameters: {
    description: "Access file system to read files and list directories",
    mcpServer: {
      transport: "stdio",
      command: "npx",
      args: ["-y", "@modelcontextprotocol/server-filesystem", "/allowed/path"]
    },
    tool: "read_file"
  }
}
```

### AI Agent Tool (Sub-Agents)
**Use when**: Need specialized expertise from a sub-agent

```javascript
{
  name: "Research Specialist",
  type: "@n8n/n8n-nodes-langchain.agentTool",
  parameters: {
    name: "research_specialist",
    description: "Expert researcher for detailed research tasks",
    systemMessage: "You are a research specialist. Search thoroughly and provide analysis."
  }
}
```

### Database as Tool

**Pattern**: Postgres/MySQL node connected as ai_tool

**Configuration**:
```javascript
{
  // Tool metadata
  name: "query_customers",
  description: "Query customer database. Use SELECT queries to find customer information by email, name, or ID.",

  // Postgres config
  operation: "executeQuery",
  query: "={{$json.sql}}",  // AI provides SQL
  // Security: Use read-only database user!
}
```

**Safety**: Create read-only DB user for AI tools!

```sql
CREATE USER ai_readonly WITH PASSWORD 'secure_password';
GRANT SELECT ON customers, orders TO ai_readonly;
-- NO INSERT, UPDATE, DELETE access
```

### Code Node as Tool

**Pattern**: Custom Python/JavaScript function

**Example** (Data processor):
```javascript
// Tool metadata
{
  name: "process_csv",
  description: "Process CSV data and return statistics. Input: csv_string"
}

// Code node
const csv = $input.first().json.csv_string;
const lines = csv.split('\n');
const data = lines.slice(1).map(line => line.split(','));

return [{
  json: {
    row_count: data.length,
    columns: lines[0].split(','),
    summary: {
      // Calculate statistics
    }
  }
}];
```

---

## Memory Configuration

### Buffer Memory
**Stores all messages** (until cleared)

```javascript
{
  memoryType: "bufferMemory",
  sessionKey: "={{$json.body.user_id}}"  // Per-user memory
}
```

### Window Buffer Memory
**Stores last N messages** (recommended)

```javascript
{
  memoryType: "windowBufferMemory",
  sessionKey: "={{$json.body.session_id}}",
  contextWindowLength: 10  // Last 10 messages
}
```

### Summary Memory
**Summarizes old messages** (for long conversations)

```javascript
{
  memoryType: "summaryMemory",
  sessionKey: "={{$json.body.session_id}}",
  maxTokenLimit: 2000
}
```

**How it works**:
1. Conversation grows beyond limit
2. AI summarizes old messages
3. Summary stored, old messages discarded
4. Saves tokens while maintaining context

---

## Agent Types

### 1. Conversational Agent
**Best for**: General chat, customer support

**Features**:
- Natural conversation flow
- Memory integration
- Tool use with reasoning

**When to use**: Most common use case

### 2. OpenAI Functions Agent
**Best for**: Tool-heavy workflows, structured outputs

**Features**:
- Optimized for function calling
- Better tool selection
- Structured responses

**When to use**: Multiple tools, need reliable tool calling

### 3. ReAct Agent
**Best for**: Step-by-step reasoning

**Features**:
- Think → Act → Observe loop
- Visible reasoning process
- Good for debugging

**When to use**: Complex multi-step tasks

---

## Prompt Engineering for Agents

### System Prompt Structure
```
You are a [ROLE].

You can:
- [CAPABILITY 1]
- [CAPABILITY 2]
- [CAPABILITY 3]

Guidelines:
- [GUIDELINE 1]
- [GUIDELINE 2]

Format:
- [OUTPUT FORMAT]
```

### Example (Customer Support)
```
You are a customer support assistant for Acme Corp.

You can:
- Search the knowledge base for answers
- Look up customer orders and shipping status
- Create support tickets for complex issues

Guidelines:
- Be friendly and professional
- If you don't know something, say so and offer to create a ticket
- Always verify customer identity before sharing order details

Format:
- Keep responses concise
- Use bullet points for multiple items
- Include relevant links when available
```

### Example (Data Analyst)
```
You are a data analyst assistant with access to the company database.

You can:
- Query sales, customer, and product data
- Perform data analysis and calculations
- Generate summary statistics

Guidelines:
- Write efficient SQL queries (always use LIMIT)
- Explain your analysis methodology
- Highlight important trends or anomalies
- Use read-only queries (SELECT only)

Format:
- Provide numerical answers with context
- Include query used (for transparency)
- Suggest follow-up analyses when relevant
```

---

## Advanced Patterns

### Streaming Responses
For real-time user experience, set Chat Trigger to streaming mode:

```javascript
// Chat Trigger parameters
{
  options: {
    responseMode: "streaming"  // or "lastNode" for non-streaming
  }
}
```

**Important**: When using streaming mode, the AI Agent must NOT have main output connections - responses stream back through Chat Trigger automatically.

### Fallback Language Models
For production reliability, connect a fallback model:

```javascript
// Primary model (targetIndex: 0)
{
  type: "addConnection",
  source: "OpenAI Chat Model",
  target: "AI Agent",
  sourceOutput: "ai_languageModel",
  targetIndex: 0
}

// Fallback model (targetIndex: 1)
{
  type: "addConnection",
  source: "Anthropic Chat Model",
  target: "AI Agent",
  sourceOutput: "ai_languageModel",
  targetIndex: 1
}
```

Enable with: `"parameters.needsFallback": true` on the AI Agent node.

### RAG (Retrieval-Augmented Generation)
Complete knowledge base setup chain:

```
Documents → Text Splitter → Vector Store ← Embeddings
                              ↓
                        Vector Store Tool → AI Agent
```

Use `ai_embedding`, `ai_document`, `ai_vectorStore`, and `ai_tool` connection types.

---

## Error Handling

### Pattern 1: Tool Execution Errors
```
AI Agent (continueOnFail on tool nodes)
  → IF (tool error occurred)
    └─ Code (log error)
    └─ Webhook Response (user-friendly error)
```

### Pattern 2: LLM API Errors
```
Main Workflow:
  AI Agent → Process Response

Error Workflow:
  Error Trigger
    → IF (rate limit error)
      └─ Wait → Retry
    → ELSE
      └─ Notify Admin
```

### Pattern 3: Invalid Tool Outputs
```javascript
// Code node - validate tool output
const result = $input.first().json;

if (!result || !result.data) {
  throw new Error('Tool returned invalid data');
}

return [{ json: result }];
```

---

## Performance Optimization

### 1. Choose Right Model
```
Fast & cheap: GPT-3.5-turbo, Claude 3 Haiku
Balanced: GPT-4, Claude 3 Sonnet
Powerful: GPT-4-turbo, Claude 3 Opus
```

### 2. Limit Context Window
```javascript
{
  memoryType: "windowBufferMemory",
  contextWindowLength: 5  // Only last 5 messages
}
```

### 3. Optimize Tool Descriptions
```javascript
// ❌ Vague
description: "Search for things"

// ✅ Clear and concise
description: "Search GitHub issues by keyword and repository. Returns top 5 matching issues with titles and URLs."
```

### 4. Cache Embeddings
For document Q&A, embed documents once:

```
Setup (run once):
  Documents → Embed → Store in Vector DB

Query (fast):
  Question → Search Vector DB → AI Agent
```

### 5. Async Tools for Slow Operations
```
AI Agent → [Queue slow tool request]
       → Return immediate response
       → [Background: Execute tool + notify when done]
```

---

## Security Considerations

### 1. Read-Only Database Tools
```sql
-- Create limited user for AI tools
CREATE USER ai_agent_ro WITH PASSWORD 'secure';
GRANT SELECT ON public.* TO ai_agent_ro;
-- NO write access!
```

### 2. Validate Tool Inputs
```javascript
// Code node - validate before execution
const query = $json.query;

if (query.toLowerCase().includes('drop ') ||
    query.toLowerCase().includes('delete ') ||
    query.toLowerCase().includes('update ')) {
  throw new Error('Invalid query - write operations not allowed');
}
```

### 3. Rate Limiting
```
Webhook → IF (check user rate limit)
        ├─ [Within limit] → AI Agent
        └─ [Exceeded] → Error (429 Too Many Requests)
```

### 4. Sanitize User Input
```javascript
// Code node
const userInput = $json.body.message
  .trim()
  .substring(0, 1000);  // Max 1000 chars

return [{ json: { sanitized: userInput } }];
```

### 5. Monitor Tool Usage
```
AI Agent → Log Tool Calls
        → IF (suspicious pattern)
          └─ Alert Admin + Pause Agent
```

---

## Testing AI Agents

### 1. Start with Manual Trigger
Replace webhook with manual trigger:
```
Manual Trigger
  → Set (mock user input)
  → AI Agent
  → Code (log output)
```

### 2. Test Tools Independently
Before connecting to agent:
```
Manual Trigger → Tool Node → Verify output format
```

### 3. Test with Standard Questions
Create test suite:
```
1. "Hello" - Test basic response
2. "Search for bug reports" - Test tool calling
3. "What did I ask before?" - Test memory
4. Invalid input - Test error handling
```

### 4. Monitor Token Usage
```javascript
// Code node - log token usage
console.log('Input tokens:', $node['AI Agent'].json.usage.input_tokens);
console.log('Output tokens:', $node['AI Agent'].json.usage.output_tokens);
```

### 5. Test Edge Cases
- Empty input
- Very long input
- Tool returns no results
- Tool returns error
- Multiple tool calls in sequence

---

## Common Gotchas

### 1. ❌ Wrong: Connecting tools to main port
```
HTTP Request → AI Agent  // Won't work as tool!
```

### ✅ Correct: Use ai_tool connection type
```
HTTP Request --[ai_tool]--> AI Agent
```

### 2. ❌ Wrong: Vague tool descriptions
```
description: "Get data"  // AI won't know when to use this
```

### ✅ Correct: Specific descriptions
```
description: "Query customer orders by email address. Returns order ID, status, and shipping info."
```

### 3. ❌ Wrong: No memory for conversations
```
Every message is standalone - no context!
```

### ✅ Correct: Add memory
```
Window Buffer Memory --[ai_memory]--> AI Agent
```

### 4. ❌ Wrong: Giving AI write access
```
Postgres (full access) as tool  // AI could DELETE data!
```

### ✅ Correct: Read-only access
```
Postgres (read-only user) as tool  // Safe
```

### 5. ❌ Wrong: Unbounded tool responses
```
Tool returns 10MB of data → exceeds token limit
```

### ✅ Correct: Limit tool output
```javascript
{
  query: "SELECT * FROM table LIMIT 10"  // Only 10 rows
}
```

---

## Real Template Examples

From n8n template library (234 AI templates):

**Simple Chatbot**:
```
Webhook → AI Agent (GPT-4 + Memory) → Webhook Response
```

**Document Q&A**:
```
Setup: Files → Embed → Vector Store
Query: Webhook → AI Agent (GPT-4 + Vector Store Tool) → Response
```

**SQL Analyst**:
```
Webhook → AI Agent (GPT-4 + Postgres Tool) → Format → Response
```

Use `search_templates({query: "ai agent"})` to find more!

---

## Checklist for AI Agent Workflows

### Planning
- [ ] Define agent purpose and capabilities
- [ ] List required tools (APIs, databases, etc.)
- [ ] Design conversation flow
- [ ] Plan memory strategy (per-user, per-session)
- [ ] Consider token costs

### Implementation
- [ ] Choose appropriate LLM model
- [ ] Write clear system prompt
- [ ] Connect tools via ai_tool ports (NOT main)
- [ ] Add tool descriptions
- [ ] Configure memory (Window Buffer recommended)
- [ ] Test each tool independently

### Security
- [ ] Use read-only database access for tools
- [ ] Validate tool inputs
- [ ] Sanitize user inputs
- [ ] Add rate limiting
- [ ] Monitor for abuse

### Testing
- [ ] Test with diverse inputs
- [ ] Verify tool calling works
- [ ] Check memory persistence
- [ ] Test error scenarios
- [ ] Monitor token usage and costs

### Deployment
- [ ] Add error handling
- [ ] Set up logging
- [ ] Monitor performance
- [ ] Set cost alerts
- [ ] Document agent capabilities

---

## Summary

**Key Points**:
1. **8 AI connection types** - Use ai_tool for tools, ai_memory for context
2. **ANY node can be a tool** - Connect to ai_tool port
3. **Memory is essential** for conversations (Window Buffer recommended)
4. **Tool descriptions matter** - AI uses them to decide when to call tools
5. **Security first** - Read-only database access, validate inputs

**Pattern**: Trigger → AI Agent (Model + Tools + Memory) → Output

**Related**:
- [webhook_processing.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/webhook_processing.md) - Receiving chat messages
- [http_api_integration.md](http_api_integration.md) - Tools that call APIs
- [database_operations.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/database_operations.md) - Database tools for agents
```

## File: `skills/n8n-workflow-patterns/database_operations.md`
```markdown
# Database Operations Pattern

**Use Case**: Read, write, sync, and manage database data in workflows.

---

## Pattern Structure

```
Trigger → [Query/Read] → [Transform] → [Write/Update] → [Verify/Log]
```

**Key Characteristic**: Data persistence and synchronization

---

## Core Components

### 1. Trigger
**Options**:
- **Schedule** - Periodic sync/maintenance (most common)
- **Webhook** - Event-driven writes
- **Manual** - One-time operations

### 2. Database Read Nodes
**Supported databases**:
- Postgres
- MySQL
- MongoDB
- Microsoft SQL
- SQLite
- Redis
- And more via community nodes

### 3. Transform
**Purpose**: Map between different database schemas or formats

**Typical nodes**:
- **Set** - Field mapping
- **Code** - Complex transformations
- **Merge** - Combine data from multiple sources

### 4. Database Write Nodes
**Operations**:
- INSERT - Create new records
- UPDATE - Modify existing records
- UPSERT - Insert or update
- DELETE - Remove records

### 5. Verification
**Purpose**: Confirm operations succeeded

**Methods**:
- Query to verify records
- Count rows affected
- Log results

---

## Common Use Cases

### 1. Data Synchronization
**Flow**: Schedule → Read Source DB → Transform → Write Target DB → Log

**Example** (Postgres to MySQL sync):
```
1. Schedule (every 15 minutes)
2. Postgres (SELECT * FROM users WHERE updated_at > {{$json.last_sync}})
3. IF (check if records exist)
4. Set (map Postgres schema to MySQL schema)
5. MySQL (INSERT or UPDATE users)
6. Postgres (UPDATE sync_log SET last_sync = NOW())
7. Slack (notify: "Synced X users")
```

**Incremental sync query**:
```sql
SELECT *
FROM users
WHERE updated_at > $1
ORDER BY updated_at ASC
LIMIT 1000
```

**Parameters**:
```javascript
{
  "parameters": [
    "={{$node['Get Last Sync'].json.last_sync}}"
  ]
}
```

### 2. ETL (Extract, Transform, Load)
**Flow**: Extract from multiple sources → Transform → Load into warehouse

**Example** (Consolidate data):
```
1. Schedule (daily at 2 AM)
2. [Parallel branches]
   ├─ Postgres (SELECT orders)
   ├─ MySQL (SELECT customers)
   └─ MongoDB (SELECT products)
3. Merge (combine all data)
4. Code (transform to warehouse schema)
5. Postgres (warehouse - INSERT into fact_sales)
6. Email (send summary report)
```

### 3. Data Validation & Cleanup
**Flow**: Schedule → Query → Validate → Update/Delete invalid records

**Example** (Clean orphaned records):
```
1. Schedule (weekly)
2. Postgres (SELECT users WHERE email IS NULL OR email = '')
3. IF (invalid records exist)
4. Postgres (UPDATE users SET status='inactive' WHERE email IS NULL)
5. Postgres (DELETE FROM users WHERE created_at < NOW() - INTERVAL '1 year' AND status='inactive')
6. Slack (alert: "Cleaned X invalid records")
```

### 4. Backup & Archive
**Flow**: Schedule → Query → Export → Store

**Example** (Archive old records):
```
1. Schedule (monthly)
2. Postgres (SELECT * FROM orders WHERE created_at < NOW() - INTERVAL '2 years')
3. Code (convert to JSON)
4. Write File (save to archive.json)
5. Google Drive (upload archive)
6. Postgres (DELETE FROM orders WHERE created_at < NOW() - INTERVAL '2 years')
```

### 5. Real-time Data Updates
**Flow**: Webhook → Parse → Update Database

**Example** (Update user status):
```
1. Webhook (receive status update)
2. Postgres (UPDATE users SET status = {{$json.body.status}} WHERE id = {{$json.body.user_id}})
3. IF (rows affected > 0)
4. Redis (SET user:{{$json.body.user_id}}:status {{$json.body.status}})
5. Webhook Response ({"success": true})
```

---

## Database Node Configuration

### Postgres

#### SELECT Query
```javascript
{
  operation: "executeQuery",
  query: "SELECT id, name, email FROM users WHERE created_at > $1 LIMIT $2",
  parameters: [
    "={{$json.since_date}}",
    "100"
  ]
}
```

#### INSERT
```javascript
{
  operation: "insert",
  table: "users",
  columns: "id, name, email, created_at",
  values: [
    {
      id: "={{$json.id}}",
      name: "={{$json.name}}",
      email: "={{$json.email}}",
      created_at: "={{$now}}"
    }
  ]
}
```

#### UPDATE
```javascript
{
  operation: "update",
  table: "users",
  updateKey: "id",
  columns: "name, email, updated_at",
  values: {
    id: "={{$json.id}}",
    name: "={{$json.name}}",
    email: "={{$json.email}}",
    updated_at: "={{$now}}"
  }
}
```

#### UPSERT (INSERT ... ON CONFLICT)
```javascript
{
  operation: "executeQuery",
  query: `
    INSERT INTO users (id, name, email)
    VALUES ($1, $2, $3)
    ON CONFLICT (id)
    DO UPDATE SET name = $2, email = $3, updated_at = NOW()
  `,
  parameters: [
    "={{$json.id}}",
    "={{$json.name}}",
    "={{$json.email}}"
  ]
}
```

### MySQL

#### SELECT with JOIN
```javascript
{
  operation: "executeQuery",
  query: `
    SELECT u.id, u.name, o.order_id, o.total
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    WHERE u.created_at > ?
  `,
  parameters: [
    "={{$json.since_date}}"
  ]
}
```

#### Bulk INSERT
```javascript
{
  operation: "insert",
  table: "orders",
  columns: "user_id, total, status",
  values: $json.orders  // Array of objects
}
```

### MongoDB

#### Find Documents
```javascript
{
  operation: "find",
  collection: "users",
  query: JSON.stringify({
    created_at: { $gt: new Date($json.since_date) },
    status: "active"
  }),
  limit: 100
}
```

#### Insert Document
```javascript
{
  operation: "insert",
  collection: "users",
  document: JSON.stringify({
    name: $json.name,
    email: $json.email,
    created_at: new Date()
  })
}
```

#### Update Document
```javascript
{
  operation: "update",
  collection: "users",
  query: JSON.stringify({ _id: $json.user_id }),
  update: JSON.stringify({
    $set: {
      status: $json.status,
      updated_at: new Date()
    }
  })
}
```

---

## Batch Processing

### Pattern 1: Split In Batches
**Use when**: Processing large datasets to avoid memory issues

```
Postgres (SELECT 10000 records)
  → Split In Batches (100 items per batch)
  → Transform
  → MySQL (write batch)
  → Loop (until all processed)
```

### Pattern 2: Paginated Queries
**Use when**: Database has millions of records

```
Set (initialize: offset=0, limit=1000)
  → Loop Start
  → Postgres (SELECT * FROM large_table LIMIT {{$json.limit}} OFFSET {{$json.offset}})
  → IF (records returned)
    ├─ Process records
    ├─ Set (increment offset by 1000)
    └─ Loop back
  └─ [No records] → End
```

**Query**:
```sql
SELECT * FROM large_table
ORDER BY id
LIMIT $1 OFFSET $2
```

### Pattern 3: Cursor-Based Pagination
**Better performance for large datasets**:

```
Set (initialize: last_id=0)
  → Loop Start
  → Postgres (SELECT * FROM table WHERE id > {{$json.last_id}} ORDER BY id LIMIT 1000)
  → IF (records returned)
    ├─ Process records
    ├─ Code (get max id from batch)
    └─ Loop back
  └─ [No records] → End
```

**Query**:
```sql
SELECT * FROM table
WHERE id > $1
ORDER BY id ASC
LIMIT 1000
```

---

## Transaction Handling

### Pattern 1: BEGIN/COMMIT/ROLLBACK
**For databases that support transactions**:

```javascript
// Node 1: Begin Transaction
{
  operation: "executeQuery",
  query: "BEGIN"
}

// Node 2-N: Your operations
{
  operation: "executeQuery",
  query: "INSERT INTO ...",
  continueOnFail: true
}

// Node N+1: Commit or Rollback
{
  operation: "executeQuery",
  query: "={{$node['Operation'].json.error ? 'ROLLBACK' : 'COMMIT'}}"
}
```

### Pattern 2: Atomic Operations
**Use database features for atomicity**:

```sql
-- Upsert example (atomic)
INSERT INTO inventory (product_id, quantity)
VALUES ($1, $2)
ON CONFLICT (product_id)
DO UPDATE SET quantity = inventory.quantity + $2
```

### Pattern 3: Error Rollback
**Manual rollback on error**:

```
Try Operations:
  Postgres (INSERT orders)
  MySQL (INSERT order_items)

Error Trigger:
  Postgres (DELETE FROM orders WHERE id = {{$json.order_id}})
  MySQL (DELETE FROM order_items WHERE order_id = {{$json.order_id}})
```

---

## Data Transformation

### Schema Mapping
```javascript
// Code node - map schemas
const sourceData = $input.all();

return sourceData.map(item => ({
  json: {
    // Source → Target mapping
    user_id: item.json.id,
    full_name: `${item.json.first_name} ${item.json.last_name}`,
    email_address: item.json.email,
    registration_date: new Date(item.json.created_at).toISOString(),
    // Computed fields
    is_premium: item.json.plan_type === 'pro',
    // Default values
    status: item.json.status || 'active'
  }
}));
```

### Data Type Conversions
```javascript
// Code node - convert data types
return $input.all().map(item => ({
  json: {
    // String to number
    user_id: parseInt(item.json.user_id),
    // String to date
    created_at: new Date(item.json.created_at),
    // Number to boolean
    is_active: item.json.active === 1,
    // JSON string to object
    metadata: JSON.parse(item.json.metadata || '{}'),
    // Null handling
    email: item.json.email || null
  }
}));
```

### Aggregation
```javascript
// Code node - aggregate data
const items = $input.all();

const summary = items.reduce((acc, item) => {
  const date = item.json.created_at.split('T')[0];
  if (!acc[date]) {
    acc[date] = { count: 0, total: 0 };
  }
  acc[date].count++;
  acc[date].total += item.json.amount;
  return acc;
}, {});

return Object.entries(summary).map(([date, data]) => ({
  json: {
    date,
    count: data.count,
    total: data.total,
    average: data.total / data.count
  }
}));
```

---

## Performance Optimization

### 1. Use Indexes
Ensure database has proper indexes:

```sql
-- Add index for sync queries
CREATE INDEX idx_users_updated_at ON users(updated_at);

-- Add index for lookups
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

### 2. Limit Result Sets
Always use LIMIT:

```sql
-- ✅ Good
SELECT * FROM large_table
WHERE created_at > $1
LIMIT 1000

-- ❌ Bad (unbounded)
SELECT * FROM large_table
WHERE created_at > $1
```

### 3. Use Prepared Statements
Parameterized queries are faster:

```javascript
// ✅ Good - prepared statement
{
  query: "SELECT * FROM users WHERE id = $1",
  parameters: ["={{$json.id}}"]
}

// ❌ Bad - string concatenation
{
  query: "SELECT * FROM users WHERE id = '={{$json.id}}'"
}
```

### 4. Batch Writes
Write multiple records at once:

```javascript
// ✅ Good - batch insert
{
  operation: "insert",
  table: "orders",
  values: $json.items  // Array of 100 items
}

// ❌ Bad - individual inserts in loop
// 100 separate INSERT statements
```

### 5. Connection Pooling
Configure in credentials:

```javascript
{
  host: "db.example.com",
  database: "mydb",
  user: "user",
  password: "pass",
  // Connection pool settings
  min: 2,
  max: 10,
  idleTimeoutMillis: 30000
}
```

---

## Error Handling

### Pattern 1: Check Rows Affected
```
Database Operation (UPDATE users...)
  → IF ({{$json.rowsAffected === 0}})
    └─ Alert: "No rows updated - record not found"
```

### Pattern 2: Constraint Violations
```javascript
// Database operation with continueOnFail: true
{
  operation: "insert",
  continueOnFail: true
}

// Next node: Check for errors
IF ({{$json.error !== undefined}})
  → IF ({{$json.error.includes('duplicate key')}})
    └─ Log: "Record already exists - skipping"
  → ELSE
    └─ Alert: "Database error: {{$json.error}}"
```

### Pattern 3: Rollback on Error
```
Try Operations:
  → Database Write 1
  → Database Write 2
  → Database Write 3

Error Trigger:
  → Rollback Operations
  → Alert Admin
```

---

## Security Best Practices

### 1. Use Parameterized Queries (Prevent SQL Injection)
```javascript
// ✅ SAFE - parameterized
{
  query: "SELECT * FROM users WHERE email = $1",
  parameters: ["={{$json.email}}"]
}

// ❌ DANGEROUS - SQL injection risk
{
  query: "SELECT * FROM users WHERE email = '={{$json.email}}'"
}
```

### 2. Least Privilege Access
**Create dedicated workflow user**:

```sql
-- ✅ Good - limited permissions
CREATE USER n8n_workflow WITH PASSWORD 'secure_password';
GRANT SELECT, INSERT, UPDATE ON orders TO n8n_workflow;
GRANT SELECT ON users TO n8n_workflow;

-- ❌ Bad - too much access
GRANT ALL PRIVILEGES TO n8n_workflow;
```

### 3. Validate Input Data
```javascript
// Code node - validate before write
const email = $json.email;
const name = $json.name;

// Validation
if (!email || !email.includes('@')) {
  throw new Error('Invalid email address');
}

if (!name || name.length < 2) {
  throw new Error('Invalid name');
}

// Sanitization
return [{
  json: {
    email: email.toLowerCase().trim(),
    name: name.trim()
  }
}];
```

### 4. Encrypt Sensitive Data
```javascript
// Code node - encrypt before storage
const crypto = require('crypto');

const algorithm = 'aes-256-cbc';
const key = Buffer.from($credentials.encryptionKey, 'hex');
const iv = crypto.randomBytes(16);

const cipher = crypto.createCipheriv(algorithm, key, iv);
let encrypted = cipher.update($json.sensitive_data, 'utf8', 'hex');
encrypted += cipher.final('hex');

return [{
  json: {
    encrypted_data: encrypted,
    iv: iv.toString('hex')
  }
}];
```

---

## Common Gotchas

### 1. ❌ Wrong: Unbounded queries
```sql
SELECT * FROM large_table  -- Could return millions
```

### ✅ Correct: Use LIMIT
```sql
SELECT * FROM large_table
ORDER BY created_at DESC
LIMIT 1000
```

### 2. ❌ Wrong: String concatenation in queries
```javascript
query: "SELECT * FROM users WHERE id = '{{$json.id}}'"
```

### ✅ Correct: Parameterized queries
```javascript
query: "SELECT * FROM users WHERE id = $1",
parameters: ["={{$json.id}}"]
```

### 3. ❌ Wrong: No transaction for multi-step operations
```
INSERT into orders
INSERT into order_items  // Fails → orphaned order record
```

### ✅ Correct: Use transaction
```
BEGIN
INSERT into orders
INSERT into order_items
COMMIT (or ROLLBACK on error)
```

### 4. ❌ Wrong: Processing all items at once
```
SELECT 1000000 records → Process all → OOM error
```

### ✅ Correct: Batch processing
```
SELECT records → Split In Batches (1000) → Process → Loop
```

---

## Real Template Examples

From n8n template library (456 database templates):

**Data Sync**:
```
Schedule → Postgres (SELECT new records) → Transform → MySQL (INSERT)
```

**ETL Pipeline**:
```
Schedule → [Multiple DB reads] → Merge → Transform → Warehouse (INSERT)
```

**Backup**:
```
Schedule → Postgres (SELECT all) → JSON → Google Drive (upload)
```

Use `search_templates({query: "database"})` to find more!

---

## Checklist for Database Workflows

### Planning
- [ ] Identify source and target databases
- [ ] Understand schema differences
- [ ] Plan transformation logic
- [ ] Consider batch size for large datasets
- [ ] Design error handling strategy

### Implementation
- [ ] Use parameterized queries (never concatenate)
- [ ] Add LIMIT to all SELECT queries
- [ ] Use appropriate operation (INSERT/UPDATE/UPSERT)
- [ ] Configure credentials properly
- [ ] Test with small dataset first

### Performance
- [ ] Add database indexes for queries
- [ ] Use batch operations
- [ ] Implement pagination for large datasets
- [ ] Configure connection pooling
- [ ] Monitor query execution times

### Security
- [ ] Use parameterized queries (SQL injection prevention)
- [ ] Least privilege database user
- [ ] Validate and sanitize input
- [ ] Encrypt sensitive data
- [ ] Never log sensitive data

### Reliability
- [ ] Add transaction handling if needed
- [ ] Check rows affected
- [ ] Handle constraint violations
- [ ] Implement retry logic
- [ ] Add Error Trigger workflow

---

## Summary

**Key Points**:
1. **Always use parameterized queries** (prevent SQL injection)
2. **Batch processing** for large datasets
3. **Transaction handling** for multi-step operations
4. **Limit result sets** to avoid memory issues
5. **Validate input data** before writes

**Pattern**: Trigger → Query → Transform → Write → Verify

**Related**:
- [http_api_integration.md](http_api_integration.md) - Fetching data to store in DB
- [scheduled_tasks.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/scheduled_tasks.md) - Periodic database maintenance
```

## File: `skills/n8n-workflow-patterns/http_api_integration.md`
```markdown
# HTTP API Integration Pattern

**Use Case**: Fetch data from REST APIs, transform it, and use it in workflows.

---

## Pattern Structure

```
Trigger → HTTP Request → [Transform] → [Action] → [Error Handler]
```

**Key Characteristic**: External data fetching with error handling

---

## Core Components

### 1. Trigger
**Options**:
- **Schedule** - Periodic fetching (most common)
- **Webhook** - Triggered by external event
- **Manual** - On-demand execution

### 2. HTTP Request Node
**Purpose**: Call external REST APIs

**Configuration**:
```javascript
{
  method: "GET",                    // GET, POST, PUT, DELETE, PATCH
  url: "https://api.example.com/users",
  authentication: "predefinedCredentialType",
  sendQuery: true,
  queryParameters: {
    "page": "={{$json.page}}",
    "limit": "100"
  },
  sendHeaders: true,
  headerParameters: {
    "Accept": "application/json",
    "X-API-Version": "v1"
  }
}
```

### 3. Response Processing
**Purpose**: Extract and transform API response data

**Typical flow**:
```
HTTP Request → Code (parse) → Set (map fields) → Action
```

### 4. Action
**Common actions**:
- Store in database
- Send to another API
- Create notifications
- Update spreadsheet

### 5. Error Handler
**Purpose**: Handle API failures gracefully

**Error Trigger Workflow**:
```
Error Trigger → Log Error → Notify Admin → Retry Logic (optional)
```

---

## Common Use Cases

### 1. Data Fetching & Storage
**Flow**: Schedule → HTTP Request → Transform → Database

**Example** (Fetch GitHub issues):
```
1. Schedule (every hour)
2. HTTP Request
   - Method: GET
   - URL: https://api.github.com/repos/owner/repo/issues
   - Auth: Bearer Token
   - Query: state=open
3. Code (filter by labels)
4. Set (map to database schema)
5. Postgres (upsert issues)
```

**Response Handling**:
```javascript
// Code node - filter issues
const issues = $input.all();
return issues
  .filter(item => item.json.labels.some(l => l.name === 'bug'))
  .map(item => ({
    json: {
      id: item.json.id,
      title: item.json.title,
      created_at: item.json.created_at
    }
  }));
```

### 2. API to API Integration
**Flow**: Trigger → Fetch from API A → Transform → Send to API B

**Example** (Jira to Slack):
```
1. Schedule (every 15 minutes)
2. HTTP Request (GET Jira tickets updated today)
3. IF (check if tickets exist)
4. Set (format for Slack)
5. HTTP Request (POST to Slack webhook)
```

### 3. Data Enrichment
**Flow**: Trigger → Fetch base data → Call enrichment API → Combine → Store

**Example** (Enrich contacts with company data):
```
1. Postgres (SELECT new contacts)
2. Code (extract company domains)
3. HTTP Request (call Clearbit API for each domain)
4. Set (combine contact + company data)
5. Postgres (UPDATE contacts with enrichment)
```

### 4. Monitoring & Alerting
**Flow**: Schedule → Check API health → IF unhealthy → Alert

**Example** (API health check):
```
1. Schedule (every 5 minutes)
2. HTTP Request (GET /health endpoint)
3. IF (status !== 200 OR response time > 2000ms)
4. Slack (alert #ops-team)
5. PagerDuty (create incident)
```

### 5. Batch Processing
**Flow**: Trigger → Fetch large dataset → Split in Batches → Process → Loop

**Example** (Process all users):
```
1. Manual Trigger
2. HTTP Request (GET /api/users?limit=1000)
3. Split In Batches (100 items per batch)
4. HTTP Request (POST /api/process for each batch)
5. Wait (2 seconds between batches - rate limiting)
6. Loop (back to step 4 until all processed)
```

---

## Authentication Methods

### 1. None (Public APIs)
```javascript
{
  authentication: "none"
}
```

### 2. Bearer Token (Most Common)
**Setup**: Create credential
```javascript
{
  authentication: "predefinedCredentialType",
  nodeCredentialType: "httpHeaderAuth",
  headerAuth: {
    name: "Authorization",
    value: "Bearer YOUR_TOKEN"
  }
}
```

**Access in workflow**:
```javascript
{
  authentication: "predefinedCredentialType",
  nodeCredentialType: "httpHeaderAuth"
}
```

### 3. API Key (Header or Query)
**Header auth**:
```javascript
{
  sendHeaders: true,
  headerParameters: {
    "X-API-Key": "={{$credentials.apiKey}}"
  }
}
```

**Query auth**:
```javascript
{
  sendQuery: true,
  queryParameters: {
    "api_key": "={{$credentials.apiKey}}"
  }
}
```

### 4. Basic Auth
**Setup**: Create "Basic Auth" credential
```javascript
{
  authentication: "predefinedCredentialType",
  nodeCredentialType: "httpBasicAuth"
}
```

### 5. OAuth2
**Setup**: Create OAuth2 credential with:
- Authorization URL
- Token URL
- Client ID
- Client Secret
- Scopes

```javascript
{
  authentication: "predefinedCredentialType",
  nodeCredentialType: "oAuth2Api"
}
```

---

## Handling API Responses

### Success Response (200-299)
**Default**: Data flows to next node

**Access response**:
```javascript
// Entire response
{{$json}}

// Specific fields
{{$json.data.id}}
{{$json.results[0].name}}
```

### Pagination

#### Pattern 1: Offset-based
```
1. Set (initialize: page=1, has_more=true)
2. HTTP Request (GET /api/items?page={{$json.page}})
3. Code (check if more pages)
4. IF (has_more === true)
   └→ Set (increment page) → Loop to step 2
```

**Code node** (check pagination):
```javascript
const items = $input.first().json;
const currentPage = $json.page || 1;

return [{
  json: {
    items: items.results,
    page: currentPage + 1,
    has_more: items.next !== null
  }
}];
```

#### Pattern 2: Cursor-based
```
1. HTTP Request (GET /api/items)
2. Code (extract next_cursor)
3. IF (next_cursor exists)
   └→ Set (cursor={{$json.next_cursor}}) → Loop to step 1
```

#### Pattern 3: Link Header
```javascript
// Code node - parse Link header
const linkHeader = $input.first().json.headers['link'];
const hasNext = linkHeader && linkHeader.includes('rel="next"');

return [{
  json: {
    items: $input.first().json.body,
    has_next: hasNext,
    next_url: hasNext ? parseNextUrl(linkHeader) : null
  }
}];
```

### Error Responses (400-599)

**Configure HTTP Request**:
```javascript
{
  continueOnFail: true,  // Don't stop workflow on error
  ignoreResponseCode: true  // Get response even on error
}
```

**Handle errors**:
```
HTTP Request (continueOnFail: true)
  → IF (check error)
    ├─ [Success Path]
    └─ [Error Path] → Log → Retry or Alert
```

**IF condition**:
```javascript
{{$json.error}} is empty
// OR
{{$json.statusCode}} < 400
```

---

## Rate Limiting

### Pattern 1: Wait Between Requests
```
Split In Batches (1 item per batch)
  → HTTP Request
  → Wait (1 second)
  → Loop
```

### Pattern 2: Exponential Backoff
```javascript
// Code node
const maxRetries = 3;
let retryCount = $json.retryCount || 0;

if ($json.error && retryCount < maxRetries) {
  const delay = Math.pow(2, retryCount) * 1000; // 1s, 2s, 4s

  return [{
    json: {
      ...$json,
      retryCount: retryCount + 1,
      waitTime: delay
    }
  }];
}
```

### Pattern 3: Respect Rate Limit Headers
```javascript
// Code node - check rate limit
const headers = $input.first().json.headers;
const remaining = parseInt(headers['x-ratelimit-remaining'] || '999');
const resetTime = parseInt(headers['x-ratelimit-reset'] || '0');

if (remaining < 10) {
  const now = Math.floor(Date.now() / 1000);
  const waitSeconds = resetTime - now;

  return [{
    json: {
      shouldWait: true,
      waitSeconds: Math.max(waitSeconds, 0)
    }
  }];
}

return [{ json: { shouldWait: false } }];
```

---

## Request Configuration

### GET Request
```javascript
{
  method: "GET",
  url: "https://api.example.com/users",
  sendQuery: true,
  queryParameters: {
    "page": "1",
    "limit": "100",
    "filter": "active"
  }
}
```

### POST Request (JSON Body)
```javascript
{
  method: "POST",
  url: "https://api.example.com/users",
  sendBody: true,
  bodyParametersJson: JSON.stringify({
    name: "={{$json.name}}",
    email: "={{$json.email}}",
    role: "user"
  })
}
```

### POST Request (Form Data)
```javascript
{
  method: "POST",
  url: "https://api.example.com/upload",
  sendBody: true,
  bodyParametersUi: {
    parameter: [
      { name: "file", value: "={{$json.fileData}}" },
      { name: "filename", value: "={{$json.filename}}" }
    ]
  },
  sendHeaders: true,
  headerParameters: {
    "Content-Type": "multipart/form-data"
  }
}
```

### PUT/PATCH Request (Update)
```javascript
{
  method: "PATCH",
  url: "https://api.example.com/users/={{$json.userId}}",
  sendBody: true,
  bodyParametersJson: JSON.stringify({
    status: "active",
    last_updated: "={{$now}}"
  })
}
```

### DELETE Request
```javascript
{
  method: "DELETE",
  url: "https://api.example.com/users/={{$json.userId}}"
}
```

---

## Error Handling Patterns

### Pattern 1: Retry on Failure
```
HTTP Request (continueOnFail: true)
  → IF (error occurred)
    └→ Wait (5 seconds)
    └→ HTTP Request (retry)
```

### Pattern 2: Fallback API
```
HTTP Request (Primary API, continueOnFail: true)
  → IF (failed)
    └→ HTTP Request (Fallback API)
```

### Pattern 3: Error Trigger Workflow
**Main Workflow**:
```
HTTP Request → Process Data
```

**Error Workflow**:
```
Error Trigger
  → Set (extract error details)
  → Slack (alert team)
  → Database (log error for analysis)
```

### Pattern 4: Circuit Breaker
```javascript
// Code node - circuit breaker logic
const failures = $json.recentFailures || 0;
const threshold = 5;

if (failures >= threshold) {
  throw new Error('Circuit breaker open - too many failures');
}

return [{ json: { canProceed: true } }];
```

---

## Response Transformation

### Extract Nested Data
```javascript
// Code node
const response = $input.first().json;

return response.data.items.map(item => ({
  json: {
    id: item.id,
    name: item.attributes.name,
    email: item.attributes.contact.email
  }
}));
```

### Flatten Arrays
```javascript
// Code node - flatten nested array
const items = $input.all();
const flattened = items.flatMap(item =>
  item.json.results.map(result => ({
    json: {
      parent_id: item.json.id,
      ...result
    }
  }))
);

return flattened;
```

### Combine Multiple API Responses
```
HTTP Request 1 (users)
  → Set (store users)
  → HTTP Request 2 (orders for each user)
  → Merge (combine users + orders)
```

---

## Testing & Debugging

### 1. Test with Manual Trigger
Replace Schedule with Manual Trigger for testing

### 2. Use Postman/Insomnia First
- Test API outside n8n
- Understand response structure
- Verify authentication

### 3. Log Responses
```javascript
// Code node - log for debugging
console.log('API Response:', JSON.stringify($input.first().json, null, 2));
return $input.all();
```

### 4. Check Execution Data
- View node output in n8n UI
- Check headers, body, status code
- Verify data structure

### 5. Use Binary Data Properly
For file downloads:
```javascript
{
  method: "GET",
  url: "https://api.example.com/download/file.pdf",
  responseFormat: "file",  // Important for binary data
  outputPropertyName: "data"
}
```

---

## Performance Optimization

### 1. Parallel Requests
Use **Split In Batches** with multiple items:
```
Set (create array of IDs)
  → Split In Batches (10 items per batch)
  → HTTP Request (processes all 10 in parallel)
  → Loop
```

### 2. Caching
```
IF (check cache exists)
  ├─ [Cache Hit] → Use cached data
  └─ [Cache Miss] → HTTP Request → Store in cache
```

### 3. Conditional Fetching
Only fetch if data changed:
```
HTTP Request (GET with If-Modified-Since header)
  → IF (status === 304)
    └─ Use existing data
  → IF (status === 200)
    └─ Process new data
```

### 4. Batch API Calls
If API supports batch operations:
```javascript
{
  method: "POST",
  url: "https://api.example.com/batch",
  bodyParametersJson: JSON.stringify({
    requests: $json.items.map(item => ({
      method: "GET",
      url: `/users/${item.id}`
    }))
  })
}
```

---

## Common Gotchas

### 1. ❌ Wrong: Hardcoded URLs
```javascript
url: "https://api.example.com/prod/users"
```

### ✅ Correct: Use environment variables
```javascript
url: "={{$env.API_BASE_URL}}/users"
```

### 2. ❌ Wrong: Credentials in parameters
```javascript
headerParameters: {
  "Authorization": "Bearer sk-abc123xyz"  // ❌ Exposed!
}
```

### ✅ Correct: Use credentials system
```javascript
authentication: "predefinedCredentialType",
nodeCredentialType: "httpHeaderAuth"
```

### 3. ❌ Wrong: No error handling
```javascript
HTTP Request → Process (fails if API down)
```

### ✅ Correct: Handle errors
```javascript
HTTP Request (continueOnFail: true) → IF (error) → Handle
```

### 4. ❌ Wrong: Blocking on large responses
Processing 10,000 items synchronously

### ✅ Correct: Use batching
```
Split In Batches (100 items) → Process → Loop
```

---

## Real Template Examples

From n8n template library (892 API integration templates):

**GitHub to Notion**:
```
Schedule → HTTP Request (GitHub API) → Transform → HTTP Request (Notion API)
```

**Weather to Slack**:
```
Schedule → HTTP Request (Weather API) → Set (format) → Slack
```

**CRM Sync**:
```
Schedule → HTTP Request (CRM A) → Transform → HTTP Request (CRM B)
```

Use `search_templates({query: "http api"})` to find more!

---

## Checklist for API Integration

### Planning
- [ ] Test API with Postman/curl first
- [ ] Understand response structure
- [ ] Check rate limits
- [ ] Review authentication method
- [ ] Plan error handling

### Implementation
- [ ] Use credentials (never hardcode)
- [ ] Configure proper HTTP method
- [ ] Set correct headers (Content-Type, Accept)
- [ ] Handle pagination if needed
- [ ] Add query parameters properly

### Error Handling
- [ ] Set continueOnFail: true if needed
- [ ] Check response status codes
- [ ] Implement retry logic
- [ ] Add Error Trigger workflow
- [ ] Alert on failures

### Performance
- [ ] Use batching for large datasets
- [ ] Add rate limiting if needed
- [ ] Consider caching
- [ ] Test with production load

### Security
- [ ] Use HTTPS only
- [ ] Store secrets in credentials
- [ ] Validate API responses
- [ ] Use environment variables

---

## Summary

**Key Points**:
1. **Authentication** via credentials system (never hardcode)
2. **Error handling** is critical (continueOnFail + IF checks)
3. **Pagination** for large datasets
4. **Rate limiting** to respect API limits
5. **Transform responses** to match your needs

**Pattern**: Trigger → HTTP Request → Transform → Action → Error Handler

**Related**:
- [webhook_processing.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/webhook_processing.md) - Receiving HTTP requests
- [database_operations.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/database_operations.md) - Storing API data
```

## File: `skills/n8n-workflow-patterns/scheduled_tasks.md`
```markdown
# Scheduled Tasks Pattern

**Use Case**: Recurring automation workflows that run automatically on a schedule.

---

## Pattern Structure

```
Schedule Trigger → [Fetch Data] → [Process] → [Deliver] → [Log/Notify]
```

**Key Characteristic**: Time-based automated execution

---

## Core Components

### 1. Schedule Trigger
**Purpose**: Execute workflow at specified times

**Modes**:
- **Interval** - Every X minutes/hours/days
- **Cron** - Specific times (advanced)
- **Days & Hours** - Simple recurring schedule

### 2. Data Source
**Common sources**:
- HTTP Request (APIs)
- Database queries
- File reads
- Service-specific nodes

### 3. Processing
**Typical operations**:
- Filter/transform data
- Aggregate statistics
- Generate reports
- Check conditions

### 4. Delivery
**Output channels**:
- Email
- Slack/Discord/Teams
- File storage
- Database writes

### 5. Logging
**Purpose**: Track execution history

**Methods**:
- Database log entries
- File append
- Monitoring service

---

## Schedule Configuration

### Interval Mode
**Best for**: Simple recurring tasks

**Examples**:
```javascript
// Every 15 minutes
{
  mode: "interval",
  interval: 15,
  unit: "minutes"
}

// Every 2 hours
{
  mode: "interval",
  interval: 2,
  unit: "hours"
}

// Every day at midnight
{
  mode: "interval",
  interval: 1,
  unit: "days"
}
```

### Days & Hours Mode
**Best for**: Specific days and times

**Examples**:
```javascript
// Weekdays at 9 AM
{
  mode: "daysAndHours",
  days: ["monday", "tuesday", "wednesday", "thursday", "friday"],
  hour: 9,
  minute: 0
}

// Every Monday at 6 PM
{
  mode: "daysAndHours",
  days: ["monday"],
  hour: 18,
  minute: 0
}
```

### Cron Mode (Advanced)
**Best for**: Complex schedules

**Examples**:
```javascript
// Every weekday at 9 AM
{
  mode: "cron",
  expression: "0 9 * * 1-5"
}

// First day of every month at midnight
{
  mode: "cron",
  expression: "0 0 1 * *"
}

// Every 15 minutes during business hours (9 AM - 5 PM) on weekdays
{
  mode: "cron",
  expression: "*/15 9-17 * * 1-5"
}
```

**Cron format**: `minute hour day month weekday`
- `*` = any value
- `*/15` = every 15 units
- `1-5` = range (Monday-Friday)
- `1,15` = specific values

**Cron examples**:
```
0 */6 * * *      Every 6 hours
0 9,17 * * *     At 9 AM and 5 PM daily
0 0 * * 0        Every Sunday at midnight
*/30 * * * *     Every 30 minutes
0 0 1,15 * *     1st and 15th of each month
```

---

## Common Use Cases

### 1. Daily Reports
**Flow**: Schedule → Fetch data → Aggregate → Format → Email

**Example** (Sales report):
```
1. Schedule (daily at 9 AM)

2. Postgres (query yesterday's sales)
   SELECT date, SUM(amount) as total, COUNT(*) as orders
   FROM orders
   WHERE date = CURRENT_DATE - INTERVAL '1 day'
   GROUP BY date

3. Code (calculate metrics)
   - Total revenue
   - Order count
   - Average order value
   - Comparison to previous day

4. Set (format email body)
   Subject: Daily Sales Report - {{$json.date}}
   Body: Formatted HTML with metrics

5. Email (send to team@company.com)

6. Slack (post summary to #sales)
```

### 2. Data Synchronization
**Flow**: Schedule → Fetch from source → Transform → Write to target

**Example** (CRM to data warehouse sync):
```
1. Schedule (every hour)

2. Set (store last sync time)
   SELECT MAX(synced_at) FROM sync_log

3. HTTP Request (fetch new CRM contacts since last sync)
   GET /api/contacts?updated_since={{$json.last_sync}}

4. IF (check if new records exist)

5. Set (transform CRM schema to warehouse schema)

6. Postgres (warehouse - INSERT new contacts)

7. Postgres (UPDATE sync_log SET synced_at = NOW())

8. IF (error occurred)
   └─ Slack (alert #data-team)
```

### 3. Monitoring & Health Checks
**Flow**: Schedule → Check endpoints → Alert if down

**Example** (Website uptime monitor):
```
1. Schedule (every 5 minutes)

2. HTTP Request (GET https://example.com/health)
   - timeout: 10 seconds
   - continueOnFail: true

3. IF (status !== 200 OR response_time > 2000ms)

4. Redis (check alert cooldown - don't spam)
   - Key: alert:website_down
   - TTL: 30 minutes

5. IF (no recent alert sent)

6. [Alert Actions]
   ├─ Slack (notify #ops-team)
   ├─ PagerDuty (create incident)
   ├─ Email (alert@company.com)
   └─ Redis (set alert cooldown)

7. Postgres (log uptime check result)
```

### 4. Cleanup & Maintenance
**Flow**: Schedule → Find old data → Archive/Delete → Report

**Example** (Database cleanup):
```
1. Schedule (weekly on Sunday at 2 AM)

2. Postgres (find old records)
   SELECT * FROM logs
   WHERE created_at < NOW() - INTERVAL '90 days'
   LIMIT 10000

3. IF (records exist)

4. Code (export to JSON for archive)

5. Google Drive (upload archive file)
   - Filename: logs_archive_{{$now.format('YYYY-MM-DD')}}.json

6. Postgres (DELETE archived records)
   DELETE FROM logs
   WHERE id IN ({{$json.archived_ids}})

7. Slack (report: "Archived X records, deleted Y records")
```

### 5. Data Enrichment
**Flow**: Schedule → Find incomplete records → Enrich → Update

**Example** (Enrich contacts with company data):
```
1. Schedule (nightly at 3 AM)

2. Postgres (find contacts without company data)
   SELECT id, email, domain FROM contacts
   WHERE company_name IS NULL
   AND created_at > NOW() - INTERVAL '7 days'
   LIMIT 100

3. Split In Batches (10 contacts per batch)

4. HTTP Request (call Clearbit enrichment API)
   - For each contact domain
   - Rate limit: wait 1 second between batches

5. Set (map API response to database schema)

6. Postgres (UPDATE contacts with company data)

7. Wait (1 second - rate limiting)

8. Loop (back to step 4 until all batches processed)

9. Email (summary: "Enriched X contacts")
```

### 6. Backup Automation
**Flow**: Schedule → Export data → Compress → Store → Verify

**Example** (Database backup):
```
1. Schedule (daily at 2 AM)

2. Code (execute pg_dump)
   const { exec } = require('child_process');
   exec('pg_dump -h db.example.com mydb > backup.sql')

3. Code (compress backup)
   const zlib = require('zlib');
   // Compress backup.sql to backup.sql.gz

4. AWS S3 (upload compressed backup)
   - Bucket: backups
   - Key: db/backup-{{$now.format('YYYY-MM-DD')}}.sql.gz

5. AWS S3 (list old backups)
   - Keep last 30 days only

6. AWS S3 (delete old backups)

7. IF (error occurred)
   ├─ PagerDuty (critical alert)
   └─ Email (backup failed!)
   ELSE
   └─ Slack (#devops: "✅ Backup completed")
```

### 7. Content Publishing
**Flow**: Schedule → Fetch content → Format → Publish

**Example** (Automated social media posts):
```
1. Schedule (every 3 hours during business hours)
   - Cron: 0 9,12,15,18 * * 1-5

2. Google Sheets (read content queue)
   - Sheet: "Scheduled Posts"
   - Filter: status=pending AND publish_time <= NOW()

3. IF (posts available)

4. HTTP Request (shorten URLs in post)

5. HTTP Request (POST to Twitter API)

6. HTTP Request (POST to LinkedIn API)

7. Google Sheets (update status=published)

8. Slack (notify #marketing: "Posted: {{$json.title}}")
```

---

## Timezone Considerations

### Set Workflow Timezone
```javascript
// In workflow settings
{
  timezone: "America/New_York"  // EST/EDT
}
```

### Common Timezones
```
America/New_York    - Eastern (US)
America/Chicago     - Central (US)
America/Denver      - Mountain (US)
America/Los_Angeles - Pacific (US)
Europe/London       - GMT/BST
Europe/Paris        - CET/CEST
Asia/Tokyo          - JST
Australia/Sydney    - AEDT
UTC                 - Universal Time
```

### Handle Daylight Saving
**Best practice**: Use timezone-aware scheduling

```javascript
// ❌ Bad: UTC schedule for "9 AM local"
// Will be off by 1 hour during DST transitions

// ✅ Good: Set workflow timezone
{
  timezone: "America/New_York",
  schedule: {
    mode: "daysAndHours",
    hour: 9  // Always 9 AM Eastern, regardless of DST
  }
}
```

---

## Error Handling

### Pattern 1: Error Trigger Workflow
**Main workflow**: Normal execution
**Error workflow**: Alerts and recovery

**Main**:
```
Schedule → Fetch → Process → Deliver
```

**Error**:
```
Error Trigger (for main workflow)
  → Set (extract error details)
  → Slack (#ops-team: "❌ Scheduled job failed")
  → Email (admin alert)
  → Postgres (log error for analysis)
```

### Pattern 2: Retry with Backoff
```
Schedule → HTTP Request (continueOnFail: true)
  → IF (error)
    ├─ Wait (5 minutes)
    ├─ HTTP Request (retry 1)
    └─ IF (still error)
      ├─ Wait (15 minutes)
      ├─ HTTP Request (retry 2)
      └─ IF (still error)
        └─ Alert admin
```

### Pattern 3: Partial Failure Handling
```
Schedule → Split In Batches
  → Process (continueOnFail: true)
  → Code (track successes and failures)
  → Report:
    "✅ Processed: 95/100"
    "❌ Failed: 5/100"
```

---

## Performance Optimization

### 1. Batch Processing
For large datasets:

```
Schedule → Query (LIMIT 10000)
  → Split In Batches (100 items)
  → Process batch
  → Loop
```

### 2. Parallel Processing
When operations are independent:

```
Schedule
  ├─ [Branch 1: Update DB]
  ├─ [Branch 2: Send emails]
  └─ [Branch 3: Generate report]
  → Merge (wait for all) → Final notification
```

### 3. Skip if Already Running
Prevent overlapping executions:

```
Schedule → Redis (check lock)
  → IF (lock exists)
    └─ End (skip this execution)
  → ELSE
    ├─ Redis (set lock, TTL 30 min)
    ├─ [Execute workflow]
    └─ Redis (delete lock)
```

### 4. Early Exit on No Data
Don't waste time if nothing to process:

```
Schedule → Query (check if work exists)
  → IF (no results)
    └─ End workflow (exit early)
  → ELSE
    └─ Process data
```

---

## Monitoring & Logging

### Pattern 1: Execution Log Table
```sql
CREATE TABLE workflow_executions (
  id SERIAL PRIMARY KEY,
  workflow_name VARCHAR(255),
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  status VARCHAR(50),
  records_processed INT,
  error_message TEXT
);
```

**Log execution**:
```
Schedule
  → Set (record start)
  → [Workflow logic]
  → Postgres (INSERT execution log)
```

### Pattern 2: Metrics Collection
```
Schedule → [Execute]
  → Code (calculate metrics)
    - Duration
    - Records processed
    - Success rate
  → HTTP Request (send to monitoring system)
    - Datadog, Prometheus, etc.
```

### Pattern 3: Summary Notifications
Daily/weekly execution summaries:

```
Schedule (daily at 6 PM) → Query execution logs
  → Code (aggregate today's executions)
  → Email (summary report)
    "Today's Workflow Executions:
     - 24/24 successful
     - 0 failures
     - Avg duration: 2.3 min"
```

---

## Testing Scheduled Workflows

### 1. Use Manual Trigger for Testing
**Development pattern**:
```
Manual Trigger (for testing)
  → [Same workflow logic]
  → [Outputs]

// Once tested, replace with Schedule Trigger
```

### 2. Test with Different Times
```javascript
// Code node - simulate different times
const testTime = new Date('2024-01-15T09:00:00Z');
return [{ json: { currentTime: testTime } }];
```

### 3. Dry Run Mode
```
Schedule → Set (dryRun: true)
  → IF (dryRun)
    └─ Log what would happen (don't execute)
  → ELSE
    └─ Execute normally
```

### 4. Shorter Interval for Testing
```javascript
// Testing: every 1 minute
{
  mode: "interval",
  interval: 1,
  unit: "minutes"
}

// Production: every 1 hour
{
  mode: "interval",
  interval: 1,
  unit: "hours"
}
```

---

## Common Gotchas

### 1. ❌ Wrong: Ignoring timezone
```javascript
Schedule (9 AM)  // 9 AM in which timezone?
```

### ✅ Correct: Set workflow timezone
```javascript
// Workflow settings
{
  timezone: "America/New_York"
}
```

### 2. ❌ Wrong: Overlapping executions
```
Schedule (every 5 min) → Long-running task (10 min)
// Two executions running simultaneously!
```

### ✅ Correct: Add execution lock
```
Schedule → Redis (check lock)
  → IF (locked) → Skip
  → ELSE → Execute
```

### 3. ❌ Wrong: No error handling
```
Schedule → API call → Process (fails silently)
```

### ✅ Correct: Add error workflow
```
Main: Schedule → Execute
Error: Error Trigger → Alert
```

### 4. ❌ Wrong: Processing all data at once
```
Schedule → SELECT 1000000 records → Process (OOM)
```

### ✅ Correct: Batch processing
```
Schedule → SELECT with pagination → Split In Batches → Process
```

### 5. ❌ Wrong: Hardcoded dates
```javascript
query: "SELECT * FROM orders WHERE date = '2024-01-15'"
```

### ✅ Correct: Dynamic dates
```javascript
query: "SELECT * FROM orders WHERE date = CURRENT_DATE - INTERVAL '1 day'"
```

---

## Real Template Examples

From n8n template library:

**Template #2947** (Weather to Slack):
```
Schedule (daily 8 AM)
  → HTTP Request (weather API)
  → Set (format message)
  → Slack (post to #general)
```

**Daily backup**:
```
Schedule (nightly 2 AM)
  → Postgres (export data)
  → Google Drive (upload)
  → Email (confirmation)
```

**Monitoring**:
```
Schedule (every 5 min)
  → HTTP Request (health check)
  → IF (down) → PagerDuty alert
```

Use `search_templates({query: "schedule"})` to find more!

---

## Checklist for Scheduled Workflows

### Planning
- [ ] Define schedule frequency (interval, cron, days & hours)
- [ ] Set workflow timezone
- [ ] Estimate execution duration
- [ ] Plan for failures and retries
- [ ] Consider timezone and DST

### Implementation
- [ ] Configure Schedule Trigger
- [ ] Set workflow timezone in settings
- [ ] Add early exit for no-op cases
- [ ] Implement batch processing for large data
- [ ] Add execution logging

### Error Handling
- [ ] Create Error Trigger workflow
- [ ] Implement retry logic
- [ ] Add alert notifications
- [ ] Log errors for analysis
- [ ] Handle partial failures gracefully

### Monitoring
- [ ] Log each execution (start, end, status)
- [ ] Track metrics (duration, records, success rate)
- [ ] Set up daily/weekly summaries
- [ ] Alert on consecutive failures
- [ ] Monitor resource usage

### Testing
- [ ] Test with Manual Trigger first
- [ ] Verify timezone behavior
- [ ] Test error scenarios
- [ ] Check for overlapping executions
- [ ] Validate output quality

### Deployment
- [ ] Document workflow purpose
- [ ] Set up monitoring
- [ ] Configure alerts
- [ ] Activate workflow in n8n UI ⚠️ **Manual activation required** (API/MCP cannot activate)
- [ ] Test in production (short interval first)
- [ ] Monitor first few executions

---

## Advanced Patterns

### Dynamic Scheduling
**Change schedule based on conditions**:

```
Schedule (check every hour) → Code (check if it's time to run)
  → IF (business hours AND weekday)
    └─ Execute workflow
  → ELSE
    └─ Skip
```

### Dependent Schedules
**Chain workflows**:

```
Workflow A (daily 2 AM): Data sync
  → On completion → Trigger Workflow B

Workflow B: Generate report (depends on fresh data)
```

### Conditional Execution
**Skip based on external factors**:

```
Schedule → HTTP Request (check feature flag)
  → IF (feature enabled)
    └─ Execute
  → ELSE
    └─ Skip
```

---

## Summary

**Key Points**:
1. **Set workflow timezone** explicitly
2. **Batch processing** for large datasets
3. **Error handling** is critical (Error Trigger + retries)
4. **Prevent overlaps** with execution locks
5. **Monitor and log** all executions

**Pattern**: Schedule → Fetch → Process → Deliver → Log

**Schedule Modes**:
- **Interval**: Simple recurring (every X minutes/hours)
- **Days & Hours**: Specific days and times
- **Cron**: Advanced complex schedules

**Related**:
- [http_api_integration.md](http_api_integration.md) - Fetching data on schedule
- [database_operations.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/database_operations.md) - Scheduled database tasks
- [webhook_processing.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/workflow_automation/n8n/n8n_workflow_patterns/webhook_processing.md) - Alternative to scheduling
```

## File: `skills/n8n-workflow-patterns/webhook_processing.md`
```markdown
# Webhook Processing Pattern

**Use Case**: Receive HTTP requests from external systems and process them instantly.

---

## Pattern Structure

```
Webhook → [Validate] → [Transform] → [Action] → [Response/Notify]
```

**Key Characteristic**: Instant event-driven processing

---

## Core Components

### 1. Webhook Node (Trigger)
**Purpose**: Create HTTP endpoint to receive data

**Configuration**:
```javascript
{
  path: "form-submit",        // URL path: https://n8n.example.com/webhook/form-submit
  httpMethod: "POST",         // GET, POST, PUT, DELETE
  responseMode: "onReceived", // or "lastNode" for custom response
  responseData: "allEntries"  // or "firstEntryJson"
}
```

**Critical Gotcha**: Data is nested under `$json.body`
```javascript
❌ {{$json.email}}
✅ {{$json.body.email}}
```

### 2. Validation (Optional but Recommended)
**Purpose**: Verify incoming data before processing

**Options**:
- **IF node** - Check required fields exist
- **Code node** - Custom validation logic
- **Stop and Error** - Fail gracefully with message

**Example**:
```javascript
// IF node condition
{{$json.body.email}} is not empty AND
{{$json.body.name}} is not empty
```

### 3. Transformation
**Purpose**: Map webhook data to desired format

**Typical nodes**:
- **Set** - Field mapping
- **Code** - Complex transformations

**Example** (Set node):
```javascript
{
  "user_email": "={{$json.body.email}}",
  "user_name": "={{$json.body.name}}",
  "timestamp": "={{$now}}"
}
```

### 4. Action
**Purpose**: Do something with the data

**Common actions**:
- Store in database (Postgres, MySQL, MongoDB)
- Send notification (Slack, Email, Discord)
- Call another API (HTTP Request)
- Update external system (CRM, support ticket)

### 5. Response (If responseMode: "lastNode")
**Purpose**: Send custom HTTP response

**Webhook Response Node**:
```javascript
{
  statusCode: 200,
  headers: {
    "Content-Type": "application/json"
  },
  body: {
    "status": "success",
    "message": "Form received"
  }
}
```

---

## Common Use Cases

### 1. Form Submissions
**Flow**: Form → Webhook → Validate → Database → Email Confirmation

**Example**:
```
1. Webhook (path: "contact-form", POST)
2. IF (check email & message not empty)
3. Postgres (insert into contacts table)
4. Email (send confirmation to user)
5. Slack (notify team in #leads)
6. Webhook Response ({"status": "success"})
```

**Real Data Access**:
```javascript
Name: {{$json.body.name}}
Email: {{$json.body.email}}
Message: {{$json.body.message}}
```

### 2. Payment Webhooks (Stripe, PayPal)
**Flow**: Payment Provider → Webhook → Verify → Update Database → Send Receipt

**Security**: Verify webhook signatures
```javascript
// Code node - verify Stripe signature
const crypto = require('crypto');
const signature = $input.item.headers['stripe-signature'];
const secret = $credentials.stripeWebhookSecret;

// Verify signature matches
const expectedSig = crypto
  .createHmac('sha256', secret)
  .update($input.item.body)
  .digest('hex');

if (signature !== expectedSig) {
  throw new Error('Invalid webhook signature');
}

return $input.item.body; // Return validated body
```

### 3. Chat Platform Integrations (Slack, Discord, Teams)
**Flow**: Chat Command → Webhook → Process → Respond

**Example** (Slack slash command):
```
1. Webhook (path: "slack-command", POST)
2. Code (parse Slack payload: $json.body.text, $json.body.user_id)
3. HTTP Request (fetch data from API)
4. Set (format Slack message)
5. Webhook Response (immediate Slack response)
```

**Slack Data Access**:
```javascript
Command: {{$json.body.command}}
Text: {{$json.body.text}}
User ID: {{$json.body.user_id}}
Channel ID: {{$json.body.channel_id}}
```

### 4. GitHub/GitLab Webhooks
**Flow**: Git Event → Webhook → Parse → Notify/Deploy

**Example** (new PR notification):
```
1. Webhook (path: "github", POST)
2. IF (check $json.body.action equals "opened")
3. Set (extract PR details: title, author, url)
4. Slack (notify #dev-team)
5. Webhook Response (200 OK)
```

**GitHub Data Access**:
```javascript
Event Type: {{$json.headers['x-github-event']}}
Action: {{$json.body.action}}
PR Title: {{$json.body.pull_request.title}}
Author: {{$json.body.pull_request.user.login}}
URL: {{$json.body.pull_request.html_url}}
```

### 5. IoT Device Data
**Flow**: Device → Webhook → Validate → Store → Alert (if threshold)

**Example** (temperature sensor):
```
1. Webhook (path: "sensor-data", POST)
2. Set (extract sensor readings)
3. Postgres (insert into sensor_readings)
4. IF (temperature > 80)
5. Email (alert admin)
```

---

## Webhook Data Structure

### Standard Structure
```json
{
  "headers": {
    "content-type": "application/json",
    "user-agent": "...",
    "x-custom-header": "..."
  },
  "params": {
    "id": "123"  // From URL: /webhook/form/:id
  },
  "query": {
    "token": "abc"  // From URL: /webhook/form?token=abc
  },
  "body": {
    // ⚠️ YOUR DATA IS HERE!
    "name": "John",
    "email": "john@example.com"
  }
}
```

### Accessing Different Parts
```javascript
// Headers
{{$json.headers['content-type']}}
{{$json.headers['x-api-key']}}

// URL Parameters
{{$json.params.id}}

// Query Parameters
{{$json.query.token}}
{{$json.query.page}}

// Body (MOST COMMON)
{{$json.body.email}}
{{$json.body.user.name}}
{{$json.body.items[0].price}}
```

---

## Authentication & Security

### 1. Query Parameter Token
**Simple but less secure**
```javascript
// IF node - validate token
{{$json.query.token}} equals "your-secret-token"
```

### 2. Header-Based Auth
**Better security**
```javascript
// IF node - check header
{{$json.headers['x-api-key']}} equals "your-api-key"
```

### 3. Signature Verification
**Best security** (for webhooks from services like Stripe, GitHub)
```javascript
// Code node
const crypto = require('crypto');
const signature = $input.item.headers['x-signature'];
const secret = $credentials.webhookSecret;

const calculatedSig = crypto
  .createHmac('sha256', secret)
  .update(JSON.stringify($input.item.body))
  .digest('hex');

if (signature !== `sha256=${calculatedSig}`) {
  throw new Error('Invalid signature');
}

return $input.item.body;
```

### 4. IP Whitelist
**Restrict access by IP** (n8n workflow settings)
- Configure in workflow settings
- Only allow specific IP ranges
- Use for internal systems

---

## Response Modes

### onReceived (Default)
**Behavior**: Immediate 200 OK response, workflow continues in background

**Use when**:
- Long-running workflows
- Response doesn't depend on workflow result
- Fire-and-forget processing

**Configuration**:
```javascript
{
  responseMode: "onReceived",
  responseCode: 200
}
```

### lastNode (Custom Response)
**Behavior**: Wait for workflow completion, send custom response

**Use when**:
- Need to return data to caller
- Synchronous processing required
- Form submissions with confirmation

**Configuration**:
```javascript
{
  responseMode: "lastNode"
}
```

**Then add Webhook Response node**:
```javascript
{
  statusCode: 200,
  headers: {
    "Content-Type": "application/json"
  },
  body: {
    "id": "={{$json.record_id}}",
    "status": "success"
  }
}
```

---

## Error Handling

### Pattern 1: Try-Catch with Error Trigger
```
Main Flow:
  Webhook → [nodes...] → Success Response

Error Flow:
  Error Trigger → Log Error → Slack Alert → Error Response
```

**Error Trigger Configuration**:
```javascript
{
  workflowId: "current-workflow-id"
}
```

**Error Response** (if responseMode: "lastNode"):
```javascript
{
  statusCode: 500,
  body: {
    "status": "error",
    "message": "Processing failed"
  }
}
```

### Pattern 2: Validation Early Exit
```
Webhook → IF (validate) → [True: Process]
                       └→ [False: Error Response]
```

**False Branch Response**:
```javascript
{
  statusCode: 400,
  body: {
    "status": "error",
    "message": "Invalid data: missing email"
  }
}
```

### Pattern 3: Continue On Fail
**Per-node setting**: Continue even if node fails

**Use case**: Non-critical notifications
```
Webhook → Database (critical) → Slack (continueOnFail: true)
```

---

## Testing Webhooks

### 1. Use Manual Trigger
Replace Webhook with Manual Trigger for testing:
```
Manual Trigger → [set test data] → rest of workflow
```

### 2. Use curl
```bash
curl -X POST https://n8n.example.com/webhook/form-submit \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "name": "Test User"}'
```

### 3. Use Postman/Insomnia
- Create request collection
- Test different payloads
- Verify responses

### 4. Webhook.site
- Use webhook.site for testing
- Copy webhook.site URL to your service
- View requests and debug

---

## Performance Considerations

### Large Payloads
- Webhook timeout: 120 seconds (default)
- For large data, consider async processing:
  ```
  Webhook → Queue (Redis/DB) → Response (immediate)

  Separate Workflow:
  Schedule → Check Queue → Process
  ```

### High Volume
- Use "Execute Once" mode if processing all items together
- Consider rate limiting
- Monitor execution times
- Scale n8n instance if needed

### Retries
- Webhook calls typically don't retry automatically
- Implement retry logic on caller side
- Or use queue pattern for guaranteed processing

---

## Common Gotchas

### 1. ❌ Wrong: Accessing webhook data
```javascript
{{$json.email}}  // Empty or undefined
```

### ✅ Correct
```javascript
{{$json.body.email}}  // Data is under .body
```

### 2. ❌ Wrong: Response mode confusion
Using Webhook Response node with responseMode: "onReceived" (ignored)

### ✅ Correct
Set responseMode: "lastNode" to use Webhook Response node

### 3. ❌ Wrong: No validation
Assuming data is always present and valid

### ✅ Correct
Validate data early with IF node or Code node

### 4. ❌ Wrong: Hardcoded paths
Using same path for dev/prod

### ✅ Correct
Use environment variables: `{{$env.WEBHOOK_PATH_PREFIX}}/form-submit`

---

## Real Template Examples

From n8n template library (1,085 webhook templates):

**Simple Form to Slack**:
```
Webhook → Set → Slack
```

**Payment Processing**:
```
Webhook → Verify Signature → Update Database → Send Receipt → Notify Admin
```

**Chat Bot**:
```
Webhook → Parse Command → AI Agent → Format Response → Webhook Response
```

Use `search_templates({query: "webhook"})` to find more!

---

## Checklist for Webhook Workflows

### Setup
- [ ] Choose descriptive webhook path
- [ ] Configure HTTP method (POST most common)
- [ ] Choose response mode (onReceived vs lastNode)
- [ ] Test webhook URL before connecting services

### Security
- [ ] Add authentication (token, signature, IP whitelist)
- [ ] Validate incoming data
- [ ] Sanitize user input (if storing/displaying)
- [ ] Use HTTPS (always)

### Data Handling
- [ ] Remember data is under $json.body
- [ ] Handle missing fields gracefully
- [ ] Transform data to desired format
- [ ] Log important data (for debugging)

### Error Handling
- [ ] Add Error Trigger workflow
- [ ] Validate required fields
- [ ] Return appropriate error responses
- [ ] Alert team on failures

### Testing
- [ ] Test with curl/Postman
- [ ] Test error scenarios
- [ ] Verify response format
- [ ] Monitor first executions

---

## Summary

**Key Points**:
1. **Data under $json.body** (most common mistake!)
2. **Validate early** to catch bad data
3. **Choose response mode** based on use case
4. **Secure webhooks** with auth
5. **Handle errors** gracefully

**Pattern**: Webhook → Validate → Transform → Action → Response

**Related**:
- [n8n Expression Syntax](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) - Accessing webhook data correctly
- [http_api_integration.md](http_api_integration.md) - Making HTTP requests in response
```

