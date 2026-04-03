---
id: github.com-jsonnet-bundler-jsonnet-bundler-b281fb9
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:16.836879
---

# KNOWLEDGE EXTRACT: github.com_jsonnet-bundler_jsonnet-bundler_b281fb9d
> **Extracted on:** 2026-04-01 07:34:41
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519042/github.com_jsonnet-bundler_jsonnet-bundler_b281fb9d

---

## File: `.gitignore`
```
_output/
```

## File: `.header`
```
// Copyright 2018 jsonnet-bundler authors
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
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## 0.5.1 / 2022-06-22

- **[ENHANCEMENT]** Update dependencies and fix CI

## 0.5.0 / 2022-06-09

#### Changes:

- **[FEATURE]** Add --quiet option to suppress git progress output (#124)
- **[FEATURE]** Support Bitbucket personal repositories (#156)
- **[FEATURE]** Add --legacy-name flag #158
- **[ENHANCEMENT]** Windows enhancements (#110)
- **[BUGFIX]** Allow dots in a repository path's "user" section (#106)
- **[BUGFIX]** On windows, use `\` instead of `/` (#115)
- **[BUGFIX]** Replace `/` in version by `-` (#146)
- **[BUGFIX]** Correct path resolution to nested local dependencies (#151)

## 0.4.0 / 2020-05-15

You can now `jb update` a single dependency.  
Run `jb update github.com/org/repo` (supports multiple at ones).

#### Changes:

- **[FEATURE]** Update single dependencies (#92)
- **[FEATURE]** Skip dependencies (#99)
- **[ENHANCEMENT]** Add support for subgroups (#91) (#93)
- **[BUGFIX]** Fix local package with relative path (#100) (#103) (#104)
- **[BUGFIX]** Fix unarchiver (#86)

## 0.3.1 / 2020-03-01

#### BREAKING:

The format of `jsonnetfile.json` has changed. While v0.3.0 can
handle the old v0.2 format, v0.2 can't and must not be used with a
`jsonnetfile.json` created by v0.3.0

#### Changes:

- **[FEATURE] Absolute imports (#63)**: Introduces a new style for importing the
  packages installed by `jb`. The `<name>/<file>` style used before caused
  issues, as it was neither unique nor clearly defined what to import.  
  To address this, `jb` will now create a directory structure that allows to use
  import paths similar to Go: `host.tld/user/repo/subdir/file.libsonnet`.  
  The old stlye is still supported, this change is backwards compatible.  
  `jb rewrite` can be used to automatically convert your imports.
- **[FEATURE] `jsonnetfile.json` versions (#85)**: Adds a `verison` key to
  `jsonnetfile.json`, so that `jb` can automatically recognize the schema
  version and handle it properly, instead of panicking.
- **[FEATURE] Generic `git` `https://` (#73)**: Previously the `host.tld/user/repo` slug
  style was only supported for GitHub. All hosts work now.
- **[BUGFIX]** `--jsonnetpkg-home` not working (#80)

## 0.2.0 / 2020-01-08

- **[FEATURE]** Rework installation process adding checksums (#44)
- **[FEATURE]** Add local dependencies as source dependency (#36)
- **[ENHANCEMENT]** Only write jsonnnet files if we made changes (#56)
- **[ENHANCEMENT]** Package install optimizations for git (#38)
- **[ENHANCEMENT]** Add integration tests (#35)
- **[ENHANCEMENT]** Suppress detached head advice (#34)
- **[BUGFIX]** Make sure to fetch git tags (#58)

## 0.1.0 / 2019-04-23

This is the first release for jsonnet-bundler.
```

## File: `Dockerfile`
```
FROM busybox:1.35.0

COPY _output/linux/amd64/jb /

ENTRYPOINT ["/jb"]
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

   Copyright 2018 jsonnet-bundler authors

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

## File: `Makefile`
```
.PHONY: all check-license crossbuild build install test generate embedmd

SHELL=/bin/bash

GITHUB_URL=github.com/jsonnet-bundler/jsonnet-bundler
VERSION := $(shell git describe --tags --dirty --always)
GOPATH=$(HOME)/go
OUT_DIR=_output
BIN?=jb
PKGS=$(shell go list ./... | grep -v /vendor/)

all: check-license build generate test

# Binaries
LDFLAGS := '-s -w -extldflags "-static" -X main.Version=${VERSION}'
cross: clean
	CGO_ENABLED=0 gox \
	  -output="$(OUT_DIR)/jb-{{.OS}}-{{.Arch}}" \
	  -ldflags=$(LDFLAGS) \
	  -arch="amd64 arm64 arm" -os="linux" \
	  -arch="amd64 arm64" -os="darwin" \
	  -osarch="windows/amd64" \
	  ./cmd/$(BIN)

static:
	CGO_ENABLED=0 go build -ldflags=${LDFLAGS} -o $(OUT_DIR)/$(BIN) ./cmd/$(BIN)

build:
	CGO_ENABLED=0 go build -o $(OUT_DIR)/$(BIN) ./cmd/$(BIN)

install: static
	@echo ">> copying $(BIN) into $(GOPATH)/bin/$(BIN)"
	cp $(OUT_DIR)/$(BIN) $(GOPATH)/bin/$(BIN)

# Tests
test:
	@echo ">> running all unit tests"
	go test -v $(PKGS)

test-integration:
	@echo ">> running all integration tests"
	go test -v -tags=integration $(PKGS)

# Documentation
generate: embedmd
	@echo ">> generating docs"
	@./scripts/generate-help-txt.sh
	$(GOPATH)/bin/embedmd -w `find ./ -path ./vendor -prune -o -name "*.md" -print`

check-license:
	@echo ">> checking license headers"
	@./scripts/check_license.sh

embedmd:
	pushd /tmp && go install github.com/campoy/embedmd@latest && popd

# Other
clean:
	rm -rf $(OUT_DIR) $(BIN)

drone:
	drone jsonnet --format
```

## File: `README.md`
```markdown
# jsonnet-bundler

The jsonnet-bundler is a package manager for [Jsonnet](http://jsonnet.org/).

## Install

```
go install -a github.com/jsonnet-bundler/jsonnet-bundler/cmd/jb@latest
```
**NOTE**: please use a recent Go version to do this, ideally Go 1.13 or greater.

This will put `jb` in `$(go env GOPATH)/bin`. If you encounter the error
`jb: command not found` after installation then you may need to add that directory to your `$PATH` as shown [in their docs](https://golang.org/doc/code.html#GOPATH).

## Package Install

* [Arch Linux AUR](https://aur.archlinux.org/packages/jsonnet-bundler-bin)
* Mac OS X via Homebrew: `brew install jsonnet-bundler`
* Fedora (>= 32): `sudo dnf install golang-github-jsonnet-bundler`

## Features

- Fetches transitive dependencies
- Can vendor subtrees, as opposed to whole repositories


## Current Limitations

- Always downloads entire dependent repositories, even when updating
- If two dependencies depend on the same package (diamond problem), they must require the same version


## Example Usage

Initialize your project:

```sh
mkdir myproject
cd myproject
jb init
```

The existence of the `jsonnetfile.json` file means your directory is now a
jsonnet-bundler package that can define dependencies.

To depend on another package (another Github repository):
*Note that your dependency need not be initialized with a `jsonnetfile.json`.
If it is not, it is assumed it has no transitive dependencies.*

```sh
jb install https://github.com/anguslees/kustomize-libsonnet
```

Now write `myconfig.jsonnet`, which can import a file from that package.
Remember to use `-J vendor` when running Jsonnet to include the vendor tree.

```jsonnet
local kustomize = import 'kustomize-libsonnet/kustomize.libsonnet';

local my_resource = {
  metadata: {
    name: 'my-resource',
  },
};

kustomize.namePrefix('staging-')(my_resource)
```

To depend on a package that is in a subtree of a Github repo (this package also
happens to bring in a transitive dependency):

```sh
jb install https://github.com/prometheus-operator/prometheus-operator/jsonnet/prometheus-operator
```

*Note that if you are copy pasting from the Github website's address bar,
remove the `tree/master` from the path.*

If pushed to Github, your project can now be referenced from other packages in
the same way, with its dependencies fetched automatically.


## All command line flags

[embedmd]:# (_output/help.txt)
```txt
$ jb -h
usage: jb [<flags>] <command> [<args> ...]

A jsonnet package manager

Flags:
  -h, --help     Show context-sensitive help (also try --help-long and
                 --help-man).
      --version  Show application version.
      --jsonnetpkg-home="vendor"  
                 The directory used to cache packages in.
  -q, --quiet    Suppress any output from git command.

Commands:
  help [<command>...]
    Show help.

  init
    Initialize a new empty jsonnetfile

  install [<flags>] [<uris>...]
    Install new dependencies. Existing ones are silently skipped

  update [<uris>...]
    Update all or specific dependencies.

  rewrite
    Automatically rewrite legacy imports to absolute ones


```

## Design

This is an implemention of the design specified in this document: https://docs.google.com/document/d/1czRScSvvOiAJaIjwf3CogOULgQxhY9MkiBKOQI1yR14/edit#heading=h.upn4d5pcxy4c
```

## File: `VERSION`
```
v0.5.1
```

## File: `go.mod`
```
module github.com/jsonnet-bundler/jsonnet-bundler

go 1.18

require (
	github.com/elliotchance/orderedmap/v2 v2.2.0
	github.com/fatih/color v1.13.0
	github.com/pkg/errors v0.9.1
	github.com/stretchr/testify v1.7.4
	gopkg.in/alecthomas/kingpin.v2 v2.2.6
)

require (
	github.com/alecthomas/template v0.0.0-20190718012654-fb15b899a751 // indirect
	github.com/alecthomas/units v0.0.0-20211218093645-b94a6e3cc137 // indirect
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/kr/pretty v0.3.0 // indirect
	github.com/mattn/go-colorable v0.1.12 // indirect
	github.com/mattn/go-isatty v0.0.14 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	github.com/rogpeppe/go-internal v1.8.1 // indirect
	golang.org/x/sys v0.0.0-20220615213510-4f61da869c0c // indirect
	gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)
```

## File: `go.sum`
```
github.com/alecthomas/template v0.0.0-20190718012654-fb15b899a751 h1:JYp7IbQjafoB+tBA3gMyHYHrpOtNuDiK/uB5uXxq5wM=
github.com/alecthomas/template v0.0.0-20190718012654-fb15b899a751/go.mod h1:LOuyumcjzFXgccqObfd/Ljyb9UuFJ6TxHnclSeseNhc=
github.com/alecthomas/units v0.0.0-20211218093645-b94a6e3cc137 h1:s6gZFSlWYmbqAuRjVTiNNhvNRfY2Wxp9nhfyel4rklc=
github.com/alecthomas/units v0.0.0-20211218093645-b94a6e3cc137/go.mod h1:OMCwj8VM1Kc9e19TLln2VL61YJF0x1XFtfdL4JdbSyE=
github.com/creack/pty v1.1.9/go.mod h1:oKZEueFk5CKHvIhNR5MUki03XCEU+Q6VDXinZuGJ33E=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/elliotchance/orderedmap/v2 v2.2.0 h1:7/2iwO98kYT4XkOjA9mBEIwvi4KpGB4cyHeOFOnj4Vk=
github.com/elliotchance/orderedmap/v2 v2.2.0/go.mod h1:85lZyVbpGaGvHvnKa7Qhx7zncAdBIBq6u56Hb1PRU5Q=
github.com/fatih/color v1.13.0 h1:8LOYc1KYPPmyKMuN8QV2DNRWNbLo6LZ0iLs8+mlH53w=
github.com/fatih/color v1.13.0/go.mod h1:kLAiJbzzSOZDVNGyDpeOxJ47H46qBXwg5ILebYFFOfk=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pretty v0.2.1/go.mod h1:ipq/a2n7PKx3OHsz4KJII5eveXtPO4qwEXGdVfWzfnI=
github.com/kr/pretty v0.3.0 h1:WgNl7dwNpEZ6jJ9k1snq4pZsg7DOEN8hP9Xw0Tsjwk0=
github.com/kr/pretty v0.3.0/go.mod h1:640gp4NfQd8pI5XOwp5fnNeVWj67G7CFk/SaSQn7NBk=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/mattn/go-colorable v0.1.9/go.mod h1:u6P/XSegPjTcexA+o6vUJrdnUu04hMope9wVRipJSqc=
github.com/mattn/go-colorable v0.1.12 h1:jF+Du6AlPIjs2BiUiQlKOX0rt3SujHxPnksPKZbaA40=
github.com/mattn/go-colorable v0.1.12/go.mod h1:u5H1YNBxpqRaxsYJYSkiCWKzEfiAb1Gb520KVy5xxl4=
github.com/mattn/go-isatty v0.0.12/go.mod h1:cbi8OIDigv2wuxKPP5vlRcQ1OAZbq2CE4Kysco4FUpU=
github.com/mattn/go-isatty v0.0.14 h1:yVuAays6BHfxijgZPzw+3Zlu5yQgKGP2/hcQbHb7S9Y=
github.com/mattn/go-isatty v0.0.14/go.mod h1:7GGIvUiUoEMVVmxf/4nioHXj79iQHKdU27kJ6hsGG94=
github.com/pkg/diff v0.0.0-20210226163009-20ebb0f2a09e/go.mod h1:pJLUxLENpZxwdsKMEsNbx1VGcRFpLqf3715MtcvvzbA=
github.com/pkg/errors v0.9.1 h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=
github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rogpeppe/go-internal v1.6.1/go.mod h1:xXDCJY+GAPziupqXw64V24skbSoqbTEfhy4qGm1nDQc=
github.com/rogpeppe/go-internal v1.8.1 h1:geMPLpDpQOgVyCg5z5GoRwLHepNdb71NXb67XFkP+Eg=
github.com/rogpeppe/go-internal v1.8.1/go.mod h1:JeRgkft04UBgHMgCIwADu4Pn6Mtm5d4nPKWu0nJ5d+o=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.4.0/go.mod h1:YvHI0jy2hoMjB+UWwv71VJQ9isScKT/TqJzVSSt89Yw=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
github.com/stretchr/testify v1.7.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.7.4 h1:wZRexSlwd7ZXfKINDLsO4r7WBt3gTKONc6K/VesHvHM=
github.com/stretchr/testify v1.7.4/go.mod h1:yNjHg4UonilssWZ8iaSj1OCr/vHnekPRkoO+kdMU+MU=
golang.org/x/sys v0.0.0-20200116001909-b77594299b42/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200223170610-d5e6a3e2c0ae/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210630005230-0f9fa26af87c/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210927094055-39ccf1dd6fa6/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220615213510-4f61da869c0c h1:aFV+BgZ4svzjfabn8ERpuB4JI4N6/rdy1iusx77G3oU=
golang.org/x/sys v0.0.0-20220615213510-4f61da869c0c/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
gopkg.in/alecthomas/kingpin.v2 v2.2.6 h1:jMFz6MfLP0/4fUyZle81rXUoxOBFi19VUFKVDOQfozc=
gopkg.in/alecthomas/kingpin.v2 v2.2.6/go.mod h1:FMv+mEhP44yOT+4EoQTLFTRgOQ1FBLkstjWtayDeSgw=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/errgo.v2 v2.1.0/go.mod h1:hNsd1EY+bozCKY1Ytp96fpM3vjJbqLJn88ws8XvfDNI=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `cmd/jb/init.go`
```go
// Copyright 2018 jsonnet-bundler authors
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
	"encoding/json"
	"io/ioutil"
	"path/filepath"

	"gopkg.in/alecthomas/kingpin.v2"

	"github.com/jsonnet-bundler/jsonnet-bundler/pkg/jsonnetfile"
	v1 "github.com/jsonnet-bundler/jsonnet-bundler/spec/v1"
)

func initCommand(dir string) int {
	exists, err := jsonnetfile.Exists(jsonnetfile.File)
	kingpin.FatalIfError(err, "Failed to check for jsonnetfile.json")

	if exists {
		kingpin.Errorf("jsonnetfile.json already exists")
		return 1
	}

	s := v1.New()
	// TODO: disable them by default eventually
	// s.LegacyImports = false

	contents, err := json.MarshalIndent(s, "", "  ")
	kingpin.FatalIfError(err, "formatting jsonnetfile contents as json")
	contents = append(contents, []byte("\n")...)

	filename := filepath.Join(dir, jsonnetfile.File)

	ioutil.WriteFile(filename, contents, 0644)
	kingpin.FatalIfError(err, "Failed to write new jsonnetfile.json")

	return 0
}
```

## File: `cmd/jb/init_test.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package main

import (
	"io/ioutil"
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestInitCommand(t *testing.T) {
	tempDir, err := ioutil.TempDir("", "jb-init")
	if err != nil {
		t.Fatal(err)
	}
	defer os.Remove(tempDir)

	code := initCommand(tempDir)
	assert.Equal(t, 0, code)
}
```

## File: `cmd/jb/install.go`
```go
// Copyright 2018 jsonnet-bundler authors
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
	"encoding/json"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"reflect"

	"github.com/pkg/errors"
	"gopkg.in/alecthomas/kingpin.v2"

	"github.com/jsonnet-bundler/jsonnet-bundler/pkg"
	"github.com/jsonnet-bundler/jsonnet-bundler/pkg/jsonnetfile"
	v1 "github.com/jsonnet-bundler/jsonnet-bundler/spec/v1"
	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

func installCommand(dir, jsonnetHome string, uris []string, single bool, legacyName string) int {
	if dir == "" {
		dir = "."
	}

	jbfilebytes, err := ioutil.ReadFile(filepath.Join(dir, jsonnetfile.File))
	kingpin.FatalIfError(err, "failed to load jsonnetfile")

	jsonnetFile, err := jsonnetfile.Unmarshal(jbfilebytes)
	kingpin.FatalIfError(err, "")

	jblockfilebytes, err := ioutil.ReadFile(filepath.Join(dir, jsonnetfile.LockFile))
	if !os.IsNotExist(err) {
		kingpin.FatalIfError(err, "failed to load lockfile")
	}

	lockFile, err := jsonnetfile.Unmarshal(jblockfilebytes)
	kingpin.FatalIfError(err, "")

	kingpin.FatalIfError(
		os.MkdirAll(filepath.Join(dir, jsonnetHome, ".tmp"), os.ModePerm),
		"creating vendor folder")

	if len(uris) > 1 && legacyName != "" {
		log.Fatal("Cannot use --legacy-name with mutliple uris")
	}

	for _, u := range uris {
		d := deps.Parse(dir, u)
		if d == nil {
			kingpin.Fatalf("Unable to parse package URI `%s`", u)
		}

		if single {
			d.Single = true
		}

		if legacyName != "" {
			d.LegacyNameCompat = legacyName
		}

		jd, _ := jsonnetFile.Dependencies.Get(d.Name())
		if !depEqual(jd, *d) {
			// the dep passed on the cli is different from the jsonnetFile
			jsonnetFile.Dependencies.Set(d.Name(), *d)

			// we want to install the passed version (ignore the lock)
			lockFile.Dependencies.Delete(d.Name())
		}
	}

	jsonnetPkgHomeDir := filepath.Join(dir, jsonnetHome)
	locked, err := pkg.Ensure(jsonnetFile, jsonnetPkgHomeDir, lockFile.Dependencies)
	kingpin.FatalIfError(err, "failed to install packages")

	pkg.CleanLegacyName(jsonnetFile.Dependencies)

	kingpin.FatalIfError(
		writeChangedJsonnetFile(jbfilebytes, &jsonnetFile, filepath.Join(dir, jsonnetfile.File)),
		"updating jsonnetfile.json")

	kingpin.FatalIfError(
		writeChangedJsonnetFile(jblockfilebytes, &v1.JsonnetFile{Dependencies: locked}, filepath.Join(dir, jsonnetfile.LockFile)),
		"updating jsonnetfile.lock.json")

	return 0
}

func depEqual(d1, d2 deps.Dependency) bool {
	name := d1.Name() == d2.Name()
	version := d1.Version == d2.Version
	source := reflect.DeepEqual(d1.Source, d2.Source)

	return name && version && source
}

func writeJSONFile(name string, d interface{}) error {
	b, err := json.MarshalIndent(d, "", "  ")
	if err != nil {
		return errors.Wrap(err, "encoding json")
	}
	b = append(b, []byte("\n")...)

	return ioutil.WriteFile(name, b, 0644)
}

func writeChangedJsonnetFile(originalBytes []byte, modified *v1.JsonnetFile, path string) error {
	origJsonnetFile, err := jsonnetfile.Unmarshal(originalBytes)
	if err != nil {
		return err
	}

	if reflect.DeepEqual(origJsonnetFile, *modified) {
		return nil
	}

	return writeJSONFile(path, *modified)
}
```

## File: `cmd/jb/install_test.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package main

import (
	"encoding/json"
	"io/ioutil"
	"os"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/jsonnet-bundler/jsonnet-bundler/pkg/jsonnetfile"
	v1 "github.com/jsonnet-bundler/jsonnet-bundler/spec/v1"
	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

const initContents = `{"version": 1, "dependencies": [], "legacyImports": true}`

func TestInstallCommand(t *testing.T) {
	testInstallCommandWithJsonnetHome(t, "vendor")
}

func TestInstallCommandCustomJsonnetHome(t *testing.T) {
	testInstallCommandWithJsonnetHome(t, "custom-vendor-dir")
}

func TestInstallCommandDeepCustomJsonnetHome(t *testing.T) {
	testInstallCommandWithJsonnetHome(t, "custom/vendor/dir")
}

func testInstallCommandWithJsonnetHome(t *testing.T, jsonnetHome string) {
	testcases := []struct {
		Name                    string
		URIs                    []string
		ExpectedCode            int
		ExpectedJsonnetFile     []byte
		ExpectedJsonnetLockFile []byte
		single                  bool
	}{
		{
			Name:                "NoURLs",
			ExpectedCode:        0,
			ExpectedJsonnetFile: []byte(initContents),
		},
		{
			Name:                    "OneURL",
			URIs:                    []string{"github.com/jsonnet-bundler/jsonnet-bundler@v0.1.0"},
			ExpectedCode:            0,
			ExpectedJsonnetFile:     []byte(`{"version": 1, "dependencies": [{"source": {"git": {"remote": "https://github.com/jsonnet-bundler/jsonnet-bundler.git", "subdir": ""}}, "version": "v0.1.0"}], "legacyImports": true}`),
			ExpectedJsonnetLockFile: []byte(`{"version": 1, "dependencies": [{"source": {"git": {"remote": "https://github.com/jsonnet-bundler/jsonnet-bundler.git", "subdir": ""}}, "version": "080f157c7fb85ad0281ea78f6c641eaa570a582f", "sum": "W1uI550rQ66axRpPXA2EZDquyPg/5PHZlvUz1NEzefg="}], "legacyImports": false}`),
		},
		{
			Name:                    "Local",
			URIs:                    []string{"jsonnet/foobar"},
			ExpectedCode:            0,
			ExpectedJsonnetFile:     []byte(`{"version": 1, "dependencies": [{"source": {"local": {"directory": "jsonnet/foobar"}}, "version": ""}], "legacyImports": true}`),
			ExpectedJsonnetLockFile: []byte(`{"version": 1, "dependencies": [{"source": {"local": {"directory": "jsonnet/foobar"}}, "version": ""}], "legacyImports": false}`),
		},
		{
			Name:                    "single",
			URIs:                    []string{"github.com/grafana/loki/production/ksonnet/loki@bd4d516262c107a0bde7a962fa2b1e567a2c21e5"},
			ExpectedCode:            0,
			ExpectedJsonnetFile:     []byte(`{"version":1,"dependencies":[{"source":{"git":{"remote":"https://github.com/grafana/loki.git","subdir":"production/ksonnet/loki"}},"version":"bd4d516262c107a0bde7a962fa2b1e567a2c21e5","single":true}],"legacyImports":true}`),
			ExpectedJsonnetLockFile: []byte(`{"version":1,"dependencies":[{"source":{"git":{"remote":"https://github.com/grafana/loki.git","subdir":"production/ksonnet/loki"}},"version":"bd4d516262c107a0bde7a962fa2b1e567a2c21e5","sum":"ExovUKXmZ4KwJAv/q8ZwNW9BdIZlrxmoGrne7aR64wo=","single":true}],"legacyImports":false}`),
			single:                  true,
		},
	}

	localDependency := "jsonnet/foobar"

	cleanup := func() {
		_ = os.Remove(jsonnetfile.File)
		_ = os.Remove(jsonnetfile.LockFile)
		_ = os.RemoveAll(jsonnetHome)
		_ = os.RemoveAll("jsonnet")
	}

	for _, tc := range testcases {
		_ = t.Run(tc.Name, func(t *testing.T) {
			cleanup()

			err := os.MkdirAll(localDependency, os.ModePerm)
			assert.NoError(t, err)

			// init + check it works correctly (legacyImports true, empty dependencies)
			initCommand("")
			jsonnetFileContent(t, jsonnetfile.File, []byte(initContents))

			// install something, check it writes only if required, etc.
			installCommand("", jsonnetHome, tc.URIs, tc.single, "")
			jsonnetFileContent(t, jsonnetfile.File, tc.ExpectedJsonnetFile)
			if tc.ExpectedJsonnetLockFile != nil {
				jsonnetFileContent(t, jsonnetfile.LockFile, tc.ExpectedJsonnetLockFile)
			}
		})
	}

	cleanup()
}

func jsonnetFileContent(t *testing.T, filename string, content []byte) {
	t.Helper()

	bytes, err := ioutil.ReadFile(filename)
	assert.NoError(t, err)
	if eq := assert.JSONEq(t, string(content), string(bytes)); !eq {
		t.Log(string(bytes))
	}
}

func TestWriteChangedJsonnetFile(t *testing.T) {
	testcases := []struct {
		Name             string
		JsonnetFileBytes []byte
		NewJsonnetFile   v1.JsonnetFile
		ExpectWrite      bool
	}{
		{
			Name:             "NoDiffEmpty",
			JsonnetFileBytes: []byte(`{}`),
			NewJsonnetFile:   v1.New(),
			ExpectWrite:      false,
		},
		{
			Name:             "NoDiffNotEmpty",
			JsonnetFileBytes: []byte(`{"dependencies": [{"version": "master"}]}`),
			NewJsonnetFile: v1.JsonnetFile{
				Dependencies: addDependencies(deps.NewOrdered(),
					deps.Dependency{
						Version: "master",
					}),
			},
			ExpectWrite: false,
		},
		{
			Name:             "DiffVersion",
			JsonnetFileBytes: []byte(`{"dependencies": [{"version": "1.0"}]}`),
			NewJsonnetFile: v1.JsonnetFile{
				Dependencies: addDependencies(deps.NewOrdered(),
					deps.Dependency{
						Version: "2.0",
					}),
			},
			ExpectWrite: true,
		},
		{
			Name:             "Diff",
			JsonnetFileBytes: []byte(`{}`),
			NewJsonnetFile: v1.JsonnetFile{
				Dependencies: addDependencies(deps.NewOrdered(),
					deps.Dependency{
						Source: deps.Source{
							GitSource: &deps.Git{
								Scheme: deps.GitSchemeHTTPS,
								Host:   "github.com",
								User:   "foobar",
								Repo:   "foobar",
								Subdir: "",
							},
						},
						Version: "master",
					}),
			},
			ExpectWrite: true,
		},
	}
	outputjsonnetfile := "changedjsonnet.json"
	for _, tc := range testcases {
		_ = t.Run(tc.Name, func(t *testing.T) {
			clean := func() {
				_ = os.Remove(outputjsonnetfile)
			}
			clean()
			defer clean()

			err := writeChangedJsonnetFile(tc.JsonnetFileBytes, &tc.NewJsonnetFile, outputjsonnetfile)
			assert.NoError(t, err)

			if tc.ExpectWrite {
				assert.FileExists(t, outputjsonnetfile)
			} else {
				_, err := os.Lstat(outputjsonnetfile)
				if err != nil {
					assert.True(t, os.IsNotExist(err))
				}
			}
		})
	}
}

func TestInstallTransitive(t *testing.T) {
	const (
		frozenLibFirstCommit  = "9f40207f668e382b706e1822f2d46ce2cd0a57cc"
		frozenLibSecondCommit = "ed7c1aff9e10d3b42fb130446d495f1c769ecd7b"
	)

	baseDir := t.TempDir()
	subDirA := filepath.Join(baseDir, "a")
	subDirB := filepath.Join(baseDir, "b")

	writeDepFileTree(t, map[string]v1.JsonnetFile{
		baseDir: {
			Dependencies: addDependencies(deps.NewOrdered(),
				localDependency(subDirA),
				localDependency(subDirB),
			)},
		subDirA: jsonnetFileWithFrozenLib(frozenLibFirstCommit, ""),
		subDirB: jsonnetFileWithFrozenLib(frozenLibSecondCommit, ""),
	})

	require.Equal(t, 0, installCommand(baseDir, "vendor", nil, false, ""))

	lockCheckFrozenLibVersion(t, filepath.Join(baseDir, "jsonnetfile.lock.json"), frozenLibFirstCommit)
	require.NoError(t, os.RemoveAll(filepath.Join(baseDir, "jsonnetfile.lock.json")))

	// Reverse the order of the dependencies. The lock file should now contain the second commit in its version field.
	writeDepFileTree(t, map[string]v1.JsonnetFile{
		subDirA: jsonnetFileWithFrozenLib(frozenLibSecondCommit, ""),
		subDirB: jsonnetFileWithFrozenLib(frozenLibFirstCommit, ""),
	})

	require.Equal(t, 0, installCommand(baseDir, "vendor", nil, false, ""))

	lockCheckFrozenLibVersion(t, filepath.Join(baseDir, "jsonnetfile.lock.json"), frozenLibSecondCommit)
}

func lockCheckFrozenLibVersion(t *testing.T, lockPath, version string) {
	t.Helper()

	rawLock, err := os.ReadFile(lockPath)
	require.NoError(t, err)
	var lock v1.JsonnetFile
	require.NoError(t, json.Unmarshal([]byte(rawLock), &lock))

	lf, lfExists := lock.Dependencies.Get("github.com/jsonnet-bundler/frozen-lib")
	require.True(t, lfExists, "expected to find frozen-lib in lock file")
	require.Equal(t, version, lf.Version, "lock file: expected frozen-lib to have commit version of the first dependency in the base jsonnet file")
}

func addDependencies(o *deps.Ordered, ds ...deps.Dependency) *deps.Ordered {
	for _, d := range ds {
		o.Set(d.Name(), d)
	}
	return o
}

func jsonnetFileWithFrozenLib(version, sum string) v1.JsonnetFile {
	return v1.JsonnetFile{
		Dependencies: addDependencies(deps.NewOrdered(),
			frozenDependency(version, sum)),
	}
}

func frozenDependency(version, sum string) deps.Dependency {
	return deps.Dependency{
		Source: deps.Source{
			GitSource: &deps.Git{
				Scheme: "https://",
				Host:   "github.com",
				User:   "jsonnet-bundler",
				Repo:   "frozen-lib",
			},
		},
		Version: version,
		Sum:     sum,
	}
}

func localDependency(dir string) deps.Dependency {
	return deps.Dependency{
		Source: deps.Source{
			LocalSource: &deps.Local{
				Directory: dir,
			},
		},
	}
}

func writeDepFileTree(t *testing.T, files map[string]v1.JsonnetFile) {
	t.Helper()

	for dir, file := range files {
		require.NoError(t, os.MkdirAll(dir, os.ModePerm))
		rj, err := json.Marshal(file)
		require.NoError(t, err)
		require.NoError(t, os.WriteFile(filepath.Join(dir, "jsonnetfile.json"), rj, 0644))
	}
}
```

## File: `cmd/jb/main.go`
```go
// Copyright 2018 jsonnet-bundler authors
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
	"fmt"
	"os"
	"path/filepath"

	"github.com/fatih/color"
	"github.com/pkg/errors"
	"gopkg.in/alecthomas/kingpin.v2"

	"github.com/jsonnet-bundler/jsonnet-bundler/pkg"
)

const (
	installActionName = "install"
	updateActionName  = "update"
	initActionName    = "init"
	rewriteActionName = "rewrite"
)

var Version = "dev"

func main() {
	os.Exit(Main())
}

func Main() int {
	cfg := struct {
		JsonnetHome string
	}{}

	color.Output = color.Error

	a := kingpin.New(filepath.Base(os.Args[0]), "A jsonnet package manager").Version(Version)
	a.HelpFlag.Short('h')

	a.Flag("jsonnetpkg-home", "The directory used to cache packages in.").
		Default("vendor").StringVar(&cfg.JsonnetHome)
	a.Flag("quiet", "Suppress any output from git command.").
		Short('q').BoolVar(&pkg.GitQuiet)

	initCmd := a.Command(initActionName, "Initialize a new empty jsonnetfile")

	installCmd := a.Command(installActionName, "Install new dependencies. Existing ones are silently skipped")
	installCmdURIs := installCmd.Arg("uris", "URIs to packages to install, URLs or file paths").Strings()
	installCmdSingle := installCmd.Flag("single", "install package without dependencies").Short('1').Bool()
	installCmdLegacyName := installCmd.Flag("legacy-name", "set legacy name").String()

	updateCmd := a.Command(updateActionName, "Update all or specific dependencies.")
	updateCmdURIs := updateCmd.Arg("uris", "URIs to packages to update, URLs or file paths").Strings()

	rewriteCmd := a.Command(rewriteActionName, "Automatically rewrite legacy imports to absolute ones")

	command, err := a.Parse(os.Args[1:])
	if err != nil {
		fmt.Fprintln(os.Stderr, errors.Wrapf(err, "Error parsing commandline arguments"))
		a.Usage(os.Args[1:])
		return 2
	}

	workdir, err := os.Getwd()
	if err != nil {
		return 1
	}

	cfg.JsonnetHome = filepath.Clean(cfg.JsonnetHome)

	switch command {
	case initCmd.FullCommand():
		return initCommand(workdir)
	case installCmd.FullCommand():
		return installCommand(workdir, cfg.JsonnetHome, *installCmdURIs, *installCmdSingle, *installCmdLegacyName)
	case updateCmd.FullCommand():
		return updateCommand(workdir, cfg.JsonnetHome, *updateCmdURIs)
	case rewriteCmd.FullCommand():
		return rewriteCommand(workdir, cfg.JsonnetHome)
	default:
		installCommand(workdir, cfg.JsonnetHome, []string{}, false, "")
	}

	return 0
}
```

## File: `cmd/jb/main_test.go`
```go
// Copyright 2018 jsonnet-bundler authors
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
	"os"
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

func TestParseDependency(t *testing.T) {
	const testFolder = "test/jsonnet/foobar"
	err := os.MkdirAll(testFolder, os.ModePerm)
	if err != nil {
		t.Fatal(err)
	}
	defer os.RemoveAll("test")

	tests := []struct {
		name string
		path string
		want *deps.Dependency
	}{
		{
			name: "Empty",
			path: "",
			want: nil,
		},
		{
			name: "Invalid",
			path: "example.com/foo",
			want: nil,
		},
		{
			name: "GitHTTPS",
			path: "example.com/jsonnet-bundler/jsonnet-bundler",
			want: &deps.Dependency{
				Source: deps.Source{
					GitSource: &deps.Git{
						Scheme: deps.GitSchemeHTTPS,
						Host:   "example.com",
						User:   "jsonnet-bundler",
						Repo:   "jsonnet-bundler",
						Subdir: "",
					},
				},
				Version: "master",
			},
		},
		{
			name: "SSH",
			path: "git+ssh://git@github.com/jsonnet-bundler/jsonnet-bundler.git",
			want: &deps.Dependency{
				Source: deps.Source{
					GitSource: &deps.Git{
						Scheme: deps.GitSchemeSSH,
						Host:   "github.com",
						User:   "jsonnet-bundler",
						Repo:   "jsonnet-bundler",
						Subdir: "",
					},
				},
				Version: "master",
			},
		},
		{
			name: "local",
			path: testFolder,
			want: &deps.Dependency{
				Source: deps.Source{
					LocalSource: &deps.Local{
						Directory: "test/jsonnet/foobar",
					},
				},
				Version: "",
			},
		},
	}
	for _, tt := range tests {
		_ = t.Run(tt.name, func(t *testing.T) {
			dependency := deps.Parse("", tt.path)

			if tt.path == "" {
				assert.Nil(t, dependency)
			} else {
				assert.Equal(t, tt.want, dependency)
			}
		})
	}
}
```

## File: `cmd/jb/rewrite.go`
```go
// Copyright 2018 jsonnet-bundler authors
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
	"path/filepath"

	kingpin "gopkg.in/alecthomas/kingpin.v2"

	"github.com/jsonnet-bundler/jsonnet-bundler/pkg/jsonnetfile"
	"github.com/jsonnet-bundler/jsonnet-bundler/tool/rewrite"
)

func rewriteCommand(dir, vendorDir string) int {
	locks, err := jsonnetfile.Load(filepath.Join(dir, jsonnetfile.LockFile))
	if err != nil {
		kingpin.Fatalf("Failed to load lockFile: %s.\nThe locks are required to compute the new import names. Make sure to run `jb install` first.", err)
	}

	if err := rewrite.Rewrite(dir, vendorDir, locks.Dependencies); err != nil {
		kingpin.FatalIfError(err, "")
	}

	return 0
}
```

## File: `cmd/jb/update.go`
```go
// Copyright 2018 jsonnet-bundler authors
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
	"os"
	"path/filepath"

	"gopkg.in/alecthomas/kingpin.v2"

	"github.com/jsonnet-bundler/jsonnet-bundler/pkg"
	"github.com/jsonnet-bundler/jsonnet-bundler/pkg/jsonnetfile"
	v1 "github.com/jsonnet-bundler/jsonnet-bundler/spec/v1"
	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

func updateCommand(dir, jsonnetHome string, uris []string) int {
	if dir == "" {
		dir = "."
	}

	// load jsonnetfiles
	jsonnetFile, err := jsonnetfile.Load(filepath.Join(dir, jsonnetfile.File))
	kingpin.FatalIfError(err, "failed to load jsonnetfile")

	lockFile, err := jsonnetfile.Load(filepath.Join(dir, jsonnetfile.LockFile))
	kingpin.FatalIfError(err, "failed to load lockfile")

	kingpin.FatalIfError(
		os.MkdirAll(filepath.Join(dir, jsonnetHome, ".tmp"), os.ModePerm),
		"creating vendor folder")

	locks := lockFile.Dependencies

	for _, u := range uris {
		d := deps.Parse(dir, u)
		if d == nil {
			kingpin.Fatalf("Unable to parse package URI `%s`", u)
		}

		locks.Delete(d.Name())
	}

	// no uris: update all
	if len(uris) == 0 {
		locks = deps.NewOrdered()
	}

	newLocks, err := pkg.Ensure(jsonnetFile, filepath.Join(dir, jsonnetHome), locks)
	kingpin.FatalIfError(err, "updating")

	kingpin.FatalIfError(
		writeJSONFile(filepath.Join(dir, jsonnetfile.LockFile), v1.JsonnetFile{Dependencies: newLocks}),
		"updating jsonnetfile.lock.json")

	return 0
}
```

## File: `cmd/jb/update_test.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package main

import (
	"io/ioutil"
	"os"
	"path/filepath"
	"testing"

	"github.com/jsonnet-bundler/jsonnet-bundler/pkg/jsonnetfile"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

// RepoState describes a point in time of a repository
type RepoState struct {
	File string
	Lock string
}

// FilePath is the path to the jsonnetfile.json
func (rs RepoState) FilePath(dir string) string {
	return filepath.Join(dir, jsonnetfile.File)
}

// LockPath is the path to the jsonnetfile.lock.json
func (rs RepoState) LockPath(dir string) string {
	return filepath.Join(dir, jsonnetfile.LockFile)
}

// Write writes this state to dir
func (rs RepoState) Write(dir string) error {
	if err := ioutil.WriteFile(rs.FilePath(dir), []byte(rs.File), 0644); err != nil {
		return err
	}
	if err := ioutil.WriteFile(rs.LockPath(dir), []byte(rs.Lock), 0644); err != nil {
		return err
	}
	if err := os.MkdirAll(filepath.Join(dir, "vendor/"), os.ModePerm); err != nil {
		return err
	}
	return nil
}

// Assert checks that dir matches this state
func (rs RepoState) Assert(t *testing.T, dir string) {
	file, err := ioutil.ReadFile(rs.FilePath(dir))
	require.NoError(t, err)
	assert.JSONEq(t, rs.File, string(file))

	lock, err := ioutil.ReadFile(rs.LockPath(dir))
	require.NoError(t, err)
	assert.JSONEq(t, rs.Lock, string(lock))
}

// UpdateCase is a testcase for jb update
type UpdateCase struct {
	name   string
	uris   []string
	before *RepoState
	after  *RepoState
}

func (u UpdateCase) Run(t *testing.T) {
	dir, err := ioutil.TempDir("", u.name)
	require.NoError(t, err)
	defer os.RemoveAll(dir)

	if u.before == nil {
		initCommand(dir)
	} else {
		err = u.before.Write(dir)
		require.NoError(t, err)
	}

	ret := updateCommand(dir, "vendor", u.uris)
	assert.Equal(t, ret, 0)

	if u.after != nil {
		u.after.Assert(t, dir)
	}
}

func TestUpdate(t *testing.T) {
	cases := []UpdateCase{
		{
			name: "simple",
			uris: []string{}, // no uris
			before: &RepoState{
				File: `{"version":1,"dependencies":[{"source":{"git":{"remote":"https://github.com/jsonnet-bundler/frozen-lib.git","subdir":""}},"version":"master"}],"legacyImports":true}`,
				Lock: `{"version":1,"dependencies":[{"source":{"git":{"remote":"https://github.com/jsonnet-bundler/frozen-lib.git","subdir":""}},"version":"9f40207f668e382b706e1822f2d46ce2cd0a57cc","sum":"qUJDskVRtmkTms2udvFpLi1t5YKVbGmMSyiZnPjXsMo="}],"legacyImports":false}`,
			},
			after: &RepoState{
				File: `{"version":1,"dependencies":[{"source":{"git":{"remote":"https://github.com/jsonnet-bundler/frozen-lib.git","subdir":""}},"version":"master"}],"legacyImports":true}`,
				Lock: `{"version":1,"dependencies":[{"source":{"git":{"remote":"https://github.com/jsonnet-bundler/frozen-lib.git","subdir":""}},"version":"ed7c1aff9e10d3b42fb130446d495f1c769ecd7b","sum":"OraOcUvDIx9Eikaihi8XsRNRsVehO75Ek35im/jYoSA="}],"legacyImports":false}`,
			},
		},
		{
			name: "single",
			uris: []string{"github.com/jsonnet-bundler/frozen-lib"},
			before: &RepoState{
				File: `{"version":1,"dependencies":[{"source":{"git":{"remote":"https://github.com/grafana/jsonnet-libs.git","subdir":"ksonnet-util"}},"version":"master"},{"source":{"git":{"remote":"https://github.com/jsonnet-bundler/frozen-lib.git","subdir":""}},"version":"master"}],"legacyImports":true}`,
				Lock: `{"version":1,"dependencies":[{"source":{"git":{"remote":"https://github.com/grafana/jsonnet-libs.git","subdir":"ksonnet-util"}},"version":"610b00d219d0a6f3d833dd44e4bb0deda2429da0","sum":"XdIrw3m7I8fJ3CL9eR8LtuYcanf2QK78n4H4OBBOADc="},{"source":{"git":{"remote":"https://github.com/jsonnet-bundler/frozen-lib.git","subdir":""}},"version":"9f40207f668e382b706e1822f2d46ce2cd0a57cc","sum":"qUJDskVRtmkTms2udvFpLi1t5YKVbGmMSyiZnPjXsMo="}],"legacyImports":false}`,
			},
			after: &RepoState{
				File: `{"version":1,"dependencies":[{"source":{"git":{"remote":"https://github.com/grafana/jsonnet-libs.git","subdir":"ksonnet-util"}},"version":"master"},{"source":{"git":{"remote":"https://github.com/jsonnet-bundler/frozen-lib.git","subdir":""}},"version":"master"}],"legacyImports":true}`,
				Lock: `{"version":1,"dependencies":[{"source":{"git":{"remote":"https://github.com/grafana/jsonnet-libs.git","subdir":"ksonnet-util"}},"version":"610b00d219d0a6f3d833dd44e4bb0deda2429da0","sum":"XdIrw3m7I8fJ3CL9eR8LtuYcanf2QK78n4H4OBBOADc="},{"source":{"git":{"remote":"https://github.com/jsonnet-bundler/frozen-lib.git","subdir":""}},"version":"ed7c1aff9e10d3b42fb130446d495f1c769ecd7b","sum":"OraOcUvDIx9Eikaihi8XsRNRsVehO75Ek35im/jYoSA="}],"legacyImports":false}`,
			},
		},
	}

	for _, c := range cases {
		t.Run(c.name, c.Run)
	}
}
```

## File: `pkg/git.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package pkg

import (
	"archive/tar"
	"bytes"
	"compress/gzip"
	"context"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	"os/exec"
	"path"
	"path/filepath"
	"regexp"
	"strings"

	"github.com/fatih/color"
	"github.com/pkg/errors"

	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

type GitPackage struct {
	Source *deps.Git
}

func NewGitPackage(source *deps.Git) Interface {
	return &GitPackage{
		Source: source,
	}
}

var GitQuiet = false

func downloadGitHubArchive(filepath string, url string) error {
	// Get the data
	resp, err := http.Get(url)
	if err != nil {
		return err
	}
	if !GitQuiet {
		color.Cyan("GET %s %d", url, resp.StatusCode)
	}
	if resp.StatusCode != 200 {
		return fmt.Errorf("unexpected status code %d", resp.StatusCode)
	}

	defer resp.Body.Close()

	// Create the file
	out, err := os.Create(filepath)
	if err != nil {
		return err
	}
	defer out.Close()

	// Write the body to file
	_, err = io.Copy(out, resp.Body)
	if err != nil {
		return err
	}

	return nil
}

func gzipUntar(dst string, r io.Reader, subDir string) error {
	gzr, err := gzip.NewReader(r)
	if err != nil {
		return err
	}
	defer gzr.Close()

	tr := tar.NewReader(gzr)

	for {
		header, err := tr.Next()
		switch {
		case err == io.EOF:
			return nil

		case err != nil:
			return err

		case header == nil:
			continue
		}

		// strip the two first components of the path
		parts := strings.SplitAfterN(header.Name, "/", 2)
		if len(parts) < 2 {
			continue
		}
		suffix := parts[1]
		prefix := dst

		// reconstruct the target parh for the archive entry
		target := filepath.Join(prefix, suffix)

		// if subdir is provided and target is not under it, skip it
		subDirPath := filepath.Join(prefix, subDir)
		if subDir != "" && !strings.HasPrefix(target, subDirPath) {
			continue
		}

		// check the file type
		switch header.Typeflag {

		// create directories as needed
		case tar.TypeDir:
			if err := os.MkdirAll(target, os.FileMode(header.Mode)); err != nil {
				return err
			}

		case tar.TypeReg:
			if err := os.MkdirAll(filepath.Dir(target), os.ModePerm); err != nil {
				return err
			}

			err := func() error {
				f, err := os.OpenFile(target, os.O_CREATE|os.O_RDWR, os.FileMode(header.Mode))
				if err != nil {
					return err
				}
				defer f.Close()

				// copy over contents
				if _, err := io.Copy(f, tr); err != nil {
					return err
				}
				return nil
			}()

			if err != nil {
				return err
			}

		case tar.TypeSymlink:
			if err := os.MkdirAll(filepath.Dir(target), os.ModePerm); err != nil {
				return err
			}

			if err := os.Symlink(header.Linkname, target); err != nil {
				return err
			}
		}
	}
}

func remoteResolveRef(ctx context.Context, remote string, ref string) (string, error) {
	b := &bytes.Buffer{}
	cmd := exec.CommandContext(ctx, "git", "ls-remote", "--heads", "--tags", "--refs", "--quiet", remote, ref)
	cmd.Stdin = os.Stdin
	cmd.Stdout = b
	cmd.Stderr = os.Stderr
	err := cmd.Run()
	if err != nil {
		return "", err
	}
	commitShaPattern := regexp.MustCompile("^([0-9a-f]{40,})\\b")
	commitSha := commitShaPattern.FindString(b.String())
	return commitSha, nil
}

func (p *GitPackage) Install(ctx context.Context, name, dir, version string) (string, error) {
	destPath := path.Join(dir, name)

	pkgh := sha256.Sum256([]byte(fmt.Sprintf("jsonnetpkg-%s-%s", strings.Replace(name, "/", "-", -1), strings.Replace(version, "/", "-", -1))))
	// using 16 bytes should be a good middle ground between length and collision resistance
	tmpDir, err := ioutil.TempDir(filepath.Join(dir, ".tmp"), hex.EncodeToString(pkgh[:16]))
	if err != nil {
		return "", errors.Wrap(err, "failed to create tmp dir")
	}
	defer os.RemoveAll(tmpDir)

	// Optimization for GitHub sources: download a tarball archive of the requested
	// version instead of cloning the entire
	isGitHubRemote, err := regexp.MatchString(`^(https|ssh)://github\.com/.+$`, p.Source.Remote())
	if isGitHubRemote {
		// Let git ls-remote decide if "version" is a ref or a commit SHA in the unlikely
		// but possible event that a ref is comprised of 40 or more hex characters
		commitSha, err := remoteResolveRef(ctx, p.Source.Remote(), version)

		// If the ref resolution failed and "version" looks like a SHA,
		// assume it is one and proceed.
		commitShaPattern := regexp.MustCompile("^([0-9a-f]{40,})$")
		if commitSha == "" && commitShaPattern.MatchString(version) {
			commitSha = version
		}

		archiveUrl := fmt.Sprintf("%s/archive/%s.tar.gz", strings.TrimSuffix(p.Source.Remote(), ".git"), commitSha)
		archiveFilepath := fmt.Sprintf("%s.tar.gz", tmpDir)

		defer os.Remove(archiveFilepath)
		err = downloadGitHubArchive(archiveFilepath, archiveUrl)
		if err == nil {
			var ar *os.File
			ar, err = os.Open(archiveFilepath)
			defer ar.Close()
			if err == nil {
				// Extract the sub-directory (if any) from the archive
				// If none specified, the entire archive is unpacked
				err = gzipUntar(tmpDir, ar, p.Source.Subdir)

				// Move the extracted directory to its final destination
				if err == nil {
					if err := os.MkdirAll(filepath.Dir(destPath), os.ModePerm); err != nil {
						panic(err)
					}
					if err := os.Rename(path.Join(tmpDir, p.Source.Subdir), destPath); err != nil {
						panic(err)
					}
				}
			}
		}

		if err == nil {
			return commitSha, nil
		}

		// The repository may be private or the archive download may not work
		// for other reasons. In any case, fall back to the slower git-based installation.
		color.Yellow("archive install failed: %s", err)
		color.Yellow("retrying with git...")
	}

	gitCmd := func(args ...string) *exec.Cmd {
		cmd := exec.CommandContext(ctx, "git", args...)
		cmd.Stdin = os.Stdin
		if GitQuiet {
			cmd.Stdout = nil
			cmd.Stderr = nil
		} else {
			cmd.Stdout = os.Stdout
			cmd.Stderr = os.Stderr
		}
		cmd.Dir = tmpDir
		return cmd
	}

	cmd := gitCmd("init")
	err = cmd.Run()
	if err != nil {
		return "", err
	}

	cmd = gitCmd("remote", "add", "origin", p.Source.Remote())
	err = cmd.Run()
	if err != nil {
		return "", err
	}

	// Attempt shallow fetch at specific revision
	cmd = gitCmd("fetch", "--tags", "--depth", "1", "origin", version)
	err = cmd.Run()
	if err != nil {
		// Fall back to normal fetch (all revisions)
		cmd = gitCmd("fetch", "origin")
		err = cmd.Run()
		if err != nil {
			return "", err
		}
	}

	// Sparse checkout optimization: if a Subdir is specified,
	// there is no need to do a full checkout
	if p.Source.Subdir != "" {
		cmd = gitCmd("config", "core.sparsecheckout", "true")
		err = cmd.Run()
		if err != nil {
			return "", err
		}

		glob := []byte(p.Source.Subdir + "/*\n")
		err = ioutil.WriteFile(filepath.Join(tmpDir, ".git", "info", "sparse-checkout"), glob, 0644)
		if err != nil {
			return "", err
		}
	}

	cmd = gitCmd("-c", "advice.detachedHead=false", "checkout", version)
	err = cmd.Run()
	if err != nil {
		return "", err
	}

	b := bytes.NewBuffer(nil)
	cmd = exec.CommandContext(ctx, "git", "rev-parse", "HEAD")
	cmd.Stdout = b
	cmd.Dir = tmpDir
	err = cmd.Run()
	if err != nil {
		return "", err
	}

	commitHash := strings.TrimSpace(b.String())

	err = os.RemoveAll(path.Join(tmpDir, ".git"))
	if err != nil {
		return "", err
	}

	err = os.MkdirAll(path.Dir(destPath), os.ModePerm)
	if err != nil {
		return "", errors.Wrap(err, "failed to create parent path")
	}

	err = os.RemoveAll(destPath)
	if err != nil {
		return "", errors.Wrap(err, "failed to clean previous destination path")
	}

	err = os.Rename(path.Join(tmpDir, p.Source.Subdir), destPath)
	if err != nil {
		return "", errors.Wrap(err, "failed to move package")
	}

	return commitHash, nil
}
```

## File: `pkg/interface.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package pkg

import (
	"context"
)

type Interface interface {
	Install(ctx context.Context, name, dir, version string) (lockVersion string, err error)
}
```

## File: `pkg/local.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package pkg

import (
	"context"
	"os"
	"path/filepath"

	"github.com/fatih/color"
	"github.com/pkg/errors"

	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

type LocalPackage struct {
	Source *deps.Local
}

func NewLocalPackage(source *deps.Local) Interface {
	return &LocalPackage{
		Source: source,
	}
}

func (p *LocalPackage) Install(ctx context.Context, name, dir, version string) (lockVersion string, err error) {
	wd, err := os.Getwd()
	if err != nil {
		return "", errors.Wrap(err, "failed to get current working directory")
	}

	oldname := filepath.Join(wd, p.Source.Directory)
	newname := filepath.Join(dir, name)
	linkname, err := filepath.Rel(dir, oldname)

	if err != nil {
		linkname = oldname
	}

	err = os.RemoveAll(newname)
	if err != nil {
		return "", errors.Wrap(err, "failed to clean previous destination path")
	}

	_, err = os.Stat(oldname)
	if os.IsNotExist(err) {
		return "", errors.Wrap(err, "symlink destination path does not exist")
	}

	err = os.Symlink(linkname, newname)
	if err != nil {
		return "", errors.Wrap(err, "failed to create symlink for local dependency")
	}

	color.Magenta("LOCAL %s -> %s", name, oldname)

	return "", nil
}
```

## File: `pkg/local_test.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package pkg

import (
	"context"
	"io/ioutil"
	"os"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

func TestLocalInstall(t *testing.T) {
	cwd, err := os.Getwd()
	assert.NoError(t, err)

	vendorDir, err := ioutil.TempDir(cwd, "vendor")
	assert.NoError(t, err)
	defer os.RemoveAll(vendorDir)

	pkgDir, err := ioutil.TempDir(cwd, "foo")
	assert.NoError(t, err)
	defer os.RemoveAll(pkgDir)

	relPath, err := filepath.Rel(cwd, pkgDir)
	assert.NoError(t, err)

	p := NewLocalPackage(&deps.Local{Directory: relPath})
	lockVersion, err := p.Install(context.TODO(), "foo", vendorDir, "v1.0")
	assert.NoError(t, err)
	assert.Empty(t, lockVersion)
}

func TestLocalInstallSourceNotFound(t *testing.T) {
	cwd, err := os.Getwd()
	assert.NoError(t, err)

	vendorDir, err := ioutil.TempDir(cwd, "vendor")
	assert.NoError(t, err)
	defer os.RemoveAll(vendorDir)

	relPath := "foo"
	p := NewLocalPackage(&deps.Local{Directory: relPath})
	lockVersion, err := p.Install(context.TODO(), "foo", vendorDir, "v1.0")
	assert.Error(t, err)
	assert.Empty(t, lockVersion)
}

func TestLocalInstallTargetDoesNotExist(t *testing.T) {
	cwd, err := os.Getwd()
	assert.NoError(t, err)

	pkgDir, err := ioutil.TempDir(cwd, "foo")
	assert.NoError(t, err)
	defer os.RemoveAll(pkgDir)

	relPath, err := filepath.Rel(cwd, pkgDir)
	assert.NoError(t, err)

	p := NewLocalPackage(&deps.Local{Directory: relPath})
	lockVersion, err := p.Install(context.TODO(), "foo", "vendor", "v1.0")
	assert.Error(t, err)
	assert.Empty(t, lockVersion)
}

func TestLocalInstallSourceAndTargetDoNotExist(t *testing.T) {
	p := NewLocalPackage(&deps.Local{Directory: "foo"})
	lockVersion, err := p.Install(context.TODO(), "foo", "bar", "v1.0")
	assert.Error(t, err)
	assert.Empty(t, lockVersion)
}
```

## File: `pkg/packages.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package pkg

import (
	"context"
	"crypto/sha256"
	"encoding/base64"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"

	"github.com/fatih/color"
	"github.com/pkg/errors"

	"github.com/jsonnet-bundler/jsonnet-bundler/pkg/jsonnetfile"
	v1 "github.com/jsonnet-bundler/jsonnet-bundler/spec/v1"
	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

var (
	VersionMismatch = errors.New("multiple colliding versions specified")
)

// Ensure receives all direct packages, the directory to vendor into and all known locks.
// It then makes sure all direct and nested dependencies are present in vendor at the correct version:
//
// If the package is locked and the files in vendor match the sha256 checksum,
// nothing needs to be done. Otherwise, the package is retrieved from the
// upstream source and added into vendor. If previously locked, the sums are
// checked as well.
// In case a (nested) package is already present in the lock,
// the one from the lock takes precedence. This allows the user to set the
// desired version in case by `jb install`ing it.
//
// Finally, all unknown files and directories are removed from vendor/
// The full list of locked depedencies is returned
func Ensure(direct v1.JsonnetFile, vendorDir string, oldLocks *deps.Ordered) (*deps.Ordered, error) {
	// ensure all required files are in vendor
	// This is the actual installation
	locks, err := ensure(direct.Dependencies, vendorDir, "", oldLocks)
	if err != nil {
		return nil, err
	}

	// remove unchanged legacyNames
	CleanLegacyName(locks)

	// find unknown dirs in vendor/
	names := []string{}
	err = filepath.Walk(vendorDir, func(path string, i os.FileInfo, err error) error {
		if path == vendorDir {
			return nil
		}
		if !i.IsDir() {
			return nil
		}

		names = append(names, path)
		return nil
	})

	// remove them
	for _, dir := range names {
		name, err := filepath.Rel(vendorDir, dir)
		if err != nil {
			return nil, err
		}
		if !known(locks, name) {
			if err := os.RemoveAll(dir); err != nil {
				return nil, err
			}
			if !strings.HasPrefix(name, ".tmp") {
				color.Magenta("CLEAN %s", dir)
			}
		}
	}

	// remove all symlinks, optionally adding known ones back later if wished
	if err := cleanLegacySymlinks(vendorDir, locks); err != nil {
		return nil, err
	}
	if !direct.LegacyImports {
		return locks, nil
	}
	if err := linkLegacy(vendorDir, locks); err != nil {
		return nil, err
	}

	// return the final lockfile contents
	return locks, nil
}

func CleanLegacyName(list *deps.Ordered) {
	for _, k := range list.Keys() {
		d, _ := list.Get(k)
		// unset if not changed by user
		if d.LegacyNameCompat == d.Source.LegacyName() {
			dep, _ := list.Get(k)
			dep.LegacyNameCompat = ""
			list.Set(k, dep)
		}
	}
}

func cleanLegacySymlinks(vendorDir string, locks *deps.Ordered) error {
	// local packages need to be ignored
	locals := map[string]bool{}
	for _, k := range locks.Keys() {
		d, _ := locks.Get(k)
		if d.Source.LocalSource == nil {
			continue
		}

		locals[filepath.Join(vendorDir, d.Name())] = true
	}

	// remove all symlinks first
	return filepath.Walk(vendorDir, func(path string, i os.FileInfo, err error) error {
		if locals[path] {
			return nil
		}

		if i.Mode()&os.ModeSymlink != 0 {
			if err := os.Remove(path); err != nil {
				return err
			}
		}
		return nil
	})
}

func linkLegacy(vendorDir string, locks *deps.Ordered) error {
	// create only the ones we want
	for _, k := range locks.Keys() {
		d, _ := locks.Get(k)
		// localSource still uses the relative style
		if d.Source.LocalSource != nil {
			continue
		}

		legacyName := filepath.Join(vendorDir, d.LegacyName())
		pkgName := d.Name()

		taken, err := checkLegacyNameTaken(legacyName, pkgName)
		if err != nil {
			fmt.Println(err)
			continue
		}
		if taken {
			continue
		}

		// create the symlink
		if err := os.Symlink(
			filepath.Join(pkgName),
			filepath.Join(legacyName),
		); err != nil {
			return err
		}
	}
	return nil
}

func checkLegacyNameTaken(legacyName string, pkgName string) (bool, error) {
	fi, err := os.Lstat(legacyName)
	if err != nil {
		// does not exist: not taken
		if os.IsNotExist(err) {
			return false, nil
		}
		// a real error
		return false, err
	}

	// is it a symlink?
	if fi.Mode()&os.ModeSymlink != 0 {
		s, err := os.Readlink(legacyName)
		if err != nil {
			return false, err
		}
		color.Yellow("WARN: cannot link '%s' to '%s', because package '%s' already uses that name. The absolute import still works\n", pkgName, legacyName, s)
		return true, nil
	}

	// sth else
	color.Yellow("WARN: cannot link '%s' to '%s', because the file/directory already exists. The absolute import still works.\n", pkgName, legacyName)
	return true, nil
}

func known(deps *deps.Ordered, p string) bool {
	p = filepath.ToSlash(p)
	for _, kd := range deps.Keys() {
		d, _ := deps.Get(kd)
		k := filepath.ToSlash(d.Name())
		if strings.HasPrefix(p, k) || strings.HasPrefix(k, p) {
			return true
		}
	}
	return false
}

func ensure(direct *deps.Ordered, vendorDir, pathToParentModule string, locks *deps.Ordered) (*deps.Ordered, error) {
	deps := deps.NewOrdered()

	for _, k := range direct.Keys() {
		d, _ := direct.Get(k)
		l, present := locks.Get(d.Name())

		// already locked and the integrity is intact
		if present {
			d.Version = l.Version

			if check(l, vendorDir) {
				deps.Set(d.Name(), l)
				continue
			}
		}
		expectedSum := l.Sum

		// either not present or not intact: download again
		dir := filepath.Join(vendorDir, d.Name())
		os.RemoveAll(dir)

		locked, err := download(d, vendorDir, pathToParentModule)
		if err != nil {
			return nil, errors.Wrap(err, "downloading")
		}
		if expectedSum != "" && locked.Sum != expectedSum {
			return nil, fmt.Errorf("checksum mismatch for %s. Expected %s but got %s", d.Name(), expectedSum, locked.Sum)
		}
		deps.Set(d.Name(), *locked)
		// we settled on a new version, add it to the locks for recursion
		locks.Set(d.Name(), *locked)
	}

	for _, k := range deps.Keys() {
		d, _ := deps.Get(k)
		if d.Single {
			// skip dependencies that explicitely don't want nested ones installed
			continue
		}

		f, err := jsonnetfile.Load(filepath.Join(vendorDir, d.Name(), jsonnetfile.File))
		if err != nil {
			if os.IsNotExist(err) {
				continue
			}
			return nil, err
		}

		absolutePath, err := filepath.EvalSymlinks(filepath.Join(vendorDir, d.Name()))
		if err != nil {
			return nil, err
		}

		nested, err := ensure(f.Dependencies, vendorDir, absolutePath, locks)
		if err != nil {
			return nil, err
		}

		for _, k := range nested.Keys() {
			d, _ := nested.Get(k)
			if _, ok := deps.Get(d.Name()); !ok {
				deps.Set(d.Name(), d)
			}
		}
	}

	return deps, nil
}

// download retrieves a package from a remote upstream. The checksum of the
// files is generated afterwards.
func download(d deps.Dependency, vendorDir, pathToParentModule string) (*deps.Dependency, error) {
	var p Interface
	switch {
	case d.Source.GitSource != nil:
		p = NewGitPackage(d.Source.GitSource)
	case d.Source.LocalSource != nil:
		wd, err := os.Getwd()
		if err != nil {
			return nil, fmt.Errorf("failed to get current working directory: %w", err)
		}

		// Resolve the relative path to the parent module. When a local
		// dependency tree is resolved recursively, nested local dependencies
		// with relative paths must be evaluated relative to their referencing
		// jsonnetfile, rather than relative to the top-level jsonnetfile.
		modulePath, err := filepath.Rel(wd, filepath.Join(pathToParentModule, d.Source.LocalSource.Directory))
		if err != nil {
			modulePath = d.Source.LocalSource.Directory
		}

		p = NewLocalPackage(&deps.Local{Directory: modulePath})
	}

	if p == nil {
		return nil, errors.New("either git or local source is required")
	}

	version, err := p.Install(context.TODO(), d.Name(), vendorDir, d.Version)
	if err != nil {
		return nil, err
	}

	var sum string
	if d.Source.LocalSource == nil {
		sum = hashDir(filepath.Join(vendorDir, d.Name()))
	}

	d.Version = version
	d.Sum = sum
	return &d, nil
}

// check returns whether the files present at the vendor/ folder match the
// sha256 sum of the package. local-directory dependencies are not checked as
// their purpose is to change during development where integrity checking would
// be a hindrance.
func check(d deps.Dependency, vendorDir string) bool {
	// assume a local dependency is intact as long as it exists
	if d.Source.LocalSource != nil {
		x, err := jsonnetfile.Exists(filepath.Join(vendorDir, d.Name()))
		if err != nil {
			return false
		}
		return x
	}

	if d.Sum == "" {
		// no sum available, need to download
		return false
	}

	dir := filepath.Join(vendorDir, d.Name())
	sum := hashDir(dir)
	return d.Sum == sum
}

// hashDir computes the checksum of a directory by concatenating all files and
// hashing this data using sha256. This can be memory heavy with lots of data,
// but jsonnet files should be fairly small
func hashDir(dir string) string {
	hasher := sha256.New()

	filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if info.IsDir() {
			return nil
		}

		f, err := os.Open(path)
		if err != nil {
			return err
		}
		defer f.Close()

		if _, err := io.Copy(hasher, f); err != nil {
			return err
		}

		return nil
	})

	return base64.StdEncoding.EncodeToString(hasher.Sum(nil))
}
```

## File: `pkg/packages_test.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package pkg

import (
	"testing"

	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

func TestKnown(t *testing.T) {
	testDeps := deps.NewOrdered()
	testDeps.Set("ksonnet-lib", deps.Dependency{
		Source: deps.Source{
			GitSource: &deps.Git{
				Scheme: deps.GitSchemeHTTPS,
				Host:   "github.com",
				User:   "ksonnet",
				Repo:   "ksonnet-lib",
				Subdir: "/ksonnet.beta.4",
			},
		},
	})

	paths := []string{
		"github.com",
		"github.com/ksonnet",
		"github.com/ksonnet/ksonnet-lib",
		"github.com/ksonnet/ksonnet-lib/ksonnet.beta.4",
		"github.com/ksonnet/ksonnet-lib/ksonnet.beta.4/k.libsonnet",
		"github.com/ksonnet-util", // don't know that one
		"ksonnet.beta.4",          // the symlink
	}

	want := []string{
		"github.com",
		"github.com/ksonnet",
		"github.com/ksonnet/ksonnet",
		"github.com/ksonnet/ksonnet-lib",
		"github.com/ksonnet/ksonnet-lib/ksonnet.beta.4",
		"github.com/ksonnet/ksonnet-lib/ksonnet.beta.4/k.libsonnet",
	}

	w := make(map[string]bool)
	for _, k := range want {
		w[k] = true
	}

	for _, p := range paths {
		if known(testDeps, p) != w[p] {
			t.Fatalf("expected %s to be %v", p, w[p])
		}
	}
}

func TestCleanLegacyName(t *testing.T) {
	testList := func(name string) *deps.Ordered {
		l := deps.NewOrdered()
		l.Set("ksonnet-lib", deps.Dependency{
			LegacyNameCompat: name,
			Source: deps.Source{
				GitSource: &deps.Git{
					Scheme: deps.GitSchemeHTTPS,
					Host:   "github.com",
					User:   "ksonnet",
					Repo:   "ksonnet-lib",
					Subdir: "/ksonnet.beta.4",
				}},
		})
		return l
	}
	cases := map[string]bool{
		"ksonnet":        false,
		"ksonnet.beta.4": true,
	}

	for name, want := range cases {
		list := testList(name)
		CleanLegacyName(list)
		if (list.GetOrDefault("ksonnet-lib", deps.Dependency{}).LegacyNameCompat == "") != want {
			t.Fatalf("expected `%s` to be removed: %v", name, want)
		}
	}
}
```

## File: `pkg/jsonnetfile/jsonnetfile.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package jsonnetfile

import (
	"encoding/json"
	"io/ioutil"
	"os"

	"github.com/pkg/errors"

	v0 "github.com/jsonnet-bundler/jsonnet-bundler/spec/v0"
	v1 "github.com/jsonnet-bundler/jsonnet-bundler/spec/v1"
)

const (
	File     = "jsonnetfile.json"
	LockFile = "jsonnetfile.lock.json"
)

var (
	ErrUpdateJB = errors.New("jsonnetfile version unknown, update jb")
)

// Load reads a jsonnetfile.(lock).json from disk
func Load(filepath string) (v1.JsonnetFile, error) {
	bytes, err := ioutil.ReadFile(filepath)
	if err != nil {
		return v1.New(), err
	}

	return Unmarshal(bytes)
}

// Unmarshal creates a spec.JsonnetFile from bytes. Empty bytes
// will create an empty spec.
func Unmarshal(bytes []byte) (v1.JsonnetFile, error) {
	m := v1.New()

	if len(bytes) == 0 {
		return m, nil
	}

	versions := struct {
		Version uint `json:"version"`
	}{}

	err := json.Unmarshal(bytes, &versions)
	if err != nil {
		return m, err
	}

	switch versions.Version {
	case v0.Version:
		var mv0 v0.JsonnetFile
		if err := json.Unmarshal(bytes, &mv0); err != nil {
			return m, errors.Wrap(err, "failed to unmarshal jsonnetfile")
		}
		return v1.FromV0(mv0)
	case v1.Version:
		if err := json.Unmarshal(bytes, &m); err != nil {
			return m, errors.Wrap(err, "failed to unmarshal v1 file")
		}
		return m, nil
	default:
		return m, ErrUpdateJB
	}
}

// Exists returns whether the file at the given path exists
func Exists(path string) (bool, error) {
	_, err := os.Stat(path)
	if os.IsNotExist(err) {
		return false, nil
	}
	if err != nil {
		return false, err
	}

	return true, nil
}
```

## File: `pkg/jsonnetfile/jsonnetfile_test.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package jsonnetfile_test

import (
	"io/ioutil"
	"os"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/jsonnet-bundler/jsonnet-bundler/pkg/jsonnetfile"
	v1 "github.com/jsonnet-bundler/jsonnet-bundler/spec/v1"
	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

const notExist = "/this/does/not/exist"

const v0JSON = `{
  "dependencies": [
	{
	  "name": "grafana-builder",
	  "source": {
		"git": {
		  "remote": "https://github.com/grafana/jsonnet-libs",
		  "subdir": "grafana-builder"
		}
	  },
	  "version": "54865853ebc1f901964e25a2e7a0e4d2cb6b9648",
	  "sum": "ELsYwK+kGdzX1mee2Yy+/b2mdO4Y503BOCDkFzwmGbE="
	},
	{
	  "name": "prometheus-mixin",
	  "source": {
		"git": {
		  "remote": "https://github.com/prometheus/prometheus",
		  "subdir": "documentation/prometheus-mixin"
		}
	  },
	  "version": "7c039a6b3b4b2a9d7c613ac8bd3fc16e8ca79684",
	  "sum": "bVGOsq3hLOw2irNPAS91a5dZJqQlBUNWy3pVwM4+kIY="
	}
  ]
}`

var v0Jsonnetfile = func() v1.JsonnetFile {
	dep := v1.JsonnetFile{
		Dependencies:  deps.NewOrdered(),
		LegacyImports: true,
	}

	dep.Dependencies.Set("github.com/grafana/jsonnet-libs/grafana-builder", deps.Dependency{
		Source: deps.Source{
			GitSource: &deps.Git{
				Scheme: deps.GitSchemeHTTPS,
				Host:   "github.com",
				User:   "grafana",
				Repo:   "jsonnet-libs",
				Subdir: "/grafana-builder",
			},
		},
		Version:          "54865853ebc1f901964e25a2e7a0e4d2cb6b9648",
		Sum:              "ELsYwK+kGdzX1mee2Yy+/b2mdO4Y503BOCDkFzwmGbE=",
		LegacyNameCompat: "grafana-builder",
	})
	dep.Dependencies.Set("github.com/prometheus/prometheus/documentation/prometheus-mixin", deps.Dependency{
		Source: deps.Source{
			GitSource: &deps.Git{
				Scheme: deps.GitSchemeHTTPS,
				Host:   "github.com",
				User:   "prometheus",
				Repo:   "prometheus",
				Subdir: "/documentation/prometheus-mixin",
			},
		},
		Version:          "7c039a6b3b4b2a9d7c613ac8bd3fc16e8ca79684",
		Sum:              "bVGOsq3hLOw2irNPAS91a5dZJqQlBUNWy3pVwM4+kIY=",
		LegacyNameCompat: "prometheus-mixin",
	})

	return dep
}()

const v1JSON = `{
  "version": 1,
  "dependencies": [
	{
	  "source": {
		"git": {
		  "remote": "https://github.com/grafana/jsonnet-libs",
		  "subdir": "grafana-builder"
		}
	  },
	  "version": "54865853ebc1f901964e25a2e7a0e4d2cb6b9648",
	  "sum": "ELsYwK+kGdzX1mee2Yy+/b2mdO4Y503BOCDkFzwmGbE="
	},
	{
	  "name": "prometheus",
	  "source": {
		"git": {
		  "remote": "https://github.com/prometheus/prometheus",
		  "subdir": "documentation/prometheus-mixin"
		}
	  },
	  "version": "7c039a6b3b4b2a9d7c613ac8bd3fc16e8ca79684",
	  "sum": "bVGOsq3hLOw2irNPAS91a5dZJqQlBUNWy3pVwM4+kIY="
	}
  ],
  "legacyImports": false
}`

var v1Jsonnetfile = func() v1.JsonnetFile {
	dep := v1.JsonnetFile{
		Dependencies:  deps.NewOrdered(),
		LegacyImports: false,
	}

	dep.Dependencies.Set("github.com/grafana/jsonnet-libs/grafana-builder", deps.Dependency{
		Source: deps.Source{
			GitSource: &deps.Git{
				Scheme: deps.GitSchemeHTTPS,
				Host:   "github.com",
				User:   "grafana",
				Repo:   "jsonnet-libs",
				Subdir: "/grafana-builder",
			},
		},
		Version: "54865853ebc1f901964e25a2e7a0e4d2cb6b9648",
		Sum:     "ELsYwK+kGdzX1mee2Yy+/b2mdO4Y503BOCDkFzwmGbE=",
	})
	dep.Dependencies.Set("github.com/prometheus/prometheus/documentation/prometheus-mixin", deps.Dependency{
		LegacyNameCompat: "prometheus",
		Source: deps.Source{
			GitSource: &deps.Git{
				Scheme: deps.GitSchemeHTTPS,
				Host:   "github.com",
				User:   "prometheus",
				Repo:   "prometheus",
				Subdir: "/documentation/prometheus-mixin",
			},
		},
		Version: "7c039a6b3b4b2a9d7c613ac8bd3fc16e8ca79684",
		Sum:     "bVGOsq3hLOw2irNPAS91a5dZJqQlBUNWy3pVwM4+kIY=",
	})

	return dep
}()

func TestVersions(t *testing.T) {
	tests := []struct {
		Name        string
		JSON        string
		Jsonnetfile v1.JsonnetFile
		Error       error
	}{
		{
			Name:        "v0",
			JSON:        v0JSON,
			Jsonnetfile: v0Jsonnetfile,
		},
		{
			Name:        "v1",
			JSON:        v1JSON,
			Jsonnetfile: v1Jsonnetfile,
		},
		{
			Name:        "v100",
			JSON:        `{"version": 100}`,
			Jsonnetfile: v1.New(),
			Error:       jsonnetfile.ErrUpdateJB,
		},
	}

	for _, tc := range tests {
		t.Run(tc.Name, func(t *testing.T) {
			jf, err := jsonnetfile.Unmarshal([]byte(tc.JSON))
			assert.Equal(t, tc.Error, err)
			assert.Equal(t, tc.Jsonnetfile, jf)
		})
	}
}

func TestLoadV1(t *testing.T) {
	tempDir, err := ioutil.TempDir("", "jb-load-jsonnetfile")
	if err != nil {
		t.Fatal(err)
	}
	defer os.RemoveAll(tempDir)

	tempFile := filepath.Join(tempDir, jsonnetfile.File)
	err = ioutil.WriteFile(tempFile, []byte(v1JSON), os.ModePerm)
	assert.Nil(t, err)

	jf, err := jsonnetfile.Load(tempFile)
	assert.Nil(t, err)
	assert.Equal(t, v1Jsonnetfile, jf)
}

func TestLoadEmpty(t *testing.T) {
	tempDir, err := ioutil.TempDir("", "jb-load-empty")
	if err != nil {
		t.Fatal(err)
	}
	defer os.RemoveAll(tempDir)

	// write empty json file
	tempFile := filepath.Join(tempDir, jsonnetfile.File)
	err = ioutil.WriteFile(tempFile, []byte(`{}`), os.ModePerm)
	assert.Nil(t, err)

	// expect it to be loaded properly
	got, err := jsonnetfile.Load(tempFile)
	assert.Nil(t, err)
	assert.Equal(t, v1.New(), got)
}

func TestLoadNotExist(t *testing.T) {
	jf, err := jsonnetfile.Load(notExist)
	assert.Equal(t, v1.New(), jf)
	assert.Error(t, err)
}

func TestFileExists(t *testing.T) {
	{
		exists, err := jsonnetfile.Exists(notExist)
		assert.False(t, exists)
		assert.Nil(t, err)
	}
	{
		tempFile, err := ioutil.TempFile("", "jb-exists")
		if err != nil {
			t.Fatal(err)
		}

		defer func() {
			err := os.Remove(tempFile.Name())
			assert.Nil(t, err)
		}()

		exists, err := jsonnetfile.Exists(tempFile.Name())
		assert.True(t, exists)
		assert.Nil(t, err)
	}
}
```

## File: `scripts/check_license.sh`
```bash
#!/bin/sh

licRes=$(
for file in $(find . -type f -iname '*.go' ! -path '*/vendor/*'); do
	head -n3 "${file}" | grep -Eq "(Copyright|generated|GENERATED)" || echo -e "  ${file}"
done;)
if [ -n "${licRes}" ]; then
	echo -e "license header checking failed:\n${licRes}"
	exit 255
fi
```

## File: `scripts/generate-help-txt.sh`
```bash
#!/usr/bin/env bash

BINARY_NAME=jb

HELP_FILE=$PWD/_output/help.txt
echo "$ $BINARY_NAME -h" > $HELP_FILE
$PWD/_output/$BINARY_NAME 2>> $HELP_FILE
exit 0
```

## File: `spec/v0/spec.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package spec

import (
	"encoding/json"
	"sort"

	"github.com/elliotchance/orderedmap/v2"
)

const Version = 0

// JsonnetFile is the structure of a `.json` file describing a set of jsonnet
// dependencies. It is used for both, the jsonnetFile and the lockFile.
type JsonnetFile struct {
	Dependencies *orderedmap.OrderedMap[string, Dependency]
}

// New returns a new JsonnetFile with the dependencies map initialized
func New() JsonnetFile {
	return JsonnetFile{
		Dependencies: orderedmap.NewOrderedMap[string, Dependency](),
	}
}

// jsonFile is the json representation of a JsonnetFile, which is different for
// compatibility reasons.
type jsonFile struct {
	Dependencies []Dependency `json:"dependencies"`
}

// UnmarshalJSON unmarshals a `jsonFile`'s json into a JsonnetFile
func (jf *JsonnetFile) UnmarshalJSON(data []byte) error {
	var s jsonFile
	if err := json.Unmarshal(data, &s); err != nil {
		return err
	}

	jf.Dependencies = orderedmap.NewOrderedMap[string, Dependency]()
	for _, d := range s.Dependencies {
		jf.Dependencies.Set(d.Name, d)
	}
	return nil
}

// MarshalJSON serializes a JsonnetFile into json of the format of a `jsonFile`
func (jf JsonnetFile) MarshalJSON() ([]byte, error) {
	var s jsonFile
	for _, k := range jf.Dependencies.Keys() {
		d, _ := jf.Dependencies.Get(k)
		s.Dependencies = append(s.Dependencies, d)
	}

	sort.SliceStable(s.Dependencies, func(i int, j int) bool {
		return s.Dependencies[i].Name < s.Dependencies[j].Name
	})

	return json.Marshal(s)
}

type Dependency struct {
	Name      string `json:"name"`
	Source    Source `json:"source"`
	Version   string `json:"version"`
	Sum       string `json:"sum,omitempty"`
	DepSource string `json:"-"`
}

type Source struct {
	GitSource   *GitSource   `json:"git,omitempty"`
	LocalSource *LocalSource `json:"local,omitempty"`
}

type GitSource struct {
	Remote string `json:"remote"`
	Subdir string `json:"subdir"`
}

type LocalSource struct {
	Directory string `json:"directory"`
}
```

## File: `spec/v0/spec_test.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package spec

import (
	"encoding/json"
	"testing"

	"github.com/elliotchance/orderedmap/v2"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

const jsonJF = `{
  "dependencies": [
    {
      "name": "grafana-builder",
      "source": {
        "git": {
          "remote": "https://github.com/grafana/jsonnet-libs",
          "subdir": "grafana-builder"
        }
      },
      "version": "54865853ebc1f901964e25a2e7a0e4d2cb6b9648",
      "sum": "ELsYwK+kGdzX1mee2Yy+/b2mdO4Y503BOCDkFzwmGbE="
    },
    {
      "name": "prometheus-mixin",
      "source": {
        "git": {
          "remote": "https://github.com/prometheus/prometheus",
          "subdir": "documentation/prometheus-mixin"
        }
      },
      "version": "7c039a6b3b4b2a9d7c613ac8bd3fc16e8ca79684",
      "sum": "bVGOsq3hLOw2irNPAS91a5dZJqQlBUNWy3pVwM4+kIY="
    }
  ]
}`

func testData() JsonnetFile {
	f := JsonnetFile{Dependencies: orderedmap.NewOrderedMap[string, Dependency]()}

	f.Dependencies.Set("grafana-builder", Dependency{
		Name: "grafana-builder",
		Source: Source{
			GitSource: &GitSource{
				Remote: "https://github.com/grafana/jsonnet-libs",
				Subdir: "grafana-builder",
			},
		},
		Version: "54865853ebc1f901964e25a2e7a0e4d2cb6b9648",
		Sum:     "ELsYwK+kGdzX1mee2Yy+/b2mdO4Y503BOCDkFzwmGbE=",
	})
	f.Dependencies.Set("prometheus-mixin", Dependency{
		Name: "prometheus-mixin",
		Source: Source{
			GitSource: &GitSource{
				Remote: "https://github.com/prometheus/prometheus",
				Subdir: "documentation/prometheus-mixin",
			},
		},
		Version: "7c039a6b3b4b2a9d7c613ac8bd3fc16e8ca79684",
		Sum:     "bVGOsq3hLOw2irNPAS91a5dZJqQlBUNWy3pVwM4+kIY=",
	})

	return f
}

// TestUnmarshal checks that unmarshalling works
func TestUnmarshal(t *testing.T) {
	var dst JsonnetFile
	err := json.Unmarshal([]byte(jsonJF), &dst)
	require.NoError(t, err)
	assert.Equal(t, testData(), dst)
}

// TestMarshal checks that marshalling works
func TestMarshal(t *testing.T) {
	data, err := json.Marshal(testData())
	require.NoError(t, err)
	assert.JSONEq(t, jsonJF, string(data))
}

// TestRemarshal checks that unmarshalling a previously marshalled object yields
// the same object
func TestRemarshal(t *testing.T) {
	jf := testData()

	data, err := json.Marshal(jf)
	require.NoError(t, err)

	var dst JsonnetFile
	err = json.Unmarshal(data, &dst)
	require.NoError(t, err)

	assert.Equal(t, jf, dst)
}
```

## File: `spec/v1/spec.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package spec

import (
	"encoding/json"
	"sort"

	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

const Version uint = 1

// JsonnetFile is the structure of a `.json` file describing a set of jsonnet
// dependencies. It is used for both, the jsonnetFile and the lockFile.
type JsonnetFile struct {
	// List of dependencies
	Dependencies *deps.Ordered

	// Symlink files to old location
	LegacyImports bool
}

// New returns a new JsonnetFile with the dependencies map initialized
func New() JsonnetFile {
	return JsonnetFile{
		Dependencies:  deps.NewOrdered(),
		LegacyImports: true,
	}
}

// jsonFile is the json representation of a JsonnetFile, which is different for
// compatibility reasons.
type jsonFile struct {
	Version       uint              `json:"version"`
	Dependencies  []deps.Dependency `json:"dependencies"`
	LegacyImports bool              `json:"legacyImports"`
}

// UnmarshalJSON unmarshals a `jsonFile`'s json into a JsonnetFile
func (jf *JsonnetFile) UnmarshalJSON(data []byte) error {
	var s jsonFile
	s.LegacyImports = jf.LegacyImports // adpot default

	if err := json.Unmarshal(data, &s); err != nil {
		return err
	}

	jf.Dependencies = deps.NewOrdered()
	for _, d := range s.Dependencies {
		jf.Dependencies.Set(d.Name(), d)
	}

	jf.LegacyImports = s.LegacyImports

	return nil
}

// MarshalJSON serializes a JsonnetFile into json of the format of a `jsonFile`
func (jf JsonnetFile) MarshalJSON() ([]byte, error) {
	var s jsonFile

	s.Version = Version
	s.LegacyImports = jf.LegacyImports

	for _, k := range jf.Dependencies.Keys() {
		d, _ := jf.Dependencies.Get(k)
		s.Dependencies = append(s.Dependencies, d)
	}

	sort.SliceStable(s.Dependencies, func(i int, j int) bool {
		return s.Dependencies[i].Name() < s.Dependencies[j].Name()
	})

	if s.Dependencies == nil {
		s.Dependencies = make([]deps.Dependency, 0, 0)
	}

	return json.Marshal(s)
}
```

## File: `spec/v1/spec_test.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

package spec

import (
	"encoding/json"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

const jsonJF = `{
  "version": 1,
  "dependencies": [
    {
      "source": {
        "git": {
          "remote": "https://github.com/grafana/jsonnet-libs.git",
          "subdir": "grafana-builder"
        }
      },
      "version": "54865853ebc1f901964e25a2e7a0e4d2cb6b9648",
      "sum": "ELsYwK+kGdzX1mee2Yy+/b2mdO4Y503BOCDkFzwmGbE="
    },
    {
      "name": "prometheus",
      "source": {
        "git": {
          "remote": "https://github.com/prometheus/prometheus.git",
          "subdir": "documentation/prometheus-mixin"
        }
      },
      "version": "7c039a6b3b4b2a9d7c613ac8bd3fc16e8ca79684",
      "sum": "bVGOsq3hLOw2irNPAS91a5dZJqQlBUNWy3pVwM4+kIY="
    }
  ],
  "legacyImports": false
}`

func testData() JsonnetFile {
	td := JsonnetFile{
		LegacyImports: false,
		Dependencies:  deps.NewOrdered(),
	}
	td.Dependencies.Set("github.com/grafana/jsonnet-libs/grafana-builder", deps.Dependency{
		Source: deps.Source{
			GitSource: &deps.Git{
				Scheme: deps.GitSchemeHTTPS,
				Host:   "github.com",
				User:   "grafana",
				Repo:   "jsonnet-libs",
				Subdir: "/grafana-builder",
			},
		},
		Version: "54865853ebc1f901964e25a2e7a0e4d2cb6b9648",
		Sum:     "ELsYwK+kGdzX1mee2Yy+/b2mdO4Y503BOCDkFzwmGbE=",
	})
	td.Dependencies.Set("github.com/prometheus/prometheus/documentation/prometheus-mixin", deps.Dependency{
		LegacyNameCompat: "prometheus",
		Source: deps.Source{
			GitSource: &deps.Git{
				Scheme: deps.GitSchemeHTTPS,
				Host:   "github.com",
				User:   "prometheus",
				Repo:   "prometheus",
				Subdir: "/documentation/prometheus-mixin",
			},
		},
		Version: "7c039a6b3b4b2a9d7c613ac8bd3fc16e8ca79684",
		Sum:     "bVGOsq3hLOw2irNPAS91a5dZJqQlBUNWy3pVwM4+kIY=",
	})
	return td
}

// TestUnmarshal checks that unmarshalling works
func TestUnmarshal(t *testing.T) {
	var dst JsonnetFile
	err := json.Unmarshal([]byte(jsonJF), &dst)
	require.NoError(t, err)
	assert.Equal(t, testData(), dst)
}

// TestMarshal checks that marshalling works
func TestMarshal(t *testing.T) {
	data, err := json.Marshal(testData())
	require.NoError(t, err)
	assert.JSONEq(t, jsonJF, string(data))
}

// TestRemarshal checks that unmarshalling a previously marshalled object yields
// the same object
func TestRemarshal(t *testing.T) {
	jf := testData()

	data, err := json.Marshal(jf)
	require.NoError(t, err)

	var dst JsonnetFile
	err = json.Unmarshal(data, &dst)
	require.NoError(t, err)

	assert.Equal(t, jf, dst)
}
```

## File: `spec/v1/v0.go`
```go
// Copyright 2018 jsonnet-bundler authors
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
package spec

import (
	"path/filepath"

	v0 "github.com/jsonnet-bundler/jsonnet-bundler/spec/v0"
	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

func FromV0(mv0 v0.JsonnetFile) (JsonnetFile, error) {
	m := New()
	m.LegacyImports = true

	for _, name := range mv0.Dependencies.Keys() {
		old, _ := mv0.Dependencies.Get(name)
		var d deps.Dependency

		switch {
		case old.Source.GitSource != nil:
			d = *deps.Parse("", old.Source.GitSource.Remote)

			if old.Source.GitSource.Subdir != "" {
				subdir := filepath.Clean("/" + old.Source.GitSource.Subdir)
				d.Source.GitSource.Subdir = subdir
			}

		case old.Source.LocalSource != nil:
			d = *deps.Parse("", old.Source.LocalSource.Directory)
		}

		d.Sum = old.Sum
		d.Version = old.Version
		d.LegacyNameCompat = name

		m.Dependencies.Set(d.Name(), d)
	}

	return m, nil
}
```

## File: `spec/v1/deps/dependencies.go`
```go
// Copyright 2018 jsonnet-bundler authors
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
package deps

import (
	"os"
	"path/filepath"

	"github.com/elliotchance/orderedmap/v2"
)

type Dependency struct {
	Source  Source `json:"source"`
	Version string `json:"version"`
	Sum     string `json:"sum,omitempty"`
	Single  bool   `json:"single,omitempty"`

	// older schema used to have `name`. We still need that data for
	// `LegacyName`
	LegacyNameCompat string `json:"name,omitempty"`
}

func Parse(dir, uri string) *Dependency {
	if uri == "" {
		return nil
	}

	if d := parseGit(uri); d != nil {
		return d
	}

	return parseLocal(dir, uri)
}

func (d Dependency) Name() string {
	return d.Source.Name()
}

func (d Dependency) LegacyName() string {
	if d.LegacyNameCompat != "" {
		return d.LegacyNameCompat
	}
	return d.Source.LegacyName()
}

type Ordered = orderedmap.OrderedMap[string, Dependency]

func NewOrdered() *Ordered {
	return orderedmap.NewOrderedMap[string, Dependency]()
}

type Source struct {
	GitSource   *Git   `json:"git,omitempty"`
	LocalSource *Local `json:"local,omitempty"`
}

func (s Source) Name() string {
	switch {
	case s.GitSource != nil:
		return s.GitSource.Name()
	case s.LocalSource != nil:
		return s.LegacyName()
	default:
		return ""
	}
}

func (s Source) LegacyName() string {
	switch {
	case s.GitSource != nil:
		return s.GitSource.LegacyName()
	case s.LocalSource != nil:
		p, err := filepath.Abs(s.LocalSource.Directory)
		if err != nil {
			panic("unable to create absolute path from local source directory: " + err.Error())
		}
		return filepath.Base(p)
	default:
		return ""
	}
}

type Local struct {
	Directory string `json:"directory"`
}

func parseLocal(dir, p string) *Dependency {
	clean := filepath.Clean(p)
	abs := filepath.Join(dir, clean)

	info, err := os.Stat(abs)
	if err != nil {
		return nil
	}

	if !info.IsDir() {
		return nil
	}

	return &Dependency{
		Source: Source{
			LocalSource: &Local{
				Directory: clean,
			},
		},
		Version: "",
	}
}
```

## File: `spec/v1/deps/dependencies_test.go`
```go
// Copyright 2018 jsonnet-bundler authors
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
package deps

import (
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestParseDependency(t *testing.T) {
	const testFolder = "test/jsonnet/foobar"
	err := os.MkdirAll(testFolder, os.ModePerm)
	if err != nil {
		t.Fatal(err)
	}
	defer os.RemoveAll("test")

	tests := []struct {
		name string
		path string
		want *Dependency
	}{
		{
			name: "Empty",
			path: "",
			want: nil,
		},
		{
			name: "Invalid",
			path: "example.com/foo",
			want: nil,
		},
		{
			name: "InvalidDomain",
			path: "example.c/foo/bar",
			want: nil,
		},
		{
			name: "InvalidDomain2",
			path: "examplec/foo/bar",
			want: nil,
		},
		{
			name: "local",
			path: testFolder,
			want: &Dependency{
				Source: Source{
					LocalSource: &Local{
						Directory: "test/jsonnet/foobar",
					},
				},
				Version: "",
			},
		},
	}
	for _, tt := range tests {
		_ = t.Run(tt.name, func(t *testing.T) {
			dependency := Parse("", tt.path)

			if tt.path == "" {
				assert.Nil(t, dependency)
			} else {
				assert.Equal(t, tt.want, dependency)
			}
		})
	}
}
```

## File: `spec/v1/deps/git.go`
```go
// Copyright 2018 jsonnet-bundler authors
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
package deps

import (
	"encoding/json"
	"fmt"
	"path/filepath"
	"regexp"
	"strings"
)

const (
	GitSchemeSSH   = "ssh://git@"
	GitSchemeHTTPS = "https://"
)

// Git holds all required information for cloning a package from git
type Git struct {
	// Scheme (Protocol) used (https, git+ssh)
	Scheme string

	// Hostname the repo is located at
	Host string
	// User (example.com/<user>)
	User string
	// Repo (example.com/<user>/<repo>)
	Repo string
	// Subdir (example.com/<user>/<repo>/<subdir>)
	Subdir string
}

// json representation of Git (for compatiblity with old format)
type jsonGit struct {
	Remote string `json:"remote"`
	Subdir string `json:"subdir"`
}

// MarshalJSON takes care of translating between Git and jsonGit
func (gs *Git) MarshalJSON() ([]byte, error) {
	j := jsonGit{
		Remote: gs.Remote(),
		Subdir: strings.TrimPrefix(gs.Subdir, "/"),
	}
	return json.Marshal(j)
}

// UnmarshalJSON takes care of translating between Git and jsonGit
func (gs *Git) UnmarshalJSON(data []byte) error {
	var j jsonGit
	if err := json.Unmarshal(data, &j); err != nil {
		return err
	}

	if j.Subdir != "" {
		gs.Subdir = "/" + strings.TrimPrefix(j.Subdir, "/")
	}

	tmp := parseGit(j.Remote)
	if tmp == nil {
		return fmt.Errorf("unable to parse git url `%s` ", j.Remote)
	}
	gs.Host = tmp.Source.GitSource.Host
	gs.User = tmp.Source.GitSource.User
	gs.Repo = tmp.Source.GitSource.Repo
	gs.Scheme = tmp.Source.GitSource.Scheme
	return nil
}

// Name returns the repository in a go-like format (example.com/user/repo/subdir)
func (gs *Git) Name() string {
	return fmt.Sprintf("%s/%s/%s%s", gs.Host, gs.User, strings.TrimSuffix(gs.Repo, ".git"), gs.Subdir)
}

// LegacyName returns the last element of the packages path
// example: github.com/ksonnet/ksonnet-lib/ksonnet.beta.4 becomes ksonnet.beta.4
func (gs *Git) LegacyName() string {
	return filepath.Base(strings.TrimSuffix(gs.Repo, ".git") + gs.Subdir)
}

var gitProtoFmts = map[string]string{
	GitSchemeSSH:   GitSchemeSSH + "%s/%s/%s.git",
	GitSchemeHTTPS: GitSchemeHTTPS + "%s/%s/%s.git",
}

// Remote returns a remote string that can be passed to git
func (gs *Git) Remote() string {
	return fmt.Sprintf(gitProtoFmts[gs.Scheme],
		gs.Host, gs.User, gs.Repo,
	)
}

// regular expressions for matching package uris
const (
	gitSSHExp = `ssh://git@(?P<host>.+)/(?P<user>.+)/(?P<repo>.+).git`
	gitSCPExp = `^git@(?P<host>.+):(?P<user>.+)/(?P<repo>.+).git`
	// The long ugly pattern for ${host} here is a generic pattern for "valid URL with zero or more subdomains and a valid TLD"
	gitHTTPSSubgroup = `(?P<host>[a-zA-Z0-9][a-zA-Z0-9-\.]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,})/(?P<user>[-_~a-zA-Z0-9/\.]+)/(?P<repo>[-_a-zA-Z0-9\.]+)\.git`
	gitHTTPSExp      = `(?P<host>[a-zA-Z0-9][a-zA-Z0-9-\.]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,})/(?P<user>[-_~a-zA-Z0-9\.]+)/(?P<repo>[-_a-zA-Z0-9\.]+)`
)

var (
	VersionRegex        = `@(?P<version>.*)`
	PathRegex           = `/(?P<subdir>.*)`
	PathAndVersionRegex = `/(?P<subdir>.*)@(?P<version>.*)`
)

func parseGit(uri string) *Dependency {
	var d = Dependency{
		Version: "master",
		Source:  Source{},
	}
	var gs *Git
	var version string

	switch {
	case reMatch(gitSSHExp, uri):
		gs, version = match(uri, gitSSHExp)
		gs.Scheme = GitSchemeSSH
	case reMatch(gitSCPExp, uri):
		gs, version = match(uri, gitSCPExp)
		gs.Scheme = GitSchemeSSH
	case reMatch(gitHTTPSSubgroup, uri):
		gs, version = match(uri, gitHTTPSSubgroup)
		gs.Scheme = GitSchemeHTTPS
	case reMatch(gitHTTPSExp, uri):
		gs, version = match(uri, gitHTTPSExp)
		gs.Scheme = GitSchemeHTTPS
	default:
		return nil
	}

	if gs.Subdir != "" {
		gs.Subdir = "/" + gs.Subdir
	}

	d.Source.GitSource = gs
	if version != "" {
		d.Version = version
	}
	return &d
}

func match(p string, exp string) (gs *Git, version string) {
	gs = &Git{}
	exps := []*regexp.Regexp{
		regexp.MustCompile(exp + PathAndVersionRegex),
		regexp.MustCompile(exp + PathRegex),
		regexp.MustCompile(exp + VersionRegex),
		regexp.MustCompile(exp),
	}

	for _, e := range exps {
		if !e.MatchString(p) {
			continue
		}

		matches := reSubMatchMap(e, p)
		gs.Host = matches["host"]
		gs.User = matches["user"]
		gs.Repo = matches["repo"]

		if sd, ok := matches["subdir"]; ok {
			gs.Subdir = sd
		}

		return gs, matches["version"]
	}
	return gs, ""
}

func reMatch(exp string, str string) bool {
	return regexp.MustCompile(exp).MatchString(str)
}

func reSubMatchMap(r *regexp.Regexp, str string) map[string]string {
	match := r.FindStringSubmatch(str)
	subMatchMap := make(map[string]string)
	for i, name := range r.SubexpNames() {
		if i != 0 {
			subMatchMap[name] = match[i]
		}
	}

	return subMatchMap
}
```

## File: `spec/v1/deps/git_test.go`
```go
// Copyright 2018 jsonnet-bundler authors
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
package deps

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestParseGit(t *testing.T) {
	sshWant := func(host string) *Dependency {
		return &Dependency{
			Version: "v1",
			Source: Source{GitSource: &Git{
				Scheme: GitSchemeSSH,
				Host:   host,
				User:   "user",
				Repo:   "repo",
				Subdir: "/foobar",
			}},
		}
	}

	tests := []struct {
		name       string
		uri        string
		want       *Dependency
		wantRemote string
	}{
		{
			name: "github-slug",
			uri:  "github.com/ksonnet/ksonnet-lib/ksonnet.beta.3",
			want: &Dependency{
				Version: "master",
				Source: Source{GitSource: &Git{
					Scheme: GitSchemeHTTPS,
					Host:   "github.com",
					User:   "ksonnet",
					Repo:   "ksonnet-lib",
					Subdir: "/ksonnet.beta.3",
				}},
			},
			wantRemote: "https://github.com/ksonnet/ksonnet-lib.git",
		},
		{
			name:       "ssh.ssh",
			uri:        "ssh://git@example.com/user/repo.git/foobar@v1",
			want:       sshWant("example.com"),
			wantRemote: "ssh://git@example.com/user/repo.git",
		},
		{
			name:       "ssh.scp",
			uri:        "git@my.host:user/repo.git/foobar@v1",
			want:       sshWant("my.host"),
			wantRemote: "ssh://git@my.host/user/repo.git", // want ssh format here
		},
		{
			name: "ValidGitHTTPS",
			uri:  "https://example.com/foo/bar",
			want: &Dependency{
				Version: "master",
				Source: Source{
					GitSource: &Git{
						Scheme: GitSchemeHTTPS,
						Host:   "example.com",
						User:   "foo",
						Repo:   "bar",
						Subdir: "",
					},
				},
			},
			wantRemote: "https://example.com/foo/bar.git",
		},
		{
			name: "ValidGitLabUserGroupHTTPS",
			uri:  "https://gitlab.example.com/first.last/project",
			want: &Dependency{
				Version: "master",
				Source: Source{
					GitSource: &Git{
						Scheme: GitSchemeHTTPS,
						Host:   "gitlab.example.com",
						User:   "first.last",
						Repo:   "project",
						Subdir: "",
					},
				},
			},
			wantRemote: "https://gitlab.example.com/first.last/project.git",
		},
		{
			name: "ValidGitNoScheme",
			uri:  "example.com/foo/bar",
			want: &Dependency{
				Version: "master",
				Source: Source{
					GitSource: &Git{
						Scheme: GitSchemeHTTPS,
						Host:   "example.com",
						User:   "foo",
						Repo:   "bar",
						Subdir: "",
					},
				},
			},
			wantRemote: "https://example.com/foo/bar.git",
		},
		{
			name: "ValidGitPath",
			uri:  "example.com/foo/bar/baz/bat",
			want: &Dependency{
				Version: "master",
				Source: Source{
					GitSource: &Git{
						Scheme: GitSchemeHTTPS,
						Host:   "example.com",
						User:   "foo",
						Repo:   "bar",
						Subdir: "/baz/bat",
					},
				},
			},
			wantRemote: "https://example.com/foo/bar.git",
		},
		{
			name: "ValidGitVersion",
			uri:  "example.com/foo/bar@baz",
			want: &Dependency{
				Version: "baz",
				Source: Source{
					GitSource: &Git{
						Scheme: GitSchemeHTTPS,
						Host:   "example.com",
						User:   "foo",
						Repo:   "bar",
						Subdir: "",
					},
				},
			},
			wantRemote: "https://example.com/foo/bar.git",
		},
		{
			name: "ValidGitPathVersion",
			uri:  "example.com/foo/bar/baz@bat",
			want: &Dependency{
				Version: "bat",
				Source: Source{
					GitSource: &Git{
						Scheme: GitSchemeHTTPS,
						Host:   "example.com",
						User:   "foo",
						Repo:   "bar",
						Subdir: "/baz",
					},
				},
			},
			wantRemote: "https://example.com/foo/bar.git",
		},
		{
			name: "ValidGitSubdomain",
			uri:  "git.example.com/foo/bar",
			want: &Dependency{
				Version: "master",
				Source: Source{
					GitSource: &Git{
						Scheme: GitSchemeHTTPS,
						Host:   "git.example.com",
						User:   "foo",
						Repo:   "bar",
						Subdir: "",
					},
				},
			},
			wantRemote: "https://git.example.com/foo/bar.git",
		},
		{
			name: "ValidGitSubgroups",
			uri:  "example.com/group/subgroup/repository.git",
			want: &Dependency{
				Version: "master",
				Source: Source{
					GitSource: &Git{
						Scheme: GitSchemeHTTPS,
						Host:   "example.com",
						User:   "group/subgroup",
						Repo:   "repository",
						Subdir: "",
					},
				},
			},
			wantRemote: "https://example.com/group/subgroup/repository.git",
		},
		{
			name: "ValidGitSubgroupSubDir",
			uri:  "example.com/group/subgroup/repository.git/subdir",
			want: &Dependency{
				Version: "master",
				Source: Source{
					GitSource: &Git{
						Scheme: GitSchemeHTTPS,
						Host:   "example.com",
						User:   "group/subgroup",
						Repo:   "repository",
						Subdir: "/subdir",
					},
				},
			},
			wantRemote: "https://example.com/group/subgroup/repository.git",
		},
		{
			name: "ValidBitbucketPersonalRepository",
			uri:  "bitbucket.org/~user/repository.git",
			want: &Dependency{
				Version: "master",
				Source: Source{
					GitSource: &Git{
						Scheme: GitSchemeHTTPS,
						Host:   "bitbucket.org",
						User:   "~user",
						Repo:   "repository",
						Subdir: "",
					},
				},
			},
			wantRemote: "https://bitbucket.org/~user/repository.git",
		},
	}

	for _, c := range tests {
		t.Run(c.name, func(t *testing.T) {
			got := Parse("", c.uri)
			require.NotNilf(t, got, "parsed dependency is nil. Most likely, no regex matched the format.")

			assert.Equal(t, c.want, got)

			require.NotNil(t, got.Source)
			require.NotNil(t, got.Source.GitSource)
			assert.Equal(t, c.wantRemote, got.Source.GitSource.Remote())
		})
	}
}
```

## File: `tool/rewrite/rewrite.go`
```go
// Copyright 2018 jsonnet-bundler authors
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

// Package rewrite provides a tool that automatically rewrites legacy imports to
// absolute ones
package rewrite

import (
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"regexp"
	"strings"

	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

var expr = regexp.MustCompile(`(?mU)(import ["'])(.*)(\/.*["'])`)

// Rewrite changes all imports in `dir` from legacy to absolute style
// All files in `vendorDir` are ignored
func Rewrite(dir, vendorDir string, packages *deps.Ordered) error {
	imports := make(map[string]string)
	for _, k := range packages.Keys() {
		p, _ := packages.Get(k)
		if p.LegacyName() == p.Name() {
			continue
		}

		imports[p.LegacyName()] = p.Name()
	}

	vendorFi, err := os.Stat(filepath.Join(dir, vendorDir))
	if err != nil {
		return err
	}

	// list all Jsonnet files
	files := []string{}
	if err := filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if os.SameFile(vendorFi, info) {
			return filepath.SkipDir
		}

		if ext := filepath.Ext(path); ext == ".jsonnet" || ext == ".libsonnet" {
			files = append(files, path)
		}
		return nil
	}); err != nil {
		return err
	}

	// change the imports
	for _, s := range files {
		if err := replaceFile(s, imports); err != nil {
			return err
		}
	}

	return nil
}

func wrap(s, q string) string {
	return fmt.Sprintf(`import %s%s`, q, s)
}

func replaceFile(name string, imports map[string]string) error {
	raw, err := ioutil.ReadFile(name)
	if err != nil {
		return err
	}

	out := replace(string(raw), imports)
	return ioutil.WriteFile(name, out, 0644)
}

func replace(data string, imports map[string]string) []byte {
	contents := strings.Split(string(data), "\n")

	// try to fix imports line by line
	buf := make([]string, 0, len(contents))
	for _, line := range contents {
		match := expr.FindStringSubmatch(line)
		// no import in this line: push unmodified
		if len(match) == 0 {
			buf = append(buf, line)
			continue
		}

		// the legacyName
		matchedName := match[2]

		replaced := false
		for legacy, absolute := range imports {
			// not this import
			if matchedName != legacy {
				continue
			}

			// fix the import
			replaced = true
			buf = append(buf, expr.ReplaceAllString(line, "${1}"+absolute+"${3}"))
		}

		// no matching known import found? push unmodified
		if !replaced {
			buf = append(buf, line)
		}
	}

	return []byte(strings.Join(buf, "\n"))
}
```

## File: `tool/rewrite/rewrite_test.go`
```go
// Copyright 2018 jsonnet-bundler authors
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
package rewrite

import (
	"io/ioutil"
	"os"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/jsonnet-bundler/jsonnet-bundler/spec/v1/deps"
)

const sample = `
(import "k.libsonnet") + // not vendored
(import "ksonnet/abc.jsonnet") + // prefix of next
(import "ksonnet.beta.4/k.libsonnet") + // normal import
(import "github.com/ksonnet/ksonnet/def.jsonnet") + // already absolute
(import "prometheus/mixin/whatever/abc.libsonnet") + // nested
(import "mylib/foo.libsonnet") + // not managed by jb
// completely unrelated line:
[ "nice" ]
`

const want = `
(import "k.libsonnet") + // not vendored
(import "github.com/ksonnet/ksonnet/abc.jsonnet") + // prefix of next
(import "github.com/ksonnet/ksonnet-lib/ksonnet.beta.4/k.libsonnet") + // normal import
(import "github.com/ksonnet/ksonnet/def.jsonnet") + // already absolute
(import "github.com/prometheus/prometheus/mixin/whatever/abc.libsonnet") + // nested
(import "mylib/foo.libsonnet") + // not managed by jb
// completely unrelated line:
[ "nice" ]
`

func TestRewrite(t *testing.T) {
	testRewriteWithJsonnetHome(t, "vendor")
}

func TestRewriteCustomJsonnetHome(t *testing.T) {
	testRewriteWithJsonnetHome(t, "custom-vendor-dir")
}

func TestRewriteDeepCustomJsonnetHome(t *testing.T) {
	testRewriteWithJsonnetHome(t, "custom/vendor/dir")
}

func testRewriteWithJsonnetHome(t *testing.T, jsonnetHome string) {
	dir, err := ioutil.TempDir("", "jbrewrite")
	require.Nil(t, err)
	defer os.RemoveAll(dir)

	name := filepath.Join(dir, "test.jsonnet")
	err = ioutil.WriteFile(name, []byte(sample), 0644)
	require.Nil(t, err)

	vendorDir := filepath.Join(dir, jsonnetHome)
	err = os.MkdirAll(vendorDir, os.ModePerm)
	require.Nil(t, err)

	err = Rewrite(dir, jsonnetHome, locks())
	require.Nil(t, err)

	content, err := ioutil.ReadFile(name)
	require.Nil(t, err)

	assert.Equal(t, want, string(content))
}

func locks() *deps.Ordered {
	ls := deps.NewOrdered()
	ls.Set("ksonnet", *deps.Parse("", "github.com/ksonnet/ksonnet"))
	ls.Set("ksonnet.beta.4", *deps.Parse("", "github.com/ksonnet/ksonnet-lib/ksonnet.beta.4"))
	ls.Set("prometheus", *deps.Parse("", "github.com/prometheus/prometheus"))

	return ls
}
```

