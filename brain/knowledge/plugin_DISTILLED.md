---
id: plugin
type: knowledge
owner: OA_Triage
---
# plugin
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Deprecated
Please use https://github.com/CastagnaIT/plugin.video.netflix/

# Netflix Plugin for Kodi 18 (plugin.video.netflix)

[![Bitcoin donate button](https://img.shields.io/badge/bitcoin-donate-yellow.svg)](https://blockchain.info/address/1DHGftMkFXXsDY7UnqQuatWwxQzKVu88sF)
[![Build Status](https://travis-ci.org/asciidisco/plugin.video.netflix.svg?branch=master)](https://travis-ci.org/asciidisco/plugin.video.netflix)
[![Test Coverage](https://codeclimate.com/github/asciidisco/plugin.video.netflix/badges/coverage.svg)](https://codeclimate.com/github/asciidisco/plugin.video.netflix/coverage)
[![Issue Count](https://codeclimate.com/github/asciidisco/plugin.video.netflix/badges/issue_count.svg)](https://codeclimate.com/github/asciidisco/plugin.video.netflix)
[![Code Climate](https://codeclimate.com/github/asciidisco/plugin.video.netflix/badges/gpa.svg)](https://codeclimate.com/github/asciidisco/plugin.video.netflix)
[![GitHub release](https://img.shields.io/github/release/asciidisco/plugin.video.netflix.svg)](https://github.com/asciidisco/plugin.video.netflix/releases)
[![Docs](https://media.readthedocs.org/static/projects/badges/passing.svg)](https://asciidisco.github.io/plugin.video.netflix/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Disclaimer

This plugin is not officially commisioned/supported by Netflix.
The trademark "Netflix" is registered by "Netflix, Inc."

## Prerequisites

- Kodi 18 [nightlybuild](http://mirrors.kodi.tv/nightlies/)
- Inputstream.adaptive [>=v2.0.0](https://github.com/peak3d/inputstream.adaptive)
  (should be included in your Kodi 18 installation)
- Libwidevine >=1.4.8.970 (for non Android devices)
- Cryptdome python library (for Linux systems, install using `pip install --user pycryptodomex` as the user that will run Kodi)

Note: The link to download the Widevine Libary for none ARM Systems can be
found in the [Firefox Sources](https://hg.mozilla.org/mozilla-central/raw-file/31465a03c03d1eec31cd4dd5d6b803724dcb29cd/toolkit/content/gmp-sources/widevinecdm.json)
& needs to be placed in the `cdm` folder in [special://home](http://kodi.wiki/view/Special_protocol).

Please make sure to read the licence agreement that comes with it,
so you know what you´re getting yourself into.

## Installation & Updates

You can use
[our repository](https://github.com/kodinerds/repo/raw/master/repository.netflix/repository.netflix-1.0.1.zip)
to install plugin.
Using this, you´ll immediately receive updates once a
new release has been drafted.

Further installations instructions can be found in the [Wiki](https://github.com/asciidisco/plugin.video.netflix/wiki)

## FAQ

- [Does it work with Kodi 17](https://github.com/asciidisco/plugin.video.netflix/issues/25)
- [Does it work on a RPI](https://github.com/asciidisco/plugin.video.netflix/issues/28)
- [Which video resolutions are supported](https://github.com/asciidisco/plugin.video.netflix/issues/27)
- [Can it play 4k Videos](https://github.com/asciidisco/plugin.video.netflix/issues/86)

## Functionality

- Multiple profiles
- Search Netflix (incl. suggestions)
- Netflix categories, recommendations, "my list" & continue watching
- Rate show/movie
- Add & remove to/from "my list"
- Export of complete shows & movies in local database

## Something doesn't work

If something doesn't work for you, please:

- Make sure all prerequisites are met
- Enable verbose logging in the plugin settings
- Enable the Debug log in you Kodi settings
- Open an issue with a titles that summarises your problems

## Donate

If you like this project feel free to buy us some cups of coffee.
Our bitcoin address is: `1DHGftMkFXXsDY7UnqQuatWwxQzKVu88sF`

## Code of Conduct

[Contributor Code of Conduct](Code_of_Conduct.md)
By participating in this project you agree to abide by its terms.

## Licence

Licenced under The MIT License.

```

### File: requirements.txt
```txt
pycrypto==2.6.1
pycryptodomex==3.4.5
codeclimate-test-reporter==0.2.1
nose==1.3.7
pylint==1.6.5
flake8==3.3.0
mccabe==0.6.1
pycodestyle==2.3.1
pyflakes==1.5.0
git+https://github.com/romanvm/Kodistubs.git#egg=Kodistubs
httpretty==0.8.14
mock==1.0.1
requests==2.12.4
pydes==2.0.1
radon==2.1.1
Sphinx==1.5.5
sphinx_rtd_theme==0.2.4
m2r==0.1.12
git+https://github.com/asciidisco/kodi-release-helper.git#egg=kodi-release-helper
dennis==0.9
blessings==1.6
demjson==2.2.4
yamllint==1.8.1
restructuredtext_lint==1.1.1

```

### File: setup.py
```py
# -*- coding: utf-8 -*-
# Module: default
# Author: asciidisco
# Created on: 24.07.2017
# License: MIT https://goo.gl/5bMj3H

"""Setup"""

import os
import re
import sys
from setuptools import find_packages, setup

REQUIRED_PYTHON_VERSION = (2, 7)
PACKAGES = find_packages()
INSTALL_DEPENDENCIES = []
SETUP_DEPENDENCIES = []
TEST_DEPENDENCIES = [
    'nose',
    'Kodistubs',
    'httpretty',
    'mock',
]
EXTRA_DEPENDENCIES = {
    'dev': [
        'nose',
        'flake8',
        'codeclimate-test-reporter',
        'pylint',
        'mccabe',
        'pycodestyle',
        'pyflakes',
        'Kodistubs',
        'httpretty',
        'mock',
        'requests',
        'pyDes',
        'radon',
        'Sphinx',
        'sphinx_rtd_theme',
        'm2r',
        'kodi-release-helper',
        'dennis',
        'blessings',
        'demjson',
        'restructuredtext_lint',
        'yamllint',
    ]
}


def get_addon_data():
    """Loads the Kodi plugin data from addon.xml"""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    pathname = os.path.join(root_dir, 'addon.xml')
    with open(pathname, 'rb') as addon_xml:
        addon_xml_contents = addon_xml.read()
        _id = re.search(
            r'(?<!xml )id="(.+?)"',
            addon_xml_contents).group(1)
        author = re.search(
            r'(?<!xml )provider-name="(.+?)"',
            addon_xml_contents).group(1)
        name = re.search(
            r'(?<!xml )name="(.+?)"',
            addon_xml_contents).group(1)
        version = re.search(
            r'(?<!xml )version="(.+?)"',
            addon_xml_contents).group(1)
        desc = re.search(
            r'(?<!xml )description lang="en_GB">(.+?)<',
            addon_xml_contents).group(1)
        email = re.search(
            r'(?<!xml )email>(.+?)<',
            addon_xml_contents).group(1)
        source = re.search(
            r'(?<!xml )source>(.+?)<',
            addon_xml_contents).group(1)
        return {
            'id': _id,
            'author': author,
            'name': name,
            'version': version,
            'desc': desc,
            'email': email,
            'source': source,
        }


if sys.version_info < REQUIRED_PYTHON_VERSION:
    sys.exit('Python >= 2.7 is required. Your version:\n' + sys.version)

if __name__ == '__main__':
    ADDON_DATA = get_addon_data()
    setup(
        name=ADDON_DATA.get('name'),
        version=ADDON_DATA.get('version'),
        author=ADDON_DATA.get('author'),
        author_email=ADDON_DATA.get('email'),
        description=ADDON_DATA.get('desc'),
        packages=PACKAGES,
        include_package_data=True,
        install_requires=INSTALL_DEPENDENCIES,
        setup_requires=SETUP_DEPENDENCIES,
        tests_require=TEST_DEPENDENCIES,
        extras_require=EXTRA_DEPENDENCIES,
        test_suite='nose.collector',
    )

```

### File: addon.py
```py
# -*- coding: utf-8 -*-
# Author: asciidisco
# Module: default
# Created on: 13.01.2017
# License: MIT https://goo.gl/5bMj3H

"""Kodi plugin for Netflix (https://netflix.com)"""


import sys
from resources.lib.NetflixCommon import NetflixCommon
from resources.lib.Navigation import Navigation

# Setup plugin
PLUGIN_HANDLE = int(sys.argv[1])
BASE_URL = sys.argv[0]
# We use string slicing to trim the leading ? from the plugin call paramstring
REQUEST_PARAMS = sys.argv[2][1:]

# init plugin libs
NETFLIX_COMMON = NetflixCommon(
    plugin_handle=PLUGIN_HANDLE,
    base_url=BASE_URL
)

NAVIGATION = Navigation(
    nx_common=NETFLIX_COMMON
)

if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    NETFLIX_COMMON.log('Started (Version ' + NETFLIX_COMMON.version + ')')
    NAVIGATION.router(paramstring=REQUEST_PARAMS)

```

### File: Code_of_Conduct.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* Use of sexualized language/imagery and unwelcome sexual attention or advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at undefined. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 1.4, available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/

```

### File: Contributing.md
```md
# Contributing to plugin.video.netflix

Please take a moment to review this document in order to make the contribution
process easy and effective for everyone involved.

Following these guidelines helps to communicate that you respect the time of
the developers managing and developing this open source project. In return,
they should reciprocate that respect in addressing your issue, assessing
changes, and helping you finalize your pull requests.

As for everything else in the project, the contributions are governed by our
[Code of Conduct](Code_of_Conduct.md).

## Using the issue tracker

First things first: **Do NOT report security vulnerabilities in public issues!**
Please disclose responsibly by letting
[us](mailto:public@asciidisco.com?subject=NetflixPluginSecurity) know upfront.
We will assess the issue as soon as possible on a best-effort basis and will
give you an estimate for when we have a fix and release available for an
eventual public disclosure.

The issue tracker is the preferred channel for [bug reports](#bugs),
[features requests](#features) and [submitting pull
requests](#pull-requests), but please respect the following restrictions:

* Please **do not** use the issue tracker for personal support requests.

* Please **do not** derail or troll issues. Keep the discussion on topic and
  respect the opinions of others.

## Bug reports

A bug is a _demonstrable problem_ that is caused by the code in the repository.
Good bug reports are extremely helpful - thank you!

Guidelines for bug reports:

* **Use the GitHub issue search** &mdash; check if the issue has already been reported.
* **Check if the issue has been fixed** &mdash; try to reproduce it using `master`.
* **Isolate the problem** &mdash; ideally create a reduced test case.

A good bug report shouldn't leave others needing to chase you up for more
information. Please try to be as detailed as possible in your report. What is
your environment? What steps will reproduce the issue? What OS experiences the
problem? What would you expect to be the outcome? All these details will help
people to fix any potential bugs.

Example:

> Short and descriptive example bug report title
>
> A summary of the issue and the Kodi & the OS/Processor Arch
> environment in which it occurs. If
> suitable, include the steps required to reproduce the bug.
>
> `This is the first step`
> `This is the second step`
> `Further steps, etc.`
>
> `<log>` - a link to the Kodi debug log
>
> Any other information you want to share that is relevant to the issue being
> reported. This might include the lines of code that you have identified as
> causing the bug, and potential solutions (and your opinions on their
> merits).

## Feature requests

Feature requests are welcome. But take a moment to find out whether your idea
fits with the scope and aims of the project. It's up to *you* to make a strong
case to convince the project's developers of the merits of this feature. Please
provide as much detail and context as possible.

## Pull requests

Good pull requests - patches, improvements, new features - are a fantastic
help. They should remain focused in scope and avoid containing unrelated
commits.

**Please ask first** before embarking on any significant pull request (e.g.
implementing features, refactoring code), otherwise you risk spending a lot of
time working on something that the project's developers might not want to merge
into the project.

### For new Contributors

If you never created a pull request before, welcome :tada: :smile:
[Here is a great tutorial](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)
on how to send one :)

* [Fork](http://help.github.com/fork-a-repo/), clone, and configure the remotes:

```bash
# Clone your fork of the repo into the current directory
git clone https://github.com/<your-username>/<repo-name>
# Navigate to the newly cloned directory
cd <repo-name>
# Assign the original repo to a remote called "upstream"
git remote add upstream https://github.com/asciidisco/plugin.video.netflix
```

* If you cloned a while ago, get the latest changes from upstream:

   ```bash
   git checkout master
   git pull upstream master
   ```

* Create a new topic branch (off the main project development branch) to
   contain your feature, change, or fix:

   ```bash
   git checkout -b <topic-branch-name>
   ```

* Make sure to update, or add to the tests when appropriate. Patches and
   features will not be accepted without tests. Run `make test` to check that
   all tests pass after you've made changes.Run `make lint` to ensure
   that your code meets our guildelines (PEP-8)

* If you added or changed a feature, make sure to document it accordingly in
   the `README.md` file.

* Push your topic branch up to your fork:

   ```bash
   git push origin <topic-branch-name>
   ```

* Note: We follow Angular style commit guildelines

  Best to install NodeJS & use commitizen for that, all you need to do is

   ```bash
   npm install
   ```

   initially in the root directiory & then use

   ```bash
   make commit
   ```

   to commit changes.

* [Open a Pull Request](https://help.github.com/articles/using-pull-requests/)
    with a clear title and description.

### Addendum

Optionally, you can help us with these things. But don’t worry if they are too
complicated, we can help you out and teach you as we go :)

* Update your branch to the latest changes in the upstream master branch. You
   can do that locally with

   ```bash
   git pull --rebase upstream master
   ```

   Afterwards force push your changes to your remote feature branch.

* Once a pull request is good to go, you can tidy up your commit messages using
   Git's [interactive rebase](https://help.github.com/articles/interactive-rebase).
   Please follow our commit message conventions shown below, as they are used by
   [semantic-release](https://github.com/semantic-release/semantic-release) to
   automatically determine the new version and release to npm. In a nutshell:

#### Commit Message Conventions

* Commit test files with `test: ...` or `test(scope): ...` prefix
* Commit bug fixes with `fix: ...` or `fix(scope): ...` prefix
* Commit breaking changes by adding `BREAKING CHANGE:` in the commit body
    (not the subject line)
* Commit changes to `package.json`, `.gitignore` and other meta files with
    `chore(filenamewithoutext): ...`
* Commit changes to README files or comments with `docs: ...`
* Cody style changes with `style: standard`

**IMPORTANT**: By submitting a patch, you agree to license your work under the
same license as that used by the project.

## Maintainers

If you have commit access, please follow this process for
merging patches and cutting new releases.

### Reviewing changes

* Check that a change is within the scope and philosophy of the component.
* Check that a change has any necessary tests.
* Check that a change has any necessary documentation.
* If there is anything you don’t like, leave a comment below the respective
   lines and submit a "Request changes" review. Repeat until everything has
   been addressed.
* If you are not sure about something, mention `@asciidisco` or specific
   people for help in a comment.
* If there is only a tiny change left before you can merge it and you think
   it’s best to fix it yourself, you can directly commit to the author’s fork.
   Leave a comment about it so the author and others will know.
* Once everything looks good, add an "Approve" review. Don’t forget to say
   something nice 👏🐶💖✨
* If the commit messages follow [our conventions](@commit-message-conventions)

* If there is a breaking change, make sure that `BREAKING CHANGE:` with
    _exactly_ that spelling (incl. the ":") is in body of the according
    commit message. This is _very important_, better look twice :)
* Make sure there are `fix: ...` or `feat: ...` commits depending on whether
    a bug was fixed or a feature was added. **Gotcha:** look for spaces before
    the prefixes of `fix:` and `feat:`, these get ignored by semantic-release.
* Use the "Rebase and merge" button to merge the pull request.
* Done! You are awesome! Thanks so much for your help 🤗

* If the commit messages _do not_ follow our conventions

* Use the "squash and merge" button to clean up the commits and merge at
    the same time: ✨🎩
* Is there a breaking change? Describe it in the commit body. Start with
    _exactly_ `BREAKING CHANGE:` followed by an empty line. For the commit
    subject:
* Was a new feature added? Use `feat: ...` prefix in the commit subject
* Was a bug fixed? Use `fix: ...` in the commit subject

Sometimes there might be a good reason to merge changes locally. The process
looks like this:

### Reviewing and merging changes locally

```bash
git checkout master # or the main branch configured on github
git pull # get latest changes
git checkout feature-branch # replace name with your branch
git rebase master
git checkout master
git merge feature-branch # replace name with your branch
git push
```

When merging PRs from forked repositories, we recommend you install the
[hub](https://github.com/github/hub) command line tools.

This allows you to do:

```bash
hub checkout link-to-pull-request
```

meaning that you will automatically check out the branch for the pull request,
without needing any other steps like setting git upstreams! :sparkles:

```

### File: ISSUE_TEMPLATE.md
```md
*I'm submitting a ...*
  - [ ] bug report
  - [ ] feature request
  - [ ] support request

## General infomration

### Prerequisites

* [ ] Are you running the latest version?

### Description

[Description of the bug or feature]

### Steps to Reproduce

1. [First Step]
2. [Second Step]
3. [and so on...]

**Expected behavior:** [What you expected to happen]

**Actual behavior:** [What actually happened]

## Context (Environment)

### Installation

* [ ] I installed the plugin via zip from the Releases page
* [ ] I´m using the Netflix Repo
* [ ] I´m using a different source (Please tell which)

### Operating System

* [ ] Linux (x86/x64)
* [ ] OSX (x86/x64)
* [ ] Windows (x86/x64)
* [ ] Linux (ARM)
* [ ] Android

#### Additional informatin on the environment

[Descripe your environment a bit more detailed, are you using LibreElec f.e.]

## Debug log

[Please include a link to your debug log (use something like [http://sprunge.us/](http://sprunge.us/)) or similar, please do not paste]

## Other information

[e.g. detailed explanation, related issues, suggestions how to fix, links for us to have context, etc.]

### Screenshots

[Please add a screenshot if that helps understanding your problem]

[You can erase any parts of this template not applicable to your Issue.]

```

### File: LICENSE.txt
```txt
MIT License

Copyright (c) 2017 Sebastian Golasch

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

### File: PULL_REQUEST_TEMPLATE.md
```md
## Types of changes

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] I have read the [**CONTRIBUTING**](Contributing.md) document.

### All Submissions:

* [ ] Have you followed the guidelines in our Contributing document?
* [ ] Have you checked to ensure there aren't other open [Pull Requests](../../pulls) for the same update/change?


### Changes to Core Features:

* [ ] Have you added an explanation of what your changes do and why you'd like us to include them?
* [ ] Have you successfully ran tests with your changes locally?

## Screenshots (if appropriate):

[You can erase any parts of this template not applicable to your Pull Request.]

```

### File: service.py
```py
# -*- coding: utf-8 -*-
# Author: asciidisco
# Module: service
# Created on: 13.01.2017
# License: MIT https://goo.gl/5bMj3H

"""Kodi plugin for Netflix (https://netflix.com)"""

# pylint: disable=import-error

import threading
import socket
import sys
from datetime import datetime, timedelta

import xbmc
from resources.lib.NetflixCommon import NetflixCommon
from resources.lib.MSLHttpRequestHandler import MSLTCPServer
from resources.lib.NetflixHttpRequestHandler import NetflixTCPServer
from resources.lib.playback import PlaybackController
from resources.lib.playback.bookmarks import BookmarkManager
from resources.lib.playback.stream_continuity import StreamContinuityManager
from resources.lib.playback.section_skipping import SectionSkipper


def select_unused_port():
    """
    Helper function to select an unused port on the host machine

    :return: int - Free port
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 0))
    _, port = sock.getsockname()
    sock.close()
    return port


# Setup plugin
BASE_URL = sys.argv[0]
PLUGIN_HANDLE = None


def strp(value, form):
    """
    Helper function to safely create datetime objects from strings

    :return: datetime - parsed datetime object
    """
    # pylint: disable=broad-except
    from time import strptime
    def_value = datetime.utcfromtimestamp(0)
    try:
        return datetime.strptime(value, form)
    except TypeError:
        try:
            return datetime(*(strptime(value, form)[0:6]))
        except ValueError:
            return def_value
    except Exception:
        return def_value


class NetflixService(object):
    """
    Netflix addon service
    """
    def __init__(self):
        # init kodi helper (for logging)
        self.nx_common = NetflixCommon(plugin_handle=PLUGIN_HANDLE,
                                       base_url=BASE_URL)

        self.last_schedule_check = datetime.now()
        self.schedule_check_interval = int(self.nx_common.get_setting(
            'schedule_check_interval'))
        self.startidle = 0
        self.freq = int('0' + self.nx_common.get_setting('auto_update'))

        # pick & store a port for the MSL service
        msl_port = select_unused_port()
        self.nx_common.set_setting('msl_service_port', str(msl_port))
        self.nx_common.log(msg='[MSL] Picked Port: ' + str(msl_port))

        # pick & store a port for the internal Netflix HTTP proxy service
        ns_port = select_unused_port()
        self.nx_common.set_setting('netflix_service_port', str(ns_port))
        self.nx_common.log(msg='[NS] Picked Port: ' + str(ns_port))

        self.nx_common.flush_settings()

        # server defaults
        MSLTCPServer.allow_reuse_address = True
        NetflixTCPServer.allow_reuse_address = True

        # configure the MSL Server
        self.msl_server = MSLTCPServer(('127.0.0.1', msl_port),
                                       self.nx_common)

        # configure the Netflix Data Server
        self.ns_server = NetflixTCPServer(('127.0.0.1', ns_port),
                                          self.nx_common)

        self.msl_thread = threading.Thread(
            target=self.msl_server.serve_forever)

        self.ns_thread = threading.Thread(
            target=self.ns_server.serve_forever)

    def _start_servers(self):
        self.msl_server.server_activate()
        self.msl_server.timeout = 1

        # start thread for MLS servie
        self.msl_thread.start()
        self.nx_common.log(msg='[MSL] Thread started')

        self.ns_server.server_activate()
        self.ns_server.timeout = 1

        # start thread for Netflix HTTP service
        self.ns_thread.start()
        self.nx_common.log(msg='[NS] Thread started')

    def _shutdown(self):
        # MSL service shutdown sequence
        self.msl_server.server_close()
        self.msl_server.shutdown()
        self.msl_thread.join()
        self.msl_server = None
        self.msl_thread = None
        self.nx_common.log(msg='Stopped MSL Service')

        # Netflix service shutdown sequence
        self.ns_server.server_close()
        self.ns_server.shutdown()
        self.ns_thread.join()
        self.ns_server = None
        self.ns_thread = None
        self.nx_common.log(msg='Stopped HTTP Service')

    def _is_idle(self):
        if self.nx_common.get_setting('wait_idle') != 'true':
            return True

        lastidle = xbmc.getGlobalIdleTime()
        if xbmc.Player().isPlaying():
            self.startidle = lastidle
        if lastidle < self.startidle:
            self.startidle = 0
        idletime = lastidle - self.startidle
        return idletime >= 300

    def _update_running(self):
        update = self.nx_common.get_setting('update_running') or 'false'
        if update != 'false':
            starttime = strp(update, '%Y-%m-%d %H:%M')
            if (starttime + timedelta(hours=6)) <= datetime.now():
                self.nx_common.set_setting('update_running', 'false')
                self.nx_common.log(
                    'Canceling previous library update - duration > 6 hours',
                    xbmc.LOGWARNING)
            else:
                self.nx_common.log('DB Update already running')
                return True
        return False

    def run(self):
        """
        Main loop. Runs until xbmc.Monitor requests abort
        """
        self._start_servers()

        controller = PlaybackController(self.nx_common)
        controller.action_managers = [
            BookmarkManager(self.nx_common),
            SectionSkipper(self.nx_common),
            StreamContinuityManager(self.nx_common)
        ]
        player = xbmc.Player()
        while not controller.abortRequested():
            if self.ns_server.esn_changed():
                self.msl_server.reset_msl_data()

            try:
                if player.isPlayingVideo():
                    controller.on_playback_tick()
                if self.library_update_scheduled() and self._is_idle():
                    self.update_library()
            except RuntimeError as exc:
                self.nx_common.log(
                    'RuntimeError in main loop: {}'.format(exc), xbmc.LOGERROR)

            if controller.waitForAbort(1):
                break
        self._shutdown()

    def library_update_scheduled(self):
        """
        Checks if the scheduled time for a library update has been reached
        """
        now = datetime.now()
        next_schedule_check = (
            self.last_schedule_check +
            timedelta(minutes=self.schedule_check_interval))

        if not self.freq or now <= next_schedule_check:
            '''
            self.nx_common.log('Auto-update disabled or schedule check '
                               'interval not complete yet ({} / {}).'
                               .format(now, next_schedule_check))
            '''
            return False

        self.last_schedule_check = now
        time = self.nx_common.get_setting('update_time') or '00:00'
        lastrun_date = (self.nx_common.get_setting('last_update') or
                        '1970-01-01')

        lastrun_full = lastrun_date + ' ' + time[0:5]
        lastrun = strp(lastrun_full, '%Y-%m-%d %H:%M')
        freqdays = [0, 1, 2, 5, 7][self.freq]
        nextrun = lastrun + timedelta(days=freqdays)

        self.nx_common.log(
            'It\'s currently {}, next run is scheduled for {}'
            .format(now, nextrun))

        return now >= nextrun

    def update_library(self):
        """
        Triggers an update of the local Kodi library
        """
        if not self._update_running():
            self.nx_common.log('Triggering library update', xbmc.LOGNOTICE)
            xbmc.executebuiltin(
                ('XBMC.RunPlugin(plugin://{}/?action=export-new-episodes'
                 '&inbackground=True)')
                .format(self.nx_common.get_addon().getAddonInfo('id')))


if __name__ == '__main__':
    NetflixService().run()

```

### File: docs\conf.py
```py
# -*- coding: utf-8 -*-
#
# plugin.video.netflix documentation build configuration file, created by
# sphinx-quickstart on Wed Apr 26 16:27:25 2017.


import os
import re
import sys
from shutil import copyfile
import sphinx_rtd_theme

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
ROOT_PATH = os.path.dirname(os.path.dirname(BASE_PATH)) + os.path.sep

sys.path.insert(0, BASE_PATH)
sys.path.insert(0, ROOT_PATH)
sys.path.insert(0, ROOT_PATH + 'resources' + os.path.sep)
sys.path.insert(0, ROOT_PATH + 'resources' + os.path.sep + 'lib' + os.path.sep)

from setup import get_addon_data

ADDON_DATA = get_addon_data()

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.viewcode',
    'm2r']

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = ADDON_DATA.get('id', '')
copyright = u'2017, ' + ADDON_DATA.get('author', '')
author = ADDON_DATA.get('author', '')

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ADDON_DATA.get('version', '')
# The full version, including alpha/beta/rc tags.
release = ADDON_DATA.get('version', '')

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../resources/icon.png']
html_logo = '_static/icon.png'

```

### File: resources\__init__.py
```py

```

### File: resources\lib\compat.py
```py
import sys

#define >= 3 values here
itername = 'items'
string_encoding = 'unicode'
compat_unicode = str
compat_basestring = str

if (sys.version_info < (3, 0)):
    itername = 'iteritems'
    string_encoding = 'utf-8'
    compat_unicode = unicode
    compat_basestring = basestring

```

### File: resources\lib\KodiHelper.py
```py
# pylint: skip-file
# -*- coding: utf-8 -*-
# Module: KodiHelper
# Created on: 13.01.2017

import re
import json
import base64
import hashlib
from os import remove
from uuid import uuid4
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
import AddonSignals
import xbmc
import xbmcgui
import xbmcplugin
import inputstreamhelper
from resources.lib.compat import compat_unicode
from resources.lib.ui.Dialogs import Dialogs
from resources.lib.NetflixCommon import Signals
from resources.lib.utils import get_user_agent
from resources.lib.UniversalAnalytics import Tracker
try:
    import cPickle as pickle
except:
    import pickle
try:
    # Python 2.6-2.7
    from HTMLParser import HTMLParser
except ImportError:
    # Python 3
    from html.parser import HTMLParser

VIEW_FOLDER = 'folder'
VIEW_MOVIE = 'movie'
VIEW_SHOW = 'show'
VIEW_SEASON = 'season'
VIEW_EPISODE = 'episode'
VIEW_EXPORTED = 'exported'

CONTENT_FOLDER = 'files'
CONTENT_MOVIE = 'movies'
CONTENT_SHOW = 'tvshows'
CONTENT_SEASON = 'seasons'
CONTENT_EPISODE = 'episodes'


def _update_if_present(source_dict, source_att, target_dict, target_att):
    if source_dict.get(source_att):
        target_dict.update({target_att: source_dict[source_att]})


class KodiHelper(object):
    """
    Consumes all the configuration data from Kodi as well as
    turns data into lists of folders and videos"""

    def __init__(self, nx_common, library):
        """
        Provides helpers for addon side (not service side)
        """
        self.nx_common = nx_common
        self.plugin_handle = nx_common.plugin_handle
        self.base_url = nx_common.base_url
        self.library = library
        self.custom_export_name = nx_common.get_setting('customexportname')
        self.show_update_db = nx_common.get_setting('show_update_db')
        self.default_fanart = nx_common.get_addon_info('fanart')
        self.setup_memcache()
        self.dialogs = Dialogs(
            get_local_string=self.get_local_string,
            custom_export_name=self.custom_export_name)
        self._context_menu_actions = None

    def refresh(self):
        """Refresh the current list"""
        return xbmc.executebuiltin('Container.Refresh')

    def toggle_adult_pin(self):
        """Toggles the adult pin setting"""
        adultpin_enabled = False
        raw_adultpin_enabled = self.nx_common.get_setting('adultpin_enable')
        if raw_adultpin_enabled == 'true' or raw_adultpin_enabled == 'True':
            adultpin_enabled = True
        if adultpin_enabled is False:
            return self.nx_common.set_setting('adultpin_enable', 'True')
        return self.nx_common.set_setting('adultpin_enable', 'False')

    def set_main_menu_selection(self, type):
        """Persist the chosen main menu entry in memory

        Parameters
        ----------
        type : :obj:`str`
            Selected menu item
        """
        current_window = xbmcgui.getCurrentWindowId()
        xbmcgui.Window(current_window).setProperty('main_menu_selection', type)

    def get_main_menu_selection(self):
        """Gets the persisted chosen main menu entry from memory

        Returns
        -------
        :obj:`str`
            The last chosen main menu entry
        """
        current_window = xbmcgui.getCurrentWindowId()
        window = xbmcgui.Window(current_window)
        return window.getProperty('main_menu_selection')

    def setup_memcache(self):
        """Sets up the memory cache if not existant"""
        current_window = xbmcgui.getCurrentWindowId()
        window = xbmcgui.Window(current_window)
        try:
            cached_items = window.getProperty('memcache')
            # no cache setup yet, create one
            if len(cached_items) >= 1:
                return
        except (EOFError, UnicodeDecodeError):
            self.nx_common.log(msg='setup_memcache failed, recreating')
            pass
        window.setProperty('memcache', pickle.dumps({}, protocol=0).decode('latin-1'))

    def invalidate_memcache(self):
        """Invalidates the memory cache"""
        current_window = xbmcgui.getCurrentWindowId()
        window = xbmcgui.Window(current_window)
        try:
            window.setProperty('memcache', pickle.dumps({}, protocol=0).decode('latin-1'))
        except EOFError:
            self.nx_common.log(msg='invalidate_memcache failed')
            pass

    def get_cached_item(self, cache_id):
        """Returns an item from the in memory cache

        Parameters
        ----------
        cache_id : :obj:`str`
            ID of the cache entry

        Returns
        -------
        mixed
            Contents of the requested cache item or none
        """
        ret = None
        current_window = xbmcgui.getCurrentWindowId()
        window = xbmcgui.Window(current_window)
        try:
            cached_items = pickle.loads(window.getProperty('memcache').encode('latin-1'))
            ret = cached_items.get(cache_id)
        except (EOFError, UnicodeDecodeError) as e:
            self.nx_common.log(msg='memcache: get_cached_items failed' + str(e))
            ret = None
        return ret

    def add_cached_item(self, cache_id, contents):
        """Adds an item to the in memory cache

        Parameters
        ----------
        cache_id : :obj:`str`
            ID of the cache entry

        contents : mixed
            Cache entry contents
        """
        current_window = xbmcgui.getCurrentWindowId()
        window = xbmcgui.Window(current_window)
        try:
            cached_items = pickle.loads(window.getProperty('memcache').encode('latin-1'))
            cached_items.update({cache_id: contents})
            window.setProperty('memcache', pickle.dumps(cached_items, protocol=0).decode('latin-1'))
        except (EOFError, UnicodeDecodeError) as e:
            self.nx_common.log(msg='memcache: add_cached_items failed' + str(e))
            pass

    def set_custom_view(self, content):
        """Set the view mode

        Parameters
        ----------
        content : :obj:`str`

            Type of content in container
            (folder, movie, show, season, episode, login, exported)

        """
        custom_view = self.nx_common.get_setting('customview')
        if custom_view == 'true':
            view = int(self.nx_common.get_setting('viewmode' + content))
            if view != -1:
                xbmc.executebuiltin('Container.SetViewMode(%s)' % view)

    def save_autologin_data(self, autologin_user, autologin_id):
        """Write autologin data to settings

        Parameters
        ----------
        autologin_user : :obj:`str`
            Profile name from netflix

        autologin_id : :obj:`str`
            Profile id from netflix
        """
        self.nx_common.set_setting('autologin_user', autologin_user)
        self.nx_common.set_setting('autologin_id', autologin_id)
        self.nx_common.set_setting('autologin_enable', 'True')
        self.dialogs.show_autologin_enabled_notify()
        self.invalidate_memcache()
        self.refresh()

    def build_profiles_listing(self, profiles, action, build_url):
        """
        Builds the profiles list Kodi screen

        :param profiles: list of user profiles
        :type profiles: list
        :param action: action paramter to build the subsequent routes
        :type action: str
        :param build_url: function to build the subsequent routes
        :type build_url: fn
        :returns: bool -- List could be build
        """
        # init html parser for entity decoding
        html_parser = HTMLParser()
        # build menu items for every profile
        for profile in profiles:
            # load & encode profile data
            enc_profile_name = profile.get('profileName', '')
            unescaped_profile_name = html_parser.unescape(enc_profile_name)
            profile_guid = profile.get('guid')

            # build urls
            url = build_url({'action': action, 'profile_id': profile_guid})
            autologin_url = build_url({
                'action': 'save_autologin',
                'autologin_id': profile_guid,
                'autologin_user': enc_profile_name})

            # add list item
            list_item = xbmcgui.ListItem(
                label=unescaped_profile_name)
            list_item.setArt(
                {'fanart_image' : self.default_fanart,
                 'icon' : profile.get('avatar')})
            # add context menu options
            auto_login = (
                self.get_local_string(30053),
                'RunPlugin(' + autologin_url + ')')
            list_item.addContextMenuItems(items=[auto_login])

            # add directory & sorting options
            xbmcplugin.addDirectoryItem(
                handle=self.plugin_handle,
                url=url,
                listitem=list_item,
                isFolder=True)
            xbmcplugin.addSortMethod(
                handle=self.plugin_handle,
                sortMethod=xbmcplugin.SORT_METHOD_LABEL)

        xbmcplugin.setContent(
            handle=self.plugin_handle,
            content=CONTENT_FOLDER)

        return xbmcplugin.endOfDirectory(handle=self.plugin_handle)

    def build_main_menu_listing(self, video_list_ids, user_list_order, actions,
                                build_url, widget_display=False):
        """
        Builds the video lists (my list, continue watching, etc.) Kodi screen

        Parameters
        ----------
        video_list_ids : :obj:`dict` of :obj:`str`
            List of video lists

        user_list_order : :obj:`list` of :obj:`str`
            Ordered user lists
            to determine what should be displayed in the main menue

        actions : :obj:`dict` of :obj:`str`
            Dictionary of actions to build subsequent routes

        build_url : :obj:`fn`
            Function to build the subsequent routes

        Returns
        -------
        bool
            List could be build
        """
        preselect_items = []
        for category in user_list_order:
            for video_list_id in video_list_ids['user']:
                if video_list_ids['user'][video_list_id]['name'] == category:
                    label = video_list_ids['user'][video_list_id]['displayName']
                    if category == 'netflixOriginals':
                        label = label.capitalize()
                    li = xbmcgui.ListItem(label=label)
                    li.setArt(
                        {'fanart_image' : self.default_fanart,
                         'icon' : self.default_fanart})
                    # determine action route
                    action = actions['default']
                    if category in actions.keys():
                        action = actions[category]
                    # determine if the item should be selected
                    preselect_items.append((False, True)[category == self.get_main_menu_selection()])
                    url = build_url({'action': action, 'video_list_id': video_list_id, 'type': category})
                    xbmcplugin.addDirectoryItem(handle=self.plugin_handle, url=url, listitem=li, isFolder=True)

        # add recommendations/genres as subfolders
        # (save us some space on the home page)
        i18n_ids = {
            'recommendations': self.get_local_string(30001),
            'genres': self.get_local_string(30010)
        }
        for type in i18n_ids.keys():
            # determine if the lists have contents
            if len(video_list_ids[type]) > 0:
                # determine action route
                action = actions['default']
                if type in actions.keys():
                    action = actions[type]
                # determine if the item should be selected
                preselect_items.append((False, True)[type == self.get_main_menu_selection()])
                li_rec = xbmcgui.ListItem(
                    label=i18n_ids[type])
                li_rec.setArt(
                    {'fanart_image' : self.default_fanart,
                     'icon' : self.default_fanart})
                url_rec = build_url({'action': action, 'type': type})
                xbmcplugin.addDirectoryItem(
                    handle=self.plugin_handle,
                    url=url_rec,
                    listitem=li_rec,
                    isFolder=True)

        # add search as subfolder
        action = actions['default']
        if 'search' in actions.keys():
            action = actions[type]
        li_rec = xbmcgui.ListItem(
            label=self.get_local_string(30011))
        li_rec.setArt(
            {'fanart_image' : self.default_fanart,
             'icon' : self.default_fanart})

        url_rec = build_url({'action': action, 'type': 'search'})
        xbmcplugin.addDirectoryItem(
            handle=self.plugin_handle,
            url=url_rec,
            listitem=li_rec,
            isFolder=True)

        # add exported as subfolder
        action = actions['default']
        if 'exported' in actions.keys():
            action = actions[type]
        li_rec = xbmcgui.ListItem(
            label=self.get_local_string(30048))
        li_rec.setArt(
            {'fanart_image' : self.default_fanart,
             'icon' : self.default_fanart})

        url_rec = build_url({'action': action, 'type': 'exported'})
        xbmcplugin.addDirectoryItem(
            handle=self.plugin_handle,
            url=url_rec,
            listitem=li_rec,
            isFolder=True)

        if self.show_update_db == 'true':
            # add updatedb as subfolder
            li_rec = xbmcgui.ListItem(
                label=self.get_local_string(30049))
            li_rec.setArt(
                {'fanart_image' : self.default_fanart,
                 'icon' : self.default_fanart})

            url_rec = build_url({'action': 'updatedb'})
            xbmcplugin.addDirectoryItem(
                handle=self.plugin_handle,
                url=url_rec,
                listitem=li_rec,
                isFolder=True)

        # no sorting & close
        xbmcplugin.addSortMethod(
            handle=self.plugin_handle,
            sortMethod=xbmcplugin.SORT_METHOD_UNSORTED)
        xbmcplugin.setContent(
            handle=self.plugin_handle,
            content=CONTENT_FOLDER)
        xbmcplugin.endOfDirectory(self.plugin_handle)

        # (re)select the previously selected main menu entry
        preselected_list_item = None
        idx = 1
        for item in preselect_items:
            idx += 1
            preselected_list_item = idx if item else None
        preselected_list_item = idx + 1 if self.get_main_menu_selection() == 'search' else preselected_list_item
        if preselected_list_item is not None:
            xbmc.executebuiltin('ActivateWindowAndFocus(%s, %s)' % (str(xbmcgui.Window(xbmcgui.getCurrentWindowId()).getFocusId()), str(preselected_list_item)))
        if not widget_display:
            sel
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
