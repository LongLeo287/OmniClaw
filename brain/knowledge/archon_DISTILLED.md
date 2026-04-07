---
id: Archon
type: knowledge
owner: OA_Triage
---
# Archon
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <img src="./archon-ui-main/public/archon-main-graphic.png" alt="Archon Main Graphic" width="853" height="422">
</p>

<p align="center">
   <a href="https://trendshift.io/repositories/13964" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13964" alt="coleam00%2FArchon | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align="center">
  <em>Power up your AI coding assistants with your own custom knowledge base and task management as an MCP server</em>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> •
  <a href="#upgrading">Upgrading</a> •
  <a href="#whats-included">What's Included</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#troubleshooting">Troubleshooting</a>
</p>

---

## 🎯 What is Archon?

> Archon is currently in beta! Expect things to not work 100%, and please feel free to share any feedback and contribute with fixes/new features! Thank you to everyone for all the excitement we have for Archon already, as well as the bug reports, PRs, and discussions. It's a lot for our small team to get through but we're committed to addressing everything and making Archon into the best tool it possibly can be!

Archon is the **command center** for AI coding assistants. For you, it's a sleek interface to manage knowledge, context, and tasks for your projects. For the AI coding assistant(s), it's a **Model Context Protocol (MCP) server** to collaborate on and leverage the same knowledge, context, and tasks. Connect Claude Code, Kiro, Cursor, Windsurf, etc. to give your AI agents access to:

- **Your documentation** (crawled websites, uploaded PDFs/docs)
- **Smart search capabilities** with advanced RAG strategies
- **Task management** integrated with your knowledge base
- **Real-time updates** as you add new content and collaborate with your coding assistant on tasks
- **Much more** coming soon to build Archon into an integrated environment for all context engineering

This new vision for Archon replaces the old one (the agenteer). Archon used to be the AI agent that builds other agents, and now you can use Archon to do that and more.

> It doesn't matter what you're building or if it's a new/existing codebase - Archon's knowledge and task management capabilities will improve the output of **any** AI driven coding.

## 🔗 Important Links

- **[GitHub Discussions](https://github.com/coleam00/Archon/discussions)** - Join the conversation and share ideas about Archon
- **[Contributing Guide](CONTRIBUTING.md)** - How to get involved and contribute to Archon
- **[Introduction Video](https://youtu.be/8pRc_s2VQIo)** - Getting started guide and vision for Archon
- **[Archon Kanban Board](https://github.com/users/coleam00/projects/1)** - Where maintainers are managing issues/features
- **[Dynamous AI Mastery](https://dynamous.ai)** - The birthplace of Archon - come join a vibrant community of other early AI adopters all helping each other transform their careers and businesses!

## Quick Start

<p align="center">
  <a href="https://youtu.be/DMXyDpnzNpY">
    <img src="https://img.youtube.com/vi/DMXyDpnzNpY/maxresdefault.jpg" alt="Archon Setup Tutorial" width="640" />
  </a>
  <br/>
  <em>📺 Click to watch the setup tutorial on YouTube</em>
  <br/>
  <a href="./archon-example-workflow">-> Example AI coding workflow in the video <-</a>
</p>

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Node.js 18+](https://nodejs.org/) (for hybrid development mode)
- [Supabase](https://supabase.com/) account (free tier or local Supabase both work)
- [OpenAI API key](https://platform.openai.com/api-keys) (Gemini and Ollama are supported too!)
- (OPTIONAL) [Make](https://www.gnu.org/software/make/) (see [Installing Make](#installing-make) below)

### Setup Instructions

1. **Clone Repository**:
   ```bash
   git clone -b stable https://github.com/coleam00/archon.git
   ```
   ```bash
   cd archon
   ```
   
   **Note:** The `stable` branch is recommended for using Archon. If you want to contribute or try the latest features, use the `main` branch with `git clone https://github.com/coleam00/archon.git`
2. **Environment Configuration**:

   ```bash
   cp .env.example .env
   # Edit .env and add your Supabase credentials:
   # SUPABASE_URL=https://your-project.supabase.co
   # SUPABASE_SERVICE_KEY=your-service-key-here
   ```

   IMPORTANT NOTES:
   - For cloud Supabase: They recently introduced a new type of service role key but use the legacy one (the longer one).
   - For local Supabase: Set `SUPABASE_URL` to http://host.docker.internal:8000 (unless you have an IP address set up). To get `SUPABASE_SERVICE_KEY` run `supabase status -o env`.

3. **Database Setup**: In your [Supabase project](https://supabase.com/dashboard) SQL Editor, copy, paste, and execute the contents of `migration/complete_setup.sql`

4. **Start Services** (choose one):

   **Full Docker Mode (Recommended for Normal Archon Usage)**

   ```bash
   docker compose up --build -d
   ```

   This starts all core microservices in Docker:
   - **Server**: Core API and business logic (Port: 8181)
   - **MCP Server**: Protocol interface for AI clients (Port: 8051)
   - **UI**: Web interface (Port: 3737)

   Ports are configurable in your .env as well!

5. **Configure API Keys**:
   - Open http://localhost:3737
   - You'll automatically be brought through an onboarding flow to set your API key (OpenAI is default)

## ⚡ Quick Test

Once everything is running:

1. **Test Web Crawling**: Go to http://localhost:3737 → Knowledge Base → "Crawl Website" → Enter a doc URL (such as https://ai.pydantic.dev/llms.txt)
2. **Test Document Upload**: Knowledge Base → Upload a PDF
3. **Test Projects**: Projects → Create a new project and add tasks
4. **Integrate with your AI coding assistant**: MCP Dashboard → Copy connection config for your AI coding assistant 

## Installing Make

<details>
<summary><strong>🛠️ Make installation (OPTIONAL - For Dev Workflows)</strong></summary>

### Windows

```bash
# Option 1: Using Chocolatey
choco install make

# Option 2: Using Scoop
scoop install make

# Option 3: Using WSL2
wsl --install
# Then in WSL: sudo apt-get install make
```

### macOS

```bash
# Make comes pre-installed on macOS
# If needed: brew install make
```

### Linux

```bash
# Debian/Ubuntu
sudo apt-get install make

# RHEL/CentOS/Fedora
sudo yum install make
```

</details>

<details>
<summary><strong>🚀 Quick Command Reference for Make</strong></summary>
<br/>

| Command           | Description                                             |
| ----------------- | ------------------------------------------------------- |
| `make dev`        | Start hybrid dev (backend in Docker, frontend local) ⭐ |
| `make dev-docker` | Everything in Docker                                    |
| `make stop`       | Stop all services                                       |
| `make test`       | Run all tests                                           |
| `make lint`       | Run linters                                             |
| `make install`    | Install dependencies                                    |
| `make check`      | Check environment setup                                 |
| `make clean`      | Remove containers and volumes (with confirmation)       |

</details>

## 🔄 Database Reset (Start Fresh if Needed)

If you need to completely reset your database and start fresh:

<details>
<summary>⚠️ <strong>Reset Database - This will delete ALL data for Archon!</strong></summary>

1. **Run Reset Script**: In your Supabase SQL Editor, run the contents of `migration/RESET_DB.sql`

   ⚠️ WARNING: This will delete all Archon specific tables and data! Nothing else will be touched in your DB though.

2. **Rebuild Database**: After reset, run `migration/complete_setup.sql` to create all the tables again.

3. **Restart Services**:

   ```bash
   docker compose --profile full up -d
   ```

4. **Reconfigure**:
   - Select your LLM/embedding provider and set the API key again
   - Re-upload any documents or re-crawl websites

The reset script safely removes all tables, functions, triggers, and policies with proper dependency handling.

</details>

## 📚 Documentation

### Core Services

| Service                    | Container Name             | Default URL           | Purpose                                    |
| -------------------------- | -------------------------- | --------------------- | ------------------------------------------ |
| **Web Interface**          | archon-ui                  | http://localhost:3737 | Main dashboard and controls                |
| **API Service**            | archon-server              | http://localhost:8181 | Web crawling, document processing          |
| **MCP Server**             | archon-mcp                 | http://localhost:8051 | Model Context Protocol interface           |
| **Agents Service**         | archon-agents              | http://localhost:8052 | AI/ML operations, reranking                |
| **Agent Work Orders** *(optional)* | archon-agent-work-orders | http://localhost:8053 | Workflow execution with Claude Code CLI    |  

## Upgrading

To upgrade Archon to the latest version:

1. **Pull latest changes**:
   ```bash
   git pull
   ```

2. **Rebuild and restart containers**:
   ```bash
   docker compose up -d --build
   ```
   This rebuilds containers with the latest code and restarts all services.

3. **Check for database migrations**:
   - Open the Archon settings in your browser: [http://localhost:3737/settings](http://localhost:3737/settings)
   - Navigate to the **Database Migrations** section
   - If there are pending migrations, the UI will display them with clear instructions
   - Click on each migration to view and copy the SQL
   - Run the SQL scripts in your Supabase SQL editor in the order shown

## What's Included

### 🧠 Knowledge Management

- **Smart Web Crawling**: Automatically detects and crawls entire documentation sites, sitemaps, and individual pages
- **Document Processing**: Upload and process PDFs, Word docs, markdown files, and text documents with intelligent chunking
- **Code Example Extraction**: Automatically identifies and indexes code examples from documentation for enhanced search
- **Vector Search**: Advanced semantic search with contextual embeddings for precise knowledge retrieval
- **Source Management**: Organize knowledge by source, type, and tags for easy filtering

### 🤖 AI Integration

- **Model Context Protocol (MCP)**: Connect any MCP-compatible client (Claude Code, Cursor, even non-AI coding assistants like Claude Desktop)
- **MCP Tools**: Comprehensive yet simple set of tools for RAG queries, task management, and project operations
- **Multi-LLM Support**: Works with OpenAI, Ollama, and Google Gemini models
- **RAG Strategies**: Hybrid search, contextual embeddings, and result reranking for optimal AI responses
- **Real-time Streaming**: Live responses from AI agents with progress tracking

### 📋 Project & Task Management

- **Hierarchical Projects**: Organize work with projects, features, and tasks in a structured workflow
- **AI-Assisted Creation**: Generate project requirements and tasks using integrated AI agents
- **Document Management**: Version-controlled documents with collaborative editing capabilities
- **Progress Tracking**: Real-time updates and status management across all project activities

### 🔄 Real-time Collaboration

- **WebSocket Updates**: Live progress tracking for crawling, processing, and AI operations
- **Multi-user Support**: Collaborative knowledge building and project management
- **Background Processing**: Asynchronous operations that don't block the user interface
- **Health Monitoring**: Built-in service health checks and automatic reconnection

## Architecture

### Microservices Structure

Archon uses true microservices architecture with clear separation of concerns:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend UI   │    │  Server (API)   │    │   MCP Server    │    │ Agents Service  │
│                 │    │                 │    │                 │    │                 │
│  React + Vite   │◄──►│    FastAPI +    │◄──►│    Lightweight  │◄──►│   PydanticAI    │
│  Port 3737      │    │    SocketIO     │    │    HTTP Wrapper │    │   Port 8052     │
│                 │    │    Port 8181    │    │    Port 8051    │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
         │                        │                        │                        │
         └────────────────────────┼────────────────────────┼────────────────────────┘
                                  │                        │
                         ┌─────────────────┐               │
                         │    Database     │               │
                         │                 │               │
                         │    Supabase     │◄──────────────┘
                         │    PostgreSQL   │
                         │    PGVector     │
                         └─────────────────┘
```

### Service Responsibilities

| Service                  | Location                       | Purpose                          | Key Features                                                       |
| ------------------------ | ------------------------------ | -------------------------------- | ------------------------------------------------------------------ |
| **Frontend**             | `archon-ui-main/`              | Web interface and dashboard      | React, TypeScript, TailwindCSS, Socket.IO client                   |
| **Server**               | `python/src/server/`           | Core business logic and APIs     | FastAPI, service layer, Socket.IO broadcasts, all ML/AI operations |
| **MCP Server**           | `python/src/mcp/`              | MCP protocol interface           | Lightweight HTTP wrapper, MCP tools, session management            |
| **Agents**               | `python/src/agents/`           | PydanticAI agent hosting         | Document and RAG agents, streaming responses                       |
| **Agent Work Orders** *(optional)* | `python/src/agent_work_orders/` | Workflow execution engine | Claude Code CLI automation, repository management, SSE updates |

### Communication Patterns

- **HTTP-based**: All inter-service communication uses HTTP APIs
- **Socket.IO**: Real-time updates from Server to Frontend
- **MCP Protocol**: AI clients connect to MCP Server via SSE or stdio
- **No Direct Imports**: Services are truly independent with no shared code dependencies

### Key Architectural Benefits

- **Lightweight Containers**: Each service contains only required dependencies
- **Independent Scaling**: Services can be scaled independently based on load
- **Development Flexibility**: Teams can work on different services without conflicts
- **Tec
... [TRUNCATED]
```

### File: .claude_DISTILLED.md
```md
---
id: .claude
type: distilled_knowledge
---
# .claude

## SWALLOW ENGINE DISTILLATION

### File: agents_DISTILLED.md
```md
---
id: agents
type: distilled_knowledge
---
# agents

## SWALLOW ENGINE DISTILLATION

### File: codebase-analyst.md
```md
---
name: "codebase-analyst"
description: "Use proactively to find codebase patterns, coding style and team standards. Specialized agent for deep codebase pattern analysis and convention discovery"
model: "sonnet"
---

You are a specialized codebase analysis agent focused on discovering patterns, conventions, and implementation approaches.

## Your Mission

Perform deep, systematic analysis of codebases to extract:

- Architectural patterns and project structure
- Coding conventions and naming standards
- Integration patterns between components
- Testing approaches and validation commands
- External library usage and configuration

## Analysis Methodology

### 1. Project Structure Discovery

- Start looking for Architecture docs rules files such as claude.md, agents.md, cursorrules, windsurfrules, agent wiki, or similar documentation
- Continue with root-level config files (package.json, pyproject.toml, go.mod, etc.)
- Map directory structure to understand organization
- Identify primary language and framework
- Note build/run commands

### 2. Pattern Extraction

- Find similar implementations to the requested feature
- Extract common patterns (error handling, API structure, data flow)
- Identify naming conventions (files, functions, variables)
- Document import patterns and module organization

### 3. Integration Analysis

- How are new features typically added?
- Where do routes/endpoints get registered?
- How are services/components wired together?
- What's the typical file creation pattern?

### 4. Testing Patterns

- What test framework is used?
- How are tests structured?
- What are common test patterns?
- Extract validation command examples

### 5. Documentation Discovery

- Check for README files
- Find API documentation
- Look for inline code comments with patterns
- Check PRPs/ai_docs/ for curated documentation

## Output Format

Provide findings in structured format:

```yaml
project:
  language: [detected language]
  framework: [main framework]
  structure: [brief description]

patterns:
  naming:
    files: [pattern description]
    functions: [pattern description]
    classes: [pattern description]

  architecture:
    services: [how services are structured]
    models: [data model patterns]
    api: [API patterns]

  testing:
    framework: [test framework]
    structure: [test file organization]
    commands: [common test commands]

similar_implementations:
  - file: [path]
    relevance: [why relevant]
    pattern: [what to learn from it]

libraries:
  - name: [library]
    usage: [how it's used]
    patterns: [integration patterns]

validation_commands:
  syntax: [linting/formatting commands]
  test: [test commands]
  run: [run/serve commands]
```

## Key Principles

- Be specific - point to exact files and line numbers
- Extract executable commands, not abstract descriptions
- Focus on patterns that repeat across the codebase
- Note both good patterns to follow and anti-patterns to avoid
- Prioritize relevance to the requested feature/story

## Search Strategy

1. Start broad (project structure) then narrow (specific patterns)
2. Use parallel searches when investigating multiple aspects
3. Follow references - if a file imports something, investigate it
4. Look for "similar" not "same" - patterns often repeat with variations

Remember: Your analysis directly determines implementation success. Be thorough, specific, and actionable.

```

### File: library-researcher.md
```md
---
name: "library-researcher"
description: "Use proactively to research external libraries and fetch implementation-critical documentation"
model: "sonnet"
---

You are a specialized library research agent focused on gathering implementation-critical documentation.

## Your Mission

Research external libraries and APIs to provide:

- Specific implementation examples
- API method signatures and patterns
- Common pitfalls and best practices
- Version-specific considerations

## Research Strategy

### 1. Official Documentation

- Start with Archon MCP tools and check if we have relevant docs in the database
- Use the RAG tools to search for relevant documentation, use specific keywords and context in your queries
- Use websearch and webfetch to search official docs (check package registry for links)
- Find quickstart guides and API references
- Identify code examples specific to the use case
- Note version-specific features or breaking changes

### 2. Implementation Examples

- Search GitHub for real-world usage
- Find Stack Overflow solutions for common patterns
- Look for blog posts with practical examples
- Check the library's test files for usage patterns

### 3. Integration Patterns

- How do others integrate this library?
- What are common configuration patterns?
- What helper utilities are typically created?
- What are typical error handling patterns?

### 4. Known Issues

- Check library's GitHub issues for gotchas
- Look for migration guides indicating breaking changes
- Find performance considerations
- Note security best practices

## Output Format

Structure findings for immediate use:

```yaml
library: [library name]
version: [version in use]
documentation:
  quickstart: [URL with section anchor]
  api_reference: [specific method docs URL]
  examples: [example code URL]

key_patterns:
  initialization: |
    [code example]

  common_usage: |
    [code example]

  error_handling: |
    [code example]

gotchas:
  - issue: [description]
    solution: [how to handle]

best_practices:
  - [specific recommendation]

save_to_ai_docs: [yes/no - if complex enough to warrant local documentation]
```

## Documentation Curation

When documentation is complex or critical:

1. Create condensed version in PRPs/ai_docs/{library}\_patterns.md
2. Focus on implementation-relevant sections
3. Include working code examples
4. Add project-specific integration notes

## Search Queries

Effective search patterns:

- "{library} {feature} example"
- "{library} TypeError site:stackoverflow.com"
- "{library} best practices {language}"
- "github {library} {feature} language:{language}"

## Key Principles

- Prefer official docs but verify with real implementations
- Focus on the specific features needed for the story
- Provide executable code examples, not abstract descriptions
- Note version differences if relevant
- Save complex findings to ai_docs for future reference

Remember: Good library research prevents implementation blockers and reduces debugging time.

```


```

### File: commands_DISTILLED.md
```md
---
id: commands
type: distilled_knowledge
---
# commands

## SWALLOW ENGINE DISTILLATION

### File: agent-work-orders_DISTILLED.md
```md
---
id: agent-work-orders
type: distilled_knowledge
---
# agent-work-orders

## SWALLOW ENGINE DISTILLATION

### File: commit.md
```md
# Create Git Commit

Create an atomic git commit with a properly formatted commit message following best practices for the uncommited changes or these specific files if specified.

Specific files (skip if not specified):

- File 1: $1
- File 2: $2
- File 3: $3
- File 4: $4
- File 5: $5

## Instructions

**Commit Message Format:**

- Use conventional commits: `<type>: <description>`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Present tense (e.g., "add", "fix", "update", not "added", "fixed", "updated")
- 50 characters or less for the subject line
- Lowercase subject line
- No period at the end
- Be specific and descriptive

**Examples:**

- `feat: add web search tool with structured logging`
- `fix: resolve type errors in middleware`
- `test: add unit tests for config module`
- `docs: update CLAUDE.md with testing guidelines`
- `refactor: simplify logging configuration`
- `chore: update dependencies`

**Atomic Commits:**

- One logical change per commit
- If you've made multiple unrelated changes, consider splitting into separate commits
- Commit should be self-contained and not break the build

**IMPORTANT**

- NEVER mention claude code, anthropic, co authored by or anything similar in the commit messages

## Run

1. Review changes: `git diff HEAD`
2. Check status: `git status`
3. Stage changes: `git add -A`
4. Create commit: `git commit -m "<type>: <description>"`

## Report

- Output the commit message used
- Confirm commit was successful with commit hash
- List files that were committed

```

### File: execute.md
```md
# Execute PRP Plan

Implement a feature plan from the PRPs directory by following its Step by Step Tasks section.

## Variables

Plan file: $ARGUMENTS

## Instructions

- Read the entire plan file carefully
- Execute **every step** in the "Step by Step Tasks" section in order, top to bottom
- Follow the "Testing Strategy" to create proper unit and integration tests
- Complete all "Validation Commands" at the end
- Ensure all linters pass and all tests pass before finishing
- Follow CLAUDE.md guidelines for type safety, logging, and docstrings

## When done

- Move the PRP file to the completed directory in PRPs/features/completed

## Report

- Summarize completed work in a concise bullet point list
- Show files and lines changed: `git diff --stat`
- Confirm all validation commands passed
- Note any deviations from the plan (if any)

```

### File: noqa.md
```md
# NOQA Analysis and Resolution

Find all noqa/type:ignore comments in the codebase, investigate why they exist, and provide recommendations for resolution or justification.

## Instructions

**Step 1: Find all NOQA comments**

- Use Grep tool to find all noqa comments: pattern `noqa|type:\s*ignore`
- Use output_mode "content" with line numbers (-n flag)
- Search across all Python files (type: "py")
- Document total count of noqa comments found

**Step 2: For EACH noqa comment (repeat this process):**

- Read the file containing the noqa comment with sufficient context (at least 10 lines before and after)
- Identify the specific linting rule or type error being suppressed
- Understand the code's purpose and why the suppression was added
- Investigate if the suppression is still necessary or can be resolved

**Step 3: Investigation checklist for each noqa:**

- What specific error/warning is being suppressed? (e.g., `type: ignore[arg-type]`, `noqa: F401`)
- Why was the suppression necessary? (legacy code, false positive, legitimate limitation, technical debt)
- Can the underlying issue be fixed? (refactor code, update types, improve imports)
- What would it take to remove the suppression? (effort estimate, breaking changes, architectural changes)
- Is the suppression justified long-term? (external library limitation, Python limitation, intentional design)

**Step 4: Research solutions:**

- Check if newer versions of tools (mypy, ruff) handle the case better
- Look for alternative code patterns that avoid the suppression
- Consider if type stubs or Protocol definitions could help
- Evaluate if refactoring would be worthwhile

## Report Format

Create a markdown report file (create the reports directory if not created yet): `PRPs/reports/noqa-analysis-{YYYY-MM-DD}.md`

Use this structure for the report:

````markdown
# NOQA Analysis Report

**Generated:** {date}
**Total NOQA comments found:** {count}

---

## Summary

- Total suppressions: {count}
- Can be removed: {count}
- Should remain: {count}
- Requires investigation: {count}

---

## Detailed Analysis

### 1. {File path}:{line number}

**Location:** `{file_path}:{line_number}`

**Suppression:** `{noqa comment or type: ignore}`

**Code context:**

```python
{relevant code snippet}
```
````

**Why it exists:**
{explanation of why the suppression was added}

**Options to resolve:**

1. {Option 1: description}
   - Effort: {Low/Medium/High}
   - Breaking: {Yes/No}
   - Impact: {description}

2. {Option 2: description}
   - Effort: {Low/Medium/High}
   - Breaking: {Yes/No}
   - Impact: {description}

**Tradeoffs:**

- {Tradeoff 1}
- {Tradeoff 2}

**Recommendation:** {Remove | Keep | Refactor}
{Justification for recommendation}

---

{Repeat for each noqa comment}

````

## Example Analysis Entry

```markdown
### 1. src/shared/config.py:45

**Location:** `src/shared/config.py:45`

**Suppression:** `# type: ignore[assignment]`

**Code context:**
```python
@property
def openai_api_key(self) -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY not set")
    return key  # type: ignore[assignment]
````

**Why it exists:**
MyPy cannot infer that the ValueError prevents None from being returned, so it thinks the return type could be `str | None`.

**Options to resolve:**

1. Use assert to help mypy narrow the type
   - Effort: Low
   - Breaking: No
   - Impact: Cleaner code, removes suppression

2. Add explicit cast with typing.cast()
   - Effort: Low
   - Breaking: No
   - Impact: More verbose but type-safe

3. Refactor to use separate validation method
   - Effort: Medium
   - Breaking: No
   - Impact: Better separation of concerns

**Tradeoffs:**

- Option 1 (assert) is cleanest but asserts can be disabled with -O flag
- Option 2 (cast) is most explicit but adds import and verbosity
- Option 3 is most robust but requires more refactoring

**Recommendation:** Remove (use Option 1)
Replace the type:ignore with an assert statement after the if check. This helps mypy understand the control flow while maintaining runtime safety. The assert will never fail in practice since the ValueError is raised first.

**Implementation:**

```python
@property
def openai_api_key(self) -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY not set")
    assert key is not None  # Help mypy understand control flow
    return key
```

```

## Report

After completing the analysis:

- Output the path to the generated report file
- Summarize findings:
  - Total suppressions found
  - How many can be removed immediately (low effort)
  - How many should remain (justified)
  - How many need deeper investigation or refactoring
- Highlight any quick wins (suppressions that can be removed with minimal effort)
```

```

### File: planning.md
```md
# Feature Planning

Create a new plan to implement the `PRP` using the exact specified markdown `PRP Format`. Follow the `Instructions` to create the plan use the `Relevant Files` to focus on the right files.

## Variables

FEATURE $1 $2

## Instructions

- IMPORTANT: You're writing a plan to implement a net new feature based on the `Feature` that will add value to the application.
- IMPORTANT: The `Feature` describes the feature that will be implemented but remember we're not implementing a new feature, we're creating the plan that will be used to implement the feature based on the `PRP Format` below.
- Create the plan in the `PRPs/features/` directory with filename: `{d
... [TRUNCATED]
```

### File: AGENTS.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Beta Development Guidelines

**Local-only deployment** - each user runs their own instance.

### Core Principles

- **No backwards compatibility; we follow a fix‑forward approach** — remove deprecated code immediately
- **Detailed errors over graceful failures** - we want to identify and fix issues fast
- **Break things to improve them** - beta is for rapid iteration
- **Continuous improvement** - embrace change and learn from mistakes
- **KISS** - keep it simple
- **DRY** when appropriate
- **YAGNI** — don't implement features that are not needed

### Error Handling

**Core Principle**: In beta, we need to intelligently decide when to fail hard and fast to quickly address issues, and when to allow processes to complete in critical services despite failures. Read below carefully and make intelligent decisions on a case-by-case basis.

#### When to Fail Fast and Loud (Let it Crash!)

These errors should stop execution and bubble up immediately: (except for crawling flows)

- **Service startup failures** - If credentials, database, or any service can't initialize, the system should crash with a clear error
- **Missing configuration** - Missing environment variables or invalid settings should stop the system
- **Database connection failures** - Don't hide connection issues, expose them
- **Authentication/authorization failures** - Security errors must be visible and halt the operation
- **Data corruption or validation errors** - Never silently accept bad data, Pydantic should raise
- **Critical dependencies unavailable** - If a required service is down, fail immediately
- **Invalid data that would corrupt state** - Never store zero embeddings, null foreign keys, or malformed JSON

#### When to Complete but Log Detailed Errors

These operations should continue but track and report failures clearly:

- **Batch processing** - When crawling websites or processing documents, complete what you can and report detailed failures for each item
- **Background tasks** - Embedding generation, async jobs should finish the queue but log failures
- **WebSocket events** - Don't crash on a single event failure, log it and continue serving other clients
- **Optional features** - If projects/tasks are disabled, log and skip rather than crash
- **External API calls** - Retry with exponential backoff, then fail with a clear message about what service failed and why

#### Critical Nuance: Never Accept Corrupted Data

When a process should continue despite failures, it must **skip the failed item entirely** rather than storing corrupted data

#### Error Message Guidelines

- Include context about what was being attempted when the error occurred
- Preserve full stack traces with `exc_info=True` in Python logging
- Use specific exception types, not generic Exception catching
- Include relevant IDs, URLs, or data that helps debug the issue
- Never return None/null to indicate failure - raise an exception with details
- For batch operations, always report both success count and detailed failure list

### Code Quality

- Remove dead code immediately rather than maintaining it - no backward compatibility or legacy functions
- Avoid backward compatibility mappings or legacy function wrappers
- Fix forward
- Focus on user experience and feature completeness
- When updating code, don't reference what is changing (avoid keywords like SIMPLIFIED, ENHANCED, LEGACY, CHANGED, REMOVED), instead focus on comments that document just the functionality of the code
- When commenting on code in the codebase, only comment on the functionality and reasoning behind the code. Refrain from speaking to Archon being in "beta" or referencing anything else that comes from these global rules.

## Development Commands

### Frontend (archon-ui-main/)

```bash
npm run dev              # Start development server on port 3737
npm run build            # Build for production
npm run lint             # Run ESLint on legacy code (excludes /features)
npm run lint:files path/to/file.tsx  # Lint specific files

# Biome for /src/features directory only
npm run biome            # Check features directory
npm run biome:fix        # Auto-fix issues
npm run biome:format     # Format code (120 char lines)
npm run biome:ai         # Machine-readable JSON output for AI
npm run biome:ai-fix     # Auto-fix with JSON output

# Testing
npm run test             # Run all tests in watch mode
npm run test:ui          # Run with Vitest UI interface
npm run test:coverage:stream  # Run once with streaming output
vitest run src/features/projects  # Test specific directory

# TypeScript
npx tsc --noEmit         # Check all TypeScript errors
npx tsc --noEmit 2>&1 | grep "src/features"  # Check features only
```

### Backend (python/)

```bash
# Using uv package manager (preferred)
uv sync --group all      # Install all dependencies
uv run python -m src.server.main  # Run server locally on 8181
uv run pytest            # Run all tests
uv run pytest tests/test_api_essentials.py -v  # Run specific test
uv run ruff check        # Run linter
uv run ruff check --fix  # Auto-fix linting issues
uv run mypy src/         # Type check

# Docker operations
docker compose up --build -d       # Start all services
docker compose --profile backend up -d  # Backend only (for hybrid dev)
docker compose logs -f archon-server   # View server logs
docker compose logs -f archon-mcp      # View MCP server logs
docker compose restart archon-server   # Restart after code changes
docker compose down      # Stop all services
docker compose down -v   # Stop and remove volumes
```

### Quick Workflows

```bash
# Hybrid development (recommended) - backend in Docker, frontend local
make dev                 # Or manually: docker compose --profile backend up -d && cd archon-ui-main && npm run dev

# Full Docker mode
make dev-docker          # Or: docker compose up --build -d

# Run linters before committing
make lint                # Runs both frontend and backend linters
make lint-fe             # Frontend only (ESLint + Biome)
make lint-be             # Backend only (Ruff + MyPy)

# Testing
make test                # Run all tests
make test-fe             # Frontend tests only
make test-be             # Backend tests only
```

## Architecture Overview

@PRPs/ai_docs/ARCHITECTURE.md

#### TanStack Query Implementation

For architecture and file references:
@PRPs/ai_docs/DATA_FETCHING_ARCHITECTURE.md

For code patterns and examples:
@PRPs/ai_docs/QUERY_PATTERNS.md

#### Service Layer Pattern

See implementation examples:

- API routes: `python/src/server/api_routes/projects_api.py`
- Service layer: `python/src/server/services/project_service.py`
- Pattern: API Route → Service → Database

#### Error Handling Patterns

See implementation examples:

- Custom exceptions: `python/src/server/exceptions.py`
- Exception handlers: `python/src/server/main.py` (search for @app.exception_handler)
- Service error handling: `python/src/server/services/` (various services)

## ETag Implementation

@PRPs/ai_docs/ETAG_IMPLEMENTATION.md

## Database Schema

Key tables in Supabase:

- `sources` - Crawled websites and uploaded documents
  - Stores metadata, crawl status, and configuration
- `documents` - Processed document chunks with embeddings
  - Text chunks with vector embeddings for semantic search
- `projects` - Project management (optional feature)
  - Contains features array, documents, and metadata
- `tasks` - Task tracking linked to projects
  - Status: todo, doing, review, done
  - Assignee: User, Archon, AI IDE Agent
- `code_examples` - Extracted code snippets
  - Language, summary, and relevance metadata

## API Naming Conventions

@PRPs/ai_docs/API_NAMING_CONVENTIONS.md

Use database values directly (no mapping in the FE typesafe from BE and up):

## Environment Variables

Required in `.env`:

```bash
SUPABASE_URL=https://your-project.supabase.co  # Or http://host.docker.internal:8000 for local
SUPABASE_SERVICE_KEY=your-service-key-here      # Use legacy key format for cloud Supabase
```

Optional variables and full configuration:
See `python/.env.example` for complete list

## Common Development Tasks

### Add a new API endpoint

1. Create route handler in `python/src/server/api_routes/`
2. Add service logic in `python/src/server/services/`
3. Include router in `python/src/server/main.py`
4. Update frontend service in `archon-ui-main/src/features/[feature]/services/`

### Add a new UI component in features directory

1. Use Radix UI primitives from `src/features/ui/primitives/`
2. Create component in relevant feature folder under `src/features/[feature]/components/`
3. Define types in `src/features/[feature]/types/`
4. Use TanStack Query hook from `src/features/[feature]/hooks/`
5. Apply Tron-inspired glassmorphism styling with Tailwind

### Add or modify MCP tools

1. MCP tools are in `python/src/mcp_server/features/[feature]/[feature]_tools.py`
2. Follow the pattern:
   - `find_[resource]` - Handles list, search, and get single item operations
   - `manage_[resource]` - Handles create, update, delete with an "action" parameter
3. Register tools in the feature's `__init__.py` file

### Debug MCP connection issues

1. Check MCP health: `curl http://localhost:8051/health`
2. View MCP logs: `docker compose logs archon-mcp`
3. Test tool execution via UI MCP page
4. Verify Supabase connection and credentials

### Fix TypeScript/Linting Issues

```bash
# TypeScript errors in features
npx tsc --noEmit 2>&1 | grep "src/features"

# Biome auto-fix for features
npm run biome:fix

# ESLint for legacy code
npm run lint:files src/components/SomeComponent.tsx
```

## Code Quality Standards

### Frontend

- **TypeScript**: Strict mode enabled, no implicit any
- **Biome** for `/src/features/`: 120 char lines, double quotes, trailing commas
- **ESLint** for legacy code: Standard React rules
- **Testing**: Vitest with React Testing Library

### Backend

- **Python 3.12** with 120 character line length
- **Ruff** for linting - checks for errors, warnings, unused imports
- **Mypy** for type checking - ensures type safety
- **Pytest** for testing with async support

## MCP Tools Available

When connected to Claude/Cursor/Windsurf, the following tools are available:

### Knowledge Base Tools

- `archon:rag_search_knowledge_base` - Search knowledge base for relevant content
- `archon:rag_search_code_examples` - Find code snippets in the knowledge base
- `archon:rag_get_available_sources` - List available knowledge sources

### Project Management

- `archon:find_projects` - Find all projects, search, or get specific project (by project_id)
- `archon:manage_project` - Manage projects with actions: "create", "update", "delete"

### Task Management

- `archon:find_tasks` - Find tasks with search, filters, or get specific task (by task_id)
- `archon:manage_task` - Manage tasks with actions: "create", "update", "delete"

### Document Management

- `archon:find_documents` - Find documents, search, or get specific document (by document_id)
- `archon:manage_document` - Manage documents with actions: "create", "update", "delete"

### Version Control

- `archon:find_versions` - Find version history or get specific version
- `archon:manage_version` - Manage versions with actions: "create", "restore"

## Important Notes

- Projects feature is optional - toggle in Settings UI
- HTTP polling handles all updates
- Frontend uses Vite proxy for API calls in development
- Python backend uses `uv` for dependency management
- Docker Compose handles service orchestration
- TanStack Query for all data fetching - NO PROP DRILLING
- Vertical slice architecture in `/features` - features own their sub-features

```

### File: check-env.js
```js
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Secure path resolution
const projectRoot = process.cwd();
const envPath = path.resolve(projectRoot, '.env');

// Security: Validate path is within project
if (!envPath.startsWith(projectRoot)) {
  console.error('Security error: Invalid .env path');
  process.exit(1);
}

// Check if .env exists
if (!fs.existsSync(envPath)) {
  console.error('ERROR: .env file not found!');
  console.error('Copy .env.example to .env and add your credentials:');
  console.error('  cp .env.example .env');
  process.exit(1);
}

// Parse .env file
const envContent = fs.readFileSync(envPath, 'utf8');
const envVars = {};

envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (!trimmed || trimmed.startsWith('#')) return;
  
  const [key, ...valueParts] = trimmed.split('=');
  if (key) {
    const value = valueParts.join('=').trim().replace(/^["']|["']$/g, '');
    envVars[key.trim()] = value;
  }
});

// Only check ESSENTIAL variables
const required = ['SUPABASE_URL', 'SUPABASE_SERVICE_KEY'];
const errors = [];

required.forEach(varName => {
  if (!envVars[varName] || envVars[varName] === '') {
    errors.push(`Missing: ${varName}`);
  }
});

if (errors.length > 0) {
  console.error('ERROR: Required environment variables missing:');
  errors.forEach(err => console.error(`  - ${err}`));
  console.error('\nPlease add these to your .env file');
  process.exit(1);
}

// Validate URL format
try {
  new URL(envVars['SUPABASE_URL']);
} catch (e) {
  console.error('ERROR: SUPABASE_URL is not a valid URL');
  console.error(`  Found: ${envVars['SUPABASE_URL']}`);
  console.error('  Expected format: https://your-project.supabase.co');
  process.exit(1);
}

// Basic validation for service key
if (envVars['SUPABASE_SERVICE_KEY'].length < 10) {
  console.error('ERROR: SUPABASE_SERVICE_KEY appears to be invalid (too short)');
  console.error('  Please check your Supabase project settings');
  process.exit(1);
}

console.log('✓ Environment configured correctly');
```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Beta Development Guidelines

**Local-only deployment** - each user runs their own instance.

### Core Principles

- **No backwards compatibility; we follow a fix‑forward approach** — remove deprecated code immediately
- **Detailed errors over graceful failures** - we want to identify and fix issues fast
- **Break things to improve them** - beta is for rapid iteration
- **Continuous improvement** - embrace change and learn from mistakes
- **KISS** - keep it simple
- **DRY** when appropriate
- **YAGNI** — don't implement features that are not needed

### Error Handling

**Core Principle**: In beta, we need to intelligently decide when to fail hard and fast to quickly address issues, and when to allow processes to complete in critical services despite failures. Read below carefully and make intelligent decisions on a case-by-case basis.

#### When to Fail Fast and Loud (Let it Crash!)

These errors should stop execution and bubble up immediately: (except for crawling flows)

- **Service startup failures** - If credentials, database, or any service can't initialize, the system should crash with a clear error
- **Missing configuration** - Missing environment variables or invalid settings should stop the system
- **Database connection failures** - Don't hide connection issues, expose them
- **Authentication/authorization failures** - Security errors must be visible and halt the operation
- **Data corruption or validation errors** - Never silently accept bad data, Pydantic should raise
- **Critical dependencies unavailable** - If a required service is down, fail immediately
- **Invalid data that would corrupt state** - Never store zero embeddings, null foreign keys, or malformed JSON

#### When to Complete but Log Detailed Errors

These operations should continue but track and report failures clearly:

- **Batch processing** - When crawling websites or processing documents, complete what you can and report detailed failures for each item
- **Background tasks** - Embedding generation, async jobs should finish the queue but log failures
- **WebSocket events** - Don't crash on a single event failure, log it and continue serving other clients
- **Optional features** - If projects/tasks are disabled, log and skip rather than crash
- **External API calls** - Retry with exponential backoff, then fail with a clear message about what service failed and why

#### Critical Nuance: Never Accept Corrupted Data

When a process should continue despite failures, it must **skip the failed item entirely** rather than storing corrupted data

#### Error Message Guidelines

- Include context about what was being attempted when the error occurred
- Preserve full stack traces with `exc_info=True` in Python logging
- Use specific exception types, not generic Exception catching
- Include relevant IDs, URLs, or data that helps debug the issue
- Never return None/null to indicate failure - raise an exception with details
- For batch operations, always report both success count and detailed failure list

### Code Quality

- Remove dead code immediately rather than maintaining it - no backward compatibility or legacy functions
- Avoid backward compatibility mappings or legacy function wrappers
- Fix forward
- Focus on user experience and feature completeness
- When updating code, don't reference what is changing (avoid keywords like SIMPLIFIED, ENHANCED, LEGACY, CHANGED, REMOVED), instead focus on comments that document just the functionality of the code
- When commenting on code in the codebase, only comment on the functionality and reasoning behind the code. Refrain from speaking to Archon being in "beta" or referencing anything else that comes from these global rules.

## Development Commands

### Frontend (archon-ui-main/)

```bash
npm run dev              # Start development server on port 3737
npm run build            # Build for production
npm run lint             # Run ESLint on legacy code (excludes /features)
npm run lint:files path/to/file.tsx  # Lint specific files

# Biome for /src/features directory only
npm run biome            # Check features directory
npm run biome:fix        # Auto-fix issues
npm run biome:format     # Format code (120 char lines)
npm run biome:ai         # Machine-readable JSON output for AI
npm run biome:ai-fix     # Auto-fix with JSON output

# Testing
npm run test             # Run all tests in watch mode
npm run test:ui          # Run with Vitest UI interface
npm run test:coverage:stream  # Run once with streaming output
vitest run src/features/projects  # Test specific directory

# TypeScript
npx tsc --noEmit         # Check all TypeScript errors
npx tsc --noEmit 2>&1 | grep "src/features"  # Check features only
```

### Backend (python/)

```bash
# Using uv package manager (preferred)
uv sync --group all      # Install all dependencies
uv run python -m src.server.main  # Run server locally on 8181
uv run pytest            # Run all tests
uv run pytest tests/test_api_essentials.py -v  # Run specific test
uv run ruff check        # Run linter
uv run ruff check --fix  # Auto-fix linting issues
uv run mypy src/         # Type check

# Agent Work Orders Service (independent microservice)
make agent-work-orders  # Run agent work orders service locally on 8053
# Or manually:
uv run python -m uvicorn src.agent_work_orders.server:app --port 8053 --reload

# Docker operations
docker compose up --build -d       # Start all services
docker compose --profile backend up -d  # Backend only (for hybrid dev)
docker compose --profile work-orders up -d   # Include agent work orders service
docker compose logs -f archon-server    # View server logs
docker compose logs -f archon-mcp       # View MCP server logs
docker compose logs -f archon-agent-work-orders  # View agent work orders service logs
docker compose restart archon-server    # Restart after code changes
docker compose down      # Stop all services
docker compose down -v   # Stop and remove volumes
```

### Quick Workflows

```bash
# Hybrid development (recommended) - backend in Docker, frontend local
make dev                 # Or manually: docker compose --profile backend up -d && cd archon-ui-main && npm run dev

# Hybrid with Agent Work Orders Service - backend in Docker, agent work orders local
make dev-work-orders     # Starts backend in Docker, prompts to run agent service in separate terminal
# Then in separate terminal:
make agent-work-orders   # Start agent work orders service locally

# Full Docker mode
make dev-docker          # Or: docker compose up --build -d
docker compose --profile work-orders up -d  # Include agent work orders service

# All Local (3 terminals) - for agent work orders service development
# Terminal 1: uv run python -m uvicorn src.server.main:app --port 8181 --reload
# Terminal 2: make agent-work-orders
# Terminal 3: cd archon-ui-main && npm run dev

# Run linters before committing
make lint                # Runs both frontend and backend linters
make lint-fe             # Frontend only (ESLint + Biome)
make lint-be             # Backend only (Ruff + MyPy)

# Testing
make test                # Run all tests
make test-fe             # Frontend tests only
make test-be             # Backend tests only
```

## Architecture Overview

@PRPs/ai_docs/ARCHITECTURE.md

#### TanStack Query Implementation

For architecture and file references:
@PRPs/ai_docs/DATA_FETCHING_ARCHITECTURE.md

For code patterns and examples:
@PRPs/ai_docs/QUERY_PATTERNS.md

#### Service Layer Pattern

See implementation examples:
- API routes: `python/src/server/api_routes/projects_api.py`
- Service layer: `python/src/server/services/project_service.py`
- Pattern: API Route → Service → Database

#### Error Handling Patterns

See implementation examples:
- Custom exceptions: `python/src/server/exceptions.py`
- Exception handlers: `python/src/server/main.py` (search for @app.exception_handler)
- Service error handling: `python/src/server/services/` (various services)

## ETag Implementation

@PRPs/ai_docs/ETAG_IMPLEMENTATION.md

## Database Schema

Key tables in Supabase:

- `sources` - Crawled websites and uploaded documents
  - Stores metadata, crawl status, and configuration
- `documents` - Processed document chunks with embeddings
  - Text chunks with vector embeddings for semantic search
- `projects` - Project management (optional feature)
  - Contains features array, documents, and metadata
- `tasks` - Task tracking linked to projects
  - Status: todo, doing, review, done
  - Assignee: User, Archon, AI IDE Agent
- `code_examples` - Extracted code snippets
  - Language, summary, and relevance metadata

## API Naming Conventions

@PRPs/ai_docs/API_NAMING_CONVENTIONS.md

Use database values directly (no FE mapping; type‑safe end‑to‑end from BE upward):

## Environment Variables

Required in `.env`:

```bash
SUPABASE_URL=https://your-project.supabase.co  # Or http://host.docker.internal:8000 for local
SUPABASE_SERVICE_KEY=your-service-key-here      # Use legacy key format for cloud Supabase
```

Optional variables and full configuration:
See `python/.env.example` for complete list

### Repository Configuration

Repository information (owner, name) is centralized in `python/src/server/config/version.py`:
- `GITHUB_REPO_OWNER` - GitHub repository owner (default: "coleam00")
- `GITHUB_REPO_NAME` - GitHub repository name (default: "Archon")

This is the single source of truth for repository configuration. All services (version checking, bug reports, etc.) should import these constants rather than hardcoding repository URLs.

Environment variable override: `GITHUB_REPO="owner/repo"` can be set to override defaults.

## Common Development Tasks

### Add a new API endpoint

1. Create route handler in `python/src/server/api_routes/`
2. Add service logic in `python/src/server/services/`
3. Include router in `python/src/server/main.py`
4. Update frontend service in `archon-ui-main/src/features/[feature]/services/`

### Add a new UI component in features directory

**IMPORTANT**: Review UI design standards in `@PRPs/ai_docs/UI_STANDARDS.md` before creating UI components.

1. Use Radix UI primitives from `src/features/ui/primitives/`
2. Create component in relevant feature folder under `src/features/[feature]/components/`
3. Define types in `src/features/[feature]/types/`
4. Use TanStack Query hook from `src/features/[feature]/hooks/`
5. Apply Tron-inspired glassmorphism styling with Tailwind
6. Follow responsive design patterns (mobile-first with breakpoints)
7. Ensure no dynamic Tailwind class construction (see UI_STANDARDS.md Section 2)

### Add or modify MCP tools

1. MCP tools are in `python/src/mcp_server/features/[feature]/[feature]_tools.py`
2. Follow the pattern:
   - `find_[resource]` - Handles list, search, and get single item operations
   - `manage_[resource]` - Handles create, update, delete with an "action" parameter
3. Register tools in the feature's `__init__.py` file

### Debug MCP connection issues

1. Check MCP health: `curl http://localhost:8051/health`
2. View MCP logs: `docker compose logs archon-mcp`
3. Test tool execution via UI MCP page
4. Verify Supabase connection and credentials

### Fix TypeScript/Linting Issues

```bash
# TypeScript errors in features
npx tsc --noEmit 2>&1 | grep "src/features"

# Biome auto-fix for features
npm run biome:fix

# ESLint for legacy code
npm run lint:files src/components/SomeComponent.tsx
```

## Code Quality Standards

### Frontend

- **TypeScript**: Strict mode enabled, no implicit any
- **Biome** for `/src/features/`: 120 char lines, double quotes, trailing commas
- **ESLint** for legacy code: Standard React rules
- **Testing**: Vitest with React Testing Library

### Backend

- **Python 3.12** with 120 character line length
- **Ruff** for linting - checks for errors, warnings, unused imports
- **Mypy** for type checking - ensures type safety
- **Pytest** for testing with async support

## MCP Tools Available

When connected to Claude/Cursor/Windsurf, the following tools are available:

### Knowledge Base Tools

- `archon:rag_search_knowledge_base` - Search knowledge base for relevant content
- `archon:rag_search_code_examples` - Find code snippets in the knowledge base
- `archon:rag_get_available_sources` - List available knowledge sources
- `archon:rag_list_pages_for_source` - List all pages for a given source (browse documentation structure)
- `archon:rag_read_full_page` - Retrieve full page content by page_id or URL

### Project Management

- `archon:find_projects` - Find all projects, search, or get specific project (by project_id)
- `archon:manage_project` - Manage projects with actions: "create", "update", "delete"

### Task Management

- `archon:find_tasks` - Find tasks with search, filters, or get specific task (by task_id)
- `archon:manage_task` - Manage tasks with actions: "create", "update", "delete"

### Document Management

- `archon:find_documents` - Find documents, search, or get specific document (by document_id)
- `archon:manage_document` - Manage documents with actions: "create", "update", "delete"

### Version Control

- `archon:find_versions` - Find version history or get specific version
- `archon:manage_version` - Manage versions with actions: "create", "restore"

## Important Notes

- Projects feature is optional - toggle in Settings UI
- TanStack Query handles all data fetching; smart HTTP polling is used where appropriate (no WebSockets)
- Frontend uses Vite proxy for API calls in development
- Python backend uses `uv` for dependency management
- Docker Compose handles service orchestration
- TanStack Query for all data fetching - NO PROP DRILLING
- Vertical slice architecture in `/features` - features own their sub-features

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
