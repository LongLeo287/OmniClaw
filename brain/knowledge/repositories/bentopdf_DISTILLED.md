---
id: repo-fetched-bentopdf-112831
type: knowledge
owner: OA
registered_at: 2026-04-05T03:50:16.840932
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_bentopdf_112831

## Assimilation Report
Auto-cloned repository: FETCHED_bentopdf_112831

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center"><img src="public/images/favicon-no-bg.svg" width="80"></p>
<h1 align="center">BentoPDF</h1>
<p align="center">
  <a href="https://www.digitalocean.com/?refcode=d93c189ef6d0&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge">
    <img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%203.svg" alt="DigitalOcean Referral Badge">
  </a>
</p>

**BentoPDF** is a powerful, privacy-first, client-side PDF toolkit that is self hostable and allows you to manipulate, edit, merge, and process PDF files directly in your browser. No server-side processing is required, ensuring your files remain secure and private.

[![Docker Downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fghcr-badge.elias.eu.org%2Fapi%2Falam00000%2Fbentopdf%2Fbentopdf&query=%24.downloadCount&logo=docker&label=Docker%20Downloads&color=blue)](https://github.com/alam00000/bentopdf/pkgs/container/bentopdf) [![Ko-fi](https://img.shields.io/badge/Buy%20me%20a%20Coffee-yellow?logo=kofi&style=flat-square)](https://ko-fi.com/alio01) ![GitHub Stars](https://img.shields.io/github/stars/alam00000/bentopdf?style=social)
[![Sponsor me on GitHub](https://img.shields.io/badge/Sponsor-%E2%9D%A4-ff69b4)](https://github.com/sponsors/alam00000)

![BentoPDF Tools](public/images/bentopdf-tools.png)

### FOSS Hack 2026

[![Watch Demo](https://img.shields.io/badge/Watch%20Demo-FOSS%20Hack%202026-red?style=for-the-badge&logo=googledrive)](https://drive.google.com/file/d/14Vf62PvHiuf1RKFKtMlAzpbf4QQPLpRF/view?usp=sharing)

---

## Table of Contents

- [Join Us on Discord](#-join-us-on-discord)
- [Documentation](#-documentation)
- [Licensing](#-licensing)
- [Stargazers over time](#-stargazers-over-time)
- [Thank You to Our Sponsors](#-thank-you-to-our-sponsors)
- [Why BentoPDF?](#-why-bentopdf)
- [Features / Tools Supported](#️-features--tools-supported)
  - [Organize & Manage PDFs](#organize--manage-pdfs)
  - [Edit & Modify PDFs](#edit--modify-pdfs)
  - [Convert to PDF](#convert-to-pdf)
  - [Convert from PDF](#convert-from-pdf)
  - [Secure & Optimize PDFs](#secure--optimize-pdfs)
- [Translations](#-translations)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Quick Start](#-quick-start)
  - [Static Hosting](#static-hosting-using-netlify-vercel-and-github-pages)
  - [Self-Hosting Locally](#-self-hosting-locally)
  - [Docker Compose / Podman Compose](#-run-with-docker-compose--podman-compose-recommended)
  - [Podman Quadlet](#-podman-quadlet-systemd-integration)
  - [Simple Mode](#-simple-mode-for-internal-use)
  - [Custom Branding](#-custom-branding)
  - [Disabling Specific Tools](#-disabling-specific-tools)
  - [WASM Configuration](#wasm-configuration)
  - [Air-Gapped / Offline Deployment](#air-gapped--offline-deployment)
  - [Security Features](#-security-features)
  - [Digital Signature CORS Proxy](#digital-signature-cors-proxy-required)
  - [Version Management](#-version-management)
  - [Development Setup](#-development-setup)
- [Tech Stack & Background](#️-tech-stack--background)
- [Roadmap](#️-roadmap)
- [Contributing](#-contributing)
- [Special Thanks](#special-thanks)

---

## 📢 Join Us on Discord

[![Discord](https://img.shields.io/badge/Discord-Join%20Server-7289da?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/Bgq3Ay3f2w)

Have questions, feature requests, or want to chat with the community? Join our Discord server!

---

## 📚 Documentation

[![Documentation](https://img.shields.io/badge/Docs-VitePress-646cff?style=for-the-badge&logo=vite&logoColor=white)](https://bentopdf.com/docs/)

Visit our [Documentation](https://bentopdf.com/docs/) for:

- **Getting Started** guide
- **Tools Reference** (50+ tools)
- **Self-Hosting** guides (Docker, Vercel, Netlify, Cloudflare, AWS, Hostinger, Nginx, Apache)
- **Contributing** guide
- **Commercial License** details

---

## 📜 Licensing

BentoPDF is **dual-licensed** to fit your needs:

| License        | Best For                                     | Price              |
| -------------- | -------------------------------------------- | ------------------ |
| **AGPL-3.0**   | Open-source projects with public source code | **Free**           |
| **Commercial** | Proprietary / closed-source applications     | **$79** (lifetime) |

<p align="center">
  <a href="https://buy.polar.sh/polar_cl_ThDfffbl733x7oAodcIryCzhlO57ZtcWPq6HJ1qMChd">
    <img src="https://img.shields.io/badge/🚀_Get_Commercial_License-$79_Lifetime-6366f1?style=for-the-badge&labelColor=1f2937" alt="Get Commercial License">
  </a>
</p>

> **One-time purchase** · **Unlimited devices & users** · **Lifetime updates** · **No AGPL obligations**

📖 For more details, see our [Licensing Page](https://bentopdf.com/licensing.html)

### AGPL Components (Pre-configured via CDN)

BentoPDF does **not** bundle AGPL-licensed processing libraries in its source code, but **pre-configures CDN URLs** so all features work out of the box with zero setup:

| Component              | License  | Features Enabled                                                                                    |
| ---------------------- | -------- | --------------------------------------------------------------------------------------------------- |
| **PyMuPDF**            | AGPL-3.0 | PDF to Text/Markdown/SVG/DOCX, Extract Images/Tables, EPUB/MOBI/XPS conversion, Compression, Deskew |
| **Ghostscript**        | AGPL-3.0 | PDF/A Conversion, Font to Outline                                                                   |
| **CoherentPDF (CPDF)** | AGPL-3.0 | Merge, Split by Bookmarks, Table of Contents, PDF to/from JSON, Attachments                         |

> [!TIP]
> **Zero-config by default.** WASM modules are loaded at runtime from jsDelivr CDN. No manual configuration is needed. For custom deployments (air-gapped, self-hosted), see [WASM Configuration](#wasm-configuration) below.

<hr>

## ⭐ Stargazers over time

[![Star History Chart](https://api.star-history.com/svg?repos=alam00000/bentopdf&type=Date)](https://star-history.com/#alam00000/bentopdf&Date)

---

## 💖 Thank You to Our Sponsors

We're incredibly grateful to all our sponsors and supporters who help keep BentoPDF free and open source!

[![Sponsor me on GitHub](https://img.shields.io/badge/Become%20a%20Sponsor-%E2%9D%A4-ff69b4?style=for-the-badge)](https://github.com/sponsors/alam00000)
[![Buy me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20Coffee-yellow?style=for-the-badge&logo=kofi)](https://ko-fi.com/alio01)

<!-- sponsors -->
<!-- sponsors -->

---

## ✨ Why BentoPDF?

- **Privacy First**: All processing happens in your browser. Your files are never uploaded to a server, guaranteeing 100% privacy.
- **No Limits**: Manipulate as many files as you want, as often you want. There are no restrictions or upload limits.
- **High Performance**: Built with modern web technologies, BentoPDF is fast and efficient, handling even large PDF files with ease.
- **Completely Free**: BentoPDF is a free and open-source tool for everyone.

---

## 🛠️ Features / Tools Supported

BentoPDF offers a comprehensive suite of tools to handle all your PDF needs.

### Organize & Manage PDFs

| Tool Name                    | Description                                                                                             |
| :--------------------------- | :------------------------------------------------------------------------------------------------------ |
| **Merge PDFs**               | Combine multiple PDF files into one. Preserves Bookmarks.                                               |
| **Split PDFs**               | Extract specific pages or divide a document into smaller files.                                         |
| **Organize Pages**           | Reorder, duplicate, or delete pages with a simple drag-and-drop interface.                              |
| **Extract Pages**            | Save a specific range of pages as a new PDF.                                                            |
| **Delete Pages**             | Remove unwanted pages from your document.                                                               |
| **Rotate PDF**               | Rotate individual or all pages in a document.                                                           |
| **Rotate by Custom Degrees** | Rotate pages by any custom angle.                                                                       |
| **N-Up PDF**                 | Combine multiple pages onto a single page.                                                              |
| **View PDF**                 | A powerful, integrated PDF viewer.                                                                      |
| **Alternate & Mix Pages**    | Merge pages by alternating pages from each PDF. Preserves Bookmarks.                                    |
| **Posterize PDF**            | Split a PDF into multiple smaller pages for print.                                                      |
| **PDF Multi Tool**           | Merge, Split, Organize, Delete, Rotate, Add Blank Pages, Extract and Duplicate in an unified interface. |
| **PDF Booklet**              | Rearrange pages for double-sided booklet printing. Fold and staple to create a booklet.                 |
| **Add Attachments**          | Embed one or more files into your PDF.                                                                  |
| **Extract Attachments**      | Extract all embedded files from PDF(s) as a ZIP.                                                        |
| **Edit Attachments**         | View or remove attachments in your PDF.                                                                 |
| **Divide Pages**             | Divide pages horizontally or vertically.                                                                |
| **Combine to Single Page**   | Stitch all pages into one continuous scroll.                                                            |
| **Add Blank Page**           | Insert an empty page anywhere in your PDF.                                                              |
| **Reverse Pages**            | Flip the order of all pages in your document.                                                           |
| **View Metadata**            | Inspect the hidden properties of your PDF.                                                              |
| **PDFs to ZIP**              | Package multiple PDF files into a ZIP archive.                                                          |
| **Compare PDFs**             | Compare two PDFs side by side.                                                                          |

### Edit & Modify PDFs

| Tool Name                 | Description                                                                                                                                                                                     |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PDF Editor**            | Annotate, highlight, redact, comment, add shapes/images, search, and view PDFs.                                                                                                                 |
| **Create Fillable Forms** | Create professional fillable PDF forms with text fields, checkboxes, dropdowns, radio buttons, signatures, and more. Fully compliant with PDF standards for compatibility with all PDF viewers. |
| **PDF Form Filler**       | Fill in forms directly in the browser. Also supports XFA forms.                                                                                                                                 |
| **Add Page Numbers**      | Easily add page numbers with customizable formatting.                                                                                                                                           |
| **Bates Numbering**       | Add sequential Bates numbers across one or more PDF files.                                                                                                                                      |
| **Add Watermark**         | Add text or image watermarks to protect your documents.                                                                                                                                         |
| **Header & Footer**       | Add customizable headers and footers.                                                                                                                                                           |
| **Crop PDF**              | Crop specific pages or the entire document.                                                                                                                                                     |
| **Deskew PDF**            | Automatically straighten tilted scanned pages using OpenCV.                                                                                                                                     |
| **Font to Outline**       | Convert all fonts to vector outlines for consistent rendering across all devices.                                                                                                               |
| **Invert Colors**         | Invert the colors of your PDF pages for better readability.                                                                                                                                     |
| **Change Background**     | Modify the background color of your PDF.                                                                                                                                                        |
| **Change Text Color**     | Change the color of text content within the PDF.                                                                                                                                                |
| **Flatten PDF**           | Flatten form fields and annotations into static content.                                                                                                                                        |
| **Remove Annotations**    | Remove comments, highlights, and other annotations.                                                                                                                                             |
| **Remove Blank Pages**    | Auto detect and remove blank pages in a PDF.                                                                                                                                                    |
| **Edit Bookmarks**        | Add, Edit, Create, Import and Export PDF Bookmarks.                                                                                                                                             |
| **Add Stamps**            | A
... [TRUNCATED]
```

### File: CCLA.md
```md
# BentoPDF Corporate Contributor License Agreement (CCLA)

Thank you for your organization's interest in contributing to BentoPDF. This Corporate Contributor License Agreement ("Agreement") documents the rights granted by corporate contributors to the Project.

By signing this Agreement, you accept and agree to the following terms and conditions for your organization's present and future Contributions submitted to the Project.

## 1. Definitions

**"You" (or "Your")** means the legal entity on behalf of which this Agreement is being entered into.

**"Contributor"** means any employee, contractor, or authorized agent of You who submits Contributions on Your behalf.

**"Contribution"** means any original work of authorship, including any modifications or additions to an existing work, that is intentionally submitted by You or any of Your Contributors to the Project for inclusion in, or documentation of, the Project. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Project or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Project for the purpose of discussing and improving the Project.

**"Project"** means the BentoPDF software project and all associated repositories, documentation, and related materials maintained at https://github.com/alam00000/bentopdf.

**"Project Owner"** means the owners and maintainers of the Project.

## 2. Grant of Copyright License

Subject to the terms and conditions of this Agreement, You hereby grant to the Project Owner and to recipients of software distributed by the Project Owner a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to:

- Reproduce, prepare derivative works of, publicly display, publicly perform, and distribute Contributions made by You and Your Contributors, and such derivative works
- Sublicense any or all of the foregoing rights to third parties
- **Relicense Contributions under any license**, including but not limited to proprietary licenses, commercial licenses, or any other open source license

This grant specifically enables the Project Owner to offer commercial licenses of the Project incorporating Your Contributions, consistent with the Project's dual licensing model (AGPL-3.0 for open source use, and a separate commercial license for proprietary use).

## 3. Grant of Patent License

Subject to the terms and conditions of this Agreement, You hereby grant to the Project Owner and to recipients of software distributed by the Project Owner a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Contribution, where such license applies only to those patent claims licensable by You that are necessarily infringed by Your Contribution(s) alone or by combination of Your Contribution(s) with the Project to which such Contribution(s) was submitted.

If any entity institutes patent litigation against You or any other entity (including a cross-claim or counterclaim in a lawsuit) alleging that Your Contribution, or the Project to which You have contributed, constitutes direct or contributory patent infringement, then any patent licenses granted to that entity under this Agreement for that Contribution or Project shall terminate as of the date such litigation is filed.

## 4. Authorized Contributors

You are responsible for:

a) Identifying the initial list of Contributors authorized to submit Contributions on Your behalf by listing them in Schedule A below

b) Keeping the list of authorized Contributors current by notifying the Project Owner when Contributors should be added or removed

c) Ensuring that all authorized Contributors are aware of and comply with the terms of this Agreement

All Contributions made by Your authorized Contributors shall be deemed to be made on Your behalf and subject to this Agreement.

## 5. Representations and Warranties

You represent and warrant that:

a) **Authority**: You are legally entitled to grant the above licenses and have the authority to bind the legal entity You represent. You have taken all necessary corporate action to authorize the execution of this Agreement.

b) **Contributor Authorization**: Each Contributor identified by You is authorized to submit Contributions on Your behalf.

c) **Originality**: Each Contribution is Your organization's original creation, or You have sufficient rights to submit the Contribution on behalf of the original authors.

d) **Third-Party Rights**: Your Contributions include complete details of any third-party license or other restriction (including, but not limited to, related patents and trademarks) of which You are aware and which are associated with any part of Your Contributions.

e) **No Conflicting Obligations**: Your Contributions do not violate any agreement or obligation You have with any third party.

f) **Accuracy**: All information You provide in connection with this Agreement and Your Contributions is accurate and complete.

## 6. Moral Rights Waiver

To the fullest extent permitted under applicable law, You hereby waive, and agree to cause Your Contributors to waive, any and all moral rights in or relating to Contributions, including without limitation:

- The right of attribution
- The right of integrity
- The right to object to derogatory treatment
- Any similar rights existing under the laws of any jurisdiction

You acknowledge that the Project Owner may modify, adapt, translate, or otherwise change Contributions without consent and without attribution.

## 7. No Revocation

**This license grant is irrevocable.** Once a Contribution has been submitted under this Agreement, You may not revoke or withdraw the licenses granted herein. The Project Owner and all downstream recipients may continue to use, distribute, modify, and sublicense Contributions indefinitely.

## 8. Retention of Copyright

You retain all right, title, and interest in and to the copyright of Your Contributions. Nothing in this Agreement is intended to transfer ownership of Your Contributions to the Project Owner. You are free to use Your Contributions for any other purpose.

## 9. No Obligation

You understand that the decision to include any Contribution in any project or source repository is entirely at the discretion of the Project Owner. The Project Owner is under no obligation to accept, use, or include any Contribution.

## 10. Support and Warranty Disclaimer

Unless required by applicable law or agreed to in writing, You provide Contributions on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.

You are not expected to provide support for Contributions, except to the extent You desire to provide support. You may provide support for free, for a fee, or not at all.

## 11. Notification

You agree to notify the Project Owner of any facts or circumstances of which You become aware that would make any of Your representations in this Agreement inaccurate in any respect.

## 12. Governing Law

This Agreement shall be governed by and construed in accordance with the laws of India, without regard to its conflict of law provisions.

---

## Signature

By signing this Agreement, You confirm that You have the authority to bind the legal entity named below, and that entity agrees to the terms of this Corporate Contributor License Agreement.

**Legal Entity Name:** ___________________________

**Address:** ___________________________

**Point of Contact Name:** ___________________________

**Point of Contact Email:** ___________________________

**Point of Contact Phone:** ___________________________

**Signature:** ___________________________

**Title:** ___________________________

**Date:** ___________________________

---

## Schedule A: Authorized Contributors

The following individuals are authorized to submit Contributions to the Project on behalf of the above-named legal entity:

| Full Name | GitHub Username | Email Address | Date Added |
|-----------|-----------------|---------------|------------|
|           |                 |               |            |
|           |                 |               |            |
|           |                 |               |            |
|           |                 |               |            |
|           |                 |               |            |

*Add additional rows as needed. To update this list, contact the Project Owner at contact@bentopdf.com*

---

*This CLA is based on the Apache Corporate Contributor License Agreement and has been adapted for BentoPDF's dual licensing model.*

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers of **BentoPDF** pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming, diverse, inclusive, and healthy community.

---

## Our Standards

Examples of behavior that contributes to a positive environment for our community include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy toward other community members

Examples of unacceptable behavior include:

- The use of sexualized language or imagery and unwelcome sexual attention or advances
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others’ private information, such as a physical or electronic address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

---

## Enforcement Responsibilities

Project maintainers of **BentoPDF** are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned with this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

---

## Reporting Guidelines

If you are subject to or witness unacceptable behavior, or have any other concerns, please report it by contacting the project team at:

**Email:** `contact@bentopdf.com`

All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances.

---

## Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing the project include using an official project email address, posting via an official social media account, or acting as an appointed representative at an online or offline event.

---

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at the email above. All complaints will be reviewed and investigated promptly and fairly.

Maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent consequences as determined by other members of the project's leadership.

---

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant, version 2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct.html), available at https://www.contributor-covenant.org.

```

### File: CONTRIBUTING.md
```md
# Contributing to BentoPDF

First off, thank you for considering contributing to **BentoPDF**! Your help makes this project better for everyone.

This document outlines how to contribute, report issues, and get involved in the project.

---

## Contributor License Agreement (CLA)

Before we can accept your contributions, you must sign our Contributor License Agreement (CLA). This is required because BentoPDF uses a dual licensing model:

- **AGPL-3.0** for open source use
- **Commercial license** for proprietary use

The CLA ensures we can include your contributions in both versions of the project.

### For Individual Contributors

Sign our [Individual Contributor License Agreement (ICLA)](ICLA.md). When you submit your first pull request, the CLA Assistant bot will automatically ask you to sign by commenting on the PR.

### For Corporate Contributors

If you are contributing on behalf of your employer, your organization needs to sign our [Corporate Contributor License Agreement (CCLA)](CCLA.md). Please contact us at [contact@bentopdf.com](mailto:contact@bentopdf.com) to arrange corporate CLA signing.

### What the CLA Grants

By signing the CLA, you:

- Grant us a broad copyright license to use, modify, and relicense your contributions (including for commercial use)
- Grant a patent license for any patents covering your contribution
- Represent that you have the authority to make the contribution
- Retain full copyright ownership of your contributions

---

## 1. How to Contribute

You can contribute in several ways:

- **Reporting Bugs:** If you find a bug or unexpected behavior, please open an issue. Include steps to reproduce and any relevant screenshots or logs.
- **Feature Requests:** Suggest new features or improvements by opening an issue and describing your idea clearly.
- **Code Contributions:** Submit a pull request with new features, bug fixes, or improvements.
- **Documentation:** Help improve the README, usage examples, or guides.
- **Testing:** Help test new releases or changes to ensure stability.

---

### Issue Template

When reporting bugs, requesting features, or asking questions, please use our [issue template](.github/ISSUE_TEMPLATE/bug_feature_question.md). The template will automatically appear when you create a new issue.

**Our issue template helps you provide:**

- Clear categorization (Bug, Feature Request, or Question)
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Environment details
- Screenshots or logs

**Title Format Examples:**

- `(Bug) Text alignment incorrect on multi-line paragraphs`
- `(Feature) Add support for custom PDF metadata`
- `(Question) How to embed custom fonts?`

### Pull Request Template

When submitting code contributions, please use our [pull request template](.github/pull_request_template.md). The template will automatically appear when you create a new PR.

**Key requirements:**

- Link to the related issue (e.g., `Fixes #123`)
- Describe the type of change (bug fix, feature, breaking change)
- Explain how you tested your changes
- Complete the checklist before submitting

## 2. Getting Started with Code Contributions

1.  **Fork the Repository**

    ```bash
    git clone https://github.com/alam00000/bentopdf.git
    cd bento-pdf
    npm install
    ```

2.  **Create a New Branch**

    ```bash
    git checkout -b feature/my-new-feature
    ```

3.  **Make Your Changes**
    - Follow the code style and conventions used in the project.
    - Add comments where necessary.
    - Update or add tests if applicable.

4.  **Run Tests**

    ```bash
    npm run test
    ```

5.  **Commit Your Changes**

    ```bash
    git add .
    git commit -m "Add a meaningful commit message"
    ```

6.  **Push and Submit a Pull Request**

    ```bash
    git push origin feature/my-new-feature
    ```

    - Open a pull request on GitHub and provide a clear description of your changes.

---

## 3. Code Style

- Follow the existing TypeScript and JavaScript conventions.
- Use `camelCase` for variables and functions.
- Keep lines reasonably short and readable.
- Comment complex logic for clarity.

---

## 4. Issues and Pull Requests

- Make sure your PR is focused and addresses a single issue or feature.
- Reference related issues in your PR description (e.g., `Closes #12`).
- Be responsive to feedback and make requested changes promptly.

---

## 5. Reporting Security Issues

If you discover a security vulnerability, please **do not** open a public issue. Instead, contact the project maintainer directly at:

**Email:** [contact@bentopdf.com](mailto:contact@bentopdf.com)

---

## 6. Code of Conduct

All contributors are expected to follow the Code of Conduct. Be respectful and considerate in all communications.

---

Thank you for helping make **BentoPDF** a better library for everyone!

```

### File: ICLA.md
```md
# BentoPDF Individual Contributor License Agreement (ICLA)

Thank you for your interest in contributing to BentoPDF. This Individual Contributor License Agreement ("Agreement") documents the rights granted by contributors to the Project.

By signing this Agreement, you accept and agree to the following terms and conditions for your present and future Contributions submitted to the Project.

## 1. Definitions

**"You" (or "Your")** means the individual who is signing this Agreement and submitting Contributions to the Project.

**"Contribution"** means any original work of authorship, including any modifications or additions to an existing work, that is intentionally submitted by You to the Project for inclusion in, or documentation of, the Project. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Project or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Project for the purpose of discussing and improving the Project.

**"Project"** means the BentoPDF software project and all associated repositories, documentation, and related materials maintained at https://github.com/alam00000/bentopdf.

**"Project Owner"** means the owners and maintainers of the Project.

## 2. Grant of Copyright License

Subject to the terms and conditions of this Agreement, You hereby grant to the Project Owner and to recipients of software distributed by the Project Owner a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to:

- Reproduce, prepare derivative works of, publicly display, publicly perform, and distribute Your Contributions and such derivative works
- Sublicense any or all of the foregoing rights to third parties
- **Relicense Your Contributions under any license**, including but not limited to proprietary licenses, commercial licenses, or any other open source license

This grant specifically enables the Project Owner to offer commercial licenses of the Project incorporating Your Contributions, consistent with the Project's dual licensing model (AGPL-3.0 for open source use, and a separate commercial license for proprietary use).

## 3. Grant of Patent License

Subject to the terms and conditions of this Agreement, You hereby grant to the Project Owner and to recipients of software distributed by the Project Owner a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Contribution, where such license applies only to those patent claims licensable by You that are necessarily infringed by Your Contribution(s) alone or by combination of Your Contribution(s) with the Project to which such Contribution(s) was submitted.

If any entity institutes patent litigation against You or any other entity (including a cross-claim or counterclaim in a lawsuit) alleging that Your Contribution, or the Project to which You have contributed, constitutes direct or contributory patent infringement, then any patent licenses granted to that entity under this Agreement for that Contribution or Project shall terminate as of the date such litigation is filed.

## 4. Representations and Warranties

You represent and warrant that:

a) **Authority**: You are legally entitled to grant the above licenses. If Your employer(s) has rights to intellectual property that You create, You represent that You have received permission to make Contributions on behalf of that employer, that Your employer has waived such rights for Your Contributions, or that Your employer has executed a separate Corporate CLA with the Project.

b) **Originality**: Each of Your Contributions is Your original creation. You represent that Your Contributions include complete details of any third-party license or other restriction (including, but not limited to, related patents and trademarks) of which You are aware and which are associated with any part of Your Contributions.

c) **No Conflicting Obligations**: Your Contribution does not violate any agreement or obligation You have with any third party.

d) **Accuracy**: All information You provide in connection with this Agreement and Your Contributions is accurate and complete.

## 5. Moral Rights Waiver

To the fullest extent permitted under applicable law, You hereby waive, and agree not to assert, any and all moral rights You may have in or relating to Your Contributions, including without limitation:

- The right of attribution
- The right of integrity
- The right to object to derogatory treatment
- Any similar rights existing under the laws of any jurisdiction

You acknowledge that the Project Owner may modify, adapt, translate, or otherwise change Your Contributions without Your consent and without attribution.

## 6. No Revocation

**This license grant is irrevocable.** Once You have submitted a Contribution under this Agreement, You may not revoke or withdraw the licenses granted herein. The Project Owner and all downstream recipients may continue to use, distribute, modify, and sublicense Your Contribution indefinitely.

## 7. Retention of Copyright

You retain all right, title, and interest in and to the copyright of Your Contributions. Nothing in this Agreement is intended to transfer ownership of Your Contributions to the Project Owner. You are free to use Your Contributions for any other purpose.

## 8. No Obligation

You understand that the decision to include Your Contribution in any project or source repository is entirely at the discretion of the Project Owner. The Project Owner is under no obligation to accept, use, or include any Contribution.

## 9. Support and Warranty Disclaimer

Unless required by applicable law or agreed to in writing, You provide Your Contributions on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.

You are not expected to provide support for Your Contributions, except to the extent You desire to provide support. You may provide support for free, for a fee, or not at all.

## 10. Notification

You agree to notify the Project Owner of any facts or circumstances of which You become aware that would make any of Your representations in this Agreement inaccurate in any respect.

## 11. Governing Law

This Agreement shall be governed by and construed in accordance with the laws of India, without regard to its conflict of law provisions.

---

## Signature

By submitting a pull request or other Contribution to the Project, and by typing your name and date below (or by signing electronically via CLA Assistant), you agree to the terms of this Individual Contributor License Agreement.

**Full Legal Name:** Stephan Paternotte

**GitHub Username:** Stephan-P

**Email Address:** stephan@paternottes.net

**Date:** 20-12-2025

**Signature:** ___________________________

---

*This CLA is based on the Apache Individual Contributor License Agreement and has been adapted for BentoPDF's dual licensing model.*

```

### File: RELEASE.md
```md
# 🚀 Release Process - Real-World Scenarios

## 📋 Common Release Scenarios

### **Scenario 1: I Just Finished a Feature and Want to Release**

**Situation:** You've completed a new feature, tested it locally, and want to release it.

**Current State:**

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  modified:   src/js/new-feature.js
  modified:   src/css/styles.css
  modified:   README.md

Untracked files:
  src/js/feature-helper.js
```

**Steps:**

```bash
# 1. Commit your feature changes
git add .
git commit -m "Add new PDF watermark feature"

# 2. Choose your release type and run
npm run release        # Patch: 1.0.0 → 1.0.1 (bug fixes, small improvements)
npm run release:minor  # Minor: 1.0.0 → 1.1.0 (new features, backward compatible)
npm run release:major  # Major: 1.0.0 → 2.0.0 (breaking changes)
```

**What Happens:**

- ✅ Your feature commit stays as-is
- ✅ Version gets bumped in `package.json` and `chart/Chart.yaml`
- ✅ New release commit is created
- ✅ Git tag is created (e.g., `v1.0.1`)
- ✅ Everything gets pushed to GitHub
- ✅ Docker image gets built and published

---

### **Scenario 2: I Have Uncommitted Changes and Want to Release**

**Situation:** You have local changes but haven't committed them yet.

**Current State:**

```bash
$ git status
Changes not staged for commit:
  modified:   package.json
  modified:   src/js/main.js
  modified:   README.md
```

**❌ This Will Fail:**

```bash
npm run release
# Error: Your local changes would be overwritten by merge
```

**✅ Solution Options:**

**Option A: Commit Everything First (Recommended)**

```bash
git add .
git commit -m "Add new features and improvements"
npm run release
```

**Option B: Stash Changes Temporarily**

```bash
git stash
npm run release
git stash pop  # Restore your changes after release
```

**Option C: Commit Only What's Needed**

```bash
git add package.json src/js/main.js
git commit -m "Add core improvements"
npm run release
git add README.md
git commit -m "Update documentation"
```

---

### **Scenario 3: I Want to Release a Hotfix**

**Situation:** There's a critical bug in production that needs immediate fixing.

**Steps:**

```bash
# 1. Fix the bug
git add src/js/bug-fix.js
git commit -m "Fix critical PDF rendering issue"

# 2. Release as patch (bug fix)
npm run release
# This creates: 1.0.0 → 1.0.1
```

**Result:**

- ✅ Bug fix gets released immediately
- ✅ Docker image with fix is available
- ✅ Users can pull the fixed version

---

### **Scenario 4: I Want to Release a Major Update**

**Situation:** You've added significant new features that might break existing functionality.

**Steps:**

```bash
# 1. Commit all your changes
git add .
git commit -m "Add major PDF editing features and API changes"

# 2. Release as major version
npm run release:major
# This creates: 1.0.0 → 2.0.0
```

**Result:**

- ✅ Major version bump indicates breaking changes
- ✅ Users know to check compatibility
- ✅ Both old and new versions available

---

### **Scenario 5: I Want to Release Multiple Features at Once**

**Situation:** You've been working on multiple features and want to release them together.

**Steps:**

```bash
# 1. Commit all features
git add .
git commit -m "Add multiple PDF tools: watermark, encryption, and compression"

# 2. Choose appropriate release type
npm run release:minor  # For new features (1.0.0 → 1.1.0)
# OR
npm run release:major  # For breaking changes (1.0.0 → 2.0.0)
```

---

### **Scenario 6: I Want to Test the Release Process**

**Situation:** You want to test the release system without affecting production.

**Steps:**

```bash
# 1. Make a small test change
echo "// Test comment" >> src/js/main.js
git add src/js/main.js
git commit -m "Test release process"

# 2. Run patch release
npm run release
# This creates: 1.0.0 → 1.0.1

# 3. Verify everything works
# Check GitHub Actions, Docker Hub, etc.

# 4. If you want to undo the test release
git tag -d v1.0.1
git push origin :refs/tags/v1.0.1
git reset --hard HEAD~1
```

---

## 🎯 **Release Type Guidelines**

| Scenario            | Command                 | Version Change  | When to Use                          |
| ------------------- | ----------------------- | --------------- | ------------------------------------ |
| **Bug Fix**         | `npm run release`       | `1.0.0 → 1.0.1` | Fixing bugs, small improvements      |
| **New Feature**     | `npm run release:minor` | `1.0.0 → 1.1.0` | Adding features, backward compatible |
| **Breaking Change** | `npm run release:major` | `1.0.0 → 2.0.0` | API changes, major rewrites          |

---

## 🔄 **What Happens After You Run a Release Command**

### **Immediate Actions (Local):**

1. **Version Update**: `package.json` version gets bumped
2. **Git Commit**: New commit created with "Release vX.X.X"
3. **Git Tag**: Tag created (e.g., `v1.0.1`)
4. **Git Push**: Everything pushed to GitHub

### **Automatic Actions (GitHub):**

1. **GitHub Actions Triggered**: Workflow starts building Docker image
2. **Docker Build**: Multi-architecture image created
3. **Docker Push**: Images pushed to Docker Hub with tags:
   - `bentopdfteam/bentopdf:latest`
   - `bentopdfteam/bentopdf:1.0.1`
   - `bentopdfteam/bentopdf:v1.0.1`

### **End Result:**

Users can immediately pull your new version:

```bash
docker pull bentopdfteam/bentopdf:1.0.1
```

---

## 🚨 **Before You Release - Prerequisites**

### **1. Docker Hub Credentials Setup**

You need to add these secrets to your GitHub repository:

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Add these secrets:
   - `DOCKER_USERNAME`: Your Docker Hub username
   - `DOCKER_TOKEN`: Your Docker Hub access token

### **2. Get Docker Hub Token**

1. Go to [Docker Hub](https://hub.docker.com)
2. Account Settings → Security → New Access Token
3. Set permissions to "Read, Write, Delete"
4. Copy the token and add it to GitHub Secrets

---

## 🔧 **Troubleshooting Common Issues**

### **❌ "Your local changes would be overwritten by merge"**

**Problem:** You have uncommitted changes
**Solution:**

```bash
git add .
git commit -m "Your commit message"
npm run release
```

### **❌ "Permission denied" in GitHub Actions**

**Problem:** Missing Docker Hub credentials
**Solution:** Add `DOCKER_USERNAME` and `DOCKER_TOKEN` to GitHub Secrets

### **❌ "Tag already exists"**

**Problem:** You've run the same release before
**Solution:** This is normal! The script will skip creating duplicate tags

### **❌ GitHub Actions fails**

**Problem:** Various build issues
**Solution:**

1. Check Actions tab for detailed logs
2. Verify Docker Hub credentials
3. Check Dockerfile for syntax errors

---

## 🧪 **Testing Your Release System**

### **Quick Test:**

```bash
# Make a small change
echo "// Test" >> src/js/main.js
git add src/js/main.js
git commit -m "Test release"
npm run release
```

### **Verify Results:**

1. **GitHub Actions**: Check Actions tab for successful build
2. **Docker Hub**: Verify images are published
3. **Git Tags**: `git tag --list` should show new tag
4. **Version**: `cat package.json | grep version` should show updated version

### **Undo Test Release:**

```bash
git tag -d v1.0.1
git push origin :refs/tags/v1.0.1
git reset --hard HEAD~1
```

---

## 🎉 **That's It!**

Your release system is now ready! Just follow the scenarios above based on your situation and run the appropriate `npm run release` command.

```

### File: SECURITY.md
```md
# Security Configuration

## Non-Root User Support

BentoPDF now uses nginx-unprivileged for enhanced security. This follows the Principle of Least Privilege and is essential for production environments.

### Security Benefits

- **Reduced Attack Surface**: If compromised, attackers won't have root privileges
- **Compliance**: Meets security standards like SOC 2, PCI DSS
- **Kubernetes/OpenShift Compatibility**: Works with security policies that require non-root execution
- **System Protection**: Prevents system-wide damage if the application is compromised

### Usage

#### Default Configuration (nginx-unprivileged)

```bash
docker build -t bentopdf .
docker run -p 8080:8080 bentopdf
```

#### Simple Mode

```bash
# Build with simple mode enabled
docker build --build-arg SIMPLE_MODE=true -t bentopdf-simple .

# Run the container
docker run -p 8080:8080 bentopdf-simple
```

#### Kubernetes Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: bentopdf
spec:
  template:
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 2000
        runAsGroup: 2000
      containers:
        - name: bentopdf
          image: bentopdf:latest
          ports:
            - containerPort: 8080
```

#### Docker Compose Example

```yaml
version: '3.8'
services:
  bentopdf:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        SIMPLE_MODE: false
    ports:
      - '8080:8080'
    security_opt:
      - no-new-privileges:true
```

### Verification

To verify the container is running as non-root:

```bash
# Check the user inside the container
docker exec <container_id> whoami
# Should output: nginx

# Check the user ID
docker exec <container_id> id
# Should show UID/GID for nginx user (typically 101)
```

### Security Best Practices

1. **Use nginx-unprivileged**: Built-in non-root user with minimal privileges
2. **Regular Updates**: Keep the base image updated (currently using 1.29-alpine)
3. **Port 8080**: Use high port numbers to avoid requiring root privileges
4. **Security Scanning**: Regularly scan images for vulnerabilities
5. **Network Policies**: Implement network segmentation

### Troubleshooting

If you encounter permission issues:

1. **Check file ownership**: Ensure all application files are owned by the nginx user
2. **Verify PID directory**: Ensure `/etc/nginx/tmp/` directory exists and is writable
3. **Port binding**: Ensure port 8080 is available and not blocked by firewall

### Migration from Root

If migrating from a root-based setup:

1. Update your Dockerfile to use nginx-unprivileged base image
2. Change port mappings from 80 to 8080 in all configurations
3. Update nginx.conf to use `/etc/nginx/tmp/nginx.pid` for PID file
4. Rebuild your images with the new security settings
5. Update your deployment configurations (Kubernetes, Docker Compose, etc.)
6. Test thoroughly in a staging environment

```

### File: SIMPLE_MODE.md
```md
# Simple Mode for BentoPDF

Simple Mode is designed for internal organizational use where you want to hide all branding and marketing content, showing only the essential PDF tools for your users.

## What Simple Mode Does

When enabled, Simple Mode will:

- Hide the navigation bar
- Hide the hero section with marketing content
- Hide the features section
- Hide the security/compliance section
- Hide the FAQ section
- Hide the testimonials section
- Hide the support section
- Hide the footer
- Update the page title to "PDF Tools"
- Make the tools section more prominent

## How to Enable Simple Mode

### Method 1: Using Pre-built Simple Mode Image (Recommended)

Use the pre-built Simple Mode image directly:

**Using GitHub Container Registry (Recommended):**

```bash
# Docker
docker run -p 3000:8080 ghcr.io/alam00000/bentopdf-simple:latest

# Podman
podman run -p 3000:8080 ghcr.io/alam00000/bentopdf-simple:latest
```

**Using Docker Hub:**

```bash
# Docker
docker run -p 3000:8080 bentopdfteam/bentopdf-simple:latest

# Podman
podman run -p 3000:8080 docker.io/bentopdfteam/bentopdf-simple:latest
```

Or with Docker Compose / Podman Compose:

```yaml
services:
  bentopdf:
    # Using GitHub Container Registry (Recommended)
    image: ghcr.io/alam00000/bentopdf-simple:latest
    # Or using Docker Hub
    # image: bentopdfteam/bentopdf-simple:latest
    container_name: bentopdf
    restart: unless-stopped
    ports:
      - '3000:8080'
```

### Method 2: Using Docker Compose with Build

Build the image locally with Simple Mode enabled:

```bash
docker compose -f docker-compose.dev.yml build --build-arg SIMPLE_MODE=true
docker compose -f docker-compose.dev.yml up -d
```

### Method 3: Using Docker Build

Build the image with the SIMPLE_MODE build argument:

```bash
docker build --build-arg SIMPLE_MODE=true -t bentopdf-simple .
docker run -p 3000:8080 bentopdf-simple
```

### Method 4: Using npm Script (Easiest for Local Development)

Use the built-in npm script that handles everything:

```bash
npm run serve:simple
```

This command automatically:

- Sets `SIMPLE_MODE=true`
- Builds the project with Simple Mode enabled
- Serves the built files on `http://localhost:3000`

### Method 5: Using Environment Variables

Set the environment variable before building:

```bash
export SIMPLE_MODE=true
npm run build
npx serve dist -p 3000
```

## 🧪 Testing Simple Mode Locally

### Method 1: Using npm Script (Easiest for Development)

```bash
npm run serve:simple
```

This automatically builds and serves Simple Mode on `http://localhost:3000`.

### Method 2: Using Pre-built Image (Easiest for Production)

```bash
# Docker - Pull and run the Simple Mode image
docker pull ghcr.io/alam00000/bentopdf-simple:latest
docker run -p 3000:8080 ghcr.io/alam00000/bentopdf-simple:latest

# Podman
podman pull ghcr.io/alam00000/bentopdf-simple:latest
podman run -p 3000:8080 ghcr.io/alam00000/bentopdf-simple:latest
```

Open `http://localhost:3000` in your browser.

### Method 3: Build and Test Locally

```bash
# Build with simple mode
SIMPLE_MODE=true npm run build

# Serve the built files
npx serve dist -p 3000
```

Open `http://localhost:3000` in your browser.

### Method 4: Compare Both Modes

```bash
# Test Normal Mode (Docker)
docker run -p 3000:8080 ghcr.io/alam00000/bentopdf:latest

# Test Simple Mode (Docker)
docker run -p 3001:8080 ghcr.io/alam00000/bentopdf-simple:latest

# Podman users: replace 'docker' with 'podman'
```

- Normal Mode: `http://localhost:3000`
- Simple Mode: `http://localhost:3001`

## 🔍 What to Look For

When Simple Mode is working correctly, you should see:

- ✅ Clean "PDF Tools" header (no marketing hero section)
- ✅ "Select a tool to get started" subtitle
- ✅ Search bar for tools
- ✅ All PDF tool cards organized by category
- ❌ No navigation bar
- ❌ No hero section with "The PDF Toolkit built for privacy"
- ❌ No features, FAQ, testimonials, or footer sections

## 📦 Available Container Images

### Normal Mode (Full Branding)

**GitHub Container Registry (Recommended):**

- `ghcr.io/alam00000/bentopdf:latest`
- `ghcr.io/alam00000/bentopdf:v1.0.0` (versioned)

**Docker Hub:**

- `bentopdfteam/bentopdf:latest`
- `bentopdfteam/bentopdf:v1.0.0` (versioned)

### Simple Mode (Clean Interface)

**GitHub Container Registry (Recommended):**

- `ghcr.io/alam00000/bentopdf-simple:latest`
- `ghcr.io/alam00000/bentopdf-simple:v1.0.0` (versioned)

**Docker Hub:**

- `bentopdfteam/bentopdf-simple:latest`
- `bentopdfteam/bentopdf-simple:v1.0.0` (versioned)

## 🚀 Production Deployment Examples

### Docker Compose / Podman Compose

```yaml
services:
  bentopdf:
    image: ghcr.io/alam00000/bentopdf-simple:latest # Recommended
    # image: bentopdfteam/bentopdf-simple:latest     # Alternative: Docker Hub
    container_name: bentopdf
    restart: unless-stopped
    ports:
      - '80:8080'
    environment:
      - PUID=1000
      - PGID=1000
```

### Podman Quadlet (Linux Systemd)

Create `~/.config/containers/systemd/bentopdf-simple.container`:

```ini
[Unit]
Description=BentoPDF Simple Mode
After=network-online.target

[Container]
Image=ghcr.io/alam00000/bentopdf-simple:latest
ContainerName=bentopdf-simple
PublishPort=80:8080
AutoUpdate=registry

[Service]
Restart=always

[Install]
WantedBy=default.target
```

Enable and start:

```bash
systemctl --user daemon-reload
systemctl --user enable --now bentopdf-simple
```

## ⚠️ Important Notes

- **Pre-built images**: Use `ghcr.io/alam00000/bentopdf-simple:latest` for Simple Mode (recommended)
- **Environment variables**: `SIMPLE_MODE=true` only works during build, not runtime
- **Build-time optimization**: Simple Mode uses dead code elimination for smaller bundles
- **Same functionality**: All PDF tools work identically in both modes

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
