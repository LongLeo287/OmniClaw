---
id: awesome-notebooklm-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:55.620156
---

# KNOWLEDGE EXTRACT: awesome-notebooklm
> **Extracted on:** 2026-03-30 17:30:44
> **Source:** awesome-notebooklm

---

## File: `.gitattributes`
```
## GITATTRIBUTES FOR WEB PROJECTS
#
# These settings are for any web project.
#
# Details per file setting:
#   text    These files should be normalized (i.e. convert CRLF to LF).
#   binary  These files are binary and should be left untouched.
#
# Note that binary is a macro for -text -diff.
######################################################################

## AUTO-DETECT
##   Handle line endings automatically for files detected as
##   text and leave all files detected as binary untouched.
##   This will handle all files NOT defined below.
* text=auto

## SOURCE CODE
*.bat      text eol=crlf
*.coffee   text
*.css      text
*.htm      text
*.html     text
*.inc      text
*.ini      text
*.js       text
*.json     text
*.jsx      text
*.less     text
*.od       text
*.onlydata text
*.php      text
*.pl       text
*.py       text
*.rb       text
*.sass     text
*.scm      text
*.scss     text
*.sh       text eol=lf
*.sql      text
*.styl     text
*.tag      text
*.ts       text
*.tsx      text
*.xml      text
*.xhtml    text

## DOCKER
*.dockerignore    text
Dockerfile    text

## DOCUMENTATION
*.markdown   text
*.md         text
*.mdwn       text
*.mdown      text
*.mkd        text
*.mkdn       text
*.mdtxt      text
*.mdtext     text
*.txt        text
AUTHORS      text
CHANGELOG    text
CHANGES      text
CONTRIBUTING text
COPYING      text
copyright    text
*COPYRIGHT*  text
INSTALL      text
license      text
LICENSE      text
NEWS         text
readme       text
*README*     text
TODO         text

## TEMPLATES
*.dot        text
*.ejs        text
*.haml       text
*.handlebars text
*.hbs        text
*.hbt        text
*.jade       text
*.latte      text
*.mustache   text
*.njk        text
*.phtml      text
*.tmpl       text
*.tpl        text
*.twig       text

## LINTERS
.csslintrc    text
.eslintrc     text
.htmlhintrc   text
.jscsrc       text
.jshintrc     text
.jshintignore text
.stylelintrc  text

## CONFIGS
*.bowerrc      text
*.cnf          text
*.conf         text
*.config       text
.browserslistrc    text
.editorconfig  text
.gitattributes text
.gitconfig     text
.htaccess      text
*.npmignore    text
*.yaml         text
*.yml          text
browserslist   text
Makefile       text
makefile       text

## HEROKU
Procfile    text
.slugignore text

## GRAPHICS
*.ai   binary
*.bmp  binary
*.eps  binary
*.gif  binary
*.ico  binary
*.jng  binary
*.jp2  binary
*.jpg  binary
*.jpeg binary
*.jpx  binary
*.jxr  binary
*.pdf  binary
*.png  binary
*.psb  binary
*.psd  binary
*.svg  text
*.svgz binary
*.tif  binary
*.tiff binary
*.wbmp binary
*.webp binary

## AUDIO
*.kar  binary
*.m4a  binary
*.mid  binary
*.midi binary
*.mp3  binary
*.ogg  binary
*.ra   binary

## VIDEO
*.3gpp binary
*.3gp  binary
*.as   binary
*.asf  binary
*.asx  binary
*.fla  binary
*.flv  binary
*.m4v  binary
*.mng  binary
*.mov  binary
*.mp4  binary
*.mpeg binary
*.mpg  binary
*.ogv  binary
*.swc  binary
*.swf  binary
*.webm binary

## ARCHIVES
*.7z  binary
*.gz  binary
*.jar binary
*.rar binary
*.tar binary
*.zip binary

## FONTS
*.ttf   binary
*.eot   binary
*.otf   binary
*.woff  binary
*.woff2 binary

## EXECUTABLES
*.exe binary
*.pyc binary
```

## File: `.tool-versions`
```
nodejs 21.6.0
```

## File: `code_of_conduct.md`
```markdown

# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, caste, color, religion, or sexual identity
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
[INSERT CONTACT METHOD].
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
[https://www.contributor-covenant.org/version/2/0/code_of_conduct.html][v2.0].

Community Impact Guidelines were inspired by 
[Mozilla's code of conduct enforcement ladder][Mozilla CoC].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][FAQ]. Translations are available 
at [https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.0]: https://www.contributor-covenant.org/version/2/0/code_of_conduct.html
[Mozilla CoC]: https://github.com/mozilla/diversity
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations

```

## File: `contributing.md`
```markdown
# Contribution Guidelines

Please note that this project is released with a [Contributor Code of Conduct](code_of_conduct.md). By participating in this project you agree to abide by its terms.

## PRs

ALWAYS create a new branch with your proposed changes. Thank you!

## Adding an new Item

- Try to fit your item into an existing sections. [Open a suggestion](https://github.com/etewiah/awesome-notebooklm/issues/new) to start as discussion about any new sections.
- Add a new item to the bottom of the list in a section.
- If a duplicate item exists, discuss why the new item should replace it.
- Check your spelling & grammar.
- The item must follow this format:
  ```
  - [item name](https link) - Description beginning with capital, ending in period.
  ```
```

## File: `license`
```
[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer exclusive Copyright and Related Rights (defined below) upon the creator and subsequent owner(s) (each and all, an "owner") of an original work of authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for the purpose of contributing to a commons of creative, cultural and scientific works ("Commons") that the public can reliably and without fear of later claims of infringement build upon, modify, incorporate in other works, reuse and redistribute as freely as possible in any form whatsoever and for any purposes, including without limitation commercial purposes. These owners may contribute to the Commons to promote the ideal of a free culture and the further production of creative, cultural and scientific works, or to gain reputation or greater distribution for their Work in part through the use and efforts of others.

For these and/or other purposes and motivations, and without any expectation of additional consideration or compensation, the person associating CC0 with a Work (the "Affirmer"), to the extent that he or she is an owner of Copyright and Related Rights in the Work, voluntarily elects to apply CC0 to the Work and publicly distribute the Work under its terms, with knowledge of his or her Copyright and Related Rights in the Work and the meaning and intended legal effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be protected by copyright and related or neighboring rights ("Copyright and Related Rights"). Copyright and Related Rights include, but are not limited to, the following:

    the right to reproduce, adapt, distribute, perform, display, communicate, and translate a Work;
    moral rights retained by the original author(s) and/or performer(s);
    publicity and privacy rights pertaining to a person's image or likeness depicted in a Work;
    rights protecting against unfair competition in regards to a Work, subject to the limitations in paragraph 4(a), below;
    rights protecting the extraction, dissemination, use and reuse of data in a Work;
    database rights (such as those arising under Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, and under any national implementation thereof, including any amended or successor version of such directive); and
    other similar, equivalent or corresponding rights throughout the world based on applicable law or treaty, and any national implementations thereof.

2. Waiver. To the greatest extent permitted by, but not in contravention of, applicable law, Affirmer hereby overtly, fully, permanently, irrevocably and unconditionally waives, abandons, and surrenders all of Affirmer's Copyright and Related Rights and associated claims and causes of action, whether now known or unknown (including existing as well as future claims and causes of action), in the Work (i) in all territories worldwide, (ii) for the maximum duration provided by applicable law or treaty (including future time extensions), (iii) in any current or future medium and for any number of copies, and (iv) for any purpose whatsoever, including without limitation commercial, advertising or promotional purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each member of the public at large and to the detriment of Affirmer's heirs and successors, fully intending that such Waiver shall not be subject to revocation, rescission, cancellation, termination, or any other legal or equitable action to disrupt the quiet enjoyment of the Work by the public as contemplated by Affirmer's express Statement of Purpose.

3. Public License Fallback. Should any part of the Waiver for any reason be judged legally invalid or ineffective under applicable law, then the Waiver shall be preserved to the maximum extent permitted taking into account Affirmer's express Statement of Purpose. In addition, to the extent the Waiver is so judged Affirmer hereby grants to each affected person a royalty-free, non transferable, non sublicensable, non exclusive, irrevocable and unconditional license to exercise Affirmer's Copyright and Related Rights in the Work (i) in all territories worldwide, (ii) for the maximum duration provided by applicable law or treaty (including future time extensions), (iii) in any current or future medium and for any number of copies, and (iv) for any purpose whatsoever, including without limitation commercial, advertising or promotional purposes (the "License"). The License shall be deemed effective as of the date CC0 was applied by Affirmer to the Work. Should any part of the License for any reason be judged legally invalid or ineffective under applicable law, such partial invalidity or ineffectiveness shall not invalidate the remainder of the License, and in such case Affirmer hereby affirms that he or she will not (i) exercise any of his or her remaining Copyright and Related Rights in the Work or (ii) assert any associated claims and causes of action with respect to the Work, in either case contrary to Affirmer's express Statement of Purpose.

4. Limitations and Disclaimers.

    No trademark or patent rights held by Affirmer are waived, abandoned, surrendered, licensed or otherwise affected by this document.
    Affirmer offers the Work as-is and makes no representations or warranties of any kind concerning the Work, express, implied, statutory or otherwise, including without limitation warranties of title, merchantability, fitness for a particular purpose, non infringement, or the absence of latent or other defects, accuracy, or the present or absence of errors, whether or not discoverable, all to the greatest extent permissible under applicable law.
    Affirmer disclaims responsibility for clearing rights of other persons that may apply to the Work or any use thereof, including without limitation any person's Copyright and Related Rights in the Work. Further, Affirmer disclaims responsibility for obtaining any necessary consents, permissions or other rights required for any use of the Work.
    Affirmer understands and acknowledges that Creative Commons is not a party to this document and has no duty or obligation with respect to this CC0 or use of the Work.
```

## File: `readme.md`
```markdown
<div align="center">

<!-- title -->

<!--lint ignore no-dead-urls-->

# Awesome NotebookLM [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![lint](https://github.com/etewiah/awesome-notebooklm/actions/workflows/lint.yaml/badge.svg)](https://github.com/etewiah/awesome-notebooklm/actions/workflows/lint.yaml)

<!-- subtitle -->

A curated list of tools related to notebooklm as well as examples of great podcasts generated by notebooklm

<!-- image -->

<!-- <a href="" target="_blank" rel="noopener noreferrer">
  <img src="" />
</a> -->

</div>

<!-- TOC -->

## Contents

- [Podcast creation alternatives](#podcast-creation-alternatives)
- [Example content](#example-content)
- [Community](#community)

<!-- CONTENT -->

## Podcast creation alternatives

- [Podcastfy](https://github.com/souzatharsis/podcastfy) - Transforming Multimodal Content into Captivating Multilingual Audio Conversations with GenAI.
- [Open Notebooklm](https://github.com/gabrielchua/open-notebooklm) - Convert any PDF into a podcast episode!
- [Zenmic](https://zenmic.com) - AI Podcast Generator.
- [Jellypod AI](https://jellypod.ai/) - Create on-brand, AI podcasts in minutes.

<!-- END CONTENT -->

## Example content

- [Gipety hacker news casts](https://news.gipety.com/) - Podcasts of selected hacker news threads.
- [Adding lipsync-ed talking heads to podcast audio](https://andresvarela.com/2024/09/how-i-used-notebooklm-for-an-elevator-pitch/) - Overview of the podcast technology with free/freemium tools to go further and generate avatars.
- [HCI Deep Dives](https://www.deep-hci.org/) - Podcasts of selected Human Computer Interaction Papers using NotebookML and podcastfy.

## Community

<!-- list people worth following on social sites (Twitter, LinkedIn, GitHub, YouTube etc.) -->

- [Reddit](https://www.reddit.com/r/notebooklm/)
- [Discord](https://discord.com/invite/Az2N7BwV7r?sjid=15620215024250848195-NC )
- [Twitter / X](https://x.com/notebooklm_pods)


## Contributing

[Contributions of any kind welcome, just follow the guidelines](contributing.md)!

### Contributors

[Thanks goes to these contributors](https://github.com/etewiah/awesome-notebooklm/graphs/contributors)!
```

## File: `ci/.gitlab-ci.yml`
```yaml
stages:
  - check

awesome-lint:
  stage: check
  image: node:lts
  cache:
    paths:
      - node_modules/
  script:
    - yarn add awesome-lint
    - yarn awesome-lint

awesome-bot:
  stage: check
  image: ruby:latest
  script:
    - gem install awesome_bot
    - awesome_bot readme.md --allow-redirect --allow-dupe
```

