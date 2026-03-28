# 🛠️ Contributing to AI OS CORP Ecosystem

*Đọc bản [Tiếng Việt (Vietnamese version) tại đây](CONTRIBUTING_vi.md).*

> **"Code is Law. Security is the Foundation."**
> — AI OS ENGINEERING DIRECTIVE

Thank you for considering contributing to the AI OS CORP ecosystem! Whether you are a Human Engineer, an AI Researcher, or an Autonomous Agent, your contributions are what make AI OS a robust, professional, and scalable operating system.

Before submitting any Pull Request (PR) or committing code, you **MUST** read and abide by the following organizational guidelines.

---

## 🛡️ The Zero-Trust Policy (MANDATORY)

AI OS operates on a Strict Zero-Trust Architecture. All incoming code is scrutinized automatically by the Content Intake and Vetting (CIV) pipeline and GitHub Actions.

1. **NO Hardcoded Credentials:** Never commit API keys, tokens, passwords, or `.env` secrets. Automated CodeQL scanners will immediately detect and block the leak, and the PR will be rejected. Use `$env:KEY_NAME` or `process.env`.
2. **NO Absolute Machine Paths:** AI OS must be 100% portable. Never write code that expects `C:\Users\John\...` or `/Users/Mac/...`. Always use relative paths (`./scripts`) or environment variables indicating the root directory (e.g., `<AI_OS_ROOT>`).
3. **DO NOT Trust External Inputs:** If your code fetches data or clones a third-party repo, it must run through the AI OS CIV Security Quarantine first. Do not blindly execute foreign scripts.

---

## 🚀 How to Contribute

To maintain a clean and reliable codebase, follow the standard Git Flow:

1. **Fork the Repository:** Create a copy of the AI OS project in your own GitHub account.
2. **Create a Feature Branch:** Always isolate your work.
   `git checkout -b feat/add-new-skill`
   `git checkout -b fix/path-resolution`
3. **Professional Commit Messages:** Adhere strictly to Conventional Commits:
   - `feat: ...` for a new feature.
   - `fix: ...` for a bug fix.
   - `docs: ...` for documentation changes.
   - `chore(security): ...` for security upgrades.
4. **Push and PR:** Push to your branch and open a Pull Request against the `main` branch of `LongLeo287/aios-local`.
5. **Wait for Approval:** Our CI/CD validation hooks (`ai-os-tests.yml` and `ai-os-validate.yml`) will run a dry-run test of your logic. Once the status checks turn green, human leadership or the Dependabot Auto-Merge Secretary will approve the merge.

---

## 🤖 Contributing Agent Skills & Plugins

If you are developing a new Skill, Plugin, or Workflow for the AI OS Agents (e.g., Antigravity, Nova, Strix):

* **Skill Identity (`SKILL.md`):** Every new plugin MUST have a `SKILL.md` file in its root folder containing the required YAML metadata headers:
  ```yaml
  ---
  name: awesome-skill
  description: What this skill does and its limits.
  version: 1.0.0
  tier: 2
  ---
  ```
* **Follow 3-Tier Architecture:** Read the Architecture guide in our `README.md`. Tier 2 specific plugins MUST strictly implement the Lazy-Loading protocol (Init -> Execute -> Teardown) to avoid clogging the main memory.
* **Scan for Duplication:** Before inventing a new Agent or Workflow, use search tools (`grep`, etc.) to verify a similar component does not already exist in the Registry. Reinventing the wheel is prohibited by `RULE-ARCH-04`.

Thank you for helping us evolve AI OS into an unstoppable autonomous operating system!
