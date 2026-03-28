# Contributing to AI OS CORP

First off, thank you for considering contributing to the AI OS CORP ecosystem! It's people like you that make AI OS a robust, Zero-Trust autonomous operating system.

## 🛡️ The Zero-Trust Policy (MANDATORY)

Before submitting any Pull Request (PR), you must abide by the **AI OS Zero-Trust principles**:
1. **Never commit hardcoded API keys**, tokens, or passwords. Your PR will be rejected immediately by automated CI/CD if a credential leak is detected.
2. **Never commit absolute machine paths** (e.g., `C:\Users\...` or `D:\Projects\...`). Always use relative paths or environment variables like `<AI_OS_ROOT>`.

## 🛠️ How to Contribute

1. **Fork the Repository**: Clone the project to your own GitHub account.
2. **Create a Feature Branch**: Example: `git checkout -b feat/add-new-skill`.
3. **Commit your changes**: Adhere to professional commit message conventions (e.g., `feat: ...`, `fix: ...`, `docs: ...`).
4. **Push to the Branch**: `git push origin feat/add-new-skill`.
5. **Open a Pull Request**: Submit the PR against the `main` branch of AI OS CORP and wait for the automated GitHub Actions (Skill Validate & Mock Dry-run) to pass.

## 🤖 Contributing Agent Skills (Plugins)

If you are developing a new Skill/Plugin for the AI OS Agents (e.g., Antigravity, Nova):
- Ensure that you have a `SKILL.md` inside your plugin folder containing the metadata headers (`name:`, `description:`, `version:`, `tier:`).
- Read our 3-Tier Plugin Architecture guide in `README.md` to ensure your skill respects lazy-loading standards.

Thank you for helping us evolve AI OS into an unstoppable operating system!
