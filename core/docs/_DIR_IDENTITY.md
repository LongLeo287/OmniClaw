---
id: core-docs
name: OmniClaw Documentation
path: core/docs
type: directory_identity
owner: OMA
tier: public
language: [en, vn]
---

# core/docs — OmniClaw Documentation Hub

**Front door for all human-readable documentation.**

Every primary document in this directory exists in 2 versions:
- `<filename>.md` — English (primary, system standard)
- `<filename>-vn.md` — Vietnamese (human-facing translation)

## Structure
```
core/docs/
├── README.md              ← Entry point (EN)
├── README-vn.md           ← Entry point (VN)
├── _DIR_IDENTITY.md       ← This file
├── architecture/          ← System architecture docs
│   ├── system_overview.md / system_overview-vn.md
│   ├── plugin_architecture.md / plugin_architecture-vn.md
│   ├── CORE_PRINCIPLES.md / CORE_PRINCIPLES-vn.md
│   ├── CORE_DAEMONS_AND_OER.md / CORE_DAEMONS_AND_OER-vn.md
│   ├── OAP_ARCHITECTURE.md / OAP_ARCHITECTURE-vn.md
│   ├── OA_CHARTER.md / OA_CHARTER-vn.md
│   ├── OER_CHARTER.md / OER_CHARTER-vn.md
│   └── SKILLS_AND_PLUGINS_MAP.md / SKILLS_AND_PLUGINS_MAP-vn.md
├── usage_guides/          ← How-to guides
│   ├── getting_started.md / getting_started-vn.md
│   ├── agent_commands.md / agent_commands-vn.md
│   ├── ACTIVATION_GUIDE.md / ACTIVATION_GUIDE-vn.md
│   ├── DATA_SCIENCE_LIBRARY.md / DATA_SCIENCE_LIBRARY-vn.md
│   └── figma_mcp_usage.md / figma_mcp_usage-vn.md
└── workflows/             ← Operational SOPs
    ├── data_intake.md / data_intake-vn.md
    ├── data_packaging_sync.md / data_packaging_sync-vn.md
    ├── deep_cleaner.md / deep_cleaner-vn.md
    └── oiw_daemon.md / oiw_daemon-vn.md
```

## Rules
- ✅ Human-readable `.md` docs only.
- ✅ Every doc MUST have both EN (primary) + VN (translation) version.
- ❌ No scripts, no `.py`, no `.json` data files.
- ❌ No subdirectory that mirrors a root OmniClaw path.
