# Contributing

Welcome! We're excited that you want to contribute to Lawvable. This guide will walk you through our streamlined contribution process.

**Important:** We take security seriously. All submissions are carefully reviewed to ensure they don't expose users to data risks or malicious code. Advanced tools may take additional time to review.

> [!IMPORTANT] 
> Due to resource limitations, you may experience some delays in getting a review from a maintainer. We appreciate your patience.

## How to Submit a Skill

It's easy! Just click the link below and fill out the form. No Git knowledge required.

<a href="https://github.com/lawvable/awesome-legal-skills/issues/new?template=submit-skill.yml">
  <h3 align="center">🚀 Submit a new Skill here!</h1>
</a>

## Before You Start

- Ensure your skill is based on a **real use case**, not a hypothetical scenario
- Search existing skills to avoid duplicates
- Verify your skill works on at least one platform (Claude.ai, Claude Code, etc.)
- If inspired by someone's workflow, prepare to give attribution

## Skill Authoring

Every skill lives in a folder with a lowercase, hyphen-separated name:

```
skill-name/
├── SKILL.md          # Required: instructions with YAML frontmatter
├── scripts/          # Optional: helper scripts
├── templates/        # Optional: document templates
└── resources/        # Optional: reference materials
```

We strongly recommend using the [**skill-creator**](https://github.com/anthropics/skill-creator) meta-skill, which comes pre-installed with many agents, to guide you through the process from start to finish. It enforces good practices around structure, progressive disclosure, and SKILL.md quality - so you don't have to remember all the rules yourself. Just ask your agent to create a new skill and it will take it from there.

Once you've gone through a few rounds of iteration, do a **final review pass**: ask the AI agent to verify that the finished skill satisfies all the guidelines set out in the skill-creator skill. This catches things like missing frontmatter fields, overly long SKILL.md files, or resources that should have been split into separate reference files.

For an extensive and well-written guide on what makes a great skill, have a look at Anthropic's official [Best Practices for Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

## Questions?

Open an [issue](https://github.com/lawvable/awesome-legal-skills/issues) for help. Please be respectful and credit original sources.
