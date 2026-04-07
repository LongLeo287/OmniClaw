---
id: cloudflared
type: knowledge
owner: OA_Triage
---
# cloudflared
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Cloudflare Tunnel client

Contains the command-line client for Cloudflare Tunnel, a tunneling daemon that proxies traffic from the Cloudflare network to your origins.
This daemon sits between Cloudflare network and your origin (e.g. a webserver). Cloudflare attracts client requests and sends them to you
via this daemon, without requiring you to poke holes on your firewall --- your origin can remain as closed as possible.
Extensive documentation can be found in the [Cloudflare Tunnel section](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel) of the Cloudflare Docs.
All usages related with proxying to your origins are available under `cloudflared tunnel help`.

You can also use `cloudflared` to access Tunnel origins (that are protected with `cloudflared tunnel`) for TCP traffic
at Layer 4 (i.e., not HTTP/websocket), which is relevant for use cases such as SSH, RDP, etc.
Such usages are available under `cloudflared access help`.

You can instead use [WARP client](https://developers.cloudflare.com/warp-client/)
to access private origins behind Tunnels for Layer 4 traffic without requiring `cloudflared access` commands on the client side.


## Before you get started

Before you use Cloudflare Tunnel, you'll need to complete a few steps in the Cloudflare dashboard: you need to add a
website to your Cloudflare account. Note that today it is possible to use Tunnel without a website (e.g. for private
routing), but for legacy reasons this requirement is still necessary:
1. [Add a website to Cloudflare](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/)
2. [Change your domain nameservers to Cloudflare](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/)


## Installing `cloudflared`

Downloads are available as standalone binaries, a Docker image, and Debian, RPM, and Homebrew packages. You can also find releases [here](https://github.com/cloudflare/cloudflared/releases) on the `cloudflared` GitHub repository.

* You can [install on macOS](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#macos) via Homebrew or by downloading the [latest Darwin amd64 release](https://github.com/cloudflare/cloudflared/releases)
* Binaries, Debian, and RPM packages for Linux [can be found here](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#linux)
* A Docker image of `cloudflared` is [available on DockerHub](https://hub.docker.com/r/cloudflare/cloudflared)
* You can install on Windows machines with the [steps here](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#windows)
* To build from source, install the required version of go, mentioned in the [Development](#development) section below. Then you can run `make cloudflared`.

User documentation for Cloudflare Tunnel can be found at https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/


## Creating Tunnels and routing traffic

Once installed, you can authenticate `cloudflared` into your Cloudflare account and begin creating Tunnels to serve traffic to your origins.

* Create a Tunnel with [these instructions](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/)
* Route traffic to that Tunnel:
  * Via public [DNS records in Cloudflare](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/dns/)
  * Or via a public hostname guided by a [Cloudflare Load Balancer](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers/)
  * Or from [WARP client private traffic](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/)


## TryCloudflare

Want to test Cloudflare Tunnel before adding a website to Cloudflare? You can do so with TryCloudflare using the documentation [available here](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/).

## Deprecated versions

Cloudflare currently supports versions of cloudflared that are **within one year** of the most recent release. Breaking changes unrelated to feature availability may be introduced that will impact versions released more than one year ago. You can read more about upgrading cloudflared in our [developer documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/).

For example, as of January 2023 Cloudflare will support cloudflared version 2023.1.1 to cloudflared 2022.1.1.

## Development

### Requirements
- [GNU Make](https://www.gnu.org/software/make/)
- [capnp](https://capnproto.org/install.html)
- [go >= 1.24](https://go.dev/doc/install)
- Optional tools:
  - [capnpc-go](https://pkg.go.dev/zombiezen.com/go/capnproto2/capnpc-go)
  - [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports)
  - [golangci-lint](https://github.com/golangci/golangci-lint)
  - [gomocks](https://pkg.go.dev/go.uber.org/mock)

### Build
To build cloudflared locally run `make cloudflared`

### Test
To locally run the tests run `make test`

### Linting
To format the code and keep a good code quality use `make fmt` and `make lint`

### Mocks
After changes on interfaces you might need to regenerate the mocks, so run `make mock`

```

### File: .ci_DISTILLED.md
```md
---
id: .ci
type: distilled_knowledge
---
# .ci

## SWALLOW ENGINE DISTILLATION

### File: scripts_DISTILLED.md
```md
---
id: scripts
type: distilled_knowledge
---
# scripts

## SWALLOW ENGINE DISTILLATION

### File: component-tests.sh
```sh
#!/bin/bash
set -e -u -o pipefail

# Fetch cloudflared from the artifacts folder
mv ./artifacts/cloudflared ./cloudflared

python3 -m venv env
. env/bin/activate

pip install --upgrade -r component-tests/requirements.txt

# Creates and routes a Named Tunnel for this build. Also constructs
# config file from env vars.
python3 component-tests/setup.py --type create

# Define the cleanup function
cleanup() {
    # The Named Tunnel is deleted and its route unprovisioned here.
    python3 component-tests/setup.py --type cleanup
}

# The trap will call the cleanup function on script exit
trap cleanup EXIT

pytest component-tests -o log_cli=true --log-cli-level=INFO --junit-xml=report.xml

```

### File: fmt-check.sh
```sh
#!/bin/bash
set -e -u -o pipefail

OUTPUT=$(go run -mod=readonly golang.org/x/tools/cmd/goimports@v0.30.0 -l -d -local github.com/cloudflare/cloudflared $(go list -mod=vendor -f '{{.Dir}}' -a ./... | fgrep -v tunnelrpc))

if [ -n "$OUTPUT" ] ; then
  PAGER=$(which colordiff || echo cat)
  echo
  echo "Code formatting issues found, use 'make fmt' to correct them"
  echo
  echo "$OUTPUT" | $PAGER
  exit 1
fi

```

### File: github-push.sh
```sh
#!/bin/bash
set -e -u -o pipefail

BRANCH="master"
TMP_PATH="$PWD/tmp"
PRIVATE_KEY_PATH="$TMP_PATH/github-deploy-key"
PUBLIC_KEY_GITHUB_PATH="$TMP_PATH/github.pub"

mkdir -p $TMP_PATH

# Setup Private Key
echo "$CLOUDFLARED_DEPLOY_SSH_KEY" > $PRIVATE_KEY_PATH
chmod 400 $PRIVATE_KEY_PATH

# Download GitHub Public Key for KnownHostsFile
ssh-keyscan -t ed25519 github.com > $PUBLIC_KEY_GITHUB_PATH

# Setup git ssh command with the right configurations
export GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=$PUBLIC_KEY_GITHUB_PATH -o IdentitiesOnly=yes -i $PRIVATE_KEY_PATH"

# Add GitHub as a new remote
git remote add github git@github.com:cloudflare/cloudflared.git || true

# GitLab doesn't pull branch references, instead it creates a new one on each pipeline.
# Therefore, we need to manually fetch the reference to then push it to GitHub.
git fetch origin $BRANCH:$BRANCH
git push -u github $BRANCH

if TAG="$(git describe --tags --exact-match 2>/dev/null)"; then
  git push -u github "$TAG"
fi

```

### File: linux_DISTILLED.md
```md
---
id: linux
type: distilled_knowledge
---
# linux

## SWALLOW ENGINE DISTILLATION

### File: build-packages-fips.sh
```sh
#!/bin/bash
set -e -u -o pipefail
VERSION=$(git describe --tags --always --match "[0-9][0-9][0-9][0-9].*.*")
echo $VERSION

# This controls the directory the built artifacts go into
export ARTIFACT_DIR=artifacts/
mkdir -p $ARTIFACT_DIR

arch=("amd64")
export TARGET_ARCH=$arch
export TARGET_OS=linux
export FIPS=true
# For BoringCrypto to link, we need CGO enabled. Otherwise compilation fails.
export CGO_ENABLED=1

make cloudflared-deb
mv cloudflared-fips\_$VERSION\_$arch.deb $ARTIFACT_DIR/cloudflared-fips-linux-$arch.deb

# rpm packages invert the - and _ and use x86_64 instead of amd64.
RPMVERSION=$(echo $VERSION | sed -r 's/-/_/g')
RPMARCH="x86_64"
make cloudflared-rpm
mv cloudflared-fips-$RPMVERSION-1.$RPMARCH.rpm $ARTIFACT_DIR/cloudflared-fips-linux-$RPMARCH.rpm

# finally move the linux binary as well.
mv ./cloudflared $ARTIFACT_DIR/cloudflared-fips-linux-$arch

```

### File: build-packages.sh
```sh
#!/bin/bash
set -e -u -o pipefail

# Check if architecture argument is provided
if [ $# -eq 0 ]; then
    echo "Error: Architecture argument is required"
    echo "Usage: $0 <architecture>"
    exit 1
fi

# Parameters
arch=$1

# Get Version
VERSION=$(git describe --tags --always --match "[0-9][0-9][0-9][0-9].*.*")
echo $VERSION

# Disable FIPS module in go-boring
export GOEXPERIMENT=noboringcrypto
export CGO_ENABLED=0

# This controls the directory the built artifacts go into
export ARTIFACT_DIR=artifacts/
mkdir -p $ARTIFACT_DIR

export TARGET_OS=linux

unset TARGET_ARM
export TARGET_ARCH=$arch

## Support for arm platforms without hardware FPU enabled
if [[ $arch == arm ]] ; then
    export TARGET_ARCH=arm
    export TARGET_ARM=5
fi

## Support for armhf builds
if [[ $arch == armhf ]] ; then
    export TARGET_ARCH=arm
    export TARGET_ARM=7
fi

make cloudflared-deb
mv cloudflared\_$VERSION\_$arch.deb $ARTIFACT_DIR/cloudflared-linux-$arch.deb

# rpm packages invert the - and _ and use x86_64 instead of amd64.
RPMVERSION=$(echo $VERSION|sed -r 's/-/_/g')
RPMARCH=$arch
if [ $arch == "amd64" ];then
    RPMARCH="x86_64"
fi
if [ $arch == "arm64" ]; then
    RPMARCH="aarch64"
fi
make cloudflared-rpm
mv cloudflared-$RPMVERSION-1.$RPMARCH.rpm $ARTIFACT_DIR/cloudflared-linux-$RPMARCH.rpm

# finally move the linux binary as well.
mv ./cloudflared $ARTIFACT_DIR/cloudflared-linux-$arch


```


```

### File: mac_DISTILLED.md
```md
---
id: mac
type: distilled_knowledge
---
# mac

## SWALLOW ENGINE DISTILLATION

### File: build.sh
```sh
#!/bin/bash

set -exo pipefail

if [[ "$(uname)" != "Darwin" ]] ; then
    echo "This should be run on macOS"
    exit 1
fi

if [[ "amd64" != "${TARGET_ARCH}" && "arm64" != "${TARGET_ARCH}" ]]
then
  echo "TARGET_ARCH must be amd64 or arm64"
  exit 1
fi

go version
export GO111MODULE=on

# build 'cloudflared-darwin-amd64.tgz'
mkdir -p artifacts
TARGET_DIRECTORY=".build"
BINARY_NAME="cloudflared"
VERSION=$(git describe --tags --always --dirty="-dev")
PRODUCT="cloudflared"
APPLE_CA_CERT="apple_dev_ca.cert"
CODE_SIGN_PRIV="code_sign.p12"
CODE_SIGN_CERT="code_sign.cer"
INSTALLER_PRIV="installer.p12"
INSTALLER_CERT="installer.cer"
BUNDLE_ID="com.cloudflare.cloudflared"
SEC_DUP_MSG="security: SecKeychainItemImport: The specified item already exists in the keychain."
export PATH="$PATH:/usr/local/bin"
FILENAME="$(pwd)/artifacts/cloudflared-darwin-$TARGET_ARCH.tgz"
PKGNAME="$(pwd)/artifacts/cloudflared-$TARGET_ARCH.pkg"
mkdir -p ../src/github.com/cloudflare/    
cp -r . ../src/github.com/cloudflare/cloudflared
cd ../src/github.com/cloudflare/cloudflared 

# Imports certificates to the Apple KeyChain
import_certificate() {
    local CERTIFICATE_NAME=$1
    local CERTIFICATE_ENV_VAR=$2
    local CERTIFICATE_FILE_NAME=$3

    echo "Importing $CERTIFICATE_NAME"

    if [[ ! -z "$CERTIFICATE_ENV_VAR" ]]; then
      # write certificate to disk and then import it keychain
      echo -n -e ${CERTIFICATE_ENV_VAR} | base64 -D > ${CERTIFICATE_FILE_NAME}
      # we set || true  here and for every `security import invoke` because the  "duplicate SecKeychainItemImport" error
      # will cause set -e to exit 1. It is okay we do this because we deliberately handle this error in the lines below.
      local out=$(security import ${CERTIFICATE_FILE_NAME} -T /usr/bin/pkgbuild -A 2>&1) || true
      local exitcode=$?
      # delete the certificate from disk
      rm -rf ${CERTIFICATE_FILE_NAME}
      if [ -n "$out" ]; then
        if [ $exitcode -eq 0 ]; then
            echo "$out"
        else
            if [ "$out" != "${SEC_DUP_MSG}" ]; then
                echo "$out" >&2
                exit $exitcode
            else
                echo "already imported code signing certificate"
            fi
        fi
      fi
    fi
}

create_cloudflared_build_keychain() {
  # Reusing the private key password as the keychain key
  local PRIVATE_KEY_PASS=$1

  # Create keychain only if it doesn't already exist
  if [ ! -f "$HOME/Library/Keychains/cloudflared_build_keychain.keychain-db" ]; then
    security create-keychain -p "$PRIVATE_KEY_PASS" cloudflared_build_keychain
  else
    echo "Keychain already exists: cloudflared_build_keychain"
  fi

  # Append temp keychain to the user domain
  security list-keychains -d user -s cloudflared_build_keychain $(security list-keychains -d user | sed s/\"//g)

  # Remove relock timeout
  security set-keychain-settings cloudflared_build_keychain

  # Unlock keychain so it doesn't require password
  security unlock-keychain -p "$PRIVATE_KEY_PASS" cloudflared_build_keychain

}

# Imports private keys to the Apple KeyChain
import_private_keys() {
    local PRIVATE_KEY_NAME=$1
    local PRIVATE_KEY_ENV_VAR=$2
    local PRIVATE_KEY_FILE_NAME=$3
    local PRIVATE_KEY_PASS=$4

    echo "Importing $PRIVATE_KEY_NAME"

    if [[ ! -z "$PRIVATE_KEY_ENV_VAR" ]]; then
      if [[ ! -z "$PRIVATE_KEY_PASS" ]]; then
        # write private key to disk and then import it keychain
        echo -n -e ${PRIVATE_KEY_ENV_VAR} | base64 -D > ${PRIVATE_KEY_FILE_NAME}
        # we set || true  here and for every `security import invoke` because the  "duplicate SecKeychainItemImport" error
        # will cause set -e to exit 1. It is okay we do this because we deliberately handle this error in the lines below.
        local out=$(security import ${PRIVATE_KEY_FILE_NAME} -k cloudflared_build_keychain -P "$PRIVATE_KEY_PASS" -T /usr/bin/pkgbuild -A -P "${PRIVATE_KEY_PASS}" 2>&1) || true
        local exitcode=$?
        rm -rf ${PRIVATE_KEY_FILE_NAME}
        if [ -n "$out" ]; then
          if [ $exitcode -eq 0 ]; then
              echo "$out"
          else
              if [ "$out" != "${SEC_DUP_MSG}" ]; then
                  echo "$out" >&2
                  exit $exitcode
              fi
          fi
        fi
      fi
    fi
}

# Create temp keychain only for this build
create_cloudflared_build_keychain "${CFD_CODE_SIGN_PASS}"

# Add Apple Root Developer certificate to the key chain
import_certificate "Apple Developer CA" "${APPLE_DEV_CA_CERT}" "${APPLE_CA_CERT}"

# Add code signing private key to the key chain
import_private_keys "Developer ID Application" "${CFD_CODE_SIGN_KEY}" "${CODE_SIGN_PRIV}" "${CFD_CODE_SIGN_PASS}"

# Add code signing certificate to the key chain
import_certificate "Developer ID Application" "${CFD_CODE_SIGN_CERT}" "${CODE_SIGN_CERT}"

# Add package signing private key to the key chain
import_private_keys "Developer ID Installer" "${CFD_INSTALLER_KEY}" "${INSTALLER_PRIV}" "${CFD_INSTALLER_PASS}"

# Add package signing certificate to the key chain
import_certificate "Developer ID Installer" "${CFD_INSTALLER_CERT}" "${INSTALLER_CERT}"

# get the code signing certificate name
if [[ ! -z "$CFD_CODE_SIGN_NAME" ]]; then
  CODE_SIGN_NAME="${CFD_CODE_SIGN_NAME}"
else
  if [[ -n "$(security find-certificate -c "Developer ID Application" cloudflared_build_keychain | cut -d'"' -f 4 -s | grep "Developer ID Application:" | head -1)" ]]; then
    CODE_SIGN_NAME=$(security find-certificate -c "Developer ID Application" cloudflared_build_keychain | cut -d'"' -f 4 -s | grep "Developer ID Application:" | head -1)
  else
    CODE_SIGN_NAME=""
  fi
fi

# get the package signing certificate name
if [[ ! -z "$CFD_INSTALLER_NAME" ]]; then
  PKG_SIGN_NAME="${CFD_INSTALLER_NAME}"
else
  if [[ -n "$(security find-certificate -c "Developer ID Installer" cloudflared_build_keychain | cut -d'"' -f 4 -s | grep "Developer ID Installer:" | head -1)" ]]; then
    PKG_SIGN_NAME=$(security find-certificate -c "Developer ID Installer" cloudflared_build_keychain | cut -d'"' -f 4 -s | grep "Developer ID Installer:" | head -1)
  else
    PKG_SIGN_NAME=""
  fi
fi

# cleanup the build directory because the previous execution might have failed without cleaning up.
rm -rf "${TARGET_DIRECTORY}"
export TARGET_OS="darwin"
GOCACHE="$PWD/../../../../" GOPATH="$PWD/../../../../" CGO_ENABLED=1 make cloudflared


# This allows apple tools to use the certificates in the keychain without requiring password input.
# This command always needs to run after the certificates have been loaded into the keychain
if [[ ! -z "$CFD_CODE_SIGN_PASS" ]]; then
  security set-key-partition-list -S apple-tool:,apple: -s -k "${CFD_CODE_SIGN_PASS}" cloudflared_build_keychain
fi

# sign the cloudflared binary
if [[ ! -z "$CODE_SIGN_NAME" ]]; then
  codesign --keychain $HOME/Library/Keychains/cloudflared_build_keychain.keychain-db -s "${CODE_SIGN_NAME}" -fv --options runtime --timestamp ${BINARY_NAME}

 # notarize the binary
 # TODO: TUN-5789
fi

ARCH_TARGET_DIRECTORY="${TARGET_DIRECTORY}/${TARGET_ARCH}-build"
# creating build directory
rm -rf $ARCH_TARGET_DIRECTORY
mkdir -p "${ARCH_TARGET_DIRECTORY}"
mkdir -p "${ARCH_TARGET_DIRECTORY}/contents"
cp -r ".mac_resources/scripts" "${ARCH_TARGET_DIRECTORY}/scripts"

# copy cloudflared into the build directory
cp ${BINARY_NAME} "${ARCH_TARGET_DIRECTORY}/contents/${PRODUCT}"

# compress cloudflared into a tar and gzipped file
tar czf "$FILENAME" "${BINARY_NAME}"

# build the installer package
if [[ ! -z "$PKG_SIGN_NAME" ]]; then

  pkgbuild --identifier com.cloudflare.${PRODUCT} \
      --version ${VERSION} \
      --scripts ${ARCH_TARGET_DIRECTORY}/scripts \
      --root ${ARCH_TARGET_DIRECTORY}/contents \
      --install-location /usr/local/bin \
      --keychain cloudflared_build_keychain \
      --sign "${PKG_SIGN_NAME}" \
      ${PKGNAME}

      # notarize the package
      # TODO: TUN-5789
else
    pkgbuild --identifier com.cloudflare.${PRODUCT} \
      --version ${VERSION} \
      --scripts ${ARCH_TARGET_DIRECTORY}/scripts \
      --root ${ARCH_TARGET_DIRECTORY}/contents \
      --install-location /usr/local/bin \
      ${PKGNAME}
fi

# cleanup build directory because this script is not ran within containers,
# which might lead to future issues in subsequent runs.
rm -rf "${TARGET_DIRECTORY}"

# cleanup the keychain
security default-keychain -d user -s login.keychain-db
security list-keychains -d user -s login.keychain-db
security delete-keychain cloudflared_build_keychain

```

### File: install-go.sh
```sh
rm -rf /tmp/go
export GOCACHE=/tmp/gocache
rm -rf $GOCACHE

if [ -z "$1" ]
  then
    echo "No go version supplied"
fi

brew install "$1"

go version
which go
go env

```


```

### File: package-windows.sh
```sh
#!/bin/bash
set -e -u -o pipefail

python3 -m venv env
. env/bin/activate
pip install pynacl==1.4.0 pygithub==1.55

VERSION=$(git describe --tags --always --match "[0-9][0-9][0-9][0-9].*.*")
echo $VERSION

export TARGET_OS=windows
# This controls the directory the built artifacts go into
export BUILT_ARTIFACT_DIR=artifacts/
export FINAL_ARTIFACT_DIR=artifacts/
mkdir -p $BUILT_ARTIFACT_DIR
mkdir -p $FINAL_ARTIFACT_DIR
windowsArchs=("amd64" "386")
for arch in ${windowsArchs[@]}; do
    export TARGET_ARCH=$arch
    # Copy .exe from artifacts directory
    cp $BUILT_ARTIFACT_DIR/cloudflared-windows-$arch.exe ./cloudflared.exe
    make cloudflared-msi
    # Copy msi into final directory
    mv cloudflared-$VERSION-$arch.msi $FINAL_ARTIFACT_DIR/cloudflared-windows-$arch.msi
done

```

### File: release-target.sh
```sh
#!/bin/bash
set -e -u -o pipefail

# Check if a make target is provided as an argument
if [ $# -eq 0 ]; then
    echo "Error: Make target argument is required"
    echo "Usage: $0 <make-target>"
    exit 1
fi

MAKE_TARGET=$1

python3 -m venv venv
source venv/bin/activate

# Our release scripts are written in python, so we should install their dependecies
... [TRUNCATED]
```

### File: .golangci.yaml
```yaml
linters:
  enable:
    # Some of the linters below are commented out. We should uncomment and start running them, but they return
    # too many problems to fix in one commit. Something for later.
    - asasalint        # Check for pass []any as any in variadic func(...any).
    - asciicheck       # Checks that all code identifiers does not have non-ASCII symbols in the name.
    - bidichk          # Checks for dangerous unicode character sequences.
    - bodyclose        # Checks whether HTTP response body is closed successfully.
    - decorder         # Check declaration order and count of types, constants, variables and functions.
    - dogsled          # Checks assignments with too many blank identifiers (e.g. x, , , _, := f()).
    - dupl             # Tool for code clone detection.
    - dupword          # Checks for duplicate words in the source code.
    - durationcheck    # Check for two durations multiplied together.
    - errcheck         # Errcheck is a program for checking for unchecked errors in Go code. These unchecked errors can be critical bugs in some cases.
    - errname          # Checks that sentinel errors are prefixed with the Err and error types are suffixed with the Error.
    - exhaustive       # Check exhaustiveness of enum switch statements.
    - gofmt            # Gofmt checks whether code was gofmt-ed. By default this tool runs with -s option to check for code simplification.
    - goimports        # Check import statements are formatted according to the 'goimport' command. Reformat imports in autofix mode.
    - gosec            # Inspects source code for security problems.
    - gosimple         # Linter for Go source code that specializes in simplifying code.
    - govet            # Vet examines Go source code and reports suspicious constructs. It is roughly the same as 'go vet' and uses its passes.
    - ineffassign      # Detects when assignments to existing variables are not used.
    - importas         # Enforces consistent import aliases.
    - misspell         # Finds commonly misspelled English words.
    - prealloc         # Finds slice declarations that could potentially be pre-allocated.
    - promlinter       # Check Prometheus metrics naming via promlint.
    - sloglint         # Ensure consistent code style when using log/slog.
    - sqlclosecheck    # Checks that sql.Rows, sql.Stmt, sqlx.NamedStmt, pgx.Query are closed.
    - staticcheck      # It's a set of rules from staticcheck. It's not the same thing as the staticcheck binary.
    - usetesting       # Reports uses of functions with replacement inside the testing package.
    - testableexamples # Linter checks if examples are testable (have an expected output).
    - testifylint      # Checks usage of github.com/stretchr/testify.
    - tparallel        # Tparallel detects inappropriate usage of t.Parallel() method in your Go test codes.
    - unconvert        # Remove unnecessary type conversions.
    - unused           # Checks Go code for unused constants, variables, functions and types.
    - wastedassign     # Finds wasted assignment statements.
    - whitespace       # Whitespace is a linter that checks for unnecessary newlines at the start and end of functions, if, for, etc.
    - zerologlint      # Detects the wrong usage of zerolog that a user forgets to dispatch with Send or Msg.
  # Other linters are disabled, list of all is here: https://golangci-lint.run/usage/linters/
run:
  timeout: 5m
  modules-download-mode: vendor

# output configuration options
output:
  formats:
    - format: 'colored-line-number'
  print-issued-lines: true
  print-linter-name: true

issues:
  # Maximum issues count per one linter.
  # Set to 0 to disable.
  # Default: 50
  max-issues-per-linter: 50
  # Maximum count of issues with the same text.
  # Set to 0 to disable.
  # Default: 3
  max-same-issues: 15
  # Show only new issues: if there are unstaged changes or untracked files,
  # only those changes are analyzed, else only changes in HEAD~ are analyzed.
  # It's a super-useful option for integration of golangci-lint into existing large codebase.
  # It's not practical to fix all existing issues at the moment of integration:
  # much better don't allow issues in new code.
  #
  # Default: false
  new: true
  # Show only new issues created after git revision `REV`.
  # Default: ""
  new-from-rev: ac34f94d423273c8fa8fdbb5f2ac60e55f2c77d5
  # Show issues in any part of update files (requires new-from-rev or new-from-patch).
  # Default: false
  whole-files: true
  # Which dirs to exclude: issues from them won't be reported.
  # Can use regexp here: `generated.*`, regexp is applied on full path,
  # including the path prefix if one is set.
  # Default dirs are skipped independently of this option's value (see exclude-dirs-use-default).
  # "/" will be replaced by current OS file path separator to properly work on Windows.
  # Default: []
  exclude-dirs:
    - vendor

linters-settings:
  # Check exhaustiveness of enum switch statements.
  exhaustive:
    # Presence of "default" case in switch statements satisfies exhaustiveness,
    # even if all enum members are not listed.
    # Default: false
    default-signifies-exhaustive: true

```

### File: .mac_resources_DISTILLED.md
```md
---
id: .mac_resources
type: distilled_knowledge
---
# .mac_resources

## SWALLOW ENGINE DISTILLATION

### File: uninstall.sh
```sh
#!/bin/bash

/usr/local/bin/cloudflared service uninstall
rm /usr/local/bin/cloudflared
pkgutil --forget com.cloudflare.cloudflared
```


```

### File: AGENTS.md
```md
# Cloudflared

Cloudflare's command-line tool and networking daemon written in Go.
Production-grade tunneling and network connectivity services used by millions of
developers and organizations worldwide.

## Essential Commands

### Build & Test (Always run before commits)

```bash
# Full development check (run before any commit)
make test lint

# Build for current platform
make cloudflared

# Run all unit tests with coverage
make test
make cover

# Run specific test
go test -run TestFunctionName ./path/to/package

# Run tests with race detection
go test -race ./...
```

### Platform-Specific Builds

```bash
# Linux
TARGET_OS=linux TARGET_ARCH=amd64 make cloudflared

# Windows
TARGET_OS=windows TARGET_ARCH=amd64 make cloudflared

# macOS ARM64
TARGET_OS=darwin TARGET_ARCH=arm64 make cloudflared

# FIPS compliant build
FIPS=true make cloudflared
```

### Code Quality & Formatting

```bash
# Run linter (38+ enabled linters)
make lint

# Auto-fix formatting
make fmt
gofmt -w .
goimports -w .

# Security scanning
make vet

# Component tests (Python integration tests)
cd component-tests && python -m pytest test_file.py::test_function_name
```

## Project Knowledge

### Package Structure

- Use meaningful package names that reflect functionality
- Package names should be lowercase, single words when possible
- Avoid generic names like `util`, `common`, `helper`

### Function and Method Guidelines

```go
// Good: Clear purpose, proper error handling
func (c *Connection) HandleRequest(ctx context.Context, req *http.Request) error {
    if req == nil {
        return errors.New("request cannot be nil")
    }
    // Implementation...
    return nil
}
```

### Error Handling

- Always handle errors explicitly, never ignore them
- Use `fmt.Errorf` for error wrapping
- Create meaningful error messages with context
- Use error variables for common errors

```go
// Good error handling patterns
if err != nil {
    return fmt.Errorf("failed to process connection: %w", err)
}
```

### Logging Standards

- Use `github.com/rs/zerolog` for structured logging
- Include relevant context fields
- Use appropriate log levels (Debug, Info, Warn, Error)

```go
logger.Info().
    Str("tunnelID", tunnel.ID).
    Int("connIndex", connIndex).
    Msg("Connection established")
```

### Testing Patterns

- Use `github.com/stretchr/testify` for assertions
- Test files end with `_test.go`
- Use table-driven tests for multiple scenarios
- Always use `t.Parallel()` for parallel-safe tests
- Use meaningful test names that describe behavior

```go
func TestMetricsListenerCreation(t *testing.T) {
    t.Parallel()
    // Test implementation
    assert.Equal(t, expected, actual)
    require.NoError(t, err)
}
```

### Constants and Variables

```go
const (
    MaxGracePeriod       = time.Minute * 3
    MaxConcurrentStreams = math.MaxUint32
    LogFieldConnIndex    = "connIndex"
)

var (
    // Group related variables
    switchingProtocolText = fmt.Sprintf("%d %s", http.StatusSwitchingProtocols, http.StatusText(http.StatusSwitchingProtocols))
    flushableContentTypes = []string{sseContentType, grpcContentType, sseJsonContentType}
)
```

### Type Definitions

- Define interfaces close to their usage
- Keep interfaces small and focused
- Use descriptive names for complex types

```go
type TunnelConnection interface {
    Serve(ctx context.Context) error
}

type TunnelProperties struct {
    Credentials    Credentials
    QuickTunnelUrl string
}
```

## Key Architectural Patterns

### Context Usage

- Always accept `context.Context` as first parameter for long-running operations
- Respect context cancellation in loops and blocking operations
- Pass context through call chains

### Concurrency

- Use channels for goroutine communication
- Protect shared state with mutexes
- Prefer `sync.RWMutex` for read-heavy workloads

### Configuration

- Use structured configuration with validation
- Support both file-based and CLI flag configuration
- Provide sensible defaults

### Metrics and Observability

- Instrument code with Prometheus metrics
- Use OpenTelemetry for distributed tracing
- Include structured logging with relevant context

## Boundaries

### ✅ Always Do

- Run `make test lint` before any commit
- Handle all errors explicitly with proper context
- Use `github.com/rs/zerolog` for all logging
- Add `t.Parallel()` to all parallel-safe tests
- Follow the import grouping conventions
- Use meaningful variable and function names
- Include context.Context for long-running operations
- Close resources in defer statements

### ⚠️ Ask First Before

- Adding new dependencies to go.mod
- Modifying CI/CD configuration files
- Changing build system or Makefile
- Modifying component test infrastructure
- Adding new linter rules or changing golangci-lint config
- Making breaking changes to public APIs
- Changing logging levels or structured logging fields

### 🚫 Never Do

- Ignore errors without explicit handling (`_ = err`)
- Use generic package names (`util`, `helper`, `common`)
- Commit code that fails `make test lint`
- Use `fmt.Print*` instead of structured logging
- Modify vendor dependencies directly
- Commit secrets, credentials, or sensitive data
- Use deprecated or unsafe Go patterns
- Skip testing for new functionality
- Remove existing tests unless they're genuinely invalid

## Dependencies Management

- Use Go modules (`go.mod`) exclusively
- Vendor dependencies for reproducible builds
- Keep dependencies up-to-date and secure
- Prefer standard library when possible
- Cloudflared uses a fork of quic-go always check release notes before bumping
  this dependency.

## Security Considerations

- FIPS compliance support available
- Vulnerability scanning integrated in CI
- Credential handling follows security best practices
- Network security with TLS/QUIC protocols
- Regular security audits and updates
- Post quantum encryption

## Common Patterns to Follow

1. **Graceful shutdown**: Always implement proper cleanup
2. **Resource management**: Close resources in defer statements
3. **Error propagation**: Wrap errors with meaningful context
4. **Configuration validation**: Validate inputs early
5. **Logging consistency**: Use structured logging throughout
6. **Testing coverage**: Aim for comprehensive test coverage
7. **Documentation**: Comment exported functions and types

Remember: This is a mission-critical networking tool used in production by many
organizations. Code quality, security, and reliability are paramount.

```

### File: catalog-info.yaml
```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: cloudflared
  description: Client for Cloudflare Tunnels
  annotations:
    cloudflare.com/software-excellence-opt-in: "true"
    cloudflare.com/jira-project-key: "TUN"
    cloudflare.com/jira-project-component: "Cloudflare Tunnel"
  tags:
    - internal
spec:
  type: "service"
  lifecycle: "Active"
  owner: "teams/tunnel-teams-routing"
  cf:
    compliance:
      fedramp-high: "pending"
      fedramp-moderate: "yes"
    FIPS: "required"

```

### File: cfsetup.yaml
```yaml
# A valid cfsetup.yaml is required but we dont have any real config to specify
dummy_key: true

```

### File: CHANGES.md
```md
## 2026.2.0
### Breaking Change
- Removes the `proxy-dns` feature from cloudflared. This feature allowed running a local DNS over HTTPS (DoH) proxy.
  Users who relied on this functionality should migrate to alternative solutions.
  
  Removed commands and flags:
  - `cloudflared proxy-dns`
  - `cloudflared tunnel proxy-dns` 
  - `--proxy-dns`, `--proxy-dns-port`, `--proxy-dns-address`, `--proxy-dns-upstream`, `--proxy-dns-max-upstream-conns`, `--proxy-dns-bootstrap`
  - `resolver` section in configuration file

## 2025.7.1
### Notices
- `cloudflared` will no longer officially support Debian and Ubuntu distros that reached end-of-life: `buster`, `bullseye`, `impish`, `trusty`.

## 2025.1.1
### New Features
- This release introduces the use of new Post Quantum curves and the ability to use Post Quantum curves when running tunnels with the QUIC protocol this applies to non-FIPS and FIPS builds.

## 2024.12.2
### New Features
- This release introduces the ability to collect troubleshooting information from one instance of cloudflared running on the local machine. The command can be executed as `cloudflared tunnel diag`.

## 2024.12.1
### Notices
- The use of the `--metrics` is still honoured meaning that if this flag is set the metrics server will try to bind it, however, this version includes a change that makes the metrics server bind to a port with a semi-deterministic approach. If the metrics flag is not present the server will bind to the first available port of the range 20241 to 20245. In case of all ports being unavailable then the fallback is to bind to a random port.

## 2024.10.0
### Bug Fixes
- We fixed a bug related to `--grace-period`. Tunnels that use QUIC as transport weren't abiding by this waiting period before forcefully closing the connections to the edge. From now on, both QUIC and HTTP2 tunnels will wait for either the grace period to end (defaults to 30 seconds) or until the last in-flight request is handled. Users that wish to maintain the previous behavior should set `--grace-period` to 0 if `--protocol` is set to `quic`. This will force `cloudflared` to shutdown as soon as either SIGTERM or SIGINT is received.

## 2024.2.1
### Notices
- Starting from this version, tunnel diagnostics will be enabled by default. This will allow the engineering team to remotely get diagnostics from cloudflared during debug activities. Users still have the capability to opt-out of this feature by defining `--management-diagnostics=false` (or env `TUNNEL_MANAGEMENT_DIAGNOSTICS`).

## 2023.9.0
### Notices
- The `warp-routing` `enabled: boolean` flag is no longer supported in the configuration file. Warp Routing traffic (eg TCP, UDP, ICMP) traffic is proxied to cloudflared if routes to the target tunnel are configured. This change does not affect remotely managed tunnels, but for locally managed tunnels, users that might be relying on this feature flag to block traffic should instead guarantee that tunnel has no Private Routes configured for the tunnel.
## 2023.7.0
### New Features
- You can now enable additional diagnostics over the management.argotunnel.com service for your active cloudflared connectors via a new runtime flag `--management-diagnostics` (or env `TUNNEL_MANAGEMENT_DIAGNOSTICS`). This feature is provided as opt-in and requires the flag to enable. Endpoints such as /metrics provides your prometheus metrics endpoint another mechanism to be reached. Additionally /debug/pprof/(goroutine|heap) are also introduced to allow for remotely retrieving active pprof information from a running cloudflared connector.

## 2023.4.1
### New Features
- You can now stream your logs from your remote cloudflared to your local terminal with `cloudflared tail <TUNNEL-ID>`. This new feature requires the remote cloudflared to be version 2023.4.1 or higher.

## 2023.3.2
### Notices
- Due to the nature of QuickTunnels (https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/do-more-with-tunnels/trycloudflare/) and its intended usage for testing and experiment of Cloudflare Tunnels, starting from 2023.3.2, QuickTunnels only make a single connection to the edge. If users want to use Tunnels in a production environment, they should move to Named Tunnels instead. (https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/remote/#set-up-a-tunnel-remotely-dashboard-setup)

## 2023.3.1
### Breaking Change
- Running a tunnel without ingress rules defined in configuration file nor from the CLI flags will no longer provide a default ingress rule to localhost:8080 and instead will return HTTP response code 503 for all incoming HTTP requests.

### Security Fixes
- Windows 32 bit machines MSI now defaults to Program Files to install cloudflared. (See CVE-2023-1314). The cloudflared client itself is unaffected. This just changes how the installer works on 32 bit windows machines.

### Bug Fixes
- Fixed a bug that would cause running tunnel on Bastion mode and without ingress rules to crash.

## 2023.2.2
### Notices
- Legacy tunnels were officially deprecated on December 1, 2022. Starting with this version, cloudflared no longer supports connecting legacy tunnels.
- h2mux tunnel connection protocol is no longer supported. Any tunnels still configured to use this protocol will alert and use http2 tunnel protocol instead. We recommend using quic protocol for all tunnels going forward.

## 2023.2.1
### Bug fixes
- Fixed a bug in TCP connection proxy that could result in the connection being closed before all data was written.
- cloudflared now correctly aborts body write if connection to origin service fails after response headers were sent already.
- Fixed a bug introduced in the previous release where debug endpoints were removed.

## 2022.12.0
### Improvements
- cloudflared now attempts to try other edge addresses before falling back to a lower protocol.
- cloudflared tunnel no longer spins up a quick tunnel. The call has to be explicit and provide a --url flag.
- cloudflared will now randomly pick the first or second region to connect to instead of always connecting to region2 first.

## 2022.9.0
### New Features
- cloudflared now rejects ingress rules with invalid http status codes for http_status.

## 2022.8.1
### New Features
- cloudflared now remembers if it connected to a certain protocol successfully. If it did, it does not fall back to a lower
  protocol on connection failures.

## 2022.7.1
### New Features
- It is now possible to connect cloudflared tunnel to Cloudflare Global Network with IPv6. See `cloudflared tunnel --help` and look for `edge-ip-version` for more information. For now, the default behavior is to still connect with IPv4 only.

### Bug Fixes
- Several bug fixes related with QUIC transport (used between cloudflared tunnel and Cloudflare Global Network). Updating to this version is highly recommended.

## 2022.4.0
### Bug Fixes
- `cloudflared tunnel run` no longer logs the Tunnel token or JSON credentials in clear text as those are the secret
that allows to run the Tunnel.

## 2022.3.4
### New Features
- It is now possible to retrieve the credentials that allow to run a Tunnel in case you forgot/lost them. This is
achievable with: `cloudflared tunnel token --cred-file /path/to/file.json TUNNEL`. This new feature only works for
Tunnels created with cloudflared version 2022.3.0 or more recent.

### Bug Fixes
- `cloudflared service install` now starts the underlying agent service on Linux operating system (similarly to the
behaviour in Windows and MacOS).

## 2022.3.3
### Bug Fixes
- `cloudflared service install` now starts the underlying agent service on Windows operating system (similarly to the
behaviour in MacOS).

## 2022.3.1
### Bug Fixes
- Various fixes to the reliability of `quic` protocol, including an edge case that could lead to cloudflared crashing.

## 2022.3.0
### New Features
- It is now possible to configure Ingress Rules to point to an origin served by unix socket with either HTTP or HTTPS.
If the origin starts with `unix:/` then we assume HTTP (existing behavior). Otherwise, the origin can start with
`unix+tls:/` for HTTPS.

## 2022.2.1
### New Features
- This project now has a new LICENSE that is more compliant with open source purposes.

### Bug Fixes
- Various fixes to the reliability of `quic` protocol.

## 2022.1.3
### New Features
- New `cloudflared tunnel vnet` commands to allow for private routing to be virtualized. This means that the same CIDR
can now be used to point to two different Tunnels with `cloudflared tunnel route ip` command. More information will be
made available on blog.cloudflare.com and developers.cloudflare.com/cloudflare-one once the feature is globally available.

### Bug Fixes
- Correctly handle proxying UDP datagrams with no payload.
- Bug fix for origins that use Server-Sent Events (SSE).

## 2022.1.0
### Improvements
- If a specific `protocol` property is defined (e.g. for `quic`), cloudflared no longer falls back to an older protocol
(such as `http2`) in face of connectivity errors. This is important because some features are only supported in a specific
protocol (e.g. UDP proxying only works for `quic`). Hence, if a user chooses a protocol, cloudflared now adheres to it
no matter what.

### Bug Fixes
- Stopping cloudflared running with `quic` protocol now respects graceful shutdown.

## 2021.12.2
### Bug Fixes
- Fix logging when `quic` transport is used and UDP traffic is proxied.
- FIPS compliant cloudflared binaries will now be released as separate artifacts. Recall that these are only for linux
and amd64.

## 2021.12.1
### Bug Fixes
 - Fixes Github issue #530 where cloudflared 2021.12.0 could not reach origins that were HTTPS and using certain encryption
methods forbidden by FIPS compliance (such as Let's Encrypt certificates). To address this fix we have temporarily reverted
FIPS compliance from amd64 linux binaries that was recently introduced (or fixed actually as it was never working before).

## 2021.12.0
### New Features
- Cloudflared binary released for amd64 linux is now FIPS compliant.

### Improvements
- Logging about connectivity to Cloudflare edge now only yields `ERR` level logging if there are no connections to
Cloudflare edge that are active. Otherwise it logs `WARN` level.
 
### Bug Fixes
- Fixes Github issue #501.

## 2021.11.0
### Improvements
- Fallback from `protocol:quic` to `protocol:http2` immediately if UDP connectivity isn't available. This could be because of a firewall or 
egress rule.

## 2021.10.4
### Improvements
- Collect quic transport metrics on RTT, packets and bytes transferred.

### Bug Fixes
- Fix race condition that was writing to the connection after the http2 handler returns.

## 2021.9.2

### New features
- `cloudflared` can now run with `quic` as the underlying tunnel transport protocol. To try it, change or add "protocol: quic" to your config.yml file or
run cloudflared with the `--protocol quic` flag. e.g:
    `cloudflared tunnel --protocol quic run <tunnel-name>`

### Bug Fixes
- Fixed some generic transport bugs in `quic` mode. It's advised to upgrade to at least this version (2021.9.2) when running `cloudflared`
with `quic` protocol.
- `cloudflared` docker images will now show version.


## 2021.8.4
### Improvements
- Temporary tunnels (those hosted on trycloudflare.com that do not require a Cloudflare login) now run as Named Tunnels
underneath. We recall that these tunnels should not be relied upon for production usage as they come with no guarantee
of uptime. Previous cloudflared versions will soon be unable to run legacy temporary tunnels and will require an update
(to this version or more recent).

## 2021.8.2
### Improvements
- Because Equinox os shutting down, all cloudflared releases are now present [here](https://github.com/cloudflare/cloudflared/releases).
[Equinox](https://dl.equinox.io/cloudflare/cloudflared/stable) will no longer receive updates. 

## 2021.8.0
### Bug fixes
- Prevents tunnel from accidentally running when only proxy-dns should run. 

### Improvements
- If auto protocol transport lookup fails, we now default to a transport instead of not connecting.

## 2021.6.0
### Bug Fixes
- Fixes a http2 transport (the new default for Named Tunnels) to work with unix socket origins.


## 2021.5.10
### Bug Fixes
- Fixes a memory leak in h2mux transport that connects cloudflared to Cloudflare edge.


## 2021.5.9
### New Features
- Uses new Worker based login helper service to facilitate token exchange in cloudflared flows.

### Bug Fixes
- Fixes Centos-7 builds.

## 2021.5.8
### New Features
- When creating a DNS record to point a hostname at a tunnel, you can now use --overwrite-dns to overwrite any existing
  DNS records with that hostname. This works both when using the CLI to provision DNS, as well as when starting an adhoc
  named tunnel, e.g.:
  - `cloudflared tunnel route dns --overwrite-dns foo-tunnel foo.example.com`
  - `cloudflared tunnel --overwrite-dns --name foo-tunnel --hostname foo.example.com`

## 2021.5.7
### New Features
- Named Tunnels will automatically select the protocol to connect to Cloudflare's edge network.

## 2021.5.0

### New Features
- It is now possible to run the same tunnel using more than one `cloudflared` instance. This is a server-side change and
  is compatible with any client version that uses Named Tunnels.

  To get started, visit our [developer documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/run-tunnel/deploy-cloudflared-replicas).
- `cloudflared tunnel ingress validate` will now warn about unused keys in your config file. This is helpful for
  detecting typos in your config.
- If `cloudflared` detects it is running inside a Linux container, it will limit itself to use only the number of CPUs
  the pod has been granted, instead of trying to use every CPU available.

## 2021.4.0

### Bug Fixes

- Fixed proxying of websocket requests to avoid possibility of losing initial frames that were sent in the same TCP
  packet as response headers [#345](https://github.com/cloudflare/cloudflared/issues/345).
- `proxy-dns` option now works in conjunction with running a named tunnel [#346](https://github.com/cloudflare/cloudflared/issues/346).

## 2021.3.6

### Bug Fixes

- Reverted 2021.3.5 improvement to use HTTP/2 in a best-effort manner between cloudflared and origin services because
  it was found to break in some cases.

## 2021.3.5

### Improvements

 - HTTP/2 transport is now always chosen if origin server supports it and the service url scheme is HTTPS.
   This was previously done in a best attempt manner.

### Bug Fixes

 - The MacOS binaries were not successfully released in 2021.3.3 and 2021.3.4. This release is aimed at addressing that.

## 2021.3.3

### Improvements

- Tunnel create command, as well as, running ad-hoc tunnels using `cloudflared tunnel -name NAME`, will not overwrite
  existing files when writing tunnel credentials.

### Bug Fixes

- Tunnel cre
... [TRUNCATED]
```

### File: check-fips.sh
```sh
# Pass the path to the executable to check for FIPS compliance
exe=$1

if [ "$(go tool nm "${exe}" | grep -c '_Cfunc__goboringcrypto_')" -eq 0 ]; then
    # Asserts that executable is using FIPS-compliant boringcrypto
    echo "${exe}: missing goboring symbols" >&2
    exit 1
fi
if [ "$(go tool nm "${exe}" | grep -c 'crypto/internal/boring/sig.FIPSOnly')" -eq 0 ]; then
    # Asserts that executable is using FIPS-only schemes
    echo "${exe}: missing fipsonly symbols" >&2
    exit 1
fi

echo "${exe} is FIPS-compliant"

```

### File: config_DISTILLED.md
```md
---
id: config
type: distilled_knowledge
---
# config

## SWALLOW ENGINE DISTILLATION

### File: configuration.go
```go
package config

import (
	"encoding/json"
	"fmt"
	"io"
	"net/url"
	"os"
	"path/filepath"
	"runtime"
	"strconv"
	"time"

	homedir "github.com/mitchellh/go-homedir"
	"github.com/pkg/errors"
	"github.com/rs/zerolog"
	"github.com/urfave/cli/v2"
	yaml "gopkg.in/yaml.v3"

	"github.com/cloudflare/cloudflared/validation"
)

var (
	// DefaultConfigFiles is the file names from which we attempt to read configuration.
	DefaultConfigFiles = []string{"config.yml", "config.yaml"}

	// DefaultUnixConfigLocation is the primary location to find a config file
	DefaultUnixConfigLocation = "/usr/local/etc/cloudflared"

	// DefaultUnixLogLocation is the primary location to find log files
	DefaultUnixLogLocation = "/var/log/cloudflared"

	// Launchd doesn't set root env variables, so there is default
	// Windows default config dir was ~/cloudflare-warp in documentation; let's keep it compatible
	defaultUserConfigDirs = []string{"~/.cloudflared", "~/.cloudflare-warp", "~/cloudflare-warp"}
	defaultNixConfigDirs  = []string{"/etc/cloudflared", DefaultUnixConfigLocation}

	ErrNoConfigFile = fmt.Errorf("Cannot determine default configuration path. No file %v in %v", DefaultConfigFiles, DefaultConfigSearchDirectories())
)

const (
	// BastionFlag is to enable bastion, or jump host, operation
	BastionFlag = "bastion"
)

// DefaultConfigDirectory returns the default directory of the config file
func DefaultConfigDirectory() string {
	if runtime.GOOS == "windows" {
		path := os.Getenv("CFDPATH")
		if path == "" {
			path = filepath.Join(os.Getenv("ProgramFiles(x86)"), "cloudflared")
			if _, err := os.Stat(path); os.IsNotExist(err) { // doesn't exist, so return an empty failure string
				return ""
			}
		}
		return path
	}
	return DefaultUnixConfigLocation
}

// DefaultLogDirectory returns the default directory for log files
func DefaultLogDirectory() string {
	if runtime.GOOS == "windows" {
		return DefaultConfigDirectory()
	}
	return DefaultUnixLogLocation
}

// DefaultConfigPath returns the default location of a config file
func DefaultConfigPath() string {
	dir := DefaultConfigDirectory()
	if dir == "" {
		return DefaultConfigFiles[0]
	}
	return filepath.Join(dir, DefaultConfigFiles[0])
}

// DefaultConfigSearchDirectories returns the default folder locations of the config
func DefaultConfigSearchDirectories() []string {
	dirs := make([]string, len(defaultUserConfigDirs))
	copy(dirs, defaultUserConfigDirs)
	if runtime.GOOS != "windows" {
		dirs = append(dirs, defaultNixConfigDirs...)
	}
	return dirs
}

// FileExists checks to see if a file exist at the provided path.
func FileExists(path string) (bool, error) {
	f, err := os.Open(path)
	if err != nil {
		if os.IsNotExist(err) {
			// ignore missing files
			return false, nil
		}
		return false, err
	}
	_ = f.Close()
	return true, nil
}

// FindDefaultConfigPath returns the first path that contains a config file.
// If none of the combination of DefaultConfigSearchDirectories() and DefaultConfigFiles
// contains a config file, return empty string.
func FindDefaultConfigPath() string {
	for _, configDir := range DefaultConfigSearchDirectories() {
		for _, configFile := range DefaultConfigFiles {
			dirPath, err := homedir.Expand(configDir)
			if err != nil {
				continue
			}
			path := filepath.Join(dirPath, configFile)
			if ok, _ := FileExists(path); ok {
				return path
			}
		}
	}
	return ""
}

// FindOrCreateConfigPath returns the first path that contains a config file
// or creates one in the primary default path if it doesn't exist
func FindOrCreateConfigPath() string {
	path := FindDefaultConfigPath()

	if path == "" {
		// create the default directory if it doesn't exist
		path = DefaultConfigPath()
		if err := os.MkdirAll(filepath.Dir(path), os.ModePerm); err != nil {
			return ""
		}

		// write a new config file out
		file, err := os.Create(path)
		if err != nil {
			return ""
		}
		defer file.Close()

		logDir := DefaultLogDirectory()
		_ = os.MkdirAll(logDir, os.ModePerm) // try and create it. Doesn't matter if it succeed or not, only byproduct will be no logs

		c := Root{
			LogDirectory: logDir,
		}
		if err := yaml.NewEncoder(file).Encode(&c); err != nil {
			return ""
		}
	}

	return path
}

// ValidateUnixSocket ensures --unix-socket param is used exclusively
// i.e. it fails if a user specifies both --url and --unix-socket
func ValidateUnixSocket(c *cli.Context) (string, error) {
	if c.IsSet("unix-socket") && (c.IsSet("url") || c.NArg() > 0) {
		return "", errors.New("--unix-socket must be used exclusively.")
	}
	return c.String("unix-socket"), nil
}

// ValidateUrl will validate url flag correctness. It can be either from --url or argument
// Notice ValidateUnixSocket, it will enforce --unix-socket is not used with --url or argument
func ValidateUrl(c *cli.Context, allowURLFromArgs bool) (*url.URL, error) {
	var url = c.String("url")
	if allowURLFromArgs && c.NArg() > 0 {
		if c.IsSet("url") {
			return nil, errors.New("Specified origin urls using both --url and argument. Decide which one you want, I can only support one.")
		}
		url = c.Args().Get(0)
	}
	validUrl, err := validation.ValidateUrl(url)
	return validUrl, err
}

type UnvalidatedIngressRule struct {
	Hostname      string              `json:"hostname,omitempty"`
	Path          string              `json:"path,omitempty"`
	Service       string              `json:"service,omitempty"`
	OriginRequest OriginRequestConfig `yaml:"originRequest" json:"originRequest"`
}

// OriginRequestConfig is a set of optional fields that users may set to
// customize how cloudflared sends requests to origin services. It is used to set
// up general config that apply to all rules, and also, specific per-rule
// config.
// Note:
// - To specify a time.Duration in go-yaml, use e.g. "3s" or "24h".
// - To specify a time.Duration in json, use int64 of the nanoseconds
type OriginRequestConfig struct {
	// HTTP proxy timeout for establishing a new connection
	ConnectTimeout *CustomDuration `yaml:"connectTimeout" json:"connectTimeout,omitempty"`
	// HTTP proxy timeout for completing a TLS handshake
	TLSTimeout *CustomDuration `yaml:"tlsTimeout" json:"tlsTimeout,omitempty"`
	// HTTP proxy TCP keepalive duration
	TCPKeepAlive *CustomDuration `yaml:"tcpKeepAlive" json:"tcpKeepAlive,omitempty"`
	// HTTP proxy should disable "happy eyeballs" for IPv4/v6 fallback
	NoHappyEyeballs *bool `yaml:"noHappyEyeballs" json:"noHappyEyeballs,omitempty"`
	// HTTP proxy maximum keepalive connection pool size
	KeepAliveConnections *int `yaml:"keepAliveConnections" json:"keepAliveConnections,omitempty"`
	// HTTP proxy timeout for closing an idle connection
	KeepAliveTimeout *CustomDuration `yaml:"keepAliveTimeout" json:"keepAliveTimeout,omitempty"`
	// Sets the HTTP Host header for the local webserver.
	HTTPHostHeader *string `yaml:"httpHostHeader" json:"httpHostHeader,omitempty"`
	// Hostname on the origin server certificate.
	OriginServerName *string `yaml:"originServerName" json:"originServerName,omitempty"`
	// Auto configure the Hostname on the origin server certificate.
	MatchSNIToHost *bool `yaml:"matchSNItoHost" json:"matchSNItoHost,omitempty"`
	// Path to the CA for the certificate of your origin.
	// This option should be used only if your certificate is not signed by Cloudflare.
	CAPool *string `yaml:"caPool" json:"caPool,omitempty"`
	// Disables TLS verification of the certificate presented by your origin.
	// Will allow any certificate from the origin to be accepted.
	// Note: The connection from your machine to Cloudflare's Edge is still encrypted.
	NoTLSVerify *bool `yaml:"noTLSVerify" json:"noTLSVerify,omitempty"`
	// Disables chunked transfer encoding.
	// Useful if you are running a WSGI server.
	DisableChunkedEncoding *bool `yaml:"disableChunkedEncoding" json:"disableChunkedEncoding,omitempty"`
	// Runs as jump host
	BastionMode *bool `yaml:"bastionMode" json:"bastionMode,omitempty"`
	// Listen address for the proxy.
	ProxyAddress *string `yaml:"proxyAddress" json:"proxyAddress,omitempty"`
	// Listen port for the proxy.
	ProxyPort *uint `yaml:"proxyPort" json:"proxyPort,omitempty"`
	// Valid options are 'socks' or empty.
	ProxyType *string `yaml:"proxyType" json:"proxyType,omitempty"`
	// IP rules for the proxy service
	IPRules []IngressIPRule `yaml:"ipRules" json:"ipRules,omitempty"`
	// Attempt to connect to origin with HTTP/2
	Http2Origin *bool `yaml:"http2Origin" json:"http2Origin,omitempty"`
	// Access holds all access related configs
	Access *AccessConfig `yaml:"access" json:"access,omitempty"`
}

type AccessConfig struct {
	// Required when set to true will fail every request that does not arrive through an access authenticated endpoint.
	Required bool `yaml:"required" json:"required,omitempty"`

	// TeamName is the organization team name to get the public key certificates for.
	TeamName string `yaml:"teamName" json:"teamName"`

	// AudTag is the AudTag to verify access JWT against.
	AudTag []string `yaml:"audTag" json:"audTag"`

	Environment string `yaml:"environment" json:"environment,omitempty"`
}

type IngressIPRule struct {
	Prefix *string `yaml:"prefix" json:"prefix"`
	Ports  []int   `yaml:"ports" json:"ports"`
	Allow  bool    `yaml:"allow" json:"allow"`
}

type Configuration struct {
	TunnelID      string `yaml:"tunnel"`
	Ingress       []UnvalidatedIngressRule
	WarpRouting   WarpRoutingConfig   `yaml:"warp-routing"`
	OriginRequest OriginRequestConfig `yaml:"originRequest"`
	sourceFile    string
}

type WarpRoutingConfig struct {
	ConnectTimeout *CustomDuration `yaml:"connectTimeout" json:"connectTimeout,omitempty"`
	MaxActiveFlows *uint64         `yaml:"maxActiveFlows" json:"maxActiveFlows,omitempty"`
	TCPKeepAlive   *CustomDuration `yaml:"tcpKeepAlive" json:"tcpKeepAlive,omitempty"`
}

type configFileSettings struct {
	Configuration `yaml:",inline"`
	// older settings will be aggregated into the generic map, should be read via cli.Context
	Settings map[string]interface{} `yaml:",inline"`
}

func (c *Configuration) Source() string {
	return c.sourceFile
}

func (c *configFileSettings) Int(name string) (int, error) {
	if raw, ok := c.Settings[name]; ok {
		if v, ok := raw.(int); ok {
			return v, nil
		}
		return 0, fmt.Errorf("expected int found %T for %s", raw, name)
	}
	return 0, nil
}

func (c *configFileSettings) Duration(name string) (time.Duration, error) {
	if raw, ok := c.Settings[name]; ok {
		switch v := raw.(type) {
		case time.Duration:
			return v, nil
		case string:
			return time.ParseDuration(v)
		}
		return 0, fmt.Errorf("expected duration found %T for %s", raw, name)
	}
	return 0, nil
}

func (c *configFileSettings) Float64(name string) (float64, error) {
	if raw, ok := c.Settings[name]; ok {
		if v, ok := raw.(float64); ok {
			return v, nil
		}
		return 0, fmt.Errorf("expected float found %T for %s", raw, name)
	}
	return 0, nil
}

func (c *configFileSettings) String(name string) (string, error) {
	if raw, ok := c.Settings[name]; ok {
		if v, ok := raw.(string); ok {
			return v, nil
		}
		return "", fmt.Errorf("expected string found %T for %s", raw, name)
	}
	return "", nil
}

func (c *configFileSettings) StringSlice(name string) ([]string, error) {
	if raw, ok := c.Settings[name]; ok {
		if slice, ok := raw.([]interface{}); ok {
			strSlice := make([]string, len(slice))
			for i, v := range slice {
				str, ok := v.(string)
				if !ok {
					return nil, fmt.Errorf("expected string, found %T for %v", i, v)
				}
				strSlice[i] = str
			}
			return strSlice, nil
		}
		return nil, fmt.Errorf("expected string slice found %T for %s", raw, name)
	}
	return nil, nil
}

func (c *configFileSettings) IntSlice(name string) ([]int, error) {
	if raw, ok := c.Settings[name]; ok {
		if slice, ok := raw.([]interface{}); ok {
			intSlice := make([]int, len(slice))
			for i, v := range slice {
				str, ok := v.(int)
				if !ok {
					return nil, fmt.Errorf("expected int, found %T for %v ", v, v)
				}
				intSlice[i] = str
			}
			return intSlice, nil
		}
		if v, ok := raw.([]int); ok {
			return v, nil
		}
		return nil, fmt.Errorf("expected int slice found %T for %s", raw, name)
	}
	return nil, nil
}

func (c *configFileSettings) Generic(name string) (cli.Generic, error) {
	return nil, errors.New("option type Generic not supported")
}

func (c *configFileSettings) Bool(name string) (bool, error) {
	if raw, ok := c.Settings[name]; ok {
		if v, ok := raw.(bool); ok {
			return v, nil
		}
		return false, fmt.Errorf("expected boolean found %T for %s", raw, name)
	}
	return false, nil
}

var configuration configFileSettings

func GetConfiguration() *Configuration {
	return &configuration.Configuration
}

// ReadConfigFile returns InputSourceContext initialized from the configuration file.
// On repeat calls returns with the same file, returns without reading the file again; however,
// if value of "config" flag changes, will read the new config file
func ReadConfigFile(c *cli.Context, log *zerolog.Logger) (settings *configFileSettings, warnings string, err error) {
	configFile := c.String("config")
	if configuration.Source() == configFile || configFile == "" {
		if configuration.Source() == "" {
			return nil, "", ErrNoConfigFile
		}
		return &configuration, "", nil
	}

	log.Debug().Msgf("Loading configuration from %s", configFile)
	file, err := os.Open(configFile)
	if err != nil {
		// If does not exist and config file was not specificly specified then return ErrNoConfigFile found.
		if os.IsNotExist(err) && !c.IsSet("config") {
			err = ErrNoConfigFile
		}
		return nil, "", err
	}
	defer file.Close()
	if err := yaml.NewDecoder(file).Decode(&configuration); err != nil {
		if err == io.EOF {
			log.Error().Msgf("Configuration file %s was empty", configFile)
			return &configuration, "", nil
		}
		return nil, "", errors.Wrap(err, "error parsing YAML in config file at "+configFile)
	}
	configuration.sourceFile = configFile

	// Parse it again, with strict mode, to find warnings.
	if file, err := os.Open(configFile); err == nil {
		decoder := yaml.NewDecoder(file)
		decoder.KnownFields(true)
		var unusedConfig configFileSettings
		if err := decoder.Decode(&unusedConfig); err != nil {
			warnings = err.Error()
		}
	}

	return &configuration, warnings, nil
}

// A CustomDuration is a Duration that has custom serialization for JSON.
// JSON in Javascript assumes that int fields are 32 bits and Duration fields are deserialized assuming that numbers
// are in nanoseconds, which in 32bit integers limits to just 2 seconds.
// This type assumes that when serializing/deserializing from JSON, that the number is in seconds, while it maintains
// the YAML serde assumptions.
type CustomDuration struct {
	time.Duration
}

func (s CustomDuration) MarshalJSON() ([]byte, error) {
	return json.Marshal(s.Duration.Seconds())
}

func (s *CustomDuration) UnmarshalJSON(data []byte) error {
	seconds, err := strconv.ParseInt(string(d
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
