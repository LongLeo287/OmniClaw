# GitHub Copilot Instructions: Agent Skills Expert (SwiftUI)

Review changes as an **Agent Skills expert**, focusing on the **Agent Skills open format** specification and ensuring this repository stays a **SwiftUI-focused, non-architectural, modern-API** skill.

## Core Agent Skills Principles

### Format Compliance
- **`SKILL.md` required**: Every skill directory must contain a `SKILL.md` with YAML frontmatter.
- **YAML frontmatter requirements**:
  - **`name`**: non-empty, **<= 64 chars**, **lowercase letters/numbers/hyphens only**.
  - **`description`**: non-empty, **<= 1024 chars**, clearly states **what the skill does** and **when to use it**.
- **Progressive disclosure**: keep `SKILL.md` as the primary entrypoint; move deep dives into `swiftui-expert-skill/references/`.
- **Filesystem-based design**: content should be organized so agents can load only what they need (metadata → instructions → references).

### Skill Content Organization (Progressive Disclosure)

**Level 1: Metadata (always loaded)**
- YAML frontmatter should be concise and trigger-relevant.

**Level 2: Instructions (loaded when triggered)**
- `swiftui-expert-skill/SKILL.md` body should contain workflows, checklists, decision trees, and quick references.
- Avoid turning `SKILL.md` into an encyclopedia; prefer linking out to references.

**Level 3: Resources (loaded as needed)**
- Topic-specific guidance lives in `swiftui-expert-skill/references/*.md`.
- References should be linked from `SKILL.md` so agents discover them naturally.

## SwiftUI Repository Constraints (Keep This Skill “On Mission”)
- **SwiftUI-only**: avoid UIKit patterns unless bridging is strictly necessary, and avoid server-side Swift.
- **No architecture mandates**: do not prescribe MVVM/MVC/VIPER/coordinators/routers or project folder structures.
- **No tooling instructions**: avoid IDE/tool walkthroughs. (Mentioning that profiling exists is fine; don’t give step-by-step tool instructions.)
- **Modern SwiftUI APIs**: prefer modern, non-deprecated APIs where correctness is impacted (e.g., `NavigationStack`, `foregroundStyle()`).
- **Performance guidance is optional**: performance optimizations should be phrased as “consider” unless it’s a correctness issue.

## This Is a Skill, Not a Codebase

Code examples in this repository are **reference patterns for AI agents**, not compilable sample code for human developers. When reviewing:

- **Do not flag "incomplete" snippets.** Examples intentionally omit surrounding struct/class context, imports, and boilerplate. An AI agent understands `@StateObject private var viewModel = MyViewModel()` without needing `MyViewModel` defined.
- **Do not request "copy-pasteable" or "self-contained" examples.** Every extra line of boilerplate burns tokens in the agent's context window. Conciseness is a feature, not a bug.
- **Do not flag force-unwraps or missing error handling in examples.** These are pattern demonstrations, not production code. The agent will add appropriate error handling when applying the pattern to real code.
- **Do flag genuinely incorrect syntax or misleading API usage.** If an example uses a non-existent API or wrong parameter name, that's a real issue -- the agent would produce wrong code.
- **Do flag factual inaccuracies** (wrong iOS version requirements, incorrect deprecation claims, etc.).

## Review Focus Areas

1. **Description Quality**
   - Does the description say **what the skill does** and **when to use it** (trigger conditions)?
   - Is it specific enough to be selected over other skills?

2. **Instruction Clarity**
   - Are instructions actionable (checklists, decision trees, “review/improve/implement” flows)?
   - Are examples correct SwiftUI and consistent with the stated constraints?

3. **Progressive Disclosure**
   - Is `SKILL.md` focused (not duplicating large reference content)?
   - Are deeper topics moved into `references/` and linked appropriately?

4. **SwiftUI Correctness and Modernity**
   - Modern API replacements are accurate and not misleading.
   - Guidance around lists/identity, sheets/navigation, and state wrappers is correct.
   - iOS 26+ / Liquid Glass guidance includes **availability gating** and sensible fallbacks.

5. **Safety / Security (for automation & scripts)**
   - GitHub Actions and scripts should avoid surprising network behavior and avoid writing outside the repo.
   - Dependencies should be minimal and justified.

## Common Issues to Flag
- **Missing/invalid YAML frontmatter** in `SKILL.md`.
- **Invalid `name`** (uppercase, underscores, spaces, too long).
- **Vague `description`** (“helps with SwiftUI”) without clear trigger conditions.
- **Overlong `SKILL.md`** that repeats reference content instead of linking to it.
- **Unlinked references** in `swiftui-expert-skill/references/` that aren’t discoverable from `SKILL.md`.
- **Architecture prescriptions** or project-structure mandates.
- **Tooling walkthroughs** (IDE-specific or step-by-step tool usage).
- **Non-SwiftUI deep dives** (general Swift language/concurrency tutorials unrelated to SwiftUI usage).

## Resources
- Agent Skills overview: https://agentskills.io/home
- Agent Skills docs: https://docs.anthropic.com/en/docs/claude-code/agent-skills
- Claude Platform docs (Agent Skills): https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- SwiftUI docs: https://developer.apple.com/documentation/swiftui

---

**Remember**: You are reviewing as an Agent Skills expert. Prioritize format compliance, progressive disclosure, SwiftUI accuracy, and keeping guidance modern and non-prescriptive.
