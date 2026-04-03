---
id: chart-testing-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:00.754786
---

# KNOWLEDGE EXTRACT: chart-testing
> **Extracted on:** 2026-03-30 22:59:40
> **Source:** chart-testing

---

## File: `.dockerignore`
```
.circleci
.history
.idea
.vscode
```

## File: `.editorconfig`
```
# EditorConfig is awesome: http://EditorConfig.org

root = true

[*]
indent_style = space
indent_size = 4
trim_trailing_whitespace = true
insert_final_newline = true
charset = utf-8

[*.{yml, yaml}]
indent_size = 2

[*.go]
indent_style = tab

[Makefile]
indent_style = tab
```

## File: `.gitignore`
```
.idea
.project
.settings
.vscode
/dist
/config.*
vendor
/ct-bin
```

## File: `.golangci.yml`
```yaml
---
version: "2"
run:
  issues-exit-code: 1
linters:
  enable:
    - asciicheck
    - errorlint
    - gocritic
    - gosec
    - importas
    - misspell
    - prealloc
    - revive
    - staticcheck
    - unconvert
    - whitespace
  exclusions:
    generated: lax
    presets:
      - comments
      - common-false-positives
      - legacy
      - std-error-handling
    paths:
      - third_party$
      - builtin$
      - examples$
issues:
  max-issues-per-linter: 0
  max-same-issues: 0
  uniq-by-line: false
formatters:
  enable:
    - gofmt
    - goimports
  exclusions:
    generated: lax
    paths:
      - third_party$
      - builtin$
      - examples$
```

## File: `.goreleaser.yml`
```yaml
project_name: chart-testing
version: 2

env:
  - COSIGN_YES=true

before:
  hooks:
    - go mod download

sboms:
  - artifacts: archive

builds:
  - main: ct/main.go
    binary: ct
    env:
      - CGO_ENABLED=0
    goarch:
      - amd64
      - arm64
      - arm
    goos:
      - linux
      - darwin
      - windows
    ignore:
      - goarch: arm
        goos: windows
    flags:
      - -trimpath
    mod_timestamp: '{{ .CommitTimestamp }}'
    ldflags:
      - >-
        -X github.com/helm/chart-testing/v3/ct/cmd.Version={{ .Tag }}
        -X github.com/helm/chart-testing/v3/ct/cmd.GitCommit={{ .Commit }}
        -X github.com/helm/chart-testing/v3/ct/cmd.BuildDate={{ .Date }}

archives:
  - format_overrides:
      - goos: windows
        formats:
          - zip
    files:
      - LICENSE
      - README.md
      - etc/chart_schema.yaml
      - etc/lintconf.yaml

checksum:
  name_template: 'checksums.txt'

snapshot:
  version_template: "{{ .Tag }}-next"

dockers_v2:
  - images:
      - "quay.io/helmpack/chart-testing"
    tags:
      - "{{ .Tag }}"
      - "latest"
    labels:
      "org.opencontainers.image.version": "{{ .Version }}"
      "org.opencontainers.image.revision": "{{ .Commit }}"
      "org.opencontainers.image.title": "{{ .ProjectName }}"
      "org.opencontainers.image.created": "{{ .Date }}"
      "org.opencontainers.image.description": "ct - The chart testing tool"
      "org.opencontainers.image.vendor": "Helm"
      "org.opencontainers.image.licenses": "Apache-2.0"
      "org.opencontainers.image.source": "https://github.com/helm/chart-testing"
      "org.opencontainers.image.authors": "The Helm Authors"
    extra_files:
      - etc/chart_schema.yaml
      - etc/lintconf.yaml

signs:
  - id: all
    signature: "${artifact}.sig"
    certificate: "${artifact}.pem"
    cmd: cosign
    args: ["sign-blob", "--output-signature", "${artifact}.sig", "--output-certificate", "${artifact}.pem", "${artifact}"]
    artifacts: all

docker_signs:
  - id: images
    cmd: cosign
    args: ["sign", "${artifact}"]

changelog:
  use: github-native
```

## File: `build.sh`
```bash
#!/usr/bin/env bash

# Copyright The Helm Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -o errexit
set -o nounset
set -o pipefail

SCRIPT_DIR=$(dirname -- "$(readlink -e "${BASH_SOURCE[0]}" || realpath "${BASH_SOURCE[0]}")")
readonly SCRIPT_DIR

show_help() {
    cat << EOF
Usage: $(basename "$0") <options>

Build ct using Goreleaser.

    -h, --help      Display help
    -d, --debug     Display verbose output and run Goreleaser with --debug
    -r, --release   Create a release using Goreleaser. This includes the creation
                    of a GitHub release and building and pushing the Docker image.
                    If this flag is not specified, Goreleaser is run with --snapshot
EOF
}

main() {
    local debug=
    local release=

    while :; do
        case "${1:-}" in
            -h | --help)
                show_help
                exit
                ;;
            -d | --debug)
                debug=true
                ;;
            -r | --release)
                release=true
                ;;
            *)
                break
                ;;
        esac

        shift
    done

    local goreleaser_args=(--clean)

    if [[ -n "$debug" ]]; then
        goreleaser_args+=(--debug)
        set -x
    fi

    if [[ -z "$release" ]]; then
        goreleaser_args+=(--snapshot --skip=sign)
    fi

    pushd "$SCRIPT_DIR" > /dev/null

    go test -race ./...
    goreleaser "${goreleaser_args[@]}"

    popd > /dev/null
}

main "$@"
```

## File: `code-of-conduct.md`
```markdown
# Community Code of Conduct

Helm follows the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/main/code-of-conduct.md).
```

## File: `Dockerfile`
```
FROM alpine:3.23

RUN apk --no-cache add \
    bash \
    curl \
    git \
    libc6-compat \
    openssh-client \
    py3-pip \
    py3-wheel \
    python3 \
    yamllint

# Install Yamale YAML schema validator
ARG yamale_version=6.0.0
LABEL yamale-version=$yamale_version
RUN pip install --break-system-packages "yamale==$yamale_version"

ARG TARGETPLATFORM
# Install kubectl
ARG kubectl_version=v1.32.0
LABEL kubectl-version=$kubectl_version
RUN targetArch=$(echo $TARGETPLATFORM | cut -f2 -d '/') \
    && if [ ${targetArch} = "amd64" ]; then \
    HELM_ARCH="linux/amd64"; \
elif [ ${targetArch} = "arm64" ]; then \
    HELM_ARCH="linux/arm64"; \
fi \
    && curl -LO "dl.k8s.io/$kubectl_version/bin/$HELM_ARCH/kubectl" \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/

# Install Helm
ARG helm_version=v3.16.4
LABEL helm-version=$helm_version
RUN targetArch=$(echo $TARGETPLATFORM | cut -f2 -d '/') \
    && if [ ${targetArch} = "amd64" ]; then \
    HELM_ARCH="linux-amd64"; \
elif [ ${targetArch} = "arm64" ]; then \
    HELM_ARCH="linux-arm64"; \
fi \
    && curl -LO "https://get.helm.sh/helm-$helm_version-$HELM_ARCH.tar.gz" \
    && mkdir -p "/usr/local/helm-$helm_version" \
    && tar -xzf "helm-$helm_version-$HELM_ARCH.tar.gz" -C "/usr/local/helm-$helm_version" \
    && ln -s "/usr/local/helm-$helm_version/$HELM_ARCH/helm" /usr/local/bin/helm \
    && rm -f "helm-$helm_version-$HELM_ARCH.tar.gz"

COPY ./etc/chart_schema.yaml /etc/ct/chart_schema.yaml
COPY ./etc/lintconf.yaml /etc/ct/lintconf.yaml
ARG TARGETPLATFORM
COPY $TARGETPLATFORM/ct /usr/local/bin/ct
# Ensure that the binary is available on path and is executable
RUN ct --help
```

## File: `e2e-kind.sh`
```bash
#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

CLUSTER_NAME=chart-testing
readonly CLUSTER_NAME

K8S_VERSION=v1.22.9
readonly K8S_VERSION

create_kind_cluster() {
    kind create cluster --name "$CLUSTER_NAME" --image "kindest/node:$K8S_VERSION" --wait 60s

    kubectl cluster-info || kubectl cluster-info dump
    echo

    kubectl get nodes
    echo

    echo 'Cluster ready!'
    echo
}

test_e2e() {
    go test -cover -race -tags=integration ./...
    echo
}

cleanup() {
    kind delete cluster --name "$CLUSTER_NAME"
    echo 'Done!'
}

main() {
    trap cleanup EXIT

    create_kind_cluster
    test_e2e
}

main
```

## File: `go.mod`
```
module github.com/helm/chart-testing/v3

go 1.25.0

require (
	github.com/MakeNowJust/heredoc v1.0.0
	github.com/Masterminds/semver v1.5.0
	github.com/hashicorp/go-multierror v1.1.1
	github.com/hashicorp/go-retryablehttp v0.7.8
	github.com/mattn/go-shellwords v1.0.12
	github.com/mitchellh/go-homedir v1.1.0
	github.com/spf13/cobra v1.10.2
	github.com/spf13/pflag v1.0.10
	github.com/spf13/viper v1.21.0
	github.com/stretchr/testify v1.11.1
	gopkg.in/yaml.v2 v2.4.0
	helm.sh/helm/v3 v3.20.1
)

require (
	github.com/cpuguy83/go-md2man/v2 v2.0.6 // indirect
	github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc // indirect
	github.com/fsnotify/fsnotify v1.9.0 // indirect
	github.com/go-viper/mapstructure/v2 v2.4.0 // indirect
	github.com/hashicorp/errwrap v1.1.0 // indirect
	github.com/hashicorp/go-cleanhttp v0.5.2 // indirect
	github.com/inconshreveable/mousetrap v1.1.0 // indirect
	github.com/pelletier/go-toml/v2 v2.2.4 // indirect
	github.com/pkg/errors v0.9.1 // indirect
	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 // indirect
	github.com/russross/blackfriday/v2 v2.1.0 // indirect
	github.com/sagikazarmark/locafero v0.11.0 // indirect
	github.com/sourcegraph/conc v0.3.1-0.20240121214520-5f936abd7ae8 // indirect
	github.com/spf13/afero v1.15.0 // indirect
	github.com/spf13/cast v1.10.0 // indirect
	github.com/stretchr/objx v0.5.2 // indirect
	github.com/subosito/gotenv v1.6.0 // indirect
	go.yaml.in/yaml/v3 v3.0.4 // indirect
	golang.org/x/sys v0.40.0 // indirect
	golang.org/x/text v0.33.0 // indirect
	gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)
```

## File: `go.sum`
```
github.com/MakeNowJust/heredoc v1.0.0 h1:cXCdzVdstXyiTqTvfqk9SDHpKNjxuom+DOlyEeQ4pzQ=
github.com/MakeNowJust/heredoc v1.0.0/go.mod h1:mG5amYoWBHf8vpLOuehzbGGw0EHxpZZ6lCpQ4fNJ8LE=
github.com/Masterminds/semver v1.5.0 h1:H65muMkzWKEuNDnfl9d70GUjFniHKHRbFPGBuZ3QEww=
github.com/Masterminds/semver v1.5.0/go.mod h1:MB6lktGJrhw8PrUyiEoblNEGEQ+RzHPF078ddwwvV3Y=
github.com/cpuguy83/go-md2man/v2 v2.0.6 h1:XJtiaUW6dEEqVuZiMTn1ldk455QWwEIsMIJlo5vtkx0=
github.com/cpuguy83/go-md2man/v2 v2.0.6/go.mod h1:oOW0eioCTA6cOiMLiUPZOpcVxMig6NIQQ7OS05n1F4g=
github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc h1:U9qPSI2PIWSS1VwoXQT9A3Wy9MM3WgvqSxFWenqJduM=
github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/fatih/color v1.16.0 h1:zmkK9Ngbjj+K0yRhTVONQh1p/HknKYSlNT+vZCzyokM=
github.com/fatih/color v1.16.0/go.mod h1:fL2Sau1YI5c0pdGEVCbKQbLXB6edEj1ZgiY4NijnWvE=
github.com/frankban/quicktest v1.14.6 h1:7Xjx+VpznH+oBnejlPUj8oUpdxnVs4f8XU8WnHkI4W8=
github.com/frankban/quicktest v1.14.6/go.mod h1:4ptaffx2x8+WTWXmUCuVU6aPUX1/Mz7zb5vbUoiM6w0=
github.com/fsnotify/fsnotify v1.9.0 h1:2Ml+OJNzbYCTzsxtv8vKSFD9PbJjmhYF14k/jKC7S9k=
github.com/fsnotify/fsnotify v1.9.0/go.mod h1:8jBTzvmWwFyi3Pb8djgCCO5IBqzKJ/Jwo8TRcHyHii0=
github.com/go-viper/mapstructure/v2 v2.4.0 h1:EBsztssimR/CONLSZZ04E8qAkxNYq4Qp9LvH92wZUgs=
github.com/go-viper/mapstructure/v2 v2.4.0/go.mod h1:oJDH3BJKyqBA2TXFhDsKDGDTlndYOZ6rGS0BRZIxGhM=
github.com/google/go-cmp v0.7.0 h1:wk8382ETsv4JYUZwIsn6YpYiWiBsYLSJiTsyBybVuN8=
github.com/google/go-cmp v0.7.0/go.mod h1:pXiqmnSA92OHEEa9HXL2W4E7lf9JzCmGVUdgjX3N/iU=
github.com/hashicorp/errwrap v1.0.0/go.mod h1:YH+1FKiLXxHSkmPseP+kNlulaMuP3n2brvKWEqk/Jc4=
github.com/hashicorp/errwrap v1.1.0 h1:OxrOeh75EUXMY8TBjag2fzXGZ40LB6IKw45YeGUDY2I=
github.com/hashicorp/errwrap v1.1.0/go.mod h1:YH+1FKiLXxHSkmPseP+kNlulaMuP3n2brvKWEqk/Jc4=
github.com/hashicorp/go-cleanhttp v0.5.2 h1:035FKYIWjmULyFRBKPs8TBQoi0x6d9G4xc9neXJWAZQ=
github.com/hashicorp/go-cleanhttp v0.5.2/go.mod h1:kO/YDlP8L1346E6Sodw+PrpBSV4/SoxCXGY6BqNFT48=
github.com/hashicorp/go-hclog v1.6.3 h1:Qr2kF+eVWjTiYmU7Y31tYlP1h0q/X3Nl3tPGdaB11/k=
github.com/hashicorp/go-hclog v1.6.3/go.mod h1:W4Qnvbt70Wk/zYJryRzDRU/4r0kIg0PVHBcfoyhpF5M=
github.com/hashicorp/go-multierror v1.1.1 h1:H5DkEtf6CXdFp0N0Em5UCwQpXMWke8IA0+lD48awMYo=
github.com/hashicorp/go-multierror v1.1.1/go.mod h1:iw975J/qwKPdAO1clOe2L8331t/9/fmwbPZ6JB6eMoM=
github.com/hashicorp/go-retryablehttp v0.7.8 h1:ylXZWnqa7Lhqpk0L1P1LzDtGcCR0rPVUrx/c8Unxc48=
github.com/hashicorp/go-retryablehttp v0.7.8/go.mod h1:rjiScheydd+CxvumBsIrFKlx3iS0jrZ7LvzFGFmuKbw=
github.com/inconshreveable/mousetrap v1.1.0 h1:wN+x4NVGpMsO7ErUn/mUI3vEoE6Jt13X2s0bqwp9tc8=
github.com/inconshreveable/mousetrap v1.1.0/go.mod h1:vpF70FUmC8bwa3OWnCshd2FqLfsEA9PFc4w1p2J65bw=
github.com/kr/pretty v0.2.1/go.mod h1:ipq/a2n7PKx3OHsz4KJII5eveXtPO4qwEXGdVfWzfnI=
github.com/kr/pretty v0.3.1 h1:flRD4NNwYAUpkphVc1HcthR4KEIFJ65n8Mw5qdRn3LE=
github.com/kr/pretty v0.3.1/go.mod h1:hoEshYVHaxMs3cyo3Yncou5ZscifuDolrwPKZanG3xk=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/mattn/go-colorable v0.1.13 h1:fFA4WZxdEF4tXPZVKMLwD8oUnCTTo08duU7wxecdEvA=
github.com/mattn/go-colorable v0.1.13/go.mod h1:7S9/ev0klgBDR4GtXTXX8a3vIGJpMovkB8vQcUbaXHg=
github.com/mattn/go-isatty v0.0.20 h1:xfD0iDuEKnDkl03q4limB+vH+GxLEtL/jb4xVJSWWEY=
github.com/mattn/go-isatty v0.0.20/go.mod h1:W+V8PltTTMOvKvAeJH7IuucS94S2C6jfK/D7dTCTo3Y=
github.com/mattn/go-shellwords v1.0.12 h1:M2zGm7EW6UQJvDeQxo4T51eKPurbeFbe8WtebGE2xrk=
github.com/mattn/go-shellwords v1.0.12/go.mod h1:EZzvwXDESEeg03EKmM+RmDnNOPKG4lLtQsUlTZDWQ8Y=
github.com/mitchellh/go-homedir v1.1.0 h1:lukF9ziXFxDFPkA1vsr5zpc1XuPDn/wFntq5mG+4E0Y=
github.com/mitchellh/go-homedir v1.1.0/go.mod h1:SfyaCUpYCn1Vlf4IUYiD9fPX4A5wJrkLzIz1N1q0pr0=
github.com/pelletier/go-toml/v2 v2.2.4 h1:mye9XuhQ6gvn5h28+VilKrrPoQVanw5PMw/TB0t5Ec4=
github.com/pelletier/go-toml/v2 v2.2.4/go.mod h1:2gIqNv+qfxSVS7cM2xJQKtLSTLUE9V8t9Stt+h56mCY=
github.com/pkg/errors v0.9.1 h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=
github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 h1:Jamvg5psRIccs7FGNTlIRMkT8wgtp5eCXdBlqhYGL6U=
github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rogpeppe/go-internal v1.9.0 h1:73kH8U+JUqXU8lRuOHeVHaa/SZPifC7BkcraZVejAe8=
github.com/rogpeppe/go-internal v1.9.0/go.mod h1:WtVeX8xhTBvf0smdhujwtBcq4Qrzq/fJaraNFVN+nFs=
github.com/russross/blackfriday/v2 v2.1.0 h1:JIOH55/0cWyOuilr9/qlrm0BSXldqnqwMsf35Ld67mk=
github.com/russross/blackfriday/v2 v2.1.0/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
github.com/sagikazarmark/locafero v0.11.0 h1:1iurJgmM9G3PA/I+wWYIOw/5SyBtxapeHDcg+AAIFXc=
github.com/sagikazarmark/locafero v0.11.0/go.mod h1:nVIGvgyzw595SUSUE6tvCp3YYTeHs15MvlmU87WwIik=
github.com/sourcegraph/conc v0.3.1-0.20240121214520-5f936abd7ae8 h1:+jumHNA0Wrelhe64i8F6HNlS8pkoyMv5sreGx2Ry5Rw=
github.com/sourcegraph/conc v0.3.1-0.20240121214520-5f936abd7ae8/go.mod h1:3n1Cwaq1E1/1lhQhtRK2ts/ZwZEhjcQeJQ1RuC6Q/8U=
github.com/spf13/afero v1.15.0 h1:b/YBCLWAJdFWJTN9cLhiXXcD7mzKn9Dm86dNnfyQw1I=
github.com/spf13/afero v1.15.0/go.mod h1:NC2ByUVxtQs4b3sIUphxK0NioZnmxgyCrfzeuq8lxMg=
github.com/spf13/cast v1.10.0 h1:h2x0u2shc1QuLHfxi+cTJvs30+ZAHOGRic8uyGTDWxY=
github.com/spf13/cast v1.10.0/go.mod h1:jNfB8QC9IA6ZuY2ZjDp0KtFO2LZZlg4S/7bzP6qqeHo=
github.com/spf13/cobra v1.10.2 h1:DMTTonx5m65Ic0GOoRY2c16WCbHxOOw6xxezuLaBpcU=
github.com/spf13/cobra v1.10.2/go.mod h1:7C1pvHqHw5A4vrJfjNwvOdzYu0Gml16OCs2GRiTUUS4=
github.com/spf13/pflag v1.0.9/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/pflag v1.0.10 h1:4EBh2KAYBwaONj6b2Ye1GiHfwjqyROoF4RwYO+vPwFk=
github.com/spf13/pflag v1.0.10/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/viper v1.21.0 h1:x5S+0EU27Lbphp4UKm1C+1oQO+rKx36vfCoaVebLFSU=
github.com/spf13/viper v1.21.0/go.mod h1:P0lhsswPGWD/1lZJ9ny3fYnVqxiegrlNrEmgLjbTCAY=
github.com/stretchr/objx v0.5.2 h1:xuMeJ0Sdp5ZMRXx/aWO6RZxdr3beISkG5/G/aIRr3pY=
github.com/stretchr/objx v0.5.2/go.mod h1:FRsXN1f5AsAjCGJKqEizvkpNtU+EGNCLh3NxZ/8L+MA=
github.com/stretchr/testify v1.11.1 h1:7s2iGBzp5EwR7/aIZr8ao5+dra3wiQyKjjFuvgVKu7U=
github.com/stretchr/testify v1.11.1/go.mod h1:wZwfW3scLgRK+23gO65QZefKpKQRnfz6sD981Nm4B6U=
github.com/subosito/gotenv v1.6.0 h1:9NlTDc1FTs4qu0DDq7AEtTPNw6SVm7uBMsUCUjABIf8=
github.com/subosito/gotenv v1.6.0/go.mod h1:Dk4QP5c2W3ibzajGcXpNraDfq2IrhjMIvMSWPKKo0FU=
go.yaml.in/yaml/v3 v3.0.4 h1:tfq32ie2Jv2UxXFdLJdh3jXuOzWiL1fo0bu/FbuKpbc=
go.yaml.in/yaml/v3 v3.0.4/go.mod h1:DhzuOOF2ATzADvBadXxruRBLzYTpT36CKvDb3+aBEFg=
golang.org/x/sys v0.40.0 h1:DBZZqJ2Rkml6QMQsZywtnjnnGvHza6BTfYFWY9kjEWQ=
golang.org/x/sys v0.40.0/go.mod h1:OgkHotnGiDImocRcuBABYBEXf8A9a87e/uXjp9XT3ks=
golang.org/x/text v0.33.0 h1:B3njUFyqtHDUI5jMn1YIr5B0IE2U0qck04r6d4KPAxE=
golang.org/x/text v0.33.0/go.mod h1:LuMebE6+rBincTi9+xWTY8TztLzKHc/9C1uBCG27+q8=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/yaml.v2 v2.4.0 h1:D8xgwECY7CYvx+Y2n4sBz93Jn9JRvxdiyyo8CTfuKaY=
gopkg.in/yaml.v2 v2.4.0/go.mod h1:RDklbk79AGWmwhnvt/jBztapEOGDOx6ZbXqjP6csGnQ=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
helm.sh/helm/v3 v3.20.1 h1:T8PodUaH1UwNvE+imUA2mIKjJItY8g7CVvLVP5g4NzI=
helm.sh/helm/v3 v3.20.1/go.mod h1:Fl1kBaWCpkUrM6IYXPjQ3bdZQfFrogKArqptvueZ6Ww=
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
# Chart Testing

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Go Report Card](https://goreportcard.com/badge/github.com/helm/chart-testing)](https://goreportcard.com/report/github.com/helm/chart-testing)
[![ci](https://github.com/helm/chart-testing/workflows/ci/badge.svg)](https://github.com/helm/chart-testing/actions/workflows/ci.yaml)

`ct` is the tool for testing Helm charts.
It is meant to be used for linting and testing pull requests.
It automatically detects charts changed against the target branch.

## Installation

### Prerequisites

It is recommended to use the provided Docker image which can be [found on Quay](https://quay.io/repository/helmpack/chart-testing).
It comes with all necessary tools installed.

* [Helm](http://helm.sh)
* [Git](https://git-scm.com) (2.17.0 or later)
* [Yamllint](https://github.com/adrienverge/yamllint)
* [Yamale](https://github.com/23andMe/Yamale)
* [Kubectl](https://kubernetes.io/brain/knowledge/docs_legacy/reference/kubectl/overview/)

### Binary Distribution

Download the release distribution for your OS from the Releases page:

https://github.com/helm/chart-testing/releases

Unpack the `ct` binary, add it to your PATH, and you are good to go!

### Docker Image

A Docker image is available at `quay.io/helmpack/chart-testing` with list of
available tags [here](https://quay.io/repository/helmpack/chart-testing?tab=tags).

### Homebrew

```console
$ brew install chart-testing
```

## Usage

See documentation for individual commands:

* [ct](doc/ct.md)
* [ct install](doc/ct_install.md)
* [ct lint](doc/ct_lint.md)
* [ct lint-and-install](doc/ct_lint-and-install.md)
* [ct list-changed](doc/ct_list-changed.md)
* [ct version](doc/ct_version.md)

For a more extensive how-to guide, please see:

* [charts-repo-actions-demo](https://github.com/helm/charts-repo-actions-demo)

## Configuration

`ct` is a command-line application.
All command-line flags can also be set via environment variables or config file.
Environment variables must be prefixed with `CT_`.
Underscores must be used instead of hyphens.

CLI flags, environment variables, and a config file can be mixed.
The following order of precedence applies:

1. CLI flags
1. Environment variables
1. Config file

Note that linting requires config file for [yamllint](https://github.com/adrienverge/yamllint) and [yamale](https://github.com/23andMe/Yamale).
If not specified, these files are search in the current directory, the `.ct` directory in current directory, `$HOME/.ct`, and `/etc/ct`, in that order.
Samples are provided in the [etc](etc) folder.

### Examples

The following example show various way of configuring the same thing:

#### CLI

#### Remote repo

With remote repo:

    ct install --remote upstream --chart-dirs stable,incubator --build-id pr-42

#### Local repo

If you have a chart in current directory and ct installed on the host then you can run:

    ct install --chart-dirs . --charts .

With docker it works with:

    docker run -it --network host --workdir=/data --volume ~/.kube/config:/root/.kube/config:ro --volume $(pwd):/data quay.io/helmpack/chart-testing:v3.14.0 ct install --chart-dirs . --charts .

Notice that `workdir` param is important and must be the same as volume mounted.


#### Environment Variables

    export CT_REMOTE=upstream
    export CT_CHART_DIRS=stable,incubator
    export CT_BUILD_ID

    ct install

#### Config File

`config.yaml`:

```yaml
remote: upstream
chart-dirs:
  - stable
  - incubator
build-id: pr-42
```

#### Config Usage

    ct install --config config.yaml


`ct` supports any format [Viper](https://github.com/spf13/viper) can read, i. e. JSON, TOML, YAML, HCL, and Java properties files.

Notice that if no config file is specified, then `ct.yaml` (or any of the supported formats) is loaded from the current directory, `$HOME/.ct`, or `/etc/ct`, in that order, if found.


#### Using private chart repositories

When adding chart-repos you can specify additional arguments for the `helm repo add` command using `helm-repo-extra-args` on a per-repo basis.
You can also specify OCI registries which will be added using the `helm registry login` command, they also support the `helm-repo-extra-args` for authentication.
This could for example be used to authenticate a private chart repository.

`config.yaml`:

```yaml
chart-repos:
  - incubator=https://incubator.io
  - basic-auth=https://private.com
  - ssl-repo=https://self-signed.ca
  - oci-registry=oci://nice-oci-registry.pt
helm-repo-extra-args:
  - ssl-repo=--ca-file ./my-ca.crt
```

    ct install --config config.yaml --helm-repo-extra-args "basic-auth=--username user --password secret"

## Building from Source

`ct` is built using Go 1.13 or higher.

`build.sh` is used to build and release the tool.
It uses [Goreleaser](https://goreleaser.com/) under the covers.

Note: on MacOS you will need `GNU Coreutils readlink`.
You can install it with:

```console
brew install coreutils
```

Then add `gnubin` to your `$PATH`, with:

```console
echo 'export PATH="$(brew --prefix coreutils)/libexec/gnubin:$PATH"' >> ~/.bash_profile
bash --login
```

To use the build script:

```console
$ ./build.sh -h
Usage: build.sh <options>

Build ct using Goreleaser.

    -h, --help      Display help
    -d, --debug     Display verbose output and run Goreleaser with --debug
    -r, --release   Create a release using Goreleaser. This includes the creation
                    of a GitHub release and building and pushing the Docker image.
                    If this flag is not specified, Goreleaser is run with --snapshot
```

## Releasing

### Prepare Release

Before a release is created, versions have to be updated in the examples.
A pull request needs to be created for this, which should be merged right before the release is cut.
Here's a previous one for reference: https://github.com/helm/chart-testing/pull/89

### Create Release

The release workflow is [dispatched from github actions](https://github.com/helm/chart-testing/actions)
Versions must start with a lower-case `v`, e. g. `v3.14.0`.

## Supported versions

The previous MAJOR version will be supported for three months after each new MAJOR release.

Within this support window, pull requests for the previous MAJOR version should be made against the previous release branch.
For example, if the current MAJOR version is `v2`, the pull request base branch should be `release-v1`.

## Upgrading

When upgrading from `< v2.0.0` you will also need to change the usage in your scripts.
This is because, while the [v2.0.0](https://github.com/helm/chart-testing/releases/tag/v2.0.0) release has parity with `v1`, it was refactored from a bash library to Go so there are minor syntax differences.
Compare [v1 usage](https://github.com/helm/chart-testing/tree/release-v1#usage) with this (`v2`) version's README [usage](#usage) section above.
```

## File: `ct/main.go`
```go
// Copyright The Helm Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"github.com/helm/chart-testing/v3/ct/cmd"
)

func main() {
	cmd.Execute()
}
```

## File: `ct/cmd/docGen.go`
```go
// Copyright The Helm Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package cmd

import (
	"fmt"

	"github.com/MakeNowJust/heredoc"
	"github.com/spf13/cobra"
	"github.com/spf13/cobra/doc"
)

func newGenerateDocsCmd() *cobra.Command {
	return &cobra.Command{
		Use:   "doc-gen",
		Short: "Generate documentation",
		Long: heredoc.Doc(`
			Generate documentation for all commands
			to the 'docs' directory.`),
		Hidden: true,
		RunE:   generateDocs,
	}
}

func generateDocs(_ *cobra.Command, _ []string) error {
	fmt.Println("Generating docs...")

	err := doc.GenMarkdownTree(NewRootCmd(), "doc")
	if err != nil {
		return err
	}

	fmt.Println("Done.")
	return nil
}
```

## File: `ct/cmd/install.go`
```go
// Copyright The Helm Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package cmd

import (
	"fmt"

	"github.com/MakeNowJust/heredoc"
	"github.com/helm/chart-testing/v3/pkg/chart"
	"github.com/helm/chart-testing/v3/pkg/config"

	"github.com/spf13/cobra"
	flag "github.com/spf13/pflag"
)

func newInstallCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "install",
		Short: "Install and test a chart",
		Long: heredoc.Doc(`
			Run 'helm install', 'helm test', and optionally 'helm upgrade' on

			* changed charts (default)
			* specific charts (--charts)
			* all charts (--all)

			in given chart directories. If upgrade (--upgrade) is true, then this
			command will validate that 'helm test' passes for the following upgrade paths:

			* previous chart revision => current chart version (if non-breaking SemVer change)
			* current chart version => current chart version

			Charts may have multiple custom values files matching the glob pattern
			'*-values.yaml' in a directory named 'ci' in the root of the chart's
			directory. The chart is installed and tested for each of these files.
			If no custom values file is present, the chart is installed and
			tested with defaults.`),
		RunE: install,
	}

	flags := cmd.Flags()
	addInstallFlags(flags)
	addCommonLintAndInstallFlags(flags)
	return cmd
}

func addInstallFlags(flags *flag.FlagSet) {
	flags.String("build-id", "", heredoc.Doc(`
		An optional, arbitrary identifier that is added to the name of the namespace a
		chart is installed into. In a CI environment, this could be the build number or
		the ID of a pull request. If not specified, the name of the chart is used`))
	flags.Bool("upgrade", false, heredoc.Doc(`
		Whether to test an in-place upgrade of each chart from its previous revision if the
		current version should not introduce a breaking change according to the SemVer spec`))
	flags.Bool("skip-missing-values", false, heredoc.Doc(`
		When --upgrade has been passed, this flag will skip testing CI values files from the
		previous chart revision if they have been deleted or renamed at the current chart
		revision`))
	flags.String("namespace", "", heredoc.Doc(`
		Namespace to install the release(s) into. If not specified, each release will be
		installed in its own randomly generated namespace`))
	flags.String("release-name", "", heredoc.Doc(`
		Name for the release. If not specified, is set to the chart name and a random 
		identifier.`))
	flags.String("release-label", "app.kubernetes.io/instance", heredoc.Doc(`
		The label to be used as a selector when inspecting resources created by charts.
		This is only used if namespace is specified`))
	flags.String("helm-extra-set-args", "", heredoc.Doc(`
		Additional arguments for Helm. Must be passed as a single quoted string
		(e.g. "--set=name=value"`))
	flags.Bool("skip-clean-up", false, heredoc.Doc(`
		Skip resources clean-up. Used if need to continue other flows or keep it around.`))
}

func install(cmd *cobra.Command, _ []string) error {
	fmt.Println("Installing charts...")

	printConfig, err := cmd.Flags().GetBool("print-config")
	if err != nil {
		return err
	}
	configuration, err := config.LoadConfiguration(cfgFile, cmd, printConfig)
	if err != nil {
		return fmt.Errorf("failed loading configuration: %w", err)
	}

	testing, err := chart.NewTesting(*configuration)
	if err != nil {
		fmt.Println(err)
	}
	results, err := testing.InstallCharts()
	testing.PrintResults(results)

	if err != nil {
		return fmt.Errorf("failed installing charts: %w", err)
	}

	fmt.Println("All charts installed successfully")
	return nil
}
```

## File: `ct/cmd/lint.go`
```go
// Copyright The Helm Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package cmd

import (
	"fmt"

	"github.com/MakeNowJust/heredoc"
	"github.com/helm/chart-testing/v3/pkg/chart"
	"github.com/helm/chart-testing/v3/pkg/config"
	"github.com/spf13/cobra"
	flag "github.com/spf13/pflag"
)

func newLintCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "lint",
		Short: "Lint and validate a chart",
		Long: heredoc.Doc(`
			Run 'helm lint', version checking, YAML schema validation
			on 'Chart.yaml', YAML linting on 'Chart.yaml' and 'values.yaml',
			and maintainer validation on

			* changed charts (default)
			* specific charts (--charts)
			* all charts (--all)

			in given chart directories.

			Charts may have multiple custom values files matching the glob pattern
			'*-values.yaml' in a directory named 'ci' in the root of the chart's
			directory. The chart is linted for each of these files. If no custom
			values file is present, the chart is linted with defaults.`),
		RunE: lint,
	}

	flags := cmd.Flags()
	addLintFlags(flags)
	addCommonLintAndInstallFlags(flags)
	return cmd
}

func addLintFlags(flags *flag.FlagSet) {
	flags.String("lint-conf", "", heredoc.Doc(`
		The config file for YAML linting. If not specified, 'lintconf.yaml'
		is searched in the current directory, '$HOME/.ct', and '/etc/ct', in
		that order`))
	flags.String("chart-yaml-schema", "", heredoc.Doc(`
		The schema for chart.yml validation. If not specified, 'chart_schema.yaml'
		is searched in the current directory, '$HOME/.ct', and '/etc/ct', in
		that order.`))
	flags.Bool("validate-maintainers", true, heredoc.Doc(`
		Enable validation of maintainer account names in chart.yml.
		Works for GitHub, GitLab, and Bitbucket`))
	flags.Bool("check-version-increment", true, "Activates a check for chart version increments")
	flags.Bool("validate-chart-schema", true, heredoc.Doc(`
		Enable schema validation of 'Chart.yaml' using Yamale`))
	flags.Bool("validate-yaml", true, heredoc.Doc(`
		Enable linting of 'Chart.yaml' and values files`))
	flags.Bool("skip-helm-dependencies", false, heredoc.Doc(`
		Skip running 'helm dependency build' before linting`))
	flags.StringSlice("additional-commands", []string{}, heredoc.Doc(`
		Additional commands to run per chart (default: [])
		Commands will be executed in the same order as provided in the list and will
		be rendered with go template before being executed.
		Example: "helm unittest --helm3 -f tests/*.yaml {{ .Path }}"`))
}

func lint(cmd *cobra.Command, _ []string) error {
	fmt.Println("Linting charts...")

	printConfig, err := cmd.Flags().GetBool("print-config")
	if err != nil {
		return err
	}
	configuration, err := config.LoadConfiguration(cfgFile, cmd, printConfig)
	if err != nil {
		return fmt.Errorf("failed loading configuration: %w", err)
	}

	testing, err := chart.NewTesting(*configuration)
	if err != nil {
		return err
	}
	results, err := testing.LintCharts()
	testing.PrintResults(results)

	if err != nil {
		return fmt.Errorf("failed linting charts: %w", err)
	}

	fmt.Println("All charts linted successfully")
	return nil
}
```

## File: `ct/cmd/lintAndInstall.go`
```go
// Copyright The Helm Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package cmd

import (
	"fmt"

	"github.com/helm/chart-testing/v3/pkg/chart"
	"github.com/helm/chart-testing/v3/pkg/config"

	"github.com/spf13/cobra"
)

func newLintAndInstallCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:     "lint-and-install",
		Aliases: []string{"li"},
		Short:   "Lint, install, and test a chart",
		Long:    "Combines 'lint' and 'install' commands.",
		RunE:    lintAndInstall,
	}

	flags := cmd.Flags()
	addLintFlags(flags)
	addInstallFlags(flags)
	addCommonLintAndInstallFlags(flags)
	return cmd
}

func lintAndInstall(cmd *cobra.Command, _ []string) error {
	fmt.Println("Linting and installing charts...")

	printConfig, err := cmd.Flags().GetBool("print-config")
	if err != nil {
		return err
	}
	configuration, err := config.LoadConfiguration(cfgFile, cmd, printConfig)
	if err != nil {
		return fmt.Errorf("failed loading configuration: %w", err)
	}

	testing, err := chart.NewTesting(*configuration)
	if err != nil {
		return err
	}
	results, err := testing.LintAndInstallCharts()
	testing.PrintResults(results)

	if err != nil {
		return fmt.Errorf("failed linting and installing charts: %w", err)
	}

	fmt.Println("All charts linted and installed successfully")
	return nil
}
```

## File: `ct/cmd/listChanged.go`
```go
// Copyright The Helm Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package cmd

import (
	"fmt"

	"github.com/MakeNowJust/heredoc"

	"github.com/helm/chart-testing/v3/pkg/chart"
	"github.com/helm/chart-testing/v3/pkg/config"
	"github.com/spf13/cobra"
)

func newListChangedCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:     "list-changed",
		Aliases: []string{"ls-changed", "lsc"},
		Short:   "List changed charts",
		Long: heredoc.Doc(`
			"List changed charts based on configured charts directories,
			"remote, and target branch`),
		RunE: listChanged,
	}

	flags := cmd.Flags()
	addCommonFlags(flags)
	return cmd
}

func listChanged(cmd *cobra.Command, _ []string) error {
	printConfig, err := cmd.Flags().GetBool("print-config")
	if err != nil {
		return err
	}
	configuration, err := config.LoadConfiguration(cfgFile, cmd, printConfig)
	if err != nil {
		return fmt.Errorf("failed loading configuration: %w", err)
	}

	testing, err := chart.NewTesting(*configuration)
	if err != nil {
		return err
	}
	chartDirs, err := testing.ComputeChangedChartDirectories()
	if err != nil {
		return err
	}

	for _, dir := range chartDirs {
		fmt.Println(dir)
	}

	return nil
}
```

## File: `ct/cmd/root.go`
```go
// Copyright The Helm Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package cmd

import (
	"fmt"
	"os"

	"github.com/MakeNowJust/heredoc"
	"github.com/spf13/cobra"
	"github.com/spf13/pflag"
)

var (
	cfgFile string
)

func NewRootCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "ct",
		Short: "The Helm chart testing tool",
		Long: heredoc.Doc(`
			Lint and test

			* changed charts
			* specific charts
			* all charts

			in given chart directories.`),
		SilenceUsage: true,
	}

	cmd.AddCommand(newLintCmd())
	cmd.AddCommand(newInstallCmd())
	cmd.AddCommand(newLintAndInstallCmd())
	cmd.AddCommand(newListChangedCmd())
	cmd.AddCommand(newVersionCmd())
	cmd.AddCommand(newGenerateDocsCmd())

	cmd.DisableAutoGenTag = true

	return cmd
}

// Execute runs the application
func Execute() {
	if err := NewRootCmd().Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

func addCommonFlags(flags *pflag.FlagSet) {
	flags.StringVar(&cfgFile, "config", "", "Config file")
	flags.String("remote", "origin", "The name of the Git remote used to identify changed charts")
	flags.String("target-branch", "main", "The name of the target branch used to identify changed charts")
	flags.String("since", "HEAD", "The Git reference used to identify changed charts")
	flags.StringSlice("chart-dirs", []string{"charts"}, heredoc.Doc(`
		Directories containing Helm charts. May be specified multiple times
		or separate values with commas`))
	flags.StringSlice("excluded-charts", []string{}, heredoc.Doc(`
		Charts that should be skipped. May be specified multiple times
		or separate values with commas`))
	flags.Bool("print-config", false, heredoc.Doc(`
		Prints the configuration to stderr (caution: setting this may
		expose sensitive data when helm-repo-extra-args contains passwords)`))
	flags.Bool("exclude-deprecated", false, "Skip charts that are marked as deprecated")
	flags.Bool("github-groups", false, heredoc.Doc(`
		Change the delimiters for github to create collapsible groups
		for command output`))
	flags.Bool("use-helmignore", false, "Use .helmignore when identifying changed charts")
}

func addCommonLintAndInstallFlags(flags *pflag.FlagSet) {
	addCommonFlags(flags)
	flags.Bool("all", false, heredoc.Doc(`
		Process all charts except those explicitly excluded.
		Disables changed charts detection and version increment checking`))
	flags.StringSlice("charts", []string{}, heredoc.Doc(`
		Specific charts to test. Disables changed charts detection and
		version increment checking. May be specified multiple times
		or separate values with commas`))
	flags.StringSlice("chart-repos", []string{}, heredoc.Doc(`
		Additional chart repositories for dependency resolutions.
		Repositories should be formatted as 'name=url' (ex: local=http://127.0.0.1:8879/charts).
		May be specified multiple times or separate values with commas`))
	flags.String("helm-extra-args", "", heredoc.Doc(`
		Additional arguments for Helm. Must be passed as a single quoted string
		(e.g. '--timeout 500s')`))
	flags.String("helm-lint-extra-args", "", heredoc.Doc(`
		Additional arguments for Helm lint subcommand. Must be passed as a single quoted string
		(e.g. '--quiet')`))
	flags.StringSlice("helm-repo-extra-args", []string{}, heredoc.Doc(`
		Additional arguments for the 'helm repo add' command to be
		specified on a per-repo basis with an equals sign as delimiter
		(e.g. 'myrepo=--username test --password secret'). May be specified
		multiple times or separate values with commas`))
	flags.StringSlice("helm-dependency-extra-args", []string{}, heredoc.Doc(`
		Additional arguments for 'helm dependency build' (e.g. ["--skip-refresh"]`))
	flags.Bool("debug", false, heredoc.Doc(`
		Print CLI calls of external tools to stdout (caution: setting this may
		expose sensitive data when helm-repo-extra-args contains passwords)`))
}
```

## File: `ct/cmd/version.go`
```go
// Copyright The Helm Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

var (
	// GitCommit is updated with the Git tag by the Goreleaser build
	GitCommit = "unknown"
	// BuildDate is updated with the current ISO timestamp by the Goreleaser build
	BuildDate = "unknown"
	// Version is updated with the latest tag by the Goreleaser build
	Version = "unreleased"
)

func newVersionCmd() *cobra.Command {
	return &cobra.Command{
		Use:   "version",
		Short: "Print version information",
		Run:   version,
	}
}

func version(_ *cobra.Command, _ []string) {
	fmt.Println("Version:\t", Version)
	fmt.Println("Git commit:\t", GitCommit)
	fmt.Println("Date:\t\t", BuildDate)
	fmt.Println("License:\t Apache 2.0")
}
```

## File: `doc/ct.md`
```markdown
## ct

The Helm chart testing tool

### Synopsis

Lint and test

* changed charts
* specific charts
* all charts

in given chart directories.

### Options

```
  -h, --help   help for ct
```

### SEE ALSO

* [ct install](ct_install.md)	 - Install and test a chart
* [ct lint](ct_lint.md)	 - Lint and validate a chart
* [ct lint-and-install](ct_lint-and-install.md)	 - Lint, install, and test a chart
* [ct list-changed](ct_list-changed.md)	 - List changed charts
* [ct version](ct_version.md)	 - Print version information

```

## File: `doc/ct_install.md`
```markdown
## ct install

Install and test a chart

### Synopsis

Run 'helm install', 'helm test', and optionally 'helm upgrade' on

* changed charts (default)
* specific charts (--charts)
* all charts (--all)

in given chart directories. If upgrade (--upgrade) is true, then this
command will validate that 'helm test' passes for the following upgrade paths:

* previous chart revision => current chart version (if non-breaking SemVer change)
* current chart version => current chart version

Charts may have multiple custom values files matching the glob pattern
'*-values.yaml' in a directory named 'ci' in the root of the chart's
directory. The chart is installed and tested for each of these files.
If no custom values file is present, the chart is installed and
tested with defaults.

```
ct install [flags]
```

### Options

```
      --all                                  Process all charts except those explicitly excluded.
                                             Disables changed charts detection and version increment checking
      --build-id string                      An optional, arbitrary identifier that is added to the name of the namespace a
                                             chart is installed into. In a CI environment, this could be the build number or
                                             the ID of a pull request. If not specified, the name of the chart is used
      --chart-dirs strings                   Directories containing Helm charts. May be specified multiple times
                                             or separate values with commas (default [charts])
      --chart-repos strings                  Additional chart repositories for dependency resolutions.
                                             Repositories should be formatted as 'name=url' (ex: local=http://127.0.0.1:8879/charts).
                                             May be specified multiple times or separate values with commas
      --charts strings                       Specific charts to test. Disables changed charts detection and
                                             version increment checking. May be specified multiple times
                                             or separate values with commas
      --config string                        Config file
      --debug                                Print CLI calls of external tools to stdout (caution: setting this may
                                             expose sensitive data when helm-repo-extra-args contains passwords)
      --exclude-deprecated                   Skip charts that are marked as deprecated
      --excluded-charts strings              Charts that should be skipped. May be specified multiple times
                                             or separate values with commas
      --github-groups                        Change the delimiters for github to create collapsible groups
                                             for command output
      --helm-dependency-extra-args strings   Additional arguments for 'helm dependency build' (e.g. ["--skip-refresh"]
      --helm-extra-args string               Additional arguments for Helm. Must be passed as a single quoted string
                                             (e.g. '--timeout 500s')
      --helm-extra-set-args string           Additional arguments for Helm. Must be passed as a single quoted string
                                             (e.g. "--set=name=value"
      --helm-lint-extra-args string          Additional arguments for Helm lint subcommand. Must be passed as a single quoted string
                                             (e.g. '--quiet')
      --helm-repo-extra-args strings         Additional arguments for the 'helm repo add' command to be
                                             specified on a per-repo basis with an equals sign as delimiter
                                             (e.g. 'myrepo=--username test --password secret'). May be specified
                                             multiple times or separate values with commas
  -h, --help                                 help for install
      --namespace string                     Namespace to install the release(s) into. If not specified, each release will be
                                             installed in its own randomly generated namespace
      --print-config                         Prints the configuration to stderr (caution: setting this may
                                             expose sensitive data when helm-repo-extra-args contains passwords)
      --release-label string                 The label to be used as a selector when inspecting resources created by charts.
                                             This is only used if namespace is specified (default "app.kubernetes.io/instance")
      --release-name string                  Name for the release. If not specified, is set to the chart name and a random 
                                             identifier.
      --remote string                        The name of the Git remote used to identify changed charts (default "origin")
      --since string                         The Git reference used to identify changed charts (default "HEAD")
      --skip-clean-up                        Skip resources clean-up. Used if need to continue other flows or keep it around.
      --skip-missing-values                  When --upgrade has been passed, this flag will skip testing CI values files from the
                                             previous chart revision if they have been deleted or renamed at the current chart
                                             revision
      --target-branch string                 The name of the target branch used to identify changed charts (default "main")
      --upgrade                              Whether to test an in-place upgrade of each chart from its previous revision if the
                                             current version should not introduce a breaking change according to the SemVer spec
      --use-helmignore                       Use .helmignore when identifying changed charts
```

### SEE ALSO

* [ct](ct.md)	 - The Helm chart testing tool

```

## File: `doc/ct_lint-and-install.md`
```markdown
## ct lint-and-install

Lint, install, and test a chart

### Synopsis

Combines 'lint' and 'install' commands.

```
ct lint-and-install [flags]
```

### Options

```
      --additional-commands strings          Additional commands to run per chart (default: [])
                                             Commands will be executed in the same order as provided in the list and will
                                             be rendered with go template before being executed.
                                             Example: "helm unittest --helm3 -f tests/*.yaml {{ .Path }}"
      --all                                  Process all charts except those explicitly excluded.
                                             Disables changed charts detection and version increment checking
      --build-id string                      An optional, arbitrary identifier that is added to the name of the namespace a
                                             chart is installed into. In a CI environment, this could be the build number or
                                             the ID of a pull request. If not specified, the name of the chart is used
      --chart-dirs strings                   Directories containing Helm charts. May be specified multiple times
                                             or separate values with commas (default [charts])
      --chart-repos strings                  Additional chart repositories for dependency resolutions.
                                             Repositories should be formatted as 'name=url' (ex: local=http://127.0.0.1:8879/charts).
                                             May be specified multiple times or separate values with commas
      --chart-yaml-schema string             The schema for chart.yml validation. If not specified, 'chart_schema.yaml'
                                             is searched in the current directory, '$HOME/.ct', and '/etc/ct', in
                                             that order.
      --charts strings                       Specific charts to test. Disables changed charts detection and
                                             version increment checking. May be specified multiple times
                                             or separate values with commas
      --check-version-increment              Activates a check for chart version increments (default true)
      --config string                        Config file
      --debug                                Print CLI calls of external tools to stdout (caution: setting this may
                                             expose sensitive data when helm-repo-extra-args contains passwords)
      --exclude-deprecated                   Skip charts that are marked as deprecated
      --excluded-charts strings              Charts that should be skipped. May be specified multiple times
                                             or separate values with commas
      --github-groups                        Change the delimiters for github to create collapsible groups
                                             for command output
      --helm-dependency-extra-args strings   Additional arguments for 'helm dependency build' (e.g. ["--skip-refresh"]
      --helm-extra-args string               Additional arguments for Helm. Must be passed as a single quoted string
                                             (e.g. '--timeout 500s')
      --helm-extra-set-args string           Additional arguments for Helm. Must be passed as a single quoted string
                                             (e.g. "--set=name=value"
      --helm-lint-extra-args string          Additional arguments for Helm lint subcommand. Must be passed as a single quoted string
                                             (e.g. '--quiet')
      --helm-repo-extra-args strings         Additional arguments for the 'helm repo add' command to be
                                             specified on a per-repo basis with an equals sign as delimiter
                                             (e.g. 'myrepo=--username test --password secret'). May be specified
                                             multiple times or separate values with commas
  -h, --help                                 help for lint-and-install
      --lint-conf string                     The config file for YAML linting. If not specified, 'lintconf.yaml'
                                             is searched in the current directory, '$HOME/.ct', and '/etc/ct', in
                                             that order
      --namespace string                     Namespace to install the release(s) into. If not specified, each release will be
                                             installed in its own randomly generated namespace
      --print-config                         Prints the configuration to stderr (caution: setting this may
                                             expose sensitive data when helm-repo-extra-args contains passwords)
      --release-label string                 The label to be used as a selector when inspecting resources created by charts.
                                             This is only used if namespace is specified (default "app.kubernetes.io/instance")
      --release-name string                  Name for the release. If not specified, is set to the chart name and a random 
                                             identifier.
      --remote string                        The name of the Git remote used to identify changed charts (default "origin")
      --since string                         The Git reference used to identify changed charts (default "HEAD")
      --skip-clean-up                        Skip resources clean-up. Used if need to continue other flows or keep it around.
      --skip-helm-dependencies               Skip running 'helm dependency build' before linting
      --skip-missing-values                  When --upgrade has been passed, this flag will skip testing CI values files from the
                                             previous chart revision if they have been deleted or renamed at the current chart
                                             revision
      --target-branch string                 The name of the target branch used to identify changed charts (default "main")
      --upgrade                              Whether to test an in-place upgrade of each chart from its previous revision if the
                                             current version should not introduce a breaking change according to the SemVer spec
      --use-helmignore                       Use .helmignore when identifying changed charts
      --validate-chart-schema                Enable schema validation of 'Chart.yaml' using Yamale (default true)
      --validate-maintainers                 Enable validation of maintainer account names in chart.yml.
                                             Works for GitHub, GitLab, and Bitbucket (default true)
      --validate-yaml                        Enable linting of 'Chart.yaml' and values files (default true)
```

### SEE ALSO

* [ct](ct.md)	 - The Helm chart testing tool

```

## File: `doc/ct_lint.md`
```markdown
## ct lint

Lint and validate a chart

### Synopsis

Run 'helm lint', version checking, YAML schema validation
on 'Chart.yaml', YAML linting on 'Chart.yaml' and 'values.yaml',
and maintainer validation on

* changed charts (default)
* specific charts (--charts)
* all charts (--all)

in given chart directories.

Charts may have multiple custom values files matching the glob pattern
'*-values.yaml' in a directory named 'ci' in the root of the chart's
directory. The chart is linted for each of these files. If no custom
values file is present, the chart is linted with defaults.

```
ct lint [flags]
```

### Options

```
      --additional-commands strings          Additional commands to run per chart (default: [])
                                             Commands will be executed in the same order as provided in the list and will
                                             be rendered with go template before being executed.
                                             Example: "helm unittest --helm3 -f tests/*.yaml {{ .Path }}"
      --all                                  Process all charts except those explicitly excluded.
                                             Disables changed charts detection and version increment checking
      --chart-dirs strings                   Directories containing Helm charts. May be specified multiple times
                                             or separate values with commas (default [charts])
      --chart-repos strings                  Additional chart repositories for dependency resolutions.
                                             Repositories should be formatted as 'name=url' (ex: local=http://127.0.0.1:8879/charts).
                                             May be specified multiple times or separate values with commas
      --chart-yaml-schema string             The schema for chart.yml validation. If not specified, 'chart_schema.yaml'
                                             is searched in the current directory, '$HOME/.ct', and '/etc/ct', in
                                             that order.
      --charts strings                       Specific charts to test. Disables changed charts detection and
                                             version increment checking. May be specified multiple times
                                             or separate values with commas
      --check-version-increment              Activates a check for chart version increments (default true)
      --config string                        Config file
      --debug                                Print CLI calls of external tools to stdout (caution: setting this may
                                             expose sensitive data when helm-repo-extra-args contains passwords)
      --exclude-deprecated                   Skip charts that are marked as deprecated
      --excluded-charts strings              Charts that should be skipped. May be specified multiple times
                                             or separate values with commas
      --github-groups                        Change the delimiters for github to create collapsible groups
                                             for command output
      --helm-dependency-extra-args strings   Additional arguments for 'helm dependency build' (e.g. ["--skip-refresh"]
      --helm-extra-args string               Additional arguments for Helm. Must be passed as a single quoted string
                                             (e.g. '--timeout 500s')
      --helm-lint-extra-args string          Additional arguments for Helm lint subcommand. Must be passed as a single quoted string
                                             (e.g. '--quiet')
      --helm-repo-extra-args strings         Additional arguments for the 'helm repo add' command to be
                                             specified on a per-repo basis with an equals sign as delimiter
                                             (e.g. 'myrepo=--username test --password secret'). May be specified
                                             multiple times or separate values with commas
  -h, --help                                 help for lint
      --lint-conf string                     The config file for YAML linting. If not specified, 'lintconf.yaml'
                                             is searched in the current directory, '$HOME/.ct', and '/etc/ct', in
                                             that order
      --print-config                         Prints the configuration to stderr (caution: setting this may
                                             expose sensitive data when helm-repo-extra-args contains passwords)
      --remote string                        The name of the Git remote used to identify changed charts (default "origin")
      --since string                         The Git reference used to identify changed charts (default "HEAD")
      --skip-helm-dependencies               Skip running 'helm dependency build' before linting
      --target-branch string                 The name of the target branch used to identify changed charts (default "main")
      --use-helmignore                       Use .helmignore when identifying changed charts
      --validate-chart-schema                Enable schema validation of 'Chart.yaml' using Yamale (default true)
      --validate-maintainers                 Enable validation of maintainer account names in chart.yml.
                                             Works for GitHub, GitLab, and Bitbucket (default true)
      --validate-yaml                        Enable linting of 'Chart.yaml' and values files (default true)
```

### SEE ALSO

* [ct](ct.md)	 - The Helm chart testing tool

```

## File: `doc/ct_list-changed.md`
```markdown
## ct list-changed

List changed charts

### Synopsis

"List changed charts based on configured charts directories,
"remote, and target branch

```
ct list-changed [flags]
```

### Options

```
      --chart-dirs strings        Directories containing Helm charts. May be specified multiple times
                                  or separate values with commas (default [charts])
      --config string             Config file
      --exclude-deprecated        Skip charts that are marked as deprecated
      --excluded-charts strings   Charts that should be skipped. May be specified multiple times
                                  or separate values with commas
      --github-groups             Change the delimiters for github to create collapsible groups
                                  for command output
  -h, --help                      help for list-changed
      --print-config              Prints the configuration to stderr (caution: setting this may
                                  expose sensitive data when helm-repo-extra-args contains passwords)
      --remote string             The name of the Git remote used to identify changed charts (default "origin")
      --since string              The Git reference used to identify changed charts (default "HEAD")
      --target-branch string      The name of the target branch used to identify changed charts (default "main")
      --use-helmignore            Use .helmignore when identifying changed charts
```

### SEE ALSO

* [ct](ct.md)	 - The Helm chart testing tool

```

## File: `doc/ct_version.md`
```markdown
## ct version

Print version information

```
ct version [flags]
```

### Options

```
  -h, --help   help for version
```

### SEE ALSO

* [ct](ct.md)	 - The Helm chart testing tool

```

## File: `etc/chart_schema.yaml`
```yaml
name: str()
home: str(required=False)
version: str()
apiVersion: str()
appVersion: any(str(), num(), required=False)
description: str(required=False)
keywords: list(str(), required=False)
sources: list(str(), required=False)
maintainers: list(include('maintainer'), required=False)
dependencies: list(include('dependency'), required=False)
icon: str(required=False)
engine: str(required=False)
condition: str(required=False)
tags: str(required=False)
deprecated: bool(required=False)
kubeVersion: str(required=False)
annotations: map(str(), str(), required=False)
type: str(required=False)
---
maintainer:
  name: str()
  email: str(required=False)
  url: str(required=False)
---
dependency:
  name: str()
  version: str()
  repository: str(required=False)
  condition: str(required=False)
  tags: list(str(), required=False)
  enabled: bool(required=False)
  import-values: list(any(str(), include('import-value')), required=False)
  alias: str(required=False)
---
import-value:
  child: str()
  parent: str()
```

## File: `etc/lintconf.yaml`
```yaml
---
rules:
  braces:
    min-spaces-inside: 0
    max-spaces-inside: 0
    min-spaces-inside-empty: -1
    max-spaces-inside-empty: -1
  brackets:
    min-spaces-inside: 0
    max-spaces-inside: 0
    min-spaces-inside-empty: -1
    max-spaces-inside-empty: -1
  colons:
    max-spaces-before: 0
    max-spaces-after: 1
  commas:
    max-spaces-before: 0
    min-spaces-after: 1
    max-spaces-after: 1
  comments:
    require-starting-space: true
    min-spaces-from-content: 2
  document-end: disable
  document-start: disable           # No --- to start a file
  empty-lines:
    max: 2
    max-start: 0
    max-end: 0
  hyphens:
    max-spaces-after: 1
  indentation:
    spaces: consistent
    indent-sequences: whatever      # - list indentation will handle both indentation and without
    check-multi-line-strings: false
  key-duplicates: enable
  line-length: disable              # Lines can be any length
  new-line-at-end-of-file: enable
  new-lines:
    type: unix
  trailing-spaces: enable
  truthy:
    level: warning
```

## File: `examples/docker-for-mac/my_test.sh`
```bash
#!/usr/bin/env bash

# Copyright The Helm Authors. All rights reserved.
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

set -o errexit
set -o nounset
set -o pipefail

readonly IMAGE_TAG=v3.14.0
readonly IMAGE_REPOSITORY="quay.io/helmpack/chart-testing"

main() {
    local testcontainer_id
    testcontainer_id=$(create_testcontainer)

    # shellcheck disable=SC2064
    trap "docker container rm --force $testcontainer_id > /dev/null" EXIT

    configure_kubectl "$testcontainer_id"
    run_test
}

lookup_apiserver_container_id() {
    docker container list --filter name=k8s_kube-apiserver --format '{{ .ID }}'
}

get_apiserver_arg() {
    local container_id="$1"
    local arg="$2"
    docker container inspect "$container_id" | jq -r ".[].Args[] | capture(\"$arg=(?<arg>.*)\") | .arg"
}

create_testcontainer() {
    docker container run --interactive --tty --detach \
        --volume "$(pwd):/workdir" --workdir /workdir \
        "$IMAGE_REPOSITORY:$IMAGE_TAG" cat
}

configure_kubectl() {
    local testcontainer_id="$1"

    local apiserver_id
    apiserver_id=$(lookup_apiserver_container_id)

    if [[ -z "$apiserver_id" ]]; then
        echo "ERROR: API-Server container not found. Make sure 'Show system containers' is enabled in Docker4Mac 'Preferences'!" >&2
        exit 1
    fi

    local ip
    ip=$(get_apiserver_arg "$apiserver_id" --advertise-address)

    local port
    port=$(get_apiserver_arg "$apiserver_id" --secure-port)

    docker cp "$HOME/.kube" "$testcontainer_id:/root/.kube"
    docker exec "$testcontainer_id" kubectl config set-cluster docker-desktop "--server=https://$ip:$port"
    docker exec "$testcontainer_id" kubectl config set-cluster docker-desktop --insecure-skip-tls-verify=true
    docker exec "$testcontainer_id" kubectl config use-context docker-desktop
}

run_test() {
    git remote add k8s https://github.com/helm/charts.git &> /dev/null || true
    git fetch k8s
    docker exec "$testcontainer_id" ct lint --chart-dirs stable,incubator --remote k8s
    docker exec "$testcontainer_id" ct install --chart-dirs stable,incubator --remote k8s
}

main
```

## File: `examples/gcp-cloud-build/cloudbuild.yaml`
```yaml
steps:

- name: 'gcr.io/cloud-builders/git'
  id: 'git-init'
  args: ['init']
  waitFor: ['-']

- name: 'gcr.io/cloud-builders/git'
  id: 'git-add-remote'
  args: ['remote', 'add', 'origin', 'git@github.com:github-account/charts-repo.git']
  waitFor: ['git-init']

- name: 'gcr.io/cloud-builders/kubectl'
  id: 'cluster-info'
  args: ['cluster-info']
  waitFor: ['git-add-remote']

- name: quay.io/helmpack/chart-testing
  id: 'lint-and-install-charts'
  entrypoint: 'ct'
  args: ['lint-and-install']
  waitFor: ['cluster-info']

options:
  env:
  - CLOUDSDK_COMPUTE_ZONE=cluster-location
  - CLOUDSDK_CONTAINER_CLUSTER=cluster-name

timeout:
  3600s
```

## File: `examples/gcp-cloud-build/README.md`
```markdown
# Chart testing example with Google Cloud Build

This example shows how to lint and test charts using [Google Cloud Build](https://cloud.google.com/cloud-build/)

Since Google Cloud Build will ignore copying over `.git` by default, you will need to initialize `git` and add a `remote`. This example assumes that there is a pre-existing GKE cluster with `helm` already installed.
```

## File: `examples/gke/Dockerfile`
```
# Copyright The Helm Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM quay.io/helmpack/chart-testing:v3.14.0

ENV PATH /google-cloud-sdk/bin:$PATH
ARG CLOUD_SDK_VERSION=221.0.0
RUN curl -LO "https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-$CLOUD_SDK_VERSION-linux-x86_64.tar.gz" && \
    tar xzf "google-cloud-sdk-$CLOUD_SDK_VERSION-linux-x86_64.tar.gz" && \
    rm "google-cloud-sdk-$CLOUD_SDK_VERSION-linux-x86_64.tar.gz" && \
    ln -s /lib /lib64 && \
    rm -rf /google-cloud-sdk/.install/.backup && \
    gcloud version

RUN gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud config set metrics/environment github_docker_image

WORKDIR /workdir
```

## File: `examples/gke/my_test.sh`
```bash
#!/usr/bin/env bash

# Copyright The Helm Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -o errexit
set -o nounset
set -o pipefail

readonly IMAGE_REPOSITORY="myrepo/chart-testing"
readonly IMAGE_TAG="v1.0.0"
readonly REPO_ROOT="${REPO_ROOT:-$(git rev-parse --show-toplevel)}"

main() {
    local config_container_id
    config_container_id=$(docker run -ti -d \
        -v "$GOOGLE_APPLICATION_CREDENTIALS:/service-account.json" \
        -v "$REPO_ROOT:/workdir" \
        -e "BUILD_ID=$PULL_NUMBER" \
        "$IMAGE_REPOSITORY:$IMAGE_TAG" cat)

    # shellcheck disable=SC2064
    trap "docker rm -f $config_container_id" EXIT

    docker exec "$config_container_id" gcloud auth activate-service-account --key-file /service-account.json
    docker exec "$config_container_id" gcloud container clusters get-credentials my-cluster --project my-project --zone us-west1-a
    docker exec "$config_container_id" kubectl cluster-info
    docker exec "$config_container_id" ct lint-and-install --chart-dirs stable,incubator
}

main
```

## File: `examples/kind/README.md`
```markdown
# Chart testing example with CircleCi and kind - `K`ubernetes `in` `D`ocker

`kind` is a tool for running local Kubernetes clusters using Docker container "nodes".

This example shows how to lint and test charts using CircleCi and [kind](https://github.com/kubernetes-sigs/kind).
It creates a cluster with a single control-plane node and one worker node.
The cluster configuration can be adjusted in [kind-config.yaml](test/kind-config.yaml). You can check for available configuration options in `kind` [docs](https://kind.sigs.k8s.io/brain/knowledge/docs_legacy/user/quick-start#configuring-your-kind-cluster)
```

## File: `examples/kind/test/ct.yaml`
```yaml
helm-extra-args: --timeout 800s
```

## File: `examples/kind/test/e2e-kind.sh`
```bash
#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

readonly CT_VERSION=v3.14.0
readonly KIND_VERSION=v0.12.0
readonly CLUSTER_NAME=chart-testing
readonly K8S_VERSION=v1.22.7

run_ct_container() {
    echo 'Running ct container...'
    docker run --rm --interactive --detach --network host --name ct \
        --volume "$(pwd)/test/ct.yaml:/etc/ct/ct.yaml" \
        --volume "$(pwd):/workdir" \
        --workdir /workdir \
        "quay.io/helmpack/chart-testing:$CT_VERSION" \
        cat
    echo
}

cleanup() {
    echo 'Removing ct container...'
    docker kill ct > /dev/null 2>&1

    echo 'Done!'
}

docker_exec() {
    docker exec --interactive ct "$@"
}

create_kind_cluster() {
    echo 'Installing kind...'

    curl -sSLo kind "https://github.com/kubernetes-sigs/kind/releases/download/$KIND_VERSION/kind-linux-amd64"
    chmod +x kind
    sudo mv kind /usr/local/bin/kind

    kind create cluster --name "$CLUSTER_NAME" --config test/kind-config.yaml --image "kindest/node:$K8S_VERSION" --wait 60s

    echo 'Copying kubeconfig to container...'
    docker_exec mkdir /root/.kube
    docker cp /root/.kube/kind-config ct:/root/.kube/config

    docker_exec kubectl cluster-info
    echo

    docker_exec kubectl get nodes
    echo

    echo 'Cluster ready!'
    echo
}

install_charts() {
    docker_exec ct install
    echo
}

main() {
    run_ct_container
    trap cleanup EXIT

    create_kind_cluster
    install_charts
}

main
```

## File: `examples/kind/test/kind-config.yaml`
```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
```

## File: `examples/kind/test/local-path-provisioner.yaml`
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: local-path-storage
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: local-path-provisioner-service-account
  namespace: local-path-storage
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRole
metadata:
  name: local-path-provisioner-role
  namespace: local-path-storage
rules:
- apiGroups: [""]
  resources: ["nodes", "persistentvolumeclaims"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["endpoints", "persistentvolumes", "pods"]
  verbs: ["*"]
- apiGroups: [""]
  resources: ["events"]
  verbs: ["create", "patch"]
- apiGroups: ["storage.k8s.io"]
  resources: ["storageclasses"]
  verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: local-path-provisioner-bind
  namespace: local-path-storage
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: local-path-provisioner-role
subjects:
- kind: ServiceAccount
  name: local-path-provisioner-service-account
  namespace: local-path-storage
---
apiVersion: apps/v1beta2
kind: Deployment
metadata:
  name: local-path-provisioner
  namespace: local-path-storage
spec:
  replicas: 1
  selector:
    matchLabels:
      app: local-path-provisioner
  template:
    metadata:
      labels:
        app: local-path-provisioner
    spec:
      serviceAccountName: local-path-provisioner-service-account
      containers:
      - name: local-path-provisioner
        image: rancher/local-path-provisioner:v0.0.11
        imagePullPolicy: Always
        command:
        - local-path-provisioner
        - --debug
        - start
        - --config
        - /etc/config/config.json
        volumeMounts:
        - name: config-volume
          mountPath: /etc/config/
        env:
        - name: POD_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
      volumes:
        - name: config-volume
          configMap:
            name: local-path-config
---
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-path
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: rancher.io/local-path
volumeBindingMode: WaitForFirstConsumer
reclaimPolicy: Delete
---
kind: ConfigMap
apiVersion: v1
metadata:
  name: local-path-config
  namespace: local-path-storage
data:
  config.json: |-
        {
                "nodePathMap":[
                {
                        "node":"DEFAULT_PATH_FOR_NON_LISTED_NODES",
                        "paths":["/opt/local-path-provisioner"]
                }
                ]
        }
```

## File: `pkg/chart/chart.go`
```go
// Copyright The Helm Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package chart

import (
	"errors"
	"fmt"
	"os"
	"path/filepath"
	"strings"

	"github.com/Masterminds/semver"
	helmignore "helm.sh/helm/v3/pkg/ignore"

	"github.com/helm/chart-testing/v3/pkg/config"
	"github.com/helm/chart-testing/v3/pkg/exec"
	"github.com/helm/chart-testing/v3/pkg/ignore"
	"github.com/helm/chart-testing/v3/pkg/tool"
	"github.com/helm/chart-testing/v3/pkg/util"
)

const maxNameLength = 63

// Git is the Interface that wraps Git operations.
//
// FileExistsOnBranch checks whether file exists on the specified remote/branch.
//
// Show returns the contents of file on the specified remote/branch.
//
// AddWorktree checks out the contents of the repository at a commit ref into the specified path.
//
// RemoveWorktree removes the working tree at the specified path.
//
// MergeBase returns the SHA1 of the merge base of commit1 and commit2.
//
// ListChangedFilesInDirs diffs commit against HEAD and returns changed files for the specified dirs.
//
// GetURLForRemote returns the repo URL for the specified remote.
//
// ValidateRepository checks that the current working directory is a valid git repository,
// and returns nil if valid.
//
// BranchExists checks whether a given branch exists in the git repository.
type Git interface {
	FileExistsOnBranch(file string, remote string, branch string) bool
	Show(file string, remote string, branch string) (string, error)
	AddWorktree(path string, ref string) error
	RemoveWorktree(path string) error
	MergeBase(commit1 string, commit2 string) (string, error)
	ListChangedFilesInDirs(commit string, dirs ...string) ([]string, error)
	GetURLForRemote(remote string) (string, error)
	ValidateRepository() error
	BranchExists(branch string) bool
}

// Helm is the interface that wraps Helm operations
//
// # AddRepo adds a chart repository to the local Helm configuration
//
// # BuildDependencies builds the chart's dependencies
//
// # BuildDependenciesWithArgs allows passing additional arguments to BuildDependencies
//
// LintWithValues runs `helm lint` for the given chart using the specified values file.
// Pass a zero value for valuesFile in order to run lint without specifying a values file.
//
// InstallWithValues runs `helm install` for the given chart using the specified values file.
// Pass a zero value for valuesFile in order to run install without specifying a values file.
//
// UpgradeWithValues runs `helm upgrade` against an existing release using the specified values file.
// Pass a zero value for valuesFile in order to run install without specifying a values file.
//
// Test runs `helm test` against an existing release. Set the cleanup argument to true in order
// to clean up test pods created by helm after the test command completes.
//
// DeleteRelease purges the specified Helm release.
type Helm interface {
	AddRepo(name string, url string, extraArgs []string) error
	BuildDependencies(chart string) error
	BuildDependenciesWithArgs(chart string, extraArgs []string) error
	LintWithValues(chart string, valuesFile string) error
	InstallWithValues(chart string, valuesFile string, namespace string, release string) error
	UpgradeWithValues(chart string, valuesFile string, namespace string, release string) error
	Test(namespace string, release string) error
	DeleteRelease(namespace string, release string)
	Version() (string, error)
}

// Kubectl is the interface that wraps kubectl operations
//
// # DeleteNamespace deletes a namespace
//
// # WaitForDeployments waits for a deployment to become ready
//
// # GetPodsforDeployment gets all pods for a deployment
//
// # GetPods gets pods for the given args
//
// # GetEvents prints all events for namespace
//
// # DescribePod prints the pod's description
//
// # Logs prints the logs of container
//
// # GetInitContainers gets all init containers of pod
//
// GetContainers gets all containers of pod
type Kubectl interface {
	CreateNamespace(namespace string) error
	DeleteNamespace(namespace string)
	WaitForDeployments(namespace string, selector string) error
	GetPodsforDeployment(namespace string, deployment string) ([]string, error)
	GetPods(args ...string) ([]string, error)
	GetEvents(namespace string) error
	DescribePod(namespace string, pod string) error
	Logs(namespace string, pod string, container string) error
	GetInitContainers(namespace string, pod string) ([]string, error)
	GetContainers(namespace string, pod string) ([]string, error)
}

// Linter is the interface that wrap linting operations
//
// # YamlLint runs `yamllint` on the specified file with the specified configuration
//
// Yamale runs `yamale` on the specified file with the specified schema file
type Linter interface {
	YamlLint(yamlFile string, configFile string) error
	Yamale(yamlFile string, schemaFile string) error
}

// CmdExecutor is the interface
//
// RunCommand renders cmdTemplate as go template using data and executes the resulting command
type CmdExecutor interface {
	RunCommand(cmdTemplate string, data interface{}) error
}

// DirectoryLister is the interface
//
// ListChildDirs lists direct child directories of parentDir given they pass the test function
type DirectoryLister interface {
	ListChildDirs(parentDir string, test func(string) bool) ([]string, error)
}

// Utils is the interface that wraps chart-related methods
//
// LookupChartDir looks up the chart's root directory based on some chart file that has changed
type Utils interface {
	LookupChartDir(chartDirs []string, dir string) (string, error)
}

// AccountValidator is the interface that wraps Git account validation
//
// Validate checks if account is valid on repoDomain
type AccountValidator interface {
	Validate(repoDomain string, account string) error
}

// Chart represents a Helm chart, and can be initialized with the NewChart method.
type Chart struct {
	path          string
	yaml          *util.ChartYaml
	ciValuesPaths []string
}

// Yaml returns the Chart metadata
func (c *Chart) Yaml() *util.ChartYaml {
	return c.yaml
}

// Path returns the chart's directory path
func (c *Chart) Path() string {
	return c.path
}

func (c *Chart) String() string {
	return fmt.Sprintf(`%s => (version: "%s", path: "%s")`, c.yaml.Name, c.yaml.Version, c.Path())
}

// ValuesFilePathsForCI returns all file paths in the 'ci' subfolder of the chart directory matching the pattern '*-values.yaml'
func (c *Chart) ValuesFilePathsForCI() []string {
	return c.ciValuesPaths
}

// HasCIValuesFile checks whether a given CI values file is present.
func (c *Chart) HasCIValuesFile(path string) bool {
	fileName := filepath.Base(path)
	for _, file := range c.ValuesFilePathsForCI() {
		if fileName == filepath.Base(file) {
			return true
		}
	}
	return false
}

// CreateInstallParams generates a randomized release name and namespace based on the chart path
// and optional buildID. If release_name is specified, the release name is set to that string instead.
// If a buildID is specified, it will be part of the generated namespace.
func (c *Chart) CreateInstallParams(buildID string, releaseName string) (release string, namespace string) {
	release = filepath.Base(c.Path())
	if release == "." || release == "/" {
		if releaseName != "" {
			release = releaseName
		} else {
			yaml := c.Yaml()
			release = yaml.Name
		}
	}
	namespace = release
	if buildID != "" {
		namespace = fmt.Sprintf("%s-%s", namespace, buildID)
	}
	randomSuffix := util.RandomString(10)
	release = util.SanitizeName(fmt.Sprintf("%s-%s", release, randomSuffix), maxNameLength)
	namespace = util.SanitizeName(fmt.Sprintf("%s-%s", namespace, randomSuffix), maxNameLength)
	return
}

// NewChart parses the path to a chart directory and allocates a new Chart object. If chartPath is
// not a valid chart directory an error is returned.
func NewChart(chartPath string) (*Chart, error) {
	yaml, err := util.ReadChartYaml(chartPath)
	if err != nil {
		return nil, err
	}
	matches, _ := filepath.Glob(filepath.Join(chartPath, "ci", "*-values.yaml"))
	return &Chart{chartPath, yaml, matches}, nil
}

type Testing struct {
	config                   config.Configuration
	helm                     Helm
	kubectl                  Kubectl
	git                      Git
	linter                   Linter
	cmdExecutor              CmdExecutor
	accountValidator         AccountValidator
	directoryLister          DirectoryLister
	utils                    Utils
	previousRevisionWorktree string
	loadRules                func(string) (*helmignore.Rules, error)
}

// TestResults holds results and overall status
type TestResults struct {
	OverallSuccess bool
	TestResults    []TestResult
}

// TestResult holds test results for a specific chart
type TestResult struct {
	Chart *Chart
	Error error
}

// NewTesting creates a new Testing struct with the given config.
func NewTesting(config config.Configuration) (Testing, error) {
	procExec := exec.NewProcessExecutor(config.Debug)
	helmExtraArgs := strings.Fields(config.HelmExtraArgs)
	helmExtraSetArgs := strings.Fields(config.HelmExtraSetArgs)
	helmLintExtraArgs := strings.Fields(config.HelmLintExtraArgs)

	testing := Testing{
		config:           config,
		helm:             tool.NewHelm(procExec, helmExtraArgs, helmLintExtraArgs, helmExtraSetArgs),
		git:              tool.NewGit(procExec),
		kubectl:          tool.NewKubectl(procExec, config.KubectlTimeout),
		linter:           tool.NewLinter(procExec),
		cmdExecutor:      tool.NewCmdTemplateExecutor(procExec),
		accountValidator: tool.AccountValidator{},
		directoryLister:  util.DirectoryLister{},
		utils:            util.Utils{},
		loadRules:        ignore.LoadRules,
	}

	versionString, err := testing.helm.Version()
	if err != nil {
		return testing, err
	}

	version, err := semver.NewVersion(versionString)
	if err != nil {
		return testing, err
	}

	if version.Major() < 3 {
		return testing, fmt.Errorf("minimum required Helm version is v3.0.0; found: %s", version)
	}
	return testing, nil
}

// computePreviousRevisionPath converts any file or directory path to the same path in the
// previous revision's working tree.
func (t *Testing) computePreviousRevisionPath(fileOrDirPath string) string {
	return filepath.Join(t.previousRevisionWorktree, fileOrDirPath)
}

func (t *Testing) processCharts(action func(chart *Chart) TestResult) ([]TestResult, error) {
	var results []TestResult // nolint: prealloc
	chartDirs, err := t.FindChartDirsToBeProcessed()
	if err != nil {
		return nil, fmt.Errorf("failed identifying charts to process: %w", err)
	} else if len(chartDirs) == 0 {
		return results, nil
	}

	var charts []*Chart
	for _, dir := range chartDirs {
		chart, err := NewChart(dir)
		if err != nil {
			return nil, err
		}

		if t.config.ExcludeDeprecated && chart.yaml.Deprecated {
			fmt.Printf("Chart %q is deprecated and will be ignored because '--exclude-deprecated' is set\n", chart.String())
		} else {
			charts = append(charts, chart)
		}
	}

	if !t.config.GithubGroups {
		fmt.Println()
		util.PrintDelimiterLineToWriter(os.Stdout, "-")
		fmt.Println(" Charts to be processed:")
		util.PrintDelimiterLineToWriter(os.Stdout, "-")
	} else {
		util.GithubGroupsBegin(os.Stdout, "Charts to be processed")
	}
	for _, chart := range charts {
		fmt.Printf(" %s\n", chart)
	}
	if !t.config.GithubGroups {
		util.PrintDelimiterLineToWriter(os.Stdout, "-")
		fmt.Println()
	} else {
		util.GithubGroupsEnd(os.Stdout)
	}

	repoArgs := map[string][]string{}

	for _, repo := range t.config.HelmRepoExtraArgs {
		repoSlice := strings.SplitN(repo, "=", 2)
		name := repoSlice[0]
		repoExtraArgs := strings.Fields(repoSlice[1])
		repoArgs[name] = repoExtraArgs
	}

	for _, repo := range t.config.ChartRepos {
		repoSlice := strings.SplitN(repo, "=", 2)
		name := repoSlice[0]
		url := repoSlice[1]

		repoExtraArgs := repoArgs[name]
		if err := t.helm.AddRepo(name, url, repoExtraArgs); err != nil {
			return nil, fmt.Errorf("failed adding repo: %s=%s: %w", name, url, err)
		}
	}

	testResults := TestResults{
		OverallSuccess: true,
		TestResults:    results,
	}

	// Checkout previous chart revisions and build their dependencies
	if t.config.Upgrade {
		mergeBase, err := t.computeMergeBase()
		if err != nil {
			return results, fmt.Errorf("failed identifying merge base: %w", err)
		}
		// Add worktree for the target revision
		worktreePath, err := os.MkdirTemp("./", "ct-previous-revision")
		if err != nil {
			return results, fmt.Errorf("could not create previous revision directory: %w", err)
		}
		t.previousRevisionWorktree = worktreePath
		err = t.git.AddWorktree(worktreePath, mergeBase)
		if err != nil {
			return results, fmt.Errorf("could not create worktree for previous revision: %w", err)
		}
		defer t.git.RemoveWorktree(worktreePath) // nolint: errcheck

		if !t.config.SkipHelmDependencies {
			for _, chart := range charts {
				if err := t.helm.BuildDependenciesWithArgs(t.computePreviousRevisionPath(chart.Path()), t.config.HelmDependencyExtraArgs); err != nil {
					// Only print error (don't exit) if building dependencies for previous revision fails.
					fmt.Printf("failed building dependencies for previous revision of chart %q: %v\n", chart, err.Error())
				}
			}
		}
	}

	for _, chart := range charts {
		if !t.config.SkipHelmDependencies {
			if err := t.helm.BuildDependenciesWithArgs(chart.Path(), t.config.HelmDependencyExtraArgs); err != nil {
				return nil, fmt.Errorf("failed building dependencies for chart %q: %w", chart, err)
			}
		}

		result := action(chart)
		if result.Error != nil {
			testResults.OverallSuccess = false
		}
		results = append(results, result)
	}
	if testResults.OverallSuccess {
		return results, nil
	}

	return results, fmt.Errorf("failed processing charts")
}

// LintCharts lints charts (changed, all, specific) depending on the configuration.
func (t *Testing) LintCharts() ([]TestResult, error) {
	return t.processCharts(t.LintChart)
}

// InstallCharts install charts (changed, all, specific) depending on the configuration.
func (t *Testing) InstallCharts() ([]TestResult, error) {
	return t.processCharts(t.InstallChart)
}

// LintAndInstallCharts first lints and then installs charts (changed, all, specific) depending on the configuration.
func (t *Testing) LintAndInstallCharts() ([]TestResult, error) {
	return t.processCharts(t.LintAndInstallChart)
}

// PrintResults writes test results to stdout.
func (t *Testing) PrintResults(results []TestResult) {
	if !t.config.GithubGroups {
		fmt.Println()
		util.PrintDelimiterLineToWriter(os.Stdout, "-")
	} else {
		util.GithubGroupsBegin(os.Stdout, "Test Results")
	}
	if results != nil {
		for _, result := range results {
			err := result.Error
			if err != nil {
				fmt.Printf(" %s %s > %s\n", "✖︎", result.Chart, err)
			} else {
				fmt.Printf(" %s %s\n", "✔︎", result.Chart)
			}
		}
	} else {
		fmt.Println("No chart changes detected.")
	}
	if !t.config.GithubGroups {
		util.PrintDelimiterLineToWriter(os.Stdout, "-")
	} else {
		util.GithubGroupsEnd(os.Stdout)
	}
}

// LintChart lints the specified chart.
func (t *Testing) LintChart(chart *Chart) TestResult {
	fmt.Printf("Linting chart %q\n", chart)

	result := TestResult{Chart: chart}

	if t.config.CheckVersionIncrement {
		if err := t.CheckVersionIncrement(chart); err != nil {
			result.Error = err
			return result
		}
	}

	chartYaml := filepath.Join(chart.Path(), "Chart.yaml")
	valuesYaml := filepath.Join(chart.Path(), "values.yaml")
	valuesFiles := chart.ValuesFilePathsForCI()

	if t.config.ValidateChartSchema {
		if err := t.linter.Yamale(chartYaml, t.config.ChartYamlSchema); err != nil {
			result.Error = err
			return result
		}
	}

	if t.config.ValidateYaml {
		yamlFiles := append([]string{chartYaml, valuesYaml}, valuesFiles...)
		for _, yamlFile := range yamlFiles {
			if err := t.linter.YamlLint(yamlFile, t.config.LintConf); err != nil {
				result.Error = err
				return result
			}
		}
	}

	if t.config.ValidateMaintainers {
		if err := t.ValidateMaintainers(chart); err != nil {
			result.Error = err
			return result
		}
	}

	for _, cmd := range t.config.AdditionalCommands {
		if err := t.cmdExecutor.RunCommand(cmd, chart); err != nil {
			result.Error = err
			return result
		}
	}

	// Lint with defaults if no values files are specified.
	if len(valuesFiles) == 0 {
		valuesFiles = append(valuesFiles, "")
	}

	for _, valuesFile := range valuesFiles {
		if valuesFile != "" {
			fmt.Printf("\nLinting chart with values file %q...\n\n", valuesFile)
		}
		if err := t.helm.LintWithValues(chart.Path(), valuesFile); err != nil {
			result.Error = err
			break
		}
	}

	return result
}

// InstallChart installs the specified chart into a new namespace, waits for resources to become ready, and eventually
// uninstalls it and deletes the namespace again.
func (t *Testing) InstallChart(chart *Chart) TestResult {
	var result TestResult

	if t.config.Upgrade {
		// Test upgrade from previous version
		result = t.UpgradeChart(chart)
		if result.Error != nil {
			return result
		}
		// Test upgrade of current version (related: https://github.com/helm/chart-testing/issues/19)
		if err := t.doUpgrade(chart, chart, true); err != nil {
			result.Error = err
			return result
		}
	}

	result = TestResult{Chart: chart}
	if err := t.doInstall(chart); err != nil {
		result.Error = err
	}

	return result
}

// UpgradeChart tests in-place upgrades of the specified chart relative to its previous revisions. If the
// initial install or helm test of a previous revision of the chart fails, that release is ignored and no
// error will be returned. If the latest revision of the chart introduces a potentially breaking change
// according to the SemVer specification, upgrade testing will be skipped.
func (t *Testing) UpgradeChart(chart *Chart) TestResult {
	result := TestResult{Chart: chart}

	breakingChangeAllowed, err := t.checkBreakingChangeAllowed(chart)

	if breakingChangeAllowed {
		if err != nil {
			fmt.Printf("Skipping upgrade test of %q because: %v\n", chart, err.Error())
		}
		return result
	} else if err != nil {
		fmt.Printf("Error comparing chart versions for %q\n", chart)
		result.Error = err
		return result
	}

	if oldChart, err := NewChart(t.computePreviousRevisionPath(chart.Path())); err == nil {
		result.Error = t.doUpgrade(oldChart, chart, false)
	}

	return result
}

func (t *Testing) doInstall(chart *Chart) error {
	fmt.Printf("Installing chart %q...\n", chart)
	valuesFiles := chart.ValuesFilePathsForCI()

	// Test with defaults if no values files are specified.
	if len(valuesFiles) == 0 {
		valuesFiles = append(valuesFiles, "")
	}

	for _, valuesFile := range valuesFiles {
		if valuesFile != "" {
			fmt.Printf("\nInstalling chart with values file %q...\n\n", valuesFile)
		}

		// Use anonymous function. Otherwise deferred calls would pile up
		// and be executed in reverse order after the loop.
		fun := func() error {
			namespace, release, releaseSelector, cleanup := t.generateInstallConfig(chart)
			if !t.config.SkipCleanUp {
				defer cleanup()
			}

			if t.config.Namespace == "" {
				if err := t.kubectl.CreateNamespace(namespace); err != nil {
					return err
				}
			}
			if err := t.helm.InstallWithValues(chart.Path(), valuesFile, namespace, release); err != nil {
				return err
			}
			return t.testRelease(namespace, release, releaseSelector)
		}

		if err := fun(); err != nil {
			return err
		}
	}

	return nil
}

func (t *Testing) doUpgrade(oldChart, newChart *Chart, oldChartMustPass bool) error {
	fmt.Printf("Testing upgrades of chart %q relative to previous revision %q...\n", newChart, oldChart)
	valuesFiles := oldChart.ValuesFilePathsForCI()
	if len(valuesFiles) == 0 {
		valuesFiles = append(valuesFiles, "")
	}
	for _, valuesFile := range valuesFiles {
		if valuesFile != "" {
			if t.config.SkipMissingValues && !newChart.HasCIValuesFile(valuesFile) {
				fmt.Printf("Upgrade testing for values file %q skipped because a corresponding values file was not found in %s/ci\n", valuesFile, newChart.Path())
				continue
			}
			fmt.Printf("\nInstalling chart %q with values file %q...\n\n", oldChart, valuesFile)
		}

		// Use anonymous function. Otherwise deferred calls would pile up
		// and be executed in reverse order after the loop.
		fun := func() error {
			namespace, release, releaseSelector, cleanup := t.generateInstallConfig(oldChart)
			if !t.config.SkipCleanUp {
				defer cleanup()
			}

			if t.config.Namespace == "" {
				if err := t.kubectl.CreateNamespace(namespace); err != nil {
					return err
				}
			}
			// Install previous version of chart. If installation fails, ignore this release.
			if err := t.helm.InstallWithValues(oldChart.Path(), valuesFile, namespace, release); err != nil {
				if oldChartMustPass {
					return err
				}
				fmt.Printf("Upgrade testing for release %q skipped because of previous revision installation error: %v\n", release, err.Error())
				return nil
			}
			if err := t.testRelease(namespace, release, releaseSelector); err != nil {
				if oldChartMustPass {
					return err
				}
				fmt.Printf("Upgrade testing for release %q skipped because of previous revision testing error: %v\n", release, err.Error())
				return nil
			}

			if err := t.helm.UpgradeWithValues(newChart.Path(), valuesFile, namespace, release); err != nil {
				return err
			}

			return t.testRelease(namespace, release, releaseSelector)
		}

		if err := fun(); err != nil {
			return err
		}
	}

	return nil
}

func (t *Testing) testRelease(namespace, release, releaseSelector string) error {
	if err := t.kubectl.WaitForDeployments(namespace, releaseSelector); err != nil {
		return err
	}

	return t.helm.Test(namespace, release)
}

func (t *Testing) generateInstallConfig(chart *Chart) (namespace, release, releaseSelector string, cleanup func()) {
	if t.config.Namespace != "" {
		namespace = t.config.Namespace
		release, _ = chart.CreateInstallParams(t.config.BuildID, t.config.ReleaseName)
		releaseSelector = fmt.Sprintf("%s=%s", t.config.ReleaseLabel, release)
		cleanup = func() {
			t.PrintEventsPodDetailsAndLogs(namespace, releaseSelector)
			t.helm.DeleteRelease(namespace, release)
		}
	} else {
		release, namespace = chart.CreateInstallParams(t.config.BuildID, t.config.ReleaseName)
		cleanup = func() {
			t.PrintEventsPodDetailsAndLogs(namespace, releaseSelector)
			t.helm.DeleteRelease(namespace, release)
			t.kubectl.DeleteNamespace(namespace)
		}
	}

	return
}

// LintAndInstallChart first lints and then installs the specified chart.
func (t *Testing) LintAndInstallChart(chart *Chart) TestResult {
	result := t.LintChart(chart)
	if result.Error != nil {
		return result
	}
	return t.InstallChart(chart)
}

// FindChartDirsToBeProcessed identifies charts to be processed depending on the configuration
// (changed charts, all charts, or specific charts).
func (t *Testing) FindChartDirsToBeProcessed() ([]string, error) {
	cfg := t.config
	if cfg.ProcessAllCharts {
		return t.ReadAllChartDirectories()
	} else if len(cfg.Charts) > 0 {
		return t.config.Charts, nil
	}
	return t.ComputeChangedChartDirectories()
}

func (t *Testing) computeMergeBase() (string, error) {
	err := t.git.ValidateRepository()
	if err != nil {
		return "", errors.New("must be in a git repository")
	}

	branch := fmt.Sprintf("%s/%s", t.config.Remote, t.config.TargetBranch)
	if !t.git.BranchExists(branch) {
		return "", fmt.Errorf("targetBranch '%s' does not exist", branch)
	}

	return t.git.MergeBase(branch, t.config.Since)
}

// ComputeChangedChartDirectories takes the merge base of HEAD and the configured remote and target branch and computes a
// slice of changed charts from that in the configured chart directories excluding those configured to be excluded.
func (t *Testing) ComputeChangedChartDirectories() ([]string, error) {
	cfg := t.config

	mergeBase, err := t.computeMergeBase()
	if err != nil {
		return nil, err
	}

	allChangedChartFiles, err := t.git.ListChangedFilesInDirs(mergeBase, cfg.ChartDirs...)
	if err != nil {
		return nil, fmt.Errorf("failed creating diff: %w", err)
	}

	changedChartFiles := map[string][]string{}
	for _, file := range allChangedChartFiles {
		pathElements := strings.SplitN(filepath.ToSlash(file), "/", 3)
		if len(pathElements) < 2 || util.StringSliceContains(cfg.ExcludedCharts, pathElements[1]) {
			continue
		}
		dir := filepath.Dir(file)
		// Make sure directory is really a chart directory
		chartDir, err := t.utils.LookupChartDir(cfg.ChartDirs, dir)
		chartDirElement := strings.Split(chartDir, "/")
		if err == nil {
			if len(chartDirElement) > 1 {
				chartDirName := chartDirElement[len(chartDirElement)-1]
				if util.StringSliceContains(cfg.ExcludedCharts, chartDirName) {
					continue
				}
			}
			changedChartFiles[chartDir] = append(changedChartFiles[chartDir], strings.TrimPrefix(file, chartDir+"/"))
		} else {
			fmt.Fprintf(os.Stderr, "Directory %q is not a valid chart directory. Skipping...\n", dir)
		}
	}

	changedChartDirs := []string{}
	if t.config.UseHelmignore {
		for chartDir, changedChartFiles := range changedChartFiles {
			rules, err := t.loadRules(chartDir)
			if err != nil {
				return nil, err
			}
			filteredChartFiles, err := ignore.FilterFiles(changedChartFiles, rules)
			if err != nil {
				return nil, err
			}
			if len(filteredChartFiles) > 0 {
				changedChartDirs = append(changedChartDirs, chartDir)
			}
		}
	} else {
		for chartDir := range changedChartFiles {
			changedChartDirs = append(changedChartDirs, chartDir)
		}
	}

	return changedChartDirs, nil
}

// ReadAllChartDirectories returns a slice of all charts in the configured chart directories except those
// configured to be excluded.
func (t *Testing) ReadAllChartDirectories() ([]string, error) {
	cfg := t.config

	var chartDirs []string
	for _, chartParentDir := range cfg.ChartDirs {
		dirs, err := t.directoryLister.ListChildDirs(chartParentDir,
			func(dir string) bool {
				_, err := t.utils.LookupChartDir(cfg.ChartDirs, dir)
				return err == nil && !util.StringSliceContains(cfg.ExcludedCharts, filepath.Base(dir))
			})
		if err != nil {
			return nil, fmt.Errorf("failed reading chart directories: %w", err)
		}
		chartDirs = append(chartDirs, dirs...)
	}

	return chartDirs, nil
}

// CheckVersionIncrement checks that the new chart version is greater than the old one using semantic version comparison.
func (t *Testing) CheckVersionIncrement(chart *Chart) error {
	fmt.Printf("Checking chart %q for a version bump...\n", chart)

	oldVersion, err := t.GetOldChartVersion(chart.Path())
	if err != nil {
		return err
	}
	if oldVersion == "" {
		// new chart, skip version check
		return nil
	}

	fmt.Println("Old chart version:", oldVersion)

	chartYaml := chart.Yaml()
	newVersion := chartYaml.Version
	fmt.Println("New chart version:", newVersion)

	result, err := util.CompareVersions(oldVersion, newVersion)
	if err != nil {
		return err
	}

	if result >= 0 {
		return errors.New("chart version not ok. Needs a version bump! ")
	}

	fmt.Println("Chart version ok.")
	return nil
}

func (t *Testing) checkBreakingChangeAllowed(chart *Chart) (allowed bool, err error) {
	oldVersion, err := t.GetOldChartVersion(chart.Path())
	if err != nil {
		return false, err
	}
	if oldVersion == "" {
		// new chart, skip upgrade check
		return true, fmt.Errorf("chart has no previous revision")
	}

	newVersion := chart.Yaml().Version

	return util.BreakingChangeAllowed(oldVersion, newVersion)
}

// GetOldChartVersion gets the version of the old Chart.yaml file from the target branch.
func (t *Testing) GetOldChartVersion(chartPath string) (string, error) {
	cfg := t.config

	chartYamlFile := filepath.Join(chartPath, "Chart.yaml")
	if !t.git.FileExistsOnBranch(chartYamlFile, cfg.Remote, cfg.TargetBranch) {
		fmt.Printf("Unable to find chart on %s. New chart detected.\n", cfg.TargetBranch)
		return "", nil
	}

	chartYamlContents, err := t.git.Show(chartYamlFile, cfg.Remote, cfg.TargetBranch)
	if err != nil {
		return "", fmt.Errorf("failed reading old Chart.yaml: %w", err)
	}

	chartYaml, err := util.UnmarshalChartYaml([]byte(chartYamlContents))
	if err != nil {
		return "", fmt.Errorf("failed reading old chart version: %w", err)
	}

	return chartYaml.Version, nil
}

// ValidateMaintainers validates maintainers in the Chart.yaml file. Maintainer names must be valid accounts
// (GitHub, Bitbucket, GitLab) names. Deprecated charts must not have maintainers.
func (t *Testing) ValidateMaintainers(chart *Chart) error {
	fmt.Println("Validating maintainers...")

	chartYaml := chart.Yaml()

	if chartYaml.Deprecated {
		if len(chartYaml.Maintainers) > 0 {
			return errors.New("deprecated chart must not have maintainers")
		}
		return nil
	}

	if len(chartYaml.Maintainers) == 0 {
		return errors.New("chart doesn't have maintainers")
	}

	repoURL, err := t.git.GetURLForRemote(t.config.Remote)
	if err != nil {
		return err
	}

	for _, maintainer := range chartYaml.Maintainers {
		if err := t.accountValidator.Validate(repoURL, maintainer.Name); err != nil {
			return err
		}
	}

	return nil
}

func (t *Testing) PrintEventsPodDetailsAndLogs(namespace string, selector string) {
	util.PrintDelimiterLineToWriter(os.Stdout, "=")

	t.printDetails(namespace, "Events of namespace", ".", func(_ string) error {
		return t.kubectl.GetEvents(namespace)
	}, namespace)

	pods, err := t.kubectl.GetPods(
		"--no-headers",
		"--namespace",
		namespace,
		"--selector",
		selector,
		"--output",
		"jsonpath={.items[*].metadata.name}",
	)
	if err != nil {
		fmt.Println("Error printing logs:", err)
		return
	}

	for _, pod := range pods {
		t.printDetails(pod, "Description of pod", "~", func(_ string) error {
			return t.kubectl.DescribePod(namespace, pod)
		}, pod)

		initContainers, err := t.kubectl.GetInitContainers(namespace, pod)
		if err != nil {
			fmt.Println("Error printing logs:", err)
			return
		}

		if t.config.PrintLogs {
			t.printDetails(pod, "Logs of init container", "-",
				func(item string) error {
					return t.kubectl.Logs(namespace, pod, item)
				}, initContainers...)

			containers, err := t.kubectl.GetContainers(namespace, pod)
			if err != nil {
				fmt.Printf("failed printing logs: %v\n", err.Error())
				return
			}

			t.printDetails(pod, "Logs of container", "-",
				func(item string) error {
					return t.kubectl.Logs(namespace, pod, item)
				},
				containers...)
		}
	}

	util.PrintDelimiterLineToWriter(os.Stdout, "=")
}

func (t *Testing) printDetails(resource string, text string, delimiterChar string, printFunc func(item string) error, items ...string) {
	for _, item := range items {
		item = strings.Trim(item, "'")

		if !t.config.GithubGroups {
			util.PrintDelimiterLineToWriter(os.Stdout, delimiterChar)
			fmt.Printf("==> %s %s\n", text, resource)
			util.PrintDelimiterLineToWriter(os.Stdout, delimiterChar)
		} else {
			util.GithubGroupsBegin(os.Stdout, fmt.Sprintf("%s %s", text, resource))
		}

		if err := printFunc(item); err != nil {
			fmt.Println("Error printing details:", err)
			return
		}

		if !t.config.GithubGroups {
			util.PrintDelimiterLineToWriter(os.Stdout, delimiterChar)
			fmt.Printf("<== %s %s\n", text, resource)
			util.PrintDelimiterLineToWriter(os.Stdout, delimiterChar)
		} else {
			util.GithubGroupsEnd(os.Stdout)
		}
	}
}
```

## File: `pkg/chart/chart_test.go`
```go
// Copyright The Helm Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package chart

import (
	"fmt"
	"strings"
	"testing"

	"github.com/helm/chart-testing/v3/pkg/config"
	"github.com/helm/chart-testing/v3/pkg/util"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"
	helmignore "helm.sh/helm/v3/pkg/ignore"
)

type fakeGit struct{}

func (g fakeGit) FileExistsOnBranch(_ string, _ string, _ string) bool {
	return true
}

func (g fakeGit) Show(_ string, _ string, _ string) (string, error) {
	return "", nil
}

func (g fakeGit) MergeBase(_ string, _ string) (string, error) {
	return "HEAD", nil
}

func (g fakeGit) ListChangedFilesInDirs(_ string, _ ...string) ([]string, error) {
	return []string{
		"test_charts/foo/Chart.yaml",
		"test_charts/bar/Chart.yaml",
		"test_charts/bar/bar_sub/templates/bar_sub.yaml",
		"test_charts/excluded/Chart.yaml",
		"test_chart_at_root/templates/foo.yaml",
		"test_chart_at_multi_level/foo/bar/Chart.yaml",
		"test_chart_at_multi_level/foo/baz/Chart.yaml",
		"test_chart_at_multi_level/foo/excluded/Chart.yaml",
		"some_non_chart_dir/some_non_chart_file",
		"some_non_chart_file",
	}, nil
}

func (g fakeGit) AddWorktree(_ string, _ string) error {
	return nil
}

func (g fakeGit) RemoveWorktree(_ string) error {
	return nil
}

func (g fakeGit) GetURLForRemote(_ string) (string, error) {
	return "git@github.com/helm/chart-testing", nil
}

func (g fakeGit) ValidateRepository() error {
	return nil
}

func (g fakeGit) BranchExists(_ string) bool {
	return true
}

type fakeAccountValidator struct{}

func (v fakeAccountValidator) Validate(_ string, account string) error {
	if strings.HasPrefix(account, "valid") {
		return nil
	}
	return fmt.Errorf("failed validating account: %s", account)
}

type fakeLinter struct {
	mock.Mock
}

func (l *fakeLinter) YamlLint(yamlFile, configFile string) error {
	l.Called(yamlFile, configFile)
	return nil
}
func (l *fakeLinter) Yamale(yamlFile, schemaFile string) error {
	l.Called(yamlFile, schemaFile)
	return nil
}

type fakeHelm struct {
	mock.Mock
}

func (h *fakeHelm) AddRepo(_, _ string, _ []string) error { return nil }
func (h *fakeHelm) BuildDependencies(_ string) error      { return nil }
func (h *fakeHelm) BuildDependenciesWithArgs(chart string, extraArgs []string) error {
	h.Called(chart, extraArgs)
	return nil
}
func (h *fakeHelm) LintWithValues(_ string, _ string) error { return nil }
func (h *fakeHelm) InstallWithValues(_ string, _ string, _ string, _ string) error {
	return nil
}
func (h *fakeHelm) UpgradeWithValues(_ string, _ string, _ string, _ string) error {
	return nil
}
func (h *fakeHelm) Test(_ string, _ string) error {
	return nil
}
func (h *fakeHelm) DeleteRelease(_ string, _ string) {}

func (h *fakeHelm) Version() (string, error) {
	return "v3.0.0", nil
}

type fakeCmdExecutor struct {
	mock.Mock
}

func (c *fakeCmdExecutor) RunCommand(cmdTemplate string, data interface{}) error {
	c.Called(cmdTemplate, data)
	return nil
}

var ct Testing

func init() {
	cfg := config.Configuration{
		ExcludedCharts: []string{"excluded"},
		ChartDirs:      []string{"test_charts", "."},
	}

	ct = newTestingMock(cfg)
}

func newTestingMock(cfg config.Configuration) Testing {
	fakeMockLinter := new(fakeLinter)
	return Testing{
		config:           cfg,
		directoryLister:  util.DirectoryLister{},
		git:              fakeGit{},
		utils:            util.Utils{},
		accountValidator: fakeAccountValidator{},
		linter:           fakeMockLinter,
		helm:             new(fakeHelm),
		loadRules: func(dir string) (*helmignore.Rules, error) {
			rules := helmignore.Empty()
			if dir == "test_charts/foo" {
				var err error
				rules, err = helmignore.Parse(strings.NewReader("Chart.yaml\n"))
				if err != nil {
					return nil, err
				}
				rules.AddDefaults()
			}
			if dir == "test_chart_at_multi_level/foo/baz" {
				var err error
				rules, err = helmignore.Parse(strings.NewReader("Chart.yaml\n"))
				if err != nil {
					return nil, err
				}
				rules.AddDefaults()
			}
			return rules, nil
		},
	}
}

func TestComputeChangedChartDirectories(t *testing.T) {
	actual, err := ct.ComputeChangedChartDirectories()
	expected := []string{"test_charts/foo", "test_charts/bar", "test_chart_at_root"}
	for _, chart := range actual {
		assert.Contains(t, expected, chart)
	}
	assert.Len(t, actual, 3)
	assert.Nil(t, err)
}

func TestComputeChangedChartDirectoriesWithHelmignore(t *testing.T) {
	cfg := config.Configuration{
		ExcludedCharts: []string{"excluded"},
		ChartDirs:      []string{"test_charts", "."},
		UseHelmignore:  true,
	}
	ct := newTestingMock(cfg)
	actual, err := ct.ComputeChangedChartDirectories()
	expected := []string{"test_charts/bar", "test_chart_at_root"}
	assert.Nil(t, err)
	assert.ElementsMatch(t, expected, actual)
}

func TestComputeChangedChartDirectoriesWithMultiLevelChart(t *testing.T) {
	cfg := config.Configuration{
		ExcludedCharts: []string{"excluded"},
		ChartDirs:      []string{"test_chart_at_multi_level/foo"},
	}
	ct := newTestingMock(cfg)
	actual, err := ct.ComputeChangedChartDirectories()
	expected := []string{"test_chart_at_multi_level/foo/bar", "test_chart_at_multi_level/foo/baz"}
	for _, chart := range actual {
		assert.Contains(t, expected, chart)
	}
	assert.Len(t, actual, 2)
	assert.Nil(t, err)
}

func TestComputeChangedChartDirectoriesWithMultiLevelChartWithHelmIgnore(t *testing.T) {
	cfg := config.Configuration{
		ExcludedCharts: []string{"excluded"},
		ChartDirs:      []string{"test_chart_at_multi_level/foo"},
		UseHelmignore:  true,
	}
	ct := newTestingMock(cfg)
	actual, err := ct.ComputeChangedChartDirectories()
	expected := []string{"test_chart_at_multi_level/foo/bar"}
	assert.Nil(t, err)
	assert.ElementsMatch(t, expected, actual)
}

func TestReadAllChartDirectories(t *testing.T) {
	actual, err := ct.ReadAllChartDirectories()
	expected := []string{
		"test_charts/foo",
		"test_charts/bar",
		"test_charts/must-pass-upgrade-install",
		"test_charts/mutating-deployment-selector",
		"test_charts/simple-deployment",
		"test_charts/simple-deployment-different-selector",
		"test_charts/mutating-sfs-volumeclaim",
		"test_chart_at_root",
	}
	for _, chart := range actual {
		assert.Contains(t, expected, chart)
	}
	assert.Len(t, actual, 8)
	assert.Nil(t, err)
}

func TestValidateMaintainers(t *testing.T) {
	var testDataSlice = []struct {
		name     string
		chartDir string
		expected bool
	}{
		{"valid", "testdata/valid_maintainers", true},
		{"invalid", "testdata/invalid_maintainers", false},
		{"no-maintainers", "testdata/no_maintainers", false},
		{"empty-maintainers", "testdata/empty_maintainers", false},
		{"valid-deprecated", "testdata/valid_maintainers_deprecated", false},
		{"no-maintainers-deprecated", "testdata/no_maintainers_deprecated", true},
	}

	for _, testData := range testDataSlice {
		t.Run(testData.name, func(t *testing.T) {
			chart, err := NewChart(testData.chartDir)
			assert.Nil(t, err)
			validationErr := ct.ValidateMaintainers(chart)
			assert.Equal(t, testData.expected, validationErr == nil)
		})
	}
}

func TestLintChartMaintainerValidation(t *testing.T) {
	type testData struct {
		name     string
		chartDir string
		expected bool
	}

	runTests := func(validate bool) {
		ct.config.ValidateMaintainers = validate

		var suffix string
		if validate {
			suffix = "with-validation"
		} else {
			suffix = "without-validation"
		}

		testCases := []testData{
			{fmt.Sprintf("maintainers-%s", suffix), "testdata/valid_maintainers", true},
			{fmt.Sprintf("no-maintainers-%s", suffix), "testdata/no_maintainers", !validate},
		}

		for _, testData := range testCases {
			t.Run(testData.name, func(t *testing.T) {
				chart, err := NewChart(testData.chartDir)
				assert.Nil(t, err)
				result := ct.LintChart(chart)
				assert.Equal(t, testData.expected, result.Error == nil)
			})
		}
	}

	runTests(true)
	runTests(false)
}

func TestLintChartSchemaValidation(t *testing.T) {
	type testData struct {
		name     string
		chartDir string
		expected bool
	}

	runTests := func(validate bool, callsYamlLint int, callsYamale int) {
		fakeMockLinter := new(fakeLinter)

		fakeMockLinter.On("Yamale", mock.Anything, mock.Anything).Return(true)
		fakeMockLinter.On("YamlLint", mock.Anything, mock.Anything).Return(true)

		ct.linter = fakeMockLinter
		ct.config.ValidateChartSchema = validate
		ct.config.ValidateMaintainers = false
		ct.config.ValidateYaml = false

		var suffix string
		if validate {
			suffix = "with-validation"
		} else {
			suffix = "without-validation"
		}

		testCases := []testData{
			{fmt.Sprintf("schema-%s", suffix), "testdata/test_lints", true},
		}

		for _, testData := range testCases {
			t.Run(testData.name, func(t *testing.T) {
				chart, err := NewChart(testData.chartDir)
				assert.Nil(t, err)
				result := ct.LintChart(chart)
				assert.Equal(t, testData.expected, result.Error == nil)
				fakeMockLinter.AssertNumberOfCalls(t, "Yamale", callsYamale)
				fakeMockLinter.AssertNumberOfCalls(t, "YamlLint", callsYamlLint)
			})
		}
	}

	runTests(true, 0, 1)
	runTests(false, 0, 0)
}

func TestLintYamlValidation(t *testing.T) {
	type testData struct {
		name     string
		chartDir string
		expected bool
	}

	runTests := func(validate bool, callsYamlLint int, callsYamale int) {
		fakeMockLinter := new(fakeLinter)

		fakeMockLinter.On("Yamale", mock.Anything, mock.Anything).Return(true)
		fakeMockLinter.On("YamlLint", mock.Anything, mock.Anything).Return(true)

		ct.linter = fakeMockLinter
		ct.config.ValidateYaml = validate
		ct.config.ValidateChartSchema = false
		ct.config.ValidateMaintainers = false

		var suffix string
		if validate {
			suffix = "with-validation"
		} else {
			suffix = "without-validation"
		}

		testCases := []testData{
			{fmt.Sprintf("lint-%s", suffix), "testdata/test_lints", true},
		}

		for _, testData := range testCases {
			t.Run(testData.name, func(t *testing.T) {
				chart, err := NewChart(testData.chartDir)
				assert.Nil(t, err)
				result := ct.LintChart(chart)
				assert.Equal(t, testData.expected, result.Error == nil)
				fakeMockLinter.AssertNumberOfCalls(t, "Yamale", callsYamale)
				fakeMockLinter.AssertNumberOfCalls(t, "YamlLint", callsYamlLint)
			})
		}
	}

	runTests(true, 2, 0)
	runTests(false, 0, 0)
}

func TestLintDependencyExtraArgs(t *testing.T) {
	chart := "testdata/test_lints"
	args := []string{"--skip-refresh"}

	fakeMockHelm := new(fakeHelm)
	ct.helm = fakeMockHelm
	ct.config.HelmDependencyExtraArgs = args
	ct.config.Charts = []string{chart}

	t.Run("lint-helm-dependency-extra-args", func(t *testing.T) {
		call := fakeMockHelm.On("BuildDependenciesWithArgs", chart, args).Return(nil)
		call.Repeatability = 1

		results, err := ct.LintCharts()
		assert.Nil(t, err)
		for _, result := range results {
			assert.Nil(t, result.Error)
		}
		// -1 is set after Repeatability runs out
		assert.Equal(t, -1, call.Repeatability)
	})
}

func TestGenerateInstallConfig(t *testing.T) {
	type testData struct {
		name  string
		cfg   config.Configuration
		chart *Chart
	}

	testCases := []testData{
		{
			"custom namespace",
			config.Configuration{
				Namespace:    "default",
				ReleaseLabel: "app.kubernetes.io/instance",
			},
			&Chart{
				yaml: &util.ChartYaml{
					Name: "bar",
				},
			},
		},
		{
			"random namespace",
			config.Configuration{
				ReleaseLabel: "app.kubernetes.io/instance",
			},
			&Chart{
				yaml: &util.ChartYaml{
					Name: "bar",
				},
			},
		},
		{
			"long chart name",
			config.Configuration{
				ReleaseLabel: "app.kubernetes.io/instance",
			},
			&Chart{
				yaml: &util.ChartYaml{
					Name: "test_charts/barbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbarbar",
				},
			},
		},
	}

	for _, testData := range testCases {
		t.Run(testData.name, func(t *testing.T) {
			ct := newTestingMock(testData.cfg)

			namespace, release, releaseSelector, _ := ct.generateInstallConfig(testData.chart)
			assert.NotEqual(t, "", namespace)
			assert.NotEqual(t, "", release)
			assert.True(t, len(release) < 64, "release should be less than 64 chars")
			assert.True(t, len(namespace) < 64, "namespace should be less than 64 chars")
			if testData.cfg.Namespace != "" {
				assert.Equal(t, testData.cfg.Namespace, namespace)
				assert.Equal(t, fmt.Sprintf("%s=%s", testData.cfg.ReleaseLabel, release), releaseSelector)
			} else {
				assert.Equal(t, "", releaseSelector)
				assert.Contains(t, namespace, release)
			}
		})
	}
}

func TestChart_HasCIValuesFile(t *testing.T) {
	type testData struct {
		name     string
		chart    *Chart
		file     string
		expected bool
	}

	testCases := []testData{
		{
			name: "has file",
			chart: &Chart{
				ciValuesPaths: []string{"foo-values.yaml"},
			},
			file:     "foo-values.yaml",
			expected: true,
		},
		{
			name: "different paths",
			chart: &Chart{
				ciValuesPaths: []string{"ci/foo-values.yaml"},
			},
			file:     "foo/bar/foo-values.yaml",
			expected: true,
		},
		{
			name: "does not have file",
			chart: &Chart{
				ciValuesPaths: []string{"foo-values.yaml"},
			},
			file:     "bar-values.yaml",
			expected: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			actual := tc.chart.HasCIValuesFile(tc.file)
			assert.Equal(t, tc.expected, actual)
		})
	}
}

func TestChart_AdditionalCommandsAreRun(t *testing.T) {
	type testData struct {
		name            string
		cfg             config.Configuration
		callsRunCommand int
	}

	testCases := []testData{
		{
			name:            "no additional commands",
			cfg:             config.Configuration{},
			callsRunCommand: 0,
		},
		{
			name: "one command",
			cfg: config.Configuration{
				AdditionalCommands: []string{"helm unittest --helm3 -f tests/*.yaml {{ .Path }}"},
			},
			callsRunCommand: 1,
		},
		{
			name: "multiple commands",
			cfg: config.Configuration{
				AdditionalCommands: []string{"echo", "helm unittest --helm3 -f tests/*.yaml {{ .Path }}"},
			},
			callsRunCommand: 2,
		},
	}

	for _, testData := range testCases {
		t.Run(testData.name, func(t *testing.T) {
			fakeCmdExecutor := new(fakeCmdExecutor)
			fakeCmdExecutor.On("RunCommand", mock.Anything, mock.Anything).Return(nil)

			ct := newTestingMock(testData.cfg)
			ct.cmdExecutor = fakeCmdExecutor

			ct.LintChart(&Chart{})

			fakeCmdExecutor.AssertNumberOfCalls(t, "RunCommand", testData.callsRunCommand)
		})
	}
}
```

## File: `pkg/chart/integration_test.go`
```go
// Copyright The Helm Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

//go:build integration
// +build integration

package chart

import (
	"fmt"
	"strings"
	"testing"
	"time"

	"github.com/helm/chart-testing/v3/pkg/config"
	"github.com/helm/chart-testing/v3/pkg/exec"
	"github.com/helm/chart-testing/v3/pkg/tool"
	"github.com/helm/chart-testing/v3/pkg/util"
	"github.com/stretchr/testify/assert"
)

func newTestingHelmIntegration(cfg config.Configuration, extraSetArgs string) Testing {
	fakeMockLinter := new(fakeLinter)
	procExec := exec.NewProcessExecutor(true)
	extraArgs := strings.Fields(cfg.HelmExtraArgs)
	extraLintArgs := strings.Fields(cfg.HelmLintExtraArgs)

	return Testing{
		config:           cfg,
		directoryLister:  util.DirectoryLister{},
		git:              fakeGit{},
		utils:            util.Utils{},
		accountValidator: fakeAccountValidator{},
		linter:           fakeMockLinter,
		helm:             tool.NewHelm(procExec, extraArgs, extraLintArgs, strings.Fields(extraSetArgs)),
		kubectl:          tool.NewKubectl(procExec, 30*time.Second),
	}
}

func TestInstallChart(t *testing.T) {
	type testCase struct {
		name     string
		cfg      config.Configuration
		chartDir string
		output   TestResult
		extraSet string
	}

	cases := []testCase{
		{
			"install only in custom namespace",
			config.Configuration{
				Debug:        true,
				Namespace:    "foobar",
				ReleaseLabel: "app.kubernetes.io/instance",
			},
			"test_charts/must-pass-upgrade-install",
			TestResult{mustNewChart("test_charts/must-pass-upgrade-install"), nil},
			"",
		},
		{
			"install only in random namespace",
			config.Configuration{
				Debug: true,
			},
			"test_charts/must-pass-upgrade-install",
			TestResult{mustNewChart("test_charts/must-pass-upgrade-install"), nil},
			"",
		},
		{
			"install with override set",
			config.Configuration{
				Debug: true,
			},
			"test_charts/must-pass-upgrade-install",
			TestResult{mustNewChart("test_charts/must-pass-upgrade-install"), nil},
			"--set=image.tag=latest",
		},
	}

	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			ct := newTestingHelmIntegration(tc.cfg, tc.extraSet)
			namespace := tc.cfg.Namespace
			if namespace != "" {
				ct.kubectl.CreateNamespace(namespace)
				defer ct.kubectl.DeleteNamespace(namespace)
			}
			result := ct.InstallChart(mustNewChart(tc.chartDir))

			if result.Error != tc.output.Error {
				if result.Error != nil && tc.output.Error != nil {
					assert.Equal(t, tc.output.Error.Error(), result.Error.Error())
				} else {
					assert.Equal(t, tc.output.Error, result.Error)
				}
			}
		})
	}
}

func TestUpgradeChart(t *testing.T) {
	type testCase struct {
		name string
		old  string
		new  string
		err  error
	}

	cfg := config.Configuration{
		Debug:   true,
		Upgrade: true,
	}
	ct := newTestingHelmIntegration(cfg, "")
	processError := fmt.Errorf("failed waiting for process: exit status 1")

	cases := []testCase{
		{
			"upgrade nginx",
			"test_charts/must-pass-upgrade-install",
			"test_charts/must-pass-upgrade-install",
			nil,
		},
		{
			"change immutable deployment.spec.selector field",
			"test_charts/mutating-deployment-selector",
			"test_charts/mutating-deployment-selector",
			processError,
		},
		{
			"change immutable statefulset.spec.volumeClaimTemplates field",
			"test_charts/mutating-sfs-volumeclaim",
			"test_charts/mutating-sfs-volumeclaim",
			processError,
		},
		{
			"change immutable deployment.spec.selector.matchLabels field",
			"test_charts/simple-deployment",
			"test_charts/simple-deployment-different-selector",
			processError,
		},
	}

	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			err := ct.doUpgrade(mustNewChart(tc.old), mustNewChart(tc.new), true)

			if err != tc.err {
				if err != nil && tc.err != nil {
					assert.Equal(t, tc.err.Error(), err.Error())
				} else {
					assert.Equal(t, tc.err, err)
				}
			}
		})
	}
}

func mustNewChart(chartPath string) *Chart {
	c, err := NewChart(chartPath)
	if err != nil {
		panic(err)
	}
	return c
}
```

## File: `pkg/chart/test_charts/must-pass-upgrade-install/Chart.yaml`
```yaml
apiVersion: v1
appVersion: "1.0"
description: A Helm chart for Kubernetes
name: nginx
version: 0.2.0
```

## File: `pkg/chart/test_charts/must-pass-upgrade-install/README.md`
```markdown
Chart generated with `helm create nginx`, and is intended to pass upgrades and installs.

A fake "previous revision" can be found at `./ct_prev_revision/must-pass-upgrade-install`.
```

## File: `pkg/chart/test_charts/must-pass-upgrade-install/values.yaml`
```yaml
# Default values for nginx.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.

replicaCount: 1

image:
  repository: nginx
  tag: stable
  pullPolicy: IfNotPresent

nameOverride: ""
fullnameOverride: ""

service:
  type: ClusterIP
  port: 80

resources: {}
  # We usually recommend not to specify default resources and to leave this as a conscious
  # choice for the user. This also increases chances charts run on environments with little
  # resources, such as Minikube. If you do want to specify resources, uncomment the following
  # lines, adjust them as necessary, and remove the curly braces after 'resources:'.
  # limits:
  #  cpu: 100m
  #  memory: 128Mi
  # requests:
  #  cpu: 100m
  #  memory: 128Mi

nodeSelector: {}

tolerations: []

affinity: {}
```

## File: `pkg/chart/test_charts/must-pass-upgrade-install/ci/test-values.yaml`
```yaml
replicaCount: 2
```

## File: `pkg/chart/test_charts/must-pass-upgrade-install/templates/deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "nginx.fullname" . }}
  labels:
    app.kubernetes.io/name: {{ include "nginx.name" . }}
    helm.sh/chart: {{ include "nginx.chart" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/managed-by: {{ .Release.Service }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app.kubernetes.io/name: {{ include "nginx.name" . }}
      app.kubernetes.io/instance: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app.kubernetes.io/name: {{ include "nginx.name" . }}
        app.kubernetes.io/instance: {{ .Release.Name }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: 80
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /
              port: http
          readinessProbe:
            httpGet:
              path: /
              port: http
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
      {{- with .Values.nodeSelector }}
      nodeSelector:
        {{- toYaml . | nindent 8 }}
      {{- end }}
    {{- with .Values.affinity }}
      affinity:
        {{- toYaml . | nindent 8 }}
    {{- end }}
    {{- with .Values.tolerations }}
      tolerations:
        {{- toYaml . | nindent 8 }}
    {{- end }}
```

## File: `pkg/chart/test_charts/must-pass-upgrade-install/templates/service.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ include "nginx.fullname" . }}
  labels:
    app.kubernetes.io/name: {{ include "nginx.name" . }}
    helm.sh/chart: {{ include "nginx.chart" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/managed-by: {{ .Release.Service }}
spec:
  type: {{ .Values.service.type }}
  ports:
    - port: {{ .Values.service.port }}
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: {{ include "nginx.name" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
```

## File: `pkg/chart/test_charts/must-pass-upgrade-install/templates/_helpers.tpl`
```
{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "nginx.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "nginx.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "nginx.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}
```

## File: `pkg/chart/test_charts/must-pass-upgrade-install/templates/tests/test-connection.yaml`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: "{{ include "nginx.fullname" . }}-test-connection"
  labels:
    app.kubernetes.io/name: {{ include "nginx.name" . }}
    helm.sh/chart: {{ include "nginx.chart" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/managed-by: {{ .Release.Service }}
  annotations:
    "helm.sh/hook": test-success
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args:  ['{{ include "nginx.fullname" . }}:{{ .Values.service.port }}']
  restartPolicy: Never
```

## File: `pkg/chart/test_charts/mutating-deployment-selector/Chart.yaml`
```yaml
apiVersion: v1
appVersion: "1.0"
description: A Helm chart for Kubernetes
name: nginx
version: 0.1.0
```

## File: `pkg/chart/test_charts/mutating-deployment-selector/README.md`
```markdown
Reproduces https://github.com/helm/charts/issues/7726
```

## File: `pkg/chart/test_charts/mutating-deployment-selector/values.yaml`
```yaml
# Default values for nginx.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.

replicaCount: 1

image:
  repository: nginx
  tag: stable
  pullPolicy: IfNotPresent

nameOverride: ""
fullnameOverride: ""

service:
  type: ClusterIP
  port: 80

resources: {}
  # We usually recommend not to specify default resources and to leave this as a conscious
  # choice for the user. This also increases chances charts run on environments with little
  # resources, such as Minikube. If you do want to specify resources, uncomment the following
  # lines, adjust them as necessary, and remove the curly braces after 'resources:'.
  # limits:
  #  cpu: 100m
  #  memory: 128Mi
  # requests:
  #  cpu: 100m
  #  memory: 128Mi

nodeSelector: {}

tolerations: []

affinity: {}
```

## File: `pkg/chart/test_charts/mutating-deployment-selector/templates/deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "nginx.fullname" . }}
  labels:
    app.kubernetes.io/name: {{ include "nginx.name" . }}
    helm.sh/chart: {{ include "nginx.chart" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/managed-by: {{ .Release.Service }}
    # Revision should change with each helm upgrade, so if we use it here
    # and don't specify spec.selector, we run into https://github.com/helm/charts/issues/7726
    revision: {{ .Release.Revision | quote }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app.kubernetes.io/name: {{ include "nginx.name" . }}
      app.kubernetes.io/instance: {{ .Release.Name }}
      revision: {{ .Release.Revision | quote }}
  template:
    metadata:
      labels:
        app.kubernetes.io/name: {{ include "nginx.name" . }}
        app.kubernetes.io/instance: {{ .Release.Name }}
        # This should change with each helm upgrade, so we shouldn't be using it as a selector!
        revision: {{ .Release.Revision | quote }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: 80
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /
              port: http
          readinessProbe:
            httpGet:
              path: /
              port: http
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
      {{- with .Values.nodeSelector }}
      nodeSelector:
        {{- toYaml . | nindent 8 }}
      {{- end }}
    {{- with .Values.affinity }}
      affinity:
        {{- toYaml . | nindent 8 }}
    {{- end }}
    {{- with .Values.tolerations }}
      tolerations:
        {{- toYaml . | nindent 8 }}
    {{- end }}
```

## File: `pkg/chart/test_charts/mutating-deployment-selector/templates/service.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ include "nginx.fullname" . }}
  labels:
    app.kubernetes.io/name: {{ include "nginx.name" . }}
    helm.sh/chart: {{ include "nginx.chart" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/managed-by: {{ .Release.Service }}
spec:
  type: {{ .Values.service.type }}
  ports:
    - port: {{ .Values.service.port }}
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: {{ include "nginx.name" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
```

## File: `pkg/chart/test_charts/mutating-deployment-selector/templates/_helpers.tpl`
```
{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "nginx.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "nginx.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "nginx.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}
```

## File: `pkg/chart/test_charts/mutating-deployment-selector/templates/tests/test-connection.yaml`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: "{{ include "nginx.fullname" . }}-test-connection"
  labels:
    app.kubernetes.io/name: {{ include "nginx.name" . }}
    helm.sh/chart: {{ include "nginx.chart" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/managed-by: {{ .Release.Service }}
  annotations:
    "helm.sh/hook": test-success
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args:  ['{{ include "nginx.fullname" . }}:{{ .Values.service.port }}']
  restartPolicy: Never
```

## File: `pkg/chart/test_charts/mutating-sfs-volumeclaim/Chart.yaml`
```yaml
apiVersion: v1
appVersion: "1.0"
description: A Helm chart for Kubernetes
name: nginx
version: 0.1.0
```

## File: `pkg/chart/test_charts/mutating-sfs-volumeclaim/README.md`
```markdown
Reproduces https://github.com/helm/charts/issues/7803
```

## File: `pkg/chart/test_charts/mutating-sfs-volumeclaim/values.yaml`
```yaml
# Default values for nginx.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.

replicaCount: 1

image:
  repository: nginx
  tag: stable
  pullPolicy: IfNotPresent

nameOverride: ""
fullnameOverride: ""

service:
  type: ClusterIP
  port: 80

resources: {}
  # We usually recommend not to specify default resources and to leave this as a conscious
  # choice for the user. This also increases chances charts run on environments with little
  # resources, such as Minikube. If you do want to specify resources, uncomment the following
  # lines, adjust them as necessary, and remove the curly braces after 'resources:'.
  # limits:
  #  cpu: 100m
  #  memory: 128Mi
  # requests:
  #  cpu: 100m
  #  memory: 128Mi

nodeSelector: {}

tolerations: []

affinity: {}
```

## File: `pkg/chart/test_charts/mutating-sfs-volumeclaim/templates/service.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ include "nginx.fullname" . }}
  labels:
    app.kubernetes.io/name: {{ include "nginx.name" . }}
    helm.sh/chart: {{ include "nginx.chart" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/managed-by: {{ .Release.Service }}
spec:
  type: {{ .Values.service.type }}
  clusterIP: None
  ports:
    - port: {{ .Values.service.port }}
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: {{ include "nginx.name" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
```

## File: `pkg/chart/test_charts/mutating-sfs-volumeclaim/templates/statefulset.yaml`
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: {{ include "nginx.fullname" . }}
  labels:
    app.kubernetes.io/name: {{ include "nginx.name" . }}
    helm.sh/chart: {{ include "nginx.chart" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/managed-by: {{ .Release.Service }}
spec:
  replicas: {{ .Values.replicaCount }}
  serviceName: {{ include "nginx.fullname" . }}
  selector:
    matchLabels:
      app.kubernetes.io/name: {{ include "nginx.name" . }}
      app.kubernetes.io/instance: {{ .Release.Name }}
  volumeClaimTemplates:
  - metadata:
      name: data
      labels:
        app.kubernetes.io/name: {{ include "nginx.name" . }}
        helm.sh/chart: {{ include "nginx.chart" . }}
        app.kubernetes.io/instance: {{ .Release.Name }}
        app.kubernetes.io/managed-by: {{ .Release.Service }}
        # Revision should change with each helm upgrade, so if we use it here
        # and don't specify spec.selector, we run into https://github.com/helm/charts/issues/7726
        revision: {{ .Release.Revision | quote }}
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 50Mi
  template:
    metadata:
      labels:
        app.kubernetes.io/name: {{ include "nginx.name" . }}
        app.kubernetes.io/instance: {{ .Release.Name }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: 80
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /
              port: http
          readinessProbe:
            httpGet:
              path: /
              port: http
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
      {{- with .Values.nodeSelector }}
      nodeSelector:
        {{- toYaml . | nindent 8 }}
      {{- end }}
    {{- with .Values.affinity }}
      affinity:
        {{- toYaml . | nindent 8 }}
    {{- end }}
    {{- with .Values.tolerations }}
      tolerations:
        {{- toYaml . | nindent 8 }}
    {{- end }}
```

## File: `pkg/chart/test_charts/mutating-sfs-volumeclaim/templates/_helpers.tpl`
```
{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "nginx.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "nginx.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "nginx.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}
```

## File: `pkg/chart/test_charts/mutating-sfs-volumeclaim/templates/tests/test-connection.yaml`
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: "{{ include "nginx.fullname" . }}-test-connection"
  labels:
    app.kubernetes.io/name: {{ include "nginx.name" . }}
    helm.sh/chart: {{ include "nginx.chart" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/managed-by: {{ .Release.Service }}
  annotations:
    "helm.sh/hook": test-success
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args:  ['{{ include "nginx.fullname" . }}:{{ .Values.service.port }}']
  restartPolicy: Never
```

