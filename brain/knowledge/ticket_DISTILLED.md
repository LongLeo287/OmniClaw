---
id: ticket
type: knowledge
owner: OA_Triage
---
# ticket
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "ticket-bot",
  "version": "3.3.1",
  "description": "Bot with a ticket system using Discord.js v14",
  "main": "dist/index.js",
  "scripts": {
    "setup": "npm install && prisma db push",
    "build": "rimraf dist && tsc",
    "start": "node dist/index.js",
    "format:fix": "prettier --write .",
    "format:check": "prettier --check .",
    "lint:fix": "eslint --fix . --ext .ts",
    "lint:check": "eslint . --ext .ts"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/Sayrix/ticket-bot.git"
  },
  "keywords": [
    "discord",
    "ticket",
    "bot"
  ],
  "author": "Sayrix",
  "license": "Apache-2.0",
  "bugs": {
    "url": "https://github.com/Sayrix/ticket-bot/issues"
  },
  "homepage": "https://github.com/Sayrix/ticket-bot#readme",
  "dependencies": {
    "@prisma/client": "^5.4.2",
    "axios": "^1.5.1",
    "better-sqlite3": "^9.0.0",
    "discord.js": "^14.13.0",
    "dotenv": "^16.3.1",
    "fs-extra": "^11.1.1",
    "jsonc": "^2.0.0",
    "mongoose": "^8.0.3",
    "readline": "^1.3.0",
    "ticket-bot-transcript-uploader": "^1.4.2-hotfix",
    "websocket": "^1.0.34"
  },
  "devDependencies": {
    "@types/better-sqlite3": "^7.6.5",
    "@types/fs-extra": "^11.0.3",
    "@types/node": "^22.7.5",
    "@types/pg": "^8.10.7",
    "@types/websocket": "^1.0.8",
    "@typescript-eslint/eslint-plugin": "^8.8.1",
    "@typescript-eslint/parser": "^8.8.1",
    "eslint": "^8.51.0",
    "eslint-config-airbnb-base": "^15.0.0",
    "eslint-config-prettier": "^9.0.0",
    "eslint-plugin-import": "^2.28.1",
    "eslint-plugin-node": "^11.1.0",
    "eslint-plugin-prettier": "^5.0.0",
    "prettier": "^3.0.3",
    "prettier-eslint": "^16.3.0",
    "prisma": "^5.4.1",
    "rimraf": "^6.0.1",
    "typescript": "^5.4.5"
  }
}

```

### File: README.md
```md
# Ticket Bot

Ticket Bot is a open source project of an ticket discord bot using [discord.js](https://discord.js.org) v14

![Discord.js ticket bot](https://i.imgur.com/564YXvR.png)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSayrix%2FTicket-Bot.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FSayrix%2FTicket-Bot?ref=badge_shield)

## 📄 Documentation

The documentation is available [here](https://doc.ticket.pm/)

## ⚠️ Incompatibility
This new source code you're seeing are completely refactored and will be incompatible with the older version.
I recommend you finish up all of your remaining support ticket and start migrating to the newer version.
If you prefer to stay in the older version, here is the doc for the old version: https://doc.ticket.pm/docs/oldDoc/intro

## 💬 Discord

You can come on the discord: https://discord.gg/VasYV6MEJy

## ✨ Contributing

Contributions are welcome! Please read the [contributing guidelines](https://github.com/Sayrix/Ticket-Bot/blob/main/CONTRIBUTING.md) first.

## 👨‍💻 Maintainers
Our current project maintainers:
* [Sayrix](https://github.com/Sayrix)
* [小兽兽/zhiyan114](https://github.com/zhiyan114)

## 💎 Sponsors
Thanks to all our sponsors! 🙏  
You can see all perks here: https://github.com/sponsors/Sayrix
<p align="center">
  <a href="https://cdn.jsdelivr.net/gh/sayrix/sponsors/sponsors.svg">
    <img src='https://raw.githubusercontent.com/Sayrix/sponsors/main/sponsors.svg'/>
  </a>
</p>

## 🎥 Videos  
[Tutorial in french + english subtitle](https://youtu.be/24zAFj8w9gE?si=OvikXeNIJglz4FJV)

## Please leave a ⭐ to help the project!


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSayrix%2FTicket-Bot.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FSayrix%2FTicket-Bot?ref=badge_large)

```

### File: .eslintrc.json
```json
{
	"env": {
		"es2021": true,
        "node": true
	},
	"overrides": [],
	"extends": ["eslint:recommended", "prettier", "plugin:@typescript-eslint/recommended"],
	"parser": "@typescript-eslint/parser",
	"parserOptions": {
        "ecmaVersion": "latest",
        "sourceType": "module"
    },
	"plugins": ["@typescript-eslint"],
	"rules": {
		"no-unused-vars": "warn",
		"no-console": "off",
		"@typescript-eslint/no-require-imports": "off",
		"no-undef": "warn",
		"no-constant-condition": "warn",
		"indent": ["error", "tab"],
		"semi": ["error", "always"],
		"quotes": [2, "double"],
		"semi-style": ["error", "last"],
		"no-process-exit": "off",
		"node/no-missing-import": "off",
		"no-var-requires": "off"
	}
}

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
s4yrix+github@gmail.com.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: CONTRIBUTING.md
```md
# Contributing to Ticket Bot
We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## We Develop with Github
We use github to host code, to track issues and feature requests, as well as accept pull requests.

## We Use [Github Flow](https://docs.github.com/en/get-started/quickstart/github-flow), So All Code Changes Happen Through Pull Requests
Pull requests are the best way to propose changes to the codebase (we use [Github Flow](https://docs.github.com/en/get-started/quickstart/github-flow)). We actively welcome your pull requests:

1. Fork the repo and create your branch from `master`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Any contributions you make will be under the Apache License 2.0
In short, when you submit code changes, your submissions are understood to be under the same [Apache License 2.0](http://choosealicense.com/licenses/apache-2.0/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Report bugs using Github's [issues](https://github.com/Sayrix/Ticket-Bot/issues)
We use GitHub issues to track public bugs. Report a bug by [opening a new issue](); it's that easy!

## Write bug reports with detail, background, and sample code

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can.
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

People *love* thorough bug reports. I'm not even kidding.

## License
By contributing, you agree that your contributions will be licensed under its Apache 2.0 License.

Thanks to Briandk for writing the [original document](https://gist.github.com/briandk/3d2e8b3ec8daf5a27a62)
```

### File: docker_run.sh
```sh
#!/bin/bash

# Setup the config files
if [ ! -f "./config/config.json" ]; then
    if [ -f "./temp_config/config.jsonc" ]; then
        # Config already setup by the user
        echo "Pre-build config detected, moving to config folder...";
        mv ./temp_config/config.jsonc ./config/config.jsonc
    else
        # Config not setup by the user
        echo "Config not detected, creating config...";
        echo "Make sure to edit the config file in /opt/ticket-bot/config/config.jsonc before starting the bot again.";
        mv ./temp_config/config.example.jsonc ./config/config.jsonc
        exit 1;
    fi
fi

npx prisma db push --schema=./prisma/docker.prisma
npm run start
```

### File: LICENSE.md
```md
# Creative Commons Attribution 4.0 International

Creative Commons Corporation (“Creative Commons”) is not a law firm and does not provide legal services or legal advice. Distribution of Creative Commons public licenses does not create a lawyer-client or other relationship. Creative Commons makes its licenses and related information available on an “as-is” basis. Creative Commons gives no warranties regarding its licenses, any material licensed under their terms and conditions, or any related information. Creative Commons disclaims all liability for damages resulting from their use to the fullest extent possible.

**Using Creative Commons Public Licenses**

Creative Commons public licenses provide a standard set of terms and conditions that creators and other rights holders may use to share original works of authorship and other material subject to copyright and certain other rights specified in the public license below. The following considerations are for informational purposes only, are not exhaustive, and do not form part of our licenses.

* __Considerations for licensors:__ Our public licenses are intended for use by those authorized to give the public permission to use material in ways otherwise restricted by copyright and certain other rights. Our licenses are irrevocable. Licensors should read and understand the terms and conditions of the license they choose before applying it. Licensors should also secure all rights necessary before applying our licenses so that the public can reuse the material as expected. Licensors should clearly mark any material not subject to the license. This includes other CC-licensed material, or material used under an exception or limitation to copyright. [More considerations for licensors](http://wiki.creativecommons.org/Considerations_for_licensors_and_licensees#Considerations_for_licensors).

* __Considerations for the public:__ By using one of our public licenses, a licensor grants the public permission to use the licensed material under specified terms and conditions. If the licensor’s permission is not necessary for any reason–for example, because of any applicable exception or limitation to copyright–then that use is not regulated by the license. Our licenses grant only permissions under copyright and certain other rights that a licensor has authority to grant. Use of the licensed material may still be restricted for other reasons, including because others have copyright or other rights in the material. A licensor may make special requests, such as asking that all changes be marked or described. Although not required by our licenses, you are encouraged to respect those requests where reasonable. [More considerations for the public](http://wiki.creativecommons.org/Considerations_for_licensors_and_licensees#Considerations_for_licensees).

## Creative Commons Attribution 4.0 International Public License

By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.

### Section 1 – Definitions.

a. __Adapted Material__ means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.

b. __Adapter's License__ means the license You apply to Your Copyright and Similar Rights in Your contributions to Adapted Material in accordance with the terms and conditions of this Public License.

c. __Copyright and Similar Rights__ means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section 2(b)(1)-(2) are not Copyright and Similar Rights.

d. __Effective Technological Measures__ means those measures that, in the absence of proper authority, may not be circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar international agreements.

e. __Exceptions and Limitations__ means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.

f. __Licensed Material__ means the artistic or literary work, database, or other material to which the Licensor applied this Public License.

g. __Licensed Rights__ means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.

h. __Licensor__ means the individual(s) or entity(ies) granting rights under this Public License.

i. __Share__ means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.

j. __Sui Generis Database Rights__ means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.

k. __You__ means the individual or entity exercising the Licensed Rights under this Public License. __Your__ has a corresponding meaning.

### Section 2 – Scope.

a. ___License grant.___

   1. Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:

       A. reproduce and Share the Licensed Material, in whole or in part; and

       B. produce, reproduce, and Share Adapted Material.

   2. __Exceptions and Limitations.__ For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.

   3. __Term.__ The term of this Public License is specified in Section 6(a).

   4. __Media and formats; technical modifications allowed.__ The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section 2(a)(4) never produces Adapted Material.

   5. __Downstream recipients.__

       A. __Offer from the Licensor – Licensed Material.__ Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.

       B. __No downstream restrictions.__ You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.

   6. __No endorsement.__ Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section 3(a)(1)(A)(i).

b. ___Other rights.___

   1. Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.

   2. Patent and trademark rights are not licensed under this Public License.

   3. To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties.

### Section 3 – License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the following conditions.

a. ___Attribution.___

   1. If You Share the Licensed Material (including in modified form), You must:

       A. retain the following if it is supplied by the Licensor with the Licensed Material:

         i. identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);

         ii. a copyright notice;

         iii. a notice that refers to this Public License;

         iv. a notice that refers to the disclaimer of warranties;

         v. a URI or hyperlink to the Licensed Material to the extent reasonably practicable;

       B. indicate if You modified the Licensed Material and retain an indication of any previous modifications; and

       C. indicate the Licensed Material is licensed under this Public License, and include the text of, or the URI or hyperlink to, this Public License.

   2. You may satisfy the conditions in Section 3(a)(1) in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.

   3. If requested by the Licensor, You must remove any of the information required by Section 3(a)(1)(A) to the extent reasonably practicable.

   4. If You Share Adapted Material You produce, the Adapter's License You apply must not prevent recipients of the Adapted Material from complying with this Public License.

### Section 4 – Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:

a. for the avoidance of doubt, Section 2(a)(1) grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database;

b. if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and

c. You must comply with the conditions in Section 3(a) if You Share all or a substantial portion of the contents of the database.

For the avoidance of doubt, this Section 4 supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.

### Section 5 – Disclaimer of Warranties and Limitation of Liability.

a. __Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.__

b. __To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.__

c. The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.

### Section 6 – Term and Termination.

a. This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.

b. Where Your right to use the Licensed Material has terminated under Section 6(a), it reinstates:

   1. automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or

   2. upon express reinstatement by the Licensor.

   For the avoidance of doubt, this Section 6(b) does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.

c. For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.

d. Sections 1, 5, 6, 7, and 8 survive termination of this Public License.

### Section 7 – Other Terms and Conditions.

a. The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.

b. Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and condit
... [TRUNCATED]
```

### File: tsconfig.json
```json
{
    "compilerOptions": {
        "outDir": "./dist",
        "rootDir": "./src/",
        "allowJs": true,
        "module": "CommonJS",
        "target": "ESNext",
        "strict": true,
        "moduleResolution": "node",
        "resolveJsonModule": true,
        "esModuleInterop": true,
        "skipLibCheck": false,
        "sourceMap": true,
        "inlineSources": true,
        "sourceRoot": "/"
    },
    "include": [
        "./src/**/*",
    ]
}
```

### File: locales\cs.json
```json
{
	"embeds": {
		"openTicket": {
			"title": "Otevřít ticket",
			"description": "Kliknutím na tlačítko otevřete ticket",
			"footer": {
				"text": "ticket.pm"
			}
		},
		"ticketOpened": {
			"title": "Ticket CATEGORYNAME",
			"description": "Náš tým vám brzy odpoví!",
			"footer": {
				"text": "ticket.pm"
			}
		},
		"ticketClosed": {
			"title": "Ticket byl uzavřen",
			"description": "Ticket uzavřel CLOSERNAME z důvodu: `REASON`"
		},
		"ticketClosedDM": {
			"title": "Ticket byl uzavřen",
			"description": "Ticket n°TICKETCOUNT byl uzavřen. Uzavřel ho CLOSERNAME z důvodu: `REASON`\n\nZde máš přepis ticketu: TRANSCRIPTURL",
			"footer": {
				"text": "ticket.pm"
			}
		}
	},
	"modals": {
		"reasonTicketOpen": {
			"title": "Otevřít ticket",
			"label": "Zadej důvod k otevření ticketu",
			"placeholder": "Prosím zadej důvod k otevření ticketu"
		},
		"reasonTicketClose": {
			"title": "Zavřít ticket",
			"label": "Zadej důvod k zavření ticketu",
			"placeholder": "Prosím zadej důvod k zavření ticketu"
		}
	},
	"buttons": {
		"close": {
			"label": "Zavřít ticket",
			"emoji": "🔒"
		},
		"claim": {
			"label": "Vzít",
			"emoji": "🙋"
		}
	},
	"invalidConfig": "Byla zjištěna neplatná konfigurace. Požádejte operátora bota, aby problém vyřešil!",
	"ticketOpenedMessage": "Ticket byl otevřen! TICKETCHANNEL",
	"ticketOnlyClaimableByStaff": "Pouze admin půže vzít ticket",
	"ticketAlreadyClaimed": "Ticket už je sebrán jiným adminem!",
	"ticketClaimedMessage": "> Ticket vzal USER",
	"ticketOnlyClosableByStaff": "Pouze admin může zavřít ticket!",
	"ticketAlreadyClosed": "Ticket už je uzavřen!",
	"ticketCreatingTranscript": "> Vytvářím přepis...",
	"ticketTranscriptCreated": "> Přepis byl vytvořen! TRANSCRIPTURL",
	"ticketLimitReached": "Můžeš mít pouze TICKETLIMIT otevřených ticketu!",

	"other": {
		"openTicketButtonMSG": "Otevřít ticket",
		"deleteTicketButtonMSG": "Smazat ticket",
		"selectTicketTypePlaceholder": "Vyber typ ticketu",
		"claimedBy": "**Tento ticket vzal**: USER",
		"noReasonGiven": "Důvod nebyl udán!",
		"unavailable": "Nedostupné"
	}
}

```

### File: locales\de.json
```json
{
	"embeds": {
		"openTicket": {
			"title": "Öffne ein Ticket",
			"description": "Klicke auf den Button, um ein Ticket zu öffnen",
			"footer": {
				"text": "ticket.pm"
			}
		},
		"ticketOpened": {
			"title": "Ticket CATEGORYNAME",
			"description": "Ein Teammitglied wird sich in Kürze um dich kümmern!",
			"footer": {
				"text": "ticket.pm"
			}
		},
		"ticketClosed": {
			"title": "Ticket geschlossen",
			"description": "Das Ticket wurde von CLOSERNAME mit folgendem Grund geschlossen: `REASON`"
		},
		"ticketClosedDM": {
			"title": "Ticket geschlossen",
			"description": "Das Ticket n°TICKETCOUNT wurde von CLOSERNAME mit folgendem Grund geschlossen: `REASON`\n\nHier findest du das Transkript: TRANSCRIPTURL",
			"footer": {
				"text": "ticket.pm"
			}
		}
	},
	"modals": {
		"reasonTicketOpen": {
			"title": "Ticket öffnen",
			"label": "Grund des Tickets",
			"placeholder": "Bitte gib einen Grund für das Öffnen des Tickets an."
		},
		"reasonTicketClose": {
			"title": "Ticket schließen",
			"label": "Grund der Schließung",
			"placeholder": "Bitte gib einen Grund für die Schließung des Tickets an."
		}
	},
	"buttons": {
		"close": {
			"label": "Ticket schließen",
			"emoji": "🔒"
		},
		"claim": {
			"label": "Beanspruchen",
			"emoji": "🙋"
		}
	},
	"invalidConfig": "Ungültige Konfiguration erkannt. Bitten Sie den Bot-Betreiber, das Problem zu beheben!",
	"ticketOpenedMessage": "Ticket geöffnet! TICKETCHANNEL",
	"ticketOnlyClaimableByStaff": "Das Ticket kann nur von Teammitgliedern beansprucht werden!",
	"ticketAlreadyClaimed": "Dieses Ticket wurde schon beansprucht!",
	"ticketClaimedMessage": "> Ticket von USER beansprucht",
	"ticketOnlyClosableByStaff": "Das Ticket kann nur von Teammitgliedern geschlossen werden!",
	"ticketAlreadyClosed": "Dieses Ticket wurde schon geschlossen!",
	"ticketCreatingTranscript": "> Generiere Transkript...",
	"ticketTranscriptCreated": "> Transkript generiert! TRANSCRIPTURL",
	"ticketOnlyRenamableByStaff": "Nur Teammitglieder können den Namen des tickets ändern!",
	"ticketRenamed": "> Ticketname geändert zu NEWNAME",
	"ticketLimitReached": "Du kannst nur TICKETLIMIT Tickets gleichzeitig offen haben",
	"noTickets": "Sie haben keinen Zugriff auf Tickets",

	"other": {
		"openTicketButtonMSG": "Öffne ein Ticket",
		"deleteTicketButtonMSG": "Ticket löschen",
		"selectTicketTypePlaceholder": "Wähle einen Typ",
		"claimedBy": "**Beansprucht von**: USER",
		"noReasonGiven": "Kein Grund angegeben",
		"unavailable": "Unavailable"
	}
}

```

### File: locales\el.json
```json
{
	"embeds": {
		"openTicket": {
			"title": "Ανοίξτε ένα ticket",
			"description": "Κάντε κλικ στο κουμπί για να ξεκινήσετε το άνοιγμα ενός ticket",
			"footer": {
				"text": "ticket.pm"
			}
		},
		"ticketOpened": {
			"title": "Ticket CATEGORYNAME",
			"description": "Ένα προσωπικό θα σας απαντήσει το συντομότερο δυνατό!",
			"footer": {
				"text": "ticket.pm"
			}
		},
		"ticketClosed": {
			"title": "Ticket έκλεισε",
			"description": "Το ticket έκλεισε από τον CLOSERNAME με τον εξής λόγο: `REASON`."
		},
		"ticketClosedDM": {
			"title": "Ticket έκλεισε",
			"description": "Το ticket n°TICKETCOUNT έκλεισε από τον CLOSERNAME με τον εξής λόγο: `REASON`\n\nΑκολουθεί η μεταγραφή του ticket: TRANSCRIPTURL",
			"footer": {
				"text": "ticket.pm"
			}
		}
	},
	"modals": {
		"reasonTicketOpen": {
			"title": "Ανοίξτε ένα ticket",
			"label": "Ο λόγος του ticket σας",
			"placeholder": "Εισαγάγετε τον λόγο για τον οποίο ανοίγετε ένα ticket"
		},
		"reasonTicketClose": {
			"title": "Κλείσιμο ticket",
			"label": "Ο λόγος που έκλεισε το ticket",
			"placeholder": "Εισαγάγετε τον λόγο για τον οποίο κλείνετε το ticket"
		}
	},
	"buttons": {
		"close": {
			"label": "Κλείσιμο ticket",
			"emoji": "🔒"
		},
		"claim": {
			"label": "Διεκδίκηση",
			"emoji": "🙋"
		}
	},
	"invalidConfig": "Εντοπίστηκε μη έγκυρη διαμόρφωση, ζητήστε από τον χειριστή του bot να τη διορθώσει!",
	"ticketOpenedMessage": "Το ticket άνοιξε! TICKETCHANNEL",
	"ticketOnlyClaimableByStaff": "Το ticket μπορεί να διεκδικηθεί μόνο από προσωπικό!",
	"ticketAlreadyClaimed": "Το ticket έχει ήδη διεκδικηθεί!",
	"ticketClaimedMessage": "> Διεκδίκηση ticket από USER",
	"ticketOnlyClosableByStaff": "Μόνο το προσωπικό μπορεί να κλείσει το ticket!",
	"ticketAlreadyClosed": "Το ticket είναι ήδη κλειστό!",
	"ticketCreatingTranscript": "> Δημιουργία μεταγραφής...",
	"ticketTranscriptCreated": "> Δημιουργήθηκε η μεταγραφή! TRANSCRIPTURL",
	"ticketOnlyRenamableByStaff": "Μόνο το προσωπικό μπορεί να μετονομάσει τα ticket!",
	"ticketRenamed": "> Το ticket μετονομάστηκε σε NEWNAME",
	"ticketLimitReached": "Μπορείτε να ανοίξετε μόνο TICKETLIMIT tickets ταυτόχρονα!",
	"noTickets": "Δεν έχετε πρόσβαση σε κανένα ticket",

	"other": {
		"openTicketButtonMSG": "Ανοίξτε ένα ticket",
		"deleteTicketButtonMSG": "Διαγραφή ticket",
		"selectTicketTypePlaceholder": "Επιλέξτε έναν τύπο ticket",
		"claimedBy": "**Διεκδικημένο από**: USER",
		"noReasonGiven": "Δεν δόθηκε λόγος",
		"unavailable": "Μη διαθέσιμο"
	}
}

```

### File: locales\es.json
```json
{
	"embeds": {
		"openTicket": {
			"title": "Abrir un ticket",
			"description": "Presiona el botón de abajo para abrir un ticket",
			"footer": {
				"text": "ticket.pm"
			}
		},
		"ticketOpened": {
			"title": "Ticket CATEGORYNAME",
			"description": "Un miembro del equipo te responderá dentro de un momento",
			"footer": {
				"text": "ticket.pm"
			}
		},
		"ticketClosed": {
			"title": "Ticket cerrado",
			"description": "El ticket fue cerrado por CLOSERNAME con la razón: `REASON`"
		},
		"ticketClosedDM": {
			"title": "Ticket cerrado",
			"description": "El ticket n°TICKETCOUNT se cerró por CLOSERNAME con la siguiente razón: `REASON`\n\nAquí tienes la traducción: TRANSCRIPTURL",
			"footer": {
				"text": "ticket.pm"
			}
		}
	},
	"modals": {
		"reasonTicketOpen": {
			"title": "Abrir ticket",
			"label": "Razón por que abres",
			"placeholder": "Ingresa la razón"
		},
		"reasonTicketClose": {
			"title": "Cerrar ticket",
			"label": "Razón del cierre",
			"placeholder": "Ingresa la razón"
		}
	},
	"buttons": {
		"close": {
			"label": "Cerrar ticket",
			"emoji": "🔒"
		},
		"claim": {
			"label": "Reclamar",
			"emoji": "🙋"
		}
	},
	"invalidConfig": "Se detectó una configuración no válida, ¡pídale al operador del bot que la arregle!",
	"ticketOpenedMessage": "¡Ticket abierto! --> TICKETCHANNEL",
	"ticketOnlyClaimableByStaff": "¡El ticket solo puede ser reclamado por un miembro del equipo!",
	"ticketAlreadyClaimed": "¡Ya se reclamó el ticket!",
	"ticketClaimedMessage": "> Ticket reclamado por USER",
	"ticketOnlyClosableByStaff": "¡El ticket solo puede ser cerrado por un miembro del equipo!",
	"ticketAlreadyClosed": "¡El ticket ya estaba cerrado!",
	"ticketCreatingTranscript": "> Transcribiendo...",
	"ticketTranscriptCreated": "> ¡Ticket transcripto! TRANSCRIPTURL",
	"ticketLimitReached": "Solo puedes tener TICKETLIMIT tickets abiertos al mismo tiempo!",

	"other": {
		"openTicketButtonMSG": "Abrir un ticket",
		"deleteTicketButtonMSG": "Eliminar ticket",
		"selectTicketTypePlaceholder": "Elegir el tipo de ticket",
		"claimedBy": "**Reclamado por**: USER",
		"noReasonGiven": ":x: No se dio una razón",
		"unavailable": "Unavailable"
	}
}

```

### File: locales\fr.json
```json
{
	"embeds": {
		"openTicket": {
			"title": "Ouvrir un ticket",
			"description": "Cliquez sur le bouton ci-dessous pour ouvrir un ticket.",
			"footer": {
				"text": "ticket.pm"
			}
		},
		"ticketOpened": {
			"title": "Ticket CATEGORYNAME",
			"description": "Votre ticket a été ouvert. Un membre du staff va vous répondre dans les plus brefs délais.",
			"footer": {
				"text": "ticket.pm"
			}
		},
		"ticketClosed": {
			"title": "Ticket fermé",
			"description": "Le ticket a été fermé par CLOSERNAME avec comme raison: `REASON`"
		},
		"ticketClosedDM": {
			"title": "Ticket fermé",
			"description": "Le ticket n°TICKETCOUNT a été fermé par CLOSERNAME avec comme raison: `REASON`\n\nVoici une retranscription du ticket: TRANSCRIPTURL",
			"footer": {
				"text": "ticket.pm"
			}
		}
	},
	"modals": {
		"reasonTicketOpen": {
			"title": "Ouvrir un ticket",
			"label": "La raison de votre ticket",
			"placeholder": "Veuillez entrer la raison de l'ouverture de votre ticket."
		},
		"reasonTicketClose": {
			"title": "Fermer un ticket",
			"label": "La raison de la fermeture du ticket",
			"placeholder": "Veuillez entrer la raison de la fermeture de votre ticket."
		}
	},
	"buttons": {
		"close": {
			"label": "Fermer le ticket",
			"emoji": "🔒"
		},
		"claim": {
			"label": "Réclamer",
			"emoji": "🙋"
		}
	},
	"invalidConfig": "Configuration non valide détectée, veuillez demander à l'opérateur du bot de la corriger!",
	"ticketOpenedMessage": "Ticket ouvert! TICKETCHANNEL",
	"ticketOnlyClaimableByStaff": "Seuls les membres du staff peuvent réclamer un ticket !",
	"ticketAlreadyClaimed": "Le ticket est déjà reçu!",
	"ticketClaimedMessage": "> Ticket reçu par USER",
	"ticketOnlyClosableByStaff": "Seuls les membres du staff peuvent fermer le ticket !",
	"ticketAlreadyClosed": "Ticket déjà fermé !",
	"ticketCreatingTranscript": "> Retranscription...",
	"ticketTranscriptCreated": "> Retranscription créée ! TRANSCRIPTURL",
	"ticketRenamed": "> Ticket renommé en NEWNAME",
	"ticketLimitReached": "Vous ne pouvez seulement que TICKETLIMIT ticket(s) ouvert(s) !",

	"other": {
		"openTicketButtonMSG": "Ouvrir un ticket",
		"deleteTicketButtonMSG": "Supprimer un ticket",
		"selectTicketTypePlaceholder": "Sélectionnez le type de ticket",
		"claimedBy": "**Claim par**: USER",
		"noReasonGiven": "Aucune raison donnée",
		"unavailable": "Unavailable"
	}
}

```

### File: locales\id.json
```json
{
    "embeds": {
        "openTicket": {
            "title": "Buka tiket",
            "description": "Klik tombol untuk mulai membuka tiket",
            "footer": {
                "text": "ticket.pm"
            }
        },
        "ticketOpened": {
            "title": "Tiket CATEGORYNAME",
            "description": "Staff akan membalas Anda sesegera mungkin!",
            "footer": {
                "text": "ticket.pm"
            }
        },
        "ticketClosed": {
            "title": "Tiket ditutup",
            "description": "Tiket telah ditutup oleh CLOSERNAME dengan alasan berikut: `REASON`",
            "deleteTicketInfo": "> Tiket akan dihapus dalam 15 detik"
        },
        "ticketClosedDM": {
            "title": "Tiket ditutup",
            "description": "Tiket nomor TICKETCOUNT telah ditutup oleh CLOSERNAME dengan alasan berikut: `REASON`\n\nBerikut transkrip tiket: TRANSCRIPTURL",
            "footer": {
                "text": "ticket.pm"
            }
        }
    },
    "modals": {
        "reasonTicketOpen": {
            "title": "Buka tiket",
            "label": "Alasan Anda membuka tiket",
            "placeholder": "Silakan masukkan alasan mengapa Anda membuka tiket"
        },
        "reasonTicketClose": {
            "title": "Tutup tiket",
            "label": "Alasan penutupan tiket",
            "placeholder": "Silakan masukkan alasan mengapa Anda menutup tiket"
        }
    },
    "buttons": {
        "close": {
            "label": "Tutup tiket",
            "emoji": "🔒"
        },
        "claim": {
            "label": "Klaim",
            "emoji": "🙋"
        }
    },
    "invalidConfig": "Konfigurasi tidak valid terdeteksi, silakan minta operator bot untuk memperbaikinya!",
    "ticketOpenedMessage": "Tiket dibuka! TICKETCHANNEL",
    "ticketOnlyClaimableByStaff": "Tiket hanya dapat diklaim oleh staff!",
    "ticketAlreadyClaimed": "Tiket sudah diklaim!",
    "ticketClaimedMessage": "> Tiket diklaim oleh USER",
    "ticketOnlyClosableByStaff": "Hanya staff yang dapat menutup tiket!",
    "ticketAlreadyClosed": "Tiket sudah ditutup!",
    "ticketCreatingTranscript": "> Membuat transkrip...",
    "ticketTranscriptCreated": "> Transkrip dibuat! TRANSCRIPTURL",
    "ticketOnlyRenamableByStaff": "Hanya staff yang dapat mengubah nama tiket!",
    "ticketRenamed": "> Tiket diubah namanya menjadi NEWNAME",
    "ticketLimitReached": "Anda hanya dapat memiliki TICKETLIMIT tiket yang dibuka pada saat yang bersamaan!",
    "noTickets": "Anda tidak memiliki akses ke tiket apa pun",

    "other": {
        "openTicketButtonMSG": "Buka tiket",
        "deleteTicketButtonMSG": "Hapus tiket",
        "selectTicketTypePlaceholder": "Pilih jenis tiket",
        "claimedBy": "**Diklaim Oleh**: USER",
        "noReasonGiven": "Tidak ada alasan yang diberikan",
        "unavailable": "Tidak tersedia"
    }
}
```

### File: locales\it.json
```json
{
    "embeds": {
        "openTicket": {
            "title": "Apri un ticket",
            "description": "Clicca sul pulsante per iniziare ad aprire un ticket",
            "footer": {
                "text": "ticket.pm"
            }
        },
        "ticketOpened": {
            "title": "Ticket CATEGORYNAME",
            "description": "Un membro dello staff ti risponderà il prima possibile!",
            "footer": {
                "text": "ticket.pm"
            }
        },
        "ticketClosed": {
            "title": "Ticket chiuso",
            "description": "Il ticket è stato chiuso da CLOSERNAME con la seguente motivazione: `REASON`",
            "deleteTicketInfo": "> Il ticket verrà eliminato in 15 secondi"
        },
        "ticketClosedDM": {
            "title": "Ticket chiuso",
            "description": "Il ticket n°TICKETCOUNT è stato chiuso da CLOSERNAME con la seguente motivazione: `REASON`\n\nEcco la trascrizione del ticket: TRANSCRIPTURL",
            "footer": {
                "text": "ticket.pm"
            }
        }
    },
    "modals": {
        "reasonTicketOpen": {
            "title": "Apri ticket",
            "label": "La motivazione del tuo ticket",
            "placeholder": "Per favore inserisci la motivazione per cui stai aprendo un ticket"
        },
        "reasonTicketClose": {
            "title": "Chiudi ticket",
            "label": "La motivazione della chiusura del ticket",
            "placeholder": "Per favore inserisci la motivazione per cui stai chiudendo il ticket"
        }
    },
    "buttons": {
        "close": {
            "label": "Chiudi ticket",
            "emoji": "🔒"
        },
        "claim": {
            "label": "Richiedi",
            "emoji": "🙋"
        }
    },
    "invalidConfig": "Configurazione non valida rilevata, per favore chiedi all'operatore del bot di sistemarla!",
    "ticketOpenedMessage": "Ticket aperto! TICKETCHANNEL",
    "ticketOnlyClaimableByStaff": "Il ticket può essere richiesto solo dallo staff!",
    "ticketAlreadyClaimed": "Il ticket è già stato richiesto!",
    "ticketClaimedMessage": "> Ticket richiesto da USER",
    "ticketOnlyClosableByStaff": "Solo lo staff può chiudere il ticket!",
    "ticketAlreadyClosed": "Il ticket è già chiuso!",
    "ticketCreatingTranscript": "> Creazione trascrizione...",
    "ticketTranscriptCreated": "> Trascrizione creata! TRANSCRIPTURL",
    "ticketOnlyRenamableByStaff": "Solo lo staff può rinominare i ticket!",
    "ticketRenamed": "> Ticket rinominato in NEWNAME",
    "ticketLimitReached": "Puoi avere solo TICKETLIMIT ticket aperti contemporaneamente!",
    "noTickets": "Non hai accesso a nessun ticket",
    "other": {
        "openTicketButtonMSG": "Apri un ticket",
        "deleteTicketButtonMSG": "Elimina ticket",
        "selectTicketTypePlaceholder": "Seleziona un tipo di ticket",
        "claimedBy": "**Richiesto Da**: USER",
        "noReasonGiven": "Nessuna motivazione fornita",
        "unavailable": "Non disponibile"
    }
}
```

### File: locales\main.json
```json
{
	"embeds": {
		"openTicket": {
			"title": "Open a ticket",
			"description": "Click on the button to start opening a ticket",
			"footer": {
				"text": "ticket.pm"
			}
		},
		"ticketOpened": {
			"title": "Ticket CATEGORYNAME",
			"description": "A staff will reply you as soon as possible!",
			"footer": {
				"text": "ticket.pm"
			}
		},
		"ticketClosed": {
			"title": "Ticket closed",
			"description": "The ticket has been closed by CLOSERNAME with the following reason: `REASON`",
			"deleteTicketInfo": "> The ticket will be deleted in 15 seconds"
		},
		"ticketClosedDM": {
			"title": "Ticket closed",
			"description": "The ticket n°TICKETCOUNT has been closed by CLOSERNAME with the following reason: `REASON`\n\nHere is the transcript of the ticket: TRANSCRIPTURL",
			"footer": {
				"text": "ticket.pm"
			}
		}
	},
	"modals": {
		"reasonTicketOpen": {
			"title": "Open ticket",
			"label": "The reason of your ticket",
			"placeholder": "Please enter the reason of why you are opening a ticket"
		},
		"reasonTicketClose": {
			"title": "Close ticket",
			"label": "The reason of the ticket closure",
			"placeholder": "Please enter the reason of why you are closing the ticket"
		}
	},
	"buttons": {
		"close": {
			"label": "Close ticket",
			"emoji": "🔒"
		},
		"claim": {
			"label": "Claim",
			"emoji": "🙋"
		}
	},
	"invalidConfig": "Invalid configuration detected, please ask the bot operator to fix it!",
	"ticketOpenedMessage": "Ticket opened! TICKETCHANNEL",
	"ticketOnlyClaimableByStaff": "The ticket can only be claimed by a staff!",
	"ticketAlreadyClaimed": "The ticket is already claimed!",
	"ticketClaimedMessage": "> Ticket claimed by USER",
	"ticketOnlyClosableByStaff": "Only staff can close the ticket!",
	"ticketAlreadyClosed": "The ticket is already closed!",
	"ticketCreatingTranscript": "> Creating transcript...",
	"ticketTranscriptCreated": "> Transcript created! TRANSCRIPTURL",
	"ticketOnlyRenamableByStaff": "Only staff can rename tickets!",
	"ticketRenamed": "> Ticket renamed to NEWNAME",
	"ticketLimitReached": "You can only have TICKETLIMIT tickets opened at the same time!",
	"noTickets": "You don't have access to any tickets",

	"other": {
		"openTicketButtonMSG": "Open a ticket",
		"deleteTicketButtonMSG": "Delete ticket",
		"selectTicketTypePlaceholder": "Select a ticket type",
		"claimedBy": "**Claimed By**: USER",
		"noReasonGiven": "No reason given",
		"unavailable": "Unavailable"
	}
}

```

### File: locales\my.json
```json
{
    "embeds": {
        "openTicket": {
            "title": "Buka tiket",
            "description": "Klik butang untuk mula membuka tiket",
            "footer": {
                "text": "ticket.pm"
            }
        },
        "ticketOpened": {
            "title": "Tiket CATEGORYNAME",
            "description": "Staf akan membalas anda secepat mungkin!",
            "footer": {
                "text": "ticket.pm"
            }
        },
        "ticketClosed": {
            "title": "Tiket ditutup",
            "description": "Tiket telah ditutup oleh CLOSERNAME dengan alasan berikut: `REASON`",
            "deleteTicketInfo": "> Tiket akan dipadam dalam 15 saat"
        },
        "ticketClosedDM": {
            "title": "Tiket ditutup",
            "description": "Tiket bernombor TICKETCOUNT telah ditutup oleh CLOSERNAME dengan alasan berikut: `REASON`\n\nBerikut adalah transkrip tiket: TRANSCRIPTURL",
            "footer": {
                "text": "ticket.pm"
            }
        }
    },
    "modals": {
        "reasonTicketOpen": {
            "title": "Buka tiket",
            "label": "Alasan anda membuka tiket",
            "placeholder": "Sila masukkan alasan mengapa anda membuka tiket"
        },
        "reasonTicketClose": {
            "title": "Tutup tiket",
            "label": "Alasan penutupan tiket",
            "placeholder": "Sila masukkan alasan mengapa anda menutup tiket"
        }
    },
    "buttons": {
        "close": {
            "label": "Tutup tiket",
            "emoji": "🔒"
        },
        "claim": {
            "label": "Tuntut",
            "emoji": "🙋"
        }
    },
    "invalidConfig": "Pengesanan konfigurasi tidak sah, sila minta pengendali bot untuk membetulkannya!",
    "ticketOpenedMessage": "Tiket dibuka! TICKETCHANNEL",
    "ticketOnlyClaimableByStaff": "Tiket hanya boleh dituntut oleh staf!",
    "ticketAlreadyClaimed": "Tiket telah dituntut!",
    "ticketClaimedMessage": "> Tiket dituntut oleh USER",
    "ticketOnlyClosableByStaff": "Hanya staf boleh menutup tiket!",
    "ticketAlreadyClosed": "Tiket sudah ditutup!",
    "ticketCreatingTranscript": "> Mencipta transkrip...",
    "ticketTranscriptCreated": "> Transkrip dicipta! TRANSCRIPTURL",
    "ticketOnlyRenamableByStaff": "Hanya staf boleh menukar nama tiket!",
    "ticketRenamed": "> Tiket ditukar nama kepada NEWNAME",
    "ticketLimitReached": "Anda hanya boleh membuka TICKETLIMIT tiket pada satu masa!",
    "noTickets": "Anda tidak mempunyai akses kepada mana-mana tiket",

    "other": {
        "openTicketButtonMSG": "Buka tiket",
        "deleteTicketButtonMSG": "Padam tiket",
        "selectTicketTypePlaceholder": "Pilih jenis tiket",
        "claimedBy": "**Dituntut Oleh**: USER",
        "noReasonGiven": "Tiada alasan diberikan",
        "unavailable": "Tidak tersedia"
    }
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
