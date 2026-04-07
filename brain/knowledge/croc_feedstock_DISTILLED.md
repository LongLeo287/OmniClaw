---
id: croc-feedstock
type: knowledge
owner: OA_Triage
---
# croc-feedstock
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

For more information, please check the [conda-forge documentation](https://conda-forge.org/docs/).

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

### File: build-locally.py
```py
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

### File: LICENSE.txt
```txt
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

### File: .ci_support\linux_64_.yaml
```yaml
channel_sources:
- conda-forge
channel_targets:
- conda-forge main
docker_image:
- quay.io/condaforge/linux-anvil-x86_64:alma9
target_platform:
- linux-64

```

### File: .ci_support\linux_aarch64_.yaml
```yaml
channel_sources:
- conda-forge
channel_targets:
- conda-forge main
docker_image:
- quay.io/condaforge/linux-anvil-x86_64:alma9
target_platform:
- linux-aarch64

```

### File: .ci_support\linux_ppc64le_.yaml
```yaml
channel_sources:
- conda-forge
channel_targets:
- conda-forge main
docker_image:
- quay.io/condaforge/linux-anvil-x86_64:alma9
target_platform:
- linux-ppc64le

```

### File: .ci_support\osx_64_.yaml
```yaml
MACOSX_DEPLOYMENT_TARGET:
- '11.0'
MACOSX_SDK_VERSION:
- '11.0'
channel_sources:
- conda-forge
channel_targets:
- conda-forge main
macos_machine:
- x86_64-apple-darwin13.4.0
target_platform:
- osx-64

```

### File: .ci_support\osx_arm64_.yaml
```yaml
MACOSX_DEPLOYMENT_TARGET:
- '11.0'
MACOSX_SDK_VERSION:
- '11.0'
channel_sources:
- conda-forge
channel_targets:
- conda-forge main
macos_machine:
- arm64-apple-darwin20.0.0
target_platform:
- osx-arm64

```

### File: .ci_support\win_64_.yaml
```yaml
channel_sources:
- conda-forge
channel_targets:
- conda-forge main
target_platform:
- win-64

```

### File: .scripts\build_steps.sh
```sh
#!/usr/bin/env bash

# PLEASE NOTE: This script has been automatically generated by conda-smithy. Any changes here
# will be lost next time ``conda smithy rerender`` is run. If you would like to make permanent
# changes to this script, consider a proposal to conda-smithy so that other feedstocks can also
# benefit from the improvement.

# -*- mode: jinja-shell -*-

set -xeuo pipefail
export FEEDSTOCK_ROOT="${FEEDSTOCK_ROOT:-/home/conda/feedstock_root}"
source ${FEEDSTOCK_ROOT}/.scripts/logging_utils.sh


( endgroup "Start Docker" ) 2> /dev/null

( startgroup "Configuring conda" ) 2> /dev/null

export PYTHONUNBUFFERED=1
export RECIPE_ROOT="${RECIPE_ROOT:-/home/conda/recipe_root}"
export CI_SUPPORT="${FEEDSTOCK_ROOT}/.ci_support"
export CONFIG_FILE="${CI_SUPPORT}/${CONFIG}.yaml"
export RATTLER_CACHE_DIR="${FEEDSTOCK_ROOT}/build_artifacts/pkg_cache"

cat >~/.condarc <<CONDARC

conda-build:
  root-dir: ${FEEDSTOCK_ROOT}/build_artifacts
pkgs_dirs:
  - ${FEEDSTOCK_ROOT}/build_artifacts/pkg_cache
  - /opt/conda/pkgs
solver: libmamba

CONDARC
pushd "${FEEDSTOCK_ROOT}"
arch=$(uname -m)
if [[ "$arch" == "x86_64" ]]; then
  arch="64"
fi
sed -i.bak -e "s/platforms = .*/platforms = [\"linux-${arch}\"]/" -e "s/# __PLATFORM_SPECIFIC_ENV__ =/docker-build-linux-$arch =/" pixi.toml
echo "Creating environment"
PIXI_CACHE_DIR=/opt/conda pixi install --environment docker-build-linux-$arch
pixi list
echo "Activating environment"
eval "$(pixi shell-hook --environment docker-build-linux-$arch)"
mv pixi.toml.bak pixi.toml
popd
export CONDA_LIBMAMBA_SOLVER_NO_CHANNELS_FROM_INSTALLED=1

# set up the condarc
setup_conda_rc "${FEEDSTOCK_ROOT}" "${RECIPE_ROOT}" "${CONFIG_FILE}"

source run_conda_forge_build_setup



# make the build number clobber
make_build_number "${FEEDSTOCK_ROOT}" "${RECIPE_ROOT}" "${CONFIG_FILE}"

if [[ "${HOST_PLATFORM}" != "${BUILD_PLATFORM}" ]] && [[ "${HOST_PLATFORM}" != linux-* ]] && [[ "${BUILD_WITH_CONDA_DEBUG:-0}" != 1 ]]; then
    EXTRA_CB_OPTIONS="${EXTRA_CB_OPTIONS:-} --test skip"
fi


( endgroup "Configuring conda" ) 2> /dev/null

if [[ -f "${FEEDSTOCK_ROOT}/LICENSE.txt" ]]; then
  cp "${FEEDSTOCK_ROOT}/LICENSE.txt" "${RECIPE_ROOT}/recipe-scripts-license.txt"
fi

if [[ "${BUILD_WITH_CONDA_DEBUG:-0}" == 1 ]]; then
    echo "rattler-build currently doesn't support debug mode"
else

    rattler-build build --recipe "${RECIPE_ROOT}" \
     -m "${CI_SUPPORT}/${CONFIG}.yaml" \
     ${EXTRA_CB_OPTIONS:-} \
     --target-platform "${HOST_PLATFORM}" \
     --extra-meta flow_run_id="${flow_run_id:-}" \
     --extra-meta remote_url="${remote_url:-}" \
     --extra-meta sha="${sha:-}"
    ( startgroup "Inspecting artifacts" ) 2> /dev/null

    # inspect_artifacts was only added in conda-forge-ci-setup 4.9.4
    command -v inspect_artifacts >/dev/null 2>&1 && inspect_artifacts --recipe-dir "${RECIPE_ROOT}" -m "${CONFIG_FILE}" || echo "inspect_artifacts needs conda-forge-ci-setup >=4.9.4"

    ( endgroup "Inspecting artifacts" ) 2> /dev/null
    ( startgroup "Validating outputs" ) 2> /dev/null

    validate_recipe_outputs "${FEEDSTOCK_NAME}"

    ( endgroup "Validating outputs" ) 2> /dev/null

    ( startgroup "Uploading packages" ) 2> /dev/null

    if [[ "${UPLOAD_PACKAGES}" != "False" ]] && [[ "${IS_PR_BUILD}" == "False" ]]; then
        upload_package --validate --feedstock-name="${FEEDSTOCK_NAME}"  "${FEEDSTOCK_ROOT}" "${RECIPE_ROOT}" "${CONFIG_FILE}"
    fi

    ( endgroup "Uploading packages" ) 2> /dev/null
fi

( startgroup "Final checks" ) 2> /dev/null

touch "${FEEDSTOCK_ROOT}/build_artifacts/conda-forge-build-done-${CONFIG}"

```

### File: .scripts\logging_utils.sh
```sh
#!/bin/bash

# Provide a unified interface for the different logging
# utilities CI providers offer. If unavailable, provide
# a compatible fallback (e.g. bare `echo xxxxxx`).

function startgroup {
    # Start a foldable group of log lines
    # Pass a single argument, quoted
    case ${CI:-} in
        azure )
            echo "##[group]$1";;
        travis )
            echo "$1"
            echo -en 'travis_fold:start:'"${1// /}"'\r';;
        github_actions )
            echo "::group::$1";;
        * )
            echo "$1";;
    esac
} 2> /dev/null

function endgroup {
    # End a foldable group of log lines
    # Pass a single argument, quoted

    case ${CI:-} in
        azure )
            echo "##[endgroup]";;
        travis )
            echo -en 'travis_fold:end:'"${1// /}"'\r';;
        github_actions )
            echo "::endgroup::";;
    esac
} 2> /dev/null

```

### File: .scripts\run_docker_build.sh
```sh
#!/usr/bin/env bash

# PLEASE NOTE: This script has been automatically generated by conda-smithy. Any changes here
# will be lost next time ``conda smithy rerender`` is run. If you would like to make permanent
# changes to this script, consider a proposal to conda-smithy so that other feedstocks can also
# benefit from the improvement.

source .scripts/logging_utils.sh

( startgroup "Configure Docker" ) 2> /dev/null

set -xeo pipefail

THISDIR="$( cd "$( dirname "$0" )" >/dev/null && pwd )"
PROVIDER_DIR="$(basename "$THISDIR")"

FEEDSTOCK_ROOT="$( cd "$( dirname "$0" )/.." >/dev/null && pwd )"
RECIPE_ROOT="${FEEDSTOCK_ROOT}/recipe"

if [ -z ${FEEDSTOCK_NAME} ]; then
    export FEEDSTOCK_NAME=$(basename ${FEEDSTOCK_ROOT})
fi

if [[ "${sha:-}" == "" ]]; then
  pushd "${FEEDSTOCK_ROOT}"
  sha=$(git rev-parse HEAD)
  popd
fi

docker info

# In order for the conda-build process in the container to write to the mounted
# volumes, we need to run with the same id as the host machine, which is
# normally the owner of the mounted volumes, or at least has write permission
export HOST_USER_ID=$(id -u)
# Check if docker-machine is being used (normally on OSX) and get the uid from
# the VM
if hash docker-machine 2> /dev/null && docker-machine active > /dev/null; then
    export HOST_USER_ID=$(docker-machine ssh $(docker-machine active) id -u)
fi

ARTIFACTS="$FEEDSTOCK_ROOT/build_artifacts"

if [ -z "$CONFIG" ]; then
    set +x
    FILES=`ls .ci_support/linux_*`
    CONFIGS=""
    for file in $FILES; do
        CONFIGS="${CONFIGS}'${file:12:-5}' or ";
    done
    echo "Need to set CONFIG env variable. Value can be one of ${CONFIGS:0:-4}"
    exit 1
fi

if [ -z "${DOCKER_IMAGE}" ]; then
    SHYAML_INSTALLED="$(shyaml -h || echo NO)"
    if [ "${SHYAML_INSTALLED}" == "NO" ]; then
        echo "WARNING: DOCKER_IMAGE variable not set and shyaml not installed. Trying to parse with coreutils"
        DOCKER_IMAGE=$(cat .ci_support/${CONFIG}.yaml | grep '^docker_image:$' -A 1 | tail -n 1 | cut -b 3-)
        if [ "${DOCKER_IMAGE}" = "" ]; then
            echo "No docker_image entry found in ${CONFIG}. Falling back to quay.io/condaforge/linux-anvil-comp7"
            DOCKER_IMAGE="quay.io/condaforge/linux-anvil-comp7"
        fi
    else
        DOCKER_IMAGE="$(cat "${FEEDSTOCK_ROOT}/.ci_support/${CONFIG}.yaml" | shyaml get-value docker_image.0 quay.io/condaforge/linux-anvil-comp7 )"
    fi
fi

mkdir -p "$ARTIFACTS"
DONE_CANARY="$ARTIFACTS/conda-forge-build-done-${CONFIG}"
rm -f "$DONE_CANARY"

# Allow people to specify extra default arguments to `docker run` (e.g. `--rm`)
DOCKER_RUN_ARGS="${CONDA_FORGE_DOCKER_RUN_ARGS}"
if [ -z "${CI}" ]; then
    DOCKER_RUN_ARGS="-it ${DOCKER_RUN_ARGS}"
fi

( endgroup "Configure Docker" ) 2> /dev/null

( startgroup "Start Docker" ) 2> /dev/null

export UPLOAD_PACKAGES="${UPLOAD_PACKAGES:-True}"
export IS_PR_BUILD="${IS_PR_BUILD:-False}"
docker pull "${DOCKER_IMAGE}"
docker run ${DOCKER_RUN_ARGS} \
           -v "${RECIPE_ROOT}":/home/conda/recipe_root:rw,z,delegated \
           -v "${FEEDSTOCK_ROOT}":/home/conda/feedstock_root:rw,z,delegated \
           -e CONFIG \
           -e HOST_USER_ID \
           -e UPLOAD_PACKAGES \
           -e IS_PR_BUILD \
           -e GIT_BRANCH \
           -e UPLOAD_ON_BRANCH \
           -e CI \
           -e FEEDSTOCK_NAME \
           -e CPU_COUNT \
           -e BUILD_WITH_CONDA_DEBUG \
           -e BUILD_OUTPUT_ID \
           -e flow_run_id \
           -e remote_url \
           -e sha \
           -e BINSTAR_TOKEN \
           -e FEEDSTOCK_TOKEN \
           -e STAGING_BINSTAR_TOKEN \
           "${DOCKER_IMAGE}" \
           bash \
           "/home/conda/feedstock_root/${PROVIDER_DIR}/build_steps.sh"

# verify that the end of the script was reached
test -f "$DONE_CANARY"

# This closes the last group opened in `build_steps.sh`
( endgroup "Final checks" ) 2> /dev/null

```

### File: .scripts\run_osx_build.sh
```sh
#!/usr/bin/env bash

# -*- mode: jinja-shell -*-

source .scripts/logging_utils.sh

set -xe

MINIFORGE_HOME="${MINIFORGE_HOME:-${HOME}/miniforge3}"
MINIFORGE_HOME="${MINIFORGE_HOME%/}" # remove trailing slash
export CONDA_BLD_PATH="${CONDA_BLD_PATH:-${MINIFORGE_HOME}/conda-bld}"
( startgroup "Provisioning base env with pixi" ) 2> /dev/null
mkdir -p "${MINIFORGE_HOME}"
curl -fsSL https://pixi.sh/install.sh | bash
export PATH="~/.pixi/bin:$PATH"
arch=$(uname -m)
if [[ "$arch" == "x86_64" ]]; then
  arch="64"
fi
sed -i.bak "s/platforms = .*/platforms = [\"osx-${arch}\"]/" pixi.toml
echo "Creating environment"
pixi install
pixi list
echo "Activating environment"
eval "$(pixi shell-hook)"
mv pixi.toml.bak pixi.toml
( endgroup "Provisioning base env with pixi" ) 2> /dev/null

( startgroup "Configuring conda" ) 2> /dev/null
export CONDA_SOLVER="libmamba"
export CONDA_LIBMAMBA_SOLVER_NO_CHANNELS_FROM_INSTALLED=1





echo -e "\n\nSetting up the condarc and mangling the compiler."
setup_conda_rc ./ ./recipe ./.ci_support/${CONFIG}.yaml

if [[ "${CI:-}" != "" ]]; then
  mangle_compiler ./ ./recipe .ci_support/${CONFIG}.yaml
fi

if [[ "${CI:-}" != "" ]]; then
  echo -e "\n\nMangling homebrew in the CI to avoid conflicts."
  /usr/bin/sudo mangle_homebrew
  /usr/bin/sudo -k
else
  echo -e "\n\nNot mangling homebrew as we are not running in CI"
fi

if [[ "${sha:-}" == "" ]]; then
  sha=$(git rev-parse HEAD)
fi

if [[ "${OSX_SDK_DIR:-}" == "" ]]; then
  if [[ "${CI:-}" == "" ]]; then
    echo "Please set OSX_SDK_DIR to a directory where SDKs can be downloaded to. Aborting"
    exit 1
  else
    export OSX_SDK_DIR=/opt/conda-sdks
    /usr/bin/sudo mkdir -p "${OSX_SDK_DIR}"
    /usr/bin/sudo chown "${USER}" "${OSX_SDK_DIR}"
  fi
else
  if tmpf=$(mktemp -p "$OSX_SDK_DIR" tmp.XXXXXXXX 2>/dev/null); then
      rm -f "$tmpf"
      echo "OSX_SDK_DIR is writeable without sudo, continuing"
  else
      echo "User-provided OSX_SDK_DIR is not writeable for current user! Aborting"
      exit 1
  fi
fi

echo -e "\n\nRunning the build setup script."
source run_conda_forge_build_setup



( endgroup "Configuring conda" ) 2> /dev/null

if [[ -f LICENSE.txt ]]; then
  cp LICENSE.txt "recipe/recipe-scripts-license.txt"
fi

if [[ "${BUILD_WITH_CONDA_DEBUG:-0}" == 1 ]]; then
    echo "rattler-build does not currently support debug mode"
else

    if [[ "${HOST_PLATFORM}" != "${BUILD_PLATFORM}" ]]; then
        EXTRA_CB_OPTIONS="${EXTRA_CB_OPTIONS:-} --test skip"
    fi

    rattler-build build --recipe ./recipe \
        -m ./.ci_support/${CONFIG}.yaml \
        ${EXTRA_CB_OPTIONS:-} \
        --target-platform "${HOST_PLATFORM}" \
        --extra-meta flow_run_id="$flow_run_id" \
        --extra-meta remote_url="$remote_url" \
        --extra-meta sha="$sha"

    ( startgroup "Inspecting artifacts" ) 2> /dev/null

    # inspect_artifacts was only added in conda-forge-ci-setup 4.9.4
    command -v inspect_artifacts >/dev/null 2>&1 && inspect_artifacts --recipe-dir ./recipe -m ./.ci_support/${CONFIG}.yaml || echo "inspect_artifacts needs conda-forge-ci-setup >=4.9.4"

    ( endgroup "Inspecting artifacts" ) 2> /dev/null
    ( startgroup "Validating outputs" ) 2> /dev/null

    validate_recipe_outputs "${FEEDSTOCK_NAME}"

    ( endgroup "Validating outputs" ) 2> /dev/null

    ( startgroup "Uploading packages" ) 2> /dev/null

    if [[ "${UPLOAD_PACKAGES}" != "False" ]] && [[ "${IS_PR_BUILD}" == "False" ]]; then
      upload_package --validate --feedstock-name="${FEEDSTOCK_NAME}" ./ ./recipe ./.ci_support/${CONFIG}.yaml
    fi

    ( endgroup "Uploading packages" ) 2> /dev/null
fi

```

