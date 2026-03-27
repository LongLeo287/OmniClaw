---
source: https://github.com/agentskills/agentskills
ingested_at: 2026-03-16T10:11:00+07:00
domain: AI|Architecture|AgentSkills|Standard
trust_level: HIGH
vet_status: PASS
tags: [agent-skills, open-standard, skill-format, copilot, claude, ai-agents, specification]
---

# Agent Skills — Open Standard Specification

**Repo:** https://github.com/agentskills/agentskills  
**Type:** Open standard + specification (không phải framework)  
**Supports:** GitHub Copilot, Anthropic Claude, OpenAI Codex, + any compatible agent

> ⚡ **AI OS đang implement standard này** — `skills/` và `plugins/` trong AI OS follow spec này.

---

## Tổng quan

Agent Skills = **open format để extend khả năng của AI agents**.

- Không phải plugin system độc quyền
- Không phải chatbot framework
- Là **chuẩn mở** để viết skills 1 lần, dùng cho nhiều agents khác nhau

**Analogy:** Như npm packages nhưng cho AI agent capabilities.

---

## Core Architecture: Folder-Based Skills

```
.agents/
└── skills/
    ├── my-skill/
    │   ├── SKILL.md          ← bắt buộc (entry point)
    │   ├── scripts/
    │   │   └── run.ps1       ← scripts tham chiếu từ SKILL.md
    │   ├── examples/
    │   │   └── example.md
    │   └── resources/
    │       └── config.json
    └── another-skill/
        └── SKILL.md
```

### `SKILL.md` — Core File

```markdown
---
name: skill-name
description: Khi nào activate skill này (agent dùng để quyết định)
version: 1.0.0
tier: 1|2|3
---

# Skill Instructions

Chi tiết instructions cho agent khi skill được load.

## Usage
Hướng dẫn cụ thể...

## Scripts
Tham chiếu scripts: `scripts/run.ps1`
```

**Quan trọng:** `description` = trigger condition — agent đọc để quyết định có load skill không.

---

## Skill Locations (Scope)

| Location | Scope | Ví dụ path |
|----------|-------|------------|
| **Project Skills** | Chỉ trong repo đó | `.github/skills/`, `.claude/skills/`, `.agents/skills/` |
| **Personal Skills** | Tất cả projects của user | `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/` |
| **System Skills** | Admin/SDK level | System-wide shared location |

> AI OS dùng: `<AI_OS_ROOT>\skills\` (project-level) + `<AI_OS_ROOT>\plugins\` (plugin-level)

---

## Key Features

### 1. Dynamic + On-Demand Loading
```
User prompt → Agent phân tích → Tìm relevant skills → Load SKILL.md + resources
```
- Chỉ load khi cần → **tiết kiệm context window**
- "Progressive disclosure" — thông tin được reveal dần theo nhu cầu
- Tránh token waste khi load toàn bộ skills cùng lúc

### 2. Rich Content Bundling
Skills có thể chứa:
- ✅ Detailed instructions (SKILL.md)
- ✅ Executable scripts (PowerShell, Python, bash)
- ✅ Code examples
- ✅ Documentation/templates
- ✅ Images + media resources
- ✅ Configuration files

### 3. Portability
- Skill viết cho Claude → dùng được với Copilot (nếu spec-compliant)
- Không phụ thuộc vào 1 vendor
- Community-shareable

### 4. Clear Separation
| | Agent Skills | Custom Instructions |
|---|---|---|
| **Scope** | Specialized capability | General behavior/coding style |
| **Content** | Instructions + scripts + resources | Text instructions only |
| **Loading** | Dynamic, on-demand | Always loaded |
| **Executable** | Có (scripts) | Không |

---

## AI OS Implementation vs. Spec

AI OS đang implement standard này với một số extensions:

| Spec | AI OS Implementation |
|------|---------------------|
| `SKILL.md` | ✅ Dùng đúng |
| `name`, `description` frontmatter | ✅ Dùng thêm `tier`, `version`, `tags`, `dependencies` |
| Folder-based | ✅ `skills/` + `plugins/` |
| Dynamic loading | ✅ `skill_loader.ps1` + `SKILL_REGISTRY.json` |
| Project scope | ✅ AI OS-level skills |
| Personal scope | Chưa implement (planned) |
| Portability | Partial — optimized cho Claude |

### AI OS Tier System (Extension)
```
Tier 1: Eager — load ngay khi boot (context_manager, reasoning_engine...)
Tier 2: Lazy  — load on-demand khi relevant
Tier 3: Manual — chỉ load khi user yêu cầu explicit
```

---

## Patterns học được

### Pattern 1: Skill Discovery Protocol
```
1. Scan skill folders → đọc SKILL.md frontmatter (chỉ metadata)
2. Build index với name + description
3. Khi user prompt → match prompt với descriptions
4. Load full SKILL.md + resources của matched skills
5. Inject vào agent context
```

### Pattern 2: Skill Composition
```
# SKILL.md có thể reference skill khác
dependencies:
  - base-reasoning
  - context-manager
```

### Pattern 3: Community Skills
```
Sources:
- Official: github.com/agentskills/agentskills/skills/
- Community: Contributed by users
- AI OS: <AI_OS_ROOT>\skills\ + plugins\
```

---

## Compatibility Matrix

| Agent | Support |
|-------|---------|
| GitHub Copilot (VS Code) | ✅ Native |
| Copilot CLI | ✅ Native |
| Claude (Anthropic) | ✅ Native |
| OpenAI Codex | ✅ Native |
| Antigravity (AI OS) | ✅ Via AI OS implementation |
| Custom agents | ✅ Via spec compliance |

---

## References
- [GitHub Spec Repo](https://github.com/agentskills/agentskills)
- [GitHub Copilot Skills Docs](https://docs.github.com/copilot/skills)
- [Community Skills Hub](https://github.com/agentskills)
