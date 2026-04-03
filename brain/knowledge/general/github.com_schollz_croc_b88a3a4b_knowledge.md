---
id: github.com-schollz-croc-b88a3a4b-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:19.544717
---

# KNOWLEDGE EXTRACT: github.com_schollz_croc_b88a3a4b
> **Extracted on:** 2026-04-01 10:15:34
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520754/github.com_schollz_croc_b88a3a4b

---

## File: `.gitignore`
```
# If you prefer the allow list template instead of the deny list, see community template:
# https://github.com/github/gitignore/blob/main/community/Golang/Go.AllowList.gitignore
#
# Binaries for programs and plugins
*.exe
*.exe~
*.dll
*.so
*.dylib

# Test binary, built with `go test -c`
*.test

# Output of the go coverage tool, specifically when used with LiteIDE
*.out

# Dependency directories (remove the comment below to include it)
# vendor/

# Go workspace file
go.work
go.work.sum

# Environment variables file
.env

# Croc builds
/croc
croc_v*
```

## File: `.goreleaser.yml`
```yaml
project_name: croc

build:
  main: main.go
  binary: croc
  ldflags: -s -w -X main.Version="v{{.Version}}-{{.Date}}"
  env:
    - CGO_ENABLED=0
  goos:
    - darwin
    - linux
    - windows
    - freebsd
    - netbsd
    - openbsd
    - dragonfly
  goarch:
    - amd64
    - 386
    - arm
    - arm64
  ignore:
    - goos: darwin
      goarch: 386
    - goos: freebsd
      goarch: arm
  goarm:
    - 7

nfpms:
  - formats:
      - deb
    vendor: "schollz.com"
    homepage: "https://schollz.com/software/croc/"
    maintainer: "Zack Scholl <zack.scholl@gmail.com>"
    description: "A simple, secure, and fast way to transfer data."
    license: "MIT"
    file_name_template: "{{.ProjectName}}_{{.Version}}_{{.Os}}-{{.Arch}}"
    replacements:
      amd64: 64bit
      386: 32bit
      arm: ARM
      arm64: ARM64
      darwin: macOS
      linux: Linux
      windows: Windows
      openbsd: OpenBSD
      netbsd: NetBSD
      freebsd: FreeBSD
      dragonfly: DragonFlyBSD

archives:
  - format: tar.gz
    format_overrides:
      - goos: windows
        format: zip
    name_template: "{{.ProjectName}}_{{.Version}}_{{.Os}}-{{.Arch}}"
    replacements:
      amd64: 64bit
      386: 32bit
      arm: ARM
      arm64: ARM64
      darwin: macOS
      linux: Linux
      windows: Windows
      openbsd: OpenBSD
      netbsd: NetBSD
      freebsd: FreeBSD
      dragonfly: DragonFlyBSD
    files:
      - README.md
      - LICENSE
      - zsh_autocomplete
      - bash_autocomplete

brews:
  - tap:
      owner: schollz
      name: homebrew-tap
    folder: Formula
    description: "croc is a tool that allows any two computers to simply and securely transfer files and folders."
    homepage: "https://schollz.com/software/croc/"
    install: |
      bin.install "croc"
    test: |
      system "#{bin}/croc --version"

scoop:
  bucket:
    owner: schollz
    name: scoop-bucket
  homepage: "https://schollz.com/software/croc/"
  description: "croc is a tool that allows any two computers to simply and securely transfer files and folders."
  license: MIT

announce:
  twitter:
    enabled: false
```

## File: `.travis.yml`
```yaml
language: go

go:
  - tip

env:
  - "PATH=/home/travis/gopath/bin:$PATH"

install: true

script:
  - env GO111MODULE=on go build -v
  - env GO111MODULE=on go test -v -cover github.com/schollz/croc/v10/src/compress
  - env GO111MODULE=on go test -v -cover github.com/schollz/croc/v10/src/croc
  - env GO111MODULE=on go test -v -cover github.com/schollz/croc/v10/src/crypt
  - env GO111MODULE=on go test -v -cover github.com/schollz/croc/v10/src/tcp
  - env GO111MODULE=on go test -v -cover github.com/schollz/croc/v10/src/utils
  - env GO111MODULE=on go test -v -cover github.com/schollz/croc/v10/src/comm

branches:
  except:
    - dev
    - win
```

## File: `Dockerfile`
```
FROM golang:1.24-alpine AS builder

RUN apk add --no-cache git gcc musl-dev

WORKDIR /go/croc

COPY . .

RUN go build -v -ldflags="-s -w"

FROM alpine:latest

EXPOSE 9009
EXPOSE 9010
EXPOSE 9011
EXPOSE 9012
EXPOSE 9013

COPY --from=builder /go/croc/croc /go/croc/croc-entrypoint.sh /

USER nobody

# Simple TCP health check with nc!
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD nc -z localhost 9009 || exit 1

ENTRYPOINT ["/croc-entrypoint.sh"]
CMD ["relay"]
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2017-2025 Zack

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
<p align="center">
  <img src="https://user-images.githubusercontent.com/6550035/46709024-9b23ad00-cbf6-11e8-9fb2-ca8b20b7dbec.jpg" width="408px" border="0" alt="croc">
  <br>
  <a href="https://github.com/schollz/croc/releases/latest"><img src="https://img.shields.io/github/v/release/schollz/croc" alt="Version"></a>
  <a href="https://github.com/schollz/croc/actions/workflows/ci.yml"><img src="https://github.com/schollz/croc/actions/workflows/ci.yml/badge.svg" alt="Build Status"></a>
  <a href="https://github.com/sponsors/schollz"><img alt="GitHub Sponsors" src="https://img.shields.io/github/sponsors/schollz"></a>
</p>
<p align="center">
  <strong>This project’s future depends on community support. <a href="https://github.com/sponsors/schollz">Become a sponsor today</a>.</strong>
</p>

## About

`croc` is a tool that allows any two computers to simply and securely transfer files and folders. AFAIK, *croc* is the only CLI file-transfer tool that does **all** of the following:

- Allows **any two computers** to transfer data (using a relay)
- Provides **end-to-end encryption** (using PAKE)
- Enables easy **cross-platform** transfers (Windows, Linux, Mac)
- Allows **multiple file** transfers
- Allows **resuming transfers** that are interrupted
- No need for local server or port-forwarding
- **IPv6-first** with IPv4 fallback
- Can **use a proxy**, like Tor

For more information about `croc`, see [my blog post](https://schollz.com/tinker/croc6/) or read a [recent interview I did](https://console.substack.com/p/console-91).

![Example](src/install/customization.gif)

## Install

You can download [the latest release for your system](https://github.com/schollz/croc/releases/latest), or install a release from the command-line:

```bash
curl https://getcroc.schollz.com | bash
```

### On macOS

Using [Homebrew](https://brew.sh/):

```bash
brew install croc
```

Using [MacPorts](https://www.macports.org/):

```bash
sudo port selfupdate
sudo port install croc
```

### On Windows

You can install the latest release with [Scoop](https://scoop.sh/), [Chocolatey](https://chocolatey.org/), or [Winget](https://learn.microsoft.com/windows/package-manager/):

```bash
scoop install croc
```

```bash
choco install croc
```

```bash
winget install schollz.croc
```

### Using nix-env

You can install the latest release with [Nix](https://nixos.org/):

```bash
nix-env -i croc
```

### On NixOS

You can add this to your [configuration.nix](https://nixos.org/manual/nixos/stable/#ch-configuration):

```nix
environment.systemPackages = [
  pkgs.croc
];
```

### On Alpine Linux

First, install dependencies:

```bash
apk add bash coreutils
wget -qO- https://getcroc.schollz.com | bash
```

### On Arch Linux

Install with `pacman`:

```bash
pacman -S croc
```

### On Fedora

Install with `dnf`:

```bash
dnf install croc
```

### On Gentoo

Install with `portage`:

```bash
emerge net-misc/croc
```

### On Termux

Install with `pkg`:

```bash
pkg install croc
```

### On FreeBSD

Install with `pkg`:

```bash
pkg install croc
```

### On Linux, macOS, and Windows via Conda

You can install from [conda-forge](https://github.com/conda-forge/croc-feedstock) globally with [`pixi`](https://pixi.sh/):

```bash
pixi global install croc
```

Or install into a particular environment with [`conda`](https://docs.conda.io/projects/conda/):

```bash
conda install --channel conda-forge croc
```

### On Linux, macOS via Docker 

Add the following one-liner function to your ~/.profile (works with any POSIX-compliant shell):

```bash
croc() { [ $# -eq 0 ] && set -- ""; mkdir -p "$HOME/.config/croc"; docker run --rm -it --user "$(id -u):$(id -g)" -v "$(pwd):/c" -v "$HOME/.config/croc:/.config/croc" -w /c -e CROC_SECRET docker.io/schollz/croc "$@"; }
```

You can also just paste it in the terminal for current session. On first run Docker will pull the image. `croc` via Docker will only work within the current directory and its subdirectories.

### Build from Source

If you prefer, you can [install Go](https://go.dev/dl/) and build from source (requires Go 1.22+):

```bash
go install github.com/schollz/croc/v10@latest
```

### On Android

There is a 3rd-party F-Droid app [available to download](https://f-droid.org/packages/com.github.howeyc.crocgui/).

## Usage

To send a file, simply do:

```bash
$ croc send [file(s)-or-folder]
Sending 'file-or-folder' (X MB)
Code is: code-phrase
```

Then, to receive the file (or folder) on another computer, run:

```bash
croc code-phrase
```

The code phrase is used to establish password-authenticated key agreement ([PAKE](https://en.wikipedia.org/wiki/Password-authenticated_key_agreement)) which generates a secret key for the sender and recipient to use for end-to-end encryption.

### Customizations & Options

#### Using `croc` on Linux or macOS

On Linux and macOS, the sending and receiving process is slightly different to avoid [leaking the secret via the process name](https://nvd.nist.gov/vuln/detail/CVE-2023-43621). You will need to run `croc` with the secret as an environment variable. For example, to receive with the secret `***`:

```bash
CROC_SECRET=*** croc
```

For single-user systems, the default behavior can be permanently enabled by running:

```bash
croc --classic
```

#### Custom Code Phrase

You can send with your own code phrase (must be more than 6 characters):

```bash
croc send --code [code-phrase] [file(s)-or-folder]
```

#### Allow Overwriting Without Prompt

To automatically overwrite files without prompting, use the `--overwrite` flag:

```bash
croc --yes --overwrite <code>
```

#### Excluding Folders

To exclude folders from being sent, use the `--exclude` flag with comma-delimited exclusions:

```bash
croc send --exclude "node_modules,.venv" [folder]
```

#### Use Pipes - stdin and stdout

You can pipe to `croc`:

```bash
cat [filename] | croc send
```

To receive the file to `stdout`, you can use:

```bash
croc --yes [code-phrase] > out
```

#### Send Text

To send URLs or short text, use:

```bash
croc send --text "hello world"
```

#### Send Multiple Files

You can send multiple files directly by listing the files and/or folders:

```bash
croc send [file1] [file2] [file3] [folder1] [folder2]
```

#### Show QR Code

To show QR code (for mobile devices), use:

```bash
croc send --qr [file(s)-or-folder]
```

#### Use a Proxy

You can send files via a proxy by adding `--socks5`:

```bash
croc --socks5 "127.0.0.1:9050" send SOMEFILE
```

#### Change Encryption Curve

To choose a different elliptic curve for encryption, use the `--curve` flag:

```bash
croc --curve p521 <codephrase>
```

#### Change Hash Algorithm

For faster hashing, use the `imohash` algorithm:

```bash
croc send --hash imohash SOMEFILE
```

#### Clipboard Options

By default, the code phrase is copied to your clipboard. To disable this:

```bash
croc --disable-clipboard send [filename]
```

To copy the full command with the secret as an environment variable (useful on Linux/macOS):

```bash
croc --extended-clipboard send [filename]
```

This copies the full command like `CROC_SECRET="code-phrase" croc` (including any relay/pass flags).

#### Quiet Mode

To suppress all output (useful for scripts and automation):

```bash
croc --quiet send [filename]
```

#### Self-host Relay

You can run your own relay:

```bash
croc relay
```

By default, it uses TCP ports 9009-9013. You can customize the ports (e.g., `croc relay --ports 1111,1112`), but at least **2** ports are required.

To send files using your relay:

```bash
croc --relay "myrelay.example.com:9009" send [filename]
```

#### Self-host Relay with Docker

You can also run a relay with Docker:

```bash
docker run -d -p 9009-9013:9009-9013 -e CROC_PASS='YOURPASSWORD' docker.io/schollz/croc
```

To send files using your custom relay:

```bash
croc --pass YOURPASSWORD --relay "myreal.example.com:9009" send [filename]
```

## Acknowledgements

`croc` has evolved through many iterations, and I am thankful for the contributions! Special thanks to:

- [@warner](https://github.com/warner) for the [idea](https://github.com/magic-wormhole/magic-wormhole)
- [@tscholl2](https://github.com/tscholl2) for the [encryption gists](https://gist.github.com/tscholl2/dc7dc15dc132ea70a98e8542fefffa28)
- [@skorokithakis](https://github.com/skorokithakis) for [proxying two connections](https://www.stavros.io/posts/proxying-two-connections-go/)

And many more!
```

## File: `croc-entrypoint.sh`
```bash
#!/bin/sh
set -e

if [ -n "$CROC_PASS" ]; then
    set -- --pass "$CROC_PASS" "$@"
fi

exec /croc "$@"
```

## File: `croc.service`
```
[Unit]
Description=croc relay
After=network.target

[Service]
Type=simple
DynamicUser=yes
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
ExecStart=/usr/bin/croc relay

[Install]
WantedBy=multi-user.target
```

## File: `go.mod`
```
module github.com/schollz/croc/v10

go 1.25.0

require (
	github.com/cespare/xxhash/v2 v2.3.0
	github.com/chzyer/readline v1.5.1
	github.com/denisbrodbeck/machineid v1.0.1
	github.com/kalafut/imohash v1.1.1
	github.com/magisterquis/connectproxy v0.0.0-20200725203833-3582e84f0c9b
	github.com/minio/highwayhash v1.0.3
	github.com/sabhiram/go-gitignore v0.0.0-20210923224102-525f6e181f06
	github.com/schollz/cli/v2 v2.2.1
	github.com/schollz/logger v1.2.0
	github.com/schollz/pake/v3 v3.1.1
	github.com/schollz/peerdiscovery v1.7.6
	github.com/schollz/progressbar/v3 v3.19.0
	github.com/skip2/go-qrcode v0.0.0-20200617195104-da1b6568686e
	github.com/stretchr/testify v1.11.1
	golang.org/x/crypto v0.48.0
	golang.org/x/net v0.51.0
	golang.org/x/sys v0.41.0
	golang.org/x/term v0.40.0
	golang.org/x/time v0.14.0
)

require (
	filippo.io/edwards25519 v1.2.0 // indirect
	github.com/cpuguy83/go-md2man/v2 v2.0.7 // indirect
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/mitchellh/colorstring v0.0.0-20190213212951-d06e56a500db // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	github.com/rivo/uniseg v0.4.7 // indirect
	github.com/russross/blackfriday/v2 v2.1.0 // indirect
	github.com/tscholl2/siec v0.0.0-20240310163802-c2c6f6198406 // indirect
	github.com/twmb/murmur3 v1.1.8 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)
```

## File: `go.sum`
```
filippo.io/edwards25519 v1.2.0 h1:crnVqOiS4jqYleHd9vaKZ+HKtHfllngJIiOpNpoJsjo=
filippo.io/edwards25519 v1.2.0/go.mod h1:xzAOLCNug/yB62zG1bQ8uziwrIqIuxhctzJT18Q77mc=
github.com/BurntSushi/toml v0.3.1/go.mod h1:xHWCNGjB5oqiDr8zfno3MHue2Ht5sIBksp03qcyfWMU=
github.com/cespare/xxhash/v2 v2.3.0 h1:UL815xU9SqsFlibzuggzjXhog7bL6oX9BbNZnL2UFvs=
github.com/cespare/xxhash/v2 v2.3.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/chengxilo/virtualterm v1.0.4 h1:Z6IpERbRVlfB8WkOmtbHiDbBANU7cimRIof7mk9/PwM=
github.com/chengxilo/virtualterm v1.0.4/go.mod h1:DyxxBZz/x1iqJjFxTFcr6/x+jSpqN0iwWCOK1q10rlY=
github.com/chzyer/logex v1.2.1 h1:XHDu3E6q+gdHgsdTPH6ImJMIp436vR6MPtH8gP05QzM=
github.com/chzyer/logex v1.2.1/go.mod h1:JLbx6lG2kDbNRFnfkgvh4eRJRPX1QCoOIWomwysCBrQ=
github.com/chzyer/readline v1.5.1 h1:upd/6fQk4src78LMRzh5vItIt361/o4uq553V8B5sGI=
github.com/chzyer/readline v1.5.1/go.mod h1:Eh+b79XXUwfKfcPLepksvw2tcLE/Ct21YObkaSkeBlk=
github.com/chzyer/test v1.0.0 h1:p3BQDXSxOhOG0P9z6/hGnII4LGiEPOYBhs8asl/fC04=
github.com/chzyer/test v1.0.0/go.mod h1:2JlltgoNkt4TW/z9V/IzDdFaMTM2JPIi26O1pF38GC8=
github.com/cpuguy83/go-md2man/v2 v2.0.0-20190314233015-f79a8a8ca69d/go.mod h1:maD7wRr/U5Z6m/iR4s+kqSMx2CaBsrgA7czyZG/E6dU=
github.com/cpuguy83/go-md2man/v2 v2.0.7 h1:zbFlGlXEAKlwXpmvle3d8Oe3YnkKIK4xSRTd3sHPnBo=
github.com/cpuguy83/go-md2man/v2 v2.0.7/go.mod h1:oOW0eioCTA6cOiMLiUPZOpcVxMig6NIQQ7OS05n1F4g=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/denisbrodbeck/machineid v1.0.1 h1:geKr9qtkB876mXguW2X6TU4ZynleN6ezuMSRhl4D7AQ=
github.com/denisbrodbeck/machineid v1.0.1/go.mod h1:dJUwb7PTidGDeYyUBmXZ2GphQBbjJCrnectwCyxcUSI=
github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/kalafut/imohash v1.1.1 h1:G/HYtKgteQSVU96LidSJEbUGoZOMiBcuXYxbeb2W9e4=
github.com/kalafut/imohash v1.1.1/go.mod h1:6cn9lU0Sj8M4eu9UaQm1kR/5y3k/ayB68yntRhGloL4=
github.com/magisterquis/connectproxy v0.0.0-20200725203833-3582e84f0c9b h1:xZ59n7Frzh8CwyfAapUZLSg+gXH5m63YEaFCMpDHhpI=
github.com/magisterquis/connectproxy v0.0.0-20200725203833-3582e84f0c9b/go.mod h1:uDd4sYVYsqcxAB8j+Q7uhL6IJCs/r1kxib1HV4bgOMg=
github.com/mattn/go-runewidth v0.0.16 h1:E5ScNMtiwvlvB5paMFdw9p4kSQzbXFikJ5SQO6TULQc=
github.com/mattn/go-runewidth v0.0.16/go.mod h1:Jdepj2loyihRzMpdS35Xk/zdY8IAYHsh153qUoGf23w=
github.com/minio/highwayhash v1.0.3 h1:kbnuUMoHYyVl7szWjSxJnxw11k2U709jqFPPmIUyD6Q=
github.com/minio/highwayhash v1.0.3/go.mod h1:GGYsuwP/fPD6Y9hMiXuapVvlIUEhFhMTh0rxU3ik1LQ=
github.com/mitchellh/colorstring v0.0.0-20190213212951-d06e56a500db h1:62I3jR2EmQ4l5rM/4FEfDWcRD+abF5XlKShorW5LRoQ=
github.com/mitchellh/colorstring v0.0.0-20190213212951-d06e56a500db/go.mod h1:l0dey0ia/Uv7NcFFVbCLtqEBQbrT4OCwCSKTEv6enCw=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rivo/uniseg v0.4.7 h1:WUdvkW8uEhrYfLC4ZzdpI2ztxP1I582+49Oc5Mq64VQ=
github.com/rivo/uniseg v0.4.7/go.mod h1:FN3SvrM+Zdj16jyLfmOkMNblXMcoc8DfTHruCPUcx88=
github.com/russross/blackfriday/v2 v2.0.1/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
github.com/russross/blackfriday/v2 v2.1.0 h1:JIOH55/0cWyOuilr9/qlrm0BSXldqnqwMsf35Ld67mk=
github.com/russross/blackfriday/v2 v2.1.0/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
github.com/sabhiram/go-gitignore v0.0.0-20210923224102-525f6e181f06 h1:OkMGxebDjyw0ULyrTYWeN0UNCCkmCWfjPnIA2W6oviI=
github.com/sabhiram/go-gitignore v0.0.0-20210923224102-525f6e181f06/go.mod h1:+ePHsJ1keEjQtpvf9HHw0f4ZeJ0TLRsxhunSI2hYJSs=
github.com/schollz/cli/v2 v2.2.1 h1:ou22Mj7ZPjrKz+8k2iDTWaHskEEV5NiAxGrdsCL36VU=
github.com/schollz/cli/v2 v2.2.1/go.mod h1:My6bfphRLZUhZdlFUK8scAxMWHydE7k4s2ed2Dtnn+s=
github.com/schollz/logger v1.2.0 h1:5WXfINRs3lEUTCZ7YXhj0uN+qukjizvITLm3Ca2m0Ho=
github.com/schollz/logger v1.2.0/go.mod h1:P6F4/dGMGcx8wh+kG1zrNEd4vnNpEBY/mwEMd/vn6AM=
github.com/schollz/pake/v3 v3.1.1 h1:lyoU5uNQ3thfjEzrahgxWWBm6+pbI1F2KAZ3gs6LIV8=
github.com/schollz/pake/v3 v3.1.1/go.mod h1:420+m3AakXcS0n7Uwc7eRs2CosQ2YfE/vKcIkilvqZc=
github.com/schollz/peerdiscovery v1.7.6 h1:HJjU1cXcNGfZgenC/vbry9F6CH9B8f+QYcTipZLbtDg=
github.com/schollz/peerdiscovery v1.7.6/go.mod h1:iTa0MWSPy49jJ2HcXL5oSSnFsd6olEUorAFljxbnj2I=
github.com/schollz/progressbar/v3 v3.19.0 h1:Ea18xuIRQXLAUidVDox3AbwfUhD0/1IvohyTutOIFoc=
github.com/schollz/progressbar/v3 v3.19.0/go.mod h1:IsO3lpbaGuzh8zIMzgY3+J8l4C8GjO0Y9S69eFvNsec=
github.com/shurcooL/sanitized_anchor_name v1.0.0/go.mod h1:1NzhyTcUVG4SuEtjjoZeVRXNmyL/1OwPU0+IJeTBvfc=
github.com/skip2/go-qrcode v0.0.0-20200617195104-da1b6568686e h1:MRM5ITcdelLK2j1vwZ3Je0FKVCfqOLp5zO6trqMLYs0=
github.com/skip2/go-qrcode v0.0.0-20200617195104-da1b6568686e/go.mod h1:XV66xRDqSt+GTGFMVlhk3ULuV0y9ZmzeVGR4mloJI3M=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.6.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.11.1 h1:7s2iGBzp5EwR7/aIZr8ao5+dra3wiQyKjjFuvgVKu7U=
github.com/stretchr/testify v1.11.1/go.mod h1:wZwfW3scLgRK+23gO65QZefKpKQRnfz6sD981Nm4B6U=
github.com/tscholl2/siec v0.0.0-20240310163802-c2c6f6198406 h1:sDWDZkwYqX0jvLWstKzFwh+pYhQNaVg65BgSkCP/f7U=
github.com/tscholl2/siec v0.0.0-20240310163802-c2c6f6198406/go.mod h1:KL9+ubr1JZdaKjgAaHr+tCytEncXBa1pR6FjbTsOJnw=
github.com/twmb/murmur3 v1.1.5/go.mod h1:Qq/R7NUyOfr65zD+6Q5IHKsJLwP7exErjN6lyyq3OSQ=
github.com/twmb/murmur3 v1.1.8 h1:8Yt9taO/WN3l08xErzjeschgZU2QSrwm1kclYq+0aRg=
github.com/twmb/murmur3 v1.1.8/go.mod h1:Qq/R7NUyOfr65zD+6Q5IHKsJLwP7exErjN6lyyq3OSQ=
github.com/yuin/goldmark v1.4.13/go.mod h1:6yULJ656Px+3vBD8DxQVa3kxgyrAnzto9xy5taEt/CY=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20210921155107-089bfa567519/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/crypto v0.13.0/go.mod h1:y6Z2r+Rw4iayiXXAIxJIDAJ1zMW4yaTpebo8fPOliYc=
golang.org/x/crypto v0.19.0/go.mod h1:Iy9bg/ha4yyC70EfRS8jz+B6ybOBKMaSxLj6P6oBDfU=
golang.org/x/crypto v0.23.0/go.mod h1:CKFgDieR+mRhux2Lsu27y0fO304Db0wZe70UKqHu0v8=
golang.org/x/crypto v0.32.0/go.mod h1:ZnnJkOaASj8g0AjIduWNlq2NRxL0PlBrbKVyZ6V/Ugc=
golang.org/x/crypto v0.48.0 h1:/VRzVqiRSggnhY7gNRxPauEQ5Drw9haKdM0jqfcCFts=
golang.org/x/crypto v0.48.0/go.mod h1:r0kV5h3qnFPlQnBSrULhlsRfryS2pmewsg+XfMgkVos=
golang.org/x/mod v0.6.0-dev.0.20220419223038-86c51ed26bb4/go.mod h1:jJ57K6gSWd91VN4djpZkiMVwK6gcyfeH4XE8wZrZaV4=
golang.org/x/mod v0.8.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/mod v0.12.0/go.mod h1:iBbtSCu2XBx23ZKBPSOrRkjjQPZFPuis4dIYUhu/chs=
golang.org/x/mod v0.15.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/mod v0.17.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/net v0.0.0-20190620200207-3b0461eec859/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20210226172049-e18ecbb05110/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/net v0.0.0-20220722155237-a158d28d115b/go.mod h1:XRhObCWvk6IyKnWLug+ECip1KBveYUHfp+8e9klMJ9c=
golang.org/x/net v0.6.0/go.mod h1:2Tu9+aMcznHK/AK1HMvgo6xiTLG5rD5rZLDS+rp2Bjs=
golang.org/x/net v0.10.0/go.mod h1:0qNGK6F8kojg2nk9dLZ2mShWaEBan6FAoqfSigmmuDg=
golang.org/x/net v0.15.0/go.mod h1:idbUs1IY1+zTqbi8yxTbhexhEEk5ur9LInksu6HrEpk=
golang.org/x/net v0.21.0/go.mod h1:bIjVDfnllIU7BJ2DNgfnXvpSvtn8VRwhlsaeUTyUS44=
golang.org/x/net v0.25.0/go.mod h1:JkAGAh7GEvH74S6FOH42FLoXpXbE/aqXSrIQjXgsiwM=
golang.org/x/net v0.34.0/go.mod h1:di0qlW3YNM5oh6GqDGQr92MyTozJPmybPK4Ev/Gm31k=
golang.org/x/net v0.51.0 h1:94R/GTO7mt3/4wIKpcR5gkGmRLOuE/2hNGeWq/GBIFo=
golang.org/x/net v0.51.0/go.mod h1:aamm+2QF5ogm02fjy5Bb7CQ0WMt1/WVM7FtyaTLlA9Y=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20220722155255-886fb9371eb4/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.1.0/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.3.0/go.mod h1:FU7BRWz2tNW+3quACPkgCx/L+uEAv1htQ0V83Z9Rj+Y=
golang.org/x/sync v0.6.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.7.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.10.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20201119102817-f84b799fce68/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210615035016-665e8c7367d1/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220310020820-b874c991c1a5/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220520151302-bc2c85ada10a/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220722155257-8c9f86f7a55f/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.5.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.8.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.12.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.17.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/sys v0.20.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/sys v0.21.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/sys v0.29.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/sys v0.41.0 h1:Ivj+2Cp/ylzLiEU89QhWblYnOE9zerudt9Ftecq2C6k=
golang.org/x/sys v0.41.0/go.mod h1:OgkHotnGiDImocRcuBABYBEXf8A9a87e/uXjp9XT3ks=
golang.org/x/telemetry v0.0.0-20240228155512-f48c80bd79b2/go.mod h1:TeRTkGYfJXctD9OcfyVLyj2J3IxLnKwHJR8f4D8a3YE=
golang.org/x/term v0.0.0-20201126162022-7de9c90e9dd1/go.mod h1:bj7SfCRtBDWHUb9snDiAeCFNEtKQo2Wmx5Cou7ajbmo=
golang.org/x/term v0.0.0-20210927222741-03fcf44c2211/go.mod h1:jbD1KX2456YbFQfuXm/mYQcufACuNUgVhRMnK/tPxf8=
golang.org/x/term v0.5.0/go.mod h1:jMB1sMXY+tzblOD4FWmEbocvup2/aLOaQEp7JmGp78k=
golang.org/x/term v0.8.0/go.mod h1:xPskH00ivmX89bAKVGSKKtLOWNx2+17Eiy94tnKShWo=
golang.org/x/term v0.12.0/go.mod h1:owVbMEjm3cBLCHdkQu9b1opXd4ETQWc3BhuQGKgXgvU=
golang.org/x/term v0.17.0/go.mod h1:lLRBjIVuehSbZlaOtGMbcMncT+aqLLLmKrsjNrUguwk=
golang.org/x/term v0.20.0/go.mod h1:8UkIAJTvZgivsXaD6/pH6U9ecQzZ45awqEOzuCvwpFY=
golang.org/x/term v0.28.0/go.mod h1:Sw/lC2IAUZ92udQNf3WodGtn4k/XoLyZoh8v/8uiwek=
golang.org/x/term v0.40.0 h1:36e4zGLqU4yhjlmxEaagx2KuYbJq3EwY8K943ZsHcvg=
golang.org/x/term v0.40.0/go.mod h1:w2P8uVp06p2iyKKuvXIm7N/y0UCRt3UfJTfZ7oOpglM=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.3/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.7/go.mod h1:u+2+/6zg+i71rQMx5EYifcz6MCKuco9NR6JIITiCfzQ=
golang.org/x/text v0.7.0/go.mod h1:mrYo+phRRbMaCq/xk9113O4dZlRixOauAjOtrjsXDZ8=
golang.org/x/text v0.9.0/go.mod h1:e1OnstbJyHTd6l/uOt8jFFHp6TRDWZR/bV3emEE/zU8=
golang.org/x/text v0.13.0/go.mod h1:TvPlkZtksWOMsz7fbANvkp4WM8x/WCo/om8BMLbz+aE=
golang.org/x/text v0.14.0/go.mod h1:18ZOQIKpY8NJVqYksKHtTdi31H5itFRjB5/qKTNYzSU=
golang.org/x/text v0.15.0/go.mod h1:18ZOQIKpY8NJVqYksKHtTdi31H5itFRjB5/qKTNYzSU=
golang.org/x/text v0.21.0/go.mod h1:4IBbMaMmOPCJ8SecivzSH54+73PCFmPWxNTLm+vZkEQ=
golang.org/x/time v0.14.0 h1:MRx4UaLrDotUKUdCIqzPC48t1Y9hANFKIRpNx+Te8PI=
golang.org/x/time v0.14.0/go.mod h1:eL/Oa2bBBK0TkX57Fyni+NgnyQQN4LitPmob2Hjnqw4=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20191119224855-298f0cb1881e/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.1.12/go.mod h1:hNGJHUnrk76NpqgfD5Aqm5Crs+Hm0VOH/i9J2+nxYbc=
golang.org/x/tools v0.6.0/go.mod h1:Xwgl3UAJ/d3gWutnCtw505GrjyAbvKui8lOU390QaIU=
golang.org/x/tools v0.13.0/go.mod h1:HvlwmtVNQAhOuCjW7xxvovg8wbNq7LwfXh/k7wXUl58=
golang.org/x/tools v0.21.1-0.20240508182429-e35e4ccd0d2d/go.mod h1:aiJjzUbINMkxbQROHiO6hDPo2LHcIPhhQsa9DLh0yGk=
golang.org/x/xerrors v0.0.0-20190717185122-a985d3407aa7/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405 h1:yhCVgyC4o1eVCa2tZl7eS0r+SDo693bJlVdllGtEeKM=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `main.go`
```go
package main

//go:generate go run src/install/updateversion.go
//go:generate git commit -am "bump $VERSION"
//go:generate git tag -af v$VERSION -m "v$VERSION"

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"

	"github.com/schollz/croc/v10/src/cli"
	"github.com/schollz/croc/v10/src/utils"
)

func main() {
	// "github.com/pkg/profile"
	// go func() {
	// 	for {
	// 		f, err := os.Create("croc.pprof")
	// 		if err != nil {
	// 			panic(err)
	// 		}
	// 		runtime.GC() // get up-to-date statistics
	// 		if err := pprof.WriteHeapProfile(f); err != nil {
	// 			panic(err)
	// 		}
	// 		f.Close()
	// 		time.Sleep(3 * time.Second)
	// 		fmt.Println("wrote profile")
	// 	}
	// }()

	// Create a channel to receive OS signals
	sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	go func() {
		if err := cli.Run(); err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
		// Exit the program gracefully
		utils.RemoveMarkedFiles()
		os.Exit(0)
	}()

	// Wait for a termination signal
	<-sigs
	utils.RemoveMarkedFiles()

	// Exit the program gracefully
	os.Exit(0)
}
```

## File: `src/cli/cli.go`
```go
package cli

import (
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"os"
	"path"
	"path/filepath"
	"runtime"
	"strconv"
	"strings"
	"time"

	"github.com/chzyer/readline"
	"github.com/schollz/cli/v2"
	"github.com/schollz/croc/v10/src/comm"
	"github.com/schollz/croc/v10/src/croc"
	"github.com/schollz/croc/v10/src/mnemonicode"
	"github.com/schollz/croc/v10/src/models"
	"github.com/schollz/croc/v10/src/tcp"
	"github.com/schollz/croc/v10/src/utils"
	log "github.com/schollz/logger"
	"github.com/schollz/pake/v3"
)

// Version specifies the version
var Version string

// Run will run the command line program
func Run() (err error) {
	// use all of the processors
	runtime.GOMAXPROCS(runtime.NumCPU())

	app := cli.NewApp()
	app.Name = "croc"
	if Version == "" {
		Version = "v10.4.2"
	}
	app.Version = Version
	app.Compiled = time.Now()
	app.Usage = "easily and securely transfer stuff from one computer to another"
	app.UsageText = `croc [GLOBAL OPTIONS] [COMMAND] [COMMAND OPTIONS] [filename(s) or folder]

   USAGE EXAMPLES:
   Send a file:
      croc send file.txt

      -git to respect your .gitignore
   Send multiple files:
      croc send file1.txt file2.txt file3.txt
    or
      croc send *.jpg

   Send everything in a folder:
      croc send example-folder-name

   Send a file with a custom code:
      croc send --code secret-code file.txt

   Receive a file using code:
      croc secret-code`
	app.Commands = []*cli.Command{
		{
			Name:        "send",
			Usage:       "send file(s), or folder (see options with croc send -h)",
			Description: "send file(s), or folder, over the relay",
			ArgsUsage:   "[filename(s) or folder]",
			Flags: []cli.Flag{
				&cli.BoolFlag{Name: "zip", Usage: "zip folder before sending"},
				&cli.StringFlag{Name: "code", Aliases: []string{"c"}, Usage: "codephrase used to connect to relay"},
				&cli.StringFlag{Name: "hash", Value: "xxhash", Usage: "hash algorithm (xxhash, imohash, md5)"},
				&cli.StringFlag{Name: "text", Aliases: []string{"t"}, Usage: "send some text"},
				&cli.BoolFlag{Name: "no-local", Usage: "disable local relay when sending"},
				&cli.BoolFlag{Name: "no-multi", Usage: "disable multiplexing"},
				&cli.BoolFlag{Name: "git", Usage: "enable .gitignore respect / don't send ignored files"},
				&cli.IntFlag{Name: "port", Value: 9009, Usage: "base port for the relay"},
				&cli.IntFlag{Name: "transfers", Value: 4, Usage: "number of ports to use for transfers"},
				&cli.BoolFlag{Name: "qrcode", Aliases: []string{"qr"}, Usage: "show receive code as a qrcode"},
				&cli.StringFlag{Name: "exclude", Value: "", Usage: "exclude files if they contain any of the comma separated strings"},
				&cli.StringFlag{Name: "socks5", Value: "", Usage: "add a socks5 proxy", EnvVars: []string{"SOCKS5_PROXY"}},
				&cli.StringFlag{Name: "connect", Value: "", Usage: "add a http proxy", EnvVars: []string{"HTTP_PROXY"}},
			},
			HelpName: "croc send",
			Action:   send,
		},
		{
			Name:        "relay",
			Usage:       "start your own relay (optional)",
			Description: "start relay",
			HelpName:    "croc relay",
			Action:      relay,
			Flags: []cli.Flag{
				&cli.StringFlag{Name: "host", Usage: "host of the relay"},
				&cli.StringFlag{Name: "ports", Value: "9009,9010,9011,9012,9013", Usage: "ports of the relay"},
				&cli.IntFlag{Name: "port", Value: 9009, Usage: "base port for the relay"},
				&cli.IntFlag{Name: "transfers", Value: 5, Usage: "number of ports to use for relay"},
			},
		},
		{
			Name:   "generate-fish-completion",
			Usage:  "generate fish completion and output to stdout",
			Hidden: true,
			Action: func(ctx *cli.Context) error {
				completion, err := ctx.App.ToFishCompletion()
				if err != nil {
					return err
				}
				fmt.Print(completion)
				return nil
			},
		},
	}
	app.Flags = []cli.Flag{
		&cli.BoolFlag{Name: "internal-dns", Usage: "use a built-in DNS stub resolver rather than the host operating system"},
		&cli.BoolFlag{Name: "classic", Usage: "toggle between the classic mode (insecure due to local attack vector) and new mode (secure)"},
		&cli.BoolFlag{Name: "remember", Usage: "save these settings to reuse next time"},
		&cli.BoolFlag{Name: "debug", Usage: "toggle debug mode"},
		&cli.BoolFlag{Name: "yes", Usage: "automatically agree to all prompts"},
		&cli.BoolFlag{Name: "stdout", Usage: "redirect file to stdout"},
		&cli.BoolFlag{Name: "no-compress", Usage: "disable compression"},
		&cli.BoolFlag{Name: "ask", Usage: "make sure sender and recipient are prompted"},
		&cli.BoolFlag{Name: "local", Usage: "force to use only local connections"},
		&cli.BoolFlag{Name: "ignore-stdin", Usage: "ignore piped stdin"},
		&cli.BoolFlag{Name: "overwrite", Usage: "do not prompt to overwrite or resume"},
		&cli.BoolFlag{Name: "testing", Usage: "flag for testing purposes"},
		&cli.BoolFlag{Name: "quiet", Usage: "disable all output"},
		&cli.BoolFlag{Name: "disable-clipboard", Usage: "disable copy to clipboard"},
		&cli.BoolFlag{Name: "extended-clipboard", Usage: "copy full command with secret as env variable to clipboard"},
		&cli.StringFlag{Name: "multicast", Value: "239.255.255.250", Usage: "multicast address to use for local discovery"},
		&cli.StringFlag{Name: "curve", Value: "p256", Usage: "choose an encryption curve (" + strings.Join(pake.AvailableCurves(), ", ") + ")"},
		&cli.StringFlag{Name: "ip", Value: "", Usage: "set sender ip if known e.g. 10.0.0.1:9009, [::1]:9009"},
		&cli.StringFlag{Name: "relay", Value: models.DEFAULT_RELAY, Usage: "address of the relay", EnvVars: []string{"CROC_RELAY"}},
		&cli.StringFlag{Name: "relay6", Value: models.DEFAULT_RELAY6, Usage: "ipv6 address of the relay", EnvVars: []string{"CROC_RELAY6"}},
		&cli.StringFlag{Name: "out", Value: ".", Usage: "specify an output folder to receive the file"},
		&cli.StringFlag{Name: "pass", Value: models.DEFAULT_PASSPHRASE, Usage: "password for the relay", EnvVars: []string{"CROC_PASS"}},
		&cli.StringFlag{Name: "socks5", Value: "", Usage: "add a socks5 proxy", EnvVars: []string{"SOCKS5_PROXY"}},
		&cli.StringFlag{Name: "connect", Value: "", Usage: "add a http proxy", EnvVars: []string{"HTTP_PROXY"}},
		&cli.StringFlag{Name: "throttleUpload", Value: "", Usage: "throttle the upload speed e.g. 500k"},
	}
	app.EnableBashCompletion = true
	app.HideHelp = false
	app.HideVersion = false
	app.Action = func(c *cli.Context) error {
		allStringsAreFiles := func(strs []string) bool {
			for _, str := range strs {
				if !utils.Exists(str) {
					return false
				}
			}
			return true
		}

		// check if "classic" is set
		classicFile := getClassicConfigFile(true)
		classicInsecureMode := utils.Exists(classicFile)
		if c.Bool("classic") {
			if classicInsecureMode {
				// classic mode not enabled
				fmt.Print(`Classic mode is currently ENABLED.

Disabling this mode will prevent the shared secret from being visible
on the host's process list when passed via the command line. On a
multi-user system, this will help ensure that other local users cannot
access the shared secret and receive the files instead of the intended
recipient.

Do you wish to continue to DISABLE the classic mode? (y/N) `)
				choice := strings.ToLower(utils.GetInput(""))
				if choice == "y" || choice == "yes" {
					os.Remove(classicFile)
					fmt.Print("\nClassic mode DISABLED.\n\n")
					fmt.Print(`To send and receive, export the CROC_SECRET variable with the code phrase:

  Send:    CROC_SECRET=*** croc send file.txt

  Receive: CROC_SECRET=*** croc` + "\n\n")
				} else {
					fmt.Print("\nClassic mode ENABLED.\n")

				}
			} else {
				// enable classic mode
				// touch the file
				fmt.Print(`Classic mode is currently DISABLED.

Please note that enabling this mode will make the shared secret visible
on the host's process list when passed via the command line. On a
multi-user system, this could allow other local users to access the
shared secret and receive the files instead of the intended recipient.

Do you wish to continue to enable the classic mode? (y/N) `)
				choice := strings.ToLower(utils.GetInput(""))
				if choice == "y" || choice == "yes" {
					fmt.Print("\nClassic mode ENABLED.\n\n")
					os.WriteFile(classicFile, []byte("enabled"), 0o644)
					fmt.Print(`To send and receive, use the code phrase:

  Send:    croc send --code *** file.txt

  Receive: croc ***` + "\n\n")
				} else {
					fmt.Print("\nClassic mode DISABLED.\n")
				}
			}
			os.Exit(0)
		}

		// if trying to send but forgot send, let the user know
		if c.Args().Present() && allStringsAreFiles(c.Args().Slice()) {
			fnames := []string{}
			for _, fpath := range c.Args().Slice() {
				_, basename := filepath.Split(fpath)
				fnames = append(fnames, "'"+basename+"'")
			}
			promptMessage := fmt.Sprintf("Did you mean to send %s? (Y/n) ", strings.Join(fnames, ", "))
			choice := strings.ToLower(utils.GetInput(promptMessage))
			if choice == "" || choice == "y" || choice == "yes" {
				return send(c)
			}
		}

		return receive(c)
	}

	return app.Run(os.Args)
}

func setDebugLevel(c *cli.Context) {
	if c.Bool("quiet") {
		log.SetLevel("error")
	} else if c.Bool("debug") {
		log.SetLevel("debug")
		log.Debug("debug mode on")
		// print the public IP address
		ip, err := utils.PublicIP()
		if err == nil {
			log.Debugf("public IP address: %s", ip)
		} else {
			log.Debug(err)
		}

	} else {
		log.SetLevel("info")
	}
}

func getSendConfigFile(requireValidPath bool) string {
	configFile, err := utils.GetConfigDir(requireValidPath)
	if err != nil {
		log.Error(err)
		return ""
	}
	return path.Join(configFile, "send.json")
}

func getClassicConfigFile(requireValidPath bool) string {
	configFile, err := utils.GetConfigDir(requireValidPath)
	if err != nil {
		log.Error(err)
		return ""
	}
	return path.Join(configFile, "classic_enabled")
}

func getReceiveConfigFile(requireValidPath bool) (string, error) {
	configFile, err := utils.GetConfigDir(requireValidPath)
	if err != nil {
		log.Error(err)
		return "", err
	}
	return path.Join(configFile, "receive.json"), nil
}

func determinePass(c *cli.Context) (pass string) {
	pass = c.String("pass")
	b, err := os.ReadFile(pass)
	if err == nil {
		pass = strings.TrimSpace(string(b))
	}
	return
}

func send(c *cli.Context) (err error) {
	setDebugLevel(c)
	comm.Socks5Proxy = c.String("socks5")
	comm.HttpProxy = c.String("connect")

	portParam := c.Int("port")
	if portParam == 0 {
		portParam = 9009
	}
	transfersParam := c.Int("transfers")
	if transfersParam == 0 {
		transfersParam = 4
	}
	excludeStrings := []string{}
	for _, v := range strings.Split(c.String("exclude"), ",") {
		v = strings.ToLower(strings.TrimSpace(v))
		if v != "" {
			excludeStrings = append(excludeStrings, v)
		}
	}

	ports := make([]string, transfersParam+1)
	for i := 0; i <= transfersParam; i++ {
		ports[i] = strconv.Itoa(portParam + i)
	}

	crocOptions := croc.Options{
		SharedSecret:      c.String("code"),
		IsSender:          true,
		Debug:             c.Bool("debug"),
		NoPrompt:          c.Bool("yes"),
		RelayAddress:      c.String("relay"),
		RelayAddress6:     c.String("relay6"),
		Stdout:            c.Bool("stdout"),
		DisableLocal:      c.Bool("no-local"),
		OnlyLocal:         c.Bool("local"),
		IgnoreStdin:       c.Bool("ignore-stdin"),
		RelayPorts:        ports,
		Ask:               c.Bool("ask"),
		NoMultiplexing:    c.Bool("no-multi"),
		RelayPassword:     determinePass(c),
		SendingText:       c.String("text") != "",
		NoCompress:        c.Bool("no-compress"),
		Overwrite:         c.Bool("overwrite"),
		Curve:             c.String("curve"),
		HashAlgorithm:     c.String("hash"),
		ThrottleUpload:    c.String("throttleUpload"),
		ZipFolder:         c.Bool("zip"),
		GitIgnore:         c.Bool("git"),
		ShowQrCode:        c.Bool("qrcode"),
		MulticastAddress:  c.String("multicast"),
		Exclude:           excludeStrings,
		Quiet:             c.Bool("quiet"),
		DisableClipboard:  c.Bool("disable-clipboard"),
		ExtendedClipboard: c.Bool("extended-clipboard"),
	}
	if crocOptions.RelayAddress != models.DEFAULT_RELAY {
		crocOptions.RelayAddress6 = ""
	} else if crocOptions.RelayAddress6 != models.DEFAULT_RELAY6 {
		crocOptions.RelayAddress = ""
	}
	b, errOpen := os.ReadFile(getSendConfigFile(false))
	if errOpen == nil && !c.Bool("remember") {
		var rememberedOptions croc.Options
		err = json.Unmarshal(b, &rememberedOptions)
		if err != nil {
			log.Error(err)
			return
		}
		// update anything that isn't explicitly set
		if !c.IsSet("no-local") {
			crocOptions.DisableLocal = rememberedOptions.DisableLocal
		}
		if !c.IsSet("ports") && len(rememberedOptions.RelayPorts) > 0 {
			crocOptions.RelayPorts = rememberedOptions.RelayPorts
		}
		if !c.IsSet("code") {
			crocOptions.SharedSecret = rememberedOptions.SharedSecret
		}
		if !c.IsSet("pass") && rememberedOptions.RelayPassword != "" {
			crocOptions.RelayPassword = rememberedOptions.RelayPassword
		}
		if !c.IsSet("overwrite") {
			crocOptions.Overwrite = rememberedOptions.Overwrite
		}
		if !c.IsSet("curve") && rememberedOptions.Curve != "" {
			crocOptions.Curve = rememberedOptions.Curve
		}
		if !c.IsSet("local") {
			crocOptions.OnlyLocal = rememberedOptions.OnlyLocal
		}
		if !c.IsSet("hash") {
			crocOptions.HashAlgorithm = rememberedOptions.HashAlgorithm
		}
		if !c.IsSet("git") {
			crocOptions.GitIgnore = rememberedOptions.GitIgnore
		}
		if !c.IsSet("relay") && strings.HasPrefix(rememberedOptions.RelayAddress, "non-default:") {
			var rememberedAddr = strings.TrimPrefix(rememberedOptions.RelayAddress, "non-default:")
			rememberedAddr = strings.TrimSpace(rememberedAddr)
			crocOptions.RelayAddress = rememberedAddr
		}
		if !c.IsSet("relay6") && strings.HasPrefix(rememberedOptions.RelayAddress6, "non-default:") {
			var rememberedAddr = strings.TrimPrefix(rememberedOptions.RelayAddress6, "non-default:")
			rememberedAddr = strings.TrimSpace(rememberedAddr)
			crocOptions.RelayAddress6 = rememberedAddr
		}
	}

	var fnames []string
	stat, _ := os.Stdin.Stat()
	if ((stat.Mode() & os.ModeCharDevice) == 0) && !c.Bool("ignore-stdin") {
		fnames, err = getStdin()
		if err != nil {
			return
		}
		utils.MarkFileForRemoval(fnames[0])
		defer func() {
			e := os.Remove(fnames[0])
			if e != nil {
				log.Error(e)
			}
		}()
	} else if c.String("text") != "" {
		fnames, err = makeTempFileWithString(c.String("text"))
		if err != nil {
			return
		}
		utils.MarkFileForRemoval(fnames[0])
		defer func() {
			e := os.Remove(fnames[0])
			if e != nil {
				log.Error(e)
			}
		}()

	} else {
		fnames = c.Args().Slice()
	}
	if len(fnames) == 0 {
		return errors.New("must specify file: croc send [filename(s) or folder]")
	}

	classicInsecureMode := utils.Exists(getClassicConfigFile(true))
	if !classicInsecureMode {
		// if operating system is UNIX, then use environmental variable to set the code
		if (!(runtime.GOOS == "windows") && c.IsSet("code")) || os.Getenv("CROC_SECRET") != "" {
			crocOptions.SharedSecret = os.Getenv("CROC_SECRET")
			if crocOptions.SharedSecret == "" {
				fmt.Printf(`On UNIX systems, to send with a custom code phrase,
you need to set the environmental variable CROC_SECRET:

  CROC_SECRET=**** croc send file.txt

Or you can have the code phrase automatically generated:

  croc send file.txt

Or you can go back to the classic croc behavior by enabling classic mode:

  croc --classic

`)
				os.Exit(0)
			}
		}
	}

	if len(crocOptions.SharedSecret) == 0 {
		// generate code phrase
		crocOptions.SharedSecret = utils.GetRandomName()
	}
	minimalFileInfos, emptyFoldersToTransfer, totalNumberFolders, err := croc.GetFilesInfo(fnames, crocOptions.ZipFolder, crocOptions.GitIgnore, crocOptions.Exclude)
	if err != nil {
		return
	}
	if len(crocOptions.Exclude) > 0 {
		minimalFileInfosInclude := []croc.FileInfo{}
		emptyFoldersToTransferInclude := []croc.FileInfo{}
		for _, f := range minimalFileInfos {
			exclude := false
			for _, exclusion := range crocOptions.Exclude {
				if strings.Contains(path.Join(strings.ToLower(f.FolderRemote), strings.ToLower(f.Name)), exclusion) {
					exclude = true
					break
				}
			}
			if !exclude {
				minimalFileInfosInclude = append(minimalFileInfosInclude, f)
			}
		}
		for _, f := range emptyFoldersToTransfer {
			exclude := false
			for _, exclusion := range crocOptions.Exclude {
				if strings.Contains(path.Join(strings.ToLower(f.FolderRemote), strings.ToLower(f.Name)), exclusion) {
					exclude = true
					break
				}
			}
			if !exclude {
				emptyFoldersToTransferInclude = append(emptyFoldersToTransferInclude, f)
			}
		}
		totalNumberFolders = 0
		folderMap := make(map[string]bool)
		for _, f := range minimalFileInfosInclude {
			folderMap[f.FolderRemote] = true
		}
		for _, f := range emptyFoldersToTransferInclude {
			folderMap[f.FolderRemote] = true
		}
		totalNumberFolders = len(folderMap)
		minimalFileInfos = minimalFileInfosInclude
		emptyFoldersToTransfer = emptyFoldersToTransferInclude
	}

	cr, err := croc.New(crocOptions)
	if err != nil {
		return
	}

	// save the config
	saveConfig(c, crocOptions)
	err = cr.Send(minimalFileInfos, emptyFoldersToTransfer, totalNumberFolders)
	return
}

func getStdin() (fnames []string, err error) {
	f, err := os.CreateTemp(".", "croc-stdin-")
	if err != nil {
		return
	}
	_, err = io.Copy(f, os.Stdin)
	if err != nil {
		return
	}
	err = f.Close()
	if err != nil {
		return
	}
	fnames = []string{f.Name()}
	return
}

func makeTempFileWithString(s string) (fnames []string, err error) {
	f, err := os.CreateTemp(".", "croc-stdin-")
	if err != nil {
		return
	}

	_, err = f.WriteString(s)
	if err != nil {
		return
	}

	err = f.Close()
	if err != nil {
		return
	}
	fnames = []string{f.Name()}
	return
}

func saveConfig(c *cli.Context, crocOptions croc.Options) {
	if c.Bool("remember") {
		configFile := getSendConfigFile(true)
		log.Debug("saving config file")
		var bConfig []byte
		// if the code wasn't set, don't save it
		if c.String("code") == "" {
			crocOptions.SharedSecret = ""
		}
		if c.String("relay") != models.DEFAULT_RELAY {
			crocOptions.RelayAddress = "non-default: " + c.String("relay")
		} else {
			crocOptions.RelayAddress = "default"
		}
		if c.String("relay6") != models.DEFAULT_RELAY6 {
			crocOptions.RelayAddress6 = "non-default: " + c.String("relay6")
		} else {
			crocOptions.RelayAddress6 = "default"
		}
		bConfig, err := json.MarshalIndent(crocOptions, "", "    ")
		if err != nil {
			log.Error(err)
			return
		}
		err = os.WriteFile(configFile, bConfig, 0o644)
		if err != nil {
			log.Error(err)
			return
		}
		log.Debugf("wrote %s", configFile)
	}
}

type TabComplete struct{}

func (t TabComplete) Do(line []rune, pos int) ([][]rune, int) {
	var words = strings.SplitAfter(string(line), "-")
	var lastPartialWord = words[len(words)-1]
	var nbCharacter = len(lastPartialWord)
	if nbCharacter == 0 {
		// No completion
		return [][]rune{[]rune("")}, 0
	}
	if len(words) == 1 && nbCharacter == utils.NbPinNumbers {
		// Check if word is indeed a number
		_, err := strconv.Atoi(lastPartialWord)
		if err == nil {
			return [][]rune{[]rune("-")}, nbCharacter
		}
	}
	var strArray [][]rune
	for _, s := range mnemonicode.WordList {
		if strings.HasPrefix(s, lastPartialWord) {
			var completionCandidate = s[nbCharacter:]
			if len(words) <= mnemonicode.WordsRequired(utils.NbBytesWords) {
				completionCandidate += "-"
			}
			strArray = append(strArray, []rune(completionCandidate))
		}
	}
	return strArray, nbCharacter
}

func receive(c *cli.Context) (err error) {
	comm.Socks5Proxy = c.String("socks5")
	comm.HttpProxy = c.String("connect")
	crocOptions := croc.Options{
		SharedSecret:      c.String("code"),
		IsSender:          false,
		Debug:             c.Bool("debug"),
		NoPrompt:          c.Bool("yes"),
		RelayAddress:      c.String("relay"),
		RelayAddress6:     c.String("relay6"),
		Stdout:            c.Bool("stdout"),
		Ask:               c.Bool("ask"),
		RelayPassword:     determinePass(c),
		OnlyLocal:         c.Bool("local"),
		IP:                c.String("ip"),
		Overwrite:         c.Bool("overwrite"),
		Curve:             c.String("curve"),
		TestFlag:          c.Bool("testing"),
		MulticastAddress:  c.String("multicast"),
		Quiet:             c.Bool("quiet"),
		DisableClipboard:  c.Bool("disable-clipboard"),
		ExtendedClipboard: c.Bool("extended-clipboard"),
	}
	if crocOptions.RelayAddress != models.DEFAULT_RELAY {
		crocOptions.RelayAddress6 = ""
	} else if crocOptions.RelayAddress6 != models.DEFAULT_RELAY6 {
		crocOptions.RelayAddress = ""
	}

	switch c.Args().Len() {
	case 1:
		crocOptions.SharedSecret = c.Args().First()
	case 3:
		fallthrough
	case 4:
		var phrase []string
		phrase = append(phrase, c.Args().First())
		phrase = append(phrase, c.Args().Tail()...)
		crocOptions.SharedSecret = strings.Join(phrase, "-")
	}

	// load options here
	setDebugLevel(c)

	doRemember := c.Bool("remember")
	configFile, err := getReceiveConfigFile(doRemember)
	if err != nil && doRemember {
		return
	}
	b, errOpen := os.ReadFile(configFile)
	if errOpen == nil && !doRemember {
		var rememberedOptions croc.Options
		err = json.Unmarshal(b, &rememberedOptions)
		if err != nil {
			log.Error(err)
			return
		}
		// update anything that isn't explicitly Globally set
		if !c.IsSet("yes") {
			crocOptions.NoPrompt = rememberedOptions.NoPrompt
		}
		if crocOptions.SharedSecret == "" {
			crocOptions.SharedSecret = rememberedOptions.SharedSecret
		}
		if !c.IsSet("pass") && rememberedOptions.RelayPassword != "" {
			crocOptions.RelayPassword = rememberedOptions.RelayPassword
		}
		if !c.IsSet("overwrite") {
			crocOptions.Overwrite = rememberedOptions.Overwrite
		}
		if !c.IsSet("curve") && rememberedOptions.Curve != "" {
			crocOptions.Curve = rememberedOptions.Curve
		}
		if !c.IsSet("local") {
			crocOptions.OnlyLocal = rememberedOptions.OnlyLocal
		}
		if !c.IsSet("relay") && strings.HasPrefix(rememberedOptions.RelayAddress, "non-default:") {
			var rememberedAddr = strings.TrimPrefix(rememberedOptions.RelayAddress, "non-default:")
			rememberedAddr = strings.TrimSpace(rememberedAddr)
			crocOptions.RelayAddress = rememberedAddr
		}
		if !c.IsSet("relay6") && strings.HasPrefix(rememberedOptions.RelayAddress6, "non-default:") {
			var rememberedAddr = strings.TrimPrefix(rememberedOptions.RelayAddress6, "non-default:")
			rememberedAddr = strings.TrimSpace(rememberedAddr)
			crocOptions.RelayAddress6 = rememberedAddr
		}
	}

	classicInsecureMode := utils.Exists(getClassicConfigFile(true))
	if crocOptions.SharedSecret == "" && os.Getenv("CROC_SECRET") != "" {
		crocOptions.SharedSecret = os.Getenv("CROC_SECRET")
	} else if !(runtime.GOOS == "windows") && crocOptions.SharedSecret != "" && !classicInsecureMode {
		crocOptions.SharedSecret = os.Getenv("CROC_SECRET")
		if crocOptions.SharedSecret == "" {
			fmt.Printf(`On UNIX systems, to receive with croc you either need
to set a code phrase using your environmental variables:

  CROC_SECRET=**** croc

Or you can specify the code phrase when you run croc without
declaring the secret on the command line:

  croc
  Enter receive code: ****

Or you can go back to the classic croc behavior by enabling classic mode:

  croc --classic

`)
			os.Exit(0)
		}
	}
	if crocOptions.SharedSecret == "" {
		l, err := readline.NewEx(&readline.Config{
			Prompt:       "Enter receive code: ",
			AutoComplete: TabComplete{},
		})
		if err != nil {
			return err
		}
		crocOptions.SharedSecret, err = l.Readline()
		if err != nil {
			return err
		}
	}
	if c.String("out") != "" {
		if err = os.Chdir(c.String("out")); err != nil {
			return err
		}
	}

	cr, err := croc.New(crocOptions)
	if err != nil {
		return
	}

	// save the config
	if doRemember {
		log.Debug("saving config file")
		var bConfig []byte
		if c.String("relay") != models.DEFAULT_RELAY {
			crocOptions.RelayAddress = "non-default: " + c.String("relay")
		} else {
			crocOptions.RelayAddress = "default"
		}
		if c.String("relay6") != models.DEFAULT_RELAY6 {
			crocOptions.RelayAddress6 = "non-default: " + c.String("relay6")
		} else {
			crocOptions.RelayAddress6 = "default"
		}
		bConfig, err = json.MarshalIndent(crocOptions, "", "    ")
		if err != nil {
			log.Error(err)
			return
		}
		err = os.WriteFile(configFile, bConfig, 0o644)
		if err != nil {
			log.Error(err)
			return
		}
		log.Debugf("wrote %s", configFile)
	}

	err = cr.Receive()
	return
}

func relay(c *cli.Context) (err error) {
	log.Infof("starting croc relay version %v", Version)
	debugString := "info"
	if c.Bool("debug") {
		debugString = "debug"
	}
	host := c.String("host")
	var ports []string

	if c.IsSet("ports") {
		ports = strings.Split(c.String("ports"), ",")
	} else {
		portString := c.Int("port")
		if portString == 0 {
			portString = 9009
		}
		transfersString := c.Int("transfers")
		if transfersString == 0 {
			transfersString = 4
		}
		ports = make([]string, transfersString)
		for i := range ports {
			ports[i] = strconv.Itoa(portString + i)
		}
	}
	if len(ports) < 2 {
		return fmt.Errorf("relay requires at least two ports; specify --ports with two or more ports or set --transfers to 2+")
	}

	tcpPorts := strings.Join(ports[1:], ",")
	for i, port := range ports {
		if i == 0 {
			continue
		}
		go func(portStr string) {
			err := tcp.Run(debugString, host, portStr, determinePass(c))
			if err != nil {
				panic(err)
			}
		}(port)
	}
	return tcp.Run(debugString, host, ports[0], determinePass(c), tcpPorts)
}
```

## File: `src/comm/comm.go`
```go
package comm

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"io"
	"net"
	"net/url"
	"strings"
	"time"

	"github.com/magisterquis/connectproxy"
	"github.com/schollz/croc/v10/src/utils"
	log "github.com/schollz/logger"
	"golang.org/x/net/proxy"
)

var Socks5Proxy = ""
var HttpProxy = ""

var MAGIC_BYTES = []byte("croc")

const maxReadMessageSize = 64 * 1024 * 1024

// Comm is some basic TCP communication
type Comm struct {
	connection net.Conn
}

// NewConnection gets a new comm to a tcp address
func NewConnection(address string, timelimit ...time.Duration) (c *Comm, err error) {
	tlimit := 30 * time.Second
	if len(timelimit) > 0 {
		tlimit = timelimit[0]
	}
	var connection net.Conn
	if Socks5Proxy != "" && !utils.IsLocalIP(address) {
		var dialer proxy.Dialer
		// prepend schema if no schema is given
		if !strings.Contains(Socks5Proxy, `://`) {
			Socks5Proxy = `socks5://` + Socks5Proxy
		}
		socks5ProxyURL, urlParseError := url.Parse(Socks5Proxy)
		if urlParseError != nil {
			err = fmt.Errorf("unable to parse socks proxy url: %s", urlParseError)
			log.Debug(err)
			return
		}
		dialer, err = proxy.FromURL(socks5ProxyURL, proxy.Direct)
		if err != nil {
			err = fmt.Errorf("proxy failed: %w", err)
			log.Debug(err)
			return
		}
		log.Debug("dialing with dialer.Dial")
		connection, err = dialer.Dial("tcp", address)
	} else if HttpProxy != "" && !utils.IsLocalIP(address) {
		var dialer proxy.Dialer
		// prepend schema if no schema is given
		if !strings.Contains(HttpProxy, `://`) {
			HttpProxy = `http://` + HttpProxy
		}
		HttpProxyURL, urlParseError := url.Parse(HttpProxy)
		if urlParseError != nil {
			err = fmt.Errorf("unable to parse http proxy url: %s", urlParseError)
			log.Debug(err)
			return
		}
		dialer, err = connectproxy.New(HttpProxyURL, proxy.Direct)
		if err != nil {
			err = fmt.Errorf("proxy failed: %w", err)
			log.Debug(err)
			return
		}
		log.Debug("dialing with dialer.Dial")
		connection, err = dialer.Dial("tcp", address)

	} else {
		log.Debugf("dialing to %s with timelimit %s", address, tlimit)
		connection, err = net.DialTimeout("tcp", address, tlimit)
	}
	if err != nil {
		err = fmt.Errorf("comm.NewConnection failed: %w", err)
		log.Debug(err)
		return
	}
	c = New(connection)
	log.Debugf("connected to '%s'", address)
	return
}

// New returns a new comm
func New(c net.Conn) *Comm {
	if err := c.SetReadDeadline(time.Now().Add(3 * time.Hour)); err != nil {
		log.Warnf("error setting read deadline: %v", err)
	}
	if err := c.SetDeadline(time.Now().Add(3 * time.Hour)); err != nil {
		log.Warnf("error setting overall deadline: %v", err)
	}
	if err := c.SetWriteDeadline(time.Now().Add(3 * time.Hour)); err != nil {
		log.Errorf("error setting write deadline: %v", err)
	}
	comm := new(Comm)
	comm.connection = c
	return comm
}

// Connection returns the net.Conn connection
func (c *Comm) Connection() net.Conn {
	return c.connection
}

// Close closes the connection
func (c *Comm) Close() {
	if err := c.connection.Close(); err != nil {
		log.Warnf("error closing connection: %v", err)
	}
}

func (c *Comm) Write(b []byte) (n int, err error) {
	header := new(bytes.Buffer)
	err = binary.Write(header, binary.LittleEndian, uint32(len(b)))
	if err != nil {
		fmt.Println("binary.Write failed:", err)
	}
	tmpCopy := append(header.Bytes(), b...)
	tmpCopy = append(MAGIC_BYTES, tmpCopy...)
	n, err = c.connection.Write(tmpCopy)
	if err != nil {
		err = fmt.Errorf("connection.Write failed: %w", err)
		return
	}
	if n != len(tmpCopy) {
		err = fmt.Errorf("wanted to write %d but wrote %d", len(b), n)
		return
	}
	return
}

func (c *Comm) Read() (buf []byte, numBytes int, bs []byte, err error) {
	// long read deadline in case waiting for file
	if err = c.connection.SetReadDeadline(time.Now().Add(3 * time.Hour)); err != nil {
		log.Warnf("error setting read deadline: %v", err)
	}
	// must clear the timeout setting
	if err := c.connection.SetDeadline(time.Time{}); err != nil {
		log.Warnf("failed to clear deadline: %v", err)
	}

	// read until we get 4 bytes for the magic
	header := make([]byte, 4)
	_, err = io.ReadFull(c.connection, header)
	if err != nil {
		log.Debugf("initial read error: %v", err)
		return
	}
	if !bytes.Equal(header, MAGIC_BYTES) {
		err = fmt.Errorf("initial bytes are not magic: %x", header)
		return
	}

	// read until we get 4 bytes for the header
	header = make([]byte, 4)
	_, err = io.ReadFull(c.connection, header)
	if err != nil {
		log.Debugf("initial read error: %v", err)
		return
	}

	var numBytesUint32 uint32
	rbuf := bytes.NewReader(header)
	err = binary.Read(rbuf, binary.LittleEndian, &numBytesUint32)
	if err != nil {
		err = fmt.Errorf("binary.Read failed: %w", err)
		log.Debug(err.Error())
		return
	}
	if numBytesUint32 > uint32(maxReadMessageSize) {
		err = fmt.Errorf("message too large: %d > %d", numBytesUint32, maxReadMessageSize)
		log.Debug(err.Error())
		return
	}
	numBytes = int(numBytesUint32)

	// shorten the reading deadline in case getting weird data
	if err = c.connection.SetReadDeadline(time.Now().Add(10 * time.Second)); err != nil {
		log.Warnf("error setting read deadline: %v", err)
	}
	buf = make([]byte, numBytes)
	_, err = io.ReadFull(c.connection, buf)
	if err != nil {
		log.Debugf("consecutive read error: %v", err)
		return
	}
	return
}

// Send a message
func (c *Comm) Send(message []byte) (err error) {
	_, err = c.Write(message)
	return
}

// Receive a message
func (c *Comm) Receive() (b []byte, err error) {
	b, _, _, err = c.Read()
	return
}
```

## File: `src/comm/comm_test.go`
```go
package comm

import (
	"bytes"
	"crypto/rand"
	"encoding/binary"
	"net"
	"testing"
	"time"

	log "github.com/schollz/logger"
	"github.com/stretchr/testify/assert"
)

func TestComm(t *testing.T) {
	token := make([]byte, 3000)
	if _, err := rand.Read(token); err != nil {
		t.Error(err)
	}

	// Use dynamic port allocation to avoid conflicts
	listener, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		t.Fatal(err)
	}
	port := listener.Addr().(*net.TCPAddr).Port
	portStr := listener.Addr().String()
	listener.Close() // Close the listener so we can reopen it in the goroutine

	go func() {
		log.Debug("starting TCP server on " + portStr)
		server, err := net.Listen("tcp", portStr)
		if err != nil {
			log.Error(err)
			return
		}
		defer func() {
			if err := server.Close(); err != nil {
				log.Error(err)
			}
		}()
		// spawn a new goroutine whenever a client connects
		for {
			connection, err := server.Accept()
			if err != nil {
				log.Error(err)
			}
			log.Debugf("client %s connected", connection.RemoteAddr().String())
			go func(_ int, connection net.Conn) {
				c := New(connection)
				err = c.Send([]byte("hello, world"))
				assert.Nil(t, err)
				data, err := c.Receive()
				assert.Nil(t, err)
				assert.Equal(t, []byte("hello, computer"), data)
				data, err = c.Receive()
				assert.Nil(t, err)
				assert.Equal(t, []byte{'\x00'}, data)
				data, err = c.Receive()
				assert.Nil(t, err)
				assert.Equal(t, token, data)
			}(port, connection)
		}
	}()

	time.Sleep(300 * time.Millisecond)
	a, err := NewConnection(portStr, 10*time.Minute)
	assert.Nil(t, err)
	data, err := a.Receive()
	assert.Equal(t, []byte("hello, world"), data)
	assert.Nil(t, err)
	assert.Nil(t, a.Send([]byte("hello, computer")))
	assert.Nil(t, a.Send([]byte{'\x00'}))

	assert.Nil(t, a.Send(token))
	_ = a.Connection()
	a.Close()
	assert.NotNil(t, a.Send(token))
	_, err = a.Write(token)
	assert.NotNil(t, err)
}

func TestReceiveRejectsOversizedMessage(t *testing.T) {
	clientConn, serverConn := net.Pipe()
	defer clientConn.Close()
	defer serverConn.Close()

	c := New(clientConn)

	writeErr := make(chan error, 1)
	go func() {
		header := new(bytes.Buffer)
		header.Write(MAGIC_BYTES)
		if err := binary.Write(header, binary.LittleEndian, uint32(maxReadMessageSize+1)); err != nil {
			writeErr <- err
			return
		}
		_, err := serverConn.Write(header.Bytes())
		writeErr <- err
	}()

	_, err := c.Receive()
	assert.NotNil(t, err)
	assert.Contains(t, err.Error(), "message too large")
	assert.Nil(t, <-writeErr)
}
```

## File: `src/compress/compress.go`
```go
package compress

import (
	"bytes"
	"compress/flate"
	"io"

	log "github.com/schollz/logger"
)

// CompressWithOption returns compressed data using the specified level
func CompressWithOption(src []byte, level int) []byte {
	compressedData := new(bytes.Buffer)
	compress(src, compressedData, level)
	return compressedData.Bytes()
}

// Compress returns a compressed byte slice.
func Compress(src []byte) []byte {
	compressedData := new(bytes.Buffer)
	compress(src, compressedData, flate.HuffmanOnly)
	return compressedData.Bytes()
}

// Decompress returns a decompressed byte slice.
func Decompress(src []byte) []byte {
	compressedData := bytes.NewBuffer(src)
	deCompressedData := new(bytes.Buffer)
	decompress(compressedData, deCompressedData)
	return deCompressedData.Bytes()
}

// compress uses flate to compress a byte slice to a corresponding level
func compress(src []byte, dest io.Writer, level int) {
	compressor, err := flate.NewWriter(dest, level)
	if err != nil {
		log.Debugf("error level data: %v", err)
		return
	}
	if _, err := compressor.Write(src); err != nil {
		log.Debugf("error writing data: %v", err)
	}
	compressor.Close()
}

// decompress uses flate to decompress an io.Reader
func decompress(src io.Reader, dest io.Writer) {
	decompressor := flate.NewReader(src)
	if _, err := io.Copy(dest, decompressor); err != nil {
		log.Debugf("error copying data: %v", err)
	}
	decompressor.Close()
}
```

## File: `src/compress/compress_test.go`
```go
package compress

import (
	"crypto/rand"
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

var fable = []byte(`The Frog and the Crocodile
Once, there was a frog who lived in the middle of a swamp. His entire family had lived in that swamp for generations, but this particular frog decided that he had had quite enough wetness to last him a lifetime. He decided that he was going to find a dry place to live instead.

The only thing that separated him from dry land was a swampy, muddy, swiftly flowing river. But the river was home to all sorts of slippery, slittering snakes that loved nothing better than a good, plump frog for dinner, so Frog didn't dare try to swim across.

So for many days, the frog stayed put, hopping along the bank, trying to think of a way to get across.

The snakes hissed and jeered at him, daring him to come closer, but he refused. Occasionally they would slither closer, jaws open to attack, but the frog always leaped out of the way. But no matter how far upstream he searched or how far downstream, the frog wasn't able to find a way across the water.

He had felt certain that there would be a bridge, or a place where the banks came together, yet all he found was more reeds and water. After a while, even the snakes stopped teasing him and went off in search of easier prey.

The frog sighed in frustration and sat to sulk in the rushes. Suddenly, he spotted two big eyes staring at him from the water. The giant log-shaped animal opened its mouth and asked him, "What are you doing, Frog? Surely there are enough flies right there for a meal."

The frog croaked in surprise and leaped away from the crocodile. That creature could swallow him whole in a moment without thinking about it! Once he was a satisfied that he was a safe distance away, he answered. "I'm tired of living in swampy waters, and I want to travel to the other side of the river. But if I swim across, the snakes will eat me."

The crocodile harrumphed in agreement and sat, thinking, for a while. "Well, if you're afraid of the snakes, I could give you a ride across," he suggested.

"Oh no, I don't think so," Frog answered quickly. "You'd eat me on the way over, or go underwater so the snakes could get me!"

"Now why would I let the snakes get you? I think they're a terrible nuisance with all their hissing and slithering! The river would be much better off without them altogether! Anyway, if you're so worried that I might eat you, you can ride on my tail."

The frog considered his offer. He did want to get to dry ground very badly, and there didn't seem to be any other way across the river. He looked at the crocodile from his short, squat buggy eyes and wondered about the crocodile's motives. But if he rode on the tail, the croc couldn't eat him anyway. And he was right about the snakes--no self-respecting crocodile would give a meal to the snakes.

"Okay, it sounds like a good plan to me. Turn around so I can hop on your tail."

The crocodile flopped his tail into the marshy mud and let the frog climb on, then he waddled out to the river. But he couldn't stick his tail into the water as a rudder because the frog was on it -- and if he put his tail in the water, the snakes would eat the frog. They clumsily floated downstream for a ways, until the crocodile said, "Hop onto my back so I can steer straight with my tail." The frog moved, and the journey smoothed out.

From where he was sitting, the frog couldn't see much except the back of Crocodile's head. "Why don't you hop up on my head so you can see everything around us?" Crocodile invited. `)

func BenchmarkCompressLevelMinusTwo(b *testing.B) {
	for i := 0; i < b.N; i++ {
		CompressWithOption(fable, -2)
	}
}

func BenchmarkCompressLevelNine(b *testing.B) {
	for i := 0; i < b.N; i++ {
		CompressWithOption(fable, 9)
	}
}

func BenchmarkCompressLevelMinusTwoBinary(b *testing.B) {
	data := make([]byte, 1000000)
	if _, err := rand.Read(data); err != nil {
		b.Fatal(err)
	}
	for i := 0; i < b.N; i++ {
		CompressWithOption(data, -2)
	}
}

func BenchmarkCompressLevelNineBinary(b *testing.B) {
	data := make([]byte, 1000000)
	if _, err := rand.Read(data); err != nil {
		b.Fatal(err)
	}
	for i := 0; i < b.N; i++ {
		CompressWithOption(data, 9)
	}
}

func TestCompress(t *testing.T) {
	compressedB := CompressWithOption(fable, 9)
	dataRateSavings := 100 * (1.0 - float64(len(compressedB))/float64(len(fable)))
	fmt.Printf("Level 9: %2.0f%% percent space savings\n", dataRateSavings)
	assert.True(t, len(compressedB) < len(fable))
	assert.Equal(t, fable, Decompress(compressedB))

	compressedB = CompressWithOption(fable, -2)
	dataRateSavings = 100 * (1.0 - float64(len(compressedB))/float64(len(fable)))
	fmt.Printf("Level -2: %2.0f%% percent space savings\n", dataRateSavings)
	assert.True(t, len(compressedB) < len(fable))

	compressedB = Compress(fable)
	dataRateSavings = 100 * (1.0 - float64(len(compressedB))/float64(len(fable)))
	fmt.Printf("Level -2: %2.0f%% percent space savings\n", dataRateSavings)
	assert.True(t, len(compressedB) < len(fable))

	data := make([]byte, 4096)
	if _, err := rand.Read(data); err != nil {
		t.Fatal(err)
	}
	compressedB = CompressWithOption(data, -2)
	dataRateSavings = 100 * (1.0 - float64(len(compressedB))/float64(len(data)))
	fmt.Printf("random, Level -2: %2.0f%% percent space savings\n", dataRateSavings)

	if _, err := rand.Read(data); err != nil {
		t.Fatal(err)
	}
	compressedB = CompressWithOption(data, 9)
	dataRateSavings = 100 * (1.0 - float64(len(compressedB))/float64(len(data)))

	fmt.Printf("random, Level 9: %2.0f%% percent space savings\n", dataRateSavings)

}
```

## File: `src/croc/croc.go`
```go
package croc

import (
	"bytes"
	"context"
	"crypto/rand"
	"crypto/sha256"
	"encoding/binary"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"io"
	"math"
	"net"
	"os"
	"os/exec"
	"path"
	"path/filepath"
	"runtime"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/denisbrodbeck/machineid"
	ignore "github.com/sabhiram/go-gitignore"
	log "github.com/schollz/logger"
	"github.com/schollz/pake/v3"
	"github.com/schollz/peerdiscovery"
	"github.com/schollz/progressbar/v3"
	"github.com/skip2/go-qrcode"
	"golang.org/x/term"
	"golang.org/x/time/rate"

	"github.com/schollz/croc/v10/src/comm"
	"github.com/schollz/croc/v10/src/compress"
	"github.com/schollz/croc/v10/src/crypt"
	"github.com/schollz/croc/v10/src/message"
	"github.com/schollz/croc/v10/src/models"
	"github.com/schollz/croc/v10/src/tcp"
	"github.com/schollz/croc/v10/src/utils"
)

var (
	ipRequest        = []byte("ips?")
	handshakeRequest = []byte("handshake")
)

func init() {
	log.SetLevel("debug")
}

// Debug toggles debug mode
func Debug(debug bool) {
	if debug {
		log.SetLevel("debug")
	} else {
		log.SetLevel("warn")
	}
}

// Options specifies user specific options
type Options struct {
	IsSender          bool
	SharedSecret      string
	RoomName          string
	Debug             bool
	RelayAddress      string
	RelayAddress6     string
	RelayPorts        []string
	RelayPassword     string
	Stdout            bool
	NoPrompt          bool
	NoMultiplexing    bool
	DisableLocal      bool
	OnlyLocal         bool
	IgnoreStdin       bool
	Ask               bool
	SendingText       bool
	NoCompress        bool
	IP                string
	Overwrite         bool
	Curve             string
	HashAlgorithm     string
	ThrottleUpload    string
	ZipFolder         bool
	TestFlag          bool
	GitIgnore         bool
	MulticastAddress  string
	ShowQrCode        bool
	Exclude           []string
	Quiet             bool
	DisableClipboard  bool
	ExtendedClipboard bool
}

type SimpleMessage struct {
	Bytes []byte
	Kind  string
}

// Client holds the state of the croc transfer
type Client struct {
	Options                         Options
	Pake                            *pake.Pake
	Key                             []byte
	ExternalIP, ExternalIPConnected string

	// steps involved in forming relationship
	Step1ChannelSecured       bool
	Step2FileInfoTransferred  bool
	Step3RecipientRequestFile bool
	Step4FileTransferred      bool
	Step5CloseChannels        bool
	SuccessfulTransfer        bool

	// send / receive information of all files
	FilesToTransfer           []FileInfo
	EmptyFoldersToTransfer    []FileInfo
	TotalNumberOfContents     int
	TotalNumberFolders        int
	FilesToTransferCurrentNum int
	FilesHasFinished          map[int]struct{}
	TotalFilesIgnored         int

	// send / receive information of current file
	CurrentFile            *os.File
	CurrentFileChunkRanges []int64
	CurrentFileChunks      []int64
	CurrentFileIsClosed    bool
	LastFolder             string

	TotalSent              int64
	TotalChunksTransferred int
	chunkMap               map[uint64]struct{}
	limiter                *rate.Limiter

	// tcp connections
	conn []*comm.Comm

	bar             *progressbar.ProgressBar
	longestFilename int
	firstSend       bool

	mutex                    *sync.Mutex
	fread                    *os.File
	numfinished              int
	quit                     chan bool
	finishedNum              int
	numberOfTransferredFiles int

	// ctx.go for graceful shutdown
	*stop
}

// Chunk contains information about the
// needed bytes
type Chunk struct {
	Bytes    []byte `json:"b,omitempty"`
	Location int64  `json:"l,omitempty"`
}

// FileInfo registers the information about the file
type FileInfo struct {
	Name         string      `json:"n,omitempty"`
	FolderRemote string      `json:"fr,omitempty"`
	FolderSource string      `json:"fs,omitempty"`
	Hash         []byte      `json:"h,omitempty"`
	Size         int64       `json:"s,omitempty"`
	ModTime      time.Time   `json:"m,omitempty"`
	IsCompressed bool        `json:"c,omitempty"`
	IsEncrypted  bool        `json:"e,omitempty"`
	Symlink      string      `json:"sy,omitempty"`
	Mode         os.FileMode `json:"md,omitempty"`
	TempFile     bool        `json:"tf,omitempty"`
	IsIgnored    bool        `json:"ig,omitempty"`
}

// RemoteFileRequest requests specific bytes
type RemoteFileRequest struct {
	CurrentFileChunkRanges    []int64
	FilesToTransferCurrentNum int
	MachineID                 string
}

// SenderInfo lists the files to be transferred
type SenderInfo struct {
	FilesToTransfer        []FileInfo
	EmptyFoldersToTransfer []FileInfo
	TotalNumberFolders     int
	MachineID              string
	Ask                    bool
	SendingText            bool
	NoCompress             bool
	HashAlgorithm          string
}

// New establishes a new connection for transferring files between two instances.
func New(ops Options) (c *Client, err error) {
	c = new(Client)
	c.FilesHasFinished = make(map[int]struct{})

	// setup basic info
	c.Options = ops
	Debug(c.Options.Debug)

	// redirect stderr to null if quiet mode is enabled
	if c.Options.Quiet {
		devNull, err := os.OpenFile(os.DevNull, os.O_WRONLY, 0)
		if err == nil {
			os.Stderr = devNull
		}
	}

	if len(c.Options.SharedSecret) < 6 {
		err = fmt.Errorf("code is too short")
		return
	}
	// Create a hash of part of the shared secret to use as the room name
	hashExtra := "croc"
	roomNameBytes := sha256.Sum256([]byte(c.Options.SharedSecret[:4] + hashExtra))
	c.Options.RoomName = hex.EncodeToString(roomNameBytes[:])

	c.conn = make([]*comm.Comm, 16)

	// initialize throttler
	if len(c.Options.ThrottleUpload) > 1 && c.Options.IsSender {
		upload := c.Options.ThrottleUpload[:len(c.Options.ThrottleUpload)-1]
		var uploadLimit int64
		uploadLimit, err = strconv.ParseInt(upload, 10, 64)
		if err != nil {
			panic("Could not parse given Upload Limit")
		}
		minBurstSize := models.TCP_BUFFER_SIZE
		var rt rate.Limit
		switch unit := string(c.Options.ThrottleUpload[len(c.Options.ThrottleUpload)-1:]); unit {
		case "g", "G":
			uploadLimit = uploadLimit * 1024 * 1024 * 1024
		case "m", "M":
			uploadLimit = uploadLimit * 1024 * 1024
		case "k", "K":
			uploadLimit = uploadLimit * 1024
		default:
			uploadLimit, err = strconv.ParseInt(c.Options.ThrottleUpload, 10, 64)
			if err != nil {
				panic("Could not parse given Upload Limit")
			}
		}

		rt = rate.Every(time.Second / time.Duration(uploadLimit))
		if int(uploadLimit) > minBurstSize {
			minBurstSize = int(uploadLimit)
		}
		c.limiter = rate.NewLimiter(rt, minBurstSize)
		log.Debugf("Throttling Upload to %#v", c.limiter.Limit())
	}

	// initialize pake for recipient
	if !c.Options.IsSender {
		c.Pake, err = pake.InitCurve([]byte(c.Options.SharedSecret[5:]), 0, c.Options.Curve)
	}
	if err != nil {
		return
	}

	c.mutex = &sync.Mutex{}
	c.stop = newStop(context.Background())
	return
}

// TransferOptions for sending
type TransferOptions struct {
	PathToFiles      []string
	KeepPathInRemote bool
}

// helper function checking for an empty folder
func isEmptyFolder(folderPath string) (bool, error) {
	f, err := os.Open(folderPath)
	if err != nil {
		return false, err
	}
	defer f.Close()

	_, err = f.Readdirnames(1)
	if err == io.EOF {
		return true, nil
	}
	return false, nil
}

// helper function to walk each subfolder and parses against an ignore file.
// returns a hashmap Key: Absolute filepath, Value: boolean (true=ignore)
func gitWalk(dir string, gitObj *ignore.GitIgnore, files map[string]bool) {
	var ignoredDir bool
	var current string
	err := filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if isChild(current, path) && ignoredDir {
			files[path] = true
			return nil
		}
		if info.IsDir() && filepath.Base(path) == filepath.Base(dir) {
			ignoredDir = false // Skip applying ignore rules for root directory
			return nil
		}
		if gitObj.MatchesPath(info.Name()) {
			files[path] = true
			ignoredDir = true
			current = path
			return nil
		} else {
			files[path] = false
			ignoredDir = false
			return nil
		}
	})
	if err != nil {
		log.Errorf("filepath error")
	}
}

func isChild(parentPath, childPath string) bool {
	relPath, err := filepath.Rel(parentPath, childPath)
	if err != nil {
		return false
	}
	return !strings.HasPrefix(relPath, "..")
}

// This function retrieves the important file information
// for every file that will be transferred
func GetFilesInfo(fnames []string, zipfolder bool, ignoreGit bool, exclusions []string) (filesInfo []FileInfo, emptyFolders []FileInfo, totalNumberFolders int, err error) {
	// fnames: the relative/absolute paths of files/folders that will be transferred
	totalNumberFolders = 0
	var paths []string
	for _, fname := range fnames {
		// Support wildcard
		if strings.Contains(fname, "*") {
			matches, errGlob := filepath.Glob(fname)
			if errGlob != nil {
				err = errGlob
				return
			}
			paths = append(paths, matches...)
			continue
		} else {
			paths = append(paths, fname)
		}
	}
	ignoredPaths := make(map[string]bool)
	if ignoreGit {
		wd, wdErr := os.Stat(".gitignore")
		if wdErr == nil {
			gitIgnore, gitErr := ignore.CompileIgnoreFile(wd.Name())
			if gitErr == nil {
				for _, path := range paths {
					abs, absErr := filepath.Abs(path)
					if absErr != nil {
						err = absErr
						return
					}
					if gitIgnore.MatchesPath(path) {
						ignoredPaths[abs] = true
					}
				}
			}
		}
		for _, path := range paths {
			abs, absErr := filepath.Abs(path)
			if absErr != nil {
				err = absErr
				return
			}
			file, fileErr := os.Stat(path)
			if fileErr == nil && file.IsDir() {
				_, subErr := os.Stat(filepath.Join(path, ".gitignore"))
				if subErr == nil {
					gitObj, gitObjErr := ignore.CompileIgnoreFile(filepath.Join(path, ".gitignore"))
					if gitObjErr != nil {
						err = gitObjErr
						return
					}
					gitWalk(abs, gitObj, ignoredPaths)
				}
			}
		}
	}
	for _, fpath := range paths {
		stat, errStat := os.Lstat(fpath)

		if errStat != nil {
			err = errStat
			return
		}

		absPath, errAbs := filepath.Abs(fpath)

		if errAbs != nil {
			err = errAbs
			return
		}
		if stat.IsDir() && zipfolder {
			if fpath[len(fpath)-1:] != "/" {
				fpath += "/"
			}
			fpath = filepath.Dir(fpath)
			dest := filepath.Base(fpath) + ".zip"
			utils.ZipDirectory(dest, fpath)
			utils.MarkFileForRemoval(dest)
			stat, errStat = os.Lstat(dest)
			if errStat != nil {
				err = errStat
				return
			}
			absPath, errAbs = filepath.Abs(dest)
			if errAbs != nil {
				err = errAbs
				return
			}

			fInfo := FileInfo{
				Name:         stat.Name(),
				FolderRemote: "./",
				FolderSource: filepath.Dir(absPath),
				Size:         stat.Size(),
				ModTime:      stat.ModTime(),
				Mode:         stat.Mode(),
				TempFile:     true,
				IsIgnored:    ignoredPaths[absPath],
			}
			if fInfo.IsIgnored {
				continue
			}
			filesInfo = append(filesInfo, fInfo)
			continue
		}

		if stat.IsDir() {
			err = filepath.Walk(absPath,
				func(pathName string, info os.FileInfo, err error) error {
					if err != nil {
						return err
					}
					absPathWithSeparator := filepath.Dir(absPath)
					if !strings.HasSuffix(absPathWithSeparator, string(os.PathSeparator)) {
						absPathWithSeparator += string(os.PathSeparator)
					}
					if strings.HasSuffix(absPathWithSeparator, string(os.PathSeparator)+string(os.PathSeparator)) {
						absPathWithSeparator = strings.TrimSuffix(absPathWithSeparator, string(os.PathSeparator))
					}
					remoteFolder := strings.TrimPrefix(filepath.Dir(pathName), absPathWithSeparator)
					if !info.IsDir() {
						fInfo := FileInfo{
							Name:         info.Name(),
							FolderRemote: strings.ReplaceAll(remoteFolder, string(os.PathSeparator), "/") + "/",
							FolderSource: filepath.Dir(pathName),
							Size:         info.Size(),
							ModTime:      info.ModTime(),
							Mode:         info.Mode(),
							TempFile:     false,
							IsIgnored:    ignoredPaths[pathName],
						}
						if fInfo.IsIgnored && ignoreGit {
							return nil
						} else {
							filesInfo = append(filesInfo, fInfo)
						}
					} else {
						if ignoredPaths[pathName] {
							return filepath.SkipDir
						}
						isEmptyFolder, _ := isEmptyFolder(pathName)
						totalNumberFolders++
						if isEmptyFolder {
							emptyFolders = append(emptyFolders, FileInfo{
								// Name: info.Name(),
								FolderRemote: strings.ReplaceAll(strings.TrimPrefix(pathName,
									filepath.Dir(absPath)+string(os.PathSeparator)), string(os.PathSeparator), "/") + "/",
							})
						}
					}
					return nil
				})
			if err != nil {
				return
			}

		} else {
			fInfo := FileInfo{
				Name:         stat.Name(),
				FolderRemote: "./",
				FolderSource: filepath.Dir(absPath),
				Size:         stat.Size(),
				ModTime:      stat.ModTime(),
				Mode:         stat.Mode(),
				TempFile:     false,
				IsIgnored:    ignoredPaths[absPath],
			}
			if fInfo.IsIgnored && ignoreGit {
				continue
			} else {
				filesInfo = append(filesInfo, fInfo)
			}
		}
	}
	return
}

func (c *Client) sendCollectFiles(filesInfo []FileInfo) (err error) {
	c.FilesToTransfer = filesInfo
	totalFilesSize := int64(0)

	for i, fileInfo := range c.FilesToTransfer {
		var fullPath string
		fullPath = fileInfo.FolderSource + string(os.PathSeparator) + fileInfo.Name
		fullPath = filepath.Clean(fullPath)

		if len(fileInfo.Name) > c.longestFilename {
			c.longestFilename = len(fileInfo.Name)
		}

		if fileInfo.Mode&os.ModeSymlink != 0 {
			log.Debugf("%s is symlink", fileInfo.Name)
			c.FilesToTransfer[i].Symlink, err = os.Readlink(fullPath)
			if err != nil {
				log.Debugf("error getting symlink: %s", err.Error())
			}
			log.Debugf("%+v", c.FilesToTransfer[i])
		}

		if c.Options.HashAlgorithm == "" {
			c.Options.HashAlgorithm = "xxhash"
		}

		c.FilesToTransfer[i].Hash, err = c.stop.hash(fullPath, c.Options.HashAlgorithm, fileInfo.Size > 1e7)
		log.Debugf("hashed %s to %x using %s", fullPath, c.FilesToTransfer[i].Hash, c.Options.HashAlgorithm)
		totalFilesSize += fileInfo.Size
		if err != nil {
			return
		}
		log.Debugf("file %d info: %+v", i, c.FilesToTransfer[i])
		fmt.Fprintf(os.Stderr, "\r                                 ")
		fmt.Fprintf(os.Stderr, "\rSending %d files (%s)", i, utils.ByteCountDecimal(totalFilesSize))
	}
	log.Debugf("longestFilename: %+v", c.longestFilename)
	fname := fmt.Sprintf("%d files", len(c.FilesToTransfer))
	folderName := fmt.Sprintf("%d folders", c.TotalNumberFolders)
	if len(c.FilesToTransfer) == 1 {
		fname = fmt.Sprintf("'%s'", c.FilesToTransfer[0].Name)
	}
	if strings.HasPrefix(fname, "'croc-stdin-") {
		fname = "'stdin'"
		if c.Options.SendingText {
			fname = "'text'"
		}
	}

	fmt.Fprintf(os.Stderr, "\r                                 ")
	if c.TotalNumberFolders > 0 {
		fmt.Fprintf(os.Stderr, "\rSending %s and %s (%s)\n", fname, folderName, utils.ByteCountDecimal(totalFilesSize))
	} else {
		fmt.Fprintf(os.Stderr, "\rSending %s (%s)\n", fname, utils.ByteCountDecimal(totalFilesSize))
	}
	return
}

func (c *Client) setupLocalRelay() {
	// setup the relay locally
	firstPort, _ := strconv.Atoi(c.Options.RelayPorts[0])
	openPorts := utils.FindOpenPorts("127.0.0.1", firstPort, len(c.Options.RelayPorts))
	if len(openPorts) < len(c.Options.RelayPorts) {
		panic("not enough open ports to run local relay")
	}
	for i, port := range openPorts {
		c.Options.RelayPorts[i] = fmt.Sprint(port)
	}
	for _, port := range c.Options.RelayPorts {
		go func(portStr string) {
			debugString := "warn"
			if c.Options.Debug {
				debugString = "debug"
			}
			err := c.stop.run(
				debugString,
				"127.0.0.1",
				portStr,
				c.Options.RelayPassword,
				strings.Join(c.Options.RelayPorts[1:], ","))
			if err != nil {
				panic(err)
			}
		}(port)
	}
}

func (c *Client) broadcastOnLocalNetwork(useipv6 bool) {
	var timeLimit time.Duration
	// if we don't use an external relay, the broadcast messages need to be sent continuously
	if c.Options.OnlyLocal {
		timeLimit = -1 * time.Second
	} else {
		timeLimit = 30 * time.Second
	}
	// look for peers first
	settings := peerdiscovery.Settings{
		Limit:     -1,
		Payload:   []byte("croc" + c.Options.RelayPorts[0]),
		Delay:     20 * time.Millisecond,
		TimeLimit: timeLimit,
		StopChan:  c.stop.stopChan,
	}
	if useipv6 {
		settings.IPVersion = peerdiscovery.IPv6
	} else {
		settings.MulticastAddress = c.Options.MulticastAddress
	}

	discoveries, err := peerdiscovery.Discover(settings)
	log.Debugf("discoveries: %+v", discoveries)

	if err != nil {
		log.Debug(err)
	}
}

func (c *Client) transferOverLocalRelay(errchan chan<- error) {
	time.Sleep(500 * time.Millisecond)
	log.Debug("establishing connection")
	var banner string
	conn, banner, ipaddr, err := tcp.ConnectToTCPServer("127.0.0.1:"+c.Options.RelayPorts[0], c.Options.RelayPassword, c.Options.RoomName)
	log.Debugf("banner: %s", banner)
	if err != nil {
		err = fmt.Errorf("could not connect to 127.0.0.1:%s: %w", c.Options.RelayPorts[0], err)
		log.Debug(err)
		// not really an error because it will try to connect over the actual relay
		return
	}
	log.Debugf("local connection established: %+v", conn)
	for {
		if err := c.ctxErr(); err != nil {
			errchan <- err
			return
		}
		data, _ := conn.Receive()
		if bytes.Equal(data, handshakeRequest) {
			break
		} else if bytes.Equal(data, []byte{1}) {
			log.Trace("got ping")
		} else {
			log.Debugf("instead of handshake got: %s", data)
		}
	}
	c.conn[0] = conn
	log.Debug("exchanged header message")
	c.Options.RelayAddress = "127.0.0.1"
	c.Options.RelayPorts = strings.Split(banner, ",")
	if c.Options.NoMultiplexing {
		log.Debug("no multiplexing")
		c.Options.RelayPorts = []string{c.Options.RelayPorts[0]}
	}
	c.ExternalIP = ipaddr
	errchan <- c.transfer()
}

// Send will send the specified file
func (c *Client) Send(filesInfo []FileInfo, emptyFoldersToTransfer []FileInfo, totalNumberFolders int) (err error) {
	go c.stop.done()
	defer c.stop.Cancel()
	c.EmptyFoldersToTransfer = emptyFoldersToTransfer
	c.TotalNumberFolders = totalNumberFolders
	c.TotalNumberOfContents = len(filesInfo)
	err = c.sendCollectFiles(filesInfo)
	if err != nil {
		return
	}
	flags := &strings.Builder{}
	if c.Options.RelayAddress != models.DEFAULT_RELAY && !c.Options.OnlyLocal {
		flags.WriteString("--relay " + c.Options.RelayAddress + " ")
	}
	if c.Options.RelayPassword != models.DEFAULT_PASSPHRASE {
		flags.WriteString("--pass " + c.Options.RelayPassword + " ")
	}
	fmt.Fprintf(os.Stderr, `Code is: %[1]s

On the other computer run:
(For Windows)
    croc %[2]s%[1]s
(For Linux/macOS)
    CROC_SECRET=%[1]q croc %[2]s
`, c.Options.SharedSecret, flags.String())
	if !c.Options.DisableClipboard {
		clipboardText := c.Options.SharedSecret
		if c.Options.ExtendedClipboard {
			clipboardText = fmt.Sprintf("CROC_SECRET=%q croc %s", c.Options.SharedSecret, strings.TrimSpace(flags.String()))
		}
		copyToClipboard(clipboardText, c.Options.Quiet, c.Options.ExtendedClipboard)
	}
	if c.Options.ShowQrCode {
		showReceiveCommandQrCode(fmt.Sprintf("%[1]s", c.Options.SharedSecret))
	}
	if c.Options.Ask {
		machid, _ := machineid.ID()
		fmt.Fprintf(os.Stderr, "\rYour machine ID is '%s'\n", machid)
	}
	// c.spinner.Suffix = " waiting for recipient..."
	// c.spinner.Start()
	// create channel for quitting
	// connect to the relay for messaging
	errchan := make(chan error, 1)

	if !c.Options.DisableLocal {
		// add two things to the error channel
		errchan = make(chan error, 2)
		c.setupLocalRelay()
		// broadcast on ipv4
		go c.broadcastOnLocalNetwork(false)
		// broadcast on ipv6
		go c.broadcastOnLocalNetwork(true)
		go c.transferOverLocalRelay(errchan)
	}

	if !c.Options.OnlyLocal {
		go func() {
			var ipaddr, banner string
			var conn *comm.Comm
			durations := []time.Duration{100 * time.Millisecond, 5 * time.Second}
			for i, address := range []string{c.Options.RelayAddress6, c.Options.RelayAddress} {
				if address == "" {
					continue
				}
				host, port, _ := net.SplitHostPort(address)
				log.Debugf("host: '%s', port: '%s'", host, port)
				// Default port to :9009
				if port == "" {
					host = address
					port = models.DEFAULT_PORT
				}
				log.Debugf("got host '%v' and port '%v'", host, port)
				address = net.JoinHostPort(host, port)
				log.Debugf("trying connection to %s", address)
				conn, banner, ipaddr, err = tcp.ConnectToTCPServer(address, c.Options.RelayPassword, c.Options.RoomName, durations[i])
				if err == nil {
					c.Options.RelayAddress = address
					break
				}
				log.Debugf("could not establish '%s'", address)
			}
			if conn == nil && err == nil {
				err = fmt.Errorf("could not connect")
			}
			if err != nil {
				err = fmt.Errorf("could not connect to %s: %w", c.Options.RelayAddress, err)
				log.Debug(err)
				errchan <- err
				return
			}
			log.Debugf("banner: %s", banner)
			log.Debugf("connection established: %+v", conn)
			var kB []byte
			B, _ := pake.InitCurve([]byte(c.Options.SharedSecret[5:]), 1, c.Options.Curve)
			for {
				if err := c.ctxErr(); err != nil {
					errchan <- err
					return
				}
				var dataMessage SimpleMessage
				log.Trace("waiting for bytes")
				data, errConn := conn.Receive()
				if errConn != nil {
					log.Tracef("[%+v] had error: %s", conn, errConn.Error())
				}
				json.Unmarshal(data, &dataMessage)
				log.Tracef("data: %+v '%s'", data, data)
				log.Tracef("dataMessage: %s", dataMessage)
				log.Tracef("kB: %x", kB)
				// if kB not null, then use it to decrypt
				if kB != nil {
					var decryptErr error
					var dataDecrypt []byte
					dataDecrypt, decryptErr = crypt.Decrypt(data, kB)
					if decryptErr != nil {
						log.Tracef("error decrypting: %v: '%s'", decryptErr, data)
						// relay sent a message encrypted with an invalid key.
						// consider this a security issue and abort
						if strings.Contains(decryptErr.Error(), "message authentication failed") {
							errchan <- decryptErr
							return
						}
					} else {
						// copy dataDecrypt to data
						data = dataDecrypt
						log.Tracef("decrypted: %s", data)
					}
				}
				if bytes.Equal(data, ipRequest) {
					log.Tracef("got ipRequest")
					// recipient wants to try to connect to local ips
					var ips []string
					// only get local ips if the local is enabled
					if !c.Options.DisableLocal {
						// get list of local ips
						ips, err = utils.GetLocalIPs()
						if err != nil {
							log.Tracef("error getting local ips: %v", err)
						}
						// prepend the port that is being listened to
						ips = append([]string{c.Options.RelayPorts[0]}, ips...)
					}
					log.Tracef("sending ips: %+v", ips)
					bips, errIps := json.Marshal(ips)
					if errIps != nil {
						log.Tracef("error marshalling ips: %v", errIps)
					}
					bips, errIps = crypt.Encrypt(bips, kB)
					if errIps != nil {
						log.Tracef("error encrypting ips: %v", errIps)
					}
					if err = conn.Send(bips); err != nil {
						log.Errorf("error sending: %v", err)
					}
				} else if dataMessage.Kind == "pake1" {
					log.Trace("got pake1")
					var pakeError error
					pakeError = B.Update(dataMessage.Bytes)
					if pakeError == nil {
						kB, pakeError = B.SessionKey()
						if pakeError == nil {
							log.Tracef("dataMessage kB: %x", kB)
							dataMessage.Bytes = B.Bytes()
							dataMessage.Kind = "pake2"
							data, _ = json.Marshal(dataMessage)
							if pakeError = conn.Send(data); err != nil {
								log.Errorf("dataMessage error sending: %v", err)
							}
						}

					}
				} else if bytes.Equal(data, handshakeRequest) {
					log.Trace("got handshake")
					break
				} else if bytes.Equal(data, []byte{1}) {
					log.Trace("got ping")
					continue
				} else {
					log.Tracef("[%+v] got weird bytes: %+v", conn, data)
					// throttle the reading
					errchan <- fmt.Errorf("gracefully refusing using the public relay")
					return
				}
			}

			c.conn[0] = conn
			c.Options.RelayPorts = strings.Split(banner, ",")
			if c.Options.NoMultiplexing {
				log.Debug("no multiplexing")
				c.Options.RelayPorts = []string{c.Options.RelayPorts[0]}
			}
			c.ExternalIP = ipaddr
			log.Debug("exchanged header message")
			errchan <- c.transfer()
		}()
	}

	err = <-errchan
	if err == nil {
		return // no error
	} else {
		log.Debugf("error from errchan: %v", err)
		if strings.Contains(err.Error(), "could not secure channel") {
			return err
		}
	}
	if !c.Options.DisableLocal {
		if strings.Contains(err.Error(), "refusing files") || strings.Contains(err.Error(), "EOF") || strings.Contains(err.Error(), "bad password") || strings.Contains(err.Error(), "message authentication failed") {
			errchan <- err
		}
		err = <-errchan
	}
	return err
}

func showReceiveCommandQrCode(command string) {
	qrCode, err := qrcode.New(command, qrcode.Medium)
	if err == nil {
		fmt.Println(qrCode.ToSmallString(false))
	}
}

// Receive will receive a file
func (c *Client) Receive() (err error) {
	go c.stop.done()
	defer c.stop.Cancel()
	fmt.Fprintf(os.Stderr, "connecting...")
	// recipient will look for peers first
	// and continue if it doesn't find any within 100 ms
	usingLocal := false
	isIPset := false

	if c.Options.OnlyLocal || c.Options.IP != "" {
		c.Options.RelayAddress = ""
		c.Options.RelayAddress6 = ""
	}

	if c.Options.IP != "" {
		// check ip version
		if strings.Count(c.Options.IP, ":") >= 2 {
			log.Debug("assume ipv6")
			c.Options.RelayAddress6 = c.Options.IP
		}
		if strings.Contains(c.Options.IP, ".") {
			log.Debug("assume ipv4")
			c.Options.RelayAddress = c.Options.IP
		}
		isIPset = true
	}

	if !c.Options.DisableLocal && !isIPset {
		log.Debug("attempt to discover peers")
		var discoveries []peerdiscovery.Discovered
		var wgDiscovery sync.WaitGroup
		var dmux sync.Mutex
		wgDiscovery.Add(2)
		go func() {
			defer wgDiscovery.Done()
			ipv4discoveries, err1 := peerdiscovery.Discover(peerdiscovery.Settings{
				Limit:            1,
				Payload:          []byte("ok"),
				Delay:            20 * time.Millisecond,
				TimeLimit:        200 * time.Millisecond,
				MulticastAddress: c.Options.MulticastAddress,
				StopChan:         c.stop.stopChan,
			})
			if err1 == nil && len(ipv4discoveries) > 0 {
				dmux.Lock()
				err = err1
				discoveries = append(discoveries, ipv4discoveries...)
				dmux.Unlock()
			}
		}()
		go func() {
			defer wgDiscovery.Done()
			ipv6discoveries, err1 := peerdiscovery.Discover(peerdiscovery.Settings{
				Limit:     1,
				Payload:   []byte("ok"),
				Delay:     20 * time.Millisecond,
				TimeLimit: 200 * time.Millisecond,
				IPVersion: peerdiscovery.IPv6,
				StopChan:  c.stop.stopChan,
			})
			if err1 == nil && len(ipv6discoveries) > 0 {
				dmux.Lock()
				err = err1
				discoveries = append(discoveries, ipv6discoveries...)
				dmux.Unlock()
			}
		}()
		wgDiscovery.Wait()

		if err == nil && len(discoveries) > 0 {
			log.Debugf("all discoveries: %+v", discoveries)
			for i := 0; i < len(discoveries); i++ {
				log.Debugf("discovery %d has payload: %+v", i, discoveries[i])
				if !bytes.HasPrefix(discoveries[i].Payload, []byte("croc")) {
					log.Debug("skipping discovery")
					continue
				}
				log.Debug("switching to local")
				portToUse := string(bytes.TrimPrefix(discoveries[i].Payload, []byte("croc")))
				if portToUse == "" {
					portToUse = models.DEFAULT_PORT
				}
				address := net.JoinHostPort(discoveries[i].Address, portToUse)
				errPing := tcp.PingServer(address)
				if errPing == nil {
					log.Debugf("successfully pinged '%s'", address)
					c.Options.RelayAddress = address
					c.ExternalIPConnected = c.Options.RelayAddress
					c.Options.RelayAddress6 = ""
					usingLocal = true
					break
				} else {
					log.Debugf("could not ping: %+v", errPing)
				}
			}
		}
		log.Debugf("discoveries: %+v", discoveries)
		log.Debug("establishing connection")
	}
	var banner string
	durations := []time.Duration{200 * time.Millisecond, 5 * time.Second}
	err = fmt.Errorf("found no addresses to connect")
	for i, address := range []string{c.Options.RelayAddress6, c.Options.RelayAddress} {
		if address == "" {
			continue
		}
		var host, port string
		host, port, _ = net.SplitHostPort(address)
		// Default port to :9009
		if port == "" {
			host = address
			port = models.DEFAULT_PORT
		}
		log.Debugf("got host '%v' and port '%v'", host, port)
		address = net.JoinHostPort(host, port)
		log.Debugf("trying connection to %s", address)
		c.conn[0], banner, c.ExternalIP, err = tcp.ConnectToTCPServer(address, c.Options.RelayPassword, c.Options.RoomName, durations[i])
		if err == nil {
			c.Options.RelayAddress = address
			break
		}
		log.Debugf("could not establish '%s'", address)
	}
	if err != nil {
		err = fmt.Errorf("could not connect to %s: %w", c.Options.RelayAddress, err)
		log.Debug(err)
		return
	}
	log.Debugf("receiver connection established: %+v", c.conn[0])
	log.Debugf("banner: %s", banner)

	if c.Options.TestFlag {
		log.Debugf("TEST FLAG ENABLED, TESTING LOCAL IPS")
	}
	if c.Options.TestFlag || (!usingLocal && !c.Options.DisableLocal && !isIPset) {
		// ask the sender for their local ips and port
		// and try to connect to them
		var ips []string
		err = func() (err error) {
			var A *pake.Pake
			var data []byte
			A, err = pake.InitCurve([]byte(c.Options.SharedSecret[5:]), 0, c.Options.Curve)
			if err != nil {
				return err
			}
			dataMessage := SimpleMessage{
				Bytes: A.Bytes(),
				Kind:  "pake1",
			}
			data, _ = json.Marshal(dataMessage)
			if err = c.conn[0].Send(data); err != nil {
				log.Errorf("dataMessage send error: %v", err)
				return
			}
			data, err = c.conn[0].Receive()
			if err != nil {
				return
			}
			err = json.Unmarshal(data, &dataMessage)
			if err != nil || dataMessage.Kind != "pake2" {
				log.Debugf("data: %s", data)
				return fmt.Errorf("dataMessage %s pake failed", ipRequest)
			}
			err = A.Update(dataMessage.Bytes)
			if err != nil {
				return
			}
			var kA []byte
			kA, err = A.SessionKey()
			if err != nil {
				return
			}
			log.Debugf("dataMessage kA: %x", kA)

			// secure ipRequest
			data, err = crypt.Encrypt([]byte(ipRequest), kA)
			if err != nil {
				return
			}
			log.Debug("sending ips?")
			if err = c.conn[0].Send(data); err != nil {
				log.Errorf("ips send error: %v", err)
			}
			data, err = c.conn[0].Receive()
			if err != nil {
				return
			}
			data, err = crypt.Decrypt(data, kA)
			if err != nil {
				return
			}
			log.Debugf("ips data: %s", data)
			if err = json.Unmarshal(data, &ips); err != nil {
				log.Debugf("ips unmarshal error: %v", err)
			}
			return
		}()

		if len(ips) > 1 {
			port := ips[0]
			ips = ips[1:]
			for _, ip := range ips {
				ipv4Addr, ipv4Net, errNet := net.ParseCIDR(fmt.Sprintf("%s/24", ip))
				log.Debugf("ipv4Add4: %+v, ipv4Net: %+v, err: %+v", ipv4Addr, ipv4Net, errNet)

				// For peer-to-peer connectivity within a LAN, the sender and receiver don't need to be on the same subnet.
				// Even with NAT routers in their respective local networks,
				// a receiver behind NAT can establish direct access to the sender without requiring internet connectivity.
				// Conversely, the local networks on the sender and receiver may overlap but not be connected.
				// This often occurs with 192.168.0.0/30 and 192.168.1.0/30 subnets.

				// localIps, _ := utils.GetLocalIPs()
				// haveLocalIP := false
				// for _, localIP := range localIps {
				// 	localIPparsed := net.ParseIP(localIP)
				// 	log.Debugf("localIP: %+v, localIPparsed: %+v", localIP, localIPparsed)
				// 	if ipv4Net.Contains(localIPparsed) {
				// 		haveLocalIP = true
				// 		log.Debugf("ip: %+v is a local IP", ip)
				// 		break
				// 	}
				// }
				// if !haveLocalIP {
				// 	log.Debugf("%s is not a local IP, skipping", ip)
				// 	continue
				// }

				serverTry := net.JoinHostPort(ip, port)
				conn, banner2, externalIP, errConn := tcp.ConnectToTCPServer(serverTry, c.Options.RelayPassword, c.Options.RoomName, 500*time.Millisecond)
				if errConn != nil {
					log.Debug(errConn)
					log.Debug("could not connect to " + serverTry)
					continue
				}
				log.Debugf("local connection established to %s", serverTry)
				log.Debugf("banner: %s", banner2)
				// reset to the local port
				banner = banner2
				c.Options.RelayAddress = serverTry
				c.ExternalIP = externalIP
				c.conn[0].Close()
				c.conn[0] = nil
				c.conn[0] = conn
				break
			}
		}
	}

	if err = c.conn[0].Send(handshakeRequest); err != nil {
		log.Errorf("handshake send error: %v", err)
	}
	c.Options.RelayPorts = strings.Split(banner, ",")
	if c.Options.NoMultiplexing {
		log.Debug("no multiplexing")
		c.Options.RelayPorts = []string{c.Options.RelayPorts[0]}
	}
	log.Debug("exchanged header message")
	fmt.Fprintf(os.Stderr, "\rsecuring channel...")
	err = c.transfer()
	if err == nil {
		if c.numberOfTransferredFiles+len(c.EmptyFoldersToTransfer) == 0 {
			fmt.Fprintf(os.Stderr, "\rNo files transferred.\n")
		}
	} else {
		c.SendError()
	}
	return
}

func (c *Client) transfer() (err error) {
	// connect to the server

	// quit with c.quit <- true
	c.quit = make(chan bool)

	// if recipient, initialize with sending pake information
	log.Debug("ready")
	if !c.Options.IsSender && !c.Step1ChannelSecured {
		err = message.Send(c.conn[0], c.Key, message.Message{
			Type:   message.TypePAKE,
			Bytes:  c.Pake.Bytes(),
			Bytes2: []byte(c.Options.Curve),
		})
		if err != nil {
			return
		}
	}

	// listen for incoming messages and process them
	for {
		if e := c.ctxErr(); e != nil {
			log.Tracef("transfer: %v", e)
			err = e
			break
		}
		var data []byte
		var done bool
		data, err = c.conn[0].Receive()
		if err != nil {
			log.Debugf("got error receiving: %v", err)
			if !c.Step1ChannelSecured {
				err = fmt.Errorf("could not secure channel")
			}
			break
		}
		done, err = c.processMessage(data)
		if err != nil {
			log.Debugf("data: %s", data)
			log.Debugf("got error processing: %v", err)
			break
		}
		if done {
			break
		}
	}
	if err := c.ctxErr(); err != nil && c.SuccessfulTransfer {
		c.SuccessfulTransfer = false
		log.Tracef("SuccessfulTransfer: %v", err)
	}
	// purge errors that come from successful transfer
	if c.SuccessfulTransfer {
		if err != nil {
			log.Debugf("purging error: %s", err)
		}
		err = nil
	}
	if c.Options.IsSender && c.SuccessfulTransfer {
		for _, file := range c.FilesToTransfer {
			if file.TempFile {
				fmt.Println("Removing " + file.Name)
				os.Remove(file.Name)
			}
		}
	}

	if c.SuccessfulTransfer && !c.Options.IsSender {
		for _, file := range c.FilesToTransfer {
			if file.TempFile {
				if unzipErr := utils.UnzipDirectory(".", file.Name); unzipErr != nil {
					c.SuccessfulTransfer = false
					err = fmt.Errorf("failed to unzip received archive %s: %w", file.Name, unzipErr)
					log.Error(err)
					break
				}
				if removeErr := os.Remove(file.Name); removeErr != nil {
					log.Warnf("error removing %s: %v", file.Name, removeErr)
				} else {
					log.Debugf("Removing %s\n", file.Name)
				}
			}
		}
	}

	if c.Options.Stdout && !c.Options.IsSender && len(c.FilesToTransfer) > 0 && c.FilesToTransferCurrentNum < len(c.FilesToTransfer) {
		pathToFile := path.Join(
			c.FilesToTransfer[c.FilesToTransferCurrentNum].FolderRemote,
			c.FilesToTransfer[c.FilesToTransferCurrentNum].Name,
		)
		log.Debugf("pathToFile: %s", pathToFile)
		// close if not closed already
		if !c.CurrentFileIsClosed {
			c.CurrentFile.Close()
			c.CurrentFileIsClosed = true
		}
		if err = os.Remove(pathToFile); err != nil {
			log.Warnf("error removing %s: %v", pathToFile, err)
		}
		fmt.Fprint(os.Stderr, "\n")
	}
	if err != nil && strings.Contains(err.Error(), "pake not successful") {
		log.Debugf("pake error: %s", err.Error())
		err = fmt.Errorf("password mismatch")
	}
	if err != nil && strings.Contains(err.Error(), "unexpected end of JSON input") {
		log.Debugf("error: %s", err.Error())
		err = fmt.Errorf("room (secure channel) not ready, maybe peer disconnected")
	}
	if err != nil {
		c.SendError()
	}
	return
}

func (c *Client) createEmptyFolder(i int) (err error) {
	err = os.MkdirAll(c.EmptyFoldersToTransfer[i].FolderRemote, os.ModePerm)
	if err != nil {
		return
	}
	fmt.Fprintf(os.Stderr, "%s\n", c.EmptyFoldersToTransfer[i].FolderRemote)
	c.bar = progressbar.NewOptions64(1,
		progressbar.OptionOnCompletion(func() {
			c.fmtPrintUpdate()
		}),
		progressbar.OptionSetWidth(20),
		progressbar.OptionSetDescription(" "),
		progressbar.OptionSetRenderBlankState(true),
		progressbar.OptionShowBytes(true),
		progressbar.OptionShowCount(),
		progressbar.OptionSetWriter(os.Stderr),
		progressbar.OptionSetVisibility(!c.Options.SendingText),
	)
	c.bar.Finish()
	return
}

func (c *Client) processMessageFileInfo(m message.Message) (done bool, err error) {
	var senderInfo SenderInfo
	err = json.Unmarshal(m.Bytes, &senderInfo)
	if err != nil {
		log.Debug(err)
		return
	}
	c.Options.SendingText = senderInfo.SendingText
	c.Options.NoCompress = senderInfo.NoCompress
	c.Options.HashAlgorithm = senderInfo.HashAlgorithm
	c.EmptyFoldersToTransfer = senderInfo.EmptyFoldersToTransfer
	c.TotalNumberFolders = senderInfo.TotalNumberFolders
	c.FilesToTransfer = senderInfo.FilesToTransfer
	for i, fi := range c.FilesToTransfer {
		// Issues #593 - sanitize the sender paths and prevent ".." from being used
		c.FilesToTransfer[i].FolderRemote = filepath.Clean(fi.FolderRemote)
		// Issues #593 - disallow specific folders like .ssh
		if strings.Contains(c.FilesToTransfer[i].FolderRemote, ".ssh") {
			return true, fmt.Errorf("invalid path detected: '%s'", fi.FolderRemote)
		}
		// Issue #595 - disallow filenames with invisible characters
		errFileName := utils.ValidFileName(path.Join(c.FilesToTransfer[i].FolderRemote, fi.Name))
		if errFileName != nil {
			return true, errFileName
		}
	}
	c.TotalNumberOfContents = 0
	if c.FilesToTransfer != nil {
		c.TotalNumberOfContents += len(c.FilesToTransfer)
	}
	if c.EmptyFoldersToTransfer != nil {
		c.TotalNumberOfContents += len(c.EmptyFoldersToTransfer)
	}

	if c.Options.HashAlgorithm == "" {
		c.Options.HashAlgorithm = "xxhash"
	}
	log.Debugf("using hash algorithm: %s", c.Options.HashAlgorithm)
	if c.Options.NoCompress {
		log.Debug("disabling compression")
	}
	if c.Options.SendingText {
		c.Options.Stdout = true
	}

	fname := fmt.Sprintf("%d files", len(c.FilesToTransfer))
	folderName := fmt.Sprintf("%d folders", c.TotalNumberFolders)
	if len(c.FilesToTransfer) == 1 {
		fname = fmt.Sprintf("'%s'", c.FilesToTransfer[0].Name)
	}
	totalSize := int64(0)
	for i, fi := range c.FilesToTransfer {
		totalSize += fi.Size
		if len(fi.Name) > c.longestFilename {
			c.longestFilename = len(fi.Name)
		}
		if strings.HasPrefix(fi.Name, "croc-stdin-") && c.Options.SendingText {
			c.FilesToTransfer[i].Name, err = utils.RandomFileName()
			if err != nil {
				return
			}
		}
	}
	// check the totalSize does not exceed disk space
	// usage := diskusage.NewDiskUsage(".")
	// if usage.Available() < uint64(totalSize) {
	// 	return true, fmt.Errorf("not enough disk space")
	// }

	// c.spinner.Stop()
	action := "Accept"
	if c.Options.SendingText {
		action = "Display"
		fname = "text message"
	}
	if !c.Options.NoPrompt || c.Options.Ask || senderInfo.Ask {
		if c.Options.Ask || senderInfo.Ask {
			machID, _ := machineid.ID()
			fmt.Fprintf(os.Stderr, "\rYour machine id is '%s'.\n%s %s (%s) from '%s'? (Y/n) ", machID, action, fname, utils.ByteCountDecimal(totalSize), senderInfo.MachineID)
		} else {
			if c.TotalNumberFolders > 0 {
				fmt.Fprintf(os.Stderr, "\r%s %s and %s (%s)? (Y/n) ", action, fname, folderName, utils.ByteCountDecimal(totalSize))
			} else {
				fmt.Fprintf(os.Stderr, "\r%s %s (%s)? (Y/n) ", action, fname, utils.ByteCountDecimal(totalSize))
			}
		}
		choice := strings.ToLower(utils.GetInput(""))
		if choice != "" && choice != "y" && choice != "yes" {
			err = message.Send(c.conn[0], c.Key, message.Message{
				Type:    message.TypeError,
				Message: "refusing files",
			})
			if err != nil {
				return false, err
			}
			return true, fmt.Errorf("refused files")
		}
	} else {
		fmt.Fprintf(os.Stderr, "\rReceiving %s (%s) \n", fname, utils.ByteCountDecimal(totalSize))
	}
	fmt.Fprintf(os.Stderr, "\nReceiving (<-%s)\n", c.ExternalIPConnected)

	for i := 0; i < len(c.EmptyFoldersToTransfer); i += 1 {
		_, errExists := os.Stat(c.EmptyFoldersToTransfer[i].FolderRemote)
		if os.IsNotExist(errExists) {
			err = c.createEmptyFolder(i)
			if err != nil {
				return
			}
		} else {
			isEmpty, _ := isEmptyFolder(c.EmptyFoldersToTransfer[i].FolderRemote)
			if !isEmpty {
				log.Debug("asking to overwrite")
				prompt := fmt.Sprintf("\n%s already has some content in it. \nDo you want"+
					" to overwrite it with an empty folder? (y/N) ", c.EmptyFoldersToTransfer[i].FolderRemote)
				choice := strings.ToLower(utils.GetInput(prompt))
				if choice == "y" || choice == "yes" {
					err = c.createEmptyFolder(i)
					if err != nil {
						return
					}
				}
			}
		}
	}

	// if no files are to be transferred, then we can end the file transfer process
	if c.FilesToTransfer == nil {
		c.SuccessfulTransfer = true
		c.Step3RecipientRequestFile = true
		c.Step4FileTransferred = true
		errStopTransfer := message.Send(c.conn[0], c.Key, message.Message{
			Type: message.TypeFinished,
		})
		if errStopTransfer != nil {
			err = errStopTransfer
		}
	}
	log.Debug(c.FilesToTransfer)
	c.Step2FileInfoTransferred = true
	return
}

func (c *Client) processMessagePake(m message.Message) (err error) {
	defer func() {
		if r := recover(); r != nil {
			if c.stop.gui {
				log.Errorf("panic: %v", r)
				c.stop.Cancel()
			} else {
				panic(r)
			}
		}
	}()
	log.Debug("received pake payload")

	var salt []byte
	if c.Options.IsSender {
		// initialize curve based on the recipient's choice
		log.Debugf("using curve %s", string(m.Bytes2))
		c.Pake, err = pake.InitCurve([]byte(c.Options.SharedSecret[5:]), 1, string(m.Bytes2))
		if err != nil {
			log.Error(err)
			return
		}

		// update the pake
		err = c.Pake.Update(m.Bytes)
		if err != nil {
			return
		}

		// generate salt and send it back to recipient
		log.Debug("generating salt")
		salt = make([]byte, 8)
		if _, rerr := rand.Read(salt); err != nil {
			log.Errorf("can't generate random numbers: %v", rerr)
			return
		}
		log.Debug("sender sending pake+salt")
		err = message.Send(c.conn[0], c.Key, message.Message{
			Type:   message.TypePAKE,
			Bytes:  c.Pake.Bytes(),
			Bytes2: salt,
		})
	} else {
		err = c.Pake.Update(m.Bytes)
		if err != nil {
			return
		}
		salt = m.Bytes2
	}
	// generate key
	key, err := c.Pake.SessionKey()
	if err != nil {
		return err
	}
	c.Key, _, err = crypt.New(key, salt)
	if err != nil {
		return err
	}
	log.Debugf("generated key = %+x with salt %x", c.Key, salt)

	// connects to the other ports of the server for transfer
	var wg sync.WaitGroup
	wg.Add(len(c.Options.RelayPorts))
	for i := 0; i < len(c.Options.RelayPorts); i++ {
		log.Debugf("port: [%s]", c.Options.RelayPorts[i])
		go func(j int) {
			defer wg.Done()
			var host string
			if c.Options.RelayAddress == "127.0.0.1" {
				host = c.Options.RelayAddress
			} else {
				host, _, err = net.SplitHostPort(c.Options.RelayAddress)
				if err != nil {
					log.Errorf("bad relay address %s", c.Options.RelayAddress)
					return
				}
			}
			server := net.JoinHostPort(host, c.Options.RelayPorts[j])
			log.Debugf("connecting to %s", server)
			c.conn[j+1], _, _, err = tcp.ConnectToTCPServer(
				server,
				c.Options.RelayPassword,
				fmt.Sprintf("%s-%d", c.Options.RoomName, j),
			)
			if err != nil {
				panic(err)
			}
			log.Debugf("connected to %s", server)
			if !c.Options.IsSender {
				go c.receiveData(j)
			}
		}(i)
	}
	wg.Wait()
	if !c.Options.IsSender {
		log.Debug("sending external IP")
		err = message.Send(c.conn[0], c.Key, message.Message{
			Type:    message.TypeExternalIP,
			Message: c.ExternalIP,
			Bytes:   m.Bytes,
		})
	}
	return
}

func (c *Client) processExternalIP(m message.Message) (done bool, err error) {
	log.Debugf("received external IP: %+v", m)
	if c.Options.IsSender {
		err = message.Send(c.conn[0], c.Key, message.Message{
			Type:    message.TypeExternalIP,
			Message: c.ExternalIP,
		})
		if err != nil {
			return true, err
		}
	}
	if c.ExternalIPConnected == "" {
		// it can be preset by the local relay
		c.ExternalIPConnected = m.Message
	}
	log.Debugf("connected as %s -> %s", c.ExternalIP, c.ExternalIPConnected)
	c.Step1ChannelSecured = true
	return
}

func (c *Client) processMessage(payload []byte) (done bool, err error) {
	m, err := message.Decode(c.Key, payload)
	if err != nil {
		err = fmt.Errorf("problem with decoding: %w", err)
		log.Debug(err)
		return
	}

	// only "pake" messages should be unencrypted
	// if a non-"pake" message is received unencrypted something
	// is weird
	if m.Type != message.TypePAKE && c.Key == nil {
		err = fmt.Errorf("unencrypted communication rejected")
		done = true
		return
	}

	switch m.Type {
	case message.TypeFinished:
		err = message.Send(c.conn[0], c.Key, message.Message{
			Type: message.TypeFinished,
		})
		done = true
		c.SuccessfulTransfer = true
		return
	case message.TypePAKE:
		err = c.processMessagePake(m)
		if err != nil {
			err = fmt.Errorf("pake not successful: %w", err)
			log.Debug(err)
		}
	case message.TypeExternalIP:
		done, err = c.processExternalIP(m)
	case message.TypeError:
		// c.spinner.Stop()
		log.Trace("Peer initiates interruption of my loops and goroutines")
		c.stop.Cancel()
		fmt.Print("\r")
		err = fmt.Errorf("peer error: %s", m.Message)
		return true, err
	case message.TypeFileInfo:
		done, err = c.processMessageFileInfo(m)
	case message.TypeRecipientReady:
		var remoteFile RemoteFileRequest
		err = json.Unmarshal(m.Bytes, &remoteFile)
		if err != nil {
			return
		}
		c.FilesToTransferCurrentNum = remoteFile.FilesToTransferCurrentNum
		c.CurrentFileChunkRanges = remoteFile.CurrentFileChunkRanges
		c.CurrentFileChunks = utils.ChunkRangesToChunks(c.CurrentFileChunkRanges)
		log.Debugf("current file chunks: %+v", c.CurrentFileChunks)
		c.mutex.Lock()
		c.chunkMap = make(map[uint64]struct{})
		for _, chunk := range c.CurrentFileChunks {
			c.chunkMap[uint64(chunk)] = struct{}{}
		}
		c.mutex.Unlock()
		c.Step3RecipientRequestFile = true

		if c.Options.Ask {
			fmt.Fprintf(os.Stderr, "Send to machine '%s'? (Y/n) ", remoteFile.MachineID)
			choice := strings.ToLower(utils.GetInput(""))
			if choice != "" && choice != "y" && choice != "yes" {
				err = message.Send(c.conn[0], c.Key, message.Message{
					Type:    message.TypeError,
					Message: "refusing files",
				})
				done = true
				return
			}
		}
	case message.TypeCloseSender:
		c.bar.Finish()
		log.Debug("close-sender received...")
		c.Step4FileTransferred = false
		c.Step3RecipientRequestFile = false
		log.Debug("sending close-recipient")
		err = message.Send(c.conn[0], c.Key, message.Message{
			Type: message.TypeCloseRecipient,
		})
	case message.TypeCloseRecipient:
		c.Step4FileTransferred = false
		c.Step3RecipientRequestFile = false
	}
	if err != nil {
		log.Debugf("got error from processing message: %v", err)
		return
	}
	err = c.updateState()
	if err != nil {
		log.Debugf("got error from updating state: %v", err)
		return
	}
	return
}

func (c *Client) updateIfSenderChannelSecured() (err error) {
	if c.Options.IsSender && c.Step1ChannelSecured && !c.Step2FileInfoTransferred {
		var b []byte
		machID, _ := machineid.ID()
		b, err = json.Marshal(SenderInfo{
			FilesToTransfer:        c.FilesToTransfer,
			EmptyFoldersToTransfer: c.EmptyFoldersToTransfer,
			MachineID:              machID,
			Ask:                    c.Options.Ask,
			TotalNumberFolders:     c.TotalNumberFolders,
			SendingText:            c.Options.SendingText,
			NoCompress:             c.Options.NoCompress,
			HashAlgorithm:          c.Options.HashAlgorithm,
		})
		if err != nil {
			log.Error(err)
			return
		}
		err = message.Send(c.conn[0], c.Key, message.Message{
			Type:  message.TypeFileInfo,
			Bytes: b,
		})
		if err != nil {
			return
		}

		c.Step2FileInfoTransferred = true
	}
	return
}

func (c *Client) recipientInitializeFile() (err error) {
	// start initiating the process to receive a new file
	log.Debugf("working on file %d", c.FilesToTransferCurrentNum)

	// recipient sets the file
	pathToFile := path.Join(
		c.FilesToTransfer[c.FilesToTransferCurrentNum].FolderRemote,
		c.FilesToTransfer[c.FilesToTransferCurrentNum].Name,
	)
	folderForFile, _ := filepath.Split(pathToFile)
	folderForFileBase := filepath.Base(folderForFile)
	if folderForFileBase != "." && folderForFileBase != "" {
		if err := os.MkdirAll(folderForFile, os.ModePerm); err != nil {
			log.Errorf("can't create %s: %v", folderForFile, err)
		}
	}
	var errOpen error
	c.CurrentFile, errOpen = os.OpenFile(
		pathToFile,
		os.O_WRONLY, 0o666)
	var truncate bool // default false
	c.CurrentFileChunks = []int64{}
	c.CurrentFileChunkRanges = []int64{}
	if errOpen == nil {
		stat, _ := c.CurrentFile.Stat()
		truncate = stat.Size() != c.FilesToTransfer[c.FilesToTransferCurrentNum].Size
		if !truncate {
			// recipient requests the file and chunks (if empty, then should receive all chunks)
			// TODO: determine the missing chunks
			c.CurrentFileChunkRanges = utils.MissingChunks(
				pathToFile,
				c.FilesToTransfer[c.FilesToTransferCurrentNum].Size,
				models.TCP_BUFFER_SIZE/2,
			)
		}
	} else {
		c.CurrentFile, errOpen = os.Create(pathToFile)
		if errOpen != nil {
			errOpen = fmt.Errorf("could not create %s: %w", pathToFile, errOpen)
			log.Error(errOpen)
			return errOpen
		}
		errChmod := os.Chmod(pathToFile, c.FilesToTransfer[c.FilesToTransferCurrentNum].Mode.Perm())
		if errChmod != nil {
			log.Error(errChmod)
		}
		truncate = true
	}
	if truncate {
		err := c.CurrentFile.Truncate(c.FilesToTransfer[c.FilesToTransferCurrentNum].Size)
		if err != nil {
			err = fmt.Errorf("could not truncate %s: %w", pathToFile, err)
			log.Error(err)
			return err
		}
	}
	return
}

func (c *Client) recipientGetFileReady(finished bool) (err error) {
	if finished {
		// TODO: do the last finishing stuff
		log.Debug("finished")
		err = message.Send(c.conn[0], c.Key, message.Message{
			Type: message.TypeFinished,
		})
		if err != nil {
			panic(err)
		}
		c.SuccessfulTransfer = true
		c.FilesHasFinished[c.FilesToTransferCurrentNum] = struct{}{}
		return
	}

	err = c.recipientInitializeFile()
	if err != nil {
		return
	}

	c.TotalSent = 0
	c.CurrentFileIsClosed = false
	machID, _ := machineid.ID()
	bRequest, _ := json.Marshal(RemoteFileRequest{
		CurrentFileChunkRanges:    c.CurrentFileChunkRanges,
		FilesToTransferCurrentNum: c.FilesToTransferCurrentNum,
		MachineID:                 machID,
	})
	log.Debug("converting to chunk range")
	c.CurrentFileChunks = utils.ChunkRangesToChunks(c.CurrentFileChunkRanges)

	if !finished {
		// setup the progressbar
		c.setBar()
	}

	log.Debugf("sending recipient ready with %d chunks", len(c.CurrentFileChunks))
	err = message.Send(c.conn[0], c.Key, message.Message{
		Type:  message.TypeRecipientReady,
		Bytes: bRequest,
	})
	if err != nil {
		return
	}
	c.Step3RecipientRequestFile = true
	return
}

func formatDescription(description string) string {
	const (
		// Reserve extra room for variable progress metadata such as [elapsed:remaining].
		progressMetaWidth = 78
		minDescription    = 12
		defaultTermWidth  = 80
	)

	width, _, err := term.GetSize(int(os.Stderr.Fd()))
	if err != nil || width <= 0 {
		width, _, err = term.GetSize(int(os.Stdout.Fd()))
	}
	if err != nil || width <= 0 {
		if envColumns, convErr := strconv.Atoi(os.Getenv("COLUMNS")); convErr == nil && envColumns > 0 {
			width = envColumns
		} else {
			width = defaultTermWidth
		}
	}

	maxDescription := width - progressMetaWidth
	if maxDescription < minDescription {
		maxDescription = minDescription
	}

	runes := []rune(description)
	if len(runes) > maxDescription {
		if maxDescription <= 3 {
			return string(runes[:maxDescription])
		}
		return string(runes[:maxDescription-3]) + "..."
	}
	return description
}

func (c *Client) createEmptyFileAndFinish(fileInfo FileInfo, i int) (err error) {
	log.Debugf("touching file with folder / name")
	if !utils.Exists(fileInfo.FolderRemote) {
		err = os.MkdirAll(fileInfo.FolderRemote, os.ModePerm)
		if err != nil {
			log.Error(err)
			return
		}
	}
	pathToFile := path.Join(fileInfo.FolderRemote, fileInfo.Name)
	if fileInfo.Symlink != "" {
		log.Debug("creating symlink")
		// remove symlink if it exists
		if _, errExists := os.Lstat(pathToFile); errExists == nil {
			os.Remove(pathToFile)
		}
		err = os.Symlink(fileInfo.Symlink, pathToFile)
		if err != nil {
			return
		}
	} else {
		emptyFile, errCreate := os.Create(pathToFile)
		if errCreate != nil {
			log.Error(errCreate)
			err = errCreate
			return
		}
		emptyFile.Close()
	}
	// setup the progressbar
	description := fmt.Sprintf("%-*s", c.longestFilename, c.FilesToTransfer[i].Name)
	if len(c.FilesToTransfer) == 1 {
		description = c.FilesToTransfer[i].Name
		// description = ""
	} else {
		description = " " + description
	}
	c.bar = progressbar.NewOptions64(1,
		progressbar.OptionOnCompletion(func() {
			c.fmtPrintUpdate()
		}),
		progressbar.OptionSetWidth(20),
		progressbar.OptionSetDescription(formatDescription(description)),
		progressbar.OptionSetRenderBlankState(true),
		progressbar.OptionShowBytes(true),
		progressbar.OptionShowCount(),
		progressbar.OptionSetWriter(os.Stderr),
		progressbar.OptionSetVisibility(!c.Options.SendingText),
	)
	c.bar.Finish()
	return
}

func (c *Client) updateIfRecipientHasFileInfo() (err error) {
	if c.Options.IsSender || !c.Step2FileInfoTransferred || c.Step3RecipientRequestFile {
		return
	}
	// find the next file to transfer and send that number
	// if the files are the same size, then look for missing chunks
	finished := true
	for i, fileInfo := range c.FilesToTransfer {
		if _, ok := c.FilesHasFinished[i]; ok {
			continue
		}
		if i < c.FilesToTransferCurrentNum {
			continue
		}
		log.Debugf("checking %+v", fileInfo)
		recipientFileInfo, errRecipientFile := os.Lstat(path.Join(fileInfo.FolderRemote, fileInfo.Name))
		var errHash error
		var fileHash []byte
		if errRecipientFile == nil && recipientFileInfo.Size() == fileInfo.Size {
			// the file exists, but is same size, so hash it
			fileHash, errHash = utils.HashFile(path.Join(fileInfo.FolderRemote, fileInfo.Name), c.Options.HashAlgorithm)
		}
		if fileInfo.Size == 0 || fileInfo.Symlink != "" {
			err = c.createEmptyFileAndFinish(fileInfo, i)
			if err != nil {
				return
			} else {
				c.numberOfTransferredFiles++
			}
			continue
		}
		log.Debugf("%s %+x %+x %+v", fileInfo.Name, fileHash, fileInfo.Hash, errHash)
		if !bytes.Equal(fileHash, fileInfo.Hash) {
			log.Debugf("hashed %s to %x using %s", fileInfo.Name, fileHash, c.Options.HashAlgorithm)
			log.Debugf("hashes are not equal %x != %x", fileHash, fileInfo.Hash)
			if errHash == nil && !c.Options.Overwrite && errRecipientFile == nil && !strings.HasPrefix(fileInfo.Name, "croc-stdin-") && !c.Options.SendingText {

				missingChunks := utils.ChunkRangesToChunks(utils.MissingChunks(
					path.Join(fileInfo.FolderRemote, fileInfo.Name),
					fileInfo.Size,
					models.TCP_BUFFER_SIZE/2,
				))
				percentDone := 100 - float64(len(missingChunks)*models.TCP_BUFFER_SIZE/2)/float64(fileInfo.Size)*100

				log.Debug("asking to overwrite")
				prompt := fmt.Sprintf("\nOverwrite '%s'? (y/N) (use --overwrite to omit) ", path.Join(fileInfo.FolderRemote, fileInfo.Name))
				if percentDone < 99 {
					prompt = fmt.Sprintf("\nResume '%s' (%2.1f%%)? (y/N)   (use --overwrite to omit) ", path.Join(fileInfo.FolderRemote, fileInfo.Name), percentDone)
				}
				choice := strings.ToLower(utils.GetInput(prompt))
				if choice != "y" && choice != "yes" {
					fmt.Fprintf(os.Stderr, "Skipping '%s'\n", path.Join(fileInfo.FolderRemote, fileInfo.Name))
					continue
				}
			}
		} else {
			log.Debugf("hashes are equal %x == %x", fileHash, fileInfo.Hash)

			if !fileInfo.ModTime.IsZero() {
				if err := os.Chtimes(path.Join(fileInfo.FolderRemote, fileInfo.Name), fileInfo.ModTime, fileInfo.ModTime); err != nil {
					log.Warnf("chtimes %v: %v", fileInfo.ModTime, err)
				} else {
					log.Debugf("chtimes %v", fileInfo.ModTime)
				}
			}
		}
		if errHash != nil {
			// probably can't find, its okay
			log.Debug(errHash)
		}
		if errHash != nil || !bytes.Equal(fileHash, fileInfo.Hash) {
			finished = false
			c.FilesToTransferCurrentNum = i
			c.numberOfTransferredFiles++
			newFolder, _ := filepath.Split(fileInfo.FolderRemote)
			if newFolder != c.LastFolder && len(c.FilesToTransfer) > 0 && !c.Options.SendingText && newFolder != "./" {
				fmt.Fprintf(os.Stderr, "\r%s\n", newFolder)
			}
			c.LastFolder = newFolder
			break
		}
	}
	c.recipientGetFileReady(finished)
	return
}

func (c *Client) fmtPrintUpdate() {
	c.finishedNum++
	if c.TotalNumberOfContents > 1 {
		fmt.Fprintf(os.Stderr, " %d/%d\n", c.finishedNum, c.TotalNumberOfContents)
	} else {
		fmt.Fprintf(os.Stderr, "\n")
	}
}

func (c *Client) updateState() (err error) {
	err = c.updateIfSenderChannelSecured()
	if err != nil {
		return
	}

	err = c.updateIfRecipientHasFileInfo()
	if err != nil {
		return
	}

	if c.Options.IsSender && c.Step3RecipientRequestFile && !c.Step4FileTransferred {
		log.Debug("start sending data!")

		if !c.firstSend {
			fmt.Fprintf(os.Stderr, "\nSending (->%s)\n", c.ExternalIPConnected)
			c.firstSend = true
			// if there are empty files, show them as already have been transferred now
			for i := range c.FilesToTransfer {
				if c.FilesToTransfer[i].Size == 0 {
					// setup the progressbar and takedown the progress bar for empty files
					description := fmt.Sprintf("%-*s", c.longestFilename, c.FilesToTransfer[i].Name)
					if len(c.FilesToTransfer) == 1 {
						description = c.FilesToTransfer[i].Name
						// description = ""
					}

					c.bar = progressbar.NewOptions64(1,
						progressbar.OptionOnCompletion(func() {
							c.fmtPrintUpdate()
						}),
						progressbar.OptionSetWidth(20),
						progressbar.OptionSetDescription(formatDescription(description)),
						progressbar.OptionSetRenderBlankState(true),
						progressbar.OptionShowBytes(true),
						progressbar.OptionShowCount(),
						progressbar.OptionSetWriter(os.Stderr),
						progressbar.OptionSetVisibility(!c.Options.SendingText),
					)
					c.bar.Finish()
				}
			}
		}
		c.Step4FileTransferred = true
		// setup the progressbar
		c.setBar()
		c.TotalSent = 0
		c.CurrentFileIsClosed = false
		log.Debug("beginning sending comms")
		pathToFile := path.Join(
			c.FilesToTransfer[c.FilesToTransferCurrentNum].FolderSource,
			c.FilesToTransfer[c.FilesToTransferCurrentNum].Name,
		)
		c.fread, err = os.Open(pathToFile)
		c.numfinished = 0
		if err != nil {
			return
		}
		for i := 0; i < len(c.Options.RelayPorts); i++ {
			log.Debugf("starting sending over comm %d", i)
			go c.sendData(i)
		}
	}
	return
}

func (c *Client) setBar() {
	description := fmt.Sprintf("%-*s", c.longestFilename, c.FilesToTransfer[c.FilesToTransferCurrentNum].Name)
	folder, _ := filepath.Split(c.FilesToTransfer[c.FilesToTransferCurrentNum].FolderRemote)
	if folder == "./" {
		description = c.FilesToTransfer[c.FilesToTransferCurrentNum].Name
	} else if !c.Options.IsSender {
		description = " " + description
	}
	c.bar = progressbar.NewOptions64(
		c.FilesToTransfer[c.FilesToTransferCurrentNum].Size,
		progressbar.OptionOnCompletion(func() {
			c.fmtPrintUpdate()
		}),
		progressbar.OptionSetWidth(20),
		progressbar.OptionSetDescription(formatDescription(description)),
		progressbar.OptionSetRenderBlankState(true),
		progressbar.OptionShowBytes(true),
		progressbar.OptionShowCount(),
		progressbar.OptionSetWriter(os.Stderr),
		progressbar.OptionThrottle(100*time.Millisecond),
		progressbar.OptionSetVisibility(!c.Options.SendingText),
	)
	byteToDo := int64(len(c.CurrentFileChunks) * models.TCP_BUFFER_SIZE / 2)
	if byteToDo > 0 {
		bytesDone := c.FilesToTransfer[c.FilesToTransferCurrentNum].Size - byteToDo
		log.Debug(byteToDo)
		log.Debug(c.FilesToTransfer[c.FilesToTransferCurrentNum].Size)
		log.Debug(bytesDone)
		if bytesDone > 0 {
			c.bar.Add64(bytesDone)
		}
	}
}

func (c *Client) receiveData(i int) {
	defer func() {
		if r := recover(); r != nil {
			if c.stop.gui {
				log.Errorf("panic: %v", r)
				c.stop.Cancel()
			} else {
				panic(r)
			}
		}
	}()
	log.Tracef("%d receiving data", i)
	for {
		data, err := c.conn[i+1].Receive()
		if err != nil {
			break
		}
		if bytes.Equal(data, []byte{1}) {
			log.Trace("got ping")
			continue
		}

		data, err = crypt.Decrypt(data, c.Key)
		if err != nil {
			panic(err)
		}
		if !c.Options.NoCompress {
			data = compress.Decompress(data)
		}

		// get position
		var position uint64
		rbuf := bytes.NewReader(data[:8])
		err = binary.Read(rbuf, binary.LittleEndian, &position)
		if err != nil {
			panic(err)
		}
		positionInt64 := int64(position)

		c.mutex.Lock()
		if c.CurrentFileIsClosed || c.CurrentFile == nil {
			c.mutex.Unlock()
			log.Tracef("was closed %d", i)
			return
		}
		if err := c.ctxErr(); err != nil {
			c.CurrentFileIsClosed = true
			defer c.mutex.Unlock()
			log.Tracef("stopping: %v", err)
			if err := c.CurrentFile.Close(); err != nil {
				log.Tracef("closing %s: %v", c.CurrentFile.Name(), err)
			} else {
				log.Tracef("Successful closing %s", c.CurrentFile.Name())
			}
			log.Tracef("sending close-sender")
			if sendErr := message.Send(c.conn[0], c.Key, message.Message{
				Type: message.TypeCloseSender,
			}); sendErr != nil {
				log.Tracef("sending close-sender: %v", sendErr)
			}
			return
		}
		_, err = c.CurrentFile.WriteAt(data[8:], positionInt64)
		if err != nil {
			panic(err)
		}
		c.bar.Add(len(data[8:]))
		c.TotalSent += int64(len(data[8:]))
		c.TotalChunksTransferred++
		// log.Debug(len(c.CurrentFileChunks), c.TotalChunksTransferred, c.TotalSent, c.FilesToTransfer[c.FilesToTransferCurrentNum].Size)

		if !c.CurrentFileIsClosed && (c.TotalChunksTransferred == len(c.CurrentFileChunks) || c.TotalSent == c.FilesToTransfer[c.FilesToTransferCurrentNum].Size) {
			c.CurrentFileIsClosed = true
			log.Debug("finished receiving!")
			if err = c.CurrentFile.Close(); err != nil {
				log.Debugf("error closing %s: %v", c.CurrentFile.Name(), err)
			} else {
				log.Debugf("Successful closing %s", c.CurrentFile.Name())
			}
			if c.Options.Stdout || c.Options.SendingText {
				pathToFile := path.Join(
					c.FilesToTransfer[c.FilesToTransferCurrentNum].FolderRemote,
					c.FilesToTransfer[c.FilesToTransferCurrentNum].Name,
				)
				b, _ := os.ReadFile(pathToFile)
				fmt.Print(string(b))
			}
			log.Debug("sending close-sender")
			err = message.Send(c.conn[0], c.Key, message.Message{
				Type: message.TypeCloseSender,
			})
			if err != nil {
				panic(err)
			}
		}
		c.mutex.Unlock()
	}
}

func (c *Client) sendData(i int) {
	defer func() {
		if r := recover(); r != nil {
			if c.stop.gui {
				log.Errorf("panic: %v", r)
				c.stop.Cancel()
			} else {
				panic(r)
			}
		}
		log.Debugf("finished with %d", i)
		c.numfinished++
		if c.numfinished == len(c.Options.RelayPorts) {
			log.Debug("closing file")
			if err := c.fread.Close(); err != nil {
				log.Errorf("error closing file: %v", err)
			}
		}
	}()

	var readingPos int64
	pos := uint64(0)
	curi := float64(0)
	for {
		if err := c.ctxErr(); err != nil {
			log.Tracef("stopping send %d: %v", i, err)
			return
		}
		// Read file
		var n int
		var errRead error
		if math.Mod(curi, float64(len(c.Options.RelayPorts))) == float64(i) {
			data := make([]byte, models.TCP_BUFFER_SIZE/2)
			n, errRead = c.fread.ReadAt(data, readingPos)
			if c.limiter != nil {
				r := c.limiter.ReserveN(time.Now(), n)
				log.Debugf("Limiting Upload for %d", r.Delay())
				time.Sleep(r.Delay())
			}
			if n > 0 {
				// check to see if this is a chunk that the recipient wants
				usableChunk := true
				c.mutex.Lock()
				if len(c.chunkMap) != 0 {
					if _, ok := c.chunkMap[pos]; !ok {
						usableChunk = false
					} else {
						delete(c.chunkMap, pos)
					}
				}
				c.mutex.Unlock()
				if usableChunk {
					// log.Debugf("sending chunk %d", pos)
					posByte := make([]byte, 8)
					binary.LittleEndian.PutUint64(posByte, pos)
					var err error
					var dataToSend []byte
					if c.Options.NoCompress {
						dataToSend, err = crypt.Encrypt(
							append(posByte, data[:n]...),
							c.Key,
						)
					} else {
						dataToSend, err = crypt.Encrypt(
							compress.Compress(
								append(posByte, data[:n]...),
							),
							c.Key,
						)
					}
					if err != nil {
						panic(err)
					}

					err = c.conn[i+1].Send(dataToSend)
					if err != nil {
						panic(err)
					}
					c.bar.Add(n)
					c.TotalSent += int64(n)
					// time.Sleep(100 * time.Millisecond)
				}
			}
		}

		if n == 0 {
			n = models.TCP_BUFFER_SIZE / 2
		}
		readingPos += int64(n)
		curi++
		pos += uint64(n)

		if errRead != nil {
			if errRead == io.EOF {
				break
			}
			panic(errRead)
		}
	}
}

// isExecutableInPath checks for the availability of an executable
func isExecutableInPath(executableName string) bool {
	_, err := exec.LookPath(executableName)
	return err == nil
}

// copyToClipboard tries to send the code to the operating system clipboard
func copyToClipboard(str string, quiet bool, extendedClipboard bool) {
	var cmd *exec.Cmd
	switch runtime.GOOS {
	// Windows should always have clip.exe in PATH by default
	case "windows":
		cmd = exec.Command("clip")
	// MacOS uses pbcopy
	case "darwin":
		cmd = exec.Command("pbcopy")
	// These Unix-like systems are likely using Xorg(with xclip or xsel) or Wayland(with wl-copy or waycopy)
	case "linux", "android", "hurd", "freebsd", "openbsd", "netbsd", "dragonfly", "solaris", "illumos", "plan9":
		if os.Getenv("XDG_SESSION_TYPE") == "wayland" { // Wayland running
			if isExecutableInPath("wl-copy") {
				cmd = exec.Command("wl-copy")
			} else if isExecutableInPath("waycopy") {
				cmd = exec.Command("waycopy")
			}
		} else if os.Getenv("XDG_SESSION_TYPE") == "x11" || os.Getenv("XDG_SESSION_TYPE") == "xorg" { // Xorg running
			if isExecutableInPath("xclip") {
				cmd = exec.Command("xclip", "-selection", "clipboard")
			}
		} else if isExecutableInPath("xsel") {
			cmd = exec.Command("xsel", "-b")
		} else if isExecutableInPath("termux-clipboard-set") {
			cmd = exec.Command("termux-clipboard-set")
		}
	default:
		return
	}
	// Nothing has been found
	if cmd == nil {
		return
	}
	// Sending stdin into the available clipboard program
	cmd.Stdin = bytes.NewReader([]byte(str))
	if err := cmd.Run(); err != nil {
		log.Debugf("error copying to clipboard: %v", err)
		return
	}
	if !quiet {
		if extendedClipboard {
			fmt.Fprintf(os.Stderr, "Command copied to clipboard!\n")
		} else {
			fmt.Fprintf(os.Stderr, "Code copied to clipboard!\n")
		}
	}
}
```

## File: `src/croc/croc_test.go`
```go
package croc

import (
	"context"
	"fmt"
	"math/rand"
	"os"
	"path"
	"path/filepath"
	"runtime"
	"strings"
	"sync"
	"testing"
	"time"

	"github.com/schollz/croc/v10/src/tcp"
	log "github.com/schollz/logger"
	"github.com/stretchr/testify/assert"
)

func init() {
	log.SetLevel("trace")

	go tcp.Run("debug", "127.0.0.1", "8281", "pass123", "8282,8283,8284,8285")
	go tcp.Run("debug", "127.0.0.1", "8282", "pass123")
	go tcp.Run("debug", "127.0.0.1", "8283", "pass123")
	go tcp.Run("debug", "127.0.0.1", "8284", "pass123")
	go tcp.Run("debug", "127.0.0.1", "8285", "pass123")
	time.Sleep(1 * time.Second)
}

func TestCrocReadme(t *testing.T) {
	defer os.Remove("README.md")

	log.Debug("setting up sender")
	sender, err := New(Options{
		IsSender:      true,
		SharedSecret:  "8123-testingthecroc",
		Debug:         true,
		RelayAddress:  "127.0.0.1:8281",
		RelayPorts:    []string{"8281"},
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
		GitIgnore:     false,
	})
	if err != nil {
		panic(err)
	}

	log.Debug("setting up receiver")
	receiver, err := New(Options{
		IsSender:      false,
		SharedSecret:  "8123-testingthecroc",
		Debug:         true,
		RelayAddress:  "127.0.0.1:8281",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
	})
	if err != nil {
		panic(err)
	}

	var wg sync.WaitGroup
	wg.Add(2)
	go func() {
		filesInfo, emptyFolders, totalNumberFolders, errGet := GetFilesInfo([]string{"../../README.md"}, false, false, []string{})
		if errGet != nil {
			t.Errorf("failed to get minimal info: %v", errGet)
		}
		err := sender.Send(filesInfo, emptyFolders, totalNumberFolders)
		if err != nil {
			t.Errorf("send failed: %v", err)
		}
		wg.Done()
	}()
	time.Sleep(100 * time.Millisecond)
	go func() {
		err := receiver.Receive()
		if err != nil {
			t.Errorf("receive failed: %v", err)
		}
		wg.Done()
	}()

	wg.Wait()
}

func TestCrocEmptyFolder(t *testing.T) {
	pathName := "../../testEmpty"
	defer os.RemoveAll(pathName)
	defer os.RemoveAll("./testEmpty")
	os.MkdirAll(pathName, 0o755)

	log.Debug("setting up sender")
	sender, err := New(Options{
		IsSender:      true,
		SharedSecret:  "8123-testingthecroc",
		Debug:         true,
		RelayAddress:  "127.0.0.1:8281",
		RelayPorts:    []string{"8281"},
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
	})
	if err != nil {
		panic(err)
	}

	log.Debug("setting up receiver")
	receiver, err := New(Options{
		IsSender:      false,
		SharedSecret:  "8123-testingthecroc",
		Debug:         true,
		RelayAddress:  "127.0.0.1:8281",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
	})
	if err != nil {
		panic(err)
	}

	var wg sync.WaitGroup
	wg.Add(2)
	go func() {
		filesInfo, emptyFolders, totalNumberFolders, errGet := GetFilesInfo([]string{pathName}, false, false, []string{})
		if errGet != nil {
			t.Errorf("failed to get minimal info: %v", errGet)
		}
		err := sender.Send(filesInfo, emptyFolders, totalNumberFolders)
		if err != nil {
			t.Errorf("send failed: %v", err)
		}
		wg.Done()
	}()
	time.Sleep(100 * time.Millisecond)
	go func() {
		err := receiver.Receive()
		if err != nil {
			t.Errorf("receive failed: %v", err)
		}
		wg.Done()
	}()

	wg.Wait()
}

func TestCrocSymlink(t *testing.T) {
	pathName := "../link-in-folder"
	defer os.RemoveAll(pathName)
	defer os.RemoveAll("./link-in-folder")
	os.MkdirAll(pathName, 0o755)
	os.Symlink("../../README.md", filepath.Join(pathName, "README.link"))

	log.Debug("setting up sender")
	sender, err := New(Options{
		IsSender:      true,
		SharedSecret:  "8124-testingthecroc",
		Debug:         true,
		RelayAddress:  "127.0.0.1:8281",
		RelayPorts:    []string{"8281"},
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
		GitIgnore:     false,
	})
	if err != nil {
		panic(err)
	}

	log.Debug("setting up receiver")
	receiver, err := New(Options{
		IsSender:      false,
		SharedSecret:  "8124-testingthecroc",
		Debug:         true,
		RelayAddress:  "127.0.0.1:8281",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
	})
	if err != nil {
		panic(err)
	}

	var wg sync.WaitGroup
	wg.Add(2)
	go func() {
		filesInfo, emptyFolders, totalNumberFolders, errGet := GetFilesInfo([]string{pathName}, false, false, []string{})
		if errGet != nil {
			t.Errorf("failed to get minimal info: %v", errGet)
		}
		err = sender.Send(filesInfo, emptyFolders, totalNumberFolders)
		if err != nil {
			t.Errorf("send failed: %v", err)
		}
		wg.Done()
	}()
	time.Sleep(100 * time.Millisecond)
	go func() {
		err = receiver.Receive()
		if err != nil {
			t.Errorf("receive failed: %v", err)
		}
		wg.Done()
	}()

	wg.Wait()

	s, err := filepath.EvalSymlinks(path.Join(pathName, "README.link"))
	if s != "../../README.md" && s != "..\\..\\README.md" {
		log.Debug(s)
		t.Errorf("symlink failed to transfer in folder")
	}
	if err != nil {
		t.Errorf("symlink transfer failed: %s", err.Error())
	}
}
func TestCrocIgnoreGit(t *testing.T) {
	log.SetLevel("trace")
	defer os.Remove(".gitignore")
	time.Sleep(300 * time.Millisecond)

	time.Sleep(1 * time.Second)
	file, err := os.Create(".gitignore")
	if err != nil {
		log.Errorf("error creating file")
	}
	_, err = file.WriteString("LICENSE")
	if err != nil {
		log.Errorf("error writing to file")
	}
	time.Sleep(1 * time.Second)
	// due to how files are ignored in this function, all we have to do to test is make sure LICENSE doesn't get included in FilesInfo.
	filesInfo, _, _, errGet := GetFilesInfo([]string{"../../LICENSE", ".gitignore", "croc.go"}, false, true, []string{})
	if errGet != nil {
		t.Errorf("failed to get minimal info: %v", errGet)
	}
	for _, file := range filesInfo {
		if strings.Contains(file.Name, "LICENSE") {
			t.Errorf("test failed, should ignore LICENSE")
		}
	}
}

func TestCrocLocal(t *testing.T) {
	log.SetLevel("trace")
	defer os.Remove("LICENSE")
	defer os.Remove("touched")
	time.Sleep(300 * time.Millisecond)

	log.Debug("setting up sender")
	sender, err := New(Options{
		IsSender:      true,
		SharedSecret:  "8123-testingthecroc",
		Debug:         true,
		RelayAddress:  "127.0.0.1:8181",
		RelayPorts:    []string{"8181", "8182"},
		RelayPassword: "pass123",
		Stdout:        true,
		NoPrompt:      true,
		DisableLocal:  false,
		Curve:         "ed25519",
		Overwrite:     true,
		GitIgnore:     false,
	})
	if err != nil {
		panic(err)
	}
	time.Sleep(1 * time.Second)

	log.Debug("setting up receiver")
	receiver, err := New(Options{
		IsSender:      false,
		SharedSecret:  "8123-testingthecroc",
		Debug:         true,
		RelayAddress:  "127.0.0.1:8181",
		RelayPassword: "pass123",
		Stdout:        true,
		NoPrompt:      true,
		DisableLocal:  false,
		Curve:         "ed25519",
		Overwrite:     true,
	})
	if err != nil {
		panic(err)
	}

	var wg sync.WaitGroup
	os.Create("touched")
	wg.Add(2)
	go func() {
		filesInfo, emptyFolders, totalNumberFolders, errGet := GetFilesInfo([]string{"../../LICENSE", "touched"}, false, false, []string{})
		if errGet != nil {
			t.Errorf("failed to get minimal info: %v", errGet)
		}
		err := sender.Send(filesInfo, emptyFolders, totalNumberFolders)
		if err != nil {
			t.Errorf("send failed: %v", err)
		}
		wg.Done()
	}()
	time.Sleep(100 * time.Millisecond)
	go func() {
		err := receiver.Receive()
		if err != nil {
			t.Errorf("send failed: %v", err)
		}
		wg.Done()
	}()

	wg.Wait()
}

func TestCrocError(t *testing.T) {
	content := []byte("temporary file's content")
	tmpfile, err := os.CreateTemp("", "example")
	if err != nil {
		panic(err)
	}

	defer os.Remove(tmpfile.Name()) // clean up

	if _, err = tmpfile.Write(content); err != nil {
		panic(err)
	}
	if err = tmpfile.Close(); err != nil {
		panic(err)
	}

	Debug(false)
	log.SetLevel("warn")
	sender, _ := New(Options{
		IsSender:      true,
		SharedSecret:  "8123-testingthecroc2",
		Debug:         true,
		RelayAddress:  "doesntexistok.com:8381",
		RelayPorts:    []string{"8381", "8382"},
		RelayPassword: "pass123",
		Stdout:        true,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
	})
	filesInfo, emptyFolders, totalNumberFolders, errGet := GetFilesInfo([]string{tmpfile.Name()}, false, false, []string{})
	if errGet != nil {
		t.Errorf("failed to get minimal info: %v", errGet)
	}
	err = sender.Send(filesInfo, emptyFolders, totalNumberFolders)
	log.Debug(err)
	assert.NotNil(t, err)
}

func TestReceiverStdoutWithInvalidSecret(t *testing.T) {
	// Test for issue: panic when receiving with --stdout and invalid CROC_SECRET
	// This should fail gracefully without panicking
	log.SetLevel("warn")
	receiver, err := New(Options{
		IsSender:      false,
		SharedSecret:  "invalid-secret-12345",
		Debug:         true,
		RelayAddress:  "127.0.0.1:8281",
		RelayPassword: "pass123",
		Stdout:        true, // This is the key flag that triggered the panic
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
	})
	if err != nil {
		t.Errorf("failed to create receiver: %v", err)
		return
	}

	// This should fail but not panic
	err = receiver.Receive()
	// We expect an error since the secret is invalid and no sender is present
	assert.NotNil(t, err)
	log.Debugf("Expected error occurred: %v", err)
}

func TestCleanUp(t *testing.T) {
	// windows allows files to be deleted only if they
	// are not open by another program so the remove actions
	// from the above tests will not always do a good clean up
	// This "test" will make sure
	operatingSystem := runtime.GOOS
	log.Debugf("The operating system is %s", operatingSystem)
	if operatingSystem == "windows" {
		time.Sleep(1 * time.Second)
		log.Debug("Full cleanup")
		var err error

		for _, file := range []string{"README.md", "./README.md"} {
			err = os.Remove(file)
			if err == nil {
				log.Debugf("Successfully purged %s", file)
			} else {
				log.Debugf("%s was already purged.", file)
			}
		}
		for _, folder := range []string{"./testEmpty", "./link-in-folder"} {
			err = os.RemoveAll(folder)
			if err == nil {
				log.Debugf("Successfully purged %s", folder)
			} else {
				log.Debugf("%s was already purged.", folder)
			}
		}
	}
}

func hashed(c *Client) bool {
	if len(c.FilesToTransfer) == 0 {
		return false
	}
	for _, file := range c.FilesToTransfer {
		if len(file.Hash) == 0 {
			return false
		}
	}
	return true
}

func waitHashed(sender *Client) (err error) {
	err = fmt.Errorf("not hashed")
	for i := 0; i < 300; i++ { // Max 3 seconds
		if hashed(sender) {
			time.Sleep(100 * time.Millisecond)
			return nil
		}
		time.Sleep(10 * time.Millisecond)
	}
	return
}

func createTestFile(t *testing.T, size int) (string, func()) {
	tempFile, err := os.CreateTemp("", "test-*.dat")
	if err != nil {
		t.Fatal(err)
	}

	data := make([]byte, size)
	for i := 0; i < size; i++ {
		data[i] = byte(i % 256)
	}

	if _, err := tempFile.Write(data); err != nil {
		tempFile.Close()
		os.Remove(tempFile.Name())
		t.Fatal(err)
	}

	if err := tempFile.Close(); err != nil {
		os.Remove(tempFile.Name())
		t.Fatal(err)
	}

	return tempFile.Name(), func() {
		os.Remove(tempFile.Name())
	}
}

func TestBase(t *testing.T) {
	tempFile, cleanup := createTestFile(t, 1024*1024) // 1 МБ
	defer cleanup()
	receivedFile := filepath.Base(tempFile)
	defer os.Remove(receivedFile)

	go tcp.Run("debug", "127.0.0.1", "8286", "pass123", "8287")
	time.Sleep(200 * time.Millisecond)
	go tcp.Run("debug", "127.0.0.1", "8287", "pass123")
	time.Sleep(200 * time.Millisecond)

	uniqueSecret := fmt.Sprintf("test-%d-%d", time.Now().UnixNano(), rand.Intn(10000))

	sender, err := New(Options{
		IsSender:      true,
		SharedSecret:  uniqueSecret,
		Debug:         true,
		RelayAddress:  "127.0.0.1:8286",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
		GitIgnore:     false,
	})
	if err != nil {
		t.Fatalf("Create sender failed: %v", err)
	}

	filesInfo, emptyFolders, totalNumberFolders, errGet := GetFilesInfo([]string{tempFile}, false, false, []string{})
	if errGet != nil {
		t.Fatalf("Get file info failed: %v", errGet)
	}

	receiver, err := New(Options{
		IsSender:      false,
		SharedSecret:  uniqueSecret,
		Debug:         true,
		RelayAddress:  "127.0.0.1:8286",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
	})
	if err != nil {
		t.Fatalf("Create receiver failed: %v", err)
	}

	fatalErr := make(chan error, 1)

	failTest := func(err error) {
		select {
		case fatalErr <- err:
		default:
		}
	}

	var wg sync.WaitGroup
	wg.Add(2)

	go func() {
		defer wg.Done()
		log.Warn("Send")
		if err := sender.Send(filesInfo, emptyFolders, totalNumberFolders); err != nil {
			failTest(fmt.Errorf("Send failed: %w", err))
		}
	}()

	go func() {
		defer wg.Done()

		if err := waitHashed(sender); err != nil {
			failTest(fmt.Errorf("waitHashed failed: %w", err))
			return
		}

		log.Warn("Receive")
		if err := receiver.Receive(); err != nil {
			failTest(fmt.Errorf("Receive failed: %w", err))
		}
	}()

	go func() {
		for i := 0; i < 3000; i++ {
			if sender.Step1ChannelSecured && receiver.Step1ChannelSecured {
				time.Sleep(time.Millisecond)
				if sender.Step2FileInfoTransferred && receiver.Step2FileInfoTransferred {
					log.Warn("Step2FileInfoTransferred reached")
					return
				}
				log.Warn("Step1ChannelSecured reached")
			}
			time.Sleep(time.Millisecond)
		}
	}()

	done := make(chan bool, 1)
	go func() {
		wg.Wait()
		done <- true
	}()

	select {
	case err := <-fatalErr:
		t.Fatal(err)
	case <-done:
	case <-time.After(5 * time.Second):
		t.Fatal("Test timeout after 5 seconds")
	}
}

func TestCtx(t *testing.T) {
	tempFile, cleanup := createTestFile(t, 1024*1024) // 1 МБ
	defer cleanup()
	receivedFile := filepath.Base(tempFile)
	defer os.Remove(receivedFile)

	ctx, cancel := context.WithTimeout(context.Background(), 4*time.Second)
	defer cancel()

	go tcp.RunCtx(ctx, "debug", "127.0.0.1", "8288", "pass123", "8289")
	time.Sleep(200 * time.Millisecond)
	go tcp.RunCtx(ctx, "debug", "127.0.0.1", "8289", "pass123")
	time.Sleep(200 * time.Millisecond)

	uniqueSecret := fmt.Sprintf("test-%d-%d", time.Now().UnixNano(), rand.Intn(10000))

	sender, err := NewCtx(ctx, Options{
		IsSender:      true,
		SharedSecret:  uniqueSecret,
		Debug:         true,
		RelayAddress:  "127.0.0.1:8288",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
		GitIgnore:     false,
	})
	if err != nil {
		t.Fatalf("Create sender failed: %v", err)
	}

	filesInfo, emptyFolders, totalNumberFolders, errGet := GetFilesInfo([]string{tempFile}, false, false, []string{})
	if errGet != nil {
		t.Fatalf("Get file info failed: %v", errGet)
	}

	receiver, err := NewCtx(ctx, Options{
		IsSender:      false,
		SharedSecret:  uniqueSecret,
		Debug:         true,
		RelayAddress:  "127.0.0.1:8288",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
	})
	if err != nil {
		t.Fatalf("Create receiver failed: %v", err)
	}

	fatalErr := make(chan error, 1)

	failTest := func(err error) {
		select {
		case fatalErr <- err:
		default:
		}
	}

	var wg sync.WaitGroup
	wg.Add(2)

	go func() {
		defer wg.Done()
		log.Warn("Send")
		if err := sender.Send(filesInfo, emptyFolders, totalNumberFolders); err != nil {
			failTest(fmt.Errorf("Send failed: %w", err))
		}
	}()

	go func() {
		defer wg.Done()

		if err := waitHashed(sender); err != nil {
			failTest(fmt.Errorf("waitHashed failed: %w", err))
			return
		}

		log.Warn("Receive")
		if err := receiver.Receive(); err != nil {
			failTest(fmt.Errorf("Receive failed: %w", err))
		}
	}()

	go func() {
		for i := 0; i < 3000; i++ {
			if sender.Step1ChannelSecured && receiver.Step1ChannelSecured {
				time.Sleep(time.Millisecond)
				if sender.Step2FileInfoTransferred && receiver.Step2FileInfoTransferred {
					log.Warn("Step2FileInfoTransferred reached")
					return
				}
				log.Warn("Step1ChannelSecured reached")
			}
			time.Sleep(time.Millisecond)
		}
	}()

	done := make(chan bool, 1)
	go func() {
		wg.Wait()
		done <- true
	}()

	select {
	case err := <-fatalErr:
		t.Fatal(err)
	case <-done:
	case <-time.After(5 * time.Second):
		t.Fatal("Test timeout after 5 seconds")
	}
}

func validErrors(err error) bool {
	s := err.Error()
	return strings.Contains(s, "cancel") ||
		strings.Contains(s, "context") ||
		strings.Contains(s, "reset") ||
		strings.Contains(s, "broken") ||
		strings.Contains(s, "refusing") ||
		strings.Contains(s, "EOF") ||
		strings.Contains(s, "closed")
}

func result(t *testing.T, err error) {
	if err != nil {
		if validErrors(err) {
			t.Logf("Expected error during context cancellation: %v", err)
		} else {
			t.Errorf("Unexpected error during cancellation: %v", err)
		}
		return
	}
	t.Error("Transfer should have been interrupted by context cancellation")
}

func TestAllCtx(t *testing.T) {
	tempFile, cleanup := createTestFile(t, 1024*1024) // 1 МБ
	defer cleanup()
	receivedFile := filepath.Base(tempFile)
	defer os.Remove(receivedFile)

	ctx, cancel := context.WithTimeout(context.Background(), 4*time.Second)
	defer cancel()

	go tcp.RunCtx(ctx, "debug", "127.0.0.1", "8290", "pass123", "8291")
	time.Sleep(200 * time.Millisecond)
	go tcp.RunCtx(ctx, "debug", "127.0.0.1", "8291", "pass123")
	time.Sleep(200 * time.Millisecond)

	uniqueSecret := fmt.Sprintf("test-%d-%d", time.Now().UnixNano(), rand.Intn(10000))

	sender, err := NewCtx(ctx, Options{
		IsSender:      true,
		SharedSecret:  uniqueSecret,
		Debug:         true,
		RelayAddress:  "127.0.0.1:8290",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
		GitIgnore:     false,
	})
	if err != nil {
		t.Fatalf("Create sender failed: %v", err)
	}

	filesInfo, emptyFolders, totalNumberFolders, errGet := GetFilesInfo([]string{tempFile}, false, false, []string{})
	if errGet != nil {
		t.Fatalf("Get file info failed: %v", errGet)
	}

	receiver, err := NewCtx(ctx, Options{
		IsSender:      false,
		SharedSecret:  uniqueSecret,
		Debug:         true,
		RelayAddress:  "127.0.0.1:8290",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
	})
	if err != nil {
		t.Fatalf("Create receiver failed: %v", err)
	}

	fatalErr := make(chan error, 1)

	failTest := func(err error) {
		select {
		case fatalErr <- err:
		default:
		}
	}

	var wg sync.WaitGroup
	wg.Add(2)

	go func() {
		defer wg.Done()
		log.Warn("Send")
		if err := sender.Send(filesInfo, emptyFolders, totalNumberFolders); err != nil {
			failTest(fmt.Errorf("Send failed: %w", err))
		}
	}()

	go func() {
		defer wg.Done()

		if err := waitHashed(sender); err != nil {
			failTest(fmt.Errorf("waitHashed failed: %w", err))
			return
		}

		log.Warn("Receive")
		if err := receiver.Receive(); err != nil {
			failTest(fmt.Errorf("Receive failed: %w", err))
		}
	}()

	go func() {
		for i := 0; i < 3000; i++ {
			if sender.Step1ChannelSecured && receiver.Step1ChannelSecured {
				time.Sleep(time.Millisecond)
				if sender.Step2FileInfoTransferred && receiver.Step2FileInfoTransferred {
					log.Warn("Step2FileInfoTransferred reached")
					cancel()
					return
				}
				log.Warn("Step1ChannelSecured reached")
			}
			time.Sleep(time.Millisecond)
		}
	}()

	done := make(chan bool, 1)
	go func() {
		wg.Wait()
		done <- true
	}()

	select {
	case err := <-fatalErr:
		result(t, err)
	case <-done:
		t.Error("Transfer should have been interrupted by context cancellation")
	case <-time.After(5 * time.Second):
		t.Fatal("Test timeout after 5 seconds")
	}
}

func TestSendCtx(t *testing.T) {
	tempFile, cleanup := createTestFile(t, 1024*1024) // 1 МБ
	defer cleanup()
	receivedFile := filepath.Base(tempFile)
	defer os.Remove(receivedFile)

	ctx, cancel := context.WithTimeout(context.Background(), 4*time.Second)
	defer cancel()

	ctx2, cancel2 := context.WithCancel(context.Background())
	defer cancel2()

	go tcp.RunCtx(ctx, "debug", "127.0.0.1", "8292", "pass123", "8293")
	time.Sleep(200 * time.Millisecond)
	go tcp.RunCtx(ctx, "debug", "127.0.0.1", "8293", "pass123")
	time.Sleep(200 * time.Millisecond)

	uniqueSecret := fmt.Sprintf("test-%d-%d", time.Now().UnixNano(), rand.Intn(10000))

	sender, err := NewCtx(ctx2, Options{
		IsSender:      true,
		SharedSecret:  uniqueSecret,
		Debug:         true,
		RelayAddress:  "127.0.0.1:8292",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
		GitIgnore:     false,
	})
	if err != nil {
		t.Fatalf("Create sender failed: %v", err)
	}

	filesInfo, emptyFolders, totalNumberFolders, errGet := GetFilesInfo([]string{tempFile}, false, false, []string{})
	if errGet != nil {
		t.Fatalf("Get file info failed: %v", errGet)
	}

	receiver, err := NewCtx(ctx, Options{
		IsSender:      false,
		SharedSecret:  uniqueSecret,
		Debug:         true,
		RelayAddress:  "127.0.0.1:8292",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
	})
	if err != nil {
		t.Fatalf("Create receiver failed: %v", err)
	}

	fatalErr := make(chan error, 1)

	failTest := func(err error) {
		select {
		case fatalErr <- err:
		default:
		}
	}

	var wg sync.WaitGroup
	wg.Add(2)

	go func() {
		defer wg.Done()
		log.Warn("Send")
		if err := sender.Send(filesInfo, emptyFolders, totalNumberFolders); err != nil {
			failTest(fmt.Errorf("Send failed: %w", err))
		}
	}()

	go func() {
		defer wg.Done()

		if err := waitHashed(sender); err != nil {
			failTest(fmt.Errorf("waitHashed failed: %w", err))
			return
		}

		log.Warn("Receive")
		if err := receiver.Receive(); err != nil {
			failTest(fmt.Errorf("Receive failed: %w", err))
		}
	}()

	go func() {
		for i := 0; i < 3000; i++ {
			if sender.Step1ChannelSecured && receiver.Step1ChannelSecured {
				time.Sleep(time.Millisecond)
				if sender.Step2FileInfoTransferred && receiver.Step2FileInfoTransferred {
					log.Warn("Step2FileInfoTransferred reached")
					cancel2()
					return
				}
				log.Warn("Step1ChannelSecured reached")
			}
			time.Sleep(time.Millisecond)
		}
	}()

	done := make(chan bool, 1)
	go func() {
		wg.Wait()
		done <- true
	}()

	select {
	case err := <-fatalErr:
		result(t, err)
	case <-done:
		t.Error("Transfer should have been interrupted by context cancellation")
	case <-time.After(5 * time.Second):
		t.Fatal("Test timeout after 5 seconds")
	}
}

func TestReceiveCtx(t *testing.T) {
	tempFile, cleanup := createTestFile(t, 1024*1024) // 1 МБ
	defer cleanup()
	receivedFile := filepath.Base(tempFile)
	defer os.Remove(receivedFile)

	ctx, cancel := context.WithTimeout(context.Background(), 4*time.Second)
	defer cancel()

	ctx2, cancel2 := context.WithCancel(context.Background())
	defer cancel2()

	go tcp.RunCtx(ctx, "debug", "127.0.0.1", "8294", "pass123", "8295")
	time.Sleep(200 * time.Millisecond)
	go tcp.RunCtx(ctx, "debug", "127.0.0.1", "8295", "pass123")
	time.Sleep(200 * time.Millisecond)

	uniqueSecret := fmt.Sprintf("test-%d-%d", time.Now().UnixNano(), rand.Intn(10000))

	sender, err := NewCtx(ctx, Options{
		IsSender:      true,
		SharedSecret:  uniqueSecret,
		Debug:         true,
		RelayAddress:  "127.0.0.1:8294",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
		GitIgnore:     false,
	})
	if err != nil {
		t.Fatalf("Create sender failed: %v", err)
	}

	filesInfo, emptyFolders, totalNumberFolders, errGet := GetFilesInfo([]string{tempFile}, false, false, []string{})
	if errGet != nil {
		t.Fatalf("Get file info failed: %v", errGet)
	}

	receiver, err := NewCtx(ctx2, Options{
		IsSender:      false,
		SharedSecret:  uniqueSecret,
		Debug:         true,
		RelayAddress:  "127.0.0.1:8294",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
	})
	if err != nil {
		t.Fatalf("Create receiver failed: %v", err)
	}

	fatalErr := make(chan error, 1)

	failTest := func(err error) {
		select {
		case fatalErr <- err:
		default:
		}
	}

	var wg sync.WaitGroup
	wg.Add(2)

	go func() {
		defer wg.Done()
		log.Warn("Send")
		if err := sender.Send(filesInfo, emptyFolders, totalNumberFolders); err != nil {
			failTest(fmt.Errorf("Send failed: %w", err))
		}
	}()

	go func() {
		defer wg.Done()

		if err := waitHashed(sender); err != nil {
			failTest(fmt.Errorf("waitHashed failed: %w", err))
			return
		}

		log.Warn("Receive")
		if err := receiver.Receive(); err != nil {
			failTest(fmt.Errorf("Receive failed: %w", err))
		}
	}()

	go func() {
		for i := 0; i < 3000; i++ {
			if sender.Step1ChannelSecured && receiver.Step1ChannelSecured {
				time.Sleep(time.Millisecond)
				if sender.Step2FileInfoTransferred && receiver.Step2FileInfoTransferred {
					log.Warn("Step2FileInfoTransferred reached")
					cancel2()
					return
				}
				log.Warn("Step1ChannelSecured reached")
			}
			time.Sleep(time.Millisecond)
		}
	}()

	done := make(chan bool, 1)
	go func() {
		wg.Wait()
		done <- true
	}()

	select {
	case err := <-fatalErr:
		result(t, err)
	case <-done:
		t.Error("Transfer should have been interrupted by context cancellation")
	case <-time.After(5 * time.Second):
		t.Fatal("Test timeout after 5 seconds")
	}
}

func TestRunCtx(t *testing.T) {
	tempFile, cleanup := createTestFile(t, 1024*1024) // 1 МБ
	defer cleanup()
	receivedFile := filepath.Base(tempFile)
	defer os.Remove(receivedFile)

	ctx, cancel := context.WithTimeout(context.Background(), 4*time.Second)
	defer cancel()

	ctx2, cancel2 := context.WithCancel(context.Background())
	defer cancel2()

	go tcp.RunCtx(ctx2, "debug", "127.0.0.1", "8296", "pass123", "8297")
	time.Sleep(200 * time.Millisecond)
	go tcp.RunCtx(ctx2, "debug", "127.0.0.1", "8297", "pass123")
	time.Sleep(200 * time.Millisecond)

	uniqueSecret := fmt.Sprintf("test-%d-%d", time.Now().UnixNano(), rand.Intn(10000))

	sender, err := NewCtx(ctx, Options{
		IsSender:      true,
		SharedSecret:  uniqueSecret,
		Debug:         true,
		RelayAddress:  "127.0.0.1:8296",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
		GitIgnore:     false,
	})
	if err != nil {
		t.Fatalf("Create sender failed: %v", err)
	}

	filesInfo, emptyFolders, totalNumberFolders, errGet := GetFilesInfo([]string{tempFile}, false, false, []string{})
	if errGet != nil {
		t.Fatalf("Get file info failed: %v", errGet)
	}

	receiver, err := NewCtx(ctx, Options{
		IsSender:      false,
		SharedSecret:  uniqueSecret,
		Debug:         true,
		RelayAddress:  "127.0.0.1:8296",
		RelayPassword: "pass123",
		Stdout:        false,
		NoPrompt:      true,
		DisableLocal:  true,
		Curve:         "siec",
		Overwrite:     true,
	})
	if err != nil {
		t.Fatalf("Create receiver failed: %v", err)
	}

	fatalErr := make(chan error, 1)

	failTest := func(err error) {
		select {
		case fatalErr <- err:
		default:
		}
	}

	var wg sync.WaitGroup
	wg.Add(2)

	go func() {
		defer wg.Done()
		log.Warn("Send")
		if err := sender.Send(filesInfo, emptyFolders, totalNumberFolders); err != nil {
			failTest(fmt.Errorf("Send failed: %w", err))
		}
	}()

	go func() {
		defer wg.Done()

		if err := waitHashed(sender); err != nil {
			failTest(fmt.Errorf("waitHashed failed: %w", err))
			return
		}

		log.Warn("Receive")
		if err := receiver.Receive(); err != nil {
			failTest(fmt.Errorf("Receive failed: %w", err))
		}
	}()

	go func() {
		for i := 0; i < 3000; i++ {
			if sender.Step1ChannelSecured && receiver.Step1ChannelSecured {
				time.Sleep(time.Millisecond)
				if sender.Step2FileInfoTransferred && receiver.Step2FileInfoTransferred {
					log.Warn("Step2FileInfoTransferred reached")
					cancel2()
					return
				}
				log.Warn("Step1ChannelSecured reached")
			}
			time.Sleep(time.Millisecond)
		}
	}()

	done := make(chan bool, 1)
	go func() {
		wg.Wait()
		done <- true
	}()

	select {
	case err := <-fatalErr:
		result(t, err)
	case <-done:
		t.Error("Transfer should have been interrupted by context cancellation")
	case <-time.After(5 * time.Second):
		t.Fatal("Test timeout after 5 seconds")
	}
}
```

## File: `src/croc/ctx.go`
```go
// ctx.go
package croc

import (
	"context"
	"time"

	"github.com/schollz/croc/v10/src/message"
	"github.com/schollz/croc/v10/src/tcp"
	"github.com/schollz/croc/v10/src/utils"
	log "github.com/schollz/logger"
)

// stop manages graceful shutdown
type stop struct {
	ctx      context.Context
	cancel   context.CancelFunc
	stopChan chan struct{} //peerdiscovery
	run      func(debugLevel string, host string, port string, password string, banner ...string) (err error)
	hash     func(fname string, algorithm string, showProgress ...bool) (hash256 []byte, err error)
	gui      bool
}

// newStop creates a new stop manager instance
func newStop(ctx context.Context) *stop {
	s := &stop{
		stopChan: make(chan struct{}),
		run:      tcp.Run,
		hash:     utils.HashFile,
	}
	if ctx == nil {
		ctx = context.Background()
	}
	s.ctx, s.cancel = context.WithCancel(ctx)

	return s
}

func (s *stop) done() {
	<-s.ctx.Done()
	time.Sleep(time.Millisecond)
	close(s.stopChan)
	log.Trace("croc done")
}

// NewCtx creates a client with context support
func NewCtx(ctx context.Context, ops Options) (*Client, error) {
	// Create a regular c
	c, err := New(ops)
	if err != nil {
		return nil, err
	}
	c.stop = newStop(ctx)
	c.stop.gui = true
	c.stop.run = func(debugLevel string, host string, port string, password string, banner ...string) (err error) {
		return tcp.RunCtx(c.stop.ctx, debugLevel, host, port, password, banner...)
	}
	c.stop.hash = func(fname string, algorithm string, showProgress ...bool) (hash256 []byte, err error) {
		return utils.HashFileCtx(c.stop.ctx, fname, algorithm, showProgress...)
	}

	go func() {
		select {
		case <-ctx.Done():
			log.Trace("parent context canceled")
			c.SendError()
		case <-c.stopChan:
			// for stop goroutine
		}
		log.Trace("croc NewCtx done")
	}()

	return c, nil
}

// ctxErr checks whether it is necessary to interrupt my loops and goroutines
func (s *stop) ctxErr() error {
	select {
	case <-s.ctx.Done():
		return s.ctx.Err()
	default:
		return nil
	}
}

// Cancel initiates interruption of my loops and goroutines
func (s *stop) Cancel() {
	log.Trace("croc Cancel")
	if s.cancel != nil {
		s.cancel()
		s.cancel = nil
	}
}

// SendError tells the peer to interrupt their loops and goroutines
func (c *Client) SendError() {
	if c.Key != nil && len(c.conn) > 0 && c.conn[0] != nil {
		message.Send(c.conn[0], c.Key, message.Message{
			Type:    message.TypeError,
			Message: "refusing files",
		})
		time.Sleep(time.Millisecond)
	}
}
```

## File: `src/crypt/crypt.go`
```go
package crypt

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"crypto/sha256"
	"fmt"
	"log"

	"golang.org/x/crypto/argon2"
	"golang.org/x/crypto/chacha20poly1305"
	"golang.org/x/crypto/pbkdf2"
)

// New generates a new key based on a passphrase and salt
func New(passphrase []byte, usersalt []byte) (key []byte, salt []byte, err error) {
	if len(passphrase) < 1 {
		err = fmt.Errorf("need more than that for passphrase")
		return
	}
	if usersalt == nil {
		salt = make([]byte, 8)
		// http://www.ietf.org/rfc/rfc2898.txt
		// Salt.
		if _, err := rand.Read(salt); err != nil {
			log.Fatalf("can't get random salt: %v", err)
		}
	} else {
		salt = usersalt
	}
	key = pbkdf2.Key(passphrase, salt, 100, 32, sha256.New)
	return
}

// Encrypt will encrypt using the pre-generated key
func Encrypt(plaintext []byte, key []byte) (encrypted []byte, err error) {
	// generate a random iv each time
	// http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf
	// Section 8.2
	ivBytes := make([]byte, 12)
	if _, err = rand.Read(ivBytes); err != nil {
		log.Fatalf("can't initialize crypto: %v", err)
	}
	b, err := aes.NewCipher(key)
	if err != nil {
		return
	}
	aesgcm, err := cipher.NewGCM(b)
	if err != nil {
		return
	}
	encrypted = aesgcm.Seal(nil, ivBytes, plaintext, nil)
	encrypted = append(ivBytes, encrypted...)
	return
}

// Decrypt using the pre-generated key
func Decrypt(encrypted []byte, key []byte) (plaintext []byte, err error) {
	if len(encrypted) < 13 {
		err = fmt.Errorf("incorrect passphrase")
		return
	}
	b, err := aes.NewCipher(key)
	if err != nil {
		return
	}
	aesgcm, err := cipher.NewGCM(b)
	if err != nil {
		return
	}
	plaintext, err = aesgcm.Open(nil, encrypted[:12], encrypted[12:], nil)
	return
}

// NewArgon2 generates a new key based on a passphrase and salt
// using argon2
// https://pkg.go.dev/golang.org/x/crypto/argon2
func NewArgon2(passphrase []byte, usersalt []byte) (aead cipher.AEAD, salt []byte, err error) {
	if len(passphrase) < 1 {
		err = fmt.Errorf("need more than that for passphrase")
		return
	}
	if usersalt == nil {
		salt = make([]byte, 8)
		// http://www.ietf.org/rfc/rfc2898.txt
		// Salt.
		if _, err = rand.Read(salt); err != nil {
			log.Fatalf("can't get random salt: %v", err)
		}
	} else {
		salt = usersalt
	}
	aead, err = chacha20poly1305.NewX(argon2.IDKey(passphrase, salt, 1, 64*1024, 4, 32))
	return
}

// EncryptChaCha will encrypt ChaCha20-Poly1305 using the pre-generated key
// https://pkg.go.dev/golang.org/x/crypto/chacha20poly1305
func EncryptChaCha(plaintext []byte, aead cipher.AEAD) (encrypted []byte, err error) {
	nonce := make([]byte, aead.NonceSize(), aead.NonceSize()+len(plaintext)+aead.Overhead())
	if _, err := rand.Read(nonce); err != nil {
		panic(err)
	}

	// Encrypt the message and append the ciphertext to the nonce.
	encrypted = aead.Seal(nonce, nonce, plaintext, nil)
	return
}

// DecryptChaCha will decrypt ChaCha20-Poly1305 using the pre-generated key
// https://pkg.go.dev/golang.org/x/crypto/chacha20poly1305
func DecryptChaCha(encryptedMsg []byte, aead cipher.AEAD) (plaintext []byte, err error) {
	if len(encryptedMsg) < aead.NonceSize() {
		err = fmt.Errorf("ciphertext too short")
		return
	}

	// Split nonce and ciphertext.
	nonce, ciphertext := encryptedMsg[:aead.NonceSize()], encryptedMsg[aead.NonceSize():]

	// Decrypt the message and check it wasn't tampered with.
	plaintext, err = aead.Open(nil, nonce, ciphertext, nil)
	return
}
```

## File: `src/crypt/crypt_test.go`
```go
package crypt

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func BenchmarkEncrypt(b *testing.B) {
	bob, _, _ := New([]byte("password"), nil)
	for i := 0; i < b.N; i++ {
		Encrypt([]byte("hello, world"), bob)
	}
}

func BenchmarkDecrypt(b *testing.B) {
	key, _, _ := New([]byte("password"), nil)
	msg := []byte("hello, world")
	enc, _ := Encrypt(msg, key)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		Decrypt(enc, key)
	}
}

func BenchmarkNewPbkdf2(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		New([]byte("password"), nil)
	}
}

func BenchmarkNewArgon2(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		NewArgon2([]byte("password"), nil)
	}
}

func BenchmarkEncryptChaCha(b *testing.B) {
	bob, _, _ := NewArgon2([]byte("password"), nil)
	for i := 0; i < b.N; i++ {
		EncryptChaCha([]byte("hello, world"), bob)
	}
}

func BenchmarkDecryptChaCha(b *testing.B) {
	key, _, _ := NewArgon2([]byte("password"), nil)
	msg := []byte("hello, world")
	enc, _ := EncryptChaCha(msg, key)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		DecryptChaCha(enc, key)
	}
}

func TestEncryption(t *testing.T) {
	key, salt, err := New([]byte("password"), nil)
	assert.Nil(t, err)
	msg := []byte("hello, world")
	enc, err := Encrypt(msg, key)
	assert.Nil(t, err)
	dec, err := Decrypt(enc, key)
	assert.Nil(t, err)
	assert.Equal(t, msg, dec)

	// check reusing the salt
	key2, _, _ := New([]byte("password"), salt)
	dec, err = Decrypt(enc, key2)
	assert.Nil(t, err)
	assert.Equal(t, msg, dec)

	// check reusing the salt
	key2, _, _ = New([]byte("wrong password"), salt)
	dec, err = Decrypt(enc, key2)
	assert.NotNil(t, err)
	assert.NotEqual(t, msg, dec)

	// error with no password
	_, err = Decrypt([]byte(""), key)
	assert.NotNil(t, err)

	// error with small password
	_, _, err = New([]byte(""), nil)
	assert.NotNil(t, err)
}

func TestEncryptionChaCha(t *testing.T) {
	key, salt, err := NewArgon2([]byte("password"), nil)
	fmt.Printf("key: %x\n", key)
	assert.Nil(t, err)
	msg := []byte("hello, world")
	enc, err := EncryptChaCha(msg, key)
	assert.Nil(t, err)
	dec, err := DecryptChaCha(enc, key)
	assert.Nil(t, err)
	assert.Equal(t, msg, dec)

	// check reusing the salt
	key2, _, _ := NewArgon2([]byte("password"), salt)
	dec, err = DecryptChaCha(enc, key2)
	assert.Nil(t, err)
	assert.Equal(t, msg, dec)

	// check reusing the salt
	key2, _, _ = NewArgon2([]byte("wrong password"), salt)
	dec, err = DecryptChaCha(enc, key2)
	assert.NotNil(t, err)
	assert.NotEqual(t, msg, dec)

	// error with no password
	_, err = DecryptChaCha([]byte(""), key)
	assert.NotNil(t, err)

	// error with small password
	_, _, err = NewArgon2([]byte(""), nil)
	assert.NotNil(t, err)
}
```

## File: `src/diskusage/diskusage.go`
```go
//go:build !windows
// +build !windows

package diskusage

import (
	"golang.org/x/sys/unix"
)

// DiskUsage contains usage data and provides user-friendly access methods
type DiskUsage struct {
	stat *unix.Statfs_t
}

// NewDiskUsage returns an object holding the disk usage of volumePath
// or nil in case of error (invalid path, etc)
func NewDiskUsage(volumePath string) *DiskUsage {
	stat := unix.Statfs_t{}
	err := unix.Statfs(volumePath, &stat)
	if err != nil {
		return nil
	}
	return &DiskUsage{&stat}
}

// Free returns total free bytes on file system
func (du *DiskUsage) Free() uint64 {
	return uint64(du.stat.Bfree) * uint64(du.stat.Bsize)
}

// Available return total available bytes on file system to an unprivileged user
func (du *DiskUsage) Available() uint64 {
	return uint64(du.stat.Bavail) * uint64(du.stat.Bsize)
}

// Size returns total size of the file system
func (du *DiskUsage) Size() uint64 {
	return uint64(du.stat.Blocks) * uint64(du.stat.Bsize)
}

// Used returns total bytes used in file system
func (du *DiskUsage) Used() uint64 {
	return du.Size() - du.Free()
}

// Usage returns percentage of use on the file system
func (du *DiskUsage) Usage() float32 {
	return float32(du.Used()) / float32(du.Size())
}
```

## File: `src/diskusage/diskusage_test.go`
```go
package diskusage

import (
	"fmt"
	"testing"
)

var KB = uint64(1024)

func TestNewDiskUsage(t *testing.T) {
	usage := NewDiskUsage(".")
	fmt.Println("Free:", usage.Free()/(KB*KB))
	fmt.Println("Available:", usage.Available()/(KB*KB))
	fmt.Println("Size:", usage.Size()/(KB*KB))
	fmt.Println("Used:", usage.Used()/(KB*KB))
	fmt.Println("Usage:", usage.Usage()*100, "%")
}
```

## File: `src/diskusage/diskusage_windows.go`
```go
package diskusage

import (
	"unsafe"

	"golang.org/x/sys/windows"
)

type DiskUsage struct {
	freeBytes  int64
	totalBytes int64
	availBytes int64
}

// NewDiskUsage returns an object holding the disk usage of volumePath
// or nil in case of error (invalid path, etc)
func NewDiskUsage(volumePath string) *DiskUsage {
	h := windows.MustLoadDLL("kernel32.dll")
	c := h.MustFindProc("GetDiskFreeSpaceExW")

	du := &DiskUsage{}

	c.Call(
		uintptr(unsafe.Pointer(windows.StringToUTF16Ptr(volumePath))),
		uintptr(unsafe.Pointer(&du.freeBytes)),
		uintptr(unsafe.Pointer(&du.totalBytes)),
		uintptr(unsafe.Pointer(&du.availBytes)))

	return du
}

// Free returns total free bytes on file system
func (du *DiskUsage) Free() uint64 {
	return uint64(du.freeBytes)
}

// Available returns total available bytes on file system to an unprivileged user
func (du *DiskUsage) Available() uint64 {
	return uint64(du.availBytes)
}

// Size returns total size of the file system
func (du *DiskUsage) Size() uint64 {
	return uint64(du.totalBytes)
}

// Used returns total bytes used in file system
func (du *DiskUsage) Used() uint64 {
	return du.Size() - du.Free()
}

// Usage returns percentage of use on the file system
func (du *DiskUsage) Usage() float32 {
	return float32(du.Used()) / float32(du.Size())
}
```

## File: `src/install/Makefile`
```
# VERSION=8.X.Y make release

release:
	cd ../../ && go run src/install/updateversion.go
	git commit -am "bump ${VERSION}"
	git tag -af v${VERSION} -m "v${VERSION}"	
	git push
	git push --tags
	cp zsh_autocomplete ../../
	cp bash_autocomplete ../../
	cd ../../ && goreleaser release
	cd ../../ && ./src/install/prepare-sources-tarball.sh
	cd ../../ && ./src/install/upload-src-tarball.sh

test:
	cp zsh_autocomplete ../../
	cp bash_autocomplete ../../
	cd ../../ && go generate
	cd ../../ && goreleaser release --skip-publish
```

## File: `src/install/bash_autocomplete`
```
: ${PROG:=$(basename ${BASH_SOURCE})}

_cli_bash_autocomplete() {
  if [[ "${COMP_WORDS[0]}" != "source" ]]; then
    local cur opts base
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    if [[ "$cur" == "-"* ]]; then
      opts=$( ${COMP_WORDS[@]:0:$COMP_CWORD} ${cur} --generate-bash-completion )
    else
      opts=$( ${COMP_WORDS[@]:0:$COMP_CWORD} --generate-bash-completion )
    fi
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
  fi
}

complete -o bashdefault -o default -o nospace -F _cli_bash_autocomplete $PROG
unset PROG
```

## File: `src/install/default.txt`
```
#!/bin/bash - 
#===============================================================================
#
#          FILE: default.txt
# 
#         USAGE: curl https://getcroc.schollz.com | bash
#                 OR
#                wget -qO- https://getcroc.schollz.com | bash
# 
#   DESCRIPTION: croc Installer Script.
#
#                This script installs croc into a specified prefix.
#                Default prefix = /usr/local/bin
#
#       OPTIONS: -p, --prefix "${INSTALL_PREFIX}"
#                      Prefix to install croc into.  Defaults to /usr/local/bin
#  REQUIREMENTS: bash, uname, tar/unzip, curl/wget, sudo/doas (if not run
#                as root), install, mktemp, sha256sum/shasum/sha256
#
#          BUGS: ...hopefully not.  Please report.
#
#         NOTES: Homepage: https://schollz.com/software/croc
#                  Issues: https://github.com/schollz/croc/issues
#
#       CREATED: 08/10/2019 16:41
#      REVISION: 0.9.2
#===============================================================================
set -o nounset                              # Treat unset variables as an error

#-------------------------------------------------------------------------------
# DEFAULTS
#-------------------------------------------------------------------------------
PREFIX="${PREFIX:-}"
ANDROID_ROOT="${ANDROID_ROOT:-}"

# Termux on Android has ${PREFIX} set which already ends with '/usr'
if [[ -n "${ANDROID_ROOT}" && -n "${PREFIX}" ]]; then
  INSTALL_PREFIX="${PREFIX}/bin"
else
  INSTALL_PREFIX="/usr/local/bin"
fi

#-------------------------------------------------------------------------------
# FUNCTIONS
#-------------------------------------------------------------------------------


#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  print_banner
#   DESCRIPTION:  Prints a banner
#    PARAMETERS:  none
#       RETURNS:  0
#-------------------------------------------------------------------------------
print_banner() {
  cat <<-'EOF'
=================================================
              ____
             / ___|_ __ ___   ___
            | |   | '__/ _ \ / __|
            | |___| | | (_) | (__
             \____|_|  \___/ \___|

       ___           _        _ _
      |_ _|_ __  ___| |_ __ _| | | ___ _ __
       | || '_ \/ __| __/ _` | | |/ _ \ '__|
       | || | | \__ \ || (_| | | |  __/ |
      |___|_| |_|___/\__\__,_|_|_|\___|_| 
==================================================
EOF
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  print_help
#   DESCRIPTION:  Prints out a help message
#    PARAMETERS:  none
#       RETURNS:  0
#-------------------------------------------------------------------------------
print_help() {
  local help_header
  local help_message

  help_header="croc Installer Script"
  help_message="Usage:
  -p INSTALL_PREFIX
      Prefix to install croc into.  Directory must already exist.
      Default = /usr/local/bin ('\${PREFIX}/bin' on Termux for Android)
  
  -h
      Prints this helpful message and exit."

  echo "${help_header}"
  echo ""
  echo "${help_message}"
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  print_message
#   DESCRIPTION:  Prints a message all fancy like
#    PARAMETERS:  $1 = Message to print
#                 $2 = Severity. info, ok, error, warn
#       RETURNS:  Formatted Message to stdout
#-------------------------------------------------------------------------------
print_message() {
  local message
  local severity
  local red
  local green
  local yellow
  local nc

  message="${1}"
  severity="${2}"
  red='\e[0;31m'
  green='\e[0;32m'
  yellow='\e[1;33m'
  nc='\e[0m'

  case "${severity}" in
    "info" ) echo -e "${nc}${message}${nc}";;
      "ok" ) echo -e "${green}${message}${nc}";;
   "error" ) echo -e "${red}${message}${nc}";;
    "warn" ) echo -e "${yellow}${message}${nc}";;
  esac


}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  make_tempdir
#   DESCRIPTION:  Makes a temp dir using mktemp if available
#    PARAMETERS:  $1 = Directory template
#       RETURNS:  0 = Created temp dir. Also prints temp file path to stdout
#                 1 = Failed to create temp dir
#                 20 = Failed to find mktemp
#-------------------------------------------------------------------------------
make_tempdir() {
  local template
  local tempdir
  local tempdir_rcode

  template="${1}.XXXXXX"

  if command -v mktemp >/dev/null 2>&1; then
    tempdir="$(mktemp -d -t "${template}")"
    tempdir_rcode="${?}"
    if [[ "${tempdir_rcode}" == "0" ]]; then
      echo "${tempdir}"
      return 0
    else
      return 1
    fi
  else
    return 20
  fi
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  determine_os
#   DESCRIPTION:  Attempts to determine host os using uname
#    PARAMETERS:  none
#       RETURNS:  0 = OS Detected. Also prints detected os to stdout
#                 1 = Unknown OS
#                 20 = 'uname' not found in path
#-------------------------------------------------------------------------------
determine_os() {
  local uname_out

  if command -v uname >/dev/null 2>&1; then
    uname_out="$(uname)"
    if [[ "${uname_out}" == "" ]]; then
      return 1
    else
      echo "${uname_out}"
      return 0
    fi
  else
    return 20
  fi
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  determine_arch
#   DESCRIPTION:  Attempt to determine architecture of host
#    PARAMETERS:  none
#       RETURNS:  0 = Arch Detected. Also prints detected arch to stdout
#                 1 = Unknown arch
#                 20 = 'uname' not found in path
#-------------------------------------------------------------------------------
determine_arch() {
  local uname_out

  if command -v uname >/dev/null 2>&1; then
    uname_out="$(uname -m)"
    if [[ "${uname_out}" == "" ]]; then
      return 1
    else
      echo "${uname_out}"
      return 0
    fi
  else
    return 20
  fi
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  run_as
#   DESCRIPTION:  Run a command as root if needed. If already root, runs it
#                 directly; otherwise tries sudo then doas. Returns 21 if
#                 neither sudo nor doas is available when needed.
#    PARAMETERS:  $@ = command and args
#       RETURNS:  Return code of executed command, or 21 if no escalation tool
#-------------------------------------------------------------------------------
run_as() {
  if [[ "${EUID}" == "0" ]]; then
    "$@"
    return $?
  fi

  if command -v sudo >/dev/null 2>&1; then
    sudo "$@"
    return $?
  fi

  if command -v doas >/dev/null 2>&1; then
    doas "$@"
    return $?
  fi

  # No escalation tool found
  return 21
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  download_file
#   DESCRIPTION:  Downloads a file into the specified directory.  Attempts to
#                 use curl, then wget.  If neither is found, fail.
#    PARAMETERS:  $1 = url of file to download
#                 $2 = location to download file into on host system
#       RETURNS:  If curl or wget found, returns the return code of curl or wget
#                 20 = Could not find curl and wget
#-------------------------------------------------------------------------------
download_file() {
  local url
  local dir
  local filename
  local rcode

  url="${1}"
  dir="${2}"
  filename="${3}"

  if command -v curl >/dev/null 2>&1; then
    curl -fsSL "${url}" -o "${dir}/${filename}"
    rcode="${?}"
  elif command -v wget >/dev/null 2>&1; then
    wget --quiet  "${url}" -O "${dir}/${filename}"
    rcode="${?}"
  else
    rcode="20"
  fi
  
  return "${rcode}"
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  checksum_check
#   DESCRIPTION:  Attempt to verify checksum of downloaded file to ensure
#                 integrity.  Tries multiple tools before failing.
#    PARAMETERS:  $1 = path to checksum file
#                 $2 = location of file to check
#                 $3 = working directory
#       RETURNS:  0 = checkusm verified
#                 1 = checksum verification failed
#                 20 = failed to determine tool to use to check checksum
#                 30 = failed to change into or go back from working dir
#-------------------------------------------------------------------------------
checksum_check() {
  local checksum_file
  local file
  local dir
  local rcode
  local shasum_1
  local shasum_2
  local shasum_c

  checksum_file="${1}"
  file="${2}"
  dir="${3}"

  cd "${dir}" || return 30
  if command -v sha256sum >/dev/null 2>&1; then
    ## Not all sha256sum versions seem to have --ignore-missing, so filter the checksum file
    ## to only include the file we downloaded.
    grep "$(basename "${file}")" "${checksum_file}" > filtered_checksum.txt
    shasum_c="$(sha256sum -c "filtered_checksum.txt")"
    rcode="${?}"
  elif command -v shasum >/dev/null 2>&1; then
    ## With shasum on FreeBSD, we don't get to --ignore-missing, so filter the checksum file
    ## to only include the file we downloaded.
    grep "$(basename "${file}")" "${checksum_file}" > filtered_checksum.txt
    shasum_c="$(shasum -a 256 -c "filtered_checksum.txt")"
    rcode="${?}"
  elif command -v sha256 >/dev/null 2>&1; then
    ## With sha256 on FreeBSD, we don't get to --ignore-missing, so filter the checksum file
    ## to only include the file we downloaded.
    ## Also sha256 -c option seems to fail, so fall back to an if statement
    grep "$(basename "${file}")" "${checksum_file}" > filtered_checksum.txt
    shasum_1="$(sha256 -q "${file}")"
    shasum_2="$(awk '{print $1}' filtered_checksum.txt)"
    if [[ "${shasum_1}" == "${shasum_2}" ]]; then
      rcode="0"
    else
      rcode="1"
    fi
    shasum_c="Expected: ${shasum_1}, Got: ${shasum_2}"
  else
    return 20
  fi
  cd - >/dev/null 2>&1 || return 30
  
  if [[ "${rcode}" -gt "0" ]]; then
    echo "${shasum_c}"
  fi
  return "${rcode}"
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  extract_file
#   DESCRIPTION:  Extracts a file into a location.  Attempts to determine which
#                 tool to use by checking file extension.
#    PARAMETERS:  $1 = file to extract
#                 $2 = location to extract file into
#                 $3 = extension
#       RETURNS:  Return code of the tool used to extract the file
#                 20 = Failed to determine which tool to use
#                 30 = Failed to find tool in path
#-------------------------------------------------------------------------------
extract_file() {
  local file
  local dir
  local ext
  local rcode

  file="${1}"
  dir="${2}"
  ext="${3}"

  case "${ext}" in
       "zip" ) if command -v unzip >/dev/null 2>&1; then
                 unzip "${file}" -d "${dir}"
                 rcode="${?}"
               else
                 rcode="30"
               fi
               ;;
    "tar.gz" ) if command -v tar >/dev/null 2>&1; then
                 tar -xf "${file}" -C "${dir}"
                 rcode="${?}"
               else
                 rcode="31"
               fi
               ;;
           * ) rcode="20";;
  esac

  return "${rcode}"
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  create_prefix
#   DESCRIPTION:  Creates the install prefix (and any parent directories). If
#                 EUID not 0, then attempt to use sudo/doas (run_as).
#    PARAMETERS:  $1 = prefix
#       RETURNS:  Return code of the tool used to make the directory
#                 0 = Created the directory
#                 >0 = Failed to create directory  
#                 20 = Could not find mkdir command
#                 21 = Could not find sudo/doas command (when needed)
#-------------------------------------------------------------------------------
create_prefix() {
  local prefix
  local rcode

  prefix="${1}"

  if command -v mkdir >/dev/null 2>&1; then
    run_as mkdir -p "${prefix}"
    rcode="${?}"
  else
    rcode="20"
  fi

  return "${rcode}"
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  install_file_freebsd
#   DESCRIPTION:  Installs a file into a location using 'install'.  If EUID not
#                 0, then attempt to use sudo/doas (run_as).
#    PARAMETERS:  $1 = file to install
#                 $2 = location to install file into
#       RETURNS:  0 = File Installed
#                 1 = File not installed
#                 20 = Could not find install command
#                 21 = Could not find sudo/doas command (when needed)
#-------------------------------------------------------------------------------
install_file_freebsd() {
  local file
  local prefix
  local rcode

  file="${1}"
  prefix="${2}"

  if command -v install >/dev/null 2>&1; then
    run_as install -C -b -B '_old' -m 755 "${file}" "${prefix}"
    rcode="${?}"
  else
    rcode="20"
  fi

  return "${rcode}"
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  install_file_linux
#   DESCRIPTION:  Installs a file into a location using 'install'.  If EUID not
#                 0, then attempt to use sudo/doas (run_as) (unless on android).
#                 Falls back to cp/chmod for BusyBox compatibility.
#    PARAMETERS:  $1 = file to install
#                 $2 = location to install file into
#       RETURNS:  0 = File Installed
#                 1 = File not installed
#                 20 = Could not find install or cp command
#                 21 = Could not find sudo/doas command (when needed)
#-------------------------------------------------------------------------------
install_file_linux() {
  local file
  local prefix
  local rcode

  file="${1}"
  prefix="${2}"

  if command -v install >/dev/null 2>&1; then
    if [[ "${EUID}" == "0" ]]; then
      # Try GNU install first, fall back to simple install for BusyBox
      install -C -b -S '_old' -m 755 -t "${prefix}" "${file}" 2>/dev/null || \
        install -m 755 "${file}" "${prefix}/"
      rcode="${?}"
    else
      # Try sudo, then doas, then (special-case) Android direct install, else fail
      if command -v sudo >/dev/null 2>&1; then
        sudo install -C -b -S '_old' -m 755 "${file}" "${prefix}" 2>/dev/null || \
          sudo install -m 755 "${file}" "${prefix}/"
        rcode="${?}"
      elif command -v doas >/dev/null 2>&1; then
        doas install -C -b -S '_old' -m 755 "${file}" "${prefix}" 2>/dev/null || \
          doas install -m 755 "${file}" "${prefix}/"
        rcode="${?}"
      elif [[ "${ANDROID_ROOT}" != "" ]]; then
        install -C -b -S '_old' -m 755 -t "${prefix}" "${file}" 2>/dev/null || \
          install -m 755 "${file}" "${prefix}/"
        rcode="${?}"
      else
        rcode="21"
      fi
    fi
  elif command -v cp >/dev/null 2>&1; then
    # Fallback to cp/chmod if install is not available
    if [[ "${EUID}" == "0" ]]; then
      cp "${file}" "${prefix}/" && chmod 755 "${prefix}/$(basename "${file}")"
      rcode="${?}"
    else
      if command -v sudo >/dev/null 2>&1; then
        sudo cp "${file}" "${prefix}/" && sudo chmod 755 "${prefix}/$(basename "${file}")"
        rcode="${?}"
      elif command -v doas >/dev/null 2>&1; then
        doas cp "${file}" "${prefix}/" && doas chmod 755 "${prefix}/$(basename "${file}")"
        rcode="${?}"
      else
        rcode="21"
      fi
    fi
  else
    rcode="20"
  fi

  return "${rcode}"
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  install_file_cygwin
#   DESCRIPTION:  Installs a file into a location using 'install'.  If EUID not
#                 0, then attempt to use sudo/doas (run_as).
#                 Not really 100% sure this is how to install croc in cygwin.
#    PARAMETERS:  $1 = file to install
#                 $2 = location to install file into
#       RETURNS:  0 = File Installed
#                 20 = Could not find install command
#                 21 = Could not find sudo/doas command (when needed)
#-------------------------------------------------------------------------------
install_file_cygwin() {
  local file
  local prefix
  local rcode

  file="${1}"
  prefix="${2}"

  if command -v install >/dev/null 2>&1; then
    run_as install -m 755 "${file}" "${prefix}"
    rcode="${?}"
  else
    rcode="20"
  fi

  return "${rcode}"
}

#---  FUNCTION  ----------------------------------------------------------------
#          NAME:  main
#   DESCRIPTION:  Put it all together in a logical way
#                 ...at least that is the hope...
#    PARAMETERS:  1 = prefix
#       RETURNS:  0 = All good
#                 1 = Something done broke
#-------------------------------------------------------------------------------
main() {
  local prefix
  local tmpdir
  local tmpdir_rcode
  local croc_arch
  local croc_arch_rcode
  local croc_os
  local croc_os_rcode
  local croc_base_url
  local croc_url
  local croc_file
  local croc_checksum_file
  local croc_bin_name
  local croc_version
  local croc_dl_ext
  local download_file_rcode
  local download_checksum_file_rcode
  local checksum_check_rcode
  local extract_file_rcode
  local install_file_rcode
  local create_prefix_rcode
  local bash_autocomplete_file
  local bash_autocomplete_prefix
  local zsh_autocomplete_file
  local zsh_autocomplete_prefix
  local autocomplete_install_rcode

  croc_bin_name="croc"
  croc_version="10.4.2"
  croc_dl_ext="tar.gz"
  croc_base_url="https://github.com/schollz/croc/releases/download"
  prefix="${1}"
  bash_autocomplete_file="bash_autocomplete"
  bash_autocomplete_prefix="/etc/bash_completion.d"
  zsh_autocomplete_file="zsh_autocomplete"
  zsh_autocomplete_prefix="/etc/zsh"

  print_banner
  print_message "== Install prefix set to ${prefix}" "info"
  
  tmpdir="$(make_tempdir "${croc_bin_name}")"
  tmpdir_rcode="${?}"
  if [[ "${tmpdir_rcode}" == "0" ]]; then
    print_message "== Created temp dir at ${tmpdir}" "info"
  elif [[ "${tmpdir_rcode}" == "1" ]]; then
    print_message "== Failed to create temp dir at ${tmpdir}" "error"
  else
    print_message "== 'mktemp' not found in path. Is it installed?" "error"
    exit 1
  fi

  croc_arch="$(determine_arch)"
  croc_arch_rcode="${?}"
  if [[ "${croc_arch_rcode}" == "0" ]]; then
    print_message "== Architecture detected as ${croc_arch}" "info"
  elif [[ "${croc_arch_rcode}" == "1" ]]; then
    print_message "== Architecture not detected" "error"
    exit 1
  else
    print_message "== 'uname' not found in path. Is it installed?" "error"
    exit 1
  fi

  croc_os="$(determine_os)"
  croc_os_rcode="${?}"
  if [[ "${croc_os_rcode}" == "0" ]]; then
    print_message "== OS detected as ${croc_os}" "info"
  elif [[ "${croc_os_rcode}" == "1" ]]; then
    print_message "== OS not detected" "error"
    exit 1
  else
    print_message "== 'uname' not found in path. Is it installed?" "error"
    exit 1
  fi

  case "${croc_os}" in
     "Darwin" ) croc_os="macOS";;
    *"BusyBox"* )
        croc_os="Linux"
        ;;
    "MINGW"* ) croc_os="Windows";
                croc_dl_ext="zip";;
    "CYGWIN"* ) croc_os="Windows";
                croc_dl_ext="zip";
                print_message "== Cygwin is currently unsupported." "error";
                exit 1;;
  esac

  case "${croc_arch}" in
     "x86_64" ) croc_arch="64bit";;
      "amd64" ) croc_arch="64bit";;
    "aarch64" ) croc_arch="ARM64";;
      "arm64" ) croc_arch="ARM64";;
     "armv7l" ) croc_arch="ARM";;
     "armv8l" ) croc_arch="ARM";;
     "armv9l" ) croc_arch="ARM";;
       "i686" ) croc_arch="32bit";;
    "riscv64" ) croc_arch="RISCV64";;
            * ) croc_arch="unknown";;
  esac

  croc_file="${croc_bin_name}_v${croc_version}_${croc_os}-${croc_arch}.${croc_dl_ext}"
  croc_checksum_file="${croc_bin_name}_v${croc_version}_checksums.txt"
  croc_url="${croc_base_url}/v${croc_version}/${croc_file}"
  croc_checksum_url="${croc_base_url}/v${croc_version}/${croc_checksum_file}"
  echo "${croc_url}" "${tmpdir}" "${croc_file}"
  download_file "${croc_url}" "${tmpdir}" "${croc_file}"
  download_file_rcode="${?}"
  if [[ "${download_file_rcode}" == "0" ]]; then
    print_message "== Downloaded croc archive into ${tmpdir}" "info"
  elif [[ "${download_file_rcode}" == "1" ]]; then
    print_message "== Failed to download croc archive" "error"
    exit 1
  elif [[ "${download_file_rcode}" == "20" ]]; then
    print_message "== Failed to locate curl or wget" "error"
    exit 1
  else
    print_message "== Return code of download tool returned an unexpected value of ${download_file_rcode}" "error"
    exit 1
  fi
  download_file "${croc_checksum_url}" "${tmpdir}" "${croc_checksum_file}"
  download_checksum_file_rcode="${?}"
  if [[ "${download_checksum_file_rcode}" == "0" ]]; then
    print_message "== Downloaded croc checksums file into ${tmpdir}" "info"
  elif [[ "${download_checksum_file_rcode}" == "1" ]]; then
    print_message "== Failed to download croc checksums" "error"
    exit 1
  elif [[ "${download_checksum_file_rcode}" == "20" ]]; then
    print_message "== Failed to locate curl or wget" "error"
    exit 1
  else
    print_message "== Return code of download tool returned an unexpected value of ${download_checksum_file_rcode}" "error"
    exit 1
  fi

  checksum_check "${tmpdir}/${croc_checksum_file}" "${tmpdir}/${croc_file}" "${tmpdir}"
  checksum_check_rcode="${?}"
  if [[ "${checksum_check_rcode}" == "0" ]]; then
    print_message "== Checksum of ${tmpdir}/${croc_file} verified" "ok"
  elif [[ "${checksum_check_rcode}" == "1" ]]; then
    print_message "== Failed to verify checksum of ${tmpdir}/${croc_file}" "error"
    exit 1
  elif [[ "${checksum_check_rcode}" == "20" ]]; then
    print_message "== Failed to find tool to verify sha256 sums" "error"
    exit 1
  elif [[ "${checksum_check_rcode}" == "30" ]]; then
    print_message "== Failed to change into working directory ${tmpdir}" "error"
    exit 1
  else
    print_message "== Unknown return code returned while checking checksum of ${tmpdir}/${croc_file}. Returned ${checksum_check_rcode}" "error"
    exit 1
  fi

  extract_file "${tmpdir}/${croc_file}" "${tmpdir}/" "${croc_dl_ext}"
  extract_file_rcode="${?}"
  if [[ "${extract_file_rcode}" == "0" ]]; then
    print_message "== Extracted ${croc_file} to ${tmpdir}/" "info"
  elif [[ "${extract_file_rcode}" == "1" ]]; then
    print_message "== Failed to extract ${croc_file}" "error"
    exit 1
  elif [[ "${extract_file_rcode}" == "20" ]]; then
    print_message "== Failed to determine which extraction tool to use" "error"
    exit 1
  elif [[ "${extract_file_rcode}" == "30" ]]; then
    print_message "== Failed to find 'unzip' in path" "error"
    exit 1
  elif [[ "${extract_file_rcode}" == "31" ]]; then
    print_message "== Failed to find 'tar' in path" "error"
    exit 1
  else
    print_message "== Unknown error returned from extraction attempt" "error"
    exit 1
  fi

  if [[ ! -d "${prefix}" ]]; then
    create_prefix "${prefix}"
    create_prefix_rcode="${?}"
    if [[ "${create_prefix_rcode}" == "0" ]]; then
      print_message "== Created install prefix at ${prefix}" "info"
    elif [[ "${create_prefix_rcode}" == "20" ]]; then
      print_message "== Failed to find mkdir in path" "error"
      exit 1
    elif [[ "${create_prefix_rcode}" == "21" ]]; then
      print_message "== Failed to find sudo or doas in path" "error"
      exit 1
    else
      print_message "== Failed to create the install prefix: ${prefix}" "error"
      exit 1
    fi
  else
    print_message "== Install prefix already exists. No need to create it." "info"
  fi

  [ ! -d "${bash_autocomplete_prefix}/croc" ] && mkdir -p "${bash_autocomplete_prefix}/croc" >/dev/null 2>&1
  case "${croc_os}" in
    "Linux" ) install_file_linux "${tmpdir}/${croc_bin_name}" "${prefix}/";
              install_file_rcode="${?}";;
  "FreeBSD" ) install_file_freebsd "${tmpdir}/${croc_bin_name}" "${prefix}/";
              install_file_rcode="${?}";;
    "macOS" ) install_file_freebsd "${tmpdir}/${croc_bin_name}" "${prefix}/";
              install_file_rcode="${?}";;
  "Windows" ) install_file_cygwin "${tmpdir}/${croc_bin_name}" "${prefix}/";
              install_file_rcode="${?}";;
  esac

  if [[ "${install_file_rcode}" == "0" ]] ; then
    print_message "== Installed ${croc_bin_name} to ${prefix}/" "ok"
  elif [[ "${install_file_rcode}" == "1" ]]; then
    print_message "== Failed to install ${croc_bin_name}" "error"
    exit 1
  elif [[ "${install_file_rcode}" == "20" ]]; then
    print_message "== Failed to locate 'install' command" "error"
    exit 1
  elif [[ "${install_file_rcode}" == "21" ]]; then
    print_message "== Failed to locate 'sudo' or 'doas' command" "error"
    exit 1
  else
    print_message "== Install attempt returned an unexpected value of ${install_file_rcode}" "error"
    exit 1
  fi

  # case "$(basename ${SHELL})" in
  #   "bash" ) install_file_linux "${tmpdir}/${bash_autocomplete_file}" "${bash_autocomplete_prefix}/croc";
  #            autocomplete_install_rcode="${?}";;
  #    "zsh" ) install_file_linux "${tmpdir}/${zsh_autocomplete_file}" "${zsh_autocomplete_prefix}/zsh_autocomplete_croc";
  #            autocomplete_install_rcode="${?}";
  #            print_message "== You will need to add the following to your ~/.zshrc to enable autocompletion" "info";
  #            print_message "\nPROG=croc\n_CLI_ZSH_AUTOCOMPLETE_HACK=1\nsource /etc/zsh/zsh_autocomplete_croc\n" "info";;
  #    *)      autocomplete_install_rcode="1";;
  # esac

  # if [[ "${autocomplete_install_rcode}" == "0" ]] ; then
  #   print_message "== Installed autocompletions for $(basename "${SHELL}")" "ok"
  # elif [[ "${autocomplete_install_rcode}" == "1" ]]; then
  #   print_message "== Failed to install ${bash_autocomplete_file}" "error"
  # elif [[ "${autocomplete_install_rcode}" == "20" ]]; then
  #   print_message "== Failed to locate 'install' command" "error"
  # elif [[ "${autocomplete_install_rcode}" == "21" ]]; then
  #   print_message "== Failed to locate 'sudo' command" "error"
  # else
  #   print_message "== Install attempt returned an unexpected value of ${autocomplete_install_rcode}" "error"
  # fi

  print_message "== Installation complete" "ok"
  
  exit 0
}

#-------------------------------------------------------------------------------
#  ARGUMENT PARSING
#-------------------------------------------------------------------------------
OPTS="hp:"
while getopts "${OPTS}" optchar; do
  case "${optchar}" in
    'h' ) print_help
          exit 0
          ;;
    'p' ) INSTALL_PREFIX="${OPTARG}"
          ;;
     /? ) print_message "Unknown option ${OPTARG}" "warn"
          ;;
  esac
done

#-------------------------------------------------------------------------------
# CALL MAIN
#-------------------------------------------------------------------------------
main "${INSTALL_PREFIX}"
```

## File: `src/install/prepare-sources-tarball.sh`
```bash
#!/bin/bash
tmp=$(mktemp -d)
echo $VERSION
git clone -b v${VERSION} --depth 1 https://github.com/schollz/croc $tmp/croc-${VERSION}
(cd $tmp/croc-${VERSION} && go mod tidy && go mod vendor)
(cd $tmp && tar -cvzf croc_${VERSION}_src.tar.gz croc-${VERSION})
mv $tmp/croc_${VERSION}_src.tar.gz dist/
```

## File: `src/install/updateversion.go`
```go
package main

import (
	"fmt"
	"os"
	"os/exec"
	"strings"
)

func main() {
	err := run()
	if err != nil {
		fmt.Println(err)
	}
}

func run() (err error) {
	versionNew := "v" + os.Getenv("VERSION")
	versionHash, err := exec.Command("git", "rev-parse", "--short", "HEAD").Output()
	if err != nil {
		return
	}
	versionHashNew := strings.TrimSpace(string(versionHash))
	fmt.Println(versionNew)
	fmt.Println(versionHashNew)

	err = replaceInFile("src/cli/cli.go", `Version = "`, `"`, versionNew+"-"+versionHashNew)
	if err == nil {
		fmt.Printf("updated cli.go to version %s\n", versionNew)
	}
	err = replaceInFile("README.md", `version-`, `-b`, strings.Split(versionNew, "-")[0])
	if err == nil {
		fmt.Printf("updated README to version %s\n", strings.Split(versionNew, "-")[0])
	}

	err = replaceInFile("src/install/default.txt", `croc_version="`, `"`, strings.Split(versionNew, "-")[0][1:])
	if err == nil {
		fmt.Printf("updated default.txt to version %s\n", strings.Split(versionNew, "-")[0][1:])
	}

	return
}

func replaceInFile(fname, start, end, replacement string) (err error) {
	b, err := os.ReadFile(fname)
	if err != nil {
		return
	}
	oldVersion := getStringInBetween(string(b), start, end)
	if oldVersion == "" {
		err = fmt.Errorf("nothing")
		return
	}
	newF := strings.Replace(
		string(b),
		fmt.Sprintf("%s%s%s", start, oldVersion, end),
		fmt.Sprintf("%s%s%s", start, replacement, end),
		1,
	)
	err = os.WriteFile(fname, []byte(newF), 0o644)
	return
}

// getStringInBetween Returns empty string if no start string found
func getStringInBetween(str, start, end string) (result string) {
	s := strings.Index(str, start)
	if s == -1 {
		return
	}
	s += len(start)
	e := strings.Index(str[s:], end)
	if e == -1 {
		return
	}
	e += s
	return str[s:e]
}
```

## File: `src/install/upload-src-tarball.sh`
```bash
#!/bin/bash
VERSION=$(cat ./src/cli/cli.go | grep 'Version = "v' | sed 's/[^0-9.]*\([0-9.]*\).*/\1/')
echo $VERSION

# Check dependencies.
set -e
xargs=$(which gxargs || which xargs)

# Validate settings.
[ "$TRACE" ] && set -x

CONFIG=$@

for line in $CONFIG; do
  eval "$line"
done

owner="schollz"
repo="croc"
tag="v${VERSION}"
filename="dist/croc_${VERSION}_src.tar.gz"

# Define variables.
GH_API="https://api.github.com"
GH_REPO="$GH_API/repos/$owner/$repo"
GH_TAGS="$GH_REPO/releases/tags/$tag"
AUTH="Authorization: token $GITHUB_TOKEN"
WGET_ARGS="--content-disposition --auth-no-challenge --no-cookie"
CURL_ARGS="-LJO#"

if [[ "$tag" == 'LATEST' ]]; then
  GH_TAGS="$GH_REPO/releases/latest"
fi

# Validate token.
curl -o /dev/null -sH "$AUTH" $GH_REPO || { echo "Error: Invalid repo, token or network issue!";  exit 1; }

# Read asset tags.
response=$(curl -sH "$AUTH" $GH_TAGS)

# Get ID of the asset based on given filename.
eval $(echo "$response" | grep -m 1 "id.:" | grep -w id | tr : = | tr -cd '[[:alnum:]]=')
[ "$id" ] || { echo "Error: Failed to get release id for tag: $tag"; echo "$response" | awk 'length($0)<100' >&2; exit 1; }

# Upload asset
echo "Uploading asset... "

# Construct url
GH_ASSET="https://uploads.github.com/repos/$owner/$repo/releases/$id/assets?name=$(basename $filename)"

curl "$GITHUB_OAUTH_BASIC" --data-binary @"$filename" -H "Authorization: token $GITHUB_TOKEN" -H "Content-Type: application/octet-stream" $GH_ASSET
```

## File: `src/install/zsh_autocomplete`
```
#compdef $PROG

_cli_zsh_autocomplete() {

  local -a opts
  local cur
  cur=${words[-1]}
  if [[ "$cur" == "-"* ]]; then
    opts=("${(@f)$(_CLI_ZSH_AUTOCOMPLETE_HACK=1 ${words[@]:0:#words[@]-1} ${cur} --generate-bash-completion)}")
  else
    opts=("${(@f)$(_CLI_ZSH_AUTOCOMPLETE_HACK=1 ${words[@]:0:#words[@]-1} --generate-bash-completion)}")
  fi

  if [[ "${opts[1]}" != "" ]]; then
    _describe 'values' opts
  else
    _files
  fi

  return
}

compdef _cli_zsh_autocomplete $PROG
```

## File: `src/message/message.go`
```go
package message

import (
	"encoding/json"

	"github.com/schollz/croc/v10/src/comm"
	"github.com/schollz/croc/v10/src/compress"
	"github.com/schollz/croc/v10/src/crypt"
	log "github.com/schollz/logger"
)

// Type is a message type
type Type string

const (
	TypePAKE           Type = "pake"
	TypeExternalIP     Type = "externalip"
	TypeFinished       Type = "finished"
	TypeError          Type = "error"
	TypeCloseRecipient Type = "close-recipient"
	TypeCloseSender    Type = "close-sender"
	TypeRecipientReady Type = "recipientready"
	TypeFileInfo       Type = "fileinfo"
)

// Message is the possible payload for messaging
type Message struct {
	Type    Type   `json:"t,omitempty"`
	Message string `json:"m,omitempty"`
	Bytes   []byte `json:"b,omitempty"`
	Bytes2  []byte `json:"b2,omitempty"`
	Num     int    `json:"n,omitempty"`
}

func (m Message) String() string {
	b, _ := json.Marshal(m)
	return string(b)
}

// Send will send out
func Send(c *comm.Comm, key []byte, m Message) (err error) {
	mSend, err := Encode(key, m)
	if err != nil {
		return
	}
	err = c.Send(mSend)
	return
}

// Encode will convert to bytes
func Encode(key []byte, m Message) (b []byte, err error) {
	b, err = json.Marshal(m)
	if err != nil {
		return
	}
	b = compress.Compress(b)
	if key != nil {
		log.Debugf("writing %s message (encrypted)", m.Type)
		b, err = crypt.Encrypt(b, key)
	} else {
		log.Debugf("writing %s message (unencrypted)", m.Type)
	}
	return
}

// Decode will convert from bytes
func Decode(key []byte, b []byte) (m Message, err error) {
	if key != nil {
		b, err = crypt.Decrypt(b, key)
		if err != nil {
			return
		}
	}
	b = compress.Decompress(b)
	err = json.Unmarshal(b, &m)
	if err == nil {
		if key != nil {
			log.Debugf("read %s message (encrypted)", m.Type)
		} else {
			log.Debugf("read %s message (unencrypted)", m.Type)
		}
	}
	return
}
```

## File: `src/message/message_test.go`
```go
package message

import (
	"crypto/rand"
	"fmt"
	"net"
	"testing"
	"time"

	"github.com/schollz/croc/v10/src/comm"
	"github.com/schollz/croc/v10/src/crypt"
	log "github.com/schollz/logger"
	"github.com/stretchr/testify/assert"
)

var TypeMessage Type = "message"

func TestMessage(t *testing.T) {
	log.SetLevel("debug")
	m := Message{Type: TypeMessage, Message: "hello, world"}
	e, salt, err := crypt.New([]byte("pass"), nil)
	assert.Nil(t, err)
	fmt.Println(string(salt))
	b, err := Encode(e, m)
	assert.Nil(t, err)
	fmt.Printf("%x\n", b)

	m2, err := Decode(e, b)
	assert.Nil(t, err)
	assert.Equal(t, m, m2)
	assert.Equal(t, `{"t":"message","m":"hello, world"}`, m.String())
	_, err = Decode([]byte("not pass"), b)
	assert.NotNil(t, err)
	_, err = Encode([]byte("0"), m)
	assert.NotNil(t, err)
}

func TestMessageNoPass(t *testing.T) {
	log.SetLevel("debug")
	m := Message{Type: TypeMessage, Message: "hello, world"}
	b, err := Encode(nil, m)
	assert.Nil(t, err)
	fmt.Printf("%x\n", b)

	m2, err := Decode(nil, b)
	assert.Nil(t, err)
	assert.Equal(t, m, m2)
	assert.Equal(t, `{"t":"message","m":"hello, world"}`, m.String())
}

func TestSend(t *testing.T) {
	token := make([]byte, 40000000)
	rand.Read(token)

	port := "8801"
	go func() {
		log.Debug("starting TCP server on " + port)
		server, err := net.Listen("tcp", "0.0.0.0:"+port)
		if err != nil {
			log.Error(err)
		}
		defer server.Close()
		// spawn a new goroutine whenever a client connects
		for {
			connection, err := server.Accept()
			if err != nil {
				log.Error(err)
			}
			log.Debugf("client %s connected", connection.RemoteAddr().String())
			go func(_ string, connection net.Conn) {
				c := comm.New(connection)
				err = c.Send([]byte("hello, world"))
				assert.Nil(t, err)
				data, err := c.Receive()
				assert.Nil(t, err)
				assert.Equal(t, []byte("hello, computer"), data)
				data, err = c.Receive()
				assert.Nil(t, err)
				assert.Equal(t, []byte{'\x00'}, data)
				data, err = c.Receive()
				assert.Nil(t, err)
				assert.Equal(t, token, data)
			}(port, connection)
		}
	}()

	time.Sleep(800 * time.Millisecond)
	a, err := comm.NewConnection("127.0.0.1:"+port, 10*time.Minute)
	assert.Nil(t, err)
	m := Message{Type: TypeMessage, Message: "hello, world"}
	e, salt, err := crypt.New([]byte("pass"), nil)
	log.Debug(salt)
	assert.Nil(t, err)

	assert.Nil(t, Send(a, e, m))
}
```

## File: `src/mnemonicode/mnemonicode.go`
```go
// From GitHub version/fork maintained by Stephen Paul Weber available at:
// https://github.com/singpolyma/mnemonicode
//
// Originally from:
// http://web.archive.org/web/20101031205747/http://www.tothink.com/mnemonic/

/*
 Copyright (c) 2000  Oren Tirosh <oren@hishome.net>

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
*/

package mnemonicode

const base = 1626

// WordsRequired returns the number of words required to encode input
// data of length bytes using mnomonic encoding.
//
// Every four bytes of input is encoded into three words. If there
// is an extra one or two bytes they get an extra one or two words
// respectively. If there is an extra three bytes, they will be encoded
// into three words with the last word being one of a small set of very
// short words (only needed to encode the last 3 bits).
func WordsRequired(length int) int {
	return ((length + 1) * 3) / 4
}

// EncodeWordList encodes src into mnemomic words which are appended to dst.
// The final wordlist is returned.
// There will be WordsRequired(len(src)) words appended.
func EncodeWordList(dst []string, src []byte) (result []string) {
	if n := len(dst) + WordsRequired(len(src)); cap(dst) < n {
		result = make([]string, len(dst), n)
		copy(result, dst)
	} else {
		result = dst
	}

	var x uint32
	for len(src) >= 4 {
		x = uint32(src[0])
		x |= uint32(src[1]) << 8
		x |= uint32(src[2]) << 16
		x |= uint32(src[3]) << 24
		src = src[4:]

		i0 := int(x % base)
		i1 := int(x/base) % base
		i2 := int(x/base/base) % base
		result = append(result, WordList[i0], WordList[i1], WordList[i2])
	}
	if len(src) > 0 {
		x = 0
		for i := len(src) - 1; i >= 0; i-- {
			x <<= 8
			x |= uint32(src[i])
		}
		i := int(x % base)
		result = append(result, WordList[i])
		if len(src) >= 2 {
			i = int(x/base) % base
			result = append(result, WordList[i])
		}
		if len(src) == 3 {
			i = base + int(x/base/base)%7
			result = append(result, WordList[i])
		}
	}

	return result
}
```

## File: `src/mnemonicode/mnemonicode_test.go`
```go
package mnemonicode

import (
	"testing"
)

func TestWordsRequired(t *testing.T) {
	tests := []struct {
		name   string
		length int
		want   int
	}{
		{"empty", 0, 0},
		{"1 byte", 1, 1},
		{"2 bytes", 2, 2},
		{"3 bytes", 3, 3},
		{"4 bytes", 4, 3},
		{"5 bytes", 5, 4},
		{"8 bytes", 8, 6},
		{"12 bytes", 12, 9},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := WordsRequired(tt.length); got != tt.want {
				t.Errorf("WordsRequired(%d) = %d, want %d", tt.length, got, tt.want)
			}
		})
	}
}

func TestEncodeWordList(t *testing.T) {
	tests := []struct {
		name string
		dst  []string
		src  []byte
		want int
	}{
		{
			name: "empty input",
			dst:  []string{},
			src:  []byte{},
			want: 0,
		},
		{
			name: "single byte",
			dst:  []string{},
			src:  []byte{0x01},
			want: 1,
		},
		{
			name: "two bytes",
			dst:  []string{},
			src:  []byte{0x01, 0x02},
			want: 2,
		},
		{
			name: "three bytes",
			dst:  []string{},
			src:  []byte{0x01, 0x02, 0x03},
			want: 3,
		},
		{
			name: "four bytes",
			dst:  []string{},
			src:  []byte{0x01, 0x02, 0x03, 0x04},
			want: 3,
		},
		{
			name: "eight bytes",
			dst:  []string{},
			src:  []byte{0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08},
			want: 6,
		},
		{
			name: "with existing dst",
			dst:  []string{"existing"},
			src:  []byte{0x01},
			want: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := EncodeWordList(tt.dst, tt.src)
			if len(result) != tt.want {
				t.Errorf("EncodeWordList() returned %d words, want %d", len(result), tt.want)
			}
			
			// Check that all words are valid
			for i, word := range result {
				if word == "" {
					t.Errorf("EncodeWordList() returned empty word at index %d", i)
				}
			}
		})
	}
}

func TestEncodeWordListConsistency(t *testing.T) {
	input := []byte{0x12, 0x34, 0x56, 0x78}
	
	// Encode twice with empty dst
	result1 := EncodeWordList([]string{}, input)
	result2 := EncodeWordList([]string{}, input)
	
	if len(result1) != len(result2) {
		t.Errorf("Inconsistent result lengths: %d vs %d", len(result1), len(result2))
	}
	
	for i := range result1 {
		if result1[i] != result2[i] {
			t.Errorf("Inconsistent result at index %d: %s vs %s", i, result1[i], result2[i])
		}
	}
}

func TestEncodeWordListCapacityHandling(t *testing.T) {
	// Test with dst that has sufficient capacity
	dst := make([]string, 1, 10)
	dst[0] = "existing"
	input := []byte{0x01, 0x02}
	
	result := EncodeWordList(dst, input)
	
	if len(result) != 3 { // 1 existing + 2 new
		t.Errorf("Expected 3 words, got %d", len(result))
	}
	
	if result[0] != "existing" {
		t.Errorf("Expected first word to be 'existing', got %s", result[0])
	}
}

func TestEncodeWordListBoundaryValues(t *testing.T) {
	tests := []struct {
		name string
		src  []byte
	}{
		{"max single byte", []byte{0xFF}},
		{"max two bytes", []byte{0xFF, 0xFF}},
		{"max three bytes", []byte{0xFF, 0xFF, 0xFF}},
		{"max four bytes", []byte{0xFF, 0xFF, 0xFF, 0xFF}},
		{"all zeros", []byte{0x00, 0x00, 0x00, 0x00}},
	}
	
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := EncodeWordList([]string{}, tt.src)
			expectedLen := WordsRequired(len(tt.src))
			
			if len(result) != expectedLen {
				t.Errorf("Expected %d words, got %d", expectedLen, len(result))
			}
			
			// Ensure all words are from the WordList
			for _, word := range result {
				found := false
				for _, validWord := range WordList {
					if word == validWord {
						found = true
						break
					}
				}
				if !found {
					t.Errorf("Invalid word generated: %s", word)
				}
			}
		})
	}
}
```

## File: `src/mnemonicode/wordlist.go`
```go
// From GitHub version/fork maintained by Stephen Paul Weber available at:
// https://github.com/singpolyma/mnemonicode
//
// Originally from:
// http://web.archive.org/web/20101031205747/http://www.tothink.com/mnemonic/

/*
Copyright (c) 2000  Oren Tirosh <oren@hishome.net>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/

package mnemonicode

// WordListVersion is the version of compiled in word list.
const WordListVersion = "0.7"

var wordMap = make(map[string]int, len(WordList))

func init() {
	for i, w := range WordList {
		wordMap[w] = i
	}
}

const longestWord = 7

var WordList = []string{
	"academy", "acrobat", "active", "actor", "adam", "admiral",
	"adrian", "africa", "agenda", "agent", "airline", "airport",
	"aladdin", "alarm", "alaska", "albert", "albino", "album",
	"alcohol", "alex", "algebra", "alibi", "alice", "alien",
	"alpha", "alpine", "amadeus", "amanda", "amazon", "amber",
	"america", "amigo", "analog", "anatomy", "angel", "animal",
	"antenna", "antonio", "apollo", "april", "archive", "arctic",
	"arizona", "arnold", "aroma", "arthur", "artist", "asia",
	"aspect", "aspirin", "athena", "athlete", "atlas", "audio",
	"august", "austria", "axiom", "aztec", "balance", "ballad",
	"banana", "bandit", "banjo", "barcode", "baron", "basic",
	"battery", "belgium", "berlin", "bermuda", "bernard", "bikini",
	"binary", "bingo", "biology", "block", "blonde", "bonus",
	"boris", "boston", "boxer", "brandy", "bravo", "brazil",
	"bronze", "brown", "bruce", "bruno", "burger", "burma",
	"cabinet", "cactus", "cafe", "cairo", "cake", "calypso",
	"camel", "camera", "campus", "canada", "canal", "cannon",
	"canoe", "cantina", "canvas", "canyon", "capital", "caramel",
	"caravan", "carbon", "cargo", "carlo", "carol", "carpet",
	"cartel", "casino", "castle", "castro", "catalog", "caviar",
	"cecilia", "cement", "center", "century", "ceramic", "chamber",
	"chance", "change", "chaos", "charlie", "charm", "charter",
	"chef", "chemist", "cherry", "chess", "chicago", "chicken",
	"chief", "china", "cigar", "cinema", "circus", "citizen",
	"city", "clara", "classic", "claudia", "clean", "client",
	"climax", "clinic", "clock", "club", "cobra", "coconut",
	"cola", "collect", "colombo", "colony", "color", "combat",
	"comedy", "comet", "command", "compact", "company", "complex",
	"concept", "concert", "connect", "consul", "contact", "context",
	"contour", "control", "convert", "copy", "corner", "corona",
	"correct", "cosmos", "couple", "courage", "cowboy", "craft",
	"crash", "credit", "cricket", "critic", "crown", "crystal",
	"cuba", "culture", "dallas", "dance", "daniel", "david",
	"decade", "decimal", "deliver", "delta", "deluxe", "demand",
	"demo", "denmark", "derby", "design", "detect", "develop",
	"diagram", "dialog", "diamond", "diana", "diego", "diesel",
	"diet", "digital", "dilemma", "diploma", "direct", "disco",
	"disney", "distant", "doctor", "dollar", "dominic", "domino",
	"donald", "dragon", "drama", "dublin", "duet", "dynamic",
	"east", "ecology", "economy", "edgar", "egypt", "elastic",
	"elegant", "element", "elite", "elvis", "email", "energy",
	"engine", "english", "episode", "equator", "escort", "ethnic",
	"europe", "everest", "evident", "exact", "example", "exit",
	"exotic", "export", "express", "extra", "fabric", "factor",
	"falcon", "family", "fantasy", "fashion", "fiber", "fiction",
	"fidel", "fiesta", "figure", "film", "filter", "final",
	"finance", "finish", "finland", "flash", "florida", "flower",
	"fluid", "flute", "focus", "ford", "forest", "formal",
	"format", "formula", "fortune", "forum", "fragile", "france",
	"frank", "friend", "frozen", "future", "gabriel", "galaxy",
	"gallery", "gamma", "garage", "garden", "garlic", "gemini",
	"general", "genetic", "genius", "germany", "global", "gloria",
	"golf", "gondola", "gong", "good", "gordon", "gorilla",
	"grand", "granite", "graph", "green", "group", "guide",
	"guitar", "guru", "hand", "happy", "harbor", "harmony",
	"harvard", "havana", "hawaii", "helena", "hello", "henry",
	"hilton", "history", "horizon", "hotel", "human", "humor",
	"icon", "idea", "igloo", "igor", "image", "impact",
	"import", "index", "india", "indigo", "input", "insect",
	"instant", "iris", "italian", "jacket", "jacob", "jaguar",
	"janet", "japan", "jargon", "jazz", "jeep", "john",
	"joker", "jordan", "jumbo", "june", "jungle", "junior",
	"jupiter", "karate", "karma", "kayak", "kermit", "kilo",
	"king", "koala", "korea", "labor", "lady", "lagoon",
	"laptop", "laser", "latin", "lava", "lecture", "left",
	"legal", "lemon", "level", "lexicon", "liberal", "libra",
	"limbo", "limit", "linda", "linear", "lion", "liquid",
	"liter", "little", "llama", "lobby", "lobster", "local",
	"logic", "logo", "lola", "london", "lotus", "lucas",
	"lunar", "machine", "macro", "madam", "madonna", "madrid",
	"maestro", "magic", "magnet", "magnum", "major", "mama",
	"mambo", "manager", "mango", "manila", "marco", "marina",
	"market", "mars", "martin", "marvin", "master", "matrix",
	"maximum", "media", "medical", "mega", "melody", "melon",
	"memo", "mental", "mentor", "menu", "mercury", "message",
	"metal", "meteor", "meter", "method", "metro", "mexico",
	"miami", "micro", "million", "mineral", "minimum", "minus",
	"minute", "miracle", "mirage", "miranda", "mister", "mixer",
	"mobile", "model", "modem", "modern", "modular", "moment",
	"monaco", "monica", "monitor", "mono", "monster", "montana",
	"morgan", "motel", "motif", "motor", "mozart", "multi",
	"museum", "music", "mustang", "natural", "neon", "nepal",
	"neptune", "nerve", "neutral", "nevada", "news", "ninja",
	"nirvana", "normal", "nova", "novel", "nuclear", "numeric",
	"nylon", "oasis", "object", "observe", "ocean", "octopus",
	"olivia", "olympic", "omega", "opera", "optic", "optimal",
	"orange", "orbit", "organic", "orient", "origin", "orlando",
	"oscar", "oxford", "oxygen", "ozone", "pablo", "pacific",
	"pagoda", "palace", "pamela", "panama", "panda", "panel",
	"panic", "paradox", "pardon", "paris", "parker", "parking",
	"parody", "partner", "passage", "passive", "pasta", "pastel",
	"patent", "patriot", "patrol", "patron", "pegasus", "pelican",
	"penguin", "pepper", "percent", "perfect", "perfume", "period",
	"permit", "person", "peru", "phone", "photo", "piano",
	"picasso", "picnic", "picture", "pigment", "pilgrim", "pilot",
	"pirate", "pixel", "pizza", "planet", "plasma", "plaster",
	"plastic", "plaza", "pocket", "poem", "poetic", "poker",
	"polaris", "police", "politic", "polo", "polygon", "pony",
	"popcorn", "popular", "postage", "postal", "precise", "prefix",
	"premium", "present", "price", "prince", "printer", "prism",
	"private", "product", "profile", "program", "project", "protect",
	"proton", "public", "pulse", "puma", "pyramid", "queen",
	"radar", "radio", "random", "rapid", "rebel", "record",
	"recycle", "reflex", "reform", "regard", "regular", "relax",
	"report", "reptile", "reverse", "ricardo", "ringo", "ritual",
	"robert", "robot", "rocket", "rodeo", "romeo", "royal",
	"russian", "safari", "salad", "salami", "salmon", "salon",
	"salute", "samba", "sandra", "santana", "sardine", "school",
	"screen", "script", "second", "secret", "section", "segment",
	"select", "seminar", "senator", "senior", "sensor", "serial",
	"service", "sheriff", "shock", "sierra", "signal", "silicon",
	"silver", "similar", "simon", "single", "siren", "slogan",
	"social", "soda", "solar", "solid", "solo", "sonic",
	"soviet", "special", "speed", "spiral", "spirit", "sport",
	"static", "station", "status", "stereo", "stone", "stop",
	"street", "strong", "student", "studio", "style", "subject",
	"sultan", "super", "susan", "sushi", "suzuki", "switch",
	"symbol", "system", "tactic", "tahiti", "talent", "tango",
	"tarzan", "taxi", "telex", "tempo", "tennis", "texas",
	"textile", "theory", "thermos", "tiger", "titanic", "tokyo",
	"tomato", "topic", "tornado", "toronto", "torpedo", "total",
	"totem", "tourist", "tractor", "traffic", "transit", "trapeze",
	"travel", "tribal", "trick", "trident", "trilogy", "tripod",
	"tropic", "trumpet", "tulip", "tuna", "turbo", "twist",
	"ultra", "uniform", "union", "uranium", "vacuum", "valid",
	"vampire", "vanilla", "vatican", "velvet", "ventura", "venus",
	"vertigo", "veteran", "victor", "video", "vienna", "viking",
	"village", "vincent", "violet", "violin", "virtual", "virus",
	"visa", "vision", "visitor", "visual", "vitamin", "viva",
	"vocal", "vodka", "volcano", "voltage", "volume", "voyage",
	"water", "weekend", "welcome", "western", "window", "winter",
	"wizard", "wolf", "world", "xray", "yankee", "yoga",
	"yogurt", "yoyo", "zebra", "zero", "zigzag", "zipper",
	"zodiac", "zoom", "abraham", "action", "address", "alabama",
	"alfred", "almond", "ammonia", "analyze", "annual", "answer",
	"apple", "arena", "armada", "arsenal", "atlanta", "atomic",
	"avenue", "average", "bagel", "baker", "ballet", "bambino",
	"bamboo", "barbara", "basket", "bazaar", "benefit", "bicycle",
	"bishop", "blitz", "bonjour", "bottle", "bridge", "british",
	"brother", "brush", "budget", "cabaret", "cadet", "candle",
	"capitan", "capsule", "career", "cartoon", "channel", "chapter",
	"cheese", "circle", "cobalt", "cockpit", "college", "compass",
	"comrade", "condor", "crimson", "cyclone", "darwin", "declare",
	"degree", "delete", "delphi", "denver", "desert", "divide",
	"dolby", "domain", "domingo", "double", "drink", "driver",
	"eagle", "earth", "echo", "eclipse", "editor", "educate",
	"edward", "effect", "electra", "emerald", "emotion", "empire",
	"empty", "escape", "eternal", "evening", "exhibit", "expand",
	"explore", "extreme", "ferrari", "first", "flag", "folio",
	"forget", "forward", "freedom", "fresh", "friday", "fuji",
	"galileo", "garcia", "genesis", "gold", "gravity", "habitat",
	"hamlet", "harlem", "helium", "holiday", "house", "hunter",
	"ibiza", "iceberg", "imagine", "infant", "isotope", "jackson",
	"jamaica", "jasmine", "java", "jessica", "judo", "kitchen",
	"lazarus", "letter", "license", "lithium", "loyal", "lucky",
	"magenta", "mailbox", "manual", "marble", "mary", "maxwell",
	"mayor", "milk", "monarch", "monday", "money", "morning",
	"mother", "mystery", "native", "nectar", "nelson", "network",
	"next", "nikita", "nobel", "nobody", "nominal", "norway",
	"nothing", "number", "october", "office", "oliver", "opinion",
	"option", "order", "outside", "package", "pancake", "pandora",
	"panther", "papa", "patient", "pattern", "pedro", "pencil",
	"people", "phantom", "philips", "pioneer", "pluto", "podium",
	"portal", "potato", "prize", "process", "protein", "proxy",
	"pump", "pupil", "python", "quality", "quarter", "quiet",
	"rabbit", "radical", "radius", "rainbow", "ralph", "ramirez",
	"ravioli", "raymond", "respect", "respond", "result", "resume",
	"retro", "richard", "right", "risk", "river", "roger",
	"roman", "rondo", "sabrina", "salary", "salsa", "sample",
	"samuel", "saturn", "savage", "scarlet", "scoop", "scorpio",
	"scratch", "scroll", "sector", "serpent", "shadow", "shampoo",
	"sharon", "sharp", "short", "shrink", "silence", "silk",
	"simple", "slang", "smart", "smoke", "snake", "society",
	"sonar", "sonata", "soprano", "source", "sparta", "sphere",
	"spider", "sponsor", "spring", "acid", "adios", "agatha",
	"alamo", "alert", "almanac", "aloha", "andrea", "anita",
	"arcade", "aurora", "avalon", "baby", "baggage", "balloon",
	"bank", "basil", "begin", "biscuit", "blue", "bombay",
	"brain", "brenda", "brigade", "cable", "carmen", "cello",
	"celtic", "chariot", "chrome", "citrus", "civil", "cloud",
	"common", "compare", "cool", "copper", "coral", "crater",
	"cubic", "cupid", "cycle", "depend", "door", "dream",
	"dynasty", "edison", "edition", "enigma", "equal", "eric",
	"event", "evita", "exodus", "extend", "famous", "farmer",
	"food", "fossil", "frog", "fruit", "geneva", "gentle",
	"george", "giant", "gilbert", "gossip", "gram", "greek",
	"grille", "hammer", "harvest", "hazard", "heaven", "herbert",
	"heroic", "hexagon", "husband", "immune", "inca", "inch",
	"initial", "isabel", "ivory", "jason", "jerome", "joel",
	"joshua", "journal", "judge", "juliet", "jump", "justice",
	"kimono", "kinetic", "leonid", "lima", "maze", "medusa",
	"member", "memphis", "michael", "miguel", "milan", "mile",
	"miller", "mimic", "mimosa", "mission", "monkey", "moral",
	"moses", "mouse", "nancy", "natasha", "nebula", "nickel",
	"nina", "noise", "orchid", "oregano", "origami", "orinoco",
	"orion", "othello", "paper", "paprika", "prelude", "prepare",
	"pretend", "profit", "promise", "provide", "puzzle", "remote",
	"repair", "reply", "rival", "riviera", "robin", "rose",
	"rover", "rudolf", "saga", "sahara", "scholar", "shelter",
	"ship", "shoe", "sigma", "sister", "sleep", "smile",
	"spain", "spark", "split", "spray", "square", "stadium",
	"star", "storm", "story", "strange", "stretch", "stuart",
	"subway", "sugar", "sulfur", "summer", "survive", "sweet",
	"swim", "table", "taboo", "target", "teacher", "telecom",
	"temple", "tibet", "ticket", "tina", "today", "toga",
	"tommy", "tower", "trivial", "tunnel", "turtle", "twin",
	"uncle", "unicorn", "unique", "update", "valery", "vega",
	"version", "voodoo", "warning", "william", "wonder", "year",
	"yellow", "young", "absent", "absorb", "accent", "alfonso",
	"alias", "ambient", "andy", "anvil", "appear", "apropos",
	"archer", "ariel", "armor", "arrow", "austin", "avatar",
	"axis", "baboon", "bahama", "bali", "balsa", "bazooka",
	"beach", "beast", "beatles", "beauty", "before", "benny",
	"betty", "between", "beyond", "billy", "bison", "blast",
	"bless", "bogart", "bonanza", "book", "border", "brave",
	"bread", "break", "broken", "bucket", "buenos", "buffalo",
	"bundle", "button", "buzzer", "byte", "caesar", "camilla",
	"canary", "candid", "carrot", "cave", "chant", "child",
	"choice", "chris", "cipher", "clarion", "clark", "clever",
	"cliff", "clone", "conan", "conduct", "congo", "content",
	"costume", "cotton", "cover", "crack", "current", "danube",
	"data", "decide", "desire", "detail", "dexter", "dinner",
	"dispute", "donor", "druid", "drum", "easy", "eddie",
	"enjoy", "enrico", "epoxy", "erosion", "except", "exile",
	"explain", "fame", "fast", "father", "felix", "field",
	"fiona", "fire", "fish", "flame", "flex", "flipper",
	"float", "flood", "floor", "forbid", "forever", "fractal",
	"frame", "freddie", "front", "fuel", "gallop", "game",
	"garbo", "gate", "gibson", "ginger", "giraffe", "gizmo",
	"glass", "goblin", "gopher", "grace", "gray", "gregory",
	"grid", "griffin", "ground", "guest", "gustav", "gyro",
	"hair", "halt", "harris", "heart", "heavy", "herman",
	"hippie", "hobby", "honey", "hope", "horse", "hostel",
	"hydro", "imitate", "info", "ingrid", "inside", "invent",
	"invest", "invite", "iron", "ivan", "james", "jester",
	"jimmy", "join", "joseph", "juice", "julius", "july",
	"justin", "kansas", "karl", "kevin", "kiwi", "ladder",
	"lake", "laura", "learn", "legacy", "legend", "lesson",
	"life", "light", "list", "locate", "lopez", "lorenzo",
	"love", "lunch", "malta", "mammal", "margo", "marion",
	"mask", "match", "mayday", "meaning", "mercy", "middle",
	"mike", "mirror", "modest", "morph", "morris", "nadia",
	"nato", "navy", "needle", "neuron", "never", "newton",
	"nice", "night", "nissan", "nitro", "nixon", "north",
	"oberon", "octavia", "ohio", "olga", "open", "opus",
	"orca", "oval", "owner", "page", "paint", "palma",
	"parade", "parent", "parole", "paul", "peace", "pearl",
	"perform", "phoenix", "phrase", "pierre", "pinball", "place",
	"plate", "plato", "plume", "pogo", "point", "polite",
	"polka", "poncho", "powder", "prague", "press", "presto",
	"pretty", "prime", "promo", "quasi", "quest", "quick",
	"quiz", "quota", "race", "rachel", "raja", "ranger",
	"region", "remark", "rent", "reward", "rhino", "ribbon",
	"rider", "road", "rodent", "round", "rubber", "ruby",
	"rufus", "sabine", "saddle", "sailor", "saint", "salt",
	"satire", "scale", "scuba", "season", "secure", "shake",
	"shallow", "shannon", "shave", "shelf", "sherman", "shine",
	"shirt", "side", "sinatra", "sincere", "size", "slalom",
	"slow", "small", "snow", "sofia", "song", "sound",
	"south", "speech", "spell", "spend", "spoon", "stage",
	"stamp", "stand", "state", "stella", "stick", "sting",
	"stock", "store", "sunday", "sunset", "support", "sweden",
	"swing", "tape", "think", "thomas", "tictac", "time",
	"toast", "tobacco", "tonight", "torch", "torso", "touch",
	"toyota", "trade", "tribune", "trinity", "triton", "truck",
	"trust", "type", "under", "unit", "urban", "urgent",
	"user", "value", "vendor", "venice", "verona", "vibrate",
	"virgo", "visible", "vista", "vital", "voice", "vortex",
	"waiter", "watch", "wave", "weather", "wedding", "wheel",
	"whiskey", "wisdom", "deal", "null", "nurse", "quebec",
	"reserve", "reunion", "roof", "singer", "verbal", "amen",
	"ego", "fax", "jet", "job", "rio", "ski",
	"yes",
}
```

## File: `src/models/constants.go`
```go
package models

import (
	"context"
	"fmt"
	"net"
	"os"
	"path"
	"time"

	"github.com/schollz/croc/v10/src/utils"
	log "github.com/schollz/logger"
)

// TCP_BUFFER_SIZE is the maximum packet size
const TCP_BUFFER_SIZE = 1024 * 64

// DEFAULT_RELAY is the default relay used (can be set using --relay)
var (
	DEFAULT_RELAY      = "croc.schollz.com"
	DEFAULT_RELAY6     = "croc6.schollz.com"
	DEFAULT_PORT       = "9009"
	DEFAULT_PASSPHRASE = "pass123"
	INTERNAL_DNS       = false
)

// publicDNS are servers to be queried if a local lookup fails
var publicDNS = []string{
	"1.0.0.1",                // Cloudflare
	"1.1.1.1",                // Cloudflare
	"[2606:4700:4700::1111]", // Cloudflare
	"[2606:4700:4700::1001]", // Cloudflare
	"8.8.4.4",                // Google
	"8.8.8.8",                // Google
	"[2001:4860:4860::8844]", // Google
	"[2001:4860:4860::8888]", // Google
	"9.9.9.9",                // Quad9
	"149.112.112.112",        // Quad9
	"[2620:fe::fe]",          // Quad9
	"[2620:fe::fe:9]",        // Quad9
	"8.26.56.26",             // Comodo
	"8.20.247.20",            // Comodo
	"208.67.220.220",         // Cisco OpenDNS
	"208.67.222.222",         // Cisco OpenDNS
	"[2620:119:35::35]",      // Cisco OpenDNS
	"[2620:119:53::53]",      // Cisco OpenDNS
}

func getConfigFile(requireValidPath bool) (fname string, err error) {
	configFile, err := utils.GetConfigDir(requireValidPath)
	if err != nil {
		return
	}
	fname = path.Join(configFile, "internal-dns")
	return
}

func init() {
	log.SetLevel("info")
	log.SetOutput(os.Stderr)
	doRemember := false
	for _, flag := range os.Args {
		if flag == "--internal-dns" {
			INTERNAL_DNS = true
			break
		}
		if flag == "--remember" {
			doRemember = true
		}
	}
	if doRemember {
		// save in config file
		fname, err := getConfigFile(true)
		if err == nil {
			f, _ := os.Create(fname)
			f.Close()
		}
	}
	if !INTERNAL_DNS {
		fname, err := getConfigFile(false)
		if err == nil {
			INTERNAL_DNS = utils.Exists(fname)
		}
	}
	log.Trace("Using internal DNS: ", INTERNAL_DNS)
	var err error
	var addr string
	addr, err = lookup(DEFAULT_RELAY)
	if err == nil {
		DEFAULT_RELAY = net.JoinHostPort(addr, DEFAULT_PORT)
	} else {
		DEFAULT_RELAY = ""
	}
	log.Tracef("Default ipv4 relay: %s", addr)
	addr, err = lookup(DEFAULT_RELAY6)
	if err == nil {
		DEFAULT_RELAY6 = net.JoinHostPort(addr, DEFAULT_PORT)
	} else {
		DEFAULT_RELAY6 = ""
	}
	log.Tracef("Default ipv6 relay: %s", addr)
}

// Resolve a hostname to an IP address using DNS.
func lookup(address string) (ipaddress string, err error) {
	if !INTERNAL_DNS {
		log.Tracef("Using local DNS to resolve %s", address)
		return localLookupIP(address)
	}
	type Result struct {
		s   string
		err error
	}
	result := make(chan Result, len(publicDNS))
	for _, dns := range publicDNS {
		go func(dns string) {
			var r Result
			r.s, r.err = remoteLookupIP(address, dns)
			log.Tracef("Resolved %s to %s using %s", address, r.s, dns)
			result <- r
		}(dns)
	}
	for i := 0; i < len(publicDNS); i++ {
		ipaddress = (<-result).s
		log.Tracef("Resolved %s to %s", address, ipaddress)
		if ipaddress != "" {
			return
		}
	}
	err = fmt.Errorf("failed to resolve %s: all DNS servers exhausted", address)
	return
}

// localLookupIP returns a host's IP address using the local DNS configuration.
func localLookupIP(address string) (ipaddress string, err error) {
	// Create a context with a 500 millisecond timeout
	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()

	r := &net.Resolver{}

	// Use the context with timeout in the LookupHost function
	ip, err := r.LookupHost(ctx, address)
	if err != nil {
		return
	}
	ipaddress = ip[0]
	return
}

// remoteLookupIP returns a host's IP address based on a remote DNS server.
func remoteLookupIP(address, dns string) (ipaddress string, err error) {
	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()

	r := &net.Resolver{
		PreferGo: true,
		Dial: func(ctx context.Context, network, _ string) (net.Conn, error) {
			d := new(net.Dialer)
			return d.DialContext(ctx, network, dns+":53")
		},
	}
	ip, err := r.LookupHost(ctx, address)
	if err != nil {
		return
	}
	ipaddress = ip[0]
	return
}
```

## File: `src/models/models_test.go`
```go
package models

import (
	"net"
	"strings"
	"testing"
	"time"
)

func TestConstants(t *testing.T) {
	if TCP_BUFFER_SIZE != 1024*64 {
		t.Errorf("TCP_BUFFER_SIZE = %d, want %d", TCP_BUFFER_SIZE, 1024*64)
	}

	if DEFAULT_PORT != "9009" {
		t.Errorf("DEFAULT_PORT = %s, want %s", DEFAULT_PORT, "9009")
	}

	if DEFAULT_PASSPHRASE != "pass123" {
		t.Errorf("DEFAULT_PASSPHRASE = %s, want %s", DEFAULT_PASSPHRASE, "pass123")
	}
}

func TestPublicDNSServers(t *testing.T) {
	if len(publicDNS) == 0 {
		t.Error("publicDNS list should not be empty")
	}

	// Check that we have both IPv4 and IPv6 servers
	hasIPv4 := false
	hasIPv6 := false

	for _, dns := range publicDNS {
		if strings.Contains(dns, "[") {
			hasIPv6 = true
		} else {
			hasIPv4 = true
		}
	}

	if !hasIPv4 {
		t.Error("publicDNS should contain IPv4 servers")
	}

	if !hasIPv6 {
		t.Error("publicDNS should contain IPv6 servers")
	}

	// Verify known DNS servers are present
	expectedServers := []string{
		"1.1.1.1",        // Cloudflare
		"8.8.8.8",        // Google
		"9.9.9.9",        // Quad9
		"208.67.220.220", // OpenDNS
	}

	for _, expected := range expectedServers {
		found := false
		for _, dns := range publicDNS {
			if dns == expected {
				found = true
				break
			}
		}
		if !found {
			t.Errorf("Expected DNS server %s not found in publicDNS", expected)
		}
	}
}

func TestLocalLookupIP(t *testing.T) {
	tests := []struct {
		name    string
		address string
		wantErr bool
	}{
		{
			name:    "localhost",
			address: "localhost",
			wantErr: false,
		},
		{
			name:    "invalid hostname",
			address: "this-hostname-should-not-exist-12345",
			wantErr: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			ip, err := localLookupIP(tt.address)

			if (err != nil) != tt.wantErr {
				t.Errorf("localLookupIP() error = %v, wantErr %v", err, tt.wantErr)
				return
			}

			if !tt.wantErr && ip == "" {
				t.Error("localLookupIP() returned empty IP for valid hostname")
			}

			if !tt.wantErr {
				// Verify it's a valid IP address
				if net.ParseIP(ip) == nil {
					t.Errorf("localLookupIP() returned invalid IP: %s", ip)
				}
			}
		})
	}
}

func TestRemoteLookupIPTimeout(t *testing.T) {
	// Test with an invalid DNS server that should timeout
	start := time.Now()
	_, err := remoteLookupIP("example.com", "192.0.2.1")
	duration := time.Since(start)

	// Should timeout within reasonable time (we set 500ms timeout)
	if duration > time.Second {
		t.Errorf("remoteLookupIP took too long: %v", duration)
	}

	if err == nil {
		t.Error("remoteLookupIP should have failed with invalid DNS server")
	}
}

func TestLookupFunction(t *testing.T) {
	// Test the main lookup function
	tests := []struct {
		name    string
		address string
		wantErr bool
	}{
		{
			name:    "localhost",
			address: "localhost",
			wantErr: false,
		},
		{
			name:    "invalid hostname",
			address: "this-hostname-should-definitely-not-exist-98765",
			wantErr: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			ip, err := lookup(tt.address)

			if (err != nil) != tt.wantErr {
				t.Errorf("lookup() error = %v, wantErr %v", err, tt.wantErr)
				return
			}

			if !tt.wantErr && ip == "" {
				t.Error("lookup() returned empty IP for valid hostname")
			}

			if !tt.wantErr {
				// Verify it's a valid IP address
				if net.ParseIP(ip) == nil {
					t.Errorf("lookup() returned invalid IP: %s", ip)
				}
			}
		})
	}
}

func TestGetConfigFile(t *testing.T) {
	fname, err := getConfigFile(false)
	if err != nil {
		t.Skip("Could not get config directory")
	}

	if !strings.HasSuffix(fname, "internal-dns") {
		t.Errorf("Expected config file to end with 'internal-dns', got %s", fname)
	}
}
```

## File: `src/tcp/ctx.go`
```go
// ctx.go
package tcp

import (
	"context"
	"errors"
	"net"
	"sync"

	log "github.com/schollz/logger"
)

// stop manages graceful shutdown of the TCP server
type stop struct {
	ctx    context.Context
	cancel context.CancelFunc
	// Track connections
	server net.Listener
	wg     sync.WaitGroup
	gui    bool
}

// newStop creates a new stop manager
func newStop(ctx context.Context) *stop {
	s := &stop{}
	if ctx == nil {
		ctx = context.Background()
	}
	s.ctx, s.cancel = context.WithCancel(ctx)

	return s
}

// Cancel initiate graceful shutdown
func (s *stop) Cancel() {
	log.Trace("tcp Cancel")
	if s.cancel != nil {
		s.cancel()
		s.cancel = nil
	}
}

func RunCtx(ctx context.Context, debugLevel, host, port, password string, banner ...string) error {
	return RunWithOptionsAsync(host, port, password, WithBanner(banner...), WithLogLevel(debugLevel), WithCtx(ctx))
}

func WithCtx(ctx context.Context) serverOptsFunc {
	return func(s *server) error {
		if s.stop.cancel != nil {
			s.stop.cancel()
		}
		s.stop = newStop(ctx)
		s.stop.gui = true
		return nil
	}
}

// Ignore context cancellation error
func Ignore(err error) error {
	if err != nil && (errors.Is(err, context.Canceled) ||
		errors.Is(err, context.DeadlineExceeded) ||
		// ignore Listener closed during cancellation
		// strings.Contains(err.Error(), "use of closed network connection") ||
		errors.Is(err, net.ErrClosed)) {
		log.Tracef("ignored: %v", err)
		return nil
	}
	return err
}
```

## File: `src/tcp/defaults.go`
```go
package tcp

import "time"

const (
	DEFAULT_LOG_LEVEL             = "debug"
	DEFAULT_ROOM_CLEANUP_INTERVAL = 10 * time.Minute
	DEFAULT_ROOM_TTL              = 3 * time.Hour
)
```

## File: `src/tcp/options.go`
```go
package tcp

import (
	"fmt"
	"time"
)

// TODO: maybe export from logger library?
var availableLogLevels = []string{"info", "error", "warn", "debug", "trace"}

type serverOptsFunc func(s *server) error

func WithBanner(banner ...string) serverOptsFunc {
	return func(s *server) error {
		if len(banner) > 0 {
			s.banner = banner[0]
		}
		return nil
	}
}

func WithLogLevel(level string) serverOptsFunc {
	return func(s *server) error {
		if !containsSlice(availableLogLevels, level) {
			return fmt.Errorf("invalid log level specified: %s", level)
		}
		s.debugLevel = level
		return nil
	}
}

func WithRoomCleanupInterval(interval time.Duration) serverOptsFunc {
	return func(s *server) error {
		s.roomCleanupInterval = interval
		return nil
	}
}

func WithRoomTTL(ttl time.Duration) serverOptsFunc {
	return func(s *server) error {
		s.roomTTL = ttl
		return nil
	}
}

func containsSlice(s []string, e string) bool {
	for _, ss := range s {
		if e == ss {
			return true
		}
	}
	return false
}
```

## File: `src/tcp/tcp.go`
```go
package tcp

import (
	"bytes"
	"context"
	"fmt"
	"net"
	"strings"
	"sync"
	"time"

	log "github.com/schollz/logger"
	"github.com/schollz/pake/v3"

	"github.com/schollz/croc/v10/src/comm"
	"github.com/schollz/croc/v10/src/crypt"
	"github.com/schollz/croc/v10/src/models"
)

type server struct {
	host       string
	port       string
	debugLevel string
	banner     string
	password   string
	rooms      roomMap

	roomCleanupInterval time.Duration
	roomTTL             time.Duration

	// stopRoomCleanup chan struct{}
	// replaced by stop ctx.go
	*stop
}

type roomInfo struct {
	first  *comm.Comm
	second *comm.Comm
	opened time.Time
	full   bool
}

type roomMap struct {
	rooms map[string]roomInfo
	sync.Mutex
}

const pingRoom = "pinglkasjdlfjsaldjf"

// newDefaultServer initializes a new server, with some default configuration options
func newDefaultServer() *server {
	s := new(server)
	s.roomCleanupInterval = DEFAULT_ROOM_CLEANUP_INTERVAL
	s.roomTTL = DEFAULT_ROOM_TTL
	s.debugLevel = DEFAULT_LOG_LEVEL
	// s.stopRoomCleanup = make(chan struct{}) replaced by stop
	s.stop = newStop(context.Background())
	return s
}

// RunWithOptionsAsync asynchronously starts a TCP listener.
func RunWithOptionsAsync(host, port, password string, opts ...serverOptsFunc) error {
	s := newDefaultServer()
	s.host = host
	s.port = port
	s.password = password
	for _, opt := range opts {
		err := opt(s)
		if err != nil {
			return fmt.Errorf("could not apply optional configurations: %w", err)
		}
	}
	return s.start()
}

// Run starts a tcp listener, run async
func Run(debugLevel, host, port, password string, banner ...string) (err error) {
	return RunWithOptionsAsync(host, port, password, WithBanner(banner...), WithLogLevel(debugLevel))
}

// Mask our password in logs
func maskedPassword(password string) (s string) {
	if len(password) > 2 {
		s = fmt.Sprintf("%c***%c", password[0], password[len(password)-1])
	} else {
		s = password
	}
	return
}

func (s *server) start() (err error) {
	log.SetLevel(s.debugLevel)

	log.Debugf("starting with password '%s'", maskedPassword(s.password))

	s.rooms.Lock()
	s.rooms.rooms = make(map[string]roomInfo)
	s.rooms.Unlock()

	s.stop.wg.Add(1)
	go func() {
		defer s.stop.wg.Done()
		s.deleteOldRooms()
	}()
	// defer s.stopRoomDeletion()
	defer s.stop.Cancel()
	if s.stop.gui {
		defer s.stop.wg.Wait()
	}

	err = s.run()
	err = Ignore(err)
	if err != nil {
		log.Error(err)
	}
	return
}

func (s *server) run() (err error) {
	network := "tcp"
	addr := net.JoinHostPort(s.host, s.port)
	if s.host != "" {
		ip := net.ParseIP(s.host)
		if ip == nil {
			var tcpIP *net.IPAddr
			tcpIP, err = net.ResolveIPAddr("ip", s.host)
			if err != nil {
				return err
			}
			ip = tcpIP.IP
		}
		addr = net.JoinHostPort(ip.String(), s.port)
		if ip.To4() != nil {
			network = "tcp4"
		} else {
			network = "tcp6"
		}

	}
	addr = strings.Replace(addr, "127.0.0.1", "0.0.0.0", 1)
	log.Infof("starting TCP server on %s", addr)
	lc := net.ListenConfig{}
	s.stop.server, err = lc.Listen(s.stop.ctx, network, addr)
	if err != nil {
		return fmt.Errorf("error listening on %s: %w", addr, err)
	}
	defer s.stop.server.Close()

	go func() {
		dc := &net.Dialer{
			Timeout: 100 * time.Millisecond,
		}
		if conn, err := dc.DialContext(s.stop.ctx, network, addr); err == nil {
			log.Debugf("started TCP server on %s", addr)
			conn.Close()
		} else {
			log.Errorf("started TCP server on %s : %v", addr, err)
			s.stop.Cancel()
		}
	}()

	// spawn a new goroutine whenever a client connects
	for {
		connection, err := s.stop.server.Accept()
		if err != nil {
			return fmt.Errorf("problem accepting connection: %w", err)
		}
		log.Debugf("client %s connected", connection.RemoteAddr().String())
		s.stop.wg.Add(1)
		go func(connection net.Conn) {
			defer s.stop.wg.Done()
			c := comm.New(connection)
			room, errCommunication := s.clientCommunication(c)
			log.Debugf("room: %+v", room)
			log.Debugf("err: %+v", errCommunication)
			if errCommunication != nil {
				log.Debugf("relay-%s: %s", connection.RemoteAddr().String(), errCommunication.Error())
				connection.Close()
				return
			}
			if room == pingRoom {
				log.Debugf("got ping")
				connection.Close()
				return
			}
			ticker := time.NewTicker(1 * time.Second)
			defer ticker.Stop()
			for {
				// check connection
				log.Tracef("checking connection of room %s for %+v", room, c)
				deleteIt := false
				s.rooms.Lock()
				roomData, ok := s.rooms.rooms[room]
				if !ok {
					log.Debug("room is gone")
					s.rooms.Unlock()
					return
				}
				log.Tracef("room: %+v", roomData)
				if roomData.first != nil && roomData.second != nil {
					log.Debug("rooms ready")
					s.rooms.Unlock()
					break
				}
				if roomData.first != nil {
					errSend := roomData.first.Send([]byte{1})
					if errSend != nil {
						log.Debug(errSend)
						deleteIt = true
					}
				}
				s.rooms.Unlock()
				if deleteIt {
					s.deleteRoom(room)
					break
				}
				select {
				case <-s.stop.ctx.Done():
					log.Tracef("check: %v", s.stop.ctx.Err())
					s.deleteRoom(room)
					return
				case <-ticker.C:
					// time.Sleep(1 * time.Second)
				}
			}
		}(connection)
	}
}

// deleteOldRooms checks for rooms at a regular interval and removes those that
// have exceeded their allocated TTL.
func (s *server) deleteOldRooms() {
	ticker := time.NewTicker(s.roomCleanupInterval)
	defer func() {
		ticker.Stop()
		log.Debug("room cleanup stopped")
	}()
	for next := true; next; {
		roomsToDelete := []string{}
		select {
		case <-ticker.C:
			s.rooms.Lock()
			for room, roomData := range s.rooms.rooms {
				if time.Since(roomData.opened) > s.roomTTL {
					roomsToDelete = append(roomsToDelete, room)
				}
			}
			s.rooms.Unlock()
		case <-s.stop.ctx.Done():
			if s.server != nil {
				log.Debugf("stop TCP server on %s", s.server.Addr())
				s.server.Close()
				time.Sleep(time.Millisecond)
			}
			log.Debug("stop room cleanup fired")
			s.rooms.Lock()
			for room := range s.rooms.rooms {
				roomsToDelete = append(roomsToDelete, room)
			}
			s.rooms.Unlock()
			next = false
		}
		for _, room := range roomsToDelete {
			s.deleteRoom(room)
			log.Debugf("room cleaned up: %s", room)
		}
	}
}

// replaced by stop
// func (s *server) stopRoomDeletion() {
// 	log.Debug("stop room cleanup fired")
// 	s.stopRoomCleanup <- struct{}{}
// }

var weakKey = []byte{1, 2, 3}

func (s *server) clientCommunication(c *comm.Comm) (room string, err error) {
	// establish secure password with PAKE for communication with relay
	B, err := pake.InitCurve(weakKey, 1, "siec")
	if err != nil {
		return
	}
	Abytes, err := c.Receive()
	if err != nil {
		return
	}
	log.Debugf("Abytes: %s", Abytes)
	if bytes.Equal(Abytes, []byte("ping")) {
		room = pingRoom
		log.Debug("sending back pong")
		c.Send([]byte("pong"))
		return
	}
	err = B.Update(Abytes)
	if err != nil {
		return
	}
	err = c.Send(B.Bytes())
	if err != nil {
		return
	}
	strongKey, err := B.SessionKey()
	if err != nil {
		return
	}
	log.Debugf("strongkey: %x", strongKey)

	// receive salt
	salt, err := c.Receive()
	if err != nil {
		return
	}
	strongKeyForEncryption, _, err := crypt.New(strongKey, salt)
	if err != nil {
		return
	}

	log.Debugf("waiting for password")
	passwordBytesEnc, err := c.Receive()
	if err != nil {
		return
	}
	passwordBytes, err := crypt.Decrypt(passwordBytesEnc, strongKeyForEncryption)
	if err != nil {
		return
	}
	if strings.TrimSpace(string(passwordBytes)) != s.password {
		err = fmt.Errorf("bad password")
		enc, _ := crypt.Encrypt([]byte(err.Error()), strongKeyForEncryption)
		if err = c.Send(enc); err != nil {
			return "", fmt.Errorf("send error: %w", err)
		}
		return
	}

	// send ok to tell client they are connected
	banner := s.banner
	if len(banner) == 0 {
		banner = "ok"
	}
	log.Debugf("sending '%s'", banner)
	bSend, err := crypt.Encrypt([]byte(banner+"|||"+c.Connection().RemoteAddr().String()), strongKeyForEncryption)
	if err != nil {
		return
	}
	err = c.Send(bSend)
	if err != nil {
		return
	}

	// wait for client to tell me which room they want
	log.Debug("waiting for answer")
	enc, err := c.Receive()
	if err != nil {
		return
	}
	roomBytes, err := crypt.Decrypt(enc, strongKeyForEncryption)
	if err != nil {
		return
	}
	room = string(roomBytes)

	s.rooms.Lock()
	// create the room if it is new
	if _, ok := s.rooms.rooms[room]; !ok {
		s.rooms.rooms[room] = roomInfo{
			first:  c,
			opened: time.Now(),
		}
		s.rooms.Unlock()
		// tell the client that they got the room

		bSend, err = crypt.Encrypt([]byte("ok"), strongKeyForEncryption)
		if err != nil {
			return
		}
		err = c.Send(bSend)
		if err != nil {
			log.Error(err)
			s.deleteRoom(room)
			return
		}
		log.Debugf("room %s has 1", room)
		return
	}
	if s.rooms.rooms[room].full {
		s.rooms.Unlock()
		bSend, err = crypt.Encrypt([]byte("room full"), strongKeyForEncryption)
		if err != nil {
			return
		}
		err = c.Send(bSend)
		if err != nil {
			log.Error(err)
			return
		}
		return
	}
	log.Debugf("room %s has 2", room)
	s.rooms.rooms[room] = roomInfo{
		first:  s.rooms.rooms[room].first,
		second: c,
		opened: s.rooms.rooms[room].opened,
		full:   true,
	}
	otherConnection := s.rooms.rooms[room].first
	s.rooms.Unlock()

	// second connection is the sender, time to staple connections
	var wg sync.WaitGroup
	wg.Add(1)

	// start piping
	go func(com1, com2 *comm.Comm, wg *sync.WaitGroup) {
		log.Debug("starting pipes")
		pipe(com1.Connection(), com2.Connection())
		wg.Done()
		log.Debug("done piping")
	}(otherConnection, c, &wg)

	// tell the sender everything is ready
	bSend, err = crypt.Encrypt([]byte("ok"), strongKeyForEncryption)
	if err != nil {
		return
	}
	err = c.Send(bSend)
	if err != nil {
		s.deleteRoom(room)
		return
	}
	wg.Wait()

	// delete room
	s.deleteRoom(room)
	return
}

func (s *server) deleteRoom(room string) {
	s.rooms.Lock()
	defer s.rooms.Unlock()
	roomData, ok := s.rooms.rooms[room]
	if !ok {
		return
	}
	log.Debugf("deleting room: %s", room)
	if roomData.first != nil {
		roomData.first.Close()
	}
	if roomData.second != nil {
		roomData.second.Close()
	}
	delete(s.rooms.rooms, room)
}

// chanFromConn creates a channel from a Conn object, and sends everything it
//
//	Read()s from the socket to the channel.
func chanFromConn(conn net.Conn) chan []byte {
	c := make(chan []byte, 1)
	if err := conn.SetReadDeadline(time.Now().Add(3 * time.Hour)); err != nil {
		log.Warnf("can't set read deadline: %v", err)
	}

	go func() {
		b := make([]byte, models.TCP_BUFFER_SIZE)
		for {
			n, err := conn.Read(b)
			if n > 0 {
				res := make([]byte, n)
				// Copy the buffer so it doesn't get changed while read by the recipient.
				copy(res, b[:n])
				c <- res
			}
			if err != nil {
				log.Debug(err)
				c <- nil
				break
			}
		}
		log.Debug("exiting")
	}()

	return c
}

// pipe creates a full-duplex pipe between the two sockets and
// transfers data from one to the other.
func pipe(conn1 net.Conn, conn2 net.Conn) {
	chan1 := chanFromConn(conn1)
	chan2 := chanFromConn(conn2)

	for {
		select {
		case b1 := <-chan1:
			if b1 == nil {
				return
			}
			if _, err := conn2.Write(b1); err != nil {
				log.Errorf("write error on channel 1: %v", err)
			}

		case b2 := <-chan2:
			if b2 == nil {
				return
			}
			if _, err := conn1.Write(b2); err != nil {
				log.Errorf("write error on channel 2: %v", err)
			}
		}
	}
}

func PingServer(address string) (err error) {
	log.Debugf("pinging %s", address)
	c, err := comm.NewConnection(address, 300*time.Millisecond)
	if err != nil {
		log.Debug(err)
		return
	}
	err = c.Send([]byte("ping"))
	if err != nil {
		log.Debug(err)
		return
	}
	b, err := c.Receive()
	if err != nil {
		log.Debug(err)
		return
	}
	if bytes.Equal(b, []byte("pong")) {
		return nil
	}
	return fmt.Errorf("no pong")
}

// ConnectToTCPServer will initiate a new connection
// to the specified address, room with optional time limit
func ConnectToTCPServer(address, password, room string, timelimit ...time.Duration) (c *comm.Comm, banner string, ipaddr string, err error) {
	if len(timelimit) > 0 {
		c, err = comm.NewConnection(address, timelimit[0])
	} else {
		c, err = comm.NewConnection(address)
	}
	if err != nil {
		log.Debug(err)
		return
	}

	// get PAKE connection with server to establish strong key to transfer info
	A, err := pake.InitCurve(weakKey, 0, "siec")
	if err != nil {
		log.Debug(err)
		return
	}
	err = c.Send(A.Bytes())
	if err != nil {
		log.Debug(err)
		return
	}
	Bbytes, err := c.Receive()
	if err != nil {
		log.Debug(err)
		return
	}
	err = A.Update(Bbytes)
	if err != nil {
		log.Debug(err)
		return
	}
	strongKey, err := A.SessionKey()
	if err != nil {
		log.Debug(err)
		return
	}
	log.Debugf("strong key: %x", strongKey)

	strongKeyForEncryption, salt, err := crypt.New(strongKey, nil)
	if err != nil {
		log.Debug(err)
		return
	}
	// send salt
	err = c.Send(salt)
	if err != nil {
		log.Debug(err)
		return
	}

	log.Debugf("sending password '%s'", maskedPassword(password))
	bSend, err := crypt.Encrypt([]byte(password), strongKeyForEncryption)
	if err != nil {
		log.Debug(err)
		return
	}
	err = c.Send(bSend)
	if err != nil {
		log.Debug(err)
		return
	}
	log.Debug("waiting for first ok")
	enc, err := c.Receive()
	if err != nil {
		log.Debug(err)
		return
	}
	data, err := crypt.Decrypt(enc, strongKeyForEncryption)
	if err != nil {
		log.Debug(err)
		return
	}
	if !strings.Contains(string(data), "|||") {
		err = fmt.Errorf("bad response: %s", string(data))
		log.Debug(err)
		return
	}
	banner = strings.Split(string(data), "|||")[0]
	ipaddr = strings.Split(string(data), "|||")[1]
	log.Debugf("sending room; %s", room)
	bSend, err = crypt.Encrypt([]byte(room), strongKeyForEncryption)
	if err != nil {
		log.Debug(err)
		return
	}
	err = c.Send(bSend)
	if err != nil {
		log.Debug(err)
		return
	}
	log.Debug("waiting for room confirmation")
	enc, err = c.Receive()
	if err != nil {
		log.Debug(err)
		return
	}
	data, err = crypt.Decrypt(enc, strongKeyForEncryption)
	if err != nil {
		log.Debug(err)
		return
	}
	if !bytes.Equal(data, []byte("ok")) {
		err = fmt.Errorf("got bad response: %s", data)
		log.Debug(err)
		return
	}
	log.Debug("all set")
	return
}
```

## File: `src/tcp/tcp_test.go`
```go
package tcp

import (
	"bytes"
	"context"
	"fmt"
	"testing"
	"time"

	log "github.com/schollz/logger"
	"github.com/stretchr/testify/assert"
)

func BenchmarkConnection(b *testing.B) {
	log.SetLevel("trace")
	go Run("debug", "127.0.0.1", "8283", "pass123", "8284")
	time.Sleep(100 * time.Millisecond)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		c, _, _, _ := ConnectToTCPServer("127.0.0.1:8283", "pass123", fmt.Sprintf("testroom%d", i), 1*time.Minute)
		if c != nil {
			c.Close()
		}
	}
}

func TestTCP(t *testing.T) {
	log.SetLevel("error")
	timeToRoomDeletion := 100 * time.Millisecond
	go RunWithOptionsAsync("127.0.0.1", "8381", "pass123",
		WithBanner("8382"),
		WithLogLevel("debug"),
		WithRoomTTL(timeToRoomDeletion))

	time.Sleep(timeToRoomDeletion)
	err := PingServer("127.0.0.1:8381")
	assert.Nil(t, err)
	err = PingServer("127.0.0.1:8333")
	assert.NotNil(t, err)

	time.Sleep(timeToRoomDeletion)
	c1, banner, _, err := ConnectToTCPServer("127.0.0.1:8381", "pass123", "testRoom", 1*time.Minute)
	assert.Equal(t, banner, "8382")
	assert.Nil(t, err)
	c2, _, _, err := ConnectToTCPServer("127.0.0.1:8381", "pass123", "testRoom")
	assert.Nil(t, err)
	_, _, _, err = ConnectToTCPServer("127.0.0.1:8381", "pass123", "testRoom")
	assert.NotNil(t, err)
	_, _, _, err = ConnectToTCPServer("127.0.0.1:8381", "pass123", "testRoom", 1*time.Nanosecond)
	assert.NotNil(t, err)

	// try sending data
	assert.Nil(t, c1.Send([]byte("hello, c2")))
	var data []byte
	for {
		data, err = c2.Receive()
		if bytes.Equal(data, []byte{1}) {
			continue
		}
		break
	}
	assert.Nil(t, err)
	assert.Equal(t, []byte("hello, c2"), data)

	assert.Nil(t, c2.Send([]byte("hello, c1")))
	for {
		data, err = c1.Receive()
		if bytes.Equal(data, []byte{1}) {
			continue
		}
		break
	}
	assert.Nil(t, err)
	assert.Equal(t, []byte("hello, c1"), data)

	c1.Close()
	time.Sleep(300 * time.Millisecond)
}

func TestTCPctx(t *testing.T) {
	log.SetLevel("error")
	// Set short room TTL for testing cleanup
	timeToRoomDeletion := 100 * time.Millisecond

	// Create cancelable context
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	// Start server with custom options
	go RunWithOptionsAsync("127.0.0.1", "8381", "pass123",
		WithBanner("8382"),
		WithLogLevel("debug"),
		WithRoomTTL(timeToRoomDeletion),
		WithCtx(ctx),
	)

	time.Sleep(timeToRoomDeletion)

	// Test ping to running server
	err := PingServer("127.0.0.1:8381")
	assert.Nil(t, err)

	// Test ping to non-existent server
	err = PingServer("127.0.0.1:8333")
	assert.NotNil(t, err)

	time.Sleep(timeToRoomDeletion)

	// Connect first client to room
	c1, banner, _, err := ConnectToTCPServer("127.0.0.1:8381", "pass123", "testRoom", 1*time.Minute)
	assert.Equal(t, banner, "8382")
	assert.Nil(t, err)

	// Connect second client to same room
	c2, _, _, err := ConnectToTCPServer("127.0.0.1:8381", "pass123", "testRoom")
	assert.Nil(t, err)

	// Third client should fail - room is full
	_, _, _, err = ConnectToTCPServer("127.0.0.1:8381", "pass123", "testRoom")
	assert.NotNil(t, err)

	// Connection with very short timeout should fail
	_, _, _, err = ConnectToTCPServer("127.0.0.1:8381", "pass123", "testRoom", 1*time.Nanosecond)
	assert.NotNil(t, err)

	// Test data exchange between clients
	// Send from c1 to c2
	assert.Nil(t, c1.Send([]byte("hello, c2")))
	var data []byte
	for {
		data, err = c2.Receive()
		if bytes.Equal(data, []byte{1}) {
			continue // Skip heartbeat
		}
		break
	}
	assert.Nil(t, err)
	assert.Equal(t, []byte("hello, c2"), data)

	// Send from c2 to c1
	assert.Nil(t, c2.Send([]byte("hello, c1")))
	for {
		data, err = c1.Receive()
		if bytes.Equal(data, []byte{1}) {
			continue // Skip heartbeat
		}
		break
	}
	assert.Nil(t, err)
	assert.Equal(t, []byte("hello, c1"), data)

	// Close server
	cancel()

	// Test ping to non-existent server
	err = PingServer("127.0.0.1:8331")
	assert.NotNil(t, err)

	time.Sleep(300 * time.Millisecond)
}

func TestWrongPassword(t *testing.T) {
	log.SetLevel("error")
	go Run("debug", "127.0.0.1", "8385", "pass123", "8386")
	time.Sleep(100 * time.Millisecond)

	// Attempt to connect with wrong password
	_, _, _, err := ConnectToTCPServer("127.0.0.1:8385", "wrongpass", "testRoom")
	assert.NotNil(t, err)
	assert.Contains(t, err.Error(), "bad password")
}

func TestRoomIsolation(t *testing.T) {
	log.SetLevel("error")
	go Run("debug", "127.0.0.1", "8387", "pass123", "8388")
	time.Sleep(100 * time.Millisecond)

	// Room 1
	c1, _, _, _ := ConnectToTCPServer("127.0.0.1:8387", "pass123", "room1")
	c2, _, _, _ := ConnectToTCPServer("127.0.0.1:8387", "pass123", "room1")

	// Room 2
	c3, _, _, _ := ConnectToTCPServer("127.0.0.1:8387", "pass123", "room2")
	c4, _, _, _ := ConnectToTCPServer("127.0.0.1:8387", "pass123", "room2")

	// Send data in different rooms
	c1.Send([]byte("to_room_1"))
	c3.Send([]byte("to_room_2"))

	// Verify reception
	var data []byte

	// c2 should receive message from room1
	for {
		data, _ = c2.Receive()
		if bytes.Equal(data, []byte{1}) {
			continue
		}
		break
	}
	assert.Equal(t, []byte("to_room_1"), data)

	// c4 should receive message from room2
	for {
		data, _ = c4.Receive()
		if bytes.Equal(data, []byte{1}) {
			continue
		}
		break
	}
	assert.Equal(t, []byte("to_room_2"), data)

	c1.Close()
	c2.Close()
	c3.Close()
	c4.Close()
}

func TestRoomRecreationAfterTTL(t *testing.T) {
	log.SetLevel("error")
	shortTTL := 50 * time.Millisecond

	go RunWithOptionsAsync("127.0.0.1", "8389", "pass123",
		WithRoomTTL(shortTTL),
		WithLogLevel("error"))
	time.Sleep(100 * time.Millisecond)

	roomName := "testRoomRecreate"

	// 1. Create a room
	c1, _, _, _ := ConnectToTCPServer("127.0.0.1:8389", "pass123", roomName)
	assert.NotNil(t, c1)

	// 2. Close first client, room becomes empty
	c1.Close()

	// 3. Wait for room cleanup (TTL + buffer)
	time.Sleep(shortTTL + 50*time.Millisecond)

	// 4. Try to connect to the same room again.
	// If room wasn't deleted, we might get "room full" or weird behavior.
	// If deleted — connection should succeed as the first client.
	c3, _, _, err := ConnectToTCPServer("127.0.0.1:8389", "pass123", roomName)
	assert.Nil(t, err)
	assert.NotNil(t, c3)

	if c3 != nil {
		c3.Close()
	}
}

func TestLargeDataTransfer(t *testing.T) {
	log.SetLevel("error")
	go Run("debug", "127.0.0.1", "8391", "pass123", "8392")
	time.Sleep(100 * time.Millisecond)

	c1, _, _, _ := ConnectToTCPServer("127.0.0.1:8391", "pass123", "bigRoom")
	c2, _, _, _ := ConnectToTCPServer("127.0.0.1:8391", "pass123", "bigRoom")

	// Generate data larger than standard buffer (e.g., 1 MB)
	largeData := make([]byte, 1024*1024)
	for i := range largeData {
		largeData[i] = byte(i % 256)
	}

	err := c1.Send(largeData)
	assert.Nil(t, err)

	var received []byte
	// Receive data, as it might arrive in chunks (though chanFromConn buffers it)
	// In this case pipe passes full Read packets, but for safety let's verify tail
	for {
		data, err := c2.Receive()
		if bytes.Equal(data, []byte{1}) {
			continue
		}
		assert.Nil(t, err)
		received = data
		break
	}

	assert.True(t, bytes.Equal(largeData, received), "Large data mismatch")

	c1.Close()
	c2.Close()
}

func TestServerReleasesPort(t *testing.T) {
	log.SetLevel("trace")
	host := "127.0.0.1"
	port := "8394"

	// 1. Start and automatically stop first server using timeout
	// RunCtx blocks the execution, so we don't need 'go' or channels
	ctx1, cancel1 := context.WithTimeout(context.Background(), 200*time.Millisecond)
	defer cancel1()

	err := RunCtx(ctx1, "trace", host, port, "pass123")
	assert.Nil(t, err, "First server should stop gracefully")

	// 2. Try to start second server on the same port immediately
	// If port is not released, this will fail with "address already in use"
	ctx2, cancel2 := context.WithTimeout(context.Background(), 200*time.Millisecond)
	defer cancel2()

	err = RunCtx(ctx2, "trace", host, port, "pass123")
	assert.Nil(t, err, "Second server should start (port was released)")
}
```

## File: `src/utils/ctx.go`
```go
// ctx.go
package utils

import (
	"context"
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"io"
	"os"
	"path"
	"time"

	"github.com/cespare/xxhash/v2"
	"github.com/minio/highwayhash"
	"github.com/schollz/progressbar/v3"
)

// ctxFile wraps os.File with context cancellation support.
type ctxFile struct {
	ctx context.Context
	f   *os.File
}

// NewCtxFile creates a new context-aware file wrapper.
func NewCtxFile(ctx context.Context, f *os.File) *ctxFile {
	return &ctxFile{ctx: ctx, f: f}
}

// Read implements io.Reader interface with context cancellation.
func (c *ctxFile) Read(p []byte) (n int, err error) {
	select {
	case <-c.ctx.Done():
		return 0, c.ctx.Err()
	default:
		n, err = c.f.Read(p)
		if c.ctx.Err() != nil {
			return 0, c.ctx.Err()
		}
		return n, err
	}
}

// ReadAt implements io.ReaderAt interface with context cancellation.
func (c *ctxFile) ReadAt(p []byte, off int64) (n int, err error) {
	select {
	case <-c.ctx.Done():
		return 0, c.ctx.Err()
	default:
		n, err = c.f.ReadAt(p, off)
		if c.ctx.Err() != nil {
			return 0, c.ctx.Err()
		}
		return n, err
	}
}

// Seek implements io.Seeker interface with context cancellation.
func (c *ctxFile) Seek(offset int64, whence int) (n int64, err error) {
	select {
	case <-c.ctx.Done():
		return 0, c.ctx.Err()
	default:
		n, err = c.f.Seek(offset, whence)
		if c.ctx.Err() != nil {
			return 0, c.ctx.Err()
		}
		return n, err
	}
}

// HashFileCtx returns the hash of a file with context cancellation support.
func HashFileCtx(ctx context.Context, fname string, algorithm string, showProgress ...bool) ([]byte, error) {
	// Quick context check before starting
	if err := ctx.Err(); err != nil {
		return nil, err
	}

	fstats, err := os.Lstat(fname)
	if err != nil {
		return nil, err
	}

	// Handle symlinks - quick operation, no context needed
	if fstats.Mode()&os.ModeSymlink != 0 {
		target, err := os.Readlink(fname)
		if err != nil {
			return nil, err
		}
		return []byte(SHA256(target)), nil
	}

	f, err := os.Open(fname)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	// Get file info for size (now file is opened, following symlinks if any)
	fi, err := f.Stat()
	if err != nil {
		return nil, err
	}

	// Wrap the file with context support
	cf := NewCtxFile(ctx, f)
	sr := io.NewSectionReader(cf, 0, fi.Size())

	// Parse showProgress parameter
	doShowProgress := false
	if len(showProgress) > 0 {
		doShowProgress = showProgress[0]
	}

	// Create progress bar based on algorithm
	var bar *progressbar.ProgressBar
	if doShowProgress {
		fnameShort := path.Base(fname)
		if len(fnameShort) > 20 {
			fnameShort = fnameShort[:20] + "..."
		}

		if algorithm == "imohash" {
			// Spinner for imohash (indeterminate progress, max = -1)
			bar = progressbar.NewOptions64(-1,
				progressbar.OptionSetWriter(os.Stderr),
				progressbar.OptionShowBytes(false),
				progressbar.OptionSetDescription(fmt.Sprintf("Sampling %s", fnameShort)),
				progressbar.OptionClearOnFinish(),
				progressbar.OptionFullWidth(),
				progressbar.OptionShowElapsedTimeOnFinish(),
				progressbar.OptionSpinnerType(14),
				progressbar.OptionSetSpinnerChangeInterval(100*time.Millisecond),
			)
		} else {
			// Regular progress bar for other algorithms
			bar = progressbar.NewOptions64(fi.Size(),
				progressbar.OptionSetWriter(os.Stderr),
				progressbar.OptionShowBytes(true),
				progressbar.OptionSetDescription(fmt.Sprintf("Hashing %s", fnameShort)),
				progressbar.OptionClearOnFinish(),
				progressbar.OptionFullWidth(),
			)
		}
	}

	// Dispatch to appropriate hash function
	switch algorithm {
	case "imohash":
		return IMOHashReader(sr, bar)
	case "md5":
		return MD5HashReader(sr, bar)
	case "xxhash":
		return XXHashReader(sr, bar)
	case "highway":
		return HighwayHashReader(sr, bar)
	default:
		return nil, fmt.Errorf("unsupported algorithm: %s", algorithm)
	}
}

// IMOHashReader returns imohash for a SectionReader.
// Uses spinner progress bar for indeterminate progress.
func IMOHashReader(sr *io.SectionReader, bar *progressbar.ProgressBar) ([]byte, error) {
	// Start spinner if provided
	if bar != nil {
		// Add(0) triggers initial render for spinner
		bar.Add(0)
	}

	b, err := imopartial.SumSectionReader(sr)
	if err != nil {
		// If there's an error, finish the bar to clean up display
		if bar != nil {
			bar.Exit()
		}
		return nil, err
	}

	// Finish the progress bar
	if bar != nil {
		bar.Finish()
	}

	return b[:], nil
}

// IMOHashReaderFull returns full imohash (no sampling) for a SectionReader.
func IMOHashReaderFull(sr *io.SectionReader, bar *progressbar.ProgressBar) ([]byte, error) {
	// For full imohash (which reads entire file), use regular progress bar logic
	if bar != nil {
		bar.Add(0) // Start the spinner
	}

	b, err := imofull.SumSectionReader(sr)
	if err != nil {
		if bar != nil {
			bar.Exit()
		}
		return nil, err
	}

	if bar != nil {
		bar.Finish()
	}

	return b[:], nil
}

// MD5HashReader returns MD5 hash for a SectionReader.
func MD5HashReader(sr *io.SectionReader, bar *progressbar.ProgressBar) ([]byte, error) {
	// Reset to beginning
	if _, err := sr.Seek(0, io.SeekStart); err != nil {
		return nil, err
	}

	h := md5.New()
	if bar != nil {
		// Copy with progress tracking (like original code)
		if _, err := io.Copy(io.MultiWriter(h, bar), sr); err != nil {
			return nil, err
		}
	} else {
		if _, err := io.Copy(h, sr); err != nil {
			return nil, err
		}
	}
	return h.Sum(nil), nil
}

// XXHashReader returns xxhash for a SectionReader.
func XXHashReader(sr *io.SectionReader, bar *progressbar.ProgressBar) ([]byte, error) {
	if _, err := sr.Seek(0, io.SeekStart); err != nil {
		return nil, err
	}

	h := xxhash.New()
	if bar != nil {
		if _, err := io.Copy(io.MultiWriter(h, bar), sr); err != nil {
			return nil, err
		}
	} else {
		if _, err := io.Copy(h, sr); err != nil {
			return nil, err
		}
	}
	return h.Sum(nil), nil
}

// HighwayHashReader returns highwayhash for a SectionReader.
func HighwayHashReader(sr *io.SectionReader, bar *progressbar.ProgressBar) ([]byte, error) {
	if _, err := sr.Seek(0, io.SeekStart); err != nil {
		return nil, err
	}

	key, err := hex.DecodeString("1553c5383fb0b86578c3310da665b4f6e0521acf22eb58a99532ffed02a6b115")
	if err != nil {
		return nil, err
	}

	h, err := highwayhash.New(key)
	if err != nil {
		return nil, fmt.Errorf("could not create highwayhash: %w", err)
	}

	if bar != nil {
		if _, err := io.Copy(io.MultiWriter(h, bar), sr); err != nil {
			return nil, err
		}
	} else {
		if _, err := io.Copy(h, sr); err != nil {
			return nil, err
		}
	}
	return h.Sum(nil), nil
}

// Helper function to update existing HashFile to use HashFileCtx
// func HashFile(fname string, algorithm string, showProgress ...bool) ([]byte, error) {
// 	return HashFileCtx(context.Background(), fname, algorithm, showProgress...)
// }
```

## File: `src/utils/utils.go`
```go
package utils

import (
	"archive/zip"
	"bufio"
	"bytes"
	"compress/flate"
	"crypto/md5"
	"crypto/rand"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"io"
	"math"
	"math/big"
	"net"
	"net/http"
	"os"
	"path"
	"path/filepath"
	"strings"
	"time"
	"unicode"

	"github.com/cespare/xxhash/v2"
	"github.com/kalafut/imohash"
	"github.com/minio/highwayhash"
	"github.com/schollz/croc/v10/src/mnemonicode"
	log "github.com/schollz/logger"
	"github.com/schollz/progressbar/v3"
)

const NbPinNumbers = 4
const NbBytesWords = 4

// Get or create home directory
func GetConfigDir(requireValidPath bool) (homedir string, err error) {
	if envHomedir, isSet := os.LookupEnv("CROC_CONFIG_DIR"); isSet {
		homedir = envHomedir
	} else if xdgConfigHome, isSet := os.LookupEnv("XDG_CONFIG_HOME"); isSet {
		homedir = path.Join(xdgConfigHome, "croc")
	} else {
		homedir, err = os.UserHomeDir()
		if err != nil {
			if !requireValidPath {
				err = nil
				homedir = ""
			}
			return
		}
		homedir = path.Join(homedir, ".config", "croc")
	}

	if requireValidPath {
		if _, err = os.Stat(homedir); os.IsNotExist(err) {
			err = os.MkdirAll(homedir, 0o700)
		}
	}
	return
}

// Exists reports whether the named file or directory exists.
func Exists(name string) bool {
	if _, err := os.Stat(name); err != nil {
		if os.IsNotExist(err) {
			return false
		}
	}
	return true
}

// GetInput returns the input with a given prompt
func GetInput(prompt string) string {
	reader := bufio.NewReader(os.Stdin)
	fmt.Fprintf(os.Stderr, "%s", prompt)
	text, _ := reader.ReadString('\n')
	return strings.TrimSpace(text)
}

// HashFile returns the hash of a file or, in case of a symlink, the
// SHA256 hash of its target. Takes an argument to specify the algorithm to use.
func HashFile(fname string, algorithm string, showProgress ...bool) (hash256 []byte, err error) {
	doShowProgress := false
	if len(showProgress) > 0 {
		doShowProgress = showProgress[0]
	}
	var fstats os.FileInfo
	fstats, err = os.Lstat(fname)
	if err != nil {
		return nil, err
	}
	if fstats.Mode()&os.ModeSymlink != 0 {
		var target string
		target, err = os.Readlink(fname)
		if err != nil {
			return nil, err
		}
		return []byte(SHA256(target)), nil
	}
	switch algorithm {
	case "imohash":
		return IMOHashFile(fname)
	case "md5":
		return MD5HashFile(fname, doShowProgress)
	case "xxhash":
		return XXHashFile(fname, doShowProgress)
	case "highway":
		return HighwayHashFile(fname, doShowProgress)
	}
	err = fmt.Errorf("unspecified algorithm")
	return
}

// HighwayHashFile returns highwayhash of a file
func HighwayHashFile(fname string, doShowProgress bool) (hashHighway []byte, err error) {
	f, err := os.Open(fname)
	if err != nil {
		return
	}
	defer f.Close()
	key, err := hex.DecodeString("1553c5383fb0b86578c3310da665b4f6e0521acf22eb58a99532ffed02a6b115")
	if err != nil {
		return
	}
	h, err := highwayhash.New(key)
	if err != nil {
		err = fmt.Errorf("could not create highwayhash: %s", err.Error())
		return
	}
	if doShowProgress {
		stat, _ := f.Stat()
		fnameShort := path.Base(fname)
		if len(fnameShort) > 20 {
			fnameShort = fnameShort[:20] + "..."
		}
		bar := progressbar.NewOptions64(stat.Size(),
			progressbar.OptionSetWriter(os.Stderr),
			progressbar.OptionShowBytes(true),
			progressbar.OptionSetDescription(fmt.Sprintf("Hashing %s", fnameShort)),
			progressbar.OptionClearOnFinish(),
			progressbar.OptionFullWidth(),
		)
		if _, err = io.Copy(io.MultiWriter(h, bar), f); err != nil {
			return
		}
	} else {
		if _, err = io.Copy(h, f); err != nil {
			return
		}
	}

	hashHighway = h.Sum(nil)
	return
}

// MD5HashFile returns MD5 hash
func MD5HashFile(fname string, doShowProgress bool) (hash256 []byte, err error) {
	f, err := os.Open(fname)
	if err != nil {
		return
	}
	defer f.Close()

	h := md5.New()
	if doShowProgress {
		stat, _ := f.Stat()
		fnameShort := path.Base(fname)
		if len(fnameShort) > 20 {
			fnameShort = fnameShort[:20] + "..."
		}
		bar := progressbar.NewOptions64(stat.Size(),
			progressbar.OptionSetWriter(os.Stderr),
			progressbar.OptionShowBytes(true),
			progressbar.OptionSetDescription(fmt.Sprintf("Hashing %s", fnameShort)),
			progressbar.OptionClearOnFinish(),
			progressbar.OptionFullWidth(),
		)
		if _, err = io.Copy(io.MultiWriter(h, bar), f); err != nil {
			return
		}
	} else {
		if _, err = io.Copy(h, f); err != nil {
			return
		}
	}

	hash256 = h.Sum(nil)
	return
}

var imofull = imohash.NewCustom(0, 0)
var imopartial = imohash.NewCustom(16*16*8*1024, 128*1024)

// IMOHashFile returns imohash
func IMOHashFile(fname string) (hash []byte, err error) {
	b, err := imopartial.SumFile(fname)
	hash = b[:]
	return
}

// IMOHashFileFull returns imohash of full file
func IMOHashFileFull(fname string) (hash []byte, err error) {
	b, err := imofull.SumFile(fname)
	hash = b[:]
	return
}

// XXHashFile returns the xxhash of a file
func XXHashFile(fname string, doShowProgress bool) (hash256 []byte, err error) {
	f, err := os.Open(fname)
	if err != nil {
		return
	}
	defer f.Close()

	h := xxhash.New()
	if doShowProgress {
		stat, _ := f.Stat()
		fnameShort := path.Base(fname)
		if len(fnameShort) > 20 {
			fnameShort = fnameShort[:20] + "..."
		}
		bar := progressbar.NewOptions64(stat.Size(),
			progressbar.OptionSetWriter(os.Stderr),
			progressbar.OptionShowBytes(true),
			progressbar.OptionSetDescription(fmt.Sprintf("Hashing %s", fnameShort)),
			progressbar.OptionClearOnFinish(),
			progressbar.OptionFullWidth(),
		)
		if _, err = io.Copy(io.MultiWriter(h, bar), f); err != nil {
			return
		}
	} else {
		if _, err = io.Copy(h, f); err != nil {
			return
		}
	}

	hash256 = h.Sum(nil)
	return
}

// SHA256 returns sha256 sum
func SHA256(s string) string {
	sha := sha256.New()
	sha.Write([]byte(s))
	return hex.EncodeToString(sha.Sum(nil))
}

// PublicIP returns public ip address
func PublicIP() (ip string, err error) {
	// ask ipv4.icanhazip.com for the public ip
	// by making http request
	// if the request fails, return nothing
	resp, err := http.Get("http://ipv4.icanhazip.com")
	if err != nil {
		return
	}
	defer resp.Body.Close()

	// read the body of the response
	// and return the ip address
	buf := new(bytes.Buffer)
	buf.ReadFrom(resp.Body)
	ip = strings.TrimSpace(buf.String())

	return
}

// LocalIP returns local ip address
func LocalIP() string {
	conn, err := net.Dial("udp", "8.8.8.8:80")
	if err != nil {
		log.Error(err)
		return ""
	}
	defer conn.Close()

	localAddr := conn.LocalAddr().(*net.UDPAddr)

	return localAddr.IP.String()
}

// GenerateRandomPin returns a randomly generated pin with set length
func GenerateRandomPin() string {
	s := ""
	max := new(big.Int)
	max.SetInt64(9)
	for range NbPinNumbers {
		v, err := rand.Int(rand.Reader, max)
		if err != nil {
			panic(err)
		}
		s += fmt.Sprintf("%d", v)
	}
	return s
}

// GetRandomName returns mnemonicoded random name
func GetRandomName() string {
	var result []string
	bs := make([]byte, NbBytesWords)
	rand.Read(bs)
	result = mnemonicode.EncodeWordList(result, bs)
	return GenerateRandomPin() + "-" + strings.Join(result, "-")
}

// ByteCountDecimal converts bytes to human readable byte string
func ByteCountDecimal(b int64) string {
	const unit = 1024
	if b < unit {
		return fmt.Sprintf("%d B", b)
	}
	div, exp := int64(unit), 0
	for n := b / unit; n >= unit; n /= unit {
		div *= unit
		exp++
	}
	return fmt.Sprintf("%.1f %cB", float64(b)/float64(div), "kMGTPE"[exp])
}

// MissingChunks returns the positions of missing chunks.
// If file doesn't exist, it returns an empty chunk list (all chunks).
// If the file size is not the same as requested, it returns an empty chunk list (all chunks).
func MissingChunks(fname string, fsize int64, chunkSize int) (chunkRanges []int64) {
	f, err := os.Open(fname)
	if err != nil {
		return
	}
	defer f.Close()

	fstat, err := os.Stat(fname)
	if err != nil || fstat.Size() != fsize {
		return
	}

	// Show progress bar for large files (> 10MB)
	var bar *progressbar.ProgressBar
	showProgress := fsize > 10*1024*1024
	if showProgress {
		fnameShort := path.Base(fname)
		if len(fnameShort) > 20 {
			fnameShort = fnameShort[:20] + "..."
		}
		bar = progressbar.NewOptions64(fsize,
			progressbar.OptionSetWriter(os.Stderr),
			progressbar.OptionShowBytes(true),
			progressbar.OptionSetDescription(fmt.Sprintf("Checking %s", fnameShort)),
			progressbar.OptionClearOnFinish(),
			progressbar.OptionFullWidth(),
			progressbar.OptionThrottle(100*time.Millisecond),
		)
	}

	emptyBuffer := make([]byte, chunkSize)
	chunkNum := 0
	chunks := make([]int64, int64(math.Ceil(float64(fsize)/float64(chunkSize))))
	var currentLocation int64
	for {
		buffer := make([]byte, chunkSize)
		bytesread, err := f.Read(buffer)
		if err != nil {
			break
		}
		if bytes.Equal(buffer[:bytesread], emptyBuffer[:bytesread]) {
			chunks[chunkNum] = currentLocation
			chunkNum++
		}
		currentLocation += int64(bytesread)
		if showProgress && bar != nil {
			bar.Add(bytesread)
		}
	}
	if showProgress && bar != nil {
		bar.Finish()
	}
	if chunkNum == 0 {
		chunkRanges = []int64{}
	} else {
		chunks = chunks[:chunkNum]
		chunkRanges = []int64{int64(chunkSize), chunks[0]}
		curCount := 0
		for i, chunk := range chunks {
			if i == 0 {
				continue
			}
			curCount++
			if chunk-chunks[i-1] > int64(chunkSize) {
				chunkRanges = append(chunkRanges, int64(curCount))
				chunkRanges = append(chunkRanges, chunk)
				curCount = 0
			}
		}
		chunkRanges = append(chunkRanges, int64(curCount+1))
	}
	return
}

// ChunkRangesToChunks converts chunk ranges to list
func ChunkRangesToChunks(chunkRanges []int64) (chunks []int64) {
	if len(chunkRanges) == 0 {
		return
	}
	chunkSize := chunkRanges[0]
	chunks = []int64{}
	for i := 1; i < len(chunkRanges); i += 2 {
		for j := int64(0); j < (chunkRanges[i+1]); j++ {
			chunks = append(chunks, chunkRanges[i]+j*chunkSize)
		}
	}
	return
}

// GetLocalIPs returns all local ips
func GetLocalIPs() (ips []string, err error) {
	addrs, err := net.InterfaceAddrs()
	if err != nil {
		if ip := LocalIP(); ip != "" {
			return []string{ip}, nil
		}
		return
	}
	ips = []string{}
	for _, address := range addrs {
		// check the address type and if it is not a loopback the display it
		if ipnet, ok := address.(*net.IPNet); ok && !ipnet.IP.IsLoopback() {
			if ipnet.IP.To4() != nil {
				ips = append(ips, ipnet.IP.String())
			}
		}
	}
	return
}

func RandomFileName() (fname string, err error) {
	f, err := os.CreateTemp(".", "croc-stdin-")
	if err != nil {
		return
	}
	fname = f.Name()
	_ = f.Close()
	return
}

func FindOpenPorts(host string, portNumStart, numPorts int) (openPorts []int) {
	openPorts = []int{}
	for port := portNumStart; port-portNumStart < 200; port++ {
		timeout := 100 * time.Millisecond
		conn, err := net.DialTimeout("tcp", net.JoinHostPort(host, fmt.Sprint(port)), timeout)
		if conn != nil {
			conn.Close()
		} else if err != nil {
			openPorts = append(openPorts, port)
		}
		if len(openPorts) >= numPorts {
			return
		}
	}
	return
}

// local ip determination
// https://stackoverflow.com/questions/41240761/check-if-ip-address-is-in-private-network-space
var privateIPBlocks []*net.IPNet

func init() {
	for _, cidr := range []string{
		"127.0.0.0/8",    // IPv4 loopback
		"10.0.0.0/8",     // RFC1918
		"172.16.0.0/12",  // RFC1918
		"192.168.0.0/16", // RFC1918
		"169.254.0.0/16", // RFC3927 link-local
		"::1/128",        // IPv6 loopback
		"fe80::/10",      // IPv6 link-local
		"fc00::/7",       // IPv6 unique local addr
	} {
		_, block, err := net.ParseCIDR(cidr)
		if err != nil {
			panic(fmt.Errorf("parse error on %q: %v", cidr, err))
		}
		privateIPBlocks = append(privateIPBlocks, block)
	}
}

func IsLocalIP(ipaddress string) bool {
	if strings.Contains(ipaddress, "127.0.0.1") {
		return true
	}
	host, _, _ := net.SplitHostPort(ipaddress)
	ip := net.ParseIP(host)
	if ip.IsLoopback() || ip.IsLinkLocalUnicast() || ip.IsLinkLocalMulticast() {
		return true
	}
	for _, block := range privateIPBlocks {
		if block.Contains(ip) {
			return true
		}
	}
	return false
}

func ZipDirectory(destination string, source string) (err error) {
	if _, err = os.Stat(destination); err == nil {
		log.Errorf("%s file already exists!\n", destination)
		return fmt.Errorf("file already exists: %s", destination)
	}

	// Check if source directory exists
	if _, err := os.Stat(source); os.IsNotExist(err) {
		log.Errorf("Source directory does not exist: %s", source)
		return fmt.Errorf("source directory does not exist: %s", source)
	}

	fmt.Fprintf(os.Stderr, "Zipping %s to %s\n", source, destination)
	file, err := os.Create(destination)
	if err != nil {
		log.Error(err)
		return fmt.Errorf("failed to create zip file: %w", err)
	}
	defer file.Close()
	writer := zip.NewWriter(file)
	// no compression because croc does its compression on the fly
	writer.RegisterCompressor(zip.Deflate, func(out io.Writer) (io.WriteCloser, error) {
		return flate.NewWriter(out, flate.NoCompression)
	})
	defer writer.Close()

	// Get base name for zip structure
	baseName := strings.TrimSuffix(filepath.Base(destination), ".zip")

	// First pass: add the root directory with its modification time
	rootInfo, err := os.Stat(source)
	if err == nil && rootInfo.IsDir() {
		header, err := zip.FileInfoHeader(rootInfo)
		if err != nil {
			log.Error(err)
		} else {
			header.Name = baseName + "/" // Trailing slash indicates directory
			header.Method = zip.Store
			header.Modified = rootInfo.ModTime()

			_, err = writer.CreateHeader(header)
			if err != nil {
				log.Error(err)
			} else {
				fmt.Fprintf(os.Stderr, "\r\033[2K")
				fmt.Fprintf(os.Stderr, "\rAdding %s", baseName+"/")
			}
		}
	}

	// Second pass: add all other directories and files
	err = filepath.Walk(source, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			log.Error(err)
			return nil
		}

		// Skip root directory (we already added it)
		if path == source {
			return nil
		}

		// Calculate relative path from source directory
		relPath, err := filepath.Rel(source, path)
		if err != nil {
			log.Error(err)
			return nil
		}

		// Create zip path with base name structure
		zipPath := filepath.Join(baseName, relPath)
		zipPath = filepath.ToSlash(zipPath)

		if info.IsDir() {
			// Add directory entry to zip with original modification time
			header, err := zip.FileInfoHeader(info)
			if err != nil {
				log.Error(err)
				return nil
			}
			header.Name = zipPath + "/" // Trailing slash indicates directory
			header.Method = zip.Store
			// Preserve the original modification time
			header.Modified = info.ModTime()

			_, err = writer.CreateHeader(header)
			if err != nil {
				log.Error(err)
				return nil
			}

			fmt.Fprintf(os.Stderr, "\r\033[2K")
			fmt.Fprintf(os.Stderr, "\rAdding %s", zipPath+"/")
			return nil
		}

		if info.Mode().IsRegular() {
			f1, err := os.Open(path)
			if err != nil {
				log.Error(err)
				return nil
			}
			defer f1.Close()

			// Create file header with modified time
			header, err := zip.FileInfoHeader(info)
			if err != nil {
				log.Error(err)
				return nil
			}
			header.Name = zipPath
			header.Method = zip.Deflate

			w1, err := writer.CreateHeader(header)
			if err != nil {
				log.Error(err)
				return nil
			}

			if _, err := io.Copy(w1, f1); err != nil {
				log.Error(err)
				return nil
			}

			fmt.Fprintf(os.Stderr, "\r\033[2K")
			fmt.Fprintf(os.Stderr, "\rAdding %s", zipPath)
		}
		return nil
	})

	if err != nil {
		log.Error(err)
		return fmt.Errorf("error during directory walk: %w", err)
	}
	fmt.Fprintf(os.Stderr, "\n")
	return nil
}

func UnzipDirectory(destination string, source string) error {
	archive, err := zip.OpenReader(source)
	if err != nil {
		log.Error(err)
		return fmt.Errorf("failed to open zip file: %w", err)
	}
	defer archive.Close()

	// Pre-validate all paths to avoid partial extraction on malicious archives.
	filePaths := make([]string, len(archive.File))
	for i, f := range archive.File {
		filePath, pathErr := resolveUnzipPath(destination, f.Name)
		if pathErr != nil {
			log.Errorf("Invalid file path %s: %v\n", f.Name, pathErr)
			return fmt.Errorf("invalid file path in zip entry %q: %w", f.Name, pathErr)
		}
		filePaths[i] = filePath
	}

	// Store modification times for all files and directories
	modTimes := make(map[string]time.Time)

	// First pass: extract all files and directories, store modification times
	for i, f := range archive.File {
		filePath := filePaths[i]
		fmt.Fprintf(os.Stderr, "\r\033[2K")
		fmt.Fprintf(os.Stderr, "\rUnzipping file %s", filePath)

		// Store modification time for this entry (BOTH files and directories)
		modifiedTime := f.Modified
		if modifiedTime.IsZero() {
			modifiedTime = f.FileHeader.Modified
		}
		if !modifiedTime.IsZero() {
			modTimes[filePath] = modifiedTime
		}

		if f.FileInfo().IsDir() {
			if err := os.MkdirAll(filePath, os.ModePerm); err != nil {
				log.Error(err)
			}
			continue
		}

		if err := os.MkdirAll(filepath.Dir(filePath), os.ModePerm); err != nil {
			log.Error(err)
			continue
		}

		// check if file exists
		if _, err := os.Stat(filePath); err == nil {
			prompt := fmt.Sprintf("\nOverwrite '%s'? (y/N) ", filePath)
			choice := strings.ToLower(GetInput(prompt))
			if choice != "y" && choice != "yes" {
				fmt.Fprintf(os.Stderr, "Skipping '%s'\n", filePath)
				continue
			}
		}

		dstFile, err := os.OpenFile(filePath, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, f.Mode())
		if err != nil {
			log.Error(err)
			continue
		}

		fileInArchive, err := f.Open()
		if err != nil {
			log.Error(err)
			dstFile.Close()
			continue
		}

		if _, err := io.Copy(dstFile, fileInArchive); err != nil {
			log.Error(err)
		}

		dstFile.Close()
		fileInArchive.Close()
	}

	// Second pass: restore modification times for ALL files and directories
	for path, modTime := range modTimes {
		if err := os.Chtimes(path, modTime, modTime); err != nil {
			log.Errorf("Failed to set modification time for %s: %v", path, err)
		} else {
			fi, err := os.Lstat(path)
			if err != nil ||
				!modTime.UTC().Equal(fi.ModTime().UTC()) {
				log.Errorf("Failed to set modification time for %s: %v", path, err)
				fmt.Fprintf(os.Stderr, "Failed to set modification time %s %v: %v\n", path, modTime, err)
			}
		}
	}

	fmt.Fprintf(os.Stderr, "\n")
	return nil
}

func resolveUnzipPath(destination string, entryName string) (string, error) {
	if filepath.IsAbs(entryName) || filepath.VolumeName(entryName) != "" {
		return "", fmt.Errorf("path escapes destination")
	}

	destinationAbs, err := filepath.Abs(destination)
	if err != nil {
		return "", fmt.Errorf("failed to resolve destination: %w", err)
	}
	destinationAbs = filepath.Clean(destinationAbs)

	filePath := filepath.Clean(filepath.Join(destinationAbs, entryName))
	relativePath, err := filepath.Rel(destinationAbs, filePath)
	if err != nil {
		return "", fmt.Errorf("failed to resolve path %q: %w", entryName, err)
	}
	if relativePath == ".." || strings.HasPrefix(relativePath, ".."+string(os.PathSeparator)) {
		return "", fmt.Errorf("path escapes destination")
	}

	return filePath, nil
}

// ValidFileName checks if a filename is valid
// by making sure it has no invisible characters
func ValidFileName(fname string) (err error) {
	// make sure it doesn't contain unicode or invisible characters
	for _, r := range fname {
		if !unicode.IsGraphic(r) {
			err = fmt.Errorf("non-graphical unicode: %x U+%d in '%x'", string(r), r, fname)
			return
		}
		if !unicode.IsPrint(r) {
			err = fmt.Errorf("non-printable unicode: %x U+%d in '%x'", string(r), r, fname)
			return
		}
	}
	// make sure basename does not include path separators
	_, basename := filepath.Split(fname)
	if strings.Contains(basename, string(os.PathSeparator)) {
		err = fmt.Errorf("basename cannot contain path separators: '%s'", basename)
		return
	}
	// make sure the filename is not an absolute path
	if filepath.IsAbs(fname) {
		err = fmt.Errorf("filename cannot be an absolute path: '%s'", fname)
		return
	}
	if !filepath.IsLocal(fname) {
		err = fmt.Errorf("filename must be a local path: '%s'", fname)
		return
	}
	return
}

const crocRemovalFile = "croc-marked-files.txt"

func MarkFileForRemoval(fname string) {
	// append the fname to the list of files to remove
	f, err := os.OpenFile(crocRemovalFile, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0o600)
	if err != nil {
		log.Debug(err)
		return
	}
	defer f.Close()
	_, err = f.WriteString(fname + "\n")
}

func RemoveMarkedFiles() (err error) {
	// read the file and remove all the files
	f, err := os.Open(crocRemovalFile)
	if err != nil {
		return
	}
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		fname := scanner.Text()
		err = os.Remove(fname)
		if err == nil {
			log.Tracef("Removed %s", fname)
		}
	}
	f.Close()
	os.Remove(crocRemovalFile)
	return
}
```

## File: `src/utils/utils_test.go`
```go
package utils

import (
	"archive/zip"
	"bytes"
	"context"
	"fmt"
	"log"
	"math/rand"
	"os"
	"path"
	"path/filepath"
	"strings"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
)

const TCP_BUFFER_SIZE = 1024 * 64

var bigFileSize = 75000000

func bigFile() {
	os.WriteFile("bigfile.test", bytes.Repeat([]byte("z"), bigFileSize), 0o666)
}

func BenchmarkMD5(b *testing.B) {
	bigFile()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		MD5HashFile("bigfile.test", false)
	}
}

func BenchmarkXXHash(b *testing.B) {
	bigFile()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		XXHashFile("bigfile.test", false)
	}
}

func BenchmarkImoHash(b *testing.B) {
	bigFile()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		IMOHashFile("bigfile.test")
	}
}

func BenchmarkHighwayHash(b *testing.B) {
	bigFile()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		HighwayHashFile("bigfile.test", false)
	}
}

func BenchmarkImoHashFull(b *testing.B) {
	bigFile()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		IMOHashFileFull("bigfile.test")
	}
}

func BenchmarkSha256(b *testing.B) {
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		SHA256("hello,world")
	}
}

func BenchmarkMissingChunks(b *testing.B) {
	bigFile()
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		MissingChunks("bigfile.test", int64(bigFileSize), TCP_BUFFER_SIZE/2)
	}
}

func TestExists(t *testing.T) {
	bigFile()
	defer os.Remove("bigfile.test")
	fmt.Println(GetLocalIPs())
	assert.True(t, Exists("bigfile.test"))
	assert.False(t, Exists("doesnotexist"))
}

func TestMD5HashFile(t *testing.T) {
	bigFile()
	defer os.Remove("bigfile.test")
	b, err := MD5HashFile("bigfile.test", false)
	assert.Nil(t, err)
	assert.Equal(t, "8304ff018e02baad0e3555bade29a405", fmt.Sprintf("%x", b))
	_, err = MD5HashFile("bigfile.test.nofile", false)
	assert.NotNil(t, err)
}

func TestHighwayHashFile(t *testing.T) {
	bigFile()
	defer os.Remove("bigfile.test")
	b, err := HighwayHashFile("bigfile.test", false)
	assert.Nil(t, err)
	assert.Equal(t, "3c32999529323ed66a67aeac5720c7bf1301dcc5dca87d8d46595e85ff990329", fmt.Sprintf("%x", b))
	_, err = HighwayHashFile("bigfile.test.nofile", false)
	assert.NotNil(t, err)
}

func TestIMOHashFile(t *testing.T) {
	bigFile()
	defer os.Remove("bigfile.test")
	b, err := IMOHashFile("bigfile.test")
	assert.Nil(t, err)
	assert.Equal(t, "c0d1e12301e6c635f6d4a8ea5c897437", fmt.Sprintf("%x", b))
}

func TestXXHashFile(t *testing.T) {
	bigFile()
	defer os.Remove("bigfile.test")
	b, err := XXHashFile("bigfile.test", false)
	assert.Nil(t, err)
	assert.Equal(t, "4918740eb5ccb6f7", fmt.Sprintf("%x", b))
	_, err = XXHashFile("nofile", false)
	assert.NotNil(t, err)
}

func TestSHA256(t *testing.T) {
	assert.Equal(t, "09ca7e4eaa6e8ae9c7d261167129184883644d07dfba7cbfbc4c8a2e08360d5b", SHA256("hello, world"))
}

func TestByteCountDecimal(t *testing.T) {
	assert.Equal(t, "10.0 kB", ByteCountDecimal(10240))
	assert.Equal(t, "50 B", ByteCountDecimal(50))
	assert.Equal(t, "12.4 MB", ByteCountDecimal(13002343))
}

func TestMissingChunks(t *testing.T) {
	fileSize := 100
	chunkSize := 10
	rand.Seed(1)
	bigBuff := make([]byte, fileSize)
	rand.Read(bigBuff)
	os.WriteFile("missing.test", bigBuff, 0o644)
	empty := make([]byte, chunkSize)
	f, err := os.OpenFile("missing.test", os.O_RDWR, 0o644)
	assert.Nil(t, err)
	for block := 0; block < fileSize/chunkSize; block++ {
		if block == 0 || block == 4 || block == 5 || block >= 7 {
			f.WriteAt(empty, int64(block*chunkSize))
		}
	}
	f.Close()

	chunkRanges := MissingChunks("missing.test", int64(fileSize), chunkSize)
	assert.Equal(t, []int64{10, 0, 1, 40, 2, 70, 3}, chunkRanges)

	chunks := ChunkRangesToChunks(chunkRanges)
	assert.Equal(t, []int64{0, 40, 50, 70, 80, 90}, chunks)

	os.Remove("missing.test")

	content := []byte("temporary file's content")
	tmpfile, err := os.CreateTemp("", "example")
	if err != nil {
		log.Fatal(err)
	}

	defer os.Remove(tmpfile.Name()) // clean up

	if _, err := tmpfile.Write(content); err != nil {
		panic(err)
	}
	if err := tmpfile.Close(); err != nil {
		panic(err)
	}
	chunkRanges = MissingChunks(tmpfile.Name(), int64(len(content)), chunkSize)
	assert.Empty(t, chunkRanges)
	chunkRanges = MissingChunks(tmpfile.Name(), int64(len(content)+10), chunkSize)
	assert.Empty(t, chunkRanges)
	chunkRanges = MissingChunks(tmpfile.Name()+"ok", int64(len(content)), chunkSize)
	assert.Empty(t, chunkRanges)
	chunks = ChunkRangesToChunks(chunkRanges)
	assert.Empty(t, chunks)
}

// func Test1(t *testing.T) {
// 	chunkRanges := MissingChunks("../../m/bigfile.test", int64(75000000), 1024*64/2)
// 	fmt.Println(chunkRanges)
// 	fmt.Println(ChunkRangesToChunks((chunkRanges)))
// 	assert.Nil(t, nil)
// }

func TestHashFile(t *testing.T) {
	content := []byte("temporary file's content")
	tmpfile, err := os.CreateTemp("", "example")
	if err != nil {
		log.Fatal(err)
	}

	defer os.Remove(tmpfile.Name()) // clean up

	if _, err = tmpfile.Write(content); err != nil {
		panic(err)
	}
	if err = tmpfile.Close(); err != nil {
		panic(err)
	}
	hashed, err := HashFile(tmpfile.Name(), "xxhash")
	assert.Nil(t, err)
	assert.Equal(t, "e66c561610ad51e2", fmt.Sprintf("%x", hashed))
}

func TestPublicIP(t *testing.T) {
	ip, err := PublicIP()
	fmt.Println(ip)
	assert.True(t, strings.Contains(ip, ".") || strings.Contains(ip, ":"))
	assert.Nil(t, err)
}

func TestLocalIP(t *testing.T) {
	ip := LocalIP()
	fmt.Println(ip)
	assert.True(t, strings.Contains(ip, ".") || strings.Contains(ip, ":"))
}

func TestGetRandomName(t *testing.T) {
	name := GetRandomName()
	fmt.Println(name)
	assert.NotEmpty(t, name)
}

func intSliceSame(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i, v := range a {
		if v != b[i] {
			return false
		}
	}
	return true
}

func TestFindOpenPorts(t *testing.T) {
	openPorts := FindOpenPorts("127.0.0.1", 9009, 4)
	if !intSliceSame(openPorts, []int{9009, 9010, 9011, 9012}) && !intSliceSame(openPorts, []int{9014, 9015, 9016, 9017}) {
		t.Errorf("openPorts: %v", openPorts)

	}
}

func TestIsLocalIP(t *testing.T) {
	assert.True(t, IsLocalIP("192.168.0.14:9009"))
}

func TestValidFileName(t *testing.T) {
	// contains regular characters
	assert.Nil(t, ValidFileName("中文.csl"))
	// contains regular characters
	assert.Nil(t, ValidFileName("[something].csl"))
	// contains regular characters
	assert.Nil(t, ValidFileName("[(something)].csl"))
	// contains invisible character
	err := ValidFileName("D中文.cslouglas​")
	assert.NotNil(t, err)
	assert.Equal(t, "non-graphical unicode: e2808b U+8203 in '44e4b8ade696872e63736c6f75676c6173e2808b'", err.Error())
	// contains "..", but not next to a path separator
	assert.Nil(t, ValidFileName("hi..txt"))
	// contains "..", but only next to a path separator on one side
	assert.Nil(t, ValidFileName("rel"+string(os.PathSeparator)+"..txt"))
	assert.Nil(t, ValidFileName("rel.."+string(os.PathSeparator)+"txt"))
	// contains ".." between two path separators, but does not break out of the base directory
	assert.Nil(t, ValidFileName("hi"+string(os.PathSeparator)+".."+string(os.PathSeparator)+"txt"))
	// contains ".." between two path separators, and breaks out of the base directory
	assert.NotNil(t, ValidFileName("hi"+string(os.PathSeparator)+".."+string(os.PathSeparator)+".."+string(os.PathSeparator)+"txt"))
	// contains ".." between a path separator and the beginning or end of the path
	assert.NotNil(t, ValidFileName(".."+string(os.PathSeparator)+"hi.txt"))
	assert.NotNil(t, ValidFileName("hi"+string(os.PathSeparator)+".."+string(os.PathSeparator)+".."+string(os.PathSeparator)+"hi.txt"))
	assert.NotNil(t, ValidFileName(".."))
	// is an absolute path
	assert.NotNil(t, ValidFileName(path.Join(string(os.PathSeparator), "abs", string(os.PathSeparator), "hi.txt")))
}

// zip

// TestUnzipDirectory tests the unzip directory functionality
func TestUnzipDirectory(t *testing.T) {
	// Create temporary directory for tests
	tmpDir, err := os.MkdirTemp("", "unzip_test")
	if err != nil {
		t.Fatalf("Failed to create temp dir: %v", err)
	}
	defer os.RemoveAll(tmpDir)

	// Create test zip and extraction directory
	zipPath := filepath.Join(tmpDir, "test.zip")
	extractDir := filepath.Join(tmpDir, "extracted")

	// Create test zip file with proper structure and known mod times
	expectedModTime := time.Date(2023, 2, 1, 10, 30, 0, 0, time.UTC)
	if err := createTestZipWithModTime(zipPath, expectedModTime); err != nil {
		t.Fatalf("Failed to create test zip: %v", err)
	}

	// Test extraction
	err = UnzipDirectory(extractDir, zipPath)
	if err != nil {
		t.Fatalf("UnzipDirectory failed: %v", err)
	}

	// Update expected files to match the actual structure from createTestZipWithModTime
	baseName := "test"
	expectedFiles := []string{
		baseName + "/file1.txt",
		baseName + "/subdir/file2.txt",
		baseName + "/subdir2/file3.txt",
		baseName + "/file4.txt",
	}

	// Also check directories
	expectedDirs := []string{
		baseName + "/",
		baseName + "/subdir/",
		baseName + "/subdir2/",
	}

	// Verify files
	for _, expectedFile := range expectedFiles {
		fullPath := filepath.Join(extractDir, expectedFile)
		if _, err := os.Stat(fullPath); os.IsNotExist(err) {
			t.Errorf("File was not extracted: %s", expectedFile)
		} else {
			// Verify modification time is preserved after extraction
			verifyFileModTime(t, fullPath, expectedModTime)
		}
	}

	// Verify directories
	for _, expectedDir := range expectedDirs {
		fullPath := filepath.Join(extractDir, expectedDir)
		if _, err := os.Stat(fullPath); os.IsNotExist(err) {
			t.Errorf("Directory was not extracted: %s", expectedDir)
		} else {
			// Verify modification time is preserved after extraction
			verifyFileModTime(t, fullPath, expectedModTime)
		}
	}

	// Verify file contents after extraction
	verifyFileContent(t, filepath.Join(extractDir, baseName+"/file1.txt"), "Test content 1")
	verifyFileContent(t, filepath.Join(extractDir, baseName+"/subdir/file2.txt"), "Test content 2")
	verifyFileContent(t, filepath.Join(extractDir, baseName+"/subdir2/file3.txt"), "Test content 3")
	verifyFileContent(t, filepath.Join(extractDir, baseName+"/file4.txt"), "Test content 4")
}

// TestUnzipToNonExistentDirectory tests unzip to non-existent destination
func TestUnzipToNonExistentDirectory(t *testing.T) {
	tmpDir, err := os.MkdirTemp("", "unzip_nonexistent_dest_test")
	if err != nil {
		t.Fatalf("Failed to create temp dir: %v", err)
	}
	defer os.RemoveAll(tmpDir)

	// Create test zip
	zipPath := filepath.Join(tmpDir, "test.zip")
	expectedModTime := time.Date(2023, 4, 1, 9, 0, 0, 0, time.UTC)
	if err := createTestZipWithModTime(zipPath, expectedModTime); err != nil {
		t.Fatalf("Failed to create test zip: %v", err)
	}

	// Extract to non-existent directory
	extractDir := filepath.Join(tmpDir, "nonexistent", "deep", "path")

	err = UnzipDirectory(extractDir, zipPath)
	if err != nil {
		t.Fatalf("UnzipDirectory failed to create destination directory: %v", err)
	}

	// Update expected files to match the actual structure
	baseName := "test"
	expectedFiles := []string{
		baseName + "/file1.txt",
		baseName + "/subdir/file2.txt",
		baseName + "/subdir2/file3.txt",
		baseName + "/file4.txt",
	}

	// Also check directories
	expectedDirs := []string{
		baseName + "/",
		baseName + "/subdir/",
		baseName + "/subdir2/",
	}

	// Verify files
	for _, expectedFile := range expectedFiles {
		fullPath := filepath.Join(extractDir, expectedFile)
		if _, err := os.Stat(fullPath); os.IsNotExist(err) {
			t.Errorf("File was not extracted to non-existent destination: %s", expectedFile)
		} else {
			// Verify modification time is preserved
			verifyFileModTime(t, fullPath, expectedModTime)
		}
	}

	// Verify directories
	for _, expectedDir := range expectedDirs {
		fullPath := filepath.Join(extractDir, expectedDir)
		if _, err := os.Stat(fullPath); os.IsNotExist(err) {
			t.Errorf("Directory was not extracted to non-existent destination: %s", expectedDir)
		} else {
			// Verify modification time is preserved
			verifyFileModTime(t, fullPath, expectedModTime)
		}
	}
}

func TestUnzipDirectoryRejectsPathTraversal(t *testing.T) {
	tmpDir := t.TempDir()
	zipPath := filepath.Join(tmpDir, "malicious-relative.zip")
	extractDir := filepath.Join(tmpDir, "extract")
	escapedPath := filepath.Join(tmpDir, "escaped.txt")

	err := createZipWithEntries(zipPath, []zipTestEntry{
		{name: "safe/file.txt", content: "safe"},
		{name: "../../escaped.txt", content: "escape"},
	})
	if err != nil {
		t.Fatalf("Failed to create malicious zip: %v", err)
	}

	err = UnzipDirectory(extractDir, zipPath)
	assert.NotNil(t, err)
	assert.Contains(t, err.Error(), "invalid file path")

	_, statErr := os.Stat(escapedPath)
	assert.True(t, os.IsNotExist(statErr), "path traversal should not create files outside destination")

	_, statErr = os.Stat(filepath.Join(extractDir, "safe", "file.txt"))
	assert.True(t, os.IsNotExist(statErr), "pre-validation should prevent partial extraction")
}

func TestResolveUnzipPathRejectsAbsolutePathEntry(t *testing.T) {
	destination := t.TempDir()
	absoluteEntry := filepath.Join(string(os.PathSeparator), "tmp", "croc-absolute-escape.txt")

	_, err := resolveUnzipPath(destination, absoluteEntry)
	assert.NotNil(t, err)
	if err != nil {
		assert.Contains(t, err.Error(), "path escapes destination")
	}
}

// TestZipAndUnzipRoundTrip tests complete zip/unzip cycle with proper paths
func TestZipAndUnzipRoundTrip(t *testing.T) {
	// Create temporary directory for tests
	tmpDir, err := os.MkdirTemp("", "roundtrip_test")
	if err != nil {
		t.Fatalf("Failed to create temp dir: %v", err)
	}
	defer os.RemoveAll(tmpDir)

	// Create source directory with test files
	sourceDir := filepath.Join(tmpDir, "source")
	if err := os.MkdirAll(sourceDir, 0755); err != nil {
		t.Fatalf("Failed to create source directory: %v", err)
	}

	// Use specific mod times for different items
	rootModTime := time.Date(2023, 3, 1, 14, 30, 0, 0, time.UTC)
	subdirModTime := time.Date(2023, 3, 1, 14, 29, 0, 0, time.UTC)
	subdir2ModTime := time.Date(2023, 3, 1, 14, 28, 0, 0, time.UTC)
	fileModTime := time.Date(2023, 3, 1, 14, 31, 0, 0, time.UTC)

	// Create directories structure first
	dirs := []string{
		"subdir",
		"subdir2",
	}

	for _, dir := range dirs {
		fullPath := filepath.Join(sourceDir, dir)
		if err := os.MkdirAll(fullPath, 0755); err != nil {
			t.Fatalf("Failed to create directory: %v", err)
		}
	}

	// Create files with specific modification times
	testFiles := map[string]string{
		"file1.txt":         "Content of file 1",
		"subdir/file2.txt":  "Content of file 2 in subdir",
		"subdir2/file3.txt": "Content of file 3 in another subdir",
		"file4.txt":         "Content of file 4",
	}

	for filePath, content := range testFiles {
		fullPath := filepath.Join(sourceDir, filePath)
		if err := os.MkdirAll(filepath.Dir(fullPath), 0755); err != nil {
			t.Fatalf("Failed to create directory: %v", err)
		}
		if err := os.WriteFile(fullPath, []byte(content), 0644); err != nil {
			t.Fatalf("Failed to create test file: %v", err)
		}
		if err := os.Chtimes(fullPath, fileModTime, fileModTime); err != nil {
			t.Fatalf("Failed to set file time: %v", err)
		}
	}

	// NOW set directory times AFTER creating all files

	// Set time for root source directory
	if err := os.Chtimes(sourceDir, rootModTime, rootModTime); err != nil {
		t.Fatalf("Failed to set source directory time: %v", err)
	}

	// Set times for subdirectories
	dirTimes := map[string]time.Time{
		"subdir":  subdirModTime,
		"subdir2": subdir2ModTime,
	}

	for dir, modTime := range dirTimes {
		fullPath := filepath.Join(sourceDir, dir)
		if err := os.Chtimes(fullPath, modTime, modTime); err != nil {
			t.Fatalf("Failed to set directory %s time: %v", dir, err)
		}
	}

	// Wait a moment to ensure time changes are applied
	time.Sleep(100 * time.Millisecond)

	// Create zip
	zipPath := filepath.Join(tmpDir, "test.zip")
	err = ZipDirectory(zipPath, sourceDir)
	if err != nil {
		t.Fatalf("ZipDirectory failed: %v", err)
	}

	// Print zip contents using Go's zip reader
	fmt.Printf("=== ZIP Archive Contents ===\n")
	archive, err := zip.OpenReader(zipPath)
	if err == nil {
		defer archive.Close()
		for _, f := range archive.File {
			modifiedTime := f.Modified
			if modifiedTime.IsZero() {
				modifiedTime = f.FileHeader.Modified
			}
			fmt.Printf("  %s (dir: %v) modTime: %v\n", f.Name, f.FileInfo().IsDir(), modifiedTime.UTC())
		}
	}

	// Extract to different directory
	extractDir := filepath.Join(tmpDir, "extracted")
	err = UnzipDirectory(extractDir, zipPath)
	if err != nil {
		t.Fatalf("UnzipDirectory failed: %v", err)
	}

	// Expected items (both files and directories)
	baseName := "test"
	expectedItems := []string{
		baseName + "/",
		baseName + "/file1.txt",
		baseName + "/subdir/",
		baseName + "/subdir/file2.txt",
		baseName + "/subdir2/",
		baseName + "/subdir2/file3.txt",
		baseName + "/file4.txt",
	}

	expectedExtractedTimes := map[string]time.Time{
		baseName + "/":                  rootModTime,
		baseName + "/subdir/":           subdirModTime,
		baseName + "/subdir2/":          subdir2ModTime,
		baseName + "/file1.txt":         fileModTime,
		baseName + "/subdir/file2.txt":  fileModTime,
		baseName + "/subdir2/file3.txt": fileModTime,
		baseName + "/file4.txt":         fileModTime,
	}

	// Verify all items exist with correct modification times
	fmt.Printf("=== Extracted Files Verification ===\n")
	for _, itemPath := range expectedItems {
		fullPath := filepath.Join(extractDir, itemPath)
		if _, err := os.Stat(fullPath); os.IsNotExist(err) {
			t.Errorf("Item was not extracted: %s", itemPath)
			continue
		}

		// Verify with test assertion
		expectedTime := expectedExtractedTimes[itemPath]
		verifyFileModTime(t, fullPath, expectedTime)
	}

	// Verify file contents
	verifyFileContent(t, filepath.Join(extractDir, baseName+"/file1.txt"), "Content of file 1")
	verifyFileContent(t, filepath.Join(extractDir, baseName+"/subdir/file2.txt"), "Content of file 2 in subdir")
	verifyFileContent(t, filepath.Join(extractDir, baseName+"/subdir2/file3.txt"), "Content of file 3 in another subdir")
	verifyFileContent(t, filepath.Join(extractDir, baseName+"/file4.txt"), "Content of file 4")
}

// Helper function to create test zip file with specific modification time
func createTestZipWithModTime(zipPath string, modTime time.Time) error {
	file, err := os.Create(zipPath)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := zip.NewWriter(file)
	defer writer.Close()

	// Get base name for consistent structure
	baseName := strings.TrimSuffix(filepath.Base(zipPath), ".zip")

	// First create entries for directories with modification time
	dirs := []string{
		baseName + "/",
		baseName + "/subdir/",
		baseName + "/subdir2/",
	}

	for _, dir := range dirs {
		header := &zip.FileHeader{
			Name:     filepath.ToSlash(dir),
			Modified: modTime,
		}
		_, err := writer.CreateHeader(header)
		if err != nil {
			return err
		}
	}

	// Then create files
	files := []struct {
		name    string
		content string
	}{
		{filepath.Join(baseName, "file1.txt"), "Test content 1"},
		{filepath.Join(baseName, "subdir", "file2.txt"), "Test content 2"},
		{filepath.Join(baseName, "subdir2", "file3.txt"), "Test content 3"},
		{filepath.Join(baseName, "file4.txt"), "Test content 4"},
	}

	for _, f := range files {
		header := &zip.FileHeader{
			Name:     filepath.ToSlash(f.name),
			Modified: modTime,
			Method:   zip.Deflate,
		}

		w, err := writer.CreateHeader(header)
		if err != nil {
			return err
		}
		if _, err := w.Write([]byte(f.content)); err != nil {
			return err
		}
	}

	return nil
}

type zipTestEntry struct {
	name    string
	content string
}

func createZipWithEntries(zipPath string, entries []zipTestEntry) error {
	file, err := os.Create(zipPath)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := zip.NewWriter(file)
	for _, entry := range entries {
		header := &zip.FileHeader{
			Name:   filepath.ToSlash(entry.name),
			Method: zip.Deflate,
		}
		w, err := writer.CreateHeader(header)
		if err != nil {
			return err
		}
		if _, err := w.Write([]byte(entry.content)); err != nil {
			return err
		}
	}

	return writer.Close()
}

// Helper function to verify file content
func verifyFileContent(t *testing.T, filePath, expectedContent string) {
	content, err := os.ReadFile(filePath)
	if err != nil {
		t.Errorf("Failed to read file %s: %v", filePath, err)
		return
	}

	if string(content) != expectedContent {
		t.Errorf("Content mismatch for %s, expected '%s', got '%s'",
			filePath, expectedContent, string(content))
	}
}

// Helper function to verify file modification time
func verifyFileModTime(t *testing.T, filePath string, expectedTime time.Time) {
	info, err := os.Stat(filePath)
	if err != nil {
		t.Errorf("Failed to stat file %s: %v", filePath, err)
		return
	}

	// Compare times truncated to seconds (file system precision may vary)
	expected := expectedTime.UTC().Truncate(time.Second)
	actual := info.ModTime().UTC().Truncate(time.Second)

	if !actual.Equal(expected) {
		t.Errorf("Modification time mismatch for %s, expected %v, got %v",
			filePath, expected, actual)
	}
}

// TestHashFileCtxNoCancellation tests HashFileCtx without cancellation
func TestHashFileCtxNoCancellation(t *testing.T) {
	// Use the same bigFile() function as other tests
	bigFile()
	defer os.Remove("bigfile.test")

	ctx := context.Background()

	// Test each algorithm - using the same expected values from existing tests
	tests := []struct {
		name      string
		algorithm string
		wantHash  string
	}{
		{
			name:      "MD5 hash",
			algorithm: "md5",
			wantHash:  "8304ff018e02baad0e3555bade29a405", // From TestMD5HashFile
		},
		{
			name:      "XXHash",
			algorithm: "xxhash",
			wantHash:  "4918740eb5ccb6f7", // From TestXXHashFile
		},
		{
			name:      "imohash",
			algorithm: "imohash",
			wantHash:  "c0d1e12301e6c635f6d4a8ea5c897437", // From TestIMOHashFile
		},
		{
			name:      "highway",
			algorithm: "highway",
			wantHash:  "3c32999529323ed66a67aeac5720c7bf1301dcc5dca87d8d46595e85ff990329", // From TestHighwayHashFile
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// Test without progress bar
			hash, err := HashFileCtx(ctx, "bigfile.test", tt.algorithm)
			assert.NoError(t, err, "HashFileCtx should not return error")
			assert.Equal(t, tt.wantHash, fmt.Sprintf("%x", hash),
				"Hash should match for algorithm %s", tt.algorithm)

			// Test with progress bar (false)
			hash, err = HashFileCtx(ctx, "bigfile.test", tt.algorithm, false)
			assert.NoError(t, err, "HashFileCtx with showProgress=false should not return error")
			assert.Equal(t, tt.wantHash, fmt.Sprintf("%x", hash),
				"Hash should match for algorithm %s with showProgress=false", tt.algorithm)

			// Test with progress bar (true) - only for non-imohash to avoid spinner issues in tests
			if tt.algorithm != "imohash" {
				hash, err = HashFileCtx(ctx, "bigfile.test", tt.algorithm, true)
				assert.NoError(t, err, "HashFileCtx with showProgress=true should not return error")
				assert.Equal(t, tt.wantHash, fmt.Sprintf("%x", hash),
					"Hash should match for algorithm %s with showProgress=true", tt.algorithm)
			}
		})
	}

	// Test symlink handling - match original behavior
	t.Run("Symlink handling", func(t *testing.T) {
		// Create symlink to bigfile.test
		symlinkPath := "bigfile.test.symlink"
		defer os.Remove(symlinkPath)

		err := os.Symlink("bigfile.test", symlinkPath)
		if err != nil && strings.Contains(err.Error(), "privilege") {
			t.Skip("Skipping symlink test - requires privilege")
		}
		assert.NoError(t, err, "Should create symlink")

		// Hash the symlink
		hash, err := HashFileCtx(ctx, symlinkPath, "md5")
		assert.NoError(t, err, "Should hash symlink target path")
		assert.NotNil(t, hash, "Should return hash for symlink")

		// The original HashFile returns []byte(SHA256(target))
		// SHA256("bigfile.test") = "3ae29e98bba80ccefc79289c59cc34cb7223954310bb61c6a26147bb9b08c4e4"
		// []byte("3ae29e98...") = ASCII bytes of hex string

		// When converted back with fmt.Sprintf("%x", hash):
		// ASCII '3' = 0x33, 'a' = 0x61, 'e' = 0x65, '2' = 0x32, etc.
		// So fmt.Sprintf("%x", []byte("3ae2...")) = "33616532..."

		actualHex := fmt.Sprintf("%x", hash)

		// Let's compute what we SHOULD get:
		targetPath := "bigfile.test"
		expectedSHA256Hex := SHA256(targetPath) // "3ae29e98..."
		expectedBytes := []byte(expectedSHA256Hex)
		expectedResultHex := fmt.Sprintf("%x", expectedBytes) // hex of ASCII bytes

		// Debug
		t.Logf("Target path: '%s'", targetPath)
		t.Logf("SHA256(target) hex: %s", expectedSHA256Hex)
		t.Logf("Expected result (hex of ASCII bytes): %s", expectedResultHex)
		t.Logf("Actual result: %s", actualHex)

		// They should match!
		assert.Equal(t, expectedResultHex, actualHex,
			"HashFileCtx should behave exactly like HashFile for symlinks")

		// Also test with original HashFile to ensure consistency
		originalHash, err := HashFile(symlinkPath, "md5")
		assert.NoError(t, err)
		originalHex := fmt.Sprintf("%x", originalHash)

		assert.Equal(t, originalHex, actualHex,
			"HashFileCtx should return same result as HashFile for symlinks")
	})
	// Test error cases
	t.Run("Error cases", func(t *testing.T) {
		// Non-existent file
		hash, err := HashFileCtx(ctx, "non_existent_file_12345.test", "md5")
		assert.Error(t, err, "Should return error for non-existent file")
		assert.Nil(t, hash, "Hash should be nil on error")

		// Unsupported algorithm
		hash, err = HashFileCtx(ctx, "bigfile.test", "unsupported_algo")
		assert.Error(t, err, "Should return error for unsupported algorithm")
		assert.Contains(t, err.Error(), "unsupported algorithm")
		assert.Nil(t, hash, "Hash should be nil on error")
	})
}

// TestHashFileCtxWithCancellation tests HashFileCtx with context cancellation
func TestHashFileCtxWithCancellation(t *testing.T) {
	// Use the same bigFile() function
	bigFile()
	defer os.Remove("bigfile.test")

	// Test 1: Cancel before starting
	t.Run("Cancel before start", func(t *testing.T) {
		ctx, cancel := context.WithCancel(context.Background())
		cancel() // Cancel immediately

		hash, err := HashFileCtx(ctx, "bigfile.test", "md5")
		assert.Error(t, err, "Should return error when context cancelled before start")
		assert.Equal(t, context.Canceled, err, "Error should be context.Canceled")
		assert.Nil(t, hash, "Hash should be nil when cancelled")
	})

	// Test 2: Cancel during operation
	t.Run("Cancel during operation", func(t *testing.T) {
		ctx, cancel := context.WithCancel(context.Background())

		// Start hash operation in goroutine
		errCh := make(chan error, 1)
		hashCh := make(chan []byte, 1)

		go func() {
			hash, err := HashFileCtx(ctx, "bigfile.test", "md5", false)
			if err != nil {
				errCh <- err
				hashCh <- nil
			} else {
				errCh <- nil
				hashCh <- hash
			}
		}()

		// Cancel after a short delay
		time.Sleep(10 * time.Millisecond)
		cancel()

		// Wait for result
		select {
		case err := <-errCh:
			hash := <-hashCh
			// Either we got an error (cancelled) or a hash (completed before cancellation)
			if err != nil {
				// Check if it's a context error
				if err == context.Canceled || err == context.DeadlineExceeded {
					assert.Error(t, err, "Should return context error when cancelled")
				}
				assert.Nil(t, hash, "Hash should be nil when cancelled")
			} else {
				// Completed successfully before cancellation
				assert.NotNil(t, hash, "If not cancelled, should return hash")
				assert.Equal(t, 16, len(hash), "MD5 hash should be 16 bytes")
				// Verify it's the correct hash
				assert.Equal(t, "8304ff018e02baad0e3555bade29a405", fmt.Sprintf("%x", hash))
			}
		case <-time.After(5 * time.Second):
			t.Fatal("Test timed out")
		}
	})

	// Test 3: Cancel with deadline
	t.Run("Cancel with deadline", func(t *testing.T) {
		ctx, cancel := context.WithTimeout(context.Background(), 1*time.Millisecond)
		defer cancel()

		// For a 75MB file, MD5 should take more than 1ms
		hash, err := HashFileCtx(ctx, "bigfile.test", "md5", false)
		assert.Error(t, err, "Should timeout for 75MB file with 1ms deadline")
		assert.Equal(t, context.DeadlineExceeded, err, "Error should be context.DeadlineExceeded")
		assert.Nil(t, hash, "Hash should be nil when deadline exceeded")
	})

	// Test 4: Imohash should be fast enough to complete before cancellation
	t.Run("Imohash fast completion", func(t *testing.T) {
		ctx, cancel := context.WithCancel(context.Background())
		defer cancel()

		// Imohash samples the file, so it should complete quickly
		hash, err := HashFileCtx(ctx, "bigfile.test", "imohash", false)
		assert.NoError(t, err, "Imohash should complete before any cancellation")
		assert.NotNil(t, hash, "Should return hash for imohash")
		assert.Equal(t, 16, len(hash), "Imohash should be 16 bytes")
		// Verify it's the correct hash
		assert.Equal(t, "c0d1e12301e6c635f6d4a8ea5c897437", fmt.Sprintf("%x", hash))
	})
}

// TestHashFileCtxEquivalence tests that HashFileCtx produces same results as original HashFile
func TestHashFileCtxEquivalence(t *testing.T) {
	// Use bigFile() for consistency
	bigFile()
	defer os.Remove("bigfile.test")

	algorithms := []string{"md5", "xxhash", "imohash", "highway"}

	for _, algorithm := range algorithms {
		t.Run(algorithm, func(t *testing.T) {
			// Get hash using original HashFile
			originalHash, err1 := HashFile("bigfile.test", algorithm)

			// Get hash using HashFileCtx with background context
			ctxHash, err2 := HashFileCtx(context.Background(), "bigfile.test", algorithm)

			// Both should succeed or fail together
			if err1 != nil {
				assert.Error(t, err2, "HashFileCtx should also fail if HashFile fails")
				t.Logf("Both failed as expected: %v", err1)
			} else {
				assert.NoError(t, err2, "HashFileCtx should not fail if HashFile succeeds")
				assert.NotNil(t, originalHash, "Original hash should not be nil")
				assert.NotNil(t, ctxHash, "Context hash should not be nil")

				// Compare hex representations
				originalHex := fmt.Sprintf("%x", originalHash)
				ctxHex := fmt.Sprintf("%x", ctxHash)
				assert.Equal(t, originalHex, ctxHex,
					"HashFile and HashFileCtx should produce same hash for algorithm %s. Got %s vs %s",
					algorithm, originalHex, ctxHex)

				// Also verify against known values from existing tests
				switch algorithm {
				case "md5":
					assert.Equal(t, "8304ff018e02baad0e3555bade29a405", originalHex)
				case "xxhash":
					assert.Equal(t, "4918740eb5ccb6f7", originalHex)
				case "imohash":
					assert.Equal(t, "c0d1e12301e6c635f6d4a8ea5c897437", originalHex)
				case "highway":
					assert.Equal(t, "3c32999529323ed66a67aeac5720c7bf1301dcc5dca87d8d46595e85ff990329", originalHex)
				}
			}
		})
	}
}

// TestHashFileCtxLargeFile tests with larger files (already using bigfile.test)
func TestHashFileCtxLargeFile(t *testing.T) {
	// Skip in short mode
	if testing.Short() {
		t.Skip("Skipping large file test in short mode")
	}

	// Use bigFile()
	bigFile()
	defer os.Remove("bigfile.test")

	ctx := context.Background()

	// Test each algorithm with large file
	algorithms := []string{"md5", "xxhash", "imohash", "highway"}

	for _, algorithm := range algorithms {
		t.Run(algorithm, func(t *testing.T) {
			hash, err := HashFileCtx(ctx, "bigfile.test", algorithm, false)
			assert.NoError(t, err, "Should hash large file with algorithm %s", algorithm)
			assert.NotNil(t, hash, "Should return hash for large file")

			// Verify hash size
			switch algorithm {
			case "md5":
				assert.Equal(t, 16, len(hash), "MD5 should be 16 bytes")
			case "xxhash":
				assert.Equal(t, 8, len(hash), "XXHash should be 8 bytes")
			case "imohash":
				assert.Equal(t, 16, len(hash), "Imohash should be 16 bytes")
			case "highway":
				assert.Equal(t, 32, len(hash), "HighwayHash should be 32 bytes")
			}

			// Verify against known values
			switch algorithm {
			case "md5":
				assert.Equal(t, "8304ff018e02baad0e3555bade29a405", fmt.Sprintf("%x", hash))
			case "xxhash":
				assert.Equal(t, "4918740eb5ccb6f7", fmt.Sprintf("%x", hash))
			case "imohash":
				assert.Equal(t, "c0d1e12301e6c635f6d4a8ea5c897437", fmt.Sprintf("%x", hash))
			case "highway":
				assert.Equal(t, "3c32999529323ed66a67aeac5720c7bf1301dcc5dca87d8d46595e85ff990329", fmt.Sprintf("%x", hash))
			}
		})
	}
}
```

