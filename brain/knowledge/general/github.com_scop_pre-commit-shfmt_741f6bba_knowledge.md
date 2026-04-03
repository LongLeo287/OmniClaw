---
id: github.com-scop-pre-commit-shfmt-741f6bba-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:19.562199
---

# KNOWLEDGE EXTRACT: github.com_scop_pre-commit-shfmt_741f6bba
> **Extracted on:** 2026-04-01 12:52:05
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522077/github.com_scop_pre-commit-shfmt_741f6bba

---

## File: `.gitignore`
```
/*.egg-info/
/.rtx.*.local.toml
/.rtx.local.toml
/build/
/dist/
/venv/
/wheelhouse/
```

## File: `.pre-commit-hooks.yaml`
```yaml
- id: shfmt
  name: shfmt
  description: Shell source code formatter (prebuilt upstream executable)
  language: python
  entry: shfmt
  args: [--write]
  types: [shell]
  exclude_types: [csh, tcsh, zsh]
  stages: [pre-commit, pre-merge-commit, pre-push, manual]
  minimum_pre_commit_version: 3.2.0 # for "stages" names

- id: shfmt-src
  name: shfmt
  description: Shell source code formatter (build from source)
  language: golang
  # Note: keep Go version in `go.mod` in sync with shfmt's required Go version
  additional_dependencies: [mvdan.cc/sh/v3/cmd/shfmt@v3.13.0]
  entry: shfmt
  args: [--write]
  types: [shell]
  exclude_types: [csh, tcsh, zsh]
  stages: [pre-commit, pre-merge-commit, pre-push, manual]
  minimum_pre_commit_version: 3.2.0 # for "stages" names

- id: shfmt-docker
  name: shfmt
  description: Shell source code formatter (Docker image)
  language: docker_image
  # Note: use the top level multiplatform image digest here
  entry: --net none mvdan/shfmt:v3.13.0@sha256:cb551dbf13a0e9a017e9c89647bcd4da3b1bd71eb16c6dc7588d2593a9b4611a
  args: [--write]
  types: [shell]
  exclude_types: [csh, tcsh, zsh]
  stages: [pre-commit, pre-merge-commit, pre-push, manual]
  minimum_pre_commit_version: 3.2.0 # for "stages" names
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2020 Ville Skyttä

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

## File: `README.md`
```markdown
# pre-commit-shfmt

[![Main push and PR checks](https://github.com/scop/pre-commit-shfmt/actions/workflows/check.yml/badge.svg)](https://github.com/scop/pre-commit-shfmt/actions/workflows/check.yml)
[![Tag checks](https://github.com/scop/pre-commit-shfmt/actions/workflows/check-tag.yml/badge.svg)](https://github.com/scop/pre-commit-shfmt/actions/workflows/check-tag.yml)
[![CodeQL](https://github.com/scop/pre-commit-shfmt/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/scop/pre-commit-shfmt/actions/workflows/github-code-scanning/codeql)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/scop/pre-commit-shfmt/badge)](https://scorecard.dev/viewer/?uri=github.com%2Fscop%2Fpre-commit-shfmt)

[shfmt](https://github.com/mvdan/sh#shfmt) hook for
[prek](https://prek.j178.dev) and
[pre-commit](https://pre-commit.com), with auto install.

Usage in `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/scop/pre-commit-shfmt
  rev: v3.13.0-1
  hooks:
    # Choose one of:
    - id: shfmt         # prebuilt upstream executable
    - id: shfmt-src     # build from source (requires/installs Go to build)
    - id: shfmt-docker  # Docker image (requires Docker to run)
```

> #### Notes
>
> From v3.12.0-2 on, the default args passed to `shfmt`
> [no longer contain `-s`](https://github.com/mvdan/sh/issues/1173).
>
> From v3.7.0-2 on, the `shfmt` id points to the variant that uses a prebuilt
> upstream executable. The one that builds from source is available as
> `shfmt-src`.
```

## File: `go.mod`
```
module github.com/scop/pre-commit-shfmt/v3

go 1.25.0
```

## File: `setup.cfg`
```
[metadata]
name = shfmt_py
version = 3.13.0-1
description = Shell source code formatter
url = https://github.com/scop/pre-commit-shfmt
# shfmt proper and Python packaging related files
license = BSD 3-Clause AND Apache Software License AND MIT License
classifiers =
    Intended Audience :: Developers
    Operating System :: MacOS
    Operating System :: Microsoft :: Windows
    Operating System :: POSIX :: Linux
    Programming Language :: Go
project_urls =
    Upstream = https://github.com/mvdan/sh#shfmt

[options]
packages =
python_requires = >=3.8
setup_requires =
    setuptools-download

[setuptools_download]
download_scripts =
    [shfmt]
    group = shfmt-binary
    marker = sys_platform == "darwin" and platform_machine == "x86_64"
    url = https://github.com/mvdan/sh/releases/download/v3.13.0/shfmt_v3.13.0_darwin_amd64
    sha256 = b6890a0009abf71d36d7c536ad56e3132c547ceb77cd5d5ee62b3469ab4e9417
    [shfmt]
    group = shfmt-binary
    marker = sys_platform == "darwin" and platform_machine == "arm64"
    url = https://github.com/mvdan/sh/releases/download/v3.13.0/shfmt_v3.13.0_darwin_arm64
    sha256 = 650970603b5946dc6041836ddcfa7a19d99b5da885e4687f64575508e99cf718
    [shfmt]
    group = shfmt-binary
    # TODO: verify i386
    marker = sys_platform == "linux" and platform_machine == "i386"
    marker = sys_platform == "linux" and platform_machine == "i686"
    url = https://github.com/mvdan/sh/releases/download/v3.13.0/shfmt_v3.13.0_linux_386
    sha256 = e645b59e34928442853fb5610dc485985f8acbe112a129679cede1dc320e54ff
    [shfmt]
    group = shfmt-binary
    marker = sys_platform == "linux" and platform_machine == "x86_64"
    url = https://github.com/mvdan/sh/releases/download/v3.13.0/shfmt_v3.13.0_linux_amd64
    sha256 = 70aa99784703a8d6569bbf0b1e43e1a91906a4166bf1a79de42050a6d0de7551
    [shfmt]
    group = shfmt-binary
    # TODO: verify armv6hf
    marker = sys_platform == "linux" and platform_machine == "armv6hf"
    marker = sys_platform == "linux" and platform_machine == "armv7l"
    url = https://github.com/mvdan/sh/releases/download/v3.13.0/shfmt_v3.13.0_linux_arm
    sha256 = 774b9a86cff4844179328cfbab2f602e75dcb68132e918e5271d015b3295c9c7
    [shfmt]
    group = shfmt-binary
    marker = sys_platform == "linux" and platform_machine == "aarch64"
    url = https://github.com/mvdan/sh/releases/download/v3.13.0/shfmt_v3.13.0_linux_arm64
    sha256 = 2091a31afd47742051a77bf7cfd175533ab07e924c20ef3151cd108fa1cab5b0
    [shfmt.exe]
    group = shfmt-binary
    # TODO: verify both
    marker = sys_platform == "win32" and platform_machine == "x86"
    marker = sys_platform == "cygwin" and platform_machine == "i386"
    url = https://github.com/mvdan/sh/releases/download/v3.13.0/shfmt_v3.13.0_windows_386.exe
    sha256 = f3e32b2a320a3053837add32803d7fb3b730d3f10b84a867d327a549ef068fa0
    [shfmt.exe]
    group = shfmt-binary
    marker = sys_platform == "win32" and platform_machine == "AMD64"
    marker = sys_platform == "cygwin" and platform_machine == "x86_64"
    url = https://github.com/mvdan/sh/releases/download/v3.13.0/shfmt_v3.13.0_windows_amd64.exe
    sha256 = 62241aaf6b0ca236f8625d8892784b73fa67ad40bc677a1ad1a64ae395f6a7d5
```

## File: `setup.py`
```python
# Copied from https://github.com/shellcheck-py/shellcheck-py/blob/0afa53fa8ddf1516d055db24e7ecb162980e67d7/setup.py,
# license at https://github.com/shellcheck-py/shellcheck-py/blob/0afa53fa8ddf1516d055db24e7ecb162980e67d7/LICENSE
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2019 Ryan Rhee
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup

try:
    from wheel.bdist_wheel import bdist_wheel as orig_bdist_wheel
except ImportError:
    cmdclass = {}
else:

    class bdist_wheel(orig_bdist_wheel):
        def finalize_options(self):
            orig_bdist_wheel.finalize_options(self)
            # Mark us as not a pure python package
            self.root_is_pure = False

        def get_tag(self):
            _, _, plat = orig_bdist_wheel.get_tag(self)
            # We don't contain any python source, nor any python extensions
            return "py2.py3", "none", plat

    cmdclass = {"bdist_wheel": bdist_wheel}

setup(cmdclass=cmdclass)
```

## File: `tools/generate_pre_commit_hooks.py`
```python
#!/usr/bin/env python3

import contextlib
import string
import sys

import docker


hooks_template = """
- id: shfmt
  name: shfmt
  description: Shell source code formatter (prebuilt upstream executable)
  language: python
  entry: shfmt
  args: [--write]
  types: [shell]
  exclude_types: [csh, tcsh]
  stages: [pre-commit, pre-merge-commit, pre-push, manual]
  minimum_pre_commit_version: 3.2.0 # for "stages" names

- id: shfmt-src
  name: shfmt
  description: Shell source code formatter (build from source)
  language: golang
  # Note: keep Go version in `go.mod` in sync with shfmt's required Go version
  additional_dependencies: [mvdan.cc/sh/v3/cmd/shfmt@${shfmt_tag}]
  entry: shfmt
  args: [--write]
  types: [shell]
  exclude_types: [csh, tcsh]
  stages: [pre-commit, pre-merge-commit, pre-push, manual]
  minimum_pre_commit_version: 3.2.0 # for "stages" names

- id: shfmt-docker
  name: shfmt
  description: Shell source code formatter (Docker image)
  language: docker_image
  # Note: use the top level multiplatform image digest here
  entry: --net none mvdan/shfmt:${shfmt_tag}@${docker_image_digest}
  args: [--write]
  types: [shell]
  exclude_types: [csh, tcsh]
  stages: [pre-commit, pre-merge-commit, pre-push, manual]
  minimum_pre_commit_version: 3.2.0 # for "stages" names
"""


def main(python_pkg_tag: str) -> None:
    shfmt_tag, _, _ = python_pkg_tag.partition("-")

    with contextlib.closing(docker.from_env()) as client:
        registry_data = client.images.get_registry_data(f"mvdan/shfmt:{shfmt_tag}")

    # Top level multiplatform image digest
    docker_image_digest = registry_data.attrs["Descriptor"]["digest"]

    data = {
        "shfmt_tag": shfmt_tag,
        "docker_image_digest": docker_image_digest,
    }
    st = string.Template(hooks_template.lstrip())
    hooks_yaml = st.substitute(data)
    sys.stdout.write(hooks_yaml)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} PYTHON-PKG-TAG", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
```

## File: `tools/generate_setup_cfg.py`
```python
#!/usr/bin/env python3

# Copyright 2023 Ville Skyttä
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

import json
import re
import string
import subprocess
import sys
from urllib.parse import quote as urlquote, urljoin

setup_cfg_template = """
[metadata]
name = shfmt_py
version = ${python_pkg_version}
description = Shell source code formatter
url = https://github.com/scop/pre-commit-shfmt
# shfmt proper and Python packaging related files
license = BSD 3-Clause AND Apache Software License AND MIT License
classifiers =
    Intended Audience :: Developers
    Operating System :: MacOS
    Operating System :: Microsoft :: Windows
    Operating System :: POSIX :: Linux
    Programming Language :: Go
project_urls =
    Upstream = https://github.com/mvdan/sh#shfmt

[options]
packages =
python_requires = >=3.8
setup_requires =
    setuptools-download

[setuptools_download]
download_scripts =
    [shfmt]
    group = shfmt-binary
    marker = sys_platform == "darwin" and platform_machine == "x86_64"
    url = ${url_darwin_amd64}
    sha256 = ${hexdigest_darwin_amd64}
    [shfmt]
    group = shfmt-binary
    marker = sys_platform == "darwin" and platform_machine == "arm64"
    url = ${url_darwin_arm64}
    sha256 = ${hexdigest_darwin_arm64}
    [shfmt]
    group = shfmt-binary
    # TODO: verify i386
    marker = sys_platform == "linux" and platform_machine == "i386"
    marker = sys_platform == "linux" and platform_machine == "i686"
    url = ${url_linux_386}
    sha256 = ${hexdigest_linux_386}
    [shfmt]
    group = shfmt-binary
    marker = sys_platform == "linux" and platform_machine == "x86_64"
    url = ${url_linux_amd64}
    sha256 = ${hexdigest_linux_amd64}
    [shfmt]
    group = shfmt-binary
    # TODO: verify armv6hf
    marker = sys_platform == "linux" and platform_machine == "armv6hf"
    marker = sys_platform == "linux" and platform_machine == "armv7l"
    url = ${url_linux_arm}
    sha256 = ${hexdigest_linux_arm}
    [shfmt]
    group = shfmt-binary
    marker = sys_platform == "linux" and platform_machine == "aarch64"
    url = ${url_linux_arm64}
    sha256 = ${hexdigest_linux_arm64}
    [shfmt.exe]
    group = shfmt-binary
    # TODO: verify both
    marker = sys_platform == "win32" and platform_machine == "x86"
    marker = sys_platform == "cygwin" and platform_machine == "i386"
    url = ${url_windows_386}
    sha256 = ${hexdigest_windows_386}
    [shfmt.exe]
    group = shfmt-binary
    marker = sys_platform == "win32" and platform_machine == "AMD64"
    marker = sys_platform == "cygwin" and platform_machine == "x86_64"
    url = ${url_windows_amd64}
    sha256 = ${hexdigest_windows_amd64}
"""

release_files = [
    "shfmt_{main_tag}_darwin_amd64",
    "shfmt_{main_tag}_darwin_arm64",
    "shfmt_{main_tag}_linux_386",
    "shfmt_{main_tag}_linux_amd64",
    "shfmt_{main_tag}_linux_arm",
    "shfmt_{main_tag}_linux_arm64",
    "shfmt_{main_tag}_windows_386.exe",
    "shfmt_{main_tag}_windows_amd64.exe",
]


def main(python_pkg_tag: str) -> None:
    main_tag, _, _ = python_pkg_tag.partition("-")
    base_url = f"https://github.com/mvdan/sh/releases/download/{urlquote(main_tag)}/"

    data = {
        "python_pkg_version": python_pkg_tag.lstrip("v"),
    }
    result = subprocess.run(["gh", "release", "view", "--repo", "mvdan/sh", main_tag, "--json", "assets"], stdout=subprocess.PIPE, check=True)
    assets = json.loads(result.stdout).get("assets", [])
    hexdigests = {asset["name"]: asset["digest"].removeprefix("sha256:") for asset in assets if asset["digest"].startswith("sha256:")}

    for fn in release_files:
        if m := re.search(r"_([a-z0-9]+_[a-z0-9]+)(?:\.exe)?$", fn):
            os_arch = m.group(1)
        else:
            raise ValueError(f"could not determine OS/arch from {fn}")
        fn = fn.format(main_tag=main_tag)
        data[f"url_{os_arch}"] = urljoin(base_url, urlquote(fn))
        if hexdigest := hexdigests.get(fn):
            data[f"hexdigest_{os_arch}"] = hexdigest
        else:
            raise KeyError(f"no hexdigest found for {fn}")

    st = string.Template(setup_cfg_template.lstrip())
    setup_cfg = st.substitute(data)
    sys.stdout.write(setup_cfg)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} PYTHON-PKG-TAG", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
```

