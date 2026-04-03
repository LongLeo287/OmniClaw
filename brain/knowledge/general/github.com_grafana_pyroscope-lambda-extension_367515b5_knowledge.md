---
id: github.com-grafana-pyroscope-lambda-extension-3675
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:04.465838
---

# KNOWLEDGE EXTRACT: github.com_grafana_pyroscope-lambda-extension_367515b5
> **Extracted on:** 2026-04-01 07:26:27
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007518767/github.com_grafana_pyroscope-lambda-extension_367515b5

---

## File: `.gitignore`
```
*.exe
*.exe~
*.dll
*.so
*.dylib

# Test binary, built with `go test -c`
*.test

# Output of the go coverage tool, specifically when used with LiteIDE
*.out

bin

.aws-sam
out.txt

examples/go
!examples/go/main.go

node_modules

.idea/
```

## File: `.tool-versions`
```
golang 1.22.9
shellcheck 0.8.0
jq 1.6
deno 1.23.2
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## [1.7.1](https://github.com/grafana/pyroscope-lambda-extension/compare/v1.7.0...v1.7.1) (2025-01-30)


### Bug Fixes

* deprecate release-please manual workflow ([#37](https://github.com/grafana/pyroscope-lambda-extension/issues/37)) ([e5c72d6](https://github.com/grafana/pyroscope-lambda-extension/commit/e5c72d61c1a6259f0cb36e27db3df01db5116f6f))

## [1.7.0](https://github.com/grafana/pyroscope-lambda-extension/compare/v1.6.1...v1.7.0) (2023-12-08)


### Features

* inject session ID in the client ([#32](https://github.com/grafana/pyroscope-lambda-extension/issues/32)) ([56ca696](https://github.com/grafana/pyroscope-lambda-extension/commit/56ca69668b90ee2fb2c6a1c81ecd88298776426c))

## [1.6.1](https://github.com/grafana/pyroscope-lambda-extension/compare/v1.6.0...v1.6.1) (2023-10-25)


### Bug Fixes

* relaying error handling ([#30](https://github.com/grafana/pyroscope-lambda-extension/issues/30)) ([815cae0](https://github.com/grafana/pyroscope-lambda-extension/commit/815cae0407880d3d3143584f73e31c58aaba3d98))

## [1.6.0](https://github.com/grafana/pyroscope-lambda-extension/compare/v1.5.0...v1.6.0) (2023-10-06)


### Features

* update pyroscope-go ([976cc87](https://github.com/grafana/pyroscope-lambda-extension/commit/976cc87e984ee173203ab3b8e7f89d8e8fccc206))

## [1.5.0](https://github.com/grafana/pyroscope-lambda-extension/compare/v1.4.1...v1.5.0) (2023-08-11)


### Features

* add optional json logging format for advanced configurations ([#25](https://github.com/grafana/pyroscope-lambda-extension/issues/25)) ([2389785](https://github.com/grafana/pyroscope-lambda-extension/commit/238978539791f2c61f6c9ac86cad372614a6bc0f))


### Bug Fixes

* change log level to debug when exiting ([#26](https://github.com/grafana/pyroscope-lambda-extension/issues/26)) ([c3bf02f](https://github.com/grafana/pyroscope-lambda-extension/commit/c3bf02f062f2eabe309f6e8e8aa01eb2192fd566))

## [1.4.1](https://github.com/grafana/pyroscope-lambda-extension/compare/v1.4.0...v1.4.1) (2023-07-13)


### Bug Fixes

* rename org_id to tenant_id ([#23](https://github.com/grafana/pyroscope-lambda-extension/issues/23)) ([f21acfc](https://github.com/grafana/pyroscope-lambda-extension/commit/f21acfccdcb1dfac1b9234473b1fc47e87a72f79))

## [1.4.0](https://github.com/pyroscope-io/pyroscope-lambda-extension/compare/v1.3.0...v1.4.0) (2023-04-23)


### Features

* relay to phlare ([#21](https://github.com/pyroscope-io/pyroscope-lambda-extension/issues/21)) ([bb9ac34](https://github.com/pyroscope-io/pyroscope-lambda-extension/commit/bb9ac34129d5da5eb0913a4e594dd08de4995087))

## [1.3.0](https://github.com/pyroscope-io/pyroscope-lambda-extension/compare/v1.2.0...v1.3.0) (2022-10-12)


### Features

* flush queue before next event polling ([#18](https://github.com/pyroscope-io/pyroscope-lambda-extension/issues/18)) ([e5b06d2](https://github.com/pyroscope-io/pyroscope-lambda-extension/commit/e5b06d2e38d174daa52828e45fb7783700bd86ee))


### Bug Fixes

* configure MaxIdleConnsPerHost (was 2 by default) ([#19](https://github.com/pyroscope-io/pyroscope-lambda-extension/issues/19)) ([9214f26](https://github.com/pyroscope-io/pyroscope-lambda-extension/commit/9214f26e2e1b4ae460981ab1f09f01c6ac92f201))

## [1.2.0](https://github.com/pyroscope-io/pyroscope-lambda-extension/compare/v1.1.0...v1.2.0) (2022-10-04)


### Features

* allow NUM_WORKERS to be configurable ([#12](https://github.com/pyroscope-io/pyroscope-lambda-extension/issues/12)) ([efbe468](https://github.com/pyroscope-io/pyroscope-lambda-extension/commit/efbe4680175be80f4db2d0ce0e3b301443d8201e))
* allow timeout to be configurable ([#16](https://github.com/pyroscope-io/pyroscope-lambda-extension/issues/16)) ([8f80d90](https://github.com/pyroscope-io/pyroscope-lambda-extension/commit/8f80d9071e352362df82dbecabb8b086494beaac))

## [1.1.0](https://github.com/pyroscope-io/pyroscope-lambda-extension/compare/v1.0.1...v1.1.0) (2022-07-05)


### Features

* initial version ([#1](https://github.com/pyroscope-io/pyroscope-lambda-extension/issues/1)) ([31471b4](https://github.com/pyroscope-io/pyroscope-lambda-extension/commit/31471b4fd059f511720baf6dba2e04a7236083ca))


### Bug Fixes

* remove ap-northeast{2,3} arm builds ([#8](https://github.com/pyroscope-io/pyroscope-lambda-extension/issues/8)) ([88501e9](https://github.com/pyroscope-io/pyroscope-lambda-extension/commit/88501e9ea03ab9fc1dcdf673ba341279679afc73))
* set architecture when publishing ([#6](https://github.com/pyroscope-io/pyroscope-lambda-extension/issues/6)) ([ae3372f](https://github.com/pyroscope-io/pyroscope-lambda-extension/commit/ae3372f4697a1d97246c0eb73448bf752ec370a1))

## 1.0.0 (2022-07-04)


### Features

* initial version ([#1](https://github.com/pyroscope-io/pyroscope-lambda-extension/issues/1)) ([31471b4](https://github.com/pyroscope-io/pyroscope-lambda-extension/commit/31471b4fd059f511720baf6dba2e04a7236083ca))
```

## File: `CODEOWNERS`
```
* @grafana/pyroscope-team
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

   Copyright 2020 Pyroscope

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
build: build-amd

build-amd:
	GOOS=linux GOARCH=amd64 go build -o bin/x86_64/extensions/pyroscope-lambda-extension-x86_64 main.go

build-arm:
	GOOS=linux GOARCH=arm64 go build -o bin/arm64/extensions/pyroscope-lambda-extension-amd64 main.go

.PHONY: clean
clean:
	rm -Rf bin/

package-amd:
	cd bin/x86_64 && zip -r extension.zip extensions

package-arm:
	cd bin/arm64 && zip -r extension.zip extensions

build-GoExampleExtensionLayer:
	GOOS=linux GOARCH=amd64 go build -o $(ARTIFACTS_DIR)/extensions/pyroscope-lambda-extension main.go
	chmod +x $(ARTIFACTS_DIR)/extensions/pyroscope-lambda-extension

run-GoExampleExtensionLayer:
	go run pyroscope-lambda-extension/main.go


.PHONY: publish-layer-dev
publish-layer-dev: build
	cd bin && zip -r extension.zip extensions && aws lambda publish-layer-version --layer-name "pyroscope-extension-test" --region=us-east-1 --zip-file "fileb://extension.zip"
	./scripts/replace-version.sh

.PHONY: lambda-build
lambda-build:
	cd hello-world && sam build

.PHONY: lambda-local-invoke
lambda-local-invoke: lambda-build
	cd hello-world && sam local invoke --region=us-east-1 --env-vars local.json --shutdown

.PHONY: lambda-local-start
lambda-local-start: lambda-build
	cd hello-world && sam local start-lambda --region=us-east-1 --env-vars local.json

lambda-local-invoke-endpoint:
	aws lambda invoke --function-name "HelloWorldFunction" --endpoint-url "http://127.0.0.1:3001" --no-verify-ssl out.txt --region=us-east-1

lambda-deploy:
	cd hello-world && sam build && sam deploy --no-confirm-changeset

.PHONY: lint
lint: ## Run the lint across the codebase
	go run "$(shell scripts/pinned-tools.sh github.com/mgechev/revive)" -config revive.toml -formatter stylish ./...
	staticcheck -f stylish ./...

.PHONY: install-dev-tools
install-dev-tools: ## Install dev tools
	cat tools/tools.go | grep _ | awk -F'"' '{print $$2}' | xargs -tI {} go install {}

.PHONY: test
test: ## Runs the test suite
	go test -race $(shell go list ./...)

.PHONY: shellcheck
shellcheck: ## runs shellcheck against all script files
	shellcheck ./scripts/*.sh
```

## File: `README.md`
```markdown
# pyroscope-lambda-extension

# Usage
Add `pyroscope-lambda-extension` to your lambda
In your lambda, add the pyroscope client. For example, the go one

```go
func main() {
	pyroscope.Start(pyroscope.Config{
		ApplicationName: "simple.golang.lambda",
		ServerAddress:   "http://localhost:4040",
	})

	lambda.Start(HandleRequest)
}
```
Keep in mind it needs to be setup BEFORE the handler setup.
Also the `ServerAddress` **MUST** be `http://localhost:4040`, which is the address of the relay server.

Then set up the `PYROSCOPE_REMOTE_ADDRESS` environment variable.
If needed, the `PYROSCOPE_AUTH_TOKEN` can be supplied.

For a complete list of variables check the section below.

## Configuration
| env var                         | default                          | description                                                                                  |
|---------------------------------|----------------------------------|----------------------------------------------------------------------------------------------|
| `PYROSCOPE_REMOTE_ADDRESS`      | `https://ingest.pyroscope.cloud` | the pyroscope instance data will be relayed to                                               |
| `PYROSCOPE_AUTH_TOKEN`          | `""`                             | authorization key (token authentication)                                                     |
| `PYROSCOPE_SELF_PROFILING`      | `false`                          | whether to profile the extension itself or not                                               |
| `PYROSCOPE_LOG_LEVEL`           | `info`                           | `error` or `info` or `debug` or `trace`                                                      |
| `PYROSCOPE_TIMEOUT`             | `10s`                            | http client timeout ([go duration format](https://pkg.go.dev/time#Duration))                 |
| `PYROSCOPE_NUM_WORKERS`         | `5`                              | num of relay workers, pick based on the number of profile types                              |
| `PYROSCOPE_FLUSH_ON_INVOKE`     | `false`                          | wait for all relay requests to be finished/flushed before next `Invocation` event is allowed |
| `PYROSCOPE_HTTP_HEADERS`        | `{}`                             | extra http headers in json format, for example: {"X-Header": "Value"}                        |
| `PYROSCOPE_TENANT_ID`           | `""`                             | phlare tenant ID, passed as X-Scope-OrgID http header                                      |
| `PYROSCOPE_BASIC_AUTH_USER`     | `""` | HTTP basic auth user |
| `PYROSCOPE_BASIC_AUTH_PASSWORD` | `""`  | HTTP basic auth password  |
| `PYROSCOPE_LOG_FORMAT`                  | `"text"`         | format to choose from from `"text"` and `"json"`                                        |
| `PYROSCOPE_LOG_TIMESTAMP_FORMAT`        | `time.RFC3339`   | logging timestamp format ([go time format](https://golang.org/pkg/time/#pkg-constants)) |
| `PYROSCOPE_LOG_TIMESTAMP_DISABLE`       | `false`          | disables automatic timestamps in logging output                                         |
| `PYROSCOPE_LOG_TIMESTAMP_FIELD_NAME`    | `"time"`         | change default field name in logs of automatic timestamps                               |
| `PYROSCOPE_LOG_LEVEL_FIELD_NAME`        | `"level"`        | change default field name in logs of level                                              |
| `PYROSCOPE_LOG_MSG_FIELD_NAME`          | `"msg"`          | change default field name in logs of message                                            |
| `PYROSCOPE_LOG_LOGRUS_ERROR_FIELD_NAME` | `"logrus_error"` | change default field name in logs of logrus error                                       |
| `PYROSCOPE_LOG_FUNC_FIELD_NAME`         | `"func"`         | change default field name in logs of caller function                                    |
| `PYROSCOPE_LOG_FILE_FIELD_NAME`         | `"file"`         | change default field name in logs of caller file                                        |

# How it works
The profiler will run as normal, and periodically will send data to the relay server (the server running at `http://localhost:4040`).
Which will then relay that request to the Remote Address (configured as `PYROSCOPE_REMOTE_ADDRESS`)

The advantage here is that the lambda handler can run pretty fast, since it only has to send data to a server running locally.

Keep in mind you are still billed by the whole execution (lambda handler + extension).


# Developing
## Initial setup
1. a) Install [asdf](https://asdf-vm.com/guide/getting-started.html) then run `asdf install`
1. b) Or if you prefer, install the appropriate go version (for the exact go version check `.tool-versions`)
2. `make install-dev-tools`
3. If you have installed using `asdf`, you need to reshim (`asdf reshim`), to make asdf aware of the global tools (eg `staticcheck`)



## Running the extension
You can run the extension in dev mode. It will not register the extension.

It's useful to test the relay server initialization.
Keep in mind there's no lambda execution, therefore to test data is being relayed correctly you need
to ingest manually (hitting `http://localhost:4040/ingest`).

`PYROSCOPE_DEV_MODE=true go run main.go`

## Building the layer
Although [it's technically possible](https://github.com/aws/aws-sam-cli/issues/1187#issuecomment-540029710), at the time of this writing I could not run a lambda extension build locally.

Therefore to test it with a lambda locally you need to:

1. Login to aws
2. `make publish-layer-dev`

It will build and push the layer.

If you are testing using the hello-world app, don't forget to update the version in `Layers` field of template (./hello-world/template.yml)

## Running the lambda locally
`make lambda-local`

## Other tips
To test pushing data to a local pyroscope instance, you can set up in the lambda layer
the ip address of your computer (eg http://192.168.1.30:4040)


# Self hosting the extension
It's possible to publish the extension on your own AWS account

```shell
ARCH="YOUR_ARCHITECTURE"
REGION="YOUR_REGION"

GOOS=linux GOARCH=$ARCH go build -o bin/extensions/pyroscope-lambda-extension main.go
cd bin
zip -r extension.zip extensions
aws lambda publish-layer-version \
  --layer-name "pyroscope-lambda-extension" \
  --region=$YOUR_REGION \
  --zip-file "fileb://extension.zip"
```

# Releasing

Releases are managed by [`release-please`](https://github.com/googleapis/release-please). It assumes you are using [Conventional Commit messages].

The most important prefixes you should have in mind are:

 * `fix:` which represents bug fixes, and correlates to a SemVer patch.
 * `feat:` which represents a new feature, and correlates to a SemVer minor.
 * `feat!:`, or `fix!:`, `refactor!:`, etc., which represent a breaking change (indicated by the !) and will result in a SemVer major.
```

## File: `go.mod`
```
module github.com/pyroscope-io/pyroscope-lambda-extension

go 1.22.9

require (
	github.com/aws/aws-lambda-go v1.32.0
	github.com/davecgh/go-spew v1.1.1
	github.com/grafana/pyroscope-go v1.2.0
	github.com/mgechev/revive v1.2.1
	github.com/sirupsen/logrus v1.9.3
	github.com/stretchr/testify v1.9.0
	golang.org/x/sync v0.10.0
	honnef.co/go/tools v0.5.1
)

require (
	github.com/BurntSushi/toml v1.4.1-0.20240526193622-a339e1f7089c // indirect
	github.com/chavacava/garif v0.0.0-20220316182200-5cad0b5181d4 // indirect
	github.com/fatih/color v1.13.0 // indirect
	github.com/fatih/structtag v1.2.0 // indirect
	github.com/grafana/pyroscope-go/godeltaprof v0.1.8 // indirect
	github.com/klauspost/compress v1.17.11 // indirect
	github.com/mattn/go-colorable v0.1.9 // indirect
	github.com/mattn/go-isatty v0.0.14 // indirect
	github.com/mattn/go-runewidth v0.0.9 // indirect
	github.com/mgechev/dots v0.0.0-20210922191527-e955255bf517 // indirect
	github.com/mitchellh/go-homedir v1.1.0 // indirect
	github.com/olekukonko/tablewriter v0.0.5 // indirect
	github.com/pkg/errors v0.9.1 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	golang.org/x/exp/typeparams v0.0.0-20250128182459-e0ece0dbea4c // indirect
	golang.org/x/mod v0.22.0 // indirect
	golang.org/x/sys v0.29.0 // indirect
	golang.org/x/tools v0.29.0 // indirect
	gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)
```

## File: `go.sum`
```
github.com/BurntSushi/toml v1.1.0/go.mod h1:CxXYINrC8qIiEnFrOxCa7Jy5BFHlXnUU2pbicEuybxQ=
github.com/BurntSushi/toml v1.4.1-0.20240526193622-a339e1f7089c h1:pxW6RcqyfI9/kWtOwnv/G+AzdKuy2ZrqINhenH4HyNs=
github.com/BurntSushi/toml v1.4.1-0.20240526193622-a339e1f7089c/go.mod h1:ukJfTF/6rtPPRCnwkur4qwRxa8vTRFBF0uk2lLoLwho=
github.com/aws/aws-lambda-go v1.32.0 h1:i8MflawW1hoyYp85GMH7LhvAs4cqzL7LOS6fSv8l2KM=
github.com/aws/aws-lambda-go v1.32.0/go.mod h1:IF5Q7wj4VyZyUFnZ54IQqeWtctHQ9tz+KhcbDenr220=
github.com/chavacava/garif v0.0.0-20220316182200-5cad0b5181d4 h1:tFXjAxje9thrTF4h57Ckik+scJjTWdwAtZqZPtOT48M=
github.com/chavacava/garif v0.0.0-20220316182200-5cad0b5181d4/go.mod h1:W8EnPSQ8Nv4fUjc/v1/8tHFqhuOJXnRub0dTfuAQktU=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/fatih/color v1.13.0 h1:8LOYc1KYPPmyKMuN8QV2DNRWNbLo6LZ0iLs8+mlH53w=
github.com/fatih/color v1.13.0/go.mod h1:kLAiJbzzSOZDVNGyDpeOxJ47H46qBXwg5ILebYFFOfk=
github.com/fatih/structtag v1.2.0 h1:/OdNE99OxoI/PqaW/SuSK9uxxT3f/tcSZgon/ssNSx4=
github.com/fatih/structtag v1.2.0/go.mod h1:mBJUNpUnHmRKrKlQQlmCrh5PuhftFbNv8Ys4/aAZl94=
github.com/google/go-cmp v0.6.0 h1:ofyhxvXcZhMsU5ulbFiLKl/XBFqE1GSq7atu8tAmTRI=
github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/grafana/pyroscope-go v1.2.0 h1:aILLKjTj8CS8f/24OPMGPewQSYlhmdQMBmol1d3KGj8=
github.com/grafana/pyroscope-go v1.2.0/go.mod h1:2GHr28Nr05bg2pElS+dDsc98f3JTUh2f6Fz1hWXrqwk=
github.com/grafana/pyroscope-go/godeltaprof v0.1.8 h1:iwOtYXeeVSAeYefJNaxDytgjKtUuKQbJqgAIjlnicKg=
github.com/grafana/pyroscope-go/godeltaprof v0.1.8/go.mod h1:2+l7K7twW49Ct4wFluZD3tZ6e0SjanjcUUBPVD/UuGU=
github.com/klauspost/compress v1.17.11 h1:In6xLpyWOi1+C7tXUUWv2ot1QvBjxevKAaI6IXrJmUc=
github.com/klauspost/compress v1.17.11/go.mod h1:pMDklpSncoRMuLFrf1W9Ss9KT+0rH90U12bZKk7uwG0=
github.com/kr/pretty v0.2.1 h1:Fmg33tUaq4/8ym9TJN1x7sLJnHVwhP33CNkpYV/7rwI=
github.com/kr/pretty v0.2.1/go.mod h1:ipq/a2n7PKx3OHsz4KJII5eveXtPO4qwEXGdVfWzfnI=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0 h1:45sCR5RtlFHMR4UwH9sdQ5TC8v0qDQCHnXt+kaKSTVE=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/mattn/go-colorable v0.1.9 h1:sqDoxXbdeALODt0DAeJCVp38ps9ZogZEAXjus69YV3U=
github.com/mattn/go-colorable v0.1.9/go.mod h1:u6P/XSegPjTcexA+o6vUJrdnUu04hMope9wVRipJSqc=
github.com/mattn/go-isatty v0.0.12/go.mod h1:cbi8OIDigv2wuxKPP5vlRcQ1OAZbq2CE4Kysco4FUpU=
github.com/mattn/go-isatty v0.0.14 h1:yVuAays6BHfxijgZPzw+3Zlu5yQgKGP2/hcQbHb7S9Y=
github.com/mattn/go-isatty v0.0.14/go.mod h1:7GGIvUiUoEMVVmxf/4nioHXj79iQHKdU27kJ6hsGG94=
github.com/mattn/go-runewidth v0.0.9 h1:Lm995f3rfxdpd6TSmuVCHVb/QhupuXlYr8sCI/QdE+0=
github.com/mattn/go-runewidth v0.0.9/go.mod h1:H031xJmbD/WCDINGzjvQ9THkh0rPKHF+m2gUSrubnMI=
github.com/mgechev/dots v0.0.0-20210922191527-e955255bf517 h1:zpIH83+oKzcpryru8ceC6BxnoG8TBrhgAvRg8obzup0=
github.com/mgechev/dots v0.0.0-20210922191527-e955255bf517/go.mod h1:KQ7+USdGKfpPjXk4Ga+5XxQM4Lm4e3gAogrreFAYpOg=
github.com/mgechev/revive v1.2.1 h1:GjFml7ZsoR0IrQ2E2YIvWFNS5GPDV7xNwvA5GM1HZC4=
github.com/mgechev/revive v1.2.1/go.mod h1:+Ro3wqY4vakcYNtkBWdZC7dBg1xSB6sp054wWwmeFm0=
github.com/mitchellh/go-homedir v1.1.0 h1:lukF9ziXFxDFPkA1vsr5zpc1XuPDn/wFntq5mG+4E0Y=
github.com/mitchellh/go-homedir v1.1.0/go.mod h1:SfyaCUpYCn1Vlf4IUYiD9fPX4A5wJrkLzIz1N1q0pr0=
github.com/olekukonko/tablewriter v0.0.5 h1:P2Ga83D34wi1o9J6Wh1mRuqd4mF/x/lgBS7N7AbDhec=
github.com/olekukonko/tablewriter v0.0.5/go.mod h1:hPp6KlRPjbx+hW8ykQs1w3UBbZlj6HuIJcUGPhkA7kY=
github.com/pkg/errors v0.9.1 h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=
github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/sirupsen/logrus v1.9.3 h1:dueUQJ1C2q9oE3F7wvmSGAaVtTmUizReu6fjN8uqzbQ=
github.com/sirupsen/logrus v1.9.3/go.mod h1:naHLuLoDiP4jHNo9R0sCBMtWGeIprob74mVsIT4qYEQ=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.5.2 h1:xuMeJ0Sdp5ZMRXx/aWO6RZxdr3beISkG5/G/aIRr3pY=
github.com/stretchr/objx v0.5.2/go.mod h1:FRsXN1f5AsAjCGJKqEizvkpNtU+EGNCLh3NxZ/8L+MA=
github.com/stretchr/testify v1.7.0/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.7.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.9.0 h1:HtqpIVDClZ4nwg75+f6Lvsy/wHu+3BoSGCbBAcpTsTg=
github.com/stretchr/testify v1.9.0/go.mod h1:r2ic/lqez/lEtzL7wO/rwa5dbSLXVDPFyf8C91i36aY=
github.com/yuin/goldmark v1.4.1/go.mod h1:mwnBkeHKe2W/ZEtQ+71ViKU8L12m81fl3OWwC1Zlc8k=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20210921155107-089bfa567519/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/exp/typeparams v0.0.0-20250128182459-e0ece0dbea4c h1:sMPlrlhFwAE8DZXzAIztseGS+N8uGlLbFQCOTsoIPmc=
golang.org/x/exp/typeparams v0.0.0-20250128182459-e0ece0dbea4c/go.mod h1:AbB0pIl9nAr9wVwH+Z2ZpaocVmF5I4GyWCDIsVjR0bk=
golang.org/x/mod v0.6.0-dev.0.20220106191415-9b9b3d81d5e3/go.mod h1:3p9vT2HGsQu2K1YbXdKPJLVgG5VJdoTa1poYQBtP1AY=
golang.org/x/mod v0.22.0 h1:D4nJWe9zXqHOmWqj4VMOJhvzj7bEZg4wEYa759z1pH4=
golang.org/x/mod v0.22.0/go.mod h1:6SkKJ3Xj0I0BrPOZoBy3bdMptDDU9oJrpohJ3eWZ1fY=
golang.org/x/net v0.0.0-20190620200207-3b0461eec859/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20210226172049-e18ecbb05110/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/net v0.0.0-20211015210444-4f30a5c0130f/go.mod h1:9nx3DQGgdP8bBQD5qxJ1jj9UTztislL4KSBs9R2vV5Y=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20210220032951-036812b2e83c/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.10.0 h1:3NQrjDixjgGwUOCaF8w2+VYHv0Ve/vGYSbdkTa98gmQ=
golang.org/x/sync v0.10.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20200116001909-b77594299b42/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200223170610-d5e6a3e2c0ae/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20201119102817-f84b799fce68/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210423082822-04245dca01da/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210615035016-665e8c7367d1/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210630005230-0f9fa26af87c/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20211019181941-9d821ace8654/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220715151400-c0bba94af5f8/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.29.0 h1:TPYlXGxvx1MGTn2GiZDhnjPA9wZzZeGKHHmKhHYvgaU=
golang.org/x/sys v0.29.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/term v0.0.0-20201126162022-7de9c90e9dd1/go.mod h1:bj7SfCRtBDWHUb9snDiAeCFNEtKQo2Wmx5Cou7ajbmo=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.3/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.6/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.7/go.mod h1:u+2+/6zg+i71rQMx5EYifcz6MCKuco9NR6JIITiCfzQ=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20191119224855-298f0cb1881e/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.1.10/go.mod h1:Uh6Zz+xoGYZom868N8YTex3t7RhtHDBrE8Gzo9bV56E=
golang.org/x/tools v0.29.0 h1:Xx0h3TtM9rzQpQuR4dKLrdglAmCEN5Oi+P74JdhdzXE=
golang.org/x/tools v0.29.0/go.mod h1:KMQVMRsVxU6nHCFXrBPhDB8XncLNLM0lIy/F14RP588=
golang.org/x/xerrors v0.0.0-20190717185122-a985d3407aa7/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191011141410-1b5146add898/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20200804184101-5ec99f83aff1/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
honnef.co/go/tools v0.5.1 h1:4bH5o3b5ZULQ4UrBmP+63W9r7qIkqJClEA9ko5YKx+I=
honnef.co/go/tools v0.5.1/go.mod h1:e9irvo83WDG9/irijV44wr3tbhcFeRnfpVlRqVwpzMs=
```

## File: `main.go`
```go
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package main

import (
	"context"
	"os"
	"os/signal"
	"path/filepath"
	"strconv"
	"syscall"
	"time"

	"github.com/sirupsen/logrus"

	"github.com/pyroscope-io/pyroscope-lambda-extension/extension"
	"github.com/pyroscope-io/pyroscope-lambda-extension/internal/sessionid"
	"github.com/pyroscope-io/pyroscope-lambda-extension/relay"
	"github.com/pyroscope-io/pyroscope-lambda-extension/selfprofiler"
)

var (
	extensionName   = filepath.Base(os.Args[0]) // extension name has to match the filename
	extensionClient = extension.NewClient(os.Getenv("AWS_LAMBDA_RUNTIME_API"))

	// in dev mode there's no extension registration. useful for testing locally
	devMode = getEnvBool("PYROSCOPE_DEV_MODE")

	// 'trace' | 'debug' | 'info' | 'error'
	logLevel = getEnvStrOr("PYROSCOPE_LOG_LEVEL", "info")

	// log format options 'json' | 'text'
	logFormat = getEnvStrOr("PYROSCOPE_LOG_FORMAT", "text")

	// log timestamp format (default: time.RFC3339), see https://golang.org/pkg/time/#pkg-constants
	logTsFormat = getEnvStrOr("PYROSCOPE_LOG_TIMESTAMP_FORMAT", time.RFC3339)

	logDisableTs = getEnvBool("PYROSCOPE_LOG_TIMESTAMP_DISABLE")

	// log field names
	logTsFieldName    = getEnvStrOr("PYROSCOPE_LOG_TIMESTAMP_FIELD_NAME", logrus.FieldKeyTime)
	logLevelFieldName = getEnvStrOr("PYROSCOPE_LOG_LEVEL_FIELD_NAME", logrus.FieldKeyLevel)
	logMsgFieldName   = getEnvStrOr("PYROSCOPE_LOG_MSG_FIELD_NAME", logrus.FieldKeyMsg)
	logErrorFieldName = getEnvStrOr("PYROSCOPE_LOG_LOGRUS_ERROR_FIELD_NAME", logrus.FieldKeyLogrusError)
	logFuncFieldName  = getEnvStrOr("PYROSCOPE_LOG_FUNC_FIELD_NAME", logrus.FieldKeyFunc)
	logFileFieldName  = getEnvStrOr("PYROSCOPE_LOG_FILE_FIELD_NAME", logrus.FieldKeyFile)

	// to where relay data to
	remoteAddress = getEnvStrOr("PYROSCOPE_REMOTE_ADDRESS", "https://profiles-prod-001.grafana.net")

	authToken         = getEnvStrOr("PYROSCOPE_AUTH_TOKEN", "")
	basicAuthUser     = getEnvStrOr("PYROSCOPE_BASIC_AUTH_USER", "")
	basicAuthPassword = getEnvStrOr("PYROSCOPE_BASIC_AUTH_PASSWORD", "")
	tenantID          = getEnvStrOr("PYROSCOPE_TENANT_ID", "")
	timeout           = getEnvDurationOr("PYROSCOPE_TIMEOUT", time.Second*10)
	numWorkers        = getEnvIntOr("PYROSCOPE_NUM_WORKERS", 5)

	// profile the extension?
	selfProfiling = getEnvBool("PYROSCOPE_SELF_PROFILING")

	flushOnInvoke = getEnvBool("PYROSCOPE_FLUSH_ON_INVOKE")

	httpHeaders = getEnvStrOr("PYROSCOPE_HTTP_HEADERS", "")
)

func main() {
	logger := initLogger()
	ctx, cancel := context.WithCancel(context.Background())

	// Init components
	remoteClient := relay.NewRemoteClient(logger, &relay.RemoteClientCfg{
		Address:             remoteAddress,
		AuthToken:           authToken,
		BasicAuthUser:       basicAuthUser,
		BasicAuthPassword:   basicAuthPassword,
		TenantID:            tenantID,
		HTTPHeadersJSON:     httpHeaders,
		Timeout:             timeout,
		MaxIdleConnsPerHost: numWorkers,
		SessionID:           sessionid.New().String(),
	})
	// TODO(eh-am): a find a better default for num of workers
	queue := relay.NewRemoteQueue(logger, &relay.RemoteQueueCfg{NumWorkers: numWorkers}, remoteClient)
	ctrl := relay.NewController(logger, queue)
	server := relay.NewServer(logger, &relay.ServerCfg{ServerAddress: "0.0.0.0:4040"}, ctrl.RelayRequest)

	selfProfiler := selfprofiler.New(logger, selfProfiling, remoteAddress, authToken)
	orch := relay.NewOrchestrator(logger, queue, server, selfProfiler)

	// Register signals
	sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, syscall.SIGTERM, syscall.SIGINT)
	go func() {
		s := <-sigs
		logger.Infof("Received signal: '%s'. Exiting\n", s)

		cancel()
	}()

	// Start relay
	go func() {
		logger.Info("Starting relay")
		if err := orch.Start(); err != nil {
			logger.Error(err)
		}
	}()

	// Register extension
	if devMode {
		// In dev mode we don't do anything
		runDevMode(ctx, logger, orch)
	} else {
		// Register extension and start listening for events
		runProdMode(ctx, logger, orch, queue)
	}
}

func initLogger() *logrus.Entry {
	// Initialize logger
	logger := logrus.WithFields(logrus.Fields{"svc": "pyroscope-lambda-ext-main"})
	lvl, err := logrus.ParseLevel(logLevel)
	if err != nil {
		lvl = logrus.InfoLevel
	}

	logrus.SetLevel(lvl)

	var f logrus.Formatter
	switch logFormat {
	case "json":
		f = &logrus.JSONFormatter{
			TimestampFormat:  logTsFormat,
			DisableTimestamp: logDisableTs,
			FieldMap: logrus.FieldMap{
				logrus.FieldKeyTime:        logTsFieldName,
				logrus.FieldKeyLevel:       logLevelFieldName,
				logrus.FieldKeyMsg:         logMsgFieldName,
				logrus.FieldKeyLogrusError: logErrorFieldName,
				logrus.FieldKeyFunc:        logFuncFieldName,
				logrus.FieldKeyFile:        logFileFieldName,
			},
		}
	default:
		f = &logrus.TextFormatter{
			TimestampFormat:  logTsFormat,
			DisableTimestamp: logDisableTs,
			FieldMap: logrus.FieldMap{
				logrus.FieldKeyTime:        logTsFieldName,
				logrus.FieldKeyLevel:       logLevelFieldName,
				logrus.FieldKeyMsg:         logMsgFieldName,
				logrus.FieldKeyLogrusError: logErrorFieldName,
				logrus.FieldKeyFunc:        logFuncFieldName,
				logrus.FieldKeyFile:        logFileFieldName,
			},
		}
	}
	logrus.SetFormatter(f)

	return logger
}

func runDevMode(ctx context.Context, logger *logrus.Entry, orch *relay.Orchestrator) {
	//lint:ignore S1000 we want to keep the same look and feel of runProdMode
	select {
	case <-ctx.Done():
		err := orch.Shutdown()
		if err != nil {
			logger.Error(err)
		}
		return
	}
}

func runProdMode(ctx context.Context, logger *logrus.Entry, orch *relay.Orchestrator, queue *relay.RemoteQueue) {
	res, err := extensionClient.Register(ctx, extensionName)
	if err != nil {
		panic(err)
	}
	logger.Trace("Register response", res)

	// Will block until shutdown event is received or cancelled via the context.
	processEvents(ctx, logger, orch, queue)
}

func processEvents(ctx context.Context, log *logrus.Entry, orch *relay.Orchestrator, queue *relay.RemoteQueue) {
	log.Debug("Starting processing events")

	shutdown := func() {
		err := orch.Shutdown()
		if err != nil {
			log.Error("Error while stopping server", err)
		}
		log.Debug("Exiting")
	}

	for {
		select {
		case <-ctx.Done():
			shutdown()
			return
		default:
			log.Debug("Waiting for event...")
			res, err := extensionClient.NextEvent(ctx)
			if err != nil {
				log.Error("Failed to register extension", err)

				shutdown()
				return
			}

			log.Trace("Received event:", res)
			// Exit if we receive a SHUTDOWN event
			if res.EventType == extension.Shutdown {
				log.Debug("Received SHUTDOWN event")
				shutdown()
				return
			}
			if res.EventType == extension.Invoke && flushOnInvoke {
				queue.Flush()
			}
		}
	}
}

func getEnvStrOr(key string, fallback string) string {
	k, ok := os.LookupEnv(key)

	// has an explicit value
	if ok && k != "" {
		return k
	}

	return fallback
}

func getEnvBool(key string) bool {
	k := os.Getenv(key)
	v, err := strconv.ParseBool(k)
	if err != nil {
		return false
	}

	return v
}

func getEnvDurationOr(key string, fallback time.Duration) time.Duration {
	k, ok := os.LookupEnv(key)

	// has an explicit value
	if ok && k != "" {
		dur, err := time.ParseDuration(k)
		if err != nil {
			logrus.Warnf("invalid value for env var '%s': '%s' defaulting to '%s'", key, k, fallback)
			return fallback
		}

		return dur
	}

	return fallback
}

func getEnvIntOr(key string, fallback int) int {
	k, ok := os.LookupEnv(key)

	// has an explicit value
	if ok && k != "" {
		val, err := strconv.Atoi(k)
		if err != nil {
			logrus.Warnf("invalid value for env var '%s': '%s' defaulting to '%d'", key, k, fallback)
			return fallback
		}
		return val
	}

	return fallback
}
```

## File: `revive.toml`
```
# See this page for descriptions:
# https://github.com/mgechev/revive/blob/master/RULES_DESCRIPTIONS.md

ignoreGeneratedHeader = false
severity = "error"
confidence = 0.8
errorCode = 1
warningCode = 0

[directive.specify-disable-reason]
[rule.context-keys-type]
[rule.time-naming]
[rule.var-declaration]
[rule.unexported-return]
[rule.errorf]
[rule.blank-imports]
[rule.context-as-argument]
[rule.dot-imports]
[rule.error-return]
[rule.error-strings]
[rule.error-naming]
# [rule.exported]
[rule.if-return]
[rule.increment-decrement]
[rule.var-naming]
[rule.package-comments]
[rule.range]
[rule.receiver-naming]
[rule.indent-error-flow]
[rule.argument-limit]
  arguments = [5]
[rule.max-public-structs]
  arguments = [10]
[rule.empty-block]
[rule.superfluous-else]
# [rule.get-return]
[rule.modifies-parameter]
[rule.confusing-results]
[rule.deep-exit]
[rule.unused-parameter]
[rule.unreachable-code]
# [rule.add-constant]
#   arguments = [{maxLitCount = "10",allowStrs ="\"\"",allowInts="0,1,2,3,4,5,6,7,8,9,16,24,32,40,48,56,64,128,256,0xff",allowFloats="0.0,0.,1.0,1.,2.0,2."}]
# [rule.flag-parameter]
[rule.unnecessary-stmt]
[rule.struct-tag]
[rule.modifies-value-receiver]
[rule.constant-logical-expr]
[rule.bool-literal-in-expr]
[rule.redefines-builtin-id]
[rule.function-result-limit]
  arguments = [4]
[rule.imports-blacklist]
[rule.range-val-in-closure]
[rule.range-val-address]
[rule.waitgroup-by-value]
[rule.atomic]
[rule.empty-lines]
[rule.line-length-limit]
  arguments = [180]
[rule.duplicated-imports]
[rule.import-shadowing]
[rule.bare-return]
[rule.unused-receiver]
[rule.string-of-int]


# These are pretty much disabled
[rule.cognitive-complexity]
  arguments = [55]

[rule.cyclomatic]
  arguments = [50]

# [rule.unhandled-error]
#   arguments = ["sb.WriteString", "fmt.Fprintf", "fmt.Printf", "fmt.Println"]

```

## File: `examples/go/main.go`
```go
package main

import (
	"context"
	"fmt"
	"runtime/pprof"

	"github.com/aws/aws-lambda-go/lambda"
	"github.com/grafana/pyroscope-go"
)

type MyEvent struct {
	Name string `json:"name"`
}

//go:noinline
func work(n int) {
	// revive:disable:empty-block this is fine because this is a example app, not real production code
	for i := 0; i < n; i++ {
	}
	// revive:enable:empty-block
}

func fastFunction(c context.Context) {
	pyroscope.TagWrapper(c, pyroscope.Labels("function", "fast"), func(c context.Context) {
		work(20000000)
	})
}

func slowFunction(c context.Context) {
	// standard pprof.Do wrappers work as well
	pprof.Do(c, pprof.Labels("function", "slow"), func(c context.Context) {
		work(80000000)
	})
}

func HandleRequest(ctx context.Context, name MyEvent) (string, error) {
	i := 0
	//	for i < 10 {
	fastFunction(ctx)
	slowFunction(ctx)
	i++
	//	}

	return fmt.Sprintf("Hello %s!", name.Name), nil
}

func main() {
	pyroscope.Start(pyroscope.Config{
		ApplicationName: "simple.golang.lambda",
		ServerAddress:   "http://localhost:4040",
		Logger:          pyroscope.StandardLogger,
	})

	lambda.Start(HandleRequest)
}
```

## File: `examples/nodejs/.tool-versions`
```
nodejs 16.16.0
```

## File: `examples/nodejs/index.js`
```javascript
const Pyroscope = require("@pyroscope/nodejs");

Pyroscope.init({
  serverAddress: "http://localhost:4040",
  appName: "my-node-service",
});
Pyroscope.start();

function doWork(number) {
  for (let i = 0; i < number; i++) {}
}

exports.handler = async (event, context) => {
  try {
    response = {
      "statusCode": 200,
      "body": JSON.stringify({
        message: "hello world",
      }),
    };
  } catch (err) {
    console.log(err);
    return err;
  }

  doWork(99999999);
  doWork(99999999);

  return response;
};
```

## File: `examples/nodejs/package.json`
```json
{
  "name": "nodejs",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "Apache-2.0",
  "dependencies": {
    "@pyroscope/nodejs": "^0.4.3"
  }
}
```

## File: `extension/client.go`
```go
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package extension

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

// RegisterResponse is the body of the response for /register
type RegisterResponse struct {
	FunctionName    string `json:"functionName"`
	FunctionVersion string `json:"functionVersion"`
	Handler         string `json:"handler"`
}

// NextEventResponse is the response for /event/next
type NextEventResponse struct {
	EventType          EventType `json:"eventType"`
	DeadlineMs         int64     `json:"deadlineMs"`
	RequestID          string    `json:"requestId"`
	InvokedFunctionArn string    `json:"invokedFunctionArn"`
	Tracing            Tracing   `json:"tracing"`
}

// Tracing is part of the response for /event/next
type Tracing struct {
	Type  string `json:"type"`
	Value string `json:"value"`
}

// StatusResponse is the body of the response for /init/error and /exit/error
type StatusResponse struct {
	Status string `json:"status"`
}

// EventType represents the type of events recieved from /event/next
type EventType string

const (
	// Invoke is a lambda invoke
	Invoke EventType = "INVOKE"

	// Shutdown is a shutdown event for the environment
	Shutdown EventType = "SHUTDOWN"

	extensionNameHeader      = "Lambda-Extension-Name"
	extensionIdentiferHeader = "Lambda-Extension-Identifier"
	extensionErrorType       = "Lambda-Extension-Function-Error-Type"
)

// Client is a simple client for the Lambda Extensions API
type Client struct {
	baseURL     string
	httpClient  *http.Client
	extensionID string
}

// NewClient returns a Lambda Extensions API client
func NewClient(awsLambdaRuntimeAPI string) *Client {
	baseURL := fmt.Sprintf("http://%s/2020-01-01/extension", awsLambdaRuntimeAPI)
	return &Client{
		baseURL:    baseURL,
		httpClient: &http.Client{},
	}
}

// Register will register the extension with the Extensions API
func (e *Client) Register(ctx context.Context, filename string) (*RegisterResponse, error) {
	const action = "/register"
	url := e.baseURL + action

	reqBody, err := json.Marshal(map[string]interface{}{
		"events": []EventType{Invoke, Shutdown},
	})
	if err != nil {
		return nil, err
	}
	httpReq, err := http.NewRequestWithContext(ctx, "POST", url, bytes.NewBuffer(reqBody))
	if err != nil {
		return nil, err
	}
	httpReq.Header.Set(extensionNameHeader, filename)
	httpRes, err := e.httpClient.Do(httpReq)
	if err != nil {
		return nil, err
	}
	if httpRes.StatusCode != 200 {
		return nil, fmt.Errorf("request failed with status %s", httpRes.Status)
	}
	defer httpRes.Body.Close()
	body, err := io.ReadAll(httpRes.Body)
	if err != nil {
		return nil, err
	}
	res := RegisterResponse{}
	err = json.Unmarshal(body, &res)
	if err != nil {
		return nil, err
	}
	e.extensionID = httpRes.Header.Get(extensionIdentiferHeader)
	print(e.extensionID)
	return &res, nil
}

// NextEvent blocks while long polling for the next lambda invoke or shutdown
func (e *Client) NextEvent(ctx context.Context) (*NextEventResponse, error) {
	const action = "/event/next"
	url := e.baseURL + action

	httpReq, err := http.NewRequestWithContext(ctx, "GET", url, nil)
	if err != nil {
		return nil, err
	}
	httpReq.Header.Set(extensionIdentiferHeader, e.extensionID)
	httpRes, err := e.httpClient.Do(httpReq)
	if err != nil {
		return nil, err
	}
	if httpRes.StatusCode != 200 {
		return nil, fmt.Errorf("request failed with status %s", httpRes.Status)
	}
	defer httpRes.Body.Close()
	body, err := io.ReadAll(httpRes.Body)
	if err != nil {
		return nil, err
	}
	res := NextEventResponse{}
	err = json.Unmarshal(body, &res)
	if err != nil {
		return nil, err
	}
	return &res, nil
}

// InitError reports an initialization error to the platform. Call it when you registered but failed to initialize
func (e *Client) InitError(ctx context.Context, errorType string) (*StatusResponse, error) {
	const action = "/init/error"
	url := e.baseURL + action

	httpReq, err := http.NewRequestWithContext(ctx, "POST", url, nil)
	if err != nil {
		return nil, err
	}
	httpReq.Header.Set(extensionIdentiferHeader, e.extensionID)
	httpReq.Header.Set(extensionErrorType, errorType)
	httpRes, err := e.httpClient.Do(httpReq)
	if err != nil {
		return nil, err
	}
	if httpRes.StatusCode != 200 {
		return nil, fmt.Errorf("request failed with status %s", httpRes.Status)
	}
	defer httpRes.Body.Close()
	body, err := io.ReadAll(httpRes.Body)
	if err != nil {
		return nil, err
	}
	res := StatusResponse{}
	err = json.Unmarshal(body, &res)
	if err != nil {
		return nil, err
	}
	return &res, nil
}

// ExitError reports an error to the platform before exiting. Call it when you encounter an unexpected failure
func (e *Client) ExitError(ctx context.Context, errorType string) (*StatusResponse, error) {
	const action = "/exit/error"
	url := e.baseURL + action

	httpReq, err := http.NewRequestWithContext(ctx, "POST", url, nil)
	if err != nil {
		return nil, err
	}
	httpReq.Header.Set(extensionIdentiferHeader, e.extensionID)
	httpReq.Header.Set(extensionErrorType, errorType)
	httpRes, err := e.httpClient.Do(httpReq)
	if err != nil {
		return nil, err
	}
	if httpRes.StatusCode != 200 {
		return nil, fmt.Errorf("request failed with status %s", httpRes.Status)
	}
	defer httpRes.Body.Close()
	body, err := io.ReadAll(httpRes.Body)
	if err != nil {
		return nil, err
	}
	res := StatusResponse{}
	err = json.Unmarshal(body, &res)
	if err != nil {
		return nil, err
	}
	return &res, nil
}
```

## File: `internal/flameql/error.go`
```go
package flameql

import (
	"errors"
	"fmt"
)

var (
	ErrInvalidQuerySyntax    = errors.New("invalid query syntax")
	ErrInvalidAppName        = errors.New("invalid application name")
	ErrInvalidMatchersSyntax = errors.New("invalid tag matchers syntax")
	ErrInvalidTagKey         = errors.New("invalid tag key")
	ErrInvalidTagValueSyntax = errors.New("invalid tag value syntax")

	ErrAppNameIsRequired = errors.New("application name is required")
	ErrTagKeyIsRequired  = errors.New("tag key is required")
	ErrTagKeyReserved    = errors.New("tag key is reserved")

	ErrMatchOperatorIsRequired = errors.New("match operator is required")
	ErrUnknownOp               = errors.New("unknown tag match operator")
)

type Error struct {
	Inner error
	Expr  string
	// TODO: add offset?
}

func newErr(err error, expr string) *Error { return &Error{Inner: err, Expr: expr} }

func (e *Error) Error() string { return e.Inner.Error() + ": " + e.Expr }

func (e *Error) Unwrap() error { return e.Inner }

func newInvalidTagKeyRuneError(k string, r rune) *Error {
	return newInvalidRuneError(ErrInvalidTagKey, k, r)
}

func newInvalidAppNameRuneError(k string, r rune) *Error {
	return newInvalidRuneError(ErrInvalidAppName, k, r)
}

func newInvalidRuneError(err error, k string, r rune) *Error {
	return newErr(err, fmt.Sprintf("%s: character is not allowed: %q", k, r))
}
```

## File: `internal/flameql/flameql.go`
```go
package flameql

import "regexp"

type Query struct {
	AppName  string
	Matchers []*TagMatcher

	q string // The original query string.
}

func (q *Query) String() string { return q.q }

type TagMatcher struct {
	Key   string
	Value string
	Op

	R *regexp.Regexp
}

type Op int

const (
	// The order should respect operator priority and cost.
	// Negating operators go first. See IsNegation.
	_               Op = iota
	OpNotEqual         // !=
	OpNotEqualRegex    // !~
	OpEqual            // =
	OpEqualRegex       // =~
)

const (
	ReservedTagKeyName = "__name__"
)

var reservedTagKeys = []string{
	ReservedTagKeyName,
}

// IsNegation reports whether the operator assumes negation.
func (o Op) IsNegation() bool { return o < OpEqual }

// ByPriority is a supplemental type for sorting tag matchers.
type ByPriority []*TagMatcher

func (p ByPriority) Len() int           { return len(p) }
func (p ByPriority) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
func (p ByPriority) Less(i, j int) bool { return p[i].Op < p[j].Op }

func (m *TagMatcher) Match(v string) bool {
	switch m.Op {
	case OpEqual:
		return m.Value == v
	case OpNotEqual:
		return m.Value != v
	case OpEqualRegex:
		return m.R.Match([]byte(v))
	case OpNotEqualRegex:
		return !m.R.Match([]byte(v))
	default:
		panic("invalid match operator")
	}
}

// ValidateTagKey report an error if the given key k violates constraints.
//
// The function should be used to validate user input. The function returns
// ErrTagKeyReserved if the key is valid but reserved for internal use.
func ValidateTagKey(k string) error {
	if len(k) == 0 {
		return ErrTagKeyIsRequired
	}
	for _, r := range k {
		if !IsTagKeyRuneAllowed(r) {
			return newInvalidTagKeyRuneError(k, r)
		}
	}
	if IsTagKeyReserved(k) {
		return newErr(ErrTagKeyReserved, k)
	}
	return nil
}

// ValidateAppName report an error if the given app name n violates constraints.
func ValidateAppName(n string) error {
	if len(n) == 0 {
		return ErrAppNameIsRequired
	}
	for _, r := range n {
		if !IsAppNameRuneAllowed(r) {
			return newInvalidAppNameRuneError(n, r)
		}
	}
	return nil
}

func IsTagKeyRuneAllowed(r rune) bool {
	return (r >= 'a' && r <= 'z') || (r >= 'A' && r <= 'Z') || (r >= '0' && r <= '9') || r == '_'
}

func IsAppNameRuneAllowed(r rune) bool {
	return r == '-' || r == '.' || IsTagKeyRuneAllowed(r)
}

func IsTagKeyReserved(k string) bool {
	for _, s := range reservedTagKeys {
		if s == k {
			return true
		}
	}
	return false
}
```

## File: `internal/flameql/key.go`
```go
package flameql

import (
	"errors"
	"strconv"
	"strings"
	"time"

	"github.com/pyroscope-io/pyroscope-lambda-extension/internal/sortedmap"
)

type Key struct {
	labels map[string]string
}

type ParserState int

const (
	nameParserState ParserState = iota
	tagKeyParserState
	tagValueParserState
	doneParserState
)

func NewKey(labels map[string]string) *Key { return &Key{labels: labels} }

func ParseKey(name string) (*Key, error) {
	k := &Key{labels: make(map[string]string)}
	p := parser{parserState: nameParserState}
	var err error
	for _, r := range name + "{" {
		switch p.parserState {
		case nameParserState:
			err = p.nameParserCase(r, k)
		case tagKeyParserState:
			p.tagKeyParserCase(r)
		case tagValueParserState:
			err = p.tagValueParserCase(r, k)
		}
		if err != nil {
			return nil, err
		}
	}
	return k, nil
}

type parser struct {
	parserState ParserState
	key         string
	value       string
}

// ParseKey's nameParserState switch case
func (p *parser) nameParserCase(r int32, k *Key) error {
	switch r {
	case '{':
		p.parserState = tagKeyParserState
		appName := strings.TrimSpace(p.value)
		if err := ValidateAppName(appName); err != nil {
			return err
		}
		k.labels["__name__"] = appName
	default:
		p.value += string(r)
	}
	return nil
}

// ParseKey's tagKeyParserState switch case
func (p *parser) tagKeyParserCase(r int32) {
	switch r {
	case '}':
		p.parserState = doneParserState
	case '=':
		p.parserState = tagValueParserState
		p.value = ""
	default:
		p.key += string(r)
	}
}

// ParseKey's tagValueParserState switch case
func (p *parser) tagValueParserCase(r int32, k *Key) error {
	switch r {
	case ',', '}':
		p.parserState = tagKeyParserState
		key := strings.TrimSpace(p.key)
		if !IsTagKeyReserved(key) {
			if err := ValidateTagKey(key); err != nil {
				return err
			}
		}
		k.labels[key] = strings.TrimSpace(p.value)
		p.key = ""
	default:
		p.value += string(r)
	}
	return nil
}

func (k *Key) SegmentKey() string {
	return k.Normalized()
}

func TreeKey(k string, depth int, unixTime int64) string {
	return k + ":" + strconv.Itoa(depth) + ":" + strconv.FormatInt(unixTime, 10)
}

func (k *Key) TreeKey(depth int, t time.Time) string {
	return TreeKey(k.Normalized(), depth, t.Unix())
}

var errKeyInvalid = errors.New("invalid key")

// ParseTreeKey retrieves tree time and depth level from the given key.
func ParseTreeKey(k string) (time.Time, int, error) {
	a := strings.Split(k, ":")
	if len(a) < 3 {
		return time.Time{}, 0, errKeyInvalid
	}
	level, err := strconv.Atoi(a[1])
	if err != nil {
		return time.Time{}, 0, err
	}
	v, err := strconv.Atoi(a[2])
	if err != nil {
		return time.Time{}, 0, err
	}
	return time.Unix(int64(v), 0), level, err
}

func (k *Key) DictKey() string {
	return k.labels["__name__"]
}

// FromTreeToDictKey returns app name from tree key k: given tree key
// "foo{}:0:1234567890", the call returns "foo".
//
// Before tags support, segment key form (i.e. app name + tags: foo{key=value})
// has been used to reference a dictionary (trie).
func FromTreeToDictKey(k string) string {
	return k[0:strings.IndexAny(k, "{")]
}

func (k *Key) Normalized() string {
	var sb strings.Builder

	sortedMap := sortedmap.New()
	for k, v := range k.labels {
		if k == "__name__" {
			sb.WriteString(v)
		} else {
			sortedMap.Put(k, v)
		}
	}

	sb.WriteString("{")
	for i, k := range sortedMap.Keys() {
		v := sortedMap.Get(k).(string)
		if i != 0 {
			sb.WriteString(",")
		}
		sb.WriteString(k)
		sb.WriteString("=")
		sb.WriteString(v)
	}
	sb.WriteString("}")

	return sb.String()
}

func (k *Key) AppName() string {
	return k.labels["__name__"]
}

func (k *Key) Labels() map[string]string {
	return k.labels
}

func (k *Key) Add(key, value string) {
	if value == "" {
		delete(k.labels, key)
	} else {
		k.labels[key] = value
	}
}

// Match reports whether the key matches the query.
func (k *Key) Clone() *Key {
	newMap := make(map[string]string)
	for k, v := range k.labels {
		newMap[k] = v
	}
	return &Key{labels: newMap}
}

func (k *Key) Match(q *Query) bool {
	if k.AppName() != q.AppName {
		return false
	}
	for _, m := range q.Matchers {
		var ok bool
		for labelKey, labelValue := range k.labels {
			if m.Key != labelKey {
				continue
			}
			if m.Match(labelValue) {
				if !m.IsNegation() {
					ok = true
					break
				}
			} else if m.IsNegation() {
				return false
			}
		}
		if !ok && !m.IsNegation() {
			return false
		}
	}
	return true
}
```

## File: `internal/flameql/parse.go`
```go
package flameql

import (
	"regexp"
	"sort"
	"strings"
)

// ParseQuery parses a string of $app_name<{<$tag_matchers>}> form.
func ParseQuery(s string) (*Query, error) {
	s = strings.TrimSpace(s)
	q := Query{q: s}

	for offset, c := range s {
		switch c {
		case '{':
			if offset == 0 {
				return nil, ErrAppNameIsRequired
			}
			if s[len(s)-1] != '}' {
				return nil, newErr(ErrInvalidQuerySyntax, "expected } at the end")
			}
			m, err := ParseMatchers(s[offset+1 : len(s)-1])
			if err != nil {
				return nil, err
			}
			q.AppName = s[:offset]
			q.Matchers = m
			return &q, nil
		default:
			if !IsAppNameRuneAllowed(c) {
				return nil, newErr(ErrInvalidAppName, s[:offset+1])
			}
		}
	}

	if len(s) == 0 {
		return nil, ErrAppNameIsRequired
	}

	q.AppName = s
	return &q, nil
}

// ParseMatchers parses a string of $tag_matcher<,$tag_matchers> form.
func ParseMatchers(s string) ([]*TagMatcher, error) {
	var matchers []*TagMatcher
	for _, t := range split(s) {
		if t == "" {
			continue
		}
		m, err := ParseMatcher(strings.TrimSpace(t))
		if err != nil {
			return nil, err
		}
		matchers = append(matchers, m)
	}
	if len(matchers) == 0 && len(s) != 0 {
		return nil, newErr(ErrInvalidMatchersSyntax, s)
	}
	sort.Sort(ByPriority(matchers))
	return matchers, nil
}

// ParseMatcher parses a string of $tag_key$op"$tag_value" form,
// where $op is one of the supported match operators.
func ParseMatcher(s string) (*TagMatcher, error) {
	var tm TagMatcher
	var offset int
	var c rune

loop:
	for offset, c = range s {
		r := len(s) - (offset + 1)
		switch c {
		case '=':
			switch {
			case r <= 2:
				return nil, newErr(ErrInvalidTagValueSyntax, s)
			case s[offset+1] == '"':
				tm.Op = OpEqual
			case s[offset+1] == '~':
				if r <= 3 {
					return nil, newErr(ErrInvalidTagValueSyntax, s)
				}
				tm.Op = OpEqualRegex
			default:
				// Just for more meaningful error message.
				if s[offset+2] != '"' {
					return nil, newErr(ErrInvalidTagValueSyntax, s)
				}
				return nil, newErr(ErrUnknownOp, s)
			}
			break loop
		case '!':
			if r <= 3 {
				return nil, newErr(ErrInvalidTagValueSyntax, s)
			}
			switch s[offset+1] {
			case '=':
				tm.Op = OpNotEqual
			case '~':
				tm.Op = OpNotEqualRegex
			default:
				return nil, newErr(ErrUnknownOp, s)
			}
			break loop
		default:
			if !IsTagKeyRuneAllowed(c) {
				return nil, newInvalidTagKeyRuneError(s, c)
			}
		}
	}

	k := s[:offset]
	if IsTagKeyReserved(k) {
		return nil, newErr(ErrTagKeyReserved, k)
	}

	var v string
	var ok bool
	switch tm.Op {
	default:
		return nil, newErr(ErrMatchOperatorIsRequired, s)
	case OpEqual:
		v, ok = unquote(s[offset+1:])
	case OpNotEqual, OpEqualRegex, OpNotEqualRegex:
		v, ok = unquote(s[offset+2:])
	}
	if !ok {
		return nil, newErr(ErrInvalidTagValueSyntax, v)
	}

	// Compile regex, if applicable.
	switch tm.Op {
	case OpEqualRegex, OpNotEqualRegex:
		r, err := regexp.Compile(v)
		if err != nil {
			return nil, newErr(err, v)
		}
		tm.R = r
	}

	tm.Key = k
	tm.Value = v
	return &tm, nil
}

func unquote(s string) (string, bool) {
	if s[0] != '"' || s[len(s)-1] != '"' {
		return s, false
	}
	return s[1 : len(s)-1], true
}

func split(s string) []string {
	var r []string
	var x int
	var y bool
	for i := 0; i < len(s); i++ {
		switch {
		case s[i] == ',' && !y:
			r = append(r, s[x:i])
			x = i + 1
		case s[i] == '"':
			if y && i > 0 && s[i-1] != '\\' {
				y = false
				continue
			}
			y = true
		}
	}
	return append(r, s[x:])
}
```

## File: `internal/sessionid/sessionid.go`
```go
package sessionid

import (
	crand "crypto/rand"
	"encoding/binary"
	"encoding/hex"
	"hash/fnv"
	"math/rand"
	"net/http"
	"os"
	"sync"

	"github.com/pyroscope-io/pyroscope-lambda-extension/internal/flameql"
)

const LabelName = "__session_id__"

func InjectToRequest(sessionID string, r *http.Request) {
	parsed, err := flameql.ParseKey(r.URL.Query().Get("name"))
	if err != nil {
		// This is an invalid request, but we defer to the backend.
		return
	}
	if _, ok := parsed.Labels()[LabelName]; !ok {
		parsed.Add(LabelName, sessionID)
		q := r.URL.Query()
		q.Set("name", parsed.Normalized())
		r.URL.RawQuery = q.Encode()
	}
}

type ID uint64

func (s ID) String() string {
	var b [8]byte
	binary.LittleEndian.PutUint64(b[:], uint64(s))
	return hex.EncodeToString(b[:])
}

func New() ID { return globalSessionIDGenerator.newSessionID() }

var globalSessionIDGenerator = newSessionIDGenerator()

type sessionIDGenerator struct {
	sync.Mutex
	src *rand.Rand
}

func (gen *sessionIDGenerator) newSessionID() ID {
	var b [8]byte
	gen.Lock()
	_, _ = gen.src.Read(b[:])
	gen.Unlock()
	return ID(binary.LittleEndian.Uint64(b[:]))
}

func newSessionIDGenerator() *sessionIDGenerator {
	s, ok := sessionIDHostSeed()
	if !ok {
		s = sessionIDRandSeed()
	}
	return &sessionIDGenerator{src: rand.New(rand.NewSource(s))}
}

func sessionIDRandSeed() int64 {
	var rndSeed int64
	_ = binary.Read(crand.Reader, binary.LittleEndian, &rndSeed)
	return rndSeed
}

var hostname = os.Hostname

func sessionIDHostSeed() (int64, bool) {
	v, err := hostname()
	if err != nil {
		return 0, false
	}
	h := fnv.New64a()
	_, _ = h.Write([]byte(v))
	return int64(h.Sum64()), true
}
```

## File: `internal/sortedmap/sortedmap.go`
```go
package sortedmap

import (
	"sort"
)

type SortedMap struct {
	data map[string]interface{}
	keys []string
}

func (s *SortedMap) Put(k string, v interface{}) {
	s.data[k] = v
	i := sort.Search(len(s.keys), func(i int) bool { return s.keys[i] >= k })
	s.keys = append(s.keys, "")
	copy(s.keys[i+1:], s.keys[i:])
	s.keys[i] = k
}

func (s *SortedMap) Get(k string) (v interface{}) {
	return s.data[k]
}

func (s *SortedMap) Keys() []string {
	return s.keys
}

func New() *SortedMap {
	return &SortedMap{
		data: make(map[string]interface{}),
		keys: make([]string, 0),
	}
}
```

## File: `relay/client.go`
```go
package relay

import (
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"path"
	"time"

	"github.com/sirupsen/logrus"

	"github.com/pyroscope-io/pyroscope-lambda-extension/internal/sessionid"
)

var (
	ErrMakingRequest = errors.New("failed to make request")
	ErrNotOkResponse = errors.New("response not ok")
)

type RemoteClientCfg struct {
	// Address refers to the remote address the request will be made to
	Address             string
	AuthToken           string
	BasicAuthUser       string
	BasicAuthPassword   string
	TenantID            string
	HTTPHeadersJSON     string
	Timeout             time.Duration
	MaxIdleConnsPerHost int
	SessionID           string
}

type RemoteClient struct {
	config    *RemoteClientCfg
	client    *http.Client
	headers   map[string]string
	log       *logrus.Entry
	sessionID string
}

func NewRemoteClient(log *logrus.Entry, config *RemoteClientCfg) *RemoteClient {
	timeout := config.Timeout
	if timeout == 0 {
		timeout = time.Second * 10
	}
	if config.MaxIdleConnsPerHost == 0 {
		config.MaxIdleConnsPerHost = 5
	}
	headers := make(map[string]string)
	if config.HTTPHeadersJSON != "" {
		err := json.Unmarshal([]byte(config.HTTPHeadersJSON), &headers)
		if err != nil {
			log.Error(fmt.Errorf("failed to parse headers json %w", err))
		}
	}
	return &RemoteClient{
		log:       log,
		config:    config,
		sessionID: config.SessionID,
		client: &http.Client{
			Timeout: timeout,
			Transport: &http.Transport{
				MaxIdleConnsPerHost: config.MaxIdleConnsPerHost,
			},
		},
	}
}

// Send relays the request to the remote server
func (r *RemoteClient) Send(req *http.Request) error {
	if req.Body != nil {
		defer req.Body.Close()
	}
	r.enhanceWithAuthToken(req)
	if r.config.TenantID != "" {
		req.Header.Set("X-Scope-OrgID", r.config.TenantID)
	}
	for k, v := range r.headers {
		req.Header.Set(k, v)
	}

	host := r.config.Address

	u, _ := url.Parse(host)

	req.RequestURI = ""
	req.URL.Host = u.Host
	req.URL.Scheme = u.Scheme
	req.URL.User = u.User
	req.URL.Path = path.Join(u.Path, req.URL.Path)
	req.Header.Set("X-Forwarded-Host", req.Header.Get("Host"))
	req.Host = u.Host
	sessionid.InjectToRequest(r.sessionID, req)
	// TODO(eh-am): check it's a request to /ingest?
	r.log.Debugf("Making request to %s", req.URL.String())
	res, err := r.client.Do(req)
	if err != nil {
		return fmt.Errorf("%w: %v", ErrMakingRequest, err)
	}
	defer res.Body.Close()

	if !(res.StatusCode >= 200 && res.StatusCode < 300) {
		respBody, _ := io.ReadAll(res.Body)
		return fmt.Errorf("%w: %v", ErrNotOkResponse, fmt.Errorf("status code: '%d'. body: '%s'", res.StatusCode, respBody))
	}

	return nil
}

// enhanceWithAuthToken adds an Authorization header if an AuthToken is supplied
// note that if no authToken is set, it's possible that the Authorization header
// from the original request is kept
func (r *RemoteClient) enhanceWithAuthToken(req *http.Request) {
	token := r.config.AuthToken

	if token != "" {
		req.Header.Set("Authorization", "Bearer "+token)
	} else if r.config.BasicAuthUser != "" && r.config.BasicAuthPassword != "" {
		req.SetBasicAuth(r.config.BasicAuthUser, r.config.BasicAuthPassword)
	}
}
```

## File: `relay/client_test.go`
```go
package relay_test

import (
	"bytes"
	"net/http"
	"net/http/httptest"
	"net/url"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"

	"github.com/pyroscope-io/pyroscope-lambda-extension/internal/flameql"
	"github.com/pyroscope-io/pyroscope-lambda-extension/internal/sessionid"
	"github.com/pyroscope-io/pyroscope-lambda-extension/relay"
)

func TestRemoteClient(t *testing.T) {
	logger := noopLogger()

	endpoint := "/ingest?aggregationType=sum&from=1655819920&name=simple.golang.app-new%7B%7D&sampleRate=100&spyName=gospy&units=samples&until=1655819927"
	u, err := url.Parse(endpoint)
	assert.NoError(t, err)
	profile := readTestdataFile(t, "testdata/profile.pprof")
	authToken := "123"

	rcc := &relay.RemoteClientCfg{
		AuthToken: "123",
		SessionID: sessionid.New().String(),
	}

	remoteServer := httptest.NewServer(http.HandlerFunc(
		func(w http.ResponseWriter, r *http.Request) {
			assert.Equal(t, u.Path, r.URL.Path, "path is mirrored")

			q := r.URL.Query()
			parsed, err := flameql.ParseKey(q.Get("name"))
			require.NoError(t, err)
			require.Equal(t,
				rcc.SessionID,
				parsed.Labels()[sessionid.LabelName],
				"requests has __session_id__ label")

			delete(parsed.Labels(), sessionid.LabelName)
			q.Set("name", parsed.Normalized())
			assert.Equal(t, u.RawQuery, q.Encode(), "query params are mirrored")

			body := &bytes.Buffer{}
			body.ReadFrom(r.Body)
			assert.Equal(t, profile, body.Bytes(), "body is mirrored")

			assert.Equal(t, "Bearer "+authToken, r.Header.Get("Authorization"), "auth header is mirrored")
		}),
	)

	rcc.Address = remoteServer.URL
	remoteClient := relay.NewRemoteClient(logger, rcc)

	req, err := http.NewRequest(http.MethodPost, endpoint, bytes.NewReader(profile))
	assert.NoError(t, err)

	err = remoteClient.Send(req)
	assert.NoError(t, err)
}

func TestRemoteClientNon2xxError(t *testing.T) {
	logger := noopLogger()

	endpoint := "/ingest?aggregationType=sum&from=1655819920&name=simple.golang.app-new%7B%7D&sampleRate=100&spyName=gospy&units=samples&until=1655819927"

	remoteServer := httptest.NewServer(http.HandlerFunc(
		func(w http.ResponseWriter, r *http.Request) {
			w.WriteHeader(500)
		}),
	)

	remoteClient := relay.NewRemoteClient(logger, &relay.RemoteClientCfg{Address: remoteServer.URL})

	req, err := http.NewRequest(http.MethodPost, endpoint, nil)
	assert.NoError(t, err)

	err = remoteClient.Send(req)
	assert.ErrorIs(t, err, relay.ErrNotOkResponse)
}

func TestRemoteClientIncompleteRequestError(t *testing.T) {
	logger := noopLogger()

	invalidUrl := ""
	remoteClient := relay.NewRemoteClient(logger, &relay.RemoteClientCfg{Address: invalidUrl})

	req, err := http.NewRequest(http.MethodPost, "/", nil)
	assert.NoError(t, err)

	// There should an error
	err = remoteClient.Send(req)
	assert.ErrorIs(t, err, relay.ErrMakingRequest)
}

func TestRemoteClientTimeout(t *testing.T) {
	logger := noopLogger()

	endpoint := "/ingest"

	remoteServer := httptest.NewServer(http.HandlerFunc(
		func(w http.ResponseWriter, r *http.Request) {
			time.Sleep(time.Second * 999)
			w.WriteHeader(200)
		}),
	)

	remoteClient := relay.NewRemoteClient(logger, &relay.RemoteClientCfg{
		Address: remoteServer.URL,
		Timeout: time.Millisecond * 50,
	})

	req, err := http.NewRequest(http.MethodPost, endpoint, nil)
	assert.NoError(t, err)

	err = remoteClient.Send(req)
	assert.ErrorIs(t, err, relay.ErrMakingRequest)
}
```

## File: `relay/controller.go`
```go
package relay

import (
	"bytes"
	"context"
	"io"
	"net/http"

	"github.com/sirupsen/logrus"
)

type Controller struct {
	log   *logrus.Entry
	queue *RemoteQueue
}

func NewController(log *logrus.Entry, queue *RemoteQueue) *Controller {
	log = log.WithField("comp", "controller")

	return &Controller{
		log:   log,
		queue: queue,
	}
}

func (c *Controller) RelayRequest(w http.ResponseWriter, r *http.Request) {
	// clones the request
	r2 := r.Clone(context.Background())

	body, err := io.ReadAll(r.Body)
	if err != nil {
		c.log.Errorf("Failed to read a request for relay. Error: %+v", err)
		w.WriteHeader(500)
		return
	}
	r2.Body = io.NopCloser(bytes.NewReader(body))

	c.queue.Send(r2)
	w.WriteHeader(200)
}
```

## File: `relay/orchestrator.go`
```go
package relay

// Orchestrator orchestrates the start/shutdown of underlying components
import (
	"context"

	"github.com/sirupsen/logrus"
	"golang.org/x/sync/errgroup"
)

type Orchestrator struct {
	log *logrus.Entry

	// TODO(eh-am): take a generic startstopper
	queue        *RemoteQueue
	server       *Server
	selfProfiler StartStopper
}

type StartStopper interface {
	Start() error
	Stop(context.Context) error
}

func NewOrchestrator(log *logrus.Entry, queue *RemoteQueue, server *Server, selfProfiler StartStopper) *Orchestrator {
	log = log.WithField("comp", "orchestrator")

	return &Orchestrator{
		log:          log,
		queue:        queue,
		server:       server,
		selfProfiler: selfProfiler,
	}
}

func (o *Orchestrator) Start() error {
	o.log.Debug("Starting queue")
	err := o.queue.Start()
	if err != nil {
		return err
	}

	o.log.Debug("Starting self profiler")
	err = o.selfProfiler.Start()
	if err != nil {
		o.log.Error("Error starting self profiler", err)
	}

	o.log.Debug("Starting Server")
	return o.server.Start()
}

func (o *Orchestrator) Shutdown() error {
	o.log.Debug("Shutting down")

	ctx := context.Background()
	g, _ := errgroup.WithContext(context.Background())

	// TODO(eh-am): validate this can indeed be done concurrently
	g.Go(func() error {
		return o.selfProfiler.Stop(ctx)
	})
	g.Go(func() error {
		return o.server.Stop(ctx)
	})
	g.Go(func() error {
		return o.queue.Stop(ctx)
	})

	return g.Wait()
}
```

## File: `relay/remotequeue.go`
```go
package relay

import (
	"context"
	"fmt"
	"net/http"
	"sync"

	"github.com/sirupsen/logrus"
)

type RemoteQueueCfg struct {
	NumWorkers int
}

type RemoteQueue struct {
	config     *RemoteQueueCfg
	jobs       chan *http.Request
	done       chan struct{}
	wg         sync.WaitGroup
	flushWG    sync.WaitGroup
	flushGuard sync.Mutex
	log        *logrus.Entry
	relayer    Relayer
}

type Relayer interface {
	Send(req *http.Request) error
}

func NewRemoteQueue(log *logrus.Entry, config *RemoteQueueCfg, relayer Relayer) *RemoteQueue {
	// Setup defaults
	if config.NumWorkers == 0 {
		// TODO(eh-am): figure out a good default value?
		config.NumWorkers = 5
	}

	return &RemoteQueue{
		config: config,
		log:    log,
		// TODO(eh-am): figure out a good default value?
		jobs:    make(chan *http.Request, 20),
		done:    make(chan struct{}),
		relayer: relayer,
	}
}

func (r *RemoteQueue) Start() error {
	for i := 0; i < r.config.NumWorkers; i++ {
		i := i
		go r.handleJobs(i)
	}
	return nil
}

// Stop signals for the workers to not handle any more jobs
// Then waits for existing jobs to finish
// Currently context is not used for anything
func (r *RemoteQueue) Stop(_ context.Context) error {
	close(r.done)

	r.log.Debugf("Waiting for %d pending jobs to finish...", len(r.jobs))
	r.wg.Wait()
	r.log.Debug("Requests finished.")

	return nil
}

// Send adds a request to the queue to be processed later
func (r *RemoteQueue) Send(req *http.Request) error {
	r.flushGuard.Lock() // block if we are currently trying to Flush
	defer r.flushGuard.Unlock()
	r.flushWG.Add(1)
	select {
	case r.jobs <- req:
	default:
		r.flushWG.Done()
		r.log.Error("Request queue is full, dropping a profile job.")
		return fmt.Errorf("request queue is full")
	}

	return nil
}
func (r *RemoteQueue) Flush() {
	r.log.Debugf("Flush: Waiting for enqueued jobs to finish")
	r.flushGuard.Lock()
	defer r.flushGuard.Unlock()
	r.flushWG.Wait()
	r.log.Debugf("Flush: Done")
}

func (r *RemoteQueue) handleJobs(workerID int) {
	for {
		select {
		case <-r.done:
			r.log.Tracef("Worker #%d closing. Not taking any more jobs", workerID)
			return
		case job := <-r.jobs:
			log := r.log.WithField("path", job.URL.Path)

			log.Trace("Relaying request to remote")
			r.wg.Add(1)
			err := r.relayer.Send(job)
			r.wg.Done()
			r.flushWG.Done()

			if err != nil {
				log.Error("Failed to relay request: ", err)
			} else {
				log.Trace("Successfully relayed request to remote", job.URL.RawQuery)
			}
		}
	}
}
```

## File: `relay/remotequeue_flush_test.go`
```go
package relay_test

import (
	"github.com/pyroscope-io/pyroscope-lambda-extension/relay"
	"github.com/sirupsen/logrus"
	"net/http"
	"sync"
	"testing"
	"time"
)

type asyncJob struct {
	name string
	m    sync.Mutex
	t    *testing.T
}

func newAsyncJob(t *testing.T, name string, f func()) *asyncJob {
	res := &asyncJob{t: t, name: name}
	res.m.Lock()
	go func() {
		f()
		res.m.Unlock()
	}()
	return res
}

func (j *asyncJob) assertNotFinished() {
	locked := j.m.TryLock()
	if locked {
		j.t.Fatalf("should be still working... " + j.name)
	}
}

func (j *asyncJob) assertFinished() {
	j.m.Lock()
}

type flushTestHelper struct {
	t         *testing.T
	log       *logrus.Entry
	responses chan struct{}
	requests  chan struct{}
	req       *http.Request
	queue     *relay.RemoteQueue
}

func newFlushMockRelay(t *testing.T) *flushTestHelper {
	req, _ := http.NewRequest(http.MethodPost, "/", nil)
	log := logrus.WithFields(logrus.Fields{"svc": "flush-test"})
	res := &flushTestHelper{
		t:         t,
		log:       log,
		responses: make(chan struct{}, 128),
		requests:  make(chan struct{}, 128),
		req:       req,
	}
	res.queue = relay.NewRemoteQueue(log, &relay.RemoteQueueCfg{
		NumWorkers: 2,
	}, res)
	logrus.SetLevel(logrus.DebugLevel)

	return res
}

func (h *flushTestHelper) Send(_ *http.Request) error {
	//h.log.Debug("flushTestHelper.send 1")
	h.requests <- struct{}{}
	//h.log.Debug("flushTestHelper.send 2")
	<-h.responses
	//h.log.Debug("flushTestHelper.send 3")
	return nil
}

func (h *flushTestHelper) respond() {
	h.responses <- struct{}{}
}

func (h *flushTestHelper) flushAsync() *asyncJob {
	return newAsyncJob(h.t, "flush", func() {
		h.queue.Flush()
	})
}

func (h *flushTestHelper) sendAsync() *asyncJob {
	return newAsyncJob(h.t, "send", func() {
		_ = h.queue.Send(h.req)
	})
}
func (h *flushTestHelper) send() {
	_ = h.queue.Send(h.req)
}

func (h *flushTestHelper) step() {
	time.Sleep(100 * time.Millisecond)
}

func (h *flushTestHelper) assertRequestsProcessed(n int) {
	if n != len(h.requests) {
		h.t.Fatalf("expected %d got %d", n, len(h.responses))
	}
}

func TestFlushWaitsForAllEnqueuedRequests(t *testing.T) {
	n := 3
	h := newFlushMockRelay(t)
	_ = h.queue.Start()
	for i := 0; i < n; i++ {
		h.send()
	}
	f := h.flushAsync()
	for i := 0; i < n; i++ {
		h.step()
		f.assertNotFinished()
		h.respond()
	}
	f.assertFinished()
	h.assertRequestsProcessed(n)
}

func TestFlushWaitsForAllEnqueuedRequestsWhenQueueIsFullAndSomeAreDropped(t *testing.T) {
	n := 30
	h := newFlushMockRelay(t)
	//queueSize := cap(h.queue.jobs)
	queueSize := 20
	for i := 0; i < n; i++ { //send 30, 10 are dropped
		h.send()
	}
	_ = h.queue.Start()
	f := h.flushAsync()
	for i := 0; i < queueSize; i++ { //20 are processed
		h.step()
		f.assertNotFinished()
		h.respond()
	}
	f.assertFinished()
	h.assertRequestsProcessed(queueSize)
}

func TestFlushWithQueueEmpty(t *testing.T) {
	h := newFlushMockRelay(t)
	_ = h.queue.Start()
	f := h.flushAsync()
	f.assertFinished()
	h.assertRequestsProcessed(0)
}

func TestFlushSendEventDuringFlushBlocks(t *testing.T) {
	n := 3
	h := newFlushMockRelay(t)
	_ = h.queue.Start()
	for i := 0; i < n; i++ {
		h.send()
	}
	f := h.flushAsync()
	h.step()
	s := h.sendAsync()
	for i := 0; i < n; i++ {
		h.step()
		f.assertNotFinished()
		s.assertNotFinished()
	}
	for i := 0; i < n; i++ {
		h.respond()
	}
	f.assertFinished()
	s.assertFinished()

}
```

## File: `relay/remotequeue_test.go`
```go
package relay_test

import (
	"context"
	"github.com/pyroscope-io/pyroscope-lambda-extension/relay"
	"github.com/stretchr/testify/assert"
	"net/http"
	"sync"
	"testing"
)

type mockRelayer struct {
	fn func(req *http.Request) error
}

func (m mockRelayer) Send(req *http.Request) error {
	return m.fn(req)
}

func TestRemoteQueue(t *testing.T) {
	logger := noopLogger()

	var wg sync.WaitGroup

	req, err := http.NewRequest(http.MethodPost, "/", nil)
	assert.NoError(t, err)

	relayer := mockRelayer{
		fn: func(r *http.Request) error {
			defer wg.Done()
			assert.Equal(t, req, r)
			return nil
		},
	}

	queue := relay.NewRemoteQueue(logger, &relay.RemoteQueueCfg{}, relayer)
	queue.Start()

	wg.Add(1)
	queue.Send(req)
	wg.Wait()
}

func TestRemoteQueueShutdown(t *testing.T) {
	logger := noopLogger()

	req, err := http.NewRequest(http.MethodPost, "/", nil)
	assert.NoError(t, err)

	reqBeingProcessed := make(chan struct{})
	reqWaitingToBeRun := make(chan struct{})

	shutdown := make(chan struct{})
	startShutdown := make(chan struct{})

	jobProcessed := false
	relayer := mockRelayer{
		fn: func(r *http.Request) error {
			reqBeingProcessed <- struct{}{}

			// Let's block here until shutdown starts
			// This is to simulate a long running process (eg a busy server)
			<-reqWaitingToBeRun

			jobProcessed = true
			return nil
		},
	}

	queue := relay.NewRemoteQueue(logger, &relay.RemoteQueueCfg{}, relayer)
	queue.Start()
	// Send data to the queue
	queue.Send(req)

	// Wait for request to start to be processed
	<-reqBeingProcessed

	go func() {
		// Signal that this goroutine is running
		startShutdown <- struct{}{}

		// This is a blocking operation
		// We are waiting for the request to be finished
		err = queue.Stop(context.TODO())
		assert.NoError(t, err)

		// Tell that we finished the shutdown
		shutdown <- struct{}{}
	}()

	<-startShutdown

	// Tell the inflight job to continue running
	reqWaitingToBeRun <- struct{}{}

	// Wait for shutdown
	<-shutdown
	assert.True(t, jobProcessed)
}
```

## File: `relay/server.go`
```go
package relay

import (
	"context"
	"net/http"

	"github.com/sirupsen/logrus"
)

type ServerCfg struct {
	ServerAddress string
}

type Server struct {
	config *ServerCfg
	log    *logrus.Entry
	server *http.Server
}

func NewServer(logger *logrus.Entry, config *ServerCfg, handlerFunc http.HandlerFunc) *Server {
	mux := http.NewServeMux()
	svr := &http.Server{
		Handler: mux,
		Addr:    config.ServerAddress,
	}

	server := &Server{
		config: config,
		log:    logger,
		server: svr,
	}

	mux.Handle("/", handlerFunc)
	return server
}

// Start starts serving requests, this is a blocking operation
func (s *Server) Start() error {
	s.log.Debugf("Serving on %s", s.config.ServerAddress)
	err := s.server.ListenAndServe()
	if err != http.ErrServerClosed {
		return err
	}

	return nil
}

func (s *Server) Stop(ctx context.Context) error {
	return s.server.Shutdown(ctx)
}
```

## File: `relay/utils_test.go`
```go
package relay_test

import (
	"io"
	"os"
	"testing"

	"github.com/sirupsen/logrus"
	"github.com/stretchr/testify/assert"
)

func noopLogger() *logrus.Entry {
	logger := logrus.New()
	logger.SetOutput(io.Discard)

	return logger.WithFields(logrus.Fields{})
}

func readTestdataFile(t *testing.T, name string) []byte {
	f, err := os.ReadFile(name)
	assert.NoError(t, err)
	return f
}
```

## File: `scripts/pinned-tools.sh`
```bash
#!/bin/bash

# shellcheck disable=SC2005,SC2086
echo "$(go list -m -f '{{.Dir}}' $1)"

```

## File: `scripts/publish.ts`
```typescript
import yargs from "https://deno.land/x/yargs@v17.5.1-deno/deno.ts";
import * as log from "https://deno.land/std@0.146.0/log/mod.ts";

type Arch = "x86_64" | "arm64";
// Not all regions support multi architecture
// Best way I found to find them is to access
// https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/create/layer
// per region
const regions: { region: string; archs: Arch[] }[] = [
  { region: "eu-north-1", archs: [] },
  { region: "ap-south-1", archs: ["x86_64", "arm64"] },
  { region: "eu-west-3", archs: [] },
  { region: "eu-west-2", archs: ["x86_64", "arm64"] },
  { region: "eu-west-1", archs: ["x86_64", "arm64"] },
  { region: "ap-northeast-3", archs: [] },
  { region: "ap-northeast-2", archs: [] },
  { region: "ap-northeast-1", archs: ["x86_64", "arm64"] },
  { region: "sa-east-1", archs: [] },
  { region: "ca-central-1", archs: [] },
  { region: "ap-southeast-1", archs: ["x86_64", "arm64"] },
  { region: "ap-southeast-2", archs: ["x86_64", "arm64"] },
  { region: "eu-central-1", archs: ["x86_64", "arm64"] },
  { region: "us-east-1", archs: ["x86_64", "arm64"] },
  { region: "us-east-2", archs: ["x86_64", "arm64"] },
  { region: "us-west-1", archs: [] },
  { region: "us-west-2", archs: ["x86_64", "arm64"] },
];

const y = yargs(Deno.args)
  .options({
    "dry-run": {
      describe: "Run the program without actually invoking commands",
      default: true,
      type: "boolean",
    },
    "name": {
      describe: "The name of the extensoin",
      demandOption: true,
    },
    "table-file": {
      describe: "file with the release info",
      default: "release.tmp.md",
    },
    "log-level": {
      describe: "DEBUG | INFO | WARNING | ERROR | CRITICAL",
      demandOption: true,
      default: "INFO",
      type: "string",
    },
  })
  .parse();

await log.setup({
  handlers: {
    console: new log.handlers.ConsoleHandler(y.logLevel),
  },

  loggers: {
    // configure default logger available via short-hand methods above.
    default: {
      level: y.logLevel,
      handlers: ["console"],
    },

    tasks: {
      level: y.logLevel,
      handlers: ["console"],
    },
  },
});

function getLayerName(name: string, arch: Arch) {
  switch (arch) {
    case "x86_64": {
      return `${name}-x86_64`;
    }
    case "arm64": {
      return `${name}-arm64`;
    }
    default: {
      throw new Error(`Unsupported arch: '${arch}'`);
    }
  }
}

async function runCommand(cmd: string[], { cwd }: { cwd?: string } = {}) {
  // Since this script is used internally only
  // we don't have to be so strict
  if (y.dryRun === true) {
    return Promise.resolve("");
  } else {
    const p = Deno.run({ cmd, stdout: "piped", cwd: cwd });

    const status = await p.status();
    if (!status.success) {
      Deno.exit(1);
    }
    const output = await p.output();

    return new TextDecoder().decode(output);
  }
}

async function publishCmd(
  layerName: string,
  region: string,
  cwd: string,
  arch?: string,
): Promise<{ version: string; layernArn: string; fullLayerName: string }> {
  if (y.dryRun) {
    return {
      version: "999",
      layernArn: "arn:aws:lambda:us-east-1:myacc:layer:pyroscope-test-x86_64",
      fullLayerName:
        "arn:aws:lambda:us-east-1:myacc:layer:pyroscope-test-x86_64:999",
    };
  }

  let cmd = [
    "aws",
    "lambda",
    "publish-layer-version",
    `--layer-name=${layerName}`,
    `--region=${region}`,
    `--zip-file=fileb://extension.zip`,
  ];

  if (arch) {
    cmd = cmd.concat([`--compatible-architectures=${arch}`]);
  }

  const output = await runCommand(cmd, { cwd });

  const parsed = JSON.parse(output);
  return {
    // eg: 1
    version: parsed.Version,
    // eg: 'arn:aws:lambda:us-east-1:myacc:layer:pyroscope-test-x86_64'
    layernArn: parsed.LayerArn,
    // eg: 'arn:aws:lambda:us-east-1:myacc:layer:pyroscope-test-x86_64:999'
    fullLayerName: parsed.LayerVersionArn,
  };
}

async function publishAmd(
  name: string,
  region: typeof regions[number]["region"],
  withArch?: boolean,
): Promise<{
  layerName: string;
  version: string;
  layernArn: string;
  fullLayerName: string;
}> {
  const cwd = "bin/x86_64";
  const layerName = getLayerName(name, "x86_64");
  if (y.dryRun) {
    return Promise.resolve({
      layerName,
      version: "999",
      layernArn: `arn:aws:lambda:${region}:myacc:layer:${layerName}`,
      fullLayerName: `arn:aws:lambda:${region}:myacc:layer:${layerName}:999`,
    });
  }

  // For zones that only support x86_64, we don't pass an architecture
  return {
    ...(await publishCmd(
      layerName,
      region,
      cwd,
      withArch ? "x86_64" : undefined,
    )),
    layerName,
  };
}

async function publishArm(
  name: string,
  region: typeof regions[number]["region"],
): Promise<{
  layerName: string;
  version: string;
  layernArn: string;
  fullLayerName: string;
}> {
  const cwd = "bin/arm64";
  const layerName = getLayerName(name, "arm64");
  if (y.dryRun) {
    return Promise.resolve({
      layerName,
      version: "999",
      layernArn: `arn:aws:lambda:${region}:myacc:layer:${layerName}`,
      fullLayerName: `arn:aws:lambda:${region}:myacc:layer:${layerName}:999`,
    });
  }

  return { ...(await publishCmd(layerName, region, cwd, "arm64")), layerName };
}

async function makePublic(
  { layerName, region, version }: {
    layerName: string;
    region: string;
    version: string;
  },
) {
  if (y.dryRun) {
    return Promise.resolve("");
  }
  const statementId = [layerName, region, version].join("-");
  const output = await runCommand([
    "aws",
    "lambda",
    "add-layer-version-permission",
    `--region=${region}`,
    `--layer-name=${layerName}`,
    `--statement-id=${statementId}`,
    `--version-number=${version}`,
    `--principal=*`,
    `--action=lambda:GetLayerVersion`,
  ]);

  const parsed = JSON.parse(output);
  return {
    // eg: 1
    version: parsed.Version,
    // eg: 'arn:aws:lambda:us-east-1:myacc:layer:pyroscope-test-x86_64'
    layernArn: parsed.layernArn,
    // eg: 'arn:aws:lambda:us-east-1:myacc:layer:pyroscope-test-x86_64:999'
    fullLayerName: parsed.LayerVersionArn,
  };
}

export async function run() {
  log.info("Publishing extension...");

  const all = (await Promise.all(regions.map(async (r) => {
    log.debug(r);

    // Since there's only a single architecture in this region
    // We don't ask to specificy a specific arch
    if (!r.archs.length) {
      log.debug("Region has no arch, defaulting to x86_64");
      const amd = await publishAmd(y.name, r.region, false);
      return [{ ...amd, region: r.region, arch: "x86_64" }];
    }

    return await Promise.all(r.archs.map(async (arch) => {
      switch (arch) {
        case "x86_64": {
          log.debug("Publishing x86_64");
          return {
            ...(await publishAmd(y.name, r.region, true)),
            region: r.region,
            arch,
          };
        }
        case "arm64": {
          log.debug("Publishing arm64");
          return {
            ...(await publishArm(y.name, r.region)),
            region: r.region,
            arch,
          };
        }
        default: {
          throw new Error(`Invalid arch ${arch}`);
        }
      }
    }));
  }))).flat();

  log.info("Making extensions public...");
  Promise.all(
    all.map(async ({ layerName, version, region }) => {
      log.debug("Making it public");
      log.debug({ layerName, version, region });
      const output = await makePublic({ layerName, version, region });
      log.debug("Done.");
      log.debug({ layerName, version, region });

      return;
    }),
  );

  return all.map(({ region, arch, fullLayerName }) => {
    return {
      region,
      arch,
      fullLayerName,
    };
  });
}

export function generateReleaseTable(published: {
  region: string;
  arch: string;
  fullLayerName: string;
}[]): string {
  return `
| region                   | arch | layer name |
|--------------------------|------|------------|\n` +
    published.map((a) => {
      return `|\`${a.region}\`|\`${a.arch}\`|\`${a.fullLayerName}\`|`;
    }).sort().join("\n");
}

// am I being executed or imported?
if (import.meta.main) {
  const output = await run();

  log.info("Generating CHANGELOG...");
  const releaseTable = generateReleaseTable(output);
  if (y.dryRun) {
    console.log(releaseTable);
  } else {
    log.debug(releaseTable);
    await Deno.writeTextFile(y.tableFile, releaseTable);
  }
}
```

## File: `scripts/replace-version.sh`
```bash
#!/usr/bin/env bash

set -euo pipefail

# Replace hello-world/template.yml with the latest version

# Query latest lambda
latestFullLayer=$(aws lambda list-layer-versions --layer-name pyroscope-extension-test --region us-east-1 --query 'max_by(LayerVersions, &Version).LayerVersionArn' --output=text)

latestLayer=$(echo "$latestFullLayer" | awk -F':' 'BEGIN { OFS = FS }; NF { NF -= 1 }; 1')
latestVersion=$(echo "$latestFullLayer" | awk -F: '{print $NF}')

# Replace the existing layer with the new one
# TODO(eh-am): fail if there's no match (eg the layer name has changed)
sed -i .bak -e "s@$latestLayer.*@$latestLayer:$latestVersion@g" hello-world/template.yml
```

## File: `selfprofiler/selfprofiler.go`
```go
package selfprofiler

import (
	"context"

	"github.com/grafana/pyroscope-go"
	"github.com/sirupsen/logrus"
)

type SelfProfiler struct {
	ps         *pyroscope.Profiler
	log        *logrus.Entry
	enabled    bool
	remoteAddr string
	authToken  string
}

func New(log *logrus.Entry, enabled bool, remoteAddr string, authToken string) *SelfProfiler {
	log = log.WithField("comp", "self-profiler")
	return &SelfProfiler{log: log, enabled: enabled, remoteAddr: remoteAddr, authToken: authToken}
}

// Start starts the self profiler
// It should never return an error
// TODO(eh-am): refactor this
func (s *SelfProfiler) Start() error {
	if !s.enabled {
		return nil
	}

	ps, err := pyroscope.Start(pyroscope.Config{
		ApplicationName: "pyroscope.lambda.extension",
		ServerAddress:   s.remoteAddr,
		Logger:          s.log,
		AuthToken:       s.authToken,
	})
	s.ps = ps

	if err != nil {
		s.log.Error(err)
	}

	return nil
}

func (s *SelfProfiler) Stop(context.Context) error {
	if s.ps != nil {
		s.log.Debug("Flushing self profiler data")
		return s.ps.Stop()
	}
	return nil
}
```

## File: `tools/tools.go`
```go
//go:build tools
// +build tools

// Package tools is used to describe various tools we use.
// Think of it as "dev-dependencies" in ruby or node projects
// See: https://marcofranssen.nl/manage-go-tools-via-go-modules/
// See Makefile for an example of how it's used
package tools

import (
	_ "github.com/davecgh/go-spew/spew"
	_ "github.com/mgechev/revive"
	_ "honnef.co/go/tools/cmd/staticcheck"
)
```

