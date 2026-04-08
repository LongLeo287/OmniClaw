---
id: repo-fetched-charts-141003
type: knowledge
owner: OA
registered_at: 2026-04-05T04:08:56.380260
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_charts_141003

## Assimilation Report
Auto-cloned repository: FETCHED_charts_141003

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<!-- markdownlint-disable MD041 -->
<p align="center">
    <img width="400px" height=auto src="https://dyltqmyl993wv.cloudfront.net/bitnami/bitnami-by-vmware.png" />
</p>

<p align="center">
    <a href="https://twitter.com/bitnami"><img src="https://badgen.net/badge/twitter/@bitnami/1DA1F2?icon&label" /></a>
    <a href="https://github.com/bitnami/charts"><img src="https://badgen.net/github/stars/bitnami/charts?icon=github" /></a>
    <a href="https://github.com/bitnami/charts"><img src="https://badgen.net/github/forks/bitnami/charts?icon=github" /></a>
    <a href="https://artifacthub.io/packages/search?repo=bitnami"><img src="https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/bitnami" /></a>
</p>

# The Bitnami Library for Kubernetes

Popular applications, provided by [Bitnami](https://bitnami.com), ready to launch on Kubernetes using [Kubernetes Helm](https://github.com/helm/helm).

## TL;DR

```console
helm install my-release oci://registry-1.docker.io/bitnamicharts/<chart>
```

## Why use Bitnami Secure Images?

Those are hardened, minimal CVE images built and maintained by Bitnami. Bitnami Secure Images are based on the cloud-optimized, security-hardened enterprise [OS Photon Linux](https://vmware.github.io/photon/). Why choose BSI images?

- Hardened secure images of popular open source software with Near-Zero Vulnerabilities
- Vulnerability Triage & Prioritization with VEX Statements, KEV and EPSS Scores
- Compliance focus with FIPS, STIG, and air-gap options, including secure bill of materials (SBOM)
- Software supply chain provenance attestation through in-toto
- First class support for the internet’s favorite Helm charts

Each image comes with valuable security metadata. You can view the metadata in [our public catalog here](https://app-catalog.vmware.com/bitnami/apps). Note: Some data is only available with [commercial subscriptions to BSI](https://bitnami.com/).

![Alt text](https://github.com/bitnami/containers/blob/main/BSI%20UI%201.png?raw=true "Application details")
![Alt text](https://github.com/bitnami/containers/blob/main/BSI%20UI%202.png?raw=true "Packaging report")

If you are looking for our previous generation of images based on Debian Linux, please see the [Bitnami Legacy registry](https://hub.docker.com/u/bitnamilegacy).

## Vulnerabilities scanner

Each Helm chart contains one or more containers. Those containers use images provided by Bitnami through its test & release pipeline and whose source code can be found at [bitnami/containers](https://github.com/bitnami/containers).

As part of the container releases, the images are scanned for vulnerabilities, [here](https://github.com/bitnami/containers#vulnerability-scan-in-bitnami-container-images) you can find more info about this topic.

Since the container image is an immutable artifact that is already analyzed, as part of the Helm chart release process we are not looking for vulnerabilities in the containers but running different verifications to ensure the Helm charts work as expected, see the testing strategy defined at [_TESTING.md_](https://github.com/bitnami/charts/blob/main/TESTING.md).

## Before you begin

### Prerequisites

- Kubernetes 1.23+
- Helm 3.8.0+

### Setup a Kubernetes Cluster

The quickest way to set up a Kubernetes cluster to install Bitnami Charts is by following the "Bitnami Get Started" guides for the different services:

- [Get Started with Bitnami Charts using VMware Tanzu Kubernetes Grid (TKG)](https://docs.bitnami.com/kubernetes/get-started-tkg/)
- [Get Started with Bitnami Charts using VMware Tanzu Mission Control (TMC)](https://docs.bitnami.com/kubernetes/get-started-tmc/)
- [Get Started With Bitnami Charts Using Azure Marketplace Kubernetes Applications](https://docs.bitnami.com/kubernetes/get-started-cnab/)
- [Get Started with Bitnami Charts using the Amazon Elastic Container Service for Kubernetes (EKS)](https://docs.bitnami.com/kubernetes/get-started-eks/)
- [Get Started with Bitnami Charts using the Google Kubernetes Engine (GKE)](https://docs.bitnami.com/kubernetes/get-started-gke/)

For setting up Kubernetes on other cloud platforms or bare-metal servers refer to the Kubernetes [getting started guide](https://kubernetes.io/docs/getting-started-guides/).

### Install Helm

Helm is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources.

To install Helm, refer to the [Helm install guide](https://github.com/helm/helm#install) and ensure that the `helm` binary is in the `PATH` of your shell.

### Using Helm

Once you have installed the Helm client, you can deploy a Bitnami Helm Chart into a Kubernetes cluster.

Please refer to the [Quick Start guide](https://helm.sh/docs/intro/quickstart/) if you wish to get running in just a few commands, otherwise, the [Using Helm Guide](https://helm.sh/docs/intro/using_helm/) provides detailed instructions on how to use the Helm client to manage packages on your Kubernetes cluster.

Useful Helm Client Commands:

- Install a chart: `helm install my-release oci://registry-1.docker.io/bitnamicharts/<chart>`
- Upgrade your application: `helm upgrade my-release oci://registry-1.docker.io/bitnamicharts/<chart>`

## License

Copyright &copy; 2026 Broadcom. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Code of Conduct

As contributors and maintainers of the "Bitnami Charts" project, we pledge to respect everyone who contributes by posting issues, updating documentation, submitting pull requests, providing feedback in comments, and any other activities.

Communication through any of Bitnami's channels (GitHub, mailing lists, Twitter, and so on) must be constructive and never resort to personal attacks, trolling, public or private harassment, insults, or other unprofessional conduct.

We promise to extend courtesy and respect to everyone involved in this project, regardless of gender, gender identity, sexual orientation, disability, age, race, ethnicity, religion, or level of experience. We expect anyone contributing to the "Bitnami Charts" project to do the same.

If any member of the community violates this code of conduct, the maintainers of the "Bitnami Charts" project may take action, including removing issues, comments, and PRs or blocking accounts, as deemed appropriate.

If you are subjected to or witness unacceptable behavior, or have any other concerns, please communicate with us.

If you have suggestions to improve this Code of Conduct, please submit an issue or PR.

## Attribution

This Code of Conduct is adapted from the Angular project available at this page: <https://github.com/angular/code-of-conduct/blob/master/CODE_OF_CONDUCT.md>

```

### File: CONTRIBUTING.md
```md
# Contributing Guidelines

Contributions are welcome via GitHub Pull Requests. This document outlines the process to help get your contribution accepted.

Any type of contribution is welcome; from new features, bug fixes, [tests](#testing), documentation improvements, or even [adding charts to the repository](#adding-a-new-chart-to-the-repository) (if it's viable once evaluated the feasibility).

## How to Contribute

1. Fork this repository, develop, and test your changes.
2. Submit a pull request.

>[!NOTE]
> To make the Pull Requests' (PRs) merging process easier, please submit changes to multiple charts in separate PRs.

### Technical Requirements

When submitting a PR make sure that it:

- Must follow [Helm best practices](https://helm.sh/docs/chart_best_practices/).
- Any change to a chart requires a version bump following [semver](https://semver.org/) principles.
- Any change to a Helm template (especially new templates) must include a license header like the following:

```yaml
{{- /*
Copyright Broadcom, Inc. All Rights Reserved.
SPDX-License-Identifier: APACHE-2.0
*/}}
```

#### Sign Your Work

The sign-off is a simple line at the end of the explanation for a commit. All commits need to be signed. Your signature certifies that you wrote the patch or otherwise have the right to contribute the material. The rules are pretty simple, you only need to certify the guidelines from [developercertificate.org](https://developercertificate.org/).

Then you just add a line to every git commit message:

```text
Signed-off-by: Joe Smith <joe.smith@example.com>
```

Use your real name (sorry, no pseudonyms or anonymous contributions.)

If you set your `user.name` and `user.email` git configs, you can sign your commit automatically with `git commit -s`.

Note: If your git config information is set properly then viewing the `git log` information for your commit will look something like this:

```text
Author: Joe Smith <joe.smith@example.com>
Date:   Thu Feb 2 11:41:15 2018 -0800

    Update README

    Signed-off-by: Joe Smith <joe.smith@example.com>
```

Notice the `Author` and `Signed-off-by` lines match. If they don't your PR will be rejected by the automated DCO check.

### Documentation Requirements

- A chart's `README.md` must include configuration options. The tables of parameters are generated based on the metadata information from the `values.yaml` file, by using [this tool](https://github.com/bitnami/readme-generator-for-helm).
- A chart's `NOTES.txt` must include relevant post-installation information.
- The title of the PR starts with chart name (e.g. `[bitnami/chart]`)


```

### File: LICENSE.md
```md
Copyright &copy; 2025 Broadcom. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
SPDX-License-Identifier: APACHE-2.0

This product includes third-party open source software. Additional copyright and licensing information can be found inside the Bitnami packages themselves and/or at https://bitnami.com/open-source

----
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

### File: SECURITY.md
```md
# Security Release Process

The community has adopted this security disclosure and response policy to ensure we responsibly handle critical issues.

## Supported Versions

For a list of support versions that this project will potentially create security fixes for, please refer to the Releases page on this project's GitHub and/or project related documentation on release cadence and support.

## Reporting a Vulnerability - Private Disclosure Process

Security is of the highest importance and all security vulnerabilities or suspected security vulnerabilities should be reported to this project privately, to minimize attacks against current users  before they are fixed. Vulnerabilities will be investigated and patched on the next patch (or minor) release as soon as possible. This information could be kept entirely internal to the project.

If you know of a publicly disclosed security vulnerability for this project, please **IMMEDIATELY** contact the maintainers of this project privately. The use of encrypted email is encouraged.

**IMPORTANT**: Do not file public issues on GitHub for security vulnerabilities

To report a vulnerability or a security-related issue, please contact the maintainers with enough details through one of the following channels:

* Directly via their individual email addresses
* Open a [GitHub Security Advisory](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability). This allows for anyone to report security vulnerabilities directly and privately to the maintainers via GitHub. Note that this option may not be present for every repository.

The report will be fielded by the maintainers who have committer and release permissions. Feedback will be sent within 3 business days, including a detailed plan to investigate the issue and any potential workarounds to perform in the meantime.

Do not report non-security-impacting bugs through this channel. Use GitHub issues for all non-security-impacting bugs.

## Proposed Report Content

Provide a descriptive title and in the description of the report include the following information:

* Basic identity information, such as your name and your affiliation or company.
* Detailed steps to reproduce the vulnerability  (POC scripts, screenshots, and logs are all helpful to us).
* Description of the effects of the vulnerability on this project and the related hardware and software configurations, so that the maintainers can reproduce it.
* How the vulnerability affects this project's usage and an estimation of the attack surface, if there is one.
* List other projects or dependencies that were used in conjunction with this project to produce the vulnerability.

## When to report a vulnerability

* When you think this project has a potential security vulnerability.
* When you suspect a potential vulnerability but you are unsure that it impacts this project.
* When you know of or suspect a potential vulnerability on another project that is used by this project.

## Patch, Release, and Disclosure

The maintainers will respond to vulnerability reports as follows:

1. The maintainers will investigate the vulnerability and determine its effects and criticality.
2. If the issue is not deemed to be a vulnerability, the maintainers will follow up with a detailed reason for rejection.
3. The maintainers will initiate a conversation with the reporter within 3 business days.
4. If a vulnerability is acknowledged and the timeline for a fix is determined, the maintainers will work on a plan to communicate with the appropriate community, including identifying mitigating steps that affected users can take to protect themselves until the fix is rolled out.
5. The maintainers will also create a [Security Advisory](https://docs.github.com/en/code-security/repository-security-advisories/publishing-a-repository-security-advisory) using the [CVSS Calculator](https://www.first.org/cvss/calculator/3.0), if it is not created yet.  The maintainers make the final call on the calculated CVSS; it is better to move quickly than making the CVSS perfect. Issues may also be reported to [Mitre](https://cve.mitre.org/) using this [scoring calculator](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator). The draft advisory will initially be set to private.
6. The maintainers will work on fixing the vulnerability and perform internal testing before preparing to roll out the fix.
7. Once the fix is confirmed, the maintainers will patch the vulnerability in the next patch or minor release, and backport a patch release into all earlier supported releases.

## Public Disclosure Process

The maintainers publish the public advisory to this project's community via GitHub. In most cases, additional communication via Slack, Twitter, mailing lists, blog, and other channels will assist in educating the project's users and rolling out the patched release to affected users.

The maintainers will also publish any mitigating steps users can take until the fix can be applied to their instances. This project's distributors will handle creating and publishing their own security advisories.

## Confidentiality, integrity and availability

We consider vulnerabilities leading to the compromise of data confidentiality, elevation of privilege, or integrity to be our highest priority concerns. Availability, in particular in areas relating to DoS and resource exhaustion, is also a serious security concern. The maintainer team takes all vulnerabilities, potential vulnerabilities, and suspected vulnerabilities seriously and will investigate them in an urgent and expeditious manner.

Note that we do not currently consider the default settings for this project to be secure-by-default. It is necessary for operators to explicitly configure settings, role based access control, and other resource related features in this project to provide a hardened environment. We will not act on any security disclosure that relates to a lack of safe defaults. Over time, we will work towards improved safe-by-default configuration, taking into account backwards compatibility.

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for charts
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
<!--
 Before you open the request please review the following guidelines and tips to help it be more easily integrated:

 - Describe the scope of your change - i.e. what the change does.
 - Describe any known limitations with your change.
 - Please run any tests or examples that can exercise your modified code.

 Thank you for contributing! We will try to test and integrate the change as soon as we can, but be aware we have many GitHub repositories to manage and can't immediately respond to every request. There is no need to bump or check in on a pull request (it will clutter the discussion of the request).

 Also don't be worried if the request is closed or not integrated sometimes the priorities of Bitnami might not match the priorities of the pull request. Don't fret, the open source community thrives on forks and GitHub makes it easy to keep your changes in a forked repo.
 -->

### Description of the change

<!-- Describe the scope of your change - i.e. what the change does. -->

### Benefits

<!-- What benefits will be realized by the code change? -->

### Possible drawbacks

<!-- Describe any known limitations with your change -->

### Applicable issues

<!-- Enter any applicable Issues here (You can reference an issue using #) -->
- fixes #

### Additional information

<!-- If there's anything else that's important and relevant to your pull request, mention that information here.-->

### Checklist

<!-- [Place an '[X]' (no spaces) in all applicable fields. Please remove unrelated fields.] -->

- [ ] Chart version bumped in `Chart.yaml` according to [semver](http://semver.org/). This is *not necessary* when the changes only affect README.md files.
- [ ] Variables are documented in the values.yaml and added to the `README.md` using [readme-generator-for-helm](https://github.com/bitnami/readme-generator-for-helm)
- [ ] Title of the pull request follows this pattern [bitnami/<name_of_the_chart>] Descriptive title
- [ ] All commits signed off and in agreement of [Developer Certificate of Origin (DCO)](https://github.com/bitnami/charts/blob/main/CONTRIBUTING.md#sign-your-work)

```

