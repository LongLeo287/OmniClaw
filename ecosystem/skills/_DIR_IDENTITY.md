---
id: ecosystem_skills_domain
name: Skills Ecosystem Domain
path: ecosystem/skills
type: directory_identity
---

# Skills Ecosystem Domain

Knowledge base domain: OmniClaw Ecosystem Skills.
(Bilingual Core Daemon standard enforced, strictly English terminology for machine interoperability)

This directory serves as the definitive registry and operational warehouse for all **1,932 integrated Agent Skills** (Competency Profiles) within the OmniClaw infrastructure. Every folder inside acts as an isolated, passive memory block that can be assimilated dynamically by the Core Daemons.

## Subsystem Architecture (Zero-Trust Storage)
Like the `plugins` ecosystem, this zone is strictly "Cold Storage". It does not execute live code or arbitrary background services. Execution is governed dynamically via Harbor Context Loading.

## Naming Standards 
- `snake_case` enforced across all files and folders. Kebab-case (`-`) is strictly forbidden and constitutes a system violation.

## Skill Declaration
All capabilities are logged structurally in the `SKILL_REGISTRY.json` map file, which is automatically compiled via the Assimilation Pipeline.
Local components run standard markdown metadata frontmatter containing execution boundaries outlined in `SKILL_SPEC.md`.