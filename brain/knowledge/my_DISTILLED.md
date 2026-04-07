---
id: my
type: knowledge
owner: OA_Triage
---
# my
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
[![GitHub stars](https://img.shields.io/github/stars/centminmod/my-claude-code-setup.svg?style=flat-square)](https://github.com/centminmod/my-claude-code-setup/stargazers) [![GitHub forks](https://img.shields.io/github/forks/centminmod/my-claude-code-setup.svg?style=flat-square)](https://github.com/centminmod/my-claude-code-setup/network) [![GitHub issues](https://img.shields.io/github/issues/centminmod/my-claude-code-setup.svg?style=flat-square)](https://github.com/centminmod/my-claude-code-setup/issues)

* Threads - https://www.threads.com/@george_sl_liu
* BlueSky - https://bsky.app/profile/georgesl.bsky.social

# My Claude Code Project's Starter Settings

## Alternate Read Me Guides

The beauty of using AI is that I can get AI to generate alternate Read Me guides using different formats and styles to suit different readers and learners. So I asked Claude Code to generate alternate Read Me guides in different styles - pick one that suits you best or read all of them to get a better understanding of how to use this project.

* [README.md](README.md) - Original written version I did myself below
* [README-v2.md](README-v2.md) - Progressive Disclosure Guide (Beginner → Intermediate → Advanced sections)
* [README-v3.md](README-v3.md) - Task-Based Guide ("I want to..." navigation for goal-oriented users)
* [README-v4.md](README-v4.md) - Technical Reference Manual (Chapter-based, dense reference format) 

## Overview

My Claude Code project's starter settings and Claude Code hooks and slash commands are provided in this repository for users to try out. The [CLAUDE.md](https://github.com/centminmod/my-claude-code-setup/blob/master/CLAUDE.md) is setup as set of memory bank files to better retain context over many chat sessions. Be sure to read the official Claude Code docs first at <https://docs.anthropic.com/en/docs/claude-code/overview> and sign up for a [paid Claude AI account](https://claude.ai/) to use Claude Code. You can pay for Claude Pro $20/month, Claude Max $100/month or Claude Max $200/month. The paid Claude tier plans will include varying quotas for usage and rate limits outlined [here](https://support.anthropic.com/en/articles/9797557-usage-limit-best-practices). You can also use Claude Code with [Z.AI](#using-zai-with-claude-code) to get higher token usage quotas and get access to Z.AI GLM-4.7 LLM models within Claude Code. Use [Z.AI invite code for additional 10% discount](https://z.ai/subscribe?ic=WWB8IFLROM) which can stack with current 50-60% yearly discounts.

1. Copy the files in this Github repo to your project directory (where you intended codebase will be).
2. Modify the template files and CLAUDE.md`to your liking. `.claude/settings.json` needs to install Terminal-Notifier for macOS https://github.com/centminmod/terminal-notifier-setup. If you're not using macOS, you can remove `.claude/settings.json`.
3. After launching Claude Code for the first time within your project directory, run `/init` so that Claude Code analyses your code base and then populates your memory bank system files as per CLAUDE.md` instructions.
4. Optional step highly recommended: Install Visual Studio Code ([beginners YouTube video guide](https://www.youtube.com/watch?v=rPITZvwyoMc) and [here](https://www.youtube.com/watch?v=P-5bWpUbO60)) and [Claude Code VSC Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code).
5. Optional step highly recommended: Sign up for [Github.com](https://github.com/) account and install Git for Visual Studio Code. Checkout YouTube guides [here](https://www.youtube.com/watch?v=twsYxYaQikI) and [here](https://www.youtube.com/watch?v=z5jZ9lrSpqk).
6. CLAUDE.md updated to instruct models to use faster tools so for macOS: `brew install ripgrep fd jq`
7. Optional step to setup Claude Code, Codex GPT-5, Gemini CLI, OpenCode, Vercel CLI, Cloudflare Wrangler, Amazon AWS CLI, all in a single isolated [Visual Studio Code dev container running Debian 12](https://claude-devcontainers.centminmod.com/). Allowing you to run YOLO modes for Claude Code with `dangerously_skip_permissions` enabled and Codex CLI with `sandbox_mode = danger-full-access` etc.
8. Claude Code via Claude Desktop apps use Git Worktrees. You may need to create a `.worktreeinclude` file as outlined [here](https://code.claude.com/docs/en/desktop#claude-code-on-desktop-preview).
9. If you use Cloudflare and ClerkOS platforms in your apps, you can keep either `CLAUDE-cloudflare.md` or `CLAUDE-cloudflare-mini.md` supplementary reference docs and update `CLAUDE.md` referencing either file to help AI understand Cloudflare and ClerkOS platforum documentation and products. Edit documentation templates as needed i.e. if you do not use ClerkOS platform, you can remove those sections.
10. If you use Convex database in your apps, you can use `CLAUDE-convex.md` supplementary reference docs for building Next.js and React apps with Convex backend deployed on Cloudflare Pages.
11. Useful read [Advent of Claude: 31 Days of Claude Code by Ado Kukic from Anthropic](https://adocomplete.com/advent-of-claude-2025/).
12. Useful [Claude Code with Claude Opus 4.5 YouTube video by Alex Finn](https://www.youtube.com/watch?v=UVJXh57MgI0) and [Claude Code YouTube video by Matt Maher](https://www.youtube.com/watch?v=Dekx_OzRwiI).
13. Configure Claude Code with [Z.AI](#using-zai-with-claude-code) to get higher token usage quotas and get access to Z.AI GLM-4.7 LLM models within Claude Code.
14. For folks intending to use Claude LLM models with OpenClaw, read this first for security, deployment and cost optimizations https://github.com/centminmod/explain-openclaw.

## CLAUDE.md Memory Bank system

[CLAUDE.md](https://github.com/centminmod/my-claude-code-setup/blob/master/CLAUDE.md) uses a memory bank system of files for Claude Code to better retain context over many chat sessions. Example of Claude Code thinking output when I ask it to `update memory bank` after a successful task completion and git commit:

```
> update memory bank

∴ Thinking…

  The user wants me to update the memory bank files. I should update the relevant CLAUDE-*.md files to reflect the v0.1.6 changes and current state. Let me check
   which memory bank files exist and update them.

∴ Thinking…

  I need to continue updating the memory bank files. I'll update:
  1. CLAUDE-patterns.md - Add export path handling pattern (Pattern 22)
  2. CLAUDE-decisions.md - Add ADR-017 for Phoneme API migration and ADR-018 for export path handling
  3. CLAUDE-troubleshooting.md - Add new issues and solutions for v0.1.6

∴ Thinking…

  The memory bank files have been modified but not committed. The v0.1.6 release was already committed and tagged, but the memory bank documentation updates are
  still uncommitted. Let me provide a summary of the completed work and offer to commit these documentation changes.

⏺ Summary: v0.1.6 Release Complete ✅

  Memory Bank Updates Complete:
  - CLAUDE-activeContext.md - v0.1.6 session context
  - CLAUDE-patterns.md - Added patterns 22-24 (Export Path, Format Detection, API Migration)
  - CLAUDE-decisions.md - Added ADR-017 & ADR-018
  - CLAUDE-troubleshooting.md - Added 4 new issue/fix entries

  v0.1.6 Fixes Applied:
  1. Export to absolute paths (e.g., --export /tmp/test.wav)
  2. Format detection from filename extension (prevents .mp3.wav)
  3. Phoneme API migrated to /dev/phonemize
  4. Test scripts updated for --export "" syntax

  Test Results: All 29 tests passing

  The memory bank documentation updates are ready to commit. Would you like me to commit them
```

## MCP Servers

I also install the following MCP servers ([install commands](#claude-code-mcp-servers)):

* [Gemini CLI MCP](https://github.com/centminmod/gemini-cli-mcp-server)
* [Cloudflare Documentation MCP](https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/docs-vectorize)
* [Context 7 MCP](https://github.com/upstash/context7)
* [Chrome Devtools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)
* [Notion MCP](https://github.com/makenotion/notion-mcp-server)
* [Claude Code Usage Metrics MCP](https://github.com/centminmod/claude-code-opentelemetry-setup)

## Claude Code Plugin Marketplace

Browser and install Claude Code plugins from official marketplace https://code.claude.com/docs/en/discover-plugins.

```bash
/plugin install plugin-name@claude-plugins-official
```

To update official Claude Code plugin marketplace:

```bash
/plugin marketplace update claude-plugins-official
```

Install [code simplifier plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier).

> Agent that simplifies and refines code for clarity, consistency, and maintainability while preserving functionality. Focuses on recently modified code.

```bash
/plugin install code-simplifier
```

Install [frontend design plugin](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design).

> Create distinctive, production-grade frontend interfaces with high design quality. Generates creative, polished code that avoids generic AI aesthetics.

```bash
/plugin install frontend-design@claude-code-plugins
```

Install [feature dev plugin](https://github.com/anthropics/claude-code/tree/main/plugins/feature-dev).

> The Feature Development Plugin provides a systematic 7-phase approach to building new features. Instead of jumping straight into code, it guides you through understanding the codebase, asking clarifying questions, designing architecture, and ensuring quality—resulting in better-designed features that integrate seamlessly with your existing code.

```bash
/plugin install feature-dev@claude-code-plugins
```

Install [Ralph Wiggum plugin](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum). Details https://paddo.dev/blog/ralph-wiggum-autonomous-loops/. Update: currently seems broken on some systems.

- https://github.com/anthropics/claude-code/issues/16398
- https://github.com/anthropics/claude-code/issues/16389

> Interactive self-referential AI loops for iterative development. Claude works on the same task repeatedly, seeing its previous work, until completion.

```bash
/plugin install ralph-wiggum@claude-code-plugins
```

How to use Ralph Wiggum plugin YouTube by Greg Isenberg and Ryan Carson https://www.youtube.com/watch?v=RpvQH0r0ecM and GitHub repo https://github.com/snarktank/ralph.

## Claude Code 3rd Party Marketplaces

Claude Code Safety Net plugin https://github.com/kenryu42/claude-code-safety-net to prevent destructive commands being run by Claude Code i.e. https://www.reddit.com/r/ClaudeAI/comments/1pgxckk/claude_cli_deleted_my_entire_home_directory_wiped/

> A Claude Code plugin that acts as a safety net, catching destructive git and filesystem commands before they execute.

```bash
/plugin marketplace add kenryu42/cc-marketplace
/plugin install safety-net@cc-marketplace
```

[Z.AI usage query plugin](https://docs.z.ai/devpack/extension/usage-query-plugin) for querying [Z.AI](#using-zai-with-claude-code) usage statistics.

> Query your current quota and usage statistics for the GLM Coding Plan directly within Claude Code.

```bash
/plugin marketplace add zai/zai-coding-plugins
/plugin install glm-plan-usage@zai-coding-plugins
```

[Cloudflare Skills marketplace](https://github.com/cloudflare/skills) for building applications on Cloudflare's platform, Workers, and the Agents SDK.

> Collection of Agent Skills providing accurate, up-to-date guidance for Cloudflare development tasks including Workers, Pages, AI services, and infrastructure.

```bash
/plugin marketplace add cloudflare/skills
```

**User commands**: `/cloudflare:build-agent`, `/cloudflare:build-mcp`

## Claude Code Statuslines

`~/.claude/statuslines/statusline.sh` configured in `~/.claude/settings.json`.

for `~/.claude/settings.json`

```bash
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statuslines/statusline.sh",
    "padding": 0
  },
```

for `~/.claude/statuslines/statusline.sh`

```bash
#!/bin/bash
# Read JSON input from stdin
input=$(cat)

# Extract model and workspace values
MODEL_DISPLAY=$(echo "$input" | jq -r '.model.display_name')
CURRENT_DIR=$(echo "$input" | jq -r '.workspace.current_dir')

# Extract context window metrics
INPUT_TOKENS=$(echo "$input" | jq -r '.context_window.total_input_tokens')
OUTPUT_TOKENS=$(echo "$input" | jq -r '.context_window.total_output_tokens')
CONTEXT_SIZE=$(echo "$input" | jq -r '.context_window.context_window_size')

# Extract cost metrics
COST_USD=$(echo "$input" | jq -r '.cost.total_cost_usd')
LINES_ADDED=$(echo "$input" | jq -r '.cost.total_lines_added')
LINES_REMOVED=$(echo "$input" | jq -r '.cost.total_lines_removed')

# Extract percentage metrics
USED_PERCENTAGE=$(echo "$input" | jq -r '.context_window.used_percentage')
REMAINING_PERCENTAGE=$(echo "$input" | jq -r '.context_window.remaining_percentage')

# Format tokens as Xk
format_tokens() {
    local num="$1"
    if [ "$num" -ge 1000 ]; then
        echo "$((num / 1000))k"
    else
        echo "$num"
    fi
}

# Generate progress bar for context usage
generate_progress_bar() {
    local percentage=$1
    local bar_width=20
    local filled=$(awk "BEGIN {printf \"%.0f\", ($percentage / 100) * $bar_width}")
    local empty=$((bar_width - filled))
    local bar=""
    for ((i=0; i<filled; i++)); do bar+="█"; done
    for ((i=0; i<empty; i++)); do bar+="░"; done
    echo "$bar"
}

# Calculate total
TOTAL_TOKENS=$((INPUT_TOKENS + OUTPUT_TOKENS))

# Generate progress bar
PROGRESS_BAR=$(generate_progress_bar "$USED_PERCENTAGE")

# Show git branch if in a git repo
GIT_BRANCH=""
if git -C "$CURRENT_DIR" rev-parse --git-dir > /dev/null 2>&1; then
    BRANCH=$(git -C "$CURRENT_DIR" branch --show-current 2>/dev/null)
    if [ -n "$BRANCH" ]; then
        # Worktree detection
        GIT_DIR=$(git -C "$CURRENT_DIR" rev-parse --git-dir 2>/dev/null)
        WORKTREE=""
        if [[ "$GIT_DIR" == *".git/worktrees/"* ]] || [[ -f "$GIT_DIR/gitdir" ]]; then
            WORKTREE=" 🌳"
        fi
        # Ahead/behind detection
        AHEAD_BEHIND=""
        UPSTREAM=$(git -C "$CURRENT_DIR" rev-parse --abbrev-ref '@{u}' 2>/dev/null)
        if [ -n "$UPSTREAM" ]; then
            AHEAD=$(git -C "$CURRENT_DIR" rev-list --count '@{u}..HEAD' 2>/dev/null || echo 0)
            BEHIND=$(git -C "$CURRENT_DIR" rev-list --count 'HEAD..@{u}' 2>/dev/null || echo 0)
            if [ "$AHEAD" -gt 0 ] && [ "$BEHIND" -gt 0 ]; then
                AHEAD_BEHIND=" ↕${AHEAD}/${BEHIND}"
            elif [ "$AHEAD" -gt 0 ]; then
                AHEAD_BEHIND=" ↑${AHEAD}"
            elif [ "$BEHIND" -gt 0 ]; then
                AHEAD_BEHIND=" ↓${BEHIND}"
            fi
        fi
        GIT_BRANCH=" | 🌿 $BRANCH${WORKTREE}${AHEAD_BEHIND}"
    fi
fi

echo "[$MODEL_DISPLAY] 📁 ${CURRENT_DIR##*/}${GIT_BRANCH}
Context: [$PROGRESS_BAR] ${USED_PERCENTAGE}%
Cost: \$${COST_USD} | +${LINES_ADDED} -${LINES_REMOVED} lines"
```

## Git Worktrees for AI Coding Sessi
... [TRUNCATED]
```

### File: .mcp.json
```json
{
  "mcpServers": {
    "Gmail": {
      "type": "http",
      "url": "https://gmail.mcp.claude.com/mcp"
    },
    "Google Calendar": {
      "type": "http",
      "url": "https://gcal.mcp.claude.com/mcp"
    }
  }
}

```

### File: AGENTS.md
```md
## ALWAYS START WITH THESE COMMANDS FOR COMMON TASKS

**Task: "List/summarize all files and directories"**

```bash
fd . -t f           # Lists ALL files recursively (FASTEST)
# OR
rg --files          # Lists files (respects .gitignore)
```

**Task: "Search for content in files"**

```bash
rg "search_term"    # Search everywhere (FASTEST)
```

**Task: "Find files by name"**

```bash
fd "filename"       # Find by name pattern (FASTEST)
```

### Directory/File Exploration

```bash
# FIRST CHOICE - List all files/dirs recursively:
fd . -t f           # All files (fastest)
fd . -t d           # All directories
rg --files          # All files (respects .gitignore)

# For current directory only:
ls -la              # OK for single directory view
```

### BANNED - Never Use These Slow Tools

* ❌ `tree` - NOT INSTALLED, use `fd` instead
* ❌ `find` - use `fd` or `rg --files`
* ❌ `grep` or `grep -r` - use `rg` instead
* ❌ `ls -R` - use `rg --files` or `fd`
* ❌ `cat file | grep` - use `rg pattern file`

### Use These Faster Tools Instead

```bash
# ripgrep (rg) - content search 
rg "search_term"                # Search in all files
rg -i "case_insensitive"        # Case-insensitive
rg "pattern" -t py              # Only Python files
rg "pattern" -g "*.md"          # Only Markdown
rg -1 "pattern"                 # Filenames with matches
rg -c "pattern"                 # Count matches per file
rg -n "pattern"                 # Show line numbers 
rg -A 3 -B 3 "error"            # Context lines
rg " (TODO| FIXME | HACK)"      # Multiple patterns

# ripgrep (rg) - file listing 
rg --files                      # List files (respects •gitignore)
rg --files | rg "pattern"       # Find files by name 
rg --files -t md                # Only Markdown files 

# fd - file finding 
fd -e js                        # All •js files (fast find) 
fd -x command {}                # Exec per-file 
fd -e md -x ls -la {}           # Example with ls 

# jq - JSON processing 
jq. data.json                   # Pretty-print 
jq -r .name file.json           # Extract field 
jq '.id = 0' x.json             # Modify field
```

### Search Strategy

1. Start broad, then narrow: `rg "partial" | rg "specific"`
2. Filter by type early: `rg -t python "def function_name"`
3. Batch patterns: `rg "(pattern1|pattern2|pattern3)"`
4. Limit scope: `rg "pattern" src/`

### INSTANT DECISION TREE

```
User asks to "list/show/summarize/explore files"?
  → USE: fd . -t f  (fastest, shows all files)
  → OR: rg --files  (respects .gitignore)

User asks to "search/grep/find text content"?
  → USE: rg "pattern"  (NOT grep!)

User asks to "find file/directory by name"?
  → USE: fd "name"  (NOT find!)

User asks for "directory structure/tree"?
  → USE: fd . -t d  (directories) + fd . -t f  (files)
  → NEVER: tree (not installed!)

Need just current directory?
  → USE: ls -la  (OK for single dir)
```

```

### File: CLAUDE-cloudflare-mini.md
```md
# CLAUDE.md - Cloudflare Quick Template

## Project: [NAME]
Auth: Clerk | Platform: Cloudflare Workers/Pages

---

## CRITICAL: Verify Before Coding

### Step 1: Detect Stack
Inspect project files:
- `package.json` -> Node/TS (check deps: hono, next, remix, astro)
- `requirements.txt` / `pyproject.toml` -> Python Workers
- `go.mod` -> Go | `Cargo.toml` -> Rust
- `index.html` (no package.json) -> Static HTML (use Pages Git Integration)
- No files? -> Run `npm create cloudflare@latest`

### Step 2: Fetch Documentation
Use MCP tools if available, otherwise web fetch these URLs:

**Cloudflare:**
| Service | URL |
|---------|-----|
| Workers | https://developers.cloudflare.com/workers/ |
| D1 Get Started | https://developers.cloudflare.com/d1/get-started/ |
| KV | https://developers.cloudflare.com/kv/ |
| R2 | https://developers.cloudflare.com/r2/ |
| Durable Objects | https://developers.cloudflare.com/durable-objects/ |
| Pages | https://developers.cloudflare.com/pages/ |
| Pages Git Integration | https://developers.cloudflare.com/pages/get-started/git-integration/ |
| Pages Functions | https://developers.cloudflare.com/pages/functions/ |
| Sandbox SDK | https://developers.cloudflare.com/sandbox/ |
| Containers | https://developers.cloudflare.com/containers/ |

**Clerk:**
| Resource | URL |
|----------|-----|
| JS Backend SDK | https://clerk.com/docs/js-backend/getting-started/quickstart |
| authenticateRequest() | https://clerk.com/docs/reference/backend/authenticate-request |
| Hono Middleware | https://github.com/honojs/middleware/tree/main/packages/clerk-auth |
| Next.js | https://clerk.com/docs/reference/nextjs/overview |

**Frameworks:**
| Framework | URL |
|-----------|-----|
| Hono | https://hono.dev/docs/getting-started/cloudflare-workers |
| Next.js | https://developers.cloudflare.com/pages/framework-guides/nextjs/ |
| Drizzle+D1 | https://orm.drizzle.team/docs/get-started/d1-new |

---

## Wrangler Config Reference

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "name": "app",
  "main": "src/index.ts",
  "compatibility_date": "2024-12-01",
  "compatibility_flags": ["nodejs_compat"],
  "d1_databases": [{ "binding": "DB", "database_name": "x", "database_id": "x" }],
  "kv_namespaces": [{ "binding": "KV", "id": "x" }],
  "r2_buckets": [{ "binding": "BUCKET", "bucket_name": "x" }]
}
```

---

## Cloudflare Pages: Static HTML via GitHub

For static HTML sites (no build step). Docs: https://developers.cloudflare.com/pages/get-started/git-integration/

### Setup (Dashboard)
1. **Dashboard > Workers & Pages > Create > Pages > Connect to Git**
2. Select GitHub repo
3. Build command: *(empty)* | Output directory: `/` or `/public`
4. Deploy

### Static Site Structure
```
/
├── index.html
├── about.html
├── css/style.css
├── js/app.js
├── _headers          # Optional: caching/security headers
└── _redirects        # Optional: redirect rules
```

### Adding API Routes (Pages Functions)
```
/
├── index.html
├── functions/
│   └── api/
│       └── hello.ts  # -> /api/hello
```

**functions/api/hello.ts:**
```typescript
// Use PagesFunction<Env> when you have bindings (D1, KV, etc.)
export const onRequest: PagesFunction = async (context) => {
  return Response.json({ message: 'Hello!' })
}
```

### CLI Commands
```bash
wrangler pages dev ./              # Local dev
wrangler pages deploy ./ --project-name=my-site  # Deploy
```

---

## Clerk Patterns (VERIFY CURRENT API BEFORE USE)

**Hono (@hono/clerk-auth):**
```typescript
import { Hono } from 'hono'
import { clerkMiddleware, getAuth } from '@hono/clerk-auth'

const app = new Hono<{ Bindings: Env }>()
app.use('*', clerkMiddleware())
app.get('/api/*', (c) => {
  const auth = getAuth(c)
  if (!auth?.userId) return c.json({ error: 'Unauthorized' }, 401)
  return c.json({ userId: auth.userId })
})
export default app
```

**Raw Workers (@clerk/backend):**
```typescript
import { createClerkClient } from '@clerk/backend'

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // BOTH keys required!
    const clerkClient = createClerkClient({
      secretKey: env.CLERK_SECRET_KEY,
      publishableKey: env.CLERK_PUBLISHABLE_KEY,
    })
    
    const { isAuthenticated, toAuth } = await clerkClient.authenticateRequest(request, {
      authorizedParties: ['https://your-domain.com']
    })
    
    if (!isAuthenticated) {
      return new Response('Unauthorized', { status: 401 })
    }
    
    const auth = toAuth()
    return new Response(JSON.stringify({ userId: auth.userId }))
  }
}
```

---

## Sandbox SDK (Code Execution)

Run untrusted code in isolated containers. Docs: https://developers.cloudflare.com/sandbox/

**Use cases:** AI agents, CI/CD, cloud REPLs, data analysis

**Setup:**
```bash
npm create cloudflare@latest -- my-sandbox --template=cloudflare/sandbox-sdk/examples/minimal
```

**Wrangler config:**
```jsonc
"containers": [{ "class_name": "Sandbox", "image": "./Dockerfile", "instance_type": "lite", "max_instances": 5 }],
"durable_objects": { "bindings": [{ "class_name": "Sandbox", "name": "Sandbox" }] },
"migrations": [{ "tag": "v1", "new_sqlite_classes": ["Sandbox"] }]
```

**Dockerfile:**
```dockerfile
FROM docker.io/cloudflare/sandbox:latest
RUN pip3 install --no-cache-dir pandas numpy
EXPOSE 8080  # Required for wrangler dev
```

**Basic usage (CRITICAL: proxyToSandbox first!):**
```typescript
import { getSandbox, proxyToSandbox, type Sandbox } from '@cloudflare/sandbox';
export { Sandbox } from '@cloudflare/sandbox';

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // CRITICAL: Must call first for preview URLs
    const proxyResponse = await proxyToSandbox(request, env);
    if (proxyResponse) return proxyResponse;

    const sandbox = getSandbox(env.Sandbox, 'my-sandbox', { normalizeId: true });
    const result = await sandbox.exec('python3 -c "print(2+2)"');
    // result.stdout, result.stderr, result.exitCode, result.success

    await sandbox.writeFile('/workspace/file.txt', 'content');  // Use /workspace!
    const file = await sandbox.readFile('/workspace/file.txt');
    return Response.json({ output: result.stdout });
  }
};
```

**Instance types:**
| Type | vCPU | Memory |
|------|------|--------|
| lite | 0.5 | 256MB |
| standard | 1 | 512MB |
| heavy | 2 | 1GB |

**Sandbox Gotchas:**
- `proxyToSandbox()` MUST be called first
- Requires Docker locally for dev
- First deploy: 2-3 min; cold start: 2-3s
- Use `/workspace` for persistent files
- Preview URLs need custom domain + wildcard DNS + `normalizeId: true`
- `keepAlive: true` requires `destroy()` call

---

## Secrets
- `.dev.vars` for local (gitignore!)
- `wrangler secret put KEY` for prod
- **Required for Clerk:** `CLERK_SECRET_KEY` AND `CLERK_PUBLISHABLE_KEY`

---

## Commands Reference

### Wrangler CLI Documentation
Full reference: https://developers.cloudflare.com/workers/wrangler/commands/

```bash
# ============================================================================
# PROJECT SETUP
# Docs: https://developers.cloudflare.com/workers/get-started/guide/
# ============================================================================
npm create cloudflare@latest              # Interactive project creation
npm create cloudflare@latest my-app       # Named project
npm create cloudflare@latest -- --template hono  # With template

# ============================================================================
# LOCAL DEVELOPMENT
# Workers: https://developers.cloudflare.com/workers/wrangler/commands/#dev
# Pages: https://developers.cloudflare.com/pages/functions/local-development/
# ============================================================================
wrangler dev                    # Workers dev server (localhost:8787)
wrangler dev --port 3000        # Custom port
wrangler dev --remote           # Use REAL cloud resources (CAUTION!)

wrangler pages dev ./           # Pages dev server (localhost:8788)
wrangler pages dev ./dist       # Pages with build output dir
wrangler pages dev ./ --d1=DB   # Pages with D1 binding

# ============================================================================
# DEPLOYMENT
# Docs: https://developers.cloudflare.com/workers/wrangler/commands/#deploy
# ============================================================================
wrangler deploy                 # Deploy Worker to production
wrangler deploy --env staging   # Deploy to environment

wrangler pages deploy ./dist --project-name=my-site  # Deploy Pages
wrangler pages project create my-site                 # Create Pages project first

# ============================================================================
# D1 DATABASE (SQLite)
# Docs: https://developers.cloudflare.com/d1/wrangler-commands/
# ============================================================================
wrangler d1 create <db-name>    # Create DB (returns database_id for config)
wrangler d1 list                # List all databases

# Execute SQL (--local for dev, --remote for production)
wrangler d1 execute <db> --local --file=./schema.sql   # Local
wrangler d1 execute <db> --remote --file=./schema.sql  # PRODUCTION (careful!)
wrangler d1 execute <db> --local --command="SELECT * FROM users"

# Migrations (recommended for schema changes)
# Docs: https://developers.cloudflare.com/d1/reference/migrations/
wrangler d1 migrations create <db> <name>   # Create migration file
wrangler d1 migrations apply <db> --local   # Apply locally
wrangler d1 migrations apply <db> --remote  # Apply to production

# ============================================================================
# KV STORAGE (Key-Value, eventually consistent)
# Docs: https://developers.cloudflare.com/kv/reference/kv-commands/
# ============================================================================
wrangler kv namespace create <name>         # Create namespace (returns id)
wrangler kv namespace create <name> --preview  # Create preview namespace
wrangler kv namespace list                  # List namespaces

wrangler kv key put --binding=KV "key" "value" --local  # Put (local)
wrangler kv key put --binding=KV "key" "value"          # Put (production)
wrangler kv key get --binding=KV "key"                  # Get value
wrangler kv key list --binding=KV                       # List keys

# ============================================================================
# R2 OBJECT STORAGE (S3-compatible)
# Docs: https://developers.cloudflare.com/r2/api/wrangler/
# ============================================================================
wrangler r2 bucket create <name>            # Create bucket
wrangler r2 bucket list                     # List buckets
wrangler r2 object put <bucket>/<key> --file=./file.txt  # Upload
wrangler r2 object get <bucket>/<key>       # Download

# ============================================================================
# SECRETS (Encrypted env vars for production)
# Docs: https://developers.cloudflare.com/workers/wrangler/commands/#secret
# ============================================================================
wrangler secret put <NAME>                  # Add secret (prompts for value)
echo "value" | wrangler secret put <NAME>   # Add from stdin (CI/CD)
wrangler secret list                        # List secret names
wrangler secret delete <NAME>               # Delete secret

# ============================================================================
# TYPESCRIPT & DEBUGGING
# ============================================================================
wrangler types                  # Generate Env types from config
                                # Docs: https://developers.cloudflare.com/workers/wrangler/commands/#types

wrangler tail                   # Stream production logs
wrangler tail --status=error    # Filter by status
wrangler tail --format=json     # JSON output
                                # Docs: https://developers.cloudflare.com/workers/wrangler/commands/#tail

# ============================================================================
# AUTH
# ============================================================================
wrangler login                  # Login to Cloudflare (opens browser)
wrangler whoami                 # Check current user
wrangler logout                 # Logout
```

### Key Command Patterns for AI

```bash
# Pattern: Local vs Remote operations
# --local  = Uses local simulation (safe for development)
# --remote = Uses PRODUCTION resources (be careful!)

# Pattern: Bindings in Pages dev
# Pass bindings via CLI when no wrangler.toml:
wrangler pages dev ./ --d1=DB --kv=CACHE --r2=STORAGE

# Pattern: Environment-specific operations
wrangler deploy --env staging
wrangler secret put API_KEY --env staging
wrangler tail --env staging

# Pattern: Get resource IDs for wrangler config
wrangler d1 create my-db      # Output includes database_id
wrangler kv namespace create CACHE  # Output includes namespace id
# Add these IDs to wrangler.toml/wrangler.jsonc bindings
```

---

## Key Constraints
| Limit | Value |
|-------|-------|
| D1 rows/query | 1000 (use pagination) |
| KV consistency | Eventually consistent |
| Workers CPU | 30s paid / 10ms free |
| R2 object size | 5TB max |

**Gotchas:**
- Clone request before reading body twice
- Use `nodejs_compat` flag for Node APIs
- Clerk `@clerk/backend` needs BOTH secretKey AND publishableKey
- D1 transactions: `await db.batch([stmt1, stmt2])`
- Set `authorizedParties` in Clerk to prevent CSRF
- Sandbox: `proxyToSandbox()` MUST be called first
- Sandbox requires Docker locally; first deploy takes 2-3 min
- Use `/workspace` for persistent files in Sandbox

---

## Notes
<!-- Project-specific notes -->
```

### File: CLAUDE-cloudflare.md
```md
# CLAUDE.md - Cloudflare Platform Project Template

## Project Overview
- **Project Name**: [PROJECT_NAME]
- **Description**: [BRIEF_DESCRIPTION]
- **Auth Provider**: Clerk

---

## CRITICAL: Documentation Verification Rules

### Before Writing ANY Code
1. **Determine project language/framework** by inspecting project files
2. **Lookup current documentation** for the detected stack before implementing
3. **Never assume** API signatures, binding syntax, or SDK methods

### MCP Tools (if available)
- **context7 MCP**: Query for latest documentation
- **Cloudflare MCP**: List/create resources, search docs, verify resource IDs

### Documentation URLs (for web fetch if no MCP)
Fetch and read these URLs to verify current APIs:

**Cloudflare Platform:**
| Service | URL |
|---------|-----|
| Workers | https://developers.cloudflare.com/workers/ |
| D1 (SQLite) | https://developers.cloudflare.com/d1/ |
| D1 Get Started | https://developers.cloudflare.com/d1/get-started/ |
| KV | https://developers.cloudflare.com/kv/ |
| R2 (Objects) | https://developers.cloudflare.com/r2/ |
| Durable Objects | https://developers.cloudflare.com/durable-objects/ |
| Queues | https://developers.cloudflare.com/queues/ |
| Workers AI | https://developers.cloudflare.com/workers-ai/ |
| Hyperdrive | https://developers.cloudflare.com/hyperdrive/ |
| Workflows | https://developers.cloudflare.com/workflows/ |
| Pages | https://developers.cloudflare.com/pages/ |
| Pages Git Integration | https://developers.cloudflare.com/pages/get-started/git-integration/ |
| Pages Functions | https://developers.cloudflare.com/pages/functions/ |
| Pages Functions Config | https://developers.cloudflare.com/pages/functions/wrangler-configuration/ |
| Wrangler Config | https://developers.cloudflare.com/workers/wrangler/configuration/ |
| Sandbox SDK | https://developers.cloudflare.com/sandbox/ |
| Sandbox Get Started | https://developers.cloudflare.com/sandbox/get-started/ |
| Containers | https://developers.cloudflare.com/containers/ |

**Clerk Authentication:**
| Resource | URL |
|----------|-----|
| Backend SDK Overview | https://clerk.com/docs/reference/backend/overview |
| JS Backend SDK Quickstart | https://clerk.com/docs/js-backend/getting-started/quickstart |
| authenticateRequest() Reference | https://clerk.com/docs/reference/backend/authenticate-request |
| Express SDK | https://clerk.com/docs/reference/express/overview |
| Next.js SDK | https://clerk.com/docs/reference/nextjs/overview |
| Hono Middleware (Community) | https://github.com/honojs/middleware/tree/main/packages/clerk-auth |

**Framework Deployment Guides:**
| Framework | URL |
|-----------|-----|
| Hono on Workers | https://hono.dev/docs/getting-started/cloudflare-workers |
| Next.js on Pages | https://developers.cloudflare.com/pages/framework-guides/nextjs/ |
| Remix on Pages | https://developers.cloudflare.com/pages/framework-guides/deploy-a-remix-site/ |
| Astro on Pages | https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/ |
| SvelteKit on Pages | https://developers.cloudflare.com/pages/framework-guides/deploy-a-svelte-kit-site/ |

**ORM/Database:**
| Tool | URL |
|------|-----|
| Drizzle + D1 | https://orm.drizzle.team/docs/get-started/d1-new |

---

## Project Detection & Setup

### Step 1: Detect Existing Project Type
Inspect project files to determine language/framework:

```
File Found                -> Stack              -> Action
-----------------------------------------------------------------
package.json              -> Node.js/TypeScript -> Check dependencies for framework
  - "hono"                -> Hono               -> Fetch Hono + CF Workers docs
  - "next"                -> Next.js            -> Fetch Next.js + CF Pages docs  
  - "@remix-run/*"        -> Remix              -> Fetch Remix + CF Pages docs
  - "astro"               -> Astro              -> Fetch Astro + CF Pages docs
  - No framework          -> Raw Worker         -> Fetch Workers docs only

requirements.txt          -> Python Workers     -> Add compatibility_flags: ["python_workers"]
pyproject.toml            -> Python Workers     -> Add compatibility_flags: ["python_workers"]
go.mod                    -> Go (WASM)          -> Fetch Go Workers docs
Cargo.toml                -> Rust (WASM)        -> Fetch Rust Workers docs
wrangler.toml/.jsonc      -> Existing config    -> Follow existing patterns

index.html (no package.json) -> Static HTML     -> Use Pages Git Integration (no build)
*.html files only         -> Static HTML        -> Use Pages Git Integration (no build)
```

### Step 2: New Project Setup (if no manifest files)
```bash
# Create new Workers project
npm create cloudflare@latest -- my-app

# Or with specific template
npm create cloudflare@latest -- my-app --template hono
```

### Step 3: Install Dependencies (after detection)
```bash
# Core (always needed for local dev)
npm install wrangler --save-dev

# Hono (if using)
npm install hono

# Clerk (choose based on framework)
npm install @clerk/backend                    # Raw Workers (also needs publishableKey!)
npm install @hono/clerk-auth @clerk/backend   # Hono (both packages required)
npm install @clerk/nextjs                     # Next.js
npm install @clerk/express                    # Express

# Drizzle ORM (if using D1)
npm install drizzle-orm
npm install drizzle-kit --save-dev
```

---

## Wrangler Configuration

### Config File (wrangler.jsonc preferred)
```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "name": "project-name",
  "main": "src/index.ts",
  "compatibility_date": "2024-12-01",
  "compatibility_flags": ["nodejs_compat"]
}
```

### Binding Configurations

**D1 Database:**
```jsonc
"d1_databases": [
  { "binding": "DB", "database_name": "my-db", "database_id": "UUID_HERE" }
]
```

**KV Namespace:**
```jsonc
"kv_namespaces": [
  { "binding": "KV", "id": "NAMESPACE_ID", "preview_id": "PREVIEW_ID" }
]
```

**R2 Bucket:**
```jsonc
"r2_buckets": [
  { "binding": "BUCKET", "bucket_name": "my-bucket" }
]
```

**Durable Objects:**
```jsonc
"durable_objects": {
  "bindings": [{ "name": "MY_DO", "class_name": "MyDurableObject" }]
},
"migrations": [{ "tag": "v1", "new_classes": ["MyDurableObject"] }]
```

**Queues:**
```jsonc
"queues": {
  "producers": [{ "binding": "QUEUE", "queue": "my-queue" }],
  "consumers": [{ "queue": "my-queue", "max_batch_size": 10 }]
}
```

**Workers AI:**
```jsonc
"ai": { "binding": "AI" }
```

**Hyperdrive (external Postgres):**
```jsonc
"hyperdrive": [
  { "binding": "HYPERDRIVE", "id": "HYPERDRIVE_ID" }
]
```

**Static Assets:**
```jsonc
"assets": { "directory": "./public" }
```

**Sandbox SDK (Containers):**
```jsonc
"containers": [
  { "class_name": "Sandbox", "image": "./Dockerfile", "instance_type": "lite", "max_instances": 5 }
],
"durable_objects": {
  "bindings": [{ "class_name": "Sandbox", "name": "Sandbox" }]
},
"migrations": [{ "tag": "v1", "new_sqlite_classes": ["Sandbox"] }]
```

---

## Cloudflare Pages: Static HTML via GitHub

For pure static HTML sites deployed via GitHub integration (no build step required).

### Documentation
| Resource | URL |
|----------|-----|
| Pages Get Started | https://developers.cloudflare.com/pages/get-started/git-integration/ |
| Pages Functions | https://developers.cloudflare.com/pages/functions/ |
| Pages Direct Upload | https://developers.cloudflare.com/pages/get-started/direct-upload/ |

### Setup via Cloudflare Dashboard (Recommended)
1. Go to **Cloudflare Dashboard > Workers & Pages > Create > Pages > Connect to Git**
2. Select your GitHub repository
3. Configure build settings:
   - **Build command**: *(leave empty for static HTML)*
   - **Build output directory**: `/` or your HTML folder (e.g., `/public`)
4. Deploy

### Repository Structure (Static HTML)
```
/
├── index.html            # Homepage
├── about.html            # Other pages
├── css/
│   └── style.css
├── js/
│   └── app.js
├── images/
│   └── logo.png
└── _headers              # Optional: custom headers
```

### Optional: `_headers` File (for caching, security)
```
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff

/css/*
  Cache-Control: public, max-age=31536000

/images/*
  Cache-Control: public, max-age=31536000
```

### Optional: `_redirects` File
```
/old-page  /new-page  301
/blog/*    /articles/:splat  302
```

### Adding API Routes (Pages Functions)
To add server-side API routes to a static site, create a `functions/` directory:

```
/
├── index.html
├── functions/
│   ├── api/
│   │   └── hello.ts      # Accessible at /api/hello
│   └── _middleware.ts    # Optional: runs on all routes
└── ...
```

**Example `functions/api/hello.ts`:**
```typescript
// VERIFY at: https://developers.cloudflare.com/pages/functions/
// PagesFunction type is globally available in Pages Functions

export const onRequest: PagesFunction = async (context) => {
  return Response.json({ message: 'Hello from Pages Function!' })
}
```

**Example `functions/api/hello.ts` with D1:**
```typescript
// Define Env interface for typed bindings
interface Env {
  DB: D1Database
}

export const onRequest: PagesFunction<Env> = async (context) => {
  const result = await context.env.DB.prepare('SELECT * FROM users LIMIT 10').all()
  return Response.json(result)
}
```

### Bindings for Pages Functions
Create `wrangler.toml` in project root for Pages Function bindings:
```toml
name = "my-static-site"
pages_build_output_dir = "./"
compatibility_date = "2024-12-01"

[[d1_databases]]
binding = "DB"
database_name = "my-db"
database_id = "UUID_HERE"

[[kv_namespaces]]
binding = "KV"
id = "NAMESPACE_ID"
```

### CLI Deployment (Alternative to GitHub)
```bash
# Install wrangler
npm install wrangler --save-dev

# Deploy directly (no GitHub needed)
wrangler pages deploy ./public --project-name=my-site

# Or create project first
wrangler pages project create my-site
wrangler pages deploy ./ --project-name=my-site
```

### Local Development
```bash
# Serve static files + Pages Functions locally
wrangler pages dev ./

# With specific port
wrangler pages dev ./ --port 3000

# With bindings (D1, KV, etc.)
wrangler pages dev ./ --d1=DB
```

### Custom Domain
1. Dashboard: **Pages project > Custom domains > Set up a custom domain**
2. Add CNAME record pointing to `<project>.pages.dev`
3. SSL provisioned automatically

---

## Sandbox SDK (Secure Code Execution)

Run untrusted code in isolated Linux containers. Each sandbox = Durable Object + Container.

### Documentation
| Resource | URL |
|----------|-----|
| Overview | https://developers.cloudflare.com/sandbox/ |
| Get Started | https://developers.cloudflare.com/sandbox/get-started/ |
| API Reference | https://developers.cloudflare.com/sandbox/api/ |
| GitHub | https://github.com/cloudflare/sandbox-sdk |

### Use Cases
- **AI Agents**: Execute LLM-generated code safely
- **CI/CD**: Automated testing pipelines
- **Cloud REPLs**: Interactive development environments
- **Data Analysis**: Run scripts with rich outputs (charts, tables)

### Instance Types
| Type | vCPU | Memory |
|------|------|--------|
| lite | 0.5 | 256 MB |
| standard | 1 | 512 MB |
| heavy | 2 | 1 GB |

### Project Setup
```bash
npm create cloudflare@latest -- my-sandbox --template=cloudflare/sandbox-sdk/examples/minimal
```

### Wrangler Configuration
```jsonc
{
  "name": "my-sandbox-app",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01",
  "containers": [{
    "class_name": "Sandbox",
    "image": "./Dockerfile",
    "instance_type": "lite",
    "max_instances": 5
  }],
  "durable_objects": {
    "bindings": [{ "class_name": "Sandbox", "name": "Sandbox" }]
  },
  "migrations": [{ "tag": "v1", "new_sqlite_classes": ["Sandbox"] }]
}
```

### Dockerfile
```dockerfile
FROM docker.io/cloudflare/sandbox:latest
RUN pip3 install --no-cache-dir pandas numpy matplotlib
EXPOSE 8080 3000  # Required for wrangler dev
```

### CRITICAL: Basic Usage Pattern
```typescript
import { getSandbox, proxyToSandbox, type Sandbox } from '@cloudflare/sandbox';
export { Sandbox } from '@cloudflare/sandbox';  // MUST re-export

type Env = { Sandbox: DurableObjectNamespace<Sandbox>; };

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // CRITICAL: proxyToSandbox MUST be called first for preview URLs
    const proxyResponse = await proxyToSandbox(request, env);
    if (proxyResponse) return proxyResponse;

    const sandbox = getSandbox(env.Sandbox, 'my-sandbox', {
      normalizeId: true,    // Required for preview URLs (lowercases ID)
      sleepAfter: '10m',    // Auto-sleep after inactivity
    });

    // Execute commands
    const result = await sandbox.exec('python3 -c "print(2 + 2)"');
    // result: { stdout, stderr, exitCode, success, duration }

    return Response.json({ output: result.stdout });
  }
};
```

### Command Execution API
```typescript
// Basic execution
const result = await sandbox.exec('python3 script.py', {
  cwd: '/workspace/project',
  env: { API_KEY: 'secret' },
  stream: true,
  onOutput: (stream, data) => console.log(data)
});

// Background processes
const process = await sandbox.startProcess('python3 -m http.server 8080', {
  processId: 'web-server',
  cwd: '/workspace/public'
});
await process.waitForPort(8080);  // Wait for readiness
await process.waitForLog(/Server running/);  // Wait for log pattern
const logs = await sandbox.getProcessLogs('web-server');
await sandbox.stopProcess('web-server');
```

### File Operations API
```typescript
// Write/read (use /workspace for persistent files)
await sandbox.writeFile('/workspace/file.txt', 'content');
await sandbox.writeFile('/workspace/img.png', base64Data, { encoding: 'base64' });
const { content } = await sandbox.readFile('/workspace/file.txt');

// Directory operations
await sandbox.mkdir('/workspace/dir', { recursive: true });
const files = await sandbox.listFiles('/workspace');
await sandbox.pathExists('/workspace/file.txt');

// Delete
await sandbox.deleteFile('/workspace/temp.txt');
await sandbox.deleteFile('/workspace/dir', { recursive: true });
```

### Sessions (Isolated Contexts)
```typescript
// Each session has own shell state, env vars, cwd
const session = await sandbox.createSession({
  id: 'user-123',
  cwd: '/workspace/user123',
  env: { USER_ID: '123' }
});

await session.exec('echo $USER_ID');
await session.writeFile('config.txt', 'data');
await sandbox.deleteSession('user-123');
```

### Code Interpreter (Rich Outputs)
```typescript
// Create context with variables
const ctx = await sandbox.createCodeContext({
  language: 'python',
  variables: { data: [1, 2, 3, 4, 5] }
});

// Execute code (state persists across runs)
const result = await ctx.runCode(`
import matplotlib.pyplot as plt
plt.plot(data, [x**2 for x in data])
plt.savefig('plot.png')
`);
// result.outputs: [{ type: 'text'|'image'|'html', content }]
```

### Port Exposure & WebSockets
```typescript
// Expose service (requires custom domain, not .workers.dev)
const { url } = await sandbox
... [TRUNCATED]
```

### File: CLAUDE-convex.md
```md
# CLAUDE.md - Convex Database Project Template

## Project Overview

- **Project Name**: [PROJECT_NAME]
- **Description**: [BRIEF_DESCRIPTION]
- **Database**: Convex
- **Hosting**: Cloudflare Pages
- **Auth Provider**: Clerk (recommended) / Convex Auth / Custom

---

## CRITICAL: Documentation Verification Rules

### Before Writing ANY Code

1. **Determine project language/framework** by inspecting project files
2. **Lookup current documentation** for the detected stack before implementing
3. **Never assume** API signatures, function syntax, or hook patterns

### MCP Tools (if available)

- **context7 MCP**: Query for latest Convex documentation
- **Cloudflare MCP**: Search Cloudflare Pages deployment docs

### Documentation URLs (for web fetch if no MCP)

Fetch and read these URLs to verify current APIs:

**Convex Platform:**

| Service | URL |
| --------- | ----- |
| LLM-Optimized Docs | <https://docs.convex.dev/llms.txt> |
| Quickstart (Next.js App Router) | <https://docs.convex.dev/quickstart/nextjs> |
| Quickstart (Next.js Pages Router) | <https://docs.convex.dev/client/nextjs/pages-router/quickstart> |
| Quickstart (React/Vite) | <https://docs.convex.dev/quickstart/react> |
| Database Schemas | <https://docs.convex.dev/database/schemas> |
| Reading Data (Queries) | <https://docs.convex.dev/database/reading-data> |
| Writing Data (Mutations) | <https://docs.convex.dev/database/writing-data> |
| Functions Overview | <https://docs.convex.dev/functions> |
| Query Functions | <https://docs.convex.dev/functions/query-functions> |
| Mutation Functions | <https://docs.convex.dev/functions/mutation-functions> |
| Actions | <https://docs.convex.dev/functions/actions> |
| HTTP Actions | <https://docs.convex.dev/functions/http-actions> |
| Scheduled Functions | <https://docs.convex.dev/scheduling/scheduled-functions> |
| Authentication Overview | <https://docs.convex.dev/auth> |
| Clerk Integration | <https://docs.convex.dev/auth/clerk> |
| Convex Auth | <https://docs.convex.dev/auth/convex-auth> |
| Custom Auth | <https://docs.convex.dev/auth/custom-auth> |
| Authorization Patterns | <https://docs.convex.dev/auth/authorization> |
| Database Indexes | <https://docs.convex.dev/database/indexes> |
| Pagination | <https://docs.convex.dev/database/pagination> |
| File Storage | <https://docs.convex.dev/file-storage> |
| Full-text Search | <https://docs.convex.dev/text-search> |
| Vector Search | <https://docs.convex.dev/vector-search> |
| TypeScript | <https://docs.convex.dev/typescript> |
| Error Handling | <https://docs.convex.dev/functions/error-handling> |
| Testing | <https://docs.convex.dev/production/testing> |
| Environment Variables | <https://docs.convex.dev/production/environment-variables> |
| Production Hosting | <https://docs.convex.dev/production/hosting> |
| Monitoring | <https://docs.convex.dev/production/monitoring> |
| Convex CLI | <https://docs.convex.dev/cli> |

**Clerk Authentication:**

| Resource | URL |
| ---------- | ----- |
| Clerk + Convex | <https://docs.convex.dev/auth/clerk> |
| Clerk Backend SDK | <https://clerk.com/docs/reference/backend/overview> |
| Clerk Next.js | <https://clerk.com/docs/reference/nextjs/overview> |
| Clerk React | <https://clerk.com/docs/reference/react/overview> |

**Cloudflare Pages Deployment:**

| Resource | URL |
| ---------- | ----- |
| Pages Overview | <https://developers.cloudflare.com/pages/> |
| Next.js on Pages | <https://developers.cloudflare.com/pages/framework-guides/nextjs/> |
| Build Configuration | <https://developers.cloudflare.com/pages/configuration/build-configuration/> |
| Pages Functions | <https://developers.cloudflare.com/pages/functions/> |

---

## Project Detection & Setup

### Step 1: Detect Existing Project Type

Inspect project files to determine language/framework:

```text
File Found                -> Stack              -> Action
-----------------------------------------------------------------
convex/ directory         -> Existing Convex    -> Check convex.json, schema.ts
package.json + "convex"   -> Convex project     -> Verify setup, check framework
  - "next" + app/         -> Next.js App Router -> Fetch Next.js App Router + Convex docs
  - "next" + pages/       -> Next.js Pages      -> Fetch Next.js Pages Router + Convex docs
  - "react" (Vite)        -> React + Vite       -> Fetch React + Convex docs
  - No framework          -> Add React/Next.js  -> User choice

No convex/ directory      -> New project        -> Run: npx create convex@latest
                                                  OR: npm install convex && npx convex dev
```

### Step 2: New Project Setup (if no convex/)

**Option 1: Create new Next.js project with Convex**

```bash
# VERIFY at: https://docs.convex.dev/quickstart/nextjs
npx create-next-app@latest my-app
cd my-app
npm install convex
npx convex dev
```

**Option 2: Add Convex to existing project**

```bash
# VERIFY at: https://docs.convex.dev/quickstart
npm install convex
npx convex dev  # Initializes convex/ directory and cloud project
```

**Option 3: Use Convex template (interactive)**

```bash
npx create convex@latest  # Interactive setup with framework selection
```

### Step 3: Install Dependencies (after detection)

**Core (always needed):**

```bash
npm install convex  # Convex client and server SDK
```

**Clerk Authentication (recommended):**

```bash
# For Next.js
npm install @clerk/nextjs

# For React
npm install @clerk/clerk-react
```

**Convex Auth (alternative, beta):**

```bash
# Built into Convex, configure via dashboard
# https://docs.convex.dev/auth/convex-auth
```

---

## Convex Configuration

### convex.json (Project Configuration)

**VERIFY at:** <https://docs.convex.dev/production/hosting/hosting-and-running>

```json
{
  "functions": "convex/",
  "node": {
    "externalPackages": ["sharp", "openai"]  // Node.js packages for actions
  }
}
```

**Technical Explanation:**

- `functions`: Directory containing Convex backend functions (queries, mutations, actions)
- `externalPackages`: Node.js packages that can be imported in actions (not queries/mutations)
- Most configuration is managed in Convex dashboard, not this file

---

### Environment Variables

**.env.local (Local Development):**

```bash
# VERIFY at: https://docs.convex.dev/production/environment-variables

# Frontend environment variable (accessible in browser)
# MUST start with NEXT_PUBLIC_ for Next.js
NEXT_PUBLIC_CONVEX_URL=https://your-deployment.convex.cloud

# For React (Vite):
VITE_CONVEX_URL=https://your-deployment.convex.cloud

# Backend environment variables are SET VIA CLI, not in .env
# Example:
# npx convex env set STRIPE_SECRET_KEY sk_test_...
# npx convex env set OPENAI_API_KEY sk-...
```

**Technical Explanation:**

- **Frontend vars**: Must be prefixed (`NEXT_PUBLIC_` or `VITE_`) - bundled into client code
- **Backend vars**: Set via CLI for security - accessible only in actions via `process.env`
- **Separate deployments**: Dev and prod have separate environment variables
- **Access in code**:
  - Frontend: `process.env.NEXT_PUBLIC_CONVEX_URL` (Next.js) or `import.meta.env.VITE_CONVEX_URL` (Vite)
  - Backend actions: `process.env.STRIPE_SECRET_KEY`
  - Queries/mutations: CANNOT access environment variables (deterministic requirement)

---

### ConvexProvider Setup Patterns

#### Next.js App Router

**VERIFY at:** <https://docs.convex.dev/quickstart/nextjs>

**app/ConvexClientProvider.tsx:**

```typescript
// ConvexClientProvider MUST be a client component
"use client";

import { ConvexProvider, ConvexReactClient } from "convex/react";
import { ReactNode } from "react";

// Initialize Convex client with deployment URL
const convex = new ConvexReactClient(process.env.NEXT_PUBLIC_CONVEX_URL!);

export function ConvexClientProvider({ children }: { children: ReactNode }) {
  return <ConvexProvider client={convex}>{children}</ConvexProvider>;
}
```

**Technical Explanation:**

- **"use client" required**: React Server Components can't use context providers
- **ConvexReactClient**: Manages WebSocket connection for real-time updates
- **Singleton pattern**: Create client once outside component to prevent reconnections

**app/layout.tsx:**

```typescript
// VERIFY at: https://docs.convex.dev/quickstart/nextjs
import { ConvexClientProvider } from "./ConvexClientProvider";

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <ConvexClientProvider>{children}</ConvexClientProvider>
      </body>
    </html>
  );
}
```

**Server-Side Rendering (SSR) with App Router:**

```typescript
// VERIFY at: https://docs.convex.dev/client/nextjs/app-router
import { preloadQuery } from "convex/nextjs";
import { api } from "@/convex/_generated/api";

export default async function ServerComponent() {
  // Preload query data on server
  const preloadedTasks = await preloadQuery(api.tasks.get);

  return <ClientComponent preloadedTasks={preloadedTasks} />;
}
```

---

#### Next.js Pages Router

**VERIFY at:** <https://docs.convex.dev/client/nextjs/pages-router/quickstart>

**pages/_app.tsx:**

```typescript
import { ConvexProvider, ConvexReactClient } from "convex/react";
import type { AppProps } from "next/app";

// Initialize Convex client
const convex = new ConvexReactClient(process.env.NEXT_PUBLIC_CONVEX_URL!);

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ConvexProvider client={convex}>
      <Component {...pageProps} />
    </ConvexProvider>
  );
}

export default MyApp;
```

**Technical Explanation:**

- **_app.tsx pattern**: Wraps all pages with ConvexProvider
- **Client-side only**: Pages Router has limited SSR support for Convex
- **API routes**: Use for server-side Convex operations

**API Route Example (pages/api/tasks.ts):**

```typescript
// VERIFY at: https://docs.convex.dev/client/nextjs/pages-router/server-rendering
import { ConvexHttpClient } from "convex/browser";
import { api } from "@/convex/_generated/api";
import type { NextApiRequest, NextApiResponse } from "next";

const client = new ConvexHttpClient(process.env.NEXT_PUBLIC_CONVEX_URL!);

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const tasks = await client.query(api.tasks.get);
  res.status(200).json({ tasks });
}
```

---

#### React (Vite)

**VERIFY at:** <https://docs.convex.dev/quickstart/react>

**src/main.tsx:**

```typescript
import React from "react";
import ReactDOM from "react-dom/client";
import { ConvexProvider, ConvexReactClient } from "convex/react";
import App from "./App";

// Initialize Convex client with Vite environment variable
const convex = new ConvexReactClient(import.meta.env.VITE_CONVEX_URL);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ConvexProvider client={convex}>
      <App />
    </ConvexProvider>
  </React.StrictMode>
);
```

**Technical Explanation:**

- **import.meta.env**: Vite's environment variable syntax (NOT process.env)
- **VITE_ prefix**: Required for Vite to include variable in build
- **Client-side only**: Pure React apps are client-rendered

---

## Database Operations

### Schema Definition

**VERIFY at:** <https://docs.convex.dev/database/schemas>

**convex/schema.ts:**

```typescript
import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

// Schema defines both database structure AND TypeScript types
export default defineSchema({
  tasks: defineTable({
    text: v.string(),
    isCompleted: v.boolean(),
    userId: v.id("users"),  // Reference to users table
    createdAt: v.number(),  // Timestamp (Date.now())
  })
    .index("by_user", ["userId"])           // Index for queries by user
    .index("by_user_status", ["userId", "isCompleted"])  // Compound index
    .searchIndex("search_text", {          // Full-text search
      searchField: "text",
    }),

  users: defineTable({
    name: v.string(),
    email: v.string(),
    clerkId: v.optional(v.string()),  // Optional field for Clerk integration
  })
    .index("by_clerk_id", ["clerkId"]),
});
```

**Technical Explanation:**

- **defineSchema**: Creates schema with type generation
- **defineTable**: Defines table structure with validators
- **Validators**: `v.string()`, `v.number()`, `v.boolean()`, `v.id("tableName")`, `v.optional()`, etc.
- **Indexes**: Required for efficient queries - must use `.withIndex()` in queries
- **Search indexes**: Enable full-text search with `searchFilter()`
- **Type safety**: Schema automatically generates TypeScript types in `convex/_generated/`

---

### Queries (Reading Data)

**VERIFY at:** <https://docs.convex.dev/database/reading-data>

**convex/tasks.ts:**

```typescript
import { query } from "./_generated/server";
import { v } from "convex/values";

// Get all tasks for a user
export const get = query({
  args: { userId: v.id("users") },
  handler: async (ctx, args) => {
    // Queries MUST use indexes for filtering
    const tasks = await ctx.db
      .query("tasks")
      .withIndex("by_user", (q) => q.eq("userId", args.userId))
      .collect();  // Returns all matching documents

    return tasks;
  },
});

// Get single task by ID
export const getById = query({
  args: { id: v.id("tasks") },
  handler: async (ctx, args) => {
    return await ctx.db.get(args.id);  // Returns task or null
  },
});

// Paginated query
export const getPaginated = query({
  args: { userId: v.id("users"), paginationOpts: v.object({ }) },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("tasks")
      .withIndex("by_user", (q) => q.eq("userId", args.userId))
      .paginate(args.paginationOpts);  // Returns { page, continueCursor, isDone }
  },
});
```

**Query Methods:**

- `.collect()` - Returns all matching documents as array
- `.take(n)` - Returns first n documents
- `.first()` - Returns first document or null
- `.unique()` - Returns single document or throws if multiple/zero
- `.paginate(opts)` - Returns paginated results with cursor

**Technical Explanation:**

- **Deterministic requirement**: Queries MUST return same result for same inputs
- **❌ Cannot use**: `Math.random()`, `Date.now()`, external API calls
- **Automatic caching**: Convex caches query results for performance
- **Real-time reactivity**: `useQuery()` hook automatically re-runs when data changes
- **withIndex() required**: Must explicitly use indexes - Convex doesn't auto-select

---

### Mutations (Writing Data)

**VERIFY at:** <https://docs.convex.dev/database/writing-data>

**convex/tasks.ts:**

```typescript
import { mutation } from "./_generated/server";
import { v } from "convex/values";

// Insert new task
export const create = mutation({
  args: {
    text: v.string(),
    userId: v.id("users"),
  },
  handler: async (ctx, args) => {
    // db.insert() returns the new document's ID
    const taskId = await ctx.db.insert("tasks", {
      text: args.text,
      userId: args.userId,
      isCompleted: false,
      create
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
