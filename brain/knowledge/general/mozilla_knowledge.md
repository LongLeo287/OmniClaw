---
id: mozilla-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:09.803481
---

# KNOWLEDGE EXTRACT: mozilla
> **Extracted on:** 2026-03-30 17:43:02
> **Source:** mozilla

---

## File: `inclusion.md`
```markdown
# 📦 mozilla/inclusion [🔖 PENDING/APPROVE]
🔗 https://github.com/mozilla/inclusion


## Meta
- **Stars:** ⭐ 1047 | **Forks:** 🍴 527
- **Language:** N/A | **License:** MPL-2.0
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Our repository for Diversity, Equity and Inclusion work at Mozilla

## README (trích đầu)
```
# Diversity & Inclusion in Open Source

Welcome!  This repository contains a number of resources, templates, standards and other useful things for open (source, education, knowledge, science) projects.  

   * [Table of Contents](#diversity--inclusion-in-open-source)
      * [Code of Conduct  Enforcement](#code-of-conduct--enforcement)
      * [Education &amp; Training](#education--training)
      * [Data &amp; Metrics Standards](#data--metrics-standards)
      * [Evaluation Resources/Tools](#evaluation-resourcestools)
      * [Research](#research)
      * [Media / Articles / Blog Posts](#media--articles--blog)

## Code of Conduct  Enforcement

* [Mozilla Community Participation Guidelines](https://www.mozilla.org/en-US/about/governance/policies/participation/)
* [Mozilla 'How to Report' Page](https://www.mozilla.org/en-US/about/governance/policies/participation/reporting/)

#### Related Blog Posts

* [Frameworks for Governance, Incentive and Consequence](https://medium.com/mozilla-open-innovation/frameworks-for-governance-incentive-and-consequence-in-foss-e1de6c091bdc) (2017)
* [How We're Making Code of Conduct Enforcement Real, and Scaling it](https://medium.com/mozilla-open-innovation/how-were-making-code-of-conduct-enforcement-real-and-scaling-it-3e382cf94415) (2018)

#### Process Standards for Enforcement
* [Rolling out an all project/systems ban](https://github.com/mozilla/diversity/blob/master/code-of-conduct-enforcement/process_documentation/community/ban-rollout.md)
* [Consequence Ladder](https://github.com/mozilla/diversity/blob/master/code-of-conduct-enforcement/consequence-ladder.md)
* [Template - CPG/Code of Conduct 'Onboarding'](https://github.com/mozilla/diversity/blob/master/code-of-conduct-enforcement/cpg-onboarding.md)
* [Template - Decision Making](https://github.com/mozilla/diversity/blob/master/code-of-conduct-enforcement/investigation/working-group/role-groups.md)

#### Investigation & Decision Making
* [Template - Decision Tracking Doc](https://github.com/mozilla/inclusion/blob/master/code-of-conduct-enforcement/investigation/working-group/decision.md)
* [Template - Working Group 1st Agenda](https://github.com/mozilla/diversity/blob/master/code-of-conduct-enforcement/investigation/working-group/working-group-first-agenda.md)
* [Template - Working Group Standard Agenda](https://github.com/mozilla/diversity/blob/master/code-of-conduct-enforcement/investigation/working-group/working-group-standard-agenda.md)
* [Template - Investigation documentation](https://github.com/mozilla/diversity/blob/master/code-of-conduct-enforcement/investigation/working-group/incident-investigation-template.md)

##### Investigation Communication
* [Template - Request for Clarification(from reporter)](https://github.com/mozilla/diversity/blob/master/code-of-conduct-enforcement/triage/communications/more-information.md)
* [Template - Receipt of Report (to reporter)](https://github.com/mozilla/diversity/blob/master/code-of-conduct-enforcement/investiga
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pdf.js.md`
```markdown
# 📦 mozilla/pdf.js [🔖 PENDING]
🔗 https://github.com/mozilla/pdf.js
🌐 https://mozilla.github.io/pdf.js/

## Meta
- **Stars:** ⭐ 53038 | **Forks:** 🍴 10607
- **Language:** JavaScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
PDF Reader in JavaScript

## README (trích đầu)
```
# PDF.js [![CI](https://github.com/mozilla/pdf.js/actions/workflows/ci.yml/badge.svg?query=branch%3Amaster)](https://github.com/mozilla/pdf.js/actions/workflows/ci.yml?query=branch%3Amaster) [![codecov](https://codecov.io/gh/mozilla/pdf.js/branch/master/graph/badge.svg)](https://codecov.io/gh/mozilla/pdf.js)

[PDF.js](https://mozilla.github.io/pdf.js/) is a Portable Document Format (PDF) viewer that is built with HTML5.

PDF.js is community-driven and supported by Mozilla. Our goal is to
create a general-purpose, web standards-based platform for parsing and
rendering PDFs.

## Contributing

PDF.js is an open source project and always looking for more contributors. To
get involved, visit:

+ [Issue Reporting Guide](https://github.com/mozilla/pdf.js/blob/master/.github/CONTRIBUTING.md)
+ [Code Contribution Guide](https://github.com/mozilla/pdf.js/wiki/Contributing)
+ [Frequently Asked Questions](https://github.com/mozilla/pdf.js/wiki/Frequently-Asked-Questions)
+ [Good Beginner Bugs](https://github.com/mozilla/pdf.js/issues?q=is%3Aissue%20state%3Aopen%20label%3Agood-beginner-bug)
+ [Projects](https://github.com/mozilla/pdf.js/projects)

Feel free to stop by our [Matrix room](https://chat.mozilla.org/#/room/#pdfjs:mozilla.org) for questions or guidance.

## Getting Started

### Online demo

Please note that the "Modern browsers" version assumes native support for the
latest JavaScript features; please also see [this wiki page](https://github.com/mozilla/pdf.js/wiki/Frequently-Asked-Questions#faq-support).

+ Modern browsers: https://mozilla.github.io/pdf.js/web/viewer.html

+ Older browsers: https://mozilla.github.io/pdf.js/legacy/web/viewer.html

### Browser Extensions

#### Firefox

PDF.js is built into version 19+ of Firefox.

#### Chrome

+ The official extension for Chrome can be installed from the [Chrome Web Store](https://chrome.google.com/webstore/detail/pdf-viewer/oemmndcbldboiebfnladdacbdfmadadm).
*This extension is maintained by [@Rob--W](https://github.com/Rob--W).*
+ Build Your Own - Get the code as explained below and issue `npx gulp chromium`. Then open
Chrome, go to `Tools > Extension` and load the (unpackaged) extension from the
directory `build/chromium`.

### PDF debugger

Browser the internal structure of a PDF document with https://mozilla.github.io/pdf.js/internal-viewer/web/debugger.html

## Getting the Code

To get a local copy of the current code, clone it using git:

    $ git clone https://github.com/mozilla/pdf.js.git
    $ cd pdf.js

Next, install Node.js via the [official package](https://nodejs.org) or via
[nvm](https://github.com/creationix/nvm). If everything worked out, install
all dependencies for PDF.js:

    $ npm install

Finally, you need to start a local web server as some browsers do not allow opening
PDF files using a `file://` URL. Run:

    $ npx gulp server

and then you can open:

+ http://localhost:8888/web/viewer.html

Please keep in mind that this assumes the latest version of Mozilla Firefox; refer 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

