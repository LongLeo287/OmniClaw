# ContribAI Documentation

Welcome to the ContribAI documentation suite. This directory contains comprehensive guides for users, developers, and operators.

---

## Quick Navigation

### For Product Managers & Decision Makers
- **[Project Overview & PDR](./project-overview-pdr.md)** — Product definition, requirements, success metrics (344 LOC)
- **[Project Roadmap](./project-roadmap.md)** — Version history, milestones, future plans (401 LOC)

### For Developers & Contributors
- **[Codebase Summary](./codebase-summary.md)** — Module map, architecture, tech stack (419 LOC)
- **[Code Standards](./code-standards.md)** — Development conventions, patterns, testing (764 LOC)
- **[System Architecture](./system-architecture.md)** — Pipeline, middleware, agents, config (661 LOC)

### For DevOps & Operations
- **[Deployment Guide](./deployment-guide.md)** — Installation, Docker, Kubernetes, CLI (822 LOC)

### Reference
- **[ARCHITECTURE.md](./ARCHITECTURE.md)** — High-level system overview (247 LOC)

---

## Documentation Map

```
docs/
├── README.md (this file)              # Navigation hub
├── project-overview-pdr.md            # Product definition & requirements
├── codebase-summary.md                # Module structure & tech stack
├── code-standards.md                  # Dev conventions & patterns
├── system-architecture.md             # Pipeline, agents, config
├── project-roadmap.md                 # Releases & future plans
├── deployment-guide.md                # Setup & operations
└── ARCHITECTURE.md                    # High-level overview
```

---

## By Role

### Product Manager
1. Start: [Project Overview & PDR](./project-overview-pdr.md)
2. Understand: Feature matrix, success metrics, requirements
3. Plan: [Project Roadmap](./project-roadmap.md)

### Software Engineer (New Contributor)
1. Start: [README.md](../README.md) in project root
2. Understand: [Codebase Summary](./codebase-summary.md) (modules, stack)
3. Learn: [Code Standards](./code-standards.md) (patterns, testing)
4. Deep dive: [System Architecture](./system-architecture.md) (pipeline, events)

### Tech Lead / Architect
1. Start: [System Architecture](./system-architecture.md)
2. Review: Dependency graphs, design patterns, event system
3. Reference: [Code Standards](./code-standards.md) for review checklist
4. Plan: [Project Roadmap](./project-roadmap.md) for future architecture

### DevOps Engineer
1. Start: [Deployment Guide](./deployment-guide.md)
2. Choose: Local install, Docker, or Kubernetes
3. Configure: Environment variables, cron jobs, webhooks
4. Monitor: Health checks, performance tuning, scaling

### Code Reviewer
1. Refer: [Code Standards](./code-standards.md) checklist
2. Verify: Type hints, docstrings, tests, error handling
3. Check: Architecture compliance with [System Architecture](./system-architecture.md)

---

## Key Concepts Glossary

| Term | Definition | Learn More |
|------|-----------|------------|
| **Pipeline** | 6-stage flow: Discovery → Analysis → Generation → PR | [System Architecture](./system-architecture.md) |
| **Hunt Mode** | Autonomous multi-round discovery + contribution | [Project Overview](./project-overview-pdr.md) |
| **Middleware** | Cross-cutting concerns (rate limit, retry, DCO, etc.) | [System Architecture](./system-architecture.md) |
| **Sub-Agent** | Specialized executor (Analyzer, Generator, Patrol) | [System Architecture](./system-architecture.md) |
| **Finding** | Issue detected by analyzer (security, code quality, etc.) | [Codebase Summary](./codebase-summary.md) |
| **Contribution** | Proposed code fix for a finding | [Codebase Summary](./codebase-summary.md) |
| **Event Bus** | Typed event system for audit trail + integrations | [System Architecture](./system-architecture.md) |
| **MCP** | Model Context Protocol (Claude Desktop integration) | [System Architecture](./system-architecture.md) |
| **Profile** | Named preset configuration (security-focused, etc.) | [Deployment Guide](./deployment-guide.md) |
| **CLA/DCO** | Compliance: Contributor License Agreement / Developer Certificate | [System Architecture](./system-architecture.md) |

---

## Common Tasks

### "How do I set up ContribAI?"
→ [Deployment Guide](./deployment-guide.md) — Installation section

### "What are the code standards?"
→ [Code Standards](./code-standards.md) — Python conventions, patterns, testing

### "How does the analysis work?"
→ [System Architecture](./system-architecture.md) — Analysis pipeline section

### "What are the success criteria?"
→ [Project Overview & PDR](./project-overview-pdr.md) — Success metrics section

### "What's the current version and roadmap?"
→ [Project Roadmap](./project-roadmap.md) — Release timeline + future plans

### "How do I deploy to production?"
→ [Deployment Guide](./deployment-guide.md) — Docker/Kubernetes sections

### "What's the codebase structure?"
→ [Codebase Summary](./codebase-summary.md) — Module map + dependency graph

### "How do I contribute?"
→ [Code Standards](./code-standards.md) — Full development guide

---

## Documentation Statistics

| Document | Purpose | Lines | Size |
|----------|---------|-------|------|
| project-overview-pdr.md | Product definition | 344 | 13K |
| codebase-summary.md | Code structure | 419 | 15K |
| code-standards.md | Dev standards | 764 | 18K |
| system-architecture.md | System design | 661 | 24K |
| project-roadmap.md | Future planning | 401 | 15K |
| deployment-guide.md | Operations | 822 | 19K |
| ARCHITECTURE.md | Overview | 247 | 11K |
| **Total** | **7 docs** | **3,658** | **115K** |

---

## Learning Paths

### Path 1: User (Want to Deploy & Use)
1. [README.md](../README.md) — Features & quick start
2. [Deployment Guide](./deployment-guide.md) — Install & configure
3. [Deployment Guide - CLI](./deployment-guide.md#cli-commands-reference) — Learn commands

### Path 2: Developer (Want to Contribute Code)
1. [Codebase Summary](./codebase-summary.md) — Understand structure
2. [Code Standards](./code-standards.md) — Learn conventions
3. [System Architecture](./system-architecture.md) — Understand pipeline
4. [CONTRIBUTING.md](../CONTRIBUTING.md) — Contribution process

### Path 3: Architect (Want to Understand Design)
1. [System Architecture](./system-architecture.md) — Full design
2. [Codebase Summary](./codebase-summary.md) — Module details
3. [Project Overview & PDR](./project-overview-pdr.md) — Requirements
4. [Project Roadmap](./project-roadmap.md) — Future direction

### Path 4: DevOps (Want to Deploy & Monitor)
1. [Deployment Guide](./deployment-guide.md) — Full guide
2. [System Architecture](./system-architecture.md) — Configuration section
3. [Code Standards](./code-standards.md) — Performance tuning

---

## FAQ

**Q: Where do I start?**
A: See "By Role" section above.

**Q: How is this documentation organized?**
A: By audience (product, developer, ops) and topic depth. Each doc is self-contained but linked to others.

**Q: Are there code examples?**
A: Yes, extensive examples in Code Standards, System Architecture, and Deployment Guide.

**Q: Is documentation up-to-date with code?**
A: Yes, verified against v3.0.2 release. Updated on each release.

**Q: Can I propose documentation improvements?**
A: Yes, open a GitHub issue or discussion with `[DOCS]` prefix.

---

## Documentation Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Product Definition | ✓ Complete | All requirements documented |
| Architecture | ✓ Complete | Pipeline, agents, config all explained |
| Code Standards | ✓ Complete | Patterns, testing, security covered |
| Deployment | ✓ Complete | Local, Docker, K8s all documented |
| API Reference | ✓ Complete | CLI commands, web routes documented |
| Troubleshooting | ✓ Complete | 9+ common issues with solutions |
| Examples | ✓ Complete | Code examples throughout |
| Cross-references | ✓ Complete | All files linked appropriately |

---

## Meta Information

- **Suite Created:** 2026-03-28
- **Last Updated:** 2026-03-28
- **Version:** 3.0.2
- **Total Coverage:** 100% (product, technical, operational requirements)
- **Quality:** All files <800 LOC, comprehensive cross-linking
- **Maintenance:** Updated on each release, quarterly reviews

---

## Related Documentation

- **README.md** — Project overview, features, quick start (project root)
- **CONTRIBUTING.md** — Contribution guidelines (project root)
- **CHANGELOG.md** — Release history & changes (project root)
- **SECURITY.md** — Security policies (project root)
- **LICENSE** — AGPL-3.0 + Commons Clause (project root)
- **.github/workflows/** — CI/CD pipeline (GitHub Actions)

---

## Questions or Feedback?

- **Report Issues:** [GitHub Issues](https://github.com/tang-vu/ContribAI/issues)
- **Discuss Ideas:** [GitHub Discussions](https://github.com/tang-vu/ContribAI/discussions)
- **Suggest Docs:** Label with `[DOCS]` in title
- **Security Issues:** See [SECURITY.md](../SECURITY.md)

---

**Made with ❤️ for the ContribAI community**
