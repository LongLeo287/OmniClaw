---
id: github.com-conda-forge-croc-feedstock-87874935-kno
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:41.507976
---

# KNOWLEDGE EXTRACT: github.com_conda-forge_croc-feedstock_87874935
> **Extracted on:** 2026-04-01 15:06:07
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524290/github.com_conda-forge_croc-feedstock_87874935

---

## File: `.gitattributes`
```
* text=auto

*.patch binary
*.diff binary
meta.yaml text eol=lf
build.sh text eol=lf
bld.bat text eol=crlf

# github helper pieces to make some files not show up in diffs automatically
.azure-pipelines/* linguist-generated=true
.circleci/* linguist-generated=true
.ci_support/README linguist-generated=true
.drone/* linguist-generated=true
.drone.yml linguist-generated=true
.github/* linguist-generated=true
.travis/* linguist-generated=true
.appveyor.yml linguist-generated=true
.gitattributes linguist-generated=true
.gitignore linguist-generated=true
.travis.yml linguist-generated=true
.scripts/* linguist-generated=true
.woodpecker.yml linguist-generated=true
/LICENSE.txt linguist-generated=true
/README.md linguist-generated=true
azure-pipelines.yml linguist-generated=true
build-locally.py linguist-generated=true
pixi.toml linguist-generated=true
shippable.yml linguist-generated=true
```

## File: `.gitignore`
```
# User content belongs under recipe/.
# Feedstock configuration goes in `conda-forge.yml`
# Everything else is managed by the conda-smithy rerender process.
# Please do not modify

# Ignore all files and folders in root
*
!/conda-forge.yml

# Don't ignore any files/folders if the parent folder is 'un-ignored'
# This also avoids warnings when adding an already-checked file with an ignored parent.
!/**/
# Don't ignore any files/folders recursively in the following folders
!/recipe/**
!/.ci_support/**

# Since we ignore files/folders recursively, any folders inside
# build_artifacts gets ignored which trips some build systems.
# To avoid that we 'un-ignore' all files/folders recursively
# and only ignore the root build_artifacts folder.
!/build_artifacts/**
/build_artifacts

*.pyc

# Rattler-build's artifacts are in `output` when not specifying anything.
/output
# Pixi's configuration
.pixi
```

## File: `LICENSE.txt`
```
BSD-3-Clause license
Copyright (c) 2015-2026, conda-forge contributors

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  1. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.
  2. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
  3. Neither the name of the copyright holder nor the names of its
     contributors may be used to endorse or promote products derived from
     this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.
```

## File: `README.md`
```markdown
About croc-feedstock
====================

Feedstock license: [BSD-3-Clause](https://github.com/conda-forge/croc-feedstock/blob/main/LICENSE.txt)

Home: https://github.com/schollz/croc

Package license: MIT

Summary: Securely send things from one computer to another

Development: https://github.com/schollz/croc

Current build status
====================


<table>
    
  <tr>
    <td>Azure</td>
    <td>
      <details>
        <summary>
          <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=23616&branchName=main">
            <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/croc-feedstock?branchName=main">
          </a>
        </summary>
        <table>
          <thead><tr><th>Variant</th><th>Status</th></tr></thead>
          <tbody><tr>
              <td>linux_64</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=23616&branchName=main">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/croc-feedstock?branchName=main&jobName=linux&configuration=linux%20linux_64_" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>linux_aarch64</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=23616&branchName=main">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/croc-feedstock?branchName=main&jobName=linux&configuration=linux%20linux_aarch64_" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>linux_ppc64le</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=23616&branchName=main">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/croc-feedstock?branchName=main&jobName=linux&configuration=linux%20linux_ppc64le_" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>osx_64</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=23616&branchName=main">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/croc-feedstock?branchName=main&jobName=osx&configuration=osx%20osx_64_" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>osx_arm64</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=23616&branchName=main">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/croc-feedstock?branchName=main&jobName=osx&configuration=osx%20osx_arm64_" alt="variant">
                </a>
              </td>
            </tr><tr>
              <td>win_64</td>
              <td>
                <a href="https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=23616&branchName=main">
                  <img src="https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/croc-feedstock?branchName=main&jobName=win&configuration=win%20win_64_" alt="variant">
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </details>
    </td>
  </tr>
</table>

Current release info
====================

| Name | Downloads | Version | Platforms |
| --- | --- | --- | --- |
| [![Conda Recipe](https://img.shields.io/badge/recipe-croc-green.svg)](https://anaconda.org/conda-forge/croc) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/croc.svg)](https://anaconda.org/conda-forge/croc) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/croc.svg)](https://anaconda.org/conda-forge/croc) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/croc.svg)](https://anaconda.org/conda-forge/croc) |

Installing croc
===============

Installing `croc` from the `conda-forge` channel can be achieved by adding `conda-forge` to your channels with:

```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Once the `conda-forge` channel has been enabled, `croc` can be installed with `conda`:

```
conda install croc
```

or with `mamba`:

```
mamba install croc
```

It is possible to list all of the versions of `croc` available on your platform with `conda`:

```
conda search croc --channel conda-forge
```

or with `mamba`:

```
mamba search croc --channel conda-forge
```

Alternatively, `mamba repoquery` may provide more information:

```
# Search all versions available on your platform:
mamba repoquery search croc --channel conda-forge

# List packages depending on `croc`:
mamba repoquery whoneeds croc --channel conda-forge

# List dependencies of `croc`:
mamba repoquery depends croc --channel conda-forge
```


About conda-forge
=================

[![Powered by
NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org)

conda-forge is a community-led conda channel of installable packages.
In order to provide high-quality builds, the process has been automated into the
conda-forge GitHub organization. The conda-forge organization contains one repository
for each of the installable packages. Such a repository is known as a *feedstock*.

A feedstock is made up of a conda recipe (the instructions on what and how to build
the package) and the necessary configurations for automatic building using freely
available continuous integration services. Thanks to the awesome service provided by
[Azure](https://azure.microsoft.com/en-us/services/devops/), [GitHub](https://github.com/),
[CircleCI](https://circleci.com/), [AppVeyor](https://www.appveyor.com/),
[Drone](https://cloud.drone.io/welcome), and [TravisCI](https://travis-ci.com/)
it is possible to build and upload installable packages to the
[conda-forge](https://anaconda.org/conda-forge) [anaconda.org](https://anaconda.org/)
channel for Linux, Windows and OSX respectively.

To manage the continuous integration and simplify feedstock maintenance,
[conda-smithy](https://github.com/conda-forge/conda-smithy) has been developed.
Using the ``conda-forge.yml`` within this repository, it is possible to re-render all of
this feedstock's supporting files (e.g. the CI configuration files) with ``conda smithy rerender``.

For more information, please check the [conda-forge documentation](https://conda-forge.org/brain/knowledge/docs_legacy/).

Terminology
===========

**feedstock** - the conda recipe (raw material), supporting scripts and CI configuration.

**conda-smithy** - the tool which helps orchestrate the feedstock.
                   Its primary use is in the construction of the CI ``.yml`` files
                   and simplify the management of *many* feedstocks.

**conda-forge** - the place where the feedstock and smithy live and work to
                  produce the finished article (built conda distributions)


Updating croc-feedstock
=======================

If you would like to improve the croc recipe or build a new
package version, please fork this repository and submit a PR. Upon submission,
your changes will be run on the appropriate platforms to give the reviewer an
opportunity to confirm that the changes result in a successful build. Once
merged, the recipe will be re-built and uploaded automatically to the
`conda-forge` channel, whereupon the built conda packages will be available for
everybody to install and use from the `conda-forge` channel.
Note that all branches in the conda-forge/croc-feedstock are
immediately built and any created packages are uploaded, so PRs should be based
on branches in forks, and branches in the main repository should only be used to
build distinct package versions.

In order to produce a uniquely identifiable distribution:
 * If the version of a package **is not** being increased, please add or increase
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string).
 * If the version of a package **is** being increased, please remember to return
   the [``build/number``](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#build-number-and-string)
   back to 0.

Feedstock Maintainers
=====================

* [@danielnachun](https://github.com/danielnachun/)

```

## File: `azure-pipelines.yml`
```yaml
# This file was generated automatically from conda-smithy. To update this configuration,
# update the conda-forge.yml and/or the recipe/meta.yaml.
# -*- mode: yaml -*-

stages:
- stage: Check
  jobs:
    - job: Skip
      pool:
        vmImage: 'ubuntu-latest'
      variables:
        DECODE_PERCENTS: 'false'
        RET: 'true'
      steps:
      - checkout: self
        fetchDepth: '2'
      - bash: |
          git_log=`git log --max-count=1 --skip=1 --pretty=format:"%B" | tr "\n" " "`
          echo "##vso[task.setvariable variable=log]$git_log"
        displayName: Obtain commit message
      - bash: echo "##vso[task.setvariable variable=RET]false"
        condition: and(eq(variables['Build.Reason'], 'PullRequest'), or(contains(variables.log, '[skip azp]'), contains(variables.log, '[azp skip]'), contains(variables.log, '[skip ci]'), contains(variables.log, '[ci skip]')))
        displayName: Skip build?
      - bash: echo "##vso[task.setvariable variable=start_main;isOutput=true]$RET"
        name: result
        displayName: Export result
- stage: Build
  condition: and(succeeded(), eq(dependencies.Check.outputs['Skip.result.start_main'], 'true'))
  dependsOn: Check
  jobs:
    - template: ./.azure-pipelines/azure-pipelines-linux.yml
    - template: ./.azure-pipelines/azure-pipelines-osx.yml
    - template: ./.azure-pipelines/azure-pipelines-win.yml
```

## File: `build-locally.py`
```python
#!/bin/sh
"""exec" "python3" "$0" "$@" #"""  # fmt: off # fmt: on

#
# This file has been generated by conda-smithy in order to build the recipe
# locally.
#
# The line above this comment is a bash / sh / zsh guard
# to stop people from running it with the wrong interpreter
import glob
import os
import platform
import subprocess
import sys
from argparse import ArgumentParser


def setup_environment(ns):
    os.environ["CONFIG"] = ns.config
    os.environ["UPLOAD_PACKAGES"] = "False"
    os.environ["IS_PR_BUILD"] = "True"
    if ns.debug:
        os.environ["BUILD_WITH_CONDA_DEBUG"] = "1"
        if ns.output_id:
            os.environ["BUILD_OUTPUT_ID"] = ns.output_id
    if "MINIFORGE_HOME" not in os.environ:
        os.environ["MINIFORGE_HOME"] = os.path.join(
            os.path.dirname(__file__), "miniforge3"
        )


def run_docker_build(ns):
    script = ".scripts/run_docker_build.sh"
    subprocess.check_call([script])


def run_osx_build(ns):
    script = ".scripts/run_osx_build.sh"
    subprocess.check_call([script])


def run_win_build(ns):
    script = ".scripts/run_win_build.bat"
    subprocess.check_call(["cmd", "/D", "/Q", "/C", f"CALL {script}"])


def verify_config(ns):
    choices_filter = ns.filter or "*"
    valid_configs = {
        os.path.basename(f)[:-5]
        for f in glob.glob(f".ci_support/{choices_filter}.yaml")
    }
    if choices_filter != "*":
        print(f"filtering for '{choices_filter}.yaml' configs")
    print(f"valid configs are {valid_configs}")
    if ns.config in valid_configs:
        print("Using " + ns.config + " configuration")
        return
    elif len(valid_configs) == 1:
        ns.config = valid_configs.pop()
        print("Found " + ns.config + " configuration")
    elif ns.config is None:
        print("config not selected, please choose from the following:\n")
        selections = list(enumerate(sorted(valid_configs), 1))
        for i, c in selections:
            print(f"{i}. {c}")
        try:
            s = input("\n> ")
        except KeyboardInterrupt:
            print("\nno option selected, bye!", file=sys.stderr)
            sys.exit(1)
        idx = int(s) - 1
        ns.config = selections[idx][1]
        print(f"selected {ns.config}")
    else:
        raise ValueError("config " + ns.config + " is not valid")
    if (
        ns.config.startswith("osx")
        and platform.system() == "Darwin"
        and not os.environ.get("OSX_SDK_DIR")
    ):
        raise RuntimeError(
            "Need OSX_SDK_DIR env variable set. Run 'export OSX_SDK_DIR=$PWD/SDKs' "
            "to download the SDK automatically to '$PWD/SDKs/MacOSX<ver>.sdk'. "
            "Note: OSX_SDK_DIR must be set to an absolute path. "
            "Setting this variable implies agreement to the licensing terms of the SDK by Apple."
        )


def main(args=None):
    p = ArgumentParser("build-locally")
    p.add_argument("config", default=None, nargs="?")
    p.add_argument(
        "--filter",
        default=None,
        help="Glob string to filter which build choices are presented in interactive mode.",
    )
    p.add_argument(
        "--debug",
        action="store_true",
        help="Setup debug environment using `conda debug`",
    )
    p.add_argument("--output-id", help="If running debug, specify the output to setup.")

    ns = p.parse_args(args=args)
    verify_config(ns)
    setup_environment(ns)

    try:
        if ns.config.startswith("linux") or (
            ns.config.startswith("osx") and platform.system() == "Linux"
        ):
            run_docker_build(ns)
        elif ns.config.startswith("osx"):
            run_osx_build(ns)
        elif ns.config.startswith("win"):
            run_win_build(ns)
    finally:
        recipe_license_file = os.path.join("recipe", "recipe-scripts-license.txt")
        if os.path.exists(recipe_license_file):
            os.remove(recipe_license_file)


if __name__ == "__main__":
    main()
```

## File: `conda-forge.yml`
```yaml
bot:
  automerge: true
build_platform:
  osx_arm64: osx_64
  linux_aarch64: linux_64
  linux_ppc64le: linux_64
github:
  branch_name: main
  tooling_branch_name: main
conda_build:
  error_overlinking: true
conda_build_tool: rattler-build
conda_forge_output_validation: true
conda_install_tool: pixi
provider:
  linux_aarch64: azure
  linux_ppc64le: azure
test: native_and_emulated
```

## File: `pixi.toml`
```
# -*- mode: toml -*-
# This file was generated automatically from conda-smithy. To update this configuration,
# update the conda-forge.yml and/or the recipe/meta.yaml.
"$schema" = "https://pixi.sh/v0.59.0/schema/manifest/schema.json"

[workspace]
name = "croc-feedstock"
version = "3.56.2"  # conda-smithy version used to generate this file
description = "Pixi configuration for conda-forge/croc-feedstock"
authors = ["@conda-forge/croc"]
channels = ["conda-forge"]
platforms = ["linux-64", "linux-aarch64", "linux-ppc64le", "osx-64", "win-64"]
requires-pixi = ">=0.59.0"

[dependencies]
conda-build = ">=24.1"
conda-forge-ci-setup = "4.*"
rattler-build = "*"

[tasks.inspect-all]
cmd = "inspect_artifacts --all-packages"
description = "List contents of all packages found in rattler-build build directory."
[tasks.build]
cmd = "rattler-build build --recipe recipe"
description = "Build croc-feedstock directly (without setup scripts), no particular variant specified"
[tasks."build-linux_64_"]
cmd = "rattler-build build --recipe recipe -m .ci_support/linux_64_.yaml"
description = "Build croc-feedstock with variant linux_64_ directly (without setup scripts)"
[tasks."inspect-linux_64_"]
cmd = "inspect_artifacts --recipe-dir recipe -m .ci_support/linux_64_.yaml"
description = "List contents of croc-feedstock packages built for variant linux_64_"
[tasks."build-linux_aarch64_"]
cmd = "rattler-build build --recipe recipe -m .ci_support/linux_aarch64_.yaml"
description = "Build croc-feedstock with variant linux_aarch64_ directly (without setup scripts)"
[tasks."inspect-linux_aarch64_"]
cmd = "inspect_artifacts --recipe-dir recipe -m .ci_support/linux_aarch64_.yaml"
description = "List contents of croc-feedstock packages built for variant linux_aarch64_"
[tasks."build-linux_ppc64le_"]
cmd = "rattler-build build --recipe recipe -m .ci_support/linux_ppc64le_.yaml"
description = "Build croc-feedstock with variant linux_ppc64le_ directly (without setup scripts)"
[tasks."inspect-linux_ppc64le_"]
cmd = "inspect_artifacts --recipe-dir recipe -m .ci_support/linux_ppc64le_.yaml"
description = "List contents of croc-feedstock packages built for variant linux_ppc64le_"
[tasks."build-osx_64_"]
cmd = "rattler-build build --recipe recipe -m .ci_support/osx_64_.yaml"
description = "Build croc-feedstock with variant osx_64_ directly (without setup scripts)"
[tasks."inspect-osx_64_"]
cmd = "inspect_artifacts --recipe-dir recipe -m .ci_support/osx_64_.yaml"
description = "List contents of croc-feedstock packages built for variant osx_64_"
[tasks."build-osx_arm64_"]
cmd = "rattler-build build --recipe recipe -m .ci_support/osx_arm64_.yaml"
description = "Build croc-feedstock with variant osx_arm64_ directly (without setup scripts)"
[tasks."inspect-osx_arm64_"]
cmd = "inspect_artifacts --recipe-dir recipe -m .ci_support/osx_arm64_.yaml"
description = "List contents of croc-feedstock packages built for variant osx_arm64_"
[tasks."build-win_64_"]
cmd = "rattler-build build --recipe recipe -m .ci_support/win_64_.yaml"
description = "Build croc-feedstock with variant win_64_ directly (without setup scripts)"
[tasks."inspect-win_64_"]
cmd = "inspect_artifacts --recipe-dir recipe -m .ci_support/win_64_.yaml"
description = "List contents of croc-feedstock packages built for variant win_64_"

[feature.smithy.dependencies]
conda-smithy = "*"
[feature.smithy.tasks.build-locally]
cmd = "python ./build-locally.py"
description = "Build packages locally using the same setup scripts used in conda-forge's CI"
[feature.smithy.tasks.smithy]
cmd = "conda-smithy"
description = "Run conda-smithy. Pass necessary arguments."
[feature.smithy.tasks.rerender]
cmd = "conda-smithy rerender"
description = "Rerender the feedstock."
[feature.smithy.tasks.lint]
cmd = "conda-smithy lint --conda-forge recipe"
description = "Lint the feedstock recipe"

[environments]
smithy = ["smithy"]

# This is a copy of default, to be enabled by build_steps.sh during Docker builds
# __PLATFORM_SPECIFIC_ENV__ = []
```

## File: `recipe/build.bat`
```
@echo on
@setlocal EnableDelayedExpansion

go build -o=%LIBRARY_PREFIX%\bin\%PKG_NAME%.exe -ldflags="-s" || goto :error
go-licenses save . --save_path=license-files || goto :error

goto :eof

:error
echo Failed with error #%errorlevel%.
exit 1
```

## File: `recipe/build.sh`
```bash
#!/usr/bin/env bash

set -o xtrace -o nounset -o pipefail -o errexit

go build -o=${PREFIX}/bin/${PKG_NAME} -ldflags="-s -w"
go-licenses save . --save_path=license-files
```

## File: `recipe/recipe.yaml`
```yaml
schema_version: 1

context:
  version: "10.4.2"

package:
  name: croc
  version: ${{ version }}

source:
  url: https://github.com/schollz/croc/archive/v${{ version }}.tar.gz
  sha256: 9ad752a5e87152c15698bac0f4157bcfa56918d49bc3947f3318e39e08be4f21

build:
  number: 0

requirements:
  build:
    - ${{ compiler('go-nocgo') }}
    - go-licenses

tests:
  - script:
      - croc --help

about:
  license: MIT
  license_file:
    - LICENSE
    - license-files/
  summary: Securely send things from one computer to another
  homepage: https://github.com/schollz/croc
  repository: https://github.com/schollz/croc

extra:
  recipe-maintainers:
    - danielnachun
```

