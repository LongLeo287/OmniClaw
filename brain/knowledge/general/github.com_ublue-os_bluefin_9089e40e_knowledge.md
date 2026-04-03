---
id: github.com-ublue-os-bluefin-9089e40e-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:32.757838
---

# KNOWLEDGE EXTRACT: github.com_ublue-os_bluefin_9089e40e
> **Extracted on:** 2026-04-01 14:54:32
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524161/github.com_ublue-os_bluefin_9089e40e

---

## File: `.devcontainer.json`
```json
// For format details, see https://aka.ms/devcontainer.json.
{
	"name": "bluefin-devcontainer",
	"image": "ghcr.io/ublue-os/devcontainer:latest"
}
```

## File: `.gitattributes`
```
*.yml linguist-detectable=true
*.yml linguist-language=YAML

*.yaml linguist-detectable=true
*.yaml linguist-language=YAML

*.just linguist-detectable=true
*.just linguist-documentation=false
*.just linguist-language=Just

*.json linguist-detectable=true
*.json linguist-documentation=false
*.json linguist-language=JSON
```

## File: `.gitignore`
```
flatpaks_with_deps
flatpak.*

*_build
*_build.*
previous.manifest.json
changelog.md
output.env
version.txt

devcontainer

# Python cache
__pycache__/
*.py[cod]
*$py.class
```

## File: `.gitmodules`
```
[submodule "system_files/shared/usr/share/gnome-shell/extensions/appindicatorsupport@rgcjonas.gmail.com"]
	path = system_files/shared/usr/share/gnome-shell/extensions/appindicatorsupport@rgcjonas.gmail.com
	url = https://github.com/ubuntu/gnome-shell-extension-appindicator.git
	branch = v61
[submodule "system_files/shared/usr/share/gnome-shell/extensions/tmp/bazaar-integration@kolunmi.github.io"]
	path = system_files/shared/usr/share/gnome-shell/extensions/tmp/bazaar-integration@kolunmi.github.io
	url = https://github.com/AlexanderVanhee/bazaar-companion.git
	branch = main
[submodule "system_files/shared/usr/share/gnome-shell/extensions/blur-my-shell@aunetx"]
	path = system_files/shared/usr/share/gnome-shell/extensions/blur-my-shell@aunetx
	url = https://github.com/aunetx/blur-my-shell.git
	branch = master
[submodule "system_files/shared/usr/share/gnome-shell/extensions/tmp/caffeine"]
	path = system_files/shared/usr/share/gnome-shell/extensions/tmp/caffeine
	url = https://github.com/eonpatapon/gnome-shell-extension-caffeine.git
	branch = v58
[submodule "system_files/shared/usr/share/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com"]
	path = system_files/shared/usr/share/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com
	url = https://github.com/micheleg/dash-to-dock.git
	branch = extensions.gnome.org-v102
[submodule "system_files/shared/usr/share/gnome-shell/extensions/gsconnect@andyholmes.github.io"]
	path = system_files/shared/usr/share/gnome-shell/extensions/gsconnect@andyholmes.github.io
	url = https://github.com/GSConnect/gnome-shell-extension-gsconnect.git
	branch = v67
[submodule "system_files/shared/usr/share/gnome-shell/extensions/logomenu@aryan_k"]
	path = system_files/shared/usr/share/gnome-shell/extensions/logomenu@aryan_k
	url = https://github.com/ublue-os/Logomenu.git
[submodule "system_files/shared/usr/share/gnome-shell/extensions/search-light@icedman.github.com"]
	path = system_files/shared/usr/share/gnome-shell/extensions/search-light@icedman.github.com
	url = https://github.com/icedman/search-light.git
```

## File: `.pre-commit-config.yaml`
```yaml
# .pre-commit-config.yaml

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
        - id: check-json
        - id: check-toml
        - id: check-yaml
        - id: end-of-file-fixer
        - id: trailing-whitespace
```

## File: `AGENTS.md`
```markdown
# Bluefin Copilot Instructions

This document provides essential information for coding agents working with the Bluefin repository to minimize exploration time and avoid common build failures.

## Repository Overview

**Bluefin** is a cloud-native desktop operating system that reimagines the Linux desktop experience. It's an OS built on Fedora Linux using container technologies with atomic updates.

- **Type**: Container-based Linux distribution build system (75MB total, 74MB system files)
- **Base**: Fedora Linux with GNOME Desktop + Universal Blue infrastructure
- **Languages**: Bash scripts, JSON configuration, Python utilities
- **Build System**: Just (command runner), Podman/Docker containers, GitHub Actions
- **Target**: desktop OS with two variants (base + developer experience)

## Repository Structure

### Root Directory Files
- `Containerfile` - Main container build definition (multi-stage: base → dx)
- `Justfile` - Build automation recipes (33KB - like Makefile but more readable)
- `.pre-commit-config.yaml` - Pre-commit hooks for basic validation
- `image-versions.yml` - Image version configurations
- `cosign.pub` - Container signing public key

### Key Directories
- `system_files/` (74MB) - User-space files, configurations, fonts, themes
- `build_files/` - Build scripts organized as base/, dx/, shared/
  - `base/` - Base image build scripts (00-image-info.sh through 19-initramfs.sh)
  - `dx/` - Developer experience build scripts
  - `shared/` - Common build utilities and helper scripts
- `.github/workflows/` - Comprehensive CI/CD pipelines
- `just/` - Additional Just recipes for apps and system management
- `brew/` - Homebrew Brewfile definitions for various tool collections
- `flatpaks/` - Flatpak application lists (system-flatpaks.list, system-flatpaks-dx.list)

### Architecture
- **Two Build Targets**: `base` (regular users) and `dx` (developer experience)
- **Image Flavors**: main, nvidia-open
- **Fedora Versions**: 42, 43 supported
- **Stream Tags**: `latest` (F42/43), `beta` (F42/43), `stable` (F42)
- **Build Process**: Sequential shell scripts in build_files/ directory
- **Base Images**: Uses `ghcr.io/ublue-os/silverblue-main` as foundation from Universal Blue

## Build Instructions

### Prerequisites
**ALWAYS install these tools before attempting any builds:**

```bash
# Install Just command runner (REQUIRED for build commands, may not be available)
# If external access is limited, Just commands will not work
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin
export PATH="$HOME/.local/bin:$PATH"

# Verify container runtime (usually available)
podman --version || docker --version

# Install pre-commit for validation (usually works)
pip install pre-commit
```

**Note**: In restricted environments, Just command runner may not be installable. Most validation can still be done with pre-commit and manual JSON validation.

### Essential Commands

**Build validation (ALWAYS run before making changes):**
```bash
# 1. Validate syntax and formatting (2-3 minutes)
# Note: .devcontainer.json will fail JSON check due to comments - this is expected
pre-commit run --all-files

# 2. Check Just syntax (requires Just installation)
just check  # Only if Just command runner is available

# 3. Fix formatting issues automatically
just fix    # Only if Just command runner is available
```

**Build commands (use with extreme caution - these take 30+ minutes and require significant resources):**
```bash
# Build base image (30-60 minutes, requires 20GB+ disk space)
just build bluefin latest main

# Build developer variant (45-90 minutes, requires 25GB+ disk space)
just build bluefin-dx latest main

# Build with specific kernel pin
just build bluefin latest main "" "" "" "6.10.10-200.fc40.x86_64"
```

**Utility commands:**
```bash
# Clean build artifacts (if Just available)
just clean

# List all available recipes (if Just available)
just --list

# Validate image/tag/flavor combinations (if Just available)
just validate bluefin latest main
```

**Working without Just (when external access is restricted):**
```bash
# Manual validation instead of 'just check':
find . -name "*.just" -exec echo "Checking {}" \; -exec head -5 {} \;

# Manual cleanup instead of 'just clean':
rm -rf *_build* previous.manifest.json changelog.md output.env

# View Justfile recipes manually:
grep -n "^[a-zA-Z].*:" Justfile | head -20
```

### Critical Build Notes

1. **Container builds require massive resources** (20GB+ disk, 8GB+ RAM, 30+ minute runtime)
2. **Always run `just check` before making changes** - catches syntax errors early
3. **Pre-commit hooks are mandatory** - run `pre-commit run --all-files` to validate changes
4. **Never run full builds in CI unless specifically testing container changes**
5. **Use `just clean` to reset build state if encountering issues**

### Common Build Failures & Workarounds

**Pre-commit failures:**
```bash
# Known issue: .devcontainer.json contains comments (invalid for JSON checker)
# This failure is expected and can be ignored:
# ".devcontainer.json: Failed to json decode"

# Fix end-of-file and trailing whitespace automatically
pre-commit run --all-files
```

**Just syntax errors (if Just is available):**
```bash
# Auto-fix formatting
just fix

# Manual validation
just check
```

**Container build failures:**
- Ensure adequate disk space (25GB+ free)
- Clean previous builds: `just clean` (if available)
- Check container runtime: `podman system info` or `docker system info`
- Build failures often indicate resource constraints rather than code issues

## Validation Pipeline

### Pre-commit Hooks (REQUIRED)
The repository uses mandatory pre-commit validation:
- `check-json` - Validates JSON syntax
- `check-toml` - Validates TOML syntax
- `check-yaml` - Validates YAML syntax
- `end-of-file-fixer` - Ensures files end with newline
- `trailing-whitespace` - Removes trailing whitespace

**Always run:** `pre-commit run --all-files` before committing changes.

### GitHub Actions Workflows
- `build-image-latest-main.yml` - Builds latest images on main branch changes
- `build-image-stable.yml` - Builds stable release images
- `build-image-beta.yml` - Builds beta images for testing F42/F43
- `reusable-build.yml` - Core build logic for all image variants
- `generate-release.yml` - Generates release artifacts and changelogs
- `validate-brewfiles.yml` - Validates Homebrew Brewfile syntax
- `clean.yml` - Cleanup old images and artifacts
- `moderator.yml` - Repository moderation tasks

**Workflow Architecture:**

- Stream-specific workflows (stable, latest, beta) call `reusable-build.yml`
- `reusable-build.yml` builds both base and dx variants for all flavors (main, nvidia-open)
- Fedora version is dynamically detected based on stream tag
- Images are signed with cosign and pushed to GHCR

### Manual Validation Steps
1. `pre-commit run --all-files` - Runs validation hooks (2-3 minutes, .devcontainer.json failure is expected)
2. `just check` - Validates Just syntax (if Just is available, 30 seconds)
3. `just fix` - Auto-fixes formatting issues (if Just is available, 30 seconds)
4. Test builds only if making container-related changes (30+ minutes)

## Package Management

### Package Configuration
Packages are defined directly in build scripts rather than in a central configuration file:
- `build_files/base/04-packages.sh` - Core package installations
  - `FEDORA_PACKAGES` array - Packages from official Fedora repos (installed in bulk)
  - `COPR_PACKAGES` array - Packages from COPR repos (installed individually with isolated enablement)
  - Fedora version-specific package sections using case statements (e.g., `42)`, `43)`)
- `build_files/dx/00-dx.sh` - Developer experience package additions

### COPR Package Installation

COPR packages use the `copr_install_isolated()` helper function from `build_files/shared/copr-helpers.sh`:
```bash
# Install packages from COPR with isolated repo enablement
copr_install_isolated "ublue-os/staging" package1 package2

```

This function:
1. Enables the COPR repo
2. Immediately disables it
3. Installs packages with `--enablerepo` flag to prevent repo conflicts

### Making Package Changes
1. Edit the appropriate shell script in `build_files/base/` or `build_files/dx/`
2. Add packages to the appropriate array (`FEDORA_PACKAGES` or `COPR_PACKAGES`)
3. For version-specific packages, add them in the Fedora version case statement
4. Validate shell script syntax: `bash -n build_files/base/04-packages.sh`
5. Run pre-commit hooks: `pre-commit run --all-files`
6. Test with container build if making critical changes

### Package Security Model
**CRITICAL**: Packages are split into separate arrays to prevent COPR repos from injecting malicious versions of Fedora packages:
- Fedora packages are installed first in bulk (safe)
- COPR packages are installed individually with isolated repo enablement

## Configuration Files

### Key Configuration Locations
- `system_files/shared/` - System-wide configurations
- `build_files/base/` - Base image build scripts
- `build_files/dx/` - Developer experience build scripts
- `build_files/shared/` - Common build utilities
- `.github/workflows/` - CI/CD pipeline definitions

### Linting/Build Configurations
- `.pre-commit-config.yaml` - Pre-commit hook configuration
- `Justfile` - Build recipe definitions and validation
- `.github/renovate.json5` - Automated dependency updates
- `Containerfile` - Container build instructions

## Build System Deep Dive

### Justfile Structure
The `Justfile` is the central build orchestration tool with these key recipes:

**Validation Recipes:**
- `just check` - Validates Just syntax across all .just files
- `just fix` - Auto-formats Just files
- `just validate <image> <tag> <flavor>` - Validates image/tag/flavor combinations

**Build Recipes:**
- `just build <image> <tag> <flavor>` - Main build command (calls build.sh)
- `just build-ghcr <image> <tag> <flavor>` - Build for GHCR (GitHub Container Registry)
- `just rechunk <image> <tag> <flavor>` - Rechunk image for optimization

**Image/Tag Definitions:**
```bash
images: bluefin, bluefin-dx
flavors: main, nvidia-open
tags: stable, latest, beta
```

**Version Detection:**
- `just fedora_version <image> <tag> <flavor>` - Dynamically detects Fedora version from upstream base images
- For `stable`: Checks `ghcr.io/ublue-os/base-main:<tag>`
- For `latest`/`beta`: Checks corresponding upstream tags
- Returns the Fedora major version (e.g., 42, 43)

### Containerfile Multi-Stage Build
The `Containerfile` uses a multi-stage build process:

1. **Stage `ctx`** (FROM scratch): Copies all build context (system_files, build_files, etc.)
2. **Stage `base`** (FROM silverblue-main): Base Bluefin image
   - Mounts build context from `ctx` stage
   - Runs `/ctx/build_files/shared/build.sh` which executes all scripts in order
3. **Stage `dx`** (optional, in full Containerfile): Developer experience layer

**Build Arguments:**
- `BASE_IMAGE_NAME` - Upstream base (silverblue/kinoite)
- `FEDORA_MAJOR_VERSION` - Dynamically set by Just (42/43)
- `IMAGE_NAME` - Target image name (bluefin/bluefin-dx)
- `KERNEL` - Pinned kernel version (optional)
- `UBLUE_IMAGE_TAG` - Stream tag (stable/latest/beta)

### Build Script Execution Order
Scripts in `build_files/base/` execute in numerical order:
1. `00-image-info.sh` - Sets image metadata and os-release info
2. `03-install-kernel-akmods.sh` - Installs kernel and akmod packages
3. `04-packages.sh` - Installs Fedora and COPR packages
4. `05-override-install.sh` - Overrides base image packages
5. `08-firmware.sh` - Firmware configurations
6. `17-cleanup.sh` - Cleanup operations
7. `18-workarounds.sh` - Temporary fixes/workarounds
8. `19-initramfs.sh` - Regenerates initramfs

### Additional Recipe Collections
- `just/bluefin-apps.just` - User-facing app management recipes
- `just/bluefin-system.just` - System management recipes
- `brew/*.Brewfile` - Homebrew package collections (ai, cli, fonts, k8s)

## Development Guidelines

### Making Changes
1. **ALWAYS validate first:** `just check && pre-commit run --all-files`
2. **Make minimal modifications** - prefer configuration over code changes
3. **Test formatting:** `just fix` to auto-format
4. **Avoid full container builds** unless specifically testing container changes
5. **Focus on system_files/ changes** for most user-facing modifications

### File Editing Best Practices
- **JSON files**: Validate syntax with `pre-commit run check-json`
- **YAML files**: Validate syntax with `pre-commit run check-yaml`
- **Justfile**: Always run `just check` after modifications
- **Shell scripts**: Follow existing patterns in build_files/

### Common Modification Patterns
- **Adding packages**: Edit `build_files/base/04-packages.sh`, add to appropriate array
- **System configuration**: Modify files in `system_files/shared/`
- **Build logic**: Edit scripts in `build_files/base/` or `build_files/dx/`
- **CI/CD**: Modify workflows in `.github/workflows/`

## Trust These Instructions

**The information in this document has been validated against the current repository state.** Only search for additional information if:
- Instructions are incomplete for your specific task
- You encounter errors not covered in the workarounds section
- Repository structure has changed significantly

This repository is complex but well-structured. Following these instructions will significantly reduce build failures and exploration time.

## Other Rules that are Important to the Maintainers

- Ensure that [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/#specification) are used and enforced for every commit and pull request title.
- Always be surgical with the least amount of code, the project strives to be easy to maintain.
- Documentation for this project exists in ublue-os/bluefin-docs
- Bluefin LTS exists in ublue-os/bluefin-lts

## Attribution Requirements

AI agents must disclose what tool and model they are using in the "Assisted-by" commit footer:

```text
Assisted-by: [Model Name] via [Tool Name]
```

Example:

```text
Assisted-by: Claude 3.5 Sonnet via GitHub Copilot
```
```

## File: `CONTRIBUTING.md`
```markdown
# CONTRIBUTING 

Thanks for helping out! 

Check the [Contributing Guide](https://docs.projectbluefin.io/contributing) for contribution information.

This repository is for building the images, you are probably looking for [@projectbluefin/common](https://github.com/projectbluefin/common) to change something in Bluefin. Make sure you check [the architecture diagram](https://docs.projectbluefin.io/contributing#understanding-bluefins-architecture). 
```

## File: `Containerfile`
```
ARG BASE_IMAGE_NAME="silverblue"
ARG FEDORA_MAJOR_VERSION="42"
ARG SOURCE_IMAGE="${BASE_IMAGE_NAME}-main"
ARG BASE_IMAGE="ghcr.io/ublue-os/${SOURCE_IMAGE}"
ARG COMMON_IMAGE="ghcr.io/projectbluefin/common:latest"
ARG COMMON_IMAGE_SHA=""
ARG BREW_IMAGE="ghcr.io/ublue-os/brew:latest"
ARG BREW_IMAGE_SHA=""

FROM ${COMMON_IMAGE}@${COMMON_IMAGE_SHA} AS common
FROM ${BREW_IMAGE}@${BREW_IMAGE_SHA} AS brew

FROM scratch AS ctx
COPY /system_files /system_files
COPY /build_files /build_files
COPY --from=common /system_files/shared /system_files/shared
COPY --from=common /system_files/bluefin /system_files/shared
COPY --from=brew /system_files /system_files/shared

## bluefin image section
FROM ${BASE_IMAGE}:${FEDORA_MAJOR_VERSION} AS base

ARG AKMODS_FLAVOR="coreos-stable"
ARG BASE_IMAGE_NAME="silverblue"
ARG FEDORA_MAJOR_VERSION="40"
ARG IMAGE_NAME="bluefin"
ARG IMAGE_VENDOR="ublue-os"
ARG KERNEL="6.10.10-200.fc40.x86_64"
ARG SHA_HEAD_SHORT="dedbeef"
ARG UBLUE_IMAGE_TAG="stable"
ARG VERSION=""
ARG IMAGE_FLAVOR=""

# Build, cleanup, lint.
RUN --mount=type=cache,dst=/var/cache/libdnf5 \
    --mount=type=cache,dst=/var/cache/rpm-ostree \
    --mount=type=bind,from=ctx,source=/,target=/ctx \
    --mount=type=secret,id=GITHUB_TOKEN \
    /ctx/build_files/shared/build.sh

# Makes `/opt` writeable by default
# Needs to be here to make the main image build strict (no /opt there)
# This is for downstream images/stuff like k0s
RUN rm -rf /opt && ln -s /var/opt /opt

CMD ["/sbin/init"]

RUN bootc container lint
```

## File: `Justfile`
```
repo_organization := "ublue-os"
rechunker_image := "ghcr.io/ublue-os/legacy-rechunk:v1.0.1-x86_64@sha256:2627cbf92ca60ab7372070dcf93b40f457926f301509ffba47a04d6a9e1ddaf7"
common_image := "ghcr.io/projectbluefin/common:latest"
brew_image := "ghcr.io/ublue-os/brew:latest"
images := '(
    [bluefin]=bluefin
    [bluefin-dx]=bluefin-dx
)'
flavors := '(
    [main]=main
    [nvidia-open]=nvidia-open
)'
tags := '(
    [stable]=stable
    [latest]=latest
    [beta]=beta
)'
export SUDO_DISPLAY := if `if [ -n "${DISPLAY:-}" ] || [ -n "${WAYLAND_DISPLAY:-}" ]; then echo true; fi` == "true" { "true" } else { "false" }
export SUDOIF := if `id -u` == "0" { "" } else if SUDO_DISPLAY == "true" { "sudo --askpass" } else { "sudo" }
export PODMAN := if path_exists("/usr/bin/podman") == "true" { env("PODMAN", "/usr/bin/podman") } else if path_exists("/usr/bin/docker") == "true" { env("PODMAN", "docker") } else { env("PODMAN", "exit 1 ; ") }
export PULL_POLICY := if PODMAN =~ "docker" { "missing" } else { "newer" }
just := just_executable()

[private]
default:
    @{{ just }} --list

# Check Just Syntax
[group('Just')]
check:
    #!/usr/bin/bash
    find . -type f -name "*.just" | while read -r file; do
    	echo "Checking syntax: $file"
    	{{ just }} --unstable --fmt --check -f $file
    done
    echo "Checking syntax: Justfile"
    {{ just }} --unstable --fmt --check -f Justfile

# Fix Just Syntax
[group('Just')]
fix:
    #!/usr/bin/bash
    find . -type f -name "*.just" | while read -r file; do
    	echo "Checking syntax: $file"
    	{{ just }} --unstable --fmt -f $file
    done
    echo "Checking syntax: Justfile"
    {{ just }} --unstable --fmt -f Justfile || { exit 1; }

# Clean Repo
[group('Utility')]
clean:
    #!/usr/bin/bash
    set -eoux pipefail
    touch _build
    find *_build* -exec rm -rf {} \;
    rm -f previous.manifest.json
    rm -f changelog.md
    rm -f output.env

# Check if valid combo
[group('Utility')]
[private]
validate $image $tag $flavor:
    #!/usr/bin/bash
    set -eou pipefail
    declare -A images={{ images }}
    declare -A tags={{ tags }}
    declare -A flavors={{ flavors }}

    # Handle Stable Daily
    if [[ "${tag}" == "stable-daily" ]]; then
        tag="stable"
    fi

    checkimage="${images[${image}]-}"
    checktag="${tags[${tag}]-}"
    checkflavor="${flavors[${flavor}]-}"

    # Validity Checks
    if [[ -z "$checkimage" ]]; then
        echo "Invalid Image..."
        exit 1
    fi
    if [[ -z "$checktag" ]]; then
        echo "Invalid tag..."
        exit 1
    fi
    if [[ -z "$checkflavor" ]]; then
        echo "Invalid flavor..."
        exit 1
    fi

# Build Image
[group('Image')]
build $image="bluefin" $tag="latest" $flavor="main" rechunk="0" ghcr="0" pipeline="0" $kernel_pin="":
    #!/usr/bin/bash

    echo "::group:: Build Prep"
    set -eoux pipefail

    # Validate
    {{ just }} validate "${image}" "${tag}" "${flavor}"

    # Image Name
    image_name=$({{ just }} image_name {{ image }} {{ tag }} {{ flavor }})

    common_image_sha=$(yq -r '.images[] | select(.name == "common") | .digest' image-versions.yml)
    brew_image_sha=$(yq -r '.images[] | select(.name == "brew") | .digest' image-versions.yml)

    # Base Image
    base_image_name="silverblue"


    # AKMODS Flavor and Kernel Version
    if [[ "${flavor}" =~ hwe ]]; then
        akmods_flavor="bazzite"
    elif [[ "${tag}" =~ stable ]]; then
        akmods_flavor="coreos-stable"
    elif [[ "${tag}" =~ beta ]]; then
        akmods_flavor="main"
    else
        akmods_flavor="main"
    fi

    # Fedora Version
    if [[ {{ ghcr }} == "0" ]]; then
        rm -f /tmp/manifest.json
    fi
    fedora_version=$({{ just }} fedora_version '{{ image }}' '{{ tag }}' '{{ flavor }}' '{{ kernel_pin }}')

    # Verify Base Image with cosign
    {{ just }} verify-container "${base_image_name}-main:${fedora_version}"

    # Kernel Release/Pin
    if [[ -z "${kernel_pin:-}" ]]; then
        kernel_release=$(skopeo inspect --retry-times 3 docker://ghcr.io/ublue-os/akmods:"${akmods_flavor}"-"${fedora_version}" | jq -r '.Labels["ostree.linux"]')
    else
        kernel_release="${kernel_pin}"
    fi

    # Verify Containers with Cosign
    {{ just }} verify-container "akmods:${akmods_flavor}-${fedora_version}-${kernel_release}"
    if [[ "${akmods_flavor}" =~ coreos ]]; then
        {{ just }} verify-container "akmods-zfs:${akmods_flavor}-${fedora_version}-${kernel_release}"
    fi
    if [[ "${flavor}" =~ nvidia-open ]]; then
        {{ just }} verify-container "akmods-nvidia-open:${akmods_flavor}-${fedora_version}-${kernel_release}"
    fi

    {{ just }} verify-container "common:latest@${common_image_sha}" ghcr.io/projectbluefin https://raw.githubusercontent.com/projectbluefin/common/refs/heads/main/cosign.pub
    {{ just }} verify-container "brew:latest@${brew_image_sha}" ghcr.io/ublue-os https://raw.githubusercontent.com/ublue-os/brew/refs/heads/main/cosign.pub

    # Get Version
    if [[ "${tag}" =~ stable ]]; then
        ver="${fedora_version}.$(date +%Y%m%d)"
    else
        ver="${tag}-${fedora_version}.$(date +%Y%m%d)"
    fi
    skopeo list-tags docker://ghcr.io/{{ repo_organization }}/${image_name} > /tmp/repotags.json
    if [[ $(jq "any(.Tags[]; contains(\"$ver\"))" < /tmp/repotags.json) == "true" ]]; then
        POINT="1"
        while $(jq -e "any(.Tags[]; contains(\"$ver.$POINT\"))" < /tmp/repotags.json)
        do
            (( POINT++ ))
        done
    fi
    if [[ -n "${POINT:-}" ]]; then
        ver="${ver}.$POINT"
    fi

    # Build Arguments
    BUILD_ARGS=()
    # Target
    if [[ "${image}" =~ dx ]]; then
        BUILD_ARGS+=("--build-arg" "IMAGE_FLAVOR=dx")
        target="dx"
    fi
    BUILD_ARGS+=("--build-arg" "AKMODS_FLAVOR=${akmods_flavor}")
    BUILD_ARGS+=("--build-arg" "BASE_IMAGE_NAME=${base_image_name}")
    BUILD_ARGS+=("--build-arg" "COMMON_IMAGE={{ common_image }}")
    BUILD_ARGS+=("--build-arg" "COMMON_IMAGE_SHA=${common_image_sha}")
    BUILD_ARGS+=("--build-arg" "BREW_IMAGE={{ brew_image }}")
    BUILD_ARGS+=("--build-arg" "BREW_IMAGE_SHA=${brew_image_sha}")
    BUILD_ARGS+=("--build-arg" "FEDORA_MAJOR_VERSION=${fedora_version}")
    BUILD_ARGS+=("--build-arg" "IMAGE_NAME=${image_name}")
    BUILD_ARGS+=("--build-arg" "IMAGE_VENDOR={{ repo_organization }}")
    BUILD_ARGS+=("--build-arg" "KERNEL=${kernel_release}")
    BUILD_ARGS+=("--build-arg" "VERSION=${ver}")
    if [[ -z "$(git status -s)" ]]; then
        BUILD_ARGS+=("--build-arg" "SHA_HEAD_SHORT=$(git rev-parse --short HEAD)")
    fi
    BUILD_ARGS+=("--build-arg" "UBLUE_IMAGE_TAG=${tag}")
    if [[ "${PODMAN}" =~ docker && "${TERM}" == "dumb" ]]; then
        BUILD_ARGS+=("--progress" "plain")
    fi

    # Labels
    LABELS=()
    LABELS+=("--label" "org.opencontainers.image.title=${image_name}")
    LABELS+=("--label" "org.opencontainers.image.version=${ver}")
    LABELS+=("--label" "ostree.linux=${kernel_release}")
    LABELS+=("--label" "io.artifacthub.package.readme-url=https://raw.githubusercontent.com/ublue-os/bluefin/refs/heads/main/README.md")
    LABELS+=("--label" "io.artifacthub.package.logo-url=https://avatars.githubusercontent.com/u/120078124?s=200&v=4")
    LABELS+=("--label" "org.opencontainers.image.description=The next generation Linux workstation, designed for reliability, performance, and sustainability.")
    LABELS+=("--label" "containers.bootc=1")
    LABELS+=("--label" "org.opencontainers.image.created=$(date -u +%Y\-%m\-%d\T%H\:%M\:%S\Z)")
    LABELS+=("--label" "org.opencontainers.image.source=https://raw.githubusercontent.com/ublue-os/bluefin/refs/heads/main/Containerfile")
    LABELS+=("--label" "org.opencontainers.image.url=https://projectbluefin.io")
    LABELS+=("--label" "org.opencontainers.image.vendor={{ repo_organization }}")
    LABELS+=("--label" "io.artifacthub.package.deprecated=false")
    LABELS+=("--label" "io.artifacthub.package.keywords=bootc,bluefin,ublue,universal-blue")
    LABELS+=("--label" "io.artifacthub.package.maintainers=[{\"name\": \"castrojo\", \"email\": \"jorge.castro@gmail.com\"}]")

    echo "::endgroup::"
    echo "::group:: Build Container"

    # Build Image
    PODMAN_BUILD_ARGS=("${BUILD_ARGS[@]}" "${LABELS[@]}" --tag localhost/"${image_name}:${tag}" --file Containerfile)

    # Add GitHub token secret if available (for CI/CD)
    if [[ -n "${GITHUB_TOKEN:-}" ]]; then
        echo "Adding GitHub token as build secret"
        PODMAN_BUILD_ARGS+=(--secret "id=GITHUB_TOKEN,env=GITHUB_TOKEN")
    else
        echo "No GitHub token found - build may hit rate limit"
    fi

    ${PODMAN} build "${PODMAN_BUILD_ARGS[@]}" .
    echo "::endgroup::"

    # Rechunk
    if [[ "{{ rechunk }}" == "1" && "{{ ghcr }}" == "1" && "{{ pipeline }}" == "1" ]]; then
        ${SUDOIF} {{ just }} rechunk "${image}" "${tag}" "${flavor}" 1 1
    elif [[ "{{ rechunk }}" == "1" && "{{ ghcr }}" == "1" ]]; then
        ${SUDOIF} {{ just }} rechunk "${image}" "${tag}" "${flavor}" 1
    elif [[ "{{ rechunk }}" == "1" ]]; then
        ${SUDOIF} {{ just }} rechunk "${image}" "${tag}" "${flavor}"
    fi

# Build Image and Rechunk
[group('Image')]
build-rechunk image="bluefin" tag="latest" flavor="main" kernel_pin="":
    @{{ just }} build {{ image }} {{ tag }} {{ flavor }} 1 0 0 {{ kernel_pin }}

# Build Image with GHCR Flag
[group('Image')]
build-ghcr image="bluefin" tag="latest" flavor="main" kernel_pin="":
    #!/usr/bin/bash
    if [[ "${UID}" -gt "0" ]]; then
        echo "Must Run with sudo or as root..."
        exit 1
    fi
    {{ just }} build {{ image }} {{ tag }} {{ flavor }} 0 1 0 {{ kernel_pin }}

# Build Image for Pipeline:
[group('Image')]
build-pipeline image="bluefin" tag="latest" flavor="main" kernel_pin="":
    #!/usr/bin/bash
    ${SUDOIF} {{ just }} build {{ image }} {{ tag }} {{ flavor }} 1 1 1 {{ kernel_pin }}

# Rechunk Image
[group('Image')]
[private]
rechunk $image="bluefin" $tag="latest" $flavor="main" ghcr="0" pipeline="0":
    #!/usr/bin/bash

    echo "::group:: Rechunk Prep"
    set -eoux pipefail

    # Validate
    {{ just }} validate "${image}" "${tag}" "${flavor}"

    # Image Name
    image_name=$({{ just }} image_name {{ image }} {{ tag }} {{ flavor }})

    # Check if image is already built
    ID=$(${PODMAN} images --filter reference=localhost/"${image_name}":"${tag}" --format "'{{ '{{.ID}}' }}'")
    if [[ -z "$ID" ]]; then
        {{ just }} build "${image}" "${tag}" "${flavor}"
    fi

    # Load into Rootful Podman
    ID=$(${SUDOIF} ${PODMAN} images --filter reference=localhost/"${image_name}":"${tag}" --format "'{{ '{{.ID}}' }}'")
    if [[ -z "$ID" && ! ${PODMAN} =~ docker ]]; then
        COPYTMP=$(mktemp -p "${PWD}" -d -t podman_scp.XXXXXXXXXX)
        ${SUDOIF} TMPDIR=${COPYTMP} ${PODMAN} image scp ${UID}@localhost::localhost/"${image_name}":"${tag}" root@localhost::localhost/"${image_name}":"${tag}"
        rm -rf "${COPYTMP}"
    fi

    # Prep Container
    CREF=$(${SUDOIF} ${PODMAN} create localhost/"${image_name}":"${tag}" bash)
    OLD_IMAGE=$(${SUDOIF} ${PODMAN} inspect $CREF | jq -r '.[].Image')
    OUT_NAME="${image_name}_build"
    MOUNT=$(${SUDOIF} ${PODMAN} mount "${CREF}")

    # Fedora Version
    fedora_version=$(${SUDOIF} ${PODMAN} inspect $CREF | jq -r '.[].Config.Labels["ostree.linux"]' | grep -oP 'fc\K[0-9]+')

    # Label Version
    VERSION=$(${SUDOIF} ${PODMAN} inspect $CREF | jq -r '.[].Config.Labels["org.opencontainers.image.version"]')

    # Git SHA
    SHA="dedbeef"
    if [[ -z "$(git status -s)" ]]; then
        SHA=$(git rev-parse HEAD)
    fi

    # Rest of Labels
    LABELS="
        io.artifacthub.package.deprecated=false
        io.artifacthub.package.keywords=bootc,fedora,bluefin,ublue,universal-blue
        io.artifacthub.package.logo-url=https://avatars.githubusercontent.com/u/120078124?s=200&v=4
        io.artifacthub.package.maintainers=[{\"name\": \"castrojo\", \"email\": \"jorge.castro@gmail.com\"}]
        io.artifacthub.package.readme-url=https://raw.githubusercontent.com/ublue-os/bluefin/refs/heads/main/README.md
        org.opencontainers.image.created=$(date -u +%Y\-%m\-%d\T%H\:%M\:%S\Z)
        org.opencontainers.image.license=Apache-2.0
        org.opencontainers.image.source=https://raw.githubusercontent.com/ublue-os/bluefin/refs/heads/main/Containerfile
        org.opencontainers.image.title=${image_name}
        org.opencontainers.image.url=https://projectbluefin.io
        org.opencontainers.image.vendor={{ repo_organization }}
        ostree.linux=$(${SUDOIF} ${PODMAN} inspect $CREF | jq -r '.[].Config.Labels["ostree.linux"]')
        containers.bootc=1
    "

    # Cleanup Space during Github Action
    if [[ "{{ ghcr }}" == "1" ]]; then
        base_image_name=silverblue-main
        if [[ "${tag}" =~ stable ]]; then
            tag="stable-daily"
        fi
        ID=$(${SUDOIF} ${PODMAN} images --filter reference=ghcr.io/{{ repo_organization }}/"${base_image_name}":${fedora_version} --format "{{ '{{.ID}}' }}")
        if [[ -n "$ID" ]]; then
            ${PODMAN} rmi "$ID"
        fi
    fi

    # Rechunk Container
    rechunker="{{ rechunker_image }}"

    echo "::endgroup::"
    echo "::group:: Prune"

    # Run Rechunker's Prune
    ${SUDOIF} ${PODMAN} run --rm \
        --pull=${PULL_POLICY} \
        --security-opt label=disable \
        --volume "$MOUNT":/var/tree \
        --env TREE=/var/tree \
        --user 0:0 \
        "${rechunker}" \
        /sources/rechunk/1_prune.sh

    echo "::endgroup::"
    echo "::group:: Create ostree tree"

    # Run Rechunker's Create
    ${SUDOIF} ${PODMAN} run --rm \
        --security-opt label=disable \
        --volume "$MOUNT":/var/tree \
        --volume "cache_ostree:/var/ostree" \
        --env TREE=/var/tree \
        --env REPO=/var/ostree/repo \
        --env RESET_TIMESTAMP=1 \
        --user 0:0 \
        "${rechunker}" \
        /sources/rechunk/2_create.sh

    # Cleanup Temp Container Reference
    ${SUDOIF} ${PODMAN} unmount "$CREF"
    ${SUDOIF} ${PODMAN} rm "$CREF"
    ${SUDOIF} ${PODMAN} rmi "$OLD_IMAGE"

    echo "::endgroup::"
    echo "::group:: Rechunker"

    # Run Rechunker
    ${SUDOIF} ${PODMAN} run --rm \
        --pull=${PULL_POLICY} \
        --security-opt label=disable \
        --volume "$PWD:/workspace" \
        --volume "$PWD:/var/git" \
        --volume cache_ostree:/var/ostree \
        --env REPO=/var/ostree/repo \
        --env PREV_REF=ghcr.io/ublue-os/"${image_name}":"${tag}" \
        --env OUT_NAME="$OUT_NAME" \
        --env LABELS="${LABELS}" \
        --env "DESCRIPTION='An interpretation of the Ubuntu spirit built on Fedora technology'" \
        --env "VERSION=${VERSION}" \
        --env VERSION_FN=/workspace/version.txt \
        --env OUT_REF="oci:$OUT_NAME" \
        --env GIT_DIR="/var/git" \
        --env REVISION="$SHA" \
        --user 0:0 \
        "${rechunker}" \
        /sources/rechunk/3_chunk.sh

    # Fix Permissions of OCI
    ${SUDOIF} find ${OUT_NAME} -type d -exec chmod 0755 {} \; || true
    ${SUDOIF} find ${OUT_NAME}* -type f -exec chmod 0644 {} \; || true

    if [[ "${UID}" -gt "0" ]]; then
        ${SUDOIF} chown "${UID}:${GROUPS}" -R "${PWD}"
    elif [[ -n "${SUDO_UID:-}" ]]; then
        chown "${SUDO_UID}":"${SUDO_GID}" -R "${PWD}"
    fi

    # Remove cache_ostree
    ${SUDOIF} ${PODMAN} volume rm cache_ostree

    echo "::endgroup::"

    # Pipeline Checks
    if [[ {{ pipeline }} == "1" && -n "${SUDO_USER:-}" ]]; then
        sudo -u "${SUDO_USER}" {{ just }} load-rechunk "${image}" "${tag}" "${flavor}"
        sudo -u "${SUDO_USER}" {{ just }} secureboot "${image}" "${tag}" "${flavor}"
    fi

# Load OCI into Podman Store
[group('Image')]
load-rechunk image="bluefin" tag="latest" flavor="main":
    #!/usr/bin/bash
    set -eou pipefail

    # Validate
    {{ just }} validate {{ image }} {{ tag }} {{ flavor }}

    # Image Name
    image_name=$({{ just }} image_name {{ image }} {{ tag }} {{ flavor }})

    # Load Image
    OUT_NAME="${image_name}_build"
    IMAGE=$(${PODMAN} pull oci:"${PWD}"/"${OUT_NAME}")
    ${PODMAN} tag ${IMAGE} localhost/"${image_name}":{{ tag }}

    # Cleanup
    rm -rf "${OUT_NAME}*"
    rm -f previous.manifest.json

# Run Container
[group('Image')]
run $image="bluefin" $tag="latest" $flavor="main":
    #!/usr/bin/bash
    set -eoux pipefail

    # Validate
    {{ just }} validate "${image}" "${tag}" "${flavor}"

    # Image Name
    image_name=$({{ just }} image_name {{ image }} {{ tag }} {{ flavor }})

    # Check if image exists
    ID=$(${PODMAN} images --filter reference=localhost/"${image_name}":"${tag}" --format "'{{ '{{.ID}}' }}'")
    if [[ -z "$ID" ]]; then
        {{ just }} build "$image" "$tag" "$flavor"
    fi

    # Run Container
    ${PODMAN} run -it --rm localhost/"${image_name}":"${tag}" bash

# Test Changelogs
[group('Changelogs')]
changelogs branch="stable" handwritten="":
    #!/usr/bin/bash
    set -eou pipefail
    python3 ./.github/changelogs.py "{{ branch }}" ./output.env ./changelog.md --workdir . --handwritten "{{ handwritten }}"

# Verify Container with Cosign
[group('Utility')]
verify-container container="" registry="ghcr.io/ublue-os" key="":
    #!/usr/bin/bash
    set -eou pipefail

    # Get Cosign if Needed
    if [[ ! $(command -v cosign) ]]; then
        COSIGN_CONTAINER_ID=$(${SUDOIF} ${PODMAN} create cgr.dev/chainguard/cosign:latest bash)
        ${SUDOIF} ${PODMAN} cp "${COSIGN_CONTAINER_ID}":/usr/bin/cosign /usr/local/bin/cosign
        ${SUDOIF} ${PODMAN} rm -f "${COSIGN_CONTAINER_ID}"
    fi

    # Verify Cosign Image Signatures if needed
    if [[ -n "${COSIGN_CONTAINER_ID:-}" ]]; then
        if ! cosign verify --certificate-oidc-issuer=https://token.actions.githubusercontent.com --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main cgr.dev/chainguard/cosign >/dev/null; then
            echo "NOTICE: Failed to verify cosign image signatures."
            exit 1
        fi
    fi

    # Public Key for Container Verification
    key={{ key }}
    if [[ -z "${key:-}" ]]; then
        key="https://raw.githubusercontent.com/ublue-os/main/main/cosign.pub"
    fi

    # Verify Container using cosign public key
    if ! cosign verify --key "${key}" "{{ registry }}"/"{{ container }}" >/dev/null; then
        echo "NOTICE: Verification failed. Please ensure your public key is correct."
        exit 1
    fi

# Secureboot Check
[group('Utility')]
secureboot $image="bluefin" $tag="latest" $flavor="main":
    #!/usr/bin/bash
    set -eou pipefail

    # Validate
    {{ just }} validate "${image}" "${tag}" "${flavor}"

    # Image Name
    image_name=$({{ just }} image_name ${image} ${tag} ${flavor})

    # Get the vmlinuz to check
    kernel_release=$(${PODMAN} inspect "${image_name}":"${tag}" | jq -r '.[].Config.Labels["ostree.linux"]')
    TMP=$(${PODMAN} create "${image_name}":"${tag}" bash)
    ${PODMAN} cp "$TMP":/usr/lib/modules/"${kernel_release}"/vmlinuz /tmp/vmlinuz
    ${PODMAN} rm "$TMP"

    # Get the Public Certificates
    curl --retry 3 -Lo /tmp/kernel-sign.der https://github.com/ublue-os/akmods/raw/main/certs/public_key.der
    curl --retry 3 -Lo /tmp/akmods.der https://github.com/ublue-os/akmods/raw/main/certs/public_key_2.der
    openssl x509 -in /tmp/kernel-sign.der -out /tmp/kernel-sign.crt
    openssl x509 -in /tmp/akmods.der -out /tmp/akmods.crt

    # Make sure we have sbverify
    CMD="$(command -v sbverify)"
    if [[ -z "${CMD:-}" ]]; then
        temp_name="sbverify-${RANDOM}"
        ${PODMAN} run -dt \
            --entrypoint /bin/sh \
            --volume /tmp/vmlinuz:/tmp/vmlinuz:z \
            --volume /tmp/kernel-sign.crt:/tmp/kernel-sign.crt:z \
            --volume /tmp/akmods.crt:/tmp/akmods.crt:z \
            --name ${temp_name} \
            alpine:edge
        ${PODMAN} exec ${temp_name} apk add sbsigntool
        CMD="${PODMAN} exec ${temp_name} /usr/bin/sbverify"
    fi

    # Confirm that Signatures Are Good
    $CMD --list /tmp/vmlinuz
    returncode=0
    if ! $CMD --cert /tmp/kernel-sign.crt /tmp/vmlinuz || ! $CMD --cert /tmp/akmods.crt /tmp/vmlinuz; then
        echo "Secureboot Signature Failed...."
        returncode=1
    fi
    if [[ -n "${temp_name:-}" ]]; then
        ${PODMAN} rm -f "${temp_name}"
    fi
    exit "$returncode"

# Get Fedora Version of an image
[group('Utility')]
[private]
fedora_version image="bluefin" tag="latest" flavor="main" $kernel_pin="":
    #!/usr/bin/bash
    set -eou pipefail
    {{ just }} validate {{ image }} {{ tag }} {{ flavor }}
    if [[ ! -f /tmp/manifest.json ]]; then
        if [[ "{{ tag }}" =~ stable ]]; then
            # CoreOS does not uses cosign
            skopeo inspect --retry-times 3 docker://quay.io/fedora/fedora-coreos:stable > /tmp/manifest.json
        else
            skopeo inspect --retry-times 3 docker://ghcr.io/ublue-os/base-main:"{{ tag }}" > /tmp/manifest.json
        fi
    fi
    fedora_version=$(jq -r '.Labels["org.opencontainers.image.version"]' < /tmp/manifest.json | grep -oP '^[0-9]+')
    if [[ -n "${kernel_pin:-}" ]]; then
        fedora_version=$(echo "${kernel_pin}" | grep -oP 'fc\K[0-9]+')
    fi
    echo "${fedora_version}"

# Image Name
[group('Utility')]
[private]
image_name image="bluefin" tag="latest" flavor="main":
    #!/usr/bin/bash
    set -eou pipefail
    {{ just }} validate {{ image }} {{ tag }} {{ flavor }}
    if [[ "{{ flavor }}" =~ main ]]; then
        image_name={{ image }}
    else
        image_name="{{ image }}-{{ flavor }}"
    fi
    echo "${image_name}"

# Generate Tags
[group('Utility')]
generate-build-tags image="bluefin" tag="latest" flavor="main" kernel_pin="" ghcr="0" $version="" github_event="" github_number="":
    #!/usr/bin/bash
    set -eou pipefail

    TODAY="$(date +%A)"
    WEEKLY="Tuesday"
    if [[ {{ ghcr }} == "0" ]]; then
        rm -f /tmp/manifest.json
    fi
    FEDORA_VERSION="$({{ just }} fedora_version '{{ image }}' '{{ tag }}' '{{ flavor }}' '{{ kernel_pin }}')"
    DEFAULT_TAG=$({{ just }} generate-default-tag {{ tag }} {{ ghcr }})
    IMAGE_NAME=$({{ just }} image_name {{ image }} {{ tag }} {{ flavor }})
    # Use Build Version from Rechunk
    if [[ -z "${version:-}" ]]; then
        version="{{ tag }}-${FEDORA_VERSION}.$(date +%Y%m%d)"
    fi
    version=${version#{{ tag }}-}

    # Arrays for Tags
    BUILD_TAGS=()
    COMMIT_TAGS=()

    # Commit Tags
    github_number="{{ github_number }}"
    SHA_SHORT="$(git rev-parse --short HEAD)"
    if [[ "{{ ghcr }}" == "1" ]]; then
        COMMIT_TAGS+=(pr-${github_number:-}-{{ tag }}-${version})
        COMMIT_TAGS+=(${SHA_SHORT}-{{ tag }}-${version})
    fi

    # Convenience Tags
    if [[ "{{ tag }}" =~ stable ]]; then
        BUILD_TAGS+=("stable-daily" "${version}" "stable-daily-${version}" "stable-daily-${version:3}")
    else
        BUILD_TAGS+=("{{ tag }}" "{{ tag }}-${version}" "{{ tag }}-${version:3}")
    fi

    # Weekly Stable / Rebuild Stable on workflow_dispatch
    github_event="{{ github_event }}"
    if [[ "{{ tag }}" =~ "stable" && "${WEEKLY}" == "${TODAY}" && "${github_event}" =~ schedule ]]; then
        BUILD_TAGS+=("stable" "stable-${version}" "stable-${version:3}" "gts" "gts-${version}" "gts-${version:3}")
    elif [[ "{{ tag }}" =~ "stable" && "${github_event}" =~ workflow_dispatch|workflow_call ]]; then
        BUILD_TAGS+=("stable" "stable-${version}" "stable-${version:3}" "gts" "gts-${version}" "gts-${version:3}")
    elif [[ "{{ tag }}" =~ "stable" && "{{ ghcr }}" == "0" ]]; then
        BUILD_TAGS+=("stable" "stable-${version}" "stable-${version:3}" "gts" "gts-${version}" "gts-${version:3}")
    elif [[ ! "{{ tag }}" =~ stable|beta ]]; then
        BUILD_TAGS+=("${FEDORA_VERSION}" "${FEDORA_VERSION}-${version}" "${FEDORA_VERSION}-${version:3}")
    fi

    if [[ "${github_event}" == "pull_request" ]]; then
        alias_tags=("${COMMIT_TAGS[@]}")
    else
        alias_tags=("${BUILD_TAGS[@]}")
    fi

    echo "${alias_tags[*]}"

# Generate Default Tag
[group('Utility')]
generate-default-tag tag="latest" ghcr="0":
    #!/usr/bin/bash
    set -eou pipefail

    # Default Tag
    if [[ "{{ tag }}" =~ stable && "{{ ghcr }}" == "1" ]]; then
        DEFAULT_TAG="stable-daily"
    elif [[ "{{ tag }}" =~ stable && "{{ ghcr }}" == "0" ]]; then
        DEFAULT_TAG="stable"
    else
        DEFAULT_TAG="{{ tag }}"
    fi

    echo "${DEFAULT_TAG}"

# Tag Images
[group('Utility')]
tag-images image_name="" default_tag="" tags="":
    #!/usr/bin/bash
    set -eou pipefail

    # Get Image, and untag
    IMAGE=$(${PODMAN} inspect localhost/{{ image_name }}:{{ default_tag }} | jq -r .[].Id)
    ${PODMAN} untag localhost/{{ image_name }}:{{ default_tag }}

    # Tag Image
    for tag in {{ tags }}; do
        ${PODMAN} tag $IMAGE {{ image_name }}:${tag}
    done


    # Show Images
    ${PODMAN} images

# DNF CI package cache
[group('Utility')]
setup-cache $image="bluefin" $tag="latest" $ghcr="0" $github_event="0":
    #!/usr/bin/bash
    set -eou pipefail

    image_name=$({{ just }} image_name '{{ image }}')
    fedora_version=$({{ just }} fedora_version '{{ image }}' '{{ tag }}')

    ALLOW_CACHE_WRITE="false"

    BLESSED_IMAGE=bluefin-dx

    if [[ "${image_name}" == "${BLESSED_IMAGE}" ]] && \
       [[ "{{ ghcr }}" == "1" ]] && \
       [[ "${github_event}" == "workflow_dispatch" || "${github_event}" == "schedule" ]]; then
        ALLOW_CACHE_WRITE="true"
    fi

    CACHE_NAME="${BLESSED_IMAGE}-${fedora_version}"

    echo "${CACHE_NAME}" "${ALLOW_CACHE_WRITE}"

# Examples:
#   > just retag-nvidia-on-ghcr stable-daily stable-daily-41.20250126.3 0
#   > just retag-nvidia-on-ghcr latest latest-41.20250228.1 0
#
# working_tag: The tag of the most recent known good image (e.g., stable-daily-41.20250126.3)
# stream:      One of latest, stable-daily, or stable
# dry_run:     Only print the skopeo commands instead of running them
#
# First generate a PAT with package write access (https://github.com/settings/tokens)
# and set $GITHUB_USERNAME and $GITHUB_PAT environment variables

# Retag images on GHCR
[group('Admin')]
retag-nvidia-on-ghcr working_tag="" stream="" dry_run="1":
    #!/bin/bash
    set -euxo pipefail
    skopeo="echo === skopeo"
    if [[ "{{ dry_run }}" -ne 1 ]]; then
        echo "$GITHUB_PAT" | podman login -u $GITHUB_USERNAME --password-stdin ghcr.io
        skopeo="skopeo"
    fi
    for image in bluefin-nvidia-open bluefin-dx-nvidia-open; do
      $skopeo copy docker://ghcr.io/ublue-os/${image}:{{ working_tag }} docker://ghcr.io/ublue-os/${image}:{{ stream }}
    done
```

## File: `LICENSE`
```
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

## File: `README.md`
```markdown
# Bluefin
*Deinonychus antirrhopus*

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2503a44c1105456483517f793af75ee7)](https://app.codacy.com/gh/ublue-os/bluefin/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/ublue-os/bluefin/badge)](https://scorecard.dev/viewer/?uri=github.com/ublue-os/bluefin)[![GTS Images](https://github.com/ublue-os/bluefin/actions/workflows/build-image-gts.yml/badge.svg)](https://github.com/ublue-os/bluefin/actions/workflows/build-image-gts.yml)[![Stable Images](https://github.com/ublue-os/bluefin/actions/workflows/build-image-stable.yml/badge.svg)](https://github.com/ublue-os/bluefin/actions/workflows/build-image-stable.yml)[![Latest Images](https://github.com/ublue-os/bluefin/actions/workflows/build-image-latest-main.yml/badge.svg)](https://github.com/ublue-os/bluefin/actions/workflows/build-image-latest-main.yml)

[<img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/ublue-os/countme/main/badge-endpoints/bluefin.json&label=Bluefin&logo=data:image%2Fpng;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAdnJLH8AAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB%2BkHDxYrIEJpLs8AAAXQSURBVFjD7ZZrbFtnGcf%2F55z3XO1jJ7ZjO7c2Sd1bmnVNM5o2tIh2mgYf6IYYk5iAsolREAMJaRI3CZAmkCYkJk0UpKBpW7VVRR0S64o2NNY1nVibdkvWdk7WS2wnji%2BxHdvpOcfnfg6fQEOwSkiJ%2BJLf9%2Bd9fh%2Be93n%2BwDrrrPN%2FhlrrBjs7H4kM7OvfF44mDsf6kgfqRAyYrZW3i6cmvnNu5g86WavGI9u%2BzX%2F2C596SZDbvxQRWMo1W5idnQHXl0L3th1HFuOXZzGDp5m1EggbA0O7eq1nmfo8ZVXyWFnKI5XqQUuKwFGbkCNyKub3HFszgZqVXhrq3b0NvudUm3bS79kINdIF17DgwQXLC22Tpy7Pr4nA%2FWNPEK7Rv%2F319PO%2FjyV2jbu6Je%2FZIOyLGg1wKxVoQghEECBE2MKqDeHm2CPJ%2BHB8%2F5bR0WGfpr9JeDZOeGHJVJV3qrcyk1ud5Sc7E6GEJIhYau%2BDRhF8dOnK5B0FDg49ThZzy2ObH9j9XYbmUjRhZgPt4ZuU55amXjkHe8XwEju6tvfvH34sMbC5TZQk0FIIvmdDWa4gHIvD1nWYug61VkG4fB0hiYMR7Ydi2yjfyP3yEwUevu%2F7T3WPjf6gs6s7wPM8bB%2BAIKJFCBzTg0cBlOvArFdA0wxc1wANAoqmwXACwIvwHQueZUBr1BBKboBRyIF3W6CD7SABHlNv%2FO3R%2FxDYEnqo%2F96ffO14Isjvl2wbqqbAjSfh16qgbQuBaASaYcAmElzThG2boAkHQmhYpgUp2gGlXIQginAsEzTLgqEZUDQN13VAKAKP9qDVKrULL7%2B79d%2F2wKGxxw%2FsOvz5v0gsZLpewbKiICnRsOabkAUOK80qiFZByNCgtHfBlOMgHgOGMIAHEIaB12qBE3g0a1WwUhDNUh69Ayn4lAfLsGBRNkTiAGr16en8C%2FV%2FCXzu3qOH9o4MviaqBUlt%2BQiEg6jV6hBTG5Av5%2BHIAVxrMnAJDYuWQZVa6IYCz%2FPA8jY4QYShtSCxBIThYTsOGNdH3%2BatcD0bhqoie2sOvRt70CyXJ0pT5WcAgBlLPSrI3vaffvozqed7wgH26rUMBlOdmLyUtof7Ikwul7tQLjVemFpQzto8f5fPUBINAsBH87YGrWVgcSaDjs4OiJIEyqcAyke1WIVEXMiMDZ8PgmEoULaBWmYeMxezP5%2B4Mv4BADDtgR3S6N6O32xKyHFHbaLRbOkdvM3emC2fDHJG%2FczZpa%2B8Of3c6fncxYkOo%2Fe5Sr5%2BwYMd0xVtAPBBcSyUpoJYNAQxIAI%2BoN1uIrtQwkgY8CkCgVCwaBYsL2DuZhEs638xpG1qVfQP3yXdUfarG9rYVoyYuJatn9sS5dpW6s2reoD9xi9eftb%2F%2BIxcnHuxDuDVL3c%2BcfrU%2Bd%2F6ewYeCzoB%2Bliyt%2F2hGOdLlKHAtmzM3VyEKAdQzZfQ32uiYOgIiQJuhxK4e2QTPnjtLcCnbwAAE5UGC0M94lZVb509ebrxY8PW3i%2FowWfOnD%2Fmf9IXnZm%2FBAAoNKatUmXqzw%2BOHfxRTKR42lBx4fyHoEMByBIHDTTMhQXIroZioAODsofyrTzy2ao2XTx5BADIZOZEcTKDo%2F98%2FPoV5P%2FXLShYismprjy3qJy8XW0c4FtqiE6E5xdyyq%2B4kHP37m7%2BhzElh6wfQU1ptGyb%2Btmhe77Fnn1v3F6VWxAkqR2m7e2aTKt7BMnZa%2BrOpXJGPRrvYCjP5t%2B5q4v%2B3vKy5r3xev5EUqb%2B9NfpF3%2BdLb7vAcCq5IFszjo%2BvF04YqsrO7%2F%2B5OGhm3MLbsvwXg23i6%2BU5orpP16sDnEy2WjxZCZTcEofr10VgZ6dHRO65eu772k%2Fdv2jue7Lf79Cg2aFtra2DC8G3z6TPp4GkP5vtfRqCLx5%2FneuYVjpZIiM1GYXKFvlirpujy9kmstNw5DvVLtqkaywbJyI2I5XXNHJ6MFB8%2BrVxafemhlfRHY9eK9zZ%2F4BT9GkAVNsoqgAAAAASUVORK5CYII%3D">](https://github.com/ublue-os/bluefin)

[![LFX Active Contributors](https://insights.linuxfoundation.org/api/badge/active-contributors?project=ublue-os-bluefin&repos=https://github.com/ublue-os/bluefin)](https://insights.linuxfoundation.org/project/ublue-os-bluefin/repository/ublue-os-bluefin/security)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/ublue-os/bluefin-docs)

**Bluefin** is a cloud-native desktop operating system that reimagines the Linux desktop experience for modern computing environments.

For end users, it provides a system as reliable as a Chromebook with near-zero maintenance. For developers, it offers a kickass cloud-native developer workflow with integrated container tools, declarative system management, and seamless CI/CD integration. Check [Introduction to Bluefin](https://docs.projectbluefin.io/introduction/) for a feature walkthrough.

🌐 **[Try Bluefin](https://projectbluefin.io/#scene-picker)**

![image](https://github.com/user-attachments/assets/e7d2a0af-b011-459a-8ab7-c26d3ba50ae5)

## Mission

Bluefin's mission is to provide a robust, cloud-native desktop operating system that bridges the gap between consumer usability and enterprise-grade infrastructure practices. We aim to deliver:

- **Reliability**: Atomic updates ensuring system stability
- **Developer Experience**: Integrated cloud-native tooling and workflows, including Kubernetes and container support
- **Sustainability**: Reduced maintenance overhead for contributors by using the latest cloud native infrastructure tech

## Communications

### Community Channels

- **📰 [Announcements](https://blog.projectbluefin.io/)** - Official project blog and announcements
- **[Project Board](https://todo.projectbluefin.io)** - What we're working on
- **💬 [Discussions](https://community.projectbluefin.io/)** - Community forum (strongly recommended!)
- **📖 [Documentation](https://docs.projectbluefin.io/)** - Documentation and User Guides
- **🔧 [Contributing Guide](https://docs.projectbluefin.io/contributing)** - How to contribute to the project

## Getting Started

Visit [projectbluefin.io](https://projectbluefin.io/#scene-picker) to explore installation options and get started with Bluefin.

### Secure Boot

Secure Boot is supported by default on our systems, providing an additional layer of security. After the first installation, you will be prompted to enroll the secure boot key in the BIOS.

Enter the password `universalblue`
when prompted to enroll our key.

If this step is not completed during the initial setup, you can manually enroll the key by running the following command in the terminal:

`
ujust enroll-secure-boot-key
`

Secure boot is supported with our custom key. The pub key can be found in the root of the akmods repository [here](https://github.com/ublue-os/akmods/raw/main/certs/public_key.der).
If you'd like to enroll this key prior to installation or rebase, download the key and run the following:

```bash
sudo mokutil --timeout -1
sudo mokutil --import public_key.der
```

## Code of Conduct

This project follows the [Universal Blue Community Guidelines](https://docs.projectbluefin.io/contributing#community-guidelines). We are committed to providing a welcoming and inclusive environment for all contributors and users.

All participants in our community are expected to follow our code of conduct. Please report any violations to the project maintainers.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

### Third-Party Components

Bluefin incorporates and builds upon several open source projects:
- **Fedora Linux** - Base operating system foundation
- **GNOME Desktop Environment** - Desktop interface
- **Universal Blue** - Cloud Native desktop infrastructure
- **Various CNCF Projects** - Cloud-native tooling and containers

All incorporated components maintain their respective licenses and attributions.

## Repobeats

![Alt](https://repobeats.axiom.co/api/embed/40b85b252bf6ea25eb90539d1adcea013ccae69a.svg "Repobeats analytics image")

<!-- Copy-paste in your Readme.md file -->

<a href="https://next.ossinsight.io/widgets/official/compose-org-participants-growth?activity=new&period=past_90_days&owner_id=120078124&repo_ids=611397346" target="_blank" style="display: block" align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-org-participants-growth/thumbnail.png?activity=new&period=past_90_days&owner_id=120078124&repo_ids=611397346&image_size=4x7&color_scheme=dark" width="657" height="auto">
    <img alt="New trends of ublue-os" src="https://next.ossinsight.io/widgets/official/compose-org-participants-growth/thumbnail.png?activity=new&period=past_90_days&owner_id=120078124&repo_ids=611397346&image_size=4x7&color_scheme=light" width="657" height="auto">
  </picture>
</a>

<!-- Made with [OSS Insight](https://ossinsight.io/) -->

<!-- Copy-paste in your Readme.md file -->

<a href="https://next.ossinsight.io/widgets/official/compose-org-participants-growth?activity=active&period=past_90_days&owner_id=120078124&repo_ids=611397346" target="_blank" style="display: block" align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-org-participants-growth/thumbnail.png?activity=active&period=past_90_days&owner_id=120078124&repo_ids=611397346&image_size=4x7&color_scheme=dark" width="657" height="auto">
    <img alt="Active trends of ublue-os" src="https://next.ossinsight.io/widgets/official/compose-org-participants-growth/thumbnail.png?activity=active&period=past_90_days&owner_id=120078124&repo_ids=611397346&image_size=4x7&color_scheme=light" width="657" height="auto">
  </picture>
</a>


## Star History

<a href="https://star-history.com/#ublue-os/bluefin&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ublue-os/bluefin&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ublue-os/bluefin&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ublue-os/bluefin&type=Date" />
  </picture>
</a>
```

## File: `artifacthub-repo.yml`
```yaml
repositoryID: 1196b123-c8db-4a49-bae5-cd046daddafa
owners: # (optional, used to claim repository ownership)
  - name: Jorge Castro
    email: jorge.castro@gmail.com
#ignore: # (optional, packages that should not be indexed by Artifact Hub)
#  - name: package1
#  - name: package2 # Exact match
```

## File: `cosign.pub`
```
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHLRpBfPRYiMl9wb7s6fx47PzzNWu
3zyJgXhWEvxoOgwv9CpwjbvUwR9qHxNMWkJhuGE6cjDA2hpy1I6NbA+24Q==
-----END PUBLIC KEY-----
```

## File: `image-versions.yml`
```yaml
images:
  - name: silverblue-main
    image: ghcr.io/ublue-os/silverblue-main
    tag: latest
    digest: sha256:a5858d18db62fc69615002bacc719f506ddba130a3c78778d1b32b47bafedac5
  - name: common
    image: ghcr.io/projectbluefin/common
    tag: latest
    digest: sha256:a04a1e68ee0e4e77eee66b2c683e07a1a3de16510e0201154321fe338e7cc988
  - name: brew
    image: ghcr.io/ublue-os/brew
    tag: latest
    digest: sha256:230f2563e08195d8af284ce7ba258fe62557d2bab106162f4a7e9465d0d6e01a
```

## File: `build_files/base/00-image-info.sh`
```bash
#!/usr/bin/env bash

echo "::group:: ===$(basename "$0")==="

set -xeuo pipefail

IMAGE_PRETTY_NAME="Bluefin"
IMAGE_LIKE="fedora"
HOME_URL="https://projectbluefin.io"
DOCUMENTATION_URL="https://docs.projectbluefin.io"
SUPPORT_URL="https://github.com/ublue-os/bluefin/issues/"
BUG_SUPPORT_URL="https://github.com/ublue-os/bluefin/issues/"
CODE_NAME="Deinonychus"
VERSION="${VERSION:-00.00000000}"

IMAGE_INFO="/usr/share/ublue-os/image-info.json"
IMAGE_REF="ostree-image-signed:docker://ghcr.io/$IMAGE_VENDOR/$IMAGE_NAME"

# Image Flavor
image_flavor="main"
if [[ "${IMAGE_NAME}" =~ nvidia-open ]]; then
  image_flavor="nvidia-open"
fi

cat >$IMAGE_INFO <<EOF
{
  "image-name": "$IMAGE_NAME",
  "image-flavor": "$image_flavor",
  "image-vendor": "$IMAGE_VENDOR",
  "image-ref": "$IMAGE_REF",
  "image-tag":"$UBLUE_IMAGE_TAG",
  "base-image-name": "$BASE_IMAGE_NAME",
  "fedora-version": "$FEDORA_MAJOR_VERSION"
}
EOF

# OS Release File
sed -i "s|^VARIANT_ID=.*|VARIANT_ID=$IMAGE_NAME|" /usr/lib/os-release
sed -i "s|^PRETTY_NAME=.*|PRETTY_NAME=\"${IMAGE_PRETTY_NAME} (Version: ${VERSION})\"|" /usr/lib/os-release
sed -i "s|^NAME=.*|NAME=\"$IMAGE_PRETTY_NAME\"|" /usr/lib/os-release
sed -i "s|^HOME_URL=.*|HOME_URL=\"$HOME_URL\"|" /usr/lib/os-release
sed -i "s|^DOCUMENTATION_URL=.*|DOCUMENTATION_URL=\"$DOCUMENTATION_URL\"|" /usr/lib/os-release
sed -i "s|^SUPPORT_URL=.*|SUPPORT_URL=\"$SUPPORT_URL\"|" /usr/lib/os-release
sed -i "s|^BUG_REPORT_URL=.*|BUG_REPORT_URL=\"$BUG_SUPPORT_URL\"|" /usr/lib/os-release
sed -i "s|^CPE_NAME=\"cpe:/o:fedoraproject:fedora|CPE_NAME=\"cpe:/o:universal-blue:${IMAGE_PRETTY_NAME,}|" /usr/lib/os-release
sed -i "s|^DEFAULT_HOSTNAME=.*|DEFAULT_HOSTNAME=\"${IMAGE_PRETTY_NAME,}\"|" /usr/lib/os-release
sed -i "s|^ID=fedora|ID=${IMAGE_PRETTY_NAME,}\nID_LIKE=\"${IMAGE_LIKE}\"|" /usr/lib/os-release
sed -i "/^REDHAT_BUGZILLA_PRODUCT=/d; /^REDHAT_BUGZILLA_PRODUCT_VERSION=/d; /^REDHAT_SUPPORT_PRODUCT=/d; /^REDHAT_SUPPORT_PRODUCT_VERSION=/d" /usr/lib/os-release
sed -i "s|^VERSION_CODENAME=.*|VERSION_CODENAME=\"$CODE_NAME\"|" /usr/lib/os-release
sed -i "s|^VERSION=.*|VERSION=\"${VERSION} (${BASE_IMAGE_NAME^})\"|" /usr/lib/os-release
sed -i "s|^OSTREE_VERSION=.*|OSTREE_VERSION=\'${VERSION}\'|" /usr/lib/os-release

if [[ -n "${SHA_HEAD_SHORT:-}" ]]; then
  echo "BUILD_ID=\"$SHA_HEAD_SHORT\"" >>/usr/lib/os-release
fi

# Added in systemd 249.
# https://www.freedesktop.org/software/systemd/man/latest/os-release.html#IMAGE_ID=
echo "IMAGE_ID=\"${IMAGE_NAME}\"" >> /usr/lib/os-release
echo "IMAGE_VERSION=\"${VERSION}\"" >> /usr/lib/os-release

# Fix issues caused by ID no longer being fedora
sed -i "s|^EFIDIR=.*|EFIDIR=\"fedora\"|" /usr/sbin/grub2-switch-to-blscfg

# Weekly user count for fastfetch
ghcurl https://raw.githubusercontent.com/ublue-os/countme/main/badge-endpoints/bluefin.json | jq -r ".message" > /usr/share/ublue-os/fastfetch-user-count

# bazaar weekly downloads used for fastfetch
curl -X 'GET' \
'https://flathub.org/api/v2/stats/io.github.kolunmi.Bazaar?all=false&days=1' \
-H 'accept: application/json' | jq -r ".installs_last_7_days" | numfmt --to=si --round=nearest > /usr/share/ublue-os/bazaar-install-count

echo "::endgroup::"
```

## File: `build_files/base/03-install-kernel-akmods.sh`
```bash
#!/usr/bin/bash

echo "::group:: ===$(basename "$0")==="

set -eoux pipefail

# Beta Updates Testing Repo...
if [[ "${UBLUE_IMAGE_TAG}" == "beta" ]]; then
    dnf5 config-manager setopt updates-testing.enabled=1
fi

# Remove Existing Kernel
for pkg in kernel kernel-core kernel-modules kernel-modules-core kernel-modules-extra; do
    rpm --erase $pkg --nodeps
done

# Fetch Common AKMODS & Kernel RPMS
skopeo copy --retry-times 3 docker://ghcr.io/ublue-os/akmods:"${AKMODS_FLAVOR}"-"$(rpm -E %fedora)"-"${KERNEL}" dir:/tmp/akmods
AKMODS_TARGZ=$(jq -r '.layers[].digest' </tmp/akmods/manifest.json | cut -d : -f 2)
tar -xvzf /tmp/akmods/"$AKMODS_TARGZ" -C /tmp/
mv /tmp/rpms/* /tmp/akmods/
# NOTE: kernel-rpms should auto-extract into correct location

# Install Kernel
dnf5 -y install \
    /tmp/kernel-rpms/kernel-[0-9]*.rpm \
    /tmp/kernel-rpms/kernel-core-*.rpm \
    /tmp/kernel-rpms/kernel-modules-*.rpm

# TODO: Figure out why akmods cache is pulling in akmods/kernel-devel
dnf5 -y install \
    /tmp/kernel-rpms/kernel-devel-*.rpm

dnf5 versionlock add kernel kernel-devel kernel-devel-matched kernel-core kernel-modules kernel-modules-core kernel-modules-extra

# Everyone
# NOTE: we won't use dnf5 copr plugin for ublue-os/akmods until our upstream provides the COPR standard naming
sed -i 's@enabled=0@enabled=1@g' /etc/yum.repos.d/_copr_ublue-os-akmods.repo

# RPMFUSION Dependent AKMODS
if [[ "${UBLUE_IMAGE_TAG}" == "beta" ]]; then
    dnf5 -y install /tmp/akmods/kmods/*framework-laptop*.rpm || true
    dnf5 -y install \
        https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-"$(rpm -E %fedora)".noarch.rpm || true
    dnf5 -y install \
        https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-"$(rpm -E %fedora)".noarch.rpm || true
    dnf5 -y install \
        v4l2loopback /tmp/akmods/kmods/*v4l2loopback*.rpm || true
    dnf5 -y remove rpmfusion-free-release || true
    dnf5 -y remove rpmfusion-nonfree-release || true
else
    dnf5 -y install \
        /tmp/akmods/kmods/*framework-laptop*.rpm
    dnf5 -y install \
        https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-"$(rpm -E %fedora)".noarch.rpm \
        https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-"$(rpm -E %fedora)".noarch.rpm
    dnf5 -y install \
        v4l2loopback /tmp/akmods/kmods/*v4l2loopback*.rpm
    dnf5 -y remove rpmfusion-free-release rpmfusion-nonfree-release
fi

# Nvidia AKMODS
if [[ "${IMAGE_NAME}" =~ nvidia ]]; then
    # Fetch Nvidia RPMs
    skopeo copy --retry-times 3 docker://ghcr.io/ublue-os/akmods-nvidia-open:"${AKMODS_FLAVOR}"-"$(rpm -E %fedora)"-"${KERNEL}" dir:/tmp/akmods-rpms
    NVIDIA_TARGZ=$(jq -r '.layers[].digest' </tmp/akmods-rpms/manifest.json | cut -d : -f 2)
    tar -xvzf /tmp/akmods-rpms/"$NVIDIA_TARGZ" -C /tmp/
    mv /tmp/rpms/* /tmp/akmods-rpms/

    # Exclude the Golang Nvidia Container Toolkit in Fedora Repo
    # Exclude for non-beta.... doesn't appear to exist for F42 yet?
    if [[ "${UBLUE_IMAGE_TAG}" != "beta" ]]; then
        dnf5 config-manager setopt excludepkgs=golang-github-nvidia-container-toolkit
    else
        # Monkey patch right now...
        if ! grep -q negativo17 <(rpm -qi mesa-dri-drivers); then
            dnf5 -y swap --repo=updates-testing \
                mesa-dri-drivers mesa-dri-drivers
        fi
    fi

    # Install Nvidia RPMs
    IMAGE_NAME="${BASE_IMAGE_NAME}" AKMODNV_PATH="/tmp/akmods-rpms" MULTILIB=0 /tmp/akmods-rpms/ublue-os/nvidia-install.sh
    rm -f /usr/share/vulkan/icd.d/nouveau_icd.*.json
    ln -sf libnvidia-ml.so.1 /usr/lib64/libnvidia-ml.so
    tee /usr/lib/bootc/kargs.d/00-nvidia.toml <<EOF
kargs = ["rd.driver.blacklist=nouveau", "modprobe.blacklist=nouveau", "nvidia-drm.modeset=1", "initcall_blacklist=simpledrm_platform_driver_init"]
EOF
fi

# ZFS for stable
if [[ ${AKMODS_FLAVOR} =~ coreos ]]; then
    # Fetch ZFS RPMs
    skopeo copy --retry-times 3 docker://ghcr.io/ublue-os/akmods-zfs:"${AKMODS_FLAVOR}"-"$(rpm -E %fedora)"-"${KERNEL}" dir:/tmp/akmods-zfs
    ZFS_TARGZ=$(jq -r '.layers[].digest' </tmp/akmods-zfs/manifest.json | cut -d : -f 2)
    tar -xvzf /tmp/akmods-zfs/"$ZFS_TARGZ" -C /tmp/
    mv /tmp/rpms/* /tmp/akmods-zfs/

    # Declare ZFS RPMs
    ZFS_RPMS=(
        /tmp/akmods-zfs/kmods/zfs/kmod-zfs-"${KERNEL}"-*.rpm
        /tmp/akmods-zfs/kmods/zfs/libnvpair[0-9]-*.rpm
        /tmp/akmods-zfs/kmods/zfs/libuutil[0-9]-*.rpm
        /tmp/akmods-zfs/kmods/zfs/libzfs[0-9]-*.rpm
        /tmp/akmods-zfs/kmods/zfs/libzpool[0-9]-*.rpm
        /tmp/akmods-zfs/kmods/zfs/python3-pyzfs-*.rpm
        /tmp/akmods-zfs/kmods/zfs/zfs-*.rpm
        pv
    )

    # Install
    dnf5 -y install "${ZFS_RPMS[@]}"

    # Depmod and autoload
    depmod -a -v "${KERNEL}"
    echo "zfs" >/usr/lib/modules-load.d/zfs.conf
fi

echo "::endgroup::"
```

## File: `build_files/base/04-packages.sh`
```bash
#!/usr/bin/bash

echo "::group:: ===$(basename "$0")==="

set -ouex pipefail

# All DNF-related operations should be done here whenever possible

# shellcheck source=build_files/shared/copr-helpers.sh
source /ctx/build_files/shared/copr-helpers.sh

# NOTE:
# Packages are split into FEDORA_PACKAGES and COPR_PACKAGES to prevent
# malicious COPRs from injecting fake versions of Fedora packages.
# Fedora packages are installed first in bulk (safe).
# COPR packages are installed individually with isolated enablement.

# Base packages from Fedora repos - common to all versions
FEDORA_PACKAGES=(
    adcli
    adw-gtk3-theme
    adwaita-fonts-all
    autofs
    bash-color-prompt
    bcache-tools
    bootc
    borgbackup
    containerd
    cryfs
    davfs2
    ddcutil
    evtest
    fastfetch
    firewall-config
    fish
    foo2zjs
    fuse-encfs
    gcc
    git-credential-libsecret
    glow
    gnome-tweaks
    gum
    hplip
    ibus-mozc
    ifuse
    igt-gpu-tools
    input-remapper
    iwd
    jetbrains-mono-fonts-all
    just
    krb5-workstation
    libgda
    libgda-sqlite
    libimobiledevice
    libratbag-ratbagd
    libxcrypt-compat
    lm_sensors
    make
    mesa-libGLU
    mozc
    nautilus-gsconnect
    oddjob-mkhomedir
    opendyslexic-fonts
    openssh-askpass
    powerstat
    powertop
    printer-driver-brlaser
    pulseaudio-utils
    python3-pip
    python3-pygit2
    rclone
    restic
    samba
    samba-dcerpc
    samba-ldb-ldap-modules
    samba-winbind-clients
    samba-winbind-modules
    setools-console
    sssd-nfs-idmap
    switcheroo-control
    tmux
    usbip
    usbmuxd
    waypipe
    wireguard-tools
    wl-clipboard
    xdg-terminal-exec
    xprop
    zenity
    zsh
)

# Version-specific Fedora package additions
case "$FEDORA_MAJOR_VERSION" in
    42)
        FEDORA_PACKAGES+=(
            evolution-ews-core
            uld
        )
        ;;
    43)
        FEDORA_PACKAGES+=(
            evolution-ews-core
            gnupg2-scdaemon
        )
        ;;
esac

# Install all Fedora packages (bulk - safe from COPR injection)
echo "Installing ${#FEDORA_PACKAGES[@]} packages from Fedora repos..."
dnf -y install "${FEDORA_PACKAGES[@]}"

dnf config-manager addrepo --from-repofile=https://pkgs.tailscale.com/stable/fedora/tailscale.repo
dnf config-manager setopt tailscale-stable.enabled=0
dnf -y install --enablerepo='tailscale-stable' tailscale

# From che/nerd-fonts
copr_install_isolated "che/nerd-fonts" "nerd-fonts"

# From ublue-os/packages
copr_install_isolated "ublue-os/packages" "uupd"

# Version-specific COPR packages
# case "$FEDORA_MAJOR_VERSION" in
#    42)
        # bazaar and uupd from ublue-os/packages
        # copr_install_isolated "ublue-os/packages" "bazaar" "uupd"
        # ;;
    # 43)
        # bazaar from ublue-os/packages
        # copr_install_isolated "ublue-os/packages" "bazaar"
        # ;;
# esac

# Packages to exclude - common to all versions
EXCLUDED_PACKAGES=(
    fedora-bookmarks
    fedora-chromium-config
    fedora-chromium-config-gnome
    firefox
    firefox-langpacks
    gnome-extensions-app
    gnome-shell-extension-background-logo
    gnome-software-rpm-ostree
    gnome-terminal-nautilus
    podman-docker
    yelp
)

# Version-specific package exclusions
case "$FEDORA_MAJOR_VERSION" in
    42)
        EXCLUDED_PACKAGES+=(gnome-software cosign)
        ;;
    43)
        EXCLUDED_PACKAGES+=(gnome-software cosign)
        ;;
esac

# Remove excluded packages if they are installed
if [[ "${#EXCLUDED_PACKAGES[@]}" -gt 0 ]]; then
    readarray -t INSTALLED_EXCLUDED < <(rpm -qa --queryformat='%{NAME}\n' "${EXCLUDED_PACKAGES[@]}" 2>/dev/null || true)
    if [[ "${#INSTALLED_EXCLUDED[@]}" -gt 0 ]]; then
        dnf -y remove "${INSTALLED_EXCLUDED[@]}"
    else
        echo "No excluded packages found to remove."
    fi
fi

# Fix for ID in fwupd
dnf -y copr enable ublue-os/staging
dnf -y copr disable ublue-os/staging
dnf -y swap \
    --repo=copr:copr.fedorainfracloud.org:ublue-os:staging \
    fwupd fwupd

# TODO: remove me on next flatpak release when preinstall landed in Fedora
if [[ "$(rpm -E %fedora)" -ge "42" ]]; then
  dnf -y copr enable ublue-os/flatpak-test
  dnf -y copr disable ublue-os/flatpak-test
  dnf -y --repo=copr:copr.fedorainfracloud.org:ublue-os:flatpak-test swap flatpak flatpak
  dnf -y --repo=copr:copr.fedorainfracloud.org:ublue-os:flatpak-test swap flatpak-libs flatpak-libs
  dnf -y --repo=copr:copr.fedorainfracloud.org:ublue-os:flatpak-test swap flatpak-session-helper flatpak-session-helper
  dnf -y --repo=copr:copr.fedorainfracloud.org:ublue-os:flatpak-test install flatpak-debuginfo flatpak-libs-debuginfo flatpak-session-helper-debuginfo
fi

## Pins and Overrides
## Use this section to pin packages in order to avoid regressions
# Remember to leave a note with rationale/link to issue for each pin!
#
# Example:
#if [ "$FEDORA_MAJOR_VERSION" -eq "41" ]; then
#    Workaround pkcs11-provider regression, see issue #1943
#    rpm-ostree override replace https://bodhi.fedoraproject.org/updates/FEDORA-2024-dd2e9fb225
#fi

echo "::endgroup::"
```

## File: `build_files/base/05-override-install.sh`
```bash
#!/usr/bin/bash

echo "::group:: ===$(basename "$0")==="

set -eoux pipefail

# We do not need anything here at all
rm -rf /usr/src
rm -rf /usr/share/doc
# Remove kernel-devel from rpmdb because all package files are removed from /usr/src
rpm --erase --nodeps kernel-devel

mkdir -p /usr/share/doc/bluefin
# Offline Bluefin documentation
ghcurl "https://github.com/ublue-os/bluefin-docs/releases/download/0.1/bluefin.pdf" --retry 3 -o /tmp/bluefin.pdf
install -Dm0644 -t /usr/share/doc/bluefin/ /tmp/bluefin.pdf

# Starship Shell Prompt
ghcurl "https://github.com/starship/starship/releases/latest/download/starship-x86_64-unknown-linux-gnu.tar.gz" --retry 3 -o /tmp/starship.tar.gz
tar -xzf /tmp/starship.tar.gz -C /tmp
install -c -m 0755 /tmp/starship /usr/bin

# Automatic wallpaper changing by month
HARDCODED_RPM_MONTH="12"
sed -i "/picture-uri/ s/${HARDCODED_RPM_MONTH}/$(date +%m)/" "/usr/share/glib-2.0/schemas/zz0-bluefin-modifications.gschema.override"
rm /usr/share/glib-2.0/schemas/gschemas.compiled
glib-compile-schemas /usr/share/glib-2.0/schemas

# Required for bluefin faces to work without conflicting with a ton of packages
rm -f /usr/share/pixmaps/faces/* || echo "Expected directory deletion to fail"
mv /usr/share/pixmaps/faces/bluefin/* /usr/share/pixmaps/faces
rm -rf /usr/share/pixmaps/faces/bluefin

# Remove desktop entries
if [[ -f /usr/share/applications/gnome-system-monitor.desktop ]]; then
    sed -i 's@\[Desktop Entry\]@\[Desktop Entry\]\nHidden=true@g' /usr/share/applications/gnome-system-monitor.desktop
fi
if [[ -f /usr/share/applications/org.gnome.SystemMonitor.desktop ]]; then
    sed -i 's@\[Desktop Entry\]@\[Desktop Entry\]\nHidden=true@g' /usr/share/applications/org.gnome.SystemMonitor.desktop
fi

# Add Mutter experimental-features
if [[ "${IMAGE_NAME}" =~ nvidia ]]; then
    sed -i "/experimental-features/ s/\]/, 'kms-modifiers'&/" /usr/share/glib-2.0/schemas/zz0-bluefin-modifications.gschema.override
    echo "Compiling gschema to include bluefin setting overrides"
    glib-compile-schemas /usr/share/glib-2.0/schemas
fi

echo "::endgroup::"
```

## File: `build_files/base/17-cleanup.sh`
```bash
#!/usr/bin/bash

echo "::group:: ===$(basename "$0")==="

set -eoux pipefail

# Prevent Distrobox containers from being updated via the background service
sed -i 's|uupd|& --disable-module-distrobox|' /usr/lib/systemd/system/uupd.service

# Setup Systemd
# systemctl --global enable bazaar.service
systemctl --global enable podman-auto-update.timer
systemctl --global enable ublue-user-setup.service
systemctl enable brew-setup.service
systemctl enable dconf-update.service
systemctl enable flatpak-nuke-fedora.service
systemctl enable input-remapper.service
systemctl enable rpm-ostree-countme.service
systemctl enable tailscaled.service
systemctl enable ublue-system-setup.service

# run flatpak preinstall once at startup
if [[ "$(rpm -E %fedora)" -ge "42" ]]; then
  systemctl enable flatpak-preinstall.service
fi

# Updater
systemctl enable uupd.timer

#disable the old rpm-ostreed-automatic.timer
systemctl disable rpm-ostreed-automatic.timer

# Hide Desktop Files. Hidden removes mime associations
for file in fish htop nvtop; do
    if [[ -f "/usr/share/applications/$file.desktop" ]]; then
        sed -i 's@\[Desktop Entry\]@\[Desktop Entry\]\nHidden=true@g' /usr/share/applications/"$file".desktop
    fi
done

#Add the Flathub Flatpak remote and remove the Fedora Flatpak remote
flatpak remote-add --system --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
systemctl disable flatpak-add-fedora-repos.service

# NOTE: With isolated COPR installation, most repos are never enabled globally.
# We only need to clean up repos that were enabled during the build process.

# Disable third-party repos
for repo in negativo17-fedora-multimedia tailscale fedora-cisco-openh264; do
    if [[ -f "/etc/yum.repos.d/${repo}.repo" ]]; then
        sed -i 's@enabled=1@enabled=0@g' "/etc/yum.repos.d/${repo}.repo"
    fi
done

# Disable all COPR repos (should already be disabled by helpers, but ensure)
for i in /etc/yum.repos.d/_copr:*.repo; do
    if [[ -f "$i" ]]; then
        sed -i 's@enabled=1@enabled=0@g' "$i"
    fi
done

# NOTE: we won't use dnf5 copr plugin for ublue-os/akmods until our upstream provides the COPR standard naming
if [[ -f "/etc/yum.repos.d/_copr_ublue-os-akmods.repo" ]]; then
    sed -i 's@enabled=1@enabled=0@g' /etc/yum.repos.d/_copr_ublue-os-akmods.repo
fi

# Disable RPM Fusion repos
for i in /etc/yum.repos.d/rpmfusion-*.repo; do
    if [[ -f "$i" ]]; then
        sed -i 's@enabled=1@enabled=0@g' "$i"
    fi
done

# Disable fedora-coreos-pool if it exists
if [ -f /etc/yum.repos.d/fedora-coreos-pool.repo ]; then
    sed -i 's@enabled=1@enabled=0@g' /etc/yum.repos.d/fedora-coreos-pool.repo
fi

echo "::endgroup::"
```

## File: `build_files/base/18-workarounds.sh`
```bash
#!/usr/bin/bash

echo "::group:: ===$(basename "$0")==="

set -eoux pipefail

# Current bluefin systems have the bling.sh and bling.fish in their default locations
mkdir -p /usr/share/ublue-os/bluefin-cli
cp /usr/share/ublue-os/bling/* /usr/share/ublue-os/bluefin-cli

# Try removing just docs (is it actually promblematic?)
rm -rf /usr/share/doc/just/README.*.md

echo "::endgroup::"
```

## File: `build_files/base/19-initramfs.sh`
```bash
#!/usr/bin/bash

echo "::group:: ===$(basename "$0")==="

set -oue pipefail

KERNEL_SUFFIX=""
QUALIFIED_KERNEL="$(rpm -qa | grep -P 'kernel-(|'"$KERNEL_SUFFIX"'-)(\d+\.\d+\.\d+)' | sed -E 's/kernel-(|'"$KERNEL_SUFFIX"'-)//')"
export DRACUT_NO_XATTR=1
/usr/bin/dracut --no-hostonly --kver "$QUALIFIED_KERNEL" --reproducible -v --add ostree -f "/lib/modules/$QUALIFIED_KERNEL/initramfs.img"
chmod 0600 "/lib/modules/$QUALIFIED_KERNEL/initramfs.img"

echo "::endgroup::"
```

## File: `build_files/base/20-tests.sh`
```bash
#!/usr/bin/bash

echo "::group:: ===$(basename "$0")==="

set -eoux pipefail

# We need to have the ublue-os signing keys on the image!
# Published images without these keys won't be able to pull ghcr.io/ublue-os/*
# and can therefore not update!
# https://github.com/ublue-os/main/blob/963609eaf01f7c2bb1a76821fe6d0ec269d2df25/build_files/install.sh#L56
# https://github.com/ublue-os/packages/tree/1f77c7e7faa9ebad120609a10d79e0412376c3b7/packages/ublue-os-signing/src

KEY1=$(jq -r '.transports.docker."ghcr.io/ublue-os"[0].keyPaths[0]' /etc/containers/policy.json)
BACKUP_KEY=$(jq -r '.transports.docker."ghcr.io/ublue-os"[0].keyPaths[1]' /etc/containers/policy.json)
KEY1_SHA256="af78ecfda6eb21c35195af3739341715e9cfc3f2f5911dd9c10b0670547bf6e8"
BACKUP_KEY_SHA256="b723467015ba562d40b4645c98c51c65d8254bb59444f6e9962debcfe2315da0"

echo "${KEY1_SHA256}  ${KEY1}" | sha256sum -c -
echo "${BACKUP_KEY_SHA256}  ${BACKUP_KEY}" | sha256sum -c -

for i in bin/ujust share/ublue-os/just/{00-entry.just,apps.just,default.just,system.just,update.just,} ; do
   stat /usr/$i
done

test -f /usr/share/ublue-os/homebrew/fonts.Brewfile

# If this file is not on the image bazaar will automatically be removed from users systems :(
# See: https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-preinstall
test -f /usr/share/flatpak/preinstall.d/bazaar.preinstall

# Basic smoke test to check if the flatpak version is from our copr
flatpak preinstall --help

# Make sure this garbage never makes it to an image
test -f /usr/lib/systemd/system/flatpak-add-fedora-repos.service && false

IMPORTANT_PACKAGES=(
    distrobox
    fish
    flatpak
    mutter
    pipewire
    gnome-shell
    ptyxis
    gdm
    systemd
    tailscale
    uupd
    wireplumber
    zsh
)

for package in "${IMPORTANT_PACKAGES[@]}"; do
    rpm -q "${package}" >/dev/null || { echo "Missing package: ${package}... Exiting"; exit 1 ; }
done

# these packages are supposed to be removed
# and are considered footguns
UNWANTED_PACKAGES=(
    fedora-logos
    firefox
    gnome-software
    gnome-software-rpm-ostree
    podman-docker
)

for package in "${UNWANTED_PACKAGES[@]}"; do
    if rpm -q "${package}" >/dev/null 2>&1; then
        echo "Unwanted package found: ${package}... Exiting"; exit 1
    fi
done

if [[ "${IMAGE_NAME}" =~ nvidia ]]; then
  NV_PACKAGES=(
      libnvidia-container-tools
      kmod-nvidia
      nvidia-driver-cuda
)
  for package in "${NV_PACKAGES[@]}"; do
      rpm -q "${package}" >/dev/null || { echo "Missing NVIDIA package: ${package}... Exiting"; exit 1 ; }
  done
fi

IMPORTANT_UNITS=(
    rpm-ostree-countme.timer
    tailscaled.service
    ublue-system-setup.service
    uupd.timer
  )

for unit in "${IMPORTANT_UNITS[@]}"; do
    if ! systemctl is-enabled "$unit" 2>/dev/null | grep -q "^enabled$"; then
        echo "${unit} is not enabled"
        exit 1
    fi
done

echo "::endgroup::"
```

## File: `build_files/dx/00-dx.sh`
```bash
#!/usr/bin/bash

echo "::group:: ===$(basename "$0")==="

set -ouex pipefail

# Load secure COPR helpers
# shellcheck source=build_files/shared/copr-helpers.sh
source /ctx/build_files/shared/copr-helpers.sh

# DX packages from Fedora repos - common to all versions
FEDORA_PACKAGES=(
    android-tools
    bcc
    bpftop
    bpftrace
    cascadia-code-fonts
    cockpit-bridge
    cockpit-machines
    cockpit-networkmanager
    cockpit-ostree
    cockpit-podman
    cockpit-selinux
    cockpit-storaged
    cockpit-system
    dbus-x11
    edk2-ovmf
    flatpak-builder
    genisoimage
    git-subtree
    git-svn
    iotop
    libvirt
    libvirt-nss
    nicstat
    numactl
    osbuild-selinux
    p7zip
    p7zip-plugins
    podman-compose
    podman-machine
    podman-tui
    qemu
    qemu-char-spice
    qemu-device-display-virtio-gpu
    qemu-device-display-virtio-vga
    qemu-device-usb-redirect
    qemu-img
    qemu-system-x86-core
    qemu-user-binfmt
    qemu-user-static
    sysprof
    incus
    incus-agent
    lxc
    tiptop
    trace-cmd
    udica
    util-linux-script
    virt-manager
    virt-v2v
    virt-viewer
    ydotool
)

echo "Installing ${#FEDORA_PACKAGES[@]} DX packages from Fedora repos..."
dnf5 -y install "${FEDORA_PACKAGES[@]}"

# rocm doesn't work well on nvidia
if [[ ! "${IMAGE_NAME}" =~ nvidia ]]; then
  dnf install -y \
    rocm-hip \
    rocm-opencl \
    rocm-smi
fi

dnf config-manager addrepo --from-repofile=https://download.docker.com/linux/fedora/docker-ce.repo
sed -i "s/enabled=.*/enabled=0/g" /etc/yum.repos.d/docker-ce.repo
dnf -y install --enablerepo=docker-ce-stable \
    containerd.io \
    docker-buildx-plugin \
    docker-ce \
    docker-ce-cli \
    docker-compose-plugin \
    docker-model-plugin

tee /etc/yum.repos.d/vscode.repo <<'EOF'
[code]
name=Visual Studio Code
baseurl=https://packages.microsoft.com/yumrepos/vscode
enabled=1
gpgcheck=1
gpgkey=https://packages.microsoft.com/keys/microsoft.asc
EOF
sed -i "s/enabled=.*/enabled=0/g" /etc/yum.repos.d/vscode.repo
dnf -y install --enablerepo=code \
    code


# DX packages to exclude - common to all versions
EXCLUDED_PACKAGES=()

# Version-specific package exclusions for DX
case "$FEDORA_MAJOR_VERSION" in
    43)
        EXCLUDED_PACKAGES+=(mozilla-fira-mono-fonts)
        ;;
esac

# Remove excluded packages if they are installed
if [[ "${#EXCLUDED_PACKAGES[@]}" -gt 0 ]]; then
    readarray -t INSTALLED_EXCLUDED < <(rpm -qa --queryformat='%{NAME}\n' "${EXCLUDED_PACKAGES[@]}" 2>/dev/null || true)
    if [[ "${#INSTALLED_EXCLUDED[@]}" -gt 0 ]]; then
        dnf5 -y remove "${INSTALLED_EXCLUDED[@]}"
    else
        echo "No excluded packages found to remove."
    fi
fi

systemctl enable docker.socket
systemctl enable podman.socket
systemctl enable swtpm-workaround.service
systemctl enable libvirt-workaround.service
systemctl enable bluefin-dx-groups.service

sed -i 's@enabled=1@enabled=0@g' /etc/yum.repos.d/fedora-cisco-openh264.repo

# NOTE: we won't use dnf5 copr plugin for ublue-os/akmods until our upstream provides the COPR standard naming
sed -i 's@enabled=1@enabled=0@g' /etc/yum.repos.d/_copr_ublue-os-akmods.repo

# Disable RPM Fusion repos
for i in /etc/yum.repos.d/rpmfusion-*.repo; do
    if [[ -f "$i" ]]; then
        sed -i 's@enabled=1@enabled=0@g' "$i"
    fi
done

echo "::endgroup::"
```

## File: `build_files/dx/01-tests-dx.sh`
```bash
#!/usr/bin/bash

echo "::group:: ===$(basename "$0")==="

set -eoux pipefail

IMPORTANT_PACKAGES_DX=(
    code
    containerd.io
    docker-ce
    docker-buildx-plugin
    docker-compose-plugin
    flatpak-builder
    libvirt
    qemu
)

for package in "${IMPORTANT_PACKAGES_DX[@]}"; do
    rpm -q "${package}" >/dev/null || { echo "Missing package: ${package}... Exiting"; exit 1 ; }
done

IMPORTANT_UNITS=(
    docker.socket
    podman.socket
)

for unit in "${IMPORTANT_UNITS[@]}"; do
    if ! systemctl is-enabled "$unit" 2>/dev/null | grep -q "^enabled$"; then
        echo "${unit} is not enabled"
        exit 1
    fi
done

echo "::endgroup::"
```

## File: `build_files/shared/build-dx.sh`
```bash
#!/usr/bin/bash

set -xeou pipefail

echo "::group:: Copy Files"

# Copy Files to Image
rsync -rvK /ctx/system_files/dx/ /

mkdir -p /tmp/scripts/helpers
install -Dm0755 /ctx/build_files/shared/utils/ghcurl /tmp/scripts/helpers/ghcurl
export PATH="/tmp/scripts/helpers:$PATH"

echo "::endgroup::"

# Apply IP Forwarding before installing Docker to prevent messing with LXC networking
sysctl -p

# Load iptable_nat module for docker-in-docker.
# See:
#   - https://github.com/ublue-os/bluefin/issues/2365
#   - https://github.com/devcontainers/features/issues/1235
mkdir -p /etc/modules-load.d
tee /etc/modules-load.d/ip_tables.conf <<EOF
iptable_nat
EOF

# Install Packages and set up DX
/ctx/build_files/dx/00-dx.sh

# Validate all repos are disabled before committing
/ctx/build_files/shared/validate-repos.sh

# Clean Up
echo "::group:: Cleanup"
/ctx/build_files/shared/clean-stage.sh

echo "::endgroup::"

# dx specific tests
/ctx/build_files/dx/01-tests-dx.sh
```

## File: `build_files/shared/build-gnome-extensions.sh`
```bash
#!/usr/bin/bash

set -eoux pipefail

echo "::group:: ===$(basename "$0")==="

# Install tooling
dnf5 -y install glib2-devel meson sassc cmake dbus-devel

# Build Extensions

# AppIndicator Support
glib-compile-schemas --strict /usr/share/gnome-shell/extensions/appindicatorsupport@rgcjonas.gmail.com/schemas

# Bazaar Companion
mv /usr/share/gnome-shell/extensions/tmp/bazaar-integration@kolunmi.github.io/src/ /usr/share/gnome-shell/extensions/bazaar-integration@kolunmi.github.io/

# Blur My Shell
make -C /usr/share/gnome-shell/extensions/blur-my-shell@aunetx
unzip -o /usr/share/gnome-shell/extensions/blur-my-shell@aunetx/build/blur-my-shell@aunetx.shell-extension.zip -d /usr/share/gnome-shell/extensions/blur-my-shell@aunetx
glib-compile-schemas --strict /usr/share/gnome-shell/extensions/blur-my-shell@aunetx/schemas
rm -rf /usr/share/gnome-shell/extensions/blur-my-shell@aunetx/build

# Caffeine
# The Caffeine extension is built/packaged into a temporary subdirectory (tmp/caffeine/caffeine@patapon.info).
# Unlike other extensions, it must be moved to the standard extensions directory so GNOME Shell can detect it.
mv /usr/share/gnome-shell/extensions/tmp/caffeine/caffeine@patapon.info /usr/share/gnome-shell/extensions/caffeine@patapon.info
glib-compile-schemas --strict /usr/share/gnome-shell/extensions/caffeine@patapon.info/schemas

# Dash to Dock
make -C /usr/share/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com
glib-compile-schemas --strict /usr/share/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com/schemas

# GSConnect (commented out until G49 support)
meson setup --prefix=/usr /usr/share/gnome-shell/extensions/gsconnect@andyholmes.github.io /usr/share/gnome-shell/extensions/gsconnect@andyholmes.github.io/_build
meson install -C /usr/share/gnome-shell/extensions/gsconnect@andyholmes.github.io/_build --skip-subprojects
# GSConnect installs schemas to /usr/share/glib-2.0/schemas and meson compiles them automatically

# Logo Menu
# xdg-terminal-exec is required for this extension as it opens up terminals using that script
install -Dpm0755 -t /usr/bin /usr/share/gnome-shell/extensions/logomenu@aryan_k/distroshelf-helper
install -Dpm0755 -t /usr/bin /usr/share/gnome-shell/extensions/logomenu@aryan_k/missioncenter-helper
glib-compile-schemas --strict /usr/share/gnome-shell/extensions/logomenu@aryan_k/schemas

# Search Light
glib-compile-schemas --strict /usr/share/gnome-shell/extensions/search-light@icedman.github.com/schemas

rm /usr/share/glib-2.0/schemas/gschemas.compiled
glib-compile-schemas /usr/share/glib-2.0/schemas

# Cleanup
dnf5 -y remove glib2-devel meson sassc cmake dbus-devel
rm -rf /usr/share/gnome-shell/extensions/tmp

echo "::endgroup::"
```

## File: `build_files/shared/build.sh`
```bash
#!/usr/bin/bash

set -eoux pipefail

echo "::group:: Copy Files"

# We need to remove this package here because lots of files we add from `projectbluefin/common` override the rpm files and they also go away when you do `dnf remove`
dnf remove -y ublue-os-luks ublue-os-just ublue-os-udev-rules ublue-os-signing ublue-os-update-services

# Keep *-logos in RPM DB for downstream package installations
# We are not allowed to ship an empty fedora-logos package
dnf -y swap fedora-logos generic-logos
rpm --erase --nodeps --nodb generic-logos

# Copy Files to Container
rsync -rvK /ctx/system_files/shared/ /

mkdir -p /tmp/scripts/helpers
install -Dm0755 /ctx/build_files/shared/utils/ghcurl /tmp/scripts/helpers/ghcurl
export PATH="/tmp/scripts/helpers:$PATH"

echo "::endgroup::"

# Generate image-info.json
/ctx/build_files/base/00-image-info.sh

# Install Kernel and Akmods
/ctx/build_files/base/03-install-kernel-akmods.sh

# Install Additional Packages
/ctx/build_files/base/04-packages.sh

# Install Overrides and Fetch Install
/ctx/build_files/base/05-override-install.sh

# Build GNOME Extensions from Git Submodules
/ctx/build_files/shared/build-gnome-extensions.sh

## late stage changes

# Systemd and Remove Items
/ctx/build_files/base/17-cleanup.sh

# Run workarounds for lf (Likely not needed)
/ctx/build_files/base/18-workarounds.sh

# Regenerate initramfs
/ctx/build_files/base/19-initramfs.sh

if [ "${IMAGE_FLAVOR}" == "dx" ] ; then
  # Now we build DX!
  /ctx/build_files/shared/build-dx.sh
fi

# Validate all repos are disabled before committing
/ctx/build_files/shared/validate-repos.sh

# Clean Up
echo "::group:: Cleanup"
/ctx/build_files/shared/clean-stage.sh

echo "::endgroup::"

# Simple Tests
/ctx/build_files/base/20-tests.sh
```

## File: `build_files/shared/clean-stage.sh`
```bash
#!/usr/bin/bash

echo "::group:: ===$(basename "$0")==="

set -eoux pipefail

dnf clean all

systemctl mask flatpak-add-fedora-repos.service
rm -f /usr/lib/systemd/system/flatpak-add-fedora-repos.service

rm -rf /.gitkeep
find /var/* -maxdepth 0 -type d \! -name cache -exec rm -fr {} \;
find /var/cache/* -maxdepth 0 -type d \! -name libdnf5 \! -name rpm-ostree -exec rm -fr {} \;
rm -rf /tmp && mkdir -p /tmp
rm -rf /boot && mkdir -p /boot

echo "::endgroup::"
```

## File: `build_files/shared/copr-helpers.sh`
```bash
#!/usr/bin/bash
set -euo pipefail

copr_install_isolated() {
    local copr_name="$1"
    shift
    local packages=("$@")

    if [[ ${#packages[@]} -eq 0 ]]; then
        echo "ERROR: No packages specified for copr_install_isolated"
        return 1
    fi

    repo_id="copr:copr.fedorainfracloud.org:${copr_name//\//:}"

    echo "Installing ${packages[*]} from COPR $copr_name (isolated)"

    dnf5 -y copr enable "$copr_name"
    dnf5 -y copr disable "$copr_name"
    dnf5 -y install --enablerepo="$repo_id" "${packages[@]}"

    echo "Installed ${packages[*]} from $copr_name"
}
```

## File: `build_files/shared/validate-repos.sh`
```bash
#!/usr/bin/bash

echo "::group:: ===$(basename "$0")==="

set -eou pipefail

REPOS_DIR="/etc/yum.repos.d"
VALIDATION_FAILED=0
ENABLED_REPOS=()

echo "Validating all repository files are disabled..."

# Check if repos directory exists
if [[ ! -d "$REPOS_DIR" ]]; then
    echo "Warning: $REPOS_DIR does not exist"
    exit 0
fi

# Function to check if a repo file has any enabled repos
check_repo_file() {
    local repo_file="$1"
    local basename_file
    basename_file=$(basename "$repo_file")

    # Skip if file doesn't exist or isn't readable
    [[ ! -f "$repo_file" ]] && return 0
    [[ ! -r "$repo_file" ]] && return 0

    # Check for enabled=1 in the file
    if grep -q "^enabled=1" "$repo_file" 2>/dev/null; then
        echo "ENABLED: $basename_file"
        ENABLED_REPOS+=("$basename_file")
        VALIDATION_FAILED=1

        # Show which sections are enabled
        echo "   Enabled sections:"
        local section_name=""
        while IFS= read -r line; do
            if [[ "$line" =~ ^\[.*\]$ ]]; then
                section_name="$line"
            elif [[ "$line" =~ ^enabled=1 ]]; then
                echo "     - $section_name"
            fi
        done < "$repo_file"
    else
        echo "Disabled: $basename_file"
    fi
}

echo ""
echo "Checking COPR repositories (standard naming)..."
echo "NOTE: With secure isolated installation, NO COPRs should be globally enabled!"
for repo in "$REPOS_DIR"/_copr:copr.fedorainfracloud.org:*.repo; do
    [[ -f "$repo" ]] && check_repo_file "$repo"
done

echo ""
echo "Checking COPR repositories (non-standard naming)..."
echo "SECURITY: Enabled COPRs can inject malicious versions of Fedora packages!"
for repo in "$REPOS_DIR"/_copr_*.repo; do
    [[ -f "$repo" ]] && check_repo_file "$repo"
done

echo ""
echo "Checking other third-party repositories..."
# List of known third-party repos that should be disabled
OTHER_REPOS=(
    "negativo17-fedora-multimedia.repo"
    "tailscale.repo"
    "vscode.repo"
    "docker-ce.repo"
    "fedora-cisco-openh264.repo"
    "fedora-coreos-pool.repo"
)

for repo_name in "${OTHER_REPOS[@]}"; do
    repo_path="$REPOS_DIR/$repo_name"
    if [[ -f "$repo_path" ]]; then
        check_repo_file "$repo_path"
    fi
done

echo ""
echo "Checking RPM Fusion repositories..."
for repo in "$REPOS_DIR"/rpmfusion-*.repo; do
    [[ -f "$repo" ]] && check_repo_file "$repo"
done

echo ""
echo "Checking Fedora updates-testing (should be disabled unless beta)..."
if [[ -f "$REPOS_DIR/fedora-updates-testing.repo" ]]; then
    if grep -q "^enabled=1" "$REPOS_DIR/fedora-updates-testing.repo" 2>/dev/null; then
        # Allow updates-testing to be enabled for beta builds
        if [[ "${UBLUE_IMAGE_TAG:-stable}" == "beta" ]]; then
            echo "updates-testing is enabled (allowed for beta builds)"
        else
            echo "ENABLED: fedora-updates-testing.repo (should only be enabled for beta)"
            ENABLED_REPOS+=("fedora-updates-testing.repo")
            VALIDATION_FAILED=1
        fi
    else
        echo "Disabled: fedora-updates-testing.repo"
    fi
fi

# Final summary
echo ""
echo "======================================"
if [[ $VALIDATION_FAILED -eq 1 ]]; then
    echo "VALIDATION FAILED"
    echo "======================================"
    echo ""
    echo "The following repositories are still ENABLED:"
    for repo in "${ENABLED_REPOS[@]}"; do
        echo "  • $repo"
    done
    exit 1
fi

echo "::endgroup::"
```

## File: `build_files/shared/utils/ghcurl`
```
#!/usr/bin/env bash
set -euo pipefail

# Check for GITHUB_TOKEN in /run/secrets/GITHUB_TOKEN (Podman secret mount)
if [[ -f /run/secrets/GITHUB_TOKEN ]]; then
  GITHUB_TOKEN=$(< /run/secrets/GITHUB_TOKEN)
  echo "Using GITHUB_TOKEN from /run/secrets/GITHUB_TOKEN for authentication." >&2
  AUTH_HEADER="Authorization: Bearer $GITHUB_TOKEN"
else
  echo "GITHUB_TOKEN secret not found. Using unauthenticated requests." >&2
  AUTH_HEADER=""
fi

URL="$1"
shift
OPTIONS=("$@")

if [[ -n "$AUTH_HEADER" ]]; then
  curl -sSL -H "$AUTH_HEADER" "${OPTIONS[@]}" "$URL"
else
  curl -sSL "${OPTIONS[@]}" "$URL"
fi
```

## File: `system_files/dx/usr/lib/dracut/dracut.conf.d/80-vfio.conf`
```
force_drivers+=" vfio vfio_iommu_type1 vfio-pci "
```

## File: `system_files/dx/usr/lib/sysctl.d/docker-ce.conf`
```
net.ipv4.ip_forward = 1
```

## File: `system_files/dx/usr/lib/systemd/system/bluefin-dx-groups.service`
```
[Unit]
Description=Add wheel members to docker,and incus-admin groups

[Service]
Type=oneshot
ExecStart=/usr/bin/bluefin-dx-groups
Restart=on-failure
RestartSec=30
StartLimitInterval=0

[Install]
WantedBy=default.target
```

## File: `system_files/dx/usr/lib/systemd/system/incus-workaround.service`
```
[Unit]
Description=Workaround swtpm not having the correct label
ConditionFileIsExecutable=/usr/bin/incus
ConditionFileIsExecutable=/usr/bin/incus-agent
ConditionPathExists=/usr/lib/incus
After=local-fs.target

[Service]
Type=oneshot
# Copy if it doesn't exist
ExecStartPre=/usr/bin/bash -c "[ -x /usr/local/bin/overrides/incus ] || /usr/bin/cp /usr/bin/incus /usr/local/bin/overrides/incus"
ExecStartPre=/usr/bin/bash -c "[ -x /usr/local/bin/overrides/incus-agent ] || /usr/bin/cp /usr/bin/incus /usr/local/bin/overrides/incus-agent"
ExecStartPre=/usr/bin/bash -c "[ -d /usr/local/lib/overrides/incus ] || /usr/bin/cp -R /usr/bin/incus /usr/local/lib/overrides/incus"
# This is faster than using .mount unit. Also allows for the previous line/cleanup
ExecStartPre=/usr/bin/mount --bind /usr/local/bin/overrides/incus /usr/bin/incus
ExecStartPre=/usr/bin/mount --bind /usr/local/bin/overrides/incus-agent /usr/bin/incus-agent
ExecStartPre=/usr/bin/mount --bind /usr/local/lib/overrides/incus /usr/lib/incus
# Fix SELinux label
ExecStart=/usr/sbin/restorecon /usr/bin/incus
ExecStart=/usr/sbin/restorecon /usr/bin/incus-agent
ExecStart=/usr/sbin/restorecon -R /usr/lib/incus
# Clean-up after ourselves
ExecStop=/usr/bin/umount /usr/bin/incus
ExecStop=/usr/bin/umount /usr/bin/incus-agent
ExecStop=/usr/bin/umount /usr/lib/incus
ExecStop=/usr/bin/rm /usr/local/bin/overrides/incus
ExecStop=/usr/bin/rm /usr/local/bin/overrides/incus-agent
ExecStop=/usr/bin/rm -r /usr/local/lib/overrides/incus
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

## File: `system_files/dx/usr/lib/systemd/system/libvirt-workaround.service`
```
[Unit]
Description=Workaround to relabel libvirt files and directories
ConditionPathIsDirectory=/var/lib/libvirt/
After=local-fs.target

[Service]
Type=oneshot
ExecStart=-/usr/sbin/restorecon -R /var/log/libvirt/
ExecStart=-/usr/sbin/restorecon -R /var/lib/libvirt/
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

## File: `system_files/dx/usr/lib/systemd/system/swtpm-workaround.service`
```
[Unit]
Description=Workaround swtpm not having the correct label
ConditionFileIsExecutable=/usr/bin/swtpm
After=local-fs.target

[Service]
Type=oneshot
# Copy if it doesn't exist
ExecStartPre=/usr/bin/bash -c "[ -x /usr/local/bin/overrides/swtpm ] || /usr/bin/cp /usr/bin/swtpm /usr/local/bin/overrides/swtpm"
# This is faster than using .mount unit. Also allows for the previous line/cleanup
ExecStartPre=/usr/bin/mount --bind /usr/local/bin/overrides/swtpm /usr/bin/swtpm
# Fix SELinux label
ExecStart=/usr/sbin/restorecon /usr/bin/swtpm
# Clean-up after ourselves
ExecStop=/usr/bin/umount /usr/bin/swtpm
ExecStop=/usr/bin/rm /usr/local/bin/overrides/swtpm
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

## File: `system_files/dx/usr/lib/tmpfiles.d/incus-workaround.conf`
```
C /usr/local/bin/overrides/incus - - - - /usr/bin/incus
C /usr/local/bin/overrides/incus-agent - - - - /usr/bin/incus-agent
C /usr/local/lib/overrides/incus - - - - /usr/lib/incus
```

## File: `system_files/dx/usr/lib/tmpfiles.d/libvirt-workaround.conf`
```
d /var/log/libvirt 0750 - - - -
```

## File: `system_files/dx/usr/lib/tmpfiles.d/swtpm-workaround.conf`
```
C /usr/local/bin/overrides/swtpm - - - - /usr/bin/swtpm
d /var/lib/swtpm-localca 0750 tss tss - -
```

## File: `system_files/dx/usr/share/ublue-os/user-setup.hooks.d/10-vscode.sh`
```bash
#!/usr/bin/bash

source /usr/lib/ublue/setup-services/libsetup.sh

version-script vscode user 1 || exit 1

set -x

# Setup VSCode
if test ! -e "$HOME"/.config/Code/User/settings.json; then
	mkdir -p "$HOME"/.config/Code/User
	cp -f /etc/skel/.config/Code/User/settings.json "$HOME"/.config/Code/User/settings.json
fi

code --install-extension ms-vscode-remote.remote-containers
code --install-extension ms-vscode-remote.remote-ssh
code --install-extension ms-azuretools.vscode-containers
```

## File: `system_files/shared/etc/rpm-ostreed.conf`
```
# Entries in this file show the compile time defaults.
# You can change settings by editing this file.
# For option meanings, see rpm-ostreed.conf(5).

[Daemon]
AutomaticUpdatePolicy=stage

##########
# NOTE: This will be set to true by default in Spring 2025
#
# Set this to false to enable local layering with dnf
# This is an unsupported configuration that can lead to upgrade issues
# You should know what you're doing before setting this to `false`
#
# See [future link] for more information
##########
# LockLayering=false
```

## File: `system_files/shared/etc/profile.d/90-bluefin-starship.sh`
```bash
# shellcheck shell=sh
command -v starship >/dev/null 2>&1 || return 0

if [ "$(basename "$(readlink /proc/$$/exe)")" = "bash" ]; then
  eval "$(starship init bash)"
fi
```

## File: `system_files/shared/usr/lib/systemd/system/flatpak-nuke-fedora.service`
```
[Unit]
Description=Remove Fedora flatpak repositories
Before=flatpak-preinstall.service
Before=flatpak-system-helper.service
# Make sure we run before the Fedora service if it exists
Before=flatpak-add-fedora-repos.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/bin/flatpak remote-delete --system fedora
ExecStart=/usr/bin/flatpak remote-delete --system fedora-testing
# Make sure even if flatpak-add-fedora-repos.service  exists, it
# won't run.
ExecStart=/usr/bin/touch /var/lib/flatpak/.fedora-initialized
# Flatpak will fail if the remote doesn't exist, but we don't mind
SuccessExitStatus=1

[Install]
WantedBy=multi-user.target
```

## File: `system_files/shared/usr/share/ublue-os/privileged-setup.hooks.d/10-tailscale.sh`
```bash
#!/usr/bin/bash

source /usr/lib/ublue/setup-services/libsetup.sh

version-script tailscale privileged 1 || exit 0

set -xeuo pipefail

tailscale set --operator="$(getent passwd "$PKEXEC_UID" | cut -d: -f1)"
```

## File: `system_files/shared/usr/share/ublue-os/privileged-setup.hooks.d/99-flatpaks.sh`
```bash
#!/usr/bin/bash

source /usr/lib/ublue/setup-services/libsetup.sh

version-script flatpaks privileged 1 || exit 0

set -x

# Set up Firefox default configuration
ARCH=$(arch)
if [ "$ARCH" != "aarch64" ] ; then
	mkdir -p "/var/lib/flatpak/extension/org.mozilla.firefox.systemconfig/${ARCH}/stable/defaults/pref"
	rm -f "/var/lib/flatpak/extension/org.mozilla.firefox.systemconfig/${ARCH}/stable/defaults/pref/*bluefin*.js"
	/usr/bin/cp -rf /usr/share/ublue-os/firefox-config/* "/var/lib/flatpak/extension/org.mozilla.firefox.systemconfig/${ARCH}/stable/defaults/pref/"
fi
```

## File: `system_files/shared/usr/share/ublue-os/system-setup.hooks.d/10-framework.sh`
```bash
#!/usr/bin/env bash

source /usr/lib/ublue/setup-services/libsetup.sh

version-script framework system 2 || exit 0

set -x

CPU_VENDOR=$(grep "vendor_id" "/proc/cpuinfo" | uniq | awk -F": " '{ print $2 }')
VEN_ID="$(cat /sys/devices/virtual/dmi/id/chassis_vendor)"
BIOS_VERSION="$(cat /sys/devices/virtual/dmi/id/bios_version 2>/dev/null)"

# GLOBAL
KARGS=$(rpm-ostree kargs)
NEEDED_KARGS=()
echo "Current kargs: $KARGS"

if [[ $KARGS =~ "nomodeset" ]]; then
	echo "Removing nomodeset"
	NEEDED_KARGS+=("--delete-if-present=nomodeset")
fi

if [[ ":Framework:" =~ :$VEN_ID: ]]; then
	if [[ "GenuineIntel" == "$CPU_VENDOR" ]]; then
		if [[ ! $KARGS =~ "hid_sensor_hub" ]]; then
			echo "Intel Framework Laptop detected, applying needed keyboard fix"
			NEEDED_KARGS+=("--append-if-missing=module_blacklist=hid_sensor_hub")
		fi
	fi
fi

#shellcheck disable=SC2128
if [[ -n "$NEEDED_KARGS" ]]; then
	echo "Found needed karg changes, applying the following: ${NEEDED_KARGS[*]}"
	plymouth display-message --text="Updating kargs - Please wait, this may take a while" || true
	rpm-ostree kargs "${NEEDED_KARGS[*]}" --reboot || exit 1
else
	echo "No karg changes needed"
fi

SYS_ID="$(cat /sys/devices/virtual/dmi/id/product_name)"

# FRAMEWORK 13 FIXES
if [[ "$VEN_ID" == "Framework" && "$SYS_ID" == "Laptop 13 ("* ]]; then
    echo "Framework Laptop 13 detected"

    # Older versions of this script applied a modprobe flag to fix 3.5 mm jack headset detection
    # which is no longer needed because the kernel applies this automatically.
    if [[ ! -f /etc/modprobe.d/alsa.conf ]]; then
        echo "Removing obsolete 3.5mm audio jack fix"
        rm -f /etc/modprobe.d/alsa.conf
    fi

    # Suspend fix for Framework 13 Ryzen 7040
    # On BIOS versions >= 3.09, the workaround is not needed
    # (https://knowledgebase.frame.work/framework-laptop-13-bios-and-driver-releases-amd-ryzen-7040-series-r1rXGVL16)
    if [[ "$SYS_ID" == "Laptop 13 (AMD Ryzen 7040Series)" && "$(printf '%s\n' 03.08 "$BIOS_VERSION" | sort -V | tail -n1)" == "03.08" ]]; then
        # BIOS is older, apply workaround
        if [[ ! -f /etc/udev/rules.d/20-suspend-fixes.rules ]]; then
            echo "Framework 13 Ryzen 7040 with BIOS $BIOS_VERSION < 3.09 — applying suspend workaround"
            echo 'ACTION=="add", SUBSYSTEM=="serio", DRIVERS=="atkbd", ATTR{power/wakeup}="disabled"' \
                > /etc/udev/rules.d/20-suspend-fixes.rules
        fi
    else
        # BIOS is >= 3.09, remove workaround if present
        # Older versions of this script also mistakenly applied then
        # workaround to Framework 13 Ryzen AI 300. Will get cleaned up here too.
        if [[ -f /etc/udev/rules.d/20-suspend-fixes.rules ]]; then
            echo "Removing old suspend workaround"
            rm -f /etc/udev/rules.d/20-suspend-fixes.rules
        fi
    fi
fi
```

## File: `system_files/shared/usr/share/ublue-os/user-setup.hooks.d/10-theming.sh`
```bash
#!/usr/bin/env bash

source /usr/lib/ublue/setup-services/libsetup.sh

version-script theming user 1 || exit 0

set -xeuo pipefail

VEN_ID="$(cat /sys/devices/virtual/dmi/id/chassis_vendor)"

if [[ ":Framework:" =~ :$VEN_ID: ]]; then
	echo 'Setting Framework logo menu'
	dconf write /org/gnome/shell/extensions/Logo-menu/symbolic-icon true
	dconf write /org/gnome/shell/extensions/Logo-menu/menu-button-icon-image 31
	echo 'Setting touch scroll type'
	dconf write /org/gnome/desktop/peripherals/mouse/natural-scroll true
	if [[ $SYS_ID == "Laptop ("* ]]; then
		echo 'Applying font fix for Framework 13'
		dconf write /org/gnome/desktop/interface/text-scaling-factor 1.25
	fi
fi

SYS_ID="$(cat /sys/devices/virtual/dmi/id/product_name)"

if [[ ":Thelio Astra:" =~ :$SYS_ID: ]]; then
	echo 'Setting Ampere Logo'
 	dconf write /org/gnome/shell/extensions/Logo-menu/symbolic-icon true
	dconf write /org/gnome/shell/extensions/Logo-menu/menu-button-icon-image 32
 fi
```

## File: `system_files/shared/usr/share/ublue-os/user-setup.hooks.d/20-framework.sh`
```bash
#!/usr/bin/env bash

source /usr/lib/ublue/setup-services/libsetup.sh

version-script framework tool 1 || exit 0

set -x

VEN_ID="$(cat /sys/devices/virtual/dmi/id/chassis_vendor)"

# Install framework_tool and wallpapers for Framework laptops
if [[ ":Framework:" =~ :$VEN_ID: ]]; then
    BREW_PREFIX="/home/linuxbrew/.linuxbrew"

    # Check if Homebrew is available and user has write permissions
    if command -v brew &> /dev/null && [[ -w "$BREW_PREFIX" ]]; then
        # Check if framework_tool is already installed via brew
        if ! brew list --cask framework_tool &> /dev/null; then
            echo "Framework laptop detected, installing framework_tool"
            if brew install --cask ublue-os/tap/framework_tool; then
                echo "framework_tool installed successfully"
            else
                echo "Warning: framework_tool installation failed, will retry on next run"
            fi
        else
            echo "framework_tool already installed, skipping"
        fi

        # Check if framework-wallpapers is already installed via brew
        if ! brew list --cask framework-wallpapers &> /dev/null; then
            echo "Installing Framework wallpapers"
            if brew install --cask ublue-os/tap/framework-wallpapers; then
                echo "Framework wallpapers installed successfully"
            else
                echo "Warning: framework-wallpapers installation failed, will retry on next run"
            fi
        else
            echo "Framework wallpapers already installed, skipping"
        fi
    else
        echo "Warning: brew not found or user lacks write permission to $BREW_PREFIX, skipping Framework software installation (will retry when available)"
    fi
fi
```

## File: `system_files/shared/usr/share/ublue-os/user-setup.hooks.d/99-privileged.sh`
```bash
#!/usr/bin/env bash

set -euo pipefail

echo "Running all privileged units"

pkexec /usr/bin/ublue-privileged-setup
```

