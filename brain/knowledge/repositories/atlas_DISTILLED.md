---
id: repo-fetched-atlas-132150
type: knowledge
owner: OA
registered_at: 2026-04-05T03:33:56.142562
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_atlas_132150

## Assimilation Report
Auto-cloned repository: FETCHED_atlas_132150

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<h1 align="center">
  <a href="http://atlasos.net" target="_blank"><img src="https://gcore.jsdelivr.net/gh/Atlas-OS/branding@main/banners/banner-v3.png" alt="Atlas" width="800"></a>
</h1>
  <p align="center">
    <a href="https://github.com/Atlas-OS/Atlas/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/atlas-os/atlas?style=for-the-badge&logo=github&color=1A91FF"/></a>
    <a href="https://github.com/Atlas-OS/Atlas/graphs/contributors"><img alt="Contributors" src="https://img.shields.io/github/contributors/atlas-os/atlas?style=for-the-badge&color=1A91FF" /></a>
    <a href="https://github.com/Atlas-OS/Atlas/releases/latest"><img alt="Release" src="https://img.shields.io/github/release/atlas-os/atlas?style=for-the-badge&color=1A91FF" /></a>
    <a href="https://github.com/Atlas-OS/.github/blob/main/profile/CODE_OF_CONDUCT.md"><img alt="Code of Conduct" src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg?style=for-the-badge&color=1A91FF" /></a>
  </p>
<p align="center">A transparent and lightweight modification to Windows, designed to optimize performance, privacy and usability.</p>

<p align="center">
  <a href="https://atlasos.net" target="_blank">🌐 Website</a>
  •
  <a href="https://docs.atlasos.net" target="_blank">📚 Documentation</a>
  •
  <a href="https://discord.atlasos.net" target="_blank">☎️ Discord</a>
  •
  <a href="https://github.com/Atlas-OS/Atlas/discussions" target="_blank">💬 Discussions</a>
</p>

## 📚 **Important Documentation**
- [Installation](https://docs.atlasos.net/getting-started/installation/)
- [Install FAQ](https://docs.atlasos.net/install-faq/removed-features/)
- [General FAQ](https://docs.atlasos.net/general-faq/atlas-and-security/)
- [Contribution Guidelines](https://docs.atlasos.net/contributing/contribution-guidelines/)
- [Branding](https://docs.atlasos.net/branding/)

## 🤔 What is Atlas?

AtlasOS, or Atlas, is an open-source project that enhances Windows by conveniently applying privacy, usability, and performance optimizations, all while maintaining functionality and [customizability](https://docs.atlasos.net/getting-started/post-installation/atlas-folder/general-configuration/).

## 👀 Why Atlas?
### 🔒 Enhanced Privacy
Atlas removes the majority of telemetry embedded within Windows and implements numerous group policies to minimize data collection. However, it cannot ensure privacy outside the scope of Windows, such as browsers and other third-party applications.

### 📈 Optimized Performance
Atlas strikes a balance between performance and compatibility. It implements numerous meaningful changes to improve Windows performance and responsiveness without breaking essential features. Atlas will not do tweaks for a placebo effect or marginal gains, making Atlas more stable and compatible.

### 🛡️ Security Features
Most Windows modifications remove key security features most users need to maintain a secure system. On the other hand, Atlas allows users to customize their security at their own risk while informing users about each option's [pros and cons](https://docs.atlasos.net/getting-started/post-installation/atlas-folder/security/).

Some optional security features are:

- Windows Defender & SmartScreen
- Windows Update
- Automatic updates are toggleable
- CPU mitigations
- User Account Control
- Core isolation features

### ✅ Increased Usability
Atlas applies many modifications and default settings to make Windows easier to use. This includes removing commonly unneeded applications (which are reinstallable), configuring many aspects of the interface, disabling advertisements, and much more.

### 🔍 Open Source and Transparent

Unlike custom Windows ISOs, Atlas is more straightforward to audit due to the use of [AME Wizard](https://amelabs.net). AME Wizard is controlled by Playbooks, a customizable script-esque system that can perform various tasks.

Playbooks are renamed **.zip** archives, with the password [`malte`](https://docs.amelabs.net/developers/getting-started/creation.html). As they primarily consist of plain text, Playbooks enable transparency, unlike custom Windows ISOs, which have many entry points for malicious activity. 

The few binaries in the Playbook are open source in our [`utilities` repository](https://github.com/Atlas-OS/utilities), with the [hashes listed here](https://github.com/Atlas-OS/Atlas/blob/main/src/playbook/Executables/AtlasModules/README.md).

Although the GUI is not open source for AME Wizard, AME Wizard's entire backend (called [TrustedUninstaller](https://github.com/Ameliorated-LLC/trusted-uninstaller-cli)) is open source under MIT, which contains each action used to run Atlas. The Atlas Playbook is open source under the [GPLv3 license](https://github.com/Atlas-OS/Atlas/blob/main/LICENSE).

### 🔒 Legal Compliance
As Atlas doesn't redistribute a modified Windows ISO, it complies with the [Microsoft Windows Usage Terms](https://www.microsoft.com/content/dam/microsoft/usetm/documents/windows/11/oem-(pre-installed)/UseTerms_OEM_Windows_11_English.pdf). In addition, Atlas does not alter activation in Windows.

## 🎨 Brand kit
Want to create your own Atlas wallpaper with some original creative designs? Visit our [Branding Kit on Docs](https://docs.atlasos.net/branding/) and share your creations on our [GitHub Discussions](https://github.com/Atlas-OS/Atlas/discussions/categories/community-artwork)!

## 💙 Contributors
<a href="https://github.com/Atlas-OS/Atlas/graphs/contributors" target="_blank"><img src="https://contrib.rocks/image?repo=Atlas-OS/Atlas&columns=18" alt="Avatars of all contributors"></a>

```

### File: src\README.md
```md
# Welcome to the source code! 😊

Here, you'll find all of Atlas' modifications in plain text. See our development documentation for more info:

- [Building the Playbook](https://docs.atlasos.net/contributing/playbook/#how-to-build-a-playbook)
- [Testing the Playbook](https://docs.atlasos.net/contributing/playbook/#how-to-run-your-built-playbooks)
- [What to test (for general testing)](https://docs.atlasos.net/contributing/testing/what-to-test/)
```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for atlas
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\CONTRIBUTING.md
```md
Contribution Guidelines are on our [Documentation](https://docs.atlasos.net/contributing/contribution-guidelines/).

```

### File: .github\pull_request_template.md
```md
### Questions
- [ ] Did you test your changes or double-check that they work?
- [ ] Did you read and follow the [Atlas Contribution Guidelines](https://docs.atlasos.net/contributions/)?

### Describe your pull request


```

### File: .github\SECURITY.md
```md
## Security Policy

### Vulnerability Reporting

At Atlas, our primary objective is to provide an optimal equilibrium between security, performance, and usability.

As Atlas is built on Windows, a proprietary operating system developed by Microsoft, we may not have solutions for security issues associated with Windows. Nonetheless, we are committed to addressing any security concerns caused by Atlas and welcome any enhancements made to the base Windows. We encourage the submission of GitHub issues and pull requests that relate to security vulnerabilities, as long as the solutions match our objective of having an equilibrium.

Should you discover any security flaws linked to the Atlas-specific software/tools or [AME Wizard](https://ameliorated.io) (i.e., anything not related to Microsoft), kindly notify us immediately through the appropriate channels. For AME Wizard, please visit the [website](https://ameliorated.io) to identify suitable contacts. For all other issues, report them to the corresponding Atlas repository as an issue.

Please note that some issues may not be rectifiable by us. If you come across a vulnerability in Atlas that is also present in the latest version of stock/vanilla Windows, please report it to Microsoft. For more information on reporting security vulnerabilities and pentesting, please visit the [Microsoft](https://www.microsoft.com/en-us/msrc/faqs-report-an-issue) website. We wish you the best of luck in your reporting endeavor.

```

