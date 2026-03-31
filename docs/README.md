# 📚 OmniClaw Corp - Official Documentation

Welcome to the **OmniClaw Official Documentation**. This directory contains human-readable guides, architectural overviews, and tutorials for understanding and interacting with the 21-department AI operating system.

[**🇻🇳 Xem Bản Tiếng Việt (Vietnamese)**](README-vn.md)

> 🔗 **OmniClaw Wiki:** For extended community resources, troubleshooting, and discussions, please visit the [**OmniClaw Official Wiki**](https://github.com/LongLeo287/OmniClaw/wiki).

---

## 🏛️ System Architecture
Learn about how the multi-agent system operates, scales, and protects itself.

- [**System Overview**](architecture/system_overview.md) — The 21-department structure and execution hierarchy.
- [**Plugin Architecture**](architecture/plugin_architecture.md) — How the 3-Tier Zero-Trust Plugin ecosystem is integrated.

## 🚀 Usage Guides
Quick starts and commands for developers and system operators.

-   [**Getting Started**](usage_guides/getting_started.md): Installation and setup.
-   [**Agent Commands & Invocations**](usage_guides/agent_commands.md): How to trigger OmniClaw features.
-   [**Data Packaging & Sync Process**](workflows/data_packaging_sync.md): How to package, backup sessions, and push data to GitHub, HuggingFace, and Google Drive securely.

## 🔄 Workflows & SOPs
Standardized rules and scripts used to maintain system integrity.

- [**Content Intake (CIV Gate)**](workflows/data_intake.md) — How external data is vetted before joining local memory.
- [**Deep Cleaner**](workflows/deep_cleaner.md) — The automated sanitation pipeline for OS integrity.

---
*If you are an AI accessing this folder, be aware that `docs/` is meant for human developers. For actual strict execution rules, reference `brain/rules/` and `brain/shared-context/` instead.*
