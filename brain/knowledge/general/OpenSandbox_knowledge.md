---
id: opensandbox-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:16.862570
---

# KNOWLEDGE EXTRACT: OpenSandbox
> **Extracted on:** 2026-03-30 17:50:27
> **Source:** OpenSandbox

---

## File: `.gitignore`
```
# IDE and Editor files
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store
Thumbs.db

# Go
# Binaries for programs and plugins
*.exe
*.exe~
*.dll
*.so
*.dylib

# Test binary, built with `go test -c`
*.test

# Output of the go coverage tool
*.out

# Dependency directories
vendor/

# Go workspace file
go.work

# Java/Kotlin
# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs
hs_err_pid*
replay_pid*

# Gradle
.gradle/
build/
!**/gradle/wrapper/gradle-wrapper.jar
!**/src/main/**/build/
!**/src/test/**/build/

# Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml
buildNumber.properties
.mvn/timing.properties
.mvn/wrapper/maven-wrapper.jar

# Node.js
# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*
.pnpm-debug.log*

# Dependency directories
node_modules/
jspm_packages/

# TypeScript cache
*.tsbuildinfo

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Optional stylelint cache
.stylelintcache

# Microbundle cache
.rpt2_cache/
.rts2_cache_cjs/
.rts2_cache_es/
.rts2_cache_umd/

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# Yarn v2
.yarn/cache
.yarn/unplugged
.yarn/build-state.yml
.yarn/install-state.gz
.pnp.*

# parcel-bundler cache (https://parceljs.org/)
.cache
.parcel-cache

# Next.js build output
.next
out

# Nuxt.js build / generate output
.nuxt
dist

# Gatsby files
.cache/
public
!docs/public/
!docs/public/CNAME

# Serverless directories
.serverless/

# FuseBox cache
.fusebox/

# DynamoDB Local files
.dynamodb/

# TernJS port file
.tern-port

# Stores VSCode versions used for testing VSCode extensions
.vscode-test

# yarn v2
.yarn/cache
.yarn/unplugged
.yarn/build-state.yml
.yarn/install-state.gz
.pnp.*

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
env/
ENV/
env.bak/
venv.bak/

# Docker
*.pid
*.seed
*.pid.lock

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Temporary files
*.tmp
*.temp
*~

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# API keys and secrets
secrets/
*.pem
*.key
*.crt
*.p12
*.pfx

# Generated API documentation
docs/generated/
docs/.vitepress/generated/
docs/.vitepress/dist/
docs/.vitepress/cache/
apidocs/

# Test results
test-results/
coverage/
*.coverage
.nyc_output

# Backup files
*.bak
*.backup
*.old

# Flattened POM files (Maven)
.flattened-pom.xml

# Kotlin
*.kotlin_module

# JetBrains specific
.idea/
*.iml
*.ipr
*.iws
out/

# Eclipse specific
.project
.classpath
.settings/
bin/

# NetBeans specific
nbproject/
nbbuild/
nbdist/
.nb-gradle/

# Generated files
generated/
**/generated/**

# gVisor runtime binaries (downloaded dynamically)
kubernetes/test/kind/gvisor/runsc
kubernetes/test/kind/gvisor/containerd-shim-runsc-v1
bin/
obj/
```

## File: `.pre-commit-config.yaml`
```yaml
# Minimal cross-language pre-commit hooks
# Install: pip install pre-commit && pre-commit install
# Run once on all files: pre-commit run --all-files

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: mixed-line-ending
      - id: check-merge-conflict
      - id: check-yaml
      - id: detect-private-key

  # Language-specific formatters/linters can be added later, for example:
  # - repo: local
  #   hooks:
  #     - id: gofmt
  #       name: gofmt
  #       entry: gofmt
  #       language: system
  #       types: [go]
  #     - id: ruff
  #       name: ruff
  #       entry: ruff check
  #       language: system
  #       types: [python]
```

## File: `AGENTS.md`
```markdown
# Repository Guidelines

## Project Structure & Module Organization
- `server/`: Python FastAPI service, configs, and tests.
- `components/execd/`: Go execution daemon and related tests.
- `sdks/`: Multi-language SDKs (`sdks/sandbox/*`, `sdks/code-interpreter/*`).
- `sandboxes/`: Runtime sandbox implementations (e.g., `sandboxes/code-interpreter/`).
- `specs/`: OpenAPI specs (`specs/execd-api.yaml`, `specs/sandbox-lifecycle.yml`).
- `examples/`: End-to-end usage examples and integrations.
- `tests/`: Cross-component/E2E tests (`tests/python/`, `tests/java/`).
- `docs/`, `oseps/`, `scripts/`: Docs, proposals, and automation scripts.

## Build, Test, and Development Commands
- Server (Python):
  - `cd server && uv sync` installs deps.
  - `cp server/example.config.toml ~/.sandbox.toml` sets local config.
  - `cd server && uv run python -m src.main` runs the API server.
- execd (Go):
  - `cd components/execd && go build -o bin/execd .` builds the daemon.
  - `cd components/execd && make fmt` formats Go sources.
- SDKs:
  - Python: `cd sdks/sandbox/python && uv sync && uv run pytest`.
  - Kotlin: `cd sdks/sandbox/kotlin && ./gradlew build`.
- Specs: `node scripts/spec-doc/generate-spec.js` regenerates spec docs.

## Coding Style & Naming Conventions
- Python: PEP 8, `ruff` for lint/format, type hints on public APIs.
- Go: `gofmt`, explicit error handling, standard import grouping.
- Kotlin: Kotlin Coding Conventions, `ktlint` where configured.
- Naming: classes `PascalCase`, functions `snake_case` (Python) / `camelCase` (Go/Kotlin), constants `UPPER_SNAKE_CASE`.

## SDK API Implementation Conventions
- Keep a clear split between generated API transport code and handwritten SDK business/adaptor code.
- In adapter/infrastructure layers, default to integrating through generated API clients instead of handcrafted request wiring.
- Prefer generated OpenAPI clients for standard request/response endpoints; use handwritten transport only for streaming or protocol-specific paths (for example SSE).
- Do not manually edit generated client files. When specs change, regenerate first, then adapt handwritten layers.
- For handwritten streaming paths, keep wire contracts aligned with OpenAPI field names/models and cover behavior with focused tests (especially parsing and error mapping).

## Testing Guidelines
- Python tests use `pytest` (async tests common).
- Go tests use `go test` under `components/execd/pkg/...`.
- Kotlin tests use Gradle (`./gradlew test`).
- Coverage targets (from CONTRIBUTING): core packages >80%, API layer >70%.

## Commit & Pull Request Guidelines
- Commit messages follow Conventional Commits, e.g. `feat(server): add runtime`.
- Use feature branches (e.g., `feature/...`, `fix/...`) and keep PRs focused.
- PRs should include summary, testing status, and linked issues; follow the template in `CONTRIBUTING.md`.
- For major API or architectural changes, submit an OSEP (`oseps/`).

## Security & Configuration Tips
- Local server config lives in `~/.sandbox.toml` (copied from `server/example.config.toml`).
- Docker is required for local sandbox execution; keep images and keys out of commits.
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Code of Conduct

We are committed to a welcoming, safe, and respectful community.

## Expected Behavior
- Be respectful and inclusive.
- Assume good intent; seek to understand.
- Provide constructive feedback; critique code, not people.
- Follow project guidelines and security practices.

## Unacceptable Behavior
- Harassment, personal attacks, or discriminatory language.
- Publishing private information without consent.
- Disruptive or aggressive behavior in any project space.

## Scope
This Code applies to all project spaces, including issues, pull requests, discussions, chat, and events.

## Reporting
Report incidents to: **conduct@opensandbox.io**. Include as much detail as possible (what happened, when/where, links, screenshots if applicable).

## Enforcement
Maintainers will investigate in good faith and may take appropriate action, including warnings, temporary bans, or removal from the community.
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to OpenSandbox

Thank you for your interest in contributing to OpenSandbox! This guide will help you get started with contributing to the project, whether you're fixing bugs, adding features, improving documentation, or helping in other ways.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Environment Setup](#development-environment-setup)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Submitting Contributions](#submitting-contributions)
- [Communication Channels](#communication-channels)

## Code of Conduct

OpenSandbox adheres to a [Code of Conduct](CODE_OF_CONDUCT.md) that we expect all contributors to follow. Please read it before contributing to ensure a welcoming and inclusive environment for everyone.

## Getting Started

### Ways to Contribute

There are many ways to contribute to OpenSandbox:

- **Report Bugs**: Submit detailed bug reports through [GitHub Issues](https://github.com/alibaba/OpenSandbox/issues)
- **Suggest Features**: Propose new features or improvements
- **Write Code**: Fix bugs, implement features, or improve performance
- **Improve Documentation**: Enhance README files, write tutorials, or fix typos
- **Write Tests**: Add test coverage or improve existing tests
- **Review Pull Requests**: Help review and test others' contributions
- **Answer Questions**: Help other users in GitHub Discussions or Issues

### Before You Start

1. **Search Existing Issues**: Check if your bug report or feature request already exists
2. **Check Roadmap**: Review the project roadmap to see if your idea aligns with project goals
3. **Discuss Major Changes**: For significant changes, open an issue first or submit an [OSEP](../../../README.md) to discuss your approach
4. **Review Architecture**: Read [docs/architecture.md](ARCHITECTURE.md) to understand the system design

## Development Environment Setup

### Prerequisites

Different components have different requirements:

#### For Server (Python)

- **Python 3.10+**
- **uv** - Python package manager ([installation guide](https://github.com/astral-sh/uv))
- **Docker** - For running sandboxes locally

#### For execd (Go)

- **Go 1.24+**
- **Make** - Build automation (optional)
- **Docker** - For building container images

#### For SDKs

- **Python SDK**: Python 3.10+, uv
- **Java/Kotlin SDK**: JDK 17+, Gradle

### Quick Setup

#### Server Development

```bash
# Navigate to server directory
cd server

# Install dependencies
uv sync

# Copy example configuration
cp example.config.toml ~/.sandbox.toml

# Edit configuration for development
# Set log_level = "DEBUG" and api_key
nano ~/.sandbox.toml

# Run server
uv run python -m src.main
```

See [server/DEVELOPMENT.md](../../../core/security/QUARANTINE/vetted/repos/llm_lean_log/docs/development.md) for detailed server development guide.

#### execd Development

```bash
# Navigate to execd directory
cd components/execd

# Download dependencies
go mod download

# Build execd
go build -o bin/execd .

# Run execd (requires Jupyter Server)
./bin/execd --jupyter-host=http://localhost:8888 --port=44772
```

See [components/execd/DEVELOPMENT.md](../../../core/security/QUARANTINE/vetted/repos/llm_lean_log/docs/development.md) for detailed execd development guide.

#### SDK Development

**Python SDK:**

```bash
cd sdks/sandbox/python
uv sync
uv run pytest
```

**Java/Kotlin SDK:**

```bash
cd sdks/sandbox/kotlin
./gradlew build
./gradlew test
```

## Project Structure

```
OpenSandbox/
├── sdks/                     # Multi-language SDKs
│   ├── code-interpreter/     # Code Interpreter SDK (Python, Kotlin)
│   └── sandbox/              # Sandbox base SDK (Python, Kotlin)
├── specs/                    # OpenAPI specifications
│   ├── execd-api.yaml        # Execution API spec
│   └── sandbox-lifecycle.yml # Lifecycle API spec
├── server/                   # Sandbox server (Python/FastAPI)
├── components/
│   └── execd/                # Execution daemon (Go/Beego)
├── sandboxes/                # Sandbox implementations
│   └── code-interpreter/     # Code Interpreter sandbox
├── examples/                 # Example integrations
├── docs/                     # Documentation
├── tests/                    # Cross-component tests
│   └── e2e/                  # End-to-end tests
└── scripts/                  # Build and utility scripts
```

## Development Workflow

### Enhancement Proposals (OSEP)

For major features, architectural changes, or modifications to the core API/security model, we follow the **OSEP (OpenSandbox Enhancement Proposals)** process.

Please read the [OSEP README](../../../README.md) to understand when an OSEP is required and how to submit one. Small bug fixes and minor improvements do not require an OSEP.

### Branching Strategy

- **main**: Stable production branch
- **feature/[name]**: New features
- **fix/[name]**: Bug fixes
- **docs/[name]**: Documentation updates
- **refactor/[name]**: Code refactoring
- **test/[name]**: Test additions or improvements

### Creating a Feature Branch

```bash
# Update main branch
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/my-awesome-feature

# Make your changes
# ...

# Commit your changes
git add .
git commit -m "feat: add my awesome feature"

# Push to your fork
git push origin feature/my-awesome-feature
```

### Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Build process, dependencies, or tooling changes
- `perf`: Performance improvements
- `ci`: CI/CD changes

**Examples:**

```
feat(server): add Kubernetes runtime support
fix(execd): resolve memory leak in session cleanup
docs(sdk): add Python SDK usage examples
test(server): add integration tests for Docker runtime
refactor(sdk): simplify filesystem API
```

### Making Changes

1. **Write Clean Code**: Follow project coding standards (see below)
2. **Add Tests**: Ensure your changes are covered by tests
3. **Update Documentation**: Update relevant documentation files
4. **Test Locally**: Run all tests and ensure they pass
5. **Check Linting**: Run linters and fix any issues

## Coding Standards

### Python (Server, Python SDKs)

- **Style Guide**: Follow [PEP 8](https://pep8.org/)
- **Formatter**: Use `ruff` for formatting and linting
- **Type Hints**: Always use type hints for function signatures
- **Docstrings**: Use Google-style docstrings for public APIs

```python
def create_sandbox(
    image: ImageSpec,
    timeout: timedelta,
    entrypoint: Optional[List[str]] = None
) -> Sandbox:
    """Create a new sandbox instance.

    Args:
        image: Container image specification
        timeout: Sandbox timeout duration
        entrypoint: Optional custom entrypoint command

    Returns:
        Created sandbox instance

    Raises:
        ValueError: If image or timeout is invalid
    """
    # Implementation
```

**Running Linter:**

```bash
cd server
uv run ruff check src tests
uv run ruff format src tests
```

### Go (execd)

- **Style Guide**: Follow [Effective Go](https://golang.org/doc/effective_go)
- **Formatter**: Use `gofmt` for formatting
- **Imports**: Organize in three groups (stdlib, third-party, internal)
- **Error Handling**: Always handle errors explicitly

```go
// Good
result, err := someOperation()
if err != nil {
    logs.Error("operation failed: %v", err)
    return fmt.Errorf("failed to do something: %w", err)
}

// Bad - silent failure
result, _ := someOperation()
```

**Running Formatter:**

```bash
cd components/execd
gofmt -w .
# Or
make fmt
```

### Java/Kotlin (Java/Kotlin SDKs)

- **Style Guide**: Follow [Kotlin Coding Conventions](https://kotlinlang.org/docs/coding-conventions.html)
- **Formatter**: Use `ktlint`
- **Null Safety**: Use Kotlin's null safety features

```kotlin
suspend fun createSandbox(
    image: ImageSpec,
    timeout: Duration,
    entrypoint: List<String>? = null
): Sandbox {
    // Implementation
}
```

### General Guidelines

- **Naming Conventions**:
  - Functions/Methods: `snake_case` (Python), `camelCase` (Go, Kotlin)
  - Classes: `PascalCase` (all languages)
  - Constants: `UPPER_SNAKE_CASE` (all languages)
  - Private members: `_leading_underscore` (Python), `unexported` (Go)

- **Comments**: Write clear, concise comments explaining "why", not "what"
- **Error Messages**: Provide actionable error messages with context
- **Logging**: Use appropriate log levels (DEBUG, INFO, WARNING, ERROR)

## Testing Guidelines

### Test Coverage Requirements

- **Core Packages**: Aim for >80% coverage
- **API Layer**: Aim for >70% coverage
- **Utilities**: Aim for >90% coverage

### Writing Tests

#### Python Tests (pytest)

```python
import pytest
from opensandbox import Sandbox

@pytest.mark.asyncio
async def test_create_sandbox():
    """Test sandbox creation with valid parameters."""
    sandbox = await Sandbox.create(
        image="python:3.11",
        timeout=timedelta(minutes=5)
    )
    assert sandbox.id is not None
    assert sandbox.status == SandboxStatus.PENDING
    await sandbox.kill()

@pytest.mark.asyncio
async def test_invalid_timeout():
    """Test sandbox creation fails with invalid timeout."""
    with pytest.raises(ValueError):
        await Sandbox.create(
            image="python:3.11",
            timeout=timedelta(seconds=-1)
        )
```

**Running Tests:**

```bash
cd server
uv run pytest
uv run pytest --cov=src --cov-report=html
```

#### Go Tests

```go
func TestController_Execute_Python(t *testing.T) {
    ctrl := NewController("http://localhost:8888", "test-token")

    req := &ExecuteCodeRequest{
        Language: Python,
        Code:     "print('hello')",
    }

    err := ctrl.Execute(req)
    assert.NoError(t, err)
}
```

**Running Tests:**

```bash
cd components/execd
go test ./pkg/...
go test -v -cover ./pkg/...
```

#### Integration Tests

Integration tests require Docker:

```bash
# Server integration tests
cd server
uv run pytest tests/integration/

# E2E tests
cd tests/e2e/python
uv run pytest
```

### Test Best Practices

- **Test Names**: Use descriptive names that explain what is being tested
- **Arrange-Act-Assert**: Structure tests clearly
- **Isolation**: Each test should be independent
- **Mocking**: Mock external dependencies appropriately
- **Cleanup**: Always clean up resources (use fixtures, context managers)

## Submitting Contributions

### Pull Request Process

1. **Create Feature Branch**: Branch from `main`
2. **Make Changes**: Implement your feature or fix
3. **Write Tests**: Add comprehensive test coverage
4. **Update Documentation**: Update relevant docs
5. **Test Locally**: Ensure all tests pass
6. **Run Linters**: Fix any style issues
7. **Commit Changes**: Use conventional commit messages
8. **Push to Fork**: Push your branch to your fork
9. **Create Pull Request**: Submit PR with detailed description

### Pull Request Template

When creating a PR, fill out the template:

```markdown
# Summary

- What is changing and why?

# Testing

- [ ] Not run (explain why)
- [ ] Unit tests
- [ ] Integration tests
- [ ] e2e / manual verification

# Breaking Changes

- [ ] None
- [ ] Yes (describe impact and migration path)

# Checklist

- [ ] Linked Issue or clearly described motivation
- [ ] Added/updated docs (if needed)
- [ ] Added/updated tests (if needed)
- [ ] Security impact considered
- [ ] Backward compatibility considered
```

### Pull Request Guidelines

**Do:**

- Keep PRs focused and reasonably sized (< 500 lines if possible)
- Write clear PR descriptions with motivation and context
- Link related issues
- Respond to review comments promptly
- Update your PR based on feedback
- Ensure CI passes before requesting review

**Don't:**

- Mix multiple unrelated changes in one PR
- Submit PRs with failing tests
- Ignore code review feedback
- Force push after reviews have started (unless necessary)
- Include commented-out code or debug statements

### Code Review Process

1. **Automated Checks**: CI runs tests, linters, and security scans
2. **Maintainer Review**: A maintainer reviews your code
3. **Feedback Loop**: Address review comments
4. **Approval**: Once approved, a maintainer will merge your PR
5. **Cleanup**: Delete your feature branch after merge

## Communication Channels

### GitHub Issues

Use GitHub Issues for:

- Bug reports
- Feature requests
- Documentation improvements
- Questions about implementation

**Bug Report Template:**

```markdown
**Description**
A clear description of the bug.

**To Reproduce**
Steps to reproduce the behavior:

1. Create sandbox with...
2. Execute command...
3. See error

**Expected Behavior**
What you expected to happen.

**Environment**

- OpenSandbox version:
- Runtime (Docker/K8s):
- OS:
- Python/Go version:

**Additional Context**
Logs, screenshots, or other relevant information.
```

### GitHub Discussions

Use GitHub Discussions for:

- General questions
- Design discussions
- Brainstorming ideas
- Community help

### Getting Help

- **Issues**: Technical problems or bugs
- **Discussions**: Questions and community support
- **Email**: For security issues, email conduct@opensandbox.io

## Additional Resources

### Documentation

- [Architecture Overview](ARCHITECTURE.md)
- [Server Development Guide](../../../core/security/QUARANTINE/vetted/repos/llm_lean_log/docs/development.md)
- [execd Development Guide](../../../core/security/QUARANTINE/vetted/repos/llm_lean_log/docs/development.md)
- [OpenAPI Specifications](../../../README.md)
- [Python SDK Documentation](../../../README.md)
- [Java/Kotlin SDK Documentation](../../../README.md)

### Examples

Browse [examples/](examples/) for real-world usage patterns:

- Code Interpreter integration
- AI Coding Agent integrations (Claude Code, Gemini CLI, etc.)
- Browser automation (Chrome, Playwright)
- Remote development (VS Code, Desktop)

### External Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Beego Documentation](https://beego.wiki/)
- [Jupyter Protocol](https://jupyter-client.readthedocs.io/en/stable/messaging.html)
- [OpenAPI Specification](https://swagger.io/specification/)
- [Docker API](https://docs.docker.com/engine/api/)

## Acknowledgments

Thank you for contributing to OpenSandbox! Your contributions help make this project better for everyone in the AI and developer tools community.

If you have suggestions for improving this contributing guide, please open an issue or submit a pull request.

## License

By contributing to OpenSandbox, you agree that your contributions will be licensed under the [Apache 2.0 License](LICENSE).
```

## File: `LICENSE`
```
Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `README.md`
```markdown
<div align="center">
  <img src="docs/assets/logo.svg" alt="OpenSandbox logo" width="150" />

  <h1>OpenSandbox</h1>

  <p align="center">
    <a href="https://trendshift.io/repositories/21828" target="_blank">
      <img src="https://trendshift.io/api/badge/repositories/21828" alt="alibaba%2FOpenSandbox | Trendshift" style="width: 320px; height: 70px;" width="320" height="70" />
    </a>
  </p>

<p align="center">
  <a href="https://github.com/alibaba/OpenSandbox">
    <img src="https://img.shields.io/github/stars/alibaba/OpenSandbox.svg?style=social" alt="GitHub stars" />
  </a>
  <a href="https://deepwiki.com/alibaba/OpenSandbox">
    <img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki" />
  </a>
  <a href="https://www.apache.org/licenses/LICENSE-2.0.html">
    <img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="license" />
  </a>
  <a href="https://badge.fury.io/py/opensandbox">
    <img src="https://badge.fury.io/py/opensandbox.svg" alt="PyPI version" />
  </a>
  <a href="https://badge.fury.io/js/@alibaba-group%2Fopensandbox">
    <img src="https://badge.fury.io/js/@alibaba-group%2Fopensandbox.svg" alt="npm version" />
  </a>
  <a href="https://qr.dingtalk.com/action/joingroup?code=v1,k1,A4Bgl5q1I1eNU/r33D18YFNrMY108aFF38V+r19RJOM=&_dt_no_comment=1&origin=11">
    <img src="https://img.shields.io/badge/DingTalk-Join-0089FF?logo=dingtalk&logoColor=white" alt="DingTalk" />
  </a>
  <a href="https://github.com/alibaba/OpenSandbox/actions">
    <img src="https://github.com/alibaba/OpenSandbox/actions/workflows/real-e2e.yml/badge.svg?branch=main" alt="E2E Status" />
  </a>
</p>

  <hr />
</div>

[Documentation](https://open-sandbox.ai/) | [中文文档](https://open-sandbox.ai/zh/)

OpenSandbox is a **general-purpose sandbox platform** for AI applications, offering multi-language SDKs, unified sandbox APIs, and Docker/Kubernetes runtimes for scenarios like Coding Agents, GUI Agents, Agent Evaluation, AI Code Execution, and RL Training.

## Features

- **Multi-language SDKs**: Provides sandbox SDKs in Python, Java/Kotlin, JavaScript/TypeScript, C#/.NET, Go (Roadmap), and more.
- **Sandbox Protocol**: Defines sandbox lifecycle management APIs and sandbox execution APIs so you can extend custom sandbox runtimes.
- **Sandbox Runtime**: Built-in lifecycle management supporting Docker and [high-performance Kubernetes runtime](./kubernetes), enabling both local runs and large-scale distributed scheduling.
- **Sandbox Environments**: Built-in Command, Filesystem, and Code Interpreter implementations. Examples cover Coding Agents (e.g., Claude Code), browser automation (Chrome, Playwright), and desktop environments (VNC, VS Code).
- **Network Policy**: Unified [Ingress Gateway](components/ingress) with multiple routing strategies plus per-sandbox [egress controls](components/egress).
- **Strong Isolation**: Supports secure container runtimes like gVisor, Kata Containers, and Firecracker microVM for enhanced isolation between sandbox workloads and the host. See [Secure Container Runtime Guide](docs/secure-container.md) for details.

## Examples

### Basic Sandbox Operations

Requirements:

- Docker (required for local execution)
- Python 3.10+ (recommended for examples and local runtime)

#### 1. Install and Configure the Sandbox Server

```bash
uv pip install opensandbox-server
opensandbox-server init-config ~/.sandbox.toml --example docker
```

> If you prefer working from source, you can still clone the repo for development, but you no longer need to clone this repository just to start the server.
>
> ```bash
> git clone https://github.com/alibaba/OpenSandbox.git
> cd OpenSandbox/server
> uv sync
> cp example.config.toml ~/.sandbox.toml # Copy configuration file
> uv run python -m src.main # Start the service
> ```

#### 2. Start the Sandbox Server

```bash
opensandbox-server

# Show help
opensandbox-server -h
```

#### 3. Create a Code Interpreter and Execute Commands

Install the Code Interpreter SDK

```bash
uv pip install opensandbox-code-interpreter
```

Create a sandbox and execute commands

```python
import asyncio
from datetime import timedelta

from code_interpreter import CodeInterpreter, SupportedLanguage
from opensandbox import Sandbox
from opensandbox.models import WriteEntry

async def main() -> None:
    # 1. Create a sandbox
    sandbox = await Sandbox.create(
        "opensandbox/code-interpreter:v1.0.2",
        entrypoint=["/opt/opensandbox/code-interpreter.sh"],
        env={"PYTHON_VERSION": "3.11"},
        timeout=timedelta(minutes=10),
    )

    async with sandbox:

        # 2. Execute a shell command
        execution = await sandbox.commands.run("echo 'Hello OpenSandbox!'")
        print(execution.logs.stdout[0].text)

        # 3. Write a file
        await sandbox.files.write_files([
            WriteEntry(path="/tmp/hello.txt", data="Hello World", mode=644)
        ])

        # 4. Read a file
        content = await sandbox.files.read_file("/tmp/hello.txt")
        print(f"Content: {content}") # Content: Hello World

        # 5. Create a code interpreter
        interpreter = await CodeInterpreter.create(sandbox)

        # 6. Execute Python code (single-run, pass language directly)
        result = await interpreter.codes.run(
              """
                  import sys
                  print(sys.version)
                  result = 2 + 2
                  result
              """,
              language=SupportedLanguage.PYTHON,
        )

        print(result.result[0].text) # 4
        print(result.logs.stdout[0].text) # 3.11.14

    # 7. Cleanup the sandbox
    await sandbox.kill()

if __name__ == "__main__":
    asyncio.run(main())
```

### More Examples

OpenSandbox provides examples covering SDK usage, agent integrations, browser automation, and training workloads. All example code is located in the `examples/` directory.

#### 🎯 Basic Examples

- **[code-interpreter](../../../README.md)** - End-to-end Code Interpreter SDK workflow in a sandbox.
- **[aio-sandbox](../../../README.md)** - All-in-One sandbox setup using the OpenSandbox SDK.
- **[agent-sandbox](../../../README.md)** - Example integration for running OpenSandbox workloads on Kubernetes with [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox).

#### 🤖 Coding Agent Integrations

- **[claude-code](../../../README.md)** - Run Claude Code inside OpenSandbox.
- **[gemini-cli](../../../README.md)** - Run Google Gemini CLI inside OpenSandbox.
- **[codex-cli](../../../README.md)** - Run OpenAI Codex CLI inside OpenSandbox.
- **[kimi-cli](../../../README.md)** - Run [Kimi CLI](https://github.com/MoonshotAI/kimi-cli) (Moonshot AI) inside OpenSandbox.
- **[iflow-cli](../../../README.md)** - Run iFLow CLI inside OpenSandbox.
- **[langgraph](../../../README.md)** - LangGraph state-machine workflow that creates/runs a sandbox job with fallback retry.
- **[google-adk](../../../README.md)** - Google ADK agent using OpenSandbox tools to write/read files and run commands.
- **[nullclaw](../../../README.md)** - Launch a [Nullclaw](https://github.com/nullclaw/nullclaw) Gateway inside a sandbox.
- **[openclaw](../../../README.md)** - Launch an OpenClaw Gateway inside a sandbox.

#### 🌐 Browser and Desktop Environments

- **[chrome](../../../README.md)** - Chromium sandbox with VNC and DevTools access for automation and debugging.
- **[playwright](../../../README.md)** - Playwright + Chromium headless scraping and testing example.
- **[desktop](../../../README.md)** - Full desktop environment in a sandbox with VNC access.
- **[vscode](../../../README.md)** - code-server (VS Code Web) running inside a sandbox for remote dev.

#### 🧠 ML and Training

- **[rl-training](../../../README.md)** - DQN CartPole training in a sandbox with checkpoints and summary output.

For more details, please refer to [examples](../../../README.md) and the README files in each example directory.

## Project Structure

| Directory | Description                                                      |
|-----------|------------------------------------------------------------------|
| [`sdks/`](sdks/) | Multi-language SDKs (Python, Java/Kotlin, TypeScript/JavaScript, C#/.NET) |
| [`specs/`](../../../README.md) | OpenAPI specs and lifecycle specifications                      |
| [`server/`](../../../README.md) | Python FastAPI sandbox lifecycle server                          |
| [`kubernetes/`](../../../README.md) | Kubernetes deployment and examples                               |
| [`components/execd/`](../../../README.md) | Sandbox execution daemon (commands and file operations)          |
| [`components/ingress/`](../../../README.md) | Sandbox traffic ingress proxy                                    |
| [`components/egress/`](../../../README.md) | Sandbox network egress control                                   |
| [`sandboxes/`](sandboxes/) | Runtime sandbox implementations                                   |
| [`examples/`](../../../README.md) | Integration examples and use cases                               |
| [`oseps/`](../../../README.md) | OpenSandbox Enhancement Proposals                                |
| [`docs/`](docs/) | Architecture and design documentation                            |
| [`tests/`](tests/) | Cross-component E2E tests                                        |
| [`scripts/`](scripts/) | Development and maintenance scripts                              |

For detailed architecture, see [docs/architecture.md](ARCHITECTURE.md).

## Documentation

- [docs/architecture.md](ARCHITECTURE.md) – Overall architecture & design philosophy
- [oseps/README.md](../../../README.md) – OpenSandbox Enhancement Proposals
- SDK
  - Sandbox base SDK ([Java/Kotlin SDK](../../../README.md), [Python SDK](../../../README.md), [JavaScript/TypeScript SDK](../../../README.md), [C#/.NET SDK](../../../README.md)) - includes sandbox lifecycle, command execution, file operations
  - Code Interpreter SDK ([Java/Kotlin SDK](../../../README.md), [Python SDK](../../../README.md), [JavaScript/TypeScript SDK](../../../README.md), [C#/.NET SDK](../../../README.md)) - code interpreter
- [specs/README.md](../../../README.md) - OpenAPI definitions for sandbox lifecycle API and sandbox execution API
- [server/README.md](../../../README.md) - Sandbox server startup and configuration; supports Docker and Kubernetes runtimes

## License

This project is open source under the [Apache 2.0 License](LICENSE).

## Roadmap [2026.03]

### SDK

- **Sandbox client connection pool** - Client-side sandbox connection pool management, providing pre-provisioned sandboxes to obtain an environment at X ms.
- **Go SDK** - Go client SDK for sandbox lifecycle management, command execution, and file operations.

### Sandbox Runtime

- **Persistent volumes** - Mountable persistent volumes for sandboxes (see [Proposal 0003](oseps/0003-volume-and-volumebinding-support.md)).
- **Local lightweight sandbox** - Lightweight sandbox for AI tools running directly on PCs.
- **Secure Container** - Secure sandbox for AI Agents running inside container.

### Deployment

- **Guide** - Deployment guide for self-hosted Kubernetes cluster.

## Contact and Discussion

- Issues: Submit bugs, feature requests, or design discussions through GitHub Issues
- DingTalk: Join the [OpenSandbox technical discussion group](https://qr.dingtalk.com/action/joingroup?code=v1,k1,A4Bgl5q1I1eNU/r33D18YFNrMY108aFF38V+r19RJOM=&_dt_no_comment=1&origin=11)
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=alibaba/OpenSandbox&type=date&legend=top-left)](https://www.star-history.com/#alibaba/OpenSandbox&type=date&legend=top-left)
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Reporting Security Issues

The OpenSandbox team takes security seriously. If you discover a security vulnerability, please report it responsibly.

### How to Report

- **GitHub Security Advisories**: Open a private security advisory on GitHub
- **Email**: Contact the maintainers directly with "[SECURITY]" in the subject

### What to Include

- Clear description of the vulnerability
- Steps to reproduce
- Potential impact and scope
- Suggested remediation (if available)

## Response Process

1. Acknowledgment within 48 hours
2. Investigation and validation
3. Fix development and testing
4. Coordinated disclosure

## Supported Versions

Only the latest release and main branch are actively supported with security updates.

## Security Best Practices

When deploying OpenSandbox:
- Keep dependencies up to date
- Use network policies to restrict sandbox egress
- Monitor audit logs regularly
- Follow principle of least privilege
```

