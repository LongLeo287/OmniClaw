---
id: github.com-thanos-io-objstore-93e3cc4b-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:27.200973
---

# KNOWLEDGE EXTRACT: github.com_thanos-io_objstore_93e3cc4b
> **Extracted on:** 2026-04-01 16:55:23
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525413/github.com_thanos-io_objstore_93e3cc4b

---

## File: `.errcheck_excludes.txt`
```
(github.com/go-kit/log.Logger).Log
fmt.Fprintln
fmt.Fprint
```

## File: `.gitignore`
```
.envrc
.bin

/vendor/

/.idea
/*.iml

tmp/bin
examples/tmp/

# Ignore the MacOS Trash (DS-Store)
.DS_Store
```

## File: `.go-version`
```
1.24.x
```

## File: `.golangci.yml`
```yaml
# This file contains all available configuration options
# with their default values.

# options for analysis running
run:
  # timeout for analysis, e.g. 30s, 5m, default is 1m
  deadline: 5m

  # exit code when at least one issue was found, default is 1
  issues-exit-code: 1

# output configuration options
output:
  # colored-line-number|line-number|json|tab|checkstyle, default is "colored-line-number"
  formats: 
    - format: colored-line-number
      path: stdout

  # print lines of code with issue, default is true
  print-issued-lines: true

  # print linter name in the end of issue text, default is true
  print-linter-name: true

linters:
  enable:
    # Sorted alphabetically.
    - copyloopvar
    - errcheck
    - goconst
    - godot
    - gofmt
    - goimports
    - gosimple
    - govet
    - ineffassign
    - misspell
    - staticcheck
    - typecheck
    - unparam
    - unused
    - promlinter

linters-settings:
  errcheck:
    exclude-functions:
      - (github.com/go-kit/log.Logger).Log
      - fmt.Fprintln
      - fmt.Fprint
  misspell:
    locale: US
  goconst:
    min-occurrences: 5

issues:
  exclude-rules:
    # We don't check metrics naming in the tests.
    - path: _test\.go
      linters:
      - promlinter
  exclude-dirs:
    - vendor    
```

## File: `.mdox.validate.yaml`
```yaml
version: 1

validators:
  # Validators to skip checking PR/issue links of Thanos, Prometheus and Cortex.
  - regex: '(^http[s]?:\/\/)(www\.)?(github\.com\/)thanos-io\/thanos(\/pull\/|\/issues\/)'
    type: 'githubPullsIssues'
  - regex: '(^http[s]?:\/\/)(www\.)?(github\.com\/)prometheus\/prometheus(\/pull\/|\/issues\/)'
    type: 'githubPullsIssues'
  - regex: '(^http[s]?:\/\/)(www\.)?(github\.com\/)cortexproject\/cortex(\/pull\/|\/issues\/)'
    type: 'githubPullsIssues'
  # Ignore Thanos release links.
  - regex: '(^http[s]?:\/\/)(www\.)?(github\.com\/)thanos-io\/thanos(\/releases\/)'
    type: 'ignore'
  # Causes http stream errors with statuscode 0 sometimes. But is safe to skip.
  - regex: 'slack\.cncf\.io'
    type: 'ignore'
  # 301 errors even when curl-ed.
  - regex: 'envoyproxy\.io'
    type: 'ignore'
  # couldn't reach even when curl-ed.
  - regex: 'cloud\.baidu\.com'
    type: 'ignore'
  # 403 when curl-ed from GitHub actions, though not from a developer machine. Likely due to secondary rate limits.
  - regex: 'docs\.github\.com'
    type: 'ignore'
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

NOTE: As semantic versioning states all 0.y.z releases can contain breaking changes in API (flags, grpc API, any backward compatibility)

We use *breaking :warning:* to mark changes that are not backward compatible (relates only to v0.y.z releases.)

## Unreleased
- [#165](https://github.com/thanos-io/objstore/pull/165) GCS: Upgrade cloud.google.com/go/storage version to `v1.50.0`.
- [#38](https://github.com/thanos-io/objstore/pull/38) GCS: Upgrade cloud.google.com/go/storage version to `v1.43.0`.
- [#145](https://github.com/thanos-io/objstore/pull/145) Include content length in the response of Get and GetRange.
- [#157](https://github.com/thanos-io/objstore/pull/157) Azure: Add `az_tenant_id`, `client_id` and `client_secret` configs.

### Fixed
- [#196](https://github.com/thanos-io/objstore/pull/196) GCS: fix error check in Exists method when object does not exist.
- [#153](https://github.com/thanos-io/objstore/pull/153) Metrics: Fix `objstore_bucket_operation_duration_seconds_*` for `get` and `get_range` operations.
- [#141](https://github.com/thanos-io/objstore/pull/142) S3: Fix missing encryption configuration for `Bucket.Exists()` and `Bucket.Attributes()` calls.
- [#117](https://github.com/thanos-io/objstore/pull/117) Metrics: Fix `objstore_bucket_operation_failures_total` incorrectly incremented if context is cancelled while reading object contents.
- [#115](https://github.com/thanos-io/objstore/pull/115) GCS: Fix creation of bucket with GRPC connections. Also update storage client to `v1.40.0`.
- [#102](https://github.com/thanos-io/objstore/pull/102) Azure: bump azblob sdk to get concurrency fixes.
- [#33](https://github.com/thanos-io/objstore/pull/33) Tracing: Add `ContextWithTracer()` to inject the tracer into the context.
- [#34](https://github.com/thanos-io/objstore/pull/34) Fix ignored options when creating shared credential Azure client.
- [#62](https://github.com/thanos-io/objstore/pull/62) S3: Fix ignored context cancellation in `Iter` method.
- [#77](https://github.com/thanos-io/objstore/pull/77) Fix buckets wrapped with metrics from being unable to determine object sizes in `Upload`.
- [#78](https://github.com/thanos-io/objstore/pull/78) S3: Fix possible concurrent modification of the PutUserMetadata map.
- [#79](https://github.com/thanos-io/objstore/pull/79) Metrics: Fix `objstore_bucket_operation_duration_seconds` for `iter` operations.

### Added
- [#15](https://github.com/thanos-io/objstore/pull/15) Add Oracle Cloud Infrastructure Object Storage Bucket support.
- [#25](https://github.com/thanos-io/objstore/pull/25) S3: Support specifying S3 storage class.
- [#32](https://github.com/thanos-io/objstore/pull/32) Swift: Support authentication using application credentials.
- [#41](https://github.com/thanos-io/objstore/pull/41) S3: Support S3 session token.
- [#43](https://github.com/thanos-io/objstore/pull/43) filesystem: abort filesystem bucket operations if the context has been cancelled
- [#44](https://github.com/thanos-io/objstore/pull/44) Add new metric to count total number of fetched bytes from bucket
- [#50](https://github.com/thanos-io/objstore/pull/50) Add Huawei Cloud OBS Object Storage Support
- [#59](https://github.com/thanos-io/objstore/pull/59) Adding method `IsCustomerManagedKeyError` on the bucket interface.
- [#61](https://github.com/thanos-io/objstore/pull/61) Add OpenTelemetry TracingBucket.
    > This also changes the behaviour of `client.NewBucket`. Now it returns, uninstrumented and untraced bucket.
    You can combine `objstore.WrapWithMetrics` and `tracing/{opentelemetry,opentracing}.WrapWithTraces` to have old behavior.
- [#69](https://github.com/thanos-io/objstore/pull/69) [#66](https://github.com/thanos-io/objstore/pull/66) Add `objstore_bucket_operation_transferred_bytes` that counts the number of total bytes read from the bucket operation Get/GetRange and also counts the number of total bytes written to the bucket operation Upload.
- [#64](https://github.com/thanos-io/objstore/pull/64) OCI: OKE Workload Identity support.
- [#73](https://github.com/thanos-io/objstore/pull/73) Аdded file path to erros from DownloadFile
- [#51](https://github.com/thanos-io/objstore/pull/51) Azure: Support using connection string authentication.
- [#76](https://github.com/thanos-io/objstore/pull/76) GCS: Query for object names only in `Iter` to possibly improve performance when listing objects.
- [#85](https://github.com/thanos-io/objstore/pull/85) S3: Allow checksum algorithm to be configured
- [#92](https://github.com/thanos-io/objstore/pull/92) GCS: Allow using a gRPC client.
- [#94](https://github.com/thanos-io/objstore/pull/94) Allow timingReadCloser to be seeker
- [#96](https://github.com/thanos-io/objstore/pull/96) Allow nopCloserWithObjectSize to be seeker
- [#86](https://github.com/thanos-io/objstore/pull/86) GCS: Add HTTP Config to GCS
- [#99](https://github.com/thanos-io/objstore/pull/99) Swift: Add HTTP_Config
- [#108](https://github.com/thanos-io/objstore/pull/108) Metrics: Add native histogram definitions to histograms
- [#112](https://github.com/thanos-io/objstore/pull/112) S3: Add `DisableDualstack option.
- [#100](https://github.com/thanos-io/objstore/pull/100) s3: add DisableMultipart option
- [#116](https://github.com/thanos-io/objstore/pull/116) Azure: Add new storage_create_container configuration property
- [#128](https://github.com/thanos-io/objstore/pull/128) GCS: Add support for `ChunkSize` for writer.
- [#130](https://github.com/thanos-io/objstore/pull/130) feat: Decouple creating bucket metrics from instrumenting the bucket
- [#147](https://github.com/thanos-io/objstore/pull/147) feat: Add MaxRetries config to cos, gcs and obs.
- [#150](https://github.com/thanos-io/objstore/pull/150) Add support for roundtripper wrapper.
- [#63](https://github.com/thanos-io/objstore/pull/63) Implement a `IterWithAttributes` method on the bucket client.
- [#155](https://github.com/thanos-io/objstore/pull/155) Add a `Provider` method on `objstore.Client`.
- [#163](https://github.com/thanos-io/objstore/pull/145) Add a `NewBucketFromConfig` constructor method for creating a client from an existing `BucketConfig` object.


### Changed
- [#38](https://github.com/thanos-io/objstore/pull/38) *: Upgrade minio-go version to `v7.0.45`.
- [#39](https://github.com/thanos-io/objstore/pull/39) COS: Upgrade cos sdk version to `v0.7.40`.
- [#35](https://github.com/thanos-io/objstore/pull/35) Azure: Update Azure SDK and fix breaking changes.
- [#65](https://github.com/thanos-io/objstore/pull/65) *: Upgrade minio-go version to `v7.0.61`.
- [#70](https://github.com/thanos-io/objstore/pull/70) GCS: Update cloud.google.com/go/storage version to `v1.27.0`.
- [#71](https://github.com/thanos-io/objstore/pull/71) Replace method `IsCustomerManagedKeyError` for a more generic `IsAccessDeniedErr` on the bucket interface.
- [#89](https://github.com/thanos-io/objstore/pull/89) GCS: Upgrade cloud.google.com/go/storage version to `v1.35.1`.
- [#123](https://github.com/thanos-io/objstore/pull/123) *: Upgrade minio-go version to `v7.0.72`.
- [#132](https://github.com/thanos-io/objstore/pull/132) s3: Upgrade aws-sdk-go-v2/config version to `v1.27.30`

### Removed
```

## File: `COPYRIGHT`
```
Copyright (c) The Thanos Authors.
Licensed under the Apache License 2.0.
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
      boilerplate notice, with the fields enclosed by brackets "{}"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright {yyyy} {name of copyright owner}

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
include .bingo/Variables.mk

FILES_TO_FMT ?= $(shell find . -path ./vendor -prune -o -name '*.go' -print)
MDOX_VALIDATE_CONFIG ?= .mdox.validate.yaml

.PHONY: test-local
test-local:
	THANOS_TEST_OBJSTORE_SKIP=GCS,S3,AZURE,SWIFT,COS,ALIYUNOSS,BOS,OCI,OBS $(MAKE) test

.PHONY: test
test:
	go test ./...

.PHONY: test-e2e
test-e2e: docker $(GOTESPLIT)
	@echo ">> cleaning docker environment."
	@docker system prune -f --volumes
	@echo ">> cleaning e2e test garbage."
	@rm -rf ./test/e2e/e2e_*
	@echo ">> running /test/e2e tests."
	# NOTE(bwplotka):
	# * If you see errors on CI (timeouts), but not locally, try to add -parallel 1 (Wiard note: to the GOTEST_OPTS arg) to limit to single CPU to reproduce small 1CPU machine.
	@$(GOTESPLIT) -total ${GH_PARALLEL} -index ${GH_INDEX} ./test/e2e/... -- ${GOTEST_OPTS}

.PHONY: docs
docs: ## Generates docs for all thanos commands, localise links, ensure GitHub format.
docs: $(MDOX)
	@echo ">> generating docs"
	PATH="${PATH}:$(GOBIN)" $(MDOX) fmt README.md
	$(MAKE) white-noise-cleanup

.PHONY: check-docs
check-docs: ## Checks docs against discrepancy with flags, links, white noise.
check-docs: $(MDOX)
	@echo ">> checking docs"
	PATH="${PATH}:$(GOBIN)" $(MDOX) fmt -l --links.validate.config-file=$(MDOX_VALIDATE_CONFIG) README.md
	$(MAKE) white-noise-cleanup
	$(call require_clean_work_tree,'run make docs and commit changes')

.PHONY: deps
deps: ## Ensures fresh go.mod and go.sum.
	@go mod tidy -compat=1.20
	@go mod verify

.PHONY: format
format: $(GOIMPORTS)
	@echo ">> formatting go code"
	@gofmt -s -w $(FILES_TO_FMT)
	@$(GOIMPORTS) -w $(FILES_TO_FMT)

.PHONY:lint
lint: deps $(GOLANGCI_LINT) $(FAILLINT) $(COPYRIGHT) docs
	$(call require_clean_work_tree,'detected not clean work tree before running lint, previous job changed something?')
	@echo ">> verifying modules being imported"
	@# TODO(bwplotka): Add, Printf, DefaultRegisterer, NewGaugeFunc and MustRegister once exception are accepted. Add fmt.{Errorf}=github.com/pkg/errors.{Errorf} once https://github.com/fatih/faillint/issues/10 is addressed.
	@$(FAILLINT) -paths "errors=github.com/pkg/errors,\
github.com/prometheus/tsdb=github.com/prometheus/prometheus/tsdb,\
github.com/prometheus/prometheus/pkg/testutils=github.com/thanos-io/thanos/pkg/testutil,\
github.com/prometheus/client_golang/prometheus.{DefaultGatherer,DefBuckets,NewUntypedFunc,UntypedFunc},\
github.com/prometheus/client_golang/prometheus.{NewCounter,NewCounterVec,NewCounterVec,NewGauge,NewGaugeVec,NewGaugeFunc,\
NewHistorgram,NewHistogramVec,NewSummary,NewSummaryVec}=github.com/prometheus/client_golang/prometheus/promauto.{NewCounter,\
NewCounterVec,NewCounterVec,NewGauge,NewGaugeVec,NewGaugeFunc,NewHistorgram,NewHistogramVec,NewSummary,NewSummaryVec},\
sync/atomic=go.uber.org/atomic" ./...
	@$(FAILLINT) -paths "fmt.{Print,Println,Sprint}" -ignore-tests ./...
	@echo ">> linting all of the Go files GOGC=${GOGC}"
	@$(GOLANGCI_LINT) run
	@echo ">> ensuring Copyright headers"
	@$(COPYRIGHT) $(shell go list -f "{{.Dir}}" ./... | xargs -i find "{}" -name "*.go")
	$(call require_clean_work_tree,'detected files without copyright, run make lint and commit changes')

.PHONY: white-noise-cleanup
white-noise-cleanup: ## Cleans up white noise in docs.
white-noise-cleanup:
	@echo ">> cleaning up white noise"
	@find . -type f \( -name "*.md" \) | SED_BIN="$(SED)" xargs scripts/cleanup-white-noise.sh
```

## File: `README.md`
```markdown
<p align="center"><img src="Thanos-logo_fullmedium.png" alt="Thanos Logo"></p>

[![Latest Release](https://img.shields.io/github/release/thanos-io/objstore.svg?style=flat-square)](https://github.com/thanos-io/objstore/releases/latest) [![Slack](https://img.shields.io/badge/join%20slack-%23thanos-brightgreen.svg)](https://slack.cncf.io/)

[![Go Report Card](https://goreportcard.com/badge/github.com/thanos-io/objstore)](https://goreportcard.com/report/github.com/thanos-io/objstore) [![Go Code reference](https://img.shields.io/badge/code%20reference-go.dev-darkblue.svg)](https://pkg.go.dev/github.com/thanos-io/objstore?tab=subdirectories)

[![Tests](https://github.com/thanos-io/objstore/workflows/Test/badge.svg)](https://github.com/thanos-io/objstore/actions?query=workflow%3Atest)

# Thanos Object Storage Client

`objstore` is a Go module providing unified interface and efficient clients to work with various object storage providers.

Features:

* Ability to perform common operations with clear contract against most popular object storages.
* High focus on efficiency and reliability required for distributed databases on object storages.
* Optional built-in YAML based configuration definition for consistent configuration.
* Optional Prometheus metric instrumentation for bucket operations.

> This moduile is battle-tested and used on high scale production by projects like Thanos, Loki, Cortex, Mimir, Tempo, Parca and more.

## Contributing

Contributions are very welcome! See our [CONTRIBUTING.md](https://github.com/thanos-io/thanos/blob/main/CONTRIBUTING.md) for more information.

## Community

Thanos is an open source project and we value and welcome new contributors and members of the community. Here are ways to get in touch with the community:

* Slack: [#thanos](https://slack.cncf.io/)
* Issue Tracker: [GitHub Issues](https://github.com/thanos-io/thanos/issues)

## Adopters

See [`Adopters List`](https://github.com/thanos-io/thanos/blob/main/website/data/adopters.yml.

## Background

This library was initially developed as a Thanos [`objstore` package](https://github.com/thanos-io/thanos/tree/79ab7c65cb4b66b9dcc4fa537cb43b00cc65066c/pkg/objstore). Thanos uses object storage as primary storage for metrics and metadata related to them. This package ended up being used by other projects like Cortex, Loki, Mimir, Tempo, Parca and more.

Given reusability, Thanos community promoted this package to standalone Go module with smaller amount of dependencies.

## Maintainers

See [MAINTAINERS.md](https://github.com/thanos-io/thanos/blob/main/MAINTAINERS.md)

### How to use `objstore`

The core this module is the [`Bucket` interface](objstore.go):

```go mdox-exec="sed -n '55,73p' objstore.go"
// Bucket provides read and write access to an object storage bucket.
// NOTE: We assume strong consistency for write-read flow.
type Bucket interface {
	io.Closer
	BucketReader

	Provider() ObjProvider

	// Upload the contents of the reader as an object into the bucket.
	// Upload should be idempotent.
	Upload(ctx context.Context, name string, r io.Reader, opts ...ObjectUploadOption) error

	// Delete removes the object with the given name.
	// If object does not exist in the moment of deletion, Delete should throw error.
	Delete(ctx context.Context, name string) error

	// Name returns the bucket name for the provider.
	Name() string
}
```

All [provider implementations](providers) have to implement `Bucket` interface that allows common read and write operations that all supported by all object providers. If you want to limit the code that will do bucket operation to only read access (smart idea, allowing to limit access permissions), you can use the [`BucketReader` interface](objstore.go):

```go mdox-exec="sed -n '89,124p' objstore.go"
// BucketReader provides read access to an object storage bucket.
type BucketReader interface {
	// Iter calls f for each entry in the given directory (not recursive.). The argument to f is the full
	// object name including the prefix of the inspected directory.

	// Entries are passed to function in sorted order.
	Iter(ctx context.Context, dir string, f func(name string) error, options ...IterOption) error

	// IterWithAttributes calls f for each entry in the given directory similar to Iter.
	// In addition to Name, it also includes requested object attributes in the argument to f.
	//
	// Attributes can be requested using IterOption.
	// Not all IterOptions are supported by all providers, requesting for an unsupported option will fail with ErrOptionNotSupported.
	IterWithAttributes(ctx context.Context, dir string, f func(attrs IterObjectAttributes) error, options ...IterOption) error

	// SupportedIterOptions returns a list of supported IterOptions by the underlying provider.
	SupportedIterOptions() []IterOptionType

	// Get returns a reader for the given object name.
	Get(ctx context.Context, name string) (io.ReadCloser, error)

	// GetRange returns a new range reader for the given object name and range.
	GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error)

	// Exists checks if the given object exists in the bucket.
	Exists(ctx context.Context, name string) (bool, error)

	// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
	IsObjNotFoundErr(err error) bool

	// IsAccessDeniedErr returns true if access to object is denied.
	IsAccessDeniedErr(err error) bool

	// Attributes returns information about the specified object.
	Attributes(ctx context.Context, name string) (ObjectAttributes, error)
}
```

Those interfaces represent the object storage operations your code can use from `objstore` clients.

#### Factory

Generally, you have two ways of using `objstore` module:

First is to import the provider you want e.g. [`github.com/thanos-io/objstore/providers/s3`](providers/s3) and instantiate it with available constructor (e.g. `NewBucket`).

The second option is to use the factory `NewBucket(logger log.Logger, confContentYaml []byte, reg prometheus.Registerer, component string)` that will instantiate the object storage client based on YAML file provided. The YAML file has generally the format like this:

```yaml
type: <PROVIDER_TYPE>
config:
  <PROVIDER_TYPE specific options>
```

The exact option depends on provider and are in sections below.

> NOTE: All code snippets are auto-generated from code and up-to-date.

Check out the [Thanos documentation](https://thanos.io/tip/thanos/storage.md/) to see how Thanos uses this module.

#### Supported Providers (Clients)

Current object storage client implementations:

| Provider                                                                                  | Maturity           | Aimed For             | Auto-tested on CI | Maintainers                      |
|-------------------------------------------------------------------------------------------|--------------------|-----------------------|-------------------|----------------------------------|
| [Google Cloud Storage](#gcs)                                                              | Stable             | Production Usage      | yes               | @bwplotka                        |
| [AWS/S3](#s3) (and all S3-compatible storages e.g disk-based [Minio](https://min.io/))    | Stable             | Production Usage      | yes               | @bwplotka                        |
| [Azure Storage Account](#azure)                                                           | Stable             | Production Usage      | no                | @vglafirov,@phillebaba           |
| [OpenStack Swift](#openstack-swift)                                                       | Beta (working PoC) | Production Usage      | yes               | @FUSAKLA                         |
| [Tencent COS](#tencent-cos)                                                               | Beta               | Production Usage      | no                | @jojohappy,@hanjm                |
| [AliYun OSS](#aliyun-oss)                                                                 | Beta               | Production Usage      | no                | @shaulboozhiao,@wujinhu          |
| [Baidu BOS](#baidu-bos)                                                                   | Beta               | Production Usage      | no                | @yahaa                           |
| [Local Filesystem](#filesystem)                                                           | Stable             | Testing and Demo only | yes               | @bwplotka                        |
| [Oracle Cloud Infrastructure Object Storage](#oracle-cloud-infrastructure-object-storage) | Beta               | Production Usage      | yes               | @aarontams,@gaurav-05,@ericrrath |
| [HuaweiCloud OBS](#huaweicloud-obs)                                                       | Beta               | Production Usage      | no                | @setoru                          |

**Missing support to some object storage?** Check out [how to add your client section](#how-to-add-a-new-client-to-thanos)

NOTE: Currently Thanos requires strong consistency (write-read) for object store implementation for singleton Compaction purposes.

##### S3

Thanos uses the [minio client](https://github.com/minio/minio-go) library to upload Prometheus data into AWS S3.

> NOTE: S3 client was designed for AWS S3, but it can be configured against other S3-compatible object storages e.g Ceph

The S3 object storage yaml configuration definition:

```yaml mdox-exec="go run scripts/cfggen/main.go --name=s3.Config"
type: S3
config:
  bucket: ""
  endpoint: ""
  region: ""
  disable_dualstack: false
  aws_sdk_auth: false
  access_key: ""
  insecure: false
  signature_version2: false
  secret_key: ""
  session_token: ""
  put_user_metadata: {}
  http_config:
    idle_conn_timeout: 1m30s
    response_header_timeout: 2m
    insecure_skip_verify: false
    tls_handshake_timeout: 10s
    expect_continue_timeout: 1s
    max_idle_conns: 100
    max_idle_conns_per_host: 100
    max_conns_per_host: 0
    tls_config:
      ca_file: ""
      cert_file: ""
      key_file: ""
      server_name: ""
      insecure_skip_verify: false
    disable_compression: false
  trace:
    enable: false
  list_objects_version: ""
  bucket_lookup_type: auto
  send_content_md5: true
  disable_multipart: false
  part_size: 67108864
  sse_config:
    type: ""
    kms_key_id: ""
    kms_encryption_context: {}
    encryption_key: ""
  sts_endpoint: ""
  max_retries: 0
prefix: ""
```

At a minimum, you will need to provide a value for the `bucket`, `endpoint`, `access_key`, and `secret_key` keys. The rest of the keys are optional.

However if you set `aws_sdk_auth: true` Thanos will use the default authentication methods of the AWS SDK for go based on [known environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html) (`AWS_PROFILE`, `AWS_WEB_IDENTITY_TOKEN_FILE` ... etc) and known AWS config files (~/.aws/config). If you turn this on, then the `bucket` and `endpoint` are the required config keys.

The field `prefix` can be used to transparently use prefixes in your S3 bucket. This allows you to separate blocks coming from different sources into paths with different prefixes, making it easier to understand what's going on (i.e. you don't have to use Thanos tooling to know from where which blocks came).

The AWS region to endpoint mapping can be found in this [link](https://docs.aws.amazon.com/general/latest/gr/s3.html).

By default, the library prefers using [dual-stack endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/dual-stack-endpoints.html). You can explicitly disable this behaviour by setting `disable_dualstack: true`.

Make sure you use a correct signature version. Currently AWS requires signature v4, so it needs `signature_version2: false`. If you don't specify it, you will get an `Access Denied` error. On the other hand, several S3 compatible APIs use `signature_version2: true`.

You can configure the timeout settings for the HTTP client by setting the `http_config.idle_conn_timeout` and `http_config.response_header_timeout` keys. As a rule of thumb, if you are seeing errors like `timeout awaiting response headers` in your logs, you may want to increase the value of `http_config.response_header_timeout`.

Please refer to the documentation of [the Transport type](https://golang.org/pkg/net/http/#Transport) in the `net/http` package for detailed information on what each option does.

`part_size` is specified in bytes and refers to the minimum file size used for multipart uploads, as some custom S3 implementations may have different requirements. A value of `0` means to use a default 128 MiB size.

Set `list_objects_version: "v1"` for S3 compatible APIs that don't support ListObjectsV2 (e.g. some versions of Ceph). Default value (`""`) is equivalent to `"v2"`.

`http_config.tls_config` allows configuring TLS connections. Please refer to the document of [tls_config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#tls_config) for detailed information on what each option does.

`bucket_lookup_type` can be `auto`, `virtual-hosted` or `path`. Read more about it [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html).

For debug and testing purposes you can set

* `insecure: true` to switch to plain insecure HTTP instead of HTTPS

* `http_config.insecure_skip_verify: true` to disable TLS certificate verification (if your S3 based storage is using a self-signed certificate, for example)

* `trace.enable: true` to enable the minio client's verbose logging. Each request and response will be logged into the debug logger, so debug level logging must be enabled for this functionality.

###### S3 Server-Side Encryption

SSE can be configued using the `sse_config`. [SSE-S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html), [SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html), and [SSE-C](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html) are supported.

* If type is set to `SSE-S3` you do not need to configure other options.

* If type is set to `SSE-KMS` you must set `kms_key_id`. The `kms_encryption_context` is optional, as [AWS provides a default encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/services-s3.html#s3-encryption-context).

* If type is set to `SSE-C` you must provide a path to the encryption key using `encryption_key`.

If the SSE Config block is set but the `type` is not one of `SSE-S3`, `SSE-KMS`, or `SSE-C`, an error is raised.

You will also need to apply the following AWS IAM policy for the user to access the KMS key:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "KMSAccess",
            "Effect": "Allow",
            "Action": [
                "kms:GenerateDataKey",
                "kms:Encrypt",
                "kms:Decrypt"
            ],
            "Resource": "arn:aws:kms:<region>:<account>:key/<KMS key id>"
        }
    ]
}
```

###### Credentials

By default Thanos will try to retrieve credentials from the following sources:

1. From config file if BOTH `access_key` and `secret_key` are present.
2. From the standard AWS environment variable - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`
3. From `~/.aws/credentials`
4. IAM credentials retrieved from an instance profile.

NOTE: Getting access key from config file and secret key from other method (and vice versa) is not supported.

###### AWS Policies

Example working AWS IAM policy for user:

* For deployment (policy for Thanos services):

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:DeleteObject",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket>/*",
                "arn:aws:s3:::<bucket>"
            ]
        }
    ]
}
```

(No bucket policy)

To test the policy, set env vars for S3 access for *empty, not used* bucket as well as:

```
THANOS_TEST_OBJSTORE_SKIP=GCS,AZURE,SWIFT,COS,ALIYUNOSS,OCI,OBS
THANOS_ALLOW_EXISTING_BUCKET_USE=true
```

And run: `GOCACHE=off go test -v -run TestObjStore_AcceptanceTest_e2e ./pkg/...`

* For testing (policy to run e2e tests):

We need access to CreateBucket and DeleteBucket and access to all buckets:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:DeleteObject",
                "s3:PutObject",
                "s3:CreateBucket",
                "s3:DeleteBucket"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket>/*",
                "arn:aws:s3:::<bucket>"
            ]
        }
    ]
}
```

With this policy you should be able to run set `THANOS_TEST_OBJSTORE_SKIP=GCS,AZURE,SWIFT,COS,ALIYUNOSS,OCI,OBS` and unset `S3_BUCKET` and run all tests using `make test`.

Details about AWS policies: https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html

###### STS Endpoint

If you want to use IAM credential retrieved from an instance profile, Thanos needs to authenticate through AWS STS. For this purposes you can specify your own STS Endpoint.

By default Thanos will use endpoint: https://sts.amazonaws.com and AWS region corresponding endpoints.

##### GCS

To configure Google Cloud Storage bucket as an object store you need to set `bucket` with GCS bucket name and configure Google Application credentials.

For example:

```yaml mdox-exec="go run scripts/cfggen/main.go --name=gcs.Config"
type: GCS
config:
  bucket: ""
  service_account: ""
  use_grpc: false
  grpc_conn_pool_size: 0
  http_config:
    idle_conn_timeout: 0s
    response_header_timeout: 0s
    insecure_skip_verify: false
    tls_handshake_timeout: 0s
    expect_continue_timeout: 0s
    max_idle_conns: 0
    max_idle_conns_per_host: 0
    max_conns_per_host: 0
    tls_config:
      ca_file: ""
      cert_file: ""
      key_file: ""
      server_name: ""
      insecure_skip_verify: false
    disable_compression: false
  chunk_size_bytes: 0
  max_retries: 0
prefix: ""
```

###### Using GOOGLE_APPLICATION_CREDENTIALS

Application credentials are configured via JSON file and only the bucket needs to be specified, the client looks for:

1. A JSON file whose path is specified by the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
2. A JSON file in a location known to the gcloud command-line tool. On Windows, this is `%APPDATA%/gcloud/application_default_credentials.json`. On other systems, `$HOME/.config/gcloud/application_default_credentials.json`.
3. On Google App Engine it uses the `appengine.AccessToken` function.
4. On Google Compute Engine and Google App Engine Managed VMs, it fetches credentials from the metadata server. (In this final case any provided scopes are ignored.)

You can read more on how to get application credential json file in [https://cloud.google.com/docs/authentication/production](https://cloud.google.com/docs/authentication/production)

###### Using inline a Service Account

Another possibility is to inline the ServiceAccount into the Thanos configuration and only maintain one file. This feature was added, so that the Prometheus Operator only needs to take care of one secret file.

```yaml
type: GCS
config:
  bucket: "thanos"
  service_account: |-
    {
      "type": "service_account",
      "project_id": "project",
      "private_key_id": "abcdefghijklmnopqrstuvwxyz12345678906666",
      "private_key": "-----BEGIN PRIVATE KEY-----\...\n-----END PRIVATE KEY-----\n",
      "client_email": "project@thanos.iam.gserviceaccount.com",
      "client_id": "123456789012345678901",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/thanos%40gitpods.iam.gserviceaccount.com"
    }
```

###### GCS Policies

**Note:** GCS Policies should be applied at the project level, not at the bucket level

For deployment:

`Storage Object Creator` and `Storage Object Viewer`

For testing:

`Storage Object Admin` for ability to create and delete temporary buckets.

To test the policy is working as expected, exec into the sidecar container, eg:

```sh
kubectl exec -it -n <namespace> <prometheus with sidecar pod name> -c <sidecar container name> -- /bin/sh
```

Then test that you can at least list objects in the bucket, eg:

```sh
thanos tools bucket ls --objstore.config="${OBJSTORE_CONFIG}"
```

##### Azure

To use Azure Storage as Thanos object store, you need to precreate storage account from Azure portal or using Azure CLI. Follow the instructions from Azure Storage Documentation: [https://docs.microsoft.com/en-us/azure/storage/common/storage-quickstart-create-account](https://docs.microsoft.com/en-us/azure/storage/common/storage-quickstart-create-account?tabs=portal)

Config file format is the following:

```yaml mdox-exec="go run scripts/cfggen/main.go --name=azure.Config"
type: AZURE
config:
  az_tenant_id: ""
  client_id: ""
  client_secret: ""
  storage_account: ""
  storage_account_key: ""
  storage_connection_string: ""
  storage_create_container: false
  container: ""
  endpoint: ""
  user_assigned_id: ""
  max_retries: 0
  reader_config:
    max_retry_requests: 0
  pipeline_config:
    max_tries: 0
    try_timeout: 0s
    retry_delay: 0s
    max_retry_delay: 0s
  http_config:
    idle_conn_timeout: 0s
    response_header_timeout: 0s
    insecure_skip_verify: false
    tls_handshake_timeout: 0s
    expect_continue_timeout: 0s
    max_idle_conns: 0
    max_idle_conns_per_host: 0
    max_conns_per_host: 0
    tls_config:
      ca_file: ""
      cert_file: ""
      key_file: ""
      server_name: ""
      insecure_skip_verify: false
    disable_compression: false
  msi_resource: ""
prefix: ""
```

If `msi_resource` is used, authentication is done via system-assigned managed identity. The value for Azure should be `https://<storage-account-name>.blob.core.windows.net`.

If `user_assigned_id` is used, authentication is done via user-assigned managed identity. When using `user_assigned_id` the `msi_resource` defaults to `https://<storage_account>.<endpoint>`

If `storage_connection_string` is set, the values of `storage_account` and `endpoint` values will not be used. Use this method over `storage_account_key` if you need to authenticate via a SAS token.

The generic `max_retries` will be used as value for the `pipeline_config`'s `max_tries` and `reader_config`'s `max_retry_requests`. For more control, `max_retries` could be ignored (0) and one could set specific retry values.

##### OpenStack Swift

Thanos uses [ncw/swift](https://github.com/ncw/swift) client to upload Prometheus data into [OpenStack Swift](https://docs.openstack.org/swift/latest/).

Below is an example configuration file for thanos to use OpenStack swift container as an object store. Note that if the `name` of a user, project or tenant is used one must also specify its domain by ID or name. Various examples for OpenStack authentication can be found in the [official documentation](https://developer.openstack.org/api-ref/identity/v3/index.html?expanded=password-authentication-with-scoped-authorization-detail#password-authentication-with-unscoped-authorization).

By default, OpenStack Swift has a limit for maximum file size of 5 GiB. Thanos index files are often larger than that. To resolve this issue, Thanos uses [Static Large Objects (SLO)](https://docs.openstack.org/swift/latest/overview_large_objects.html) which are uploaded as segments. These are by default put into the `segments` directory of the same container. The default limit for using SLO is 1 GiB which is also the maximum size of the segment. If you don't want to use the same container for the segments (best practise is to use `<container_name>_segments` to avoid polluting listing of the container objects) you can use the `large_file_segments_container_name` option to override the default and put the segments to other container. *In rare cases you can switch to [Dynamic Large Objects (DLO)](https://docs.openstack.org/swift/latest/overview_large_objects.html) by setting the `use_dynamic_large_objects` to true, but use it with caution since it even more relies on eventual consistency.*

```yaml mdox-exec="go run scripts/cfggen/main.go --name=swift.Config"
type: SWIFT
config:
  auth_version: 0
  auth_url: ""
  username: ""
  user_domain_name: ""
  user_domain_id: ""
  user_id: ""
  password: ""
  domain_id: ""
  domain_name: ""
  application_credential_id: ""
  application_credential_name: ""
  application_credential_secret: ""
  project_id: ""
  project_name: ""
  project_domain_id: ""
  project_domain_name: ""
  region_name: ""
  container_name: ""
  large_object_chunk_size: 1073741824
  large_object_segments_container_name: ""
  retries: 3
  connect_timeout: 10s
  timeout: 5m
  use_dynamic_large_objects: false
  http_config:
    idle_conn_timeout: 1m30s
    response_header_timeout: 2m
    insecure_skip_verify: false
    tls_handshake_timeout: 10s
    expect_continue_timeout: 1s
    max_idle_conns: 100
    max_idle_conns_per_host: 100
    max_conns_per_host: 0
    tls_config:
      ca_file: ""
      cert_file: ""
      key_file: ""
      server_name: ""
      insecure_skip_verify: false
    disable_compression: false
prefix: ""
```

##### Tencent COS

To use Tencent COS as storage store, you should apply a Tencent Account to create an object storage bucket at first. Note that detailed from Tencent Cloud Documents: [https://cloud.tencent.com/document/product/436](https://cloud.tencent.com/document/product/436)

To configure Tencent Account to use COS as storage store you need to set these parameters in yaml format stored in a file:

```yaml mdox-exec="go run scripts/cfggen/main.go --name=cos.Config"
type: COS
config:
  bucket: ""
  region: ""
  app_id: ""
  endpoint: ""
  secret_key: ""
  secret_id: ""
  max_retries: 0
  http_config:
    idle_conn_timeout: 1m30s
    response_header_timeout: 2m
    insecure_skip_verify: false
    tls_handshake_timeout: 10s
    expect_continue_timeout: 1s
    max_idle_conns: 100
    max_idle_conns_per_host: 100
    max_conns_per_host: 0
    tls_config:
      ca_file: ""
      cert_file: ""
      key_file: ""
      server_name: ""
      insecure_skip_verify: false
    disable_compression: false
prefix: ""
```

The `secret_key` and `secret_id` field is required. The `http_config` field is optional for optimize HTTP transport settings. There are two ways to configure the required bucket information:
1. Provide the values of `bucket`, `region` and `app_id` keys.
2. Provide the values of `endpoint` key with url format when you want to specify vpc internal endpoint. Please refer to the document of [endpoint](https://intl.cloud.tencent.com/document/product/436/6224) for more detail.

##### AliYun OSS

In order to use AliYun OSS object storage, you should first create a bucket with proper Storage Class , ACLs and get the access key on the AliYun cloud. Go to [https://www.alibabacloud.com/product/oss](https://www.alibabacloud.com/product/oss) for more detail.

The AliYun OSS object storage yaml configuration definition:

```yaml mdox-exec="go run scripts/cfggen/main.go --name=oss.Config"
type: ALIYUNOSS
config:
  endpoint: ""
  bucket: ""
  access_key_id: ""
  access_key_secret: ""
prefix: ""
```

##### Baidu BOS

In order to use Baidu BOS object storage, you should apply for a Baidu Account and create an object storage bucket first. Refer to [Baidu Cloud Documents](https://cloud.baidu.com/doc/BOS/index.html) for more details. The Baidu BOS object storage yaml configuration definition:

```yaml mdox-exec="go run scripts/cfggen/main.go --name=bos.Config"
type: BOS
config:
  bucket: ""
  endpoint: ""
  access_key: ""
  secret_key: ""
prefix: ""
```

##### Filesystem

This storage type is used when user wants to store and access the bucket in the local filesystem. We treat filesystem the same way we would treat object storage, so all optimization for remote bucket applies even though, we might have the files locally.

NOTE: This storage type is experimental and might be inefficient. It is NOT advised to use it as the main storage for metrics in production environment. Particularly there is no planned support for distributed filesystems like NFS. This is mainly useful for testing and demos.

Filesystem "object storage" yaml configuration definition:

```yaml mdox-exec="go run scripts/cfggen/main.go --name=filesystem.Config"
type: FILESYSTEM
config:
  directory: ""
prefix: ""
```

### Oracle Cloud Infrastructure Object Storage

To configure Oracle Cloud Infrastructure (OCI) Object Storage as a Thanos Object Store, you need to provide appropriate authentication credentials to your OCI tenancy. The OCI object storage client implementation for Thanos supports default keypair, instance principal, and OKE workload identity authentication.

#### API Signing Key

The default API signing key authentication provider leverages same [configuration as the OCI CLI](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm) which is usually stored in at `$HOME/.oci/config` or via variable names starting with the string `OCI_CLI`. You can also use environment variables that start with `TF_VAR`. If the same configuration is found in multiple places the provider will prefer the first one.

The following example configures the provider to look for an existing API signing key for authentication:

```yaml
type: OCI
config:
  provider: "default"
  bucket: ""
  compartment_ocid: ""
  part_size: ""                   // Optional part size to override the OCI default of 128 MiB, value is in bytes.
  max_request_retries: ""         // Optional maximum number of retries for a request.
  request_retry_interval: ""      // Optional sleep duration in seconds between retry requests.
  http_config:
    idle_conn_timeout: 1m30s      // Optional maximum amount of time an idle (keep-alive) connection will remain idle before closing itself. Zero means no limit.
    response_header_timeout: 2m   // Optional amount of time to wait for a server's response headers after fully writing the request.
    tls_handshake_timeout: 10s    // Optional maximum amount of time waiting to wait for a TLS handshake. Zero means no timeout.
    expect_continue_timeout: 1s   // Optional amount of time to wait for a server's first response headers. Zero means no timeout and causes the body to be sent immediately.
    insecure_skip_verify: false   // Optional. If true, crypto/tls accepts any certificate presented by the server and any host name in that certificate.
    max_idle_conns: 100           // Optional maximum number of idle (keep-alive) connections across all hosts. Zero means no limit.
    max_idle_conns_per_host: 100  // Optional maximum idle (keep-alive) connections to keep per-host. If zero, DefaultMaxIdleConnsPerHost=2 is used.
    max_conns_per_host: 0         // Optional maximum total number of connections per host.
    disable_compression: false    // Optional. If true, prevents the Transport from requesting compression.
    client_timeout: 90s           // Optional time limit for requests made by the HTTP Client.
prefix: ""
```

#### Instance Principal Provider

For Example:

```yaml
type: OCI
config:
  provider: "instance-principal"
  bucket: ""
  compartment_ocid: ""
prefix: ""
```

You can also include any of the optional configuration just like the example in `Default Provider`.

#### Raw Provider

For Example:

```yaml
type: OCI
config:
  provider: "raw"
  bucket: ""
  compartment_ocid: ""
  tenancy_ocid: ""
  user_ocid: ""
  region: ""
  fingerprint: ""
  privatekey: ""
  passphrase: ""         // Optional passphrase to encrypt the private API Signing key
prefix: ""
```

You can also include any of the optional configuration just like the example in `Default Provider`.

#### OKE Workload Identity Provider

For Example:

```yaml
type: OCI
config:
  provider: "oke-workload-identity"
  bucket: ""
  region: ""
prefix: ""
```

The `bucket` and `region` fields are required. The `region` field identifies the bucket region.

##### HuaweiCloud OBS

To use HuaweiCloud OBS as an object store, you should apply for a HuaweiCloud Account to create an object storage bucket at first. More details: [HuaweiCloud OBS](https://support.huaweicloud.com/obs/index.html)

To configure HuaweiCloud Account to use OBS as storage store you need to set these parameters in YAML format stored in a file:

```yaml mdox-exec="go run scripts/cfggen/main.go --name=obs.Config"
type: OBS
config:
  bucket: ""
  endpoint: ""
  access_key: ""
  secret_key: ""
  max_retries: 0
  http_config:
    idle_conn_timeout: 1m30s
    response_header_timeout: 2m
    insecure_skip_verify: false
    tls_handshake_timeout: 10s
    expect_continue_timeout: 1s
    max_idle_conns: 100
    max_idle_conns_per_host: 100
    max_conns_per_host: 0
    tls_config:
      ca_file: ""
      cert_file: ""
      key_file: ""
      server_name: ""
      insecure_skip_verify: false
    disable_compression: false
prefix: ""
```

The `access_key` and `secret_key` field is required. The `http_config` field is optional for optimize HTTP transport settings.

#### How to add a new client to Thanos?

Following checklist allows adding new Go code client to supported providers:

1. Create new directory under `./providers/<provider>`
2. Implement [objstore.Bucket interface](objstore.go)
3. Add `NewTestBucket` constructor for testing purposes, that creates and deletes temporary bucket.
4. Use created `NewTestBucket` in [ForeachStore method](objtesting/foreach.go) to ensure we can run tests against new provider. (In PR)
5. RUN the [TestObjStoreAcceptanceTest](objtesting/acceptance_e2e_test.go) against your provider to ensure it fits. Fix any found error until test passes. (In PR)
6. Add client implementation to the factory in [factory](client/factory.go) code. (Using as small amount of flags as possible in every command)
7. Add client struct config to [cfggen](scripts/cfggen/main.go); to allow config auto generation.

At that point, anyone can use your provider by spec.
```

## File: `go.mod`
```
module github.com/thanos-io/objstore

go 1.24.0

require (
	cloud.google.com/go/storage v1.50.0
	github.com/aliyun/aliyun-oss-go-sdk v2.2.2+incompatible
	github.com/aws/aws-sdk-go-v2 v1.30.4
	github.com/aws/aws-sdk-go-v2/config v1.27.30
	github.com/baidubce/bce-sdk-go v0.9.111
	github.com/efficientgo/core v1.0.0-rc.0.0.20221201130417-ba593f67d2a4
	github.com/efficientgo/e2e v0.13.1-0.20220922081603-45de9fc588a8
	github.com/fatih/structtag v1.2.0
	github.com/fullstorydev/emulators/storage v1.0.0
	github.com/go-kit/log v0.2.1
	github.com/huaweicloud/huaweicloud-sdk-go-obs v3.25.4+incompatible
	github.com/minio/minio-go/v7 v7.0.95
	github.com/ncw/swift v1.0.53
	github.com/opentracing/opentracing-go v1.2.0
	github.com/oracle/oci-go-sdk/v65 v65.41.1
	github.com/pkg/errors v0.9.1
	github.com/prometheus/client_golang v1.17.0
	github.com/prometheus/common v0.44.0
	github.com/tencentyun/cos-go-sdk-v5 v0.7.40
	go.opentelemetry.io/otel v1.34.0
	go.opentelemetry.io/otel/trace v1.34.0
	go.uber.org/atomic v1.9.0
	golang.org/x/oauth2 v0.30.0
	golang.org/x/sync v0.15.0
	google.golang.org/api v0.220.0
	google.golang.org/grpc v1.70.0
	gopkg.in/alecthomas/kingpin.v2 v2.2.6
	gopkg.in/yaml.v2 v2.4.0
)

require (
	cel.dev/expr v0.19.2 // indirect
	cloud.google.com/go v0.118.1 // indirect
	cloud.google.com/go/auth v0.14.1 // indirect
	cloud.google.com/go/auth/oauth2adapt v0.2.7 // indirect
	cloud.google.com/go/compute/metadata v0.6.0 // indirect
	cloud.google.com/go/iam v1.3.1 // indirect
	cloud.google.com/go/monitoring v1.24.0 // indirect
	github.com/Azure/azure-sdk-for-go/sdk/internal v1.11.1 // indirect
	github.com/AzureAD/microsoft-authentication-library-for-go v1.4.2 // indirect
	github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.26.0 // indirect
	github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric v0.50.0 // indirect
	github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping v0.50.0 // indirect
	github.com/alecthomas/template v0.0.0-20190718012654-fb15b899a751 // indirect
	github.com/alecthomas/units v0.0.0-20211218093645-b94a6e3cc137 // indirect
	github.com/aws/aws-sdk-go-v2/credentials v1.17.29 // indirect
	github.com/aws/aws-sdk-go-v2/feature/ec2/imds v1.16.12 // indirect
	github.com/aws/aws-sdk-go-v2/internal/configsources v1.3.16 // indirect
	github.com/aws/aws-sdk-go-v2/internal/endpoints/v2 v2.6.16 // indirect
	github.com/aws/aws-sdk-go-v2/internal/ini v1.8.1 // indirect
	github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding v1.11.4 // indirect
	github.com/aws/aws-sdk-go-v2/service/internal/presigned-url v1.11.18 // indirect
	github.com/aws/aws-sdk-go-v2/service/sso v1.22.5 // indirect
	github.com/aws/aws-sdk-go-v2/service/ssooidc v1.26.5 // indirect
	github.com/aws/aws-sdk-go-v2/service/sts v1.30.5 // indirect
	github.com/aws/smithy-go v1.20.4 // indirect
	github.com/baiyubin/aliyun-sts-go-sdk v0.0.0-20180326062324-cfa1a18b161f // indirect
	github.com/beorn7/perks v1.0.1 // indirect
	github.com/bluele/gcache v0.0.2 // indirect
	github.com/cespare/xxhash/v2 v2.3.0 // indirect
	github.com/clbanning/mxj v1.8.4 // indirect
	github.com/cncf/xds/go v0.0.0-20250121191232-2f005788dc42 // indirect
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/dustin/go-humanize v1.0.1 // indirect
	github.com/envoyproxy/go-control-plane/envoy v1.32.4 // indirect
	github.com/envoyproxy/protoc-gen-validate v1.2.1 // indirect
	github.com/felixge/httpsnoop v1.0.4 // indirect
	github.com/go-ini/ini v1.67.0 // indirect
	github.com/go-logfmt/logfmt v0.5.1 // indirect
	github.com/go-logr/logr v1.4.2 // indirect
	github.com/go-logr/stdr v1.2.2 // indirect
	github.com/goccy/go-json v0.10.5 // indirect
	github.com/gofrs/flock v0.8.1 // indirect
	github.com/golang-jwt/jwt/v5 v5.2.2 // indirect
	github.com/golang/protobuf v1.5.4 // indirect
	github.com/google/btree v1.1.3 // indirect
	github.com/google/go-querystring v1.1.0 // indirect
	github.com/google/s2a-go v0.1.9 // indirect
	github.com/google/uuid v1.6.0 // indirect
	github.com/googleapis/enterprise-certificate-proxy v0.3.4 // indirect
	github.com/googleapis/gax-go/v2 v2.14.1 // indirect
	github.com/jpillora/backoff v1.0.0 // indirect
	github.com/klauspost/compress v1.18.0 // indirect
	github.com/klauspost/cpuid/v2 v2.2.11 // indirect
	github.com/kylelemons/godebug v1.1.0 // indirect
	github.com/matttproud/golang_protobuf_extensions v1.0.4 // indirect
	github.com/minio/crc64nvme v1.0.2 // indirect
	github.com/minio/md5-simd v1.1.2 // indirect
	github.com/mitchellh/mapstructure v1.4.3 // indirect
	github.com/mozillazg/go-httpheader v0.2.1 // indirect
	github.com/mwitkow/go-conntrack v0.0.0-20190716064945-2f068394615f // indirect
	github.com/philhofer/fwd v1.2.0 // indirect
	github.com/pkg/browser v0.0.0-20240102092130-5ac0b6a4141c // indirect
	github.com/planetscale/vtprotobuf v0.6.1-0.20240319094008-0393e58bdf10 // indirect
	github.com/prometheus/client_model v0.6.1 // indirect
	github.com/prometheus/procfs v0.11.1 // indirect
	github.com/rs/xid v1.6.0 // indirect
	github.com/sony/gobreaker v0.5.0 // indirect
	github.com/stretchr/objx v0.5.2 // indirect
	github.com/tinylib/msgp v1.3.0 // indirect
	go.opentelemetry.io/auto/sdk v1.1.0 // indirect
	go.opentelemetry.io/contrib/detectors/gcp v1.34.0 // indirect
	go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc v0.59.0 // indirect
	go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp v0.59.0 // indirect
	go.opentelemetry.io/otel/metric v1.34.0 // indirect
	go.opentelemetry.io/otel/sdk v1.34.0 // indirect
	go.opentelemetry.io/otel/sdk/metric v1.34.0 // indirect
	golang.org/x/net v0.41.0 // indirect
	golang.org/x/sys v0.33.0 // indirect
	golang.org/x/text v0.26.0 // indirect
	golang.org/x/time v0.10.0 // indirect
	google.golang.org/genproto v0.0.0-20250204164813-702378808489 // indirect
	google.golang.org/genproto/googleapis/api v0.0.0-20250204164813-702378808489 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20250204164813-702378808489 // indirect
	google.golang.org/protobuf v1.36.4 // indirect
)

require (
	github.com/Azure/azure-sdk-for-go/sdk/azcore v1.18.1
	github.com/Azure/azure-sdk-for-go/sdk/azidentity v1.10.1
	github.com/Azure/azure-sdk-for-go/sdk/storage/azblob v1.6.1
	github.com/satori/go.uuid v1.2.1-0.20181028125025-b2ce2384e17b // indirect
	golang.org/x/crypto v0.39.0 // indirect
)
```

## File: `go.sum`
```
cel.dev/expr v0.19.2 h1:V354PbqIXr9IQdwy4SYA4xa0HXaWq1BUPAGzugBY5V4=
cel.dev/expr v0.19.2/go.mod h1:MrpN08Q+lEBs+bGYdLxxHkZoUSsCp0nSKTs0nTymJgw=
cloud.google.com/go v0.118.1 h1:b8RATMcrK9A4BH0rj8yQupPXp+aP+cJ0l6H7V9osV1E=
cloud.google.com/go v0.118.1/go.mod h1:CFO4UPEPi8oV21xoezZCrd3d81K4fFkDTEJu4R8K+9M=
cloud.google.com/go/auth v0.14.1 h1:AwoJbzUdxA/whv1qj3TLKwh3XX5sikny2fc40wUl+h0=
cloud.google.com/go/auth v0.14.1/go.mod h1:4JHUxlGXisL0AW8kXPtUF6ztuOksyfUQNFjfsOCXkPM=
cloud.google.com/go/auth/oauth2adapt v0.2.7 h1:/Lc7xODdqcEw8IrZ9SvwnlLX6j9FHQM74z6cBk9Rw6M=
cloud.google.com/go/auth/oauth2adapt v0.2.7/go.mod h1:NTbTTzfvPl1Y3V1nPpOgl2w6d/FjO7NNUQaWSox6ZMc=
cloud.google.com/go/compute/metadata v0.6.0 h1:A6hENjEsCDtC1k8byVsgwvVcioamEHvZ4j01OwKxG9I=
cloud.google.com/go/compute/metadata v0.6.0/go.mod h1:FjyFAW1MW0C203CEOMDTu3Dk1FlqW3Rga40jzHL4hfg=
cloud.google.com/go/iam v1.3.1 h1:KFf8SaT71yYq+sQtRISn90Gyhyf4X8RGgeAVC8XGf3E=
cloud.google.com/go/iam v1.3.1/go.mod h1:3wMtuyT4NcbnYNPLMBzYRFiEfjKfJlLVLrisE7bwm34=
cloud.google.com/go/logging v1.13.0 h1:7j0HgAp0B94o1YRDqiqm26w4q1rDMH7XNRU34lJXHYc=
cloud.google.com/go/logging v1.13.0/go.mod h1:36CoKh6KA/M0PbhPKMq6/qety2DCAErbhXT62TuXALA=
cloud.google.com/go/longrunning v0.6.4 h1:3tyw9rO3E2XVXzSApn1gyEEnH2K9SynNQjMlBi3uHLg=
cloud.google.com/go/longrunning v0.6.4/go.mod h1:ttZpLCe6e7EXvn9OxpBRx7kZEB0efv8yBO6YnVMfhJs=
cloud.google.com/go/monitoring v1.24.0 h1:csSKiCJ+WVRgNkRzzz3BPoGjFhjPY23ZTcaenToJxMM=
cloud.google.com/go/monitoring v1.24.0/go.mod h1:Bd1PRK5bmQBQNnuGwHBfUamAV1ys9049oEPHnn4pcsc=
cloud.google.com/go/storage v1.50.0 h1:3TbVkzTooBvnZsk7WaAQfOsNrdoM8QHusXA1cpk6QJs=
cloud.google.com/go/storage v1.50.0/go.mod h1:l7XeiD//vx5lfqE3RavfmU9yvk5Pp0Zhcv482poyafY=
cloud.google.com/go/trace v1.11.3 h1:c+I4YFjxRQjvAhRmSsmjpASUKq88chOX854ied0K/pE=
cloud.google.com/go/trace v1.11.3/go.mod h1:pt7zCYiDSQjC9Y2oqCsh9jF4GStB/hmjrYLsxRR27q8=
github.com/Azure/azure-sdk-for-go/sdk/azcore v1.18.1 h1:Wc1ml6QlJs2BHQ/9Bqu1jiyggbsSjramq2oUmp5WeIo=
github.com/Azure/azure-sdk-for-go/sdk/azcore v1.18.1/go.mod h1:Ot/6aikWnKWi4l9QB7qVSwa8iMphQNqkWALMoNT3rzM=
github.com/Azure/azure-sdk-for-go/sdk/azidentity v1.10.1 h1:B+blDbyVIG3WaikNxPnhPiJ1MThR03b3vKGtER95TP4=
github.com/Azure/azure-sdk-for-go/sdk/azidentity v1.10.1/go.mod h1:JdM5psgjfBf5fo2uWOZhflPWyDBZ/O/CNAH9CtsuZE4=
github.com/Azure/azure-sdk-for-go/sdk/azidentity/cache v0.3.2 h1:yz1bePFlP5Vws5+8ez6T3HWXPmwOK7Yvq8QxDBD3SKY=
github.com/Azure/azure-sdk-for-go/sdk/azidentity/cache v0.3.2/go.mod h1:Pa9ZNPuoNu/GztvBSKk9J1cDJW6vk/n0zLtV4mgd8N8=
github.com/Azure/azure-sdk-for-go/sdk/internal v1.11.1 h1:FPKJS1T+clwv+OLGt13a8UjqeRuh0O4SJ3lUriThc+4=
github.com/Azure/azure-sdk-for-go/sdk/internal v1.11.1/go.mod h1:j2chePtV91HrC22tGoRX3sGY42uF13WzmmV80/OdVAA=
github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/storage/armstorage v1.8.0 h1:LR0kAX9ykz8G4YgLCaRDVJ3+n43R8MneB5dTy2konZo=
github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/storage/armstorage v1.8.0/go.mod h1:DWAciXemNf++PQJLeXUB4HHH5OpsAh12HZnu2wXE1jA=
github.com/Azure/azure-sdk-for-go/sdk/storage/azblob v1.6.1 h1:lhZdRq7TIx0GJQvSyX2Si406vrYsov2FXGp/RnSEtcs=
github.com/Azure/azure-sdk-for-go/sdk/storage/azblob v1.6.1/go.mod h1:8cl44BDmi+effbARHMQjgOKA2AYvcohNm7KEt42mSV8=
github.com/AzureAD/microsoft-authentication-extensions-for-go/cache v0.1.1 h1:WJTmL004Abzc5wDB5VtZG2PJk5ndYDgVacGqfirKxjM=
github.com/AzureAD/microsoft-authentication-extensions-for-go/cache v0.1.1/go.mod h1:tCcJZ0uHAmvjsVYzEFivsRTN00oz5BEsRgQHu5JZ9WE=
github.com/AzureAD/microsoft-authentication-library-for-go v1.4.2 h1:oygO0locgZJe7PpYPXT5A29ZkwJaPqcva7BVeemZOZs=
github.com/AzureAD/microsoft-authentication-library-for-go v1.4.2/go.mod h1:wP83P5OoQ5p6ip3ScPr0BAq0BvuPAvacpEuSzyouqAI=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.26.0 h1:f2Qw/Ehhimh5uO1fayV0QIW7DShEQqhtUfhYc+cBPlw=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.26.0/go.mod h1:2bIszWvQRlJVmJLiuLhukLImRjKPcYdzzsx6darK02A=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric v0.50.0 h1:5IT7xOdq17MtcdtL/vtl6mGfzhaq4m4vpollPRmlsBQ=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric v0.50.0/go.mod h1:ZV4VOm0/eHR06JLrXWe09068dHpr3TRpY9Uo7T+anuA=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/cloudmock v0.50.0 h1:nNMpRpnkWDAaqcpxMJvxa/Ud98gjbYwayJY4/9bdjiU=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/cloudmock v0.50.0/go.mod h1:SZiPHWGOOk3bl8tkevxkoiwPgsIl6CwrWcbwjfHZpdM=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping v0.50.0 h1:ig/FpDD2JofP/NExKQUbn7uOSZzJAQqogfqluZK4ed4=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping v0.50.0/go.mod h1:otE2jQekW/PqXk1Awf5lmfokJx4uwuqcj1ab5SpGeW0=
github.com/QcloudApi/qcloud_sign_golang v0.0.0-20141224014652-e4130a326409/go.mod h1:1pk82RBxDY/JZnPQrtqHlUFfCctgdorsd9M06fMynOM=
github.com/alecthomas/template v0.0.0-20190718012654-fb15b899a751 h1:JYp7IbQjafoB+tBA3gMyHYHrpOtNuDiK/uB5uXxq5wM=
github.com/alecthomas/template v0.0.0-20190718012654-fb15b899a751/go.mod h1:LOuyumcjzFXgccqObfd/Ljyb9UuFJ6TxHnclSeseNhc=
github.com/alecthomas/units v0.0.0-20211218093645-b94a6e3cc137 h1:s6gZFSlWYmbqAuRjVTiNNhvNRfY2Wxp9nhfyel4rklc=
github.com/alecthomas/units v0.0.0-20211218093645-b94a6e3cc137/go.mod h1:OMCwj8VM1Kc9e19TLln2VL61YJF0x1XFtfdL4JdbSyE=
github.com/aliyun/aliyun-oss-go-sdk v2.2.2+incompatible h1:9gWa46nstkJ9miBReJcN8Gq34cBFbzSpQZVVT9N09TM=
github.com/aliyun/aliyun-oss-go-sdk v2.2.2+incompatible/go.mod h1:T/Aws4fEfogEE9v+HPhhw+CntffsBHJ8nXQCwKr0/g8=
github.com/aws/aws-sdk-go-v2 v1.30.4 h1:frhcagrVNrzmT95RJImMHgabt99vkXGslubDaDagTk8=
github.com/aws/aws-sdk-go-v2 v1.30.4/go.mod h1:CT+ZPWXbYrci8chcARI3OmI/qgd+f6WtuLOoaIA8PR0=
github.com/aws/aws-sdk-go-v2/config v1.27.30 h1:AQF3/+rOgeJBQP3iI4vojlPib5X6eeOYoa/af7OxAYg=
github.com/aws/aws-sdk-go-v2/config v1.27.30/go.mod h1:yxqvuubha9Vw8stEgNiStO+yZpP68Wm9hLmcm+R/Qk4=
github.com/aws/aws-sdk-go-v2/credentials v1.17.29 h1:CwGsupsXIlAFYuDVHv1nnK0wnxO0wZ/g1L8DSK/xiIw=
github.com/aws/aws-sdk-go-v2/credentials v1.17.29/go.mod h1:BPJ/yXV92ZVq6G8uYvbU0gSl8q94UB63nMT5ctNO38g=
github.com/aws/aws-sdk-go-v2/feature/ec2/imds v1.16.12 h1:yjwoSyDZF8Jth+mUk5lSPJCkMC0lMy6FaCD51jm6ayE=
github.com/aws/aws-sdk-go-v2/feature/ec2/imds v1.16.12/go.mod h1:fuR57fAgMk7ot3WcNQfb6rSEn+SUffl7ri+aa8uKysI=
github.com/aws/aws-sdk-go-v2/internal/configsources v1.3.16 h1:TNyt/+X43KJ9IJJMjKfa3bNTiZbUP7DeCxfbTROESwY=
github.com/aws/aws-sdk-go-v2/internal/configsources v1.3.16/go.mod h1:2DwJF39FlNAUiX5pAc0UNeiz16lK2t7IaFcm0LFHEgc=
github.com/aws/aws-sdk-go-v2/internal/endpoints/v2 v2.6.16 h1:jYfy8UPmd+6kJW5YhY0L1/KftReOGxI/4NtVSTh9O/I=
github.com/aws/aws-sdk-go-v2/internal/endpoints/v2 v2.6.16/go.mod h1:7ZfEPZxkW42Afq4uQB8H2E2e6ebh6mXTueEpYzjCzcs=
github.com/aws/aws-sdk-go-v2/internal/ini v1.8.1 h1:VaRN3TlFdd6KxX1x3ILT5ynH6HvKgqdiXoTxAF4HQcQ=
github.com/aws/aws-sdk-go-v2/internal/ini v1.8.1/go.mod h1:FbtygfRFze9usAadmnGJNc8KsP346kEe+y2/oyhGAGc=
github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding v1.11.4 h1:KypMCbLPPHEmf9DgMGw51jMj77VfGPAN2Kv4cfhlfgI=
github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding v1.11.4/go.mod h1:Vz1JQXliGcQktFTN/LN6uGppAIRoLBR2bMvIMP0gOjc=
github.com/aws/aws-sdk-go-v2/service/internal/presigned-url v1.11.18 h1:tJ5RnkHCiSH0jyd6gROjlJtNwov0eGYNz8s8nFcR0jQ=
github.com/aws/aws-sdk-go-v2/service/internal/presigned-url v1.11.18/go.mod h1:++NHzT+nAF7ZPrHPsA+ENvsXkOO8wEu+C6RXltAG4/c=
github.com/aws/aws-sdk-go-v2/service/sso v1.22.5 h1:zCsFCKvbj25i7p1u94imVoO447I/sFv8qq+lGJhRN0c=
github.com/aws/aws-sdk-go-v2/service/sso v1.22.5/go.mod h1:ZeDX1SnKsVlejeuz41GiajjZpRSWR7/42q/EyA/QEiM=
github.com/aws/aws-sdk-go-v2/service/ssooidc v1.26.5 h1:SKvPgvdvmiTWoi0GAJ7AsJfOz3ngVkD/ERbs5pUnHNI=
github.com/aws/aws-sdk-go-v2/service/ssooidc v1.26.5/go.mod h1:20sz31hv/WsPa3HhU3hfrIet2kxM4Pe0r20eBZ20Tac=
github.com/aws/aws-sdk-go-v2/service/sts v1.30.5 h1:OMsEmCyz2i89XwRwPouAJvhj81wINh+4UK+k/0Yo/q8=
github.com/aws/aws-sdk-go-v2/service/sts v1.30.5/go.mod h1:vmSqFK+BVIwVpDAGZB3CoCXHzurt4qBE8lf+I/kRTh0=
github.com/aws/smithy-go v1.20.4 h1:2HK1zBdPgRbjFOHlfeQZfpC4r72MOb9bZkiFwggKO+4=
github.com/aws/smithy-go v1.20.4/go.mod h1:irrKGvNn1InZwb2d7fkIRNucdfwR8R+Ts3wxYa/cJHg=
github.com/baidubce/bce-sdk-go v0.9.111 h1:yGgtPpZYUZW4uoVorQ4xnuEgVeddACydlcJKW87MDV4=
github.com/baidubce/bce-sdk-go v0.9.111/go.mod h1:zbYJMQwE4IZuyrJiFO8tO8NbtYiKTFTbwh4eIsqjVdg=
github.com/baiyubin/aliyun-sts-go-sdk v0.0.0-20180326062324-cfa1a18b161f h1:ZNv7On9kyUzm7fvRZumSyy/IUiSC7AzL0I1jKKtwooA=
github.com/baiyubin/aliyun-sts-go-sdk v0.0.0-20180326062324-cfa1a18b161f/go.mod h1:AuiFmCCPBSrqvVMvuqFuk0qogytodnVFVSN5CeJB8Gc=
github.com/beorn7/perks v1.0.1 h1:VlbKKnNfV8bJzeqoa4cOKqO6bYr3WgKZxO8Z16+hsOM=
github.com/beorn7/perks v1.0.1/go.mod h1:G2ZrVWU2WbWT9wwq4/hrbKbnv/1ERSJQ0ibhJ6rlkpw=
github.com/bluele/gcache v0.0.2 h1:WcbfdXICg7G/DGBh1PFfcirkWOQV+v077yF1pSy3DGw=
github.com/bluele/gcache v0.0.2/go.mod h1:m15KV+ECjptwSPxKhOhQoAFQVtUFjTVkc3H8o0t/fp0=
github.com/cespare/xxhash/v2 v2.3.0 h1:UL815xU9SqsFlibzuggzjXhog7bL6oX9BbNZnL2UFvs=
github.com/cespare/xxhash/v2 v2.3.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/clbanning/mxj v1.8.4 h1:HuhwZtbyvyOw+3Z1AowPkU87JkJUSv751ELWaiTpj8I=
github.com/clbanning/mxj v1.8.4/go.mod h1:BVjHeAH+rl9rs6f+QIpeRl0tfu10SXn1pUSa5PVGJng=
github.com/cncf/xds/go v0.0.0-20250121191232-2f005788dc42 h1:Om6kYQYDUk5wWbT0t0q6pvyM49i9XZAv9dDrkDA7gjk=
github.com/cncf/xds/go v0.0.0-20250121191232-2f005788dc42/go.mod h1:W+zGtBO5Y1IgJhy4+A9GOqVhqLpfZi+vwmdNXUehLA8=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/dgryski/go-rendezvous v0.0.0-20200823014737-9f7001d12a5f h1:lO4WD4F/rVNCu3HqELle0jiPLLBs70cWOduZpkS1E78=
github.com/dgryski/go-rendezvous v0.0.0-20200823014737-9f7001d12a5f/go.mod h1:cuUVRXasLTGF7a8hSLbxyZXjz+1KgoB3wDUb6vlszIc=
github.com/dustin/go-humanize v1.0.1 h1:GzkhY7T5VNhEkwH0PVJgjz+fX1rhBrR7pRT3mDkpeCY=
github.com/dustin/go-humanize v1.0.1/go.mod h1:Mu1zIs6XwVuF/gI1OepvI0qD18qycQx+mFykh5fBlto=
github.com/efficientgo/core v1.0.0-rc.0.0.20221201130417-ba593f67d2a4 h1:rydBwnBoywKQMjWF0z8SriYtQ+uUcaFsxuijMjJr5PI=
github.com/efficientgo/core v1.0.0-rc.0.0.20221201130417-ba593f67d2a4/go.mod h1:kQa0V74HNYMfuJH6jiPiwNdpWXl4xd/K4tzlrcvYDQI=
github.com/efficientgo/e2e v0.13.1-0.20220922081603-45de9fc588a8 h1:UFLc39BcUXahSNCLUrKjNGZABMUZaS4M74EZvTRnq3k=
github.com/efficientgo/e2e v0.13.1-0.20220922081603-45de9fc588a8/go.mod h1:Hi+sz0REtlhVZ8zcdeTC3j6LUEEpJpPtNjOaOKuNcgI=
github.com/envoyproxy/go-control-plane v0.13.4 h1:zEqyPVyku6IvWCFwux4x9RxkLOMUL+1vC9xUFv5l2/M=
github.com/envoyproxy/go-control-plane v0.13.4/go.mod h1:kDfuBlDVsSj2MjrLEtRWtHlsWIFcGyB2RMO44Dc5GZA=
github.com/envoyproxy/go-control-plane/envoy v1.32.4 h1:jb83lalDRZSpPWW2Z7Mck/8kXZ5CQAFYVjQcdVIr83A=
github.com/envoyproxy/go-control-plane/envoy v1.32.4/go.mod h1:Gzjc5k8JcJswLjAx1Zm+wSYE20UrLtt7JZMWiWQXQEw=
github.com/envoyproxy/go-control-plane/ratelimit v0.1.0 h1:/G9QYbddjL25KvtKTv3an9lx6VBE2cnb8wp1vEGNYGI=
github.com/envoyproxy/go-control-plane/ratelimit v0.1.0/go.mod h1:Wk+tMFAFbCXaJPzVVHnPgRKdUdwW/KdbRt94AzgRee4=
github.com/envoyproxy/protoc-gen-validate v1.2.1 h1:DEo3O99U8j4hBFwbJfrz9VtgcDfUKS7KJ7spH3d86P8=
github.com/envoyproxy/protoc-gen-validate v1.2.1/go.mod h1:d/C80l/jxXLdfEIhX1W2TmLfsJ31lvEjwamM4DxlWXU=
github.com/fatih/structtag v1.2.0 h1:/OdNE99OxoI/PqaW/SuSK9uxxT3f/tcSZgon/ssNSx4=
github.com/fatih/structtag v1.2.0/go.mod h1:mBJUNpUnHmRKrKlQQlmCrh5PuhftFbNv8Ys4/aAZl94=
github.com/felixge/httpsnoop v1.0.4 h1:NFTV2Zj1bL4mc9sqWACXbQFVBBg2W3GPvqp8/ESS2Wg=
github.com/felixge/httpsnoop v1.0.4/go.mod h1:m8KPJKqk1gH5J9DgRY2ASl2lWCfGKXixSwevea8zH2U=
github.com/fullstorydev/emulators/storage v1.0.0 h1:fU+p9PkzQV35QJVKZl4I8frQvPLcwheud0ammOLJhZY=
github.com/fullstorydev/emulators/storage v1.0.0/go.mod h1:tKvCtgVqtN/OdLUdVWcBC56T2Mo6GC1Tf17AimCogr0=
github.com/go-ini/ini v1.67.0 h1:z6ZrTEZqSWOTyH2FlglNbNgARyHG8oLW9gMELqKr06A=
github.com/go-ini/ini v1.67.0/go.mod h1:ByCAeIL28uOIIG0E3PJtZPDL8WnHpFKFOtgjp+3Ies8=
github.com/go-kit/log v0.2.1 h1:MRVx0/zhvdseW+Gza6N9rVzU/IVzaeE1SFI4raAhmBU=
github.com/go-kit/log v0.2.1/go.mod h1:NwTd00d/i8cPZ3xOwwiv2PO5MOcx78fFErGNcVmBjv0=
github.com/go-logfmt/logfmt v0.5.1 h1:otpy5pqBCBZ1ng9RQ0dPu4PN7ba75Y/aA+UpowDyNVA=
github.com/go-logfmt/logfmt v0.5.1/go.mod h1:WYhtIu8zTZfxdn5+rREduYbwxfcBr/Vr6KEVveWlfTs=
github.com/go-logr/logr v1.2.2/go.mod h1:jdQByPbusPIv2/zmleS9BjJVeZ6kBagPoEUsqbVz/1A=
github.com/go-logr/logr v1.4.2 h1:6pFjapn8bFcIbiKo3XT4j/BhANplGihG6tvd+8rYgrY=
github.com/go-logr/logr v1.4.2/go.mod h1:9T104GzyrTigFIr8wt5mBrctHMim0Nb2HLGrmQ40KvY=
github.com/go-logr/stdr v1.2.2 h1:hSWxHoqTgW2S2qGc0LTAI563KZ5YKYRhT3MFKZMbjag=
github.com/go-logr/stdr v1.2.2/go.mod h1:mMo/vtBO5dYbehREoey6XUKy/eSumjCCveDpRre4VKE=
github.com/goccy/go-json v0.10.5 h1:Fq85nIqj+gXn/S5ahsiTlK3TmC85qgirsdTP/+DeaC4=
github.com/goccy/go-json v0.10.5/go.mod h1:oq7eo15ShAhp70Anwd5lgX2pLfOS3QCiwU/PULtXL6M=
github.com/gofrs/flock v0.8.1 h1:+gYjHKf32LDeiEEFhQaotPbLuUXjY5ZqxKgXy7n59aw=
github.com/gofrs/flock v0.8.1/go.mod h1:F1TvTiK9OcQqauNUHlbJvyl9Qa1QvF/gOUDKA14jxHU=
github.com/golang-jwt/jwt/v5 v5.2.2 h1:Rl4B7itRWVtYIHFrSNd7vhTiz9UpLdi6gZhZ3wEeDy8=
github.com/golang-jwt/jwt/v5 v5.2.2/go.mod h1:pqrtFR0X4osieyHYxtmOUWsAWrfe1Q5UVIyoH402zdk=
github.com/golang/protobuf v1.2.0/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.5.4 h1:i7eJL8qZTpSEXOPTxNKhASYpMn+8e5Q6AdndVa1dWek=
github.com/golang/protobuf v1.5.4/go.mod h1:lnTiLA8Wa4RWRcIUkrtSVa5nRhsEGBg48fD6rSs7xps=
github.com/google/btree v1.1.3 h1:CVpQJjYgC4VbzxeGVHfvZrv1ctoYCAI8vbl07Fcxlyg=
github.com/google/btree v1.1.3/go.mod h1:qOPhT0dTNdNzV6Z/lhRX0YXUafgPLFUh+gZMl761Gm4=
github.com/google/go-cmp v0.5.2/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.6.0 h1:ofyhxvXcZhMsU5ulbFiLKl/XBFqE1GSq7atu8tAmTRI=
github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/google/go-querystring v1.0.0/go.mod h1:odCYkC5MyYFN7vkCjXpyrEuKhc/BUO6wN/zVPAxq5ck=
github.com/google/go-querystring v1.1.0 h1:AnCroh3fv4ZBgVIf1Iwtovgjaw/GiKJo8M8yD/fhyJ8=
github.com/google/go-querystring v1.1.0/go.mod h1:Kcdr2DB4koayq7X8pmAG4sNG59So17icRSOU623lUBU=
github.com/google/martian/v3 v3.3.3 h1:DIhPTQrbPkgs2yJYdXU/eNACCG5DVQjySNRNlflZ9Fc=
github.com/google/martian/v3 v3.3.3/go.mod h1:iEPrYcgCF7jA9OtScMFQyAlZZ4YXTKEtJ1E6RWzmBA0=
github.com/google/s2a-go v0.1.9 h1:LGD7gtMgezd8a/Xak7mEWL0PjoTQFvpRudN895yqKW0=
github.com/google/s2a-go v0.1.9/go.mod h1:YA0Ei2ZQL3acow2O62kdp9UlnvMmU7kA6Eutn0dXayM=
github.com/google/uuid v1.1.1/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/googleapis/enterprise-certificate-proxy v0.3.4 h1:XYIDZApgAnrN1c855gTgghdIA6Stxb52D5RnLI1SLyw=
github.com/googleapis/enterprise-certificate-proxy v0.3.4/go.mod h1:YKe7cfqYXjKGpGvmSg28/fFvhNzinZQm8DGnaburhGA=
github.com/googleapis/gax-go/v2 v2.14.1 h1:hb0FFeiPaQskmvakKu5EbCbpntQn48jyHuvrkurSS/Q=
github.com/googleapis/gax-go/v2 v2.14.1/go.mod h1:Hb/NubMaVM88SrNkvl8X/o8XWwDJEPqouaLeN2IUxoA=
github.com/huaweicloud/huaweicloud-sdk-go-obs v3.25.4+incompatible h1:yNjwdvn9fwuN6Ouxr0xHM0cVu03YMUWUyFmu2van/Yc=
github.com/huaweicloud/huaweicloud-sdk-go-obs v3.25.4+incompatible/go.mod h1:l7VUhRbTKCzdOacdT4oWCwATKyvZqUOlOqr0Ous3k4s=
github.com/jpillora/backoff v1.0.0 h1:uvFg412JmmHBHw7iwprIxkPMI+sGQ4kzOWsMeHnm2EA=
github.com/jpillora/backoff v1.0.0/go.mod h1:J/6gKK9jxlEcS3zixgDgUAsiuZ7yrSoa/FX5e0EB2j4=
github.com/keybase/go-keychain v0.0.1 h1:way+bWYa6lDppZoZcgMbYsvC7GxljxrskdNInRtuthU=
github.com/keybase/go-keychain v0.0.1/go.mod h1:PdEILRW3i9D8JcdM+FmY6RwkHGnhHxXwkPPMeUgOK1k=
github.com/klauspost/compress v1.18.0 h1:c/Cqfb0r+Yi+JtIEq73FWXVkRonBlf0CRNYc8Zttxdo=
github.com/klauspost/compress v1.18.0/go.mod h1:2Pp+KzxcywXVXMr50+X0Q/Lsb43OQHYWRCY2AiWywWQ=
github.com/klauspost/cpuid/v2 v2.0.1/go.mod h1:FInQzS24/EEf25PyTYn52gqo7WaD8xa0213Md/qVLRg=
github.com/klauspost/cpuid/v2 v2.2.11 h1:0OwqZRYI2rFrjS4kvkDnqJkKHdHaRnCm68/DY4OxRzU=
github.com/klauspost/cpuid/v2 v2.2.11/go.mod h1:hqwkgyIinND0mEev00jJYCxPNVRVXFQeu1XKlok6oO0=
github.com/kr/pretty v0.3.1 h1:flRD4NNwYAUpkphVc1HcthR4KEIFJ65n8Mw5qdRn3LE=
github.com/kr/pretty v0.3.1/go.mod h1:hoEshYVHaxMs3cyo3Yncou5ZscifuDolrwPKZanG3xk=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/kylelemons/godebug v1.1.0 h1:RPNrshWIDI6G2gRW9EHilWtl7Z6Sb1BR0xunSBf0SNc=
github.com/kylelemons/godebug v1.1.0/go.mod h1:9/0rRGxNHcop5bhtWyNeEfOS8JIWk580+fNqagV/RAw=
github.com/matttproud/golang_protobuf_extensions v1.0.4 h1:mmDVorXM7PCGKw94cs5zkfA9PSy5pEvNWRP0ET0TIVo=
github.com/matttproud/golang_protobuf_extensions v1.0.4/go.mod h1:BSXmuO+STAnVfrANrmjBb36TMTDstsz7MSK+HVaYKv4=
github.com/minio/crc64nvme v1.0.2 h1:6uO1UxGAD+kwqWWp7mBFsi5gAse66C4NXO8cmcVculg=
github.com/minio/crc64nvme v1.0.2/go.mod h1:eVfm2fAzLlxMdUGc0EEBGSMmPwmXD5XiNRpnu9J3bvg=
github.com/minio/md5-simd v1.1.2 h1:Gdi1DZK69+ZVMoNHRXJyNcxrMA4dSxoYHZSQbirFg34=
github.com/minio/md5-simd v1.1.2/go.mod h1:MzdKDxYpY2BT9XQFocsiZf/NKVtR7nkE4RoEpN+20RM=
github.com/minio/minio-go/v7 v7.0.95 h1:ywOUPg+PebTMTzn9VDsoFJy32ZuARN9zhB+K3IYEvYU=
github.com/minio/minio-go/v7 v7.0.95/go.mod h1:wOOX3uxS334vImCNRVyIDdXX9OsXDm89ToynKgqUKlo=
github.com/mitchellh/mapstructure v1.4.3 h1:OVowDSCllw/YjdLkam3/sm7wEtOy59d8ndGgCcyj8cs=
github.com/mitchellh/mapstructure v1.4.3/go.mod h1:bFUtVrKA4DC2yAKiSyO/QUcy7e+RRV2QTWOzhPopBRo=
github.com/mozillazg/go-httpheader v0.2.1 h1:geV7TrjbL8KXSyvghnFm+NyTux/hxwueTSrwhe88TQQ=
github.com/mozillazg/go-httpheader v0.2.1/go.mod h1:jJ8xECTlalr6ValeXYdOF8fFUISeBAdw6E61aqQma60=
github.com/mwitkow/go-conntrack v0.0.0-20190716064945-2f068394615f h1:KUppIJq7/+SVif2QVs3tOP0zanoHgBEVAwHxUSIzRqU=
github.com/mwitkow/go-conntrack v0.0.0-20190716064945-2f068394615f/go.mod h1:qRWi+5nqEBWmkhHvq77mSJWrCKwh8bxhgT7d/eI7P4U=
github.com/ncw/swift v1.0.53 h1:luHjjTNtekIEvHg5KdAFIBaH7bWfNkefwFnpDffSIks=
github.com/ncw/swift v1.0.53/go.mod h1:23YIA4yWVnGwv2dQlN4bB7egfYX6YLn0Yo/S6zZO/ZM=
github.com/opentracing/opentracing-go v1.2.0 h1:uEJPy/1a5RIPAJ0Ov+OIO8OxWu77jEv+1B0VhjKrZUs=
github.com/opentracing/opentracing-go v1.2.0/go.mod h1:GxEUsuufX4nBwe+T+Wl9TAgYrxe9dPLANfrWvHYVTgc=
github.com/oracle/oci-go-sdk/v65 v65.41.1 h1:+lbosOyNiib3TGJDvLq1HwEAuFqkOjPJDIkyxM15WdQ=
github.com/oracle/oci-go-sdk/v65 v65.41.1/go.mod h1:MXMLMzHnnd9wlpgadPkdlkZ9YrwQmCOmbX5kjVEJodw=
github.com/philhofer/fwd v1.2.0 h1:e6DnBTl7vGY+Gz322/ASL4Gyp1FspeMvx1RNDoToZuM=
github.com/philhofer/fwd v1.2.0/go.mod h1:RqIHx9QI14HlwKwm98g9Re5prTQ6LdeRQn+gXJFxsJM=
github.com/pkg/browser v0.0.0-20240102092130-5ac0b6a4141c h1:+mdjkGKdHQG3305AYmdv1U2eRNDiU2ErMBj1gwrq8eQ=
github.com/pkg/browser v0.0.0-20240102092130-5ac0b6a4141c/go.mod h1:7rwL4CYBLnjLxUqIJNnCWiEdr3bn6IUYi15bNlnbCCU=
github.com/pkg/errors v0.9.1 h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=
github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/planetscale/vtprotobuf v0.6.1-0.20240319094008-0393e58bdf10 h1:GFCKgmp0tecUJ0sJuv4pzYCqS9+RGSn52M3FUwPs+uo=
github.com/planetscale/vtprotobuf v0.6.1-0.20240319094008-0393e58bdf10/go.mod h1:t/avpk3KcrXxUnYOhZhMXJlSEyie6gQbtLq5NM3loB8=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/prometheus/client_golang v1.17.0 h1:rl2sfwZMtSthVU752MqfjQozy7blglC+1SOtjMAMh+Q=
github.com/prometheus/client_golang v1.17.0/go.mod h1:VeL+gMmOAxkS2IqfCq0ZmHSL+LjWfWDUmp1mBz9JgUY=
github.com/prometheus/client_model v0.6.1 h1:ZKSh/rekM+n3CeS952MLRAdFwIKqeY8b62p8ais2e9E=
github.com/prometheus/client_model v0.6.1/go.mod h1:OrxVMOVHjw3lKMa8+x6HeMGkHMQyHDk9E3jmP2AmGiY=
github.com/prometheus/common v0.44.0 h1:+5BrQJwiBB9xsMygAB3TNvpQKOwlkc25LbISbrdOOfY=
github.com/prometheus/common v0.44.0/go.mod h1:ofAIvZbQ1e/nugmZGz4/qCb9Ap1VoSTIO7x0VV9VvuY=
github.com/prometheus/procfs v0.11.1 h1:xRC8Iq1yyca5ypa9n1EZnWZkt7dwcoRPQwX/5gwaUuI=
github.com/prometheus/procfs v0.11.1/go.mod h1:eesXgaPo1q7lBpVMoMy0ZOFTth9hBn4W/y0/p/ScXhY=
github.com/redis/go-redis/v9 v9.8.0 h1:q3nRvjrlge/6UD7eTu/DSg2uYiU2mCL0G/uzBWqhicI=
github.com/redis/go-redis/v9 v9.8.0/go.mod h1:huWgSWd8mW6+m0VPhJjSSQ+d6Nh1VICQ6Q5lHuCH/Iw=
github.com/rogpeppe/go-internal v1.13.1 h1:KvO1DLK/DRN07sQ1LQKScxyZJuNnedQ5/wKSR38lUII=
github.com/rogpeppe/go-internal v1.13.1/go.mod h1:uMEvuHeurkdAXX61udpOXGD/AzZDWNMNyH2VO9fmH0o=
github.com/rs/xid v1.6.0 h1:fV591PaemRlL6JfRxGDEPl69wICngIQ3shQtzfy2gxU=
github.com/rs/xid v1.6.0/go.mod h1:7XoLgs4eV+QndskICGsho+ADou8ySMSjJKDIan90Nz0=
github.com/satori/go.uuid v1.2.1-0.20181028125025-b2ce2384e17b h1:gQZ0qzfKHQIybLANtM3mBXNUtOfsCFXeTsnBqCsx1KM=
github.com/satori/go.uuid v1.2.1-0.20181028125025-b2ce2384e17b/go.mod h1:dA0hQrYB0VpLJoorglMZABFdXlWrHn1NEOzdhQKdks0=
github.com/sony/gobreaker v0.5.0 h1:dRCvqm0P490vZPmy7ppEk2qCnCieBooFJ+YoXGYB+yg=
github.com/sony/gobreaker v0.5.0/go.mod h1:ZKptC7FHNvhBz7dN2LGjPVBz2sZJmc0/PkyDJOjmxWY=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.5.2 h1:xuMeJ0Sdp5ZMRXx/aWO6RZxdr3beISkG5/G/aIRr3pY=
github.com/stretchr/objx v0.5.2/go.mod h1:FRsXN1f5AsAjCGJKqEizvkpNtU+EGNCLh3NxZ/8L+MA=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
github.com/stretchr/testify v1.6.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.10.0 h1:Xv5erBjTwe/5IxqUQTdXv5kgmIvbHo3QQyRwhJsOfJA=
github.com/stretchr/testify v1.10.0/go.mod h1:r2ic/lqez/lEtzL7wO/rwa5dbSLXVDPFyf8C91i36aY=
github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common v1.0.194/go.mod h1:7sCQWVkxcsR38nffDW057DRGk8mUjK1Ing/EFOK8s8Y=
github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/kms v1.0.194/go.mod h1:yrBKWhChnDqNz1xuXdSbWXG56XawEq0G5j1lg4VwBD4=
github.com/tencentyun/cos-go-sdk-v5 v0.7.40 h1:W6vDGKCHe4wBACI1d2UgE6+50sJFhRWU4O8IB2ozzxM=
github.com/tencentyun/cos-go-sdk-v5 v0.7.40/go.mod h1:4dCEtLHGh8QPxHEkgq+nFaky7yZxQuYwgSJM87icDaw=
github.com/tinylib/msgp v1.3.0 h1:ULuf7GPooDaIlbyvgAxBV/FI7ynli6LZ1/nVUNu+0ww=
github.com/tinylib/msgp v1.3.0/go.mod h1:ykjzy2wzgrlvpDCRc4LA8UXy6D8bzMSuAF3WD57Gok0=
go.opentelemetry.io/auto/sdk v1.1.0 h1:cH53jehLUN6UFLY71z+NDOiNJqDdPRaXzTel0sJySYA=
go.opentelemetry.io/auto/sdk v1.1.0/go.mod h1:3wSPjt5PWp2RhlCcmmOial7AvC4DQqZb7a7wCow3W8A=
go.opentelemetry.io/contrib/detectors/gcp v1.34.0 h1:JRxssobiPg23otYU5SbWtQC//snGVIM3Tx6QRzlQBao=
go.opentelemetry.io/contrib/detectors/gcp v1.34.0/go.mod h1:cV4BMFcscUR/ckqLkbfQmF0PRsq8w/lMGzdbCSveBHo=
go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc v0.59.0 h1:rgMkmiGfix9vFJDcDi1PK8WEQP4FLQwLDfhp5ZLpFeE=
go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc v0.59.0/go.mod h1:ijPqXp5P6IRRByFVVg9DY8P5HkxkHE5ARIa+86aXPf4=
go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp v0.59.0 h1:CV7UdSGJt/Ao6Gp4CXckLxVRRsRgDHoI8XjbL3PDl8s=
go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp v0.59.0/go.mod h1:FRmFuRJfag1IZ2dPkHnEoSFVgTVPUd2qf5Vi69hLb8I=
go.opentelemetry.io/otel v1.34.0 h1:zRLXxLCgL1WyKsPVrgbSdMN4c0FMkDAskSTQP+0hdUY=
go.opentelemetry.io/otel v1.34.0/go.mod h1:OWFPOQ+h4G8xpyjgqo4SxJYdDQ/qmRH+wivy7zzx9oI=
go.opentelemetry.io/otel/exporters/stdout/stdoutmetric v1.29.0 h1:WDdP9acbMYjbKIyJUhTvtzj601sVJOqgWdUxSdR/Ysc=
go.opentelemetry.io/otel/exporters/stdout/stdoutmetric v1.29.0/go.mod h1:BLbf7zbNIONBLPwvFnwNHGj4zge8uTCM/UPIVW1Mq2I=
go.opentelemetry.io/otel/metric v1.34.0 h1:+eTR3U0MyfWjRDhmFMxe2SsW64QrZ84AOhvqS7Y+PoQ=
go.opentelemetry.io/otel/metric v1.34.0/go.mod h1:CEDrp0fy2D0MvkXE+dPV7cMi8tWZwX3dmaIhwPOaqHE=
go.opentelemetry.io/otel/sdk v1.34.0 h1:95zS4k/2GOy069d321O8jWgYsW3MzVV+KuSPKp7Wr1A=
go.opentelemetry.io/otel/sdk v1.34.0/go.mod h1:0e/pNiaMAqaykJGKbi+tSjWfNNHMTxoC9qANsCzbyxU=
go.opentelemetry.io/otel/sdk/metric v1.34.0 h1:5CeK9ujjbFVL5c1PhLuStg1wxA7vQv7ce1EK0Gyvahk=
go.opentelemetry.io/otel/sdk/metric v1.34.0/go.mod h1:jQ/r8Ze28zRKoNRdkjCZxfs6YvBTG1+YIqyFVFYec5w=
go.opentelemetry.io/otel/trace v1.34.0 h1:+ouXS2V8Rd4hp4580a8q23bg0azF2nI8cqLYnC8mh/k=
go.opentelemetry.io/otel/trace v1.34.0/go.mod h1:Svm7lSjQD7kG7KJ/MUHPVXSDGz2OX4h0M2jHBhmSfRE=
go.uber.org/atomic v1.9.0 h1:ECmE8Bn/WFTYwEW/bpKD3M8VtR/zQVbavAoalC1PYyE=
go.uber.org/atomic v1.9.0/go.mod h1:fEN4uk6kAWBTFdckzkM89CLk9XfWZrxpCo0nPH17wJc=
golang.org/x/crypto v0.39.0 h1:SHs+kF4LP+f+p14esP5jAoDpHU8Gu/v9lFRK6IT5imM=
golang.org/x/crypto v0.39.0/go.mod h1:L+Xg3Wf6HoL4Bn4238Z6ft6KfEpN0tJGo53AAPC632U=
golang.org/x/net v0.41.0 h1:vBTly1HeNPEn3wtREYfy4GZ/NECgw2Cnl+nK6Nz3uvw=
golang.org/x/net v0.41.0/go.mod h1:B/K4NNqkfmg07DQYrbwvSluqCJOOXwUjeb/5lOisjbA=
golang.org/x/oauth2 v0.30.0 h1:dnDm7JmhM45NNpd8FDDeLhK6FwqbOf4MLCM9zb1BOHI=
golang.org/x/oauth2 v0.30.0/go.mod h1:B++QgG3ZKulg6sRPGD/mqlHQs5rB3Ml9erfeDY7xKlU=
golang.org/x/sync v0.0.0-20181221193216-37e7f081c4d4/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.15.0 h1:KWH3jNZsfyT6xfAfKiz6MRNmd46ByHDYaZ7KSkCtdW8=
golang.org/x/sync v0.15.0/go.mod h1:1dzgHSNfp02xaA81J2MS99Qcpr2w7fw1gpm99rleRqA=
golang.org/x/sys v0.1.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.6.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.33.0 h1:q3i8TbbEz+JRD9ywIRlyRAQbM0qF7hu24q3teo2hbuw=
golang.org/x/sys v0.33.0/go.mod h1:BJP2sWEmIv4KK5OTEluFJCKSidICx8ciO85XgH3Ak8k=
golang.org/x/text v0.26.0 h1:P42AVeLghgTYr4+xUnTRKDMqpar+PtX7KWuNQL21L8M=
golang.org/x/text v0.26.0/go.mod h1:QK15LZJUUQVJxhz7wXgxSy/CJaTFjd0G+YLonydOVQA=
golang.org/x/time v0.10.0 h1:3usCWA8tQn0L8+hFJQNgzpWbd89begxN66o1Ojdn5L4=
golang.org/x/time v0.10.0/go.mod h1:3BpzKBy/shNhVucY/MWOyx10tF3SFh9QdLuxbVysPQM=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
google.golang.org/api v0.220.0 h1:3oMI4gdBgB72WFVwE1nerDD8W3HUOS4kypK6rRLbGns=
google.golang.org/api v0.220.0/go.mod h1:26ZAlY6aN/8WgpCzjPNy18QpYaz7Zgg1h0qe1GkZEmY=
google.golang.org/genproto v0.0.0-20250204164813-702378808489 h1:nQcbCCOg2h2CQ0yA8SY3AHqriNKDvsetuq9mE/HFjtc=
google.golang.org/genproto v0.0.0-20250204164813-702378808489/go.mod h1:wkQ2Aj/xvshAUDtO/JHvu9y+AaN9cqs28QuSVSHtZSY=
google.golang.org/genproto/googleapis/api v0.0.0-20250204164813-702378808489 h1:fCuMM4fowGzigT89NCIsW57Pk9k2D12MMi2ODn+Nk+o=
google.golang.org/genproto/googleapis/api v0.0.0-20250204164813-702378808489/go.mod h1:iYONQfRdizDB8JJBybql13nArx91jcUk7zCXEsOofM4=
google.golang.org/genproto/googleapis/rpc v0.0.0-20250204164813-702378808489 h1:5bKytslY8ViY0Cj/ewmRtrWHW64bNF03cAatUUFCdFI=
google.golang.org/genproto/googleapis/rpc v0.0.0-20250204164813-702378808489/go.mod h1:8BS3B93F/U1juMFq9+EDk+qOT5CO1R9IzXxG3PTqiRk=
google.golang.org/grpc v1.70.0 h1:pWFv03aZoHzlRKHWicjsZytKAiYCtNS0dHbXnIdq7jQ=
google.golang.org/grpc v1.70.0/go.mod h1:ofIJqVKDXx/JiXrwr2IG4/zwdH9txy3IlF40RmcJSQw=
google.golang.org/protobuf v1.36.4 h1:6A3ZDJHn/eNqc1i+IdefRzy/9PokBTPvcqMySR7NNIM=
google.golang.org/protobuf v1.36.4/go.mod h1:9fA7Ob0pmnwhb644+1+CVWFRbNajQ6iRojtC/QF5bRE=
gopkg.in/alecthomas/kingpin.v2 v2.2.6 h1:jMFz6MfLP0/4fUyZle81rXUoxOBFi19VUFKVDOQfozc=
gopkg.in/alecthomas/kingpin.v2 v2.2.6/go.mod h1:FMv+mEhP44yOT+4EoQTLFTRgOQ1FBLkstjWtayDeSgw=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.4.0 h1:D8xgwECY7CYvx+Y2n4sBz93Jn9JRvxdiyyo8CTfuKaY=
gopkg.in/yaml.v2 v2.4.0/go.mod h1:RDklbk79AGWmwhnvt/jBztapEOGDOx6ZbXqjP6csGnQ=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gotest.tools/v3 v3.5.1 h1:EENdUnS3pdur5nybKYIh2Vfgc8IUNBjxDPSjtiJcOzU=
gotest.tools/v3 v3.5.1/go.mod h1:isy3WKz7GK6uNw/sbHzfKBLvlvXwUyV06n6brMxxopU=
```

## File: `inmem.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package objstore

import (
	"bytes"
	"context"
	"io"
	"sort"
	"strings"
	"sync"
	"time"

	"github.com/pkg/errors"
)

var errNotFound = errors.New("inmem: object not found")

// InMemBucket implements the objstore.Bucket interfaces against local memory.
// Methods from Bucket interface are thread-safe. Objects are assumed to be immutable.
type InMemBucket struct {
	mtx     sync.RWMutex
	objects map[string][]byte
	attrs   map[string]ObjectAttributes
}

// NewInMemBucket returns a new in memory Bucket.
// NOTE: Returned bucket is just a naive in memory bucket implementation. For test use cases only.
func NewInMemBucket() *InMemBucket {
	return &InMemBucket{
		objects: map[string][]byte{},
		attrs:   map[string]ObjectAttributes{},
	}
}

// ChangeLastModified changes the last modified timestamp of the object at the given path.
// If the object does not exist, it returns an error.
// This method is useful for testing purposes to simulate updates to objects.
func (b *InMemBucket) ChangeLastModified(path string, lastModified time.Time) error {
	b.mtx.Lock()
	defer b.mtx.Unlock()

	if _, ok := b.objects[path]; !ok {
		return errNotFound
	}

	attrs := b.attrs[path]
	attrs.LastModified = lastModified
	b.attrs[path] = attrs

	return nil
}

func (b *InMemBucket) Provider() ObjProvider { return MEMORY }

// Objects returns a copy of the internally stored objects.
// NOTE: For assert purposes.
func (b *InMemBucket) Objects() map[string][]byte {
	b.mtx.RLock()
	defer b.mtx.RUnlock()

	objs := make(map[string][]byte)
	for k, v := range b.objects {
		objs[k] = v
	}

	return objs
}

func (b *InMemBucket) genericIter(_ context.Context, dir string, f func(string, time.Time) error, options ...IterOption) error {
	unique := map[string]struct{}{}
	lastModified := map[string]time.Time{}
	params := ApplyIterOptions(options...)

	var dirPartsCount int
	dirParts := strings.SplitAfter(dir, DirDelim)
	for _, p := range dirParts {
		if p == "" {
			continue
		}
		dirPartsCount++
	}

	b.mtx.RLock()
	for filename := range b.objects {
		if !strings.HasPrefix(filename, dir) || dir == filename {
			continue
		}

		if params.Recursive {
			// Any object matching the prefix should be included.
			unique[filename] = struct{}{}
			lastModified[filename] = b.attrs[filename].LastModified
			continue
		}

		parts := strings.SplitAfter(filename, DirDelim)

		name := strings.Join(parts[:dirPartsCount+1], "")
		unique[name] = struct{}{}

		if params.LastModified {
			lastModified[name] = b.attrs[filename].LastModified
		}
	}
	b.mtx.RUnlock()

	var keys []string
	for n := range unique {
		keys = append(keys, n)
	}
	sort.Slice(keys, func(i, j int) bool {
		if strings.HasSuffix(keys[i], DirDelim) && strings.HasSuffix(keys[j], DirDelim) {
			return strings.Compare(keys[i], keys[j]) < 0
		}
		if strings.HasSuffix(keys[i], DirDelim) {
			return false
		}
		if strings.HasSuffix(keys[j], DirDelim) {
			return true
		}

		return strings.Compare(keys[i], keys[j]) < 0
	})

	for _, k := range keys {
		var modifiedTS time.Time
		if params.LastModified {
			modifiedTS = lastModified[k]
		}
		if err := f(k, modifiedTS); err != nil {
			return err
		}
	}
	return nil
}

// Iter calls f for each entry in the given directory. The argument to f is the full
// object name including the prefix of the inspected directory.
func (b *InMemBucket) Iter(_ context.Context, dir string, f func(string) error, options ...IterOption) error {
	return b.genericIter(context.Background(), dir, func(s string, t time.Time) error {
		return f(s)
	}, options...)
}

func (i *InMemBucket) SupportedIterOptions() []IterOptionType {
	return []IterOptionType{Recursive, UpdatedAt}
}

func (b *InMemBucket) IterWithAttributes(ctx context.Context, dir string, f func(attrs IterObjectAttributes) error, options ...IterOption) error {
	if err := ValidateIterOptions(b.SupportedIterOptions(), options...); err != nil {
		return err
	}

	return b.genericIter(context.Background(), dir, func(s string, t time.Time) error {
		attrs := IterObjectAttributes{Name: s}
		attrs.SetLastModified(t)

		return f(attrs)
	}, options...)
}

// Get returns a reader for the given object name.
func (b *InMemBucket) Get(_ context.Context, name string) (io.ReadCloser, error) {
	if name == "" {
		return nil, errors.New("inmem: object name is empty")
	}

	b.mtx.RLock()
	file, ok := b.objects[name]
	b.mtx.RUnlock()
	if !ok {
		return nil, errNotFound
	}

	return ObjectSizerReadCloser{
		ReadCloser: io.NopCloser(bytes.NewReader(file)),
		Size: func() (int64, error) {
			return int64(len(file)), nil
		},
	}, nil
}

// GetRange returns a new range reader for the given object name and range.
func (b *InMemBucket) GetRange(_ context.Context, name string, off, length int64) (io.ReadCloser, error) {
	if name == "" {
		return nil, errors.New("inmem: object name is empty")
	}

	b.mtx.RLock()
	file, ok := b.objects[name]
	b.mtx.RUnlock()
	if !ok {
		return nil, errNotFound
	}

	if int64(len(file)) < off {
		return ObjectSizerReadCloser{
			ReadCloser: io.NopCloser(bytes.NewReader(nil)),
			Size:       func() (int64, error) { return 0, nil },
		}, nil
	}

	if length == -1 {
		return ObjectSizerReadCloser{
			ReadCloser: io.NopCloser(bytes.NewReader(file[off:])),
			Size: func() (int64, error) {
				return int64(len(file[off:])), nil
			},
		}, nil
	}

	if length <= 0 {
		// wrap with ObjectSizerReadCloser to return 0 size.
		return ObjectSizerReadCloser{
			ReadCloser: io.NopCloser(bytes.NewReader(nil)),
			Size:       func() (int64, error) { return 0, nil },
		}, errors.New("length cannot be smaller or equal 0")
	}

	if int64(len(file)) <= off+length {
		// Just return maximum of what we have.
		length = int64(len(file)) - off
	}

	return ObjectSizerReadCloser{
		ReadCloser: io.NopCloser(bytes.NewReader(file[off : off+length])),
		Size: func() (int64, error) {
			return length, nil
		},
	}, nil
}

// Exists checks if the given directory exists in memory.
func (b *InMemBucket) Exists(_ context.Context, name string) (bool, error) {
	b.mtx.RLock()
	defer b.mtx.RUnlock()
	_, ok := b.objects[name]
	return ok, nil
}

// Attributes returns information about the specified object.
func (b *InMemBucket) Attributes(_ context.Context, name string) (ObjectAttributes, error) {
	b.mtx.RLock()
	attrs, ok := b.attrs[name]
	b.mtx.RUnlock()
	if !ok {
		return ObjectAttributes{}, errNotFound
	}
	return attrs, nil
}

// Upload writes the file specified in src to into the memory.
func (b *InMemBucket) Upload(_ context.Context, name string, r io.Reader, _ ...ObjectUploadOption) error {
	b.mtx.Lock()
	defer b.mtx.Unlock()
	body, err := io.ReadAll(r)
	if err != nil {
		return err
	}
	b.objects[name] = body
	b.attrs[name] = ObjectAttributes{
		Size:         int64(len(body)),
		LastModified: time.Now(),
	}
	return nil
}

// Delete removes all data prefixed with the dir.
func (b *InMemBucket) Delete(_ context.Context, name string) error {
	b.mtx.Lock()
	defer b.mtx.Unlock()
	if _, ok := b.objects[name]; !ok {
		return errNotFound
	}
	delete(b.objects, name)
	delete(b.attrs, name)
	return nil
}

// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
func (b *InMemBucket) IsObjNotFoundErr(err error) bool {
	return errors.Is(err, errNotFound)
}

// IsAccessDeniedErr returns true if access to object is denied.
func (b *InMemBucket) IsAccessDeniedErr(err error) bool {
	return false
}

func (b *InMemBucket) Close() error { return nil }

// Name returns the bucket name.
func (b *InMemBucket) Name() string {
	return "inmem"
}
```

## File: `inmem_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package objstore

import (
	"context"
	"strings"
	"testing"

	"github.com/efficientgo/core/testutil"
)

func TestInMem_ReturnsModifiedInIterAttributes(t *testing.T) {
	b := NewInMemBucket()
	testutil.Ok(t, b.Upload(context.Background(), "test/file1.txt", strings.NewReader("test-data1")))

	var itemsIterated int

	testutil.Ok(t, b.IterWithAttributes(context.Background(), "", func(attrs IterObjectAttributes) error {
		testutil.Equals(t, "test/", attrs.Name)
		ts, ok := attrs.LastModified()
		testutil.Equals(t, true, ok)
		testutil.Assert(t, !ts.IsZero(), "expected LastModified to be not zero")
		itemsIterated++

		return nil
	}, WithUpdatedAt()))

	testutil.Ok(t, b.IterWithAttributes(context.Background(), "", func(attrs IterObjectAttributes) error {
		testutil.Equals(t, "test/file1.txt", attrs.Name)

		ts, ok := attrs.LastModified()
		testutil.Equals(t, true, ok)
		testutil.Assert(t, !ts.IsZero(), "expected LastModified to be not zero")

		itemsIterated++

		return nil
	}, WithRecursiveIter(), WithUpdatedAt()))

	testutil.Equals(t, 2, itemsIterated)
}
```

## File: `objstore.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package objstore

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"io/fs"
	"os"
	"path"
	"path/filepath"
	"slices"
	"strings"
	"sync"
	"time"

	"github.com/efficientgo/core/logerrcapture"
	"github.com/go-kit/log"
	"github.com/go-kit/log/level"
	"github.com/pkg/errors"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"golang.org/x/sync/errgroup"
)

type ObjProvider string

const (
	MEMORY     ObjProvider = "MEMORY"
	FILESYSTEM ObjProvider = "FILESYSTEM"
	GCS        ObjProvider = "GCS"
	S3         ObjProvider = "S3"
	AZURE      ObjProvider = "AZURE"
	SWIFT      ObjProvider = "SWIFT"
	COS        ObjProvider = "COS"
	ALIYUNOSS  ObjProvider = "ALIYUNOSS"
	BOS        ObjProvider = "BOS"
	OCI        ObjProvider = "OCI"
	OBS        ObjProvider = "OBS"
)

const (
	OpIter       = "iter"
	OpGet        = "get"
	OpGetRange   = "get_range"
	OpExists     = "exists"
	OpUpload     = "upload"
	OpDelete     = "delete"
	OpAttributes = "attributes"
)

// Bucket provides read and write access to an object storage bucket.
// NOTE: We assume strong consistency for write-read flow.
type Bucket interface {
	io.Closer
	BucketReader

	Provider() ObjProvider

	// Upload the contents of the reader as an object into the bucket.
	// Upload should be idempotent.
	Upload(ctx context.Context, name string, r io.Reader, opts ...ObjectUploadOption) error

	// Delete removes the object with the given name.
	// If object does not exist in the moment of deletion, Delete should throw error.
	Delete(ctx context.Context, name string) error

	// Name returns the bucket name for the provider.
	Name() string
}

// InstrumentedBucket is a Bucket with optional instrumentation control on reader.
type InstrumentedBucket interface {
	Bucket

	// WithExpectedErrs allows to specify a filter that marks certain errors as expected, so it will not increment
	// objstore_bucket_operation_failures_total metric.
	WithExpectedErrs(IsOpFailureExpectedFunc) Bucket

	// ReaderWithExpectedErrs allows to specify a filter that marks certain errors as expected, so it will not increment
	// objstore_bucket_operation_failures_total metric.
	// TODO(bwplotka): Remove this when moved to Go 1.14 and replace with InstrumentedBucketReader.
	ReaderWithExpectedErrs(IsOpFailureExpectedFunc) BucketReader
}

// BucketReader provides read access to an object storage bucket.
type BucketReader interface {
	// Iter calls f for each entry in the given directory (not recursive.). The argument to f is the full
	// object name including the prefix of the inspected directory.

	// Entries are passed to function in sorted order.
	Iter(ctx context.Context, dir string, f func(name string) error, options ...IterOption) error

	// IterWithAttributes calls f for each entry in the given directory similar to Iter.
	// In addition to Name, it also includes requested object attributes in the argument to f.
	//
	// Attributes can be requested using IterOption.
	// Not all IterOptions are supported by all providers, requesting for an unsupported option will fail with ErrOptionNotSupported.
	IterWithAttributes(ctx context.Context, dir string, f func(attrs IterObjectAttributes) error, options ...IterOption) error

	// SupportedIterOptions returns a list of supported IterOptions by the underlying provider.
	SupportedIterOptions() []IterOptionType

	// Get returns a reader for the given object name.
	Get(ctx context.Context, name string) (io.ReadCloser, error)

	// GetRange returns a new range reader for the given object name and range.
	GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error)

	// Exists checks if the given object exists in the bucket.
	Exists(ctx context.Context, name string) (bool, error)

	// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
	IsObjNotFoundErr(err error) bool

	// IsAccessDeniedErr returns true if access to object is denied.
	IsAccessDeniedErr(err error) bool

	// Attributes returns information about the specified object.
	Attributes(ctx context.Context, name string) (ObjectAttributes, error)
}

// InstrumentedBucketReader is a BucketReader with optional instrumentation control.
type InstrumentedBucketReader interface {
	BucketReader

	// ReaderWithExpectedErrs allows to specify a filter that marks certain errors as expected, so it will not increment
	// objstore_bucket_operation_failures_total metric.
	ReaderWithExpectedErrs(IsOpFailureExpectedFunc) BucketReader
}

var ErrOptionNotSupported = errors.New("iter option is not supported")

// IterOptionType is used for type-safe option support checking.
type IterOptionType int

const (
	Recursive IterOptionType = iota
	UpdatedAt
)

// IterOption configures the provided params.
type IterOption struct {
	Type  IterOptionType
	Apply func(params *IterParams)
}

// WithRecursiveIter is an option that can be applied to Iter() to recursively list objects
// in the bucket.
func WithRecursiveIter() IterOption {
	return IterOption{
		Type: Recursive,
		Apply: func(params *IterParams) {
			params.Recursive = true
		},
	}
}

// WithUpdatedAt is an option that can be applied to Iter() to
// include the last modified time in the attributes.
// NB: Prefixes may not report last modified time.
// This option is currently supported for the azure, s3, bos, gcs and filesystem providers.
func WithUpdatedAt() IterOption {
	return IterOption{
		Type: UpdatedAt,
		Apply: func(params *IterParams) {
			params.LastModified = true
		},
	}
}

// IterParams holds the Iter() parameters and is used by objstore clients implementations.
type IterParams struct {
	Recursive    bool
	LastModified bool
}

func ValidateIterOptions(supportedOptions []IterOptionType, options ...IterOption) error {
	for _, opt := range options {
		if !slices.Contains(supportedOptions, opt.Type) {
			return fmt.Errorf("%w: %v", ErrOptionNotSupported, opt.Type)
		}
	}

	return nil
}

func ApplyIterOptions(options ...IterOption) IterParams {
	out := IterParams{}
	for _, opt := range options {
		opt.Apply(&out)
	}
	return out
}

type UploadObjectParams struct {
	ContentType string
}

type ObjectUploadOption func(f *UploadObjectParams)

func WithContentType(contentType string) ObjectUploadOption {
	return func(f *UploadObjectParams) {
		f.ContentType = contentType
	}
}

func ApplyObjectUploadOptions(opts ...ObjectUploadOption) UploadObjectParams {
	out := UploadObjectParams{}
	for _, opt := range opts {
		opt(&out)
	}
	return out
}

// DownloadOption configures the provided params.
type DownloadOption func(params *downloadParams)

// downloadParams holds the DownloadDir() parameters and is used by objstore clients implementations.
type downloadParams struct {
	concurrency  int
	ignoredPaths []string
}

// WithDownloadIgnoredPaths is an option to set the paths to not be downloaded.
func WithDownloadIgnoredPaths(ignoredPaths ...string) DownloadOption {
	return func(params *downloadParams) {
		params.ignoredPaths = ignoredPaths
	}
}

// WithFetchConcurrency is an option to set the concurrency of the download operation.
func WithFetchConcurrency(concurrency int) DownloadOption {
	return func(params *downloadParams) {
		params.concurrency = concurrency
	}
}

func applyDownloadOptions(options ...DownloadOption) downloadParams {
	out := downloadParams{
		concurrency: 1,
	}
	for _, opt := range options {
		opt(&out)
	}
	return out
}

// UploadOption configures the provided params.
type UploadOption func(params *uploadParams)

// uploadParams holds the UploadDir() parameters and is used by objstore clients implementations.
type uploadParams struct {
	concurrency int
}

// WithUploadConcurrency is an option to set the concurrency of the upload operation.
func WithUploadConcurrency(concurrency int) UploadOption {
	return func(params *uploadParams) {
		params.concurrency = concurrency
	}
}

func applyUploadOptions(options ...UploadOption) uploadParams {
	out := uploadParams{
		concurrency: 1,
	}
	for _, opt := range options {
		opt(&out)
	}
	return out
}

type ObjectAttributes struct {
	// Size is the object size in bytes.
	Size int64 `json:"size"`

	// LastModified is the timestamp the object was last modified.
	LastModified time.Time `json:"last_modified"`
}

type IterObjectAttributes struct {
	Name         string
	lastModified time.Time
}

func (i *IterObjectAttributes) SetLastModified(t time.Time) {
	i.lastModified = t
}

// LastModified returns the timestamp the object was last modified. Returns false if the timestamp is not available.
func (i *IterObjectAttributes) LastModified() (time.Time, bool) {
	return i.lastModified, !i.lastModified.IsZero()
}

// TryToGetSize tries to get upfront size from reader.
// Some implementations may return only size of unread data in the reader, so it's best to call this method before
// doing any reading.
//
// TODO(https://github.com/thanos-io/thanos/issues/678): Remove guessing length when minio provider will support multipart upload without this.
func TryToGetSize(r io.Reader) (int64, error) {
	switch f := r.(type) {
	case *os.File:
		fileInfo, err := f.Stat()
		if err != nil {
			return 0, errors.Wrap(err, "os.File.Stat()")
		}
		return fileInfo.Size(), nil
	case *bytes.Buffer:
		return int64(f.Len()), nil
	case *bytes.Reader:
		// Returns length of unread data only.
		return int64(f.Len()), nil
	case *strings.Reader:
		return f.Size(), nil
	case ObjectSizer:
		return f.ObjectSize()
	case *io.LimitedReader:
		return f.N, nil
	}
	return 0, errors.Errorf("unsupported type of io.Reader: %T", r)
}

// ObjectSizer can return size of object.
type ObjectSizer interface {
	// ObjectSize returns the size of the object in bytes, or error if it is not available.
	ObjectSize() (int64, error)
}

type nopCloserWithObjectSize struct{ io.Reader }

func (nopCloserWithObjectSize) Close() error                 { return nil }
func (n nopCloserWithObjectSize) ObjectSize() (int64, error) { return TryToGetSize(n.Reader) }

// NopCloserWithSize returns a ReadCloser with a no-op Close method wrapping
// the provided Reader r. Returned ReadCloser also implements Size method.
func NopCloserWithSize(r io.Reader) io.ReadCloser {
	return nopCloserWithObjectSize{r}
}

// UploadDir uploads all files in srcdir to the bucket with into a top-level directory
// named dstdir. It is a caller responsibility to clean partial upload in case of failure.
func UploadDir(ctx context.Context, logger log.Logger, bkt Bucket, srcdir, dstdir string, options ...UploadOption) error {
	df, err := os.Stat(srcdir)
	opts := applyUploadOptions(options...)

	// The derived Context is canceled the first time a function passed to Go returns a non-nil error or the first
	// time Wait returns, whichever occurs first.
	g, ctx := errgroup.WithContext(ctx)
	g.SetLimit(opts.concurrency)

	if err != nil {
		return errors.Wrap(err, "stat dir")
	}
	if !df.IsDir() {
		return errors.Errorf("%s is not a directory", srcdir)
	}
	err = filepath.WalkDir(srcdir, func(src string, d fs.DirEntry, err error) error {
		g.Go(func() error {
			if err != nil {
				return err
			}
			if d.IsDir() {
				return nil
			}
			srcRel, err := filepath.Rel(srcdir, src)
			if err != nil {
				return errors.Wrap(err, "getting relative path")
			}

			dst := path.Join(dstdir, filepath.ToSlash(srcRel))
			return UploadFile(ctx, logger, bkt, src, dst)
		})

		return nil
	})

	if err == nil {
		err = g.Wait()
	}

	return err
}

// UploadFile uploads the file with the given name to the bucket.
// It is a caller responsibility to clean partial upload in case of failure.
func UploadFile(ctx context.Context, logger log.Logger, bkt Bucket, src, dst string) error {
	r, err := os.Open(filepath.Clean(src))
	if err != nil {
		return errors.Wrapf(err, "open file %s", src)
	}
	defer logerrcapture.Do(logger, r.Close, "close file %s", src)

	if err := bkt.Upload(ctx, dst, r); err != nil {
		return errors.Wrapf(err, "upload file %s as %s", src, dst)
	}
	level.Debug(logger).Log("msg", "uploaded file", "from", src, "dst", dst, "bucket", bkt.Name())
	return nil
}

// DirDelim is the delimiter used to model a directory structure in an object store bucket.
const DirDelim = "/"

// DownloadFile downloads the src file from the bucket to dst. If dst is an existing
// directory, a file with the same name as the source is created in dst.
// If destination file is already existing, download file will overwrite it.
func DownloadFile(ctx context.Context, logger log.Logger, bkt BucketReader, src, dst string) (err error) {
	if fi, err := os.Stat(dst); err == nil {
		if fi.IsDir() {
			dst = filepath.Join(dst, filepath.Base(src))
		}
	} else if !os.IsNotExist(err) {
		return err
	}

	rc, err := bkt.Get(ctx, src)
	if err != nil {
		return errors.Wrapf(err, "get file %s", src)
	}
	defer logerrcapture.Do(logger, rc.Close, "close block's file reader")

	f, err := os.Create(dst)
	if err != nil {
		return errors.Wrapf(err, "create file %s", dst)
	}
	defer func() {
		if err != nil {
			if rerr := os.Remove(dst); rerr != nil {
				level.Warn(logger).Log("msg", "failed to remove partially downloaded file", "file", dst, "err", rerr)
			}
		}
	}()
	defer logerrcapture.Do(logger, f.Close, "close block's output file")

	if _, err = io.Copy(f, rc); err != nil {
		return errors.Wrapf(err, "copy object to file %s", src)
	}
	return nil
}

// DownloadDir downloads all object found in the directory into the local directory.
func DownloadDir(ctx context.Context, logger log.Logger, bkt BucketReader, originalSrc, src, dst string, options ...DownloadOption) error {
	if err := os.MkdirAll(dst, 0750); err != nil {
		return errors.Wrap(err, "create dir")
	}
	opts := applyDownloadOptions(options...)

	// The derived Context is canceled the first time a function passed to Go returns a non-nil error or the first
	// time Wait returns, whichever occurs first.
	g, ctx := errgroup.WithContext(ctx)
	g.SetLimit(opts.concurrency)

	var downloadedFiles []string
	var m sync.Mutex

	err := bkt.Iter(ctx, src, func(name string) error {
		g.Go(func() error {
			dst := filepath.Join(dst, filepath.Base(name))
			if strings.HasSuffix(name, DirDelim) {
				if err := DownloadDir(ctx, logger, bkt, originalSrc, name, dst, options...); err != nil {
					return err
				}
				m.Lock()
				downloadedFiles = append(downloadedFiles, dst)
				m.Unlock()
				return nil
			}
			for _, ignoredPath := range opts.ignoredPaths {
				if ignoredPath == strings.TrimPrefix(name, string(originalSrc)+DirDelim) {
					level.Debug(logger).Log("msg", "not downloading again because a provided path matches this one", "file", name)
					return nil
				}
			}
			if err := DownloadFile(ctx, logger, bkt, name, dst); err != nil {
				return err
			}

			m.Lock()
			downloadedFiles = append(downloadedFiles, dst)
			m.Unlock()
			return nil
		})
		return nil
	})

	if err == nil {
		err = g.Wait()
	}

	if err != nil {
		downloadedFiles = append(downloadedFiles, dst) // Last, clean up the root dst directory.
		// Best-effort cleanup if the download failed.
		for _, f := range downloadedFiles {
			if rerr := os.RemoveAll(f); rerr != nil {
				level.Warn(logger).Log("msg", "failed to remove file on partial dir download error", "file", f, "err", rerr)
			}
		}
		return err
	}

	return nil
}

// IsOpFailureExpectedFunc allows to mark certain errors as expected, so they will not increment objstore_bucket_operation_failures_total metric.
type IsOpFailureExpectedFunc func(error) bool

var _ InstrumentedBucket = &metricBucket{}

func BucketMetrics(reg prometheus.Registerer, name string) *Metrics {
	return &Metrics{
		isOpFailureExpected: func(err error) bool { return false },
		ops: promauto.With(reg).NewCounterVec(prometheus.CounterOpts{
			Name:        "objstore_bucket_operations_total",
			Help:        "Total number of all attempted operations against a bucket.",
			ConstLabels: prometheus.Labels{"bucket": name},
		}, []string{"operation"}),

		opsFailures: promauto.With(reg).NewCounterVec(prometheus.CounterOpts{
			Name:        "objstore_bucket_operation_failures_total",
			Help:        "Total number of operations against a bucket that failed, but were not expected to fail in certain way from caller perspective. Those errors have to be investigated.",
			ConstLabels: prometheus.Labels{"bucket": name},
		}, []string{"operation"}),

		opsFetchedBytes: promauto.With(reg).NewCounterVec(prometheus.CounterOpts{
			Name:        "objstore_bucket_operation_fetched_bytes_total",
			Help:        "Total number of bytes fetched from bucket, per operation.",
			ConstLabels: prometheus.Labels{"bucket": name},
		}, []string{"operation"}),

		opsTransferredBytes: promauto.With(reg).NewHistogramVec(prometheus.HistogramOpts{
			Name:        "objstore_bucket_operation_transferred_bytes",
			Help:        "Number of bytes transferred from/to bucket per operation.",
			ConstLabels: prometheus.Labels{"bucket": name},
			Buckets:     prometheus.ExponentialBuckets(2<<14, 2, 16), // 32KiB, 64KiB, ... 1GiB
			// Use factor=2 for native histograms, which gives similar buckets as the original exponential buckets.
			NativeHistogramBucketFactor:     2,
			NativeHistogramMaxBucketNumber:  100,
			NativeHistogramMinResetDuration: 1 * time.Hour,
		}, []string{"operation"}),

		opsDuration: promauto.With(reg).NewHistogramVec(prometheus.HistogramOpts{
			Name:        "objstore_bucket_operation_duration_seconds",
			Help:        "Duration of successful operations against the bucket per operation - iter operations include time spent on each callback.",
			ConstLabels: prometheus.Labels{"bucket": name},
			Buckets:     []float64{0.001, 0.01, 0.1, 0.3, 0.6, 1, 3, 6, 9, 20, 30, 60, 90, 120},
			// Use the recommended defaults for native histograms with 10% growth factor.
			NativeHistogramBucketFactor:     1.1,
			NativeHistogramMaxBucketNumber:  100,
			NativeHistogramMinResetDuration: 1 * time.Hour,
		}, []string{"operation"}),

		lastSuccessfulUploadTime: promauto.With(reg).NewGauge(prometheus.GaugeOpts{
			Name:        "objstore_bucket_last_successful_upload_time",
			Help:        "Second timestamp of the last successful upload to the bucket.",
			ConstLabels: prometheus.Labels{"bucket": name},
		}),
	}
}

// WrapWithMetrics takes a bucket and registers metrics with the given registry for
// operations run against the bucket.
func WrapWithMetrics(b Bucket, reg prometheus.Registerer, name string) *metricBucket {
	metrics := BucketMetrics(reg, name)
	return wrapWithMetrics(b, metrics)
}

// WrapWith takes a `bucket` and `metrics` that returns instrumented bucket.
// Similar to WrapWithMetrics, but `metrics` can be passed separately as an argument.
func WrapWith(b Bucket, metrics *Metrics) *metricBucket {
	return wrapWithMetrics(b, metrics)
}

func wrapWithMetrics(b Bucket, metrics *Metrics) *metricBucket {
	bkt := &metricBucket{
		bkt:     b,
		metrics: metrics,
	}

	for _, op := range []string{
		OpIter,
		OpGet,
		OpGetRange,
		OpExists,
		OpUpload,
		OpDelete,
		OpAttributes,
	} {
		bkt.metrics.ops.WithLabelValues(op)
		bkt.metrics.opsFailures.WithLabelValues(op)
		bkt.metrics.opsDuration.WithLabelValues(op)
	}

	// fetched bytes only relevant for get, getrange and upload
	for _, op := range []string{
		OpGet,
		OpGetRange,
		OpUpload,
	} {
		bkt.metrics.opsFetchedBytes.WithLabelValues(op)
		bkt.metrics.opsTransferredBytes.WithLabelValues(op)
	}
	return bkt
}

type Metrics struct {
	ops                 *prometheus.CounterVec
	opsFailures         *prometheus.CounterVec
	isOpFailureExpected IsOpFailureExpectedFunc

	opsFetchedBytes          *prometheus.CounterVec
	opsTransferredBytes      *prometheus.HistogramVec
	opsDuration              *prometheus.HistogramVec
	lastSuccessfulUploadTime prometheus.Gauge
}

type metricBucket struct {
	bkt     Bucket
	metrics *Metrics
}

func (b *metricBucket) Provider() ObjProvider {
	return b.bkt.Provider()
}

func (b *metricBucket) WithExpectedErrs(fn IsOpFailureExpectedFunc) Bucket {
	return &metricBucket{
		bkt: b.bkt,
		metrics: &Metrics{
			ops:                      b.metrics.ops,
			opsFailures:              b.metrics.opsFailures,
			opsFetchedBytes:          b.metrics.opsFetchedBytes,
			opsTransferredBytes:      b.metrics.opsTransferredBytes,
			isOpFailureExpected:      fn,
			opsDuration:              b.metrics.opsDuration,
			lastSuccessfulUploadTime: b.metrics.lastSuccessfulUploadTime,
		},
	}
}

func (b *metricBucket) ReaderWithExpectedErrs(fn IsOpFailureExpectedFunc) BucketReader {
	return b.WithExpectedErrs(fn)
}

func (b *metricBucket) Iter(ctx context.Context, dir string, f func(string) error, options ...IterOption) error {
	const op = OpIter
	b.metrics.ops.WithLabelValues(op).Inc()

	timer := prometheus.NewTimer(b.metrics.opsDuration.WithLabelValues(op))
	defer timer.ObserveDuration()

	err := b.bkt.Iter(ctx, dir, f, options...)
	if err != nil {
		if !b.metrics.isOpFailureExpected(err) && ctx.Err() != context.Canceled {
			b.metrics.opsFailures.WithLabelValues(op).Inc()
		}
	}
	return err
}

func (b *metricBucket) IterWithAttributes(ctx context.Context, dir string, f func(IterObjectAttributes) error, options ...IterOption) error {
	const op = OpIter
	b.metrics.ops.WithLabelValues(op).Inc()

	timer := prometheus.NewTimer(b.metrics.opsDuration.WithLabelValues(op))
	defer timer.ObserveDuration()

	err := b.bkt.IterWithAttributes(ctx, dir, f, options...)
	if err != nil {
		if !b.metrics.isOpFailureExpected(err) && ctx.Err() != context.Canceled {
			b.metrics.opsFailures.WithLabelValues(op).Inc()
		}
	}

	return err
}

func (b *metricBucket) SupportedIterOptions() []IterOptionType {
	return b.bkt.SupportedIterOptions()
}

func (b *metricBucket) Attributes(ctx context.Context, name string) (ObjectAttributes, error) {
	const op = OpAttributes
	b.metrics.ops.WithLabelValues(op).Inc()

	start := time.Now()
	attrs, err := b.bkt.Attributes(ctx, name)
	if err != nil {
		if !b.metrics.isOpFailureExpected(err) && ctx.Err() != context.Canceled {
			b.metrics.opsFailures.WithLabelValues(op).Inc()
		}
		return attrs, err
	}
	b.metrics.opsDuration.WithLabelValues(op).Observe(time.Since(start).Seconds())
	return attrs, nil
}

func (b *metricBucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	const op = OpGet
	b.metrics.ops.WithLabelValues(op).Inc()

	start := time.Now()

	rc, err := b.bkt.Get(ctx, name)
	if err != nil {
		if !b.metrics.isOpFailureExpected(err) && ctx.Err() != context.Canceled {
			b.metrics.opsFailures.WithLabelValues(op).Inc()
		}
		b.metrics.opsDuration.WithLabelValues(op).Observe(time.Since(start).Seconds())
		return nil, err
	}
	return newTimingReader(
		start,
		rc,
		true,
		op,
		b.metrics.opsDuration,
		b.metrics.opsFailures,
		b.metrics.isOpFailureExpected,
		b.metrics.opsFetchedBytes,
		b.metrics.opsTransferredBytes,
	), nil
}

func (b *metricBucket) GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	const op = OpGetRange
	b.metrics.ops.WithLabelValues(op).Inc()

	start := time.Now()

	rc, err := b.bkt.GetRange(ctx, name, off, length)
	if err != nil {
		if !b.metrics.isOpFailureExpected(err) && ctx.Err() != context.Canceled {
			b.metrics.opsFailures.WithLabelValues(op).Inc()
		}
		b.metrics.opsDuration.WithLabelValues(op).Observe(time.Since(start).Seconds())
		return nil, err
	}
	return newTimingReader(
		start,
		rc,
		true,
		op,
		b.metrics.opsDuration,
		b.metrics.opsFailures,
		b.metrics.isOpFailureExpected,
		b.metrics.opsFetchedBytes,
		b.metrics.opsTransferredBytes,
	), nil
}

func (b *metricBucket) Exists(ctx context.Context, name string) (bool, error) {
	const op = OpExists
	b.metrics.ops.WithLabelValues(op).Inc()

	start := time.Now()
	ok, err := b.bkt.Exists(ctx, name)
	if err != nil {
		if !b.metrics.isOpFailureExpected(err) && ctx.Err() != context.Canceled {
			b.metrics.opsFailures.WithLabelValues(op).Inc()
		}
		return false, err
	}
	b.metrics.opsDuration.WithLabelValues(op).Observe(time.Since(start).Seconds())
	return ok, nil
}

func (b *metricBucket) Upload(ctx context.Context, name string, r io.Reader, opts ...ObjectUploadOption) error {
	const op = OpUpload
	b.metrics.ops.WithLabelValues(op).Inc()

	start := time.Now()

	trc := newTimingReader(
		start,
		r,
		false,
		op,
		b.metrics.opsDuration,
		b.metrics.opsFailures,
		b.metrics.isOpFailureExpected,
		nil,
		b.metrics.opsTransferredBytes,
	)
	defer trc.Close()
	err := b.bkt.Upload(ctx, name, trc, opts...)
	if err != nil {
		if !b.metrics.isOpFailureExpected(err) && ctx.Err() != context.Canceled {
			b.metrics.opsFailures.WithLabelValues(op).Inc()
		}
		return err
	}
	b.metrics.lastSuccessfulUploadTime.SetToCurrentTime()

	return nil
}

func (b *metricBucket) Delete(ctx context.Context, name string) error {
	const op = OpDelete
	b.metrics.ops.WithLabelValues(op).Inc()

	start := time.Now()
	if err := b.bkt.Delete(ctx, name); err != nil {
		if !b.metrics.isOpFailureExpected(err) && ctx.Err() != context.Canceled {
			b.metrics.opsFailures.WithLabelValues(op).Inc()
		}
		return err
	}
	b.metrics.opsDuration.WithLabelValues(op).Observe(time.Since(start).Seconds())

	return nil
}

func (b *metricBucket) IsObjNotFoundErr(err error) bool {
	return b.bkt.IsObjNotFoundErr(err)
}

func (b *metricBucket) IsAccessDeniedErr(err error) bool {
	return b.bkt.IsAccessDeniedErr(err)
}

func (b *metricBucket) Close() error {
	return b.bkt.Close()
}

func (b *metricBucket) Name() string {
	return b.bkt.Name()
}

type timingReader struct {
	io.Reader

	// closeReader holds whether the wrapper io.Reader should be closed when
	// Close() is called on the timingReader.
	closeReader bool

	objSize    int64
	objSizeErr error

	alreadyGotErr bool

	start             time.Time
	op                string
	readBytes         int64
	duration          *prometheus.HistogramVec
	failed            *prometheus.CounterVec
	isFailureExpected IsOpFailureExpectedFunc
	fetchedBytes      *prometheus.CounterVec
	transferredBytes  *prometheus.HistogramVec
}

func newTimingReader(start time.Time, r io.Reader, closeReader bool, op string, dur *prometheus.HistogramVec, failed *prometheus.CounterVec, isFailureExpected IsOpFailureExpectedFunc, fetchedBytes *prometheus.CounterVec, transferredBytes *prometheus.HistogramVec) io.ReadCloser {
	// Initialize the metrics with 0.
	dur.WithLabelValues(op)
	failed.WithLabelValues(op)
	objSize, objSizeErr := TryToGetSize(r)

	trc := timingReader{
		Reader:            r,
		closeReader:       closeReader,
		objSize:           objSize,
		objSizeErr:        objSizeErr,
		start:             start,
		op:                op,
		duration:          dur,
		failed:            failed,
		isFailureExpected: isFailureExpected,
		fetchedBytes:      fetchedBytes,
		transferredBytes:  transferredBytes,
		readBytes:         0,
	}

	_, isSeeker := r.(io.Seeker)
	_, isReaderAt := r.(io.ReaderAt)
	if isSeeker && isReaderAt {
		// The assumption is that in most cases when io.ReaderAt() is implemented then
		// io.Seeker is implemented too (e.g. os.File).
		return &timingReaderSeekerReaderAt{timingReaderSeeker: timingReaderSeeker{timingReader: trc}}
	}
	if isSeeker {
		return &timingReaderSeeker{timingReader: trc}
	}
	if _, isWriterTo := r.(io.WriterTo); isWriterTo {
		return &timingReaderWriterTo{timingReader: trc}
	}

	return &trc
}

func (r *timingReader) ObjectSize() (int64, error) {
	return r.objSize, r.objSizeErr
}

func (r *timingReader) Close() error {
	var closeErr error

	// Call the wrapped reader if it implements Close(), only if we've been asked to close it.
	if closer, ok := r.Reader.(io.Closer); r.closeReader && ok {
		closeErr = closer.Close()

		if !r.alreadyGotErr && closeErr != nil {
			r.failed.WithLabelValues(r.op).Inc()
			r.alreadyGotErr = true
		}
	}

	// Track duration and transferred bytes only if no error occurred.
	if !r.alreadyGotErr {
		r.duration.WithLabelValues(r.op).Observe(time.Since(r.start).Seconds())
		r.transferredBytes.WithLabelValues(r.op).Observe(float64(r.readBytes))

		// Trick to tracking metrics multiple times in case Close() gets called again.
		r.alreadyGotErr = true
	}

	return closeErr
}

func (r *timingReader) Read(b []byte) (n int, err error) {
	n, err = r.Reader.Read(b)
	r.updateMetrics(n, err)
	return n, err
}

func (r *timingReader) updateMetrics(n int, err error) {
	if r.fetchedBytes != nil {
		r.fetchedBytes.WithLabelValues(r.op).Add(float64(n))
	}
	r.readBytes += int64(n)

	// Report metric just once.
	if !r.alreadyGotErr && err != nil && err != io.EOF {
		if !r.isFailureExpected(err) && !errors.Is(err, context.Canceled) {
			r.failed.WithLabelValues(r.op).Inc()
		}
		r.alreadyGotErr = true
	}
}

type timingReaderSeeker struct {
	timingReader
}

func (rsc *timingReaderSeeker) Seek(offset int64, whence int) (int64, error) {
	return (rsc.Reader).(io.Seeker).Seek(offset, whence)
}

type timingReaderSeekerReaderAt struct {
	timingReaderSeeker
}

func (rsc *timingReaderSeekerReaderAt) ReadAt(p []byte, off int64) (int, error) {
	return (rsc.Reader).(io.ReaderAt).ReadAt(p, off)
}

type timingReaderWriterTo struct {
	timingReader
}

func (t *timingReaderWriterTo) WriteTo(w io.Writer) (n int64, err error) {
	n, err = (t.Reader).(io.WriterTo).WriteTo(w)
	t.timingReader.updateMetrics(int(n), err)
	return n, err
}

type ObjectSizerReadCloser struct {
	io.ReadCloser
	Size func() (int64, error)
}

// ObjectSize implement ObjectSizer.
func (o ObjectSizerReadCloser) ObjectSize() (int64, error) {
	if o.Size == nil {
		return 0, errors.New("unknown size")
	}

	return o.Size()
}
```

## File: `objstore_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package objstore

import (
	"bytes"
	"context"
	"io"
	"os"
	"path/filepath"
	"strings"
	"testing"
	"time"

	"github.com/efficientgo/core/testutil"
	"github.com/go-kit/log"
	"github.com/pkg/errors"
	"github.com/prometheus/client_golang/prometheus"
	promtest "github.com/prometheus/client_golang/prometheus/testutil"
	"go.uber.org/atomic"
)

func TestMetricBucket_Close(t *testing.T) {
	bkt := WrapWithMetrics(NewInMemBucket(), nil, "abc")
	// Expected initialized metrics.
	testutil.Equals(t, 7, promtest.CollectAndCount(bkt.metrics.ops))
	testutil.Equals(t, 7, promtest.CollectAndCount(bkt.metrics.opsFailures))
	testutil.Equals(t, 7, promtest.CollectAndCount(bkt.metrics.opsDuration))

	AcceptanceTest(t, bkt.WithExpectedErrs(bkt.IsObjNotFoundErr))
	testutil.Equals(t, float64(9), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpIter)))
	testutil.Equals(t, float64(2), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpAttributes)))
	testutil.Equals(t, float64(3), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpGet)))
	testutil.Equals(t, float64(3), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpGetRange)))
	testutil.Equals(t, float64(2), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpExists)))
	testutil.Equals(t, float64(9), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpUpload)))
	testutil.Equals(t, float64(3), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpDelete)))
	testutil.Equals(t, 7, promtest.CollectAndCount(bkt.metrics.ops))
	testutil.Equals(t, float64(0), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpIter)))
	testutil.Equals(t, float64(0), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpAttributes)))
	testutil.Equals(t, float64(1), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpGet)))
	testutil.Equals(t, float64(0), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpGetRange)))
	testutil.Equals(t, float64(0), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpExists)))
	testutil.Equals(t, float64(0), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpUpload)))
	testutil.Equals(t, float64(0), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpDelete)))
	testutil.Equals(t, 7, promtest.CollectAndCount(bkt.metrics.opsFailures))
	testutil.Equals(t, 7, promtest.CollectAndCount(bkt.metrics.opsDuration))
	lastUpload := promtest.ToFloat64(bkt.metrics.lastSuccessfulUploadTime)
	testutil.Assert(t, lastUpload > 0, "last upload not greater than 0, val: %f", lastUpload)

	// Clear bucket, but don't clear metrics to ensure we use same.
	bkt.bkt = NewInMemBucket()
	AcceptanceTest(t, bkt)
	testutil.Equals(t, float64(18), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpIter)))
	testutil.Equals(t, float64(4), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpAttributes)))
	testutil.Equals(t, float64(6), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpGet)))
	testutil.Equals(t, float64(6), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpGetRange)))
	testutil.Equals(t, float64(4), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpExists)))
	testutil.Equals(t, float64(18), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpUpload)))
	testutil.Equals(t, float64(6), promtest.ToFloat64(bkt.metrics.ops.WithLabelValues(OpDelete)))
	testutil.Equals(t, 7, promtest.CollectAndCount(bkt.metrics.ops))
	testutil.Equals(t, float64(0), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpIter)))
	// Not expected not found error here.
	testutil.Equals(t, float64(1), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpAttributes)))
	// Not expected not found errors, this should increment failure metric on get for not found as well, so +2.
	testutil.Equals(t, float64(3), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpGet)))
	testutil.Equals(t, float64(0), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpGetRange)))
	testutil.Equals(t, float64(0), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpExists)))
	testutil.Equals(t, float64(0), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpUpload)))
	testutil.Equals(t, float64(0), promtest.ToFloat64(bkt.metrics.opsFailures.WithLabelValues(OpDelete)))
	testutil.Equals(t, 7, promtest.CollectAndCount(bkt.metrics.opsFailures))
	testutil.Equals(t, 7, promtest.CollectAndCount(bkt.metrics.opsDuration))
	testutil.Assert(t, promtest.ToFloat64(bkt.metrics.lastSuccessfulUploadTime) > lastUpload)
}

// TestMetricBucket_MultipleClients tests that the metrics from two different buckets clients are not conflicting with each other.
func TestMetricBucket_Multiple_Clients(t *testing.T) {
	reg := prometheus.NewPedanticRegistry()

	WrapWithMetrics(NewInMemBucket(), reg, "abc")
	WrapWithMetrics(NewInMemBucket(), reg, "def")
}

func TestMetricBucket_UploadShouldPreserveReaderFeatures(t *testing.T) {
	tests := map[string]struct {
		reader             io.Reader
		expectedIsSeeker   bool
		expectedIsReaderAt bool
	}{
		"bytes.Reader": {
			reader:             bytes.NewReader([]byte("1")),
			expectedIsSeeker:   true,
			expectedIsReaderAt: true,
		},
		"bytes.Buffer": {
			reader:             bytes.NewBuffer([]byte("1")),
			expectedIsSeeker:   false,
			expectedIsReaderAt: false,
		},
		"os.File": {
			reader: func() io.Reader {
				// Create a test file.
				testFilepath := filepath.Join(t.TempDir(), "test")
				testutil.Ok(t, os.WriteFile(testFilepath, []byte("test"), os.ModePerm))

				// Open the file (it will be used as io.Reader).
				file, err := os.Open(testFilepath)
				testutil.Ok(t, err)
				t.Cleanup(func() {
					testutil.Ok(t, file.Close())
				})

				return file
			}(),
			expectedIsSeeker:   true,
			expectedIsReaderAt: true,
		},
	}

	for testName, testData := range tests {
		t.Run(testName, func(t *testing.T) {
			var uploadReader io.Reader

			m := &mockBucket{
				Bucket: WrapWithMetrics(NewInMemBucket(), nil, ""),
				upload: func(ctx context.Context, name string, r io.Reader, opts ...ObjectUploadOption) error {
					uploadReader = r
					return nil
				},
			}

			testutil.Ok(t, m.Upload(context.Background(), "dir/obj1", testData.reader))

			_, isSeeker := uploadReader.(io.Seeker)
			testutil.Equals(t, testData.expectedIsSeeker, isSeeker)

			_, isReaderAt := uploadReader.(io.ReaderAt)
			testutil.Equals(t, testData.expectedIsReaderAt, isReaderAt)
		})
	}
}

func TestMetricBucket_ReaderClose(t *testing.T) {
	const objPath = "dir/obj1"

	t.Run("Upload() should not close the input Reader", func(t *testing.T) {
		closeCalled := false

		reader := &mockReader{
			Reader: bytes.NewBuffer([]byte("test")),
			close: func() error {
				closeCalled = true
				return nil
			},
		}

		bucket := WrapWithMetrics(NewInMemBucket(), nil, "")
		testutil.Ok(t, bucket.Upload(context.Background(), objPath, reader))

		// Should not call Close() on the reader.
		testutil.Assert(t, !closeCalled)

		// An explicit call to Close() should close it.
		testutil.Ok(t, reader.Close())
		testutil.Assert(t, closeCalled)

		testutil.Equals(t, float64(1), promtest.ToFloat64(bucket.metrics.ops.WithLabelValues(OpUpload)))
		testutil.Equals(t, float64(0), promtest.ToFloat64(bucket.metrics.opsFailures.WithLabelValues(OpUpload)))
	})

	t.Run("Get() should return a wrapper io.ReadCloser that correctly Close the wrapped one", func(t *testing.T) {
		closeCalled := false

		origReader := &mockReader{
			Reader: bytes.NewBuffer([]byte("test")),
			close: func() error {
				closeCalled = true
				return nil
			},
		}

		bucket := WrapWithMetrics(&mockBucket{
			get: func(_ context.Context, _ string) (io.ReadCloser, error) {
				return origReader, nil
			},
		}, nil, "")

		wrappedReader, err := bucket.Get(context.Background(), objPath)
		testutil.Ok(t, err)
		testutil.Assert(t, origReader != wrappedReader)

		// Calling Close() to the wrappedReader should close origReader.
		testutil.Assert(t, !closeCalled)
		testutil.Ok(t, wrappedReader.Close())
		testutil.Assert(t, closeCalled)

		testutil.Equals(t, float64(1), promtest.ToFloat64(bucket.metrics.ops.WithLabelValues(OpGet)))
		testutil.Equals(t, float64(0), promtest.ToFloat64(bucket.metrics.opsFailures.WithLabelValues(OpGet)))
	})

	t.Run("GetRange() should return a wrapper io.ReadCloser that correctly Close the wrapped one", func(t *testing.T) {
		closeCalled := false

		origReader := &mockReader{
			Reader: bytes.NewBuffer([]byte("test")),
			close: func() error {
				closeCalled = true
				return nil
			},
		}

		bucket := WrapWithMetrics(&mockBucket{
			getRange: func(_ context.Context, _ string, _, _ int64) (io.ReadCloser, error) {
				return origReader, nil
			},
		}, nil, "")

		wrappedReader, err := bucket.GetRange(context.Background(), objPath, 0, 1)
		testutil.Ok(t, err)
		testutil.Assert(t, origReader != wrappedReader)

		// Calling Close() to the wrappedReader should close origReader.
		testutil.Assert(t, !closeCalled)
		testutil.Ok(t, wrappedReader.Close())
		testutil.Assert(t, closeCalled)

		testutil.Equals(t, float64(1), promtest.ToFloat64(bucket.metrics.ops.WithLabelValues(OpGetRange)))
		testutil.Equals(t, float64(0), promtest.ToFloat64(bucket.metrics.opsFailures.WithLabelValues(OpGetRange)))
	})
}

func TestMetricBucket_ReaderCloseError(t *testing.T) {
	origReader := &mockReader{
		Reader: bytes.NewBuffer([]byte("test")),
		close: func() error {
			return errors.New("mocked error")
		},
	}

	t.Run("Get() should track failure if reader Close() returns error", func(t *testing.T) {
		bucket := WrapWithMetrics(&mockBucket{
			get: func(ctx context.Context, name string) (io.ReadCloser, error) {
				return origReader, nil
			},
		}, nil, "")

		testutil.NotOk(t, bucket.Upload(context.Background(), "test", origReader))

		testutil.Equals(t, float64(1), promtest.ToFloat64(bucket.metrics.ops.WithLabelValues(OpUpload)))
		testutil.Equals(t, float64(1), promtest.ToFloat64(bucket.metrics.opsFailures.WithLabelValues(OpUpload)))
	})

	t.Run("Get() should track failure if reader Close() returns error", func(t *testing.T) {
		bucket := WrapWithMetrics(&mockBucket{
			get: func(ctx context.Context, name string) (io.ReadCloser, error) {
				return origReader, nil
			},
		}, nil, "")

		reader, err := bucket.Get(context.Background(), "test")
		testutil.Ok(t, err)
		testutil.NotOk(t, reader.Close())
		testutil.NotOk(t, reader.Close()) // Called twice to ensure metrics are not tracked twice.

		testutil.Equals(t, float64(1), promtest.ToFloat64(bucket.metrics.ops.WithLabelValues(OpGet)))
		testutil.Equals(t, float64(1), promtest.ToFloat64(bucket.metrics.opsFailures.WithLabelValues(OpGet)))
	})

	t.Run("GetRange() should track failure if reader Close() returns error", func(t *testing.T) {
		bucket := WrapWithMetrics(&mockBucket{
			getRange: func(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
				return origReader, nil
			},
		}, nil, "")

		reader, err := bucket.GetRange(context.Background(), "test", 0, 1)
		testutil.Ok(t, err)
		testutil.NotOk(t, reader.Close())
		testutil.NotOk(t, reader.Close()) // Called twice to ensure metrics are not tracked twice.

		testutil.Equals(t, float64(1), promtest.ToFloat64(bucket.metrics.ops.WithLabelValues(OpGetRange)))
		testutil.Equals(t, float64(1), promtest.ToFloat64(bucket.metrics.opsFailures.WithLabelValues(OpGetRange)))
	})
}

func TestDownloadUploadDirConcurrency(t *testing.T) {
	r := prometheus.NewRegistry()
	m := WrapWithMetrics(NewInMemBucket(), r, "")
	tempDir := t.TempDir()

	testutil.Ok(t, m.Upload(context.Background(), "dir/obj1", bytes.NewReader([]byte("1"))))
	testutil.Ok(t, m.Upload(context.Background(), "dir/obj2", bytes.NewReader([]byte("2"))))
	testutil.Ok(t, m.Upload(context.Background(), "dir/obj3", bytes.NewReader(bytes.Repeat([]byte("3"), 1024*1024))))

	testutil.Ok(t, promtest.GatherAndCompare(r, strings.NewReader(`
		# HELP objstore_bucket_operations_total Total number of all attempted operations against a bucket.
        # TYPE objstore_bucket_operations_total counter
        objstore_bucket_operations_total{bucket="",operation="attributes"} 0
        objstore_bucket_operations_total{bucket="",operation="delete"} 0
        objstore_bucket_operations_total{bucket="",operation="exists"} 0
        objstore_bucket_operations_total{bucket="",operation="get"} 0
        objstore_bucket_operations_total{bucket="",operation="get_range"} 0
        objstore_bucket_operations_total{bucket="",operation="iter"} 0
        objstore_bucket_operations_total{bucket="",operation="upload"} 3
		`), `objstore_bucket_operations_total`))

	testutil.Ok(t, DownloadDir(context.Background(), log.NewNopLogger(), m, "dir/", "dir/", tempDir, WithFetchConcurrency(10)))
	i, err := os.ReadDir(tempDir)
	testutil.Ok(t, err)
	testutil.Assert(t, len(i) == 3)
	testutil.Ok(t, promtest.GatherAndCompare(r, strings.NewReader(`
		# HELP objstore_bucket_operations_total Total number of all attempted operations against a bucket.
        # TYPE objstore_bucket_operations_total counter
        objstore_bucket_operations_total{bucket="",operation="attributes"} 0
        objstore_bucket_operations_total{bucket="",operation="delete"} 0
        objstore_bucket_operations_total{bucket="",operation="exists"} 0
        objstore_bucket_operations_total{bucket="",operation="get"} 3
        objstore_bucket_operations_total{bucket="",operation="get_range"} 0
        objstore_bucket_operations_total{bucket="",operation="iter"} 1
        objstore_bucket_operations_total{bucket="",operation="upload"} 3
		`), `objstore_bucket_operations_total`))

	testutil.Ok(t, promtest.GatherAndCompare(r, strings.NewReader(`
        # HELP objstore_bucket_operation_fetched_bytes_total Total number of bytes fetched from bucket, per operation.
        # TYPE objstore_bucket_operation_fetched_bytes_total counter
        objstore_bucket_operation_fetched_bytes_total{bucket="",operation="get"} 1.048578e+06
        objstore_bucket_operation_fetched_bytes_total{bucket="",operation="get_range"} 0
        objstore_bucket_operation_fetched_bytes_total{bucket="",operation="upload"} 0
		`), `objstore_bucket_operation_fetched_bytes_total`))

	testutil.Ok(t, promtest.GatherAndCompare(r, strings.NewReader(`
        # HELP objstore_bucket_operation_transferred_bytes Number of bytes transferred from/to bucket per operation.
        # TYPE objstore_bucket_operation_transferred_bytes histogram
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="32768"} 2
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="65536"} 2
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="131072"} 2
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="262144"} 2
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="524288"} 2
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="1.048576e+06"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="2.097152e+06"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="4.194304e+06"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="8.388608e+06"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="1.6777216e+07"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="3.3554432e+07"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="6.7108864e+07"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="1.34217728e+08"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="2.68435456e+08"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="5.36870912e+08"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="1.073741824e+09"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get",le="+Inf"} 3
        objstore_bucket_operation_transferred_bytes_sum{bucket="",operation="get"} 1.048578e+06
        objstore_bucket_operation_transferred_bytes_count{bucket="",operation="get"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="32768"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="65536"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="131072"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="262144"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="524288"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="1.048576e+06"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="2.097152e+06"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="4.194304e+06"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="8.388608e+06"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="1.6777216e+07"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="3.3554432e+07"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="6.7108864e+07"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="1.34217728e+08"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="2.68435456e+08"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="5.36870912e+08"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="1.073741824e+09"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="get_range",le="+Inf"} 0
        objstore_bucket_operation_transferred_bytes_sum{bucket="",operation="get_range"} 0
        objstore_bucket_operation_transferred_bytes_count{bucket="",operation="get_range"} 0
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="32768"} 2
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="65536"} 2
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="131072"} 2
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="262144"} 2
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="524288"} 2
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="1.048576e+06"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="2.097152e+06"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="4.194304e+06"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="8.388608e+06"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="1.6777216e+07"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="3.3554432e+07"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="6.7108864e+07"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="1.34217728e+08"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="2.68435456e+08"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="5.36870912e+08"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="1.073741824e+09"} 3
        objstore_bucket_operation_transferred_bytes_bucket{bucket="",operation="upload",le="+Inf"} 3
        objstore_bucket_operation_transferred_bytes_sum{bucket="",operation="upload"} 1.048578e+06
        objstore_bucket_operation_transferred_bytes_count{bucket="",operation="upload"} 3
		`), `objstore_bucket_operation_transferred_bytes`))

	testutil.Ok(t, UploadDir(context.Background(), log.NewNopLogger(), m, tempDir, "/dir-copy", WithUploadConcurrency(10)))

	testutil.Ok(t, promtest.GatherAndCompare(r, strings.NewReader(`
		# HELP objstore_bucket_operations_total Total number of all attempted operations against a bucket.
        # TYPE objstore_bucket_operations_total counter
        objstore_bucket_operations_total{bucket="",operation="attributes"} 0
        objstore_bucket_operations_total{bucket="",operation="delete"} 0
        objstore_bucket_operations_total{bucket="",operation="exists"} 0
        objstore_bucket_operations_total{bucket="",operation="get"} 3
        objstore_bucket_operations_total{bucket="",operation="get_range"} 0
        objstore_bucket_operations_total{bucket="",operation="iter"} 1
        objstore_bucket_operations_total{bucket="",operation="upload"} 6
		`), `objstore_bucket_operations_total`))
}

func TestTimingReader(t *testing.T) {
	m := WrapWithMetrics(NewInMemBucket(), nil, "")
	r := bytes.NewReader([]byte("hello world"))
	tr := newTimingReader(time.Now(), r, true, OpGet, m.metrics.opsDuration, m.metrics.opsFailures, func(err error) bool {
		return false
	}, m.metrics.opsFetchedBytes, m.metrics.opsTransferredBytes)

	size, err := TryToGetSize(tr)

	testutil.Ok(t, err)
	testutil.Equals(t, int64(11), size)

	smallBuf := make([]byte, 4)
	n, err := io.ReadFull(tr, smallBuf)
	testutil.Ok(t, err)
	testutil.Equals(t, 4, n)

	// Verify that size is still the same, after reading 4 bytes.
	size, err = TryToGetSize(tr)

	testutil.Ok(t, err)
	testutil.Equals(t, int64(11), size)

	// Given the reader was bytes.Reader it should both implement io.Seeker and io.ReaderAt.
	_, isSeeker := tr.(io.Seeker)
	testutil.Assert(t, isSeeker)

	_, isReaderAt := tr.(io.ReaderAt)
	testutil.Assert(t, isReaderAt)

	testutil.Equals(t, float64(0), promtest.ToFloat64(m.metrics.opsFailures.WithLabelValues(OpGet)))
}

func TestTimingReader_ExpectedError(t *testing.T) {
	readerErr := errors.New("something went wrong")

	m := WrapWithMetrics(NewInMemBucket(), nil, "")
	r := dummyReader{readerErr}
	tr := newTimingReader(time.Now(), r, true, OpGet, m.metrics.opsDuration, m.metrics.opsFailures, func(err error) bool { return errors.Is(err, readerErr) }, m.metrics.opsFetchedBytes, m.metrics.opsTransferredBytes)

	buf := make([]byte, 1)
	_, err := io.ReadFull(tr, buf)
	testutil.Equals(t, readerErr, err)

	testutil.Equals(t, float64(0), promtest.ToFloat64(m.metrics.opsFailures.WithLabelValues(OpGet)))
}

func TestTimingReader_UnexpectedError(t *testing.T) {
	readerErr := errors.New("something went wrong")

	m := WrapWithMetrics(NewInMemBucket(), nil, "")
	r := dummyReader{readerErr}
	tr := newTimingReader(time.Now(), r, true, OpGet, m.metrics.opsDuration, m.metrics.opsFailures, func(err error) bool { return false }, m.metrics.opsFetchedBytes, m.metrics.opsTransferredBytes)

	buf := make([]byte, 1)
	_, err := io.ReadFull(tr, buf)
	testutil.Equals(t, readerErr, err)

	testutil.Equals(t, float64(1), promtest.ToFloat64(m.metrics.opsFailures.WithLabelValues(OpGet)))
}

func TestTimingReader_ContextCancellation(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	cancel()

	m := WrapWithMetrics(NewInMemBucket(), nil, "")
	r := dummyReader{ctx.Err()}
	tr := newTimingReader(time.Now(), r, true, OpGet, m.metrics.opsDuration, m.metrics.opsFailures, func(err error) bool { return false }, m.metrics.opsFetchedBytes, m.metrics.opsTransferredBytes)

	buf := make([]byte, 1)
	_, err := io.ReadFull(tr, buf)
	testutil.Equals(t, ctx.Err(), err)

	testutil.Equals(t, float64(0), promtest.ToFloat64(m.metrics.opsFailures.WithLabelValues(OpGet)))
}

type dummyReader struct {
	err error
}

func (r dummyReader) Read(_ []byte) (int, error) {
	return 0, r.err
}

func TestTimingReader_ShouldCorrectlyWrapFile(t *testing.T) {
	// Create a test file.
	testFilepath := filepath.Join(t.TempDir(), "test")
	testutil.Ok(t, os.WriteFile(testFilepath, []byte("test"), os.ModePerm))

	// Open the file (it will be used as io.Reader).
	file, err := os.Open(testFilepath)
	testutil.Ok(t, err)
	t.Cleanup(func() {
		testutil.Ok(t, file.Close())
	})

	m := WrapWithMetrics(NewInMemBucket(), nil, "")
	r := newTimingReader(time.Now(), file, true, "", m.metrics.opsDuration, m.metrics.opsFailures, func(err error) bool {
		return false
	}, m.metrics.opsFetchedBytes, m.metrics.opsTransferredBytes)

	// It must both implement io.Seeker and io.ReaderAt.
	_, isSeeker := r.(io.Seeker)
	testutil.Assert(t, isSeeker)

	_, isReaderAt := r.(io.ReaderAt)
	testutil.Assert(t, isReaderAt)
}

func TestDownloadDir_CleanUp(t *testing.T) {
	b := unreliableBucket{
		Bucket:  NewInMemBucket(),
		n:       3,
		current: atomic.NewInt32(0),
	}
	tempDir := t.TempDir()

	testutil.Ok(t, b.Upload(context.Background(), "dir/obj1", bytes.NewReader([]byte("1"))))
	testutil.Ok(t, b.Upload(context.Background(), "dir/obj2", bytes.NewReader([]byte("2"))))
	testutil.Ok(t, b.Upload(context.Background(), "dir/obj3", bytes.NewReader([]byte("3"))))

	// We exapect the third Get to fail
	testutil.NotOk(t, DownloadDir(context.Background(), log.NewNopLogger(), b, "dir/", "dir/", tempDir))
	_, err := os.Stat(tempDir)
	testutil.Assert(t, os.IsNotExist(err))
}

// unreliableBucket implements Bucket and returns an error on every n-th Get.
type unreliableBucket struct {
	Bucket

	n       int32
	current *atomic.Int32
}

func (b unreliableBucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	if b.current.Inc()%b.n == 0 {
		return nil, errors.Errorf("some error message")
	}
	return b.Bucket.Get(ctx, name)
}

// mockReader implements io.ReadCloser and allows to mock the functions.
type mockReader struct {
	io.Reader

	close func() error
}

func (r *mockReader) Close() error {
	if r.close != nil {
		return r.close()
	}
	return nil
}

// mockBucket implements Bucket and allows to mock the functions.
type mockBucket struct {
	Bucket

	upload   func(ctx context.Context, name string, r io.Reader, opts ...ObjectUploadOption) error
	get      func(ctx context.Context, name string) (io.ReadCloser, error)
	getRange func(ctx context.Context, name string, off, length int64) (io.ReadCloser, error)
}

func (b *mockBucket) Upload(ctx context.Context, name string, r io.Reader, opts ...ObjectUploadOption) error {
	if b.upload != nil {
		return b.upload(ctx, name, r, opts...)
	}
	return errors.New("Upload has not been mocked")
}

func (b *mockBucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	if b.get != nil {
		return b.get(ctx, name)
	}
	return nil, errors.New("Get has not been mocked")
}

func (b *mockBucket) GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	if b.getRange != nil {
		return b.getRange(ctx, name, off, length)
	}
	return nil, errors.New("GetRange has not been mocked")
}

func Test_TryToGetSizeLimitedReader(t *testing.T) {
	b := &bytes.Buffer{}
	r := io.LimitReader(b, 1024)
	size, err := TryToGetSize(r)
	testutil.Ok(t, err)
	testutil.Equals(t, int64(1024), size)
}
```

## File: `prefixed_bucket.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package objstore

import (
	"context"
	"io"
	"strings"
)

type PrefixedBucket struct {
	bkt    Bucket
	prefix string
}

func NewPrefixedBucket(bkt Bucket, prefix string) Bucket {
	if validPrefix(prefix) {
		return &PrefixedBucket{bkt: bkt, prefix: strings.Trim(prefix, DirDelim)}
	}

	return bkt
}

func validPrefix(prefix string) bool {
	prefix = strings.Replace(prefix, "/", "", -1)
	return len(prefix) > 0
}

func conditionalPrefix(prefix, name string) string {
	if len(name) > 0 {
		return withPrefix(prefix, name)
	}

	return name
}

func withPrefix(prefix, name string) string {
	return prefix + DirDelim + name
}

func (p *PrefixedBucket) Provider() ObjProvider { return p.bkt.Provider() }

func (p *PrefixedBucket) Close() error {
	return p.bkt.Close()
}

// Iter calls f for each entry in the given directory (not recursive.). The argument to f is the full
// object name including the prefix of the inspected directory.
// Entries are passed to function in sorted order.
func (p *PrefixedBucket) Iter(ctx context.Context, dir string, f func(string) error, options ...IterOption) error {
	pdir := withPrefix(p.prefix, dir)

	return p.bkt.Iter(ctx, pdir, func(s string) error {
		return f(strings.TrimPrefix(s, p.prefix+DirDelim))
	}, options...)
}

func (p *PrefixedBucket) IterWithAttributes(ctx context.Context, dir string, f func(IterObjectAttributes) error, options ...IterOption) error {
	pdir := withPrefix(p.prefix, dir)

	return p.bkt.IterWithAttributes(ctx, pdir, func(attrs IterObjectAttributes) error {
		attrs.Name = strings.TrimPrefix(attrs.Name, p.prefix+DirDelim)
		return f(attrs)
	}, options...)
}

func (p *PrefixedBucket) SupportedIterOptions() []IterOptionType {
	return p.bkt.SupportedIterOptions()
}

// Get returns a reader for the given object name.
func (p *PrefixedBucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	return p.bkt.Get(ctx, conditionalPrefix(p.prefix, name))
}

// GetRange returns a new range reader for the given object name and range.
func (p *PrefixedBucket) GetRange(ctx context.Context, name string, off int64, length int64) (io.ReadCloser, error) {
	return p.bkt.GetRange(ctx, conditionalPrefix(p.prefix, name), off, length)
}

// Exists checks if the given object exists in the bucket.
func (p *PrefixedBucket) Exists(ctx context.Context, name string) (bool, error) {
	return p.bkt.Exists(ctx, conditionalPrefix(p.prefix, name))
}

// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
func (p *PrefixedBucket) IsObjNotFoundErr(err error) bool {
	return p.bkt.IsObjNotFoundErr(err)
}

// IsAccessDeniedErr returns true if access to object is denied.
func (p *PrefixedBucket) IsAccessDeniedErr(err error) bool {
	return p.bkt.IsAccessDeniedErr(err)
}

// Attributes returns information about the specified object.
func (p *PrefixedBucket) Attributes(ctx context.Context, name string) (ObjectAttributes, error) {
	return p.bkt.Attributes(ctx, conditionalPrefix(p.prefix, name))
}

// Upload the contents of the reader as an object into the bucket.
// Upload should be idempotent.
func (p *PrefixedBucket) Upload(ctx context.Context, name string, r io.Reader, opts ...ObjectUploadOption) error {
	return p.bkt.Upload(ctx, conditionalPrefix(p.prefix, name), r, opts...)
}

// Delete removes the object with the given name.
// If object does not exists in the moment of deletion, Delete should throw error.
func (p *PrefixedBucket) Delete(ctx context.Context, name string) error {
	return p.bkt.Delete(ctx, conditionalPrefix(p.prefix, name))
}

// Name returns the bucket name for the provider.
func (p *PrefixedBucket) Name() string {
	return p.bkt.Name()
}
```

## File: `prefixed_bucket_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package objstore

import (
	"context"
	"io"
	"sort"
	"strings"
	"testing"

	"github.com/efficientgo/core/testutil"
)

func TestPrefixedBucket_Acceptance(t *testing.T) {

	prefixes := []string{
		"/someprefix/anotherprefix/",
		"someprefix/anotherprefix/",
		"someprefix/anotherprefix",
		"someprefix/",
		"someprefix"}

	for _, prefix := range prefixes {
		AcceptanceTest(t, NewPrefixedBucket(NewInMemBucket(), prefix))
		UsesPrefixTest(t, NewInMemBucket(), prefix)
	}
}

func UsesPrefixTest(t *testing.T, bkt Bucket, prefix string) {
	testutil.Ok(t, bkt.Upload(context.Background(), strings.Trim(prefix, "/")+"/file1.jpg", strings.NewReader("test-data1")))

	pBkt := NewPrefixedBucket(bkt, prefix)
	rc1, err := pBkt.Get(context.Background(), "file1.jpg")
	testutil.Ok(t, err)

	testutil.Ok(t, err)
	defer func() { testutil.Ok(t, rc1.Close()) }()
	content, err := io.ReadAll(rc1)
	testutil.Ok(t, err)
	testutil.Equals(t, "test-data1", string(content))

	testutil.Ok(t, pBkt.Upload(context.Background(), "file2.jpg", strings.NewReader("test-data2")))
	rc2, err := bkt.Get(context.Background(), strings.Trim(prefix, "/")+"/file2.jpg")
	testutil.Ok(t, err)
	defer func() { testutil.Ok(t, rc2.Close()) }()
	contentUpload, err := io.ReadAll(rc2)
	testutil.Ok(t, err)
	testutil.Equals(t, "test-data2", string(contentUpload))

	testutil.Ok(t, pBkt.Delete(context.Background(), "file2.jpg"))
	_, err = bkt.Get(context.Background(), strings.Trim(prefix, "/")+"/file2.jpg")
	testutil.NotOk(t, err)
	testutil.Assert(t, pBkt.IsObjNotFoundErr(err), "expected not found error got %s", err)

	rc3, err := pBkt.GetRange(context.Background(), "file1.jpg", 1, 3)
	testutil.Ok(t, err)
	defer func() { testutil.Ok(t, rc3.Close()) }()
	content, err = io.ReadAll(rc3)
	testutil.Ok(t, err)
	testutil.Equals(t, "est", string(content))

	ok, err := pBkt.Exists(context.Background(), "file1.jpg")
	testutil.Ok(t, err)
	testutil.Assert(t, ok, "expected exits")

	attrs, err := pBkt.Attributes(context.Background(), "file1.jpg")
	testutil.Ok(t, err)
	testutil.Assert(t, attrs.Size == 10, "expected size to be equal to 10")

	testutil.Ok(t, bkt.Upload(context.Background(), strings.Trim(prefix, "/")+"/dir/file1.jpg", strings.NewReader("test-data1")))
	seen := []string{}
	testutil.Ok(t, pBkt.Iter(context.Background(), "", func(fn string) error {
		seen = append(seen, fn)
		return nil
	}, WithRecursiveIter()))
	expected := []string{"dir/file1.jpg", "file1.jpg"}
	sort.Strings(expected)
	sort.Strings(seen)
	testutil.Equals(t, expected, seen)

	seen = []string{}
	testutil.Ok(t, pBkt.Iter(context.Background(), "", func(fn string) error {
		seen = append(seen, fn)
		return nil
	}))
	expected = []string{"dir/", "file1.jpg"}
	sort.Strings(expected)
	sort.Strings(seen)
	testutil.Equals(t, expected, seen)
}
```

## File: `testing.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package objstore

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"math/rand"
	"sort"
	"strings"
	"sync"
	"testing"
	"time"

	"github.com/efficientgo/core/testutil"
)

func CreateTemporaryTestBucketName(t testing.TB) string {
	src := rand.NewSource(time.Now().UnixNano())

	// Bucket name need to conform: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-s3-bucket-naming-requirements.html.
	name := strings.ReplaceAll(strings.Replace(fmt.Sprintf("test_%x_%s", src.Int63(), strings.ToLower(t.Name())), "_", "-", -1), "/", "-")
	if len(name) >= 63 {
		name = name[:63]
	}
	return name
}

// EmptyBucket deletes all objects from bucket. This operation is required to properly delete bucket as a whole.
// It is used for testing only.
// TODO(bplotka): Add retries.
func EmptyBucket(t testing.TB, ctx context.Context, bkt Bucket) {
	var wg sync.WaitGroup

	queue := []string{""}
	for len(queue) > 0 {
		elem := queue[0]
		queue = queue[1:]

		err := bkt.Iter(ctx, elem, func(p string) error {
			if strings.HasSuffix(p, DirDelim) {
				queue = append(queue, p)
				return nil
			}

			wg.Add(1)
			go func() {
				if err := bkt.Delete(ctx, p); err != nil {
					t.Logf("deleting object %s failed: %s", p, err)
				}
				wg.Done()
			}()
			return nil
		})
		if err != nil {
			t.Logf("iterating over bucket objects failed: %s", err)
			wg.Wait()
			return
		}
	}
	wg.Wait()
}

func WithNoopInstr(bkt Bucket) InstrumentedBucket {
	return noopInstrumentedBucket{Bucket: bkt}
}

type noopInstrumentedBucket struct {
	Bucket
}

func (b noopInstrumentedBucket) WithExpectedErrs(IsOpFailureExpectedFunc) Bucket {
	return b
}

func (b noopInstrumentedBucket) ReaderWithExpectedErrs(IsOpFailureExpectedFunc) BucketReader {
	return b
}

func AcceptanceTest(t *testing.T, bkt Bucket) {
	ctx := context.Background()

	_, err := bkt.Get(ctx, "")
	testutil.NotOk(t, err)
	testutil.Assert(t, !bkt.IsObjNotFoundErr(err), "expected user error got not found %s", err)

	_, err = bkt.Get(ctx, "id1/obj_1.some")
	testutil.NotOk(t, err)
	testutil.Assert(t, bkt.IsObjNotFoundErr(err), "expected not found error got %s", err)

	ok, err := bkt.Exists(ctx, "id1/obj_1.some")
	testutil.Ok(t, err)
	testutil.Assert(t, !ok, "expected not exits")

	_, err = bkt.Attributes(ctx, "id1/obj_1.some")
	testutil.NotOk(t, err)
	testutil.Assert(t, bkt.IsObjNotFoundErr(err), "expected not found error but got %s", err)

	// Upload first object.
	testutil.Ok(t, bkt.Upload(ctx, "id1/obj_1.some", strings.NewReader("@test-data@")))

	// Double check we can immediately read it.
	rc1, err := bkt.Get(ctx, "id1/obj_1.some")
	testutil.Ok(t, err)
	defer func() { testutil.Ok(t, rc1.Close()) }()

	sz, err := TryToGetSize(rc1)
	testutil.Ok(t, err)
	testutil.Equals(t, int64(11), sz, "expected size to be equal to 11")

	content, err := io.ReadAll(rc1)
	testutil.Ok(t, err)
	testutil.Equals(t, "@test-data@", string(content))

	// Check if we can get the correct size.
	attrs, err := bkt.Attributes(ctx, "id1/obj_1.some")
	testutil.Ok(t, err)
	testutil.Assert(t, attrs.Size == 11, "expected size to be equal to 11")

	rc2, err := bkt.GetRange(ctx, "id1/obj_1.some", 1, 3)
	testutil.Ok(t, err)
	defer func() { testutil.Ok(t, rc2.Close()) }()

	sz, err = TryToGetSize(rc2)
	testutil.Ok(t, err)
	testutil.Equals(t, int64(3), sz, "expected size to be equal to 3")

	content, err = io.ReadAll(rc2)
	testutil.Ok(t, err)
	testutil.Equals(t, "tes", string(content))

	// Unspecified range with offset.
	rcUnspecifiedLen, err := bkt.GetRange(ctx, "id1/obj_1.some", 1, -1)
	testutil.Ok(t, err)
	defer func() { testutil.Ok(t, rcUnspecifiedLen.Close()) }()

	sz, err = TryToGetSize(rcUnspecifiedLen)
	testutil.Ok(t, err)
	testutil.Equals(t, int64(10), sz, "expected size to be equal to 10")

	content, err = io.ReadAll(rcUnspecifiedLen)
	testutil.Ok(t, err)
	testutil.Equals(t, "test-data@", string(content))

	// Out of band offset. Do not rely on outcome.
	// NOTE: For various providers we have different outcome.
	// * GCS is giving 416 status code
	// * S3 errors immdiately with invalid range error.
	// * inmem and filesystem are returning 0 bytes.
	//rcOffset, err := bkt.GetRange(ctx, "id1/obj_1.some", 124141, 3)

	// Out of band length. We expect to read file fully.
	rcLength, err := bkt.GetRange(ctx, "id1/obj_1.some", 3, 9999)
	testutil.Ok(t, err)
	defer func() { testutil.Ok(t, rcLength.Close()) }()

	sz, err = TryToGetSize(rcLength)
	testutil.Ok(t, err)
	testutil.Equals(t, int64(8), sz, "expected size to be equal to 8")

	content, err = io.ReadAll(rcLength)
	testutil.Ok(t, err)
	testutil.Equals(t, "st-data@", string(content))

	ok, err = bkt.Exists(ctx, "id1/obj_1.some")
	testutil.Ok(t, err)
	testutil.Assert(t, ok, "expected exits")

	// Upload other objects.
	testutil.Ok(t, bkt.Upload(ctx, "id1/obj_2.some", strings.NewReader("@test-data2@")))
	// Upload should be idempotent.
	testutil.Ok(t, bkt.Upload(ctx, "id1/obj_2.some", strings.NewReader("@test-data2@")))
	testutil.Ok(t, bkt.Upload(ctx, "id1/obj_3.some", strings.NewReader("@test-data3@")))
	testutil.Ok(t, bkt.Upload(ctx, "id1/sub/subobj_1.some", strings.NewReader("@test-data4@")))
	testutil.Ok(t, bkt.Upload(ctx, "id1/sub/subobj_2.some", strings.NewReader("@test-data5@")))
	testutil.Ok(t, bkt.Upload(ctx, "id2/obj_4.some", strings.NewReader("@test-data6@")))
	testutil.Ok(t, bkt.Upload(ctx, "obj_5.some", strings.NewReader("@test-data7@")))

	// Can we iter over items from top dir?
	var seen []string
	testutil.Ok(t, bkt.Iter(ctx, "", func(fn string) error {
		seen = append(seen, fn)
		return nil
	}))
	expected := []string{"obj_5.some", "id1/", "id2/"}
	sort.Strings(expected)
	sort.Strings(seen)
	testutil.Equals(t, expected, seen)

	// Can we iter over items from top dir recursively?
	seen = []string{}
	testutil.Ok(t, bkt.Iter(ctx, "", func(fn string) error {
		seen = append(seen, fn)
		return nil
	}, WithRecursiveIter()))
	expected = []string{"id1/obj_1.some", "id1/obj_2.some", "id1/obj_3.some", "id1/sub/subobj_1.some", "id1/sub/subobj_2.some", "id2/obj_4.some", "obj_5.some"}
	sort.Strings(expected)
	sort.Strings(seen)
	testutil.Equals(t, expected, seen)

	// Can we iter over items from id1/ dir?
	seen = []string{}
	testutil.Ok(t, bkt.Iter(ctx, "id1/", func(fn string) error {
		seen = append(seen, fn)
		return nil
	}))
	testutil.Equals(t, []string{"id1/obj_1.some", "id1/obj_2.some", "id1/obj_3.some", "id1/sub/"}, seen)

	// Can we iter over items from id1/ dir recursively?
	seen = []string{}
	testutil.Ok(t, bkt.Iter(ctx, "id1/", func(fn string) error {
		seen = append(seen, fn)
		return nil
	}, WithRecursiveIter()))
	testutil.Equals(t, []string{"id1/obj_1.some", "id1/obj_2.some", "id1/obj_3.some", "id1/sub/subobj_1.some", "id1/sub/subobj_2.some"}, seen)

	// Can we iter over items from id1 dir?
	seen = []string{}
	testutil.Ok(t, bkt.Iter(ctx, "id1", func(fn string) error {
		seen = append(seen, fn)
		return nil
	}))
	testutil.Equals(t, []string{"id1/obj_1.some", "id1/obj_2.some", "id1/obj_3.some", "id1/sub/"}, seen)

	// Can we iter over items from id1 dir recursively?
	seen = []string{}
	testutil.Ok(t, bkt.Iter(ctx, "id1", func(fn string) error {
		seen = append(seen, fn)
		return nil
	}, WithRecursiveIter()))
	testutil.Equals(t, []string{"id1/obj_1.some", "id1/obj_2.some", "id1/obj_3.some", "id1/sub/subobj_1.some", "id1/sub/subobj_2.some"}, seen)

	// Can we iter over items from not existing dir?
	testutil.Ok(t, bkt.Iter(ctx, "id0", func(fn string) error {
		t.Error("Not expected to loop through not existing directory")
		t.FailNow()

		return nil
	}))

	testutil.Ok(t, bkt.Delete(ctx, "id1/obj_2.some"))

	// Delete is expected to fail on non existing object.
	// NOTE: Don't rely on this. S3 is not complying with this as GCS is.
	// testutil.NotOk(t, bkt.Delete(ctx, "id1/obj_2.some"))

	// Can we iter over items from id1/ dir and see obj2 being deleted?
	seen = []string{}
	testutil.Ok(t, bkt.Iter(ctx, "id1/", func(fn string) error {
		seen = append(seen, fn)
		return nil
	}))
	testutil.Equals(t, []string{"id1/obj_1.some", "id1/obj_3.some", "id1/sub/"}, seen)

	testutil.Ok(t, bkt.Delete(ctx, "id2/obj_4.some"))

	seen = []string{}
	testutil.Ok(t, bkt.Iter(ctx, "", func(fn string) error {
		seen = append(seen, fn)
		return nil
	}))
	expected = []string{"obj_5.some", "id1/"}
	sort.Strings(expected)
	sort.Strings(seen)
	testutil.Equals(t, expected, seen)

	testutil.Ok(t, bkt.Upload(ctx, "obj_6.som", bytes.NewReader(make([]byte, 1024*1024*200))))
	testutil.Ok(t, bkt.Delete(ctx, "obj_6.som"))
}

type delayingBucket struct {
	bkt   Bucket
	delay time.Duration
}

func WithDelay(bkt Bucket, delay time.Duration) Bucket {
	return &delayingBucket{bkt: bkt, delay: delay}
}

func (d *delayingBucket) Provider() ObjProvider { return d.bkt.Provider() }

func (d *delayingBucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	time.Sleep(d.delay)
	return d.bkt.Get(ctx, name)
}

func (d *delayingBucket) Attributes(ctx context.Context, name string) (ObjectAttributes, error) {
	time.Sleep(d.delay)
	return d.bkt.Attributes(ctx, name)
}

func (d *delayingBucket) Iter(ctx context.Context, dir string, f func(string) error, options ...IterOption) error {
	time.Sleep(d.delay)
	return d.bkt.Iter(ctx, dir, f, options...)
}

func (d *delayingBucket) IterWithAttributes(ctx context.Context, dir string, f func(IterObjectAttributes) error, options ...IterOption) error {
	time.Sleep(d.delay)
	return d.bkt.IterWithAttributes(ctx, dir, f, options...)
}

func (d *delayingBucket) SupportedIterOptions() []IterOptionType {
	return d.bkt.SupportedIterOptions()
}

func (d *delayingBucket) GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	time.Sleep(d.delay)
	return d.bkt.GetRange(ctx, name, off, length)
}

func (d *delayingBucket) Exists(ctx context.Context, name string) (bool, error) {
	time.Sleep(d.delay)
	return d.bkt.Exists(ctx, name)
}

func (d *delayingBucket) Upload(ctx context.Context, name string, r io.Reader, opts ...ObjectUploadOption) error {
	time.Sleep(d.delay)
	return d.bkt.Upload(ctx, name, r, opts...)
}

func (d *delayingBucket) Delete(ctx context.Context, name string) error {
	time.Sleep(d.delay)
	return d.bkt.Delete(ctx, name)
}

func (d *delayingBucket) Name() string {
	time.Sleep(d.delay)
	return d.bkt.Name()
}

func (d *delayingBucket) Close() error {
	// No delay for a local operation.
	return d.bkt.Close()
}
func (d *delayingBucket) IsObjNotFoundErr(err error) bool {
	// No delay for a local operation.
	return d.bkt.IsObjNotFoundErr(err)
}

func (d *delayingBucket) IsAccessDeniedErr(err error) bool {
	return d.bkt.IsAccessDeniedErr(err)
}
```

## File: `tlsconfig.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package objstore

import (
	"crypto/tls"
	"crypto/x509"
	"fmt"
	"os"
)

// NewTLSConfig creates a new tls.Config from the given TLSConfig.
func NewTLSConfig(cfg *TLSConfig) (*tls.Config, error) {
	tlsConfig := &tls.Config{InsecureSkipVerify: cfg.InsecureSkipVerify}

	// If a CA cert is provided then let's read it in.
	if len(cfg.CAFile) > 0 {
		b, err := readCAFile(cfg.CAFile)
		if err != nil {
			return nil, err
		}
		if !updateRootCA(tlsConfig, b) {
			return nil, fmt.Errorf("unable to use specified CA cert %s", cfg.CAFile)
		}
	}

	if len(cfg.ServerName) > 0 {
		tlsConfig.ServerName = cfg.ServerName
	}
	// If a client cert & key is provided then configure TLS config accordingly.
	if len(cfg.CertFile) > 0 && len(cfg.KeyFile) == 0 {
		return nil, fmt.Errorf("client cert file %q specified without client key file", cfg.CertFile)
	} else if len(cfg.KeyFile) > 0 && len(cfg.CertFile) == 0 {
		return nil, fmt.Errorf("client key file %q specified without client cert file", cfg.KeyFile)
	} else if len(cfg.CertFile) > 0 && len(cfg.KeyFile) > 0 {
		// Verify that client cert and key are valid.
		if _, err := cfg.getClientCertificate(nil); err != nil {
			return nil, err
		}
		tlsConfig.GetClientCertificate = cfg.getClientCertificate
	}

	return tlsConfig, nil
}

// readCAFile reads the CA cert file from disk.
func readCAFile(f string) ([]byte, error) {
	data, err := os.ReadFile(f)
	if err != nil {
		return nil, fmt.Errorf("unable to load specified CA cert %s: %s", f, err)
	}
	return data, nil
}

// updateRootCA parses the given byte slice as a series of PEM encoded certificates and updates tls.Config.RootCAs.
func updateRootCA(cfg *tls.Config, b []byte) bool {
	caCertPool := x509.NewCertPool()
	if !caCertPool.AppendCertsFromPEM(b) {
		return false
	}
	cfg.RootCAs = caCertPool
	return true
}

// getClientCertificate reads the pair of client cert and key from disk and returns a tls.Certificate.
func (c *TLSConfig) getClientCertificate(*tls.CertificateRequestInfo) (*tls.Certificate, error) {
	cert, err := tls.LoadX509KeyPair(c.CertFile, c.KeyFile)
	if err != nil {
		return nil, fmt.Errorf("unable to use specified client cert (%s) & key (%s): %s", c.CertFile, c.KeyFile, err)
	}
	return &cert, nil
}

// TLSConfig configures the options for TLS connections.
type TLSConfig struct {
	// The CA cert to use for the targets.
	CAFile string `yaml:"ca_file"`
	// The client cert file for the targets.
	CertFile string `yaml:"cert_file"`
	// The client key file for the targets.
	KeyFile string `yaml:"key_file"`
	// Used to verify the hostname for the targets.
	ServerName string `yaml:"server_name"`
	// Disable target certificate validation.
	InsecureSkipVerify bool `yaml:"insecure_skip_verify"`
}
```

## File: `client/factory.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package client

import (
	"context"
	"fmt"
	"net/http"
	"strings"

	"github.com/thanos-io/objstore"
	"github.com/thanos-io/objstore/providers/azure"
	"github.com/thanos-io/objstore/providers/bos"
	"github.com/thanos-io/objstore/providers/cos"
	"github.com/thanos-io/objstore/providers/filesystem"
	"github.com/thanos-io/objstore/providers/gcs"
	"github.com/thanos-io/objstore/providers/obs"
	"github.com/thanos-io/objstore/providers/oci"
	"github.com/thanos-io/objstore/providers/oss"
	"github.com/thanos-io/objstore/providers/s3"
	"github.com/thanos-io/objstore/providers/swift"

	"github.com/go-kit/log"
	"github.com/go-kit/log/level"
	"github.com/pkg/errors"
	"gopkg.in/yaml.v2"
)

type BucketConfig struct {
	Type   objstore.ObjProvider `yaml:"type"`
	Config interface{}          `yaml:"config"`
	Prefix string               `yaml:"prefix" default:""`
}

// NewBucket initializes and returns new object storage clients.
// NOTE: confContentYaml can contain secrets.
func NewBucket(logger log.Logger, confContentYaml []byte, component string, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (objstore.Bucket, error) {
	level.Info(logger).Log("msg", "loading bucket configuration")
	bucketConf := &BucketConfig{}
	if err := yaml.UnmarshalStrict(confContentYaml, bucketConf); err != nil {
		return nil, errors.Wrap(err, "parsing config YAML file")
	}

	return NewBucketFromConfig(logger, bucketConf, component, wrapRoundtripper)
}

// NewBucketFromConfig creates an objstore.Bucket from an existing BucketConfig object.
func NewBucketFromConfig(logger log.Logger, bucketConf *BucketConfig, component string, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (objstore.Bucket, error) {
	config, err := yaml.Marshal(bucketConf.Config)
	if err != nil {
		return nil, errors.Wrap(err, "marshal content of bucket configuration")
	}

	var bucket objstore.Bucket
	switch strings.ToUpper(string(bucketConf.Type)) {
	case string(objstore.GCS):
		bucket, err = gcs.NewBucket(context.Background(), logger, config, component, wrapRoundtripper)
	case string(objstore.S3):
		bucket, err = s3.NewBucket(logger, config, component, wrapRoundtripper)
	case string(objstore.AZURE):
		bucket, err = azure.NewBucket(logger, config, component, wrapRoundtripper)
	case string(objstore.SWIFT):
		bucket, err = swift.NewContainer(logger, config, wrapRoundtripper)
	case string(objstore.COS):
		bucket, err = cos.NewBucket(logger, config, component, wrapRoundtripper)
	case string(objstore.ALIYUNOSS):
		bucket, err = oss.NewBucket(logger, config, component, wrapRoundtripper)
	case string(objstore.FILESYSTEM):
		bucket, err = filesystem.NewBucketFromConfig(config)
	case string(objstore.BOS):
		bucket, err = bos.NewBucket(logger, config, component)
	case string(objstore.OCI):
		bucket, err = oci.NewBucket(logger, config, wrapRoundtripper)
	case string(objstore.OBS):
		bucket, err = obs.NewBucket(logger, config)
	default:
		return nil, errors.Errorf("bucket with type %s is not supported", bucketConf.Type)
	}
	if err != nil {
		return nil, errors.Wrap(err, fmt.Sprintf("create %s client", bucketConf.Type))
	}

	return objstore.NewPrefixedBucket(bucket, bucketConf.Prefix), nil
}
```

## File: `client/factory_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package client

import (
	"context"
	"fmt"
	"os"

	"github.com/go-kit/log"
)

func ExampleBucket() {
	// Read the configuration file.
	confContentYaml, err := os.ReadFile("testconf/filesystem.conf.yml")
	if err != nil {
		panic(err)
	}

	// Create a new bucket.
	bucket, err := NewBucket(log.NewNopLogger(), confContentYaml, "example", nil)
	if err != nil {
		panic(err)
	}

	// Test it.
	exists, err := bucket.Exists(context.Background(), "example")
	if err != nil {
		panic(err)
	}
	fmt.Println(exists)
	// Output:
	// false
}
```

## File: `client/testconf/filesystem.conf.yml`
```yaml
type: "FILESYSTEM"
config:
  directory: "./data"
```

## File: `clientutil/parse.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package clientutil

import (
	"net/http"
	"strconv"
	"time"

	"github.com/pkg/errors"
)

// ParseContentLength returns the content length (in bytes) parsed from the Content-Length
// HTTP header in input.
func ParseContentLength(m http.Header) (int64, error) {
	const name = "Content-Length"

	v, ok := m[name]
	if !ok {
		return 0, errors.Errorf("%s header not found", name)
	}

	if len(v) == 0 {
		return 0, errors.Errorf("%s header has no values", name)
	}

	ret, err := strconv.ParseInt(v[0], 10, 64)
	if err != nil {
		return 0, errors.Wrapf(err, "convert %s", name)
	}

	return ret, nil
}

// ParseLastModified returns the timestamp parsed from the Last-Modified
// HTTP header in input.
// Passing an second parameter, named f, to specify the time format.
// If f is empty then RFC3339 will be used as default format.
func ParseLastModified(m http.Header, f string) (time.Time, error) {
	const (
		name          = "Last-Modified"
		defaultFormat = time.RFC3339
	)

	v, ok := m[name]
	if !ok {
		return time.Time{}, errors.Errorf("%s header not found", name)
	}

	if len(v) == 0 {
		return time.Time{}, errors.Errorf("%s header has no values", name)
	}

	if f == "" {
		f = defaultFormat
	}

	mod, err := time.Parse(f, v[0])
	if err != nil {
		return time.Time{}, errors.Wrapf(err, "parse %s", name)
	}

	return mod, nil
}
```

## File: `clientutil/parse_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package clientutil

import (
	"net/http"
	"testing"
	"time"

	alioss "github.com/aliyun/aliyun-oss-go-sdk/oss"
	"github.com/efficientgo/core/testutil"
)

func TestParseLastModified(t *testing.T) {
	location, _ := time.LoadLocation("GMT")
	tests := map[string]struct {
		headerValue string
		expectedVal time.Time
		expectedErr string
		format      string
	}{
		"no header": {
			expectedErr: "Last-Modified header not found",
		},
		"empty format string to default RFC3339 format": {
			headerValue: "2015-11-06T10:07:11.000Z",
			expectedVal: time.Date(2015, time.November, 6, 10, 7, 11, 0, time.UTC),
			format:      "",
		},
		"valid RFC3339 header value": {
			headerValue: "2015-11-06T10:07:11.000Z",
			expectedVal: time.Date(2015, time.November, 6, 10, 7, 11, 0, time.UTC),
			format:      time.RFC3339,
		},
		"invalid RFC3339 header value": {
			headerValue: "invalid",
			expectedErr: `parse Last-Modified: parsing time "invalid" as "2006-01-02T15:04:05Z07:00": cannot parse "invalid" as "2006"`,
			format:      time.RFC3339,
		},
		"valid RFC1123 header value": {
			headerValue: "Fri, 24 Feb 2012 06:07:48 GMT",
			expectedVal: time.Date(2012, time.February, 24, 6, 7, 48, 0, location),
			format:      time.RFC1123,
		},
		"invalid RFC1123 header value": {
			headerValue: "invalid",
			expectedErr: `parse Last-Modified: parsing time "invalid" as "Mon, 02 Jan 2006 15:04:05 MST": cannot parse "invalid" as "Mon"`,
			format:      time.RFC1123,
		},
	}

	for testName, testData := range tests {
		t.Run(testName, func(t *testing.T) {
			meta := http.Header{}
			if testData.headerValue != "" {
				meta.Add(alioss.HTTPHeaderLastModified, testData.headerValue)
			}

			actual, err := ParseLastModified(meta, testData.format)

			if testData.expectedErr != "" {
				testutil.NotOk(t, err)
				testutil.Equals(t, testData.expectedErr, err.Error())
			} else {
				testutil.Ok(t, err)
				testutil.Assert(t, testData.expectedVal.Equal(actual))
			}
		})
	}
}

func TestParseContentLength(t *testing.T) {
	tests := map[string]struct {
		headerValue string
		expectedVal int64
		expectedErr string
	}{
		"no header": {
			expectedErr: "Content-Length header not found",
		},
		"invalid header value": {
			headerValue: "invalid",
			expectedErr: `convert Content-Length: strconv.ParseInt: parsing "invalid": invalid syntax`,
		},
		"valid header value": {
			headerValue: "12345",
			expectedVal: 12345,
		},
	}

	for testName, testData := range tests {
		t.Run(testName, func(t *testing.T) {
			meta := http.Header{}
			if testData.headerValue != "" {
				meta.Add(alioss.HTTPHeaderContentLength, testData.headerValue)
			}

			actual, err := ParseContentLength(meta)

			if testData.expectedErr != "" {
				testutil.NotOk(t, err)
				testutil.Equals(t, testData.expectedErr, err.Error())
			} else {
				testutil.Ok(t, err)
				testutil.Equals(t, testData.expectedVal, actual)
			}
		})
	}
}
```

## File: `errutil/multierror.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package errutil

import (
	"bytes"
	"fmt"
)

// The MultiError type implements the error interface, and contains the
// Errors used to construct it.
type MultiError []error

// Add adds the error to the error list if it is not nil.
func (es *MultiError) Add(err error) {
	if err == nil {
		return
	}
	if merr, ok := err.(NonNilMultiError); ok {
		*es = append(*es, merr...)
	} else {
		*es = append(*es, err)
	}
}

// Err returns the error list as an error or nil if it is empty.
func (es MultiError) Err() error {
	if len(es) == 0 {
		return nil
	}
	return NonNilMultiError(es)
}

type NonNilMultiError MultiError

// Returns a concatenated string of the contained errors.
func (es NonNilMultiError) Error() string {
	var buf bytes.Buffer

	if len(es) > 1 {
		fmt.Fprintf(&buf, "%d errors: ", len(es))
	}

	for i, err := range es {
		if i != 0 {
			buf.WriteString("; ")
		}
		buf.WriteString(err.Error())
	}

	return buf.String()
}
```

## File: `errutil/rt_error.go`
```go
package errutil

import (
	"net/http"

	"github.com/pkg/errors"
)

var rtErr = errors.New("RoundTripper error")

func IsMockedError(err error) bool {
	return errors.Is(err, rtErr)
}

// ErrorRoundTripper is a custom RoundTripper that always returns an error.
type ErrorRoundTripper struct {
	Err error
}

func (ert *ErrorRoundTripper) RoundTrip(*http.Request) (*http.Response, error) {
	return nil, ert.Err
}

func WrapWithErrRoundtripper(rt http.RoundTripper) http.RoundTripper {
	return &ErrorRoundTripper{Err: rtErr}
}
```

## File: `exthttp/parse.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package exthttp

import (
	"net/http"
	"strconv"
	"time"

	"github.com/pkg/errors"
)

const (
	ContentLengthHeader = "Content-Length"
	LastModifiedHeader  = "Last-Modified"
)

// ParseContentLength returns the content length (in bytes) parsed from the Content-Length
// HTTP header in input.
func ParseContentLength(m http.Header) (int64, error) {
	v, ok := m[ContentLengthHeader]
	if !ok {
		return 0, errors.Errorf("%s header not found", ContentLengthHeader)
	}

	if len(v) == 0 {
		return 0, errors.Errorf("%s header has no values", ContentLengthHeader)
	}

	ret, err := strconv.ParseInt(v[0], 10, 64)
	if err != nil {
		return 0, errors.Wrapf(err, "convert %s", ContentLengthHeader)
	}

	return ret, nil
}

// ParseLastModified returns the timestamp parsed from the Last-Modified
// HTTP header in input.
// Passing an second parameter, named f, to specify the time format.
// If f is empty then RFC3339 will be used as default format.
func ParseLastModified(m http.Header, f string) (time.Time, error) {
	const defaultFormat = time.RFC3339

	v, ok := m[LastModifiedHeader]
	if !ok {
		return time.Time{}, errors.Errorf("%s header not found", LastModifiedHeader)
	}

	if len(v) == 0 {
		return time.Time{}, errors.Errorf("%s header has no values", LastModifiedHeader)
	}

	if f == "" {
		f = defaultFormat
	}

	mod, err := time.Parse(f, v[0])
	if err != nil {
		return time.Time{}, errors.Wrapf(err, "parse %s", LastModifiedHeader)
	}

	return mod, nil
}
```

## File: `exthttp/parse_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package exthttp

import (
	"net/http"
	"testing"
	"time"

	"github.com/efficientgo/core/testutil"
)

func TestParseLastModified(t *testing.T) {
	location, _ := time.LoadLocation("GMT")
	tests := map[string]struct {
		headerValue string
		expectedVal time.Time
		expectedErr string
		format      string
	}{
		"no header": {
			expectedErr: "Last-Modified header not found",
		},
		"empty format string to default RFC3339 format": {
			headerValue: "2015-11-06T10:07:11.000Z",
			expectedVal: time.Date(2015, time.November, 6, 10, 7, 11, 0, time.UTC),
			format:      "",
		},
		"valid RFC3339 header value": {
			headerValue: "2015-11-06T10:07:11.000Z",
			expectedVal: time.Date(2015, time.November, 6, 10, 7, 11, 0, time.UTC),
			format:      time.RFC3339,
		},
		"invalid RFC3339 header value": {
			headerValue: "invalid",
			expectedErr: `parse Last-Modified: parsing time "invalid" as "2006-01-02T15:04:05Z07:00": cannot parse "invalid" as "2006"`,
			format:      time.RFC3339,
		},
		"valid RFC1123 header value": {
			headerValue: "Fri, 24 Feb 2012 06:07:48 GMT",
			expectedVal: time.Date(2012, time.February, 24, 6, 7, 48, 0, location),
			format:      time.RFC1123,
		},
		"invalid RFC1123 header value": {
			headerValue: "invalid",
			expectedErr: `parse Last-Modified: parsing time "invalid" as "Mon, 02 Jan 2006 15:04:05 MST": cannot parse "invalid" as "Mon"`,
			format:      time.RFC1123,
		},
	}

	for testName, testData := range tests {
		t.Run(testName, func(t *testing.T) {
			meta := http.Header{}
			if testData.headerValue != "" {
				meta.Add(LastModifiedHeader, testData.headerValue)
			}

			actual, err := ParseLastModified(meta, testData.format)

			if testData.expectedErr != "" {
				testutil.NotOk(t, err)
				testutil.Equals(t, testData.expectedErr, err.Error())
			} else {
				testutil.Ok(t, err)
				testutil.Assert(t, testData.expectedVal.Equal(actual))
			}
		})
	}
}

func TestParseContentLength(t *testing.T) {
	tests := map[string]struct {
		headerValue string
		expectedVal int64
		expectedErr string
	}{
		"no header": {
			expectedErr: "Content-Length header not found",
		},
		"invalid header value": {
			headerValue: "invalid",
			expectedErr: `convert Content-Length: strconv.ParseInt: parsing "invalid": invalid syntax`,
		},
		"valid header value": {
			headerValue: "12345",
			expectedVal: 12345,
		},
	}

	for testName, testData := range tests {
		t.Run(testName, func(t *testing.T) {
			meta := http.Header{}
			if testData.headerValue != "" {
				meta.Add(ContentLengthHeader, testData.headerValue)
			}

			actual, err := ParseContentLength(meta)

			if testData.expectedErr != "" {
				testutil.NotOk(t, err)
				testutil.Equals(t, testData.expectedErr, err.Error())
			} else {
				testutil.Ok(t, err)
				testutil.Equals(t, testData.expectedVal, actual)
			}
		})
	}
}
```

## File: `exthttp/tlsconfig.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package exthttp

import (
	"crypto/tls"
	"crypto/x509"
	"fmt"
	"os"
)

// TLSConfig configures the options for TLS connections.
type TLSConfig struct {
	// The CA cert to use for the targets.
	CAFile string `yaml:"ca_file"`
	// The client cert file for the targets.
	CertFile string `yaml:"cert_file"`
	// The client key file for the targets.
	KeyFile string `yaml:"key_file"`
	// Used to verify the hostname for the targets.
	ServerName string `yaml:"server_name"`
	// Disable target certificate validation.
	InsecureSkipVerify bool `yaml:"insecure_skip_verify"`
}

// NewTLSConfig creates a new tls.Config from the given TLSConfig.
func NewTLSConfig(cfg *TLSConfig) (*tls.Config, error) {
	tlsConfig := &tls.Config{InsecureSkipVerify: cfg.InsecureSkipVerify}

	// If a CA cert is provided then let's read it in.
	if len(cfg.CAFile) > 0 {
		b, err := readCAFile(cfg.CAFile)
		if err != nil {
			return nil, err
		}
		if !updateRootCA(tlsConfig, b) {
			return nil, fmt.Errorf("unable to use specified CA cert %s", cfg.CAFile)
		}
	}

	if len(cfg.ServerName) > 0 {
		tlsConfig.ServerName = cfg.ServerName
	}
	// If a client cert & key is provided then configure TLS config accordingly.
	if len(cfg.CertFile) > 0 && len(cfg.KeyFile) == 0 {
		return nil, fmt.Errorf("client cert file %q specified without client key file", cfg.CertFile)
	} else if len(cfg.KeyFile) > 0 && len(cfg.CertFile) == 0 {
		return nil, fmt.Errorf("client key file %q specified without client cert file", cfg.KeyFile)
	} else if len(cfg.CertFile) > 0 && len(cfg.KeyFile) > 0 {
		// Verify that client cert and key are valid.
		if _, err := cfg.getClientCertificate(nil); err != nil {
			return nil, err
		}
		tlsConfig.GetClientCertificate = cfg.getClientCertificate
	}

	return tlsConfig, nil
}

// readCAFile reads the CA cert file from disk.
func readCAFile(f string) ([]byte, error) {
	data, err := os.ReadFile(f)
	if err != nil {
		return nil, fmt.Errorf("unable to load specified CA cert %s: %s", f, err)
	}
	return data, nil
}

// updateRootCA parses the given byte slice as a series of PEM encoded certificates and updates tls.Config.RootCAs.
func updateRootCA(cfg *tls.Config, b []byte) bool {
	caCertPool := x509.NewCertPool()
	if !caCertPool.AppendCertsFromPEM(b) {
		return false
	}
	cfg.RootCAs = caCertPool
	return true
}

// getClientCertificate reads the pair of client cert and key from disk and returns a tls.Certificate.
func (c *TLSConfig) getClientCertificate(*tls.CertificateRequestInfo) (*tls.Certificate, error) {
	cert, err := tls.LoadX509KeyPair(c.CertFile, c.KeyFile)
	if err != nil {
		return nil, fmt.Errorf("unable to use specified client cert (%s) & key (%s): %s", c.CertFile, c.KeyFile, err)
	}
	return &cert, nil
}
```

## File: `exthttp/transport.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package exthttp

import (
	"net"
	"net/http"
	"time"

	"github.com/prometheus/common/model"
)

var DefaultHTTPConfig = HTTPConfig{
	IdleConnTimeout:       model.Duration(90 * time.Second),
	ResponseHeaderTimeout: model.Duration(2 * time.Minute),
	TLSHandshakeTimeout:   model.Duration(10 * time.Second),
	ExpectContinueTimeout: model.Duration(1 * time.Second),
	MaxIdleConns:          100,
	MaxIdleConnsPerHost:   100,
	MaxConnsPerHost:       0,
}

// HTTPConfig stores the http.Transport configuration for the cos and s3 minio client.
type HTTPConfig struct {
	IdleConnTimeout       model.Duration `yaml:"idle_conn_timeout"`
	ResponseHeaderTimeout model.Duration `yaml:"response_header_timeout"`
	InsecureSkipVerify    bool           `yaml:"insecure_skip_verify"`

	TLSHandshakeTimeout   model.Duration `yaml:"tls_handshake_timeout"`
	ExpectContinueTimeout model.Duration `yaml:"expect_continue_timeout"`
	MaxIdleConns          int            `yaml:"max_idle_conns"`
	MaxIdleConnsPerHost   int            `yaml:"max_idle_conns_per_host"`
	MaxConnsPerHost       int            `yaml:"max_conns_per_host"`

	// Transport field allows upstream callers to inject a custom round tripper.
	Transport http.RoundTripper `yaml:"-"`

	TLSConfig          TLSConfig `yaml:"tls_config"`
	DisableCompression bool      `yaml:"disable_compression"`
}

// DefaultTransport - this default transport is based on the Minio
// DefaultTransport up until the following commit:
// https://github.com/minio/minio-go/commit/008c7aa71fc17e11bf980c209a4f8c4d687fc884
// The values have since diverged.
func DefaultTransport(config HTTPConfig) (*http.Transport, error) {
	tlsConfig, err := NewTLSConfig(&config.TLSConfig)
	if err != nil {
		return nil, err
	}
	tlsConfig.InsecureSkipVerify = config.InsecureSkipVerify

	return &http.Transport{
		Proxy: http.ProxyFromEnvironment,
		DialContext: (&net.Dialer{
			Timeout:   30 * time.Second,
			KeepAlive: 30 * time.Second,
			DualStack: true,
		}).DialContext,

		MaxIdleConns:          config.MaxIdleConns,
		MaxIdleConnsPerHost:   config.MaxIdleConnsPerHost,
		IdleConnTimeout:       time.Duration(config.IdleConnTimeout),
		MaxConnsPerHost:       config.MaxConnsPerHost,
		TLSHandshakeTimeout:   time.Duration(config.TLSHandshakeTimeout),
		ExpectContinueTimeout: time.Duration(config.ExpectContinueTimeout),
		// A custom ResponseHeaderTimeout was introduced
		// to cover cases where the tcp connection works but
		// the server never answers. Defaults to 2 minutes.
		ResponseHeaderTimeout: time.Duration(config.ResponseHeaderTimeout),
		// Set this value so that the underlying transport round-tripper
		// doesn't try to auto decode the body of objects with
		// content-encoding set to `gzip`.
		//
		// Refer: https://golang.org/src/net/http/transport.go?h=roundTrip#L1843.
		TLSClientConfig: tlsConfig,
	}, nil
}
```

## File: `objtesting/acceptance_e2e_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package objtesting

import (
	"testing"

	"github.com/thanos-io/objstore"
)

// TestObjStoreAcceptanceTest_e2e tests all known implementation against interface behavior contract we agreed on.
// This ensures consistent behavior across all implementations.
// NOTE: This test assumes strong consistency, but in the same way it does not guarantee that if it passes, the
// used object store is strongly consistent.
func TestObjStore_AcceptanceTest_e2e(t *testing.T) {
	ForeachStore(t, objstore.AcceptanceTest)
}
```

## File: `objtesting/foreach.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package objtesting

import (
	"os"
	"strings"
	"testing"

	"github.com/thanos-io/objstore"
	"github.com/thanos-io/objstore/providers/azure"
	"github.com/thanos-io/objstore/providers/bos"
	"github.com/thanos-io/objstore/providers/cos"
	"github.com/thanos-io/objstore/providers/filesystem"
	"github.com/thanos-io/objstore/providers/gcs"
	"github.com/thanos-io/objstore/providers/obs"
	"github.com/thanos-io/objstore/providers/oci"
	"github.com/thanos-io/objstore/providers/oss"
	"github.com/thanos-io/objstore/providers/s3"
	"github.com/thanos-io/objstore/providers/swift"

	"github.com/efficientgo/core/testutil"
)

// IsObjStoreSkipped returns true if given provider ID is found in THANOS_TEST_OBJSTORE_SKIP array delimited by comma e.g:
// THANOS_TEST_OBJSTORE_SKIP=GCS,S3,AZURE,SWIFT,COS,ALIYUNOSS,BOS,OCI.
func IsObjStoreSkipped(t *testing.T, provider objstore.ObjProvider) bool {
	if e, ok := os.LookupEnv("THANOS_TEST_OBJSTORE_SKIP"); ok {
		obstores := strings.Split(e, ",")
		for _, objstore := range obstores {
			if objstore == string(provider) {
				t.Logf("%s found in THANOS_TEST_OBJSTORE_SKIP array. Skipping.", provider)
				return true
			}
		}
	}

	return false
}

// ForeachStore runs given test using all available objstore implementations.
// For each it creates a new bucket with a random name and a cleanup function
// that deletes it after test was run.
// Use THANOS_TEST_OBJSTORE_SKIP to skip explicitly certain object storages.
func ForeachStore(t *testing.T, testFn func(t *testing.T, bkt objstore.Bucket)) {
	t.Parallel()

	// Mandatory Inmem. Not parallel, to detect problem early.
	if ok := t.Run("inmem", func(t *testing.T) {
		testFn(t, objstore.NewInMemBucket())
	}); !ok {
		return
	}

	// Mandatory Filesystem.
	t.Run("filesystem", func(t *testing.T) {
		t.Parallel()

		dir, err := os.MkdirTemp("", "filesystem-foreach-store-test")
		testutil.Ok(t, err)
		defer testutil.Ok(t, os.RemoveAll(dir))

		b, err := filesystem.NewBucket(dir)
		testutil.Ok(t, err)
		testFn(t, b)
		testFn(t, objstore.NewPrefixedBucket(b, "some_prefix"))
	})

	// Optional GCS.
	if !IsObjStoreSkipped(t, objstore.GCS) {
		t.Run("gcs", func(t *testing.T) {
			bkt, closeFn, err := gcs.NewTestBucket(t, os.Getenv("GCP_PROJECT"))
			testutil.Ok(t, err)

			t.Parallel()
			defer closeFn()

			// TODO(bwplotka): Add goleak when https://github.com/GoogleCloudPlatform/google-cloud-go/issues/1025 is resolved.
			testFn(t, bkt)
			testFn(t, objstore.NewPrefixedBucket(bkt, "some_prefix"))
		})
	}

	// Optional S3.
	if !IsObjStoreSkipped(t, objstore.S3) {
		t.Run("aws s3", func(t *testing.T) {
			// TODO(bwplotka): Allow taking location from envvar.
			bkt, closeFn, err := s3.NewTestBucket(t, "us-west-2")
			testutil.Ok(t, err)

			t.Parallel()
			defer closeFn()

			// TODO(bwplotka): Add goleak when we fix potential leak in minio library.
			// We cannot use goleak for detecting our own potential leaks, when goleak detects leaks in minio itself.
			// This needs to be investigated more.

			testFn(t, bkt)
			testFn(t, objstore.NewPrefixedBucket(bkt, "some_prefix"))
		})
	}

	// Optional Azure.
	if !IsObjStoreSkipped(t, objstore.AZURE) {
		t.Run("azure", func(t *testing.T) {
			bkt, closeFn, err := azure.NewTestBucket(t, "e2e-tests")
			testutil.Ok(t, err)

			t.Parallel()
			defer closeFn()

			testFn(t, bkt)
			testFn(t, objstore.NewPrefixedBucket(bkt, "some_prefix"))
		})
	}

	// Optional SWIFT.
	if !IsObjStoreSkipped(t, objstore.SWIFT) {
		t.Run("swift", func(t *testing.T) {
			container, closeFn, err := swift.NewTestContainer(t)
			testutil.Ok(t, err)

			t.Parallel()
			defer closeFn()

			testFn(t, container)
			testFn(t, objstore.NewPrefixedBucket(container, "some_prefix"))
		})
	}

	// Optional COS.
	if !IsObjStoreSkipped(t, objstore.COS) {
		t.Run("Tencent cos", func(t *testing.T) {
			bkt, closeFn, err := cos.NewTestBucket(t)
			testutil.Ok(t, err)

			t.Parallel()
			defer closeFn()

			testFn(t, bkt)
			testFn(t, objstore.NewPrefixedBucket(bkt, "some_prefix"))
		})
	}

	// Optional OSS.
	if !IsObjStoreSkipped(t, objstore.ALIYUNOSS) {
		t.Run("AliYun oss", func(t *testing.T) {
			bkt, closeFn, err := oss.NewTestBucket(t)
			testutil.Ok(t, err)

			t.Parallel()
			defer closeFn()

			testFn(t, bkt)
			testFn(t, objstore.NewPrefixedBucket(bkt, "some_prefix"))
		})
	}

	// Optional BOS.
	if !IsObjStoreSkipped(t, objstore.BOS) {
		t.Run("Baidu BOS", func(t *testing.T) {
			bkt, closeFn, err := bos.NewTestBucket(t)
			testutil.Ok(t, err)

			t.Parallel()
			defer closeFn()

			testFn(t, bkt)
			testFn(t, objstore.NewPrefixedBucket(bkt, "some_prefix"))
		})
	}

	// Optional OCI.
	if !IsObjStoreSkipped(t, objstore.OCI) {
		t.Run("oci", func(t *testing.T) {
			bkt, closeFn, err := oci.NewTestBucket(t)
			testutil.Ok(t, err)

			t.Parallel()
			defer closeFn()

			testFn(t, bkt)
		})
	}

	// Optional OBS.
	if !IsObjStoreSkipped(t, objstore.OBS) {
		t.Run("obs", func(t *testing.T) {
			bkt, closeFn, err := obs.NewTestBucket(t, "cn-south-1")
			testutil.Ok(t, err)

			t.Parallel()
			defer closeFn()

			testFn(t, bkt)
			testFn(t, objstore.NewPrefixedBucket(bkt, "some_prefix"))
		})
	}
}
```

## File: `providers/azure/azure.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package azure

import (
	"context"
	"io"
	"net/http"
	"os"
	"strings"
	"testing"
	"time"

	"github.com/Azure/azure-sdk-for-go/sdk/azcore/to"
	"github.com/Azure/azure-sdk-for-go/sdk/storage/azblob"
	"github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/blob"
	"github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/bloberror"
	"github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/blockblob"
	"github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/container"
	"github.com/go-kit/log"
	"github.com/go-kit/log/level"
	"github.com/pkg/errors"
	"github.com/prometheus/common/model"
	"gopkg.in/yaml.v2"

	"github.com/thanos-io/objstore"
	"github.com/thanos-io/objstore/exthttp"
)

// DefaultConfig for Azure objstore client.
var DefaultConfig = Config{
	Endpoint:               "blob.core.windows.net",
	StorageCreateContainer: true,
	HTTPConfig: exthttp.HTTPConfig{
		IdleConnTimeout:       model.Duration(90 * time.Second),
		ResponseHeaderTimeout: model.Duration(2 * time.Minute),
		TLSHandshakeTimeout:   model.Duration(10 * time.Second),
		ExpectContinueTimeout: model.Duration(1 * time.Second),
		MaxIdleConns:          100,
		MaxIdleConnsPerHost:   100,
		MaxConnsPerHost:       0,
		DisableCompression:    false,
	},
}

// Config Azure storage configuration.
type Config struct {
	AzTenantID              string             `yaml:"az_tenant_id"`
	ClientID                string             `yaml:"client_id"`
	ClientSecret            string             `yaml:"client_secret"`
	StorageAccountName      string             `yaml:"storage_account"`
	StorageAccountKey       string             `yaml:"storage_account_key"`
	StorageConnectionString string             `yaml:"storage_connection_string"`
	StorageCreateContainer  bool               `yaml:"storage_create_container"`
	ContainerName           string             `yaml:"container"`
	Endpoint                string             `yaml:"endpoint"`
	UserAssignedID          string             `yaml:"user_assigned_id"`
	MaxRetries              int                `yaml:"max_retries"`
	ReaderConfig            ReaderConfig       `yaml:"reader_config"`
	PipelineConfig          PipelineConfig     `yaml:"pipeline_config"`
	HTTPConfig              exthttp.HTTPConfig `yaml:"http_config"`

	// Deprecated: Is automatically set by the Azure SDK.
	MSIResource string `yaml:"msi_resource"`
}

type ReaderConfig struct {
	MaxRetryRequests int `yaml:"max_retry_requests"`
}

type PipelineConfig struct {
	MaxTries      int32          `yaml:"max_tries"`
	TryTimeout    model.Duration `yaml:"try_timeout"`
	RetryDelay    model.Duration `yaml:"retry_delay"`
	MaxRetryDelay model.Duration `yaml:"max_retry_delay"`
}

// Validate checks to see if any of the config options are set.
func (conf *Config) validate() error {
	var errMsg []string
	if conf.UserAssignedID != "" && conf.StorageAccountKey != "" {
		errMsg = append(errMsg, "user_assigned_id cannot be set when using storage_account_key authentication")
	}

	if conf.UserAssignedID != "" && conf.StorageConnectionString != "" {
		errMsg = append(errMsg, "user_assigned_id cannot be set when using storage_connection_string authentication")
	}

	if conf.UserAssignedID != "" && conf.ClientID != "" {
		errMsg = append(errMsg, "user_assigned_id cannot be set when using client_id authentication")
	}

	if (conf.AzTenantID != "" || conf.ClientSecret != "" || conf.ClientID != "") && (conf.AzTenantID == "" || conf.ClientSecret == "" || conf.ClientID == "") {
		errMsg = append(errMsg, "az_tenant_id, client_id, and client_secret must be set together")
	}

	if conf.StorageAccountKey != "" && conf.StorageConnectionString != "" {
		errMsg = append(errMsg, "storage_account_key and storage_connection_string cannot both be set")
	}

	if conf.StorageAccountName == "" {
		errMsg = append(errMsg, "storage_account_name is required but not configured")
	}

	if conf.ContainerName == "" {
		errMsg = append(errMsg, "no container specified")
	}

	if conf.PipelineConfig.MaxTries < 0 {
		errMsg = append(errMsg, "The value of max_tries must be greater than or equal to 0 in the config file")
	}

	if conf.ReaderConfig.MaxRetryRequests < 0 {
		errMsg = append(errMsg, "The value of max_retry_requests must be greater than or equal to 0 in the config file")
	}

	if len(errMsg) > 0 {
		return errors.New(strings.Join(errMsg, ", "))
	}

	return nil
}

// HTTPConfig exists here only because Cortex depends on it, and we depend on Cortex.
// Deprecated.
// TODO(bwplotka): Remove it, once we remove Cortex cycle dep, or Cortex stops using this.
type HTTPConfig = exthttp.HTTPConfig

// parseConfig unmarshals a buffer into a Config with default values.
func parseConfig(conf []byte) (Config, error) {
	config := DefaultConfig
	if err := yaml.UnmarshalStrict(conf, &config); err != nil {
		return Config{}, err
	}

	// If we don't have config specific retry values but we do have the generic MaxRetries.
	// This is for backwards compatibility but also ease of configuration.
	if config.MaxRetries > 0 {
		if config.PipelineConfig.MaxTries == 0 {
			config.PipelineConfig.MaxTries = int32(config.MaxRetries)
		}
		if config.ReaderConfig.MaxRetryRequests == 0 {
			config.ReaderConfig.MaxRetryRequests = config.MaxRetries
		}
	}

	return config, nil
}

// Bucket implements the store.Bucket interface against Azure APIs.
type Bucket struct {
	logger           log.Logger
	containerClient  *container.Client
	containerName    string
	readerMaxRetries int
}

// NewBucket returns a new Bucket using the provided Azure config.
func NewBucket(logger log.Logger, azureConfig []byte, component string, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Bucket, error) {
	level.Debug(logger).Log("msg", "creating new Azure bucket connection", "component", component)
	conf, err := parseConfig(azureConfig)
	if err != nil {
		return nil, err
	}
	if conf.MSIResource != "" {
		level.Warn(logger).Log("msg", "The field msi_resource has been deprecated and should no longer be set")
	}
	return NewBucketWithConfig(logger, conf, component, wrapRoundtripper)
}

// NewBucketWithConfig returns a new Bucket using the provided Azure config struct.
func NewBucketWithConfig(logger log.Logger, conf Config, component string, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Bucket, error) {
	if err := conf.validate(); err != nil {
		return nil, err
	}

	containerClient, err := getContainerClient(conf, wrapRoundtripper)
	if err != nil {
		return nil, err
	}

	// Check if storage account container already exists, and create one if it does not.
	if conf.StorageCreateContainer {
		ctx := context.Background()
		_, err = containerClient.GetProperties(ctx, &container.GetPropertiesOptions{})
		if err != nil {
			if !bloberror.HasCode(err, bloberror.ContainerNotFound) {
				return nil, err
			}
			_, err := containerClient.Create(ctx, nil)
			if err != nil {
				return nil, errors.Wrapf(err, "error creating Azure blob container: %s", conf.ContainerName)
			}
			level.Info(logger).Log("msg", "Azure blob container successfully created", "address", conf.ContainerName)
		}
	}
	bkt := &Bucket{
		logger:           logger,
		containerClient:  containerClient,
		containerName:    conf.ContainerName,
		readerMaxRetries: conf.ReaderConfig.MaxRetryRequests,
	}
	return bkt, nil
}

func (b *Bucket) Provider() objstore.ObjProvider { return objstore.AZURE }

func (b *Bucket) SupportedIterOptions() []objstore.IterOptionType {
	return []objstore.IterOptionType{objstore.Recursive, objstore.UpdatedAt}
}

func (b *Bucket) IterWithAttributes(ctx context.Context, dir string, f func(attrs objstore.IterObjectAttributes) error, options ...objstore.IterOption) error {
	if err := objstore.ValidateIterOptions(b.SupportedIterOptions(), options...); err != nil {
		return err
	}

	prefix := dir
	if prefix != "" && !strings.HasSuffix(prefix, DirDelim) {
		prefix += DirDelim
	}

	params := objstore.ApplyIterOptions(options...)
	if params.Recursive {
		opt := &container.ListBlobsFlatOptions{Prefix: &prefix}
		pager := b.containerClient.NewListBlobsFlatPager(opt)
		for pager.More() {
			resp, err := pager.NextPage(ctx)
			if err != nil {
				return err
			}
			for _, blob := range resp.Segment.BlobItems {
				attrs := objstore.IterObjectAttributes{
					Name: *blob.Name,
				}
				if params.LastModified {
					attrs.SetLastModified(*blob.Properties.LastModified)
				}
				if err := f(attrs); err != nil {
					return err
				}
			}
		}
		return nil
	}

	opt := &container.ListBlobsHierarchyOptions{Prefix: &prefix}
	pager := b.containerClient.NewListBlobsHierarchyPager(DirDelim, opt)
	for pager.More() {
		resp, err := pager.NextPage(ctx)
		if err != nil {
			return err
		}
		for _, blobItem := range resp.Segment.BlobItems {
			attrs := objstore.IterObjectAttributes{
				Name: *blobItem.Name,
			}
			if params.LastModified {
				attrs.SetLastModified(*blobItem.Properties.LastModified)
			}
			if err := f(attrs); err != nil {
				return err
			}
		}
		for _, blobPrefix := range resp.Segment.BlobPrefixes {
			if err := f(objstore.IterObjectAttributes{Name: *blobPrefix.Name}); err != nil {
				return err
			}
		}
	}
	return nil
}

// Iter calls f for each entry in the given directory. The argument to f is the full
// object name including the prefix of the inspected directory.
func (b *Bucket) Iter(ctx context.Context, dir string, f func(string) error, opts ...objstore.IterOption) error {
	// Only include recursive option since attributes are not used in this method.
	var filteredOpts []objstore.IterOption
	for _, opt := range opts {
		if opt.Type == objstore.Recursive {
			filteredOpts = append(filteredOpts, opt)
			break
		}
	}

	return b.IterWithAttributes(ctx, dir, func(attrs objstore.IterObjectAttributes) error {
		return f(attrs.Name)
	}, filteredOpts...)
}

// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
func (b *Bucket) IsObjNotFoundErr(err error) bool {
	if err == nil {
		return false
	}
	return bloberror.HasCode(err, bloberror.BlobNotFound) || bloberror.HasCode(err, bloberror.InvalidURI)
}

// IsAccessDeniedErr returns true if access to object is denied.
func (b *Bucket) IsAccessDeniedErr(err error) bool {
	if err == nil {
		return false
	}
	return bloberror.HasCode(err, bloberror.AuthorizationPermissionMismatch) || bloberror.HasCode(err, bloberror.InsufficientAccountPermissions)
}

func (b *Bucket) getBlobReader(ctx context.Context, name string, httpRange blob.HTTPRange) (io.ReadCloser, error) {
	level.Debug(b.logger).Log("msg", "getting blob", "blob", name, "offset", httpRange.Offset, "length", httpRange.Count)
	if name == "" {
		return nil, errors.New("blob name cannot be empty")
	}
	blobClient := b.containerClient.NewBlobClient(name)
	downloadOpt := &blob.DownloadStreamOptions{
		Range: httpRange,
	}
	resp, err := blobClient.DownloadStream(ctx, downloadOpt)
	if err != nil {
		return nil, errors.Wrapf(err, "cannot download blob, address: %s", blobClient.URL())
	}
	retryOpts := azblob.RetryReaderOptions{MaxRetries: int32(b.readerMaxRetries)}

	return objstore.ObjectSizerReadCloser{
		ReadCloser: resp.NewRetryReader(ctx, &retryOpts),
		Size: func() (int64, error) {
			return *resp.ContentLength, nil
		},
	}, nil
}

// Get returns a reader for the given object name.
func (b *Bucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	return b.getBlobReader(ctx, name, blob.HTTPRange{})
}

// GetRange returns a new range reader for the given object name and range.
func (b *Bucket) GetRange(ctx context.Context, name string, offset, length int64) (io.ReadCloser, error) {
	return b.getBlobReader(ctx, name, blob.HTTPRange{Offset: offset, Count: length})
}

// Attributes returns information about the specified object.
func (b *Bucket) Attributes(ctx context.Context, name string) (objstore.ObjectAttributes, error) {
	level.Debug(b.logger).Log("msg", "Getting blob attributes", "blob", name)
	blobClient := b.containerClient.NewBlobClient(name)
	resp, err := blobClient.GetProperties(ctx, nil)
	if err != nil {
		return objstore.ObjectAttributes{}, err
	}
	return objstore.ObjectAttributes{
		Size:         *resp.ContentLength,
		LastModified: *resp.LastModified,
	}, nil
}

// Exists checks if the given object exists.
func (b *Bucket) Exists(ctx context.Context, name string) (bool, error) {
	level.Debug(b.logger).Log("msg", "checking if blob exists", "blob", name)
	blobClient := b.containerClient.NewBlobClient(name)
	if _, err := blobClient.GetProperties(ctx, nil); err != nil {
		if b.IsObjNotFoundErr(err) {
			return false, nil
		}
		return false, errors.Wrapf(err, "cannot get properties for Azure blob, address: %s", name)
	}
	return true, nil
}

// Upload the contents of the reader as an object into the bucket.
func (b *Bucket) Upload(ctx context.Context, name string, r io.Reader, uploadOpts ...objstore.ObjectUploadOption) error {
	level.Debug(b.logger).Log("msg", "uploading blob", "blob", name)
	blobClient := b.containerClient.NewBlockBlobClient(name)

	uploadOptions := objstore.ApplyObjectUploadOptions(uploadOpts...)
	opts := &blockblob.UploadStreamOptions{
		BlockSize:   3 * 1024 * 1024,
		Concurrency: 4,
		HTTPHeaders: &blob.HTTPHeaders{
			BlobContentType: &uploadOptions.ContentType,
		},
	}
	if _, err := blobClient.UploadStream(ctx, r, opts); err != nil {
		return errors.Wrapf(err, "cannot upload Azure blob, address: %s", name)
	}
	return nil
}

// Delete removes the object with the given name.
func (b *Bucket) Delete(ctx context.Context, name string) error {
	level.Debug(b.logger).Log("msg", "deleting blob", "blob", name)
	blobClient := b.containerClient.NewBlobClient(name)
	opt := &blob.DeleteOptions{
		DeleteSnapshots: to.Ptr(blob.DeleteSnapshotsOptionTypeInclude),
	}
	if _, err := blobClient.Delete(ctx, opt); err != nil {
		return errors.Wrapf(err, "error deleting blob, address: %s", name)
	}
	return nil
}

// Name returns Azure container name.
func (b *Bucket) Name() string {
	return b.containerName
}

// NewTestBucket creates test bkt client that before returning creates temporary bucket.
// In a close function it empties and deletes the bucket.
func NewTestBucket(t testing.TB, component string) (objstore.Bucket, func(), error) {
	t.Log("Using test Azure bucket.")

	conf := &DefaultConfig
	conf.StorageAccountName = os.Getenv("AZURE_STORAGE_ACCOUNT")
	conf.StorageAccountKey = os.Getenv("AZURE_STORAGE_ACCESS_KEY")
	conf.ContainerName = objstore.CreateTemporaryTestBucketName(t)

	bc, err := yaml.Marshal(conf)
	if err != nil {
		return nil, nil, err
	}
	bkt, err := NewBucket(log.NewNopLogger(), bc, component, nil)
	if err != nil {
		t.Errorf("Cannot create Azure storage container:")
		return nil, nil, err
	}
	ctx := context.Background()
	return bkt, func() {
		objstore.EmptyBucket(t, ctx, bkt)
		_, err := bkt.containerClient.Delete(ctx, &container.DeleteOptions{})
		if err != nil {
			t.Logf("deleting bucket failed: %s", err)
		}
	}, nil
}

// Close bucket.
func (b *Bucket) Close() error {
	return nil
}
```

## File: `providers/azure/azure_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package azure

import (
	"testing"
	"time"

	"github.com/efficientgo/core/testutil"
	"github.com/go-kit/log"

	"github.com/thanos-io/objstore/errutil"
	"github.com/thanos-io/objstore/exthttp"
)

type TestCase struct {
	name             string
	config           []byte
	wantFailParse    bool
	wantFailValidate bool
}

var validConfig = []byte(`storage_account: "myStorageAccount"
storage_account_key: "bXlTdXBlclNlY3JldEtleTEyMyFAIw=="
container: "MyContainer"
endpoint: "blob.core.windows.net"
reader_config:
  "max_retry_requests": 100
pipeline_config:
  "try_timeout": 0`)

var tests = []TestCase{
	{
		name:             "validConfig",
		config:           validConfig,
		wantFailParse:    false,
		wantFailValidate: false,
	},
	{
		name: "Missing storage account",
		config: []byte(`storage_account: ""
storage_account_key: "abc123"
container: "MyContainer"
endpoint: "blob.core.windows.net"
reader_config:
  "max_retry_requests": 100
pipeline_config:
  "try_timeout": 0`),
		wantFailParse:    false,
		wantFailValidate: true,
	},
	{
		name: "Negative max_tries",
		config: []byte(`storage_account: "asdfasdf"
storage_account_key: "asdfsdf"
container: "MyContainer"
endpoint: "not.valid"
reader_config:
  "max_retry_requests": 100
pipeline_config:
  "max_tries": -1
  "try_timeout": 0`),
		wantFailParse:    false,
		wantFailValidate: true,
	},
	{
		name: "Negative max_retry_requests",
		config: []byte(`storage_account: "asdfasdf"
storage_account_key: "asdfsdf"
container: "MyContainer"
endpoint: "not.valid"
reader_config:
  "max_retry_requests": -100
pipeline_config:
  "try_timeout": 0`),
		wantFailParse:    false,
		wantFailValidate: true,
	},
	{
		name: "Not a Duration",
		config: []byte(`storage_account: "asdfasdf"
storage_account_key: "asdfsdf"
container: "MyContainer"
endpoint: "not.valid"
reader_config:
  "max_retry_requests": 100
pipeline_config:
  "try_timeout": 10`),
		wantFailParse:    true,
		wantFailValidate: true,
	},
	{
		name: "Valid Duration",
		config: []byte(`storage_account: "asdfasdf"
storage_account_key: "asdfsdf"
container: "MyContainer"
endpoint: "not.valid"
reader_config:
  "max_retry_requests": 100
pipeline_config:
  "try_timeout": "10s"`),
		wantFailParse:    false,
		wantFailValidate: false,
	},
	{
		name: "Valid MSI Resource",
		config: []byte(`storage_account: "myAccount"
storage_account_key: ""
container: "MyContainer"
endpoint: "not.valid"
reader_config:
  "max_retry_requests": 100
pipeline_config:
  "try_timeout": "10s"`),
		wantFailParse:    false,
		wantFailValidate: false,
	},
	{
		name: "Valid User Assigned Identity Config without Resource",
		config: []byte(`storage_account: "myAccount"
storage_account_key: ""
user_assigned_id: "1234-56578678-655"
container: "MyContainer"`),
		wantFailParse:    false,
		wantFailValidate: false,
	},
	{
		name: "Valid User Assigned Identity Config with Resource",
		config: []byte(`storage_account: "myAccount"
storage_account_key: ""
user_assigned_id: "1234-56578678-655"
container: "MyContainer"`),
		wantFailParse:    false,
		wantFailValidate: false,
	},
	{
		name: "Valid User Assigned and Connection String set",
		config: []byte(`storage_account: "myAccount"
storage_account_key: ""
user_assigned_id: "1234-56578678-655"
storage_connection_string: "myConnectionString"
container: "MyContainer"`),
		wantFailParse:    false,
		wantFailValidate: true,
	},
	{
		name: "Valid AzTenantID, ClientID, ClientSecret",
		config: []byte(`storage_account: "myAccount"
storage_account_key: ""
az_tenant_id: "1234-56578678-655"
client_id: "1234-56578678-655"
client_secret: "1234-56578678-655"
container: "MyContainer"`),
		wantFailParse:    false,
		wantFailValidate: false,
	},
	{
		name: "Valid ClientID and ClientSecret but missing AzTenantID",
		config: []byte(`storage_account: "myAccount"
storage_account_key: ""
client_id: "1234-56578678-655"
client_secret: "1234-56578678-655"
container: "MyContainer"`),
		wantFailParse:    false,
		wantFailValidate: true,
	},
}

func TestConfig_validate(t *testing.T) {

	for _, testCase := range tests {

		conf, err := parseConfig(testCase.config)

		if (err != nil) != testCase.wantFailParse {
			t.Errorf("%s error = %v, wantFailParse %v", testCase.name, err, testCase.wantFailParse)
			continue
		}

		validateErr := conf.validate()
		if (validateErr != nil) != testCase.wantFailValidate {
			t.Errorf("%s error = %v, wantFailValidate %v", testCase.name, validateErr, testCase.wantFailValidate)
		}
	}

}

func TestParseConfig_DefaultHTTPConfig(t *testing.T) {

	cfg, err := parseConfig(validConfig)
	testutil.Ok(t, err)

	if time.Duration(cfg.HTTPConfig.IdleConnTimeout) != time.Duration(90*time.Second) {
		t.Errorf("parsing of idle_conn_timeout failed: got %v, expected %v",
			time.Duration(cfg.HTTPConfig.IdleConnTimeout), time.Duration(90*time.Second))
	}

	if time.Duration(cfg.HTTPConfig.ResponseHeaderTimeout) != time.Duration(2*time.Minute) {
		t.Errorf("parsing of response_header_timeout failed: got %v, expected %v",
			time.Duration(cfg.HTTPConfig.IdleConnTimeout), time.Duration(2*time.Minute))
	}

	if cfg.HTTPConfig.InsecureSkipVerify {
		t.Errorf("parsing of insecure_skip_verify failed: got %v, expected %v", cfg.HTTPConfig.InsecureSkipVerify, false)
	}
}

func TestParseConfig_CustomHTTPConfigWithTLS(t *testing.T) {
	input := []byte(`storage_account: "myStorageAccount"
storage_account_key: "abc123"
container: "MyContainer"
endpoint: "blob.core.windows.net"
http_config:
  tls_config:
    ca_file: /certs/ca.crt
    cert_file: /certs/cert.crt
    key_file: /certs/key.key
    server_name: server
    insecure_skip_verify: false
  `)
	cfg, err := parseConfig(input)
	testutil.Ok(t, err)

	testutil.Equals(t, "/certs/ca.crt", cfg.HTTPConfig.TLSConfig.CAFile)
	testutil.Equals(t, "/certs/cert.crt", cfg.HTTPConfig.TLSConfig.CertFile)
	testutil.Equals(t, "/certs/key.key", cfg.HTTPConfig.TLSConfig.KeyFile)
	testutil.Equals(t, "server", cfg.HTTPConfig.TLSConfig.ServerName)
	testutil.Equals(t, false, cfg.HTTPConfig.TLSConfig.InsecureSkipVerify)
}

func TestParseConfig_CustomLegacyInsecureSkipVerify(t *testing.T) {
	input := []byte(`storage_account: "myStorageAccount"
storage_account_key: "abc123"
container: "MyContainer"
endpoint: "blob.core.windows.net"
http_config:
  insecure_skip_verify: true
  tls_config:
    insecure_skip_verify: false
  `)
	cfg, err := parseConfig(input)
	testutil.Ok(t, err)
	transport, err := exthttp.DefaultTransport(cfg.HTTPConfig)
	testutil.Ok(t, err)
	testutil.Equals(t, true, transport.TLSClientConfig.InsecureSkipVerify)
}

func TestNewBucketWithErrorRoundTripper(t *testing.T) {
	cfg, err := parseConfig(validConfig)
	testutil.Ok(t, err)

	_, err = NewBucketWithConfig(log.NewNopLogger(), cfg, "test", errutil.WrapWithErrRoundtripper)

	// We expect an error from the RoundTripper
	testutil.NotOk(t, err)
	testutil.Assert(t, errutil.IsMockedError(err), "Expected RoundTripper error, got: %v", err)
}
```

## File: `providers/azure/helpers.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package azure

import (
	"fmt"
	"net/http"
	"time"

	"github.com/Azure/azure-sdk-for-go/sdk/azcore"
	"github.com/Azure/azure-sdk-for-go/sdk/azcore/policy"
	"github.com/Azure/azure-sdk-for-go/sdk/azidentity"
	"github.com/Azure/azure-sdk-for-go/sdk/storage/azblob/container"

	"github.com/thanos-io/objstore/exthttp"
)

// DirDelim is the delimiter used to model a directory structure in an object store bucket.
const DirDelim = "/"

func getContainerClient(conf Config, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*container.Client, error) {
	var rt http.RoundTripper
	rt, err := exthttp.DefaultTransport(conf.HTTPConfig)
	if err != nil {
		return nil, err
	}
	if conf.HTTPConfig.Transport != nil {
		rt = conf.HTTPConfig.Transport
	}
	if wrapRoundtripper != nil {
		rt = wrapRoundtripper(rt)
	}
	opt := &container.ClientOptions{
		ClientOptions: azcore.ClientOptions{
			Retry: policy.RetryOptions{
				MaxRetries:    conf.PipelineConfig.MaxTries,
				TryTimeout:    time.Duration(conf.PipelineConfig.TryTimeout),
				RetryDelay:    time.Duration(conf.PipelineConfig.RetryDelay),
				MaxRetryDelay: time.Duration(conf.PipelineConfig.MaxRetryDelay),
			},
			Telemetry: policy.TelemetryOptions{
				ApplicationID: "Thanos",
			},
			Transport: &http.Client{Transport: rt},
		},
	}

	// Use connection string if set
	if conf.StorageConnectionString != "" {
		containerClient, err := container.NewClientFromConnectionString(conf.StorageConnectionString, conf.ContainerName, opt)
		if err != nil {
			return nil, err
		}
		return containerClient, nil
	}

	containerURL := fmt.Sprintf("https://%s.%s/%s", conf.StorageAccountName, conf.Endpoint, conf.ContainerName)

	// Use shared keys if set
	if conf.StorageAccountKey != "" {
		cred, err := container.NewSharedKeyCredential(conf.StorageAccountName, conf.StorageAccountKey)
		if err != nil {
			return nil, err
		}
		containerClient, err := container.NewClientWithSharedKeyCredential(containerURL, cred, opt)
		if err != nil {
			return nil, err
		}
		return containerClient, nil
	}

	// Otherwise use a token credential
	cred, err := getTokenCredential(conf)

	if err != nil {
		return nil, err
	}

	containerClient, err := container.NewClient(containerURL, cred, opt)
	if err != nil {
		return nil, err
	}

	return containerClient, nil
}

func getTokenCredential(conf Config) (azcore.TokenCredential, error) {
	if conf.ClientSecret != "" && conf.AzTenantID != "" && conf.ClientID != "" {
		return azidentity.NewClientSecretCredential(conf.AzTenantID, conf.ClientID, conf.ClientSecret, &azidentity.ClientSecretCredentialOptions{})
	}

	if conf.UserAssignedID == "" {
		return azidentity.NewDefaultAzureCredential(nil)
	}

	msiOpt := &azidentity.ManagedIdentityCredentialOptions{}
	msiOpt.ID = azidentity.ClientID(conf.UserAssignedID)
	return azidentity.NewManagedIdentityCredential(msiOpt)
}
```

## File: `providers/bos/bos.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package bos

import (
	"context"
	"fmt"
	"io"
	"math"
	"math/rand"
	"net/http"
	"os"
	"strings"
	"testing"
	"time"

	"github.com/baidubce/bce-sdk-go/bce"
	"github.com/baidubce/bce-sdk-go/services/bos"
	"github.com/baidubce/bce-sdk-go/services/bos/api"
	"github.com/go-kit/log"
	"github.com/pkg/errors"
	"gopkg.in/yaml.v2"

	"github.com/thanos-io/objstore"
)

// partSize 128MB.
const partSize = 1024 * 1024 * 128

// Bucket implements the store.Bucket interface against bos-compatible(Baidu Object Storage) APIs.
type Bucket struct {
	logger log.Logger
	client *bos.Client
	name   string
}

// Config encapsulates the necessary config values to instantiate an bos client.
type Config struct {
	Bucket    string `yaml:"bucket"`
	Endpoint  string `yaml:"endpoint"`
	AccessKey string `yaml:"access_key"`
	SecretKey string `yaml:"secret_key"`
}

func (conf *Config) validate() error {
	if conf.Bucket == "" ||
		conf.Endpoint == "" ||
		conf.AccessKey == "" ||
		conf.SecretKey == "" {
		return errors.New("insufficient BOS configuration information")
	}

	return nil
}

// parseConfig unmarshal a buffer into a Config with default HTTPConfig values.
func parseConfig(conf []byte) (Config, error) {
	config := Config{}
	if err := yaml.Unmarshal(conf, &config); err != nil {
		return Config{}, err
	}

	return config, nil
}

// NewBucket new bos bucket.
func NewBucket(logger log.Logger, conf []byte, component string) (*Bucket, error) {
	// TODO(https://github.com/thanos-io/objstore/pull/150): Add support for roundtripper wrapper.
	if logger == nil {
		logger = log.NewNopLogger()
	}

	config, err := parseConfig(conf)
	if err != nil {
		return nil, errors.Wrap(err, "parsing BOS configuration")
	}

	return NewBucketWithConfig(logger, config, component)
}

// NewBucketWithConfig returns a new Bucket using the provided bos config struct.
func NewBucketWithConfig(logger log.Logger, config Config, component string) (*Bucket, error) {
	if err := config.validate(); err != nil {
		return nil, errors.Wrap(err, "validating BOS configuration")
	}

	client, err := bos.NewClient(config.AccessKey, config.SecretKey, config.Endpoint)
	if err != nil {
		return nil, errors.Wrap(err, "creating BOS client")
	}

	client.Config.UserAgent = fmt.Sprintf("thanos-%s", component)

	bkt := &Bucket{
		logger: logger,
		client: client,
		name:   config.Bucket,
	}
	return bkt, nil
}

func (b *Bucket) Provider() objstore.ObjProvider { return objstore.BOS }

// Name returns the bucket name for the provider.
func (b *Bucket) Name() string {
	return b.name
}

// Delete removes the object with the given name.
func (b *Bucket) Delete(_ context.Context, name string) error {
	return b.client.DeleteObject(b.name, name)
}

// Upload the contents of the reader as an object into the bucket.
func (b *Bucket) Upload(_ context.Context, name string, r io.Reader, opts ...objstore.ObjectUploadOption) error {
	size, err := objstore.TryToGetSize(r)
	if err != nil {
		return errors.Wrapf(err, "getting size of %s", name)
	}

	uploadOpts := objstore.ApplyObjectUploadOptions(opts...)
	partNums, lastSlice := int(math.Floor(float64(size)/partSize)), size%partSize
	if partNums == 0 {
		body, err := bce.NewBodyFromSizedReader(r, lastSlice)
		if err != nil {
			return errors.Wrapf(err, "failed to create SizedReader for %s", name)
		}

		if _, err := b.client.PutObject(b.name, name, body, &api.PutObjectArgs{ContentType: uploadOpts.ContentType}); err != nil {
			return errors.Wrapf(err, "failed to upload %s", name)
		}

		return nil
	}

	result, err := b.client.InitiateMultipartUpload(b.name, name, uploadOpts.ContentType, nil)
	if err != nil {
		return errors.Wrapf(err, "failed to initiate MultipartUpload for %s", name)
	}

	uploadEveryPart := func(partSize int64, part int, uploadId string) (string, error) {
		body, err := bce.NewBodyFromSizedReader(r, partSize)
		if err != nil {
			return "", err
		}

		etag, err := b.client.UploadPart(b.name, name, uploadId, part, body, nil)
		if err != nil {
			if err := b.client.AbortMultipartUpload(b.name, name, uploadId); err != nil {
				return etag, err
			}
			return etag, err
		}
		return etag, nil
	}

	var parts []api.UploadInfoType

	for part := 1; part <= partNums; part++ {
		etag, err := uploadEveryPart(partSize, part, result.UploadId)
		if err != nil {
			return errors.Wrapf(err, "failed to upload part %d for %s", part, name)
		}
		parts = append(parts, api.UploadInfoType{PartNumber: part, ETag: etag})
	}

	if lastSlice != 0 {
		etag, err := uploadEveryPart(lastSlice, partNums+1, result.UploadId)
		if err != nil {
			return errors.Wrapf(err, "failed to upload the last part for %s", name)
		}
		parts = append(parts, api.UploadInfoType{PartNumber: partNums + 1, ETag: etag})
	}

	if _, err := b.client.CompleteMultipartUploadFromStruct(b.name, name, result.UploadId, &api.CompleteMultipartUploadArgs{Parts: parts}); err != nil {
		return errors.Wrapf(err, "failed to set %s upload completed", name)
	}
	return nil
}

func (b *Bucket) SupportedIterOptions() []objstore.IterOptionType {
	return []objstore.IterOptionType{objstore.Recursive, objstore.UpdatedAt}
}

func (b *Bucket) IterWithAttributes(ctx context.Context, dir string, f func(attrs objstore.IterObjectAttributes) error, options ...objstore.IterOption) error {
	if err := objstore.ValidateIterOptions(b.SupportedIterOptions(), options...); err != nil {
		return err
	}

	if dir != "" {
		dir = strings.TrimSuffix(dir, objstore.DirDelim) + objstore.DirDelim
	}

	delimiter := objstore.DirDelim

	params := objstore.ApplyIterOptions(options...)
	if params.Recursive {
		delimiter = ""
	}

	var marker string
	for {
		if err := ctx.Err(); err != nil {
			return err
		}

		objects, err := b.client.ListObjects(b.name, &api.ListObjectsArgs{
			Delimiter: delimiter,
			Marker:    marker,
			MaxKeys:   1000,
			Prefix:    dir,
		})
		if err != nil {
			return err
		}

		marker = objects.NextMarker
		for _, object := range objects.Contents {
			attrs := objstore.IterObjectAttributes{
				Name: object.Key,
			}

			if params.LastModified && object.LastModified != "" {
				lastModified, err := time.Parse(time.RFC1123, object.LastModified)
				if err != nil {
					return fmt.Errorf("iter: get last modified: %w", err)
				}
				attrs.SetLastModified(lastModified)
			}

			if err := f(attrs); err != nil {
				return err
			}
		}

		for _, object := range objects.CommonPrefixes {
			if err := f(objstore.IterObjectAttributes{Name: object.Prefix}); err != nil {
				return err
			}
		}
		if !objects.IsTruncated {
			break
		}
	}
	return nil
}

// Iter calls f for each entry in the given directory. The argument to f is the full
// object name including the prefix of the inspected directory.
func (b *Bucket) Iter(ctx context.Context, dir string, f func(string) error, opts ...objstore.IterOption) error {
	// Only include recursive option since attributes are not used in this method.
	var filteredOpts []objstore.IterOption
	for _, opt := range opts {
		if opt.Type == objstore.Recursive {
			filteredOpts = append(filteredOpts, opt)
			break
		}
	}

	return b.IterWithAttributes(ctx, dir, func(attrs objstore.IterObjectAttributes) error {
		return f(attrs.Name)
	}, filteredOpts...)
}

// Get returns a reader for the given object name.
func (b *Bucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	return b.getRange(ctx, b.name, name, 0, -1)
}

// GetRange returns a new range reader for the given object name and range.
func (b *Bucket) GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	return b.getRange(ctx, b.name, name, off, length)
}

// Exists checks if the given object exists in the bucket.
func (b *Bucket) Exists(_ context.Context, name string) (bool, error) {
	_, err := b.client.GetObjectMeta(b.name, name)
	if err != nil {
		if b.IsObjNotFoundErr(err) {
			return false, nil
		}
		return false, errors.Wrapf(err, "getting object metadata of %s", name)
	}
	return true, nil
}

func (b *Bucket) Close() error {
	return nil
}

// ObjectSize returns the size of the specified object.
func (b *Bucket) ObjectSize(_ context.Context, name string) (uint64, error) {
	objMeta, err := b.client.GetObjectMeta(b.name, name)
	if err != nil {
		return 0, err
	}
	return uint64(objMeta.ContentLength), nil
}

// Attributes returns information about the specified object.
func (b *Bucket) Attributes(_ context.Context, name string) (objstore.ObjectAttributes, error) {
	objMeta, err := b.client.GetObjectMeta(b.name, name)
	if err != nil {
		return objstore.ObjectAttributes{}, errors.Wrapf(err, "gettting objectmeta of %s", name)
	}

	lastModified, err := time.Parse(time.RFC1123, objMeta.LastModified)
	if err != nil {
		return objstore.ObjectAttributes{}, err
	}

	return objstore.ObjectAttributes{
		Size:         objMeta.ContentLength,
		LastModified: lastModified,
	}, nil
}

// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
func (b *Bucket) IsObjNotFoundErr(err error) bool {
	switch bosErr := errors.Cause(err).(type) {
	case *bce.BceServiceError:
		if bosErr.StatusCode == http.StatusNotFound || bosErr.Code == "NoSuchKey" {
			return true
		}
	}
	return false
}

// IsAccessDeniedErr returns true if access to object is denied.
func (b *Bucket) IsAccessDeniedErr(_ error) bool {
	return false
}

func (b *Bucket) getRange(_ context.Context, bucketName, objectKey string, off, length int64) (io.ReadCloser, error) {
	if len(objectKey) == 0 {
		return nil, errors.Errorf("given object name should not empty")
	}

	ranges := []int64{off}
	if length != -1 {
		ranges = append(ranges, off+length-1)
	}

	obj, err := b.client.GetObject(bucketName, objectKey, map[string]string{}, ranges...)
	if err != nil {
		return nil, err
	}

	return objstore.ObjectSizerReadCloser{
		ReadCloser: obj.Body,
		Size: func() (int64, error) {
			return obj.ContentLength, nil
		},
	}, err
}

func configFromEnv() Config {
	c := Config{
		Bucket:    os.Getenv("BOS_BUCKET"),
		Endpoint:  os.Getenv("BOS_ENDPOINT"),
		AccessKey: os.Getenv("BOS_ACCESS_KEY"),
		SecretKey: os.Getenv("BOS_SECRET_KEY"),
	}
	return c
}

// NewTestBucket creates test bkt client that before returning creates temporary bucket.
// In a close function it empties and deletes the bucket.
func NewTestBucket(t testing.TB) (objstore.Bucket, func(), error) {
	c := configFromEnv()
	if err := validateForTest(c); err != nil {
		return nil, nil, err
	}

	if c.Bucket != "" {
		if os.Getenv("THANOS_ALLOW_EXISTING_BUCKET_USE") == "" {
			return nil, nil, errors.New("BOS_BUCKET is defined. Normally this tests will create temporary bucket " +
				"and delete it after test. Unset BOS_BUCKET env variable to use default logic. If you really want to run " +
				"tests against provided (NOT USED!) bucket, set THANOS_ALLOW_EXISTING_BUCKET_USE=true. WARNING: That bucket " +
				"needs to be manually cleared. This means that it is only useful to run one test in a time. This is due " +
				"to safety (accidentally pointing prod bucket for test) as well as BOS not being fully strong consistent.")
		}

		bc, err := yaml.Marshal(c)
		if err != nil {
			return nil, nil, err
		}

		b, err := NewBucket(log.NewNopLogger(), bc, "thanos-e2e-test")
		if err != nil {
			return nil, nil, err
		}

		if err := b.Iter(context.Background(), "", func(f string) error {
			return errors.Errorf("bucket %s is not empty", c.Bucket)
		}); err != nil {
			return nil, nil, errors.Wrapf(err, "checking bucket %s", c.Bucket)
		}

		t.Log("WARNING. Reusing", c.Bucket, "BOS bucket for BOS tests. Manual cleanup afterwards is required")
		return b, func() {}, nil
	}

	src := rand.NewSource(time.Now().UnixNano())
	tmpBucketName := strings.Replace(fmt.Sprintf("test_%x", src.Int63()), "_", "-", -1)

	if len(tmpBucketName) >= 31 {
		tmpBucketName = tmpBucketName[:31]
	}

	c.Bucket = tmpBucketName
	bc, err := yaml.Marshal(c)
	if err != nil {
		return nil, nil, err
	}

	b, err := NewBucket(log.NewNopLogger(), bc, "thanos-e2e-test")
	if err != nil {
		return nil, nil, err
	}

	if _, err := b.client.PutBucket(b.name); err != nil {
		return nil, nil, err
	}

	t.Log("created temporary BOS bucket for BOS tests with name", tmpBucketName)
	return b, func() {
		objstore.EmptyBucket(t, context.Background(), b)
		if err := b.client.DeleteBucket(b.name); err != nil {
			t.Logf("deleting bucket %s failed: %s", tmpBucketName, err)
		}
	}, nil
}

func validateForTest(conf Config) error {
	if conf.Endpoint == "" ||
		conf.AccessKey == "" ||
		conf.SecretKey == "" {
		return errors.New("insufficient BOS configuration information")
	}
	return nil
}
```

## File: `providers/cos/cos.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package cos

import (
	"context"
	"fmt"
	"io"
	"math"
	"math/rand"
	"net/http"
	"net/url"
	"os"
	"strings"
	"testing"
	"time"

	"github.com/efficientgo/core/logerrcapture"
	"github.com/go-kit/log"
	"github.com/pkg/errors"
	"github.com/prometheus/common/model"
	"github.com/tencentyun/cos-go-sdk-v5"
	"gopkg.in/yaml.v2"

	"github.com/thanos-io/objstore"
	"github.com/thanos-io/objstore/clientutil"
	"github.com/thanos-io/objstore/exthttp"
)

// DirDelim is the delimiter used to model a directory structure in an object store bucket.
const dirDelim = "/"

// Bucket implements the store.Bucket interface against cos-compatible(Tencent Object Storage) APIs.
type Bucket struct {
	logger log.Logger
	client *cos.Client
	name   string
}

// DefaultConfig is the default config for an cos client. default tune the `MaxIdleConnsPerHost`.
var DefaultConfig = Config{
	HTTPConfig: exthttp.HTTPConfig{
		IdleConnTimeout:       model.Duration(90 * time.Second),
		ResponseHeaderTimeout: model.Duration(2 * time.Minute),
		TLSHandshakeTimeout:   model.Duration(10 * time.Second),
		ExpectContinueTimeout: model.Duration(1 * time.Second),
		MaxIdleConns:          100,
		MaxIdleConnsPerHost:   100,
		MaxConnsPerHost:       0,
	},
}

// Config encapsulates the necessary config values to instantiate an cos client.
type Config struct {
	Bucket     string             `yaml:"bucket"`
	Region     string             `yaml:"region"`
	AppId      string             `yaml:"app_id"`
	Endpoint   string             `yaml:"endpoint"`
	SecretKey  string             `yaml:"secret_key"`
	SecretId   string             `yaml:"secret_id"`
	MaxRetries int                `yaml:"max_retries"`
	HTTPConfig exthttp.HTTPConfig `yaml:"http_config"`
}

// Validate checks to see if mandatory cos config options are set.
func (conf *Config) validate() error {
	if conf.Endpoint != "" {
		if _, err := url.Parse(conf.Endpoint); err != nil {
			return errors.Wrap(err, "parse endpoint")
		}
		if conf.SecretId == "" ||
			conf.SecretKey == "" {
			return errors.New("secret_id or secret_key is empty")
		}
		return nil
	}
	if conf.Bucket == "" ||
		conf.AppId == "" ||
		conf.Region == "" ||
		conf.SecretId == "" ||
		conf.SecretKey == "" {
		return errors.New("insufficient cos configuration information")
	}
	return nil
}

// parseConfig unmarshal a buffer into a Config with default HTTPConfig values.
func parseConfig(conf []byte) (Config, error) {
	config := DefaultConfig
	if err := yaml.Unmarshal(conf, &config); err != nil {
		return Config{}, err
	}

	return config, nil
}

// NewBucket returns a new Bucket using the provided cos configuration.
func NewBucket(logger log.Logger, conf []byte, component string, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Bucket, error) {
	if logger == nil {
		logger = log.NewNopLogger()
	}

	config, err := parseConfig(conf)
	if err != nil {
		return nil, errors.Wrap(err, "parsing cos configuration")
	}
	return NewBucketWithConfig(logger, config, component, wrapRoundtripper)
}

// NewBucketWithConfig returns a new Bucket using the provided cos config values.
func NewBucketWithConfig(logger log.Logger, config Config, component string, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Bucket, error) {
	if err := config.validate(); err != nil {
		return nil, errors.Wrap(err, "validate cos configuration")
	}

	var bucketURL *url.URL
	var err error
	if config.Endpoint != "" {
		bucketURL, err = url.Parse(config.Endpoint)
		if err != nil {
			return nil, errors.Wrap(err, "parse endpoint")
		}
	} else {
		bucketURL, err = cos.NewBucketURL(fmt.Sprintf("%s-%s", config.Bucket, config.AppId), config.Region, true)
		if err != nil {
			return nil, errors.Wrap(err, "create bucket")
		}
	}
	b := &cos.BaseURL{BucketURL: bucketURL}
	var rt http.RoundTripper
	rt, err = exthttp.DefaultTransport(config.HTTPConfig)
	if err != nil {
		return nil, err
	}
	if config.HTTPConfig.Transport != nil {
		rt = config.HTTPConfig.Transport
	}
	if wrapRoundtripper != nil {
		rt = wrapRoundtripper(rt)
	}
	client := cos.NewClient(b, &http.Client{
		Transport: &cos.AuthorizationTransport{
			SecretID:  config.SecretId,
			SecretKey: config.SecretKey,
			Transport: rt,
		},
	})

	if config.MaxRetries > 0 {
		client.Conf.RetryOpt.Count = config.MaxRetries
	}

	bkt := &Bucket{
		logger: logger,
		client: client,
		name:   config.Bucket,
	}
	return bkt, nil
}

func (b *Bucket) Provider() objstore.ObjProvider { return objstore.COS }

// Name returns the bucket name for COS.
func (b *Bucket) Name() string {
	return b.name
}

// Attributes returns information about the specified object.
func (b *Bucket) Attributes(ctx context.Context, name string) (objstore.ObjectAttributes, error) {
	resp, err := b.client.Object.Head(ctx, name, nil)
	if err != nil {
		return objstore.ObjectAttributes{}, err
	}

	size, err := clientutil.ParseContentLength(resp.Header)
	if err != nil {
		return objstore.ObjectAttributes{}, err
	}

	// tencent cos return Last-Modified header in RFC1123 format.
	// see api doc for details: https://intl.cloud.tencent.com/document/product/436/7729
	mod, err := clientutil.ParseLastModified(resp.Header, time.RFC1123)
	if err != nil {
		return objstore.ObjectAttributes{}, err
	}

	return objstore.ObjectAttributes{
		Size:         size,
		LastModified: mod,
	}, nil
}

var (
	_ cos.FixedLengthReader = (*fixedLengthReader)(nil)
)

type fixedLengthReader struct {
	io.Reader
	size int64
}

func newFixedLengthReader(r io.Reader, size int64) io.Reader {
	return fixedLengthReader{
		Reader: io.LimitReader(r, size),
		size:   size,
	}
}

// Size implement cos.FixedLengthReader interface.
func (r fixedLengthReader) Size() int64 {
	return r.size
}

// Upload the contents of the reader as an object into the bucket.
func (b *Bucket) Upload(ctx context.Context, name string, r io.Reader, opts ...objstore.ObjectUploadOption) error {
	size, err := objstore.TryToGetSize(r)
	if err != nil {
		return errors.Wrapf(err, "getting size of %s", name)
	}
	uploadOpts := objstore.ApplyObjectUploadOptions(opts...)

	// partSize 128MB.
	const partSize = 1024 * 1024 * 128
	partNums, lastSlice := int(math.Floor(float64(size)/partSize)), size%partSize
	if partNums == 0 {
		cosOpts := &cos.ObjectPutOptions{
			ObjectPutHeaderOptions: &cos.ObjectPutHeaderOptions{
				ContentType: uploadOpts.ContentType,
			},
		}
		if _, err := b.client.Object.Put(ctx, name, r, cosOpts); err != nil {
			return errors.Wrapf(err, "Put object: %s", name)
		}
		return nil
	}
	// 1. init.
	cosOpts := &cos.InitiateMultipartUploadOptions{
		ObjectPutHeaderOptions: &cos.ObjectPutHeaderOptions{
			ContentType: uploadOpts.ContentType,
		},
	}
	result, _, err := b.client.Object.InitiateMultipartUpload(ctx, name, cosOpts)
	if err != nil {
		return errors.Wrapf(err, "InitiateMultipartUpload %s", name)
	}
	uploadEveryPart := func(partSize int64, part int, uploadID string) (string, error) {
		r := newFixedLengthReader(r, partSize)
		resp, err := b.client.Object.UploadPart(ctx, name, uploadID, part, r, &cos.ObjectUploadPartOptions{
			ContentLength: partSize,
		})
		if err != nil {
			if _, err := b.client.Object.AbortMultipartUpload(ctx, name, uploadID); err != nil {
				return "", err
			}
			return "", err
		}
		etag := resp.Header.Get("ETag")
		return etag, nil
	}
	optcom := &cos.CompleteMultipartUploadOptions{}
	// 2. upload parts.
	for part := 1; part <= partNums; part++ {
		etag, err := uploadEveryPart(partSize, part, result.UploadID)
		if err != nil {
			return errors.Wrapf(err, "uploadPart %d, %s", part, name)
		}
		optcom.Parts = append(optcom.Parts, cos.Object{
			PartNumber: part, ETag: etag},
		)
	}
	// 3. upload last part.
	if lastSlice != 0 {
		part := partNums + 1
		etag, err := uploadEveryPart(lastSlice, part, result.UploadID)
		if err != nil {
			return errors.Wrapf(err, "uploadPart %d, %s", part, name)
		}
		optcom.Parts = append(optcom.Parts, cos.Object{
			PartNumber: part, ETag: etag},
		)
	}
	// 4. complete.
	if _, _, err := b.client.Object.CompleteMultipartUpload(ctx, name, result.UploadID, optcom); err != nil {
		return errors.Wrapf(err, "CompleteMultipartUpload %s", name)
	}
	return nil
}

// Delete removes the object with the given name.
func (b *Bucket) Delete(ctx context.Context, name string) error {
	if _, err := b.client.Object.Delete(ctx, name); err != nil {
		return errors.Wrap(err, "delete cos object")
	}
	return nil
}

func (b *Bucket) SupportedIterOptions() []objstore.IterOptionType {
	return []objstore.IterOptionType{objstore.Recursive}
}

// Iter calls f for each entry in the given directory. The argument to f is the full
// object name including the prefix of the inspected directory.
func (b *Bucket) Iter(ctx context.Context, dir string, f func(string) error, options ...objstore.IterOption) error {
	if dir != "" {
		dir = strings.TrimSuffix(dir, dirDelim) + dirDelim
	}

	for object := range b.listObjects(ctx, dir, options...) {
		if object.err != nil {
			return object.err
		}
		if object.key == "" {
			continue
		}
		if err := f(object.key); err != nil {
			return err
		}
	}

	return nil
}

func (b *Bucket) IterWithAttributes(ctx context.Context, dir string, f func(attrs objstore.IterObjectAttributes) error, options ...objstore.IterOption) error {
	if err := objstore.ValidateIterOptions(b.SupportedIterOptions(), options...); err != nil {
		return err
	}

	return b.Iter(ctx, dir, func(name string) error {
		return f(objstore.IterObjectAttributes{Name: name})
	}, options...)
}

func (b *Bucket) getRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	if name == "" {
		return nil, errors.New("given object name should not empty")
	}

	opts := &cos.ObjectGetOptions{}
	if length != -1 {
		if err := setRange(opts, off, off+length-1); err != nil {
			return nil, err
		}
	} else if off > 0 {
		if err := setRange(opts, off, 0); err != nil {
			return nil, err
		}
	}

	resp, err := b.client.Object.Get(ctx, name, opts)
	if err != nil {
		return nil, err
	}
	if _, err := resp.Body.Read(nil); err != nil {
		logerrcapture.ExhaustClose(b.logger, resp.Body, "cos get range obj close")
		return nil, err
	}
	// Add size info into reader to pass it to Upload function.
	return objstore.ObjectSizerReadCloser{
		ReadCloser: resp.Body,
		Size: func() (int64, error) {
			return resp.ContentLength, nil
		},
	}, nil
}

// Get returns a reader for the given object name.
func (b *Bucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	return b.getRange(ctx, name, 0, -1)
}

// GetRange returns a new range reader for the given object name and range.
func (b *Bucket) GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	return b.getRange(ctx, name, off, length)
}

// Exists checks if the given object exists in the bucket.
func (b *Bucket) Exists(ctx context.Context, name string) (bool, error) {
	if _, err := b.client.Object.Head(ctx, name, nil); err != nil {
		if b.IsObjNotFoundErr(err) {
			return false, nil
		}
		return false, errors.Wrap(err, "head cos object")
	}

	return true, nil
}

// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
func (b *Bucket) IsObjNotFoundErr(err error) bool {
	switch tmpErr := errors.Cause(err).(type) {
	case *cos.ErrorResponse:
		if tmpErr.Code == "NoSuchKey" ||
			(tmpErr.Response != nil && tmpErr.Response.StatusCode == http.StatusNotFound) {
			return true
		}
		return false
	default:
		return false
	}
}

// IsAccessDeniedErr returns true if access to object is denied.
func (b *Bucket) IsAccessDeniedErr(_ error) bool {
	return false
}

func (b *Bucket) Close() error { return nil }

type objectInfo struct {
	key string
	err error
}

func (b *Bucket) listObjects(ctx context.Context, objectPrefix string, options ...objstore.IterOption) <-chan objectInfo {
	objectsCh := make(chan objectInfo, 1)

	// If recursive iteration is enabled we should pass an empty delimiter.
	delimiter := dirDelim
	if objstore.ApplyIterOptions(options...).Recursive {
		delimiter = ""
	}

	go func(objectsCh chan<- objectInfo) {
		defer close(objectsCh)
		var marker string
		for {
			result, _, err := b.client.Bucket.Get(ctx, &cos.BucketGetOptions{
				Prefix:    objectPrefix,
				MaxKeys:   1000,
				Marker:    marker,
				Delimiter: delimiter,
			})
			if err != nil {
				select {
				case objectsCh <- objectInfo{
					err: err,
				}:
				case <-ctx.Done():
				}
				return
			}

			for _, object := range result.Contents {
				select {
				case objectsCh <- objectInfo{
					key: object.Key,
				}:
				case <-ctx.Done():
					return
				}
			}

			// The result of CommonPrefixes contains the objects
			// that have the same keys between Prefix and the key specified by delimiter.
			for _, obj := range result.CommonPrefixes {
				select {
				case objectsCh <- objectInfo{
					key: obj,
				}:
				case <-ctx.Done():
					return
				}
			}

			if !result.IsTruncated {
				return
			}

			marker = result.NextMarker
		}
	}(objectsCh)
	return objectsCh
}

func setRange(opts *cos.ObjectGetOptions, start, end int64) error {
	if start == 0 && end < 0 {
		opts.Range = fmt.Sprintf("bytes=%d", end)
	} else if 0 < start && end == 0 {
		opts.Range = fmt.Sprintf("bytes=%d-", start)
	} else if 0 <= start && start <= end {
		opts.Range = fmt.Sprintf("bytes=%d-%d", start, end)
	} else {
		return errors.Errorf("Invalid range specified: start=%d end=%d", start, end)
	}
	return nil
}

func configFromEnv() Config {
	c := Config{
		Bucket:    os.Getenv("COS_BUCKET"),
		AppId:     os.Getenv("COS_APP_ID"),
		Region:    os.Getenv("COS_REGION"),
		Endpoint:  os.Getenv("COS_ENDPOINT"),
		SecretId:  os.Getenv("COS_SECRET_ID"),
		SecretKey: os.Getenv("COS_SECRET_KEY"),
	}

	return c
}

// NewTestBucket creates test bkt client that before returning creates temporary bucket.
// In a close function it empties and deletes the bucket.
func NewTestBucket(t testing.TB) (objstore.Bucket, func(), error) {
	c := configFromEnv()
	if err := validateForTest(c); err != nil {
		return nil, nil, err
	}

	if c.Bucket != "" {
		if os.Getenv("THANOS_ALLOW_EXISTING_BUCKET_USE") == "" {
			return nil, nil, errors.New("COS_BUCKET is defined. Normally this tests will create temporary bucket " +
				"and delete it after test. Unset COS_BUCKET env variable to use default logic. If you really want to run " +
				"tests against provided (NOT USED!) bucket, set THANOS_ALLOW_EXISTING_BUCKET_USE=true. WARNING: That bucket " +
				"needs to be manually cleared. This means that it is only useful to run one test in a time. This is due " +
				"to safety (accidentally pointing prod bucket for test) as well as COS not being fully strong consistent.")
		}

		bc, err := yaml.Marshal(c)
		if err != nil {
			return nil, nil, err
		}

		b, err := NewBucket(log.NewNopLogger(), bc, "thanos-e2e-test", nil)
		if err != nil {
			return nil, nil, err
		}

		if err := b.Iter(context.Background(), "", func(_ string) error {
			return errors.Errorf("bucket %s is not empty", c.Bucket)
		}); err != nil {
			return nil, nil, errors.Wrapf(err, "cos check bucket %s", c.Bucket)
		}

		t.Log("WARNING. Reusing", c.Bucket, "COS bucket for COS tests. Manual cleanup afterwards is required")
		return b, func() {}, nil
	}
	c.Bucket = createTemporaryTestBucketName(t)

	bc, err := yaml.Marshal(c)
	if err != nil {
		return nil, nil, err
	}

	b, err := NewBucket(log.NewNopLogger(), bc, "thanos-e2e-test", nil)
	if err != nil {
		return nil, nil, err
	}

	if _, err := b.client.Bucket.Put(context.Background(), nil); err != nil {
		return nil, nil, err
	}
	t.Log("created temporary COS bucket for COS tests with name", c.Bucket)

	return b, func() {
		objstore.EmptyBucket(t, context.Background(), b)
		if _, err := b.client.Bucket.Delete(context.Background()); err != nil {
			t.Logf("deleting bucket %s failed: %s", c.Bucket, err)
		}
	}, nil
}

func validateForTest(conf Config) error {
	if conf.Endpoint != "" {
		if _, err := url.Parse(conf.Endpoint); err != nil {
			return errors.Wrap(err, "parse endpoint")
		}
		if conf.SecretId == "" ||
			conf.SecretKey == "" {
			return errors.New("secret_id or secret_key is empty")
		}
		return nil
	}
	if conf.AppId == "" ||
		conf.Region == "" ||
		conf.SecretId == "" ||
		conf.SecretKey == "" {
		return errors.New("insufficient cos configuration information")
	}
	return nil
}

// createTemporaryTestBucketName create a temp cos bucket for test.
// Bucket Naming Conventions: https://intl.cloud.tencent.com/document/product/436/13312#overview
func createTemporaryTestBucketName(t testing.TB) string {
	src := rand.New(rand.NewSource(time.Now().UnixNano()))
	name := fmt.Sprintf("test_%x_%s", src.Int31(), strings.ToLower(t.Name()))
	name = strings.NewReplacer("_", "-", "/", "-").Replace(name)
	const maxLength = 50
	if len(name) >= maxLength {
		name = name[:maxLength]
	}
	return strings.TrimSuffix(name, "-")
}
```

## File: `providers/cos/cos_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package cos

import (
	"context"
	"testing"
	"time"

	"github.com/efficientgo/core/testutil"
	"github.com/go-kit/log"
	"github.com/prometheus/common/model"

	"github.com/thanos-io/objstore/errutil"
	"github.com/thanos-io/objstore/exthttp"
)

func Test_parseConfig(t *testing.T) {
	type args struct {
		conf []byte
	}
	tests := []struct {
		name    string
		args    args
		want    Config
		wantErr bool
	}{
		{
			name: "empty",
			args: args{
				conf: []byte(""),
			},
			want:    DefaultConfig,
			wantErr: false,
		},
		{
			name: "max_idle_conns",
			args: args{
				conf: []byte(`
http_config:
  max_idle_conns: 200
`),
			},
			want: Config{
				HTTPConfig: exthttp.HTTPConfig{
					IdleConnTimeout:       model.Duration(90 * time.Second),
					ResponseHeaderTimeout: model.Duration(2 * time.Minute),
					TLSHandshakeTimeout:   model.Duration(10 * time.Second),
					ExpectContinueTimeout: model.Duration(1 * time.Second),
					MaxIdleConns:          200,
					MaxIdleConnsPerHost:   100,
					MaxConnsPerHost:       0,
				},
			},
			wantErr: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := parseConfig(tt.args.conf)
			if (err != nil) != tt.wantErr {
				t.Errorf("parseConfig() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			testutil.Equals(t, tt.want, got)
		})
	}
}

func TestConfig_validate(t *testing.T) {
	type fields struct {
		Bucket     string
		Region     string
		AppId      string
		Endpoint   string
		SecretKey  string
		SecretId   string
		HTTPConfig exthttp.HTTPConfig
	}
	tests := []struct {
		name    string
		fields  fields
		wantErr bool
	}{
		{
			name: "ok endpoint",
			fields: fields{
				Endpoint:  "http://bucket-123.cos.ap-beijing.myqcloud.com",
				SecretId:  "sid",
				SecretKey: "skey",
			},
			wantErr: false,
		},
		{
			name: "ok bucket-appid-region",
			fields: fields{
				Bucket:    "bucket",
				AppId:     "123",
				Region:    "ap-beijing",
				SecretId:  "sid",
				SecretKey: "skey",
			},
			wantErr: false,
		},
		{
			name: "missing skey",
			fields: fields{
				Bucket: "bucket",
				AppId:  "123",
				Region: "ap-beijing",
			},
			wantErr: true,
		},
		{
			name: "missing bucket",
			fields: fields{
				AppId:     "123",
				Region:    "ap-beijing",
				SecretId:  "sid",
				SecretKey: "skey",
			},
			wantErr: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			conf := &Config{
				Bucket:     tt.fields.Bucket,
				Region:     tt.fields.Region,
				AppId:      tt.fields.AppId,
				Endpoint:   tt.fields.Endpoint,
				SecretKey:  tt.fields.SecretKey,
				SecretId:   tt.fields.SecretId,
				HTTPConfig: tt.fields.HTTPConfig,
			}
			if err := conf.validate(); (err != nil) != tt.wantErr {
				t.Errorf("validate() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

func TestNewBucketWithErrorRoundTripper(t *testing.T) {
	config := Config{
		Bucket:    "bucket",
		AppId:     "123",
		Region:    "test",
		SecretId:  "sid",
		SecretKey: "skey",
	}

	bkt, err := NewBucketWithConfig(log.NewNopLogger(), config, "test", errutil.WrapWithErrRoundtripper)
	testutil.Ok(t, err)
	_, err = bkt.Get(context.Background(), "Test")
	// We expect an error from the RoundTripper
	testutil.NotOk(t, err)
	testutil.Assert(t, errutil.IsMockedError(err), "Expected RoundTripper error, got: %v", err)
}
```

## File: `providers/filesystem/filesystem.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package filesystem

import (
	"context"
	"fmt"
	"io"
	"os"
	"path/filepath"

	"github.com/efficientgo/core/errcapture"
	"github.com/pkg/errors"
	"gopkg.in/yaml.v2"

	"github.com/thanos-io/objstore"
)

// Config stores the configuration for storing and accessing blobs in filesystem.
type Config struct {
	Directory string `yaml:"directory"`
}

// Bucket implements the objstore.Bucket interfaces against filesystem that binary runs on.
// Methods from Bucket interface are thread-safe. Objects are assumed to be immutable.
// NOTE: It does not follow symbolic links.
type Bucket struct {
	rootDir string
}

// NewBucketFromConfig returns a new filesystem.Bucket from config.
func NewBucketFromConfig(conf []byte) (*Bucket, error) {
	var c Config
	if err := yaml.Unmarshal(conf, &c); err != nil {
		return nil, err
	}
	if c.Directory == "" {
		return nil, errors.New("missing directory for filesystem bucket")
	}
	return NewBucket(c.Directory)
}

// NewBucket returns a new filesystem.Bucket.
func NewBucket(rootDir string) (*Bucket, error) {
	absDir, err := filepath.Abs(rootDir)
	if err != nil {
		return nil, err
	}
	return &Bucket{rootDir: absDir}, nil
}

func (b *Bucket) Provider() objstore.ObjProvider { return objstore.FILESYSTEM }

func (b *Bucket) SupportedIterOptions() []objstore.IterOptionType {
	return []objstore.IterOptionType{objstore.Recursive, objstore.UpdatedAt}
}

func (b *Bucket) IterWithAttributes(ctx context.Context, dir string, f func(attrs objstore.IterObjectAttributes) error, options ...objstore.IterOption) error {
	if ctx.Err() != nil {
		return ctx.Err()
	}

	if err := objstore.ValidateIterOptions(b.SupportedIterOptions(), options...); err != nil {
		return err
	}

	params := objstore.ApplyIterOptions(options...)
	absDir := filepath.Join(b.rootDir, dir)
	info, err := os.Stat(absDir)
	if err != nil {
		if os.IsNotExist(err) {
			return nil
		}
		return errors.Wrapf(err, "stat %s", absDir)
	}
	if !info.IsDir() {
		return nil
	}

	files, err := os.ReadDir(absDir)
	if err != nil {
		return err
	}
	for _, file := range files {
		name := filepath.Join(dir, file.Name())

		if file.IsDir() {
			empty, err := isDirEmpty(filepath.Join(absDir, file.Name()))
			if err != nil {
				return err
			}

			if empty {
				// Skip empty directories.
				continue
			}

			name += objstore.DirDelim

			if params.Recursive {
				// Recursively list files in the subdirectory.
				if err := b.IterWithAttributes(ctx, name, f, options...); err != nil {
					return err
				}

				// The callback f() has already been called for the subdirectory
				// files so we should skip to next filesystem entry.
				continue
			}
		}

		attrs := objstore.IterObjectAttributes{
			Name: name,
		}
		if params.LastModified {
			absPath := filepath.Join(absDir, file.Name())
			stat, err := os.Stat(absPath)
			if err != nil {
				return errors.Wrapf(err, "stat %s", name)
			}
			attrs.SetLastModified(stat.ModTime())
		}
		if err := f(attrs); err != nil {
			return err
		}
	}
	return nil
}

// Iter calls f for each entry in the given directory. The argument to f is the full
// object name including the prefix of the inspected directory.
func (b *Bucket) Iter(ctx context.Context, dir string, f func(string) error, opts ...objstore.IterOption) error {
	// Only include recursive option since attributes are not used in this method.
	var filteredOpts []objstore.IterOption
	for _, opt := range opts {
		if opt.Type == objstore.Recursive {
			filteredOpts = append(filteredOpts, opt)
			break
		}
	}

	return b.IterWithAttributes(ctx, dir, func(attrs objstore.IterObjectAttributes) error {
		return f(attrs.Name)
	}, filteredOpts...)
}

// Get returns a reader for the given object name.
func (b *Bucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	return b.GetRange(ctx, name, 0, -1)
}

type rangeReaderCloser struct {
	io.Reader
	f *os.File
}

func (r *rangeReaderCloser) Close() error {
	return r.f.Close()
}

// Attributes returns information about the specified object.
func (b *Bucket) Attributes(ctx context.Context, name string) (objstore.ObjectAttributes, error) {
	if ctx.Err() != nil {
		return objstore.ObjectAttributes{}, ctx.Err()
	}

	file := filepath.Join(b.rootDir, name)
	stat, err := os.Stat(file)
	if err != nil {
		return objstore.ObjectAttributes{}, errors.Wrapf(err, "stat %s", file)
	}

	return objstore.ObjectAttributes{
		Size:         stat.Size(),
		LastModified: stat.ModTime(),
	}, nil
}

// GetRange returns a new range reader for the given object name and range.
func (b *Bucket) GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	if ctx.Err() != nil {
		return nil, ctx.Err()
	}

	if name == "" {
		return nil, errors.New("object name is empty")
	}

	var (
		file = filepath.Join(b.rootDir, name)
		stat os.FileInfo
		err  error
	)
	if stat, err = os.Stat(file); err != nil {
		return nil, errors.Wrapf(err, "stat %s", file)
	}

	f, err := os.OpenFile(filepath.Clean(file), os.O_RDONLY, 0600)
	if err != nil {
		return nil, err
	}

	var newOffset int64
	if off > 0 {
		newOffset, err = f.Seek(off, 0)
		if err != nil {
			return nil, errors.Wrapf(err, "seek %v", off)
		}
	}

	size := stat.Size() - newOffset
	if length == -1 {
		return objstore.ObjectSizerReadCloser{
			ReadCloser: f,
			Size: func() (int64, error) {
				return size, nil
			},
		}, nil
	}

	return objstore.ObjectSizerReadCloser{
		ReadCloser: &rangeReaderCloser{
			Reader: io.LimitReader(f, length),
			f:      f,
		},
		Size: func() (int64, error) {
			return min(length, size), nil
		},
	}, nil
}

// Exists checks if the given directory exists in memory.
func (b *Bucket) Exists(ctx context.Context, name string) (bool, error) {
	if ctx.Err() != nil {
		return false, ctx.Err()
	}

	info, err := os.Stat(filepath.Join(b.rootDir, name))
	if err != nil {
		if os.IsNotExist(err) {
			return false, nil
		}
		return false, errors.Wrapf(err, "stat %s", filepath.Join(b.rootDir, name))
	}
	return !info.IsDir(), nil
}

// Upload writes the file specified in src to into the memory.
func (b *Bucket) Upload(ctx context.Context, name string, r io.Reader, _ ...objstore.ObjectUploadOption) (err error) {
	if ctx.Err() != nil {
		return ctx.Err()
	}

	file := filepath.Join(b.rootDir, name)
	if err := os.MkdirAll(filepath.Dir(file), os.ModePerm); err != nil {
		return err
	}

	f, err := os.Create(file)
	if err != nil {
		return err
	}
	defer errcapture.Do(&err, f.Close, "close")

	if _, err := io.Copy(f, r); err != nil {
		return errors.Wrapf(err, "copy to %s", file)
	}
	return nil
}

func isDirEmpty(name string) (ok bool, err error) {
	f, err := os.Open(filepath.Clean(name))
	if os.IsNotExist(err) {
		// The directory doesn't exist. We don't consider it an error and we treat it like empty.
		return true, nil
	}
	if err != nil {
		return false, err
	}
	defer errcapture.Do(&err, f.Close, "close dir")

	if _, err = f.Readdir(1); err == io.EOF || os.IsNotExist(err) {
		return true, nil
	}
	return false, err
}

// Delete removes all data prefixed with the dir.
func (b *Bucket) Delete(ctx context.Context, name string) error {
	if ctx.Err() != nil {
		return ctx.Err()
	}

	file := filepath.Join(b.rootDir, name)
	for file != b.rootDir {
		if err := os.RemoveAll(file); err != nil {
			return errors.Wrapf(err, "rm %s", file)
		}
		file = filepath.Dir(file)
		empty, err := isDirEmpty(file)
		if err != nil {
			return err
		}
		if !empty {
			break
		}
	}
	return nil
}

// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
func (b *Bucket) IsObjNotFoundErr(err error) bool {
	return os.IsNotExist(errors.Cause(err))
}

// IsAccessDeniedErr returns true if access to object is denied.
func (b *Bucket) IsAccessDeniedErr(_ error) bool {
	return false
}

func (b *Bucket) Close() error { return nil }

// Name returns the bucket name.
func (b *Bucket) Name() string {
	return fmt.Sprintf("fs: %s", b.rootDir)
}
```

## File: `providers/filesystem/filesystem_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package filesystem

import (
	"bytes"
	"context"
	"os"
	"strings"
	"sync"
	"testing"
	"time"

	"github.com/efficientgo/core/testutil"

	"github.com/thanos-io/objstore"
)

func TestDelete_EmptyDirDeletionRaceCondition(t *testing.T) {
	const runs = 1000

	ctx := context.Background()

	for r := 0; r < runs; r++ {
		b, err := NewBucket(t.TempDir())
		testutil.Ok(t, err)

		// Upload 2 objects in a subfolder.
		testutil.Ok(t, b.Upload(ctx, "subfolder/first", strings.NewReader("first")))
		testutil.Ok(t, b.Upload(ctx, "subfolder/second", strings.NewReader("second")))

		// Prepare goroutines to concurrently delete the 2 objects (each one deletes a different object)
		start := make(chan struct{})
		group := sync.WaitGroup{}
		group.Add(2)

		for _, object := range []string{"first", "second"} {
			go func(object string) {
				defer group.Done()

				<-start
				testutil.Ok(t, b.Delete(ctx, "subfolder/"+object))
			}(object)
		}

		// Go!
		close(start)
		group.Wait()
	}
}

func TestIter_CancelledContext(t *testing.T) {
	b, err := NewBucket(t.TempDir())
	testutil.Ok(t, err)

	ctx, cancel := context.WithCancel(context.Background())
	cancel()

	err = b.Iter(ctx, "", func(s string) error {
		return nil
	})

	testutil.NotOk(t, err)
	testutil.Equals(t, context.Canceled, err)
}

func TestIterWithAttributes(t *testing.T) {
	dir := t.TempDir()
	f, err := os.CreateTemp(dir, "test")
	testutil.Ok(t, err)
	defer f.Close()

	stat, err := f.Stat()
	testutil.Ok(t, err)

	cases := []struct {
		name              string
		opts              []objstore.IterOption
		expectedUpdatedAt time.Time
	}{
		{
			name: "no options",
			opts: nil,
		},
		{
			name: "with updated at",
			opts: []objstore.IterOption{
				objstore.WithUpdatedAt(),
			},
			expectedUpdatedAt: stat.ModTime(),
		},
	}

	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			b, err := NewBucket(dir)
			testutil.Ok(t, err)

			var attrs objstore.IterObjectAttributes

			ctx := context.Background()
			err = b.IterWithAttributes(ctx, "", func(objectAttrs objstore.IterObjectAttributes) error {
				attrs = objectAttrs
				return nil
			}, tc.opts...)

			testutil.Ok(t, err)

			lastModified, ok := attrs.LastModified()
			if zero := tc.expectedUpdatedAt.IsZero(); zero {
				testutil.Equals(t, false, ok)
			} else {
				testutil.Equals(t, true, ok)
				testutil.Equals(t, tc.expectedUpdatedAt, lastModified)
			}
		})

	}
}

func TestGet_CancelledContext(t *testing.T) {
	b, err := NewBucket(t.TempDir())
	testutil.Ok(t, err)

	ctx, cancel := context.WithCancel(context.Background())
	cancel()

	_, err = b.Get(ctx, "some-file")
	testutil.NotOk(t, err)
	testutil.Equals(t, context.Canceled, err)
}

func TestAttributes_CancelledContext(t *testing.T) {
	b, err := NewBucket(t.TempDir())
	testutil.Ok(t, err)

	ctx, cancel := context.WithCancel(context.Background())
	cancel()

	_, err = b.Attributes(ctx, "some-file")
	testutil.NotOk(t, err)
	testutil.Equals(t, context.Canceled, err)
}

func TestGetRange_CancelledContext(t *testing.T) {
	b, err := NewBucket(t.TempDir())
	testutil.Ok(t, err)

	ctx, cancel := context.WithCancel(context.Background())
	cancel()

	_, err = b.GetRange(ctx, "some-file", 0, 100)
	testutil.NotOk(t, err)
	testutil.Equals(t, context.Canceled, err)
}

func TestExists_CancelledContext(t *testing.T) {
	b, err := NewBucket(t.TempDir())
	testutil.Ok(t, err)

	ctx, cancel := context.WithCancel(context.Background())
	cancel()

	_, err = b.Exists(ctx, "some-file")
	testutil.NotOk(t, err)
	testutil.Equals(t, context.Canceled, err)
}

func TestUpload_CancelledContext(t *testing.T) {
	b, err := NewBucket(t.TempDir())
	testutil.Ok(t, err)

	ctx, cancel := context.WithCancel(context.Background())
	cancel()

	err = b.Upload(ctx, "some-file", bytes.NewReader([]byte("file content")))
	testutil.NotOk(t, err)
	testutil.Equals(t, context.Canceled, err)
}

func TestDelete_CancelledContext(t *testing.T) {
	b, err := NewBucket(t.TempDir())
	testutil.Ok(t, err)

	ctx, cancel := context.WithCancel(context.Background())
	cancel()

	err = b.Delete(ctx, "some-file")
	testutil.NotOk(t, err)
	testutil.Equals(t, context.Canceled, err)
}
```

## File: `providers/gcs/gcs.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

// Package gcs implements common object storage abstractions against Google Cloud Storage.
package gcs

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"runtime"
	"strings"
	"testing"
	"time"

	"cloud.google.com/go/storage"
	"github.com/go-kit/log"
	"github.com/pkg/errors"
	"github.com/prometheus/common/version"
	"golang.org/x/oauth2/google"
	"google.golang.org/api/iterator"
	"google.golang.org/api/option"
	htransport "google.golang.org/api/transport/http"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	"gopkg.in/yaml.v2"

	"github.com/thanos-io/objstore"
	"github.com/thanos-io/objstore/exthttp"
)

// DirDelim is the delimiter used to model a directory structure in an object store bucket.
const DirDelim = "/"

var DefaultConfig = Config{
	HTTPConfig: exthttp.DefaultHTTPConfig,
}

// Config stores the configuration for gcs bucket.
type Config struct {
	Bucket         string `yaml:"bucket"`
	ServiceAccount string `yaml:"service_account"`
	UseGRPC        bool   `yaml:"use_grpc"`
	// GRPCConnPoolSize controls the size of the gRPC connection pool and should only be used
	// when direct path is not enabled.
	// See https://pkg.go.dev/cloud.google.com/go/storage#hdr-Experimental_gRPC_API for more details
	// on how to enable direct path.
	GRPCConnPoolSize int                `yaml:"grpc_conn_pool_size"`
	HTTPConfig       exthttp.HTTPConfig `yaml:"http_config"`

	// ChunkSizeBytes controls the maximum number of bytes of the object that the
	// Writer will attempt to send to the server in a single request
	// Used as storage.Writer.ChunkSize of https://pkg.go.dev/google.golang.org/cloud/storage#Writer
	ChunkSizeBytes int  `yaml:"chunk_size_bytes"`
	noAuth         bool `yaml:"no_auth"`

	// MaxRetries controls the number of retries for idempotent operations.
	// Overrides the default gcs storage client behavior if this value is greater than 0.
	// Set this to 1 to disable retries.
	MaxRetries int `yaml:"max_retries"`
}

// Bucket implements the store.Bucket and shipper.Bucket interfaces against GCS.
type Bucket struct {
	logger    log.Logger
	bkt       *storage.BucketHandle
	name      string
	chunkSize int

	closer io.Closer
}

// parseConfig unmarshals a buffer into a Config with default values.
func parseConfig(conf []byte) (Config, error) {
	config := DefaultConfig
	if err := yaml.UnmarshalStrict(conf, &config); err != nil {
		return Config{}, err
	}

	return config, nil
}

// NewBucket returns a new Bucket against the given bucket handle.
func NewBucket(ctx context.Context, logger log.Logger, conf []byte, component string, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Bucket, error) {
	config, err := parseConfig(conf)
	if err != nil {
		return nil, err
	}
	return NewBucketWithConfig(ctx, logger, config, component, wrapRoundtripper)
}

// NewBucketWithConfig returns a new Bucket with gcs Config struct.
func NewBucketWithConfig(ctx context.Context, logger log.Logger, gc Config, component string, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Bucket, error) {
	if gc.Bucket == "" {
		return nil, errors.New("missing Google Cloud Storage bucket name for stored blocks")
	}

	var opts []option.ClientOption

	// If ServiceAccount is provided, use them in GCS client, otherwise fallback to Google default logic.
	if gc.ServiceAccount != "" {
		credentials, err := google.CredentialsFromJSON(ctx, []byte(gc.ServiceAccount), storage.ScopeFullControl)
		if err != nil {
			return nil, errors.Wrap(err, "failed to create credentials from JSON")
		}
		opts = append(opts, option.WithCredentials(credentials))
	}
	if gc.noAuth {
		opts = append(opts, option.WithoutAuthentication())
	}
	opts = append(opts,
		option.WithUserAgent(fmt.Sprintf("thanos-%s/%s (%s)", component, version.Version, runtime.Version())),
	)

	if !gc.UseGRPC {
		var err error
		opts, err = appendHttpOptions(gc, opts, wrapRoundtripper)
		if err != nil {
			return nil, err
		}
	}

	return newBucket(ctx, logger, gc, opts)
}

func appendHttpOptions(gc Config, opts []option.ClientOption, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) ([]option.ClientOption, error) {
	// Check if a roundtripper has been set in the config
	// otherwise build the default transport.
	var rt http.RoundTripper
	rt, err := exthttp.DefaultTransport(gc.HTTPConfig)
	if err != nil {
		return nil, err
	}
	if gc.HTTPConfig.Transport != nil {
		rt = gc.HTTPConfig.Transport
	}
	if wrapRoundtripper != nil {
		rt = wrapRoundtripper(rt)
	}

	// GCS uses some defaults when "options.WithHTTPClient" is not used that are important when we call
	// htransport.NewTransport namely the scopes that are then used for OAth authentication. So to build our own
	// http client we need to se those defaults
	opts = append(opts, option.WithScopes(storage.ScopeFullControl, "https://www.googleapis.com/auth/cloud-platform"))
	gRT, err := htransport.NewTransport(context.Background(), rt, opts...)
	if err != nil {
		return nil, err
	}

	httpCli := &http.Client{
		Transport: gRT,
		Timeout:   time.Duration(gc.HTTPConfig.IdleConnTimeout),
	}
	return append(opts, option.WithHTTPClient(httpCli)), nil
}

func newBucket(ctx context.Context, logger log.Logger, gc Config, opts []option.ClientOption) (*Bucket, error) {
	var (
		err       error
		gcsClient *storage.Client
	)
	if gc.UseGRPC {
		opts = append(opts,
			option.WithGRPCConnectionPool(gc.GRPCConnPoolSize),
		)
		gcsClient, err = storage.NewGRPCClient(ctx, opts...)
	} else {
		gcsClient, err = storage.NewClient(ctx, opts...)
	}
	if err != nil {
		return nil, err
	}
	bkt := &Bucket{
		logger:    logger,
		bkt:       gcsClient.Bucket(gc.Bucket),
		closer:    gcsClient,
		name:      gc.Bucket,
		chunkSize: gc.ChunkSizeBytes,
	}

	if gc.MaxRetries > 0 {
		bkt.bkt = bkt.bkt.Retryer(storage.WithMaxAttempts(gc.MaxRetries))
	}

	return bkt, nil
}

func (b *Bucket) Provider() objstore.ObjProvider { return objstore.GCS }

// Name returns the bucket name for gcs.
func (b *Bucket) Name() string {
	return b.name
}

func (b *Bucket) SupportedIterOptions() []objstore.IterOptionType {
	return []objstore.IterOptionType{objstore.Recursive, objstore.UpdatedAt}
}

func (b *Bucket) IterWithAttributes(ctx context.Context, dir string, f func(attrs objstore.IterObjectAttributes) error, options ...objstore.IterOption) error {
	if err := objstore.ValidateIterOptions(b.SupportedIterOptions(), options...); err != nil {
		return err
	}

	// Ensure the object name actually ends with a dir suffix. Otherwise we'll just iterate the
	// object itself as one prefix item.
	if dir != "" {
		dir = strings.TrimSuffix(dir, DirDelim) + DirDelim
	}

	appliedOpts := objstore.ApplyIterOptions(options...)

	// If recursive iteration is enabled we should pass an empty delimiter.
	delimiter := DirDelim
	if appliedOpts.Recursive {
		delimiter = ""
	}

	query := &storage.Query{
		Prefix:    dir,
		Delimiter: delimiter,
	}
	if appliedOpts.LastModified {
		if err := query.SetAttrSelection([]string{"Name", "Updated"}); err != nil {
			return err
		}
	} else {
		if err := query.SetAttrSelection([]string{"Name"}); err != nil {
			return err
		}
	}
	it := b.bkt.Objects(ctx, query)
	for {
		select {
		case <-ctx.Done():
			return ctx.Err()
		default:
		}
		attrs, err := it.Next()
		if err == iterator.Done {
			return nil
		}
		if err != nil {
			return err
		}

		objAttrs := objstore.IterObjectAttributes{Name: attrs.Prefix + attrs.Name}
		if appliedOpts.LastModified {
			objAttrs.SetLastModified(attrs.Updated)
		}
		if err := f(objAttrs); err != nil {
			return err
		}
	}
}

// Iter calls f for each entry in the given directory. The argument to f is the full
// object name including the prefix of the inspected directory.
func (b *Bucket) Iter(ctx context.Context, dir string, f func(string) error, opts ...objstore.IterOption) error {
	// Only include recursive option since attributes are not used in this method.
	var filteredOpts []objstore.IterOption
	for _, opt := range opts {
		if opt.Type == objstore.Recursive {
			filteredOpts = append(filteredOpts, opt)
			break
		}
	}

	return b.IterWithAttributes(ctx, dir, func(attrs objstore.IterObjectAttributes) error {
		return f(attrs.Name)
	}, filteredOpts...)
}

// Get returns a reader for the given object name.
func (b *Bucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	r, err := b.bkt.Object(name).NewReader(ctx)
	if err != nil {
		return r, err
	}

	return objstore.ObjectSizerReadCloser{
		ReadCloser: r,
		Size: func() (int64, error) {
			return r.Attrs.Size, nil
		},
	}, nil
}

// GetRange returns a new range reader for the given object name and range.
func (b *Bucket) GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	r, err := b.bkt.Object(name).NewRangeReader(ctx, off, length)
	if err != nil {
		return r, err
	}

	sz := r.Remain()
	return objstore.ObjectSizerReadCloser{
		ReadCloser: r,
		Size: func() (int64, error) {
			return sz, nil
		},
	}, nil
}

// Attributes returns information about the specified object.
func (b *Bucket) Attributes(ctx context.Context, name string) (objstore.ObjectAttributes, error) {
	attrs, err := b.bkt.Object(name).Attrs(ctx)
	if err != nil {
		return objstore.ObjectAttributes{}, err
	}

	return objstore.ObjectAttributes{
		Size:         attrs.Size,
		LastModified: attrs.Updated,
	}, nil
}

// Handle returns the underlying GCS bucket handle.
// Used for testing purposes (we return handle, so it is not instrumented).
func (b *Bucket) Handle() *storage.BucketHandle {
	return b.bkt
}

// Exists checks if the given object exists.
func (b *Bucket) Exists(ctx context.Context, name string) (bool, error) {
	if _, err := b.bkt.Object(name).Attrs(ctx); err == nil {
		return true, nil
	} else if !b.IsObjNotFoundErr(err) {
		return false, err
	}
	return false, nil
}

// Upload writes the file specified in src to remote GCS location specified as target.
func (b *Bucket) Upload(ctx context.Context, name string, r io.Reader, opts ...objstore.ObjectUploadOption) error {
	w := b.bkt.Object(name).NewWriter(ctx)

	uploadOpts := objstore.ApplyObjectUploadOptions(opts...)
	// if `chunkSize` is 0, we don't set any custom value for writer's ChunkSize.
	// It uses whatever the default value https://pkg.go.dev/google.golang.org/cloud/storage#Writer
	if b.chunkSize > 0 {
		w.ChunkSize = b.chunkSize
		w.ContentType = uploadOpts.ContentType
	}

	if _, err := io.Copy(w, r); err != nil {
		return err
	}
	return w.Close()
}

// Delete removes the object with the given name.
func (b *Bucket) Delete(ctx context.Context, name string) error {
	return b.bkt.Object(name).Delete(ctx)
}

// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
func (b *Bucket) IsObjNotFoundErr(err error) bool {
	return errors.Is(err, storage.ErrObjectNotExist)
}

// IsAccessDeniedErr returns true if access to object is denied.
func (b *Bucket) IsAccessDeniedErr(err error) bool {
	if s, ok := status.FromError(err); ok && s.Code() == codes.PermissionDenied {
		return true
	}
	return false
}

func (b *Bucket) Close() error {
	return b.closer.Close()
}

// NewTestBucket creates test bkt client that before returning creates temporary bucket.
// In a close function it empties and deletes the bucket.
func NewTestBucket(t testing.TB, project string) (objstore.Bucket, func(), error) {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	gTestConfig := Config{
		Bucket: objstore.CreateTemporaryTestBucketName(t),
	}

	bc, err := yaml.Marshal(gTestConfig)
	if err != nil {
		return nil, nil, err
	}

	b, err := NewBucket(ctx, log.NewNopLogger(), bc, "thanos-e2e-test", nil)
	if err != nil {
		return nil, nil, err
	}

	if err = b.bkt.Create(ctx, project, nil); err != nil {
		_ = b.Close()
		return nil, nil, err
	}

	t.Log("created temporary GCS bucket for GCS tests with name", b.name, "in project", project)
	return b, func() {
		objstore.EmptyBucket(t, ctx, b)
		if err := b.bkt.Delete(ctx); err != nil {
			t.Logf("deleting bucket failed: %s", err)
		}
		if err := b.Close(); err != nil {
			t.Logf("closing bucket failed: %s", err)
		}
	}, nil
}
```

## File: `providers/gcs/gcs_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package gcs

import (
	"context"
	"io"
	"net/http"
	"net/http/httptest"
	"os"
	"testing"
	"time"

	"github.com/efficientgo/core/testutil"
	"github.com/fullstorydev/emulators/storage/gcsemu"
	"github.com/go-kit/log"
	"github.com/prometheus/common/model"
	"github.com/thanos-io/objstore/errutil"
	"google.golang.org/api/option"
)

func TestBucket_Get_ShouldReturnErrorIfServerTruncateResponse(t *testing.T) {
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Last-Modified", "Wed, 21 Oct 2015 07:28:00 GMT")
		w.Header().Set("Content-Length", "100")

		// Write less bytes than the content length.
		_, err := w.Write([]byte("12345"))
		testutil.Ok(t, err)
	}))
	defer srv.Close()

	os.Setenv("STORAGE_EMULATOR_HOST", srv.Listener.Addr().String())

	cfg := Config{
		Bucket:         "test-bucket",
		ServiceAccount: "",
	}

	// NewBucketWithConfig wraps newBucket and processes HTTP options. Can skip for test.
	bkt, err := newBucket(context.Background(), log.NewNopLogger(), cfg, []option.ClientOption{})
	testutil.Ok(t, err)

	reader, err := bkt.Get(context.Background(), "test")
	testutil.Ok(t, err)

	// We expect an error when reading back.
	_, err = io.ReadAll(reader)
	testutil.NotOk(t, err)
	testutil.Equals(t, "storage: partial request not satisfied", err.Error())
}

func TestNewBucketWithConfig_ShouldCreateGRPC(t *testing.T) {
	cfg := Config{
		Bucket:         "test-bucket",
		ServiceAccount: "",
		UseGRPC:        true,
	}

	svr, err := gcsemu.NewServer("127.0.0.1:0", gcsemu.Options{})
	testutil.Ok(t, err)
	err = os.Setenv("STORAGE_EMULATOR_HOST", svr.Addr)
	testutil.Ok(t, err)
	err = os.Setenv("GCS_EMULATOR_HOST", svr.Addr)
	testutil.Ok(t, err)
	err = os.Setenv("STORAGE_EMULATOR_HOST_GRPC", svr.Addr)
	testutil.Ok(t, err)

	bkt, err := NewBucketWithConfig(context.Background(), log.NewNopLogger(), cfg, "test-bucket", nil)
	testutil.Ok(t, err)

	// Check if the bucket is created.
	testutil.Assert(t, bkt != nil, "expected bucket to be created")
}

func TestParseConfig_ChunkSize(t *testing.T) {
	for _, tc := range []struct {
		name       string
		input      string
		assertions func(cfg Config)
	}{
		{
			name:  "DefaultConfig",
			input: `bucket: abcd`,
			assertions: func(cfg Config) {
				testutil.Equals(t, cfg.ChunkSizeBytes, 0)
			},
		},
		{
			name: "CustomConfig",
			input: `bucket: abcd
chunk_size_bytes: 1024`,
			assertions: func(cfg Config) {
				testutil.Equals(t, cfg.ChunkSizeBytes, 1024)
			},
		},
	} {
		t.Run(tc.name, func(t *testing.T) {
			cfg, err := parseConfig([]byte(tc.input))
			testutil.Ok(t, err)
			tc.assertions(cfg)
		})
	}
}

func TestParseConfig_HTTPConfig(t *testing.T) {
	for _, tc := range []struct {
		name       string
		input      string
		assertions func(cfg Config)
	}{
		{
			name:  "DefaultHTTPConfig",
			input: `bucket: abcd`,
			assertions: func(cfg Config) {
				testutil.Equals(t, cfg.HTTPConfig.IdleConnTimeout, model.Duration(90*time.Second))
				testutil.Equals(t, cfg.HTTPConfig.ResponseHeaderTimeout, model.Duration(2*time.Minute))
				testutil.Equals(t, cfg.HTTPConfig.InsecureSkipVerify, false)
			},
		},
		{
			name: "CustomHTTPConfig",
			input: `bucket: abcd
http_config:
  insecure_skip_verify: true
  idle_conn_timeout: 50s
  response_header_timeout: 1m`,
			assertions: func(cfg Config) {
				testutil.Equals(t, cfg.HTTPConfig.IdleConnTimeout, model.Duration(50*time.Second))
				testutil.Equals(t, cfg.HTTPConfig.ResponseHeaderTimeout, model.Duration(1*time.Minute))
				testutil.Equals(t, cfg.HTTPConfig.InsecureSkipVerify, true)
			},
		},
		{
			name: "CustomHTTPConfigWithTLS",
			input: `bucket: abcd
http_config:
  tls_config:
    ca_file: /certs/ca.crt
    cert_file: /certs/cert.crt
    key_file: /certs/key.key
    server_name: server
    insecure_skip_verify: false`,
			assertions: func(cfg Config) {
				testutil.Equals(t, "/certs/ca.crt", cfg.HTTPConfig.TLSConfig.CAFile)
				testutil.Equals(t, "/certs/cert.crt", cfg.HTTPConfig.TLSConfig.CertFile)
				testutil.Equals(t, "/certs/key.key", cfg.HTTPConfig.TLSConfig.KeyFile)
				testutil.Equals(t, "server", cfg.HTTPConfig.TLSConfig.ServerName)
				testutil.Equals(t, false, cfg.HTTPConfig.TLSConfig.InsecureSkipVerify)
			},
		},
	} {
		t.Run(tc.name, func(t *testing.T) {
			cfg, err := parseConfig([]byte(tc.input))
			testutil.Ok(t, err)
			tc.assertions(cfg)
		})
	}
}

func TestNewBucketWithErrorRoundTripper(t *testing.T) {
	cfg := Config{
		Bucket:         "test-bucket",
		ServiceAccount: "",
		UseGRPC:        false,
		noAuth:         true,
	}
	svr, err := gcsemu.NewServer("127.0.0.1:0", gcsemu.Options{})
	testutil.Ok(t, err)
	defer svr.Close()
	err = os.Setenv("STORAGE_EMULATOR_HOST", svr.Addr)
	testutil.Ok(t, err)

	bkt, err := NewBucketWithConfig(context.Background(), log.NewNopLogger(), cfg, "test-bucket", errutil.WrapWithErrRoundtripper)
	testutil.Ok(t, err)
	_, err = bkt.Get(context.Background(), "test-bucket")
	testutil.NotOk(t, err)
	testutil.Assert(t, errutil.IsMockedError(err), "Expected RoundTripper error, got: %v", err)
}
```

## File: `providers/obs/obs.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package obs

import (
	"context"
	"io"
	"math"
	"os"
	"strings"
	"testing"
	"time"

	"github.com/thanos-io/objstore"
	"github.com/thanos-io/objstore/exthttp"

	"github.com/go-kit/log"
	"github.com/huaweicloud/huaweicloud-sdk-go-obs/obs"
	"github.com/pkg/errors"
	"github.com/prometheus/common/model"
	"gopkg.in/yaml.v2"
)

const DirDelim = "/"

const (
	MinMultipartUploadSize int64 = 1024 * 1024 * 100
	PartSize               int64 = 1024 * 1024 * 100
)

var DefaultConfig = Config{
	HTTPConfig: exthttp.HTTPConfig{
		IdleConnTimeout:       model.Duration(90 * time.Second),
		ResponseHeaderTimeout: model.Duration(2 * time.Minute),
		TLSHandshakeTimeout:   model.Duration(10 * time.Second),
		ExpectContinueTimeout: model.Duration(1 * time.Second),
		MaxIdleConns:          100,
		MaxIdleConnsPerHost:   100,
		MaxConnsPerHost:       0,
	},
}

type Config struct {
	Bucket     string             `yaml:"bucket"`
	Endpoint   string             `yaml:"endpoint"`
	AccessKey  string             `yaml:"access_key"`
	SecretKey  string             `yaml:"secret_key"`
	MaxRetries int                `yaml:"max_retries"`
	HTTPConfig exthttp.HTTPConfig `yaml:"http_config"`
}

func (conf *Config) validate() error {
	if conf.Endpoint == "" {
		return errors.New("no obs endpoint in config file")
	}

	if conf.AccessKey == "" && conf.SecretKey != "" {
		return errors.New("no obs access_key specified")
	}

	if conf.AccessKey != "" && conf.SecretKey == "" {
		return errors.New("no obs secret_key specified")
	}

	if conf.AccessKey == "" && conf.SecretKey == "" {
		return errors.New("no obs secret_key and access_key specified")
	}
	return nil
}

type Bucket struct {
	logger log.Logger
	client *obs.ObsClient
	name   string
}

func NewBucket(logger log.Logger, conf []byte) (*Bucket, error) {
	// TODO(https://github.com/thanos-io/objstore/pull/150): Add support for roundtripper wrapper.
	config, err := parseConfig(conf)
	if err != nil {
		return nil, errors.Wrap(err, "parsing cos configuration")
	}
	return NewBucketWithConfig(logger, config)
}

func parseConfig(conf []byte) (Config, error) {
	config := DefaultConfig
	if err := yaml.UnmarshalStrict(conf, &config); err != nil {
		return Config{}, err
	}

	return config, nil
}

func NewBucketWithConfig(logger log.Logger, config Config) (*Bucket, error) {
	if err := config.validate(); err != nil {
		return nil, errors.Wrap(err, "validate obs config err")
	}

	rt, err := exthttp.DefaultTransport(config.HTTPConfig)
	if err != nil {
		return nil, errors.Wrap(err, "get http transport err")
	}

	var client *obs.ObsClient
	if config.MaxRetries > 0 {
		client, err = obs.New(config.AccessKey, config.SecretKey, config.Endpoint, obs.WithHttpTransport(rt), obs.WithMaxRetryCount(config.MaxRetries))
	} else {
		client, err = obs.New(config.AccessKey, config.SecretKey, config.Endpoint, obs.WithHttpTransport(rt))
	}

	if err != nil {
		return nil, errors.Wrap(err, "initialize obs client err")
	}

	bkt := &Bucket{
		logger: logger,
		client: client,
		name:   config.Bucket,
	}
	return bkt, nil
}

func (b *Bucket) Provider() objstore.ObjProvider { return objstore.OBS }

// Name returns the bucket name for the provider.
func (b *Bucket) Name() string {
	return b.name
}

// Delete removes the object with the given name.
func (b *Bucket) Delete(ctx context.Context, name string) error {
	input := &obs.DeleteObjectInput{Bucket: b.name, Key: name}
	_, err := b.client.DeleteObject(input)
	return err
}

// Upload the contents of the reader as an object into the bucket.
func (b *Bucket) Upload(ctx context.Context, name string, r io.Reader, opts ...objstore.ObjectUploadOption) error {
	size, err := objstore.TryToGetSize(r)

	if err != nil {
		return errors.Wrapf(err, "failed to get size apriori to upload %s", name)
	}

	if size <= 0 {
		return errors.New("object size must be provided")
	}

	uploadOpts := objstore.ApplyObjectUploadOptions(opts...)
	if size <= MinMultipartUploadSize {
		err = b.putObjectSingle(name, r, uploadOpts)
		if err != nil {
			return err
		}
	} else {
		var initOutput *obs.InitiateMultipartUploadOutput
		initOutput, err = b.initiateMultipartUpload(name, uploadOpts)
		if err != nil {
			return err
		}

		uploadId := initOutput.UploadId
		defer func() {
			if err != nil {
				if _, err = b.client.AbortMultipartUpload(&obs.AbortMultipartUploadInput{
					UploadId: uploadId,
					Bucket:   b.name,
					Key:      name,
				}); err != nil {
					err = errors.Wrap(err, "failed to abort multipart upload")
					return
				}
			}
		}()
		parts, err := b.multipartUpload(size, name, uploadId, r)
		if err != nil {
			return err
		}

		_, err = b.client.CompleteMultipartUpload(&obs.CompleteMultipartUploadInput{
			Bucket:   b.name,
			Key:      name,
			UploadId: uploadId,
			Parts:    parts,
		})
		if err != nil {
			return errors.Wrap(err, "failed to complete multipart upload")
		}
	}
	return nil
}

func (b *Bucket) putObjectSingle(key string, body io.Reader, opts objstore.UploadObjectParams) error {
	input := &obs.PutObjectInput{}
	input.Bucket = b.name
	input.Key = key
	input.Body = body
	input.ContentType = opts.ContentType
	_, err := b.client.PutObject(input)
	if err != nil {
		return errors.Wrap(err, "failed to upload object")
	}
	return nil
}

func (b *Bucket) initiateMultipartUpload(key string, opts objstore.UploadObjectParams) (output *obs.InitiateMultipartUploadOutput, err error) {
	initInput := &obs.InitiateMultipartUploadInput{}
	initInput.Bucket = b.name
	initInput.Key = key
	initInput.ContentType = opts.ContentType
	initOutput, err := b.client.InitiateMultipartUpload(initInput)
	if err != nil {
		return nil, errors.Wrap(err, "failed to init multipart upload job")
	}
	return initOutput, nil
}

func (b *Bucket) multipartUpload(size int64, key, uploadId string, body io.Reader) ([]obs.Part, error) {
	partSum := int(math.Ceil(float64(size) / float64(PartSize)))
	lastPart := size % PartSize
	parts := make([]obs.Part, 0, partSum)
	for i := 1; i <= partSum; i++ {
		partSize := PartSize
		if i == partSum {
			partSize = lastPart
		}
		output, err := b.client.UploadPart(&obs.UploadPartInput{
			Bucket:     b.name,
			Key:        key,
			UploadId:   uploadId,
			Body:       body,
			PartNumber: i,
			PartSize:   partSize,
			Offset:     int64(i-1) * PartSize,
		})
		if err != nil {
			return nil, errors.Wrap(err, "failed to multipart upload")
		}
		parts = append(parts, obs.Part{PartNumber: output.PartNumber, ETag: output.ETag})
	}
	return parts, nil
}

func (b *Bucket) Close() error { return nil }

func (b *Bucket) SupportedIterOptions() []objstore.IterOptionType {
	return []objstore.IterOptionType{objstore.Recursive}
}

// Iter calls f for each entry in the given directory (not recursive.)
func (b *Bucket) Iter(ctx context.Context, dir string, f func(string) error, options ...objstore.IterOption) error {
	if dir != "" {
		dir = strings.TrimSuffix(dir, DirDelim) + DirDelim
	}

	input := &obs.ListObjectsInput{}
	input.Bucket = b.name
	input.Prefix = dir
	input.Delimiter = DirDelim
	if objstore.ApplyIterOptions(options...).Recursive {
		input.Delimiter = ""
	}
	for {
		output, err := b.client.ListObjects(input)
		if err != nil {
			return errors.Wrap(err, "failed to list object")
		}
		for _, content := range output.Contents {
			if err := f(content.Key); err != nil {
				return errors.Wrapf(err, "failed to call iter function for object %s", content.Key)
			}
		}
		for _, topDir := range output.CommonPrefixes {
			if err := f(topDir); err != nil {
				return errors.Wrapf(err, "failed to call iter function for top dir object %s", topDir)
			}
		}

		if !output.IsTruncated {
			break
		}

		input.Marker = output.NextMarker
	}
	return nil
}

func (b *Bucket) IterWithAttributes(ctx context.Context, dir string, f func(attrs objstore.IterObjectAttributes) error, options ...objstore.IterOption) error {
	if err := objstore.ValidateIterOptions(b.SupportedIterOptions(), options...); err != nil {
		return err
	}

	return b.Iter(ctx, dir, func(name string) error {
		return f(objstore.IterObjectAttributes{Name: name})
	}, options...)
}

// Get returns a reader for the given object name.
func (b *Bucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	return b.getRange(ctx, name, 0, -1)
}

// GetRange returns a new range reader for the given object name and range.
func (b *Bucket) GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	return b.getRange(ctx, name, off, length)
}

func (b *Bucket) getRange(_ context.Context, name string, off, length int64) (io.ReadCloser, error) {
	if strings.TrimSpace(name) == "" {
		return nil, errors.New("object name cannot be empty")
	}
	input := &obs.GetObjectInput{}
	input.Bucket = b.name
	input.Key = name
	if off < 0 {
		return nil, errors.New("incorrect offset")
	}
	input.RangeStart = off
	input.RangeEnd = math.MaxInt64
	if length != -1 {
		input.RangeEnd = off + length - 1
	}
	output, err := b.client.GetObject(input)
	if err != nil {
		return nil, errors.Wrap(err, "failed to get object")
	}
	return objstore.ObjectSizerReadCloser{
		ReadCloser: output.Body,
		Size: func() (int64, error) {
			return output.ContentLength, nil
		},
	}, nil
}

// Exists checks if the given object exists in the bucket.
func (b *Bucket) Exists(ctx context.Context, name string) (bool, error) {
	_, err := b.client.GetObjectMetadata(&obs.GetObjectMetadataInput{
		Bucket: b.name,
		Key:    name,
	})
	if err != nil {
		if b.IsObjNotFoundErr(err) {
			return false, nil
		}
		return false, errors.Wrap(err, "failed to get object metadata")
	}
	return true, nil
}

// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
func (b *Bucket) IsObjNotFoundErr(err error) bool {
	if oriErr, ok := errors.Cause(err).(obs.ObsError); ok {
		if oriErr.Status == "404 Not Found" {
			return true
		}
	}
	return false
}

// IsAccessDeniedErr returns true if access to object is denied.
func (b *Bucket) IsAccessDeniedErr(_ error) bool {
	return false
}

// Attributes returns information about the specified object.
func (b *Bucket) Attributes(ctx context.Context, name string) (objstore.ObjectAttributes, error) {
	output, err := b.client.GetObjectMetadata(&obs.GetObjectMetadataInput{
		Bucket: b.name,
		Key:    name,
	})
	if err != nil {
		return objstore.ObjectAttributes{}, errors.Wrap(err, "failed to get object metadata")
	}
	return objstore.ObjectAttributes{
		Size:         output.ContentLength,
		LastModified: output.LastModified,
	}, nil
}

// NewTestBucket creates test bkt client that before returning creates temporary bucket.
func NewTestBucket(t testing.TB, location string) (objstore.Bucket, func(), error) {
	c := configFromEnv()
	if c.Endpoint == "" || c.AccessKey == "" || c.SecretKey == "" {
		return nil, nil, errors.New("insufficient obs test configuration information")
	}

	if c.Bucket != "" && os.Getenv("THANOS_ALLOW_EXISTING_BUCKET_USE") == "" {
		return nil, nil, errors.New("OBS_BUCKET is defined. Normally this tests will create temporary bucket " +
			"and delete it after test. Unset OBS_BUCKET env variable to use default logic. If you really want to run " +
			"tests against provided (NOT USED!) bucket, set THANOS_ALLOW_EXISTING_BUCKET_USE=true.")
	}
	return NewTestBucketFromConfig(t, c, false, location)
}

func NewTestBucketFromConfig(t testing.TB, c Config, reuseBucket bool, location string) (objstore.Bucket, func(), error) {
	ctx := context.Background()

	bc, err := yaml.Marshal(c)
	if err != nil {
		return nil, nil, err
	}
	b, err := NewBucket(log.NewNopLogger(), bc)
	if err != nil {
		return nil, nil, err
	}

	bktToCreate := c.Bucket
	if c.Bucket != "" && reuseBucket {
		if err := b.Iter(ctx, "", func(_ string) error {
			return errors.Errorf("bucket %s is not empty", c.Bucket)
		}); err != nil {
			return nil, nil, err
		}

		t.Log("WARNING. Reusing", c.Bucket, "OBS bucket for OBS tests. Manual cleanup afterwards is required")
		return b, func() {}, nil
	}

	if c.Bucket == "" {
		bktToCreate = objstore.CreateTemporaryTestBucketName(t)
	}

	_, err = b.client.CreateBucket(&obs.CreateBucketInput{
		Bucket:         bktToCreate,
		BucketLocation: obs.BucketLocation{Location: location},
	})
	if err != nil {
		return nil, nil, err
	}
	b.name = bktToCreate
	t.Log("created temporary OBS bucket for OBS tests with name", bktToCreate)

	return b, func() {
		objstore.EmptyBucket(t, ctx, b)
		if _, err := b.client.DeleteBucket(bktToCreate); err != nil {
			t.Logf("deleting bucket %s failed: %s", bktToCreate, err)
		}
	}, nil
}

func configFromEnv() Config {
	c := Config{
		Bucket:    os.Getenv("OBS_BUCKET"),
		Endpoint:  os.Getenv("OBS_ENDPOINT"),
		AccessKey: os.Getenv("OBS_ACCESS_KEY"),
		SecretKey: os.Getenv("OBS_SECRET_KEY"),
	}
	return c
}
```

## File: `providers/oci/helper.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package oci

import (
	"context"
	"crypto/tls"
	"fmt"
	"net"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/oracle/oci-go-sdk/v65/common"
	"github.com/oracle/oci-go-sdk/v65/objectstorage"
	"github.com/pkg/errors"
	"github.com/prometheus/common/model"
	"github.com/thanos-io/objstore"
)

func CustomTransport(config Config) *http.Transport {
	return &http.Transport{
		Proxy: http.ProxyFromEnvironment,
		DialContext: (&net.Dialer{
			Timeout:   30 * time.Second,
			KeepAlive: 30 * time.Second,
		}).DialContext,

		IdleConnTimeout:       time.Duration(config.HTTPConfig.IdleConnTimeout),
		ResponseHeaderTimeout: time.Duration(config.HTTPConfig.ResponseHeaderTimeout),
		TLSHandshakeTimeout:   time.Duration(config.HTTPConfig.TLSHandshakeTimeout),
		ExpectContinueTimeout: time.Duration(config.HTTPConfig.ExpectContinueTimeout),
		TLSClientConfig:       &tls.Config{InsecureSkipVerify: config.HTTPConfig.InsecureSkipVerify},
		MaxIdleConns:          config.HTTPConfig.MaxIdleConns,
		MaxIdleConnsPerHost:   config.HTTPConfig.MaxIdleConnsPerHost,
		MaxConnsPerHost:       config.HTTPConfig.MaxConnsPerHost,
		DisableCompression:    config.HTTPConfig.DisableCompression,
	}
}

func getNamespace(client objectstorage.ObjectStorageClient, requestMetadata common.RequestMetadata) (namespace *string, err error) {
	response, err := client.GetNamespace(
		context.Background(),
		objectstorage.GetNamespaceRequest{RequestMetadata: requestMetadata},
	)
	if err != nil {
		return nil, err
	}
	return response.Value, nil
}

func getObject(ctx context.Context, bkt Bucket, objectName string, byteRange string) (response objectstorage.GetObjectResponse, err error) {
	if len(objectName) == 0 {
		err = fmt.Errorf("value cannot be empty for field ObjectName in path")
		return
	}
	request := objectstorage.GetObjectRequest{
		NamespaceName:   &bkt.namespace,
		BucketName:      &bkt.name,
		ObjectName:      &objectName,
		RequestMetadata: bkt.requestMetadata,
	}
	if byteRange != "" {
		request.Range = &byteRange
	}
	return bkt.client.GetObject(ctx, request)
}

func listAllObjects(ctx context.Context, bkt Bucket, prefix string, options ...objstore.IterOption) (objectNames []string, err error) {
	var allObjectNames []string
	var nextStartWith *string = nil
	init := true

	for init || nextStartWith != nil {
		init = false
		objectNames, nextStartWith, err = listObjects(ctx, bkt, prefix, nextStartWith)
		if err != nil {
			return nil, err
		}

		if objstore.ApplyIterOptions(options...).Recursive {
			for _, objectName := range objectNames {
				if strings.HasSuffix(objectName, DirDelim) {
					subObjectNames, err := listAllObjects(ctx, bkt, objectName, options...)
					if err != nil {
						return nil, err
					}
					allObjectNames = append(allObjectNames, subObjectNames...)
				} else {
					allObjectNames = append(allObjectNames, objectName)
				}
			}
		} else {
			allObjectNames = append(allObjectNames, objectNames...)
		}
	}
	return allObjectNames, nil
}

func listObjects(ctx context.Context, bkt Bucket, prefix string, start *string) (objectNames []string, nextStartWith *string, err error) {
	request := objectstorage.ListObjectsRequest{
		NamespaceName:   &bkt.namespace,
		BucketName:      &bkt.name,
		Delimiter:       common.String(DirDelim),
		Prefix:          &prefix,
		Start:           start,
		RequestMetadata: bkt.requestMetadata,
	}
	response, err := bkt.client.ListObjects(ctx, request)
	if err != nil {
		return nil, nil, err
	}

	for _, object := range response.ListObjects.Objects {
		objectNames = append(objectNames, *object.Name)
	}
	objectNames = append(objectNames, response.ListObjects.Prefixes...)

	return objectNames, response.NextStartWith, nil
}

func (config *Config) validateConfig() (err error) {
	var errMsg []string

	if config.Tenancy == "" {
		errMsg = append(errMsg, "no OCI tenancy ocid specified")
	}
	if config.User == "" {
		errMsg = append(errMsg, "no OCI user ocid specified")
	}
	if config.Region == "" {
		errMsg = append(errMsg, "no OCI region specified")
	}
	if config.Fingerprint == "" {
		errMsg = append(errMsg, "no OCI fingerprint specified")
	}
	if config.PrivateKey == "" {
		errMsg = append(errMsg, "no OCI privatekey specified")
	}

	if len(errMsg) > 0 {
		return errors.New(strings.Join(errMsg, ", "))
	}

	return
}

func getRequestMetadata(maxRequestRetries int, requestRetryInterval int) common.RequestMetadata {
	if maxRequestRetries <= 1 {
		retryPolicy := common.NoRetryPolicy()
		return common.RequestMetadata{
			RetryPolicy: &retryPolicy,
		}
	}
	retryPolicy := common.NewRetryPolicyWithOptions(common.WithMaximumNumberAttempts(uint(maxRequestRetries)),
		common.WithFixedBackoff(time.Duration(requestRetryInterval)*time.Second))
	return common.RequestMetadata{
		RetryPolicy: &retryPolicy,
	}
}

func getConfigFromEnv() (config Config, err error) {
	config = Config{
		Provider:    strings.ToLower(os.Getenv("OCI_PROVIDER")),
		Bucket:      os.Getenv("OCI_BUCKET"),
		Compartment: os.Getenv("OCI_COMPARTMENT"),
		Tenancy:     os.Getenv("OCI_TENANCY_OCID"),
		User:        os.Getenv("OCI_USER_OCID"),
		Region:      os.Getenv("OCI_REGION"),
		Fingerprint: os.Getenv("OCI_FINGERPRINT"),
		PrivateKey:  os.Getenv("OCI_PRIVATEKEY"),
		Passphrase:  os.Getenv("OCI_PASSPHRASE"),
	}

	// [Optional] Override the default part size of 128 MiB, value is in bytes. The max part size is 50GiB
	if os.Getenv("OCI_PART_SIZE") != "" {
		partSize, err := strconv.ParseInt(os.Getenv("OCI_PART_SIZE"), 10, 64)
		if err != nil {
			return Config{}, err
		}
		config.PartSize = partSize
	}

	if os.Getenv("OCI_MAX_REQUEST_RETRIES") != "" {
		maxRequestRetries, err := strconv.Atoi(os.Getenv("OCI_MAX_REQUEST_RETRIES"))
		if err != nil {
			return Config{}, err
		}
		config.MaxRequestRetries = maxRequestRetries
	}

	if os.Getenv("OCI_REQUEST_RETRY_INTERVAL") != "" {
		requestRetryInterval, err := strconv.Atoi(os.Getenv("OCI_REQUEST_RETRY_INTERVAL"))
		if err != nil {
			return Config{}, err
		}
		config.RequestRetryInterval = requestRetryInterval
	}

	if os.Getenv("HTTP_CONFIG_IDLE_CONN_TIMEOUT") != "" {
		idleConnTimeout, err := model.ParseDuration(os.Getenv("HTTP_CONFIG_IDLE_CONN_TIMEOUT"))
		if err != nil {
			return Config{}, err
		}
		config.HTTPConfig.IdleConnTimeout = idleConnTimeout
	}

	if os.Getenv("HTTP_CONFIG_RESPONSE_HEADER_TIMEOUT") != "" {
		responseHeaderTimeout, err := model.ParseDuration(os.Getenv("HTTP_CONFIG_RESPONSE_HEADER_TIMEOUT"))
		if err != nil {
			return Config{}, err
		}
		config.HTTPConfig.ResponseHeaderTimeout = responseHeaderTimeout
	}

	if os.Getenv("HTTP_CONFIG_TLS_HANDSHAKE_TIMEOUT") != "" {
		tlsHandshakeTimeout, err := model.ParseDuration(os.Getenv("HTTP_CONFIG_TLS_HANDSHAKE_TIMEOUT"))
		if err != nil {
			return Config{}, err
		}
		config.HTTPConfig.TLSHandshakeTimeout = tlsHandshakeTimeout
	}

	if os.Getenv("HTTP_CONFIG_EXPECT_CONTINUE_TIMEOUT") != "" {
		expectContinueTimeout, err := model.ParseDuration(os.Getenv("HTTP_CONFIG_EXPECT_CONTINUE_TIMEOUT"))
		if err != nil {
			return Config{}, err
		}
		config.HTTPConfig.ExpectContinueTimeout = expectContinueTimeout
	}

	if os.Getenv("HTTP_CONFIG_INSECURE_SKIP_VERIFY") != "" {
		insecureSkipVerify, err := strconv.ParseBool(os.Getenv("HTTP_CONFIG_INSECURE_SKIP_VERIFY"))
		if err != nil {
			return Config{}, err
		}
		config.HTTPConfig.InsecureSkipVerify = insecureSkipVerify
	}

	if os.Getenv("HTTP_CONFIG_MAX_IDLE_CONNS") != "" {
		maxIdleConns, err := strconv.Atoi(os.Getenv("HTTP_CONFIG_MAX_IDLE_CONNS"))
		if err != nil {
			return Config{}, err
		}
		config.HTTPConfig.MaxIdleConns = maxIdleConns
	}

	if os.Getenv("HTTP_CONFIG_MAX_IDLE_CONNS_PER_HOST") != "" {
		maxIdleConnsPerHost, err := strconv.Atoi(os.Getenv("HTTP_CONFIG_MAX_IDLE_CONNS_PER_HOST"))
		if err != nil {
			return Config{}, err
		}
		config.HTTPConfig.MaxIdleConnsPerHost = maxIdleConnsPerHost
	}

	if os.Getenv("HTTP_CONFIG_MAX_CONNS_PER_HOST") != "" {
		maxConnsPerHost, err := strconv.Atoi(os.Getenv("HTTP_CONFIG_MAX_CONNS_PER_HOST"))
		if err != nil {
			return Config{}, err
		}
		config.HTTPConfig.MaxConnsPerHost = maxConnsPerHost
	}

	if os.Getenv("HTTP_CONFIG_DISABLE_COMPRESSION") != "" {
		disableCompression, err := strconv.ParseBool(os.Getenv("HTTP_CONFIG_DISABLE_COMPRESSION"))
		if err != nil {
			return Config{}, err
		}
		config.HTTPConfig.DisableCompression = disableCompression
	}

	return config, nil
}
```

## File: `providers/oci/oci.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package oci

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
	"testing"
	"time"

	"github.com/go-kit/log"
	"github.com/go-kit/log/level"
	"github.com/oracle/oci-go-sdk/v65/common"
	"github.com/oracle/oci-go-sdk/v65/common/auth"
	"github.com/oracle/oci-go-sdk/v65/objectstorage"
	"github.com/oracle/oci-go-sdk/v65/objectstorage/transfer"
	"github.com/pkg/errors"
	"github.com/prometheus/common/model"
	"gopkg.in/yaml.v2"

	"github.com/thanos-io/objstore"
)

// DirDelim is the delimiter used to model a directory structure in an object store bucket.
const DirDelim = "/"

type Provider string

const (
	defaultConfigProvider             = Provider("default")
	instancePrincipalConfigProvider   = Provider("instance-principal")
	rawConfigProvider                 = Provider("raw")
	okeWorkloadIdentityConfigProvider = Provider("oke-workload-identity")
)

var DefaultConfig = Config{
	HTTPConfig: HTTPConfig{
		IdleConnTimeout:       model.Duration(90 * time.Second),
		ResponseHeaderTimeout: model.Duration(2 * time.Minute),
		TLSHandshakeTimeout:   model.Duration(10 * time.Second),
		ExpectContinueTimeout: model.Duration(1 * time.Second),
		InsecureSkipVerify:    false,
		MaxIdleConns:          100,
		MaxIdleConnsPerHost:   100,
		MaxConnsPerHost:       0,
		DisableCompression:    false,
		ClientTimeout:         90 * time.Second,
	},
}

// HTTPConfig stores the http.Transport configuration for the OCI client.
type HTTPConfig struct {
	IdleConnTimeout       model.Duration `yaml:"idle_conn_timeout"`
	ResponseHeaderTimeout model.Duration `yaml:"response_header_timeout"`
	InsecureSkipVerify    bool           `yaml:"insecure_skip_verify"`

	TLSHandshakeTimeout   model.Duration    `yaml:"tls_handshake_timeout"`
	ExpectContinueTimeout model.Duration    `yaml:"expect_continue_timeout"`
	MaxIdleConns          int               `yaml:"max_idle_conns"`
	MaxIdleConnsPerHost   int               `yaml:"max_idle_conns_per_host"`
	MaxConnsPerHost       int               `yaml:"max_conns_per_host"`
	DisableCompression    bool              `yaml:"disable_compression"`
	ClientTimeout         time.Duration     `yaml:"client_timeout"`
	Transport             http.RoundTripper `yaml:"-"`
}

// Config stores the configuration for oci bucket.
type Config struct {
	Provider             string     `yaml:"provider"`
	Bucket               string     `yaml:"bucket"`
	Compartment          string     `yaml:"compartment_ocid"`
	Tenancy              string     `yaml:"tenancy_ocid"`
	User                 string     `yaml:"user_ocid"`
	Region               string     `yaml:"region"`
	Fingerprint          string     `yaml:"fingerprint"`
	PrivateKey           string     `yaml:"privatekey"`
	Passphrase           string     `yaml:"passphrase"`
	PartSize             int64      `yaml:"part_size"`
	MaxRequestRetries    int        `yaml:"max_request_retries"`
	RequestRetryInterval int        `yaml:"request_retry_interval"`
	HTTPConfig           HTTPConfig `yaml:"http_config"`
}

// Bucket implements the store.Bucket interface against OCI APIs.
type Bucket struct {
	logger          log.Logger
	name            string
	namespace       string
	client          *objectstorage.ObjectStorageClient
	partSize        int64
	requestMetadata common.RequestMetadata
}

func (b *Bucket) Provider() objstore.ObjProvider { return objstore.OCI }

// Name returns the bucket name for the provider.
func (b *Bucket) Name() string {
	return b.name
}

func (b *Bucket) SupportedIterOptions() []objstore.IterOptionType {
	return []objstore.IterOptionType{objstore.Recursive}
}

// Iter calls f for each entry in the given directory. The argument to f is the full
// object name including the prefix of the inspected directory.
func (b *Bucket) Iter(ctx context.Context, dir string, f func(string) error, options ...objstore.IterOption) error {
	// Ensure the object name actually ends with a dir suffix. Otherwise we'll just iterate the
	// object itself as one prefix item.
	if dir != "" {
		dir = strings.TrimSuffix(dir, DirDelim) + DirDelim
	}

	objectNames, err := listAllObjects(ctx, *b, dir, options...)
	if err != nil {
		return errors.Wrapf(err, "cannot list objects in directory '%s'", dir)
	}

	level.Debug(b.logger).Log("NumberOfObjects", len(objectNames))

	for _, objectName := range objectNames {
		if objectName == "" || objectName == dir {
			continue
		}

		if err := f(objectName); err != nil {
			return err
		}
	}

	return nil
}

func (b *Bucket) IterWithAttributes(ctx context.Context, dir string, f func(attrs objstore.IterObjectAttributes) error, options ...objstore.IterOption) error {
	if err := objstore.ValidateIterOptions(b.SupportedIterOptions(), options...); err != nil {
		return err
	}

	return b.Iter(ctx, dir, func(name string) error {
		return f(objstore.IterObjectAttributes{Name: name})
	}, options...)
}

// Get returns a reader for the given object name.
func (b *Bucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	response, err := getObject(ctx, *b, name, "")
	if err != nil {
		return nil, err
	}
	return objstore.ObjectSizerReadCloser{
		ReadCloser: response.Content,
		Size: func() (int64, error) {
			return *response.ContentLength, nil
		},
	}, nil
}

// GetRange returns a new range reader for the given object name and range.
func (b *Bucket) GetRange(ctx context.Context, name string, offset, length int64) (io.ReadCloser, error) {
	level.Debug(b.logger).Log("msg", "getting object", "name", name, "off", offset, "length", length)

	// A single byte range to fetch, as described in RFC 7233 (https://tools.ietf.org/html/rfc7233#section-2.1).
	byteRange := ""

	if offset >= 0 {
		if length > 0 {
			byteRange = fmt.Sprintf("bytes=%d-%d", offset, offset+length-1)
		} else {
			byteRange = fmt.Sprintf("bytes=%d-", offset)
		}
	} else {
		if length > 0 {
			byteRange = fmt.Sprintf("bytes=-%d", length)
		} else {
			return nil, errors.New(fmt.Sprintf("invalid range specified: offset=%d length=%d", offset, length))
		}
	}

	level.Debug(b.logger).Log("byteRange", byteRange)

	response, err := getObject(ctx, *b, name, byteRange)
	if err != nil {
		return nil, err
	}
	return objstore.ObjectSizerReadCloser{ReadCloser: response.Content,
		Size: func() (int64, error) {
			return *response.ContentLength, nil
		},
	}, nil
}

// Upload the contents of the reader as an object into the bucket.
// Upload should be idempotent.
func (b *Bucket) Upload(ctx context.Context, name string, r io.Reader, opts ...objstore.ObjectUploadOption) (err error) {
	req := transfer.UploadStreamRequest{
		UploadRequest: transfer.UploadRequest{
			NamespaceName:                       common.String(b.namespace),
			BucketName:                          common.String(b.name),
			ObjectName:                          &name,
			EnableMultipartChecksumVerification: common.Bool(true), // TODO: should we check?
			ObjectStorageClient:                 b.client,
			RequestMetadata:                     b.requestMetadata,
		},
		StreamReader: r,
	}
	if b.partSize > 0 {
		req.UploadRequest.PartSize = &b.partSize
	}

	uploadOptions := objstore.ApplyObjectUploadOptions(opts...)
	if uploadOptions.ContentType != "" {
		req.UploadRequest.ContentType = &uploadOptions.ContentType
	}

	uploadManager := transfer.NewUploadManager()
	_, err = uploadManager.UploadStream(ctx, req)

	return err
}

// Exists checks if the given object exists in the bucket.
func (b *Bucket) Exists(ctx context.Context, name string) (bool, error) {
	_, err := getObject(ctx, *b, name, "")
	if err != nil {
		if b.IsObjNotFoundErr(err) {
			return false, nil
		}
		return false, errors.Wrapf(err, "cannot get OCI object '%s'", name)
	}
	return true, nil
}

// Delete removes the object with the given name.
// If object does not exists in the moment of deletion, Delete should throw error.
func (b *Bucket) Delete(ctx context.Context, name string) (err error) {
	request := objectstorage.DeleteObjectRequest{
		NamespaceName:   &b.namespace,
		BucketName:      &b.name,
		ObjectName:      &name,
		RequestMetadata: b.requestMetadata,
	}
	_, err = b.client.DeleteObject(ctx, request)
	return err
}

// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
func (b *Bucket) IsObjNotFoundErr(err error) bool {
	failure, isServiceError := common.IsServiceError(err)
	if isServiceError {
		k := failure.GetHTTPStatusCode()
		match := k == http.StatusNotFound
		level.Debug(b.logger).Log("msg", match)
		return failure.GetHTTPStatusCode() == http.StatusNotFound
	}
	return false
}

// IsAccessDeniedErr returns true if access to object is denied.
func (b *Bucket) IsAccessDeniedErr(err error) bool {
	failure, isServiceError := common.IsServiceError(err)
	if isServiceError {
		return failure.GetHTTPStatusCode() == http.StatusForbidden
	}
	return false
}

// ObjectSize returns the size of the specified object.
func (b *Bucket) ObjectSize(ctx context.Context, name string) (uint64, error) {
	response, err := getObject(ctx, *b, name, "")
	if err != nil {
		return 0, err
	}
	return uint64(*response.ContentLength), nil
}

// Close closes bucket.
func (b *Bucket) Close() error {
	return nil
}

// Attributes returns information about the specified object.
func (b *Bucket) Attributes(ctx context.Context, name string) (objstore.ObjectAttributes, error) {
	response, err := getObject(ctx, *b, name, "")
	if err != nil {
		return objstore.ObjectAttributes{}, err
	}
	return objstore.ObjectAttributes{
		Size:         *response.ContentLength,
		LastModified: response.LastModified.Time,
	}, nil
}

// createBucket creates bucket.
func (b *Bucket) createBucket(ctx context.Context, compartmentId string) (err error) {
	request := objectstorage.CreateBucketRequest{
		NamespaceName:   &b.namespace,
		RequestMetadata: b.requestMetadata,
	}
	request.CompartmentId = &compartmentId
	request.Name = &b.name
	request.Metadata = make(map[string]string)
	request.PublicAccessType = objectstorage.CreateBucketDetailsPublicAccessTypeNopublicaccess
	_, err = b.client.CreateBucket(ctx, request)
	return err
}

// deleteBucket deletes bucket.
func (b *Bucket) deleteBucket(ctx context.Context) (err error) {
	request := objectstorage.DeleteBucketRequest{
		NamespaceName:   &b.namespace,
		BucketName:      &b.name,
		RequestMetadata: b.requestMetadata,
	}
	_, err = b.client.DeleteBucket(ctx, request)
	return err
}

// NewBucket returns a new Bucket using the provided oci config values.
func NewBucket(logger log.Logger, ociConfig []byte, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Bucket, error) {
	level.Debug(logger).Log("msg", "creating new oci bucket connection")
	var config = DefaultConfig
	var configurationProvider common.ConfigurationProvider
	var err error

	if err := yaml.Unmarshal(ociConfig, &config); err != nil {
		return nil, errors.Wrapf(err, "unable to unmarshal the given oci configurations")
	}

	provider := Provider(strings.ToLower(config.Provider))
	level.Info(logger).Log("msg", "creating OCI client", "provider", provider)
	switch provider {
	case defaultConfigProvider:
		configurationProvider = common.DefaultConfigProvider()
	case instancePrincipalConfigProvider:
		configurationProvider, err = auth.InstancePrincipalConfigurationProvider()
		if err != nil {
			return nil, errors.Wrapf(err, "unable to create OCI instance principal config provider")
		}
	case rawConfigProvider:
		if err := config.validateConfig(); err != nil {
			return nil, errors.Wrapf(err, "invalid oci configurations")
		}
		configurationProvider = common.NewRawConfigurationProvider(config.Tenancy, config.User, config.Region,
			config.Fingerprint, config.PrivateKey, &config.Passphrase)
	case okeWorkloadIdentityConfigProvider:
		if err := os.Setenv(auth.ResourcePrincipalVersionEnvVar, auth.ResourcePrincipalVersion2_2); err != nil {
			return nil, errors.Wrapf(err, "unable to set environment variable: %s", auth.ResourcePrincipalVersionEnvVar)
		}
		if err := os.Setenv(auth.ResourcePrincipalRegionEnvVar, config.Region); err != nil {
			return nil, errors.Wrapf(err, "unable to set environment variable: %s", auth.ResourcePrincipalRegionEnvVar)
		}

		configurationProvider, err = auth.OkeWorkloadIdentityConfigurationProvider()
		if err != nil {
			return nil, errors.Wrapf(err, "unable to create OKE workload identity config provider")
		}
	default:
		return nil, fmt.Errorf("unsupported OCI provider: %s", provider)
	}

	client, err := objectstorage.NewObjectStorageClientWithConfigurationProvider(configurationProvider)
	if err != nil {
		return nil, errors.Wrapf(err, "unable to create ObjectStorage client with the given oci configurations")
	}
	var rt http.RoundTripper
	rt = CustomTransport(config)
	if config.HTTPConfig.Transport != nil {
		rt = config.HTTPConfig.Transport
	}
	if wrapRoundtripper != nil {
		rt = wrapRoundtripper(rt)
	}
	httpClient := http.Client{
		Transport: rt,
		Timeout:   config.HTTPConfig.ClientTimeout,
	}
	client.HTTPClient = &httpClient

	requestMetadata := getRequestMetadata(config.MaxRequestRetries, config.RequestRetryInterval)

	level.Info(logger).Log("msg", "getting namespace, it might take some time")
	namespace, err := getNamespace(client, requestMetadata)
	if err != nil {
		return nil, err
	}
	level.Debug(logger).Log("msg", fmt.Sprintf("Oracle Cloud Infrastructure tenancy namespace: %s", *namespace))

	bkt := Bucket{
		logger:          logger,
		name:            config.Bucket,
		namespace:       *namespace,
		client:          &client,
		partSize:        config.PartSize,
		requestMetadata: requestMetadata,
	}

	return &bkt, nil
}

// NewTestBucket creates test bkt client that before returning creates temporary bucket.
// In a close function it empties and deletes the bucket.
func NewTestBucket(t testing.TB) (objstore.Bucket, func(), error) {
	config, err := getConfigFromEnv()
	if err != nil {
		return nil, nil, err
	}

	ociConfig, err := yaml.Marshal(config)
	if err != nil {
		return nil, nil, err
	}

	bkt, err := NewBucket(log.NewNopLogger(), ociConfig, nil)
	if err != nil {
		return nil, nil, err
	}

	ctx := context.Background()
	bkt.name = objstore.CreateTemporaryTestBucketName(t)
	if err := bkt.createBucket(ctx, config.Compartment); err != nil {
		t.Errorf("failed to create temporary Oracle Cloud Infrastructure bucket '%s' for testing", bkt.name)
		return nil, nil, err
	}

	t.Logf("created temporary Oracle Cloud Infrastructure bucket '%s' for testing", bkt.name)
	return bkt, func() {
		objstore.EmptyBucket(t, ctx, bkt)
		if err := bkt.deleteBucket(ctx); err != nil {
			t.Logf("failed to delete temporary Oracle Cloud Infrastructure bucket %s for testing: %s", bkt.name, err)
		}
		t.Logf("deleted temporary Oracle Cloud Infrastructure bucket '%s' for testing", bkt.name)
	}, nil
}
```

## File: `providers/oci/oci_test.go`
```go
package oci

import (
	"testing"

	"github.com/efficientgo/core/testutil"
	"github.com/go-kit/log"
	"github.com/thanos-io/objstore/errutil"
	"gopkg.in/yaml.v2"
)

func TestNewBucketWithErrorRoundTripper(t *testing.T) {
	const mockPrivateKey = `-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQDCFENGw33yGihy92pDjZQhl0C36rPJj+CvfSC8+q28hxA161QF
NUd13wuCTUcq0Qd2qsBe/2hFyc2DCJJg0h1L78+6Z4UMR7EOcpfdUE9Hf3m/hs+F
UR45uBJeDK1HSFHD8bHKD6kv8FPGfJTotc+2xjJwoYi+1hqp1fIekaxsyQIDAQAB
AoGBAJR8ZkCUvx5kzv+utdl7T5MnordT1TvoXXJGXK7ZZ+UuvMNUCdN2QPc4sBiA
QWvLw1cSKt5DsKZ8UETpYPy8pPYnnDEz2dDYiaew9+xEpubyeW2oH4Zx71wqBtOK
kqwrXa/pzdpiucRRjk6vE6YY7EBBs/g7uanVpGibOVAEsqH1AkEA7DkjVH28WDUg
f1nqvfn2Kj6CT7nIcE3jGJsZZ7zlZmBmHFDONMLUrXR/Zm3pR5m0tCmBqa5RK95u
412jt1dPIwJBANJT3v8pnkth48bQo/fKel6uEYyboRtA5/uHuHkZ6FQF7OUkGogc
mSJluOdc5t6hI1VsLn0QZEjQZMEOWr+wKSMCQQCC4kXJEsHAve77oP6HtG/IiEn7
kpyUXRNvFsDE0czpJJBvL/aRFUJxuRK91jhjC68sA7NsKMGg5OXb5I5Jj36xAkEA
gIT7aFOYBFwGgQAQkWNKLvySgKbAZRTeLBacpHMuQdl1DfdntvAyqpAZ0lY0RKmW
G6aFKaqQfOXKCyWoUiVknQJAXrlgySFci/2ueKlIE1QqIiLSZ8V8OlpFLRnb1pzI
7U1yQXnTAEFYM560yJlzUpOb1V4cScGd365tiSMvxLOvTA==
-----END RSA PRIVATE KEY-----`

	config := DefaultConfig
	config.Provider = "raw"
	config.Tenancy = "test"
	config.User = "test"
	config.Region = "test"
	config.Fingerprint = "123"
	config.PrivateKey = mockPrivateKey
	config.Passphrase = "123"
	ociConfig, err := yaml.Marshal(config)
	testutil.Ok(t, err)

	_, err = NewBucket(log.NewNopLogger(), ociConfig, errutil.WrapWithErrRoundtripper)
	// We expect an error from the RoundTripper
	testutil.NotOk(t, err)
	testutil.Assert(t, errutil.IsMockedError(err), "Expected RoundTripper error, got: %v", err)
}
```

## File: `providers/oss/oss.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package oss

import (
	"context"
	"fmt"
	"io"
	"math"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"strings"
	"testing"
	"time"

	"github.com/aliyun/aliyun-oss-go-sdk/oss"
	alioss "github.com/aliyun/aliyun-oss-go-sdk/oss"
	"github.com/go-kit/log"
	"github.com/pkg/errors"
	"gopkg.in/yaml.v2"

	"github.com/thanos-io/objstore"
	"github.com/thanos-io/objstore/clientutil"
	"github.com/thanos-io/objstore/exthttp"
)

// PartSize is a part size for multi part upload.
const PartSize = 1024 * 1024 * 128

// Config stores the configuration for oss bucket.
type Config struct {
	Endpoint        string `yaml:"endpoint"`
	Bucket          string `yaml:"bucket"`
	AccessKeyID     string `yaml:"access_key_id"`
	AccessKeySecret string `yaml:"access_key_secret"`
}

// Bucket implements the store.Bucket interface.
type Bucket struct {
	name   string
	logger log.Logger
	client *alioss.Client
	config Config
	bucket *alioss.Bucket
}

func NewTestBucket(t testing.TB) (objstore.Bucket, func(), error) {
	c := Config{
		Endpoint:        os.Getenv("ALIYUNOSS_ENDPOINT"),
		Bucket:          os.Getenv("ALIYUNOSS_BUCKET"),
		AccessKeyID:     os.Getenv("ALIYUNOSS_ACCESS_KEY_ID"),
		AccessKeySecret: os.Getenv("ALIYUNOSS_ACCESS_KEY_SECRET"),
	}

	if c.Endpoint == "" || c.AccessKeyID == "" || c.AccessKeySecret == "" {
		return nil, nil, errors.New("aliyun oss endpoint or access_key_id or access_key_secret " +
			"is not present in config file")
	}
	if c.Bucket != "" && os.Getenv("THANOS_ALLOW_EXISTING_BUCKET_USE") == "true" {
		t.Log("ALIYUNOSS_BUCKET is defined. Normally this tests will create temporary bucket " +
			"and delete it after test. Unset ALIYUNOSS_BUCKET env variable to use default logic. If you really want to run " +
			"tests against provided (NOT USED!) bucket, set THANOS_ALLOW_EXISTING_BUCKET_USE=true.")
		return NewTestBucketFromConfig(t, c, true)
	}
	return NewTestBucketFromConfig(t, c, false)
}

func (b *Bucket) Provider() objstore.ObjProvider { return objstore.ALIYUNOSS }

// Upload the contents of the reader as an object into the bucket.
func (b *Bucket) Upload(_ context.Context, name string, r io.Reader, opts ...objstore.ObjectUploadOption) error {
	// TODO(https://github.com/thanos-io/thanos/issues/678): Remove guessing length when minio provider will support multipart upload without this.
	size, err := objstore.TryToGetSize(r)
	if err != nil {
		return errors.Wrapf(err, "failed to get size apriori to upload %s", name)
	}

	uploadOpts := objstore.ApplyObjectUploadOptions(opts...)

	chunksnum, lastslice := int(math.Floor(float64(size)/PartSize)), size%PartSize

	ncloser := io.NopCloser(r)
	switch chunksnum {
	case 0:
		if err := b.bucket.PutObject(name, ncloser, oss.ContentType(uploadOpts.ContentType)); err != nil {
			return errors.Wrap(err, "failed to upload oss object")
		}
	default:
		{
			init, err := b.bucket.InitiateMultipartUpload(name, oss.ContentType(uploadOpts.ContentType))
			if err != nil {
				return errors.Wrap(err, "failed to initiate multi-part upload")
			}
			chunk := 0
			uploadEveryPart := func(everypartsize int64, cnk int) (alioss.UploadPart, error) {
				prt, err := b.bucket.UploadPart(init, ncloser, everypartsize, cnk)
				if err != nil {
					if err := b.bucket.AbortMultipartUpload(init); err != nil {
						return prt, errors.Wrap(err, "failed to abort multi-part upload")
					}

					return prt, errors.Wrap(err, "failed to upload multi-part chunk")
				}
				return prt, nil
			}
			var parts []alioss.UploadPart
			for ; chunk < chunksnum; chunk++ {
				part, err := uploadEveryPart(PartSize, chunk+1)
				if err != nil {
					return errors.Wrap(err, "failed to upload every part")
				}
				parts = append(parts, part)
			}
			if lastslice != 0 {
				part, err := uploadEveryPart(lastslice, chunksnum+1)
				if err != nil {
					return errors.Wrap(err, "failed to upload the last chunk")
				}
				parts = append(parts, part)
			}
			if _, err := b.bucket.CompleteMultipartUpload(init, parts); err != nil {
				return errors.Wrap(err, "failed to set multi-part upload completive")
			}
		}
	}
	return nil
}

// Delete removes the object with the given name.
func (b *Bucket) Delete(ctx context.Context, name string) error {
	if err := b.bucket.DeleteObject(name); err != nil {
		return errors.Wrap(err, "delete oss object")
	}
	return nil
}

// Attributes returns information about the specified object.
func (b *Bucket) Attributes(ctx context.Context, name string) (objstore.ObjectAttributes, error) {
	m, err := b.bucket.GetObjectMeta(name)
	if err != nil {
		return objstore.ObjectAttributes{}, err
	}

	size, err := clientutil.ParseContentLength(m)
	if err != nil {
		return objstore.ObjectAttributes{}, err
	}

	// aliyun oss return Last-Modified header in RFC1123 format.
	// see api doc for details: https://www.alibabacloud.com/help/doc-detail/31985.htm
	mod, err := clientutil.ParseLastModified(m, time.RFC1123)
	if err != nil {
		return objstore.ObjectAttributes{}, err
	}

	return objstore.ObjectAttributes{
		Size:         size,
		LastModified: mod,
	}, nil
}

// NewBucket returns a new Bucket using the provided oss config values.
func NewBucket(logger log.Logger, conf []byte, component string, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Bucket, error) {
	var config Config
	if err := yaml.Unmarshal(conf, &config); err != nil {
		return nil, errors.Wrap(err, "parse aliyun oss config file failed")
	}
	return NewBucketWithConfig(logger, config, component, wrapRoundtripper)
}

// NewBucketWithConfig returns a new Bucket using the provided oss config struct.
func NewBucketWithConfig(logger log.Logger, config Config, component string, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Bucket, error) {
	if err := validate(config); err != nil {
		return nil, err
	}
	var clientOptions []alioss.ClientOption
	if wrapRoundtripper != nil {
		rt, err := exthttp.DefaultTransport(exthttp.DefaultHTTPConfig)
		if err != nil {
			return nil, err
		}
		clientOptions = append(clientOptions, func(client *alioss.Client) {
			client.HTTPClient = &http.Client{
				Transport: wrapRoundtripper(rt),
			}
		})
	}
	client, err := alioss.New(config.Endpoint, config.AccessKeyID, config.AccessKeySecret, clientOptions...)
	if err != nil {
		return nil, errors.Wrap(err, "create aliyun oss client failed")
	}
	bk, err := client.Bucket(config.Bucket)
	if err != nil {
		return nil, errors.Wrapf(err, "use aliyun oss bucket %s failed", config.Bucket)
	}

	bkt := &Bucket{
		logger: logger,
		client: client,
		name:   config.Bucket,
		config: config,
		bucket: bk,
	}
	return bkt, nil
}

// validate checks to see the config options are set.
func validate(config Config) error {
	if config.Endpoint == "" || config.Bucket == "" {
		return errors.New("aliyun oss endpoint or bucket is not present in config file")
	}
	if config.AccessKeyID == "" || config.AccessKeySecret == "" {
		return errors.New("aliyun oss access_key_id or access_key_secret is not present in config file")
	}

	return nil
}

func (b *Bucket) SupportedIterOptions() []objstore.IterOptionType {
	return []objstore.IterOptionType{objstore.Recursive}
}

// Iter calls f for each entry in the given directory. The argument to f is the full
// object name including the prefix of the inspected directory.
func (b *Bucket) Iter(ctx context.Context, dir string, f func(string) error, options ...objstore.IterOption) error {
	if dir != "" {
		dir = strings.TrimSuffix(dir, objstore.DirDelim) + objstore.DirDelim
	}

	delimiter := alioss.Delimiter(objstore.DirDelim)
	if objstore.ApplyIterOptions(options...).Recursive {
		delimiter = nil
	}

	marker := alioss.Marker("")
	for {
		if err := ctx.Err(); err != nil {
			return errors.Wrap(err, "context closed while iterating bucket")
		}
		objects, err := b.bucket.ListObjects(alioss.Prefix(dir), delimiter, marker)
		if err != nil {
			return errors.Wrap(err, "listing aliyun oss bucket failed")
		}
		marker = alioss.Marker(objects.NextMarker)

		for _, object := range objects.Objects {
			if err := f(object.Key); err != nil {
				return errors.Wrapf(err, "callback func invoke for object %s failed ", object.Key)
			}
		}

		for _, object := range objects.CommonPrefixes {
			if err := f(object); err != nil {
				return errors.Wrapf(err, "callback func invoke for directory %s failed", object)
			}
		}
		if !objects.IsTruncated {
			break
		}
	}

	return nil
}

func (b *Bucket) IterWithAttributes(ctx context.Context, dir string, f func(attrs objstore.IterObjectAttributes) error, options ...objstore.IterOption) error {
	if err := objstore.ValidateIterOptions(b.SupportedIterOptions(), options...); err != nil {
		return err
	}

	return b.Iter(ctx, dir, func(name string) error {
		return f(objstore.IterObjectAttributes{Name: name})
	}, options...)
}

func (b *Bucket) Name() string {
	return b.name
}

func NewTestBucketFromConfig(t testing.TB, c Config, reuseBucket bool) (objstore.Bucket, func(), error) {
	if c.Bucket == "" {
		src := rand.NewSource(time.Now().UnixNano())

		bktToCreate := strings.ReplaceAll(fmt.Sprintf("test_%s_%x", strings.ToLower(t.Name()), src.Int63()), "_", "-")
		if len(bktToCreate) >= 63 {
			bktToCreate = bktToCreate[:63]
		}
		testclient, err := alioss.New(c.Endpoint, c.AccessKeyID, c.AccessKeySecret)
		if err != nil {
			return nil, nil, errors.Wrap(err, "create aliyun oss client failed")
		}

		if err := testclient.CreateBucket(bktToCreate); err != nil {
			return nil, nil, errors.Wrapf(err, "create aliyun oss bucket %s failed", bktToCreate)
		}
		c.Bucket = bktToCreate
	}

	bc, err := yaml.Marshal(c)
	if err != nil {
		return nil, nil, err
	}

	b, err := NewBucket(log.NewNopLogger(), bc, "thanos-aliyun-oss-test", nil)
	if err != nil {
		return nil, nil, err
	}

	if reuseBucket {
		if err := b.Iter(context.Background(), "", func(_ string) error {
			return errors.Errorf("bucket %s is not empty", c.Bucket)
		}); err != nil {
			return nil, nil, errors.Wrapf(err, "oss check bucket %s", c.Bucket)
		}

		t.Log("WARNING. Reusing", c.Bucket, "Aliyun OSS bucket for OSS tests. Manual cleanup afterwards is required")
		return b, func() {}, nil
	}

	return b, func() {
		objstore.EmptyBucket(t, context.Background(), b)
		if err := b.client.DeleteBucket(c.Bucket); err != nil {
			t.Logf("deleting bucket %s failed: %s", c.Bucket, err)
		}
	}, nil
}

func (b *Bucket) Close() error { return nil }

func (b *Bucket) setRange(start, end int64, name string) (alioss.Option, error) {
	var opt alioss.Option
	if 0 <= start && start <= end {
		header, err := b.bucket.GetObjectMeta(name)
		if err != nil {
			return nil, err
		}

		size, err := strconv.ParseInt(header["Content-Length"][0], 10, 64)
		if err != nil {
			return nil, err
		}

		if end > size {
			end = size - 1
		}

		opt = alioss.Range(start, end)
	} else {
		return nil, errors.Errorf("Invalid range specified: start=%d end=%d", start, end)
	}
	return opt, nil
}

func (b *Bucket) getRange(_ context.Context, name string, off, length int64) (io.ReadCloser, error) {
	if name == "" {
		return nil, errors.New("given object name should not empty")
	}

	var opts []alioss.Option
	if length != -1 {
		opt, err := b.setRange(off, off+length-1, name)
		if err != nil {
			return nil, err
		}
		opts = append(opts, opt)
	}

	resp, err := b.bucket.DoGetObject(&oss.GetObjectRequest{ObjectKey: name}, opts)
	if err != nil {
		return nil, err
	}

	size, err := clientutil.ParseContentLength(resp.Response.Headers)
	if err == nil {
		return objstore.ObjectSizerReadCloser{
			ReadCloser: resp.Response,
			Size: func() (int64, error) {
				return size, nil
			},
		}, nil
	}

	return resp.Response, nil
}

// Get returns a reader for the given object name.
func (b *Bucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	return b.getRange(ctx, name, 0, -1)
}

func (b *Bucket) GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	return b.getRange(ctx, name, off, length)
}

// Exists checks if the given object exists in the bucket.
func (b *Bucket) Exists(ctx context.Context, name string) (bool, error) {
	exists, err := b.bucket.IsObjectExist(name)
	if err != nil {
		if b.IsObjNotFoundErr(err) {
			return false, nil
		}
		return false, errors.Wrap(err, "cloud not check if object exists")
	}

	return exists, nil
}

// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
func (b *Bucket) IsObjNotFoundErr(err error) bool {
	switch aliErr := errors.Cause(err).(type) {
	case alioss.ServiceError:
		if aliErr.StatusCode == http.StatusNotFound {
			return true
		}
	}
	return false
}

// IsAccessDeniedErr returns true if access to object is denied.
func (b *Bucket) IsAccessDeniedErr(err error) bool {
	switch aliErr := errors.Cause(err).(type) {
	case alioss.ServiceError:
		if aliErr.StatusCode == http.StatusForbidden {
			return true
		}
	}
	return false
}
```

## File: `providers/oss/oss_test.go`
```go
package oss

import (
	"context"
	"testing"

	"github.com/efficientgo/core/testutil"
	"github.com/go-kit/log"
	"github.com/thanos-io/objstore/errutil"
)

func TestNewBucketWithErrorRoundTripper(t *testing.T) {
	config := Config{
		Endpoint:        "http://test.com/",
		AccessKeyID:     "123",
		AccessKeySecret: "123",
		Bucket:          "test",
	}

	bkt, err := NewBucketWithConfig(log.NewNopLogger(), config, "test", errutil.WrapWithErrRoundtripper)
	// We expect an error from the RoundTripper
	testutil.Ok(t, err)
	_, err = bkt.Get(context.Background(), "test")
	testutil.NotOk(t, err)
	testutil.Assert(t, errutil.IsMockedError(err), "Expected RoundTripper error, got: %v", err)
}
```

## File: `providers/s3/s3.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

// Package s3 implements common object storage abstractions against s3-compatible APIs.
package s3

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"os"
	"runtime"
	"strconv"
	"strings"
	"testing"

	"github.com/efficientgo/core/logerrcapture"
	"github.com/go-kit/log"
	"github.com/go-kit/log/level"
	"github.com/minio/minio-go/v7"
	"github.com/minio/minio-go/v7/pkg/credentials"
	"github.com/minio/minio-go/v7/pkg/encrypt"
	"github.com/pkg/errors"
	"github.com/prometheus/common/version"
	"gopkg.in/yaml.v2"

	"github.com/thanos-io/objstore"
	"github.com/thanos-io/objstore/exthttp"
)

type ctxKey int

type BucketLookupType int

func (blt BucketLookupType) String() string {
	return []string{"auto", "virtual-hosted", "path"}[blt]
}

func (blt BucketLookupType) MinioType() minio.BucketLookupType {
	return []minio.BucketLookupType{
		minio.BucketLookupAuto,
		minio.BucketLookupDNS,
		minio.BucketLookupPath,
	}[blt]
}

func (blt BucketLookupType) MarshalYAML() (interface{}, error) {
	return blt.String(), nil
}

func (blt *BucketLookupType) UnmarshalYAML(unmarshal func(interface{}) error) error {
	var lookupType string
	if err := unmarshal(&lookupType); err != nil {
		return err
	}

	switch lookupType {
	case "auto":
		*blt = AutoLookup
		return nil
	case "virtual-hosted":
		*blt = VirtualHostLookup
		return nil
	case "path":
		*blt = PathLookup
		return nil
	}

	return fmt.Errorf("unsupported bucket lookup type: %s", lookupType)
}

const (
	AutoLookup BucketLookupType = iota
	VirtualHostLookup
	PathLookup

	// DirDelim is the delimiter used to model a directory structure in an object store bucket.
	DirDelim = "/"

	// SSEKMS is the name of the SSE-KMS method for objectstore encryption.
	SSEKMS = "SSE-KMS"

	// SSEC is the name of the SSE-C method for objstore encryption.
	SSEC = "SSE-C"

	// SSES3 is the name of the SSE-S3 method for objstore encryption.
	SSES3 = "SSE-S3"

	// sseConfigKey is the context key to override SSE config. This feature is used by downstream
	// projects (eg. Cortex) to inject custom SSE config on a per-request basis. Future work or
	// refactoring can introduce breaking changes as far as the functionality is preserved.
	// NOTE: we're using a context value only because it's a very specific S3 option. If SSE will
	// be available to wider set of backends we should probably add a variadic option to Get() and Upload().
	sseConfigKey = ctxKey(0)

	// Storage class header.
	amzStorageClass = "X-Amz-Storage-Class"
)

var DefaultConfig = Config{
	PutUserMetadata:  map[string]string{},
	HTTPConfig:       exthttp.DefaultHTTPConfig,
	DisableMultipart: false,
	PartSize:         1024 * 1024 * 64, // 64MB.
	BucketLookupType: AutoLookup,
	SendContentMd5:   true, // Default to using MD5.
}

// HTTPConfig exists here only because Cortex depends on it, and we depend on Cortex.
// Deprecated.
// TODO(bwplotka): Remove it, once we remove Cortex cycle dep, or Cortex stops using this.
type HTTPConfig = exthttp.HTTPConfig

// Config stores the configuration for s3 bucket.
type Config struct {
	Bucket             string             `yaml:"bucket"`
	Endpoint           string             `yaml:"endpoint"`
	Region             string             `yaml:"region"`
	DisableDualstack   bool               `yaml:"disable_dualstack"`
	AWSSDKAuth         bool               `yaml:"aws_sdk_auth"`
	AccessKey          string             `yaml:"access_key"`
	Insecure           bool               `yaml:"insecure"`
	SignatureV2        bool               `yaml:"signature_version2"`
	SecretKey          string             `yaml:"secret_key"`
	SessionToken       string             `yaml:"session_token"`
	PutUserMetadata    map[string]string  `yaml:"put_user_metadata"`
	HTTPConfig         exthttp.HTTPConfig `yaml:"http_config"`
	TraceConfig        TraceConfig        `yaml:"trace"`
	ListObjectsVersion string             `yaml:"list_objects_version"`
	BucketLookupType   BucketLookupType   `yaml:"bucket_lookup_type"`
	SendContentMd5     bool               `yaml:"send_content_md5"`
	DisableMultipart   bool               `yaml:"disable_multipart"`
	// PartSize used for multipart upload. Only used if uploaded object size is known and larger than configured PartSize.
	// NOTE we need to make sure this number does not produce more parts than 10 000.
	PartSize    uint64    `yaml:"part_size"`
	SSEConfig   SSEConfig `yaml:"sse_config"`
	STSEndpoint string    `yaml:"sts_endpoint"`
	MaxRetries  int       `yaml:"max_retries"`
}

// SSEConfig deals with the configuration of SSE for Minio. The following options are valid:
// KMSEncryptionContext == https://docs.aws.amazon.com/kms/latest/developerguide/services-s3.html#s3-encryption-context
type SSEConfig struct {
	Type                 string            `yaml:"type"`
	KMSKeyID             string            `yaml:"kms_key_id"`
	KMSEncryptionContext map[string]string `yaml:"kms_encryption_context"`
	EncryptionKey        string            `yaml:"encryption_key"`
}

type TraceConfig struct {
	Enable bool `yaml:"enable"`
}

// Bucket implements the store.Bucket interface against s3-compatible APIs.
type Bucket struct {
	logger           log.Logger
	name             string
	client           *minio.Client
	defaultSSE       encrypt.ServerSide
	putUserMetadata  map[string]string
	storageClass     string
	disableMultipart bool
	partSize         uint64
	listObjectsV1    bool
	sendContentMd5   bool
}

// parseConfig unmarshals a buffer into a Config with default values.
func parseConfig(conf []byte) (Config, error) {
	config := DefaultConfig
	if err := yaml.UnmarshalStrict(conf, &config); err != nil {
		return Config{}, err
	}

	return config, nil
}

// NewBucket returns a new Bucket using the provided s3 config values.
func NewBucket(logger log.Logger, conf []byte, component string, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Bucket, error) {
	config, err := parseConfig(conf)
	if err != nil {
		return nil, err
	}

	return NewBucketWithConfig(logger, config, component, wrapRoundtripper)
}

type overrideSignerType struct {
	credentials.Provider
	signerType credentials.SignatureType
}

func (s *overrideSignerType) Retrieve() (credentials.Value, error) {
	v, err := s.RetrieveWithCredContext(nil)
	if err != nil {
		return v, err
	}
	if !v.SignerType.IsAnonymous() {
		v.SignerType = s.signerType
	}
	return v, nil
}

// NewBucketWithConfig returns a new Bucket using the provided s3 config values.
func NewBucketWithConfig(logger log.Logger, config Config, component string, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Bucket, error) {
	var chain []credentials.Provider

	// TODO(bwplotka): Don't do flags as they won't scale, use actual params like v2, v4 instead
	wrapCredentialsProvider := func(p credentials.Provider) credentials.Provider { return p }
	if config.SignatureV2 {
		wrapCredentialsProvider = func(p credentials.Provider) credentials.Provider {
			return &overrideSignerType{Provider: p, signerType: credentials.SignatureV2}
		}
	}

	if err := validate(config); err != nil {
		return nil, err
	}

	if config.AWSSDKAuth {
		chain = []credentials.Provider{
			wrapCredentialsProvider(&AWSSDKAuth{Region: config.Region}),
		}
	} else if config.AccessKey != "" {
		chain = []credentials.Provider{wrapCredentialsProvider(&credentials.Static{
			Value: credentials.Value{
				AccessKeyID:     config.AccessKey,
				SecretAccessKey: config.SecretKey,
				SessionToken:    config.SessionToken,
				SignerType:      credentials.SignatureV4,
			},
		})}
	} else {
		chain = []credentials.Provider{
			wrapCredentialsProvider(&credentials.EnvAWS{}),
			wrapCredentialsProvider(&credentials.FileAWSCredentials{}),
			wrapCredentialsProvider(&credentials.IAM{
				Client: &http.Client{
					Transport: http.DefaultTransport,
				},
				Endpoint: config.STSEndpoint,
			}),
		}
	}

	// Check if a roundtripper has been set in the config
	// otherwise build the default transport.
	var tpt http.RoundTripper
	tpt, err := exthttp.DefaultTransport(config.HTTPConfig)
	if err != nil {
		return nil, err
	}
	if config.HTTPConfig.Transport != nil {
		tpt = config.HTTPConfig.Transport
	}
	if wrapRoundtripper != nil {
		tpt = wrapRoundtripper(tpt)
	}

	client, err := minio.New(config.Endpoint, &minio.Options{
		Creds:        credentials.NewChainCredentials(chain),
		Secure:       !config.Insecure,
		Region:       config.Region,
		Transport:    tpt,
		BucketLookup: config.BucketLookupType.MinioType(),
		MaxRetries:   config.MaxRetries,
	})
	if err != nil {
		return nil, errors.Wrap(err, "initialize s3 client")
	}
	client.SetAppInfo(fmt.Sprintf("thanos-%s", component), fmt.Sprintf("%s (%s)", version.Version, runtime.Version()))

	var sse encrypt.ServerSide
	if config.SSEConfig.Type != "" {
		switch config.SSEConfig.Type {
		case SSEKMS:
			// If the KMSEncryptionContext is a nil map the header that is
			// constructed by the encrypt.ServerSide object will be base64
			// encoded "nil" which is not accepted by AWS.
			if config.SSEConfig.KMSEncryptionContext == nil {
				config.SSEConfig.KMSEncryptionContext = make(map[string]string)
			}
			sse, err = encrypt.NewSSEKMS(config.SSEConfig.KMSKeyID, config.SSEConfig.KMSEncryptionContext)
			if err != nil {
				return nil, errors.Wrap(err, "initialize s3 client SSE-KMS")
			}

		case SSEC:
			key, err := os.ReadFile(config.SSEConfig.EncryptionKey)
			if err != nil {
				return nil, err
			}

			sse, err = encrypt.NewSSEC(key)
			if err != nil {
				return nil, errors.Wrap(err, "initialize s3 client SSE-C")
			}

		case SSES3:
			sse = encrypt.NewSSE()

		default:
			sseErrMsg := errors.Errorf("Unsupported type %q was provided. Supported types are SSE-S3, SSE-KMS, SSE-C", config.SSEConfig.Type)
			return nil, errors.Wrap(sseErrMsg, "Initialize s3 client SSE Config")
		}
	}

	if config.DisableDualstack {
		// The value in the config is inverted for backward compatibility
		client.SetS3EnableDualstack(false)
	}

	if config.TraceConfig.Enable {
		logWriter := log.NewStdlibAdapter(level.Debug(logger), log.MessageKey("s3TraceMsg"))
		client.TraceOn(logWriter)
	}

	if config.ListObjectsVersion != "" && config.ListObjectsVersion != "v1" && config.ListObjectsVersion != "v2" {
		return nil, errors.Errorf("Initialize s3 client list objects version: Unsupported version %q was provided. Supported values are v1, v2", config.ListObjectsVersion)
	}

	var storageClass string
	amzStorageClassLower := strings.ToLower(amzStorageClass)
	for k, v := range config.PutUserMetadata {
		if strings.ToLower(k) == amzStorageClassLower {
			delete(config.PutUserMetadata, k)
			storageClass = v
			break
		}
	}

	bkt := &Bucket{
		logger:           logger,
		name:             config.Bucket,
		client:           client,
		defaultSSE:       sse,
		putUserMetadata:  config.PutUserMetadata,
		storageClass:     storageClass,
		disableMultipart: config.DisableMultipart,
		partSize:         config.PartSize,
		listObjectsV1:    config.ListObjectsVersion == "v1",
		sendContentMd5:   config.SendContentMd5,
	}
	return bkt, nil
}

func (b *Bucket) Provider() objstore.ObjProvider { return objstore.S3 }

// Name returns the bucket name for s3.
func (b *Bucket) Name() string {
	return b.name
}

// validate checks to see the config options are set.
func validate(conf Config) error {
	if conf.Endpoint == "" {
		return errors.New("no s3 endpoint in config file")
	}

	if conf.AWSSDKAuth && conf.AccessKey != "" {
		return errors.New("aws_sdk_auth and access_key are mutually exclusive configurations")
	}

	if conf.AccessKey == "" && conf.SecretKey != "" {
		return errors.New("no s3 access_key specified while secret_key is present in config file; either both should be present in config or envvars/IAM should be used.")
	}

	if conf.AccessKey != "" && conf.SecretKey == "" {
		return errors.New("no s3 secret_key specified while access_key is present in config file; either both should be present in config or envvars/IAM should be used.")
	}

	if conf.SSEConfig.Type == SSEC && conf.SSEConfig.EncryptionKey == "" {
		return errors.New("encryption_key must be set if sse_config.type is set to 'SSE-C'")
	}

	if conf.SSEConfig.Type == SSEKMS && conf.SSEConfig.KMSKeyID == "" {
		return errors.New("kms_key_id must be set if sse_config.type is set to 'SSE-KMS'")
	}

	return nil
}

// ValidateForTests checks to see the config options for tests are set.
func ValidateForTests(conf Config) error {
	if conf.Endpoint == "" ||
		conf.AccessKey == "" ||
		conf.SecretKey == "" {
		return errors.New("insufficient s3 test configuration information")
	}
	return nil
}

func (b *Bucket) SupportedIterOptions() []objstore.IterOptionType {
	return []objstore.IterOptionType{objstore.Recursive, objstore.UpdatedAt}
}

func (b *Bucket) IterWithAttributes(ctx context.Context, dir string, f func(attrs objstore.IterObjectAttributes) error, options ...objstore.IterOption) error {
	if err := objstore.ValidateIterOptions(b.SupportedIterOptions(), options...); err != nil {
		return err
	}

	// Ensure the object name actually ends with a dir suffix. Otherwise we'll just iterate the
	// object itself as one prefix item.
	if dir != "" {
		dir = strings.TrimSuffix(dir, DirDelim) + DirDelim
	}

	appliedOpts := objstore.ApplyIterOptions(options...)

	opts := minio.ListObjectsOptions{
		Prefix:    dir,
		Recursive: appliedOpts.Recursive,
		UseV1:     b.listObjectsV1,
	}

	for object := range b.client.ListObjects(ctx, b.name, opts) {
		// Catch the error when failed to list objects.
		if object.Err != nil {
			return object.Err
		}
		// This sometimes happens with empty buckets.
		if object.Key == "" {
			continue
		}
		// The s3 client can also return the directory itself in the ListObjects call above.
		if object.Key == dir {
			continue
		}

		attr := objstore.IterObjectAttributes{
			Name: object.Key,
		}
		if appliedOpts.LastModified {
			attr.SetLastModified(object.LastModified)
		}

		if err := f(attr); err != nil {
			return err
		}
	}

	return ctx.Err()
}

func (b *Bucket) Iter(ctx context.Context, dir string, f func(string) error, opts ...objstore.IterOption) error {
	// Only include recursive option since attributes are not used in this method.
	var filteredOpts []objstore.IterOption
	for _, opt := range opts {
		if opt.Type == objstore.Recursive {
			filteredOpts = append(filteredOpts, opt)
			break
		}
	}

	return b.IterWithAttributes(ctx, dir, func(attrs objstore.IterObjectAttributes) error {
		return f(attrs.Name)
	}, filteredOpts...)
}

func (b *Bucket) getRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	sse, err := b.getServerSideEncryption(ctx)
	if err != nil {
		return nil, err
	}

	opts := &minio.GetObjectOptions{ServerSideEncryption: sse}
	if length != -1 {
		if err := opts.SetRange(off, off+length-1); err != nil {
			return nil, err
		}
	} else if off > 0 {
		if err := opts.SetRange(off, 0); err != nil {
			return nil, err
		}
	}
	r, err := b.client.GetObject(ctx, b.name, name, *opts)
	if err != nil {
		return nil, err
	}

	// NotFoundObject error is revealed only after first Read. This does the initial GetRequest. Prefetch this here
	// for convenience.
	if _, err := r.Read(nil); err != nil {
		defer logerrcapture.Do(b.logger, r.Close, "s3 get range obj close")

		// First GET Object request error.
		return nil, err
	}

	return objstore.ObjectSizerReadCloser{
		ReadCloser: r,
		Size: func() (int64, error) {
			stat, err := r.Stat()
			if err != nil {
				return 0, err
			}

			return stat.Size, nil
		},
	}, nil
}

// Get returns a reader for the given object name.
func (b *Bucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	return b.getRange(ctx, name, 0, -1)
}

// GetRange returns a new range reader for the given object name and range.
func (b *Bucket) GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	return b.getRange(ctx, name, off, length)
}

// Exists checks if the given object exists.
func (b *Bucket) Exists(ctx context.Context, name string) (bool, error) {
	sse, err := b.getServerSideEncryption(ctx)
	if err != nil {
		return false, err
	}

	_, err = b.client.StatObject(ctx, b.name, name, minio.StatObjectOptions{
		ServerSideEncryption: sse,
	})
	if err != nil {
		if b.IsObjNotFoundErr(err) {
			return false, nil
		}
		return false, errors.Wrap(err, "stat s3 object")
	}

	return true, nil
}

// Upload the contents of the reader as an object into the bucket.
func (b *Bucket) Upload(ctx context.Context, name string, r io.Reader, opts ...objstore.ObjectUploadOption) error {
	sse, err := b.getServerSideEncryption(ctx)
	if err != nil {
		return err
	}

	// TODO(https://github.com/thanos-io/thanos/issues/678): Remove guessing length when minio provider will support multipart upload without this.
	size, err := objstore.TryToGetSize(r)
	if err != nil {
		level.Warn(b.logger).Log("msg", "could not guess file size for multipart upload; upload might be not optimized", "name", name, "err", err)
		size = -1
	}

	partSize := b.partSize
	if size < int64(partSize) {
		partSize = 0
	}

	// Cloning map since minio may modify it
	userMetadata := make(map[string]string, len(b.putUserMetadata))
	for k, v := range b.putUserMetadata {
		userMetadata[k] = v
	}

	uploadOpts := objstore.ApplyObjectUploadOptions(opts...)

	if _, err := b.client.PutObject(
		ctx,
		b.name,
		name,
		r,
		size,
		minio.PutObjectOptions{
			DisableMultipart:     b.disableMultipart,
			PartSize:             partSize,
			ServerSideEncryption: sse,
			UserMetadata:         userMetadata,
			StorageClass:         b.storageClass,
			SendContentMd5:       b.sendContentMd5,
			// 4 is what minio-go have as the default. To be certain we do micro benchmark before any changes we
			// ensure we pin this number to four.
			// TODO(bwplotka): Consider adjusting this number to GOMAXPROCS or to expose this in config if it becomes bottleneck.
			NumThreads:  4,
			ContentType: uploadOpts.ContentType,
		},
	); err != nil {
		return errors.Wrap(err, "upload s3 object")
	}

	return nil
}

// Attributes returns information about the specified object.
func (b *Bucket) Attributes(ctx context.Context, name string) (objstore.ObjectAttributes, error) {
	sse, err := b.getServerSideEncryption(ctx)
	if err != nil {
		return objstore.ObjectAttributes{}, err
	}

	objInfo, err := b.client.StatObject(ctx, b.name, name, minio.StatObjectOptions{
		ServerSideEncryption: sse,
	})
	if err != nil {
		return objstore.ObjectAttributes{}, err
	}

	return objstore.ObjectAttributes{
		Size:         objInfo.Size,
		LastModified: objInfo.LastModified,
	}, nil
}

// Delete removes the object with the given name.
func (b *Bucket) Delete(ctx context.Context, name string) error {
	return b.client.RemoveObject(ctx, b.name, name, minio.RemoveObjectOptions{})
}

// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
func (b *Bucket) IsObjNotFoundErr(err error) bool {
	return minio.ToErrorResponse(errors.Cause(err)).Code == "NoSuchKey"
}

// IsAccessDeniedErr returns true if access to object is denied.
func (b *Bucket) IsAccessDeniedErr(err error) bool {
	return minio.ToErrorResponse(errors.Cause(err)).Code == "AccessDenied"
}

func (b *Bucket) Close() error { return nil }

// getServerSideEncryption returns the SSE to use.
func (b *Bucket) getServerSideEncryption(ctx context.Context) (encrypt.ServerSide, error) {
	if value := ctx.Value(sseConfigKey); value != nil {
		if sse, ok := value.(encrypt.ServerSide); ok {
			return sse, nil
		}
		return nil, errors.New("invalid SSE config override provided in the context")
	}

	return b.defaultSSE, nil
}

func configFromEnv() Config {
	c := Config{
		Bucket:       os.Getenv("S3_BUCKET"),
		Endpoint:     os.Getenv("S3_ENDPOINT"),
		AccessKey:    os.Getenv("S3_ACCESS_KEY"),
		SecretKey:    os.Getenv("S3_SECRET_KEY"),
		SessionToken: os.Getenv("S3_SESSION_TOKEN"),
	}

	c.Insecure, _ = strconv.ParseBool(os.Getenv("S3_INSECURE"))
	c.HTTPConfig.InsecureSkipVerify, _ = strconv.ParseBool(os.Getenv("S3_INSECURE_SKIP_VERIFY"))
	c.SignatureV2, _ = strconv.ParseBool(os.Getenv("S3_SIGNATURE_VERSION2"))
	return c
}

// NewTestBucket creates test bkt client that before returning creates temporary bucket.
// In a close function it empties and deletes the bucket.
func NewTestBucket(t testing.TB, location string) (objstore.Bucket, func(), error) {
	c := configFromEnv()
	if err := ValidateForTests(c); err != nil {
		return nil, nil, err
	}

	if c.Bucket != "" && os.Getenv("THANOS_ALLOW_EXISTING_BUCKET_USE") == "" {
		return nil, nil, errors.New("S3_BUCKET is defined. Normally this tests will create temporary bucket " +
			"and delete it after test. Unset S3_BUCKET env variable to use default logic. If you really want to run " +
			"tests against provided (NOT USED!) bucket, set THANOS_ALLOW_EXISTING_BUCKET_USE=true. WARNING: That bucket " +
			"needs to be manually cleared. This means that it is only useful to run one test in a time. This is due " +
			"to safety (accidentally pointing prod bucket for test) as well as aws s3 not being fully strong consistent.")
	}

	return NewTestBucketFromConfig(t, location, c, true)
}

func NewTestBucketFromConfig(t testing.TB, location string, c Config, reuseBucket bool) (objstore.Bucket, func(), error) {
	ctx := context.Background()

	bc, err := yaml.Marshal(c)
	if err != nil {
		return nil, nil, err
	}
	b, err := NewBucket(log.NewNopLogger(), bc, "thanos-e2e-test", nil)
	if err != nil {
		return nil, nil, err
	}

	bktToCreate := c.Bucket
	if c.Bucket != "" && reuseBucket {
		if err := b.Iter(ctx, "", func(string) error {
			return errors.Errorf("bucket %s is not empty", c.Bucket)
		}); err != nil {
			return nil, nil, errors.Wrapf(err, "s3 check bucket %s", c.Bucket)
		}

		t.Log("WARNING. Reusing", c.Bucket, "AWS bucket for AWS tests. Manual cleanup afterwards is required")
		return b, func() {}, nil
	}

	if c.Bucket == "" {
		bktToCreate = objstore.CreateTemporaryTestBucketName(t)
	}

	if err := b.client.MakeBucket(ctx, bktToCreate, minio.MakeBucketOptions{Region: location}); err != nil {
		return nil, nil, err
	}
	b.name = bktToCreate
	t.Log("created temporary AWS bucket for AWS tests with name", bktToCreate, "in", location)

	return b, func() {
		objstore.EmptyBucket(t, ctx, b)
		if err := b.client.RemoveBucket(ctx, bktToCreate); err != nil {
			t.Logf("deleting bucket %s failed: %s", bktToCreate, err)
		}
	}, nil
}

// ContextWithSSEConfig returns a context with a  custom SSE config set. The returned context should be
// provided to S3 objstore client functions to override the default SSE config.
func ContextWithSSEConfig(ctx context.Context, value encrypt.ServerSide) context.Context {
	return context.WithValue(ctx, sseConfigKey, value)
}
```

## File: `providers/s3/s3_aws_sdk_auth.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package s3

import (
	"context"

	aws "github.com/aws/aws-sdk-go-v2/aws"
	awsconfig "github.com/aws/aws-sdk-go-v2/config"
	"github.com/minio/minio-go/v7/pkg/credentials"
	"github.com/pkg/errors"
)

// AWSSDKAuth retrieves credentials from the aws-sdk-go.
type AWSSDKAuth struct {
	Region string
	creds  aws.Credentials
}

// NewAWSSDKAuth returns a pointer to a new Credentials object
// wrapping the environment variable provider.
func NewAWSSDKAuth(region string) *credentials.Credentials {
	return credentials.New(&AWSSDKAuth{
		Region: region,
	})
}

func (a *AWSSDKAuth) RetrieveWithCredContext(cc *credentials.CredContext) (credentials.Value, error) {
	cfg, err := awsconfig.LoadDefaultConfig(context.TODO(), awsconfig.WithRegion(a.Region))
	if err != nil {
		return credentials.Value{}, errors.Wrap(err, "load AWS SDK config")
	}

	creds, err := cfg.Credentials.Retrieve(context.TODO())
	if err != nil {
		return credentials.Value{}, errors.Wrap(err, "retrieve AWS SDK credentials")
	}

	a.creds = creds

	return credentials.Value{
		AccessKeyID:     creds.AccessKeyID,
		SecretAccessKey: creds.SecretAccessKey,
		SessionToken:    creds.SessionToken,
		SignerType:      credentials.SignatureV4,
	}, nil
}

// Retrieve retrieves the keys from the environment.
func (a *AWSSDKAuth) Retrieve() (credentials.Value, error) {
	return a.RetrieveWithCredContext(nil)
}

// IsExpired returns if the credentials have been retrieved.
func (a *AWSSDKAuth) IsExpired() bool {
	return a.creds.Expired()
}
```

## File: `providers/s3/s3_e2e_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package s3_test

import (
	"bytes"
	"context"
	"io"
	"path/filepath"
	"strings"
	"testing"

	"github.com/efficientgo/core/testutil"
	"github.com/efficientgo/e2e"
	e2edb "github.com/efficientgo/e2e/db"
	"github.com/go-kit/log"
	"github.com/minio/minio-go/v7/pkg/encrypt"

	"github.com/thanos-io/objstore/exthttp"
	"github.com/thanos-io/objstore/providers/s3"
	"github.com/thanos-io/objstore/test/e2e/e2ethanos"
)

// Regression benchmark for https://github.com/thanos-io/thanos/issues/3917 and https://github.com/thanos-io/thanos/issues/3967.
//
//	$ export ver=v1 && go test ./pkg/objstore/s3/... -run '^$' -bench '^BenchmarkUpload' -benchtime 5s -count 5 \
//		-memprofile=${ver}.mem.pprof -cpuprofile=${ver}.cpu.pprof | tee ${ver}.txt .
func BenchmarkUpload(b *testing.B) {
	b.ReportAllocs()
	ctx := context.Background()

	e, err := e2e.NewDockerEnvironment("e2e_bench_mino_client", e2e.WithLogger(log.NewNopLogger()))
	testutil.Ok(b, err)
	b.Cleanup(e2ethanos.CleanScenario(b, e))

	const bucket = "benchmark"
	m := e2ethanos.NewMinio(e, "benchmark", bucket)
	testutil.Ok(b, e2e.StartAndWaitReady(m))

	bkt, err := s3.NewBucketWithConfig(
		log.NewNopLogger(),
		e2ethanos.NewS3Config(bucket, m.Endpoint("https"), m.Dir()),
		"test-feed",
		nil,
	)
	testutil.Ok(b, err)

	buf := bytes.Buffer{}
	buf.Grow(1028 * 1028 * 100) // 100MB.
	word := "abcdefghij"
	for i := 0; i < buf.Cap()/len(word); i++ {
		_, _ = buf.WriteString(word)
	}
	str := buf.String()

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		testutil.Ok(b, bkt.Upload(ctx, "test", strings.NewReader(str)))
	}
}

func TestSSECencryption(t *testing.T) {
	ctx := context.Background()
	e, err := e2e.NewDockerEnvironment("e2e-ssec", e2e.WithLogger(log.NewNopLogger()))
	testutil.Ok(t, err)
	t.Cleanup(e2ethanos.CleanScenario(t, e))

	const bucket = "sse-c-encryption"
	m := e2ethanos.NewMinio(e, "sse-c-encryption", bucket)
	testutil.Ok(t, e2e.StartAndWaitReady(m))

	cfg := s3.Config{
		Bucket:    bucket,
		AccessKey: e2edb.MinioAccessKey,
		SecretKey: e2edb.MinioSecretKey,
		Endpoint:  m.Endpoint("https"),
		Insecure:  false,
		HTTPConfig: exthttp.HTTPConfig{
			TLSConfig: exthttp.TLSConfig{
				CAFile:   filepath.Join(m.Dir(), "certs", "CAs", "ca.crt"),
				CertFile: filepath.Join(m.Dir(), "certs", "public.crt"),
				KeyFile:  filepath.Join(m.Dir(), "certs", "private.key"),
			},
		},
		SSEConfig: s3.SSEConfig{
			Type:          string(encrypt.SSEC),
			EncryptionKey: "testdata/encryption_key",
		},
		BucketLookupType: s3.AutoLookup,
	}

	bkt, err := s3.NewBucketWithConfig(
		log.NewNopLogger(),
		cfg,
		"test-ssec",
		nil,
	)
	testutil.Ok(t, err)

	upload := "secret content"
	testutil.Ok(t, bkt.Upload(ctx, "encrypted", strings.NewReader(upload)))

	exists, err := bkt.Exists(ctx, "encrypted")
	testutil.Ok(t, err)
	if !exists {
		t.Fatalf("upload failed")
	}

	r, err := bkt.Get(ctx, "encrypted")
	testutil.Ok(t, err)
	b, err := io.ReadAll(r)
	testutil.Ok(t, err)
	testutil.Equals(t, upload, string(b))
}
```

## File: `providers/s3/s3_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package s3

import (
	"context"
	"encoding/base64"
	"encoding/json"
	"io"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"

	"github.com/efficientgo/core/testutil"
	"github.com/go-kit/log"
	"github.com/minio/minio-go/v7/pkg/encrypt"

	"github.com/thanos-io/objstore/errutil"
	"github.com/thanos-io/objstore/exthttp"
)

const endpoint string = "localhost:80"

func TestParseConfig(t *testing.T) {
	input := []byte(`bucket: abcd
insecure: false`)
	cfg, err := parseConfig(input)
	testutil.Ok(t, err)

	if cfg.Bucket != "abcd" {
		t.Errorf("parsing of bucket failed: got %v, expected %v", cfg.Bucket, "abcd")
	}
	if cfg.Insecure {
		t.Errorf("parsing of insecure failed: got %v, expected %v", cfg.Insecure, false)
	}
}

func TestParseConfig_SSEConfig(t *testing.T) {
	input := []byte(`bucket: abdd
endpoint: "s3-endpoint"
sse_config:
  type: SSE-S3`)

	cfg, err := parseConfig(input)
	testutil.Ok(t, err)
	testutil.Ok(t, validate(cfg))

	input2 := []byte(`bucket: abdd
endpoint: "s3-endpoint"
sse_config:
  type: SSE-C`)

	cfg, err = parseConfig(input2)
	testutil.Ok(t, err)
	testutil.NotOk(t, validate(cfg))

	input3 := []byte(`bucket: abdd
endpoint: "s3-endpoint"
sse_config:
  type: SSE-C
  kms_key_id: qweasd`)

	cfg, err = parseConfig(input3)
	testutil.Ok(t, err)
	testutil.NotOk(t, validate(cfg))

	input4 := []byte(`bucket: abdd
endpoint: "s3-endpoint"
sse_config:
  type: SSE-C
  encryption_key: /some/file`)

	cfg, err = parseConfig(input4)
	testutil.Ok(t, err)
	testutil.Ok(t, validate(cfg))

	input5 := []byte(`bucket: abdd
endpoint: "s3-endpoint"
sse_config:
  type: SSE-KMS`)

	cfg, err = parseConfig(input5)
	testutil.Ok(t, err)
	testutil.NotOk(t, validate(cfg))

	input6 := []byte(`bucket: abdd
endpoint: "s3-endpoint"
sse_config:
  type: SSE-KMS
  kms_key_id: abcd1234-ab12-cd34-1234567890ab`)

	cfg, err = parseConfig(input6)
	testutil.Ok(t, err)
	testutil.Ok(t, validate(cfg))

	input7 := []byte(`bucket: abdd
endpoint: "s3-endpoint"
sse_config:
  type: SSE-KMS
  kms_key_id: abcd1234-ab12-cd34-1234567890ab
  kms_encryption_context:
    key: value
    something: else
    a: b`)

	cfg, err = parseConfig(input7)
	testutil.Ok(t, err)
	testutil.Ok(t, validate(cfg))

	input8 := []byte(`bucket: abdd
endpoint: "s3-endpoint"
sse_config:
  type: SSE-MagicKey
  kms_key_id: abcd1234-ab12-cd34-1234567890ab
  encryption_key: /some/file`)

	cfg, err = parseConfig(input8)
	testutil.Ok(t, err)
	// Since the error handling for "proper type" if done as we're setting up the bucket.
	testutil.Ok(t, validate(cfg))
}

func TestParseConfig_DefaultHTTPConfig(t *testing.T) {
	input := []byte(`bucket: abcd
insecure: false`)
	cfg, err := parseConfig(input)
	testutil.Ok(t, err)

	if time.Duration(cfg.HTTPConfig.IdleConnTimeout) != time.Duration(90*time.Second) {
		t.Errorf("parsing of idle_conn_timeout failed: got %v, expected %v",
			time.Duration(cfg.HTTPConfig.IdleConnTimeout), time.Duration(90*time.Second))
	}

	if time.Duration(cfg.HTTPConfig.ResponseHeaderTimeout) != time.Duration(2*time.Minute) {
		t.Errorf("parsing of response_header_timeout failed: got %v, expected %v",
			time.Duration(cfg.HTTPConfig.IdleConnTimeout), time.Duration(2*time.Minute))
	}

	if cfg.HTTPConfig.InsecureSkipVerify {
		t.Errorf("parsing of insecure_skip_verify failed: got %v, expected %v", cfg.HTTPConfig.InsecureSkipVerify, false)
	}
}

func TestParseConfig_CustomHTTPConfig(t *testing.T) {
	input := []byte(`bucket: abcd
insecure: false
http_config:
  insecure_skip_verify: true
  idle_conn_timeout: 50s
  response_header_timeout: 1m`)
	cfg, err := parseConfig(input)
	testutil.Ok(t, err)

	if time.Duration(cfg.HTTPConfig.IdleConnTimeout) != time.Duration(50*time.Second) {
		t.Errorf("parsing of idle_conn_timeout failed: got %v, expected %v",
			time.Duration(cfg.HTTPConfig.IdleConnTimeout), time.Duration(50*time.Second))
	}

	if time.Duration(cfg.HTTPConfig.ResponseHeaderTimeout) != time.Duration(1*time.Minute) {
		t.Errorf("parsing of response_header_timeout failed: got %v, expected %v",
			time.Duration(cfg.HTTPConfig.IdleConnTimeout), time.Duration(1*time.Minute))
	}

	if !cfg.HTTPConfig.InsecureSkipVerify {
		t.Errorf("parsing of insecure_skip_verify failed: got %v, expected %v", cfg.HTTPConfig.InsecureSkipVerify, false)
	}
}

func TestParseConfig_CustomHTTPConfigWithTLS(t *testing.T) {
	input := []byte(`bucket: abcd
insecure: false
http_config:
  tls_config:
    ca_file: /certs/ca.crt
    cert_file: /certs/cert.crt
    key_file: /certs/key.key
    server_name: server
    insecure_skip_verify: false
  `)
	cfg, err := parseConfig(input)
	testutil.Ok(t, err)

	testutil.Equals(t, "/certs/ca.crt", cfg.HTTPConfig.TLSConfig.CAFile)
	testutil.Equals(t, "/certs/cert.crt", cfg.HTTPConfig.TLSConfig.CertFile)
	testutil.Equals(t, "/certs/key.key", cfg.HTTPConfig.TLSConfig.KeyFile)
	testutil.Equals(t, "server", cfg.HTTPConfig.TLSConfig.ServerName)
	testutil.Equals(t, false, cfg.HTTPConfig.TLSConfig.InsecureSkipVerify)
}

func TestParseConfig_CustomLegacyInsecureSkipVerify(t *testing.T) {
	input := []byte(`bucket: abcd
insecure: false
http_config:
  insecure_skip_verify: true
  tls_config:
    insecure_skip_verify: false
  `)
	cfg, err := parseConfig(input)
	testutil.Ok(t, err)
	transport, err := exthttp.DefaultTransport(cfg.HTTPConfig)
	testutil.Ok(t, err)
	testutil.Equals(t, true, transport.TLSClientConfig.InsecureSkipVerify)
}

func TestValidate_OK(t *testing.T) {
	input := []byte(`bucket: "bucket-name"
endpoint: "s3-endpoint"
access_key: "access_key"
insecure: false
signature_version2: false
secret_key: "secret_key"
http_config:
  insecure_skip_verify: false
  idle_conn_timeout: 50s`)
	cfg, err := parseConfig(input)
	testutil.Ok(t, err)
	testutil.Ok(t, validate(cfg))
	testutil.Assert(t, cfg.PutUserMetadata != nil, "map should not be nil")

	input2 := []byte(`bucket: "bucket-name"
endpoint: "s3-endpoint"
access_key: "access_key"
insecure: false
signature_version2: false
secret_key: "secret_key"
put_user_metadata:
  "X-Amz-Acl": "bucket-owner-full-control"
http_config:
  idle_conn_timeout: 0s`)
	cfg2, err := parseConfig(input2)
	testutil.Ok(t, err)
	testutil.Ok(t, validate(cfg2))

	testutil.Equals(t, "bucket-owner-full-control", cfg2.PutUserMetadata["X-Amz-Acl"])

	input3 := []byte(`bucket: "bucket-name"
endpoint: "s3-endpoint"
access_key: "access_key"
insecure: false
signature_version2: false
secret_key: "secret_key"
session_token: "session_token"
http_config:
  idle_conn_timeout: 0s`)
	cfg3, err := parseConfig(input3)
	testutil.Ok(t, err)
	testutil.Ok(t, validate(cfg3))

	testutil.Equals(t, "session_token", cfg3.SessionToken)
}

func TestParseConfig_PartSize(t *testing.T) {
	input := []byte(`bucket: "bucket-name"
endpoint: "s3-endpoint"
access_key: "access_key"
insecure: false
signature_version2: false
secret_key: "secret_key"
http_config:
  insecure_skip_verify: false
  idle_conn_timeout: 50s`)

	cfg, err := parseConfig(input)
	testutil.Ok(t, err)
	testutil.Assert(t, cfg.PartSize == 1024*1024*64, "when part size not set it should default to 128MiB")

	input2 := []byte(`bucket: "bucket-name"
endpoint: "s3-endpoint"
access_key: "access_key"
insecure: false
signature_version2: false
secret_key: "secret_key"
part_size: 104857600
http_config:
  insecure_skip_verify: false
  idle_conn_timeout: 50s`)
	cfg2, err := parseConfig(input2)
	testutil.Ok(t, err)
	testutil.Assert(t, cfg2.PartSize == 1024*1024*100, "when part size should be set to 100MiB")
}

func TestParseConfig_OldSEEncryptionFieldShouldFail(t *testing.T) {
	input := []byte(`bucket: "bucket-name"
endpoint: "s3-endpoint"
access_key: "access_key"
insecure: false
signature_version2: false
encrypt_sse: false
secret_key: "secret_key"
see_encryption: true
put_user_metadata:
  "X-Amz-Acl": "bucket-owner-full-control"
http_config:
  idle_conn_timeout: 0s`)
	_, err := parseConfig(input)
	testutil.NotOk(t, err)
}

func TestParseConfig_ListObjectsV1(t *testing.T) {
	input := []byte(`bucket: "bucket-name"
endpoint: "s3-endpoint"`)

	cfg, err := parseConfig(input)
	testutil.Ok(t, err)

	if cfg.ListObjectsVersion != "" {
		t.Errorf("when list_objects_version not set, it should default to empty")
	}

	input2 := []byte(`bucket: "bucket-name"
endpoint: "s3-endpoint"
list_objects_version: "abcd"`)

	cfg2, err := parseConfig(input2)
	testutil.Ok(t, err)

	if cfg2.ListObjectsVersion != "abcd" {
		t.Errorf("parsing of list_objects_version failed: got %v, expected %v", cfg.ListObjectsVersion, "abcd")
	}
}

func TestBucket_getServerSideEncryption(t *testing.T) {
	// Default config should return no SSE config.
	cfg := DefaultConfig
	cfg.Endpoint = endpoint
	bkt, err := NewBucketWithConfig(log.NewNopLogger(), cfg, "test", nil)
	testutil.Ok(t, err)

	sse, err := bkt.getServerSideEncryption(context.Background())
	testutil.Ok(t, err)
	testutil.Equals(t, nil, sse)

	// If SSE is configured in the client config it should be used.
	cfg = DefaultConfig
	cfg.Endpoint = endpoint
	cfg.SSEConfig = SSEConfig{Type: SSES3}
	bkt, err = NewBucketWithConfig(log.NewNopLogger(), cfg, "test", nil)
	testutil.Ok(t, err)

	sse, err = bkt.getServerSideEncryption(context.Background())
	testutil.Ok(t, err)
	testutil.Equals(t, encrypt.S3, sse.Type())

	// SSE-KMS can be configured in the client config with an optional
	// KMSEncryptionContext - In this case the encryptionContextHeader should be
	// a base64 encoded string which represents a string-string map "{}"
	cfg = DefaultConfig
	cfg.Endpoint = endpoint
	cfg.SSEConfig = SSEConfig{
		Type:     SSEKMS,
		KMSKeyID: "key",
	}
	bkt, err = NewBucketWithConfig(log.NewNopLogger(), cfg, "test", nil)
	testutil.Ok(t, err)

	sse, err = bkt.getServerSideEncryption(context.Background())
	testutil.Ok(t, err)
	testutil.Equals(t, encrypt.KMS, sse.Type())

	encryptionContextHeader := "X-Amz-Server-Side-Encryption-Context"
	headers := make(http.Header)
	sse.Marshal(headers)
	wantJson, err := json.Marshal(make(map[string]string))
	testutil.Ok(t, err)
	want := base64.StdEncoding.EncodeToString(wantJson)
	testutil.Equals(t, want, headers.Get(encryptionContextHeader))

	// If the KMSEncryptionContext is set then the header should reflect it's
	// value.
	cfg = DefaultConfig
	cfg.Endpoint = endpoint
	cfg.SSEConfig = SSEConfig{
		Type:                 SSEKMS,
		KMSKeyID:             "key",
		KMSEncryptionContext: map[string]string{"foo": "bar"},
	}
	bkt, err = NewBucketWithConfig(log.NewNopLogger(), cfg, "test", nil)
	testutil.Ok(t, err)

	sse, err = bkt.getServerSideEncryption(context.Background())
	testutil.Ok(t, err)
	testutil.Equals(t, encrypt.KMS, sse.Type())

	headers = make(http.Header)
	sse.Marshal(headers)
	wantJson, err = json.Marshal(cfg.SSEConfig.KMSEncryptionContext)
	testutil.Ok(t, err)
	want = base64.StdEncoding.EncodeToString(wantJson)
	testutil.Equals(t, want, headers.Get(encryptionContextHeader))

	// If SSE is configured in the context it should win.
	cfg = DefaultConfig
	cfg.Endpoint = endpoint
	cfg.SSEConfig = SSEConfig{Type: SSES3}
	override, err := encrypt.NewSSEKMS("test", nil)
	testutil.Ok(t, err)

	bkt, err = NewBucketWithConfig(log.NewNopLogger(), cfg, "test", nil)
	testutil.Ok(t, err)

	sse, err = bkt.getServerSideEncryption(context.WithValue(context.Background(), sseConfigKey, override))
	testutil.Ok(t, err)
	testutil.Equals(t, encrypt.KMS, sse.Type())
}

func TestBucket_Get_ShouldReturnErrorIfServerTruncateResponse(t *testing.T) {
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Last-Modified", "Wed, 21 Oct 2015 07:28:00 GMT")
		w.Header().Set("Content-Length", "100")

		// Write less bytes than the content length.
		_, err := w.Write([]byte("12345"))
		testutil.Ok(t, err)
	}))
	defer srv.Close()

	cfg := DefaultConfig
	cfg.Bucket = "test-bucket"
	cfg.Endpoint = srv.Listener.Addr().String()
	cfg.Insecure = true
	cfg.Region = "test"
	cfg.AccessKey = "test"
	cfg.SecretKey = "test"

	bkt, err := NewBucketWithConfig(log.NewNopLogger(), cfg, "test", nil)
	testutil.Ok(t, err)

	reader, err := bkt.Get(context.Background(), "test")
	testutil.Ok(t, err)

	// We expect an error when reading back.
	_, err = io.ReadAll(reader)
	testutil.Equals(t, io.ErrUnexpectedEOF, err)
}

func TestParseConfig_CustomStorageClass(t *testing.T) {
	for _, testCase := range []struct {
		name, storageClassKey string
	}{
		{name: "ProperCase", storageClassKey: "X-Amz-Storage-Class"},
		{name: "UpperCase", storageClassKey: "X-AMZ-STORAGE-CLASS"},
		{name: "LowerCase", storageClassKey: "x-amz-storage-class"},
		{name: "MixedCase", storageClassKey: "X-Amz-sToraGe-Class"},
	} {
		t.Run(testCase.name, func(t *testing.T) {
			cfg := DefaultConfig
			cfg.Endpoint = endpoint
			storageClass := "STANDARD_IA"
			cfg.PutUserMetadata[testCase.storageClassKey] = storageClass
			bkt, err := NewBucketWithConfig(log.NewNopLogger(), cfg, "test", nil)
			testutil.Ok(t, err)
			testutil.Equals(t, storageClass, bkt.storageClass)
		})
	}
}

func TestParseConfig_DefaultStorageClassIsZero(t *testing.T) {
	cfg := DefaultConfig
	cfg.Endpoint = endpoint
	bkt, err := NewBucketWithConfig(log.NewNopLogger(), cfg, "test", nil)
	testutil.Ok(t, err)
	testutil.Equals(t, "", bkt.storageClass)
}

func TestNewBucketWithErrorRoundTripper(t *testing.T) {
	cfg := DefaultConfig
	cfg.Endpoint = endpoint
	cfg.Bucket = "test"
	bkt, err := NewBucketWithConfig(log.NewNopLogger(), cfg, "test", errutil.WrapWithErrRoundtripper)
	testutil.Ok(t, err)
	_, err = bkt.Get(context.Background(), "test")
	// We expect an error from the RoundTripper
	testutil.NotOk(t, err)
	testutil.Assert(t, errutil.IsMockedError(err), "Expected RoundTripper error, got: %v", err)
}
```

## File: `providers/s3/testdata/encryption_key`
```
suchSecretVeryCryptographicKeyZ
```

## File: `providers/swift/swift.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

// Package swift implements common object storage abstractions against OpenStack swift APIs.
package swift

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"
	"strings"
	"testing"
	"time"

	"github.com/efficientgo/core/errcapture"
	"github.com/go-kit/log"
	"github.com/go-kit/log/level"
	"github.com/ncw/swift"
	"github.com/pkg/errors"
	"github.com/prometheus/common/model"

	"github.com/thanos-io/objstore"
	"github.com/thanos-io/objstore/exthttp"
	"gopkg.in/yaml.v2"
)

const (
	// DirDelim is the delimiter used to model a directory structure in an object store bucket.
	DirDelim = '/'
	// SegmentsDir represent name of the directory in bucket, where to store file parts of SLO and DLO.
	SegmentsDir = "segments/"
)

var DefaultConfig = Config{
	AuthVersion:    0, // Means autodetect of the auth API version by the library.
	ChunkSize:      1024 * 1024 * 1024,
	Retries:        3,
	ConnectTimeout: model.Duration(10 * time.Second),
	Timeout:        model.Duration(5 * time.Minute),
	HTTPConfig:     exthttp.DefaultHTTPConfig,
}

type Config struct {
	AuthVersion                 int                `yaml:"auth_version"`
	AuthUrl                     string             `yaml:"auth_url"`
	Username                    string             `yaml:"username"`
	UserDomainName              string             `yaml:"user_domain_name"`
	UserDomainID                string             `yaml:"user_domain_id"`
	UserId                      string             `yaml:"user_id"`
	Password                    string             `yaml:"password"`
	DomainId                    string             `yaml:"domain_id"`
	DomainName                  string             `yaml:"domain_name"`
	ApplicationCredentialID     string             `yaml:"application_credential_id"`
	ApplicationCredentialName   string             `yaml:"application_credential_name"`
	ApplicationCredentialSecret string             `yaml:"application_credential_secret"`
	ProjectID                   string             `yaml:"project_id"`
	ProjectName                 string             `yaml:"project_name"`
	ProjectDomainID             string             `yaml:"project_domain_id"`
	ProjectDomainName           string             `yaml:"project_domain_name"`
	RegionName                  string             `yaml:"region_name"`
	ContainerName               string             `yaml:"container_name"`
	ChunkSize                   int64              `yaml:"large_object_chunk_size"`
	SegmentContainerName        string             `yaml:"large_object_segments_container_name"`
	Retries                     int                `yaml:"retries"`
	ConnectTimeout              model.Duration     `yaml:"connect_timeout"`
	Timeout                     model.Duration     `yaml:"timeout"`
	UseDynamicLargeObjects      bool               `yaml:"use_dynamic_large_objects"`
	HTTPConfig                  exthttp.HTTPConfig `yaml:"http_config"`
}

func parseConfig(conf []byte) (*Config, error) {
	sc := DefaultConfig
	err := yaml.UnmarshalStrict(conf, &sc)
	return &sc, err
}

func configFromEnv() (*Config, error) {
	c := swift.Connection{}
	if err := c.ApplyEnvironment(); err != nil {
		return nil, err
	}

	config := Config{
		AuthVersion:                 c.AuthVersion,
		AuthUrl:                     c.AuthUrl,
		Username:                    c.UserName,
		UserId:                      c.UserId,
		Password:                    c.ApiKey,
		DomainId:                    c.DomainId,
		DomainName:                  c.Domain,
		ApplicationCredentialID:     c.ApplicationCredentialId,
		ApplicationCredentialName:   c.ApplicationCredentialName,
		ApplicationCredentialSecret: c.ApplicationCredentialSecret,
		ProjectID:                   c.TenantId,
		ProjectName:                 c.Tenant,
		ProjectDomainID:             c.TenantDomainId,
		ProjectDomainName:           c.TenantDomain,
		RegionName:                  c.Region,
		ContainerName:               os.Getenv("OS_CONTAINER_NAME"),
		ChunkSize:                   DefaultConfig.ChunkSize,
		SegmentContainerName:        os.Getenv("SWIFT_SEGMENTS_CONTAINER_NAME"),
		Retries:                     c.Retries,
		ConnectTimeout:              model.Duration(c.ConnectTimeout),
		Timeout:                     model.Duration(c.Timeout),
		UseDynamicLargeObjects:      false,
		HTTPConfig:                  DefaultConfig.HTTPConfig,
	}
	if os.Getenv("SWIFT_CHUNK_SIZE") != "" {
		var err error
		config.ChunkSize, err = strconv.ParseInt(os.Getenv("SWIFT_CHUNK_SIZE"), 10, 64)
		if err != nil {
			return nil, errors.Wrap(err, "parsing chunk size")
		}
	}
	if strings.ToLower(os.Getenv("SWIFT_USE_DYNAMIC_LARGE_OBJECTS")) == "true" {
		config.UseDynamicLargeObjects = true
	}
	return &config, nil
}

func connectionFromConfig(sc *Config, rt http.RoundTripper) *swift.Connection {
	connection := swift.Connection{
		AuthVersion:                 sc.AuthVersion,
		AuthUrl:                     sc.AuthUrl,
		UserName:                    sc.Username,
		UserId:                      sc.UserId,
		ApiKey:                      sc.Password,
		DomainId:                    sc.DomainId,
		Domain:                      sc.DomainName,
		ApplicationCredentialId:     sc.ApplicationCredentialID,
		ApplicationCredentialName:   sc.ApplicationCredentialName,
		ApplicationCredentialSecret: sc.ApplicationCredentialSecret,
		TenantId:                    sc.ProjectID,
		Tenant:                      sc.ProjectName,
		TenantDomain:                sc.ProjectDomainName,
		TenantDomainId:              sc.ProjectDomainID,
		Region:                      sc.RegionName,
		Retries:                     sc.Retries,
		ConnectTimeout:              time.Duration(sc.ConnectTimeout),
		Timeout:                     time.Duration(sc.Timeout),
		Transport:                   rt,
	}
	return &connection
}

type Container struct {
	logger                 log.Logger
	name                   string
	connection             *swift.Connection
	chunkSize              int64
	useDynamicLargeObjects bool
	segmentsContainer      string
}

func NewContainer(logger log.Logger, conf []byte, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Container, error) {
	sc, err := parseConfig(conf)
	if err != nil {
		return nil, errors.Wrap(err, "parse config")
	}
	return NewContainerFromConfig(logger, sc, false, wrapRoundtripper)
}

func ensureContainer(connection *swift.Connection, name string, createIfNotExist bool) error {
	if _, _, err := connection.Container(name); err != nil {
		if err != swift.ContainerNotFound {
			return errors.Wrapf(err, "verify container %s", name)
		}
		if !createIfNotExist {
			return fmt.Errorf("unable to find the expected container %s", name)
		}
		if err = connection.ContainerCreate(name, swift.Headers{}); err != nil {
			return errors.Wrapf(err, "create container %s", name)
		}
		return nil
	}
	return nil
}

func NewContainerFromConfig(logger log.Logger, sc *Config, createContainer bool, wrapRoundtripper func(http.RoundTripper) http.RoundTripper) (*Container, error) {
	// Check if a roundtripper has been set in the config
	// otherwise build the default transport.
	var rt http.RoundTripper
	rt, err := exthttp.DefaultTransport(sc.HTTPConfig)
	if err != nil {
		return nil, err
	}
	if sc.HTTPConfig.Transport != nil {
		rt = sc.HTTPConfig.Transport
	}
	if wrapRoundtripper != nil {
		rt = wrapRoundtripper(rt)
	}

	connection := connectionFromConfig(sc, rt)
	if err := connection.Authenticate(); err != nil {
		return nil, errors.Wrap(err, "authentication")
	}

	if err := ensureContainer(connection, sc.ContainerName, createContainer); err != nil {
		return nil, err
	}
	if sc.SegmentContainerName == "" {
		sc.SegmentContainerName = sc.ContainerName
	} else if err := ensureContainer(connection, sc.SegmentContainerName, createContainer); err != nil {
		return nil, err
	}

	return &Container{
		logger:                 logger,
		name:                   sc.ContainerName,
		connection:             connection,
		chunkSize:              sc.ChunkSize,
		useDynamicLargeObjects: sc.UseDynamicLargeObjects,
		segmentsContainer:      sc.SegmentContainerName,
	}, nil
}

func (c *Container) Provider() objstore.ObjProvider { return objstore.SWIFT }

// Name returns the container name for swift.
func (c *Container) Name() string {
	return c.name
}

func (c *Container) SupportedIterOptions() []objstore.IterOptionType {
	return []objstore.IterOptionType{objstore.Recursive}
}

// Iter calls f for each entry in the given directory. The argument to f is the full
// object name including the prefix of the inspected directory.
func (c *Container) Iter(ctx context.Context, dir string, f func(string) error, options ...objstore.IterOption) error {
	if dir != "" {
		dir = strings.TrimSuffix(dir, string(DirDelim)) + string(DirDelim)
	}

	listOptions := &swift.ObjectsOpts{
		Prefix:    dir,
		Delimiter: DirDelim,
	}
	if objstore.ApplyIterOptions(options...).Recursive {
		listOptions.Delimiter = rune(0)
	}

	return c.connection.ObjectsWalk(c.name, listOptions, func(opts *swift.ObjectsOpts) (interface{}, error) {
		objects, err := c.connection.ObjectNames(c.name, opts)
		if err != nil {
			return objects, errors.Wrap(err, "list object names")
		}

		for _, object := range objects {
			if object == SegmentsDir {
				continue
			}
			if err := f(object); err != nil {
				return objects, errors.Wrap(err, "iteration over objects")
			}
		}
		return objects, nil
	})
}

func (c *Container) IterWithAttributes(ctx context.Context, dir string, f func(attrs objstore.IterObjectAttributes) error, options ...objstore.IterOption) error {
	if err := objstore.ValidateIterOptions(c.SupportedIterOptions(), options...); err != nil {
		return err
	}

	return c.Iter(ctx, dir, func(name string) error {
		return f(objstore.IterObjectAttributes{Name: name})
	}, options...)
}

func (c *Container) get(name string, headers swift.Headers, checkHash bool) (io.ReadCloser, error) {
	if name == "" {
		return nil, errors.New("object name cannot be empty")
	}
	file, _, err := c.connection.ObjectOpen(c.name, name, checkHash, headers)
	if err != nil {
		return nil, errors.Wrap(err, "open object")
	}

	return objstore.ObjectSizerReadCloser{
		ReadCloser: file,
		Size:       file.Length,
	}, nil
}

// Get returns a reader for the given object name.
func (c *Container) Get(_ context.Context, name string) (io.ReadCloser, error) {
	return c.get(name, swift.Headers{}, true)
}

func (c *Container) GetRange(_ context.Context, name string, off, length int64) (io.ReadCloser, error) {
	// Set Range HTTP header, see the docs https://docs.openstack.org/api-ref/object-store/?expanded=show-container-details-and-list-objects-detail,get-object-content-and-metadata-detail#id76.
	bytesRange := fmt.Sprintf("bytes=%d-", off)
	if length != -1 {
		bytesRange = fmt.Sprintf("%s%d", bytesRange, off+length-1)
	}
	return c.get(name, swift.Headers{"Range": bytesRange}, false)
}

// Attributes returns information about the specified object.
func (c *Container) Attributes(_ context.Context, name string) (objstore.ObjectAttributes, error) {
	if name == "" {
		return objstore.ObjectAttributes{}, errors.New("object name cannot be empty")
	}
	info, _, err := c.connection.Object(c.name, name)
	if err != nil {
		return objstore.ObjectAttributes{}, errors.Wrap(err, "get object attributes")
	}
	return objstore.ObjectAttributes{
		Size:         info.Bytes,
		LastModified: info.LastModified,
	}, nil
}

// Exists checks if the given object exists.
func (c *Container) Exists(_ context.Context, name string) (bool, error) {
	found := true
	_, _, err := c.connection.Object(c.name, name)
	if c.IsObjNotFoundErr(err) {
		err = nil
		found = false
	}
	return found, err
}

// IsObjNotFoundErr returns true if error means that object is not found. Relevant to Get operations.
func (c *Container) IsObjNotFoundErr(err error) bool {
	return errors.Is(err, swift.ObjectNotFound)
}

// IsAccessDeniedErr returns true if access to object is denied.
func (c *Container) IsAccessDeniedErr(err error) bool {
	return errors.Is(err, swift.Forbidden)
}

// Upload writes the contents of the reader as an object into the container.
func (c *Container) Upload(_ context.Context, name string, r io.Reader, opts ...objstore.ObjectUploadOption) (err error) {
	size, err := objstore.TryToGetSize(r)
	if err != nil {
		level.Warn(c.logger).Log("msg", "could not guess file size, using large object to avoid issues if the file is larger than limit", "name", name, "err", err)
		// Anything higher or equal to chunk size so the SLO is used.
		size = c.chunkSize
	}

	uploadOpts := objstore.ApplyObjectUploadOptions(opts...)

	var file io.WriteCloser
	if size >= c.chunkSize {
		opts := swift.LargeObjectOpts{
			Container:        c.name,
			ObjectName:       name,
			ChunkSize:        c.chunkSize,
			SegmentContainer: c.segmentsContainer,
			CheckHash:        true,
			ContentType:      uploadOpts.ContentType,
		}
		if c.useDynamicLargeObjects {
			if file, err = c.connection.DynamicLargeObjectCreateFile(&opts); err != nil {
				return errors.Wrap(err, "create DLO file")
			}
		} else {
			if file, err = c.connection.StaticLargeObjectCreateFile(&opts); err != nil {
				return errors.Wrap(err, "create SLO file")
			}
		}
	} else {
		if file, err = c.connection.ObjectCreate(c.name, name, true, "", uploadOpts.ContentType, swift.Headers{}); err != nil {
			return errors.Wrap(err, "create file")
		}
	}
	defer errcapture.Do(&err, file.Close, "upload object close")
	if _, err := io.Copy(file, r); err != nil {
		return errors.Wrap(err, "uploading object")
	}
	return nil
}

// Delete removes the object with the given name.
func (c *Container) Delete(_ context.Context, name string) error {
	return errors.Wrap(c.connection.LargeObjectDelete(c.name, name), "delete object")
}

func (*Container) Close() error {
	// Nothing to close.
	return nil
}

// NewTestContainer creates test objStore client that before returning creates temporary container.
// In a close function it empties and deletes the container.
func NewTestContainer(t testing.TB) (objstore.Bucket, func(), error) {
	config, err := configFromEnv()
	if err != nil {
		return nil, nil, errors.Wrap(err, "loading config from ENV")
	}
	if config.ContainerName != "" {
		if os.Getenv("THANOS_ALLOW_EXISTING_BUCKET_USE") == "" {
			return nil, nil, errors.New("OS_CONTAINER_NAME is defined. Normally this tests will create temporary container " +
				"and delete it after test. Unset OS_CONTAINER_NAME env variable to use default logic. If you really want to run " +
				"tests against provided (NOT USED!) container, set THANOS_ALLOW_EXISTING_BUCKET_USE=true. WARNING: That container " +
				"needs to be manually cleared. This means that it is only useful to run one test in a time. This is due " +
				"to safety (accidentally pointing prod container for test) as well as swift not being fully strong consistent.")
		}
		c, err := NewContainerFromConfig(log.NewNopLogger(), config, false, nil)
		if err != nil {
			return nil, nil, errors.Wrap(err, "initializing new container")
		}
		if err := c.Iter(context.Background(), "", func(f string) error {
			return errors.Errorf("container %s is not empty", c.Name())
		}); err != nil {
			return nil, nil, errors.Wrapf(err, "check container %s", c.Name())
		}
		t.Log("WARNING. Reusing", c.Name(), "container for Swift tests. Manual cleanup afterwards is required")
		return c, func() {}, nil
	}
	config.ContainerName = objstore.CreateTemporaryTestBucketName(t)
	config.SegmentContainerName = config.ContainerName
	c, err := NewContainerFromConfig(log.NewNopLogger(), config, true, nil)
	if err != nil {
		return nil, nil, errors.Wrap(err, "initializing new container")
	}
	t.Log("created temporary container for swift tests with name", c.Name())

	return c, func() {
		objstore.EmptyBucket(t, context.Background(), c)
		if err := c.connection.ContainerDelete(c.name); err != nil {
			t.Logf("deleting container %s failed: %s", c.Name(), err)
		}
		if err := c.connection.ContainerDelete(c.segmentsContainer); err != nil {
			t.Logf("deleting segments container %s failed: %s", c.segmentsContainer, err)
		}
	}, nil
}
```

## File: `providers/swift/swift_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package swift

import (
	"testing"
	"time"

	"github.com/efficientgo/core/testutil"
	"github.com/go-kit/log"
	"github.com/prometheus/common/model"
	"github.com/thanos-io/objstore/errutil"
)

func TestParseConfig(t *testing.T) {
	input := []byte(`auth_url: http://identity.something.com/v3
username: thanos
user_domain_name: userDomain
project_name: thanosProject
project_domain_name: projectDomain`)

	cfg, err := parseConfig(input)
	testutil.Ok(t, err)

	testutil.Equals(t, "http://identity.something.com/v3", cfg.AuthUrl)
	testutil.Equals(t, "thanos", cfg.Username)
	testutil.Equals(t, "userDomain", cfg.UserDomainName)
	testutil.Equals(t, "thanosProject", cfg.ProjectName)
	testutil.Equals(t, "projectDomain", cfg.ProjectDomainName)
}

func TestParseConfigFail(t *testing.T) {
	input := []byte(`auth_url: http://identity.something.com/v3
tenant_name: something`)

	_, err := parseConfig(input)
	// Must result in unmarshal error as there's no `tenant_name` in SwiftConfig.
	testutil.NotOk(t, err)
}

func TestParseConfig_HTTPConfig(t *testing.T) {
	input := []byte(`auth_url: http://identity.something.com/v3
username: thanos
user_domain_name: userDomain
project_name: thanosProject
project_domain_name: projectDomain
http_config:
  tls_config:
    ca_file: /certs/ca.crt
    cert_file: /certs/cert.crt
    key_file: /certs/key.key
    server_name: server
    insecure_skip_verify: false`)
	cfg, err := parseConfig([]byte(input))

	testutil.Ok(t, err)

	testutil.Equals(t, "http://identity.something.com/v3", cfg.AuthUrl)
	testutil.Equals(t, "thanos", cfg.Username)
	testutil.Equals(t, "userDomain", cfg.UserDomainName)
	testutil.Equals(t, "thanosProject", cfg.ProjectName)
	testutil.Equals(t, "projectDomain", cfg.ProjectDomainName)
	testutil.Equals(t, model.Duration(90*time.Second), cfg.HTTPConfig.IdleConnTimeout)
	testutil.Equals(t, model.Duration(2*time.Minute), cfg.HTTPConfig.ResponseHeaderTimeout)
	testutil.Equals(t, false, cfg.HTTPConfig.InsecureSkipVerify)

}

func TestNewBucketWithErrorRoundTripper(t *testing.T) {
	config := DefaultConfig
	config.AuthUrl = "http://identity.something.com/v3"
	_, err := NewContainerFromConfig(log.NewNopLogger(), &config, false, errutil.WrapWithErrRoundtripper)

	// We expect an error from the RoundTripper
	testutil.NotOk(t, err)
	testutil.Assert(t, errutil.IsMockedError(err), "Expected RoundTripper error, got: %v", err)
}
```

## File: `scripts/cleanup-white-noise.sh`
```bash
#!/bin/bash
SED_BIN=${SED_BIN:-sed}

${SED_BIN} -i 's/[ \t]*$//' "$@"
```

## File: `scripts/cfggen/main.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package main

import (
	"fmt"
	"github.com/thanos-io/objstore"
	"io"
	"os"
	"path/filepath"
	"reflect"
	"strings"

	"github.com/thanos-io/objstore/client"
	"github.com/thanos-io/objstore/providers/azure"
	"github.com/thanos-io/objstore/providers/bos"
	"github.com/thanos-io/objstore/providers/cos"
	"github.com/thanos-io/objstore/providers/filesystem"
	"github.com/thanos-io/objstore/providers/gcs"
	"github.com/thanos-io/objstore/providers/obs"
	"github.com/thanos-io/objstore/providers/oci"
	"github.com/thanos-io/objstore/providers/oss"
	"github.com/thanos-io/objstore/providers/s3"
	"github.com/thanos-io/objstore/providers/swift"

	"github.com/fatih/structtag"
	"github.com/go-kit/log"
	"github.com/go-kit/log/level"
	"github.com/pkg/errors"
	"gopkg.in/alecthomas/kingpin.v2"
	"gopkg.in/yaml.v2"
)

var (
	configs        map[string]interface{}
	possibleValues []string

	bucketConfigs = map[objstore.ObjProvider]interface{}{
		objstore.AZURE:      azure.Config{},
		objstore.GCS:        gcs.Config{},
		objstore.S3:         s3.DefaultConfig,
		objstore.SWIFT:      swift.DefaultConfig,
		objstore.COS:        cos.DefaultConfig,
		objstore.ALIYUNOSS:  oss.Config{},
		objstore.FILESYSTEM: filesystem.Config{},
		objstore.BOS:        bos.Config{},
		objstore.OCI:        oci.Config{},
		objstore.OBS:        obs.DefaultConfig,
	}
)

func init() {
	configs = map[string]interface{}{}

	for typ, config := range bucketConfigs {
		configs[name(config)] = client.BucketConfig{Type: typ, Config: config}
	}

	for k := range configs {
		possibleValues = append(possibleValues, k)
	}
}

func name(typ interface{}) string {
	return fmt.Sprintf("%T", typ)
}

func main() {
	app := kingpin.New(filepath.Base(os.Args[0]), "Thanos config examples generator.")
	app.HelpFlag.Short('h')
	structName := app.Flag("name", fmt.Sprintf("Name of the struct to generated example for. Possible values: %v", strings.Join(possibleValues, ","))).Required().String()

	errLogger := level.Error(log.NewLogfmtLogger(log.NewSyncWriter(os.Stderr)))
	if _, err := app.Parse(os.Args[1:]); err != nil {
		errLogger.Log("err", err)
		os.Exit(1)
	}

	if c, ok := configs[*structName]; ok {
		if err := generate(c, os.Stdout); err != nil {
			errLogger.Log("err", err)
			os.Exit(1)
		}
		return
	}

	errLogger.Log("err", errors.Errorf("%v struct not found. Possible values %v", *structName, strings.Join(possibleValues, ",")))
	os.Exit(1)
}

func generate(obj interface{}, w io.Writer) error {
	// We forbid omitempty option. This is for simplification for doc generation.
	if err := checkForOmitEmptyTagOption(obj); err != nil {
		return errors.Wrap(err, "invalid type")
	}
	return yaml.NewEncoder(w).Encode(obj)
}

func checkForOmitEmptyTagOption(obj interface{}) error {
	return checkForOmitEmptyTagOptionRec(reflect.ValueOf(obj))
}

func checkForOmitEmptyTagOptionRec(v reflect.Value) error {
	switch v.Kind() {
	case reflect.Struct:
		for i := 0; i < v.NumField(); i++ {
			tags, err := structtag.Parse(string(v.Type().Field(i).Tag))
			if err != nil {
				return errors.Wrapf(err, "%s: failed to parse tag %q", v.Type().Field(i).Name, v.Type().Field(i).Tag)
			}

			tag, err := tags.Get("yaml")
			if err != nil {
				return errors.Wrapf(err, "%s: failed to get tag %q", v.Type().Field(i).Name, v.Type().Field(i).Tag)
			}

			for _, opts := range tag.Options {
				if opts == "omitempty" {
					return errors.Errorf("omitempty is forbidden for config, but spotted on field '%s'", v.Type().Field(i).Name)
				}
			}

			if err := checkForOmitEmptyTagOptionRec(v.Field(i)); err != nil {
				return errors.Wrapf(err, "%s", v.Type().Field(i).Name)
			}
		}

	case reflect.Ptr:
		return errors.New("nil pointers are not allowed in configuration")

	case reflect.Interface:
		return checkForOmitEmptyTagOptionRec(v.Elem())
	}

	return nil
}
```

## File: `test/e2e/e2ethanos/helpers.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package e2ethanos

import (
	"net/http"
	"net/http/httputil"
	"net/url"
	"os/exec"
	"strings"
	"testing"

	"github.com/efficientgo/core/testutil"
	"github.com/efficientgo/e2e"
)

func CleanScenario(t testing.TB, e *e2e.DockerEnvironment) func() {
	return func() {
		// Make sure Clean can properly delete everything.
		testutil.Ok(t, exec.Command("chmod", "-R", "777", e.SharedDir()).Run())
		e.Close()
	}
}

func singleJoiningSlash(a, b string) string {
	aslash := strings.HasSuffix(a, "/")
	bslash := strings.HasPrefix(b, "/")
	switch {
	case aslash && bslash:
		return a + b[1:]
	case !aslash && !bslash:
		return a + "/" + b
	}
	return a + b
}

// NewSingleHostReverseProxy is almost same as httputil.NewSingleHostReverseProxy
// but it performs a url path rewrite.
func NewSingleHostReverseProxy(target *url.URL, externalPrefix string) *httputil.ReverseProxy {
	targetQuery := target.RawQuery
	director := func(req *http.Request) {
		req.URL.Scheme = target.Scheme
		req.URL.Host = target.Host
		req.URL.Path = singleJoiningSlash(target.Path, strings.TrimPrefix(req.URL.Path, "/"+externalPrefix))

		if targetQuery == "" || req.URL.RawQuery == "" {
			req.URL.RawQuery = targetQuery + req.URL.RawQuery
		} else {
			req.URL.RawQuery = targetQuery + "&" + req.URL.RawQuery
		}
	}
	return &httputil.ReverseProxy{Director: director}
}
```

## File: `test/e2e/e2ethanos/services.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package e2ethanos

import (
	"crypto/rand"
	"crypto/rsa"
	"crypto/x509"
	"encoding/pem"
	"fmt"
	"math/big"
	"net"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"

	"github.com/efficientgo/core/backoff"
	"github.com/efficientgo/e2e"
	e2edb "github.com/efficientgo/e2e/db"
	e2emon "github.com/efficientgo/e2e/monitoring"
	"github.com/efficientgo/e2e/monitoring/promconfig/discovery/targetgroup"
	"github.com/pkg/errors"
	"github.com/prometheus/common/model"
	"gopkg.in/yaml.v2"

	"github.com/thanos-io/objstore/client"
	"github.com/thanos-io/objstore/exthttp"
	"github.com/thanos-io/objstore/providers/s3"
)

const (
	infoLogLevel = "info"
)

// Same as default for now.
var defaultBackoffConfig = backoff.Config{
	Min:        300 * time.Millisecond,
	Max:        600 * time.Millisecond,
	MaxRetries: 50,
}

// TODO(bwplotka): Make strconv.Itoa(os.Getuid()) pattern in e2e?
func wrapWithDefaults(opt e2e.StartOptions) e2e.StartOptions {
	if opt.User == "" {
		opt.User = strconv.Itoa(os.Getuid())
	}
	if opt.WaitReadyBackoff == nil {
		opt.WaitReadyBackoff = &defaultBackoffConfig
	}
	return opt
}

const (
	// FeatureExemplarStorage is a feature flag that enables exemplar storage on Prometheus.
	FeatureExemplarStorage = "exemplar-storage"
)

// DefaultPrometheusImage sets default Prometheus image used in e2e service.
func DefaultPrometheusImage() string {
	return "quay.io/prometheus/prometheus:v2.29.2"
}

// DefaultAlertmanagerImage sets default Alertmanager image used in e2e service.
func DefaultAlertmanagerImage() string {
	return "quay.io/prometheus/alertmanager:v0.20.0"
}

// DefaultImage returns the local docker image to use to run Thanos.
func DefaultImage() string {
	// Get the Thanos image from the THANOS_IMAGE env variable.
	if os.Getenv("THANOS_IMAGE") != "" {
		return os.Getenv("THANOS_IMAGE")
	}

	return "thanos"
}

func defaultPromHttpConfig() string {
	// username: test, secret: test(bcrypt hash)
	return `basic_auth:
  username: test
  password: test
`
}

func NewPrometheus(e e2e.Environment, name, promConfig, webConfig, promImage string, enableFeatures ...string) *e2emon.InstrumentedRunnable {
	f := e.Runnable(name).
		WithPorts(map[string]int{"http": 9090}).
		Future()

	if err := os.MkdirAll(f.Dir(), 0750); err != nil {
		return &e2emon.InstrumentedRunnable{Runnable: e2e.NewFailedRunnable(name, errors.Wrap(err, "create prometheus dir"))}
	}

	if err := os.WriteFile(filepath.Join(f.Dir(), "prometheus.yml"), []byte(promConfig), 0600); err != nil {
		return &e2emon.InstrumentedRunnable{Runnable: e2e.NewFailedRunnable(name, errors.Wrap(err, "creating prom config"))}
	}

	if len(webConfig) > 0 {
		if err := os.WriteFile(filepath.Join(f.Dir(), "web-config.yml"), []byte(webConfig), 0600); err != nil {
			return &e2emon.InstrumentedRunnable{Runnable: e2e.NewFailedRunnable(name, errors.Wrap(err, "creating web-config"))}
		}
	}

	probe := e2e.NewHTTPReadinessProbe("http", "/-/ready", 200, 200)
	args := e2e.BuildArgs(map[string]string{
		"--config.file":                     filepath.Join(f.InternalDir(), "prometheus.yml"),
		"--storage.tsdb.path":               f.InternalDir(),
		"--storage.tsdb.max-block-duration": "2h",
		"--log.level":                       infoLogLevel,
		"--web.listen-address":              ":9090",
	})

	if len(enableFeatures) > 0 {
		args = append(args, fmt.Sprintf("--enable-feature=%s", strings.Join(enableFeatures, ",")))
	}
	if len(webConfig) > 0 {
		args = append(args, fmt.Sprintf("--web.config.file=%s", filepath.Join(f.InternalDir(), "web-config.yml")))
		// If auth is enabled then prober would get 401 error.
		probe = e2e.NewHTTPReadinessProbe("http", "/-/ready", 401, 401)
	}
	return e2emon.AsInstrumented(f.Init(wrapWithDefaults(e2e.StartOptions{
		Image:     promImage,
		Command:   e2e.NewCommandWithoutEntrypoint("prometheus", args...),
		Readiness: probe,
	})), "http")
}

func NewPrometheusWithSidecar(e e2e.Environment, name, promConfig, webConfig, promImage, minTime string, enableFeatures ...string) (*e2emon.InstrumentedRunnable, *e2emon.InstrumentedRunnable) {
	return NewPrometheusWithSidecarCustomImage(e, name, promConfig, webConfig, promImage, minTime, DefaultImage(), enableFeatures...)
}

func NewPrometheusWithSidecarCustomImage(e e2e.Environment, name, promConfig, webConfig, promImage, minTime string, sidecarImage string, enableFeatures ...string) (*e2emon.InstrumentedRunnable, *e2emon.InstrumentedRunnable) {
	prom := NewPrometheus(e, name, promConfig, webConfig, promImage, enableFeatures...)

	args := map[string]string{
		"--debug.name":        fmt.Sprintf("sidecar-%v", name),
		"--grpc-address":      ":9091",
		"--grpc-grace-period": "0s",
		"--http-address":      ":8080",
		"--prometheus.url":    "http://" + prom.InternalEndpoint("http"),
		"--tsdb.path":         prom.InternalDir(),
		"--log.level":         "debug",
	}
	if len(webConfig) > 0 {
		args["--prometheus.http-client"] = defaultPromHttpConfig()
	}
	if minTime != "" {
		args["--min-time"] = minTime
	}
	sidecarRunnable := e.Runnable(fmt.Sprintf("sidecar-%s", name)).WithPorts(map[string]int{"http": 8080, "grpc": 9091}).Init(wrapWithDefaults(e2e.StartOptions{
		Image:     sidecarImage,
		Command:   e2e.NewCommand("sidecar", e2e.BuildArgs(args)...),
		Readiness: e2e.NewHTTPReadinessProbe("http", "/-/ready", 200, 200),
	}))
	sidecar := e2emon.AsInstrumented(sidecarRunnable, "http")
	return prom, sidecar
}

type QuerierBuilder struct {
	name           string
	routePrefix    string
	externalPrefix string
	image          string

	storeAddresses       []string
	fileSDStoreAddresses []string
	ruleAddresses        []string
	metadataAddresses    []string
	targetAddresses      []string
	exemplarAddresses    []string
	enableFeatures       []string
	endpoints            []string

	replicaLabels []string
	tracingConfig string

	e2e.Linkable
	f e2e.FutureRunnable
}

func NewQuerierBuilder(e e2e.Environment, name string, storeAddresses ...string) *QuerierBuilder {
	f := e.Runnable(fmt.Sprintf("querier-%v", name)).
		WithPorts(map[string]int{
			"http": 8080,
			"grpc": 9091,
		}).
		Future()
	return &QuerierBuilder{
		Linkable:       f,
		f:              f,
		name:           name,
		storeAddresses: storeAddresses,
		image:          DefaultImage(),
		replicaLabels:  []string{replicaLabel},
	}
}

func (q *QuerierBuilder) WithEnabledFeatures(enableFeatures []string) *QuerierBuilder {
	q.enableFeatures = enableFeatures
	return q
}

func (q *QuerierBuilder) WithImage(image string) *QuerierBuilder {
	q.image = image
	return q
}

func (q *QuerierBuilder) WithStoreAddresses(storeAddresses ...string) *QuerierBuilder {
	q.storeAddresses = storeAddresses
	return q
}

func (q *QuerierBuilder) WithFileSDStoreAddresses(fileSDStoreAddresses ...string) *QuerierBuilder {
	q.fileSDStoreAddresses = fileSDStoreAddresses
	return q
}

func (q *QuerierBuilder) WithRuleAddresses(ruleAddresses ...string) *QuerierBuilder {
	q.ruleAddresses = ruleAddresses
	return q
}

func (q *QuerierBuilder) WithTargetAddresses(targetAddresses ...string) *QuerierBuilder {
	q.targetAddresses = targetAddresses
	return q
}

func (q *QuerierBuilder) WithExemplarAddresses(exemplarAddresses ...string) *QuerierBuilder {
	q.exemplarAddresses = exemplarAddresses
	return q
}

func (q *QuerierBuilder) WithMetadataAddresses(metadataAddresses ...string) *QuerierBuilder {
	q.metadataAddresses = metadataAddresses
	return q
}

func (q *QuerierBuilder) WithEndpoints(endpoints ...string) *QuerierBuilder {
	q.endpoints = endpoints
	return q
}

func (q *QuerierBuilder) WithRoutePrefix(routePrefix string) *QuerierBuilder {
	q.routePrefix = routePrefix
	return q
}

func (q *QuerierBuilder) WithExternalPrefix(externalPrefix string) *QuerierBuilder {
	q.externalPrefix = externalPrefix
	return q
}

func (q *QuerierBuilder) WithTracingConfig(tracingConfig string) *QuerierBuilder {
	q.tracingConfig = tracingConfig
	return q
}

// WithReplicaLabels replaces default [replica] replica label configuration for the querier.
func (q *QuerierBuilder) WithReplicaLabels(labels ...string) *QuerierBuilder {
	q.replicaLabels = labels
	return q
}

func (q *QuerierBuilder) Init() *e2emon.InstrumentedRunnable {
	args, err := q.collectArgs()
	if err != nil {
		return &e2emon.InstrumentedRunnable{Runnable: e2e.NewFailedRunnable(q.name, err)}
	}

	return e2emon.AsInstrumented(q.f.Init(wrapWithDefaults(e2e.StartOptions{
		Image:     q.image,
		Command:   e2e.NewCommand("query", args...),
		Readiness: e2e.NewHTTPReadinessProbe("http", "/-/ready", 200, 200),
	})), "http")
}

const replicaLabel = "replica"

func (q *QuerierBuilder) collectArgs() ([]string, error) {
	args := e2e.BuildArgs(map[string]string{
		"--debug.name":            fmt.Sprintf("querier-%v", q.name),
		"--grpc-address":          ":9091",
		"--grpc-grace-period":     "0s",
		"--http-address":          ":8080",
		"--store.sd-dns-interval": "5s",
		"--log.level":             infoLogLevel,
		"--query.max-concurrent":  "1",
		"--store.sd-interval":     "5s",
	})

	for _, repl := range q.replicaLabels {
		args = append(args, "--query.replica-label="+repl)
	}
	for _, addr := range q.storeAddresses {
		args = append(args, "--store="+addr)
	}
	for _, addr := range q.ruleAddresses {
		args = append(args, "--rule="+addr)
	}
	for _, addr := range q.targetAddresses {
		args = append(args, "--target="+addr)
	}
	for _, addr := range q.metadataAddresses {
		args = append(args, "--metadata="+addr)
	}
	for _, addr := range q.exemplarAddresses {
		args = append(args, "--exemplar="+addr)
	}
	for _, feature := range q.enableFeatures {
		args = append(args, "--enable-feature="+feature)
	}
	for _, addr := range q.endpoints {
		args = append(args, "--endpoint="+addr)
	}
	if len(q.fileSDStoreAddresses) > 0 {
		if err := os.MkdirAll(q.Dir(), 0750); err != nil {
			return nil, errors.Wrap(err, "create query dir failed")
		}

		fileSD := []*targetgroup.Group{{}}
		for _, a := range q.fileSDStoreAddresses {
			fileSD[0].Targets = append(fileSD[0].Targets, model.LabelSet{model.AddressLabel: model.LabelValue(a)})
		}

		b, err := yaml.Marshal(fileSD)
		if err != nil {
			return nil, err
		}

		if err := os.WriteFile(q.Dir()+"/filesd.yaml", b, 0600); err != nil {
			return nil, errors.Wrap(err, "creating query SD config failed")
		}

		args = append(args, "--store.sd-files="+filepath.Join(q.InternalDir(), "filesd.yaml"))
	}
	if q.routePrefix != "" {
		args = append(args, "--web.route-prefix="+q.routePrefix)
	}
	if q.externalPrefix != "" {
		args = append(args, "--web.external-prefix="+q.externalPrefix)
	}
	if q.tracingConfig != "" {
		args = append(args, "--tracing.config="+q.tracingConfig)
	}
	return args, nil
}

func NewReverseProxy(e e2e.Environment, name, tenantID, target string) *e2emon.InstrumentedRunnable {
	conf := fmt.Sprintf(`
events {
	worker_connections  1024;
}

http {
	server {
		listen 80;
		server_name _;

		location / {
			proxy_set_header THANOS-TENANT %s;
			proxy_pass %s;
		}
	}
}
`, tenantID, target)

	f := e.Runnable(fmt.Sprintf("nginx-%s", name)).
		WithPorts(map[string]int{"http": 80}).
		Future()

	if err := os.MkdirAll(f.Dir(), 0750); err != nil {
		return &e2emon.InstrumentedRunnable{Runnable: e2e.NewFailedRunnable(name, errors.Wrap(err, "create store dir"))}
	}

	if err := os.WriteFile(filepath.Join(f.Dir(), "nginx.conf"), []byte(conf), 0600); err != nil {
		return &e2emon.InstrumentedRunnable{Runnable: e2e.NewFailedRunnable(name, errors.Wrap(err, "creating nginx config file failed"))}
	}

	return e2emon.AsInstrumented(f.Init(e2e.StartOptions{
		Image:            "docker.io/nginx:1.21.1-alpine",
		Volumes:          []string{filepath.Join(f.Dir(), "/nginx.conf") + ":/etc/nginx/nginx.conf:ro"},
		WaitReadyBackoff: &defaultBackoffConfig,
	}), "http")
}

// NewMinio returns minio server, used as a local replacement for S3.
// TODO(@matej-g): This is a temporary workaround for https://github.com/efficientgo/e2e/issues/11;
// after this is addresses fixed all calls should be replaced with e2edb.NewMinio.
func NewMinio(e e2e.Environment, name, bktName string) *e2emon.InstrumentedRunnable {
	image := "minio/minio:RELEASE.2022-07-30T05-21-40Z"
	minioKESGithubContent := "https://raw.githubusercontent.com/minio/kes/master"

	httpsPort := 8090
	consolePort := 8080
	f := e.Runnable(fmt.Sprintf("minio-%s", name)).
		WithPorts(map[string]int{"https": httpsPort, "console": consolePort}).
		Future()

	if err := os.MkdirAll(filepath.Join(f.Dir(), "certs", "CAs"), 0750); err != nil {
		return &e2emon.InstrumentedRunnable{Runnable: e2e.NewFailedRunnable(name, errors.Wrap(err, "create certs dir"))}
	}

	if err := genCerts(
		filepath.Join(f.Dir(), "certs", "public.crt"),
		filepath.Join(f.Dir(), "certs", "private.key"),
		filepath.Join(f.Dir(), "certs", "CAs", "ca.crt"),
		fmt.Sprintf("%s-minio-%s", e.Name(), name),
	); err != nil {
		return &e2emon.InstrumentedRunnable{Runnable: e2e.NewFailedRunnable(name, errors.Wrap(err, "fail to generate certs"))}
	}

	commands := []string{
		fmt.Sprintf("curl -sSL --tlsv1.2 -O '%s/root.key' -O '%s/root.cert'", minioKESGithubContent, minioKESGithubContent),
		fmt.Sprintf("mkdir -p /data/%s && minio server --certs-dir %s/certs --address :%v --console-address :%v /data", bktName, f.InternalDir(), httpsPort, consolePort),
	}

	minio := e2emon.AsInstrumented(f.Init(e2e.StartOptions{
		Image: image,
		// Create the required bucket before starting minio.
		Command:   e2e.NewCommandWithoutEntrypoint("sh", "-c", strings.Join(commands, " && ")),
		Readiness: e2e.NewHTTPSReadinessProbe("console", "/", 200, 200),
		EnvVars: map[string]string{
			"MINIO_ROOT_USER":     e2edb.MinioAccessKey,
			"MINIO_ROOT_PASSWORD": e2edb.MinioSecretKey,
			"MINIO_BROWSER":       "on",
			"ENABLE_HTTPS":        "1",
			// https://docs.min.io/docs/minio-kms-quickstart-guide.html
			"MINIO_KMS_KES_ENDPOINT":  "https://play.min.io:7373",
			"MINIO_KMS_KES_KEY_FILE":  "root.key",
			"MINIO_KMS_KES_CERT_FILE": "root.cert",
			"MINIO_KMS_KES_KEY_NAME":  "my-minio-key",
		},
	}), "https")
	return minio
}

func NewMemcached(e e2e.Environment, name string) *e2emon.InstrumentedRunnable {
	return e2emon.AsInstrumented(e.Runnable(fmt.Sprintf("memcached-%s", name)).
		WithPorts(map[string]int{"memcached": 11211}).
		Init(e2e.StartOptions{
			Image:            "docker.io/memcached:1.6.3-alpine",
			Command:          e2e.NewCommand("memcached", []string{"-m 1024", "-I 1m", "-c 1024", "-v"}...),
			User:             strconv.Itoa(os.Getuid()),
			WaitReadyBackoff: &defaultBackoffConfig,
		}), "memcached")
}

func NewToolsBucketWeb(
	e e2e.Environment,
	name string,
	bucketConfig client.BucketConfig,
	routePrefix,
	externalPrefix string,
	minTime string,
	maxTime string,
	relabelConfig string,
) *e2emon.InstrumentedRunnable {
	bktConfigBytes, err := yaml.Marshal(bucketConfig)
	if err != nil {
		return &e2emon.InstrumentedRunnable{Runnable: e2e.NewFailedRunnable(name, errors.Wrapf(err, "generate tools bucket web config file: %v", bucketConfig))}
	}

	f := e.Runnable(fmt.Sprintf("toolsBucketWeb-%s", name)).
		WithPorts(map[string]int{"http": 8080, "grpc": 9091}).
		Future()

	args := e2e.BuildArgs(map[string]string{
		"--debug.name":      fmt.Sprintf("toolsBucketWeb-%s", name),
		"--http-address":    ":8080",
		"--log.level":       infoLogLevel,
		"--objstore.config": string(bktConfigBytes),
	})
	if routePrefix != "" {
		args = append(args, "--web.route-prefix="+routePrefix)
	}

	if externalPrefix != "" {
		args = append(args, "--web.external-prefix="+externalPrefix)
	}

	if minTime != "" {
		args = append(args, "--min-time="+minTime)
	}

	if maxTime != "" {
		args = append(args, "--max-time="+maxTime)
	}

	if relabelConfig != "" {
		args = append(args, "--selector.relabel-config="+relabelConfig)
	}

	args = append([]string{"bucket", "web"}, args...)

	return e2emon.AsInstrumented(f.Init(wrapWithDefaults(e2e.StartOptions{
		Image:     DefaultImage(),
		Command:   e2e.NewCommand("tools", args...),
		Readiness: e2e.NewHTTPReadinessProbe("http", "/-/ready", 200, 200),
	})), "http")
}

// genCerts generates certificates and writes those to the provided paths.
func genCerts(certPath, privkeyPath, caPath, serverName string) error {
	var caRoot = &x509.Certificate{
		SerialNumber:          big.NewInt(2019),
		NotAfter:              time.Now().AddDate(10, 0, 0),
		IsCA:                  true,
		ExtKeyUsage:           []x509.ExtKeyUsage{x509.ExtKeyUsageClientAuth, x509.ExtKeyUsageServerAuth},
		KeyUsage:              x509.KeyUsageDigitalSignature | x509.KeyUsageCertSign,
		BasicConstraintsValid: true,
	}

	var cert = &x509.Certificate{
		SerialNumber: big.NewInt(1658),
		DNSNames:     []string{serverName},
		IPAddresses:  []net.IP{net.ParseIP("127.0.0.1"), net.ParseIP("::1")},
		NotAfter:     time.Now().AddDate(10, 0, 0),
		SubjectKeyId: []byte{1, 2, 3},
		ExtKeyUsage:  []x509.ExtKeyUsage{x509.ExtKeyUsageClientAuth, x509.ExtKeyUsageServerAuth},
		KeyUsage:     x509.KeyUsageDigitalSignature,
	}

	caPrivKey, err := rsa.GenerateKey(rand.Reader, 2048)
	if err != nil {
		return err
	}

	certPrivKey, err := rsa.GenerateKey(rand.Reader, 2048)
	if err != nil {
		return err
	}
	// Generate CA cert.
	caBytes, err := x509.CreateCertificate(rand.Reader, caRoot, caRoot, &caPrivKey.PublicKey, caPrivKey)
	if err != nil {
		return err
	}
	caPEM := pem.EncodeToMemory(&pem.Block{
		Type:  "CERTIFICATE",
		Bytes: caBytes,
	})
	err = os.WriteFile(caPath, caPEM, 0644)
	if err != nil {
		return err
	}

	// Sign the cert with the CA private key.
	certBytes, err := x509.CreateCertificate(rand.Reader, cert, caRoot, &certPrivKey.PublicKey, caPrivKey)
	if err != nil {
		return err
	}
	certPEM := pem.EncodeToMemory(&pem.Block{
		Type:  "CERTIFICATE",
		Bytes: certBytes,
	})
	err = os.WriteFile(certPath, certPEM, 0644)
	if err != nil {
		return err
	}

	certPrivKeyPEM := pem.EncodeToMemory(&pem.Block{
		Type:  "RSA PRIVATE KEY",
		Bytes: x509.MarshalPKCS1PrivateKey(certPrivKey),
	})
	err = os.WriteFile(privkeyPath, certPrivKeyPEM, 0644)
	if err != nil {
		return err
	}

	return nil
}

func NewS3Config(bucket, endpoint, basePath string) s3.Config {
	return s3.Config{
		Bucket:    bucket,
		AccessKey: e2edb.MinioAccessKey,
		SecretKey: e2edb.MinioSecretKey,
		Endpoint:  endpoint,
		Insecure:  false,
		HTTPConfig: exthttp.HTTPConfig{
			TLSConfig: exthttp.TLSConfig{
				CAFile:   filepath.Join(basePath, "certs", "CAs", "ca.crt"),
				CertFile: filepath.Join(basePath, "certs", "public.crt"),
				KeyFile:  filepath.Join(basePath, "certs", "private.key"),
			},
		},
		BucketLookupType: s3.AutoLookup,
	}
}

// NOTE: by using aggregation all results are now unsorted.
var QueryUpWithoutInstance = func() string { return "sum(up) without (instance)" }

// LocalPrometheusTarget is a constant to be used in the Prometheus config if you
// wish to enable Prometheus to scrape itself in a test.
const LocalPrometheusTarget = "localhost:9090"

// DefaultPromConfig returns Prometheus config that sets Prometheus to:
// * expose 2 external labels, source and replica.
// * optionallly scrape self. This will produce up == 0 metric which we can assert on.
// * optionally remote write endpoint to write into.
func DefaultPromConfig(name string, replica int, remoteWriteEndpoint, ruleFile string, scrapeTargets ...string) string {
	var targets string
	if len(scrapeTargets) > 0 {
		targets = strings.Join(scrapeTargets, ",")
	}

	config := fmt.Sprintf(`
global:
  external_labels:
    prometheus: %v
    replica: %v
`, name, replica)

	if targets != "" {
		config = fmt.Sprintf(`
%s
scrape_configs:
- job_name: 'myself'
  # Quick scrapes for test purposes.
  scrape_interval: 1s
  scrape_timeout: 1s
  static_configs:
  - targets: [%s]
  relabel_configs:
  - source_labels: ['__address__']
    regex: '^.+:80$'
    action: drop
`, config, targets)
	}

	if remoteWriteEndpoint != "" {
		config = fmt.Sprintf(`
%s
remote_write:
- url: "%s"
  # Don't spam receiver on mistake.
  queue_config:
    min_backoff: 2s
    max_backoff: 10s
`, config, remoteWriteEndpoint)
	}

	if ruleFile != "" {
		config = fmt.Sprintf(`
%s
rule_files:
-  "%s"
`, config, ruleFile)
	}

	return config
}
```

## File: `tracing/tracing.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package tracing

const (
	// ForceTracingBaggageKey is a request header name that forces tracing sampling.
	ForceTracingBaggageKey = "X-Thanos-Force-Tracing"
)
```

## File: `tracing/opentelemetry/opentelemetry.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package opentelemetry

import (
	"context"
	"io"

	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/trace"

	"github.com/thanos-io/objstore"
)

// TracingBucket is a wrapper around objstore.Bucket that adds tracing to all operations using OpenTelemetry.
type TracingBucket struct {
	tracer trace.Tracer
	bkt    objstore.Bucket
}

func WrapWithTraces(bkt objstore.Bucket, tracer trace.Tracer) objstore.InstrumentedBucket {
	return TracingBucket{tracer: tracer, bkt: bkt}
}

func (t TracingBucket) Provider() objstore.ObjProvider { return t.bkt.Provider() }

func (t TracingBucket) Iter(ctx context.Context, dir string, f func(string) error, options ...objstore.IterOption) (err error) {
	ctx, span := t.tracer.Start(ctx, "bucket_iter")
	defer span.End()
	span.SetAttributes(attribute.String("dir", dir))

	defer func() {
		if err != nil {
			span.RecordError(err)
		}
	}()
	return t.bkt.Iter(ctx, dir, f, options...)
}

func (t TracingBucket) IterWithAttributes(ctx context.Context, dir string, f func(attrs objstore.IterObjectAttributes) error, options ...objstore.IterOption) (err error) {
	ctx, span := t.tracer.Start(ctx, "bucket_iter_with_attrs")
	defer span.End()
	span.SetAttributes(attribute.String("dir", dir))

	defer func() {
		if err != nil {
			span.RecordError(err)
		}
	}()
	return t.bkt.IterWithAttributes(ctx, dir, f, options...)
}

// SupportedIterOptions returns a list of supported IterOptions by the underlying provider.
func (t TracingBucket) SupportedIterOptions() []objstore.IterOptionType {
	return t.bkt.SupportedIterOptions()
}

func (t TracingBucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	ctx, span := t.tracer.Start(ctx, "bucket_get")
	defer span.End()
	span.SetAttributes(attribute.String("name", name))

	r, err := t.bkt.Get(ctx, name)
	if err != nil {
		span.RecordError(err)
		return nil, err
	}

	return newTracingReadCloser(r, span), nil
}

func (t TracingBucket) GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	ctx, span := t.tracer.Start(ctx, "bucket_getrange")
	defer span.End()
	span.SetAttributes(attribute.String("name", name), attribute.Int64("offset", off), attribute.Int64("length", length))

	r, err := t.bkt.GetRange(ctx, name, off, length)
	if err != nil {
		span.RecordError(err)
		return nil, err
	}

	return newTracingReadCloser(r, span), nil
}

func (t TracingBucket) Exists(ctx context.Context, name string) (_ bool, err error) {
	ctx, span := t.tracer.Start(ctx, "bucket_exists")
	defer span.End()
	span.SetAttributes(attribute.String("name", name))

	defer func() {
		if err != nil {
			span.RecordError(err)
		}
	}()
	return t.bkt.Exists(ctx, name)
}

func (t TracingBucket) Attributes(ctx context.Context, name string) (_ objstore.ObjectAttributes, err error) {
	ctx, span := t.tracer.Start(ctx, "bucket_attributes")
	defer span.End()
	span.SetAttributes(attribute.String("name", name))

	defer func() {
		if err != nil {
			span.RecordError(err)
		}
	}()
	return t.bkt.Attributes(ctx, name)
}

func (t TracingBucket) Upload(ctx context.Context, name string, r io.Reader, opts ...objstore.ObjectUploadOption) (err error) {
	ctx, span := t.tracer.Start(ctx, "bucket_upload")
	defer span.End()
	span.SetAttributes(attribute.String("name", name))

	defer func() {
		if err != nil {
			span.RecordError(err)
		}
	}()
	return t.bkt.Upload(ctx, name, r, opts...)
}

func (t TracingBucket) Delete(ctx context.Context, name string) (err error) {
	ctx, span := t.tracer.Start(ctx, "bucket_delete")
	defer span.End()
	span.SetAttributes(attribute.String("name", name))

	defer func() {
		if err != nil {
			span.RecordError(err)
		}
	}()
	return t.bkt.Delete(ctx, name)
}

func (t TracingBucket) Name() string {
	return "tracing: " + t.bkt.Name()
}

func (t TracingBucket) Close() error {
	return t.bkt.Close()
}

func (t TracingBucket) IsObjNotFoundErr(err error) bool {
	return t.bkt.IsObjNotFoundErr(err)
}

func (t TracingBucket) IsAccessDeniedErr(err error) bool {
	return t.bkt.IsAccessDeniedErr(err)
}

func (t TracingBucket) WithExpectedErrs(expectedFunc objstore.IsOpFailureExpectedFunc) objstore.Bucket {
	if ib, ok := t.bkt.(objstore.InstrumentedBucket); ok {
		return TracingBucket{tracer: t.tracer, bkt: ib.WithExpectedErrs(expectedFunc)}
	}
	return t
}

func (t TracingBucket) ReaderWithExpectedErrs(expectedFunc objstore.IsOpFailureExpectedFunc) objstore.BucketReader {
	return t.WithExpectedErrs(expectedFunc)
}

type tracingReadCloser struct {
	r io.ReadCloser
	s trace.Span

	objSize    int64
	objSizeErr error

	read int
}

func newTracingReadCloser(r io.ReadCloser, span trace.Span) io.ReadCloser {
	// Since TryToGetSize can only reliably return size before doing any read calls,
	// we call during "construction" and remember the results.
	objSize, objSizeErr := objstore.TryToGetSize(r)

	return &tracingReadCloser{r: r, s: span, objSize: objSize, objSizeErr: objSizeErr}
}

func (t *tracingReadCloser) ObjectSize() (int64, error) {
	return t.objSize, t.objSizeErr
}

func (t *tracingReadCloser) Read(p []byte) (int, error) {
	n, err := t.r.Read(p)
	if n > 0 {
		t.read += n
	}
	if err != nil && err != io.EOF && t.s != nil {
		t.s.RecordError(err)
	}
	return n, err
}

func (t *tracingReadCloser) Close() error {
	err := t.r.Close()
	if t.s != nil {
		t.s.SetAttributes(attribute.Int64("read", int64(t.read)))
		if err != nil {
			t.s.SetAttributes(attribute.String("close_err", err.Error()))
		}
		t.s.End()
		t.s = nil
	}
	return err
}
```

## File: `tracing/opentracing/opentracing.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package opentracing

import (
	"context"
	"io"

	"github.com/opentracing/opentracing-go"

	"github.com/thanos-io/objstore"
)

type contextKey struct{}

var tracerKey = contextKey{}

// Tracer interface to provide GetTraceIDFromSpanContext method.
type Tracer interface {
	GetTraceIDFromSpanContext(ctx opentracing.SpanContext) (string, bool)
}

// ContextWithTracer returns a new `context.Context` that holds a reference to given opentracing.Tracer.
func ContextWithTracer(ctx context.Context, tracer opentracing.Tracer) context.Context {
	return context.WithValue(ctx, tracerKey, tracer)
}

// TracerFromContext extracts opentracing.Tracer from the given context.
func TracerFromContext(ctx context.Context) opentracing.Tracer {
	val := ctx.Value(tracerKey)
	if sp, ok := val.(opentracing.Tracer); ok {
		return sp
	}
	return nil
}

// TracingBucket includes bucket operations in the traces.
type TracingBucket struct {
	bkt objstore.Bucket
}

func WrapWithTraces(bkt objstore.Bucket) objstore.InstrumentedBucket {
	return TracingBucket{bkt: bkt}
}

func (t TracingBucket) Provider() objstore.ObjProvider { return t.bkt.Provider() }

func (t TracingBucket) Iter(ctx context.Context, dir string, f func(string) error, options ...objstore.IterOption) (err error) {
	doWithSpan(ctx, "bucket_iter", func(spanCtx context.Context, span opentracing.Span) {
		span.LogKV("dir", dir)
		err = t.bkt.Iter(spanCtx, dir, f, options...)
	})
	return
}

func (t TracingBucket) IterWithAttributes(ctx context.Context, dir string, f func(attrs objstore.IterObjectAttributes) error, options ...objstore.IterOption) (err error) {
	doWithSpan(ctx, "bucket_iter_with_attrs", func(spanCtx context.Context, span opentracing.Span) {
		span.LogKV("dir", dir)
		err = t.bkt.IterWithAttributes(spanCtx, dir, f, options...)
	})
	return
}

func (t TracingBucket) SupportedIterOptions() []objstore.IterOptionType {
	return t.bkt.SupportedIterOptions()
}

func (t TracingBucket) Get(ctx context.Context, name string) (io.ReadCloser, error) {
	span, spanCtx := startSpan(ctx, "bucket_get")
	span.LogKV("name", name)

	r, err := t.bkt.Get(spanCtx, name)
	if err != nil {
		span.LogKV("err", err)
		span.Finish()
		return nil, err
	}

	return newTracingReadCloser(r, span), nil
}

func (t TracingBucket) GetRange(ctx context.Context, name string, off, length int64) (io.ReadCloser, error) {
	span, spanCtx := startSpan(ctx, "bucket_getrange")
	span.LogKV("name", name, "offset", off, "length", length)

	r, err := t.bkt.GetRange(spanCtx, name, off, length)
	if err != nil {
		span.LogKV("err", err)
		span.Finish()
		return nil, err
	}

	return newTracingReadCloser(r, span), nil
}

func (t TracingBucket) Exists(ctx context.Context, name string) (exists bool, err error) {
	doWithSpan(ctx, "bucket_exists", func(spanCtx context.Context, span opentracing.Span) {
		span.LogKV("name", name)
		exists, err = t.bkt.Exists(spanCtx, name)
	})
	return
}

func (t TracingBucket) Attributes(ctx context.Context, name string) (attrs objstore.ObjectAttributes, err error) {
	doWithSpan(ctx, "bucket_attributes", func(spanCtx context.Context, span opentracing.Span) {
		span.LogKV("name", name)
		attrs, err = t.bkt.Attributes(spanCtx, name)
	})
	return
}

func (t TracingBucket) Upload(ctx context.Context, name string, r io.Reader, opts ...objstore.ObjectUploadOption) (err error) {
	doWithSpan(ctx, "bucket_upload", func(spanCtx context.Context, span opentracing.Span) {
		span.LogKV("name", name)
		err = t.bkt.Upload(spanCtx, name, r, opts...)
	})
	return
}

func (t TracingBucket) Delete(ctx context.Context, name string) (err error) {
	doWithSpan(ctx, "bucket_delete", func(spanCtx context.Context, span opentracing.Span) {
		span.LogKV("name", name)
		err = t.bkt.Delete(spanCtx, name)
	})
	return
}

func (t TracingBucket) Name() string {
	return "tracing: " + t.bkt.Name()
}

func (t TracingBucket) Close() error {
	return t.bkt.Close()
}

func (t TracingBucket) IsObjNotFoundErr(err error) bool {
	return t.bkt.IsObjNotFoundErr(err)
}

func (t TracingBucket) IsAccessDeniedErr(err error) bool {
	return t.bkt.IsAccessDeniedErr(err)
}

func (t TracingBucket) WithExpectedErrs(expectedFunc objstore.IsOpFailureExpectedFunc) objstore.Bucket {
	if ib, ok := t.bkt.(objstore.InstrumentedBucket); ok {
		return TracingBucket{bkt: ib.WithExpectedErrs(expectedFunc)}
	}
	return t
}

func (t TracingBucket) ReaderWithExpectedErrs(expectedFunc objstore.IsOpFailureExpectedFunc) objstore.BucketReader {
	return t.WithExpectedErrs(expectedFunc)
}

type tracingReadCloser struct {
	r io.ReadCloser
	s opentracing.Span

	objSize    int64
	objSizeErr error

	read int
}

func newTracingReadCloser(r io.ReadCloser, span opentracing.Span) io.ReadCloser {
	// Since TryToGetSize can only reliably return size before doing any read calls,
	// we call during "construction" and remember the results.
	objSize, objSizeErr := objstore.TryToGetSize(r)

	return &tracingReadCloser{r: r, s: span, objSize: objSize, objSizeErr: objSizeErr}
}

func (t *tracingReadCloser) ObjectSize() (int64, error) {
	return t.objSize, t.objSizeErr
}

func (t *tracingReadCloser) Read(p []byte) (int, error) {
	n, err := t.r.Read(p)
	if n > 0 {
		t.read += n
	}
	if err != nil && err != io.EOF && t.s != nil {
		t.s.LogKV("err", err)
	}
	return n, err
}

func (t *tracingReadCloser) Close() error {
	err := t.r.Close()
	if t.s != nil {
		t.s.LogKV("read", t.read)
		if err != nil {
			t.s.LogKV("close err", err)
		}
		t.s.Finish()
		t.s = nil
	}
	return err
}

// Aliases to avoid spreading opentracing package to Thanos code.
type Tag = opentracing.Tag
type Tags = opentracing.Tags
type Span = opentracing.Span

// startSpan starts and returns span with `operationName` and hooking as child to a span found within given context if any.
// It uses opentracing.Tracer propagated in context. If no found, it uses noop tracer without notification.
func startSpan(ctx context.Context, operationName string, opts ...opentracing.StartSpanOption) (Span, context.Context) {
	tracer := TracerFromContext(ctx)
	if tracer == nil {
		// No tracing found, return noop span.
		return opentracing.NoopTracer{}.StartSpan(operationName), ctx
	}

	var span Span
	if parentSpan := opentracing.SpanFromContext(ctx); parentSpan != nil {
		opts = append(opts, opentracing.ChildOf(parentSpan.Context()))
	}
	span = tracer.StartSpan(operationName, opts...)
	return span, opentracing.ContextWithSpan(ctx, span)
}

// doWithSpan executes function doFn inside new span with `operationName` name and hooking as child to a span found within given context if any.
// It uses opentracing.Tracer propagated in context. If no found, it uses noop tracer notification.
func doWithSpan(ctx context.Context, operationName string, doFn func(context.Context, Span), _ ...opentracing.StartSpanOption) {
	span, newCtx := startSpan(ctx, operationName)
	defer span.Finish()
	doFn(newCtx, span)
}
```

## File: `tracing/opentracing/opentracing_test.go`
```go
// Copyright (c) The Thanos Authors.
// Licensed under the Apache License 2.0.

package opentracing

import (
	"bytes"
	"io"
	"testing"

	"github.com/efficientgo/core/testutil"
	"github.com/thanos-io/objstore"
)

func TestTracingReader(t *testing.T) {
	r := bytes.NewReader([]byte("hello world"))
	tr := newTracingReadCloser(objstore.NopCloserWithSize(r), nil)

	size, err := objstore.TryToGetSize(tr)

	testutil.Ok(t, err)
	testutil.Equals(t, int64(11), size)

	smallBuf := make([]byte, 4)
	n, err := io.ReadFull(tr, smallBuf)
	testutil.Ok(t, err)
	testutil.Equals(t, 4, n)

	// Verify that size is still the same, after reading 4 bytes.
	size, err = objstore.TryToGetSize(tr)

	testutil.Ok(t, err)
	testutil.Equals(t, int64(11), size)
}
```

