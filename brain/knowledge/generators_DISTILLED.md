---
id: generators
type: knowledge
owner: OA_Triage
---
# generators
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "eventcatalog-generators",
  "scripts": {
    "build": "turbo build",
    "dev": "turbo dev",
    "lint": "turbo lint",
    "clean": "turbo clean && rm -rf node_modules",
    "test": "turbo run test",
    "changeset": "changeset",
    "version-packages": "changeset version",
    "release": "turbo build && changeset publish",
    "format": "prettier --write . --ignore-path .prettierignore",
    "format:diff": "prettier --list-different . --ignore-path .prettierignore",
    "publish-packages": "turbo run build lint test && changeset version && changeset publish"
  },
  "devDependencies": {
    "@changesets/cli": "^2.27.12",
    "@types/update-notifier": "^6.0.8",
    "prettier": "^3.4.2",
    "turbo": "^2.4.0",
    "typescript": "5.7.3"
  },
  "packageManager": "pnpm@9.0.0",
  "engines": {
    "node": ">=18"
  },
  "dependencies": {
    "@eventcatalog/license": "^0.0.7",
    "boxen": "^8.0.1",
    "chalk": "4.1.2",
    "update-notifier": "^7.3.1"
  },
  "pnpm": {
    "overrides": {
      "graphql": "^16.8.1"
    }
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/event-catalog/generators"
  }
}

```

### File: README.md
```md
# EventCatalog Generators

This repository contains the generators for the EventCatalog project.

## Integration list with EventCatalog

- [OpenAPI](./packages/generator-openapi/README.md)
  - [Documentation](https://www.eventcatalog.dev/integrations/openapi)
  - [Example Projects](./examples/generator-openapi/)
- [AsyncAPI](./packages/generator-asyncapi/README.md)
  - [Documentation](https://www.eventcatalog.dev/integrations/asyncapi)
  - [Example Projects](./examples/generator-asyncapi/)
- [GraphQL](./packages/generator-graphql/README.md)
  - [Documentation](https://www.eventcatalog.dev/integrations/graphql)
  - [Example Projects](./examples/generator-graphql/)
- [EventCatalog AI](./packages/generator-ai/README.md)
  - [Documentation](https://www.eventcatalog.dev/integrations/ai)
- [EventCatalog Federation](./packages/generator-federation/README.md)
  - [Documentation](https://www.eventcatalog.dev/federation)
- [Amazon EventBridge](./packages/generator-eventbridge/README.md)
  - [Documentation](https://www.eventcatalog.dev/integrations/amazon-eventbridge)
- [Backstage](https://github.com/event-catalog/backstage-plugin-eventcatalog)
  - [Documentation](https://www.eventcatalog.dev/integrations/backstage)
- [AWS Glue Schema Registry](./packages/generator-aws-glue/README.md)
  - [Documentation](https://www.eventcatalog.dev/integrations/aws-glue-registry)
- [GitHub (As Schema Registry)](./packages/generator-github/README.md)
  - [Documentation](https://www.eventcatalog.dev/integrations/github)
- [Confluent Schema Registry](./packages/generator-confluent-schema-registry/README.md)
  - [Documentation](https://www.eventcatalog.dev/integrations/confluent-schema-registry)

All plugins require a license key. You can get a license key from [EventCatalog Cloud](https://eventcatalog.cloud).

---

## Examples

**OpenAPI Integrations [(watch demo)](https://www.youtube.com/watch?v=E6cXxQXH49k)**

- [Integrate OpenAPI files into EventCatalog](./examples/generator-openapi/)
- [Integrate OpenAPI files from remote URLs into EventCatalog](./examples/generator-openapi/fetch-from-remote-urls/)
- [Mapping commands, events and queries using the `x-eventcatalog-message-type` extension](./examples/generator-openapi/mapping-commands-events-queries/)
- [Independent Message Versioning using the `x-eventcatalog-message-version` extension](./examples/generator-openapi/independent-message-versioning/)

**AsyncAPI Integrations [(watch demo)](https://www.youtube.com/watch?v=XglwSNAnpKY)**

- [Integrate AsyncAPI files into EventCatalog](./examples/generator-asyncapi/)
- [Integrate AsyncAPI files from remote URLs into EventCatalog](./examples/generator-asyncapi/fetch-from-remote-urls/)
- [Mapping commands, events and queries using the `x-eventcatalog-message-type` extension](./examples/generator-asyncapi/mapping-commands-events-queries/)
- [Independent Message Versioning using the `x-eventcatalog-message-version` extension](./examples/generator-asyncapi/independent-message-versioning/)
- [Message Ownership using the `x-eventcatalog-role` extension to control which service owns a message](./examples/generator-asyncapi/message-ownership/)
  - EventCatalog will parse all messages, sometimes this leads to duplicated messages being created.
  - The `x-eventcatalog-role` extension can be used to control which service owns a message.
  - This is useful when you have multiple AsyncAPI files that define the same message.

**GraphQL Integrations**

- [Integrate GraphQL files into EventCatalog](./examples/generator-graphql/)

**EventBridge Integrations [(watch demo)](https://www.youtube.com/watch?v=MeBuwAflwM4)**

- [Import EventBridge schemas into EventCatalog using schema discovery](./examples/generator-eventbridge/basic/)
- [Import EventBridge schemas into EventCatalog using a custom schema registry](./examples/generator-eventbridge/custom-registry/)

**EventCatalog Federation [(watch demo)](https://www.youtube.com/watch?v=KnTQkrt-7cc)**

- [Merge multiple catalogs into one central catalog](./examples/generator-federation/basic/)
  - Give your teams their own EventCatalog instance, and use the federation plugin to merge them together.
  - Let your teams focus on what they do best, and use the federation plugin to merge their documentation together.
  - The central catalog is hosted for the organization where people can view the merged catalog and single source of truth.

**Backstage Integrations [(watch demo)](https://www.youtube.com/watch?v=mjf7qwoSAC4)**

- [Integrate Backstage plugin into EventCatalog](https://github.com/event-catalog/backstage-eventcatalog-demo)

**AWS Glue Schema Registry**

- [Integrate AWS Glue Schema Registry into EventCatalog](./examples/generator-glue-registry/basic/)

**Multi Generator Example**

- [Integrate multiple generators (AsyncAPI and OpenAPI) into EventCatalog](./examples/multi-generator-example/)

---

## Found a problem?

Raise a GitHub issue on this project, or contact us on [our Discord server](https://discord.gg/3rjaZMmrAm).

## Commercial use

All plugins are licensed under a [dual-license](./LICENSE-COMMERCIAL.md). To ensure the sustainability of the project, you can freely make use of this software if your projects are Open Source. Otherwise for internal systems you must obtain a [commercial license](./LICENSE-COMMERCIAL.md).

If you would like to obtain a Commercial License, you can get a free trial (14 days) per plugin at https://eventcatalog.cloud or email us at `hello@eventcatalog.dev`

<!-- # Sponsors

Thank you to our project sponsors.

## Gold sponsors

<div align="center">
  <img alt="gravitee" src="./images/sponsors/gravitee-logo-black.svg" width="50%" />
  <p style="margin: 0; padding: 0;">Manage, secure, and govern every API in your organization</p>
  <a href="https://gravitee.io?utm_source=eventcatalog&utm_medium=web&utm_campaign=sponsorship" target="_blank" >Learn more</a>
</div>

<hr />

_Sponsors help make EventCatalog sustainable, want to help the project? Get in touch! Or [visit our sponsor page](https://github.com/sponsors/event-catalog)._ -->

# Enterprise support

Interested in collaborating with us? Our offerings include dedicated support, priority assistance, feature development, custom integrations, and more.

Find more details on our [services page](https://eventcatalog.dev/services).

# Contributing

If you have any questions, features or issues please raise any issue or pull requests you like. We will try my best to get back to you.

You can find the [contributing guidelines here](https://eventcatalog.dev/docs/contributing/overview).

```

### File: .changeset\README.md
```md
# Changesets

Hello and welcome! This folder has been automatically generated by `@changesets/cli`, a build tool that works
with multi-package repos, or single-package repos to help you version and publish your code. You can
find the full documentation for it [in our repository](https://github.com/changesets/changesets)

We have a quick list of common questions to get you started engaging with this project in
[our documentation](https://github.com/changesets/changesets/blob/main/docs/common-questions.md)

```

### File: AGENTS.md
```md
# AGENTS.md

Read and follow all instructions in @CLAUDE.md

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This project is a monorepo that contains the EventCatalog generators. These are plugins that generate documentation for EventCatalog using the EventCatalog SDK.

## Build, Lint, and Test Commands

- **Build**: `pnpm run verify-build:catalog`
- **Test**: `pnpm run test`
- **Format and lint code**: `pnpm run format`

## Code Style Guidelines

### TypeScript

- Strict typing with TypeScript
- ES modules with explicit imports/exports
- Error handling with proper type guards

## Project Structure

- `/packages` - The location of the EventCatalog generators
- `/examples` - Examples of EventCatalog using the generators

Follow existing patterns when adding new code.

## Plan Mode

- Make the plan extremely concise. Sacrifice grammar for the sake of concision.
- At the end of each plan, give me a list of unresolved questions to answer, if any.

```

### File: LICENSE-COMMERCIAL.md
```md
The EventCatalog Commercial License (the "Commercial License")
Copyright (c) 2024-2026 EventCatalog Ltd

With regard to the EventCatalog Software:

This software and associated documentation files (the "Software") may only be
used in production for proprietary, internal, or commercial purposes, if you
(and any entity that you represent) have agreed to, and are in compliance with,
the EventCatalog Terms of Service available at
https://www.eventcatalog.dev/terms, or other agreements governing the use of
the Software, as mutually agreed by you and EventCatalog Ltd ("EventCatalog"),
and otherwise have a valid EventCatalog Starter, Scale, or Enterprise
subscription, or a valid individual plugin license ("Commercial License").

A 14-day free trial of the Software is available at https://eventcatalog.cloud/
to help you evaluate the Software before purchasing a Commercial License.

Subject to the foregoing sentence, you are free to modify this Software and
publish patches to the Software. You agree that EventCatalog and/or its
licensors (as applicable) retain all right, title and interest in and to all
such modifications and/or patches, and all such modifications and/or patches
may only be used, copied, modified, displayed, distributed, or otherwise
exploited with a valid Commercial License.

Notwithstanding the foregoing, you may copy and modify the Software for
development and testing purposes, without requiring a subscription. You agree
that EventCatalog and/or its licensors (as applicable) retain all right, title
and interest in and to all such modifications. You are not granted any other
rights beyond what is expressly stated herein. Subject to the foregoing, it is
forbidden to copy, merge, publish, distribute, sublicense, and/or sell the
Software.

You may not move, change, disable, or circumvent the license key functionality
in the Software, and you may not remove or obscure any functionality in the
Software that is protected by the license key.

This Software is source-available for the purposes of transparency and
auditability. Source availability does not constitute a grant of rights to use
the Software in production without a valid Commercial License.

When Do You Need a Commercial License?

You need a Commercial License if:

- You are using the Software for internal business purposes and do not wish to
  release your source code under the AGPL-3.0 license.
- You are building proprietary software or SaaS platforms where you do not want
  to share the source code with customers or the public.
- You are creating a closed-source product that incorporates this Software.

If your project is open source and you are willing to release your source code
under the AGPL-3.0 license, you may use the Software under the terms of the
AGPL-3.0 license instead. See LICENSE-OPENSOURCE.md for those terms.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

For all third party components incorporated into the EventCatalog Software,
those components are licensed under the original license provided by the owner
of the applicable component.

```

### File: LICENSE-OPENSOURCE.md
```md
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.

                            Preamble

The GNU Affero General Public License is a free, copyleft license for
software and other kinds of works, specifically designed to ensure
cooperation with the community in the case of network server software.

The licenses for most software and other practical works are designed
to take away your freedom to share and change the works. By contrast,
our General Public Licenses are intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.

When we speak of free software, we are referring to freedom, not
price. Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

Developers that use our General Public Licenses protect your rights
with two steps: (1) assert copyright on the software, and (2) offer
you this License which gives you legal permission to copy, distribute
and/or modify the software.

A secondary benefit of defending all users' freedom is that
improvements made in alternate versions of the program, if they
receive widespread use, become available for other developers to
incorporate. Many developers of free software are heartened and
encouraged by the resulting cooperation. However, in the case of
software used on network servers, this result may fail to come about.
The GNU General Public License permits making a modified version and
letting the public access it on a server without ever releasing its
source code to the public.

The GNU Affero General Public License is designed specifically to
ensure that, in such cases, the modified source code becomes available
to the community. It requires the operator of a network server to
provide the source code of the modified version running there to the
users of that server. Therefore, public use of a modified version, on
a publicly accessible server, gives the public access to the source
code of the modified version.

An older license, called the Affero General Public License and
published by Affero, was designed to accomplish similar goals. This is
a different license, not a version of the Affero GPL, but Affero has
released a new version of the Affero GPL which permits relicensing under
this license.

The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

0. Definitions.

"This License" refers to version 3 of the GNU Affero General Public License.

"Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

"The Program" refers to any copyrightable work licensed under this
License. Each licensee is addressed as "you". "Licensees" and
"recipients" may be individuals or organizations.

To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy. The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

A "covered work" means either the unmodified Program or a work based
on the Program.

To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy. Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

To "convey" a work means any kind of propagation that enables other
parties to make or receive copies. Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License. If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

1. Source Code.

The "source code" for a work means the preferred form of the work
for making modifications to it. "Object code" means any non-source
form of a work.

A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form. A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities. However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work. For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

The Corresponding Source for a work in source code form is that
same work.

2. Basic Permissions.

All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met. This License explicitly affirms your unlimited
permission to run the unmodified Program. The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work. This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force. You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright. Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

Conveying under any other circumstances is permitted solely under
the conditions stated below. Sublicensing is not allowed; section 10
makes it unnecessary.

3. Protecting Users' Legal Rights From Anti-Circumvention Law.

No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

4. Conveying Verbatim Copies.

You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

5. Conveying Modified Source Versions.

You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit. Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

6. Conveying Non-Source Forms.

You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling. In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage. For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product. A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unle
... [TRUNCATED]
```

### File: pnpm-workspace.yaml
```yaml
packages:
  - 'apps/*'
  - 'packages/*'

```

### File: turbo.json
```json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["$TURBO_DEFAULT$", ".env*"],
      "outputs": ["dist/**", ".next/**", "!.next/cache/**"]
    },
    "lint": {
      "dependsOn": ["^lint"]
    },
    "check-types": {
      "dependsOn": ["^check-types"]
    },
    "test": {},
    "test:watch": {
      "cache": false,
      "persistent": true
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}

```

### File: .changeset\config.json
```json
{
  "$schema": "https://unpkg.com/@changesets/config@3.0.5/schema.json",
  "changelog": "@changesets/cli/changelog",
  "commit": false,
  "fixed": [],
  "linked": [],
  "access": "restricted",
  "baseBranch": "main",
  "updateInternalDependencies": "patch",
  "ignore": []
}

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
<!--
Thank you for sending the PR! We appreciate you spending the time to work on these changes.

Help us understand your motivation by explaining why you decided to make this change.

You can learn more about contributing to EventCatalog here: https://www.eventcatalog.dev/docs/contributing/overview

Happy contributing!

-->

## Motivation

(Write your motivation here.)

```

### File: shared\check-for-package-update.ts
```ts
import boxen from 'boxen';
import fs from 'fs';
import path from 'path';

const getInstalledVersionOfPackage = (packageName: string) => {
  try {
    const PROJECT_DIR = process.env.PROJECT_DIR || process.cwd();
    const pkg = fs.readFileSync(path.join(PROJECT_DIR, 'package.json'), 'utf8');
    const json = JSON.parse(pkg);
    const version = json.dependencies[packageName];
    // Clean up the version string by removing ^, ~ and other special characters
    return version?.replace(/[\^~><=]/g, '');
  } catch (error) {
    return null;
  }
};

export async function checkForPackageUpdate(packageName: string) {
  const installedVersion = getInstalledVersionOfPackage(packageName);

  if (!installedVersion || installedVersion === 'latest') return;

  try {
    const pkg = { name: packageName, version: installedVersion };
    const updateNotifierModule = await import('update-notifier');
    const notifier = updateNotifierModule.default({ pkg, updateCheckInterval: 0, shouldNotifyInNpmScript: true });

    const info = await notifier.fetchInfo();

    if (info?.type !== 'latest') {
      const message = `Package ${packageName} update available ${info.current} → ${info.latest}
Run npm i ${packageName} to update`;

      console.log(
        boxen(message, {
          padding: 1,
          margin: 1,
          align: 'center',
          borderColor: 'yellow',
          borderStyle: {
            topLeft: ' ',
            topRight: ' ',
            bottomLeft: ' ',
            bottomRight: ' ',
            right: ' ',
            top: '-',
            bottom: '-',
            left: ' ',
          },
        })
      );
    }
  } catch (error) {
    // Silently ignore update check failures (common in bundled environments)
    // This prevents the ERR_INVALID_ARG_TYPE error when update-notifier's
    // dependencies can't properly resolve file paths in bundled code
  }
}

```

### File: shared\checkLicense.ts
```ts
import chalk from 'chalk';
import { isFeatureEnabled, hasOfflineLicenseKey } from '@eventcatalog/license';

export default async (pkgName: string, licenseKey?: string) => {
  if (!hasOfflineLicenseKey() && !licenseKey) {
    console.log(chalk.bgRed(`\nNo license key provided for ${pkgName}`));
    console.log(chalk.redBright('You can get a free 14 day trial license at https://eventcatalog.cloud/'));
    process.exit(1);
  }

  try {
    const featureEnabled = await isFeatureEnabled(pkgName, licenseKey);
    if (!featureEnabled) {
      console.log(chalk.bgRed(`\nInvalid license key`));
      console.log(chalk.redBright('Please check your plugin license key or purchase a license at https://eventcatalog.cloud/'));
      process.exit(1);
    }
    return Promise.resolve();
  } catch (error) {
    console.log(error);
    console.log(chalk.bgRed(`\nFailed to verify license key`));
    console.log(chalk.redBright('Please check your plugin license key or purchase a license at https://eventcatalog.cloud/'));
    process.exit(1);
  }
};

```

